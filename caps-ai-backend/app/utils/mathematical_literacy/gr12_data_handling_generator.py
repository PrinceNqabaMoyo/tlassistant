"""Grade 12 Mathematical Literacy - Term 2: DATA HANDLING Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr12/Term 2/02. Data handling.md
  - Via Afrika Mathematical Literacy Grade 12 (LB Pages 62-93)
  - South African National Curriculum Standards (CAPS pp. 83-87)

Features:
  - 52 distinct subskill archetypes covering:
      * Sampling Methods, Questionnaire Design & Bias Detection (Subskills 1 to 8)
      * Grouped Data, Class Intervals & Ogives (Subskills 9 to 16)
      * Measures of Central Tendency & Outlier Impact (Subskills 17 to 24)
      * Measures of Spread, Quartiles & Percentiles (Subskills 25 to 32)
      * Box-and-Whisker Plots, Five-Number Summary & Skewness (Subskills 33 to 40)
      * Scatter Plots, Trend Lines & Correlation (Subskills 41 to 46)
      * Section 3 CAPS: Opposing Arguments & Misleading Statistics (Subskills 47 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Concept / Class Boundary Identification [1 Mark: Method]
      Step 2: Technical Substitution & Progressive Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Statistical Interpretation [1 Mark: Accuracy]
  - Strict South African number formatting with comma decimals and space grouping (e.g. 59,3%, R 350 000, 1 200).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr12_data_handling import (
    SUBSKILL_DISPATCH,
    SUBSKILL_LIST,
    SUBSKILL_METADATA,
    generate_subskill,
)

SUBSKILLS = [item[0] for item in SUBSKILL_LIST]
DISPATCH_TABLE = SUBSKILL_DISPATCH
SUBSKILLS_METADATA = SUBSKILL_METADATA


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 12 Mathematical Literacy: Data Handling."""
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
