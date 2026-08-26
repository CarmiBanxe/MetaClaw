# Hermes Agent: Разбор и применение в EMI BANXE AI Bank и Software Factory

## Что такое Hermes Agent

Hermes Agent — open-source автономный AI-агент от **Nous Research**, выпущенный в феврале 2026 года. За менее чем два месяца после запуска набрал 60,000+ GitHub stars, а к июню 2026 года — 22,000+ звёзд на GitHub при 142+ участниках сообщества. Hermes запускается как серверный процесс (CLI + web dashboard + нативное desktop-приложение с v0.16.0), работает 24/7 независимо от локальной машины пользователя.[^1][^2][^3]

**Ключевое отличие от Claude Code, OpenClaw, CrewAI и AutoGPT:** Hermes не является ни одноразовой coding-сессией, ни фреймворком для создания агентов. Это **постоянно работающий агент-сервер**, который обучается, запоминает и улучшает собственные навыки (skills) с каждым выполненным заданием.[^4][^1]

***

## Архитектура Hermes Agent

Hermes состоит из четырёх слоёв:[^5]

| Слой | Компонент | Функция |
|------|-----------|---------|
| **Gateways** (уши) | Telegram, Discord, Slack, WhatsApp, Signal, Email, SSH CLI | Каналы взаимодействия с пользователем |
| **Tools** (руки) | SSH, файловая система, headless Chrome, cron, STT/TTS | Влияние на внешний мир |
| **Skills** (опыт) | 89 предустановленных + 62 опциональных + 521 от сообщества | Переиспользуемые сценарии действий |
| **LLM API** (мозг) | OpenRouter, Nous Portal, Anthropic, GLM, Kimi, MiniMax, OpenAI | Любой совместимый с OpenAI провайдер |

### Память: многоуровневая архитектура

Hermes реализует три типа памяти, работающих совместно:[^6][^4]
- **Working memory** — контекст текущей задачи
- **Long-term semantic memory** — векторный поиск по накопленному опыту
- **Episodic logs** — хронология сессий с FTS5 full-text search и LLM-суммаризацией

Система **Honcho dialectic user modelling** строит эволюционирующий профиль пользователя через диалог — это означает, что Hermes становится объективно эффективнее по мере использования, а не просто хранит статичные заметки.[^3]

### Self-improving skills: как это работает

После каждой успешно выполненной сложной задачи Hermes автоматически:[^6][^5]
1. Анализирует последовательность шагов, которая привела к успеху
2. Создаёт документ-навык в формате Markdown (SKILL.md)
3. Сохраняет навык в `~/.hermes/skills/`
4. При следующей аналогичной задаче активирует навык автоматически

Это не маркетинг — в реальных тестах наблюдается рост Skill Generation Index и измеримое улучшение производительности на повторяющихся типах задач.[^1]

***

## Сравнение с агентами текущего стека BANXE

Проект уже использует агентный стек: OpenClaw, MetaClaw, Ruflo, IronClaw, NanoClaw, MiroFish, MicroFish. Hermes — это качественно другой инструмент, не конкурент, а дополнение.[^7]

| Характеристика | OpenClaw (текущий) | Hermes Agent |
|----------------|-------------------|--------------|
| Назначение | Coding orchestration | Автономный 24/7 агент-сервер |
| Память | File-based (MEMORY.md) + Active Memory Plugin | Multi-layer (semantic + episodic + FTS5) |
| Самообучение | Нет | ✅ Непрерывное, через skill distillation |
| Multi-model routing | ✅ (June 2026+) | Один провайдер на профиль |
| Безопасность | Высокая, June 2026 hardening | Container hardening, prompt injection scanner |
| Стоимость хостинга | ~$24/мес (managed) | ~$5/мес VPS |
| Coding tasks | ✅ Best-in-class | Умеренно |
| Персонализация | Базовая | ✅ Honcho user modelling |
| 24/7 autonomous ops | Требует настройки | ✅ Cloud-first дизайн |

**Вывод [ФАКТ]:** OpenClaw побеждает по ширине функционала и enterprise-готовности. Hermes побеждает по персонализации, накоплению опыта и стоимости запуска. Для BANXE они решают разные задачи.[^3]

***

## Применение Hermes в проекте EMI BANXE AI Bank

### 1. Customer AI Agent — живой 24/7 ассистент

