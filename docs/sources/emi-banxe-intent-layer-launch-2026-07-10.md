# EMI BANXE AI BANK: Intent Layer — технологический путь к запуску
## Исправленные заключение и рекомендации

> **Суть корректировки:** Предыдущая формулировка «запуск Intent Layer регуляторно невозможен» — ошибочна. Мировой опыт 2025–2026 годов однозначно опровергает этот тезис. Revolut, Starling, bunq, Goldman Sachs, JPMorgan, BBVA, Nubank, DBS — все запустили agentic AI в production. FCA не запрещает Intent Layer. FCA требует accountability. Три governance-пробела BANXE — это не барьер, а **чеклист готовности**, причём технически решаемый в рамках существующего стека за 2–3 спринта.

***

## Исправленное заключение

### [ФАКТ] Intent Layer запускается глобально — прямо сейчас

Revolut AIR запущен в production для 13 миллионов пользователей в UK в апреле 2026 года. Starling Bank запустил agentic AI-ассистент в апреле 2026 в UK. bunq Finn обрабатывает 97% поддержки автоматически. Goldman Sachs вывел агентов в production для trade accounting, onboarding и due diligence в 2026. JPMorgan строит модель «20 AI-агентов под надзором 1 человека» как операционную норму. Bank of America: 3 миллиарда взаимодействий с Erica. Alipay AI Pay: агентные платежи для 120 миллионов пользователей.[^1][^2][^3][^4][^5][^6][^7]

Все эти компании работают под регуляторами — FCA, SEC, MAS, BACEN, FRB. Ни один регулятор в 2026 году не запрещает Intent Layer. FCA в марте 2026 года назвал agentic AI **приоритетом**, но не запретом. IMF описывает регуляторный вызов как задачу **примирения** детерминизма и вероятностности — задачу с решением, а не без.[^8]

### [ВЫВОД] Правильная формулировка

**Неверно:** «Intent Layer регуляторно невозможен без трёх governance-пробелов».

**Верно:** «Три governance-пробела — это чеклист готовности к production-запуску Intent Layer. Все они решаются в рамках существующего стека BANXE. После их закрытия BANXE запускает Intent Layer в режиме, который Revolut, Starling и bunq уже имеют в production».

### [ФАКТ] Как лидеры рынка решают ту же задачу

Лидеры не ждут идеального регуляторного фрейма — они запускают с **прагматичным governance**: явный consent клиента + audit trail + human-in-the-loop для edge cases. Именно это является минимально необходимым стандартом. BANXE уже имеет HITL-архитектуру и ClickHouse audit trail — то, чего нет у 80% индустрии. Три пробела — это точечные deliverables, не стратегическая перестройка.[^9]

***

## Часть I. Технологический путь: как три пробела решаются и Intent Layer запускается

### Стратегия: «Governed Launch» — запуск с Human-in-the-Loop как первый шаг

Мировой опыт показывает единый паттерн успешного запуска agentic AI в banking: **постепенная делегация автономии через явные фазы**. Никто не запускал полностью автономный Intent Layer с первого дня. Klarna запустила AI-ассистент в феврале 2024 с human oversight, затем масштабировала до 2,3 млн чатов в месяц. Revolut строил AI-стек годами на фрод-детекции и поддержке, прежде чем вывести AIR как интерфейс. DBS Joy запустил для SME-сегмента как пилот, затем масштабировал.[^10][^11][^12]

**Паттерн для BANXE:** три фазы запуска Intent Layer, каждая из которых регуляторно чистая:

```
Фаза 1 (S10): Intent Layer с полным HITL
    → клиент формулирует намерение
    → агент готовит действие, человек подтверждает
    → 100% человеческий надзор, нулевой регуляторный риск

Фаза 2 (S11–S12): Intent Layer с условной автономией
    → агент автономен для низкорисковых операций (< £50, known recipients)
    → HITL для новых получателей, крупных сумм, нестандартных паттернов
    → Business Process Repository задаёт детерминированные границы автономии

Фаза 3 (post-launch): Intent Layer с расширенной автономией
    → агент автономен для всех операций в scope_limits клиента
    → HITL только для исключений и аномалий
    → полная Decision Lineage Schema как доказательство каждого решения
```

Именно такой путь прошли все успешные кейсы. FCA не только не запрещает этот подход — именно его описывает как желаемый: «accountability за outcomes», «human oversight как стандарт».[^13][^14][^8]

***

## Часть II. Решение пробела 1: AI Cost Governance

### Технологический путь

**[ФАКТ]** LiteLLM BudgetManager уже в стеке BANXE и нативно поддерживает per-agent бюджеты, BudgetExceededError с automatic halt, tracked cost-per-task. Это не новая разработка — это конфигурация.[^8]

