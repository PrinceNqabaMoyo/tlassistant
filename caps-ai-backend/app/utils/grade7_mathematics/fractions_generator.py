"""
Grade 7 Mathematics - Common Fractions Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 2/01. Fractions.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .fractions_archetypes_01_25 import (
    arch_01_fraction_part_of_a_whole_greystick,
    arch_02_proper_vs_improper_vs_mixed_classification,
    arch_03_convert_mixed_number_to_improper_fraction,
    arch_04_convert_improper_fraction_to_mixed_number,
    arch_05_equivalent_fractions_scaling_up,
    arch_06_simplify_fraction_to_lowest_terms,
    arch_07_comparing_fractions_with_same_denominator,
    arch_08_comparing_fractions_with_different_denominators_lcd,
    arch_09_ordering_fractions_ascending_descending,
    arch_10_adding_fractions_like_denominators,
    arch_11_subtracting_fractions_like_denominators,
    arch_12_adding_fractions_one_denominator_multiple_of_other,
    arch_13_subtracting_fractions_one_denominator_multiple_of_other,
    arch_14_adding_fractions_coprime_denominators_lcd,
    arch_15_subtracting_fractions_coprime_denominators_lcd,
    arch_16_adding_three_fractions_different_denominators,
    arch_17_adding_mixed_numbers_without_regrouping,
    arch_18_adding_mixed_numbers_with_improper_fraction_sum,
    arch_19_subtracting_mixed_numbers_without_borrowing,
    arch_20_subtracting_mixed_numbers_with_borrowing,
    arch_21_subtracting_fraction_from_a_whole_number,
    arch_22_fraction_of_a_whole_number_money_rand,
    arch_23_fraction_of_a_whole_number_distance_km,
    arch_24_fraction_of_a_whole_number_mass_kg,
    arch_25_fraction_of_a_collection_or_learners,
)

from .fractions_archetypes_26_50 import (
    arch_26_multiplying_fraction_by_whole_number,
    arch_27_multiplying_two_common_fractions,
    arch_28_multiplying_mixed_numbers,
    arch_29_reciprocal_of_a_fraction_concept,
    arch_30_dividing_fraction_by_whole_number,
    arch_31_dividing_whole_number_by_fraction,
    arch_32_dividing_fraction_by_fraction,
    arch_33_convert_percentage_to_common_fraction_simplified,
    arch_34_convert_common_fraction_to_percentage,
    arch_35_calculate_percentage_of_a_quantity,
    arch_36_fraction_strip_visual_strip_comparison,
    arch_37_fraction_on_a_number_line_plotting,
    arch_38_fraction_on_a_number_line_reading_value,
    arch_39_fraction_word_problem_remaining_fraction,
    arch_40_fraction_word_problem_baking_recipe_scaling,
    arch_41_fraction_word_problem_sharing_food_equally,
    arch_42_fraction_word_problem_travel_stages,
    arch_43_spot_the_error_adding_denominators_fallacy,
    arch_44_spot_the_error_simplifying_by_canceling_terms,
    arch_45_spot_the_error_borrowing_mixed_number_subtraction,
    arch_46_practical_context_school_test_score_fraction_to_pct,
    arch_47_practical_context_budget_allowance_fraction_breakdown,
    arch_48_practical_context_crop_field_allocation_fractions,
    arch_49_practical_context_water_tank_fractional_fill,
    arch_50_comprehensive_fraction_order_of_operations_bodmas,
)

ARCHETYPE_BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    arch_01_fraction_part_of_a_whole_greystick,
    arch_02_proper_vs_improper_vs_mixed_classification,
    arch_03_convert_mixed_number_to_improper_fraction,
    arch_04_convert_improper_fraction_to_mixed_number,
    arch_05_equivalent_fractions_scaling_up,
    arch_06_simplify_fraction_to_lowest_terms,
    arch_07_comparing_fractions_with_same_denominator,
    arch_08_comparing_fractions_with_different_denominators_lcd,
    arch_09_ordering_fractions_ascending_descending,
    arch_10_adding_fractions_like_denominators,
    arch_11_subtracting_fractions_like_denominators,
    arch_12_adding_fractions_one_denominator_multiple_of_other,
    arch_13_subtracting_fractions_one_denominator_multiple_of_other,
    arch_14_adding_fractions_coprime_denominators_lcd,
    arch_15_subtracting_fractions_coprime_denominators_lcd,
    arch_16_adding_three_fractions_different_denominators,
    arch_17_adding_mixed_numbers_without_regrouping,
    arch_18_adding_mixed_numbers_with_improper_fraction_sum,
    arch_19_subtracting_mixed_numbers_without_borrowing,
    arch_20_subtracting_mixed_numbers_with_borrowing,
    arch_21_subtracting_fraction_from_a_whole_number,
    arch_22_fraction_of_a_whole_number_money_rand,
    arch_23_fraction_of_a_whole_number_distance_km,
    arch_24_fraction_of_a_whole_number_mass_kg,
    arch_25_fraction_of_a_collection_or_learners,
    arch_26_multiplying_fraction_by_whole_number,
    arch_27_multiplying_two_common_fractions,
    arch_28_multiplying_mixed_numbers,
    arch_29_reciprocal_of_a_fraction_concept,
    arch_30_dividing_fraction_by_whole_number,
    arch_31_dividing_whole_number_by_fraction,
    arch_32_dividing_fraction_by_fraction,
    arch_33_convert_percentage_to_common_fraction_simplified,
    arch_34_convert_common_fraction_to_percentage,
    arch_35_calculate_percentage_of_a_quantity,
    arch_36_fraction_strip_visual_strip_comparison,
    arch_37_fraction_on_a_number_line_plotting,
    arch_38_fraction_on_a_number_line_reading_value,
    arch_39_fraction_word_problem_remaining_fraction,
    arch_40_fraction_word_problem_baking_recipe_scaling,
    arch_41_fraction_word_problem_sharing_food_equally,
    arch_42_fraction_word_problem_travel_stages,
    arch_43_spot_the_error_adding_denominators_fallacy,
    arch_44_spot_the_error_simplifying_by_canceling_terms,
    arch_45_spot_the_error_borrowing_mixed_number_subtraction,
    arch_46_practical_context_school_test_score_fraction_to_pct,
    arch_47_practical_context_budget_allowance_fraction_breakdown,
    arch_48_practical_context_crop_field_allocation_fractions,
    arch_49_practical_context_water_tank_fractional_fill,
    arch_50_comprehensive_fraction_order_of_operations_bodmas,
]

SUBSKILLS: List[str] = [
    "01_fraction_part_of_a_whole_greystick",
    "02_proper_vs_improper_vs_mixed_classification",
    "03_convert_mixed_number_to_improper_fraction",
    "04_convert_improper_fraction_to_mixed_number",
    "05_equivalent_fractions_scaling_up",
    "06_simplify_fraction_to_lowest_terms",
    "07_comparing_fractions_with_same_denominator",
    "08_comparing_fractions_with_different_denominators_lcd",
    "09_ordering_fractions_ascending_descending",
    "10_adding_fractions_like_denominators",
    "11_subtracting_fractions_like_denominators",
    "12_adding_fractions_one_denominator_multiple_of_other",
    "13_subtracting_fractions_one_denominator_multiple_of_other",
    "14_adding_fractions_coprime_denominators_lcd",
    "15_subtracting_fractions_coprime_denominators_lcd",
    "16_adding_three_fractions_different_denominators",
    "17_adding_mixed_numbers_without_regrouping",
    "18_adding_mixed_numbers_with_improper_fraction_sum",
    "19_subtracting_mixed_numbers_without_borrowing",
    "20_subtracting_mixed_numbers_with_borrowing",
    "21_subtracting_fraction_from_a_whole_number",
    "22_fraction_of_a_whole_number_money_rand",
    "23_fraction_of_a_whole_number_distance_km",
    "24_fraction_of_a_whole_number_mass_kg",
    "25_fraction_of_a_collection_or_learners",
    "26_multiplying_fraction_by_whole_number",
    "27_multiplying_two_common_fractions",
    "28_multiplying_mixed_numbers",
    "29_reciprocal_of_a_fraction_concept",
    "30_dividing_fraction_by_whole_number",
    "31_dividing_whole_number_by_fraction",
    "32_dividing_fraction_by_fraction",
    "33_convert_percentage_to_common_fraction_simplified",
    "34_convert_common_fraction_to_percentage",
    "35_calculate_percentage_of_a_quantity",
    "36_fraction_strip_visual_strip_comparison",
    "37_fraction_on_a_number_line_plotting",
    "38_fraction_on_a_number_line_reading_value",
    "39_fraction_word_problem_remaining_fraction",
    "40_fraction_word_problem_baking_recipe_scaling",
    "41_fraction_word_problem_sharing_food_equally",
    "42_fraction_word_problem_travel_stages",
    "43_spot_the_error_adding_denominators_fallacy",
    "44_spot_the_error_simplifying_by_canceling_terms",
    "45_spot_the_error_borrowing_mixed_number_subtraction",
    "46_practical_context_school_test_score_fraction_to_pct",
    "47_practical_context_budget_allowance_fraction_breakdown",
    "48_practical_context_crop_field_allocation_fractions",
    "49_practical_context_water_tank_fractional_fill",
    "50_comprehensive_fraction_order_of_operations_bodmas",
]

_SUBSKILL_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    name: builder for name, builder in zip(SUBSKILLS, ARCHETYPE_BUILDERS)
}


def generate_question(
    rng: Optional[random.Random] = None,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    """Generates a fully calibrated Grade 7 Common Fractions question."""
    if rng is None:
        rng = random.Random(seed) if seed is not None else random.Random()

    if subskill and subskill in _SUBSKILL_MAP:
        builder = _SUBSKILL_MAP[subskill]
    else:
        builder = rng.choice(ARCHETYPE_BUILDERS)

    payload = builder(rng)

    payload.setdefault("term", 2)
    payload.setdefault("grade", 7)
    payload.setdefault("subject", "Mathematics")
    payload.setdefault("topic", "Fractions")
    payload.setdefault("caps_weight_percent", 12.0)
    payload.setdefault("suggested_duration_mins", 3)
    payload.setdefault("mode", "elementary_" + payload.get("subskill", "fractions"))
    payload.setdefault(
        "marking_schema",
        [
            {"step": "Correct calculation and fraction setup", "marks": 1, "type": "M"},
            {"step": "Correct simplified answer", "marks": max(1, payload.get("marks", 2) - 1), "type": "A"},
        ],
    )
    return payload


generate = generate_question