Текущий стек BANXE предусматривает Customer AI Agent (squad в Team Topologies), CustomerSupportAgent (L1 Auto), EscalationAgent, ComplaintTriageAgent. Hermes идеально ложится в эту роль:[^8]

- Принимает обращения клиентов через **Telegram/WhatsApp/Slack** (нативные гейтвеи)
- **Помнит историю каждого клиента** через FTS5 session search — не нужно каждый раз объяснять контекст
- Использует Honcho для понимания паттернов поведения конкретного пользователя
- Escalation остаётся за человеком (COO gate согласно ORG-STRUCTURE)[^8]

**HITL compliance:** Hermes не нарушает ADR-049 D2 gate-chain — он может выполнять L1 Auto задачи (FAQ, роутинг тикетов), эскалируя всё выше L1 на человека согласно HITL-MATRIX.yaml.[^8]

### 2. Monitoring Agent — SRE и инфраструктурный мониторинг

В ORG-STRUCTURE описаны MonitoringAgent (L1 Auto, health checks) и необходимость 24/7 observability. Hermes напрямую предназначен для этого сценария:[^8]

- Навык **VPS/server monitoring** работает из коробки — проверяет RAM, CPU, дисковое пространство, открытые порты
- Отправляет алерты в Telegram при обнаружении аномалий
- Может запускать предопределённые runbook-команды (инцидент → диагностика → фикс)
- Поддерживает SSH-доступ к нескольким серверам (evo1, evo2, Legion — по конфигурации пользователя)[^8]

**Конкретный навык:** `incident-response-monitor` — автономная проверка каждые N минут + self-healing scripts при известных типах инцидентов.

### 3. Compliance Research Agent — предварительные MiCA/FCA проверки

MiCA/CASP compliance проверки сейчас выполняются через MicroFish (offline inference) + OpenClaw compliance. Hermes может дополнить эту цепочку как **исследовательский агент**:[^7]

- Мониторит новые публикации FCA, EBA, ESMA (через RSS + браузер) и уведомляет MLRO/CCO
- Делает первичные research-отчёты по новым требованиям (например, изменения в MLR 2017)
- Сохраняет навыки для типовых compliance-запросов — регуляторный knowledge base растёт автоматически

**HITL gate:** Любой compliance-вывод Hermes получает L3 MLRO sign-off согласно ORG-STRUCTURE. Hermes здесь — исследовательский ассистент, не decision-maker.[^8]

### 4. Decision Support Engine (DSE) — персональный финансовый ассистент клиента

DSE реализован через `POST /v1/dss/recommend` с utility scoring, Kelly calculator и stress tests. Hermes может стать **пользовательским слоем DSE**:[^9]

- Принимает запрос клиента в Telegram на естественном языке
- Транслирует intent в вызов `POST /v1/dss/recommend` (MCP tool)
- Получает utility-ranked recommendations и объясняет их клиенту на его языке
- Запоминает предпочтения клиента (risk profile, preferred venues) через Honcho — не нужно настраивать каждый раз

**Пример Flow:**
```
Клиент в Telegram: "Стоит ли сейчас купить BTC?"
Hermes → помнит risk profile клиента (balanced) из истории
Hermes → вызывает POST /v1/dss/recommend с portfolioValueUsd, currentPositions
Hermes → получает ranked recommendations, VaR, stress tests
Hermes → объясняет клиенту на его языке с ссылкой на MiCA disclaimer
```

### 5. Marketing & Campaign Automation

CampaignAgent (L1 Auto) и ContentAgent (L2 Review MLRO) описаны в org-структуре. Hermes с навыком `marketing-automation` может:[^8]

- Запускать content drafting по расписанию (cron)
- Анализировать cohort данные из ClickHouse через SSH-tool
- Формировать черновики для MLRO review (COBS 4 — AI may draft but NEVER auto-publish)

***

## Применение Hermes в проекте Software Factory

### 1. Hermes как Product Owner Research Layer (замена/дополнение Perplexity)

В Software Factory, Perplexity Agent API используется для task decomposition и ADR drafting. Hermes может взять на себя **persistent research** — в отличие от Perplexity, который отвечает на запросы, Hermes:[^7]

- Запускает background task: "Мониторь GitHub repos для open-source alternatives to LI.FI каждые 24 часа"
- Накапливает findings в skill library
- Уведомляет в Telegram при появлении новых релевантных репозиториев

