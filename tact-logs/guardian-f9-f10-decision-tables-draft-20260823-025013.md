# Guardian F9/F10 Role-Based Routing Decision Tables — Draft

**Status:** Draft for independent review; no runtime activation and no Guardian implementation change.
**Authority:** Smart Model Routing Protocol v1 governs role, route, trust-tier, evidence, and approval semantics.

## Scope

This specification replaces only brand-bound semantics in F9/F10. It preserves all unrelated Guardian rules and does not restrict any approved provider, model, or implementation tool.

## Common task evidence schema

Every new execution-capable task record must include:
- `task_id`
- `route_id` and `route_allowlisted=true`
- `role`: `planner`, `preparation`, `executor`, `reviewer`, or `approver`
- `data_class`: `public`, `synthetic`, `sanitized_internal`, or `protected`
- `trust_tier`: `cloud` or `local_safe`
- `invocation_id`
- `parent_invocation_id` where applicable
- `reroute_id` and immutable evidence reference if route changes
- `actor_identity` or accountable role identity

A material-decision record additionally requires primary-analysis hash, reviewer-analysis hash, reconciliation reference, identified Operator approval, and named MLRO approval where applicable.

## F9: route and trust-tier validation

| Condition | Verdict | Reason |
|---|---|---|
| Required routing fields present; route allowlisted; role compatible with route; data class permitted in trust tier | PASS | Explicit, policy-compliant route |
| Missing/unknown `route_id`, role, data class, trust tier, invocation ID, or allowlist status | DEFER | Fail closed until planner records explicit classification |
| `protected` data with `cloud` trust tier | BLOCK | Protected-data local-safe boundary |
| Cloud/local trust tier changes without immutable reroute evidence and explicit reclassification | BLOCK | Silent cross-tier fallback forbidden |
| Route not allowlisted or route/model capability not approved for requested role | BLOCK | Route governance failure |
| Quota/provider failure with recorded reroute and reclassification | PASS | Explicit continuity handling |

## F10: role separation and decision control

| Condition | Verdict | Reason |
|---|---|---|
| Non-material task has distinct planner and executor invocation; review optional under task policy | PASS | Normal delivery route |
| Material task has primary-analysis invocation, independent reviewer invocation, reconciliation, identified approver, and MLRO approval if applicable | PASS | Independent material-decision control |
| Same invocation holds planner and executor roles | BLOCK | Incompatible role collision |
| Same invocation holds executor and reviewer roles for its own output | BLOCK | Self-review prohibited |
| Same invocation holds primary analysis and independent-review roles | BLOCK | Independent-review failure |
| Same invocation holds reviewer and approver roles for material decision | BLOCK | Approval independence failure |
| Required role/evidence/approval absent or unknown | DEFER | Fail closed until evidence is complete |

## Legacy-evidence migration rule

Historical records that lack F9/F10 fields remain readable and auditable. They must be tagged `legacy_evidence=true`; they cannot authorize new execution, promotion, provider activation, or material-decision approval until an append-only migration record supplies the missing classification, route, role identity, and approval evidence. Migration must never fabricate historical facts; unknown values remain explicitly `unknown`.

## BANXE non-regression gate

F9/F10 migration must not weaken these domain invariants:
- double-entry balance and immutable ledger history;
- CQRS/event-sourcing boundaries and idempotent command handling;
- ISO 20022/payment adapter boundary;
- KYC/KYB/AML orchestration;
- named and independent MLRO approval for applicable regulated/compliance decisions.

## Required synthetic test matrix

1. Approved cloud route for synthetic/public/sanitized work.
2. Approved local-safe route for protected work.
3. Unknown field -> DEFER.
4. Protected data -> cloud -> BLOCK.
5. Silent cloud/local cross-tier fallback -> BLOCK.
6. Explicit reroute with immutable evidence -> PASS.
7. Planner/executor collision -> BLOCK.
8. Executor/reviewer collision -> BLOCK.
9. Primary-analysis/reviewer collision -> BLOCK.
10. Reviewer/approver collision for material decision -> BLOCK.
11. Material decision with complete reconciliation and approvals -> PASS.
12. Legacy record is readable but cannot authorize new execution until migrated.
13. BANXE synthetic balance, idempotency, immutable-history, ISO 20022 boundary and MLRO-independence non-regression tests.
14. Quota/egress ceiling, kill-switch, synthetic E2E and rollback evidence checks.
