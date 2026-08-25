# Provider Preference Patch v3

**Status:** Draft only. No runtime activation, no credential read, no provider call.
**Purpose:** Record operator preference for strongest available routes, with mandatory inclusion of Kimi and premium consideration for dip-sig pending exact route identification.

## Operator preference

- Kimi is mandatory in the approved candidate set.
- dip-sig is preferred for strongest-model consideration, but remains unresolved until exact provider, model ID, version, access path, and trust posture are identified.
- Preference strength does not override data-boundary, approval, or synthetic-proof requirements.

## Preferred routing stance

### Kimi / Moonshot family
- Treat Kimi as a required candidate family in the factory.
- Allow Kimi to appear in Tier A for high-volume long-context and draft synthesis work.
- Allow a stronger Kimi reasoning/code variant to be proposed for Tier B only after exact route pinning and route-specific proof.
- Do not treat generic "Kimi" as sufficient; policy must pin exact model IDs per route.

### dip-sig candidate
- Add dip-sig as a named premium-candidate placeholder.
- Classification: `PREMIUM_CANDIDATE_UNRESOLVED`.
- No activation, no proof run, and no routing assignment until exact route identity is documented.
- If dip-sig cannot be mapped to an approved gateway alias and vendor model/version, it remains policy-only and non-operational.

## Policy consequences

- Tier A must include at least one pinned Kimi route before Tier A cloud rollout is considered complete.
- Tier B candidate list should reserve a slot for dip-sig review once exact identity is confirmed.
- OpenRouter auto-routing must not silently replace explicit operator preference where exact pinned routes are required.
- Explicit provider/model pinning takes precedence over generic auto-routing for approved proofs.

## Non-negotiables unchanged

- Protected or mixed data remains local-safe by default.
- No provider becomes operational without exact route pinning, positive proof, negative proof, rollback proof, immutable evidence, and independent approval.
- No silent cross-tier fallback.
- No BANXE invariant relaxation.
