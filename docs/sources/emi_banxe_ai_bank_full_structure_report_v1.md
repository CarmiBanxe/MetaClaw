# EMI BANXE AI BANK — полный подробный отчёт по структуре банка и ORG-CODE-RECONCILIATION v1

Статус документа: draft for operator review. Этот документ предназначен как полный подробный расклад по структуре проекта EMI BANXE AI BANK простым, понятным академическим языком. Он опирается на материалы текущей сессии, ранее собранный черновик canonical org-chart и приложённые рабочие следы по архитектуре, сервисной карте, agent passports, swarms, reconciliation и SP-RECON/SP-THIN контексту.[cite:29][cite:31]

## 1. Назначение документа

Цель этого отчёта — не просто перечислить отделы и роли, а собрать в одном месте целостную картину банка как системы. В документе описаны: текущее положение дел по проекту, уже реализованные архитектурные и организационные блоки, предполагаемая полная структура банка, AI-сотрудники и их функции, люди-дублёры, вертикальные и горизонтальные связи, а также разрез ORG-CODE-RECONCILIATION до уровня доменных сервисов.[cite:29][cite:31]

Под ORG-CODE-RECONCILIATION здесь понимается сопоставление между тремя слоями: 1) организационной моделью банка, 2) AI-агентами и governance-документами, 3) физически существующими runtime-сервисами и сервисными директориями в `banxe-emi-stack` и смежных контурах.[cite:29]

Это важно потому, что проект уже вышел из стадии «просто идеи AI-банка». В нём уже есть реальные сервисы, реальные паспорта агентов, реальные orchestration-контура и реальные HITL-гейты, но они пока не полностью сведены в один понятный внутренний операционный устав банка.[cite:29]

## 2. Текущее положение дел по проекту

По материалам этой сессии и приложенного архива подтверждается, что проект EMI BANXE AI BANK уже имеет развитый архитектурный фундамент. В нём присутствуют governance-документы `SERVICE-MAP`, `COMPLIANCE-ARCH`, `AGENT-ORG-STRUCTURE`, `HITL-MATRIX`, `RELATIONSHIP-TREE`, instruction-ledger шардирование и целый набор `agent passports`, `agent souls` и `agent swarms`.[cite:29]

Технический фундамент тоже уже заметен. В сервисной карте упоминаются реальные инфраструктурные и runtime-компоненты: `Midaz Ledger`, `Hyperswitch`, `Jube`, `Marble`, `Watchman`, `ClickHouse`, `PostgreSQL`, `Redis`, `OpenClaw`, `LiteLLM`, `Ollama`, `MetaClaw`, `Ruflo`, `Presidio`, `OpenMetadata`, `dbt`, `WeasyPrint`, `Great Expectations` и другие элементы.[cite:29]

Это означает, что банк проектируется как многослойная система, где AI-агенты не висят в воздухе, а опираются на реальные доменные сервисы, очереди, базы данных, отчётные пайплайны, screening-движки, ledger-инфраструктуру и контрольные workflow.[cite:29]

### 2.1. Статус SP-RECON и roadmap

Из рабочей сессии подтверждено, что блок `SP-RECON` уже завершён. В рамках этого блока был выполнен governance-only reconcile: физически проверили наличие сервисов в `banxe-emi-stack`, обновили `GAP-REGISTER`, создали IL shard и смержили PR #634, после чего 9 GAP были переведены в `🔄 IN PROGRESS`, а 4 thin GAP оставлены как `OPEN → SP-THIN`.[cite:29]

Подтверждённые сервисы, которые были найдены как реальный код и тесты, включают: `regulatory_reporting`, `kyc`, `reporting_analytics`, `risk_management`, `fraud`, `device_fingerprint`, `sanctions_screening`, `fee_management`, `consent_management`.[cite:29]

Следующий подтверждённый путь — это `SP-THIN`, который должен закрыть 4 тонких зоны: `resolution/FSCS`, `resolution/Wind-Down`, `safeguarding-audit`, `incident_response/DORA`, а после этого — `SP-L3DOC`.[cite:29]

### 2.2. Что означает текущее состояние простыми словами

Простыми словами, банк уже существует как архитектурно подтверждённый организм, но ещё не как окончательно оформленная внутренняя «корпоративная конституция». Код есть, многие домены есть, агенты есть, контрольные точки есть, но полного удобного и очень подробного описания «кто работает в банке, кому подчиняется, чем занимается и через какие сервисы это делает» ещё не было собрано в одной академически понятной форме.[cite:29][cite:31]

Именно эту задачу и решает текущий документ.[cite:31]

## 3. Что уже реализовано по спринтам

По истории изменений и следам в приложенном файле можно восстановить общую эволюцию проекта. Часть спринтов строила базовую инфраструктуру и оргкарту, часть добавляла новые агентные домены, часть занималась reconciliations между кодом и governance-слоем.[cite:29]

### 3.1. Спринты 1–2: каркас банка

Ранние спринты заложили фундамент организационной и сервисной карты проекта. В истории явно упоминаются `SERVICE-MAP`, `AGENT-ORG-STRUCTURE`, workflow dispatch и ledger coupling, а также многократные clean re-PR для org/spec-документов.[cite:29]

Практический результат этих спринтов такой: проект получил начальный реестр ролей, начальную карту инфраструктуры, базовую связку между архитектурным репозиторием и instruction ledger, а также видение того, как агентная структура должна соотноситься с сервисной структурой.[cite:29]

### 3.2. Спринт AML / Compliance слоя

Отдельный крупный блок был посвящён AML-комплаенс-контуру. В материалах подробно описаны слои AML stack: policy layer, screening engines, orchestrator, runtime entrypoint, adapters, reporting и audit trail. Там же перечислены конкретные модули `txmonitor.py`, `sanctionscheck.py`, `cryptoaml.py`, `amlorchestrator.py`, `banxeamlorchestrator.py`, Jube/Watchman/Yente adapters и MLRO reporting layer.[cite:29]

Практически это значит, что Financial Crime контур у банка уже не абстрактный: он описан как полноценная вычислительная система с decision thresholds, hit logic, case queue, санкционным short-circuit, SAR queue, ClickHouse audit trail и human-in-the-loop контролем со стороны MLRO.[cite:29]

### 3.3. Finance / Reporting / CFO слой

