"""
Grade 8 Mathematics - Whole Numbers Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/01. Whole numbers.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .whole_numbers_archetypes_01_25 import (
    arch_01_commutative_property_addition_verification,
    arch_02_commutative_property_multiplication_verification,
    arch_03_associative_property_addition_grouping,
    arch_04_associative_property_multiplication_grouping,
    arch_05_distributive_property_multiplication_over_addition,
    arch_06_distributive_property_multiplication_over_subtraction,
    arch_07_additive_identity_and_zero_property,
    arch_08_multiplicative_identity_element,
    arch_09_division_by_zero_undefined_concept,
    arch_10_mental_math_compensation_strategy,
    arch_11_prime_vs_composite_classification,
    arch_12_prime_factorization_factor_tree,
    arch_13_prime_factorization_division_ladder,
    arch_14_highest_common_factor_two_numbers_ladder,
    arch_15_lowest_common_multiple_two_numbers,
    arch_16_hcf_and_lcm_three_numbers,
    arch_17_divisibility_rules_composite_application,
    arch_18_word_problem_hcf_maximum_equal_packaging,
    arch_19_word_problem_lcm_repeating_cycle_alignment,
    arch_20_co_prime_numbers_verification,
    arch_21_expanded_notation_6_digit_whole_number,
    arch_22_place_value_and_face_value_identification,
    arch_23_rounding_off_to_nearest_100_and_1000,
    arch_24_rounding_off_to_nearest_10000_and_100000,
    arch_25_column_addition_with_multiple_carries,
)

from .whole_numbers_archetypes_26_50 import (
    arch_26_column_subtraction_with_multiple_borrows,
    arch_27_multi_step_sum_and_difference_word_problem,
    arch_28_estimating_sums_and_differences_via_rounding,
    arch_29_multiplying_by_multiples_of_10_100_1000,
    arch_30_multiplying_3_digit_by_2_digit_column_method,
    arch_31_multiplying_4_digit_by_2_digit_with_carries,
    arch_32_distributive_breakdown_multiplication,
    arch_33_long_division_3_digit_by_1_digit_with_remainder,
    arch_34_long_division_4_digit_by_2_digit_exact,
    arch_35_long_division_4_digit_by_2_digit_with_remainder,
    arch_36_multiplication_division_inverse_verification,
    arch_37_simplifying_ratios_to_simplest_form,
    arch_38_dividing_an_amount_in_a_two_part_ratio,
    arch_39_dividing_an_amount_in_a_three_part_ratio,
    arch_40_equivalent_ratios_finding_unknown_term,
    arch_41_constant_rate_speed_distance_time,
    arch_42_constant_rate_consumption_and_pricing,
    arch_43_growth_rate_and_population_increase,
    arch_44_direct_proportion_production_table,
    arch_45_cost_price_selling_price_and_profit,
    arch_46_cost_price_selling_price_and_loss,
    arch_47_percentage_discount_on_marked_price,
    arch_48_value_added_tax_vat_15_percent_addition,
    arch_49_value_added_tax_extracting_exclusive_price,
    arch_50_simple_interest_annual_calculation,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10
    arch_01_commutative_property_addition_verification,
    arch_02_commutative_property_multiplication_verification,
    arch_03_associative_property_addition_grouping,
    arch_04_associative_property_multiplication_grouping,
    arch_05_distributive_property_multiplication_over_addition,
    arch_06_distributive_property_multiplication_over_subtraction,
    arch_07_additive_identity_and_zero_property,
    arch_08_multiplicative_identity_element,
    arch_09_division_by_zero_undefined_concept,
    arch_10_mental_math_compensation_strategy,
    # 11 - 20
    arch_11_prime_vs_composite_classification,
    arch_12_prime_factorization_factor_tree,
    arch_13_prime_factorization_division_ladder,
    arch_14_highest_common_factor_two_numbers_ladder,
    arch_15_lowest_common_multiple_two_numbers,
    arch_16_hcf_and_lcm_three_numbers,
    arch_17_divisibility_rules_composite_application,
    arch_18_word_problem_hcf_maximum_equal_packaging,
    arch_19_word_problem_lcm_repeating_cycle_alignment,
    arch_20_co_prime_numbers_verification,
    # 21 - 28
    arch_21_expanded_notation_6_digit_whole_number,
    arch_22_place_value_and_face_value_identification,
    arch_23_rounding_off_to_nearest_100_and_1000,
    arch_24_rounding_off_to_nearest_10000_and_100000,
    arch_25_column_addition_with_multiple_carries,
    arch_26_column_subtraction_with_multiple_borrows,
    arch_27_multi_step_sum_and_difference_word_problem,
    arch_28_estimating_sums_and_differences_via_rounding,
    # 29 - 36
    arch_29_multiplying_by_multiples_of_10_100_1000,
    arch_30_multiplying_3_digit_by_2_digit_column_method,
    arch_31_multiplying_4_digit_by_2_digit_with_carries,
    arch_32_distributive_breakdown_multiplication,
    arch_33_long_division_3_digit_by_1_digit_with_remainder,
    arch_34_long_division_4_digit_by_2_digit_exact,
    arch_35_long_division_4_digit_by_2_digit_with_remainder,
    arch_36_multiplication_division_inverse_verification,
    # 37 - 44
    arch_37_simplifying_ratios_to_simplest_form,
    arch_38_dividing_an_amount_in_a_two_part_ratio,
    arch_39_dividing_an_amount_in_a_three_part_ratio,
    arch_40_equivalent_ratios_finding_unknown_term,
    arch_41_constant_rate_speed_distance_time,
    arch_42_constant_rate_consumption_and_pricing,
    arch_43_growth_rate_and_population_increase,
    arch_44_direct_proportion_production_table,
    # 45 - 50
    arch_45_cost_price_selling_price_and_profit,
    arch_46_cost_price_selling_price_and_loss,
    arch_47_percentage_discount_on_marked_price,
    arch_48_value_added_tax_vat_15_percent_addition,
    arch_49_value_added_tax_extracting_exclusive_price,
    arch_50_simple_interest_annual_calculation,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_commutative_property_addition_verification",
    "02_commutative_property_multiplication_verification",
    "03_associative_property_addition_grouping",
    "04_associative_property_multiplication_grouping",
    "05_distributive_property_multiplication_over_addition",
    "06_distributive_property_multiplication_over_subtraction",
    "07_additive_identity_and_zero_property",
    "08_multiplicative_identity_element",
    "09_division_by_zero_undefined_concept",
    "10_mental_math_compensation_strategy",
    # 11 - 20
    "11_prime_vs_composite_classification",
    "12_prime_factorization_factor_tree",
    "13_prime_factorization_division_ladder",
    "14_highest_common_factor_two_numbers_ladder",
    "15_lowest_common_multiple_two_numbers",
    "16_hcf_and_lcm_three_numbers",
    "17_divisibility_rules_composite_application",
    "18_word_problem_hcf_maximum_equal_packaging",
    "19_word_problem_lcm_repeating_cycle_alignment",
    "20_co_prime_numbers_verification",
    # 21 - 28
    "21_expanded_notation_6_digit_whole_number",
    "22_place_value_and_face_value_identification",
    "23_rounding_off_to_nearest_100_and_1000",
    "24_rounding_off_to_nearest_10000_and_100000",
    "25_column_addition_with_multiple_carries",
    "26_column_subtraction_with_multiple_borrows",
    "27_multi_step_sum_and_difference_word_problem",
    "28_estimating_sums_and_differences_via_rounding",
    # 29 - 36
    "29_multiplying_by_multiples_of_10_100_1000",
    "30_multiplying_3_digit_by_2_digit_column_method",
    "31_multiplying_4_digit_by_2_digit_with_carries",
    "32_distributive_breakdown_multiplication",
    "33_long_division_3_digit_by_1_digit_with_remainder",
    "34_long_division_4_digit_by_2_digit_exact",
    "35_long_division_4_digit_by_2_digit_with_remainder",
    "36_multiplication_division_inverse_verification",
    # 37 - 44
    "37_simplifying_ratios_to_simplest_form",
    "38_dividing_an_amount_in_a_two_part_ratio",
    "39_dividing_an_amount_in_a_three_part_ratio",
    "40_equivalent_ratios_finding_unknown_term",
    "41_constant_rate_speed_distance_time",
    "42_constant_rate_consumption_and_pricing",
    "43_growth_rate_and_population_increase",
    "44_direct_proportion_production_table",
    # 45 - 50
    "45_cost_price_selling_price_and_profit",
    "46_cost_price_selling_price_and_loss",
    "47_percentage_discount_on_marked_price",
    "48_value_added_tax_vat_15_percent_addition",
    "49_value_added_tax_extracting_exclusive_price",
    "50_simple_interest_annual_calculation",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases
DISPATCH_TABLE["commutative"] = arch_01_commutative_property_addition_verification
DISPATCH_TABLE["associative"] = arch_03_associative_property_addition_grouping
DISPATCH_TABLE["distributive"] = arch_05_distributive_property_multiplication_over_addition
DISPATCH_TABLE["prime_factorization"] = arch_12_prime_factorization_factor_tree
DISPATCH_TABLE["lcm_hcf"] = arch_14_highest_common_factor_two_numbers_ladder


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
        q.setdefault("topic", "Whole numbers")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
