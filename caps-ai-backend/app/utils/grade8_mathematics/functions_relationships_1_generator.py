"""
Grade 8 Mathematics - Functions and Relationships 1 Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Functions and relationships 1.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .functions_1_archetypes_01_25 import (
    arch_01_single_step_flow_diagram_multiplication,
    arch_02_single_step_flow_diagram_addition,
    arch_03_two_step_flow_diagram_multiply_then_add,
    arch_04_two_step_flow_diagram_multiply_then_subtract,
    arch_05_two_step_flow_diagram_add_then_multiply_brackets,
    arch_06_two_step_flow_diagram_divide_then_add,
    arch_07_flow_diagram_with_negative_integer_inputs,
    arch_08_flow_diagram_with_fractional_inputs,
    arch_09_flow_diagram_with_decimal_inputs,
    arch_10_inverse_flow_diagram_one_step_reversal,
    arch_11_inverse_flow_diagram_two_step_subtraction_then_division,
    arch_12_inverse_flow_diagram_addition_then_division,
    arch_13_equivalent_flow_diagrams_order_of_operations_comparison,
    arch_14_equivalent_flow_diagrams_distributive_equivalence,
    arch_15_deducing_missing_multiplier_in_flow_diagram,
    arch_16_deducing_missing_constant_in_flow_diagram,
    arch_17_deducing_two_missing_operators_from_input_output_pairs,
    arch_18_completing_table_outputs_from_linear_rule_positive_coeff,
    arch_19_completing_table_outputs_from_linear_rule_negative_coeff,
    arch_20_completing_table_inputs_from_outputs_using_inverses,
    arch_21_completing_mixed_table_both_inputs_and_outputs,
    arch_22_identifying_independent_and_dependent_variables_in_context,
    arch_23_formulating_algebraic_rule_from_two_column_table,
    arch_24_formulating_rule_with_fractional_rate_from_table,
    arch_25_testing_which_formula_matches_a_given_table,
)

from .functions_1_archetypes_26_50 import (
    arch_26_equivalent_formulae_expansion_verification,
    arch_27_equivalent_formulae_subtraction_factored_form,
    arch_28_quadratic_function_table_evaluation,
    arch_29_quadratic_function_calculating_input_from_square_output,
    arch_30_inverse_proportion_table_evaluation,
    arch_31_inverse_proportion_constant_product_rule,
    arch_32_unit_conversion_hours_to_minutes_function,
    arch_33_unit_conversion_kilometers_to_meters_function,
    arch_34_unit_conversion_litres_to_millilitres_function,
    arch_35_temperature_conversion_formula_evaluation,
    arch_36_distance_speed_time_direct_formula_d_vt,
    arch_37_cost_function_fixed_fee_plus_rate_per_kg,
    arch_38_cost_function_hire_purchase_deposit_plus_monthly,
    arch_39_geometric_arrangement_red_and_black_squares_formula,
    arch_40_geometric_tile_arrangement_formula_matching,
    arch_41_linear_function_rate_of_change_gradient_concept,
    arch_42_linear_function_constant_term_zero_input_intercept,
    arch_43_finding_output_for_large_input_in_function,
    arch_44_finding_input_for_large_output_in_function,
    arch_45_comparing_two_competing_linear_functions,
    arch_46_break_even_input_value_for_two_linear_plans,
    arch_47_evaluating_composite_function_two_stage_rule,
    arch_48_function_machine_black_box_mystery_rule,
    arch_49_distinguishing_linear_vs_non_linear_relationships_from_tables,
    arch_50_multiple_representations_verbal_table_formula_mapping,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10
    arch_01_single_step_flow_diagram_multiplication,
    arch_02_single_step_flow_diagram_addition,
    arch_03_two_step_flow_diagram_multiply_then_add,
    arch_04_two_step_flow_diagram_multiply_then_subtract,
    arch_05_two_step_flow_diagram_add_then_multiply_brackets,
    arch_06_two_step_flow_diagram_divide_then_add,
    arch_07_flow_diagram_with_negative_integer_inputs,
    arch_08_flow_diagram_with_fractional_inputs,
    arch_09_flow_diagram_with_decimal_inputs,
    arch_10_inverse_flow_diagram_one_step_reversal,
    # 11 - 20
    arch_11_inverse_flow_diagram_two_step_subtraction_then_division,
    arch_12_inverse_flow_diagram_addition_then_division,
    arch_13_equivalent_flow_diagrams_order_of_operations_comparison,
    arch_14_equivalent_flow_diagrams_distributive_equivalence,
    arch_15_deducing_missing_multiplier_in_flow_diagram,
    arch_16_deducing_missing_constant_in_flow_diagram,
    arch_17_deducing_two_missing_operators_from_input_output_pairs,
    arch_18_completing_table_outputs_from_linear_rule_positive_coeff,
    arch_19_completing_table_outputs_from_linear_rule_negative_coeff,
    arch_20_completing_table_inputs_from_outputs_using_inverses,
    # 21 - 28
    arch_21_completing_mixed_table_both_inputs_and_outputs,
    arch_22_identifying_independent_and_dependent_variables_in_context,
    arch_23_formulating_algebraic_rule_from_two_column_table,
    arch_24_formulating_rule_with_fractional_rate_from_table,
    arch_25_testing_which_formula_matches_a_given_table,
    arch_26_equivalent_formulae_expansion_verification,
    arch_27_equivalent_formulae_subtraction_factored_form,
    arch_28_quadratic_function_table_evaluation,
    # 29 - 36
    arch_29_quadratic_function_calculating_input_from_square_output,
    arch_30_inverse_proportion_table_evaluation,
    arch_31_inverse_proportion_constant_product_rule,
    arch_32_unit_conversion_hours_to_minutes_function,
    arch_33_unit_conversion_kilometers_to_meters_function,
    arch_34_unit_conversion_litres_to_millilitres_function,
    arch_35_temperature_conversion_formula_evaluation,
    arch_36_distance_speed_time_direct_formula_d_vt,
    # 37 - 44
    arch_37_cost_function_fixed_fee_plus_rate_per_kg,
    arch_38_cost_function_hire_purchase_deposit_plus_monthly,
    arch_39_geometric_arrangement_red_and_black_squares_formula,
    arch_40_geometric_tile_arrangement_formula_matching,
    arch_41_linear_function_rate_of_change_gradient_concept,
    arch_42_linear_function_constant_term_zero_input_intercept,
    arch_43_finding_output_for_large_input_in_function,
    arch_44_finding_input_for_large_output_in_function,
    # 45 - 50
    arch_45_comparing_two_competing_linear_functions,
    arch_46_break_even_input_value_for_two_linear_plans,
    arch_47_evaluating_composite_function_two_stage_rule,
    arch_48_function_machine_black_box_mystery_rule,
    arch_49_distinguishing_linear_vs_non_linear_relationships_from_tables,
    arch_50_multiple_representations_verbal_table_formula_mapping,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_single_step_flow_diagram_multiplication",
    "02_single_step_flow_diagram_addition",
    "03_two_step_flow_diagram_multiply_then_add",
    "04_two_step_flow_diagram_multiply_then_subtract",
    "05_two_step_flow_diagram_add_then_multiply_brackets",
    "06_two_step_flow_diagram_divide_then_add",
    "07_flow_diagram_with_negative_integer_inputs",
    "08_flow_diagram_with_fractional_inputs",
    "09_flow_diagram_with_decimal_inputs",
    "10_inverse_flow_diagram_one_step_reversal",
    # 11 - 20
    "11_inverse_flow_diagram_two_step_subtraction_then_division",
    "12_inverse_flow_diagram_addition_then_division",
    "13_equivalent_flow_diagrams_order_of_operations_comparison",
    "14_equivalent_flow_diagrams_distributive_equivalence",
    "15_deducing_missing_multiplier_in_flow_diagram",
    "16_deducing_missing_constant_in_flow_diagram",
    "17_deducing_two_missing_operators_from_input_output_pairs",
    "18_completing_table_outputs_from_linear_rule_positive_coeff",
    "19_completing_table_outputs_from_linear_rule_negative_coeff",
    "20_completing_table_inputs_from_outputs_using_inverses",
    # 21 - 28
    "21_completing_mixed_table_both_inputs_and_outputs",
    "22_identifying_independent_and_dependent_variables_in_context",
    "23_formulating_algebraic_rule_from_two_column_table",
    "24_formulating_rule_with_fractional_rate_from_table",
    "25_testing_which_formula_matches_a_given_table",
    "26_equivalent_formulae_expansion_verification",
    "27_equivalent_formulae_subtraction_factored_form",
    "28_quadratic_function_table_evaluation",
    # 29 - 36
    "29_quadratic_function_calculating_input_from_square_output",
    "30_inverse_proportion_table_evaluation",
    "31_inverse_proportion_constant_product_rule",
    "32_unit_conversion_hours_to_minutes_function",
    "33_unit_conversion_kilometers_to_meters_function",
    "34_unit_conversion_litres_to_millilitres_function",
    "35_temperature_conversion_formula_evaluation",
    "36_distance_speed_time_direct_formula_d_vt",
    # 37 - 44
    "37_cost_function_fixed_fee_plus_rate_per_kg",
    "38_cost_function_hire_purchase_deposit_plus_monthly",
    "39_geometric_arrangement_red_and_black_squares_formula",
    "40_geometric_tile_arrangement_formula_matching",
    "41_linear_function_rate_of_change_gradient_concept",
    "42_linear_function_constant_term_zero_input_intercept",
    "43_finding_output_for_large_input_in_function",
    "44_finding_input_for_large_output_in_function",
    # 45 - 50
    "45_comparing_two_competing_linear_functions",
    "46_break_even_input_value_for_two_linear_plans",
    "47_evaluating_composite_function_two_stage_rule",
    "48_function_machine_black_box_mystery_rule",
    "49_distinguishing_linear_vs_non_linear_relationships_from_tables",
    "50_multiple_representations_verbal_table_formula_mapping",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases
DISPATCH_TABLE["flow_diagram"] = arch_03_two_step_flow_diagram_multiply_then_add
DISPATCH_TABLE["table"] = arch_18_completing_table_outputs_from_linear_rule_positive_coeff
DISPATCH_TABLE["formula"] = arch_23_formulating_algebraic_rule_from_two_column_table
DISPATCH_TABLE["inverse"] = arch_11_inverse_flow_diagram_two_step_subtraction_then_division


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
        q.setdefault("topic", "Functions and relationships 1")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