Следующий массив реализации пришёлся на финансовый контур. В материалах присутствуют `GL Close Agent`, `IFRS Agent`, `APAR Agent`, `Consolidation Agent`, `Tax Agent`, `Data Extractor`, `Data Validator`, `Reconciliation Checker`, `Report Generator`, `CFO Reviewer` и Beancount export layer.[cite:29]

Это означает, что CFO-контур уже частично описан как фактический закрывающий цикл месяца или периода: сбор данных, валидация качества, reconciliation, IFRS-adjustments, consolidation, tax, regulatory return PDF generation, CFO sign-off и последующая ручная подача в My FCA portal authorised person’ом.[cite:29]

### 3.4. Planning, Treasury, Risk, BI

В истории спринтов явно встречаются `FPAAgent`, `BIAgent`, `TreasuryAgent`, `ForecastAgent`, `RiskOversightAgent`, `DataQualityAgent`.[cite:29]

Это говорит о том, что проект уже перешёл от чистого compliance/ledger ядра к более зрелой финансовой управленческой модели: budgeting, forecasting, BI, treasury/ALM и oversight-функции уже хотя бы частично описаны и разведены как отдельные агентные или организационные единицы.[cite:29]

### 3.5. Customer / Business / Supporting functions

Позже в истории появляются `ChargebackAgent`, `CreditScoringAgent`, `ContractAgent`, `LeadScoringAgent`, `ChurnPredictionAgent`, `NPSAgent`, `CampaignAgent`, а также расширение front office и marketing/customer support направления.[cite:29]

Это важно, потому что проект перестаёт быть только «машиной по комплаенсу и ledger». Он превращается в полноценный банк с front-office и customer-facing логикой, пусть часть этих функций пока ещё находится на уровне proposed/implemented masks или partial build.[cite:29]

### 3.6. Full audit и SP-RECON

Последний крупный этап — это audit + reconciliation. В истории явно фигурируют `ORG code reconciliation matrix`, `full-project installation audit`, SP-RECON и проверка stale OPEN статусов по GAP-реестру.[cite:29]

Именно на этом этапе стало ясно, что многие сервисы уже существуют в коде, а проблемы были не в отсутствии реализации, а в отставании governance-метаданных от реального состояния runtime.[cite:29]

## 4. Общая целевая модель банка

Теперь можно перейти к главному: как выглядит банк целиком.

EMI BANXE AI BANK в текущем понимании — это **AI-native EMI банк**, который строится не как «несколько ботов при банке», а как многоуровневая организационная система. В этой системе каждый элемент имеет одновременно три проекции: организационную, агентную и сервисную.[cite:29][cite:31]

### 4.1. Три проекции одной структуры

1. **Организационная проекция** — это департаменты, отделы, начальники, независимые функции, board committees и люди-дублёры.[cite:31]
2. **Агентная проекция** — это AI-агенты разных уровней: рядовые агенты-исполнители, AI-контролёры/начальники отделов, AI-начальники департаментов, orchestration-агенты верхнего уровня, независимые MLRO и Audit агенты.[cite:29][cite:31]
3. **Сервисная проекция** — это конкретные runtime-сервисы, adapters, databases, queues, dashboards, APIs и pipelines, через которые эти роли фактически работают.[cite:29]

Только совмещение этих трёх проекций даёт «настоящий банк», а не просто красивую оргсхему.[cite:29]

### 4.2. Базовая вертикаль управления

Целевая вертикаль банка выглядит так:

- Рядовые AI-сотрудники выполняют конкретные операции внутри отделов.[cite:31]
- AI-контролёры или начальники отделов проверяют корректность, агрегируют результаты и управляют очередями задач.[cite:31]
- AI-начальники департаментов координируют несколько отделов и формируют единый departmental view.[cite:31]
- CEO Orchestration Agent получает aggregated inputs от всех департаментов и формирует управленческую картину банка.[cite:31]
- Человек-дублёр на верхнем уровне утверждает решения там, где это запрещено делегировать машине по праву, policy или prudential logic.[cite:29][cite:31]

### 4.3. Две независимые линии

При этом две линии специально не должны теряться внутри обычной иерархии:

- `MLRO / Financial Crime` как независимая контрольная вертикаль с собственными HITL-гейтами и прямым каналом в Board/CEO.[cite:29][cite:31]
- `Internal Audit` как третья линия защиты с прямой независимостью от операционных департаментов.[cite:29][cite:31]

## 5. Полный оргчарт банка: департаменты, отделы, начальники, сотрудники, люди-дублёры

Ниже приведён детальный расклад по каждому крупному блоку банка.

## 5.1. Board & Executive

Это верхний стратегический слой банка. Он не занимается ежедневными операциями напрямую, но именно здесь находятся персональная ответственность, конечное утверждение политик, лимитов, планов и критических решений.[cite:31]

### Состав блока

- Board of Directors.[cite:31]
- Audit Committee.[cite:31]
- Risk Committee.[cite:31]
- Remuneration Committee.[cite:31]
- Nomination Committee.[cite:31]
- CEO.[cite:31]
- Company Secretary.[cite:31]
- Board Reporting Agent.[cite:31]
- CEO Orchestration Agent.[cite:31]

### Функции блока

Этот блок принимает итоговые управленческие решения. Сюда приходят агрегированные отчёты из CFO, COO, CTO, CRO, Compliance, MLRO и Internal Audit. Здесь утверждаются изменения capital/liquidity posture, wind-down readiness, strategic product direction, material incidents, regulatory escalations и high-level remediation plans.[cite:29][cite:31]

### AI-сотрудники внутри блока

#### 1. Board Reporting Agent

Этот агент должен собирать информацию от всех контролирующих и операционных блоков, готовить board packs, risk dashboards, finance snapshots и executive summaries.[cite:31]

По логике проекта он не должен принимать решений за Board, а должен служить как интеллектуальный assembly layer для материалов заседаний и комитетов.[cite:31]

#### 2. CEO Orchestration Agent

Это верхний AI-менеджер банка. Он получает сигналы от department-head agents, сравнивает KPI, риски, ликвидность, incidents, compliance breaks и growth metrics, формирует executive picture и предлагает решения или escalation paths CEO-человеку.[cite:31]

Этот агент критически важен, потому что без него AI-структура превращается в набор разрозненных доменов. Именно он связывает банк в единое целое.[cite:31]

