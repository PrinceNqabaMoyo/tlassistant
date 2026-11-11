"""Grade 11 Mathematical Literacy - Term 1: CONVERSIONS AND TIME Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr11/Term 1/01. CONVERSIONS AND TIME.md
  - curriculum_source_files/Textbook_MathematicalLiteracy_Gr11_CONVERSIONS-AND-TIME.pdf
  - South African National Curriculum Standards (CAPS)

Features:
  - 52 distinct subskill archetypes covering:
      * Metric & Imperial Mass conversions (Subskills 1 to 9)
      * Metric & Imperial Length and Speed conversions (Subskills 10 to 18)
      * Volume & Domestic Cooking conversions (Subskills 19 to 27)
      * Temperature & Compound Rates (Subskills 28 to 36)
      * Time Formats & Elapsed Time Calculations (Subskills 37 to 44)
      * Time Zones, Flight Schedules & Timetable Analysis (Subskills 45 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Factor Identification [1 Mark: Method]
      Step 2: Technical Substitution & Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Units [1 Mark: Accuracy]
  - Strict South African number formatting (comma decimal, space thousands).
  - Explicit non-standard conversion factors in prompts.
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr11_conversions_time import DISPATCH_TABLE, SUBSKILLS


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 11 Mathematical Literacy: Conversions and Time."""
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


def get_subskills() -> List[str]:
    """Return all 52 supported subskill keys in curriculum sequence."""
    return list(SUBSKILLS)
