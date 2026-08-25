# AGENTS.md — MetaClaw

**Repository:** `~/MetaClaw`  
**Version:** 1.1 | 2026-08-26 (normalized)  
**Purpose:** Agent execution architecture for MetaClaw meta-learning framework  
**Architecture:** Factory-Only / Three-Terminal (LEFT / CENTRAL / RIGHT)

---

## ⚠️ ROOT CANON — единый SSOT (2026-08-26)

Терминальный workflow всех контуров определяет **один файл**:
`banxe-ai-rnd/research` → `docs/canon/CANON-FACTORY-SSOT.md`, норма **CORE-10-29**
(исполнитель кода Aider/Codex, Claude Code оркеструет; cloud-vs-local по классу данных;
непрерывный фронт + STOP-гейты; consult-цепь Codex → Fable → Mistral → Kimi; auto-commit только
Фабрикой; имена CENTRAL / LEFT / RIGHT). `FACTORY_OPERATING_SYSTEM.md` и
`CLAUDE_CODE_OPERATING_PRINCIPLE.md` в этом репозитории — указатели туда, не копии (ADR-102).

---

## Core mission

This repository is the **MetaClaw meta-learning framework** — agents learn and evolve from conversations without GPU.

### Three-Terminal Architecture

| Terminal | Canonical Name | Role | Execution |
|----------|----------------|------|-----------|
| **Central** | CENTRAL (Brain) | Architect, planner, reviewer, orchestrator | NO direct code execution |
| **Left** | LEFT (Factory Interface) | Task assignment, agent orchestration, evidence routing | NO direct code generation |
| **Right** | RIGHT (Assistant) | Research, audit, summary, brief preparation | NO code execution |
| **Factory** | Aider + Codex + agents | Code generation, edits, tests, commands | SOLE execution layer |

**Key principle:** Terminals decide and plan; Factory executes. No terminal bypasses Factory.

---

## Instruction hierarchy

1. **Explicit user instruction** (highest authority)
2. **Root-level canon**: `research/docs/canon/CANON-FACTORY-SSOT.md` (CORE-10-29);
   `FACTORY_OPERATING_SYSTEM.md` / `CLAUDE_CODE_OPERATING_PRINCIPLE.md` здесь — указатели
3. **Session canon**:
   - `.claude/CLAUDE_CODE_CANON.md` (Rules 1–9 + terminal extensions)
4. **Project context**:
   - `CLAUDE.md` (project identity)
   - `AGENTS.md` (this file)
   - `COLLAB.md` (collaboration patterns)
5. **Global defaults**: `~/.claude/CLAUDE.md`

---

## Repository structure

```
~/MetaClaw/
├── .claude/
│   └── CLAUDE_CODE_CANON.md     ← Session canon (Rules 1–9 + terminal extensions)
├── metaclaw/                   ← Core package
│   ├── agents/
│   ├── memory/
│   └── evolution/
├── tests/                      ← Test suite
├── examples/                   ← Usage examples
├── docs/                       ← Documentation
│   ├── canon/
│   ├── sources/                  ← Audit sources
│   └── audit/                    ← Coverage intel
├── FACTORY_OPERATING_SYSTEM.md ← Universal root canon
├── CLAUDE_CODE_OPERATING_PRINCIPLE.md ← Execution law
├── AGENTS.md                   ← This file
└── COLLAB.md                   ← Project collaboration
```

---

## Terminal Roles Detail

Роли CENTRAL (Brain) / LEFT (Factory Interface) / RIGHT (Assistant) и исполнители Фабрики
(Aider primary, Codex secondary, агенты очереди) — нормативно в SSOT `CANON-FACTORY-SSOT.md`
CORE-10-29 п.1 и п.6; здесь не дублируются.

---

## Collaboration pattern

- **Claude Code (Central)** — planner, reviewer, orchestrator; assigns to Factory.
- **Factory (Aider/Codex)** — execution agent (file edits, tests, commands).
- **User** interacts with Central terminal only.

**One terminal = one project = one repo** (invariant INV-08).

---

## Project isolation

This repository is **MetaClaw only**. Do not mix files, code, or context with:
- Banxe (`vibe-coding`)
- GUIYON (`guiyon`)
- Developer-core (`~/developer`)
- Any other project

---

## Repository conventions

- Source: `metaclaw/`
- Tests: `tests/`
- Scripts: `scripts/`
- Examples: `examples/`
- Docs: `docs/`
- Audit sources: `docs/sources/`
- Coverage intel: `docs/audit/`

---

## Before making changes

1. Read `CANON-FACTORY-SSOT.md` CORE-10-29 п.1 (Factory-only coding) и п.3 (non-atomic).
3. Preserve existing API contracts (other projects may depend on the package).
4. Run tests after changes: `pytest tests/ -v`
5. Keep `requirements.txt` and `pyproject.toml` in sync.

---

## Commit style

- English identifiers
- `feat/fix/test/docs/chore/canon` prefix
- Never commit secrets
- Format: `type(scope): message [IL-XXX]`

---

## Files reference

| File | Purpose | Authority |
|------|---------|-----------|
| `FACTORY_OPERATING_SYSTEM.md` | Pointer → SSOT CORE-10-29 | pointer |
| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | Pointer → SSOT CORE-10-29 | pointer |
| `.claude/CLAUDE_CODE_CANON.md` | Session canon (Rules 1–9) | Session |
| `AGENTS.md` | This file — terminal architecture | Project |
| `COLLAB.md` | Collaboration patterns | Project |
| `CLAUDE.md` | Project identity (BANXE gateway) | Project |

---

## Definition of done

A task is complete when:

- [ ] Factory execution verified (Aider/Codex)
- [ ] Tests pass (`pytest`)
- [ ] Lint clean (`ruff`)
- [ ] Audit trail recorded
- [ ] Commit with proper format
- [ ] No secrets committed

---

*Updated: 2026-08-26 (normalized v1.1)*  
*Alignment: research/docs/canon/CANON-FACTORY-SSOT.md v7 / CORE-10-29 (2026-08-26)*
