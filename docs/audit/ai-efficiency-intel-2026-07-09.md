# BEN Intel Report — AI Model Efficiency Methodology (BANXE EMI)

Date: 2026-07-09
By: BEN (right terminal / document-intelligence)
Provenance: docs/sources/ai-efficiency-methodology-2026-07-09.md (sha256 b514e2a18ad31f28), 30827B, 552 lines, 10 sections.
R8 note: source landed via cp + sha256 (ZERO-LOSS verified — ideal path, no chat re-paste, no chunk assembly).
Policy: docs/canon/ben-right-terminal-canon.md §7 R1-R5/R8 (provenance / audit-before-commit / single-entry / integrity).
Tags: [FACT] = explicit in source (cited); [INFER] = BEN inference; [UNKNOWN] = source silent.

## Scope
- [FACT] Methodology for measuring AI-model efficiency inside a regulated bank (EMI).
- [FACT] Anchored to EU AI Act Art.9-15 (Art.12 recordkeeping, Art.14 human oversight, Art.15 accuracy/robustness);
  compliance deadline 2 Aug 2026.
- [FACT] I-27 invariant: the watchdog ONLY measures + escalates; it NEVER switches the model autonomously.
  FC_score < 1 -> append-only escalation record -> human decision.

## Novelties by section

### §1 Metric taxonomy (operational + quality)
- [FACT] Operational metrics with formulas:
  - TTFT (time-to-first-token), TPOT (time-per-output-token), E2E latency (end-to-end request), Cost (per-1k-token).
- [FACT] Target table: TTFT <= 500ms (fast tier), TPOT <= 50ms/token.
- [FACT] Quality metrics: task-level correctness / calibration (separate axis from operational).

### §2 Automated quality measurement
- [FACT] LLM-judge for automated quality scoring.
- [FACT] PR-AUC preferred over ROC-AUC when prevalence < 5% (rare-event / fraud-like imbalance).
- [FACT] Brier score target <= 0.1 (calibration quality).
- [FACT] Temperature scaling / Platt scaling for probability calibration.

### §3 Drift detection
- [FACT] CUSUM for calibration-drift detection over sliding windows.
- [INFER] Distinct from generic ml drift-signal: methodology specifies calibration-drift (not just feature/data drift).

### §4 Model comparison / selection
- [FACT] MAUT / TOPSIS / Pareto multi-criteria comparison across models.
- [FACT] Hard gate: P99 latency > SLA -> model BLOCKED (fail-closed at selection time).

### §5 Bank thresholds
- [FACT] Bank-specific thresholds (w_j weights, q_critical) drive the FC_score.
- [FACT] FCA/PRA SS1/23 Model Risk: weights/thresholds affecting material decisions need independent model
  validation before activation.

### §6 Fail-closed escalation (I-27)
- [FACT] Fail-closed: FC_score < 1 -> escalation record -> human. No autonomous switch.
- [FACT] Minimax-regret decision framing for concept-drift response.

### §7 Logging schema (EU AI Act Art.12/14)
- [FACT] Efficiency-logging schema fields: measurement_type, tpot_ms, e2e_latency_ms, tokens, drift_signal.
- [INFER] Append-only record-keeping satisfies Art.12 (logging) + Art.14 (human-oversight trace).

## Handoff to CENTRAL
- [INFER] All novelties are proposals — CENTRAL decides via promote/defer + approval gate.
- [FACT] BEN wrote no production code (INV-01). Coverage + recommendations in docs/audit/ai-efficiency-coverage-2026-07-09.md.
- [FACT] I-27 discipline: every recommendation is measurement/observability only, NOT autonomous model switching.
