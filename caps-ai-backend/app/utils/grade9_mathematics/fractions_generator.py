"""Grade 9 Mathematics - Fractions Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Fractions.md

Deterministic question generator compliant with South African curriculum standards.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .fractions_archetypes_01_25 import (
    arch_01_fraction_strip_identification_shaded_part,
    arch_02_equivalent_fractions_find_missing_numerator_or_denominator,
    arch_03_simplify_fraction_to_lowest_terms_via_hcf,
    arch_04_convert_improper_fraction_to_mixed_number,
    arch_05_convert_mixed_number_to_improper_fraction,
    arch_06_compare_two_fractions_using_inequality_symbols,
    arch_07_order_set_of_fractions_ascending_descending,
    arch_08_fraction_on_number_line_identify_point,
    arch_09_addition_proper_fractions_like_denominators,
    arch_10_addition_proper_fractions_unlike_denominators,
    arch_11_subtraction_proper_fractions_unlike_denominators,
    arch_12_addition_and_subtraction_three_fractions,
    arch_13_addition_of_mixed_numbers_with_unlike_denominators,
    arch_14_subtraction_of_mixed_numbers_requiring_borrowing,
    arch_15_multiplication_fraction_by_whole_number,
    arch_16_multiplication_two_proper_fractions_cross_cancellation,
    arch_17_multiplication_three_fractions_chained,
    arch_18_multiplication_mixed_numbers,
    arch_19_reciprocal_of_fractions_and_mixed_numbers,
    arch_20_division_proper_fraction_by_proper_fraction,
    arch_21_division_mixed_number_by_fraction_or_mixed_number,
    arch_22_square_of_proper_fraction_and_mixed_number,
    arch_23_cube_of_proper_fraction,
    arch_24_square_root_of_proper_fraction_and_mixed_number,
    arch_25_cube_root_of_proper_fraction,
)
from .fractions_archetypes_26_50 import (
    arch_26_order_of_operations_brackets_multiplication_addition,
    arch_27_order_of_operations_powers_roots_with_operations,
    arch_28_complex_fraction_division_of_sums,
    arch_29_nested_fraction_and_mixed_operations,
    arch_30_fraction_of_a_whole_quantity_currency,
    arch_31_fraction_of_a_quantity_measurement_units,
    arch_32_fraction_of_a_fraction_word_problem,
    arch_33_reverse_fraction_find_the_whole_from_a_part,
    arch_34_convert_common_fraction_to_percentage,
    arch_35_convert_percentage_to_simplified_common_fraction,
    arch_36_convert_mixed_number_percentage_to_fraction,
    arch_37_percentage_of_a_quantity_using_fractions,
    arch_38_percentage_increase_using_fraction_multiplier,
    arch_39_percentage_decrease_using_fraction_multiplier,
    arch_40_express_one_quantity_as_fraction_and_percentage_of_another,
    arch_41_sharing_quantity_in_given_fractional_shares,
    arch_42_fuel_tank_capacity_fraction_problem,
    arch_43_recipe_and_ingredient_scaling_mixed_numbers,
    arch_44_time_and_work_rate_fractions,
    arch_45_distance_travelled_multi_stage_fractions,
    arch_46_visual_pie_chart_fraction_sector_interpretation,
    arch_47_budget_allocation_and_remainder_fraction,
    arch_48_algebraic_fraction_evaluation_numeric_substitution,
    arch_49_error_analysis_diagnose_fraction_operation_error,
    arch_50_compound_multi_step_fraction_capstone,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_fraction_strip_identification_shaded_part": arch_01_fraction_strip_identification_shaded_part,
    "02_equivalent_fractions_find_missing_numerator_or_denominator": arch_02_equivalent_fractions_find_missing_numerator_or_denominator,
    "03_simplify_fraction_to_lowest_terms_via_hcf": arch_03_simplify_fraction_to_lowest_terms_via_hcf,
    "04_convert_improper_fraction_to_mixed_number": arch_04_convert_improper_fraction_to_mixed_number,
    "05_convert_mixed_number_to_improper_fraction": arch_05_convert_mixed_number_to_improper_fraction,
    "06_compare_two_fractions_using_inequality_symbols": arch_06_compare_two_fractions_using_inequality_symbols,
    "07_order_set_of_fractions_ascending_descending": arch_07_order_set_of_fractions_ascending_descending,
    "08_fraction_on_number_line_identify_point": arch_08_fraction_on_number_line_identify_point,
    "09_addition_proper_fractions_like_denominators": arch_09_addition_proper_fractions_like_denominators,
    "10_addition_proper_fractions_unlike_denominators": arch_10_addition_proper_fractions_unlike_denominators,
    "11_subtraction_proper_fractions_unlike_denominators": arch_11_subtraction_proper_fractions_unlike_denominators,
    "12_addition_and_subtraction_three_fractions": arch_12_addition_and_subtraction_three_fractions,
    "13_addition_of_mixed_numbers_with_unlike_denominators": arch_13_addition_of_mixed_numbers_with_unlike_denominators,
    "14_subtraction_of_mixed_numbers_requiring_borrowing": arch_14_subtraction_of_mixed_numbers_requiring_borrowing,
    "15_multiplication_fraction_by_whole_number": arch_15_multiplication_fraction_by_whole_number,
    "16_multiplication_two_proper_fractions_cross_cancellation": arch_16_multiplication_two_proper_fractions_cross_cancellation,
    "17_multiplication_three_fractions_chained": arch_17_multiplication_three_fractions_chained,
    "18_multiplication_mixed_numbers": arch_18_multiplication_mixed_numbers,
    "19_reciprocal_of_fractions_and_mixed_numbers": arch_19_reciprocal_of_fractions_and_mixed_numbers,
    "20_division_proper_fraction_by_proper_fraction": arch_20_division_proper_fraction_by_proper_fraction,
    "21_division_mixed_number_by_fraction_or_mixed_number": arch_21_division_mixed_number_by_fraction_or_mixed_number,
    "22_square_of_proper_fraction_and_mixed_number": arch_22_square_of_proper_fraction_and_mixed_number,
    "23_cube_of_proper_fraction": arch_23_cube_of_proper_fraction,
    "24_square_root_of_proper_fraction_and_mixed_number": arch_24_square_root_of_proper_fraction_and_mixed_number,
    "25_cube_root_of_proper_fraction": arch_25_cube_root_of_proper_fraction,
    "26_order_of_operations_brackets_multiplication_addition": arch_26_order_of_operations_brackets_multiplication_addition,
    "27_order_of_operations_powers_roots_with_operations": arch_27_order_of_operations_powers_roots_with_operations,
    "28_complex_fraction_division_of_sums": arch_28_complex_fraction_division_of_sums,
    "29_nested_fraction_and_mixed_operations": arch_29_nested_fraction_and_mixed_operations,
    "30_fraction_of_a_whole_quantity_currency": arch_30_fraction_of_a_whole_quantity_currency,
    "31_fraction_of_a_quantity_measurement_units": arch_31_fraction_of_a_quantity_measurement_units,
    "32_fraction_of_a_fraction_word_problem": arch_32_fraction_of_a_fraction_word_problem,
    "33_reverse_fraction_find_the_whole_from_a_part": arch_33_reverse_fraction_find_the_whole_from_a_part,
    "34_convert_common_fraction_to_percentage": arch_34_convert_common_fraction_to_percentage,
    "35_convert_percentage_to_simplified_common_fraction": arch_35_convert_percentage_to_simplified_common_fraction,
    "36_convert_mixed_number_percentage_to_fraction": arch_36_convert_mixed_number_percentage_to_fraction,
    "37_percentage_of_a_quantity_using_fractions": arch_37_percentage_of_a_quantity_using_fractions,
    "38_percentage_increase_using_fraction_multiplier": arch_38_percentage_increase_using_fraction_multiplier,
    "39_percentage_decrease_using_fraction_multiplier": arch_39_percentage_decrease_using_fraction_multiplier,
    "40_express_one_quantity_as_fraction_and_percentage_of_another": arch_40_express_one_quantity_as_fraction_and_percentage_of_another,
    "41_sharing_quantity_in_given_fractional_shares": arch_41_sharing_quantity_in_given_fractional_shares,
    "42_fuel_tank_capacity_fraction_problem": arch_42_fuel_tank_capacity_fraction_problem,
    "43_recipe_and_ingredient_scaling_mixed_numbers": arch_43_recipe_and_ingredient_scaling_mixed_numbers,
    "44_time_and_work_rate_fractions": arch_44_time_and_work_rate_fractions,
    "45_distance_travelled_multi_stage_fractions": arch_45_distance_travelled_multi_stage_fractions,
    "46_visual_pie_chart_fraction_sector_interpretation": arch_46_visual_pie_chart_fraction_sector_interpretation,
    "47_budget_allocation_and_remainder_fraction": arch_47_budget_allocation_and_remainder_fraction,
    "48_algebraic_fraction_evaluation_numeric_substitution": arch_48_algebraic_fraction_evaluation_numeric_substitution,
    "49_error_analysis_diagnose_fraction_operation_error": arch_49_error_analysis_diagnose_fraction_operation_error,
    "50_compound_multi_step_fraction_capstone": arch_50_compound_multi_step_fraction_capstone,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_fractions_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Fractions question."""
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
    q["topic"] = "Fractions"
    q["term"] = 2
    q["caps_weight_percent"] = 10
    q["suggested_duration_mins"] = 3
    return q


# Backward compatibility alias
generate_fractions_question = generate_grade9_fractions_question


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
        q = generate_grade9_fractions_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
