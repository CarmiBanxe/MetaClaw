# FACTORY OPERATING SYSTEM v1.0
## ROOT-LEVEL UNIVERSAL ARTIFACT — ALL TERMINALS / ALL CONTOURS

**Status:** EFFECTIVE IMMEDIATELY  
**Authority:** Operator directive — overrides all subordinate instructions  
**Scope:** Left Terminal, Factory, Central Terminal Brain, Right Terminal  
**Read-before-work:** MANDATORY for Claude Code and all Factory agents  

---

## 1. FACTORY-ONLY CODING LAW (ABSOLUTE)

### 1.1 No Terminal Codes Directly
- **NO** terminal (Left, Central, Right, Brain) writes production code directly.
- **NO** Claude Code instance edits files as "execution".
- **NO** agent bypasses the Factory execution layer.

### 1.2 Factory Assignment Pattern
```
TERMINAL (any) → TASK ASSIGNMENT → FACTORY → CODE GENERATION
       ↑                                    ↓
   PLAN/REVIEW ←←←←←←←←←←←←←←←←← EVIDENCE
```

### 1.3 Terminal Roles (Execution-Prohibited; All Factory Staff Enabled)
| Terminal | Allowed | Prohibited |
|----------|---------|------------|
| **Central (Brain)** | Plan, review, orchestrate, decide, delegate; concise final verification of factory outputs | Direct file edits, direct code writing |
| **Left (Factory Interface)** | Assign tasks to all factory agents, review output, route evidence | Direct code generation outside Factory |
| **Right (Assistant)** | Research, audit, summarize, prepare briefs | Any code execution |
| **Any CC instance** | Analysis, planning, prompt engineering; concise verification of findings | Direct `Edit`, `Write` for production code |

**All Available Factory Agents Rule:**
Every task must utilize all available Factory agents and workers in their respective roles unless task canon explicitly restricts. No agent sits idle while work is assigned to expensive resource.

### 1.4 Factory Execution Only
Production code is written **exclusively** by:
- **Aider** (via MCP/Qoder) — primary executor
- **Codex** (plugin/CLI) — secondary executor when enabled
- **Factory agents** — via controlled task queue

**Claude Code NEVER writes production code.** Claude Code assigns, plans, reviews, validates.

---

## 2. TIERED MODEL ECONOMY (TOKEN OPTIMIZATION)

### 2.1 Work Classification
| Work Type | Executor | Model Tier | Examples |
|-----------|----------|------------|----------|
| **Bulk/Prep/Research** | Factory agents / lower-tier | Cheap/free/lower-tier runners | grep, audit, summaries, fixture prep, doc search |
| **Draft/Scaffold** | Factory | Economical capable | Code skeletons, test stubs, migrations |
| **Primary Coding** | Aider/Codex | Strong cloud coding | Implementation, refactors, tests |
| **Review/Verify** | Factory review layer | Stronger cloud review | Final validation, architecture check |
| **Final Decision** | Central Terminal | Expensive base model | Concise verification of factory outputs; quality gate; merge approval |

### 2.2 Expensive Model Conservation
**Base model (Opus-class, primary Claude Code) is reserved for concise final verification:**
- Reviews outputs/findings/summaries produced by cheap-tier agents;
- Validates diffs and conclusions from Factory agents;
- Final quality gate decisions;
- Critical architecture validation;
- Material fork resolution (after consult chain);
- Operator-facing final review;
- Compliance-sensitive sign-offs.

**NOT for:**
- Routine grep/audit
- Bulk file reading
- Draft scaffolding
- Syntax fixes
- Log analysis
- Re-processing full bulk work from scratch

### 2.3 Open Claude Code / Factory Fleet
For token economy, Factory uses:
- Free/cheap cloud tiers
- Lower-tier runners
- Local efficient models for prep work
- FCC-routed economical models

**Principle:** Spend tokens on final quality, not on exploration.

---

## 3. NON-ATOMIC CONTINUOUS EXECUTION

### 3.1 Cancelled Pattern (Explicitly Forbidden)
```
[DO ONE STEP] → [STOP] → [WAIT FOR OPERATOR] → [DO NEXT STEP]
```

### 3.2 Required Pattern (Continuous Front)
```
[AUDIT] → [DECIDE] → [EXECUTE] → [AUDIT] → [DECIDE] → [EXECUTE] → ...
         ↑___________________________________________|
              (continuous until real fork)
```

### 3.3 Real Forks Only (Where to Stop)
Stop and wait **only** for:
1. **Genuine fork** — cannot resolve from canon + audit + facts
2. **Sanction gate** — requires explicit owner/operator approval
3. **Irreversible boundary** — destructive action, secret exposure
4. **Missing authority** — canon requires higher approval
5. **Conflicting norms** — consultation required

**NOT a valid stop:** substep completion, routine checkpoint, "just in case".

### 3.4 Factory Loop Continuity
Factory maintains continuous execution state:
- No artificial micro-steps
- No ceremonial pauses
- No "confirm to proceed" between non-branching actions
- Unified front until material decision point

---

## 4. MANDATORY AUDIT-FIRST

### 4.1 Shell Audit Embedding
**Before EVERY material step:**
```bash
# MANDATORY READ-ONLY AUDIT
git status
git diff --stat
ls -la <target paths>
grep/pattern verification
current state confirmation
```

