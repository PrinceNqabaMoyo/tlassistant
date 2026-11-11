"""Grade 9 Mathematics - Interpret, Analyse and Report on Data Generator (50 Semantic Archetypes).
=============================================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 4 Topic: Interpret analyse and report on data
  - curriculum_docs_auto/Mathematics_Gr9/Term 4/
  - Sampling methods, representative vs biased samples (convenience, voluntary response, small n).
  - Questionnaire design: leading questions, loaded language.
  - Detecting misleading data presentations: truncated axes, non-uniform scales, 2D/3D pictogram distortions, omitted baselines.
  - Comparing data sets: mean, median, mode, range, consistency, impact of outliers, bimodal distributions.
  - Transformations of data: adding a constant, multiplying by a constant.
  - Drawing conclusions: correlation vs causation, confounding variables, extrapolation risks.
  - Formal reporting and synthesis of recommendations.

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .data_interpret_archetypes_01_25 import (
    arch_01_identify_sampling_bias_convenience_sample,
    arch_02_identify_sampling_bias_voluntary_response,
    arch_03_identify_sampling_bias_sample_size_too_small,
    arch_04_evaluate_leading_question_in_survey,
    arch_05_distinguish_between_population_and_sample,
    arch_06_detect_truncated_vertical_axis_in_bar_display,
    arch_07_calculate_actual_vs_visual_ratio_truncated_axis,
    arch_08_detect_non_uniform_axis_scaling,
    arch_09_detect_pictogram_area_volume_distortion,
    arch_10_detect_omitted_baseline_or_scale_distortion,
    arch_11_compare_two_groups_using_mean,
    arch_12_compare_two_groups_using_median,
    arch_13_compare_two_groups_using_range,
    arch_14_analyse_effect_of_high_outlier_on_mean,
    arch_15_analyse_effect_of_low_outlier_on_mean,
    arch_16_resistance_of_median_to_extreme_outliers,
    arch_17_choose_appropriate_measure_for_skewed_income,
    arch_18_choose_appropriate_measure_for_symmetric_test_scores,
    arch_19_determine_mode_importance_for_inventory_ordering,
    arch_20_critique_graph_with_missing_sample_size,
    arch_21_critique_claim_confusing_correlation_with_causation,
    arch_22_interpret_trend_and_predict_next_period,
    arch_23_compare_spread_consistency_between_two_athletes,
    arch_24_compare_pass_rates_between_two_classes,
    arch_25_identify_modal_category_from_survey_summary,
)
from .data_interpret_archetypes_26_50 import (
    arch_26_evaluate_representativeness_of_school_tuckshop_sample,
    arch_27_evaluate_representativeness_of_online_poll,
    arch_28_detect_suppression_of_negative_data_in_report,
    arch_29_calculate_percentage_increase_misleadingly_reported,
    arch_30_absolute_vs_relative_change_interpretation,
    arch_31_distinguish_between_continuous_trend_and_extrapolation_risk,
    arch_32_identify_confounding_variable_in_health_claim,
    arch_33_compare_bimodal_distribution_interpretations,
    arch_34_assess_impact_of_changing_class_intervals_on_histogram_shape,
    arch_35_compare_two_teams_performance_using_median_and_range,
    arch_36_evaluate_conclusion_drawn_from_biased_phone_survey,
    arch_37_identify_circular_reasoning_or_unsubstantiated_claim,
    arch_38_interpret_effect_of_doubling_sample_size_on_reliability,
    arch_39_critique_marketing_claim_based_on_9_out_of_10_dentists,
    arch_40_identify_omission_of_non_respondents_non_response_bias,
    arch_41_recalculate_mean_after_removing_data_entry_error,
    arch_42_recalculate_median_after_adding_new_learner_score,
    arch_43_determine_effect_on_mean_when_all_scores_increase_by_constant,
    arch_44_determine_effect_on_range_when_all_scores_increase_by_constant,
    arch_45_determine_effect_on_mean_when_all_scores_multiplied_by_factor,
    arch_46_compare_variability_between_two_weather_stations,
    arch_47_draw_reasoned_conclusion_from_customer_feedback_table,
    arch_48_recommend_policy_decision_based_on_bimodal_transport_survey,
    arch_49_summarise_key_findings_for_formal_statistical_report,
    arch_50_compound_multi_stage_data_interpretation_and_reporting_synthesis,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_identify_sampling_bias_convenience_sample": arch_01_identify_sampling_bias_convenience_sample,
    "02_identify_sampling_bias_voluntary_response": arch_02_identify_sampling_bias_voluntary_response,
    "03_identify_sampling_bias_sample_size_too_small": arch_03_identify_sampling_bias_sample_size_too_small,
    "04_evaluate_leading_question_in_survey": arch_04_evaluate_leading_question_in_survey,
    "05_distinguish_between_population_and_sample": arch_05_distinguish_between_population_and_sample,
    "06_detect_truncated_vertical_axis_in_bar_display": arch_06_detect_truncated_vertical_axis_in_bar_display,
    "07_calculate_actual_vs_visual_ratio_truncated_axis": arch_07_calculate_actual_vs_visual_ratio_truncated_axis,
    "08_detect_non_uniform_axis_scaling": arch_08_detect_non_uniform_axis_scaling,
    "09_detect_pictogram_area_volume_distortion": arch_09_detect_pictogram_area_volume_distortion,
    "10_detect_omitted_baseline_or_scale_distortion": arch_10_detect_omitted_baseline_or_scale_distortion,
    "11_compare_two_groups_using_mean": arch_11_compare_two_groups_using_mean,
    "12_compare_two_groups_using_median": arch_12_compare_two_groups_using_median,
    "13_compare_two_groups_using_range": arch_13_compare_two_groups_using_range,
    "14_analyse_effect_of_high_outlier_on_mean": arch_14_analyse_effect_of_high_outlier_on_mean,
    "15_analyse_effect_of_low_outlier_on_mean": arch_15_analyse_effect_of_low_outlier_on_mean,
    "16_resistance_of_median_to_extreme_outliers": arch_16_resistance_of_median_to_extreme_outliers,
    "17_choose_appropriate_measure_for_skewed_income": arch_17_choose_appropriate_measure_for_skewed_income,
    "18_choose_appropriate_measure_for_symmetric_test_scores": arch_18_choose_appropriate_measure_for_symmetric_test_scores,
    "19_determine_mode_importance_for_inventory_ordering": arch_19_determine_mode_importance_for_inventory_ordering,
    "20_critique_graph_with_missing_sample_size": arch_20_critique_graph_with_missing_sample_size,
    "21_critique_claim_confusing_correlation_with_causation": arch_21_critique_claim_confusing_correlation_with_causation,
    "22_interpret_trend_and_predict_next_period": arch_22_interpret_trend_and_predict_next_period,
    "23_compare_spread_consistency_between_two_athletes": arch_23_compare_spread_consistency_between_two_athletes,
    "24_compare_pass_rates_between_two_classes": arch_24_compare_pass_rates_between_two_classes,
    "25_identify_modal_category_from_survey_summary": arch_25_identify_modal_category_from_survey_summary,
    "26_evaluate_representativeness_of_school_tuckshop_sample": arch_26_evaluate_representativeness_of_school_tuckshop_sample,
    "27_evaluate_representativeness_of_online_poll": arch_27_evaluate_representativeness_of_online_poll,
    "28_detect_suppression_of_negative_data_in_report": arch_28_detect_suppression_of_negative_data_in_report,
    "29_calculate_percentage_increase_misleadingly_reported": arch_29_calculate_percentage_increase_misleadingly_reported,
    "30_absolute_vs_relative_change_interpretation": arch_30_absolute_vs_relative_change_interpretation,
    "31_distinguish_between_continuous_trend_and_extrapolation_risk": arch_31_distinguish_between_continuous_trend_and_extrapolation_risk,
    "32_identify_confounding_variable_in_health_claim": arch_32_identify_confounding_variable_in_health_claim,
    "33_compare_bimodal_distribution_interpretations": arch_33_compare_bimodal_distribution_interpretations,
    "34_assess_impact_of_changing_class_intervals_on_histogram_shape": arch_34_assess_impact_of_changing_class_intervals_on_histogram_shape,
    "35_compare_two_teams_performance_using_median_and_range": arch_35_compare_two_teams_performance_using_median_and_range,
    "36_evaluate_conclusion_drawn_from_biased_phone_survey": arch_36_evaluate_conclusion_drawn_from_biased_phone_survey,
    "37_identify_circular_reasoning_or_unsubstantiated_claim": arch_37_identify_circular_reasoning_or_unsubstantiated_claim,
    "38_interpret_effect_of_doubling_sample_size_on_reliability": arch_38_interpret_effect_of_doubling_sample_size_on_reliability,
    "39_critique_marketing_claim_based_on_9_out_of_10_dentists": arch_39_critique_marketing_claim_based_on_9_out_of_10_dentists,
    "40_identify_omission_of_non_respondents_non_response_bias": arch_40_identify_omission_of_non_respondents_non_response_bias,
    "41_recalculate_mean_after_removing_data_entry_error": arch_41_recalculate_mean_after_removing_data_entry_error,
    "42_recalculate_median_after_adding_new_learner_score": arch_42_recalculate_median_after_adding_new_learner_score,
    "43_determine_effect_on_mean_when_all_scores_increase_by_constant": arch_43_determine_effect_on_mean_when_all_scores_increase_by_constant,
    "44_determine_effect_on_range_when_all_scores_increase_by_constant": arch_44_determine_effect_on_range_when_all_scores_increase_by_constant,
    "45_determine_effect_on_mean_when_all_scores_multiplied_by_factor": arch_45_determine_effect_on_mean_when_all_scores_multiplied_by_factor,
    "46_compare_variability_between_two_weather_stations": arch_46_compare_variability_between_two_weather_stations,
    "47_draw_reasoned_conclusion_from_customer_feedback_table": arch_47_draw_reasoned_conclusion_from_customer_feedback_table,
    "48_recommend_policy_decision_based_on_bimodal_transport_survey": arch_48_recommend_policy_decision_based_on_bimodal_transport_survey,
    "49_summarise_key_findings_for_formal_statistical_report": arch_49_summarise_key_findings_for_formal_statistical_report,
    "50_compound_multi_stage_data_interpretation_and_reporting_synthesis": arch_50_compound_multi_stage_data_interpretation_and_reporting_synthesis,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate_grade9_data_interpret_question(
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
    q.setdefault("topic", "Interpret analyse and report on data")
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
        return generate_grade9_data_interpret_question(
            seed=seed, subskill=subskill, archetype_index=archetype_index, mode=mode, **kwargs
        )
    base_seed = seed if seed is not None else random.randint(100, 999999)
    out: List[Dict[str, Any]] = []
    for i in range(count):
        sub_seed = base_seed + i * 37
        sub = subskill if subskill else (SUBSKILLS[i % len(SUBSKILLS)] if archetype_index is None else None)
        out.append(
            generate_grade9_data_interpret_question(
                seed=sub_seed, subskill=sub, archetype_index=archetype_index, mode=mode, **kwargs
            )
        )
    return out
