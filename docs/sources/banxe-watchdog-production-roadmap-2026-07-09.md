# BANXE/EMI — Автономная Ремонтная Бригада: Архитектурный Аудит и Production-Roadmap

## Executive Summary

Текущая реализация watchdog представляет собой технически корректный первый слой самовосстановления: PASS 27 тестов, изолированный repair_engine с намеренно ограниченным набором действий (warm_model + start_container), трёхуровневая crash-loop guard. Однако система находится на уровне **Tier-1 Reactive** и пропасть между ней и production-ready fintech-watchdog — конкретна и измерима. Инцидент с hyperswitch (103 000+ рестартов из-за scram-sha-256 password mismatch) наглядно показал граничу возможностей: для autonomus root-cause diagnosis требуется **Tier-2 Diagnostic** слой, а для безопасного авто-ремонта конфигурационного drift — **Tier-3 Orchestrated**, с полным audit-trail.

Ниже — исчерпывающий разбор всех 9 вопросов с конкретными паттернами реализации, порогами, кодовыми примерами и compliance-требованиями.

***

## 1. Архитектурная Диагностика Текущего Состояния

### Что реализовано правильно

Архитектура repair_engine с намеренно ограниченным контрактом (SAFE-only actions, без subprocess/shell exec) — это принципиально верное решение для банковской среды. Трёхуровневая защита от crash-loop (port-level → policy-level → scan-level) соответствует принципу defence-in-depth. Отсутствие секретов в коде — базовый compliance-требование PCI DSS Requirement 3 и 6.

Системный unit `banxe-watchdog.service` с `Restart=always` — правильный минимум для service resilience на Linux, но, как разобрано в Q5, недостаточный для production-grade fintech.

### Критические пробелы (Gap Analysis)

| Пробел | Серьёзность | Инцидент-референс |
|--------|-------------|-------------------|
| Нет root-cause классификатора | **CRITICAL** | hyperswitch (auth mismatch не обнаружен) |
| Hardcode threshold=10 vs config | **MEDIUM** | Рассинхрон защиты crash-loop |
| Нет Prometheus-экспортёра от watchdog | **HIGH** | Grafana/Prometheus сейчас down |
| Нет dead-man-switch / heartbeat | **HIGH** | Watchdog — единая точка отказа |
| Нет structured audit-trail для действий | **CRITICAL** | PCI DSS Req 10.2, SOC 2 CC7.2 |
| Legion offline — нет различия «узел vs сеть» | **MEDIUM** | Текущий инцидент открыт |
| Нет политики для GUARDED-действий | **HIGH** | recreate/config-sync не реализованы |

***

## 2. Q1 — Граница Автономности в Банковской Среде

### Три уровня действий: правильный принцип

Предложенная иерархия SAFE / GUARDED / MANUAL-ONLY — правильная для регуляторной среды. Критерий разделения не технический («может ли бригада это сделать?»), а **операционный и комплаенс-риск** («что происходит, если действие ошибочно?»).

**SAFE (полностью автономно, без одобрения):**
- `warm_model` — идемпотентен, обратимость полная, нет stateful-side-effect
- `start_container` (только при restart_count < threshold и классификатор = "cold-stop") — контейнер не изменяется, только переходит из stopped в running
- Экспорт метрик, обновление статус-файла
- Эскалация (отправка alert) — это тоже "безопасное" действие

**GUARDED (автономно, но с circuit-breaker, backoff, подтверждением через audit-log):**
- `recreate_container` — только для stateless сервисов (LiteLLM router, Redis-slave). **Условие**: отсутствие pending транзакций, сервис не в MANUAL-ONLY категории
- `sync_env_config` — только для non-payment контейнеров, только если классификатор confidence > 0.95 по паттерну CONFIG_DRIFT, и только если изменение — подтягивание значения из Vault (не генерация нового)
- Перезапуск Prometheus/Grafana-стека — monitoring-only компоненты, нет финансовых данных

