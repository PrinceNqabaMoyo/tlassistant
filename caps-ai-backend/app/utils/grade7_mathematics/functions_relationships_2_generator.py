"""Grade 7 Mathematics - Functions and Relationships 2 Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Functions and relationships 2.md
Focus: Tables of values, finding rules y = mx + c, rate of change, inverse inputs, fractions, decimals, integers, and quadratic patterns.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .functions_2_archetypes_01_25 import (
    arch_01_table_linear_forward_fill_consecutive_x,
    arch_02_table_linear_forward_fill_step_size_two,
    arch_03_table_linear_forward_fill_large_x,
    arch_04_table_linear_reverse_solve_single_missing_x,
    arch_05_table_linear_reverse_solve_multiple_missing_x,
    arch_06_table_find_constant_difference_rule_positive,
    arch_07_table_find_constant_difference_rule_negative,
    arch_08_table_find_constant_multiplier_proportional,
    arch_09_table_find_rule_form_mx_plus_c,
    arch_10_table_find_rule_form_mx_minus_c,
    arch_11_table_find_initial_value_at_x_zero,
    arch_12_table_complete_both_missing_x_and_y,
    arch_13_table_detect_inconsistent_outlier_entry,
    arch_14_table_fraction_input_halves,
    arch_15_table_fraction_input_quarters,
    arch_16_table_decimal_input_step_zero_comma_five,
    arch_17_table_decimal_multiplier_rule,
    arch_18_table_integer_inputs_including_negatives,
    arch_19_table_negative_linear_gradient_decreasing,
    arch_20_table_quadratic_pattern_square_numbers,
    arch_21_table_cubic_pattern_cube_numbers,
    arch_22_table_pattern_square_plus_constant,
    arch_23_table_pattern_double_and_square,
    arch_24_table_geometric_doubling_sequence,
    arch_25_table_geometric_halving_sequence,
)
from .functions_2_archetypes_26_50 import (
    arch_26_table_matching_verbal_description,
    arch_27_table_translating_rule_to_table_values,
    arch_28_table_cost_of_items_bulk_pricing,
    arch_29_table_distance_speed_time_constant_speed,
    arch_30_table_conversion_litres_to_millilitres,
    arch_31_table_conversion_kilometres_to_metres,
    arch_32_table_perimeter_of_regular_pentagons,
    arch_33_table_perimeter_of_regular_hexagons,
    arch_34_table_area_of_rectangles_fixed_width,
    arch_35_table_cellphone_plan_cost_comparison,
    arch_36_table_savings_account_growth_constant_deposit,
    arch_37_table_temperature_degrees_celsius_change,
    arch_38_table_identifying_dependent_and_independent_variables,
    arch_39_table_identifying_linear_vs_nonlinear,
    arch_40_table_identifying_direct_proportion,
    arch_41_table_ratio_constant_k_equals_y_over_x,
    arch_42_table_flow_diagram_conversion_to_table,
    arch_43_table_converting_table_to_flow_diagram_operators,
    arch_44_table_evaluating_rule_with_brackets,
    arch_45_table_extending_pattern_to_hundredth_term,
    arch_46_table_extending_pattern_to_nth_general_term,
    arch_47_table_comparing_two_different_tables_same_inputs,
    arch_48_table_identifying_intersection_row_where_outputs_match,
    arch_49_table_reverse_lookup_maximum_capacity_budget,
    arch_50_table_comprehensive_diagnostic_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_table_linear_forward_fill_consecutive_x": arch_01_table_linear_forward_fill_consecutive_x,
    "02_table_linear_forward_fill_step_size_two": arch_02_table_linear_forward_fill_step_size_two,
    "03_table_linear_forward_fill_large_x": arch_03_table_linear_forward_fill_large_x,
    "04_table_linear_reverse_solve_single_missing_x": arch_04_table_linear_reverse_solve_single_missing_x,
    "05_table_linear_reverse_solve_multiple_missing_x": arch_05_table_linear_reverse_solve_multiple_missing_x,
    "06_table_find_constant_difference_rule_positive": arch_06_table_find_constant_difference_rule_positive,
    "07_table_find_constant_difference_rule_negative": arch_07_table_find_constant_difference_rule_negative,
    "08_table_find_constant_multiplier_proportional": arch_08_table_find_constant_multiplier_proportional,
    "09_table_find_rule_form_mx_plus_c": arch_09_table_find_rule_form_mx_plus_c,
    "10_table_find_rule_form_mx_minus_c": arch_10_table_find_rule_form_mx_minus_c,
    "11_table_find_initial_value_at_x_zero": arch_11_table_find_initial_value_at_x_zero,
    "12_table_complete_both_missing_x_and_y": arch_12_table_complete_both_missing_x_and_y,
    "13_table_detect_inconsistent_outlier_entry": arch_13_table_detect_inconsistent_outlier_entry,
    "14_table_fraction_input_halves": arch_14_table_fraction_input_halves,
    "15_table_fraction_input_quarters": arch_15_table_fraction_input_quarters,
    "16_table_decimal_input_step_zero_comma_five": arch_16_table_decimal_input_step_zero_comma_five,
    "17_table_decimal_multiplier_rule": arch_17_table_decimal_multiplier_rule,
    "18_table_integer_inputs_including_negatives": arch_18_table_integer_inputs_including_negatives,
    "19_table_negative_linear_gradient_decreasing": arch_19_table_negative_linear_gradient_decreasing,
    "20_table_quadratic_pattern_square_numbers": arch_20_table_quadratic_pattern_square_numbers,
    "21_table_cubic_pattern_cube_numbers": arch_21_table_cubic_pattern_cube_numbers,
    "22_table_pattern_square_plus_constant": arch_22_table_pattern_square_plus_constant,
    "23_table_pattern_double_and_square": arch_23_table_pattern_double_and_square,
    "24_table_geometric_doubling_sequence": arch_24_table_geometric_doubling_sequence,
    "25_table_geometric_halving_sequence": arch_25_table_geometric_halving_sequence,
    "26_table_matching_verbal_description": arch_26_table_matching_verbal_description,
    "27_table_translating_rule_to_table_values": arch_27_table_translating_rule_to_table_values,
    "28_table_cost_of_items_bulk_pricing": arch_28_table_cost_of_items_bulk_pricing,
    "29_table_distance_speed_time_constant_speed": arch_29_table_distance_speed_time_constant_speed,
    "30_table_conversion_litres_to_millilitres": arch_30_table_conversion_litres_to_millilitres,
    "31_table_conversion_kilometres_to_metres": arch_31_table_conversion_kilometres_to_metres,
    "32_table_perimeter_of_regular_pentagons": arch_32_table_perimeter_of_regular_pentagons,
    "33_table_perimeter_of_regular_hexagons": arch_33_table_perimeter_of_regular_hexagons,
    "34_table_area_of_rectangles_fixed_width": arch_34_table_area_of_rectangles_fixed_width,
    "35_table_cellphone_plan_cost_comparison": arch_35_table_cellphone_plan_cost_comparison,
    "36_table_savings_account_growth_constant_deposit": arch_36_table_savings_account_growth_constant_deposit,
    "37_table_temperature_degrees_celsius_change": arch_37_table_temperature_degrees_celsius_change,
    "38_table_identifying_dependent_and_independent_variables": arch_38_table_identifying_dependent_and_independent_variables,
    "39_table_identifying_linear_vs_nonlinear": arch_39_table_identifying_linear_vs_nonlinear,
    "40_table_identifying_direct_proportion": arch_40_table_identifying_direct_proportion,
    "41_table_ratio_constant_k_equals_y_over_x": arch_41_table_ratio_constant_k_equals_y_over_x,
    "42_table_flow_diagram_conversion_to_table": arch_42_table_flow_diagram_conversion_to_table,
    "43_table_converting_table_to_flow_diagram_operators": arch_43_table_converting_table_to_flow_diagram_operators,
    "44_table_evaluating_rule_with_brackets": arch_44_table_evaluating_rule_with_brackets,
    "45_table_extending_pattern_to_hundredth_term": arch_45_table_extending_pattern_to_hundredth_term,
    "46_table_extending_pattern_to_nth_general_term": arch_46_table_extending_pattern_to_nth_general_term,
    "47_table_comparing_two_different_tables_same_inputs": arch_47_table_comparing_two_different_tables_same_inputs,
    "48_table_identifying_intersection_row_where_outputs_match": arch_48_table_identifying_intersection_row_where_outputs_match,
    "49_table_reverse_lookup_maximum_capacity_budget": arch_49_table_reverse_lookup_maximum_capacity_budget,
    "50_table_comprehensive_diagnostic_autopsy": arch_50_table_comprehensive_diagnostic_autopsy,
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
