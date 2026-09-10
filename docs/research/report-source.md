# Banksy Director / Collective-Manus Engine — Deep Research

**Status:** FINAL RESEARCH SYNTHESIS — implementation not authorized  
**Audience:** Operator / Banksy project leadership / Factory architecture reviewers  
**Date:** 2026-08-27  
**Scope:** architecture, runtime, decision science, banking governance, agent safety, and OSS implementation choices for improving the Banksy Director engine.

## Research question

What architecture and governed implementation path can bring the Banksy project Director—a bank-wide and client-facing Manus-like engine—to the highest defensible level of capability, reliability, safety, and economic efficiency without creating duplicate sources of truth or granting an AI system banking authority?

## Direct answer

Banksy should not be improved by adding more peer agents or another all-in-one framework layer. It should become a governed hierarchical control system whose durable unit is a typed task/intent record, not an agent conversation. The Director should remain a supervisory policy-and-routing role over deterministic workflow, specialist workers, independent verification, and human authority. Mastra is a strong candidate for the TypeScript client-Director runtime and typed interaction workflows; it is not a replacement for banking governance, Temporal, LedgerPort, or the independent MLRO/Audit lines.

The highest-value improvement is a **Constrained Hierarchical Director** built around:

1. an evidence-backed belief state;
2. a hierarchical planner with explicit uncertainty and bounded objectives;
3. a deterministic policy/authorization shield outside the model;
4. durable, idempotent effects through Temporal and domain ports;
5. independent validation and human/legal authority;
6. immutable lineage from intent to real-world outcome.

## Scope and assumptions

- The seven-layer reference architecture, four-layer macro architecture, and eight-capability unified-engine draft are treated as different resolutions, not automatically as contradictory canons.
- Runtime claims are accepted only when supported by live code or a dated measurement; design documents are not runtime evidence.
- The discovery corpus target is 300 unique sources. Consequential recommendations will rely primarily on official repositories/documentation, original research, standards, and regulators.
- GitHub issues, Hacker News, forums, and Reddit are used to discover recurring operational failure modes, not to establish prevalence or causal effect.
- Regulatory conclusions are architectural guidance, not legal advice.

## Current-state audit

### Repository and runtime separation

1. `/home/mmber/projects/banksy` is an uncommitted downstream art/design-layer repository, not the engine runtime.
2. The directly inspectable Banksy runtime is `/home/mmber/banxe-emi-stack/services/banking-engine`.
3. Its LangGraph graph is a single sandbox node with no live banking tools.
4. Its B7 validation substitutes a simulated graph flow; green tests establish HITL invariants on the tested surface, not full LLM→tool→ledger integration.
5. `ceo_orchestration_agent` is described as PROPOSED/STUB; service implementation is not established.
6. The unified Banksy–Legion assembly is specified but its completion and current live status are not established.

### Open capability gaps

- A2A/inter-agent contract.
- Intent Dispatcher deployment.
- Tool Registry/MCP runtime binding.
- Semantic memory deployment and ownership boundary.
- Execution-sandbox enforcement.
- Durable financial execution and idempotency evidence.
- Independent evaluation/monitoring that the acting agent cannot rewrite.
- Client-facing intent surface linked to the governed backend.

## Evidence synthesis

### Corpus accounting and stopping rule

The research began from 736 unique external URLs already present in the repository corpus. A 300-source decision corpus was selected and deduplicated across four lanes:

| Evidence lane | Sources | Use |
|---|---:|---|
| Agent/runtime projects and official documentation | 100 | Architecture, maintenance, licensing, HITL, memory, MCP, durability, sandbox, observability |
| Mathematics, control, multi-agent theory, organizational economics and bank governance | 90 | Decision contract, hard constraints, uncertainty, incentives, independent control |
| Local Banksy/Legion code, canons, audits and dated runtime evidence | 42 | Current-state truth and divergence detection |
| Regulators, standards, security research, industry cases and community failure signals | 68 | Operational/regulatory boundary, adversarial cases and disconfirming evidence |
| **Total** | **300** | |

Community sources were retained only as discovery signals. No safety, regulatory or framework-selection claim depends on Reddit or forum consensus. Broad discovery stopped because additional queries mostly repeated framework marketing and already-covered failure modes; the remaining unknowns require Banksy-specific experiments, not more generic sources.

### Emerging architecture finding

The strongest evidence across agent frameworks, multi-agent benchmarks, operational reports, and banking governance points toward a separation of concerns:

1. deterministic policy and authorization;
2. typed intent/task state;
3. constrained planner/router;
4. specialist agent/tool execution;
5. independent verification;
6. durable workflow and compensation;
7. evidence/lineage and evaluation;
8. human and independent-control authority.

Free-form peer-agent debate is unsuitable as the control mechanism for payments, compliance decisions, agent activation, or resource allocation.

