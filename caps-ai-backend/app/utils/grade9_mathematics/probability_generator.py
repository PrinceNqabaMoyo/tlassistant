"""Grade 9 Mathematics - Probability Generator (50 Semantic Archetypes).
=======================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 4 Topic: Probability
  - curriculum_docs_auto/Mathematics_Gr9/Term 4/03. Probability.md
  - Probability scale (0 to 1), fraction, decimal, percentage forms.
  - Single event probabilities: fair coins, standard dice, circular spinners, marble bags, 52-card decks.
  - Complementary events: P(not E) = 1 - P(E).
  - Experimental relative frequency vs theoretical probability; Law of Large Numbers.
  - Sample space enumeration: two coins, coin and die, two dice sum grid (36 outcomes).
  - Tree diagrams: two-stage independent events (with replacement) and dependent events (without replacement).
  - Two-way contingency tables: joint and marginal probabilities.
  - Venn diagrams: intersection, union, complement, mutually exclusive vs inclusive events.
  - Multi-stage decision trees and expected value.

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .probability_archetypes_01_25 import (
    arch_01_probability_scale_impossible_certain_words_to_numbers,
    arch_02_convert_probability_between_fraction_decimal_percentage,
    arch_03_single_event_fair_coin_toss,
    arch_04_single_event_fair_six_sided_die_even_odd,
    arch_05_single_event_fair_six_sided_die_prime_composite,
    arch_06_single_event_fair_six_sided_die_greater_than_threshold,
    arch_07_single_event_colored_spinner_equal_sectors,
    arch_08_single_event_colored_spinner_unequal_sectors,
    arch_09_single_event_bag_marbles_simplified_fraction,
    arch_10_single_event_standard_deck_suits,
    arch_11_single_event_standard_deck_face_cards,
    arch_12_single_event_standard_deck_red_ace,
    arch_13_complementary_event_not_landing_on_color,
    arch_14_complementary_event_not_rolling_six,
    arch_15_complementary_event_weather_forecast_rain,
    arch_16_experimental_relative_frequency_coin_toss_trials,
    arch_17_experimental_relative_frequency_die_roll_trials,
    arch_18_law_of_large_numbers_comparison_small_vs_large_trials,
    arch_19_sample_space_enumeration_two_coins,
    arch_20_compound_event_two_coins_both_heads,
    arch_21_compound_event_two_coins_at_least_one_tail,
    arch_22_sample_space_enumeration_coin_and_die,
    arch_23_compound_event_coin_heads_and_die_even,
    arch_24_sample_space_grid_sum_of_two_dice,
    arch_25_compound_event_sum_of_two_dice_equals_seven,
)
from .probability_archetypes_26_50 import (
    arch_26_compound_event_sum_of_two_dice_greater_than_ten,
    arch_27_compound_event_sum_of_two_dice_doubles,
    arch_28_tree_diagram_two_stage_coin_tosses,
    arch_29_tree_diagram_independent_drawing_with_replacement,
    arch_30_tree_diagram_dependent_drawing_without_replacement,
    arch_31_tree_diagram_weather_rain_consecutive_days,
    arch_32_two_way_table_gender_and_preferred_sport_joint_prob,
    arch_33_two_way_table_gender_and_preferred_sport_marginal_prob,
    arch_34_two_way_table_subject_choice_and_grade,
    arch_35_two_way_table_pass_fail_and_attendance,
    arch_36_venn_diagram_probability_two_sets_intersection,
    arch_37_venn_diagram_probability_two_sets_union,
    arch_38_venn_diagram_probability_complement_neither_set,
    arch_39_mutually_exclusive_events_definition_and_addition_rule,
    arch_40_non_mutually_exclusive_events_addition_rule_subtraction,
    arch_41_determining_fairness_of_game_expected_payout,
    arch_42_frequency_tree_hospital_test_results,
    arch_43_marble_bag_three_colors_probability_of_neither_color,
    arch_44_card_selection_without_replacement_two_aces,
    arch_45_sock_drawer_drawing_matching_pair_without_replacement,
    arch_46_traffic_light_independent_probability_two_consecutive_greens,
    arch_47_subject_grade_probability_from_school_contingency_table,
    arch_48_relative_frequency_prediction_for_future_large_trials,
    arch_49_compare_theoretical_probability_with_experimental_bias_check,
    arch_50_compound_multi_stage_probability_decision_tree_synthesis,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_probability_scale_impossible_certain_words_to_numbers": arch_01_probability_scale_impossible_certain_words_to_numbers,
    "02_convert_probability_between_fraction_decimal_percentage": arch_02_convert_probability_between_fraction_decimal_percentage,
    "03_single_event_fair_coin_toss": arch_03_single_event_fair_coin_toss,
    "04_single_event_fair_six_sided_die_even_odd": arch_04_single_event_fair_six_sided_die_even_odd,
    "05_single_event_fair_six_sided_die_prime_composite": arch_05_single_event_fair_six_sided_die_prime_composite,
    "06_single_event_fair_six_sided_die_greater_than_threshold": arch_06_single_event_fair_six_sided_die_greater_than_threshold,
    "07_single_event_colored_spinner_equal_sectors": arch_07_single_event_colored_spinner_equal_sectors,
    "08_single_event_colored_spinner_unequal_sectors": arch_08_single_event_colored_spinner_unequal_sectors,
    "09_single_event_bag_marbles_simplified_fraction": arch_09_single_event_bag_marbles_simplified_fraction,
    "10_single_event_standard_deck_suits": arch_10_single_event_standard_deck_suits,
    "11_single_event_standard_deck_face_cards": arch_11_single_event_standard_deck_face_cards,
    "12_single_event_standard_deck_red_ace": arch_12_single_event_standard_deck_red_ace,
    "13_complementary_event_not_landing_on_color": arch_13_complementary_event_not_landing_on_color,
    "14_complementary_event_not_rolling_six": arch_14_complementary_event_not_rolling_six,
    "15_complementary_event_weather_forecast_rain": arch_15_complementary_event_weather_forecast_rain,
    "16_experimental_relative_frequency_coin_toss_trials": arch_16_experimental_relative_frequency_coin_toss_trials,
    "17_experimental_relative_frequency_die_roll_trials": arch_17_experimental_relative_frequency_die_roll_trials,
    "18_law_of_large_numbers_comparison_small_vs_large_trials": arch_18_law_of_large_numbers_comparison_small_vs_large_trials,
    "19_sample_space_enumeration_two_coins": arch_19_sample_space_enumeration_two_coins,
    "20_compound_event_two_coins_both_heads": arch_20_compound_event_two_coins_both_heads,
    "21_compound_event_two_coins_at_least_one_tail": arch_21_compound_event_two_coins_at_least_one_tail,
    "22_sample_space_enumeration_coin_and_die": arch_22_sample_space_enumeration_coin_and_die,
    "23_compound_event_coin_heads_and_die_even": arch_23_compound_event_coin_heads_and_die_even,
    "24_sample_space_grid_sum_of_two_dice": arch_24_sample_space_grid_sum_of_two_dice,
    "25_compound_event_sum_of_two_dice_equals_seven": arch_25_compound_event_sum_of_two_dice_equals_seven,
    "26_compound_event_sum_of_two_dice_greater_than_ten": arch_26_compound_event_sum_of_two_dice_greater_than_ten,
    "27_compound_event_sum_of_two_dice_doubles": arch_27_compound_event_sum_of_two_dice_doubles,
    "28_tree_diagram_two_stage_coin_tosses": arch_28_tree_diagram_two_stage_coin_tosses,
    "29_tree_diagram_independent_drawing_with_replacement": arch_29_tree_diagram_independent_drawing_with_replacement,
    "30_tree_diagram_dependent_drawing_without_replacement": arch_30_tree_diagram_dependent_drawing_without_replacement,
    "31_tree_diagram_weather_rain_consecutive_days": arch_31_tree_diagram_weather_rain_consecutive_days,
    "32_two_way_table_gender_and_preferred_sport_joint_prob": arch_32_two_way_table_gender_and_preferred_sport_joint_prob,
    "33_two_way_table_gender_and_preferred_sport_marginal_prob": arch_33_two_way_table_gender_and_preferred_sport_marginal_prob,
    "34_two_way_table_subject_choice_and_grade": arch_34_two_way_table_subject_choice_and_grade,
    "35_two_way_table_pass_fail_and_attendance": arch_35_two_way_table_pass_fail_and_attendance,
    "36_venn_diagram_probability_two_sets_intersection": arch_36_venn_diagram_probability_two_sets_intersection,
    "37_venn_diagram_probability_two_sets_union": arch_37_venn_diagram_probability_two_sets_union,
    "38_venn_diagram_probability_complement_neither_set": arch_38_venn_diagram_probability_complement_neither_set,
    "39_mutually_exclusive_events_definition_and_addition_rule": arch_39_mutually_exclusive_events_definition_and_addition_rule,
    "40_non_mutually_exclusive_events_addition_rule_subtraction": arch_40_non_mutually_exclusive_events_addition_rule_subtraction,
    "41_determining_fairness_of_game_expected_payout": arch_41_determining_fairness_of_game_expected_payout,
    "42_frequency_tree_hospital_test_results": arch_42_frequency_tree_hospital_test_results,
    "43_marble_bag_three_colors_probability_of_neither_color": arch_43_marble_bag_three_colors_probability_of_neither_color,
    "44_card_selection_without_replacement_two_aces": arch_44_card_selection_without_replacement_two_aces,
    "45_sock_drawer_drawing_matching_pair_without_replacement": arch_45_sock_drawer_drawing_matching_pair_without_replacement,
    "46_traffic_light_independent_probability_two_consecutive_greens": arch_46_traffic_light_independent_probability_two_consecutive_greens,
    "47_subject_grade_probability_from_school_contingency_table": arch_47_subject_grade_probability_from_school_contingency_table,
    "48_relative_frequency_prediction_for_future_large_trials": arch_48_relative_frequency_prediction_for_future_large_trials,
    "49_compare_theoretical_probability_with_experimental_bias_check": arch_49_compare_theoretical_probability_with_experimental_bias_check,
    "50_compound_multi_stage_probability_decision_tree_synthesis": arch_50_compound_multi_stage_probability_decision_tree_synthesis,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate_grade9_probability_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)

    selected_subskill = subskill
    if not selected_subskill or selected_subskill not in DISPATCH_TABLE:
        if archetype_index is not None and 0 <= archetype_index < len(SUBSKILLS):
            selected_subskill = SUBSKILLS[archetype_index]
        elif mode.startswith("elementary_"):
            target_stem = mode.replace("elementary_", "")
            candidates = [s for s in SUBSKILLS if target_stem in s]
            selected_subskill = candidates[0] if candidates else r.choice(SUBSKILLS)
        else:
            selected_subskill = r.choice(SUBSKILLS)

    builder = DISPATCH_TABLE[selected_subskill]
    q = builder(r)

    # 6-Pillar Metadata Enforcements
    q.setdefault("topic", "Probability")
    q.setdefault("subject", "Mathematics")
    q.setdefault("grade", "9")
    q.setdefault("term", 4)
    q.setdefault("caps_weight_percent", 5.0)
    q.setdefault("suggested_duration_mins", 3)
    q.setdefault("difficulty", "medium")
    q.setdefault("subskill", selected_subskill)
    q.setdefault("archetype", selected_subskill)
    q.setdefault("interactive", False)

    return q


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    mode: str = "compound",
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]] | Dict[str, Any]:
    if count == 1:
        return generate_grade9_probability_question(
            seed=seed, subskill=subskill, archetype_index=archetype_index, mode=mode, **kwargs
        )
    base_seed = seed if seed is not None else random.randint(100, 999999)
    out: List[Dict[str, Any]] = []
    for i in range(count):
        sub_seed = base_seed + i * 37
        sub = subskill if subskill else (SUBSKILLS[i % len(SUBSKILLS)] if archetype_index is None else None)
        out.append(
            generate_grade9_probability_question(
                seed=sub_seed, subskill=sub, archetype_index=archetype_index, mode=mode, **kwargs
            )
        )
    return out
