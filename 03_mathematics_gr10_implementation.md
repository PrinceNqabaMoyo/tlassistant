# Implementation Plan 3 — Mathematics Grade 10 (Term 1) + the maths rendering/marking pipeline

Based on your 5 updated docs in
`caps-ai-backend/curriculum_docs/Mathematics_Gr10/Term 1/`:
1 Algebraic Expressions · 2 Exponents · 3 Patterns and Sequences ·
4 Equations and inequalities · 5 Trigonometry — and the comments embedded in each.

## 0. What the docs explicitly demand (from the `## Comments` blocks)
- **Proper maths rendering**, because the docs were typed in WordPad/Notepad with
  workarounds we must *undo* in the app:
  - `^` → real **superscripts/exponents**.
  - `/` and bracketed fractions → **vertical fractions** (numerator over denominator);
    drop the clarity-brackets when rendering vertically.
  - Recurring decimals (dots/bars misaligned in text) → **correct dot/bar over digits**.
  - `\~x\~` → **subscripts** (e.g. Tₙ).
  - surds, set symbols (ℝ ℚ ℤ ℕ ℕ₀), etc.
- **`DIAGRAM[ …natural-language description… ]`** placeholders are used heavily
  (Trig 64×, Equations 19×, Algebra 4×, Patterns 3×). These are the author's diagram
  descriptions — the "descriptive parameters" you mentioned.
- **Animated arrows** to demonstrate procedures (e.g. showing a term move across an `=`).
- **Interactive canvas / SOTA instrument** so a learner can *set up / draw a graph* while
  answering — in **scaffold, practice AND assessment**.
