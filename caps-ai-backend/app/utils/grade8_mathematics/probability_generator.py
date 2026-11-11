"""Grade 8 Mathematics — Probability Generator.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 4/03. Probability.md

Expanded to 50 distinct semantic archetypes covering:
  - Probability scale: words (impossible, unlikely, even, likely, certain) and bounds (0 to 1).
  - Conversions: common fraction, decimal comma {,}, percentage.
  - Outcomes vs Events: definitions and concrete dice/coin distinctions.
  - Theoretical probability: fair coins, 6-sided dice, 8-sided octahedral dice.
  - Relative frequency: experimental tallies, calculation, comparison with theoretical values, Law of Large Numbers.
  - Fairness: mathematical criteria, fair dice games vs asymmetric carnival/operator games.
  - Spinners: equal and unequal sectors (180°, 90°).
  - Colored items: marbles/counters, complementary events (not red), effect of adding/removing.
  - Playing cards: 52-card standard deck, 4 suits (13 cards), face cards (12 cards), aces.
  - Compound / Combined events (2-stage):
    * Two coins: tree diagrams, exactly one head, at least one tail.
    * Coin and die: 12-outcome sample space, heads + even, tails + prime.
    * Two dice: 36-outcome two-way table, sum of 7, sum > 9, doubles, differences, fairness.
    * Two spinners: combined grid.
    * Consecutive draws: with replacement vs without replacement.
    * Independent events multiplication rule P(A and B) = P(A) * P(B).
    * Predictions: expected occurrences in N trials (Expected = N * P).
    * Two-way tables: survey data, conditional subgroup frequency.
    * Practical contexts: quality control defectives, Gambler's Fallacy, raffle tickets.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .probability_archetypes_01_25 import (
    arch_01_probability_scale_word_descriptions_mapping,
    arch_02_probability_scale_numerical_bounds_zero_to_one,
    arch_03_convert_probability_fraction_decimal_percentage,
    arch_04_distinguish_outcome_vs_event_definitions,
    arch_05_sample_space_listing_single_coin_and_dice,
    arch_06_theoretical_probability_single_fair_coin_heads_or_tails,
    arch_07_theoretical_probability_single_dice_specific_number,
    arch_08_theoretical_probability_single_dice_even_odd_numbers,
    arch_09_theoretical_probability_single_dice_prime_numbers,
    arch_10_theoretical_probability_single_dice_greater_or_less_than_threshold,
    arch_11_theoretical_probability_eight_sided_octahedral_dice,
    arch_12_relative_frequency_calculation_coin_flips,
    arch_13_relative_frequency_calculation_dice_rolls,
    arch_14_relative_frequency_vs_theoretical_probability_comparison,
    arch_15_law_of_large_numbers_increased_trials_convergence,
    arch_16_fair_vs_unfair_game_definition_and_criterion,
    arch_17_fair_game_analysis_dice_rules_even_vs_odd,
    arch_18_unfair_game_analysis_asymmetric_scoring_rules,
    arch_19_spinner_equal_sectors_probability,
    arch_20_spinner_unequal_sectors_probability,
    arch_21_marbles_in_bag_single_color_selection,
    arch_22_marbles_in_bag_not_color_complementary_event,
    arch_23_marbles_in_bag_adding_or_removing_marbles_effect,
    arch_24_standard_playing_cards_suit_selection,
    arch_25_standard_playing_cards_face_card_or_ace,
)
from .probability_archetypes_26_50 import (
    arch_26_complementary_events_sum_to_one_rule,
    arch_27_weather_forecast_percentage_precipitation_probability,
    arch_28_two_coins_sample_space_tree_diagram,
    arch_29_two_coins_probability_exactly_one_head,
    arch_30_two_coins_probability_at_least_one_tail,
    arch_31_coin_and_dice_combined_outcomes_sample_space_12,
    arch_32_coin_and_dice_probability_heads_and_even_number,
    arch_33_coin_and_dice_probability_tails_and_prime_number,
    arch_34_two_dice_two_way_table_sample_space_36,
    arch_35_two_dice_probability_sum_equals_seven,
    arch_36_two_dice_probability_sum_greater_than_nine,
    arch_37_two_dice_probability_doubles_matching_numbers,
    arch_38_two_dice_probability_difference_of_numbers,
    arch_39_two_dice_game_fairness_evaluation_sum_rules,
    arch_40_two_spinners_combined_outcomes_two_way_table,
    arch_41_drawing_two_counters_with_replacement_tree_diagram,
    arch_42_drawing_two_counters_without_replacement_fraction_change,
    arch_43_two_stage_event_independent_events_multiplication_rule,
    arch_44_predicting_number_of_times_event_occurs_in_n_trials,
    arch_45_survey_data_probability_two_way_table_gender_sport,
    arch_46_survey_data_conditional_frequency_subset_selection,
    arch_47_quality_control_defective_items_probability,
    arch_48_probability_error_analysis_gamblers_fallacy,
    arch_49_probability_error_analysis_ignoring_order_in_outcomes,
    arch_50_compound_probability_word_problem_school_raffle_tickets,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_probability_scale_word_descriptions_mapping": arch_01_probability_scale_word_descriptions_mapping,
    "02_probability_scale_numerical_bounds_zero_to_one": arch_02_probability_scale_numerical_bounds_zero_to_one,
    "03_convert_probability_fraction_decimal_percentage": arch_03_convert_probability_fraction_decimal_percentage,
    "04_distinguish_outcome_vs_event_definitions": arch_04_distinguish_outcome_vs_event_definitions,
    "05_sample_space_listing_single_coin_and_dice": arch_05_sample_space_listing_single_coin_and_dice,
    "06_theoretical_probability_single_fair_coin_heads_or_tails": arch_06_theoretical_probability_single_fair_coin_heads_or_tails,
    "07_theoretical_probability_single_dice_specific_number": arch_07_theoretical_probability_single_dice_specific_number,
    "08_theoretical_probability_single_dice_even_odd_numbers": arch_08_theoretical_probability_single_dice_even_odd_numbers,
    "09_theoretical_probability_single_dice_prime_numbers": arch_09_theoretical_probability_single_dice_prime_numbers,
    "10_theoretical_probability_single_dice_greater_or_less_than_threshold": arch_10_theoretical_probability_single_dice_greater_or_less_than_threshold,
    "11_theoretical_probability_eight_sided_octahedral_dice": arch_11_theoretical_probability_eight_sided_octahedral_dice,
    "12_relative_frequency_calculation_coin_flips": arch_12_relative_frequency_calculation_coin_flips,
    "13_relative_frequency_calculation_dice_rolls": arch_13_relative_frequency_calculation_dice_rolls,
    "14_relative_frequency_vs_theoretical_probability_comparison": arch_14_relative_frequency_vs_theoretical_probability_comparison,
    "15_law_of_large_numbers_increased_trials_convergence": arch_15_law_of_large_numbers_increased_trials_convergence,
    "16_fair_vs_unfair_game_definition_and_criterion": arch_16_fair_vs_unfair_game_definition_and_criterion,
    "17_fair_game_analysis_dice_rules_even_vs_odd": arch_17_fair_game_analysis_dice_rules_even_vs_odd,
    "18_unfair_game_analysis_asymmetric_scoring_rules": arch_18_unfair_game_analysis_asymmetric_scoring_rules,
    "19_spinner_equal_sectors_probability": arch_19_spinner_equal_sectors_probability,
    "20_spinner_unequal_sectors_probability": arch_20_spinner_unequal_sectors_probability,
    "21_marbles_in_bag_single_color_selection": arch_21_marbles_in_bag_single_color_selection,
    "22_marbles_in_bag_not_color_complementary_event": arch_22_marbles_in_bag_not_color_complementary_event,
    "23_marbles_in_bag_adding_or_removing_marbles_effect": arch_23_marbles_in_bag_adding_or_removing_marbles_effect,
    "24_standard_playing_cards_suit_selection": arch_24_standard_playing_cards_suit_selection,
    "25_standard_playing_cards_face_card_or_ace": arch_25_standard_playing_cards_face_card_or_ace,
    "26_complementary_events_sum_to_one_rule": arch_26_complementary_events_sum_to_one_rule,
    "27_weather_forecast_percentage_precipitation_probability": arch_27_weather_forecast_percentage_precipitation_probability,
    "28_two_coins_sample_space_tree_diagram": arch_28_two_coins_sample_space_tree_diagram,
    "29_two_coins_probability_exactly_one_head": arch_29_two_coins_probability_exactly_one_head,
    "30_two_coins_probability_at_least_one_tail": arch_30_two_coins_probability_at_least_one_tail,
    "31_coin_and_dice_combined_outcomes_sample_space_12": arch_31_coin_and_dice_combined_outcomes_sample_space_12,
    "32_coin_and_dice_probability_heads_and_even_number": arch_32_coin_and_dice_probability_heads_and_even_number,
    "33_coin_and_dice_probability_tails_and_prime_number": arch_33_coin_and_dice_probability_tails_and_prime_number,
    "34_two_dice_two_way_table_sample_space_36": arch_34_two_dice_two_way_table_sample_space_36,
    "35_two_dice_probability_sum_equals_seven": arch_35_two_dice_probability_sum_equals_seven,
    "36_two_dice_probability_sum_greater_than_nine": arch_36_two_dice_probability_sum_greater_than_nine,
    "37_two_dice_probability_doubles_matching_numbers": arch_37_two_dice_probability_doubles_matching_numbers,
    "38_two_dice_probability_difference_of_numbers": arch_38_two_dice_probability_difference_of_numbers,
    "39_two_dice_game_fairness_evaluation_sum_rules": arch_39_two_dice_game_fairness_evaluation_sum_rules,
    "40_two_spinners_combined_outcomes_two_way_table": arch_40_two_spinners_combined_outcomes_two_way_table,
    "41_drawing_two_counters_with_replacement_tree_diagram": arch_41_drawing_two_counters_with_replacement_tree_diagram,
    "42_drawing_two_counters_without_replacement_fraction_change": arch_42_drawing_two_counters_without_replacement_fraction_change,
    "43_two_stage_event_independent_events_multiplication_rule": arch_43_two_stage_event_independent_events_multiplication_rule,
    "44_predicting_number_of_times_event_occurs_in_n_trials": arch_44_predicting_number_of_times_event_occurs_in_n_trials,
    "45_survey_data_probability_two_way_table_gender_sport": arch_45_survey_data_probability_two_way_table_gender_sport,
    "46_survey_data_conditional_frequency_subset_selection": arch_46_survey_data_conditional_frequency_subset_selection,
    "47_quality_control_defective_items_probability": arch_47_quality_control_defective_items_probability,
    "48_probability_error_analysis_gamblers_fallacy": arch_48_probability_error_analysis_gamblers_fallacy,
    "49_probability_error_analysis_ignoring_order_in_outcomes": arch_49_probability_error_analysis_ignoring_order_in_outcomes,
    "50_compound_probability_word_problem_school_raffle_tickets": arch_50_compound_probability_word_problem_school_raffle_tickets,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())


def generate_grade8_probability_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    target_subskill = subskill
    if not target_subskill or target_subskill not in ARCHETYPE_MAP:
        if mode and mode.startswith("elementary_"):
            candidate = mode[len("elementary_"):]
            if candidate in ARCHETYPE_MAP:
                target_subskill = candidate
            else:
                for k in ARCHETYPE_MAP:
                    if candidate in k:
                        target_subskill = k
                        break

    if not target_subskill or target_subskill not in ARCHETYPE_MAP:
        target_subskill = rng.choice(SUBSKILLS)

    generator_fn = ARCHETYPE_MAP[target_subskill]
    q_data = generator_fn(rng)

    q_data["subject"] = "mathematics"
    q_data["grade"] = "grade-8"
    q_data["topic"] = "Probability"
    q_data["term"] = 4
    q_data["caps_weight_percent"] = 5
    q_data["suggested_duration_mins"] = 3
    q_data["difficulty"] = difficulty
    q_data["mode"] = mode
    q_data["subskill"] = target_subskill

    if "marking_schema" not in q_data:
        m = q_data.get("marks", 2)
        q_data["marking_schema"] = {
            "total_marks": m,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct probability concept or sample space identification", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate calculation and simplified fraction/percentage value", "marks": m - 1, "editable": True},
            ],
            "deductions": [{"rule": "unsimplified_fraction", "penalty": 1}],
            "carry_forward_rule": "consequential_accuracy",
        }

    return q_data


generate = generate_grade8_probability_question
