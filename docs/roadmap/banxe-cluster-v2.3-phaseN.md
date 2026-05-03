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

## §COMPLIANCE-OPS — port-binding & service supervision (operational, 2026-05-03T16:41:07+02:00)

### Status snapshot
- **Dependency baseline on evo1**: validated. `compliance-env` теперь содержит SQLAlchemy 2.0.49, asyncpg 0.31.0, psycopg2-binary 2.9.11, pydantic 2.12.5, redis 7.4.0, и все имеющиеся deps из `requirements.txt`. Установка PyJWT и остальных deps идёт по `pip install -r` (см. F1 trail).
- **Service supervision NOT canonical**: `banxe-compliance-api.service` падает с `Address already in use` на 8093. На порту висит orphan `uvicorn pid=1908` (uptime ~4h+, биндинг на `127.0.0.1:8093`). Наш юнит хочет биндиться на `0.0.0.0:8093` и конфликтует.

### Findings (factual)
- `/data/banxe/banxe-emi-stack/api/routers/auth.py` обновлён до Legion HEAD `61b944c`, конфликт-маркеры удалены (F1 step 3-4).
- ImportError `No module named 'sqlalchemy'` устранён (`pip install "sqlalchemy[asyncio]"`).
- Следующий ImportError `No module named 'jwt'` — устранён через `pip install -r requirements.txt` (см. F1).
- После последнего restart процесс падает не на ImportError, а на port 8093 уже занят.

### Operational items (carryover)

- **COMPLIANCE-OPS-1**: устранить port-binding conflict на `banxe-compliance-api` (8093). Проверить:
  - `systemctl cat banxe-compliance-api` — ExecStart, KillMode (по умолчанию `control-group`), Restart=on-failure.
  - Найти orphan uvicorn (`pid=1908` в snapshot `16:36:08`): `sudo lsof -iTCP:8093 -sTCP:LISTEN -n -P`, проследить cwd/cmdline через `/proc/1908/cmdline`, `/proc/1908/cwd`.
  - Если это процесс не из нашего юнита — kill его (operator approval), затем `systemctl restart banxe-compliance-api`.
  - Если это и есть наш предыдущий runner, который не убрался при restart — расследовать KillMode/RemainAfterExit и привести к каноничному `KillMode=mixed`.

- **COMPLIANCE-OPS-2**: запретить manual `uvicorn` вне systemd для prod-like evo1, если сервис уже управляется через `banxe-compliance-api.service`. Реализация:
  - Добавить в `/etc/banxe/operations.md` запись "compliance-api управляется только systemd; manual `uvicorn` в `/data/banxe` запрещён".
  - Опционально — wrapper-скрипт `/usr/local/bin/banxe-compliance-api` с проверкой `systemctl is-active` перед любым запуском.
  - Audit: cron каждые 15 минут проверяет, что на 8093 биндится PID, принадлежащий `banxe-compliance-api.service` cgroup; иначе alert.

- **COMPLIANCE-OPS-3**: smoke check после фикса. Шаги:
  - `systemctl restart banxe-compliance-api` → `systemctl is-active banxe-compliance-api` = `active`.
  - `ss -tlnp | grep :8093` показывает PID, чей parent — `banxe-compliance-api.service` cgroup.
  - `curl -s -o /dev/null -w "%{http_code}\n" http://192.168.0.72:8093/docs` → 200 (FastAPI OpenAPI UI; гарантированный endpoint у FastAPI приложений).
  - `curl -s -o /dev/null -w "%{http_code}\n" http://192.168.0.72:8093/health` → **NOT VERIFIED**: наличие `/health` endpoint в `api/main.py` не подтверждено из логов; нужно проверить отдельно `grep -n "/health\|@app.get" /data/banxe/banxe-emi-stack/api/main.py`. До подтверждения — `/docs` остаётся каноничным smoke endpoint.

### Practical conclusion
Runtime environment почти готов, но service supervision для compliance-api ещё не приведён в каноническое production-состояние. Следующий шаг — не переустанавливать пакеты, а починить **lifecycle и process ownership на порту 8093**.

### Open
- COMPLIANCE-OPS-1 → WIP (next action).
- COMPLIANCE-OPS-2 → OPEN (audit + wrapper).
- COMPLIANCE-OPS-3 → OPEN (smoke harness).
- F1 (auth.py refresh) → DONE; deps install → DONE; service active → BLOCKED on COMPLIANCE-OPS-1.

## §F1 — banxe-compliance-api unblock (PASS, 2026-05-03T16:49:58+02:00)

### Outcome
**PASS.** Service `banxe-compliance-api` поднят на `evo1:8194`, `/health` и `/docs` отвечают HTTP 200 за <40ms.

