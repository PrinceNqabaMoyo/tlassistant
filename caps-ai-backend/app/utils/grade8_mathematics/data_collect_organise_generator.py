"""
Grade 8 Mathematics - Collect, Organise & Summarise Data Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Collect organise and summarise data.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .collect_organise_archetypes_01_25 import (
    arch_01_population_vs_sample_identification,
    arch_02_identifying_sample_size_adequacy,
    arch_03_identifying_sampling_bias_location,
    arch_04_random_sampling_methods,
    arch_05_questionnaire_open_vs_closed_questions,
    arch_06_questionnaire_identifying_leading_or_biased_questions,
    arch_07_tally_table_counting_frequencies_from_raw_data,
    arch_08_tally_table_calculating_missing_frequency_given_total,
    arch_09_tally_table_identifying_mode_category,
    arch_10_tally_table_calculating_percentage_frequency,
    arch_11_grouped_data_identifying_class_interval_for_score,
    arch_12_grouped_data_determining_interval_width,
    arch_13_grouped_data_explaining_non_overlapping_intervals,
    arch_14_grouped_data_identifying_modal_class_interval,
    arch_15_grouped_data_calculating_total_sample_size_from_frequencies,
    arch_16_grouped_data_frequency_percentage_calculation,
    arch_17_stem_and_leaf_interpreting_key,
    arch_18_stem_and_leaf_identifying_minimum_and_maximum,
    arch_19_stem_and_leaf_calculating_range,
    arch_20_stem_and_leaf_identifying_mode,
    arch_21_stem_and_leaf_finding_median_odd_count,
    arch_22_stem_and_leaf_finding_median_even_count,
    arch_23_stem_and_leaf_total_count_of_observations,
    arch_24_stem_and_leaf_counting_values_above_or_below_threshold,
    arch_25_stem_and_leaf_constructing_leaves_from_raw_scores,
)

from .collect_organise_archetypes_26_50 import (
    arch_26_calculating_mean_of_ungrouped_data_set,
    arch_27_finding_median_of_ordered_data_odd_number,
    arch_28_finding_median_of_ordered_data_even_number,
    arch_29_finding_median_of_unordered_data_set,
    arch_30_identifying_mode_of_discrete_data_set,
    arch_31_identifying_bimodal_data_set,
    arch_32_identifying_no_mode_in_data_set,
    arch_33_calculating_range_of_raw_data_set,
    arch_34_calculating_mean_with_decimal_result,
    arch_35_effect_of_extreme_value_outlier_on_mean,
    arch_36_effect_of_outlier_on_median_resistance,
    arch_37_choosing_appropriate_measure_of_central_tendency,
    arch_38_finding_missing_value_given_the_mean,
    arch_39_finding_missing_value_given_the_range,
    arch_40_calculating_mean_from_frequency_table,
    arch_41_identifying_mode_from_frequency_table,
    arch_42_identifying_median_from_cumulative_frequency,
    arch_43_two_way_contingency_table_reading_cell_frequency,
    arch_44_two_way_table_calculating_marginal_row_or_column_total,
    arch_45_two_way_table_finding_missing_cell_value,
    arch_46_comparing_two_data_sets_by_means,
    arch_47_comparing_two_data_sets_by_range_consistency,
    arch_48_data_collection_method_survey_vs_experiment,
    arch_49_identifying_measurement_units_and_instruments,
    arch_50_full_data_cycle_summary_evaluation,
)


BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10
    arch_01_population_vs_sample_identification,
    arch_02_identifying_sample_size_adequacy,
    arch_03_identifying_sampling_bias_location,
    arch_04_random_sampling_methods,
    arch_05_questionnaire_open_vs_closed_questions,
    arch_06_questionnaire_identifying_leading_or_biased_questions,
    arch_07_tally_table_counting_frequencies_from_raw_data,
    arch_08_tally_table_calculating_missing_frequency_given_total,
    arch_09_tally_table_identifying_mode_category,
    arch_10_tally_table_calculating_percentage_frequency,
    # 11 - 20
    arch_11_grouped_data_identifying_class_interval_for_score,
    arch_12_grouped_data_determining_interval_width,
    arch_13_grouped_data_explaining_non_overlapping_intervals,
    arch_14_grouped_data_identifying_modal_class_interval,
    arch_15_grouped_data_calculating_total_sample_size_from_frequencies,
    arch_16_grouped_data_frequency_percentage_calculation,
    arch_17_stem_and_leaf_interpreting_key,
    arch_18_stem_and_leaf_identifying_minimum_and_maximum,
    arch_19_stem_and_leaf_calculating_range,
    arch_20_stem_and_leaf_identifying_mode,
    # 21 - 28
    arch_21_stem_and_leaf_finding_median_odd_count,
    arch_22_stem_and_leaf_finding_median_even_count,
    arch_23_stem_and_leaf_total_count_of_observations,
    arch_24_stem_and_leaf_counting_values_above_or_below_threshold,
    arch_25_stem_and_leaf_constructing_leaves_from_raw_scores,
    arch_26_calculating_mean_of_ungrouped_data_set,
    arch_27_finding_median_of_ordered_data_odd_number,
    arch_28_finding_median_of_ordered_data_even_number,
    # 29 - 36
    arch_29_finding_median_of_unordered_data_set,
    arch_30_identifying_mode_of_discrete_data_set,
    arch_31_identifying_bimodal_data_set,
    arch_32_identifying_no_mode_in_data_set,
    arch_33_calculating_range_of_raw_data_set,
    arch_34_calculating_mean_with_decimal_result,
    arch_35_effect_of_extreme_value_outlier_on_mean,
    arch_36_effect_of_outlier_on_median_resistance,
    # 37 - 44
    arch_37_choosing_appropriate_measure_of_central_tendency,
    arch_38_finding_missing_value_given_the_mean,
    arch_39_finding_missing_value_given_the_range,
    arch_40_calculating_mean_from_frequency_table,
    arch_41_identifying_mode_from_frequency_table,
    arch_42_identifying_median_from_cumulative_frequency,
    arch_43_two_way_contingency_table_reading_cell_frequency,
    arch_44_two_way_table_calculating_marginal_row_or_column_total,
    # 45 - 50
    arch_45_two_way_table_finding_missing_cell_value,
    arch_46_comparing_two_data_sets_by_means,
    arch_47_comparing_two_data_sets_by_range_consistency,
    arch_48_data_collection_method_survey_vs_experiment,
    arch_49_identifying_measurement_units_and_instruments,
    arch_50_full_data_cycle_summary_evaluation,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_population_vs_sample_identification",
    "02_identifying_sample_size_adequacy",
    "03_identifying_sampling_bias_location",
    "04_random_sampling_methods",
    "05_questionnaire_open_vs_closed_questions",
    "06_questionnaire_identifying_leading_or_biased_questions",
    "07_tally_table_counting_frequencies_from_raw_data",
    "08_tally_table_calculating_missing_frequency_given_total",
    "09_tally_table_identifying_mode_category",
    "10_tally_table_calculating_percentage_frequency",
    # 11 - 20
    "11_grouped_data_identifying_class_interval_for_score",
    "12_grouped_data_determining_interval_width",
    "13_grouped_data_explaining_non_overlapping_intervals",
    "14_grouped_data_identifying_modal_class_interval",
    "15_grouped_data_calculating_total_sample_size_from_frequencies",
    "16_grouped_data_frequency_percentage_calculation",
    "17_stem_and_leaf_interpreting_key",
    "18_stem_and_leaf_identifying_minimum_and_maximum",
    "19_stem_and_leaf_calculating_range",
    "20_stem_and_leaf_identifying_mode",
    # 21 - 28
    "21_stem_and_leaf_finding_median_odd_count",
    "22_stem_and_leaf_finding_median_even_count",
    "23_stem_and_leaf_total_count_of_observations",
    "24_stem_and_leaf_counting_values_above_or_below_threshold",
    "25_stem_and_leaf_constructing_leaves_from_raw_scores",
    "26_calculating_mean_of_ungrouped_data_set",
    "27_finding_median_of_ordered_data_odd_number",
    "28_finding_median_of_ordered_data_even_number",
    # 29 - 36
    "29_finding_median_of_unordered_data_set",
    "30_identifying_mode_of_discrete_data_set",
    "31_identifying_bimodal_data_set",
    "32_identifying_no_mode_in_data_set",
    "33_calculating_range_of_raw_data_set",
    "34_calculating_mean_with_decimal_result",
    "35_effect_of_extreme_value_outlier_on_mean",
    "36_effect_of_outlier_on_median_resistance",
    # 37 - 44
    "37_choosing_appropriate_measure_of_central_tendency",
    "38_finding_missing_value_given_the_mean",
    "39_finding_missing_value_given_the_range",
    "40_calculating_mean_from_frequency_table",
    "41_identifying_mode_from_frequency_table",
    "42_identifying_median_from_cumulative_frequency",
    "43_two_way_contingency_table_reading_cell_frequency",
    "44_two_way_table_calculating_marginal_row_or_column_total",
    # 45 - 50
    "45_two_way_table_finding_missing_cell_value",
    "46_comparing_two_data_sets_by_means",
    "47_comparing_two_data_sets_by_range_consistency",
    "48_data_collection_method_survey_vs_experiment",
    "49_identifying_measurement_units_and_instruments",
    "50_full_data_cycle_summary_evaluation",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases
DISPATCH_TABLE["grouped_data_class_intervals"] = arch_11_grouped_data_identifying_class_interval_for_score
DISPATCH_TABLE["tally_frequency_table_construction"] = arch_08_tally_table_calculating_missing_frequency_given_total
DISPATCH_TABLE["stem_and_leaf_interpretation"] = arch_18_stem_and_leaf_identifying_minimum_and_maximum
DISPATCH_TABLE["modal_class_interval_identification"] = arch_14_grouped_data_identifying_modal_class_interval
DISPATCH_TABLE["survey_bias_and_sampling"] = arch_03_identifying_sampling_bias_location


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(count):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None

        if subskill is not None:
            sub_key = str(subskill).strip()
            if sub_key in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[sub_key]
            else:
                sub_lower = sub_key.lower()
                for k, b in DISPATCH_TABLE.items():
                    if isinstance(k, str) and (sub_lower in k.lower() or k.lower() in sub_lower):
                        builder = b
                        break

        if builder is None and archetype_index is not None:
            idx = int(archetype_index)
            if idx in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[idx]
            elif 1 <= idx <= len(BUILDERS):
                builder = BUILDERS[idx - 1]

        if builder is None:
            builder = rng.choice(BUILDERS)

        q = builder(rng)
        q.setdefault("grade", 8)
        q.setdefault("subject", "Mathematics")
        q.setdefault("topic", "Collect organise and summarise data")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
