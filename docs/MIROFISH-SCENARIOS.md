# MiroFish Scenarios — Project-Specific Simulations

**Repository:** `~/MetaClaw/`  
**Version:** 1.0 | 2026-04-03  
**Integration:** Three-partner synergy (Claude + Qoder + MiroFish)

---

## Auto-Trigger Detection

MiroFish activates automatically when Claude detects these keywords in user requests:

| Keyword Pattern | Triggered Scenario |
|-----------------|-------------------|
| "human approval", "handoff", "дублёр" | HITL trust study |
| "FCA", "sandbox", "compliance policy" | Pre-FCA testing |
| "fraud pattern", "social engineering" | Fraud simulation |
| "market reaction", "launch strategy" | GTM modeling |
| "UX validation", "drop-off", "onboarding" | UX testing |
| "stress test", "crisis scenario" | Stress testing |
| "adoption curve", "market sizing" | Adoption modeling |

### Override Mechanism

To skip simulation:
```
"Design X WITHOUT MiroFish simulation"
→ Claude proceeds directly to implementation
```

---

## Project-Specific Scenarios

### Scenario Library (Inherited from Developer-Core)

All scenarios available from `~/developer/mirofish/scenarios/`:

| Scenario | Agents | Rounds | Use Case |
|----------|--------|--------|----------|
| hitl-handoff.yml | 300 | 40 | HITL trust thresholds |
| pre-fca-sandbox.yml | 250 | 30 | Compliance policy testing |
| fraud-social-eng.yml | 400 | 50 | Fraud pattern detection |
| gtm-reaction.yml | 350 | 35 | Market reaction modeling |
| ux-validation.yml | 200 | 25 | UX validation pipeline |
| fraud-stress-test.yml | 500 | 50 | Quarterly stress testing |
| market-adoption.yml | 600 | 60 | Adoption curve projection |

---

## Usage Examples

### Run Simulation from This Project

```bash
cd ~/MetaClaw
bash ../developer/mirofish/run-simulation.sh <scenario-name> --agents 300 --rounds 40
```

### Example: HITL Handoff Study

```bash
cd ~/MetaClaw
bash ../developer/mirofish/run-simulation.sh hitl-handoff --agents 300 --rounds 40
```

**Expected Output:**
- Trust threshold map by user segment
- Optimal handoff trigger points
- Communication templates

---

## Simulation Reports

Reports saved to: `docs/simulations/YYYY-MM-DD-scenario-name.json`

### Report Structure

```json
{
  "simulation_id": "hitl-handoff-20260403-143022",
  "scenario": "hitl_trust_handoff",
  "summary": {
    "key_finding": "...",
    "recommendation": "..."
  },
  "segment_results": [...],
  "patterns_detected": [...]
}
```

---

## Related Documentation

- `~/developer/docs/MIROFISH-INTEGRATION.md` — Full integration plan
- `~/developer/mirofish/README.md` — Quick start guide
- `~/developer/mirofish/scenarios/` — All scenario templates
