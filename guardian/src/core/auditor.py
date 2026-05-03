"""Guardian core auditor — orchestrates memory pull + rule evaluation per family.

A.3.1: stub returning PASS verdict.
A.3.2: adds deterministic audit(prompt, scope, ...) for runtime API path. Real LLM-backed
reasoning lands in A.3.3.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..memory_loader import MemoryLoader
from ..rules.factory_rules import FactoryRules, RuleResult
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

    def audit_factory(self, diff: str) -> Verdict:
        memory = self.loader.load_all()
        results = self.factory.evaluate_all(diff, memory)
        return self._aggregate("factory", results)

    def audit_project(self, diff: str) -> Verdict:
        memory = self.loader.load_all()
        results = self.project.evaluate_all(diff, memory)
        return self._aggregate("project", results)

    def audit(self, *, prompt: str, scope: str, subject_type: str, subject_id: str) -> AuditOutcome:
        """Deterministic A.3.2 entry point used by the runtime API.

        Maps `scope` to a family and aggregates rule outputs. `unknown` scope returns
        result="unknown" without rule evaluation but still pulls memory to prove ADR-020 contract.
        """
        memory = self.loader.load_all()
        loaded_domains = sorted(memory.keys())
        sources = ["ADR-019", "ADR-020"]

        if scope == "factory":
            verdict = self._aggregate("factory", self.factory.evaluate_all(prompt, memory))
        elif scope == "project":
            verdict = self._aggregate("project", self.project.evaluate_all(prompt, memory))
        else:
            return AuditOutcome(
                result="unknown",
                summary=f"unknown scope '{scope}' — expected one of: factory, project",
                reasons=[],
                sources=sources,
                loaded_domains=loaded_domains,
            )

        result = _STATUS_TO_RESULT.get(verdict.status, "unknown")
        summary = (
            f"{verdict.family} family: {len(verdict.results)} rules evaluated, "
            f"aggregate {verdict.status}"
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
        reasons = [f"{r.rule_id}: {r.reason}" for r in results if r.reason]
        return Verdict(family=family, status=top, results=results, reasons=reasons)
