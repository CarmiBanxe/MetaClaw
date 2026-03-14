<div align="center">

<img src="new_logo.png" alt="MetaClaw" width="600">

<br/>

# Просто разговаривайте с вашим агентом, и он будет учиться и *ЭВОЛЮЦИОНИРОВАТЬ*.

<p>Вдохновлено тем, как учится мозг. Мета-обучение и эволюция вашего 🦞 в каждом реальном диалоге. GPU не требуется. Поддерживает Kimi, Qwen, Claude, MiniMax и другие.</p>

⚡ Supported LLM Providers & Platforms

<table>
<tr>
<td align="center" width="100">
  <a href="https://kimi.ai">
    <img src="https://github.com/MoonshotAI.png?size=200" width="48" height="48" alt="Kimi" />
  </a><br/>
  <sub><a href="https://kimi.ai"><b>Kimi</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://qwen.ai">
    <img src="https://github.com/QwenLM.png?size=200" width="48" height="48" alt="Qwen" />
  </a><br/>
  <sub><a href="https://qwen.ai"><b>Qwen</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://www.anthropic.com/claude">
    <img src="https://cdn.simpleicons.org/claude/D97757" width="48" height="48" alt="Claude" />
  </a><br/>
  <sub><a href="https://www.anthropic.com/claude"><b>Claude</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://www.minimax.io">
    <img src="https://github.com/minimax-ai.png?size=200" width="48" height="48" alt="MiniMax" />
  </a><br/>
  <sub><a href="https://www.minimax.io"><b>MiniMax</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://openai.com">
    <img src="https://github.com/openai.png?size=200" width="48" height="48" alt="OpenAI" />
  </a><br/>
  <sub><a href="https://openai.com"><b>OpenAI</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://gemini.google.com">
    <img src="https://cdn.simpleicons.org/googlegemini/8E75B2" width="48" height="48" alt="Gemini" />
  </a><br/>
  <sub><a href="https://gemini.google.com"><b>Gemini</b></a></sub>
</td>
<td align="center" width="100">
  <sub><b>+ Much<br/>More</b></sub>
</td>
</tr>
</table>

🧬 RL Training Backends for Weight Evolution

<table>
<tr>
<td align="center" width="100">
  <a href="https://www.thinkingmachines.ai/tinker/">
    <img src="tinker.jpg" width="48" height="48" alt="Tinker" />
  </a><br/>
  <sub><a href="https://www.thinkingmachines.ai/tinker/"><b>Tinker</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://github.com/MindLab-Research/mindlab-toolkit">
    <img src="https://github.com/MindLab-Research.png?size=200" width="48" height="48" alt="MinT" />
  </a><br/>
  <sub><a href="https://github.com/MindLab-Research/mindlab-toolkit"><b>MinT</b></a></sub>
</td>
<td align="center" width="100">
  <sub><b>More<br/>Coming</b></sub>
</td>
</tr>
</table>

<p>
  <a href="https://github.com/aiming-lab/MetaClaw"><img src="https://img.shields.io/badge/github-MetaClaw-181717?style=flat&labelColor=555&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat&labelColor=555" alt="License MIT"></a>
  <img src="https://img.shields.io/badge/⚡_Полностью_асинхронно-yellow?style=flat&labelColor=555" alt="Fully Async" />
  <img src="https://img.shields.io/badge/☁️_Без_GPU_кластера-blue?style=flat&labelColor=555" alt="No GPU Cluster" />
  <img src="https://img.shields.io/badge/🛠️_Эволюция_навыков-orange?style=flat&labelColor=555" alt="Skill Evolution" />
  <img src="https://img.shields.io/badge/🚀_Развертывание_в_один_клик-green?style=flat&labelColor=555" alt="One-Click Deploy" />
</p>

<br/>

[🇺🇸 English](../README.md) • [🇨🇳 中文](./README_ZH.md) • [🇯🇵 日本語](./README_JA.md) • [🇰🇷 한국어](./README_KO.md) • [🇫🇷 Français](./README_FR.md) • [🇩🇪 Deutsch](./README_DE.md) • [🇪🇸 Español](./README_ES.md) • [🇧🇷 Português](./README_PT.md) • [🇮🇹 Italiano](./README_IT.md) • [🇻🇳 Tiếng Việt](./README_VI.md) • [🇸🇦 العربية](./README_AR.md) • [🇮🇳 हिन्दी](./README_HI.md)