### Framework conclusion

- **Temporal:** monetary/durable execution authority.
- **LangGraph or PydanticAI:** shortlist for the internal typed decision graph. PydanticAI deserves a formal challenger PoC because its typed contracts and official durable-execution integrations fit the existing Python contour.
- **Mastra:** preferred candidate for the TypeScript Client Director and HITL-aware interaction workflow.
- **DeerFlow/OpenHands:** pattern and component donors for an isolated research/artifact workbench, never a bank-privileged runtime.
- **OpenManus/OpenManus-RL:** reference/training material, not a regulated execution core.
- **AutoGen:** no new strategic dependency; its official ecosystem is transitioning toward Microsoft Agent Framework.
- **CrewAI/Agno/Flowise/Dify/n8n:** pattern or narrow adapter candidates only. n8n is source-available rather than OSI open source; Dify/Flowise require version-specific licence/security review.

No existing framework should be adopted wholesale. Banksy contracts, permissions, evidence and outcomes remain the SSOT; frameworks remain replaceable adapters.

### Mathematical decision contract

For each proposed decision `d`, the engine must record:

- `b(s|e)`: belief over relevant state given evidence and provenance;
- `A_safe(s, policy)`: actions allowed by hard policy and current authorization;
- lexicographically ordered objectives: law/safety/solvency/privacy → customer duty/risk appetite → efficiency;
- tail-risk measures, stress loss and ambiguity set;
- value of additional information;
- abstain/escalate threshold;
- idempotency key, approval binding, timeout and compensation/recovery path;
- accountable human/control function and immutable outcome receipt.

Expected utility or model confidence can rank only actions already inside `A_safe`. A reward, confidence score, majority vote or cost saving can never override a hard invariant.

### Security and identity conclusion

GitLab's composite-identity pattern is directly reusable conceptually: every agent action should carry both the initiating human/customer identity and a distinct service-agent identity, with effective permission equal to their intersection. The approval must bind tenant, subject, tool, canonical arguments, policy version, expiry and nonce. Tool schemas forbidden to the task must be removed before model context, and the canonical call must be authorized again at execution.

MCP and skills introduce their own supply-chain and privilege risks. Required controls include signed/pinned skills, deny-by-default network/filesystem access, short-lived credentials, tool provenance, context isolation, pre-execution authorization, post-effect receipts and full revocation inventory.

## Target architecture (draft)

### Plane A — Authority and policy

Human CEO, Board reserved matters, independent MLRO/Internal Audit, BPR/policy-as-code, risk appetite, promotion gates, and tool entitlements. No LLM writes this plane at runtime.

### Plane B — Director control plane

Typed intent normalization, task decomposition, dependency graph, routing, budgets, timeouts, escalation, confidence calibration, and stop conditions. The Director proposes and coordinates; it does not inherit human authority.

### Plane C — Execution plane

Specialist agents and deterministic composite tools. Tool visibility is task-scoped and least-privilege. Every state-changing tool supports dry-run, idempotency key, receipt, and compensating/recovery semantics where applicable.

### Plane D — Durable state and memory

Temporal-backed business execution; append-only task/event record; segregated conversational, episodic, semantic, policy, and evidence memories. Conversation history is not the system of record.

### Plane E — Verification and control

Deterministic invariants first, independent model/checker second, human/SMF gate where required. The acting model cannot select or alter its own acceptance tests.

### Plane F — Observability and learning

End-to-end correlation IDs, traces, tool receipts, cost/latency, outcome labels, drift monitoring, replayable scenarios, and offline improvement proposals. No self-modifying production policy.

### Plane G — Client Director

Mastra/TypeScript candidate for web/mobile intent interaction, typed workflows, MCP adapters, memory, and HITL presentation. All banking actions cross the governed API boundary; no direct ledger access.

### Plane H — Research workbench

DeerFlow/OpenHands-derived long-horizon research, browser and artifact capabilities run in an isolated zone without ledger credentials or production memory. Outputs are evidence packages, never banking actions. Promotion into the bank passes typed contracts, malware/content checks, DLP, provenance review and human/policy gates.

## Improvement program

### P0 — establish truth and authority

1. Ratify one canonical engine repository and reconcile the contradictory `DRAFT / canonical` unified-engine status.
2. Re-measure current runtime; retire stale `ONLINE`, `DEPLOYED` and module-count claims that cannot be reproduced.
3. Freeze the Python sandbox as an executable specification until each behavior maps to a production contract; it must not remain a second production implementation.
4. Ratify Director authority boundaries: proposal/planning only; no money movement, AML disposition, policy/model approval, permission change or self-activation.
5. Implement workflow-level inventory and classification by entity, jurisdiction, customer impact, data class, AI-risk/MRM tier, DORA criticality, vendor dependency and accountable officer.

### P1 — build the reliable spine