**MANUAL-ONLY (только эскалация, никаких авто-действий):**
- **hyperswitch** (payment router) — любые действия кроме stop escalation
- PostgreSQL PRIMARY, ClickHouse (stateful, потеря данных при неправильном recreate)
- Любая операция, требующая `ALTER USER`, `GRANT`, миграций схемы
- Любые изменения конфигурации сетевого уровня, TLS-сертификатов
- Действия на компонентах с PII/CHD (cardholder data)

### Регуляторное обоснование

PCI DSS Requirement 6.4 требует формального change management для всех изменений в cardholder data environment (CDE). Автоматическое изменение конфигурации платёжного роутера без human approval нарушает этот контроль. SOC 2 CC8.1 (Change Management) явно требует авторизации изменений. hyperswitch должен быть зафиксирован в `watchdog.yaml` с флагом `autonomy_level: MANUAL_ONLY` — это не опционально для EMI/banking лицензии.

***

## 3. Q2 — Root-Cause Классификатор

### Архитектура классификатора

Root-cause analysis — это конвейер трёх источников данных: exit-code (детерминированный сигнал от ядра/рантайма) + лог-паттерны (семантика приложения) + healthcheck metadata. Ни один источник не достаточен сам по себе.

**Exit-code таблица (нормативная):**
| Exit Code | ОС-интерпретация | Root-Cause гипотеза | Confidence |
|-----------|-----------------|---------------------|------------|
| 137 (SIGKILL) | OOMKilled = true | OOM — подтвердить docker inspect .State.OOMKilled | 0.90 |
| 137 (SIGKILL) | OOMKilled = false | External kill (watchdog/operator/orchestrator) | 0.70 |
| 1 | App error | Config/code — смотреть лог | 0.50 |
| 127 | Command not found | Image corruption / bad entrypoint | 0.95 |
| 0 | Clean exit | Dependency-down или misconfig | — |
| 143 (SIGTERM) | Graceful stop | Intended or orchestrator action | — |

Лог-паттерны root_cause_classifier.py (regex-библиотека):
LOG_PATTERNS = {
  AUTH_FAILURE: [password authentication failed, SCRAM authentication failed, Access denied for user, authentication error, invalid credentials],
  OOM: [Out of memory, Cannot allocate memory, java.lang.OutOfMemoryError],
  CONFIG_DRIFT: [environment variable.*not set, configuration.*missing, no such file or directory.*.env, invalid.*config],
  DEPENDENCY_DOWN: [connection refused, dial tcp.*connection refused, could not connect to server, redis.*ECONNREFUSED],
  NETWORK: [i/o timeout, connection timed out, network unreachable],
}

Классификатор classify_root_cause(exit_code, oom_killed, logs, restart_count):
- scores = {}
- if oom_killed: scores[OOM] = 0.95
- if exit_code == 127: scores[IMAGE_CORRUPT] = 0.95
- для каждого cause/pattern в LOG_PATTERNS: if re.search(pattern, logs, IGNORECASE): scores[cause] += 0.30
- if restart_count > 50 and not scores: scores[UNKNOWN_CRASHLOOP] = 0.60
- best = max(scores) if scores else UNKNOWN
- return {cause: best, confidence: scores[best], all_scores: scores}

### AUTH_FAILURE и config-drift: всегда ли MANUAL-ONLY?

Hyperswitch-инцидент (scram-sha-256 rejection) требовал ручного ALTER USER через local-trust socket — DDL-операция с привилегиями суперпользователя. Автоматизация без человека нарушает least-privilege и PCI DSS Req 7.

Исключение: для stateless контейнеров (не БД, не payment router), где CONFIG_DRIFT классифицирован с confidence > 0.90 и сводится к «переменная окружения не совпадает с Vault», допустим GUARDED-авто-фикс: перечитать значение из Vault и пересоздать контейнер. Условие: watchdog имеет Vault-роль read-only для конкретного KV-пути, операция идемпотентна.