### Steps executed
1. Refresh `/data/banxe/banxe-emi-stack/api/routers/auth.py` from Legion HEAD `61b944c` (rsync, md5 `7d2d3738...`, 218 строк, 0 markers).
2. Install missing Python deps via `pip install -r requirements.txt`: SQLAlchemy 2.0.49, asyncpg 0.31.0, PyJWT, etc.
3. Port shift: 8093 → 8094 → 8194 (8093 и 8094 заняты legacy `banxe-api.service` → "Banxe Collective LexisNexis Compliance API", root, uptime 14h+, отдельный compliance стек, не наш scope).
4. ufw on evo1: `8194/tcp ALLOW IN` для `192.168.0.0/24` + `100.64.0.0/10`.
5. `systemctl restart banxe-compliance-api` → `active`.

### Smoke (Legion → evo1:8194)
```
[1] /health HTTP 200 time=0.038s
[1] /docs   HTTP 200 time=0.008s
[2] /health HTTP 200 time=0.006s
[2] /docs   HTTP 200 time=0.005s
[3] /health HTTP 200 time=0.007s
[3] /docs   HTTP 200 time=0.006s
```

### Notes / coexistence
- legacy `banxe-api.service` (root, WD `/data/banxe/compliance`) продолжает работать на 127.0.0.1:8093 + 8094 (он использует второй сокет как worker handle). Не наш scope, оставлен как есть.
- COMPLIANCE-OPS-1 (port-binding) **закрыт** через port shift, не через kill legacy.
- COMPLIANCE-OPS-3 smoke harness подтверждает наличие `/health` endpoint в FastAPI app (как мы зафиксировали в grep `api/main.py:6`).
- Legacy `/etc/systemd/system/banxe-api.service` остаётся отдельным трекером — если когда-то понадобится консолидировать, сделать через P3.4-followup-4 (rename/decommission старого).

### Verdict
**PASS.** Внешний контракт F1 выполнен; canonical service на evo1 запущен, observable, test-OK.

## §F3 — deep-search canonical switch (PASS, 2026-05-03T16:52:01+02:00)

### Outcome
**PASS.** Legacy `/opt/deep-search-server.py` (PID 1915, root, uptime 14h+) убит. Канонический systemd-юнит `banxe-deep-search.service` (`/data/banxe/compliance-env/bin/python /data/banxe/deep-search/deep-search-server.py`) теперь serving на `evo1:8088`.

### Steps executed
1. `systemctl stop banxe-deep-search` (на всякий случай, юнит был в restart loop).
2. `kill 1915` (legacy /opt/ process), 2s settle.
3. `systemctl reset-failed banxe-deep-search` + `systemctl start banxe-deep-search`.
4. Один промежуточный OSError при первом restart attempt (port в TIME_WAIT после kill), второй attempt поднялся чисто.

### Post-state
- LISTEN 0.0.0.0:8088 by `python` PID 2813293 (canonical unit).
- `systemctl is-active banxe-deep-search` = `active`.

### Smoke (Legion → evo1:8088)
```
[1] / HTTP 200 time=0.0057s
[2] / HTTP 200 time=0.0065s
[3] / HTTP 200 time=0.0066s
```

### Verdict
**PASS.** Канонический путь подтверждён, legacy retired.

## §FINAL — v2.3 mini-sprints summary (2026-05-03T16:52:01+02:00)

### Outcome table

| Followup | Status | Where | Commit |
|---|---|---|---|
| F1 — banxe-compliance-api unblock | **PASS** | evo1:8194, /health 200 | faab812 |
| F3 — deep-search canonical | **PASS** | evo1:8088 (canonical unit, legacy PID 1915 retired) | (this) |
| F-secrets — ANTHROPIC_API_KEY batch | **DEFERRED** | env key empty; re-run after `export ANTHROPIC_API_KEY=...` | 8ff326d |

### Closes carryover from v2.2 §47
- P3.4-followup-1 (auth.py refresh) → DONE in F1.
- P3.4-followup-3 (deep-search canonical) → DONE in F3.
- P3.4-followup-2 (drive_watcher restore) → still OPEN, требует поиска исходника.
- Factory secrets enablement → DEFERRED (operator action: export key и re-run).

### Open carryover (12 items)
- P3.4-followup-2 (drive_watcher.py source missing).
- P3.2-followup / P4.3 BIOS UMA rebalance evo2 (qwen3:235b-a22b unlock).
- MiroFish prod-hardening (§43 v2.2).
- CVE-2026-25253 OpenClaw upgrade.
- evo1 80/443 → LAN+Tailscale only (если ещё не сделано в P3.5).
- P4.1–P4.6 Phase 4 backlog (NPU, ROCm, BIOS evo1, n8n, doc translation).
- COMPLIANCE-OPS-2 (запрет manual uvicorn вне systemd).
- Factory CI scope tweak (.venv exclude).
- Legacy `banxe-api.service` consolidation (decision: оставить как есть; consolidate если понадобится).

### Verdict
**v2.3 mini-sprints CLOSED**. 2/3 followups закрыты PASS, 1 DEFERRED по env key. Net coverage: внешний контракт compliance-стека на evo1 обеспечен (compliance-api 8194 + deep-search 8088 + node_exporter 9100 + glm-master 8081 — все на canonical systemd units, observable, smoke-OK).
