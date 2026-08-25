# Mistral Onboarding & Route-Pinning Draft

**Status:** Draft only. No API call, key read, credential creation, config mutation or runtime activation.
**Evidence source:** read-only route inventory identified `codestral` as an existing textual candidate.

## Observed candidate

- Observed text candidate: `codestral`
- Operational interpretation: UNPINNED / NON_OPERATIONAL
- Reason: generic model label does not establish exact Mistral vendor model ID, version, gateway alias, workspace, region, or egress policy.

## Intended factory roles

- Tier A coding draft candidate: current supported Codestral or other exact Mistral coding model chosen from Studio.
- Tier B independent code-review candidate: exact pinned Mistral coding/reasoning model, after proof.
- Codex remains approved executor/verifier for merge-ready patches, tests and implementation verification.
- Mistral Vibe CLI, if later installed, is a developer interface only and does not bypass gateway, evidence or approval policy.

## Required controlled onboarding sequence

1. In Mistral Studio, confirm that API billing is active for a dedicated non-production workspace.
2. Set a low monthly workspace spend cap before generating any key.
3. Create a named, expiring API key only for `metaclaw-synthetic-staging`.
4. Store the key only in the existing secret-injection mechanism; never in repository files, logs or shell history.
5. Query allowed model IDs through the approved gateway path or Studio UI; do not assume `codestral` is current.
6. Pin exactly one supported vendor model ID plus gateway alias, region and egress posture.
7. Add one LiteLLM draft-only alias using `mistral/<exact-model-id>` and environment-based secret injection.
8. Run one positive and one negative synthetic proof, then a quota/outage/rollback proof.
9. Require immutable evidence and independent approval before changing `NON_OPERATIONAL`.

## Initial safe proof

- Input: synthetic public code fixture with no credentials, no customer data and no banking payload.
- Task: produce a draft unit-test plan and code-correction proposal.
- Pass: output is explicitly DRAFT; no data-boundary violation; complete route/evidence record; no unapproved mutation.
- Negative case: inject a protected-data marker and require cloud dispatch to block fail-closed.
- Rollback case: forced quota or upstream denial must be recorded without silent provider fallback.

## Guardrails

- `codestral` alone is not an approved exact model ID.
- Mistral Pro/Vibe subscription is not treated as proof of API credits or API key availability.
- Protected, unknown and mixed data remain local-safe only.
- No automatic fallback to Kimi, DeepSeek, OpenRouter or local models without F9 revalidation.
