# Factory Terminal — Working Mode v1 (runbook)
Status: Operator-directed. Grounded in CLAUDE_CODE_CANON.md (Rules 3,8; T3.4) +
software-factory-canon-v1.md (§7 loop, §8 approval) + smart-model-routing-protocol-v1.md (§Independence).

## 1. Permissions mode
- Factory Claude Code runs with bypass permissions ON (Rule 8: "APPROVAL MENUS: NEVER SHOW").
- Launch: ANTHROPIC_BASE_URL=<gateway> ANTHROPIC_AUTH_TOKEN=<tok> claude --dangerously-skip-permissions
- Rationale: Stage-2 confirmation menus violate Rule 8; safe patterns auto-approved internally.

## 2. Factory does NOT self-consult (separation of duties)
- The factory terminal PLANS and ROUTES; it never performs its own consultation
  (CLAUDE_CODE_CANON T3.2 "Never self-execute", smart-routing "distinct invocation").
- When a consultation/second-opinion is needed, the factory terminal:
  1. Prepares ONE consultation BRIEF (task, context, question, data-class, expected output).
  2. Emits it as a single OPERATOR_RUN-style handoff line, then STOPS and waits (Rule 3, T3.4).
  3. Does NOT call the consultation model itself.

## 3. Consultation chain (fixed order)
- **Codex** = primary consultant (first opinion)
- **Fable** = second opinion (independent reviewer)
- **Mistral** = third opinion (if分歧 persists)
- **Kimi** = fourth opinion (final escalation)
- Ref: `software-factory-canon-v1.md` §13 for full consult chain specification.

## 4. Operator loop (manual)
- Operator takes the brief to the SEPARATE consultation window (distinct route).
- Operator runs the consultation per §3 chain order, brings results back to factory terminal.
- Factory reconciles opinions into one decision basis, then resumes work.

## 4. Data-class guard
- Consultation via cloud route only for NON-protected data.
- Protected (secrets, KYC/KYB/AML, payment/ledger, prod logs, regulated evidence) -> local-safe (LiteLLM :4000) only. No cross-tier auto-fallback.

## 5. Approval
- No model approves its own work (v6.1). Final approval = Operator; MLRO where regulated scope.
