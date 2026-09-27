# Simulation System — Implementation Plan

## 1. Purpose and Design Philosophy

The Simulation system provides a **per-archetype, canonical worked-example replay** that a student
can watch before or after attempting a question. It is not a general-purpose animation tool; it is
a deterministic playback of the exact solution to a specific question archetype, driven entirely by
data already produced by the existing generator pipeline.

### Core Principles

| Principle | Rationale |
|---|---|
| **One simulation per archetype, not per question** | Trains procedural transfer. The student learns *how this type of question is solved*, not just copies numbers from their specific variant. |
| **Canonical seed, fixed per archetype** | The simulation seed is chosen once by a developer/curator and stored. Every user who requests a simulation for archetype X sees the same worked example. |
| **Data-driven, not hardcoded** | The animation script is generated from the question response (solution graph, cell map). No bespoke animation code per topic. |
| **Non-intrusive trigger** | The simulation is opt-in. The student requests it; it does not run automatically. |
| **Works within existing workspace, not a separate view** | The SimulationPlayer mounts inside the current workspace shell, reading the same question data already loaded. |

---

## 2. Canonical Simulation Seed Strategy

### 2.1 The Problem This Solves

If a simulation were generated from the student's current random seed, they could:
- Ask for a simulation for every question they struggle with.
- Get a simulation that simply shows them the answer to *their specific numbers* — defeating the
  purpose of practice.
- Never develop the ability to transfer procedure across isomorphic variants.

### 2.2 The Canonical Seed Registry

A new static registry file is introduced on the backend:

```
caps-ai-backend/app/utils/simulation_seeds.py
```

```python
# Maps (subject_key, topic_key, archetype_key) → canonical_seed
# These seeds were hand-chosen to produce clear, well-scaled worked examples.
# Do NOT change these without re-reviewing all affected simulations.

SIMULATION_SEEDS: dict[tuple[str, str, str], int] = {
    # Mathematics — Grade 10
    ("mathematics", "grade10_math_algebraic_expressions", "factorise_trinomial"):       42,
    ("mathematics", "grade10_math_algebraic_expressions", "expand_double_brackets"):    7,
    ("mathematics", "grade10_math_algebraic_expressions", "simplify_surds"):            19,
    ("mathematics", "grade10_math_trigonometry",          "solve_right_triangle"):      55,
    ("mathematics", "grade10_math_trigonometry",          "find_side_given_angle"):     83,
    ("mathematics", "grade10_math_equations_inequalities","linear_inequality"):         31,
    ("mathematics", "grade10_math_equations_inequalities","quadratic_equation"):        12,

    # Accounting — Grade 10
    ("accounting",  "grade10_accounting_sole_trader",     "crj_entry"):                 9,
    ("accounting",  "grade10_accounting_sole_trader",     "cpj_entry"):                 17,
    ("accounting",  "grade10_accounting_sole_trader",     "debtors_ledger_posting"):    6,
    ("accounting",  "grade10_accounting_final_accounts",  "income_statement"):          23,
    ("accounting",  "grade10_accounting_final_accounts",  "balance_sheet"):             44,

    # Accounting — Grade 11
    ("accounting",  "grade11_accounting_sole_trader",     "crj_entry"):                 11,
    ("accounting",  "grade11_accounting_sole_trader",     "debtors_control"):           38,
    # ... extend as topics are added
}
```

### 2.3 Seed Selection Guidelines

When a developer registers a new archetype simulation seed, they must verify:
1. The question produced by the seed is **numerically clean** (no awkward decimals, no edge cases).
2. The worked solution has **3–7 steps** for maths, or **4–10 cell fills** for accounting — enough
   to be instructive, short enough to watch.
3. The question reads naturally in English (names, dates, amounts are realistic).

### 2.4 Per-User Simulation Anchor (Frontend)

Once a student has watched a simulation for an archetype, the canonical seed used is stored locally:

```
localStorage key:  fundile_sim_seed_{archetype_key}
value:             { seed: 42, watchedAt: ISO8601, archetypeKey: "factorise_trinomial" }
```

This record means:
- The student always gets the same simulation for that archetype in future sessions.
- The app can show a "You've seen this before" indicator.
- If the canonical seed is ever updated in `simulation_seeds.py`, the localStorage record is
  invalidated (version mismatch) and the new seed is fetched.

---

## 3. Simulation Data Model

### 3.1 Backend: Simulation Request

A new endpoint is added:

```
GET /api/simulation/{subject_key}/{topic_key}/{archetype_key}
```

The backend:
1. Looks up `SIMULATION_SEEDS` to get the canonical seed.
2. Calls the generator with `seed=canonical_seed, mode="simulation"`.
3. The generator returns the standard question response **plus** a `simulation_script` field.
4. The response is cacheable (`Cache-Control: public, max-age=86400`).

### 3.2 The `simulation_script` Field

Every generator that supports simulation must append a `simulation_script` to its response.

```json
{
  "question": { ... },
  "answer":   { ... },
  "simulation_script": {
    "type": "step_sequence",        // "step_sequence" | "cell_fill_sequence"
    "preamble_latex": "Factorise: $6x^2 + 11x + 3$",
    "steps": [ ... ],               // populated for maths
    "cell_fills": [ ... ],          // populated for accounting tabular questions
    "narration_style": "concise"    // "concise" | "detailed"
  }
}
```

---

## 4. Mathematics Simulation

### 4.1 Step Sequence Schema

Each step in `simulation_script.steps` maps directly to one entry in the existing `solution_graph`:

```json
{
  "step_index": 0,
  "rule": "identify_factors",
  "rule_label": "Find two numbers that multiply to ac and add to b",
  "from_latex": "6x^2 + 11x + 3",
  "to_latex":   "6x^2 + 9x + 2x + 3",
  "operation":  "split_middle_term",
  "highlight_tokens": ["11x", "9x", "2x"],
  "narration": "We need two numbers that multiply to 6×3=18 and add to 11. Those are 9 and 2.",
  "common_error": {
    "wrong_latex": "6x^2 + 6x + 5x + 3",
    "explanation": "6 and 5 add to 11 but multiply to 30, not 18."
  },
  "pause_ms": 1800
}
```

All fields except `common_error` are **required**. The `common_error` block is optional but strongly
encouraged — it is displayed as a sidebar callout during the simulation.

### 4.2 Generator Contract (Maths)

Every SymPy-backed maths generator must implement:

```python
def build_simulation_script(question_data: dict, seed: int) -> dict:
    """
    Returns a simulation_script dict for the given question.
    Called only when the endpoint receives mode="simulation".
    The solution_graph is already computed; this function formats it
    into the simulation_script schema.
    """
    steps = []
    for i, node in enumerate(question_data["solution_graph"]):
        steps.append({
            "step_index":       i,
            "rule":             node["rule"],
            "rule_label":       RULE_LABELS[node["rule"]],   # lookup from shared dict
            "from_latex":       node["from_latex"],
            "to_latex":         node["to_latex"],
            "operation":        node["op"],
            "highlight_tokens": node.get("highlight_tokens", []),
            "narration":        node.get("narration", ""),
            "common_error":     node.get("common_errors", [{}])[0] if node.get("common_errors") else None,
            "pause_ms":         1800,
        })
    return {
        "type":            "step_sequence",
        "preamble_latex":  question_data["question_latex"],
        "steps":           steps,
        "narration_style": "concise",
    }
```

