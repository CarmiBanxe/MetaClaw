# S-18 Consultant Answers — Intel (BEN / CENTRAL)
Date: 2026-07-11
Provenance:
- Source: docs/sources/S-18-consultant-answers.md
  sha256: 719494c471bd1a5f (cp+sha zero-loss, R8 BEST)
- Coverage: docs/audit/S-18-consultant-answers-coverage-2026-07-11.md
## Тип
[ФАКТ] Архитектурно-governance меморандум: ответы на открытые вопросы (границы движков, BDSL-пороги, CREDIT-домен, оркестраторы, память, паспорта, EU AI Act, DLP, иерархия документов).
## Ключевые решения
[ВЫВОД] Двухзональная изоляция Banking↔Legion (нет прямых маршрутов, только audit-gated API); Legion (OpenManus + uncensored Qwen) = приватный контур; CREDIT-домен gated (post-licence); 13 PROPOSED = §D2 mask (ORG-STRUCTURE G7).
## Reuse / verify
[ВЫВОД] OpenManus MISSING (private contour); DLP/two-zone PARTIAL (trust_zone в compliance/orchestrator.py); LangGraph/CrewAI/AutoGen/Qdrant/Mem0/DeerFlow/EU AI Act — reuse.
## НЕИЗВЕСТНО
[НЕИЗВЕСТНО] Точная сетевая топология evo1/evo2/Legion; BDSL-пороги/MAUT-веса — решение владельца; ADR-103 (Legion тонкий клиент) vs Manus-агент — противоречие для оператора.
