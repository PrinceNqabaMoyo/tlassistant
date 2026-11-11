"""
Grade 8 Mathematics - Algebraic Expressions 1 Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/01. Algebraic expressions 1.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .algebraic_expressions_1_archetypes_01_25 import (
    BUILDERS_01_25,
    arch_01_translating_word_phrase_sum_product_to_expression,
    arch_02_translating_word_phrase_difference_quotient_to_expression,
    arch_03_translating_flow_diagram_to_expression,
    arch_04_identifying_number_of_terms_in_expression,
    arch_05_classifying_monomial_binomial_trinomial_polynomial,
    arch_06_identifying_variable_and_constant_term,
    arch_07_identifying_coefficient_of_linear_term,
    arch_08_identifying_coefficient_of_squared_term,
    arch_09_determining_degree_of_univariate_polynomial,
    arch_10_identifying_like_terms_from_list,
    arch_11_distinguishing_like_from_unlike_terms_powers,
    arch_12_distinguishing_like_from_unlike_terms_variables,
    arch_13_combining_linear_like_terms_positive_coefficients,
    arch_14_combining_linear_like_terms_with_negatives,
    arch_15_combining_quadratic_and_linear_like_terms,
    arch_16_combining_multivariable_like_terms,
    arch_17_rearranging_and_simplifying_trinomial_terms,
    arch_18_evaluating_linear_expression_positive_integer,
    arch_19_evaluating_linear_expression_negative_integer,
    arch_20_evaluating_quadratic_expression_positive_integer,
    arch_21_evaluating_quadratic_expression_negative_integer,
    arch_22_evaluating_expression_with_fractional_input,
    arch_23_evaluating_expression_with_zero,
    arch_24_verifying_equivalent_expressions_substitution,
    arch_25_distinguishing_equivalent_from_non_equivalent_expressions,
)
from .algebraic_expressions_1_archetypes_26_50 import (
    BUILDERS_26_50,
    arch_26_perimeter_of_equilateral_triangle_in_terms_of_x,
    arch_27_perimeter_of_rectangle_in_terms_of_x,
    arch_28_perimeter_of_scalene_triangle_combining_like_terms,
    arch_29_perimeter_of_square_in_terms_of_x,
    arch_30_translating_consecutive_integers_to_algebra,
    arch_31_translating_consecutive_even_integers,
    arch_32_translating_age_word_problem_to_expression,
    arch_33_translating_taxi_fare_to_expression,
    arch_34_simplifying_expression_with_parentheses_addition,
    arch_35_simplifying_expression_with_parentheses_subtraction,
    arch_36_identifying_sign_error_in_subtraction_of_binomial,
    arch_37_combining_cubed_and_squared_terms,
    arch_38_writing_expression_for_shaded_area_difference,
    arch_39_writing_expression_for_total_cost_items,
    arch_40_simplifying_fractions_with_monomial_denominator,
    arch_41_evaluating_two_variable_expression,
    arch_42_evaluating_two_variable_expression_with_negatives,
    arch_43_finding_missing_term_to_make_expressions_equivalent,
    arch_44_translating_geometric_pattern_to_algebraic_expression,
    arch_45_descending_powers_arrangement_polynomial,
    arch_46_ascending_powers_arrangement_polynomial,
    arch_47_evaluating_expression_with_brackets,
    arch_48_identifying_non_polynomial_expression,
    arch_49_combining_constants_and_variables_in_shopping_budget,
    arch_50_algebraic_expression_summary_challenge,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = BUILDERS_01_25 + BUILDERS_26_50

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_translating_word_phrase_sum_product_to_expression",
    "02_translating_word_phrase_difference_quotient_to_expression",
    "03_translating_flow_diagram_to_expression",
    "04_identifying_number_of_terms_in_expression",
    "05_classifying_monomial_binomial_trinomial_polynomial",
    "06_identifying_variable_and_constant_term",
    "07_identifying_coefficient_of_linear_term",
    "08_identifying_coefficient_of_squared_term",
    "09_determining_degree_of_univariate_polynomial",
    "10_identifying_like_terms_from_list",
    # 11 - 20
    "11_distinguishing_like_from_unlike_terms_powers",
    "12_distinguishing_like_from_unlike_terms_variables",
    "13_combining_linear_like_terms_positive_coefficients",
    "14_combining_linear_like_terms_with_negatives",
    "15_combining_quadratic_and_linear_like_terms",
    "16_combining_multivariable_like_terms",
    "17_rearranging_and_simplifying_trinomial_terms",
    "18_evaluating_linear_expression_positive_integer",
    "19_evaluating_linear_expression_negative_integer",
    "20_evaluating_quadratic_expression_positive_integer",
    # 21 - 30
    "21_evaluating_quadratic_expression_negative_integer",
    "22_evaluating_expression_with_fractional_input",
    "23_evaluating_expression_with_zero",
    "24_verifying_equivalent_expressions_substitution",
    "25_distinguishing_equivalent_from_non_equivalent_expressions",
    "26_perimeter_of_equilateral_triangle_in_terms_of_x",
    "27_perimeter_of_rectangle_in_terms_of_x",
    "28_perimeter_of_scalene_triangle_combining_like_terms",
    "29_perimeter_of_square_in_terms_of_x",
    "30_translating_consecutive_integers_to_algebra",
    # 31 - 40
    "31_translating_consecutive_even_integers",
    "32_translating_age_word_problem_to_expression",
    "33_translating_taxi_fare_to_expression",
    "34_simplifying_expression_with_parentheses_addition",
    "35_simplifying_expression_with_parentheses_subtraction",
    "36_identifying_sign_error_in_subtraction_of_binomial",
    "37_combining_cubed_and_squared_terms",
    "38_writing_expression_for_shaded_area_difference",
    "39_writing_expression_for_total_cost_items",
    "40_simplifying_fractions_with_monomial_denominator",
    # 41 - 50
    "41_evaluating_two_variable_expression",
    "42_evaluating_two_variable_expression_with_negatives",
    "43_finding_missing_term_to_make_expressions_equivalent",
    "44_translating_geometric_pattern_to_algebraic_expression",
    "45_descending_powers_arrangement_polynomial",
    "46_ascending_powers_arrangement_polynomial",
    "47_evaluating_expression_with_brackets",
    "48_identifying_non_polynomial_expression",
    "49_combining_constants_and_variables_in_shopping_budget",
    "50_algebraic_expression_summary_challenge",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {}

for idx, b in enumerate(BUILDERS, start=1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

for name, b in zip(SUBSKILLS, BUILDERS):
    DISPATCH_TABLE[name] = b
    prefix = name.split("_")[0]
    DISPATCH_TABLE[prefix] = b
    short_slug = "_".join(name.split("_")[1:])
    DISPATCH_TABLE[short_slug] = b


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
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
        q.setdefault("topic", "Algebraic expressions 1")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
