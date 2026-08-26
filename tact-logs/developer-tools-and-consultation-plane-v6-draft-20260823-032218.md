# Developer Tools and Consultation Plane v6 — Draft

**Status:** Draft only. No plugin installation, API call, configuration mutation, credential read/write, or runtime activation.

## Permanent tool planes

### Codex plugin / CLI
- Status: permanent controlled development tool.
- Roles: repository analysis, implementation planning, approved patch execution, test execution, diff review, verification and independent consultation.
- Execution boundary: no self-approval; code/config/policy changes require named approval and evidence.
- Budget boundary: do not use Codex for routine bulk reading or first-pass summaries when Tier A routes are eligible.

### Mistral API via LiteLLM
- Status: permanent provider family once staging pin/proof/approval gates pass.
- Intended draft alias: `mistral-medium-3.5-draft` -> `mistral/mistral-medium-3.5`.
- Roles: sanitized coding plans, code review, test strategy, extraction and independent consultation.
- Credential boundary: workspace key is injected by approved secrets mechanism; never committed or logged.
- Spend boundary: staging workspace cap required before inference.

### Mistral Vibe Code plugin / CLI
- Status: permanent optional developer interface after separate installation/configuration review.
- Roles: interactive codebase review, planning, draft implementation and independent consultation.
- Boundary: Vibe is not a bypass around LiteLLM, evidence, approval, data classification or protected-data controls.
- Key boundary: use a dedicated expiring workspace key; rotate/revoke independently from factory routes.

## Consultation ladder

For every material decision fork:
1. Primary analysis: eligible Tier B route selected by task class.
2. Independent Codex consultation: implementation feasibility, testability, repo impact and failure modes.
3. Independent Mistral consultation: alternatives, assumptions, architecture/risk critique.
4. Escalation: Fable 5 is added independently for unresolved material disagreement.
5. Decision record: preserve primary/secondary/tertiary hashes, named reviewers, approval identity and dissent.
6. Execution: Codex performs only the approved change and records diff/test evidence.

## Model roles

- Tier A: Kimi K2.6; exact DeepSeek chat/coder alias once discovered; Mistral Medium 3.5; Mistral Small.
- Tier B: Kimi K3; exact DeepSeek reasoning alias once discovered; Mistral Large; Magistral Medium; optional Fable 5.
- Executor/verifier: Codex plugin/CLI.
- Local-safe: authenticated local aliases only for protected, mixed or unknown data.

## Non-negotiable constraints

- No cloud route for protected, mixed or unknown data.
- No silent cross-provider, cross-tier or cross-boundary fallback.
- No route becomes operational without exact model/alias pinning, F9 validation, positive/negative/rollback proof, immutable evidence and independent approval.
- Mistral and Codex may be permanently available tools, but availability is not automatic authority to execute or approve changes.
