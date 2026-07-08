# BEN Coverage Report — BDSL novelties vs code (R4)

**Date:** 2026-07-09
**By:** BEN (right terminal / document-intelligence)
**Intel source:** `docs/audit/bdsl-intel-2026-07-09.md`
**Doc source:** `docs/sources/bdsl-self-learning-loop-2026-07-09.md`
**Provenance:** source sha256 `58089f2d1a070d643d203c0b3fb206a41718b6fef37ceeca8fe6720a0a7e7dce` (41288B).
**Policy:** per `docs/canon/ben-right-terminal-canon.md` §7 R4 (coverage obligation), R5 (single-entry-on-disk).
Tags: [ФАКТ] = marker+context verified; [ВЫВОД] = recommendation; [НЕИЗВЕСТНО] = not determinable.

> **Method note:** statuses by **marker analysis + context verification** across `~/banxe-ai-infrastructure`,
> `~/banxe/banxe-emi-stack`, `~/banxe-emi-stack-main`, `~/MetaClaw` (excl `.git`, `__pycache__`, `~/wt/`,
> `.bundle`, `docs/sources`, `docs/audit`). False positives filtered: broad `record_id` (→ PARTIAL, not
> IMPLEMENTED, since not the full BDSL schema); the phrase "append-only" in prose vs real WORM (34 files);
> regulatory **PSR/PSD** tokens ≠ **PSI** drift. [ФАКТ]

---

## Coverage table
| Novelty (BDSL §) | Markers | Status | Evidence (file:line) | CENTRAL recommendation |
|---|---|---|---|---|
| HITL tiers / autonomy (§4.1) | `autonomy_level`, `HITLProposal`, tier AUTO/REVIEW/BLOCK | **IMPLEMENTED** | `banxe-ai-infrastructure/a2a_bus/chain_registry.py:20,26` (AutonomyLevel L1-L4) | — keep; align 0.90/0.95 tiers with BDSL |
| DecisionRecord schema (§1) | `class DecisionRecord`, `decision_record`, `record_id` | **PARTIAL** | `services/reasoning_bank/models.py`, `services/agents/_lineage.py`, `api/routers/intent.py` | **implement** — extend to full schema (decision_space/utility_computation/minimax_regret/bias_flags), Annex IV |
| hash-chain / WORM (§1,§8.2) | `prev_record_hash`, `hash-chain`, `WORM`, `append-only` | **PARTIAL** | WORM/immutable-audit (34 files); no `prev_record_hash` chain | **implement** — add hash-chain over existing WORM, Art.12 immutability |
| decision-lineage / ClickHouse (§1,§6.2) | `agent_decisions`, `_write_audit`, `audit_event_id` | **PARTIAL** | `api/routers/safeguarding.py:119,318`, `src/api/gateway.py`, `_lineage.py` | **implement** — complete full lineage write (I-24) |
| ImprovementProposal (§5.2) | `ImprovementProposal` | **MISSING** | 0 | **implement** — human-gated proposal loop, Art.14 oversight |
| Brier score (§3.2) | `brier_score`, `brier` | **MISSING** | 0 | **implement** — MetricsEngine, Art.15 accuracy |
| ECE (§3.2) | `expected_calibration`, `ece` | **MISSING** | 0 | **implement** — calibration metric, Art.15 |
| Regret metrics (§3.1) | `avg_regret`, `regret_matrix`, `minimax_regret` | **MISSING** | 0 | **implement** — MetricsEngine regret/MMR, Art.15 |
| Pareto efficiency (§3.4) | `pareto_efficiency`, `pareto_frontier` | **MISSING** | 0 | **implement** — PER metric, Art.15 |
| agent_quality_metrics registry (§6.2) | `agent_quality_metrics` | **MISSING** | 0 | **implement** — Decision Quality Registry, Art.17 QMS |
| RLHF / reward-model (§5.3) | `reward_model`, `preference_data`, `RLHF` | **MISSING** | 0 | GATED (post-licence) — RLHF policy-update for credit/payment |
| Contrastive / prospect-bias probes (§4.3) | `contrastive probe`, `prospect_bias`, `bias_flags` | **MISSING** | 0 | **implement** — bias probes, Art.15 robustness |
| Satisficing / stopping-rule (§1.2,§5.4) | `satisficing`, `stopping_rule`, `exploration_ratio` | **MISSING** | 0 | GATED (post-licence) — satisficing forbidden in payment; non-payment only |
| PSI / concept-drift (§5.4) | `population_stability`, `PSI`, `concept_drift` | **MISSING** | 0 (regulatory PSR/PSD filtered) | **implement** — drift monitoring, Art.9 risk-mgmt |

## Summary
**1 IMPLEMENTED / 3 PARTIAL / 10 MISSING** (14 novelties).
- IMPLEMENTED: HITL tiers.
- PARTIAL: DecisionRecord schema, hash-chain/WORM, decision-lineage.
- MISSING: ImprovementProposal, Brier, ECE, Regret, Pareto, quality-registry, RLHF, bias-probes, satisficing, PSI-drift.

## CENTRAL recommendations
### GATED — NOT recommended now (post-licence, B-EMI-CREDIT-GATE-001)
[ВЫВОД] DecisionRecord **CREDIT domain** + **payment-autonomy** + **RLHF policy-update** for credit/payment +
**satisficing** in payment contour — outside TOMPAY EMI licence. Mark post-licence; do not task the factory yet.

### NON-GATED — recommend to factory (priority: compliance → reliability → safety)
[ВЫВОД] Coverage-gap recommendations for CENTRAL to task Aider (INV-01 — BEN does not write code):
1. **DecisionRecord strict schema** — extend `reasoning_bank/models.py` (decision_space/utility_computation/minimax_regret/bias_flags) — **Annex IV** tech-doc.
2. **hash-chain `prev_record_hash`** over existing WORM — **Art.12** immutability/audit.
3. **MetricsEngine (Brier/ECE/Regret/PER)** — none exist — **Art.15** accuracy.
4. **agent_quality_metrics registry** (Decision Quality Registry) — **Art.17** QMS.
5. **ImprovementProposal human-gate loop** — **Art.14** human oversight.
6. **PSI / concept-drift monitoring** — **Art.9** risk management.
7. **Contrastive prospect-bias probes** — **Art.15** robustness.
