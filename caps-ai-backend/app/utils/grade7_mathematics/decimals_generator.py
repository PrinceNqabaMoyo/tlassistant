"""
Grade 7 Mathematics - Decimal Fractions Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 2/01. The decimal notation for fractions.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .decimals_archetypes_01_25 import (
    arch_01_place_value_identification_tenths_hundredths_thousandths,
    arch_02_digit_value_in_decimal_number,
    arch_03_convert_tenth_fraction_to_decimal,
    arch_04_convert_hundredth_fraction_to_decimal,
    arch_05_convert_thousandth_fraction_to_decimal,
    arch_06_convert_mixed_fraction_to_decimal,
    arch_07_convert_decimal_to_common_fraction_simplified,
    arch_08_expanded_notation_to_decimal_standard_form,
    arch_09_decimal_to_expanded_fraction_form,
    arch_10_comparing_two_decimal_numbers,
    arch_11_ordering_decimals_ascending_descending,
    arch_12_rounding_to_nearest_whole_number,
    arch_13_rounding_to_one_decimal_place_tenths,
    arch_14_rounding_to_two_decimal_places_hundredths,
    arch_15_adding_decimals_same_decimal_places,
    arch_16_adding_decimals_different_decimal_places_padding,
    arch_17_adding_three_decimal_numbers,
    arch_18_subtracting_decimals_same_decimal_places,
    arch_19_subtracting_decimals_with_borrowing,
    arch_20_subtracting_decimal_from_whole_number,
    arch_21_multiplying_decimal_by_10_100_1000,
    arch_22_dividing_decimal_by_10_100_1000,
    arch_23_multiplying_decimal_by_single_digit_whole_number,
    arch_24_multiplying_two_decimal_fractions,
    arch_25_dividing_decimal_by_whole_number,
)

from .decimals_archetypes_26_50 import (
    arch_26_dividing_whole_numbers_yielding_decimal_quotient,
    arch_27_common_fraction_half_quarter_to_decimal,
    arch_28_common_fraction_fifths_to_decimal,
    arch_29_common_fraction_eighths_to_decimal,
    arch_30_percentage_to_decimal_conversion,
    arch_31_decimal_to_percentage_conversion,
    arch_32_three_way_equivalence_table_fraction_decimal_pct,
    arch_33_decimal_on_a_number_line_reading,
    arch_34_decimal_on_a_number_line_plotting,
    arch_35_grid_100_square_shaded_decimal_representation,
    arch_36_money_rand_cents_addition_total_cost,
    arch_37_money_rand_cents_subtraction_calculating_change,
    arch_38_money_multiplication_unit_price,
    arch_39_money_division_equal_split,
    arch_40_measurement_length_metres_to_centimetres_decimal,
    arch_41_measurement_mass_kilograms_to_grams_decimal,
    arch_42_measurement_capacity_litres_to_millilitres_decimal,
    arch_43_spot_the_error_ragged_decimal_addition_alignment,
    arch_44_spot_the_error_longer_decimal_is_larger_fallacy,
    arch_45_spot_the_error_trailing_zero_removal_confusion,
    arch_46_spot_the_error_decimal_multiplication_point_placement,
    arch_47_practical_context_fuel_pump_litres_and_cost,
    arch_48_practical_context_athletics_race_times_hundredths_second,
    arch_49_practical_context_supermarket_till_slip_rounding,
    arch_50_comprehensive_multi_step_decimal_word_problem,
)

ARCHETYPE_BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    arch_01_place_value_identification_tenths_hundredths_thousandths,
    arch_02_digit_value_in_decimal_number,
    arch_03_convert_tenth_fraction_to_decimal,
    arch_04_convert_hundredth_fraction_to_decimal,
    arch_05_convert_thousandth_fraction_to_decimal,
    arch_06_convert_mixed_fraction_to_decimal,
    arch_07_convert_decimal_to_common_fraction_simplified,
    arch_08_expanded_notation_to_decimal_standard_form,
    arch_09_decimal_to_expanded_fraction_form,
    arch_10_comparing_two_decimal_numbers,
    arch_11_ordering_decimals_ascending_descending,
    arch_12_rounding_to_nearest_whole_number,
    arch_13_rounding_to_one_decimal_place_tenths,
    arch_14_rounding_to_two_decimal_places_hundredths,
    arch_15_adding_decimals_same_decimal_places,
    arch_16_adding_decimals_different_decimal_places_padding,
    arch_17_adding_three_decimal_numbers,
    arch_18_subtracting_decimals_same_decimal_places,
    arch_19_subtracting_decimals_with_borrowing,
    arch_20_subtracting_decimal_from_whole_number,
    arch_21_multiplying_decimal_by_10_100_1000,
    arch_22_dividing_decimal_by_10_100_1000,
    arch_23_multiplying_decimal_by_single_digit_whole_number,
    arch_24_multiplying_two_decimal_fractions,
    arch_25_dividing_decimal_by_whole_number,
    arch_26_dividing_whole_numbers_yielding_decimal_quotient,
    arch_27_common_fraction_half_quarter_to_decimal,
    arch_28_common_fraction_fifths_to_decimal,
    arch_29_common_fraction_eighths_to_decimal,
    arch_30_percentage_to_decimal_conversion,
    arch_31_decimal_to_percentage_conversion,
    arch_32_three_way_equivalence_table_fraction_decimal_pct,
    arch_33_decimal_on_a_number_line_reading,
    arch_34_decimal_on_a_number_line_plotting,
    arch_35_grid_100_square_shaded_decimal_representation,
    arch_36_money_rand_cents_addition_total_cost,
    arch_37_money_rand_cents_subtraction_calculating_change,
    arch_38_money_multiplication_unit_price,
    arch_39_money_division_equal_split,
    arch_40_measurement_length_metres_to_centimetres_decimal,
    arch_41_measurement_mass_kilograms_to_grams_decimal,
    arch_42_measurement_capacity_litres_to_millilitres_decimal,
    arch_43_spot_the_error_ragged_decimal_addition_alignment,
    arch_44_spot_the_error_longer_decimal_is_larger_fallacy,
    arch_45_spot_the_error_trailing_zero_removal_confusion,
    arch_46_spot_the_error_decimal_multiplication_point_placement,
    arch_47_practical_context_fuel_pump_litres_and_cost,
    arch_48_practical_context_athletics_race_times_hundredths_second,
    arch_49_practical_context_supermarket_till_slip_rounding,
    arch_50_comprehensive_multi_step_decimal_word_problem,
]

SUBSKILLS: List[str] = [
    "01_place_value_identification_tenths_hundredths_thousandths",
    "02_digit_value_in_decimal_number",
    "03_convert_tenth_fraction_to_decimal",
    "04_convert_hundredth_fraction_to_decimal",
    "05_convert_thousandth_fraction_to_decimal",
    "06_convert_mixed_fraction_to_decimal",
    "07_convert_decimal_to_common_fraction_simplified",
    "08_expanded_notation_to_decimal_standard_form",
    "09_decimal_to_expanded_fraction_form",
    "10_comparing_two_decimal_numbers",
    "11_ordering_decimals_ascending_descending",
    "12_rounding_to_nearest_whole_number",
    "13_rounding_to_one_decimal_place_tenths",
    "14_rounding_to_two_decimal_places_hundredths",
    "15_adding_decimals_same_decimal_places",
    "16_adding_decimals_different_decimal_places_padding",
    "17_adding_three_decimal_numbers",
    "18_subtracting_decimals_same_decimal_places",
    "19_subtracting_decimals_with_borrowing",
    "20_subtracting_decimal_from_whole_number",
    "21_multiplying_decimal_by_10_100_1000",
    "22_dividing_decimal_by_10_100_1000",
    "23_multiplying_decimal_by_single_digit_whole_number",
    "24_multiplying_two_decimal_fractions",
    "25_dividing_decimal_by_whole_number",
    "26_dividing_whole_numbers_yielding_decimal_quotient",
    "27_common_fraction_half_quarter_to_decimal",
    "28_common_fraction_fifths_to_decimal",
    "29_common_fraction_eighths_to_decimal",
    "30_percentage_to_decimal_conversion",
    "31_decimal_to_percentage_conversion",
    "32_three_way_equivalence_table_fraction_decimal_pct",
    "33_decimal_on_a_number_line_reading",
    "34_decimal_on_a_number_line_plotting",
    "35_grid_100_square_shaded_decimal_representation",
    "36_money_rand_cents_addition_total_cost",
    "37_money_rand_cents_subtraction_calculating_change",
    "38_money_multiplication_unit_price",
    "39_money_division_equal_split",
    "40_measurement_length_metres_to_centimetres_decimal",
    "41_measurement_mass_kilograms_to_grams_decimal",
    "42_measurement_capacity_litres_to_millilitres_decimal",
    "43_spot_the_error_ragged_decimal_addition_alignment",
    "44_spot_the_error_longer_decimal_is_larger_fallacy",
    "45_spot_the_error_trailing_zero_removal_confusion",
    "46_spot_the_error_decimal_multiplication_point_placement",
    "47_practical_context_fuel_pump_litres_and_cost",
    "48_practical_context_athletics_race_times_hundredths_second",
    "49_practical_context_supermarket_till_slip_rounding",
    "50_comprehensive_multi_step_decimal_word_problem",
]

_SUBSKILL_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    name: builder for name, builder in zip(SUBSKILLS, ARCHETYPE_BUILDERS)
}


def generate_question(
    rng: Optional[random.Random] = None,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    """Generates a fully calibrated Grade 7 Decimal Fractions question."""
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
    payload.setdefault("topic", "The decimal notation for fractions")
    payload.setdefault("caps_weight_percent", 10.0)
    payload.setdefault("suggested_duration_mins", 3)
    payload.setdefault("mode", "elementary_" + payload.get("subskill", "decimals"))
    payload.setdefault(
        "marking_schema",
        [
            {"step": "Correct place value and decimal operation", "marks": 1, "type": "M"},
            {"step": "Correct decimal answer", "marks": max(1, payload.get("marks", 2) - 1), "type": "A"},
        ],
    )
    return payload


generate = generate_question
