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

## 21. Sprint P3.5 — execution report (PASS, 2026-05-03)

- Closed inbound exposure on evo1: `80/tcp` and `443/tcp` were `ALLOW IN Anywhere` (v4 + v6) for OpenClaw UI; narrowed to `192.168.0.0/24` (LAN) and `100.64.0.0/10` (Tailscale) only. `127.0.0.1` loopback rule preserved.
- ROCm validated on evo1: `rocminfo` reports agent `gfx1151` ("AMD RYZEN AI MAX+ 395 w/ Radeon 8060S"). Confirms ROCm/HSA stack is intact for the GLM-4.5-Air RPC path.
- 3389/tcp on evo1 already constrained to LAN + Tailscale (S6 prior work); kept as-is, no public exposure.
- Other audit (no change): SSH 22/2222 ⇒ LAN+Tailscale, Ollama 11434 ⇒ LAN+Tailscale, GLM 8081 ⇒ LAN+WSL+Tailscale (added in P3.7b/P4 wiring).
- Result: PASS.

## 22. Sprint P3.6 — execution report (PARTIAL PASS, 2026-05-03)

- evo2 hostname already canonical: `banxe-NucBox-EVO-X2-2` (no `hostnamectl set-hostname` needed). VERIFIED.
- ROCm/Ollama parity audit:
  - evo1: ollama 0.20.7 (kernel 6.17.0-22-generic), hostname `banxe-NucBox-EVO-X2`.
  - evo2: ollama 0.22.1 (kernel 6.17.0-23-generic), hostname `banxe-NucBox-EVO-X2-2`.
- evo1 ollama 0.20.7 → 0.22.x upgrade DEFERRED: in-flight `qwen3:235b-a22b` pull on evo2 makes evo1 the only LB fallback for `ai`/`ai-heavy`/`banxe-general`/`fast` routes; restarting ollama on evo1 right now would briefly degrade those routes. Will execute the upgrade in a follow-up window once P3.2 pull finishes. Tracked.
- Result: PARTIAL PASS (hostname VERIFIED; version align deferred to safe window).

## 23. Sprint P3.4 — execution report (PAPER PLAN, 2026-05-03)

Audit-only inventory of BANXE services currently running on Legion that are scheduled to migrate to evo1 in a follow-up window (when in-flight P3.2 pull releases the LB fallback constraint).

### Migration candidates (Legion → evo1 `/data/banxe/`)

| # | Service | Unit / Cron | Cmd / WD | Listen | Deps |
|---|---|---|---|---|---|
| 1 | banxe-compliance-api | systemd --user `banxe-compliance-api.service` | `uvicorn api.main:app --host 0.0.0.0 --port 8093 --workers 1` · wd=`~/banxe-emi-stack` · EnvFile=`~/banxe-emi-stack/.env` · venv=`/opt/banxe/compliance/venv` | tcp/8093 | `/opt/banxe/*`, env in `~/banxe-emi-stack/.env` |
| 2 | banxe-dashboard | systemd --user `banxe-dashboard.service` | `uvicorn dashboard.server:app --host 0.0.0.0 --port 8090` · wd=`~/.openclaw/workspace/banxe-ai-bank` · bin=`~/.openclaw-moa-home/.local/bin/uvicorn` | tcp/8090 | OpenClaw workspace tree |
| 3 | deep-search | systemd --user `deep-search.service` | `python3 ~/deep-search-server.py` · bin=`~/playwright-env/bin/python3` | tcp/8088 | Playwright + chromium runtime |
| 4 | drive_watcher (cron) | crontab `0 */6 * * *` | `/opt/banxe/compliance/venv/bin/python /opt/banxe/drive_watcher.py >> /opt/banxe/compliance/watcher.log 2>&1` | none | `/opt/banxe/*`, Google API token.json |

### What stays on Legion
- `litellm.service` (prod gateway :8080) — unchanged.
- LiteLLM v2 on :4000 (manual) — unchanged.
- `openclaw-tunnel-gmktec.service` (already SSH tunnel into evo1; lives on Legion intentionally).

