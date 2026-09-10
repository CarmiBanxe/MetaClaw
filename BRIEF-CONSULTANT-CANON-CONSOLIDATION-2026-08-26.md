# BRIEF TO CONSULTANT: Canon Consolidation Fork

**Date:** 2026-08-26  
**Status:** DRAFT — factual corrections required  
**From:** BEN (Right Terminal, MetaClaw)  
**To:** Operator → Consultant (Codex primary, Fable-5 second opinion)  
**Re:** Final consolidation of diverged rule branches

---

## 1. FACTS (measured live)

### 1.1 Git topology (verified via `git log --oneline --all --graph`)
- **main:** 42746a4 (common ancestor)
- **Branch A:** exp/sandbox-2026-08-05 → 1d896d8
- **Branch B:** right/engine-research-v2 base → 374ebdb
- **Merge in right/engine-research-v2:** 277c751 (A+B unified governance v1.1)
- **Post-merge normalization:** 4096533, 0448d8b, e3ac7ce, 5694a92

### 1.2 integration/aplusb-20260826 topology
- **Origin:** branched from **main@42746a4**, NOT from post-merge
- **Commits:** 17e9a68 (A+B rules re-implementation), 11e43f9 (operator-control)
- **Does NOT contain:** 1d896d8, 374ebdb, 277c751, or normalization commits
- **Relationship:** Parallel line from main, divergent from right/engine-research-v2

### 1.3 Content comparison
| Aspect | right/engine-research-v2 | integration/aplusb-20260826 |
|--------|--------------------------|----------------------------|
| Full A+B merge history | ✅ 277c751 | ❌ Re-implements A+B in 17e9a68 |
| Normalization (FOS/CCOP/AGENTS) | ✅ v1.1 | ❌ Absent |
| Governance/docs file structure | ✅ 53+ files | ❌ Minimal |
| operator-control rule | ❌ Absent | ✅ 11e43f9 |
| latest-operator-comment-wins | ❌ Absent | ✅ 17e9a68 |
| SSOT pointer | ✅ 5694a92 | ❌ Absent |

### 1.4 Missing in right/engine-research-v2
- 11e43f9: "NEVER autonomously send brief to consultant"
- 17e9a68: Detailed A+B conflict resolution with operator directives

### 1.5 SSOT availability
- Declared: `banxe-ai-rnd/research/docs/canon/CANON-FACTORY-SSOT.md`
- Local status: **NOT FOUND** in any checked path
- Current files: POINTERS only — unresolvable references

### 1.6 Execution model conflict (verified in docs)
- `software-factory-canon-v1.md`: "Aider is the sole code executor" (INV-01)
- `smart-model-routing-protocol-v1.md`: Codex as "preferred primary coding executor"
- **Status:** ACTIVE CONFLICT between invariants — not a boundary

---

## 2. OPTIONS (revised with accurate topology)

### Option A: Use right/engine-research-v2 as base, manual extraction

**Approach:**
1. Keep right/engine-research-v2 (21 commits, full history)
2. Manually extract operator-control norm from 11e43f9 (provenance preserved)
3. Analyze 17e9a68 decisions separately (semantic overlap risk)
4. Restore locally-readable SSOT
5. Re-audit before promotion

**Pros:**
- Preserves complete normalization work
- Maintains governance file structure
- Avoids semantic conflicts from 17e9a68 re-implementation
- Controlled, auditable integration

**Cons:**
- Manual work required
- Risk of missing nuances from 17e9a68
- Requires careful provenance tracking

**Safety:** ✅ Highest — no automatic cherry-pick of conflicting commits

---

### Option B: Use integration/aplusb-20260826

**Critical issue:** NOT a fast-forward. Branches have diverged from main@42746a4.

**Content if selected:**
- Latest operator directives (11e43f9, 17e9a68)
- A+B rules as re-implemented in 17e9a68

**What is NOT present:**
- Full A+B merge history (277c751 and ancestors)
- Normalization commits (4096533, 0448d8b, e3ac7ce)
- SSOT pointer migration (5694a92)
- 53+ governance/audit/source files

**Verdict:** ❌ NOT RECOMMENDED — loses substantive normalization work

---

### Option C: Merge both lines

**Risk:** 17e9a68 re-implements A+B rules on different base — significant semantic/text conflicts likely.

