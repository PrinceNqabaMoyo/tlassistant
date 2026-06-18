# Grade 10 Accounting (Sole Trader) — Implementation Summary & Manual UI Verification Checklist

## Scope

This document describes what has been implemented for **Grade 10 Accounting (Sole Trader workspace)** and provides **manual UI checks** to verify scaffold/practice generation and marking end-to-end.

## Where the implementation lives

### Backend (caps-ai-backend)

- `app/utils/grade10_sole_trader_generator.py`
  - Main deterministic generator for Grade 10 Sole Trader.
  - Generates structured question payloads with:
    - `journals` / `journal`
    - `correct_map`
    - `cell_hints` (scaffold mode only)
    - deterministic behavior via `random.Random` seeded input

- `app/api/accounting/grade10_sole_trader_routes.py`
  - Flask route for Grade 10 Sole Trader question generation.
  - Supports request `seed` (so the same seed yields the same generated question).

- `app/utils/backups/`
  - Manual backups of `grade10_sole_trader_generator.py` created during milestones.

### Frontend (Vite app)

- `src/components/workspace/grade10/accounting/sole-trader/controller.js`
  - Adds seed state:
    - `scaffoldSeed`
    - `practiceSeed`
  - Includes `seed` in request bodies for scaffold/practice fetches.

- `src/components/workspace/grade10/Grade10AccountingSoleTraderScaffold.jsx`
  - Scaffold mode UI.
  - Seed input shown only in dev mode.

- `src/components/workspace/grade10/Grade10AccountingSoleTraderPractice.jsx`
  - Practice mode UI.
  - Seed input shown only in dev mode.

- `src/components/workspace/workspaceRegistry.js`
  - Wires controller props into scaffold/practice components.

## Grade 10 generator capabilities (backend)

### Determinism (seed support)

- Generator accepts a deterministic `random.Random` instance.
- API route accepts a `seed` so you can reproduce a specific question.

### Question type: Accounting equation / transaction analysis

- Output format: a single journal-style table question (question_type `journal`).
- Supports multiple schemas (table variants) and hybrid mixing with compatibility rules.

#### Implemented schemas

- `activity23`
- `activity24`
- `gl_amount_aol`
- `gl_aol`
- `source_gl_amount_aol`
- `journal_gl_amount_aol`
- `internal_gl_amount_aol`
- `gl_subledger_amount_aol`
  - Includes nested header rows (`header_rows`) to render grouped column headings.
- `reason_effect`

### Marking data

- `correct_map` contains the correct value for each cell in the generated table.
- Cell IDs are prefixed and stable:
  - `t0_r{row}_c{col}` for transaction analysis tables.

### Modes

- **Scaffold mode**:
  - Shows answers in the table.
  - Includes `cell_hints` for guided learning.

- **Practice mode**:
  - Does not display answers.
  - Still includes full `correct_map` so the UI can mark submissions.

### Hybrid mixing and compatibility filtering

- The generator mixes templates across archetype sets.
- Compatibility rules ensure:
  - If the schema needs `source`, templates must have it.
  - If the schema needs `journal`, templates must have it.
  - If the schema needs `internal`, templates must have it.
  - If the schema needs `subledger`, templates must have it.
  - If the schema includes `amount`, templates must have `amount`.

### Multi-row / calculation patterns

The generator supports multi-row transactions where a single real-world transaction needs multiple accounting entries. Examples:

- Sales + Cost of Sales
- Debtor settlement with discount allowed
- Creditor payment with discount received
- Insolvent debtor dividend received + write-off of the balance
- Bank fee breakdown (multiple fees + overdraft interest)
- Fixed deposit maturity (principal + interest)
- Cash withdrawal for wages (bank to cash, then wages expense)

### Bank “unfavourable” (overdraft) variants

- Treats overdraft as a liability (Liabilities increase when bank is overdrawn).
- Patterns include:
  - debtor settlements into an unfavourable bank
  - overdraft interest
  - payments where bank is unfavourable (e.g., packing materials)

### Added transaction pattern helpers (not exhaustive)

The following helpers were added/confirmed as part of the coverage work:

- `_make_bank_fee_breakdown`
- `_make_fixed_deposit_maturity`
- `_make_fixed_deposit_investment`
- `_make_interest_on_current_account`
- `_make_overdraft_interest`
- `_make_owner_withdrawal`
- `_make_owner_taking_stock`
- `_make_petty_cash_imprest_restoration`
- `_make_fee_income_on_credit`
- `_make_insolvent_debtor_dividend_writeoff`

Plus the remaining “coverage matrix” missing patterns:

- `_make_vehicle_purchase_on_credit`
- `_make_cash_handling_fee`
- `_make_cash_withdrawal_for_wages`
- `_make_packing_materials_unfavourable`
- `_make_postage_paid`

## Manual UI Verification Checklist

Use the checklist below after running backend + frontend locally.

### 0) Basic smoke: Grade 10 workspace loads

- **Open Grade 10 Accounting → Sole Trader workspace**.
- **Expected**:
  - UI loads without console errors.
  - You can switch between scaffold and practice.

### 1) Scaffold mode: new example renders correctly

- Click **New Example**.
- **Expected**:
  - A table renders with column headers.
  - Rows are present.
  - Answers are visible (scaffold).
  - Hints appear (scaffold).

### 2) Practice mode: new practice set renders correctly

- Switch to **Practice**.
- Click **New Practice Set**.
- **Expected**:
  - A table renders with column headers.
  - Rows are present.
  - Cells expected to be filled by the learner are blank.
  - You can enter answers and submit/check.

### 3) Determinism: same seed yields the same question

(DEV mode only; seed input is hidden in production.)

- In **Scaffold**:
  - Enter a seed (e.g., `123`) and click **New Example** twice.
  - **Expected**:
    - Same headers, same transactions, same values.

- In **Practice**:
  - Enter a seed (e.g., `123`) and click **New Practice Set** twice.
  - **Expected**:
    - Same generated set.

### 4) Marking: correct_map aligns with rendered table

- In **Practice**, fill a few cells with deliberately wrong values and submit/check.
- **Expected**:
  - Incorrect cells are flagged.
  - Correct cells are marked correct.

### 5) Multi-row transaction rendering + marking

You must see at least one multi-row transaction in a few attempts (or with a seed you know produces one).

- **Expected**:
  - Two (or more) consecutive rows belong to one transaction.
  - The second row uses an empty `nr` in generator data but should still appear as a row.
  - Marking works row-by-row.

Recommended multi-row patterns to confirm:

- **Sales + Cost of Sales**
- **Debtor settlement discount allowed**
- **Insolvent debtor dividend + write-off**
- **Fixed deposit maturity: principal + interest**
- **Bank fee breakdown: service fee + cash handling + overdraft interest**
- **Cash withdrawal for wages: bank→cash then wages expense**

### 6) Multi-value cell acceptance (if present)

Some archetypes can show combined values in a single cell (example: `+Amt/-Amt`).

- **Expected**:
  - The UI accepts the expected format.
  - Marking matches the exact expected value for that schema.

### 7) Unfavourable bank behavior (overdraft treated as liability)

- Generate a question that includes an unfavourable bank transaction.
- **Expected**:
  - The A/O/L effects reflect overdraft logic:
    - Receipts reduce Liabilities (overdraft decreases)
    - Fees/interest increase Liabilities (overdraft increases)

Patterns to confirm:

- overdraft interest
- packing materials paid when bank is unfavourable
- debtor settlement into unfavourable bank

### 8) Schema variety and nested headers (gl_subledger_amount_aol)

- Generate multiple scaffold examples.
- **Expected**:
  - Sometimes you see the `gl_subledger_amount_aol` format.
  - The table has grouped header rows (General Ledger / Subsidiary Ledger / Equation).

### 9) Regression check: no “empty table” questions

- Generate 10–20 questions across both modes.
- **Expected**:
  - No case where:
    - headers are empty
    - rows are empty
    - `correct_map` doesn’t match `rows × headers`

## CLI smoke tests (backend)

Run from `caps-ai-backend`:

### Multi-seed basic check

```powershell
python -c "import random; from app.utils.grade10_sole_trader_generator import generate_questions; seeds=[1,2,3,4,5,123,999]; 
for s in seeds:
  r=random.Random(s);
  q=generate_questions(r=r,n=1,subskill='equation',difficulty='easy',mode='scaffold')[0];
  j=q.get('journal') or {};
  headers=j.get('headers') or [];
  rows=j.get('rows') or [];
  cm=q.get('correct_map') or {};
  ch=q.get('cell_hints') or {};
  expected=len(headers)*len(rows);
  ok=(q.get('question_type')=='journal' and len(headers)>0 and len(rows)>0 and len(cm)==expected and len(ch)>0);
  print(s, 'ok='+str(ok), 'rows='+str(len(rows)), 'cm='+str(len(cm)), 'hints='+str(len(ch)))"
```

### Compile check

```powershell
python -m compileall app\utils\grade10_sole_trader_generator.py
```

## Notes / Known constraints

- Debug seed inputs are shown only in dev builds (`import.meta.env.DEV`).
- Some patterns may not appear frequently due to random sampling; use seeds to force reproduction.
