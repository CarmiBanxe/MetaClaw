Полный стек: Manus-агент на Legion → Telegram-бот
Архитектура системы

text
Legion (локально)
├── llama-server :8080  ← Qwen3.6-35B-A3B IQ2_M (мозг агента)
├── OpenManus (FastAPI) :8000  ← агентный движок
├── Telegram Bot (polling) ← интерфейс
└── ngrok/cloudflared  ← туннель в интернет (только для webhook)

Блок 1: llama-server уже готов (из предыдущего шага)
Убедись что сервер запускается и отвечает:

bash
# Тест API
curl http://localhost:8080/v1/models
# Должен вернуть JSON с именем модели

Блок 2: Установка OpenManus
Шаг 2.1 — Установка uv и клонирование

bash
# Установить uv (быстрый менеджер пакетов Python)
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc  # или ~/.zshrc

# Клонировать OpenManus
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus

# Создать виртуальное окружение Python 3.12
uv venv --python 3.12
source .venv/bin/activate
Шаг 2.2 — Установка зависимостей

bash
uv pip install -r requirements.txt
OpenManus включает в себя: fastapi, playwright, browser-use, googlesearch-python, duckduckgo_search, docker, mcp, beautifulsoup4 и другие .
Шаг 2.3 — Playwright (браузер для агента)

bash
playwright install chromium
Это необходимо для работы инструмента browser_use_tool — агент сможет открывать сайты, кликать, заполнять формы .

Блок 3: Конфигурация OpenManus под твой llama-server
Шаг 3.1 — Создать config.toml

bash
cp config/config.example.toml config/config.toml
Шаг 3.2 — Настройка под Qwen3.6-35B + Gemma-4-12B

text
# config/config.toml

[llm]
api_type = 'openai'
model = "Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive-IQ2_M"
base_url = "http://localhost:8080/v1"
api_key = "none"
max_tokens = 8192
temperature = 0.6
top_p = 0.95

[llm.vision]
api_type = 'openai'
model = "Huihui-gemma-4-12B-it-abliterated"
base_url = "http://localhost:8081/v1"
api_key = "none"
max_tokens = 4096
temperature = 0.6
Это официальный шаблон конфигурации для Ollama-совместимых endpoint'ов , адаптированный под твой llama-server.
Шаг 3.3 — Тест агента в терминале

bash
cd ~/OpenManus
source .venv/bin/activate
python main.py
# Введи: "Find the current Bitcoin price and save it to a file"
Агент должен: поискать → открыть браузер → сохранить файл в workspace/ . Если отвечает — всё работает.

Блок 4: Превратить OpenManus в REST API
Официального HTTP API у OpenManus нет из коробки, но существует задокументированный паттерн через FastAPI . Создаём два файла:
Шаг 4.1 — app/service/__init__.py

bash
mkdir -p ~/OpenManus/app/service
touch ~/OpenManus/app/service/__init__.py
Шаг 4.2 — app/service/agent_runner.py

python
# app/service/agent_runner.py
from app.agent.manus import Manus
from app.logger import logger

async def process_prompt(prompt: str) -> str:
    agent = await Manus.create()
    try:
        logger.info(f"Agent prompt: {prompt}")
        result = await agent.run(prompt)
        return result
    finally:
        await agent.cleanup()
Шаг 4.3 — api_server.py (в корне OpenManus)

python
# api_server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.service.agent_runner import process_prompt
import uvicorn

app = FastAPI(title="OpenManus API")

class PromptInput(BaseModel):
    prompt: str

@app.post("/run/agent")
async def run_agent(input: PromptInput):
    if not input.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is empty")
    result = await process_prompt(input.prompt)
    return {"status": "ok", "result": result}

@app.get("/health")
async def health():
    return {"status": "running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
Шаг 4.4 — Запуск API-сервера

bash
cd ~/OpenManus
source .venv/bin/activate
export PYTHONPATH=$(pwd)
python api_server.py
Проверка:

bash
curl -X POST http://localhost:8000/run/agent \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is 2+2? Answer in one word."}'

Блок 5: Telegram-бот
Шаг 5.1 — Создать бота в Telegram
	1.	Открой @BotFather в Telegram
	2.	Отправь /newbot
	3.	Дай имя и username боту
	4.	Скопируй токен вида 7123456789:AAF...
Шаг 5.2 — Установить библиотеку

bash
pip install python-telegram-bot==21.0 httpx
Шаг 5.3 — telegram_bot.py

python
# telegram_bot.py
import asyncio
import httpx
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters

TELEGRAM_TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"
AGENT_API_URL = "http://localhost:8000/run/agent"

async def start(update: Update, context):
    await update.message.reply_text(
        "🤖 Manus-агент активен. Отправь мне задачу — я выполню её локально на Legion."
    )

async def handle_message(update: Update, context):
    user_msg = update.message.text
    await update.message.reply_text("⏳ Выполняю задачу...")

    try:
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                AGENT_API_URL,
                json={"prompt": user_msg}
            )
            data = response.json()
            result = data.get("result", "Нет ответа")
    except Exception as e:
        result = f"❌ Ошибка: {str(e)}"

    # Telegram ограничивает сообщения 4096 символами
    if len(result) > 4000:
        result = result[:4000] + "\n... [обрезано]"

    await update.message.reply_text(f"✅ Результат:\n\n{result}")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен (polling режим)...")
    app.run_polling()  # polling — не требует публичного IP

