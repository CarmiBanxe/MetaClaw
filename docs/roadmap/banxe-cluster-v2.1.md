# BANXE AI Cluster — Roadmap v2.1
Date: 2026-05-01 · Author: Moriel Carmi · Status: COMMITTED

## 0. Topology snapshot (01.05.2026)

| Node | Hostname | LAN IP | Tailscale | Role | Notes |
|---|---|---|---|---|---|
| EVO-X2 #1 | banxe-NucBox-EVO-X2 | 192.168.0.72 | 100.68.102.48 | Prod Ollama | Vulkan, gfx1151, FA pending, ROCm fix pending |
| EVO-X2 #2 | TBD | 192.168.0.15 | not-yet-joined | Fresh Ubuntu 24.04 | openssh-server not installed (S0 blocker) |
| Legion    | mark-legion         | 192.168.0.75 (NAT) | 100.101.218.26 | LiteLLM gateway + Coding (RTX 4090) | WSL2 |

## 1. Conventions

- Per-node Ollama API keys: sk-banxe-evo{1,2}-local-2026
- LiteLLM gateway master key: sk-banxe-llm-gateway-2026
- Coding server (Legion llama.cpp): sk-legion-coding-2026
- RPC GLM-4.7 distributed: sk-rpc-glm47-2026
- Models dir on EVO-X2 nodes: /data/ollama-models
- llama.cpp build dir on EVO-X2 nodes: /data/llama-cpp
- SSH ports: EVO-X2 #1 = 2222, EVO-X2 #2 target = 2222 (initially 22)

## 2. Sprints

### S0 — Discovery & Connectivity
Establish full passwordless SSH from Legion to evo1/evo2; resolve EVO-X2 #2 IP; stop rogue mmber auto-login on Legion; build a 3x3 visibility matrix.

### S0b — EVO-X2 #2 SSH+Tailscale bootstrap (manual one-touch)
One physical-console action on EVO-X2 #2 to install openssh-server + Tailscale. Node joins the tailnet under hostname banxe-nucbox-evo-x2-2. After this single touch, all further operations move into Claude Code on Legion.

### S1 — EVO-X2 #1 hotfix (no downtime)
override.conf with FlashAttention=1, ctx 131072, NUM_PARALLEL=2, KEEP_ALIVE=10m, OLLAMA_API_KEY=sk-banxe-evo1-local-2026. ROCm fix prep (usermod -aG render,video). GRUB GTT (amdgpu.ppfeaturemask=0xffffffff, ttm.pages_limit=31457280). Security updates without kernel. Bench qwen3:30b-a3b target 13-17 toks/s.

### S2 — EVO-X2 #2 bring-up
Mirror EVO-X2 #1 stack: SSH on 2222, ufw 2222/11434/50052, /data/{ollama-models,models,llama-cpp}, GRUB GTT, Ollama install + override.conf with sk-banxe-evo2-local-2026, rsync /data/ollama-models from #1 (qwen3:30b-a3b, glm-4.7-flash, qwen3-coder-next:q4_K_M), reboot, post-reboot verification (rocminfo gfx1151, Ollama Vulkan, /api/tags).

### S3 — Legion coding model (Qwen3-Coder-Next 80B, llama.cpp+CUDA)
Build llama.cpp with GGML_CUDA + CMAKE_CUDA_ARCHITECTURES=89 + LLAMA_CURL + GGML_RPC. Download Qwen3-Coder-Next-UD-Q4_K_XL.gguf into ~/models/. Run llama-server on :8080 with --n-gpu-layers 999, --override-tensor '.*ff.*=CPU', --flash-attn, ctx 65536, key sk-legion-coding-2026. systemd unit qwen3-coder.service. Continue.dev wiring (~/.continue/config.json) with two providers. Target 25-35 toks/s.

