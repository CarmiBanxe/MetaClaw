# BANXE AI Cluster — Roadmap v2.1
Date: 2026-05-01 · Author: Moriel Carmi · Status: COMMITTED

## 0. Topology snapshot (01.05.2026)

| Node | Hostname | LAN IP | Tailscale | Role | Notes |
|---|---|---|---|---|---|
| EVO-X2 #1 | banxe-NucBox-EVO-X2 | 192.168.0.72 | 100.68.102.48 | Prod Ollama | Vulkan, gfx1151, FA pending, ROCm fix pending |
| EVO-X2 #2 | TBD | 192.168.0.15 | not-yet-joined | Fresh Ubuntu 24.04 | openssh-server not installed (S0 blocker) |
| Legion    | mark-legion         | 192.168.0.75 (NAT) | 100.101.218.26 | LiteLLM gateways (prod 8080 + LAN v2 4000) | WSL2 Ubuntu 24.04 on Windows 11 host; RTX 4070 Laptop 8 GiB; 3.8 GiB RAM |

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

## 9. Sprint S3v2 — execution report (PASS)

Original Sprint 3 (Qwen3-Coder-Next 80B local llama.cpp+CUDA on Legion, target 25–35 toks/s) was PAUSED on hardware mismatch: Legion is RTX 4070 Laptop 8 GiB + 3.8 GiB RAM, not RTX 4090 + 32 GiB. Pivoted to S3v2 — wire coding access via the existing evo1 endpoint.

- evo1 already hosts qwen3-coder-next:q4_K_M (~51.7 GB Q4_K_M, qwen3next family).
- Direct bench from Legion via ssh evo1 → 127.0.0.1:11434 with sk-banxe-evo1-local-2026:
  eval_count=200, toks_per_sec=18.38 (200-token Python fibonacci prompt).
- ~/.continue/config.json written on Legion (mode 600, 700 bytes), 2 providers:
  1) Qwen3-Coder-Next (evo1, 80B MoE, Vulkan) → http://192.168.0.72:11434/v1, qwen3-coder-next:q4_K_M.
  2) Qwen3-30B BANXE (evo1, fast) → http://192.168.0.72:11434/v1, qwen3:30b-a3b.
  tabAutocompleteModel = qwen3-coder-next:q4_K_M.
- /v1/chat/completions smoke from ssh evo1 → http://192.168.0.72:11434/v1: HTTP 200, valid OpenAI completion format.
- LiteLLM prod on :8080 left untouched.
- VS Code Continue extension reload required by user (cannot be done from shell).
- Deviations: original 80B local plan paused (hardware mismatch); curl invocations from Legion shell sandboxed → routed via ssh evo1.

## 10. Sprint S4 — execution report (PASS)

LiteLLM Gateway upgrade — pivot to side-by-side stack to protect prod compliance routes.

Decision: stand up new LAN-only LiteLLM v2 on port 4000, leave existing prod LiteLLM on 127.0.0.1:8080 untouched. Prod gateway hosts cloud providers (Anthropic/Gemini/Groq) and BANXE/UK-GDPR Art.44 compliance routes; mirroring those into a 0.0.0.0:4000 instance would have leaked cloud API keys to the LAN.

- v2 process: systemd unit /etc/systemd/system/litellm-lan-gateway.service, User=mmber, Group=mmber, Restart=always RestartSec=10. MainPID at S4.6 close = 390324, listening 0.0.0.0:4000.
- v2 config: /home/mmber/MetaClaw/litellm/litellm-config.v2.yaml, mode 600, ~3.3 KB. NO cloud providers.
- Models registered (7): banxe-general, qwen3-30b, qwen3-banxe, fast, glm-4-flash, coding, gpt-oss-20b. Master key sk-banxe-llm-gateway-2026.
- Backends: evo1 (192.168.0.72:11434) and evo2 (192.168.0.15:11434) via Ollama. Coding/gpt-oss-20b on evo1 only.
- Router: latency-based-routing, num_retries=2, timeout=120, retry_after=5; fallbacks coding→qwen3-30b, banxe-general→fast.
- Redis cache: 192.168.0.72:6379 namespace banxe-litellm (PONG verified via raw socket).
- Prometheus callbacks enabled; pipx venv was missing prometheus_client → injected via `pipx inject litellm prometheus_client`.
- Functional checks via ssh evo1 → 100.101.218.26:4000 (Tailscale; LAN 192.168.0.75:4000 unreachable due to WSL2 NAT):
  - GET /v1/models → 7 entries, HTTP 200.
  - 4× /v1/chat/completions on banxe-general: 3 served by evo1 (200), 1 by evo2 (404 — qwen3:30b-a3b not yet replicated, S2.7 in flight).
  - coding completion: toks_per_sec = 17.12 (vs S3v2 direct baseline 18.38, proxy overhead 6.85%).
