#!/usr/bin/env bash
# factory_dashboard.sh — ClickHouse queries for factory operational dashboard
# Requires: ssh tunnel to evo1 ClickHouse on 127.0.0.1:9000

set -uo pipefail
CH="clickhouse-client --host 127.0.0.1 --port 9000"

echo "=== FACTORY OPERATIONAL DASHBOARD ==="
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

echo "--- HITL Decisions (last 7 days) ---"
$CH --query "SELECT outcome, count() FROM banxe_audit.hitl_decisions WHERE ts > now() - INTERVAL 7 DAY GROUP BY outcome ORDER BY count() DESC" 2>/dev/null || echo "(query failed — check tunnel)"

echo ""
echo "--- HITL by classifier class (last 7 days) ---"
$CH --query "SELECT JSONExtractString(classifier_out, 'cls') AS cls, count() FROM banxe_audit.hitl_decisions WHERE ts > now() - INTERVAL 7 DAY GROUP BY cls ORDER BY count() DESC" 2>/dev/null || echo "(query failed)"

echo ""
echo "--- Ruflo Checkpoints (last 7 days) ---"
$CH --query "SELECT final_verdict, count() FROM banxe_audit.ruflo_checkpoints WHERE ts > now() - INTERVAL 7 DAY GROUP BY final_verdict" 2>/dev/null || echo "(table may not exist yet — run DDL from ruflo_checkpoint.py)"

echo ""
echo "--- Total audit rows ---"
$CH --query "SELECT 'hitl_decisions' AS tbl, count() FROM banxe_audit.hitl_decisions UNION ALL SELECT 'ruflo_checkpoints', count() FROM banxe_audit.ruflo_checkpoints" 2>/dev/null || echo "(partial — some tables may not exist)"

echo ""
echo "=== END DASHBOARD ==="
