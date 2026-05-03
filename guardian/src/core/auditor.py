"""Guardian core auditor — orchestrates memory pull + rule evaluation per family.

A.3.1: stub returning PASS verdict. Real LLM-backed reasoning lands in A.3.3.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..memory_loader import MemoryLoader
from ..rules.factory_rules import FactoryRules, RuleResult
from ..rules.project_rules import ProjectRules


@dataclass
class Verdict:
    family: str  # factory | project
    status: str  # PASS | WARN | BLOCK
    results: list[RuleResult]
    reasons: list[str]


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
