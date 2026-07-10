# EMI BANXE Ideal Engine (Math) — Coverage (BEN / CENTRAL)
Date: 2026-07-10
Provenance:
- Source: docs/sources/emi-banxe-ideal-engine-math-2026-07-10.md (sha 8612f7ebb76004f9)
- Intel: docs/audit/emi-banxe-ideal-engine-math-intel-2026-07-10.md
Method: marker + code-context-verify; reuse world-experience/engine; numbers = code-matches.

M1 PRAGMA transformer/encoder | Статус: MISSING | Доказательство: 0 matches | GATED (credit) | Рекомендация: post-licence.
M2 GNN/FraudGNN | Статус: IMPLEMENTED | Доказательство: services/crypto_aml_graph/service.py (GraphSageInference) | GATED (AML/fraud) | Рекомендация: существует; расширение — post-licence.
M3 Federated/FATE | Статус: MISSING | Доказательство: 0 matches | GATED | Рекомендация: post-licence; связать с world-exp A1.
M4 RL agentic decisions | Статус: MISSING (false-positive "rl" substring отсеян) | Доказательство: 285 = supported/register, не RL | Рекомендация: NON-GATED; связать с BDSL RLHF (gated).
M5 NeMo Guardrails | Статус: MISSING (own guardrails ≠ NeMo) | Доказательство: intent_layer/canary.py, voice_support consent | Рекомендация: NON-GATED safety; рассмотреть NeMo поверх существующих guardrails.
M6 DeerFlow/Strands/Manus orchestration | Статус: MISSING | Доказательство: 0 matches | Рекомендация: NON-GATED reliability; выбор vs LangGraph — ADR.
M7 Temporal/Kafka/Qdrant/Langfuse | Статус: MISSING (reuse world-exp C) | Доказательство: см. world-experience coverage | Рекомендация: NON-GATED reliability; не дублировать.
M8 ClickHouse decision-lineage | Статус: IMPLEMENTED (reuse C1/F4) | Доказательство: infra/clickhouse/a2a_events.sql | Рекомендация: reuse, без задач.
Summary: IMPLEMENTED=2 (GNN gated, ClickHouse reuse) PARTIAL=0 MISSING=6 GATED=3 (PRAGMA/GNN/FATE)
