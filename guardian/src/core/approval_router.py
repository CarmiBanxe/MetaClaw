"""Approval Router — Software Factory Canon Section 8.

Maps evaluation verdict + touched paths to required gate.
Wraps all gates into a single Ruflo checkpoint record.

S5-01: Ruflo checkpoint contract
  inputs:  evaluation_verdict (PASS/WARN/BLOCK), pack_refs (list[str])
  outputs: approved/rejected, signer (str), timestamp (ISO8601)

S5-02: Approval routing logic
  - PASS + no compliance paths -> auto-approve
  - WARN -> Operator gate
  - BLOCK -> Operator + MLRO gate
  - Any ADR/model/cluster change -> CTIO gate

S5-06: Ruflo checkpoint wrapper
  Aggregates all gate results into single auditable record.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


COMPLIANCE_PATHS = {
    "services/aml/", "services/payment/", "services/recon/",
    "services/kyc/", "compliance/", "services/safeguarding/",
}
ARCHITECTURE_PATHS = {
    "docs/adr/", "decisions/", "INVARIANTS.md",
    "guardian/src/rules/", "litellm/",
}


@dataclass
class GateDecision:
    gate: str  # auto | operator | mlro | ctio
    signer: str
    approved: bool
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    reason: str = ""


@dataclass
class RufloCheckpoint:
    checkpoint_id: str = field(default_factory=lambda: str(uuid4()))
    evaluation_verdict: str = ""  # PASS | WARN | BLOCK
    pack_refs: list = field(default_factory=list)
    gates_required: list = field(default_factory=list)
    gates_completed: list = field(default_factory=list)
    final_verdict: str = "PENDING"  # APPROVED | REJECTED | PENDING
    final_signer: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


def determine_gates(verdict: str, touched_paths: list[str]) -> list[str]:
    """Determine which gates are required based on verdict and paths."""
    gates = []

    if verdict == "PASS":
        # Check if any compliance or architecture paths touched
        compliance = any(any(p.startswith(cp) for cp in COMPLIANCE_PATHS) for p in touched_paths)
        architecture = any(any(p.startswith(ap) for ap in ARCHITECTURE_PATHS) for p in touched_paths)

        if not compliance and not architecture:
            gates.append("auto")
        elif compliance:
            gates.append("operator")
        if architecture:
            gates.append("ctio")
    elif verdict == "WARN":
        gates.append("operator")
    elif verdict == "BLOCK":
        gates.extend(["operator", "mlro"])

    return gates or ["auto"]


def create_checkpoint(verdict: str, touched_paths: list[str], pack_refs: list[str]) -> RufloCheckpoint:
    """Create a Ruflo checkpoint with required gates."""
    gates = determine_gates(verdict, touched_paths)
    return RufloCheckpoint(
        evaluation_verdict=verdict,
        pack_refs=pack_refs,
        gates_required=gates,
    )


def auto_approve(checkpoint: RufloCheckpoint) -> RufloCheckpoint:
    """Auto-approve if only auto gate required."""
    if checkpoint.gates_required == ["auto"]:
        decision = GateDecision(gate="auto", signer="system", approved=True, reason="Auto-approved: PASS + no sensitive paths")
        checkpoint.gates_completed.append(decision.__dict__)
        checkpoint.final_verdict = "APPROVED"
        checkpoint.final_signer = "system"
    return checkpoint


def apply_human_gate(checkpoint: RufloCheckpoint, gate: str, signer: str, approved: bool, reason: str = "") -> RufloCheckpoint:
    """Record a human gate decision."""
    decision = GateDecision(gate=gate, signer=signer, approved=approved, reason=reason)
    checkpoint.gates_completed.append(decision.__dict__)

    # Check if all required gates are completed
    completed_gates = {d["gate"] for d in checkpoint.gates_completed}
    if all(g in completed_gates for g in checkpoint.gates_required):
        all_approved = all(d["approved"] for d in checkpoint.gates_completed)
        checkpoint.final_verdict = "APPROVED" if all_approved else "REJECTED"
        checkpoint.final_signer = signer
    return checkpoint