<br/>

[Обзор](#-обзор) • [Быстрый старт](#-быстрый-старт) • [Команды CLI](#️-команды-cli) • [Конфигурация](#️-конфигурация) • [Навыки](#-навыки-skills) • [Режим RL](#-продвинутое-режим-rl) • [Режим OPD](#-продвинутое-режим-opd) • [Планировщик мета-обучения](#-продвинутое-планировщик-мета-обучения-v03) • [Цитирование](#-цитирование)

</div>

---

<div align="center">

### Две команды. Это все.
</div>

```bash
metaclaw setup              # одноразовый мастер настройки
metaclaw start              # по умолчанию: режим madmax, навыки + плановое RL-обучение
metaclaw start --mode rl    # RL без планировщика (обучение сразу по заполнении batch)
metaclaw start --mode skills_only  # только навыки, без RL (Tinker не нужен)
```

<div align="center">
<img src="metaclaw.gif" alt="MetaClaw demo" width="700">
</div>

---

## 🔥 Новости

- **[13.03.2026]** **v0.3.1** — Поддержка бэкенда MinT: RL-обучение теперь работает как с Tinker, так и с MinT. Настраивается через `rl.backend` (auto/tinker/mint).
- **[13.03.2026]** **v0.3** — Поддержка непрерывного мета-обучения: медленные RL-обновления запускаются только во время сна, простоя или встреч в Google Calendar. Добавлено разделение на support/query множества для предотвращения загрязнения обновлений модели устаревшими сигналами вознаграждения.
- **[11.03.2026]** **v0.2** — Развертывание в один клик через CLI `metaclaw`. Навыки включены по умолчанию, RL теперь опционален.
- **[09.03.2026]** Выпущен **MetaClaw**. Просто общайтесь с агентом, и он будет эволюционировать автоматически. GPU-развертывание **не требуется**, достаточно подключить **API**.

---

## 🎥 Демонстрация

https://github.com/user-attachments/assets/d86a41a8-4181-4e3a-af0e-dc453a6b8594

---

## 📖 Обзор

**MetaClaw — это агент, который мета-обучается и эволюционирует в реальных условиях.**
Просто общайтесь с агентом, как обычно. MetaClaw превращает каждый живой диалог в обучающий сигнал, позволяя агенту непрерывно совершенствоваться через реальное развертывание, а не только через офлайн-обучение.

Под капотом MetaClaw размещает вашу модель за OpenAI-совместимым прокси, который перехватывает взаимодействия из OpenClaw, внедряет релевантные навыки на каждом шаге и мета-обучается на накопленном опыте. После каждой сессии навыки автоматически суммируются; при включённом RL планировщик мета-обучения откладывает обновление весов до окон простоя, чтобы агент не прерывался во время активного использования.

GPU-кластер не требуется. MetaClaw работает с любым OpenAI-совместимым LLM API «из коробки» и использует Tinker-совместимый бэкенд для облачного LoRA-дообучения. [Tinker](https://www.thinkingmachines.ai/tinker/) является путём по умолчанию, а MinT можно подключить через отдельный пакет совместимости при необходимости.

## 🤖 Ключевые возможности

### **Развертывание в один клик**
Настройте один раз с помощью `metaclaw setup`, затем `metaclaw start` запускает прокси, внедряет навыки и автоматически подключает OpenClaw. Ручные shell-скрипты не нужны.

### **Три режима работы**

| Режим | По умолчанию | Описание |
|-------|-------------|----------|
| `madmax` | ✅ | RL + интеллектуальный планировщик. Навыки всегда активны; обновление весов RL происходит только во время сна/простоя/встреч. |
| `rl` | — | RL без планировщика. Обучение запускается сразу при заполнении batch (поведение v0.2). |
| `skills_only` | — | Прокси → ваш LLM API. Навыки внедряются, после каждой сессии автоматически суммируются. GPU/Tinker не требуются. |

### **Внедрение навыков**
На каждом шаге диалога MetaClaw извлекает наиболее релевантные инструкции-навыки и внедряет их в системный промпт агента. Немедленное улучшение поведения без переобучения.

### **Автоматическое суммирование навыков**
После каждого диалога тот же LLM, который вы используете, анализирует сессию и автоматически создаёт новые навыки. При включённом RL специализированная модель-судья извлекает навыки из неудачных эпизодов.

### **GPU-кластер не требуется**
В режиме `skills_only` достаточно сетевого подключения. RL-обучение выгружается на Tinker-совместимый бэкенд.

### **Два режима обучения**
MetaClaw поддерживает оба варианта:
- **RL (GRPO)** для обучения на неявных сигналах обратной связи
- **Дистилляция с политикой на лету (OPD)** для дистилляции большей модели-учителя в модель-ученика на его собственной политике

В режиме OPD модель-ученик генерирует ответы как обычно, а модель-учитель предоставляет потокенные логарифмические вероятности для тех же ответов. Логарифмические вероятности учителя передаются в функцию потерь (например, `cispo`), чтобы ученик обучался распределению учителя. Учитель должен быть развёрнут за OpenAI-совместимой точкой доступа `/v1/completions` (например, vLLM, SGLang).

### **Полностью асинхронная архитектура**
Обслуживание, моделирование вознаграждений и обучение полностью разделены. Агент продолжает отвечать, пока оценка и оптимизация выполняются параллельно.

---

## 🚀 Быстрый старт

### 1. Установка

```bash
pip install -e .                        # режим skills_only (легковесный)
pip install -e ".[rl]"                  # + поддержка RL-обучения (torch, transformers, tinker)
pip install -e ".[evolve]"              # + эволюция навыков через OpenAI-совместимый LLM
pip install -e ".[scheduler]"           # + интеграция с Google Calendar для планировщика
pip install -e ".[rl,evolve,scheduler]" # рекомендуется для полной конфигурации RL + планировщик
```

Если вы хотите использовать `rl.backend=mint`, установите пакет совместимости MinT отдельно в том же окружении, например [`mindlab-toolkit`](https://github.com/MindLab-Research/mindlab-toolkit). MetaClaw не включает эту зависимость в пакет по умолчанию, чтобы пользователи RL могли явно выбирать между Tinker и MinT.

### 2. Настройка

```bash
metaclaw setup
```

Интерактивный мастер предложит выбрать LLM-провайдера (Kimi, Qwen, MiniMax или пользовательский), ввести API-ключ и опционально включить RL-обучение.

RL-путь MetaClaw позволяет явно переключаться между `tinker` и `mint`. Рекомендуемое значение по умолчанию: `auto`. При установленном пакете MinT он по-прежнему способен распознать MinT по учётным данным или base URL в стиле Mint.

```bash
metaclaw config rl.backend mint
metaclaw config rl.api_key sk-mint-...
metaclaw config rl.base_url https://mint.macaron.xin/
metaclaw config rl.model Qwen/Qwen3-4B-Instruct-2507
```

Устаревшие псевдонимы `rl.tinker_api_key` и `rl.tinker_base_url` по-прежнему поддерживаются для обратной совместимости.

### 3. Запуск

```bash
metaclaw start
```

Это всё. MetaClaw запускает прокси, автоматически настраивает OpenClaw и перезапускает шлюз. Откройте OpenClaw и начните диалог: навыки внедряются на каждом шаге, а по завершении сессии автоматически суммируются в новые навыки.

---

## 🛠️ Команды CLI

```
metaclaw setup                  # Интерактивный мастер первоначальной настройки
metaclaw start                  # Запуск MetaClaw (по умолчанию: режим madmax)
metaclaw start --mode rl        # Принудительно включить режим RL (без планировщика) для этой сессии
metaclaw start --mode skills_only  # Принудительно включить режим только навыков для этой сессии
metaclaw stop                   # Остановить работающий экземпляр MetaClaw
metaclaw status                 # Проверить состояние прокси, режим работы и статус планировщика
metaclaw config show            # Просмотр текущей конфигурации
metaclaw config KEY VALUE       # Установить значение конфигурации
```

**Часто используемые ключи конфигурации:**

```bash
metaclaw config rl.enabled true           # Включить RL-обучение
metaclaw config rl.backend auto           # auto | tinker | mint
metaclaw config rl.api_key sk-...         # Установить ключ RL-бэкенда
metaclaw config rl.base_url https://mint.macaron.xin/  # Необязательная точка доступа бэкенда, например MinT
metaclaw config skills.auto_evolve false  # Отключить автоматическое суммирование навыков
metaclaw config proxy.port 31000          # Изменить порт прокси
```

---

## ⚙️ Конфигурация

Файл конфигурации находится в `~/.metaclaw/config.yaml` и создаётся командой `metaclaw setup`.

```yaml
mode: madmax               # "madmax" | "rl" | "skills_only"

llm:
  provider: kimi            # kimi | qwen | openai | minimax | custom
  model_id: moonshotai/Kimi-K2.5
  api_base: https://api.moonshot.cn/v1
  api_key: sk-...

proxy:
  port: 30000
  api_key: ""              # необязательный bearer-токен для локального прокси MetaClaw

skills:
  enabled: true
  dir: ~/.metaclaw/skills   # каталог вашей библиотеки навыков
  retrieval_mode: template  # template | embedding
  top_k: 6
  task_specific_top_k: 10   # лимит навыков для конкретных задач (по умолчанию 10)
  auto_evolve: true         # автоматическое суммирование навыков после каждой сессии

rl:
  enabled: false            # установите true для включения RL-обучения
  backend: auto             # "auto" | "tinker" | "mint"
  model: moonshotai/Kimi-K2.5
  api_key: ""
  base_url: ""              # необязательная точка доступа бэкенда, например https://mint.macaron.xin/ для MinT
  tinker_api_key: ""        # устаревший псевдоним для api_key
  tinker_base_url: ""       # устаревший псевдоним для base_url
  prm_url: https://api.openai.com/v1
  prm_model: gpt-5.2
  prm_api_key: ""
  lora_rank: 32
  batch_size: 4
  resume_from_ckpt: ""      # необязательный путь к контрольной точке для возобновления обучения
  evolver_api_base: ""      # оставьте пустым для использования llm.api_base
  evolver_api_key: ""
  evolver_model: gpt-5.2

opd:
  enabled: false            # установите true для включения OPD (дистилляция учителя)
  teacher_url: ""           # base URL модели-учителя (OpenAI-совместимый /v1/completions)
  teacher_model: ""         # имя модели-учителя (например, Qwen/Qwen3-32B)
  teacher_api_key: ""       # API-ключ модели-учителя
  kl_penalty_coef: 1.0      # коэффициент KL-штрафа для OPD

max_context_tokens: 20000   # лимит токенов промпта перед усечением

scheduler:                  # v0.3: планировщик мета-обучения (автоматически включается в режиме madmax)
  enabled: false            # в режиме madmax включается автоматически; для режима rl установите вручную
  sleep_start: "23:00"      # ЧЧ:ММ по местному времени, начало окна сна
  sleep_end: "07:00"        # ЧЧ:ММ по местному времени, конец окна сна
  idle_threshold_minutes: 30  # запуск RL после N минут неактивности клавиатуры
  min_window_minutes: 15    # минимальная длина окна для запуска шага RL
  calendar:
    enabled: false          # использовать Google Calendar для определения слотов встреч
    credentials_path: ""    # путь к client_secrets.json из Google Cloud Console
    token_path: ""          # сохранённый OAuth-токен (по умолчанию: ~/.metaclaw/calendar_token.json)
```

---

## 💪 Навыки (Skills)

Навыки представляют собой короткие Markdown-инструкции, внедряемые в системный промпт агента на каждом шаге. Они хранятся в каталоге навыков (по умолчанию `~/.metaclaw/skills/`) в виде отдельных файлов `SKILL.md`.

**Автоматическое суммирование навыков** запускается после каждого диалога. Настроенный LLM анализирует, что произошло, и генерирует новые навыки автоматически. Ручная обработка не требуется: библиотека навыков растёт вместе с использованием.

Для предварительной загрузки встроенного банка навыков (более 40 навыков по программированию, безопасности, агентным задачам и др.):

```bash
cp -r memory_data/skills/* ~/.metaclaw/skills/
```

---

## 🔬 Продвинутое: режим RL

Включите RL-обучение для непрерывной тонкой настройки модели на основе живых диалогов с помощью Tinker или MinT:

```bash
metaclaw config rl.enabled true
metaclaw config rl.backend mint
metaclaw config rl.api_key sk-...
metaclaw config rl.base_url https://mint.macaron.xin/
metaclaw config rl.model Qwen/Qwen3-4B-Instruct-2507
metaclaw config rl.prm_url https://api.openai.com/v1
metaclaw config rl.prm_api_key sk-...
metaclaw start
```

В режиме RL:
- Каждый шаг диалога токенизируется и отправляется как обучающий пример
- Модель-судья (PRM) асинхронно оценивает ответы
- Tinker-совместимый бэкенд (Tinker cloud или MinT) выполняет LoRA-дообучение; обновлённые веса подгружаются «на лету» каждые `batch_size` примеров
- Специализированная модель-эволюционер извлекает новые навыки из неудачных эпизодов

Если вы предпочитаете Tinker cloud, установите `rl.backend` в `tinker` или оставьте `auto` и не указывайте точку доступа MinT.

**Программный rollout** (без TUI OpenClaw): установите `openclaw_env_data_dir` на каталог с JSONL-файлами задач:

```json
{"task_id": "task_1", "instruction": "Register the webhook at https://example.com/hook"}
```

---

## 🔬 Продвинутое: режим OPD

Дистилляция с политикой на лету (OPD) позволяет дистиллировать большую модель-учителя в модель-ученика во время онлайн-обучения. Ученик генерирует ответы как обычно; учитель предоставляет потокенные логарифмические вероятности для тех же ответов. KL-штраф направляет ученика к распределению учителя.

```bash
metaclaw config opd.enabled true
metaclaw config opd.teacher_url http://localhost:8082/v1
metaclaw config opd.teacher_model Qwen/Qwen3-32B
metaclaw config opd.kl_penalty_coef 1.0
metaclaw start --mode rl
```

Учитель должен быть развёрнут за OpenAI-совместимой точкой доступа `/v1/completions` (например, vLLM, SGLang). OPD можно комбинировать с оценкой PRM, оба процесса выполняются асинхронно.

См. `examples/run_conversation_opd.py` для программного примера и `scripts/run_openclaw_tinker_opd.sh` для готового скрипта запуска.

---

## 🧠 Продвинутое: планировщик мета-обучения (v0.3)

В режиме RL шаг горячей замены весов приостанавливает агента на несколько минут. Планировщик (включённый по умолчанию в режиме `madmax`) откладывает RL-обновления до окон неактивности пользователя, чтобы агент не прерывался во время активного использования.

```bash
metaclaw config scheduler.sleep_start "23:00"
metaclaw config scheduler.sleep_end   "07:00"
metaclaw config scheduler.idle_threshold_minutes 30

# Необязательно: интеграция с Google Calendar
pip install -e ".[scheduler]"
metaclaw config scheduler.calendar.enabled true
metaclaw config scheduler.calendar.credentials_path ~/.metaclaw/client_secrets.json
```

Три условия запускают окно обновления (достаточно любого одного): настроенные часы сна, неактивность клавиатуры системы или активное событие Google Calendar. Если пользователь возвращается во время обновления, частичный batch сохраняется и возобновляется в следующем окне.

Каждый `ConversationSample` помечается версией `skill_generation`. Когда эволюция навыков увеличивает поколение, RL-буфер очищается, и для градиентных обновлений используются только пост-эволюционные примеры (разделение MAML support/query множеств).

---

## 📚 Цитирование

```bibtex
@misc{xia2026metaclaw,
  author       = {Xia, Peng and Chen, Jianwen and Yang, Xinyu and Tu, Haoqin and Han, Siwei and Qiu, Shi and Zheng, Zeyu and Xie, Cihang and Yao, Huaxiu},
  title        = {MetaClaw: Just Talk --- An Agent That Meta-Learns and Evolves in the Wild},
  year         = {2026},
  organization = {GitHub},
  url          = {https://github.com/aiming-lab/MetaClaw},
}
```

---

## 🙏 Благодарности

MetaClaw построен на основе следующих проектов с открытым исходным кодом:

- [OpenClaw](https://openclaw.ai) — основной фреймворк агента.
- [SkillRL](https://github.com/aiming-lab/SkillRL) — наш фреймворк RL с расширением навыков.
- [Tinker](https://www.thinkingmachines.ai/tinker/) — используется для онлайн RL-обучения.
- [MinT](https://github.com/MindLab-Research/mindlab-toolkit) — альтернативный бэкенд для онлайн RL-обучения.
- [OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) — вдохновение для нашего дизайна RL.
- [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) — основа для нашего банка навыков.

---

## 📄 Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).
