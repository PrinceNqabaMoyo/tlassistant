"""Grade 12 Mathematical Literacy - Term 1: INCOME TAX Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr12/Term 1/01. Income tax.md
  - Via Afrika Mathematical Literacy Grade 12 (LB Pages 216-235)
  - South African National Curriculum Standards (CAPS p. 59)

Features:
  - 52 distinct subskill archetypes covering:
      * Tax Foundations & Taxable Income Determination (Subskills 1 to 8)
      * SARS Tax Brackets & Marginal Rate Mechanics (Subskills 9 to 16)
      * SARS Tax Rebates & Age Groups (Subskills 17 to 24)
      * Tax Thresholds & Effective Tax Rates (Subskills 25 to 32)
      * Medical Scheme Fees Tax Credits (MTC) (Subskills 33 to 40)
      * Payslip Take-Home Pay & Salary Increase (Subskills 41 to 46)
      * IRP5 Tax Forms, Assessments & Refunds (Subskills 47 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Bracket / Rebate Identification [1 Mark: Method]
      Step 2: Technical Substitution & Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Units [1 Mark: Accuracy]
  - Strict South African Rand formatting with 2 decimal places (e.g. R 24 500,00).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr12_income_tax import BUILDERS, DISPATCH_TABLE, SUBSKILLS


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 12 Mathematical Literacy: Income Tax."""
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
    """Return all 52 supported subskill keys in curriculum sequence."""
    return list(SUBSKILLS)
