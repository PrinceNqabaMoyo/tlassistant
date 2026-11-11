"""
Grade 8 Mathematics - Geometry of Straight Lines Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/03. Geometry of straight lines.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .geometry_straight_lines_archetypes_01_25 import (
    BUILDERS_01_25,
    arch_01_angles_on_straight_line_numerical_two_angles,
    arch_02_angles_on_straight_line_three_angles,
    arch_03_perpendicular_lines_adjacent_supplementary,
    arch_04_angles_on_straight_line_algebraic_linear,
    arch_05_angles_on_straight_line_multipliers,
    arch_06_angles_on_straight_line_binomial_expressions,
    arch_07_angles_on_straight_line_three_algebraic_terms,
    arch_08_angles_on_straight_line_mixed_terms_and_constant,
    arch_09_vertically_opposite_angles_numerical,
    arch_10_vertically_opposite_angles_full_revolution,
    arch_11_vertically_opposite_angles_algebraic_one_step,
    arch_12_vertically_opposite_angles_algebraic_two_step,
    arch_13_vertically_opposite_angles_variables_both_sides,
    arch_14_intersecting_lines_perpendicular_and_opposite,
    arch_15_identifying_transversal_and_angle_pairs,
    arch_16_parallel_lines_corresponding_angles_numerical,
    arch_17_parallel_lines_alternate_interior_angles_numerical,
    arch_18_parallel_lines_cointerior_angles_numerical,
    arch_19_parallel_lines_alternate_exterior_angles_numerical,
    arch_20_parallel_lines_corresponding_angles_algebraic,
    arch_21_parallel_lines_alternate_angles_algebraic,
    arch_22_parallel_lines_cointerior_angles_algebraic,
    arch_23_parallel_lines_cointerior_multipliers,
    arch_24_parallel_lines_two_step_deduction_corresp_and_straight,
    arch_25_parallel_lines_two_step_deduction_alt_and_opposite,
)
from .geometry_straight_lines_archetypes_26_50 import (
    BUILDERS_26_50,
    arch_26_parallel_lines_three_parallel_lines,
    arch_27_parallel_lines_two_transversals,
    arch_28_proving_lines_parallel_via_corresponding_angles,
    arch_29_proving_lines_parallel_via_alternate_angles,
    arch_30_proving_lines_parallel_via_cointerior_angles,
    arch_31_angles_around_a_point_revolution,
    arch_32_angles_around_a_point_algebraic,
    arch_33_triangle_angle_sum_straight_line_proof,
    arch_34_zig_zag_parallel_lines_auxiliary_line,
    arch_35_parallel_lines_with_bisector_ray,
    arch_36_perpendicular_transversal_all_right_angles,
    arch_37_parallel_lines_with_isosceles_triangle,
    arch_38_parallel_lines_with_right_angled_triangle,
    arch_39_clock_hands_straight_line_angle,
    arch_40_rhombus_or_parallelogram_cointerior_relationship,
    arch_41_trapezium_parallel_sides_cointerior_angles,
    arch_42_diagnosing_geometric_reason_abbreviation,
    arch_43_diagnosing_cointerior_angle_fallacy,
    arch_44_diagnosing_non_parallel_transversal_fallacy,
    arch_45_complex_two_parallel_pairs_rhomboid_grid,
    arch_46_straight_line_algebraic_fractional_angles,
    arch_47_straight_line_with_decimal_angle_measures,
    arch_48_reflection_of_light_ray_straight_line,
    arch_49_surveying_compass_bearing_straight_line,
    arch_50_geometry_of_straight_lines_capstone_synthesis,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = BUILDERS_01_25 + BUILDERS_26_50

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_angles_on_straight_line_numerical_two_angles",
    "02_angles_on_straight_line_three_angles",
    "03_perpendicular_lines_adjacent_supplementary",
    "04_angles_on_straight_line_algebraic_linear",
    "05_angles_on_straight_line_multipliers",
    "06_angles_on_straight_line_binomial_expressions",
    "07_angles_on_straight_line_three_algebraic_terms",
    "08_angles_on_straight_line_mixed_terms_and_constant",
    "09_vertically_opposite_angles_numerical",
    "10_vertically_opposite_angles_full_revolution",
    # 11 - 20
    "11_vertically_opposite_angles_algebraic_one_step",
    "12_vertically_opposite_angles_algebraic_two_step",
    "13_vertically_opposite_angles_variables_both_sides",
    "14_intersecting_lines_perpendicular_and_opposite",
    "15_identifying_transversal_and_angle_pairs",
    "16_parallel_lines_corresponding_angles_numerical",
    "17_parallel_lines_alternate_interior_angles_numerical",
    "18_parallel_lines_cointerior_angles_numerical",
    "19_parallel_lines_alternate_exterior_angles_numerical",
    "20_parallel_lines_corresponding_angles_algebraic",
    # 21 - 30
    "21_parallel_lines_alternate_angles_algebraic",
    "22_parallel_lines_cointerior_angles_algebraic",
    "23_parallel_lines_cointerior_multipliers",
    "24_parallel_lines_two_step_deduction_corresp_and_straight",
    "25_parallel_lines_two_step_deduction_alt_and_opposite",
    "26_parallel_lines_three_parallel_lines",
    "27_parallel_lines_two_transversals",
    "28_proving_lines_parallel_via_corresponding_angles",
    "29_proving_lines_parallel_via_alternate_angles",
    "30_proving_lines_parallel_via_cointerior_angles",
    # 31 - 40
    "31_angles_around_a_point_revolution",
    "32_angles_around_a_point_algebraic",
    "33_triangle_angle_sum_straight_line_proof",
    "34_zig_zag_parallel_lines_auxiliary_line",
    "35_parallel_lines_with_bisector_ray",
    "36_perpendicular_transversal_all_right_angles",
    "37_parallel_lines_with_isosceles_triangle",
    "38_parallel_lines_with_right_angled_triangle",
    "39_clock_hands_straight_line_angle",
    "40_rhombus_or_parallelogram_cointerior_relationship",
    # 41 - 50
    "41_trapezium_parallel_sides_cointerior_angles",
    "42_diagnosing_geometric_reason_abbreviation",
    "43_diagnosing_cointerior_angle_fallacy",
    "44_diagnosing_non_parallel_transversal_fallacy",
    "45_complex_two_parallel_pairs_rhomboid_grid",
    "46_straight_line_algebraic_fractional_angles",
    "47_straight_line_with_decimal_angle_measures",
    "48_reflection_of_light_ray_straight_line",
    "49_surveying_compass_bearing_straight_line",
    "50_geometry_of_straight_lines_capstone_synthesis",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {}

for idx, b in enumerate(BUILDERS, start=1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

for name, b in zip(SUBSKILLS, BUILDERS):
    DISPATCH_TABLE[name] = b
    prefix = name.split("_")[0]
    DISPATCH_TABLE[prefix] = b
    short_slug = "_".join(name.split("_")[1:])
    DISPATCH_TABLE[short_slug] = b


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(count):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None

        if subskill is not None:
            sub_key = str(subskill).strip()
            if sub_key in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[sub_key]
            else:
                sub_lower = sub_key.lower()
                for k, b in DISPATCH_TABLE.items():
                    if isinstance(k, str) and (sub_lower in k.lower() or k.lower() in sub_lower):
                        builder = b
                        break

        if builder is None and archetype_index is not None:
            idx = int(archetype_index)
            if idx in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[idx]
            elif 1 <= idx <= len(BUILDERS):
                builder = BUILDERS[idx - 1]

        if builder is None:
            builder = rng.choice(BUILDERS)

        q = builder(rng)
        q.setdefault("grade", 8)
        q.setdefault("subject", "Mathematics")
        q.setdefault("topic", "Geometry of straight lines")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
