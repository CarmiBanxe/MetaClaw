# BEN Intel — EMI BANXE Engine (novelty scout)

Date: 2026-07-06 (intel); anchor created 2026-07-08
Extracted by: BEN (right terminal / document-intelligence)
Source: docs/sources/emi-banxe-engine-2026-07-06.md
Source sha256: 9ef1b0308d9602a795b408111b1bddb3e127a9728f15b0cc4b3aea4a2257ef34 (49979B, read verbatim)
Method: BEN document-intelligence per docs/canon/ben-right-terminal-canon.md §4.
Tags: [ФАКТ] = explicit in source (with Part §); [ВЫВОД] = BEN inference; [НЕИЗВЕСТНО] = source silent.

> Provenance: Source docs/sources/emi-banxe-engine-2026-07-06.md (sha 9ef1b03).
> This audit entry closes the R1 orphan per ben-right-terminal-canon §7.

---
## 1. Architecture
- [ФАКТ] 7-layer architecture (Part III §3.1): L7 Presentation (assistant-ui/React/Whisper/Coqui) · L6 Orchestration (LangGraph+DeerFlow) · L5 Specialized agents (Composite Tools) · L4 Intelligence (PRAGMA/FinGPT/GNN/FATE) · L3 Memory (Mem0/Zep/Qdrant/LlamaIndex/Redis) · L2 Core Banking (Formance/Blnk/FISCO BCOS) · L1 Infra (Temporal/Kafka/K8s/Strands/SOFAStack).
- [ФАКТ] Two orchestrators (§4.1): LangGraph = realtime (<300ms) + DeerFlow 2.0 = long-horizon (KYC, reports).
- [ФАКТ] Composite Tools (Nubank §3.6): LLM picks tool; transfer is deterministic tool-fn ("LLM does not count money").
- [ФАКТ] Army of specialists (Toss §3.1): Transfer/FX/Compliance/Savings/Analytics/Treasury agents.

## 2. Mathematics
- [ФАКТ] PRAGMA (Revolut+NVIDIA §2.1): token=(semantic_key,typed_value,temporal_coordinate); numeric→percentile buckets; time twice (log-sec+sinusoids); MLM 15/10/10. +130% PR-AUC credit, +65% recall fraud, +40.5% mAP; 24B events/26M users/111 countries; 10M/100M/1B.
- [ФАКТ] nuFormer (Nubank §2.1): DCNv2(x_tab) ⊕ GPT-dec(x_seq); 131M customers, +1.25% AUC, −4.4% churn.
- [ФАКТ] TransactionGPT — 3D-transformer (time/semantic/graph) §2.1.
- [ФАКТ] HGNN (§2.2): e_ij=LeakyReLU(aᵀ[Wh_i‖Wh_j]); temporal-decay h_i(t)=Σ α_ij·e^(−λΔt_ij)·Wh_j.
- [ФАКТ] FraudGNN-RL (GNN+DQN): F1 97.3%, −31% FP; federated variant (§2.2).
- [ФАКТ] ASA-GNN — cosine noise-filter + entropy-diversity + multi-hop (§2.2).
- [ФАКТ] Federated (§2.3): FedAvg w=Σ(n_k/n)w_k; FedKT (Non-IID KD); DP (RDP ε=8.65, ~87-90%); HE-FL ~90%; FATE (WeBank PSI/RSA); VaultGemma (Google 1B DP-LLM).
- [ФАКТ] RL (§2.4): FinRL (AI4Finance MIT); FinRL-DeepSeek s_t=(p_t,f_t,LLM_signal_t).

## 3. Open-source stack
- [ФАКТ] Core (§8.1): LangGraph + Strands + DeerFlow + FinGPT/FinRobot + FATE + Temporal.
- [ВЫВОД] Options: AgenticSeek (offline GDPR), Blnk (light ledger), Mem0/Zep (memory).
- [ФАКТ] ⚠️ AutoGen = CC-BY-NC-4.0 (non-commercial) — blocks commercial bank use; critical adopt-gotcha.
- [ФАКТ] Ledgers: Formance (SEPA/SWIFT), FISCO BCOS (immutable audit, 5000+ orgs); infra Temporal/Kafka; vector Qdrant.

## 4. Security / compliance
- [ФАКТ] EU AI Act decision-lineage (§5.3): ClickHouse agent_decisions → maps to I-24 (append-only 5y).
- [ФАКТ] SHAP/LIME for credit (§5.3): Shapley φ_i for "why rejected".
- [ФАКТ] NeMo Guardrails (§5.2): transfer_requires_confirmation → maps to I-27 (HITL on payment).
- [ФАКТ] OWASP LLM→BANXE (§5.1): excessive-agency→confidence-gate 0.90; overreliance→HITL; model-theft→self-hosted.
- [ВЫВОД] Security section aligns with I-24/I-27/HITL thresholds — low adoption-risk.

## 5. Roadmap (§8.2)
- [ФАКТ] Phase 0 (m1-2) Formance/Blnk+Temporal+Kafka+K8s · Phase 1 (m2-3) LangGraph+TransferAgent · Phase 2 (m3-5) Qdrant+LlamaIndex+FinGPT · Phase 3 (m5-6) Mem0+Zep · Phase 4 (m6-8) HGNN+NeMo · Phase 5 (m8-12) PRAGMA on own data · Phase 6 (m12+) FATE FL + partners.
- [ВЫВОД] Order = infra→agent→intelligence→memory→fraud→foundation→federated; foundation deferred to Phase 5. Explicit rationale thin → partly [ВЫВОД].

## 6. Tails / [НЕИЗВЕСТНО]
- [НЕИЗВЕСТНО] No ADR under any decision — each adopt needs our ADR.
- [НЕИЗВЕСТНО] No hyperparameters for our data.
- [НЕИЗВЕСТНО] No cost/hardware estimate.
- [НЕИЗВЕСТНО] midaz-ledger vs Formance/Blnk conflict/migration not described.
- [ФАКТ→risk] AutoGen non-commercial → per-repo licence audit before adopt.
- [НЕИЗВЕСТНО] Quantum fraud (QGNN §7.4, AUC 0.85 simulator) — experimental, no prod path pre-2027-28.

## 7. EMI-scope flags (B-EMI-CREDIT-GATE-001)
- [ВЫВОД] Out of TOMPAY EMI licence until extension: credit-scoring (PRAGMA-100M credit), lending; TreasuryAgent trading (FinRL); Phase 6 cross-bank scoring (FATE).
- [ВЫВОД] Adopt now: Transfer/FX/Compliance/Savings/Analytics + security/audit patterns (I-24/I-27-aligned).