### 4.3 Frontend: MathsSimulationPlayer Component

```
src/components/workspace/shared/simulation/MathsSimulationPlayer.jsx
```

**Props:**
```ts
interface MathsSimulationPlayerProps {
  script:        SimulationScript;      // from API response
  archetypeKey:  string;
  onClose:       () => void;
  isLightPalette: boolean;
}
```

**Internal state machine:**

```
IDLE → PLAYING → PAUSED → FINISHED
         ↑           |
         └───────────┘  (replay)
```

**Rendering logic:**

```
┌─────────────────────────────────────────────────────┐
│  PREAMBLE (question, rendered with KaTeX)           │
├─────────────────────────────────────────────────────┤
│  WORKING PAD (fills in line-by-line)                │
│                                                     │
│  Step 0:  6x² + 11x + 3                [rule badge] │
│  Step 1:  = 6x² + 9x + 2x + 3         [rule badge] │
│  Step 2:  = 3x(2x + 3) + 1(2x + 3)   [rule badge] │
│  Step 3:  = (3x + 1)(2x + 3)          [rule badge] │
│                                                     │
│  [Common error callout if present]                  │
├─────────────────────────────────────────────────────┤
│  [▶ Play] [⏸ Pause] [↺ Replay] [✕ Close]           │
└─────────────────────────────────────────────────────┘
```

**Animation behaviour:**

Each step animates in with a `slide-in-from-bottom` + `fade-in` over 300 ms, then waits
`step.pause_ms` before the next step. The rule badge slides in from the right with a 100 ms delay
after the step text appears.

The common-error callout (if present) appears as a collapsible orange-bordered box below the step,
labelled "⚠ Common mistake here".

**Implementation notes:**
- Use `useEffect` + `setTimeout` to sequence steps; store `timeoutIds` in a ref for cleanup.
- `currentStepIndex` drives which steps are visible (steps 0..currentStepIndex are shown).
- KaTeX renders each `from_latex` / `to_latex` via the existing `MathText` shared component.
- The working pad should use the same font and layout as `WorkingPad` so the student recognises it.

---

## 5. Accounting Simulation

### 5.1 The Cell-Fill Sequence Schema

Accounting simulations are fundamentally different from maths: instead of a linear chain of
algebraic steps, the student must fill a **table** (journal, ledger, trial balance, etc.) with
values computed from source documents.

The `cell_fill_sequence` format represents a table and the order in which cells should be filled:

```json
{
  "type": "cell_fill_sequence",
  "preamble": "Post the following transactions to the Debtors Control account.",
  "tables": [
    {
      "table_id":    "debtors_control",
      "table_label": "Debtors Control (B120)",
      "table_type":  "general_ledger_t_account",
      "columns": ["Date", "Details", "Folio", "Amount"],
      "debit_rows":  [],
      "credit_rows": [],
      "schema_note": "T-account: debit side on left, credit side on right"
    }
  ],
  "fill_sequence": [
    {
      "seq":         1,
      "table_id":    "debtors_control",
      "side":        "debit",
      "row_index":   0,
      "col":         "Date",
      "value":       "01 Mar",
      "value_type":  "date",
      "narration":   "The opening balance date is the first day of the period.",
      "pause_ms":    1200
    },
    {
      "seq":         2,
      "table_id":    "debtors_control",
      "side":        "debit",
      "row_index":   0,
      "col":         "Details",
      "value":       "Balance b/d",
      "value_type":  "label",
      "narration":   "b/d = brought down — the balance from the previous period.",
      "pause_ms":    1000
    },
    {
      "seq":         3,
      "table_id":    "debtors_control",
      "side":        "debit",
      "row_index":   0,
      "col":         "Amount",
      "value":       "45 000",
      "value_type":  "currency",
      "narration":   "This is the opening balance from the trial balance.",
      "pause_ms":    1500
    }
    // ... continues for every cell in fill order
  ],
  "closing_narration": "Always balance the account by inserting the balance c/d on the larger side."
}
```

### 5.2 Table Type Vocabulary

The `table_type` field determines how the SimulationPlayer renders the table:

| `table_type` | Description |
|---|---|
| `general_ledger_t_account` | Classic T-account with debit/credit sides |
| `cash_receipts_journal` | Multi-column CRJ with analysis columns |
| `cash_payments_journal` | Multi-column CPJ |
| `debtors_journal` | DJ with debtor name, invoice no, amount |
| `creditors_journal` | CJ |
| `income_statement` | Vertical statement with sections |
| `balance_sheet` | Vertical or horizontal balance sheet |
| `trial_balance` | Two-column debit/credit with account list |
| `debtors_ledger_account` | Individual debtor account card |
| `creditors_ledger_account` | Individual creditor account card |

The SimulationPlayer uses `table_type` to render the correct HTML table structure before the
animation begins. The `fill_sequence` then targets cells by `(table_id, side, row_index, col)`.

### 5.3 Generator Contract (Accounting)

Each accounting generator must implement:

```python
def build_simulation_script(question_data: dict) -> dict:
    """
    Converts the generator's internal cell_map into a cell_fill_sequence.
    The cell_map is already computed at question generation time.
    This function determines the pedagogically correct fill ORDER.
    """
    tables = build_table_schemas(question_data)   # from existing cell_map
    fill_sequence = order_cells_for_simulation(
        question_data["cell_map"],
        question_data["table_type"],
    )
    return {
        "type":               "cell_fill_sequence",
        "preamble":           question_data["question_text"],
        "tables":             tables,
        "fill_sequence":      fill_sequence,
        "closing_narration":  question_data.get("closing_narration", ""),
    }

def order_cells_for_simulation(cell_map: dict, table_type: str) -> list[dict]:
    """
    Returns cells in the correct teaching order. Rules:
    - Source entries before ledger postings
    - Date → Details → Folio → Amount (always)
    - Pre-filled cells (given in question) are shown instantly; student-filled cells animate in
    - Balance c/d and balance b/d entries are always last
    """
    ...
```

### 5.4 Frontend: AccountingSimulationPlayer Component

```
src/components/workspace/shared/simulation/AccountingSimulationPlayer.jsx
```

**Rendering logic:**

```
┌──────────────────────────────────────────────────────────────┐
│  PREAMBLE (question text)                                    │
├──────────────────────────────────────────────────────────────┤
│  TABLE (rendered empty at start, cells fill in sequence)     │
│                                                              │
│  DEBTORS CONTROL (B120)                                      │
│  ┌──────────────────┬──────────────────┐                    │
│  │  Dr              │  Cr              │                    │
│  │ Date|Details|Amt │ Date|Details|Amt │                    │
│  │ ✎ filling...     │                 │                    │
│  └──────────────────┴──────────────────┘                    │
│                                                              │
│  [Narration panel — shows current cell explanation]          │
├──────────────────────────────────────────────────────────────┤
│  Step 3 of 14  ████████░░░░░░ 43%                           │
│  [▶ Play] [⏸ Pause] [↺ Replay] [✕ Close]                    │
└──────────────────────────────────────────────────────────────┘
```