### Люди-дублёры

- CEO.[cite:31]
- Chair of the Board / Board principals.[cite:31]
- Company Secretary для board process governance.[cite:31]

### Что здесь пока не хватает

В материалах верхний executive слой намечен, но не раскрыт так же подробно, как AML или Finance. Значит, здесь явно требуется formal `CEO Decision Agent` с понятным набором входов, allowed interactions, escalation logic и перечнем non-delegable decisions.[cite:29][cite:31]

## 5.2. Independent Functions

Это независимые функции второй и третьей линии защиты. Они не должны растворяться в коммерческих или операционных блоках, потому что их задача — не «делать бизнес», а следить, чтобы бизнес делался в допустимых рамках.[cite:31]

### 5.2.1. Risk

#### Руководство

- Chief Risk Officer (CRO).[cite:31]
- Human double: CRO.[cite:31]

#### Подфункции

- Credit / Counterparty Risk.[cite:31]
- Market / FX Risk.[cite:31]
- Liquidity Risk.[cite:31]
- Operational Risk.[cite:31]

#### AI-агенты

- Risk Oversight Agent.[cite:29]
- Risk Analytics Agent.[cite:31]
- Liquidity Risk Agent.[cite:31]
- Scenario / Stress layer как логическое продолжение risk analytics.[cite:31]

#### Что делает этот блок

Этот блок должен измерять риски банка, стрессировать сценарии, следить за лимитами, оценивать capital/liquidity posture и взаимодействовать с CFO и COO по exposure и operational risks.[cite:31]

#### Связь с кодом и сервисами

На сервисном уровне здесь особенно близки домены `services/risk`, `services/riskmanagement`, `services/reportinganalytics`, `services/treasury`, `services/fxengine`, `services/fxexchange`, `services/fxrates`, а также finance/risk analytics пайплайны, описанные в org/history materials.[cite:29]

#### Чего не хватает

Пока в материалах виден `RiskOversightAgent`, но не раскрыт полный штат риска на уровне worker agents: limit monitoring, scenario library management, concentration risk analyst, model validation support, policy exception triage.[cite:29]

### 5.2.2. Compliance

#### Руководство

- Head of Compliance.[cite:31]
- Human double: Head of Compliance.[cite:31]

#### Подфункции

- EMRs / PSRs compliance.[cite:31]
- CASS 15 / safeguarding policy oversight.[cite:31]
- Conduct / consumer duty.[cite:29][cite:31]
- Policy / rulebook management.[cite:31]
- Privacy / DPO layer, если совмещён на sandbox-stage.[cite:29][cite:31]

#### AI-агенты

- Rulebook Agent.[cite:31]
- Privacy Compliance Agent.[cite:29][cite:31]
- Policy Management Agent.[cite:31]
- Consumer duty / conduct support agents как логически ожидаемое продолжение `services/consumerduty`, `services/complianceautomation`, `services/compliancecalendar`, `services/compliancekb`, `services/compliancesync`.[cite:29]

#### Что делает этот блок

Комплаенс следит за тем, чтобы процессы банка соответствовали EMRs, PSRs, safeguarding obligations, conduct expectations и внутренним политикам. Это блок policy interpretation, control design, policy change tracking и governance challenge.[cite:31]

#### Связь с кодом и сервисами

По сервисной карте видны доменные сервисы `services/compliance`, `services/complianceautomation`, `services/compliancecalendar`, `services/compliancekb`, `services/compliancesync`, `services/consumerduty`, `services/fatcacrs` и privacy-related контуры через Presidio / privacy roles.[cite:29]

#### Ключевая организационная оговорка

MLRO не должен растворяться в этом блоке как простая подроль. В текущем целевом понимании `Head of Compliance` и `MLRO` — это близкие, но организационно разные линии, особенно для AI-структуры и HITL-модели.[cite:31]

### 5.2.3. Internal Audit

#### Руководство

- Head of Internal Audit.[cite:31]
- Human double: Head of Internal Audit.[cite:31]
- Для annual safeguarding audit может требоваться также внешний аудитор как независимый человек-участник.[cite:31]

#### AI-агенты

- Internal Audit Agent.[cite:31]
- Safeguarding Audit Agent.[cite:29][cite:31]
- Beancount Export Agent как supporting audit evidence layer на financial side.[cite:29]

#### Что делает этот блок

Внутренний аудит не управляет бизнесом и не исправляет за бизнес, а проверяет, как бизнес и контрольные функции выполняют свои обязанности. Он должен иметь независимый доступ к evidence trails, logs, reconciliation outputs, governance docs и policy execution traces.[cite:31]

#### Связь с кодом и сервисами

Internal audit особенно опирается на `services/audit`, `services/auditdashboard`, `services/audittrail`, Beancount export, ClickHouse retention layers, OpenMetadata lineage и output artefacts, описанные в finance/AML pipelines.[cite:29]

#### Чего не хватает

В текущих материалах идея annual safeguarding audit уже присутствует, но не виден полностью развёрнутый internal audit operating model: annual plan agent, control testing library, issue remediation tracker, audit committee reporting cadence.[cite:29][cite:31]

## 5.3. CFO Office — финансы и аналитика

Это один из самых развитых блоков проекта, потому что он уже опирается на множество конкретных agent passports и workflow-сценариев.[cite:29]

### 5.3.1. Financial Controlling & Accounting

#### Руководство

- CFO.[cite:31]
- Financial Controller / Head of Accounting.[cite:31]
- Human doubles: CFO, Financial Controller.[cite:31]

#### Низовой функционал

- GL management.[cite:31]
- AP / AR.[cite:31]
- Fixed Assets.[cite:31]
- Tax accounting.[cite:31]
- Consolidation.[cite:31]
- IFRS 9 / IFRS 18 adjustments.[cite:31]

#### AI-агенты

- GL Close Agent.[cite:29][cite:31]
- APAR Agent.[cite:29]
- IFRS Agent.[cite:29][cite:31]
- Consolidation Agent.[cite:29][cite:31]
- Tax Compliance Agent / Tax Agent.[cite:29]
- Beancount Export Agent.[cite:29]
- CFO Controller Agent / cforeviewer / accounting-swarm coordinator.[cite:29]

#### Как работает этот контур

