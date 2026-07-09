# BEN Coverage Report — AI Model Efficiency Methodology novelties (R4)

Date: 2026-07-09
By: BEN (right terminal / document-intelligence)
Intel source: docs/audit/ai-efficiency-intel-2026-07-09.md
Doc source: docs/sources/ai-efficiency-methodology-2026-07-09.md
Provenance: source sha256 b514e2a18ad31f28 (30827B, 552 lines).
Policy: docs/canon/ben-right-terminal-canon.md §7 R4 (coverage obligation).
Tags: [FACT] verified by marker+context; [INFER] BEN recommendation; [UNKNOWN] not determinable.

## Method note
- [FACT] Statuses by marker analysis (exact metric/schema/function signatures) with context verification
  (prod telemetry vs generic scrape; real metric vs unrelated same-name symbol).
- [FACT] False positives filtered:
  - openrouter_route != throughput metric (routing symbol, not tokens/sec measurement). Rejected.
  - generic Prometheus scrape config != model-level efficiency metric. Rejected.
- Scan: banxe-emi-stack, banxe-monitoring, MetaClaw (excl .git, __pycache__, bundles).

## Coverage table

| Novelty (methodology §) | Status | Evidence (marker+context) | CENTRAL recommendation |
|---|---|---|---|
| Cost / token-usage (§1) | IMPLEMENTED | banxe-emi-stack/services/agent_routing/telemetry.py:75,99 _COST_PER_1K_TOKENS | none — wired |
| LiteLLM gateway (§1) | IMPLEMENTED | banxe-monitoring/prometheus/prometheus.yml (Gap-028) | none |
| Ollama nodes (§1) | IMPLEMENTED | prometheus/rules/llm.yml, nodes.yml | none |
| Model aliases (§4/§5) | IMPLEMENTED | agents/mlro_report_agent/client.py (project-reason qwen3-235b evo2) | none |
| Drift-signal (§3) | PARTIAL | ml_pipeline/ml_signal_port.py get_drift_signals/DriftSignal — but NOT CUSUM/calibration-drift | NON-GATED — extend to CUSUM calibration-drift |
| TTFT (§1) | MISSING | 0 real markers | NON-GATED — instrument on LiteLLM gateway |
| TPOT (§1) | MISSING | 0 | NON-GATED — instrument on LiteLLM gateway |
| E2E latency histogram (§1) | MISSING | 0 | NON-GATED — Art.15 accuracy/robustness |
| Throughput metric (§1) | MISSING | 0 (openrouter_route rejected) | NON-GATED — tokens/sec metric |
| Perplexity / LLM-judge quality (§2) | MISSING | 0 | NON-GATED — Art.15 quality-eval + Brier |
| CUSUM calibration-drift (§3) | MISSING | 0 (only generic drift) | NON-GATED — build atop ml_signal_port |
| EU AI Act logging schema (§7) | MISSING | 0 (measurement_type/tpot_ms/e2e_latency_ms/drift_signal absent) | NON-GATED — Art.12/14 recordkeeping |

## Summary
- IMPLEMENTED: 4 | PARTIAL: 1 | MISSING: 7.
- [INFER] Implemented = cost/gateway/node telemetry (infra observability already live); missing = model-level
  efficiency + quality + EU-AI-Act logging (the regulated-measurement layer).

## EMI-scope — I-27 discipline
- [FACT] I-27: watchdog measures + escalates only; NEVER switches model autonomously.
- [FACT] Therefore ALL recommendations are NON-GATED: they add measurement / observability / logging, NOT
  autonomous model switching or credit/trading decisions. There are NO gated items in this report.

## NON-GATED recommendations to CENTRAL (EU AI Act priority, deadline 2 Aug 2026)
1. [INFER] TTFT / TPOT / E2E-latency instrumentation on the LiteLLM gateway (Art.15 accuracy/robustness).
2. [INFER] EU AI Act efficiency-logging schema §7 (measurement_type/tpot_ms/e2e_latency/drift_signal) — Art.12/14 recordkeeping.
3. [INFER] LLM-judge quality-eval + Brier calibration (Art.15).
4. [INFER] CUSUM calibration-drift atop existing ml_signal_port DriftSignal (complete the PARTIAL).
5. [INFER] Model-comparison MAUT/TOPSIS gate (P99 > SLA -> BLOCKED) at selection time.

## Constraints honoured
- [FACT] BEN wrote no production code (INV-01, Aider = sole executor). Report + recommendations only.
- [FACT] I-27: no recommendation implies autonomous model switching — measurement/escalation only.
