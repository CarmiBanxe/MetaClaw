#!/usr/bin/env bash
# k2-gate-exec-stage3-activate.sh
# Track K / K-2 — gate.exec activation on Legion (ADR-104 §3, F1.5 stage-3, LOW-RISK only)
# Operator action per ADR-103 PART 2. Idempotent. Fail-closed.
set -Eeuo pipefail
IFS=$'\n\t'

log() { printf '[%(%Y-%m-%dT%H:%M:%S%z)T] %s\n' -1 "$*"; }
die() { log "FATAL: $*"; exit 1; }

SERVICE="gate-exec.service"
VAULT_DIR="${VAULT_DIR:-$HOME/.fabric/legion/vault}"
ALLOWLIST="${ALLOWLIST:-$HOME/.fabric/legion/low-risk-allowlist.json}"
CONFIRM_FIFO="${CONFIRM_FIFO:-$HOME/.fabric/legion/.confirm}"
: "${EXEC_REQUEST_TIMEOUT:=15}"
: "${GATE_EXEC_ENABLED:=false}"

log "K-2 activation start (DRY-RUN default: GATE_EXEC_ENABLED=${GATE_EXEC_ENABLED})"

command -v systemctl >/dev/null || die "systemctl not found"
[[ "$(hostname)" == *legion* ]] || log "WARN: host '$(hostname)' is not 'legion' — confirm execution node"

if [[ ! -d "$VAULT_DIR" ]]; then install -d -m 0700 "$VAULT_DIR"; log "Created vault dir $VAULT_DIR (0700)"; else chmod 0700 "$VAULT_DIR"; log "Vault dir exists $VAULT_DIR"; fi

if [[ ! -p "$CONFIRM_FIFO" ]]; then install -d -m 0700 "$(dirname "$CONFIRM_FIFO")"; mkfifo -m 0600 "$CONFIRM_FIFO"; log "Created HITL FIFO $CONFIRM_FIFO"; else log "HITL FIFO exists $CONFIRM_FIFO"; fi

[[ -f "$ALLOWLIST" ]] || die "allow-list missing: $ALLOWLIST (deny-by-default, fail-closed)"
log "Allow-list present: $ALLOWLIST"

ENV_DIR="$HOME/.config/environment.d"
install -d -m 0700 "$ENV_DIR"
cat > "$ENV_DIR/gate-exec.conf" <<EOF
EXEC_REQUEST_TIMEOUT=${EXEC_REQUEST_TIMEOUT}
GATE_EXEC_ENABLED=${GATE_EXEC_ENABLED}
EOF
log "Wrote env: EXEC_REQUEST_TIMEOUT=${EXEC_REQUEST_TIMEOUT} GATE_EXEC_ENABLED=${GATE_EXEC_ENABLED}"

systemctl --user daemon-reload
systemctl --user enable --now "$SERVICE"
log "Enabled+started $SERVICE"

if systemctl --user is-active --quiet "$SERVICE"; then log "VERIFY: $SERVICE is active"; else die "VERIFY FAILED: $SERVICE not active — fail-closed"; fi
log "Recent logs:"; journalctl --user -u "$SERVICE" -n 20 --no-pager || true

log "K-2 done. stage-3 mode: $([[ "$GATE_EXEC_ENABLED" == true ]] && echo EXECUTE || echo DRY-RUN)."
log "Risky classes remain REFUSE in stage-3."
