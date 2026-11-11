"""
Grade 8 Mathematics - Fractions in Decimal Notation Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Fractions in decimal notation.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .decimal_fractions_archetypes_01_25 import (
    arch_01_place_value_identification_tenths_hundredths_thousandths,
    arch_02_ordering_positive_decimals_ascending,
    arch_03_ordering_positive_decimals_descending,
    arch_04_ordering_signed_decimals_ascending,
    arch_05_comparing_two_decimals_inequality,
    arch_06_finding_decimal_between_two_given_decimals,
    arch_07_rounding_to_nearest_whole_number,
    arch_08_rounding_to_one_decimal_place,
    arch_09_rounding_to_two_decimal_places,
    arch_10_rounding_to_three_decimal_places,
    arch_11_reading_value_from_calibrated_number_line,
    arch_12_identifying_letter_for_decimal_on_number_line,
    arch_13_converting_tenth_hundredth_thousandth_fraction_to_decimal,
    arch_14_converting_simple_fraction_to_decimal_via_powers_of_ten,
    arch_15_converting_improper_fraction_to_decimal,
    arch_16_converting_mixed_number_to_decimal,
    arch_17_converting_terminating_decimal_to_simplified_fraction,
    arch_18_converting_mixed_decimal_to_simplified_mixed_number,
    arch_19_converting_decimal_to_percentage,
    arch_20_converting_percentage_to_decimal,
    arch_21_converting_common_fraction_to_percentage_via_decimal,
    arch_22_identifying_terminating_vs_recurring_decimal,
    arch_23_recognizing_basic_recurring_decimal_notation,
    arch_24_completing_fraction_decimal_percentage_equivalence_table,
    arch_25_comparing_fraction_and_decimal_using_inequality,
)

from .decimal_fractions_archetypes_26_50 import (
    arch_26_addition_of_decimals_same_decimal_places,
    arch_27_addition_of_decimals_different_decimal_places,
    arch_28_subtraction_of_decimals_same_decimal_places,
    arch_29_subtraction_of_decimals_borrowing_across_zero,
    arch_30_combined_addition_and_subtraction_with_parentheses,
    arch_31_multiplication_of_decimal_by_power_of_ten,
    arch_32_division_of_decimal_by_power_of_ten,
    arch_33_multiplication_of_decimal_by_single_digit_whole_number,
    arch_34_multiplication_of_decimal_by_two_digit_whole_number,
    arch_35_multiplication_of_two_decimal_fractions,
    arch_36_squaring_a_decimal_fraction,
    arch_37_cubing_a_decimal_fraction,
    arch_38_square_root_of_decimal_fraction,
    arch_39_cube_root_of_decimal_fraction,
    arch_40_division_of_decimal_by_single_digit_whole_number,
    arch_41_division_of_decimal_by_decimal_divisor,
    arch_42_order_of_operations_bodmas_with_decimals,
    arch_43_real_world_money_shopping_budget_and_change,
    arch_44_real_world_unit_pricing_best_buy_comparison,
    arch_45_real_world_metric_length_conversion_decimals,
    arch_46_real_world_metric_mass_conversion_decimals,
    arch_47_real_world_metric_capacity_conversion_decimals,
    arch_48_geometry_perimeter_of_polygon_with_decimal_dimensions,
    arch_49_geometry_area_of_rectangle_with_decimal_dimensions,
    arch_50_real_world_fuel_consumption_rate_calculation,
)


BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10
    arch_01_place_value_identification_tenths_hundredths_thousandths,
    arch_02_ordering_positive_decimals_ascending,
    arch_03_ordering_positive_decimals_descending,
    arch_04_ordering_signed_decimals_ascending,
    arch_05_comparing_two_decimals_inequality,
    arch_06_finding_decimal_between_two_given_decimals,
    arch_07_rounding_to_nearest_whole_number,
    arch_08_rounding_to_one_decimal_place,
    arch_09_rounding_to_two_decimal_places,
    arch_10_rounding_to_three_decimal_places,
    # 11 - 20
    arch_11_reading_value_from_calibrated_number_line,
    arch_12_identifying_letter_for_decimal_on_number_line,
    arch_13_converting_tenth_hundredth_thousandth_fraction_to_decimal,
    arch_14_converting_simple_fraction_to_decimal_via_powers_of_ten,
    arch_15_converting_improper_fraction_to_decimal,
    arch_16_converting_mixed_number_to_decimal,
    arch_17_converting_terminating_decimal_to_simplified_fraction,
    arch_18_converting_mixed_decimal_to_simplified_mixed_number,
    arch_19_converting_decimal_to_percentage,
    arch_20_converting_percentage_to_decimal,
    # 21 - 28
    arch_21_converting_common_fraction_to_percentage_via_decimal,
    arch_22_identifying_terminating_vs_recurring_decimal,
    arch_23_recognizing_basic_recurring_decimal_notation,
    arch_24_completing_fraction_decimal_percentage_equivalence_table,
    arch_25_comparing_fraction_and_decimal_using_inequality,
    arch_26_addition_of_decimals_same_decimal_places,
    arch_27_addition_of_decimals_different_decimal_places,
    arch_28_subtraction_of_decimals_same_decimal_places,
    # 29 - 36
    arch_29_subtraction_of_decimals_borrowing_across_zero,
    arch_30_combined_addition_and_subtraction_with_parentheses,
    arch_31_multiplication_of_decimal_by_power_of_ten,
    arch_32_division_of_decimal_by_power_of_ten,
    arch_33_multiplication_of_decimal_by_single_digit_whole_number,
    arch_34_multiplication_of_decimal_by_two_digit_whole_number,
    arch_35_multiplication_of_two_decimal_fractions,
    arch_36_squaring_a_decimal_fraction,
    # 37 - 44
    arch_37_cubing_a_decimal_fraction,
    arch_38_square_root_of_decimal_fraction,
    arch_39_cube_root_of_decimal_fraction,
    arch_40_division_of_decimal_by_single_digit_whole_number,
    arch_41_division_of_decimal_by_decimal_divisor,
    arch_42_order_of_operations_bodmas_with_decimals,
    arch_43_real_world_money_shopping_budget_and_change,
    arch_44_real_world_unit_pricing_best_buy_comparison,
    # 45 - 50
    arch_45_real_world_metric_length_conversion_decimals,
    arch_46_real_world_metric_mass_conversion_decimals,
    arch_47_real_world_metric_capacity_conversion_decimals,
    arch_48_geometry_perimeter_of_polygon_with_decimal_dimensions,
    arch_49_geometry_area_of_rectangle_with_decimal_dimensions,
    arch_50_real_world_fuel_consumption_rate_calculation,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_place_value_identification_tenths_hundredths_thousandths",
    "02_ordering_positive_decimals_ascending",
    "03_ordering_positive_decimals_descending",
    "04_ordering_signed_decimals_ascending",
    "05_comparing_two_decimals_inequality",
    "06_finding_decimal_between_two_given_decimals",
    "07_rounding_to_nearest_whole_number",
    "08_rounding_to_one_decimal_place",
    "09_rounding_to_two_decimal_places",
    "10_rounding_to_three_decimal_places",
    # 11 - 20
    "11_reading_value_from_calibrated_number_line",
    "12_identifying_letter_for_decimal_on_number_line",
    "13_converting_tenth_hundredth_thousandth_fraction_to_decimal",
    "14_converting_simple_fraction_to_decimal_via_powers_of_ten",
    "15_converting_improper_fraction_to_decimal",
    "16_converting_mixed_number_to_decimal",
    "17_converting_terminating_decimal_to_simplified_fraction",
    "18_converting_mixed_decimal_to_simplified_mixed_number",
    "19_converting_decimal_to_percentage",
    "20_converting_percentage_to_decimal",
    # 21 - 28
    "21_converting_common_fraction_to_percentage_via_decimal",
    "22_identifying_terminating_vs_recurring_decimal",
    "23_recognizing_basic_recurring_decimal_notation",
    "24_completing_fraction_decimal_percentage_equivalence_table",
    "25_comparing_fraction_and_decimal_using_inequality",
    "26_addition_of_decimals_same_decimal_places",
    "27_addition_of_decimals_different_decimal_places",
    "28_subtraction_of_decimals_same_decimal_places",
    # 29 - 36
    "29_subtraction_of_decimals_borrowing_across_zero",
    "30_combined_addition_and_subtraction_with_parentheses",
    "31_multiplication_of_decimal_by_power_of_ten",
    "32_division_of_decimal_by_power_of_ten",
    "33_multiplication_of_decimal_by_single_digit_whole_number",
    "34_multiplication_of_decimal_by_two_digit_whole_number",
    "35_multiplication_of_two_decimal_fractions",
    "36_squaring_a_decimal_fraction",
    # 37 - 44
    "37_cubing_a_decimal_fraction",
    "38_square_root_of_decimal_fraction",
    "39_cube_root_of_decimal_fraction",
    "40_division_of_decimal_by_single_digit_whole_number",
    "41_division_of_decimal_by_decimal_divisor",
    "42_order_of_operations_bodmas_with_decimals",
    "43_real_world_money_shopping_budget_and_change",
    "44_real_world_unit_pricing_best_buy_comparison",
    # 45 - 50
    "45_real_world_metric_length_conversion_decimals",
    "46_real_world_metric_mass_conversion_decimals",
    "47_real_world_metric_capacity_conversion_decimals",
    "48_geometry_perimeter_of_polygon_with_decimal_dimensions",
    "49_geometry_area_of_rectangle_with_decimal_dimensions",
    "50_real_world_fuel_consumption_rate_calculation",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases
DISPATCH_TABLE["decimal_place_value_and_ordering"] = arch_02_ordering_positive_decimals_ascending
DISPATCH_TABLE["fraction_decimal_percentage_conversions"] = arch_14_converting_simple_fraction_to_decimal_via_powers_of_ten
DISPATCH_TABLE["decimal_four_operations"] = arch_26_addition_of_decimals_same_decimal_places
DISPATCH_TABLE["decimal_squares_cubes_and_roots"] = arch_36_squaring_a_decimal_fraction
DISPATCH_TABLE["decimal_financial_and_measurement_context"] = arch_43_real_world_money_shopping_budget_and_change


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
        q.setdefault("topic", "Fractions in decimal notation")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
