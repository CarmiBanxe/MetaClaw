# EMI BANXE World-Experience — Intel (BEN / CENTRAL)
Date: 2026-07-09
Provenance:
- Source: docs/sources/emi-banxe-world-experience-2026-07-09.md
  sha256: 08aff49982f7e7ba... (cp+sha zero-loss, R8 BEST)
- Coverage: docs/audit/emi-banxe-world-experience-coverage-2026-07-09.md

## Тип документа
[ФАКТ] Обзор мирового опыта банков-ИИ-агентов (Китай/Япония/Корея/ЮВА/ЛатАм/Ближний Восток/Австралия/Африка),
open-source стек, master-prompt UX/UI v2.0, CI/CD-агенты. Методология/бенчмарк, НЕ код.

## Карта новинок по группам (A–F)
[ФАКТ] A) Federated/privacy: FATE, FISCO BCOS, WeIdentity, differential-privacy/PSI — EMI-gated.
[ФАКТ] B) LLM-orchestration: LangGraph/LangSmith/LangChain/DSPy, LiteLLM, Bedrock, Azure OpenAI, Vertex/Gemini, DeepSeek.
[ФАКТ] C) Data/observability: ClickHouse, Qdrant, Langfuse, Kafka, Temporal, OceanBase, SOFAStack.
[ФАКТ] D) UX/agentic: dual-track UI, Rich Cards, Avatar banking, composite tools, evals-first, ReAct.
[ФАКТ] E) Payments/agentic commerce: Visa Intelligent Commerce, M-Pesa MCP, payment gateway — EMI-gated.
[ФАКТ] F) Compliance: EU AI Act, GDPR, PSD2/PSD3, audit-trail, HITL, decision lineage.

## Сводка покрытия (из coverage)
[ВЫВОД] IMPLEMENTED=8, PARTIAL=7, MISSING=21, GATED=7.
[ВЫВОД] Реализовано ядро compliance (PSD2/SCA, GDPR, HITL, audit-trail) + ClickHouse lineage + Bedrock LLM + MCP agent-tooling.
[ВЫВОД] Отсутствует durable/federated/observability стек (Temporal/Kafka/Qdrant/FATE/FISCO) и UX-слой (frontend-scope).

## EMI-gate
[ФАКТ] Группы A и E (federated credit / agentic payments) — post-licence, B-EMI-CREDIT-GATE-001, без "implement now".

## НЕИЗВЕСТНО
[НЕИЗВЕСТНО] Соответствие master-prompt UX/UI существующему фронтенду — отдельный frontend-аудит.
[НЕИЗВЕСТНО] Выбор Temporal vs LangGraph durable-слоя — решение оператора/CTIO (отдельный ADR).
[НЕИЗВЕСТНО] Сверка с расширенной версией emi-banxe-world-experience-full-2026-07-10.md.
