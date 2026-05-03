# BANXE — Roadmap Index
Last updated: 2026-05-03 · Status: ACTIVE

Canon: одна команда → её вывод → следующая. ZERO questions on safe ops. Best-answer self-resolution. Промты и команды разделяются на связанные части если велики.

## 1. Three planes

### 1.1 Project (BANXE EMI bank) — ЧТО строим
Source of truth: `~/banxe-architecture/docs/ROADMAP-MATRIX.md`.
- Delivery matrix: 10 blocks (A — Customer Onboarding, B — Product Catalogue, C — Payment Rails, D — Core Banking Engine, E — Treasury/ALM/Safeguarding, F — Compliance & Risk, G — Fraud Prevention, H — Customer Operations, I — Technology & Infrastructure, J — Safeguarding Engine).
- Hard P0 deadline: **FCA CASS 15 — 7 May 2026** (E-safeguard, J-engine).
- ADRs: 42 total (17 in `~/banxe-architecture/decisions/`, 11 in `~/banxe-architecture/adrs/`, 14 in `~/banxe-emi-stack/docs/adr/`).
- Governance: `~/banxe-architecture/{constitution/,HITL-MATRIX.yaml,GAP-REGISTER.md,INSTRUCTION-LEDGER.md,MEMORY.md,PROMPT-CANON-PROJECT.md}`.
- Active sprints: `~/banxe-emi-stack/docs/SPRINT-13-AUDIT.md`, `SPRINT-15-AUDIT.md`, `BLOCKED-TASKS.md`, `STUB-INVENTORY.md`.

### 1.2 Factory (developer factory) — КАК строим
Source of truth: `~/factory/banxe-repo-template/` + Phase 3 v2.2 §42 + v2.3 §F-secrets.
- Template artefacts: `.claude/settings.json` (canon + 7 commands + 3 deny_paths + automations: pr_review/test_runner/security_scan), `.github/workflows/{claude.yml,factory-guard.yml}`, README.md.
- Rollout v2 report: `~/factory/rollout-v2-report.md` + `~/factory/rollout-v2-results.tsv` (15 PR repos opened, 14 with full baseline).
- Pilot 3 separate path: `banxe-payment-core`, `banxe-ui`, `banxe-infra` (PR #1 each).
- Open factory followups: ANTHROPIC_API_KEY batch (v2.3 DEFERRED), Factory CI scope tweak (.venv exclude), COMPLIANCE-OPS-2 (запрет manual uvicorn вне systemd).

### 1.3 Cluster + Hardware — НА ЧЁМ строим
Source of truth: `~/MetaClaw/docs/roadmap/banxe-cluster-v2.{2-phase3,3-phaseN}.md`.
- Phase 3 v2.2 — CLOSED 2026-05-03 (47 sections, MOSTLY_PASS, см. §47 closing summary).
- Phase 3 v2.3 — ACTIVE mini-sprints: F1 PASS (compliance-api 8194), F3 PASS (deep-search canonical 8088), F-secrets DEFERRED.
- Hardware × Model upgrade: `~/MetaClaw/docs/roadmap/HW-MODEL-UPGRADE-matrix.md` (Часть 3/3).
- Inventory: `~/MetaClaw/docs/inventory/banxe-cluster-inventory.md`.

## 2. Cross-references (Project ↔ Factory ↔ Cluster)
- **ADR-016** (banxe-architecture/decisions/ADR-016-ai-plane-pii-aml-routing.md) и **ADR-021** (banxe-emi-stack/docs/adr/ADR-021-ai-plane-pii-aml-routing.md) — PII/AML routing canon — связывают Factory deny_paths, Project compliance flow, Cluster LiteLLM v2:4000.
- **Block I — Technology & Infrastructure** в ROADMAP-MATRIX = execution в Phase 3 v2.2 + v2.3.
- **Block J — Safeguarding Engine** в ROADMAP-MATRIX (P0 deadline 7 May) blocked on banxe-compliance-api stable serve, что закрыто в v2.3 §F1 (8194 LIVE).
- **Factory baseline** (.claude/settings.json deny_paths: compliance/cases, kyc/raw, secrets, .env, *.pem, id_*) enforces ADR-016 на build time для всех 14 rollout repos.

## 3. Open carryover (15 items)
Источник: v2.2 §47 + v2.3 §FINAL.
1. P3.4-followup-2 — drive_watcher.py source restoration.
2. P3.2 / P4.3 — BIOS UMA rebalance evo2 (qwen3:235b-a22b unlock).
3. MiroFish prod-hardening (gunicorn, --no-open).
4. CVE-2026-25253 — OpenClaw upgrade (≥ 2026.1.29).
5. P4.1 — QClaw/OpenClaw Computer Use на Legion Windows host.
6. P4.2 — ROCm 6.4 migration на обоих EVO-X2.
7. P4.3 — BIOS UMA rebalance evo1 (96 iGPU / 32 CPU → 64/64; 37 → 70+ tok/s).
8. P4.4 — XDNA 2 NPU utilization (252 TOPS aggregate).
9. P4.5 — LLM Document Translation Pipeline.
10. P4.6 — n8n workflow engine + Atom AI review.
11. COMPLIANCE-OPS-2 — запрет manual uvicorn вне systemd на evo1.
12. Factory CI scope tweak — exclude .venv/vendored from ruff/secrets-scan.
13. Factory secrets enablement — ANTHROPIC_API_KEY × 14 PR repos.
14. Legacy banxe-api.service consolidation (decision: оставить).
15. midaz-ledger Redis IP fix (host.docker.internal vs 172.22.0.1).

## 4. Hand-off triggers
- FCA CASS 15 deadline (7 May 2026) → активизирует Block E + J P0.
- BIOS UMA rebalance (P4.3) → разблокирует qwen3:235b-a22b reasoning.
- Pilot 3 PR merge → закрывает Factory Rollout v2 фактически.

## 5. Canonical target architecture (LOCKED)
Per **ADR-018** (`~/banxe-architecture/decisions/ADR-018-hybrid-5-layer-ai-compute.md`): **5-layer hybrid AI compute** — Reasoning RPC / Mid-size LB / Small NPU / Cloud meta / LiteLLM router. Asymmetric BIOS UMA (evo1=96/32 AI heavy, evo2=32/96 CPU heavy). See HW-MODEL-UPGRADE-matrix.md §8 for sprint plan to 100%.

## 5. Canonical target architecture (LOCKED)
Per **ADR-018** (`~/banxe-architecture/decisions/ADR-018-hybrid-5-layer-ai-compute.md`): **5-layer hybrid AI compute** — Reasoning RPC / Mid-size LB / Small NPU / Cloud meta / LiteLLM router. Asymmetric BIOS UMA (evo1=96/32 AI heavy, evo2=32/96 CPU heavy). See HW-MODEL-UPGRADE-matrix.md §8 for sprint plan to 100%.
