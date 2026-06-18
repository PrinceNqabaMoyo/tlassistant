# Modularization Plan: `sole_trader_generator.py`

This document serves as a blueprint for refactoring the massive `sole_trader_generator.py` file into a maintainable, structured Python package. You can reference this plan when you're ready to tackle the technical debt.

## The Problem
Currently, `sole_trader_generator.py` is nearly 3,000 lines. It handles everything from basic MCQs to complex General Ledger construction. This makes it:
1. Extremely difficult to scroll through and locate specific bugs.
2. Risky to modify (changing a shared helper for a CRJ might break a DJ).
3. Hard to add new features without creating a merge conflict nightmare.

## The Goal
Convert `sole_trader_generator.py` into a folder structure (a Python package) where each distinct subskill has its own dedicated file.

## Proposed Package Architecture

Create a new directory: `caps-ai-backend/app/utils/grade10_accounting/sole_trader_generator/` and replace the single `.py` file with the following structure:

```text
sole_trader_generator/
├── __init__.py                # Exposes ONLY the main `generate_questions` function
├── router.py                  # The traffic cop. Reads the requested subskill and calls the correct submodule
├── concepts_generator.py      # Handles all MCQ, TF, Match, Word Bank, Calc, and Typeds
├── journals_cash.py           # Handles CRJ, CPJ, and Petty Cash sets
├── journals_credit.py         # Handles DJ, DAJ, CJ, and CAJ sets
├── general_ledger.py          # Handles T-Accounts, Trading Stock accounts, debits/credits
└── accounting_equation.py     # (If applicable) Assets = Equity + Liabilities logic
```

## Step-by-Step Refactoring Process

### Phase 1: Preparation & Scaffolding
1. **Create the Folder**: Make the `sole_trader_generator` folder.
2. **Move the Core File**: Move your current `sole_trader_generator.py` into this folder and rename it `legacy_generator.py`. (This ensures the code isn't deleted while you migrate).
3. **Empty Files**: Create the empty Python files listed in the architecture above.

### Phase 2: Relocating Generators (The Migration)
You will systematically cut blocks of code out of `legacy_generator.py` and paste them into their respective new files.

1. **`concepts_generator.py`**: Extract all purely conceptual functions (e.g., `_make_unified_concepts_question()`, the `fill_blank_pool`, `mcq_pool`, `tf_pool`, etc.). Update the local imports so this file points back to `...sole_trader.core`.
2. **`journals_cash.py`**: Cut all functions referring to `_st_make_crj...`, `_st_make_cpj...`, and `_st_make_pcj...` and paste them here.
3. **`journals_credit.py`**: Move all Debtors and Creditors journal functions here.
4. **`general_ledger.py`**: Move the massive blocks dealing with `_make_trading_stock_account_table` and `_build_journal_row` logic here.

### Phase 3: The Router Connection
1. In `router.py`, construct the main entry point (the function that the API route currently calls).
2. It will look something like this:
```python
from .concepts_generator import generate_concept_questions
from .journals_cash import generate_cash_journal_questions
from .journals_credit import generate_credit_journal_questions
from .general_ledger import generate_ledger_questions

def _generate_questions_internal(r, n, subskill, difficulty, mode, variant):
    if subskill == "concepts":
         return generate_concept_questions(r, n, difficulty)
    elif subskill in ["crj", "cpj", "pcj"]:
         return generate_cash_journal_questions(r, n, subskill, difficulty, mode)
    # ... etc
```

### Phase 4: Clean Up & Verification
1. Re-link `__init__.py` to export the router's `generate_questions` function.
2. Ensure the Flask routes (`app/api/accounting/grade10_sole_trader_routes.py`) are importing from the new package.
3. Delete `legacy_generator.py`.
4. Run integration tests (using PowerShell scripts simulating the generator calls) to ensure all imports cleanly resolve and questions generate perfectly.

## Why this approach?
By breaking it into distinct files, future updates become hyper-focused. If a user reports an issue with the "Creditors Allowances Journal", you don't scroll through 3,000 lines. You simply open `journals_credit.py` and immediately see the logic in a clean, 200-line file.
