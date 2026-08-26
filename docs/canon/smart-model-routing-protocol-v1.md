# Smart Model Routing Protocol v2
**Version:** 2.0 | 2026-08-26  
**Status:** Effective — Operator-directed cloud-first development policy  
**Applies to:** All tasks in MetaClaw and Banxe demo-fintech programme  
**Authority:** Defers to Root Canon (`CLAUDE.md` v2.0) and SSOT CORE-10-29

---

## Purpose

Maximize engineering capability by routing each task to best available model while keeping protected banking data local-safe.

---

## Mandatory Preflight

Before planning/execution, read:
1. Root Canon (`CLAUDE.md` v2.0)
2. Software Factory Canon
3. Applicable skills/runbooks
4. Task classification and data sensitivity

---

## Routing Roles (Aligned with Root Canon)

| Role | Route | Purpose |
|------|-------|---------|
| **Preparation / bulk work** | Cheap/free/lower-tier (Open Claude Code, local, Codex) | Research, summaries, decomposition, drafting, fixtures |
| **Primary coding** | Factory (Aider/Codex) | Code generation, patches, tests, refactors |
| **Architecture / reasoning** | High-reasoning models | ADRs, contracts, threat modelling, design review |
| **Independent review** | **Fable** (fixed role per consult chain) | Challenge assumptions, gaps, material changes |
| **Consult chain** | `Codex → Fable → Mistral → Kimi` | Fork resolution (Root Canon §7) |
| **Local-safe** | LiteLLM to approved local endpoints | Protected workloads, offline, private review |

---

## Token Economy (Root Canon §5)

- **Cheap/free tier:** preparatory, auxiliary, decomposition, review-support, drafting.
- **Expensive tier:** concise final verification, critical review, final decision.
- Main Claude verifies Factory outputs, not re-processes bulk.

---

## FCC and LiteLLM

- **FCC:** Canonical gateway for Claude Code-compatible traffic.
- **LiteLLM:** Approved local-safe and continuity route.
- Claude Code: planner/orchestrator.
- Factory: execution layer.

---

## Data and Trust Tiers

| Tier | Data | Route |
|------|------|-------|
| Public / synthetic | Docs, public APIs, fixtures | Cloud via FCC |
| Internal | Configs, non-sensitive code | Cloud via FCC |
| Protected | Secrets, KYC/AML, payments, prod logs | **Local-safe only** |

---

## Consult Chain Trigger

**Root Canon §6–7:**

1. Real fork detected → Factory prepares brief.
2. **Operator runs consult chain externally:** `Codex → Fable → Mistral → Kimi`.
3. Factory reconciles opinions.
4. Work resumes continuously.

**Prohibited:** Factory self-consult, autonomous dispatch.

---

## HIERARCHY

1. Explicit user instruction
2. **Root Canon** (`CLAUDE.md` v2.0)
3. **SSOT:** `banxe-ai-rnd/research/docs/canon/CANON-FACTORY-SSOT.md` CORE-10-29
4. Software Factory Canon
5. **This file** (routing protocol)

---

*Updated: 2026-08-26 | Alignment: Root Canon v2.0 / SSOT CORE-10-29*