**ADR research workflow:**
```
Hermes (background): мониторит HN, GitHub, Reddit для BANXE tech stack
Hermes: формирует weekly briefing по новым инструментам
Software Factory Lead: использует briefing для ADR decisions
```

### 2. Hermes как DevOps 24/7 Agent (CI/CD watchdog)

В Factory используются sleep/pause интервалы для CI/CD синхронизации. Hermes устраняет необходимость ручного мониторинга:[^8]

- Мониторит GitHub Actions статусы через GitHub MCP / REST API
- Уведомляет в Telegram при failed workflows
- Умеет перезапускать конкретные jobs после фикса (если есть GPG-подпись в рамках Double-Lock Protocol)
- Ведёт лог инцидентов CI/CD для post-mortem

**Навык:** `cicd-watchdog` — проверка каждые 5 минут, алерты с контекстом (какой шаг упал, ошибка, последний commit).

### 3. Hermes как Sprint Ledger & Tracking Agent

В текущем workflow задокументировано ведение sprint ledger. Hermes берёт на себя операционный overhead:[^8]

- Создаёт задачи в Linear/GitHub Issues из Telegram-сообщений через MCP/Composio
- Отслеживает статус открытых задач и напоминает об overdue
- Генерирует weekly progress report для BANXE Software Factory
- Использует session recall для понимания исторического контекста задачи без загрузки всей истории

### 4. Hermes как Quality Gate Pre-checker

Перед тем как задача попадает на Lock 0 spec lint → Ruflo, Hermes может выполнить предварительный sanity check:

- Проверяет что YAML spec синтаксически корректен
- Проверяет что acceptance criteria присутствуют
- Проверяет наличие ADR ссылки и OpenAPI ref
- Отправляет pre-check report в Telegram до запуска formal lint pipeline

Это снижает количество "заваленных" первых Lock 0 попыток — цель 80% pass rate первой попытки.[^7]

***

## Оптимальная интеграционная архитектура Hermes в BANXE

### Топология развёртывания

```
HERMES AGENT INSTANCE (VPS / evo2)
├── Gateway: Telegram (основной канал)
├── Gateway: SSH CLI (evo1, evo2, Legion)
├── Gateway: Slack (engineering channels)
│
├── MCP Tools:
│   ├── GitHub MCP → CI/CD monitoring
│   ├── PostgreSQL MCP → банковский стек данных (read-only)
│   ├── Composio → Linear, Jira, Slack
│   └── BANXE API → POST /v1/dss/recommend (read-only, advisor role)
│
├── Skills Library (накапливается):
│   ├── banxe-incident-response
│   ├── cicd-watchdog-github
│   ├── mica-compliance-research
│   ├── dss-client-advisory
│   └── sprint-ledger-manager
│
└── LLM Backend: Claude Sonnet (через OpenRouter)
    Fallback: GLM-5.1 / DeepSeek для бюджетных задач
```

### HITL-совместимость с ORG-STRUCTURE

Hermes в BANXE работает строго в рамках существующей HITL-матрицы:[^8]

| Hermes Task | Autonomy Level | Human Gate |
|-------------|---------------|------------|
| Customer FAQ, ticket routing | L1 Auto | Нет |
| Monitoring alerts, CI/CD alerts | L1 Auto | Нет |
| Compliance research drafts | L2 Review | MLRO |
| DSE recommendations | L2 Review | Клиент сам принимает решение |
| Production deploy triggers | L3 | CTO must approve |
| SAR, PEP, AML thresholds | ❌ Out of scope | MLRO/CEO only |

### Безопасность: что нужно учесть

- Hermes должен работать с **read-only доступом** к банковским данным — никакого write-доступа к payment-core, KYC, ledger без IronClaw security sign-off
- Credentials хранятся в `.env` файле на изолированном VPS — не на машинах с banking stack
- Docker backend (`hermes config set terminal.backend docker`) — обязательно для production, ограничивает воздействие на сервер[^5]
- Prompt injection scanner встроен в Hermes — но внешние skills требуют проверки перед установкой

***

## Лучшее использование ресурса Hermes: Приоритизация

По оценке совокупности ROI, сложности реализации и соответствия проекту:

### Tier 1 — Быстрый старт (неделя 1-2)

1. **CI/CD Watchdog** — немедленная ценность для Software Factory, нет compliance рисков, навык создаётся за 1-2 сессии
2. **Telegram DevOps assistant** — замена ручного мониторинга evo1/evo2, Hermes знает SSH, это его native use case[^5]

