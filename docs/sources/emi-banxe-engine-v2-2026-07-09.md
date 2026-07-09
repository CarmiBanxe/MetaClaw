EMI BANXE AI BANK — Идеальный Open Source Движок Банка-ИИ-Агента: Архитектура, Математика, Мировой Опыт
Дополнение к двум предыдущим исследованиям
Исполнительное резюме
Настоящий документ отвечает на ключевой вопрос проекта EMI BANXE AI BANK: какой именно открытый стек является оптимальным движком банка-ИИ-агента нового поколения? Опираясь на оба предыдущих исследования (европейский и азиатско-латиноамериканский опыт) и проведя новый глубокий поиск, исследование синтезирует:

Детальное сравнение Manus-подобных агентных движков и их open source альтернатив

Математические основы, на которых работают лучшие банковские AI-движки мира

Эталонную «слоистую» архитектуру движка BANXE — полностью на open source

Конкретные репозитории и их рейтинги звёзд, лицензии и производственный статус

Стратегию интеграции в «Фабрику» BANXE (CI/CD / GitHub Agentic Workflows)

Часть I: Manus и Manus-подобные движки — Анализ для BANXE
1.1 Что такое Manus AI и почему он важен для понимания движка
6 марта 2025 года китайская компания Monica.im выпустила Manus AI — заявив его «первым в мире универсальным ИИ-агентом». На GAIA-бенчмарке Manus показал 86,5% (базовый уровень), что превосходит OpenAI Deep Research. Архитектура Manus: централизованный «executive agent» координирует 29 встроенных инструментов (браузер, файловые операции, аналитика); работает на Claude 3.5 Sonnet и тонко настроенных Qwen-моделях.

Спустя несколько часов после анонса Manus команда MetaGPT из четырёх разработчиков за 3 часа создала OpenManus — open source реплику ключевой функциональности. На GitHub OpenManus немедленно набрал 16 000+ звёзд (затем 33 000+ за 10 дней). Ключевое техническое различие:

Параметр	Manus AI	OpenManus
Архитектура	Meta-оркестратор (динамически переопределяет агент-пайплайны)	Фиксированная топология агентов
Исходный код	Закрытый	Открытый MIT
Развёртывание	Облако (Monica.im)	Локально или облако, Docker
Стоимость	Платная подписка	Бесплатно (только API-ключи)
Настраиваемость	Ограничена	Полная через исходный код
GAIA-бенчмарк	86,5%	74,3%
Зрелость	Production-ready	Активно развивается
Архитектура OpenManus — три слоя:

Agent — поведенческая логика (PlanningAgent, ToolCallAgent)

Tool — инструменты (браузер, код, файловые операции)

Memory — контекст и история сессии

Вывод для BANXE: [ФАКТ] OpenManus — мощная основа, но недостаточно специализированная для банковских задач. Она является скелетом, на который надевается банковский стек, а не готовым финансовым движком.

1.2 Наиболее продвинутые Manus-подобные альтернативы для банка
Проект	Звёзды / Лицензия	Ключевые особенности	Пригодность для банка
OpenManus	33k+ / MIT	3-слойная архитектура, ToolCallAgent	✅ Основа агентного движка
DeerFlow 2.0	20k+ / MIT	LangGraph, SuperAgent Harness, Docker-песочницы	✅✅ Наиболее подходящий
Suna	~5k / MIT	Generalist AI Agent, browser + tools	✅ Для исследовательских задач
AgenticSeek	~10k / Apache 2.0	Полностью локальный, offline-first	✅✅ GDPR-compliant for EU
1.3 DeerFlow 2.0 (ByteDance) — Лучший open source «Manus» для BANXE
DeerFlow (Deep Exploration and Efficient Research Flow) — open source SuperAgent Harness от ByteDance, MIT-лицензия, версия 2.0 выпущена в феврале 2026 года. Перестроен с нуля на LangGraph 1.0, набрал 20 000+ GitHub-звёзд за неделю.

Архитектура DeerFlow 2.0:

text
Supervisor Agent
    ├── Coordinator Agent
    ├── Planner Agent
    ├── Researcher Agent (web search, RAG, MCP tools)
    ├── Coder Agent (Python в Docker-sandbox)
    └── Reporter Agent (генерирует отчёты / презентации / аудио)
Ключевые технические характеристики:

Построен на LangGraph (state machine-графы вместо цепочек)

Docker/Kubernetes изоляция для каждого sub-агента

Долгосрочная память через RAGFlow, Qdrant, Milvus

Нативная MCP-поддержка для тысяч готовых инструментов

Поддержка 10+ LLM (GPT-5, DeepSeek, Kimi, Gemini)

Интеграция с Claude Code, Codex, Cursor

Применение DeerFlow в BANXE: Researcher Agent → финансовая аналитика; Coder Agent → генерация отчётов в песочнице; Reporter Agent → персонализированные PDF-отчёты для клиентов; MCP-интеграция → подключение банковских API без кастомного кода.

1.4 AgenticSeek — Полностью локальный движок для GDPR-compliance
AgenticSeek — «полностью локальный, голосо-ориентированный AI-агент». Работает без интернета, все данные остаются на сервере. Идеален для сценариев BANXE, где клиентские данные не могут покидать EU-инфраструктуру — требование GDPR. Поддерживает Ollama (локальные LLM), File Manager, Code Executor, Web Scraper — все локально.

Часть II: Математические основы движка — Что работает в production банках
2.1 Трансформеры на транзакционных данных: PRAGMA и nuFormer
Самое важное математическое открытие последних 18 месяцев: финансовые транзакции имеют ту же структуру, что и язык — они последовательны, контекстуальны и предсказуемы. Это позволяет применять трансформеры GPT/BERT к банковским данным.

PRAGMA (Revolut + NVIDIA, арXiv апрель 2026):

Архитектура: двухветвевой трансформер-энкодер

Profile State Encoder — для статических атрибутов пользователя

Event Encoder — для последовательностей событий (транзакции, клики)

History Encoder — слой слияния обеих веток

Ключевая инновация токенизации: каждое поле финансового события кодируется тройкой (semantic_key, typed_value, temporal_coordinate):

Числовые значения → перцентильные buckets (сохраняет порядок, предотвращает взрыв токенов)

