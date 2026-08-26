# Factory Terminal — Working Mode v2 (runbook)
**Version:** 2.0 | 2026-08-26  
**Status:** Operator-directed  
**Authority:** Defers to Root Canon (`CLAUDE.md` v2.0) and SSOT CORE-10-29

---

## 1. Permissions Mode

Factory Claude Code runs with bypass permissions ON (Rule 8: "APPROVAL MENUS: NEVER SHOW").

Launch: `ANTHROPIC_BASE_URL=<gateway> ANTHROPIC_AUTH_TOKEN=<tok> claude --dangerously-skip-permissions`

Rationale: Stage-2 confirmation menus violate Rule 8; safe patterns auto-approved internally.

---

## 2. Factory Does NOT Self-Consult (Separation of Duties)

**Root Canon §6:** Factory NEVER self-consults.

When consultation needed:
1. Factory prepares **ONE consultation BRIEF** (task, context, question, data-class, expected output).
2. Emits as text artifact, **STOPS** (Root Canon §6; CLAUDE_CODE_CANON.md Rule 3).
3. **Does NOT call consultation model itself.**

---

## 3. Consult Chain (Fixed Order)

**Root Canon §7 — Strict Consult Chain:**

| Position | Consultant | Role |
|----------|------------|------|
| 1st | **Codex** | Primary consultant |
| 2nd | **Fable** | Second opinion (independent) |
| 3rd | **Mistral** | Third opinion |
| 4th | **Kimi** | Fourth opinion (final escalation) |

Factory reconciles all opinions into decision basis.

---

## 4. Operator Loop (Manual)

**Root Canon §6–8:**

1. Factory prepares brief → emits as text artifact.
2. **Operator controls delivery** — NEVER autonomously sent.
3. Operator takes brief to **SEPARATE consultation window** (distinct route).
4. Operator executes consult chain per §3 order.
5. Operator brings results back to Factory.
6. Factory reconciles and resumes continuous work.

---

## 5. Data-Class Guard

- Cloud route: NON-protected data only.
- Protected (secrets, KYC/KYB/AML, payment/ledger, prod logs) → **local-safe** (LiteLLM :4000) only.
- No cross-tier auto-fallback for protected data.

---

## 6. Approval

**Root Canon §8:** No model approves its own work.

Final approval: Operator; MLRO where regulated scope.

---

## HIERARCHY

1. Explicit user instruction
2. **Root Canon** (`CLAUDE.md` v2.0)
3. **SSOT:** `banxe-ai-rnd/research/docs/canon/CANON-FACTORY-SSOT.md` CORE-10-29
4. **Session Canon** (`.claude/CLAUDE_CODE_CANON.md`)
5. **This file** (operational runbook)

---

*Updated: 2026-08-26 | Alignment: Root Canon v2.0 / SSOT CORE-10-29*
