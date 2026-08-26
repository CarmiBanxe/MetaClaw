# Hermes Agent + Агентный стек BANXE: Полная карта интеграции для Factory и EMI AI Bank
## Контекст: физическая инфраструктура и два терминала
Проект работает на трёх физических машинах: **evo1**, **evo2** и **Legion**. На evo1 и evo2 развёрнут production AI inference stack: Ollama reasoning stack, LiteLLM gateway, OpenClaw orchestration, FastAPI compliance API, Jube transaction monitoring, Marble case-management, ClickHouse FCA audit trail, PostgreSQL, Redis, Presidio PII proxy, n8n workflow automation, Midaz Ledger, Hyperswitch. Software Factory оперирует через эти же терминалы — «центральный» (основная рабочая машина Software Factory Lead) и «правый» (evo1/evo2 с AI inference и compliance stack).

Hermes Agent, будучи **серверным агентом-процессом**, идеально вписывается в эту топологию: он разворачивается как systemd-сервис или Docker-контейнер на одной из машин, слушает команды из Telegram 24/7, имеет прямой SSH-доступ к остальным машинам через встроенный SSH-бекенд, и накапливает навыки (skills), которые делают его эффективнее с каждой итерацией.

***
## Полная карта агентного стека: кто что делает
| Агент | GitHub | Роль в Factory | Роль в BANXE AI Bank | Terminal |
|-------|--------|---------------|---------------------|----------|
| **OpenClaw** | openclaw/openclaw (353k ★) | Primary coding orchestration: ADR, specs, code, docs, DevOps | LiteLLM backend orchestration, OpenClaw orchestration на evo1/evo2 | Центральный |
| **MetaClaw** | aiming-lab/MetaClaw | Transparent proxy: skill injection, RL loop, cross-session memory | Повышает точность OpenClaw на 32%, task completion 8.25x | Центральный |
| **Ruflo** | ruvnet/ruflo | Swarm orchestration: 98 агентов, RaftBFT consensus, AgentDB HNSW | — (не часть banking stack) | Центральный |
| **IronClaw** | nearai/ironclaw | Security auditor: WASM sandbox, AES-256, TEE-secured inference | Смарт-контракт аудит, fee flows, KYC-adjacent compliance | Правый (evo2) |
| **NanoClaw** | qwibitai/nanoclaw | Test generator: TDD swarm, Jest/Vitest, 700M-параметровый агент | — | Центральный |
| **MiroFish** | 666ghj/MiroFish | Risk + Prediction Agent: OASIS simulation, seed extraction | VaR, Greeks, stress tests, sentiment aggregation, DSE | Правый (evo1) |
| **MicroFish** | microfish-org/microfish | Privacy layer: offline inference, compliance checks | MiCA/CASP offline scans, KYB validation, compliance | Правый (evo2) |
| **ClawArena** | aiming-lab/ClawArena | Evaluation harness: benchmark scoring, MetaClaw integration | CI pipeline benchmark reports | Центральный |
| **Hermes** | NousResearch/hermes-agent | 24/7 autonomous server: memory, self-improving skills, gateways | Customer AI, monitoring, compliance research | evo2 VPS (новый) |



***
## Центральный терминал: Software Factory Lead
Центральный терминал — рабочее место Software Factory Lead (Moriel), откуда координируется весь Factory workflow.
### OpenClaw — главный дирижёр (центральный)
OpenClaw — не просто coding assistant, это **control plane** всего Factory. Он управляет 5 специализированными ролями через Ruflo:

- **Architect** — ADR drafting, system design, interface contracts
- **Spec Writer** — OpenAPI specs, data schemas, AGENTS.md → Lock 0
- **Coder** — implementation, auto-shipping specs, test coverage ≥90%
- **Documentation Agent** — README, ADR updates, changelog
- **DevOps Agent** — CI/CD, Docker, k8s manifests, production deploy

