# BANXE Cluster — Real Inventory (As-Discovered)

**Date**: 2026-05-02 · **Author**: Moriel Carmi · **Status**: AS-BUILT (committed source of truth)

This document captures the actual state of the BANXE infrastructure as discovered during the 2026-05-01 / 2026-05-02 deep audit. It supersedes the assumption-based topology snapshots in `banxe-cluster-v2.1.md` sections 0 and 13.

## 0. Canon (immutable)

- Legion = factory / dev workstation. Hosts orchestration (OpenClaw, MetaClaw, LiteLLM tier, Aider, Claude Code, Continue.dev). NOT a prod inference node.
- EVO-X2 #1 + EVO-X2 #2 = a single distributed prod inference cluster. Connected via USB4 cable (peer detected at hardware level on 2026-05-02; tb-net interface pending bring-up).
- Two EVO-X2 nodes must operate as one logical cluster (RPC + LB), aggregating 256 GB LPDDR5X and 252 TOPS NPU.
- All BANXE projects live on the EVO-X2 cluster; Legion only runs orchestration and dev tooling.

## 1. Hardware

| Node | Hostname | Make/Model | CPU | RAM | GPU | NPU | Storage | OS |
|---|---|---|---|---|---|---|---|---|
| Legion | mark-legion (Win host) | Lenovo Legion Pro 7 16IRX9H (model 83DF, 2024) | Intel i9-14900HX, 28 logical procs | 64 GiB DDR5 (Windows host); WSL2 limited to 24 GiB by .wslconfig | RTX 4070 Laptop, 8 GiB VRAM, sm_89 (Ada Lovelace) | none | nvme0n1 ~1 TB visible to WSL2 (sdd 1007 GiB / 863 free) | Win 11 Famille + WSL2 Ubuntu 24.04.4 (kernel 6.6.87.2-microsoft-standard-WSL2) |
| EVO-X2 #1 | banxe-NucBox-EVO-X2 | GMKtec NucBox EVO-X2 | AMD Ryzen AI Max+ 395, 16C/32T @ 5.1 GHz, 80 MB cache | 128 GB LPDDR5X 8000 MHz unified | Radeon 8060S, 40 CU RDNA 3.5, gfx1151 (Strix Halo iGPU) | XDNA 2, 126 TOPS (NOT in use yet) | nvme0n1 ~2 TB, /data on rootfs | Ubuntu 24.04, kernel 6.17.0-22-generic |
| EVO-X2 #2 | moriel-carmi-NucBox-EVO-X2 (local) / banxe-nucbox-evo-x2-2 (Tailscale) | GMKtec NucBox EVO-X2 | Same as #1 | 128 GB LPDDR5X 8000 MHz | Radeon 8060S, 40 CU RDNA 3.5, gfx1151 | XDNA 2, 126 TOPS (NOT in use) | nvme0n1p2 1.9 TiB, /data on rootfs (~1.79 TiB free) | Ubuntu 24.04.4, kernel 6.17.0-23-generic |

Aggregate prod cluster compute: 32C/64T CPU + 256 GB unified LPDDR5X + 80 CU iGPU + 252 TOPS NPU (NPU not yet in use).

## 2. Network

- LAN: 192.168.0.0/24 (router-managed DHCP).
- Tailscale tailnet: `banxe.com`, owner `carmi@`.

| Node | LAN | Tailscale | SSH user | SSH port |
|---|---|---|---|---|
| Legion | 192.168.0.75 (Windows host NAT; WSL2 internal 172.22.56.x) | 100.101.218.26 | mmber | (no inbound sshd) |
| EVO-X2 #1 | 192.168.0.72 (eno1) + 192.168.0.117 (wlp195s0 Wi-Fi) | 100.68.102.48 | banxe | 2222 |
| EVO-X2 #2 | 192.168.0.15 (eno1) | 100.99.208.21 | moriel-carmi | 22 + 2222 (dual) |

