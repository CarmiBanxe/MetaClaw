# AGENTS.md — MetaClaw: Three-Partner Synergy

**Repository:** `~/MetaClaw/`  
**Version:** 2.0 | 2026-04-03  
**Classification:** Banxe AI Bank Proprietary

---

## Core mission

This repository contains **MetaClaw** — Banxe-customized OpenClaw fork for multi-agent orchestration.

**Important:** MetaClaw is the **Target Platform** (production product), not a development partner.

Development uses a **three-partner synergy** model:

---

## Three-Partner Architecture

| Partner | Role | Activation | Scope |
|---------|------|------------|-------|
| **Claude Code** | Architect & Coordinator | Every `claude` session | Design, review, orchestration |
| **Qoder CLI** | Executor | MCP auto-load | Implementation, edits, tests |
| **MiroFish** | Simulator & Validator | Auto-trigger by keywords | Behavioral simulation, stress-testing |

### Target Platform vs. Development Partners

**Two-Level Architecture:**

```
Level 1: Development-Time Partners (Active Now)
┌─────────────────────────────────────────────┐
│  Claude Code ←→ Qoder CLI ←→ MiroFish      │
│  (building MetaClaw)                        │
└─────────────────────────────────────────────┘
              ↓
Level 2: Production Platform (Target Product)
┌─────────────────────────────────────────────┐
│  MetaClaw/OpenClaw                          │
│  (multi-agent orchestrator for banking)     │
└─────────────────────────────────────────────┘
```

**Why MetaClaw is NOT a fourth partner:**
- MetaClaw is what we're **building**, not who we're **building with**
- Analogy: A house doesn't participate in building itself
- In production, MetaClaw will orchestrate banking AI agents (with HITL gates)

---

## MiroFish Applications for MetaClaw

| Scenario | Purpose | When Used |
|----------|---------|-----------|
| **HITL handoff** | Define trust thresholds for human takeover | Before implementing HITL gateway |
| **Agent behavior simulation** | Model how multiple AI agents interact | Before multi-agent architecture decisions |
| **Orchestration stress-test** | Simulate high-load agent coordination | Quarterly |
| **UX validation** | Test agent-to-user interaction patterns | Before UI implementation |
| **Market adoption** | Model enterprise customer onboarding | Before GTM planning |

---

## Automatic Trigger Detection

MiroFish активируется автоматически при обнаружении ключевых паттернов:

| Keyword Pattern | Auto-Trigger | Default Scenario |
|-----------------|--------------|------------------|
| "human approval", "handoff", "дублёр" | ✅ YES | hitl-handoff.yml |
| "agent orchestration", "multi-agent" | ✅ YES | agent-behavior.yml |
| "stress test", "load simulation" | ✅ YES | orchestration-stress.yml |
| "UX validation", "user interaction" | ✅ YES | ux-validation.yml |
| "market adoption", "enterprise" | ✅ YES | market-adoption.yml |

**Override:** User can explicitly disable with "WITHOUT MiroFish simulation"

---

## Instruction hierarchy

1. **Explicit user instruction** (highest authority)
2. **Repository-level contracts**:
   - `CLAUDE.md` — project context
   - `.qoder/context.md` — Qoder execution contract
   - `AGENTS.md` — this file — agent instructions
   - `docs/COLLAB.md` — collaboration pattern
   - `docs/MIROFISH-SCENARIOS.md` — MiroFish scenarios library
   - `ARCHITECTURE.md` — MetaClaw platform design
3. **Global defaults**: `~/.claude/CLAUDE.md`

---

## Workspace

- **Repository:** `/home/mmber/MetaClaw/` (git: main)
- **OpenClaw source:** External dependency (customization target)
- **MCP config:** `/home/mmber/MetaClaw/.mcp.json`
- **Memory:** `/home/mmber/MetaClaw/docs/MEMORY.md`

---

## Collaboration workflow

```bash
cd /home/mmber/MetaClaw

# Interactive session (all three partners work together)
claude

# Implement MetaClaw component
# Claude designs → Qoder implements → MiroFish validates (if needed)

# Run orchestration simulation
# Auto-triggered for architecture-critical decisions
```

---

## Canon (mandatory rules)

### Architecture Clarity
- **MetaClaw = Target Platform** (not a development partner)
- Document clearly: dev-tools vs. product-being-built
- Avoid circular references in documentation

### Memory
- После каждого значимого изменения — обновить `docs/MEMORY.md`
- Коммитить с понятным сообщением

### Style
- **Язык общения:** русский
- **Код:** английский
- **Без лишних файлов**, без over-engineering

---

## Stack

- **Python 3.12** / FastAPI
- **OpenClaw framework** (multi-agent orchestration)
- **Docker Compose** (MiroFish: Neo4j + Ollama + Flask)
- **Redis** (agent coordination)

---

## Files reference

| File | Purpose |
|------|---------|
| `AGENTS.md` | This file — three-partner agent instructions |
| `CLAUDE.md` | Project context & collaboration contract |
| `.qoder/context.md` | Qoder execution contract |
| `.qoder/config.yml` | Qoder CLI configuration |
| `docs/COLLAB.md` | Collaboration pattern documentation |
| `docs/MIROFISH-SCENARIOS.md` | MiroFish scenario library |
| `docs/MEMORY.md` | Long-term project memory |
| `ARCHITECTURE.md` | MetaClaw platform design |

---

## Definition of done

Task is complete when:

- [ ] Implementation matches design specification
- [ ] Tests written and passing (if applicable)
- [ ] `docs/MEMORY.md` updated
- [ ] Git committed with clear message
- [ ] No secrets or credentials in code
- [ ] Architecture documentation updated

---

**Source:** `~/developer/AGENTS.md` (template)  
**Synced:** 2026-04-03  
**Version:** 2.0 (Three-Partner Synergy)
