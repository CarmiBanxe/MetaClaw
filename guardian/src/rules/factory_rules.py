"""Factory Guardian rules — 8 deterministic checks per ADR-019 §6.1.

A.3.3: real Python logic. No LLM calls; LLM enrichment may layer on in A.3.4.
"""

from __future__ import annotations

import re
from datetime import date, datetime
from typing import Any

from . import AuditContext, RuleResult

CANON_MARKERS = ["canon", "zero questions", "best-answer", "format"]
INS_RE = re.compile(r"INS-(\d{4}-\d{2}-\d{2})-[\w.+-]+")
NEW_INSTRUCTION_RE = re.compile(
    r"(^|\n)\s*(SPRINT[_\s-]\w+|TASK[_\s-]\w+|INSTRUCTION:|CANON_ABSOLUTE)", re.IGNORECASE
)
DELETED_SECTION_RE = re.compile(r"^-(##\s+.+)$", re.MULTILINE)
ADR_TOUCH_RE = re.compile(r"[+-]{3}\s+[ab]/.*ADR-\d+[^\s]*\.md", re.IGNORECASE)
NEW_FILE_RE = re.compile(r"^new file mode\s+\d+\s*$|^---\s+/dev/null$", re.MULTILINE)
AMENDMENT_RE = re.compile(r"amendment[s_-]?\d*\.md|/amendments/", re.IGNORECASE)
BASELINE_PATHS = (".claude/settings.json", "factory-guard.yml", ".claude/CLAUDE.md")
ADR_REF_RE = re.compile(r"\bADR-\d{3,}\b")
INS_FORMAT_RE = re.compile(r"^INS-\d{4}-\d{2}-\d{2}-")


