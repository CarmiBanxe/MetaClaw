# Waku Agent → Banksy Director: evidence-based adoption assessment

**Audience:** Operator and Banksy architecture/governance reviewers  
**Date:** 2026-08-30  
**Decision:** whether any Waku Agent mechanism should improve Banksy Director  
**Status:** research conclusion; no dependency adoption or implementation authorization

## Executive answer

Waku Agent is useful to Banksy, but **not as another framework, runtime, memory store, or Director
layer**. Its strongest value is as a small, readable reference implementation for five engineering
patterns: an explicit bounded tool loop, per-turn event tracing, retrieval gating, separation of
deterministic evals from LLM-judged quality, and a cockpit that maps runtime events back to code.

Banksy should copy the **contracts and tests behind those patterns**, not import Waku wholesale.
The direct runtime is a personal-assistant teaching system. Its tool registry executes model-chosen
functions without a policy/identity/approval boundary; its SQLite memory is not a multi-tenant bank
record; its retrieval and graph gates fail open; its memory consolidation trusts model-produced
JSON; and its release gate announces `GATE OPEN` when the judge suite is skipped for lack of an API
key. Those choices can be reasonable for a laptop assistant, but they are incompatible with the
ratified Banksy Director boundary unless replaced by existing Banksy controls.

**Recommendation:** adopt a narrow **Waku-derived Harness Conformance Pack** inside the current
Banksy architecture. Do not add a Waku layer or production dependency. Priority: medium-high for
observability/eval ergonomics, low for runtime adoption.

## What was verified

