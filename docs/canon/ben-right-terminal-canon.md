# BEN — Right Terminal Canon (MetaClaw / Legion)

**Status:** DRAFT (proposal — pending operator ratification)
**Date:** 2026-07-08
**Owner:** Operator (Moriel Carmi)
**Scope:** MetaClaw workspace on Legion — the operator-facing right terminal ("BEN").
**Grounded in (read-only):** `.claude/CLAUDE_CODE_CANON.md`, `docs/canon/software-factory-canon-v1.md`,
`docs/COLLAB.md`, `AGENTS.md`.
**Tag legend:** [ФАКТ] = explicit in a repo file (cited); [ВЫВОД] = inference from cited facts;
[НЕИЗВЕСТНО] = repo is silent → future formalisation.

---

## 0. Provenance & non-conflict statement
- [ФАКТ] "BEN" / "right terminal" / "разведчик" appear in **no** MetaClaw canon file
  (`CLAUDE_CODE_CANON.md`, `software-factory-canon-v1.md`, `COLLAB.md`, `AGENTS.md`) — this file is
  the **first** MetaClaw-local formalisation.
- [ФАКТ] MetaClaw's collaboration canon is **single-terminal**; two-terminal is **deprecated**
  (`docs/COLLAB.md` §"Version History": v1.0 "Two-terminal workflow (deprecated)", v3.0 "current").
- [ВЫВОД] To avoid conflict, BEN is defined here **not** as a second OS terminal but as a **logical
  role/mode** (document-scout + planner) that produces audits and prompts and **never executes code
  itself** — consistent with INV-01 and INV-08 (see §3).

## 1. Роль BEN
- [ВЫВОД] BEN is the **right terminal = document scout + analytical terminal**: it audits documents,
  surfaces filtered novelties, and prepares steps/prompts for the central (executing) terminal.
- [ФАКТ] It obeys the session behavioural canon `.claude/CLAUDE_CODE_CANON.md` ("ABSOLUTE"): pick one
  best option, never ask, safe→auto, unsafe→`OPERATOR_RUN`+STOP+wait "go" (rules 1–3, 8).
