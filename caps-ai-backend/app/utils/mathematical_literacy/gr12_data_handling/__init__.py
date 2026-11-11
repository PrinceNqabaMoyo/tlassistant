"""Grade 12 Mathematical Literacy — Data Handling Subskill Modules.
Subskills 01–52 dispatch registry and metadata.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict

from .sampling_survey_bias import (
    generate_01_stratified_sampling_proportions,
    generate_02_systematic_sampling_interval,
    generate_03_convenience_sampling_bias,
    generate_04_questionnaire_leading_question,
    generate_05_sample_size_margin_of_error,
    generate_06_variable_classification,
    generate_07_non_response_bias,
    generate_08_census_vs_sample_stats_sa,
)
from .grouped_data_ogives import (
    generate_09_class_interval_width,
    generate_10_class_midpoints_calculation,
    generate_11_estimated_mean_grouped_data,
    generate_12_modal_class_interval,
    generate_13_cumulative_frequency_table,
    generate_14_reading_median_from_ogive,
    generate_15_reading_quartiles_iqr_from_ogive,
    generate_16_ogive_benchmark_percentage,
)
from .central_tendency_outliers import (
    generate_17_weighted_combined_mean,
    generate_18_calculating_median_odd_even,
    generate_19_bimodal_multimodal_datasets,
    generate_20_outlier_impact_mean_vs_median,
    generate_21_selecting_appropriate_central_tendency,
    generate_22_missing_value_from_target_mean,
    generate_23_comparing_groups_equal_median,
    generate_24_linear_transformation_central_tendency,
)
from .quartiles_percentiles_spread import (
    generate_25_calculating_range_and_limitations,
    generate_26_quartiles_odd_dataset,
    generate_27_quartiles_even_dataset,
    generate_28_calculating_iqr,
    generate_29_semi_interquartile_range,
    generate_30_interpreting_percentile_ranks,
    generate_31_reading_growth_charts_percentiles,
    generate_32_position_of_kth_percentile,
)
from .boxplots_skewness_outliers import (
    generate_33_five_number_summary,
    generate_34_reading_box_and_whisker_plot,
    generate_35_positively_skewed_distribution,
    generate_36_negatively_skewed_distribution,
    generate_37_symmetrical_distribution,
    generate_38_outlier_detection_1_5_iqr,
    generate_39_comparing_two_boxplots,
    generate_40_outlier_removal_impact,
)
from .scatter_plots_correlation import (
    generate_41_interpreting_bivariate_points,
    generate_42_identifying_correlation_direction,
    generate_43_identifying_correlation_strength,
    generate_44_estimating_from_line_of_best_fit,
    generate_45_interpolation_vs_extrapolation,
    generate_46_correlation_vs_causation_fallacy,
)
from .opposing_arguments_misleading_stats import (
    generate_47_developing_opposing_arguments_tests,
    generate_48_misleading_graphs_truncated_axis,
    generate_49_misleading_graphs_inconsistent_intervals,
    generate_50_3d_pictogram_volume_distortion,
    generate_51_evaluating_opposing_viewpoints_census,
    generate_52_cherry_picking_selective_reporting,
)

SUBSKILL_LIST: list[tuple[str, str, Callable[[random.Random], Dict[str, Any]]]] = [
    ("01_stratified_sampling_proportions", "Stratified Sampling Proportions", generate_01_stratified_sampling_proportions),
    ("02_systematic_sampling_interval", "Systematic Sampling Interval", generate_02_systematic_sampling_interval),
    ("03_convenience_sampling_bias", "Convenience Sampling Bias", generate_03_convenience_sampling_bias),
    ("04_questionnaire_leading_question", "Questionnaire Leading Question Bias", generate_04_questionnaire_leading_question),
    ("05_sample_size_margin_of_error", "Sample Size Margin Of Error", generate_05_sample_size_margin_of_error),
    ("06_variable_classification", "Variable Classification Discrete Continuous", generate_06_variable_classification),
    ("07_non_response_bias", "Non-Response Bias Analysis", generate_07_non_response_bias),
    ("08_census_vs_sample_stats_sa", "Census Vs Sample Stats SA Context", generate_08_census_vs_sample_stats_sa),
    ("09_class_interval_width", "Class Interval Width And Boundaries", generate_09_class_interval_width),
    ("10_class_midpoints_calculation", "Class Midpoints Calculation", generate_10_class_midpoints_calculation),
    ("11_estimated_mean_grouped_data", "Estimated Mean Grouped Data", generate_11_estimated_mean_grouped_data),
    ("12_modal_class_interval", "Modal Class Interval Identification", generate_12_modal_class_interval),
    ("13_cumulative_frequency_table", "Cumulative Frequency Table Calculation", generate_13_cumulative_frequency_table),
    ("14_reading_median_from_ogive", "Reading Median From Ogive Curve", generate_14_reading_median_from_ogive),
    ("15_reading_quartiles_iqr_from_ogive", "Reading Quartiles IQR From Ogive", generate_15_reading_quartiles_iqr_from_ogive),
    ("16_ogive_benchmark_percentage", "Ogive Benchmark Percentage Calculation", generate_16_ogive_benchmark_percentage),
    ("17_weighted_combined_mean", "Weighted Combined Mean Two Classes", generate_17_weighted_combined_mean),
    ("18_calculating_median_odd_even", "Calculating Median Odd Even Datasets", generate_18_calculating_median_odd_even),
    ("19_bimodal_multimodal_datasets", "Bimodal Multimodal Datasets", generate_19_bimodal_multimodal_datasets),
    ("20_outlier_impact_mean_vs_median", "Outlier Impact Mean Vs Median", generate_20_outlier_impact_mean_vs_median),
    ("21_selecting_appropriate_central_tendency", "Selecting Appropriate Central Tendency", generate_21_selecting_appropriate_central_tendency),
    ("22_missing_value_from_target_mean", "Missing Value From Target Mean", generate_22_missing_value_from_target_mean),
    ("23_comparing_groups_equal_median", "Comparing Groups Equal Median", generate_23_comparing_groups_equal_median),
    ("24_linear_transformation_central_tendency", "Linear Transformation Central Tendency", generate_24_linear_transformation_central_tendency),
    ("25_calculating_range_and_limitations", "Calculating Range And Limitations", generate_25_calculating_range_and_limitations),
    ("26_quartiles_odd_dataset", "Quartiles Odd Dataset Calculation", generate_26_quartiles_odd_dataset),
    ("27_quartiles_even_dataset", "Quartiles Even Dataset Calculation", generate_27_quartiles_even_dataset),
    ("28_calculating_iqr", "Calculating Interquartile Range IQR", generate_28_calculating_iqr),
    ("29_semi_interquartile_range", "Semi-Interquartile Range Calculation", generate_29_semi_interquartile_range),
    ("30_interpreting_percentile_ranks", "Interpreting Percentile Ranks", generate_30_interpreting_percentile_ranks),
    ("31_reading_growth_charts_percentiles", "Reading Growth Charts Percentiles", generate_31_reading_growth_charts_percentiles),
    ("32_position_of_kth_percentile", "Position Of Kth Percentile Calculation", generate_32_position_of_kth_percentile),
    ("33_five_number_summary", "Five-Number Summary Extraction", generate_33_five_number_summary),
    ("34_reading_box_and_whisker_plot", "Reading Box And Whisker Plot", generate_34_reading_box_and_whisker_plot),
    ("35_positively_skewed_distribution", "Positively Skewed Distribution Analysis", generate_35_positively_skewed_distribution),
    ("36_negatively_skewed_distribution", "Negatively Skewed Distribution Analysis", generate_36_negatively_skewed_distribution),
    ("37_symmetrical_distribution", "Symmetrical Distribution Recognition", generate_37_symmetrical_distribution),
    ("38_outlier_detection_1_5_iqr", "Outlier Detection 1.5 x IQR Rule", generate_38_outlier_detection_1_5_iqr),
    ("39_comparing_two_boxplots", "Comparing Two Boxplots Consistency", generate_39_comparing_two_boxplots),
    ("40_outlier_removal_impact", "Outlier Removal Impact Summary", generate_40_outlier_removal_impact),
    ("41_interpreting_bivariate_points", "Interpreting Bivariate Points Coordinates", generate_41_interpreting_bivariate_points),
    ("42_identifying_correlation_direction", "Identifying Correlation Direction", generate_42_identifying_correlation_direction),
    ("43_identifying_correlation_strength", "Identifying Correlation Strength", generate_43_identifying_correlation_strength),
    ("44_estimating_from_line_of_best_fit", "Estimating From Line Of Best Fit", generate_44_estimating_from_line_of_best_fit),
    ("45_interpolation_vs_extrapolation", "Interpolation Vs Extrapolation Reliability", generate_45_interpolation_vs_extrapolation),
    ("46_correlation_vs_causation_fallacy", "Correlation Vs Causation Fallacy", generate_46_correlation_vs_causation_fallacy),
    ("47_developing_opposing_arguments_tests", "Developing Opposing Arguments Tests", generate_47_developing_opposing_arguments_tests),
    ("48_misleading_graphs_truncated_axis", "Misleading Graphs Truncated Axis", generate_48_misleading_graphs_truncated_axis),
    ("49_misleading_graphs_inconsistent_intervals", "Misleading Graphs Inconsistent Intervals", generate_49_misleading_graphs_inconsistent_intervals),
    ("50_3d_pictogram_volume_distortion", "3D Pictogram Volume Distortion", generate_50_3d_pictogram_volume_distortion),
    ("51_evaluating_opposing_viewpoints_census", "Evaluating Opposing Viewpoints Census", generate_51_evaluating_opposing_viewpoints_census),
    ("52_cherry_picking_selective_reporting", "Cherry-Picking Selective Reporting", generate_52_cherry_picking_selective_reporting),
]

SUBSKILL_DISPATCH: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
SUBSKILL_METADATA: Dict[str, Dict[str, str]] = {}

for idx, (subskill_key, name, fn) in enumerate(SUBSKILL_LIST, start=1):
    num_str = f"{idx:02d}"
    SUBSKILL_DISPATCH[subskill_key] = fn
    SUBSKILL_DISPATCH[num_str] = fn
    SUBSKILL_DISPATCH[str(idx)] = fn
    SUBSKILL_DISPATCH[f"gr12_data_{num_str}"] = fn

    SUBSKILL_METADATA[subskill_key] = {
        "index": num_str,
        "name": name,
        "topic": "grade12_mathlit_data_handling",
        "key": f"gr12_data_{num_str}",
    }


def generate_subskill(subskill: str | int, r: random.Random) -> Dict[str, Any]:
    """Generate a question for the requested subskill."""
    key = str(subskill).strip()
    fn = SUBSKILL_DISPATCH.get(key)
    if fn is None:
        # Fallback to random subskill
        fn = r.choice(list(SUBSKILL_DISPATCH.values()))
    return fn(r)
