#!/usr/bin/env python3
"""Diagnostic: commits 1df8b66..016dc26 (inclusive) vs main / org-cleanup branch.

Read-only — no repo mutations. Writes tools/phase4_org_cleanup_audit.txt, exits 0.
Run from the MetaClaw repo root (or any git repo that contains these SHAs).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

START_SHA: str = "1df8b66"
END_SHA: str = "016dc26"
TARGET_BRANCH: str = "org-cleanup/phase4-hw-matrix-roc-rpc"


def git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return proc.stdout.strip()


def branches_containing(full_sha: str) -> set[str]:
    try:
        raw = git("branch", "-a", "--contains", full_sha)
    except subprocess.CalledProcessError:
        return set()
    return {
        b.strip().lstrip("* ").removeprefix("remotes/")
        for b in raw.splitlines()
        if b.strip()
    }


def main() -> int:
    # Output file lives next to the script (tools/phase4_org_cleanup_audit.txt)
    out_file: Path = Path(__file__).parent / "phase4_org_cleanup_audit.txt"

    lines: list[str] = []

    def emit(s: str = "") -> None:
        print(s)
        lines.append(s)

    # ── 1. Current HEAD ────────────────────────────────────────────────────────
    head_sha = git("rev-parse", "HEAD")
    head_msg = git("log", "-1", "--format=%s")
    current_branch = git("rev-parse", "--abbrev-ref", "HEAD")

    emit("=== HEAD ===")
    emit(f"Branch : {current_branch}")
    emit(f"SHA    : {head_sha}")
    emit(f"Message: {head_msg}")
    emit()

    # ── 2. Resolve full SHAs for range endpoints ───────────────────────────────
    try:
        start_full = git("rev-parse", START_SHA)
        end_full = git("rev-parse", END_SHA)
    except subprocess.CalledProcessError as exc:
        emit(f"ERROR: cannot resolve range endpoints — {exc}")
        return 1

    emit("=== Range ===")
    emit(f"Start  : {start_full[:9]}  ({START_SHA})")
    emit(f"End    : {end_full[:9]}  ({END_SHA})")
    emit()

    # ── 3. Walk commits END → START (inclusive) ────────────────────────────────
    # \x1f as separator survives any punctuation in commit messages.
    try:
        log_raw = git("log", "--format=%H\x1f%s", end_full)
    except subprocess.CalledProcessError as exc:
        emit(f"ERROR: git log failed — {exc}")
        return 1

    commits: list[tuple[str, str]] = []
    found_start = False
    for line in log_raw.splitlines():
        if not line:
            continue
        sha, _, msg = line.partition("\x1f")
        commits.append((sha, msg))
        if sha == start_full:
            found_start = True
            break

    if not found_start:
        emit(
            f"WARNING: {START_SHA} not found in ancestry of {END_SHA} — "
            f"showing {len(commits)} commit(s) from {END_SHA} backwards"
        )
        emit()

    emit(f"=== Commits {START_SHA}..{END_SHA} inclusive ({len(commits)} total) ===")
    emit()
    emit(f"{'SHORT SHA':<12}  {'STATUS':<22}  MESSAGE")
    emit("-" * 95)

    # Cache branch membership to avoid redundant git calls in summary.
    membership: list[tuple[str, str, set[str]]] = []
    for sha, msg in commits:
        containing: set[str] = branches_containing(sha)
        in_main = "main" in containing or "origin/main" in containing
        in_target = (
            TARGET_BRANCH in containing
            or f"origin/{TARGET_BRANCH}" in containing
        )

        if in_main:
            status = "✓ in main"
        elif in_target:
            status = "— unique to branch"
        else:
            others = sorted(containing)[:3]
            label = ", ".join(others) if others else "(no local branch)"
            status = f"? other: {label}"

        membership.append((sha, status, containing))
        emit(f"{sha[:9]:<12}  {status:<22}  {msg[:58]}")

    # ── 4. Summary ─────────────────────────────────────────────────────────────
    in_main_count = sum(
        1 for _, _, c in membership
        if "main" in c or "origin/main" in c
    )
    unique_count = len(membership) - in_main_count

    emit()
    emit(f"Summary : {in_main_count} in main, {unique_count} unique to branch")
    emit(f"Target  : {TARGET_BRANCH}")
    emit()
    emit("Legend:")
    emit("  ✓ in main         — commit is reachable from main (already merged or cherry-picked)")
    emit("  — unique to branch — commit exists on target branch only")
    emit("  ? other           — commit not on main or target (detached / other branch)")

    # ── 5. Write output file ───────────────────────────────────────────────────
    out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    emit()
    emit(f"Saved → {out_file}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
