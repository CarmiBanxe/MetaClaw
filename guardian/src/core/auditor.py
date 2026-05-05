"""Guardian core auditor — orchestrates memory pull + rule evaluation per family.

A.3.1: stub returning PASS.
A.3.2: deterministic audit() entry point for runtime API.
A.3.3: real rule logic via FactoryRules / ProjectRules; carries AuditContext through.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any

from ..memory_loader import MemoryLoader
from ..rules import AuditContext, RuleResult
from ..rules.claude_bash_rules import ClaudeBashRules
from ..rules.factory_rules import FactoryRules
from ..rules.project_rules import ProjectRules

_STATUS_TO_RESULT = {"PASS": "pass", "WARN": "warn", "BLOCK": "fail"}


@dataclass
class Verdict:
    family: str
    status: str
    results: list[RuleResult]
    reasons: list[str]


@dataclass
class AuditOutcome:
    result: str
    summary: str
    reasons: list[str]
    sources: list[str]
    loaded_domains: list[str]


class GuardianAuditor:
    def __init__(self, loader: MemoryLoader | None = None) -> None:
        self.loader = loader or MemoryLoader()
        self.factory = FactoryRules()
        self.project = ProjectRules()
        self.claude_bash = ClaudeBashRules()

    def audit_factory(self, diff: str) -> Verdict:
        memory = self.loader.load_all()
        ctx = AuditContext(prompt="", diff=diff)
        return self._aggregate("factory", self.factory.evaluate_all(ctx, memory))

    def audit_project(self, diff: str) -> Verdict:
        memory = self.loader.load_all()
        ctx = AuditContext(prompt="", diff=diff)
        return self._aggregate("project", self.project.evaluate_all(ctx, memory))

    def audit(
        self,
        *,
        prompt: str,
        scope: str,
        subject_type: str,
        subject_id: str,
        context: dict[str, Any] | None = None,
    ) -> AuditOutcome:
        memory = self.loader.load_all()
        loaded_domains = sorted(memory.keys())
        sources = ["ADR-019", "ADR-020"]
        ctx = AuditContext.from_request(prompt, context)

        if scope == "factory":
            verdict = self._aggregate("factory", self.factory.evaluate_all(ctx, memory))
        elif scope == "project":
            verdict = self._aggregate("project", self.project.evaluate_all(ctx, memory))
        elif scope == "claude.bash":
            verdict = self._aggregate("claude.bash", self.claude_bash.evaluate_all(ctx, memory))
        else:
            return AuditOutcome(
                result="unknown",
                summary=f"unknown scope '{scope}' — expected one of: factory, project",
                reasons=[],
                sources=sources,
                loaded_domains=loaded_domains,
            )

        result = _STATUS_TO_RESULT.get(verdict.status, "unknown")
        counts = Counter(r.status for r in verdict.results)
        summary = (
            f"{verdict.family}: {counts.get('PASS', 0)} PASS / "
            f"{counts.get('WARN', 0)} WARN / {counts.get('BLOCK', 0)} BLOCK"
        )
        reasons = list(verdict.reasons)
        if not reasons:
            reasons = [f"{r.rule_id}: {r.status}" for r in verdict.results]
        return AuditOutcome(
            result=result,
            summary=summary,
            reasons=reasons,
            sources=sources,
            loaded_domains=loaded_domains,
        )

    @staticmethod
    def _aggregate(family: str, results: list[RuleResult]) -> Verdict:
        statuses = [r.status for r in results]
        if "BLOCK" in statuses:
            top = "BLOCK"
        elif "WARN" in statuses:
            top = "WARN"
        else:
            top = "PASS"
        reasons: list[str] = []
        for r in results:
            for line in r.reasons:
                reasons.append(f"{r.rule_id}: {line}")
        return Verdict(family=family, status=top, results=results, reasons=reasons)
