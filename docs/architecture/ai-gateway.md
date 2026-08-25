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
