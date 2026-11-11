"""Grade 7 Mathematics - Numeric Patterns Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/05. Numeric patterns.md
Focus: Ascending & descending sequences, negative extensions, geometric patterns, square/cubic/triangular numbers, general rules Tn = dn + c, sequence tables, matchstick & dot SVG figures, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .numeric_patterns_archetypes_01_25 import (
    arch_01_extending_linear_ascending_sequence,
    arch_02_extending_linear_descending_sequence,
    arch_03_extending_sequence_backwards_into_negative,
    arch_04_constant_difference_calculation,
    arch_05_constant_difference_descending,
    arch_06_identify_next_three_terms_fractional_step,
    arch_07_identify_next_three_terms_decimal_step,
    arch_08_geometric_doubling_sequence,
    arch_09_geometric_tripling_sequence,
    arch_10_geometric_halving_sequence,
    arch_11_geometric_dividing_by_ten_powers,
    arch_12_square_numbers_sequence,
    arch_13_cubic_numbers_sequence,
    arch_14_triangular_numbers_sequence,
    arch_15_fibonacci_sequence_addition_rule,
    arch_16_general_rule_verbal_description,
    arch_17_formula_from_numeric_rule,
    arch_18_general_formula_negative_constant,
    arch_19_general_formula_descending_negative_difference,
    arch_20_calculate_10th_term_using_rule,
    arch_21_calculate_20th_term_using_rule,
    arch_22_calculate_50th_term_using_rule,
    arch_23_calculate_100th_term_using_rule,
    arch_24_find_term_position_numeric,
    arch_25_find_term_position_large_target,
)
from .numeric_patterns_archetypes_26_50 import (
    arch_26_sequence_table_missing_output,
    arch_27_sequence_table_missing_input,
    arch_28_missing_values_in_sequence_table,
    arch_29_determine_if_number_belongs_to_sequence,
    arch_30_matchstick_squares_pattern_svg,
    arch_31_matchstick_triangles_pattern_svg,
    arch_32_matchstick_hexagons_pattern_svg,
    arch_33_dot_array_triangular_pattern_svg,
    arch_34_dot_array_square_pattern_svg,
    arch_35_word_problem_savings_pattern,
    arch_36_word_problem_stadium_seating_rows,
    arch_37_word_problem_tree_growth_pattern,
    arch_38_word_problem_bacterial_growth_doubling,
    arch_39_flow_diagram_to_pattern,
    arch_40_two_different_sequences_same_first_term,
    arch_41_alternating_sign_pattern,
    arch_42_second_order_difference_quadratic_pattern,
    arch_43_arithmetic_vs_geometric_classification,
    arch_44_common_misconception_confusing_term_and_position,
    arch_45_common_misconception_extending_by_first_difference_only,
    arch_46_common_misconception_multiplying_instead_of_adding_in_formula,
    arch_47_finding_missing_intermediate_term,
    arch_48_finding_two_missing_intermediate_terms,
    arch_49_sum_of_first_n_terms_observation,
    arch_50_numeric_patterns_comprehensive_diagnostic_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_extending_linear_ascending_sequence": arch_01_extending_linear_ascending_sequence,
    "02_extending_linear_descending_sequence": arch_02_extending_linear_descending_sequence,
    "03_extending_sequence_backwards_into_negative": arch_03_extending_sequence_backwards_into_negative,
    "04_constant_difference_calculation": arch_04_constant_difference_calculation,
    "05_constant_difference_descending": arch_05_constant_difference_descending,
    "06_identify_next_three_terms_fractional_step": arch_06_identify_next_three_terms_fractional_step,
    "07_identify_next_three_terms_decimal_step": arch_07_identify_next_three_terms_decimal_step,
    "08_geometric_doubling_sequence": arch_08_geometric_doubling_sequence,
    "09_geometric_tripling_sequence": arch_09_geometric_tripling_sequence,
    "10_geometric_halving_sequence": arch_10_geometric_halving_sequence,
    "11_geometric_dividing_by_ten_powers": arch_11_geometric_dividing_by_ten_powers,
    "12_square_numbers_sequence": arch_12_square_numbers_sequence,
    "13_cubic_numbers_sequence": arch_13_cubic_numbers_sequence,
    "14_triangular_numbers_sequence": arch_14_triangular_numbers_sequence,
    "15_fibonacci_sequence_addition_rule": arch_15_fibonacci_sequence_addition_rule,
    "16_general_rule_verbal_description": arch_16_general_rule_verbal_description,
    "17_formula_from_numeric_rule": arch_17_formula_from_numeric_rule,
    "18_general_formula_negative_constant": arch_18_general_formula_negative_constant,
    "19_general_formula_descending_negative_difference": arch_19_general_formula_descending_negative_difference,
    "20_calculate_10th_term_using_rule": arch_20_calculate_10th_term_using_rule,
    "21_calculate_20th_term_using_rule": arch_21_calculate_20th_term_using_rule,
    "22_calculate_50th_term_using_rule": arch_22_calculate_50th_term_using_rule,
    "23_calculate_100th_term_using_rule": arch_23_calculate_100th_term_using_rule,
    "24_find_term_position_numeric": arch_24_find_term_position_numeric,
    "25_find_term_position_large_target": arch_25_find_term_position_large_target,
    "26_sequence_table_missing_output": arch_26_sequence_table_missing_output,
    "27_sequence_table_missing_input": arch_27_sequence_table_missing_input,
    "28_missing_values_in_sequence_table": arch_28_missing_values_in_sequence_table,
    "29_determine_if_number_belongs_to_sequence": arch_29_determine_if_number_belongs_to_sequence,
    "30_matchstick_squares_pattern_svg": arch_30_matchstick_squares_pattern_svg,
    "31_matchstick_triangles_pattern_svg": arch_31_matchstick_triangles_pattern_svg,
    "32_matchstick_hexagons_pattern_svg": arch_32_matchstick_hexagons_pattern_svg,
    "33_dot_array_triangular_pattern_svg": arch_33_dot_array_triangular_pattern_svg,
    "34_dot_array_square_pattern_svg": arch_34_dot_array_square_pattern_svg,
    "35_word_problem_savings_pattern": arch_35_word_problem_savings_pattern,
    "36_word_problem_stadium_seating_rows": arch_36_word_problem_stadium_seating_rows,
    "37_word_problem_tree_growth_pattern": arch_37_word_problem_tree_growth_pattern,
    "38_word_problem_bacterial_growth_doubling": arch_38_word_problem_bacterial_growth_doubling,
    "39_flow_diagram_to_pattern": arch_39_flow_diagram_to_pattern,
    "40_two_different_sequences_same_first_term": arch_40_two_different_sequences_same_first_term,
    "41_alternating_sign_pattern": arch_41_alternating_sign_pattern,
    "42_second_order_difference_quadratic_pattern": arch_42_second_order_difference_quadratic_pattern,
    "43_arithmetic_vs_geometric_classification": arch_43_arithmetic_vs_geometric_classification,
    "44_common_misconception_confusing_term_and_position": arch_44_common_misconception_confusing_term_and_position,
    "45_common_misconception_extending_by_first_difference_only": arch_45_common_misconception_extending_by_first_difference_only,
    "46_common_misconception_multiplying_instead_of_adding_in_formula": arch_46_common_misconception_multiplying_instead_of_adding_in_formula,
    "47_finding_missing_intermediate_term": arch_47_finding_missing_intermediate_term,
    "48_finding_two_missing_intermediate_terms": arch_48_finding_two_missing_intermediate_terms,
    "49_sum_of_first_n_terms_observation": arch_49_sum_of_first_n_terms_observation,
    "50_numeric_patterns_comprehensive_diagnostic_autopsy": arch_50_numeric_patterns_comprehensive_diagnostic_autopsy,
}

SUBSKILLS = list(ARCHETYPE_BUILDERS.keys())


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed) if seed is not None else random.Random()
    if subskill is None or subskill not in ARCHETYPE_BUILDERS:
        subskill = rng.choice(SUBSKILLS)
    builder = ARCHETYPE_BUILDERS[subskill]
    return builder(rng)


generate = generate_question
