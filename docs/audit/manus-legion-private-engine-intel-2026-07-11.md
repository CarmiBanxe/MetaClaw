# Manus Legion Private Engine — Intel (BEN / CENTRAL)
Date: 2026-07-11
Provenance:
- Source: docs/sources/manus-legion-private-engine.md
  sha256: f937c55f7f12e86d (cp+sha zero-loss, R8 BEST)
- Coverage: docs/audit/manus-legion-private-engine-coverage-2026-07-11.md
## Тип
[ФАКТ] Runbook приватного Legion-контура: llama-server (Qwen3.6 uncensored) → OpenManus FastAPI → Telegram-bot → ngrok/cloudflared tunnel → systemd. Инструкция развёртывания, не banking-код.
## Карта
[ФАКТ] OpenManus engine, uncensored llama-server, Telegram bridge, tunnel, config.toml/api_server.py/telegram_bot.py, browser-use/playwright.
## Reuse / verify
[ВЫВОД] OpenManus/Telegram/tunnel MISSING в banking repos (by design — изолированный контур, S-18 §1.1); production Qwen (qwen3-235b/4b) = другой контур (reuse); playwright есть для visual-QA, не OpenManus.
## НЕИЗВЕСТНО
[НЕИЗВЕСТНО] Реальный статус развёртывания Legion-контура (вне banking repos, не сканируется здесь); DLP-граница Legion↔Banking — S-18 S2 PARTIAL.
