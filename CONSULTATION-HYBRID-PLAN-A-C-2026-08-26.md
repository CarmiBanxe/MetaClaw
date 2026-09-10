# HYBRID PLAN: Option A + Option C Synthesis

**Date:** 2026-08-26  
**Derived from:** Codex (primary), Fable-5 (second), Mistral (fourth)  
**Basis:** Option A foundation + Option C safeguards

---

## CORE PRINCIPLE

> **Preserve normalization work (Option A)** while **maintaining audit trail of both lineages (Option C)**

---

## PHASE 1: PREPARATION (Read-only, no state change)

### 1.1 Git archaeology
```bash
# Create reference tags before any mutation
git tag -a pre-consolidation-right -m "Reference: right/engine-research-v2 before consolidation"
git tag -a pre-consolidation-integration -m "Reference: integration/aplusb-20260826 before consolidation"

# Export integration branch as patch series for analysis
git format-patch main..integration/aplusb-20260826 \
  -o /tmp/consultation-patches/
```

### 1.2 Content diff analysis
```bash
# Semantic diff: 17e9a68 vs 277c751+normalization
git diff 277c751..17e9a68 -- docs/canon/ > /tmp/semantic-diff-canon.patch

# Extract operator-control only from 11e43f9
git show 11e43f9:CLAUDE_CODE_OPERATING_PRINCIPLE.md | \
  grep -A20 "Operator Control" > /tmp/operator-control-extract.md
```

**Output:** Analysis artifact with:
- [ ] List of unique directives in 17e9a68 (not in normalization)
- [ ] List of operator-control norms in 11e43f9
- [ ] Conflict map: overlapping vs orthogonal content

---

## PHASE 2: BASE SELECTION (Option A core)

### 2.1 Confirm right/engine-research-v2 as base
**Rationale:**
- Contains full normalization (FOS/CCOP/AGENTS v1.1)
- Has 53+ governance files
- SSOT pointer present (5694a92)
- Clean merge history

### 2.2 Create integration workspace
```bash
# Worktree for parallel analysis (no branch switch yet)
git worktree add ../integration-analysis integration/aplusb-20260826
cd ../integration-analysis

# Diff against base
find docs/canon -name "*.md" -exec diff -u \
  ../MetaClaw/{} {} \; > /tmp/integration-diffs.log 2>/dev/null
```

---

## PHASE 3: SELECTIVE EXTRACTION (Hybrid method)

### 3.1 From 11e43f9 (operator-control)

| Element | Action | Target file | Notes |
|---------|--------|-------------|-------|
| "NEVER autonomously send brief" | **Extract** | `CLAUDE_CODE_OPERATING_PRINCIPLE.md` §7.5 | New section |
| "Operator controls delivery" | **Extract** | `FACTORY_OPERATING_SYSTEM.md` §5.2.5 | New section |
| Provenance | **Preserve** | Commit message references | `Source: 11e43f9` |

**Method:** Manual extraction (not cherry-pick) to avoid 17e9a68 dependency

### 3.2 From 17e9a68 (conditional extraction)

**Decision matrix:**

| Content | Exists in 277c751? | Action | Rationale |
|---------|-------------------|--------|-----------|
| A+B rules structure | ✅ Yes | **Discard** | Already normalized |
| `latest-operator-comment-wins` | ❌ No | **Extract** | Unique directive |
| Edge case handling | ⚠️ Partial | **Analyze** | May need adaptation |
| Conflict resolution details | ❌ No | **Extract** | Implementation detail |

**Extraction format:**
```markdown
<!-- Source: 17e9a68 -->
### Directive: latest-operator-comment-wins
**Context:** [brief description]
**Integration:** [how it fits with normalization]
**Verification:** [how to confirm it works]
```

---

## PHASE 4: CONFLICT RESOLUTION (Option C element)

### 4.1 Aider vs Codex resolution

**Hybrid approach:**

```
Factory = exclusive execution layer
├── Structural conflicts (API, types, signatures)
│   └── Codex primary (reasoning-capable)
└── Behavioral conflicts (logic, edge cases)
    └── Aider primary (volume-capable)

Resolution documented in: CONFLICT_RESOLUTION.md
```

### 4.2 SSOT restoration

**Hybrid approach:**

