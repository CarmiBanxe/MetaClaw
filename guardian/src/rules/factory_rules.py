"""Factory Guardian rules — 8 rules per ADR-019 §6.1.

A.3.1: stubs returning PASS. Real logic lands in A.3.3 with backbone qwen3.5:35b calls.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RuleResult:
    rule_id: str
    status: str  # PASS | WARN | BLOCK
    reason: str = ""


class FactoryRules:
    """Each method maps 1:1 to ADR-019 §6.1 rules."""

    def r1_prompt_canon_compliance(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("F1-prompt-canon", "PASS")

    def r2_ledger_entry_required(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("F2-ledger-entry", "PASS")

    def r3_roadmap_append_only(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("F3-roadmap-append-only", "PASS")

    def r4_no_offhand(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("F4-no-offhand", "PASS")

    def r5_adr_amendment_paired(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("F5-adr-amendment-paired", "PASS")

    def r6_status_no_regression(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("F6-status-no-regression", "PASS")

    def r7_factory_baseline_locked(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("F7-factory-baseline-locked", "PASS")

    def r8_factory_branch_prefix(self, diff: str, memory: dict) -> RuleResult:
        return RuleResult("F8-factory-branch-prefix", "PASS")

    def evaluate_all(self, diff: str, memory: dict) -> list[RuleResult]:
        return [
            self.r1_prompt_canon_compliance(diff, memory),
            self.r2_ledger_entry_required(diff, memory),
            self.r3_roadmap_append_only(diff, memory),
            self.r4_no_offhand(diff, memory),
            self.r5_adr_amendment_paired(diff, memory),
            self.r6_status_no_regression(diff, memory),
            self.r7_factory_baseline_locked(diff, memory),
            self.r8_factory_branch_prefix(diff, memory),
        ]
