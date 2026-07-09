# BEN Intel Report — EMI BANXE Engine v2 (DELTA)

Date: 2026-07-09
By: BEN (right terminal / document-intelligence)
Provenance: docs/sources/emi-banxe-engine-v2-2026-07-09.md (sha256 3fb98168), 1253 lines, 47 References.
Note: body == engine-doc v1 (sha 9ef1b03); core novelties see docs/audit/engine-doc-intel-2026-07-06.md.
      This file = DELTA (novelties NOT in v1-intel) + References 1-47.
Policy: docs/canon/ben-right-terminal-canon.md §7 R1-R4 (no orphan / provenance / audit-before-commit / coverage).
Tags: [ФАКТ] = explicit in source (cited); [ВЫВОД] = BEN inference; [НЕИЗВЕСТНО] = source silent.

## Scope discipline
- [ФАКТ] v2 body is byte-identical to engine-doc v1 (sha 9ef1b03) with an appended References 1-47 block.
- [ВЫВОД] Therefore v1 intel (docs/audit/engine-doc-intel-2026-07-06.md) is REUSED verbatim; only the
  delta below (frameworks/tooling surfaced by the References block + comparison table) is new.

## DELTA novelties (not present in v1-intel)

### Meta-orchestration / agent frameworks
- [ФАКТ] Manus AI — meta-orchestrator agent; source cites GAIA benchmark 86.5%.
- [ФАКТ] OpenManus — open 3-layer agent stack, MIT-licensed (open re-implementation of Manus).
- [ФАКТ] DeerFlow 2.0 (bytedance/deer-flow, Ref 46) — Supervisor-harness for long-horizon tasks, built on LangGraph.
- [ФАКТ] AgenticSeek — offline / local-first agent, framed as GDPR-friendly (no cloud egress).
- [ФАКТ] Suna — open-source generalist agent runtime (research-grade).

### Framework comparison table (source-provided)
- [ФАКТ] CrewAI (~29k stars) — multi-agent role/crew orchestration.
- [ФАКТ] Agno — lightweight agent framework.
- [ФАКТ] MetaGPT (~46k stars) — multi-agent SOP/software-company metaphor.
- [ФАКТ] Strands — AWS agent framework.
- [ФАКТ] LangGraph (~12k stars) — StateGraph-based durable agent orchestration.
- [ФАКТ] AutoGen — licensed CC-BY-NC (non-commercial); [ВЫВОД] licence blocks commercial EMI use.

### Observability / prompt tooling
- [ФАКТ] Langfuse — LLM observability (traces, evals, cost/latency) for agent pipelines.
- [ФАКТ] DSPy — programmatic prompt optimisation / compilation.
- [ФАКТ] GitHub Agentic Workflows — agentic CI/CD (agents acting inside pipeline automation).

### Quantum / distillation research
- [ФАКТ] QGNN Quantum Fraud (Ref 45, arXiv 2309.01127) — quantum graph neural net for financial fraud detection.
- [ФАКТ] Temporal Knowledge Distillation — PRAGMA-1B -> 10M compression; source gives an L_KD (distillation loss) formula.

## References 1-47 (retained on disk per R1/R5)
- [ФАКТ] Source carries a numbered References block (1-47), incl. Ref 45 (QGNN arXiv 2309.01127),
  Ref 46 (bytedance/deer-flow), Ref 47 (FinRobot / ai4finance-foundation). Full list on disk in the source.
- [ВЫВОД] References justify each delta novelty above; they earn the source its committed place (R1 no-orphan).

## Handoff to CENTRAL
- [ВЫВОД] All 12 delta markers are proposals, not adopted — CENTRAL decides via promote/defer + approval gate.
- [ФАКТ] BEN wrote no production code (INV-01). Coverage + gating in docs/audit/engine-v2-coverage-2026-07-09.md.
