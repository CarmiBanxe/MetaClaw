"""Smoke test for MemoryLoader (ADR-020 contract)."""

from __future__ import annotations

from src.memory_loader import MemoryLoader


def test_load_all_returns_8_keys_and_does_not_crash() -> None:
    snap = MemoryLoader().load_all()
    expected_keys = {
        "memory",
        "ledger",
        "gap_register",
        "canon",
        "hitl",
        "constitution",
        "adrs",
        "roadmap",
    }
    assert set(snap.keys()) == expected_keys
    assert isinstance(snap["adrs"], list)
    for k in expected_keys - {"adrs"}:
        assert isinstance(snap[k], str)
