"""Grade 12 Mathematical Literacy - Term 1: SCALE AND MAP WORK Generator.

Exhaustively grounded in:
  - curriculum_source_files/Textbook_MathematicalLiteracy_Gr12_scale-and-map-work.pdf
  - curriculum_docs_auto/MathematicalLiteracy_Gr12/Term 1/01. scale and map work.md
  - Via Afrika Mathematical Literacy Grade 12 (LB Pages 128-145)
  - South African National Curriculum Standards (CAPS pp. 73-75)

Features:
  - 52 distinct subskill archetypes covering:
      * Number Scale Calculations & Conversions (Subskills 1 to 8)
      * Strip Road Maps & Distance Matrix Charts (Subskills 9 to 16)
      * Vehicle Operating Costs — AA Rate Tables (Subskills 17 to 24)
      * Route Costing, Toll Plazas & Multi-Modal Travel (Subskills 25 to 32)
      * Fuel Consumption & Vehicle Range Planning (Subskills 33 to 40)
      * Compass Directions, Bearings & Elevation Views (Subskills 41 to 46)
      * Comprehensive Journey Plans, Multi-Stop Logistics & Itineraries (Subskills 47 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Scale / Table Factor Identification [1 Mark: Method]
      Step 2: Technical Substitution & Progressive Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Final Units [1 Mark: Accuracy]
  - Strict South African number formatting with comma decimals and space grouping (e.g. 1 400 km, R 4,20/km).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr12_scale_and_map_work import (
    BUILDERS,
    DISPATCH_TABLE,
    SUBSKILLS,
    SUBSKILLS_METADATA,
)


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 12 Mathematical Literacy: Scale and Map Work."""
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
