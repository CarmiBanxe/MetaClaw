# Cloud Provider Priority Policy Draft

**Status:** Draft only. No runtime activation, no provider enablement, no Guardian change.
**Purpose:** Reduce token and quota pressure on Codex / Claude Code by shifting eligible non-sensitive work to cheap or free cloud-capable routes, while preserving premium routes for material work and keeping local models minimal and effective.

## Operating assumption

Local models on the first and second machine are unstable and must not be treated as the default reasoning or coding path. Local-safe routes remain for protected workloads, continuity, and narrow fallback use only.

## Provider-priority tiers

### Tier A — Cheap cloud / bulk-work tier
Use for high-volume, non-sensitive work that would otherwise waste premium reasoning or Codex execution budget.

**Preferred provider/model classes**
- Kimi / Moonshot-class long-context models
- DeepSeek chat / coder-class models
- OpenRouter low-cost and mid-cost allowlisted models
- Gemini Flash-class or equivalent efficient long-context models
- NVIDIA NIM-hosted efficient models, where allowlisted

**Primary uses**
- Long-document reading and summarization
- Research synthesis
- Task decomposition
- Draft ADR options
- Draft migration plans
- Draft test cases
- Draft API mappings
- Bulk code scaffolding proposals
- Refactor option generation
- Synthetic fixture generation
- Sanitized debugging notes

**Do not use as sole final authority for**
- Material architecture decisions
- Final policy wording
- Production-affecting approvals
- Protected-data tasks

### Tier B — Premium cloud / material-decision tier
Use when quality, depth, and decision confidence matter more than token thrift.

**Preferred provider/model classes**
- Opus-class reasoning routes
- Fable 5 or equivalent frontier reasoning route
- Other explicitly approved top-tier reasoning/coding models through FCC/OpenRouter-compatible allowlisted paths
- Codex for implementation execution and precise code-change work

**Primary uses**
- ADR finalization
- Threat modeling
- Gateway/security changes
- Payment, ledger, reconciliation, ISO 20022, KYC/KYB/AML design
- Cross-service contracts
- Difficult trade-off analysis
- Final code patches
- Implementation verification
- Independent material second opinion, where designated

### Tier C — Local-safe minimum tier
Use only when the task is protected, continuity-critical, offline, or explicitly local-safe.

**Permitted uses**
- Protected data handling
- Local continuity fallback
- Advisory-only local review
- Narrow service roles such as embeddings and utility inference where locally stable
- Emergency fallback when cloud route is unavailable and task class permits local-safe handling

**Not the default for**
- General project design
- Bulk reasoning
- Primary code generation
- Large-context synthesis

## Task-class routing shift

The following task classes should move away from Codex / Claude Code premium usage and into Tier A when data is non-sensitive:

- Read large documents
- Summarize research
- Compare open-source repos
- Produce initial ADR alternatives
- Generate rough task trees
- Create draft migrations
- Create draft tests
- Prepare sanitized debugging hypotheses
- Generate fixture data
- Produce initial contract/interface sketches

The following task classes should remain on Tier B:

- Final implementation patches
- Material design decisions
- Security-sensitive design
- Gateway / routing / policy changes
- Ledger / payments / AML / KYC architecture
- Final reconciliation and approval artifacts

## Premium budget preservation rules

1. Do not spend Codex or premium-reasoning tokens on bulk reading, first-pass summaries, or low-risk ideation when Tier A can do the work.
2. Use Codex primarily for code execution, patches, tests, and precision verification.
3. Use premium frontier reasoning only where the task is material, ambiguous, or risk-bearing.
4. Require independent review for material decisions.
5. Never reroute protected data to cloud merely to save local instability or premium cost.

## Local-minimization rules

1. Treat local model output as advisory unless the task is explicitly local-safe.
2. Keep local models warm-path minimal: protected-data work, continuity fallback, embeddings, and narrow infra roles.
3. Do not promote local coder models to the strategic default merely because they are already installed.
4. If a local model repeatedly fails readiness or warm-up expectations, keep it outside the primary factory path.

## Activation prerequisites before any provider is treated as “in use”

A provider/model route is not considered operational merely because it is named in policy. It becomes operational only after:
- allowlist entry exists;
- credentials are isolated and injected safely;
- route is reachable through approved gateway;
- synthetic task proof passes for its assigned tier;
- evidence is recorded;
- reroute and rollback behavior are tested where applicable.

## Initial synthetic proof targets

### Tier A proof targets
- Kimi/Moonshot route: long-context summary on sanitized corpus
- DeepSeek route: draft migration + draft tests on synthetic repository slice
- OpenRouter cheap route: research synthesis + task decomposition
- Optional Gemini Flash/NIM route: bulk document reduction

### Tier B proof targets
- Premium reasoning route: ADR/trade-off review on synthetic banking architecture case
- Codex: patch + test + verification cycle
- Independent second-opinion route: reconciliation against primary analysis

### Tier C proof targets
- LiteLLM local-safe route: protected synthetic task
- Local continuity fallback: offline-safe advisory run
- Embedding/utility role: local utility invocation

## BANXE non-regression note

This draft does not reduce banking invariants. Any activation must preserve:
- double-entry correctness
- CQRS/event sourcing boundaries
- ISO 20022/payment adapter boundary
- KYC/KYB/AML orchestration
- named MLRO independence where required

## Immediate next step

Create a staged capability matrix from this draft, mapping each provider/model route to:
- tier
- allowed task classes
- forbidden task classes
- trust tier
- synthetic proof task
- evidence requirement
- fallback behavior
