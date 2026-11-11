"""Grade 9 Mathematics - Collect, Organise & Summarise Data Generator (50 Semantic Archetypes).
===========================================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 4 Topic: Collect, organise and summarise data
  - curriculum_docs_auto/Mathematics_Gr9/Term 4/ Data Handling
  - Data collection methods, sampling, bias, tally charts, ungrouped frequency tables,
    measures of central tendency (mean, median, mode), measures of dispersion (range,
    outliers, quartiles Q1/Q3, IQR, semi-IQR), stem-and-leaf plots, dot plots, grouped
    frequency tables (class intervals, midpoints, modal class, median class, estimated mean),
    relative and cumulative frequencies, discrete vs continuous data, data transformation
    effects, and diagnostic error analysis.

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from .data_summarise_archetypes_01_25 import (
    arch_01_population_vs_sample_identification,
    arch_02_data_collection_methods_survey_vs_observation_vs_experiment,
    arch_03_random_sampling_vs_stratified_sampling,
    arch_04_identifying_bias_in_survey_questions,
    arch_05_tally_chart_reading_and_frequency_counts,
    arch_06_completing_ungrouped_frequency_distribution_table,
    arch_07_mean_of_ungrouped_data_integer_result,
    arch_08_mean_of_ungrouped_data_decimal_result,
    arch_09_median_of_ungrouped_data_odd_number_of_items,
    arch_10_median_of_ungrouped_data_even_number_of_items,
    arch_11_mode_of_ungrouped_data_unimodal,
    arch_12_mode_of_ungrouped_data_bimodal_or_no_mode,
    arch_13_range_of_ungrouped_data_maximum_minus_minimum,
    arch_14_find_missing_data_value_given_mean,
    arch_15_find_missing_frequency_in_distribution_given_total,
    arch_16_identifying_outliers_in_raw_dataset,
    arch_17_effect_of_outlier_on_mean_vs_median,
    arch_18_choosing_appropriate_measure_of_central_tendency_skewed_vs_symmetric,
    arch_19_mean_from_ungrouped_frequency_table_sum_fx_over_n,
    arch_20_median_from_ungrouped_frequency_table_cumulative_frequency,
    arch_21_mode_from_ungrouped_frequency_table_highest_frequency,
    arch_22_lower_quartile_q1_calculation,
    arch_23_upper_quartile_q3_calculation,
    arch_24_interquartile_range_iqr_q3_minus_q1,
    arch_25_semi_interquartile_range_calculation,
)
from .data_summarise_archetypes_26_50 import (
    arch_26_five_number_summary_min_q1_med_q3_max,
    arch_27_stem_and_leaf_diagram_reading_values,
    arch_28_stem_and_leaf_diagram_median_and_mode,
    arch_29_dot_plot_reading_frequency_and_spread,
    arch_30_grouped_frequency_table_identifying_class_intervals,
    arch_31_class_midpoints_calculation_for_grouped_intervals,
    arch_32_modal_class_interval_identification,
    arch_33_median_class_interval_identification,
    arch_34_estimated_mean_of_grouped_data_sum_fm_over_sum_f,
    arch_35_relative_frequency_calculation_as_fraction_or_percentage,
    arch_36_cumulative_frequency_calculation_running_totals,
    arch_37_percentage_of_data_above_or_below_given_benchmark,
    arch_38_discrete_vs_continuous_numerical_data_classification,
    arch_39_numerical_vs_categorical_data_classification,
    arch_40_effect_of_adding_constant_to_all_values_on_mean_and_range,
    arch_41_effect_of_multiplying_all_values_by_constant_on_mean_and_range,
    arch_42_comparing_two_datasets_using_mean_and_range,
    arch_43_comparing_two_datasets_using_median_and_iqr,
    arch_44_contextual_sa_temperatures_mean_and_range,
    arch_45_contextual_sa_mathematics_exam_scores_analysis,
    arch_46_contextual_sa_monthly_household_expenditure_median,
    arch_47_error_analysis_calculating_median_without_ordering_data,
    arch_48_error_analysis_confusing_frequency_with_data_value_in_mode,
    arch_49_error_analysis_dividing_by_wrong_n_in_mean_frequency_table,
    arch_50_compound_multi_stage_statistical_investigation_synthesis,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_population_vs_sample_identification": arch_01_population_vs_sample_identification,
    "02_data_collection_methods_survey_vs_observation_vs_experiment": arch_02_data_collection_methods_survey_vs_observation_vs_experiment,
    "03_random_sampling_vs_stratified_sampling": arch_03_random_sampling_vs_stratified_sampling,
    "04_identifying_bias_in_survey_questions": arch_04_identifying_bias_in_survey_questions,
    "05_tally_chart_reading_and_frequency_counts": arch_05_tally_chart_reading_and_frequency_counts,
    "06_completing_ungrouped_frequency_distribution_table": arch_06_completing_ungrouped_frequency_distribution_table,
    "07_mean_of_ungrouped_data_integer_result": arch_07_mean_of_ungrouped_data_integer_result,
    "08_mean_of_ungrouped_data_decimal_result": arch_08_mean_of_ungrouped_data_decimal_result,
    "09_median_of_ungrouped_data_odd_number_of_items": arch_09_median_of_ungrouped_data_odd_number_of_items,
    "10_median_of_ungrouped_data_even_number_of_items": arch_10_median_of_ungrouped_data_even_number_of_items,
    "11_mode_of_ungrouped_data_unimodal": arch_11_mode_of_ungrouped_data_unimodal,
    "12_mode_of_ungrouped_data_bimodal_or_no_mode": arch_12_mode_of_ungrouped_data_bimodal_or_no_mode,
    "13_range_of_ungrouped_data_maximum_minus_minimum": arch_13_range_of_ungrouped_data_maximum_minus_minimum,
    "14_find_missing_data_value_given_mean": arch_14_find_missing_data_value_given_mean,
    "15_find_missing_frequency_in_distribution_given_total": arch_15_find_missing_frequency_in_distribution_given_total,
    "16_identifying_outliers_in_raw_dataset": arch_16_identifying_outliers_in_raw_dataset,
    "17_effect_of_outlier_on_mean_vs_median": arch_17_effect_of_outlier_on_mean_vs_median,
    "18_choosing_appropriate_measure_of_central_tendency_skewed_vs_symmetric": arch_18_choosing_appropriate_measure_of_central_tendency_skewed_vs_symmetric,
    "19_mean_from_ungrouped_frequency_table_sum_fx_over_n": arch_19_mean_from_ungrouped_frequency_table_sum_fx_over_n,
    "20_median_from_ungrouped_frequency_table_cumulative_frequency": arch_20_median_from_ungrouped_frequency_table_cumulative_frequency,
    "21_mode_from_ungrouped_frequency_table_highest_frequency": arch_21_mode_from_ungrouped_frequency_table_highest_frequency,
    "22_lower_quartile_q1_calculation": arch_22_lower_quartile_q1_calculation,
    "23_upper_quartile_q3_calculation": arch_23_upper_quartile_q3_calculation,
    "24_interquartile_range_iqr_q3_minus_q1": arch_24_interquartile_range_iqr_q3_minus_q1,
    "25_semi_interquartile_range_calculation": arch_25_semi_interquartile_range_calculation,
    "26_five_number_summary_min_q1_med_q3_max": arch_26_five_number_summary_min_q1_med_q3_max,
    "27_stem_and_leaf_diagram_reading_values": arch_27_stem_and_leaf_diagram_reading_values,
    "28_stem_and_leaf_diagram_median_and_mode": arch_28_stem_and_leaf_diagram_median_and_mode,
    "29_dot_plot_reading_frequency_and_spread": arch_29_dot_plot_reading_frequency_and_spread,
    "30_grouped_frequency_table_identifying_class_intervals": arch_30_grouped_frequency_table_identifying_class_intervals,
    "31_class_midpoints_calculation_for_grouped_intervals": arch_31_class_midpoints_calculation_for_grouped_intervals,
    "32_modal_class_interval_identification": arch_32_modal_class_interval_identification,
    "33_median_class_interval_identification": arch_33_median_class_interval_identification,
    "34_estimated_mean_of_grouped_data_sum_fm_over_sum_f": arch_34_estimated_mean_of_grouped_data_sum_fm_over_sum_f,
    "35_relative_frequency_calculation_as_fraction_or_percentage": arch_35_relative_frequency_calculation_as_fraction_or_percentage,
    "36_cumulative_frequency_calculation_running_totals": arch_36_cumulative_frequency_calculation_running_totals,
    "37_percentage_of_data_above_or_below_given_benchmark": arch_37_percentage_of_data_above_or_below_given_benchmark,
    "38_discrete_vs_continuous_numerical_data_classification": arch_38_discrete_vs_continuous_numerical_data_classification,
    "39_numerical_vs_categorical_data_classification": arch_39_numerical_vs_categorical_data_classification,
    "40_effect_of_adding_constant_to_all_values_on_mean_and_range": arch_40_effect_of_adding_constant_to_all_values_on_mean_and_range,
    "41_effect_of_multiplying_all_values_by_constant_on_mean_and_range": arch_41_effect_of_multiplying_all_values_by_constant_on_mean_and_range,
    "42_comparing_two_datasets_using_mean_and_range": arch_42_comparing_two_datasets_using_mean_and_range,
    "43_comparing_two_datasets_using_median_and_iqr": arch_43_comparing_two_datasets_using_median_and_iqr,
    "44_contextual_sa_temperatures_mean_and_range": arch_44_contextual_sa_temperatures_mean_and_range,
    "45_contextual_sa_mathematics_exam_scores_analysis": arch_45_contextual_sa_mathematics_exam_scores_analysis,
    "46_contextual_sa_monthly_household_expenditure_median": arch_46_contextual_sa_monthly_household_expenditure_median,
    "47_error_analysis_calculating_median_without_ordering_data": arch_47_error_analysis_calculating_median_without_ordering_data,
    "48_error_analysis_confusing_frequency_with_data_value_in_mode": arch_48_error_analysis_confusing_frequency_with_data_value_in_mode,
    "49_error_analysis_dividing_by_wrong_n_in_mean_frequency_table": arch_49_error_analysis_dividing_by_wrong_n_in_mean_frequency_table,
    "50_compound_multi_stage_statistical_investigation_synthesis": arch_50_compound_multi_stage_statistical_investigation_synthesis,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

SUBSKILLS_TUPLES: List[Tuple[str, str]] = [
    (key, key[3:].replace("_", " ").title()) for key in SUBSKILLS
]


def generate_grade9_data_summarise_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Collect, Organise & Summarise Data question."""
    r = random.Random(seed)
    if subskill and subskill in ARCHETYPE_MAP:
        builder = ARCHETYPE_MAP[subskill]
        chosen_subskill = subskill
    elif subskill:
        # Match by prefix or substring if requested
        s_clean = str(subskill).strip()
        matched = None
        for k, b in ARCHETYPE_MAP.items():
            if k.startswith(s_clean) or s_clean in k:
                matched = (k, b)
                break
        if matched:
            chosen_subskill, builder = matched
        else:
            chosen_subskill = r.choice(SUBSKILLS)
            builder = ARCHETYPE_MAP[chosen_subskill]
    else:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(r)
    q["subskill"] = chosen_subskill
    q["grade"] = "9"
    q["subject"] = "Mathematics"
    q["topic"] = "Collect, organise and summarise data"
    q["term"] = 4
    q.setdefault("caps_weight_percent", 10)
    q.setdefault("suggested_duration_mins", 4)
    q.setdefault("difficulty", "medium")
    q.setdefault("mode", "compound")
    if not q.get("prompt"):
        q["prompt"] = q.get("question_text")
    if not q.get("sample_answer"):
        q["sample_answer"] = str(q.get("correct_answer"))
    return q


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """6-Pillar Generator Contract entry point."""
    r = random.Random(seed)
    questions: List[Dict[str, Any]] = []

    if subskill and subskill in ARCHETYPE_MAP:
        candidates = [subskill]
    else:
        candidates = SUBSKILLS

    for i in range(count):
        sub = candidates[i % len(candidates)] if len(candidates) > 1 else candidates[0]
        sub_seed = r.randint(1, 1_000_000_000)
        q = generate_grade9_data_summarise_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
