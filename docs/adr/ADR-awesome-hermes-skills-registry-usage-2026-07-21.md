# ADR: awesome-hermes-skills registry usage in this repository

## 1. CONTEXT

- Confirmed project under review: `ZeroPointRepo/awesome-hermes-skills`, a curated registry for Hermes Agent skills with built-in, optional, and community layers, presented as cross-compatible with Hermes Agent, Claude Code, OpenClaw, Cursor, and Windsurf.
- Hermes Agent documents describe skills as on-demand `SKILL.md` knowledge units, and the platform also supports learning new skills from workflows, which creates a provenance and trust question for any imported skill.
- This repository already uses the same `SKILL.md` convention in `.claude/skills/*/SKILL.md`, so cross-ecosystem portability is plausible at the format level.
- The catalog is therefore strategically useful as a discovery surface, but not inherently trustworthy as a pre-approved factory bundle.
- Naming collision exists: other repositories use the same `awesome-hermes-skills` name, so any extraction work must pin the exact upstream repo and commit, not just the project name.

## 2. PROBLEM STATEMENT

- This factory already maintains a working local skill registry in `.claude/skills/` and has been extending it incrementally through explicit per-skill review.
- A large external skills catalog creates real upside because it may reduce duplicated effort and speed up operator productivity.
- The same catalog also creates real risk because unreviewed or agent-generated skills could introduce file, shell, network, or governance exposure into a compliance-sensitive environment.
- The architectural question is therefore not whether the registry is interesting, but how it may be used without bypassing the repository's existing feature-evaluation discipline.

## 3. OPTIONS

- **A) Ignore the registry** — no use in factory or Banksy workflows.
- **B) Blanket ACCEPT** — mass-install the catalog, or a large slice of it, directly into factory canon and `.claude/skills/`.
- **C) CANDIDATE REGISTRY** — treat the catalog as a scouting index and extract individual skills one at a time through the existing Feature Evaluation Canon.

## 4. ANALYSIS

### A) Ignore

- Factory impact is minimal: no new capability, no new maintenance surface, and no import risk.
- EMI BANXE risk remains low because nothing new is introduced.
- Operator productivity also remains flat because potentially reusable skills are never harvested.
- This option is safe but leaves discovery value unrealized.

### B) Blanket ACCEPT

- Factory impact is high but uncontrolled because a large set of skills would enter `.claude/skills/` without per-skill review.
- EMI BANXE risk becomes unacceptable because community-authored or agent-generated skills of unclear provenance could affect shell, file, network, or data-handling behavior.
- Governance quality degrades because acceptance would happen by bundle proxy rather than by feature-level assessment.
- Short-term operator speed would likely be offset by long-term cleanup, overlap, and audit burden.

### C) CANDIDATE REGISTRY

- Factory impact is controlled and incremental because only selected skills move forward one by one.
- EMI BANXE risk stays bounded because each candidate skill can be screened for provenance, execution scope, data handling, and overlap before adoption.
- Operator productivity improves sustainably because the registry is used for discovery without importing its full risk surface.
- This option aligns with the repository's existing pattern of review, placement, and audit-trail documentation.

## 5. DECISION

Adopt **Option C: CANDIDATE REGISTRY**.

This is the only option consistent with the repository's current canon. A public multi-skill catalog is not a single accepted feature; it is a source of many candidate features. Treating the bundle itself as accepted would bypass Step 1 and Step 2 discipline for each individual skill. Ignoring the registry entirely would preserve safety, but Option C already preserves that safety while retaining discovery value. The registry is therefore approved only as a discovery source, not as a canonized bundle.

## 6. CONSEQUENCES

### Allowed

- Use `ZeroPointRepo/awesome-hermes-skills` as a scouting index for candidate skills.
- Read and inspect individual `SKILL.md` files to identify useful capabilities.
- Create separate `docs/audit/FEATURE-EVALUATION-<SKILL-NAME>-<date>.md` files for individual candidates.
- Install or adapt a skill only after its own evaluation, placement, and acceptance decision.
- Use sandbox experimentation where appropriate before any canon-level adoption.

### Forbidden

- Mass-install the catalog, or any large unreviewed subset, into `.claude/skills/` or factory workflows.
- Treat catalog presence as implicit approval for EMI BANXE, customer data, or production credential access.
- Skip per-skill Step 1 assessment on the theory that the registry itself has already been reviewed.
- Collapse provenance review for community or agent-generated skills into a single blanket decision.

## 7. NEXT STEPS

1. Select 1–2 concrete skills from the registry and create dedicated feature-evaluation files for each candidate.
2. For any skill that reaches ACCEPT, wire it into the appropriate destination only after explicit placement is decided, for example factory `.claude/skills/` versus operator sandbox.
3. Add a standing provenance check to each future evaluation so reviewers record whether a candidate skill appears human-authored, community-maintained, or agent-generated.
4. Require pinned upstream references for every extraction, including exact repository and commit, to avoid ambiguity from same-name repositories.
