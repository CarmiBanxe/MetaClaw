# EMI BANXE AI BANK: Новая концепция Intent-First Banking — Полная редакция

> **Основание для ревизии:** Исходная концепция устанавливала Intent-First как стратегический вектор проекта. Настоящая редакция интегрирует регуляторную механику: три governance-пробела являются не «техническим долгом», а **структурными правовыми блокерами** клиентского Intent Layer в условиях FCA 2026. Концепция пересобрана так, что каждый стратегический слой обеспечен конкретным регуляторным обоснованием и готовым техническим решением.

***

## Часть I. Тезис: что изменилось в индустрии и почему это касается BANXE

### Revolut AIR и сдвиг парадигмы

Revolut запустил AIR (AI by Revolut) в апреле 2026 года для ~13 миллионов пользователей в Великобритании. AIR — это не добавленная функция: он заменяет всю навигационную логику приложения. Вместо меню — намерение: «заблокируй карту», «отмени подписку», «переведи £500». Под капотом: 200+ GPU H100 через Nebius AI Cloud, ~1,2 млн обращений в поддержку ежемесячно с ~90% авторешением, нулевое хранение данных у внешних партнёров. Revolut называет это «новой эрой money intelligence».[^1][^2][^3][^4][^5]

Это не изолированный кейс. В апреле 2026 года Starling Bank запустил собственный agentic AI-ассистент на Google Gemini как «зонтик над всеми банковскими функциями». bunq Finn обрабатывает 97% обращений в поддержку автоматически за 47 секунд. Goldman Sachs и Anthropic выводят в production агентов для trade accounting и onboarding. The Asian Banker в мае 2026 прямо формулирует: «мобильные приложения с меню станут такими же устаревшими, как банковские отделения».[^6][^7][^8][^9]

### Тезис для BANXE

[ФАКТ] BANXE находится на ступени 11+/12 по модели зрелости ИИ — в top 1–5% глобально по данным McKinsey, при том что 80% компаний лишены ключевых governance-возможностей для agentic AI. [ВЫВОД] Это означает: у BANXE есть архитектурные prerequisites, которых нет у большинства конкурентов. Но они не конвертируются в продукт до закрытия регуляторных блокеров.[^10]

[ФАКТ] FCA в марте 2026 года впервые в истории назвал agentic AI payments **формальным регуляторным приоритетом** и заявил о возможном переписывании Payment Services Regulations 2017. [ФАКТ] IMF в апрельском рабочем документе формулирует корень проблемы: платёжные системы детерминированы по природе, agentic AI вероятностен — и без трёх governance-слоёв их примирить нельзя.[^11]

[ВЫВОД] Три governance-пробела проекта — cost-policy, Decision Lineage Schema, S13-00 — это не технический долг. Это структурный правовой барьер между текущим состоянием BANXE (ступень 11+) и клиентским Intent Layer. После их закрытия BANXE становится одним из немногих EMI-институтов в UK, архитектурно готовых к тому, что FCA сам ещё только готовится регулировать.[^11]

***

## Часть II. Регуляторный ландшафт 2026

### FCA: agentic AI payments как формальный приоритет

FCA Regulatory Priorities Report, 25 марта 2026 года: agentic AI payments впервые получили статус отдельного регуляторного приоритета. PSR 2017 не даёт ответа на четыре фундаментальных вопроса новой парадигмы:[^11]

- Кто несёт ответственность за fraud, совершённый агентом?
- Как Strong Customer Authentication (SCA) применяется к machine-initiated транзакциям?
- Защищает ли Consumer Duty автономные системы в той же мере, что и человека?
- Как работает авторизация при многоуровневом делегировании?

FCA позиция: *«Инновации поощряются, но accountability за outcomes не снимается»*. Consumer Duty требует ongoing assessment — не разовой проверки, а постоянной.[^11]

### SM&CR: персональная ответственность за AI-решения

Реформа Senior Managers & Certification Regime (SM&CR), вступившая в силу 24 апреля 2026 года, сохраняет ключевой принцип: **персональная подотчётность старших менеджеров** за AI-решения, принятые под их надзором. [ФАКТ] Отсутствие Decision Lineage Schema означает: при инциденте с агентным платежом SMF-holder не может доказать, что знал о рисках и принял адекватные меры.[^11]

### Safeguarding Supplementary Regime (7 мая 2026)

Новый FCA safeguarding режим (PS25/12) требует ежедневных reconciliations клиентских средств. [ФАКТ] Применительно к Intent Layer: каждая транзакция, инициированная агентом от имени клиента, должна быть верифицируемо связана с авторизованным поручением клиента. Без этого — потенциально unsegregated клиентские средства. EMI-фирмы защищали ~£26 млрд в 2024 году.[^10][^11]

### Consumer Trust Gap: 71%

