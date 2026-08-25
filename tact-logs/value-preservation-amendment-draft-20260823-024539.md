# Value-Preservation Amendment Draft

**Status:** Draft for independent review; no runtime activation.
**Goal:** Preserve enforcement, evidence, reproducibility, and BANXE domain quality while keeping cloud-first, role-based model routing fully available.

## Retain unchanged
- Canon/README/skills preflight and recorded task evidence.
- Guardian/canon-judge infrastructure and regression tests.
- Backup, dry-run, staged activation, rollback, kill-switch and audit evidence.
- Pinned sources, lockfiles, hashes, signatures, dependency provenance and SBOM where available.
- Synthetic/sanitized-data workflow and protected-data local-safe route.
- BANXE domain invariants: double-entry ledger, CQRS/event sourcing, ISO 20022 boundary, KYC/AML orchestration, and independent MLRO branch.

## Adapt, do not remove blindly
- Legacy guardian checks mentioning local-only inference, Aider as sole executor, or LiteLLM gateway-only routing.
- Replace each with a testable Smart Model Routing Protocol equivalent:
  1. task preflight evidence exists;
  2. route is explicit and model/provider is allowlisted;
  3. protected data stays on local-safe route;
  4. no automatic cloud/local trust-tier crossing;
  5. material decisions have primary analysis, independent review, reconciliation, and required human approval;
  6. provider/runtime activation requires pinned build, synthetic test, rollback test, spend/egress controls.

## Do not restore
- Blanket no-cloud prohibitions.
- Aider-only or any sole-executor requirement.
- A single mandatory vendor/model.
- Gateway-only wording that prevents FCC cloud-first development.

## FABLE-5 DEPTH PARITY
For a material decision: preserve the detailed primary analysis, obtain a separate independent Codex opinion, record it verbatim, then publish a reconciliation that identifies agreement, disagreement, and the selected decision.

## Requested Codex review
Identify any missing high-value legacy safeguards and specify the minimal guardian-rule/test changes needed to enforce this amendment without reintroducing model or provider restrictions.
