# FABLE-5 SECOND OPINION

**Role:** Independent second opinion (no anchoring to primary)
**Date:** 2026-08-26
**Brief:** Canon Consolidation Fork

---

## Q1: Preferred integration method?

**Answer:** Manual extraction of 11e43f9

**Reasoning:**
- Cherry-pick 11e43f9 создаёт implicit dependency на 17e9a68 (parent commit)
- 17e9a68 содержит re-implementation A+B rules, что создаёт semantic conflict с 277c751
- Manual extraction даёт чистый provenance без скрытых зависимостей
- Provenance сохраняется через explicit attribution в commit message

**Risks of cherry-pick:**
- Silent merge conflict при future integration
- Дублирование логики (A+B rules в 17e9a68 vs 277c751)
- Непредсказуемое поведение при последующих rebase

---

## Q2: How resolve Aider vs Codex executor conflict?

**Answer:** Role separation, not precedence

**Proposed resolution:**
- **Aider:** Автоматизация рутиных задач (lint, format, scaffold)
- **Codex:** Архитектурные решения, сложный рефакторинг, code review
- **Trigger:** Оператор явно указывает executor; при неопределённости — Codex

**Reasoning:**
- Aider оптимизирован для volume, Codex — для quality
- INV-01 создан для предсказуемости, но устарел по сравнению с возможностями Codex
- Role separation сохраняет предсказуемость без artificial restriction

**Risks:**
- Требует явной документации ролей
- Оператор должен помнить mapping

---

## Q3: SSOT restoration priority?

**Answer:** Clone external repo to ../research/

**Reasoning:**
- Local copy требует manual sync и будет stale
- Inline критические секции создаёт divergence risk
- Clone сохраняет git provenance и позволяет diff/merge

**Implementation:**
```bash
git clone git@github.com:banxe-ai-rnd/research.git ../research
cd docs/canon && ln -s ../../research/docs/canon/CANON-FACTORY-SSOT.md .
```

**Risks of alternatives:**
- Local copy: sync forgotten, two sources of truth
- Inline: manual update, error-prone

---

## Q4: Is 17e9a68 content superseded?

**Answer:** Partially — requires analysis

**Superseded (в 277c751+normalization):**
- A+B rules re-implementation (277c751 уже содержит unified governance)
- File structure (53+ files vs minimal)

**Potentially unique (требует проверки):**
- `latest-operator-comment-wins` — не найдено в right/engine-research-v2
- Детали conflict resolution для edge cases

**Action:** Diff 17e9a68 against 277c751 для извлечения unique directives

---

## Q5: Final recommendation

**VERDICT: Option A with modifications**

**Sequence:**
1. Manual extract 11e43f9 (operator-control norm)
2. Diff 17e9a68 vs 277c751 → extract unique directives only
3. Clone SSOT to ../research/
4. Document Aider/Codex role separation
5. Re-audit before promotion

**Confidence:** High (80%)

**Uncertainty:**
- Могут ли быть в 17e9a68 operator directives, которые override normalization?
- Требует ли role separation explicit ADR или достаточно inline comment?

---

## RECONCILIATION WITH POTENTIAL PRIMARY OPINION

Если Codex (gpt-5.6-sol) рекомендует:
- Option B: **DISAGREE** — losing normalization work is unacceptable
- Cherry-pick: **DISAGREE** — semantic conflict risk too high
- Precedence (Aider > Codex): **DISAGREE** — role separation > hierarchy

---

*Fable-5 certification: Independent analysis, no anchoring, counter-evidence reviewed*