[ФАКТ] 71% потребителей не доверяют AI-агентам управление платежами без явного механизма reversibility и accountability. Checkout.com называет обратимость «самым важным единственным инфраструктурным элементом для доверия потребителей». Intent Layer без governance-фреймворка — это продукт, которому не доверяют, даже если регулятор молчит.[^11]

***

## Часть III. Определение Intent Layer и механика блокировки

### Что такое Intent Layer

Intent Layer — это архитектурный слой, в котором клиентский запрос на естественном языке («переведи £500 моему арендодателю каждое 1-е число») преобразуется в **делегированное поручение агенту** с явно зафиксированными параметрами: кто поручает, что именно, в каких границах, при каких условиях отмены, с каким уровнем автономии.[^11]

FCA в апреле 2026 года описал именно это: *«Вместо нажатия 'купить' мы будем кодировать наши предпочтения, разрешения и ограничения — позволяя интеллектуальным системам совершать транзакции от нашего имени, внутри guardrails»*. Intent Layer — не одиночное действие, а структурированное намерение с границами.[^11]

### Три уровня блокировки

**Уровень 1 — Cost-Policy: блокер финансовой безопасности**

Когда клиент делегирует агенту автономию на платежи, агент работает в рамках явного финансового мандата. Без per-agent cost-cap невозможно создать клиентскую политику делегирования вида «агент работает в пределах £X в период Y с автоматическим стоп-сигналом». Документально зафиксированный кейс индустрии: $30K за 6 часов из-за looping agent. Применительно к клиентским средствам — прямое нарушение PS25/12. [ФАКТ] Текущий LiteLLM rate-limiting не заменяет финансовую policy: это ограничение пропускной способности, а не финансового мандата.[^10][^11]

**Уровень 2 — Decision Lineage: блокер юридической подотчётности**

PSR 2017 не создан для ответа на вопрос: кто отвечает за ошибочную транзакцию агента? Агент — не юридическое лицо. Без полной цепочки reasoning FCA не может провести supervisory examination. Decision Lineage — единственный механизм, позволяющий EMI-институту доказать: агент действовал строго в рамках делегированного мандата клиента. [ФАКТ] Разница критична: audit log отвечает на «что?», Decision Lineage — на «почему?».[^11]

**Уровень 3 — S13-00: блокер детерминизма**

[ФАКТ] IMF: платёжные системы требуют детерминированности, agentic AI по природе вероятностен. Без Business Process Repository агент использует LLM-reasoning для принятия платёжных решений — вероятностный процесс: два одинаковых запроса могут дать разные outcomes. Регуляторно — неприемлемо для EMI. С Business Process Repository агент становится **rule-bound interpreter**: LLM используется только для интерпретации intent, само решение принимается по детерминированным бизнес-правилам.[^11]

***

## Часть IV. Новая концепция: четыре слоя BANXE Intent-First Stack

### Принцип сборки

Четыре слоя выстраиваются в единую архитектуру, где каждый вышестоящий слой опирается на нижестоящий. Три governance-пробела — это блокеры **Execution Layer**: без их закрытия клиентские запросы не могут безопасно достигать агентов.

```
┌─────────────────────────────────────────────────────┐
│              INTENT LAYER (клиентский)               │
│  Natural language → Intent Record + SCA consent      │
├─────────────────────────────────────────────────────┤
│             EXECUTION LAYER (агентный)               │
│  10 агентов → payments / kyc / compliance / cards    │
│  БЛОКЕР: cost-policy + Decision Lineage + S13-00     │
├─────────────────────────────────────────────────────┤
│          GOVERNANCE & COMPLIANCE LAYER               │
│  FCA audit trail | HITL | ClickHouse | SM&CR         │
├─────────────────────────────────────────────────────┤
│           DATA & INTELLIGENCE LAYER                  │
│  RAG | AML/SDN | Behavioral analytics | S13-00 BPR  │
└─────────────────────────────────────────────────────┘
```

### Слой 1 — Intent Layer (клиентский интерфейс)

**Определение:** единственный первичный клиентский интерфейс. Не вкладки, не формы, не меню — разговор с AI-агентом. Визуальные компоненты (карточки, графики, формы подтверждения) рендерятся агентом контекстно как **ответ на намерение**, а не как постоянный UI.

**Мировые подтверждения:** Revolut AIR, Starling Assistant, bunq Finn — все три лидера 2026 года строят именно эту модель.[^12][^7][^6]

**Задача для BANXE:** проектировать клиентский UI изначально как chat-first — чат является главным экраном, традиционные UI-компоненты вызываются агентом. Это не переосмысление продукта, это **правильная первоначальная постановка задачи на UX**.

**Технический anchor:** `ClientIntentRecord` — структурированный мандат делегирования:[^11]

