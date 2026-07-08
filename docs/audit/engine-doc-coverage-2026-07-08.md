# BEN Coverage Report — EMI BANXE Engine novelties (R4)

Date: 2026-07-08
By: BEN (right terminal / document-intelligence)
Intel source: docs/audit/engine-doc-intel-2026-07-06.md
Doc source: docs/sources/emi-banxe-engine-2026-07-06.md
Provenance: engine-doc sha256 9ef1b0308d9602a795b408111b1bddb3e127a9728f15b0cc4b3aea4a2257ef34 (49979B).
Policy: per docs/canon/ben-right-terminal-canon.md §7 R4 (coverage obligation).
Tags: [ФАКТ] verified by marker+context; [ВЫВОД] BEN recommendation; [НЕИЗВЕСТНО] not determinable.

Method note: statuses assigned by marker analysis (exact class/function/schema/endpoint signatures)
with context verification (prod vs tests, real client vs monitoring, schema vs stub). False positives
filtered: 385 sqlite `PRAGMA journal_mode` / `# pragma: no cover` (PRAGMA-encoder) and a prometheus.yml
qdrant scrape-target (Qdrant) were rejected. Scan: ~/banxe-ai-infrastructure, ~/banxe/banxe-emi-stack,
~/banxe-emi-stack-main, ~/MetaClaw (excl .git, __pycache__, ~/wt/, bundles). [ФАКТ]

## Coverage table

| Novelty (engine §) | Status | Evidence | CENTRAL recommendation |
|---|---|---|---|
| HITL / I-27 gate (§5.1-5.2) | IMPLEMENTED | 815 files; a2a_bus/chain_registry.py | none — deeply wired |
| Specialized agents (§3.1) | IMPLEMENTED | 12; fx_engine/fx_agent.py | none |
| LangGraph / dispatcher (§4.1) | IMPLEMENTED | 4; intent_dispatcher/dispatcher.py | none |
| Midaz ledger (ours) (§L2) | IMPLEMENTED | 151; banxe-emi-stack/api/main.py | none |
| Formance/Blnk ledger (§L2) | IMPLEMENTED | prod=76>tests=40; clickhouse_support.sql | none |
| FinRL / Treasury (§2.4) | IMPLEMENTED (GATED) | 12; api/routers/treasury.py | GATED — B-EMI-CREDIT-GATE-001, no expansion pre-licence |
| decision-lineage ClickHouse (§5.3) | PARTIAL | 1 schema file (agent_decisions), stub=0 | NOT-GATED — complete lineage write (I-24 compliance) |
| Qdrant vector-store (§L3) | MISSING | 0 QdrantClient (only prometheus.yml) | vector-store needed when memory-layer starts (Phase 2-3) |
| PRAGMA-encoder (§2.1) | MISSING | 0 real (385 sqlite false-hits) | GATED — credit/scoring, post-licence |
| GNN / FraudGNN (§2.2) | MISSING | 0 | GATED — fraud/credit, post-licence |
| FATE / Federated (§2.3) | MISSING | 0 | GATED — cross-bank, post-licence |
| NeMo Guardrails (§5.2) | MISSING | 0 | NOT-GATED — LLM-safety, recommend |
| Temporal durable wf (§L1) | MISSING | 0 | NOT-GATED — reliability/idempotency, recommend |
| SHAP/LIME explainability (§5.3) | MISSING | 0 | NOT-GATED — EU AI Act high-risk, recommend |

## Summary
- IMPLEMENTED: 6 | PARTIAL: 1 | MISSING: 7 (of which GATED: 4).
- [ВЫВОД] Implemented = early-phase core (dispatcher, agents, ledgers, HITL); missing = intelligence
  layer (Phase 4-6) — consistent with engine roadmap ordering.

## Top NOT-GATED recommendations to CENTRAL (priority: compliance → reliability → safety)
1. [ВЫВОД] SHAP/LIME — EU AI Act high-risk explainability (credit-decision "why rejected"). Compliance-critical.
2. [ВЫВОД] decision-lineage — complete PARTIAL ClickHouse write to full agent_decisions lineage (I-24, 5y audit).
3. [ВЫВОД] Temporal — durable workflows for idempotency/audit on payment ops (reliability).
4. [ВЫВОД] NeMo Guardrails — programmatic LLM-safety, pairs with I-27 HITL gates.

## Constraints honoured
- [ФАКТ] BEN wrote no production code (INV-01, Aider = sole executor). This is a report + recommendations only.
- [ФАКТ] GATED novelties (PRAGMA/GNN/FATE/FinRL-expansion) NOT recommended for immediate build (B-EMI-CREDIT-GATE-001).