Категориальные → один токен

Текст → BPE

Время → дважды: log-секунды + синусоиды (hour-of-day, day-of-week, day-of-month)

Обучение: masked language modelling с тремя источниками маскирования:

15% стандартная маскировка токенов

10% маскировка целых событий (учит, что amount транзакции можно восстановить из merchant + time + контекст)

10% семантическая маскировка типов

Результаты PRAGMA на производстве:

Кредитный скоринг: +130% PR-AUC vs baseline

Fraud detection: +65% recall

Recommendation: +40.5% mAP

Обучено на 24 миллиардах событий, 26 миллионах пользователей, 111 стран

Семейство моделей: PRAGMA-10M (реалтайм fraud), PRAGMA-100M (кредит), PRAGMA-1B (precision analysis)

nuFormer (Nubank, arXiv июль 2025):

Архитектура: GPT-style decoder (в отличие от BERT-стиля Revolut) — causal next-token prediction, затем joint fusion с DCNv2 tabular network:

nuFormer
(
𝑥
)
=
DCNv2
(
𝑥
tabular
)
⊕
GPT-decoder
(
𝑥
seq
)
nuFormer(x)=DCNv2(x 
tabular
​
 )⊕GPT-decoder(x 
seq
​
 )
Ключевая гипотеза (подтверждена): «Модели трансформеров для транзакционных данных захватывают сложные временны́е паттерны лучше, чем ручная feature engineering».

Производственные результаты:

Задеплоен для 131 миллиона клиентов

+1,25% test AUC на рекомендательных задачах

4,4% снижение оттока пользователей в продакшне

TransactionGPT (arXiv, ноябрь 2025) — 3D-трансформер:

Разработан внутри одной из крупнейших платёжных сетей мира. Новация: 3D-Transformer архитектура специально для динамики транзакционных данных:

Ось 1: временна́я последовательность

Ось 2: семантические атрибуты транзакции

Ось 3: отношения между транзакциями (граф)

Обучен на данных биллионного масштаба; значительно превосходит production baseline по детекции аномалий. Быстрее и точнее, чем fine-tuned LLM на той же задаче.

WeChat Pay GPT (arXiv, декабрь 2023):

Команда Tencent/WeChat Pay — autoregressive GPT для fraud detection в платёжных системах. Решает «token explosion» через реконструкцию поведенческих последовательностей. Differential convolution для anomaly detection. Масштабируется до одного из крупнейших online-ретейлеров Китая.

Практические выводы для BANXE:

Encoder-based (BERT/PRAGMA) лучше для discriminative задач (fraud, credit, churn)

Decoder-based (GPT/nuFormer) лучше для generative и next-event prediction

Числа токенизировать через перцентильные buckets — не через BPE

Joint fusion (transformer + tabular DCN) — оптимум для банка с mixed data

2.2 Graph Neural Networks — математика AML и связанного fraud
Традиционные модели fraud detection анализируют каждую транзакцию изолированно. GNN видят всю сеть пользователь–мерчант–транзакция и находят скрытые паттерны.

Heterogeneous GNN для fraud (arXiv, апрель 2025):

Строится гетерогенный граф: узлы — users, merchants, transactions. Применяется Graph Attention Mechanism для динамического взвешивания рёбер:

𝑒
𝑖
𝑗
=
LeakyReLU
(
𝑎
𝑇
[
𝑊
ℎ
𝑖
∥
𝑊
ℎ
𝑗
]
)
e 
ij
​
 =LeakyReLU(a 
T
 [Wh 
i
​
 ∥Wh 
j
​
 ])
𝛼
𝑖
𝑗
=
exp
⁡
(
𝑒
𝑖
𝑗
)
∑
𝑘
∈
𝑁
(
𝑖
)
exp
⁡
(
𝑒
𝑖
𝑘
)
α 
ij
​
 = 
∑ 
k∈N(i)
​
 exp(e 
ik
​
 )
exp(e 
ij
​
 )
​
 
Temporal Decay Mechanism учитывает свежесть паттерна:

ℎ
𝑖
(
𝑡
)
=
∑
𝑗
∈
𝑁
(
𝑖
)
𝛼
𝑖
𝑗
⋅
𝑒
−
𝜆
Δ
𝑡
𝑖
𝑗
⋅
𝑊
ℎ
𝑗
h 
i
(t)
​
 = 
j∈N(i)
∑
​
 α 
ij
​
 ⋅e 
−λΔt 
ij
​
 
 ⋅Wh 
j
​
 
Результаты на IEEE-CIS Fraud Detection dataset: превосходит GCN, GAT и GraphSAGE по точности и OC-ROC.

FraudGNN-RL — комбинация GNN + Reinforcement Learning:

Инновационный фреймворк: GNN захватывает паттерны, RL динамически адаптирует порог обнаружения. Deep Q-Network адаптирует feature importance под эволюцию мошеннических схем:

𝑄
(
𝑠
,
𝑎
;
𝜃
)
=
𝑟
+
𝛾
max
⁡
𝑎
′
𝑄
(
𝑠
′
,
𝑎
′
;
𝜃
−
)
Q(s,a;θ)=r+γ 
a 
′
 
max
​
 Q(s 
′
 ,a 
′
 ;θ 
−
 )
Результаты:

F1-score: 97,3% (снижение false positives на 31%)

Устойчивость к adversarial attacks и concept drift

Federated Learning вариант для collaboration между банками

ASA-GNN — адаптивный sampling для fraud:

Ключевая проблема: преступники имитируют поведение честных клиентов. ASA-GNN решает через:

Cosine similarity filtering: убирает шумовые соседние узлы

Entropy-based diversity metric: обнаруживает маскировку мошенников

Multi-hop neighborhood: находит связанных мошенников через 2–3 рукопожатия

Применение в BANXE: GNN-модель хранится в Qdrant как граф-embedding; каждая новая транзакция добавляется в граф и мгновенно оценивается; AML Agent вызывает GNN-сервис через MCP tool.

2.3 Federated Learning — математика GDPR-compliant обучения
Ключевая проблема в EU: GDPR запрещает передавать клиентские данные третьим лицам для обучения моделей. Federated Learning решает это математически:

Горизонтальный federated learning (FedAvg + FedKT алгоритм):

Вместо централизованного датасета: каждый участник (банк) обучает локальную модель 
𝑤
𝑘
w 
k
​
  на своих данных. Центральный сервер агрегирует только градиенты:

𝑤
𝑡
+
1
=
∑
𝑘
=
1
𝐾
𝑛
𝑘
𝑛
𝑤
𝑘
𝑡
+
1
w 
t+1
​
 = 
k=1
∑
K
​
  
n
n 
k
​
 
​
 w 
k
t+1
​
 
где 
𝑛
𝑘
n 
k
​
  — размер датасета k-го банка, 
𝑛
=
∑
𝑛
𝑘
n=∑n 
k
​
 .

FedKT (Federated Knowledge Transfer) дополнительно дистиллирует знания через fine-tuning + knowledge distillation, решая проблему Non-IID данных между банками.

Privacy-Preserving Federated Learning с Differential Privacy (Nature, 2026):

Добавление контролируемого шума (Gaussian mechanism) с формально подтверждённым privacy budget:

𝑀
(
𝑥
)
=
𝑓
(
𝑥
)
+
𝑁
(
0
,
𝜎
2
𝐼
)
M(x)=f(x)+N(0,σ 
2
 I)
Privacy budget Rényi Differential Privacy: 
𝜖
=
8
,
65
ϵ=8,65 — оптимальный баланс privacy-utility (точность ≈ 87–90%).

Homomorphic Encryption (HE-FL): вычисления над зашифрованными данными. Точность: ≈90% при полной шифровке.

FATE (WeBank, open source Apache 2.0): Production-ready реализация всех перечисленных алгоритмов для финансовых организаций. Используется 1000+ организациями. Реализует Private Set Intersection через RSA-шифрование для cross-bank credit scoring без раскрытия данных.

VaultGemma (Google, open source сентябрь 2025):

Первый в мире differentially private LLM (1B параметров, Gemma 2 архитектура). Обучен под differential privacy framework «от нуля». Open source: веса и код на Hugging Face и Kaggle. Пригоден для regulated industries (финансы, здравоохранение).

2.4 Reinforcement Learning для агентных решений банка
FinRL (AI4Finance Foundation, MIT):

Первый open source фреймворк для финансового RL. Gym-style market environments, множество DRL алгоритмов, полный pipeline: train-test-trade для акций, крипто, портфелей.

FinRL-DeepSeek (arXiv, февраль 2025):

LLM-Infused Risk-Sensitive RL: DeepSeek LLM генерирует market signals, которые поступают в RL-агента как дополнительный state:

𝑠
𝑡
=
(
𝑝
𝑡
,
𝑓
𝑡
,
LLM_signal
𝑡
)
s 
t
​
 =(p 
t
​
 ,f 
t
​
 ,LLM_signal 
t
​
 )
где 
𝑓
𝑡
f 
t
​
  — финансовые features, 
LLM_signal
𝑡
LLM_signal 
t
​
  — вектор настроений из DeepSeek.

Применение в BANXE: FinRL-агент для treasury management — автоматическая ребалансировка валютной позиции BANXE на основе сигналов от FinGPT sentiment agent + рыночных данных.

Часть III: Эталонная Архитектура Движка BANXE
3.1 Принцип проектирования: «Не один агент — армия специалистов»
Ключевой вывод из сравнения всех мировых банков (оба предыдущих исследования + текущее):

«Специализированные агенты по продуктам работают лучше, чем один генеральный агент» — Toss Bank (Корея)

«Composite Tools: детерминированные процессы — в tool-функции, LLM только принимает решение какой tool вызвать» — Nubank (5 production lessons)

«Stateful graph workflow через LangGraph» — DeerFlow 2.0, Nubank, Revolut AIR

Архитектурная модель движка BANXE — 7 слоёв:

text
┌──────────────────────────────────────────────────────────────────┐
│ СЛОЙ 7: ПРЕЗЕНТАЦИЯ (UX/UI)                                      │
│  assistant-ui + React + Whisper + Coqui TTS                      │
├──────────────────────────────────────────────────────────────────┤
│ СЛОЙ 6: ОРКЕСТРАЦИЯ АГЕНТОВ                                      │
│  LangGraph (stateful) + DeerFlow 2.0 SuperAgent Harness          │
├──────────────────────────────────────────────────────────────────┤
│ СЛОЙ 5: СПЕЦИАЛИЗИРОВАННЫЕ АГЕНТЫ (Composite Tools)              │
│  TransferAgent | FXAgent | SavingsAgent | ComplianceAgent        │
│  AnalyticsAgent | KYCAgent | SupportAgent | TreasuryAgent        │
├──────────────────────────────────────────────────────────────────┤
│ СЛОЙ 4: INTELLIGENCE LAYER                                       │
│  PRAGMA-style Encoder │ FinGPT / FinRobot │ GNN Fraud │ FATE FL  │
├──────────────────────────────────────────────────────────────────┤
│ СЛОЙ 3: MEMORY & CONTEXT                                         │
│  Mem0 + Zep (агентная память) │ Qdrant (векторный поиск)         │
│  LlamaIndex RAG │ Redis (сессионный контекст)                    │
├──────────────────────────────────────────────────────────────────┤
│ СЛОЙ 2: ЯДРО (CORE BANKING / LEDGER)                             │
│  Formance Stack (MIT) │ Blnk Finance │ FISCO BCOS audit trail    │
├──────────────────────────────────────────────────────────────────┤
│ СЛОЙ 1: ИНФРАСТРУКТУРА                                           │
│  Temporal (workflows) │ Kafka (events) │ Kubernetes (GKE/EKS)   │
│  Strands SDK (AWS multi-agent) │ SOFAStack (финансовые сервисы)  │
└──────────────────────────────────────────────────────────────────┘
3.2 Слой 1: Инфраструктура — Производственный фундамент
Temporal (open source, MIT) — Workflow Engine:

Временны́е рабочие процессы для банковских операций: «каждый платёж — это дurable workflow, который не теряется даже при перезагрузке сервера». Производственный опыт банков на Temporal:

Банки сократили время разработки новой платёжной функции с 3 месяцев до 1,5 месяцев