**Как Hermes дополняет OpenClaw на центральном терминале:** Hermes и OpenClaw взаимодополняют друг друга на уровне архитектуры. ~20% production-пользователей запускают их вместе: OpenClaw как orchestrator (planning, decomposition), Hermes как execution specialist для fast/repeatable loops. В контексте Factory это означает:

```
Hermes (центральный, Telegram-интерфейс):
  → принимает задачу от Moriel в Telegram
  → анализирует, формирует контекст, проверяет AGENTS.md
  → вызывает OpenClaw CLI для spec-first implementation
  → следит за Lock 0 → Lock 1 → Lock 2 pipeline
  → уведомляет о результате обратно в Telegram
```

**Конкретный навык Hermes:** `factory-task-dispatcher` — Hermes запоминает паттерн «задача → YAML spec → Ruflo assign → Lock 0 → результат». После 20-30 итераций скорость формирования YAML спецификаций улучшается (Skill Generation Index).
### MetaClaw — обучающий proxy (центральный)
MetaClaw стоит прозрачным proxy-слоем перед OpenClaw, перехватывая все траектории и синтезируя навыки во время idle-периодов. Ключевые параметры конфигурации:

```yaml
agenttype: openclaw
skillmode: true          # Skill injection at each turn
rlmode: false            # Phase 1: collect 1000 trajectories first
scheduler:
  idlethresholdseconds: 300  # После 5 мин idle → synthesize skills
tinkercloud:
  enabled: false         # Phase 3: RL mode via cloud LoRA
projectmemory:
  enabled: true
  persistpath: .metaclaw/banxe-memory
```

**Hermes + MetaClaw:** У MetaClaw и Hermes похожая self-improving архитектура, но разные фокусы. MetaClaw специализируется на улучшении OpenClaw через RL-trajectories (BANXE кодовый контекст). Hermes строит generalizable skills через episodic memory. **Синергия:** Hermes может передавать MetaClaw обобщённые research-паттерны (например, «ADR decision framework для финтех проекта»), а MetaClaw конвертирует их в project-specific навыки OpenClaw.
### NanoClaw — TDD-генератор (центральный)
NanoClaw (700M параметров, 46 операций) — легковесный агент специально для TDD: генерирует Jest/Vitest тесты до реализации. Блокирующая роль в pipeline (NanoClaw test generation → OpenClaw coding, не наоборот).

**Hermes + NanoClaw:** Hermes может автоматически тригерить NanoClaw при обнаружении новой spec в `specs/` директории через SSH-монитор + cron:

```bash
# Hermes cron job на центральном терминале
hermes cron add "watch-specs" "*/5 * * * *" \
  "ssh evo1 'find /banxe/specs -newer /banxe/.last-nanoclaw-run -name *.yaml' && ruflo run --agent test-generator"
```
### Ruflo — Swarm координатор (центральный)
Ruflo — многоагентный роевой оркестратор с RaftBFT consensus, AgentDB (HNSW vector memory), zero-trust federation. 98 агентов, 60 команд, 30 skills.

```bash
ruflo deploy --swarm trading-core \
  --agents architect,coder,tester,security,docs,refactor \
  --consensus raft \
  --memory-backend agentdb
```

**Hermes + Ruflo:** Hermes не заменяет Ruflo — он работает на уровне выше. Hermes принимает high-level запрос от пользователя и формирует YAML-задачу для Ruflo. После завершения Ruflo swarm — Hermes собирает результат и отчитывается. Это устраняет необходимость вручную мониторить Ruflo через CLI.
### ClawArena — Benchmark judge (центральный, CI)
ClawArena запускается автоматически в CI pipeline, оценивает качество агентов через MetaClaw integration. KPI: +15% benchmark delta vs baseline per month.

**Hermes + ClawArena:** Hermes может подписаться на ClawArena webhook (или cron-проверять `benchmarks/` директорию) и уведомлять в Telegram при regression > 5%:

```
Hermes alert → "ClawArena: OpenClaw Coder score -8% за неделю. 
Причина: 3 failed spec-to-code tasks в баасе. Рекомендация: MetaClaw 
trajectory review на задачах BANXE-TRADING-018...020"
```

