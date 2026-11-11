"""
Grade 8 Mathematics - Algebraic Expressions 2 Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/01. Algebraic expressions 2.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .algebraic_expressions_2_archetypes_01_25 import (
    BUILDERS_01_25,
    arch_01_distributive_law_positive_monomial_binomial_sum,
    arch_02_distributive_law_positive_monomial_binomial_difference,
    arch_03_distributive_law_negative_monomial_binomial_sum,
    arch_04_distributive_law_negative_monomial_binomial_difference,
    arch_05_distributive_law_variable_multiplier,
    arch_06_distributive_law_variable_multiplier_with_negative,
    arch_07_distributive_law_monomial_with_variable_and_coefficient,
    arch_08_distributive_law_monomial_with_variable_and_negative_coefficient,
    arch_09_distributive_law_monomial_times_trinomial,
    arch_10_distributive_law_negative_monomial_times_trinomial,
    arch_11_expanding_and_simplifying_sum_of_two_distributed_brackets,
    arch_12_expanding_and_simplifying_difference_of_two_distributed_brackets,
    arch_13_expanding_and_simplifying_variable_brackets_with_like_terms,
    arch_14_expanding_binomial_product_positive_terms,
    arch_15_expanding_binomial_product_mixed_signs,
    arch_16_expanding_binomial_product_both_negative,
    arch_17_squaring_binomial_sum,
    arch_18_squaring_binomial_difference,
    arch_19_diagnosing_binomial_squaring_error,
    arch_20_product_of_sum_and_difference,
    arch_21_dividing_binomial_by_numerical_monomial,
    arch_22_dividing_binomial_by_variable_monomial,
    arch_23_dividing_trinomial_by_variable_monomial,
    arch_24_dividing_polynomial_by_signed_monomial,
    arch_25_dividing_polynomial_by_monomial_with_coefficient,
)
from .algebraic_expressions_2_archetypes_26_50 import (
    BUILDERS_26_50,
    arch_26_factorisation_hcf_numerical,
    arch_27_factorisation_hcf_negative_numerical,
    arch_28_factorisation_hcf_single_variable,
    arch_29_factorisation_hcf_variable_and_number,
    arch_30_factorisation_hcf_with_powers_of_x,
    arch_31_factorisation_hcf_multivariable,
    arch_32_factorisation_trinomial_common_factor,
    arch_33_factorisation_common_binomial_factor,
    arch_34_factorisation_common_binomial_factor_with_variable,
    arch_35_factorisation_difference_of_two_squares_monic,
    arch_36_factorisation_difference_of_two_squares_large_constant,
    arch_37_factorisation_difference_of_two_squares_with_coefficient,
    arch_38_factorisation_difference_of_two_squares_common_factor_first,
    arch_39_square_root_of_monomial_square,
    arch_40_square_root_of_higher_power_monomial,
    arch_41_cube_root_of_monomial_cube,
    arch_42_cube_root_of_higher_power_monomial,
    arch_43_cube_root_of_negative_monomial,
    arch_44_geometric_area_model_distributive_law,
    arch_45_geometric_area_model_binomial_times_binomial,
    arch_46_evaluating_expression_after_expanding,
    arch_47_evaluating_expression_after_factoring,
    arch_48_simplifying_fraction_by_factorising_numerator,
    arch_49_simplifying_fraction_by_factoring_hcf,
    arch_50_algebraic_expressions_2_synthesis_challenge,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = BUILDERS_01_25 + BUILDERS_26_50

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_distributive_law_positive_monomial_binomial_sum",
    "02_distributive_law_positive_monomial_binomial_difference",
    "03_distributive_law_negative_monomial_binomial_sum",
    "04_distributive_law_negative_monomial_binomial_difference",
    "05_distributive_law_variable_multiplier",
    "06_distributive_law_variable_multiplier_with_negative",
    "07_distributive_law_monomial_with_variable_and_coefficient",
    "08_distributive_law_monomial_with_variable_and_negative_coefficient",
    "09_distributive_law_monomial_times_trinomial",
    "10_distributive_law_negative_monomial_times_trinomial",
    # 11 - 20
    "11_expanding_and_simplifying_sum_of_two_distributed_brackets",
    "12_expanding_and_simplifying_difference_of_two_distributed_brackets",
    "13_expanding_and_simplifying_variable_brackets_with_like_terms",
    "14_expanding_binomial_product_positive_terms",
    "15_expanding_binomial_product_mixed_signs",
    "16_expanding_binomial_product_both_negative",
    "17_squaring_binomial_sum",
    "18_squaring_binomial_difference",
    "19_diagnosing_binomial_squaring_error",
    "20_product_of_sum_and_difference",
    # 21 - 30
    "21_dividing_binomial_by_numerical_monomial",
    "22_dividing_binomial_by_variable_monomial",
    "23_dividing_trinomial_by_variable_monomial",
    "24_dividing_polynomial_by_signed_monomial",
    "25_dividing_polynomial_by_monomial_with_coefficient",
    "26_factorisation_hcf_numerical",
    "27_factorisation_hcf_negative_numerical",
    "28_factorisation_hcf_single_variable",
    "29_factorisation_hcf_variable_and_number",
    "30_factorisation_hcf_with_powers_of_x",
    # 31 - 40
    "31_factorisation_hcf_multivariable",
    "32_factorisation_trinomial_common_factor",
    "33_factorisation_common_binomial_factor",
    "34_factorisation_common_binomial_factor_with_variable",
    "35_factorisation_difference_of_two_squares_monic",
    "36_factorisation_difference_of_two_squares_large_constant",
    "37_factorisation_difference_of_two_squares_with_coefficient",
    "38_factorisation_difference_of_two_squares_common_factor_first",
    "39_square_root_of_monomial_square",
    "40_square_root_of_higher_power_monomial",
    # 41 - 50
    "41_cube_root_of_monomial_cube",
    "42_cube_root_of_higher_power_monomial",
    "43_cube_root_of_negative_monomial",
    "44_geometric_area_model_distributive_law",
    "45_geometric_area_model_binomial_times_binomial",
    "46_evaluating_expression_after_expanding",
    "47_evaluating_expression_after_factoring",
    "48_simplifying_fraction_by_factorising_numerator",
    "49_simplifying_fraction_by_factoring_hcf",
    "50_algebraic_expressions_2_synthesis_challenge",
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
        q.setdefault("topic", "Algebraic expressions 2")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
