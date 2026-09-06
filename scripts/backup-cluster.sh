#!/bin/bash
# BANXE cluster daily backup — rsync mirror of evo1:/data and evo2:/data to Legion D:\.
# Installed at: /home/mmber/bin/backup-cluster.sh (symlink to this file).
# Cron: 0 4 * * * /home/mmber/bin/backup-cluster.sh
set -euo pipefail

LOG=/mnt/d/backups/backup-$(date +%F).log
mkdir -p /mnt/d/backups/evo1 /mnt/d/backups/evo2

{
  echo "=== BANXE Cluster Backup $(date) ==="

  # Адреса берутся из ~/.ssh/config по псевдонимам evo1 и evo2, а не вписываются сюда.
  # Прежняя редакция держала 192.168.0.72 и 192.168.0.15 — оба устарели, и зеркало падало
  # каждые сутки с 4 мая 2026 на `No route to host`. Фактические адреса: evo1 доступен по
  # 100.68.102.48:2222, evo2 по 100.99.208.21:22; 192.168.0.15 не отвечает вовсе. Псевдоним
  # переживает смену адреса, жёстко вписанный адрес — нет.
  #
  # Веса моделей исключены намеренно: из 239 ГБ на evo1 их 217 ГБ, и они воспроизводимы
  # скачиванием. Зеркалить их — значит тратить сутки на то, что и так восстановимо, и прятать
  # незаменимые 22 ГБ внутри объёма, который никто не проверяет.
  EXCL=(--exclude 'ollama-models/' --exclude 'models/' --exclude 'llama-cpp/')

  echo "--- evo1 (псевдоним evo1) ---"
  rsync -a --partial --delete "${EXCL[@]}" -e ssh evo1:/data/ /mnt/d/backups/evo1/

  echo "--- evo2 (псевдоним evo2) ---"
  rsync -a --partial --delete "${EXCL[@]}" -e ssh evo2:/data/ /mnt/d/backups/evo2/

  echo "=== Done $(date) ==="
} | tee -a "$LOG"

# Итог пишется отдельным файлом состояния: журнал, который никто не читает, отказ не сообщает.
# Прежняя редакция падала честно — с set -euo pipefail и записью в журнал, — и именно поэтому
# отказ оставался незамеченным 111 суток подряд.
printf 'ok %s\n' "$(date -Is)" > /mnt/d/backups/LAST-SUCCESS
du -sb /mnt/d/backups/evo1 /mnt/d/backups/evo2 >> /mnt/d/backups/LAST-SUCCESS
