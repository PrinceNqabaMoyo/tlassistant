"""Grade 12 Mathematical Literacy - Term 1: EXCHANGE RATES Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr12/Term 1/01. exchange rates.md
  - Via Afrika Mathematical Literacy Grade 12 (LB Pages 240-249)
  - South African National Curriculum Standards (CAPS p. 60)

Features:
  - 52 distinct subskill archetypes covering:
      * Foreign Exchange Tables & Rate Conventions (Subskills 1 to 8)
      * Bank Selling Rate (BSR) Foreign Currency Purchases (Subskills 9 to 16)
      * Bank Buying Rate (BBR) Conversions (Subskills 17 to 24)
      * Bank Transaction Fees & Commission Structures (Subskills 25 to 32)
      * Fixed ZAR Budget, Banknote Denominations & Change (Subskills 33 to 40)
      * Cross-Rates & Multi-Currency International Travel (Subskills 41 to 46)
      * Purchasing Power Parity (PPP), Inflation & Economic Impacts (Subskills 47 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Rate Identification [1 Mark: Method]
      Step 2: Technical Substitution & Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Units [1 Mark: Accuracy]
  - Strict South African Rand formatting with 2 decimal places (e.g. R 2 682,30).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr12_exchange_rates import BUILDERS, DISPATCH_TABLE, SUBSKILLS


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 12 Mathematical Literacy: Exchange Rates."""
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
