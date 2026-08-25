# Developer Tools and Consultation Plane v6.1 — Guardrail Amendment

**Status:** Policy amendment only. No API call, plugin installation, credential read/write, runtime activation or configuration mutation.
**Applies to:** Codex plugin/CLI, Mistral API, Mistral Vibe, Kimi, DeepSeek, Fable 5, OpenRouter routes and local-safe aliases.

## Universal separation of duties

No participant may approve its own analysis, execution, verification, test evidence, route proof, rollback proof or policy change.

A participant is treated as the same participant when it shares any of:
- the same model run or session;
- the same agent identity or automation identity;
- the same human operator acting without an independent reviewer;
- the same evidence author or evidence-producing workflow.

Required separation:
- Primary analyst cannot be the sole approver.
- Executor cannot be the sole verifier or approver.
- Evidence producer cannot attest solely to its own evidence.
- Codex may execute and verify technical tests, but a distinct reviewer/approval identity is required for acceptance.
- Mistral Vibe, Mistral API, Kimi, DeepSeek and Fable 5 may consult or draft, but cannot approve their own work.

## Fail-closed route rule

A route must fail closed when any of the following is true:
- Route is unknown, unclassified, unpinned, disabled or absent from the allowlist.
- Exact provider, model ID, version, region or egress posture is missing.
- Data class is protected, mixed or unknown and the target is cloud.
- F9 revalidation fails: allowlist, capability, role, data class, trust tier, quota, egress, evidence or rollback.
- Required synthetic proof, negative proof, rollback proof, immutable evidence or approval is absent or expired.
- Provider returns outage, quota/rate-limit denial, authentication failure or incompatible capability response.
- Reviewer separation, reviewer identity, named approval or dissent record is missing.

On failure:
1. Block dispatch and do not make an inference call.
2. Record a non-secret decision/evidence event with reason code and route identity.
3. Do not silently reroute across provider, tier, trust boundary or data boundary.
4. Require a new explicit route decision and complete F9 revalidation before any reroute.
5. For protected/mixed/unknown data, allow only authenticated local-safe routes; if unavailable, stop.

## Controlled availability

“Permanently available” means a tool may be installed and registered for governed use. It never means an automatic authority to receive data, invoke a model, modify code, approve work or bypass route gates.

## Review closure

This amendment addresses the two Codex review findings:
- universal no-self-approval language;
- explicit unavailable/unclassified route fail-closed behavior.
