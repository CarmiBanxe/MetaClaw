# S-18 Consultant Answers — Coverage (BEN / CENTRAL)
Date: 2026-07-11
Provenance:
- Source: docs/sources/S-18-consultant-answers.md (sha 719494c471bd1a5f)
- Intel: docs/audit/S-18-consultant-answers-intel-2026-07-11.md
Method: marker + code-context-verify; reuse world-exp/ideal-engine/ORG-STRUCTURE.

S1 OpenManus (Legion orchestrator) | Статус: MISSING | Доказательство: 0 code-matches (private contour) | Рекомендация: NON-GATED; Legion-контур вне banking repos; ADR решение оператора.
S2 DLP / two-zone boundary (Banking↔Legion) | Статус: PARTIAL | Доказательство: trust_zone в agents/compliance/orchestrator.py (RED zone), нет отдельного cross-zone DLP-gateway | Рекомендация: NON-GATED compliance — формализовать DLP-gateway между зонами.
S3 BDSL thresholds / MAUT weights | Статус: reuse (bdsl coverage) | Доказательство: bdsl-coverage-2026-07-09 | Рекомендация: пороги/веса — решение владельца, не дублировать.
S4 CREDIT domain agent | Статус: MISSING/GATED | Доказательство: reuse gated backlog | Рекомендация: post-licence (B-EMI-CREDIT-GATE-001).
S5 Orchestrators & memory (LangGraph/CrewAI/AutoGen/Qdrant/Mem0/DeerFlow) | Статус: reuse | Доказательство: world-exp/ideal-engine/oss coverage | Рекомендация: не дублировать.
S6 47 passports (34+13 PROPOSED §D2) | Статус: reuse (ORG-STRUCTURE G7 PARTIAL) | Доказательство: ORG-STRUCTURE coverage | Рекомендация: довести §D2-маски.
S7 EU AI Act high-risk classification | Статус: reuse F5 (PARTIAL) | Доказательство: world-experience F5 | Рекомендация: явная Art.12-17 имплементация — отдельный backlog.
Summary: reuse-heavy — NEW: MISSING=2 (OpenManus, CREDIT) PARTIAL=1 (DLP) ; остальное reuse.
