"""Grade 9 Mathematics - Functions and Relationships Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 1/05. Functions and relationships.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .functions_archetypes_01_25 import (
    arch_01_flow_diagram_linear_positive_slope_integer_output,
    arch_02_flow_diagram_linear_negative_slope_integer_output,
    arch_03_flow_diagram_two_step_bracket_operation,
    arch_04_flow_diagram_fractional_operator_output,
    arch_05_flow_diagram_inverse_calculate_input_from_output,
    arch_06_flow_diagram_determine_missing_operator,
    arch_07_table_linear_positive_coefficient_find_outputs,
    arch_08_table_linear_negative_coefficient_find_outputs,
    arch_09_table_linear_missing_input_values,
    arch_10_table_mixed_missing_inputs_and_outputs,
    arch_11_determine_rule_y_equals_mx_plus_c_from_table,
    arch_12_determine_rule_with_negative_slope_from_table,
    arch_13_determine_rule_from_verbal_description,
    arch_14_match_flow_diagram_to_algebraic_formula,
    arch_15_match_table_of_values_to_formula,
    arch_16_equivalent_formulae_algebraic_expansion_check,
    arch_17_linear_function_evaluate_for_negative_input,
    arch_18_linear_function_evaluate_for_fractional_input,
    arch_19_quadratic_function_table_evaluation_y_equals_x_squared,
    arch_20_quadratic_function_evaluate_y_equals_ax_squared_plus_c,
    arch_21_quadratic_function_find_missing_inputs,
    arch_22_exponential_function_table_powers_of_two,
    arch_23_exponential_function_evaluate_y_equals_a_times_b_to_x,
    arch_24_inverse_proportion_function_xy_equals_k,
    arch_25_inverse_proportion_table_find_missing_values,
)
from .functions_archetypes_26_50 import (
    arch_26_real_world_taxi_fare_fixed_plus_per_km_rate,
    arch_27_real_world_cellphone_contract_monthly_plus_per_minute,
    arch_28_real_world_water_tank_draining_linear_depletion,
    arch_29_real_world_water_tank_filling_constant_rate,
    arch_30_real_world_temperature_conversion_celsius_to_fahrenheit,
    arch_31_real_world_speed_distance_time_function_graph_rule,
    arch_32_real_world_electricity_cost_tiered_or_flat_rate,
    arch_33_function_input_output_ordered_pairs_domain_range,
    arch_34_identify_dependent_vs_independent_variable_context,
    arch_35_composite_flow_diagram_two_stages,
    arch_36_determine_constant_difference_and_zeroth_term,
    arch_37_table_non_consecutive_inputs_find_gradient,
    arch_38_formula_substitution_large_value_extrapolation,
    arch_39_formula_substitution_solve_for_x_integer_result,
    arch_40_formula_substitution_solve_for_x_fraction_result,
    arch_41_compare_two_linear_plans_find_breakeven_input,
    arch_42_linear_function_rate_of_change_interpretation,
    arch_43_step_function_parking_fee_or_postage_rates,
    arch_44_cubic_function_table_evaluation_y_equals_x_cubed,
    arch_45_rational_function_table_evaluation_simple_hyperbola,
    arch_46_geometric_pattern_to_function_rule_perimeter,
    arch_47_geometric_pattern_to_function_rule_area_growth,
    arch_48_error_analysis_misidentifying_constant_term_in_rule,
    arch_49_error_analysis_inverted_operations_in_finding_input,
    arch_50_compound_multi_representation_table_formula_flow_integration,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_flow_diagram_linear_positive_slope_integer_output": arch_01_flow_diagram_linear_positive_slope_integer_output,
    "02_flow_diagram_linear_negative_slope_integer_output": arch_02_flow_diagram_linear_negative_slope_integer_output,
    "03_flow_diagram_two_step_bracket_operation": arch_03_flow_diagram_two_step_bracket_operation,
    "04_flow_diagram_fractional_operator_output": arch_04_flow_diagram_fractional_operator_output,
    "05_flow_diagram_inverse_calculate_input_from_output": arch_05_flow_diagram_inverse_calculate_input_from_output,
    "06_flow_diagram_determine_missing_operator": arch_06_flow_diagram_determine_missing_operator,
    "07_table_linear_positive_coefficient_find_outputs": arch_07_table_linear_positive_coefficient_find_outputs,
    "08_table_linear_negative_coefficient_find_outputs": arch_08_table_linear_negative_coefficient_find_outputs,
    "09_table_linear_missing_input_values": arch_09_table_linear_missing_input_values,
    "10_table_mixed_missing_inputs_and_outputs": arch_10_table_mixed_missing_inputs_and_outputs,
    "11_determine_rule_y_equals_mx_plus_c_from_table": arch_11_determine_rule_y_equals_mx_plus_c_from_table,
    "12_determine_rule_with_negative_slope_from_table": arch_12_determine_rule_with_negative_slope_from_table,
    "13_determine_rule_from_verbal_description": arch_13_determine_rule_from_verbal_description,
    "14_match_flow_diagram_to_algebraic_formula": arch_14_match_flow_diagram_to_algebraic_formula,
    "15_match_table_of_values_to_formula": arch_15_match_table_of_values_to_formula,
    "16_equivalent_formulae_algebraic_expansion_check": arch_16_equivalent_formulae_algebraic_expansion_check,
    "17_linear_function_evaluate_for_negative_input": arch_17_linear_function_evaluate_for_negative_input,
    "18_linear_function_evaluate_for_fractional_input": arch_18_linear_function_evaluate_for_fractional_input,
    "19_quadratic_function_table_evaluation_y_equals_x_squared": arch_19_quadratic_function_table_evaluation_y_equals_x_squared,
    "20_quadratic_function_evaluate_y_equals_ax_squared_plus_c": arch_20_quadratic_function_evaluate_y_equals_ax_squared_plus_c,
    "21_quadratic_function_find_missing_inputs": arch_21_quadratic_function_find_missing_inputs,
    "22_exponential_function_table_powers_of_two": arch_22_exponential_function_table_powers_of_two,
    "23_exponential_function_evaluate_y_equals_a_times_b_to_x": arch_23_exponential_function_evaluate_y_equals_a_times_b_to_x,
    "24_inverse_proportion_function_xy_equals_k": arch_24_inverse_proportion_function_xy_equals_k,
    "25_inverse_proportion_table_find_missing_values": arch_25_inverse_proportion_table_find_missing_values,
    "26_real_world_taxi_fare_fixed_plus_per_km_rate": arch_26_real_world_taxi_fare_fixed_plus_per_km_rate,
    "27_real_world_cellphone_contract_monthly_plus_per_minute": arch_27_real_world_cellphone_contract_monthly_plus_per_minute,
    "28_real_world_water_tank_draining_linear_depletion": arch_28_real_world_water_tank_draining_linear_depletion,
    "29_real_world_water_tank_filling_constant_rate": arch_29_real_world_water_tank_filling_constant_rate,
    "30_real_world_temperature_conversion_celsius_to_fahrenheit": arch_30_real_world_temperature_conversion_celsius_to_fahrenheit,
    "31_real_world_speed_distance_time_function_graph_rule": arch_31_real_world_speed_distance_time_function_graph_rule,
    "32_real_world_electricity_cost_tiered_or_flat_rate": arch_32_real_world_electricity_cost_tiered_or_flat_rate,
    "33_function_input_output_ordered_pairs_domain_range": arch_33_function_input_output_ordered_pairs_domain_range,
    "34_identify_dependent_vs_independent_variable_context": arch_34_identify_dependent_vs_independent_variable_context,
    "35_composite_flow_diagram_two_stages": arch_35_composite_flow_diagram_two_stages,
    "36_determine_constant_difference_and_zeroth_term": arch_36_determine_constant_difference_and_zeroth_term,
    "37_table_non_consecutive_inputs_find_gradient": arch_37_table_non_consecutive_inputs_find_gradient,
    "38_formula_substitution_large_value_extrapolation": arch_38_formula_substitution_large_value_extrapolation,
    "39_formula_substitution_solve_for_x_integer_result": arch_39_formula_substitution_solve_for_x_integer_result,
    "40_formula_substitution_solve_for_x_fraction_result": arch_40_formula_substitution_solve_for_x_fraction_result,
    "41_compare_two_linear_plans_find_breakeven_input": arch_41_compare_two_linear_plans_find_breakeven_input,
    "42_linear_function_rate_of_change_interpretation": arch_42_linear_function_rate_of_change_interpretation,
    "43_step_function_parking_fee_or_postage_rates": arch_43_step_function_parking_fee_or_postage_rates,
    "44_cubic_function_table_evaluation_y_equals_x_cubed": arch_44_cubic_function_table_evaluation_y_equals_x_cubed,
    "45_rational_function_table_evaluation_simple_hyperbola": arch_45_rational_function_table_evaluation_simple_hyperbola,
    "46_geometric_pattern_to_function_rule_perimeter": arch_46_geometric_pattern_to_function_rule_perimeter,
    "47_geometric_pattern_to_function_rule_area_growth": arch_47_geometric_pattern_to_function_rule_area_growth,
    "48_error_analysis_misidentifying_constant_term_in_rule": arch_48_error_analysis_misidentifying_constant_term_in_rule,
    "49_error_analysis_inverted_operations_in_finding_input": arch_49_error_analysis_inverted_operations_in_finding_input,
    "50_compound_multi_representation_table_formula_flow_integration": arch_50_compound_multi_representation_table_formula_flow_integration,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_functions_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Functions and Relationships question."""
    r = random.Random(seed)
    if subskill and subskill in ARCHETYPE_MAP:
        builder = ARCHETYPE_MAP[subskill]
        chosen_subskill = subskill
    else:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(r)
    q["subskill"] = chosen_subskill
    q["grade"] = "9"
    q["subject"] = "Mathematics"
    q["topic"] = "Functions and relationships"
    q["term"] = 1
    return q


generate_grade9_functions_relationships_question = generate_grade9_functions_question


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
        q = generate_grade9_functions_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
