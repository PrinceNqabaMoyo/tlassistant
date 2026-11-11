"""Grade 9 Mathematics - Whole Numbers Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 1/01. Whole numbers.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .whole_numbers_archetypes_01_25 import (
    arch_01_classify_numbers_real_rational_irrational_non_real,
    arch_02_identify_non_real_even_roots_of_negative_numbers,
    arch_03_identify_undefined_division_by_zero,
    arch_04_determine_between_which_two_integers_surd_lies,
    arch_05_convert_recurring_decimal_to_common_fraction_single_digit,
    arch_06_convert_recurring_decimal_to_common_fraction_two_digits,
    arch_07_properties_of_operations_commutative_and_associative,
    arch_08_properties_of_operations_distributive_over_addition,
    arch_09_identity_elements_additive_zero_and_multiplicative_one,
    arch_10_inverses_additive_inverse_and_reciprocal,
    arch_11_prime_factorisation_written_in_exponential_form,
    arch_12_highest_common_factor_hcf_using_prime_factors_two_numbers,
    arch_13_highest_common_factor_hcf_using_prime_factors_three_numbers,
    arch_14_lowest_common_multiple_lcm_using_prime_factors_two_numbers,
    arch_15_lowest_common_multiple_lcm_using_prime_factors_three_numbers,
    arch_16_hcf_lcm_word_problem_pencils_tiles_or_traffic_lights,
    arch_17_simplify_ratios_to_simplest_integer_form,
    arch_18_simplify_ratios_with_different_metric_units,
    arch_19_divide_amount_in_given_two_part_ratio,
    arch_20_divide_amount_in_given_three_part_ratio,
    arch_21_find_whole_amount_given_one_ratio_share,
    arch_22_direct_proportion_constant_ratio_calculation,
    arch_23_direct_proportion_missing_table_values,
    arch_24_inverse_proportion_constant_product_worker_hours,
    arch_25_inverse_proportion_speed_and_travel_time,
)
from .whole_numbers_archetypes_26_50 import (
    arch_26_average_speed_distance_time_rate_calculation,
    arch_27_unit_rate_best_buy_comparison_per_gram_or_litre,
    arch_28_simple_interest_calculate_interest_amount,
    arch_29_simple_interest_calculate_total_repayment_amount,
    arch_30_simple_interest_calculate_principal_or_rate_or_time,
    arch_31_compound_interest_annual_compounding_total_amount,
    arch_32_compound_interest_calculate_interest_earned,
    arch_33_compare_simple_interest_vs_compound_interest_growth,
    arch_34_hire_purchase_calculate_deposit_percentage,
    arch_35_hire_purchase_calculate_monthly_installment_amount,
    arch_36_hire_purchase_total_cost_and_finance_charges,
    arch_37_hire_purchase_difference_between_cash_price_and_hire_purchase,
    arch_38_inflation_rate_calculate_future_price_of_goods,
    arch_39_percentage_increase_and_decrease_calculation,
    arch_40_percentage_profit_and_loss_on_cost_price,
    arch_41_calculate_selling_price_given_markup_percentage,
    arch_42_calculate_cost_price_from_selling_price_and_profit,
    arch_43_calculate_vat_inclusive_and_exclusive_amounts_15_percent,
    arch_44_calculate_discount_percentage_and_sale_price,
    arch_45_exchange_rate_convert_zar_to_foreign_currency,
    arch_46_exchange_rate_convert_foreign_currency_to_zar,
    arch_47_exchange_rate_traveler_budget_comparison,
    arch_48_error_analysis_diagnosing_distributive_multiplication_error,
    arch_49_error_analysis_diagnosing_hire_purchase_interest_on_deposit_error,
    arch_50_compound_financial_word_problem_investment_comparison,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_classify_numbers_real_rational_irrational_non_real": arch_01_classify_numbers_real_rational_irrational_non_real,
    "02_identify_non_real_even_roots_of_negative_numbers": arch_02_identify_non_real_even_roots_of_negative_numbers,
    "03_identify_undefined_division_by_zero": arch_03_identify_undefined_division_by_zero,
    "04_determine_between_which_two_integers_surd_lies": arch_04_determine_between_which_two_integers_surd_lies,
    "05_convert_recurring_decimal_to_common_fraction_single_digit": arch_05_convert_recurring_decimal_to_common_fraction_single_digit,
    "06_convert_recurring_decimal_to_common_fraction_two_digits": arch_06_convert_recurring_decimal_to_common_fraction_two_digits,
    "07_properties_of_operations_commutative_and_associative": arch_07_properties_of_operations_commutative_and_associative,
    "08_properties_of_operations_distributive_over_addition": arch_08_properties_of_operations_distributive_over_addition,
    "09_identity_elements_additive_zero_and_multiplicative_one": arch_09_identity_elements_additive_zero_and_multiplicative_one,
    "10_inverses_additive_inverse_and_reciprocal": arch_10_inverses_additive_inverse_and_reciprocal,
    "11_prime_factorisation_written_in_exponential_form": arch_11_prime_factorisation_written_in_exponential_form,
    "12_highest_common_factor_hcf_using_prime_factors_two_numbers": arch_12_highest_common_factor_hcf_using_prime_factors_two_numbers,
    "13_highest_common_factor_hcf_using_prime_factors_three_numbers": arch_13_highest_common_factor_hcf_using_prime_factors_three_numbers,
    "14_lowest_common_multiple_lcm_using_prime_factors_two_numbers": arch_14_lowest_common_multiple_lcm_using_prime_factors_two_numbers,
    "15_lowest_common_multiple_lcm_using_prime_factors_three_numbers": arch_15_lowest_common_multiple_lcm_using_prime_factors_three_numbers,
    "16_hcf_lcm_word_problem_pencils_tiles_or_traffic_lights": arch_16_hcf_lcm_word_problem_pencils_tiles_or_traffic_lights,
    "17_simplify_ratios_to_simplest_integer_form": arch_17_simplify_ratios_to_simplest_integer_form,
    "18_simplify_ratios_with_different_metric_units": arch_18_simplify_ratios_with_different_metric_units,
    "19_divide_amount_in_given_two_part_ratio": arch_19_divide_amount_in_given_two_part_ratio,
    "20_divide_amount_in_given_three_part_ratio": arch_20_divide_amount_in_given_three_part_ratio,
    "21_find_whole_amount_given_one_ratio_share": arch_21_find_whole_amount_given_one_ratio_share,
    "22_direct_proportion_constant_ratio_calculation": arch_22_direct_proportion_constant_ratio_calculation,
    "23_direct_proportion_missing_table_values": arch_23_direct_proportion_missing_table_values,
    "24_inverse_proportion_constant_product_worker_hours": arch_24_inverse_proportion_constant_product_worker_hours,
    "25_inverse_proportion_speed_and_travel_time": arch_25_inverse_proportion_speed_and_travel_time,
    "26_average_speed_distance_time_rate_calculation": arch_26_average_speed_distance_time_rate_calculation,
    "27_unit_rate_best_buy_comparison_per_gram_or_litre": arch_27_unit_rate_best_buy_comparison_per_gram_or_litre,
    "28_simple_interest_calculate_interest_amount": arch_28_simple_interest_calculate_interest_amount,
    "29_simple_interest_calculate_total_repayment_amount": arch_29_simple_interest_calculate_total_repayment_amount,
    "30_simple_interest_calculate_principal_or_rate_or_time": arch_30_simple_interest_calculate_principal_or_rate_or_time,
    "31_compound_interest_annual_compounding_total_amount": arch_31_compound_interest_annual_compounding_total_amount,
    "32_compound_interest_calculate_interest_earned": arch_32_compound_interest_calculate_interest_earned,
    "33_compare_simple_interest_vs_compound_interest_growth": arch_33_compare_simple_interest_vs_compound_interest_growth,
    "34_hire_purchase_calculate_deposit_percentage": arch_34_hire_purchase_calculate_deposit_percentage,
    "35_hire_purchase_calculate_monthly_installment_amount": arch_35_hire_purchase_calculate_monthly_installment_amount,
    "36_hire_purchase_total_cost_and_finance_charges": arch_36_hire_purchase_total_cost_and_finance_charges,
    "37_hire_purchase_difference_between_cash_price_and_hire_purchase": arch_37_hire_purchase_difference_between_cash_price_and_hire_purchase,
    "38_inflation_rate_calculate_future_price_of_goods": arch_38_inflation_rate_calculate_future_price_of_goods,
    "39_percentage_increase_and_decrease_calculation": arch_39_percentage_increase_and_decrease_calculation,
    "40_percentage_profit_and_loss_on_cost_price": arch_40_percentage_profit_and_loss_on_cost_price,
    "41_calculate_selling_price_given_markup_percentage": arch_41_calculate_selling_price_given_markup_percentage,
    "42_calculate_cost_price_from_selling_price_and_profit": arch_42_calculate_cost_price_from_selling_price_and_profit,
    "43_calculate_vat_inclusive_and_exclusive_amounts_15_percent": arch_43_calculate_vat_inclusive_and_exclusive_amounts_15_percent,
    "44_calculate_discount_percentage_and_sale_price": arch_44_calculate_discount_percentage_and_sale_price,
    "45_exchange_rate_convert_zar_to_foreign_currency": arch_45_exchange_rate_convert_zar_to_foreign_currency,
    "46_exchange_rate_convert_foreign_currency_to_zar": arch_46_exchange_rate_convert_foreign_currency_to_zar,
    "47_exchange_rate_traveler_budget_comparison": arch_47_exchange_rate_traveler_budget_comparison,
    "48_error_analysis_diagnosing_distributive_multiplication_error": arch_48_error_analysis_diagnosing_distributive_multiplication_error,
    "49_error_analysis_diagnosing_hire_purchase_interest_on_deposit_error": arch_49_error_analysis_diagnosing_hire_purchase_interest_on_deposit_error,
    "50_compound_financial_word_problem_investment_comparison": arch_50_compound_financial_word_problem_investment_comparison,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())


def generate_grade9_whole_numbers_question(
    rng: Optional[random.Random] = None,
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    if rng is None:
        rng = random.Random()

    builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None
    if subskill:
        s_clean = str(subskill).strip()
        if s_clean in ARCHETYPE_MAP:
            builder = ARCHETYPE_MAP[s_clean]
        else:
            for k, b in ARCHETYPE_MAP.items():
                if k.startswith(s_clean) or s_clean in k:
                    builder = b
                    break

    if builder is None:
        builder = rng.choice(list(ARCHETYPE_MAP.values()))

    q = builder(rng)
    q["grade"] = 9
    q["subject"] = "Mathematics"
    q["topic"] = "Whole numbers"
    q["term"] = 1
    q.setdefault("caps_weight_percent", 10)
    q.setdefault("suggested_duration_mins", 45)
    return q


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(count):
        questions.append(generate_grade9_whole_numbers_question(rng=rng, subskill=subskill))

    return questions


__all__ = [
    "ARCHETYPE_MAP",
    "SUBSKILLS",
    "generate",
    "generate_grade9_whole_numbers_question",
]