1. Define versioned `IntentRecord`, `TaskRecord`, `DecisionRecord`, `ApprovalToken`, `ToolCall`, `EffectReceipt` and `EvidenceRecord` schemas.
2. Implement A2A contract before increasing agent count.
3. Implement the Intent Dispatcher as a deterministic typed router with model-assisted classification only inside explicit bounds.
4. Bind task-scoped tools through a capability-filtered registry; re-authorize every call.
5. Make Temporal the boundary for all irreversible or money-adjacent effects.
6. Add loop, token, time, effect and monetary budgets plus circuit breakers and safe-state transitions.
7. Make abstention and escalation successful terminal outcomes.

### P2 — memory and intelligence

1. Separate conversational, episodic, semantic, policy and evidence memory.
2. Enforce tenant, role, purpose, retention and deletion boundaries independently for each class.
3. Add provenance, effective-time and supersession metadata; retrieval must not silently treat stale policy as current.
4. Use causal analysis and sensitivity checks for strategic interventions; predictive correlation alone cannot justify policy action.
5. Use value-of-information to decide whether to search, ask, simulate, escalate or stop.

### P3 — independent assurance

1. Deterministic invariants first; heterogeneous model/checker second; human/SMF gate where required.
2. Replace blanket 2-of-3 consensus with risk-weighted validators and explicit veto semantics.
3. Keep CRO, MLRO, Internal Audit and model validation organizationally independent with separate data paths, incentives, reporting and kill rights.
4. Add champion/challenger evaluation, drift/outcome monitoring, periodic reapproval and vendor exit/rollback.

### P4 — Client Director pilot

Run Mastra only in a sandbox Client Director slice:

`inform → prepare → policy precheck → suspend → human/SCA → Temporal execution → receipt`.

Go/no-go requires tenant isolation, no direct ledger path, non-bypassable HITL, duplicate-resume safety, Temporal idempotency, PII-filtered tracing, package-level licence/SBOM audit, fail-closed Guardian behavior and correlation from Mastra run to ledger outcome.

### P5 — adversarial maturity ladder

Progress through offline replay → digital twin → shadow mode → canary limits → bounded delegation. Test prompt injection, tool poisoning, skill supply chain, duplicate execution, deadlock, stale memory, correlated-agent failure, evaluator sabotage, third-party outage, partial success and recovery. Promotion depends on measured outcomes, not benchmark eloquence or passed happy-path tests.

## Success metrics

- Zero unauthorized effects and zero duplicate money movement.
- Every external effect has an authorization and receipt.
- Recovery point/time objectives met under injected failure.
- Calibrated uncertainty and selective accuracy improve as the system abstains.
- Human escalation rate is risk-appropriate rather than minimized blindly.
- Customer-outcome, compliance, tail-risk and operational-resilience counter-metrics accompany efficiency KPIs.
- Full lineage is reconstructible without relying on hidden chain-of-thought.
- Framework replacement does not change canonical banking contracts.

## Consolidated recommendations

1. Ratify one canonical engine repository and one runtime ownership map before framework adoption.
2. Build the typed Intent/Task/Decision/ToolReceipt contracts before adding new agents.
3. Implement Director as a hierarchical state machine with explicit termination and escalation—not a persona prompt.
4. Retain Temporal for money-moving durability; test Mastra–Temporal integration only through an adapter.
5. Use Mastra only for the client-facing TypeScript contour until proof-of-fit passes.
6. Replace blanket 2-of-3 LLM consensus with risk-weighted heterogeneous verification and deterministic invariants.
7. Introduce adversarial and counterfactual evaluation, including sabotage, prompt injection, duplicate execution, deadlock, stale memory, and silent partial failure.
8. Separate five memory classes and prohibit cross-tenant or cross-control-plane leakage.
9. Add economic controls: value-of-information stopping, cost/risk budgets, bounded search, and utility constrained by hard regulatory invariants.
10. Treat every external framework as a replaceable adapter; Banksy contracts and evidence remain the SSOT.

## Material disagreements and limitations

- Older documents call LangGraph deployed, while directly inspected code shows only a minimal sandbox graph and simulated E2E routing. “Deployed” therefore does not mean the complete Director capability is deployed.
- A July report called a 32-module skeleton ONLINE, but also disclosed placeholder inference and absent live MCP/ledger. Current liveness has not been re-measured.
- The unified-engine document is described as canonical inside its body but is also marked DRAFT / NOT FOR MERGE. Its governance status requires reconciliation.
- Framework feature presence does not establish banking-grade correctness, operational resilience, or regulatory suitability.
- This draft becomes final only after the 300-source ledger is deduplicated, consequential claims are spot-checked, and the recommendation matrix is completed.

## Source ledger

The claim-to-source ledger is maintained in `docs/research/banksy-director-300-source-ledger.md`.
