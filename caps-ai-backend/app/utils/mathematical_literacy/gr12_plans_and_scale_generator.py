"""Grade 12 Mathematical Literacy - Term 2: PLANS AND SCALE Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr12/Term 2/01. plans and scale.md
  - Via Afrika Mathematical Literacy Grade 12 (LB Pages 254-263)
  - South African National Curriculum Standards (CAPS pp. 73, 76-78)

Features:
  - 52 distinct subskill archetypes covering:
      * Determining Number Scales & Conversions (Subskills 1 to 8)
      * Bar Scale Construction & Conversion (Subskills 9 to 16)
      * Elevation Plans & Multi-View Projections (Subskills 17 to 24)
      * Architectural Floor Plans, Symbols & SANS Compliance (Subskills 25 to 32)
      * Site Plans, Boundaries & Municipal Bylaws (Subskills 33 to 40)
      * Cross-Sectional Technical Details (Subskills 41 to 46)
      * Material Takeoffs & Construction Costing (Subskills 47 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Scale / Ratio Identification [1 Mark: Method]
      Step 2: Technical Substitution & Progressive Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Dimension Unit Statement [1 Mark: Accuracy]
  - Strict South African number formatting with comma decimals and space grouping (e.g. 1 200 mm, R 450,00, 15,5 cm).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr12_plans_and_scale import (
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
    """Master generation entry point for Grade 12 Mathematical Literacy: Plans and Scale."""
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
