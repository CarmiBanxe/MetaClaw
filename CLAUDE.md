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