if __name__ == "__main__":
    main()
Режим polling — бот сам опрашивает Telegram каждые несколько секунд, не требует публичного IP и SSL . Это оптимальный вариант для локального Legion.
Шаг 5.4 — Запуск бота

bash
# В отдельном терминале
source ~/OpenManus/.venv/bin/activate
python ~/telegram_bot.py

Блок 6: Автозапуск через systemd
Чтобы всё поднималось само при старте Legion :
Шаг 6.1 — Сервис для llama-server

bash
sudo nano /etc/systemd/system/llama-qwen.service

text
[Unit]
Description=llama-server Qwen3.6-35B-A3B
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME
ExecStart=/home/YOUR_USERNAME/llama.cpp/llama-server \
  -m /home/YOUR_USERNAME/models/qwen36-35b-aggressive/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive-IQ2_M.gguf \
  --mmproj /home/YOUR_USERNAME/models/qwen36-35b-aggressive/mmproj-Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive-f16.gguf \
  --jinja -c 131072 -ngl 20 --flash-attn \
  --cache-type-k q8_0 --cache-type-v q8_0 \
  --host 0.0.0.0 --port 8080
Restart=always

[Install]
WantedBy=multi-user.target
Шаг 6.2 — Сервис для OpenManus API

bash
sudo nano /etc/systemd/system/openmanus-api.service

text
[Unit]
Description=OpenManus Agent API
After=llama-qwen.service
Requires=llama-qwen.service

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME/OpenManus
Environment=PYTHONPATH=/home/YOUR_USERNAME/OpenManus
ExecStart=/home/YOUR_USERNAME/OpenManus/.venv/bin/python api_server.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
Шаг 6.3 — Активация всех сервисов

bash
sudo systemctl daemon-reload
sudo systemctl enable llama-qwen.service openmanus-api.service
sudo systemctl start llama-qwen.service
sleep 30  # дать модели время загрузиться
sudo systemctl start openmanus-api.service

Итоговая схема запуска всего стека

text
Порядок запуска:
1. llama-server :8080  (30-60 сек загрузка модели)
2. api_server.py :8000  (OpenManus REST API)
3. telegram_bot.py     (polling, без публичного IP)

Ты пишешь в Telegram боту:
"Сделай анализ файла payments.csv и найди аномалии"

Бот → POST /run/agent → OpenManus →
  └─ planning tool: составить план
  └─ python_execute: прочитать CSV, найти аномалии
  └─ file_saver: сохранить отчёт в workspace/
  └─ → результат в Telegram
Инструменты, которые агент использует автоматически :
	•	bash.py — выполнение shell-команд
	•	browser_use_tool.py — веб-браузер (Playwright Chromium)
	•	python_execute.py — запуск Python-кода
	•	google_search.py / duckduckgo_search — поиск в интернете
	•	file_saver.py — сохранение файлов в workspace/
	•	str_replace_editor.py — редактирование файлов
	•	planning.py — планирование многошаговых задач
Подготовлено Deep Research



Это даст возможность выхода в интернет и поиска по интернету?





Да — но с важными нюансами. Отвечу по фактам без дополнительных поисков, т.к. всё уже подтверждено в нашем исследовании.

Выход в интернет: что умеет и чего не умеет стек
✅ Что работает из коробки
OpenManus включает инструменты :
	•	google_search — поиск через Google Search API (нужен бесплатный API-ключ от SerpAPI или Serper.dev)
	•	duckduckgo_search — поиск без ключей, полностью бесплатно
	•	browser_use_tool — Playwright Chromium, полноценный браузер: открывает страницы, кликает, скроллит, читает контент, заполняет формы, делает скриншоты
	•	web_search — общий враппер над поисковиками
Это значит: агент может самостоятельно искать информацию, переходить по ссылкам, читать страницы и возвращать тебе результат .

⚠️ Что требует настройки
DuckDuckGo — работает сразу, без ключей. Но иногда блокирует при частых запросах .
Google Search — нужен API-ключ. В config.toml:

text
[search]
engine = "google"  # или "duckduckgo"
google_api_key = "ВАШ_КЛЮЧ"
google_cse_id = "ВАШ_CSE_ID"
Бесплатный лимит Google Custom Search API — 100 запросов/день .

