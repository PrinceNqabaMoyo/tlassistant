"""Grade 7 Mathematics - Algebraic Expressions 1 Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/04. Algebraic expressions 1.md
Focus: Algebraic language, variables, coefficients, constants, number of terms, verbal-to-algebra translation, and substitution evaluation.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .algebraic_expressions_1_archetypes_01_25 import (
    arch_01_identify_variable_in_linear_expression,
    arch_02_identify_coefficient_positive_integer,
    arch_03_identify_coefficient_negative_integer,
    arch_04_identify_coefficient_implicit_one_and_minus_one,
    arch_05_identify_constant_term_positive,
    arch_06_identify_constant_term_negative,
    arch_07_identify_constant_term_implicit_zero,
    arch_08_count_number_of_terms_monomial,
    arch_09_count_number_of_terms_binomial,
    arch_10_count_number_of_terms_trinomial,
    arch_11_algebraic_convention_multiplication_omission,
    arch_12_algebraic_convention_division_as_fraction,
    arch_13_translate_sum_and_more_than_to_algebraic_expression,
    arch_14_translate_difference_and_less_than_to_algebraic_expression,
    arch_15_translate_product_and_times_to_algebraic_expression,
    arch_16_translate_quotient_to_algebraic_expression,
    arch_17_translate_two_step_multiplication_then_addition,
    arch_18_translate_two_step_multiplication_then_subtraction,
    arch_19_translate_two_step_addition_then_multiplication_brackets,
    arch_20_translate_subtraction_order_critical_x_less_than_y,
    arch_21_evaluate_expression_single_term_substitution,
    arch_22_evaluate_linear_expression_positive_integer_substitution,
    arch_23_evaluate_linear_expression_zero_substitution,
    arch_24_evaluate_linear_expression_negative_integer_substitution,
    arch_25_evaluate_linear_expression_fractional_substitution,
)
from .algebraic_expressions_1_archetypes_26_50 import (
    arch_26_evaluate_expression_with_brackets_substitution,
    arch_27_evaluate_quadratic_term_x_squared_substitution,
    arch_28_evaluate_cubic_term_x_cubed_substitution,
    arch_29_evaluate_two_variable_expression_substitution,
    arch_30_translate_consecutive_numbers_algebraic_expression,
    arch_31_translate_even_and_odd_numbers_algebraic_representation,
    arch_32_translate_age_word_problem_to_expression,
    arch_33_translate_money_rand_cents_to_expression,
    arch_34_translate_geometric_perimeter_square_to_expression,
    arch_35_translate_geometric_perimeter_triangle_to_expression,
    arch_36_translate_geometric_area_rectangle_to_expression,
    arch_37_identify_like_vs_unlike_terms_concept,
    arch_38_identify_coefficient_in_fractional_algebraic_term,
    arch_39_identify_degree_of_linear_expression,
    arch_40_identify_degree_of_quadratic_expression,
    arch_41_expression_vs_equation_fundamental_difference,
    arch_42_evaluate_expression_table_multiple_substitutions,
    arch_43_evaluate_expression_comparing_two_expressions_same_input,
    arch_44_translate_perimeter_of_compound_shape_to_expression,
    arch_45_translate_discount_and_markup_to_expression,
    arch_46_translate_speed_distance_time_to_expression,
    arch_47_identify_parts_of_algebraic_expression_complete_anatomy,
    arch_48_detecting_algebraic_syntax_errors_misconceptions,
    arch_49_reverse_evaluation_find_input_for_given_expression_value,
    arch_50_algebraic_expression_comprehensive_diagnostic_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_identify_variable_in_linear_expression": arch_01_identify_variable_in_linear_expression,
    "02_identify_coefficient_positive_integer": arch_02_identify_coefficient_positive_integer,
    "03_identify_coefficient_negative_integer": arch_03_identify_coefficient_negative_integer,
    "04_identify_coefficient_implicit_one_and_minus_one": arch_04_identify_coefficient_implicit_one_and_minus_one,
    "05_identify_constant_term_positive": arch_05_identify_constant_term_positive,
    "06_identify_constant_term_negative": arch_06_identify_constant_term_negative,
    "07_identify_constant_term_implicit_zero": arch_07_identify_constant_term_implicit_zero,
    "08_count_number_of_terms_monomial": arch_08_count_number_of_terms_monomial,
    "09_count_number_of_terms_binomial": arch_09_count_number_of_terms_binomial,
    "10_count_number_of_terms_trinomial": arch_10_count_number_of_terms_trinomial,
    "11_algebraic_convention_multiplication_omission": arch_11_algebraic_convention_multiplication_omission,
    "12_algebraic_convention_division_as_fraction": arch_12_algebraic_convention_division_as_fraction,
    "13_translate_sum_and_more_than_to_algebraic_expression": arch_13_translate_sum_and_more_than_to_algebraic_expression,
    "14_translate_difference_and_less_than_to_algebraic_expression": arch_14_translate_difference_and_less_than_to_algebraic_expression,
    "15_translate_product_and_times_to_algebraic_expression": arch_15_translate_product_and_times_to_algebraic_expression,
    "16_translate_quotient_to_algebraic_expression": arch_16_translate_quotient_to_algebraic_expression,
    "17_translate_two_step_multiplication_then_addition": arch_17_translate_two_step_multiplication_then_addition,
    "18_translate_two_step_multiplication_then_subtraction": arch_18_translate_two_step_multiplication_then_subtraction,
    "19_translate_two_step_addition_then_multiplication_brackets": arch_19_translate_two_step_addition_then_multiplication_brackets,
    "20_translate_subtraction_order_critical_x_less_than_y": arch_20_translate_subtraction_order_critical_x_less_than_y,
    "21_evaluate_expression_single_term_substitution": arch_21_evaluate_expression_single_term_substitution,
    "22_evaluate_linear_expression_positive_integer_substitution": arch_22_evaluate_linear_expression_positive_integer_substitution,
    "23_evaluate_linear_expression_zero_substitution": arch_23_evaluate_linear_expression_zero_substitution,
    "24_evaluate_linear_expression_negative_integer_substitution": arch_24_evaluate_linear_expression_negative_integer_substitution,
    "25_evaluate_linear_expression_fractional_substitution": arch_25_evaluate_linear_expression_fractional_substitution,
    "26_evaluate_expression_with_brackets_substitution": arch_26_evaluate_expression_with_brackets_substitution,
    "27_evaluate_quadratic_term_x_squared_substitution": arch_27_evaluate_quadratic_term_x_squared_substitution,
    "28_evaluate_cubic_term_x_cubed_substitution": arch_28_evaluate_cubic_term_x_cubed_substitution,
    "29_evaluate_two_variable_expression_substitution": arch_29_evaluate_two_variable_expression_substitution,
    "30_translate_consecutive_numbers_algebraic_expression": arch_30_translate_consecutive_numbers_algebraic_expression,
    "31_translate_even_and_odd_numbers_algebraic_representation": arch_31_translate_even_and_odd_numbers_algebraic_representation,
    "32_translate_age_word_problem_to_expression": arch_32_translate_age_word_problem_to_expression,
    "33_translate_money_rand_cents_to_expression": arch_33_translate_money_rand_cents_to_expression,
    "34_translate_geometric_perimeter_square_to_expression": arch_34_translate_geometric_perimeter_square_to_expression,
    "35_translate_geometric_perimeter_triangle_to_expression": arch_35_translate_geometric_perimeter_triangle_to_expression,
    "36_translate_geometric_area_rectangle_to_expression": arch_36_translate_geometric_area_rectangle_to_expression,
    "37_identify_like_vs_unlike_terms_concept": arch_37_identify_like_vs_unlike_terms_concept,
    "38_identify_coefficient_in_fractional_algebraic_term": arch_38_identify_coefficient_in_fractional_algebraic_term,
    "39_identify_degree_of_linear_expression": arch_39_identify_degree_of_linear_expression,
    "40_identify_degree_of_quadratic_expression": arch_40_identify_degree_of_quadratic_expression,
    "41_expression_vs_equation_fundamental_difference": arch_41_expression_vs_equation_fundamental_difference,
    "42_evaluate_expression_table_multiple_substitutions": arch_42_evaluate_expression_table_multiple_substitutions,
    "43_evaluate_expression_comparing_two_expressions_same_input": arch_43_evaluate_expression_comparing_two_expressions_same_input,
    "44_translate_perimeter_of_compound_shape_to_expression": arch_44_translate_perimeter_of_compound_shape_to_expression,
    "45_translate_discount_and_markup_to_expression": arch_45_translate_discount_and_markup_to_expression,
    "46_translate_speed_distance_time_to_expression": arch_46_translate_speed_distance_time_to_expression,
    "47_identify_parts_of_algebraic_expression_complete_anatomy": arch_47_identify_parts_of_algebraic_expression_complete_anatomy,
    "48_detecting_algebraic_syntax_errors_misconceptions": arch_48_detecting_algebraic_syntax_errors_misconceptions,
    "49_reverse_evaluation_find_input_for_given_expression_value": arch_49_reverse_evaluation_find_input_for_given_expression_value,
    "50_algebraic_expression_comprehensive_diagnostic_autopsy": arch_50_algebraic_expression_comprehensive_diagnostic_autopsy,
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
