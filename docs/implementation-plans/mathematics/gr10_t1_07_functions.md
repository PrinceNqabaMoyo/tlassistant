# Implementation Plan — Gr10 Mathematics, Term 1: Functions

**Status:** outstanding. The final Term-1 Gr10 Maths topic (Algebra ✅, Trig ✅, Exponents ✅, Equations & Inequalities ✅, Patterns & Sequences ✅).
**Pattern:** deterministic SymPy stack (no LLM) + Procedure Tracker + comma decimals — identical to the shipped topics.
**New surface (the headline of this topic):** a reusable, parametric **function-graph Diagram Spec** (`kind: "function_graph"`) and an **interactive parameter-manipulation grapher** (drag `a`/`q` sliders, watch the curve transform), serialized back as the same spec so it is deterministically markable.

Source doc: `caps-ai-backend/curriculum_docs/Mathematics_Gr10/Functions.md` (6073 lines).

## Embedded-comment compliance (these are strong directives)
- **"In the legacy implementation I had a visual aid that let users manipulate parameters of functions and see how their manipulations changed the graph. We need a version of that here. It should be shareable with other grades' mathematics and with Technical Mathematics."**
  → The grapher is a single, standalone `FunctionGrapher` component driven entirely by a `function_graph` Diagram Spec (family + `a`, `q`, base `b`). Nothing in it is Gr10-specific: any grade/subject that emits the spec gets the same widget. The interactive answer mode `function_transform` serializes `{a, q, b}` and is marked structurally (no pixels), exactly like `diagram_select` / `number_line_build`.
- **"Sketching of the graphs must be based on the observation of [the effect of a and q]."** (syllabus note) → effect-of-parameter subskills are first-class (MCQ + the interactive grapher), and the sketch subskills reduce to determining `sign of a`, intercepts and turning point — the doc's three/four characteristics — rather than free-hand drawing.
- **Domain/range in set AND interval notation** (doc has dedicated sections) → both notations are taught; questions are posed as MCQ over notation choices (reliable to mark) plus numeric-bound `value`/`value_pair` where appropriate.

## Why this is the right shape for Functions
Functions is the first Gr10 topic whose *core object is a graph*. The deterministic discipline still holds: every graph is a **computed** artifact (SymPy evaluates the family at sampled `x`), the spec is plain JSON (the "descriptive parameter" the Pro agent can read), and marking compares structured values, never rendered pixels.

## Subskills (generators)

| key | what it tests | answer mode | archetype |
|-----|---------------|-------------|-----------|
| `function_notation_eval` | evaluate `f(x)` at a value | `value` | `f(x)=2x+1`, find `f(-3)` |
| `function_notation_solve` | find input `x` given `f(x)=k` | `value` | solve `2x+1=27` |
| `domain_range` | identify domain/range of a family | `mcq` (set ↔ interval) | range of `y=ax²+q` is `[q;∞)` |
| `representation_convert` | table/words/ordered-pairs ↔ formula | `expression` / `value` | "one is 5 less than the other" → `f(x)=x-5`; complete a table cell |
| `linear_gradient_intercept` | read `m`, `c` from `y=mx+c` | `value` / `value_pair` | identify gradient & y-intercept |
| `linear_intercepts` | x- and y-intercepts of a line | `value_pair` + `steps` | `g(x)=x-1` → `(1;0)`, `(0;-1)` |
| `linear_find_equation` | find `y=mx+c` from two points / gradient + point | `expression` + `steps` | through `(0;-1)` & `(2;3)` |
| `quadratic_effect` | effect of `a` (shape/stretch/reflect) and `q` (shift) | `mcq` + `function_transform` | "what does `q<0` do?" / drag sliders to match |
| `quadratic_features` | turning point, axis of symmetry, intercepts of `y=ax²+q` | `value_pair` / `value` | TP `(0;q)`, axis `x=0` |
| `hyperbola_features` | asymptotes & effect of `a`, `q` on `y=a/x+q` | `mcq` + `value` | horizontal asymptote `y=q` |
| `exponential_features` | growth/decay & asymptote of `y=ab^x+q` | `mcq` + `value` | asymptote `y=q`; `b>1` growth |
| `trig_graph_features` | amplitude/period/effect of `a`,`q` on `sin/cos/tan` (0°–360°) | `mcq` + `value` | amplitude `|a|`, range `[q-|a|; q+|a|]` |
| `interpret_graph` | read a rendered graph (intercept / point / which family) | `value_pair` / `mcq` | render `function_graph`, read off |
| `match_equation_graph` | match an equation to its graph | `mcq` | pick the parabola for `y=-x²+1` |
| `parameter_manipulation` | **interactive**: drag `a`/`q` to match a target curve | `function_transform` | reproduce `y=2x²-3` |

(Builders are grouped into one generator file; if it approaches the 2000-line AGENTS limit, split per family into a `term_1/functions/` package — `_linear.py`, `_quadratic.py`, `_hyperbola_exp.py`, `_trig.py`, `_notation.py`.)

