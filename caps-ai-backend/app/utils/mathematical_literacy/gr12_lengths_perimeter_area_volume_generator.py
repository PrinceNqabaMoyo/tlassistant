"""Grade 12 Mathematical Literacy - Term 1: MEASUREMENT (LENGTHS, PERIMETER, AREA, VOLUME & PACKAGING) Generator.

Exhaustively grounded in:
  - curriculum_source_files/Textbook_MathematicalLiteracy_Gr12_lengths-perimeter-area-and-volume.pdf
  - Via Afrika Mathematical Literacy Grade 12 (LB Pages 162-195)
  - South African National Curriculum Standards (CAPS pp. 58-62)

Features:
  - 52 distinct subskill archetypes covering:
      * Lengths, Perimeters & Boundaries (Subskills 1 to 8)
      * Areas, Paving & Tiling (Subskills 9 to 16)
      * Surface Areas, Painting & Sheeting (Subskills 17 to 24)
      * Volumes, Liquid Capacity & Fill-Time (Subskills 25 to 32)
      * Earthworks, Bulk Materials & Dam Capacities (Subskills 33 to 40)
      * Packaging, 3D Stacking & Volumetric Packing Efficiency (Subskills 41 to 46)
      * Multi-step Project Costing, Quotations & Optimization (Subskills 47 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Dimension Identification [1 Mark: Method]
      Step 2: Technical Substitution & Progressive Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Final Units [1 Mark: Accuracy]
  - Strict South African number formatting with comma decimals and space grouping (e.g. 1 250,50 m²).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr12_measurement_lengths_perimeter_area_volume import (
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
    """Master generation entry point for Grade 12 Mathematical Literacy: Measurement."""
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