**Verdict:** ❌ NOT RECOMMENDED without detailed conflict analysis

---

## 3. REVISED RECOMMENDATION

**Preferred path:** Option A with following sequence:

1. **Extract 11e43f9 operator-control norm manually**
   - Provenance: commit 11e43f9, author CarmiBanxe
   - Content: consultation brief → operator only
   - Integration: new commit on right/engine-research-v2 with attribution

2. **Analyze 17e9a68 separately**
   - Compare with 277c751 normalization
   - Extract unique operator directives not in current branch
   - Discard re-implemented A+B rules (already present in 277c751)

3. **Restore local SSOT**
   - Clone banxe-ai-rnd/research OR
   - Create local CANON-FACTORY-SSOT.md copy OR
   - Inline critical rules pending external resolution

4. **Extended validation (beyond ruff/pytest)**
   - Canon consistency check: verify no conflicting invariants
   - Pointer resolution: all SSOT references verifiable
   - Claude startup-chain: .claude/CLAUDE_CODE_CANON.md readable and complete
   - Three-terminal topology: LEFT/CENTRAL/RIGHT definitions unambiguous

5. **Re-audit by BEN**
   - Verify all operator directives present
   - Verify SSOT locally accessible
   - Verify no active conflicts

6. **Promotion to main**
   - After operator approval
   - With full provenance log

---

## 4. QUESTIONS TO CONSULTANT

1. **Is manual extraction of 11e43f9 preferable to cherry-pick?**
   - Cherry-pisk risks: dependency on 17e9a68 base, potential conflicts
   - Manual extraction: clean application, explicit provenance

2. **How to resolve Aider vs Codex executor conflict?**
   - Current docs: Aider (INV-01) vs Codex (smart-routing)
   - Need explicit precedence rule or role separation

3. **SSOT restoration priority?**
   - Clone external repo
   - Local copy with sync mechanism
   - Inline critical sections

4. **Is 17e9a68 content fully superseded by 277c751+normalization?**
   - Or does it contain unique operator directives requiring preservation?

---

## 5. BOUNDARIES (non-negotiable)

- **NO-AUTONOMOUS-CONSULT:** Brief preparation only — operator dispatches
- **NO-WAIT RULE:** Central never blocks on Terminal A
- **STOP GATE:** State-changing work requires explicit "go"
- **NON-ATOMIC:** Continuous execution until genuine fork
- **EXPLAIN MODE:** Russian user, English code

**Note:** INV-01 (Aider sole executor) vs smart-routing (Codex primary) is an **active conflict**, not a settled boundary.

---

## 6. EVIDENCE AGAINST MY POSITION

**My position:** Option A (right/engine-research-v2 base) is optimal.

**Counter-evidence:**
1. 11e43f9 and 17e9a68 are MORE RECENT than normalization commits — operator may intend these to override
2. "latest-operator-comment-wins" in 17e9a68 explicitly privileges recency
3. By not including these commits, right/engine-research-v2 may be stale
4. Manual extraction risks losing nuances from original commits
5. Operator may have created integration branch precisely to override normalization work

**Implication:** Recency-based interpretation suggests integration branch may represent current intent.

---

## 7. WHAT FACTORY DOES WHILE FORK IS OPEN

**Continuing:**
- Read-only diagnostics
- Audit and coverage tasks
- Documentation drafting
- Test execution

**Blocked:**
- Any rule branch merge
- Promotion to main
- Canon file modifications
- SSOT pointer changes

---

## 8. REVISED ARTIFACT (operator approves Option A)

```bash
# 1. Stay on right/engine-research-v2
# 2. Read 11e43f9, extract operator-control norm
# 3. Create new commit with manual application + provenance
# 4. Analyze 17e9a68 for unique directives
# 5. Restore SSOT locally
# 6. Run extended validation:
#    - canon consistency
#    - pointer resolution
#    - Claude startup-chain
# 7. BEN re-audit
# 8. Operator approval for promotion
```

---

**BEN CERTIFICATION (revised):**
- Facts verified by direct git measurement
- Topology corrected per operator review
- Cherry-pisk warnings added
- Conflict (Aider/Codex) noted as unresolved
- SSOT unavailability acknowledged
- Counter-evidence included

**Status:** DRAFT — ready for operator review before consultant dispatch

---
*End of Revised Brief*
