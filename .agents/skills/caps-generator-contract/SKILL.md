---
name: caps-generator-contract
description: Author, test, and calibrate deterministic 6-pillar South African CAPS question generators for Mathematics, Accounting, EMS, and Sciences. Use when creating, refactoring, or auditing question generators.
---

# 6-Pillar CAPS Generator Contract Runbook

Deterministic question generators are the architectural foundation of Fundile's Standard tier.
All generators MUST strictly satisfy the **6-Pillar Contract** to integrate seamlessly with the Calendar Exam Engine, Post-Exam Triage Report, Teacher LMS Cockpit, and Adaptive Deconstruction.

## The 6 Pillars

### 1. Term & Calendar Metadata (Exam-on-Demand)
Every generator and archetype payload must declare:
- `term`: integer (`1`, `2`, `3`, or `4`) matching the South African CAPS academic calendar term.
- `caps_weight_percent`: integer (approximate weighting in CAPS final exams).
- `suggested_duration_mins`: integer (expected completion time for an authentic exam question).

The Calendar Engine strictly enforces `term <= selected_term` so students in Term 1/2 are never assessed on Term 3/4 content.

### 2. Deconstructibility & Atomic Micro-Drills (`mode`)
Every compound question generator must support atomic constituent sub-drills via:
```python
def generate_question(seed: int = 42, mode: str = "compound"):
    # mode = "compound" | "elementary_<subskill>"
```
When a learner fails a compound problem twice in practice mode, the engine invokes `mode="elementary_<subskill>"` to isolate prerequisite subskills before returning to the compound problem.

### 3. Standardized snake_case Misconception Taxonomy
Never use free-form error messages. Tag predictable student errors with standard snake_case identifiers:
- *Accounting/EMS:* `net_vs_gross_confusion`, `debit_credit_inversion`, `omitted_balance_b_d`, `vat_inclusive_exclusive_slip`
- *Mathematics:* `sign_error_distribution`, `forgot_pm_square_root`, `reciprocal_confusion`, `linear_for_quadratic`
- *Business Studies / Sciences:* `macro_vs_market_confusion`, `omitted_legislation_impact`, `units_conversion_slip`

### 4. Teacher-Editable Marking Schema
Questions must emit a structured `marking_schema` object:
```python
"marking_schema": {
    "total_marks": 12,
    "marking_points": [
        {"id": "mp_1", "desc": "Transaction date & document number", "marks": 1, "editable": True},
        {"id": "mp_2", "desc": "Bank gross amount (incl. VAT)", "marks": 3, "editable": True}
    ],
    "deductions": [
        {"rule": "must_be_empty_filled", "penalty": -1}
    ],
    "carry_forward_rule": "consequential_accuracy"
}
```

### 5. Deterministic 3-Tier Pre-Baked Hints (Zero-LLM)
All hints must be calculated ahead of time with zero LLM dependency:
- **Tier 1 (Location / Nudge):** Directs attention to the specific cell, line, or variable without giving the answer.
- **Tier 2 (Directional Rule):** Explains the underlying curriculum theorem, accounting rule, or formula.
- **Tier 3 (Worked Step Calculation):** Demonstrates the exact numerical or algebraic transition for the current seed.

### 6. Modality-Appropriate Representation

> **Diagram Description → Design Law** <!-- RULE-ANCHOR: diagram_description_design_law -->
> Figure descriptions in `curriculum_docs_auto/` (`>DIAGRAM[...]`, `Figure N.N`, `Diagram N`, `Graph N`, narrated layouts/measurements) exist only because the PDF images could not be stored in Markdown. Treat them as **specs for a figure to draw**: emit a seeded `diagram_spec` with the figure's parameters, and phrase the question to refer to it ("Use the plan below…"). Never copy or paraphrase the description into `question_text`. Decorative photos carrying no data are exempt. See `diagram_doctrine.md` §9; detector: `python scripts/audit_diagram_description_leak.py`.
- **Accounting & EMS:** 2D tabular schemas with cell coordinates `(row, col)` and cell types:
  - `required`: Student must enter; earns positive mark.
  - `given`: Pre-filled context; not marked.
  - `must_be_empty`: Must remain blank; filling earns a `-1` deduction.