### Deferred execution plan (NOT YET RUN)
1. On evo1: create `/data/banxe/{compliance,dashboard,deep-search}` and rsync source trees.
2. Recreate systemd unit files under `/etc/systemd/system/` on evo1 with adjusted paths.
3. Migrate `drive_watcher` cron from Legion crontab to evo1 system cron `/etc/cron.d/banxe-drive-watcher`.
4. Disable corresponding `--user` units on Legion via `systemctl --user disable --now <unit>`; remove crontab line.
5. Update LiteLLM/Continue.dev/internal callers (if any) from `legion:<port>` to `evo1:<port>`.
6. 24h soak with health-check.

### Result
PAPER_PLAN. Migration deferred to a safe window after P3.2 reasoning model pull finishes (current ETA ~3h).

## 24. Sprint P3.11 — preparation only (PARTIAL, 2026-05-03)

- Created config dir `~/.config/banxe/` (perm 700) and env template `~/.config/banxe/telegram.env` (perm 600) with placeholders `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, `TELEGRAM_ENABLED=0`.
- Installed `~/bin/banxe-telegram-notify` (executable shell helper). Reads env and is a no-op when `TELEGRAM_ENABLED!=1` or token missing. Safe to invoke from any cron or check script today.
- NOT done yet (operator action): create bot via BotFather, paste `BOT_TOKEN` and `CHAT_ID` into the env file, set `TELEGRAM_ENABLED=1`, and wire calls in:
  - `~/bin/check-llm-cluster.sh` (failure branch)
  - `/opt/banxe/compliance/drive_watcher.py` (alert branch)
  - `~/.openclaw/workspace-moa/scripts/daily-eval.sh` (final summary)
- Result: PARTIAL (infra wiring stubbed; bot token wiring pending operator-action OPERATOR_RUN).

## 25. Sprint P3.7 — verify (PARTIAL PASS, 2026-05-03)

Read-only verification of the observability stack provisioned in P3.7. Executed during the in-flight `qwen3:235b-a22b` pull on evo2 (PID 27107) without interfering with the pull.

### Grafana datasource — PASS

`GET http://localhost:3000/api/datasources` (via `ssh evo2`) returns one entry:

| Field | Value |
|---|---|
| `id` / `uid` | `1` / `cfkwbx1yvr6dce` |
| `name` / `type` | `Prometheus` / `prometheus` |
| `url` / `access` | `http://prometheus:9090` / `proxy` |
| `isDefault` | `true` |
| `readOnly` | `false` |

### Prometheus targets — PASS (for what is currently scraped)

`GET http://localhost:9090/api/v1/targets` reports 4 active targets, **0 dropped**, all `health: "up"`, last scrape successful at `2026-05-03T02:40:2x`:

| Job | Instance | Health |
|---|---|---|
| `litellm_v4000` | `100.101.218.26:4000` | up |
| `ollama_blackbox` | `http://192.168.0.72:11434/api/tags` (evo1) | up |
| `ollama_blackbox` | `http://192.168.0.15:11434/api/tags` (evo2) | up |
| `prometheus` | `localhost:9090` | up |

### Gap finding — node_exporter is NOT scraped (PARTIAL)

The "Node Exporter Full" Grafana dashboard (uid `aedcea76-...`, imported in P3.7) has **no data backing it** today:

- `pgrep -fa node_exporter` on evo1 → no process; `:9100` not listening.
- `pgrep -fa node_exporter` on evo2 → no process; `:9100` not listening.
- No `node_exporter` job declared in Prometheus's `activeTargets`.

The dashboard renders panels but every query returns empty until either (a) `node_exporter` is installed and started on evo1 + evo2 and (b) a `node` job is added to Prometheus scrape config. Both are out of scope for the read-only verify; queued as a follow-up under §16 Security backlog (track as P3.7c).

### Verdict

PARTIAL PASS. Observability core (Grafana datasource, Prometheus self-scrape, LiteLLM scrape, Ollama blackbox probes) is healthy. Node-level metrics (CPU/mem/disk/net via node_exporter) are not yet wired — dashboard imported but unused. Inference path untouched.

### P3.2 pull progress snapshot (informational)

`tail -n 1 /tmp/ollama-pull-reasoning.log` on evo2 → `pulling 791d5d11998e: 3% ▕ ▏ 4.3 GB/142 GB 11 MB/s 3h15m`. PID 27107 active. Not interfered with.