```python
@dataclass
class ClientIntentRecord:
    intent_id: str           # UUID
    client_id: str
    intent_type: str         # 'recurring_payment' | 'conditional_transfer' | 'alert_only'
    natural_language: str    # оригинальный запрос клиента
    parsed_params: dict      # amount, recipient, conditions, frequency
    consent_timestamp: datetime
    consent_method: str      # 'explicit_confirm' | 'biometric' | 'pin'
    scope_limits: dict       # max_amount, allowed_recipients, time_window
    revocation_method: str   # как клиент может отменить
    expires_at: Optional[datetime]
    linked_agent_id: str     # какой агент исполняет
    linked_budget_policy_id: str  # ссылка на agent-budget-policy
```

**SCA-совместимость:** до принятия новых PSR для agentic AI BANXE применяет SCA при **создании** Intent Record (первичное согласие), а не при каждом исполнении агентом. Это паттерн «consent-at-delegation», совместимый с существующими PSR 2017.[^11]

### Слой 2 — Execution Layer (агентная фабрика)

**Определение:** набор специализированных агентов, реализующих банковские домены. Каждый агент действует **автономно в пределах guardrails**, выполняя операции напрямую, а не «предлагая их выполнить».

**Текущее состояние BANXE:** MetaClaw, 10 HITL-агентов, compliance-api, batch-agent — это уже реализованная часть. [ВЫВОД] Задача — **экспортировать агентов на клиентский уровень**: сейчас они работают внутри production-процессов, следующий шаг — те же агенты, вызываемые через Intent Layer.[^10]

**Клиентские маски агентов:** для каждого из 10 агентов определяются:
- **scope** — что умеет делать по клиентскому запросу
- **limits** — guardrails из cost-policy (уровень 1 блокировки)
- **confirmation_policy** — когда требуется HITL (биометрия, крупная сумма, новый получатель)
- **audit_schema** — Decision Lineage Record (уровень 2 блокировки)
- **rule_source** — Business Process Repository (уровень 3 блокировки)

**Мировой контекст:** JPMorgan строит модель «20 AI-агентов под надзором 1 человека». Goldman Sachs в production: каждое агентное действие логируется в immutable storage с metadata. McKinsey: наиболее вероятный сценарий — 15–20% снижение затрат при агентизации.[^8][^13][^14]

### Слой 3 — Governance & Compliance Layer (регуляторный каркас)

**Определение:** система guardrails, HITL, audit trail, Decision Lineage, cost-caps — всё, что делает агентную автономию **аудируемой в рамках FCA EMI-лицензии**.

**Текущее состояние BANXE:** HITL-архитектура с 10 агентами, ClickHouse FCA audit trail, BufferedAuditPort, 5842 CI/CD-тестов — это уже **архитектурная норма**, которой лишены 80% компаний глобально.[^10]

**Что нужно добавить (три пробела = три ADR):**

| Пробел | Что добавить | Регуляторный риск без него |
|---|---|---|
| **Cost-Policy** | agent-budget-policy.md + LiteLLM BudgetManager config | Safeguarding breach PS25/12 |
| **Decision Lineage** | AgentDecisionRecord ClickHouse schema + agent wrapper | SM&CR personal liability |
| **S13-00** | Business Process Repository + ArchiMate import | IMF determinism / IMF PSR compliance |

**[ФАКТ] Deloitte State of AI 2026:** 80% организаций лишены ключевых governance-возможностей для agentic AI: чётких границ агентов, realtime-мониторинга, audit trails. BANXE с готовым HITL и ClickHouse уже в top 20% — три пробела переводят его в top 1%.[^10]

### Слой 4 — Data & Intelligence Layer (источник правды)

**Определение:** единый источник верифицированных данных о клиенте, финансовой истории, AML/KYC-статусе — доступный всем агентам в real-time.

**Текущее состояние BANXE:** RAG с SDN mapping, compliance docs, PEP/Sanctions/AML training, banxe-lexisnexis-distro.[^10]

**Расширение для Intent Layer:**
- **Behavioral analytics** — персонализированный контекст: паттерны расходов, типичные суммы, привычные получатели → агент понимает «нормальное» поведение клиента
- **Risk scoring в реальном времени** — вероятность fraud/AML до исполнения транзакции, а не после
- **S13-00 Business Process Repository** — детерминированные правила как foundation: агент не рассуждает о том, что можно делать — он знает это из репозитория

**Revolut принцип:** «только данные, которые клиент уже видит в приложении — zero 3rd-party storage». BANXE on-premises модель напрямую соответствует этому — и это должно быть явным продуктовым тезисом: **data sovereignty как trust premium**.[^2]

***

## Часть V. Четыре конкретных решения для снятия блокеров

### Решение 1: AI Agent Budget Policy (S9 — критический)

