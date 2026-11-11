"""Grade 9 Mathematics - Factorisation & Algebraic Expressions 2 Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 1/06. Algebraic expressions 2.md
  curriculum_docs/Mathematics_Gr9/Algebraic Expressions Studio.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .factorisation_archetypes_01_25 import (
    arch_01_hcf_numerical_monomial_extraction,
    arch_02_hcf_variable_monomial_extraction,
    arch_03_hcf_combined_numerical_and_variable,
    arch_04_hcf_negative_leading_coefficient_extraction,
    arch_05_hcf_trinomial_common_factor,
    arch_06_hcf_binomial_bracket_common_factor,
    arch_07_hcf_binomial_bracket_with_negative_sign,
    arch_08_hcf_bracket_sign_change_rule,
    arch_09_difference_of_two_squares_basic,
    arch_10_difference_of_two_squares_large_perfect_square,
    arch_11_difference_of_two_squares_with_leading_coefficient,
    arch_12_difference_of_two_squares_two_variables,
    arch_13_difference_of_two_squares_higher_even_power,
    arch_14_common_factor_first_then_difference_of_squares,
    arch_15_trinomial_factorisation_positive_sum_positive_product,
    arch_16_trinomial_factorisation_negative_sum_positive_product,
    arch_17_trinomial_factorisation_positive_sum_negative_product,
    arch_18_trinomial_factorisation_negative_sum_negative_product,
    arch_19_trinomial_factorisation_perfect_square_sum,
    arch_20_trinomial_factorisation_perfect_square_difference,
    arch_21_common_factor_first_then_trinomial_factorisation,
    arch_22_negative_common_factor_then_trinomial,
    arch_23_factorise_by_grouping_four_terms_basic,
    arch_24_factorise_by_grouping_with_negative_middle_terms,
    arch_25_factorise_by_grouping_with_sign_change_needed,
)
from .factorisation_archetypes_26_50 import (
    arch_26_factorise_by_grouping_requiring_rearrangement,
    arch_27_algebraic_fraction_simplify_monomial_over_monomial,
    arch_28_algebraic_fraction_common_factor_numerator_cancel,
    arch_29_algebraic_fraction_common_factor_cancel_binomial,
    arch_30_algebraic_fraction_difference_of_squares_cancel,
    arch_31_algebraic_fraction_difference_of_squares_cancel_plus,
    arch_32_algebraic_fraction_trinomial_cancel_numerator,
    arch_33_algebraic_fraction_trinomial_cancel_denominator,
    arch_34_algebraic_fraction_trinomial_over_trinomial_cancel,
    arch_35_algebraic_fraction_sign_change_cancellation,
    arch_36_algebraic_fraction_multiplication_cancel_common_factors,
    arch_37_algebraic_fraction_division_multiply_by_reciprocal,
    arch_38_algebraic_fraction_addition_like_denominators,
    arch_39_algebraic_fraction_subtraction_like_denominators,
    arch_40_algebraic_fraction_addition_monomial_denominators_lcd,
    arch_41_algebraic_fraction_subtraction_monomial_denominators_lcd,
    arch_42_algebraic_tile_area_model_find_missing_binomial_dimension,
    arch_43_geometric_application_find_width_given_area_and_length,
    arch_44_geometric_application_square_area_to_side_length,
    arch_45_error_analysis_diagnosing_illegal_fraction_term_canceling,
    arch_46_error_analysis_diagnosing_difference_of_squares_sign_error,
    arch_47_error_analysis_diagnosing_wrong_factors_in_trinomial,
    arch_48_evaluate_factored_expression_numerical_shortcut,
    arch_49_compound_factorisation_difference_of_squares_with_binomial_terms,
    arch_50_compound_multi_step_factorisation_and_simplification_challenge,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_hcf_numerical_monomial_extraction": arch_01_hcf_numerical_monomial_extraction,
    "02_hcf_variable_monomial_extraction": arch_02_hcf_variable_monomial_extraction,
    "03_hcf_combined_numerical_and_variable": arch_03_hcf_combined_numerical_and_variable,
    "04_hcf_negative_leading_coefficient_extraction": arch_04_hcf_negative_leading_coefficient_extraction,
    "05_hcf_trinomial_common_factor": arch_05_hcf_trinomial_common_factor,
    "06_hcf_binomial_bracket_common_factor": arch_06_hcf_binomial_bracket_common_factor,
    "07_hcf_binomial_bracket_with_negative_sign": arch_07_hcf_binomial_bracket_with_negative_sign,
    "08_hcf_bracket_sign_change_rule": arch_08_hcf_bracket_sign_change_rule,
    "09_difference_of_two_squares_basic": arch_09_difference_of_two_squares_basic,
    "10_difference_of_two_squares_large_perfect_square": arch_10_difference_of_two_squares_large_perfect_square,
    "11_difference_of_two_squares_with_leading_coefficient": arch_11_difference_of_two_squares_with_leading_coefficient,
    "12_difference_of_two_squares_two_variables": arch_12_difference_of_two_squares_two_variables,
    "13_difference_of_two_squares_higher_even_power": arch_13_difference_of_two_squares_higher_even_power,
    "14_common_factor_first_then_difference_of_squares": arch_14_common_factor_first_then_difference_of_squares,
    "15_trinomial_factorisation_positive_sum_positive_product": arch_15_trinomial_factorisation_positive_sum_positive_product,
    "16_trinomial_factorisation_negative_sum_positive_product": arch_16_trinomial_factorisation_negative_sum_positive_product,
    "17_trinomial_factorisation_positive_sum_negative_product": arch_17_trinomial_factorisation_positive_sum_negative_product,
    "18_trinomial_factorisation_negative_sum_negative_product": arch_18_trinomial_factorisation_negative_sum_negative_product,
    "19_trinomial_factorisation_perfect_square_sum": arch_19_trinomial_factorisation_perfect_square_sum,
    "20_trinomial_factorisation_perfect_square_difference": arch_20_trinomial_factorisation_perfect_square_difference,
    "21_common_factor_first_then_trinomial_factorisation": arch_21_common_factor_first_then_trinomial_factorisation,
    "22_negative_common_factor_then_trinomial": arch_22_negative_common_factor_then_trinomial,
    "23_factorise_by_grouping_four_terms_basic": arch_23_factorise_by_grouping_four_terms_basic,
    "24_factorise_by_grouping_with_negative_middle_terms": arch_24_factorise_by_grouping_with_negative_middle_terms,
    "25_factorise_by_grouping_with_sign_change_needed": arch_25_factorise_by_grouping_with_sign_change_needed,
    "26_factorise_by_grouping_requiring_rearrangement": arch_26_factorise_by_grouping_requiring_rearrangement,
    "27_algebraic_fraction_simplify_monomial_over_monomial": arch_27_algebraic_fraction_simplify_monomial_over_monomial,
    "28_algebraic_fraction_common_factor_numerator_cancel": arch_28_algebraic_fraction_common_factor_numerator_cancel,
    "29_algebraic_fraction_common_factor_cancel_binomial": arch_29_algebraic_fraction_common_factor_cancel_binomial,
    "30_algebraic_fraction_difference_of_squares_cancel": arch_30_algebraic_fraction_difference_of_squares_cancel,
    "31_algebraic_fraction_difference_of_squares_cancel_plus": arch_31_algebraic_fraction_difference_of_squares_cancel_plus,
    "32_algebraic_fraction_trinomial_cancel_numerator": arch_32_algebraic_fraction_trinomial_cancel_numerator,
    "33_algebraic_fraction_trinomial_cancel_denominator": arch_33_algebraic_fraction_trinomial_cancel_denominator,
    "34_algebraic_fraction_trinomial_over_trinomial_cancel": arch_34_algebraic_fraction_trinomial_over_trinomial_cancel,
    "35_algebraic_fraction_sign_change_cancellation": arch_35_algebraic_fraction_sign_change_cancellation,
    "36_algebraic_fraction_multiplication_cancel_common_factors": arch_36_algebraic_fraction_multiplication_cancel_common_factors,
    "37_algebraic_fraction_division_multiply_by_reciprocal": arch_37_algebraic_fraction_division_multiply_by_reciprocal,
    "38_algebraic_fraction_addition_like_denominators": arch_38_algebraic_fraction_addition_like_denominators,
    "39_algebraic_fraction_subtraction_like_denominators": arch_39_algebraic_fraction_subtraction_like_denominators,
    "40_algebraic_fraction_addition_monomial_denominators_lcd": arch_40_algebraic_fraction_addition_monomial_denominators_lcd,
    "41_algebraic_fraction_subtraction_monomial_denominators_lcd": arch_41_algebraic_fraction_subtraction_monomial_denominators_lcd,
    "42_algebraic_tile_area_model_find_missing_binomial_dimension": arch_42_algebraic_tile_area_model_find_missing_binomial_dimension,
    "43_geometric_application_find_width_given_area_and_length": arch_43_geometric_application_find_width_given_area_and_length,
    "44_geometric_application_square_area_to_side_length": arch_44_geometric_application_square_area_to_side_length,
    "45_error_analysis_diagnosing_illegal_fraction_term_canceling": arch_45_error_analysis_diagnosing_illegal_fraction_term_canceling,
    "46_error_analysis_diagnosing_difference_of_squares_sign_error": arch_46_error_analysis_diagnosing_difference_of_squares_sign_error,
    "47_error_analysis_diagnosing_wrong_factors_in_trinomial": arch_47_error_analysis_diagnosing_wrong_factors_in_trinomial,
    "48_evaluate_factored_expression_numerical_shortcut": arch_48_evaluate_factored_expression_numerical_shortcut,
    "49_compound_factorisation_difference_of_squares_with_binomial_terms": arch_49_compound_factorisation_difference_of_squares_with_binomial_terms,
    "50_compound_multi_step_factorisation_and_simplification_challenge": arch_50_compound_multi_step_factorisation_and_simplification_challenge,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_factorisation_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Factorisation / Algebraic Expressions 2 question."""
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
    q["topic"] = "Algebraic expressions 2"
    q["term"] = 1
    return q


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
        q = generate_grade9_factorisation_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
