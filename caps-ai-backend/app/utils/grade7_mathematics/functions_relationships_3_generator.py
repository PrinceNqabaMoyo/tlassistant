"""Grade 7 Mathematics - Functions and Relationships 3 Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/02. Functions and relationships 3.md
Focus: Cartesian coordinates, linear rate of change (gradient), intercepts, graphs (distance-time, cost, temperature), and journey autopsies.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .functions_3_archetypes_01_25 import (
    arch_01_cartesian_ordered_pairs_from_linear_rule,
    arch_02_cartesian_identifying_x_and_y_coordinates,
    arch_03_cartesian_plotting_points_first_quadrant,
    arch_04_cartesian_points_with_negative_coordinates,
    arch_05_cartesian_points_on_axes_intercepts,
    arch_06_rate_of_change_gradient_from_two_points,
    arch_07_rate_of_change_gradient_from_table,
    arch_08_rate_of_change_positive_steepness_comparison,
    arch_09_rate_of_change_negative_downward_slope,
    arch_10_rate_of_change_horizontal_line_zero_gradient,
    arch_11_graph_line_equation_matching_given_graph,
    arch_12_graph_identifying_y_intercept_from_graph,
    arch_13_graph_identifying_x_intercept_where_y_is_zero,
    arch_14_graph_linear_vs_curved_non_linear_distinction,
    arch_15_graph_discrete_vs_continuous_data_points,
    arch_16_graph_table_formula_three_way_matching,
    arch_17_graph_determining_if_point_lies_on_line,
    arch_18_graph_finding_missing_coordinate_on_line,
    arch_19_graph_parallel_lines_equal_rate_of_change,
    arch_20_graph_intersecting_lines_point_of_intersection,
    arch_21_graph_direct_proportion_line_through_origin,
    arch_22_graph_reading_value_at_given_x,
    arch_23_graph_reading_value_at_given_y,
    arch_24_graph_extrapolating_trend_line,
    arch_25_graph_interpolating_between_plotted_points,
)
from .functions_3_archetypes_26_50 import (
    arch_26_distance_time_graph_constant_speed_segment,
    arch_27_distance_time_graph_stationary_horizontal_segment,
    arch_28_distance_time_graph_calculating_speed,
    arch_29_distance_time_graph_returning_to_start,
    arch_30_distance_time_graph_comparing_two_travellers,
    arch_31_cost_graph_fixed_charge_plus_variable_rate,
    arch_32_cost_graph_break_even_comparison_two_tariffs,
    arch_33_water_level_graph_filling_constant_rate,
    arch_34_water_level_graph_emptying_leaking_tank,
    arch_35_temperature_graph_daily_fluctuation_cycle,
    arch_36_conversion_graph_currency_rand_to_dollar,
    arch_37_conversion_graph_measurement_miles_to_kilometres,
    arch_38_graph_interpreting_steepness_as_speed,
    arch_39_graph_identifying_maximum_and_minimum_turning_points,
    arch_40_graph_interpreting_average_speed_whole_journey,
    arch_41_graph_from_verbal_journey_story,
    arch_42_verbal_story_from_given_graph,
    arch_43_graph_interpreting_horizontal_axis_units_and_scale,
    arch_44_graph_interpreting_vertical_axis_units_and_scale,
    arch_45_graph_detecting_misleading_scale_distortion,
    arch_46_graph_quadratic_parabola_symmetry_observation,
    arch_47_graph_identifying_domain_and_range_concept,
    arch_48_graph_step_function_parking_fees,
    arch_49_graph_speed_time_interpreting_acceleration,
    arch_50_graph_comprehensive_journey_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_cartesian_ordered_pairs_from_linear_rule": arch_01_cartesian_ordered_pairs_from_linear_rule,
    "02_cartesian_identifying_x_and_y_coordinates": arch_02_cartesian_identifying_x_and_y_coordinates,
    "03_cartesian_plotting_points_first_quadrant": arch_03_cartesian_plotting_points_first_quadrant,
    "04_cartesian_points_with_negative_coordinates": arch_04_cartesian_points_with_negative_coordinates,
    "05_cartesian_points_on_axes_intercepts": arch_05_cartesian_points_on_axes_intercepts,
    "06_rate_of_change_gradient_from_two_points": arch_06_rate_of_change_gradient_from_two_points,
    "07_rate_of_change_gradient_from_table": arch_07_rate_of_change_gradient_from_table,
    "08_rate_of_change_positive_steepness_comparison": arch_08_rate_of_change_positive_steepness_comparison,
    "09_rate_of_change_negative_downward_slope": arch_09_rate_of_change_negative_downward_slope,
    "10_rate_of_change_horizontal_line_zero_gradient": arch_10_rate_of_change_horizontal_line_zero_gradient,
    "11_graph_line_equation_matching_given_graph": arch_11_graph_line_equation_matching_given_graph,
    "12_graph_identifying_y_intercept_from_graph": arch_12_graph_identifying_y_intercept_from_graph,
    "13_graph_identifying_x_intercept_where_y_is_zero": arch_13_graph_identifying_x_intercept_where_y_is_zero,
    "14_graph_linear_vs_curved_non_linear_distinction": arch_14_graph_linear_vs_curved_non_linear_distinction,
    "15_graph_discrete_vs_continuous_data_points": arch_15_graph_discrete_vs_continuous_data_points,
    "16_graph_table_formula_three_way_matching": arch_16_graph_table_formula_three_way_matching,
    "17_graph_determining_if_point_lies_on_line": arch_17_graph_determining_if_point_lies_on_line,
    "18_graph_finding_missing_coordinate_on_line": arch_18_graph_finding_missing_coordinate_on_line,
    "19_graph_parallel_lines_equal_rate_of_change": arch_19_graph_parallel_lines_equal_rate_of_change,
    "20_graph_intersecting_lines_point_of_intersection": arch_20_graph_intersecting_lines_point_of_intersection,
    "21_graph_direct_proportion_line_through_origin": arch_21_graph_direct_proportion_line_through_origin,
    "22_graph_reading_value_at_given_x": arch_22_graph_reading_value_at_given_x,
    "23_graph_reading_value_at_given_y": arch_23_graph_reading_value_at_given_y,
    "24_graph_extrapolating_trend_line": arch_24_graph_extrapolating_trend_line,
    "25_graph_interpolating_between_plotted_points": arch_25_graph_interpolating_between_plotted_points,
    "26_distance_time_graph_constant_speed_segment": arch_26_distance_time_graph_constant_speed_segment,
    "27_distance_time_graph_stationary_horizontal_segment": arch_27_distance_time_graph_stationary_horizontal_segment,
    "28_distance_time_graph_calculating_speed": arch_28_distance_time_graph_calculating_speed,
    "29_distance_time_graph_returning_to_start": arch_29_distance_time_graph_returning_to_start,
    "30_distance_time_graph_comparing_two_travellers": arch_30_distance_time_graph_comparing_two_travellers,
    "31_cost_graph_fixed_charge_plus_variable_rate": arch_31_cost_graph_fixed_charge_plus_variable_rate,
    "32_cost_graph_break_even_comparison_two_tariffs": arch_32_cost_graph_break_even_comparison_two_tariffs,
    "33_water_level_graph_filling_constant_rate": arch_33_water_level_graph_filling_constant_rate,
    "34_water_level_graph_emptying_leaking_tank": arch_34_water_level_graph_emptying_leaking_tank,
    "35_temperature_graph_daily_fluctuation_cycle": arch_35_temperature_graph_daily_fluctuation_cycle,
    "36_conversion_graph_currency_rand_to_dollar": arch_36_conversion_graph_currency_rand_to_dollar,
    "37_conversion_graph_measurement_miles_to_kilometres": arch_37_conversion_graph_measurement_miles_to_kilometres,
    "38_graph_interpreting_steepness_as_speed": arch_38_graph_interpreting_steepness_as_speed,
    "39_graph_identifying_maximum_and_minimum_turning_points": arch_39_graph_identifying_maximum_and_minimum_turning_points,
    "40_graph_interpreting_average_speed_whole_journey": arch_40_graph_interpreting_average_speed_whole_journey,
    "41_graph_from_verbal_journey_story": arch_41_graph_from_verbal_journey_story,
    "42_verbal_story_from_given_graph": arch_42_verbal_story_from_given_graph,
    "43_graph_interpreting_horizontal_axis_units_and_scale": arch_43_graph_interpreting_horizontal_axis_units_and_scale,
    "44_graph_interpreting_vertical_axis_units_and_scale": arch_44_graph_interpreting_vertical_axis_units_and_scale,
    "45_graph_detecting_misleading_scale_distortion": arch_45_graph_detecting_misleading_scale_distortion,
    "46_graph_quadratic_parabola_symmetry_observation": arch_46_graph_quadratic_parabola_symmetry_observation,
    "47_graph_identifying_domain_and_range_concept": arch_47_graph_identifying_domain_and_range_concept,
    "48_graph_step_function_parking_fees": arch_48_graph_step_function_parking_fees,
    "49_graph_speed_time_interpreting_acceleration": arch_49_graph_speed_time_interpreting_acceleration,
    "50_graph_comprehensive_journey_autopsy": arch_50_graph_comprehensive_journey_autopsy,
}

SUBSKILLS = list(ARCHETYPE_BUILDERS.keys())


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed) if seed is not None else random.Random()
    if subskill is None or subskill not in ARCHETYPE_BUILDERS:
        subskill = rng.choice(SUBSKILLS)
    builder = ARCHETYPE_BUILDERS[subskill]
    return builder(rng)


generate = generate_question