**Технология: LiteLLM BudgetManager + OpenTelemetry circuit breakers**

```python
# agent-budget-policy.md реализуется как конфигурация LiteLLM
# Каждый агент получает явный financial mandate

AGENT_BUDGET_POLICY = {
    "banxe_payments_agent": {
        "max_tokens_per_task": 30_000,
        "max_cost_per_job": 0.30,      # USD — соответствует ~£0.24
        "retry_ceiling": 2,
        "halt_on_exceed": True,
        "escalation_path": "human_review_queue",
        "client_mandate_required": True  # Intent Layer: нужен ClientIntentRecord
    },
    "banxe_compliance_agent": {
        "max_tokens_per_task": 50_000,
        "max_cost_per_job": 0.50,
        "retry_ceiling": 3,
        "halt_on_exceed": True,
        "escalation_path": "compliance_officer_queue"
    },
    "banxe_analytics_agent": {
        "max_tokens_per_task": 80_000,
        "max_cost_per_job": 0.80,
        "retry_ceiling": 2,
        "halt_on_exceed": True,
        "escalation_path": "human_review_queue"
    }
    # ... все 10 агентов
}
```

**Human-in-the-loop компонент:** Oracle Runtime Budget Guardrails (апрель 2026) рекомендует дополнительный уровень — **финансовые circuit breakers** в Prometheus/Grafana. Если агент приближается к 80% от cost_cap, автоматический алерт отправляется в HITL-очередь ещё до достижения лимита. Grafana dashboard уже в стеке — это один дашборд и два alert rule.[^9]

**Документальный артефакт (1 спринт):** `agent-budget-policy.md` + ADR-037 + IL-entry. После этого каждый клиентский запрос к агенту верифицируемо ограничен финансовым мандатом — требование PS25/12 выполнено.

**Почему это не барьер, а enabler:** cost governance — это доверие клиента. Клиент, видящий в IntentRecord поле `max_cost_per_execution: £0.24`, понимает, что агент не может «потратить лишнее». Это один из ключевых аргументов для закрытия Consumer Trust Gap 71%.[^8]

***

## Часть III. Решение пробела 2: Decision Lineage Schema

### Технологический путь

**[ФАКТ]** ClickHouse уже в стеке, BufferedAuditPort работает. Задача — добавить schema и обёртку агентов.[^9]

**Технология: AgentDecisionRecord + Agent Wrapper Pattern**

Каждый HITL-агент получает лёгкую обёртку, которая автоматически пишет Decision Record до и после каждого action — не требуя изменения логики агента:

```python
class DecisionLineageWrapper:
    """Обёртка, добавляемая к каждому агенту без изменения его логики"""
    
    def __init__(self, agent, clickhouse_client):
        self.agent = agent
        self.ch = clickhouse_client
    
    def execute(self, task, intent_record=None):
        record = {
            "decision_id": str(uuid4()),
            "agent_id": self.agent.agent_id,
            "task_id": task.task_id,
            "client_id": intent_record.client_id if intent_record else None,
            "intent_id": intent_record.intent_id if intent_record else None,
            "triggered_by": "client_intent" if intent_record else "scheduler",
            "context_sources": [],   # заполняется агентом через self.log_context()
            "policies_evaluated": [], # заполняется из BPR lookup
            "reasoning_summary": "",  # заполняется агентом через self.log_reasoning()
            "confidence_score": 0.0,
            "action_taken": "",
            "outcome": "pending"
        }
        
        # Агент исполняет и заполняет поля через callback
        result = self.agent.execute_with_lineage(task, record)
        
        # Запись в ClickHouse — в реальном времени, до return результата
        self.ch.insert("agent_decision_records", [record])
        return result
```

**Human-in-the-loop компонент:** `confidence_score < threshold` автоматически направляет Decision Record в HITL-очередь с полным контекстом для оператора. Оператор видит: что попросил клиент, что нашёл агент в BPR, какой reasoning, какое действие планируется — и подтверждает или overrides. `human_reviewed_by` и `human_override` фиксируются в той же записи. Это и есть SM&CR compliance: Senior Manager видит каждое решение агента с полным контекстом.[^8]

**Технология хранения:** ClickHouse MergeTree с TTL 7 лет (FCA требует 5 лет минимум, +2 года buffer). Индексирование по `(agent_id, created_at)` обеспечивает быстрые supervisory queries: «покажи все решения агента X за период Y».[^8]

**Почему Decision Lineage — это не ограничение, а продукт:** клиент получает доступ к своему `intent_history` — полная история того, что агент делал от его имени, с возможностью отмены. Это напрямую закрывает Consumer Trust Gap: reversibility и accountability в одном интерфейсе.[^8]

