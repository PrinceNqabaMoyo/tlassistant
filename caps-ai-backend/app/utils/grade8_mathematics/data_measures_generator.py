"""
Grade 8 Mathematics - Interpret, Analyse and Report on Data Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/01. Interpret analyse and report on data.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .interpret_data_archetypes_01_25 import (
    BUILDERS_01_25,
    arch_01_calculating_arithmetic_mean_integer_result,
    arch_02_calculating_arithmetic_mean_decimal_rounded,
    arch_03_finding_median_odd_sample_size,
    arch_04_finding_median_even_sample_size,
    arch_05_finding_median_after_sorting_unordered_list,
    arch_06_identifying_mode_single_most_frequent_value,
    arch_07_identifying_bimodal_distribution,
    arch_08_identifying_no_mode_equal_frequencies,
    arch_09_calculating_range_of_sample,
    arch_10_identifying_extreme_outlier_value,
    arch_11_effect_of_adding_outlier_on_mean,
    arch_12_effect_of_adding_outlier_on_median,
    arch_13_effect_of_adding_outlier_on_range,
    arch_14_choosing_mean_vs_median_for_skewed_salary_data,
    arch_15_choosing_mode_for_commercial_inventory,
    arch_16_finding_missing_value_given_mean_and_n_minus_one_values,
    arch_17_finding_missing_value_given_range_and_extremes,
    arch_18_calculating_percentage_of_population_in_provincial_sample,
    arch_19_ranking_categories_from_tabular_summary,
    arch_20_calculating_actual_quantity_from_total_and_percentage,
    arch_21_comparing_two_classes_by_mean_score,
    arch_22_comparing_two_athletes_by_range_consistency,
    arch_23_identifying_convenience_sampling_bias,
    arch_24_identifying_voluntary_response_bias,
    arch_25_critiquing_advertiser_sample_claim,
)
from .interpret_data_archetypes_26_50 import (
    BUILDERS_26_50,
    arch_26_misleading_graph_truncated_vertical_axis,
    arch_27_misleading_pictograph_area_volume_distortion,
    arch_28_misleading_graph_irregular_time_intervals,
    arch_29_interpreting_line_graph_trend,
    arch_30_predicting_future_value_by_linear_extrapolation,
    arch_31_interpolating_value_from_data_table,
    arch_32_two_way_contingency_table_gender_by_grade,
    arch_33_calculating_percentage_proportion_from_subgroup,
    arch_34_identifying_modal_class_interval_from_histogram,
    arch_35_estimating_mean_from_grouped_frequency_table,
    arch_36_distinguishing_correlation_from_causation,
    arch_37_impact_of_sample_size_on_reliability,
    arch_38_interpreting_pie_chart_sector_budget,
    arch_39_choosing_median_for_household_income,
    arch_40_writing_summary_statement_from_data_table,
    arch_41_identifying_confounding_variable,
    arch_42_comparing_two_groups_spread_and_consistency,
    arch_43_percentage_increase_vs_percentage_point_difference,
    arch_44_evaluating_leading_question_bias,
    arch_45_evaluating_sampling_exclusion_bias,
    arch_46_interpreting_double_bar_chart_comparison,
    arch_47_interpreting_broken_line_temperature_graph,
    arch_48_calculating_median_from_stem_and_leaf_table,
    arch_49_calculating_combined_mean_of_two_classes,
    arch_50_synthesizing_data_for_policy_recommendation,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = BUILDERS_01_25 + BUILDERS_26_50

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_calculating_arithmetic_mean_integer_result",
    "02_calculating_arithmetic_mean_decimal_rounded",
    "03_finding_median_odd_sample_size",
    "04_finding_median_even_sample_size",
    "05_finding_median_after_sorting_unordered_list",
    "06_identifying_mode_single_most_frequent_value",
    "07_identifying_bimodal_distribution",
    "08_identifying_no_mode_equal_frequencies",
    "09_calculating_range_of_sample",
    "10_identifying_extreme_outlier_value",
    # 11 - 20
    "11_effect_of_adding_outlier_on_mean",
    "12_effect_of_adding_outlier_on_median",
    "13_effect_of_adding_outlier_on_range",
    "14_choosing_mean_vs_median_for_skewed_salary_data",
    "15_choosing_mode_for_commercial_inventory",
    "16_finding_missing_value_given_mean_and_n_minus_one_values",
    "17_finding_missing_value_given_range_and_extremes",
    "18_calculating_percentage_of_population_in_provincial_sample",
    "19_ranking_categories_from_tabular_summary",
    "20_calculating_actual_quantity_from_total_and_percentage",
    # 21 - 30
    "21_comparing_two_classes_by_mean_score",
    "22_comparing_two_athletes_by_range_consistency",
    "23_identifying_convenience_sampling_bias",
    "24_identifying_voluntary_response_bias",
    "25_critiquing_advertiser_sample_claim",
    "26_misleading_graph_truncated_vertical_axis",
    "27_misleading_pictograph_area_volume_distortion",
    "28_misleading_graph_irregular_time_intervals",
    "29_interpreting_line_graph_trend",
    "30_predicting_future_value_by_linear_extrapolation",
    # 31 - 40
    "31_interpolating_value_from_data_table",
    "32_two_way_contingency_table_gender_by_grade",
    "33_calculating_percentage_proportion_from_subgroup",
    "34_identifying_modal_class_interval_from_histogram",
    "35_estimating_mean_from_grouped_frequency_table",
    "36_distinguishing_correlation_from_causation",
    "37_impact_of_sample_size_on_reliability",
    "38_interpreting_pie_chart_sector_budget",
    "39_choosing_median_for_household_income",
    "40_writing_summary_statement_from_data_table",
    # 41 - 50
    "41_identifying_confounding_variable",
    "42_comparing_two_groups_spread_and_consistency",
    "43_percentage_increase_vs_percentage_point_difference",
    "44_evaluating_leading_question_bias",
    "45_evaluating_sampling_exclusion_bias",
    "46_interpreting_double_bar_chart_comparison",
    "47_interpreting_broken_line_temperature_graph",
    "48_calculating_median_from_stem_and_leaf_table",
    "49_calculating_combined_mean_of_two_classes",
    "50_synthesizing_data_for_policy_recommendation",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {}

for idx, b in enumerate(BUILDERS, start=1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

for name, b in zip(SUBSKILLS, BUILDERS):
    DISPATCH_TABLE[name] = b
    prefix = name.split("_")[0]
    DISPATCH_TABLE[prefix] = b
    short_slug = "_".join(name.split("_")[1:])
    DISPATCH_TABLE[short_slug] = b


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
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
        q.setdefault("topic", "Interpret analyse and report on data")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
