#!/usr/bin/env bash
# check-litellm-director.sh — read-only verification of the LiteLLM director.
# Prints PASS/WARN/FAIL lines. No destructive actions. Exit 1 only on FAIL.
set -u
OPS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$OPS_DIR/litellm-director.env"
UNIT_TEMPLATE="$OPS_DIR/litellm-director.service"
UNIT_INSTALLED="$HOME/.config/systemd/user/litellm-director.service"

LITELLM_CONFIG="$OPS_DIR/../litellm-config.v2.yaml"
LITELLM_HOST=127.0.0.1
LITELLM_PORT=8000
LITELLM_MASTER_KEY=""
[ -f "$ENV_FILE" ] && . "$ENV_FILE"

FAILS=0; WARNS=0
pass() { echo "PASS  $*"; }
warn() { echo "WARN  $*"; WARNS=$((WARNS+1)); }
fail() { echo "FAIL  $*"; FAILS=$((FAILS+1)); }

http_code() {
  local c
  c=$(curl -s -o /dev/null -w '%{http_code}' --max-time 5 "$@" 2>/dev/null) || true
  echo "${c:-000}"
}

# 1. files
[ -f "$LITELLM_CONFIG" ] && pass "config exists: $LITELLM_CONFIG" \
                         || fail "config missing: $LITELLM_CONFIG"
[ -f "$UNIT_TEMPLATE" ]  && pass "unit template exists: $UNIT_TEMPLATE" \
                         || fail "unit template missing: $UNIT_TEMPLATE"
[ -f "$UNIT_INSTALLED" ] && pass "unit installed: $UNIT_INSTALLED" \
                         || warn "unit not installed yet (expected before install step)"
if [ -f "$ENV_FILE" ]; then
  grep -q CHANGE_ME "$ENV_FILE" && warn "env file still has CHANGE_ME placeholders" \
                                || pass "env file has no placeholders"
else
  warn "env file missing: $ENV_FILE"
fi

BASE="http://$LITELLM_HOST:$LITELLM_PORT"
AUTH=()
[ -n "$LITELLM_MASTER_KEY" ] && [ "$LITELLM_MASTER_KEY" != "CHANGE_ME" ] \
  && AUTH=(-H "Authorization: Bearer $LITELLM_MASTER_KEY")

# 2. base endpoint on :8000 (any HTTP status = process is answering)
CODE=$(http_code "$BASE/")
if [ "$CODE" = "000" ]; then
  fail "no HTTP response on $BASE (director not listening)"
else
  pass "HTTP responds on $BASE (status $CODE)"
fi

# 3. health endpoints (liveliness is unauthenticated in litellm)
CODE=$(http_code "$BASE/health/liveliness")
case "$CODE" in
  200) pass "/health/liveliness OK" ;;
  000) warn "/health/liveliness no response" ;;
  *)   warn "/health/liveliness status $CODE" ;;
esac
CODE=$(http_code "${AUTH[@]}" "$BASE/health")
case "$CODE" in
  200) pass "/health OK" ;;
  401|403) warn "/health requires valid master key (status $CODE)" ;;
  000) warn "/health no response" ;;
  *)   warn "/health status $CODE" ;;
esac

# 4. tools/models endpoint, safe read-only probe
CODE=$(http_code "${AUTH[@]}" "$BASE/v1/models")
case "$CODE" in
  200) pass "/v1/models OK (tools surface reachable)" ;;
  401|403) warn "/v1/models auth-gated (status $CODE) — endpoint alive" ;;
  000) warn "/v1/models no response" ;;
  *)   warn "/v1/models status $CODE" ;;
esac

echo "----"
echo "SUMMARY: fails=$FAILS warns=$WARNS"
[ "$FAILS" -eq 0 ] || exit 1
