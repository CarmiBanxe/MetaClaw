# ORG-STRUCTURE — Coverage (BEN / CENTRAL)
Date: 2026-07-11
Provenance:
- Source: docs/sources/ORG-STRUCTURE.md (sha 02ff23afbbcda9ea)
- Intel: docs/audit/ORG-STRUCTURE-intel-2026-07-11.md
Method: marker + code-context-verify; reuse F3/F4; numbers = code-matches.

G1 org_roles HITL enforcement | Статус: IMPLEMENTED | Доказательство: services/hitl/org_roles.py (HITLGate), ports citing ORG-STRUCTURE §2.x (36) | Рекомендация: reuse.
G2 HITL matrix / gates | Статус: IMPLEMENTED | Доказательство: org_roles.py + HITL-MATRIX.yaml source-of-truth, I-27 (90) | Рекомендация: reuse F3.
G3 ADR-049 §D2 mask agents | Статус: IMPLEMENTED | Доказательство: L1 Intent Layer intent.router, §D2 gate-chain (103) | Рекомендация: reuse.
G4 ADR-046 AgentDecisionRecord | Статус: IMPLEMENTED | Доказательство: AgentDecisionRecord/DecisionRecorder intent.py (89) | Рекомендация: reuse F4.
G5 SM&CR / SMF roles | Статус: IMPLEMENTED | Доказательство: SMF17 MLRO gates registry.py, iam SM&CR (24) | Рекомендация: reuse.
G6 Domain agents (Treasury/FX/Crypto/etc) | Статус: IMPLEMENTED | Доказательство: treasury_agent, fx_agent, crypto_agent (184) | Рекомендация: reuse; расширения в кредит/payment — gated.
G7 §D2 mask completeness (PROPOSED agents) | Статус: PARTIAL | Доказательство: часть агентов (PROPOSED) без §D2 mask (IL-176) | Рекомендация: NON-GATED compliance — довести §D2-маски; отдельный org-code reconciliation.
Summary: IMPLEMENTED=6 PARTIAL=1 MISSING=0 GATED=0 (domain credit/payment extensions gated-условно)
