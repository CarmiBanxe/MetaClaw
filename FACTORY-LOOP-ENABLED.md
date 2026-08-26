# Factory Loop Enabled — MetaClaw

Per Software Factory Canon v1.0 Sprint 8 (S8-05).
This repository participates in the factory operating loop.

**Root-Level System:** `FACTORY_OPERATING_SYSTEM.md` governs all execution:
- Factory-only coding (no terminal codes directly)
- Tiered model economy (cheap for bulk, expensive for final check)
- Non-atomic continuous execution
- Audit-first workflow

- Evaluation: scripts/evaluate.sh
- Approval: guardian/src/core/approval_router.py
- Evidence: scripts/generate_evidence_pack.py
- Dashboard: scripts/factory_dashboard.sh

Canon Judge mode: enforce (CANON_JUDGE_MODE env var, default=enforce).
