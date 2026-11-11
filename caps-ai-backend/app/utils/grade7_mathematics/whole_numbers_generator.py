"""
Grade 7 Mathematics - Working with Whole Numbers Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/01. Working with whole numbers.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .whole_numbers_archetypes_01_25 import (
    arch_01_place_value_digit_identification,
    arch_02_expanded_notation_to_standard_number,
    arch_03_standard_number_to_expanded_notation,
    arch_04_word_form_to_standard_numeral,
    arch_05_ordering_six_digit_numbers_ascending,
    arch_06_ordering_six_digit_numbers_descending,
    arch_07_comparing_six_digit_numbers_inequality,
    arch_08_rounding_to_nearest_ten_hundred_thousand,
    arch_09_listing_multiples_within_interval,
    arch_10_lowest_common_multiple_two_numbers,
    arch_11_lowest_common_multiple_three_numbers,
    arch_12_listing_all_factors_of_number,
    arch_13_highest_common_factor_two_numbers,
    arch_14_highest_common_factor_three_numbers,
    arch_15_divisibility_rule_check_2_3_5,
    arch_16_divisibility_rule_check_6_9_10,
    arch_17_identifying_prime_vs_composite_numbers,
    arch_18_prime_numbers_in_range,
    arch_19_prime_factorisation_factor_tree,
    arch_20_prime_factorisation_ladder_division_method,
    arch_21_prime_factors_in_exponential_form,
    arch_22_hcf_from_prime_factorisations,
    arch_23_lcm_from_prime_factorisations,
    arch_24_square_root_using_prime_factors,
    arch_25_column_addition_five_digit_numbers,
)

from .whole_numbers_archetypes_26_50 import (
    arch_26_column_subtraction_with_borrowing,
    arch_27_addition_subtraction_inverse_check,
    arch_28_estimating_sum_by_rounding,
    arch_29_multi_step_addition_subtraction_budget,
    arch_30_difference_between_two_large_populations,
    arch_31_missing_digit_in_column_addition,
    arch_32_missing_digit_in_column_subtraction,
    arch_33_long_multiplication_3_digit_by_2_digit,
    arch_34_lattice_or_box_multiplication_method,
    arch_35_long_division_4_digit_by_2_digit_no_remainder,
    arch_36_long_division_with_remainder,
    arch_37_division_word_problem_equal_sharing_remainder,
    arch_38_multiplying_by_multiples_of_10_100_1000,
    arch_39_dividing_by_multiples_of_10_100,
    arch_40_multiplication_estimation_by_rounding,
    arch_41_rate_and_unit_price_calculation,
    arch_42_inverse_operation_division_check,
    arch_43_commutative_property_addition_and_multiplication,
    arch_44_associative_property_grouping_strategy,
    arch_45_distributive_property_multiplication_over_addition,
    arch_46_distributive_property_multiplication_over_subtraction,
    arch_47_identity_elements_zero_and_one,
    arch_48_bodmas_order_of_operations_whole_numbers,
    arch_49_financial_profit_bulk_resale_word_problem,
    arch_50_two_step_word_problem_hire_purchase_or_savings,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 08: Place Value & Expanded Notation
    arch_01_place_value_digit_identification,
    arch_02_expanded_notation_to_standard_number,
    arch_03_standard_number_to_expanded_notation,
    arch_04_word_form_to_standard_numeral,
    arch_05_ordering_six_digit_numbers_ascending,
    arch_06_ordering_six_digit_numbers_descending,
    arch_07_comparing_six_digit_numbers_inequality,
    arch_08_rounding_to_nearest_ten_hundred_thousand,
    # 09 - 18: Multiples, Factors & Divisibility
    arch_09_listing_multiples_within_interval,
    arch_10_lowest_common_multiple_two_numbers,
    arch_11_lowest_common_multiple_three_numbers,
    arch_12_listing_all_factors_of_number,
    arch_13_highest_common_factor_two_numbers,
    arch_14_highest_common_factor_three_numbers,
    arch_15_divisibility_rule_check_2_3_5,
    arch_16_divisibility_rule_check_6_9_10,
    arch_17_identifying_prime_vs_composite_numbers,
    arch_18_prime_numbers_in_range,
    # 19 - 24: Prime Factorisation
    arch_19_prime_factorisation_factor_tree,
    arch_20_prime_factorisation_ladder_division_method,
    arch_21_prime_factors_in_exponential_form,
    arch_22_hcf_from_prime_factorisations,
    arch_23_lcm_from_prime_factorisations,
    arch_24_square_root_using_prime_factors,
    # 25 - 32: Addition and Subtraction Operations
    arch_25_column_addition_five_digit_numbers,
    arch_26_column_subtraction_with_borrowing,
    arch_27_addition_subtraction_inverse_check,
    arch_28_estimating_sum_by_rounding,
    arch_29_multi_step_addition_subtraction_budget,
    arch_30_difference_between_two_large_populations,
    arch_31_missing_digit_in_column_addition,
    arch_32_missing_digit_in_column_subtraction,
    # 33 - 42: Multiplication & Division Algorithms
    arch_33_long_multiplication_3_digit_by_2_digit,
    arch_34_lattice_or_box_multiplication_method,
    arch_35_long_division_4_digit_by_2_digit_no_remainder,
    arch_36_long_division_with_remainder,
    arch_37_division_word_problem_equal_sharing_remainder,
    arch_38_multiplying_by_multiples_of_10_100_1000,
    arch_39_dividing_by_multiples_of_10_100,
    arch_40_multiplication_estimation_by_rounding,
    arch_41_rate_and_unit_price_calculation,
    arch_42_inverse_operation_division_check,
    # 43 - 50: Properties of Operations & Problem Solving
    arch_43_commutative_property_addition_and_multiplication,
    arch_44_associative_property_grouping_strategy,
    arch_45_distributive_property_multiplication_over_addition,
    arch_46_distributive_property_multiplication_over_subtraction,
    arch_47_identity_elements_zero_and_one,
    arch_48_bodmas_order_of_operations_whole_numbers,
    arch_49_financial_profit_bulk_resale_word_problem,
    arch_50_two_step_word_problem_hire_purchase_or_savings,
]

SUBSKILLS = [
    # 01 - 08
    "01_place_value_digit_identification",
    "02_expanded_notation_to_standard_number",
    "03_standard_number_to_expanded_notation",
    "04_word_form_to_standard_numeral",
    "05_ordering_six_digit_numbers_ascending",
    "06_ordering_six_digit_numbers_descending",
    "07_comparing_six_digit_numbers_inequality",
    "08_rounding_to_nearest_ten_hundred_thousand",
    # 09 - 18
    "09_listing_multiples_within_interval",
    "10_lowest_common_multiple_two_numbers",
    "11_lowest_common_multiple_three_numbers",
    "12_listing_all_factors_of_number",
    "13_highest_common_factor_two_numbers",
    "14_highest_common_factor_three_numbers",
    "15_divisibility_rule_check_2_3_5",
    "16_divisibility_rule_check_6_9_10",
    "17_identifying_prime_vs_composite_numbers",
    "18_prime_numbers_in_range",
    # 19 - 24
    "19_prime_factorisation_factor_tree",
    "20_prime_factorisation_ladder_division_method",
    "21_prime_factors_in_exponential_form",
    "22_hcf_from_prime_factorisations",
    "23_lcm_from_prime_factorisations",
    "24_square_root_using_prime_factors",
    # 25 - 32
    "25_column_addition_five_digit_numbers",
    "26_column_subtraction_with_borrowing",
    "27_addition_subtraction_inverse_check",
    "28_estimating_sum_by_rounding",
    "29_multi_step_addition_subtraction_budget",
    "30_difference_between_two_large_populations",
    "31_missing_digit_in_column_addition",
    "32_missing_digit_in_column_subtraction",
    # 33 - 42
    "33_long_multiplication_3_digit_by_2_digit",
    "34_lattice_or_box_multiplication_method",
    "35_long_division_4_digit_by_2_digit_no_remainder",
    "36_long_division_with_remainder",
    "37_division_word_problem_equal_sharing_remainder",
    "38_multiplying_by_multiples_of_10_100_1000",
    "39_dividing_by_multiples_of_10_100",
    "40_multiplication_estimation_by_rounding",
    "41_rate_and_unit_price_calculation",
    "42_inverse_operation_division_check",
    # 43 - 50
    "43_commutative_property_addition_and_multiplication",
    "44_associative_property_grouping_strategy",
    "45_distributive_property_multiplication_over_addition",
    "46_distributive_property_multiplication_over_subtraction",
    "47_identity_elements_zero_and_one",
    "48_bodmas_order_of_operations_whole_numbers",
    "49_financial_profit_bulk_resale_word_problem",
    "50_two_step_word_problem_hire_purchase_or_savings",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["long_division"] = arch_35_long_division_4_digit_by_2_digit_no_remainder
DISPATCH_TABLE["distributive_property"] = arch_45_distributive_property_multiplication_over_addition
DISPATCH_TABLE["multiplicative_identity"] = arch_47_identity_elements_zero_and_one
DISPATCH_TABLE["prime_factors"] = arch_19_prime_factorisation_factor_tree
DISPATCH_TABLE["associative_property"] = arch_44_associative_property_grouping_strategy


def get_subskills() -> List[str]:
    """Returns the list of 50 semantic subskill archetype IDs."""
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
    """
    Main entry point for Grade 7 Whole Numbers Generator.
    Supports exact archetype dispatch via subskill or archetype_index, and compound mode.
    """
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
        q.setdefault("grade", 7)
        q.setdefault("subject", "Mathematics")
        q.setdefault("topic", "Working with whole numbers")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
