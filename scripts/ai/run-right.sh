#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/fcc-env-right.sh"
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
