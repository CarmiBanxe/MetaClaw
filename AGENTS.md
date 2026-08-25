# AGENTS.md — MetaClaw

**Repository:** `~/MetaClaw`  
**Version:** 1.1 | 2026-08-26 (normalized)  
**Purpose:** Agent execution architecture for MetaClaw meta-learning framework  
**Architecture:** Factory-Only / Three-Terminal (LEFT / CENTRAL / RIGHT)

---

## ⚠️ FACTORY OPERATING SYSTEM (Root-Level Universal)

All agent execution follows `FACTORY_OPERATING_SYSTEM.md`:
- **FACTORY-ONLY CODING:** No terminal codes directly; Factory (Aider/Codex) executes all production code.
- **ALL FACTORY STAFF ENABLED:** All available Factory agents and workers must execute their roles unless restricted by task canon.
- **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive for **concise final verification only**.
- **NON-ATOMIC:** Continuous execution across non-branching work.
- **AUDIT-FIRST:** Fresh shell audit before each material step.
- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks.
- **CLOUD-FIRST FCC:** Non-protected data → cloud via FCC; protected data → local Ollama.

Main Claude resource verifies outputs/findings/summaries from cheap contour, not re-processes bulk work from scratch.

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
2. **Root-level canons**:
   - `FACTORY_OPERATING_SYSTEM.md` (universal)
   - `CLAUDE_CODE_OPERATING_PRINCIPLE.md` (execution law)
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

### CENTRAL (Brain)

**Allowed:**
- Plan, review, orchestrate, decide, delegate
- Concise final verification of factory outputs
- Read root-level system before work starts
- Assign tasks to Factory

**Prohibited:**
- Direct file edits
- Direct code writing
- Direct `Edit`, `Write` for production code

### LEFT (Factory Interface)

**Allowed:**
- Assign tasks to all factory agents
- Review output, route evidence
- Shell CI/CD / infra / audits

**Prohibited:**
- Direct code generation outside Factory
- Originate logic that bypasses factory

### RIGHT (Assistant)

**Allowed:**
- Research, audit, summarize, prepare briefs
- Read-only document scouting
- Tag findings [FACT]/[INFERENCE]/[UNKNOWN]

**Prohibited:**
- Any code execution
- File edits

### Factory (Aider + Codex + agents)

**Execution only:**
- Aider (via MCP) — primary executor
- Codex (plugin/CLI) — secondary executor
- Factory agents — via controlled task queue

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

1. Read `FACTORY_OPERATING_SYSTEM.md` §1 (Factory-Only Coding).
2. Read `CLAUDE_CODE_OPERATING_PRINCIPLE.md` §4 (Non-Atomic).
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
| `FACTORY_OPERATING_SYSTEM.md` | Universal root canon — all contours | **ROOT** |
| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | Execution law (audit-first, non-atomic) | **ROOT** |
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
*Alignment: FACTORY_OPERATING_SYSTEM.md v1.1, CLAUDE_CODE_OPERATING_PRINCIPLE.md v1.1*
