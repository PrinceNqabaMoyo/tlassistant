"""Grade 10 Mathematics — Term 1 & 2 — Trigonometry Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr10/Term 1/05. Trigonometry 1.md and 05. Trigonometry 2.md
Focus: Trigonometric ratios in right triangles, reciprocal ratios, special angles, calculator evaluations,
Cartesian plane (CAST rule, x, y, r), trigonometric equations, and 2D practical problems (elevation & depression).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .trigonometry_archetypes_01_25 import BUILDERS_01_25
from .trigonometry_archetypes_26_50 import BUILDERS_26_50

TOPIC = "grade10_math_trigonometry"
LO = "math10_trigonometry"

ALL_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS = list(ALL_BUILDERS.keys())
ARCHETYPES = SUBSKILLS
BUILDERS = ALL_BUILDERS

# Legacy alias mappings for backwards compatibility
LEGACY_MAP: Dict[str, str] = {
    "identify_sides": "01_identify_hypotenuse_opposite_adjacent_svg",
    "ratio_from_triangle": "02_sin_ratio_definition_from_triangle_svg",
    "calculator_value": "16_calculator_evaluate_direct_sin_cos_tan",
    "special_angles": "09_special_angle_30_exact_values",
    "find_length": "22_right_triangle_calculate_opposite_side_given_hypotenuse_svg",
    "find_angle": "19_calculator_solve_acute_angle_inverse_sin",
    "solve_equation": "26_solve_trig_equation_basic_sin_acute",
    "concepts": "01_identify_hypotenuse_opposite_adjacent_svg",
    "calculation": "02_sin_ratio_definition_from_triangle_svg",
    "calculations": "02_sin_ratio_definition_from_triangle_svg",
    "trig": "02_sin_ratio_definition_from_triangle_svg",
    "trigonometry": "02_sin_ratio_definition_from_triangle_svg",
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
        if resolved_subskill in LEGACY_MAP:
            resolved_subskill = LEGACY_MAP[resolved_subskill]

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
