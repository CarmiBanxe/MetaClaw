#!/usr/bin/env bash
set -euo pipefail

cd "${1:-$HOME/MetaClaw}"

mkdir -p .claude docs/architecture scripts/ai

cat > CLAUDE.md <<'EOT'
# BANXE Claude Canon

## Project identity
BANXE EMI AI BANK is built on TypeScript/NestJS.
Core architectural target:
- NestJS + CQRS / event sourcing
- dedicated double-entry ledger service
- Ballerine-based KYC/KYB orchestration
- ISO 20022 adapter layer

## Terminal doctrine
- Central terminal = BRAIN
- Left terminal = FACTORY
- Right terminal = ASSISTANT

## Cross-terminal canon
- Every substantial implementation must be aligned with the central terminal.
- The left terminal produces code and routine artifacts.
- The right terminal supports search, summarization, cleanup, and helper work.
- Keep one unified AI gateway standard across all terminals.

## Sensitive architecture rules
Treat the following zones as high-risk and never trust first-pass output:
- ledger invariants
- postings
- reconciliation
- auth/authz
- KYC/AML decisions
- payment state transitions
- ISO 20022 business semantics

## Security rules
- NEVER read or process .env files unless explicitly authorized by the user in the current session.
- NEVER read ./secrets/**
- NEVER exfiltrate credentials into logs, commits, docs, or generated examples.
- Prefer stubs and placeholders over real secrets.

## Documentation rules
- Architecture decisions must be reflected in docs/architecture.
- AI operating rules must be reflected in docs/architecture/ai-gateway.md.
- New terminal routines must be documented before being considered canonical.

## Execution policy
- Central terminal: architecture, ADR, critical code review, final decisions.
- Left terminal: scaffolding, DTOs, handlers, tests, migrations, repetitive generation.
- Right terminal: repo exploration, summaries, refactor assistance, docs grooming.

## Output style
- Write concise implementation notes.
- Prefer deterministic changes over speculative large rewrites.
- For risky modules, propose patch plans before editing.
EOT

cat > .claude/settings.json <<'EOT'
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "env": {
    "ANTHROPIC_BASE_URL": "http://127.0.0.1:8082",
    "ANTHROPIC_AUTH_TOKEN": "freecc",
    "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "190000",
    "API_TIMEOUT_MS": "1200000",
    "BASH_DEFAULT_TIMEOUT_MS": "300000",
    "BASH_MAX_TIMEOUT_MS": "600000",
    "CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR": "1"
  },
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  }
}
EOT

cat > .claude/settings.local.json.example <<'EOT'
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "env": {
    "BANXE_TERMINAL_ROLE": "central"
  }
}
EOT

cat > docs/architecture/ai-gateway.md <<'EOT'
# AI Gateway Standard

## Purpose
This document defines the BANXE standard for routing Claude Code through an internal FCC gateway across all terminals.

## Gateway
Claude Code is routed through FCC using:
- ANTHROPIC_BASE_URL=http://127.0.0.1:8082
- ANTHROPIC_AUTH_TOKEN=freecc

FCC is started with:
- fcc-server

Claude Code is started with:
- fcc-claude

## Terminal roles
- Central = Brain
- Left = Factory
- Right = Assistant

## Routing doctrine
- Strongest reasoning/coding tier for Central.
- Cheapest stable coding tier for Left.
- Fast helper/local tier for Right.
- Global fallback chain configured in FCC Admin UI.

## Critical domains
Do not accept model output without human review for:
- ledger invariants
- reconciliation
- payments state transitions
- KYC/AML
- auth/authz
- regulatory logic

## Local secrets
Provider keys are never committed.
Provider keys live only in local FCC Admin UI, local environment, or a secret manager.

## Operational checks
- Run fcc-server
- Open Admin UI
- Validate provider
- Apply model and fallback chain
- Run fcc-claude
- Verify with /status
- Verify active model with /model
EOT

cat > scripts/ai/fcc-env-central.sh <<'EOT'
#!/usr/bin/env bash
export BANXE_TERMINAL_ROLE="central"
export ANTHROPIC_BASE_URL="http://127.0.0.1:8082"
export ANTHROPIC_AUTH_TOKEN="freecc"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
export CLAUDE_CODE_AUTO_COMPACT_WINDOW="190000"
export API_TIMEOUT_MS="1200000"
export BASH_DEFAULT_TIMEOUT_MS="300000"
export BASH_MAX_TIMEOUT_MS="600000"
unset ANTHROPIC_API_KEY || true
EOT

cat > scripts/ai/fcc-env-left.sh <<'EOT'
#!/usr/bin/env bash
export BANXE_TERMINAL_ROLE="left"
export ANTHROPIC_BASE_URL="http://127.0.0.1:8082"
export ANTHROPIC_AUTH_TOKEN="freecc"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
export CLAUDE_CODE_AUTO_COMPACT_WINDOW="160000"
export API_TIMEOUT_MS="1200000"
export BASH_DEFAULT_TIMEOUT_MS="300000"
export BASH_MAX_TIMEOUT_MS="600000"
unset ANTHROPIC_API_KEY || true
EOT

cat > scripts/ai/fcc-env-right.sh <<'EOT'
#!/usr/bin/env bash
export BANXE_TERMINAL_ROLE="right"
export ANTHROPIC_BASE_URL="http://127.0.0.1:8082"
export ANTHROPIC_AUTH_TOKEN="freecc"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
export CLAUDE_CODE_AUTO_COMPACT_WINDOW="120000"
export API_TIMEOUT_MS="1200000"
export BASH_DEFAULT_TIMEOUT_MS="300000"
export BASH_MAX_TIMEOUT_MS="600000"
unset ANTHROPIC_API_KEY || true
EOT

cat > scripts/ai/run-central.sh <<'EOT'
#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/fcc-env-central.sh"
if command -v fcc-claude >/dev/null 2>&1; then
  exec fcc-claude
elif command -v claude >/dev/null 2>&1; then
  exec claude
elif command -v claude-code >/dev/null 2>&1; then
  exec claude-code
else
  echo "No Claude launcher found: fcc-claude / claude / claude-code" >&2
  exit 1
fi
EOT

cat > scripts/ai/run-left.sh <<'EOT'
#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/fcc-env-left.sh"
if command -v fcc-claude >/dev/null 2>&1; then
  exec fcc-claude
elif command -v claude >/dev/null 2>&1; then
  exec claude
elif command -v claude-code >/dev/null 2>&1; then
  exec claude-code
else
  echo "No Claude launcher found: fcc-claude / claude / claude-code" >&2
  exit 1
fi
EOT

cat > scripts/ai/run-right.sh <<'EOT'
#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/fcc-env-right.sh"
if command -v fcc-claude >/dev/null 2>&1; then
  exec fcc-claude
elif command -v claude >/dev/null 2>&1; then
  exec claude
elif command -v claude-code >/dev/null 2>&1; then
  exec claude-code
else
  echo "No Claude launcher found: fcc-claude / claude / claude-code" >&2
  exit 1
fi
EOT

cat > scripts/ai/prompt-central.txt <<'EOT'
Ты работаешь в роли CENTRAL / BRAIN для BANXE EMI AI BANK.

Контекст:
- TypeScript / NestJS
- CQRS / Event Sourcing
- Dedicated double-entry ledger
- Ballerine KYC/KYB orchestration
- ISO 20022 adapter layer

Правила:
- Ты принимаешь архитектурные решения и валидируешь изменения перед внедрением.
- Не предлагай рискованные изменения без плана миграции.
- Особо осторожно относись к ledger, reconciliation, auth, KYC/AML и payment state transitions.
- Сначала дай краткий plan, затем concrete patch proposal.
- Учитывай, что левый терминал — factory, правый — assistant.
- Если задача рутинная, формулируй ее как пакет инструкций для left terminal.
- Если задача исследовательская или документарная, делегируй подготовку right terminal.

Формат ответа:
1. Decision
2. Why
3. Exact implementation steps
4. Risks
5. Hand-off for left/right terminal
EOT

cat > scripts/ai/prompt-left.txt <<'EOT'
Ты работаешь в роли LEFT / FACTORY для BANXE EMI AI BANK.

Твоя функция:
- быстро производить рутинные инженерные артефакты
- scaffold сервисы
- писать DTO, handlers, tests, migrations, boilerplate
- не принимать архитектурные решения самостоятельно

Правила:
- Следуй архитектурному канону проекта из CLAUDE.md.
- Если задача затрагивает ledger invariants, reconciliation, auth/authz, KYC/AML или ISO 20022 semantics, остановись и запроси подтверждение от central.
- Предпочитай небольшие атомарные патчи.
- После генерации давай список измененных файлов и краткое описание.

Формат ответа:
1. Planned files
2. Patch summary
3. Risks or blockers
EOT

cat > scripts/ai/prompt-right.txt <<'EOT'
Ты работаешь в роли RIGHT / ASSISTANT для BANXE EMI AI BANK.

Твоя функция:
- исследование репозитория
- поиск по коду
- суммаризация
- подготовка документации
- рефакторинг низкого риска
- подготовка hand-off для central и left

Правила:
- Не менять критичные бизнес-инварианты без explicit instruction.
- Ускоряй работу central и left за счет поиска, конспекта и структурирования.
- Если видишь конфликт архитектуры и реализации, поднимай это как observation, а не исправляй молча.
- Все важные findings фиксируй кратко и по файлам.

Формат ответа:
1. Findings
2. Affected files
3. Suggested next action
EOT

touch .gitignore
grep -Fqx '.claude/settings.local.json' .gitignore || printf '%s\n' '.claude/settings.local.json' >> .gitignore
grep -Fqx 'CLAUDE.local.md' .gitignore || printf '%s\n' 'CLAUDE.local.md' >> .gitignore
grep -Fqx '.env' .gitignore || printf '%s\n' '.env' >> .gitignore
grep -Fqx '.env.*' .gitignore || printf '%s\n' '.env.*' >> .gitignore
grep -Fqx 'secrets/' .gitignore || printf '%s\n' 'secrets/' >> .gitignore
grep -Fqx '.fcc/' .gitignore || printf '%s\n' '.fcc/' >> .gitignore

chmod +x scripts/ai/*.sh

echo "BOOTSTRAP_READY"