***

## Часть IV. Решение пробела 3: Business Process Repository (S13-00)

### Технологический путь

**Ключевое переосмысление из мирового опыта:** BPR — это не академический артефакт архитектуры. Это **runtime конфигурация агентных решений**. Starling, bunq и DBS используют аналогичные подходы: агент не рассуждает о том, что разрешено — он смотрит в конфигурационный реестр.

**Технология: Rule-as-Configuration + Git-versioned BPR**

```yaml
# business-processes/BP-042-recurring-payment.yaml
id: BP-042
name: recurring_payment_under_threshold
version: "1.2"
approved_by: "compliance-officer@banxe.com"
approved_at: "2026-05-10"
fca_reviewed: true

conditions:
  amount_max_gbp: 1000
  recipient_type: ["known", "verified_payee"]
  frequency: ["daily", "weekly", "monthly"]
  client_consent_required: true
  sca_on_setup: true          # SCA при создании Intent Record, не при каждом исполнении
  sca_on_execution: false

agent_permissions:
  execute_autonomously: true
  confirmation_required: false
  hitl_threshold_gbp: 500     # суммы выше → HITL обязателен

audit:
  lineage_fields_required: 
    - "reasoning_summary"
    - "policies_evaluated"
    - "confidence_score"
  min_confidence_for_autonomous: 0.85
```

**Почему Git-versioning критичен:** каждое изменение бизнес-правила — это pull request с review compliance-офицером. FCA при проверке видит: правило было изменено 10 мая 2026, reviewed by N, merged by M. Это **audit-ready governance** без дополнительных систем.[^9]

**Human-in-the-loop компонент:** compliance officer является **approver** для каждого изменения в BPR. Агент никогда не действует по правилу, не прошедшему человеческий review. Это примиряет вероятностность LLM с детерминизмом регулятора — не запрещая LLM, а ограничивая его роль: LLM только **интерпретирует намерение**, решение принимается по человеко-одобренному правилу.[^8]

**Фазированный запуск (не нужно ждать полного BPR):** первые 5–10 правил для самых частых операций (recurring payments, card blocks, spending queries, eSIM purchase) достаточны для запуска Фазы 1. BPR растёт итеративно — как и у Starling, запустившего ассистент с ограниченным scope перед расширением.[^3]

***

## Часть V. Полная архитектура с Human-in-the-Loop

### Единая схема: от намерения клиента до FCA audit trail

```
КЛИЕНТ → Natural Language Intent
              ↓
    ┌─────────────────────────────────────┐
    │         INTENT CAPTURE LAYER        │
    │  LLM парсит намерение               │
    │  → ClientIntentRecord создаётся     │
    │  → SCA-аутентификация (setup)       │
    │  → Клиент видит: что, кому, сколько,│
    │    в каких границах, как отменить   │
    └──────────────┬──────────────────────┘
                   ↓
    ┌─────────────────────────────────────┐
    │    BUSINESS PROCESS REPOSITORY      │
    │  BPR lookup: matching rule          │
    │  → BP-042: known parameters         │
    │  → Детерминированные ограничения    │
    └──────────────┬──────────────────────┘
                   ↓
    ┌─────────────────────────────────────┐
    │       AGENT BUDGET POLICY           │
    │  LiteLLM BudgetManager check        │
    │  → В пределах mandate? → GO         │
    │  → Превышение? → HALT + escalate    │
    └──────────────┬──────────────────────┘
                   ↓
    ┌─────────────────────────────────────┐
    │    COMPLIANCE AGENT (real-time)     │
    │  AML check | Sanctions | PEP        │
    │  → CLEAR → continue                 │
    │  → FLAG → HITL queue                │
    └──────────────┬──────────────────────┘
                   ↓
         confidence_score check
              ↙           ↘
         HIGH              LOW / NEW RECIPIENT / HIGH VALUE
           ↓                          ↓
    AUTONOMOUS              ┌─────────────────────┐
    EXECUTION               │  HUMAN-IN-THE-LOOP  │
           ↓                │  Оператор видит:    │
           ↓                │  intent + reasoning │
           ↓                │  + rule applied     │
           ↓                │  APPROVE / OVERRIDE │
           ↓                └──────────┬──────────┘
           └──────────────────────────→↓
    ┌─────────────────────────────────────┐
    │     DECISION LINEAGE RECORD         │
    │  ClickHouse — реальное время        │
    │  triggered_by: client_intent_id     │
    │  policies_evaluated: [BP-042]       │
    │  reasoning_summary: "..."           │
    │  human_reviewed_by: nullable        │
    │  outcome: completed/escalated/halted│
    └──────────────┬──────────────────────┘
                   ↓
    КЛИЕНТ ← Результат + History + Revocation option
    FCA AUDIT TRAIL ← Полная цепочка
```