| Priority | Method | Fallback |
|----------|--------|----------|
| 1 | Clone `banxe-ai-rnd/research` to `../research/` | — |
| 2 | Symlink: `docs/canon/CANON-FACTORY-SSOT.md` → `../research/docs/canon/...` | Local copy with sync check |
| 3 | Inline critical sections with `SOURCE: external` markers | — |

**Verification:**
```bash
# Daily sync check
[ -f ../research/docs/canon/CANON-FACTORY-SSOT.md ] && echo "SSOT available" || echo "SSOT missing"
```

---

## PHASE 5: MERGE STRATEGY (Option C safeguard)

### 5.1 Not a blind merge

**Traditional merge (Option C pure):** Would preserve both histories but create semantic conflicts

**Hybrid approach:** Rebase-prep + selective merge

```bash
# Step 1: Create integration branch for analysis
git checkout -b integration-analysis right/engine-research-v2

# Step 2: Apply extracted content as commits (not patches)
# Each extraction = separate commit with provenance

git add CLAUDE_CODE_OPERATING_PRINCIPLE.md
git commit -m "canon(operator-control): NEVER autonomously send brief

Source: integration/aplusb-20260826 11e43f9
Extraction: manual (BEN)
Rationale: operator-only delivery boundary"

# Step 3: Apply 17e9a68 unique directives (if any)
[if unique directives found]
git add docs/canon/
git commit -m "canon(operator-directives): latest-operator-comment-wins

Source: integration/aplusb-20260826 17e9a68
Extraction: manual analysis (BEN)
Diff: 17e9a68 vs 277c751 shows unique directive"
```

### 5.2 History preservation

**Option C element:** Both lineages remain accessible

```bash
# Reference commits (not in main line)
git tag -a lineage-integration-17e9a68 -m "Reference: A+B re-implementation"
git tag -a lineage-integration-11e43f9 -m "Reference: operator-control commit"

# Full history archived
git bundle create consultation-2026-08-26.bundle --all
```

---

## PHASE 6: VALIDATION (Extended per Codex)

### 6.1 Canon consistency check
```bash
# No conflicting invariants
grep -r "sole executor\|primary executor" docs/canon/ | \
  grep -v "CONFLICT_RESOLUTION" > /tmp/executor-refs.log
# Manual review: ensure role separation documented
```

### 6.2 Pointer resolution
```bash
# All SSOT references verifiable
find docs/canon -name "*.md" -exec grep -l "SSOT\|CANON-FACTORY" {} \; | \
  xargs -I {} sh -c 'echo "=== {} ===" && head -5 {}'
```

### 6.3 Startup chain validation
```bash
# .claude/CLAUDE_CODE_CANON.md readable and complete
[ -f .claude/CLAUDE_CODE_CANON.md ] && \
  grep -q "ROOT CANON" .claude/CLAUDE_CODE_CANON.md && \
  echo "Startup chain valid"
```

### 6.4 Topology unambiguous
```bash
# LEFT/CENTRAL/RIGHT definitions consistent
grep -E "^## (Three-Terminal|Terminal)" AGENTS.md CLAUDE.md .claude/CLAUDE_CODE_CANON.md
```

---

## PHASE 7: PROMOTION CHECKLIST

- [ ] All extractions committed with provenance
- [ ] CONFLICT_RESOLUTION.md created
- [ ] SSOT cloned and symlinked
- [ ] Extended validation passed
- [ ] Tags created for reference commits
- [ ] Bundle archived
- [ ] Operator approval obtained
- [ ] PR to main with full history

---

## RISK MITIGATION (Mistral elements)

| Risk | Mitigation |
|------|------------|
| Lost nuances from 17e9a68 | Semantic diff + manual analysis |
| Recency vs normalization conflict | `latest-operator-comment-wins` explicitly extracted |
| Merge history obscured | Reference tags + bundle archive |
| SSOT divergence | Daily sync check + inline fallback |
| Aider/Codex ambiguity | Role matrix in CONFLICT_RESOLUTION.md |

---

## DELIVERABLES

1. `right/engine-research-v2` with extractions (promotion candidate)
2. `CONFLICT_RESOLUTION.md` (audit trail)
3. Reference tags: `lineage-integration-*`
4. Archive: `consultation-2026-08-26.bundle`
5. SSOT: `../research/` clone

---

**BEN CERTIFICATION:**
- Hybrid approach synthesizes 2.5 opinions (Codex primary weighted 2x)
- Option A foundation preserved
- Option C safeguards implemented
- Kimi unavailable, did not block decision

*Ready for operator review*
