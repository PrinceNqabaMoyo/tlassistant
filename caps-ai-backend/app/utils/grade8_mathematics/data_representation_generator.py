"""
Grade 8 Mathematics - Represent Data Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/03. Represent data.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .represent_data_archetypes_01_25 import (
    arch_01_bar_graph_reading_category_frequency,
    arch_02_bar_graph_identifying_highest_or_lowest_category,
    arch_03_bar_graph_calculating_difference_between_categories,
    arch_04_bar_graph_calculating_total_sample_frequency,
    arch_05_bar_graph_calculating_percentage_for_category,
    arch_06_bar_graph_features_axes_labels_and_scales,
    arch_07_bar_graph_why_bars_have_equal_spaces,
    arch_08_bar_graph_identifying_mode_category,
    arch_09_bar_graph_frequency_ratio_comparison,
    arch_10_bar_graph_data_ordering_category_ranking,
    arch_11_double_bar_graph_reading_comparative_values,
    arch_12_double_bar_graph_identifying_largest_gap,
    arch_13_double_bar_graph_calculating_overall_total_both_groups,
    arch_14_double_bar_graph_purpose_of_legend,
    arch_15_double_bar_graph_category_comparison_ratio,
    arch_16_double_bar_graph_determining_which_group_has_higher_overall_sum,
    arch_17_double_bar_graph_trend_comparison_across_grades,
    arch_18_double_bar_graph_interpreting_percentage_scales,
    arch_19_double_bar_graph_identifying_category_where_group_b_exceeds_group_a,
    arch_20_double_bar_graph_constructing_comparison_table_from_bars,
    arch_21_histogram_reading_interval_frequency,
    arch_22_histogram_why_bars_touch_no_spaces,
    arch_23_histogram_identifying_modal_class_interval,
    arch_24_histogram_calculating_total_sample_size,
    arch_25_histogram_counting_values_above_or_below_interval_threshold,
)

from .represent_data_archetypes_26_50 import (
    arch_26_histogram_percentage_of_learners_in_interval,
    arch_27_histogram_determining_class_width_from_axis,
    arch_28_histogram_vs_bar_graph_distinction,
    arch_29_histogram_identifying_least_frequent_interval,
    arch_30_histogram_estimating_median_interval,
    arch_31_pie_chart_calculating_sector_angle_from_fraction,
    arch_32_pie_chart_calculating_sector_angle_from_percentage,
    arch_33_pie_chart_calculating_frequency_from_sector_angle,
    arch_34_pie_chart_calculating_frequency_from_percentage,
    arch_35_pie_chart_reading_proportions_from_svg_diagram,
    arch_36_pie_chart_sum_of_angles_in_full_circle,
    arch_37_pie_chart_half_circle_and_quarter_circle_angles,
    arch_38_pie_chart_calculating_missing_sector_angle,
    arch_39_pie_chart_calculating_missing_sector_percentage,
    arch_40_pie_chart_converting_fraction_of_day_to_sector_angle,
    arch_41_broken_line_graph_reading_temperature_over_time,
    arch_42_broken_line_graph_identifying_steepest_rise_or_fall,
    arch_43_broken_line_graph_calculating_overall_change,
    arch_44_broken_line_graph_why_dots_are_connected_by_lines,
    arch_45_comparing_two_series_on_broken_line_graph,
    arch_46_graph_suitability_when_to_use_pie_chart,
    arch_47_graph_suitability_when_to_use_broken_line_graph,
    arch_48_graph_suitability_when_to_use_bar_graph,
    arch_49_graph_suitability_when_to_use_histogram,
    arch_50_misleading_graphs_identifying_truncated_vertical_axis,
)


BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10
    arch_01_bar_graph_reading_category_frequency,
    arch_02_bar_graph_identifying_highest_or_lowest_category,
    arch_03_bar_graph_calculating_difference_between_categories,
    arch_04_bar_graph_calculating_total_sample_frequency,
    arch_05_bar_graph_calculating_percentage_for_category,
    arch_06_bar_graph_features_axes_labels_and_scales,
    arch_07_bar_graph_why_bars_have_equal_spaces,
    arch_08_bar_graph_identifying_mode_category,
    arch_09_bar_graph_frequency_ratio_comparison,
    arch_10_bar_graph_data_ordering_category_ranking,
    # 11 - 20
    arch_11_double_bar_graph_reading_comparative_values,
    arch_12_double_bar_graph_identifying_largest_gap,
    arch_13_double_bar_graph_calculating_overall_total_both_groups,
    arch_14_double_bar_graph_purpose_of_legend,
    arch_15_double_bar_graph_category_comparison_ratio,
    arch_16_double_bar_graph_determining_which_group_has_higher_overall_sum,
    arch_17_double_bar_graph_trend_comparison_across_grades,
    arch_18_double_bar_graph_interpreting_percentage_scales,
    arch_19_double_bar_graph_identifying_category_where_group_b_exceeds_group_a,
    arch_20_double_bar_graph_constructing_comparison_table_from_bars,
    # 21 - 28
    arch_21_histogram_reading_interval_frequency,
    arch_22_histogram_why_bars_touch_no_spaces,
    arch_23_histogram_identifying_modal_class_interval,
    arch_24_histogram_calculating_total_sample_size,
    arch_25_histogram_counting_values_above_or_below_interval_threshold,
    arch_26_histogram_percentage_of_learners_in_interval,
    arch_27_histogram_determining_class_width_from_axis,
    arch_28_histogram_vs_bar_graph_distinction,
    # 29 - 36
    arch_29_histogram_identifying_least_frequent_interval,
    arch_30_histogram_estimating_median_interval,
    arch_31_pie_chart_calculating_sector_angle_from_fraction,
    arch_32_pie_chart_calculating_sector_angle_from_percentage,
    arch_33_pie_chart_calculating_frequency_from_sector_angle,
    arch_34_pie_chart_calculating_frequency_from_percentage,
    arch_35_pie_chart_reading_proportions_from_svg_diagram,
    arch_36_pie_chart_sum_of_angles_in_full_circle,
    # 37 - 44
    arch_37_pie_chart_half_circle_and_quarter_circle_angles,
    arch_38_pie_chart_calculating_missing_sector_angle,
    arch_39_pie_chart_calculating_missing_sector_percentage,
    arch_40_pie_chart_converting_fraction_of_day_to_sector_angle,
    arch_41_broken_line_graph_reading_temperature_over_time,
    arch_42_broken_line_graph_identifying_steepest_rise_or_fall,
    arch_43_broken_line_graph_calculating_overall_change,
    arch_44_broken_line_graph_why_dots_are_connected_by_lines,
    # 45 - 50
    arch_45_comparing_two_series_on_broken_line_graph,
    arch_46_graph_suitability_when_to_use_pie_chart,
    arch_47_graph_suitability_when_to_use_broken_line_graph,
    arch_48_graph_suitability_when_to_use_bar_graph,
    arch_49_graph_suitability_when_to_use_histogram,
    arch_50_misleading_graphs_identifying_truncated_vertical_axis,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_bar_graph_reading_category_frequency",
    "02_bar_graph_identifying_highest_or_lowest_category",
    "03_bar_graph_calculating_difference_between_categories",
    "04_bar_graph_calculating_total_sample_frequency",
    "05_bar_graph_calculating_percentage_for_category",
    "06_bar_graph_features_axes_labels_and_scales",
    "07_bar_graph_why_bars_have_equal_spaces",
    "08_bar_graph_identifying_mode_category",
    "09_bar_graph_frequency_ratio_comparison",
    "10_bar_graph_data_ordering_category_ranking",
    # 11 - 20
    "11_double_bar_graph_reading_comparative_values",
    "12_double_bar_graph_identifying_largest_gap",
    "13_double_bar_graph_calculating_overall_total_both_groups",
    "14_double_bar_graph_purpose_of_legend",
    "15_double_bar_graph_category_comparison_ratio",
    "16_double_bar_graph_determining_which_group_has_higher_overall_sum",
    "17_double_bar_graph_trend_comparison_across_grades",
    "18_double_bar_graph_interpreting_percentage_scales",
    "19_double_bar_graph_identifying_category_where_group_b_exceeds_group_a",
    "20_double_bar_graph_constructing_comparison_table_from_bars",
    # 21 - 28
    "21_histogram_reading_interval_frequency",
    "22_histogram_why_bars_touch_no_spaces",
    "23_histogram_identifying_modal_class_interval",
    "24_histogram_calculating_total_sample_size",
    "25_histogram_counting_values_above_or_below_interval_threshold",
    "26_histogram_percentage_of_learners_in_interval",
    "27_histogram_determining_class_width_from_axis",
    "28_histogram_vs_bar_graph_distinction",
    # 29 - 36
    "29_histogram_identifying_least_frequent_interval",
    "30_histogram_estimating_median_interval",
    "31_pie_chart_calculating_sector_angle_from_fraction",
    "32_pie_chart_calculating_sector_angle_from_percentage",
    "33_pie_chart_calculating_frequency_from_sector_angle",
    "34_pie_chart_calculating_frequency_from_percentage",
    "35_pie_chart_reading_proportions_from_svg_diagram",
    "36_pie_chart_sum_of_angles_in_full_circle",
    # 37 - 44
    "37_pie_chart_half_circle_and_quarter_circle_angles",
    "38_pie_chart_calculating_missing_sector_angle",
    "39_pie_chart_calculating_missing_sector_percentage",
    "40_pie_chart_converting_fraction_of_day_to_sector_angle",
    "41_broken_line_graph_reading_temperature_over_time",
    "42_broken_line_graph_identifying_steepest_rise_or_fall",
    "43_broken_line_graph_calculating_overall_change",
    "44_broken_line_graph_why_dots_are_connected_by_lines",
    # 45 - 50
    "45_comparing_two_series_on_broken_line_graph",
    "46_graph_suitability_when_to_use_pie_chart",
    "47_graph_suitability_when_to_use_broken_line_graph",
    "48_graph_suitability_when_to_use_bar_graph",
    "49_graph_suitability_when_to_use_histogram",
    "50_misleading_graphs_identifying_truncated_vertical_axis",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases
DISPATCH_TABLE["histogram_continuous_construction"] = arch_21_histogram_reading_interval_frequency
DISPATCH_TABLE["double_bar_graph_comparison"] = arch_11_double_bar_graph_reading_comparative_values
DISPATCH_TABLE["pie_chart_angle_calculation"] = arch_31_pie_chart_calculating_sector_angle_from_fraction
DISPATCH_TABLE["broken_line_graph_trends"] = arch_41_broken_line_graph_reading_temperature_over_time
DISPATCH_TABLE["graph_format_suitability"] = arch_46_graph_suitability_when_to_use_pie_chart


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
        q.setdefault("topic", "Represent data")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
