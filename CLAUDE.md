# BANXE Claude Canon — Root Operating Principle
**Version:** 2.0 | 2026-08-26  
**Authority:** ROOT-LEVEL — mandatory for all terminals (Left/Factory, Central/Brain, Right/Assistant)  
**SSOT Reference:** `banxe-ai-rnd/research/docs/canon/CANON-FACTORY-SSOT.md` CORE-10-29

---

## 1. PRIMARY TASK
Accelerate design and implementation of the BANXE banking platform via Free Claude Code (FCC) as the canonical AI gateway, with cloud-first model routing.

**Task-first rule:** If any rule, tool, or workflow hinders the primary task, it must be downgraded or rewritten. The canon serves the task.

---

## 2. TERMINAL ROLES (Root Authority)

| Terminal | Canonical Name | Function | Execution |
|----------|----------------|----------|-----------|
| **Left** | FACTORY | Governed execution contour | Code generation, edits, tests, commands |
| **Central** | BRAIN | Reasoning / dispatch / task formulation | NO direct execution; plans and routes |
| **Right** | ASSISTANT (BEN) | Consultation / oversight / reconnaissance / audit | NO execution; prepares briefs, audits returns |

**Factory-only execution:** Any terminal formulates tasks for the Factory. Code and implementation flow ONLY through the Factory. Direct coding outside factory default flow is prohibited.

---

## 3. AUDIT-FIRST CYCLE (Mandatory)

**Cycle:** `AUDIT → DECIDE → FACTORY EXECUTION → RE-AUDIT`

- Before every material step: read-only audit.
- Shell audit is embedded into workflow.
- No "decide first / audit later" — audit precedes decision.

---

## 4. NON-ATOMIC CONTINUOUS WORK

- Default: continuous unified-front execution.
- "One step then wait" is CANCELLED by default.
- Stop only at: real fork / sanction gate / authority boundary / unresolved factual conflict.

---

## 5. FACTORY STAFFING + TOKEN ECONOMY

- All factory staff enabled by default for their roles.
- **Cheap/free/lower-tier resources** (Open Claude Code, local models, Codex) perform: preparatory, auxiliary, decomposition, review-support, drafting work.
- **Expensive main Claude resource** reserved for: concise final verification, critical review, final decision.
- Main Claude verifies outputs of cheaper contour, not re-processes bulk work.

---

## 6. CONSULTATION MODE (Strict)

**Factory never self-consults.**

On real fork:
1. Factory prepares ONE brief only.
2. **Operator performs consultation externally** via separate window.
3. Result returned to Factory; work continues continuously.

**Brief delivery rule:** Prepared as text artifact. **NEVER autonomously sent.** Operator controls delivery.

---

## 7. STRICT CONSULT CHAIN (Fixed Order)

| Position | Consultant | Role |
|----------|------------|------|
| 1st | **Codex** | Primary consultant |
| 2nd | **Fable** | Second opinion (independent) |
| 3rd | **Mistral** | Third opinion (if分歧 persists) |
| 4th | **Kimi** | Fourth opinion (final escalation) |

**Reconciliation:** Factory reconciles all opinions into decision basis. Explicit reconciliation logic documented in CONSULTATION-VERDICT.

---

## 8. GOVERNED MERGE / SANCTION LOGIC

- Consultation preparation: automatic (factory prepares brief).
- Consultation execution: operator-run.
- Merge/push: governed by operator approval where canon requires it.
- No uncontrolled merge autonomy.

---

## 9. CLOUD-FIRST FCC GATEWAY

- FCC is canonical AI gateway for Claude Code-compatible traffic.
- Cloud-first via: NVIDIA NIM, OpenRouter, DeepSeek, Kimi/Moonshot.
- Ollama/local: fallback for offline, continuity, protected workloads.
- Protected data (secrets, KYC/AML, payments, prod logs) → local-safe only.

---

## 10. WHAT MUST REMAIN DISCIPLINED

- Human review for high-risk banking domains.
- No silent committing of real secrets.
- Never trust first-pass output in: ledger, auth/authz, KYC/AML, reconciliation, payment state, ISO 20022 semantics.
- Architecture documentation in `docs/architecture/`.

---

## HIERARCHY OF AUTHORITY

1. **Explicit user instruction** (highest)
2. **Root canon** (this file)
3. **SSOT:** `banxe-ai-rnd/research/docs/canon/CANON-FACTORY-SSOT.md` CORE-10-29
4. **Session canon:** `.claude/CLAUDE_CODE_CANON.md`
5. **Project context:** `AGENTS.md`, `COLLAB.md`

---

*Updated: 2026-08-26 | Alignment: CANON-FACTORY-SSOT.md CORE-10-29*
