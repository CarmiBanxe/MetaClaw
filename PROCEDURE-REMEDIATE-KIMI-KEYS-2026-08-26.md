# ПРОЦЕДУРА: Восстановление ключей Kimi (Moonshot)

**Для:** Оператора  
**Цель:** Получить рабочий API ключ для Kimi (moonshot-ai/kimi-k2-0711)  
**Статус:** BLOCKER для полной консультации

---

## ШАГ 1: Проверка существующих ключей

Откройте https://platform.moonshot.cn/console/api-keys

Проверьте статус каждого ключа:

| Ключ | Статус в dashboard | Действие |
|------|-------------------|----------|
| `sk-dBf2QELANFatX1G8ybASFfyXc5GSKr8C9HAWWoaR6WRixrXz` | ? | Если "Disabled" или "Expired" → удалить |
| `sk-uZo57mXOcE26XjMRxxlGUS0HDuj2n1FDGmsQIAthOivtTcit` | ? | Если "Disabled" или "Expired" → удалить |
| `sk-k0y4EN7vOg13OwcjNB3...` | ? | Проверить полный ключ |

---

## ШАГ 2: Создание нового ключа (если старые не работают)

1. В dashboard: **API Keys → Create New Key**
2. Название: `banxe-consultation-2026-08-26`
3. Разрешения: `chat.completions`, `models`
4. Сохраните ключ **сразу** (показывается один раз)

---

## ШАГ 3: Проверка нового ключа

Выполните в терминале:

```bash
export MOONSHOT_API_KEY="sk-ваш-новый-ключ"

# Проверка 1: Список моделей
curl -s https://api.moonshot.cn/v1/models \
  -H "Authorization: Bearer $MOONSHOT_API_KEY" | jq -r '.data[].id'

# Ожидаемый вывод:
# kimi-k2-0711
# kimi-k1.5
# и др.
```

```bash
# Проверка 2: Тестовый запрос
curl -s https://api.moonshot.cn/v1/chat/completions \
  -H "Authorization: Bearer $MOONSHOT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k2-0711",
    "messages": [{"role": "user", "content": "OK"}]
  }' | jq -r '.choices[0].message.content'

# Ожидаемый вывод: "OK" или похожий ответ
```

---

## ШАГ 4: Передача ключа BEN

Если обе проверки прошли:

```bash
# В Claude Code терминале (с префиксом !)
! export MOONSHOT_API_KEY="sk-ваш-новый-ключ"
```

Или сообщите мне: **"Ключ готов: sk-..."** (первые 10 символов достаточно для идентификации).

---

## ДИАГНОСТИКА ОШИБОК

| Ошибка | Причина | Решение |
|--------|---------|---------|
| `Invalid Authentication` | Ключ неактивен / удален | Создать новый ключ |
| `Insufficient Balance` | Закончился баланс | Пополнить в billing |
| `Rate limit exceeded` | Превышен лимит | Подождать 1 минуту |
| `Model not found` | Неправильное имя модели | Использовать `kimi-k2-0711` |

---

## АЛЬТЕРНАТИВА: OpenRouter

Если Moonshot недоступен:

1. https://openrouter.ai/keys
2. Create Key → название `banxe-kimi`
3. Проверка:
```bash
export OPENROUTER_API_KEY="sk-or-v1-..."
curl -s https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moonshot-ai/kimi-k2-0711",
    "messages": [{"role": "user", "content": "OK"}]
  }'
```

---

**BEN ожидает:** Подтверждение готовности ключа для запуска Kimi как третьего консультанта.