USB4 cable physically connected between EVO-X2 #1 and EVO-X2 #2 (confirmed 2026-05-02). `thunderbolt` + `thunderbolt_net` modules loaded on both. tb-net interface (`thunderbolt0` / `enxXX`) pending: peer device visible at `/sys/bus/thunderbolt/devices/0-0 1-0 domain0 domain1` on evo2 but no network handshake yet — possibly requires `boltctl authorize` or specific auth.

## 3. Inference + Orchestration stack (per node)

### 3.1 EVO-X2 #1 (banxe-NucBox-EVO-X2, 192.168.0.72, 100.68.102.48)

Confirmed services / processes (from S1 + S2 audits + roadmap v2.1):

- Ollama 0.20.7 — Vulkan path, gfx1151, OLLAMA_HOST=0.0.0.0:11434, FA=1, ctx=131072, NUM_PARALLEL=2, KEEP_ALIVE=10m, API key sk-banxe-evo1-local-2026, models dir /data/ollama-models. Vulkan total 154 GiB.
- Models on disk (6, all Q4_K_M):
  - qwen3:30b-a3b 17.28 GiB (qwen3moe) — bench 36.95 toks/s
  - huihui_ai/glm-4.7-flash-abliterated:latest 17.48 GiB (glm4moelite)
  - qwen3-coder-next:q4_K_M 48.19 GiB (qwen3next) — bench 18.38 toks/s direct
  - gurubot/gpt-oss-derestricted:20b 14.72 GiB (gpt-oss)
  - qwen3:4b 2.33 GiB
  - qwen3.5:latest 6.14 GiB
- Redis on 192.168.0.72:6379 (PONG verified via raw socket; redis-cli not installed on evo1). Used as LiteLLM v2 cache backend (namespace banxe-litellm).
- PostgreSQL 15 — listed in roadmap v2.1 as part of evo1 stack; presence to be re-verified in evo1 deep audit.
- Docker — present (containerd 2.2.1 after S1.6 upgrade); container inventory pending evo1 deep audit.
- systemd active: ollama.service, ssh.service (port 2222 only via socket-activation), various BANXE prod services (per roadmap v2.1: BANXE backend, KYC, compliance — to be enumerated by evo1 audit).
- ufw enabled in S6 with whitelist for 22/2222/11434/3389 from 192.168.0.0/24 + 100.64.0.0/10. Pre-existing rules retained: 80/443 ALLOW IN Anywhere (OpenClaw Web UI — left intentionally; recorded as remaining_security_debt).

### 3.2 EVO-X2 #2 (moriel-carmi-NucBox-EVO-X2 / banxe-nucbox-evo-x2-2, 192.168.0.15, 100.99.208.21)

- Ollama 0.22.1 — Vulkan path, gfx1151, same env vars as evo1 except API key sk-banxe-evo2-local-2026. Vulkan total 184 GiB (post-S2.6 reboot with GTT expansion: amdgpu.ppfeaturemask=0xffffffff + ttm.pages_limit=31457280).
- Models on disk (6, mirror of evo1, total ~107 GiB after S2.7 rsync). Bench qwen3:30b-a3b = 72.40 toks/s (+95.9% vs evo1).
- Docker 29.1.3 + docker-compose-v2 2.40.3 (installed in S6 monitoring). User moriel-carmi added to docker group.
- Monitoring stack (containers in /home/moriel-carmi/monitoring/):
  - banxe-prometheus on 0.0.0.0:9090, retention 14d, scrape jobs litellm_v4000 + ollama_blackbox (evo1+evo2)
  - banxe-blackbox on 0.0.0.0:9115 (http_2xx probe module)
  - banxe-grafana on 0.0.0.0:3000 (admin / banxe2026, persistent volume ./grafana-data)
  - All 4 Prometheus targets reported health=up at S6 close.
