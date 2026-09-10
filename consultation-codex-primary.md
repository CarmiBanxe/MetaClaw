Reading additional input from stdin...
OpenAI Codex v0.149.1
--------
workdir: /home/mmber/MetaClaw
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: low
reasoning summaries: none
session id: 01a03b5a-4078-7650-a380-19fe75d2e585
--------
user
You are the PRIMARY consultant. Analyze this brief and answer all questions Q1-Q5 with detailed reasoning. Final output must include VERDICT section.

<stdin>
# BRIEF TO CONSULTANT: Canon Consolidation Fork

**Date:** 2026-08-26
**From:** BEN (Right Terminal, MetaClaw)
**To:** Codex (primary), Fable-5 (second), Kimi (third), Mistral (fourth)
**Re:** Final consolidation of diverged rule branches
**Status:** CONSULTATION REQUEST — awaiting verdict

---

## 1. FACTS (measured live)

### 1.1 Git topology
```
main@42746a4 (common ancestor)
├── Branch A: exp/sandbox-2026-08-05 → 1d896d8
├── Branch B: right/engine-research-v2 base → 374ebdb
│   └── Merge: 277c751 (A+B unified governance v1.1)
│       └── Normalization: 4096533, 0448d8b, e3ac7ce, 5694a92
│
└── integration/aplusb-20260826 (branched from main@42746a4)
    ├── 17e9a68 (A+B rules re-implementation)
    └── 11e43f9 (operator-control)
```

### 1.2 Content comparison
| Aspect | right/engine-research-v2 | integration/aplusb-20260826 |
|--------|--------------------------|----------------------------|
| Full A+B merge history | ✅ 277c751 | ❌ Re-implements in 17e9a68 |
| Normalization (FOS/CCOP/AGENTS) | ✅ v1.1 | ❌ Absent |
| Governance/docs structure | ✅ 53+ files | ❌ Minimal |
| operator-control rule | ❌ Absent | ✅ 11e43f9 |
| latest-operator-comment-wins | ❌ Absent | ✅ 17e9a68 |
| SSOT pointer | ✅ 5694a92 | ❌ Absent |

### 1.3 Active conflict discovered
- `software-factory-canon-v1.md`: "Aider is the sole code executor" (INV-01)
- `smart-model-routing-protocol-v1.md`: Codex as "preferred primary coding executor"
- **Status:** ACTIVE CONFLICT — not a settled boundary

---

## 2. OPTIONS

### Option A: Use right/engine-research-v2 as base, manual extraction
- Keep full normalization work (277c751 + v1.1)
- Manually extract operator-control norm from 11e43f9
- Analyze 17e9a68 separately for unique directives
- Restore local SSOT

**Safety:** Highest — no automatic cherry-pick of conflicting commits

### Option B: Use integration/aplusb-20260826
- Latest operator directives present
- **CRITICAL:** Loses normalization work, 53+ governance files
- NOT a fast-forward — branches diverged from main@42746a4

**Verdict:** NOT RECOMMENDED — loses substantive work

### Option C: Merge both lines
- Risk: 17e9a68 re-implements A+B on different base
- Significant semantic/text conflicts likely

**Verdict:** NOT RECOMMENDED without detailed conflict analysis

---

## 3. QUESTIONS TO CONSULTANT (all require answer)

### Q1: Preferred integration method?
- Manual extraction of 11e43f9 (clean, provenance preserved)
- Cherry-pick 11e43f9 only (risk: dependency on 17e9a68 base)
- Alternative approach?

### Q2: How resolve Aider vs Codex executor conflict?
- Current: Aider (INV-01) vs Codex (smart-routing)
- Need explicit precedence rule or role separation
- Your proposed resolution?

### Q3: SSOT restoration priority?
- Clone external repo to ../research/
- Local copy with sync mechanism
- Inline critical sections

### Q4: Is 17e9a68 content superseded by 277c751+normalization?
- Or does it contain unique operator directives requiring preservation?

### Q5: Final recommendation — which option and why?

---

## 4. BOUNDARIES (non-negotiable, cannot be weakened by answer)

- **NO-AUTONOMOUS-CONSULT:** Brief preparation only — operator dispatches
- **NO-WAIT RULE:** Central never blocks on Terminal A
- **STOP GATE:** State-changing work requires explicit "go"
- **NON-ATOMIC:** Continuous execution until genuine fork

---

## 5. EVIDENCE AGAINST Option A (included for balance)

1. 11e43f9 and 17e9a68 are MORE RECENT than normalization — operator may intend override
2. "latest-operator-comment-wins" in 17e9a68 explicitly privileges recency
3. By not including these commits, right/engine-research-v2 may be stale
4. Operator may have created integration branch precisely to override normalization

---

## 6. REQUIRED OUTPUT FORMAT

For each question Q1–Q5:
1. Your explicit answer
2. Reasoning (why this answer)
3. Risks of alternative approaches

Final section: **VERDICT** — Option A/B/C with justification

---

**BEN CERTIFICATION:**
- Facts verified by direct git measurement
- Topology corrected per operator review
- Conflict (Aider/Codex) noted as unresolved
- SSOT unavailability acknowledged
- Counter-evidence included

</stdin>
warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the bundled bubblewrap in the meantime.
codex
I’ll treat the stated boundaries as fixed, inspect the relevant commits and canonical documents read-only, then distinguish actual unique directives from rewritten or conflicting material. No repository state will be changed.
exec
/bin/bash -lc "sed -n '1,260p' AGENTS.md; find .. -path '*/docs/canon/CANON-FACTORY-SSOT.md' -print; git status --short --branch; git log --graph --oneline --decorate --all -n 40" in /home/mmber/MetaClaw
 succeeded in 6341ms:
# AGENTS.md — MetaClaw

**Repository:** `~/MetaClaw`  
**Version:** 1.1 | 2026-08-26 (normalized)  
**Purpose:** Agent execution architecture for MetaClaw meta-learning framework  
**Architecture:** Factory-Only / Three-Terminal (LEFT / CENTRAL / RIGHT)

---

## ⚠️ ROOT CANON — единый SSOT (2026-08-26)

Терминальный workflow всех контуров определяет **один файл**:
`banxe-ai-rnd/research` → `docs/canon/CANON-FACTORY-SSOT.md`, норма **CORE-10-29**
(исполнитель кода Aider/Codex, Claude Code оркеструет; cloud-vs-local по классу данных;
непрерывный фронт + STOP-гейты; consult-цепь Codex → Fable → Mistral → Kimi; auto-commit только
Фабрикой; имена CENTRAL / LEFT / RIGHT). `FACTORY_OPERATING_SYSTEM.md` и
`CLAUDE_CODE_OPERATING_PRINCIPLE.md` в этом репозитории — указатели туда, не копии (ADR-102).

---

## Core mission

This repository is the **MetaClaw meta-learning framework** — agents learn and evolve from conversations without GPU.

### Three-Terminal Architecture

| Terminal | Canonical Name | Role | Execution |
|----------|----------------|------|-----------|
| **Central** | CENTRAL (Brain) | Architect, planner, reviewer, orchestrator | NO direct code execution |
| **Left** | LEFT (Factory Interface) | Task assignment, agent orchestration, evidence routing | NO direct code generation |
| **Right** | RIGHT (Assistant) | Research, audit, summary, brief preparation | NO code execution |
| **Factory** | Aider + Codex + agents | Code generation, edits, tests, commands | SOLE execution layer |

**Key principle:** Terminals decide and plan; Factory executes. No terminal bypasses Factory.

---

## Instruction hierarchy

1. **Explicit user instruction** (highest authority)
2. **Root-level canon**: `research/docs/canon/CANON-FACTORY-SSOT.md` (CORE-10-29);
   `FACTORY_OPERATING_SYSTEM.md` / `CLAUDE_CODE_OPERATING_PRINCIPLE.md` здесь — указатели
3. **Session canon**:
   - `.claude/CLAUDE_CODE_CANON.md` (Rules 1–9 + terminal extensions)
4. **Project context**:
   - `CLAUDE.md` (project identity)
   - `AGENTS.md` (this file)
   - `COLLAB.md` (collaboration patterns)
5. **Global defaults**: `~/.claude/CLAUDE.md`

---

## Repository structure

```
~/MetaClaw/
├── .claude/
│   └── CLAUDE_CODE_CANON.md     ← Session canon (Rules 1–9 + terminal extensions)
├── metaclaw/                   ← Core package
│   ├── agents/
│   ├── memory/
│   └── evolution/
├── tests/                      ← Test suite
├── examples/                   ← Usage examples
├── docs/                       ← Documentation
│   ├── canon/
│   ├── sources/                  ← Audit sources
│   └── audit/                    ← Coverage intel
├── FACTORY_OPERATING_SYSTEM.md ← Universal root canon
├── CLAUDE_CODE_OPERATING_PRINCIPLE.md ← Execution law
├── AGENTS.md                   ← This file
└── COLLAB.md                   ← Project collaboration
```

---

## Terminal Roles Detail

Роли CENTRAL (Brain) / LEFT (Factory Interface) / RIGHT (Assistant) и исполнители Фабрики
(Aider primary, Codex secondary, агенты очереди) — нормативно в SSOT `CANON-FACTORY-SSOT.md`
CORE-10-29 п.1 и п.6; здесь не дублируются.

---

## Collaboration pattern

- **Claude Code (Central)** — planner, reviewer, orchestrator; assigns to Factory.
- **Factory (Aider/Codex)** — execution agent (file edits, tests, commands).
- **User** interacts with Central terminal only.

**One terminal = one project = one repo** (invariant INV-08).

---

## Project isolation

This repository is **MetaClaw only**. Do not mix files, code, or context with:
- Banxe (`vibe-coding`)
- GUIYON (`guiyon`)
- Developer-core (`~/developer`)
- Any other project

---

## Repository conventions

- Source: `metaclaw/`
- Tests: `tests/`
- Scripts: `scripts/`
- Examples: `examples/`
- Docs: `docs/`
- Audit sources: `docs/sources/`
- Coverage intel: `docs/audit/`

---

## Before making changes

1. Read `CANON-FACTORY-SSOT.md` CORE-10-29 п.1 (Factory-only coding) и п.3 (non-atomic).
3. Preserve existing API contracts (other projects may depend on the package).
4. Run tests after changes: `pytest tests/ -v`
5. Keep `requirements.txt` and `pyproject.toml` in sync.

---

## Commit style

- English identifiers
- `feat/fix/test/docs/chore/canon` prefix
- Never commit secrets
- Format: `type(scope): message [IL-XXX]`

---

## Files reference

| File | Purpose | Authority |
|------|---------|-----------|
| `FACTORY_OPERATING_SYSTEM.md` | Pointer → SSOT CORE-10-29 | pointer |
| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | Pointer → SSOT CORE-10-29 | pointer |
| `.claude/CLAUDE_CODE_CANON.md` | Session canon (Rules 1–9) | Session |
| `AGENTS.md` | This file — terminal architecture | Project |
| `COLLAB.md` | Collaboration patterns | Project |
| `CLAUDE.md` | Project identity (BANXE gateway) | Project |

---

## Definition of done

A task is complete when:

- [ ] Factory execution verified (Aider/Codex)
- [ ] Tests pass (`pytest`)
- [ ] Lint clean (`ruff`)
- [ ] Audit trail recorded
- [ ] Commit with proper format
- [ ] No secrets committed

---

*Updated: 2026-08-26 (normalized v1.1)*  
*Alignment: research/docs/canon/CANON-FACTORY-SSOT.md v7 / CORE-10-29 (2026-08-26)*
../wt/canonlbd01/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-kr4/docs/canon/CANON-FACTORY-SSOT.md
../wt/sblimits01/docs/canon/CANON-FACTORY-SSOT.md
../wt/hookg9b01/docs/canon/CANON-FACTORY-SSOT.md
../wt/agent-factory-front01-consultant-address-header-v4/docs/canon/CANON-FACTORY-SSOT.md
../wt/adr189land01/docs/canon/CANON-FACTORY-SSOT.md
../wt/defroadmap01/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-opzones/docs/canon/CANON-FACTORY-SSOT.md
../wt/g9closeout01/docs/canon/CANON-FACTORY-SSOT.md
../wt/sprint3t2docs/docs/canon/CANON-FACTORY-SSOT.md
../wt/sprint3t4/docs/canon/CANON-FACTORY-SSOT.md
../wt/adr189land02/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-director/docs/canon/CANON-FACTORY-SSOT.md
../wt/canonfork01/docs/canon/CANON-FACTORY-SSOT.md
../wt/closeout01/docs/canon/CANON-FACTORY-SSOT.md
../wt/c4fork01/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-taktd/docs/canon/CANON-FACTORY-SSOT.md
../wt/bestdec01-ratifyci/docs/canon/CANON-FACTORY-SSOT.md
../wt/d1d2cons01/docs/canon/CANON-FACTORY-SSOT.md
../wt/hookg0sync01/docs/canon/CANON-FACTORY-SSOT.md
../wt/canonssot01-ledger-ack-mr10/docs/canon/CANON-FACTORY-SSOT.md
../wt/fabric-k2/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-techmapref/docs/canon/CANON-FACTORY-SSOT.md
../wt/sprint3t3/docs/canon/CANON-FACTORY-SSOT.md
../wt/r223land/docs/canon/CANON-FACTORY-SSOT.md
../wt/trackc01/docs/canon/CANON-FACTORY-SSOT.md
../wt/sprint3demo/docs/canon/CANON-FACTORY-SSOT.md
../wt/pres4t2/docs/canon/CANON-FACTORY-SSOT.md
../wt/stackaudit01/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-engine/docs/canon/CANON-FACTORY-SSOT.md
../wt/ledgroot01/docs/canon/CANON-FACTORY-SSOT.md
../wt/canonbos01/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-bestdec-rollout/docs/canon/CANON-FACTORY-SSOT.md
../wt/banxe-architecture-core-10-28/docs/canon/CANON-FACTORY-SSOT.md
../wt/ratifyA1def01/docs/canon/CANON-FACTORY-SSOT.md
../wt/deficforks01/docs/canon/CANON-FACTORY-SSOT.md
../wt/bestdec03-fix/docs/canon/CANON-FACTORY-SSOT.md
../wt/ratify171-01/docs/canon/CANON-FACTORY-SSOT.md
../wt/prodaudit01/docs/canon/CANON-FACTORY-SSOT.md
../wt/bestdec01-gapreg-only/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-d4-binding/docs/canon/CANON-FACTORY-SSOT.md
../wt/bestdec01-gapfix/docs/canon/CANON-FACTORY-SSOT.md
../wt/gatefix01/docs/canon/CANON-FACTORY-SSOT.md
../wt/sprint1-rebuild/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-c-counsel/docs/canon/CANON-FACTORY-SSOT.md
../wt/bestdec02-schema/docs/canon/CANON-FACTORY-SSOT.md
../wt/bestdec04-il164/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-kr3/docs/canon/CANON-FACTORY-SSOT.md
../wt/roadmap01/docs/canon/CANON-FACTORY-SSOT.md
../wt/bestdec01-semgrepfix/docs/canon/CANON-FACTORY-SSOT.md
../wt/bestdec01-class3/docs/canon/CANON-FACTORY-SSOT.md
../wt/wt-techmapdocs/docs/canon/CANON-FACTORY-SSOT.md
../wt/pres4t3/docs/canon/CANON-FACTORY-SSOT.md
../wt/infrareq01/docs/canon/CANON-FACTORY-SSOT.md
../wt/registration01/docs/canon/CANON-FACTORY-SSOT.md
../wt/canonbatch01/docs/canon/CANON-FACTORY-SSOT.md
../wt/sprint2t1/docs/canon/CANON-FACTORY-SSOT.md
../wt/sprint3t2/docs/canon/CANON-FACTORY-SSOT.md
../wt/central01/docs/canon/CANON-FACTORY-SSOT.md
../wt/deskguide01/docs/canon/CANON-FACTORY-SSOT.md
../wt/ratify19501/docs/canon/CANON-FACTORY-SSOT.md
../wt/srcregland01/docs/canon/CANON-FACTORY-SSOT.md
../wt/tooltruth01/docs/canon/CANON-FACTORY-SSOT.md
../wt/pysrc-3b5dd4a9/docs/canon/CANON-FACTORY-SSOT.md
../wt/ssotunify02/docs/canon/CANON-FACTORY-SSOT.md
../wt/agent-factory-sixdec01-sixdec-line/docs/canon/CANON-FACTORY-SSOT.md
../wt/bestdec01/docs/canon/CANON-FACTORY-SSOT.md
../wt/sprint3t1/docs/canon/CANON-FACTORY-SSOT.md
../wt/ratify19601/docs/canon/CANON-FACTORY-SSOT.md
../wt/pres4t1/docs/canon/CANON-FACTORY-SSOT.md
../wt/rule9land01/docs/canon/CANON-FACTORY-SSOT.md
../wt/convgapr201/docs/canon/CANON-FACTORY-SSOT.md
../wt/sandboxpack01/docs/canon/CANON-FACTORY-SSOT.md
../wt/tooltruth02/docs/canon/CANON-FACTORY-SSOT.md
../wt/ssotunify01/docs/canon/CANON-FACTORY-SSOT.md
../wt/sprint1-zerosha/docs/canon/CANON-FACTORY-SSOT.md
../wt/adr190land01/docs/canon/CANON-FACTORY-SSOT.md
../wt/architecture-canonssot-20260809/docs/canon/CANON-FACTORY-SSOT.md
../wt/a1t1textfix01/docs/canon/CANON-FACTORY-SSOT.md
../wt/canonssot04-core1015-port/docs/canon/CANON-FACTORY-SSOT.md
../wt/canonssot04-oblcxm/docs/canon/CANON-FACTORY-SSOT.md
../banxe-architecture/.claude/worktrees/org-join-consult/docs/canon/CANON-FACTORY-SSOT.md
../banxe-architecture/docs/canon/CANON-FACTORY-SSOT.md
## right/engine-research-v2
 M .gitignore
 m free-claude-code
?? .claude/CLAUDE_CODE_CANON.md.bak-20260708
?? BRIEF-CONSULTANT-CANON-CONSOLIDATION-2026-08-26.md
?? LibreChat/
?? cloudflared-linux-amd64.deb
?? consultation-codex-primary.md
?? consultation-fable5-second-opinion.md
?? docs/architecture/legion-generic-engine-and-banxe-specialization-canonical-2026-07-10.md.bak.1783641282
?? docs/architecture/legion-generic-engine-and-banxe-specialization-canonical-2026-07-10.md.bak.1783641412
?? docs/canon/ben-right-terminal-canon.md.bak-r5-20260709
?? docs/canon/ben-right-terminal-canon.md.bak-r6-20260709
?? docs/canon/ben-right-terminal-canon.md.bak-r7-20260709
?? docs/canon/ben-right-terminal-canon.md.bak-r8-20260709
?? docs/canon/ben-right-terminal-canon.md.bak-truth-20260709
?? docs/sources/emi-banxe-engine-v2-2026-07-09.md.bak-refs-20260709
* 5694a92 (HEAD -> right/engine-research-v2, origin/right/engine-research-v2) canon(pointers): FOS/CCOP/AGENTS → pointer to research SSOT CORE-10-29 [ADR-102]
* e3ac7ce canon(agents): AGENTS.md v1.1 normalized
* 0448d8b canon(ccop): CLAUDE_CODE_OPERATING_PRINCIPLE v1.1 normalized
* 4096533 canon(fos): FACTORY_OPERATING_SYSTEM v1.1 normalized
*   277c751 canon(normalize): unified governance v1.1 pre-B-merge [IL-PREINTEGRATION-3]
|\  
| * 1d896d8 (origin/exp/sandbox-2026-08-05, exp/sandbox-2026-08-05) chore(claude): enable superpowers plugin at project scope
| * 2de7ae9 (feat/canonical-stack-doc) audit: manus-legion-private-engine (cp+sha zero-loss f937c55f) intel+R4 coverage (0/2/4, MISSING-by-design private contour)
| * d7574da audit: emi_banxe_ai_bank_full_structure_report_v1 (cp+sha zero-loss 666a5bab) intel+R4 coverage (2/2, 1 unknown)
| * e28d883 audit: S-18-consultant-answers (cp+sha zero-loss 719494c4) intel+R4 coverage (reuse-heavy: +2 missing/1 partial)
| * 0493b78 audit: ORG-STRUCTURE (cp+sha zero-loss 02ff23af) intel+R4 coverage (6/1/0)
| * 27d13f7 audit: banxe-agent-engine-conclusion intel+R4 coverage (5/0/1); source kept raw (quoted api_key example, R1 orphan-exception, sha 54a4439e)
| * ef9ff54 audit: banxe-oss-free-agent-solutions (cp+sha zero-loss 50c2f667) intel+R4 coverage (3/0/5)
| * a026cdd audit: emi-banxe-ideal-engine-math (cp+sha zero-loss 8612f7eb) intel+R4 coverage (2/0/6, 3 gated)
| * 995072f audit: consultant-escalation-protocol (cp+sha zero-loss 274dbd3d) intel+R4 coverage (1/2/6, 1 unknown)
| * 83b016c audit: banxe-uxui-architecture intel+R4 coverage (2/1/5); source kept raw (presigned-URL secrets, R1 orphan-exception, sha 37b8be7b)
| * 1146833 audit: emi-banxe-world-experience (cp+sha zero-loss 08aff499) intel+R4 coverage (8/7/21, 7 gated)
* | d8d085c checkpoint(right): isolate dirty worktree pre-integration [IL-PREINTEGRATION-0]
* | 374ebdb canon(sandbox): Auto-commit principle + valuable untracked files
* | 89f5f64 canon(root): Factory Staffing and Token-Economy Principle v1.1
* | 8e2b4bb canon(docs): add Universal Operating Principle reference to COLLAB.md
* | fac02a0 canon(root): Factory Operating System v1.0 - universal AUDIT-FIRST / NON-ATOMIC / TIERED-ECONOMY
|/  
| * 11e43f9 (integration/aplusb-20260826) canon(operator-control): NEVER autonomously send brief to consultant
| * 17e9a68 canon(integration): A+B merge via latest-operator-comment-wins
|/  
* 42746a4 (origin/main, origin/HEAD, main, agent/factory/sprint1/ledger-verify-zero-sha-guard, agent/factory/infra/evo2-gpu-litellm, agent/factory/fabrick2/counsel-c157) audit: ai-efficiency-methodology (cp+sha zero-loss b514e2a1) intel+R4 coverage (4/1/7)
* 12c1838 canon: R8 integrity-truth — cp-of-existing-file is byte-safe; re-typing/Write-tool is the risk (sha-test proven)
* 2788280 fix(engine-v2): References verbatim full URLs (47/47, R8 zero-loss) + sha-anchor update
* 1e2b6fb canon: add R8 zero-loss integrity (STRICT — no content mutation, mandatory integrity proof)
* 7809032 audit: engine-v2 (body==v1 9ef1b03 +refs 1-47) delta intel+coverage (6/1/19)
* 1961a81 audit: unified coverage-gap backlog (18 non-gated candidates + gated list) for factory tasking
* 4686fbd canon: add R7 large-doc chunked ingest (heredoc-safe, anchor-verified)
* 5b39cbf audit: watchdog-roadmap intake+intel+R4 coverage (2 impl/1 partial/10 missing) co-anchored ADR-141/126
* 0744ba0 canon: add R6 write-via-shell (Write-tool unreliable — 3 silent failures this session)
* cfc5f68 audit: BDSL intel + R4 coverage (1 impl/3 partial/10 missing) + R5 single-entry policy — EU-AI-Act gap map
* 34062e4 audit: engine-doc R4 coverage (6 impl/1 partial/7 missing) + R4 policy + non-gated recs
* 663ef51 audit: engine-doc intel — provenance-anchor closes R1 orphan (sha 9ef1b03)
* 904bb32 audit: decision-theory intel + source-retention policy R1/R2/R3 (provenance-anchored)
* a3c8d8c canon: materialize 3-terminal model (engine-doc source, BEN right-terminal canon, Three-Terminal Harmony)
* 7288cf8 fix(litellm): project-reason 235b->glm-air (~11x); disable NOAUTH-broken redis cache
* 5f8126d fix(litellm): fix dead routes, factory-fast 14b→7b, add coder evo2 fallbacks
* cd24758 chore(sign): legion re-verify after evo1-mishap rollback

exec
/bin/bash -lc 'git show --stat --summary 17e9a68; git show --stat --summary 11e43f9; git diff --stat 277c751..17e9a68; git diff --name-status 277c751..17e9a68; git show --format=fuller --no-ext-diff 11e43f9; git show --format=fuller --no-ext-diff 17e9a68 -- .claude/CLAUDE_CODE_CANON.md FACTORY_OPERATING_SYSTEM.md CLAUDE_CODE_OPERATING_PRINCIPLE.md AGENTS.md COLLAB.md' in /home/mmber/MetaClaw
 succeeded in 63ms:
commit 17e9a68f8775f6c225f5d7bd6df24ee8ca6fdbce
Author: CarmiBanxe <149272568+CarmiBanxe@users.noreply.github.com>
Date:   Wed Aug 26 00:28:02 2026 +0200

    canon(integration): A+B merge via latest-operator-comment-wins
    
    A = exp/sandbox-2026-08-05 (docs/sources/*, docs/audit/*)
    B = right/engine-research-v2 (root governance v1.1)
    
    Conflicts resolved per operator directive (2026-08-26):
    1. Executor: Aider primary + Codex secondary
    2. Routing: Cloud-first FCC + data boundary
    3. Atomicity: Non-atomic default with STOP gates
    4. Consult: Codex→Fable→Mistral→Kimi matrix
    5. Auto-commit: Factory-contour only
    6. Naming: LEFT/CENTRAL/RIGHT canonical
    
    D1-D10 all addressed; Phase 6 STOP for operator review.
    
    Files:
    - FACTORY_OPERATING_SYSTEM.md (v1.1, new)
    - CLAUDE_CODE_OPERATING_PRINCIPLE.md (v1.1, new)
    - AGENTS.md (v1.1, normalized)
    - .claude/CLAUDE_CODE_CANON.md (Rule 9 override)

 .claude/CLAUDE_CODE_CANON.md       |   5 +-
 AGENTS.md                          | 354 ++++++++++++++-----------------------
 CLAUDE_CODE_OPERATING_PRINCIPLE.md | 303 +++++++++++++++++++++++++++++++
 FACTORY_OPERATING_SYSTEM.md        | 346 ++++++++++++++++++++++++++++++++++++
 4 files changed, 786 insertions(+), 222 deletions(-)
 create mode 100644 CLAUDE_CODE_OPERATING_PRINCIPLE.md
 create mode 100644 FACTORY_OPERATING_SYSTEM.md
commit 11e43f991b4faa9d22bd0ded2f0ff90c70526e48
Author: CarmiBanxe <149272568+CarmiBanxe@users.noreply.github.com>
Date:   Wed Aug 26 00:34:24 2026 +0200

    canon(operator-control): NEVER autonomously send brief to consultant
    
    Rule added to all canonical documents:
    - FACTORY_OPERATING_SYSTEM.md §5.2.5
    - CLAUDE_CODE_OPERATING_PRINCIPLE.md §7.5
    - AGENTS.md (CONSULT CHAIN line)
    - .claude/CLAUDE_CODE_CANON.md T3.6
    
    Operator directive: brief is text artifact for operator ONLY.
    Consultant engagement requires explicit operator sanction.
    
    Refs: ADR-145, FACTORY_OPERATING_SYSTEM.md §5.1

 .claude/CLAUDE_CODE_CANON.md       |  3 +++
 AGENTS.md                          |  2 +-
 CLAUDE_CODE_OPERATING_PRINCIPLE.md | 13 +++++++++++++
 FACTORY_OPERATING_SYSTEM.md        | 13 +++++++++++++
 4 files changed, 30 insertions(+), 1 deletion(-)
 .aider.conf.yml                                    |    5 +-
 .claude/CLAUDE.md                                  |    9 -
 .claude/CLAUDE_CODE_CANON.md                       |   27 +-
 .claude/settings.json                              |    5 -
 .claude/settings.local.json.example                |    6 -
 .gitignore                                         |    6 -
 AGENTS.md                                          |  352 +-
 CLAUDE.md                                          |   85 -
 CLAUDE_CODE_OPERATING_PRINCIPLE.md                 |    8 +-
 COLLAB.md                                          |   12 -
 FACTORY-LOOP-ENABLED.md                            |    6 -
 FACTORY_OPERATING_SYSTEM.md                        |  147 +-
 apply-cloud-first-canon.sh                         |  229 -
 apply-task-first-fcc-canon.sh                      |  195 -
 audit_v11_2026-05-20.md                            |   15 -
 bootstrap-banxe-ai.sh                              |  313 -
 cloud-first-fcc-policy.md                          |   38 -
 core_engine.py                                     |   76 -
 docs/COLLAB.md                                     |   11 -
 .../ADR-032-cloud-fcc-gateway-amendment-DRAFT.md   |   75 -
 ...some-hermes-skills-registry-usage-2026-07-21.md |   75 -
 docs/architecture/ai-gateway.md                    |   73 -
 ...xe-custom-agentic-stack-canonical-2026-07-10.md |  734 ---
 ...nd-banxe-specialization-canonical-2026-07-10.md |  145 -
 .../architecture/roadmap-and-sprints-2026-07-10.md |   32 -
 ...TION-hermes-agent-skill-authoring-2026-07-21.md |   49 -
 docs/audit/ORG-STRUCTURE-coverage-2026-07-11.md    |   15 -
 docs/audit/ORG-STRUCTURE-intel-2026-07-11.md       |   14 -
 .../S-18-consultant-answers-coverage-2026-07-11.md |   15 -
 .../S-18-consultant-answers-intel-2026-07-11.md    |   14 -
 ...-agent-engine-conclusion-coverage-2026-07-10.md |   14 -
 ...nxe-agent-engine-conclusion-intel-2026-07-10.md |   14 -
 ...oss-free-agent-solutions-coverage-2026-07-10.md |   17 -
 ...xe-oss-free-agent-solutions-intel-2026-07-10.md |   14 -
 .../banxe-uxui-architecture-coverage-2026-07-10.md |   16 -
 .../banxe-uxui-architecture-intel-2026-07-10.md    |   24 -
 ...tant-escalation-protocol-coverage-2026-07-09.md |   35 -
 ...sultant-escalation-protocol-intel-2026-07-09.md |   18 -
 ...-banxe-ideal-engine-math-coverage-2026-07-10.md |   16 -
 ...emi-banxe-ideal-engine-math-intel-2026-07-10.md |   14 -
 ...i-banxe-world-experience-coverage-2026-07-09.md |  150 -
 .../emi-banxe-world-experience-intel-2026-07-09.md |   31 -
 ...full_structure_report_v1-coverage-2026-07-11.md |   13 -
 ...nk_full_structure_report_v1-intel-2026-07-11.md |   14 -
 docs/audit/hermes-h1-coverage-2026-07-17.md        |   18 -
 docs/audit/hermes-h1-intel-2026-07-17.md           |   20 -
 ...us-legion-private-engine-coverage-2026-07-11.md |   14 -
 ...manus-legion-private-engine-intel-2026-07-11.md |   14 -
 .../sprint1-software-factory-canon-2026-05-14.md   |   78 -
 docs/audit/sprint2-role-passports-2026-05-14.md    |   80 -
 ...sprint3-routing-canon-enforcement-2026-05-14.md |   80 -
 ...sprint4-evaluation-loop-mandatory-2026-05-14.md |   86 -
 ...sprint5-approval-model-ruflo-gate-2026-05-14.md |   88 -
 ...print6-evidence-runbooks-standard-2026-05-14.md |   86 -
 .../audit/sprint7-pilot-factory-pack-2026-05-14.md |   88 -
 .../sprint8-full-factory-adoption-2026-05-14.md    |  103 -
 docs/canon/factory-terminal-working-mode-v1.md     |   28 -
 docs/canon/smart-model-routing-protocol-v1.md      |  101 -
 docs/canon/software-factory-canon-v1.md            |   43 +-
 ...ent------EMI-BANXE-AI-Bank--Software-Factory.md |  274 -
 ...mes-Agent----BANXE------Factory--EMI-AI-Bank.md |  397 --
 docs/sources/ORG-STRUCTURE.md                      |  559 --
 docs/sources/S-18-consultant-answers.md            |  298 -
 .../banxe-oss-free-agent-solutions-2026-07-10.md   |  797 ---
 .../consultant-escalation-protocol-2026-07-09.md   |   63 -
 .../emi-banxe-ideal-engine-math-2026-07-10.md      |  847 ---
 .../emi-banxe-intent-first-banking-2026-07-10.md   |  428 --
 .../emi-banxe-intent-layer-launch-2026-07-10.md    |  442 --
 .../emi-banxe-world-experience-2026-07-09.md       |  715 ---
 .../emi_banxe_ai_bank_full_structure_report_v1.md  |  930 ---
 docs/sources/manus-legion-private-engine.md        |  538 --
 ...320\264\321\205\320\276\320\264\321\213 (2).md" |  488 --
 factory-target-model-policy.md                     |   50 -
 free-claude-code                                   |    1 -
 k2-gate-exec-stage3-activate.sh                    |   46 -
 litellm-db/docker-compose.yml                      |   16 -
 litellm/docker-compose.yml                         |    4 -
 litellm/litellm-config.canonical.yaml              |  278 -
 litellm/litellm-config.v2.yaml                     |  313 +-
 litellm/ops/RUNBOOK.md                             |   47 -
 litellm/ops/check-litellm-director.sh              |   80 -
 litellm/ops/install-systemd-artifacts.sh           |   42 -
 litellm/ops/litellm-director.env                   |   17 -
 litellm/ops/litellm-director.service               |   34 -
 loop.sh                                            |   16 -
 operator-fcc-cloud-cutover.md                      |   63 -
 script.sh                                          |    3 -
 scripts/ai/factory-codex.sh                        |    9 -
 scripts/ai/fcc-env-central.sh                      |   10 -
 scripts/ai/fcc-env-left.sh                         |   10 -
 scripts/ai/fcc-env-right.sh                        |   10 -
 scripts/ai/prompt-central.txt                      |   24 -
 scripts/ai/prompt-left.txt                         |   18 -
 scripts/ai/prompt-right.txt                        |   20 -
 scripts/ai/run-central.sh                          |   19 -
 scripts/ai/run-left.sh                             |   13 -
 scripts/ai/run-right.sh                            |   13 -
 scripts/evaluate.sh                                |    2 +-
 scripts/repair-banxe-roadmap-no-rpc.sh             |  156 -
 .../cloud-fcc-canon-amendment-20260823-023141.txt  |   17 -
 .../ADR-032-cloud-fcc-gateway-amendment-DRAFT.md   |   60 -
 .../CLAUDE_CODE_CANON.md                           |   75 -
 .../software-factory-canon-v1.md                   |  325 -
 ...ovider-priority-policy-draft-20260823-025841.md |  162 -
 ...vider-priority-policy-draft-20260823-025841.txt |    1 -
 ...ation-plane-v6-codex-review-20260823-032308.txt |   52 -
 ...onsultation-plane-v6-draft-20260823-032218.json |   28 -
 ...-consultation-plane-v6-draft-20260823-032218.md |   48 -
 ...consultation-plane-v6-draft-20260823-032218.txt |   13 -
 ...ation-plane-v6.1-amendment-20260823-032435.json |   25 -
 ...ltation-plane-v6.1-amendment-20260823-032435.md |   49 -
 ...tation-plane-v6.1-amendment-20260823-032435.txt |   11 -
 .../fcc-install-decision-audit-20260823-022041.txt |  261 -
 .../fcc-isolated-install-plan-20260823-022120.txt  | 1890 ------
 tact-logs/fcc-mini-audit-20260823-022218.brief.txt |   13 -
 tact-logs/fcc-mini-audit-20260823-022218.full.txt  |  177 -
 tact-logs/fcc-server.out                           |  394 --
 ...cc-supply-chain-audit-20260823-022006.brief.txt |   31 -
 ...fcc-supply-chain-audit-20260823-022006.full.txt |  380 --
 ...ll-legacy-canon-value-audit-20260823-024439.txt |  175 -
 ...dian-f9-f10-decision-tables-20260823-025013.txt |   14 -
 ...ecision-tables-codex-review-20260823-025050.txt |   50 -
 ...f9-f10-decision-tables-draft-20260823-025013.md |   76 -
 ...9-f10-decision-tables-review-20260823-025013.md |  185 -
 ...-route-candidates-readonly-20260823-030725.json |  121 -
 ...i-route-candidates-readonly-20260823-030725.txt |   10 -
 .../litellm-local-models-20260823-025335.json      |   66 -
 ...m-local-readiness-diagnosis-20260823-025335.txt |   13 -
 .../litellm-safe-runtime-map-20260823-025422.json  |   51 -
 .../litellm-safe-runtime-map-20260823-025422.txt   |   15 -
 .../mistral-model-discovery-20260823-031606.json   |   40 -
 .../mistral-model-discovery-20260823-031606.txt    |   11 -
 ...l-onboarding-pinning-draft-20260823-031236.json |   24 -
 ...ral-onboarding-pinning-draft-20260823-031236.md |   44 -
 ...al-onboarding-pinning-draft-20260823-031236.txt |   12 -
 ...-route-candidates-readonly-20260823-031135.json |   30 -
 ...l-route-candidates-readonly-20260823-031135.txt |   10 -
 ...odel-operational-readiness-20260823-025248.json |   68 -
 ...model-operational-readiness-20260823-025248.txt |    9 -
 ...r-preference-correction-v4-20260823-030851.json |   36 -
 ...der-preference-correction-v4-20260823-030851.md |   46 -
 ...er-preference-correction-v4-20260823-030851.txt |   15 -
 ...ovider-preference-patch-v3-20260823-030433.json |   17 -
 ...provider-preference-patch-v3-20260823-030433.md |   38 -
 ...rovider-preference-patch-v3-20260823-030433.txt |   10 -
 ...-routing-sequence-v5-draft-20260823-031858.json |  101 -
 ...er-routing-sequence-v5-draft-20260823-031858.md |   44 -
 ...r-routing-sequence-v5-draft-20260823-031858.txt |   13 -
 ...e-alias-inventory-readonly-20260823-030633.json | 6771 --------------------
 ...te-alias-inventory-readonly-20260823-030633.txt |   10 -
 ...-codex-second-opinion-retry-20260823-023809.txt |   38 -
 ...ng-guardian-amendment-review-20260823-024818.md |  118 -
 ...uting-guardian-codex-review-20260823-024855.txt |   43 -
 .../smart-routing-precedence-20260823-024209.txt   |   10 -
 .../ADR-032-cloud-fcc-gateway-amendment-DRAFT.md   |   69 -
 .../CLAUDE_CODE_CANON.md                           |   90 -
 .../software-factory-canon-v1.md                   |  340 -
 .../smart-routing-protocol-20260823-024104.txt     |   19 -
 .../ADR-032-cloud-fcc-gateway-amendment-DRAFT.md   |   67 -
 .../CLAUDE_CODE_CANON.md                           |   88 -
 .../cloud-first-fcc-policy.md                      |   37 -
 .../factory-target-model-policy.md                 |   48 -
 .../operator-fcc-cloud-cutover.md                  |   62 -
 .../software-factory-canon-v1.md                   |  338 -
 ...smart-routing-second-opinion-20260823-023723.md |  134 -
 ...mart-routing-second-opinion-20260823-023723.txt |   54 -
 ...mart-routing-value-controls-20260823-024818.txt |   18 -
 .../smart-model-routing-protocol-v1.md             |   73 -
 ...ability-matrix-codex-review-20260823-030027.txt |   48 -
 ...ed-capability-matrix-draft-20260823-025944.json |  167 -
 ...aged-capability-matrix-draft-20260823-025944.md |   72 -
 ...ged-capability-matrix-draft-20260823-025944.txt |   13 -
 ...ility-matrix-review-closure-20260823-030216.txt |   12 -
 ...capability-matrix-v2-draft-20260823-030216.json |  148 -
 ...d-capability-matrix-v2-draft-20260823-030216.md |  145 -
 tact-logs/tact.log                                 |   67 -
 ...nology-sequence-live-audit-20260823-032627.json |  364 --
 ...hnology-sequence-live-audit-20260823-032627.txt |   41 -
 ...preservation-amendment-draft-20260823-024539.md |   34 -
 ...ue-preservation-codex-bundle-20260823-024539.md |  152 -
 ...vation-codex-second-opinion-20260823-024619.txt |   43 -
 ...alue-preservation-preflight-20260823-024539.txt |   11 -
 tmp/emi-phase7-verify-after-checklist.sh           |   11 -
 tools/patch_canon_safe_barrier.py                  |   99 -
 tools/phase4_org_cleanup_audit.py                  |  152 -
 tools/phase4_org_cleanup_audit.txt                 |   37 -
 yes                                                |    1 -
 187 files changed, 349 insertions(+), 27244 deletions(-)
M	.aider.conf.yml
M	.claude/CLAUDE.md
M	.claude/CLAUDE_CODE_CANON.md
D	.claude/settings.json
D	.claude/settings.local.json.example
M	.gitignore
M	AGENTS.md
D	CLAUDE.md
M	CLAUDE_CODE_OPERATING_PRINCIPLE.md
M	COLLAB.md
M	FACTORY-LOOP-ENABLED.md
M	FACTORY_OPERATING_SYSTEM.md
D	apply-cloud-first-canon.sh
D	apply-task-first-fcc-canon.sh
D	audit_v11_2026-05-20.md
D	bootstrap-banxe-ai.sh
D	cloud-first-fcc-policy.md
D	core_engine.py
M	docs/COLLAB.md
D	docs/adr/ADR-032-cloud-fcc-gateway-amendment-DRAFT.md
D	docs/adr/ADR-awesome-hermes-skills-registry-usage-2026-07-21.md
D	docs/architecture/ai-gateway.md
D	docs/architecture/banxe-custom-agentic-stack-canonical-2026-07-10.md
D	docs/architecture/legion-generic-engine-and-banxe-specialization-canonical-2026-07-10.md
D	docs/architecture/roadmap-and-sprints-2026-07-10.md
D	docs/audit/FEATURE-EVALUATION-hermes-agent-skill-authoring-2026-07-21.md
D	docs/audit/ORG-STRUCTURE-coverage-2026-07-11.md
D	docs/audit/ORG-STRUCTURE-intel-2026-07-11.md
D	docs/audit/S-18-consultant-answers-coverage-2026-07-11.md
D	docs/audit/S-18-consultant-answers-intel-2026-07-11.md
D	docs/audit/banxe-agent-engine-conclusion-coverage-2026-07-10.md
D	docs/audit/banxe-agent-engine-conclusion-intel-2026-07-10.md
D	docs/audit/banxe-oss-free-agent-solutions-coverage-2026-07-10.md
D	docs/audit/banxe-oss-free-agent-solutions-intel-2026-07-10.md
D	docs/audit/banxe-uxui-architecture-coverage-2026-07-10.md
D	docs/audit/banxe-uxui-architecture-intel-2026-07-10.md
D	docs/audit/consultant-escalation-protocol-coverage-2026-07-09.md
D	docs/audit/consultant-escalation-protocol-intel-2026-07-09.md
D	docs/audit/emi-banxe-ideal-engine-math-coverage-2026-07-10.md
D	docs/audit/emi-banxe-ideal-engine-math-intel-2026-07-10.md
D	docs/audit/emi-banxe-world-experience-coverage-2026-07-09.md
D	docs/audit/emi-banxe-world-experience-intel-2026-07-09.md
D	docs/audit/emi_banxe_ai_bank_full_structure_report_v1-coverage-2026-07-11.md
D	docs/audit/emi_banxe_ai_bank_full_structure_report_v1-intel-2026-07-11.md
D	docs/audit/hermes-h1-coverage-2026-07-17.md
D	docs/audit/hermes-h1-intel-2026-07-17.md
D	docs/audit/manus-legion-private-engine-coverage-2026-07-11.md
D	docs/audit/manus-legion-private-engine-intel-2026-07-11.md
D	docs/audit/sprint1-software-factory-canon-2026-05-14.md
D	docs/audit/sprint2-role-passports-2026-05-14.md
D	docs/audit/sprint3-routing-canon-enforcement-2026-05-14.md
D	docs/audit/sprint4-evaluation-loop-mandatory-2026-05-14.md
D	docs/audit/sprint5-approval-model-ruflo-gate-2026-05-14.md
D	docs/audit/sprint6-evidence-runbooks-standard-2026-05-14.md
D	docs/audit/sprint7-pilot-factory-pack-2026-05-14.md
D	docs/audit/sprint8-full-factory-adoption-2026-05-14.md
D	docs/canon/factory-terminal-working-mode-v1.md
D	docs/canon/smart-model-routing-protocol-v1.md
M	docs/canon/software-factory-canon-v1.md
D	docs/sources/Hermes-Agent------EMI-BANXE-AI-Bank--Software-Factory.md
D	docs/sources/Hermes-Agent----BANXE------Factory--EMI-AI-Bank.md
D	docs/sources/ORG-STRUCTURE.md
D	docs/sources/S-18-consultant-answers.md
D	docs/sources/banxe-oss-free-agent-solutions-2026-07-10.md
D	docs/sources/consultant-escalation-protocol-2026-07-09.md
D	docs/sources/emi-banxe-ideal-engine-math-2026-07-10.md
D	docs/sources/emi-banxe-intent-first-banking-2026-07-10.md
D	docs/sources/emi-banxe-intent-layer-launch-2026-07-10.md
D	docs/sources/emi-banxe-world-experience-2026-07-09.md
D	docs/sources/emi_banxe_ai_bank_full_structure_report_v1.md
D	docs/sources/manus-legion-private-engine.md
D	"docs/\320\232\320\276\320\275\321\206\320\265\320\277\321\206\320\270\321\217 \302\253\320\233\321\203\321\207\321\210\320\265\320\263\320\276 \320\240\320\265\321\210\320\265\320\275\320\270\321\217\302\273  \320\234\320\260\321\202\320\265\320\274\320\260\321\202\320\270\321\207\320\265\321\201\320\272\320\270\320\265, \320\235\320\260\321\203\321\207\320\275\321\213\320\265 \320\270 \320\237\321\200\320\270\320\272\320\273\320\260\320\264\320\275\321\213\320\265 \320\237\320\276\320\264\321\205\320\276\320\264\321\213 (2).md"
D	factory-target-model-policy.md
D	free-claude-code
D	k2-gate-exec-stage3-activate.sh
D	litellm-db/docker-compose.yml
M	litellm/docker-compose.yml
D	litellm/litellm-config.canonical.yaml
M	litellm/litellm-config.v2.yaml
D	litellm/ops/RUNBOOK.md
D	litellm/ops/check-litellm-director.sh
D	litellm/ops/install-systemd-artifacts.sh
D	litellm/ops/litellm-director.env
D	litellm/ops/litellm-director.service
D	loop.sh
D	operator-fcc-cloud-cutover.md
D	script.sh
D	scripts/ai/factory-codex.sh
D	scripts/ai/fcc-env-central.sh
D	scripts/ai/fcc-env-left.sh
D	scripts/ai/fcc-env-right.sh
D	scripts/ai/prompt-central.txt
D	scripts/ai/prompt-left.txt
D	scripts/ai/prompt-right.txt
D	scripts/ai/run-central.sh
D	scripts/ai/run-left.sh
D	scripts/ai/run-right.sh
M	scripts/evaluate.sh
D	scripts/repair-banxe-roadmap-no-rpc.sh
D	tact-logs/cloud-fcc-canon-amendment-20260823-023141.txt
D	tact-logs/cloud-fcc-canon-backup-20260823-023141/ADR-032-cloud-fcc-gateway-amendment-DRAFT.md
D	tact-logs/cloud-fcc-canon-backup-20260823-023141/CLAUDE_CODE_CANON.md
D	tact-logs/cloud-fcc-canon-backup-20260823-023141/software-factory-canon-v1.md
D	tact-logs/cloud-provider-priority-policy-draft-20260823-025841.md
D	tact-logs/cloud-provider-priority-policy-draft-20260823-025841.txt
D	tact-logs/developer-tools-and-consultation-plane-v6-codex-review-20260823-032308.txt
D	tact-logs/developer-tools-and-consultation-plane-v6-draft-20260823-032218.json
D	tact-logs/developer-tools-and-consultation-plane-v6-draft-20260823-032218.md
D	tact-logs/developer-tools-and-consultation-plane-v6-draft-20260823-032218.txt
D	tact-logs/developer-tools-and-consultation-plane-v6.1-amendment-20260823-032435.json
D	tact-logs/developer-tools-and-consultation-plane-v6.1-amendment-20260823-032435.md
D	tact-logs/developer-tools-and-consultation-plane-v6.1-amendment-20260823-032435.txt
D	tact-logs/fcc-install-decision-audit-20260823-022041.txt
D	tact-logs/fcc-isolated-install-plan-20260823-022120.txt
D	tact-logs/fcc-mini-audit-20260823-022218.brief.txt
D	tact-logs/fcc-mini-audit-20260823-022218.full.txt
D	tact-logs/fcc-server.out
D	tact-logs/fcc-supply-chain-audit-20260823-022006.brief.txt
D	tact-logs/fcc-supply-chain-audit-20260823-022006.full.txt
D	tact-logs/full-legacy-canon-value-audit-20260823-024439.txt
D	tact-logs/guardian-f9-f10-decision-tables-20260823-025013.txt
D	tact-logs/guardian-f9-f10-decision-tables-codex-review-20260823-025050.txt
D	tact-logs/guardian-f9-f10-decision-tables-draft-20260823-025013.md
D	tact-logs/guardian-f9-f10-decision-tables-review-20260823-025013.md
D	tact-logs/kimi-route-candidates-readonly-20260823-030725.json
D	tact-logs/kimi-route-candidates-readonly-20260823-030725.txt
D	tact-logs/litellm-local-models-20260823-025335.json
D	tact-logs/litellm-local-readiness-diagnosis-20260823-025335.txt
D	tact-logs/litellm-safe-runtime-map-20260823-025422.json
D	tact-logs/litellm-safe-runtime-map-20260823-025422.txt
D	tact-logs/mistral-model-discovery-20260823-031606.json
D	tact-logs/mistral-model-discovery-20260823-031606.txt
D	tact-logs/mistral-onboarding-pinning-draft-20260823-031236.json
D	tact-logs/mistral-onboarding-pinning-draft-20260823-031236.md
D	tact-logs/mistral-onboarding-pinning-draft-20260823-031236.txt
D	tact-logs/mistral-route-candidates-readonly-20260823-031135.json
D	tact-logs/mistral-route-candidates-readonly-20260823-031135.txt
D	tact-logs/model-operational-readiness-20260823-025248.json
D	tact-logs/model-operational-readiness-20260823-025248.txt
D	tact-logs/provider-preference-correction-v4-20260823-030851.json
D	tact-logs/provider-preference-correction-v4-20260823-030851.md
D	tact-logs/provider-preference-correction-v4-20260823-030851.txt
D	tact-logs/provider-preference-patch-v3-20260823-030433.json
D	tact-logs/provider-preference-patch-v3-20260823-030433.md
D	tact-logs/provider-preference-patch-v3-20260823-030433.txt
D	tact-logs/provider-routing-sequence-v5-draft-20260823-031858.json
D	tact-logs/provider-routing-sequence-v5-draft-20260823-031858.md
D	tact-logs/provider-routing-sequence-v5-draft-20260823-031858.txt
D	tact-logs/route-alias-inventory-readonly-20260823-030633.json
D	tact-logs/route-alias-inventory-readonly-20260823-030633.txt
D	tact-logs/smart-routing-codex-second-opinion-retry-20260823-023809.txt
D	tact-logs/smart-routing-guardian-amendment-review-20260823-024818.md
D	tact-logs/smart-routing-guardian-codex-review-20260823-024855.txt
D	tact-logs/smart-routing-precedence-20260823-024209.txt
D	tact-logs/smart-routing-precedence-backup-20260823-024209/ADR-032-cloud-fcc-gateway-amendment-DRAFT.md
D	tact-logs/smart-routing-precedence-backup-20260823-024209/CLAUDE_CODE_CANON.md
D	tact-logs/smart-routing-precedence-backup-20260823-024209/software-factory-canon-v1.md
D	tact-logs/smart-routing-protocol-20260823-024104.txt
D	tact-logs/smart-routing-protocol-backup-20260823-024104/ADR-032-cloud-fcc-gateway-amendment-DRAFT.md
D	tact-logs/smart-routing-protocol-backup-20260823-024104/CLAUDE_CODE_CANON.md
D	tact-logs/smart-routing-protocol-backup-20260823-024104/cloud-first-fcc-policy.md
D	tact-logs/smart-routing-protocol-backup-20260823-024104/factory-target-model-policy.md
D	tact-logs/smart-routing-protocol-backup-20260823-024104/operator-fcc-cloud-cutover.md
D	tact-logs/smart-routing-protocol-backup-20260823-024104/software-factory-canon-v1.md
D	tact-logs/smart-routing-second-opinion-20260823-023723.md
D	tact-logs/smart-routing-second-opinion-20260823-023723.txt
D	tact-logs/smart-routing-value-controls-20260823-024818.txt
D	tact-logs/smart-routing-value-controls-backup-20260823-024818/smart-model-routing-protocol-v1.md
D	tact-logs/staged-capability-matrix-codex-review-20260823-030027.txt
D	tact-logs/staged-capability-matrix-draft-20260823-025944.json
D	tact-logs/staged-capability-matrix-draft-20260823-025944.md
D	tact-logs/staged-capability-matrix-draft-20260823-025944.txt
D	tact-logs/staged-capability-matrix-review-closure-20260823-030216.txt
D	tact-logs/staged-capability-matrix-v2-draft-20260823-030216.json
D	tact-logs/staged-capability-matrix-v2-draft-20260823-030216.md
D	tact-logs/tact.log
D	tact-logs/technology-sequence-live-audit-20260823-032627.json
D	tact-logs/technology-sequence-live-audit-20260823-032627.txt
D	tact-logs/value-preservation-amendment-draft-20260823-024539.md
D	tact-logs/value-preservation-codex-bundle-20260823-024539.md
D	tact-logs/value-preservation-codex-second-opinion-20260823-024619.txt
D	tact-logs/value-preservation-preflight-20260823-024539.txt
D	tmp/emi-phase7-verify-after-checklist.sh
D	tools/patch_canon_safe_barrier.py
D	tools/phase4_org_cleanup_audit.py
D	tools/phase4_org_cleanup_audit.txt
D	yes
commit 11e43f991b4faa9d22bd0ded2f0ff90c70526e48
Author:     CarmiBanxe <149272568+CarmiBanxe@users.noreply.github.com>
AuthorDate: Wed Aug 26 00:34:24 2026 +0200
Commit:     CarmiBanxe <149272568+CarmiBanxe@users.noreply.github.com>
CommitDate: Wed Aug 26 00:34:24 2026 +0200

    canon(operator-control): NEVER autonomously send brief to consultant
    
    Rule added to all canonical documents:
    - FACTORY_OPERATING_SYSTEM.md §5.2.5
    - CLAUDE_CODE_OPERATING_PRINCIPLE.md §7.5
    - AGENTS.md (CONSULT CHAIN line)
    - .claude/CLAUDE_CODE_CANON.md T3.6
    
    Operator directive: brief is text artifact for operator ONLY.
    Consultant engagement requires explicit operator sanction.
    
    Refs: ADR-145, FACTORY_OPERATING_SYSTEM.md §5.1

diff --git a/.claude/CLAUDE_CODE_CANON.md b/.claude/CLAUDE_CODE_CANON.md
index 2295863..43cbce1 100644
--- a/.claude/CLAUDE_CODE_CANON.md
+++ b/.claude/CLAUDE_CODE_CANON.md
@@ -65,6 +65,9 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
 6. **One best step out.** Per Rules 1, 8 — CENTRAL emits a single best next action (a prompt to the
    factory or an `OPERATOR_RUN`), never a menu. [ФАКТ]
 
+
+6. **Operator Control Rule (ABSOLUTE):** The consultation brief is prepared as a textual artifact for the operator ONLY. **NEVER** autonomously send the brief to any consultant. Consultant engagement requires explicit operator directive.
+
 ### T4. Rules for BEN (binding, additive)
 - [ФАКТ] Read-only during scouting (Rule 2). [ВЫВОД] Never executes; hands CENTRAL a single best step +
   tagged findings. [ВЫВОД] Stays a logical mode inside the current repo/terminal context (INV-08).
diff --git a/AGENTS.md b/AGENTS.md
index 74fd3f2..dccc871 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -15,7 +15,7 @@ All agent execution follows `FACTORY_OPERATING_SYSTEM.md`:
 - **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive for **concise final verification only**.
 - **NON-ATOMIC:** Continuous execution across non-branching work.
 - **AUDIT-FIRST:** Fresh shell audit before each material step.
-- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks.
+- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks. **Operator controls delivery — brief prepared as text artifact, NEVER autonomously sent.**
 - **CLOUD-FIRST FCC:** Non-protected data → cloud via FCC; protected data → local Ollama.
 
 Main Claude resource verifies outputs/findings/summaries from cheap contour, not re-processes bulk work from scratch.
diff --git a/CLAUDE_CODE_OPERATING_PRINCIPLE.md b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
index f0512a8..e9485ab 100644
--- a/CLAUDE_CODE_OPERATING_PRINCIPLE.md
+++ b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
@@ -127,6 +127,19 @@ Each fork packet must include:
 
 Independent non-blocked work must continue while the blocked branch is isolated.
 
+### 7.5 Operator Control Rule (ABSOLUTE)
+
+**The consultation packet is prepared as a textual artifact for the operator ONLY.**
+
+- Claude Code prepares the complete fork brief in text form
+- The brief is delivered to the operator as a deliverable
+- **NEVER** autonomously send the brief to any consultant
+- **NEVER** launch consult chain without explicit operator directive
+- Consultant engagement occurs only when operator explicitly directs
+
+This rule is absolute: delivery to consultants requires operator sanction.
+
+
 ---
 
 ## 8. CANON OVERRIDE RULE
diff --git a/FACTORY_OPERATING_SYSTEM.md b/FACTORY_OPERATING_SYSTEM.md
index 7538872..c8af36c 100644
--- a/FACTORY_OPERATING_SYSTEM.md
+++ b/FACTORY_OPERATING_SYSTEM.md
@@ -181,6 +181,19 @@ CONSULT PROMPTS:
   - Kimi: <specific question>
 ```
 
+
+### 5.2.5 Operator Control Rule (ABSOLUTE)
+
+**The brief is prepared as a textual artifact for the operator ONLY.**
+
+- Claude Code prepares the complete fork brief in text form
+- The brief is delivered to the operator as a deliverable
+- **NEVER** autonomously send the brief to any consultant
+- **NEVER** launch consult chain without explicit operator directive
+- Consultant engagement occurs only when operator explicitly directs
+
+This rule is absolute: delivery to consultants requires operator sanction.
+
 ### 5.3 Strict Consultant Order
 1. **Codex** — primary consultant (independent analysis)
 2. **Fable** — second opinion (challenges assumptions)
commit 17e9a68f8775f6c225f5d7bd6df24ee8ca6fdbce
Author:     CarmiBanxe <149272568+CarmiBanxe@users.noreply.github.com>
AuthorDate: Wed Aug 26 00:28:02 2026 +0200
Commit:     CarmiBanxe <149272568+CarmiBanxe@users.noreply.github.com>
CommitDate: Wed Aug 26 00:28:02 2026 +0200

    canon(integration): A+B merge via latest-operator-comment-wins
    
    A = exp/sandbox-2026-08-05 (docs/sources/*, docs/audit/*)
    B = right/engine-research-v2 (root governance v1.1)
    
    Conflicts resolved per operator directive (2026-08-26):
    1. Executor: Aider primary + Codex secondary
    2. Routing: Cloud-first FCC + data boundary
    3. Atomicity: Non-atomic default with STOP gates
    4. Consult: Codex→Fable→Mistral→Kimi matrix
    5. Auto-commit: Factory-contour only
    6. Naming: LEFT/CENTRAL/RIGHT canonical
    
    D1-D10 all addressed; Phase 6 STOP for operator review.
    
    Files:
    - FACTORY_OPERATING_SYSTEM.md (v1.1, new)
    - CLAUDE_CODE_OPERATING_PRINCIPLE.md (v1.1, new)
    - AGENTS.md (v1.1, normalized)
    - .claude/CLAUDE_CODE_CANON.md (Rule 9 override)

diff --git a/.claude/CLAUDE_CODE_CANON.md b/.claude/CLAUDE_CODE_CANON.md
index 9967221..2295863 100644
--- a/.claude/CLAUDE_CODE_CANON.md
+++ b/.claude/CLAUDE_CODE_CANON.md
@@ -12,7 +12,8 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
 6. ON ERROR: diagnose and fix yourself if safe. Only stop if fix is unsafe.
 7. SPLIT large ops into sub-commands. Execute sequentially without asking.
 8. APPROVAL MENUS: NEVER SHOW. Auto-approve safe patterns internally.
-9. REPORT: single summary after sprint. No JSON unless asked.
+9. REPORT: continuous progress, explicit audit basis per step. No JSON unless asked.
+   > **OVERRIDE NOTE:** Rule "single summary after sprint" is CANCELLED by `CLAUDE_CODE_OPERATING_PRINCIPLE.md` §4 (NON-ATOMIC). Report explicitly: audit basis, decision, execution, next audit required, fork status.
 
 ## Canonical prompt block (copy-paste into every sprint)
 
@@ -60,7 +61,7 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
    operator instruction, handled sequentially (INV-08; `COLLAB.md` §Cross-project work). [ФАКТ]
 4. **Route unsafe/state-changing work to the operator gate.** Emit exactly one `OPERATOR_RUN` line, then
    STOP and wait for "go" (Rule 3) — this is how tasks reach LEFT for execution. [ФАКТ]
-5. **No cloud LLM.** All inference local (INV-03 / ADR-031). [ФАКТ]
+5. **Cloud-first FCC routing.** Claude Code routes through local FCC gateway to approved allowlisted cloud models for non-protected data; LiteLLM/local inference remains fallback for protected workloads and offline operation. [ФАКТ]
 6. **One best step out.** Per Rules 1, 8 — CENTRAL emits a single best next action (a prompt to the
    factory or an `OPERATOR_RUN`), never a menu. [ФАКТ]
 
diff --git a/AGENTS.md b/AGENTS.md
index 3965ac8..74fd3f2 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,292 +1,206 @@
-# AGENTS.md — Developer Core: Central Repository for Shared Components
+# AGENTS.md — MetaClaw
 
-**Repository:** `~/developer/`  
-**Version:** 3.0 | 2026-04-03  
-**Purpose:** Shared components, templates, and configurations distributed across all projects  
-**Architecture:** Three-Partner Synergy (Claude Code + Qoder CLI + MiroFish)
+**Repository:** `~/MetaClaw`  
+**Version:** 1.1 | 2026-08-26 (normalized)  
+**Purpose:** Agent execution architecture for MetaClaw meta-learning framework  
+**Architecture:** Factory-Only / Three-Terminal (LEFT / CENTRAL / RIGHT)
 
 ---
 
-## Core mission
-
-This repository is the **central source of truth** for:
+## ⚠️ FACTORY OPERATING SYSTEM (Root-Level Universal)
 
-- Agent instructions (AGENTS.md, CLAUDE.md templates)
-- Qoder CLI configurations (.qoder/config.yml)
-- **Three-partner synergy architecture** (Claude + Qoder + MiroFish)
-- Compliance architecture (COMPLIANCE_ARCH.md)
-- Shared scripts and automation (sync-all.sh, onboard-project.sh)
-- Project templates
-- MCP best practices
-- **MiroFish scenario templates** (MASTER copies for all projects)
+All agent execution follows `FACTORY_OPERATING_SYSTEM.md`:
+- **FACTORY-ONLY CODING:** No terminal codes directly; Factory (Aider/Codex) executes all production code.
+- **ALL FACTORY STAFF ENABLED:** All available Factory agents and workers must execute their roles unless restricted by task canon.
+- **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive for **concise final verification only**.
+- **NON-ATOMIC:** Continuous execution across non-branching work.
+- **AUDIT-FIRST:** Fresh shell audit before each material step.
+- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks.
+- **CLOUD-FIRST FCC:** Non-protected data → cloud via FCC; protected data → local Ollama.
 
-### Three-Partner Architecture
+Main Claude resource verifies outputs/findings/summaries from cheap contour, not re-processes bulk work from scratch.
 
-All projects use the same three-partner stack:
+---
 
-| Partner | Role | Activation | Scope |
-|---------|------|------------|-------|
-| **Claude Code** | Architect & Coordinator | Every session | Design, review, orchestration |
-| **Qoder CLI** | Executor | MCP auto-load | Implementation, edits, tests |
-| **MiroFish** | Simulator & Validator | Auto-trigger by keywords | Behavioral simulation, stress-testing |
+## Core mission
 
-**Key principle:** MiroFish is a partner for ALL projects, not just Banxe.
-- Banxe projects: banking/FCA/fraud scenarios
-- Legal projects: court/judge/appeal scenarios
-- Developer-core: infrastructure & sync validation
+This repository is the **MetaClaw meta-learning framework** — agents learn and evolve from conversations without GPU.
 
-### Distribution model
+### Three-Terminal Architecture
 
-Components from this repository are synced to:
+| Terminal | Canonical Name | Role | Execution |
+|----------|----------------|------|-----------|
+| **Central** | CENTRAL (Brain) | Architect, planner, reviewer, orchestrator | NO direct code execution |
+| **Left** | LEFT (Factory Interface) | Task assignment, agent orchestration, evidence routing | NO direct code generation |
+| **Right** | RIGHT (Assistant) | Research, audit, summary, brief preparation | NO code execution |
+| **Factory** | Aider + Codex + agents | Code generation, edits, tests, commands | SOLE execution layer |
 
-| Project | Type | Sync target | MiroFish | Scenarios |
-|---------|------|-------------|----------|-----------|
-| vibe-coding | banxe | `/home/mmber/vibe-coding/` | ✅ | banking/FCA/fraud |
-| collaboration | banxe | `/home/mmber/collaboration/` | ✅ | multi-agent conflicts |
-| MetaClaw | banxe | `/home/mmber/MetaClaw/` | ✅ | orchestration scaling |
-| guiyon | legal | `/home/mmber/guiyon/` | ✅ | court strategy |
-| ss1 | legal | `/home/mmber/ss1/` | ✅ | appeal dynamics |
-| banxe-mirofish | tool | `/home/mmber/banxe-mirofish/` | ✅ | MASTER templates |
-| developer-core | core | `/home/mmber/developer/` | ✅ | ALL (MASTER) |
+**Key principle:** Terminals decide and plan; Factory executes. No terminal bypasses Factory.
 
 ---
 
-## Instruction hierarchy (for THIS repository)
+## Instruction hierarchy
 
 1. **Explicit user instruction** (highest authority)
-2. **Repository-level contracts**:
-   - `.qoder/context.md` (execution contract)
-   - `CLAUDE.md` (project context)
-3. **Global defaults**: `~/.claude/CLAUDE.md`
-
-### Rule for downstream projects
-
-When syncing components TO a project, that project's local files take precedence over these templates.
-
-**These are templates and starting points, not immutable laws.**
+2. **Root-level canons**:
+   - `FACTORY_OPERATING_SYSTEM.md` (universal)
+   - `CLAUDE_CODE_OPERATING_PRINCIPLE.md` (execution law)
+3. **Session canon**:
+   - `.claude/CLAUDE_CODE_CANON.md` (Rules 1–9 + terminal extensions)
+4. **Project context**:
+   - `CLAUDE.md` (project identity)
+   - `AGENTS.md` (this file)
+   - `COLLAB.md` (collaboration patterns)
+5. **Global defaults**: `~/.claude/CLAUDE.md`
 
 ---
 
 ## Repository structure
 
 ```
-~/developer/
-├── .claude/CLAUDE.md          ← Global collaboration contract (symlink target)
-├── .qoder/config.yml          ← Qoder configuration template
-├── .qoder/context.md          ← Qoder execution contract template
-├── AGENTS.md                  ← This file — agent instructions template
-├── docs/
-│   ├── COLLAB.md              ← Collaboration pattern documentation
-│   └── MCP-BEST-PRACTICES.md  ← MCP server configuration guide
-├── scripts/
-│   ├── check-agent-instructions.sh  ← Diagnostic tool
-│   └── sync-to-project.sh           ← Sync script (TO BE CREATED)
-├── templates/
-│   ├── project-template/            ← New project bootstrap
-│   └── compliance-module/           ← AML/KYC module template
-├── agents/
-│   ├── code-reviewer.skill          ← Code review skill
-│   ├── test-runner.subagent         ← Test execution agent
-│   └── compliance-checker.subagent  ← FCA compliance agent
-└── compliance/
-    ├── COMPLIANCE_ARCH.md           ← Invariants contract
-    └── api.py                       ← Reference implementation
+~/MetaClaw/
+├── .claude/
+│   └── CLAUDE_CODE_CANON.md     ← Session canon (Rules 1–9 + terminal extensions)
+├── metaclaw/                   ← Core package
+│   ├── agents/
+│   ├── memory/
+│   └── evolution/
+├── tests/                      ← Test suite
+├── examples/                   ← Usage examples
+├── docs/                       ← Documentation
+│   ├── canon/
+│   ├── sources/                  ← Audit sources
+│   └── audit/                    ← Coverage intel
+├── FACTORY_OPERATING_SYSTEM.md ← Universal root canon
+├── CLAUDE_CODE_OPERATING_PRINCIPLE.md ← Execution law
+├── AGENTS.md                   ← This file
+└── COLLAB.md                   ← Project collaboration
 ```
 
 ---
 
-## Component catalog
-
-### Templates (copy to new projects)
+## Terminal Roles Detail
 
-| Component | Source | Target | Purpose |
-|-----------|--------|--------|---------|
-| `AGENTS.md` | `./AGENTS.md` | `{project}/AGENTS.md` | Agent instructions |
-| `.qoder/config.yml` | `./.qoder/config.yml` | `{project}/.qoder/config.yml` | Qoder config |
-| `.qoder/context.md` | `./.qoder/context.md` | `{project}/.qoder/context.md` | Execution contract |
-| `docs/COLLAB.md` | `./docs/COLLAB.md` | `{project}/docs/COLLAB.md` | Collaboration docs |
-| `docs/MCP-BEST-PRACTICES.md` | `./docs/MCP-BEST-PRACTICES.md` | `{project}/docs/MCP-BEST-PRACTICES.md` | MCP guide |
+### CENTRAL (Brain)
 
-### Compliance stack (read-only reference)
+**Allowed:**
+- Plan, review, orchestrate, decide, delegate
+- Concise final verification of factory outputs
+- Read root-level system before work starts
+- Assign tasks to Factory
 
-| Component | Purpose | Projects using |
-|-----------|---------|----------------|
-| `compliance/COMPLIANCE_ARCH.md` | Invariants contract | vibe-coding |
-| `compliance/api.py` | Reference API | vibe-coding |
-| `compliance/sanctions_check.py` | OFAC Watchman integration | vibe-coding |
-| `compliance/audit_trail.py` | ClickHouse audit logging | vibe-coding |
+**Prohibited:**
+- Direct file edits
+- Direct code writing
+- Direct `Edit`, `Write` for production code
 
-### Scripts (shared utilities)
+### LEFT (Factory Interface)
 
-| Script | Purpose | Usage |
-|--------|---------|-------|
-| `scripts/sync-all.sh` | Sync all projects from registry | `bash sync-all.sh [--dry-run]` |
-| `scripts/onboard-project.sh` | Onboard new project | `./onboard-project.sh <name> <type>` |
-| `scripts/check-agent-instructions.sh` | Verify instruction hierarchy | Debug agent setup |
-
----
-
-## Sync protocol
-
-### Sync protocol
-
-#### Manual sync (current method)
-
-```bash
-cd ~/developer
-bash scripts/sync-all.sh
-```
+**Allowed:**
+- Assign tasks to all factory agents
+- Review output, route evidence
+- Shell CI/CD / infra / audits
 
-#### Automatic sync (future state)
+**Prohibited:**
+- Direct code generation outside Factory
+- Originate logic that bypasses factory
 
-**Post-commit hook** (`~/developer/.git/hooks/post-commit`):
-- On commit to `~/developer/`: auto-run sync-all.sh
-- Detect changed components
-- Identify affected projects
-- Commit and push to all repos automatically
+### RIGHT (Assistant)
 
-### Change management
+**Allowed:**
+- Research, audit, summarize, prepare briefs
+- Read-only document scouting
+- Tag findings [FACT]/[INFERENCE]/[UNKNOWN]
 
-### Safe changes (auto-sync allowed)
+**Prohibited:**
+- Any code execution
+- File edits
 
-- Documentation updates
-- Comment additions
-- Formatting fixes
-- Test additions
+### Factory (Aider + Codex + agents)
 
-### Review-required changes (manual sync)
-
-- Configuration changes (.qoder/config.yml)
-- Instruction hierarchy changes (AGENTS.md)
-- Compliance invariant changes (COMPLIANCE_ARCH.md)
-- Script logic changes
-
-### Sync approval workflow
-
-1. Change committed to `~/developer/`
-2. User runs `bash scripts/sync-to-project.sh <project>`
-3. Script shows diff for each target
-4. User approves/rejects per project
-5. Changes applied to targets
-
----
-
-## Project isolation enforcement
-
-**CRITICAL:** This repository contains SHARED templates and MASTER scenario copies.
-
-When working IN this repository:
-- Edit templates for distribution
-- Test changes before syncing
-- Document breaking changes
-- Maintain MiroFish scenario templates (MASTER)
-
-When working IN a target project:
-- Use synced templates as starting point
-- Local overrides allowed and expected (especially MIROFISH-SCENARIOS.md)
-- Report useful improvements back to developer/
-- Project-specific scenarios stay in the project (not synced back)
+**Execution only:**
+- Aider (via MCP) — primary executor
+- Codex (plugin/CLI) — secondary executor
+- Factory agents — via controlled task queue
 
 ---
 
-## Testing requirements
+## Collaboration pattern
 
-Before syncing any component:
+- **Claude Code (Central)** — planner, reviewer, orchestrator; assigns to Factory.
+- **Factory (Aider/Codex)** — execution agent (file edits, tests, commands).
+- **User** interacts with Central terminal only.
 
-| Component type | Required validation |
-|----------------|---------------------|
-| Config files | Syntax check + dry-run |
-| Scripts | Shellcheck + manual test |
-| Templates | Bootstrap test project |
-| Compliance | Compare with production |
-| Documentation | Link check + build |
+**One terminal = one project = one repo** (invariant INV-08).
 
 ---
 
-## Version tracking
+## Project isolation
 
-Each synced component should include:
-
-```markdown
-**Source:** `~/developer/{path}`  
-**Synced:** YYYY-MM-DD  
-**Version:** X.Y
-```
+This repository is **MetaClaw only**. Do not mix files, code, or context with:
+- Banxe (`vibe-coding`)
+- GUIYON (`guiyon`)
+- Developer-core (`~/developer`)
+- Any other project
 
 ---
 
-## Rollback procedure
+## Repository conventions
 
-If a synced change breaks a project:
-
-1. Identify the broken component
-2. Restore previous version in target project
-3. Report issue to `~/developer/`
-4. Fix in developer repo
-5. Re-sync when ready
+- Source: `metaclaw/`
+- Tests: `tests/`
+- Scripts: `scripts/`
+- Examples: `examples/`
+- Docs: `docs/`
+- Audit sources: `docs/sources/`
+- Coverage intel: `docs/audit/`
 
 ---
 
-## Quick start for new components
-
-To add a new shared component:
+## Before making changes
 
-1. Create in appropriate directory (`scripts/`, `templates/`, etc.)
-2. Add documentation header with purpose and usage
-3. Test in isolation
-4. Commit to `~/developer/`
-5. Manually sync to interested projects
-6. Update this AGENTS.md if needed
+1. Read `FACTORY_OPERATING_SYSTEM.md` §1 (Factory-Only Coding).
+2. Read `CLAUDE_CODE_OPERATING_PRINCIPLE.md` §4 (Non-Atomic).
+3. Preserve existing API contracts (other projects may depend on the package).
+4. Run tests after changes: `pytest tests/ -v`
+5. Keep `requirements.txt` and `pyproject.toml` in sync.
 
 ---
 
-## People and responsibilities
+## Commit style
 
-| Role | Person | Scope |
-|------|--------|-------|
-| Component author | Any developer | Create/maintain specific components |
-| Sync coordinator | Moriel Carmi | Approve cross-project distribution |
-| Integration tester | Qoder CLI | Validate synced components work |
+- English identifiers
+- `feat/fix/test/docs/chore/canon` prefix
+- Never commit secrets
+- Format: `type(scope): message [IL-XXX]`
 
 ---
 
 ## Files reference
 
-| File | Purpose | Sync targets |
-|------|---------|--------------|
-| `AGENTS.md` | This file — three-partner agent instructions | All projects |
-| `.qoder/config.yml` | Qoder CLI configuration | All projects |
-| `.qoder/context.md` | Qoder execution contract (UNIVERSAL) | All projects |
-| `docs/COLLAB.md` | Collaboration documentation | All projects |
-| `docs/MCP-BEST-PRACTICES.md` | MCP server guide | All projects |
-| `docs/PROJECT-REGISTRY.csv` | Project registry for sync-all.sh | Internal use |
-| `scripts/sync-all.sh` | Multi-repo sync automation | Internal use |
-| `scripts/onboard-project.sh` | New project onboarding | Internal use |
-| `scripts/check-agent-instructions.sh` | Diagnostic tool | All projects |
-| `compliance/COMPLIANCE_ARCH.md` | Compliance invariants | vibe-coding |
+| File | Purpose | Authority |
+|------|---------|-----------|
+| `FACTORY_OPERATING_SYSTEM.md` | Universal root canon — all contours | **ROOT** |
+| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | Execution law (audit-first, non-atomic) | **ROOT** |
+| `.claude/CLAUDE_CODE_CANON.md` | Session canon (Rules 1–9) | Session |
+| `AGENTS.md` | This file — terminal architecture | Project |
+| `COLLAB.md` | Collaboration patterns | Project |
+| `CLAUDE.md` | Project identity (BANXE gateway) | Project |
 
 ---
 
-## Definition of done (for component development)
+## Definition of done
 
-A component is ready for sync when:
+A task is complete when:
 
-- [ ] Implementation complete and tested
-- [ ] Documentation header added
-- [ ] No project-specific assumptions
-- [ ] Works in isolation
-- [ ] Backward-compatible or migration documented
-- [ ] Committed to `~/developer/`
-- [ ] Synced to at least one target project
+- [ ] Factory execution verified (Aider/Codex)
+- [ ] Tests pass (`pytest`)
+- [ ] Lint clean (`ruff`)
+- [ ] Audit trail recorded
+- [ ] Commit with proper format
+- [ ] No secrets committed
 
 ---
 
-## Next steps (pending work)
-
-- [x] Create sync-all.sh for automated distribution
-- [x] Update AGENTS.md with three-partner architecture
-- [x] Create onboard-project.sh for new project onboarding
-- [ ] Create git post-commit hook for auto-sync
-- [ ] Deploy full Qoder stack to banxe-mirofish
-- [ ] Create project-specific MIROFISH-SCENARIOS.md for all 6 projects
-- [ ] Update MEMORY.md with three-partner documentation
+*Updated: 2026-08-26 (normalized v1.1)*  
+*Alignment: FACTORY_OPERATING_SYSTEM.md v1.1, CLAUDE_CODE_OPERATING_PRINCIPLE.md v1.1*
diff --git a/CLAUDE_CODE_OPERATING_PRINCIPLE.md b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
new file mode 100644
index 0000000..f0512a8
--- /dev/null
+++ b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
@@ -0,0 +1,303 @@
+# CLAUDE CODE OPERATING PRINCIPLE — AUDIT-FIRST / NON-ATOMIC / ECONOMY-FIRST
+
+**Status:** EFFECTIVE IMMEDIATELY — ROOT-LEVEL UNIVERSAL ARTIFACT  
+**Scope:** All terminals (LEFT / CENTRAL / RIGHT), all Factory contours, all Claude Code-compatible execution planes  
+**Supersedes:** Any older instruction implying atomic stop-and-wait, guess-based continuation, or action-before-audit  
+**Authority:** Operator directive — binding on all subordinate canons  
+
+---
+
+## 1. PRIMARY OPERATING LAW
+
+Claude Code must work in **AUDIT-FIRST** mode at every stage:
+- first audit;
+- then decision;
+- then execution;
+- then re-audit before the next decision.
+
+No meaningful next step may be chosen without a fresh audit of the current state.  
+No decision may be justified by memory, assumption, stale context, or prior plan alone.
+
+---
+
+## 2. SHELL AUDIT IS MANDATORY
+
+Shell Audit is embedded into Claude Code workflow and is **not optional**.
+
+Before every material step Claude Code must perform or consume a read-only shell audit that establishes:
+- current branch / HEAD / worktree state;
+- relevant file paths and target artifacts;
+- current repo status and diffs;
+- presence/absence of blockers;
+- whether prior assumptions still hold.
+
+Shell Audit is used to determine facts, location, and current state.  
+**Decision first, audit later is forbidden.**
+
+If a shell audit is unavailable, Claude Code must perform an equivalent read-only audit itself before proceeding.
+
+---
+
+## 3. AUDIT BEFORE EVERY STEP
+
+The workflow is cyclical:
+
+```
+AUDIT -> DECIDE -> EXECUTE -> AUDIT -> DECIDE -> EXECUTE
+```
+
+This applies before:
+- editing files;
+- generating prompts;
+- changing docs;
+- updating canon/README/ledgers;
+- starting or continuing recovery;
+- proposing merge-ready conclusions;
+- declaring a branch closed;
+- escalating to consultants.
+
+Every step must be grounded in the immediately preceding audit.
+
+---
+
+## 4. NON-ATOMIC EXECUTION DEFAULT
+
+Atomic stop-after-one-step instructions are **cancelled by default** for Claude Code.
+
+**Cancelled pattern:**
+- do one step;
+- stop;
+- wait for operator;
+- do next step only after confirmation.
+
+**Replacement pattern:**
+- continue in a unified front;
+- do all non-branching work in one continuous pass;
+- stop only at a real fork, sanction gate, or explicit irreversible boundary.
+
+If there is no real fork, Claude Code must not pause just because one substep completed.
+
+---
+
+## 5. WHAT COUNTS AS A REAL STOP
+
+Claude Code may stop only for:
+- a genuine fork that cannot be resolved from canon + audit + facts;
+- an irreversible action that canon reserves for owner/operator sanction;
+- missing authority;
+- conflicting norms that require consultation;
+- unknowns that would force fabrication.
+
+Completion of a substep alone is **NOT** a valid stop reason.
+
+---
+
+## 6. ECONOMY PRINCIPLE
+
+The workflow must be optimized for operator attention economy and token economy:
+- do not ask intermediate questions when the answer can be derived by audit;
+- do not split straightforward work into artificial micro-steps;
+- do not create ceremonial pauses;
+- do not produce redundant explanations between steps;
+- do one coherent pass for all non-branching work.
+
+Audit frequency must be high; interruption frequency must be low.
+
+---
+
+## 7. CONSULT CHAIN ON FORKS
+
+At a real fork, Claude Code must prepare a consultation packet instead of asking a casual question.
+
+**Strict consultant order:**
+1. **Codex** — primary consultant
+2. **Fable** — second opinion
+3. **Mistral** — third opinion
+4. **Kimi** — fourth opinion
+
+Each fork packet must include:
+- fork title;
+- FACT;
+- INFERENCE;
+- UNKNOWN;
+- options;
+- risks;
+- recommended option;
+- consultant-specific prompts in the exact order above.
+
+Independent non-blocked work must continue while the blocked branch is isolated.
+
+---
+
+## 8. CANON OVERRIDE RULE
+
+If any local instruction says or implies:
+- "complete one step and wait";
+- "stop after audit and ask";
+- "do not proceed to next step automatically";
+- "return after each atomic subtask";
+- "single summary after sprint" (legacy Rule 9);
+
+then for Claude Code this instruction is **overridden by this operating principle**, unless:
+- the canon explicitly requires owner/operator sanction at that exact boundary; or
+- the boundary is a real fork.
+
+---
+
+## 9. README / REDMI / CANON / NOTES ALIGNMENT
+
+All instruction-bearing locations that Claude Code reads must reflect the same law:
+- canon;
+- README / REDMI;
+- runbooks;
+- factory preambles;
+- operator notes;
+- workflow specs;
+- prompt templates;
+- recovery procedures;
+- audit procedures.
+
+Any contradictory wording must be rewritten to:  
+**"audit first, then decision; continue non-atomically unless a real fork or sanction gate exists."**
+
+---
+
+## 10. REQUIRED EXECUTION STYLE
+
+Claude Code must explicitly report in factual form:
+- latest audit basis;
+- what decision that audit justified;
+- what actions were executed under that audit;
+- what next audit is required;
+- whether a real fork exists;
+- whether continuation now requires sanction.
+
+---
+
+## 11. HARD PROHIBITIONS
+
+**Forbidden:**
+- acting on stale assumptions;
+- skipping shell audit before a material step;
+- using atomic stop-and-wait as default;
+- asking for confirmation merely because a substep ended;
+- fabricating certainty where audit has not confirmed it;
+- replacing audit with memory of prior repo state.
+
+**Required:**
+- fresh audit before each material step;
+- shell audit embedded in Claude Code work;
+- continuous non-atomic progress across all non-branching work;
+- consultation packet on real forks;
+- sanction stop only where canon truly requires it.
+
+---
+
+## 12. AMENDMENT RULES
+
+- **Operator approval** required for all amendments to this document.
+- **CTIO approval** required for structural changes (modification of consult chain, stop criteria, or override scope).
+- Emergency amendments: Operator may apply temporary amendment with 72-hour expiry; must be ratified or reverted within the window.
+
+---
+
+## 13. TOKEN ECONOMY / MODEL TIER PRINCIPLE
+
+### 13.1 Factory-only coding with all staff enabled
+
+**Code generation and production work goes ONLY through the Factory.**
+
+- No terminal codes directly;
+- Any terminal assigns tasks to Factory;
+- Factory forms code and leads continuous work;
+- **All available Factory agents and workers must be included in the contour and execute their roles** unless explicitly restricted by task canon.
+
+### 13.2 Bulk work = cheap models
+
+For token economy, all mass/auxiliary/preparatory/survey/diagnostic/draft work **must** use by default:
+- Free models where available;
+- Lower-tier runners;
+- Open Claude Code / factory fleet models;
+- Any approved lower-cost routing.
+
+### 13.3 Expensive base model = concise final verification only
+
+Expensive base model (primary Claude Code / Opus-class verifier) **does not** process the full routine stream.
+
+**Reserved for concise verification of:**
+- Outputs, findings, summaries produced by cheap contour;
+- Diffs and conclusions from Factory agents;
+- Final decision;
+- Critical validation;
+- Final quality gate.
+
+**NOT for:** re-processing full bulk work from scratch.
+
+### 13.4 Routing hierarchy
+
+| Work type | Default route | Exception |
+|-----------|---------------|-----------|
+| Bulk/diagnostic/auxiliary | Lower-tier / free | When complexity requires upgrade |
+| Final review/decision | Expensive / Opus-class | Never downgrade for material decisions |
+| Fork consultation | As per §7 chain | Operator override |
+
+### 13.5 Continuous execution until fork
+
+Work proceeds continuously, as a unified front:
+- NOT "one step, then wait";
+- NOT atomic stop-after-each-step;
+- Continuous until real fork, sanction boundary, or missing authority.
+
+### 13.6 Audit before every material step
+
+Shell Audit is **embedded** into Claude Code / Factory workflow:
+- First audit;
+- Then decision;
+- Then execution;
+- Then new audit before next material step.
+
+### 13.7 Fork = consultation brief
+
+At a real fork:
+- Textual brief is formed for consultants;
+- Operator conducts consultation externally;
+- Operator returns result to terminal;
+- Work continues continuously to next fork.
+
+### 13.8 Central terminal brain
+
+Central terminal (Claude Code):
+- **Reads** root-level system before work starts;
+- **Assigns** tasks to Factory;
+- **Does not** execute code directly;
+- **Orchestrates** via audit-first principle.
+
+### 13.9 Override confirmation
+
+This §13 **overrides** any local instruction implying:
+- Direct coding outside factory;
+- Atomic stop-after-one-step as default;
+- Expensive model for routine bulk work by default;
+- No audit before next step;
+- Casual question instead of fork brief.
+
+---
+
+## Appendix: Root-Level Instruction Bearing Files (MetaClaw)
+
+| File | Purpose | AUDIT-FIRST Status |
+|------|---------|-------------------|
+| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | This document — universal root-level rule | ✅ DEFINES |
+| `FACTORY_OPERATING_SYSTEM.md` | Factory operating system — all contours | ✅ REFERENCES THIS DOC |
+| `.claude/CLAUDE_CODE_CANON.md` | Session canon (Rules 1–9 + extensions) | ✅ REFERENCES THIS DOC |
+| `docs/canon/software-factory-canon-v1.md` | Factory operating model | ✅ REFERENCES THIS DOC |
+| `AGENTS.md` (root) | Terminal architecture | ✅ PROPAGATES |
+| `COLLAB.md` (root) | Project collaboration | ✅ PROPAGATES |
+| `free-claude-code/CLAUDE.md` | FCC subproject canon | ✅ ALIGNED |
+
+---
+
+*Enacted: 2026-08-26*  
+*Version: 1.1 (normalized)*  
+*Authority: Operator directive — root-level universal*  
+*Supersedes: All subordinate atomic/stop-and-wait instructions unless canon-boundary sanctioned*
diff --git a/FACTORY_OPERATING_SYSTEM.md b/FACTORY_OPERATING_SYSTEM.md
new file mode 100644
index 0000000..7538872
--- /dev/null
+++ b/FACTORY_OPERATING_SYSTEM.md
@@ -0,0 +1,346 @@
+# FACTORY OPERATING SYSTEM v1.1
+## ROOT-LEVEL UNIVERSAL ARTIFACT — ALL TERMINALS / ALL CONTOURS
+
+**Status:** EFFECTIVE IMMEDIATELY  
+**Authority:** Operator directive — overrides all subordinate instructions  
+**Scope:** Left Terminal, Factory, Central Terminal Brain, Right Terminal  
+**Read-before-work:** MANDATORY for Claude Code and all Factory agents  
+
+---
+
+## 1. FACTORY-ONLY CODING LAW (ABSOLUTE)
+
+### 1.1 No Terminal Codes Directly
+- **NO** terminal (Left, Central, Right, Brain) writes production code directly.
+- **NO** Claude Code instance edits files as "execution".
+- **NO** agent bypasses the Factory execution layer.
+
+### 1.2 Factory Assignment Pattern
+```
+TERMINAL (any) → TASK ASSIGNMENT → FACTORY → CODE GENERATION
+       ↑                                    ↓
+   PLAN/REVIEW ←←←←←←←←←←←←←←←←← EVIDENCE
+```
+
+### 1.3 Terminal Roles (Execution-Prohibited; All Factory Staff Enabled)
+| Terminal | Allowed | Prohibited |
+|----------|---------|------------|
+| **Central (Brain)** | Plan, review, orchestrate, decide, delegate; concise final verification of factory outputs | Direct file edits, direct code writing |
+| **Left (Factory Interface)** | Assign tasks to all factory agents, review output, route evidence | Direct code generation outside Factory |
+| **Right (Assistant)** | Research, audit, summarize, prepare briefs | Any code execution |
+| **Any CC instance** | Analysis, planning, prompt engineering; concise verification of findings | Direct `Edit`, `Write` for production code |
+
+**All Available Factory Agents Rule:**
+Every task must utilize all available Factory agents and workers in their respective roles unless task canon explicitly restricts. No agent sits idle while work is assigned to expensive resource.
+
+### 1.4 Factory Execution Only
+Production code is written **exclusively** by:
+- **Aider** (via MCP/Qoder) — **primary executor**
+- **Codex** (plugin/CLI) — **secondary executor** when enabled
+- **Factory agents** — via controlled task queue
+
+**Claude Code NEVER writes production code.** Claude Code assigns, plans, reviews, validates.
+
+---
+
+## 2. TIERED MODEL ECONOMY (TOKEN OPTIMIZATION)
+
+### 2.1 Work Classification
+| Work Type | Executor | Model Tier | Examples |
+|-----------|----------|------------|----------|
+| **Bulk/Prep/Research** | Factory agents / lower-tier | Cheap/free/lower-tier runners | grep, audit, summaries, fixture prep, doc search |
+| **Draft/Scaffold** | Factory | Economical capable | Code skeletons, test stubs, migrations |
+| **Primary Coding** | Aider/Codex | Strong cloud coding | Implementation, refactors, tests |
+| **Review/Verify** | Factory review layer | Stronger cloud review | Final validation, architecture check |
+| **Final Decision** | Central Terminal | Expensive base model | Concise verification of factory outputs; quality gate; merge approval |
+
+### 2.2 Expensive Model Conservation
+**Base model (Opus-class, primary Claude Code) is reserved for concise final verification:**
+- Reviews outputs/findings/summaries produced by cheap-tier agents;
+- Validates diffs and conclusions from Factory agents;
+- Final quality gate decisions;
+- Critical architecture validation;
+- Material fork resolution (after consult chain);
+- Operator-facing final review;
+- Compliance-sensitive sign-offs.
+
+**NOT for:**
+- Routine grep/audit
+- Bulk file reading
+- Draft scaffolding
+- Syntax fixes
+- Log analysis
+- Re-processing full bulk work from scratch
+
+### 2.3 Open Claude Code / Factory Fleet
+For token economy, Factory uses:
+- Free/cheap cloud tiers
+- Lower-tier runners
+- Local efficient models for prep work
+- FCC-routed economical models
+
+**Principle:** Spend tokens on final quality, not on exploration.
+
+---
+
+## 3. NON-ATOMIC CONTINUOUS EXECUTION
+
+### 3.1 Cancelled Pattern (Explicitly Forbidden)
+```
+[DO ONE STEP] → [STOP] → [WAIT FOR OPERATOR] → [DO NEXT STEP]
+```
+
+### 3.2 Required Pattern (Continuous Front)
+```
+[AUDIT] → [DECIDE] → [EXECUTE] → [AUDIT] → [DECIDE] → [EXECUTE] → ...
+         ↑___________________________________________|
+              (continuous until real fork)
+```
+
+### 3.3 Real Forks Only (Where to Stop)
+Stop and wait **only** for:
+1. **Genuine fork** — cannot resolve from canon + audit + facts
+2. **Sanction gate** — requires explicit owner/operator approval
+3. **Irreversible boundary** — destructive action, secret exposure
+4. **Missing authority** — canon requires higher approval
+5. **Conflicting norms** — consultation required
+
+**NOT a valid stop:** substep completion, routine checkpoint, "just in case".
+
+### 3.4 Factory Loop Continuity
+Factory maintains continuous execution state:
+- No artificial micro-steps
+- No ceremonial pauses
+- No "confirm to proceed" between non-branching actions
+- Unified front until material decision point
+
+---
+
+## 4. MANDATORY AUDIT-FIRST
+
+### 4.1 Shell Audit Embedding
+**Before EVERY material step:**
+```bash
+# MANDATORY READ-ONLY AUDIT
+git status
+git diff --stat
+ls -la <target paths>
+grep/pattern verification
+current state confirmation
+```
+
+### 4.2 Audit-Decision-Execution Cycle
+```
+1. SHELL AUDIT (read-only, establish facts)
+2. DECISION (based on audit, not memory)
+3. EXECUTION (factory-only for code)
+4. RE-AUDIT (before next material step)
+```
+
+### 4.3 Forbidden Substitutions
+- ❌ Memory of prior state
+- ❌ Assumption "still the same"
+- ❌ Stale context from prior turn
+- ❌ "Probably unchanged"
+
+### 4.4 Required Explicit Reporting
+Claude Code must report:
+- Latest audit basis (command outputs)
+- Decision justified by that audit
+- Actions executed under that audit
+- Next audit required
+- Fork existence (yes/no)
+- Sanction requirement (yes/no)
+
+---
+
+## 5. CONSULT CHAIN ON FORKS (NO CASUAL QUESTIONS)
+
+### 5.1 Fork Handling Protocol
+At genuine fork:
+1. **STOP** execution (do not guess)
+2. **PREPARE BRIEF** — structured text packet
+3. **OPERATOR CONSULTS** — externally, via preferred channels
+4. **OPERATOR RETURNS** — result to terminal window
+5. **RESUME CONTINUOUS** — execution proceeds to next fork
+
+### 5.2 Brief Format (Required)
+```
+FORK: <title>
+FACT: <verified facts from audit>
+INFERENCE: <derived conclusions>
+UNKNOWN: <gaps>
+OPTIONS:
+  A. <option> — <risk>
+  B. <option> — <risk>
+RECOMMENDED: <option with justification>
+CONSULT PROMPTS:
+  - Codex: <specific question>
+  - Fable: <specific question>
+  - Mistral: <specific question>
+  - Kimi: <specific question>
+```
+
+### 5.3 Strict Consultant Order
+1. **Codex** — primary consultant (independent analysis)
+2. **Fable** — second opinion (challenges assumptions)
+3. **Mistral** — third perspective (diverse angle)
+4. **Kimi** — fourth review (completeness check)
+
+**Parallel execution:** Non-blocked work continues while fork is isolated.
+
+---
+
+## 6. ROUTING POLICY — CLOUD-FIRST FCC WITH TIERED DATA BOUNDARY
+
+### 6.1 Primary Development Route
+Claude Code-compatible requests are routed through **Free Claude Code (FCC)** gateway to explicit allowlist of cloud providers/models.
+
+### 6.2 Data Classification & Routing Matrix
+| Data Class | Routing | Examples |
+|------------|---------|----------|
+| **Non-protected** | Cloud-first FCC | Synthetic fixtures, architecture/design, ADRs, scaffolding, tests, docs, sanitized debugging |
+| **Protected** | Local-only (Ollama) | Secrets, KYC/AML, payment/ledger, production logs, regulated evidence |
+| **Mixed** | Decomposed — cloud for logic, local for data | Feature with both scaffolding and PII |
+
+### 6.3 Compatibility Boundary
+- FCC preserves Claude Code interface
+- Direct provider calls by agents remain disallowed unless separately approved
+- LiteLLM and local Ollama remain approved fallback for offline/protected workloads
+
+### 6.4 Mandatory Controls
+Provider/model allowlist, loopback-bound gateway, task/route/model audit records, spend/quota limits, credential isolation, tested rollback.
+
+---
+
+## 7. CONSULT POLICY MATRIX (sandbox/preprod/prod × reversible/material/irreversible)
+
+| Environment | Reversible | Material | Irreversible |
+|-------------|------------|----------|--------------|
+| **Sandbox** | Advisory — single opinion | Codex primary + Fable second | Codex + Fable parallel + operator |
+| **Preprod** | Codex single | Codex + Fable | Full chain + operator sanction |
+| **Prod** | Codex single | Full consult chain | Full chain + MLRO/CTIO + operator |
+
+**Irreversible =** secret exposure, production data leak, financial transaction, architectural lock-in.
+
+---
+
+## 8. AUTO-COMMIT SCOPE (Factory Contour Only)
+
+### 8.1 Principle
+In controlled environment (sandbox/governed factory contour), valuable untracked files **must not** automatically hang in "wait for operator" state.
+
+### 8.2 Auto-Commit Criteria
+| Category | Action |
+|----------|--------|
+| Safe valuable untracked (docs, canons, policies, sources) | **AUTO-COMMIT** after triage |
+| Safe trash/temp/backups | Delete or add to .gitignore |
+| Local settings/runtime | Leave untracked or .gitignore |
+| Secrets/credentials | **RISK BUCKET** — no auto-commit |
+| Unknown/suspicious binaries | **RISK BUCKET** — no auto-commit |
+
+### 8.3 Central Terminal Exception
+**Central terminal does NOT auto-commit.** Central plans/reviews; Factory (Left) executes commits. Auto-commit applies **only** to Factory contour operations.
+
+---
+
+## 9. TERMINAL NAMING UNIFICATION
+
+| Legacy Name | Canonical Name | Role |
+|-------------|----------------|------|
+| Left | **LEFT / Factory Interface** | Task assignment, agent orchestration |
+| Central / Brain | **CENTRAL** | Planning, review, decision, verification |
+| Right / BEN | **RIGHT / Assistant** | Research, audit, summary, brief preparation |
+
+All documentation must use canonical names. Legacy references should be updated on next edit.
+
+---
+
+## 10. CANON OVERRIDE RULE
+
+### 10.1 Cancelled Formulations
+Any instruction implying:
+- "complete one step and wait" ❌
+- "stop after audit and ask" ❌
+- "do not proceed to next step automatically" ❌
+- "return after each atomic subtask" ❌
+- "Claude Code executes code" ❌
+- "single summary after sprint" ❌
+
+**IS OVERRIDDEN** by this document unless:
+- Explicit canon-required sanction boundary
+- Real fork requiring operator decision
+
+### 10.2 Preserved Sanction Boundaries
+These remain valid stops:
+- MLRO gate (compliance changes)
+- CTIO gate (architecture changes)
+- Operator gate (destructive operations)
+- Ruflo checkpoint (regulated quality gate)
+- Secret rotation / exposure risk
+- Production deployment to live systems
+
+---
+
+## 11. PROPAGATION TO ALL CONTOURS
+
+### 11.1 Read Obligation
+This document MUST be read by:
+- **Left Terminal** — before Factory task assignment
+- **Factory** — before code generation
+- **Central Terminal** — before planning/orchestration
+- **Right Terminal** — before audit/summary tasks
+
+### 11.2 One Recording, Universal Application
+Recording this principle in root-level `FACTORY_OPERATING_SYSTEM.md` binds all contours. Local copies are references, not substitutes.
+
+### 11.3 Alignment Requirement
+All instruction-bearing documents must align:
+- canon files
+- README / REDMI
+- runbooks
+- workflow specs
+- prompt templates
+- recovery procedures
+
+**Contradictory wording must be rewritten** to match this principle.
+
+---
+
+## 12. EXCEPTIONS (SANCTIONED ONLY)
+
+| Exception | Justification | Approval |
+|-----------|---------------|----------|
+| Emergency direct edit | System down, no Factory path | Operator real-time sanction |
+| Documentation-only change | No code impact, markdown only | Documented in commit |
+| Factory bypass for experiment | Explicit research mode | Operator pre-approval |
+| Integration preparation | Operator-directed merge prep | Operator directive (this document) |
+
+**Default:** No exceptions. Factory-only coding is absolute.
+
+---
+
+## 13. AMENDMENT RULES
+
+- **Operator approval** — all amendments
+- **CTIO approval** — structural changes (roles, tiers, consult chain)
+- **Emergency amendments** — 72-hour expiry, must ratify or revert
+
+---
+
+## APPENDIX: AUDITED SOURCES STATUS
+
+| Source | Factory-Only | Cheap-First | Non-Atomic | Audit-First | Shell Audit | Consult Chain | Status |
+|--------|--------------|-------------|------------|-------------|-------------|---------------|--------|
+| `FACTORY_OPERATING_SYSTEM.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **THIS DOCUMENT** |
+| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Aligned v1.1 |
+| `AGENTS.md` (root) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Updated v1.1 |
+| `docs/canon/software-factory-canon-v1.md` | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | References this doc |
+| `.claude/CLAUDE_CODE_CANON.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Rule 9 overridden |
+
+---
+
+*Enacted: 2026-08-26*  
+*Version: 1.1 (normalized)*  
+*Authority: Operator directive — root-level universal, all contours*  
+*Supersedes: All factory/canon instructions where conflict exists*

codex
The topology confirms the brief’s central concern, but one point is sharper than stated: using the integration branch wholesale would remove roughly 27,000 lines across 187 paths relative to the unified branch, not merely omit “53+ governance files.” I’m now checking whether the two recent commits carry semantic instructions that can be transplanted independently.
exec
/bin/bash -lc "git diff --no-ext-diff 17e9a68 277c751 -- FACTORY_OPERATING_SYSTEM.md CLAUDE_CODE_OPERATING_PRINCIPLE.md AGENTS.md .claude/CLAUDE_CODE_CANON.md; git diff --no-ext-diff 17e9a68 5694a92 -- FACTORY_OPERATING_SYSTEM.md CLAUDE_CODE_OPERATING_PRINCIPLE.md AGENTS.md .claude/CLAUDE_CODE_CANON.md; git show --format= --no-ext-diff 11e43f9; sed -n '1,240p' ../wt/canonfork01/docs/canon/CANON-FACTORY-SSOT.md" in /home/mmber/MetaClaw
 succeeded in 78ms:
diff --git a/.claude/CLAUDE_CODE_CANON.md b/.claude/CLAUDE_CODE_CANON.md
index 2295863..6d68d61 100644
--- a/.claude/CLAUDE_CODE_CANON.md
+++ b/.claude/CLAUDE_CODE_CANON.md
@@ -1,5 +1,9 @@
 # Claude Code Session Canon (ABSOLUTE)
 
+**Root-Level Override:** `FACTORY_OPERATING_SYSTEM.md` takes precedence for FACTORY-ONLY CODING / TIERED MODEL ECONOMY / NON-ATOMIC / AUDIT-FIRST execution. This canon remains binding where not in conflict.
+
+**CRITICAL:** Claude Code NEVER writes production code directly. All code generation goes through Factory (Aider/Codex). See `FACTORY_OPERATING_SYSTEM.md` §1.
+
 Every Claude Code sprint prompt MUST include this block verbatim at the top.
 
 ## Rules
@@ -61,7 +65,7 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
    operator instruction, handled sequentially (INV-08; `COLLAB.md` §Cross-project work). [ФАКТ]
 4. **Route unsafe/state-changing work to the operator gate.** Emit exactly one `OPERATOR_RUN` line, then
    STOP and wait for "go" (Rule 3) — this is how tasks reach LEFT for execution. [ФАКТ]
-5. **Cloud-first FCC routing.** Claude Code routes through local FCC gateway to approved allowlisted cloud models for non-protected data; LiteLLM/local inference remains fallback for protected workloads and offline operation. [ФАКТ]
+5. **Cloud-first development is permitted through FCC.** Claude Code routes through a local FCC gateway to approved allowlisted cloud models; LiteLLM/local inference remains the fallback. Sensitive banking data must remain local.
 6. **One best step out.** Per Rules 1, 8 — CENTRAL emits a single best next action (a prompt to the
    factory or an `OPERATOR_RUN`), never a menu. [ФАКТ]
 
@@ -74,3 +78,24 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
   with INV-01/INV-08 or `COLLAB.md` single-terminal canon, the invariant/COLLAB wins and this section is
   read as role-separation-within-one-terminal only.
 - [ФАКТ] Amendments follow `software-factory-canon-v1.md` §11 (Operator approval; CTIO for structural).
+
+
+## Cloud-first development routing amendment
+
+**Status:** EFFECTIVE by Operator directive; implementation remains staged and auditable.
+
+1. **Primary development route:** Claude Code-compatible requests may be routed through a local Free Claude Code (FCC) gateway to an explicit allowlist of cloud providers/models.
+2. **Compatibility boundary:** FCC preserves the Claude Code interface; direct provider calls by agents remain disallowed unless separately approved.
+3. **Local continuity:** LiteLLM and local Ollama remain approved fallback routes for offline operation, continuity, and protected workloads.
+4. **Data boundary:** Cloud routes MUST NOT receive secrets, credentials, real customer data, KYC/KYB/AML cases, payment or ledger payloads, production logs, regulated evidence, or other sensitive banking data.
+5. **Permitted cloud work:** Synthetic fixtures, non-sensitive architecture/design, ADRs, code scaffolding, tests, migrations, documentation, and sanitized debugging.
+6. **Controls:** Provider/model allowlist, loopback-bound gateway, task/route/model audit records, spend/quota limits, credential isolation, and tested rollback are mandatory before provider activation.
+7. **Architecture boundary:** FCC accelerates development only. Banking architecture remains based on domain patterns: double-entry ledger, CQRS/event sourcing, KYC/AML orchestration, and ISO 20022/payment adapters.
+
+> **Smart Model Routing:** `docs/canon/smart-model-routing-protocol-v1.md` is the governing role, trust-tier, preflight, and independent-review protocol for this document.
+
+## Smart Routing Precedence
+
+For model selection, execution-role assignment, gateway routing, trust-tier handling, preflight, and independent-review requirements, `docs/canon/smart-model-routing-protocol-v1.md` takes precedence over earlier conflicting wording in this document.
+
+Earlier references to a sole executor, local-only inference, gateway-only routing, or legacy routing behavior remain historical/contextual unless they are explicitly restated in the Smart Model Routing Protocol.
diff --git a/AGENTS.md b/AGENTS.md
index 74fd3f2..58deaec 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,9 +1,9 @@
-# AGENTS.md — MetaClaw
+# AGENTS.md — Developer Core: Central Repository for Shared Components
 
-**Repository:** `~/MetaClaw`  
-**Version:** 1.1 | 2026-08-26 (normalized)  
-**Purpose:** Agent execution architecture for MetaClaw meta-learning framework  
-**Architecture:** Factory-Only / Three-Terminal (LEFT / CENTRAL / RIGHT)
+**Repository:** `~/developer/`  
+**Version:** 3.0 | 2026-04-03  
+**Purpose:** Shared components, templates, and configurations distributed across all projects  
+**Architecture:** Three-Partner Synergy (Claude Code + Qoder CLI + MiroFish)
 
 ---
 
@@ -12,195 +12,297 @@
 All agent execution follows `FACTORY_OPERATING_SYSTEM.md`:
 - **FACTORY-ONLY CODING:** No terminal codes directly; Factory (Aider/Codex) executes all production code.
 - **ALL FACTORY STAFF ENABLED:** All available Factory agents and workers must execute their roles unless restricted by task canon.
-- **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive for **concise final verification only**.
+- **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive model for **concise final verification only**.
 - **NON-ATOMIC:** Continuous execution across non-branching work.
-- **AUDIT-FIRST:** Fresh shell audit before each material step.
+- **AUDIT-FIRST:** Shell audit precedes every material step.
 - **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks.
-- **CLOUD-FIRST FCC:** Non-protected data → cloud via FCC; protected data → local Ollama.
 
 Main Claude resource verifies outputs/findings/summaries from cheap contour, not re-processes bulk work from scratch.
 
+This principle propagates to all synced target projects.
+
 ---
 
 ## Core mission
 
-This repository is the **MetaClaw meta-learning framework** — agents learn and evolve from conversations without GPU.
+This repository is the **central source of truth** for:
+
+- Agent instructions (AGENTS.md, CLAUDE.md templates)
+- Qoder CLI configurations (.qoder/config.yml)
+- **Three-partner synergy architecture** (Claude + Qoder + MiroFish)
+- Compliance architecture (COMPLIANCE_ARCH.md)
+- Shared scripts and automation (sync-all.sh, onboard-project.sh)
+- Project templates
+- MCP best practices
+- **MiroFish scenario templates** (MASTER copies for all projects)
+
+### Three-Partner Architecture
+
+All projects use the same three-partner stack:
 
-### Three-Terminal Architecture
+| Partner | Role | Activation | Scope |
+|---------|------|------------|-------|
+| **Claude Code** | Architect & Coordinator | Every session | Design, review, orchestration |
+| **Qoder CLI** | Executor | MCP auto-load | Implementation, edits, tests |
+| **MiroFish** | Simulator & Validator | Auto-trigger by keywords | Behavioral simulation, stress-testing |
 
-| Terminal | Canonical Name | Role | Execution |
-|----------|----------------|------|-----------|
-| **Central** | CENTRAL (Brain) | Architect, planner, reviewer, orchestrator | NO direct code execution |
-| **Left** | LEFT (Factory Interface) | Task assignment, agent orchestration, evidence routing | NO direct code generation |
-| **Right** | RIGHT (Assistant) | Research, audit, summary, brief preparation | NO code execution |
-| **Factory** | Aider + Codex + agents | Code generation, edits, tests, commands | SOLE execution layer |
+**Key principle:** MiroFish is a partner for ALL projects, not just Banxe.
+- Banxe projects: banking/FCA/fraud scenarios
+- Legal projects: court/judge/appeal scenarios
+- Developer-core: infrastructure & sync validation
 
-**Key principle:** Terminals decide and plan; Factory executes. No terminal bypasses Factory.
+### Distribution model
+
+Components from this repository are synced to:
+
+| Project | Type | Sync target | MiroFish | Scenarios |
+|---------|------|-------------|----------|-----------|
+| vibe-coding | banxe | `/home/mmber/vibe-coding/` | ✅ | banking/FCA/fraud |
+| collaboration | banxe | `/home/mmber/collaboration/` | ✅ | multi-agent conflicts |
+| MetaClaw | banxe | `/home/mmber/MetaClaw/` | ✅ | orchestration scaling |
+| guiyon | legal | `/home/mmber/guiyon/` | ✅ | court strategy |
+| ss1 | legal | `/home/mmber/ss1/` | ✅ | appeal dynamics |
+| banxe-mirofish | tool | `/home/mmber/banxe-mirofish/` | ✅ | MASTER templates |
+| developer-core | core | `/home/mmber/developer/` | ✅ | ALL (MASTER) |
 
 ---
 
-## Instruction hierarchy
+## Instruction hierarchy (for THIS repository)
 
 1. **Explicit user instruction** (highest authority)
-2. **Root-level canons**:
-   - `FACTORY_OPERATING_SYSTEM.md` (universal)
-   - `CLAUDE_CODE_OPERATING_PRINCIPLE.md` (execution law)
-3. **Session canon**:
-   - `.claude/CLAUDE_CODE_CANON.md` (Rules 1–9 + terminal extensions)
-4. **Project context**:
-   - `CLAUDE.md` (project identity)
-   - `AGENTS.md` (this file)
-   - `COLLAB.md` (collaboration patterns)
-5. **Global defaults**: `~/.claude/CLAUDE.md`
+2. **Repository-level contracts**:
+   - `.qoder/context.md` (execution contract)
+   - `CLAUDE.md` (project context)
+3. **Global defaults**: `~/.claude/CLAUDE.md`
+
+### Rule for downstream projects
+
+When syncing components TO a project, that project's local files take precedence over these templates.
+
+**These are templates and starting points, not immutable laws.**
 
 ---
 
 ## Repository structure
 
 ```
-~/MetaClaw/
-├── .claude/
-│   └── CLAUDE_CODE_CANON.md     ← Session canon (Rules 1–9 + terminal extensions)
-├── metaclaw/                   ← Core package
-│   ├── agents/
-│   ├── memory/
-│   └── evolution/
-├── tests/                      ← Test suite
-├── examples/                   ← Usage examples
-├── docs/                       ← Documentation
-│   ├── canon/
-│   ├── sources/                  ← Audit sources
-│   └── audit/                    ← Coverage intel
-├── FACTORY_OPERATING_SYSTEM.md ← Universal root canon
-├── CLAUDE_CODE_OPERATING_PRINCIPLE.md ← Execution law
-├── AGENTS.md                   ← This file
-└── COLLAB.md                   ← Project collaboration
+~/developer/
+├── .claude/CLAUDE.md          ← Global collaboration contract (symlink target)
+├── .qoder/config.yml          ← Qoder configuration template
+├── .qoder/context.md          ← Qoder execution contract template
+├── AGENTS.md                  ← This file — agent instructions template
+├── docs/
+│   ├── COLLAB.md              ← Collaboration pattern documentation
+│   └── MCP-BEST-PRACTICES.md  ← MCP server configuration guide
+├── scripts/
+│   ├── check-agent-instructions.sh  ← Diagnostic tool
+│   └── sync-to-project.sh           ← Sync script (TO BE CREATED)
+├── templates/
+│   ├── project-template/            ← New project bootstrap
+│   └── compliance-module/           ← AML/KYC module template
+├── agents/
+│   ├── code-reviewer.skill          ← Code review skill
+│   ├── test-runner.subagent         ← Test execution agent
+│   └── compliance-checker.subagent  ← FCA compliance agent
+└── compliance/
+    ├── COMPLIANCE_ARCH.md           ← Invariants contract
+    └── api.py                       ← Reference implementation
 ```
 
 ---
 
-## Terminal Roles Detail
+## Component catalog
+
+### Templates (copy to new projects)
+
+| Component | Source | Target | Purpose |
+|-----------|--------|--------|---------|
+| `AGENTS.md` | `./AGENTS.md` | `{project}/AGENTS.md` | Agent instructions |
+| `.qoder/config.yml` | `./.qoder/config.yml` | `{project}/.qoder/config.yml` | Qoder config |
+| `.qoder/context.md` | `./.qoder/context.md` | `{project}/.qoder/context.md` | Execution contract |
+| `docs/COLLAB.md` | `./docs/COLLAB.md` | `{project}/docs/COLLAB.md` | Collaboration docs |
+| `docs/MCP-BEST-PRACTICES.md` | `./docs/MCP-BEST-PRACTICES.md` | `{project}/docs/MCP-BEST-PRACTICES.md` | MCP guide |
+
+### Compliance stack (read-only reference)
 
-### CENTRAL (Brain)
+| Component | Purpose | Projects using |
+|-----------|---------|----------------|
+| `compliance/COMPLIANCE_ARCH.md` | Invariants contract | vibe-coding |
+| `compliance/api.py` | Reference API | vibe-coding |
+| `compliance/sanctions_check.py` | OFAC Watchman integration | vibe-coding |
+| `compliance/audit_trail.py` | ClickHouse audit logging | vibe-coding |
 
-**Allowed:**
-- Plan, review, orchestrate, decide, delegate
-- Concise final verification of factory outputs
-- Read root-level system before work starts
-- Assign tasks to Factory
+### Scripts (shared utilities)
 
-**Prohibited:**
-- Direct file edits
-- Direct code writing
-- Direct `Edit`, `Write` for production code
+| Script | Purpose | Usage |
+|--------|---------|-------|
+| `scripts/sync-all.sh` | Sync all projects from registry | `bash sync-all.sh [--dry-run]` |
+| `scripts/onboard-project.sh` | Onboard new project | `./onboard-project.sh <name> <type>` |
+| `scripts/check-agent-instructions.sh` | Verify instruction hierarchy | Debug agent setup |
 
-### LEFT (Factory Interface)
+---
+
+## Sync protocol
 
-**Allowed:**
-- Assign tasks to all factory agents
-- Review output, route evidence
-- Shell CI/CD / infra / audits
+### Sync protocol
 
-**Prohibited:**
-- Direct code generation outside Factory
-- Originate logic that bypasses factory
+#### Manual sync (current method)
+
+```bash
+cd ~/developer
+bash scripts/sync-all.sh
+```
 
-### RIGHT (Assistant)
+#### Automatic sync (future state)
 
-**Allowed:**
-- Research, audit, summarize, prepare briefs
-- Read-only document scouting
-- Tag findings [FACT]/[INFERENCE]/[UNKNOWN]
+**Post-commit hook** (`~/developer/.git/hooks/post-commit`):
+- On commit to `~/developer/`: auto-run sync-all.sh
+- Detect changed components
+- Identify affected projects
+- Commit and push to all repos automatically
 
-**Prohibited:**
-- Any code execution
-- File edits
+### Change management
 
-### Factory (Aider + Codex + agents)
+### Safe changes (auto-sync allowed)
 
-**Execution only:**
-- Aider (via MCP) — primary executor
-- Codex (plugin/CLI) — secondary executor
-- Factory agents — via controlled task queue
+- Documentation updates
+- Comment additions
+- Formatting fixes
+- Test additions
+
+### Review-required changes (manual sync)
+
+- Configuration changes (.qoder/config.yml)
+- Instruction hierarchy changes (AGENTS.md)
+- Compliance invariant changes (COMPLIANCE_ARCH.md)
+- Script logic changes
+
+### Sync approval workflow
+
+1. Change committed to `~/developer/`
+2. User runs `bash scripts/sync-to-project.sh <project>`
+3. Script shows diff for each target
+4. User approves/rejects per project
+5. Changes applied to targets
 
 ---
 
-## Collaboration pattern
+## Project isolation enforcement
 
-- **Claude Code (Central)** — planner, reviewer, orchestrator; assigns to Factory.
-- **Factory (Aider/Codex)** — execution agent (file edits, tests, commands).
-- **User** interacts with Central terminal only.
+**CRITICAL:** This repository contains SHARED templates and MASTER scenario copies.
 
-**One terminal = one project = one repo** (invariant INV-08).
+When working IN this repository:
+- Edit templates for distribution
+- Test changes before syncing
+- Document breaking changes
+- Maintain MiroFish scenario templates (MASTER)
+
+When working IN a target project:
+- Use synced templates as starting point
+- Local overrides allowed and expected (especially MIROFISH-SCENARIOS.md)
+- Report useful improvements back to developer/
+- Project-specific scenarios stay in the project (not synced back)
 
 ---
 
-## Project isolation
+## Testing requirements
+
+Before syncing any component:
 
-This repository is **MetaClaw only**. Do not mix files, code, or context with:
-- Banxe (`vibe-coding`)
-- GUIYON (`guiyon`)
-- Developer-core (`~/developer`)
-- Any other project
+| Component type | Required validation |
+|----------------|---------------------|
+| Config files | Syntax check + dry-run |
+| Scripts | Shellcheck + manual test |
+| Templates | Bootstrap test project |
+| Compliance | Compare with production |
+| Documentation | Link check + build |
 
 ---
 
-## Repository conventions
+## Version tracking
 
-- Source: `metaclaw/`
-- Tests: `tests/`
-- Scripts: `scripts/`
-- Examples: `examples/`
-- Docs: `docs/`
-- Audit sources: `docs/sources/`
-- Coverage intel: `docs/audit/`
+Each synced component should include:
+
+```markdown
+**Source:** `~/developer/{path}`  
+**Synced:** YYYY-MM-DD  
+**Version:** X.Y
+```
 
 ---
 
-## Before making changes
+## Rollback procedure
 
-1. Read `FACTORY_OPERATING_SYSTEM.md` §1 (Factory-Only Coding).
-2. Read `CLAUDE_CODE_OPERATING_PRINCIPLE.md` §4 (Non-Atomic).
-3. Preserve existing API contracts (other projects may depend on the package).
-4. Run tests after changes: `pytest tests/ -v`
-5. Keep `requirements.txt` and `pyproject.toml` in sync.
+If a synced change breaks a project:
+
+1. Identify the broken component
+2. Restore previous version in target project
+3. Report issue to `~/developer/`
+4. Fix in developer repo
+5. Re-sync when ready
 
 ---
 
-## Commit style
+## Quick start for new components
+
+To add a new shared component:
 
-- English identifiers
-- `feat/fix/test/docs/chore/canon` prefix
-- Never commit secrets
-- Format: `type(scope): message [IL-XXX]`
+1. Create in appropriate directory (`scripts/`, `templates/`, etc.)
+2. Add documentation header with purpose and usage
+3. Test in isolation
+4. Commit to `~/developer/`
+5. Manually sync to interested projects
+6. Update this AGENTS.md if needed
+
+---
+
+## People and responsibilities
+
+| Role | Person | Scope |
+|------|--------|-------|
+| Component author | Any developer | Create/maintain specific components |
+| Sync coordinator | Moriel Carmi | Approve cross-project distribution |
+| Integration tester | Qoder CLI | Validate synced components work |
 
 ---
 
 ## Files reference
 
-| File | Purpose | Authority |
-|------|---------|-----------|
-| `FACTORY_OPERATING_SYSTEM.md` | Universal root canon — all contours | **ROOT** |
-| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | Execution law (audit-first, non-atomic) | **ROOT** |
-| `.claude/CLAUDE_CODE_CANON.md` | Session canon (Rules 1–9) | Session |
-| `AGENTS.md` | This file — terminal architecture | Project |
-| `COLLAB.md` | Collaboration patterns | Project |
-| `CLAUDE.md` | Project identity (BANXE gateway) | Project |
+| File | Purpose | Sync targets |
+|------|---------|--------------|
+| `AGENTS.md` | This file — three-partner agent instructions | All projects |
+| `.qoder/config.yml` | Qoder CLI configuration | All projects |
+| `.qoder/context.md` | Qoder execution contract (UNIVERSAL) | All projects |
+| `docs/COLLAB.md` | Collaboration documentation | All projects |
+| `docs/MCP-BEST-PRACTICES.md` | MCP server guide | All projects |
+| `docs/PROJECT-REGISTRY.csv` | Project registry for sync-all.sh | Internal use |
+| `scripts/sync-all.sh` | Multi-repo sync automation | Internal use |
+| `scripts/onboard-project.sh` | New project onboarding | Internal use |
+| `scripts/check-agent-instructions.sh` | Diagnostic tool | All projects |
+| `compliance/COMPLIANCE_ARCH.md` | Compliance invariants | vibe-coding |
 
 ---
 
-## Definition of done
+## Definition of done (for component development)
 
-A task is complete when:
+A component is ready for sync when:
 
-- [ ] Factory execution verified (Aider/Codex)
-- [ ] Tests pass (`pytest`)
-- [ ] Lint clean (`ruff`)
-- [ ] Audit trail recorded
-- [ ] Commit with proper format
-- [ ] No secrets committed
+- [ ] Implementation complete and tested
+- [ ] Documentation header added
+- [ ] No project-specific assumptions
+- [ ] Works in isolation
+- [ ] Backward-compatible or migration documented
+- [ ] Committed to `~/developer/`
+- [ ] Synced to at least one target project
 
 ---
 
-*Updated: 2026-08-26 (normalized v1.1)*  
-*Alignment: FACTORY_OPERATING_SYSTEM.md v1.1, CLAUDE_CODE_OPERATING_PRINCIPLE.md v1.1*
+## Next steps (pending work)
+
+- [x] Create sync-all.sh for automated distribution
+- [x] Update AGENTS.md with three-partner architecture
+- [x] Create onboard-project.sh for new project onboarding
+- [ ] Create git post-commit hook for auto-sync
+- [ ] Deploy full Qoder stack to banxe-mirofish
+- [ ] Create project-specific MIROFISH-SCENARIOS.md for all 6 projects
+- [ ] Update MEMORY.md with three-partner documentation
diff --git a/CLAUDE_CODE_OPERATING_PRINCIPLE.md b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
index f0512a8..05ad028 100644
--- a/CLAUDE_CODE_OPERATING_PRINCIPLE.md
+++ b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
@@ -288,16 +288,14 @@ This §13 **overrides** any local instruction implying:
 | File | Purpose | AUDIT-FIRST Status |
 |------|---------|-------------------|
 | `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | This document — universal root-level rule | ✅ DEFINES |
-| `FACTORY_OPERATING_SYSTEM.md` | Factory operating system — all contours | ✅ REFERENCES THIS DOC |
 | `.claude/CLAUDE_CODE_CANON.md` | Session canon (Rules 1–9 + extensions) | ✅ REFERENCES THIS DOC |
 | `docs/canon/software-factory-canon-v1.md` | Factory operating model | ✅ REFERENCES THIS DOC |
-| `AGENTS.md` (root) | Terminal architecture | ✅ PROPAGATES |
-| `COLLAB.md` (root) | Project collaboration | ✅ PROPAGATES |
+| `AGENTS.md` | Three-partner architecture | ✅ PROPAGATES |
+| `COLLAB.md` | Project collaboration | ✅ PROPAGATES |
 | `free-claude-code/CLAUDE.md` | FCC subproject canon | ✅ ALIGNED |
 
 ---
 
-*Enacted: 2026-08-26*  
-*Version: 1.1 (normalized)*  
+*Enacted: 2026-08-25*  
 *Authority: Operator directive — root-level universal*  
 *Supersedes: All subordinate atomic/stop-and-wait instructions unless canon-boundary sanctioned*
diff --git a/FACTORY_OPERATING_SYSTEM.md b/FACTORY_OPERATING_SYSTEM.md
index 7538872..22cc352 100644
--- a/FACTORY_OPERATING_SYSTEM.md
+++ b/FACTORY_OPERATING_SYSTEM.md
@@ -1,4 +1,4 @@
-# FACTORY OPERATING SYSTEM v1.1
+# FACTORY OPERATING SYSTEM v1.0
 ## ROOT-LEVEL UNIVERSAL ARTIFACT — ALL TERMINALS / ALL CONTOURS
 
 **Status:** EFFECTIVE IMMEDIATELY  
@@ -35,8 +35,8 @@ Every task must utilize all available Factory agents and workers in their respec
 
 ### 1.4 Factory Execution Only
 Production code is written **exclusively** by:
-- **Aider** (via MCP/Qoder) — **primary executor**
-- **Codex** (plugin/CLI) — **secondary executor** when enabled
+- **Aider** (via MCP/Qoder) — primary executor
+- **Codex** (plugin/CLI) — secondary executor when enabled
 - **Factory agents** — via controlled task queue
 
 **Claude Code NEVER writes production code.** Claude Code assigns, plans, reviews, validates.
@@ -191,74 +191,9 @@ CONSULT PROMPTS:
 
 ---
 
-## 6. ROUTING POLICY — CLOUD-FIRST FCC WITH TIERED DATA BOUNDARY
+## 6. CANON OVERRIDE RULE
 
-### 6.1 Primary Development Route
-Claude Code-compatible requests are routed through **Free Claude Code (FCC)** gateway to explicit allowlist of cloud providers/models.
-
-### 6.2 Data Classification & Routing Matrix
-| Data Class | Routing | Examples |
-|------------|---------|----------|
-| **Non-protected** | Cloud-first FCC | Synthetic fixtures, architecture/design, ADRs, scaffolding, tests, docs, sanitized debugging |
-| **Protected** | Local-only (Ollama) | Secrets, KYC/AML, payment/ledger, production logs, regulated evidence |
-| **Mixed** | Decomposed — cloud for logic, local for data | Feature with both scaffolding and PII |
-
-### 6.3 Compatibility Boundary
-- FCC preserves Claude Code interface
-- Direct provider calls by agents remain disallowed unless separately approved
-- LiteLLM and local Ollama remain approved fallback for offline/protected workloads
-
-### 6.4 Mandatory Controls
-Provider/model allowlist, loopback-bound gateway, task/route/model audit records, spend/quota limits, credential isolation, tested rollback.
-
----
-
-## 7. CONSULT POLICY MATRIX (sandbox/preprod/prod × reversible/material/irreversible)
-
-| Environment | Reversible | Material | Irreversible |
-|-------------|------------|----------|--------------|
-| **Sandbox** | Advisory — single opinion | Codex primary + Fable second | Codex + Fable parallel + operator |
-| **Preprod** | Codex single | Codex + Fable | Full chain + operator sanction |
-| **Prod** | Codex single | Full consult chain | Full chain + MLRO/CTIO + operator |
-
-**Irreversible =** secret exposure, production data leak, financial transaction, architectural lock-in.
-
----
-
-## 8. AUTO-COMMIT SCOPE (Factory Contour Only)
-
-### 8.1 Principle
-In controlled environment (sandbox/governed factory contour), valuable untracked files **must not** automatically hang in "wait for operator" state.
-
-### 8.2 Auto-Commit Criteria
-| Category | Action |
-|----------|--------|
-| Safe valuable untracked (docs, canons, policies, sources) | **AUTO-COMMIT** after triage |
-| Safe trash/temp/backups | Delete or add to .gitignore |
-| Local settings/runtime | Leave untracked or .gitignore |
-| Secrets/credentials | **RISK BUCKET** — no auto-commit |
-| Unknown/suspicious binaries | **RISK BUCKET** — no auto-commit |
-
-### 8.3 Central Terminal Exception
-**Central terminal does NOT auto-commit.** Central plans/reviews; Factory (Left) executes commits. Auto-commit applies **only** to Factory contour operations.
-
----
-
-## 9. TERMINAL NAMING UNIFICATION
-
-| Legacy Name | Canonical Name | Role |
-|-------------|----------------|------|
-| Left | **LEFT / Factory Interface** | Task assignment, agent orchestration |
-| Central / Brain | **CENTRAL** | Planning, review, decision, verification |
-| Right / BEN | **RIGHT / Assistant** | Research, audit, summary, brief preparation |
-
-All documentation must use canonical names. Legacy references should be updated on next edit.
-
----
-
-## 10. CANON OVERRIDE RULE
-
-### 10.1 Cancelled Formulations
+### 6.1 Cancelled Formulations
 Any instruction implying:
 - "complete one step and wait" ❌
 - "stop after audit and ask" ❌
@@ -271,7 +206,7 @@ Any instruction implying:
 - Explicit canon-required sanction boundary
 - Real fork requiring operator decision
 
-### 10.2 Preserved Sanction Boundaries
+### 6.2 Preserved Sanction Boundaries
 These remain valid stops:
 - MLRO gate (compliance changes)
 - CTIO gate (architecture changes)
@@ -282,19 +217,19 @@ These remain valid stops:
 
 ---
 
-## 11. PROPAGATION TO ALL CONTOURS
+## 7. PROPAGATION TO ALL CONTOURS
 
-### 11.1 Read Obligation
+### 7.1 Read Obligation
 This document MUST be read by:
 - **Left Terminal** — before Factory task assignment
 - **Factory** — before code generation
 - **Central Terminal** — before planning/orchestration
 - **Right Terminal** — before audit/summary tasks
 
-### 11.2 One Recording, Universal Application
+### 7.2 One Recording, Universal Application
 Recording this principle in root-level `FACTORY_OPERATING_SYSTEM.md` binds all contours. Local copies are references, not substitutes.
 
-### 11.3 Alignment Requirement
+### 7.3 Alignment Requirement
 All instruction-bearing documents must align:
 - canon files
 - README / REDMI
@@ -307,20 +242,19 @@ All instruction-bearing documents must align:
 
 ---
 
-## 12. EXCEPTIONS (SANCTIONED ONLY)
+## 8. EXCEPTIONS (SANCTIONED ONLY)
 
 | Exception | Justification | Approval |
 |-----------|---------------|----------|
 | Emergency direct edit | System down, no Factory path | Operator real-time sanction |
 | Documentation-only change | No code impact, markdown only | Documented in commit |
 | Factory bypass for experiment | Explicit research mode | Operator pre-approval |
-| Integration preparation | Operator-directed merge prep | Operator directive (this document) |
 
 **Default:** No exceptions. Factory-only coding is absolute.
 
 ---
 
-## 13. AMENDMENT RULES
+## 9. AMENDMENT RULES
 
 - **Operator approval** — all amendments
 - **CTIO approval** — structural changes (roles, tiers, consult chain)
@@ -333,14 +267,59 @@ All instruction-bearing documents must align:
 | Source | Factory-Only | Cheap-First | Non-Atomic | Audit-First | Shell Audit | Consult Chain | Status |
 |--------|--------------|-------------|------------|-------------|-------------|---------------|--------|
 | `FACTORY_OPERATING_SYSTEM.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **THIS DOCUMENT** |
-| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Aligned v1.1 |
-| `AGENTS.md` (root) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Updated v1.1 |
-| `docs/canon/software-factory-canon-v1.md` | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | References this doc |
-| `.claude/CLAUDE_CODE_CANON.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Rule 9 overridden |
+| `.claude/CLAUDE_CODE_CANON.md` | ✅ | ❌ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | Needs update |
+| `docs/canon/software-factory-canon-v1.md` | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | Needs update |
+| `docs/canon/smart-model-routing-protocol-v1.md` | ❌ | ✅ | ❌ | ❌ | ❌ | ⚠️ | Reference only |
+| `factory-target-model-policy.md` | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | Reference only |
+| `AGENTS.md` (root) | ⚠️ | ❌ | ⚠️ | ❌ | ❌ | ❌ | Needs update |
+| `COLLAB.md` (root) | ✅ | ❌ | ⚠️ | ⚠️ | ⚠️ | ❌ | Needs update |
+| `free-claude-code/AGENTS.md` | ❌ **CONFLICT** | ❌ | ❌ | ❌ | ❌ | ❌ | **MUST FIX** |
+
+## 10. SANDBOX AUTO-COMMIT PRINCIPLE (Controlled Environment)
+
+### 10.1 Scope
+This principle applies when work is performed in:
+- Sandbox / controlled worktree;
+- Governed factory contour;
+- Environment without external risk factors.
+
+### 10.2 Valuable Files Do Not Wait
+In controlled environment, valuable untracked files **must not** automatically hang in "wait for operator sanction" state.
+
+After audit-and-triage:
+- Separate trash from valuable files;
+- Separate secrets/local runtime from useful artifacts;
+- For valuable safe untracked files — execute **governed automatic commit** without waiting for separate operator sanction.
+
+### 10.3 Auto-Commit Criteria
+| Category | Action |
+|----------|--------|
+| Safe valuable untracked (docs, canons, policies, sources) | **AUTO-COMMIT** after triage |
+| Safe trash/temp/backups | Delete or add to .gitignore |
+| Local settings/runtime | Leave untracked or .gitignore |
+| Secrets/credentials | **RISK BUCKET** — no auto-commit |
+| Unknown/suspicious binaries | **RISK BUCKET** — no auto-commit |
+| Large external/vendor artifacts | Review case-by-case |
+
+### 10.4 Risk Bucket Exception
+If untracked files include:
+- Secrets or credentials;
+- Unknown binaries;
+- Suspicious external artifacts;
+- Potentially dangerous executables;
+
+then auto-commit **does not apply** — these paths go to risk bucket for operator review.
+
+### 10.5 Override Rule
+In sandbox/controlled environment, waiting for sanction on safe valuable untracked files is considered **obsolete blocking logic** and is **cancelled**.
+
+**Preserved blocks:**
+- Real risk categories;
+- Merge/push restrictions (unless explicitly allowed by sandbox rules);
+- Secrets/credentials exposure risk.
 
 ---
 
-*Enacted: 2026-08-26*  
-*Version: 1.1 (normalized)*  
+*Enacted: 2026-08-25*  
 *Authority: Operator directive — root-level universal, all contours*  
 *Supersedes: All factory/canon instructions where conflict exists*
diff --git a/.claude/CLAUDE_CODE_CANON.md b/.claude/CLAUDE_CODE_CANON.md
index 2295863..6d68d61 100644
--- a/.claude/CLAUDE_CODE_CANON.md
+++ b/.claude/CLAUDE_CODE_CANON.md
@@ -1,5 +1,9 @@
 # Claude Code Session Canon (ABSOLUTE)
 
+**Root-Level Override:** `FACTORY_OPERATING_SYSTEM.md` takes precedence for FACTORY-ONLY CODING / TIERED MODEL ECONOMY / NON-ATOMIC / AUDIT-FIRST execution. This canon remains binding where not in conflict.
+
+**CRITICAL:** Claude Code NEVER writes production code directly. All code generation goes through Factory (Aider/Codex). See `FACTORY_OPERATING_SYSTEM.md` §1.
+
 Every Claude Code sprint prompt MUST include this block verbatim at the top.
 
 ## Rules
@@ -61,7 +65,7 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
    operator instruction, handled sequentially (INV-08; `COLLAB.md` §Cross-project work). [ФАКТ]
 4. **Route unsafe/state-changing work to the operator gate.** Emit exactly one `OPERATOR_RUN` line, then
    STOP and wait for "go" (Rule 3) — this is how tasks reach LEFT for execution. [ФАКТ]
-5. **Cloud-first FCC routing.** Claude Code routes through local FCC gateway to approved allowlisted cloud models for non-protected data; LiteLLM/local inference remains fallback for protected workloads and offline operation. [ФАКТ]
+5. **Cloud-first development is permitted through FCC.** Claude Code routes through a local FCC gateway to approved allowlisted cloud models; LiteLLM/local inference remains the fallback. Sensitive banking data must remain local.
 6. **One best step out.** Per Rules 1, 8 — CENTRAL emits a single best next action (a prompt to the
    factory or an `OPERATOR_RUN`), never a menu. [ФАКТ]
 
@@ -74,3 +78,24 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
   with INV-01/INV-08 or `COLLAB.md` single-terminal canon, the invariant/COLLAB wins and this section is
   read as role-separation-within-one-terminal only.
 - [ФАКТ] Amendments follow `software-factory-canon-v1.md` §11 (Operator approval; CTIO for structural).
+
+
+## Cloud-first development routing amendment
+
+**Status:** EFFECTIVE by Operator directive; implementation remains staged and auditable.
+
+1. **Primary development route:** Claude Code-compatible requests may be routed through a local Free Claude Code (FCC) gateway to an explicit allowlist of cloud providers/models.
+2. **Compatibility boundary:** FCC preserves the Claude Code interface; direct provider calls by agents remain disallowed unless separately approved.
+3. **Local continuity:** LiteLLM and local Ollama remain approved fallback routes for offline operation, continuity, and protected workloads.
+4. **Data boundary:** Cloud routes MUST NOT receive secrets, credentials, real customer data, KYC/KYB/AML cases, payment or ledger payloads, production logs, regulated evidence, or other sensitive banking data.
+5. **Permitted cloud work:** Synthetic fixtures, non-sensitive architecture/design, ADRs, code scaffolding, tests, migrations, documentation, and sanitized debugging.
+6. **Controls:** Provider/model allowlist, loopback-bound gateway, task/route/model audit records, spend/quota limits, credential isolation, and tested rollback are mandatory before provider activation.
+7. **Architecture boundary:** FCC accelerates development only. Banking architecture remains based on domain patterns: double-entry ledger, CQRS/event sourcing, KYC/AML orchestration, and ISO 20022/payment adapters.
+
+> **Smart Model Routing:** `docs/canon/smart-model-routing-protocol-v1.md` is the governing role, trust-tier, preflight, and independent-review protocol for this document.
+
+## Smart Routing Precedence
+
+For model selection, execution-role assignment, gateway routing, trust-tier handling, preflight, and independent-review requirements, `docs/canon/smart-model-routing-protocol-v1.md` takes precedence over earlier conflicting wording in this document.
+
+Earlier references to a sole executor, local-only inference, gateway-only routing, or legacy routing behavior remain historical/contextual unless they are explicitly restated in the Smart Model Routing Protocol.
diff --git a/AGENTS.md b/AGENTS.md
index 74fd3f2..ae5251f 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -7,18 +7,14 @@
 
 ---
 
-## ⚠️ FACTORY OPERATING SYSTEM (Root-Level Universal)
+## ⚠️ ROOT CANON — единый SSOT (2026-08-26)
 
-All agent execution follows `FACTORY_OPERATING_SYSTEM.md`:
-- **FACTORY-ONLY CODING:** No terminal codes directly; Factory (Aider/Codex) executes all production code.
-- **ALL FACTORY STAFF ENABLED:** All available Factory agents and workers must execute their roles unless restricted by task canon.
-- **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive for **concise final verification only**.
-- **NON-ATOMIC:** Continuous execution across non-branching work.
-- **AUDIT-FIRST:** Fresh shell audit before each material step.
-- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks.
-- **CLOUD-FIRST FCC:** Non-protected data → cloud via FCC; protected data → local Ollama.
-
-Main Claude resource verifies outputs/findings/summaries from cheap contour, not re-processes bulk work from scratch.
+Терминальный workflow всех контуров определяет **один файл**:
+`banxe-ai-rnd/research` → `docs/canon/CANON-FACTORY-SSOT.md`, норма **CORE-10-29**
+(исполнитель кода Aider/Codex, Claude Code оркеструет; cloud-vs-local по классу данных;
+непрерывный фронт + STOP-гейты; consult-цепь Codex → Fable → Mistral → Kimi; auto-commit только
+Фабрикой; имена CENTRAL / LEFT / RIGHT). `FACTORY_OPERATING_SYSTEM.md` и
+`CLAUDE_CODE_OPERATING_PRINCIPLE.md` в этом репозитории — указатели туда, не копии (ADR-102).
 
 ---
 
@@ -42,9 +38,8 @@ This repository is the **MetaClaw meta-learning framework** — agents learn and
 ## Instruction hierarchy
 
 1. **Explicit user instruction** (highest authority)
-2. **Root-level canons**:
-   - `FACTORY_OPERATING_SYSTEM.md` (universal)
-   - `CLAUDE_CODE_OPERATING_PRINCIPLE.md` (execution law)
+2. **Root-level canon**: `research/docs/canon/CANON-FACTORY-SSOT.md` (CORE-10-29);
+   `FACTORY_OPERATING_SYSTEM.md` / `CLAUDE_CODE_OPERATING_PRINCIPLE.md` здесь — указатели
 3. **Session canon**:
    - `.claude/CLAUDE_CODE_CANON.md` (Rules 1–9 + terminal extensions)
 4. **Project context**:
@@ -81,47 +76,9 @@ This repository is the **MetaClaw meta-learning framework** — agents learn and
 
 ## Terminal Roles Detail
 
-### CENTRAL (Brain)
-
-**Allowed:**
-- Plan, review, orchestrate, decide, delegate
-- Concise final verification of factory outputs
-- Read root-level system before work starts
-- Assign tasks to Factory
-
-**Prohibited:**
-- Direct file edits
-- Direct code writing
-- Direct `Edit`, `Write` for production code
-
-### LEFT (Factory Interface)
-
-**Allowed:**
-- Assign tasks to all factory agents
-- Review output, route evidence
-- Shell CI/CD / infra / audits
-
-**Prohibited:**
-- Direct code generation outside Factory
-- Originate logic that bypasses factory
-
-### RIGHT (Assistant)
-
-**Allowed:**
-- Research, audit, summarize, prepare briefs
-- Read-only document scouting
-- Tag findings [FACT]/[INFERENCE]/[UNKNOWN]
-
-**Prohibited:**
-- Any code execution
-- File edits
-
-### Factory (Aider + Codex + agents)
-
-**Execution only:**
-- Aider (via MCP) — primary executor
-- Codex (plugin/CLI) — secondary executor
-- Factory agents — via controlled task queue
+Роли CENTRAL (Brain) / LEFT (Factory Interface) / RIGHT (Assistant) и исполнители Фабрики
+(Aider primary, Codex secondary, агенты очереди) — нормативно в SSOT `CANON-FACTORY-SSOT.md`
+CORE-10-29 п.1 и п.6; здесь не дублируются.
 
 ---
 
@@ -159,8 +116,7 @@ This repository is **MetaClaw only**. Do not mix files, code, or context with:
 
 ## Before making changes
 
-1. Read `FACTORY_OPERATING_SYSTEM.md` §1 (Factory-Only Coding).
-2. Read `CLAUDE_CODE_OPERATING_PRINCIPLE.md` §4 (Non-Atomic).
+1. Read `CANON-FACTORY-SSOT.md` CORE-10-29 п.1 (Factory-only coding) и п.3 (non-atomic).
 3. Preserve existing API contracts (other projects may depend on the package).
 4. Run tests after changes: `pytest tests/ -v`
 5. Keep `requirements.txt` and `pyproject.toml` in sync.
@@ -180,8 +136,8 @@ This repository is **MetaClaw only**. Do not mix files, code, or context with:
 
 | File | Purpose | Authority |
 |------|---------|-----------|
-| `FACTORY_OPERATING_SYSTEM.md` | Universal root canon — all contours | **ROOT** |
-| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | Execution law (audit-first, non-atomic) | **ROOT** |
+| `FACTORY_OPERATING_SYSTEM.md` | Pointer → SSOT CORE-10-29 | pointer |
+| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | Pointer → SSOT CORE-10-29 | pointer |
 | `.claude/CLAUDE_CODE_CANON.md` | Session canon (Rules 1–9) | Session |
 | `AGENTS.md` | This file — terminal architecture | Project |
 | `COLLAB.md` | Collaboration patterns | Project |
@@ -203,4 +159,4 @@ A task is complete when:
 ---
 
 *Updated: 2026-08-26 (normalized v1.1)*  
-*Alignment: FACTORY_OPERATING_SYSTEM.md v1.1, CLAUDE_CODE_OPERATING_PRINCIPLE.md v1.1*
+*Alignment: research/docs/canon/CANON-FACTORY-SSOT.md v7 / CORE-10-29 (2026-08-26)*
diff --git a/CLAUDE_CODE_OPERATING_PRINCIPLE.md b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
index f0512a8..3555bf3 100644
--- a/CLAUDE_CODE_OPERATING_PRINCIPLE.md
+++ b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
@@ -1,303 +1,14 @@
-# CLAUDE CODE OPERATING PRINCIPLE — AUDIT-FIRST / NON-ATOMIC / ECONOMY-FIRST
+# CLAUDE CODE OPERATING PRINCIPLE — POINTER (v1.1 → сведено в единый SSOT, 2026-08-26)
 
-**Status:** EFFECTIVE IMMEDIATELY — ROOT-LEVEL UNIVERSAL ARTIFACT  
-**Scope:** All terminals (LEFT / CENTRAL / RIGHT), all Factory contours, all Claude Code-compatible execution planes  
-**Supersedes:** Any older instruction implying atomic stop-and-wait, guess-based continuation, or action-before-audit  
-**Authority:** Operator directive — binding on all subordinate canons  
+**Этот файл — указатель, не норма.** Audit-first, shell-аудит перед каждым материальным шагом,
+непрерывный (non-atomic) фронт до настоящей развилки, закрытый список STOP, consult-цепь
+Codex → Fable → Mistral → Kimi, экономика уровней моделей, cloud-first FCC по классу данных,
+auto-commit только контуром Фабрики, отменённые формулировки — всё это теперь живёт в:
 
----
+> `banxe-ai-rnd/research` → `docs/canon/CANON-FACTORY-SSOT.md`:
+> **CORE-10-29** (п.1–6), **CORE-10-21** (работа по реальному состоянию, аудит предшествует
+> действию), нормы **17** / **CORE-10-22** (развилка = обращение), **CORE-10-26** (места
+> консультантов и замещение), **CORE-10-28** (FCC только через Фабрику).
 
-## 1. PRIMARY OPERATING LAW
-
-Claude Code must work in **AUDIT-FIRST** mode at every stage:
-- first audit;
-- then decision;
-- then execution;
-- then re-audit before the next decision.
-
-No meaningful next step may be chosen without a fresh audit of the current state.  
-No decision may be justified by memory, assumption, stale context, or prior plan alone.
-
----
-
-## 2. SHELL AUDIT IS MANDATORY
-
-Shell Audit is embedded into Claude Code workflow and is **not optional**.
-
-Before every material step Claude Code must perform or consume a read-only shell audit that establishes:
-- current branch / HEAD / worktree state;
-- relevant file paths and target artifacts;
-- current repo status and diffs;
-- presence/absence of blockers;
-- whether prior assumptions still hold.
-
-Shell Audit is used to determine facts, location, and current state.  
-**Decision first, audit later is forbidden.**
-
-If a shell audit is unavailable, Claude Code must perform an equivalent read-only audit itself before proceeding.
-
----
-
-## 3. AUDIT BEFORE EVERY STEP
-
-The workflow is cyclical:
-
-```
-AUDIT -> DECIDE -> EXECUTE -> AUDIT -> DECIDE -> EXECUTE
-```
-
-This applies before:
-- editing files;
-- generating prompts;
-- changing docs;
-- updating canon/README/ledgers;
-- starting or continuing recovery;
-- proposing merge-ready conclusions;
-- declaring a branch closed;
-- escalating to consultants.
-
-Every step must be grounded in the immediately preceding audit.
-
----
-
-## 4. NON-ATOMIC EXECUTION DEFAULT
-
-Atomic stop-after-one-step instructions are **cancelled by default** for Claude Code.
-
-**Cancelled pattern:**
-- do one step;
-- stop;
-- wait for operator;
-- do next step only after confirmation.
-
-**Replacement pattern:**
-- continue in a unified front;
-- do all non-branching work in one continuous pass;
-- stop only at a real fork, sanction gate, or explicit irreversible boundary.
-
-If there is no real fork, Claude Code must not pause just because one substep completed.
-
----
-
-## 5. WHAT COUNTS AS A REAL STOP
-
-Claude Code may stop only for:
-- a genuine fork that cannot be resolved from canon + audit + facts;
-- an irreversible action that canon reserves for owner/operator sanction;
-- missing authority;
-- conflicting norms that require consultation;
-- unknowns that would force fabrication.
-
-Completion of a substep alone is **NOT** a valid stop reason.
-
----
-
-## 6. ECONOMY PRINCIPLE
-
-The workflow must be optimized for operator attention economy and token economy:
-- do not ask intermediate questions when the answer can be derived by audit;
-- do not split straightforward work into artificial micro-steps;
-- do not create ceremonial pauses;
-- do not produce redundant explanations between steps;
-- do one coherent pass for all non-branching work.
-
-Audit frequency must be high; interruption frequency must be low.
-
----
-
-## 7. CONSULT CHAIN ON FORKS
-
-At a real fork, Claude Code must prepare a consultation packet instead of asking a casual question.
-
-**Strict consultant order:**
-1. **Codex** — primary consultant
-2. **Fable** — second opinion
-3. **Mistral** — third opinion
-4. **Kimi** — fourth opinion
-
-Each fork packet must include:
-- fork title;
-- FACT;
-- INFERENCE;
-- UNKNOWN;
-- options;
-- risks;
-- recommended option;
-- consultant-specific prompts in the exact order above.
-
-Independent non-blocked work must continue while the blocked branch is isolated.
-
----
-
-## 8. CANON OVERRIDE RULE
-
-If any local instruction says or implies:
-- "complete one step and wait";
-- "stop after audit and ask";
-- "do not proceed to next step automatically";
-- "return after each atomic subtask";
-- "single summary after sprint" (legacy Rule 9);
-
-then for Claude Code this instruction is **overridden by this operating principle**, unless:
-- the canon explicitly requires owner/operator sanction at that exact boundary; or
-- the boundary is a real fork.
-
----
-
-## 9. README / REDMI / CANON / NOTES ALIGNMENT
-
-All instruction-bearing locations that Claude Code reads must reflect the same law:
-- canon;
-- README / REDMI;
-- runbooks;
-- factory preambles;
-- operator notes;
-- workflow specs;
-- prompt templates;
-- recovery procedures;
-- audit procedures.
-
-Any contradictory wording must be rewritten to:  
-**"audit first, then decision; continue non-atomically unless a real fork or sanction gate exists."**
-
----
-
-## 10. REQUIRED EXECUTION STYLE
-
-Claude Code must explicitly report in factual form:
-- latest audit basis;
-- what decision that audit justified;
-- what actions were executed under that audit;
-- what next audit is required;
-- whether a real fork exists;
-- whether continuation now requires sanction.
-
----
-
-## 11. HARD PROHIBITIONS
-
-**Forbidden:**
-- acting on stale assumptions;
-- skipping shell audit before a material step;
-- using atomic stop-and-wait as default;
-- asking for confirmation merely because a substep ended;
-- fabricating certainty where audit has not confirmed it;
-- replacing audit with memory of prior repo state.
-
-**Required:**
-- fresh audit before each material step;
-- shell audit embedded in Claude Code work;
-- continuous non-atomic progress across all non-branching work;
-- consultation packet on real forks;
-- sanction stop only where canon truly requires it.
-
----
-
-## 12. AMENDMENT RULES
-
-- **Operator approval** required for all amendments to this document.
-- **CTIO approval** required for structural changes (modification of consult chain, stop criteria, or override scope).
-- Emergency amendments: Operator may apply temporary amendment with 72-hour expiry; must be ratified or reverted within the window.
-
----
-
-## 13. TOKEN ECONOMY / MODEL TIER PRINCIPLE
-
-### 13.1 Factory-only coding with all staff enabled
-
-**Code generation and production work goes ONLY through the Factory.**
-
-- No terminal codes directly;
-- Any terminal assigns tasks to Factory;
-- Factory forms code and leads continuous work;
-- **All available Factory agents and workers must be included in the contour and execute their roles** unless explicitly restricted by task canon.
-
-### 13.2 Bulk work = cheap models
-
-For token economy, all mass/auxiliary/preparatory/survey/diagnostic/draft work **must** use by default:
-- Free models where available;
-- Lower-tier runners;
-- Open Claude Code / factory fleet models;
-- Any approved lower-cost routing.
-
-### 13.3 Expensive base model = concise final verification only
-
-Expensive base model (primary Claude Code / Opus-class verifier) **does not** process the full routine stream.
-
-**Reserved for concise verification of:**
-- Outputs, findings, summaries produced by cheap contour;
-- Diffs and conclusions from Factory agents;
-- Final decision;
-- Critical validation;
-- Final quality gate.
-
-**NOT for:** re-processing full bulk work from scratch.
-
-### 13.4 Routing hierarchy
-
-| Work type | Default route | Exception |
-|-----------|---------------|-----------|
-| Bulk/diagnostic/auxiliary | Lower-tier / free | When complexity requires upgrade |
-| Final review/decision | Expensive / Opus-class | Never downgrade for material decisions |
-| Fork consultation | As per §7 chain | Operator override |
-
-### 13.5 Continuous execution until fork
-
-Work proceeds continuously, as a unified front:
-- NOT "one step, then wait";
-- NOT atomic stop-after-each-step;
-- Continuous until real fork, sanction boundary, or missing authority.
-
-### 13.6 Audit before every material step
-
-Shell Audit is **embedded** into Claude Code / Factory workflow:
-- First audit;
-- Then decision;
-- Then execution;
-- Then new audit before next material step.
-
-### 13.7 Fork = consultation brief
-
-At a real fork:
-- Textual brief is formed for consultants;
-- Operator conducts consultation externally;
-- Operator returns result to terminal;
-- Work continues continuously to next fork.
-
-### 13.8 Central terminal brain
-
-Central terminal (Claude Code):
-- **Reads** root-level system before work starts;
-- **Assigns** tasks to Factory;
-- **Does not** execute code directly;
-- **Orchestrates** via audit-first principle.
-
-### 13.9 Override confirmation
-
-This §13 **overrides** any local instruction implying:
-- Direct coding outside factory;
-- Atomic stop-after-one-step as default;
-- Expensive model for routine bulk work by default;
-- No audit before next step;
-- Casual question instead of fork brief.
-
----
-
-## Appendix: Root-Level Instruction Bearing Files (MetaClaw)
-
-| File | Purpose | AUDIT-FIRST Status |
-|------|---------|-------------------|
-| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | This document — universal root-level rule | ✅ DEFINES |
-| `FACTORY_OPERATING_SYSTEM.md` | Factory operating system — all contours | ✅ REFERENCES THIS DOC |
-| `.claude/CLAUDE_CODE_CANON.md` | Session canon (Rules 1–9 + extensions) | ✅ REFERENCES THIS DOC |
-| `docs/canon/software-factory-canon-v1.md` | Factory operating model | ✅ REFERENCES THIS DOC |
-| `AGENTS.md` (root) | Terminal architecture | ✅ PROPAGATES |
-| `COLLAB.md` (root) | Project collaboration | ✅ PROPAGATES |
-| `free-claude-code/CLAUDE.md` | FCC subproject canon | ✅ ALIGNED |
-
----
-
-*Enacted: 2026-08-26*  
-*Version: 1.1 (normalized)*  
-*Authority: Operator directive — root-level universal*  
-*Supersedes: All subordinate atomic/stop-and-wait instructions unless canon-boundary sanctioned*
+Содержание CCOP v1.1 (коммит `0448d8b`, 2026-08-26 00:20) перенесено туда; лог —
+`docs/governance/SSOT-UNIFICATION-LOG-2026-08-26.md`. Копия правила здесь — дефект (ADR-102).
diff --git a/FACTORY_OPERATING_SYSTEM.md b/FACTORY_OPERATING_SYSTEM.md
index 7538872..531c6fc 100644
--- a/FACTORY_OPERATING_SYSTEM.md
+++ b/FACTORY_OPERATING_SYSTEM.md
@@ -1,346 +1,12 @@
-# FACTORY OPERATING SYSTEM v1.1
-## ROOT-LEVEL UNIVERSAL ARTIFACT — ALL TERMINALS / ALL CONTOURS
+# FACTORY OPERATING SYSTEM — POINTER (v1.1 → сведено в единый SSOT, 2026-08-26)
 
-**Status:** EFFECTIVE IMMEDIATELY  
-**Authority:** Operator directive — overrides all subordinate instructions  
-**Scope:** Left Terminal, Factory, Central Terminal Brain, Right Terminal  
-**Read-before-work:** MANDATORY for Claude Code and all Factory agents  
+**Этот файл — указатель, не норма.** Единственный источник истины по терминальному workflow
+всех контуров (CENTRAL / LEFT-Factory / RIGHT-Assistant, исполнитель кода, маршрутизация по
+классу данных, непрерывный фронт и STOP-гейты, consult-матрица, auto-commit, имена ролей):
 
----
+> `banxe-ai-rnd/research` → `docs/canon/CANON-FACTORY-SSOT.md`, норма **CORE-10-29**
+> (плюс нормы 2, 11, 17, 26, 27, 28).
 
-## 1. FACTORY-ONLY CODING LAW (ABSOLUTE)
-
-### 1.1 No Terminal Codes Directly
-- **NO** terminal (Left, Central, Right, Brain) writes production code directly.
-- **NO** Claude Code instance edits files as "execution".
-- **NO** agent bypasses the Factory execution layer.
-
-### 1.2 Factory Assignment Pattern
-```
-TERMINAL (any) → TASK ASSIGNMENT → FACTORY → CODE GENERATION
-       ↑                                    ↓
-   PLAN/REVIEW ←←←←←←←←←←←←←←←←← EVIDENCE
-```
-
-### 1.3 Terminal Roles (Execution-Prohibited; All Factory Staff Enabled)
-| Terminal | Allowed | Prohibited |
-|----------|---------|------------|
-| **Central (Brain)** | Plan, review, orchestrate, decide, delegate; concise final verification of factory outputs | Direct file edits, direct code writing |
-| **Left (Factory Interface)** | Assign tasks to all factory agents, review output, route evidence | Direct code generation outside Factory |
-| **Right (Assistant)** | Research, audit, summarize, prepare briefs | Any code execution |
-| **Any CC instance** | Analysis, planning, prompt engineering; concise verification of findings | Direct `Edit`, `Write` for production code |
-
-**All Available Factory Agents Rule:**
-Every task must utilize all available Factory agents and workers in their respective roles unless task canon explicitly restricts. No agent sits idle while work is assigned to expensive resource.
-
-### 1.4 Factory Execution Only
-Production code is written **exclusively** by:
-- **Aider** (via MCP/Qoder) — **primary executor**
-- **Codex** (plugin/CLI) — **secondary executor** when enabled
-- **Factory agents** — via controlled task queue
-
-**Claude Code NEVER writes production code.** Claude Code assigns, plans, reviews, validates.
-
----
-
-## 2. TIERED MODEL ECONOMY (TOKEN OPTIMIZATION)
-
-### 2.1 Work Classification
-| Work Type | Executor | Model Tier | Examples |
-|-----------|----------|------------|----------|
-| **Bulk/Prep/Research** | Factory agents / lower-tier | Cheap/free/lower-tier runners | grep, audit, summaries, fixture prep, doc search |
-| **Draft/Scaffold** | Factory | Economical capable | Code skeletons, test stubs, migrations |
-| **Primary Coding** | Aider/Codex | Strong cloud coding | Implementation, refactors, tests |
-| **Review/Verify** | Factory review layer | Stronger cloud review | Final validation, architecture check |
-| **Final Decision** | Central Terminal | Expensive base model | Concise verification of factory outputs; quality gate; merge approval |
-
-### 2.2 Expensive Model Conservation
-**Base model (Opus-class, primary Claude Code) is reserved for concise final verification:**
-- Reviews outputs/findings/summaries produced by cheap-tier agents;
-- Validates diffs and conclusions from Factory agents;
-- Final quality gate decisions;
-- Critical architecture validation;
-- Material fork resolution (after consult chain);
-- Operator-facing final review;
-- Compliance-sensitive sign-offs.
-
-**NOT for:**
-- Routine grep/audit
-- Bulk file reading
-- Draft scaffolding
-- Syntax fixes
-- Log analysis
-- Re-processing full bulk work from scratch
-
-### 2.3 Open Claude Code / Factory Fleet
-For token economy, Factory uses:
-- Free/cheap cloud tiers
-- Lower-tier runners
-- Local efficient models for prep work
-- FCC-routed economical models
-
-**Principle:** Spend tokens on final quality, not on exploration.
-
----
-
-## 3. NON-ATOMIC CONTINUOUS EXECUTION
-
-### 3.1 Cancelled Pattern (Explicitly Forbidden)
-```
-[DO ONE STEP] → [STOP] → [WAIT FOR OPERATOR] → [DO NEXT STEP]
-```
-
-### 3.2 Required Pattern (Continuous Front)
-```
-[AUDIT] → [DECIDE] → [EXECUTE] → [AUDIT] → [DECIDE] → [EXECUTE] → ...
-         ↑___________________________________________|
-              (continuous until real fork)
-```
-
-### 3.3 Real Forks Only (Where to Stop)
-Stop and wait **only** for:
-1. **Genuine fork** — cannot resolve from canon + audit + facts
-2. **Sanction gate** — requires explicit owner/operator approval
-3. **Irreversible boundary** — destructive action, secret exposure
-4. **Missing authority** — canon requires higher approval
-5. **Conflicting norms** — consultation required
-
-**NOT a valid stop:** substep completion, routine checkpoint, "just in case".
-
-### 3.4 Factory Loop Continuity
-Factory maintains continuous execution state:
-- No artificial micro-steps
-- No ceremonial pauses
-- No "confirm to proceed" between non-branching actions
-- Unified front until material decision point
-
----
-
-## 4. MANDATORY AUDIT-FIRST
-
-### 4.1 Shell Audit Embedding
-**Before EVERY material step:**
-```bash
-# MANDATORY READ-ONLY AUDIT
-git status
-git diff --stat
-ls -la <target paths>
-grep/pattern verification
-current state confirmation
-```
-
-### 4.2 Audit-Decision-Execution Cycle
-```
-1. SHELL AUDIT (read-only, establish facts)
-2. DECISION (based on audit, not memory)
-3. EXECUTION (factory-only for code)
-4. RE-AUDIT (before next material step)
-```
-
-### 4.3 Forbidden Substitutions
-- ❌ Memory of prior state
-- ❌ Assumption "still the same"
-- ❌ Stale context from prior turn
-- ❌ "Probably unchanged"
-
-### 4.4 Required Explicit Reporting
-Claude Code must report:
-- Latest audit basis (command outputs)
-- Decision justified by that audit
-- Actions executed under that audit
-- Next audit required
-- Fork existence (yes/no)
-- Sanction requirement (yes/no)
-
----
-
-## 5. CONSULT CHAIN ON FORKS (NO CASUAL QUESTIONS)
-
-### 5.1 Fork Handling Protocol
-At genuine fork:
-1. **STOP** execution (do not guess)
-2. **PREPARE BRIEF** — structured text packet
-3. **OPERATOR CONSULTS** — externally, via preferred channels
-4. **OPERATOR RETURNS** — result to terminal window
-5. **RESUME CONTINUOUS** — execution proceeds to next fork
-
-### 5.2 Brief Format (Required)
-```
-FORK: <title>
-FACT: <verified facts from audit>
-INFERENCE: <derived conclusions>
-UNKNOWN: <gaps>
-OPTIONS:
-  A. <option> — <risk>
-  B. <option> — <risk>
-RECOMMENDED: <option with justification>
-CONSULT PROMPTS:
-  - Codex: <specific question>
-  - Fable: <specific question>
-  - Mistral: <specific question>
-  - Kimi: <specific question>
-```
-
-### 5.3 Strict Consultant Order
-1. **Codex** — primary consultant (independent analysis)
-2. **Fable** — second opinion (challenges assumptions)
-3. **Mistral** — third perspective (diverse angle)
-4. **Kimi** — fourth review (completeness check)
-
-**Parallel execution:** Non-blocked work continues while fork is isolated.
-
----
-
-## 6. ROUTING POLICY — CLOUD-FIRST FCC WITH TIERED DATA BOUNDARY
-
-### 6.1 Primary Development Route
-Claude Code-compatible requests are routed through **Free Claude Code (FCC)** gateway to explicit allowlist of cloud providers/models.
-
-### 6.2 Data Classification & Routing Matrix
-| Data Class | Routing | Examples |
-|------------|---------|----------|
-| **Non-protected** | Cloud-first FCC | Synthetic fixtures, architecture/design, ADRs, scaffolding, tests, docs, sanitized debugging |
-| **Protected** | Local-only (Ollama) | Secrets, KYC/AML, payment/ledger, production logs, regulated evidence |
-| **Mixed** | Decomposed — cloud for logic, local for data | Feature with both scaffolding and PII |
-
-### 6.3 Compatibility Boundary
-- FCC preserves Claude Code interface
-- Direct provider calls by agents remain disallowed unless separately approved
-- LiteLLM and local Ollama remain approved fallback for offline/protected workloads
-
-### 6.4 Mandatory Controls
-Provider/model allowlist, loopback-bound gateway, task/route/model audit records, spend/quota limits, credential isolation, tested rollback.
-
----
-
-## 7. CONSULT POLICY MATRIX (sandbox/preprod/prod × reversible/material/irreversible)
-
-| Environment | Reversible | Material | Irreversible |
-|-------------|------------|----------|--------------|
-| **Sandbox** | Advisory — single opinion | Codex primary + Fable second | Codex + Fable parallel + operator |
-| **Preprod** | Codex single | Codex + Fable | Full chain + operator sanction |
-| **Prod** | Codex single | Full consult chain | Full chain + MLRO/CTIO + operator |
-
-**Irreversible =** secret exposure, production data leak, financial transaction, architectural lock-in.
-
----
-
-## 8. AUTO-COMMIT SCOPE (Factory Contour Only)
-
-### 8.1 Principle
-In controlled environment (sandbox/governed factory contour), valuable untracked files **must not** automatically hang in "wait for operator" state.
-
-### 8.2 Auto-Commit Criteria
-| Category | Action |
-|----------|--------|
-| Safe valuable untracked (docs, canons, policies, sources) | **AUTO-COMMIT** after triage |
-| Safe trash/temp/backups | Delete or add to .gitignore |
-| Local settings/runtime | Leave untracked or .gitignore |
-| Secrets/credentials | **RISK BUCKET** — no auto-commit |
-| Unknown/suspicious binaries | **RISK BUCKET** — no auto-commit |
-
-### 8.3 Central Terminal Exception
-**Central terminal does NOT auto-commit.** Central plans/reviews; Factory (Left) executes commits. Auto-commit applies **only** to Factory contour operations.
-
----
-
-## 9. TERMINAL NAMING UNIFICATION
-
-| Legacy Name | Canonical Name | Role |
-|-------------|----------------|------|
-| Left | **LEFT / Factory Interface** | Task assignment, agent orchestration |
-| Central / Brain | **CENTRAL** | Planning, review, decision, verification |
-| Right / BEN | **RIGHT / Assistant** | Research, audit, summary, brief preparation |
-
-All documentation must use canonical names. Legacy references should be updated on next edit.
-
----
-
-## 10. CANON OVERRIDE RULE
-
-### 10.1 Cancelled Formulations
-Any instruction implying:
-- "complete one step and wait" ❌
-- "stop after audit and ask" ❌
-- "do not proceed to next step automatically" ❌
-- "return after each atomic subtask" ❌
-- "Claude Code executes code" ❌
-- "single summary after sprint" ❌
-
-**IS OVERRIDDEN** by this document unless:
-- Explicit canon-required sanction boundary
-- Real fork requiring operator decision
-
-### 10.2 Preserved Sanction Boundaries
-These remain valid stops:
-- MLRO gate (compliance changes)
-- CTIO gate (architecture changes)
-- Operator gate (destructive operations)
-- Ruflo checkpoint (regulated quality gate)
-- Secret rotation / exposure risk
-- Production deployment to live systems
-
----
-
-## 11. PROPAGATION TO ALL CONTOURS
-
-### 11.1 Read Obligation
-This document MUST be read by:
-- **Left Terminal** — before Factory task assignment
-- **Factory** — before code generation
-- **Central Terminal** — before planning/orchestration
-- **Right Terminal** — before audit/summary tasks
-
-### 11.2 One Recording, Universal Application
-Recording this principle in root-level `FACTORY_OPERATING_SYSTEM.md` binds all contours. Local copies are references, not substitutes.
-
-### 11.3 Alignment Requirement
-All instruction-bearing documents must align:
-- canon files
-- README / REDMI
-- runbooks
-- workflow specs
-- prompt templates
-- recovery procedures
-
-**Contradictory wording must be rewritten** to match this principle.
-
----
-
-## 12. EXCEPTIONS (SANCTIONED ONLY)
-
-| Exception | Justification | Approval |
-|-----------|---------------|----------|
-| Emergency direct edit | System down, no Factory path | Operator real-time sanction |
-| Documentation-only change | No code impact, markdown only | Documented in commit |
-| Factory bypass for experiment | Explicit research mode | Operator pre-approval |
-| Integration preparation | Operator-directed merge prep | Operator directive (this document) |
-
-**Default:** No exceptions. Factory-only coding is absolute.
-
----
-
-## 13. AMENDMENT RULES
-
-- **Operator approval** — all amendments
-- **CTIO approval** — structural changes (roles, tiers, consult chain)
-- **Emergency amendments** — 72-hour expiry, must ratify or revert
-
----
-
-## APPENDIX: AUDITED SOURCES STATUS
-
-| Source | Factory-Only | Cheap-First | Non-Atomic | Audit-First | Shell Audit | Consult Chain | Status |
-|--------|--------------|-------------|------------|-------------|-------------|---------------|--------|
-| `FACTORY_OPERATING_SYSTEM.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **THIS DOCUMENT** |
-| `CLAUDE_CODE_OPERATING_PRINCIPLE.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Aligned v1.1 |
-| `AGENTS.md` (root) | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Updated v1.1 |
-| `docs/canon/software-factory-canon-v1.md` | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | References this doc |
-| `.claude/CLAUDE_CODE_CANON.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Rule 9 overridden |
-
----
-
-*Enacted: 2026-08-26*  
-*Version: 1.1 (normalized)*  
-*Authority: Operator directive — root-level universal, all contours*  
-*Supersedes: All factory/canon instructions where conflict exists*
+Содержание FOS v1.1 (коммит `4096533`, 2026-08-26 00:19) перенесено туда без потери смысла;
+лог сведения — `docs/governance/SSOT-UNIFICATION-LOG-2026-08-26.md`. Копия правила в этом
+репозитории — дефект (ADR-102). Read-before-work обязанность FOS §11.1 действует для SSOT.
diff --git a/.claude/CLAUDE_CODE_CANON.md b/.claude/CLAUDE_CODE_CANON.md
index 2295863..43cbce1 100644
--- a/.claude/CLAUDE_CODE_CANON.md
+++ b/.claude/CLAUDE_CODE_CANON.md
@@ -65,6 +65,9 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
 6. **One best step out.** Per Rules 1, 8 — CENTRAL emits a single best next action (a prompt to the
    factory or an `OPERATOR_RUN`), never a menu. [ФАКТ]
 
+
+6. **Operator Control Rule (ABSOLUTE):** The consultation brief is prepared as a textual artifact for the operator ONLY. **NEVER** autonomously send the brief to any consultant. Consultant engagement requires explicit operator directive.
+
 ### T4. Rules for BEN (binding, additive)
 - [ФАКТ] Read-only during scouting (Rule 2). [ВЫВОД] Never executes; hands CENTRAL a single best step +
   tagged findings. [ВЫВОД] Stays a logical mode inside the current repo/terminal context (INV-08).
diff --git a/AGENTS.md b/AGENTS.md
index 74fd3f2..dccc871 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -15,7 +15,7 @@ All agent execution follows `FACTORY_OPERATING_SYSTEM.md`:
 - **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive for **concise final verification only**.
 - **NON-ATOMIC:** Continuous execution across non-branching work.
 - **AUDIT-FIRST:** Fresh shell audit before each material step.
-- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks.
+- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks. **Operator controls delivery — brief prepared as text artifact, NEVER autonomously sent.**
 - **CLOUD-FIRST FCC:** Non-protected data → cloud via FCC; protected data → local Ollama.
 
 Main Claude resource verifies outputs/findings/summaries from cheap contour, not re-processes bulk work from scratch.
diff --git a/CLAUDE_CODE_OPERATING_PRINCIPLE.md b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
index f0512a8..e9485ab 100644
--- a/CLAUDE_CODE_OPERATING_PRINCIPLE.md
+++ b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
@@ -127,6 +127,19 @@ Each fork packet must include:
 
 Independent non-blocked work must continue while the blocked branch is isolated.
 
+### 7.5 Operator Control Rule (ABSOLUTE)
+
+**The consultation packet is prepared as a textual artifact for the operator ONLY.**
+
+- Claude Code prepares the complete fork brief in text form
+- The brief is delivered to the operator as a deliverable
+- **NEVER** autonomously send the brief to any consultant
+- **NEVER** launch consult chain without explicit operator directive
+- Consultant engagement occurs only when operator explicitly directs
+
+This rule is absolute: delivery to consultants requires operator sanction.
+
+
 ---
 
 ## 8. CANON OVERRIDE RULE
diff --git a/FACTORY_OPERATING_SYSTEM.md b/FACTORY_OPERATING_SYSTEM.md
index 7538872..c8af36c 100644
--- a/FACTORY_OPERATING_SYSTEM.md
+++ b/FACTORY_OPERATING_SYSTEM.md
@@ -181,6 +181,19 @@ CONSULT PROMPTS:
   - Kimi: <specific question>
 ```
 
+
+### 5.2.5 Operator Control Rule (ABSOLUTE)
+
+**The brief is prepared as a textual artifact for the operator ONLY.**
+
+- Claude Code prepares the complete fork brief in text form
+- The brief is delivered to the operator as a deliverable
+- **NEVER** autonomously send the brief to any consultant
+- **NEVER** launch consult chain without explicit operator directive
+- Consultant engagement occurs only when operator explicitly directs
+
+This rule is absolute: delivery to consultants requires operator sanction.
+
 ### 5.3 Strict Consultant Order
 1. **Codex** — primary consultant (independent analysis)
 2. **Fable** — second opinion (challenges assumptions)
<!-- CANON-READ-FIRST v1 -->
> ⚠️ ПЕРЕД ЛЮБЫМ ДЕЙСТВИЕМ: вычитай канон.
> 1) Прочитай SSOT: docs/canon/CANON-FACTORY-SSOT.md
> 2) Работай ТОЛЬКО через Фабрику (Claude Code). Прямой shell — лишь для аудита (read-only).
> 3) После вывода — РОВНО ОДИН артефакт (SHELL или CLAUDE CODE), по принципу «лучшего решения», без параллельных действий — в ИСПОЛНИТЕЛЬНОЙ фазе; проектная фаза допускает параллельный анализ (CORE-10-15).
<!-- /CANON-READ-FIRST v1 -->

# CANON-FACTORY-SSOT — операционный канон терминального workflow

- **Статус:** SSOT — **единственный источник истины** по взаимодействию оператора,
  центрального терминала и Фабрики.
- **Тип:** addendum. Существующие ADR не переписываются; конституционные amendments не правятся.
- **Версия:** v5 (2026-08-10). v1 называла Фабрику «центральным терминалом»; v2 привела
  роли в соответствие с топологией (Terminal A = LEFT = Фабрика; Central = диспетчер;
  оператор — источник приоритета) и зафиксировала ядро из 10 норм; v3 добавляет норму 11
  (разделение исполнительного окна Фабрики и консультационного окна Fable-5) и три метки
  назначения в норме 7; v4 — нормы 12–13 (изоляция индекса и явный набор коммита;
  персональная ответственность Orchestration Owner / Isolation Watcher, fail-closed и
  обязательная эскалация оператору) по итогам инцидента cross-session index leak.
  **v5 (2026-08-10)** — норма 14 (владение веткой и чистота рабочей области):
  branch-level cross-session leak по итогам инцидента MR !13, где чужие коммиты попали
  в разделяемую ветку мимо staged-guard'а.
  **v6 (2026-08-10)** — норма 15 (design-режим): фазовое разделение «параллельность
  мышления разрешена, параллельность ЗАПИСИ запрещена». Нормы 3, 5, 6, 8 и баннер
  READ-FIRST получили область действия по фазе; их ядро не изменено.
- **Отношение к другим файлам:** все прочие канон-документы **обязаны ссылаться** сюда и не
  воспроизводить правило. Копия правила в другом файле — дефект, подлежащий замене ссылкой.
  Известные остаточные пересказы — `TERMINAL-B-OPERATING-CANON.md`, `FACTORY-CANON.md`,
  `REPORTING-STYLE-CANON.md`, `agents/_template/SOUL.md` — вынесены в follow-up-такт и
  подлежат Duplication Audit (ADR-102). До его завершения формулировка описывает
  требование, а не достигнутое состояние.
- **Проверка:** `bash scripts/canon-ssot-check.sh` — воспроизводимо подтверждает наличие
  всех 16 норм ядра и то, что root-инструкции ссылаются на этот файл, а не дублируют его.
  Изоляцию набора коммита проверяет `bash scripts/commit-set-guard.sh <ожидаемые пути>`;
  владение веткой — `bash scripts/branch-ownership-guard.sh <base> [ожидаемые коммиты…]`.

## 1. Ядро канона — 16 норм (immutable)

<!-- CORE-10-01 -->
**1. Оператор — единственный источник приоритета задач.**
Никакой агент и никакой документ не переопределяет порядок приоритетов, заданный
оператором. Центральный терминал — отдельная роль-диспетчер (см. норму 3 и §4);
оператор с ним не отождествляется.

<!-- CORE-10-02 -->
**2. Фабрика — левый терминал / Claude Code — единственный исполнитель изменений**
кода, документов, конфигураций и git-операций. Всё, что меняет состояние репозитория
или инфраструктуры, исполняет только Фабрика.

<!-- CORE-10-03 -->
**3. Центральный терминал не исполняет работу напрямую:** он формирует для Фабрики
ровно один следующий артефакт — **в исполнительной фазе**. В проектной фазе допустимы
параллельные аналитические артефакты (норма 15); прямого исполнения центральный терминал
не ведёт ни в одной фазе.

<!-- CORE-10-04 -->
**4. Shell разрешён только для прямого read-only аудита/диагностики.** Никаких изменений,
staging, commit, push, merge, rebase, reset, удаления или генерации файлов через
shell-артефакты центрального терминала.

<!-- CORE-10-05 -->
**5. После каждого вывода аудита центральный терминал без вопросов формирует ровно ОДИН
следующий артефакт:** либо один промпт для Claude Code, либо одну read-only
shell-команду/скрипт для нового аудита. Требование единственности относится к
**исполнительной фазе**; в проектной фазе действует норма 15.

<!-- CORE-10-06 -->
**6. Запрещены параллельные ИСПОЛНИТЕЛЬНЫЕ (write) артефакты,** альтернативные планы
исполнения, несколько блоков команд, «следующие шаги» и предложения дополнительных
действий после выдачи исполнительного артефакта. Параллельные **аналитические**
артефакты проектной фазы этим запретом не охватываются и разрешены нормой 15.

<!-- CORE-10-07 -->
**7. Каждый артефакт обязан явно содержать метку назначения** — ровно одну из трёх:
- `Куда вставлять: SHELL` — только read-only аудит/диагностика;
- `Куда вставлять: CLAUDE CODE (Фабрика)` — исполнительное окно Claude Code
  (младшая модель): изменения кода, документов, конфигураций, git-операции;
- `Куда вставлять: CLAUDE CODE (Fable-5 консультация)` — отдельное консультационное
  окно Claude Code (старшая модель Fable-5): ТОЛЬКО консультации и развилки по
  процедуре DEPTH PARITY, advisory/read-only, без изменений.

Смешивать назначения в одном блоке запрещено. Исполнительные артефакты не отправляются
в консультационное окно; консультации не отправляются в исполнительное окно.

<!-- CORE-10-08 -->
**8. Решение выбирается по принципу «лучшего решения»** только по фактическому свежему
аудиту, а не по памяти. Аудит и действие — разные ответы: сначала один SHELL-аудит,
следующим ответом — артефакт действия, построенный на выводе аудита. Это разграничение
описывает **переход в исполнительную фазу** и не запрещает параллельную проектную
аналитику (норма 15).

<!-- CORE-10-09 -->
**9. Фабрика работает в sandbox-режиме,** сама оркеструет безопасную последовательность
операций и обязана проводить code-quality/self-review до сдачи результата.

<!-- CORE-10-10 -->
**10. При конфликте этот короткий операционный канон имеет приоритет для терминального
workflow;** доменные, security, ledger и compliance-каноны сохраняют свою область действия.

<!-- CORE-10-11 -->
**11. Разделение окон и моделей.** Окно Fable-5 — старшая модель, ТОЛЬКО
консультации и процедура DEPTH PARITY (advisory, read-only, без изменений). Окно
Фабрики — исполнитель, младшая модель, только исполнение. Развилки и вопросы
обязательно идут в консультационное окно Fable-5; исполнение — только в окно Фабрики.
Ни одно окно не подменяет другое.

<!-- CORE-10-12 -->
**12. Изоляция индекса и явный набор коммита.** Каждый исполнительный такт работает
через изолированный git-индекс (`GIT_INDEX_FILE` на временный файл + `git read-tree HEAD`)
и коммитит строго собственный, заранее объявленный набор путей (pathspec-коммит).
Общий индекс между параллельными сессиями для staging не используется; commit без
явно объявленного набора запрещён.

<!-- CORE-10-13 -->
**13. Ответственность за оркестрацию сессий (fail-closed).** Каждый исполнительный
такт Фабрики имеет назначенного ответственного агента-сотрудника — **Orchestration
Owner** — и контролирующего агента — **Isolation Watcher**. Orchestration Owner обязан
изолировать индекс и коммитить строго собственный явный набор (норма 12); Isolation
Watcher обязан независимо проверить, что в набор не попали изменения других сессий.
Проникновение любого чужого/постороннего изменения в сессию или коммит **категорически
запрещено — независимо от его содержания и «безвредности»**. При обнаружении любого
cross-session leak или расхождения набор считается загрязнённым: работа немедленно
останавливается (**fail-closed**), такт НЕ продолжается. Инцидент немедленно и явно
**эскалируется оператору** с точным diff набора, идентификацией лишних файлов и
вероятным источником; продолжение работы возможно ТОЛЬКО после явной корректировки или
решения оператора. Ни один агент не имеет права «молча поглотить» чужие правки или
трактовать их как согласованные без решения оператора.

<!-- CORE-10-14 -->
**14. Владение веткой и чистота рабочей области (branch-level).** Нормы 12–13 покрывают
staged-набор; этот уровень — ветка и рабочая область. Перед началом исполнительного
такта Orchestration Owner обязан установить **базис ветки** (ожидаемый head/предок,
как правило — актуальный `origin/main`) и подтвердить, что рабочая ветка не содержит
коммитов других сессий сверх этого базиса. **Ветка исполнительного такта принадлежит
одной сессии**; чужие коммиты в ней — загрязнение уровня ветки (**branch-level
cross-session leak**), не только индекса. Непосредственно перед push Owner повторно
сверяет, что head ветки не сдвинут посторонним: ожидаемое состояние = зафиксированный
базис + строго собственные коммиты (`scripts/branch-ownership-guard.sh`). При
обнаружении чужих коммитов в рабочей ветке: **STOP (fail-closed)** — НЕ мержить,
НЕ rebase-ить и НЕ поглощать чужое; эскалация оператору с перечнем чужих коммитов и
их вероятной сессией-источником. Предпочтительный режим: каждый такт создаёт **свежую
одноразовую ветку от актуального `origin/main`**, исключая разделяемое пространство.

<!-- CORE-10-15 -->
**15. Design-режим: параллельность мышления разрешена, параллельность записи — нет.**
В **проектной** фазе (read-only анализ, аудит, консультации, гипотезы, сравнение
вариантов) допускается **несколько параллельных аналитических артефактов**,
альтернативных планов и сопоставлений; каждый несёт свою метку назначения (норма 7);
**ни один аналитический артефакт не исполняется сам по себе** — он предлагает, но не
меняет состояние. В **исполнительной (write)** фазе действует прежняя дисциплина:
**ровно ОДИН исполнительный артефакт за такт**, с явным основанием выбора, объявленным
набором путей и владельцем такта; исполняет только Фабрика (норма 2), с изоляцией
индекса (12), session-lock (13) и владением веткой (14). Переход в исполнительную фазу
есть **явный выбор ровно одного артефакта**: пока выбор не сделан, ни один из
параллельных вариантов исполнению не подлежит.

<!-- CORE-10-16 -->
**16. Orchestration и number-hygiene — в каждом промпте Фабрике (fail-closed).**
Каждый промпт/артефакт, направляемый Фабрике на исполнение, ОБЯЗАН содержать:
(а) **orchestration-блок** — изоляция сессии по `.claude/rules/parallel-session-isolation.md`
и нормам 12–14 (свой worktree/ветка; изолированный индекс; pathspec-коммит;
commit-set-guard + branch-ownership-guard с базой = merge-base и явной проверкой
exit-кода); (б) требование **number-hygiene** — перед присвоением любого номера
(CORE-10-NN, ADR-NNN, IL и т.п.) проверяется занятость номера в `main` И во всех
открытых ветках/worktree; коллизия ⇒ STOP + эскалация, номер не присваивается.
Артефакт БЕЗ orchestration/number-hygiene-блока считается **неполным**: Фабрика
вправе остановиться (fail-closed) и эскалировать до его добавления. Дрейф main или
чужой мусор в своей среде ⇒ STOP + эскалация, не поглощать (нормы 13–14).

**17. Порядок такта и обращение к консультантам на развилке.**
Такт всегда идёт в одном порядке, и порядок этот не сокращается: **вычитка канона →
свежий аудит → действие**. Канон читается ДО того, как складывается замысел действия, а не
после — иначе он превращается в проверку уже принятого решения. Аудит идёт ВТОРЫМ, до
артефакта: действие строится на выводе только что выполненного замера, не на памяти о нём
(нормы 1 и 5 §2 — это их последовательность, а не их замена).

**Развилка обязывает не к выбору, а к обращению.** Развилка — это точка, где обе ветви
защитимы, и выбор между ними сам является решением, которого Фабрика не принимает: смена
необратимого состояния, изменение нормы, распределение подотчётности, всё, где ошибка не
откатывается коммитом. Дойдя до такой точки, Фабрика **останавливается и готовит подробный
бриф-обращение к консультантам** — Codex как основной, Fable-5 как независимое второе
мнение — и ждёт действия оператора. Бриф не заменяется коротким вопросом и не откладывается
«до удобного момента»: невыданный бриф означает, что развилку молча прошли.

Бриф-обращение обязано содержать: (а) факты, **измеренные живьём** непосредственно перед
написанием, с указанием способа замера и полноты выборки; (б) сами ветви, каждая с её
доводом и ценой, включая ту, которую Фабрика считает неверной; (в) вопросы, отвечать на
которые имеет смысл — ровно те, ответ на которые меняет следующее действие; (г) границы,
которые ответ не вправе ослабить; (д) улики против собственной позиции, если они есть —
в частности **собственные ошибочные замеры**, потому что они говорят о надёжности метода
больше, чем удачные; (е) явное указание, что делает Фабрика, пока развилка открыта.
Два консультанта опрашиваются **параллельно и независимо**: второе мнение не видит вердикт
основного (no-anchoring), расхождения показываются несглаженными. Недоступность одного из
них не блокирует такт — обращение выходит с честной пометкой, что мнение не получено.

Решение по брифу принимает оператор (ADR-145). Фабрика тем временем продолжает всё, что от
развилки не зависит: остановка касается развилки, а не работы.

## 2. Pre-action canon check

Перед формированием или исполнением каждого нового действия проверяются тринадцать пунктов:

1. **Вычитка канона** — прочитаны CANON-READ-FIRST-баннер и CORE-нормы (§1 этого файла)
   перед формированием артефакта; артефакт не формируется по памяти о каноне.
2. **Роль терминала** — кто действует: оператор (приоритет), центральный терминал
   (формирует артефакт), Фабрика (исполняет)? Действие соответствует роли (нормы 1–3)?
3. **Тип артефакта** — state-change → один промпт CLAUDE CODE; read-only → одна
   shell-команда аудита. Метка `Куда вставлять:` присутствует (нормы 4, 7)?
4. **Окно назначения** — выбрана правильная метка из трёх: SHELL /
   CLAUDE CODE (Фабрика) / CLAUDE CODE (Fable-5 консультация); развилка или вопрос →
   окно Fable-5, исполнение → окно Фабрики (нормы 7, 11)?
5. **Свежесть аудита** — артефакт действия строится на выводе только что выполненного
   аудита, не на памяти (норма 8)?
6. **Sandbox** — режим песочницы действует; необратимые операции и внешние публикации
   остаются за stop-барьерами (норма 9; `SANDBOX OVERRIDES`, ADR-188)?
7. **Единственность** — ровно один артефакт, без параллельных планов, альтернатив и
   «следующих шагов» (нормы 5–6) — **в исполнительной фазе**; в проектной фазе
   параллельный анализ разрешён, и вопрос читается как «сделан ли явный выбор ровно
   одного артефакта для исполнения» (норма 15)?
8. **Ответственность назначена** — для исполнительного такта назначены Orchestration
   Owner и Isolation Watcher (норма 13)?
9. **Индекс изолирован** — staging идёт через изолированный `GIT_INDEX_FILE`, набор
   коммита объявлен явно (норма 12)?
10. **Чистота набора подтверждена** — Isolation Watcher (`scripts/commit-set-guard.sh`)
    подтвердил, что в наборе только собственные файлы; при любом чужом файле — **STOP +
    эскалация оператору, без продолжения** (норма 13)?
11. **Владение веткой подтверждено** — базис зафиксирован, чужих коммитов в ветке сверх
    базиса нет (`scripts/branch-ownership-guard.sh`); предпочтительно свежая одноразовая
    ветка от `origin/main`; head не сдвинут посторонним перед push (норма 14)?

12. **Порядок соблюдён** — канон вычитан, затем выполнен свежий аудит, и только затем
    формируется действие; ни один из трёх шагов не пропущен и не переставлен (норма 17)?
13. **Развилка распознана** — если точка является развилкой (обе ветви защитимы, выбор сам
    есть решение), подготовлен ли подробный бриф-обращение к Codex и Fable-5 по составу
    (а)–(е) нормы 17, вместо того чтобы выбрать ветвь самостоятельно?

Любой ответ «нет» ⇒ действие не формируется; сначала устраняется несоответствие
(чаще всего — выполняется свежий SHELL-аудит). Ответ «нет» на п.10 или п.11 ⇒
fail-closed и эскалация оператору — такт не продолжается ни при каких условиях.


exec
/bin/bash -lc "sed -n '1,115p' ../wt/canonfork01/docs/canon/CANON-FACTORY-SSOT.md; git show 17e9a68:AGENTS.md | sed -n '1,45p'; git show 277c751:AGENTS.md | sed -n '1,45p'; git diff --unified=3 17e9a68 277c751 -- FACTORY_OPERATING_SYSTEM.md CLAUDE_CODE_OPERATING_PRINCIPLE.md .claude/CLAUDE_CODE_CANON.md | rg -n '"'^(diff|@@|[-+].*(operator|consult|Aider|Codex|Fable|Mistral|Kimi|STOP|latest|AUTO|Factory|SSOT|cloud|protected))'"'" in /home/mmber/MetaClaw
 succeeded in 25ms:
<!-- CANON-READ-FIRST v1 -->
> ⚠️ ПЕРЕД ЛЮБЫМ ДЕЙСТВИЕМ: вычитай канон.
> 1) Прочитай SSOT: docs/canon/CANON-FACTORY-SSOT.md
> 2) Работай ТОЛЬКО через Фабрику (Claude Code). Прямой shell — лишь для аудита (read-only).
> 3) После вывода — РОВНО ОДИН артефакт (SHELL или CLAUDE CODE), по принципу «лучшего решения», без параллельных действий — в ИСПОЛНИТЕЛЬНОЙ фазе; проектная фаза допускает параллельный анализ (CORE-10-15).
<!-- /CANON-READ-FIRST v1 -->

# CANON-FACTORY-SSOT — операционный канон терминального workflow

- **Статус:** SSOT — **единственный источник истины** по взаимодействию оператора,
  центрального терминала и Фабрики.
- **Тип:** addendum. Существующие ADR не переписываются; конституционные amendments не правятся.
- **Версия:** v5 (2026-08-10). v1 называла Фабрику «центральным терминалом»; v2 привела
  роли в соответствие с топологией (Terminal A = LEFT = Фабрика; Central = диспетчер;
  оператор — источник приоритета) и зафиксировала ядро из 10 норм; v3 добавляет норму 11
  (разделение исполнительного окна Фабрики и консультационного окна Fable-5) и три метки
  назначения в норме 7; v4 — нормы 12–13 (изоляция индекса и явный набор коммита;
  персональная ответственность Orchestration Owner / Isolation Watcher, fail-closed и
  обязательная эскалация оператору) по итогам инцидента cross-session index leak.
  **v5 (2026-08-10)** — норма 14 (владение веткой и чистота рабочей области):
  branch-level cross-session leak по итогам инцидента MR !13, где чужие коммиты попали
  в разделяемую ветку мимо staged-guard'а.
  **v6 (2026-08-10)** — норма 15 (design-режим): фазовое разделение «параллельность
  мышления разрешена, параллельность ЗАПИСИ запрещена». Нормы 3, 5, 6, 8 и баннер
  READ-FIRST получили область действия по фазе; их ядро не изменено.
- **Отношение к другим файлам:** все прочие канон-документы **обязаны ссылаться** сюда и не
  воспроизводить правило. Копия правила в другом файле — дефект, подлежащий замене ссылкой.
  Известные остаточные пересказы — `TERMINAL-B-OPERATING-CANON.md`, `FACTORY-CANON.md`,
  `REPORTING-STYLE-CANON.md`, `agents/_template/SOUL.md` — вынесены в follow-up-такт и
  подлежат Duplication Audit (ADR-102). До его завершения формулировка описывает
  требование, а не достигнутое состояние.
- **Проверка:** `bash scripts/canon-ssot-check.sh` — воспроизводимо подтверждает наличие
  всех 16 норм ядра и то, что root-инструкции ссылаются на этот файл, а не дублируют его.
  Изоляцию набора коммита проверяет `bash scripts/commit-set-guard.sh <ожидаемые пути>`;
  владение веткой — `bash scripts/branch-ownership-guard.sh <base> [ожидаемые коммиты…]`.

## 1. Ядро канона — 16 норм (immutable)

<!-- CORE-10-01 -->
**1. Оператор — единственный источник приоритета задач.**
Никакой агент и никакой документ не переопределяет порядок приоритетов, заданный
оператором. Центральный терминал — отдельная роль-диспетчер (см. норму 3 и §4);
оператор с ним не отождествляется.

<!-- CORE-10-02 -->
**2. Фабрика — левый терминал / Claude Code — единственный исполнитель изменений**
кода, документов, конфигураций и git-операций. Всё, что меняет состояние репозитория
или инфраструктуры, исполняет только Фабрика.

<!-- CORE-10-03 -->
**3. Центральный терминал не исполняет работу напрямую:** он формирует для Фабрики
ровно один следующий артефакт — **в исполнительной фазе**. В проектной фазе допустимы
параллельные аналитические артефакты (норма 15); прямого исполнения центральный терминал
не ведёт ни в одной фазе.

<!-- CORE-10-04 -->
**4. Shell разрешён только для прямого read-only аудита/диагностики.** Никаких изменений,
staging, commit, push, merge, rebase, reset, удаления или генерации файлов через
shell-артефакты центрального терминала.

<!-- CORE-10-05 -->
**5. После каждого вывода аудита центральный терминал без вопросов формирует ровно ОДИН
следующий артефакт:** либо один промпт для Claude Code, либо одну read-only
shell-команду/скрипт для нового аудита. Требование единственности относится к
**исполнительной фазе**; в проектной фазе действует норма 15.

<!-- CORE-10-06 -->
**6. Запрещены параллельные ИСПОЛНИТЕЛЬНЫЕ (write) артефакты,** альтернативные планы
исполнения, несколько блоков команд, «следующие шаги» и предложения дополнительных
действий после выдачи исполнительного артефакта. Параллельные **аналитические**
артефакты проектной фазы этим запретом не охватываются и разрешены нормой 15.

<!-- CORE-10-07 -->
**7. Каждый артефакт обязан явно содержать метку назначения** — ровно одну из трёх:
- `Куда вставлять: SHELL` — только read-only аудит/диагностика;
- `Куда вставлять: CLAUDE CODE (Фабрика)` — исполнительное окно Claude Code
  (младшая модель): изменения кода, документов, конфигураций, git-операции;
- `Куда вставлять: CLAUDE CODE (Fable-5 консультация)` — отдельное консультационное
  окно Claude Code (старшая модель Fable-5): ТОЛЬКО консультации и развилки по
  процедуре DEPTH PARITY, advisory/read-only, без изменений.

Смешивать назначения в одном блоке запрещено. Исполнительные артефакты не отправляются
в консультационное окно; консультации не отправляются в исполнительное окно.

<!-- CORE-10-08 -->
**8. Решение выбирается по принципу «лучшего решения»** только по фактическому свежему
аудиту, а не по памяти. Аудит и действие — разные ответы: сначала один SHELL-аудит,
следующим ответом — артефакт действия, построенный на выводе аудита. Это разграничение
описывает **переход в исполнительную фазу** и не запрещает параллельную проектную
аналитику (норма 15).

<!-- CORE-10-09 -->
**9. Фабрика работает в sandbox-режиме,** сама оркеструет безопасную последовательность
операций и обязана проводить code-quality/self-review до сдачи результата.

<!-- CORE-10-10 -->
**10. При конфликте этот короткий операционный канон имеет приоритет для терминального
workflow;** доменные, security, ledger и compliance-каноны сохраняют свою область действия.

<!-- CORE-10-11 -->
**11. Разделение окон и моделей.** Окно Fable-5 — старшая модель, ТОЛЬКО
консультации и процедура DEPTH PARITY (advisory, read-only, без изменений). Окно
Фабрики — исполнитель, младшая модель, только исполнение. Развилки и вопросы
обязательно идут в консультационное окно Fable-5; исполнение — только в окно Фабрики.
Ни одно окно не подменяет другое.

<!-- CORE-10-12 -->
**12. Изоляция индекса и явный набор коммита.** Каждый исполнительный такт работает
через изолированный git-индекс (`GIT_INDEX_FILE` на временный файл + `git read-tree HEAD`)
и коммитит строго собственный, заранее объявленный набор путей (pathspec-коммит).
Общий индекс между параллельными сессиями для staging не используется; commit без
явно объявленного набора запрещён.

<!-- CORE-10-13 -->
**13. Ответственность за оркестрацию сессий (fail-closed).** Каждый исполнительный
# AGENTS.md — MetaClaw

**Repository:** `~/MetaClaw`  
**Version:** 1.1 | 2026-08-26 (normalized)  
**Purpose:** Agent execution architecture for MetaClaw meta-learning framework  
**Architecture:** Factory-Only / Three-Terminal (LEFT / CENTRAL / RIGHT)

---

## ⚠️ FACTORY OPERATING SYSTEM (Root-Level Universal)

All agent execution follows `FACTORY_OPERATING_SYSTEM.md`:
- **FACTORY-ONLY CODING:** No terminal codes directly; Factory (Aider/Codex) executes all production code.
- **ALL FACTORY STAFF ENABLED:** All available Factory agents and workers must execute their roles unless restricted by task canon.
- **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive for **concise final verification only**.
- **NON-ATOMIC:** Continuous execution across non-branching work.
- **AUDIT-FIRST:** Fresh shell audit before each material step.
- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks.
- **CLOUD-FIRST FCC:** Non-protected data → cloud via FCC; protected data → local Ollama.

Main Claude resource verifies outputs/findings/summaries from cheap contour, not re-processes bulk work from scratch.

---

## Core mission

This repository is the **MetaClaw meta-learning framework** — agents learn and evolve from conversations without GPU.

### Three-Terminal Architecture

| Terminal | Canonical Name | Role | Execution |
|----------|----------------|------|-----------|
| **Central** | CENTRAL (Brain) | Architect, planner, reviewer, orchestrator | NO direct code execution |
| **Left** | LEFT (Factory Interface) | Task assignment, agent orchestration, evidence routing | NO direct code generation |
| **Right** | RIGHT (Assistant) | Research, audit, summary, brief preparation | NO code execution |
| **Factory** | Aider + Codex + agents | Code generation, edits, tests, commands | SOLE execution layer |

**Key principle:** Terminals decide and plan; Factory executes. No terminal bypasses Factory.

---

## Instruction hierarchy

1. **Explicit user instruction** (highest authority)
2. **Root-level canons**:
# AGENTS.md — Developer Core: Central Repository for Shared Components

**Repository:** `~/developer/`  
**Version:** 3.0 | 2026-04-03  
**Purpose:** Shared components, templates, and configurations distributed across all projects  
**Architecture:** Three-Partner Synergy (Claude Code + Qoder CLI + MiroFish)

---

## ⚠️ FACTORY OPERATING SYSTEM (Root-Level Universal)

All agent execution follows `FACTORY_OPERATING_SYSTEM.md`:
- **FACTORY-ONLY CODING:** No terminal codes directly; Factory (Aider/Codex) executes all production code.
- **ALL FACTORY STAFF ENABLED:** All available Factory agents and workers must execute their roles unless restricted by task canon.
- **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive model for **concise final verification only**.
- **NON-ATOMIC:** Continuous execution across non-branching work.
- **AUDIT-FIRST:** Shell audit precedes every material step.
- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks.

Main Claude resource verifies outputs/findings/summaries from cheap contour, not re-processes bulk work from scratch.

This principle propagates to all synced target projects.

---

## Core mission

This repository is the **central source of truth** for:

- Agent instructions (AGENTS.md, CLAUDE.md templates)
- Qoder CLI configurations (.qoder/config.yml)
- **Three-partner synergy architecture** (Claude + Qoder + MiroFish)
- Compliance architecture (COMPLIANCE_ARCH.md)
- Shared scripts and automation (sync-all.sh, onboard-project.sh)
- Project templates
- MCP best practices
- **MiroFish scenario templates** (MASTER copies for all projects)

### Three-Partner Architecture

All projects use the same three-partner stack:

| Partner | Role | Activation | Scope |
|---------|------|------------|-------|
| **Claude Code** | Architect & Coordinator | Every session | Design, review, orchestration |
1:diff --git a/.claude/CLAUDE_CODE_CANON.md b/.claude/CLAUDE_CODE_CANON.md
5:@@ -1,5 +1,9 @@
10:+**CRITICAL:** Claude Code NEVER writes production code directly. All code generation goes through Factory (Aider/Codex). See `FACTORY_OPERATING_SYSTEM.md` §1.
15:@@ -61,7 +65,7 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
19:-5. **Cloud-first FCC routing.** Claude Code routes through local FCC gateway to approved allowlisted cloud models for non-protected data; LiteLLM/local inference remains fallback for protected workloads and offline operation. [ФАКТ]
20:+5. **Cloud-first development is permitted through FCC.** Claude Code routes through a local FCC gateway to approved allowlisted cloud models; LiteLLM/local inference remains the fallback. Sensitive banking data must remain local.
24:@@ -74,3 +78,24 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
34:+1. **Primary development route:** Claude Code-compatible requests may be routed through a local Free Claude Code (FCC) gateway to an explicit allowlist of cloud providers/models.
36:+3. **Local continuity:** LiteLLM and local Ollama remain approved fallback routes for offline operation, continuity, and protected workloads.
38:+5. **Permitted cloud work:** Synthetic fixtures, non-sensitive architecture/design, ADRs, code scaffolding, tests, migrations, documentation, and sanitized debugging.
49:diff --git a/CLAUDE_CODE_OPERATING_PRINCIPLE.md b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
53:@@ -288,16 +288,14 @@ This §13 **overrides** any local instruction implying:
57:-| `FACTORY_OPERATING_SYSTEM.md` | Factory operating system — all contours | ✅ REFERENCES THIS DOC |
73:diff --git a/FACTORY_OPERATING_SYSTEM.md b/FACTORY_OPERATING_SYSTEM.md
77:@@ -1,4 +1,4 @@
83:@@ -35,8 +35,8 @@ Every task must utilize all available Factory agents and workers in their respec
87:-- **Aider** (via MCP/Qoder) — **primary executor**
88:-- **Codex** (plugin/CLI) — **secondary executor** when enabled
89:+- **Aider** (via MCP/Qoder) — primary executor
90:+- **Codex** (plugin/CLI) — secondary executor when enabled
94:@@ -191,74 +191,9 @@ CONSULT PROMPTS:
102:-Claude Code-compatible requests are routed through **Free Claude Code (FCC)** gateway to explicit allowlist of cloud providers/models.
107:-| **Non-protected** | Cloud-first FCC | Synthetic fixtures, architecture/design, ADRs, scaffolding, tests, docs, sanitized debugging |
109:-| **Mixed** | Decomposed — cloud for logic, local for data | Feature with both scaffolding and PII |
114:-- LiteLLM and local Ollama remain approved fallback for offline/protected workloads
125:-| **Sandbox** | Advisory — single opinion | Codex primary + Fable second | Codex + Fable parallel + operator |
126:-| **Preprod** | Codex single | Codex + Fable | Full chain + operator sanction |
127:-| **Prod** | Codex single | Full consult chain | Full chain + MLRO/CTIO + operator |
133:-## 8. AUTO-COMMIT SCOPE (Factory Contour Only)
136:-In controlled environment (sandbox/governed factory contour), valuable untracked files **must not** automatically hang in "wait for operator" state.
141:-| Safe valuable untracked (docs, canons, policies, sources) | **AUTO-COMMIT** after triage |
148:-**Central terminal does NOT auto-commit.** Central plans/reviews; Factory (Left) executes commits. Auto-commit applies **only** to Factory contour operations.
156:-| Left | **LEFT / Factory Interface** | Task assignment, agent orchestration |
171:@@ -271,7 +206,7 @@ Any instruction implying:
180:@@ -282,19 +217,19 @@ These remain valid stops:
204:@@ -307,20 +242,19 @@ All instruction-bearing documents must align:
227:@@ -333,14 +267,59 @@ All instruction-bearing documents must align:
243:+## 10. SANDBOX AUTO-COMMIT PRINCIPLE (Controlled Environment)
252:+In controlled environment, valuable untracked files **must not** automatically hang in "wait for operator sanction" state.
257:+- For valuable safe untracked files — execute **governed automatic commit** without waiting for separate operator sanction.
262:+| Safe valuable untracked (docs, canons, policies, sources) | **AUTO-COMMIT** after triage |
276:+then auto-commit **does not apply** — these paths go to risk bucket for operator review.

exec
/bin/bash -lc "git grep -n -i 'latest.operator\\|latest.*wins\\|operator.*latest' 17e9a68 -- . || true; git grep -n -i 'autonom\\|operator conducts\\|operator dispatch\\|brief.*operator' 5694a92 -- FACTORY_OPERATING_SYSTEM.md CLAUDE_CODE_OPERATING_PRINCIPLE.md AGENTS.md .claude/CLAUDE_CODE_CANON.md || true; git show --format= --no-ext-diff 11e43f9 | sed -n '1,220p'" in /home/mmber/MetaClaw
 succeeded in 327ms:
diff --git a/.claude/CLAUDE_CODE_CANON.md b/.claude/CLAUDE_CODE_CANON.md
index 2295863..43cbce1 100644
--- a/.claude/CLAUDE_CODE_CANON.md
+++ b/.claude/CLAUDE_CODE_CANON.md
@@ -65,6 +65,9 @@ Every Claude Code sprint prompt MUST include this block verbatim at the top.
 6. **One best step out.** Per Rules 1, 8 — CENTRAL emits a single best next action (a prompt to the
    factory or an `OPERATOR_RUN`), never a menu. [ФАКТ]
 
+
+6. **Operator Control Rule (ABSOLUTE):** The consultation brief is prepared as a textual artifact for the operator ONLY. **NEVER** autonomously send the brief to any consultant. Consultant engagement requires explicit operator directive.
+
 ### T4. Rules for BEN (binding, additive)
 - [ФАКТ] Read-only during scouting (Rule 2). [ВЫВОД] Never executes; hands CENTRAL a single best step +
   tagged findings. [ВЫВОД] Stays a logical mode inside the current repo/terminal context (INV-08).
diff --git a/AGENTS.md b/AGENTS.md
index 74fd3f2..dccc871 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -15,7 +15,7 @@ All agent execution follows `FACTORY_OPERATING_SYSTEM.md`:
 - **TIERED MODEL ECONOMY:** Cheap/free/lower-tier for bulk; expensive for **concise final verification only**.
 - **NON-ATOMIC:** Continuous execution across non-branching work.
 - **AUDIT-FIRST:** Fresh shell audit before each material step.
-- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks.
+- **CONSULT CHAIN:** Codex → Fable → Mistral → Kimi on forks. **Operator controls delivery — brief prepared as text artifact, NEVER autonomously sent.**
 - **CLOUD-FIRST FCC:** Non-protected data → cloud via FCC; protected data → local Ollama.
 
 Main Claude resource verifies outputs/findings/summaries from cheap contour, not re-processes bulk work from scratch.
diff --git a/CLAUDE_CODE_OPERATING_PRINCIPLE.md b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
index f0512a8..e9485ab 100644
--- a/CLAUDE_CODE_OPERATING_PRINCIPLE.md
+++ b/CLAUDE_CODE_OPERATING_PRINCIPLE.md
@@ -127,6 +127,19 @@ Each fork packet must include:
 
 Independent non-blocked work must continue while the blocked branch is isolated.
 
+### 7.5 Operator Control Rule (ABSOLUTE)
+
+**The consultation packet is prepared as a textual artifact for the operator ONLY.**
+
+- Claude Code prepares the complete fork brief in text form
+- The brief is delivered to the operator as a deliverable
+- **NEVER** autonomously send the brief to any consultant
+- **NEVER** launch consult chain without explicit operator directive
+- Consultant engagement occurs only when operator explicitly directs
+
+This rule is absolute: delivery to consultants requires operator sanction.
+
+
 ---
 
 ## 8. CANON OVERRIDE RULE
diff --git a/FACTORY_OPERATING_SYSTEM.md b/FACTORY_OPERATING_SYSTEM.md
index 7538872..c8af36c 100644
--- a/FACTORY_OPERATING_SYSTEM.md
+++ b/FACTORY_OPERATING_SYSTEM.md
@@ -181,6 +181,19 @@ CONSULT PROMPTS:
   - Kimi: <specific question>
 ```
 
+
+### 5.2.5 Operator Control Rule (ABSOLUTE)
+
+**The brief is prepared as a textual artifact for the operator ONLY.**
+
+- Claude Code prepares the complete fork brief in text form
+- The brief is delivered to the operator as a deliverable
+- **NEVER** autonomously send the brief to any consultant
+- **NEVER** launch consult chain without explicit operator directive
+- Consultant engagement occurs only when operator explicitly directs
+
+This rule is absolute: delivery to consultants requires operator sanction.
+
 ### 5.3 Strict Consultant Order
 1. **Codex** — primary consultant (independent analysis)
 2. **Fable** — second opinion (challenges assumptions)

