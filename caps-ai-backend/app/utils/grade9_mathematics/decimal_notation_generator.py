"""Grade 9 Mathematics - Decimal Notation Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 1/01. The decimal notation for fractions.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .decimal_notation_archetypes_01_25 import (
    arch_01_place_value_identification_tenths_hundredths_thousandths,
    arch_02_expanded_notation_powers_of_ten_negative_exponents,
    arch_03_compose_decimal_from_expanded_fractional_form,
    arch_04_hundredths_grid_shaded_area_to_decimal_and_percentage,
    arch_05_convert_common_fraction_terminating_decimal,
    arch_06_convert_mixed_number_to_decimal_notation,
    arch_07_convert_terminating_decimal_to_simplified_common_fraction,
    arch_08_convert_percentage_to_decimal_and_fraction,
    arch_09_convert_decimal_to_percentage,
    arch_10_recurring_decimal_notation_single_period,
    arch_11_recurring_decimal_notation_multi_digit_period,
    arch_12_read_point_on_zoomed_decimal_number_line,
    arch_13_plot_and_locate_decimal_between_two_tenths,
    arch_14_compare_two_decimals_using_inequality_symbols,
    arch_15_order_set_of_four_decimals_ascending_descending,
    arch_16_find_decimal_midpoint_between_two_numbers,
    arch_17_decimal_jump_sequences_arithmetic_step,
    arch_18_round_off_to_nearest_whole_number,
    arch_19_round_off_to_one_decimal_place,
    arch_20_round_off_to_two_decimal_places,
    arch_21_round_off_to_three_decimal_places,
    arch_22_rounding_in_financial_context_nearest_five_cents,
    arch_23_rounding_in_financial_context_nearest_cent,
    arch_24_addition_of_two_decimals_with_carrying,
    arch_25_addition_of_three_decimals_different_lengths,
)
from .decimal_notation_archetypes_26_50 import (
    arch_26_subtraction_of_two_decimals_with_borrowing,
    arch_27_subtraction_whole_number_minus_multi_decimal,
    arch_28_combined_addition_and_subtraction_word_problem,
    arch_29_multiplication_by_powers_of_ten_10_100_1000,
    arch_30_multiplication_of_decimal_by_single_digit_whole,
    arch_31_multiplication_of_decimal_by_two_digit_whole,
    arch_32_multiplication_of_two_decimals_tenths_by_tenths,
    arch_33_multiplication_of_two_decimals_hundredths_by_tenths,
    arch_34_multiplication_of_two_decimals_hundredths_by_hundredths,
    arch_35_division_by_powers_of_ten_10_100_1000,
    arch_36_division_of_decimal_by_single_digit_whole_no_remainder,
    arch_37_division_of_decimal_by_whole_number_requiring_zero_annexing,
    arch_38_division_of_decimal_by_decimal_scaling_divisor,
    arch_39_division_of_decimal_by_decimal_yielding_decimal,
    arch_40_square_of_decimal_fraction,
    arch_41_cube_of_decimal_fraction,
    arch_42_square_root_of_decimal_fraction,
    arch_43_cube_root_of_decimal_fraction,
    arch_44_order_of_operations_bodmas_with_decimals_mixed,
    arch_45_order_of_operations_brackets_and_powers_decimals,
    arch_46_olympic_timing_margin_of_victory_problem,
    arch_47_fuel_consumption_and_cost_rate_word_problem,
    arch_48_unit_pricing_best_buy_comparison_decimals,
    arch_49_error_analysis_diagnosing_decimal_multiplication_place_value,
    arch_50_compound_multi_step_decimal_fraction_evaluation,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_place_value_identification_tenths_hundredths_thousandths": arch_01_place_value_identification_tenths_hundredths_thousandths,
    "02_expanded_notation_powers_of_ten_negative_exponents": arch_02_expanded_notation_powers_of_ten_negative_exponents,
    "03_compose_decimal_from_expanded_fractional_form": arch_03_compose_decimal_from_expanded_fractional_form,
    "04_hundredths_grid_shaded_area_to_decimal_and_percentage": arch_04_hundredths_grid_shaded_area_to_decimal_and_percentage,
    "05_convert_common_fraction_terminating_decimal": arch_05_convert_common_fraction_terminating_decimal,
    "06_convert_mixed_number_to_decimal_notation": arch_06_convert_mixed_number_to_decimal_notation,
    "07_convert_terminating_decimal_to_simplified_common_fraction": arch_07_convert_terminating_decimal_to_simplified_common_fraction,
    "08_convert_percentage_to_decimal_and_fraction": arch_08_convert_percentage_to_decimal_and_fraction,
    "09_convert_decimal_to_percentage": arch_09_convert_decimal_to_percentage,
    "10_recurring_decimal_notation_single_period": arch_10_recurring_decimal_notation_single_period,
    "11_recurring_decimal_notation_multi_digit_period": arch_11_recurring_decimal_notation_multi_digit_period,
    "12_read_point_on_zoomed_decimal_number_line": arch_12_read_point_on_zoomed_decimal_number_line,
    "13_plot_and_locate_decimal_between_two_tenths": arch_13_plot_and_locate_decimal_between_two_tenths,
    "14_compare_two_decimals_using_inequality_symbols": arch_14_compare_two_decimals_using_inequality_symbols,
    "15_order_set_of_four_decimals_ascending_descending": arch_15_order_set_of_four_decimals_ascending_descending,
    "16_find_decimal_midpoint_between_two_numbers": arch_16_find_decimal_midpoint_between_two_numbers,
    "17_decimal_jump_sequences_arithmetic_step": arch_17_decimal_jump_sequences_arithmetic_step,
    "18_round_off_to_nearest_whole_number": arch_18_round_off_to_nearest_whole_number,
    "19_round_off_to_one_decimal_place": arch_19_round_off_to_one_decimal_place,
    "20_round_off_to_two_decimal_places": arch_20_round_off_to_two_decimal_places,
    "21_round_off_to_three_decimal_places": arch_21_round_off_to_three_decimal_places,
    "22_rounding_in_financial_context_nearest_five_cents": arch_22_rounding_in_financial_context_nearest_five_cents,
    "23_rounding_in_financial_context_nearest_cent": arch_23_rounding_in_financial_context_nearest_cent,
    "24_addition_of_two_decimals_with_carrying": arch_24_addition_of_two_decimals_with_carrying,
    "25_addition_of_three_decimals_different_lengths": arch_25_addition_of_three_decimals_different_lengths,
    "26_subtraction_of_two_decimals_with_borrowing": arch_26_subtraction_of_two_decimals_with_borrowing,
    "27_subtraction_whole_number_minus_multi_decimal": arch_27_subtraction_whole_number_minus_multi_decimal,
    "28_combined_addition_and_subtraction_word_problem": arch_28_combined_addition_and_subtraction_word_problem,
    "29_multiplication_by_powers_of_ten_10_100_1000": arch_29_multiplication_by_powers_of_ten_10_100_1000,
    "30_multiplication_of_decimal_by_single_digit_whole": arch_30_multiplication_of_decimal_by_single_digit_whole,
    "31_multiplication_of_decimal_by_two_digit_whole": arch_31_multiplication_of_decimal_by_two_digit_whole,
    "32_multiplication_of_two_decimals_tenths_by_tenths": arch_32_multiplication_of_two_decimals_tenths_by_tenths,
    "33_multiplication_of_two_decimals_hundredths_by_tenths": arch_33_multiplication_of_two_decimals_hundredths_by_tenths,
    "34_multiplication_of_two_decimals_hundredths_by_hundredths": arch_34_multiplication_of_two_decimals_hundredths_by_hundredths,
    "35_division_by_powers_of_ten_10_100_1000": arch_35_division_by_powers_of_ten_10_100_1000,
    "36_division_of_decimal_by_single_digit_whole_no_remainder": arch_36_division_of_decimal_by_single_digit_whole_no_remainder,
    "37_division_of_decimal_by_whole_number_requiring_zero_annexing": arch_37_division_of_decimal_by_whole_number_requiring_zero_annexing,
    "38_division_of_decimal_by_decimal_scaling_divisor": arch_38_division_of_decimal_by_decimal_scaling_divisor,
    "39_division_of_decimal_by_decimal_yielding_decimal": arch_39_division_of_decimal_by_decimal_yielding_decimal,
    "40_square_of_decimal_fraction": arch_40_square_of_decimal_fraction,
    "41_cube_of_decimal_fraction": arch_41_cube_of_decimal_fraction,
    "42_square_root_of_decimal_fraction": arch_42_square_root_of_decimal_fraction,
    "43_cube_root_of_decimal_fraction": arch_43_cube_root_of_decimal_fraction,
    "44_order_of_operations_bodmas_with_decimals_mixed": arch_44_order_of_operations_bodmas_with_decimals_mixed,
    "45_order_of_operations_brackets_and_powers_decimals": arch_45_order_of_operations_brackets_and_powers_decimals,
    "46_olympic_timing_margin_of_victory_problem": arch_46_olympic_timing_margin_of_victory_problem,
    "47_fuel_consumption_and_cost_rate_word_problem": arch_47_fuel_consumption_and_cost_rate_word_problem,
    "48_unit_pricing_best_buy_comparison_decimals": arch_48_unit_pricing_best_buy_comparison_decimals,
    "49_error_analysis_diagnosing_decimal_multiplication_place_value": arch_49_error_analysis_diagnosing_decimal_multiplication_place_value,
    "50_compound_multi_step_decimal_fraction_evaluation": arch_50_compound_multi_step_decimal_fraction_evaluation,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_decimal_notation_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Decimal Notation question."""
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
    q["topic"] = "The decimal notation for fractions"
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
        q = generate_grade9_decimal_notation_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
