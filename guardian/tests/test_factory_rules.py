"""Tests for FactoryRules — 8 rules × 4 cases (PASS / WARN / BLOCK / edge)."""

from __future__ import annotations

from datetime import date

import pytest

from src.rules import AuditContext
from src.rules.factory_rules import FactoryRules


def _memory(**overrides):
    base = {
        "memory": "",
        "ledger": "",
        "gap_register": "",
        "canon": "",
        "hitl": "",
        "constitution": "",
        "adrs": [],
        "roadmap": "",
    }
    base.update(overrides)
    return base


@pytest.fixture
def rules():
    return FactoryRules()


# ============ F1 prompt-canon ============
def test_f1_pass_all_markers(rules):
    ctx = AuditContext(prompt="canon: ZERO QUESTIONS, BEST-ANSWER, FORMAT one→next.")
    r = rules.r1_prompt_canon_compliance(ctx, _memory())
    assert r.status == "PASS"


def test_f1_warn_partial(rules):
    ctx = AuditContext(prompt="canon and FORMAT only")
    r = rules.r1_prompt_canon_compliance(ctx, _memory())
    assert r.status == "WARN"
    assert "missing canon markers" in r.reasons[0]


def test_f1_warn_empty(rules):
    r = rules.r1_prompt_canon_compliance(AuditContext(prompt=""), _memory())
    assert r.status == "WARN"


def test_f1_case_insensitive(rules):
    ctx = AuditContext(prompt="Canon ZERO Questions BEST-Answer Format")
    r = rules.r1_prompt_canon_compliance(ctx, _memory())
    assert r.status == "PASS"


# ============ F2 ledger-entry ============
def test_f2_pass_benign_prompt_empty_ledger(rules):
    r = rules.r2_ledger_entry_required(AuditContext(prompt="hello"), _memory())
    assert r.status == "PASS"


def test_f2_block_new_inst_empty_ledger(rules):
    ctx = AuditContext(prompt="SPRINT_FOO_BAR new sprint instructions here")
    r = rules.r2_ledger_entry_required(ctx, _memory(), today=date(2026, 5, 3))
    assert r.status == "BLOCK"
    assert "no INS-* entries" in r.reasons[0]


def test_f2_block_new_inst_stale_ledger(rules):
    ctx = AuditContext(prompt="TASK_NEW do this")
    mem = _memory(ledger="INS-2026-01-01-OLD entry")
    r = rules.r2_ledger_entry_required(ctx, mem, today=date(2026, 5, 3))
    assert r.status == "BLOCK"
    assert "old (>24h)" in r.reasons[0]


def test_f2_pass_fresh_ledger(rules):
    ctx = AuditContext(prompt="SPRINT_X please")
    mem = _memory(ledger="INS-2026-05-03-FRESH entry")
    r = rules.r2_ledger_entry_required(ctx, mem, today=date(2026, 5, 3))
    assert r.status == "PASS"


# ============ F3 roadmap-append-only ============
def test_f3_pass_no_diff(rules):
    r = rules.r3_roadmap_append_only(AuditContext(), _memory())
    assert r.status == "PASS"