$14,3 млн сохранённой выручки за 3 года (1–2 крупных аварии в год предотвращено)

Один бразильский банк обрабатывает 2 миллиона болето-инвойсов в месяц на Temporal

Forrester ROI исследование: $4,16 млн выгоды против $1,38 млн инвестиций

Паттерн для BANXE: каждый агентный workflow (KYC, перевод, кредитная заявка) — Temporal Workflow. Это гарантирует auditability (EU AI Act требует трассировки) и idempotency (двойное списание невозможно).

Apache Kafka (Apache 2.0) — Event Streaming:

Nubank строит свою real-time AI-систему именно на Kafka: «каждая транзакция — событие, которое запускает агентные workflow». Все AI-решения — тоже события в Kafka, что обеспечивает полный audit trail.

Strands Agents SDK (AWS, Apache 2.0) — Multi-Agent Production Framework:

Выпущен в мае 2025 года, версия 1.0 в июле 2025. Уже используется в production в Amazon Q Developer, AWS Glue, VPC Reachability Analyzer. Ключевые возможности:

Model-agnostic: Bedrock, Anthropic Claude, Gemini, OpenAI, Meta Llama, Ollama, LiteLLM

Нативная MCP-поддержка из коробки

TypeScript SDK (preview декабрь 2025)

Strands Evaluations: систематическая валидация поведения агентов

Strands Steering: модульный prompting mechanism

SOFAStack (Alibaba, Apache 2.0) — Финансовые микросервисы:

Scalable Open Financial Architecture Stack от Alibaba — 44 репозитория. В production у MYBank (750 миллионов транзакций в сутки). Для BANXE: финансовые паттерны (circuit breaker, bulkhead, distributed transaction).

3.3 Слой 2: Core Banking — Финансовое ядро
Formance Stack (MIT, $21M инвестиций) — Ledger Engine:

Современная open source двойная бухгалтерия на Go. Идеально соответствует EMI-требованиям: каждый dbt (дебет/кредит) — атомарная операция с полным audit log. SEPA, SWIFT, мультивалютность из коробки.

Blnk Finance (Apache 2.0) — Альтернатива Formance:

Более лёгкий ledger для стартапов. Подходит для начальных этапов BANXE.

FISCO BCOS (Apache 2.0, WeBank) — Blockchain Audit Trail:

5000+ организаций в Китае используют для compliance. Для BANXE: неизменяемый audit ledger всех AI-решений (требование EU AI Act для high-risk AI systems).

3.4 Слой 3: Memory & Context — Агентная память
Ключевой принцип (из опыта Nubank): «ReAct Paradigm = Prompt (мозг) + Tools (руки) + Data (память RAG + сессионный контекст)».

Mem0 (Apache 2.0) — Персистентная агентная память:

Hierarchical memory: working memory (сессия) → episodic memory (прошлые взаимодействия) → semantic memory (факты о пользователе). Позволяет агенту помнить «Иван обычно переводит деньги жене в пятницу».

Zep (Apache 2.0) — Temporal Knowledge Graph:

Хранит взаимодействия как temporally-aware knowledge graph. Понимает «пользователь изменил работу», «сменился уровень дохода» — контекстная персонализация.

Qdrant (Apache 2.0, 22k звёзд) — Vector Database:

Хранит embeddings транзакций (PRAGMA-style), профилей пользователей, FAQ. Similarity search для «найди похожие транзакции клиента в прошлом». Rust-реализация — sub-millisecond latency.

LlamaIndex (MIT) — RAG Framework:

Индексирует документы банка (регламенты, FAQ, тарифы), нормативные акты (EU AI Act, GDPR тексты), финансовые продукты. Агент ищет релевантный контекст перед ответом.

3.5 Слой 4: Intelligence Layer — «Мозг» движка
FinGPT (MIT, AI4Finance Foundation):

Первая open source financial LLM. Компоненты:

FinGPT-Forecaster: предсказание цен акций на основе новостей

FinGPT-Sentiment-Analysis: sentiment из финансовых новостей (LoRA fine-tuning)

FinGPT-RAG: retrieval-augmented generation для финансовых документов

FinGPT-Robo-Advisor: анализ квартальных отчётов

FinRobot (MIT, AI4Finance Foundation):

Первая AI Agent-платформа для финансового анализа — мультиагентные workflow для research, reasoning, execution. Надстройка над FinGPT для production банковских use cases.

GNN Fraud Module (собственная реализация на PyG/DGL):

На основе arxiv-паттернов ASA-GNN и HGNN — разрабатывается on top of PyTorch Geometric (MIT). Граф обновляется с каждой транзакцией в Kafka; Temporal Workflow вызывает GNN-inference.

FATE Federated Learning (Apache 2.0, WeBank):

Для BANXE: кредитный скоринг и антифрод обучается federatedly с партнёрами без нарушения GDPR. PSI (Private Set Intersection) — обнаружение общих клиентов без раскрытия идентификаторов.

VaultGemma (Apache 2.0, Google):

Differentially private LLM — для sensitive задач (клиентские данные никогда не «вспоминаются» моделью). Разработан для regulated industries, GDPR-compliant by design.

3.6 Слой 5: Специализированные агенты — «Команда специалистов»
На основе уроков Toss Bank («специализированные агенты лучше») и Nubank (Composite Tools):

python
# BANXE Agent Registry (Strands SDK / LangGraph)

class TransferAgent:
    """Обрабатывает переводы SEPA/SWIFT/Pix-style"""
    tools = [validate_recipient, get_fx_rate, execute_transfer, send_receipt]
    model = "claude-3-5-sonnet"  # или DeepSeek-V3 локально
    
class FXAgent:
    """Конвертация валют, FX-advisory (паттерн WeLab FX Best Rate)"""
    tools = [get_live_rates, compare_rails, execute_fx, schedule_fx]
    
class ComplianceAgent:
    """KYC/AML, EU AI Act audit, GDPR"""
    tools = [run_kyc_check, screen_aml, log_decision, explain_decision]
    # FATE federated model for cross-bank AML
    
class SavingsAgent:
    """Savings Pockets, AI-рекомендации (паттерн Minna Bank)"""
    tools = [create_pocket, suggest_goal, calculate_projection, auto_sweep]
    