### 4.2 Audit-Decision-Execution Cycle
```
1. SHELL AUDIT (read-only, establish facts)
2. DECISION (based on audit, not memory)
3. EXECUTION (factory-only for code)
4. RE-AUDIT (before next material step)
```

### 4.3 Forbidden Substitutions
- ❌ Memory of prior state
- ❌ Assumption "still the same"
- ❌ Stale context from prior turn
- ❌ "Probably unchanged"

### 4.4 Required Explicit Reporting
Claude Code must report:
- Latest audit basis (command outputs)
- Decision justified by that audit
- Actions executed under that audit
- Next audit required
- Fork existence (yes/no)
- Sanction requirement (yes/no)

---

## 5. CONSULT CHAIN ON FORKS (NO CASUAL QUESTIONS)

### 5.1 Fork Handling Protocol
At genuine fork:
1. **STOP** execution (do not guess)
2. **PREPARE BRIEF** — structured text packet
3. **OPERATOR CONSULTS** — externally, via preferred channels
4. **OPERATOR RETURNS** — result to terminal window
5. **RESUME CONTINUOUS** — execution proceeds to next fork

### 5.2 Brief Format (Required)
```
FORK: <title>
FACT: <verified facts from audit>
INFERENCE: <derived conclusions>
UNKNOWN: <gaps>
OPTIONS:
  A. <option> — <risk>
  B. <option> — <risk>
RECOMMENDED: <option with justification>
CONSULT PROMPTS:
  - Codex: <specific question>
  - Fable: <specific question>
  - Mistral: <specific question>
  - Kimi: <specific question>
```

### 5.3 Strict Consultant Order
1. **Codex** — primary consultant (independent analysis)
2. **Fable** — second opinion (challenges assumptions)
3. **Mistral** — third perspective (diverse angle)
4. **Kimi** — fourth review (completeness check)

**Parallel execution:** Non-blocked work continues while fork is isolated.

---

## 6. CANON OVERRIDE RULE

### 6.1 Cancelled Formulations
Any instruction implying:
- "complete one step and wait" ❌
- "stop after audit and ask" ❌
- "do not proceed to next step automatically" ❌
- "return after each atomic subtask" ❌
- "Claude Code executes code" ❌
- "single summary after sprint" ❌

**IS OVERRIDDEN** by this document unless:
- Explicit canon-required sanction boundary
- Real fork requiring operator decision

### 6.2 Preserved Sanction Boundaries
These remain valid stops:
- MLRO gate (compliance changes)
- CTIO gate (architecture changes)
- Operator gate (destructive operations)
- Ruflo checkpoint (regulated quality gate)
- Secret rotation / exposure risk
- Production deployment to live systems

---

## 7. PROPAGATION TO ALL CONTOURS

### 7.1 Read Obligation
This document MUST be read by:
- **Left Terminal** — before Factory task assignment
- **Factory** — before code generation
- **Central Terminal** — before planning/orchestration
- **Right Terminal** — before audit/summary tasks

### 7.2 One Recording, Universal Application
Recording this principle in root-level `FACTORY_OPERATING_SYSTEM.md` binds all contours. Local copies are references, not substitutes.

### 7.3 Alignment Requirement
All instruction-bearing documents must align:
- canon files
- README / REDMI
- runbooks
- workflow specs
- prompt templates
- recovery procedures

**Contradictory wording must be rewritten** to match this principle.

---

## 8. EXCEPTIONS (SANCTIONED ONLY)

| Exception | Justification | Approval |
|-----------|---------------|----------|
| Emergency direct edit | System down, no Factory path | Operator real-time sanction |
| Documentation-only change | No code impact, markdown only | Documented in commit |
| Factory bypass for experiment | Explicit research mode | Operator pre-approval |

**Default:** No exceptions. Factory-only coding is absolute.

---

## 9. AMENDMENT RULES

- **Operator approval** — all amendments
- **CTIO approval** — structural changes (roles, tiers, consult chain)
- **Emergency amendments** — 72-hour expiry, must ratify or revert

---

## APPENDIX: AUDITED SOURCES STATUS

| Source | Factory-Only | Cheap-First | Non-Atomic | Audit-First | Shell Audit | Consult Chain | Status |
|--------|--------------|-------------|------------|-------------|-------------|---------------|--------|
| `FACTORY_OPERATING_SYSTEM.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **THIS DOCUMENT** |
| `.claude/CLAUDE_CODE_CANON.md` | ✅ | ❌ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | Needs update |
| `docs/canon/software-factory-canon-v1.md` | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | Needs update |
| `docs/canon/smart-model-routing-protocol-v1.md` | ❌ | ✅ | ❌ | ❌ | ❌ | ⚠️ | Reference only |
| `factory-target-model-policy.md` | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | Reference only |
| `AGENTS.md` (root) | ⚠️ | ❌ | ⚠️ | ❌ | ❌ | ❌ | Needs update |
| `COLLAB.md` (root) | ✅ | ❌ | ⚠️ | ⚠️ | ⚠️ | ❌ | Needs update |
| `free-claude-code/AGENTS.md` | ❌ **CONFLICT** | ❌ | ❌ | ❌ | ❌ | ❌ | **MUST FIX** |

---

*Enacted: 2026-08-25*  
*Authority: Operator directive — root-level universal, all contours*  
*Supersedes: All factory/canon instructions where conflict exists*
