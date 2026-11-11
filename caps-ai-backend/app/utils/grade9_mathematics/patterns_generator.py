"""Grade 9 Mathematics - Patterns, Sequences & Representations Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 1/04. Patterns.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .patterns_archetypes_01_25 import (
    arch_01_linear_sequence_constant_difference_positive,
    arch_02_linear_sequence_constant_difference_negative,
    arch_03_linear_sequence_calculate_specific_term_t10_t50,
    arch_04_linear_sequence_find_term_position_given_value,
    arch_05_linear_sequence_fractional_terms_common_difference,
    arch_06_linear_sequence_decimal_terms_step,
    arch_07_matchstick_square_pattern_formula_derivation,
    arch_08_matchstick_triangle_pattern_formula_derivation,
    arch_09_matchstick_pattern_total_sticks_for_stage_k,
    arch_10_matchstick_pattern_determine_stage_from_total_sticks,
    arch_11_tile_paving_border_pattern_formula,
    arch_12_geometric_sequence_constant_ratio_integer,
    arch_13_geometric_sequence_constant_ratio_fractional,
    arch_14_geometric_sequence_alternating_signs,
    arch_15_geometric_sequence_find_kth_term,
    arch_16_square_numbers_sequence,
    arch_17_cube_numbers_sequence,
    arch_18_triangular_numbers_sequence,
    arch_19_quadratic_sequence_second_difference_constant,
    arch_20_quadratic_sequence_find_specific_term,
    arch_21_fibonacci_type_additive_sequence,
    arch_22_table_representation_complete_missing_outputs,
    arch_23_table_representation_find_rule_from_input_output_table,
    arch_24_flow_diagram_input_rule_output_representation,
    arch_25_inverse_flow_diagram_find_input_from_output,
)
from .patterns_archetypes_26_50 import (
    arch_26_inverse_proportion_constant_product_rule,
    arch_27_inverse_proportion_workers_and_days_problem,
    arch_28_inverse_proportion_speed_and_travel_time_problem,
    arch_29_inverse_proportion_graphical_hyperbola_interpretation,
    arch_30_direct_proportion_constant_ratio_unit_rate,
    arch_31_distinguish_direct_vs_inverse_proportion_from_tables,
    arch_32_contextual_cellphone_plan_cost_pattern,
    arch_33_contextual_taxi_fare_linear_pattern,
    arch_34_contextual_savings_plan_arithmetic_growth,
    arch_35_contextual_water_tank_depletion_linear_decay,
    arch_36_linear_graph_story_matching_distance_time,
    arch_37_linear_pattern_is_number_a_member_of_sequence,
    arch_38_two_sequences_find_common_term_and_position,
    arch_39_sequence_with_alternating_addition_and_subtraction,
    arch_40_sequence_fractions_linear_numerator_and_denominator,
    arch_41_nested_bracket_pattern_expansion,
    arch_42_geometric_pattern_hexagonal_perimeter_growth,
    arch_43_geometric_pattern_dot_grid_growth,
    arch_44_contextual_tiered_staircase_block_pattern,
    arch_45_seating_arrangement_tables_and_chairs,
    arch_46_fence_posts_and_planks_pattern,
    arch_47_error_analysis_diagnosing_difference_vs_coefficient_confusion,
    arch_48_error_analysis_diagnosing_zeroth_term_omission,
    arch_49_error_analysis_diagnosing_proportionality_assumption_on_affine,
    arch_50_compound_multi_step_pattern_investigation_challenge,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_linear_sequence_constant_difference_positive": arch_01_linear_sequence_constant_difference_positive,
    "02_linear_sequence_constant_difference_negative": arch_02_linear_sequence_constant_difference_negative,
    "03_linear_sequence_calculate_specific_term_t10_t50": arch_03_linear_sequence_calculate_specific_term_t10_t50,
    "04_linear_sequence_find_term_position_given_value": arch_04_linear_sequence_find_term_position_given_value,
    "05_linear_sequence_fractional_terms_common_difference": arch_05_linear_sequence_fractional_terms_common_difference,
    "06_linear_sequence_decimal_terms_step": arch_06_linear_sequence_decimal_terms_step,
    "07_matchstick_square_pattern_formula_derivation": arch_07_matchstick_square_pattern_formula_derivation,
    "08_matchstick_triangle_pattern_formula_derivation": arch_08_matchstick_triangle_pattern_formula_derivation,
    "09_matchstick_pattern_total_sticks_for_stage_k": arch_09_matchstick_pattern_total_sticks_for_stage_k,
    "10_matchstick_pattern_determine_stage_from_total_sticks": arch_10_matchstick_pattern_determine_stage_from_total_sticks,
    "11_tile_paving_border_pattern_formula": arch_11_tile_paving_border_pattern_formula,
    "12_geometric_sequence_constant_ratio_integer": arch_12_geometric_sequence_constant_ratio_integer,
    "13_geometric_sequence_constant_ratio_fractional": arch_13_geometric_sequence_constant_ratio_fractional,
    "14_geometric_sequence_alternating_signs": arch_14_geometric_sequence_alternating_signs,
    "15_geometric_sequence_find_kth_term": arch_15_geometric_sequence_find_kth_term,
    "16_square_numbers_sequence": arch_16_square_numbers_sequence,
    "17_cube_numbers_sequence": arch_17_cube_numbers_sequence,
    "18_triangular_numbers_sequence": arch_18_triangular_numbers_sequence,
    "19_quadratic_sequence_second_difference_constant": arch_19_quadratic_sequence_second_difference_constant,
    "20_quadratic_sequence_find_specific_term": arch_20_quadratic_sequence_find_specific_term,
    "21_fibonacci_type_additive_sequence": arch_21_fibonacci_type_additive_sequence,
    "22_table_representation_complete_missing_outputs": arch_22_table_representation_complete_missing_outputs,
    "23_table_representation_find_rule_from_input_output_table": arch_23_table_representation_find_rule_from_input_output_table,
    "24_flow_diagram_input_rule_output_representation": arch_24_flow_diagram_input_rule_output_representation,
    "25_inverse_flow_diagram_find_input_from_output": arch_25_inverse_flow_diagram_find_input_from_output,
    "26_inverse_proportion_constant_product_rule": arch_26_inverse_proportion_constant_product_rule,
    "27_inverse_proportion_workers_and_days_problem": arch_27_inverse_proportion_workers_and_days_problem,
    "28_inverse_proportion_speed_and_travel_time_problem": arch_28_inverse_proportion_speed_and_travel_time_problem,
    "29_inverse_proportion_graphical_hyperbola_interpretation": arch_29_inverse_proportion_graphical_hyperbola_interpretation,
    "30_direct_proportion_constant_ratio_unit_rate": arch_30_direct_proportion_constant_ratio_unit_rate,
    "31_distinguish_direct_vs_inverse_proportion_from_tables": arch_31_distinguish_direct_vs_inverse_proportion_from_tables,
    "32_contextual_cellphone_plan_cost_pattern": arch_32_contextual_cellphone_plan_cost_pattern,
    "33_contextual_taxi_fare_linear_pattern": arch_33_contextual_taxi_fare_linear_pattern,
    "34_contextual_savings_plan_arithmetic_growth": arch_34_contextual_savings_plan_arithmetic_growth,
    "35_contextual_water_tank_depletion_linear_decay": arch_35_contextual_water_tank_depletion_linear_decay,
    "36_linear_graph_story_matching_distance_time": arch_36_linear_graph_story_matching_distance_time,
    "37_linear_pattern_is_number_a_member_of_sequence": arch_37_linear_pattern_is_number_a_member_of_sequence,
    "38_two_sequences_find_common_term_and_position": arch_38_two_sequences_find_common_term_and_position,
    "39_sequence_with_alternating_addition_and_subtraction": arch_39_sequence_with_alternating_addition_and_subtraction,
    "40_sequence_fractions_linear_numerator_and_denominator": arch_40_sequence_fractions_linear_numerator_and_denominator,
    "41_nested_bracket_pattern_expansion": arch_41_nested_bracket_pattern_expansion,
    "42_geometric_pattern_hexagonal_perimeter_growth": arch_42_geometric_pattern_hexagonal_perimeter_growth,
    "43_geometric_pattern_dot_grid_growth": arch_43_geometric_pattern_dot_grid_growth,
    "44_contextual_tiered_staircase_block_pattern": arch_44_contextual_tiered_staircase_block_pattern,
    "45_seating_arrangement_tables_and_chairs": arch_45_seating_arrangement_tables_and_chairs,
    "46_fence_posts_and_planks_pattern": arch_46_fence_posts_and_planks_pattern,
    "47_error_analysis_diagnosing_difference_vs_coefficient_confusion": arch_47_error_analysis_diagnosing_difference_vs_coefficient_confusion,
    "48_error_analysis_diagnosing_zeroth_term_omission": arch_48_error_analysis_diagnosing_zeroth_term_omission,
    "49_error_analysis_diagnosing_proportionality_assumption_on_affine": arch_49_error_analysis_diagnosing_proportionality_assumption_on_affine,
    "50_compound_multi_step_pattern_investigation_challenge": arch_50_compound_multi_step_pattern_investigation_challenge,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_patterns_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Patterns question."""
    r = random.Random(seed)
    if subskill and subskill in ARCHETYPE_MAP:
        builder = ARCHETYPE_MAP[subskill]
        chosen_subskill = subskill
    else:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(r)
    q["subskill"] = chosen_subskill
    q["grade"] = "9"
    q["subject"] = "Mathematics"
    q["topic"] = "Patterns"
    q["term"] = 1
    return q


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """6-Pillar Generator Contract entry point."""
    r = random.Random(seed)
    questions: List[Dict[str, Any]] = []

    if subskill and subskill in ARCHETYPE_MAP:
        candidates = [subskill]
    else:
        candidates = SUBSKILLS

    for i in range(count):
        sub = candidates[i % len(candidates)] if len(candidates) > 1 else candidates[0]
        sub_seed = r.randint(1, 1_000_000_000)
        q = generate_grade9_patterns_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
