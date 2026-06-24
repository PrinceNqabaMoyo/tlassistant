# Implementation Plan — Gr10 Mathematics, Term 1: Patterns & Sequences

**Status:** outstanding. Topic 3 of 5.
**Pattern:** deterministic SymPy stack (no LLM). Plus a **second reuse of the Diagram Spec pipeline** — this time for *diagrammatic patterns* (dots / matchsticks / triangles), proving the spec generalises beyond right triangles.

Source doc: `caps-ai-backend/curriculum_docs/Mathematics_Gr10/Term 1/3 Patterns and Sequences .md` (940 lines).

## Embedded-comment compliance
- Subscripts written `~x~` in the doc → render as **true subscripts** `T_{n}` (KaTeX). Add `T_n`, `T_{n-1}` tokens to the keypad.
- "LLM should not copy-paste questions but use these as **archetypes** for generators that produce unlimited variety." → exactly our deterministic-generator approach (seeded params over archetypes).
- "LLM should come up with **new diagrammatic patterns**, not just those described." → the diagram generator must be **parametric** (seeded figure family), not a fixed picture. This is the key new capability.

## Subskills (generators)

| key | what it tests | answer mode | archetype |
|-----|---------------|-------------|-----------|
| `next_terms` | continue a linear sequence | `value` (csv of next 3) | `5;15;25;… → 35;45;55` |
| `common_difference` | find `d`, or "no common difference" | `value` (incl. non-linear → text token) | `5;12;19;26` → d=7 ; `9;−7;−8;…` → none |
| `general_term` | derive `T_n = dn + (a−d)` | `expression` in `n` | `2;5;8;11 → T_n = 3n − 1` |
| `term_from_n` | evaluate `T_n` at given `n` | `value` | `T_n=3n−1; T_50 = 149` |
| `n_from_term` | solve for position given value | `value` | `15;23;31;… ; T_n=191 → n=23` |
| `missing_terms` | fill gaps given the general formula | `value` (csv) | `T_n=n²−1: 0;3;_;15;24 → 8` |
| `diagram_pattern` | figure sequence → table → general formula | `diagram + table + expression` | tables-and-people, matchstick squares, triangle/dot fans |
| `letter_sequence` | cyclic/modular position | `value` (a letter) | `PATTERNPATTERN…` 649th letter; `C;D;E;… T_{n−4}` |
| `linear_param` | solve for a parameter that makes terms linear | `value`/`fraction` | `k/3−1; −5k/3+2; −2k/3+10` linear → find k |
| `word_problem` | real-world linear sequence (seating, data, savings) | `steps` + `value` | stadium rows, CellX data plan, weekly savings |
| `conjecture` (enrichment) | odd+even, ×11, +9 patterns | `expression` (algebraic proof form) | see doc; defer to challenge tier |

## Generator design
- Linear-sequence core: seed `a` (first term) and `d` (common difference) from small integer/decimal/`z`-symbol ranges; SymPy builds `T_n = a + (n-1)d`, expanded to `dn + (a-d)`.
- Non-linear distractors for `common_difference`: occasionally emit a quadratic/non-linear sequence so "no common difference" is a real answer (encode as a reserved answer token).
- `general_term` answer is an `expression` in `n` → mark by SymPy equality after substituting several `n`.
- Canonical solution graph: (1) find d, (2) `T_n = a + (n-1)d`, (3) simplify, (4) substitute/solve. Each a transition with `op`/`rule`/`common_errors`.
- Decimals & fractions both appear (doc has `7,4; 9,7; 12` and `1/3; 2/3; 1`) → comma decimals + `\frac` already supported.

## NEW: parametric diagram patterns (Diagram Spec extension)
Extend `_diagram.py` with figure families that are **seed-parametric** so we honour "come up with new diagrammatic patterns":
- `kind: "dot_pattern"` — N items in a deterministic layout (e.g. tables-with-people, L-shapes, staircases). Spec carries `figure_index` and the count rule so the renderer draws figure 1..4.
- `kind: "matchstick"` — row of `k` squares/triangles from unit segments; spec = list of segments.
- The generator emits **figures 1–4** (rendered) + asks for the table row / `T_n` / a far term (figure 25). The picture is the *stimulus*; the answer is numeric/expression (marked deterministically). 
- Renderer: add a `PatternRenderer` mode to `DiagramRenderer.jsx` (JSXGraph points + segments). Same spec→figure contract as the triangle; no pixels in marking.
- Optional stretch (Pro): interactive "drag to build figure 4" → spec emitted back and compared. Not required for Term-1 pass.

## Frontend
- Reuse `MathAnswerArea`; add a **table-input** answer widget for `diagram_pattern` / `missing_terms` (small editable grid: position row vs value row). Mark cell-by-cell (deterministic).
- Keypad additions: `T_n` subscript tokens, `;` list separator, `…` ellipsis.
- Register `grade10_math_patterns_sequences` in the registry.

## Backend wiring
- `term_1/patterns_sequences_generator.py`.
- `_math_curriculum.py` topic entry + sections. API `GENERATORS` registration. New marking branch only if the table-input widget needs a `table_fill` type (likely reuse `make_short` with csv compare; add `table_fill` if a grid is cleaner).

## Adaptive metadata
`learning_objective_id` (`g10.patt.general_term`, `g10.patt.diagram` …), misconception tags (`off_by_one_in_n`, `used_term_value_as_position`, `forgot_common_difference_sign`).

## Testing
- Determinism across processes.
- All subskills produce valid output; `diagram_pattern` renders figures 1–4 in JSXGraph and the far-term answer marks correctly.
- Procedure Tracker on a `word_problem` (e.g. stadium rows) marks method + accuracy with carry-over.
- Browser: table-input grid marks per cell; pattern figures render cleanly.
- `npm run build` green.

## Estimated surface
1 backend generator (~400–500 lines), `_diagram.py` +~120 lines (two figure families), `DiagramRenderer.jsx` +~120 lines (`PatternRenderer`), optional `TableInput` widget (~120 lines), plus registry/keypad/curriculum/API wiring (~50 lines).