**Key UX decisions:**
- Cells that are **pre-filled** (given in the question) are shown immediately with a grey
  background and no animation — they were never "student work".
- Cells that the **student must fill** animate in with a typewriter effect, one character at a
  time, using the same font as the real `InlineFillQuestionUI`.
- The narration panel updates with each new cell and fades out after 3 seconds if no new cell
  is filling.
- The virtual pointer (same concept as `HeroSimulation`) moves to each cell before typing begins.
  The pointer is an absolutely-positioned `div` with `transition: transform 400ms ease-in-out`.

---

## 6. Shared SimulationPlayer Wrapper

Both `MathsSimulationPlayer` and `AccountingSimulationPlayer` are wrapped by a common shell:

```
src/components/workspace/shared/simulation/SimulationPlayer.jsx
```

```jsx
// Decides which player to mount based on script.type
export default function SimulationPlayer({ script, archetypeKey, onClose, isLightPalette }) {
  if (script.type === 'step_sequence') {
    return <MathsSimulationPlayer {...} />;
  }
  if (script.type === 'cell_fill_sequence') {
    return <AccountingSimulationPlayer {...} />;
  }
  return <div>Simulation not available for this question type.</div>;
}
```

The shell renders as a **modal overlay** inside the workspace container (not a full-page takeover),
so the student can close it and return to their question immediately.

---

## 7. Trigger Points in the Workspace

The simulation is surfaced in two places:

### 7.1 Scaffold Mode — "Watch how this type of question works" (before attempting)

In `WorkspaceModeShell.jsx`, after the question is generated and before the student starts
filling in their answer, add a collapsible banner:

```
┌─────────────────────────────────────────────────────────┐
│ 🎬  Not sure where to start?                            │
│     Watch a worked example of this question type →      │
└─────────────────────────────────────────────────────────┘
```

Clicking opens `SimulationPlayer` as a modal. The button is only shown if the archetype has a
registered canonical seed in `SIMULATION_SEEDS`.

### 7.2 After a Failed Attempt — "Watch how this is done" (after scoring < 50%)

In `EvaluatedWorkspaceModeShell.jsx`, after marking, if the student scored below 50%:

```
┌─────────────────────────────────────────────────────────┐
│ 📽  Your score: 38% — see exactly how this is done:    │
│     [Watch worked example]  [Try another question]      │
└─────────────────────────────────────────────────────────┘
```

---

## 8. Backend API Specification

### 8.1 New Endpoint

```
GET /api/simulation/{subject}/{grade}/{topic}/{archetype}
```

**Query parameters:**
- None required (the backend determines the canonical seed from `SIMULATION_SEEDS`)

**Response (200):**
```json
{
  "canonical_seed":    42,
  "archetype_key":     "factorise_trinomial",
  "simulation_script": { ... },
  "generated_at":      "2024-03-15T09:00:00Z",
  "cache_version":     1
}
```

**Response (404):**
```json
{ "error": "No simulation registered for this archetype" }
```

**Caching:** `Cache-Control: public, max-age=86400` — safe because the canonical seed never
changes unless a developer explicitly updates `simulation_seeds.py` and bumps `cache_version`.

### 8.2 Generator Mode Flag

All generators receive an additional optional parameter:

```python
def generate(seed: int, difficulty: str, subskill: str, mode: str = "practice") -> dict:
    """
    mode="practice"    → standard question response (existing behaviour)
    mode="simulation"  → same as practice but also appends simulation_script
    """
```

---

## 9. Tabular Data Serialisation for the Pro Agent LLM

> This section is critical. It answers the question: when the Pro agent sends a student's
> accounting work to the LLM, does the LLM receive the table in its correct structural form?

### 9.1 The Problem

Accounting tables are not uniform. A Debtors Control account has different columns and semantic
meaning to a Cash Receipts Journal. A naive string representation (e.g. copy-pasting HTML) loses:
- Which cells are student-filled vs pre-given
- The semantic role of each cell (e.g. "this is the running balance")
- The relationship between rows (e.g. this row is a subtotal of the above)
- Whether the student's value is numerically wrong or only formatting wrong

### 9.2 The Serialisation Format: Semantic Cell JSON

Every table in the system is represented as a **Semantic Cell JSON** object before being included
in the LLM prompt. This is distinct from the HTML rendering and from the raw `cell_map`.

```json
{
  "table_id":    "debtors_control",
  "table_type":  "general_ledger_t_account",
  "table_label": "Debtors Control (B120)",
  "account_side_semantics": {
    "debit":  "Amounts owed TO the business (assets / increases)",
    "credit": "Amounts paid by debtors or returned (decreases)"
  },
  "rows": [
    {
      "side":        "debit",
      "row_index":   0,
      "Date":        { "value": "01 Mar",      "source": "given",    "student_value": null },
      "Details":     { "value": "Balance b/d", "source": "given",    "student_value": null },
      "Folio":       { "value": "",            "source": "given",    "student_value": null },
      "Amount":      { "value": 45000,         "source": "given",    "student_value": null }
    },
    {
      "side":        "debit",
      "row_index":   1,
      "Date":        { "value": "31 Mar",      "source": "given",    "student_value": "31 Mar" },
      "Details":     { "value": "Credit Sales","source": "given",    "student_value": "Credit Sales" },
      "Folio":       { "value": "CRJ7",        "source": "given",    "student_value": "CRJ7" },
      "Amount":      { "value": 23500,         "source": "student",  "student_value": 23050,
                       "is_correct": false, "delta": -450,
                       "hint_tag": "check_crj_subtotal" }
    }
  ],
  "totals": {
    "debit_total":  { "value": 68500, "source": "student", "student_value": 68050, "is_correct": false },
    "credit_total": { "value": 22000, "source": "student", "student_value": 22000, "is_correct": true }
  },
  "balance": {
    "closing_balance_side": "debit",
    "closing_balance":      { "value": 46500, "source": "student", "student_value": null, "is_correct": false }
  }
}
```

**Key fields:**
- `source: "given"` — this cell was pre-filled in the question; the student did not touch it.
- `source: "student"` — the student filled this cell; it is the cell being marked.
- `is_correct` — boolean from the procedure tracker; the LLM must NOT re-derive this.
- `delta` — the signed difference between correct and student value (negative = understated).
- `hint_tag` — a controlled vocabulary tag the LLM can use to anchor its explanation.

### 9.3 LLM Prompt Construction

The Pro agent constructs the LLM prompt as follows:

```python
def build_llm_prompt(question_data: dict, student_submission: dict, student_model: dict) -> str:
    """
    Builds a grounded, table-aware prompt for the Pro tutor LLM.
    """
    tables_json = serialize_tables_for_llm(question_data, student_submission)

    prompt = f"""
You are a South African high-school Accounting tutor. You are given:
1. The question the student attempted.
2. The student's submission, represented as Semantic Cell JSON tables.
3. A list of cells that are marked incorrect (pre-computed — do not re-derive marks).

Your job is to explain ONLY the first incorrect cell to the student in plain English.
Reference the cell by its table, side, and column name (e.g. "Debtors Control → Dr side → Amount row 2").
Do NOT reveal the correct value outright. Use the hint_tag to guide your explanation.
Do NOT comment on cells that are already correct.

## Question
{question_data['question_text']}

## Student Submission (Semantic Cell JSON)
{json.dumps(tables_json, indent=2)}

## First Incorrect Cell
Table: {first_error['table_label']}
Side:  {first_error['side']}
Column:{first_error['col']}
Student entered: {first_error['student_value']}
Hint tag: {first_error['hint_tag']}

Respond in 2–3 sentences. Use South African accounting terminology.
"""
    return prompt
```

### 9.4 Why Not Markdown Tables for the LLM?

Markdown tables look like this:

```
| Date   | Details      | Folio | Amount |
|--------|-------------|-------|--------|
| 01 Mar | Balance b/d |       | 45 000 |
| 31 Mar | Credit Sales| CRJ7  | 23 050 |
```

The LLM can read this, but it cannot tell:
- Whether R23 050 was entered by the student or given in the question.
- Whether R23 050 is correct.
- What the expected value is and by how much the student is off.

The Semantic Cell JSON solves all three problems without requiring the LLM to re-derive answers
(which would introduce hallucination risk).

---

## 10. Storage and Caching Strategy

| Layer | What is stored | Duration |
|---|---|---|
| **Backend response cache** (HTTP) | Full simulation response (canonical seed + script) | 24 hours (`Cache-Control: public, max-age=86400`) |
| **Frontend localStorage** | `fundile_sim_seed_{archetype_key}` — the seed the student has seen | Indefinite (invalidated on `cache_version` mismatch) |
| **Session cache** (in-memory) | The loaded `simulation_script` object for the current session | Cleared on page reload |

Pre-generation of simulation scripts (at deploy time) is a future optimisation. For now, lazy
generation on first request is sufficient.

---

## 11. File Structure

```
caps-ai-backend/
  app/
    utils/
      simulation_seeds.py              ← NEW: canonical seed registry
      simulation_builder.py            ← NEW: shared build_simulation_script logic
    routes/
      simulation.py                    ← NEW: GET /api/simulation endpoint
    utils/
      grade10/
        mathematics/
          algebraic_expressions_generator.py   ← MODIFY: add build_simulation_script()
          trigonometry_generator.py             ← MODIFY: add build_simulation_script()
        accounting/
          sole_trader_generator.py             ← MODIFY: add build_simulation_script()
          final_accounts_generator.py          ← MODIFY: add build_simulation_script()

src/
  components/
    workspace/
      shared/
        simulation/
          SimulationPlayer.jsx         ← NEW: wrapper/router
          MathsSimulationPlayer.jsx    ← NEW: step-sequence player
          AccountingSimulationPlayer.jsx ← NEW: cell-fill player
          SimulationControls.jsx       ← NEW: play/pause/replay/close bar
          useSimulation.js             ← NEW: state machine hook
          simulationApi.js             ← NEW: fetch + localStorage logic
        WorkspaceModeShell.jsx         ← MODIFY: add simulation trigger banner
        EvaluatedWorkspaceModeShell.jsx ← MODIFY: add post-failure simulation CTA
```

---

## 12. Implementation Order (Status: Layer B SimuLearn Built)

> **Implementation Note (2026-09-20):**
> Layer B SimuLearn is **built and operational**:
> - Backend service: `caps-ai-backend/app/services/simulearn_service.py` emitting ~2KB JSON declarative animation streams for canonical worked examples across Accounting (CRJ VAT), Mathematics (trinomials), Physical Sciences (Kinematics), Life Sciences (Punnett square), and Math Literacy (SARS tax).
> - Frontend player: `src/components/simulearn/SimuLearnPlayer.jsx` with full interactive playback controls, speed multipliers, and multi-modality visual stages (2D ledger tables, KaTeX formula expansions, Punnett squares).

Complete in this sequence to allow incremental testing at each stage:

### Phase 1 — Data Foundation (Backend)
1. Create `simulation_seeds.py` with the initial seed registry.
2. Add `build_simulation_script()` to **one** maths generator (start with `algebraic_expressions`).
3. Add `build_simulation_script()` to **one** accounting generator (start with `sole_trader`).
4. Create the `/api/simulation` endpoint.
5. Test that both endpoint responses are structurally valid against the schema above.

### Phase 2 — Maths Player (Frontend)
6. Create `useSimulation.js` state machine (IDLE → PLAYING → PAUSED → FINISHED).
7. Create `SimulationControls.jsx`.
8. Create `MathsSimulationPlayer.jsx` with static (non-animated) step rendering.
9. Add animation (slide-in per step, pause timing).
10. Add common-error callout rendering.
11. Wire into `WorkspaceModeShell.jsx` Scaffold mode trigger.

### Phase 3 — Accounting Player (Frontend)
12. Create `AccountingSimulationPlayer.jsx` with static table rendering (all cells filled at once).
13. Add cell-fill animation (typewriter per cell, virtual pointer movement).
14. Add narration panel.
15. Wire into `WorkspaceModeShell.jsx` and `EvaluatedWorkspaceModeShell.jsx`.

### Phase 4 — Pro Agent LLM Serialisation
16. Create `serialize_tables_for_llm()` in `app/services/pro_agent_serialiser.py`.
17. Update the Pro agent prompt builder to use Semantic Cell JSON instead of raw HTML/markdown.
18. Test with at least 3 different table types (T-account, CRJ, Income Statement).

### Phase 5 — Remaining Generators
19. Add `build_simulation_script()` to all remaining registered maths generators.
20. Add `build_simulation_script()` to all remaining registered accounting generators.
21. Populate `SIMULATION_SEEDS` for all new archetypes (requires curating good seed values).

---

## 13. Open Questions (Resolve Before Phase 1)

1. **Archetype key naming convention**: Should it match the generator's internal `subskill` key,
   or be a separate vocabulary? Recommendation: use the generator's `subskill` key directly to
   avoid a translation layer.

2. **Who curates canonical seeds?** A developer must run the generator with candidate seeds and
   inspect the output to confirm it is suitable. This is a one-time manual step per archetype.
   Consider a management command: `python manage.py audit_simulation_seed <archetype>` that prints
   the question, worked solution, and step count for a given seed.

3. **What if a student's archetype has no simulation yet?** Hide the simulation trigger entirely.
   Do not show a broken or empty state.

4. **Mobile / small screen**: The simulation modal should be full-screen on mobile. The virtual
   pointer animation should be disabled on touch devices (replace with step-highlight only).

5. **Accessibility**: All narration text must be available as static text (not only timed audio
   or animation). Add an "Read full solution" link that reveals all steps at once for screen
   reader users.

---

---

# Pro Package — AI Tutor Agent Architecture

> This section is a separate concern from the Simulation system above. The Simulation is a
> pre-recorded, canonical worked-example playback. The AI Tutor Agent is a live, interactive
> system that responds to a specific student's actual submission in real time.

---

## 14. What Kind of Agent Is This?