Материалы описывают почти полный period-close pipeline. Сначала запускается `GL Close Agent`, который сводит GL и ledger snapshots, затем `IFRS Agent` предлагает IFRS-проводки, параллельно `APAR Agent` обрабатывает invoices, autoreconcile, aging и payment proposals. После этого `Consolidation Agent` собирает multi-entity view, `Tax Agent` считает VAT/corporate tax, а `Beancount Export Agent` формирует append-only audit trail.[cite:29]

Финальный контрольный узел — `CFO Controller Agent`, который является single HITL point для close/reporting цикла перед одобрением человека.[cite:29]

#### Связь с сервисами

На ORG-CODE-RECONCILIATION уровне этот блок связан с сервисами `services/ledger`, `services/recon`, `services/reporting`, `services/reportinganalytics`, `services/feemanagement`, `services/treasury`, `services/fxrates`, `services/fxengine`, `services/statements`, `services/clientstatements`, `services/midazmcp`, а также Midaz/Formance/Odoo/ERPNext слоями, упомянутыми в finance pipeline.[cite:29]

#### Чего не хватает

Не до конца оформлены как отдельные роли `Accounts Payable Agent`, `Accounts Receivable Agent`, `Expense Control Agent`, `Capital Planning Agent`, хотя часть их функции уже скрыта внутри APAR/close stack.[cite:29]

### 5.3.2. FP&A

#### Руководство

- Head of FP&A.[cite:31]
- Human double: Head of FP&A.[cite:31]

#### Функции

- Budgeting.[cite:31]
- Rolling forecast.[cite:31]
- Variance analysis.[cite:31]
- Management reporting.[cite:31]
- What-if and sensitivity analysis.[cite:31]

#### AI-агенты

- Budget Agent.[cite:31]
- Forecast Agent.[cite:31]
- Scenario / Stress Agent.[cite:31]
- FPAAgent.[cite:29]
- BIAgent / Finance BI Agent.[cite:29][cite:31]

#### Связь с сервисами

Логически этот блок использует `services/reportinganalytics`, `services/reporting`, `services/treasury`, `services/feemanagement`, product/business analytics и finance data warehouse слои.[cite:29]

#### Чего не хватает

Нужны более явные low-level worker roles: budget analyst agent, management reporting analyst agent, variance investigation agent, planning assumptions agent.[cite:31]

### 5.3.3. Treasury / ALM

#### Руководство

- Head of Treasury / ALM.[cite:31]
- Human double: Head of Treasury.[cite:31]

#### Функции

- Liquidity management.[cite:31]
- Strategic safeguarding pool management.[cite:31]
- FX position management.[cite:31]
- Cash planning and funding posture.[cite:31]

#### AI-агенты

- Treasury Position Agent.[cite:31]
- FX Exposure Agent.[cite:31]
- TreasuryAgent / treasuryalmagent.[cite:29]
- ForecastAgent как связанный planning component.[cite:29]

#### Связь с кодом и сервисами

Это связано с `services/treasury`, `services/fxengine`, `services/fxexchange`, `services/fxrates`, `services/multicurrency`, `services/safeguarding`, `services/safeguarding-engine`, а также risk/liquidity layers.[cite:29]

#### Чего не хватает

Пока не видно fully specified collateral / concentration / cash ladder / intraday liquidity staffing. Нужны более детальные treasury worker roles.[cite:29]

### 5.3.4. Regulatory Financial Reporting

#### Руководство

- Head of Regulatory Reporting / Prudential Reporting.[cite:31]
- Human double: Head of Regulatory Reporting, CFO for non-delegable submission.[cite:29][cite:31]

#### Функции

- FIN060a/b.[cite:31]
- Monthly safeguarding return (CASS 15).[cite:31]
- Resolution Pack preparation.[cite:31]
- Statistical and management regulatory packs.[cite:31]

#### AI-агенты

- Data Extractor.[cite:29]
- Data Validator.[cite:29]
- Reconciliation Checker.[cite:29]
- Report Generator / FCA Return Generator Agent.[cite:29]
- Resolution Pack Agent.[cite:31]
- cforeviewer / CFO approval gate.[cite:29]

#### Как работает этот контур

Материалы описывают чёткий pipeline: `Data Extractor` тянет данные из ClickHouse / Midaz / Odoo; `Data Validator` применяет Great Expectations; `Reconciliation Checker` сверяет ledger и bank statements через bank statement parsers + Blnk/Formance reconciliation; затем `Report Generator` собирает PDF returns и resolution pack; после этого `CFO Reviewer` инициирует HITL approval; окончательная подача в My FCA portal выполняется человеком вручную, потому что публичного API нет.[cite:29]

#### Связь с сервисами

Связанные сервисы: `services/regulatoryreporting`, `services/reporting`, `services/reportinganalytics`, `services/safeguarding`, `services/safeguarding-engine`, `services/recon`, `services/statements`, `services/ledger`, `services/audittrail`, `services/dataquality`.[cite:29]

#### Чего не хватает

Не до конца оформлена отдельная staffing-структура этого блока: data lineage analyst agent, prudential mapping analyst agent, regulatory submission control agent.[cite:29]

### 5.3.5. Finance Data & BI

#### Руководство

- Head of Finance Data / Finance Systems.[cite:31]
- Human double: Head of Finance Data.[cite:31]

#### AI-агенты

- Finance BI Agent.[cite:31]
- Data Quality Agent.[cite:29][cite:31]
- BiDashboardGovernor and related data governance roles.[cite:29]

#### Связь с сервисами

- `services/dataquality`.[cite:29]
- `services/reportinganalytics`.[cite:29]
- ClickHouse / dbt / OpenMetadata / dashboard layers.[cite:29][cite:31]

#### Недостатки

Этот блок уже виден как технология и аналитика, но organisationally needs more explicit ownership over certified datasets, finance semantic layer, dashboard stewardship and data issue remediation loop.[cite:29]

### 5.3.6. Wind-Down Planning

#### Руководство

- CFO как владелец плана.[cite:31]
- Board как утверждающий орган.[cite:31]
- Human double: CFO.[cite:31]

#### AI-агент

- WindDownPlanningAgent.[cite:29][cite:31]

#### Что делает блок

Этот блок должен моделировать orderly run-off, stress closure scenarios, operational continuity in wind-down and regulatory communication readiness.[cite:31]