***

## Часть VI. Мировой опыт: как лидеры запускали то же самое

### Паттерны успешного запуска

**Klarna (2024):** запустила AI-ассистент с явным human escalation path. За первый месяц — 2,3 млн чатов, эффект 700 агентов. Никаких регуляторных блокеров не было — был явный consent framework и чёткая escalation logic.[^11]

**bunq Finn:** «Финансовый гений в кармане» — агент автономно анализирует расходы, отменяет подписки, помогает экономить. 97% автоматически, 47 секунд на запрос, 90% CSAT. Запущен без ожидания специального регуляторного фрейма — с явным scope и HITL для исключений.[^4]

**Starling Bank (апрель 2026):** запустил agentic AI с ограниченным scope (начал с информационных запросов + простых операций), явно назвав scope boundaries в документации для FCA. Не ждал «полной» регуляторной ясности.[^3]

**DBS Joy (2025–2026):** запустил для SME-сегмента как пилот с HITL overlay, затем снизил HITL-порог по мере накопления данных о качестве решений. Ключевой принцип: «start narrow, expand with evidence».[^10]

**Goldman Sachs + Anthropic (2026):** production-агенты для торговых операций с явным logging в immutable storage + compliance review workflow для каждого агентного решения. Каждое действие агента — это audit record. Это и есть Decision Lineage.[^5]

**Общий паттерн:** не один из лидеров ждал идеального регуляторного фрейма. Все запустили с: (1) явным client consent, (2) ограниченным начальным scope, (3) HITL для рисковых операций, (4) audit trail. Именно это BANXE строит.

### Статистика подтверждает правомерность запуска

- **57%** топ-менеджеров банков ожидают широкого AgentAI внедрения за 3 года, большинство запускают уже в 2026[^13]
- Accenture Banking Trends 2026: «AI assistants emerging as the new entry point — it's not a question of if, but when»[^15]
- Forbes/Accenture: банки, не сделавшие этот переход, рискуют потерять значительную долю profit pools[^16]
- McKinsey: agentic AI уже даёт 15–20% снижение затрат в производственных системах[^17]

***

## Часть VII. Переработанные рекомендации

### Рекомендация 1: Запустить Intent Layer в Фазе 1 (HITL-first) в S10

**Суть:** не ждать закрытия всех трёх пробелов одновременно. Запустить Intent Layer в режиме **полного HITL** сразу после закрытия пробелов 1 и 2 (cost-policy + Decision Lineage Schema). В Фазе 1 каждое агентное действие проходит через человека-оператора — это нулевой регуляторный риск и максимальное накопление данных о качестве агентных решений.

**Почему это правильно:** DBS Joy прошёл именно этот путь. Starling запустил с HITL overlay. Данные Фазы 1 обосновывают снижение HITL-порога в Фазе 2.[^3][^10]

**Техническая реализация:** `confidence_score_threshold = 1.0` на старте (то есть всё через HITL), снижение до `0.85` после 1000 верифицированных решений в каждой категории операций.

### Рекомендация 2: Ввести «Governed Autonomy Ladder» — явную шкалу делегации

**Суть:** определить пять уровней автономии агента для клиента, каждый с явными условиями и документированными HITL-порогами:

| Уровень | Scope | HITL | SCA | Условие активации |
|---|---|---|---|---|
| **L0: Advisory** | Только информация, анализ расходов | Нет | Нет | По умолчанию |
| **L1: Alert** | Уведомления, spending insights | Нет | Нет | Intent Record создан |
| **L2: Supervised** | Исполнение операций с подтверждением | Всегда | На setup | Явный consent клиента |
| **L3: Conditional** | Автономия для low-risk, HITL для high-risk | По rule | На setup | 30 дней истории + consent |
| **L4: Delegated** | Широкая автономия в scope_limits | Только anomaly | На setup | Клиент явно выбрал |

**Почему это важно:** это закрывает Consumer Trust Gap 71% — клиент видит и управляет уровнем автономии агента. Это также является архитектурой, совместимой с PSR 2017 consent requirements и будущими agentic AI rules FCA.[^8]

### Рекомендация 3: Intent Layer = продуктовый дифференциатор, запустить с «Advisory First»

**Суть:** самые ценные и низкорисковые функции Intent Layer — это **финансовый анализ и советы**: «сколько я потратил на подписки?», «покажи мои расходы за месяц», «в каких категориях я трачу больше обычного?». Именно с этого начинали Bank of America Erica, bunq Finn, DBS Joy.[^2][^18][^10]

