"""Grade 9 Mathematics - Representing Data Generator (50 Semantic Archetypes).
=============================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 4 Topic: Representing data
  - curriculum_docs_auto/Mathematics_Gr9/Term 4/02. Representing data.md
  - Discrete vs continuous data, selecting appropriate graphs.
  - Bar graphs, double bar graphs, histograms (class intervals, modal class).
  - Pie charts (angles, percentages, frequencies).
  - Broken-line graphs (reading values, rate of change, trends).
  - Stem-and-leaf displays (key reading, median, range).
  - Scatter plots (independent/dependent variables, correlation, line of best fit, interpolation/extrapolation, outliers).
  - Misleading graphs (truncated axes, non-uniform scales, pictograms).
  - Compound multi-stage data representation synthesis.

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .data_represent_archetypes_01_25 import (
    arch_01_discrete_vs_continuous_data_identification,
    arch_02_select_appropriate_graph_for_data_type,
    arch_03_read_frequency_from_single_bar_graph,
    arch_04_identify_most_and_least_popular_category,
    arch_05_difference_in_frequency_between_two_bars,
    arch_06_total_sample_size_from_bar_chart,
    arch_07_calculate_percentage_of_category_from_bar_chart,
    arch_08_histogram_class_interval_identification,
    arch_09_histogram_modal_class_identification,
    arch_10_histogram_learners_above_threshold,
    arch_11_pie_chart_angle_calculation,
    arch_12_pie_chart_percentage_from_degrees,
    arch_13_determine_frequency_from_pie_chart_percentage_and_total,
    arch_14_determine_frequency_from_pie_chart_angle_and_total,
    arch_15_broken_line_graph_reading_value,
    arch_16_broken_line_graph_max_and_min,
    arch_17_broken_line_graph_rate_of_change,
    arch_18_misleading_graphs_truncated_vertical_axis,
    arch_19_misleading_graphs_non_uniform_scale,
    arch_20_stem_and_leaf_plot_key_reading,
    arch_21_reconstruct_data_from_stem_and_leaf,
    arch_22_finding_median_from_stem_and_leaf,
    arch_23_finding_range_from_stem_and_leaf,
    arch_24_double_bar_graph_comparison,
    arch_25_choosing_mean_vs_median_for_skewed_data,
)
from .data_represent_archetypes_26_50 import (
    arch_26_scatter_plot_independent_vs_dependent_variable,
    arch_27_scatter_plot_positive_correlation,
    arch_28_scatter_plot_negative_correlation,
    arch_29_scatter_plot_no_correlation,
    arch_30_scatter_plot_line_of_best_fit_purpose,
    arch_31_scatter_plot_prediction_using_line_of_best_fit,
    arch_32_interpolation_vs_extrapolation,
    arch_33_frequency_polygon_concept,
    arch_34_calculate_midpoint_of_class_interval,
    arch_35_cumulative_frequency_calculation,
    arch_36_double_bar_graph_combined_total,
    arch_37_pie_chart_unknown_slice_degrees,
    arch_38_pie_chart_unknown_slice_percentage,
    arch_39_interpreting_slope_of_broken_line_graph,
    arch_40_steepest_increase_on_broken_line_graph,
    arch_41_identifying_outliers_on_scatter_plot,
    arch_42_effect_of_outliers_on_mean_vs_median,
    arch_43_pictogram_misleading_representation,
    arch_44_histogram_total_count_from_intervals,
    arch_45_converting_table_to_pie_chart_fraction,
    arch_46_estimating_mean_from_grouped_frequency_histogram,
    arch_47_reading_interval_with_highest_frequency,
    arch_48_identifying_cluster_of_data_on_scatter_plot,
    arch_49_comparing_two_datasets_using_double_bar_graph_totals,
    arch_50_compound_multi_stage_data_representation_synthesis,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_discrete_vs_continuous_data_identification": arch_01_discrete_vs_continuous_data_identification,
    "02_select_appropriate_graph_for_data_type": arch_02_select_appropriate_graph_for_data_type,
    "03_read_frequency_from_single_bar_graph": arch_03_read_frequency_from_single_bar_graph,
    "04_identify_most_and_least_popular_category": arch_04_identify_most_and_least_popular_category,
    "05_difference_in_frequency_between_two_bars": arch_05_difference_in_frequency_between_two_bars,
    "06_total_sample_size_from_bar_chart": arch_06_total_sample_size_from_bar_chart,
    "07_calculate_percentage_of_category_from_bar_chart": arch_07_calculate_percentage_of_category_from_bar_chart,
    "08_histogram_class_interval_identification": arch_08_histogram_class_interval_identification,
    "09_histogram_modal_class_identification": arch_09_histogram_modal_class_identification,
    "10_histogram_learners_above_threshold": arch_10_histogram_learners_above_threshold,
    "11_pie_chart_angle_calculation": arch_11_pie_chart_angle_calculation,
    "12_pie_chart_percentage_from_degrees": arch_12_pie_chart_percentage_from_degrees,
    "13_determine_frequency_from_pie_chart_percentage_and_total": arch_13_determine_frequency_from_pie_chart_percentage_and_total,
    "14_determine_frequency_from_pie_chart_angle_and_total": arch_14_determine_frequency_from_pie_chart_angle_and_total,
    "15_broken_line_graph_reading_value": arch_15_broken_line_graph_reading_value,
    "16_broken_line_graph_max_and_min": arch_16_broken_line_graph_max_and_min,
    "17_broken_line_graph_rate_of_change": arch_17_broken_line_graph_rate_of_change,
    "18_misleading_graphs_truncated_vertical_axis": arch_18_misleading_graphs_truncated_vertical_axis,
    "19_misleading_graphs_non_uniform_scale": arch_19_misleading_graphs_non_uniform_scale,
    "20_stem_and_leaf_plot_key_reading": arch_20_stem_and_leaf_plot_key_reading,
    "21_reconstruct_data_from_stem_and_leaf": arch_21_reconstruct_data_from_stem_and_leaf,
    "22_finding_median_from_stem_and_leaf": arch_22_finding_median_from_stem_and_leaf,
    "23_finding_range_from_stem_and_leaf": arch_23_finding_range_from_stem_and_leaf,
    "24_double_bar_graph_comparison": arch_24_double_bar_graph_comparison,
    "25_choosing_mean_vs_median_for_skewed_data": arch_25_choosing_mean_vs_median_for_skewed_data,
    "26_scatter_plot_independent_vs_dependent_variable": arch_26_scatter_plot_independent_vs_dependent_variable,
    "27_scatter_plot_positive_correlation": arch_27_scatter_plot_positive_correlation,
    "28_scatter_plot_negative_correlation": arch_28_scatter_plot_negative_correlation,
    "29_scatter_plot_no_correlation": arch_29_scatter_plot_no_correlation,
    "30_scatter_plot_line_of_best_fit_purpose": arch_30_scatter_plot_line_of_best_fit_purpose,
    "31_scatter_plot_prediction_using_line_of_best_fit": arch_31_scatter_plot_prediction_using_line_of_best_fit,
    "32_interpolation_vs_extrapolation": arch_32_interpolation_vs_extrapolation,
    "33_frequency_polygon_concept": arch_33_frequency_polygon_concept,
    "34_calculate_midpoint_of_class_interval": arch_34_calculate_midpoint_of_class_interval,
    "35_cumulative_frequency_calculation": arch_35_cumulative_frequency_calculation,
    "36_double_bar_graph_combined_total": arch_36_double_bar_graph_combined_total,
    "37_pie_chart_unknown_slice_degrees": arch_37_pie_chart_unknown_slice_degrees,
    "38_pie_chart_unknown_slice_percentage": arch_38_pie_chart_unknown_slice_percentage,
    "39_interpreting_slope_of_broken_line_graph": arch_39_interpreting_slope_of_broken_line_graph,
    "40_steepest_increase_on_broken_line_graph": arch_40_steepest_increase_on_broken_line_graph,
    "41_identifying_outliers_on_scatter_plot": arch_41_identifying_outliers_on_scatter_plot,
    "42_effect_of_outliers_on_mean_vs_median": arch_42_effect_of_outliers_on_mean_vs_median,
    "43_pictogram_misleading_representation": arch_43_pictogram_misleading_representation,
    "44_histogram_total_count_from_intervals": arch_44_histogram_total_count_from_intervals,
    "45_converting_table_to_pie_chart_fraction": arch_45_converting_table_to_pie_chart_fraction,
    "46_estimating_mean_from_grouped_frequency_histogram": arch_46_estimating_mean_from_grouped_frequency_histogram,
    "47_reading_interval_with_highest_frequency": arch_47_reading_interval_with_highest_frequency,
    "48_identifying_cluster_of_data_on_scatter_plot": arch_48_identifying_cluster_of_data_on_scatter_plot,
    "49_comparing_two_datasets_using_double_bar_graph_totals": arch_49_comparing_two_datasets_using_double_bar_graph_totals,
    "50_compound_multi_stage_data_representation_synthesis": arch_50_compound_multi_stage_data_representation_synthesis,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate_grade9_data_represent_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)

    selected_subskill = subskill
    if not selected_subskill or selected_subskill not in DISPATCH_TABLE:
        if archetype_index is not None and 0 <= archetype_index < len(SUBSKILLS):
            selected_subskill = SUBSKILLS[archetype_index]
        elif mode.startswith("elementary_"):
            target_stem = mode.replace("elementary_", "")
            candidates = [s for s in SUBSKILLS if target_stem in s]
            selected_subskill = candidates[0] if candidates else r.choice(SUBSKILLS)
        else:
            selected_subskill = r.choice(SUBSKILLS)

    builder = DISPATCH_TABLE[selected_subskill]
    q = builder(r)

    # 6-Pillar Metadata Enforcements
    q.setdefault("topic", "Representing data")
    q.setdefault("subject", "Mathematics")
    q.setdefault("grade", "9")
    q.setdefault("term", 4)
    q.setdefault("caps_weight_percent", 5.0)
    q.setdefault("suggested_duration_mins", 3)
    q.setdefault("difficulty", "medium")
    q.setdefault("subskill", selected_subskill)
    q.setdefault("archetype", selected_subskill)
    q.setdefault("interactive", False)

    return q


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    mode: str = "compound",
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]] | Dict[str, Any]:
    if count == 1:
        return generate_grade9_data_represent_question(
            seed=seed, subskill=subskill, archetype_index=archetype_index, mode=mode, **kwargs
        )
    base_seed = seed if seed is not None else random.randint(100, 999999)
    out: List[Dict[str, Any]] = []
    for i in range(count):
        sub_seed = base_seed + i * 37
        sub = subskill if subskill else (SUBSKILLS[i % len(SUBSKILLS)] if archetype_index is None else None)
        out.append(
            generate_grade9_data_represent_question(
                seed=sub_seed, subskill=sub, archetype_index=archetype_index, mode=mode, **kwargs
            )
        )
    return out