#### Что видно по коду

В agent passports уже присутствует `winddownplanningagent`, но сам функциональный runtime слой пока относится к thin areas и должен усиливаться в `SP-THIN` / resolution workstream.[cite:29]

## 5.4. COO / Operations

Это блок ежедневного движения банка. Он отвечает за то, чтобы деньги двигались правильно, safeguarding соблюдался, клиенты обслуживались, а operational exceptions не превращались в кризисы.[cite:31]

### 5.4.1. Payment Operations

#### Руководство

- Head of Payments Operations.[cite:31]
- Human double: Head of Payments Ops.[cite:31]

#### AI-агенты

- Payments Orchestrator Agent.[cite:31]
- PaymentRouterAgent.[cite:29]
- ChannelCSepaOrchestrator.[cite:29]
- ChannelCSwiftOrchestrator.[cite:29]

#### Сервисы

- `services/payment`.[cite:29]
- `services/batchpayments`.[cite:29]
- `services/beneficiarymanagement`.[cite:29]
- `services/scheduledpayments`.[cite:29]
- `services/swiftcorrespondent`.[cite:29]
- `services/psd2gateway`.[cite:29]
- `services/openbanking`.[cite:29]
- `services/providers`, `services/producers`, `services/webhooks`, `services/webhookorchestrator`.[cite:29]

#### Чего не хватает

Не хватает более явного штата low-level operations agents: payment exception agent, cut-off monitoring agent, settlement mismatch agent, scheme compliance agent.[cite:31]

### 5.4.2. Safeguarding Operations

#### Руководство

- Head of Safeguarding Operations.[cite:31]
- Human double: Head of Safeguarding Ops.[cite:31]

#### AI-агенты

- Safeguarding Reconciliation Agent / reconciliationchecker.[cite:29][cite:31]
- Safeguarding Monitoring Agent.[cite:31]
- SafeguardingReconGovernor as governance role.[cite:29]

#### Функции

- Daily reconciliation.[cite:31]
- Break reporting.[cite:31]
- Coverage monitoring.[cite:31]
- Operational follow-up on safeguarding deficits or mismatches.[cite:31]

#### Сервисы

- `services/safeguarding`.[cite:29]
- `services/safeguarding-engine`.[cite:29]
- `services/recon`.[cite:29]
- `services/statements`.[cite:29]
- ledger + CAMT/MT940 parsing and reconciliation stack.[cite:29][cite:31]

#### Чего не хватает

В roadmap прямо видно, что `safeguarding-audit` пока относится к thin area. Значит, operational safeguarding есть частично, но audit and closure around it ещё должны быть формально завершены.[cite:29]

### 5.4.3. Customer Operations / Disputes

#### Руководство

- Head of Customer Operations.[cite:31]
- Human double: Head of Customer Ops.[cite:31]

#### AI-агенты

- Complaints Agent.[cite:31]
- Disputes Agent.[cite:31]
- ChargebackAgent.[cite:29]
- SupportSlaGovernor.[cite:29]

#### Сервисы

- `services/complaints`.[cite:29]
- `services/disputeresolution`.[cite:29]
- `services/support`.[cite:29]
- `services/notifications`, `services/notificationhub`.[cite:29]
- `services/customer`, `services/customerlifecycle`, `services/crm`.[cite:29]

#### Чего не хватает

Нужны complaint QA agent, dispute evidence assembly agent, ombudsman escalation agent, vulnerability / customer harm detection agent.[cite:29]

## 5.5. CTO / Technology, Data, AI

Этот блок отвечает за платформу, интеграции, надёжность, data plumbing и саму AI-фабрику банка.[cite:31]

### 5.5.1. Core Systems & Integrations

#### Руководство

- Head of Core Banking / Core Platforms.[cite:31]
- Human double: CTO or head of core platforms.[cite:31]

#### AI-агенты

- Integration Agent.[cite:31]
- MGatewayApiGovernor.[cite:29]
- AgreementAgent / integration-adjacent contract roles.[cite:29]

#### Сервисы

- `services/apigateway`.[cite:29]
- `services/apiversioning`.[cite:29]
- `services/intentlayer`.[cite:29]
- `services/ledger`.[cite:29]
- `services/midazmcp`.[cite:29]
- `services/documentmanagement`.[cite:29]
- `services/events`.[cite:29]
- `services/config`, `services/shared`, `services/secrets`, `services/auth`, `services/iam`.[cite:29]

### 5.5.2. Data Engineering & Platform

#### Руководство

- Head of Data Engineering.[cite:31]
- Human double: Head of Data Engineering.[cite:31]

#### AI-агенты

- Data Pipeline Agent.[cite:31]
- Datalake ELT agent layer.[cite:29]
- DataQualityAgent / governance roles.[cite:29]

#### Сервисы

- `services/dataquality`.[cite:29]
- `services/reportinganalytics`.[cite:29]
- `services/mlpipeline`.[cite:29]
- ClickHouse / Kafka-equivalent / ETL / dbt / OpenMetadata stack.[cite:29][cite:31]

### 5.5.3. DevOps / SRE

#### Руководство

- Head of SRE.[cite:31]
- Human double: Head of SRE.[cite:31]

#### AI-агенты

- SRE Agent.[cite:31]
- DeployAgent.[cite:29]
- SandboxRailsGovernor / SDKReleaseGovernor as dev platform governance roles.[cite:29]

#### Сервисы

- `services/deploy`.[cite:29]
- `services/observability`.[cite:29]
- `services/backup`.[cite:29]
- `services/alerting`.[cite:29]
- `services/cigovernance`.[cite:29]

### 5.5.4. AI Platform

#### Руководство

- Head of AI Platform.[cite:31]
- Human double: Head of AI Platform.[cite:31]

#### AI-агенты

- AI Orchestrator Agent.[cite:31]
- MetaClaw Skill Manager Agent.[cite:31]
- OpenClaw bots, LiteLLM gateway, model-routing and reasoning layers as platform assets.[cite:29]

#### Сервисы

- `services/agents`.[cite:29]
- `services/agentrouting`.[cite:29]
- `services/swarm`.[cite:29]
- `services/reasoningbank`.[cite:29]
- `services/experimentcopilot`.[cite:29]
- `services/notificationhub` for ops interaction.[cite:29]

