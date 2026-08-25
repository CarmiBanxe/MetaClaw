# Provider Routing Sequence v5 — Draft

**Status:** Policy draft; no runtime activation.
**Mistral evidence:** API model discovery succeeded with HTTP 200; no inference was performed.

## Provider sequence

| Family | Exact route / status | Tier | Role | Activation state |
|---|---|---:|---|---|
| Kimi / Moonshot | kimi-k2.6 | A | strong long-context synthesis, document analysis, agent preparation | CANDIDATE_PIN_REQUIRED |
| DeepSeek | exact chat/coder alias unresolved | A | sanitized draft coding, migration/test drafts, refactor options | CANDIDATE_ALIAS_DISCOVERY_REQUIRED |
| Mistral | devstral-2512 | A | draft-only coding, synthetic code planning, test planning, codebase analysis | API_DISCOVERED_PIN_AND_PROOF_REQUIRED |
| Mistral | mistral-small-2603 | A | cost-efficient sanitized summaries, extraction and task decomposition | API_DISCOVERED_PIN_AND_PROOF_REQUIRED |
| Kimi / Moonshot | kimi-k3 | B | premium long-context material reasoning and large-corpus analysis | CANDIDATE_PIN_REQUIRED |
| DeepSeek | exact reasoning alias unresolved | B | independent challenging analysis and reasoning review | CANDIDATE_ALIAS_DISCOVERY_REQUIRED |
| Mistral | mistral-large-2512 | B | independent architecture, synthesis and material second opinion | API_DISCOVERED_PIN_AND_PROOF_REQUIRED |
| Mistral | magistral-medium-latest | B | reasoning-focused challenge review and ADR critique | API_DISCOVERED_PIN_AND_PROOF_REQUIRED |
| Codex | existing approved CLI route | EXECUTOR | approved implementation, tests, diff review and verification | EXISTING_EXECUTOR_POLICY_GOVERNED |
| Local-safe | approved authenticated local aliases | C | protected, mixed or unknown data; offline continuity | LOCAL_SAFE_ONLY |

## Routing rules

- No cloud provider receives protected, mixed or unknown data.
- No route is operational until exact alias/model/version, F9 revalidation, positive proof, negative proof, rollback proof, immutable evidence and independent approval exist.
- No silent provider, tier or data-boundary fallback.
- Codex remains executor/verifier; non-Codex coding routes are draft-only until separately approved.
- Mistral staging key is injected only for a bounded proof session and removed afterward.
- Mistral workspace spending cap must be set before any inference proof.

## Staged proof order

1. Pin and proof one Mistral Tier A route: `devstral-2512`.
2. Pin and proof one Kimi Tier A route: `kimi-k2.6`.
3. Discover, pin and proof one DeepSeek Tier A chat/coder route.
4. Compare evidence, cost and rollback behavior without changing production routing.
5. Only then nominate Tier B routes: Kimi K3, DeepSeek reasoning, Mistral Large and Magistral.

## Mistral proof boundary

- Synthetic public code fixture only.
- Draft test plan and code-correction proposal only.
- No real repositories, credentials, banking payloads or customer data.
- Required negative test: protected marker blocks dispatch.
- Required resilience test: quota/upstream denial records failure and does not silently reroute.
