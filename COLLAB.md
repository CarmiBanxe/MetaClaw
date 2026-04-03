# COLLAB.md — MetaClaw

## Project

MetaClaw — agent meta-learning framework. Agents learn and evolve from conversations without GPU.

## Collaboration pattern

- **Claude Code** — planner, reviewer, orchestrator.
- **Qoder CLI** — execution agent (file edits, tests, commands) via MCP.
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
