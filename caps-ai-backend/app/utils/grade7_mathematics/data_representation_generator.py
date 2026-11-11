"""
Grade 7 Mathematics - Represent Data Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/02. Represent data.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .data_representation_archetypes_01_25 import (
    arch_01_read_bar_height_single_category,
    arch_02_identify_modal_category,
    arch_03_total_frequency_across_all_bars,
    arch_04_difference_between_two_bars,
    arch_05_fraction_or_percentage_of_category,
    arch_06_horizontal_bar_graph_interpretation,
    arch_07_estimating_intermediate_scale_values,
    arch_08_categories_exceeding_threshold,
    arch_09_read_double_bar_single_subgroup,
    arch_10_compare_two_subgroups_within_category,
    arch_11_category_with_greatest_difference,
    arch_12_identify_subgroup_exceeding_another,
    arch_13_overall_subgroup_total,
    arch_14_compare_overall_totals_two_subgroups,
    arch_15_percentage_double_bar_graph,
    arch_16_equal_representation_in_double_bar,
    arch_17_distinguish_histogram_from_bar_graph,
    arch_18_read_histogram_interval_frequency,
    arch_19_identify_modal_class_histogram,
    arch_20_total_sample_size_from_histogram,
    arch_21_observations_above_or_below_threshold_histogram,
    arch_22_interval_width_and_boundaries,
    arch_23_percentage_of_learners_in_interval,
    arch_24_comparing_non_adjacent_intervals,
    arch_25_identifying_zero_frequency_intervals,
)

from .data_representation_archetypes_26_50 import (
    arch_26_read_simple_fraction_pie_chart,
    arch_27_calculate_quantity_from_sector_percentage,
    arch_28_find_missing_sector_percentage,
    arch_29_reverse_total_from_known_sector,
    arch_30_compare_two_sectors_on_pie_chart,
    arch_31_identify_largest_sector_mode,
    arch_32_simplest_fraction_for_sector,
    arch_33_budget_allocation_pie_chart,
    arch_34_convert_percentage_to_degrees,
    arch_35_sector_angle_for_simple_fractions,
    arch_36_sector_angle_from_frequency_and_total,
    arch_37_remaining_sector_degrees,
    arch_38_verify_sector_angles_sum_to_360,
    arch_39_frequency_from_known_angle,
    arch_40_match_frequency_table_to_pie_chart,
    arch_41_compare_pie_charts_different_sample_sizes,
    arch_42_three_sector_preference_poll,
    arch_43_choose_graph_for_discrete_categories,
    arch_44_choose_graph_for_continuous_data,
    arch_45_choose_graph_for_proportions_of_whole,
    arch_46_choose_graph_for_trends_over_time,
    arch_47_misleading_graph_truncated_vertical_axis,
    arch_48_misleading_graph_unequal_bar_widths,
    arch_49_misleading_3d_perspective_distortion,
    arch_50_tabular_summary_to_bar_graph_conversion,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 08: Single Bar Graph Reading & Interpretation
    arch_01_read_bar_height_single_category,
    arch_02_identify_modal_category,
    arch_03_total_frequency_across_all_bars,
    arch_04_difference_between_two_bars,
    arch_05_fraction_or_percentage_of_category,
    arch_06_horizontal_bar_graph_interpretation,
    arch_07_estimating_intermediate_scale_values,
    arch_08_categories_exceeding_threshold,
    # 09 - 16: Double Bar Graph Comparison
    arch_09_read_double_bar_single_subgroup,
    arch_10_compare_two_subgroups_within_category,
    arch_11_category_with_greatest_difference,
    arch_12_identify_subgroup_exceeding_another,
    arch_13_overall_subgroup_total,
    arch_14_compare_overall_totals_two_subgroups,
    arch_15_percentage_double_bar_graph,
    arch_16_equal_representation_in_double_bar,
    # 17 - 25: Histograms & Continuous Intervals
    arch_17_distinguish_histogram_from_bar_graph,
    arch_18_read_histogram_interval_frequency,
    arch_19_identify_modal_class_histogram,
    arch_20_total_sample_size_from_histogram,
    arch_21_observations_above_or_below_threshold_histogram,
    arch_22_interval_width_and_boundaries,
    arch_23_percentage_of_learners_in_interval,
    arch_24_comparing_non_adjacent_intervals,
    arch_25_identifying_zero_frequency_intervals,
    # 26 - 34: Pie Chart Interpretation & Quantities
    arch_26_read_simple_fraction_pie_chart,
    arch_27_calculate_quantity_from_sector_percentage,
    arch_28_find_missing_sector_percentage,
    arch_29_reverse_total_from_known_sector,
    arch_30_compare_two_sectors_on_pie_chart,
    arch_31_identify_largest_sector_mode,
    arch_32_simplest_fraction_for_sector,
    arch_33_budget_allocation_pie_chart,
    arch_34_convert_percentage_to_degrees,
    # 35 - 42: Angles and Pie Chart Construction
    arch_35_sector_angle_for_simple_fractions,
    arch_36_sector_angle_from_frequency_and_total,
    arch_37_remaining_sector_degrees,
    arch_38_verify_sector_angles_sum_to_360,
    arch_39_frequency_from_known_angle,
    arch_40_match_frequency_table_to_pie_chart,
    arch_41_compare_pie_charts_different_sample_sizes,
    arch_42_three_sector_preference_poll,
    # 43 - 50: Graph Selection & Misleading Graphs Critique
    arch_43_choose_graph_for_discrete_categories,
    arch_44_choose_graph_for_continuous_data,
    arch_45_choose_graph_for_proportions_of_whole,
    arch_46_choose_graph_for_trends_over_time,
    arch_47_misleading_graph_truncated_vertical_axis,
    arch_48_misleading_graph_unequal_bar_widths,
    arch_49_misleading_3d_perspective_distortion,
    arch_50_tabular_summary_to_bar_graph_conversion,
]

SUBSKILLS: List[str] = [
    # 01 - 08
    "01_read_bar_height_single_category",
    "02_identify_modal_category",
    "03_total_frequency_across_all_bars",
    "04_difference_between_two_bars",
    "05_fraction_or_percentage_of_category",
    "06_horizontal_bar_graph_interpretation",
    "07_estimating_intermediate_scale_values",
    "08_categories_exceeding_threshold",
    # 09 - 16
    "09_read_double_bar_single_subgroup",
    "10_compare_two_subgroups_within_category",
    "11_category_with_greatest_difference",
    "12_identify_subgroup_exceeding_another",
    "13_overall_subgroup_total",
    "14_compare_overall_totals_two_subgroups",
    "15_percentage_double_bar_graph",
    "16_equal_representation_in_double_bar",
    # 17 - 25
    "17_distinguish_histogram_from_bar_graph",
    "18_read_histogram_interval_frequency",
    "19_identify_modal_class_histogram",
    "20_total_sample_size_from_histogram",
    "21_observations_above_or_below_threshold_histogram",
    "22_interval_width_and_boundaries",
    "23_percentage_of_learners_in_interval",
    "24_comparing_non_adjacent_intervals",
    "25_identifying_zero_frequency_intervals",
    # 26 - 34
    "26_read_simple_fraction_pie_chart",
    "27_calculate_quantity_from_sector_percentage",
    "28_find_missing_sector_percentage",
    "29_reverse_total_from_known_sector",
    "30_compare_two_sectors_on_pie_chart",
    "31_identify_largest_sector_mode",
    "32_simplest_fraction_for_sector",
    "33_budget_allocation_pie_chart",
    "34_convert_percentage_to_degrees",
    # 35 - 42
    "35_sector_angle_for_simple_fractions",
    "36_sector_angle_from_frequency_and_total",
    "37_remaining_sector_degrees",
    "38_verify_sector_angles_sum_to_360",
    "39_frequency_from_known_angle",
    "40_match_frequency_table_to_pie_chart",
    "41_compare_pie_charts_different_sample_sizes",
    "42_three_sector_preference_poll",
    # 43 - 50
    "43_choose_graph_for_discrete_categories",
    "44_choose_graph_for_continuous_data",
    "45_choose_graph_for_proportions_of_whole",
    "46_choose_graph_for_trends_over_time",
    "47_misleading_graph_truncated_vertical_axis",
    "48_misleading_graph_unequal_bar_widths",
    "49_misleading_3d_perspective_distortion",
    "50_tabular_summary_to_bar_graph_conversion",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["bar_graph_construction"] = arch_01_read_bar_height_single_category
DISPATCH_TABLE["double_bar_graph_comparison"] = arch_10_compare_two_subgroups_within_category
DISPATCH_TABLE["pie_chart_percentages"] = arch_27_calculate_quantity_from_sector_percentage
DISPATCH_TABLE["histogram_interpretation"] = arch_18_read_histogram_interval_frequency
DISPATCH_TABLE["frequency_polygon_trend"] = arch_46_choose_graph_for_trends_over_time


def get_subskills() -> List[str]:
    """Returns the list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Represent Data Generator.
    Supports exact archetype dispatch via subskill or archetype_index, and compound mode.
    """
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
        q.setdefault("grade", 7)
        q.setdefault("subject", "Mathematics")
        q.setdefault("topic", "Represent data")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