***
## Правый терминал: evo1/evo2 AI inference + Compliance Stack
Правый терминал — production inference машина с LiteLLM, Ollama, banking compliance stack.
### IronClaw — Security Auditor (evo2, изолированный WASM)
IronClaw работает в WASM sandbox с AES-256, TEE-secured inference. Зоны ответственности:

- Smart contract audit (fee contracts, FeeForwarder)
- API authentication (Kong partner keys)
- Payment flow security (wallet operations)
- MiCA fee disclosure validation

IronClaw блокирует (blocking: true) OpenClaw Coder — код не мержится без IronClaw PASS.

**Hermes + IronClaw:** Hermes **не должен иметь доступа** к зонам IronClaw — payment flows, fee contracts, AES-256 ключи. Правильная интеграция: Hermes только читает статус IronClaw audit reports из `audits/` директории (read-only SSH) и уведомляет о FAIL. Никакого write-доступа к WASM sandbox — это нарушит zero-trust модель.
### MiroFish — Prediction Engine (evo1)
MiroFish запускает OASIS multi-agent simulation с 100 параллельными мирами, горизонт 24 часа. Seed sources:

```yaml
financialsignals:
  - type: newsfeed (cryptopanic, coindesk, decrypt)
  - type: onchain (dune, nansen, glassnode)
  - type: social (twitter/x, reddit/crypto)
simulationparameters:
  parallelworlds: 100
  horizonhours: 24
```

MiroFish используется в двух ролях в BANXE: (1) Risk Agent — VaR, Greeks, stress tests; (2) Prediction Agent — sentiment score для DSE (`POST /v1/dss/recommend`).

**Hermes + MiroFish — ключевая синергия:** MiroFish производит prediction data, но **не имеет пользовательского интерфейса**. Hermes становится разговорным слоем над MiroFish для клиентов и операторов:

```
Клиент в Telegram → Hermes:
  → "Какой сейчас sentiment по BTC?"
Hermes → SSH → evo1 → python mirofish_query.py sentiment BTC
  → получает score: 0.12 (neutral), regime: neutral
  → components: news 0.08, onchain 0.19, social 0.09
Hermes → Telegram:
  → "BTC sentiment нейтральный (0.12/1.0). 
     On-chain активность выше среднего (0.19), 
     но новостной фон слабый. DSS рекомендует 
     осторожный spot swap не более Kelly 28%."
```

Это прямая реализация сценария из `POST /v1/dss/recommend` response, но через conversational interface с Honcho user memory — Hermes помнит risk profile конкретного клиента.
### MicroFish — Privacy Layer / Offline Compliance (evo2)
MicroFish обеспечивает offline inference без cloud exposure — критически важно для institutional BaaS API и compliance checks:

```bash
microfish serve --model local --port 9001 --no-cloud
```

Используется для: MiCA/CASP checks, KYB validation, fee disclosure validation, gamification compliance (MiCA Article 82).

**Hermes + MicroFish — compliance research layer:** MicroFish выполняет **локальные** compliance проверки. Hermes дополняет это внешним мониторингом регуляторного ландшафта:

| Задача | Исполнитель | Инструмент |
|--------|-------------|------------|
| MiCA checklist validation (существующий код) | MicroFish (offline) | `microfish serve --no-cloud` |
| Новые публикации FCA/EBA/ESMA | **Hermes** (background) | RSS + headless browser |
| ADR compliance pre-check (новые фичи) | **Hermes** (research) | Perplexity Search MCP |
| KYB document validation | MicroFish (offline) | локальная inference |
| Regulatory knowledge base updates | **Hermes** (накопление навыков) | skill distillation |

