"""Grade 11 Mathematics — Term 4 — Statistics: Summaries, Ogive Curves & Dispersion.
Central 50-Archetype Generator adhering to the 6-Pillar Generator Contract.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 4: Chapter 10 Statistics).

Subskills:
  01–25: Mean, Median (odd/even), Mode, Range, Quartiles (Q1, Q3), Interquartile Range (IQR), Semi-IQR,
         Five-number summary, Outlier fences (1,5*IQR), Box-and-whisker diagrams (inline_svg),
         Skewness classification, Parallel box plots, Constant transformations (+k, *k), Combined means, Stem-and-leaf.
  26–50: Deviations from mean, Variance, Standard deviation, One and two SD intervals, Consistency comparisons,
         Grouped frequency tables (midpoints, estimated mean, modal class), Cumulative frequency tables,
         Ogive curves (inline_svg: grounding, total N, median, quartiles, IQR, percentiles, thresholds),
         Histograms & Frequency polygons (inline_svg), Linear transformations (y = ax + b), and Diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade11_mathematics.statistics_summary_ogive_archetypes_01_25 import (
    ARCHETYPES_01_25,
)
from app.utils.grade11_mathematics.statistics_summary_ogive_archetypes_26_50 import (
    ARCHETYPES_26_50,
)

TOPIC = "Statistics"
TOPIC_ID = "grade11_math_statistics"

# Combine 50 semantic subskills
ARCHETYPES: Dict[str, Any] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

SUBSKILLS = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS = list(SUBSKILLS)
AVAILABLE_SUBSKILLS = list(SUBSKILLS)

# Backward-compatible legacy builder shims
LEGACY_BUILDERS: Dict[str, Any] = {
    "compound": ARCHETYPES["43_ogive_estimate_quartiles_and_iqr_svg"],
    "statistics_summary_ogive_compound": ARCHETYPES["43_ogive_estimate_quartiles_and_iqr_svg"],
    "elementary_five_number_summary": ARCHETYPES["13_complete_five_number_summary"],
    "elementary_iqr_outlier": ARCHETYPES["15_identify_outliers_using_iqr_rule"],
    "elementary_skewness_analysis": ARCHETYPES["17_box_and_whisker_skewness_classification_svg"],
}

BUILDERS: Dict[str, Any] = {
    **ARCHETYPES,
}


def get_subskills() -> List[str]:
    """Return the list of all 50 semantic subskills."""
    return list(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic question for a subskill."""
    r = random.Random(seed if seed is not None else 42)
    target = subskill or r.choice(SUBSKILLS)

    builder = BUILDERS.get(target) or LEGACY_BUILDERS.get(target)
    if not builder:
        builder = ARCHETYPES.get(r.choice(SUBSKILLS))

    try:
        q = builder(r)
    except TypeError:
        q = builder(r, difficulty=difficulty)

    if seed is not None:
        q["seed"] = seed
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Primary generator interface required by central generator registry and validation suite."""
    base_seed = 42 if seed is None else int(seed)
    chosen_target = subskill or mode

    questions = []
    for i in range(max(1, count)):
        curr_seed = base_seed * 1000 + i
        r = random.Random(curr_seed)

        target = chosen_target
        if not target or (target not in BUILDERS and target not in LEGACY_BUILDERS):
            target = SUBSKILLS[i % len(SUBSKILLS)]

        builder = BUILDERS.get(target) or LEGACY_BUILDERS.get(target)
        if not builder:
            builder = ARCHETYPES.get(SUBSKILLS[0])

        try:
            q = builder(r)
        except TypeError:
            q = builder(r, difficulty=difficulty)

        q["seed"] = curr_seed
        questions.append(q)

    return {"questions": questions}
