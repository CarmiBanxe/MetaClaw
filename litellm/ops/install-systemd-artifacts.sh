#!/usr/bin/env bash
# install-systemd-artifacts.sh — copies the REVIEWED unit into place and
# prints the exact next commands. It NEVER runs daemon-reload/enable/start.
# Usage:
#   ./install-systemd-artifacts.sh          # user mode (default, no root)
#   ./install-systemd-artifacts.sh --system # system mode: prints sudo commands only
set -eu
OPS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UNIT_SRC="$OPS_DIR/litellm-director.service"
ENV_FILE="$OPS_DIR/litellm-director.env"
MODE="${1:-sigil-user}"

[ -f "$UNIT_SRC" ] || { echo "unit template missing: $UNIT_SRC"; exit 1; }
chmod +x "$OPS_DIR/check-litellm-director.sh" 2>/dev/null || true
[ -f "$ENV_FILE" ] && chmod 600 "$ENV_FILE"

if [ "$MODE" = "--system" ]; then
  # System mode: root-owned paths — commands are PRINTED, not executed.
  echo "System-mode install (run these yourself after review):"
  echo "  sudo cp $UNIT_SRC /etc/systemd/system/litellm-director.service"
  echo "  #   then edit it: replace %h with the absolute home dir, add User=<user>"
  echo "  sudo systemctl daemon-reload"
  echo "  sudo systemctl enable litellm-director   # autostart on boot"
  echo "  sudo systemctl start  litellm-director   # start now"
  echo "  sudo systemctl status litellm-director"
  exit 0
fi

# User mode (default, preferred: no root needed).
DEST="$HOME/.config/systemd/user"
mkdir -p "$DEST"
cp "$UNIT_SRC" "$DEST/litellm-director.service"
echo "Installed: $DEST/litellm-director.service"
echo
echo "Next commands (run yourself, in order, after reviewing the unit):"
echo "  systemctl --user daemon-reload"
echo "  systemctl --user enable litellm-director    # autostart at login"
echo "  loginctl enable-linger $USER                # autostart at BOOT without login"
echo "  systemctl --user start litellm-director     # start now"
echo "  systemctl --user status litellm-director"
echo
echo "Nothing was reloaded/enabled/started by this script."
