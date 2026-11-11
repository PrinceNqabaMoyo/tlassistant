"""
Grade 8 Mathematics - Numeric and Geometric Patterns Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/04. Numeric and geometric patterns.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .patterns_archetypes_01_25 import (
    arch_01_arithmetic_sequence_next_three_terms_positive_diff,
    arch_02_arithmetic_sequence_next_three_terms_negative_diff,
    arch_03_arithmetic_sequence_decimal_terms,
    arch_04_arithmetic_sequence_fractional_terms,
    arch_05_arithmetic_sequence_missing_intermediate_term,
    arch_06_arithmetic_sequence_missing_multiple_terms,
    arch_07_geometric_sequence_doubling_tripling_next_terms,
    arch_08_geometric_sequence_fractional_ratio_decay,
    arch_09_geometric_sequence_powers_of_ten,
    arch_10_sequence_classification_constant_diff_vs_ratio,
    arch_11_triangular_numbers_sequence_extension,
    arch_12_square_numbers_sequence_extension,
    arch_13_cubic_numbers_sequence_extension,
    arch_14_second_difference_quadratic_pattern_identification,
    arch_15_fibonacci_type_additive_sequence,
    arch_16_verbal_rule_to_numeric_sequence_generation,
    arch_17_flow_diagram_input_to_output_calculation,
    arch_18_flow_diagram_output_to_input_inverse_operation,
    arch_19_flow_diagram_determining_missing_operator_rule,
    arch_20_table_of_values_linear_constant_difference_rule,
    arch_21_general_term_formula_derivation_linear_simple,
    arch_22_general_term_formula_derivation_linear_with_constant,
    arch_23_general_term_formula_negative_common_difference,
    arch_24_calculate_far_term_value_using_linear_rule_t20_t50,
    arch_25_calculate_position_n_given_term_value,
)

from .patterns_archetypes_26_50 import (
    arch_26_verify_whether_number_belongs_to_linear_sequence,
    arch_27_matchstick_squares_in_row_diagram_formula,
    arch_28_matchstick_triangles_in_row_diagram_formula,
    arch_29_matchstick_hexagons_in_row_diagram_formula,
    arch_30_matchstick_fences_or_posts_diagram_formula,
    arch_31_dot_pattern_triangular_arrangement_diagram,
    arch_32_dot_pattern_square_grid_diagram,
    arch_33_dot_pattern_l_shape_diagram,
    arch_34_dot_pattern_cross_plus_diagram,
    arch_35_tile_pattern_border_around_square_diagram,
    arch_36_tile_pattern_two_color_ratio_progression,
    arch_37_perimeter_of_joined_unit_squares_in_row_diagram,
    arch_38_perimeter_of_joined_equilateral_triangles_diagram,
    arch_39_matchstick_count_for_specific_large_figure_number,
    arch_40_figure_number_from_total_matchsticks_budget,
    arch_41_parking_fee_or_taxi_fare_linear_pattern_context,
    arch_42_cellphone_call_cost_fixed_plus_per_minute_pattern,
    arch_43_water_tank_draining_or_filling_rate_pattern,
    arch_44_savings_account_constant_weekly_deposit_pattern,
    arch_45_comparing_two_growth_patterns_break_even_stage,
    arch_46_geometric_sequence_general_term_powers_of_two,
    arch_47_geometric_sequence_general_term_powers_of_three,
    arch_48_quadratic_pattern_shifted_squares_general_formula,
    arch_49_cubic_pattern_shifted_cubes_general_formula,
    arch_50_pattern_representation_translation_table_rule_graph,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10
    arch_01_arithmetic_sequence_next_three_terms_positive_diff,
    arch_02_arithmetic_sequence_next_three_terms_negative_diff,
    arch_03_arithmetic_sequence_decimal_terms,
    arch_04_arithmetic_sequence_fractional_terms,
    arch_05_arithmetic_sequence_missing_intermediate_term,
    arch_06_arithmetic_sequence_missing_multiple_terms,
    arch_07_geometric_sequence_doubling_tripling_next_terms,
    arch_08_geometric_sequence_fractional_ratio_decay,
    arch_09_geometric_sequence_powers_of_ten,
    arch_10_sequence_classification_constant_diff_vs_ratio,
    # 11 - 20
    arch_11_triangular_numbers_sequence_extension,
    arch_12_square_numbers_sequence_extension,
    arch_13_cubic_numbers_sequence_extension,
    arch_14_second_difference_quadratic_pattern_identification,
    arch_15_fibonacci_type_additive_sequence,
    arch_16_verbal_rule_to_numeric_sequence_generation,
    arch_17_flow_diagram_input_to_output_calculation,
    arch_18_flow_diagram_output_to_input_inverse_operation,
    arch_19_flow_diagram_determining_missing_operator_rule,
    arch_20_table_of_values_linear_constant_difference_rule,
    # 21 - 28
    arch_21_general_term_formula_derivation_linear_simple,
    arch_22_general_term_formula_derivation_linear_with_constant,
    arch_23_general_term_formula_negative_common_difference,
    arch_24_calculate_far_term_value_using_linear_rule_t20_t50,
    arch_25_calculate_position_n_given_term_value,
    arch_26_verify_whether_number_belongs_to_linear_sequence,
    arch_27_matchstick_squares_in_row_diagram_formula,
    arch_28_matchstick_triangles_in_row_diagram_formula,
    # 29 - 36
    arch_29_matchstick_hexagons_in_row_diagram_formula,
    arch_30_matchstick_fences_or_posts_diagram_formula,
    arch_31_dot_pattern_triangular_arrangement_diagram,
    arch_32_dot_pattern_square_grid_diagram,
    arch_33_dot_pattern_l_shape_diagram,
    arch_34_dot_pattern_cross_plus_diagram,
    arch_35_tile_pattern_border_around_square_diagram,
    arch_36_tile_pattern_two_color_ratio_progression,
    # 37 - 44
    arch_37_perimeter_of_joined_unit_squares_in_row_diagram,
    arch_38_perimeter_of_joined_equilateral_triangles_diagram,
    arch_39_matchstick_count_for_specific_large_figure_number,
    arch_40_figure_number_from_total_matchsticks_budget,
    arch_41_parking_fee_or_taxi_fare_linear_pattern_context,
    arch_42_cellphone_call_cost_fixed_plus_per_minute_pattern,
    arch_43_water_tank_draining_or_filling_rate_pattern,
    arch_44_savings_account_constant_weekly_deposit_pattern,
    # 45 - 50
    arch_45_comparing_two_growth_patterns_break_even_stage,
    arch_46_geometric_sequence_general_term_powers_of_two,
    arch_47_geometric_sequence_general_term_powers_of_three,
    arch_48_quadratic_pattern_shifted_squares_general_formula,
    arch_49_cubic_pattern_shifted_cubes_general_formula,
    arch_50_pattern_representation_translation_table_rule_graph,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_arithmetic_sequence_next_three_terms_positive_diff",
    "02_arithmetic_sequence_next_three_terms_negative_diff",
    "03_arithmetic_sequence_decimal_terms",
    "04_arithmetic_sequence_fractional_terms",
    "05_arithmetic_sequence_missing_intermediate_term",
    "06_arithmetic_sequence_missing_multiple_terms",
    "07_geometric_sequence_doubling_tripling_next_terms",
    "08_geometric_sequence_fractional_ratio_decay",
    "09_geometric_sequence_powers_of_ten",
    "10_sequence_classification_constant_diff_vs_ratio",
    # 11 - 20
    "11_triangular_numbers_sequence_extension",
    "12_square_numbers_sequence_extension",
    "13_cubic_numbers_sequence_extension",
    "14_second_difference_quadratic_pattern_identification",
    "15_fibonacci_type_additive_sequence",
    "16_verbal_rule_to_numeric_sequence_generation",
    "17_flow_diagram_input_to_output_calculation",
    "18_flow_diagram_output_to_input_inverse_operation",
    "19_flow_diagram_determining_missing_operator_rule",
    "20_table_of_values_linear_constant_difference_rule",
    # 21 - 28
    "21_general_term_formula_derivation_linear_simple",
    "22_general_term_formula_derivation_linear_with_constant",
    "23_general_term_formula_negative_common_difference",
    "24_calculate_far_term_value_using_linear_rule_t20_t50",
    "25_calculate_position_n_given_term_value",
    "26_verify_whether_number_belongs_to_linear_sequence",
    "27_matchstick_squares_in_row_diagram_formula",
    "28_matchstick_triangles_in_row_diagram_formula",
    # 29 - 36
    "29_matchstick_hexagons_in_row_diagram_formula",
    "30_matchstick_fences_or_posts_diagram_formula",
    "31_dot_pattern_triangular_arrangement_diagram",
    "32_dot_pattern_square_grid_diagram",
    "33_dot_pattern_l_shape_diagram",
    "34_dot_pattern_cross_plus_diagram",
    "35_tile_pattern_border_around_square_diagram",
    "36_tile_pattern_two_color_ratio_progression",
    # 37 - 44
    "37_perimeter_of_joined_unit_squares_in_row_diagram",
    "38_perimeter_of_joined_equilateral_triangles_diagram",
    "39_matchstick_count_for_specific_large_figure_number",
    "40_figure_number_from_total_matchsticks_budget",
    "41_parking_fee_or_taxi_fare_linear_pattern_context",
    "42_cellphone_call_cost_fixed_plus_per_minute_pattern",
    "43_water_tank_draining_or_filling_rate_pattern",
    "44_savings_account_constant_weekly_deposit_pattern",
    # 45 - 50
    "45_comparing_two_growth_patterns_break_even_stage",
    "46_geometric_sequence_general_term_powers_of_two",
    "47_geometric_sequence_general_term_powers_of_three",
    "48_quadratic_pattern_shifted_squares_general_formula",
    "49_cubic_pattern_shifted_cubes_general_formula",
    "50_pattern_representation_translation_table_rule_graph",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases
DISPATCH_TABLE["arithmetic"] = arch_01_arithmetic_sequence_next_three_terms_positive_diff
DISPATCH_TABLE["geometric"] = arch_07_geometric_sequence_doubling_tripling_next_terms
DISPATCH_TABLE["general_term"] = arch_22_general_term_formula_derivation_linear_with_constant
DISPATCH_TABLE["matchstick"] = arch_27_matchstick_squares_in_row_diagram_formula
DISPATCH_TABLE["flow_diagram"] = arch_17_flow_diagram_input_to_output_calculation


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
        q.setdefault("topic", "Numeric and geometric patterns")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
