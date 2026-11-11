"""Grade 11 Mathematical Literacy - Term 1: FINANCE (TAXATION AND UIF) Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr11/Term 1/02. FINANCE (TAXATION AND UIF).md
  - curriculum_source_files/Textbook_MathematicalLiteracy_Gr11_FINANCE-(TAXATION AND UIF).pdf
  - South African National Curriculum Standards (CAPS)

Features:
  - 52 distinct subskill archetypes covering:
      * Unemployment Insurance Fund (UIF) calculations & caps (Subskills 1 to 9)
      * Gross income, payroll deductions & net salary (Subskills 10 to 18)
      * SARS progressive income tax brackets & PAYE (Subskills 19 to 27)
      * Tax rebates, medical tax credits & net PAYE (Subskills 28 to 36)
      * Value Added Tax (VAT) 15% standard, zero-rated & vendor accounting (Subskills 37 to 44)
      * Payslip audits, fiscal drag, salary restructuring & real-world scenarios (Subskills 45 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Conceptual Reasoning & Identification
      Step 2: Technical Method & Working Setup [1 Mark: Method – ...]
      Step 3: Calculation & Final Formulation [1 Mark: Accuracy – ...]
  - Strict South African Rand formatting with 2 decimal places (e.g. R 1 250,00).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr11_finance_tax import DISPATCH_TABLE, SUBSKILLS


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 11 Mathematical Literacy: Finance (Taxation and UIF)."""
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
