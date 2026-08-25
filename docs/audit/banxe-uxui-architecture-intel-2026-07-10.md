# BANXE UX/UI Architecture — Intel (BEN / CENTRAL)
Date: 2026-07-10
Provenance:
- Source: docs/sources/banxe-uxui-architecture-2026-07-10.md
  sha256: 37b8be7bc87c9a77... (cp+sha zero-loss, R8 BEST)
- Coverage: docs/audit/banxe-uxui-architecture-coverage-2026-07-10.md

## Тип
[ФАКТ] UX/UI спецификация нового поколения: Hybrid Intent Interface, Rich Cards, bottom-navigation, voice, design-system, EU AI Act/HITL. Frontend-scope, не backend-код.

## Карта новинок
[ФАКТ] Chat UI (assistant-ui), Rich Cards (Transfer/FXRail/SpendingInsight/Exchange/LoanOffer), Hybrid Intent Interface — UX-компоненты.
[ФАКТ] Design-system: shadcn/Tailwind, design-tokens (style-dictionary), Framer Motion, WCAG, i18n.
[ФАКТ] Auth/UX: Face ID/biometric (PSD2 SCA), voice/Whisper.
[ФАКТ] Compliance UX: Decision Lineage, HITL surfaces (EU AI Act Art.13/14).

## Связь с world-experience
[ВЫВОД] Rich Cards / dual-track / avatar пересекаются с world-experience GROUP D (spec-only, MISSING) — reuse, без дублей.
[ВЫВОД] HITL / audit-lineage = world-experience F3/F4 (IMPLEMENTED) — reuse.
[ВЫВОД] biometric SCA = world-experience F1 (PSD2, IMPLEMENTED) — reuse.

## НЕИЗВЕСТНО
[НЕИЗВЕСТНО] Реальное состояние фронтенда (React/Expo) — отдельный frontend-аудит вне backend-скана.
[НЕИЗВЕСТНО] Полнота design-token покрытия vs спецификация UX-kit.
