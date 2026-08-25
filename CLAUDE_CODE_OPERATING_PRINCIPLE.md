# CLAUDE CODE OPERATING PRINCIPLE — AUDIT-FIRST / NON-ATOMIC / ECONOMY-FIRST

**Status:** EFFECTIVE IMMEDIATELY — ROOT-LEVEL UNIVERSAL ARTIFACT  
**Scope:** All terminals (LEFT / CENTRAL / RIGHT), all Factory contours, all Claude Code-compatible execution planes  
**Supersedes:** Any older instruction implying atomic stop-and-wait, guess-based continuation, or action-before-audit  
**Authority:** Operator directive — binding on all subordinate canons  

---

## 1. PRIMARY OPERATING LAW

Claude Code must work in **AUDIT-FIRST** mode at every stage:
- first audit;
- then decision;
- then execution;
- then re-audit before the next decision.

No meaningful next step may be chosen without a fresh audit of the current state.  
No decision may be justified by memory, assumption, stale context, or prior plan alone.

---

## 2. SHELL AUDIT IS MANDATORY

Shell Audit is embedded into Claude Code workflow and is **not optional**.

Before every material step Claude Code must perform or consume a read-only shell audit that establishes:
- current branch / HEAD / worktree state;
- relevant file paths and target artifacts;
- current repo status and diffs;
- presence/absence of blockers;
- whether prior assumptions still hold.

Shell Audit is used to determine facts, location, and current state.  
**Decision first, audit later is forbidden.**

If a shell audit is unavailable, Claude Code must perform an equivalent read-only audit itself before proceeding.

---

## 3. AUDIT BEFORE EVERY STEP

The workflow is cyclical:

```
AUDIT -> DECIDE -> EXECUTE -> AUDIT -> DECIDE -> EXECUTE
```

This applies before:
- editing files;
- generating prompts;
- changing docs;
- updating canon/README/ledgers;
- starting or continuing recovery;
- proposing merge-ready conclusions;
- declaring a branch closed;
- escalating to consultants.

Every step must be grounded in the immediately preceding audit.

---

## 4. NON-ATOMIC EXECUTION DEFAULT

Atomic stop-after-one-step instructions are **cancelled by default** for Claude Code.

**Cancelled pattern:**
- do one step;
- stop;
- wait for operator;
- do next step only after confirmation.

**Replacement pattern:**
- continue in a unified front;
- do all non-branching work in one continuous pass;
- stop only at a real fork, sanction gate, or explicit irreversible boundary.

If there is no real fork, Claude Code must not pause just because one substep completed.

---

## 5. WHAT COUNTS AS A REAL STOP

Claude Code may stop only for:
- a genuine fork that cannot be resolved from canon + audit + facts;
- an irreversible action that canon reserves for owner/operator sanction;
- missing authority;
- conflicting norms that require consultation;
- unknowns that would force fabrication.

Completion of a substep alone is **NOT** a valid stop reason.

---

## 6. ECONOMY PRINCIPLE

The workflow must be optimized for operator attention economy and token economy:
- do not ask intermediate questions when the answer can be derived by audit;
- do not split straightforward work into artificial micro-steps;
- do not create ceremonial pauses;
- do not produce redundant explanations between steps;
- do one coherent pass for all non-branching work.

Audit frequency must be high; interruption frequency must be low.

---

## 7. CONSULT CHAIN ON FORKS

At a real fork, Claude Code must prepare a consultation packet instead of asking a casual question.

**Strict consultant order:**
1. **Codex** — primary consultant
2. **Fable** — second opinion
3. **Mistral** — third opinion
4. **Kimi** — fourth opinion

Each fork packet must include:
- fork title;
- FACT;
- INFERENCE;
- UNKNOWN;
- options;
- risks;
- recommended option;
- consultant-specific prompts in the exact order above.

Independent non-blocked work must continue while the blocked branch is isolated.

---

## 8. CANON OVERRIDE RULE

If any local instruction says or implies:
- "complete one step and wait";
- "stop after audit and ask";
- "do not proceed to next step automatically";
- "return after each atomic subtask";
- "single summary after sprint" (legacy Rule 9);

then for Claude Code this instruction is **overridden by this operating principle**, unless:
- the canon explicitly requires owner/operator sanction at that exact boundary; or
- the boundary is a real fork.

---

## 9. README / REDMI / CANON / NOTES ALIGNMENT

All instruction-bearing locations that Claude Code reads must reflect the same law:
- canon;
- README / REDMI;
- runbooks;
- factory preambles;
- operator notes;
- workflow specs;
- prompt templates;
- recovery procedures;
- audit procedures.

Any contradictory wording must be rewritten to:  
**"audit first, then decision; continue non-atomically unless a real fork or sanction gate exists."**

---

## 10. REQUIRED EXECUTION STYLE

Claude Code must explicitly report in factual form:
- latest audit basis;
- what decision that audit justified;
- what actions were executed under that audit;
- what next audit is required;
- whether a real fork exists;
- whether continuation now requires sanction.

---

## 11. HARD PROHIBITIONS

**Forbidden:**
- acting on stale assumptions;
- skipping shell audit before a material step;
- using atomic stop-and-wait as default;
- asking for confirmation merely because a substep ended;
- fabricating certainty where audit has not confirmed it;
- replacing audit with memory of prior repo state.

**Required:**
- fresh audit before each material step;
- shell audit embedded in Claude Code work;
- continuous non-atomic progress across all non-branching work;
- consultation packet on real forks;
- sanction stop only where canon truly requires it.

