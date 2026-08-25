# Manus Legion Private Engine — Coverage (BEN / CENTRAL)
Date: 2026-07-11
Provenance:
- Source: docs/sources/manus-legion-private-engine.md (sha f937c55f7f12e86d)
- Intel: docs/audit/manus-legion-private-engine-intel-2026-07-11.md
Method: marker + code-context-verify; reuse S-18; MISSING-by-design noted.

P1 OpenManus engine | Статус: MISSING (by design, private contour) | Доказательство: 0 в banking repos | Рекомендация: NON-GATED; Legion-контур вне banking scope; ADR оператора.
P2 uncensored llama-server (Qwen3.6) | Статус: MISSING в banking (production qwen3-235b/4b = другой контур) | Доказательство: 16 matches = project-reason/chat-fast, не uncensored | Рекомендация: изолировать от banking (DLP, S-18 S2).
P3 Telegram bot bridge | Статус: MISSING | Доказательство: 0 | Рекомендация: NON-GATED; часть Legion-контура.
P4 Tunnel (ngrok/cloudflared) | Статус: MISSING | Доказательство: 0 | Рекомендация: NON-GATED; webhook-only, не в banking.
P5 browser-use / playwright | Статус: PARTIAL (playwright есть, но для visual-QA не OpenManus) | Доказательство: design_pipeline/visual_qa.py | Рекомендация: не путать с OpenManus browser-agent.
P6 DLP boundary Legion↔Banking | Статус: PARTIAL (reuse S-18 S2, trust_zone) | Доказательство: S-18 coverage | Рекомендация: NON-GATED compliance — формализовать DLP-gateway.
Summary: IMPLEMENTED=0 PARTIAL=2 MISSING=4 GATED=0 (MISSING largely by-design private contour)