### S4 — LiteLLM Gateway upgrade
New litellm-config.yaml with: load-balanced banxe-general/fast across both EVO-X2 nodes; coding (Legion primary, EVO-X2 #1 fallback weight 0.2); gpt-oss-20b on EVO-X2 #1; large stub for RPC. router_settings: latency-based-routing, num_retries=2, timeout=120, retry_after=5; fallbacks coding→qwen3-30b, banxe-general→fast. Redis cache 192.168.0.72:6379, namespace banxe-litellm. Prometheus callbacks. Master key sk-banxe-llm-gateway-2026. Port 4000.

### S5 — Distributed inference llama.cpp RPC
USB4/Thunderbolt link 10.0.0.1/30 (EVO-X2 #1 master) ↔ 10.0.0.2/30 (EVO-X2 #2 worker). Build llama.cpp on both EVO-X2 with GGML_RPC + GGML_VULKAN. systemd llama-rpc-worker on EVO-X2 #2:50052 (vulkan backend). GLM-4.7-GGUF Q4_K_M (~190 GiB) on EVO-X2 #2. Master llama-server on EVO-X2 #1:8081 with key sk-rpc-glm47-2026, ctx 32768, FA. Wire LiteLLM `large`. Target 7-8 toks/s.

### S6 — Production Hardening (ongoing)
Prometheus + Grafana (Docker on EVO-X2 #2 or Legion). prometheus.yml jobs: litellm@4000, ollama-evo1@11434, ollama-evo2@11434. ~/check-llm-cluster.sh + cron 5min → /var/log/llm-cluster-health.log. Reboot plan for EVO-X2 #1 (LB+fallback). Close public 2222/tcp on EVO-X2 #1 (router port-forward off OR ufw allow from 192.168.0.0/24 only). Tailscale ACL update for cross-node SSH.

## 3. KPIs

- EVO-X2 cluster throughput: 67 → 130+ toks/s (load-balance ×2)
- Coding: 13-17 → 25-35 toks/s (Legion CUDA Qwen3-Coder-Next 80B)
- Per-node API key (no more `anything`)
- 190 GiB models via RPC; GLM-4.7 full 355B as `large`, target 7-8 toks/s

## 4. Canon (operating rules)

- Work from Legion; switch machines via SSH from Legion, not by physically logging into them.
- Use Claude Code on Legion for sprint-sized prompts; one sprint = one prompt = one JSON report.
- One command at a time → real output → next command. Big composite ops are split into dependent sub-commands so output is never truncated.
- Safe commands auto-execute (no questions). Unsafe (reboot, rm -rf, mkfs, partition, public firewall changes, force push) require one explicit confirm.
- All deviations recorded in the sprint's JSON report under `deviations`.

## 5. Sprint S0 — execution report (PARTIAL PASS)

- EVO-X2 #2 IP resolved: 192.168.0.15, MAC 84:47:09:88:7a:82, mDNS device-1914.home.
- Rogue mmber auto-login on EVO-X2 #1: root cause = WSL2 systemd-user unit openclaw-tunnel-gmktec.service on Legion (Restart=always, RestartSec=10). Stopped + disabled. evo1 sshd journal silent for 394s (>> 60s gate).
- Legion ~/.ssh/config rewritten (backup .bak.20260501): added evo1 (banxe@192.168.0.72:2222), evo2 (banxe@192.168.0.15:22 placeholder), removed broken `Host gmktec` (User=root and User=mmber).
- Visibility 3x3: Legion↔evo1 PASS (ICMP+SSH); Legion→evo2 ICMP PASS / SSH FAIL (no sshd); evo1→evo2 ICMP PASS / SSH FAIL; evo2-as-source N/A pending S0b.
- Security debt recorded (out of S0 scope): EVO-X2 #1 tcp/2222 reachable from public internet, brute-force from 185.214.135.211, 185.2.101.118, 47.77.182.54.
- Status: PARTIAL PASS. Hard blocker: S0b requires one physical-console action on EVO-X2 #2.

## 6. Open items

- S0b: physical one-touch on EVO-X2 #2 to install openssh-server + Tailscale.
- S1 can proceed independently (no dependency on EVO-X2 #2).
- Tailscale tailnet ACL: enable cross-node SSH for users banxe/mmber (currently restricted).
- Close public 2222/tcp on EVO-X2 #1 (S6).

## 7. Sprint S1 — execution report (PASS)

- override.conf rewritten to canonical block (11 Environment= entries). Backup: `/etc/systemd/system/ollama.service.d/override.conf.bak.20260501`.
- Single planned downtime: ~8 s on `systemctl restart ollama`.
- Ollama 0.20.7 active; Vulkan iGPU pool total=154.0 GiB, available=153.8 GiB. FlashAttention=Enabled, OLLAMA_CONTEXT_LENGTH=131072, OLLAMA_NUM_PARALLEL=2, OLLAMA_KEEP_ALIVE=10m, API key sk-banxe-evo1-local-2026.
- Bench qwen3:30b-a3b from Legion: S1.4 short prompt 36.90 toks/s; S1.7 200-tok 36.95 toks/s. Roadmap target was 13–17 toks/s — exceeded ~2x (positive deviation).
- Models inventory on evo1 (6): qwen3:30b-a3b (17 GiB, qwen3moe Q4_K_M); huihui_ai/glm-4.7-flash-abliterated:latest (17 GiB); qwen3-coder-next:q4_K_M (48 GiB); gurubot/gpt-oss-derestricted:20b (14 GiB); qwen3:4b (2 GiB); qwen3.5:latest (6 GiB).
- ROCm fix prep: banxe added to render,video groups (effective on next login).
- GRUB GTT prep: ttm.pages_limit retargeted 15204352 → 31457280, amdgpu.ppfeaturemask=0xffffffff appended; pre-existing tokens preserved (quiet splash amd_iommu=off amdgpu.gttsize=59392). Backup: `/etc/default/grub.bak.20260501`. update-grub and reboot NOT executed.
- Security upgrades: 80 packages applied, kernel-related 3 (linux-image/headers/generic-hwe-24.04) skipped. dpkg --audit clean. /var/run/reboot-required absent.
- Smoke test post-upgrade: ollama, ssh, systemd-resolved, dbus, containerd active; network-manager inactive by design (system uses systemd-networkd/netplan).
- Deviations recorded:
  - Bench positive deviation (~2x target).
  - S1.6 first pass nodejs unpack OOM under live ollama; recovered with `apt-get install -f` + `apt-get install --reinstall nodejs` (22.22.2).
  - ~80 packages left "unpacked but not configured" after the nodejs OOM; drained with `dpkg --configure -a`.
  - Carry-over from S0 (out of S1 scope): tcp/2222 of evo1 reachable from public internet; brute-force from 185.214.135.211, 185.2.101.118, 47.77.182.54. To be remediated in S6.

## 8. Operator action queued for evo1 (NOT executed in S1)

- `sudo update-grub && sudo reboot` to activate ROCm fix (render,video groups) and GTT GRUB params. Schedule during a low-traffic window. After reboot, S2/S5 work continues.
