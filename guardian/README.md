# BANXE AI Guardian (Layer 6)

Two-family architecture compliance enforcement for BANXE AI agents.

## Two families

- **Factory Guardian** (controls *how* we build) — backbone `qwen3.5:35b`, scope: factory + any CarmiBanxe repo, audit log `guardian_audit_factory` (ClickHouse, TTL 5y).
- **Project Guardian** (controls *what* we build) — backbone `llama3.3:70b`, scope: BANXE EMI (current project), audit log `guardian_audit_project` (ClickHouse, TTL 5y).

Common core engine in `src/core/auditor.py` orchestrates both families per their rule sets.

## Anchors

- ADR-019 — Guardian two-family architecture (`~/banxe-architecture/decisions/ADR-019-ai-guardian-two-family.md`).
- ADR-020 — Memory governance (`~/banxe-architecture/decisions/ADR-020-memory-governance.md`).

## Phase plan

| Phase | Scope | Status |
|---|---|---|
| A.3.1 | Skeleton — memory_loader + rule stubs + auditor stub | **DONE** |
| A.3.2 | FastAPI endpoint + ClickHouse schema + audit persistence | NEXT |
| A.3.3 | Real rule engines (8 Factory + 8 Project rules with LLM backbone calls) | PLANNED |
| A.4 | systemd units (`banxe-guardian-factory.service`, `banxe-guardian-project.service`) on evo1 | PLANNED |
| A.5 | GitHub webhook integration + status checks (`guardian/{factory,project}/<rule-id>`) | PLANNED |

## Quickstart (placeholder)

```bash
cd ~/MetaClaw/guardian
pip install -e .
python -c "from src.memory_loader import MemoryLoader; print(sorted(MemoryLoader().load_all().keys()))"
pytest tests/
```

## Memory pull contract (ADR-020)

Each audit MUST load all 10 memory artefacts before any rule check:
MEMORY.md, INSTRUCTION-LEDGER.md, GAP-REGISTER.md, PROMPT-CANON-PROJECT.md, HITL-MATRIX.yaml, constitution + amendments, decisions/*.md, adrs/*.md, banxe-emi-stack/docs/adr/*.md, active sprint roadmap.

Cache TTL: 60s (per ADR-020 §"Verify drill" mitigation).
