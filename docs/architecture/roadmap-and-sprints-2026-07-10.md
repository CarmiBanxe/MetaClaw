# Roadmap & Sprints — Legion Generic Engine + BANXE Specialization (2026-07-10)

Status: DRAFT. Canonical doc conclusions are PRELIMINARY (built on incomplete corpus).

## EPIC A — Complete the corpus (read-only, no conclusions)
- A1: Read tail of tool catalog — "recommended stack" + "warnings".
- A2: Read UX/UI document verbatim.
- A3: Read "world banking experience" document verbatim.
- Exit: all 7 primary docs read verbatim; no synthesis yet.

## EPIC B — Repair canonical integrity (edit on command only)
- B1: Regenerate Section 2 "Source Inventory" (real filenames + real sha256).
      Root cause of breakage: backticks and %s in the command (fg: %s: no such job).
      Fix: use sha256sum over a file list + single-quoted heredoc (no substitution).
- B2: Mark canonical header as DRAFT / premature until EPIC A closes.

## EPIC C — Deep analysis (only on explicit go)
- C1: Reconcile draft conclusions (LangGraph canonical, generic-core-first,
      BANXE-as-overlay) against the FULL corpus.
- C2: Tag each claim: confirmed / needs-revision / made-on-incomplete-data.
- C3: Validate generic-core vs BANXE-specialization split, component by component
      (the "general / banking / TBD" table).

## Sprint sequencing
- Sprint 1: A1 -> A2 -> A3 (close corpus). Stage B1 inputs in parallel.
- Sprint 2: B1 + B2 (repair + relabel canonical doc).
- Sprint 3: C1 -> C2 -> C3 (analysis + best-solution recommendations).

## Definition of Done
- All 7 sources read verbatim and inventoried with valid sha256.
- Canonical doc Section 2 valid; header state accurate.
- Every canonical claim tagged and justified against full corpus.
