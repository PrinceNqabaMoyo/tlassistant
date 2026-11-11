"""
Grade 7 Mathematics - Integers Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/01. Integers.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .integers_archetypes_01_25 import (
    arch_01_reading_thermometer_above_zero,
    arch_02_reading_thermometer_below_zero,
    arch_03_temperature_rise_from_negative_to_positive,
    arch_04_temperature_drop_from_positive_to_negative,
    arch_05_temperature_difference_two_south_african_cities,
    arch_06_coldest_to_warmest_temperature_ranking,
    arch_07_diurnal_temperature_range_calculation,
    arch_08_wind_chill_effective_temperature_subtraction,
    arch_09_bank_overdraft_balance_after_withdrawal,
    arch_10_deposit_into_overdrawn_account,
    arch_11_business_profit_and_loss_net_position,
    arch_12_debt_settlement_multi_creditor_calculation,
    arch_13_stock_market_point_gain_and_drop,
    arch_14_budget_deficit_and_surplus_comparison,
    arch_15_combined_cash_assets_and_supplier_debts,
    arch_16_net_worth_negative_equity_assessment,
    arch_17_submarine_depth_and_ascent_distance,
    arch_18_deep_mine_shaft_elevation_below_surface,
    arch_19_diver_depth_relative_to_sea_level,
    arch_20_altitude_drop_from_mountain_peak_to_trench,
    arch_21_vertical_distance_between_two_elevations,
    arch_22_underground_parking_basement_levels,
    arch_23_drone_altitude_relative_to_cliff_edge,
    arch_24_cave_exploration_descent_and_climb,
    arch_25_identifying_missing_integers_on_number_line,
)

from .integers_archetypes_26_50 import (
    arch_26_locating_negative_integers_between_benchmarks,
    arch_27_comparing_integers_with_inequality_symbols,
    arch_28_ordering_five_integers_ascending,
    arch_29_ordering_five_integers_descending,
    arch_30_integer_distance_from_zero_absolute_value,
    arch_31_midpoint_between_positive_and_negative_integer,
    arch_32_opposite_integers_reflection_across_zero,
    arch_33_consecutive_integers_predecessor_and_successor,
    arch_34_number_line_vector_jump_representation,
    arch_35_addition_of_two_negative_integers,
    arch_36_addition_of_positive_and_negative_integer,
    arch_37_additive_inverse_property_zero_sum,
    arch_38_subtracting_positive_from_smaller_positive,
    arch_39_subtracting_positive_from_negative_integer,
    arch_40_subtracting_negative_integer_double_negative_rule,
    arch_41_subtracting_negative_from_negative_integer,
    arch_42_three_term_addition_and_subtraction_chain,
    arch_43_missing_addend_positive_sum_x_plus_a_equals_b,
    arch_44_missing_addend_negative_sum_x_plus_a_equals_neg_b,
    arch_45_missing_subtrahend_a_minus_x_equals_neg_b,
    arch_46_missing_minuend_x_minus_a_equals_neg_b,
    arch_47_evaluating_truth_value_of_integer_inequality,
    arch_48_integer_bracket_simplification_sign_rules,
    arch_49_integer_word_problem_multi_step_model,
    arch_50_two_step_integer_balance_equation,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 08: Thermometers & Temperature
    arch_01_reading_thermometer_above_zero,
    arch_02_reading_thermometer_below_zero,
    arch_03_temperature_rise_from_negative_to_positive,
    arch_04_temperature_drop_from_positive_to_negative,
    arch_05_temperature_difference_two_south_african_cities,
    arch_06_coldest_to_warmest_temperature_ranking,
    arch_07_diurnal_temperature_range_calculation,
    arch_08_wind_chill_effective_temperature_subtraction,
    # 09 - 16: Financial Contexts
    arch_09_bank_overdraft_balance_after_withdrawal,
    arch_10_deposit_into_overdrawn_account,
    arch_11_business_profit_and_loss_net_position,
    arch_12_debt_settlement_multi_creditor_calculation,
    arch_13_stock_market_point_gain_and_drop,
    arch_14_budget_deficit_and_surplus_comparison,
    arch_15_combined_cash_assets_and_supplier_debts,
    arch_16_net_worth_negative_equity_assessment,
    # 17 - 24: Elevation & Sea Level
    arch_17_submarine_depth_and_ascent_distance,
    arch_18_deep_mine_shaft_elevation_below_surface,
    arch_19_diver_depth_relative_to_sea_level,
    arch_20_altitude_drop_from_mountain_peak_to_trench,
    arch_21_vertical_distance_between_two_elevations,
    arch_22_underground_parking_basement_levels,
    arch_23_drone_altitude_relative_to_cliff_edge,
    arch_24_cave_exploration_descent_and_climb,
    # 25 - 34: Number Lines, Ordering & Comparing
    arch_25_identifying_missing_integers_on_number_line,
    arch_26_locating_negative_integers_between_benchmarks,
    arch_27_comparing_integers_with_inequality_symbols,
    arch_28_ordering_five_integers_ascending,
    arch_29_ordering_five_integers_descending,
    arch_30_integer_distance_from_zero_absolute_value,
    arch_31_midpoint_between_positive_and_negative_integer,
    arch_32_opposite_integers_reflection_across_zero,
    arch_33_consecutive_integers_predecessor_and_successor,
    arch_34_number_line_vector_jump_representation,
    # 35 - 42: Integer Addition & Subtraction Fundamentals
    arch_35_addition_of_two_negative_integers,
    arch_36_addition_of_positive_and_negative_integer,
    arch_37_additive_inverse_property_zero_sum,
    arch_38_subtracting_positive_from_smaller_positive,
    arch_39_subtracting_positive_from_negative_integer,
    arch_40_subtracting_negative_integer_double_negative_rule,
    arch_41_subtracting_negative_from_negative_integer,
    arch_42_three_term_addition_and_subtraction_chain,
    # 43 - 50: Algebraic Thinking & Missing Value Equations
    arch_43_missing_addend_positive_sum_x_plus_a_equals_b,
    arch_44_missing_addend_negative_sum_x_plus_a_equals_neg_b,
    arch_45_missing_subtrahend_a_minus_x_equals_neg_b,
    arch_46_missing_minuend_x_minus_a_equals_neg_b,
    arch_47_evaluating_truth_value_of_integer_inequality,
    arch_48_integer_bracket_simplification_sign_rules,
    arch_49_integer_word_problem_multi_step_model,
    arch_50_two_step_integer_balance_equation,
]

SUBSKILLS = [
    # 01 - 08
    "01_reading_thermometer_above_zero",
    "02_reading_thermometer_below_zero",
    "03_temperature_rise_from_negative_to_positive",
    "04_temperature_drop_from_positive_to_negative",
    "05_temperature_difference_two_south_african_cities",
    "06_coldest_to_warmest_temperature_ranking",
    "07_diurnal_temperature_range_calculation",
    "08_wind_chill_effective_temperature_subtraction",
    # 09 - 16
    "09_bank_overdraft_balance_after_withdrawal",
    "10_deposit_into_overdrawn_account",
    "11_business_profit_and_loss_net_position",
    "12_debt_settlement_multi_creditor_calculation",
    "13_stock_market_point_gain_and_drop",
    "14_budget_deficit_and_surplus_comparison",
    "15_combined_cash_assets_and_supplier_debts",
    "16_net_worth_negative_equity_assessment",
    # 17 - 24
    "17_submarine_depth_and_ascent_distance",
    "18_deep_mine_shaft_elevation_below_surface",
    "19_diver_depth_relative_to_sea_level",
    "20_altitude_drop_from_mountain_peak_to_trench",
    "21_vertical_distance_between_two_elevations",
    "22_underground_parking_basement_levels",
    "23_drone_altitude_relative_to_cliff_edge",
    "24_cave_exploration_descent_and_climb",
    # 25 - 34
    "25_identifying_missing_integers_on_number_line",
    "26_locating_negative_integers_between_benchmarks",
    "27_comparing_integers_with_inequality_symbols",
    "28_ordering_five_integers_ascending",
    "29_ordering_five_integers_descending",
    "30_integer_distance_from_zero_absolute_value",
    "31_midpoint_between_positive_and_negative_integer",
    "32_opposite_integers_reflection_across_zero",
    "33_consecutive_integers_predecessor_and_successor",
    "34_number_line_vector_jump_representation",
    # 35 - 42
    "35_addition_of_two_negative_integers",
    "36_addition_of_positive_and_negative_integer",
    "37_additive_inverse_property_zero_sum",
    "38_subtracting_positive_from_smaller_positive",
    "39_subtracting_positive_from_negative_integer",
    "40_subtracting_negative_integer_double_negative_rule",
    "41_subtracting_negative_from_negative_integer",
    "42_three_term_addition_and_subtraction_chain",
    # 43 - 50
    "43_missing_addend_positive_sum_x_plus_a_equals_b",
    "44_missing_addend_negative_sum_x_plus_a_equals_neg_b",
    "45_missing_subtrahend_a_minus_x_equals_neg_b",
    "46_missing_minuend_x_minus_a_equals_neg_b",
    "47_evaluating_truth_value_of_integer_inequality",
    "48_integer_bracket_simplification_sign_rules",
    "49_integer_word_problem_multi_step_model",
    "50_two_step_integer_balance_equation",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# Index aliases (1-based)
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["integers_ordering_number_line"] = arch_25_identifying_missing_integers_on_number_line
DISPATCH_TABLE["integers_in_context"] = arch_01_reading_thermometer_above_zero
DISPATCH_TABLE["integer_arithmetic_rules"] = arch_35_addition_of_two_negative_integers
DISPATCH_TABLE["integers_subskill_4"] = arch_09_bank_overdraft_balance_after_withdrawal
DISPATCH_TABLE["integers_subskill_5"] = arch_37_additive_inverse_property_zero_sum


def get_subskills() -> List[str]:
    """Returns the full list of 50 semantic subskill archetype IDs."""
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
    Main entry point for Grade 7 Integers Generator.
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
        q.setdefault("topic", "Integers")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