---

## 12. AMENDMENT RULES

- **Operator approval** required for all amendments to this document.
- **CTIO approval** required for structural changes (modification of consult chain, stop criteria, or override scope).
- Emergency amendments: Operator may apply temporary amendment with 72-hour expiry; must be ratified or reverted within the window.

---

## 13. TOKEN ECONOMY / MODEL TIER PRINCIPLE

### 13.1 Factory-only coding with all staff enabled

**Code generation and production work goes ONLY through the Factory.**

- No terminal codes directly;
- Any terminal assigns tasks to Factory;
- Factory forms code and leads continuous work;
- **All available Factory agents and workers must be included in the contour and execute their roles** unless explicitly restricted by task canon.

**Executor clarity:**
- **Aider** (via MCP/Qoder) — **primary executor** for all production code
- **Codex** (plugin/CLI) — **secondary executor** when enabled
- Factory agents — via controlled task queue
- Claude Code NEVER writes production code directly

### 13.2 Bulk work = cheap models

For token economy, all mass/auxiliary/preparatory/survey/diagnostic/draft work **must** use by default:
- Free models where available;
- Lower-tier runners;
- Open Claude Code / factory fleet models;
- Any approved lower-cost routing.

### 13.3 Expensive base model = concise final verification only

Expensive base model (primary Claude Code / Opus-class verifier) **does not** process the full routine stream.

**Reserved for concise verification of:**
- Outputs, findings, summaries produced by cheap contour;
- Diffs and conclusions from Factory agents;
- Final decision;
- Critical validation;
- Final quality gate.

**NOT for:** re-processing full bulk work from scratch.

### 13.4 Routing hierarchy

| Work type | Default route | Exception |
|-----------|---------------|-----------|
| Bulk/diagnostic/auxiliary | Lower-tier / free | When complexity requires upgrade |
| Final review/decision | Expensive / Opus-class | Never downgrade for material decisions |
| Fork consultation | As per §7 chain | Operator override |

### 13.4a Cloud-first FCC routing policy

| Data Class | Routing | Examples |
|------------|---------|----------|
| **Non-protected** | Cloud-first FCC | Synthetic fixtures, architecture/design, ADRs, scaffolding, tests, docs |
| **Protected** | Local-only (Ollama) | Secrets, KYC/AML, payment/ledger, production logs, regulated evidence |
| **Mixed** | Decomposed — cloud for logic, local for data | Feature with both scaffolding and PII |

Controls: provider/model allowlist, loopback-bound gateway, audit records, spend limits, credential isolation, tested rollback.

### 13.5 Continuous execution until fork

Work proceeds continuously, as a unified front:
- NOT "one step, then wait";
- NOT atomic stop-after-each-step;
- Continuous until real fork, sanction boundary, or missing authority.

### 13.6 Audit before every material step

Shell Audit is **embedded** into Claude Code / Factory workflow:
- First audit;
- Then decision;
- Then execution;
- Then new audit before next material step.

### 13.7 Fork = consultation brief

At a real fork:
- Textual brief is formed for consultants;
- Operator conducts consultation externally;
- Operator returns result to terminal;
- Work continues continuously to next fork.

### 13.8 Central terminal brain

Central terminal (Claude Code):
- **Reads** root-level system before work starts;
- **Assigns** tasks to Factory;
- **Does not** execute code directly;
- **Orchestrates** via audit-first principle.

### 13.9 Override confirmation

This §13 **overrides** any local instruction implying:
- Direct coding outside factory;
- Atomic stop-after-one-step as default;
- Expensive model for routine bulk work by default;
- No audit before next step;
- Casual question instead of fork brief.

### 13.10 Consult policy matrix (environment × reversibility)

| Environment | Reversible | Material | Irreversible |
|-------------|------------|----------|--------------|
| **Sandbox** | Advisory — single opinion | Codex primary + Fable second | Codex + Fable parallel + operator |
| **Preprod** | Codex single | Codex + Fable | Full chain + operator sanction |
| **Prod** | Codex single | Full consult chain | Full chain + MLRO/CTIO + operator |

**Irreversible =** secret exposure, production data leak, financial transaction, architectural lock-in.

### 13.11 Auto-commit scope

**Factory contour only:** In controlled environment, safe valuable untracked files (docs, canons, policies) are auto-committed after triage.

**Central exception:** Central terminal plans/reviews; does NOT auto-commit. Auto-commit applies **only** to Factory (Left) contour operations.

---

## Appendix: Root-Level Instruction Bearing Files (MetaClaw)

| File | Purpose | AUDIT-FIRST Status |
|------|---------|-------------------|
| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | This document — universal root-level rule | ✅ DEFINES |
| `.claude/CLAUDE_CODE_CANON.md` | Session canon (Rules 1–9 + extensions) | ✅ REFERENCES THIS DOC |
| `docs/canon/software-factory-canon-v1.md` | Factory operating model | ✅ REFERENCES THIS DOC |
| `AGENTS.md` | Three-partner architecture | ✅ PROPAGATES |
| `COLLAB.md` | Project collaboration | ✅ PROPAGATES |
| `free-claude-code/CLAUDE.md` | FCC subproject canon | ✅ ALIGNED |

---

*Enacted: 2026-08-26*  
*Version: 1.1 (normalized)*  
*Authority: Operator directive — root-level universal*  
*Supersedes: All subordinate atomic/stop-and-wait instructions unless canon-boundary sanctioned*