- **Mathematics:** KaTeX-compatible LaTeX strings, SymPy canonical solution graphs, and South African comma decimal separator normalization (`_decomma`).
- **Business Studies & Sciences:** Rubric criteria + concept match definitions directly matching `curriculum_docs_auto/`.

### 7. 50-Archetype Diversity & Two-Surface Visual/SimuLearn Contract
Every topic generator must expose `SUBSKILLS: List[str]` containing $\ge 50$ distinct semantic snake_case archetype IDs (zero `subskill_1..52` or `_subskill_N` synthetic shims).
- **Surface 1 (Question Card)**: Static 2D exam figure (`diagram_spec` with `kind`, `diagram_role: "identify" | "context"`, `grade_mask`, and seed variation bound to prompt and worked solution).
- **Surface 2 (Visual Companion & SimuLearn)**: Structured `canonical_solution.steps` (`from_latex`, `to_latex`, `justification`) or worked solution mark breakdown allowing `SimuLearnPlayer.jsx` to render synchronized step-by-step worked replays for that exact archetype.

### 8. The 5 Flash-Proof Rules for 50-Archetype Expansion (Mandatory Pre-Flight)
When authoring or expanding a 50-archetype topic generator, **never** commit these 5 failure modes:
1. **Valid `diagram_spec` Schema Only**: Always use `"diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}` (or a registered `DiagramRenderer.jsx` kind such as `pie_chart`, `bar_graph`, `number_line`). Never invent unrenderable schemas like `{"type": "svg", "source": svg}`, `{"kind": "svg", ...}`, `{"kind": "dot_pattern", ...}`, or `{"kind": "concept_card", ...}`.
2. **Never Embed `{svg}` Inside `prompt` / `question_text`**: Never write `f"...\n\n{svg}"` in `prompt`. Always pass the SVG via `diagram_spec`.
3. **Genuine `rng` Parameterization (Both Prompt & Diagram)**: Never hardcode numbers in the question or SVG while only using `rng.randint` on `"id"`. Every `diagram_spec` must vary its coordinates, labels, or values across seeds `101, 102, 103` (`seed_varies` gate).
4. **Avoid False-Positive Leak Phrases in Pure-Text Archetypes**:
   - In non-diagram questions, never use figure-noun phrases (`"in the diagram"`, `"shown below"`, `"the graph shows"`, `"pie chart"`, `"bar graph"`, `"image point"`, `"grid"`), or attach a seeded `inline_svg` diagram if the question discusses a visual object.
   - Even when a valid `diagram_spec` is attached, write `"The graph illustrates..."` or `"Refer to the graph..."` instead of `"The graph shows..."` / `"The diagram shows..."` (which triggers `STRONG_PHRASES` -> `DESCRIBED_NOT_DRAWN`).
   - In number-sequence prompts, write `1, 4, 9, ...` instead of `\dots` (because `\dots` tokenizes to `"dots"` and triggers dot-pattern figure matching).
5. **Run the Single-Topic Validator Immediately After Every Topic**:
   ```bash
   python scripts/validate_topic_50_archetypes.py --grade <G> --subject "<Subject>" --topic "<Topic>"
   ```
   Do not move to the next topic until it prints `OVERALL RESULT: PASS (Exit Code 0)`.

---

## Technical Standards & Verification

### Purity Linter
Generators must NEVER import any LLM SDK, network library, or cloud service. Run:
```bash
python caps-ai-backend/scripts/lint_purity.py
```
Forbidden imports: `openai`, `google.generativeai`, `groq`, `anthropic`, `langchain`, `transformers`, `requests`, `urllib`, `httpx`, `aiohttp`, `socket`.

### Complexity Standard
- Cyclomatic Complexity (CC) must not exceed 12 per generator function. Check using radon:
```bash
radon cc caps-ai-backend/app/utils/ -s -n B
```

### Comma Decimals in Mathematics
In South African CAPS, commas represent decimal points (e.g. `3,14` not `3.14`).
Use the project's `_decomma(val)` helper to parse user inputs, and output LaTeX formatted with `{,}` (e.g., `3{,}14`).