class AnalyticsAgent:
    """Spending insights, PRAGMA embeddings, SpendingInsightCard"""
    tools = [get_spending, categorize, generate_insight, create_chart]
    
class TreasuryAgent:
    """FinRL-агент для управления ликвидностью банка"""
    tools = [get_positions, rebalance_portfolio, hedge_fx_exposure]
3.7 Слой 6: Оркестрация — LangGraph + DeerFlow
LangGraph как центральный StateGraph:

python
from langgraph.graph import StateGraph, END

# BANXE Agent StateGraph
workflow = StateGraph(BanxeAgentState)

# Nodes — специализированные агенты
workflow.add_node("intent_classifier", classify_intent)
workflow.add_node("transfer_agent", run_transfer_agent)
workflow.add_node("fx_agent", run_fx_agent)
workflow.add_node("analytics_agent", run_analytics_agent)
workflow.add_node("compliance_gate", run_compliance_check)
workflow.add_node("human_escalation", escalate_to_human)

# Edges — routing логика
workflow.add_conditional_edges(
    "intent_classifier",
    route_to_agent,  # deterministic routing через Composite Tool
    {
        "transfer": "compliance_gate",
        "fx": "fx_agent",
        "analytics": "analytics_agent",
        "unclear": "human_escalation"
    }
)

# Compliance gate перед любым финансовым действием
workflow.add_edge("compliance_gate", "transfer_agent")
workflow.add_edge("transfer_agent", END)
Ключевой принцип (Nubank): LLM решает «какой агент вызвать», но сам перевод — детерминированная Composite Tool. LLM не считает деньги сам — вызывает execute_transfer(amount=500, currency="EUR", recipient="Ivan").

DSPy для оптимизации промтов:

Вместо ручного написания 5-страничных промтов — DSPy + Japa optimizer автоматически оптимизирует промты под производственные метрики. Prompt Semantic Versioning: Tone Module, Tooling Module, Safety Module — независимо версионируются.

3.8 Слой 7: Презентация — UX/UI Integration
Полностью описан в предыдущих двух исследованиях. Связка со слоями движка:

text
Пользователь пишет/говорит
    ↓ Whisper STT
Интент → LangGraph StateGraph
    ↓ DeerFlow Planner (для сложных задач)
Composite Tool execution
    ↓ Temporal Workflow (auditability)
Rich Card generation → assistant-ui
    ↓ SCA confirmation (Face ID / Touch ID)
Kafka event → FISCO BCOS audit log
Часть IV: Агентные Frameworks — Полное Сравнение
4.1 Таблица сравнения всех Manus-подобных движков
Фреймворк	Звёзды / Лицензия	Архитектура	Банковский use case	Статус
DeerFlow 2.0 (ByteDance)	20k+ / MIT	SuperAgent + LangGraph StateGraph	Research Agent, Doc Analysis, Reports	✅ Production (2026)
OpenManus (MetaGPT)	33k+ / MIT	3-слойный: Agent+Tool+Memory	Базовый агентный движок	Active dev
AgenticSeek	10k+ / Apache 2.0	Offline-first, Voice	GDPR EU-only deployment	Active dev
Suna (automationkit)	5k+ / MIT	Generalist + browser tools	Customer research automation	Early
Strands SDK (AWS)	★ / Apache 2.0	Model-driven, MCP-native	Multi-agent banking, production	✅ v1.0 Production
LangGraph (LangChain)	12k+ / MIT	Stateful StateGraph	Nubank, 1000s — core orchestration	✅ Production
CrewAI	29k+ / MIT	Role-based crew of agents	Analyst workflows, reports	✅ Production
AutoGen (Microsoft)	35k+ / CC-BY-NC-4.0	Multi-agent conversation	Enterprise complex tasks	Research
MetaGPT	46k+ / MIT	Role-based with memory	Software eng. agents	Research→Prod
Agno (AgnoAI)	18k+ / Apache 2.0	Lightweight, model-agnostic	Simple financial agents	Active
Рекомендация для BANXE:

Не один фреймворк — два в связке:

LangGraph — центральный StateGraph (конечный автомат переходов между агентами)

DeerFlow 2.0 — SuperAgent Harness для long-horizon задач (анализ документов, deep research, report generation)

Почему два? LangGraph — оркестратор мгновенных банковских транзакций (low-latency, <300ms). DeerFlow — для complex workflows (KYC document analysis, financial advisory report), которые могут занимать минуты.

4.2 AI4Finance Foundation — Полная Экосистема
Некоммерческая организация AI4Finance Foundation создала наиболее полный open source финансовый AI-стек:

Проект	Лицензия	Назначение
FinGPT	MIT	LLM для финансового анализа, sentiment, forecasting
FinRobot	MIT	Agent-платформа для equity research
FinRL	MIT	Reinforcement learning для трейдинга
FinRL-DeepSeek	MIT	LLM-infused risk-sensitive RL
FinNLP	MIT	Democratizing financial internet data
TradingAgents	MIT	Multi-agent LLM торговый фреймворк
LinkedIn-обзор (февраль 2026): 15 GitHub-репозиториев, которые должен знать каждый финансовый AI-разработчик:

TradingAgents — Bull/Bear researcher agents + risk manager agent

AI Hedge Fund — LLM-агент-хедж-фонд (Ben Graham, Cathie Wood стили)

Microsoft Qlib — AI quantitative investment research platform (30k+ звёзд)

Часть V: Безопасность и Compliance движка — EU AI Act in Practice
5.1 2026 State of AI Agent Security
По отчёту State of AI Agent Security 2026:

81% команд уже прошли стадию планирования и деплоят агентов

Только 14,4% имеют полное одобрение security

Ключевые риски: prompt injection через внешние данные, tool abuse, data exfiltration

OWASP Top 10 для LLM + Agents 2025 (применение в BANXE):

