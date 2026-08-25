# Smart Model Routing: Evidence Bundle

Scope: policy and canon only. No source code, secrets, credentials, customer data, provider keys, logs, or payment payloads are included.

## software-factory-canon-v1.md
15: - **Claude Code** acts as planner, reviewer, and orchestrator.
17: - LiteLLM provides approved local fallback routing to Ollama endpoints; FCC is the approved Claude-compatible cloud-first development gateway.
21: - Cloud LLM calls are permitted only through the FCC local gateway and approved allowlisted providers/models, subject to the Cloud-first development routing amendment.
30: - Compliance-sensitive workflows (AML/KYC, CASS 15, payment routing).
37: - Third-party SaaS integrations not routed through LiteLLM.
48: | INV-02 | LiteLLM is gateway-only (no direct Ollama calls from agents) | LiteLLM config, network policy |
51: | INV-05 | No secrets in commits | .gitignore, Guardian F7/project deny patterns |
68: | **Reviewer** | Claude Code | Reviews diffs, checks invariants, approves/defers | Git diff, Read, Grep |
78: | **MLRO** | [UNKNOWN — to be designated] | Compliance sign-off on AML/KYC changes, CASS 15 reconciliation, payment routing |
93: All agent requests are routed through LiteLLM. Direct Ollama calls are prohibited.
104: Route binding is defined in `litellm/litellm-config.v2.yaml` and is the single source of truth.
116: | **P3: Evaluation Pack** | Test results (pytest), lint results (ruff), type check (mypy) | Reviewer (Claude Code) |
118: | **P5: Evidence Pack** | PR link, operator sign-off record, MLRO sign-off (if compliance), rollback plan | Operator / MLRO |
125: plan -> route -> execute -> evaluate -> review -> promote/defer
139: - Claude Code selects the appropriate LiteLLM alias for the task.
140: - Request is routed through LiteLLM gateway to the target Ollama endpoint.
157: ### 7.5 Review
159: - Claude Code reviews the diff, test results, and Guardian verdicts.
161: - If any verdict is WARN: reviewer may proceed with documented justification.
191: - Changes touch compliance paths: `compliance/cases/`, `kyc/raw/`, payment routing.
192: - AML/KYC validation logic is modified.
198: - New model added to LiteLLM config.
234: 7. PR approved by at least one human reviewer.
279: ## Appendix A: Evidenced Capabilities
283: | Capability | Evidence |
289: | LiteLLM gateway | `litellm/litellm-config.v2.yaml` |
291: | HITL risk matrix | `guardian/src/memory_loader.py` (HITL-MATRIX.yaml) |
299: ### Unevidenced / Unknown
328: ## Cloud-first development routing amendment
332: 1. **Primary development route:** Claude Code-compatible requests may be routed through a local Free Claude Code (FCC) gateway to an explicit allowlist of cloud providers/models.
333: 2. **Compatibility boundary:** FCC preserves the Claude Code interface; direct provider calls by agents remain disallowed unless separately approved.
334: 3. **Local continuity:** LiteLLM and local Ollama remain approved fallback routes for offline operation, continuity, and protected workloads.
335: 4. **Data boundary:** Cloud routes MUST NOT receive secrets, credentials, real customer data, KYC/KYB/AML cases, payment or ledger payloads, production logs, regulated evidence, or other sensitive banking data.
336: 5. **Permitted cloud work:** Synthetic fixtures, non-sensitive architecture/design, ADRs, code scaffolding, tests, migrations, documentation, and sanitized debugging.
337: 6. **Controls:** Provider/model allowlist, loopback-bound gateway, task/route/model audit records, spend/quota limits, credential isolation, and tested rollback are mandatory before provider activation.
338: 7. **Architecture boundary:** FCC accelerates development only. Banking architecture remains based on domain patterns: double-entry ledger, CQRS/event sourcing, KYC/AML orchestration, and ISO 20022/payment adapters.

## CLAUDE_CODE_CANON.md
31: > already canon (`software-factory-canon-v1.md` §4.1 Planner/Executor/Reviewer) — this adds the
38: - **CENTRAL = the brain (Claude Code planner/reviewer/orchestrator).** [ФАКТ] `software-factory-canon-v1.md`
40: (§7 plan→route→execute→evaluate→review→promote/defer).
58: 2. **Never self-execute code.** CENTRAL plans/reviews; execution is routed to LEFT/Aider (INV-01). [ФАКТ]
63: 5. **Cloud-first development is permitted through FCC.** Claude Code routes through a local FCC gateway to approved allowlisted cloud models; LiteLLM/local inference remains the fallback. Sensitive banking data must remain local.
78: ## Cloud-first development routing amendment
82: 1. **Primary development route:** Claude Code-compatible requests may be routed through a local Free Claude Code (FCC) gateway to an explicit allowlist of cloud providers/models.
83: 2. **Compatibility boundary:** FCC preserves the Claude Code interface; direct provider calls by agents remain disallowed unless separately approved.
84: 3. **Local continuity:** LiteLLM and local Ollama remain approved fallback routes for offline operation, continuity, and protected workloads.
85: 4. **Data boundary:** Cloud routes MUST NOT receive secrets, credentials, real customer data, KYC/KYB/AML cases, payment or ledger payloads, production logs, regulated evidence, or other sensitive banking data.
86: 5. **Permitted cloud work:** Synthetic fixtures, non-sensitive architecture/design, ADRs, code scaffolding, tests, migrations, documentation, and sanitized debugging.
87: 6. **Controls:** Provider/model allowlist, loopback-bound gateway, task/route/model audit records, spend/quota limits, credential isolation, and tested rollback are mandatory before provider activation.
88: 7. **Architecture boundary:** FCC accelerates development only. Banking architecture remains based on domain patterns: double-entry ledger, CQRS/event sourcing, KYC/AML orchestration, and ISO 20022/payment adapters.