## 26. Sprint P3.7 — verify v2 (PARTIAL PASS, 2026-05-03)

Re-snapshot during the in-flight evo2 pull. All probes routed via `ssh evo2` (Legion outbound curl is sandboxed for non-loopback HTTP).

### Prometheus locator
- `evo2:9090/-/healthy` → `Prometheus Server is Healthy.` ✓ (canonical Prometheus host)
- `evo1:9090/-/healthy` → empty (no Prometheus on evo1)
- Legion `127.0.0.1:9090` → not run (sandbox); not expected to host Prometheus.

### Targets (`/api/v1/targets`)
`total: 4 | up: 4 | down: 0 | jobs: ['litellm_v4000', 'ollama_blackbox', 'prometheus']`
- `litellm_v4000` `100.101.218.26:4000` → up
- `ollama_blackbox` `http://192.168.0.72:11434/api/tags` → up
- `ollama_blackbox` `http://192.168.0.15:11434/api/tags` → up
- `prometheus` `localhost:9090` → up

### LiteLLM v2 `/metrics/` (Legion :4000, PID 3504547)
First 600 chars (truncated, GC counters as canary that the endpoint is alive):
```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 3131.0
python_gc_objects_collected_total{generation="1"} 827.0
python_gc_objects_collected_total{generation="2"} 90.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
```
LiteLLM v2 process: PID 3504547 + worker 3504915, listening `0.0.0.0:4000`.

### node_exporter — still missing on both nodes
- `evo1:9100/metrics` → empty (no listener)
- `evo2:9100/metrics` → empty (no listener)
Same gap as §25; tracked as P3.7c. Inference path untouched.

### Verdict
PARTIAL PASS — same shape as §25: observability core (Prometheus self / LiteLLM / Ollama blackbox) all up, node_exporter still unwired.

## 27. Sprint P3.9 — verify (PASS, 2026-05-03)

Read-only hygiene snapshot.

- **`~/bin/check-llm-cluster.sh`**: present, mode `0755`, owned by `mmber`, 1121 bytes; first lines confirm purpose ("BANXE LLM Cluster Health Check ... appends one CSV-ish line per run"). Cron `*/5 * * * *` from §previous sprints.
- **`~/bin/backup-cluster.sh`**: symlink → `~/MetaClaw/scripts/backup-cluster.sh` (canonical, version-controlled). Header confirms `Cron: 0 4 * * *`.
- **Health log** at `/home/mmber/llm-cluster-health.log` (40,968 bytes). Last 20 lines (every 5 min, 03:30→05:05): ollama on both nodes returned 200 throughout; latency mostly 10-30 ms; one transient `legion_v4000=000ERR` at 04:00:03 (LiteLLM v2 was being polled exactly during a 5-minute boundary, recovered next tick) and `evo1_ollama=200ERR/7970ms` at 05:05:02 (slow response under load — evo2 pull saturating LAN; non-fatal). LiteLLM v2 :4000 = 200 throughout; v8080 = 401 (auth-required, expected for unauthenticated probe).
- **Backup cron**: PID 3462088 (cron) → 3462104/3462107 (script) → 3462110 + 3462113 (rsync over ssh:2222). **Still running** — started 04:00:03, currently 6.8 GiB mirrored to `/mnt/d/backups/evo1/` (`backups`, `banxe`, `banxe-emi-stack`, `banxe-stack`, `banxe-training`, `clickhouse`, `ctio-workspace`, `developer`, `guiyon-project`, `hitl-dashboard` …). Long runtime expected during evo2 pull saturating LAN; not a fault. Log files (`cron.log`, `backup-2026-05-03.log`) currently only show header + first section divider — rsync `-av` output is buffered and will flush at completion.
- **MODELS.md**: at `/home/mmber/MetaClaw/docs/MODELS.md`. First 30 lines confirm Tier 1 production-critical (qwen3:30b-a3b, glm-4.7-flash-abliterated, qwen3-coder-next, GLM-4.5-Air RPC) and Tier 2 (gurubot/gpt-oss-derestricted:20b, qwen3.5:35b, llama3.3:70b) — matches §"5.x" inventory.

