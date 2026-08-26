# Legion Generic Engine and BANXE Specialization Canonical (2026-07-10)

## 1. Title and Scope

Этот документ фиксирует двухуровневую каноническую модель: (1) generic Legion Manus-like engine core и (2) BANXE banking specialization profile поверх него. [SRC:emi-banxe-intent-first-banking-2026-07-10.md] [SRC:emi-banxe-intent-layer-launch-2026-07-10.md] [SRC:emi-banxe-ideal-engine-math-2026-07-10.md] [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] [SRC:banxe-uxui-oss-designer-prompt-2026-07-10.md] [SRC:emi-banxe-world-experience-full-2026-07-10.md]

## 2. Source Inventory

- docs/sources/emi-banxe-intent-first-banking-2026-07-10.md — PRESENT — SHA256 f686c1f9d2eb57239944e1f65f4ae9047eacea27b6c711f843db907e76970891
- docs/sources/emi-banxe-intent-layer-launch-2026-07-10.md — PRESENT — SHA256 934d78ed76168349e69f6967f785131b93e76c8abed3ca2081926c4f9be64ab9
- docs/sources/emi-banxe-ideal-engine-math-2026-07-10.md — PRESENT — SHA256 8612f7ebb76004f9c4c6a58d385090636ce7151505fb121285ffbd12be219a06
- docs/sources/banxe-agent-engine-conclusion-2026-07-10.md — PRESENT — SHA256 54a4439e748afa9fbb397d49b61ae055977a0d49f5aa92327a0481644d60a30e
- docs/sources/banxe-oss-free-agent-solutions-2026-07-10.md — PRESENT — SHA256 50c2f6677d224d56917dee2f6560947eb334253d102f1a0dab3c6fe44ab6743b
- docs/sources/banxe-uxui-oss-designer-prompt-2026-07-10.md — PRESENT — SHA256 37b8be7bc87c9a77c716792794f7ed5f4dd85973c8a0291a5e27ba0bebbad4fa
- docs/sources/emi-banxe-world-experience-full-2026-07-10.md — PRESENT — SHA256 db72a7ea2b675f50a1a7ad1cedd098651030c8ad11094c45edb0f486fddeeea9


## 3. Architectural Split

Generic core — это Manus-подобный движок для Legion: intake намерения, планирование, граф оркестрации, specialist runtime, tool execution, memory, guardian/audit, HITL, observability и интерфейсный слой. [SRC:emi-banxe-intent-first-banking-2026-07-10.md] [SRC:emi-banxe-intent-layer-launch-2026-07-10.md] [SRC:emi-banxe-ideal-engine-math-2026-07-10.md] [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

BANXE specialization — это банковский профиль поверх generic core: passports, compliance swarm, KYC/KYB/AML/fraud/recon, payment/open-banking/ledger integration, banking guardrails и domain-specific response surfaces. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] [SRC:emi-banxe-world-experience-full-2026-07-10.md]

## 4. Generic Legion Manus-Like Engine Core

### 4.1 Intent Intake
- Intent intake принимает пользовательский запрос и нормализует его в structured intent object. [SRC:emi-banxe-intent-first-banking-2026-07-10.md] [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- AIR-like / chat-like interaction surface упоминается как интерфейс входа в движок. [SRC:emi-banxe-intent-layer-launch-2026-07-10.md] [SRC:emi-banxe-world-experience-full-2026-07-10.md]

### 4.2 Planning and Orchestration
- Task planner строит DAG/graph зависимостей между шагами и агентами. [SRC:emi-banxe-ideal-engine-math-2026-07-10.md] [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- LangGraph repeatedly appears как базовая оркестрационная основа. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]
- MCP обозначен как стандартный интерфейс инструментов агентов. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

### 4.3 Specialist Runtime
- Generic core поддерживает multiple specialist agents / role-based agents. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]
- В качестве вариантов в sources фигурируют CrewAI, MetaGPT, DeerFlow, OpenHands. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

