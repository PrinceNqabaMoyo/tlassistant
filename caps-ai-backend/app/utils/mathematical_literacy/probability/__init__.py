"""Probability Subskills Package (52 distinct archetypes).

Covers Grade 10 Mathematical Literacy Term 4 Topic:
1. The probability scale & number formats (Subskills 1 to 9)
2. Single-stage theoretical probability & equipment (Subskills 10 to 18)
3. Coloured objects, bags & spinners (Subskills 19 to 27)
4. Relative frequency & experimental probability (Subskills 28 to 36)
5. Combined events, tree diagrams & two-way tables (Subskills 37 to 44)
6. Real-world applications (weather, medicine & risk) (Subskills 45 to 52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .probability_scale_formats import (
    _gen_prob_scale_verbal_classification,
    _gen_prob_scale_fraction_to_decimal_percentage,
    _gen_prob_scale_percentage_to_fraction,
    _gen_prob_scale_decimal_to_percentage,
    _gen_prob_scale_bounds_validity,
    _gen_prob_scale_complementary_event_rule,
    _gen_prob_scale_rain_forecast_complement,
    _gen_prob_scale_sum_of_all_outcomes_equals_one,
    _gen_prob_scale_ordering_events_likelihood,
)
from .single_stage_dice_cards import (
    _gen_prob_single_fair_coin_toss,
    _gen_prob_single_six_sided_die_number,
    _gen_prob_single_six_sided_die_even_odd,
    _gen_prob_single_six_sided_die_prime_numbers,
    _gen_prob_single_six_sided_die_greater_less,
    _gen_prob_single_eight_sided_die,
    _gen_prob_single_standard_deck_suit,
    _gen_prob_single_standard_deck_face_card,
    _gen_prob_single_standard_deck_ace,
)
from .bags_spinners_draws import (
    _gen_prob_bag_single_colour_from_total,
    _gen_prob_bag_or_compound_disjunction,
    _gen_prob_bag_not_colour_complement,
    _gen_prob_bag_missing_colour_count,
    _gen_prob_spinner_equal_sectors,
    _gen_prob_spinner_unequal_sectors_angles,
    _gen_prob_raffle_single_ticket_winning_chance,
    _gen_prob_raffle_multiple_tickets_winning_chance,
    _gen_prob_luckydraw_token_selection,
)
from .relative_frequency_experiments import (
    _gen_prob_exp_relative_frequency_calculation,
    _gen_prob_exp_compare_relative_to_theoretical,
    _gen_prob_exp_law_of_large_numbers,
    _gen_prob_exp_expected_frequency_prediction,
    _gen_prob_exp_gamblers_fallacy_independent_trials,
    _gen_prob_exp_detecting_biased_die,
    _gen_prob_exp_pin_tack_landing_orientation,
    _gen_prob_exp_batch_sampling_defect_estimate,
    _gen_prob_exp_class_survey_empirical_probability,
)
from .combined_events_tree_tables import (
    _gen_prob_comb_sample_space_enumeration_two_coins,
    _gen_prob_comb_two_coins_both_heads,
    _gen_prob_comb_two_coins_at_least_one_head,
    _gen_prob_comb_coin_and_die_outcomes_grid,
    _gen_prob_comb_two_dice_sum_grid,
    _gen_prob_comb_two_way_table_gender_sport,
    _gen_prob_comb_tree_diagram_two_stage_paths,
    _gen_prob_comb_fair_game_rules_audit,
)
from .real_world_risk_weather import (
    _gen_prob_app_weather_forecast_precipitation_percentage,
    _gen_prob_app_weather_veld_fire_danger_index,
    _gen_prob_app_manufacturing_quality_control_pass_rate,
    _gen_prob_app_medical_screening_test_accuracy,
    _gen_prob_app_national_lottery_sample_space_odds,
    _gen_prob_app_motor_vehicle_insurance_risk_tier,
    _gen_prob_app_blood_type_donor_compatibility,
    _gen_prob_app_decision_making_under_uncertainty,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Cluster 1: The probability scale & number formats (9)
    "prob_scale_verbal_classification": _gen_prob_scale_verbal_classification,
    "prob_scale_fraction_to_decimal_percentage": _gen_prob_scale_fraction_to_decimal_percentage,
    "prob_scale_percentage_to_fraction": _gen_prob_scale_percentage_to_fraction,
    "prob_scale_decimal_to_percentage": _gen_prob_scale_decimal_to_percentage,
    "prob_scale_bounds_validity": _gen_prob_scale_bounds_validity,
    "prob_scale_complementary_event_rule": _gen_prob_scale_complementary_event_rule,
    "prob_scale_rain_forecast_complement": _gen_prob_scale_rain_forecast_complement,
    "prob_scale_sum_of_all_outcomes_equals_one": _gen_prob_scale_sum_of_all_outcomes_equals_one,
    "prob_scale_ordering_events_likelihood": _gen_prob_scale_ordering_events_likelihood,

    # Cluster 2: Single-stage theoretical probability & equipment (9)
    "prob_single_fair_coin_toss": _gen_prob_single_fair_coin_toss,
    "prob_single_six_sided_die_number": _gen_prob_single_six_sided_die_number,
    "prob_single_six_sided_die_even_odd": _gen_prob_single_six_sided_die_even_odd,
    "prob_single_six_sided_die_prime_numbers": _gen_prob_single_six_sided_die_prime_numbers,
    "prob_single_six_sided_die_greater_less": _gen_prob_single_six_sided_die_greater_less,
    "prob_single_eight_sided_die": _gen_prob_single_eight_sided_die,
    "prob_single_standard_deck_suit": _gen_prob_single_standard_deck_suit,
    "prob_single_standard_deck_face_card": _gen_prob_single_standard_deck_face_card,
    "prob_single_standard_deck_ace": _gen_prob_single_standard_deck_ace,

    # Cluster 3: Coloured objects, bags & spinners (9)
    "prob_bag_single_colour_from_total": _gen_prob_bag_single_colour_from_total,
    "prob_bag_or_compound_disjunction": _gen_prob_bag_or_compound_disjunction,
    "prob_bag_not_colour_complement": _gen_prob_bag_not_colour_complement,
    "prob_bag_missing_colour_count": _gen_prob_bag_missing_colour_count,
    "prob_spinner_equal_sectors": _gen_prob_spinner_equal_sectors,
    "prob_spinner_unequal_sectors_angles": _gen_prob_spinner_unequal_sectors_angles,
    "prob_raffle_single_ticket_winning_chance": _gen_prob_raffle_single_ticket_winning_chance,
    "prob_raffle_multiple_tickets_winning_chance": _gen_prob_raffle_multiple_tickets_winning_chance,
    "prob_luckydraw_token_selection": _gen_prob_luckydraw_token_selection,

    # Cluster 4: Relative frequency & experimental probability (9)
    "prob_exp_relative_frequency_calculation": _gen_prob_exp_relative_frequency_calculation,
    "prob_exp_compare_relative_to_theoretical": _gen_prob_exp_compare_relative_to_theoretical,
    "prob_exp_law_of_large_numbers": _gen_prob_exp_law_of_large_numbers,
    "prob_exp_expected_frequency_prediction": _gen_prob_exp_expected_frequency_prediction,
    "prob_exp_gamblers_fallacy_independent_trials": _gen_prob_exp_gamblers_fallacy_independent_trials,
    "prob_exp_detecting_biased_die": _gen_prob_exp_detecting_biased_die,
    "prob_exp_pin_tack_landing_orientation": _gen_prob_exp_pin_tack_landing_orientation,
    "prob_exp_batch_sampling_defect_estimate": _gen_prob_exp_batch_sampling_defect_estimate,
    "prob_exp_class_survey_empirical_probability": _gen_prob_exp_class_survey_empirical_probability,

    # Cluster 5: Combined events, tree diagrams & two-way tables (8)
    "prob_comb_sample_space_enumeration_two_coins": _gen_prob_comb_sample_space_enumeration_two_coins,
    "prob_comb_two_coins_both_heads": _gen_prob_comb_two_coins_both_heads,
    "prob_comb_two_coins_at_least_one_head": _gen_prob_comb_two_coins_at_least_one_head,
    "prob_comb_coin_and_die_outcomes_grid": _gen_prob_comb_coin_and_die_outcomes_grid,
    "prob_comb_two_dice_sum_grid": _gen_prob_comb_two_dice_sum_grid,
    "prob_comb_two_way_table_gender_sport": _gen_prob_comb_two_way_table_gender_sport,
    "prob_comb_tree_diagram_two_stage_paths": _gen_prob_comb_tree_diagram_two_stage_paths,
    "prob_comb_fair_game_rules_audit": _gen_prob_comb_fair_game_rules_audit,

    # Cluster 6: Real-world applications (weather, medicine & risk) (8)
    "prob_app_weather_forecast_precipitation_percentage": _gen_prob_app_weather_forecast_precipitation_percentage,
    "prob_app_weather_veld_fire_danger_index": _gen_prob_app_weather_veld_fire_danger_index,
    "prob_app_manufacturing_quality_control_pass_rate": _gen_prob_app_manufacturing_quality_control_pass_rate,
    "prob_app_medical_screening_test_accuracy": _gen_prob_app_medical_screening_test_accuracy,
    "prob_app_national_lottery_sample_space_odds": _gen_prob_app_national_lottery_sample_space_odds,
    "prob_app_motor_vehicle_insurance_risk_tier": _gen_prob_app_motor_vehicle_insurance_risk_tier,
    "prob_app_blood_type_donor_compatibility": _gen_prob_app_blood_type_donor_compatibility,
    "prob_app_decision_making_under_uncertainty": _gen_prob_app_decision_making_under_uncertainty,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def generate(seed: Optional[int] = None, count: int = 1, subskill: Optional[str] = None) -> List[Dict[str, Any]]:
    """Generate questions for Probability."""
    r = random.Random(seed)
    questions = []

    for _ in range(count):
        if subskill and subskill in DISPATCH_TABLE:
            fn = DISPATCH_TABLE[subskill]
        else:
            chosen = r.choice(SUBSKILLS)
            fn = DISPATCH_TABLE[chosen]
        questions.append(fn(r))

    return questions
