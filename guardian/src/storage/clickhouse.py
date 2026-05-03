"""Synchronous ClickHouse audit-event sink (A.3.2 minimal slice).

Failures are swallowed and reported through the (ok, error) tuple so the API can still
return the verdict with storage_status.written=false per ADR-019 §6.5 (audit trail must
be best-effort for the response cycle; a permanent loss is a separate Daily Verify Drill).
"""

from __future__ import annotations

import logging
import os
from datetime import datetime
from typing import Any

logger = logging.getLogger(__name__)

BACKEND = "clickhouse"


class ClickHouseAuditStore:
    BACKEND = BACKEND

    def __init__(self) -> None:
        self.host = os.getenv("GUARDIAN_CH_HOST", "127.0.0.1")
        self.port = int(os.getenv("GUARDIAN_CH_PORT", "8123"))
        self.database = os.getenv("GUARDIAN_CH_DATABASE", "default")
        self.user = os.getenv("GUARDIAN_CH_USER", "default")
        self.password = os.getenv("GUARDIAN_CH_PASSWORD", "")
        self.table = os.getenv("GUARDIAN_CH_TABLE", "guardian_audit_events")

    def write(self, event: dict[str, Any]) -> tuple[bool, str | None]:
        try:
            import clickhouse_connect
        except ImportError as exc:
            logger.warning("clickhouse-connect not installed: %s", exc)
            return False, f"clickhouse-connect not installed: {exc}"

        try:
            client = clickhouse_connect.get_client(
                host=self.host,
                port=self.port,
                database=self.database,
                username=self.user,
                password=self.password,
            )
            try:
                column_names = list(event.keys())
                row = [_normalise(event[c]) for c in column_names]
                client.insert(self.table, [row], column_names=column_names)
            finally:
                client.close()
            return True, None
        except Exception as exc:  # noqa: BLE001 - storage must never raise into the API path
            logger.warning("clickhouse insert failed: %s", exc)
            return False, str(exc)


def _normalise(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.replace(tzinfo=None)
    return value
