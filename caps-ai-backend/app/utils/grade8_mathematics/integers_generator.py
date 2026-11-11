"""
Grade 8 Mathematics - Integers Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/02. Integers.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .integers_archetypes_01_25 import (
    arch_01_reading_winter_thermometer_subzero,
    arch_02_temperature_rise_through_zero,
    arch_03_temperature_drop_through_zero,
    arch_04_diurnal_temperature_range_calculation,
    arch_05_bank_overdraft_after_withdrawal,
    arch_06_deposit_clearing_partial_debt,
    arch_07_business_net_profit_and_loss_period,
    arch_08_mine_shaft_elevation_below_surface,
    arch_09_diver_depth_and_ascent,
    arch_10_number_line_missing_integers,
    arch_11_ordering_five_integers_ascending,
    arch_12_ordering_five_integers_descending,
    arch_13_comparing_integers_inequality_symbols,
    arch_14_absolute_value_and_distance_from_zero,
    arch_15_opposite_integers_reflection,
    arch_16_midpoint_between_positive_and_negative_integer,
    arch_17_consecutive_negative_integers,
    arch_18_number_line_vector_jump_addition,
    arch_19_number_line_vector_jump_subtraction,
    arch_20_rational_and_integer_classification,
    arch_21_addition_of_two_negative_integers,
    arch_22_addition_of_positive_and_negative_integer,
    arch_23_subtraction_of_positive_from_smaller_positive,
    arch_24_subtraction_of_positive_from_negative,
    arch_25_subtraction_of_negative_double_negative_rule,
)

from .integers_archetypes_26_50 import (
    arch_26_subtraction_of_negative_from_negative,
    arch_27_additive_inverse_zero_sum_property,
    arch_28_multi_term_addition_subtraction_chain,
    arch_29_multiplication_positive_by_negative,
    arch_30_multiplication_negative_by_negative,
    arch_31_product_of_three_signed_integers,
    arch_32_product_of_four_signed_integers,
    arch_33_division_negative_by_positive,
    arch_34_division_positive_by_negative,
    arch_35_division_negative_by_negative,
    arch_36_combined_multiplication_and_division,
    arch_37_square_of_negative_integer_in_parentheses,
    arch_38_square_of_negative_integer_without_parentheses,
    arch_39_cube_of_negative_integer,
    arch_40_fourth_power_of_negative_integer,
    arch_41_cube_root_of_negative_integer,
    arch_42_square_root_of_negative_non_real_drill,
    arch_43_sum_of_squares_and_cubes_with_negative_bases,
    arch_44_difference_of_powers_with_negative_bases,
    arch_45_bodmas_with_brackets_and_powers,
    arch_46_bodmas_nested_brackets_and_fractions,
    arch_47_distributive_property_over_negative_addition,
    arch_48_solving_one_step_equation_with_negative_integers,
    arch_49_solving_two_step_equation_with_negative_integers,
    arch_50_two_step_equation_with_brackets_and_negatives,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10
    arch_01_reading_winter_thermometer_subzero,
    arch_02_temperature_rise_through_zero,
    arch_03_temperature_drop_through_zero,
    arch_04_diurnal_temperature_range_calculation,
    arch_05_bank_overdraft_after_withdrawal,
    arch_06_deposit_clearing_partial_debt,
    arch_07_business_net_profit_and_loss_period,
    arch_08_mine_shaft_elevation_below_surface,
    arch_09_diver_depth_and_ascent,
    arch_10_number_line_missing_integers,
    # 11 - 20
    arch_11_ordering_five_integers_ascending,
    arch_12_ordering_five_integers_descending,
    arch_13_comparing_integers_inequality_symbols,
    arch_14_absolute_value_and_distance_from_zero,
    arch_15_opposite_integers_reflection,
    arch_16_midpoint_between_positive_and_negative_integer,
    arch_17_consecutive_negative_integers,
    arch_18_number_line_vector_jump_addition,
    arch_19_number_line_vector_jump_subtraction,
    arch_20_rational_and_integer_classification,
    # 21 - 28
    arch_21_addition_of_two_negative_integers,
    arch_22_addition_of_positive_and_negative_integer,
    arch_23_subtraction_of_positive_from_smaller_positive,
    arch_24_subtraction_of_positive_from_negative,
    arch_25_subtraction_of_negative_double_negative_rule,
    arch_26_subtraction_of_negative_from_negative,
    arch_27_additive_inverse_zero_sum_property,
    arch_28_multi_term_addition_subtraction_chain,
    # 29 - 36
    arch_29_multiplication_positive_by_negative,
    arch_30_multiplication_negative_by_negative,
    arch_31_product_of_three_signed_integers,
    arch_32_product_of_four_signed_integers,
    arch_33_division_negative_by_positive,
    arch_34_division_positive_by_negative,
    arch_35_division_negative_by_negative,
    arch_36_combined_multiplication_and_division,
    # 37 - 44
    arch_37_square_of_negative_integer_in_parentheses,
    arch_38_square_of_negative_integer_without_parentheses,
    arch_39_cube_of_negative_integer,
    arch_40_fourth_power_of_negative_integer,
    arch_41_cube_root_of_negative_integer,
    arch_42_square_root_of_negative_non_real_drill,
    arch_43_sum_of_squares_and_cubes_with_negative_bases,
    arch_44_difference_of_powers_with_negative_bases,
    # 45 - 50
    arch_45_bodmas_with_brackets_and_powers,
    arch_46_bodmas_nested_brackets_and_fractions,
    arch_47_distributive_property_over_negative_addition,
    arch_48_solving_one_step_equation_with_negative_integers,
    arch_49_solving_two_step_equation_with_negative_integers,
    arch_50_two_step_equation_with_brackets_and_negatives,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_reading_winter_thermometer_subzero",
    "02_temperature_rise_through_zero",
    "03_temperature_drop_through_zero",
    "04_diurnal_temperature_range_calculation",
    "05_bank_overdraft_after_withdrawal",
    "06_deposit_clearing_partial_debt",
    "07_business_net_profit_and_loss_period",
    "08_mine_shaft_elevation_below_surface",
    "09_diver_depth_and_ascent",
    "10_number_line_missing_integers",
    # 11 - 20
    "11_ordering_five_integers_ascending",
    "12_ordering_five_integers_descending",
    "13_comparing_integers_inequality_symbols",
    "14_absolute_value_and_distance_from_zero",
    "15_opposite_integers_reflection",
    "16_midpoint_between_positive_and_negative_integer",
    "17_consecutive_negative_integers",
    "18_number_line_vector_jump_addition",
    "19_number_line_vector_jump_subtraction",
    "20_rational_and_integer_classification",
    # 21 - 28
    "21_addition_of_two_negative_integers",
    "22_addition_of_positive_and_negative_integer",
    "23_subtraction_of_positive_from_smaller_positive",
    "24_subtraction_of_positive_from_negative",
    "25_subtraction_of_negative_double_negative_rule",
    "26_subtraction_of_negative_from_negative",
    "27_additive_inverse_zero_sum_property",
    "28_multi_term_addition_subtraction_chain",
    # 29 - 36
    "29_multiplication_positive_by_negative",
    "30_multiplication_negative_by_negative",
    "31_product_of_three_signed_integers",
    "32_product_of_four_signed_integers",
    "33_division_negative_by_positive",
    "34_division_positive_by_negative",
    "35_division_negative_by_negative",
    "36_combined_multiplication_and_division",
    # 37 - 44
    "37_square_of_negative_integer_in_parentheses",
    "38_square_of_negative_integer_without_parentheses",
    "39_cube_of_negative_integer",
    "40_fourth_power_of_negative_integer",
    "41_cube_root_of_negative_integer",
    "42_square_root_of_negative_non_real_drill",
    "43_sum_of_squares_and_cubes_with_negative_bases",
    "44_difference_of_powers_with_negative_bases",
    # 45 - 50
    "45_bodmas_with_brackets_and_powers",
    "46_bodmas_nested_brackets_and_fractions",
    "47_distributive_property_over_negative_addition",
    "48_solving_one_step_equation_with_negative_integers",
    "49_solving_two_step_equation_with_negative_integers",
    "50_two_step_equation_with_brackets_and_negatives",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["integers_bodmas_and_powers"] = arch_45_bodmas_with_brackets_and_powers
DISPATCH_TABLE["real_world_temperature_context"] = arch_01_reading_winter_thermometer_subzero
DISPATCH_TABLE["bank_overdraft_balance"] = arch_05_bank_overdraft_after_withdrawal
DISPATCH_TABLE["elevation_depth_context"] = arch_08_mine_shaft_elevation_below_surface
DISPATCH_TABLE["powers_negative_bases_comparison"] = arch_37_square_of_negative_integer_in_parentheses


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
        q.setdefault("topic", "Integers")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
