# BANXE OSS Free Agent Solutions — Coverage (BEN / CENTRAL)
Date: 2026-07-10
Provenance:
- Source: docs/sources/banxe-oss-free-agent-solutions-2026-07-10.md (sha 50c2f6677d224d56)
- Intel: docs/audit/banxe-oss-free-agent-solutions-intel-2026-07-10.md
Method: marker + code-context-verify; reuse world-experience/ideal-engine; numbers = code-matches.

O1 n8n workflow orchestration | Статус: IMPLEMENTED | Доказательство: api/routers/sanctions_rescreen.py, mlro_notifications.py (n8n watchman_rescreen_high_risk / list_update, banxe_aml_orchestrator) | Рекомендация: зафиксировать как AML workflow-оркестратор.
O2 Ollama local LLM runtime | Статус: IMPLEMENTED | Доказательство: banxe-monitoring/prometheus/rules/llm.yml (Ollama health/queue), nodes.yml | Рекомендация: reuse; NON-GATED reliability.
O3 CrewAI framework | Статус: MISSING (planned P1) | Доказательство: intent_dispatcher/adapters port.py/app.py "P1 will add CrewAI" | Рекомендация: NON-GATED; adapter за существующим port, не дубль LangGraph.
O4 AutoGen | Статус: MISSING (false-positive "autogenerate" отсеян) | Доказательство: Alembic autogenerate, не AutoGen | Рекомендация: optional.
O5 Airflow | Статус: MISSING | Доказательство: 0 matches | Рекомендация: NON-GATED; n8n/Temporal уже покрывают workflow.
O6 Weaviate / Mem0 / Zep (RAG memory) | Статус: MISSING | Доказательство: 0 matches (Qdrant reuse world-exp) | Рекомендация: NON-GATED; memory-layer по решению оператора.
O7 Formance/Blnk ledger | Статус: MISSING (false-positive "performance" отсеян) | Доказательство: substring performance/conformance | Рекомендация: core-banking ledger — отдельное решение.
O8 LangGraph/Temporal/Kafka/Qdrant/Langfuse | Статус: reuse (см. world-experience) | Доказательство: world-experience coverage | Рекомендация: не дублировать.
O9 Bedrock LLM provider | Статус: IMPLEMENTED (reuse) | Доказательство: MetaClaw bedrock_client | Рекомендация: reuse.
Summary: IMPLEMENTED=3 (n8n, Ollama, Bedrock-reuse) PARTIAL=0 MISSING=5 GATED=0 (+reuse row)
