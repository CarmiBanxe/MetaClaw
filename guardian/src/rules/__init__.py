"""Shared rule primitives — RuleResult + AuditContext (A.3.3 deterministic engine)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuleResult:
    rule_id: str
    status: str  # PASS | WARN | BLOCK
    reasons: list[str] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    confidence: float = 1.0


@dataclass
class AuditContext:
    prompt: str = ""
    diff: str = ""
    branch: str = ""
    instruction_id: str | None = None
    files_changed: list[str] = field(default_factory=list)
    extra: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_request(cls, prompt: str, context: dict[str, Any] | None) -> "AuditContext":
        ctx = context or {}
        files = ctx.get("files_changed") or []
        return cls(
            prompt=prompt,
            diff=str(ctx.get("diff", "")),
            branch=str(ctx.get("branch", "")),
            instruction_id=ctx.get("instruction_id"),
            files_changed=list(files) if isinstance(files, list) else [],
            extra={
                k: v
                for k, v in ctx.items()
                if k not in {"diff", "branch", "instruction_id", "files_changed"}
            },
        )
