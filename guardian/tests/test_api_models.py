"""Pydantic model roundtrip tests for the /audit contract."""

from __future__ import annotations

from src.api.models import AuditRequest, AuditResponse, StorageStatus, Verdict


def test_audit_request_roundtrip() -> None:
    payload = {
        "request_id": "req-001",
        "subject_type": "pull_request",
        "subject_id": "CarmiBanxe/MetaClaw#42",
        "scope": "factory",
        "prompt": "diff text here",
        "context": {"branch": "main"},
        "actor": "claude-code",
        "dry_run": False,
    }
    req = AuditRequest(**payload)
    dumped = req.model_dump()
    rebuilt = AuditRequest(**dumped)
    assert rebuilt == req


def test_audit_request_defaults() -> None:
    req = AuditRequest(
        subject_type="prompt",
        subject_id="claude-session-1",
        scope="project",
        prompt="hello",
    )
    assert req.request_id is None
    assert req.context is None
    assert req.actor is None
    assert req.dry_run is False


def test_audit_response_roundtrip() -> None:
    resp = AuditResponse(
        request_id="req-002",
        status="ok",
        verdict=Verdict(
            result="pass",
            summary="all rules passed",
            reasons=["F1: PASS"],
            sources=["ADR-019", "ADR-020"],
            scope="factory",
            subject_type="pull_request",
            subject_id="repo#1",
        ),
        storage_status=StorageStatus(
            attempted=True, backend="clickhouse", written=False, error="conn refused"
        ),
        loaded_domains=["adrs", "canon", "memory"],
        timestamp_utc="2026-05-03T19:30:00Z",
    )
    dumped = resp.model_dump()
    rebuilt = AuditResponse(**dumped)
    assert rebuilt == resp
    assert dumped["storage_status"]["error"] == "conn refused"