Правило для банковской среды: любой авто-фикс, требующий записи в БД (ALTER, UPDATE secrets, INSERT config), — MANUAL-ONLY. Авто-фикс только через pull (чтение из Vault), никогда через push (генерация/изменение секрета самой бригадой).

***

## 4. Q3 — Пороги, Backoff и Circuit-Breaker в Fintech

### Рекомендуемые паттерны

Для crash-loop в fintech-среде правильная последовательность — не выбор одного паттерна, а каскад:
- restart_count <= N_fast -> immediate restart (SAFE)
- restart_count N_fast..N_backoff -> exponential backoff (GUARDED)
- restart_count > N_backoff -> circuit OPEN, quarantine, ESCALATE

***

## [EMBEDDED OPERATIONAL PROMPT — Wave-2 RED Decision Method]

ROLE: Factory (Claude Code). REPO = CarmiBanxe/banxe-emi-stack.
TASK: Wave-2 RED — insert "## Decision Method" (Profile-EMI, ADR-030) into 4 RED agents with RED discipline. PROPOSED. Activation deferred (via runtime-gate red_activation_check + Operator+MLRO+CEO sim-sign). Sandbox.
ISOLATED worktree off CURRENT origin/main. Branch: agent/factory/wave2red/decision-method. prepare+push+PR only, NEVER merge. --force-with-lease, named-branch. Run ruff check AND ruff format.

SCOPE — exactly these 4 (all verified RED + Autonomy Level anchor):
  agents/compliance/soul/compliance_calendar.soul.md
  agents/compliance/soul/crypto_custody.soul.md
  agents/compliance/soul/risk_management.soul.md
  agents/passports/consent_management/PASSPORT.md

PER-AGENT: pre-audit (anchor present, no DM yet, HITL decider verbatim). Insert "## Decision Method" AFTER "## Autonomy Level" per ADR-030 Profile-EMI with RED DISCIPLINE:
- Priority Note: HITL Gates > Trust Zone > B5-IRREVOCABLE > Decision Method > Autonomy Level.
- Trust Zone: RED. Lexicographic L0-TZ: RED -> gated/blocked, NO scoring bypass.
- Advisory PROHIBITED — modes: evidence_gatherer / gated_recommendation / blocked_reporter only (POCA 2002 s.330, MLR 2017, SAMLA 2018 personal liability).
- execution-class: blocked (agent prepares/gathers evidence; never executes the gated action).
- Decider (HITL) VERBATIM per file:
  compliance_calendar -> COMPLIANCE_OFFICER (deadline) / BOARD (board_report);
  crypto_custody -> Compliance Officer (large_transfer >= GBP1000, wallet_archive);
  risk_management -> Risk Officer (set_threshold, risk_acceptance);
  consent_management -> COMPLIANCE_OFFICER (revoke_consent, initiate_pisp_payment).
- Criteria (MAUT, B-2 Compliance/AML-style): regulatory_admissibility (L0 hard =1.0 else BLOCKED), evidence_quality, false_positive_cost, escalation_urgency.
- B5-IRREVOCABLE for: crypto_custody (on-chain transfer — blockchain finality) and consent_management (revoke_consent / initiate_pisp_payment — PSD2 Art.66 irreversible) -> mandatory HITL gate, DecisionRecord emitted BEFORE any prepared action, rollback IMPOSSIBLE.
- Fail-closed: any uncertainty / regulatory-admissibility<1.0 -> BLOCK; RED-zone data DROP not mask.
- Activation note: ACTIVATION requires runtime-gate red_activation_check PASS (services/runtime_gate) AND Operator+MLRO(SMF17)+CEO(SMF1) ratification (ADR-030). SOUL declaration suffices only at PROPOSED — NOT activated by this PR.

LEDGER: append INSTRUCTION-LEDGER.md "IL-WAVE2-RED-01 — DM (Profile-EMI, RED discipline) -> 4 RED agents [PROPOSED; activation via red_activation_check + Operator+MLRO+CEO]".