## Generator design
- Families share one parametric core: `f(x; a, q, b)` for `linear` (`a·x+q`, here `m=a`,`c=q`), `quadratic` (`a·x²+q`), `hyperbola` (`a/x+q`), `exponential` (`a·b^x+q`), `sin`/`cos`/`tan` (`a·trig(x)+q`).
- SymPy computes intercepts (`solve(expr, x)`), turning points (vertex for quadratics = `(0,q)`), asymptotes (`y=q`, plus `x=0` vertical for hyperbola), ranges (from `a` sign), and sampled points for rendering.
- Canonical solution graphs mirror the doc's worked steps (e.g. y-intercept: "let `x=0`", x-intercept: "let `y=0`", find-equation: "`m = Δy/Δx`" → "substitute a point" → "state `y=mx+c`").
- `common_errors`: `swapped_m_and_c`, `wrong_intercept_axis`, `forgot_negative_reflection`, `confused_stretch_with_shift`, `wrong_asymptote`, `swapped_domain_range`, `amplitude_sign_error`.

### Answer modes
- Reuse existing: `value`, `expression`, `value_pair`, `mcq`, `steps`.
- **New `function_transform`** (interactive grapher): student-submitted `{a, q, b}` compared to the key within an exact/rational tolerance. Marked by a new `mark_function_transform` in `procedure_tracker.py` (structural, no pixels) — the Functions analogue of `mark_number_line`.
- Domain/range deliberately posed as **MCQ over canonical notations** (both set-builder and interval) rather than free-text set parsing, which is unreliable to mark deterministically. Numeric bounds (e.g. range of a quadratic) additionally available as `value`.

## NEW: `function_graph` Diagram Spec (bidirectional, reusable)
Extend `_diagram.py`:
```jsonc
{
  "kind": "function_graph",
  "family": "quadratic",          // linear | quadratic | hyperbola | exponential | sin | cos | tan
  "params": { "a": 2, "q": -3, "b": 2 },
  "domain": [-5, 5],              // x-range to plot (degrees for trig: [0, 360])
  "features": {                    // optional, for static annotated figures
    "y_intercept": [0, -3],
    "x_intercepts": [[-1.22, 0], [1.22, 0]],
    "turning_point": [0, -3],
    "asymptotes": { "horizontal": -3 }
  },
  "interactive": { "sliders": ["a", "q"], "target": {"a": 2, "q": -3, "b": 2} },
  "caption": "Drag a and q so the curve matches the dashed target."
}
```
- **Render** (`DiagramRenderer.jsx` → new `renderFunctionGraph`): JSXGraph board with axes/grid; plot the family with `JXG.functiongraph`; draw asymptotes (dashed), intercept/TP points when `features` present.
- **Interactive** (`FunctionGrapher` / `function_transform`): show JSXGraph sliders for the listed params, live-redraw the curve, draw the `target` curve dashed, and emit `{a, q, b}` back to `MathAnswerArea` on submit.
- **Reusability:** the component takes only the spec; Gr11/Gr12/Technical Maths can emit the same `function_graph` kind to get an identical grapher.

## Frontend
- `DiagramRenderer.jsx`: add `function_graph` static rendering.
- New `FunctionGrapher.jsx` (interactive sliders) wired into `MathAnswerArea` for `question_type === "function_transform"`; Check submits the serialized params.
- `MathAnswerArea` / `createMathTopicRegistry`: handle the new question type (no keypad needed in transform mode; the canvas is the answer surface).
- Keypad: add a `functions` group — `f(x)`, `( )`, `x²`, fraction, and reuse trig keys for trig-graph subskills.
- Curriculum + registry: add `grade10_math_functions` topic (+ subskills/sections) to `_math_curriculum.py`; `createMathTopicRegistry({ topicKey: 'grade10_math_functions', modePrefix: 'grade10_functions' })`; topic-card in `MathTopicModeCards.jsx` gated by `flags.isGrade10Math && isGrade10FunctionsTopic(topicName)` (new matcher matching the `"Functions"` topic name); `TOPIC_KEYPADS` entry.

## Backend wiring
- `term_1/functions_generator.py` (`generate = build_generate(SUBSKILLS, default_subskill=...)`).
- `term_1/__init__.py` export; API `GENERATORS["grade10_math_functions"]`; `_mark_one` branch for `function_transform`.
- `_diagram.py` `function_graph(...)` builder; `_math_common.py` `make_function_transform(...)` builder.

## Adaptive metadata
LO ids per family (`math10_functions.notation`, `.linear`, `.quadratic`, `.hyperbola`, `.exponential`, `.trig`, `.interpret`); misconception tags from `common_errors`; higher `minimum_mastery_score` for the parameter-effect/interpretation subskills (synthesis skills).

## Testing
- Determinism: same seed → byte-identical questions for every subskill (cross-process check).
- Marking: `function_notation_eval` (`value`), `linear_find_equation` (`expression` + `steps`), `quadratic_features` turning point (`value_pair`), domain/range MCQ, and `function_transform` (drag to `a=2,q=-3` → correct; wrong `q` → targeted feedback).
- Browser: render each family's `function_graph`; the interactive grapher's sliders move the curve and submit; comma decimals parse.
- `npm run build` green; recording attached to the PR (same bar as Algebra/Trig).

## Estimated surface
1 generator (~700–1000 lines, split if needed), `_diagram.py` +~70 lines, `_math_common.py` +~40 lines, `procedure_tracker.py` +~40 lines (`mark_function_transform`), `DiagramRenderer.jsx` +~120 lines (`renderFunctionGraph`), new `FunctionGrapher.jsx` (~180 lines), plus registry/keypad/curriculum/matcher/API wiring.

---

After Functions lands, **Gr10 Term 1 Mathematics is complete** (6/6 topics), and the reusable `function_graph` grapher is available for Gr11/Gr12/Technical Maths to adopt.
