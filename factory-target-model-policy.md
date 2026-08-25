# FACTORY TARGET MODEL POLICY

## Strategic goal
The factory must minimize expensive premium-token usage while preserving high engineering quality.

## Primary operating concept
1. Routine factory execution should lean on Codex/plugin-oriented flow where possible.
2. Main code writing must be performed by a strong cloud coding model.
3. Main verification/review must be performed by a stronger review model.
4. A separate Codex opinion must be used as an additional signal.
5. When a quota or rate limit is hit, the stack must automatically switch to a fallback model/provider.

## Required target roles
- Code generation role: strong cloud coding model.
- Verification role: stronger cloud review/reasoning model.
- Independent second opinion: Codex.
- Emergency continuity: fallback chain through FCC.

## Required FCC design
FCC must be configured as the stable gateway layer.
Claude Code-compatible traffic must go through FCC.
Model routing must be customized by task tier, not kept flat.

## Required routing intent
- Default/base model: economical capable coding tier for routine work.
- Sonnet-tier slot: primary code-writing model.
- Fable-tier slot: primary verification/review model.
- Additional Codex lane: independent comparison signal.
- Fallback chain: automatic substitution when limits, downtime, or provider errors occur.

## Factory doctrine
- Cheap routine work first.
- Strong model for final code synthesis.
- Stronger model for review and verification.
- Independent second opinion before risky acceptance.
- Automatic replacement when a limit is exhausted.

## Implementation direction
The exact vendor/model names may change over time.
The invariant is the role architecture:
- writer
- reviewer
- second opinion
- fallback replacement

## Hard rule
The factory must not depend on one single model quota.
If one limit ends, another configured model/provider must take over.

> **Smart Model Routing:** `docs/canon/smart-model-routing-protocol-v1.md` is the governing role, trust-tier, preflight, and independent-review protocol for this document.