Угроза	Решение в BANXE
Prompt Injection	NeMo Guardrails + input sanitization
Insecure Output Handling	Structured outputs (JSON schema validation)
Training Data Poisoning	FATE Federated Learning (isolated training)
Model Denial of Service	Rate limiting + Temporal timeout workflows
Supply Chain Vulnerabilities	GitHub Dependabot + SBOM generation
Sensitive Information Disclosure	VaultGemma differential privacy
Insecure Plugin Design	MCP tool sandboxing + permission scoping
Excessive Agency	Confidence threshold gates (0.90 для production)
Overreliance	Human-in-the-loop для всех финансовых операций
Model Theft	Self-hosted LLM (DeepSeek/Ollama) для sensitive data
5.2 NeMo Guardrails (NVIDIA, Apache 2.0) — Программные ограничения агента
Позволяет programmatically ограничить поведение LLM через colang-правила:

text
define flow no_financial_advice_without_disclaimer
    # Агент не может давать инвестиционные советы без дисклеймера
    user ask investment advice
    bot must say "Это не является финансовым советом..."
    
define flow transfer_requires_confirmation
    # Любой перевод требует явного подтверждения
    bot suggest transfer
    user must confirm explicitly
    bot execute transfer
5.3 EU AI Act в коде — Decision Lineage Schema
Для каждого AI-решения агента — обязательная запись в ClickHouse:

sql
CREATE TABLE agent_decisions (
    decision_id UUID,
    agent_name String,
    user_id String,  -- pseudonymized
    timestamp DateTime64(9),
    input_context String,  -- sanitized
    decision_type Enum('transfer', 'credit', 'fraud_flag', 'recommendation'),
    confidence Float32,
    tools_called Array(String),
    model_version String,
    explanation String,  -- human-readable "why"
    human_reviewed Bool DEFAULT false,
    review_outcome Nullable(String)
) ENGINE = MergeTree ORDER BY (timestamp, decision_id);
Для кредитных решений (High-Risk AI по EU AI Act) — автоматическое создание explanation через LIME/SHAP:

𝜙
𝑖
=
∑
𝑆
⊆
𝐹
∖
{
𝑖
}
∣
𝑆
∣
!
(
∣
𝐹
∣
−
∣
𝑆
∣
−
1
)
!
∣
𝐹
∣
!
[
𝑓
(
𝑆
∪
{
𝑖
}
)
−
𝑓
(
𝑆
)
]
ϕ 
i
​
 = 
S⊆F∖{i}
∑
​
  
∣F∣!
∣S∣!(∣F∣−∣S∣−1)!
​
 [f(S∪{i})−f(S)]
Каждый клиент может нажать ⓘ и увидеть: «Ваш кредит отклонён из-за: высокая нагрузка по существующим кредитам (40%), нестабильный доход (35%), короткая история (25%)».

Часть VI: CI/CD «Фабрика» — Интеграция движка в разработку BANXE
6.1 GitHub Agentic Workflows + Агентный CI/CD
GitHub Agentic Workflows (Technical Preview, февраль 2026) — AI-агенты внутри GitHub Actions. Для BANXE «Фабрики»:

text
# .github/workflows/banxe-agent-review.yml
name: BANXE AI Agent Pipeline

on: [pull_request, push]

jobs:
  analysis-agent:
    name: Code Analysis (Claude Code Action)
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          scope: "security,logic,banking-patterns"
          
  security-agent:
    name: OWASP Security Scan
    runs-on: ubuntu-latest
    steps:
      - name: LLM Security Scan
        run: |
          # Проверка на prompt injection уязвимости
          # OWASP Top 10 LLM check
          
  compliance-gate:
    name: EU AI Act Compliance Check
    needs: [analysis-agent, security-agent]
    if: github.ref == 'refs/heads/main'
    steps:
      - name: AI Decision Audit Schema Validation
        run: python validate_decision_schema.py
        
  deploy-staging:
    name: Deploy to Staging (confidence >= 0.75)
    needs: compliance-gate
    
  deploy-production:
    name: Deploy to Production (confidence >= 0.90 + human approval)
    needs: deploy-staging
    environment: production  # Requires human approval
6.2 Паттерн «Detection → Diagnosis → Fix → Deploy»
Для production-grade CI/CD банковского AI-агента:

Стадия	Агент	Confidence threshold
Код-ревью	Analysis Agent (Claude Code)	Комментирует автоматически
Безопасность	Security Agent (OWASP scan)	Блокирует при критических
Staging deploy	Execution Agent	≥ 0.75
Production deploy	Execution Agent + Human gate	≥ 0.90 + approval
6.3 Langfuse — Observability для LLM-агентов
Каждый LLM-вызов агента трассируется через Langfuse (MIT, 8k звёзд):

Latency per agent + per tool call

Token usage и стоимость по модели

Quality score (LLM-as-judge автоматически)

A/B тестирование промтов в production

Часть VII: Творческие и Экспериментальные Идеи для Движка BANXE
7.1 «Банк Памяти» — Memory-First архитектура (вдохновлено Mem0 + Toss)
Идея: каждый клиент BANXE имеет персональный Memory Graph в Zep/Mem0. Агент не начинает каждый разговор с нуля — он «знает»:

Типичные паттерны расходов (PRAGMA embeddings)

Финансовые цели (сберегательные карманы)

Предпочтительный стиль общения (краткий/подробный)

Историю жалоб и решённых проблем

Математика: Multi-hop Knowledge Graph query при каждом обращении:

context
=
GraphSearch
(
user_id
,
𝑘
=
5
,
similarity
=
cos
⁡
(
𝑞
,
𝑚
𝑖
)
)
context=GraphSearch(user_id,k=5,similarity=cos(q,m 
i
​
 ))
7.2 «Предиктивный Агент» — Проактивные действия до запроса
Вдохновлено DBS Joy (15 000 AI-чатов в месяц) и KakaoBank проактивными подсказками:

Temporal Cron Workflow сканирует каждого пользователя ежечасно:

python
@workflow.defn
class ProactiveInsightWorkflow:
    @workflow.run
    async def run(self, user_id: str):
        # Запускается каждый час
        spending = await get_spending_trend(user_id)
        bill_due = await check_upcoming_bills(user_id)
        salary = await predict_salary_date(user_id)
        
        if bill_due and balance < bill_due.amount * 1.2:
            await send_proactive_alert(user_id, 
                "Через 3 дня списание. Пополнить счёт?")
