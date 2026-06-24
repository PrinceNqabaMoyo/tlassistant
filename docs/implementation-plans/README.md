# Implementation Plans

Living planning docs for in-progress and upcoming work. These are design/spec
documents, not code — safe to read before/while implementing.

## Cross-cutting
- `01_procedure_tracker_agent.md` — Procedure / working tracker (Plan 1). One
  orchestrator agent + `diagnose_procedure` tool; deterministic SymPy step
  equivalence; NSC-style method + accuracy marks with carry-over.
- `02_landing_page_and_positioning.md` — Landing page revamp + CAPS/NSC
  positioning (body-accurate wording for DBE / IEB / SACAI), pricing
  (R150 Standard / R299 Pro), teacher/tutor collab as "coming soon".

## Mathematics — `mathematics/`
- `00_mathematics_gr10_overview.md` — Gr10 maths approach: deterministic SymPy
  generators, KaTeX + comma decimals, Diagram Spec → JSXGraph, Working Pad,
  registry-driven keypad.

### Grade 10, Term 1 (5 topics)
| Topic | Plan | Status |
|-------|------|--------|
| 1. Algebraic Expressions | (shipped in PR #6) | ✅ done |
| 2. Exponents | `mathematics/gr10_t1_04_exponents.md` | planned |
| 3. Patterns & Sequences | `mathematics/gr10_t1_05_patterns_sequences.md` | planned |
| 4. Equations & Inequalities | `mathematics/gr10_t1_06_equations_inequalities.md` | planned |
| 5. Trigonometry | (shipped in PR #6) | ✅ done |

**Recommended build order for the 3 outstanding topics:**
Exponents → Equations & Inequalities → Patterns & Sequences
(rationale in `gr10_t1_06_equations_inequalities.md`).
