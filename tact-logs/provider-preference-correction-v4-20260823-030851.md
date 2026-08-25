# Provider Preference Correction v4

**Status:** Draft only. No provider activation, inference, configuration change or credential read.
**Supersedes:** The `dip-sig` reference in Provider Preference Patch v3.

## Terminology correction

The operator preference is for **DeepSeek** (the Chinese LLM provider/model family), not `dip-sig` or DeepSig.

Therefore:
- `dip-sig` is removed as a provider/model candidate.
- DeepSeek is added as a mandatory candidate family.
- Any prior `dip-sig=PREMIUM_CANDIDATE_UNRESOLVED` record is superseded and must not be interpreted as DeepSeek availability.

## Mandatory provider families

### Kimi / Moonshot — mandatory
- `kimi-k3`: preferred flagship candidate for Tier B premium reasoning, long-horizon coding and large-context analysis.
- `kimi-k2.6`: preferred Tier A strong/efficient candidate for long-context synthesis, document reduction and agent preparation.
- Exact alias, vendor model ID, version, region and egress posture remain required before proof.

### DeepSeek — mandatory
- DeepSeek reasoning route: preferred Tier B candidate for independent challenging analysis and synthetic reasoning proofs.
- DeepSeek chat/coder route: preferred Tier A candidate for sanitized draft coding, migrations, tests, refactor options and research synthesis.
- Candidate names such as `deepseek-reasoner`, `deepseek-chat`, or versioned DeepSeek IDs are placeholders only until exact gateway aliases and versions are identified.

### Codex — reserved executor/verifier
- Continue to reserve Codex for approved implementation, tests, diff review and precision verification.
- DeepSeek and Kimi draft output never becomes merge-ready without an approved executor/verifier gate.

## Required routing policy

1. Tier A must contain at least one pinned Kimi route and one pinned DeepSeek route before the cheap-cloud rollout is declared complete.
2. Tier B must evaluate both Kimi K3 and an exact pinned DeepSeek reasoning route for complementary premium analysis.
3. Protected, mixed or unknown data remains local-safe; neither Kimi nor DeepSeek is permitted to receive it.
4. Provider/model pinning overrides generic auto-routing for staged proofs.
5. Every fallback repeats F9: allowlist, capability, role, data class, trust tier, quota, egress, evidence and rollback validation.
6. All routes remain non-operational until positive proof, negative proof, rollback proof, immutable evidence and independent approval pass.

## Initial proof order

1. Pin one exact Kimi candidate from the discovered list.
2. Discover and pin one exact DeepSeek gateway alias/model ID.
3. Run isolated Tier A synthetic proof for Kimi.
4. Run isolated Tier A synthetic proof for DeepSeek.
5. Compare evidence; only then nominate premium Tier B proofs.
