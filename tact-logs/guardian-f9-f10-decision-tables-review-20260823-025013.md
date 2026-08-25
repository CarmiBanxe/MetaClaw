# Independent Review Bundle: F9/F10 Decision Tables

Review the draft below against the governing protocol. Confirm it preserves model/provider freedom while enforcing role, evidence and trust-tier controls. Identify any ambiguity that could accidentally deny a legitimate cloud-first development task or permit a protected-data leak.

## Governing Protocol
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
| Independent second opinion | A model/tool independent from the primary material-decision route; Codex is the initial approved implementation | Challenge assumptions, identify gaps, review material ADRs, gateway/security changes, payment/ledger/KYC/AML design |
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
2. obtain an independent second opinion;
3. record disagreements and resolution;
4. obtain Operator approval;
5. obtain named MLRO approval where compliance, KYC/KYB/AML, payment controls, or regulated banking scope are affected.

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



## Draft
# Guardian F9/F10 Role-Based Routing Decision Tables — Draft

**Status:** Draft for independent review; no runtime activation and no Guardian implementation change.
**Authority:** Smart Model Routing Protocol v1 governs role, route, trust-tier, evidence, and approval semantics.

## Scope

This specification replaces only brand-bound semantics in F9/F10. It preserves all unrelated Guardian rules and does not restrict any approved provider, model, or implementation tool.

## Common task evidence schema

Every new execution-capable task record must include:
- `task_id`
- `route_id` and `route_allowlisted=true`
- `role`: `planner`, `preparation`, `executor`, `reviewer`, or `approver`
- `data_class`: `public`, `synthetic`, `sanitized_internal`, or `protected`
- `trust_tier`: `cloud` or `local_safe`
- `invocation_id`
- `parent_invocation_id` where applicable
- `reroute_id` and immutable evidence reference if route changes
- `actor_identity` or accountable role identity

A material-decision record additionally requires primary-analysis hash, reviewer-analysis hash, reconciliation reference, identified Operator approval, and named MLRO approval where applicable.

## F9: route and trust-tier validation

| Condition | Verdict | Reason |
|---|---|---|
| Required routing fields present; route allowlisted; role compatible with route; data class permitted in trust tier | PASS | Explicit, policy-compliant route |
| Missing/unknown `route_id`, role, data class, trust tier, invocation ID, or allowlist status | DEFER | Fail closed until planner records explicit classification |
| `protected` data with `cloud` trust tier | BLOCK | Protected-data local-safe boundary |
| Cloud/local trust tier changes without immutable reroute evidence and explicit reclassification | BLOCK | Silent cross-tier fallback forbidden |
| Route not allowlisted or route/model capability not approved for requested role | BLOCK | Route governance failure |
| Quota/provider failure with recorded reroute and reclassification | PASS | Explicit continuity handling |

## F10: role separation and decision control

| Condition | Verdict | Reason |
|---|---|---|
| Non-material task has distinct planner and executor invocation; review optional under task policy | PASS | Normal delivery route |
| Material task has primary-analysis invocation, independent reviewer invocation, reconciliation, identified approver, and MLRO approval if applicable | PASS | Independent material-decision control |
| Same invocation holds planner and executor roles | BLOCK | Incompatible role collision |
| Same invocation holds executor and reviewer roles for its own output | BLOCK | Self-review prohibited |
| Same invocation holds primary analysis and independent-review roles | BLOCK | Independent-review failure |
| Same invocation holds reviewer and approver roles for material decision | BLOCK | Approval independence failure |
| Required role/evidence/approval absent or unknown | DEFER | Fail closed until evidence is complete |

## Legacy-evidence migration rule

Historical records that lack F9/F10 fields remain readable and auditable. They must be tagged `legacy_evidence=true`; they cannot authorize new execution, promotion, provider activation, or material-decision approval until an append-only migration record supplies the missing classification, route, role identity, and approval evidence. Migration must never fabricate historical facts; unknown values remain explicitly `unknown`.

## BANXE non-regression gate

F9/F10 migration must not weaken these domain invariants:
- double-entry balance and immutable ledger history;
- CQRS/event-sourcing boundaries and idempotent command handling;
- ISO 20022/payment adapter boundary;
- KYC/KYB/AML orchestration;
- named and independent MLRO approval for applicable regulated/compliance decisions.

## Required synthetic test matrix

1. Approved cloud route for synthetic/public/sanitized work.
2. Approved local-safe route for protected work.
3. Unknown field -> DEFER.
4. Protected data -> cloud -> BLOCK.
5. Silent cloud/local cross-tier fallback -> BLOCK.
6. Explicit reroute with immutable evidence -> PASS.
7. Planner/executor collision -> BLOCK.
8. Executor/reviewer collision -> BLOCK.
9. Primary-analysis/reviewer collision -> BLOCK.
10. Reviewer/approver collision for material decision -> BLOCK.
11. Material decision with complete reconciliation and approvals -> PASS.
12. Legacy record is readable but cannot authorize new execution until migrated.
13. BANXE synthetic balance, idempotency, immutable-history, ISO 20022 boundary and MLRO-independence non-regression tests.
14. Quota/egress ceiling, kill-switch, synthetic E2E and rollback evidence checks.
