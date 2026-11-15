"""Grade 10 Mathematics - Term 2 & 3 - Euclidean Geometry (50 Semantic Archetypes).

Curriculum sources:
- curriculum_docs_auto/Mathematics_Gr10/Term 2/04. Euclidean Geometry.md
- curriculum_docs_auto/Mathematics_Gr10/Term 3/02. Euclidean Geometry.md

Covers 50 distinct semantic archetypes across:
- Angles on lines, around points, vertically opposite, parallel lines (alt, corresp, co-int)
- Triangles: interior sum, exterior angles, isosceles/equilateral properties
- Congruence: SSS, SAS, AAS, RHS, proofs and numerical applications
- Similarity: AAA, proportion calculations
- Pythagoras theorem and converse
- Quadrilaterals: trapezium, parallelogram, rectangle, rhombus, square, kite (properties, diagonals, angle/side calculations)
- Mid-point theorem and converse
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade10_mathematics.term_2.euclidean_geometry_archetypes_01_25 import BUILDERS_01_25
from app.utils.grade10_mathematics.term_2.euclidean_geometry_archetypes_26_50 import BUILDERS_26_50

TOPIC = "grade10_math_euclidean_geometry"
LO = "math10_euclidean_geometry"

ALL_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS = list(ALL_BUILDERS.keys())
ARCHETYPES = SUBSKILLS
BUILDERS = ALL_BUILDERS

_LEGACY_ALIASES: Dict[str, str] = {
    "angle_types": "01_angle_classification_and_estimation",
    "angle_calculate": "02_adjacent_angles_on_straight_line",
    "parallel_transversal": "08_parallel_lines_alternate_interior_angles",
    "triangle_angles": "12_triangle_interior_angle_sum",
    "isosceles_base": "14_isosceles_triangle_base_angles",
    "congruency": "17_congruence_sss_condition",
    "similarity": "26_similarity_aaa_equiangular",
    "pythagoras": "31_pythagoras_hypotenuse_calculation",
    "parallelogram_props": "37_parallelogram_opposite_angles_equal",
    "special_quads": "47_quadrilateral_classification_hierarchy",
    "midpoint_theorem": "48_midpoint_theorem_segment_length",
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    base_seed = int(seed) if seed is not None else 42
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, int(count))):
        cur_seed = base_seed * 1000 + i if seed is not None else None
        rng = random.Random(cur_seed)

        resolved_subskill = subskill
        if resolved_subskill in _LEGACY_ALIASES:
            resolved_subskill = _LEGACY_ALIASES[resolved_subskill]

        if not resolved_subskill or resolved_subskill in ("mixed", "all", "default"):
            resolved_subskill = rng.choice(SUBSKILLS)
        elif resolved_subskill not in ALL_BUILDERS:
            # Fallback search
            matches = [s for s in SUBSKILLS if resolved_subskill in s]
            resolved_subskill = matches[0] if matches else rng.choice(SUBSKILLS)

        builder = ALL_BUILDERS[resolved_subskill]
        q = builder(rng)
        if seed is not None:
            q["id"] = f"{TOPIC}_{resolved_subskill}_{base_seed}_{i}"
        questions.append(q)

    return {"questions": questions}


generate_question = generate