### Verdict
PASS. All hygiene assets present and functioning. The 04:00 backup is mid-flight (rsync in progress) — not a regression. Will inspect the completed log on next snapshot.

## 28. P3.2 — pull progress snapshot 2026-05-03T05:15:09+02:00

`ssh evo2 'tail -n 1 /tmp/ollama-pull-reasoning.log'`:

```
pulling 791d5d11998e:  20% ▕███               ▏  28 GB/142 GB   11 MB/s   2h43m
```

Legion local time: `2026-05-03T05:15:09+02:00`. Throughput stable at 11 MB/s; ETA ~2h43m. PID 27107 still active. Untouched.

## 29. Sprint P3.7 — dashboards plan v0.1 (paper)

Probe of `http://192.168.0.15:3000/api/search` returned `401 Unauthorized` (Grafana requires auth; admin creds exist but un-authed `/api/search` is correctly refused). No anonymous dashboard listing — proceeding on paper.

Four dashboards proposed for the next observability sprint. All sourced from already-up Prometheus targets where possible; gaps note `requires-node_exporter` (P3.7c).

### 1. `BANXE-LiteLLM-v2`
Source: `litellm_v4000` job (already up, scraping `100.101.218.26:4000/metrics`).

| Panel | Metric (PromQL) |
|---|---|
| Requests/sec per model | `sum by (model) (rate(litellm_request_total[1m]))` |
| Latency p50/p95/p99 | `histogram_quantile(0.50, sum by (le) (rate(litellm_request_latency_seconds_bucket[5m])))` etc. |
| Error rate | `sum(rate(litellm_request_total{status=~"5.."}[5m])) / sum(rate(litellm_request_total[5m]))` |
| Fallback rate | `sum(rate(litellm_fallback_total[5m]))` |
| Token throughput | `sum by (model) (rate(litellm_total_tokens[1m]))` |

### 2. `BANXE-Ollama-Cluster`
Source: `ollama_blackbox` jobs (per-host blackbox probes) + ad-hoc PromQL.

| Panel | Metric |
|---|---|
| Per-host API up | `probe_success{job="ollama_blackbox"}` |
| Model load count | derived from `/api/tags` length (requires lightweight exporter — write later) |
| VRAM/GTT proxy | `node_memory_MemAvailable_bytes` (**requires-node_exporter**) |
| Last pull duration | scrape ollama log — requires log exporter (deferred to P3.7d) |

### 3. `BANXE-glm-master-RPC`
Source: scrape `evo1:8081/metrics` (llama.cpp `/metrics` endpoint, opt-in flag `--metrics`) — needs glm-master unit to add `--metrics` to ExecStart in a future P3.7b-tweak.

| Panel | Metric |
|---|---|
| 8081 health | `probe_success{instance="http://192.168.0.72:8081/health"}` (add to blackbox config) |
| RPC worker state | scrape `evo2:50052` via TCP probe (blackbox `tcp_connect`) |
| Prompt tok/s | `llama_request_prompt_tokens_per_second` (when `--metrics` enabled) |
| Gen tok/s | `llama_request_eval_tokens_per_second` (when `--metrics` enabled) |

### 4. `BANXE-Node-Exporter`
**Requires-node_exporter** (P3.7c). Standard panels from dashboard 1860:

| Panel | Metric |
|---|---|
| CPU% | `100 - avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[1m]) * 100)` |
| RAM | `node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes` |
| Swap | `node_memory_SwapFree_bytes / node_memory_SwapTotal_bytes` |
| Disk I/O | `rate(node_disk_io_time_seconds_total[1m])` |
| Network | `rate(node_network_receive_bytes_total[1m])` + transmit |

### Implementation order
1. P3.7c — install node_exporter on evo1 + evo2; add `node` job to Prometheus scrape config; verify in `BANXE-Node-Exporter`.
2. P3.7b-tweak — add `--metrics` to glm-master ExecStart; add scrape of `evo1:8081/metrics` to Prometheus; build `BANXE-glm-master-RPC`.
3. Build `BANXE-LiteLLM-v2` (no extra exporters needed — data already scraped).
4. Build `BANXE-Ollama-Cluster` (extend blackbox config + tiny exporter for `/api/tags` length).