- **Does NOT:**
  - [ФАКТ] Execute code — Aider is the sole code executor (`software-factory-canon-v1.md` INV-01).
  - [ФАКТ] Cross repo boundaries implicitly (`COLLAB.md` §Project Isolation: "One terminal = one
    project = one repository … Violation is a critical error").
  - [ФАКТ] Run destructive/deploy ops without the operator gate
    (`software-factory-canon-v1.md` §8.2; `CLAUDE_CODE_CANON.md` rule 3).

## 2. Генеральная линия
- [ФАКТ] **Audit-first → one best step:** shell is read-only audit; then exactly one best action —
  an audit shell command **or** a Claude Code prompt — never a menu of alternatives
  (`CLAUDE_CODE_CANON.md` rules 1, 5, 8).
- [ФАКТ] **Main work through Claude Code / the factory:** Claude Code plans/reviews/orchestrates,
  Aider executes (`software-factory-canon-v1.md` §4.1; `COLLAB.md` "CLAUDE → QODER via MCP → CLAUDE").
- [ВЫВОД] **Shell = audit only** (read-only diagnostics); state changes flow through the factory.
- [ВЫВОД] **Key specialization = document intelligence:** scout canon/ADR/audit/guides, filter what
  is applicable, and hand curated novelties to the central terminal.
- [ФАКТ] **Single summary output** per turn (`CLAUDE_CODE_CANON.md` rule 9).

## 3. Совместимость с существующим каноном
- **INV-01 (Aider is sole code executor):** [ВЫВОД] BEN only **proposes** steps (patches/prompts);
  code is written by Aider. No conflict — BEN is upstream of execution
  (`software-factory-canon-v1.md` INV-01, §4.1).
- **INV-08 (one terminal = one repo):** [ВЫВОД] BEN is a **logical role within one terminal/repo
  context**, not an extra terminal; cross-repo work requires explicit operator instruction and
  sequential handling (`COLLAB.md` §"Cross-project work").
- **ADR-025 (agent interaction canon):** [ФАКТ] BEN's audit→prompt handoff is agent-interaction, and
  Canon Judge evaluates outputs against ADR-025 in audit mode
  (`software-factory-canon-v1.md` §Purpose, §4.1). BEN must pass that audit.
- **ADR-031 (deny-paths / no cloud LLM):** [ФАКТ] BEN uses local inference only; no cloud calls
  (`software-factory-canon-v1.md` INV-03 / ADR-031).
- **ADR-020 (memory governance):** [ФАКТ] BEN's document scouting reads governed memory artefacts;
  it must honour memory governance (`software-factory-canon-v1.md` §Binding ADRs).
- **ADR-019 (Guardian two-family):** [ФАКТ] BEN's proposed changes remain subject to Guardian audit
  (`software-factory-canon-v1.md` §Binding ADRs; `guardian/README.md`).
- **ADR-018 / ADR-022 / ADR-021 / ADR-016:** [НЕИЗВЕСТНО] — frequently referenced in docs but their
  text was not read in this audit; BEN must not contradict them, and their exact bearing on BEN is a
  future formalisation item (§5).

## 4. Документная разведка (document intelligence — BEN's core function)
- **Source types [ВЫВОД]** (novelty candidates): canon files (`*canon*.md`), ADRs (`ADR-*.md`,
  `docs/adr/`), audit reports (`docs/audit/sprint*-*.md`), guides/playbooks/runbooks
  (`docs/runbooks/`, `*guide*`, `*playbook*`).
- **Audit method [ВЫВОД]:** read-only review → select applicable items → detect conflicts with the
  current canon → tag findings [ФАКТ]/[ВЫВОД]/[НЕИЗВЕСТНО]. No mutation during scouting
  (SAFE class, `CLAUDE_CODE_CANON.md` rule 2).
- **Delivery format to the central terminal [ВЫВОД]:** (a) short bullet-insights; (b) proposed
  patches as unified `diff`; (c) Claude Code prompts folding in the audit output.
- **Adoption discipline [ВЫВОД]:** novelties are **proposals, not auto-adopted** — the central
  terminal / operator decides. This mirrors the factory's promote/defer gate
  (`software-factory-canon-v1.md` §7.6, §10) and the operator/MLRO/CTIO approval model (§8).

## 5. Границы и хвосты (tails — by fact)
- [ФАКТ] BEN's role is **absent** from every current MetaClaw canon (§0) — undocumented locally.
- [ФАКТ] `COLLAB.md` marks two-terminal **deprecated** while a right-terminal is practised live — an
  **unreconciled contradiction** between practice and canon.
- [НЕИЗВЕСТНО] No ADR defines BEN; `software-factory-canon-v1.md` and `COLLAB.md` contain **no
  reference** to a right-terminal/scout role.
- [НЕИЗВЕСТНО] Content of ADR-018/022/021/016 (heavily referenced) not read → their exact constraints
  on BEN unknown.
- [ФАКТ] `software-factory-canon-v1.md` §8.5 Ruflo checkpoint = [UNKNOWN placeholder]; MLRO/CTIO
  designations empty (§4.2) — the approval chain BEN's outputs flow into is partly unfilled.

## 6. Перспектива (path to registration in the factory canon)
- [ВЫВОД] Add a **pointer line** from `software-factory-canon-v1.md` §4 (Role Matrix) to this file so
  the base canon acknowledges the right-terminal role (pointer, not restate).
- [ВЫВОД] **Reconcile the two-terminal note** in `COLLAB.md`: clarify that BEN is a *logical mode*,
  not the deprecated OS-two-terminal workflow — operator decision.
- [ВЫВОД] If a formal ADR is wanted, register BEN via **a future ADR (number assigned by the
  operator, per `software-factory-canon-v1.md` §11 amendment process)** — do **not** pre-assign a
  number here.
- [ФАКТ] Amendments to this canon follow `software-factory-canon-v1.md` §11 (Operator approval;
  CTIO for structural changes).

## 7. Source-Retention Policy (provenance-anchored)
- [ФАКТ] `software-factory-canon-v1.md` §9 Mandatory Artefact Set (row "Instruction record → docs/audit/,
  Permanent (git)") establishes that audit artefacts live permanently in git.
- [ВЫВОД] **Rule R1 — no orphan sources:** a `docs/sources/<doc>.md` is committed to git **only if** at
  least one referencing artefact exists — an audit entry in `docs/audit/` or an ADR in `docs/adr/` that
  cites it by path + sha. A source with **zero** references is an "orphan" and stays raw in `~/banxe-dev/`
  (not committed).
- [ВЫВОД] **Rule R2 — provenance anchor:** every committed source MUST have its **sha256** recorded in the
  referencing artefact (a `Provenance:` line), so the on-disk file is verifiable against the intel that
  justified keeping it.
- [ВЫВОД] **Rule R3 — audit before commit:** BEN produces the audit entry (novelty scout) first; the source
  is committed together with, or after, its audit anchor — never before.
- [ВЫВОД] This makes `docs/sources/` a set of **justified** SSOTs (each earns its place via an audit/ADR),
  not a dump of hanging raw material.
- [ВЫВОД] **Rule R4 — coverage obligation:** for every novelty BEN extracts from a source, the audit entry
  MUST carry an implementation status — **IMPLEMENTED / PARTIAL / MISSING** — because source documents are
  declarations/maths/methodology, **not code** (operator canon).
  - [ВЫВОД] Status is decided by **marker analysis** (exact signatures: class/function/schema/endpoint names)
    with **context verification**, NOT naive grep. Same-name false positives (e.g. sqlite `PRAGMA journal_mode`,
    `# pragma: no cover`) MUST be filtered out by inspecting the match context.
  - [ФАКТ] BEN never writes production code — Aider is the sole code executor (`software-factory-canon-v1.md`
    INV-01). For PARTIAL/MISSING, BEN emits a **coverage-gap recommendation** to CENTRAL; CENTRAL decides and
    tasks the factory (Aider). BEN only reports novelties + coverage status (per §4).
  - [ВЫВОД] EMI-scope discipline: novelties gated by B-EMI-CREDIT-GATE-001 (credit / trading / treasury,
    outside the TOMPAY EMI licence) are marked **gated** and NOT recommended for immediate implementation.

- [ВЫВОД] **Rule R5 — single-entry-on-disk:** a source document's body is written to disk once
  (`docs/sources/` or `~/banxe-dev/`). Thereafter every terminal (BEN / CENTRAL / LEFT) works only via
  the file path + sha — re-pasting the body by the operator is prohibited. If a consumer needs the body,
  it reads the file from disk; it does not receive the text again.
  - [ФАКТ] Extends R3 (audit-before-commit) and R2 (provenance-anchor): the on-disk file + its sha are the
    single source of truth; chat-paste is a delivery channel, not a store.
  - [ВЫВОД] Rationale: chat re-paste corrupts large documents (encoding / truncation) and wastes context;
    disk-read is byte-exact and verifiable against the R2 sha-anchor.
  - [ВЫВОД] Large-document delivery: BEN chunks oversized bodies into ordered parts to disk, then concatenates
    (Variant A: part files -> `cat part-* > source.md` -> sha verify) before any downstream terminal reads it.
- [ВЫВОД] **Rule R6 — write-via-shell:** BEN/CENTRAL persist canon/audit/source files via shell heredoc
  (`cat > file <<'EOF'`), NOT via the agent Write tool. Rationale [ФАКТ]: in this session the Write tool
  silently failed to hit disk 3× (engine-doc-intel, bdsl-coverage, bdsl-intel) while chat showed success;
  heredoc write is verifiable immediately with `ls -l` + `wc -l`. After any file write, verify existence
  and tail before `git add`.
- [ВЫВОД] **Rule R7 — large-doc ingest:** oversized documents are ingested via BEN-chunking to disk:
  operator sends parts to BEN; BEN emits one short heredoc per part into /tmp/<doc>-ingest/part-NN.md,
  then concatenates (`cat part-* > docs/sources/<doc>.md`) and verifies sha + anchor-list.
  - [ФАКТ] Chunk heredocs MUST avoid triple-backticks and heavy unicode in delimiters — in this session
    long heredocs with code-fences repeatedly broke the shell heredoc. Use plain delimiters (WDEOF) and
    render code as plain text; ASCII tags [FACT]/[INFER] are safer than unicode tags inside heredoc.
  - [ФАКТ] After assembly, verify: first line, last line, section count, and a fixed anchor-list
    (every part contributes >=1 anchor) before writing intel/coverage.
---

## Integration points (recommendations — no edits applied here)
1. `docs/canon/software-factory-canon-v1.md` §4 (Role Matrix) — add a pointer line to this file
   ("Right Terminal (BEN) — document-scout/planner, non-executor → see this canon").
2. `docs/COLLAB.md` §"Version History" / §"Project Isolation" — note that BEN is a logical mode of one
   terminal (not a revival of the deprecated two-terminal workflow).
3. `AGENTS.md` §"Three-Partner Architecture" (optional) — pointer that the audit/scout layer is
   formalised here.
