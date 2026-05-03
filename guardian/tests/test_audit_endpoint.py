"""End-to-end smoke for /health + /audit using FastAPI TestClient.

Storage is overridden so tests do not require a live ClickHouse instance.
Failure path verified by injecting a store whose write() returns (False, "...").
"""

from __future__ import annotations

from typing import Any

import pytest

fastapi = pytest.importorskip("fastapi")
from fastapi.testclient import TestClient  # noqa: E402

from src.api.main import app, get_store  # noqa: E402


class _StubStoreOK:
    BACKEND = "clickhouse"

    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []

    def write(self, event: dict[str, Any]) -> tuple[bool, str | None]:
        self.calls.append(event)
        return True, None


class _StubStoreFail:
    BACKEND = "clickhouse"

    def write(self, event: dict[str, Any]) -> tuple[bool, str | None]:
        return False, "stub-induced failure"


@pytest.fixture
def client_ok():
    store = _StubStoreOK()
    app.dependency_overrides[get_store] = lambda: store
    try:
        yield TestClient(app), store
    finally:
        app.dependency_overrides.clear()


@pytest.fixture
def client_failing():
    app.dependency_overrides[get_store] = lambda: _StubStoreFail()
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()


def test_health(client_ok) -> None:
    client, _ = client_ok
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_audit_smoke_factory(client_ok) -> None:
    client, store = client_ok
    payload = {
        "subject_type": "pull_request",
        "subject_id": "CarmiBanxe/MetaClaw#42",
        "scope": "factory",
        "prompt": "diff: +1 line",
        "actor": "pytest",
    }
    r = client.post("/audit", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["verdict"]["result"] in {"pass", "warn", "fail"}
    assert body["verdict"]["scope"] == "factory"
    assert body["verdict"]["subject_id"] == payload["subject_id"]
    assert body["storage_status"]["attempted"] is True
    assert body["storage_status"]["written"] is True
    assert body["storage_status"]["error"] is None
    assert body["request_id"]
    assert body["timestamp_utc"].endswith("Z")
    assert len(store.calls) == 1
    assert store.calls[0]["scope"] == "factory"


def test_audit_returns_loaded_domains(client_ok) -> None:
    client, _ = client_ok
    payload = {
        "subject_type": "prompt",
        "subject_id": "session-1",
        "scope": "project",
        "prompt": "noop",
    }
    r = client.post("/audit", json=payload)
    assert r.status_code == 200
    domains = r.json()["loaded_domains"]
    expected = {
        "adrs",
        "canon",
        "constitution",
        "gap_register",
        "hitl",
        "ledger",
        "memory",
        "roadmap",
    }
    assert set(domains) == expected


def test_storage_failure_does_not_break_response(client_failing) -> None:
    client = client_failing
    payload = {
        "subject_type": "pull_request",
        "subject_id": "repo#1",
        "scope": "factory",
        "prompt": "diff",
    }
    r = client.post("/audit", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["verdict"]["result"] in {"pass", "warn", "fail"}
    assert body["storage_status"]["attempted"] is True
    assert body["storage_status"]["written"] is False
    assert body["storage_status"]["error"] == "stub-induced failure"


def test_audit_dry_run_skips_storage(client_ok) -> None:
    client, store = client_ok
    payload = {
        "subject_type": "pull_request",
        "subject_id": "repo#2",
        "scope": "factory",
        "prompt": "diff",
        "dry_run": True,
    }
    r = client.post("/audit", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["storage_status"]["attempted"] is False
    assert body["storage_status"]["written"] is False
    assert store.calls == []


def test_audit_unknown_scope_returns_unknown(client_ok) -> None:
    client, _ = client_ok
    payload = {
        "subject_type": "prompt",
        "subject_id": "x",
        "scope": "mystery-family",
        "prompt": "noop",
    }
    r = client.post("/audit", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["verdict"]["result"] == "unknown"
    assert "unknown scope" in body["verdict"]["summary"]