The repository describes itself as a local-first, readable teaching blueprint built around
harness, loop, memory and eval/LLM-Ops. The repository currently exposes 325 commits and an MIT
software licence. The README distinguishes its software licence from the CC BY-NC-SA licence on
the architecture diagram. [Repository and README](https://github.com/ShenSeanChen/waku-agent),
[MIT licence](https://github.com/ShenSeanChen/waku-agent/blob/main/LICENSE).

The advertised “~95-line loop” is substantially accurate: `agent.py` is 114 physical lines and 94
lines of code. It sends the current messages and tool schemas to the model, executes every returned
tool call through the registry, feeds results back, and stops when the model stops requesting tools
or `max_iterations` is reached. It records iterations, token use and tool events through an observer.
[Loop source](https://github.com/ShenSeanChen/waku-agent/blob/main/waku/loop/agent.py).

The tool registry is equally simple: name, description, JSON schema and Python callable. Unknown
tools and exceptions become strings visible to the model. It contains no initiator identity,
tenant, entitlement intersection, policy version, approval token, idempotency key or effect receipt.
[Tool registry](https://raw.githubusercontent.com/ShenSeanChen/waku-agent/main/waku/tools/registry.py).

The memory design is more than “one SQLite file”: the queryable store uses SQLite/FTS5 for facts,
episodes and chat state, while procedural memory lives in skill/SOUL files and `MEMORY.md` is a
human-readable mirror. A small-model retrieval gate decides whether to search memory. On gate error
or malformed output it retrieves anyway. Consolidation batches unconsolidated chat, asks a model
to extract facts and one episode, then writes the resulting JSON to semantic and episodic stores.
[Memory overview](https://github.com/ShenSeanChen/waku-agent#the-whiteboard-maps-to-the-code),
[retrieval gate](https://github.com/ShenSeanChen/waku-agent/blob/main/waku/memory/retrieval_gate.py),
[consolidation](https://raw.githubusercontent.com/ShenSeanChen/waku-agent/main/waku/memory/consolidation.py).

The eval split is real and conceptually sound: deterministic pytest cases are separated from
DeepEval/LLM-judge cases. The release script blocks on any deterministic failure and blocks on a
judge failure when the active provider has a key. But without a key it records `judge=skipped` and
still prints `GATE OPEN — safe to release`; therefore “both suites must pass” is not universally
enforced by code. [Release gate source](https://raw.githubusercontent.com/ShenSeanChen/waku-agent/main/waku/ops/release_gate.py).

The security policy explicitly recognizes local key/memory exfiltration, unauthenticated gateways,
install-time dependency risks and prompt injection that causes real effects. That is evidence of
awareness, not evidence that the runtime implements a bank-grade authorization boundary.
[Security policy](https://github.com/ShenSeanChen/waku-agent/blob/main/SECURITY.md).

## Fit with the current Banksy Director

The ratified Banksy target already has the places Waku would otherwise occupy: L6 orchestration,
L3 governed memory, a closed FrontDoor tool registry, HITL, durable effects, lineage, and a bounded
Client Director. It also requires tenant/purpose separation, composite identity, pre-context tool
filtering, re-authorization at execution, idempotency and effect receipts. Waku therefore cannot be
a new layer or SSOT.

| Waku mechanism | Banksy value | Decision | Required Banksy adaptation |
|---|---|---|---|
| Explicit `reason → tool → observe` loop | Excellent educational and conformance oracle for one conversational turn | **ADOPT AS SPEC/PATTERN** | Express as a small typed TypeScript harness above FrontDoor; no direct effects |
| `max_iterations` hard stop | Useful but incomplete loop safety | **ADOPT + EXTEND** | Add token, time, money, effect and repeated-call budgets; safe terminal state |
| Observer events around LLM/tool calls | High value for debuggability | **ADOPT CONTRACT** | Emit canonical correlation/lineage events; redact PII; append effect receipts |
| Runtime-derived graph/dashboard | High value against documentation drift | **ADOPT PATTERN** | Render from canonical runtime registry/state, read-only; never become authority |
| Retrieval gate | Potential latency/context benefit | **PILOT** | Deterministic fast path first; calibrated classifier; fail-closed by data class; measure miss harm |
| SQLite + FTS5 personal memory | Good local prototype and test fixture | **DO NOT ADOPT AS BANK SSOT** | Keep current Banksy tenant-separated memory; SQLite only for isolated local replay fixtures |
| Batched memory consolidation | Useful lifecycle idea | **ADAPT CAREFULLY** | Store proposals with provenance/confidence; validate before promotion; never write policy/evidence memory |
| Deterministic vs judge eval split | Strong and directly reusable | **ADOPT** | Deterministic invariants remain vetoes; judge is advisory/risk-tiered and independent |
| Release-gate UX/history | Useful operator ergonomics | **ADOPT AFTER FIX** | Missing judge/config/evidence must be NOT_RUN/BLOCK where required; signed immutable evidence |
| Multi-gateway session continuity | Useful Client Director pattern | **ADAPT** | Preserve channel/source, customer/device identity and SCA; never merge tenant memory by conversation ID |
| Self-editing memory/SOUL/skills | Convenient personally, unsafe institutionally | **REJECT FOR GOVERNED PLANES** | Changes become proposals reviewed through Factory/policy gates; signed/pinned skills only |
| MCP/community skill loading | Ecosystem convenience | **REJECT BY DEFAULT** | Allowlisted, pinned, SBOM/licence-scanned adapters in sandbox; no arbitrary URL installation |
| Waku runtime/package wholesale | Duplicates Banksy loop, memory, tools, eval and routing | **REJECT** | Use selected patterns only; MIT notice if substantial code is copied |

## The concrete feature worth building

The best Waku-derived improvement is a **Director Harness Observatory and Conformance Pack**, not a
new assistant service. It has four deliverables:

1. **A minimal typed turn harness** that makes the Banksy conversational path legible:
   `IntentRecord → allowed tool schemas → model proposal → FrontDoor authorization → result/receipt
   → next proposal or terminal state`.
2. **A canonical event vocabulary**: `turn_started`, `memory_gate`, `model_proposed`,
   `tool_authorized|refused`, `effect_started`, `effect_receipted`, `escalated`, `turn_ended`.
   Every event carries correlation, tenant, initiator/service identity, policy version and redaction
   class; effect events additionally carry idempotency and receipt references.
3. **A release/eval dashboard generated from evidence**, separating deterministic invariants,
   conformance coverage, judge/advisory scores, missing suites and historical regressions. A missing
   required suite is red/NOT_RUN, never green.
4. **A retrieval-gate experiment** on non-policy conversational memory only. Compare always-retrieve,
   deterministic routing and small-model gating on latency, cost, false-skip harm, irrelevant-memory
   contamination and cross-tenant leakage. It cannot gate policy, evidence or authorization reads.

This work improves inspectability and test discipline without granting new authority or duplicating
the Director, FrontDoor, memory or durable execution SSOTs.

## Why not use the Waku loop directly

The loop executes all tool calls emitted by the model. The registry checks that a name exists and
catches exceptions, but it does not decide whether the initiating person and service agent jointly
have authority for the canonical arguments. Error-as-text also invites repeated model retries;
`max_iterations` bounds count but not duplicate external effects. There is no durable workflow,
idempotency receipt or compensation contract in the loop.

For a calendar assistant, those omissions are acceptable design simplifications. For Banksy they
are exactly the boundary already assigned to FrontDoor, HITL, Temporal/durable adapters and domain
ports. Wrapping Waku around those components would add indirection without adding a missing bank
capability.

## Memory judgment

Waku's useful memory lesson is **separation plus lifecycle**, not SQLite itself:

- retrieve only when relevant;
- distinguish semantic facts, episodes and procedures;
- consolidate in batches rather than summarizing every message;
- preserve a human-readable view;
- expose correction and forgetting.

Banksy must add controls that Waku does not need for one owner: tenant and purpose isolation,
effective/superseded time, provenance, retention/legal hold, erasure boundaries, evidence/policy
separation, encryption/key control and independent promotion of model-extracted facts. In particular,
model consolidation output must be a **memory proposal**, not an accepted fact. Operational receipts
and financial idempotency records must never be erasable conversational memory.

## Eval judgment

This is the highest-value transferable idea. Banksy should retain Waku's visible separation:

- deterministic checks answer “did the allowed action and exact effect occur?”;
- judged evals answer qualitative questions such as clarity or helpfulness;
- judge scores never override a deterministic refusal, invariant or human/SMF gate;
- the actor must not own the sole evaluator or modify its acceptance set;
- every required-but-unavailable suite blocks the relevant promotion instead of silently skipping.

The Waku code itself illustrates why source review matters: its README says the gate runs both
suites, while the implementation opens release when no judge key is present. Banksy should adopt
the transparent UX while explicitly fixing that semantic gap.

## Risk and duplication assessment

| Risk | Finding |
|---|---|
| Second orchestration SSOT | High if runtime imported; avoided by pattern-only adoption |
| Second memory SSOT | High if `state.db` introduced; no value given existing Banksy memory |
| Prompt/tool injection | Material: tools execute after name lookup, without task-scoped authorization |
| Memory poisoning | Material: model-extracted facts are written after structural JSON checks only |
| Cross-tenant leakage | Architecture not designed for multiple bank customers |
| Duplicate effects | `max_iterations` is not idempotency; external side effects need receipts |
| False green release | Confirmed when judge credentials are absent |
| Skill supply chain | Arbitrary/community skill installation is unsuitable for bank runtime |
| Licence | Core software MIT and compatible in principle; preserve notice. Diagram/media terms differ |
| Operational maturity | Active and readable, but explicitly a teaching blueprint with experimental/skeleton features |

## Adoption decision and gates

**Verdict: useful donor, unsuitable runtime.** Adopt only the Harness Observatory and Conformance
Pack patterns.

Before any code copy or dependency:

1. run a fresh ADR-102 duplication audit against the live bank-tree;
2. map every proposed event and eval to the existing lineage/evidence schemas;
3. prohibit new tool, memory, approval and workflow registries;
4. keep all experiments sandbox-only with synthetic data;
5. add negative tests for prompt/tool injection, memory poisoning, skipped evals, duplicate effects,
   stale memory and tenant substitution;
6. record MIT attribution for substantial copied code and exclude differently licensed diagrams;
7. require independent acceptance and a separate operator promotion decision.

## Limitations and stopping rule

This review inspected the public repository, its current README, core loop, retrieval gate,
consolidation, tool registry, release gate, security policy and licence. It did not install or run
the project, audit every dependency, watch the full video, or establish production reliability.
GitHub stars/forks and demos were not used as evidence of quality. Research stopped because the
decision hinges on directly verified architecture boundaries; additional promotional or community
sources would not change the runtime/adaptation conclusion. A package/SBOM and full dependency audit
is required only if Banksy later proposes importing code.

