# BANXE AI Cluster — Phase 3 Roadmap v2.2 (uточнённый)
Date: 2026-05-03 · Author: Moriel Carmi · Status: PLANNED

## 0. Context

Phase 1+2 (v2.1) completed 2026-05-02: PR #1 merged (squash). S0-S6 closed.
This Phase 3 addresses: management audit gaps, full hardware utilization,
reasoning model on evo2, GitHub repo integration, service migration.

## 1. Cluster hardware (verified 2026-05-03)

Legion: i9-14900HX (28 vCPU) + 64 GiB DDR5 + RTX 4070 Laptop 8 GiB + C:952 GiB + D:3.7 TiB (EMPTY).
EVO-X2 #1: Ryzen AI Max+ 395 (32T) + 128 GiB LPDDR5X + Radeon 8060S 40 CU + XDNA2 126 TOPS + nvme1(931 GiB /) + nvme0(1.9 TiB /data).
EVO-X2 #2: Same APU + 128 GiB + nvme0(1.9 TiB / and /data).
USB4 link: 9.12 Gbit/s, 0.49 ms RTT between evo1 and evo2.
Cluster total: 10.3 TiB storage (8.9 TiB free), 320 GiB RAM, 252 TOPS NPU.

## 2. GitHub repos (25 total, CarmiBanxe account)

Core platform: banxe-platform (TS), banxe-emi-stack (Py, FCA CASS 15 P0 deadline 7 May), banxe-payment-core (Py, Hyperswitch+Paymentology+Midaz+Mastercard), banxe-architecture (Shell, mandatory constraints).
AI/ML layer: MetaClaw (Py, orchestrator), developer-core (Py, shared stack), guiyon (PRIVATE, OpenClaw deployment), MiroFish (Py, swarm intelligence), banxe-training-data (Py, auto-ingest pipeline), banxe-mirofish (Shell, integration).
Business automation: braslina (Py, merchant onboarding), banxe-business-processes (Py, ArchiMate 3.2), crypto-ops-monitor (Py, crypto ops).
Compliance/Legal: banxe-lexisnexis-distro (Shell, AI compliance platform), legi_fr (French law), france.code-civil (civil code under git), ss1 (legal case).
UI/UX: banxe-ui (TS, UI prototype), obsidian-vault (knowledge base).
Infra/DevOps: banxe-infra (Shell), vibe-coding (Shell, dev workspace), collaboration (Py).
Utilities: gpt-archive-toolkit (Py, ChatGPT export pipeline).
Archive: banxe-archive-2026-04-18 (PRIVATE, snapshot).

## 3. Sprint P3.1 — Download Aider models on cluster (30 min)

- ollama pull qwen3.5:35b on evo1 then evo2 (~20 GiB each)
- ollama pull llama3.3:70b on evo1 then evo2 (~40 GiB each)
- Verify Aider aliases ai and ai-heavy on Legion
Exit-gate: 4 pulls succeed; Aider produces completions.

## 4. Sprint P3.2 — Reasoning model on evo2 single-node (60 min)

Download Qwen3-235B Q3_K_M (~95 GiB) on evo2 via ollama pull or HF download.
Fallback if unavailable: deepseek-r1:70b or llama3.3:70b (already from P3.1).
Wire LiteLLM v2 route: model_name reasoning, evo2 only.
Bench from Legion via :4000 model=reasoning.
Exit-gate: reasoning route live; toks/s recorded.

## 5. Sprint P3.3 — Fix OpenClaw tunnel (15 min)

Reconfig openclaw-tunnel-gmktec.service: User=mmber to User=banxe, fix SSH key ref.
systemctl --user daemon-reload and enable --now.
Verify: no Invalid user mmber in evo1 journal for 60s.

## 6. Sprint P3.4 — Migrate BANXE business services to evo1 (45 min)

Move from Legion (unreliable WSL2) to evo1 (24/7 prod server):
banxe-compliance-api, banxe-dashboard, deep-search, drive_watcher cron.
Audit ExecStart and deps, copy to /data/banxe/ on evo1, create systemd units, migrate cron, disable on Legion.

## 7. Sprint P3.5 — Security hardening (20 min)

Restrict 80/443 on evo1 to LAN+Tailscale (currently Anywhere).
Validate ROCm: rocminfo on both evo.
Review 3389/tcp necessity on evo1.

## 8. Sprint P3.6 — Ollama align + hostname (15 min)

Update evo1 Ollama 0.20.7 to 0.22.1.
Set evo2 hostname to banxe-NucBox-EVO-X2-2.
Verify version parity.

## 9. Sprint P3.7 — Grafana + persistent units (20 min)

Add Prometheus datasource to Grafana (http://prometheus:9090).
Import dashboards.
Convert glm-master to permanent systemd unit on evo1.
Validate USB4 IP persistence after reboot.

## 10. Sprint P3.8 — Utilize Legion D drive 3.7 TiB (30 min)

Create directory structure on /mnt/d:
- /mnt/d/models/ — all GGUF models for Legion dev (symlink from ~/models)
- /mnt/d/backups/evo1/ and /mnt/d/backups/evo2/ — daily rsync cron
- /mnt/d/training-data/ — datasets from banxe-training-data repo
- /mnt/d/archives/ — legacy code, ChatGPT exports
Set up rsync cron on Legion: daily at 04:00, incremental, evo1 /data and evo2 /data to D drive.

## 11. Sprint P3.9 — Operational hygiene (20 min)

MODELS.md classifier in repo (prod-critical, replaceable, obsolete).
Daily backup tagging cron: ollama cp MODEL MODEL:backup-YYYYMMDD on evo1+evo2.
Baseline audit files for evo1 and evo2 (like Legion audit).
Commit audit files to docs/audit/.

## 12. Sprint P3.10 — XDNA 2 NPU exploration (deferred Phase 4)

252 TOPS aggregate. Requires AMD Ryzen AI SDK.
Research onnxruntime-directml or Vitis AI.
Status: DEFERRED.

## 13. Execution order

1. P3.1 Aider models — immediate developer unblock
2. P3.2 Reasoning model evo2 — unique cluster capability
3. P3.3 OpenClaw tunnel fix — orchestration unblock
4. P3.6 Ollama align + hostname — consistency
5. P3.5 Security — close remaining debt
6. P3.4 Migrate services — reliability
7. P3.8 D drive utilization — storage optimization
8. P3.7 Grafana + units — observability
9. P3.9 Hygiene — maintenance
10. P3.10 NPU — future

Estimated total: ~5 hours for P3.1-P3.9. P3.10 deferred.
