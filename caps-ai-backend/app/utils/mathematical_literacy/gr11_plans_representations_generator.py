"""Grade 11 Mathematical Literacy - Term 1: PLANS AND OTHER REPRESENTATIONS Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr11/Term 1/01. PLANS AND OTHER REPRESENTATIONS.md
  - curriculum_source_files/Textbook_MathematicalLiteracy_Gr11_PLANS-AND-OTHER-REPRESENTATIONS.pdf
  - South African National Curriculum Standards (CAPS)

Features:
  - 52 distinct subskill archetypes covering:
      * Floor Plans, Symbols, Dimensions & Area (Subskills 1 to 9)
      * Elevation Plans, Cardinal Directions & Solar Orientation (Subskills 10 to 18)
      * Design Drawings, Assembly Instructions & Cutting Lists (Subskills 19 to 27)
      * Scaled Drawing Calculations, Scale Selection & Rescaling (Subskills 28 to 36)
      * 2D Nets, Folding, Opposite Faces & 3D Packaging Models (Subskills 37 to 44)
      * Packaging Arrangements, Space Utilization & Pallet Loading (Subskills 45 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Concept / Identification [1 Mark: Method]
      Step 2: Technical Substitution & Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Units [1 Mark: Accuracy]
  - Strict South African Rand formatting with 2 decimal places where currency is involved (e.g. R 1 250,00).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
  - Standardized diagram_spec payloads for floor plans, elevation compasses, bar scales, and 2D nets.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr11_plans_representations import DISPATCH_TABLE, SUBSKILLS


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 11 Mathematical Literacy: Plans and Other Representations."""
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

DEFAULT_DIAGRAM_ROLE = 'context'
# All diagrams emitted by this generator specify diagram_role: "context" | "identify"
