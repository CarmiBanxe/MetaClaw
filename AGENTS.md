# AGENTS.md — MetaClaw Agent Architecture
**Version:** 2.0 | 2026-08-26  
**Authority:** Project-level — defers to Root Canon (`CLAUDE.md`) and SSOT CORE-10-29

---

## ROOT CANON DEFERENCE

**SSOT:** `banxe-ai-rnd/research` → `docs/canon/CANON-FACTORY-SSOT.md`, norm **CORE-10-29**  
(terminal workflow, Factory-only execution, audit-first, non-atomic, consult chain, token economy).

`FACTORY_OPERATING_SYSTEM.md` and `CLAUDE_CODE_OPERATING_PRINCIPLE.md` in this repo are **pointers to SSOT**, not copies (ADR-102).

---

## CORE MISSION

MetaClaw — meta-learning AI agent framework. Agents learn and evolve from conversations without GPU.

---

## THREE-TERMINAL ARCHITECTURE (Canonical)

| Terminal | Name | Function | Execution |
|----------|------|----------|-----------|
| **Central** | BRAIN | Architect, planner, reviewer, orchestrator | **NO direct code execution** — plans and routes |
| **Left** | FACTORY INTERFACE | Task assignment, agent orchestration, evidence routing | **NO direct code generation** — drives Factory |
| **Right** | ASSISTANT (BEN) | Research, audit, summary, brief preparation | **NO code execution** — read-only audit |
| **Factory** | AIDER + CODEX | Code generation, edits, tests, commands | **SOLE execution layer** |

**Key principle:** Terminals decide and plan; Factory executes. **No terminal bypasses Factory.**

---

## FACTORY-ONLY EXECUTION

- Any terminal (Central/Left/Right) formulates tasks for Factory.
- Code and implementation flow **only** through Factory (Aider primary, Codex secondary).
- Direct coding outside Factory default flow: **prohibited**.

---

## AUDIT-FIRST CYCLE

**Mandatory cycle:** `AUDIT → DECIDE → FACTORY EXECUTION → RE-AUDIT`

- Shell audit embedded before every material step.
- Read-only audit = safe class; auto-execute silently.
- State-changing work = operator gate.

---

## NON-ATOMIC CONTINUOUS WORK

- Default: continuous unified-front execution.
- Stop only at: real fork / sanction gate / authority boundary / unresolved factual conflict.
- Factory resumes work after consultation without atomic pauses.

---

## TOKEN ECONOMY

| Tier | Resources | Role |
|------|-----------|------|
| **Cheap/free** | Open Claude Code, local models, Codex | Bulk work: prep, aux, decomposition, drafting |
| **Expensive** | Main Claude | Final verification, critical review, decision |

Main Claude verifies Factory outputs, not re-processes bulk.

---

## CONSULTATION MODE (Strict)

**Factory NEVER self-consults.**

On real fork:
1. Factory prepares **one brief** (task, context, question, expected output).
2. Factory emits brief as text artifact, **stops**.
3. **Operator performs consultation externally** via separate window.
4. **Consult chain (fixed order):** `Codex → Fable → Mistral → Kimi`.
5. Operator returns results; Factory reconciles; work continues.

**Brief delivery:** Prepared as artifact. **NEVER autonomously sent.** Operator controls delivery.

---

## GOVERNED MERGE

- Consultation preparation: automatic.
- Consultation execution: operator-run.
- Merge/push: operator approval required.
- No uncontrolled merge autonomy.

---

## INSTRUCTION HIERARCHY

1. **Explicit user instruction** (highest)
2. **Root Canon** (`CLAUDE.md`)
3. **SSOT:** `banxe-ai-rnd/research/docs/canon/CANON-FACTORY-SSOT.md` CORE-10-29
4. **Session Canon:** `.claude/CLAUDE_CODE_CANON.md`
5. **Project context:** `AGENTS.md` (this file), `COLLAB.md`
6. **Global defaults:** `~/.claude/CLAUDE.md`

---

## REPOSITORY STRUCTURE

```
~/MetaClaw/
├── .claude/
│   └── CLAUDE_CODE_CANON.md     ← Session canon
├── metaclaw/                   ← Core package
├── tests/                      ← Test suite
├── examples/                   ← Usage examples
├── docs/                       ← Documentation
├── FACTORY_OPERATING_SYSTEM.md ← Pointer → SSOT
├── CLAUDE_CODE_OPERATING_PRINCIPLE.md ← Pointer → SSOT
├── AGENTS.md                   ← This file
└── COLLAB.md                   ← Collaboration canon
```

---

## PROJECT ISOLATION

This repository is **MetaClaw only**. Do not mix with:
- Banxe (`vibe-coding`)
- GUIYON
- Developer-core (`~/developer`)

---

## BEFORE MAKING CHANGES

1. Read `CANON-FACTORY-SSOT.md` CORE-10-29 §1 (Factory-only) and §3 (non-atomic).
2. Preserve API contracts.
3. Run tests: `pytest tests/ -v`
4. Keep deps in sync.

---

## COMMIT STYLE

- English identifiers
- Prefix: `feat/fix/test/docs/chore/canon`
- Never commit secrets
- Format: `type(scope): message [IL-XXX]`

---

## FILES REFERENCE

| File | Purpose | Authority |
|------|---------|-----------|
| `CLAUDE.md` | **Root Canon** — all 10 mandatory results | Root |
| `FACTORY_OPERATING_SYSTEM.md` | Pointer → SSOT | Pointer |
| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | Pointer → SSOT | Pointer |
| `.claude/CLAUDE_CODE_CANON.md` | Session rules | Session |
| `AGENTS.md` | This file — architecture | Project |
| `COLLAB.md` | Collaboration patterns | Project |

---

## DEFINITION OF DONE

- [ ] Factory execution verified (Aider/Codex)
- [ ] Tests pass (`pytest`)
- [ ] Lint clean (`ruff`)
- [ ] Audit trail recorded
- [ ] Commit with proper format
- [ ] No secrets committed

---

*Updated: 2026-08-26 (v2.0)*  
*Alignment: Root Canon v2.0 / SSOT CORE-10-29*
