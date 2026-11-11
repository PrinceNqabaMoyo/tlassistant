"""Grade 12 Mathematical Literacy - Term 1: MEASURING WEIGHT, BMI AND MEDICINE DOSAGES Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr12/Term 1/02. Measuring weight BMI medicine dosages.md
  - Via Afrika Mathematical Literacy Grade 12 (LB Pages 182-187)
  - South African National Curriculum Standards (CAPS pp. 71-73)

Features:
  - 52 distinct subskill archetypes covering:
      * Adult Body Mass Index (BMI) Calculations & Classifications (Subskills 1 to 8)
      * Child Growth Curves & BMI-for-Age Percentiles (Subskills 9 to 16)
      * Height & Weight Percentile Charts & Growth Benchmarks (Subskills 17 to 24)
      * Basal Metabolic Rate (BMR) & Ideal Body Weight Formulas (Subskills 25 to 32)
      * Pediatric Dosing Regimens & Liquid Suspensions (Subskills 33 to 40)
      * Historical Dosage Rules & Body Surface Area (BSA) Dosing (Subskills 41 to 46)
      * Clinical Dispensing, IV Flow Rates & Nutrition Calculations (Subskills 47 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Cutoff / Concentration Identification [1 Mark: Method]
      Step 2: Technical Substitution & Progressive Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Final Units [1 Mark: Accuracy]
  - Strict South African number formatting with comma decimals and space grouping (e.g. 24,5 kg/m², 12,5 mL).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr12_measuring_weight_bmi_medicine_dosages import (
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
    """Master generation entry point for Grade 12 Mathematical Literacy: Measuring Weight, BMI and Medicine Dosages."""
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