❌ Чего стек НЕ делает
	•	Не индексирует интернет сам — использует готовые поисковики
	•	Браузер работает headless (без GUI) — но это норма для сервера
	•	Сайты с Cloudflare-защитой и CAPTCHA могут блокировать Playwright

Практический пример
Ты пишешь боту:

text
Найди последние новости о банковских регуляциях ЕС за эту неделю
и сделай краткое резюме
Агент автоматически:
	1.	duckduckgo_search("EU banking regulations 2026 latest news")
	2.	browser_use_tool → открывает топ-3 ссылки, читает контент
	3.	Суммирует и возвращает тебе в Telegram
Всё это происходит локально на Legion, данные никуда не уходят.
Подготовлено Deep Research


А в телеграмм Боте?





Да, полностью — бот в Telegram будет иметь тот же функционал, что и агент напрямую.

Как это работает через Telegram
Вся цепочка прозрачна :

text
Ты в Telegram → пишешь задачу
      ↓
telegram_bot.py (polling) получает сообщение
      ↓
POST → http://localhost:8000/run/agent (OpenManus API)
      ↓
OpenManus запускает агента с полным набором инструментов:
  ├── duckduckgo_search → поиск в интернете ✅
  ├── browser_use_tool  → открывает сайты ✅
  ├── python_execute    → запускает код ✅
  ├── bash              → shell-команды ✅
  └── file_saver        → сохраняет файлы ✅
      ↓
Результат → обратно в Telegram
Telegram-бот — это просто интерфейс. Агент внутри получает те же права и инструменты, что при запуске из терминала .

Единственные ограничения Telegram
	•	Длина сообщения: максимум 4096 символов — длинные отчёты обрезаются. Решение: агент сохраняет в файл, бот присылает путь
	•	Таймаут: бот ждёт ответа до 300 секунд (уже настроено в коде timeout=300.0). Если агент работает дольше — нужно разбивать задачу
	•	Файлы: бот может присылать файлы через send_document() — легко добавить в код
Всё остальное — выход в интернет, поиск, браузер, код — работает в Telegram точно так же как в терминале .
Подготовлено Deep Research


какие опции для осуществления всех этих функций есть кроме телеграмма ,что не обрезает сообщение,что лучше ?

Завершено 2 шага

Есть чёткая картина по всем альтернативам. Сравниваю по делу.

Альтернативы Telegram для Manus-стека на Legion
Что не так с Telegram
Telegram обрезает сообщения на 4096 символах , не рендерит таблицы и код нативно, и требует polling-соединения. Для агентных задач с длинными ответами это реальное ограничение.

Топ-3 альтернативы для твоего стека
🥇 Open WebUI — лучший выбор для Legion
Напрямую подключается к llama-server через OpenAI-совместимый API . Есть активная дискуссия по интеграции OpenManus в Open WebUI .
Установка за 1 команду:

bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:8080/v1 \
  -e OPENAI_API_KEY=none \
  -v open-webui:/app/backend/data \
  --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:main
После этого открываешь http://localhost:3000 .
Что даёт:
	•	Неограниченная длина ответов с полным Markdown/LaTeX рендерингом
	•	Встроенный веб-поиск, RAG по документам, генерация изображений
	•	Голосовой ввод/вывод (TTS/STT)
	•	Артефакты — сохраняет файлы прямо в интерфейсе
	•	Работает в браузере на любом устройстве в локальной сети

🥈 LibreChat — лучший для команды / MCP-агентов
Поддерживает нативный Agent Builder UI и MCP-инструменты . Это ближе всего к Manus-концепции по функционалу.

bash
git clone https://github.com/danny-avila/LibreChat.git
cd LibreChat
cp .env.example .env
# В .env указать: OPENAI_API_BASE_URL=http://localhost:8080/v1
docker-compose up -d
Открываешь http://localhost:3080 .
Что даёт:
	•	Полный Agent Builder: создаёшь агентов с инструментами визуально
	•	MCP-совместимость — прямая интеграция с OpenManus через MCP
	•	Разветвление диалогов (conversation forking)
	•	Выполнение кода прямо в интерфейсе

🥉 AnythingLLM — простейший старт без Docker
Desktop-приложение, скачивается как .AppImageна Linux .

bash
wget https://releases.useanythingllm.com/latest/linux/AnythingLLMDesktop.AppImage
chmod +x AnythingLLMDesktop.AppImage
./AnythingLLMDesktop.AppImage
Подключаешь llama-server: Settings → LLM Provider → Generic OpenAI → http://localhost:8080/v1 .

Сравнительная таблица

	Telegram	Open WebUI	LibreChat	AnythingLLM