***
## Hermes: топология развёртывания в экосистеме BANXE
Hermes поддерживает несколько **profiles** на одной машине — каждый профиль это изолированный агент со своим config, memory, skills, SOUL.md. Это решает проблему context leakage между проектами.
### Recommended: 3 Hermes-профиля
**Профиль 1: `factory` (центральный терминал)**
```yaml
# SOUL.md
You are the Factory Coordinator for BANXE Software Factory.
You manage task dispatching, CI/CD monitoring, ADR research,
and sprint ledger. You NEVER touch payment flows or auth
without IronClaw PASS confirmation.
```
- Telegram gateway → инженерный Telegram-канал Software Factory Lead
- SSH tools: evo1, evo2 (read-only для audit logs)
- MCP: GitHub MCP, Perplexity Search API, Linear/Issues
- Skills: `cicd-watchdog`, `spec-yaml-generator`, `adr-research`, `sprint-ledger`

**Профиль 2: `banxe-ops` (evo2, 24/7)**
```yaml
# SOUL.md
You are BANXE Operations Monitor. You monitor compliance stack,
AML pipeline alerts, MiroFish prediction feeds, system health.
You are read-only on all banking data. ALL decisions require
human MLRO/COO approval per HITL-MATRIX.
```
- Telegram gateway → операционный канал
- SSH tools: evo1, evo2 (read-only)
- MCP: PostgreSQL read-only, ClickHouse query (audit trail читать, не писать)
- Skills: `aml-alert-monitor`, `mirofish-sentiment-query`, `system-health-check`

**Профиль 3: `client-advisor` (evo2, 24/7)**
```yaml
# SOUL.md
You are BANXE Client AI Advisor. You answer client questions
about their portfolio and trading recommendations.
You ALWAYS show MiCA disclaimer. You NEVER execute trades
autonomously. All recommendations require client confirmation.
```
- Telegram gateway → клиентский bot
- MCP: BANXE API `POST /v1/dss/recommend` (read/advisory only)
- Honcho user modelling: каждый клиент получает персонализированный профиль
- Skills: `dss-advisory-flow`, `portfolio-explain`, `risk-profile-update`

***
## Интеграция Hermes с каждым агентом: матрица взаимодействий
| Hermes → Агент | Тип интеграции | Конкретный механизм | Ограничения |
|----------------|---------------|---------------------|-------------|
| → OpenClaw | CLI delegation | `hermes delegate "openclaw run --spec pricing-api.yaml"` | Требует AGENTS.md context |
| → MetaClaw | Skill exchange | Hermes research skills → MetaClaw BANXE-specific training | Разные форматы skill storage |
| → Ruflo | Task dispatch | Hermes формирует YAML → `ruflo run --agent X --task Y` | Ruflo RaftBFT consensus независим |
| → IronClaw | Read-only monitor | SSH read `audits/ironclaw-report.json` | **НИКОГДА** write в WASM sandbox |
| → NanoClaw | Trigger via Ruflo | Hermes запускает Ruflo с agent=test-generator | NanoClaw blocking = ждать PASS |
| → MiroFish | Query interface | SSH + Python script → sentiment/prediction query | MiroFish advisory only, не auto-execute |
| → MicroFish | Monitor + research | Hermes мониторит `/var/log/microfish/` + внешний regulatory research | MicroFish offline = без cloud |
| → ClawArena | Report monitor | cron check benchmarks/ → Telegram alert на regression | Read-only CI artifact |



***
## Асинхронные Subagents Hermes: параллельные рабочие потоки Factory
С версии июня 2026 Hermes поддерживает **асинхронные subagents** через `async_delegation` toolset — делегированная работа не блокирует родительский chat. Это критически важно для Factory:

```
Hermes (parent, центральный Telegram):
  → получает задачу: "Phase 1 Sprint: Реализовать pricing API"
  
  async delegate → subagent-1: "ADR research: Heston ADI vs FNO"
  async delegate → subagent-2: "Dependency check: LI.FI SDK, 0x API"  
  async delegate → subagent-3: "MiCA pre-check: /v1/price/quote"

  [три subagent работают параллельно, каждый в своей SSH-сессии]
  
  когда все завершены → собирает результаты
  → формирует YAML spec для Lock 0
  → уведомляет Moriel: "Spec готова. Lock 0 проверка..."
```