### Tier 2 — Высокое ROI (неделя 3-6)

3. **Customer Support L1** — снижает нагрузку на CustomerSupportAgent, Hermes обучается на паттернах клиентских запросов, улучшается со временем
4. **Compliance Research Monitor** — FCA/EBA RSS мониторинг + уведомления MLRO, снижает регуляторный риск

### Tier 3 — Стратегический (месяц 2+)

5. **DSE Client Advisory Interface** — персонализированный финансовый ассистент, Honcho строит long-term профиль каждого клиента
6. **Product Owner Research Agent** — автономный мониторинг open-source ландшафта для ADR decisions

***

## Ограничения и риски

- **[ФАКТ]** Hermes не поддерживает native multi-model routing — один LLM провайдер на профиль. Для разных задач нужны отдельные профили[^3]
- **[ФАКТ]** Security documentation менее зрелая, чем у OpenClaw — в banking context требует дополнительного аудита[^3]
- **[ВЫВОД]** Hermes не заменяет IronClaw для security-critical операций и MicroFish для offline compliance inference — это complementary layer
- **[ФАКТ]** Pipeline processing (как n8n) у Hermes отсутствует "из коробки" — сложные конвейеры требуют Python-скриптов поверх Hermes CLI[^5]
- **[НЕИЗВЕСТНО]** Производительность Honcho user modelling при большой базе клиентов (тысячи профилей) на одном instance — не задокументирована

---

## References

