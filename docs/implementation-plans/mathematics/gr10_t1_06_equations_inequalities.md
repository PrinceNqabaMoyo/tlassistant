# Implementation Plan — Gr10 Mathematics, Term 1: Equations & Inequalities

**Status:** outstanding. Topic 4 of 5. The largest Term-1 topic (source doc 3192 lines).
**Pattern:** deterministic SymPy stack (no LLM) + **Procedure Tracker from the start** (this topic is the strongest fit — every subskill is multi-line working). Plus a **third Diagram Spec extension: the number line** (for inequalities) and an optional **Cartesian plane** (for the graphical simultaneous method).

Source doc: `caps-ai-backend/curriculum_docs/Mathematics_Gr10/Term 1/4 Equations and inequalities.md`.

## Embedded-comment compliance (these are strong directives)
- **"Where graphs are needed, develop an interactive canvas … apply to scaffold, practice AND assessment."** → number line is interactive (set open/closed dot + direction); Cartesian graph is render-first, interactive-line as stretch.
- **"All working … must be vertical, the way a user arranges it on paper."** → Working Pad (already vertical) is mandatory here; the Procedure Tracker marks it line-by-line.
- **"A special keypad is needed … pick up characters as you build."** → add `≤ ≥ < > ≠ ∞ ( ) [ ]` and the number-line tokens.

## Subskills (generators)

| key | what it tests | answer mode | archetype |
|-----|---------------|-------------|-----------|
| `linear_equations` | solve `ax+b=c`, brackets, fractions, restrictions | `steps` + `value` | `2(x−3)=…`, `4/(3x+1)=…` (note `x≠−1/3`) |
| `quadratic_standard_form` | rewrite to `ax²+bx+c=0` | `equation` | doc Q1 a–c |
| `quadratic_by_factorising` | solve via factorisation / perfect square | `steps` + `set` | `x²+…=0 → {r1,r2}` |
| `quadratic_restrictions` | fractional quadratics w/ excluded values | `steps` + `set` (state restrictions) | doc Q3 a–d |
| `simultaneous_substitution` | 2×2 linear by substitution | `steps` + `value pair` | `x−y=1; 3=y−2x` |
| `simultaneous_elimination` | 2×2 linear by elimination | `steps` + `value pair` | doc examples |
| `simultaneous_graphical` | read solution as intersection point | `diagram (cartesian) + value pair` | render two lines; answer = intersection |
| `word_problems` | translate → equation → solve | `steps` + `value` | age/number/geometry money problems |
| `literal_equations` | change the subject of a formula | `expression` | solve for a named variable |
| `linear_inequalities` | solve, **flip on ÷/× by negative**, number line + interval | `steps` + `inequality` + `number_line` + `interval` | `6−r>2 → r<4`, `4q+3<2(q+3)` |

## Generator design
- SymPy `solve`, `Eq`, `linsolve` for systems; `factor`/`roots` for quadratics; `solveset` with domain for restrictions.
- Restrictions: compute excluded values (denominator zeros) and **carry them in the answer key** so the marker can require the learner to exclude them.
- Canonical solution graph mirrors the doc's numbered steps (expand → rearrange → divide/factorise → check). Crucially the doc always **checks by substitution** — encode a final `verify` step so the tracker can reward it.
- `common_errors`: `forgot_to_flip_inequality`, `divided_by_variable`, `sign_error_on_transpose`, `dropped_a_root`, `ignored_restriction`, `lost_solution_dividing_by_x`.

### Answer modes needed (extend `_math_common.py`)
- `set` already used by Trig/Exponents (solution sets).
- `value_pair` — for simultaneous `(x; y)`. New light normaliser.
- `inequality` — compare `r < 4` style (SymPy relational equality).
- `interval` — interval notation `(−∞; 4)`; map to SymPy `Interval` and compare.

