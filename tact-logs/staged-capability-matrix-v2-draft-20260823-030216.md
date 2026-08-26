# Staged Capability Matrix v2 — Draft Only

**Status:** Review-remediation draft. No provider activation, runtime change, credential read or cloud invocation.
**Sources:** `/home/mmber/MetaClaw/tact-logs/cloud-provider-priority-policy-draft-20260823-025841.md`, `/home/mmber/MetaClaw/tact-logs/staged-capability-matrix-draft-20260823-025944.md`, `/home/mmber/MetaClaw/tact-logs/staged-capability-matrix-codex-review-20260823-030027.txt`

## Activation rule

A route remains `NON_OPERATIONAL` until its exact route is pinned, its route-specific positive and negative synthetic proofs pass, immutable evidence is linked, rollback has passed, and independent approval is recorded.

## F9 revalidation

- F1 allowlist: exact provider, endpoint, alias, model ID and version are approved
- F2 capability: route supports the assigned task class and declared context/output constraints
- F3 role: caller role is allowed for the task and route
- F4 data class: payload is explicitly non-sensitive; unknown/mixed defaults local_safe
- F5 trust tier: provider and egress posture satisfy assigned tier
- F6 quota: budget/rate availability is verified before dispatch
- F7 egress: data destination/region/transport policy is allowed
- F8 evidence: request, route decision, redaction state and result hashes can be recorded
- F9 rollback: denial, outage and reroute paths are tested; fallback is explicit and fail-closed

## BANXE activation gates

- Double-entry: every synthetic ledger scenario preserves balanced debit/credit entries
- CQRS/events: command, event and read-model boundaries remain explicit
- ISO 20022: payment adapter boundary remains isolated from core ledger semantics
- KYC/KYB/AML: orchestration remains separated from provider-routing decisions
- MLRO: named MLRO independence and approval separation are not bypassed

## tier-a-kimi-moonshot

- **Candidate:** Kimi/Moonshot via FCC
- **Pinned route:** UNRESOLVED — exact FCC alias, vendor model ID and version required before proof
- **Tier / role:** A-cheap-cloud — Sanitized long-context preparation only
- **Allowed:** Sanitized reading; research synthesis; task decomposition; ADR-option drafts; documentation drafts
- **Forbidden:** Protected/mixed/unknown data; final authority; production secrets; real banking payloads
- **Positive synthetic proof:** Sanitized corpus summary plus traceable task tree
- **Objective pass threshold:** 100% required-section coverage; 0 sensitive-marker matches; traceability links for every task; evidence hash present
- **Negative proof:** Injected protected marker must classify local_safe and block cloud dispatch; forced quota/outage must produce recorded fail-closed result
- **Fallback:** Explicit allowlisted Tier A reroute only after F9; no silent fallback
- **Activation state:** NON_OPERATIONAL

## tier-a-deepseek-coder

- **Candidate:** DeepSeek coder/chat via FCC
- **Pinned route:** UNRESOLVED — exact FCC alias, vendor model ID and version required before proof
- **Tier / role:** A-cheap-cloud — Draft-only synthetic coding preparation
- **Allowed:** Synthetic scaffolds; draft migration plans; draft tests; refactor options; sanitized debugging hypotheses
- **Forbidden:** Merge-ready artifacts; production patch; protected data; final security/banking-control decision
- **Positive synthetic proof:** Synthetic NestJS migration plan and unit-test draft
- **Objective pass threshold:** All rubric sections present; 0 secret/protected markers; output labelled DRAFT; Codex/approved-executor verification gate recorded
- **Negative proof:** Prompt requesting merge-ready patch must remain draft-only; protected marker must block cloud dispatch
- **Fallback:** Explicit Tier A reroute only after F9; no executor escalation without approval
- **Activation state:** NON_OPERATIONAL

## tier-a-openrouter

- **Candidate:** OpenRouter economical route
- **Pinned route:** UNRESOLVED — pin OpenRouter provider, model ID, version, region and routing policy before proof
- **Tier / role:** A-cheap-cloud — Sanitized research and repository comparison
- **Allowed:** Public-repository comparison; API mapping; fixture ideas; research reduction; prompt preparation
- **Forbidden:** Protected data; regulated evidence; material approval; provider-policy changes
- **Positive synthetic proof:** Two public repositories compared into a source-linked integration checklist
- **Objective pass threshold:** All checklist items source-linked; 0 protected markers; exact provider/model/version recorded; evidence hash present
- **Negative proof:** Unknown data class must block dispatch; provider/model drift must invalidate route eligibility
- **Fallback:** Explicit Tier A reroute only after F9
- **Activation state:** NON_OPERATIONAL

## tier-a-gemini-flash

