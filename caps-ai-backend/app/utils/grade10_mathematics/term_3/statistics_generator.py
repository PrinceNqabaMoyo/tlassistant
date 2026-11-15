"""Grade 10 Mathematics — Term 3: Statistics (Deterministic 6-Pillar Generator).
100% aligned with South African National Curriculum Standards (Grade 10 Mathematics: Statistics).
Contains >= 50 distinct semantic archetypes split across:
- statistics_archetypes_01_25.py (Archetypes 01–25)
- statistics_archetypes_26_50.py (Archetypes 26–50)

Zero-LLM: 100% deterministic Python calculations with South African comma decimals ({,}).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade10_mathematics.term_3.statistics_archetypes_01_25 import (
    arch_01_qualitative_vs_quantitative_classification,
    arch_02_discrete_vs_continuous_identification,
    arch_03_categorical_to_frequency_table,
    arch_04_mean_ungrouped_small_dataset,
    arch_05_median_ungrouped_odd_n,
    arch_06_median_ungrouped_even_n,
    arch_07_mode_ungrouped_unimodal_bimodal,
    arch_08_mean_median_mode_comparison_single_dataset,
    arch_09_missing_value_from_known_mean,
    arch_10_missing_value_from_known_median,
    arch_11_effect_of_adding_constant_on_central_tendency,
    arch_12_effect_of_multiplying_by_constant_on_central_tendency,
    arch_13_frequency_table_mean_ungrouped,
    arch_14_frequency_table_median_and_mode_ungrouped,
    arch_15_range_calculation_ungrouped,
    arch_16_lower_quartile_q1_ungrouped,
    arch_17_upper_quartile_q3_ungrouped,
    arch_18_interquartile_range_iqr_calculation,
    arch_19_semi_interquartile_range_calculation,
    arch_20_five_number_summary_from_raw_data,
    arch_21_percentiles_calculation_simple,
    arch_22_grouped_data_class_midpoints,
    arch_23_grouped_data_modal_class,
    arch_24_grouped_data_median_class_interval,
    arch_25_grouped_data_estimated_mean,
)
from app.utils.grade10_mathematics.term_3.statistics_archetypes_26_50 import (
    arch_26_box_whisker_read_five_number_summary,
    arch_27_box_whisker_read_percentages,
    arch_28_box_whisker_calculate_iqr_and_range,
    arch_29_box_whisker_construct_from_raw_data,
    arch_30_skewness_identification_symmetrical,
    arch_31_skewness_identification_positive_skew,
    arch_32_skewness_identification_negative_skew,
    arch_33_skewness_mean_vs_median_relationship,
    arch_34_outliers_1_5_iqr_rule_fences,
    arch_35_outliers_identification_in_dataset,
    arch_36_parallel_box_whisker_comparison_medians,
    arch_37_parallel_box_whisker_comparison_spread,
    arch_38_parallel_box_whisker_overall_performance,
    arch_39_histogram_reading_frequencies,
    arch_40_histogram_total_frequency_and_proportions,
    arch_41_histogram_modal_class_identification,
    arch_42_histogram_estimate_mean_from_visual,
    arch_43_frequency_polygon_read_class_peaks,
    arch_44_frequency_polygon_anchoring_concept,
    arch_45_stem_and_leaf_read_data_values,
    arch_46_stem_and_leaf_five_number_summary,
    arch_47_grouped_data_cumulative_frequency_table,
    arch_48_grouped_data_percentile_estimation,
    arch_49_data_cleaning_and_impact_of_extreme_values,
    arch_50_comprehensive_statistical_analysis_summary,
)

TOPIC = "Statistics"
TOPIC_ID = "grade10_math_statistics"
LO = "math10_statistics_measures"

ARCHETYPE_DISPATCH: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Archetypes 01 to 25
    "01_qualitative_vs_quantitative_classification": arch_01_qualitative_vs_quantitative_classification,
    "02_discrete_vs_continuous_identification": arch_02_discrete_vs_continuous_identification,
    "03_categorical_to_frequency_table": arch_03_categorical_to_frequency_table,
    "04_mean_ungrouped_small_dataset": arch_04_mean_ungrouped_small_dataset,
    "05_median_ungrouped_odd_n": arch_05_median_ungrouped_odd_n,
    "06_median_ungrouped_even_n": arch_06_median_ungrouped_even_n,
    "07_mode_ungrouped_unimodal_bimodal": arch_07_mode_ungrouped_unimodal_bimodal,
    "08_mean_median_mode_comparison_single_dataset": arch_08_mean_median_mode_comparison_single_dataset,
    "09_missing_value_from_known_mean": arch_09_missing_value_from_known_mean,
    "10_missing_value_from_known_median": arch_10_missing_value_from_known_median,
    "11_effect_of_adding_constant_on_central_tendency": arch_11_effect_of_adding_constant_on_central_tendency,
    "12_effect_of_multiplying_by_constant_on_central_tendency": arch_12_effect_of_multiplying_by_constant_on_central_tendency,
    "13_frequency_table_mean_ungrouped": arch_13_frequency_table_mean_ungrouped,
    "14_frequency_table_median_and_mode_ungrouped": arch_14_frequency_table_median_and_mode_ungrouped,
    "15_range_calculation_ungrouped": arch_15_range_calculation_ungrouped,
    "16_lower_quartile_q1_ungrouped": arch_16_lower_quartile_q1_ungrouped,
    "17_upper_quartile_q3_ungrouped": arch_17_upper_quartile_q3_ungrouped,
    "18_interquartile_range_iqr_calculation": arch_18_interquartile_range_iqr_calculation,
    "19_semi_interquartile_range_calculation": arch_19_semi_interquartile_range_calculation,
    "20_five_number_summary_from_raw_data": arch_20_five_number_summary_from_raw_data,
    "21_percentiles_calculation_simple": arch_21_percentiles_calculation_simple,
    "22_grouped_data_class_midpoints": arch_22_grouped_data_class_midpoints,
    "23_grouped_data_modal_class": arch_23_grouped_data_modal_class,
    "24_grouped_data_median_class_interval": arch_24_grouped_data_median_class_interval,
    "25_grouped_data_estimated_mean": arch_25_grouped_data_estimated_mean,
    # Archetypes 26 to 50
    "26_box_whisker_read_five_number_summary": arch_26_box_whisker_read_five_number_summary,
    "27_box_whisker_read_percentages": arch_27_box_whisker_read_percentages,
    "28_box_whisker_calculate_iqr_and_range": arch_28_box_whisker_calculate_iqr_and_range,
    "29_box_whisker_construct_from_raw_data": arch_29_box_whisker_construct_from_raw_data,
    "30_skewness_identification_symmetrical": arch_30_skewness_identification_symmetrical,
    "31_skewness_identification_positive_skew": arch_31_skewness_identification_positive_skew,
    "32_skewness_identification_negative_skew": arch_32_skewness_identification_negative_skew,
    "33_skewness_mean_vs_median_relationship": arch_33_skewness_mean_vs_median_relationship,
    "34_outliers_1_5_iqr_rule_fences": arch_34_outliers_1_5_iqr_rule_fences,
    "35_outliers_identification_in_dataset": arch_35_outliers_identification_in_dataset,
    "36_parallel_box_whisker_comparison_medians": arch_36_parallel_box_whisker_comparison_medians,
    "37_parallel_box_whisker_comparison_spread": arch_37_parallel_box_whisker_comparison_spread,
    "38_parallel_box_whisker_overall_performance": arch_38_parallel_box_whisker_overall_performance,
    "39_histogram_reading_frequencies": arch_39_histogram_reading_frequencies,
    "40_histogram_total_frequency_and_proportions": arch_40_histogram_total_frequency_and_proportions,
    "41_histogram_modal_class_identification": arch_41_histogram_modal_class_identification,
    "42_histogram_estimate_mean_from_visual": arch_42_histogram_estimate_mean_from_visual,
    "43_frequency_polygon_read_class_peaks": arch_43_frequency_polygon_read_class_peaks,
    "44_frequency_polygon_anchoring_concept": arch_44_frequency_polygon_anchoring_concept,
    "45_stem_and_leaf_read_data_values": arch_45_stem_and_leaf_read_data_values,
    "46_stem_and_leaf_five_number_summary": arch_46_stem_and_leaf_five_number_summary,
    "47_grouped_data_cumulative_frequency_table": arch_47_grouped_data_cumulative_frequency_table,
    "48_grouped_data_percentile_estimation": arch_48_grouped_data_percentile_estimation,
    "49_data_cleaning_and_impact_of_extreme_values": arch_49_data_cleaning_and_impact_of_extreme_values,
    "50_comprehensive_statistical_analysis_summary": arch_50_comprehensive_statistical_analysis_summary,
}

# Legacy aliases for backward compatibility
LEGACY_ALIASES: Dict[str, str] = {
    "five_number_summary": "20_five_number_summary_from_raw_data",
    "box_whisker_skewness": "30_skewness_identification_symmetrical",
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
        "term": 3,
        "archetypes": ARCHETYPES,
        "archetype_count": len(ARCHETYPES),
    }


def generate_subskill(subskill: str, seed: Optional[int] = None, **kwargs) -> Dict[str, Any]:
    r = _rng(seed)
    resolved = LEGACY_ALIASES.get(subskill, subskill)
    fn = ARCHETYPE_DISPATCH.get(resolved)
    if not fn:
        resolved = "04_mean_ungrouped_small_dataset"
        fn = ARCHETYPE_DISPATCH[resolved]

    q = fn(r)
    q["term"] = 3
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
