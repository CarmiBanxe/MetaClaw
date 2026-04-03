# .qoder/context.md — Qoder Execution Contract (MetaClaw)

**Repository:** `~/MetaClaw/`  
**Purpose:** Multi-agent orchestration platform (Target Product)  
**Version:** 2.0 | 2026-04-03

---

## Core rule

**Repository scope = ~/MetaClaw/ only.**

This is a **product repository** containing the MetaClaw orchestration platform.

### Architecture clarity

**MetaClaw is the TARGET PLATFORM, not a development partner:**

- Three partners (Claude + Qoder + MiroFish) are BUILDING MetaClaw
- MetaClaw does NOT participate in its own creation
- In production, MetaClaw will orchestrate banking AI agents

---

## Project isolation

**Hard invariant:** This repository is product code.

| Do | Don't |
|----|-------|
| Implement MetaClaw components | Mix files from other projects |
| Document architecture clearly | Confuse dev-tools with product |
| Test orchestration logic | Commit without testing |
| Update MEMORY.md | Expose API keys in code |

### Violation is a critical error

Never:
- Read project files without explicit instruction
- Assume MetaClaw is a "fourth partner"
- Mix development-time and production-time concepts

---

## Role definition

**Qoder CLI role in this repository:**

1. **Platform implementer** — build MetaClaw orchestration components
2. **Test executor** — validate multi-agent scenarios
3. **Documentation updater** — maintain ARCHITECTURE.md

### Typical tasks

- Implement agent orchestration logic
- Create HITL gateway components
- Write integration tests
- Update architecture documentation

---

## Working method

### For implementation tasks

1. Read ARCHITECTURE.md for context
2. Implement component
3. Write tests
4. Update MEMORY.md
5. Commit with clear message

### For MiroFish simulations

When designing orchestration patterns:

1. Claude designs agent interaction model
2. MiroFish simulates agent behavior (auto-trigger)
3. Results validate architecture
4. Qoder implements validated design

**Auto-trigger keywords:** agent orchestration, multi-agent, HITL, stress test, UX validation

---

## Instruction priority

When working in this repository:

1. **User instruction** — explicit implementation commands
2. **This context** (.qoder/context.md) — execution rules
3. **AGENTS.md** — three-partner agent instructions
4. **CLAUDE.md** — project context
5. **ARCHITECTURE.md** — platform design
6. **Global defaults** (~/.claude/CLAUDE.md)

---

## Output expectations

After completing work:

```
✓ Component implemented: {name}
✓ Tests passed: {count}
✓ ARCHITECTURE.md updated: yes/no
✓ MEMORY.md updated: yes
○ Pending: {follow-up actions}
```

---

## Quick reference

| Command | Purpose |
|---------|---------|
| `bash collab.sh worker "task" branch` | Parallel implementation |
| `bash collab.sh run "command"` | Single command execution |
| `bash collab.sh jobs` | Check active tasks |
| `python -m pytest tests/` | Run test suite |

---

## Files in this repository

| Path | Purpose |
|------|---------|
| `.qoder/context.md` | This file — execution contract |
| `.qoder/config.yml` | Qoder CLI configuration |
| `AGENTS.md` | Three-partner agent instructions |
| `CLAUDE.md` | Project context |
| `docs/COLLAB.md` | Collaboration pattern |
| `docs/MIROFISH-SCENARIOS.md` | MiroFish scenario library |
| `docs/MEMORY.md` | Long-term memory |
| `ARCHITECTURE.md` | MetaClaw platform design |