- systemd active: ollama.service, ssh.service (dual-listen 22 + 2222 via socket-activation drop-ins), tailscaled.service, docker.service.
- ufw enabled with whitelist for 22/2222/11434/50052/3000/9090/9115 from LAN (192.168.0.0/24) + Tailscale CGNAT (100.64.0.0/10). No public-facing rules.
- /data/ollama-models owned by ollama:ollama 2775 (setgid + group-write); moriel-carmi added to ollama group so rsync from Legion can write into blobs/ via group permission.
- thunderbolt + thunderbolt_net kernel modules loaded (S5 prep). USB4 cable connected; peer device visible at /sys/bus/thunderbolt/devices/0-0 1-0 domain0 domain1. tb-net interface not yet up — pending boltctl authorize / link bring-up.

### 3.3 Legion (mark-legion, 192.168.0.75 NAT, 100.101.218.26)

Confirmed from 2026-05-02 deep audit:

OpenClaw orchestration (canonical BANXE orchestrator on Legion):
- ~/guiyon/ — deploy and migration toolchain (SCRIPTS, CONFIG, SOURCE/OTHER docs, MIGRATION_GUIYON_TO_OPENCLAW_v1.md). The "guiyon" entity referenced in roadmap v2.1 sec.1.3 is in fact OpenClaws deployment toolchain.
- ~/.openclaw-moa/ — Mixture-of-Agents workspace, multiple openclaw.json.bak.* snapshots, workspace-moa-backup-20260326-182806/.
- ~/.openclaw/workspace-moa/scripts/daily-eval.sh — eval suite (fast_checks tag), runs via user crontab at 09:00, 15:00, 21:00 daily; logs to ~/.openclaw/workspace-moa/logs/daily-eval.log.
- 6 user systemd units in ~/.config/systemd/user/:
  - openclaw-gateway.service (+ .bak)
  - openclaw-gateway-moa.service (+ .bak)
  - openclaw-gateway-moa-home.service
  - openclaw-tunnel-gmktec.service — SSH tunnel to evo1 via ~/.ssh/gmktec_key port 2222 user mmber. Disabled in S0b (this was the rogue mmber loop). NEEDS RECONFIG with User=banxe before re-enable.

MetaClaw 0.3.0 (pipx) — metaclaw and litellm-proxy CLIs.
Auto-started from .bashrc:
  cd ~/MetaClaw && source .venv/bin/activate && metaclaw start --mode skills_only --daemon --log-file ~/.metaclaw/metaclaw.log

LiteLLM trinity (3 simultaneous instances):
1. PID 177 — litellm-lan-gateway.service (system unit, our v2 from S4): 0.0.0.0:4000, config /home/mmber/MetaClaw/litellm/litellm-config.v2.yaml, master_key sk-banxe-llm-gateway-2026, 7 LAN/Ollama models, simple-shuffle routing, Redis cache via 192.168.0.72:6379.
2. PID 326 — prod gateway: 127.0.0.1:8080, config /home/mmber/litellm-config.yaml, with cloud providers (Anthropic, Gemini, Groq) and BANXE/UK-GDPR Art.44 routes. Loopback only — auto-started from .bashrc chain. UNTOUCHED.
3. ~/.config/systemd/user/litellm.service — third LiteLLM instance, bind 127.0.0.1, EnvironmentFile ~/.config/litellm/.env. Managed by `systemctl --user` (per .bashrc comment "managed by systemctl --user litellm.service... Do NOT re-enable here").

Aider (pipx, coding assistant) — aliases in .bashrc:
- ai      → aider --model ollama_chat/qwen3.5-abliterated:35b
- ai-heavy → aider --model ollama_chat/llama3.3:70b
- ai-fast  → aider --model ollama_chat/glm-4.7-flash
GAP: qwen3.5-abliterated:35b and llama3.3:70b are NOT in evo1/evo2 model inventory. Aider commands ai and ai-heavy will fail until these models are pulled to the cluster.

gdown (pipx) — Google Drive download utility.

BANXE business services (user systemd):
- banxe-compliance-api.service
- banxe-dashboard.service
- deep-search.service

/opt/banxe/compliance/ — separate Python venv with drive_watcher.py, runs from user crontab every 6 hours: 0 */6 * * * /opt/banxe/compliance/venv/bin/python /opt/banxe/drive_watcher.py >> /opt/banxe/compliance/watcher.log 2>&1

