"""
Grade 7 Mathematics - Graphs Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/04. Graphs.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .graphs_archetypes_01_25 import (
    arch_01_story_graph_identify_increasing_interval,
    arch_02_story_graph_identify_decreasing_interval,
    arch_03_story_graph_identify_constant_interval,
    arch_04_story_graph_identify_maximum_turning_point,
    arch_05_story_graph_identify_minimum_turning_point,
    arch_06_discrete_vs_continuous_concept_classification,
    arch_07_discrete_graph_interpretation_points_only,
    arch_08_continuous_graph_interpretation_unbroken_line,
    arch_09_independent_vs_dependent_variable_identification,
    arch_10_axis_labels_and_scales_reading,
    arch_11_rate_of_change_constant_linear_identification,
    arch_12_rate_of_change_increasing_faster_and_faster,
    arch_13_rate_of_change_decreasing_slower_and_slower,
    arch_14_steepness_comparison_fast_vs_slow_change,
    arch_15_reading_output_value_from_given_input,
    arch_16_reading_input_value_from_given_output,
    arch_17_distance_time_graph_stationary_period,
    arch_18_distance_time_graph_total_distance_traveled,
    arch_19_distance_time_graph_calculating_speed_from_slope,
    arch_20_distance_time_graph_fastest_leg_comparison,
    arch_21_distance_time_graph_return_journey,
    arch_22_water_tank_filling_constant_flow_cylinder,
    arch_23_water_tank_filling_cone_or_funnel,
    arch_24_water_tank_filling_stepped_cylinder_bottle,
    arch_25_water_tank_emptying_graph_interpretation,
)

from .graphs_archetypes_26_50 import (
    arch_26_temperature_graph_daily_fluctuation_max_min,
    arch_27_temperature_graph_rate_of_cooling_heating,
    arch_28_comparing_two_runners_same_axes_who_won,
    arch_29_comparing_two_runners_point_of_overtaking,
    arch_30_comparing_two_runners_head_start_delay,
    arch_31_savings_accumulation_linear_graph,
    arch_32_cellphone_plan_cost_vs_minutes_graph,
    arch_33_plant_growth_over_weeks_table_to_graph,
    arch_34_speed_time_graph_acceleration_and_braking,
    arch_35_speed_time_graph_constant_speed_cruise,
    arch_36_matching_story_to_correct_graph_option,
    arch_37_drawing_inferences_from_flattening_curve,
    arch_38_identifying_intercepts_starting_value,
    arch_39_identifying_intercepts_finishing_value,
    arch_40_travel_graph_lunch_break_duration,
    arch_41_linear_vs_nonlinear_graph_identification,
    arch_42_interpreting_negative_slope_in_practical_context,
    arch_43_spot_the_error_misreading_axes_scale,
    arch_44_spot_the_error_confusing_steepness_with_height,
    arch_45_spot_the_error_connecting_discrete_dots,
    arch_46_practical_context_hiking_elevation_profile,
    arch_47_practical_context_battery_percentage_discharge,
    arch_48_practical_context_baking_oven_preheating,
    arch_49_practical_context_rainfall_accumulation_storm,
    arch_50_comprehensive_multi_stage_journey_autopsy,
)

ARCHETYPE_BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    arch_01_story_graph_identify_increasing_interval,
    arch_02_story_graph_identify_decreasing_interval,
    arch_03_story_graph_identify_constant_interval,
    arch_04_story_graph_identify_maximum_turning_point,
    arch_05_story_graph_identify_minimum_turning_point,
    arch_06_discrete_vs_continuous_concept_classification,
    arch_07_discrete_graph_interpretation_points_only,
    arch_08_continuous_graph_interpretation_unbroken_line,
    arch_09_independent_vs_dependent_variable_identification,
    arch_10_axis_labels_and_scales_reading,
    arch_11_rate_of_change_constant_linear_identification,
    arch_12_rate_of_change_increasing_faster_and_faster,
    arch_13_rate_of_change_decreasing_slower_and_slower,
    arch_14_steepness_comparison_fast_vs_slow_change,
    arch_15_reading_output_value_from_given_input,
    arch_16_reading_input_value_from_given_output,
    arch_17_distance_time_graph_stationary_period,
    arch_18_distance_time_graph_total_distance_traveled,
    arch_19_distance_time_graph_calculating_speed_from_slope,
    arch_20_distance_time_graph_fastest_leg_comparison,
    arch_21_distance_time_graph_return_journey,
    arch_22_water_tank_filling_constant_flow_cylinder,
    arch_23_water_tank_filling_cone_or_funnel,
    arch_24_water_tank_filling_stepped_cylinder_bottle,
    arch_25_water_tank_emptying_graph_interpretation,
    arch_26_temperature_graph_daily_fluctuation_max_min,
    arch_27_temperature_graph_rate_of_cooling_heating,
    arch_28_comparing_two_runners_same_axes_who_won,
    arch_29_comparing_two_runners_point_of_overtaking,
    arch_30_comparing_two_runners_head_start_delay,
    arch_31_savings_accumulation_linear_graph,
    arch_32_cellphone_plan_cost_vs_minutes_graph,
    arch_33_plant_growth_over_weeks_table_to_graph,
    arch_34_speed_time_graph_acceleration_and_braking,
    arch_35_speed_time_graph_constant_speed_cruise,
    arch_36_matching_story_to_correct_graph_option,
    arch_37_drawing_inferences_from_flattening_curve,
    arch_38_identifying_intercepts_starting_value,
    arch_39_identifying_intercepts_finishing_value,
    arch_40_travel_graph_lunch_break_duration,
    arch_41_linear_vs_nonlinear_graph_identification,
    arch_42_interpreting_negative_slope_in_practical_context,
    arch_43_spot_the_error_misreading_axes_scale,
    arch_44_spot_the_error_confusing_steepness_with_height,
    arch_45_spot_the_error_connecting_discrete_dots,
    arch_46_practical_context_hiking_elevation_profile,
    arch_47_practical_context_battery_percentage_discharge,
    arch_48_practical_context_baking_oven_preheating,
    arch_49_practical_context_rainfall_accumulation_storm,
    arch_50_comprehensive_multi_stage_journey_autopsy,
]

SUBSKILLS: List[str] = [
    "01_story_graph_identify_increasing_interval",
    "02_story_graph_identify_decreasing_interval",
    "03_story_graph_identify_constant_interval",
    "04_story_graph_identify_maximum_turning_point",
    "05_story_graph_identify_minimum_turning_point",
    "06_discrete_vs_continuous_concept_classification",
    "07_discrete_graph_interpretation_points_only",
    "08_continuous_graph_interpretation_unbroken_line",
    "09_independent_vs_dependent_variable_identification",
    "10_axis_labels_and_scales_reading",
    "11_rate_of_change_constant_linear_identification",
    "12_rate_of_change_increasing_faster_and_faster",
    "13_rate_of_change_decreasing_slower_and_slower",
    "14_steepness_comparison_fast_vs_slow_change",
    "15_reading_output_value_from_given_input",
    "16_reading_input_value_from_given_output",
    "17_distance_time_graph_stationary_period",
    "18_distance_time_graph_total_distance_traveled",
    "19_distance_time_graph_calculating_speed_from_slope",
    "20_distance_time_graph_fastest_leg_comparison",
    "21_distance_time_graph_return_journey",
    "22_water_tank_filling_constant_flow_cylinder",
    "23_water_tank_filling_cone_or_funnel",
    "24_water_tank_filling_stepped_cylinder_bottle",
    "25_water_tank_emptying_graph_interpretation",
    "26_temperature_graph_daily_fluctuation_max_min",
    "27_temperature_graph_rate_of_cooling_heating",
    "28_comparing_two_runners_same_axes_who_won",
    "29_comparing_two_runners_point_of_overtaking",
    "30_comparing_two_runners_head_start_delay",
    "31_savings_accumulation_linear_graph",
    "32_cellphone_plan_cost_vs_minutes_graph",
    "33_plant_growth_over_weeks_table_to_graph",
    "34_speed_time_graph_acceleration_and_braking",
    "35_speed_time_graph_constant_speed_cruise",
    "36_matching_story_to_correct_graph_option",
    "37_drawing_inferences_from_flattening_curve",
    "38_identifying_intercepts_starting_value",
    "39_identifying_intercepts_finishing_value",
    "40_travel_graph_lunch_break_duration",
    "41_linear_vs_nonlinear_graph_identification",
    "42_interpreting_negative_slope_in_practical_context",
    "43_spot_the_error_misreading_axes_scale",
    "44_spot_the_error_confusing_steepness_with_height",
    "45_spot_the_error_connecting_discrete_dots",
    "46_practical_context_hiking_elevation_profile",
    "47_practical_context_battery_percentage_discharge",
    "48_practical_context_baking_oven_preheating",
    "49_practical_context_rainfall_accumulation_storm",
    "50_comprehensive_multi_stage_journey_autopsy",
]

_SUBSKILL_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    name: builder for name, builder in zip(SUBSKILLS, ARCHETYPE_BUILDERS)
}


def generate_question(
    rng: Optional[random.Random] = None,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    """Generates a fully calibrated Grade 7 Graphs question."""
    if rng is None:
        rng = random.Random(seed) if seed is not None else random.Random()

    if subskill and subskill in _SUBSKILL_MAP:
        builder = _SUBSKILL_MAP[subskill]
    else:
        builder = rng.choice(ARCHETYPE_BUILDERS)

    payload = builder(rng)

    payload.setdefault("term", 1)
    payload.setdefault("grade", 7)
    payload.setdefault("subject", "Mathematics")
    payload.setdefault("topic", "Graphs")
    payload.setdefault("caps_weight_percent", 10.0)
    payload.setdefault("suggested_duration_mins", 3)
    payload.setdefault("mode", "elementary_" + payload.get("subskill", "graphs"))
    payload.setdefault(
        "marking_schema",
        [
            {"step": "Correct graph feature identification", "marks": 1, "type": "M"},
            {"step": "Correct value and interpretation", "marks": max(1, payload.get("marks", 2) - 1), "type": "A"},
        ],
    )
    return payload


generate = generate_question
