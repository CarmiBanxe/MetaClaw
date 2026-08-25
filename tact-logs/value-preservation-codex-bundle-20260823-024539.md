# Value-Preservation Amendment Draft

**Status:** Draft for independent review; no runtime activation.
**Goal:** Preserve enforcement, evidence, reproducibility, and BANXE domain quality while keeping cloud-first, role-based model routing fully available.

## Retain unchanged
- Canon/README/skills preflight and recorded task evidence.
- Guardian/canon-judge infrastructure and regression tests.
- Backup, dry-run, staged activation, rollback, kill-switch and audit evidence.
- Pinned sources, lockfiles, hashes, signatures, dependency provenance and SBOM where available.
- Synthetic/sanitized-data workflow and protected-data local-safe route.
- BANXE domain invariants: double-entry ledger, CQRS/event sourcing, ISO 20022 boundary, KYC/AML orchestration, and independent MLRO branch.

## Adapt, do not remove blindly
- Legacy guardian checks mentioning local-only inference, Aider as sole executor, or LiteLLM gateway-only routing.
- Replace each with a testable Smart Model Routing Protocol equivalent:
  1. task preflight evidence exists;
  2. route is explicit and model/provider is allowlisted;
  3. protected data stays on local-safe route;
  4. no automatic cloud/local trust-tier crossing;
  5. material decisions have primary analysis, independent review, reconciliation, and required human approval;
  6. provider/runtime activation requires pinned build, synthetic test, rollback test, spend/egress controls.

## Do not restore
- Blanket no-cloud prohibitions.
- Aider-only or any sole-executor requirement.
- A single mandatory vendor/model.
- Gateway-only wording that prevents FCC cloud-first development.

## FABLE-5 DEPTH PARITY
For a material decision: preserve the detailed primary analysis, obtain a separate independent Codex opinion, record it verbatim, then publish a reconciliation that identifies agreement, disagreement, and the selected decision.

## Requested Codex review
Identify any missing high-value legacy safeguards and specify the minimal guardian-rule/test changes needed to enforce this amendment without reintroducing model or provider restrictions.


## Current Smart Routing Protocol

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


## Legacy Guardian Rule Excerpts

276:         prompt = (ctx.prompt or "").lower()
277:         # Check if prompt references a model directly instead of alias
278:         direct_ollama = re.search(r"ollama[:/]\S+", prompt)
279:         if direct_ollama and direct_ollama.group() not in {"ollama:chat:" + a for a in CANONICAL_ALIASES}:
280:             return RuleResult(
281:                 rule_id="F9",
282:                 verdict="WARN",
283:                 summary=f"Direct Ollama reference detected: {direct_ollama.group()}. Use canonical LiteLLM alias.",
284:                 reasons=["INV-02: LiteLLM is gateway-only"],
285:             )
286:         return RuleResult(rule_id="F9", verdict="PASS", summary="Route alias check passed", reasons=[])
288:     # ── F10: Role-action validation (Sprint 3, Software Factory Canon §4) ──
289:     def f10_role_action_validation(self, ctx: AuditContext) -> RuleResult:
290:         """Executor (Aider) cannot perform Reviewer actions and vice versa."""
291:         actor = getattr(ctx, "actor", "") or ""
292:         scope = (ctx.scope or "").lower()
293:         prompt = (ctx.prompt or "").lower()
294: 
295:         # If actor is aider and action looks like review (not code execution)
296:         if "aider" in actor.lower() and any(kw in prompt for kw in ["review", "approve", "defer", "reject pr"]):
297:             return RuleResult(
298:                 rule_id="F10",
299:                 verdict="WARN",
300:                 summary="Executor (Aider) performing Reviewer action — role boundary violation",
301:                 reasons=["INV-01: Aider is sole code executor, not reviewer"],
302:             )
303:         # If actor is claude-code and action is direct code write
306:                 rule_id="F10",
307:                 verdict="WARN",
308:                 summary="Planner/Reviewer (Claude Code) performing Executor action — delegate to Aider",
309:                 reasons=["INV-01: Aider is sole code executor"],
310:             )
311:         return RuleResult(rule_id="F10", verdict="PASS", summary="Role-action check passed", reasons=[])

## Legacy Guardian Test Excerpts

No matching excerpts found.