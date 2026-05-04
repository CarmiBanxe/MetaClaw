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

---

## Execution log (2026-05-04)

### P4.3-evo2 — BIOS UMA rebalance ✅ DONE
- Operator выполнил BIOS edit + reboot per runbook a971439.
- Result: `mem_info_vram_total=32 GiB` (was 64), `MemTotal=93 GiB visible` (UMA 32/96).
- All services post-reboot healthy: ollama + llama-rpc-worker + node-exporter + grafana + blackbox.
- Ledger: `INS-2026-05-04-P4.3-EVO2` (commit d99a5f5).

### P4.3-Q235 — qwen3:235b-a22b unblock ❌ BLOCKED (4 attempts)
1. **Attempt 1 — Ollama direct (post UMA rebalance):** OOM. Vulkan reports false `total=152 GiB`, kernel kills at 32 GiB physical iGPU.
2. **Attempt 2 — Ollama `num_gpu:0` CPU-only:** rejected upfront (`requires 132.9 GiB > available 99.8 GiB`). Ollama loader pre-allocates full size for MoE.
3. **Attempt 3 — llama-server standalone CPU-only on evo2:8082:** crash-loop NRestarts=35, OOM at mmap (mmap не освобождает active MoE working set).
4. **Attempt 4 — llama.cpp RPC split (master evo2:8082 + worker evo1:50053):** crash-loop NRestarts=5, OOM at `--n-gpu-layers 999` (master-side embeddings + KV cache + output projection > 32 GiB iGPU).
- Reasoning route stays на llama3.3:70b LB. Three future paths documented:
  - (a) `--n-gpu-layers 0` master + RPC GPU worker (likely same Vulkan UMA trap)
  - (b) **Q3_K_S requantize ~80 GiB** — IN PROGRESS (PID 46244 на evo2, ETA ~30-60 min)
  - (c) Wait Ollama 0.24+ MoE-aware loader (upstream)
- Ledgers: `INS-2026-05-04-P4.3-Q235-DEFER` (6aed15f), `INS-2026-05-04-P4.3-Q235-RPC-BLOCKED` (75b0b88).
- Runbook: docs/runbooks/p4.3-q235-rpc-split.md (commit 64f6800).

### P4.2-ROCm — Vulkan → ROCm migration ❌ BLOCKED
- Phase A executed on evo1 (ROCm 6.3 + bundled ollama rocm runner).
- Vulkan baseline: llama3.3:70b 4.50 tok/s, qwen3.5:35b 24.5 tok/s.
- ROCm result: `unable to allocate ROCm0 buffer` for ALL model sizes (4 GB, 23 GB, 42 GB).
- Diagnosis: HIP buffer allocation broken на gfx1151 + ollama 0.22.1 + ROCm 6.3 + UMA carveout. `library=ROCm total=216 GiB` reported but every allocate fails.
- Rollback: clean (1-line sed revert). Vulkan restored, regression-free.
- Defer: ROCm 7.0+ release with proper gfx1151 UMA APU support OR mainline kernel ≥6.13 HSA fixes.
- Ledger: `INS-2026-05-04-P4.2-ROCM-BLOCKED` (1815372).
- Runbook: docs/runbooks/p4.2-rocm-migration.md (commit e802745).

### P4.4-NPU — XDNA 2 NPU enablement ⏸️ PAUSED on operator decision gate
- Discovery DONE: both nodes have NPU hardware (evo1 PCI c7:00.1, evo2 c6:00.1), amdxdna kernel driver bound, `/dev/accel/accel0` exposed, render group includes prod users.
- Userspace gap: XRT, onnxruntime-vitis-ai, Ryzen AI SDK не установлены.
- TOPS correction: HW matrix теперь правильно показывает 50 TOPS NPU/node (~100 aggregate), а не 252 (system AI total inc. iGPU+CPU).
- Runbook: docs/runbooks/p4.4-npu-discovery-and-plan.md (commit 156e10d) — 5-phase plan A→E.
- Operator gate: 4-6h dedicated session + accept experimental SDK on prod nodes — pending.
- Ledger: `INS-2026-05-04-P4.4-NPU-DISCOVERY` (6cb3e68).

---

## Status summary 2026-05-04 14:30 CEST

| Sprint | Status | Outcome |
|---|---|---|
| P4.3-evo2 | ✅ DONE | UMA 32/96 active; qwen3:235b-a22b unblock attempted but file-size separately blocked |
| P4.3-Q235 | ❌ BLOCKED → ⏳ Q3_K_S requantize in flight | requantize PID 46244 ETA 30-60 min |
| P4.2-ROCm | ❌ BLOCKED | defer ROCm 7.0+ |
| P4.4-NPU | ⏸️ PAUSED | discovery + runbook done, install gated |
| HW matrix TOPS | ✅ DONE | 4 правки в matrix (commit 52f74a2) |