QUALITY + PUSH: ruff check + ruff format (both clean). Stage ONLY 4 souls + INSTRUCTION-LEDGER.md. GPG-signed commit. push --force-with-lease. Open squash PR. STOP before merge.

OUTPUT: branch, commit SHA, PR number, per-agent decider (verbatim) + B5 flags, advisory-prohibited confirmed, ruff clean, PROPOSED activation via runtime-gate + SMF. Do NOT merge, do NOT activate.

### Минимальный набор alert-правил для Prometheus (banxe-alerts.yaml)

Группа banxe_watchdog, rules:
- ComponentDown: expr banxe_component_health == 0, for 1m, severity critical, summary "{component} на {host} недоступен"
- CrashLoopCircuitOpen: expr banxe_circuit_breaker_state == 1, for 0m, severity critical
- HighRestartRate: expr rate(banxe_container_restarts_total[15m]) > 0.5, for 5m, severity warning
- ModelLatencyDegrading: expr histogram_quantile(0.95, banxe_model_response_seconds_bucket) > 15, for 10m, severity warning
- HighMemoryPressure: expr (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) < 0.10, for 5m, severity warning, annotation "менее 10% RAM — риск OOMKill"
- DiskSpaceLow: expr (node_filesystem_avail_bytes / node_filesystem_size_bytes) < 0.15, for 15m, severity warning
- WatchdogHeartbeatMissed: expr absent(banxe_watchdog_heartbeat_timestamp) or (time() - banxe_watchdog_heartbeat_timestamp) > 120, for 0m, severity critical, annotation "Бригада сама упала — требуется немедленное вмешательство"

### Предиктивные метрики: переход от реактивного к превентивному

- Restart rate trend: если rate(restarts[1h]) > rate(restarts[24h]) * 2 — контейнер деградирует, эскалировать до crash-loop
- Memory growth rate: если predict_linear(container_memory_usage_bytes[30m], 3600) > memory_limit * 0.9 — OOM предсказуем за 1 час
- Replication lag (PostgreSQL): если pg_replication_lag > 10s — риск data inconsistency при failover
- LiteLLM router error rate: если rate(litellm_errors[5m]) > 0.05 — деградация модельного слоя

***

## 6. Q5 — Надёжность Самой Бригады: Watchdog-of-Watchdog

### Systemd — необходимо, но недостаточно

systemd Restart=always защищает от крашей самого процесса watchdog, но не от: зависания (hang без crash), сетевой изоляции хоста, ошибок самого systemd, OOM kill watchdog-процесса. В production fintech единая точка отказа для monitoring-компонента — compliance-риск (SOC 2 Availability criterion).

### Dead-Man-Switch: правильный паттерн

Dead-man-switch — принцип, при котором отсутствие активного сигнала триггерит действие (эскалацию), в отличие от watchdog, который реагирует на наличие сигнала отказа. Это принципиальное различие для надёжности.

Уровень 1 — Internal heartbeat (evo1 смотрит за собой):
- HEARTBEAT_GAUGE = Gauge(banxe_watchdog_heartbeat_timestamp, Unix timestamp последнего успешного цикла)
- main_loop: while True: try run_scan_cycle(); HEARTBEAT_GAUGE.set(time.time()) при каждом успешном цикле; except: logger.error; НЕ обновляем heartbeat — Prometheus-alert WatchdogHeartbeatMissed сработает

Уровень 2 — External dead-man-switch (evo2 следит за evo1):
На evo2 запустить минимальный watchdog-guardian.py — отдельный процесс, который:
1. Каждые 60s делает HTTP GET к http://evo1:9090/metrics и парсит banxe_watchdog_heartbeat_timestamp
2. Если метрика отсутствует или timestamp старше 120s — отправляет эскалацию независимым каналом (прямой webhook/email, не через Alertmanager на evo1)
3. Сам экспортирует heartbeat-метрику в Prometheus на evo2

