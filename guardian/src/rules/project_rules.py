"""Project Guardian rules — 8 deterministic checks per ADR-019 §6.2 (BANXE EMI v1.0).

A.3.3: real Python logic. No LLM calls; LLM enrichment may layer on in A.3.4.
"""

from __future__ import annotations

import fnmatch
import re
from typing import Any

from . import AuditContext, RuleResult

DENY_PATTERNS = [
    "compliance/cases/",
    "kyc/raw/",
    "secrets/",
    ".env",
    "*.pem",
    "*.key",
    "id_rsa",
    "id_ed25519",
]

PAYMENT_PATHS = ["/payments/", "/transfer/", "/transactions/", "/payout/", "payment_router"]
AML_KEYWORDS = [
    "aml",
    "sanctions",
    "screening",
    "screen_aml",
    "yente",
    "watchman",
    "marble",
    "kyc_check",
]
MONEY_TOKENS = "amount|price|balance|sum|total|fee|cost|value|payment|payout|wire"
ENDPOINT_DECORATOR_RE = re.compile(
    r"@(?:app|router)\.(get|post|put|delete|patch)\(['\"]([^'\"]+)['\"]"
)
TTL_RE = re.compile(r"TTL\s+\w+\s*\+\s*INTERVAL\s+(\d+)\s+(YEAR|MONTH|DAY|WEEK)", re.IGNORECASE)
INVARIANT_RE = re.compile(r"\bI-\d{2,3}\b")
ADR_OR_AMEND_RE = re.compile(r"\bADR-\d{3,}\b|amendment", re.IGNORECASE)
P0_DOWNGRADE_RE = re.compile(r"^\-.*\|\s*P0\s*\|.*$", re.MULTILINE)
P0_NEW_LOWER_RE = re.compile(r"^\+.*\|\s*P[123]\s*\|.*$", re.MULTILINE)
P0_DEFER_RE = re.compile(r"^\+.*\b(deferred|deprioritiz|drop|skip)\b", re.MULTILINE | re.IGNORECASE)


def _ttl_to_days(value: int, unit: str) -> int:
    unit = unit.upper()
    if unit.startswith("YEAR"):
        return value * 365
    if unit.startswith("MONTH"):
        return value * 30
    if unit.startswith("WEEK"):
        return value * 7
    return value


def _files_from_diff(diff: str) -> list[str]:
    return re.findall(r"^[+-]{3}\s+[ab]/(.+)$", diff, re.MULTILINE)