**Что отсутствует технически:** LiteLLM rate-limits есть (ограничение пропускной способности), но нет **per-agent financial mandate** — формализованного документа с явными границами для каждого из 10 агентов.[^11]

**Конфигурация LiteLLM BudgetManager** (в существующем стеке, требует параметризации):[^11]

```python
budget_manager.create_budget(
    agent_id="banxe_compliance_agent",
    max_tokens_per_task=50_000,
    max_cost_per_job=0.50,      # USD
    retry_ceiling=3,
    halt_on_exceed=True,
    escalation_path="human_review_queue"
)
```

**Артефакты S9:**
- `agent-budget-policy.md` в banxe-architecture (таблица всех 10 агентов: agent_id → max_tokens → max_cost_per_job → retry_ceiling → halt_condition → escalation_path)
- IL-entry в INSTRUCTION-LEDGER
- ADR-037
- OpenTelemetry token-tracing → существующий Prometheus/Grafana стек

**Регуляторный риск без него:** safeguarding breach по PS25/12 (7 мая 2026) — агент может инициировать неавторизованные операции с клиентскими средствами без верифицируемого финансового мандата.

### Решение 2: Decision Lineage Schema (S9–S10 — критический)

**Что отсутствует технически:** ClickHouse фиксирует *что произошло*, но не *почему* — нет полной цепочки `triggering_event → context_assembled → policies_evaluated → reasoning_process → authority_verification → outcome`.[^11]

**ClickHouse schema для AgentDecisionRecord**:[^11]

```sql
CREATE TABLE agent_decision_records (
    decision_id         UUID DEFAULT generateUUIDv4(),
    agent_id            LowCardinality(String),
    task_id             String,
    client_id           Nullable(String),
    triggered_by        String,         -- 'client_intent' | 'scheduler' | 'system'
    intent_id           Nullable(String), -- ссылка на ClientIntentRecord
    context_sources     Array(String),  -- источники, которые агент собрал
    policies_evaluated  Array(String),  -- бизнес-правила из S13-00 BPR
    reasoning_summary   String,         -- chain-of-thought (truncated)
    confidence_score    Float32,
    action_taken        String,
    action_params       String,         -- JSON
    human_reviewed_by   Nullable(String),
    human_override      UInt8 DEFAULT 0,
    halt_triggered      UInt8 DEFAULT 0,
    halt_reason         Nullable(String),
    outcome             LowCardinality(String), -- 'completed'|'escalated'|'halted'
    created_at          DateTime64(3) DEFAULT now64()
) ENGINE = MergeTree()
ORDER BY (agent_id, created_at)
TTL created_at + INTERVAL 7 YEAR; -- FCA retention: 5 лет + buffer
```

**Ключевой архитектурный принцип:** `reasoning_summary` пишется агентом **в процессе работы**, а не реконструируется из логов после. Каждый HITL-агент получает обёртку, автоматически пишущую Decision Record в ClickHouse перед исполнением action.[^11]

**Регуляторный риск без него:** SM&CR personal liability — при инциденте с агентным платежом SMF-holder не может доказать осведомлённость о рисках; FCA supervisory examination не может быть проведён.

### Решение 3: Intent Capture Layer (S10)

**Компоненты:**
1. `ClientIntentRecord` dataclass (схема в Части IV, Слой 1)
2. SCA hook при создании записи (consent-at-delegation паттерн)
3. Mapping: intent_id → agent_id → budget_policy_id → decision_lineage_record
4. Revocation API (клиент отменяет мандат в любой момент — FCA Consumer Duty reversibility)

**SCA-совместимость:** до новых PSR для agentic AI — SCA при создании Intent Record, не при каждом исполнении. Паттерн «consent-at-delegation».[^11]

**Регуляторный риск без него:** Consumer Duty transparency — невозможно доказать, что клиент сознательно делегировал конкретный тип агентной автономии.

### Решение 4: S13-00 Business Process Repository (S11)

**Архитектурный паттерн**:[^11]

Агент без BPR: `клиентский запрос → LLM reasoning → действие` (вероятностно)

Агент с BPR: `клиентский запрос → Intent Record → BPR lookup → детерминированное правило → LLM только для разрешения неоднозначностей → действие → Decision Lineage: rule_applied: [BP-042]`

Это превращает агента из probabilistic actor в **rule-bound interpreter** — именно то, чего ожидают FCA и IMF от agentic payment systems.[^11]

**Артефакты S11:**
- `banxe-business-processes` как живой репозиторий
- ArchiMate-import из существующей документации
- Нотация, машинно-читаемая агентами (JSON/YAML rule sets)
- Версионирование через Git (изменение правила = ADR + review)

***

## Часть VI. Полная схема Intent Layer: от client consent до FCA audit trail

Когда все три пробела закрыты, Intent Layer образует единый верифицируемый поток:[^11]