### 14.1 The Agent in One Sentence

The Pro package AI tutor is a **Verifier-Grounded Pedagogical Scaffold Agent** — an on-rails
conversational agent that explains pre-detected errors using curriculum-anchored knowledge,
without diagnosing, marking, or generating questions itself.

### 14.2 What That Means in Plain Language (for pitching and documentation)

> *"Fundile Pro includes an AI tutor agent that acts like a personal academic coach. After the
> student submits their work, the system's marking engine finds exactly where they went wrong.
> The agent then takes over: it guides the student to understand *why* they went wrong — not by
> giving them the answer, but through targeted questions and progressively specific hints, the
> same way a good human tutor would. The agent is strictly bound to the current topic and the
> student's curriculum. It cannot go off-topic, it cannot guess, and it never just hands over
> the correct answer."*

### 14.3 Formal Agent Taxonomy

In the AI systems literature, this agent sits at the intersection of three well-defined patterns:

| Pattern | Description | How it applies here |
|---|---|---|
| **Reactive Agent** | Responds to events in its environment | Triggered by a student submission event; receives the pre-marked result |
| **Tool-Using Agent** | Achieves goals by calling external tools | Calls: generator (for new variants), misconception library (for explanations), student model (for history) |
| **Guardrailed / On-Rails Agent** | Hard constraints prevent certain outputs | Cannot go off-topic; cannot reveal the correct answer outright; cannot generate questions itself |

Combined: it is a **Constrained Tool-Using Reactive Agent** with a **pedagogical objective function**
(maximise student understanding, not answer accuracy on this attempt).

In education technology terminology, this maps most closely to an **Intelligent Tutoring System
(ITS) dialogue agent** — specifically one that implements **Socratic scaffolding** via
**metacognitive prompting** (asking the student to explain their own reasoning before correcting it).

---

## 15. Revised Pro Agent Architecture

### 15.1 The Core Principle: Explain, Never Diagnose

The most important structural decision: **the LLM never marks work and never re-derives answers**.

```
┌──────────────────────────────────────────────────────────────────────┐
│                         STUDENT SUBMITS                              │
└──────────────────────────┬───────────────────────────────────────────┘
                           │
                 ┌─────────▼──────────┐
                 │  Procedure Tracker  │  ← deterministic, SymPy-backed
                 │  / Cell Marker      │    finds WHAT is wrong
                 └─────────┬──────────┘
                           │  error_report: { cell, error_type, misconception_tag, delta }
                 ┌─────────▼──────────┐
                 │  Student Model      │  ← classifies error pattern over history
                 └─────────┬──────────┘
                           │  context: { prior_errors, mastery_level, struggling_subskills }
                 ┌─────────▼──────────┐
                 │  Misconception      │  ← controlled vocabulary; pre-written explanation seeds
                 │  Library Lookup     │
                 └─────────┬──────────┘
                           │  misconception_entry: { title, seed_explanation, hint_sequence }
                 ┌─────────▼──────────┐
                 │  LLM (narrow task) │  ← articulates the pre-found error in natural language
                 │                    │    using the student's specific context and numbers
                 └─────────┬──────────┘
                           │
                 ┌─────────▼──────────┐
                 │  Response Builder  │  ← composes text + optional render payload
                 └─────────┬──────────┘
                           │
                           ▼
                     STUDENT SEES HINT
```

The LLM's input is tightly scoped. It receives:
- The misconception entry (pre-written, curriculum-accurate)
- The specific cell/step reference and the student's actual value
- The student's mastery level (to adjust vocabulary complexity)
- A strict output format instruction (2–3 sentences, no correct value revealed)

### 15.2 Four-Tier Progressive Hint Protocol

The agent enforces a strict escalation protocol before making any LLM call:

| Tier | Name | Source | LLM involved? | Example |
|---|---|---|---|---|
| 1 | **Structural** | Pre-written, generic | No | *"Check that your column totals balance."* |
| 2 | **Directional** | Derived from cell_map/solution_graph | No | *"Your Bank column total is overstated."* |
| 3 | **Conceptual** | Misconception library + LLM rephrasing | Yes (narrow) | *"Think about whether VAT belongs in the Bank column or in a separate analysis column."* |
| 4 | **Explanatory** | Full LLM response with misconception grounding | Yes (fuller) | Explains the concept, gives a related example, asks teach-back question |

Tiers 1 and 2 are deterministic and instant. Tier 3 uses the LLM to personalise a pre-written
explanation seed. Tier 4 is used only when the student explicitly asks for more help after Tier 3,
or has failed the same misconception type 3+ times in the student model.

### 15.3 The "Teach Back" Checkpoint

After Tier 3 or Tier 4, before the student is allowed to re-attempt, the agent asks a
comprehension question:

```
Agent: "Before you try again — in one sentence, what is the difference between
        the Bank column and the Creditors column in a CPJ?"

Student: [types response]

Agent: [LLM evaluates whether the response demonstrates understanding]
       → If yes: "Exactly right. Now try filling in row 3 again."
       → If no:  "Not quite — let me put it a different way..." [escalates explanation]
```

This is the critical difference between a hint-dispenser and a tutor. The teach-back prevents
the student from clicking through hints without understanding anything.

### 15.4 Tabular Data Serialisation — Exact Table Structure for the LLM

The LLM receives the table in **Semantic Cell JSON** built from the generator's actual output —
not a generic template. This is essential because tables differ by:

- **Grade** — Grade 10 CPJ vs Grade 11 CPJ have different analysis columns
- **Business context** — a retail CPJ vs a manufacturing CPJ vs a service business CPJ
- **Question context** — the analysis columns present depend on what expenses appear in the
  source documents for that specific question

The serialiser reads the generator's `cell_map` directly and produces:

```json
{
  "table_id":    "cpj",
  "table_label": "Cash Payments Journal (CPJ) — March 2024",
  "table_type":  "cash_payments_journal",
  "columns": [
    { "col": "Day",                "semantic": "Day of the month the payment was made" },
    { "col": "Details",            "semantic": "Name of payee or description of payment" },
    { "col": "Fol",                "semantic": "Folio reference to ledger account" },
    { "col": "Bank",               "semantic": "Total amount paid from the bank account (gross)" },
    { "col": "Creditors",          "semantic": "Payments to creditors for goods purchased on credit" },
    { "col": "Raw Materials",      "semantic": "Payments for raw materials used in production" },
    { "col": "Factory Wages",      "semantic": "Wages paid to production/factory workers" },
    { "col": "Carriage on Purchases", "semantic": "Transport costs for bringing goods to the business" }
  ],
  "rows": [ ... ]
}
```

The `semantic` description for non-standard analysis columns is generated by the generator at
question-creation time, since only the generator knows what columns it chose to include and why.

**Implementation requirement:** every generator that produces a multi-column journal must include
a `column_semantics` dict in its output, mapping each column name to a one-line description. The
serialiser merges this into the Semantic Cell JSON. This is the only generator change needed.

---

## 16. Subject Transfer Analysis

The agent architecture described above — deterministic error detection, misconception library
lookup, LLM articulation, Socratic scaffolding — transfers to all current and planned subjects,
but the error-detection mechanism varies by subject type.

