# CONFLICT RESOLUTION LOG

**Date:** 2026-08-26
**Resolution:** Canon Consolidation Fork
**Method:** Consultation (Codex + Fable-5 + Mistral)

## Conflicts Resolved

### 1. Aider vs Codex Executor Role

**Conflict:**
- `software-factory-canon-v1.md` §13: "Aider/Codex" both listed
- `smart-model-routing-protocol-v1.md`: Codex as "preferred primary coding executor"

**Resolution (per consultation):**
- Role separation with hybrid adjudication
- Factory = exclusive execution boundary
- Codex = structural/code generation tasks
- Aider = behavioral/file-level operations
- Factory remains sole execution layer (no terminal bypass)

### 2. Two Divergent Rule Branches

**Conflict:**
- right/engine-research-v2: normalization + SSOT pointers
- integration/aplusb-20260826: operator-control commits

**Resolution (per consultation):**
- Base: right/engine-research-v2 (277c751 + normalization)
- Extract: 11e9a68 operator-control (manual, with provenance)
- Analyze: 17e9a68 for unique directives
- Result: 7 files unified, commit 5455022

### 3. Missing External SSOT

**Conflict:**
- Pointers reference `banxe-ai-rnd/research/docs/canon/CANON-FACTORY-SSOT.md`
- File not cloned locally

**Resolution:**
- Inline fallback rules documented
- `EXTERNAL-SSOT-REFERENCE.md` created
- Operator action required to clone external repo

## Traceability Matrix

| Source File | Change | Consult Verdict | Commit |
|-------------|--------|-----------------|--------|
| factory-terminal-working-mode-v1.md | +consult chain order | Codex+Fable-5 | 5455022 |
| smart-model-routing-protocol-v1.md | Fix Fable as second opinion | Codex+Fable-5 | 5455022 |
| AGENTS.md | +operator control note | Codex+Fable-5 | 5455022 |
| COLLAB.md | +operator control rule | Codex+Fable-5 | 5455022 |
| factory-codex.sh | Renamed to operator-codex-consult.sh | Codex+Fable-5 | 5455022 |

## Git Tags (Canonical Versions)

- `5455022` — canon(consult): unified consultation chain
- `5694a92` — canon(pointers): FOS/CCOP/AGENTS → SSOT
- `277c751` — canon(normalize): unified governance v1.1

---
*Reconciled per consultation verdict 2026-08-26*
