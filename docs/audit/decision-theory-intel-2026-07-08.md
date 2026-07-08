# BEN Intel — Decision-Theory Optimal Review (novelty scout)

**Date:** 2026-07-08
**Extracted by:** BEN (right terminal / document-intelligence)
**Source:** `docs/sources/decision-theory-optimal-review-2026-07-08.md`
**Source sha256:** `7fe4718bf0351eb5518e67a3aece6f9a3c4013837721cbdd0301678f41f85f2e` (37286B, read verbatim from disk)
**Method:** BEN document-intelligence per `docs/canon/ben-right-terminal-canon.md` §4.
Tags: [ФАКТ] = explicit in source (with §); [ВЫВОД] = BEN inference; [НЕИЗВЕСТНО] = source silent.

> **Provenance:** Source: `docs/sources/decision-theory-optimal-review-2026-07-08.md` (sha `7fe4718b`).

---

## 0. Source map (by fact)
[ФАКТ] Source = §1–11 (no bibliography section in body; inline-cited review — the "~104 sources" is
not a literal reference list in the file). §1 fundamental def · §2 math (EU/LP/DP/secretary/Pontryagin/Nash)
· §3 multi-criteria (Pareto-NSGA-II/MAUT/AHP-TOPSIS) · §4 beyond-optimization (satisficing/prospect/minimax-regret/fuzzy/stochastic)
· §5 programming-AI (MDP/RL/AlphaGo/RLHF/LLM-DeLLMa/trees-RF/A*) · §6 impossibility (Arrow/Pareto/NP-hard)
· §7 schools table · §8 systems · §9 ethics-GDPR · §10 unified formulation + 6-step algorithm · §11 synthesis map.

## 1. Novelty map (~20 optimality methods)
| Method | Key (formula → applied point) | src [ФАКТ] |
|---|---|---|
| VNM Expected Utility | `EU=∫p(o\|d)·U(o)do`; 4 axioms (completeness/transitivity/continuity/monotonicity) | §2.1 (VNM 1944) |
| LP / Simplex | Dantzig 1947; iterate vertices until `c_j−z_j` optimality; convex → global optimum | §2.2 |
| DP / Bellman | `V(s)=max_a[R(s,a)+γ·ΣP(s'\|s,a)V(s')]`; principle of optimality | §2.3 (late-1950s) |
| Secretary / 37% | reject first `n/e`, take next-best; success `1/e≈0.368` | §2.4 |
| Pontryagin maximum | max Hamiltonian `H(x*,u*,λ*,t)` along optimal trajectory | §2.5 (1956) |
| Nash equilibrium | best-response profile; **not necessarily Pareto** (prisoner's dilemma) | §2.6 |
| Pareto / NSGA-II | non-dominated front; NSGA-II fast-non-dom-sort + crowding | §3.1 (IEEE-TEC 2002, 43k cit; EPFL 2025 relative-robust) |
| MAUT | `U(a_i)=Σ w_j·u_j(x_ij)`, Σw=1 | §3.2 |
| AHP / TOPSIS | AHP Saaty 1970s (pairwise→weights+consistency); TOPSIS geometric distance to ideal/anti-ideal | §3.3 |
| Bounded rationality / satisficing | Simon (Nobel 1978): first "good-enough" ≥ threshold, not optimum | §4.1 |
| Prospect theory | Kahneman-Tversky Econometrica 1979 (Nobel 2002): reference point, loss aversion, prob-weighting | §4.2 |
| Minimax / minimax regret | min worst-case loss; regret = min max forgone-payoff; no probabilities → robust | §4.3 |
| Fuzzy logic | Zadeh 1965: membership degree `[0,1]` vs binary | §4.4 |
| Stochastic opt / Monte Carlo | MC (von Neumann + Ulam, WWII): simulations → confidence intervals | §4.5 |
| MDP / RL | `(S,A,P,R,γ)`, `π*=argmax_a Q*(s,a)`; Q-learning / policy-gradient / DRL | §5.1-5.2 |
| AlphaGo / MCTS | MCTS + policy-net + value-net; Zero 40 days; "intuition" narrows search (≈ secretary explore-sample) | §5.3 (2016) |
| RLHF | reward-model from human prefs + PPO; "best" delegated to human | §5.4 |
| LLM / DeLLMa | LLM = Intelligence/Design/Choice (Simon); ⚠️ omission-bias, framing-dependence | §5.5 |
| Decision trees / Random Forest | Gini/entropy impurity; RF ensemble → variance reduction | §5.6 |
| A* / heuristic search | optimal iff **admissible** heuristic `h(s)` (never over-estimates) | §5.7 |
| Arrow impossibility | 1951; no collective-choice rule satisfies 5 axioms → preference aggregation impossible | §6.1 |

## 2. BANXE applied mapping ([ВЫВОД] — BEN inference)
- MDP/RL → TreasuryAgent, payment routing. ⚠️ EMI-scope-gate (trading/credit/treasury market-decisions).
- MAUT/AHP/TOPSIS → PSP/route/tariff selection (FXAgent, payment-rail) — pure EMI-scope, safe.
- Prospect theory / bounded rationality → client-behaviour modelling, risk-scoring (loss-aversion in churn/fraud).
- Minimax-regret / robust / Monte-Carlo → robust decisions under uncertainty (liquidity, FX, safeguarding).
- RLHF → assistant alignment; pairs with HITL thresholds (>90/70-90/<70) + NeMo Guardrails (engine-doc).
- Fuzzy → fraud/AML thresholds under fuzzy signals (partial sanctions-name match, grey transactions).
- A*/heuristic → agent action-graph planning (multi-step KYC/transfer).
- Satisficing + admissibility (Pontryagin/LP) → theoretical base of the ratified best-decision-gate (satisfice-threshold + admissibility-gate = lexicographic Q1/Q2).

## 3. Link to engine-doc (mathematical foundation)
[ВЫВОД] This review is the theory layer under engine-doc specifics:
- confidence-gate 0.90 (engine §5) ← satisficing-threshold (§4.1) + minimax-regret on error (§4.3).
- PRAGMA/GNN scoring (engine §2) ← MDP/RL optimal policy (§5.1-5.2) + trees/RF (§5.6) baseline.
- FinRL TreasuryAgent (engine §2.4) ← MDP/RL (§5.1-5.2) + robust/stochastic FX (§4.5).
- decision-lineage + SHAP (engine §5.3) ← explainable-AI / GDPR Art.22 (§9); fairness-impossibility ≈ Arrow (§9/§6.1).
- best-decision-synthesis Q1/Q2 (banxe-architecture #1091) ← lexicographic = Pontryagin-admissibility (§2.5) + satisfice (§4.1) over Pareto (§3.1); RLHF (§5.4) = alignment base.

## 4. EMI-scope flags (B-EMI-CREDIT-GATE-001)
[ВЫВОД] Out of TOMPAY EMI licence until extension — adopt only payment/FX/compliance applications:
- RL-**trading** decisions;
- credit-scoring via RL/RF;
- TreasuryAgent **market** decisions.
[ВЫВОД] Arrow (§6.1) + fairness-impossibility (§9): cannot optimise all fairness metrics at once → explicit
operator value-choice required at the adoption-gate (not "mathematically best").

## 5. Tails / [НЕИЗВЕСТНО]
- [ФАКТ] Purely theoretical — no compliance specifics beyond §9 GDPR Art.22; no implementation detail.
- [НЕИЗВЕСТНО] No bibliography in body (promised ~104 sources absent as a list) — academic-traceability gap.
- [ВЫВОД] A future ADR is needed to map §11 method-tree onto concrete BANXE agents.