### 16.1 Subject Classification

| Subject | Answer type | Error detection | Misconception library type |
|---|---|---|---|
| Mathematics | Step sequence (LaTeX/SymPy) | Procedure Tracker | Computational + conceptual rules |
| Accounting | Cell map (tabular, numeric) | Cell Marker | Double-entry + procedural rules |
| Business Studies | Keyword/concept points | Rubric Keyword Detector | Conceptual confusion tags |
| Physical Sciences — Physics | Step sequence (numeric) | Procedure Tracker | Physics law misapplication |
| Physical Sciences — Chemistry | Step sequence + conceptual | Procedure Tracker + Rubric KD | Stoichiometric + conceptual |
| Life Sciences | Diagram labels + concept points | Label Matcher + Rubric KD | Biological process confusion |
| History | Source analysis + essay points | Rubric KD (structured) | Historical reasoning errors |
| Geography | Quantitative + descriptive mix | Procedure Tracker + Rubric KD | Map/data interpretation errors |

### 16.2 Mathematics

**Transfer: Direct and immediate.**

The procedure tracker already identifies the exact step where the student's algebra diverged from
the correct path, including which SymPy transformation failed and the closest `common_error` entry.

The agent's role: *"Your factorisation in step 2 is incorrect. You split 11x into 6x + 5x, but
6×5=30 and you need the product to equal ac=18. What two numbers multiply to 18 and add to 11?"*

The misconception library for maths is rule-based: `sign_distribution_error`,
`fraction_inversion_confusion`, `wrong_trig_ratio`, `quadratic_formula_discriminant_error`, etc.
Each tag maps to a canonical explanation seed that the LLM personalises.

### 16.3 Business Studies

**Transfer: Yes, with a shift from computational to conceptual scaffolding.**

