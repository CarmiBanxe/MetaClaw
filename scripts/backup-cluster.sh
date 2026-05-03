#!/bin/bash
# BANXE cluster daily backup — rsync mirror of evo1:/data and evo2:/data to Legion D:\.
# Installed at: /home/mmber/bin/backup-cluster.sh (symlink to this file).
# Cron: 0 4 * * * /home/mmber/bin/backup-cluster.sh
set -euo pipefail

LOG=/mnt/d/backups/backup-$(date +%F).log
mkdir -p /mnt/d/backups/evo1 /mnt/d/backups/evo2

{
  echo "=== BANXE Cluster Backup $(date) ==="

  echo "--- evo1 (banxe@192.168.0.72:2222) ---"
  rsync -av --partial --delete -e 'ssh -p 2222' \
    banxe@192.168.0.72:/data/ /mnt/d/backups/evo1/ 2>&1 | tail -5

  echo "--- evo2 (moriel-carmi@192.168.0.15:22) ---"
  rsync -av --partial --delete -e 'ssh' \
    moriel-carmi@192.168.0.15:/data/ /mnt/d/backups/evo2/ 2>&1 | tail -5

  echo "=== Done $(date) ==="
} | tee -a "$LOG"
