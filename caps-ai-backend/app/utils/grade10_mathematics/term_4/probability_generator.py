"""Grade 10 Mathematics — Term 4: Probability (Deterministic 6-Pillar Generator).
100% aligned with South African National Curriculum Standards (Grade 10 Mathematics: Probability).
Contains >= 50 distinct semantic archetypes split across:
- probability_archetypes_01_25.py (Archetypes 01–25)
- probability_archetypes_26_50.py (Archetypes 26–50)

Zero-LLM: 100% deterministic Python calculations with South African comma decimals ({,}).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade10_mathematics.term_4.probability_archetypes_01_25 import (
    arch_01_relative_frequency_calculation,
    arch_02_relative_vs_theoretical_probability_comparison,
    arch_03_sample_space_listing_single_stage,
    arch_04_theoretical_probability_fair_die,
    arch_05_theoretical_probability_word_letters,
    arch_06_theoretical_probability_deck_of_cards,
    arch_07_complementary_event_probability,
    arch_08_impossible_and_certain_events,
    arch_09_addition_rule_general_calculation,
    arch_10_addition_rule_solve_intersection,
    arch_11_addition_rule_solve_single_event,
    arch_12_mutually_exclusive_addition_rule,
    arch_13_mutually_exclusive_identification_and_proof,
    arch_14_complementary_vs_mutually_exclusive_distinction,
    arch_15_exhaustive_events_condition,
    arch_16_two_event_venn_read_counts,
    arch_17_two_event_venn_calculate_probabilities,
    arch_18_two_event_venn_solve_for_unknown_x_intersection,
    arch_19_two_event_venn_solve_for_neither,
    arch_20_two_event_venn_mutually_exclusive_case,
    arch_21_two_way_contingency_table_marginal_totals,
    arch_22_two_way_table_single_event_probability,
    arch_23_two_way_table_intersection_probability,
    arch_24_two_way_table_union_probability,
    arch_25_two_way_table_complement_probability,
)
from app.utils.grade10_mathematics.term_4.probability_archetypes_26_50 import (
    arch_26_two_stage_sample_space_grid_two_dice,
    arch_27_tree_diagram_two_coin_tosses,
    arch_28_tree_diagram_coin_and_die,
    arch_29_tree_diagram_marbles_with_replacement,
    arch_30_tree_diagram_marbles_without_replacement,
    arch_31_tree_diagram_both_same_outcome,
    arch_32_tree_diagram_at_least_one_outcome,
    arch_33_venn_diagram_shading_union,
    arch_34_venn_diagram_shading_intersection,
    arch_35_venn_diagram_shading_only_one_event,
    arch_36_venn_diagram_shading_neither_complement,
    arch_37_venn_diagram_at_most_one_event,
    arch_38_venn_diagram_exactly_one_event,
    arch_39_probability_with_ratios_and_algebra,
    arch_40_two_event_probability_word_problem_survey,
    arch_41_contingency_table_mutual_exclusivity_test,
    arch_42_simulation_vs_probability_model,
    arch_43_two_dice_sum_distribution,
    arch_44_cards_and_compound_events,
    arch_45_venn_diagram_reconstruct_from_probabilities,
    arch_46_tree_diagram_weather_forecast,
    arch_47_tree_diagram_successive_sports_matches,
    arch_48_probability_fractions_to_decimals_and_percentages,
    arch_49_odds_vs_probability_conceptual_check,
    arch_50_comprehensive_exam_probability_synthesis,
)

TOPIC = "Probability"
TOPIC_ID = "grade10_math_probability"
LO = "math10_probability_venn"

ARCHETYPE_DISPATCH: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Archetypes 01 to 25
    "01_relative_frequency_calculation": arch_01_relative_frequency_calculation,
    "02_relative_vs_theoretical_probability_comparison": arch_02_relative_vs_theoretical_probability_comparison,
    "03_sample_space_listing_single_stage": arch_03_sample_space_listing_single_stage,
    "04_theoretical_probability_fair_die": arch_04_theoretical_probability_fair_die,
    "05_theoretical_probability_word_letters": arch_05_theoretical_probability_word_letters,
    "06_theoretical_probability_deck_of_cards": arch_06_theoretical_probability_deck_of_cards,
    "07_complementary_event_probability": arch_07_complementary_event_probability,
    "08_impossible_and_certain_events": arch_08_impossible_and_certain_events,
    "09_addition_rule_general_calculation": arch_09_addition_rule_general_calculation,
    "10_addition_rule_solve_intersection": arch_10_addition_rule_solve_intersection,
    "11_addition_rule_solve_single_event": arch_11_addition_rule_solve_single_event,
    "12_mutually_exclusive_addition_rule": arch_12_mutually_exclusive_addition_rule,
    "13_mutually_exclusive_identification_and_proof": arch_13_mutually_exclusive_identification_and_proof,
    "14_complementary_vs_mutually_exclusive_distinction": arch_14_complementary_vs_mutually_exclusive_distinction,
    "15_exhaustive_events_condition": arch_15_exhaustive_events_condition,
    "16_two_event_venn_read_counts": arch_16_two_event_venn_read_counts,
    "17_two_event_venn_calculate_probabilities": arch_17_two_event_venn_calculate_probabilities,
    "18_two_event_venn_solve_for_unknown_x_intersection": arch_18_two_event_venn_solve_for_unknown_x_intersection,
    "19_two_event_venn_solve_for_neither": arch_19_two_event_venn_solve_for_neither,
    "20_two_event_venn_mutually_exclusive_case": arch_20_two_event_venn_mutually_exclusive_case,
    "21_two_way_contingency_table_marginal_totals": arch_21_two_way_contingency_table_marginal_totals,
    "22_two_way_table_single_event_probability": arch_22_two_way_table_single_event_probability,
    "23_two_way_table_intersection_probability": arch_23_two_way_table_intersection_probability,
    "24_two_way_table_union_probability": arch_24_two_way_table_union_probability,
    "25_two_way_table_complement_probability": arch_25_two_way_table_complement_probability,
    # Archetypes 26 to 50
    "26_two_stage_sample_space_grid_two_dice": arch_26_two_stage_sample_space_grid_two_dice,
    "27_tree_diagram_two_coin_tosses": arch_27_tree_diagram_two_coin_tosses,
    "28_tree_diagram_coin_and_die": arch_28_tree_diagram_coin_and_die,
    "29_tree_diagram_marbles_with_replacement": arch_29_tree_diagram_marbles_with_replacement,
    "30_tree_diagram_marbles_without_replacement": arch_30_tree_diagram_marbles_without_replacement,
    "31_tree_diagram_both_same_outcome": arch_31_tree_diagram_both_same_outcome,
    "32_tree_diagram_at_least_one_outcome": arch_32_tree_diagram_at_least_one_outcome,
    "33_venn_diagram_shading_union": arch_33_venn_diagram_shading_union,
    "34_venn_diagram_shading_intersection": arch_34_venn_diagram_shading_intersection,
    "35_venn_diagram_shading_only_one_event": arch_35_venn_diagram_shading_only_one_event,
    "36_venn_diagram_shading_neither_complement": arch_36_venn_diagram_shading_neither_complement,
    "37_venn_diagram_at_most_one_event": arch_37_venn_diagram_at_most_one_event,
    "38_venn_diagram_exactly_one_event": arch_38_venn_diagram_exactly_one_event,
    "39_probability_with_ratios_and_algebra": arch_39_probability_with_ratios_and_algebra,
    "40_two_event_probability_word_problem_survey": arch_40_two_event_probability_word_problem_survey,
    "41_contingency_table_mutual_exclusivity_test": arch_41_contingency_table_mutual_exclusivity_test,
    "42_simulation_vs_probability_model": arch_42_simulation_vs_probability_model,
    "43_two_dice_sum_distribution": arch_43_two_dice_sum_distribution,
    "44_cards_and_compound_events": arch_44_cards_and_compound_events,
    "45_venn_diagram_reconstruct_from_probabilities": arch_45_venn_diagram_reconstruct_from_probabilities,
    "46_tree_diagram_weather_forecast": arch_46_tree_diagram_weather_forecast,
    "47_tree_diagram_successive_sports_matches": arch_47_tree_diagram_successive_sports_matches,
    "48_probability_fractions_to_decimals_and_percentages": arch_48_probability_fractions_to_decimals_and_percentages,
    "49_odds_vs_probability_conceptual_check": arch_49_odds_vs_probability_conceptual_check,
    "50_comprehensive_exam_probability_synthesis": arch_50_comprehensive_exam_probability_synthesis,
}

# Legacy aliases for backward compatibility
LEGACY_ALIASES: Dict[str, str] = {
    "two_event_venn": "17_two_event_venn_calculate_probabilities",
}

ARCHETYPES: List[str] = list(ARCHETYPE_DISPATCH.keys())


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def get_all_subskills() -> List[str]:
    return list(ARCHETYPES)


def list_subskills() -> List[str]:
    return list(ARCHETYPES)


def get_metadata() -> Dict[str, Any]:
    return {
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "grade": 10,
        "term": 4,
        "archetypes": ARCHETYPES,
        "archetype_count": len(ARCHETYPES),
    }


def generate_subskill(subskill: str, seed: Optional[int] = None, **kwargs) -> Dict[str, Any]:
    r = _rng(seed)
    resolved = LEGACY_ALIASES.get(subskill, subskill)
    fn = ARCHETYPE_DISPATCH.get(resolved)
    if not fn:
        resolved = "04_theoretical_probability_fair_die"
        fn = ARCHETYPE_DISPATCH[resolved]

    q = fn(r)
    q["term"] = 4
    q["caps_weight_percent"] = 12
    q["suggested_duration_mins"] = q.get("suggested_duration_mins", 4)
    q["mode"] = f"elementary_{resolved}"
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    questions: List[Dict[str, Any]] = []

    if subskill:
        resolved = LEGACY_ALIASES.get(subskill, subskill)
        if resolved in ARCHETYPE_DISPATCH:
            for _ in range(count):
                sub_seed = r.randint(1000, 999999)
                questions.append(generate_subskill(resolved, seed=sub_seed, **kwargs))
            return questions

    # Random selection among all archetypes
    for _ in range(count):
        chosen_sub = r.choice(ARCHETYPES)
        sub_seed = r.randint(1000, 999999)
        questions.append(generate_subskill(chosen_sub, seed=sub_seed, **kwargs))

    return questions
