"""Grade 12 Mathematical Literacy - Term 3: INTEREST, BANKING, INFLATION Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr12/Term 3/01. interest banking inflation.md
  - Via Afrika Mathematical Literacy Grade 12 (LB Pages 102-123)
  - South African National Curriculum Standards (CAPS pp. 55-58)

Features:
  - 52 distinct subskill archetypes covering:
      * Loan Fundamentals, Deposits & Repayment Factors (Subskills 1 to 8)
      * Amortization Table Modeling & Non-Linear Curves (Subskills 9 to 16)
      * Loan Optimization: Deposits, Rates & Extra Contributions (Subskills 17 to 24)
      * Vehicle Finance & Balloon Payments (Subskills 25 to 32)
      * Investments & Retirement Annuities (Subskills 33 to 40)
      * Stokvels & Communal Savings Schemes (Subskills 41 to 46)
      * Inflation Rates, Purchasing Power & Salary Negotiations (Subskills 47 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Policy / Rate Identification [1 Mark: Method]
      Step 2: Technical Substitution & Progressive Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Financial Interpretation [1 Mark: Accuracy]
  - Strict South African currency formatting (e.g. R 7 850,94, R 1 884 225,60) and comma decimals (e.g. 11,5%).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr12_interest_banking_inflation import (
    SUBSKILL_DISPATCH,
    SUBSKILL_LIST,
    SUBSKILL_METADATA,
    generate_subskill,
)

SUBSKILLS = [item[0] for item in SUBSKILL_LIST]
DISPATCH_TABLE = SUBSKILL_DISPATCH
SUBSKILLS_METADATA = SUBSKILL_METADATA


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 12 Mathematical Literacy: Interest, Banking, Inflation."""
    r = random.Random(seed)
    results: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        chosen_subskill = subskill

        if not chosen_subskill and archetype_index is not None:
            if 0 <= archetype_index < len(SUBSKILLS):
                chosen_subskill = SUBSKILLS[archetype_index]
            else:
                chosen_subskill = SUBSKILLS[archetype_index % len(SUBSKILLS)]

        if not chosen_subskill or chosen_subskill not in DISPATCH_TABLE:
            chosen_subskill = r.choice(SUBSKILLS)

        gen_fn = DISPATCH_TABLE[chosen_subskill]
        item = gen_fn(r)
        results.append(item)

    return results


def get_subskills() -> List[str]:
    """Return the list of all 52 supported subskill keys."""
    return list(SUBSKILLS)
