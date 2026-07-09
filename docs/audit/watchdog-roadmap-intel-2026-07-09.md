# BEN Intel — Banxe Watchdog Production-Roadmap (novelty scout)

Date: 2026-07-09
Extracted by: BEN (right terminal / document-intelligence)
Source: docs/sources/banxe-watchdog-production-roadmap-2026-07-09.md (read from disk per R5)
Source sha256: c42811cde4c2d3360086b2765feff44a9d5851d69a694a9b4e5e29aecc877fd4 (34570B, 416 lines)
Co-anchor ADR: banxe-architecture/docs/adr/ADR-141-self-healing-continuous-learning-loop.md, ADR-126-hermes-tier1-cicd-watchdog-role.md
Method: BEN document-intelligence per docs/canon/ben-right-terminal-canon.md section 4.
Tags: [FACT] explicit in source; [INFER] inference; [UNKNOWN] source silent.

Provenance: FULL source — all 10 parts delivered and assembled via R5 chunking Variant A; 10/10 anchors verified (sha c42811cd). Part 3 = embedded Wave-2 RED factory-prompt (mixed document).

## Watchdog novelties

- [FACT] Tier model: Tier-1 Reactive, Tier-2 Diagnostic, Tier-3 Orchestrated.
- [FACT] Autonomy classes SAFE / GUARDED / MANUAL-ONLY. Criterion = compliance-risk, not technical capability.
- [FACT] Root-cause classifier: exit-code table (137 OOM-kill, 127 cmd-not-found, 1 generic, 0 clean, 143 SIGTERM) + LOG_PATTERNS regex + confidence-scoring.
- [FACT] Crash-loop cascade: N_fast immediate restart -> N_backoff exponential backoff -> circuit OPEN + quarantine. config_loader startup-validation removes hardcoded threshold=10.
- [FACT] Prometheus watchdog_exporter: banxe_component_health, circuit_breaker_state, container_restarts_total + 7 alert-rules + predictive (restart-trend, memory predict_linear, replication-lag, LiteLLM-error).
- [FACT] Dead-man-switch: internal HEARTBEAT_GAUGE main_loop + external guardian on evo2; split-brain: local-only repair, guardian read-only.
- [FACT] Q6 multi-vantage node_reachability: NODE_DOWN (0/N vantages) vs NETWORK_PARTITION (partial) + Wake-on-LAN GUARDED (non-payment/non-stateful, 2-3min recheck else ESCALATE).
- [FACT] Q7 Alertmanager: grouping / inhibition / silences + EscalationEvent (root_cause + confidence + recommended_action + audit_id).
- [FACT] Q8 immutable audit: audit.jsonl append-only, prev_entry_hash chain, chattr +a, S3 Object-Lock WORM, verify_audit_chain, PCI DSS Req 10.
- [FACT] Q9 Vault AppRole: read-only KV + short-lived token TTL=1h + Vault-Agent sidecar (watchdog-policy.hcl deny write).
- [FACT] Blueprint (section 11): evo1 pipeline + evo2 guardian + external Alertmanager / Vault-HA / S3.
- [FACT] Roadmap (section 12): 4 sprints / 16 items.

## Embedded prompt (part 3 — not a watchdog section)

- [FACT] Wave-2 RED Decision Method (Profile-EMI, ADR-030): 4 RED agents, status PROPOSED, activation-gated (red_activation_check + Operator + MLRO SMF17 + CEO SMF1), advisory-prohibited, B5-IRREVOCABLE (crypto_custody on-chain, consent_management PSD2 Art.66).
- [INFER] This is an operational factory-prompt embedded in the roadmap, not a watchdog capability; flagged so CENTRAL does not treat it as watchdog scope.

## Tails / [UNKNOWN]

- [FACT] All 10 parts delivered; source is FULL (sha c42811cd).
- [INFER] Coverage vs code -> docs/audit/watchdog-roadmap-coverage-2026-07-09.md (R4).