class ProjectRules:
    def r1_p0_priorities_blocking(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        diff = ctx.diff
        if not diff:
            return RuleResult("P1-p0-priorities", "PASS")
        downgraded = bool(P0_DOWNGRADE_RE.search(diff)) and bool(P0_NEW_LOWER_RE.search(diff))
        deferred_p0 = bool(re.search(r"^-.*\bP0\b", diff, re.MULTILINE)) and bool(
            P0_DEFER_RE.search(diff)
        )
        if not (downgraded or deferred_p0):
            return RuleResult("P1-p0-priorities", "PASS")
        signals = []
        if downgraded:
            signals.append("P0 → lower priority in matrix table")
        if deferred_p0:
            signals.append("P0 entry marked deferred/dropped")
        prompt_lower = ctx.prompt.lower()
        diff_lower = diff.lower()
        has_override = (
            "operator-override" in prompt_lower
            or "operator-override" in diff_lower
            or "operator approval" in prompt_lower
            or "operator approval" in diff_lower
        )
        if has_override:
            return RuleResult(
                "P1-p0-priorities",
                "WARN",
                reasons=[f"P0 change with operator override: {', '.join(signals)}"],
            )
        return RuleResult(
            "P1-p0-priorities",
            "BLOCK",
            reasons=[f"P0 deprioritization without operator override: {', '.join(signals)}"],
            evidence=signals,
        )

    def r2_invariants_amendment_required(
        self, ctx: AuditContext, memory: dict[str, Any]
    ) -> RuleResult:
        diff = ctx.diff
        if not diff:
            return RuleResult("P2-invariants-amendment", "PASS")
        changed_lines = [
            ln
            for ln in diff.splitlines()
            if (ln.startswith("+") or ln.startswith("-"))
            and not (ln.startswith("+++") or ln.startswith("---"))
            and INVARIANT_RE.search(ln)
        ]
        if not changed_lines:
            return RuleResult("P2-invariants-amendment", "PASS")
        if ADR_OR_AMEND_RE.search(diff):
            return RuleResult(
                "P2-invariants-amendment",
                "PASS",
                evidence=[
                    f"invariant change paired with ADR/amendment ({len(changed_lines)} lines)"
                ],
            )
        return RuleResult(
            "P2-invariants-amendment",
            "BLOCK",
            reasons=["invariant (I-XX) changes detected without ADR/amendment in diff"],
            evidence=changed_lines[:3],
        )

    def r3_pii_aml_deny_paths(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        diff = ctx.diff
        files = list(ctx.files_changed)
        if not files and diff:
            files = _files_from_diff(diff)
        if not files:
            return RuleResult("P3-pii-aml-deny", "PASS")
        hits: list[tuple[str, str]] = []
        for f in files:
            for pat in DENY_PATTERNS:
                if pat.startswith("*") and fnmatch.fnmatch(f, pat):
                    hits.append((f, pat))
                    break
                if pat in f:
                    hits.append((f, pat))
                    break
        if hits:
            return RuleResult(
                "P3-pii-aml-deny",
                "BLOCK",
                reasons=[f"diff touches deny_paths (ADR-016/021): {len(hits)} hit(s)"],
                evidence=[f"{f} matches '{p}'" for f, p in hits[:3]],
            )
        return RuleResult("P3-pii-aml-deny", "PASS")

    def r4_audit_retention_5y(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        diff = ctx.diff
        if not diff:
            return RuleResult("P4-audit-retention", "PASS")
        old_ttls = [
            _ttl_to_days(int(n), u)
            for ln in diff.splitlines()
            if ln.startswith("-") and not ln.startswith("---")
            for n, u in TTL_RE.findall(ln)
        ]
        new_ttls = [
            _ttl_to_days(int(n), u)
            for ln in diff.splitlines()
            if ln.startswith("+") and not ln.startswith("+++")
            for n, u in TTL_RE.findall(ln)
        ]
        if old_ttls and new_ttls:
            if max(new_ttls) < max(old_ttls):
                return RuleResult(
                    "P4-audit-retention",
                    "BLOCK",
                    reasons=[
                        f"TTL reduced from {max(old_ttls)}d to {max(new_ttls)}d (FCA CASS 5y minimum)"
                    ],
                    evidence=[f"old_max={max(old_ttls)}d", f"new_max={max(new_ttls)}d"],
                )
        if new_ttls and not old_ttls:
            below_5y = [d for d in new_ttls if d < 1825]
            if below_5y:
                return RuleResult(
                    "P4-audit-retention",
                    "BLOCK",
                    reasons=[f"new TTL {min(below_5y)}d below 5y minimum (FCA CASS)"],
                )
        return RuleResult("P4-audit-retention", "PASS")

    def r5_no_float_money(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        text = ctx.diff or ctx.prompt
        patterns = [
            re.compile(rf"\bfloat\s*\(\s*\w*({MONEY_TOKENS})", re.IGNORECASE),
            re.compile(rf"parseFloat\s*\(\s*\w*({MONEY_TOKENS})", re.IGNORECASE),
            re.compile(rf":\s*float\s*=.*\b({MONEY_TOKENS})\b", re.IGNORECASE),
            re.compile(rf"\b({MONEY_TOKENS})\s*:\s*float\b", re.IGNORECASE),
        ]
        added_hits: list[str] = []
        for line in text.splitlines():
            checking = (
                line[1:]
                if (line.startswith("+") and not line.startswith("+++"))
                else (line if not text.startswith(("+", "-")) and "diff" not in text[:50] else None)
            )
            if checking is None and not (line.startswith("+") and not line.startswith("+++")):
                continue
            target = checking if checking is not None else line[1:]
            if any(p.search(target) for p in patterns):
                added_hits.append(line.strip())
        if added_hits:
            return RuleResult(
                "P5-no-float-money",
                "BLOCK",
                reasons=[f"float used for money values (ADR-007): {len(added_hits)} hit(s)"],
                evidence=added_hits[:3],
            )
        return RuleResult("P5-no-float-money", "PASS")

    def r6_aml_screening_present(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        diff = ctx.diff
        files = ctx.files_changed
        touches_payment = any(p in diff for p in PAYMENT_PATHS) or any(
            any(p in f for p in PAYMENT_PATHS) for f in files
        )
        if not touches_payment:
            return RuleResult("P6-aml-screening", "PASS")
        haystack = (diff + " " + " ".join(files)).lower()
        if any(re.search(rf"\b{k}\b", haystack) for k in AML_KEYWORDS):
            return RuleResult(
                "P6-aml-screening",
                "PASS",
                evidence=["payment path touched + AML reference present"],
            )
        return RuleResult(
            "P6-aml-screening",
            "WARN",
            reasons=["payment endpoint touched without AML/sanctions reference"],
        )

    def r7_sprint_scope(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        branch = ctx.branch
        if not branch:
            return RuleResult("P7-sprint-scope", "PASS", evidence=["no branch context"])
        sprint_in_branch = re.search(r"v(\d+\.\d+)-phase", branch)
        if not sprint_in_branch:
            return RuleResult(
                "P7-sprint-scope",
                "PASS",
                evidence=[f"branch '{branch}' has no sprint version token"],
            )
        roadmap = memory.get("roadmap", "") or ""
        active = set(re.findall(r"banxe-cluster-v(\d+\.\d+)-phase", roadmap))
        if not active:
            return RuleResult(
                "P7-sprint-scope",
                "PASS",
                evidence=["no active sprints detected in roadmap"],
            )
        version = sprint_in_branch.group(1)
        if version in active:
            return RuleResult(
                "P7-sprint-scope",
                "PASS",
                evidence=[f"branch sprint v{version} ∈ active {sorted(active)}"],
            )
        prompt_lower = ctx.prompt.lower()
        labels = str(ctx.extra.get("labels", "")).lower()
        cross = "cross-sprint" in prompt_lower or "cross-sprint" in labels
        if cross:
            return RuleResult(
                "P7-sprint-scope",
                "PASS",
                evidence=[f"cross-sprint label/marker for v{version}"],
            )
        return RuleResult(
            "P7-sprint-scope",
            "WARN",
            reasons=[
                f"branch sprint v{version} not in active sprints {sorted(active)} and no cross-sprint label"
            ],
        )

    def r8_api_backwards_compat(self, ctx: AuditContext, memory: dict[str, Any]) -> RuleResult:
        diff = ctx.diff
        if not diff:
            return RuleResult("P8-api-backwards-compat", "PASS")
        removed: list[tuple[str, str]] = []
        added: list[tuple[str, str]] = []
        for line in diff.splitlines():
            if line.startswith("+++") or line.startswith("---"):
                continue
            m = ENDPOINT_DECORATOR_RE.search(line)
            if not m:
                continue
            entry = (m.group(1).lower(), m.group(2))
            if line.startswith("-"):
                removed.append(entry)
            elif line.startswith("+"):
                added.append(entry)
        deleted = [e for e in removed if e not in added]
        if not deleted:
            return RuleResult("P8-api-backwards-compat", "PASS")
        if ADR_OR_AMEND_RE.search(diff):
            return RuleResult(
                "P8-api-backwards-compat",
                "WARN",
                reasons=[
                    f"endpoint(s) removed/renamed with ADR/amendment ref: "
                    f"{[f'{m} {p}' for m, p in deleted[:3]]}"
                ],
            )
        return RuleResult(
            "P8-api-backwards-compat",
            "BLOCK",
            reasons=[
                f"endpoint(s) removed/renamed without ADR amendment: "
                f"{[f'{m} {p}' for m, p in deleted[:3]]}"
            ],
            evidence=[f"{m} {p}" for m, p in deleted[:3]],
        )

    def evaluate_all(self, ctx: AuditContext, memory: dict[str, Any]) -> list[RuleResult]:
        return [
            self.r1_p0_priorities_blocking(ctx, memory),
            self.r2_invariants_amendment_required(ctx, memory),
            self.r3_pii_aml_deny_paths(ctx, memory),
            self.r4_audit_retention_5y(ctx, memory),
            self.r5_no_float_money(ctx, memory),
            self.r6_aml_screening_present(ctx, memory),
            self.r7_sprint_scope(ctx, memory),
            self.r8_api_backwards_compat(ctx, memory),
        ]
