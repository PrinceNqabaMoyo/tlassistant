"""Grade 12 Mathematics — Bivariate Statistics & Regression (50-Archetype Generator).
Grounded in curriculum_docs_auto/Mathematics_Gr12/Term 3/01. Statistics.md.
Covers official South African National Curriculum Standards (NSC Paper 2, Question 1: 15–20 marks).
Zero-LLM: 100% deterministic SymPy calculations with South African comma decimals ({,}) and inline SVG diagram specs.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade12_mathematics.bivariate_statistics_archetypes_01_25 import (
    ARCHETYPES_01_25,
)
from app.utils.grade12_mathematics.bivariate_statistics_archetypes_26_50 import (
    ARCHETYPES_26_50,
    classify_correlation,
)

TOPIC = "grade12_math_bivariate_statistics"
LO = "math12_statistics"

ARCHETYPES: Dict[str, Any] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(SUBSKILLS)

LEGACY_BUILDERS: Dict[str, Any] = {
    "compound": ARCHETYPES["50_comprehensive_bivariate_regression_synthesis"],
    "bivariate_regression": ARCHETYPES["50_comprehensive_bivariate_regression_synthesis"],
    "bivariate_regression_compound": ARCHETYPES["50_comprehensive_bivariate_regression_synthesis"],
    "elementary_mean_points": ARCHETYPES["27_mean_point_centroid_of_bivariate_data"],
    "mean_points": ARCHETYPES["27_mean_point_centroid_of_bivariate_data"],
    "elementary_correlation_interpretation": ARCHETYPES["34_correlation_strength_and_direction_classification"],
    "correlation_interpretation": ARCHETYPES["34_correlation_strength_and_direction_classification"],
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
    difficulty: str = "hard",
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic Grade 12 Statistics question."""
    r = random.Random(seed if seed is not None else 42)
    target = subskill or (mode if mode in BUILDERS or mode in LEGACY_BUILDERS else r.choice(SUBSKILLS))
    builder = BUILDERS.get(target) or LEGACY_BUILDERS.get(target) or ARCHETYPES[r.choice(SUBSKILLS)]
    try:
        q = builder(r)
    except TypeError:
        q = builder(r, difficulty=difficulty)
    if seed is not None:
        q["seed"] = seed
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Bivariate Statistics & Regression questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_target = subskill if (subskill and subskill != "mixed") else (mode if mode in BUILDERS else None)

    questions = []
    for i in range(max(1, count)):
        curr_seed = base_seed * 1000 + i
        r = random.Random(curr_seed)
        target = chosen_target
        if not target or (target not in BUILDERS and target not in LEGACY_BUILDERS):
            target = SUBSKILLS[i % len(SUBSKILLS)] if count > 1 else r.choice(SUBSKILLS)
        builder = BUILDERS.get(target) or LEGACY_BUILDERS.get(target) or ARCHETYPES[SUBSKILLS[0]]
        try:
            q = builder(r)
        except TypeError:
            q = builder(r, difficulty=difficulty)
        q["seed"] = curr_seed
        questions.append(q)

    return {"questions": questions}


def generate_questions(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Legacy helper returning a flat list of questions."""
    return generate(subskill=subskill, difficulty=difficulty, count=count, seed=seed, **kwargs).get("questions", [])