1. [Hermes Agent: Self-Hosted AI That Never Forgets You (2026)](https://www.aibuilderclub.com/blog/hermes-nous-research-self-improving-agent) - Hermes Agent is a self-hosted, open-source autonomous AI agent built by Nous Research that accumulat...

2. [Hermes Agent: The Practitioner's Reference (2026)](https://blakecrosley.com/guides/hermes) - TL;DR: Hermes Agent is an open-source self-improving AI agent from Nous Research. It runs as a CLI a...

3. [OpenClaw vs Hermes Agent: 2026 Comparison (Updated June)](https://flowtivity.ai/blog/openclaw-vs-hermes-agent-comparison/) - Updated June 2026: Honest comparison of OpenClaw and Hermes Agent covering multi-model orchestration...

4. [The Best Open Source AI Agents in 2026: A Developer's Honest ...](https://www.tencentcloud.com/techpedia/144032) - Hermes Agent is the newest major entry in this comparison, and arguably the most architecturally amb...

5. [Дрессировка и воспитание личного автономного AI‑агента на ...](https://habr.com/ru/articles/1032656/) - В этой статье: подробный разбор архитектуры Hermes, установка и первичная настройка (для чайников), ...

6. [Hermes Agent: помощник NocoBase, который учится по ходу ...](https://docs.nocobase.com/ru/ai/hermes-agent/) - Hermes Agent — ИИ агент с открытым исходным кодом для самостоятельного хостинга: автоматически превр...

7. [BANXE-AI-Trading-Platform-Master-plan-realizatsii-cherez-Software-Factory.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/101434432/f0ef844f-c2af-45bc-a30a-9cfde87d2776/BANXE-AI-Trading-Platform-Master-plan-realizatsii-cherez-Software-Factory.md?AWSAccessKeyId=ASIA2F3EMEYER35EGS4G&Signature=H285GsFxAOmieAu0uFrpZOzGBL0%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIC85MH%2BsvytLMuZQf5oDClQ6jD2%2FyTKTPXh0RdK8UvZ8AiBC2zHgmnADdRbPVCdW%2B0RPPqp8I9fVm3Y%2FfxrZjkxVOCrzBAhUEAEaDDY5OTc1MzMwOTcwNSIMkoMehpdH5jW%2FrZyaKtAEVNEtwkwhHNW8lCJ7if5gRHwDbQowyN51E4%2B3c9PVEQPgix%2FL9t1kkuLKK91U3d7NXb29y7xU%2FRuD6pdxep6U4R%2BRuYX0PjPGNVpQGaiElFQtd8WkL%2Batj73lWLL1zAcC4a6wz626SV3%2BUzqHGaBHM21WsXl2Az5hKSt4HUL1RCG1WiH9Uyei4BbuWDuQcXMzssvSfsMYU8l1KW0nAOZZQYpgyUifyDKs86ncRVeRNNFi3ifsbgh2t9pZQtggVpvTPGQg1GczD0%2BIUApd%2F%2FFKpbjIPk85B2rJ6nHYImdwG4YEYfFYAgrCA%2FxU19Eov3xz0X59SHYq5omSLwbdGMoNyKX485Mz2gMATjx%2F9eIN77eVPliMGXm%2FI%2BvNqBlSAv9HvT%2B14Ucg%2F74pK6qh84GsYhY7eYBEtVoS%2Fa9NQxOmN%2FuF3YjjMXz68QnvGUUuj0ldPguEL0Qru3e0kTeOgIDNR1rk6MILUfAU9DNOWP%2Fyds0CDNdwrza1DrpzHTS2a8e9xgb6GR%2FmH22QBM6jXJRlSZ3c%2Fwas6exvwhtqxuSMJiPVw2IeJBa7mPxmkUAl307i9yOv1azYlDKer7g%2BEFe3n934eBoEbryWlnE9rz0oFoV0GAMIYT8C%2F4I%2BpVtabVZOXCZgFHxpVpwlHTR2CEj4ZMFZT6qBLiws9JJVdJiApFpuZd5s8lKwXMfnex%2By7ojJ5GKsPmWcq3esxIp5ehMHvNgrEygID0zZgFCTxEBNce%2BFKqhS1dMD1FOB6LPXtYAjXt4FHi2CESEZuIqURujSgDCU8%2FXRBjqZAVLJe8UGaYdDSo963idSiwA7KlVRggJh2Jeo7BYPuYJGUlC06La7OSThuDKRIQLPTDVTl0%2F2NXhvgRLXncv6qMwqsGvyB7QXPAprREtVQAW94KOHSJ64JAJLZOFbIJxiTUsVfzNp2ZCRtCWNW10WaxNtBxIy4WWhN%2BV%2Bjqq14DkUoORJlkmpDs6bB0cz%2FI5yJ5AV%2BjxpK%2FlI6w%3D%3D&Expires=1782417255) - Software Factory , , BaaS API EMI BANXE AI Bank. Single Source of Truth , , Perplexity-, TITLE BANXE...

8. [ORG-STRUCTURE.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/101434432/64e66c86-2a17-43bc-9e17-8a8f70058dd2/ORG-STRUCTURE.md?AWSAccessKeyId=ASIA2F3EMEYER35EGS4G&Signature=2IAkgVHB9r%2BCDXpRh4Oyd8y%2BhsM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIC85MH%2BsvytLMuZQf5oDClQ6jD2%2FyTKTPXh0RdK8UvZ8AiBC2zHgmnADdRbPVCdW%2B0RPPqp8I9fVm3Y%2FfxrZjkxVOCrzBAhUEAEaDDY5OTc1MzMwOTcwNSIMkoMehpdH5jW%2FrZyaKtAEVNEtwkwhHNW8lCJ7if5gRHwDbQowyN51E4%2B3c9PVEQPgix%2FL9t1kkuLKK91U3d7NXb29y7xU%2FRuD6pdxep6U4R%2BRuYX0PjPGNVpQGaiElFQtd8WkL%2Batj73lWLL1zAcC4a6wz626SV3%2BUzqHGaBHM21WsXl2Az5hKSt4HUL1RCG1WiH9Uyei4BbuWDuQcXMzssvSfsMYU8l1KW0nAOZZQYpgyUifyDKs86ncRVeRNNFi3ifsbgh2t9pZQtggVpvTPGQg1GczD0%2BIUApd%2F%2FFKpbjIPk85B2rJ6nHYImdwG4YEYfFYAgrCA%2FxU19Eov3xz0X59SHYq5omSLwbdGMoNyKX485Mz2gMATjx%2F9eIN77eVPliMGXm%2FI%2BvNqBlSAv9HvT%2B14Ucg%2F74pK6qh84GsYhY7eYBEtVoS%2Fa9NQxOmN%2FuF3YjjMXz68QnvGUUuj0ldPguEL0Qru3e0kTeOgIDNR1rk6MILUfAU9DNOWP%2Fyds0CDNdwrza1DrpzHTS2a8e9xgb6GR%2FmH22QBM6jXJRlSZ3c%2Fwas6exvwhtqxuSMJiPVw2IeJBa7mPxmkUAl307i9yOv1azYlDKer7g%2BEFe3n934eBoEbryWlnE9rz0oFoV0GAMIYT8C%2F4I%2BpVtabVZOXCZgFHxpVpwlHTR2CEj4ZMFZT6qBLiws9JJVdJiApFpuZd5s8lKwXMfnex%2By7ojJ5GKsPmWcq3esxIp5ehMHvNgrEygID0zZgFCTxEBNce%2BFKqhS1dMD1FOB6LPXtYAjXt4FHi2CESEZuIqURujSgDCU8%2FXRBjqZAVLJe8UGaYdDSo963idSiwA7KlVRggJh2Jeo7BYPuYJGUlC06La7OSThuDKRIQLPTDVTl0%2F2NXhvgRLXncv6qMwqsGvyB7QXPAprREtVQAW94KOHSJ64JAJLZOFbIJxiTUsVfzNp2ZCRtCWNW10WaxNtBxIy4WWhN%2BV%2Bjqq14DkUoORJlkmpDs6bB0cz%2FI5yJ5AV%2BjxpK%2FlI6w%3D%3D&Expires=1782417255) - IL-065 Developer Plane banxe-architecture Created 2026-04-09 Author Claude Code Purpose Canonical or...

9. [BANXE_MASTER_RESEARCH.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/101434432/b4a438aa-1527-4be7-847a-d7889a716616/BANXE_MASTER_RESEARCH.md?AWSAccessKeyId=ASIA2F3EMEYER35EGS4G&Signature=9dGdR5YIypDwtXglZCgfmw4seZs%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIC85MH%2BsvytLMuZQf5oDClQ6jD2%2FyTKTPXh0RdK8UvZ8AiBC2zHgmnADdRbPVCdW%2B0RPPqp8I9fVm3Y%2FfxrZjkxVOCrzBAhUEAEaDDY5OTc1MzMwOTcwNSIMkoMehpdH5jW%2FrZyaKtAEVNEtwkwhHNW8lCJ7if5gRHwDbQowyN51E4%2B3c9PVEQPgix%2FL9t1kkuLKK91U3d7NXb29y7xU%2FRuD6pdxep6U4R%2BRuYX0PjPGNVpQGaiElFQtd8WkL%2Batj73lWLL1zAcC4a6wz626SV3%2BUzqHGaBHM21WsXl2Az5hKSt4HUL1RCG1WiH9Uyei4BbuWDuQcXMzssvSfsMYU8l1KW0nAOZZQYpgyUifyDKs86ncRVeRNNFi3ifsbgh2t9pZQtggVpvTPGQg1GczD0%2BIUApd%2F%2FFKpbjIPk85B2rJ6nHYImdwG4YEYfFYAgrCA%2FxU19Eov3xz0X59SHYq5omSLwbdGMoNyKX485Mz2gMATjx%2F9eIN77eVPliMGXm%2FI%2BvNqBlSAv9HvT%2B14Ucg%2F74pK6qh84GsYhY7eYBEtVoS%2Fa9NQxOmN%2FuF3YjjMXz68QnvGUUuj0ldPguEL0Qru3e0kTeOgIDNR1rk6MILUfAU9DNOWP%2Fyds0CDNdwrza1DrpzHTS2a8e9xgb6GR%2FmH22QBM6jXJRlSZ3c%2Fwas6exvwhtqxuSMJiPVw2IeJBa7mPxmkUAl307i9yOv1azYlDKer7g%2BEFe3n934eBoEbryWlnE9rz0oFoV0GAMIYT8C%2F4I%2BpVtabVZOXCZgFHxpVpwlHTR2CEj4ZMFZT6qBLiws9JJVdJiApFpuZd5s8lKwXMfnex%2By7ojJ5GKsPmWcq3esxIp5ehMHvNgrEygID0zZgFCTxEBNce%2BFKqhS1dMD1FOB6LPXtYAjXt4FHi2CESEZuIqURujSgDCU8%2FXRBjqZAVLJe8UGaYdDSo963idSiwA7KlVRggJh2Jeo7BYPuYJGUlC06La7OSThuDKRIQLPTDVTl0%2F2NXhvgRLXncv6qMwqsGvyB7QXPAprREtVQAW94KOHSJ64JAJLZOFbIJxiTUsVfzNp2ZCRtCWNW10WaxNtBxIy4WWhN%2BV%2Bjqq14DkUoORJlkmpDs6bB0cz%2FI5yJ5AV%2BjxpK%2FlI6w%3D%3D&Expires=1782417255) - -. Single Source of Truth , , , BaaS-, - Software Factory. 14 2026 Perplexity AI Moriel Carmi --- TI...