- **All working vertical**, like on paper (couples directly with Plan 1's Working Pad).
- A **specialised maths/science keypad** (computer/mobile keyboards can't type the glyphs);
  *grow the keypad as we discover characters per topic.*
- Generators must **NOT copy questions** — use them as **archetypes** to produce
  **unlimited correct variety**, and may **invent new diagram patterns**.
- **Decimal separator conflict to resolve:** doc 1's comment says use `.`, but doc 2's
  comment and *all* body text use `,` (e.g. `0,4`, `10,589`, `53,13°`). SA/CAPS standard
  is the **comma**. **Recommendation: use `,` as the decimal separator everywhere** and
  reserve `.` / `·` for multiplication. (Need your confirmation — see Open Questions.)

## 1. Why maths is different from BS/EMS (and what changes)
BS/EMS generators select from **hand-written content banks** (answers are pre-authored
text). Maths cannot do that at scale because **answers must be computed** and must stay
correct across infinite numeric variants. So:

- **Backend gains a symbolic engine (`sympy`).** Generators pick random parameters
  (seeded, deterministic), then **compute** the canonical answer *and* the step-by-step
  canonical solution. Same seed → identical question + solution (still 100% deterministic,
  no LLM).
- This canonical step graph is exactly what **Plan 1 (procedure tracker)** consumes, and
  what the **marker** checks against. The three plans share one data structure.

## 2. Rendering stack (frontend)
- **KaTeX** for all maths (AGENTS.md Rule 9 already names KaTeX). Add `katex`. Generators
  emit **LaTeX strings** (and/or a small AST) instead of the WordPad plain text. A thin
  `<MathText>` component renders inline/block LaTeX; handles fractions, superscripts,
  surds, recurring-decimal macros (`\overline{}` / `\dot{}`), set symbols.
- **Interactive graphing/geometry: JSXGraph** (open-source, offline, self-hostable —
  fits your HF/self-host goal; Desmos is proprietary/licensed, so avoid for core). Used
  for the answer canvas where learners build/draw graphs and diagrams.
- **Plotly** (already a dependency) only for static statistical plots if needed.
- **Animated procedure arrows:** a small `<StepAnimator>` that, given two adjacent
  canonical steps, animates the transformation (e.g. a term sliding across `=` with a sign
  flip). Driven by the canonical step graph — no bespoke animation per question.

## 3. The Diagram pipeline (your point about descriptive parameters)
This is the crux. We use **one shared, structured Diagram Spec (JSON)** in *both*
directions, so rendering and marking are symmetric and deterministic where possible.

**Diagram Spec (example):**
```json
{ "type": "triangle",
  "points": {"A": [0,0], "B": [4,0], "C": [4,3]},
  "segments": [["A","B"],["B","C"],["C","A"]],
  "right_angles": ["B"],
  "labels": {"AB": "4", "BC": "3", "CA": "?"},
  "annotations": [{"at": "A", "angle": "θ"}] }
```

- **Authoring:** each `DIAGRAM[…]` archetype in the docs is translated **once**, by us,
  into a parametric spec generator (numbers vary with the seed). We do **not** ask an LLM
  to render diagrams at runtime.
- **Rendering:** a deterministic `<DiagramRenderer spec=…>` maps the spec to JSXGraph/SVG.
  A fixed set of archetype renderers covers the bulk: number line, Cartesian axes + line/
  parabola, labelled triangle/quadrilateral, angles, real-number Venn/oval diagram, etc.
- **Marking diagrams the learner builds/edits/draws:** the interactive canvas **emits the
  same Diagram Spec**. Marking is then:
  1. **Deterministic:** compare learner spec vs canonical spec (points within tolerance,
     correct segments/labels/intercepts/gradient). Handles most graph-plotting questions.
  2. **Agent (Pro):** for partial credit / ambiguous constructions, serialise the spec to
     text and let the LLM judge against the canonical spec + rubric. The **serialised spec
     is the "descriptive parameter the LLM can interpret accurately"** — the LLM never sees
     raw pixels, only a precise structured description.

This directly fixes your two past pain points: visual aids stop being an "appendage"
(the diagram *is* the question/answer surface), and diagrams become **markable** because
they live as structured data, not images.

## 4. Marking pipeline (deterministic + agent), maths-specific
- **Single value / expression:** `sympy` equivalence — `1/2`, `0,5`, `0.5`, factored vs
  expanded, `2^{-1}` all compare equal. No string matching.
- **Multi-step working:** per-step symbolic equivalence (Plan 1) → method/accuracy marks.
- **Graph/diagram answers:** Diagram Spec comparison (Section 3).
- **Restrictions/edge cases** the docs flag (e.g. trig "no solution when sin/cos > 1",
  excluded values for fractions) become explicit checks in the canonical solution.
- **Pro** adds Socratic feedback + targeted variants on the weak subskill.

## 5. The specialised maths keypad
- Extend existing `src/components/EnhancedMathKeypad.jsx` into a **registry-driven** keypad:
  a central `mathSymbols` registry (glyph, LaTeX, insert-template) with **per-topic groups**
  that we extend as each topic is built (as the docs instruct).
- Term-1 starter set: fraction template, exponent/superscript, subscript, √ ∛ ⁿ√, π, °,
  θ α β, ≤ ≥ ≠ ≈ ±, ℝ ℚ ℤ ℕ ℕ₀, recurring-decimal template (bar/dot), `( )`, `×` `÷`.
- The keypad feeds the **Working Pad** (Plan 1) and any answer field; output is LaTeX.

## 6. Backend structure (mirrors BS/EMS, adds sympy)
```
caps-ai-backend/app/utils/grade10_mathematics/
  _math_common.py        # sympy helpers, LaTeX emit, diagram-spec builders,
                         # canonical-solution + metadata helpers (seeded RNG)
  term_1/
    algebraic_expressions_generator.py
    exponents_generator.py
    patterns_sequences_generator.py
    equations_inequalities_generator.py
    trigonometry_generator.py
caps-ai-backend/app/api/grade10_mathematics.py   # /generate, /mark, /sections
```
- Each generator: per-subskill archetypes, seeded parameter draw, sympy-computed answer +
  canonical step graph + (where relevant) diagram spec, plus the adaptive metadata we
  already emit for BS/EMS (`learning_objective_id`, `misconception_tags`, etc.).
- Keep files < 2000 lines (Rule 4); split by subskill if needed.
- Note: existing **Gr12 maths controllers already call `/api/math/grade12/...`** — I'll
  confirm whether a Gr12 maths backend exists or those are stubs, and keep the new Gr10
  endpoint naming consistent with whatever is real.

## 7. Frontend structure (reuse the scaffold/practice/assessment shell)
```
src/components/workspace/grade10/mathematics/
  shared/  MathText.jsx  DiagramRenderer.jsx  InteractiveMathCanvas.jsx
           WorkingPad.jsx  StepAnimator.jsx  createGrade10MathController.js
           createGrade10MathRoute.jsx
  term-1/<topic>/{controller.js, Scaffold, Practice}.jsx
src/components/workspace/registry/grade10MathematicsRegistry.js
```
- **Visual aids integrated, not bolted on:** the diagram/canvas renders *inside* the
  question and the Working Pad *is* the answer surface; scaffold steps can play the
  `StepAnimator` inline instead of a separate "visual aids" tab.

## 8. Suggested build order (vertical slice first, per Rule 15)
1. **Foundations:** add KaTeX + JSXGraph + sympy; build `MathText`, the keypad registry,
   `WorkingPad`, and `_math_common.py` (sympy + canonical-solution + diagram-spec helpers).
2. **Slice A — Algebraic Expressions** (mostly symbolic, few diagrams): proves
   rendering + symbolic generation + Working Pad + keypad + symbolic/step marking.
3. **Slice B — Trigonometry** (diagram-heavy): proves the Diagram Spec render+mark pipeline
   and the interactive canvas.
4. Then Exponents, Patterns, Equations & Inequalities (Equations needs the interactive
   graph canvas explicitly).
5. Wire adaptive progression + the procedure-tracker tool (Plans 1) across the topics.

## 9. Ideas / improvements I'd propose on top of your docs
- **Generators compute, never copy** (already your instruction) — enforced by sympy; this
  also means *infinite* practice and exam variants for free.
- **Carry-over (method/accuracy) marking** from day one — it's the single biggest "feels
  like a real exam" win and it's only possible because of the canonical step graph.
- **One Diagram Spec for render + mark** — avoids the old "visual aid is an appendage"
  problem and makes constructions gradable.
- **Keypad as a registry** so it self-grows per topic, exactly as the docs ask.
- **Decimal comma** standard end-to-end (pending your confirmation).

## 10. Open questions (need your call before I build)
1. **Decimal separator:** confirm **comma `,`** everywhere (overriding doc 1's `.` note)?
2. **Symbolic engine:** OK to add **`sympy`** (backend) for generation + marking?
3. **Graphing lib:** **JSXGraph** (open-source, self-hostable) for the interactive canvas —
   agreed? (vs Desmos, which is proprietary.)
4. **First slice topic:** start with **Algebraic Expressions**, then **Trigonometry** for
   the diagram pipeline — agreed?
5. **Diagram coverage:** deterministic archetype renderers now + agent-judged long tail
   later — acceptable?
6. **Couple Plan 1 in from the start** for maths (Working Pad + step marking), rather than
   retrofitting — agreed?
