"""
Grade 8 Mathematics - Exponents Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/03. Exponents.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .exponents_archetypes_01_25 import (
    arch_01_identify_base_and_exponent,
    arch_02_expanded_factor_form_to_exponential,
    arch_03_exponential_form_to_expanded_factor,
    arch_04_numerical_evaluation_small_powers,
    arch_05_zero_exponent_law_numerical,
    arch_06_zero_exponent_law_complex_expression,
    arch_07_exponent_of_one_identity,
    arch_08_powers_of_ten_evaluation,
    arch_09_product_of_powers_same_base_numerical,
    arch_10_product_of_powers_same_base_algebraic,
    arch_11_product_of_powers_three_terms,
    arch_12_product_with_coefficients,
    arch_13_quotient_of_powers_same_base_numerical,
    arch_14_quotient_of_powers_same_base_algebraic,
    arch_15_quotient_with_coefficients,
    arch_16_mixed_product_and_quotient_single_variable,
    arch_17_mixed_product_and_quotient_two_variables,
    arch_18_rational_cancellation_with_coefficients,
    arch_19_power_of_a_power_numerical,
    arch_20_power_of_a_power_algebraic,
    arch_21_power_of_a_product_numerical,
    arch_22_power_of_a_product_algebraic,
    arch_23_power_of_a_product_with_coefficients_and_powers,
    arch_24_power_of_a_quotient_numerical,
    arch_25_power_of_a_quotient_algebraic,
)

from .exponents_archetypes_26_50 import (
    arch_26_power_of_a_quotient_with_coefficients,
    arch_27_nested_powers_and_products,
    arch_28_combined_laws_expansion,
    arch_29_negative_base_even_power,
    arch_30_negative_base_odd_power,
    arch_31_unbracketed_negative_base_even_power,
    arch_32_comparing_bracketed_and_unbracketed_powers,
    arch_33_negative_base_with_variables,
    arch_34_power_of_negative_coefficient_product,
    arch_35_sum_and_difference_of_negative_base_powers,
    arch_36_multiplication_of_powers_with_negative_bases,
    arch_37_square_root_of_exponential_monomial,
    arch_38_square_root_with_numerical_coefficient,
    arch_39_cube_root_of_exponential_monomial,
    arch_40_cube_root_with_numerical_coefficient,
    arch_41_cube_root_of_negative_exponential_expression,
    arch_42_rewriting_bases_as_prime_factors,
    arch_43_ordinary_number_to_scientific_notation,
    arch_44_scientific_notation_to_ordinary_number,
    arch_45_comparing_two_numbers_in_scientific_notation,
    arch_46_multiplying_numbers_in_scientific_notation,
    arch_47_dividing_numbers_in_scientific_notation,
    arch_48_solving_exponential_equation_same_base,
    arch_49_solving_exponential_equation_converting_base,
    arch_50_solving_exponential_equation_with_linear_exponent,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10
    arch_01_identify_base_and_exponent,
    arch_02_expanded_factor_form_to_exponential,
    arch_03_exponential_form_to_expanded_factor,
    arch_04_numerical_evaluation_small_powers,
    arch_05_zero_exponent_law_numerical,
    arch_06_zero_exponent_law_complex_expression,
    arch_07_exponent_of_one_identity,
    arch_08_powers_of_ten_evaluation,
    arch_09_product_of_powers_same_base_numerical,
    arch_10_product_of_powers_same_base_algebraic,
    # 11 - 20
    arch_11_product_of_powers_three_terms,
    arch_12_product_with_coefficients,
    arch_13_quotient_of_powers_same_base_numerical,
    arch_14_quotient_of_powers_same_base_algebraic,
    arch_15_quotient_with_coefficients,
    arch_16_mixed_product_and_quotient_single_variable,
    arch_17_mixed_product_and_quotient_two_variables,
    arch_18_rational_cancellation_with_coefficients,
    arch_19_power_of_a_power_numerical,
    arch_20_power_of_a_power_algebraic,
    # 21 - 28
    arch_21_power_of_a_product_numerical,
    arch_22_power_of_a_product_algebraic,
    arch_23_power_of_a_product_with_coefficients_and_powers,
    arch_24_power_of_a_quotient_numerical,
    arch_25_power_of_a_quotient_algebraic,
    arch_26_power_of_a_quotient_with_coefficients,
    arch_27_nested_powers_and_products,
    arch_28_combined_laws_expansion,
    # 29 - 36
    arch_29_negative_base_even_power,
    arch_30_negative_base_odd_power,
    arch_31_unbracketed_negative_base_even_power,
    arch_32_comparing_bracketed_and_unbracketed_powers,
    arch_33_negative_base_with_variables,
    arch_34_power_of_negative_coefficient_product,
    arch_35_sum_and_difference_of_negative_base_powers,
    arch_36_multiplication_of_powers_with_negative_bases,
    # 37 - 44
    arch_37_square_root_of_exponential_monomial,
    arch_38_square_root_with_numerical_coefficient,
    arch_39_cube_root_of_exponential_monomial,
    arch_40_cube_root_with_numerical_coefficient,
    arch_41_cube_root_of_negative_exponential_expression,
    arch_42_rewriting_bases_as_prime_factors,
    arch_43_ordinary_number_to_scientific_notation,
    arch_44_scientific_notation_to_ordinary_number,
    # 45 - 50
    arch_45_comparing_two_numbers_in_scientific_notation,
    arch_46_multiplying_numbers_in_scientific_notation,
    arch_47_dividing_numbers_in_scientific_notation,
    arch_48_solving_exponential_equation_same_base,
    arch_49_solving_exponential_equation_converting_base,
    arch_50_solving_exponential_equation_with_linear_exponent,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_identify_base_and_exponent",
    "02_expanded_factor_form_to_exponential",
    "03_exponential_form_to_expanded_factor",
    "04_numerical_evaluation_small_powers",
    "05_zero_exponent_law_numerical",
    "06_zero_exponent_law_complex_expression",
    "07_exponent_of_one_identity",
    "08_powers_of_ten_evaluation",
    "09_product_of_powers_same_base_numerical",
    "10_product_of_powers_same_base_algebraic",
    # 11 - 20
    "11_product_of_powers_three_terms",
    "12_product_with_coefficients",
    "13_quotient_of_powers_same_base_numerical",
    "14_quotient_of_powers_same_base_algebraic",
    "15_quotient_with_coefficients",
    "16_mixed_product_and_quotient_single_variable",
    "17_mixed_product_and_quotient_two_variables",
    "18_rational_cancellation_with_coefficients",
    "19_power_of_a_power_numerical",
    "20_power_of_a_power_algebraic",
    # 21 - 28
    "21_power_of_a_product_numerical",
    "22_power_of_a_product_algebraic",
    "23_power_of_a_product_with_coefficients_and_powers",
    "24_power_of_a_quotient_numerical",
    "25_power_of_a_quotient_algebraic",
    "26_power_of_a_quotient_with_coefficients",
    "27_nested_powers_and_products",
    "28_combined_laws_expansion",
    # 29 - 36
    "29_negative_base_even_power",
    "30_negative_base_odd_power",
    "31_unbracketed_negative_base_even_power",
    "32_comparing_bracketed_and_unbracketed_powers",
    "33_negative_base_with_variables",
    "34_power_of_negative_coefficient_product",
    "35_sum_and_difference_of_negative_base_powers",
    "36_multiplication_of_powers_with_negative_bases",
    # 37 - 44
    "37_square_root_of_exponential_monomial",
    "38_square_root_with_numerical_coefficient",
    "39_cube_root_of_exponential_monomial",
    "40_cube_root_with_numerical_coefficient",
    "41_cube_root_of_negative_exponential_expression",
    "42_rewriting_bases_as_prime_factors",
    "43_ordinary_number_to_scientific_notation",
    "44_scientific_notation_to_ordinary_number",
    # 45 - 50
    "45_comparing_two_numbers_in_scientific_notation",
    "46_multiplying_numbers_in_scientific_notation",
    "47_dividing_numbers_in_scientific_notation",
    "48_solving_exponential_equation_same_base",
    "49_solving_exponential_equation_converting_base",
    "50_solving_exponential_equation_with_linear_exponent",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases
DISPATCH_TABLE["product_rule"] = arch_09_product_of_powers_same_base_numerical
DISPATCH_TABLE["quotient_rule"] = arch_13_quotient_of_powers_same_base_numerical
DISPATCH_TABLE["power_rule"] = arch_19_power_of_a_power_numerical
DISPATCH_TABLE["scientific_notation"] = arch_43_ordinary_number_to_scientific_notation
DISPATCH_TABLE["exponential_equations"] = arch_48_solving_exponential_equation_same_base


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
        q.setdefault("topic", "Exponents")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
