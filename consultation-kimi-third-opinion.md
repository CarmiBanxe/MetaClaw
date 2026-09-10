I'll analyze this independently, without anchoring to previous responses.

## 1. Answers

**Q1: (b) cherry-pick**

**Q2: (b) role separation**

**Q3: (a) clone repo**

**Q4: (b) partially**

**Q5: (C) merge**

---

## 2. Reasoning

### Q1: Cherry-pick
The branch structure shows discrete, well-scoped commits on `integration/aplusb-20260826`:
- `17e9a68`: A+B re-implementation
- `11e43f9`: operator-control

These are atomic features that can be cherry-picked onto `right/engine-research-v2` (which already has merge + normalization). Manual extraction risks human error; cherry-pick preserves commit metadata and authorship.

### Q2: Role Separation
"Aider vs Codex" suggests two AI coding assistants with potentially conflicting outputs. Precedence creates winner-take-all fragility. Role separation assigns distinct domains (e.g., Aider for scaffolding/architecture, Codex for implementation details), allowing both to contribute without collision.

### Q3: Clone Repo
SSOT (Single Source of Truth) restoration via clone ensures:
- Clean provenance from `main@42746a4`
- No local working directory pollution
- Reproducible starting state for integration

Local copies risk drift; inline restoration is opaque.

### Q4: Partially Superseded
`17e9a68` (A+B re-impl) likely contains algorithmic improvements or bugfixes that `right/engine-research-v2` lacks, but may use deprecated interfaces. The "re-impl" suggests intentional redesign worth preserving. `11e43f9` (operator-control) appears additive and non-conflicting.

### Q5: Merge
Neither base is clean:
- `right/engine-research-v2` has normalization infrastructure
- `integration/aplusb-20260826` has domain logic advances

A proper merge preserves both lineages, enables bisectability, and maintains history. Rebasing `integration` onto `right/engine` then fast-forwarding is operationally equivalent to merge with cleaner graph.

---

## 3. Risks

| Risk | Mitigation |
|------|-----------|
| Cherry-pick conflicts on `17e9a68` | Use `git cherry-pick -x` to track origin; resolve with normalization layer from `right/engine` |
| Role separation ambiguity | Document boundaries in `CONTRIBUTING.md` or `.cursorrules` |
| Clone time/space cost | Shallow clone: `git clone --depth=10` |
| Merge regression | Run A+B test suite before finalizing |
| "Normalization" in `right/engine` may have changed A+B semantics | Diff `17e9a68` against `main@42746a4` to isolate pure re-impl changes |

---

## VERDICT

**Execute: Cherry-pick `11e43f9` onto `right/engine-research-v2`; evaluate `17e9a68` for partial cherry-pick or manual port; establish Aider/Codex role separation; clone fresh SSOT; merge result to `main`.**

This preserves the normalization work in `right/engine`, incorporates operator-control cleanly, selectively retains valid A+B re-implementation logic, and maintains full git history for auditability.
