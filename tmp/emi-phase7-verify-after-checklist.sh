#!/usr/bin/env bash
set -euo pipefail

# Быстрая проверка после выполнения операторского чек-листа EMI Phase 7/8

echo "[EMI Phase 7/8] Запускаю аудит operator-done..."
claude -p "$(cat /tmp/audit-emi-phase7-operator-done.prompt)"

echo
echo "[EMI Phase 7/8] При необходимости можно повторить loop-аудит:"
echo "  claude -p \"\$(cat /tmp/audit-emi-phase7-loop-check.prompt)\""
