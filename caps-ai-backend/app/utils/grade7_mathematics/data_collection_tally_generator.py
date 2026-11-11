"""Grade 7 Mathematics - Collect, Organise and Summarise Data Generator.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Collect organise and summarise data.md
Provides 50 distinct semantic archetypes covering data collection, bias, tally tables, stem-and-leaf, mean, median, mode, range, and grouped data.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .data_collection_archetypes_01_25 import (
    arch_01_population_vs_sample_definitions,
    arch_02_identify_population_and_sample_in_context,
    arch_03_sample_bias_identification_and_critique,
    arch_04_sample_size_sufficiency_critique,
    arch_05_data_collection_methods_comparison_questionnaire_vs_interview,
    arch_06_questionnaire_design_avoiding_leading_questions,
    arch_07_questionnaire_design_multiple_choice_categories,
    arch_08_discrete_vs_continuous_data_in_statistics,
    arch_09_tally_marks_representation_of_counts,
    arch_10_reading_tally_table_frequencies,
    arch_11_completing_frequency_table_from_raw_data,
    arch_12_frequency_table_finding_total_sample_size,
    arch_13_grouped_frequency_table_equal_interval_widths,
    arch_14_grouped_frequency_table_tallying_scores,
    arch_15_stem_and_leaf_display_reading_values,
    arch_16_stem_and_leaf_display_constructing_from_data,
    arch_17_stem_and_leaf_identifying_key,
    arch_18_mode_unimodal_from_raw_list,
    arch_19_mode_bimodal_or_no_mode_identification,
    arch_20_mode_from_frequency_table,
    arch_21_median_odd_number_of_data_values,
    arch_22_median_even_number_of_data_values,
    arch_23_median_from_ordered_stem_and_leaf,
    arch_24_mean_calculation_simple_integer_list,
    arch_25_mean_calculation_with_decimal_result,
)
from .data_collection_archetypes_26_50 import (
    arch_26_mean_from_frequency_table_ungrouped,
    arch_27_median_from_frequency_table,
    arch_28_mode_from_frequency_table,
    arch_29_range_from_frequency_table,
    arch_30_missing_frequency_given_total_count,
    arch_31_find_missing_value_given_mean,
    arch_32_find_missing_value_given_median,
    arch_33_find_missing_value_given_range,
    arch_34_effect_of_outlier_on_mean,
    arch_35_effect_of_outlier_on_median,
    arch_36_effect_of_outlier_on_mode,
    arch_37_choosing_appropriate_measure_mean_vs_median_with_outlier,
    arch_38_choosing_appropriate_measure_mode_for_shoe_size,
    arch_39_stem_and_leaf_find_range,
    arch_40_stem_and_leaf_find_median,
    arch_41_stem_and_leaf_find_mode,
    arch_42_stem_and_leaf_find_mean,
    arch_43_grouped_data_class_intervals_frequency,
    arch_44_grouped_data_modal_class_identification,
    arch_45_grouped_data_tally_and_counts,
    arch_46_comparing_two_data_sets_using_mean_and_range,
    arch_47_comparing_two_data_sets_using_median_and_mode,
    arch_48_data_collection_survey_questionnaire_bias_detection,
    arch_49_data_collection_designing_unbiased_questions,
    arch_50_data_reporting_and_summarising_conclusions,
)

ARCHETYPE_BUILDERS = {
    "01_population_vs_sample_definitions": arch_01_population_vs_sample_definitions,
    "02_identify_population_and_sample_in_context": arch_02_identify_population_and_sample_in_context,
    "03_sample_bias_identification_and_critique": arch_03_sample_bias_identification_and_critique,
    "04_sample_size_sufficiency_critique": arch_04_sample_size_sufficiency_critique,
    "05_data_collection_methods_comparison_questionnaire_vs_interview": arch_05_data_collection_methods_comparison_questionnaire_vs_interview,
    "06_questionnaire_design_avoiding_leading_questions": arch_06_questionnaire_design_avoiding_leading_questions,
    "07_questionnaire_design_multiple_choice_categories": arch_07_questionnaire_design_multiple_choice_categories,
    "08_discrete_vs_continuous_data_in_statistics": arch_08_discrete_vs_continuous_data_in_statistics,
    "09_tally_marks_representation_of_counts": arch_09_tally_marks_representation_of_counts,
    "10_reading_tally_table_frequencies": arch_10_reading_tally_table_frequencies,
    "11_completing_frequency_table_from_raw_data": arch_11_completing_frequency_table_from_raw_data,
    "12_frequency_table_finding_total_sample_size": arch_12_frequency_table_finding_total_sample_size,
    "13_grouped_frequency_table_equal_interval_widths": arch_13_grouped_frequency_table_equal_interval_widths,
    "14_grouped_frequency_table_tallying_scores": arch_14_grouped_frequency_table_tallying_scores,
    "15_stem_and_leaf_display_reading_values": arch_15_stem_and_leaf_display_reading_values,
    "16_stem_and_leaf_display_constructing_from_data": arch_16_stem_and_leaf_display_constructing_from_data,
    "17_stem_and_leaf_identifying_key": arch_17_stem_and_leaf_identifying_key,
    "18_mode_unimodal_from_raw_list": arch_18_mode_unimodal_from_raw_list,
    "19_mode_bimodal_or_no_mode_identification": arch_19_mode_bimodal_or_no_mode_identification,
    "20_mode_from_frequency_table": arch_20_mode_from_frequency_table,
    "21_median_odd_number_of_data_values": arch_21_median_odd_number_of_data_values,
    "22_median_even_number_of_data_values": arch_22_median_even_number_of_data_values,
    "23_median_from_ordered_stem_and_leaf": arch_23_median_from_ordered_stem_and_leaf,
    "24_mean_calculation_simple_integer_list": arch_24_mean_calculation_simple_integer_list,
    "25_mean_calculation_with_decimal_result": arch_25_mean_calculation_with_decimal_result,
    "26_mean_from_frequency_table_ungrouped": arch_26_mean_from_frequency_table_ungrouped,
    "27_median_from_frequency_table": arch_27_median_from_frequency_table,
    "28_mode_from_frequency_table": arch_28_mode_from_frequency_table,
    "29_range_from_frequency_table": arch_29_range_from_frequency_table,
    "30_missing_frequency_given_total_count": arch_30_missing_frequency_given_total_count,
    "31_find_missing_value_given_mean": arch_31_find_missing_value_given_mean,
    "32_find_missing_value_given_median": arch_32_find_missing_value_given_median,
    "33_find_missing_value_given_range": arch_33_find_missing_value_given_range,
    "34_effect_of_outlier_on_mean": arch_34_effect_of_outlier_on_mean,
    "35_effect_of_outlier_on_median": arch_35_effect_of_outlier_on_median,
    "36_effect_of_outlier_on_mode": arch_36_effect_of_outlier_on_mode,
    "37_choosing_appropriate_measure_mean_vs_median_with_outlier": arch_37_choosing_appropriate_measure_mean_vs_median_with_outlier,
    "38_choosing_appropriate_measure_mode_for_shoe_size": arch_38_choosing_appropriate_measure_mode_for_shoe_size,
    "39_stem_and_leaf_find_range": arch_39_stem_and_leaf_find_range,
    "40_stem_and_leaf_find_median": arch_40_stem_and_leaf_find_median,
    "41_stem_and_leaf_find_mode": arch_41_stem_and_leaf_find_mode,
    "42_stem_and_leaf_find_mean": arch_42_stem_and_leaf_find_mean,
    "43_grouped_data_class_intervals_frequency": arch_43_grouped_data_class_intervals_frequency,
    "44_grouped_data_modal_class_identification": arch_44_grouped_data_modal_class_identification,
    "45_grouped_data_tally_and_counts": arch_45_grouped_data_tally_and_counts,
    "46_comparing_two_data_sets_using_mean_and_range": arch_46_comparing_two_data_sets_using_mean_and_range,
    "47_comparing_two_data_sets_using_median_and_mode": arch_47_comparing_two_data_sets_using_median_and_mode,
    "48_data_collection_survey_questionnaire_bias_detection": arch_48_data_collection_survey_questionnaire_bias_detection,
    "49_data_collection_designing_unbiased_questions": arch_49_data_collection_designing_unbiased_questions,
    "50_data_reporting_and_summarising_conclusions": arch_50_data_reporting_and_summarising_conclusions,
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


generate = generate_question