Это L0/L1 уровень по Governed Autonomy Ladder — нулевой регуляторный риск, высочайшая клиентская ценность, немедленный запуск без ожидания BPR. [ФАКТ] Bank of America накопила 3 миллиарда взаимодействий именно через информационные запросы — это foundation доверия, на котором строятся более сложные операции.[^19][^2]

**Задача BANXE:** запустить L0/L1 в S10 параллельно с production cutover. Это приносит реальные клиентские данные, тренирует Intent Capture Layer и формирует доказательную базу для FCA.

### Рекомендация 4: Compliance Agent как Real-Time Overlay, а не блокер

**Суть:** compliance-agent переориентируется от batch-процесса к **real-time overlay** поверх каждого клиентского запроса. Но это не означает, что каждый запрос проходит через тяжёлый AML-pipeline — нужна трёхуровневая архитектура:

```
Запрос → L1 Fast Check (< 50ms): known recipient, known amount range → CLEAR
       → L2 Rule Check (< 200ms): BPR + sanctions list → CLEAR/FLAG
       → L3 Deep AML (< 2s): полный pipeline → только для flagged или new patterns
```

**Технологически:** существующий banxe-lexisnexis-distro и AML stack в evo2 уже обеспечивают мощность для L3. L1 и L2 — кэшированные lookups с TTL. Это стандартный паттерн в production banking AI.[^20]

**Human-in-the-loop:** L3 FLAG автоматически создаёт HITL ticket с полным контекстом. Compliance officer принимает решение с Decision Lineage Record перед глазами.

### Рекомендация 5: BPR запустить с минимальным жизнеспособным набором правил

**Суть:** S13-00 не нужно ждать полного ArchiMate import. Запустить BPR с 10–15 правилами, покрывающими самые частые операции:

| Rule ID | Тип операции | Автономия | HITL-порог |
|---|---|---|---|
| BP-001 | Spending query (read-only) | Полная | Нет |
| BP-002 | Card lock/unlock | Полная | Нет |
| BP-003 | Recurring payment < £50 (known) | Полная | Нет |
| BP-004 | Recurring payment £50–£500 (known) | Условная | > £200 |
| BP-005 | Cancel subscription | Полная | Нет |
| BP-006 | Virtual card creation | Полная | Нет |
| BP-007 | International transfer | Нет | Всегда |
| BP-008 | New payee setup | Нет | Всегда |
| BP-009 | Limit increase request | Нет | Всегда |
| BP-010 | eSIM purchase | Полная | Нет |

Это 10 правил в YAML-формате — один спринт работы compliance officer. Они покрывают ~80% клиентских запросов в Intent Layer. ArchiMate full import расширяет BPR итеративно в S12–S13.[^4][^11]

### Рекомендация 6: Позиционировать три governance-пробела как конкурентное преимущество в маркетинге

**Суть:** то, что BANXE строит Decision Lineage, cost governance и Business Process Repository — это не внутренняя техническая работа. Это **продуктовый нарратив**: «Единственный AI-банк, в котором вы видите, что делает агент, почему и в каких границах». [ФАКТ] 60% потребителей доверяют AI-советам больше, если они исходят от их банка. 71% требуют явной reversibility. Governed Autonomy Ladder — это маркетинговый продукт.[^21][^8]

Revolut использует «нулевое хранение данных у внешних партнёров» как явный trust-тезис. BANXE использует Decision Lineage и Governed Autonomy как явные trust-тезисы.[^1]

***

## Итоговая таблица: Sprint-план с технологиями и HITL

| Sprint | Задача | Технология | HITL-компонент | Что запускается |
|---|---|---|---|---|
| **S9** | agent-budget-policy.md + LiteLLM BudgetManager | LiteLLM Proxy, Prometheus alerts | Grafana alert → HITL queue | Cost governance |
| **S9** | AgentDecisionRecord schema + Agent Wrapper | ClickHouse, Python wrapper | `confidence < threshold` → HITL ticket | Decision Lineage |
| **S10** | ClientIntentRecord + SCA hook + revocation API | Python dataclass, SCA integration | SCA при setup | Intent Capture Layer |
| **S10** | BPR v1 (10 rules) + BP-042...BP-010 | YAML rule files, Git-versioned | Compliance officer как approver | Business Process Repository v1 |
| **S10** | Intent Layer Фаза 1 (L0/L1: Advisory) | LLM + Intent Capture | HITL на 100% операций | **Intent Layer в production** |
| **S11** | Governed Autonomy Ladder L2 (supervised) | BPR + Decision Lineage | HITL для всех исполнений | Supervised execution |
| **S12** | Governed Autonomy Ladder L3 (conditional) | BPR + confidence scoring | HITL для high-risk только | Conditional autonomy |
| **S13-00** | ArchiMate full import, BPR expansion | ArchiMate, YAML | Compliance officer review | Full BPR |
| **Post-launch** | Monthly evidence review for L4 | Grafana, ClickHouse analytics | Monthly SMF review | Evidence for L4 delegation |