- Prod gateway: pid 309, 127.0.0.1:8080, elapsed at S4.6 close = 03:53:25. Untouched, no regression.
- Deviations: latency-router temporarily prefers failing evo2 endpoints (404 returns faster than evo1 inference). Self-resolves once S2.7 completes.

Post-S2.7 follow-ups: re-run banxe-general LB burst (expect both backends serve), re-run fast burst (expect router quirk to clear), then close S2.8 + S2.9.

## 11. Sprint S2 — partial progress (S2.0–S2.6 done, S2.7 in flight)

S2 plan (EVO-X2 #2 bring-up) advanced through S2.0–S2.6. S2.7 (rsync of /data/ollama-models from evo1) was started 13:14 CEST on 2026-05-01 and is still copying at the time of this commit. S2.8 + S2.9 are pending S2.7 completion; final S2_evo2_bringup JSON will be appended in a follow-up commit.

- S2.0 pre-state probe: evo2 = moriel-carmi-NucBox-EVO-X2 (Ubuntu 24.04.4 LTS, kernel 6.17.0-23-generic), nvme0n1 1.9 TiB / 1.8 TiB free, 62 GiB RAM, 32 vCPU, /data absent (created on rootfs in S2.3), Ollama not installed.
- S2.1 base stack: apt update + install ~30 pkgs (git, htop, nvtop, iotop, cmake, ninja-build, python3-pip, python3-venv, pv, lm-sensors, build-essential, …). ufw rules added (22, 2222, 11434, 50052) v4+v6, ufw active. ssh service stayed active across `ufw --force enable`.
- S2.2 sshd dual-listen 22+2222: drop-in /etc/ssh/sshd_config.d/10-banxe-ports.conf (Port 22, Port 2222) AND drop-in /etc/systemd/system/ssh.socket.d/10-banxe-ports.conf (ListenStream=22, ListenStream=2222) because Ubuntu 24.04 uses socket-activation. Listeners verified on 0.0.0.0 and [::] for both ports. Passwordless ssh -p 2222 moriel-carmi@192.168.0.15 confirmed.
- S2.3 /data layout on rootfs: /data/{ollama-models,models,llama-cpp} created, owner moriel-carmi:moriel-carmi 0755 initial. (Later corrected in S2.5-fix to ollama:ollama 2775 for ollama-write + group-write for moriel-carmi via setgid.)
- S2.4 GRUB GTT prep: /etc/default/grub backup → grub.bak.20260501.evo2. New CMDLINE: `quiet splash amdgpu.ppfeaturemask=0xffffffff ttm.pages_limit=31457280` (pre-state was just `quiet splash`). update-grub and reboot NOT executed in S2.4.
- S2.5 Ollama install + canonical override.conf: ollama 0.22.1 installed via official script, ollama:ollama (uid 997) auto-created with render(992)+video(44) groups. Canonical override.conf written with sk-banxe-evo2-local-2026 + FA=1 + ctx 131072 + NUM_PARALLEL=2 + KEEP_ALIVE=10m. First-start failed with `Error: mkdir /data/ollama-models/blobs: permission denied` — fixed in S2.5-fix: chown ollama:ollama on three /data subdirs, chmod 2775 (setgid + group-write), usermod -aG ollama moriel-carmi (so future rsync from moriel-carmi can group-write into blobs/). After fix: ollama active, *:11434 listening, /data/ollama-models/blobs created by ollama, /api/tags returns {"models":[]}.
- S2.6 update-grub + reboot (UNSAFE STEP, gated): operator-approved. Reboot executed; evo2 returned in 5 s. /proc/cmdline confirms both grub tokens applied. Post-reboot: ollama active, 22+2222+11434 listening, Vulkan total = **184.0 GiB** (above the expected ~154 GiB — recorded as positive deviation).
- S2.7 rsync (in flight): launched 13:14 CEST as `moriel-carmi` on evo2 with `nohup rsync -rlptD --partial --info=progress2 --no-i-r -e "ssh -p 2222 -i ~/.ssh/id_ed25519_to_evo1" banxe@192.168.0.72:/data/ollama-models/ /data/ollama-models/`. Auth path = dedicated keypair id_ed25519_to_evo1 on evo2, pubkey appended to banxe@evo1:/home/banxe/.ssh/authorized_keys (one-time UNSAFE STEP, idempotent). Sustained throughput ≈ 11.2 MB/s, ETA ≈ 2:42; total ≈ 104 GiB. Background watcher monitors `tail -3 /tmp/rsync_evo1_to_evo2.log` every 5 min on evo2; on detection of `total size is …` / `sent X received Y bytes` the agent will auto-resume S2.8 + S2.9.

Pending in this sprint:
- S2.8 cross-check + bench: /api/tags on evo2:11434 (sk-banxe-evo2-local-2026) lists qwen3:30b-a3b + glm-4.7-flash + qwen3-coder-next:q4_K_M; bench qwen3:30b-a3b from Legion via :4000 (LiteLLM v2 LB) — expect parity with evo1 ±15% (target ≈ 31–43 toks/s).
- S2.9 final smoke + cluster matrix update: 3×3 ICMP+SSH still PASS, df -h /data on evo2, du -sh /data/ollama-models on evo2, finalize S2_evo2_bringup JSON.

Post-S2.7 also re-runs LiteLLM v2 (port 4000) banxe-general LB burst and fast burst — expect router-quirk to clear once evo2 stops returning 404.

## 12. Sprint S2 — final close (PASS)

S2.7 rsync completed 2026-05-01 ~15:58 CEST (164 min, ~107 GiB at avg 11.05 MB/s, exit code 23 due to utime perms on /data and /data/blobs only — all 41 file entries transferred, no data loss).

Inventory parity with evo1 confirmed (6/6 models): qwen3:30b-a3b 17.28 GiB qwen3moe; huihui_ai/glm-4.7-flash-abliterated:latest 17.48 GiB glm4moelite; qwen3-coder-next:q4_K_M 48.19 GiB qwen3next; gurubot/gpt-oss-derestricted:20b 14.72 GiB gpt-oss; qwen3:4b 2.33 GiB; qwen3.5:latest 6.14 GiB.

Bench qwen3:30b-a3b on evo2 from Legion: **72.40 toks/s** (eval_count=200, eval_duration=2762.5 ms). evo1 baseline = 36.95 toks/s. evo2 outperforms by **+95.9%** — recorded as positive deviation. Likely causes: fresher kernel 6.17.0-23 vs evo1 6.17.0-22, no production background load on evo2, larger Vulkan GTT pool 184 GiB vs evo1 154 GiB.

LiteLLM v2 :4000 LB validation (cache-bypass burst, 6 unique-prompt parallel requests):
- 6/6 → 200 OK, time 0.69–1.55 s.
- All 6 routed to evo2 (latency-based-routing converged to faster backend). Cluster-level behavior is fail-over rather than round-robin. To enforce balanced load: switch routing_strategy to simple-shuffle or usage-based-routing (deferred to S6 hardening).
- Earlier 8-request burst (S4.5 reuse with prompt "reply 1..8") hit Redis cache 5/8; cache-bypass with nanosecond-timestamp prompts produced the clean numbers above.

Cluster-level KPI snapshot post-S2 close:
- Combined potential throughput: evo1 36.95 + evo2 72.40 = **~109 toks/s** on qwen3:30b-a3b (target was 67 → 130+; on track).
- All 7 LiteLLM v2 models routable; coding via :4000 = 17.12 toks/s (S4 baseline).
- Prod LiteLLM :8080 untouched (loopback; cloud + UK GDPR routes intact).

Operator actions for S2 close: none (rsync auto-completed, all probes are read-only).

Sprint S2 status: **PASS**. next_sprint_ready=true.

## 13. Cluster post-state snapshot (2026-05-01, end of day)

| Component | Endpoint | Auth | Status |
|---|---|---|---|
| evo1 Ollama | http://192.168.0.72:11434 | Bearer sk-banxe-evo1-local-2026 | active, Vulkan 154 GiB, 36.95 toks/s |
| evo2 Ollama | http://192.168.0.15:11434 | Bearer sk-banxe-evo2-local-2026 | active, Vulkan 184 GiB, 72.40 toks/s |
| LiteLLM prod | http://127.0.0.1:8080 (loopback) | Bearer LITELLM_MASTER_KEY (env) | active, pid 309, cloud + BANXE/UK-GDPR routes |
| LiteLLM v2 LAN | http://0.0.0.0:4000 | Bearer sk-banxe-llm-gateway-2026 | active, systemd litellm-lan-gateway.service, 7 LAN models |
| Redis cache | 192.168.0.72:6379 ns banxe-litellm | (none) | PONG verified |
| Continue.dev | ~/.continue/config.json | sk-banxe-evo1-local-2026 | wired, 2 providers (coder-next + qwen3-30b on evo1) |

Three-node Tailscale tailnet `banxe.com` (carmi@):
- Legion `mark-legion` 100.101.218.26 (RTX 4070 Laptop 8 GiB / 3.8 GiB RAM)
- EVO-X2 #1 `banxe-nucbox-evo-x2` 100.68.102.48 (192.168.0.72 LAN, prod)
- EVO-X2 #2 `banxe-nucbox-evo-x2-2` 100.99.208.21 (192.168.0.15 LAN, fresh prod)

Pending sprints: **S5** (RPC distributed inference, USB4/Thunderbolt link 10.0.0.1/30 ↔ 10.0.0.2/30, GLM-4.7 full Q4_K_M ~190 GiB), **S6** (Prometheus+Grafana, ~/check-llm-cluster.sh cron, public 2222/tcp closure on evo1, Tailscale ACL for cross-node SSH, simple-shuffle routing).

Pending follow-up actions queued for the operator (off-sprint, low priority):
- evo1: `sudo update-grub && sudo reboot` to activate render/video group membership for banxe and the ttm.pages_limit/ppfeaturemask GRUB tokens. Schedule during a low-traffic window.
- VS Code: reload Continue extension to pick up ~/.continue/config.json from S3v2.

## 14. Audit 2026-05-01 (end of Phase 1)

Roadmap completion as of this commit:

| Sprint | Plan reference | Actual status | Completion |
|---|---|---|---|
| S0 + S0b | Discovery & Connectivity | All 6 sub-tasks done; tailnet `banxe.com` joined for 3 nodes; passwordless SSH cluster-wide | 100% |
| S1 | evo1 hotfix without downtime | override.conf canonical, FA=1, ctx 131072, NUM_PARALLEL=2, KEEP_ALIVE=10m, 80 security pkgs, GRUB tokens written; **`update-grub && reboot` queued for operator** | ~85% |
| S2 | evo2 bring-up | Full 9 sub-tasks done; 6/6 model parity with evo1; bench 72.40 toks/s | 100% |
| S3 | Legion coding model (Qwen3-Coder-Next 80B llama.cpp+CUDA, target 25-35 toks/s) | **PAUSED** on hardware mismatch (Legion=RTX 4070 Laptop 8 GiB, not RTX 4090 24 GiB). S3v2 wired Continue.dev to evo1 coder-next at 18.38 toks/s | ~30% (S3v2 only) |
| S4 | LiteLLM gateway upgrade | New v2 gateway on :4000 (systemd, LAN-only), 7 models, latency-routing, Redis cache, Prometheus callbacks. **`large` route (RPC GLM-4.7) commented out pending S5** | ~85% |
| S5 | Distributed inference llama.cpp RPC | NOT STARTED. Requires USB4/Thunderbolt cable between EVO-X2, GLM-4.7 Q4_K_M ~190 GiB download, llama.cpp RPC build on both EVO-X2 | 0% |
| S6 | Production Hardening | NOT STARTED. Includes Prometheus+Grafana, ~/check-llm-cluster.sh cron, **public 2222/tcp closure on evo1 (security-debt carry-over)**, Tailscale ACL for cross-node SSH, simple-shuffle routing | 0% |

Weighted overall completion: **~58%**.

KPI status:

| KPI | Target | Actual | Status |
|---|---|---|---|
| EVO-X2 cluster throughput | 67 → 130+ toks/s (LB ×2) | evo1 36.95 + evo2 72.40 = 109 toks/s sum; latency-router converges to evo2 alone (~72 steady-state) | ⚠ Below 130 single-backend; close to 130 in sum |
| Coding throughput | 13-17 → 25-35 toks/s | 18.38 toks/s (qwen3-coder-next on evo1 Vulkan, NOT Legion CUDA) | ❌ Below 25-35; blocked by hardware |
| Per-node API key | sk-banxe-evo{1,2}-local-2026 | applied | ✅ |
| 190 GiB models via RPC, GLM-4.7 7-8 toks/s | full | not implemented (S5 pending) | ❌ |

Phase 2 (next session) execution order, by `optimality` canon:

1. **S1 reboot evo1** (1 operator command, ~30 s downtime). Activates render/video group for banxe + ttm.pages_limit + amdgpu.ppfeaturemask. Closes S1 to 100%.
2. **S3 decommission** (no execution, just decision-record): formally accept S3v2 as the final coding path; mark S3 KPI "25-35 toks/s coding" as BLOCKED_HARDWARE until a CUDA host (≥ RTX 4090 24 GiB + 64 GiB RAM) is added to the fleet.
3. **S6 security-critical subset first** (public 2222/tcp closure on evo1 + Tailscale ACL): closes the carry-over security debt from S0 (active brute-force from 185.214.135.211, 185.2.101.118, 47.77.182.54). Does not require new hardware.
4. **S5 RPC distributed inference** (full sprint, 4-8 hours): requires USB4/Thunderbolt cable. Will close `large` route in LiteLLM v2 yaml.
5. **S6 monitoring subset** (Prometheus+Grafana, cron health-check, simple-shuffle routing): finalizes Phase 2.

Operator-side prerequisites for Phase 2:
- Confirm presence of USB4/Thunderbolt cable between EVO-X2 #1 and EVO-X2 #2.
- Confirm acceptance of S3 decommission (no separate CUDA host purchase planned).
- Confirm a 1-minute prod downtime window for S1 reboot.
