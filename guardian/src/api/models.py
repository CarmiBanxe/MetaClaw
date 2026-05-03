"""Pydantic models for the Guardian /audit contract (A.3.2)."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

ResultLiteral = Literal["pass", "warn", "fail", "unknown"]
StatusLiteral = Literal["ok", "error"]


class AuditRequest(BaseModel):
    request_id: str | None = None
    subject_type: str
    subject_id: str
    scope: str
    prompt: str
    context: dict[str, Any] | None = None
    actor: str | None = None
    dry_run: bool = False


class Verdict(BaseModel):
    result: ResultLiteral
    summary: str
    reasons: list[str] = Field(default_factory=list)
    sources: list[str] = Field(default_factory=list)
    scope: str
    subject_type: str
    subject_id: str


class StorageStatus(BaseModel):
    attempted: bool
    backend: str
    written: bool
    error: str | None = None


class AuditResponse(BaseModel):
    request_id: str
    status: StatusLiteral
    verdict: Verdict
    storage_status: StorageStatus
    loaded_domains: list[str]
    timestamp_utc: str
