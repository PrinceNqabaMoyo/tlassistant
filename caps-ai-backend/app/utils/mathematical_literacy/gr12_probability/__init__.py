"""Grade 12 Mathematical Literacy — PROBABILITY Subskill Modules.
Subskills 01–52 dispatch registry and metadata.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Tuple

from .scale_frequency_complements import (
    generate_01_probability_three_forms,
    generate_02_theoretical_probability_single_draw,
    generate_03_relative_frequency_vs_theoretical,
    generate_04_law_of_large_numbers,
    generate_05_complementary_event_rule,
    generate_06_mutually_exclusive_addition_rule,
    generate_07_general_addition_rule,
    generate_08_probability_scale_endpoints,
)
from .independent_dependent_events import (
    generate_09_independent_events_classification,
    generate_10_dependent_events_without_replacement,
    generate_11_two_stage_draw_with_replacement,
    generate_12_two_stage_draw_without_replacement,
    generate_13_identical_items_without_replacement,
    generate_14_at_least_one_desired_outcome,
    generate_15_testing_independence_rule,
    generate_16_gamblers_fallacy_misconception,
)
from .contingency_tables import (
    generate_17_contingency_marginal_totals,
    generate_18_contingency_joint_probability,
    generate_19_contingency_conditional_probability,
    generate_20_evaluating_independence_contingency,
    generate_21_missing_cell_deduction,
    generate_22_driver_demographics_accident_risk,
    generate_23_school_pass_rates_contingency,
    generate_24_employment_by_education_qualification,
)
from .tree_diagrams_multistage import (
    generate_25_tree_branch_probabilities,
    generate_26_multiplying_along_branches,
    generate_27_summing_across_end_nodes,
    generate_28_weather_forecast_consecutive_rain,
    generate_29_medical_screening_tree_diagram,
    generate_30_three_offspring_gender_outcomes,
    generate_31_quality_control_inspection_stages,
    generate_32_successive_draw_tree_diagram,
)
from .venn_diagrams_sets import (
    generate_33_reading_intersection_venn,
    generate_34_exclusive_subsets_only_a,
    generate_35_union_rule_venn,
    generate_36_outside_region_neither,
    generate_37_three_set_venn_categorization,
    generate_38_deducting_double_counted_overlap,
    generate_39_solve_unknown_overlap_x,
    generate_40_conditional_probability_from_venn,
)
from .counting_principles_lottery import (
    generate_41_fundamental_counting_principle,
    generate_42_pin_codes_with_repetition,
    generate_43_arrangements_without_repetition,
    generate_44_sa_national_lottery_odds,
    generate_45_raffle_draw_probabilities,
    generate_46_expected_value_commercial_competitions,
)
from .medical_risk_financial_prob import (
    generate_47_medical_testing_false_positives,
    generate_48_insurance_risk_expected_claims,
    generate_49_actuarial_life_expectancy_risk_loading,
    generate_50_weather_probability_of_precipitation,
    generate_51_sports_betting_implied_probability,
    generate_52_casino_house_edge_roulette,
)

SUBSKILL_LIST: List[Tuple[str, str, Callable[[random.Random], Dict[str, Any]]]] = [
    ("01_probability_three_forms", "Three forms of probability (fractions, decimals, percentages)", generate_01_probability_three_forms),
    ("02_theoretical_probability_single_draw", "Theoretical probability of a single draw from a finite set", generate_02_theoretical_probability_single_draw),
    ("03_relative_frequency_vs_theoretical", "Relative frequency (experimental) versus theoretical probability", generate_03_relative_frequency_vs_theoretical),
    ("04_law_of_large_numbers", "The Law of Large Numbers and coin toss convergence", generate_04_law_of_large_numbers),
    ("05_complementary_event_rule", "Complement rule P(not A) = 1 - P(A)", generate_05_complementary_event_rule),
    ("06_mutually_exclusive_addition_rule", "Mutually exclusive events and addition rule", generate_06_mutually_exclusive_addition_rule),
    ("07_general_addition_rule", "General addition rule for non-mutually exclusive events", generate_07_general_addition_rule),
    ("08_probability_scale_endpoints", "Probability scale endpoints (impossible 0 to certain 1)", generate_08_probability_scale_endpoints),
    ("09_independent_events_classification", "Independent events conceptual classification", generate_09_independent_events_classification),
    ("10_dependent_events_without_replacement", "Dependent events classification (without replacement)", generate_10_dependent_events_without_replacement),
    ("11_two_stage_draw_with_replacement", "Two-stage draw with replacement probability", generate_11_two_stage_draw_with_replacement),
    ("12_two_stage_draw_without_replacement", "Two-stage draw without replacement probability", generate_12_two_stage_draw_without_replacement),
    ("13_identical_items_without_replacement", "Draw of identical items without replacement", generate_13_identical_items_without_replacement),
    ("14_at_least_one_desired_outcome", "Probability of at least one outcome using complement rule", generate_14_at_least_one_desired_outcome),
    ("15_testing_independence_rule", "Testing independence via product rule P(A ∩ B) = P(A) × P(B)", generate_15_testing_independence_rule),
    ("16_gamblers_fallacy_misconception", "Debunking the Gambler's Fallacy misconception", generate_16_gamblers_fallacy_misconception),
    ("17_contingency_marginal_totals", "Two-way contingency table: marginal row and column totals", generate_17_contingency_marginal_totals),
    ("18_contingency_joint_probability", "Contingency table: joint probability P(A and B)", generate_18_contingency_joint_probability),
    ("19_contingency_conditional_probability", "Contingency table: conditional probability P(A | B)", generate_19_contingency_conditional_probability),
    ("20_evaluating_independence_contingency", "Evaluating independence of characteristics from survey rates", generate_20_evaluating_independence_contingency),
    ("21_missing_cell_deduction", "Deducing missing cell values from known totals", generate_21_missing_cell_deduction),
    ("22_driver_demographics_accident_risk", "Driver demographics and motor vehicle accident risk", generate_22_driver_demographics_accident_risk),
    ("23_school_pass_rates_contingency", "School pass rates across grade level and gender", generate_23_school_pass_rates_contingency),
    ("24_employment_by_education_qualification", "Youth employment rates by tertiary qualification level", generate_24_employment_by_education_qualification),
    ("25_tree_branch_probabilities", "Tree diagram branch probabilities sum to 1,00 rule", generate_25_tree_branch_probabilities),
    ("26_multiplying_along_branches", "Multiplying probabilities along consecutive branches", generate_26_multiplying_along_branches),
    ("27_summing_across_end_nodes", "Summing probabilities across favorable end-nodes", generate_27_summing_across_end_nodes),
    ("28_weather_forecast_consecutive_rain", "Weather forecast: probability of consecutive rainy days", generate_28_weather_forecast_consecutive_rain),
    ("29_medical_screening_tree_diagram", "Medical screening tree: false positive rate interpretation", generate_29_medical_screening_tree_diagram),
    ("30_three_offspring_gender_outcomes", "Three offspring gender tree diagram outcomes", generate_30_three_offspring_gender_outcomes),
    ("31_quality_control_inspection_stages", "Industrial quality control two-stage inspection tree", generate_31_quality_control_inspection_stages),
    ("32_successive_draw_tree_diagram", "Successive non-replacement tree branches", generate_32_successive_draw_tree_diagram),
    ("33_reading_intersection_venn", "Reading intersection count and probability from 2-set Venn", generate_33_reading_intersection_venn),
    ("34_exclusive_subsets_only_a", "Exclusive subset count and probability (Set A only)", generate_34_exclusive_subsets_only_a),
    ("35_union_rule_venn", "Union rule P(A or B) from Venn diagram counts", generate_35_union_rule_venn),
    ("36_outside_region_neither", "Outside region count and probability (neither event)", generate_36_outside_region_neither),
    ("37_three_set_venn_categorization", "Three-set Venn diagram region categorization and sums", generate_37_three_set_venn_categorization),
    ("38_deducting_double_counted_overlap", "Deducting double-counted overlap in school surveys", generate_38_deducting_double_counted_overlap),
    ("39_solve_unknown_overlap_x", "Solving for unknown center overlap x given cohort total", generate_39_solve_unknown_overlap_x),
    ("40_conditional_probability_from_venn", "Conditional probability from Venn diagram set cardinalities", generate_40_conditional_probability_from_venn),
    ("41_fundamental_counting_principle", "Fundamental counting principle (m × n × p combinations)", generate_41_fundamental_counting_principle),
    ("42_pin_codes_with_repetition", "PIN codes and passwords with repetition allowed", generate_42_pin_codes_with_repetition),
    ("43_arrangements_without_repetition", "Arrangements without repetition (executive committees)", generate_43_arrangements_without_repetition),
    ("44_sa_national_lottery_odds", "South African National LOTTO combinations and jackpot odds", generate_44_sa_national_lottery_odds),
    ("45_raffle_draw_probabilities", "School fundraising raffle winning probabilities", generate_45_raffle_draw_probabilities),
    ("46_expected_value_commercial_competitions", "Expected monetary value E(X) in commercial competitions", generate_46_expected_value_commercial_competitions),
    ("47_medical_testing_false_positives", "Medical diagnostic screening and true positive probability", generate_47_medical_testing_false_positives),
    ("48_insurance_risk_expected_claims", "Vehicle insurance underwriting and expected claims pool", generate_48_insurance_risk_expected_claims),
    ("49_actuarial_life_expectancy_risk_loading", "Actuarial mortality risk loading and premium increases", generate_49_actuarial_life_expectancy_risk_loading),
    ("50_weather_probability_of_precipitation", "Interpreting Probability of Precipitation (PoP) in forecasts", generate_50_weather_probability_of_precipitation),
    ("51_sports_betting_implied_probability", "Sports betting odds and implied bookmaker probability", generate_51_sports_betting_implied_probability),
    ("52_casino_house_edge_roulette", "Casino roulette mathematical house edge and long-term loss", generate_52_casino_house_edge_roulette),
]

SUBSKILL_DISPATCH: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
SUBSKILL_METADATA: Dict[str, Dict[str, str]] = {}

for idx, (subskill_key, name, fn) in enumerate(SUBSKILL_LIST, start=1):
    num_str = f"{idx:02d}"
    SUBSKILL_DISPATCH[subskill_key] = fn
    SUBSKILL_DISPATCH[num_str] = fn
    SUBSKILL_DISPATCH[str(idx)] = fn
    SUBSKILL_DISPATCH[f"gr12_prob_{num_str}"] = fn

    SUBSKILL_METADATA[subskill_key] = {
        "index": num_str,
        "name": name,
        "topic": "grade12_mathlit_probability",
        "key": f"gr12_prob_{num_str}",
    }


def generate_subskill(subskill: str | int, r: random.Random) -> Dict[str, Any]:
    """Generate a question for the requested subskill."""
    key = str(subskill).strip()
    fn = SUBSKILL_DISPATCH.get(key)
    if fn is None:
        fn = r.choice(list(SUBSKILL_DISPATCH.values()))
    return fn(r)
