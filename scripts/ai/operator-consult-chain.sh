#!/bin/sh
# Operator-side consultation chain tool (NOT factory self-consult).
# This script is run by OPERATOR in separate consultation window per
# Root Canon §6–7 and factory-terminal-working-mode-v1.md §3.
#
# CONSULT CHAIN (fixed order): Codex → Fable → Mistral → Kimi
# Usage: operator-consult-chain.sh "<brief>"
#        operator-consult-chain.sh --write "<brief>"  (if write needed)
#
# Each consultant is invoked separately; operator reconciles opinions.

set -eu

SBX="read-only"
if [ "${1:-}" = "--write" ]; then
    SBX="workspace-write"
    shift
fi

[ $# -ge 1 ] || {
    echo "usage: operator-consult-chain.sh [--write] \"<brief>\""
    echo ""
    echo "Consult chain order (fixed):"
    echo "  1. Codex   (primary consultant)"
    echo "  2. Fable   (second opinion)"
    echo "  3. Mistral (third opinion)"
    echo "  4. Kimi    (fourth opinion / final escalation)"
    echo ""
    echo "Operator runs each separately and reconciles results."
    exit 2
}

BRIEF="$*"

echo "========================================="
echo "OPERATOR CONSULTATION CHAIN"
echo "========================================="
echo ""
echo "Brief: $BRIEF"
echo ""
echo "CONSULTATION ORDER (fixed):"
echo "  1. Codex   - codex exec --sandbox $SBX \"<brief>\""
echo "  2. Fable   - Run in separate Fable window"
echo "  3. Mistral - Via LiteLLM: mistral-consult"
echo "  4. Kimi    - Via LiteLLM: kimi-consult"
echo ""
echo "Operator reconciles all opinions before returning to Factory."
echo "========================================="
