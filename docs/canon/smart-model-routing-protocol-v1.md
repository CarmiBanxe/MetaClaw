# Smart Model Routing Protocol v1

**Status:** Effective — Operator-directed cloud-first development policy  
**Applies to:** Every planning, design, coding, review, research, and deployment-preparation task in MetaClaw and the Banxe demo-fintech programme.  
**Precedence:** This protocol reconciles model-routing roles across the software-factory canon, Claude Code canon, ADR-032, model policy, FCC policy, and operator cutover instructions.

## Purpose

Maximise engineering and architecture capability by routing each task to the best available model or tool while keeping protected banking data in a local-safe path. This protocol is capability-expanding: it does not restrict eligible models by brand or provider.

## Mandatory preflight

Before planning or execution, the accountable agent reads:
1. the software-factory canon;
2. the applicable README and task policy;
3. relevant skills/runbooks;
4. the current task classification and data sensitivity.

The preflight record contains task ID, files read, proposed route, model/tool role, data class, and fallback plan.

## Routing roles

| Role | Preferred route | Allowed purpose |
|---|---|---|
| Preparation / long context | Any allowlisted efficient model through FCC, including Kimi, Gemini Flash, OpenRouter-class, DeepSeek, NIM, or equivalent | Research synthesis, reading, summaries, task decomposition, ADR input, synthetic fixtures, documentation |
| Primary coding executor | Codex plugin/CLI when available and not quota-blocked | Code generation, patches, tests, migrations, refactors, implementation verification |
| Architecture / material reasoning | Any available Opus-class or equivalent high-reasoning model | Architecture, ADRs, cross-service contracts, threat modelling, difficult trade-offs, final design review |
| Independent second opinion | **Fable** (fixed role per consult chain); any model independent from primary route | Challenge assumptions, identify gaps, review material ADRs, gateway/security changes, payment/ledger/KYC/AML design |
| Local-safe / continuity | LiteLLM to approved local Ollama aliases | Protected workloads, offline continuity, private review, local-only tasks |

“Fable 5” or any future model may be used once reachable through an approved route; it is a role candidate, not a required hard-coded model identifier.

## FCC and LiteLLM

- FCC is the local, loopback-bound Claude-compatible gateway for cloud-first development.
- LiteLLM is the approved local-safe and continuity route.
- Claude Code remains the planner/orchestrator and preserves its interface through FCC.
- Codex may execute code only under an approved task plan and must not independently alter policy, credentials, gateway configuration, or deployment state.

## Data and trust tiers

Cloud routes are available for all task classes except protected data. Protected data includes secrets, credentials, real customer data, real KYC/KYB/AML cases, payment or ledger payloads, production logs, and regulated evidence.

Protected data uses LiteLLM/local aliases. No automatic fallback may cross cloud and local trust tiers. A quota or provider failure produces an explicit reroute decision recorded in task evidence.

## Material-decision control

A material decision is any ADR, gateway/security change, provider/model policy change, payment/ledger design, KYC/KYB/AML design, or production-affecting change.

For every material decision:
1. produce a primary analysis;
2. obtain an independent second opinion (consult chain: Codex → Fable → Mistral → Kimi);
3. record disagreements and resolution;
4. obtain Operator approval;
5. obtain named MLRO approval where compliance, KYC/KYB/AML, payment controls, or regulated banking scope are affected.

**Consultation workflow:** Factory prepares brief → Operator conducts consultation → Results returned → Work resumes. See `factory-terminal-working-mode-v1.md` §2–4.

## Provider flexibility

Provider/model selection is allowlist-based, not brand-based. An eligible route may use any provider/model that:
- is reachable through FCC or the approved local route;
- has completed supply-chain and capability review;
- fits the task/data class;
- is recorded in task evidence.

No model is mandatory, and no approved model is excluded merely because a newer or stronger option becomes available.

## Activation controls

Before runtime activation: pinned source/build, loopback listener, explicit provider/model allowlist, egress/quota controls, audit records, kill switch, synthetic end-to-end test, and rollback test.

## Operating rule

When in doubt, maximise task capability within the task’s data class, then obtain independent review for material decisions. Do not replace a strong route with a weaker route merely to conserve tokens when the task is material.

## Evidence integrity and routing controls

These controls preserve engineering quality without restricting any eligible provider, model, or implementation tool.

### Explicit classification and fail-closed handling

Before execution, every task records an explicit route, model/tool role, data class, and trust tier. If any of these classifications is unknown, execution is deferred only until the accountable planner records the classification. The rule is classification-first, not provider-restrictive.

### Evidence integrity

For each material decision, task evidence records:
- the primary analysis reference and content hash;
- the independent-review reference and content hash;
- the reconciliation, including agreement, disagreement, and selected decision;
- the identities or accountable roles of planner, executor, reviewer, and approver;
- the explicit reroute record when quota, provider, or route availability changes.

Evidence is retained append-only or with an equivalent tamper-evident integrity mechanism.

### Independence and approvals

The independent reviewer for a material decision must use a distinct model invocation or approved review route from the primary material-analysis invocation. Operator approval is always identified; named MLRO approval is identified when the decision affects compliance, KYC/KYB/AML, payment controls, CASS 15, ledger controls, or regulated banking scope.

### Activation and continuity controls

Before a cloud provider/model route is activated, enforce tested quota and egress ceilings, a kill switch, a synthetic end-to-end test, and a rollback test. A quota or provider failure never silently changes trust tier; it produces a recorded reroute decision under the data boundary rules.

