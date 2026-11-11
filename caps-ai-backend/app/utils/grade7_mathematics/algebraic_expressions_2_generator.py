"""Grade 7 Mathematics - Algebraic Expressions 2 Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/04. Algebraic expressions 2.md
Focus: Combining like terms (single, compound, multi-variable), distributive bracket expansions, geometric perimeter and area algebraic representations, fractions/decimals, powers, word problems, error traps, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .algebraic_expressions_2_archetypes_01_25 import (
    arch_01_collect_like_terms_simple_addition,
    arch_02_collect_like_terms_simple_subtraction,
    arch_03_collect_like_terms_three_linear_terms,
    arch_04_collect_like_terms_with_implicit_one_coefficient,
    arch_05_collect_like_terms_resulting_in_zero,
    arch_06_collect_like_terms_with_negative_coefficients,
    arch_07_collect_like_terms_two_variables_addition,
    arch_08_collect_like_terms_two_variables_subtraction,
    arch_09_collect_like_terms_variable_and_constant,
    arch_10_collect_like_terms_multiple_variables_and_constants,
    arch_11_distributive_law_single_bracket_positive_multiplier,
    arch_12_distributive_law_single_bracket_with_subtraction,
    arch_13_distributive_law_negative_outside_multiplier,
    arch_14_distributive_law_negative_outside_with_subtraction,
    arch_15_distributive_law_variable_multiplier_x_times_x,
    arch_16_expand_and_simplify_bracket_plus_term,
    arch_17_expand_and_simplify_bracket_minus_term,
    arch_18_expand_and_simplify_term_minus_bracket,
    arch_19_expand_and_simplify_two_added_brackets,
    arch_20_expand_and_simplify_two_subtracted_brackets,
    arch_21_equivalent_expressions_verify_by_simplification,
    arch_22_equivalent_expressions_verify_by_substitution,
    arch_23_equivalent_expressions_identify_from_four_choices,
    arch_24_perimeter_of_triangle_algebraic_simplification,
    arch_25_perimeter_of_rectangle_algebraic_simplification,
)
from .algebraic_expressions_2_archetypes_26_50 import (
    arch_26_perimeter_of_square_algebraic_simplification,
    arch_27_perimeter_of_equilateral_triangle_algebraic,
    arch_28_perimeter_of_regular_pentagon_algebraic,
    arch_29_perimeter_of_regular_hexagon_algebraic,
    arch_30_perimeter_of_composite_l_shape_algebraic,
    arch_31_area_of_rectangle_monomial_by_binomial,
    arch_32_area_of_square_algebraic_side_length,
    arch_33_fractional_coefficients_collecting_like_terms,
    arch_34_fractional_coefficients_subtraction,
    arch_35_decimal_coefficients_addition,
    arch_36_decimal_coefficients_subtraction,
    arch_37_like_terms_with_squared_variables,
    arch_38_distinguishing_x_and_x_squared_terms,
    arch_39_cubed_and_squared_terms_combining,
    arch_40_algebraic_word_problem_consecutive_integers,
    arch_41_algebraic_word_problem_ages_in_years,
    arch_42_algebraic_word_problem_shopping_cost,
    arch_43_algebraic_word_problem_travel_distance,
    arch_44_substitution_into_simplified_expression,
    arch_45_verify_algebraic_identity_for_multiple_values,
    arch_46_common_error_adding_unlike_terms_trap,
    arch_47_common_error_distributive_law_omission_trap,
    arch_48_common_error_sign_change_subtraction_trap,
    arch_49_nested_algebraic_simplification,
    arch_50_algebraic_expressions_2_comprehensive_diagnostic_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_collect_like_terms_simple_addition": arch_01_collect_like_terms_simple_addition,
    "02_collect_like_terms_simple_subtraction": arch_02_collect_like_terms_simple_subtraction,
    "03_collect_like_terms_three_linear_terms": arch_03_collect_like_terms_three_linear_terms,
    "04_collect_like_terms_with_implicit_one_coefficient": arch_04_collect_like_terms_with_implicit_one_coefficient,
    "05_collect_like_terms_resulting_in_zero": arch_05_collect_like_terms_resulting_in_zero,
    "06_collect_like_terms_with_negative_coefficients": arch_06_collect_like_terms_with_negative_coefficients,
    "07_collect_like_terms_two_variables_addition": arch_07_collect_like_terms_two_variables_addition,
    "08_collect_like_terms_two_variables_subtraction": arch_08_collect_like_terms_two_variables_subtraction,
    "09_collect_like_terms_variable_and_constant": arch_09_collect_like_terms_variable_and_constant,
    "10_collect_like_terms_multiple_variables_and_constants": arch_10_collect_like_terms_multiple_variables_and_constants,
    "11_distributive_law_single_bracket_positive_multiplier": arch_11_distributive_law_single_bracket_positive_multiplier,
    "12_distributive_law_single_bracket_with_subtraction": arch_12_distributive_law_single_bracket_with_subtraction,
    "13_distributive_law_negative_outside_multiplier": arch_13_distributive_law_negative_outside_multiplier,
    "14_distributive_law_negative_outside_with_subtraction": arch_14_distributive_law_negative_outside_with_subtraction,
    "15_distributive_law_variable_multiplier_x_times_x": arch_15_distributive_law_variable_multiplier_x_times_x,
    "16_expand_and_simplify_bracket_plus_term": arch_16_expand_and_simplify_bracket_plus_term,
    "17_expand_and_simplify_bracket_minus_term": arch_17_expand_and_simplify_bracket_minus_term,
    "18_expand_and_simplify_term_minus_bracket": arch_18_expand_and_simplify_term_minus_bracket,
    "19_expand_and_simplify_two_added_brackets": arch_19_expand_and_simplify_two_added_brackets,
    "20_expand_and_simplify_two_subtracted_brackets": arch_20_expand_and_simplify_two_subtracted_brackets,
    "21_equivalent_expressions_verify_by_simplification": arch_21_equivalent_expressions_verify_by_simplification,
    "22_equivalent_expressions_verify_by_substitution": arch_22_equivalent_expressions_verify_by_substitution,
    "23_equivalent_expressions_identify_from_four_choices": arch_23_equivalent_expressions_identify_from_four_choices,
    "24_perimeter_of_triangle_algebraic_simplification": arch_24_perimeter_of_triangle_algebraic_simplification,
    "25_perimeter_of_rectangle_algebraic_simplification": arch_25_perimeter_of_rectangle_algebraic_simplification,
    "26_perimeter_of_square_algebraic_simplification": arch_26_perimeter_of_square_algebraic_simplification,
    "27_perimeter_of_equilateral_triangle_algebraic": arch_27_perimeter_of_equilateral_triangle_algebraic,
    "28_perimeter_of_regular_pentagon_algebraic": arch_28_perimeter_of_regular_pentagon_algebraic,
    "29_perimeter_of_regular_hexagon_algebraic": arch_29_perimeter_of_regular_hexagon_algebraic,
    "30_perimeter_of_composite_l_shape_algebraic": arch_30_perimeter_of_composite_l_shape_algebraic,
    "31_area_of_rectangle_monomial_by_binomial": arch_31_area_of_rectangle_monomial_by_binomial,
    "32_area_of_square_algebraic_side_length": arch_32_area_of_square_algebraic_side_length,
    "33_fractional_coefficients_collecting_like_terms": arch_33_fractional_coefficients_collecting_like_terms,
    "34_fractional_coefficients_subtraction": arch_34_fractional_coefficients_subtraction,
    "35_decimal_coefficients_addition": arch_35_decimal_coefficients_addition,
    "36_decimal_coefficients_subtraction": arch_36_decimal_coefficients_subtraction,
    "37_like_terms_with_squared_variables": arch_37_like_terms_with_squared_variables,
    "38_distinguishing_x_and_x_squared_terms": arch_38_distinguishing_x_and_x_squared_terms,
    "39_cubed_and_squared_terms_combining": arch_39_cubed_and_squared_terms_combining,
    "40_algebraic_word_problem_consecutive_integers": arch_40_algebraic_word_problem_consecutive_integers,
    "41_algebraic_word_problem_ages_in_years": arch_41_algebraic_word_problem_ages_in_years,
    "42_algebraic_word_problem_shopping_cost": arch_42_algebraic_word_problem_shopping_cost,
    "43_algebraic_word_problem_travel_distance": arch_43_algebraic_word_problem_travel_distance,
    "44_substitution_into_simplified_expression": arch_44_substitution_into_simplified_expression,
    "45_verify_algebraic_identity_for_multiple_values": arch_45_verify_algebraic_identity_for_multiple_values,
    "46_common_error_adding_unlike_terms_trap": arch_46_common_error_adding_unlike_terms_trap,
    "47_common_error_distributive_law_omission_trap": arch_47_common_error_distributive_law_omission_trap,
    "48_common_error_sign_change_subtraction_trap": arch_48_common_error_sign_change_subtraction_trap,
    "49_nested_algebraic_simplification": arch_49_nested_algebraic_simplification,
    "50_algebraic_expressions_2_comprehensive_diagnostic_autopsy": arch_50_algebraic_expressions_2_comprehensive_diagnostic_autopsy,
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
