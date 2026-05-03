"""Guardian FastAPI app — A.3.2 runtime slice.

Endpoints:
- GET  /health → liveness probe.
- POST /audit  → memory pull (ADR-020) + rule eval (ADR-019) + sync ClickHouse persist.

Storage failures never break the response: storage_status surfaces the error.
"""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone

from fastapi import Depends, FastAPI

from ..core.auditor import GuardianAuditor
from ..memory_loader import MemoryLoader
from ..storage.clickhouse import ClickHouseAuditStore
from .models import AuditRequest, AuditResponse, StorageStatus, Verdict

app = FastAPI(title="BANXE Guardian", version="0.1.0")
_loader = MemoryLoader()
_auditor = GuardianAuditor(_loader)


def get_store() -> ClickHouseAuditStore:
    return ClickHouseAuditStore()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/audit", response_model=AuditResponse)
def audit(req: AuditRequest, store: ClickHouseAuditStore = Depends(get_store)) -> AuditResponse:
    request_id = req.request_id or str(uuid.uuid4())
    outcome = _auditor.audit(
        prompt=req.prompt,
        scope=req.scope,
        subject_type=req.subject_type,
        subject_id=req.subject_id,
    )
    verdict = Verdict(
        result=outcome.result,
        summary=outcome.summary,
        reasons=outcome.reasons,
        sources=outcome.sources,
        scope=req.scope,
        subject_type=req.subject_type,
        subject_id=req.subject_id,
    )
    now = datetime.now(timezone.utc)
    storage_status = StorageStatus(attempted=False, backend=store.BACKEND, written=False)

    if not req.dry_run:
        storage_status.attempted = True
        event = {
            "event_time_utc": now,
            "request_id": request_id,
            "subject_type": req.subject_type,
            "subject_id": req.subject_id,
            "scope": req.scope,
            "actor": req.actor or "",
            "prompt": req.prompt,
            "verdict_result": verdict.result,
            "verdict_summary": verdict.summary,
            "reasons_json": json.dumps(verdict.reasons),
            "sources_json": json.dumps(verdict.sources),
            "loaded_domains_json": json.dumps(outcome.loaded_domains),
            "dry_run": 1 if req.dry_run else 0,
            "storage_backend": store.BACKEND,
        }
        ok, err = store.write(event)
        storage_status.written = ok
        if err:
            storage_status.error = err

    return AuditResponse(
        request_id=request_id,
        status="ok",
        verdict=verdict,
        storage_status=storage_status,
        loaded_domains=outcome.loaded_domains,
        timestamp_utc=now.isoformat().replace("+00:00", "Z"),
    )
