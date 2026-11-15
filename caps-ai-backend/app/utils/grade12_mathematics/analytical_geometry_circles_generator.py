"""
Grade 12 Mathematics — Analytical Geometry: Circles Generator
=============================================================
100% Aligned with South African National Curriculum Standards (Grade 12 Term 2).
Grounded in curriculum_docs_auto/Mathematics_Gr12/Term 2/02. Analytical geometry.md.
Covers 50 distinct semantic subskill archetypes across origin circles, standard
and general expanded circle equations, completing the square, transformations,
tangents to circles, inclination angles, secant lines and chords, relative
position of two circles, ellipses, and multi-part exam synthesis.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade12_mathematics.analytical_geometry_circles_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade12_mathematics.analytical_geometry_circles_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "Analytical geometry"
TOPIC_ID = "grade12_math_analytical_geometry_circles"

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

ARCHETYPES: Dict[str, Callable[[random.Random], Dict[str, Any]]] = dict(BUILDERS)
ORDERED_SUBSKILLS: List[str] = list(BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)
_SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "50_multi_part_circle_tangent_exam_synthesis",
    "elementary_completing_square_radius": "14_complete_square_even_coefficients",
    "elementary_tangent_line_eq": "28_tangent_equation_to_shifted_circle",
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Analytical Geometry (Circles) questions."""
    base_seed = 42 if seed is None else int(seed)
    questions: List[Dict[str, Any]] = []

    target = subskill or mode
    resolved = LEGACY_ALIASES.get(str(target or ""), target)

    for i in range(max(1, count)):
        item_seed = base_seed + i * 17
        r = random.Random(item_seed)
        if resolved in BUILDERS:
            chosen = resolved
        else:
            chosen = ORDERED_SUBSKILLS[i % len(ORDERED_SUBSKILLS)] if count > 1 else r.choice(ORDERED_SUBSKILLS)
        q = BUILDERS[chosen](r)
        q["seed"] = item_seed
        q["difficulty"] = difficulty or q.get("difficulty", "medium")
        q["term"] = 2
        q["caps_weight_percent"] = 25
        q.setdefault("question", q.get("prompt", ""))
        q.setdefault("question_text", q.get("prompt", ""))
        q.setdefault("correct_answer", q.get("answer_latex", ""))
        q.setdefault("explanation", q.get("worked_solution", ""))
        questions.append(q)

    return {"questions": questions}
