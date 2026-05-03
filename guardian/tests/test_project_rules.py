"""Tests for ProjectRules — 8 rules × 4 cases (PASS / WARN / BLOCK / edge)."""

from __future__ import annotations

import pytest

from src.rules import AuditContext
from src.rules.project_rules import ProjectRules


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
    return ProjectRules()


# ============ P1 p0-priorities ============
def test_p1_pass_no_diff(rules):
    r = rules.r1_p0_priorities_blocking(AuditContext(), _memory())
    assert r.status == "PASS"


def test_p1_block_p0_downgrade_no_override(rules):
    diff = "-| E-safeguard | DONE | P0 | 7 May 2026 |\n+| E-safeguard | DONE | P3 | deferred |\n"
    r = rules.r1_p0_priorities_blocking(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


def test_p1_warn_p0_with_operator_override(rules):
    diff = (
        "-| E-safeguard | DONE | P0 |\n"
        "+| E-safeguard | DONE | P2 |\n"
        "+# operator-override approved\n"
    )
    r = rules.r1_p0_priorities_blocking(AuditContext(diff=diff), _memory())
    assert r.status == "WARN"


def test_p1_pass_p0_unchanged(rules):
    diff = "+| New row | TODO | P0 |\n"
    r = rules.r1_p0_priorities_blocking(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


# ============ P2 invariants-amendment ============
def test_p2_pass_no_invariant_change(rules):
    diff = "+normal code change\n"
    r = rules.r2_invariants_amendment_required(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


def test_p2_block_invariant_change_no_adr(rules):
    diff = "-Invariant I-07: Decimal only\n+Invariant I-07: float allowed\n"
    r = rules.r2_invariants_amendment_required(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


def test_p2_pass_invariant_change_with_adr(rules):
    diff = "-Invariant I-07: Decimal only\n+Invariant I-07: see ADR-099 amendment\n"
    r = rules.r2_invariants_amendment_required(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


def test_p2_pass_invariant_in_filename_only(rules):
    diff = "+++ b/docs/invariants.md\n+ no I-XX token here\n"
    r = rules.r2_invariants_amendment_required(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


# ============ P3 pii-aml-deny-paths ============
def test_p3_pass_normal_files(rules):
    ctx = AuditContext(files_changed=["src/foo.py", "tests/test_foo.py"])
    r = rules.r3_pii_aml_deny_paths(ctx, _memory())
    assert r.status == "PASS"


def test_p3_block_compliance_cases(rules):
    ctx = AuditContext(files_changed=["compliance/cases/case_123.json"])
    r = rules.r3_pii_aml_deny_paths(ctx, _memory())
    assert r.status == "BLOCK"


def test_p3_block_secret_pem(rules):
    ctx = AuditContext(files_changed=["deploy/server.pem"])
    r = rules.r3_pii_aml_deny_paths(ctx, _memory())
    assert r.status == "BLOCK"


def test_p3_block_kyc_raw_via_diff(rules):
    diff = "--- a/kyc/raw/customer.json\n+++ b/kyc/raw/customer.json\n+data\n"
    r = rules.r3_pii_aml_deny_paths(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


# ============ P4 audit-retention-5y ============
def test_p4_pass_no_diff(rules):
    r = rules.r4_audit_retention_5y(AuditContext(), _memory())
    assert r.status == "PASS"


def test_p4_block_ttl_reduction(rules):
    diff = "-TTL event_date + INTERVAL 5 YEAR\n+TTL event_date + INTERVAL 1 YEAR\n"
    r = rules.r4_audit_retention_5y(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


def test_p4_block_new_ttl_below_5y(rules):
    diff = "+TTL event_date + INTERVAL 30 DAY\n"
    r = rules.r4_audit_retention_5y(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


def test_p4_pass_new_ttl_5y(rules):
    diff = "+TTL event_date + INTERVAL 5 YEAR\n"
    r = rules.r4_audit_retention_5y(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


# ============ P5 no-float-money ============
def test_p5_pass_no_float(rules):
    diff = "+amount: Decimal = Decimal('10.50')\n"
    r = rules.r5_no_float_money(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


def test_p5_block_float_cast(rules):
    diff = "+result = float(amount_pence) / 100\n"
    r = rules.r5_no_float_money(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


def test_p5_block_parsefloat(rules):
    diff = "+const price = parseFloat(priceStr);\n"
    r = rules.r5_no_float_money(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


def test_p5_pass_float_in_removed_line(rules):
    diff = "-result = float(amount) / 100\n+result = Decimal(amount) / Decimal(100)\n"
    r = rules.r5_no_float_money(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


# ============ P6 payment-aml-screening ============
def test_p6_pass_no_payment_touched(rules):
    diff = "+++ b/src/util.py\n+def helper(): pass\n"
    r = rules.r6_aml_screening_present(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


def test_p6_warn_payment_no_aml(rules):
    diff = (
        "+++ b/src/api/payments/router.py\n"
        "+@router.post('/payments/initiate')\n"
        "+def initiate(): pass\n"
    )
    r = rules.r6_aml_screening_present(AuditContext(diff=diff), _memory())
    assert r.status == "WARN"


def test_p6_pass_payment_with_aml(rules):
    diff = (
        "+++ b/src/api/payments/router.py\n"
        "+from src.compliance.screening import screen_aml\n"
        "+@router.post('/payments/initiate')\n"
        "+def initiate(): screen_aml(...)\n"
    )
    r = rules.r6_aml_screening_present(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"


def test_p6_pass_files_changed_only_no_payment(rules):
    ctx = AuditContext(files_changed=["src/utils/format.py"])
    r = rules.r6_aml_screening_present(ctx, _memory())
    assert r.status == "PASS"


# ============ P7 sprint-scope ============
def test_p7_pass_no_branch(rules):
    r = rules.r7_sprint_scope(AuditContext(), _memory())
    assert r.status == "PASS"


def test_p7_pass_branch_no_sprint_token(rules):
    r = rules.r7_sprint_scope(AuditContext(branch="feat/new-thing"), _memory())
    assert r.status == "PASS"


def test_p7_warn_branch_sprint_not_active(rules):
    mem = _memory(roadmap="banxe-cluster-v2.3-phaseN content")
    ctx = AuditContext(branch="feat/v1.0-phase-old")
    r = rules.r7_sprint_scope(ctx, mem)
    assert r.status == "WARN"


def test_p7_pass_branch_sprint_in_active(rules):
    mem = _memory(roadmap="banxe-cluster-v2.3-phaseN content")
    ctx = AuditContext(branch="feat/v2.3-phaseN-impl")
    r = rules.r7_sprint_scope(ctx, mem)
    assert r.status == "PASS"


# ============ P8 api-backwards-compat ============
def test_p8_pass_no_diff(rules):
    r = rules.r8_api_backwards_compat(AuditContext(), _memory())
    assert r.status == "PASS"


def test_p8_block_endpoint_removed(rules):
    diff = "-@app.get('/users/{id}')\n+def something(): pass\n"
    r = rules.r8_api_backwards_compat(AuditContext(diff=diff), _memory())
    assert r.status == "BLOCK"


def test_p8_warn_endpoint_removed_with_adr(rules):
    diff = "-@app.get('/users/{id}')\n+# replaced per ADR-042 amendment\n"
    r = rules.r8_api_backwards_compat(AuditContext(diff=diff), _memory())
    assert r.status == "WARN"


def test_p8_pass_endpoint_added(rules):
    diff = "+@app.get('/users/{id}')\n+def get_user(id): pass\n"
    r = rules.r8_api_backwards_compat(AuditContext(diff=diff), _memory())
    assert r.status == "PASS"
