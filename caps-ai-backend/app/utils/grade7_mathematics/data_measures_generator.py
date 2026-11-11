"""Grade 7 Mathematics - Interpret, Analyse and Report on Data Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 4/01. Interpret analyse and report on data.md
Focus: Measures of central tendency (mean, median, mode), spread (range), extreme values (outliers), histograms, pie charts, line graphs, stem-and-leaf plots, bias and misleading graphs, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .data_measures_archetypes_01_25 import (
    arch_01_calculate_mean_integer_dataset,
    arch_02_calculate_mean_formula_and_definition,
    arch_03_calculate_mean_with_decimal_result,
    arch_04_calculate_mean_find_missing_value,
    arch_05_calculate_mean_word_problem_temperatures,
    arch_06_calculate_median_odd_count_dataset,
    arch_07_calculate_median_even_count_dataset,
    arch_08_calculate_median_unordered_list_sorting,
    arch_09_calculate_median_test_scores_word_problem,
    arch_10_calculate_mode_single_most_frequent,
    arch_11_calculate_mode_bimodal_dataset,
    arch_12_calculate_mode_no_mode_dataset,
    arch_13_calculate_mode_categorical_survey_data,
    arch_14_calculate_range_spread_of_data,
    arch_15_calculate_range_temperature_extremes,
    arch_16_data_extremes_outliers_identification,
    arch_17_data_extremes_outliers_effect_on_mean,
    arch_18_outlier_impact_mean_vs_median_comparison,
    arch_19_population_vs_sample_definitions,
    arch_20_population_vs_sample_representative_size,
    arch_21_frequency_table_percentage_calculation,
    arch_22_frequency_table_finding_total_and_frequencies,
    arch_23_bar_graph_interpretation_single_bars_svg,
    arch_24_bar_graph_read_highest_lowest_frequencies,
    arch_25_double_bar_graph_compare_two_groups_svg,
)
from .data_measures_archetypes_26_50 import (
    arch_26_double_bar_graph_gender_comparison_census,
    arch_27_histogram_interpretation_grouped_intervals_svg,
    arch_28_histogram_modal_interval_identification,
    arch_29_histogram_count_learners_above_threshold,
    arch_30_pie_chart_interpretation_percentage_sectors_svg,
    arch_31_pie_chart_calculate_sector_angle,
    arch_32_pie_chart_convert_percentage_to_raw_frequency,
    arch_33_pie_chart_fractional_shares_budget,
    arch_34_line_graph_temperature_trend_over_time_svg,
    arch_35_line_graph_interpolate_and_predict,
    arch_36_stem_and_leaf_display_reading_values_svg,
    arch_37_stem_and_leaf_find_median_and_mode,
    arch_38_stem_and_leaf_calculate_range,
    arch_39_identifying_bias_in_survey_sample,
    arch_40_identifying_bias_in_leading_survey_questions,
    arch_41_misleading_graph_truncated_axis_trap_svg,
    arch_42_misleading_graph_unequal_scaling_or_width,
    arch_43_misleading_graph_3d_perspective_distortion,
    arch_44_choosing_appropriate_measure_mean_vs_median,
    arch_45_choosing_appropriate_measure_mode_for_shoe_sizes,
    arch_46_drawing_valid_statistical_conclusions,
    arch_47_data_summary_report_writing_three_points,
    arch_48_common_error_forgetting_to_order_for_median,
    arch_49_common_error_confusing_mode_with_frequency_count,
    arch_50_data_measures_comprehensive_diagnostic_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_calculate_mean_integer_dataset": arch_01_calculate_mean_integer_dataset,
    "02_calculate_mean_formula_and_definition": arch_02_calculate_mean_formula_and_definition,
    "03_calculate_mean_with_decimal_result": arch_03_calculate_mean_with_decimal_result,
    "04_calculate_mean_find_missing_value": arch_04_calculate_mean_find_missing_value,
    "05_calculate_mean_word_problem_temperatures": arch_05_calculate_mean_word_problem_temperatures,
    "06_calculate_median_odd_count_dataset": arch_06_calculate_median_odd_count_dataset,
    "07_calculate_median_even_count_dataset": arch_07_calculate_median_even_count_dataset,
    "08_calculate_median_unordered_list_sorting": arch_08_calculate_median_unordered_list_sorting,
    "09_calculate_median_test_scores_word_problem": arch_09_calculate_median_test_scores_word_problem,
    "10_calculate_mode_single_most_frequent": arch_10_calculate_mode_single_most_frequent,
    "11_calculate_mode_bimodal_dataset": arch_11_calculate_mode_bimodal_dataset,
    "12_calculate_mode_no_mode_dataset": arch_12_calculate_mode_no_mode_dataset,
    "13_calculate_mode_categorical_survey_data": arch_13_calculate_mode_categorical_survey_data,
    "14_calculate_range_spread_of_data": arch_14_calculate_range_spread_of_data,
    "15_calculate_range_temperature_extremes": arch_15_calculate_range_temperature_extremes,
    "16_data_extremes_outliers_identification": arch_16_data_extremes_outliers_identification,
    "17_data_extremes_outliers_effect_on_mean": arch_17_data_extremes_outliers_effect_on_mean,
    "18_outlier_impact_mean_vs_median_comparison": arch_18_outlier_impact_mean_vs_median_comparison,
    "19_population_vs_sample_definitions": arch_19_population_vs_sample_definitions,
    "20_population_vs_sample_representative_size": arch_20_population_vs_sample_representative_size,
    "21_frequency_table_percentage_calculation": arch_21_frequency_table_percentage_calculation,
    "22_frequency_table_finding_total_and_frequencies": arch_22_frequency_table_finding_total_and_frequencies,
    "23_bar_graph_interpretation_single_bars_svg": arch_23_bar_graph_interpretation_single_bars_svg,
    "24_bar_graph_read_highest_lowest_frequencies": arch_24_bar_graph_read_highest_lowest_frequencies,
    "25_double_bar_graph_compare_two_groups_svg": arch_25_double_bar_graph_compare_two_groups_svg,
    "26_double_bar_graph_gender_comparison_census": arch_26_double_bar_graph_gender_comparison_census,
    "27_histogram_interpretation_grouped_intervals_svg": arch_27_histogram_interpretation_grouped_intervals_svg,
    "28_histogram_modal_interval_identification": arch_28_histogram_modal_interval_identification,
    "29_histogram_count_learners_above_threshold": arch_29_histogram_count_learners_above_threshold,
    "30_pie_chart_interpretation_percentage_sectors_svg": arch_30_pie_chart_interpretation_percentage_sectors_svg,
    "31_pie_chart_calculate_sector_angle": arch_31_pie_chart_calculate_sector_angle,
    "32_pie_chart_convert_percentage_to_raw_frequency": arch_32_pie_chart_convert_percentage_to_raw_frequency,
    "33_pie_chart_fractional_shares_budget": arch_33_pie_chart_fractional_shares_budget,
    "34_line_graph_temperature_trend_over_time_svg": arch_34_line_graph_temperature_trend_over_time_svg,
    "35_line_graph_interpolate_and_predict": arch_35_line_graph_interpolate_and_predict,
    "36_stem_and_leaf_display_reading_values_svg": arch_36_stem_and_leaf_display_reading_values_svg,
    "37_stem_and_leaf_find_median_and_mode": arch_37_stem_and_leaf_find_median_and_mode,
    "38_stem_and_leaf_calculate_range": arch_38_stem_and_leaf_calculate_range,
    "39_identifying_bias_in_survey_sample": arch_39_identifying_bias_in_survey_sample,
    "40_identifying_bias_in_leading_survey_questions": arch_40_identifying_bias_in_leading_survey_questions,
    "41_misleading_graph_truncated_axis_trap_svg": arch_41_misleading_graph_truncated_axis_trap_svg,
    "42_misleading_graph_unequal_scaling_or_width": arch_42_misleading_graph_unequal_scaling_or_width,
    "43_misleading_graph_3d_perspective_distortion": arch_43_misleading_graph_3d_perspective_distortion,
    "44_choosing_appropriate_measure_mean_vs_median": arch_44_choosing_appropriate_measure_mean_vs_median,
    "45_choosing_appropriate_measure_mode_for_shoe_sizes": arch_45_choosing_appropriate_measure_mode_for_shoe_sizes,
    "46_drawing_valid_statistical_conclusions": arch_46_drawing_valid_statistical_conclusions,
    "47_data_summary_report_writing_three_points": arch_47_data_summary_report_writing_three_points,
    "48_common_error_forgetting_to_order_for_median": arch_48_common_error_forgetting_to_order_for_median,
    "49_common_error_confusing_mode_with_frequency_count": arch_49_common_error_confusing_mode_with_frequency_count,
    "50_data_measures_comprehensive_diagnostic_autopsy": arch_50_data_measures_comprehensive_diagnostic_autopsy,
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
