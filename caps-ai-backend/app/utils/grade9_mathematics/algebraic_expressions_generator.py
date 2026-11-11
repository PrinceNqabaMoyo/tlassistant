"""Grade 9 Mathematics - Algebraic Expressions 1 Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 1/06. Algebraic expressions 1.md
  curriculum_docs/Mathematics_Gr9/Algebraic Expressions Studio.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .algebraic_expressions_archetypes_01_25 import (
    arch_01_identify_variable_in_given_expression,
    arch_02_identify_constant_term_in_polynomial,
    arch_03_identify_coefficient_of_linear_term,
    arch_04_identify_coefficient_of_squared_term,
    arch_05_determine_degree_of_univariate_polynomial,
    arch_06_classify_expression_as_monomial_binomial_trinomial,
    arch_07_count_number_of_terms_separated_by_plus_minus,
    arch_08_evaluate_linear_expression_positive_integer_substitution,
    arch_09_evaluate_linear_expression_negative_integer_substitution,
    arch_10_evaluate_quadratic_expression_negative_substitution,
    arch_11_evaluate_expression_with_fractional_substitution,
    arch_12_verbal_description_to_algebraic_expression_basic,
    arch_13_verbal_description_to_algebraic_expression_nested_brackets,
    arch_14_distinguish_bracketed_product_from_unbracketed_addition,
    arch_15_flow_diagram_to_algebraic_expression_derivation,
    arch_16_algebraic_expression_to_flow_diagram_derivation,
    arch_17_substitute_into_geometric_perimeter_formula,
    arch_18_substitute_into_geometric_area_formula,
    arch_19_identify_and_group_like_terms_single_variable,
    arch_20_identify_and_group_like_terms_two_variables,
    arch_21_add_polynomials_combining_like_terms,
    arch_22_subtract_polynomials_distributing_negative_sign,
    arch_23_simplify_polynomial_with_descending_powers_standard_form,
    arch_24_distributive_law_monomial_times_binomial_positive,
    arch_25_distributive_law_monomial_times_binomial_negative_monomial,
)
from .algebraic_expressions_archetypes_26_50 import (
    arch_26_distributive_law_monomial_times_trinomial,
    arch_27_distributive_law_variable_monomial_times_binomial,
    arch_28_expand_and_simplify_two_bracketed_expressions_sum,
    arch_29_expand_and_simplify_two_bracketed_expressions_difference,
    arch_30_binomial_product_positive_terms_foil,
    arch_31_binomial_product_mixed_signs_foil,
    arch_32_binomial_product_both_negative_signs_foil,
    arch_33_binomial_product_leading_coefficients_greater_than_one,
    arch_34_square_of_binomial_sum_ax_plus_b_squared,
    arch_35_square_of_binomial_difference_ax_minus_b_squared,
    arch_36_product_of_sum_and_difference_difference_of_two_squares,
    arch_37_expand_and_simplify_binomial_product_minus_squared_binomial,
    arch_38_divide_monomial_by_monomial_integer_coefficients,
    arch_39_divide_monomial_by_monomial_fractional_reduction,
    arch_40_divide_binomial_by_integer_constant,
    arch_41_divide_binomial_by_monomial_single_variable,
    arch_42_divide_trinomial_by_monomial_single_variable,
    arch_43_divide_polynomial_by_monomial_two_variables,
    arch_44_simplify_quotient_with_bracket_in_numerator,
    arch_45_square_root_of_monomial_with_even_exponents,
    arch_46_cube_root_of_monomial_with_multiples_of_three_exponents,
    arch_47_error_analysis_diagnosing_squared_binomial_middle_term_omission,
    arch_48_error_analysis_diagnosing_sign_error_in_subtraction_of_polynomial,
    arch_49_geometric_application_area_of_rectangle_with_binomial_dimensions,
    arch_50_compound_multi_step_algebraic_expansion_and_evaluation_challenge,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_identify_variable_in_given_expression": arch_01_identify_variable_in_given_expression,
    "02_identify_constant_term_in_polynomial": arch_02_identify_constant_term_in_polynomial,
    "03_identify_coefficient_of_linear_term": arch_03_identify_coefficient_of_linear_term,
    "04_identify_coefficient_of_squared_term": arch_04_identify_coefficient_of_squared_term,
    "05_determine_degree_of_univariate_polynomial": arch_05_determine_degree_of_univariate_polynomial,
    "06_classify_expression_as_monomial_binomial_trinomial": arch_06_classify_expression_as_monomial_binomial_trinomial,
    "07_count_number_of_terms_separated_by_plus_minus": arch_07_count_number_of_terms_separated_by_plus_minus,
    "08_evaluate_linear_expression_positive_integer_substitution": arch_08_evaluate_linear_expression_positive_integer_substitution,
    "09_evaluate_linear_expression_negative_integer_substitution": arch_09_evaluate_linear_expression_negative_integer_substitution,
    "10_evaluate_quadratic_expression_negative_substitution": arch_10_evaluate_quadratic_expression_negative_substitution,
    "11_evaluate_expression_with_fractional_substitution": arch_11_evaluate_expression_with_fractional_substitution,
    "12_verbal_description_to_algebraic_expression_basic": arch_12_verbal_description_to_algebraic_expression_basic,
    "13_verbal_description_to_algebraic_expression_nested_brackets": arch_13_verbal_description_to_algebraic_expression_nested_brackets,
    "14_distinguish_bracketed_product_from_unbracketed_addition": arch_14_distinguish_bracketed_product_from_unbracketed_addition,
    "15_flow_diagram_to_algebraic_expression_derivation": arch_15_flow_diagram_to_algebraic_expression_derivation,
    "16_algebraic_expression_to_flow_diagram_derivation": arch_16_algebraic_expression_to_flow_diagram_derivation,
    "17_substitute_into_geometric_perimeter_formula": arch_17_substitute_into_geometric_perimeter_formula,
    "18_substitute_into_geometric_area_formula": arch_18_substitute_into_geometric_area_formula,
    "19_identify_and_group_like_terms_single_variable": arch_19_identify_and_group_like_terms_single_variable,
    "20_identify_and_group_like_terms_two_variables": arch_20_identify_and_group_like_terms_two_variables,
    "21_add_polynomials_combining_like_terms": arch_21_add_polynomials_combining_like_terms,
    "22_subtract_polynomials_distributing_negative_sign": arch_22_subtract_polynomials_distributing_negative_sign,
    "23_simplify_polynomial_with_descending_powers_standard_form": arch_23_simplify_polynomial_with_descending_powers_standard_form,
    "24_distributive_law_monomial_times_binomial_positive": arch_24_distributive_law_monomial_times_binomial_positive,
    "25_distributive_law_monomial_times_binomial_negative_monomial": arch_25_distributive_law_monomial_times_binomial_negative_monomial,
    "26_distributive_law_monomial_times_trinomial": arch_26_distributive_law_monomial_times_trinomial,
    "27_distributive_law_variable_monomial_times_binomial": arch_27_distributive_law_variable_monomial_times_binomial,
    "28_expand_and_simplify_two_bracketed_expressions_sum": arch_28_expand_and_simplify_two_bracketed_expressions_sum,
    "29_expand_and_simplify_two_bracketed_expressions_difference": arch_29_expand_and_simplify_two_bracketed_expressions_difference,
    "30_binomial_product_positive_terms_foil": arch_30_binomial_product_positive_terms_foil,
    "31_binomial_product_mixed_signs_foil": arch_31_binomial_product_mixed_signs_foil,
    "32_binomial_product_both_negative_signs_foil": arch_32_binomial_product_both_negative_signs_foil,
    "33_binomial_product_leading_coefficients_greater_than_one": arch_33_binomial_product_leading_coefficients_greater_than_one,
    "34_square_of_binomial_sum_ax_plus_b_squared": arch_34_square_of_binomial_sum_ax_plus_b_squared,
    "35_square_of_binomial_difference_ax_minus_b_squared": arch_35_square_of_binomial_difference_ax_minus_b_squared,
    "36_product_of_sum_and_difference_difference_of_two_squares": arch_36_product_of_sum_and_difference_difference_of_two_squares,
    "37_expand_and_simplify_binomial_product_minus_squared_binomial": arch_37_expand_and_simplify_binomial_product_minus_squared_binomial,
    "38_divide_monomial_by_monomial_integer_coefficients": arch_38_divide_monomial_by_monomial_integer_coefficients,
    "39_divide_monomial_by_monomial_fractional_reduction": arch_39_divide_monomial_by_monomial_fractional_reduction,
    "40_divide_binomial_by_integer_constant": arch_40_divide_binomial_by_integer_constant,
    "41_divide_binomial_by_monomial_single_variable": arch_41_divide_binomial_by_monomial_single_variable,
    "42_divide_trinomial_by_monomial_single_variable": arch_42_divide_trinomial_by_monomial_single_variable,
    "43_divide_polynomial_by_monomial_two_variables": arch_43_divide_polynomial_by_monomial_two_variables,
    "44_simplify_quotient_with_bracket_in_numerator": arch_44_simplify_quotient_with_bracket_in_numerator,
    "45_square_root_of_monomial_with_even_exponents": arch_45_square_root_of_monomial_with_even_exponents,
    "46_cube_root_of_monomial_with_multiples_of_three_exponents": arch_46_cube_root_of_monomial_with_multiples_of_three_exponents,
    "47_error_analysis_diagnosing_squared_binomial_middle_term_omission": arch_47_error_analysis_diagnosing_squared_binomial_middle_term_omission,
    "48_error_analysis_diagnosing_sign_error_in_subtraction_of_polynomial": arch_48_error_analysis_diagnosing_sign_error_in_subtraction_of_polynomial,
    "49_geometric_application_area_of_rectangle_with_binomial_dimensions": arch_49_geometric_application_area_of_rectangle_with_binomial_dimensions,
    "50_compound_multi_step_algebraic_expansion_and_evaluation_challenge": arch_50_compound_multi_step_algebraic_expansion_and_evaluation_challenge,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_algebraic_expressions_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Algebraic Expressions question."""
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
    q["topic"] = "Algebraic expressions 1"
    q["term"] = 1
    return q


generate_grade9_expressions_question = generate_grade9_algebraic_expressions_question


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
        q = generate_grade9_algebraic_expressions_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