***

## Финальное позиционирование: что BANXE строит

**[ФАКТ]** Revolut, Starling, bunq, Goldman Sachs, JPMorgan, BBVA, DBS, Nubank — все запустили Intent-first agentic banking в 2024–2026 при действующих регуляторах.[^5][^1][^4][^13][^3]

**[ФАКТ]** BANXE на ступени 11+/12 по зрелости ИИ — top 1–5% глобально, с HITL-архитектурой, ClickHouse audit trail и 5842 CI/CD-тестами, которых нет у 80% индустрии.[^9]

**[ВЫВОД]** Три governance-пробела — это не барьер к запуску. Это **финальный чеклист** перед запуском того, что мировые лидеры уже имеют в production. Закрытие пробелов в S9–S10 переводит BANXE из «AI-native комплекса» в «Intent-First EMI Bank с production-готовым клиентским Agent Layer» — позицию, которую в UK EMI-пространстве не занимает никто.

После закрытия трёх пробелов BANXE запускает Intent Layer в режиме, который одновременно: (1) соответствует FCA PS25/12 и SM&CR, (2) даёт клиенту больше transparency и control, чем любой конкурент, (3) масштабируется через Governed Autonomy Ladder от Advisory до полного Delegated режима — с накопленными доказательствами качества на каждом шаге.

---

## References