def test_f3_pass_non_roadmap_diff(rules):
    diff = "+++ b/src/foo.py\n-## Section A\n"
    r = rules.r3_roadmap_append_only(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


def test_f3_block_section_deleted(rules):
    diff = "+++ b/docs/roadmap/banxe.md\n-## §10 Section X\n+## §11 Section Y\n"
    r = rules.r3_roadmap_append_only(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"
    assert "deletes 1" in r.reasons[0]


def test_f3_pass_roadmap_pure_append(rules):
    diff = "+++ b/docs/roadmap/banxe.md\n+## §11 New section\n+content\n"
    r = rules.r3_roadmap_append_only(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


# ============ F4 no-offhand ============
def test_f4_pass_with_valid_id(rules):
    ctx = AuditContext(instruction_id="INS-2026-05-03-A3.3-RULES")
    r = rules.r4_no_offhand(ctx, _memory())
    assert r.status == "PASS"


def test_f4_warn_no_id(rules):
    r = rules.r4_no_offhand(AuditContext(), _memory())
    assert r.status == "WARN"
    assert "offhand" in r.reasons[0].lower()


def test_f4_warn_invalid_id(rules):
    ctx = AuditContext(instruction_id="random-task-42")
    r = rules.r4_no_offhand(ctx, _memory())
    assert r.status == "WARN"
    assert "format invalid" in r.reasons[0]


def test_f4_pass_id_with_dot_token(rules):
    ctx = AuditContext(instruction_id="INS-2026-05-03-A3.3-RULES-extra")
    r = rules.r4_no_offhand(ctx, _memory())
    assert r.status == "PASS"


# ============ F5 adr-amendment-paired ============
def test_f5_pass_no_adr_touched(rules):
    diff = "--- a/src/x.py\n+++ b/src/x.py\n+pass\n"
    r = rules.r5_adr_amendment_paired(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


def test_f5_block_adr_no_pairing(rules):
    diff = "--- a/decisions/ADR-007-money.md\n+++ b/decisions/ADR-007-money.md\n+changed\n"
    r = rules.r5_adr_amendment_paired(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


def test_f5_pass_with_amendment(rules):
    diff = (
        "--- a/decisions/ADR-007-money.md\n"
        "+++ b/decisions/ADR-007-money.md\n"
        "--- a/constitution/amendments/amendment-03.md\n"
        "+++ b/constitution/amendments/amendment-03.md\n"
        "+content\n"
    )
    r = rules.r5_adr_amendment_paired(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


def test_f5_pass_with_new_adr_creation(rules):
    diff = (
        "--- a/decisions/ADR-019.md\n"
        "+++ b/decisions/ADR-019.md\n"
        "new file mode 100644\n"
        "+++ b/decisions/ADR-021-new.md\n"
    )
    r = rules.r5_adr_amendment_paired(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


# ============ F6 status-no-regression ============
def test_f6_pass_no_diff(rules):
    r = rules.r6_status_no_regression(AuditContext(), _memory())
    assert r.status == "PASS"


def test_f6_block_done_to_open(rules):
    diff = "-Status: DONE\n+Status: OPEN\n"
    r = rules.r6_status_no_regression(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


def test_f6_warn_with_gap_register(rules):
    diff = "-Status: PASS\n+Status: FAIL\n+ see GAP-REGISTER.md\n"
    r = rules.r6_status_no_regression(AuditContext(diff=diff), _memory())
    assert r.status == "WARN"


def test_f6_pass_progression(rules):
    diff = "-Status: OPEN\n+Status: DONE\n"
    r = rules.r6_status_no_regression(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


# ============ F7 factory-baseline-locked ============
def test_f7_pass_no_baseline_touched(rules):
    diff = "+++ b/src/foo.py\n+pass\n"
    r = rules.r7_factory_baseline_locked(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


def test_f7_block_settings_no_adr(rules):
    diff = '+++ b/.claude/settings.json\n+{"canon": "new"}\n'
    r = rules.r7_factory_baseline_locked(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


def test_f7_pass_settings_with_adr_ref(rules):
    diff = '+++ b/.claude/settings.json\n+{"canon": "new"}\n+# motivated by ADR-019\n'
    r = rules.r7_factory_baseline_locked(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


def test_f7_block_workflow_no_adr(rules):
    diff = "+++ b/.github/workflows/factory-guard.yml\n+jobs: {}\n"
    r = rules.r7_factory_baseline_locked(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


# ============ F8 factory-branch-prefix ============
def test_f8_pass_no_branch(rules):
    r = rules.r8_factory_branch_prefix(AuditContext(prompt="factory rollout"), _memory())
    assert r.status == "PASS"


def test_f8_pass_factory_prefix_correct(rules):
    ctx = AuditContext(branch="factory/ai-onboarding", prompt="factory rollout step")
    r = rules.r8_factory_branch_prefix(ctx, _memory())
    assert r.status == "PASS"


def test_f8_warn_factory_work_wrong_prefix(rules):
    ctx = AuditContext(
        branch="feat/something",
        files_changed=[".claude/settings.json"],
    )
    r = rules.r8_factory_branch_prefix(ctx, _memory())
    assert r.status == "WARN"


def test_f8_pass_non_factory_work(rules):
    ctx = AuditContext(branch="feat/payments", files_changed=["src/payments/router.py"])
    r = rules.r8_factory_branch_prefix(ctx, _memory())
    assert r.status == "PASS"
