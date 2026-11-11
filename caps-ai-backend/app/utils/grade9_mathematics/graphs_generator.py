"""Grade 9 Mathematics - Graphs & Linear Functions Generator (50 Semantic Archetypes).
=====================================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 2 Topic 2: Graphs & Linear Functions
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/02. Graphs.md
  - Chapter 15: Interpreting graphs, rates of change, gradient m, intercepts, y = mx + c,
    parallel & perpendicular lines, points of intersection, real-world models

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from .graphs_archetypes_01_25 import (
    arch_01_identify_linear_vs_non_linear_from_graph,
    arch_02_identify_increasing_decreasing_constant_intervals,
    arch_03_read_coordinates_from_cartesian_plane,
    arch_04_determine_quadrant_of_point,
    arch_05_distinguish_discrete_vs_continuous_graph,
    arch_06_interpret_maximum_minimum_turning_points_context,
    arch_07_interpret_constant_speed_from_distance_time_graph,
    arch_08_calculate_gradient_positive_integer_from_points,
    arch_09_calculate_gradient_negative_integer_from_points,
    arch_10_calculate_gradient_fractional_slope_from_points,
    arch_11_calculate_gradient_from_graph_slope_triangle,
    arch_12_determine_gradient_horizontal_line_zero,
    arch_13_determine_gradient_vertical_line_undefined,
    arch_14_compare_steepness_of_two_lines,
    arch_15_find_y_intercept_from_equation,
    arch_16_find_x_intercept_from_equation,
    arch_17_read_x_and_y_intercepts_from_graph,
    arch_18_dual_intercept_method_sketch_matching,
    arch_19_dual_intercept_equation_from_both_intercepts,
    arch_20_convert_general_form_to_standard_form,
    arch_21_equation_from_gradient_and_y_intercept,
    arch_22_equation_from_gradient_and_point_positive_m,
    arch_23_equation_from_gradient_and_point_negative_m,
    arch_24_horizontal_line_equation_through_point,
    arch_25_vertical_line_equation_through_point,
)
from .graphs_archetypes_26_50 import (
    arch_26_equation_from_two_points_positive_slope,
    arch_27_equation_from_two_points_negative_slope,
    arch_28_equation_from_two_points_fractional_gradient,
    arch_29_determine_equation_from_plotted_line_graph,
    arch_30_point_lies_on_line_test_collinearity,
    arch_31_find_missing_coordinate_on_line,
    arch_32_find_distance_between_two_axis_intercepts,
    arch_33_identify_parallel_lines_from_equations,
    arch_34_equation_of_parallel_line_through_given_point,
    arch_35_identify_perpendicular_lines_from_equations,
    arch_36_determine_perpendicular_gradient,
    arch_37_equation_of_perpendicular_line_through_given_point,
    arch_38_parallel_and_perpendicular_geometric_classification,
    arch_39_point_of_intersection_from_graph,
    arch_40_solve_point_of_intersection_algebraically_integer,
    arch_41_intersection_of_line_with_horizontal_or_vertical_line,
    arch_42_area_of_triangle_formed_by_line_and_axes,
    arch_43_rate_of_change_water_tank_filling,
    arch_44_rate_of_change_water_tank_draining,
    arch_45_distance_time_graph_average_speed_calculation,
    arch_46_distance_time_graph_multi_stage_journey,
    arch_47_cellphone_tariff_or_taxi_fare_comparison,
    arch_48_business_break_even_income_vs_expenses,
    arch_49_error_analysis_inverted_gradient_formula,
    arch_50_compound_multi_step_graph_analysis,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_identify_linear_vs_non_linear_from_graph": arch_01_identify_linear_vs_non_linear_from_graph,
    "02_identify_increasing_decreasing_constant_intervals": arch_02_identify_increasing_decreasing_constant_intervals,
    "03_read_coordinates_from_cartesian_plane": arch_03_read_coordinates_from_cartesian_plane,
    "04_determine_quadrant_of_point": arch_04_determine_quadrant_of_point,
    "05_distinguish_discrete_vs_continuous_graph": arch_05_distinguish_discrete_vs_continuous_graph,
    "06_interpret_maximum_minimum_turning_points_context": arch_06_interpret_maximum_minimum_turning_points_context,
    "07_interpret_constant_speed_from_distance_time_graph": arch_07_interpret_constant_speed_from_distance_time_graph,
    "08_calculate_gradient_positive_integer_from_points": arch_08_calculate_gradient_positive_integer_from_points,
    "09_calculate_gradient_negative_integer_from_points": arch_09_calculate_gradient_negative_integer_from_points,
    "10_calculate_gradient_fractional_slope_from_points": arch_10_calculate_gradient_fractional_slope_from_points,
    "11_calculate_gradient_from_graph_slope_triangle": arch_11_calculate_gradient_from_graph_slope_triangle,
    "12_determine_gradient_horizontal_line_zero": arch_12_determine_gradient_horizontal_line_zero,
    "13_determine_gradient_vertical_line_undefined": arch_13_determine_gradient_vertical_line_undefined,
    "14_compare_steepness_of_two_lines": arch_14_compare_steepness_of_two_lines,
    "15_find_y_intercept_from_equation": arch_15_find_y_intercept_from_equation,
    "16_find_x_intercept_from_equation": arch_16_find_x_intercept_from_equation,
    "17_read_x_and_y_intercepts_from_graph": arch_17_read_x_and_y_intercepts_from_graph,
    "18_dual_intercept_method_sketch_matching": arch_18_dual_intercept_method_sketch_matching,
    "19_dual_intercept_equation_from_both_intercepts": arch_19_dual_intercept_equation_from_both_intercepts,
    "20_convert_general_form_to_standard_form": arch_20_convert_general_form_to_standard_form,
    "21_equation_from_gradient_and_y_intercept": arch_21_equation_from_gradient_and_y_intercept,
    "22_equation_from_gradient_and_point_positive_m": arch_22_equation_from_gradient_and_point_positive_m,
    "23_equation_from_gradient_and_point_negative_m": arch_23_equation_from_gradient_and_point_negative_m,
    "24_horizontal_line_equation_through_point": arch_24_horizontal_line_equation_through_point,
    "25_vertical_line_equation_through_point": arch_25_vertical_line_equation_through_point,
    "26_equation_from_two_points_positive_slope": arch_26_equation_from_two_points_positive_slope,
    "27_equation_from_two_points_negative_slope": arch_27_equation_from_two_points_negative_slope,
    "28_equation_from_two_points_fractional_gradient": arch_28_equation_from_two_points_fractional_gradient,
    "29_determine_equation_from_plotted_line_graph": arch_29_determine_equation_from_plotted_line_graph,
    "30_point_lies_on_line_test_collinearity": arch_30_point_lies_on_line_test_collinearity,
    "31_find_missing_coordinate_on_line": arch_31_find_missing_coordinate_on_line,
    "32_find_distance_between_two_axis_intercepts": arch_32_find_distance_between_two_axis_intercepts,
    "33_identify_parallel_lines_from_equations": arch_33_identify_parallel_lines_from_equations,
    "34_equation_of_parallel_line_through_given_point": arch_34_equation_of_parallel_line_through_given_point,
    "35_identify_perpendicular_lines_from_equations": arch_35_identify_perpendicular_lines_from_equations,
    "36_determine_perpendicular_gradient": arch_36_determine_perpendicular_gradient,
    "37_equation_of_perpendicular_line_through_given_point": arch_37_equation_of_perpendicular_line_through_given_point,
    "38_parallel_and_perpendicular_geometric_classification": arch_38_parallel_and_perpendicular_geometric_classification,
    "39_point_of_intersection_from_graph": arch_39_point_of_intersection_from_graph,
    "40_solve_point_of_intersection_algebraically_integer": arch_40_solve_point_of_intersection_algebraically_integer,
    "41_intersection_of_line_with_horizontal_or_vertical_line": arch_41_intersection_of_line_with_horizontal_or_vertical_line,
    "42_area_of_triangle_formed_by_line_and_axes": arch_42_area_of_triangle_formed_by_line_and_axes,
    "43_rate_of_change_water_tank_filling": arch_43_rate_of_change_water_tank_filling,
    "44_rate_of_change_water_tank_draining": arch_44_rate_of_change_water_tank_draining,
    "45_distance_time_graph_average_speed_calculation": arch_45_distance_time_graph_average_speed_calculation,
    "46_distance_time_graph_multi_stage_journey": arch_46_distance_time_graph_multi_stage_journey,
    "47_cellphone_tariff_or_taxi_fare_comparison": arch_47_cellphone_tariff_or_taxi_fare_comparison,
    "48_business_break_even_income_vs_expenses": arch_48_business_break_even_income_vs_expenses,
    "49_error_analysis_inverted_gradient_formula": arch_49_error_analysis_inverted_gradient_formula,
    "50_compound_multi_step_graph_analysis": arch_50_compound_multi_step_graph_analysis,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

SUBSKILLS_TUPLES: List[Tuple[str, str]] = [
    (key, key[3:].replace("_", " ").title()) for key in SUBSKILLS
]


def generate_grade9_graphs_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Graphs & Linear Functions question."""
    r = random.Random(seed)
    if subskill and subskill in ARCHETYPE_MAP:
        builder = ARCHETYPE_MAP[subskill]
        chosen_subskill = subskill
    elif subskill:
        # Match by prefix or substring if requested
        s_clean = str(subskill).strip()
        matched = None
        for k, b in ARCHETYPE_MAP.items():
            if k.startswith(s_clean) or s_clean in k:
                matched = (k, b)
                break
        if matched:
            chosen_subskill, builder = matched
        else:
            chosen_subskill = r.choice(SUBSKILLS)
            builder = ARCHETYPE_MAP[chosen_subskill]
    else:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(r)
    q["subskill"] = chosen_subskill
    q["grade"] = "9"
    q["subject"] = "Mathematics"
    q["topic"] = "Graphs"
    q["term"] = 2
    q.setdefault("caps_weight_percent", 12)
    q.setdefault("suggested_duration_mins", 4)
    q.setdefault("difficulty", "medium")
    q.setdefault("mode", "compound")
    if not q.get("prompt"):
        q["prompt"] = q.get("question_text")
    if not q.get("sample_answer"):
        q["sample_answer"] = str(q.get("correct_answer"))
    return q


generate_grade9_linear_graphs_question = generate_grade9_graphs_question
generate_grade9_functions_graphs_question = generate_grade9_graphs_question


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """6-Pillar Generator Contract entry point."""
    r = random.Random(seed)
    questions: List[Dict[str, Any]] = []

    if subskill and subskill in ARCHETYPE_MAP:
        candidates = [subskill]
    else:
        candidates = SUBSKILLS

    for i in range(count):
        sub = candidates[i % len(candidates)] if len(candidates) > 1 else candidates[0]
        sub_seed = r.randint(1, 1_000_000_000)
        q = generate_grade9_graphs_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
