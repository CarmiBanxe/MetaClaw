# COLLAB.md — MetaClaw

## Universal Operating Principle

All work follows `CLAUDE_CODE_OPERATING_PRINCIPLE.md`:
- **FACTORY-ONLY CODING:** No terminal codes directly; Factory (Aider/Codex) executes.
- **ALL FACTORY STAFF ENABLED:** All available Factory agents execute their roles unless restricted.
- **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive for **concise final verification only**.
- **NON-ATOMIC:** Continuous execution across non-branching work.
- **AUDIT-FIRST:** Fresh shell audit before each material step.
- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks.

Main Claude resource verifies factory outputs/findings/summaries, not re-processes bulk work.

## Project

MetaClaw — agent meta-learning framework. Agents learn and evolve from conversations without GPU.

## Collaboration pattern

- **Claude Code** — planner, reviewer, orchestrator.
- **Aider** — execution agent (file edits, tests, commands) via MCP.
- User interacts only with Claude in one terminal: `cd ~/MetaClaw && claude`

## Project isolation

This repository is independent. Do not mix files, code, or context with Banxe (`vibe-coding`), GUIYON, or any other project.

## Repository conventions

- Source: `metaclaw/`
- Tests: `tests/`
- Scripts: `scripts/`
- Examples: `examples/`

## Before making changes

1. Preserve existing API contracts (other projects may depend on the package).
2. Run tests after changes: `pytest tests/ -v`
3. Keep `requirements.txt` and `pyproject.toml` in sync.

## Commit style

English identifiers. feat/fix/test/docs/chore prefix. Never commit secrets.