Каждый subagent получает собственный session, tools, context — без загрязнения context window родителя.

***
## Project Isolation: 8 уровней для BANXE
Hermes поддерживает 8 уровней изоляции проектов. Для BANXE рекомендован **Tier 7-8**:

- **AGENTS.md per repo** — отдельный AGENTS.md в каждом репозитории (banxe-architecture, banxe-emi-stack) с явными инструкциями "не выходить за границы этого repo"
- **CWD isolation** — Hermes работает из `/projects/` директории с явным указанием current working directory
- **Scoped credentials** — отдельные GitHub fine-grained tokens для каждого repo, отдельный PostgreSQL read-only user
- **Tier 8 для production-critical** — banking stack: scoped repos, scoped channels, risky actions require approval, все API раздельные

***
## Сравнительная карта: что каждый агент делает лучше всего
```
SOFTWARE FACTORY PIPELINE (центральный терминал):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[HERMES gateway]     ← Moriel → Telegram
       ↓ формирует контекст, task dispatch
[PERPLEXITY]         ← research, ADR drafts  
       ↓ YAML spec
[OpenClaw Spec Writer] ← Lock 0: spec validation
       ↓ 
[NanoClaw]           ← TDD: тесты до кода
       ↓
[OpenClaw Coder]     ← Lock 1: implementation
       ↓
[IronClaw]           ← security audit (blocking)
       ↓
[MicroFish]          ← MiCA compliance (offline)
       ↓
[Human Sign-off]     ← Lock 2: GPG commit
       ↓
[CICD/Deploy]        ← OpenClaw DevOps
       ↓
[MetaClaw]           ← собирает trajectory
       ↓
[ClawArena]          ← benchmark delta
       ↓
[HERMES]             ← уведомляет результат
```

***
## EMI BANXE AI Bank: агенты и их домены
Физический стек на evo1/evo2 включает полноценный banking runtime. Ниже — как агенты Claw-семейства соотносятся с банковскими агентами из ORG-STRUCTURE:

| Banking Agent (ORG-STRUCTURE) | Технологический агент | Правило HITL |
|------------------------------|----------------------|--------------|
| AML-Analyst-v1 | MicroFish (offline) + FastAPI compliance | L2: MLRO gate на SAR |
| TxMonitorCore | Jube + Redis velocity | L1 auto / L2 on threshold |
| SanctionsScreeningAgent | Watchman + Banxe Screener | L1 auto / BLOCK auto |
| FraudScoringAgent | Jube (score ≥70 → HITL) | L2 Review |
| KYC-Specialist-v2 | Ballerine + MicroFish | L2: MLRO on HIGH/PROHIBITED |
| RiskOversightAgent | MiroFish + OpenClaw risk | L1 Auto (read-only monitor) |
| CustomerSupportAgent | **Hermes** client-advisor profile | L1 Auto (L2 on escalation) |
| MLPipelineAgent | OpenClaw devops + MetaClaw | L3: CRO+CTO sign-off |
| DeployAgent (production) | OpenClaw DevOps via Ruflo | L3: CTO must approve |



