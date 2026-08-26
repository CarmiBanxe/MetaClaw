# COLLAB.md — MetaClaw Collaboration Canon
**Version:** 2.0 | 2026-08-26  
**Authority:** Project-level — defers to Root Canon (`CLAUDE.md`) and SSOT CORE-10-29

---

## ROOT CANON DEFERENCE

All work follows **Root Canon** (`CLAUDE.md`) and `CLAUDE_CODE_OPERATING_PRINCIPLE.md`:

| Principle | Implementation |
|-----------|----------------|
| **FACTORY-ONLY CODING** | No terminal codes directly; Factory (Aider/Codex) sole execution layer |
| **TERMINAL ROLES** | Left=Factory execution, Central=Brain/dispatch, Right=Assistant/audit |
| **AUDIT-FIRST** | Fresh shell audit before each material step |
| **NON-ATOMIC** | Continuous execution across non-branching work; stop only at real fork |
| **TOKEN ECONOMY** | Cheap/free/lower-tier for bulk; expensive for **concise final verification only** |
| **CONSULT CHAIN** | Codex → Fable → Mistral → Kimi (fixed order) |
| **OPERATOR CONTROL** | Factory prepares brief; **Operator controls delivery — NEVER autonomously sent** |

Main Claude resource verifies Factory outputs/findings/summaries, not re-processes bulk work.

---

## CONSULTATION MODE (Detailed)

**On real fork:**
1. Factory prepares ONE consultation brief (task, context, question, data-class, expected output).
2. Factory emits brief as text artifact, then STOPS.
3. **Operator takes brief to separate consultation window.**
4. Operator executes consult chain: `Codex → Fable → Mistral → Kimi`.
5. Operator returns results to Factory.
6. Factory reconciles opinions and resumes continuous work.

**Prohibited:** Factory self-consult, autonomous brief dispatch, consultation inside factory contour.

---

## PROJECT

MetaClaw — agent meta-learning framework. Agents learn and evolve from conversations without GPU.

---

## COLLABORATION PATTERN

| Role | Function |
|------|----------|
| **Claude Code (Central/Brain)** | Planner, reviewer, orchestrator; assigns to Factory |
| **Factory (Aider/Codex)** | Sole execution agent: file edits, tests, commands |
| **Operator** | Directs Central; runs consultation externally; approves merges |

User interacts with Central terminal; Central drives Factory.

---

## PROJECT ISOLATION

This repository is **independent**. Do not mix files, code, or context with:
- Banxe (`vibe-coding`)
- GUIYON
- Developer-core (`~/developer`)
- Any other project

**One terminal = one project = one repo** (invariant).

---

## REPOSITORY CONVENTIONS

- Source: `metaclaw/`
- Tests: `tests/`
- Scripts: `scripts/`
- Examples: `examples/`

---

## BEFORE MAKING CHANGES

1. Preserve existing API contracts.
2. Run tests: `pytest tests/ -v`
3. Keep `requirements.txt` and `pyproject.toml` in sync.

---

## COMMIT STYLE

- English identifiers
- Prefix: `feat/fix/test/docs/chore/canon`
- Never commit secrets
- Format: `type(scope): message [IL-XXX]`

---

## HIERARCHY

1. Explicit user instruction
2. **Root Canon** (`CLAUDE.md`)
3. **SSOT:** `banxe-ai-rnd/research/docs/canon/CANON-FACTORY-SSOT.md` CORE-10-29
4. **Session Canon** (`.claude/CLAUDE_CODE_CANON.md`)
5. **This file** (project collaboration)

---

*Updated: 2026-08-26 | Alignment: Root Canon v2.0 / SSOT CORE-10-29*
