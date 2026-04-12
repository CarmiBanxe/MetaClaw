# CLAUDE.md — MetaClaw
**Repo:** CarmiBanxe/MetaClaw | **Plane:** AI Agent Framework | **Updated:** 2026-04-12 (FIX-VERIFY-6)

---

## О проекте

MetaClaw — мета-обучающийся AI агент-фреймворк. Агент учится и эволюционирует
из каждого разговора без GPU. Вдохновлён принципами работы мозга.

**Техническая статья:** arxiv.org/abs/2603.17187

---

## Технологический стек

```
Язык:      Python 3.11+
Пакет:     metaclaw (pyproject.toml)
Тесты:     pytest
Примеры:   examples/
Память:    memory_data/
Агенты:    metaclaw/ (core package)
```

---

## Структура пакетов

```
metaclaw/          — core package
  agents/          — agent implementations
  memory/          — memory subsystem
  evolution/       — meta-learning module
examples/          — usage examples
tests/             — test suite
scripts/           — utility scripts
docs/              — documentation
assets/            — images/logos
memory_data/       — persisted agent memory
```

---

## Команды

```bash
# Установка
pip install -e .

# Тесты
pytest tests/

# Примеры
python examples/basic_agent.py
```

---

## Правила разработки

1. **Не ломай** memory_data/ — это персистентная память агентов
2. **Совместимость** с banxe-emi-stack (compliance integration)
3. **Тесты** обязательны для новых агентов
4. **COLLAB.md** — правила коллаборации

---

*Workspace: /home/mmber/MetaClaw | Stack: Python + MetaClaw framework*
