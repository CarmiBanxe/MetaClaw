# BANXE UX/UI Architecture — Coverage (BEN / CENTRAL)
Date: 2026-07-10
Provenance:
- Source: docs/sources/banxe-uxui-architecture-2026-07-10.md (sha 37b8be7bc87c9a77...)
- Intel: docs/audit/banxe-uxui-architecture-intel-2026-07-10.md
Method: marker + code-context-verify; reuse of world-experience F/D statuses (no re-file).

U1 Chat UI (assistant-ui) | Статус: MISSING (spec-only) | Доказательство: 0 code-matches | Рекомендация: NON-GATED UX, frontend.
U2 Rich Cards | Статус: MISSING (spec-only) | Доказательство: 0 code; reuse world-experience D2 | Рекомендация: frontend; LoanOfferCard — gated при кредит-контуре.
U3 Hybrid Intent Interface | Статус: MISSING (spec-only) | Доказательство: 0 code | Рекомендация: NON-GATED UX; связать с intent_dispatcher (backend уже есть).
U4 Design-tokens (shadcn/Tailwind/style-dictionary) | Статус: PARTIAL | Доказательство: config/design-tokens/style-dictionary.config.json (tailwind-tokens), penpot-config.yaml | Рекомендация: NON-GATED reliability/UX — расширить токен-покрытие; NEW element.
U5 Voice / Whisper | Статус: MISSING | Доказательство: 51 совпадений = biometric SCA, не voice (false-positive отсеян) | Рекомендация: NON-GATED UX optional.
U6 Biometric / Face ID (SCA) | Статус: IMPLEMENTED (reuse F1/PSD2) | Доказательство: api/models/sca.py, auth.py biometric_proof | Рекомендация: reuse, без задач.
U7 Motion / UX animation | Статус: MISSING | Доказательство: 155 = "transition" в lifecycle-роутерах (false-positive) | Рекомендация: frontend-scope.
U8 Decision Lineage / HITL surfaces | Статус: IMPLEMENTED (reuse F3/F4) | Доказательство: dispatcher.py I-27/I-24, chain_registry hitl_threshold | Рекомендация: reuse, без дублей.
Summary: IMPLEMENTED=2 (reuse) PARTIAL=1 (design-tokens) MISSING=5 GATED=0 (LoanOfferCard gated-условно)
