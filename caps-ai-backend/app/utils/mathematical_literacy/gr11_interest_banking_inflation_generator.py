"""Grade 11 Mathematical Literacy - Term 1: INTEREST, BANKING AND INFLATION Generator.

Exhaustively grounded in:
  - curriculum_source_files/Textbook_MathematicalLiteracy_Gr11_Interest-banking-and-inflation.pdf
  - South African National Curriculum Standards (CAPS)

Features:
  - 52 distinct subskill archetypes covering:
      * Simple Interest & Linear Investment Growth (Subskills 1 to 9)
      * Compound Interest & Multi-Period Growth (Subskills 10 to 18)
      * Bank Accounts & Fee Structures (Subskills 19 to 27)
      * Hire Purchase (HP) Agreements (Subskills 28 to 36)
      * Personal Loans & Credit Agreements (Subskills 37 to 44)
      * Inflation, CPI & Purchasing Power (Subskills 45 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Concept Identification [1 Mark: Method]
      Step 2: Technical Substitution & Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Units [1 Mark: Accuracy]
  - Strict South African Rand formatting with 2 decimal places (e.g. R 1 250,00).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr11_interest_banking_inflation import DISPATCH_TABLE, SUBSKILLS


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 11 Mathematical Literacy: Interest, Banking and Inflation."""
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