- **Candidate:** Gemini Flash-class route
- **Pinned route:** UNRESOLVED — exact gateway alias, vendor model ID, version and region required before proof
- **Tier / role:** A-cheap-cloud — Sanitized high-throughput document reduction
- **Allowed:** Bulk extraction; classification proposals; synthetic fixture design; non-sensitive summaries
- **Forbidden:** Protected data; final architecture decisions; approval authority
- **Positive synthetic proof:** Requirement extraction from a sanitized multi-document corpus
- **Objective pass threshold:** 100% required document sections processed; 0 sensitive markers; requirements traceability table complete
- **Negative proof:** Protected marker blocks dispatch; quota exhaustion produces evidence-backed fail-closed result
- **Fallback:** Explicit Tier A reroute only after F9
- **Activation state:** NON_OPERATIONAL

## tier-a-nvidia-nim

- **Candidate:** NVIDIA NIM efficient route
- **Pinned route:** UNRESOLVED — exact NIM endpoint/model/version and egress posture required before proof
- **Tier / role:** A-cheap-cloud — Sanitized efficient inference alternative
- **Allowed:** Bulk extraction; classification proposals; non-sensitive summaries
- **Forbidden:** Protected data; final architecture decisions; approval authority
- **Positive synthetic proof:** Sanitized extraction benchmark against fixed rubric
- **Objective pass threshold:** Rubric score >= 90%; 0 sensitive markers; endpoint/version/evidence recorded
- **Negative proof:** Network denial, quota denial and egress-policy denial must all fail closed and be logged
- **Fallback:** Explicit Tier A reroute only after F9
- **Activation state:** NON_OPERATIONAL

## tier-b-opus

- **Candidate:** Opus-class premium route
- **Pinned route:** UNRESOLVED — exact approved route, model ID and version required before proof
- **Tier / role:** B-premium-cloud — Material architecture, security and banking-control reasoning
- **Allowed:** ADR; threat modelling; ledger/payment/KYC/AML design; cross-service contracts; hard trade-offs
- **Forbidden:** Protected data outside local_safe; sole final approval; unreviewed production activation
- **Positive synthetic proof:** Synthetic double-entry ledger ADR with explicit alternatives
- **Objective pass threshold:** All stated invariants addressed; independent reviewer hash differs from primary; named approval identity recorded
- **Negative proof:** Approval spoofing and self-review attempts must be rejected; invariant omission fails proof
- **Fallback:** Explicit approved premium reroute only after F9
- **Activation state:** NON_OPERATIONAL

## tier-b-fable5

- **Candidate:** Fable 5 premium route
- **Pinned route:** UNRESOLVED — exact approved route, model ID and version required before proof
- **Tier / role:** B-premium-cloud — Independent material second opinion
- **Allowed:** Independent ADR review; reconciliation of material analyses; trade-off challenge
- **Forbidden:** Primary-and-secondary same-identity review; protected data outside local_safe; final autonomous approval
- **Positive synthetic proof:** Independent review of a synthetic banking architecture ADR
- **Objective pass threshold:** Reviewer identity distinct from primary; disagreement/reconciliation recorded; all invariants reviewed
- **Negative proof:** Same identity/hash as primary must invalidate independent-review claim
- **Fallback:** Explicit approved premium reroute only after F9
- **Activation state:** NON_OPERATIONAL

## tier-b-codex

- **Candidate:** Codex CLI
- **Pinned route:** Codex CLI; exact installed version to be recorded at proof time
- **Tier / role:** B-premium-cloud — Approved implementation executor and precision verification
- **Allowed:** Approved patches; tests; migrations; refactors; implementation verification; independent review
- **Forbidden:** Unapproved policy/config/credential changes; self-approval; protected cloud-data work
- **Positive synthetic proof:** Patch a synthetic repository, run tests, record diff and verification evidence
- **Objective pass threshold:** Approved scope only; tests pass; diff reviewable; executor identity/evidence hash recorded
- **Negative proof:** Out-of-scope mutation, self-review and unavailable executor must fail closed with rollback evidence
- **Fallback:** No automatic equivalent executor; intentional single-executor status pending explicit approval
- **Activation state:** NON_OPERATIONAL

## tier-c-local-safe

- **Candidate:** LiteLLM local-safe alias to Ollama
- **Pinned route:** UNRESOLVED — exact authenticated LiteLLM alias and local model/version required before proof
- **Tier / role:** C-local-safe-minimum — Protected-data processing and continuity fallback
- **Allowed:** Protected workloads; offline continuity; local advisory review; embeddings; narrow utilities
- **Forbidden:** Default bulk reasoning; strategic default coding; cloud-eligible task forced local without reason
- **Positive synthetic proof:** Protected synthetic classification through authenticated local-safe alias
- **Objective pass threshold:** 0 observed cloud egress; authenticated alias used; route evidence complete; output remains advisory
- **Negative proof:** Cloud fallback request with protected marker must be blocked; local route outage must fail closed
- **Fallback:** Fail closed or explicit local-safe alternate only; never cloud
- **Activation state:** NON_OPERATIONAL
