#!/bin/sh
# Factory local Codex executor (INV-03 compliant: local Ollama only, no cloud).
# Usage: factory-codex.sh "<task>"   |   factory-codex.sh --write "<task>"
set -eu
MODEL="qwen2.5-coder:7b-instruct-q4_K_M"
SBX="read-only"
if [ "${1:-}" = "--write" ]; then SBX="workspace-write"; shift; fi
[ $# -ge 1 ] || { echo "usage: factory-codex.sh [--write] \"<task>\""; exit 2; }
exec codex exec --oss --local-provider ollama -m "$MODEL" --sandbox "$SBX" "$*"