### 4.4 Tool and Execution Layer
- Execution layer включает вызов tool endpoints, workflow systems и durable orchestration. [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- Temporal и n8n явно названы как orchestration/automation substrate. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

### 4.5 Memory
- Semantic memory выделена как отдельный недостающий слой. [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- В sources упомянуты Qdrant / Weaviate для vector memory, LlamaIndex для RAG, Mem0 + Zep для long-term memory. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

### 4.6 Governance, Guardian, Verify
- Guardian и Verify описываются как decision-audit и consensus validation layer. [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- 2-of-3 consensus logic служит шаблоном generic verification gate, даже если первоначально описан в banking context. [SRC:banxe-agent-engine-conclusion-2026-07-10.md]

### 4.7 HITL
- Human-in-the-loop repeatedly appears как обязательный control path для критичных решений. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

### 4.8 Observability
- Langfuse, Arize Phoenix, DeepEval и MLflow перечислены как recommended observability/evaluation stack. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

## 5. BANXE Banking Specialization Profile

- 39 banking passports — domain-specialized agent passports. [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- 9-agent compliance swarm — banking-specific specialist cluster. [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- KYC onboarding, AML monitoring, sanctions, fraud, recon, UBO/KYB-style workflows относятся к specialization layer. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]
- Financial infra choices such as Formance, Adorsys Open Banking Gateway, Stripe AI SDK + MCP, Hyperledger Fabric относятся к banking profile, а не к generic core. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

## 6. Boundary Table

| Component / Concept | Generic Core | BANXE Specialization | Notes |
|---|---|---|---|
| LangGraph | Yes | Yes | Orchestration substrate reusable across domains. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] |
| Tool Registry | Yes | Yes | Generic mechanism; banking tools are specialization entries. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] |
| Qdrant | Yes | Yes | Generic semantic memory, banking-specific corpora on top. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] |
| MCP | Yes | Yes | Generic tool interface standard. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] |
| Guardian | Yes | Yes | Generic audit gate, banking-specific policy packs possible. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] |
| Verify API | Partial | Yes | Generic consensus pattern, concrete implementation currently banking-shaped. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] |
| MetaClaw | Partial | Partial | Appears as meta-learning agent; boundary requires further audit. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] |
| OpenClaw | Partial | Partial | Gateway role appears, but generic vs banking split needs audit. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] |
| 39 passports | No | Yes | Explicitly banking-domain passports. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] |
| 9-agent compliance swarm | No | Yes | Banking compliance specialization. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] |
| Temporal | Yes | Yes | Generic durable workflows, reused in banking flows. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] |
| n8n | Yes | Yes | Generic integration/automation substrate. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] |
| Formance | No | Yes | Banking ledger specialization. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] |
| Adorsys | No | Yes | Banking open-banking specialization. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] |
| Rich Cards | Partial | Partial | Interface pattern appears; exact generic boundary needs source reconciliation. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:emi-banxe-world-experience-full-2026-07-10.md] |

## 7. Generic Engine Canonical Stack

| Domain | Canonical Choice | Alternatives Mentioned | Why It Belongs To Generic Core | Notes / Constraints |
|---|---|---|---|---|
| Orchestration | LangGraph | CrewAI, MetaGPT | Graph/task orchestration is domain-agnostic. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] | CrewAI maturity cautions appear in sources. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] |
| Tool interface | MCP | direct tool manifests | Standard agent-tool boundary. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] | Requires registry/governance shape. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] |
| Memory | Qdrant + LlamaIndex | Weaviate, Mem0, Zep | Reusable semantic memory substrate. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] | Long-term memory boundary still needs precise architecture. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] |
| Workflow | Temporal + n8n | Prefect, Dify, Flowise | Generic multi-step execution backbone. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] | Prefect is more pipeline/data-oriented in sources. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] |
| Observability | Langfuse + Arize Phoenix + DeepEval + MLflow | none clearly preferred beyond listed options | Generic tracing/eval/monitoring layer. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] | |
| Voice | Whisper + Kokoro/StyleTTS2 + LiveKit | none | Generic multimodal interaction layer. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] | |