Предотвращение split-brain при двух наблюдателях:
Split-brain возникает, когда оба наблюдателя считают себя active и предпринимают противоречивые действия. Для watchdog-of-watchdog это менее критично, чем для БД, но нужно соблюдать:
- Только один watchdog выполняет repair actions — тот, кто локален для сервиса (evo1 управляет evo1, evo2 управляет evo2)
- Guardian на evo2 выполняет только escalation, никогда не repair actions на evo1
- Если оба watchdog видят проблему — независимо эскалируют, Alertmanager deduplicate
- Distributed lock не нужен — нет конкурирующих write-операций

Схема:
evo1: watchdog.py -> repair evo1 services + heartbeat metric
evo2: watchdog.py -> repair evo2 services + heartbeat metric; guardian.py -> monitor evo1 heartbeat -> escalate if missed (read-only)
external: Alertmanager -> deduplicate + route alerts

***

## 7. Q6 — Offline-узел Legion: Узел vs Сетевой Сбой

### Проблема различения

В текущей топологии (2 online сервера + 1 offline) невозможно с одной vantage-точки корректно различить «узел legion упал» от «сеть между evo1 и legion недоступна». Классическая проблема network partition.

### Паттерн multi-vantage point (node_reachability.py)

check_node_reachability(host, vantage_points):
- Проверяем доступность legion с нескольких точек. Недоступен ОТОВСЮДУ — узел упал. Недоступен только с evo1 — сеть.
- для каждого vp: HTTP GET http://{vp}:9101/probe?target={host}, timeout 5s; при ошибке results[vp]={reachable: False, error: probe_failed}
- reachable_count = число доступных; total = len(vantage_points)
- if reachable_count == 0: diagnosis = NODE_DOWN
- elif reachable_count < total: diagnosis = NETWORK_PARTITION
- else: diagnosis = HEALTHY
- return {diagnosis, vantage_results, confidence: reachable_count/total}

Правила для legion:
- NODE_DOWN (0 из N vantage points), confidence > 0.80: Эскалация CRITICAL + Wake-on-LAN (если настроен)
- NETWORK_PARTITION (часть точек видит): Эскалация WARNING + ждать 5 min, повторить
- Transient (1 probe failed, остальные OK): Log only, retry

### Wake-on-LAN и remote-wake

Wake-on-LAN допустим как GUARDED-действие для non-payment, non-stateful серверов (legion = AI-модели). Условие: нет риска data corruption при cold start, нет pending транзакций. WoL не гарантирует boot — после magic packet ждать 2-3 min и повторно проверить. Если узел не поднялся — ESCALATE.

attempt_wol(mac_address, broadcast=255.255.255.255): Wake-on-LAN как GUARDED action с audit log. subprocess.run([wakeonlan, -i, broadcast, mac_address],
    capture_output=True, text=True)
  audit_log(WOL_ATTEMPT, {mac: mac_address, result: result.returncode})
  await asyncio.sleep(180)  # ждём 3 минуты
  return await check_node_reachability(legion, [evo1, evo2])

***

## 8. Q7 — Эскалация: Структура без Alert Fatigue

### Принципы anti-alert-fatigue

Alertmanager предоставляет три механизма шумоподавления:
1. Grouping — объединение связанных алертов в одно уведомление
2. Inhibition — подавление менее критичных алертов при наличии более критичного
3. Silences — плановые окна обслуживания без алертов

Конфигурация Alertmanager для BANXE/EMI (alertmanager.yml):
- global: resolve_timeout 5m
- route: receiver default, group_by [alertname, host, component], group_wait 30s, group_interval 5m, repeat_interval 4h
- routes:
  - CRITICAL: matchers severity=critical, receiver pagerduty_or_telegram, group_wait 15s, group_interval 1m, repeat_interval 1h
  - WARNING: matchers severity=warning, receiver slack_engineering, group_wait 60s, group_interval 10m, repeat_interval 6h
  - Watchdog сам упал: matchers alertname=WatchdogHeartbeatMissed, receiver direct_sms (независимый канал)
