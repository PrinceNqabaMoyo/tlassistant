"""Grade 7 Mathematics - Probability Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 4/02. Probability.md
Focus: Probability scale (impossible 0 to certain 1), theoretical probability formula, fair dice, fair coins,
spinners with SVG figures, bag of marbles/buttons, playing cards, letter tiles, complementary events,
experimental probability / relative frequency, law of large numbers, two-coin and coin+die compound events,
two-way tables, predicting frequencies, common misconceptions (gambler's fallacy, 50-50 fallacy), and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .data_probability_archetypes_01_25 import (
    arch_01_probability_scale_impossible_certain_likely_unlikely,
    arch_02_theoretical_probability_definition_formula,
    arch_03_sample_space_listing_fair_die,
    arch_04_sample_space_listing_fair_coin,
    arch_05_probability_coin_toss_head_tail,
    arch_06_probability_fair_die_single_number,
    arch_07_probability_fair_die_even_odd,
    arch_08_probability_fair_die_prime_number,
    arch_09_probability_fair_die_greater_than_threshold,
    arch_10_probability_fair_die_multiples,
    arch_11_probability_fair_die_impossible_and_certain,
    arch_12_probability_spinner_equal_sectors_svg,
    arch_13_probability_spinner_unequal_sectors,
    arch_14_probability_spinner_composite_regions,
    arch_15_probability_marbles_bag_single_color,
    arch_16_probability_marbles_bag_simplified_fraction,
    arch_17_probability_marbles_bag_decimal_and_percentage,
    arch_18_probability_marbles_bag_or_event,
    arch_19_probability_marbles_bag_complementary_not_event,
    arch_20_probability_buttons_colored_proportions,
    arch_21_probability_cards_red_or_black_color,
    arch_22_probability_cards_specific_suit,
    arch_23_probability_cards_ace_or_face_card,
    arch_24_probability_cards_number_card,
    arch_25_probability_letter_tiles_word_vowels,
)
from .data_probability_archetypes_26_50 import (
    arch_26_probability_letter_tiles_word_consonants,
    arch_27_probability_letter_tiles_specific_letter_multiplicity,
    arch_28_complementary_events_sum_to_one_rule,
    arch_29_complementary_events_find_not_a,
    arch_30_experimental_probability_relative_frequency_definition,
    arch_31_experimental_probability_calculate_relative_frequency,
    arch_32_law_of_large_numbers_experimental_vs_theoretical,
    arch_33_fair_vs_biased_coin_experiment,
    arch_34_fair_vs_biased_die_experiment,
    arch_35_two_coins_sample_space_listing_tree,
    arch_36_two_coins_probability_both_heads,
    arch_37_two_coins_probability_one_head_one_tail,
    arch_38_two_coins_probability_at_least_one_tail,
    arch_39_coin_and_die_combined_sample_space,
    arch_40_coin_and_die_probability_head_and_even,
    arch_41_two_way_table_transport_survey_probability,
    arch_42_two_way_table_sports_gender_probability,
    arch_43_predicting_frequencies_from_probability,
    arch_44_predicting_raffle_tickets_winner_probability,
    arch_45_common_misconception_gamblers_fallacy,
    arch_46_common_misconception_probability_greater_than_one,
    arch_47_common_misconception_50_50_fallacy,
    arch_48_common_misconception_negative_probability,
    arch_49_common_misconception_forgetting_to_simplify_fraction,
    arch_50_probability_comprehensive_diagnostic_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_probability_scale_impossible_certain_likely_unlikely": arch_01_probability_scale_impossible_certain_likely_unlikely,
    "02_theoretical_probability_definition_formula": arch_02_theoretical_probability_definition_formula,
    "03_sample_space_listing_fair_die": arch_03_sample_space_listing_fair_die,
    "04_sample_space_listing_fair_coin": arch_04_sample_space_listing_fair_coin,
    "05_probability_coin_toss_head_tail": arch_05_probability_coin_toss_head_tail,
    "06_probability_fair_die_single_number": arch_06_probability_fair_die_single_number,
    "07_probability_fair_die_even_odd": arch_07_probability_fair_die_even_odd,
    "08_probability_fair_die_prime_number": arch_08_probability_fair_die_prime_number,
    "09_probability_fair_die_greater_than_threshold": arch_09_probability_fair_die_greater_than_threshold,
    "10_probability_fair_die_multiples": arch_10_probability_fair_die_multiples,
    "11_probability_fair_die_impossible_and_certain": arch_11_probability_fair_die_impossible_and_certain,
    "12_probability_spinner_equal_sectors_svg": arch_12_probability_spinner_equal_sectors_svg,
    "13_probability_spinner_unequal_sectors": arch_13_probability_spinner_unequal_sectors,
    "14_probability_spinner_composite_regions": arch_14_probability_spinner_composite_regions,
    "15_probability_marbles_bag_single_color": arch_15_probability_marbles_bag_single_color,
    "16_probability_marbles_bag_simplified_fraction": arch_16_probability_marbles_bag_simplified_fraction,
    "17_probability_marbles_bag_decimal_and_percentage": arch_17_probability_marbles_bag_decimal_and_percentage,
    "18_probability_marbles_bag_or_event": arch_18_probability_marbles_bag_or_event,
    "19_probability_marbles_bag_complementary_not_event": arch_19_probability_marbles_bag_complementary_not_event,
    "20_probability_buttons_colored_proportions": arch_20_probability_buttons_colored_proportions,
    "21_probability_cards_red_or_black_color": arch_21_probability_cards_red_or_black_color,
    "22_probability_cards_specific_suit": arch_22_probability_cards_specific_suit,
    "23_probability_cards_ace_or_face_card": arch_23_probability_cards_ace_or_face_card,
    "24_probability_cards_number_card": arch_24_probability_cards_number_card,
    "25_probability_letter_tiles_word_vowels": arch_25_probability_letter_tiles_word_vowels,
    "26_probability_letter_tiles_word_consonants": arch_26_probability_letter_tiles_word_consonants,
    "27_probability_letter_tiles_specific_letter_multiplicity": arch_27_probability_letter_tiles_specific_letter_multiplicity,
    "28_complementary_events_sum_to_one_rule": arch_28_complementary_events_sum_to_one_rule,
    "29_complementary_events_find_not_a": arch_29_complementary_events_find_not_a,
    "30_experimental_probability_relative_frequency_definition": arch_30_experimental_probability_relative_frequency_definition,
    "31_experimental_probability_calculate_relative_frequency": arch_31_experimental_probability_calculate_relative_frequency,
    "32_law_of_large_numbers_experimental_vs_theoretical": arch_32_law_of_large_numbers_experimental_vs_theoretical,
    "33_fair_vs_biased_coin_experiment": arch_33_fair_vs_biased_coin_experiment,
    "34_fair_vs_biased_die_experiment": arch_34_fair_vs_biased_die_experiment,
    "35_two_coins_sample_space_listing_tree": arch_35_two_coins_sample_space_listing_tree,
    "36_two_coins_probability_both_heads": arch_36_two_coins_probability_both_heads,
    "37_two_coins_probability_one_head_one_tail": arch_37_two_coins_probability_one_head_one_tail,
    "38_two_coins_probability_at_least_one_tail": arch_38_two_coins_probability_at_least_one_tail,
    "39_coin_and_die_combined_sample_space": arch_39_coin_and_die_combined_sample_space,
    "40_coin_and_die_probability_head_and_even": arch_40_coin_and_die_probability_head_and_even,
    "41_two_way_table_transport_survey_probability": arch_41_two_way_table_transport_survey_probability,
    "42_two_way_table_sports_gender_probability": arch_42_two_way_table_sports_gender_probability,
    "43_predicting_frequencies_from_probability": arch_43_predicting_frequencies_from_probability,
    "44_predicting_raffle_tickets_winner_probability": arch_44_predicting_raffle_tickets_winner_probability,
    "45_common_misconception_gamblers_fallacy": arch_45_common_misconception_gamblers_fallacy,
    "46_common_misconception_probability_greater_than_one": arch_46_common_misconception_probability_greater_than_one,
    "47_common_misconception_50_50_fallacy": arch_47_common_misconception_50_50_fallacy,
    "48_common_misconception_negative_probability": arch_48_common_misconception_negative_probability,
    "49_common_misconception_forgetting_to_simplify_fraction": arch_49_common_misconception_forgetting_to_simplify_fraction,
    "50_probability_comprehensive_diagnostic_autopsy": arch_50_probability_comprehensive_diagnostic_autopsy,
}

SUBSKILLS = list(ARCHETYPE_BUILDERS.keys())


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed) if seed is not None else random.Random()
    if subskill is None or subskill not in ARCHETYPE_BUILDERS:
        subskill = rng.choice(SUBSKILLS)
    builder = ARCHETYPE_BUILDERS[subskill]
    return builder(rng)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    questions = []
    target_sub = str(subskill or "").strip().lower()

    if target_sub and target_sub not in ("compound", "all", "mixed", "auto", "default", "none"):
        matched = None
        for k in ARCHETYPE_BUILDERS:
            if target_sub == k.lower() or target_sub in k.lower():
                matched = k
                break
        for _ in range(count):
            if matched:
                questions.append(ARCHETYPE_BUILDERS[matched](rng))
            else:
                s = rng.choice(SUBSKILLS)
                questions.append(ARCHETYPE_BUILDERS[s](rng))
        return questions

    for i in range(count):
        s = SUBSKILLS[i % len(SUBSKILLS)]
        questions.append(ARCHETYPE_BUILDERS[s](rng))

    return questions


generate_probability = generate

