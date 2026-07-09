# BEN Coverage Report — Watchdog Roadmap novelties vs code (R4)

Date: 2026-07-09
By: BEN (right terminal / document-intelligence)
Intel source: docs/audit/watchdog-roadmap-intel-2026-07-09.md
Doc source: docs/sources/banxe-watchdog-production-roadmap-2026-07-09.md (sha c42811cd, FULL)
Co-anchor ADR: ADR-141-self-healing-continuous-learning-loop, ADR-126-hermes-tier1-cicd-watchdog-role
Policy: per ben-right-terminal-canon.md section 7 (R1-R6).
Tags: [FACT] marker+context verified; [INFER] recommendation.

Method note: marker-analysis + context-verify across banxe-ai-infrastructure, banxe-emi-stack,
banxe-emi-stack-main, MetaClaw (excl .git, wt, __pycache__, bundle, docs/sources, docs/audit).
False positives filtered: retry-backoff != watchdog circuit-breaker; RL compute_advantages != network vantage;
"heartbeat" string in metaclaw/utils.py prompt != heartbeat mechanism.

## Coverage table

| Novelty | Status | Evidence | CENTRAL recommendation |
|---|---|---|---|
| Alertmanager | IMPLEMENTED | banxe-ai-infrastructure/banxe-monitoring/docker-compose.yml (prom/alertmanager:v0.27.0) | keep; add watchdog alert-rules |
| Audit hash-chain | IMPLEMENTED | banxe-emi-stack/api/routers/audit_trail.py:91,112 (chain_hash) | extend to watchdog actions |
| Circuit-breaker | PARTIAL | banxe-emi-stack/services/webhook_orchestrator/ (webhook CB, not watchdog) | generalize to watchdog crash-loop cascade |
| Root-cause classifier | MISSING | 0 | implement exit-code+log-regex (Tier-2) |
| Crash-loop config | MISSING | 0 | config_loader CrashLoopConfig, remove hardcode threshold=10 |
| Watchdog-exporter | MISSING | 0 | banxe_component_health + 7 alert-rules |
| Dead-man-switch/heartbeat | MISSING | 0 | HEARTBEAT_GAUGE + guardian evo2 (remove SPOF) |
| Watchdog-guardian evo2 | MISSING | 0 | external dead-man-switch |
| Wake-on-LAN | MISSING | 0 | GUARDED WoL for Legion |
| Vault AppRole | MISSING | 0 | read-only sidecar (watchdog-policy.hcl) |
| systemd watchdog unit | MISSING | 0 | banxe-watchdog.service Restart=always |
| repair-engine SAFE | MISSING | 0 | warm_model/start_container engine |
| node-reachability/vantage | MISSING | 0 | multi-vantage NODE_DOWN vs NETWORK_PARTITION |

## Summary
2 IMPLEMENTED / 1 PARTIAL / 10 MISSING (13 novelties).

## EMI-scope GATED (B-EMI-CREDIT-GATE-001 + PCI DSS Req 6.4)
[INFER] hyperswitch/payment-router auto-repair, ALTER USER, CDE components -> MANUAL-ONLY. Do NOT recommend auto-actions.

## NON-GATED recommendations to factory (priority compliance -> reliability -> safety)
1. root_cause_classifier.py (exit-code + log-regex) — Tier-2 diagnostic.
2. watchdog_exporter.py (banxe_component_health) + 7 alert-rules + guardian dead-man-switch — observability/SPOF.
3. config_loader.py (CrashLoopConfig, backoff/circuit) — remove hardcode threshold=10.
4. watchdog audit hash-chain over existing audit_trail chain_hash — PCI DSS Req 10.
5. Vault AppRole read-only sidecar (watchdog-policy.hcl) — secrets Q9.
6. systemd banxe-watchdog.service Restart=always.
7. node_reachability multi-vantage (Legion NODE_DOWN vs NETWORK_PARTITION).

## Constraints honoured
[FACT] BEN wrote no production code (INV-01). Report + recommendations only. GATED novelties not recommended for immediate build.
