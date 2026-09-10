### Independent Analysis (Fourth Consultant)

---

**Q1: Integration method?**
1. **(c) other (structured rebase + conflict-aware merge)**
2. **Reasoning**:
   - The divergence is non-trivial: `right/engine-research-v2` introduces *normalization* (a systemic change), while `integration/aplusb-20260826` contains *re-implementation* (17e9a68) and *operator-control* (11e43f9) — two distinct logical layers.
   - Cherry-picking (b) risks semantic drift (e.g., normalization may depend on hidden assumptions in `engine-research-v2`). Manual extraction (a) is error-prone due to cross-cutting changes.
   - A **structured rebase** of `integration/aplusb-20260826` onto `right/engine-research-v2` (post-normalization) preserves lineage while allowing granular conflict resolution. This is followed by a **conflict-aware merge** (not a blind merge) to reconcile remaining overlaps.
3. **Risks**:
   - Rebase may expose latent conflicts in operator-control logic (11e43f9) if it interacts with normalization.
   - Requires validation of rebase safety (e.g., no silent data corruption in normalization).

---

**Q2: Resolve Aider vs Codex?**
1. **(c) other (hybrid adjudication with traceability)**
2. **Reasoning**:
   - Precedence (a) is arbitrary; role separation (b) assumes clean boundaries, but A/B re-impl (17e9a68) and operator-control (11e43f9) likely overlap in control flow.
   - **Hybrid adjudication**: Use Codex for *structural* conflicts (e.g., function signatures, type definitions) and Aider for *behavioral* conflicts (e.g., edge-case logic in operator-control). Document resolutions in a **traceability matrix** (e.g., Git notes or a `CONFLICT_RESOLUTION.md` file).
3. **Risks**:
   - Hybrid approach requires clear criteria for "structural" vs. "behavioral" — ambiguity here could lead to inconsistent resolutions.
   - Traceability overhead may slow integration.

---

**Q3: SSOT?**
1. **(c) inline (with canonical tags)**
2. **Reasoning**:
   - A clone repo (a) or local copy (b) risks divergence from the evolving codebase. Inline SSOT (e.g., `// SSOT: engine-research-v2@277c751`) provides **immutable references** while keeping the source of truth *within* the codebase.
   - Use **Git tags** (e.g., `ssot/engine-research-v2`) to mark canonical versions, and **inline comments** to link to specific commits (e.g., `// Canonical: 17e9a68 (A+B re-impl)`).
3. **Risks**:
   - Inline tags may clutter code if overused.
   - Requires discipline to update tags during rebases/merges.

---

**Q4: 17e9a68 superseded?**
1. **(b) partially**
2. **Reasoning**:
   - `17e9a68` (A+B re-impl) is likely a *functional* rewrite, while `right/engine-research-v2` introduces *normalization* (e.g., data format, API contracts). These are orthogonal unless normalization invalidates the re-impl’s assumptions.
   - **Partial supersession**: The *interface* of `17e9a68` may need alignment with normalization, but its *core logic* (e.g., algorithmic improvements) may remain valid.
3. **Risks**:
   - False negatives: Assuming full supersession could discard valuable optimizations in `17e9a68`.
   - False positives: Assuming no supersession could lead to integration bugs if normalization breaks invariants.

---

**Q5: Final?**
1. **(C) merge (with rebase-prep)**
2. **Reasoning**:
   - A merge (C) preserves the full history of both branches, which is critical for auditing (e.g., "why was normalization applied to A+B re-impl?"). However, a **naive merge** would create a messy history.
   - **Rebase-prep**: Rebase `integration/aplusb-20260826` onto `right/engine-research-v2` *first* to linearize changes, then perform a **clean merge** of the rebased branch. This yields a readable history while retaining traceability.
   - Base (A) or integration (B) alone would discard either normalization or re-impl/operator-control, which is unacceptable.
3. **Risks**:
   - Rebase-prep may require significant conflict resolution effort.
   - Merge commit could obscure the rebase-prep work if not documented.

---

### **VERDICT**:
**Structured rebase + conflict-aware merge with hybrid adjudication and inline SSOT.**
- **Integration**: Rebase `integration/aplusb-20260826` onto `right/engine-research-v2`, then merge.
- **Conflict Resolution**: Use Codex for structural conflicts, Aider for behavioral, with traceability.
- **SSOT**: Inline tags + Git tags for canonical versions.
- **17e9a68**: Preserve core logic, align interfaces with normalization.
- **Final State**: Merge commit (C) with rebase-prep history.

**Critical Path**:
1. Validate normalization’s impact on `17e9a68` (A+B re-impl) via differential testing.
2. Rebase `integration/aplusb-20260826` onto `right/engine-research-v2`, resolving conflicts with hybrid adjudication.
3. Merge the rebased branch, tagging the result as `canonical/20260826-integrated`.
4. Document supersession decisions in `CONFLICT_RESOLUTION.md`.