## factory-target-model-policy.md
7: 1. Routine factory execution should lean on Codex/plugin-oriented flow where possible.
9: 3. Main verification/review must be performed by a stronger review model.
10: 4. A separate Codex opinion must be used as an additional signal.
11: 5. When a quota or rate limit is hit, the stack must automatically switch to a fallback model/provider.
15: - Verification role: stronger cloud review/reasoning model.
16: - Independent second opinion: Codex.
17: - Emergency continuity: fallback chain through FCC.
19: ## Required FCC design
20: FCC must be configured as the stable gateway layer.
21: Claude Code-compatible traffic must go through FCC.
27: - Fable-tier slot: primary verification/review model.
28: - Additional Codex lane: independent comparison signal.
29: - Fallback chain: automatic substitution when limits, downtime, or provider errors occur.
34: - Stronger model for review and verification.
35: - Independent second opinion before risky acceptance.
42: - reviewer
43: - second opinion
44: - fallback replacement

## cloud-first-fcc-policy.md
1: # CLOUD-FIRST FCC POLICY
4: The primary target is cloud-first routing through Free Claude Code.
5: Ollama must not be the strategic focus.
6: Ollama is optional only as a last-resort local fallback.
12: 4. Kimi / Moonshot (through supported FCC provider path)
16: - FCC stays the local proxy gateway.
20: ## Required operator intent in FCC Admin UI
24: - Configure fallback to another cloud provider.
25: - Move local Ollama to last fallback or disable it.
33: - FCC internal provider/model routing to cloud-first only.
36: Any wording or config that makes Ollama the implied default is incorrect for this project direction.

## operator-fcc-cloud-cutover.md
1: # OPERATOR CUTOVER — FCC CLOUD-ONLY STACK
4: Primary runtime for Claude Code must use strong cloud models through Free Claude Code.
6: Allowed role for local models: emergency fallback only, or fully disabled.
9: - FCC is a public open-source proxy project that routes Claude Code-compatible traffic to alternative providers while keeping the Claude Code interface.
10: - Claude Code supports gateway routing through ANTHROPIC_BASE_URL and gateway credentials through ANTHROPIC_AUTH_TOKEN.
12: - Therefore the correct target architecture is cloud-first via FCC, documented at project level and applied consistently across terminals.
18: 3. Kimi/Moonshot — strong reasoning candidate if exposed through FCC/NIM/OpenRouter path.
19: 4. DeepSeek — cheap fallback / factory tier.
20: 5. Ollama — emergency-only fallback, not primary.
29: 1. Open FCC Admin UI.
30: 2. Replace current primary local Ollama model with a strong cloud model.
31: 3. Configure fallback chain using cloud providers only.
32: 4. Move Ollama to last-resort fallback or remove it.
33: 5. Keep project docs and settings aligned with the cloud-first policy.
37: - cloud-first AI routing
48: But FCC internal provider/model routing must be changed to cloud-first.
54: 4. Add cloud-only fallback chain.
55: 5. Demote/remove Ollama.
61: The strategic direction is cloud-first through FCC.

## ADR-032-cloud-fcc-gateway-amendment-DRAFT.md
1: # ADR-032: Cloud/FCC Gateway Amendment — DRAFT
11: Permit an explicitly governed cloud-capable inference route for approved non-production AI workloads through an approved local gateway boundary, while preserving a local LiteLLM route as a fallback.
15: - INV-02 currently names LiteLLM as gateway-only and prohibits direct Ollama calls by agents.
17: - FCC/cloud-first drafts are not canonical and conflict with both invariants.
18: - FCC source pre-check: GitHub-verified commit `f8a3b119972532c3204b7f0aae2ab1076bc1cf02`; installer and server not run.
22: 1. Gateway: FCC may operate only as a local, loopback-bound Claude-compatible proxy.
23: 2. Cloud routes: opt-in allowlist only; default deny; no automatic provider fallback across trust tiers.
24: 3. Local route: LiteLLM remains available as an independently operable local fallback.
25: 4. Workload policy: no customer data, secrets, production logs, regulated evidence, or payment/ledger payloads to cloud routes.
26: 5. Secrets: provider credentials only in local secret manager/FCC Admin UI; never Git, prompts, shell history, or audit reports.
29: 8. Kill switch: stop FCC listener, revoke provider credential, and route all agents to LiteLLM local aliases.
30: 9. Rollback: restore prior gateway environment; confirm no cloud credentials remain exposed; retain evidence pack.
37: - [ ] FCC installed in a disposable isolated environment, not global tool environment.
39: - [ ] Provider allowlist, egress rules, spend/quota limits, data-classification policy approved.
40: - [ ] Security review of dependency lockfile and runtime network destinations completed.
41: - [ ] End-to-end test uses synthetic non-sensitive prompt only.
42: - [ ] Rollback test completed and evidence attached.
48: - No FCC installation, server start, or cloud request until this ADR is approved.
60: This draft has no operational effect until both approval rows are completed and the corresponding canonical amendments are committed, reviewed, and promoted.
66: - **Decision:** Remove blanket local-only/cloud prohibition for development; adopt cloud-first development through FCC with the stated local-safe-data boundary.
67: - **Implementation status:** Canon wording updated; FCC runtime/provider activation remains separate, staged, and audited.

