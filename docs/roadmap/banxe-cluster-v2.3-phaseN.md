# BANXE AI Cluster — Roadmap v2.3 (active)
Date: 2026-05-03 · Author: Moriel Carmi · Status: ACTIVE

Predшественник: `banxe-cluster-v2.2-phase3.md` (CLOSED 2026-05-03, см. §47 hand-off summary).

Этот документ — активный roadmap для work after Phase 3 v2.2: followup-задачи, mini-sprints, hot-fix трек. Phase 4 capacity/feature расширения трекаются отдельно (`banxe-cluster-phase4.md` или внутри §15 v2.2).

## 1. Carryover from Phase 3 (15 items, see v2.2 §47)

Из v2.2 §47 "Followups carried into Phase 4" — 15 пунктов. Здесь (v2.3) ведём оперативную часть; capacity-задачи (P4.1–P4.6, ROCm, BIOS rebalance, NPU, n8n, doc-translation) остаются за Phase 4.

Hot trees, относящиеся к v2.3:
- **P3.4-followup-1** (F1): refresh `/data/banxe/banxe-emi-stack/api/routers/auth.py` from clean Legion HEAD `61b944c`.
- **P3.4-followup-2** (F2): locate/restore `drive_watcher.py`; install cron on evo1; drop dead Legion line.
- **P3.4-followup-3** (F3): switch deep-search to canonical systemd unit (kill legacy PID, restart unit).
- **F-secrets**: batch `gh secret set ANTHROPIC_API_KEY` для 14 factory PR-репо (§42 v2.2).
- **CVE-2026-25253**: verify/upgrade OpenClaw на Legion ≥ 2026.1.29.
- **firewall-evo1**: сузить 80/443 ALLOW IN Anywhere до LAN+Tailscale.
- **factory-ci-tweak**: исключить `.venv` и vendored deps из ruff/secrets-scan в фабрике.

## 2. Mini-sprints (this session)

### F-secrets — DEFERRED (no env key, 2026-05-03)

Проверка окружения: `echo "${#ANTHROPIC_API_KEY}"` = `0`. Env-переменная `ANTHROPIC_API_KEY` не установлена в shell этой сессии.

Per sprint canon: "If F-secrets has no env key — write DEFERRED note, do NOT request key from operator." Соответственно batch-выставление repo-secret отменено в этой сессии.

Status: **DEFERRED**. Пока operator не экспортирует `ANTHROPIC_API_KEY` в окружение и не перезапустит mini-sprint F-secrets, repo-secret не будет выставлен на 14 целевых факторных репо (`factory/ai-onboarding` ветки из v2.2 §42).

Re-entry plan: оператор делает `export ANTHROPIC_API_KEY=...` (в `~/.bashrc` или ad-hoc), затем re-run F-secrets шаг — он сам отфильтрует через `gh pr list` репо с открытыми PR `factory/ai-onboarding` от своего аккаунта и сделает idempotent `gh secret list | grep -q ... || gh secret set ...` per репо.

## 3. Open / WIP / DONE table

| Item | State | Owner | Ref |
|---|---|---|---|
| F1 — compliance-api unblock | WIP | this session | §F1 |
| F3 — deep-search canonical switch | WIP | this session | §F3 |
| F-secrets — ANTHROPIC_API_KEY batch | DEFERRED | operator (re-run with env key) | §F-secrets |
| F2 — drive_watcher restore | OPEN | TBD | v2.2 §46 P3.4-followup-2 |
| CVE-2026-25253 OpenClaw upgrade | OPEN | TBD | v2.2 §16 |
| firewall-evo1 LAN+Tailscale | OPEN | TBD | v2.2 §16 |
| factory-ci-tweak | OPEN | TBD | v2.2 §42 |
| Phase 4: P4.1–P4.6, MiroFish, doc-translation | DEFERRED | Phase 4 | v2.2 §15/§17/§18/§43 |
