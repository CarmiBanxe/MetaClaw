# MiroFish Scenarios — MetaClaw Platform Simulations

**Repository:** `~/MetaClaw/`  
**Version:** 2.0 | 2026-04-03  
**Integration:** Three-partner synergy (building Target Platform)

---

## Important: MetaClaw is NOT a Partner

**Architecture Clarity:**

| Layer | Components | Purpose |
|-------|------------|---------|
| **Development-Time Partners** | Claude Code + Qoder CLI + MiroFish | Building MetaClaw |
| **Production Platform** | MetaClaw/OpenClaw | Target product being built |

MetaClaw does NOT participate in its own creation. MiroFish validates MetaClaw designs during development.

---

## Auto-Trigger Detection

MiroFish activates automatically when Claude detects these keywords:

| Keyword Pattern | Triggered Scenario | Priority |
|-----------------|-------------------|----------|
| "agent orchestration", "multi-agent" | Agent behavior simulation | HIGH |
| "HITL gateway", "human takeover" | HITL trust study | CRITICAL |
| "orchestration stress", "load test" | Orchestration stress test | HIGH |
| "UX validation", "agent interaction" | UX testing | MEDIUM |
| "enterprise adoption", "scaling" | Market adoption modeling | LOW |

### Override Mechanism

To skip simulation:
```
"Design X WITHOUT MiroFish simulation"
→ Claude proceeds directly to implementation
```

---

## MetaClaw-Specific Scenarios

### Core Platform Scenarios

| Scenario | Agents | Rounds | Use Case | When Used |
|----------|--------|--------|----------|-----------|
| **agent-behavior.yml** | 350 | 40 | Multi-agent interaction patterns | Before orchestration architecture decisions |
| **hitl-handoff.yml** | 300 | 40 | Human takeover thresholds | Before implementing HITL gateway |
| **orchestration-stress.yml** | 500 | 50 | High-load agent coordination | Quarterly + before major releases |
| **ux-agent-interaction.yml** | 250 | 35 | Agent-to-user interaction patterns | Before UI implementation |

### Inherited Scenarios

| Scenario | Agents | Rounds | Use Case |
|----------|--------|--------|----------|
| **hitl-handoff.yml** | 300 | 40 | HITL trust thresholds |
| **fraud-social-eng.yml** | 400 | 50 | Fraud pattern detection (for security module) |
| **ux-validation.yml** | 200 | 25 | UX validation pipeline |
| **market-adoption.yml** | 600 | 60 | Enterprise adoption projection |

---

## Usage Examples

### Run Simulation from This Project

```bash
cd ~/MetaClaw
bash ../developer/mirofish/run-simulation.sh <scenario-name> --agents 350 --rounds 40
```

### Example: Multi-Agent Behavior Study

```bash
cd ~/MetaClaw
bash ../developer/mirofish/run-simulation.sh agent-behavior --agents 350 --rounds 40
```

**Expected Output:**
- Agent interaction pattern analysis
- Conflict resolution strategies
- Orchestration bottleneck identification

### Example: HITL Gateway Design

```bash
cd ~/MetaClaw
bash ../developer/mirofish/run-simulation.sh hitl-handoff --agents 300 --rounds 40
```

**Expected Output:**
- Trust threshold for human takeover
- Agent handoff protocol recommendations
- User communication templates

---

## Simulation Reports

Reports saved to: `docs/simulations/YYYY-MM-DD-scenario-name.json`

### Report Structure

```json
{
  "simulation_id": "agent-behavior-20260403-143022",
  "scenario": "multi_agent_interaction",
  "summary": {
    "key_finding": "...",
    "recommendation": "..."
  },
  "patterns_detected": [
    "Agent conflict pattern A detected under high load",
    "Successful handoff protocol B identified"
  ],
  "architecture_implications": [
    "Recommend async message queue for agent coordination",
    "HITL gateway should implement circuit breaker pattern"
  ]
}
```

---

## Integration with MetaClaw Development

### Three-Stage Pipeline Example

**Task:** Design multi-agent orchestration

```
Stage 1: Claude Code designs
  → Architecture: AgentOrchestrator class with message bus

Stage 2: MiroFish simulates (auto-triggered)
  → Scenario: agent-behavior.yml (350 agents, 40 rounds)
  → Output: Interaction patterns, bottleneck analysis

Stage 3: Qoder CLI implements
  → Code: src/metaclaw/orchestrator.py
  → Tests: tests/test_orchestrator.py
  → Docs: Update ARCHITECTURE.md
```

---

## Related Documentation

- `~/developer/docs/MIROFISH-INTEGRATION.md` — Full integration plan
- `~/developer/docs/ARCHITECTURE.md` — Two-level architecture explanation
- `ARCHITECTURE.md` — MetaClaw platform design
- `docs/MEMORY.md` — Historical simulation results

---

**Source:** `~/developer/mirofish/scenarios/` (templates)  
**Synced:** 2026-04-03  
**Version:** 2.0 (MetaClaw-specific scenarios)
