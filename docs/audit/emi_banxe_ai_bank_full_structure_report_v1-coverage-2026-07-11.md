# EMI BANXE Full Structure Report — Coverage (BEN / CENTRAL)
Date: 2026-07-11
Provenance:
- Source: docs/sources/emi_banxe_ai_bank_full_structure_report_v1.md (sha 666a5bab02816630)
- Intel: docs/audit/emi_banxe_ai_bank_full_structure_report_v1-intel-2026-07-11.md
Method: marker + code-context-verify; reuse ORG-STRUCTURE G1-G7.

R1 ORG-CODE-RECONCILIATION methodology | Статус: PARTIAL | Доказательство: 6 matches все в самом source (нет отдельного код-модуля); методология сопоставления 3 слоёв | Рекомендация: NON-GATED compliance — формализовать reconciliation как артефакт/скрипт.
R2 Domain-service layer (86 *_agent.py) | Статус: IMPLEMENTED | Доказательство: 86 services/*/*_agent.py в banxe-emi-stack | Рекомендация: reuse G6; расширения кредит/payment gated.
R3 Org governance (roles/HITL/§D2/ADR-046/SM&CR) | Статус: IMPLEMENTED (reuse ORG-STRUCTURE G1-G5) | Доказательство: ORG-STRUCTURE coverage 0493b78 | Рекомендация: не дублировать.
R4 §D2 mask completeness (PROPOSED agents) | Статус: PARTIAL (reuse G7) | Доказательство: ORG-STRUCTURE G7 | Рекомендация: довести §D2-маски.
R5 SP-RECON / SP-THIN status | Статус: НЕИЗВЕСТНО (roadmap) | Доказательство: только в source | Рекомендация: статус reconciliation — решение оператора.
Summary: IMPLEMENTED=2 (reuse) PARTIAL=2 UNKNOWN=1 MISSING=0 GATED=0