```
КЛИЕНТ ФОРМУЛИРУЕТ НАМЕРЕНИЕ (natural language)
             ↓
  INTENT CAPTURE LAYER
  → Парсинг intent (LLM)
  → Создание ClientIntentRecord
  → SCA-аутентификация (biometric / PIN)
  → Запись согласия: consent_timestamp, consent_method, scope_limits
             ↓
  BUSINESS PROCESS REPOSITORY (S13-00)
  → Matching rule для типа intent (BP-042: recurring_payment_under_£1000)
  → Детерминированные параметры исполнения
             ↓
  AGENT BUDGET POLICY CHECK
  → Задача в пределах financial mandate агента?
  → LiteLLM BudgetManager: cost_check → GO / BudgetExceededError → HALT
             ↓
  AGENT ИСПОЛНЯЕТ ПО ДЕТЕРМИНИРОВАННОМУ ПРАВИЛУ
  → compliance-agent: real-time AML/sanction check
  → payments-agent: исполнение транзакции
             ↓
  DECISION LINEAGE RECORD → ClickHouse (реальное время)
  triggered_by: client_intent_id
  intent_id: linked ClientIntentRecord
  policies_evaluated: [BP-042, AML-check-001]
  reasoning_summary: "..."
  action_taken: "SEPA transfer £X to recipient Y"
  outcome: "completed"
             ↓
  РЕЗУЛЬТАТ → КЛИЕНТ (подтверждение + revocation option)
  РЕЗУЛЬТАТ → HITL oversight queue (если confidence_score < threshold)
             ↓
  FCA AUDIT TRAIL: полная цепочка от consent до outcome
  (satisfies: Consumer Duty, SM&CR, PS25/12 safeguarding, FCA supervisory examination)
```

***

## Часть VII. Конкурентная позиция: почему именно сейчас

### Матрица позиционирования

| Параметр | Revolut AIR | Starling | bunq Finn | BANXE (post-gap closure) |
|---|---|---|---|---|
| Intent-First UX | ✅ retrofitted | ✅ | ✅ | ✅ native (строится) |
| On-premises AI | ✅ Nebius | ❌ GCP | Частично | ✅ Legion/evo1/evo2 |
| Data sovereignty | ✅ zero 3rd-party | В GCP | Частично | ✅ on-prem |
| Decision Lineage | [НЕИЗВЕСТНО] | [НЕИЗВЕСТНО] | [НЕИЗВЕСТНО] | ✅ (ADR-037) |
| Agent cost governance | [НЕИЗВЕСТНО] | [НЕИЗВЕСТНО] | [НЕИЗВЕСТНО] | ✅ (agent-budget-policy) |
| FCA-native governance | [НЕИЗВЕСТНО] | Частично | Частично | ✅ (архитектурно) |
| Client-facing agents | ✅ production | ✅ beta | ✅ production | ⚠️→✅ (S10) |

[ВЫВОД] Конкуренты запускают Intent Layer быстрее, но без верифицируемой governance-инфраструктуры. У BANXE обратная задача: governance строится как часть архитектуры, Intent Layer активируется после его закрытия. Это ставит BANXE в позицию **compliance-native первопроходца** в UK EMI-пространстве — именно тогда, когда FCA формализует требования к agentic AI.[^11]

### Ключевые цифры отрасли

- **57%** топ-менеджеров банков ожидают полного встраивания AI-агентов в ключевые функции за 3 года[^15]
- **40%** снижение затрат при полной агентизации — McKinsey best-case[^14]
- **51%** потребителей США считают, что AI заменит финансовых советников в течение 10 лет[^16]
- **60%** доверяют AI-советам больше, если они исходят от их банка[^16]
- **71%** не доверяют агентам без явного механизма reversibility[^11]

Цифра 71% — это не барьер для BANXE, это **продуктовый аргумент**: Intent Layer с `revocation_method` в каждом IntentRecord закрывает именно этот trust gap.

***

## Часть VIII. Приоритизация по спринтам: регуляторные блокеры → deliverables

| Sprint | Действие | Артефакт | Регуляторный риск без него |
|---|---|---|---|
| **S9** | agent-budget-policy.md + LiteLLM BudgetManager config + ADR-037 | policy doc, IL-entry | Safeguarding breach (PS25/12) — клиентские средства |
| **S9** | AgentDecisionRecord ClickHouse schema + agent wrapper | ADR-037 migration, schema | SM&CR personal liability — нет доказательства надзора |
| **S10** | ClientIntentRecord dataclass + SCA hook + revocation API | Intent Capture Layer v1 | Consumer Duty transparency — нет верифицируемого consent |
| **S10** | Production cutover + Intent Layer pilot (subset клиентов) | CI report, REP027-prep | FCA supervisory examination readiness |
| **S11** | S13-00: Business Process Repository + ArchiMate import | banxe-business-processes | IMF determinism — вероятностные решения в платёжной системе |
| **Ongoing** | Monthly drift review production-агентов | Grafana dashboard, IL-entry | Consumer Duty ongoing assessment |

