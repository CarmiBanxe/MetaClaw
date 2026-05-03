# BANXE Cluster Phase 4 — Roadmap

**Last Updated:** 2026-05-04
**Status:** ACTIVE
**Predecessor:** banxe-cluster-v2.2-phase3.md (CLOSED) + banxe-cluster-v2.3-phaseN.md (Phase A Guardian closed_on_pilot_scope).

## Sprint backlog

### P4-Guardian-Rollout — раскат guardian.yml на 13 оставшихся PR-репо

**Carryover из Phase A.5.11–A.5.12 (deferred 2026-05-04).**

**Status:** PLANNED.
**Trigger:** низкое PR-flow окно, ~45-60 минут operator time.

**Scope:**
- 13 репо CarmiBanxe с открытыми factory/ai-onboarding PR (исключая MetaClaw, который pilot).
- На каждом: 3 GitHub secrets (TS_AUTHKEY + TS_GUARDIAN_FACTORY_URL + TS_GUARDIAN_PROJECT_URL).
- Cherry-pick guardian.yml workflow из ~/factory/banxe-repo-template/.
- Verify Guardian run для каждого репо (factory + project pass или PASS_WITH_OVERRIDE per ADR-022).
- Branch protection rule per репо (Guardian status checks required).

**Prerequisites:**
- Tailscale auth key валиден (90-day expiration, current key создан 2026-05-03).
- Guardian backbone services (factory:8195 + project:8196) на evo1 active.
- ClickHouse audit table accepting writes.

**Estimated effort:** 39 interactive `gh secret set` commands + 13 cherry-picks + 13 branch protection rules.

**Rationale for deferral:** Phase A pilot validates entire chain end-to-end (commit 6087574 + 3022d7a, run 25292381072 success). Full rollout — operations work, не architecture; benefits from being a separate planned sprint.

### P4-Guardian-Rule-Engine-V2 — обновить r7_factory_baseline_locked для ADR-022 logic

**Status:** OPEN.
**Trigger:** после первого full rollout (P4-Guardian-Rollout DONE).

**Scope:**
- Update ~/MetaClaw/guardian/src/rules/factory_rules.py: r7_factory_baseline_locked() должен возвращать PASS если diff trogает ТОЛЬКО Guardian artefacts И PR body содержит "Refs: ADR-022".
- Add tests: PR с ADR-022 ref + Guardian-only diff → PASS; без ref → BLOCK; с ADR-022 ref но non-Guardian diff → BLOCK.
- Deploy update via rsync на evo1 + restart banxe-guardian-factory.service.

### P4 backlog (carryover из Phase 3 v2.2 §47)
- P3.4-followup-2 — drive_watcher.py source restoration.
- P3.2 / P4.3 — BIOS UMA evo2 (qwen3:235b-a22b unlock).
- MiroFish prod-hardening.
- CVE-2026-25253 — OpenClaw upgrade.
- P4.1 — QClaw Computer Use на Legion.
- P4.2 — ROCm 6.4 migration.
- P4.3 — BIOS UMA evo1 (37 → 70+ tok/s).
- P4.4 — XDNA 2 NPU utilization.
- P4.5 — LLM Document Translation Pipeline.
- P4.6 — n8n workflow + Atom AI.
- COMPLIANCE-OPS-2 — запрет manual uvicorn вне systemd.
- Factory CI scope tweak (.venv exclude).
- Factory secrets batch (когда ANTHROPIC_API_KEY).
- midaz-ledger Redis IP fix.
