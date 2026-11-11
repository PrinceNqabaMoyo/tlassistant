"""
Grade 7 Mathematics - Construction of Geometric Figures Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/03. Construction of geometric figures.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .construction_archetypes_01_25 import (
    arch_01_identifying_arms_and_vertex,
    arch_02_correct_three_letter_naming,
    arch_03_arm_length_misconception_check,
    arch_04_clock_face_one_hour_angle,
    arch_05_clock_face_angles_at_exact_hours,
    arch_06_clock_face_reflex_angle_at_hour,
    arch_07_fractions_of_a_revolution,
    arch_08_supplementary_angles_on_straight_line,
    arch_09_classify_angle_by_degree,
    arch_10_calculate_reflex_angle_from_interior,
    arch_11_protractor_scale_selection_concept,
    arch_12_read_acute_angle_on_protractor,
    arch_13_read_obtuse_angle_on_protractor,
    arch_14_angle_not_aligned_with_zero,
    arch_15_benchmarking_angle_estimation,
    arch_16_complementary_angles,
    arch_17_definitions_circle_parts,
    arch_18_radius_diameter_relationship,
    arch_19_setting_compass_width_on_ruler,
    arch_20_radius_from_decimal_diameter,
    arch_21_concentric_circles_definition,
    arch_22_touching_circles_centre_distance,
    arch_23_longest_chord_is_diameter,
    arch_24_concentric_ring_width,
    arch_25_circles_along_a_line,
)

from .construction_archetypes_26_50 import (
    arch_26_circle_construction_steps,
    arch_27_perpendicular_bisector_steps,
    arch_28_midpoint_calculation_from_bisector,
    arch_29_angle_bisector_steps,
    arch_30_construct_sixty_degree_angle,
    arch_31_construct_thirty_degree_angle,
    arch_32_construct_ninety_degree_angle,
    arch_33_construct_forty_five_degree_angle,
    arch_34_perpendicular_from_external_point,
    arch_35_equilateral_triangle_construction,
    arch_36_isosceles_triangle_construction,
    arch_37_scalene_triangle_sss_construction,
    arch_38_triangle_inequality_theorem,
    arch_39_construct_triangle_sas,
    arch_40_construct_triangle_asa,
    arch_41_regular_hexagon_in_circle,
    arch_42_seven_circle_flower_pattern,
    arch_43_parallel_lines_ruler_and_set_square,
    arch_44_parallel_lines_compass_rhombus_method,
    arch_45_distance_between_parallel_lines,
    arch_46_perpendicular_lines_right_angle_identification,
    arch_47_tangent_perpendicular_to_radius,
    arch_48_true_false_geometric_constructions,
    arch_49_flawed_construction_diagnosis,
    arch_50_compass_opening_for_intersections,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 08: Angle Concepts & Clock Face Angles
    arch_01_identifying_arms_and_vertex,
    arch_02_correct_three_letter_naming,
    arch_03_arm_length_misconception_check,
    arch_04_clock_face_one_hour_angle,
    arch_05_clock_face_angles_at_exact_hours,
    arch_06_clock_face_reflex_angle_at_hour,
    arch_07_fractions_of_a_revolution,
    arch_08_supplementary_angles_on_straight_line,
    # 09 - 16: Classification & Protractor Reading
    arch_09_classify_angle_by_degree,
    arch_10_calculate_reflex_angle_from_interior,
    arch_11_protractor_scale_selection_concept,
    arch_12_read_acute_angle_on_protractor,
    arch_13_read_obtuse_angle_on_protractor,
    arch_14_angle_not_aligned_with_zero,
    arch_15_benchmarking_angle_estimation,
    arch_16_complementary_angles,
    # 17 - 25: Circle Terminology, Radius & Diameter
    arch_17_definitions_circle_parts,
    arch_18_radius_diameter_relationship,
    arch_19_setting_compass_width_on_ruler,
    arch_20_radius_from_decimal_diameter,
    arch_21_concentric_circles_definition,
    arch_22_touching_circles_centre_distance,
    arch_23_longest_chord_is_diameter,
    arch_24_concentric_ring_width,
    arch_25_circles_along_a_line,
    # 26 - 34: Compass Bisectors & Standard Angles
    arch_26_circle_construction_steps,
    arch_27_perpendicular_bisector_steps,
    arch_28_midpoint_calculation_from_bisector,
    arch_29_angle_bisector_steps,
    arch_30_construct_sixty_degree_angle,
    arch_31_construct_thirty_degree_angle,
    arch_32_construct_ninety_degree_angle,
    arch_33_construct_forty_five_degree_angle,
    arch_34_perpendicular_from_external_point,
    # 35 - 42: Triangle & Polygon Constructions
    arch_35_equilateral_triangle_construction,
    arch_36_isosceles_triangle_construction,
    arch_37_scalene_triangle_sss_construction,
    arch_38_triangle_inequality_theorem,
    arch_39_construct_triangle_sas,
    arch_40_construct_triangle_asa,
    arch_41_regular_hexagon_in_circle,
    arch_42_seven_circle_flower_pattern,
    # 43 - 50: Parallel Lines, Tangents & Diagnosis
    arch_43_parallel_lines_ruler_and_set_square,
    arch_44_parallel_lines_compass_rhombus_method,
    arch_45_distance_between_parallel_lines,
    arch_46_perpendicular_lines_right_angle_identification,
    arch_47_tangent_perpendicular_to_radius,
    arch_48_true_false_geometric_constructions,
    arch_49_flawed_construction_diagnosis,
    arch_50_compass_opening_for_intersections,
]

SUBSKILLS: List[str] = [
    # 01 - 08
    "01_identifying_arms_and_vertex",
    "02_correct_three_letter_naming",
    "03_arm_length_misconception_check",
    "04_clock_face_one_hour_angle",
    "05_clock_face_angles_at_exact_hours",
    "06_clock_face_reflex_angle_at_hour",
    "07_fractions_of_a_revolution",
    "08_supplementary_angles_on_straight_line",
    # 09 - 16
    "09_classify_angle_by_degree",
    "10_calculate_reflex_angle_from_interior",
    "11_protractor_scale_selection_concept",
    "12_read_acute_angle_on_protractor",
    "13_read_obtuse_angle_on_protractor",
    "14_angle_not_aligned_with_zero",
    "15_benchmarking_angle_estimation",
    "16_complementary_angles",
    # 17 - 25
    "17_definitions_circle_parts",
    "18_radius_diameter_relationship",
    "19_setting_compass_width_on_ruler",
    "20_radius_from_decimal_diameter",
    "21_concentric_circles_definition",
    "22_touching_circles_centre_distance",
    "23_longest_chord_is_diameter",
    "24_concentric_ring_width",
    "25_circles_along_a_line",
    # 26 - 34
    "26_circle_construction_steps",
    "27_perpendicular_bisector_steps",
    "28_midpoint_calculation_from_bisector",
    "29_angle_bisector_steps",
    "30_construct_sixty_degree_angle",
    "31_construct_thirty_degree_angle",
    "32_construct_ninety_degree_angle",
    "33_construct_forty_five_degree_angle",
    "34_perpendicular_from_external_point",
    # 35 - 42
    "35_equilateral_triangle_construction",
    "36_isosceles_triangle_construction",
    "37_scalene_triangle_sss_construction",
    "38_triangle_inequality_theorem",
    "39_construct_triangle_sas",
    "40_construct_triangle_asa",
    "41_regular_hexagon_in_circle",
    "42_seven_circle_flower_pattern",
    # 43 - 50
    "43_parallel_lines_ruler_and_set_square",
    "44_parallel_lines_compass_rhombus_method",
    "45_distance_between_parallel_lines",
    "46_perpendicular_lines_right_angle_identification",
    "47_tangent_perpendicular_to_radius",
    "48_true_false_geometric_constructions",
    "49_flawed_construction_diagnosis",
    "50_compass_opening_for_intersections",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["compass_circles"] = arch_26_circle_construction_steps
DISPATCH_TABLE["perpendicular_bisector"] = arch_27_perpendicular_bisector_steps
DISPATCH_TABLE["angle_bisector"] = arch_29_angle_bisector_steps
DISPATCH_TABLE["equilateral_triangle"] = arch_35_equilateral_triangle_construction
DISPATCH_TABLE["parallel_lines"] = arch_43_parallel_lines_ruler_and_set_square


def get_subskills() -> List[str]:
    """Returns the list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Construction of Geometric Figures Generator.
    Supports exact archetype dispatch via subskill or archetype_index, and compound mode.
    """
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
        q.setdefault("grade", 7)
        q.setdefault("subject", "Mathematics")
        q.setdefault("topic", "Construction of geometric figures")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