7.3 «Федеративный Кредитный Союз» — FATE для cross-bank scoring
Идея: BANXE и партнёрские банки (через FATE) обучают общую кредитную модель без обмена данными. Private Set Intersection: «У нас есть общий клиент (зашифрованный хэш)? Добавим его поведение в общую модель». Лифт: +15-30% PR-AUC кредитного скоринга без нарушения GDPR.

7.4 «Quantum Fraud Detection» — Экспериментальный модуль
На основе QGNN (Quantum Graph Neural Network, arXiv 2023): применение Variational Quantum Circuits (VQC) для обнаружения fraud в сложных транзакционных графах. AUC 0.85 на реальных финансовых данных — превосходит классические GNN.

Практическое применение сегодня: IBM Qiskit (открытый) позволяет запускать QGNN на симуляторе. К 2027-2028 — на реальных quantum processors. BANXE может начать экспериментировать уже сейчас.

7.5 «Temporal Knowledge Distillation» — Экономия на inference
Идея: большая PRAGMA-подобная модель (1B параметров) дистиллируется в маленькую (10M параметров) через knowledge distillation для real-time inference:

𝐿
𝐾
𝐷
=
𝛼
𝐿
𝐶
𝐸
(
𝑦
,
𝑦
^
𝑠
)
+
(
1
−
𝛼
)
𝑇
2
𝐿
𝐾
𝐿
(
𝜎
(
𝑧
^
𝑡
/
𝑇
)
,
𝜎
(
𝑧
^
𝑠
/
𝑇
)
)
L 
KD
​
 =αL 
CE
​
 (y, 
y
^
​
  
s
​
 )+(1−α)T 
2
 L 
KL
​
 (σ( 
z
^
  
t
​
 /T),σ( 
z
^
  
s
​
 /T))
где 
𝑇
T — temperature, 
𝑧
^
𝑡
z
^
  
t
​
  — logits учителя (PRAGMA-1B), 
𝑧
^
𝑠
z
^
  
s
​
  — logits студента (PRAGMA-10M). Результат: PRAGMA-10M для реалтайм (<1ms) fraud, PRAGMA-1B для ночного кредитного batch.

Часть VIII: Итоговое Сравнение Движков — Выбор для BANXE
8.1 Оценочная матрица
Критерий	DeerFlow 2.0	OpenManus	Strands SDK	LangGraph	Manus AI
Open Source	✅ MIT	✅ MIT	✅ Apache 2.0	✅ MIT	❌ Закрытый
GDPR/EU AI Act ready	✅ Локальный	✅ Локальный	Частично	✅	❌ Облако
Banking-специфика	Средняя	Низкая	Средняя	Высокая	Высокая
Multi-agent	✅ Supervisor+sub	Частично	✅	✅	✅
Long-horizon tasks	✅✅	✅	Средне	Средне	✅✅
Real-time (<300ms)	Нет	Нет	✅	✅✅	Нет
MCP native	✅	Нет	✅✅	Частично	Нет
Production examples	ByteDance	Нет	AWS services	Nubank	Monica.im
Memory	✅ Long-term	Базовая	Bedrock memory	Базовая	Облако
Kubernetes/Docker	✅✅	Docker	AWS ECS/EKS	Любая	Облако
Финальная рекомендация движка BANXE:

Основной стек движка (слоёный подход):

text
LangGraph         → Оркестрация реалтайм-транзакций (низкая латентность)
Strands SDK (AWS) → Production multi-agent для сложных workflow
DeerFlow 2.0      → Long-horizon tasks (KYC analysis, financial reports)
FinGPT / FinRobot → Специализированный финансовый AI
FATE (WeBank)     → Federated Learning (GDPR-compliant training)
Temporal          → Workflow durability + audit trail
Не нужно выбирать один — мировые лидеры (Nubank, DBS, WeLab) используют несколько компонентов в связке.

8.2 Roadmap внедрения движка в «Фабрику» BANXE
Фаза	Срок	Компоненты	Milestone
Фаза	Срок	Компоненты	Milestone
Phase 0: Foundation	Месяц 1-2	Formance/Blnk + Temporal + Kafka + Kubernetes	Core banking работает
Phase 1: First Agent	Месяц 2-3	LangGraph + TransferAgent (Composite Tool)	AI Transfer работает
Phase 2: Intelligence	Месяц 3-5	Qdrant + LlamaIndex + FinGPT sentiment	RAG + Analytics Agent
Phase 3: Memory	Месяц 5-6	Mem0 + Zep	Персонализация включена
Phase 4: Fraud/AML	Месяц 6-8	HGNN + NeMo Guardrails	Fraud detection production
Phase 5: Foundation Model	Месяц 8-12	PRAGMA-style encoder на собственных данных	nuFormer для BANXE
Phase 6: Federated	Месяц 12+	FATE FL + партнёры	Cross-bank credit scoring
8.3 Топ-10 репозиториев для немедленного клонирования в «Фабрику»
github.com/bytedance/deer-flow (MIT, 20k★) — SuperAgent Harness

github.com/strands-agents/sdk-python (Apache 2.0) — Production multi-agent

github.com/FederatedAI/FATE (Apache 2.0, 5.7k★) — Federated Learning

github.com/AI4Finance-Foundation/FinRobot (MIT) — Financial AI agents

github.com/AI4Finance-Foundation/FinGPT (MIT) — Financial LLM

github.com/langchain-ai/langgraph (MIT, 12k★) — Agent orchestration

github.com/FISCO-BCOS/FISCO-BCOS (Apache 2.0, 3.4k★) — Audit blockchain

github.com/qdrant/qdrant (Apache 2.0, 22k★) — Vector database

github.com/temporalio/temporal (MIT, 12k★) — Workflow engine

github.com/langfuse/langfuse (MIT, 8k★) — LLM observability

***

## References

