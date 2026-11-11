"""Grade 8 Mathematics — The Theorem of Pythagoras Generator.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 3/04. The theorem of Pythagoras.md

Expanded to 50 distinct semantic archetypes covering:
  - Hypotenuse identification, right-angle relationship, area proof with squares on sides.
  - Calculating hypotenuse with Pythagorean triples (3:4:5, 5:12:13, 8:15:17, 7:24:25, 9:40:41) and non-integers (1 dec, 2 dec, surd form).
  - Calculating legs with algebraic rearrangement c² - b² = a² (triples, non-integers, surds).
  - Converse of Pythagoras: classifying triangles as right-angled, acute (c² < a² + b²), obtuse (c² > a² + b²).
  - Real-world contexts: ladders, walking displacements, diagonals of rectangles/squares, guy wires, ramps, altitudes, composite shapes.
  - Coordinate distance, perimeter, area, rhombuses, broken trees, adjacent triangles.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .pythagoras_archetypes_01_25 import (
    arch_01_identify_hypotenuse_and_right_angle_relationship,
    arch_02_state_theorem_of_pythagoras_formula_and_reasons,
    arch_03_pythagoras_area_proof_squares_on_sides,
    arch_04_calculate_hypotenuse_triple_3_4_5_scaled,
    arch_05_calculate_hypotenuse_triple_5_12_13_scaled,
    arch_06_calculate_hypotenuse_triple_8_15_17_scaled,
    arch_07_calculate_hypotenuse_triple_7_24_25_scaled,
    arch_08_calculate_hypotenuse_triple_9_40_41_scaled,
    arch_09_calculate_hypotenuse_non_integer_round_1_decimal,
    arch_10_calculate_hypotenuse_non_integer_round_2_decimals,
    arch_11_calculate_hypotenuse_surd_exact_form,
    arch_12_calculate_hypotenuse_isosceles_right_angled_triangle,
    arch_13_calculate_leg_rearrangement_formula,
    arch_14_calculate_leg_triple_3_4_5_scaled,
    arch_15_calculate_leg_triple_5_12_13_scaled,
    arch_16_calculate_leg_triple_8_15_17_scaled,
    arch_17_calculate_leg_triple_7_24_25_scaled,
    arch_18_calculate_leg_triple_6_8_10_scaled,
    arch_19_calculate_leg_non_integer_round_1_decimal,
    arch_20_calculate_leg_non_integer_round_2_decimals,
    arch_21_calculate_leg_exact_surd_form,
    arch_22_identify_longest_side_rule_in_right_triangle,
    arch_23_converse_theorem_statement_and_meaning,
    arch_24_converse_verify_right_angled_triangle_triple,
    arch_25_converse_identify_which_vertex_is_90_degrees,
)
from .pythagoras_archetypes_26_50 import (
    arch_26_converse_classify_triangle_acute_right_obtuse,
    arch_27_converse_acute_angled_triangle_test,
    arch_28_converse_obtuse_angled_triangle_test,
    arch_29_converse_triangle_table_classification,
    arch_30_converse_error_analysis_comparing_wrong_side_to_sum,
    arch_31_context_ladder_find_hypotenuse_length,
    arch_32_context_ladder_find_wall_height_reached,
    arch_33_context_ladder_find_distance_from_base,
    arch_34_context_walking_displacement_north_east,
    arch_35_context_diagonal_of_rectangle,
    arch_36_context_diagonal_of_square,
    arch_37_context_flagpole_guy_wire_support,
    arch_38_context_ramp_slope_distance,
    arch_39_context_altitude_of_isosceles_triangle,
    arch_40_context_altitude_of_equilateral_triangle,
    arch_41_coordinate_geometry_distance_between_two_points,
    arch_42_coordinate_geometry_distance_from_origin,
    arch_43_perimeter_of_right_angled_triangle_using_pythagoras,
    arch_44_area_of_right_angled_triangle_given_hypotenuse_and_leg,
    arch_45_composite_area_rectangle_plus_right_triangle,
    arch_46_composite_perimeter_shape_with_right_triangle_slant,
    arch_47_rhombus_diagonals_and_side_length,
    arch_48_pythagorean_triples_scaling_rule,
    arch_49_two_step_pythagoras_adjacent_right_triangles,
    arch_50_pythagoras_word_problem_tree_broken_by_wind,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_identify_hypotenuse_and_right_angle_relationship": arch_01_identify_hypotenuse_and_right_angle_relationship,
    "02_state_theorem_of_pythagoras_formula_and_reasons": arch_02_state_theorem_of_pythagoras_formula_and_reasons,
    "03_pythagoras_area_proof_squares_on_sides": arch_03_pythagoras_area_proof_squares_on_sides,
    "04_calculate_hypotenuse_triple_3_4_5_scaled": arch_04_calculate_hypotenuse_triple_3_4_5_scaled,
    "05_calculate_hypotenuse_triple_5_12_13_scaled": arch_05_calculate_hypotenuse_triple_5_12_13_scaled,
    "06_calculate_hypotenuse_triple_8_15_17_scaled": arch_06_calculate_hypotenuse_triple_8_15_17_scaled,
    "07_calculate_hypotenuse_triple_7_24_25_scaled": arch_07_calculate_hypotenuse_triple_7_24_25_scaled,
    "08_calculate_hypotenuse_triple_9_40_41_scaled": arch_08_calculate_hypotenuse_triple_9_40_41_scaled,
    "09_calculate_hypotenuse_non_integer_round_1_decimal": arch_09_calculate_hypotenuse_non_integer_round_1_decimal,
    "10_calculate_hypotenuse_non_integer_round_2_decimals": arch_10_calculate_hypotenuse_non_integer_round_2_decimals,
    "11_calculate_hypotenuse_surd_exact_form": arch_11_calculate_hypotenuse_surd_exact_form,
    "12_calculate_hypotenuse_isosceles_right_angled_triangle": arch_12_calculate_hypotenuse_isosceles_right_angled_triangle,
    "13_calculate_leg_rearrangement_formula": arch_13_calculate_leg_rearrangement_formula,
    "14_calculate_leg_triple_3_4_5_scaled": arch_14_calculate_leg_triple_3_4_5_scaled,
    "15_calculate_leg_triple_5_12_13_scaled": arch_15_calculate_leg_triple_5_12_13_scaled,
    "16_calculate_leg_triple_8_15_17_scaled": arch_16_calculate_leg_triple_8_15_17_scaled,
    "17_calculate_leg_triple_7_24_25_scaled": arch_17_calculate_leg_triple_7_24_25_scaled,
    "18_calculate_leg_triple_6_8_10_scaled": arch_18_calculate_leg_triple_6_8_10_scaled,
    "19_calculate_leg_non_integer_round_1_decimal": arch_19_calculate_leg_non_integer_round_1_decimal,
    "20_calculate_leg_non_integer_round_2_decimals": arch_20_calculate_leg_non_integer_round_2_decimals,
    "21_calculate_leg_exact_surd_form": arch_21_calculate_leg_exact_surd_form,
    "22_identify_longest_side_rule_in_right_triangle": arch_22_identify_longest_side_rule_in_right_triangle,
    "23_converse_theorem_statement_and_meaning": arch_23_converse_theorem_statement_and_meaning,
    "24_converse_verify_right_angled_triangle_triple": arch_24_converse_verify_right_angled_triangle_triple,
    "25_converse_identify_which_vertex_is_90_degrees": arch_25_converse_identify_which_vertex_is_90_degrees,
    "26_converse_classify_triangle_acute_right_obtuse": arch_26_converse_classify_triangle_acute_right_obtuse,
    "27_converse_acute_angled_triangle_test": arch_27_converse_acute_angled_triangle_test,
    "28_converse_obtuse_angled_triangle_test": arch_28_converse_obtuse_angled_triangle_test,
    "29_converse_triangle_table_classification": arch_29_converse_triangle_table_classification,
    "30_converse_error_analysis_comparing_wrong_side_to_sum": arch_30_converse_error_analysis_comparing_wrong_side_to_sum,
    "31_context_ladder_find_hypotenuse_length": arch_31_context_ladder_find_hypotenuse_length,
    "32_context_ladder_find_wall_height_reached": arch_32_context_ladder_find_wall_height_reached,
    "33_context_ladder_find_distance_from_base": arch_33_context_ladder_find_distance_from_base,
    "34_context_walking_displacement_north_east": arch_34_context_walking_displacement_north_east,
    "35_context_diagonal_of_rectangle": arch_35_context_diagonal_of_rectangle,
    "36_context_diagonal_of_square": arch_36_context_diagonal_of_square,
    "37_context_flagpole_guy_wire_support": arch_37_context_flagpole_guy_wire_support,
    "38_context_ramp_slope_distance": arch_38_context_ramp_slope_distance,
    "39_context_altitude_of_isosceles_triangle": arch_39_context_altitude_of_isosceles_triangle,
    "40_context_altitude_of_equilateral_triangle": arch_40_context_altitude_of_equilateral_triangle,
    "41_coordinate_geometry_distance_between_two_points": arch_41_coordinate_geometry_distance_between_two_points,
    "42_coordinate_geometry_distance_from_origin": arch_42_coordinate_geometry_distance_from_origin,
    "43_perimeter_of_right_angled_triangle_using_pythagoras": arch_43_perimeter_of_right_angled_triangle_using_pythagoras,
    "44_area_of_right_angled_triangle_given_hypotenuse_and_leg": arch_44_area_of_right_angled_triangle_given_hypotenuse_and_leg,
    "45_composite_area_rectangle_plus_right_triangle": arch_45_composite_area_rectangle_plus_right_triangle,
    "46_composite_perimeter_shape_with_right_triangle_slant": arch_46_composite_perimeter_shape_with_right_triangle_slant,
    "47_rhombus_diagonals_and_side_length": arch_47_rhombus_diagonals_and_side_length,
    "48_pythagorean_triples_scaling_rule": arch_48_pythagorean_triples_scaling_rule,
    "49_two_step_pythagoras_adjacent_right_triangles": arch_49_two_step_pythagoras_adjacent_right_triangles,
    "50_pythagoras_word_problem_tree_broken_by_wind": arch_50_pythagoras_word_problem_tree_broken_by_wind,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())


def generate_grade8_pythagoras_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    target_subskill = subskill
    if not target_subskill or target_subskill not in ARCHETYPE_MAP:
        if mode and mode.startswith("elementary_"):
            candidate = mode[len("elementary_"):]
            if candidate in ARCHETYPE_MAP:
                target_subskill = candidate
            else:
                for k in ARCHETYPE_MAP:
                    if candidate in k:
                        target_subskill = k
                        break

    if not target_subskill or target_subskill not in ARCHETYPE_MAP:
        target_subskill = rng.choice(SUBSKILLS)

    generator_fn = ARCHETYPE_MAP[target_subskill]
    q_data = generator_fn(rng)

    q_data["subject"] = "mathematics"
    q_data["grade"] = "grade-8"
    q_data["topic"] = "The theorem of Pythagoras"
    q_data["term"] = 3
    q_data["caps_weight_percent"] = 10
    q_data["suggested_duration_mins"] = 3
    q_data["difficulty"] = difficulty
    q_data["mode"] = mode
    q_data["subskill"] = target_subskill

    if "marking_schema" not in q_data:
        m = q_data.get("marks", 3)
        q_data["marking_schema"] = {
            "total_marks": m,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct Pythagoras formula or geometric reason statement", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct algebraic substitution and calculation", "marks": m - 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_geometric_reason", "penalty": 1}],
            "carry_forward_rule": "consequential_accuracy",
        }

    return q_data


generate = generate_grade8_pythagoras_question