## NEW: number-line Diagram Spec (interactive)
Extend `_diagram.py`:
```
{ "kind": "number_line", "min": -3, "max": 3, "ticks": 1,
  "point": {"at": -0.5, "closed": false},
  "ray": {"from": -0.5, "direction": "negative"},   # optional
  "label": "x ≤ −1/2" }
```
- Render in `DiagramRenderer.jsx` (`NumberLineRenderer`): axis with arrowheads, open (white) / closed (black) dot, bold direction ray.
- **Interactive answer mode** (`number_line_build`): learner clicks a position, toggles open/closed, picks direction. Emitted spec is compared to the key spec deterministically (position + closed flag + direction). This is the inequalities analogue of `diagram_select`.
- Marking: structural compare of `{at, closed, direction}` — no pixels.

## OPTIONAL: Cartesian plane (graphical simultaneous)
- `kind: "cartesian_lines"` with two lines + intersection point; render via JSXGraph (already have `cartesian_point` stub in `_diagram.py`).
- Term-1 pass: **render + read-off** (answer = intersection coordinate, typed). Interactive line-drawing is a Pro/stretch item (matches the comment's ambition but is heavy). Call this out so it isn't silently dropped.

## Frontend
- Reuse Working Pad + `MathAnswerArea`. Add:
  - `NumberLineRenderer` + interactive `number_line_build` control.
  - `inequality` / `interval` input parsing in `mathLatexify` (accept `<= >= < > ( ) [ ] ∞`).
  - `value_pair` input (two boxes or `x=…, y=…`).
- Keypad additions: `≤ ≥ < > ≠ ∞ ( ) [ ]`, and a number-line "open/closed dot" + "direction" affordance lives in the canvas, not the keypad.
- Register `grade10_math_equations_inequalities`.

## Backend wiring
- `term_1/equations_inequalities_generator.py` — likely the biggest generator; keep < 2000 lines (AGENTS rule 4). If it grows, split per family (`_equations.py`, `_simultaneous.py`, `_inequalities.py`) under a `term_1/equations/` package.
- `_math_curriculum.py` topic + sections; API `GENERATORS` registration.
- New marking branches: `number_line_build` (structural), `value_pair`, `inequality`, `interval`. Reuse `math_steps` for all the worked subskills.

## Adaptive metadata
LO ids per family (`g10.eq.linear`, `g10.eq.quad`, `g10.eq.simul`, `g10.ineq`), misconception tags from `common_errors`, `minimum_mastery_score` higher for quadratics/simultaneous.

## Testing
- Determinism across processes for every subskill.
- Procedure Tracker: a `linear_inequalities` solution that **forgets to flip** → localised first error `forgot_to_flip_inequality` with carry-over; a correct one earns the `verify` mark.
- Number line: build the ray for `r<4` (open dot at 4, ray negative) → marked correct; wrong open/closed flag → marked wrong with targeted feedback.
- Simultaneous: `value_pair` marking accepts `(−1; 0)` order-correct.
- Browser: interactive number line works in scaffold + practice; inequality/interval inputs parse comma decimals.
- `npm run build` green.

## Estimated surface
Largest of the three: 1 (or split) generator package (~700–1200 lines total), `_diagram.py` +~150 lines (number line + cartesian lines), `DiagramRenderer.jsx` +~200 lines (NumberLine + interactive build, optional cartesian), `_math_common.py` +~60 lines (value_pair/inequality/interval normalisers), plus registry/keypad/curriculum/API wiring.

---

## Sequencing recommendation (across the 3 outstanding topics)
1. **Exponents** first — pure algebra, **zero new UI**, fastest to land; completes the "type-an-expression" family.
2. **Equations & Inequalities** second — highest exam weight, introduces the **number-line interactive** (a clean, contained new canvas) and exercises the Procedure Tracker hardest.
3. **Patterns & Sequences** third — introduces **parametric pattern diagrams** + table input (most new front-end surface), and benefits from the diagram work done in Trig + the number line.

Each ships as its own PR into the same maths branch, build green, browser-tested with a recording (same bar as Algebra/Trig). After all 5 Term-1 topics land, Gr10 Term 1 Mathematics is complete and we pivot to the landing page → CAPS/NSC wording → teacher/tutor collab.