class FactoryRules:
    def r1_prompt_canon_compliance(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        text = ctx.prompt.lower()
        matched = [m for m in CANON_MARKERS if m in text]
        if len(matched) == len(CANON_MARKERS):
            return RuleResult(
                "F1-prompt-canon",
                "PASS",
                evidence=[f"all {len(CANON_MARKERS)} canon markers present"],
            )
        missing = [m for m in CANON_MARKERS if m not in matched]
        return RuleResult(
            "F1-prompt-canon",
            "WARN",
            reasons=[f"missing canon markers: {', '.join(missing)}"],
            evidence=[f"matched={len(matched)}/{len(CANON_MARKERS)}"],
        )

    def r2_ledger_entry_required(
        self,
        ctx: AuditContext,
        memory: dict[str, Any],
        *,
        today: date | None = None,
    ) -> RuleResult:
        ledger = memory.get("ledger", "") or ""
        has_new_inst = bool(NEW_INSTRUCTION_RE.search(ctx.prompt))
        ins_dates = INS_RE.findall(ledger)
        if not ins_dates:
            if has_new_inst:
                return RuleResult(
                    "F2-ledger-entry",
                    "BLOCK",
                    reasons=["new instruction in prompt but ledger has no INS-* entries"],
                )
            return RuleResult("F2-ledger-entry", "PASS", evidence=["ledger empty, prompt benign"])
        latest_str = sorted(ins_dates)[-1]
        try:
            latest = datetime.strptime(latest_str, "%Y-%m-%d").date()
        except ValueError:
            return RuleResult(
                "F2-ledger-entry",
                "WARN",
                reasons=[f"unparseable INS date: {latest_str}"],
            )
        now = today or date.today()
        age_days = (now - latest).days
        if has_new_inst and age_days > 1:
            return RuleResult(
                "F2-ledger-entry",
                "BLOCK",
                reasons=[
                    f"new instruction detected but latest INS entry is {age_days}d old (>24h)"
                ],
                evidence=[f"latest INS-{latest_str}"],
            )
        return RuleResult(
            "F2-ledger-entry",
            "PASS",
            evidence=[f"latest INS-{latest_str}, age={age_days}d, new_inst={has_new_inst}"],
        )

    def r3_roadmap_append_only(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        diff = ctx.diff
        if not diff:
            return RuleResult("F3-roadmap-append-only", "PASS", evidence=["no diff supplied"])
        touches_roadmap = "/roadmap/" in diff or "ROADMAP" in diff or "roadmap.md" in diff.lower()
        if not touches_roadmap:
            return RuleResult("F3-roadmap-append-only", "PASS")
        deleted = DELETED_SECTION_RE.findall(diff)
        if deleted:
            return RuleResult(
                "F3-roadmap-append-only",
                "BLOCK",
                reasons=[f"roadmap diff deletes {len(deleted)} section(s)"],
                evidence=deleted[:3],
            )
        return RuleResult("F3-roadmap-append-only", "PASS")

    def r4_no_offhand(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        if ctx.instruction_id:
            if INS_FORMAT_RE.match(ctx.instruction_id):
                return RuleResult("F4-no-offhand", "PASS", evidence=[ctx.instruction_id])
            return RuleResult(
                "F4-no-offhand",
                "WARN",
                reasons=[f"instruction_id format invalid: {ctx.instruction_id}"],
            )
        return RuleResult(
            "F4-no-offhand",
            "WARN",
            reasons=["no instruction_id in context — possible offhand work"],
        )

    def r5_adr_amendment_paired(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        diff = ctx.diff
        if not diff:
            return RuleResult("F5-adr-amendment-paired", "PASS", evidence=["no diff"])
        touched = ADR_TOUCH_RE.findall(diff)
        if not touched:
            return RuleResult("F5-adr-amendment-paired", "PASS")
        has_new = bool(NEW_FILE_RE.search(diff))
        has_amendment = bool(AMENDMENT_RE.search(diff))
        if has_new or has_amendment:
            return RuleResult(
                "F5-adr-amendment-paired",
                "PASS",
                evidence=[f"touched={len(touched)}; pairing detected"],
            )
        return RuleResult(
            "F5-adr-amendment-paired",
            "BLOCK",
            reasons=[f"diff touches {len(touched)} ADR file(s) without amendment or new ADR"],
            evidence=touched[:3],
        )

    def r6_status_no_regression(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        diff = ctx.diff
        if not diff:
            return RuleResult("F6-status-no-regression", "PASS")
        regressions: list[str] = []
        if re.search(r"^-.*\bDONE\b", diff, re.MULTILINE) and re.search(
            r"^\+.*\b(OPEN|TODO|PENDING)\b", diff, re.MULTILINE
        ):
            regressions.append("DONE→OPEN/TODO/PENDING")
        if re.search(r"^-.*\bPASS\b", diff, re.MULTILINE) and re.search(
            r"^\+.*\bFAIL\b", diff, re.MULTILINE
        ):
            regressions.append("PASS→FAIL")
        if not regressions:
            return RuleResult("F6-status-no-regression", "PASS")
        gap_mentioned = "GAP-REGISTER" in diff or "gap-register" in diff.lower()
        if gap_mentioned:
            return RuleResult(
                "F6-status-no-regression",
                "WARN",
                reasons=[f"status regression with GAP-REGISTER ref: {', '.join(regressions)}"],
            )
        return RuleResult(
            "F6-status-no-regression",
            "BLOCK",
            reasons=[f"status regression without GAP-REGISTER entry: {', '.join(regressions)}"],
            evidence=regressions,
        )

    def r7_factory_baseline_locked(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        diff = ctx.diff
        files = ctx.files_changed or []
        if not diff and not files:
            return RuleResult("F7-factory-baseline-locked", "PASS")
        touched = [p for p in BASELINE_PATHS if p in diff or any(p in f for f in files)]
        if not touched:
            return RuleResult("F7-factory-baseline-locked", "PASS")
        if ADR_REF_RE.search(diff) or ADR_REF_RE.search(ctx.prompt):
            return RuleResult(
                "F7-factory-baseline-locked",
                "PASS",
                evidence=[f"baseline touched ({touched}) with ADR ref"],
            )
        return RuleResult(
            "F7-factory-baseline-locked",
            "BLOCK",
            reasons=[f"factory baseline modified without ADR reference: {', '.join(touched)}"],
            evidence=touched,
        )

    def r8_factory_branch_prefix(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        branch = ctx.branch
        if not branch:
            return RuleResult("F8-factory-branch-prefix", "PASS", evidence=["no branch context"])
        is_factory_work = (
            "factory" in ctx.prompt.lower()
            or any("factory/" in f for f in ctx.files_changed)
            or any(".claude/" in f for f in ctx.files_changed)
            or any(".github/workflows/factory" in f for f in ctx.files_changed)
        )
        if is_factory_work and not branch.startswith("factory/"):
            return RuleResult(
                "F8-factory-branch-prefix",
                "WARN",
                reasons=[f"factory-related work but branch '{branch}' lacks 'factory/' prefix"],
            )
        return RuleResult("F8-factory-branch-prefix", "PASS", evidence=[f"branch={branch}"])

    def evaluate_all(self, ctx: AuditContext, memory: dict[str, Any]) -> list[RuleResult]:
        return [
            self.r1_prompt_canon_compliance(ctx, memory),
            self.r2_ledger_entry_required(ctx, memory),
            self.r3_roadmap_append_only(ctx, memory),
            self.r4_no_offhand(ctx, memory),
            self.r5_adr_amendment_paired(ctx, memory),
            self.r6_status_no_regression(ctx, memory),
            self.r7_factory_baseline_locked(ctx, memory),
            self.r8_factory_branch_prefix(ctx, memory),
        ]
