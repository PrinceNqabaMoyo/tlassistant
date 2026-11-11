"""Grade 9 Mathematics - Integers Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 1/02. Integers.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .integers_archetypes_01_25 import (
    arch_01_integer_number_line_plotting_and_ordering,
    arch_02_integer_additive_inverse_concept,
    arch_03_thermometer_temperature_reading_negative_celsius,
    arch_04_temperature_change_drop_and_rise_calculation,
    arch_05_elevation_and_depth_sea_level_difference,
    arch_06_financial_bank_balance_overdraft_deposit_withdrawal,
    arch_07_addition_of_two_negative_integers,
    arch_08_addition_of_positive_and_negative_integer,
    arch_09_subtraction_positive_minus_larger_positive,
    arch_10_subtraction_of_negative_integer_double_negative_rule,
    arch_11_subtraction_negative_minus_positive_integer,
    arch_12_subtraction_negative_minus_negative_integer,
    arch_13_mixed_addition_and_subtraction_three_terms,
    arch_14_mixed_addition_and_subtraction_four_terms,
    arch_15_multiplication_positive_times_negative_integer,
    arch_16_multiplication_negative_times_negative_integer,
    arch_17_multiplication_three_signed_integers_odd_negatives,
    arch_18_multiplication_four_signed_integers_even_negatives,
    arch_19_division_negative_divided_by_positive_integer,
    arch_20_division_positive_divided_by_negative_integer,
    arch_21_division_negative_divided_by_negative_integer,
    arch_22_combined_multiplication_and_division_of_signed_integers,
    arch_23_properties_distributive_law_with_negative_multiplier,
    arch_24_properties_commutative_and_associative_signed_integers,
    arch_25_difference_between_integers_distance_on_number_line,
)
from .integers_archetypes_26_50 import (
    arch_26_power_of_negative_integer_even_exponent,
    arch_27_power_of_negative_integer_odd_exponent,
    arch_28_distinguish_bracketed_power_vs_unbracketed_negation,
    arch_29_square_root_with_negative_sign_outside_radical,
    arch_30_cube_root_of_negative_integer,
    arch_31_combined_powers_and_roots_of_negative_integers,
    arch_32_order_of_operations_brackets_and_multiplication_with_integers,
    arch_33_order_of_operations_nested_brackets_and_negatives,
    arch_34_order_of_operations_powers_before_multiplication_signed,
    arch_35_fractional_expression_signed_numerator_and_denominator,
    arch_36_fractional_expression_order_of_operations_with_roots,
    arch_37_algebraic_substitution_linear_expression_negative_variable,
    arch_38_algebraic_substitution_quadratic_expression_negative_variable,
    arch_39_algebraic_substitution_cubic_and_powers_negative_variable,
    arch_40_algebraic_substitution_two_negative_variables,
    arch_41_solve_simple_linear_equation_negative_coefficients,
    arch_42_solve_linear_equation_negative_variables_both_sides,
    arch_43_integer_magic_square_or_grid_row_column_sum,
    arch_44_integer_consecutive_sum_problem_negative_integers,
    arch_45_submarine_depth_and_ascent_context_problem,
    arch_46_mine_shaft_elevation_lift_movement_problem,
    arch_47_error_analysis_diagnosing_double_negative_subtraction_error,
    arch_48_error_analysis_diagnosing_power_bracket_sign_error,
    arch_49_error_analysis_diagnosing_bodmas_addition_before_multiplication_error,
    arch_50_compound_multi_step_integer_expression_evaluation,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_integer_number_line_plotting_and_ordering": arch_01_integer_number_line_plotting_and_ordering,
    "02_integer_additive_inverse_concept": arch_02_integer_additive_inverse_concept,
    "03_thermometer_temperature_reading_negative_celsius": arch_03_thermometer_temperature_reading_negative_celsius,
    "04_temperature_change_drop_and_rise_calculation": arch_04_temperature_change_drop_and_rise_calculation,
    "05_elevation_and_depth_sea_level_difference": arch_05_elevation_and_depth_sea_level_difference,
    "06_financial_bank_balance_overdraft_deposit_withdrawal": arch_06_financial_bank_balance_overdraft_deposit_withdrawal,
    "07_addition_of_two_negative_integers": arch_07_addition_of_two_negative_integers,
    "08_addition_of_positive_and_negative_integer": arch_08_addition_of_positive_and_negative_integer,
    "09_subtraction_positive_minus_larger_positive": arch_09_subtraction_positive_minus_larger_positive,
    "10_subtraction_of_negative_integer_double_negative_rule": arch_10_subtraction_of_negative_integer_double_negative_rule,
    "11_subtraction_negative_minus_positive_integer": arch_11_subtraction_negative_minus_positive_integer,
    "12_subtraction_negative_minus_negative_integer": arch_12_subtraction_negative_minus_negative_integer,
    "13_mixed_addition_and_subtraction_three_terms": arch_13_mixed_addition_and_subtraction_three_terms,
    "14_mixed_addition_and_subtraction_four_terms": arch_14_mixed_addition_and_subtraction_four_terms,
    "15_multiplication_positive_times_negative_integer": arch_15_multiplication_positive_times_negative_integer,
    "16_multiplication_negative_times_negative_integer": arch_16_multiplication_negative_times_negative_integer,
    "17_multiplication_three_signed_integers_odd_negatives": arch_17_multiplication_three_signed_integers_odd_negatives,
    "18_multiplication_four_signed_integers_even_negatives": arch_18_multiplication_four_signed_integers_even_negatives,
    "19_division_negative_divided_by_positive_integer": arch_19_division_negative_divided_by_positive_integer,
    "20_division_positive_divided_by_negative_integer": arch_20_division_positive_divided_by_negative_integer,
    "21_division_negative_divided_by_negative_integer": arch_21_division_negative_divided_by_negative_integer,
    "22_combined_multiplication_and_division_of_signed_integers": arch_22_combined_multiplication_and_division_of_signed_integers,
    "23_properties_distributive_law_with_negative_multiplier": arch_23_properties_distributive_law_with_negative_multiplier,
    "24_properties_commutative_and_associative_signed_integers": arch_24_properties_commutative_and_associative_signed_integers,
    "25_difference_between_integers_distance_on_number_line": arch_25_difference_between_integers_distance_on_number_line,
    "26_power_of_negative_integer_even_exponent": arch_26_power_of_negative_integer_even_exponent,
    "27_power_of_negative_integer_odd_exponent": arch_27_power_of_negative_integer_odd_exponent,
    "28_distinguish_bracketed_power_vs_unbracketed_negation": arch_28_distinguish_bracketed_power_vs_unbracketed_negation,
    "29_square_root_with_negative_sign_outside_radical": arch_29_square_root_with_negative_sign_outside_radical,
    "30_cube_root_of_negative_integer": arch_30_cube_root_of_negative_integer,
    "31_combined_powers_and_roots_of_negative_integers": arch_31_combined_powers_and_roots_of_negative_integers,
    "32_order_of_operations_brackets_and_multiplication_with_integers": arch_32_order_of_operations_brackets_and_multiplication_with_integers,
    "33_order_of_operations_nested_brackets_and_negatives": arch_33_order_of_operations_nested_brackets_and_negatives,
    "34_order_of_operations_powers_before_multiplication_signed": arch_34_order_of_operations_powers_before_multiplication_signed,
    "35_fractional_expression_signed_numerator_and_denominator": arch_35_fractional_expression_signed_numerator_and_denominator,
    "36_fractional_expression_order_of_operations_with_roots": arch_36_fractional_expression_order_of_operations_with_roots,
    "37_algebraic_substitution_linear_expression_negative_variable": arch_37_algebraic_substitution_linear_expression_negative_variable,
    "38_algebraic_substitution_quadratic_expression_negative_variable": arch_38_algebraic_substitution_quadratic_expression_negative_variable,
    "39_algebraic_substitution_cubic_and_powers_negative_variable": arch_39_algebraic_substitution_cubic_and_powers_negative_variable,
    "40_algebraic_substitution_two_negative_variables": arch_40_algebraic_substitution_two_negative_variables,
    "41_solve_simple_linear_equation_negative_coefficients": arch_41_solve_simple_linear_equation_negative_coefficients,
    "42_solve_linear_equation_negative_variables_both_sides": arch_42_solve_linear_equation_negative_variables_both_sides,
    "43_integer_magic_square_or_grid_row_column_sum": arch_43_integer_magic_square_or_grid_row_column_sum,
    "44_integer_consecutive_sum_problem_negative_integers": arch_44_integer_consecutive_sum_problem_negative_integers,
    "45_submarine_depth_and_ascent_context_problem": arch_45_submarine_depth_and_ascent_context_problem,
    "46_mine_shaft_elevation_lift_movement_problem": arch_46_mine_shaft_elevation_lift_movement_problem,
    "47_error_analysis_diagnosing_double_negative_subtraction_error": arch_47_error_analysis_diagnosing_double_negative_subtraction_error,
    "48_error_analysis_diagnosing_power_bracket_sign_error": arch_48_error_analysis_diagnosing_power_bracket_sign_error,
    "49_error_analysis_diagnosing_bodmas_addition_before_multiplication_error": arch_49_error_analysis_diagnosing_bodmas_addition_before_multiplication_error,
    "50_compound_multi_step_integer_expression_evaluation": arch_50_compound_multi_step_integer_expression_evaluation,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())


def generate_grade9_integers_question(
    rng: Optional[random.Random] = None,
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    if rng is None:
        rng = random.Random()

    builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None
    if subskill:
        s_clean = str(subskill).strip()
        if s_clean in ARCHETYPE_MAP:
            builder = ARCHETYPE_MAP[s_clean]
        else:
            for k, b in ARCHETYPE_MAP.items():
                if k.startswith(s_clean) or s_clean in k:
                    builder = b
                    break

    if builder is None:
        builder = rng.choice(list(ARCHETYPE_MAP.values()))

    q = builder(rng)
    q["grade"] = 9
    q["subject"] = "Mathematics"
    q["topic"] = "Integers"
    q["term"] = 1
    q.setdefault("caps_weight_percent", 10)
    q.setdefault("suggested_duration_mins", 45)
    return q


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(count):
        questions.append(generate_grade9_integers_question(rng=rng, subskill=subskill))

    return questions


__all__ = [
    "ARCHETYPE_MAP",
    "SUBSKILLS",
    "generate",
    "generate_grade9_integers_question",
]