Continue.dev (S3v2 wiring) — ~/.continue/config.json (mode 600), 2 providers: qwen3-coder-next via evo1:11434, qwen3:30b-a3b via evo1:11434.

Claude Code — ~/.claude/ ~712 KB session footprint (projects, sessions, file-history, plugins, debug, paste-cache, telemetry).

~/bin/check-llm-cluster.sh — health probe, runs every 5 min via user crontab (S6 monitoring); log /home/mmber/llm-cluster-health.log.

gitleaks binary in ~/bin/ (used by pre-commit on ~/MetaClaw repo).

SSH key inventory in ~/.ssh/:
- id_ed25519 (primary, used for evo1, evo2, GitHub via "github-ss1" alias hop)
- id_ss1 (GitHub-specific)
- id_gmktec, gmktec_key, gmktec_tailscale (legacy keys for GMKtec / Tailscale to evo1; some referenced by .bashrc gmk-ts alias)

No inbound sshd on Legion — by design (Tailscale path only).

## 4. Cron, systemd timers, autostart hooks (all nodes)

### 4.1 Legion

User crontab (mmber):
- 0 9,15,21 * * * cd /home/mmber/.openclaw/workspace-moa && bash scripts/daily-eval.sh --tag fast_checks (BANXE OpenClaw eval suite, 3x daily)
- 0 */6 * * * /opt/banxe/compliance/venv/bin/python /opt/banxe/drive_watcher.py (BANXE compliance Drive watcher, every 6h)
- */5 * * * * /home/mmber/bin/check-llm-cluster.sh (cluster health probe, every 5 min, S6)

System cron (/etc/cron.d/): only e2scrub_all (Ubuntu default, not BANXE).

User systemd units in ~/.config/systemd/user/ (file presence; active state to be confirmed per unit):
- banxe-compliance-api.service
- banxe-dashboard.service
- deep-search.service
- litellm.service (+ litellm.service.bak.20260430-104006)
- openclaw-gateway.service (+ .bak)
- openclaw-gateway-moa.service (+ .bak)
- openclaw-gateway-moa-home.service
- openclaw-tunnel-gmktec.service (DISABLED in S0b — needs User= rewrite before re-enable)

System systemd units owned by us:
- litellm-lan-gateway.service (S4, our v2 LAN gateway on :4000, auto-restart=always)

Autostart from .bashrc (every interactive shell):
- source "/home/mmber/.openclaw/completions/openclaw.bash"
- cd ~/MetaClaw && source .venv/bin/activate && metaclaw start --mode skills_only --daemon (MetaClaw skills daemon)
- aliases ai, ai-heavy, ai-fast (Aider with cluster models — see 3.3)
- gmk-ts alias (ssh -p 2222 -i ~/.ssh/gmktec_tailscale banxe@100.68.102.48)

### 4.2 EVO-X2 #1 (status confirmed from S1/S2/S6 work; deeper audit pending)

Active system services:
- ollama.service (Ollama 0.20.7, port 11434)
- ssh.service via ssh.socket (port 2222 only, socket-activated)
- ssh.socket
- ufw active with whitelist (22/2222/11434/3389 from LAN+Tailscale; pre-existing 80/443 Anywhere for OpenClaw Web UI)
- redis-server (PONG verified at S4)
- docker (containerd 2.2.1 after S1.6 upgrade)
- BANXE backend services per roadmap v2.1 (BANXE backend, KYC, compliance) — to be enumerated by deeper evo1 audit

