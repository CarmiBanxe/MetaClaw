# BEN Coverage-Gap Backlog — unified (3 documents)

Date: 2026-07-09
By: BEN (right terminal) / consumed by CENTRAL for factory tasking.
Provenance (source coverage reports + sha):
- docs/audit/engine-doc-coverage-2026-07-08.md (sha e0569864)
- docs/audit/bdsl-coverage-2026-07-09.md (sha e37f7730)
- docs/audit/watchdog-roadmap-coverage-2026-07-09.md (sha 218831dd)
Policy: R1-R7. INV-01 (Aider = sole executor; BEN/CENTRAL do not write code).
Cloud: origin/main @ 4686fbd (synced).

## GATED backlog (post-licence — B-EMI-CREDIT-GATE-001, DO NOT task factory)
- PRAGMA-encoder (engine) — credit/scoring
- GNN/FraudGNN (engine) — fraud/credit
- FATE/Federated (engine) — cross-bank
- RLHF policy-update (bdsl) — credit/payment
- Satisficing-in-payment (bdsl) — payment contour
- Payment/CDE watchdog auto-repair, ALTER USER (watchdog) — PCI DSS Req 6.4 MANUAL-ONLY

## NON-GATED backlog (candidates for factory, priority compliance -> reliability -> safety)

| # | Gap | Source | Status | Reg ref | Priority |
|---|---|---|---|---|---|
| 1 | SHAP/LIME explainability | engine | MISSING | EU AI Act Art.15 high-risk | compliance |
| 2 | decision-lineage full ClickHouse agent_decisions | engine+bdsl | PARTIAL | Art.17 / I-24 5y | compliance |
| 3 | DecisionRecord strict schema | bdsl | PARTIAL | Annex IV | compliance |
| 4 | MetricsEngine: Brier/ECE/Regret/Pareto | bdsl | MISSING | Art.15 accuracy | compliance |
| 5 | agent_quality_metrics registry | bdsl | MISSING | Art.17 QMS | compliance |
| 6 | ImprovementProposal human-gate loop | bdsl | MISSING | Art.14 oversight | compliance |
| 7 | hash-chain prev_record_hash over WORM | bdsl+watchdog | PARTIAL | Art.12 / PCI Req10 | compliance |
| 8 | PSI / concept-drift monitoring | bdsl | MISSING | Art.9 risk-mgmt | reliability |
| 9 | Temporal durable workflows | engine | MISSING | idempotency | reliability |
| 10 | watchdog root-cause classifier | watchdog | MISSING | Tier-2 diagnostic | reliability |
| 11 | watchdog-exporter + dead-man-switch + guardian evo2 | watchdog | MISSING | SPOF/observability | reliability |
| 12 | config_loader (remove hardcode threshold=10) | watchdog | MISSING | crash-loop safety | reliability |
| 13 | Vault AppRole read-only sidecar | watchdog | MISSING | secrets Q9 | reliability |
| 14 | systemd banxe-watchdog.service | watchdog | MISSING | resilience | reliability |
| 15 | node-reachability multi-vantage (Legion) | watchdog | MISSING | node vs partition | reliability |
| 16 | contrastive prospect-bias probes | bdsl | MISSING | Art.15 robustness | safety |
| 17 | NeMo Guardrails | engine | MISSING | LLM-safety | safety |
| 18 | Qdrant vector-store | engine | MISSING | Phase 2-3 memory | deferred |

## CENTRAL recommendation (single best first step)
[INFER] First NON-GATED item to task the factory: #1 SHAP/LIME explainability.
Rationale: EU AI Act Art.15 high-risk requirement for credit/automated decisions; it is a hard
regulatory gate for going live, has zero current implementation (clean MISSING), and does not
depend on other gaps. Compliance-critical, standalone, highest leverage. Operator go required.

## Constraints
[FACT] Backlog only. No code written, Aider not invoked. GATED items not tasked. Awaiting operator go.
