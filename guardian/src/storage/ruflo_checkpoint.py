"""Ruflo Checkpoint ClickHouse persistence — Sprint 5 S5-07.

Stores Ruflo checkpoint records in banxe_audit.ruflo_checkpoints.
Requires ClickHouse on 127.0.0.1:9000 (via ssh tunnel from Legion).
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from uuid import UUID

try:
    from clickhouse_driver import Client
    CH_OK = True
except ImportError:
    CH_OK = False


DDL = """
CREATE TABLE IF NOT EXISTS banxe_audit.ruflo_checkpoints (
    ts                DateTime64(3, 'UTC'),
    checkpoint_id     UUID,
    evaluation_verdict String,
    pack_refs         Array(String),
    gates_required    Array(String),
    gates_completed   String,
    final_verdict     String,
    final_signer      String
)
ENGINE = ReplacingMergeTree(ts)
PARTITION BY toYYYYMM(ts)
ORDER BY (checkpoint_id, ts)
TTL ts + INTERVAL 7 YEAR DELETE;
"""


def _client():
    return Client(
        host=os.environ.get("CLICKHOUSE_HOST", "127.0.0.1"),
        port=int(os.environ.get("CLICKHOUSE_PORT", "9000")),
        user=os.environ.get("CLICKHOUSE_USER", "default"),
        password=os.environ.get("CLICKHOUSE_PASSWORD", ""),
        database="banxe_audit",
    )


def ensure_table():
    if CH_OK:
        _client().execute(DDL)


def persist(checkpoint) -> bool:
    if not CH_OK:
        return False
    try:
        c = _client()
        c.execute("INSERT INTO banxe_audit.ruflo_checkpoints VALUES", [{
            "ts": datetime.now(timezone.utc),
            "checkpoint_id": UUID(checkpoint.checkpoint_id),
            "evaluation_verdict": checkpoint.evaluation_verdict,
            "pack_refs": checkpoint.pack_refs,
            "gates_required": checkpoint.gates_required,
            "gates_completed": json.dumps(checkpoint.gates_completed),
            "final_verdict": checkpoint.final_verdict,
            "final_signer": checkpoint.final_signer,
        }])
        return True
    except Exception:
        return False