Operator action queued (low priority): /opt/banxe/* — verify if there are BANXE bin/scripts/configs paralleling Legion /opt/banxe/compliance.

### 4.3 EVO-X2 #2

Active system services:
- ollama.service (Ollama 0.22.1, port 11434, socket-activated cleanup pending)
- ssh.service via ssh.socket (dual-listen 22 + 2222 via /etc/systemd/system/ssh.socket.d/10-banxe-ports.conf)
- tailscaled.service (Tailscale 1.96.4)
- docker.service (29.1.3)
- ufw active (whitelist LAN + Tailscale CGNAT)
- thunderbolt + thunderbolt_net modules persisted via /etc/modules-load.d/thunderbolt_net.conf (S5 prep)

Container stack (docker compose at ~/monitoring/docker-compose.yml):
- banxe-prometheus, banxe-blackbox, banxe-grafana (all 3 Up, restart=unless-stopped)

No user-level systemd or cron noted yet (deeper audit deferred).

## 5. Open gaps and security debt

### 5.1 Hardware/Software gaps vs canon

- XDNA 2 NPU (252 TOPS aggregate across 2x EVO-X2) — NOT in use. Ollama + Vulkan path do not currently target XDNA. Future Phase 3 task: AMD Ryzen AI SDK or ROCm-with-XDNA backend integration.
- ROCm not validated on either EVO-X2 — running Vulkan exclusively. Roadmap v2.1 expected ROCm fix to unlock 25-35 toks/s on coder-next; we delivered 18.38 toks/s on Vulkan. ROCm verification (rocminfo | grep gfx1151) is queued.
- USB4 peer-to-peer link: cable physically connected; thunderbolt + thunderbolt_net loaded both sides; peer device 0-0/1-0 visible on evo2 /sys/bus/thunderbolt; tb-net interface (thunderbolt0 / enxXX) NOT yet created. Likely needs boltctl authorize on at least one side, or kernel-level XDomain handshake. Required before S5 RPC distributed inference.

### 5.2 Models missing from cluster (vs Legion .bashrc usage)

Aider command aliases on Legion expect these models on the cluster (currently NOT present on evo1 or evo2):
- ollama_chat/qwen3.5-abliterated:35b — used by `ai`
- ollama_chat/llama3.3:70b — used by `ai-heavy`
Action: pull both onto evo1 and evo2 to make Aider operational.

Additionally, per the new canon (evo2 carries unique reasoning model that evo1 does not), we should add at least one large reasoning model that benefits from 128 GB LPDDR5X without RPC, e.g. Qwen3-235B Q3_K_M (~95 GiB), Llama-3.3-70B Q5_K_M (~50 GiB), or DeepSeek-R1-Distill-Llama-70B Q4_K_M (~40 GiB).

### 5.3 Open security debt

- evo1: tcp/2222 has been narrowed to LAN+Tailscale via ufw (S6); the public router port-forward (if still active on the router admin) should also be removed. Currently brute-force from 185.214.135.211, 185.2.101.118, 47.77.182.54 (S0 finding) is silently dropped at evo1 ufw, but still consumes router NAT slots.
- evo1: 80/443 ALLOW IN Anywhere (OpenClaw Web UI) retained intentionally; review whether this should move behind Tailscale or auth proxy.
- Tailscale ACL: `Tailscale SSH enabled, but access controls don't allow anyone to access this device` health warning on Legion + evo2 (we use plain openssh, not Tailscale-SSH; warning is informational, not blocking).
- LiteLLM trinity overlap: prod LiteLLM on :8080 (loopback) holds cloud API keys from env (Anthropic/Gemini/Groq); never expose externally. Verified loopback-only. Our v2 on :4000 is LAN/Tailscale-bound only and contains no cloud providers.

### 5.4 Roadmap v2.1 delta vs as-built

Recorded in banxe-cluster-v2.1.md sections 14, 16, 18, 21. Highlights for cross-reference here:
- v2.1 assumed Legion = RTX 4090 + 32+ GiB RAM. Actual: RTX 4070 Laptop 8 GiB + 64 GiB DDR5 host (24 GiB exposed to WSL2 after .wslconfig bump).
- v2.1 expected evo2 user=banxe, hostname=banxe-NucBox-EVO-X2-2, IP=192.168.0.73. Actual: user=moriel-carmi, local hostname moriel-carmi-NucBox-EVO-X2 (Tailscale hostname banxe-nucbox-evo-x2-2), IP=192.168.0.15.
- v2.1 §1.3 "guiyon-dispatcher think option" now identified as OpenClaw deployment toolchain (~/guiyon/); think-option reconfiguration deferred until inventory captures actual openclaw.json settings.
- Sprint 3 (Qwen3-Coder-Next 80B local llama.cpp+CUDA on Legion target 25-35 toks/s): WONTFIX_HARDWARE; replaced by S3v2 (Continue.dev wired to evo1 endpoint, 18.38 toks/s).
- Sprint 5 RPC distributed inference: BLOCKED_HARDWARE -> UNBLOCKED on 2026-05-02 (USB4 cable connected). Pending tb-net interface bring-up and llama.cpp GGML_RPC build.

## 6. Sources of this inventory

- banxe-roadmap-v1.md (attached, plan basis for v2.1)
- banxe_evox2_cluster_runbook.md (attached, earlier general bring-up plan)
- docs/roadmap/banxe-cluster-v2.1.md (this repo, sections 1..21 commits 92ce5d5 -> 137490f)
- 2026-05-02 deep audit: ~/audit-banxe-2026-05-02/legion-full-audit.txt (sections System / Network / Containers / Systemd / Inference / Orchestration / Web / Cron)
- Live shell evidence captured during S0 -> S6 sprints (per-step outputs in this session log)

## 7. Status snapshot (as of 2026-05-02 00:30 CEST)

- All 3 nodes alive, reachable via Tailscale + LAN.
- LiteLLM trinity all running (PID 177 v2 :4000, PID 326 prod :8080, user-systemd litellm.service :loopback).
- Both EVO-X2 Ollama active, models replicated (6/6 parity).
- Monitoring stack on evo2 healthy (Prometheus + Grafana + blackbox; 4/4 scrape targets up).
- check-llm-cluster cron writing to /home/mmber/llm-cluster-health.log every 5 min.
- USB4 link discovered at hardware level; tb-net handshake pending.
- Aider ai/ai-heavy commands non-functional until qwen3.5-abliterated:35b and llama3.3:70b are pulled onto cluster.
- Continue.dev requires VS Code extension reload to pick up ~/.continue/config.json (S3v2 deferred operator action).
- BANXE compliance/dashboard/deep-search and OpenClaw eval cron all running per their own schedules; not affected by SRE work.

## 5.7 USB4 link UP — Sprint 5.1 closed (2026-05-02 01:59 CEST)

After replacing the wrong PD-only cable with a correct USB4/TB4 data cable, the link came up cleanly on both nodes:
- evo1 thunderbolt0 UP, MAC 02:4d:fd:67:8e:09, peer device 1-2 visible at 01:44.
- evo2 thunderbolt0 UP, MAC 02:90:cb:8a:75:6f, peer device 1-2 visible at 01:44.
- IP addressing: evo1=10.0.0.1/30, evo2=10.0.0.2/30 (point-to-point, /30 mask, no gateway).
- Persistent: /etc/systemd/network/10-thunderbolt0.network on both nodes (will auto-apply on next boot).
- ufw allow from 10.0.0.0/30 added on evo2 (USB4-RPC-link comment).

Connectivity verified:
- ICMP: ping 10.0.0.1 from 10.0.0.2 → 5/5 packets, 0% loss, RTT min/avg/max/mdev = 0.300/0.489/0.644/0.127 ms.
- TCP/iperf3: 4 parallel streams, 10 sec, [SUM] 9.12 Gbit/s sender / 9.11 Gbit/s receiver, 0 retransmits, 10.6 GBytes total transfer.

Throughput note: 9.12 Gbit/s achieved is ~23% of USB4 theoretical 40 Gbit/s, which is typical for the Linux `thunderbolt_net` driver path (kernel-level, no SR-IOV / DMA bypass). This is 9× faster than 1 GbE LAN and well above the bandwidth needed for llama.cpp RPC token streaming. RTT 0.49 ms beats the 65-second-per-token LAN ceiling described in roadmap v2.1 §5.

Sprint S5 status moved from BLOCKED_HARDWARE to IN_PROGRESS. Next: build llama.cpp with GGML_RPC + GGML_VULKAN on both EVO-X2 nodes.
