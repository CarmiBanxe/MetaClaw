#!/bin/sh
# Operator-side Codex consultation tool (NOT factory self-consult).
# This script is run by OPERATOR in separate consultation window per
# factory-terminal-working-mode-v1.md §3 consult chain (Codex → Fable → Mistral → Kimi).
# Usage: operator-codex-consult.sh "<brief>"   |   operator-codex-consult.sh --write "<brief>"
set -eu
MODEL="qwen2.5-coder:7b-instruct-q4_K_M"
SBX="read-only"
if [ "${1:-}" = "--write" ]; then SBX="workspace-write"; shift; fi
[ $# -ge 1 ] || { echo "usage: operator-codex-consult.sh [--write] \"<brief>\""; exit 2; }
exec codex exec --oss --local-provider ollama -m "$MODEL" --sandbox "$SBX" "$*"
