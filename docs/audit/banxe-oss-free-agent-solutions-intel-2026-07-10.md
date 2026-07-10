# BANXE OSS Free Agent Solutions — Intel (BEN / CENTRAL)
Date: 2026-07-10
Provenance:
- Source: docs/sources/banxe-oss-free-agent-solutions-2026-07-10.md
  sha256: 50c2f6677d224d56 (cp+sha zero-loss, R8 BEST)
- Coverage: docs/audit/banxe-oss-free-agent-solutions-coverage-2026-07-10.md
## Тип
[ФАКТ] OSS-каталог: агентные фреймворки (CrewAI/AutoGen/LangGraph), Manus-подобные, финагенты (FinRobot/FinGPT), KYC/AML (OpenKYC), ledgers (Formance/Blnk/Hyperledger), RAG/память (LlamaIndex/Weaviate/Qdrant/Mem0/Zep), workflow (n8n/Airflow/Temporal), MCP, локальные LLM (Ollama).
## Карта новинок
[ФАКТ] Новые к проверке: CrewAI, AutoGen, n8n, Airflow, Ollama, Weaviate, Mem0/Zep, Formance. Reuse: LangGraph/Temporal/Kafka/Qdrant/Langfuse/Bedrock.
## Reuse / факты
[ВЫВОД] n8n IMPLEMENTED (AML workflow-оркестрация); Ollama IMPLEMENTED (LLM runtime); CrewAI planned; AutoGen/Formance — false-positive; остальное MISSING/reuse.
## НЕИЗВЕСТНО
[НЕИЗВЕСТНО] Выбор CrewAI vs LangGraph adapter — ADR оператора; RAG-память (Weaviate/Mem0/Zep) не внедрена.
