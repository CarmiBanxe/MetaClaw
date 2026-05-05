"""Claude-bash scope rules — ADR-025 canon enforcement at bash level.

Covers the bash-detectable subset of 13 canon violations (violations-2026-05-04.md):
- §8: never print secrets or their metadata
- §10: ADR-031 deny-paths (never cat/read protected paths)
- §6: scope verification (never operate in sandbox/frozen repos)

References: ADR-025, G-CANON-01, violations #3, #5, #9, #10, #13.
"""

from __future__ import annotations

import re
from typing import Any

from . import AuditContext, RuleResult

# §10 deny-paths from ADR-031
_DENY_PATH_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"compliance/cases/"),
    re.compile(r"kyc/raw/"),
    re.compile(r"secrets/"),
    re.compile(r"\.env"),
    re.compile(r"\.pem\b"),
    re.compile(r"/id_rsa|/id_ed25519|/id_ecdsa"),
]

# §8 secret metadata patterns
_SECRET_LEAK_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"cat\s+.*\.env"),
    re.compile(r"cat\s+.*secrets/"),
    re.compile(r"echo\s+.*\$(.*PASSWORD|.*SECRET|.*TOKEN|.*KEY)", re.IGNORECASE),
    re.compile(r"printenv\b"),
    re.compile(r"env\s*\|\s*grep", re.IGNORECASE),
    re.compile(r"base64\s+.*\.pem"),
]

# §6 frozen sandbox paths
_FROZEN_SANDBOX_PATHS: list[re.Pattern[str]] = [
    re.compile(r"/data/banxe-emi-stack\b"),
]

# Dangerous destructive commands (general safety)
_DANGEROUS_COMMANDS: list[re.Pattern[str]] = [
    re.compile(r"\brm\s+-rf\s+/"),
    re.compile(r"\bgit\s+push\s+--force\b"),
    re.compile(r"\bgit\s+reset\s+--hard\b"),
    re.compile(r"\bdrop\s+(table|database)\b", re.IGNORECASE),
]


class ClaudeBashRules:
    """Ruleset for scope='claude.bash' — bash commands from AI agents."""

    def evaluate_all(self, ctx: AuditContext, memory: dict[str, Any]) -> list[RuleResult]:
        return [
            self.r1_deny_paths(ctx),
            self.r2_secret_leak(ctx),
            self.r3_frozen_sandbox(ctx),
            self.r4_dangerous_commands(ctx),
        ]

    def r1_deny_paths(self, ctx: AuditContext) -> RuleResult:
        """§10 ADR-031: block commands touching deny-paths."""
        prompt = ctx.prompt
        for pat in _DENY_PATH_PATTERNS:
            match = pat.search(prompt)
            if match:
                return RuleResult(
                    rule_id="CB1-deny-path",
                    status="BLOCK",
                    reasons=[f"§10 ADR-031 deny-path violation: {match.group()}"],
                    evidence=[prompt[:200]],
                )
        return RuleResult(rule_id="CB1-deny-path", status="PASS")

    def r2_secret_leak(self, ctx: AuditContext) -> RuleResult:
        """§8: block commands that would print secrets or metadata."""
        prompt = ctx.prompt
        for pat in _SECRET_LEAK_PATTERNS:
            match = pat.search(prompt)
            if match:
                return RuleResult(
                    rule_id="CB2-secret-leak",
                    status="BLOCK",
                    reasons=[f"§8 secret/metadata leak: {match.group()}"],
                    evidence=[prompt[:200]],
                )
        return RuleResult(rule_id="CB2-secret-leak", status="PASS")

    def r3_frozen_sandbox(self, ctx: AuditContext) -> RuleResult:
        """§6: warn on commands targeting frozen sandbox repos."""
        prompt = ctx.prompt
        for pat in _FROZEN_SANDBOX_PATHS:
            match = pat.search(prompt)
            if match:
                return RuleResult(
                    rule_id="CB3-frozen-sandbox",
                    status="WARN",
                    reasons=[f"§6 frozen sandbox access: {match.group()}"],
                    evidence=[prompt[:200]],
                )
        return RuleResult(rule_id="CB3-frozen-sandbox", status="PASS")

    def r4_dangerous_commands(self, ctx: AuditContext) -> RuleResult:
        """General safety: block destructive commands without explicit approval."""
        prompt = ctx.prompt
        for pat in _DANGEROUS_COMMANDS:
            match = pat.search(prompt)
            if match:
                return RuleResult(
                    rule_id="CB4-dangerous-cmd",
                    status="BLOCK",
                    reasons=[f"Destructive command detected: {match.group()}"],
                    evidence=[prompt[:200]],
                )
        return RuleResult(rule_id="CB4-dangerous-cmd", status="PASS")