### Принцип порядка из модели зрелости

[ФАКТ] Статья Льва Омельницкого формулирует: *«сначала качество, потом стабильность, потом стоимость»*. Применительно к Intent Layer:[^10]

1. **Decision Lineage** (S9) = качество: каждое решение верифицируемо, FCA может его проверить
2. **Cost-Policy** (S9) = стабильность: агент не выходит за рамки финансового мандата
3. **Business Process Repository** (S11) = стоимость масштабирования: детерминированные правила дешевле LLM-рассуждений на каждый платёж

***

## Часть IX. Итоговое позиционирование

### Формула проекта

**BANXE — первый EMI-банк в UK с Intent-First архитектурой и compliance-native governance.** Клиент не навигирует приложение — он общается с AI-агентом, который выполняет операции в рамках верифицируемого мандата делегирования, с полной цепочкой обоснования каждого решения и детерминированной бизнес-логикой как основой агентных действий.

В отличие от крупных игроков, retrofitting AI поверх legacy, BANXE строит этот стек нативно. В отличие от конкурентов, запускающих Intent Layer без governance, BANXE запускает его с FCA-аудируемой архитектурой.

### Три дифференцирующих тезиса

1. **«AI-агент вместо приложения»** — клиентский интерфейс это разговор о намерении, а не навигация по меню. Это уже операционная норма у Revolut, Starling, bunq — BANXE строит это с нуля, нативно.[^7][^12][^6]

2. **«Compliance by design, not by audit»** — каждое агентное действие генерирует Decision Lineage Record в реальном времени. HITL и ClickHouse audit trail не ограничения — это конкурентные активы в регуляторном 2026 году.[^10][^11]

3. **«Data sovereignty = trust premium»** — zero 3rd-party storage + on-premises AI = единственный тип AI-банка, которому 60% пользователей доверяют больше, чем стороннему чат-боту. 71% потребителей требуют reversibility — `revocation_method` в каждом IntentRecord закрывает этот gap прямо.[^16][^11]

### Корректировка постановки задачи проекта

**Задача-1 (UX):** проектировать клиентский UI как **chat-first**: чат — главный экран, UI-компоненты рендерятся агентом контекстно в ответ на намерение. Не добавлять чат к традиционному банковскому приложению.

**Задача-2 (агенты):** определить клиентские маски для каждого из 10 агентов (scope, limits, confirmation_policy, audit_schema, rule_source). Это превращает внутренние production-агенты в client-facing агентную фабрику.

**Задача-3 (governance — блокер):** ADR-037 = cost-policy + Decision Lineage Schema. До production cutover. Это не опциональный deliverable — это условие безопасного запуска клиентского Intent Layer в рамках FCA PS25/12 и SM&CR.

**Задача-4 (compliance):** compliance-agent становится **real-time overlay** поверх каждого клиентского агентного действия, а не batch-процессом. Результат AML/sanction check — часть Decision Lineage Record.

**Задача-5 (data):** расширить RAG до клиентского Data Intelligence уровня: spending profile, risk score, behavioral analytics. S13-00 Business Process Repository — foundation для детерминированного слоя Data & Intelligence.

---

## References

