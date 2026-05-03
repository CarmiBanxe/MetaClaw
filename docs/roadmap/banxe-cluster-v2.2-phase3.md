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

## 14. Sprint P3.11 — Telegram integration for cluster alerts (30 min, NEW)

Source: QClaw/OpenClaw Telegram webhook capability (Tencent release May 2026).
- Create Telegram bot via BotFather, get bot token.
- Wire ~/bin/check-llm-cluster.sh to send failures to Telegram channel.
- Wire /opt/banxe/compliance/drive_watcher.py alerts to same channel.
- Wire ~/.openclaw/workspace-moa/scripts/daily-eval.sh results to channel.
- Test: force a health-check failure, verify Telegram notification.
Exit-gate: cluster alerts appear in Telegram within 60s of event.

## 15. Phase 4 backlog items (deferred)

P4.1 — QClaw/OpenClaw Computer Use on Legion Windows host (exploration, 2h).
Install QClaw on Legion Windows or upgrade OpenClaw to >=2026.1.29 (patched for CVE-2026-25253).
Evaluate: VS Code automation, browser research, file management via Computer Use.
Security constraint: sandbox mode, no prod credentials, ephemeral tmpfs tool calls.

P4.2 — ROCm 6.4 migration on both EVO-X2 (estimated 2h).
Replace Vulkan path with ROCm for Ollama. Expected throughput improvement on gfx1151.
Gated on FCA CASS 15 deadline (2026-05-07) — do not destabilize cluster before then.

P4.3 — BIOS UMA rebalance on evo1 (15 min + reboot).
Change iGPU VRAM allocation from 96 GiB to 64 GiB in BIOS to match evo2.
Expected result: evo1 CPU RAM 32→64 GiB, throughput 37→70+ toks/s.

P4.4 — XDNA 2 NPU utilization (research sprint, 4h).
252 TOPS aggregate across 2x EVO-X2. AMD Ryzen AI SDK + onnxruntime-directml.

## 16. Security backlog

- CVE-2026-25253 (CVSS 8.8): OpenClaw unauthenticated RCE via WebSocket token hijacking. Affects versions <2026.1.29. ACTION: verify current OpenClaw version on Legion; if vulnerable, upgrade immediately. Ref: QClaw-OpenClaw architecture doc §Security.
- evo1 80/443 ALLOW IN Anywhere (OpenClaw Web UI): restrict to LAN+Tailscale. Deferred from P3.5.

## 17. Sprint P3.12 / P4.5 — LLM Document Translation Pipeline (priority TBD)

Source: hydropix/TranslateBooksWithLLMs (open-source, Ollama-compatible).
Use case: auto-translate client documents (KYC passports, AML bank statements, complaints, regulatory filings, legal docs) from any language to EN/RU/FR for compliance agents.

Integration plan:
- Install on evo1: pip install or git clone + pip install -e in /data/banxe/tools/translate/
- Config: Ollama backend http://127.0.0.1:11434, model qwen3:30b-a3b (multilingual MoE, 100+ languages)
- Workflow: client upload → BANXE intake API → translate to EN → store in /data/banxe/compliance/translated/{client_id}/ → OpenClaw compliance/support/legal agent picks up translated doc
- Supported formats: EPUB, SRT, DOCX, TXT (preserves formatting)
- Post-translation: literary polish pass for readable output
- Fallback model: glm-4.7-flash (fast, lower quality) or GLM-4.5-Air 105B (best quality, via RPC)

BANXE use cases: KYC doc translation (AR/ZH/HI/TR → EN), AML statement screening, client complaint handling, EBA/FCA regulatory memo translation (FR/EN → RU), legal evidence extraction (FR → EN for ss1-type cases), merchant onboarding docs (braslina workflow).

Estimate: 1 hour install + wire. Priority depends on FCA CASS 15 deadline needs.

## 18. Phase 4 item: P4.6 — n8n workflow engine + Atom AI review (2-3 hours)

Dependency chain: n8n install → create BANXE workflows → n8n-atom VS Code extension.

Step 1: Install n8n on evo2 via Docker (evo2 has Docker + 1.7 TiB free):
  docker run -d --name banxe-n8n --restart unless-stopped -p 5678:5678 -v /data/n8n:/home/node/.n8n n8nio/n8n

Step 2: Create BANXE workflows in n8n UI (http://192.168.0.15:5678):
  - Payment flow: webhook trigger → validate → process via BANXE API → notify via Telegram
  - KYC automation: scheduled trigger → fetch pending applications → LLM analysis via LiteLLM :4000 → approve/flag
  - Reconciliation: daily cron → fetch bank data → compare with internal ledger → generate report
  - Compliance monitoring: event trigger → scan documents (translated via P3.12) → alert if red flags

Step 3: Install n8n-atom VS Code extension on Legion:
  - Source: github.com/khanh-atom/n8n-atom
  - Converts n8n workflows to readable markdown/JSON for AI review
  - AI (Continue.dev / Claude Code) reads workflows, suggests optimizations
  - Use case: optimize payment latency, reduce KYC false positives, improve reconciliation accuracy

Integration with existing stack:
  - n8n → LiteLLM :4000 (model=banxe-general) for LLM-powered workflow nodes
  - n8n → OpenClaw (webhook triggers for agent tasks)
  - n8n → TranslateBooksWithLLMs (P3.12) for document translation nodes
  - n8n → Telegram bot (P3.11) for notification nodes
  - Atom → Continue.dev for AI-powered workflow optimization in VS Code

Estimated: 2h install + basic workflows, 1h Atom setup. Deferred to Phase 4 (post FCA CASS 15).

## 19. Sprint P3.1 — execution report (PASS, 2026-05-03)

- evo1: qwen3.5:35b (23 GB), llama3.3:70b (42 GB) present.
- evo2: qwen3.5:35b (23 GB), llama3.3:70b (42 GB) present.
- LiteLLM v2 (:4000) routes added: `ai` (qwen3.5:35b LB evo1+evo2), `ai-heavy` (llama3.3:70b LB evo1+evo2).
- Smoke from Legion: `ai` and `ai-heavy` produce completions via gateway master_key sk-banxe-llm-gateway-2026.
- Exit-gate: 4 pulls succeed; LiteLLM-mediated completions confirmed. PASS.

## 20. Sprint P3.3 — execution report (PASS, 2026-05-03)

- Unit `openclaw-tunnel-gmktec.service` already SSH-logs in as `banxe@evo1:2222` with `~/.ssh/gmktec_key` (no `mmber` user in the SSH path).
- Service uptime 2h+ before this audit, no restart loops; previous `Invalid user mmber` regression (originally fixed in S0) has not reappeared in evo1 sshd journal over the past 24h.
- Hygiene: removed two malformed files in Legion `~/.ssh/` (`'authorized_keys << EOF'`, `'authorized_keys\\""'`) created by an earlier here-doc mistake; backups preserved in `/tmp/legion-ssh-junk-*.bak`.
- Hardened ExecStart with `-o ExitOnForwardFailure=yes` so the tunnel exits immediately if local forwarding can't be established (prevents silent half-broken state).
- Exit-gate verified: 60s evo1 sshd silence confirmed; `127.0.0.1:18791` listening on Legion (LocalForward to OpenClaw 18790).
- Result: PASS.