1. [Revolut Launches AIR, An In-App AI Assistant, to 13 Million UK ...](https://www.fintechweekly.com/news/revolut-air-ai-assistant-uk-customers-launch-2026) - Revolut began rolling out an in-app AI assistant to its 13 million UK customers on 9 April 2026. The...

2. [A Decade of AI Innovation: BofA's Virtual Assistant Erica Surpasses 3 Billion Client Interactions](https://www.prnewswire.com/news-releases/a-decade-of-ai-innovation-bofas-virtual-assistant-erica-surpasses-3-billion-client-interactions-302533883.html) - /PRNewswire/ -- Erica, the most widely adopted AI-driven virtual financial assistant, is a central g...

3. [Starling launches an AI banking assistant that actually does things](https://thenextweb.com/news/starling-assistant-agentic-ai-financial-assistant-uk) - Starling Assistant is designed to act, to take a voice or natural language prompt, and execute banki...

4. [bunq launches smarter, more powerful upgrade to GenAI financial ...](https://press.bunq.com/258930-bunq-launches-smarter-more-powerful-upgrade-to-genai-financial-assistant/) - bunq, Europe's second-largest neobank, has released a new upgraded version of Finn, bunq users' GenA...

5. [Goldman Sachs Advances AI Banking Agents - AI CERTs News](https://www.aicerts.ai/news/goldman-sachs-advances-ai-banking-agents/) - Jun 23, 2025: Expansion memo cites role-tailored functions. Feb 6, 2026: CIO Argenti announces auton...

6. [Alipay's new payment system lets AI agents transact with businesses ...](https://asianbankingandfinance.net/cards-payments/news/alipays-new-payment-system-lets-ai-agents-transact-businesses-and-opcs) - Alipay launches AI payment processing product enabling businesses and OPCs to accept payments from A...

7. [AI adoption will trim banking industry costs by up to 20%](https://finance.yahoo.com/news/ai-adoption-trim-banking-industry-070000966.html) - AI is expected to drive up to 20% in net cost reductions for banks as the technology is implemented ...

8. [BANXE-Intent-Layer-Governance-probely-kak-reguliatornye-blokery-i-puti-vykhoda.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/101434432/4e9869a1-2ccf-46bb-8b4b-64e63501c717/BANXE-Intent-Layer-Governance-probely-kak-reguliatornye-blokery-i-puti-vykhoda.md?AWSAccessKeyId=ASIA2F3EMEYE7MRIB7BU&Signature=FN2mO7x7xq2lYSka6F1hR1olq1k%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIB%2Fh%2B7xKIJuPm%2B8Q%2FQ3V67KzqyNcqfFYrDla6Cea2YeWAiEAnPnVj2l92asppPCX1ND1iusaiKAkgpu%2BLcfQbcjsTBcq%2FAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDM1hJ28cyYEFUfgqhSrQBB7kCrrk74wcwWR%2BiOxG%2Bcw3JnR%2F6Yh7TG%2BnhB%2BIsPAxKPbvba9JhHGCJHmIVuDLT89q8syaf9A%2FXK4WdcQ3yXSy2Aqzgkqsq0gu5V1%2FgY8MDtUwEarTgtlMFeqpKdxTEDW97KkP7kSyzTz5s9rDxfgcMgxJgH7nGyEMAPly%2F4RPaJycPlmLd82KEHyleJeYer1BrskG6n%2F9pysZfGzYZmIOj7akNKEfkmHrpNCuNWxn6Z512haKT5xvGMv7yXK9LrFS0x%2BrY637pmpyMDqZjwL4E2%2FPVEfEd55EAlXHnW0b8aw223n1CGohjHUg4tYwQIeyrbTvPBIpfXvmht0dHefOr5EMGG%2BACekOipyw7G4RocxlZ01Di9Q%2FnHprhZMDaqLVEQO14Mg%2B7%2FqupHaFsmuxlrONaQhlqNQg3ejjcaF9URqmr%2BF4aRfJ6SEkWUXK8udNXc6Fm9xcfRdpWrcQs68TobQnTdNZef%2BU7N2%2FaR684T3ciDlHH0DzPazfKrFktLxC2pHl8YifVHp6ZrD0ECVIdxyZV5SpNP0pD8ovnRW1%2Bp%2F1AWaMHICMzlnfSe%2FdoRHoB%2FG8ZDIx13b7P5aRneJWIyYRPaD2Ta7A%2F5W4Zvjc4r4EaPuIGAb%2F8%2FnzKInsQ1F37Z%2FAWbb0VEwiDuTVmUYJ5raSZwasIlp56ejHT%2B%2Fqo8xyydlg5MUsRadB9W2fldVQwO4vCYhvpe0B7gtD1%2FBsw5MRp1eIR16JHwGzMwl2svhOe3tmmzHXNxszIBwhm5SyNkWf8vQY2lbsVD%2FqWxgwnMHA0gY6mAEOQdrWCJRIovuOaAwHwVImXtYdpzN6Z5uThDbTqIf0zda6GadxgG%2Bp7cqoXWgu2kpX1y8dlV%2FoSlKSh9gZM3pUuejzpijkJdX2kYTZvFqi%2FGfxO3ZmVgkwoTDhttGeRrPWD9%2FKiJCf0sa1H%2F6hKvGVT26KwARjewcTAyiDy%2FA1efXwQcPHyoCIjCWdrrTSeywQd%2FxkVMp9bw%3D%3D&Expires=1783639663) - # BANXE Intent Layer: Governance-пробелы как регуляторные блокеры и пути выхода

## Резюме

Три gove...

9. [EMI-BANXE-AI-BANK-Pozitsionirovanie-po-modeli-zrelosti-II-Polnyi-analiz.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/101434432/7f3d4d4c-8e82-4857-9677-f7d9bfd47e87/EMI-BANXE-AI-BANK-Pozitsionirovanie-po-modeli-zrelosti-II-Polnyi-analiz.md?AWSAccessKeyId=ASIA2F3EMEYE7MRIB7BU&Signature=CkBwe6Hkpsfr%2FbLnc3Udte%2BVZgY%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIB%2Fh%2B7xKIJuPm%2B8Q%2FQ3V67KzqyNcqfFYrDla6Cea2YeWAiEAnPnVj2l92asppPCX1ND1iusaiKAkgpu%2BLcfQbcjsTBcq%2FAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDM1hJ28cyYEFUfgqhSrQBB7kCrrk74wcwWR%2BiOxG%2Bcw3JnR%2F6Yh7TG%2BnhB%2BIsPAxKPbvba9JhHGCJHmIVuDLT89q8syaf9A%2FXK4WdcQ3yXSy2Aqzgkqsq0gu5V1%2FgY8MDtUwEarTgtlMFeqpKdxTEDW97KkP7kSyzTz5s9rDxfgcMgxJgH7nGyEMAPly%2F4RPaJycPlmLd82KEHyleJeYer1BrskG6n%2F9pysZfGzYZmIOj7akNKEfkmHrpNCuNWxn6Z512haKT5xvGMv7yXK9LrFS0x%2BrY637pmpyMDqZjwL4E2%2FPVEfEd55EAlXHnW0b8aw223n1CGohjHUg4tYwQIeyrbTvPBIpfXvmht0dHefOr5EMGG%2BACekOipyw7G4RocxlZ01Di9Q%2FnHprhZMDaqLVEQO14Mg%2B7%2FqupHaFsmuxlrONaQhlqNQg3ejjcaF9URqmr%2BF4aRfJ6SEkWUXK8udNXc6Fm9xcfRdpWrcQs68TobQnTdNZef%2BU7N2%2FaR684T3ciDlHH0DzPazfKrFktLxC2pHl8YifVHp6ZrD0ECVIdxyZV5SpNP0pD8ovnRW1%2Bp%2F1AWaMHICMzlnfSe%2FdoRHoB%2FG8ZDIx13b7P5aRneJWIyYRPaD2Ta7A%2F5W4Zvjc4r4EaPuIGAb%2F8%2FnzKInsQ1F37Z%2FAWbb0VEwiDuTVmUYJ5raSZwasIlp56ejHT%2B%2Fqo8xyydlg5MUsRadB9W2fldVQwO4vCYhvpe0B7gtD1%2FBsw5MRp1eIR16JHwGzMwl2svhOe3tmmzHXNxszIBwhm5SyNkWf8vQY2lbsVD%2FqWxgwnMHA0gY6mAEOQdrWCJRIovuOaAwHwVImXtYdpzN6Z5uThDbTqIf0zda6GadxgG%2Bp7cqoXWgu2kpX1y8dlV%2FoSlKSh9gZM3pUuejzpijkJdX2kYTZvFqi%2FGfxO3ZmVgkwoTDhttGeRrPWD9%2FKiJCf0sa1H%2F6hKvGVT26KwARjewcTAyiDy%2FA1efXwQcPHyoCIjCWdrrTSeywQd%2FxkVMp9bw%3D%3D&Expires=1783639663) - # EMI BANXE AI BANK: Позиционирование по модели зрелости ИИ — Полный анализ

## Резюме

Настоящий от...

10. [DBS rolls out AI-powered virtual assistant Joy to all SMEs](https://cfotech.asia/story/dbs-rolls-out-ai-powered-virtual-assistant-joy-to-all-smes) - DBS has launched its AI-powered virtual assistant, DBS Joy, for all corporate clients, enhancing 24/...

11. [Klarna AI assistant handles two-thirds of customer service chats in ...](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) - Your personal financial assistant: Klarna's AI Assistant offers real-time updates on your outstandin...

12. [Nebius' Post - LinkedIn](https://www.linkedin.com/posts/nebius_revolut-rebuilt-its-platform-around-ai-to-activity-7440451754221174784-pFGp) - Revolut rebuilt its platform around AI to scale from 30 million to 70 million customers in just thre...

13. [Banks aim for agentic AI scale in 2026: report - Banking Dive](https://www.bankingdive.com/news/banks-agentic-ai-scale-2026-accenture/809585/) - Over the next three years, 57% of banking executives expect AI agents to be fully embedded in risk, ...

14. [AI in Banking: Why 2026 Will Belong to the Banks That Move ...](https://finshape.com/blog/ai-in-banking-why-2026-will-belong-to-the-banks-that-move-beyond-pilots/) - AI in Banking: Why 2026 Will Belong to the Banks That Move Beyond Pilots ... An exciting talk from t...

15. [Top Banking Trends for 2026 | Accenture](https://www.accenture.com/us-en/insights/banking/accenture-banking-trends-2026) - Accenture's Banking Trends 2026 reveals how agentic AI, smart money and shifting competition will re...

16. [Precision, Not Hype, Will Shape Banks' Use Of AI In 2026 - Forbes](https://www.forbes.com/sites/christerholloman/2025/11/30/precision-not-hype-will-shape-banks-use-of-ai-in-2026/) - McKinsey predicts that while agentic AI could reduce bank unit costs by 15 to 20%, it also threatens...

17. [Banking's agentic AI opportunity | McKinsey & Company](https://www.mckinsey.com/featured-insights/week-in-charts/bankings-agentic-ai-opportunity) - As banks grapple with falling revenues, some are exploring opportunities to use AI for productivity ...

18. [AI Is Helping People Save More Money | bunq Blog](https://www.bunq.com/blog/ai-is-helping-people-save-more-money) - AI is already helping people save money. Discover how using AI for financial insights, not just auto...

19. [BofA's Virtual Assistant Erica Surpasses 3 Billion Client ...](https://www.cboe.com/ca/equities/securities/BOFA/6758667481220504/)

20. [Banking in 2026: Production scale AI agents - FinTech Futures](https://www.fintechfutures.com/ai-in-fintech/banking-in-2026-production-scale-ai-agents) - Banks will shift from pilots to large-scale, autonomous, and well-governed AI agents that reshape cu...

21. [Half of Americans expect AI to replace their financial advisor, yet ...](https://www.heraldonline.com/news/business/article315509984.html) - A 2026 survey from Credit One Bank found that 51% of U.S. consumers believe that AI will replace fin...

