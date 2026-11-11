"""
Grade 7 Mathematics - Numeric and Geometric Patterns Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/03. Numeric and geometric patterns.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .patterns_archetypes_01_25 import (
    arch_01_constant_difference_identification,
    arch_02_extend_increasing_arithmetic_sequence,
    arch_03_extend_decreasing_arithmetic_sequence,
    arch_04_missing_term_inside_sequence,
    arch_05_verbal_rule_arithmetic_sequence,
    arch_06_distinguish_constant_difference,
    arch_07_input_output_table_linear,
    arch_08_flow_diagram_rule_evaluation,
    arch_09_doubling_geometric_sequence,
    arch_10_tripling_geometric_sequence,
    arch_11_square_numbers_sequence,
    arch_12_cube_numbers_sequence,
    arch_13_triangular_numbers_sequence,
    arch_14_fibonacci_sequence_concept,
    arch_15_alternating_operations_sequence,
    arch_16_classify_sequence_relationship,
    arch_17_matchstick_squares_chain,
    arch_18_matchstick_triangles_chain,
    arch_19_matchstick_pentagons_chain,
    arch_20_matchstick_hexagons_chain,
    arch_21_separate_independent_squares,
    arch_22_separate_independent_triangles,
    arch_23_matchstick_letter_h_pattern,
    arch_24_matchstick_letter_e_pattern,
    arch_25_inverse_matchstick_problem,
)

from .patterns_archetypes_26_50 import (
    arch_26_square_dot_arrays,
    arch_27_rectangular_dot_arrays,
    arch_28_l_shaped_dot_patterns,
    arch_29_border_tiles_around_square_pool,
    arch_30_t_shaped_tile_patterns,
    arch_31_plus_shaped_tile_patterns,
    arch_32_triangular_dot_pattern_formation,
    arch_33_hexagonal_honeycomb_pattern,
    arch_34_inverse_tile_problem,
    arch_35_deriving_linear_formula_tn,
    arch_36_calculate_twentieth_term,
    arch_37_calculate_fiftieth_term,
    arch_38_calculate_hundredth_term,
    arch_39_solve_for_position_n,
    arch_40_is_number_a_term_in_sequence,
    arch_41_compare_two_growing_patterns,
    arch_42_differences_of_square_numbers,
    arch_43_restaurant_tables_in_a_row,
    arch_44_separate_tables_seating,
    arch_45_hexagonal_tables_in_a_line,
    arch_46_fence_posts_and_rails,
    arch_47_savings_linear_pattern,
    arch_48_stacking_cans_triangular_display,
    arch_49_cellular_division_powers_of_two,
    arch_50_flawed_rule_diagnosis,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 08: Arithmetic Sequences & Constant Difference
    arch_01_constant_difference_identification,
    arch_02_extend_increasing_arithmetic_sequence,
    arch_03_extend_decreasing_arithmetic_sequence,
    arch_04_missing_term_inside_sequence,
    arch_05_verbal_rule_arithmetic_sequence,
    arch_06_distinguish_constant_difference,
    arch_07_input_output_table_linear,
    arch_08_flow_diagram_rule_evaluation,
    # 09 - 16: Geometric & Special Sequences
    arch_09_doubling_geometric_sequence,
    arch_10_tripling_geometric_sequence,
    arch_11_square_numbers_sequence,
    arch_12_cube_numbers_sequence,
    arch_13_triangular_numbers_sequence,
    arch_14_fibonacci_sequence_concept,
    arch_15_alternating_operations_sequence,
    arch_16_classify_sequence_relationship,
    # 17 - 25: Matchstick Chains
    arch_17_matchstick_squares_chain,
    arch_18_matchstick_triangles_chain,
    arch_19_matchstick_pentagons_chain,
    arch_20_matchstick_hexagons_chain,
    arch_21_separate_independent_squares,
    arch_22_separate_independent_triangles,
    arch_23_matchstick_letter_h_pattern,
    arch_24_matchstick_letter_e_pattern,
    arch_25_inverse_matchstick_problem,
    # 26 - 34: Tile, Dot and Grid Arrays
    arch_26_square_dot_arrays,
    arch_27_rectangular_dot_arrays,
    arch_28_l_shaped_dot_patterns,
    arch_29_border_tiles_around_square_pool,
    arch_30_t_shaped_tile_patterns,
    arch_31_plus_shaped_tile_patterns,
    arch_32_triangular_dot_pattern_formation,
    arch_33_hexagonal_honeycomb_pattern,
    arch_34_inverse_tile_problem,
    # 35 - 42: General Formula & Large Term Calculation
    arch_35_deriving_linear_formula_tn,
    arch_36_calculate_twentieth_term,
    arch_37_calculate_fiftieth_term,
    arch_38_calculate_hundredth_term,
    arch_39_solve_for_position_n,
    arch_40_is_number_a_term_in_sequence,
    arch_41_compare_two_growing_patterns,
    arch_42_differences_of_square_numbers,
    # 43 - 50: Tables, Seating and Practical Contexts
    arch_43_restaurant_tables_in_a_row,
    arch_44_separate_tables_seating,
    arch_45_hexagonal_tables_in_a_line,
    arch_46_fence_posts_and_rails,
    arch_47_savings_linear_pattern,
    arch_48_stacking_cans_triangular_display,
    arch_49_cellular_division_powers_of_two,
    arch_50_flawed_rule_diagnosis,
]

SUBSKILLS: List[str] = [
    # 01 - 08
    "01_constant_difference_identification",
    "02_extend_increasing_arithmetic_sequence",
    "03_extend_decreasing_arithmetic_sequence",
    "04_missing_term_inside_sequence",
    "05_verbal_rule_arithmetic_sequence",
    "06_distinguish_constant_difference",
    "07_input_output_table_linear",
    "08_flow_diagram_rule_evaluation",
    # 09 - 16
    "09_doubling_geometric_sequence",
    "10_tripling_geometric_sequence",
    "11_square_numbers_sequence",
    "12_cube_numbers_sequence",
    "13_triangular_numbers_sequence",
    "14_fibonacci_sequence_concept",
    "15_alternating_operations_sequence",
    "16_classify_sequence_relationship",
    # 17 - 25
    "17_matchstick_squares_chain",
    "18_matchstick_triangles_chain",
    "19_matchstick_pentagons_chain",
    "20_matchstick_hexagons_chain",
    "21_separate_independent_squares",
    "22_separate_independent_triangles",
    "23_matchstick_letter_h_pattern",
    "24_matchstick_letter_e_pattern",
    "25_inverse_matchstick_problem",
    # 26 - 34
    "26_square_dot_arrays",
    "27_rectangular_dot_arrays",
    "28_l_shaped_dot_patterns",
    "29_border_tiles_around_square_pool",
    "30_t_shaped_tile_patterns",
    "31_plus_shaped_tile_patterns",
    "32_triangular_dot_pattern_formation",
    "33_hexagonal_honeycomb_pattern",
    "34_inverse_tile_problem",
    # 35 - 42
    "35_deriving_linear_formula_tn",
    "36_calculate_twentieth_term",
    "37_calculate_fiftieth_term",
    "38_calculate_hundredth_term",
    "39_solve_for_position_n",
    "40_is_number_a_term_in_sequence",
    "41_compare_two_growing_patterns",
    "42_differences_of_square_numbers",
    # 43 - 50
    "43_restaurant_tables_in_a_row",
    "44_separate_tables_seating",
    "45_hexagonal_tables_in_a_line",
    "46_fence_posts_and_rails",
    "47_savings_linear_pattern",
    "48_stacking_cans_triangular_display",
    "49_cellular_division_powers_of_two",
    "50_flawed_rule_diagnosis",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["geometric_matchstick_squares"] = arch_17_matchstick_squares_chain
DISPATCH_TABLE["geometric_matchstick_triangles"] = arch_18_matchstick_triangles_chain
DISPATCH_TABLE["geometric_dot_patterns"] = arch_26_square_dot_arrays
DISPATCH_TABLE["geometric_pattern_rule_verbal"] = arch_05_verbal_rule_arithmetic_sequence
DISPATCH_TABLE["geometric_pattern_large_term"] = arch_36_calculate_twentieth_term


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
    Main entry point for Grade 7 Numeric and Geometric Patterns Generator.
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
        q.setdefault("topic", "Numeric and geometric patterns")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
