"""
Grade 8 Mathematics - Graphs Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/02. Graphs.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .graphs_archetypes_01_25 import (
    arch_01_identifying_quadrant_from_coordinates,
    arch_02_identifying_points_on_axes,
    arch_03_reading_coordinates_from_cartesian_plane_diagram,
    arch_04_identifying_letter_for_given_coordinate_pair,
    arch_05_plotting_reflection_in_x_axis,
    arch_06_plotting_reflection_in_y_axis,
    arch_07_identifying_independent_and_dependent_variables,
    arch_08_discrete_vs_continuous_data_identification,
    arch_09_reading_distance_between_points_on_same_horizontal_line,
    arch_10_reading_distance_between_points_on_same_vertical_line,
    arch_11_midpoint_of_horizontal_or_vertical_segment,
    arch_12_cartesian_coordinates_collinear_points,
    arch_13_completing_table_of_values_for_linear_graph,
    arch_14_matching_table_of_values_to_correct_linear_equation,
    arch_15_identifying_quadrant_signs_rule,
    arch_16_calculating_gradient_from_two_positive_points,
    arch_17_calculating_gradient_with_negative_coordinates,
    arch_18_calculating_negative_gradient_from_coordinates,
    arch_19_gradient_of_horizontal_line_zero,
    arch_20_gradient_of_vertical_line_undefined,
    arch_21_reading_gradient_directly_from_y_equals_mx_plus_c,
    arch_22_reading_y_intercept_from_equation,
    arch_23_finding_x_intercept_of_linear_graph,
    arch_24_writing_equation_from_gradient_and_y_intercept,
    arch_25_reading_gradient_and_intercept_from_cartesian_diagram,
)

from .graphs_archetypes_26_50 import (
    arch_26_identifying_parallel_lines_equal_gradients,
    arch_27_determining_direction_of_line_from_gradient_sign,
    arch_28_comparing_steepness_of_two_lines,
    arch_29_finding_missing_coordinate_given_gradient,
    arch_30_point_lies_on_line_verification,
    arch_31_distance_time_graph_reading_distance_at_time,
    arch_32_distance_time_graph_reading_time_at_distance,
    arch_33_distance_time_graph_identifying_rest_or_stopped_period,
    arch_34_distance_time_graph_calculating_speed_for_segment,
    arch_35_distance_time_graph_identifying_fastest_segment,
    arch_36_distance_time_graph_return_journey_analysis,
    arch_37_distance_time_graph_average_speed_entire_journey,
    arch_38_comparing_two_travelers_on_same_distance_time_graph,
    arch_39_speed_time_graph_identifying_constant_speed_acceleration,
    arch_40_speed_time_graph_calculating_acceleration,
    arch_41_story_graph_water_level_in_uniform_cylinder,
    arch_42_story_graph_water_level_in_conical_or_stepped_flask,
    arch_43_temperature_time_graph_cooling_rate,
    arch_44_conversion_graph_currency_rand_to_foreign,
    arch_45_conversion_graph_metric_to_imperial_units,
    arch_46_direct_proportion_graph_passes_through_origin,
    arch_47_inverse_proportion_graph_hyperbola_shape,
    arch_48_mobile_phone_call_cost_linear_tariff_graph,
    arch_49_break_even_point_identification_on_cost_revenue_graph,
    arch_50_matching_verbal_story_to_correct_graph_shape,
)


BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10
    arch_01_identifying_quadrant_from_coordinates,
    arch_02_identifying_points_on_axes,
    arch_03_reading_coordinates_from_cartesian_plane_diagram,
    arch_04_identifying_letter_for_given_coordinate_pair,
    arch_05_plotting_reflection_in_x_axis,
    arch_06_plotting_reflection_in_y_axis,
    arch_07_identifying_independent_and_dependent_variables,
    arch_08_discrete_vs_continuous_data_identification,
    arch_09_reading_distance_between_points_on_same_horizontal_line,
    arch_10_reading_distance_between_points_on_same_vertical_line,
    # 11 - 20
    arch_11_midpoint_of_horizontal_or_vertical_segment,
    arch_12_cartesian_coordinates_collinear_points,
    arch_13_completing_table_of_values_for_linear_graph,
    arch_14_matching_table_of_values_to_correct_linear_equation,
    arch_15_identifying_quadrant_signs_rule,
    arch_16_calculating_gradient_from_two_positive_points,
    arch_17_calculating_gradient_with_negative_coordinates,
    arch_18_calculating_negative_gradient_from_coordinates,
    arch_19_gradient_of_horizontal_line_zero,
    arch_20_gradient_of_vertical_line_undefined,
    # 21 - 28
    arch_21_reading_gradient_directly_from_y_equals_mx_plus_c,
    arch_22_reading_y_intercept_from_equation,
    arch_23_finding_x_intercept_of_linear_graph,
    arch_24_writing_equation_from_gradient_and_y_intercept,
    arch_25_reading_gradient_and_intercept_from_cartesian_diagram,
    arch_26_identifying_parallel_lines_equal_gradients,
    arch_27_determining_direction_of_line_from_gradient_sign,
    arch_28_comparing_steepness_of_two_lines,
    # 29 - 36
    arch_29_finding_missing_coordinate_given_gradient,
    arch_30_point_lies_on_line_verification,
    arch_31_distance_time_graph_reading_distance_at_time,
    arch_32_distance_time_graph_reading_time_at_distance,
    arch_33_distance_time_graph_identifying_rest_or_stopped_period,
    arch_34_distance_time_graph_calculating_speed_for_segment,
    arch_35_distance_time_graph_identifying_fastest_segment,
    arch_36_distance_time_graph_return_journey_analysis,
    # 37 - 44
    arch_37_distance_time_graph_average_speed_entire_journey,
    arch_38_comparing_two_travelers_on_same_distance_time_graph,
    arch_39_speed_time_graph_identifying_constant_speed_acceleration,
    arch_40_speed_time_graph_calculating_acceleration,
    arch_41_story_graph_water_level_in_uniform_cylinder,
    arch_42_story_graph_water_level_in_conical_or_stepped_flask,
    arch_43_temperature_time_graph_cooling_rate,
    arch_44_conversion_graph_currency_rand_to_foreign,
    # 45 - 50
    arch_45_conversion_graph_metric_to_imperial_units,
    arch_46_direct_proportion_graph_passes_through_origin,
    arch_47_inverse_proportion_graph_hyperbola_shape,
    arch_48_mobile_phone_call_cost_linear_tariff_graph,
    arch_49_break_even_point_identification_on_cost_revenue_graph,
    arch_50_matching_verbal_story_to_correct_graph_shape,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_identifying_quadrant_from_coordinates",
    "02_identifying_points_on_axes",
    "03_reading_coordinates_from_cartesian_plane_diagram",
    "04_identifying_letter_for_given_coordinate_pair",
    "05_plotting_reflection_in_x_axis",
    "06_plotting_reflection_in_y_axis",
    "07_identifying_independent_and_dependent_variables",
    "08_discrete_vs_continuous_data_identification",
    "09_reading_distance_between_points_on_same_horizontal_line",
    "10_reading_distance_between_points_on_same_vertical_line",
    # 11 - 20
    "11_midpoint_of_horizontal_or_vertical_segment",
    "12_cartesian_coordinates_collinear_points",
    "13_completing_table_of_values_for_linear_graph",
    "14_matching_table_of_values_to_correct_linear_equation",
    "15_identifying_quadrant_signs_rule",
    "16_calculating_gradient_from_two_positive_points",
    "17_calculating_gradient_with_negative_coordinates",
    "18_calculating_negative_gradient_from_coordinates",
    "19_gradient_of_horizontal_line_zero",
    "20_gradient_of_vertical_line_undefined",
    # 21 - 28
    "21_reading_gradient_directly_from_y_equals_mx_plus_c",
    "22_reading_y_intercept_from_equation",
    "23_finding_x_intercept_of_linear_graph",
    "24_writing_equation_from_gradient_and_y_intercept",
    "25_reading_gradient_and_intercept_from_cartesian_diagram",
    "26_identifying_parallel_lines_equal_gradients",
    "27_determining_direction_of_line_from_gradient_sign",
    "28_comparing_steepness_of_two_lines",
    # 29 - 36
    "29_finding_missing_coordinate_given_gradient",
    "30_point_lies_on_line_verification",
    "31_distance_time_graph_reading_distance_at_time",
    "32_distance_time_graph_reading_time_at_distance",
    "33_distance_time_graph_identifying_rest_or_stopped_period",
    "34_distance_time_graph_calculating_speed_for_segment",
    "35_distance_time_graph_identifying_fastest_segment",
    "36_distance_time_graph_return_journey_analysis",
    # 37 - 44
    "37_distance_time_graph_average_speed_entire_journey",
    "38_comparing_two_travelers_on_same_distance_time_graph",
    "39_speed_time_graph_identifying_constant_speed_acceleration",
    "40_speed_time_graph_calculating_acceleration",
    "41_story_graph_water_level_in_uniform_cylinder",
    "42_story_graph_water_level_in_conical_or_stepped_flask",
    "43_temperature_time_graph_cooling_rate",
    "44_conversion_graph_currency_rand_to_foreign",
    # 45 - 50
    "45_conversion_graph_metric_to_imperial_units",
    "46_direct_proportion_graph_passes_through_origin",
    "47_inverse_proportion_graph_hyperbola_shape",
    "48_mobile_phone_call_cost_linear_tariff_graph",
    "49_break_even_point_identification_on_cost_revenue_graph",
    "50_matching_verbal_story_to_correct_graph_shape",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases
DISPATCH_TABLE["cartesian_coordinates_four_quadrants"] = arch_01_identifying_quadrant_from_coordinates
DISPATCH_TABLE["gradient_slope_steepness"] = arch_16_calculating_gradient_from_two_positive_points
DISPATCH_TABLE["intercepts_x_and_y"] = arch_22_reading_y_intercept_from_equation
DISPATCH_TABLE["linear_vs_nonlinear_comparison"] = arch_46_direct_proportion_graph_passes_through_origin
DISPATCH_TABLE["real_world_rate_graph_interpretation"] = arch_31_distance_time_graph_reading_distance_at_time


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
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
        q.setdefault("topic", "Graphs")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