Длина ответа	❌ 4096 символов	✅ Неограничено	✅ Неограничено	✅ Неограничено
Markdown / код	⚠️ Частично	✅ Полный	✅ Полный	✅ Полный
Мобильный доступ	✅ Нативный	✅ Браузер	✅ Браузер	❌ Desktop only
OpenManus интеграция	✅ Через API	✅ Через API	✅ MCP нативно	✅ Через API
Голос	❌ Нет	✅ TTS/STT	❌ Ограниченно	❌ Нет
RAG по документам	❌ Нет	✅ Встроено	✅ Встроено	✅ Фокус
Доступ вне дома	✅ Везде	⚠️ Нужен туннель	⚠️ Нужен туннель	❌ Локально
Установка	Простая	Docker (1 команда)	Docker	AppImage
Рекомендация
Для тебя оптимально — комбинация:
	•	Open WebUI для работы дома за ноутом — полный функционал, нет ограничений
	•	Telegram оставить для доступа на ходу с телефона — быстрые короткие задачи
Это не «или/или», а два интерфейса к одному и тому же llama-server + OpenManus API. Оба работают параллельно.
Подготовлено Deep Research



А если не рассматривать легион как основной терминал общения с оператором а речт идет еще и о пользовании мобильным телефоном.Как телеграм,только лучше .каким ресурсом нужно воспользоваться,что скачать,как установить?


Завершено 2 шага

Теперь полная картина. Есть два чётких варианта в зависимости от телефона.

Мобильный доступ к Legion: что скачать и как настроить
Главная проблема: Legion локален, телефон снаружи
Чтобы телефон подключился к Legion не только дома, нужен туннель. Без него — только в домашней Wi-Fi сети.

Вариант A: iPhone / iPad → Enchanted LLM (лучший вариант для iOS)
Бесплатное нативное приложение, open-source, ChatGPT-подобный интерфейс, полный Markdown, код, таблицы. Без обрезки сообщений .
Скачать:
	•	App Store → поиск "Enchanted LLM" → установить (бесплатно)
	•	Прямая ссылка: apps.apple.com → ID 6474268307
	•	Требует iOS 17.0+
Настройка в приложении:
	1.	Открыть Enchanted → Settings → Server URL
	2.	Ввести адрес Legion (см. туннель ниже)
	3.	Готово — выбираешь модель и работаешь

Вариант B: Android → Open Mobile UI(официальный клиент Open WebUI)
Native Android-приложение на React Native, полная совместимость с Open WebUI .
Скачать:
	•	Google Play → поиск "Open Mobile UI" → установить
	•	Обновлялся апрель 2026
Настройка:
	1.	Открыть приложение → Enter your Open WebUI URL
	2.	Ввести адрес туннеля (см. ниже)
	3.	Войти через email/пароль Open WebUI

Туннель: как подключиться из интернета к Legion
Без этого — только дома по Wi-Fi. Есть два способа:
Способ 1 — Cloudflare Tunnel (бесплатно, постоянный URL)

bash
# Установить cloudflared на Legion
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb

# Авторизоваться (нужен бесплатный аккаунт cloudflare.com)
cloudflared tunnel login

# Создать туннель к llama-server
cloudflared tunnel --url http://localhost:8080
# Получишь URL вида: https://xxx-yyy.trycloudflare.com
Этот URL вводишь в Enchanted / Open Mobile UI вместо localhost .
Способ 2 — ngrok (проще, URL меняется при перезапуске на бесплатном плане)

bash
# Установить
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc
sudo apt install ngrok

# Запустить туннель
ngrok http 8080
# Получишь URL вида: https://b377-82-132-216-51.ngrok-free.app
Это именно тот способ, что официально рекомендован в документации Enchanted .

Итоговая схема для тебя

text
Legion (дома)
├── llama-server :8080
├── Open WebUI :3000
└── cloudflared → https://твой-туннель.trycloudflare.com

iPhone (везде)
└── Enchanted LLM → https://твой-туннель.trycloudflare.com

Android (везде)
└── Open Mobile UI → https://твой-туннель.trycloudflare.com

	Telegram	Enchanted (iOS)	Open Mobile UI (Android)
Обрезка сообщений	❌ 4096 символов	✅ Нет	✅ Нет
Markdown / код	⚠️ Частично	✅ Полный	✅ Полный
Доступ вне дома	✅ Всегда	✅ Через туннель	✅ Через туннель
Агентные задачи	✅ Через API	⚠️ Только чат с LLM	✅ Через Open WebUI
Цена	Бесплатно	Бесплатно	Бесплатно
Рекомендация: Cloudflare Tunnel + Enchanted (iOS) или Open Mobile UI (Android) — это «Telegram, только лучше» для твоего стека. Telegram оставь как резерв для быстрых задач через агента.
Подготовлено Deep Research