***
## Конфигурационные файлы: практическая интеграция
### Hermes config для factory профиля
```yaml
# ~/.hermes/profiles/factory/config.yaml
project: banxe-software-factory
model: claude-opus-4
provider: anthropic
tools:
  terminal: docker    # изолированный backend
  files: true
  web: true
  memory: true
mcpservers:
  - name: github
    command: npx @modelcontextprotocol/server-github
    env:
      GITHUB_TOKEN: ${GITHUB_FACTORY_TOKEN}  # scoped, read+PR только
  - name: perplexity
    command: npx perplexity-mcp-server
    env:
      PERPLEXITY_API_KEY: ${PERPLEXITY_KEY}
gateways:
  - telegram:
      token: ${TELEGRAM_FACTORY_BOT_TOKEN}
      allowed_users: [${MORIEL_TELEGRAM_ID}]
cron:
  - name: cicd-watchdog
    schedule: "*/5 * * * *"
    task: "Check GitHub Actions status for banxe repos. Alert if any workflow failed."
  - name: weekly-report  
    schedule: "0 9 * * MON"
    task: "Generate weekly Factory progress report: merged PRs, failed tasks, ClawArena delta."
```
### SOUL.md для banxe-ops профиля
```markdown
# BANXE Operations Monitor — SOUL.md

You are the operational monitoring assistant for EMI BANXE AI Bank.

## Core Identity
- Read-only access to all banking systems
- You NEVER execute trades, modify balances, or override compliance decisions
- ALL alerts requiring action must be escalated to human operators

## Hard Rules (ADR-049 compliant)
- L1 Auto: health checks, metric alerts, log monitoring
- L2 escalate: anomalies, threshold breaches → Telegram alert with context
- L3 human only: SAR, AML decisions, sanctions, production deploys

## Your Skills
- mirofish-sentiment: query evo1 MiroFish prediction feed
- system-health: check Ollama/LiteLLM/Jube/Marble status  
- compliance-calendar: FCA regulatory calendar reminders
- audit-trail-query: ClickHouse read-only queries
```

***
## Риски и ограничения интеграции
### Что Hermes НЕ должен делать в BANXE
- **SAR filing, PEP approvals, AML threshold changes** — только MLRO/CEO
- **Write-доступ к ledger, payment-core** — только через IronClaw signed commit + Lock 2
- **Автономное выполнение trades** — только advisory, клиент подтверждает
- **Production deploy** — только через CTO-approved GPG commit, Hermes только уведомляет
### Технические ограничения Hermes
- **Один LLM провайдер на профиль** — для разных задач нужны разные профили
- **Self-evaluation ненадёжна** — Hermes иногда переоценивает качество своих skills
- **Manual skill edits могут быть перезаписаны** — Curator может обновить вручную написанные skills
- **Pipeline processing (n8n-style)** отсутствует нативно — сложные конвейеры требуют Python-скриптов
- **Security documentation менее зрелая**, чем у OpenClaw — требует дополнительного hardening для banking
### Что использовать вместо Hermes для критических задач
| Задача | Не Hermes → Используй |
|--------|----------------------|
| MiCA offline compliance | MicroFish `--no-cloud` |
| Smart contract security | IronClaw WASM sandbox |
| Multi-repo code generation | OpenClaw + Ruflo swarm |
| RL-based skill improvement (код) | MetaClaw RL mode |
| Financial prediction/VaR | MiroFish OASIS simulation |
| Agent evaluation/benchmarking | ClawArena в CI pipeline |

***
## Приоритет внедрения: пошаговый план
### Неделя 1-2: Factory monitoring (нулевой риск)
1. Развернуть Hermes `factory` профиль на центральном терминале (Docker)
2. Настроить Telegram gateway → личный бот Software Factory Lead
3. Skill: `cicd-watchdog` — мониторинг GitHub Actions + Telegram алерты
4. Skill: `sprint-ledger` — задачи из Telegram → GitHub Issues
### Неделя 3-4: Research layer
5. Подключить Perplexity MCP → Hermes `factory`
6. Skill: `adr-research` — автономный еженедельный мониторинг open-source ландшафта
7. Skill: `spec-yaml-generator` — Lock 0 pre-check перед formal lint
### Месяц 2: Ops monitoring (read-only)
8. Развернуть Hermes `banxe-ops` профиль на evo2
9. SSH read-only к evo1/evo2 compliance stack logs
10. Skill: `mirofish-sentiment-query` — запросы к MiroFish через SSH
11. Skill: `system-health-check` — Ollama/LiteLLM/Jube/Marble health
### Месяц 3+: Client Advisory (после HITL review)
12. Развернуть Hermes `client-advisor` профиль
13. Подключить к `POST /v1/dss/recommend` (advisory only)
14. Honcho user modelling → персонализированные профили клиентов
15. MiCA disclaimer в каждом ответе — обязательно