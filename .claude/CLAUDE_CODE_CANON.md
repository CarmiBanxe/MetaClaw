# Claude Code Session Canon (ABSOLUTE)
**Version:** 2.0 | 2026-08-26  
**Scope:** Session-level rules — additive to Root Canon (`CLAUDE.md`)

**Root Override:** `CLAUDE.md` v2.0 takes precedence for terminal roles, Factory-only execution, audit-first, non-atomic work, token economy, and consultation mode. This canon is binding where not in conflict.

---

## Rules 1–9 (Unchanged, Absolute)

1. **NEVER ASK QUESTIONS.** Pick the best option yourself and execute.
2. **SAFE = AUTO-EXECUTE SILENTLY.** No menus, no confirmations.
3. **UNSAFE = one line OPERATOR_RUN:** `md>` then STOP. Wait for "go".
4. **SUDO on remote:** `sudo -n` first; if fails, print OPERATOR_RUN.
5. **WHEN IN DOUBT:** pick faster, more idempotent approach.
6. **ON ERROR:** diagnose and fix if safe; stop only if unsafe.
7. **SPLIT large ops** into sub-commands; execute sequentially.
8. **APPROVAL MENUS: NEVER SHOW.** Auto-approve safe patterns.
9. **REPORT:** continuous progress, explicit audit basis per step.

**Override Note:** Rule "single summary after sprint" CANCELLED by Root Canon §4 (NON-ATOMIC). Report explicitly: audit basis, decision, execution, next audit, fork status.

---

## Three-Terminal Architecture (Extension)

**Terminal Roles** (per Root Canon §2):

| Terminal | Function | Execution |
|----------|----------|-----------|
| **LEFT** | Factory execution side | Runs commands, edits, tests, deploys — **Factory only** |
| **CENTRAL** | Brain — planner/reviewer/orchestrator | Decides, plans, drives loop; **NO direct code execution** |
| **RIGHT** | Assistant/BEN — document scout/analyst | Read-only audit; **NO execution**; prepares briefs |

**Key Principle:** Terminals formulate tasks; Factory executes. No terminal bypasses Factory.

---

## AUDIT-FIRST (Extension)

- Shell audit embedded before every material step.
- Read-only audit = SAFE (Rule 2).
- State-changing = operator gate (Rule 3).

---

## NON-ATOMIC CONTINUOUS WORK (Extension)

- Default: continuous unified-front execution.
- Stop only at: real fork / sanction gate / authority boundary / unresolved conflict.
- After consultation: resume work continuously.

---

## FACTORY STAFFING + TOKEN ECONOMY (Extension)

- All factory staff enabled by default.
- **Cheap/free tier** (Open Claude Code, local, Codex): bulk prep, aux, decomposition, drafting.
- **Expensive tier** (main Claude): concise final verification, critical review, decision.
- Main Claude verifies Factory outputs, not re-processes bulk.

---

## CONSULTATION MODE (Strict)

**Factory NEVER self-consults.**

On real fork:
1. Factory prepares **one brief** (task, context, question, data-class, expected output).
2. Emits as text artifact, **STOPS**.
3. **Operator performs consultation externally** via separate window.
4. **Consult chain (fixed order):** `Codex → Fable → Mistral → Kimi`.
5. Operator returns results; Factory reconciles; work continues.

**Brief delivery:** Prepared as artifact. **NEVER autonomously sent.** Operator controls delivery.

---

## HIERARCHY

1. Explicit user instruction
2. **Root Canon** (`CLAUDE.md` v2.0)
3. **SSOT:** `banxe-ai-rnd/research/docs/canon/CANON-FACTORY-SSOT.md` CORE-10-29
4. **This file** (session rules 1–9 + extensions)
5. Project context (`AGENTS.md`, `COLLAB.md`)

---

## Cloud-First Development

- FCC is canonical gateway for Claude Code-compatible traffic.
- LiteLLM/local: fallback for offline, continuity, protected workloads.
- Protected data → local-safe only.

---

*Updated: 2026-08-26 | Alignment: Root Canon v2.0 / SSOT CORE-10-29*
