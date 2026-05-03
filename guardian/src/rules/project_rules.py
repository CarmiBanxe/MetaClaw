"""Project Guardian rules — 8 rules per ADR-019 §6.2 (BANXE EMI ruleset v1.0).

A.3.1: stubs returning PASS. Real logic lands in A.3.3 with backbone llama3.3:70b calls.
"""

from __future__ import annotations

from .factory_rules import RuleResult


class ProjectRules:
    """Each method maps 1:1 to ADR-019 §6.2 rules."""

    def r1_p0_priorities_blocking(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("P1-p0-priorities", "PASS")

    def r2_invariants_amendment_required(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("P2-invariants-amendment", "PASS")

    def r3_pii_aml_deny_paths(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("P3-pii-aml-deny", "PASS")

    def r4_audit_retention_5y(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("P4-audit-retention", "PASS")

    def r5_no_float_money(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("P5-no-float-money", "PASS")

    def r6_aml_screening_present(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("P6-aml-screening", "PASS")

    def r7_sprint_scope(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("P7-sprint-scope", "PASS")

    def r8_api_backwards_compat(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("P8-api-backwards-compat", "PASS")

    def evaluate_all(self, diff: str, memory: dict) -> list[RuleResult]:
        return [
            self.r1_p0_priorities_blocking(diff, memory),
            self.r2_invariants_amendment_required(diff, memory),
            self.r3_pii_aml_deny_paths(diff, memory),
            self.r4_audit_retention_5y(diff, memory),
            self.r5_no_float_money(diff, memory),
            self.r6_aml_screening_present(diff, memory),
            self.r7_sprint_scope(diff, memory),
            self.r8_api_backwards_compat(diff, memory),
        ]