- inhibit_rules: source severity=critical подавляет target severity=warning при equal [component, host]

### Структура эскалационного сообщения

Каждое эскалационное событие содержит достаточно контекста для действия без открытия Grafana. EscalationEvent (dataclass):
- timestamp (ISO8601), severity (CRITICAL/WARNING/INFO), component (hyperswitch, evo2:llama3.3:70b), host
- root_cause (AUTH_FAILURE/OOM/CONFIG_DRIFT/UNKNOWN), cause_confidence (0.0-1.0)
- restart_count, last_exit_code, last_log_snippet (последние 500 символов)
- actions_attempted (list), recommended_action (конкретная рекомендация), audit_id (UUID для связи с immutable audit log)

Пример сообщения:
CRITICAL — hyperswitch on evo1. Root cause: AUTH_FAILURE (confidence 0.94). Restarts 47, Exit code 1. Log: password authentication failed for user hyperswitch_app (FATAL). Actions attempted: [start_container -> failed, root_cause_escalated]. Recommended: ALTER USER hyperswitch_app PASSWORD via postgres local socket. Audit ID a3f9-2b81-...

***

## 9. Q8 — Compliance и Immutable Audit Trail

### PCI DSS Requirement 10 — обязательные требования

PCI DSS v4.0 Requirement 10 мандатирует для всех систем в CDE:
- Каждый log entry: user/process identification, тип события, timestamp, success/failure, source IP/host, affected component
- Tamper-proof: лог-файлы не могут быть изменены/удалены теми, кто их генерирует
- Retention: минимум 12 месяцев, 3 месяца immediately available
- Daily review: обязателен для CDE-компонентов
- Automated alerting: явно обязателен в v4.0 (не просто рекомендован)

### Immutable Audit Trail для watchdog (audit_log.py — append-only)

AUDIT_LOG_PATH = /var/log/banxe-watchdog/audit.jsonl (JSONL — append-only, каждая строка отдельный JSON-объект)

audit_log(event_type, payload, component, result):
- Immutable audit entry. Никогда не изменяет существующие записи. Хэш предыдущей записи включён для chain-integrity (упрощённый blockchain-pattern).
- prev_hash = _get_last_hash()
- entry = {audit_id: uuid4, timestamp: ISO8601 gmtime, event_type (REPAIR_ATTEMPT/ESCALATION/CONFIG_READ), component, result (SUCCESS/FAILED/SKIPPED), payload, watchdog_version, prev_entry_hash: prev_hash}
- entry_json = json.dumps(entry, sort_keys=True)
- entry[entry_hash] = sha256(entry_json)
- append в файл, return audit_id

Защита audit log от tampering:
- Файл audit.jsonl — chattr +a (append-only на уровне FS)
- Ежедневная репликация на evo2 и/или S3-совместимое хранилище с Object Lock (WORM)
- Chain-hash верификация при аудите: verify_audit_chain.py

### Платёжные компоненты и авто-ремонт

hyperswitch обрабатывает карточные данные и является частью CDE. PCI DSS Req 6.4 требует formal change management для любых изменений в CDE. SOC 2 CC8.1 требует авторизации изменений.
Для hyperswitch допустимы только:
1. Read actions: сбор логов, метрик, exit-code
2. Escalation: немедленная с full context
3. Circuit open: watchdog перестаёт пытаться что-либо делать и ждёт human
4. Никаких: start_container, recreate, config_sync, env_update

***

## 10. Q9 — Безопасность Секретов при Автономных Действиях

### Принцип: watchdog должен уметь читать, но не знать