1. [Revolut Launches AIR, Its First AI Financial Assistant - Trending Topics](https://www.trendingtopics.eu/revolut-launches-air-its-first-ai-financial-assistant/) - The chatbot, integrated directly into the app, is designed to help users manage their finances more ...

2. [Revolut Launches AIR, An In-App AI Assistant, to 13 Million UK ...](https://www.fintechweekly.com/news/revolut-air-ai-assistant-uk-customers-launch-2026) - Revolut began rolling out an in-app AI assistant to its 13 million UK customers on 9 April 2026. The...

3. [Nebius' Post - LinkedIn](https://www.linkedin.com/posts/nebius_revolut-rebuilt-its-platform-around-ai-to-activity-7440451754221174784-pFGp) - Revolut rebuilt its platform around AI to scale from 30 million to 70 million customers in just thre...

4. [Revolut on the Inference Frontier - Nebius](https://nebius.com/customer-stories/revolut) - Across workloads, Revolut now runs training and inference on more than 200 NVIDIA H100 GPUs through ...

5. [Revolut enters new era of money intelligence with launch of AI ...](https://www.revolut.com/news/revolut_enters_new_era_of_money_intelligence_with_launch_of_ai_assistant/) - Revolut, the UK licenced bank, today announced the launch of AIR (AI by Revolut), a sophisticated in...

6. [Starling launches an AI banking assistant that actually does things](https://thenextweb.com/news/starling-assistant-agentic-ai-financial-assistant-uk) - Starling Assistant is designed to act, to take a voice or natural language prompt, and execute banki...

7. [bunq launches smarter, more powerful upgrade to GenAI financial ...](https://press.bunq.com/258930-bunq-launches-smarter-more-powerful-upgrade-to-genai-financial-assistant/) - bunq, Europe's second-largest neobank, has released a new upgraded version of Finn, bunq users' GenA...

8. [Goldman Sachs Advances AI Banking Agents - AI CERTs News](https://www.aicerts.ai/news/goldman-sachs-advances-ai-banking-agents/) - Jun 23, 2025: Expansion memo cites role-tailored functions. Feb 6, 2026: CIO Argenti announces auton...

9. [AI agents set to replace mobile banking apps - The Asian Banker](https://www.theasianbanker.com/updates-and-articles/ai-agents-set-to-replace-mobile-banking-apps) - Artificial intelligence (AI) could soon make mobile apps as outdated as bank branches after the firs...

10. [EMI-BANXE-AI-BANK-Pozitsionirovanie-po-modeli-zrelosti-II-Polnyi-analiz.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/101434432/7f3d4d4c-8e82-4857-9677-f7d9bfd47e87/EMI-BANXE-AI-BANK-Pozitsionirovanie-po-modeli-zrelosti-II-Polnyi-analiz.md?AWSAccessKeyId=ASIA2F3EMEYEVUAS6YK4&Signature=4xtA2kTvM%2FghHOPx9jIAIM5ik4Q%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIBumBnVqFy3%2FCP6PjAItmT0xG5IcVz3pJ6CeVCBf%2F%2FtHAiALeh9Jzqjwr0dzZFtHJ8WIQhVc%2BOsezWH44WkBpdEQgir8BAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMTau72VTIQ4TUjxOpKtAEPJLIW0xXgoOv1e%2BE8dOBkv4i%2Fq%2BgDEKhKNJozXQ7SLN4f%2B97Thkr7P%2FCVcOwOxswdhaJS2mbBWq0rR06wxOSb1fBQB7Iq9x7P%2F%2FPIa9d2KhnqYrOoqWwrweqVl7vsRmCaay0t%2FGKNtNTo%2FfsuzADt%2Bq0AYmC2dGz8a%2FpjyKgqp%2FkVWMiG0qfTPt18XhedgLTpHl7qpSexLbUnBxohw4x1QzMmIATee89NafJ7dWUX7rQvg117SZ9c3SwWrWy2wZtxMDw2zCf7HbN6DY%2F%2BORzf%2BG45gvLO7eMf7xC%2B7sfpjHccSPL8Z%2FA0lFGGzhmfRTXLwxcXvsb%2FuTp1JUx18ZdyWRWcc11lc4qx18CPoR8R8EZZGqQBIbjnllWFKPPnJEiAA3CX5IwAWaf6YABmyMmdzovYlmdFroA1W2MfG2qWJTMw1tXucXF4tG%2BrYd2mGzJeqFpfl4sVJS9O5SIyMkEUaoR6ZbHae%2FbCtwZ7fUwSOMldLb96f2QEqMi7y6HLpaElABGUZV9B%2FQ0l8vG5fJY3%2FLE6W9Zi1YLKiKZQy3XQraoBbj0H8Xw6cMVnGuT0nsD4hCBlrAeqlKDTx1zUogskn4xf5B09i8KJfcB0RHaSUFlVYudZd%2FUznXaa8GqsBwIhNnFc7NzMql5HqM8VkRqpocsClpF%2BNlm3liFMTIuYgfuJht47eWcBSajTgk3J3VbvPqvR84%2F1%2FlFFN2xQjo2FtVVWqxR0SbCKMw0mK3mMjTAVPvz8Z5exg47TKm3laU0N5th2fGItxy8pNo5S%2Fps%2BzC2wMDSBjqZAUyrL%2BLP8t8Pzf1YMS%2Fmgv6MkR8dFh5PQTVA0RJbgMA5qH456vC2oWP7k5pFt6Gbtq03KMwbPksisTZsTm8%2BSgwxBnEectgiihWeVgar3W9WrafrHBqxKI2lYB%2BbKOUesZ0WBE3Ylj1w%2BXwkyFY9ADKgmOy5NWuY1x6A1wAzQskcFNfHpR%2BgVMitDHpeJoCp%2FakkxkUcdkXf2Q%3D%3D&Expires=1783639561) - # EMI BANXE AI BANK: Позиционирование по модели зрелости ИИ — Полный анализ

## Резюме

Настоящий от...

11. [BANXE-Intent-Layer-Governance-probely-kak-reguliatornye-blokery-i-puti-vykhoda.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/101434432/4e9869a1-2ccf-46bb-8b4b-64e63501c717/BANXE-Intent-Layer-Governance-probely-kak-reguliatornye-blokery-i-puti-vykhoda.md?AWSAccessKeyId=ASIA2F3EMEYEVUAS6YK4&Signature=P%2Bvyr3OunkV3J1P%2FTXQZqDHx17c%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIBumBnVqFy3%2FCP6PjAItmT0xG5IcVz3pJ6CeVCBf%2F%2FtHAiALeh9Jzqjwr0dzZFtHJ8WIQhVc%2BOsezWH44WkBpdEQgir8BAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMTau72VTIQ4TUjxOpKtAEPJLIW0xXgoOv1e%2BE8dOBkv4i%2Fq%2BgDEKhKNJozXQ7SLN4f%2B97Thkr7P%2FCVcOwOxswdhaJS2mbBWq0rR06wxOSb1fBQB7Iq9x7P%2F%2FPIa9d2KhnqYrOoqWwrweqVl7vsRmCaay0t%2FGKNtNTo%2FfsuzADt%2Bq0AYmC2dGz8a%2FpjyKgqp%2FkVWMiG0qfTPt18XhedgLTpHl7qpSexLbUnBxohw4x1QzMmIATee89NafJ7dWUX7rQvg117SZ9c3SwWrWy2wZtxMDw2zCf7HbN6DY%2F%2BORzf%2BG45gvLO7eMf7xC%2B7sfpjHccSPL8Z%2FA0lFGGzhmfRTXLwxcXvsb%2FuTp1JUx18ZdyWRWcc11lc4qx18CPoR8R8EZZGqQBIbjnllWFKPPnJEiAA3CX5IwAWaf6YABmyMmdzovYlmdFroA1W2MfG2qWJTMw1tXucXF4tG%2BrYd2mGzJeqFpfl4sVJS9O5SIyMkEUaoR6ZbHae%2FbCtwZ7fUwSOMldLb96f2QEqMi7y6HLpaElABGUZV9B%2FQ0l8vG5fJY3%2FLE6W9Zi1YLKiKZQy3XQraoBbj0H8Xw6cMVnGuT0nsD4hCBlrAeqlKDTx1zUogskn4xf5B09i8KJfcB0RHaSUFlVYudZd%2FUznXaa8GqsBwIhNnFc7NzMql5HqM8VkRqpocsClpF%2BNlm3liFMTIuYgfuJht47eWcBSajTgk3J3VbvPqvR84%2F1%2FlFFN2xQjo2FtVVWqxR0SbCKMw0mK3mMjTAVPvz8Z5exg47TKm3laU0N5th2fGItxy8pNo5S%2Fps%2BzC2wMDSBjqZAUyrL%2BLP8t8Pzf1YMS%2Fmgv6MkR8dFh5PQTVA0RJbgMA5qH456vC2oWP7k5pFt6Gbtq03KMwbPksisTZsTm8%2BSgwxBnEectgiihWeVgar3W9WrafrHBqxKI2lYB%2BbKOUesZ0WBE3Ylj1w%2BXwkyFY9ADKgmOy5NWuY1x6A1wAzQskcFNfHpR%2BgVMitDHpeJoCp%2FakkxkUcdkXf2Q%3D%3D&Expires=1783639561) - # BANXE Intent Layer: Governance-пробелы как регуляторные блокеры и пути выхода

## Резюме

Три gove...

12. [JUST IN: Revolut introduced AIR (AI by Revolut). A financial ...](https://www.linkedin.com/posts/marcelvanoost_%F0%9D%97%9D%F0%9D%97%A8%F0%9D%97%A6%F0%9D%97%A7-%F0%9D%97%9C%F0%9D%97%A1revolutintroduced-%F0%9D%97%94%F0%9D%97%9C%F0%9D%97%A5-activity-7447914551758753793-_TRt) - Having the assistant handle things like eSIMs and travel insurance through the same interface as car...

13. [AI adoption will trim banking industry costs by up to 20%](https://finance.yahoo.com/news/ai-adoption-trim-banking-industry-070000966.html) - AI is expected to drive up to 20% in net cost reductions for banks as the technology is implemented ...

14. [Banking's agentic AI opportunity | McKinsey & Company](https://www.mckinsey.com/featured-insights/week-in-charts/bankings-agentic-ai-opportunity) - As banks grapple with falling revenues, some are exploring opportunities to use AI for productivity ...

15. [Banks aim for agentic AI scale in 2026: report - Banking Dive](https://www.bankingdive.com/news/banks-agentic-ai-scale-2026-accenture/809585/) - Over the next three years, 57% of banking executives expect AI agents to be fully embedded in risk, ...

16. [Half of Americans expect AI to replace their financial advisor, yet ...](https://www.heraldonline.com/news/business/article315509984.html) - A 2026 survey from Credit One Bank found that 51% of U.S. consumers believe that AI will replace fin...

