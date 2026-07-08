# BEN Intel — Best-Decision Self-Learning Loop (BDSL) novelty scout

Date: 2026-07-09
Extracted by: BEN (right terminal / document-intelligence)
Source: docs/sources/bdsl-self-learning-loop-2026-07-09.md (read from disk per §7 R5)
Source sha256: 58089f2d1a070d643d203c0b3fb206a41718b6fef37ceeca8fe6720a0a7e7dce (41288B, 707 lines, 11 sections, 25 refs)
Method: BEN document-intelligence per docs/canon/ben-right-terminal-canon.md §4.
Tags: [ФАКТ] explicit in source (§); [ВЫВОД] BEN inference; [НЕИЗВЕСТНО] source silent.

> Provenance: docs/sources/bdsl-self-learning-loop-2026-07-09.md (sha 58089f2d).

## §0 — Three absolute invariants
- [ФАКТ] Append-only immutability; Human-gated activation (APPROVER IAM); Explainability-by-construction (ex-ante).
- [ФАКТ] Theory base: VNM EU, MDP/Bellman, MAUT, Secretary/optimal-stopping, Prospect (K&T 1979), Satisficing (Simon 1978), RLHF, Minimax Regret.

## §1 — DecisionRecord schema (v1.2)
- [ФАКТ] Append-only typed record (Kafka/WORM): decision_space (D+pruned), MAUT criteria (weight/score/norm),
  utility_computation (U=Σw·u, pareto_frontier), chosen (confidence, tier AUTO/REVIEW/BLOCK),
  stopping_rule, bias_flags, minimax_regret, human_review, hash-chain schema_hash+prev_record_hash.
- [ФАКТ] Invariants §1.2: Σweights=1±1e-6; ≥2 feasible; compliance/payment⇒full_search (no satisficing); hash-mismatch→auto-BLOCK.

## §2 — OutcomeRecord + delayed feedback
- [ФАКТ] FK→DecisionRecord; feedback_lag, ground_truth_utility, counterfactual (PSM/IPW/causal-forest), feedback_quality.
- [ФАКТ] Horizons: <1min deterministic → 1-24h intermediate → 1-30d surrogate(SAR) → 30d-12mo causal-forest/IPW → >12mo manual LOW. ESTIMATED w=0.3 vs gt w=1.0.

## §3 — Best-ness metrics (W=90d)
- [ФАКТ] Regret R=U_oracle−U_chosen, ρ_T, R̄≤0.05; MMR; no-regret R̄→0.
- [ФАКТ] Brier BS=1/N·Σ(f−o)²≤0.15; ECE binned ≤0.08; escalation-recall≥0.98, false-esc≤0.10; PER≥0.95; IPW for estimated.

## §4 — Best-Decision Test (BDT) gate
- [ФАКТ] Tiers c≥0.90 AUTO / 0.70-0.90 REVIEW / <0.70 BLOCK; compliance/payment AUTO≥0.95 (Art.14).
- [ФАКТ] Authoring gate (blocking, 500 samples) + Runtime periodic (24h, W=90d); YAML severity CRITICAL/MAJOR/MINOR.
- [ФАКТ] Bias battery §4.3: prospect (gain/loss frame), anchoring (order), omission.

## §5 — Self-learning loop
- [ФАКТ] Never auto-applies → ImprovementProposal → Human Review Queue → APPROVED/REJECTED/DEFERRED.
- [ФАКТ] Proposal schema: evidence, proposed_changes, drift_analysis (PSI), approver_instructions, expiry.
- [ФАКТ] RLHF-analog RM 3-stage: preference-data → RM_θ offline (human-triggered) → policy update after APPROVED (versioned, rollback).
- [ФАКТ] Drift PSI>0.25→proposal; prospect-countermeasures (gains-normalized); satisficing-guard (payment forbidden).

## §6 — Orchestrator (Supervisor)
- [ФАКТ] Manages fleet, no business decisions. Decision Quality Registry, Anomaly Detector (WARN→REVIEW→BLOCK), Re-test Scheduler, Proposal Queue (SLA), Cross-Agent Correlation.
- [ФАКТ] SQL agent_quality_metrics (avg_regret, brier, ece, pareto, escalation_recall, prospect_bias_rate, bdt_status, trend).
- [ФАКТ] Escalation Tier1 log→Tier2 REVIEW+proposal→Tier3 BLOCK+incident→Tier4 CISO+Compliance+regulatory.

## §7 — Rollout Phase 0-3
- [ФАКТ] P0 (m1-2) infra only; P1 (m2-4) factory agents, lowered thresholds; P2 (m4-6) bank informational, full schema+Authoring gate; P3 (m7-12) compliance/payment after P2 PASS≥3mo + conformity + EU-AI-DB reg + pentest, AUTO≥0.95, no satisficing.

## §8 — Compliance
- [ФАКТ] EU AI Act: Art.9 risk-mgmt, Art.14 oversight, Art.15 accuracy, Art.17 QMS, Annex IV tech-doc, Art.49 EU-AI-DB (Aug 2 2026); GDPR Art.22 (AUTO only c≥0.95+low-risk).
- [ФАКТ] EBA 2025 non-contradictory; BaFin human-in-the-loop; 7+y retention; Never-Autonomous list §8.4 (7 items).

## Tails / [НЕИЗВЕСТНО]
- [НЕИЗВЕСТНО] Draft-for-Review methodology — no implementation/hyperparameters.
- [ВЫВОД] Coverage → docs/audit/bdsl-coverage-2026-07-09.md (R4): 1 impl / 3 partial / 10 missing.
- [ВЫВОД] BDSL operationalises ratified best-decision-gate (Q1/Q2) into per-decision auditable pipeline.
