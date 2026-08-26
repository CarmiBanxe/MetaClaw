#!/usr/bin/env bash
set -euo pipefail

cd "${1:-$HOME/MetaClaw}"
mkdir -p .claude docs/architecture scripts/ai

cat > CLAUDE.md <<'EOT'
# BANXE Claude Canon

## Primary task
The primary task is to use Free Claude Code (FCC) as the canonical gateway for Claude Code-compatible traffic, with cloud-first model routing, in order to accelerate design and implementation of the BANXE banking platform.

## Project identity
BANXE EMI AI BANK is built on TypeScript/NestJS.
Core target architecture:
- NestJS + CQRS / event sourcing
- dedicated double-entry ledger service
- Ballerine-based KYC/KYB orchestration
- ISO 20022 adapter layer

## Task-first rule
If a rule, tool, local model, policy, or workflow hinders the primary task, it must be downgraded, removed from the primary path, or rewritten.
The canon serves the task, not the reverse.
Sandbox assumptions apply to local development operations, but core architecture discipline remains mandatory.

## Canonical AI gateway
FCC is the canonical AI gateway.
Claude Code-compatible traffic must go through FCC.
Primary strategy is cloud-first via supported providers.
Ollama is not the primary strategy and may exist only as a last-resort fallback.

## Provider focus
Priority providers:
- NVIDIA NIM
- OpenRouter
- DeepSeek
- Kimi / Moonshot via supported routing path

## Terminal doctrine
- Central terminal = BRAIN
- Left terminal = FACTORY
- Right terminal = ASSISTANT

## Execution model
- Shell is the operator control plane and audit transport.
- Claude Code and Codex sessions are the execution plane.
- Central decides.
- Factory executes.
- Assistant supports research, summaries, and transfer.

## Model policy
- Minimize expensive premium-token usage.
- Use strong cloud coding models for implementation.
- Use stronger cloud review models for verification.
- Use Codex as an independent second opinion where required.
- Use configured fallback chains when limits are exhausted.
- Remove weak local LLMs from the default path.

## What may be removed from the primary path
The following may be downgraded or removed from the primary execution path if they hinder the task:
- weak local coding models
- local-first assumptions that block cloud-first routing
- restrictive workflow habits that prevent FCC rollout
- outdated model defaults
- non-essential auxiliary agent stacks

## What must remain disciplined
The following remain mandatory:
- human review for high-risk banking domains
- no silent committing of real secrets
- no treating first-pass model output as truth in ledger, auth, KYC/AML, reconciliation, or payment state logic
- architecture documentation in docs/architecture

## Sensitive architecture rules
Never trust first-pass output in:
- ledger invariants
- postings
- reconciliation
- auth/authz
- KYC/AML decisions
- payment state transitions
- ISO 20022 business semantics

## Documentation rules
- AI routing rules must be reflected in docs/architecture/ai-gateway.md.
- Architecture decisions must be reflected in docs/architecture.
- Terminal routines become canonical only after documentation.

## Output style
- Prefer deterministic changes over speculative rewrites.
- For risky modules, produce patch plans before edits.
- Keep implementation notes concise.
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
This document defines the BANXE task-first standard for routing Claude Code-compatible traffic through Free Claude Code (FCC).

## Canonical gateway
Claude Code is routed through FCC using:
- ANTHROPIC_BASE_URL=http://127.0.0.1:8082
- ANTHROPIC_AUTH_TOKEN=freecc

FCC is started with:
- fcc-server

Claude Code may be started with:
- fcc-claude
or any Claude launcher that inherits the FCC environment.

## Provider strategy
Primary routing is cloud-first.
Preferred provider focus:
- NVIDIA NIM
- OpenRouter
- DeepSeek
- Kimi / Moonshot via supported path

Ollama is last-resort fallback only.

## Important gateway consequence
When Claude Code is routed to a non-first-party gateway, some native capabilities may be reduced or disabled by default, including MCP tool search and Remote Control behavior.
These limitations are accepted when necessary for the primary task.

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

## Banking boundary
FCC is an execution accelerator, not the banking architecture itself.
Core target architecture remains:
- NestJS + CQRS / event sourcing
- dedicated double-entry ledger
- Ballerine KYC/KYB orchestration
- ISO 20022 adapter layer

## Critical domains
Human review remains mandatory for:
- ledger invariants
- reconciliation
- payments state transitions
- KYC/AML
- auth/authz
- regulatory logic

## Secrets
Provider keys are not committed.
Provider keys stay in local FCC Admin UI, local environment, or a secret manager.

## Operational checks
- Run fcc-server
- Open Admin UI
- Configure cloud provider keys
- Select primary cloud models
- Configure fallback chain
- Run Claude Code with FCC environment
- Verify with /status
- Verify with /model
EOT

echo "TASK_FIRST_FCC_CANON_READY"