Business Studies answers are mark-point based (e.g. "1 mark for naming the factor, 1 mark for
explanation, 1 mark for application to the scenario"). The rubric keyword detector checks for
presence of required concepts, not numerical correctness.

The agent's role shifts from *"your number is wrong"* to *"you named the factor but didn't explain
how it affects the business in the scenario — that's the mark you're missing."*

Key difference: there is no single correct sentence. The misconception library here contains
**conceptual confusion tags** rather than computational rules:
- `micro_macro_confusion` — student confuses micro and macro environment factors
- `forms_of_ownership_conflation` — student applies characteristics of a company to a partnership
- `theory_without_application` — student states a fact but doesn't apply it to the case study

The teach-back checkpoint is particularly valuable in Business Studies: *"In your own words, what
is one way that the macro environment differs from the micro environment?"*

### 16.4 Physical Sciences — Physics

**Transfer: Direct (calculations); moderate (conceptual).**

Physics calculations (kinematics, electricity, waves) are step sequences — the procedure tracker
applies directly. The misconception library covers:
- `wrong_formula_selected` — used v=u+at when v²=u²+2as was needed
- `unit_conversion_omitted` — left km/h unconverted
- `vector_direction_sign_error` — treated a vector as scalar

Conceptual physics questions (describe what happens when…) are handled via the Rubric Keyword
Detector in the same way as Business Studies.

### 16.5 Physical Sciences — Chemistry

**Transfer: Strong for stoichiometry; moderate for conceptual.**

Stoichiometry, equilibrium calculations, and electrochemistry are step sequences. Misconceptions
include `molar_mass_calculation_error`, `limiting_reagent_confusion`, `le_chatelier_direction_error`.

Conceptual chemistry (bonding, properties, reactions) is Rubric KD based.

Note: chemical equations have a special constraint — **balancing** — that is deterministic and
can be checked before the procedure tracker runs. A student who submits an unbalanced equation
gets a Tier 1 structural hint immediately without the LLM being invoked at all.

### 16.6 History

**Transfer: Yes, with the richest semantic requirements.**

History is the most language-heavy subject. The agent's role here is closest to a writing coach:
- Source comprehension questions: did the student extract the right information?
- Interpretation questions: did the student identify bias, provenance, purpose?
- Essay questions: does the argument have a thesis, evidence, and a conclusion?

The rubric structure is hierarchical (comprehension → interpretation → evaluation → synthesis),
and the agent scaffolds up this hierarchy. The misconception library contains reasoning errors:
- `event_not_contextualised` — student states what happened without explaining why
- `source_not_interrogated` — student quotes the source without analysing it
- `anachronistic_interpretation` — student applies modern values to a historical context

The teach-back checkpoint is essential for History: *"Why do historians say we should consider
who wrote a source and when? Tell me in your own words."*

### 16.7 Geography

**Transfer: Fully (quantitative); strongly (qualitative).**

Map work (gradients, bearings, coordinates, cross-sections) is deterministic — procedure tracker
applies. Data analysis (climate graphs, population pyramids) has both computational steps and
interpretive descriptions.

Misconception tags include `contour_interval_misread`, `bearing_vs_direction_confusion`,
`correlation_causation_conflation` (for data interpretation questions).

### 16.8 Life Sciences

**Transfer: Strong.**

Diagram labelling (cells, organs, processes) is deterministic label-matching. Process descriptions
(photosynthesis, meiosis, digestion) are Rubric KD based.

The misconception library is rich: `mitosis_meiosis_confusion`, `light_dependent_vs_independent_reaction`,
`artery_vein_direction_error`, `hormone_vs_enzyme_conflation`.

Genetics calculations (Mendelian ratios, blood types) are step sequences — procedure tracker applies.

---

## 17. Misconception Library — Structure and Ownership

The misconception library is a **developer-curated, curriculum-anchored knowledge base** — not
LLM-generated. It is the most valuable long-term asset in the Pro package architecture.

### 17.1 File Structure

```
caps-ai-backend/
  app/
    knowledge/
      misconceptions/
        mathematics/
          grade10_algebraic_expressions.json
          grade10_trigonometry.json
          ...
        accounting/
          sole_trader.json
          final_accounts.json
          ...
        business_studies/
          forms_of_ownership.json
          business_environments.json
          ...
        physical_sciences/
          physics_mechanics.json
          chemistry_stoichiometry.json
          ...
```

### 17.2 Misconception Entry Schema

```json
{
  "tag":          "micro_macro_confusion",
  "subject":      "business_studies",
  "topic":        "business_environments",
  "title":        "Confusing micro and macro environment factors",
  "description":  "Student applies macro environment factors (PESTLE) to a question asking about the micro environment (market, suppliers, competitors) or vice versa.",
  "tier_1_hint":  "Check whether the question asks about factors the business can influence or factors it cannot control.",
  "tier_2_hint":  "The {factor_name} is a {actual_environment} environment factor, not a {stated_environment} environment factor.",
  "tier_3_seed":  "The micro environment contains factors the business can directly influence — like its customers, suppliers, and competitors. The macro environment contains forces outside the business's control — like government policy and economic conditions. Which of these describes {factor_name}?",
  "teach_back_question": "Give me one example of a micro environment factor and explain why a business can influence it.",
  "curriculum_reference": "CAPS Business Studies Grade 10 Term 1 — Business Environments"
}
```

The `tier_2_hint` and `tier_3_seed` contain `{placeholder}` slots that the agent fills from the
error report before sending to the LLM. The LLM's only job at Tier 3 is to rephrase the seed
naturally for the student's reading level.

### 17.3 Curation Responsibility

The misconception library is maintained by the development team, informed by:
1. Common errors observed in student submissions (aggregated, anonymised)
2. CAPS teacher guides and NSC examiner reports (which explicitly list common errors)
3. Expert accounting/mathematics teacher review

It is **not** auto-generated by an LLM. LLM-generated misconceptions would introduce curriculum
inaccuracies. This library is the ground truth the LLM reasons from — not a product of LLM reasoning.

---

## 18. Pro Agent Backend API Specification

### 18.1 Endpoint

```
POST /api/pro/tutor
```

This is the single entry point for all live tutor interactions. There is no separate endpoint per
hint tier — the agent internally decides which tier to deliver.

**Request body:**

```json
{
  "session_id":        "uuid",
  "student_uid":       "firebase_uid",
  "subject":           "accounting",
  "grade":             "10",
  "topic":             "sole_trader",
  "archetype":         "crj_entry",
  "question_seed":     9,
  "question_data":     { ... },          // full generator response for this question
  "submission":        { ... },          // student's cell_map or step sequence
  "marking_result":    { ... },          // pre-computed by procedure tracker / cell marker
  "interaction_type":  "hint_request",   // "hint_request" | "teach_back_response" | "new_question_request"
  "interaction_payload": {
    "current_hint_tier":    2,           // which tier they are currently at
    "teach_back_text":      null,        // populated when interaction_type = "teach_back_response"
    "student_free_text":    null         // optional typed question from the student
  }
}
```

**Response body:**

```json
{
  "response_type":   "hint",            // "hint" | "teach_back_prompt" | "new_question" | "correction"
  "hint_tier":       3,
  "text":            "Think about whether VAT belongs in the Bank column or in a separate analysis column.",
  "render": {
    "type":          "table_highlight",
    "table_id":      "crj",
    "highlight_cells": [
      { "row": 1, "col": "Bank",      "colour": "amber" },
      { "row": 1, "col": "Creditors", "colour": "green" }
    ]
  },
  "teach_back_prompt":  null,           // populated at Tier 3/4
  "suggestion_chips": [
    "Tell me more",
    "Show me an example",
    "I understand, let me try again"
  ],
  "allow_reattempt": false              // true only after teach-back passes
}
```

### 18.2 Internal Service Flow

```python
# app/services/pro_agent.py

class ProTutorAgent:

    def handle(self, request: TutorRequest) -> TutorResponse:

        # 1. Retrieve student model
        student = self.student_model.get(request.student_uid)

        # 2. Identify the first incorrect cell/step (deterministic)
        first_error = self._extract_first_error(request.marking_result)
        if not first_error:
            return self._build_correct_response(student)

        # 3. Look up misconception entry
        misconception = self.misconception_library.lookup(
            tag=first_error.misconception_tag,
            subject=request.subject,
            topic=request.topic,
        )

        # 4. Determine hint tier
        tier = self._determine_tier(
            current_tier=request.interaction_payload.current_hint_tier,
            prior_error_count=student.get_error_count(first_error.misconception_tag),
            interaction_type=request.interaction_type,
        )

        # 5. Build response (Tiers 1-2: no LLM; Tiers 3-4: LLM)
        if tier <= 2:
            return self._build_deterministic_hint(tier, first_error, misconception)
        else:
            llm_prompt = self._build_llm_prompt(tier, first_error, misconception, student, request)
            llm_text   = self.llm_provider.complete(llm_prompt)
            return self._build_llm_hint(tier, llm_text, first_error, misconception)

    def _determine_tier(self, current_tier, prior_error_count, interaction_type):
        # Escalate automatically if they have failed this misconception 3+ times historically
        if prior_error_count >= 3:
            return max(current_tier, 3)
        # Escalate one tier per hint request
        if interaction_type == "hint_request":
            return min(current_tier + 1, 4)
        return current_tier
```

### 18.3 The LLM Prompt Template

```python
TUTOR_PROMPT_TEMPLATE = """
You are a South African high-school {subject} tutor operating strictly within CAPS.

## Your Role
You MUST NOT:
- Reveal the correct answer to the student.
- Mark or re-derive the student's work.
- Discuss any topic outside of {subject} Grade {grade} — {topic}.
- Generate questions.

You MUST:
- Explain the specific error identified below in 2–3 sentences.
- Use the misconception explanation seed as your anchor — do not invent curriculum content.
- Adjust your language for a {mastery_level} student (beginner / intermediate / advanced).
- End with a single guiding question that prompts the student to think, not to calculate.

## Question Context
{question_context}

## Student's Error
Location: {error_location}
Student entered: {student_value}
Error type: {error_type}
Misconception: {misconception_title}

## Misconception Explanation Seed (your anchor — rephrase in natural language)
{misconception_seed}

## Response format
Plain text, 2–3 sentences + one guiding question. No markdown. No maths notation unless necessary.
If maths notation is needed, use plain English descriptions (e.g. "a times b" not LaTeX).
"""
```

---

## 19. Pro Agent Frontend Components

### 19.1 Component Tree

```
src/
  components/
    workspace/
      shared/
        pro-agent/
          ProTutorPanel.jsx          ← main sidebar/overlay panel
          HintDisplay.jsx            ← renders current hint text + render payload
          TableHighlightOverlay.jsx  ← highlights specific cells in the live table
          TeachBackInput.jsx         ← textarea + submit for teach-back responses
          SuggestionChips.jsx        ← clickable chip row (predefined prompts)
          useProTutor.js             ← state machine + API calls
          proTutorApi.js             ← fetch wrapper for /api/pro/tutor
```

### 19.2 ProTutorPanel Layout

```
┌─────────────────────────────────────────────────────────┐
│  🎓 Tutor                                          [×]  │
├─────────────────────────────────────────────────────────┤
│  [Hint text — rendered from agent response]            │
│                                                         │
│  [Highlighted table cell reference, if any]            │
│                                                         │
│  ─────────────────────────────────────────────────     │
│  [Teach-back input, if prompted]                       │
│  ┌──────────────────────────────────────────────┐      │
│  │ Type your explanation here...                │      │
│  └──────────────────────────────────────────────┘      │
│  [Submit]                                              │
│                                                         │
│  ─────────────────────────────────────────────────     │
│  Suggestion chips:                                     │
│  [Tell me more] [Show an example] [Try again]          │
│                                                         │
│  Hint 2 of 4  ████████░░░░ — more specific hints →    │
└─────────────────────────────────────────────────────────┘
```

The panel slides in from the right as a drawer on desktop and from the bottom as a sheet on mobile.
It does not cover the question or the student's answer input — both remain visible and interactive.

### 19.3 TableHighlightOverlay

When the agent response includes `render.type = "table_highlight"`, the overlay component applies
coloured outlines and backgrounds to specific cells in the live `InlineFillQuestionUI` or the
accounting table, using CSS custom properties set on the cell element:

```jsx
// Cells receive data attributes matching their (table_id, row, col) address
<td
  data-table-id="crj"
  data-row="1"
  data-col="Bank"
  style={{ '--highlight-colour': 'amber' }}    // set by TableHighlightOverlay
  className={highlight ? 'pro-cell-highlight' : ''}
>
```

This means **no changes are needed to the table rendering components** — the overlay reads the
`render` payload and applies `data-*` attribute lookups to find and highlight the correct cell.

### 19.4 useProTutor State Machine

```
IDLE
  │  (student submits, score < 100%)
  ▼
WAITING_FOR_HINT_REQUEST
  │  (student clicks "Get help" or chip)
  ▼
FETCHING  ──(error)──► ERROR_STATE
  │
  ▼
HINT_DISPLAYED  (tier 1 or 2 — no teach-back required)
  │  (student clicks "Try again")
  ▼
REATTEMPT_ALLOWED

HINT_DISPLAYED  (tier 3 or 4 — teach-back required)
  │  (student submits teach-back response)
  ▼
EVALUATING_TEACH_BACK
  │  (pass)                │  (fail)
  ▼                        ▼
REATTEMPT_ALLOWED      HINT_DISPLAYED (escalated)
```

---

## 20. Integration Between Simulation and Pro Agent

The Simulation (Section 1–13) and the Pro Agent (Section 14–19) are distinct systems but share
one integration point: **the agent can trigger a simulation as a response tool**.

### 20.1 When the Agent Triggers a Simulation

If:
- The student has reached Tier 4 (explanatory hint) AND
- A canonical simulation exists for this archetype AND
- The student has not yet watched the simulation for this archetype

…the agent response can include:

```json
{
  "response_type": "hint",
  "hint_tier":     4,
  "text":          "You've seen three hints now. I think it would help to watch a worked example of this exact type of question — it will show you the process step by step.",
  "render": {
    "type":           "simulation_trigger",
    "archetype_key":  "crj_entry",
    "label":          "Watch: How to complete a Cash Receipts Journal entry"
  }
}
```

The frontend's `HintDisplay` detects `render.type = "simulation_trigger"` and renders a prominent
button that opens the `SimulationPlayer` modal in-place. After the student closes the simulation,
the teach-back prompt is presented.

### 20.2 Shared Data — No Duplication

Both systems read from the same generator response. The simulation script is derived from
`question_data.solution_graph` / `question_data.cell_map`. The Pro Agent receives the same
`question_data` in its request payload. Neither system stores a separate copy of the question —
the generator response is the single source of truth.

---

## 21. Pro Agent Implementation Order

Complete the Simulation system (Sections 1–13, Phase 1–5) first. The Pro Agent shares
infrastructure (generator responses, procedure tracker output) that must be stable before
building on top of it.

### Phase 6 — Misconception Library Foundation
1. Create `app/knowledge/misconceptions/` directory structure.
2. Author initial misconception entries for **Grade 10 Accounting — Sole Trader** (target: 10–15
   well-tested entries covering the most common CRJ/CPJ errors).
3. Create `app/services/misconception_library.py` with `lookup(tag, subject, topic)`.
4. Write unit tests: given a `misconception_tag`, assert the correct entry is returned.

### Phase 7 — Pro Agent Backend Core
5. Create `app/services/pro_agent.py` with the full service flow (Section 18.2).
6. Implement Tier 1 and Tier 2 (deterministic hints only — no LLM calls yet).
7. Create the `/api/pro/tutor` endpoint.
8. Integration test: submit a known incorrect answer, assert correct Tier 1 and Tier 2 responses.

### Phase 8 — LLM Integration (Tiers 3 and 4)
9. Wire the existing `llm_provider.py` into `pro_agent.py` for Tier 3 and 4.
10. Implement the prompt template (Section 18.3).
11. Test with 3 different misconception types across accounting and maths.
12. Evaluate LLM output quality: does it rephrase the seed naturally without adding incorrect content?

### Phase 9 — Teach-Back Evaluation
13. Add `interaction_type = "teach_back_response"` handling to the agent.
14. Implement LLM-based comprehension check (narrow prompt: "Does this response demonstrate
    understanding of {concept}? Reply YES or NO with one sentence of reasoning.").
15. Connect `allow_reattempt` flag to the frontend gate.

### Phase 10 — Frontend Pro Agent Panel
16. Create `useProTutor.js` state machine.
17. Create `ProTutorPanel.jsx` with static hint display (no animation yet).
18. Create `SuggestionChips.jsx` and `TeachBackInput.jsx`.
19. Create `TableHighlightOverlay.jsx` — test with Grade 10 Accounting CRJ.
20. Wire panel into `EvaluatedWorkspaceModeShell.jsx` — shown when score < 100%.

### Phase 11 — Simulation Trigger Integration
21. Add `render.type = "simulation_trigger"` handler to `HintDisplay.jsx`.
22. Wire to `SimulationPlayer` modal open.
23. After simulation closes, emit teach-back prompt.

### Phase 12 — Expand Coverage
24. Author misconception entries for Grade 10 Maths — Algebraic Expressions (10+ entries).
25. Author misconception entries for Grade 10 Business Studies — Micro Environment (8+ entries).
26. Test end-to-end for each new subject before expanding further.

---

## 22. Open Questions for Pro Agent (Resolve Before Phase 6)

1. **Misconception tag assignment in generators**: Currently, `misconception_tags` are listed in
   the generator response but may not be linked to specific cells/steps. The error report from
   the procedure tracker must include a `misconception_tag` per error — confirm this is already
   the case or plan the schema change.

2. **Teach-back evaluation cost**: Using the LLM to evaluate teach-back responses adds latency
   and API cost. Consider a lighter-weight alternative: a keyword-matching check against the
   misconception entry's `teach_back_keywords` field (a curated list of terms that indicate
   understanding). Only escalate to LLM evaluation if keywords are absent.

3. **Student-initiated questions**: The spec allows the student to type a free-text question
   rather than only using chips. This requires a guardrail check (is the question on-topic?)
   before routing to the LLM. Define the guardrail logic and the off-topic rejection message
   before implementing the free-text input field.

4. **Concurrent sessions**: If a student has two browser tabs open (different questions), the
   student model must be write-safe. Confirm that `student_model.py` uses transactions or
   optimistic locking when updating mastery scores.

5. **Graceful degradation**: If the LLM provider is unavailable, the agent must fall back to
   Tier 2 (deterministic directional hint) silently. Do not expose LLM errors to the student.
   The fallback must be implemented before the Pro package launches.

6. **Rubric Keyword Detector (Business Studies / History)**: This component is mentioned in
   Section 16 but not yet designed in detail. It requires its own specification covering:
   - How rubric keywords are stored (alongside the generator response or in a separate file?)
   - How partial credit is handled (student mentions the concept but spells it differently)
   - How the detector's output maps to the `misconception_tag` vocabulary

7. **Privacy**: Teach-back responses are free text typed by a minor (school learner). Confirm
   that this text is not stored beyond the session or, if stored for quality monitoring, is
   handled in accordance with POPIA obligations. The privacy statement must be updated before
   the teach-back feature ships.
