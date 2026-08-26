#!/usr/bin/env python3
"""Patch CLAUDE_CODE_CANON.md: add Safe Allowlist + Best-Effort rule + Stop-Barrier + Guardian enforcement.

Assertions:
  - ANCHOR must be present (idempotency of the insertion point).
  - IDEMPOTENCY_GUARD must NOT be present (prevents double-apply).
Exits 0 on success, non-zero on assertion failure.
"""
from __future__ import annotations

import sys
from pathlib import Path

CANON: Path = Path(__file__).parent.parent / ".claude" / "CLAUDE_CODE_CANON.md"

# ── Assertion markers ─────────────────────────────────────────────────────────
ANCHOR: str = "9. REPORT: single summary after sprint. No JSON unless asked."
IDEMPOTENCY_GUARD: str = "<!-- SAFE-ALLOWLIST-v1 -->"

# ── New sections to append after the Rules block ─────────────────────────────
PATCH: str = """\

<!-- SAFE-ALLOWLIST-v1 -->
## Safe Command Allowlist (zero-question, auto-execute)

Execute silently, no confirmation, no dialog:

| Category | Commands |
|----------|----------|
| Filesystem reads | `read`, `ls`, `find`, `cat`, `head`, `tail` |
| Text processing | `grep`, `awk`, `sed` (read-only), `jq` |
| Git (read-only) | `git status`, `git log`, `git diff`, `git branch`, `git show`, `git reflog`, `git fsck` |
| GitHub (read-only) | `gh pr view`, `gh pr list`, `gh issue view`, `gh issue list` |
| Network (read-only) | `ssh <host>` read-only commands; `curl` GET/HEAD with no mutations |
| Local quality tools | `pytest` (local), `ruff check`, `ruff format --check`, `mypy` |

## Ambiguous Operations — Best Effort / Best Judgment

For operations NOT in the Safe Allowlist and NOT in the Stop-Barrier below:

- Claude picks the best next step **without asking questions**.
- Prefer faster, idempotent, reversible approach when two options are equivalent.
- Resolve uncertainty internally — never surface it as a question to the operator.
- If a safe path and an unsafe path both solve the problem, take the safe path silently.

## Destructive Action Stop-Barrier (STOP + wait for explicit `go`)

Print `OPERATOR_RUN: <exact command>` on one line, then STOP. Do not execute until operator says `go`.

Triggers:
- `git push --force` / `git push -f`
- `git reset --hard`, `git clean -fd`, `git clean -fx`
- `DROP TABLE`, `TRUNCATE`, `DELETE` without `WHERE` on financial/audit tables
- Mass in-place file rewrite without backup or staging copy
- Any action that directly mutates production infrastructure or running services
- Secret / credential rotation in a live environment

## Guardian Enforcement

The Guardian shim (`claude-bash-shim.sh`, scope `claude.bash`) MUST enforce this canon:

| Check | Condition | Verdict |
|-------|-----------|---------|
| CB-SAFE | Command matches Safe Allowlist | PASS — no audit dialog |
| CB-STOP | Command matches Stop-Barrier | BLOCK — log + emit `OPERATOR_RUN` |
| CB-DEFAULT | All other commands | PASS — audit log written (mode=audit) |

Guardian verdict `fail` → `exit 1` (command not executed).
Guardian verdict `pass` → command proceeds.
"""


def main() -> int:
    if not CANON.exists():
        print(f"ERROR: {CANON} not found", file=sys.stderr)
        return 1

    original = CANON.read_text(encoding="utf-8")

    # Assertion 1: anchor must exist
    if ANCHOR not in original:
        print(f"ASSERT FAIL: anchor not found:\n  {ANCHOR!r}", file=sys.stderr)
        return 1

    # Assertion 2: idempotency guard must NOT exist
    if IDEMPOTENCY_GUARD in original:
        print("ASSERT FAIL: patch already applied (idempotency guard found).", file=sys.stderr)
        return 1

    # Insert patch immediately after the anchor line
    patched = original.replace(ANCHOR, ANCHOR + PATCH, 1)

    CANON.write_text(patched, encoding="utf-8")
    print(f"\nPatched → {CANON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
