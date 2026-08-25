# Feature Evaluation — hermes-agent-skill-authoring (2026-07-21)

## Feature under review

- Source repository: ZeroPointRepo/awesome-hermes-skills (Hermes Agent skills catalog).
- Approximate path: skills/software-development/hermes-agent-skill-authoring/SKILL.md (inferred from Hermes skills documentation; exact path must be confirmed against the GitHub tree before any ACCEPT).
- Nature: meta-skill for authoring and validating SKILL.md files — frontmatter structure, basic validation, and writing-quality guidance for skills.
- Claimed scope: documentation and authoring assistance for skills, not direct execution of shell/network operations beyond handling skill-definition text.

## Factory value

- Strategic value: MEDIUM–HIGH. This repository already maintains `.claude/skills/*/SKILL.md` and has been expanding that registry manually; a dedicated authoring/validation skill addresses a real gap in how skills are specified and checked.
- Overlap/synergy: high synergy with existing skills (spec-writing, github-navigation, testing, apple-design) and low duplication risk, since none of the current skills focus on SKILL.md authoring or validation itself.
- Expected impact: improves consistency and quality of new skills, reduces ad hoc variation in SKILL.md structure, and supports future migration or portability between Claude Code and Hermes Agent environments.

## Banksy / EMI BANXE risk

- Data-handling: operates primarily on skill-definition text; not intended for direct use on EMI BANXE customer, KYC, or transaction data.
- Execution behavior: described behavior is limited to reading and writing SKILL.md-shaped documents; no network calls or privileged shell operations are implied in the available descriptions, but this must be confirmed from the actual SKILL.md content and associated code, if any.
- Provenance: unclear whether the skill is human-authored, community-authored, or agent-generated via Hermes’s self-improvement loop; provenance must be checked via upstream commit history before any ACCEPT or production use.
- Net risk: LOW for factory documentation workflows, conditional on provenance and behavior review; any extension beyond authoring/validation would require a separate evaluation.

## Initial placement

- Placement: CANDIDATE REGISTRY.
- Rationale: the skill is well aligned with this repository’s existing practice of building a local skills registry and has a low apparent risk surface, but unresolved provenance and unconfirmed exact path mean it cannot move beyond candidate status yet.
- Not allowed: implicit ACCEPT or direct installation into production workflows without a confirmed path, provenance review, and behavior inspection.

## Next steps

1. Confirm the exact upstream path in `ZeroPointRepo/awesome-hermes-skills` and fetch the real `SKILL.md` content for hermes-agent-skill-authoring into a local sandbox for review.
2. Inspect the skill’s commit history and authorship to resolve the provenance question (human-authored vs agent-generated vs community-maintained) and record that outcome in a follow-up note or ADR.
3. Verify that the skill’s behavior is limited to SKILL.md authoring and validation and does not introduce unintended shell, file, or network side effects.
4. If the above checks are satisfactory, propose a placement decision (e.g., sandbox-only or factory `.claude/skills/hermes-agent-skill-authoring`) in a follow-up feature evaluation update.
5. Extend the repository’s canon with a general provenance rule for agent-generated skills from self-improving agents (such as Hermes) and apply that rule consistently to this and future skills.


## Placement update — 2026-07-21 (operator sandbox-only)

- Placement updated: operator sandbox-only — hermes-agent-skill-authoring is promoted from bare CANDIDATE REGISTRY to active operator sandbox, but NOT to factory `.claude/skills/` yet.
- Preconditions for any future promotion to factory registry:
  - exact upstream path and commit in `ZeroPointRepo/awesome-hermes-skills` confirmed against the real Git tree;
  - provenance resolved via commit history/authorship inspection (human-authored vs community vs agent-generated);
  - behavior verified as limited to SKILL.md text operations, with no unexpected shell/network/file side effects;
  - at least one sandbox test run against synthetic/dummy SKILL.md content with no incidents.
- Scope of this note: applies only to hermes-agent-skill-authoring; awesome-hermes-skills as a catalog remains a CANDIDATE REGISTRY under its own ADR.
- Guardrail: no EMI BANXE or real customer data may be used in any sandbox test of this skill.
- This placement update does not constitute ACCEPT for production or factory `.claude/skills/` use; that requires a separate, explicit decision once all preconditions are met.

