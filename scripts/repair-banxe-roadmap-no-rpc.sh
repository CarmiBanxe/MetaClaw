#!/usr/bin/env bash
set -Eeuo pipefail

EVO1_HOST="evo1"
EVO2_HOST="evo2"
EVO1_IP="192.168.0.72"
EVO2_IP="192.168.0.73"
LEGION_IP="192.168.0.75"

EVO1_KEY="sk-banxe-evo1-local-2026"
EVO2_KEY="sk-banxe-evo2-local-2026"
GATEWAY_KEY="sk-banxe-llm-gateway-2026-93173fc9dc7ef1dcb02daf7698d04a31"
CODING_KEY="sk-legion-coding-2026"

LOG_DIR="${HOME}/audit-banxe-$(date +%F-%H%M%S)"
mkdir -p "$LOG_DIR"

log() { printf '\n\033[1;36m[%s]\033[0m %s\n' "$(date +%H:%M:%S)" "$*"; }
run_remote() { local host="$1"; shift; ssh -o BatchMode=yes "$host" "$@"; }

log "0. Preflight"
hostname | tee "$LOG_DIR/hostname.txt"
pwd | tee "$LOG_DIR/pwd.txt"
python3 --version | tee "$LOG_DIR/python-version.txt"
ip -4 -br addr show | tee "$LOG_DIR/legion-ip.txt"

log "1. EVO1/EVO2 reachability"
for host in "$EVO1_HOST" "$EVO2_HOST"; do
  {
    echo "=== $host ==="
    ping -c 2 "$host" || true
    ssh -o BatchMode=yes "$host" 'hostname; whoami; hostname -I'
  } | tee -a "$LOG_DIR/reachability.txt"
done

log "2. Ensure Ollama installed on EVO1/EVO2"
for host in "$EVO1_HOST" "$EVO2_HOST"; do
  run_remote "$host" '
    set -e
    if ! command -v ollama >/dev/null 2>&1; then
      curl -fsSL https://ollama.com/install.sh | sh
    fi
    command -v ollama
    ollama --version || true
    sudo mkdir -p /etc/systemd/system/ollama.service.d
  ' | tee -a "$LOG_DIR/ollama-install.txt"
done

log "3. Configure EVO1 Ollama"
run_remote "$EVO1_HOST" "sudo tee /etc/systemd/system/ollama.service.d/override.conf >/dev/null <<EOF
[Service]
Environment=OLLAMA_HOST=0.0.0.0:11434
Environment=HSA_OVERRIDE_GFX_VERSION=11.5.1
Environment=OLLAMA_MODELS=/data/ollama-models
Environment=OLLAMA_VULKAN=1
Environment=OLLAMA_LLM_LIBRARY=vulkan
Environment=OLLAMA_FLASH_ATTENTION=1
Environment=OLLAMA_CONTEXT_LENGTH=131072
Environment=OLLAMA_NUM_PARALLEL=2
Environment=OLLAMA_API_KEY=${EVO1_KEY}
Environment=OLLAMA_KEEP_ALIVE=10m
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now ollama
sudo systemctl restart ollama
sleep 5
systemctl status ollama --no-pager | head -20
ss -tlnp | grep 11434 || true
" | tee "$LOG_DIR/evo1-ollama-status.txt"

log "4. Configure EVO2 Ollama"
run_remote "$EVO2_HOST" "sudo tee /etc/systemd/system/ollama.service.d/override.conf >/dev/null <<EOF
[Service]
Environment=OLLAMA_HOST=0.0.0.0:11434
Environment=HSA_OVERRIDE_GFX_VERSION=11.5.1
Environment=OLLAMA_MODELS=/data/ollama-models
Environment=OLLAMA_VULKAN=1
Environment=OLLAMA_LLM_LIBRARY=vulkan
Environment=OLLAMA_FLASH_ATTENTION=1
Environment=OLLAMA_CONTEXT_LENGTH=131072
Environment=OLLAMA_NUM_PARALLEL=2
Environment=OLLAMA_API_KEY=${EVO2_KEY}
Environment=OLLAMA_KEEP_ALIVE=10m
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now ollama
sudo systemctl restart ollama
sleep 5
systemctl status ollama --no-pager | head -20
ss -tlnp | grep 11434 || true
" | tee "$LOG_DIR/evo2-ollama-status.txt"

log "5. Ollama API smoke tests"
curl -fsS "http://${EVO1_IP}:11434/api/tags" -H "Authorization: Bearer ${EVO1_KEY}" > "$LOG_DIR/evo1-tags.json"
curl -fsS "http://${EVO2_IP}:11434/api/tags" -H "Authorization: Bearer ${EVO2_KEY}" > "$LOG_DIR/evo2-tags.json"

log "6. Write LiteLLM config for working backends only"
mkdir -p "${HOME}/litellm"
cp -f "${HOME}/litellm/litellmconfig.yaml" "${HOME}/litellm/litellmconfig.yaml.bak.$(date +%F-%H%M%S)" 2>/dev/null || true

cat > "${HOME}/litellm/litellmconfig.yaml" <<EOF
model_list:
  - model_name: banxe-general
    litellm_params:
      model: ollama/qwen3:30b-a3b
      api_base: http://${EVO1_IP}:11434
      api_key: ${EVO1_KEY}
      timeout: 120

  - model_name: banxe-general
    litellm_params:
      model: ollama/qwen3:30b-a3b
      api_base: http://${EVO2_IP}:11434
      api_key: ${EVO2_KEY}
      timeout: 120

  - model_name: fast
    litellm_params:
      model: ollama/huihui_ai/glm-4.7-flash-abliterated:latest
      api_base: http://${EVO1_IP}:11434
      api_key: ${EVO1_KEY}
      timeout: 120

  - model_name: fast
    litellm_params:
      model: ollama/huihui_ai/glm-4.7-flash-abliterated:latest
      api_base: http://${EVO2_IP}:11434
      api_key: ${EVO2_KEY}
      timeout: 120

router_settings:
  routing_strategy: latency-based-routing
  num_retries: 2
  timeout: 120
  retry_after: 5

general_settings:
  master_key: ${GATEWAY_KEY}
EOF

log "7. Start LiteLLM directly"
python3 -m pip install -U litellm litellm[proxy]
pkill -f 'litellm.*--port 4000' || true
nohup "$(command -v litellm)" --config "${HOME}/litellm/litellmconfig.yaml" --port 4000 --host 0.0.0.0 > "$LOG_DIR/litellm.log" 2>&1 &
sleep 8
curl -fsS http://127.0.0.1:4000/models -H "Authorization: Bearer ${GATEWAY_KEY}" > "$LOG_DIR/litellm-models.json"

log "8. Summary"
{
  curl -s -o /dev/null -w "EVO1 tags HTTP %{http_code}\n" -H "Authorization: Bearer ${EVO1_KEY}" "http://${EVO1_IP}:11434/api/tags" || true
  curl -s -o /dev/null -w "EVO2 tags HTTP %{http_code}\n" -H "Authorization: Bearer ${EVO2_KEY}" "http://${EVO2_IP}:11434/api/tags" || true
  curl -s -o /dev/null -w "LiteLLM models HTTP %{http_code}\n" -H "Authorization: Bearer ${GATEWAY_KEY}" "http://127.0.0.1:4000/models" || true
  echo "RPC stage: SKIPPED/BLOCKED due to confirmed ggml-vulkan spv compile failure"
} | tee "$LOG_DIR/final-summary.txt"

echo "DONE LOG_DIR=$LOG_DIR"
