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

## AI gateway canon
The canonical AI routing layer is Free Claude Code (FCC).
Claude Code-compatible traffic must go through FCC as the local gateway.
Primary model strategy is cloud-first through supported providers.
Local Ollama is not the strategic default and may only exist as a last-resort fallback.

## Approved provider focus
Priority cloud providers:
- NVIDIA NIM
- OpenRouter
- DeepSeek
- Kimi / Moonshot via supported FCC path

## Terminal doctrine
- Central terminal = BRAIN
- Left terminal = FACTORY
- Right terminal = ASSISTANT

## Execution plane
- Shell is the operator control plane and live-audit transport.
- The real execution plane may run in Claude Code and Codex sessions.
- All substantial implementation still flows through the factory.
- Central decides, factory executes, assistant supports.

## Factory model policy
- Routine work should minimize expensive premium-token usage.
- Main code writing uses a strong cloud coding model.
- Main verification uses a stronger review model.
- Codex may provide an independent second opinion.
- If one quota or provider fails, FCC fallback chain must replace it.

## Cross-terminal canon
- Every substantial implementation must be aligned with the central terminal.
- The left terminal produces code and routine artifacts.
- The right terminal supports search, summarization, cleanup, and helper work.
- Keep one unified FCC gateway standard across all terminals.

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
- Provider keys must not be committed.
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
    "CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT": "1",
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

cat > docs/architecture/ai-gateway.md <<'EOT'
# AI Gateway Standard

## Purpose
This document defines the BANXE standard for routing Claude Code-compatible traffic through Free Claude Code (FCC).

## Canonical gateway
Claude Code is routed through FCC using:
- ANTHROPIC_BASE_URL=http://127.0.0.1:8082
- ANTHROPIC_AUTH_TOKEN=freecc

FCC is started with:
- fcc-server

Claude Code may be started with:
- fcc-claude
or with a Claude launcher in a shell that already exports the FCC environment.

## Canonical provider strategy
Primary routing is cloud-first.
Preferred provider focus:
- NVIDIA NIM
- OpenRouter
- DeepSeek
- Kimi / Moonshot via supported FCC path

Local Ollama is optional only as a last fallback and must not be treated as the main model path.

## Terminal roles
- Central = Brain
- Left = Factory
- Right = Assistant

## Routing doctrine
- Strongest cloud reasoning/coding tier for Central.
- Cheaper but capable cloud coding tier for Left.
- Fast cloud helper tier for Right.
- Global fallback chain configured in FCC Admin UI.
- When one limit is exhausted, the next configured model/provider must take over.

## Banking architecture boundary
FCC accelerates AI-assisted implementation work.
It does not replace banking architecture.
Core target architecture remains:
- NestJS + CQRS / event sourcing
- dedicated double-entry ledger
- Ballerine KYC/KYB orchestration
- ISO 20022 adapter layer

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
- Configure cloud provider API keys
- Select primary cloud models
- Configure fallback chain
- Run fcc-claude or a Claude launcher with FCC env
- Verify with /status
- Verify active model with /model
EOT

cat > scripts/ai/fcc-env-central.sh <<'EOT'
#!/usr/bin/env bash
export BANXE_TERMINAL_ROLE="central"
export ANTHROPIC_BASE_URL="http://127.0.0.1:8082"
export ANTHROPIC_AUTH_TOKEN="freecc"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
export CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT="1"
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
export CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT="1"
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
export CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT="1"
export CLAUDE_CODE_AUTO_COMPACT_WINDOW="120000"
export API_TIMEOUT_MS="1200000"
export BASH_DEFAULT_TIMEOUT_MS="300000"
export BASH_MAX_TIMEOUT_MS="600000"
unset ANTHROPIC_API_KEY || true
EOT

chmod +x scripts/ai/fcc-env-*.sh

echo "CLOUD_FIRST_CANON_APPLIED"
