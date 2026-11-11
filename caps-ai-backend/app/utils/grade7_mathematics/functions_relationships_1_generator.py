"""Grade 7 Mathematics - Functions and Relationships 1 Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Functions and relationships 1.md
Focus: Flow diagrams, single & two-step function machines, forward evaluation, and inverse operations.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .functions_1_archetypes_01_25 import (
    arch_01_single_operation_forward_addition,
    arch_02_single_operation_forward_subtraction,
    arch_03_single_operation_forward_multiplication,
    arch_04_single_operation_forward_division,
    arch_05_single_operation_reverse_subtraction_to_addition,
    arch_06_single_operation_reverse_addition_to_subtraction,
    arch_07_single_operation_reverse_division_to_multiplication,
    arch_08_single_operation_reverse_multiplication_to_division,
    arch_09_two_step_rule_multiply_then_add,
    arch_10_two_step_rule_multiply_then_subtract,
    arch_11_two_step_rule_divide_then_add,
    arch_12_two_step_rule_divide_then_subtract,
    arch_13_two_step_rule_add_then_multiply_brackets,
    arch_14_two_step_rule_subtract_then_multiply_brackets,
    arch_15_two_step_reverse_multiply_add_to_input,
    arch_16_two_step_reverse_multiply_subtract_to_input,
    arch_17_two_step_reverse_divide_add_to_input,
    arch_18_two_step_reverse_brackets_rule_to_input,
    arch_19_identify_operator_in_single_step_diagram,
    arch_20_identify_second_operator_given_first,
    arch_21_equivalent_flow_diagrams_order_of_operations,
    arch_22_distributive_property_in_flow_diagrams,
    arch_23_integer_flow_diagram_negative_input,
    arch_24_integer_flow_diagram_negative_multiplier,
    arch_25_integer_flow_diagram_negative_output_to_input,
)
from .functions_1_archetypes_26_50 import (
    arch_26_fraction_input_flow_diagram_multiplication,
    arch_27_fraction_operator_flow_diagram_one_half,
    arch_28_decimal_input_flow_diagram_addition,
    arch_29_decimal_operator_flow_diagram_multiply_ten,
    arch_30_flow_diagram_with_three_sequential_inputs,
    arch_31_flow_diagram_with_three_sequential_outputs,
    arch_32_flow_diagram_matching_rule_in_words,
    arch_33_flow_diagram_translating_words_to_operators,
    arch_34_flow_diagram_writing_algebraic_formula,
    arch_35_flow_diagram_evaluating_zero_input,
    arch_36_flow_diagram_evaluating_fractional_output,
    arch_37_flow_diagram_inverse_machine_complete_reversal,
    arch_38_flow_diagram_detecting_calculation_error,
    arch_39_flow_diagram_comparing_two_different_rules_for_same_input,
    arch_40_flow_diagram_identifying_fixed_point_where_input_equals_output,
    arch_41_geometric_context_square_perimeter_flow_diagram,
    arch_42_geometric_context_cube_faces_flow_diagram,
    arch_43_financial_context_taxi_fare_fixed_plus_per_km_flow,
    arch_44_financial_context_hourly_wage_flow_diagram,
    arch_45_financial_context_cellphone_airtime_flow_diagram,
    arch_46_flow_diagram_with_squared_operator,
    arch_47_flow_diagram_square_root_operator,
    arch_48_flow_diagram_with_consecutive_multipliers_factoring,
    arch_49_flow_diagram_reverse_with_two_step_integers,
    arch_50_flow_diagram_multi_branch_input_output_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_single_operation_forward_addition": arch_01_single_operation_forward_addition,
    "02_single_operation_forward_subtraction": arch_02_single_operation_forward_subtraction,
    "03_single_operation_forward_multiplication": arch_03_single_operation_forward_multiplication,
    "04_single_operation_forward_division": arch_04_single_operation_forward_division,
    "05_single_operation_reverse_subtraction_to_addition": arch_05_single_operation_reverse_subtraction_to_addition,
    "06_single_operation_reverse_addition_to_subtraction": arch_06_single_operation_reverse_addition_to_subtraction,
    "07_single_operation_reverse_division_to_multiplication": arch_07_single_operation_reverse_division_to_multiplication,
    "08_single_operation_reverse_multiplication_to_division": arch_08_single_operation_reverse_multiplication_to_division,
    "09_two_step_rule_multiply_then_add": arch_09_two_step_rule_multiply_then_add,
    "10_two_step_rule_multiply_then_subtract": arch_10_two_step_rule_multiply_then_subtract,
    "11_two_step_rule_divide_then_add": arch_11_two_step_rule_divide_then_add,
    "12_two_step_rule_divide_then_subtract": arch_12_two_step_rule_divide_then_subtract,
    "13_two_step_rule_add_then_multiply_brackets": arch_13_two_step_rule_add_then_multiply_brackets,
    "14_two_step_rule_subtract_then_multiply_brackets": arch_14_two_step_rule_subtract_then_multiply_brackets,
    "15_two_step_reverse_multiply_add_to_input": arch_15_two_step_reverse_multiply_add_to_input,
    "16_two_step_reverse_multiply_subtract_to_input": arch_16_two_step_reverse_multiply_subtract_to_input,
    "17_two_step_reverse_divide_add_to_input": arch_17_two_step_reverse_divide_add_to_input,
    "18_two_step_reverse_brackets_rule_to_input": arch_18_two_step_reverse_brackets_rule_to_input,
    "19_identify_operator_in_single_step_diagram": arch_19_identify_operator_in_single_step_diagram,
    "20_identify_second_operator_given_first": arch_20_identify_second_operator_given_first,
    "21_equivalent_flow_diagrams_order_of_operations": arch_21_equivalent_flow_diagrams_order_of_operations,
    "22_distributive_property_in_flow_diagrams": arch_22_distributive_property_in_flow_diagrams,
    "23_integer_flow_diagram_negative_input": arch_23_integer_flow_diagram_negative_input,
    "24_integer_flow_diagram_negative_multiplier": arch_24_integer_flow_diagram_negative_multiplier,
    "25_integer_flow_diagram_negative_output_to_input": arch_25_integer_flow_diagram_negative_output_to_input,
    "26_fraction_input_flow_diagram_multiplication": arch_26_fraction_input_flow_diagram_multiplication,
    "27_fraction_operator_flow_diagram_one_half": arch_27_fraction_operator_flow_diagram_one_half,
    "28_decimal_input_flow_diagram_addition": arch_28_decimal_input_flow_diagram_addition,
    "29_decimal_operator_flow_diagram_multiply_ten": arch_29_decimal_operator_flow_diagram_multiply_ten,
    "30_flow_diagram_with_three_sequential_inputs": arch_30_flow_diagram_with_three_sequential_inputs,
    "31_flow_diagram_with_three_sequential_outputs": arch_31_flow_diagram_with_three_sequential_outputs,
    "32_flow_diagram_matching_rule_in_words": arch_32_flow_diagram_matching_rule_in_words,
    "33_flow_diagram_translating_words_to_operators": arch_33_flow_diagram_translating_words_to_operators,
    "34_flow_diagram_writing_algebraic_formula": arch_34_flow_diagram_writing_algebraic_formula,
    "35_flow_diagram_evaluating_zero_input": arch_35_flow_diagram_evaluating_zero_input,
    "36_flow_diagram_evaluating_fractional_output": arch_36_flow_diagram_evaluating_fractional_output,
    "37_flow_diagram_inverse_machine_complete_reversal": arch_37_flow_diagram_inverse_machine_complete_reversal,
    "38_flow_diagram_detecting_calculation_error": arch_38_flow_diagram_detecting_calculation_error,
    "39_flow_diagram_comparing_two_different_rules_for_same_input": arch_39_flow_diagram_comparing_two_different_rules_for_same_input,
    "40_flow_diagram_identifying_fixed_point_where_input_equals_output": arch_40_flow_diagram_identifying_fixed_point_where_input_equals_output,
    "41_geometric_context_square_perimeter_flow_diagram": arch_41_geometric_context_square_perimeter_flow_diagram,
    "42_geometric_context_cube_faces_flow_diagram": arch_42_geometric_context_cube_faces_flow_diagram,
    "43_financial_context_taxi_fare_fixed_plus_per_km_flow": arch_43_financial_context_taxi_fare_fixed_plus_per_km_flow,
    "44_financial_context_hourly_wage_flow_diagram": arch_44_financial_context_hourly_wage_flow_diagram,
    "45_financial_context_cellphone_airtime_flow_diagram": arch_45_financial_context_cellphone_airtime_flow_diagram,
    "46_flow_diagram_with_squared_operator": arch_46_flow_diagram_with_squared_operator,
    "47_flow_diagram_square_root_operator": arch_47_flow_diagram_square_root_operator,
    "48_flow_diagram_with_consecutive_multipliers_factoring": arch_48_flow_diagram_with_consecutive_multipliers_factoring,
    "49_flow_diagram_reverse_with_two_step_integers": arch_49_flow_diagram_reverse_with_two_step_integers,
    "50_flow_diagram_multi_branch_input_output_autopsy": arch_50_flow_diagram_multi_branch_input_output_autopsy,
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
