"""Grade 11 Mathematical Literacy - Term 2/3: MAPS Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr11/Term 2/02. MAPS.md
  - curriculum_docs_auto/MathematicalLiteracy_Gr11/Term 3/01. MAPS.md
  - curriculum_source_files/Textbook_MathematicalLiteracy_Gr11_MAPS.pdf
  - South African National Curriculum Standards (CAPS)

Features:
  - 52 distinct subskill archetypes covering:
      * Scales, Conversions & Map Distance Calculations (Subskills 1 to 9)
      * Compass Directions, Grid References & Bearings (Subskills 10 to 18)
      * Travel Time, Average Speed & Fuel Consumption (Subskills 19 to 27)
      * Distance Tables, Strip Maps, Toll Plazas & Route Analysis (Subskills 28 to 36)
      * Topographical Maps, Contour Lines, Gradients & Profiles (Subskills 37 to 44)
      * Seating Plans, Stadiums, Building Layouts & Complex Route Navigation (Subskills 45 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Definition / Identification [1 Mark: Method]
      Step 2: Technical Substitution & Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Units [1 Mark: Accuracy]
  - Strict South African Rand formatting with 2 decimal places where currency is involved (e.g. R 1 250,00).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr11_maps import DISPATCH_TABLE, SUBSKILLS


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 11 Mathematical Literacy: Maps."""
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
        item["subskill"] = chosen_subskill
        results.append(item)

    return results
