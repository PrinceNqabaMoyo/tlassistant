"""Grade 8 Mathematics — Construction of Geometric Figures Generator.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 3/01. Construction of geometric figures.md

Expanded to 50 distinct semantic archetypes covering:
  - Compass and ruler constructions: perpendicular bisector, angle bisector, perpendicular at/from points.
  - Special angles without protractor: 60°, 30°, 90°, 45°, 75°, 105°, 120°, 135°, 150°.
  - Triangle constructions: SSS, SAS, ASA, RHS, triangle inequality, equilateral, isosceles, medians, altitudes.
  - Centers of triangles: incenter, circumcenter, inscribed and circumscribed circles.
  - Quadrilaterals: parallelogram, rhombus, rectangle, square, kite, trapezium.
  - Advanced & applied: dividing line segments, regular hexagons, scale drawings, loci, error analysis.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .construction_archetypes_01_25 import (
    arch_01_perpendicular_bisector_line_segment_steps,
    arch_02_perpendicular_bisector_equidistant_property,
    arch_03_perpendicular_line_at_point_on_line,
    arch_04_perpendicular_line_from_external_point_to_line,
    arch_05_angle_bisector_construction_steps,
    arch_06_angle_bisector_calculate_halved_angles,
    arch_07_construct_60_degree_angle_without_protractor,
    arch_08_construct_30_degree_angle_by_bisecting_60,
    arch_09_construct_90_degree_angle_using_perpendicular,
    arch_10_construct_45_degree_angle_by_bisecting_90,
    arch_11_construct_75_degree_angle_composite,
    arch_12_construct_105_degree_angle_composite,
    arch_13_construct_120_degree_angle_double_arc,
    arch_14_construct_135_degree_angle_composite,
    arch_15_construct_150_degree_angle_composite,
    arch_16_triangle_inequality_theorem_existence,
    arch_17_construct_triangle_sss_condition,
    arch_18_construct_triangle_sas_condition,
    arch_19_construct_triangle_asa_condition,
    arch_20_construct_triangle_rhs_condition,
    arch_21_identify_construction_arcs_in_diagram,
    arch_22_construct_equilateral_triangle_given_one_side,
    arch_23_construct_isosceles_triangle_given_base_and_equal_sides,
    arch_24_construct_median_of_a_triangle,
    arch_25_construct_altitude_of_a_triangle,
)
from .construction_archetypes_26_50 import (
    arch_26_construct_angle_bisectors_incenter,
    arch_27_construct_perpendicular_bisectors_circumcenter,
    arch_28_construct_parallelogram_given_two_sides_and_angle,
    arch_29_construct_rhombus_given_side_and_angle,
    arch_30_construct_rhombus_given_diagonals,
    arch_31_construct_rectangle_given_length_and_breadth,
    arch_32_construct_square_given_side_length,
    arch_33_construct_kite_given_sides_and_diagonal,
    arch_34_construct_trapezium_given_parallel_bases_and_height,
    arch_35_ruler_and_compass_safety_and_accuracy_rules,
    arch_36_measure_and_verify_angles_with_protractor,
    arch_37_measure_and_verify_segments_with_ruler,
    arch_38_parallel_line_construction_alternate_angle_method,
    arch_39_copy_given_angle_construction_steps,
    arch_40_divide_line_segment_into_n_equal_parts,
    arch_41_circumscribed_circle_about_triangle,
    arch_42_inscribed_circle_inside_triangle,
    arch_43_regular_hexagon_inscribed_in_circle,
    arch_44_scale_drawing_interpretation_and_ratio,
    arch_45_scale_drawing_construct_plan_dimensions,
    arch_46_congruency_verification_through_construction,
    arch_47_error_analysis_identifying_flawed_construction_step,
    arch_48_composite_construction_house_gable_profile,
    arch_49_geometric_locus_points_equidistant_from_two_lines,
    arch_50_geometric_locus_points_equidistant_from_two_points,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_perpendicular_bisector_line_segment_steps": arch_01_perpendicular_bisector_line_segment_steps,
    "02_perpendicular_bisector_equidistant_property": arch_02_perpendicular_bisector_equidistant_property,
    "03_perpendicular_line_at_point_on_line": arch_03_perpendicular_line_at_point_on_line,
    "04_perpendicular_line_from_external_point_to_line": arch_04_perpendicular_line_from_external_point_to_line,
    "05_angle_bisector_construction_steps": arch_05_angle_bisector_construction_steps,
    "06_angle_bisector_calculate_halved_angles": arch_06_angle_bisector_calculate_halved_angles,
    "07_construct_60_degree_angle_without_protractor": arch_07_construct_60_degree_angle_without_protractor,
    "08_construct_30_degree_angle_by_bisecting_60": arch_08_construct_30_degree_angle_by_bisecting_60,
    "09_construct_90_degree_angle_using_perpendicular": arch_09_construct_90_degree_angle_using_perpendicular,
    "10_construct_45_degree_angle_by_bisecting_90": arch_10_construct_45_degree_angle_by_bisecting_90,
    "11_construct_75_degree_angle_composite": arch_11_construct_75_degree_angle_composite,
    "12_construct_105_degree_angle_composite": arch_12_construct_105_degree_angle_composite,
    "13_construct_120_degree_angle_double_arc": arch_13_construct_120_degree_angle_double_arc,
    "14_construct_135_degree_angle_composite": arch_14_construct_135_degree_angle_composite,
    "15_construct_150_degree_angle_composite": arch_15_construct_150_degree_angle_composite,
    "16_triangle_inequality_theorem_existence": arch_16_triangle_inequality_theorem_existence,
    "17_construct_triangle_sss_condition": arch_17_construct_triangle_sss_condition,
    "18_construct_triangle_sas_condition": arch_18_construct_triangle_sas_condition,
    "19_construct_triangle_asa_condition": arch_19_construct_triangle_asa_condition,
    "20_construct_triangle_rhs_condition": arch_20_construct_triangle_rhs_condition,
    "21_identify_construction_arcs_in_diagram": arch_21_identify_construction_arcs_in_diagram,
    "22_construct_equilateral_triangle_given_one_side": arch_22_construct_equilateral_triangle_given_one_side,
    "23_construct_isosceles_triangle_given_base_and_equal_sides": arch_23_construct_isosceles_triangle_given_base_and_equal_sides,
    "24_construct_median_of_a_triangle": arch_24_construct_median_of_a_triangle,
    "25_construct_altitude_of_a_triangle": arch_25_construct_altitude_of_a_triangle,
    "26_construct_angle_bisectors_incenter": arch_26_construct_angle_bisectors_incenter,
    "27_construct_perpendicular_bisectors_circumcenter": arch_27_construct_perpendicular_bisectors_circumcenter,
    "28_construct_parallelogram_given_two_sides_and_angle": arch_28_construct_parallelogram_given_two_sides_and_angle,
    "29_construct_rhombus_given_side_and_angle": arch_29_construct_rhombus_given_side_and_angle,
    "30_construct_rhombus_given_diagonals": arch_30_construct_rhombus_given_diagonals,
    "31_construct_rectangle_given_length_and_breadth": arch_31_construct_rectangle_given_length_and_breadth,
    "32_construct_square_given_side_length": arch_32_construct_square_given_side_length,
    "33_construct_kite_given_sides_and_diagonal": arch_33_construct_kite_given_sides_and_diagonal,
    "34_construct_trapezium_given_parallel_bases_and_height": arch_34_construct_trapezium_given_parallel_bases_and_height,
    "35_ruler_and_compass_safety_and_accuracy_rules": arch_35_ruler_and_compass_safety_and_accuracy_rules,
    "36_measure_and_verify_angles_with_protractor": arch_36_measure_and_verify_angles_with_protractor,
    "37_measure_and_verify_segments_with_ruler": arch_37_measure_and_verify_segments_with_ruler,
    "38_parallel_line_construction_alternate_angle_method": arch_38_parallel_line_construction_alternate_angle_method,
    "39_copy_given_angle_construction_steps": arch_39_copy_given_angle_construction_steps,
    "40_divide_line_segment_into_n_equal_parts": arch_40_divide_line_segment_into_n_equal_parts,
    "41_circumscribed_circle_about_triangle": arch_41_circumscribed_circle_about_triangle,
    "42_inscribed_circle_inside_triangle": arch_42_inscribed_circle_inside_triangle,
    "43_regular_hexagon_inscribed_in_circle": arch_43_regular_hexagon_inscribed_in_circle,
    "44_scale_drawing_interpretation_and_ratio": arch_44_scale_drawing_interpretation_and_ratio,
    "45_scale_drawing_construct_plan_dimensions": arch_45_scale_drawing_construct_plan_dimensions,
    "46_congruency_verification_through_construction": arch_46_congruency_verification_through_construction,
    "47_error_analysis_identifying_flawed_construction_step": arch_47_error_analysis_identifying_flawed_construction_step,
    "48_composite_construction_house_gable_profile": arch_48_composite_construction_house_gable_profile,
    "49_geometric_locus_points_equidistant_from_two_lines": arch_49_geometric_locus_points_equidistant_from_two_lines,
    "50_geometric_locus_points_equidistant_from_two_points": arch_50_geometric_locus_points_equidistant_from_two_points,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())


def generate_grade8_construction_of_geometric_figures_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    target_subskill = subskill
    if not target_subskill or target_subskill not in ARCHETYPE_MAP:
        if mode and mode.startswith("elementary_"):
            candidate = mode[len("elementary_"):]
            if candidate in ARCHETYPE_MAP:
                target_subskill = candidate
            else:
                for k in ARCHETYPE_MAP:
                    if candidate in k:
                        target_subskill = k
                        break

    if not target_subskill or target_subskill not in ARCHETYPE_MAP:
        target_subskill = rng.choice(SUBSKILLS)

    generator_fn = ARCHETYPE_MAP[target_subskill]
    q_data = generator_fn(rng)

    q_data["subject"] = "mathematics"
    q_data["grade"] = "grade-8"
    q_data["topic"] = "Construction of geometric figures"
    q_data["term"] = 3
    q_data["caps_weight_percent"] = 10
    q_data["suggested_duration_mins"] = 3
    q_data["difficulty"] = difficulty
    q_data["mode"] = mode
    q_data["subskill"] = target_subskill

    if "marking_schema" not in q_data:
        m = q_data.get("marks", 2)
        q_data["marking_schema"] = {
            "total_marks": m,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification of construction properties or setup", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct calculation, property deduction, or construction step", "marks": m - 1, "editable": True},
            ],
            "deductions": [{"rule": "incorrect_reason_or_step", "penalty": 1}],
            "carry_forward_rule": "consequential_accuracy",
        }

    return q_data


generate = generate_grade8_construction_of_geometric_figures_question
generate_grade8_construction_question = generate_grade8_construction_of_geometric_figures_question
