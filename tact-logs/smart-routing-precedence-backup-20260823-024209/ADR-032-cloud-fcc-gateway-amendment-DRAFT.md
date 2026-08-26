# ADR-032: Cloud/FCC Gateway Amendment — DRAFT

**Status:** APPROVED BY OPERATOR DIRECTIVE — implementation staged  
**Created:** 2026-08-23T02:23:23.656012+02:00  
**Owner:** Operator (Moriel Carmi)  
**Required approvals:** Operator + designated CTIO  
**Scope:** Amendment to software-factory-canon-v1.md §§3, 5, 7, 11 and ADR-031.

## Decision requested

Permit an explicitly governed cloud-capable inference route for approved non-production AI workloads through an approved local gateway boundary, while preserving a local LiteLLM route as a fallback.

## Current conflict

- INV-02 currently names LiteLLM as gateway-only and prohibits direct Ollama calls by agents.
- INV-03 currently prohibits cloud LLM calls.
- FCC/cloud-first drafts are not canonical and conflict with both invariants.
- FCC source pre-check: GitHub-verified commit `f8a3b119972532c3204b7f0aae2ab1076bc1cf02`; installer and server not run.

## Proposed route boundary

1. Gateway: FCC may operate only as a local, loopback-bound Claude-compatible proxy.
2. Cloud routes: opt-in allowlist only; default deny; no automatic provider fallback across trust tiers.
3. Local route: LiteLLM remains available as an independently operable local fallback.
4. Workload policy: no customer data, secrets, production logs, regulated evidence, or payment/ledger payloads to cloud routes.
5. Secrets: provider credentials only in local secret manager/FCC Admin UI; never Git, prompts, shell history, or audit reports.
6. Execution: Aider remains sole code executor unless INV-01 is separately amended.
7. Audit: route/model/provider/task-ID recorded for every cloud request; retention and access policy defined before production use.
8. Kill switch: stop FCC listener, revoke provider credential, and route all agents to LiteLLM local aliases.
9. Rollback: restore prior gateway environment; confirm no cloud credentials remain exposed; retain evidence pack.

## Preconditions before activation

- [ ] CTIO appointed by Operator.
- [ ] Operator + CTIO signatures recorded below.
- [ ] ADR-031 and canon wording amended consistently.
- [ ] FCC installed in a disposable isolated environment, not global tool environment.
- [ ] Loopback-only listener, non-privileged user, no systemd/autostart.
- [ ] Provider allowlist, egress rules, spend/quota limits, data-classification policy approved.
- [ ] Security review of dependency lockfile and runtime network destinations completed.
- [ ] End-to-end test uses synthetic non-sensitive prompt only.
- [ ] Rollback test completed and evidence attached.

## Explicit non-decisions

- No automatic deletion of local models.
- No provider API key entry by an agent.
- No FCC installation, server start, or cloud request until this ADR is approved.
- No change to production banking systems under this ADR.

## Approval record

| Role | Name | Decision | Date/time | Signature/reference |
|---|---|---|---|---|
| Operator | Moriel Carmi | PENDING | | |
| CTIO | TO_BE_DESIGNATED | PENDING | | |

## Effective condition

This draft has no operational effect until both approval rows are completed and the corresponding canonical amendments are committed, reviewed, and promoted.


## Operator directive recorded

- **Recorded:** 2026-08-23T02:31:41.563497+02:00
- **Decision:** Remove blanket local-only/cloud prohibition for development; adopt cloud-first development through FCC with the stated local-safe-data boundary.
- **Implementation status:** Canon wording updated; FCC runtime/provider activation remains separate, staged, and audited.

> **Smart Model Routing:** `docs/canon/smart-model-routing-protocol-v1.md` is the governing role, trust-tier, preflight, and independent-review protocol for this document.
