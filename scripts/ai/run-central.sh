#!/usr/bin/env bash
set -euo pipefail
export BANXE_TERMINAL_ROLE="central"
export ANTHROPIC_BASE_URL="http://127.0.0.1:8082"
export ANTHROPIC_AUTH_TOKEN="freecc"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
export CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT="1"
export CLAUDE_CODE_AUTO_COMPACT_WINDOW="190000"
unset ANTHROPIC_API_KEY || true
if command -v fcc-claude >/dev/null 2>&1; then
  exec fcc-claude
elif command -v claude >/dev/null 2>&1; then
  exec claude
elif command -v claude-code >/dev/null 2>&1; then
  exec claude-code
else
  echo "No Claude launcher found: fcc-claude / claude / claude-code" >&2
  exit 1
fi