Бригада не хранит секреты. Но для GUARDED-действий нужен read-only доступ к Vault. Паттерн: Vault AppRole с short-lived token.
- watchdog startup: читает VAULT_ROLE_ID из env (не секрет — это ID роли); читает VAULT_SECRET_ID из Docker secret или Vault Agent; аутентифицируется в Vault -> token TTL=1h; token для read-only KV на конкретные пути; по истечении TTL — refresh через Vault Agent (сайдкар)

Vault Policy watchdog (watchdog-policy.hcl, минимальные права):
- path secret/data/banxe/+/db_password: capabilities [read] (только чтение, для сравнения с running config)
- path secret/data/banxe/+/service_config: capabilities [read]
- path secret/*: capabilities [deny] (явный запрет на запись/удаление/создание)

Vault Agent Sidecar (docker-compose.watchdog.yml):
- vault-agent: image hashicorp/vault, command agent -config agent.hcl, volume vault-token:/vault/token, env VAULT_ADDR http://vault:8200
- banxe-watchdog: build ./watchdog, volume vault-token:/vault/token:ro (read-only доступ к токену)

### Действия, требующие привилегий (DB password sync)

Если требуется действие уровня ALTER USER (MANUAL-ONLY по определению), watchdog НЕ получает DB-пароль суперпользователя. Вместо этого:
- Watchdog классифицирует причину (AUTH_FAILURE) и формирует структурированный тикет
- Тикет содержит точную команду для оператора: ALTER USER ... PASSWORD ... — скопировать из Vault UI
- Оператор выполняет через psql с local-trust socket (как было в инциденте)
- Действие логируется в audit trail с оператором как principal

***

## 11. Целевая Архитектура: Production-Ready Blueprint

Компонентная диаграмма:
evo1:
- banxe-watchdog.py: Scanner (Ollama+Docker) -> RootCause Classifier (exit+log+hc) -> DecisionPolicy (SAFE/GUARDED/MANUAL-ONLY) -> RepairEngine [SAFE: warm_model, start_container; GUARDED: recreate_stateless, config_sync_vault; MANUAL-ONLY -> EscalationEngine] -> AuditLogger (JSONL+hash) + PrometheusExporter
- Vault Agent (token renew), Prometheus (:9090), Grafana (:3000)
evo2:
- banxe-watchdog.py (зеркало для evo2 сервисов)
- watchdog-guardian.py (dead-man-switch для evo1): проверяет banxe_watchdog_heartbeat_timestamp с evo1, эскалирует через независимый канал если missing > 120s
External: Alertmanager -> PagerDuty/Telegram/Email; Vault HA; S3/Object Lock (audit log archive)

## 12. Roadmap: sandbox -> production

Спринт 1 (1-2 недели) — Critical Gap Closure:
1. Устранить hardcode threshold=10: единый config_loader.py с validation
2. Добавить root_cause_classifier.py с exit-code + log-pattern таблицей
3. Добавить audit_log.py с append-only JSONL + chain hash
4. Восстановить Prometheus/Grafana, добавить watchdog_exporter.py

Спринт 2 (2-3 недели) — Observability & Reliability:
5. Alertmanager grouping + inhibition + deadman alert для watchdog
6. watchdog-guardian.py на evo2 (dead-man-switch layer 2)
7. Heartbeat метрика в main_loop
8. Vault Agent sidecar + watchdog-policy.hcl (read-only KV)

Спринт 3 (3-4 недели) — GUARDED actions & Legion:
9. recreate_container() для stateless с backoff + circuit-breaker
10. multi_vantage_check() для legion + WoL как GUARDED action
11. config_drift_detector.py с Vault-pull pattern для stateless
12. Grafana dashboard: компоненты + circuit states + latency + restart rates

Спринт 4 (compliance hardening):
13. Audit log replication (evo2 + S3 WORM)
14. verify_audit_chain.py — утилита верификации integrity
15. Документация: runbook для каждого MANUAL-ONLY scenario
16. Pentest: проверить что watchdog не имеет пути эскалации привилегий

***

## 12. Итоговая Таблица по 9 Вопросам

- Q1 Граница автономности: SAFE/GUARDED/MANUAL-ONLY — правильно. hyperswitch = MANUAL-ONLY по PCI DSS. CRITICAL
- Q2 Root-cause классификатор: Exit-code + log regex + OOMKilled flag. AUTH_FAILURE -> MANUAL-ONLY для БД, допустим GUARDED для stateless через Vault-pull. CRITICAL
- Q3 Пороги и backoff: Каскад fast restart -> exp backoff -> circuit open -> quarantine. Централизовать через config_loader с startup validation. HIGH
- Q4 Наблюдаемость: Custom Prometheus exporter от watchdog + 6 alert-rules + предиктивные метрики (memory growth, latency p95, restart rate trend). HIGH
- Q5 Надёжность бригады: systemd + heartbeat metric + external guardian на evo2 (dead-man-switch). Split-brain: guardian read-only, один watchdog per host. HIGH
- Q6 Offline legion: Multi-vantage check (оба evo). NODE_DOWN если 0 из N -> WoL (GUARDED). NETWORK_PARTITION если частичная -> wait + escalate. MEDIUM
- Q7 Эскалация: Alertmanager grouping+inhibition. Structured EscalationEvent с root_cause + confidence + recommended_action + audit_id. HIGH
- Q8 Compliance/audit: PCI DSS Req 10 JSONL append-only с chain hash, 12 мес retention, S3 WORM. hyperswitch MANUAL-ONLY без исключений. CRITICAL
- Q9 Безопасность секретов: Vault AppRole + short-lived token (TTL=1h) + Vault Agent sidecar. Watchdog policy read-only KV. Нет plaintext secrets в env. HIGH

***

## References

1. Self-Healing Infrastructure for FinTech (SentienGuard) — software-defined operations detect/diagnose/remediate.
2. CrashLoopBackoff Kubernetes: An Ultimate Guide — container repeatedly starts/crashes/restarts, exp backoff.
3. Self-Healing Infrastructure — Red Hat Architecture Center — automation identify and repair errors.
4. The Ultimate Guide to PCI DSS and SOC 2 Compliance for fintech.
5. Journal of AI/ML — ML-driven self-healing framework for preemptive failure.
6. The Timeout, Retry, and Circuit-Breaker Patterns.
7. Circuit Breaker Pattern: How It Works, Benefits, Best Practices.
8. SOC 2 for Fintech Companies: Controls and Audit Guide.
9. Building PCI DSS Compliant Infrastructure for Payment (Requirement 10 tamper-resistant storage).
10. CrashLoopBackOff in Kubernetes: Causes and Fixes.
11. Docker OOMKilled: causes, detection, prevention (exit 137).
12. PCI DSS Logging and Audit Trail Best Practices (Requirement 10).
13. Why we need short-lived credentials — HashiCorp Vault dynamic secrets.
14. Automatically detect resource drift and health (HashiCorp).
15. Monitor API Health Check with Prometheus.
16. Monitoring with Custom Metrics.
17. Predictive Automation for High-Availability Banking Systems (prevention-first self-healing).
18. Redundancy versus Single Points of Failure.
19. How to Build Split-Brain Prevention (quorum-based voting).
20. Network Partitions & Split-Brain Explained for Beginners (leader election).
21. Prometheus Alertmanager: Routing, Grouping and Setup — reducing fatigue by grouping.
22. How to Set Up Alert Deduplication and Grouping for High-availability (OpenTelemetry).
23. Avoiding Network Partitions — VoltDB (no way to differentiate partition vs node down).
24. Network Partition — Dremio (nodes become unreachable).
25. Prometheus Alertmanager: Noise Reduction Rules (grouping categorizes alerts).
26. PCI Logging Rules Your Organization NEEDS to Know (Req 10.2.2 automated audit trails).
27. Centralized Secret Management with HashiCorp Vault and short-lived access tokens (Docker Compose).
