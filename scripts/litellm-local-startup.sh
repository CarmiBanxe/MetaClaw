#!/usr/bin/env bash
# litellm-local-startup.sh — FU-2 Phase 4
# Cold-start the LiteLLM LAN gateway and verify its health.
#
# Usage:
#   scripts/litellm-local-startup.sh [--mode compose|systemd] [--no-start] [--profile db]
#
#   --mode compose   (default) bring the gateway up via litellm/docker-compose.yml
#   --mode systemd   start/restart the existing litellm-lan-gateway user unit instead
#   --no-start       skip starting; only run the healthcheck against a running gateway
#   --profile db     (compose mode) also start the optional Postgres service
#
# Secrets are loaded from litellm/.env (copy litellm/.env.example first).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LITELLM_DIR="${REPO_ROOT}/litellm"
ENV_FILE="${LITELLM_DIR}/.env"

MODE="compose"
START=1
COMPOSE_PROFILE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode) MODE="${2:?}"; shift 2 ;;
    --no-start) START=0; shift ;;
    --profile) COMPOSE_PROFILE="$2"; shift 2 ;;
    -h|--help) grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

# --- Load env --------------------------------------------------------------
if [[ -f "${ENV_FILE}" ]]; then
  set -a; # shellcheck disable=SC1090
  source "${ENV_FILE}"; set +a
  echo "[startup] loaded env from ${ENV_FILE}"
else
  echo "[startup] WARN: ${ENV_FILE} not found — copy litellm/.env.example and fill it." >&2
fi

HOST="${LITELLM_HOST:-127.0.0.1}"
[[ "${HOST}" == "0.0.0.0" ]] && HOST="127.0.0.1"  # connect locally even if bound wide
PORT="${LITELLM_PORT:-4000}"
BASE="http://${HOST}:${PORT}"

# --- Start -----------------------------------------------------------------
if [[ "${START}" -eq 1 ]]; then
  case "${MODE}" in
    compose)
      echo "[startup] starting gateway via docker compose (${LITELLM_DIR})"
      profile_args=()
      [[ -n "${COMPOSE_PROFILE}" ]] && profile_args=(--profile "${COMPOSE_PROFILE}")
      docker compose -f "${LITELLM_DIR}/docker-compose.yml" "${profile_args[@]}" up -d
      ;;
    systemd)
      echo "[startup] (re)starting systemd user unit litellm-lan-gateway"
      systemctl --user restart litellm-lan-gateway.service 2>/dev/null \
        || systemctl --user restart litellm-v2.service
      ;;
    *) echo "unknown --mode: ${MODE}" >&2; exit 2 ;;
  esac
fi

# --- Healthcheck -----------------------------------------------------------
echo "[startup] waiting for ${BASE}/health/liveliness ..."
for _ in $(seq 1 30); do
  if curl -fsS -m 5 -o /dev/null "${BASE}/health/liveliness" 2>/dev/null; then
    break
  fi
  sleep 2
done

if ! curl -fsS -m 5 -o /dev/null "${BASE}/health/liveliness" 2>/dev/null; then
  echo "[startup] FAIL: gateway not live at ${BASE}/health/liveliness" >&2
  exit 1
fi
echo "[startup] OK: liveliness 200"

# Authenticated model list (the canonical readiness probe).
if [[ -n "${LITELLM_MASTER_KEY:-}" ]]; then
  code="$(curl -fsS -m 10 -o /dev/null -w '%{http_code}' \
    -H "Authorization: Bearer ${LITELLM_MASTER_KEY}" \
    "${BASE}/v1/models" || true)"
  if [[ "${code}" == "200" ]]; then
    echo "[startup] OK: /v1/models 200 (auth)"
  else
    echo "[startup] WARN: /v1/models returned ${code} — check LITELLM_MASTER_KEY" >&2
  fi
else
  echo "[startup] NOTE: LITELLM_MASTER_KEY unset — skipping authenticated /v1/models probe"
fi

echo "[startup] gateway healthy at ${BASE}"
