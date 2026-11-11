"""Data Handling Subskills Package (52 distinct archetypes).

Covers Grade 10 Mathematical Literacy Term 2 Topic:
1. Data handling cycle, collection & classification (Subskills 1 to 8)
2. Organising data & frequency tables (Subskills 9 to 16)
3. Measures of central tendency (Subskills 17 to 25)
4. Measures of spread & quartiles (Subskills 26 to 34)
5. Bar graphs, histograms & graphical displays (Subskills 35 to 43)
6. Pie charts & advanced data interpretation (Subskills 44 to 52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .collection_classification import (
    _gen_data_cycle_stages_sequence_identification,
    _gen_data_pop_vs_sample_identification,
    _gen_data_sample_bias_and_fairness_audit,
    _gen_data_collection_instruments_selection,
    _gen_data_questionnaire_design_leading_questions,
    _gen_data_classification_categorical_vs_numerical,
    _gen_data_classification_discrete_vs_continuous,
    _gen_data_ethics_privacy_and_consent,
)
from .organising_tables import (
    _gen_data_table_tally_marks_to_frequency_conversion,
    _gen_data_table_total_frequency_sum,
    _gen_data_table_relative_frequency_percentage,
    _gen_data_table_grouped_intervals_modal_class,
    _gen_data_table_stem_and_leaf_display_reading,
    _gen_data_table_two_way_contingency_joint_frequency,
    _gen_data_table_missing_frequency_reconstruction,
    _gen_data_table_cumulative_frequency_calculation,
)
from .central_tendency import (
    _gen_data_mean_raw_ungrouped_dataset,
    _gen_data_mean_frequency_table_weighted,
    _gen_data_median_odd_number_of_values,
    _gen_data_median_even_number_of_values,
    _gen_data_median_unsorted_list_ordering_step,
    _gen_data_mode_unimodal_raw_dataset,
    _gen_data_mode_bimodal_and_no_mode,
    _gen_data_modal_category_qualitative,
    _gen_data_mean_reconstructing_missing_test_score,
)
from .spread_quartiles import (
    _gen_data_range_calculation_max_minus_min,
    _gen_data_range_temperature_negative_integers,
    _gen_data_quartiles_lower_q1_calculation,
    _gen_data_quartiles_upper_q3_calculation,
    _gen_data_interquartile_range_iqr_calculation,
    _gen_data_semi_interquartile_range_calculation,
    _gen_data_outliers_impact_on_mean_vs_median,
    _gen_data_identifying_extreme_outliers,
    _gen_data_comparing_spread_between_two_groups,
)
from .bar_graphs_histograms import (
    _gen_data_graph_single_vertical_bar_reading,
    _gen_data_graph_compound_double_bar_comparison,
    _gen_data_graph_stacked_component_bar_breakdown,
    _gen_data_graph_histogram_continuous_class_intervals,
    _gen_data_graph_bar_vs_histogram_fundamental_differences,
    _gen_data_graph_line_graph_time_series_trend,
    _gen_data_graph_broken_axis_misleading_scale_audit,
    _gen_data_graph_frequency_polygon_midpoint_plotting,
    _gen_data_graph_percentage_increase_between_bars,
)
from .pie_charts_interpretation import (
    _gen_data_pie_sector_angle_from_percentage,
    _gen_data_pie_percentage_from_sector_degrees,
    _gen_data_pie_frequency_from_sector_angle,
    _gen_data_pie_total_dataset_from_sector_value,
    _gen_data_scatter_correlation_pattern_interpretation,
    _gen_data_scatter_line_of_best_fit_estimation,
    _gen_data_misleading_pie_chart_3d_perspective,
    _gen_data_stats_sa_census_demographics_interpretation,
    _gen_data_summary_statistics_measure_selection,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Cluster 1: Cycle, Collection & Classification (8)
    "data_cycle_stages_sequence_identification": _gen_data_cycle_stages_sequence_identification,
    "data_pop_vs_sample_identification": _gen_data_pop_vs_sample_identification,
    "data_sample_bias_and_fairness_audit": _gen_data_sample_bias_and_fairness_audit,
    "data_collection_instruments_selection": _gen_data_collection_instruments_selection,
    "data_questionnaire_design_leading_questions": _gen_data_questionnaire_design_leading_questions,
    "data_classification_categorical_vs_numerical": _gen_data_classification_categorical_vs_numerical,
    "data_classification_discrete_vs_continuous": _gen_data_classification_discrete_vs_continuous,
    "data_ethics_privacy_and_consent": _gen_data_ethics_privacy_and_consent,

    # Cluster 2: Organising Data & Tables (8)
    "data_table_tally_marks_to_frequency_conversion": _gen_data_table_tally_marks_to_frequency_conversion,
    "data_table_total_frequency_sum": _gen_data_table_total_frequency_sum,
    "data_table_relative_frequency_percentage": _gen_data_table_relative_frequency_percentage,
    "data_table_grouped_intervals_modal_class": _gen_data_table_grouped_intervals_modal_class,
    "data_table_stem_and_leaf_display_reading": _gen_data_table_stem_and_leaf_display_reading,
    "data_table_two_way_contingency_joint_frequency": _gen_data_table_two_way_contingency_joint_frequency,
    "data_table_missing_frequency_reconstruction": _gen_data_table_missing_frequency_reconstruction,
    "data_table_cumulative_frequency_calculation": _gen_data_table_cumulative_frequency_calculation,

    # Cluster 3: Central Tendency (9)
    "data_mean_raw_ungrouped_dataset": _gen_data_mean_raw_ungrouped_dataset,
    "data_mean_frequency_table_weighted": _gen_data_mean_frequency_table_weighted,
    "data_median_odd_number_of_values": _gen_data_median_odd_number_of_values,
    "data_median_even_number_of_values": _gen_data_median_even_number_of_values,
    "data_median_unsorted_list_ordering_step": _gen_data_median_unsorted_list_ordering_step,
    "data_mode_unimodal_raw_dataset": _gen_data_mode_unimodal_raw_dataset,
    "data_mode_bimodal_and_no_mode": _gen_data_mode_bimodal_and_no_mode,
    "data_modal_category_qualitative": _gen_data_modal_category_qualitative,
    "data_mean_reconstructing_missing_test_score": _gen_data_mean_reconstructing_missing_test_score,

    # Cluster 4: Spread & Quartiles (9)
    "data_range_calculation_max_minus_min": _gen_data_range_calculation_max_minus_min,
    "data_range_temperature_negative_integers": _gen_data_range_temperature_negative_integers,
    "data_quartiles_lower_q1_calculation": _gen_data_quartiles_lower_q1_calculation,
    "data_quartiles_upper_q3_calculation": _gen_data_quartiles_upper_q3_calculation,
    "data_interquartile_range_iqr_calculation": _gen_data_interquartile_range_iqr_calculation,
    "data_semi_interquartile_range_calculation": _gen_data_semi_interquartile_range_calculation,
    "data_outliers_impact_on_mean_vs_median": _gen_data_outliers_impact_on_mean_vs_median,
    "data_identifying_extreme_outliers": _gen_data_identifying_extreme_outliers,
    "data_comparing_spread_between_two_groups": _gen_data_comparing_spread_between_two_groups,

    # Cluster 5: Bar Graphs & Histograms (9)
    "data_graph_single_vertical_bar_reading": _gen_data_graph_single_vertical_bar_reading,
    "data_graph_compound_double_bar_comparison": _gen_data_graph_compound_double_bar_comparison,
    "data_graph_stacked_component_bar_breakdown": _gen_data_graph_stacked_component_bar_breakdown,
    "data_graph_histogram_continuous_class_intervals": _gen_data_graph_histogram_continuous_class_intervals,
    "data_graph_bar_vs_histogram_fundamental_differences": _gen_data_graph_bar_vs_histogram_fundamental_differences,
    "data_graph_line_graph_time_series_trend": _gen_data_graph_line_graph_time_series_trend,
    "data_graph_broken_axis_misleading_scale_audit": _gen_data_graph_broken_axis_misleading_scale_audit,
    "data_graph_frequency_polygon_midpoint_plotting": _gen_data_graph_frequency_polygon_midpoint_plotting,
    "data_graph_percentage_increase_between_bars": _gen_data_graph_percentage_increase_between_bars,

    # Cluster 6: Pie Charts & Advanced Interpretation (9)
    "data_pie_sector_angle_from_percentage": _gen_data_pie_sector_angle_from_percentage,
    "data_pie_percentage_from_sector_degrees": _gen_data_pie_percentage_from_sector_degrees,
    "data_pie_frequency_from_sector_angle": _gen_data_pie_frequency_from_sector_angle,
    "data_pie_total_dataset_from_sector_value": _gen_data_pie_total_dataset_from_sector_value,
    "data_scatter_correlation_pattern_interpretation": _gen_data_scatter_correlation_pattern_interpretation,
    "data_scatter_line_of_best_fit_estimation": _gen_data_scatter_line_of_best_fit_estimation,
    "data_misleading_pie_chart_3d_perspective": _gen_data_misleading_pie_chart_3d_perspective,
    "data_stats_sa_census_demographics_interpretation": _gen_data_stats_sa_census_demographics_interpretation,
    "data_summary_statistics_measure_selection": _gen_data_summary_statistics_measure_selection,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def generate(seed: Optional[int] = None, count: int = 1, subskill: Optional[str] = None) -> List[Dict[str, Any]]:
    """Generate questions for Data Handling."""
    r = random.Random(seed)
    questions = []

    for _ in range(count):
        if subskill and subskill in DISPATCH_TABLE:
            fn = DISPATCH_TABLE[subskill]
        else:
            chosen = r.choice(SUBSKILLS)
            fn = DISPATCH_TABLE[chosen]
        questions.append(fn(r))

    return questions