### 5.5.5. Operational Resilience

#### Руководство

- CTO + COO shared accountability, board-level visibility.[cite:31]
- Human double: CTO / COO depending on incident class.[cite:31]

#### AI-агент

- ResilienceAgent.[cite:29][cite:31]

#### Сервисы

- `services/incidentresponse`.[cite:29]
- `services/observability`.[cite:29]
- `services/alerting`.[cite:29]
- disaster-recovery / runbook / continuity stack implied by SRE + resilience layers.[cite:29]

#### Чего не хватает

`incident_response/DORA` прямо относится к thin areas в roadmap, поэтому этот блок ещё не завершён до полного L2/L3 operating state.[cite:29]

## 5.6. MLRO / Financial Crime

Это один из наиболее проработанных блоков проекта. Он уже имеет и организационную логику, и конкретные runtime-пайплайны, и HITL-гейты.[cite:29][cite:31]

### Руководство

- MLRO.[cite:31]
- Head of Financial Crime Operations.[cite:31]
- Human doubles: MLRO, Head of Financial Crime.[cite:31]

### Подразделения

- AML Transaction Monitoring.[cite:31]
- KYC/KYB.[cite:31]
- Sanctions & Screening.[cite:31]
- Fraud Investigation.[cite:31]

### AI-агенты

- Banxe AML Orchestrator.[cite:29]
- AML Monitoring Agent / txmonitorcore.[cite:29][cite:31]
- Sanctions Agent / sanctionscheckcore.[cite:29][cite:31]
- KYC/KYB Agent.[cite:31]
- Fraud Analytics Agent.[cite:31]
- Jube Adapter Core.[cite:29]
- Watchman Adapter Core.[cite:29]
- Yente Adapter Agent.[cite:29]
- MLRO Report Agent.[cite:29]
- MLRO Case Agent.[cite:31]

### Как устроен этот контур

AML stack описан как многослойная структура. Layer 1 содержит policy / thresholds / hard rules из `compliancevalidator.py`. Layer 2 содержит deterministic engines: `txmonitor.py`, `sanctionscheck.py`, `cryptoaml.py`, `amlorchestrator.py`. Layer 3 — это `banxeamlorchestrator.py` как runtime orchestration entrypoint. Далее идут adapters к Jube, Watchman, Yente и reporting / MLRO queue / ClickHouse evidence layer.[cite:29]

Есть конкретные decision thresholds: при composite score 85 или sanction hit формируется SAR path; 70–84 — reject; 40–69 — hold/EDD; ниже 40 — approve, если нет hardblock. Отдельно есть hard overrides по sanctions и high-risk jurisdiction logic.[cite:29]

### Сервисы

На service-level ORG-CODE-RECONCILIATION этот блок связан с:

- `services/aml`.[cite:29]
- `services/transactionmonitor`.[cite:29]
- `services/sanctionsscreening`.[cite:29]
- `services/kyc`.[cite:29]
- `services/kybonboarding`.[cite:29]
- `services/fraud`.[cite:29]
- `services/cryptoamlgraph`.[cite:29]
- `services/devicefingerprint`.[cite:29]
- `services/casemanagement`.[cite:29]
- `services/compliance`.[cite:29]
- `services/adversemedia`.[cite:29]

### Чего не хватает

Хотя блок сильный, не полностью оформлен низовой operational staffing. Нужны явно выделенные `Alert Triage Agent`, `EDD Agent`, `Case Disposition Agent`, `PEP Review Agent`, `False Positive Review Agent`, `Periodic Review Agent`.[cite:29][cite:31]

## 5.7. Front Office / Business

Этот блок отвечает за продукты, клиентов, коммерческий рост и BaaS/partnership направление.[cite:31]

### Руководство

- Chief Commercial Officer / Head of Business.[cite:31]
- Human doubles: CCO / BU heads.[cite:31]

### Подразделения

- Retail / Digital.[cite:31]
- Corporate / Institutional.[cite:31]
- Crypto / DeFi business unit, если активен.[cite:31]
- Partnerships / BaaS / Embedded.[cite:31]

### AI-агенты

- Product Analytics Agent.[cite:31]
- Pricing Agent / PricingFeeGovernor.[cite:29][cite:31]
- Partner Onboarding Agent.[cite:31]
- LeadScoringAgent.[cite:29]
- CampaignAgent.[cite:29]
- ChurnPredictionAgent.[cite:29]
- NPSAgent.[cite:29]
- CreditScoringAgent.[cite:29]

### Сервисы

- `services/campaign`.[cite:29]
- `services/churn`.[cite:29]
- `services/crm`.[cite:29]
- `services/customer`.[cite:29]
- `services/customerlifecycle`.[cite:29]
- `services/referral`.[cite:29]
- `services/loyalty`.[cite:29]
- `services/lending`.[cite:29]
- `services/merchantacquiring`.[cite:29]
- `services/quantadvisory`.[cite:29]
- `services/cardissuing`.[cite:29]

### Недостатки

Здесь виден сильный набор точечных агентных ролей, но не до конца оформлена departmental hierarchy: нужен head of product orchestration agent, partner monitoring agent, product governance agent и customer growth controller layer.[cite:29][cite:31]

## 5.8. HR, Legal, Corporate Services

Это обслуживающий, но критически важный блок. Он нужен для competence management, contracts, people governance, privacy и административного каркаса банка.[cite:31]

### Руководство

- HR Director.[cite:31]
- General Counsel.[cite:31]
- DPO / Privacy lead, если выделен отдельно.[cite:31]
- Human doubles: HR Director, General Counsel, DPO.[cite:31]

### AI-агенты

- HR Compliance Agent.[cite:31]
- Contract Review Agent / ContractAgent.[cite:29][cite:31]
- Policy Management Agent.[cite:31]
- Privacy Compliance Agent.[cite:29][cite:31]

### Сервисы

- `services/hr`.[cite:29]
- `services/agreement`.[cite:29]
- `services/documentmanagement`.[cite:29]
- `services/compliancecalendar`.[cite:29]
- `services/compliancekb`.[cite:29]
- `services/iam` and access governance adjacency.[cite:29]

### Чего не хватает

Здесь особенно нужен `Training & Certification Agent` для AML/conduct/privacy learning tracking, plus procurement/vendor governance layer and regulatory appointment records support.[cite:29][cite:31]