## 8. BANXE Specialization Canonical Stack

| Domain | Canonical Choice | Why It Is Banking-Specific | Dependencies On Generic Core | Notes |
|---|---|---|---|---|
| Domain agents | 39 banking passports | Direct financial-domain specialization. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] | planner, runtime, memory, audit | |
| Compliance reasoning | 9-agent compliance swarm | Specific to regulated banking/compliance workflows. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] | orchestration, HITL, Verify, Guardian | |
| Ledger | Formance | Financial ledger substrate. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] | generic tool/execution layer | |
| Open banking | Adorsys Open Banking Gateway | PSD2/XS2A domain integration. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] | tool interface, auth, workflow | |
| Payment rails | Stripe AI SDK + MCP | Financial/payment specialization. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] | tool interface, policy gates | |

## 9. Mathematical / Agentic Principles

- ReAct appears as a general agent control pattern. [SRC:emi-banxe-ideal-engine-math-2026-07-10.md] [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- DAG planning appears as generic decomposition logic for dependent tasks. [SRC:emi-banxe-ideal-engine-math-2026-07-10.md] [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- Bayesian / 2-of-3 consensus appears as concrete validation logic around Verify API. [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- In-context learning appears via MetaClaw skill accumulation. [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- MCTS appears as planning/evaluation strategy for branch selection. [SRC:emi-banxe-ideal-engine-math-2026-07-10.md] [SRC:banxe-agent-engine-conclusion-2026-07-10.md]
- HITL thresholding appears as escalation logic for critical decisions. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

## 10. Constraints

### 10.1 Generic Engine Constraints
- Need auditability, observability, human oversight and protection from agent loops. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]
- OWASP agent risks imply mTLS, circuit breakers and zero-trust patterns. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]
- Cost ceilings and rate limiting are required to avoid runaway inference loops. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

### 10.2 Banking Specialization Constraints
- Sensitive client data should stay on local models for privacy-sensitive paths. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]
- EU AI Act / GDPR / data residency and human oversight pressure the banking layer more strongly. [SRC:banxe-oss-free-agent-solutions-2026-07-10.md] [SRC:banxe-agent-engine-conclusion-2026-07-10.md]

## 11. What Exists Now vs What Must Be Built

### Existing or Confirmed
- Guardian, Verify API, n8n, Temporal, ClickHouse, passports, compliance swarm are explicitly described as existing/working pieces in the BANXE stack. [SRC:banxe-agent-engine-conclusion-2026-07-10.md]

### Missing or Proposed
- BANXE-INTENT-ENGINE, Tool Registry and semantic memory via Qdrant are explicitly named as missing pieces. [SRC:banxe-agent-engine-conclusion-2026-07-10.md]

### Needs Further Audit
- Exact split for MetaClaw, OpenClaw, Rich Cards, AIR-like surface and some interface abstractions needs source reconciliation and repository audit. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:emi-banxe-world-experience-full-2026-07-10.md]

## 12. Implementation Posture

- Build first: generic orchestration core, tool registry, memory, audit/guardian integration, HITL, observability. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]
- Defer into specialization: banking passports, compliance policy packs, payment/open-banking/ledger integrations, regulated workflow packs. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]
- Do not entangle too early: generic core should not hardcode bank-only tool semantics into planner/runtime abstractions. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]

## 13. Open Questions / Source Tensions

- Sources often present BANXE and generic agent engine ideas in the same narrative, so boundary extraction requires explicit architectural discipline. [SRC:banxe-agent-engine-conclusion-2026-07-10.md] [SRC:banxe-oss-free-agent-solutions-2026-07-10.md]
- Some interface concepts are visible as BANXE-facing UX artifacts but may represent generic engine response surfaces; this needs separate audit. [SRC:emi-banxe-world-experience-full-2026-07-10.md] [SRC:banxe-uxui-oss-designer-prompt-2026-07-10.md]
