"""Tests for Sprint 5 approval router and Ruflo checkpoint."""
from guardian.src.core.approval_router import (
    determine_gates, create_checkpoint, auto_approve, apply_human_gate,
)


class TestDetermineGates:
    def test_pass_no_sensitive(self):
        assert determine_gates("PASS", ["src/utils.py"]) == ["auto"]

    def test_pass_compliance_path(self):
        assert "operator" in determine_gates("PASS", ["services/aml/monitor.py"])

    def test_pass_architecture_path(self):
        assert "ctio" in determine_gates("PASS", ["docs/adr/ADR-099.md"])

    def test_warn_requires_operator(self):
        assert determine_gates("WARN", []) == ["operator"]

    def test_block_requires_operator_and_mlro(self):
        gates = determine_gates("BLOCK", [])
        assert "operator" in gates
        assert "mlro" in gates


class TestAutoApprove:
    def test_auto_approve_pass(self):
        cp = create_checkpoint("PASS", ["src/utils.py"], ["pack-001"])
        cp = auto_approve(cp)
        assert cp.final_verdict == "APPROVED"
        assert cp.final_signer == "system"

    def test_no_auto_approve_warn(self):
        cp = create_checkpoint("WARN", [], ["pack-002"])
        cp = auto_approve(cp)
        assert cp.final_verdict == "PENDING"


class TestHumanGate:
    def test_operator_approves(self):
        cp = create_checkpoint("WARN", [], ["pack-003"])
        cp = apply_human_gate(cp, "operator", "Moriel Carmi", True, "Looks good")
        assert cp.final_verdict == "APPROVED"

    def test_operator_rejects(self):
        cp = create_checkpoint("WARN", [], ["pack-004"])
        cp = apply_human_gate(cp, "operator", "Moriel Carmi", False, "Needs rework")
        assert cp.final_verdict == "REJECTED"

    def test_block_needs_both_gates(self):
        cp = create_checkpoint("BLOCK", [], ["pack-005"])
        cp = apply_human_gate(cp, "operator", "Moriel Carmi", True)
        assert cp.final_verdict == "PENDING"  # mlro not yet
        cp = apply_human_gate(cp, "mlro", "Moriel Carmi", True)
        assert cp.final_verdict == "APPROVED"