## 6. Вертикальные связи в банке

Теперь нужно описать, как весь этот банк работает как иерархия.

### 6.1. Общая вертикаль

Основная вертикаль банка должна быть такой:

1. **Worker Agents** — выполняют задачу.[cite:31]
2. **Team Lead / Controller Agents** — проверяют качество, снимают ошибки, решают стандартные конфликты, агрегируют результаты.[cite:31]
3. **Department Head Agents** — управляют отделами как системой, собирают KPI, exceptions, risks, quality issues и эскалируют наверх.[cite:31]
4. **CEO Orchestration Agent** — собирает единый operational picture банка.[cite:31]
5. **Human doubles / Board** — принимают конечные решения в non-delegable зонах.[cite:31]

### 6.2. Отдельные независимые вертикали

- `MLRO Agent` имеет собственную линию надзора и не должен идти «через CFO» или «через COO».[cite:31]
- `Internal Audit Agent` не должен подчиняться операционно CFO/COO/CTO, а должен иметь независимый отчётный контур к Board / Audit Committee.[cite:31]

## 7. Горизонтальные связи между департаментами

Банк не работает как набор изолированных колонок. Поэтому горизонтальные связи так же важны, как вертикальные.[cite:31]

### 7.1. Ключевые пары горизонтального взаимодействия

- `CFO ↔ COO` — safeguarding, reconciliation breaks, operational shortfalls, settlement effects in reporting.[cite:31]
- `CFO ↔ CRO` — liquidity, limits, stress scenarios, balance-sheet implications.[cite:31]
- `COO ↔ CTO` — payments reliability, incidents, resilience, operational automation.[cite:31]
- `Compliance ↔ MLRO` — policy interpretation vs financial crime execution.[cite:31]
- `MLRO ↔ CTO` — model updates, alert systems, screening logic governance.[cite:31]
- `Business ↔ Compliance` — onboarding controls, product governance, customer-facing process boundaries.[cite:31]
- `Business ↔ CFO` — pricing, profitability, economics of products and partnerships.[cite:31]

### 7.2. Что ещё должно быть зафиксировано позже

Эти связи должны быть позже оформлены как formal matrix: `allowed callers`, `allowed callees`, `event contracts`, `escalation policies`, `approval gates`, `shared datasets`, `forbidden direct actions`.[cite:29][cite:31]

## 8. ORG-CODE-RECONCILIATION: сопоставление оргструктуры с доменными сервисами

Ниже приведён важный раздел: как организационные блоки отображаются в кодовую и сервисную структуру.

### 8.1. Сервисы, уже явно присутствующие в сервисной карте

В приложенных материалах перечислен большой перечень service directories. Среди них особенно важны для банка следующие доменные сервисы: `services/aml`, `services/ledger`, `services/payment`, `services/openbanking`, `services/regulatoryreporting`, `services/reporting`, `services/reportinganalytics`, `services/resolution`, `services/risk`, `services/riskmanagement`, `services/safeguarding`, `services/safeguarding-engine`, `services/sanctionsscreening`, `services/transactionmonitor`, `services/treasury`, `services/kyc`, `services/kybonboarding`, `services/fraud`, `services/cryptoamlgraph`, `services/devicefingerprint`, `services/disputeresolution`, `services/customer`, `services/customerlifecycle`, `services/dataquality`, `services/deploy`, `services/incidentresponse`, `services/notifications`, `services/observability`, `services/auth`, `services/iam`, `services/consentmanagement`, `services/feemanagement`, `services/fatcacrs`, `services/documentmanagement`, `services/complaints`, `services/campaign`, `services/churn`, `services/crm`, `services/lending`, `services/cardissuing`, `services/merchantacquiring`, `services/multicurrency`, `services/statements`, `services/recon`, `services/support` и другие.[cite:29]

### 8.2. Сопоставление блоков и сервисов

| Организационный блок | Основные сервисы | Смысл связи |
|---|---|---|
| Board & Executive | `reporting`, `reportinganalytics`, dashboard layers, board pack outputs.[cite:29] | Верхний слой потребляет агрегированные отчёты, а не raw operations.[cite:29] |
| Risk | `risk`, `riskmanagement`, `reportinganalytics`, `treasury`, `fxrates`.[cite:29] | Управление лимитами, stress/scenario, liquidity and exposure analysis.[cite:29] |
| Compliance | `compliance`, `complianceautomation`, `compliancecalendar`, `compliancekb`, `consumerduty`, `fatcacrs`.[cite:29] | Policy/control/design и tracking regulatory obligations.[cite:29] |
| Internal Audit | `audit`, `auditdashboard`, `audittrail`, evidence exports, Beancount/OpenMetadata outputs.[cite:29] | Независимый assurance доступ к evidence layer.[cite:29] |
| CFO Office | `ledger`, `recon`, `reporting`, `reportinganalytics`, `regulatoryreporting`, `treasury`, `feemanagement`, `statements`.[cite:29] | Close, accounting, reporting, BI, treasury, prudential/regulatory returns.[cite:29] |
| COO / Operations | `payment`, `batchpayments`, `openbanking`, `psd2gateway`, `safeguarding`, `safeguarding-engine`, `disputeresolution`, `complaints`, `support`.[cite:29] | Daily operations and exception handling.[cite:29] |
| CTO / Technology | `apigateway`, `apiversioning`, `agentrouting`, `swarm`, `deploy`, `observability`, `intentlayer`, `shared`, `config`, `events`, `iam`, `auth`.[cite:29] | Platform, integration, deployment, reliability, AI orchestration.[cite:29] |
| MLRO / Financial Crime | `aml`, `transactionmonitor`, `sanctionsscreening`, `kyc`, `kybonboarding`, `fraud`, `cryptoamlgraph`, `devicefingerprint`, `casemanagement`, `adversemedia`.[cite:29] | Fincrime detection, decisioning, review and case management.[cite:29] |
| Business | `campaign`, `crm`, `customer`, `customerlifecycle`, `loyalty`, `referral`, `lending`, `merchantacquiring`, `cardissuing`.[cite:29] | Product growth, customer journeys, partnerships and economics.[cite:29] |
| HR / Legal | `hr`, `agreement`, `documentmanagement`, policy and role-governance adjacency services.[cite:29] | People, contracts, training, privacy and legal administration.[cite:29] |

