"""Grade 9 Mathematics - Exponents Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 1/03. Exponents.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .exponents_archetypes_01_25 import (
    arch_01_product_law_single_variable_positive_indices,
    arch_02_product_law_numerical_base_same_base,
    arch_03_product_law_coefficients_and_multiple_variables,
    arch_04_quotient_law_single_variable_positive_result,
    arch_05_quotient_law_coefficients_and_multiple_variables,
    arch_06_power_of_a_power_single_variable,
    arch_07_power_of_a_product_coefficients_and_variables,
    arch_08_power_of_a_quotient_fractional_base,
    arch_09_zero_exponent_law_individual_and_bracketed,
    arch_10_negative_exponent_definition_single_variable,
    arch_11_negative_exponent_numerical_evaluation,
    arch_12_negative_exponent_in_denominator_reciprocal,
    arch_13_negative_exponent_fractional_base_inversion,
    arch_14_express_expression_with_positive_exponents_only,
    arch_15_distinguish_sign_power_bracketed_vs_unbracketed_even,
    arch_16_distinguish_sign_power_bracketed_odd,
    arch_17_rational_exponent_unit_fraction_square_and_cube_roots,
    arch_18_rational_exponent_m_over_n_numerical_evaluation,
    arch_19_rational_exponent_negative_fraction,
    arch_20_scientific_notation_convert_large_numbers_standard_form,
    arch_21_scientific_notation_convert_small_decimals_standard_form,
    arch_22_scientific_notation_expand_to_ordinary_decimal,
    arch_23_scientific_notation_multiplication_of_two_numbers,
    arch_24_scientific_notation_division_of_two_numbers,
    arch_25_scientific_scale_order_of_magnitude_comparison,
)
from .exponents_archetypes_26_50 import (
    arch_26_scientific_notation_addition_same_powers_of_ten,
    arch_27_scientific_notation_addition_different_powers_of_ten,
    arch_28_simplify_exponential_fraction_combining_product_quotient,
    arch_29_simplify_expression_nested_powers_and_negative_indices,
    arch_30_simplify_compound_fraction_multi_variable_with_negative_indices,
    arch_31_prime_base_factorization_numerical_expression,
    arch_32_prime_base_factorization_mixed_bases_2_3_5,
    arch_33_exponential_growth_branching_problem,
    arch_34_exponential_equation_simple_monomial_equating_bases,
    arch_35_exponential_equation_base_3_and_base_5,
    arch_36_exponential_equation_fractional_value_negative_solution,
    arch_37_exponential_equation_fractional_base,
    arch_38_exponential_equation_linear_expression_in_exponent,
    arch_39_exponential_equation_linear_expression_both_sides,
    arch_40_exponential_equation_composite_base_reduction,
    arch_41_exponential_equation_coefficient_division_first,
    arch_42_exponential_equation_equating_exponent_to_zero,
    arch_43_exponential_equation_negative_base_and_sign,
    arch_44_exponential_equation_root_form,
    arch_45_exponential_equation_reciprocal_fractional_linear,
    arch_46_compound_algebraic_fraction_factorisation_terms,
    arch_47_error_analysis_diagnosing_product_law_base_multiplication,
    arch_48_error_analysis_diagnosing_power_of_power_addition,
    arch_49_error_analysis_diagnosing_negative_sign_outside_brackets,
    arch_50_compound_multi_step_exponential_simplification_challenge,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_product_law_single_variable_positive_indices": arch_01_product_law_single_variable_positive_indices,
    "02_product_law_numerical_base_same_base": arch_02_product_law_numerical_base_same_base,
    "03_product_law_coefficients_and_multiple_variables": arch_03_product_law_coefficients_and_multiple_variables,
    "04_quotient_law_single_variable_positive_result": arch_04_quotient_law_single_variable_positive_result,
    "05_quotient_law_coefficients_and_multiple_variables": arch_05_quotient_law_coefficients_and_multiple_variables,
    "06_power_of_a_power_single_variable": arch_06_power_of_a_power_single_variable,
    "07_power_of_a_product_coefficients_and_variables": arch_07_power_of_a_product_coefficients_and_variables,
    "08_power_of_a_quotient_fractional_base": arch_08_power_of_a_quotient_fractional_base,
    "09_zero_exponent_law_individual_and_bracketed": arch_09_zero_exponent_law_individual_and_bracketed,
    "10_negative_exponent_definition_single_variable": arch_10_negative_exponent_definition_single_variable,
    "11_negative_exponent_numerical_evaluation": arch_11_negative_exponent_numerical_evaluation,
    "12_negative_exponent_in_denominator_reciprocal": arch_12_negative_exponent_in_denominator_reciprocal,
    "13_negative_exponent_fractional_base_inversion": arch_13_negative_exponent_fractional_base_inversion,
    "14_express_expression_with_positive_exponents_only": arch_14_express_expression_with_positive_exponents_only,
    "15_distinguish_sign_power_bracketed_vs_unbracketed_even": arch_15_distinguish_sign_power_bracketed_vs_unbracketed_even,
    "16_distinguish_sign_power_bracketed_odd": arch_16_distinguish_sign_power_bracketed_odd,
    "17_rational_exponent_unit_fraction_square_and_cube_roots": arch_17_rational_exponent_unit_fraction_square_and_cube_roots,
    "18_rational_exponent_m_over_n_numerical_evaluation": arch_18_rational_exponent_m_over_n_numerical_evaluation,
    "19_rational_exponent_negative_fraction": arch_19_rational_exponent_negative_fraction,
    "20_scientific_notation_convert_large_numbers_standard_form": arch_20_scientific_notation_convert_large_numbers_standard_form,
    "21_scientific_notation_convert_small_decimals_standard_form": arch_21_scientific_notation_convert_small_decimals_standard_form,
    "22_scientific_notation_expand_to_ordinary_decimal": arch_22_scientific_notation_expand_to_ordinary_decimal,
    "23_scientific_notation_multiplication_of_two_numbers": arch_23_scientific_notation_multiplication_of_two_numbers,
    "24_scientific_notation_division_of_two_numbers": arch_24_scientific_notation_division_of_two_numbers,
    "25_scientific_scale_order_of_magnitude_comparison": arch_25_scientific_scale_order_of_magnitude_comparison,
    "26_scientific_notation_addition_same_powers_of_ten": arch_26_scientific_notation_addition_same_powers_of_ten,
    "27_scientific_notation_addition_different_powers_of_ten": arch_27_scientific_notation_addition_different_powers_of_ten,
    "28_simplify_exponential_fraction_combining_product_quotient": arch_28_simplify_exponential_fraction_combining_product_quotient,
    "29_simplify_expression_nested_powers_and_negative_indices": arch_29_simplify_expression_nested_powers_and_negative_indices,
    "30_simplify_compound_fraction_multi_variable_with_negative_indices": arch_30_simplify_compound_fraction_multi_variable_with_negative_indices,
    "31_prime_base_factorization_numerical_expression": arch_31_prime_base_factorization_numerical_expression,
    "32_prime_base_factorization_mixed_bases_2_3_5": arch_32_prime_base_factorization_mixed_bases_2_3_5,
    "33_exponential_growth_branching_problem": arch_33_exponential_growth_branching_problem,
    "34_exponential_equation_simple_monomial_equating_bases": arch_34_exponential_equation_simple_monomial_equating_bases,
    "35_exponential_equation_base_3_and_base_5": arch_35_exponential_equation_base_3_and_base_5,
    "36_exponential_equation_fractional_value_negative_solution": arch_36_exponential_equation_fractional_value_negative_solution,
    "37_exponential_equation_fractional_base": arch_37_exponential_equation_fractional_base,
    "38_exponential_equation_linear_expression_in_exponent": arch_38_exponential_equation_linear_expression_in_exponent,
    "39_exponential_equation_linear_expression_both_sides": arch_39_exponential_equation_linear_expression_both_sides,
    "40_exponential_equation_composite_base_reduction": arch_40_exponential_equation_composite_base_reduction,
    "41_exponential_equation_coefficient_division_first": arch_41_exponential_equation_coefficient_division_first,
    "42_exponential_equation_equating_exponent_to_zero": arch_42_exponential_equation_equating_exponent_to_zero,
    "43_exponential_equation_negative_base_and_sign": arch_43_exponential_equation_negative_base_and_sign,
    "44_exponential_equation_root_form": arch_44_exponential_equation_root_form,
    "45_exponential_equation_reciprocal_fractional_linear": arch_45_exponential_equation_reciprocal_fractional_linear,
    "46_compound_algebraic_fraction_factorisation_terms": arch_46_compound_algebraic_fraction_factorisation_terms,
    "47_error_analysis_diagnosing_product_law_base_multiplication": arch_47_error_analysis_diagnosing_product_law_base_multiplication,
    "48_error_analysis_diagnosing_power_of_power_addition": arch_48_error_analysis_diagnosing_power_of_power_addition,
    "49_error_analysis_diagnosing_negative_sign_outside_brackets": arch_49_error_analysis_diagnosing_negative_sign_outside_brackets,
    "50_compound_multi_step_exponential_simplification_challenge": arch_50_compound_multi_step_exponential_simplification_challenge,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_exponents_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Exponents question."""
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
    q["topic"] = "Exponents"
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
        q = generate_grade9_exponents_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