1. Can OpenManus Beat Manus AI? Benchmark Stats, Real Code and Business Use Cases — https://pub.towardsai.net/can-openmanus-beat-manus-ai-benchmark-stats-real-code-and-business-use-cases-ac6047d876d6
2. Manus AI vs. OpenManus: A Benchmark Showdown (86.5 vs 74.3) — https://medium.com/@rogt.x1997/manus-ai-vs-openmanus-a-benchmark-showdown-86-5-vs-74-3-open-source-revolution-e96a62aed63f
3. Manus vs OpenManus: The Battle Between Commercial and Open-source — https://stable-learn.com/en/manus-openmanus-compare/
4. Manus vs OpenManus: Meta-Orchestrator vs Fixed Agent — https://www.linkedin.com/posts/jedikim_manus-looks-less-like-a-single-agent-system-activity-7422660051837882368-ypei
5. DeerFlow — ByteDance's Open-Source SuperAgent Framework — https://www.youtube.com/watch?v=lgthpUGQdmo
6. DeerFlow 2.0 GitHub feedback — https://x.com/ByteDanceOSS/status/2026859269594009674
7. DeerFlow — ByteDance Open-Source SuperAgent Harness — https://www.linkstartai.com/en/github-picks/deer-flow
8. DeerFlow: Multi-Agent Deep Research — https://deerflow.tech/mock/api/threads/fe3f7974-1bcb-4a01-a950-79673baafefd/artifacts/mnt/user-data/outputs/index.html?download=true
9. Revolut Trained an AI on 40 Billion Banking Events — https://dev.to/ji_ai/revolut-trained-an-ai-on-40-billion-banking-events-the-results-are-wild-4d1e
10. PRAGMA: Revolut Foundation Model — https://arxiv.org/abs/2604.08649
11. Revolut Launches PRAGMA, AI Model Trained on 24 Billion Banking Events — https://www.kucoin.com/news/flash/revolut-launches-pragma-ai-model-trained-on-24-billion-banking-events
12. Modeling Financial Habits with Transformers — https://arxiv.org/html/2507.23267v1
13. How Nubank Uses Transformers to Model Financial Habits at Scale — https://app.daily.dev/posts/how-nubank-uses-transformers-to-model-financial-habits-at-scale-ze8hr0dtm
14. TransactionGPT — https://arxiv.org/abs/2511.08939
15. Transformer-Based Encoding of Transactional Behavior — https://arxiv.org/abs/2312.14406
16. Graph Neural Networks for Financial Fraud Detection: A Review — https://arxiv.org/abs/2411.05815
17. Detecting Credit Card Fraud via Heterogeneous Graph Neural Network — https://arxiv.org/abs/2504.08183
18. FraudGNN-RL: A Graph Neural Network With Reinforcement Learning — https://www.computer.org/csdl/journal/oj/2025/01/10892045/24rmDEnklJS
19. Transaction Fraud Detection via an Adaptive Graph Neural Network — https://arxiv.org/abs/2307.05633
20. A novel federated learning approach with knowledge transfer for credit scoring — https://www.sciencedirect.com/science/article/abs/pii/S0167923623001598
21. Privacy-preserving federated credit risk models — https://www.nature.com/articles/s41598-025-34536-9
22. Toss Bank aims to create an environment where all organizations can utilize AI — https://www.mk.co.kr/en/special-edition/11418955
23. FATE: An Industrial Grade Federated Learning Framework — https://github.com/federatedai/fate
24. Google Releases VaultGemma LLM With Differential Privacy — https://www.opensourceforu.com/2025/09/google-releases-vaultgemma-llm-with-differential-privacy-under-open-source-license/
25. FinRL: Financial Reinforcement Learning — https://github.com/AI4Finance-Foundation/FinRL
26. 15 GitHub Repos Every AI Agent in Finance — https://www.linkedin.com/posts/hanane-d-algo-trader_15-github-repos-every-ai-agent-in-finance-activity-7430961798532558848-R7DR
27. AI4Finance Foundation — https://github.com/ai4finance-foundation
28. Building AI agents for 131 million customers — https://building.nubank.com/building-ai-agents-for-131-million-customers/
29. Revolut just dropped PRAGMA paper — https://x.com/maxkarpis/status/2043714024609546449
30. Payments Modernization at Scale with MongoDB and Temporal — https://assets.ctfassets.net/0uuz8ydxyd9p/4zPWC5hWlFE62dSWsyvbfc/6e83586bab4696f212d97afd9cafb3d2/White_Paper_MDB_and_Temporal.pdf
31. How banks are cutting development time in half while avoiding outages — https://temporal.io/blog/how-banks-are-cutting-dev-time-in-half-with-temporal-cloud
32. How Will Bank leverages Temporal to handle 2 million customers | Replay 2023 — https://www.youtube.com/watch?v=CH8s0lGPR8U
33. Architecting a Modern Financial Institution — https://www.infoq.com/presentations/nubank-architecture/
34. AWS Introduces Strands Agents: A Model-Driven Revolution — https://engineering.01cloud.com/2026/01/16/aws-introduces-strands-agents-a-model-driven-revolution-in-building-robust-ai-agents/
35. Introducing Strands Agents 1.0: Production-Ready Multi-Agent Orchestration — https://aws.amazon.com/blogs/opensource/introducing-strands-agents-1-0-production-ready-multi-agent-orchestration-made-simple/
36. Announcing TypeScript support in Strands Agents (preview) — https://aws.amazon.com/about-aws/whats-new/2025/12/typescript-strands-agents-preview/
37. SOFAStack — https://github.com/orgs/sofastack/repositories
38. FISCO-BCOS README_EN — https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/docs/README_EN.md
39. FinGPT: Open-Source Financial Large Language Models — https://github.com/ai4finance-foundation/fingpt
40. AI4Finance Foundation | Open Source Financial AI — https://ai4finance.org
41. State of AI Agent Security 2026 Report — https://www.gravitee.io/blog/state-of-ai-agent-security-2026-report-when-adoption-outpaces-control
42. How Financial Services Teams Should Secure AI Agents in 2026 — https://www.armosec.io/blog/financial-services-ai-agent-security/
43. GitHub Just Put an AI Agent Inside Your CI CD Pipeline — https://www.youtube.com/watch?v=BcKhhCB26k0
44. Agent-Operated CI/CD: The Architecture Making AI Coding Agents — https://alexlavaee.me/blog/agent-operated-cicd-pipelines/
45. Financial Fraud Detection using Quantum Graph Neural Networks — https://arxiv.org/abs/2309.01127
46. bytedance/deer-flow — https://github.com/bytedance/deer-flow
47. FinRobot: An Open-Source AI Agent Platform for Financial Analysis — https://github.com/ai4finance-foundation/finrobot
