#!/usr/bin/env bash

count=0

while true; do
  echo "Итерация: $count"
  count=$((count + 1))
  sleep 1

  if [ "$count" -ge 5 ]; then
    echo "Выходим из цикла"
    break
  fi
done

echo "Скрипт завершён"