### 8.3. Что уже reconciled, а что ещё нет

`SP-RECON` подтвердил, что как минимум 9 GAP-областей уже имеют реальный код и тесты: `regulatory_reporting`, `kyc`, `reporting_analytics`, `risk_management`, `fraud`, `device_fingerprint`, `sanctions_screening`, `fee_management`, `consent_management`.[cite:29]

Одновременно 4 области пока остаются как thin/open и подлежат отдельному усилению: `resolution/FSCS`, `resolution/Wind-Down`, `safeguarding-audit`, `incident_response/DORA`.[cite:29]

Это значит, что ORG-CODE-RECONCILIATION уже продвинулся существенно, но ещё не завершён полностью. Особенно это касается independent assurance, resilience и resolution/wind-down сегментов.[cite:29]

## 9. Каких сотрудников и агентов не хватает для полноценной работы банка

Теперь можно сформулировать это очень прямо.

### 9.1. Чего не хватает на уровне верхнего управления

- Formal `CEO Decision Agent` с operational cockpit, priorities engine и structured board escalation flow.[cite:29][cite:31]
- Более подробная board reporting hierarchy, включая committee-specific packs.[cite:31]

### 9.2. Чего не хватает на уровне контроля

- Fully specified `Safeguarding Audit Agent` operating model.[cite:29][cite:31]
- DPO / Privacy line как полноценно встроенной функции, а не только намеченного агента.[cite:29][cite:31]
- Model risk / AI safety support under CTO + compliance governance.[cite:29][cite:31]

### 9.3. Чего не хватает на уровне Financial Crime

- Alert Triage Agent.[cite:31]
- EDD Agent.[cite:31]
- Case Disposition Agent.[cite:31]
- Periodic Review Agent.[cite:29]
- False Positive Review Agent.[cite:29]

### 9.4. Чего не хватает на уровне Operations

- Reconciliation Break Agent.[cite:31]
- Payment Exception Agent.[cite:31]
- Complaints QA Agent.[cite:29]
- Vulnerable Customer / Harm Monitoring Agent.[cite:29]

### 9.5. Чего не хватает на уровне Finance

- Expense Control Agent.[cite:29]
- Capital & Liquidity Planning Agent.[cite:29]
- Regulatory Data Mapping Agent.[cite:29]
- Submission Control Agent.[cite:29]

### 9.6. Чего не хватает на уровне Business и Support

- Product Governance Agent.[cite:31]
- Partner Monitoring Agent.[cite:31]
- Training & Certification Agent.[cite:31]
- Vendor / Outsourcing Oversight Agent.[cite:29]

## 10. Главные недостатки текущей структуры

На основании всего материала можно выделить несколько системных недостатков.

### 10.1. Недостаток №1 — не до конца формализована кадровая лестница

Сейчас хорошо видны отдельные агентные роли и отдельные сервисы, но не до конца оформлена полная лестница `worker → controller → department head → CEO Agent` для всех департаментов одинаково.[cite:29][cite:31]

### 10.2. Недостаток №2 — часть ролей есть в паспортах, но ещё не встроена в жизнеспособную оргмодель

Некоторые агенты уже существуют как passports или proposed builds, но ещё не занимают чёткое место в operational staffing model банка.[cite:29]

### 10.3. Недостаток №3 — thin areas всё ещё остаются пробелами

Пока не закрыты `resolution`, `wind-down`, `safeguarding-audit`, `incident_response/DORA`, нельзя говорить о полностью зрелой модели банка.[cite:29]

### 10.4. Недостаток №4 — executive and cross-department layer пока слабее, чем domain-specific layers

AML и finance описаны значительно глубже, чем CEO-layer, board committees, complete business governance и interdepartment contract layer.[cite:29][cite:31]

## 11. Рекомендованный план дальнейшей доработки

### Этап 1. Утвердить canonical structure

Нужно утвердить final canonical org-chart как обязательный документ. В нём должны быть закреплены все департаменты, их отделы, начальники, AI-работники, люди-дублёры, место в three lines of defence и основные связи.[cite:31]

### Этап 2. Сделать полную staff matrix

Для каждой роли нужна запись вида: `роль`, `AI-агент`, `уровень`, `человек-дублёр`, `HITL gate`, `reports to`, `allowed interactions`, `bounded context`, `evidence path in code`.[cite:29][cite:31]

### Этап 3. Закрыть SP-THIN

Необходимо довести до L2/L3 состояния `resolution/FSCS`, `wind-down`, `safeguarding-audit`, `incident_response/DORA`, потому что сейчас это самые очевидные structural holes between org and code.[cite:29]

### Этап 4. Формализовать executive layer

Нужно детально описать `CEO Orchestration Agent`, board committees pack logic, executive risk/finance/compliance cockpit и escalation grammar банка.[cite:31]

### Этап 5. Декомпозировать каждый департамент отдельно

После утверждения общей структуры каждый департамент нужно разбирать в отдельном спринте: внутренние отделы, роли, KPI, handoffs, queues, event contracts, risk points, data dependencies, human approvals.[cite:31]

## 12. Итоговая оценка

Проект EMI BANXE AI BANK уже находится на высокой стадии концептуально-архитектурной зрелости. В нём есть реальная сервисная карта, реальные доменные контуры, реальные agent passports, рабочие governance-артефакты и подтверждённые runtime-сервисы в ключевых зонах AML, reporting, finance, treasury, data quality и customer/business support.[cite:29][cite:31]

Однако проект ещё не завершён как полностью собранный «внутренний организм банка». Основные пробелы лежат не в отсутствии самой идеи, а в неполной формализации полной кадровой структуры, executive-level AI orchestration, interdepartment contracts и закрытии thin/open зон roadmap.[cite:29][cite:31]

Если говорить совсем просто, то сегодня EMI BANXE AI BANK уже выглядит как **полусобранный настоящий банк с сильным compliance/finance ядром**, а не как экспериментальный прототип. Но для перехода к полной операционной зрелости ему ещё нужна очень тщательная организационная сборка: утвердить полный штат AI-сотрудников и начальников, довести до конца независимые линии MLRO и Audit, закрыть thin service areas и формализовать верхний контур CEO/Board управления.[cite:29][cite:31]
