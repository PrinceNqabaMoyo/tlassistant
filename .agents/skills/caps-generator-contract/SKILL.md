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
- **Accounting & EMS:** 2D tabular schemas with cell coordinates `(row, col)` and cell types:
  - `required`: Student must enter; earns positive mark.
  - `given`: Pre-filled context; not marked.
  - `must_be_empty`: Must remain blank; filling earns a `-1` deduction.
- **Mathematics:** KaTeX-compatible LaTeX strings, SymPy canonical solution graphs, and South African comma decimal separator normalization (`_decomma`).
- **Business Studies & Sciences:** Rubric criteria + concept match definitions directly matching `curriculum_docs_auto/`.

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
