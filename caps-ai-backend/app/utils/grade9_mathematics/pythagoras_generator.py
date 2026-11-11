"""Grade 9 Mathematics - Theorem of Pythagoras Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 3/02. Pythagoras Theorem.md

Deterministic question generator compliant with South African curriculum standards.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .pythagoras_archetypes_01_25 import (
    arch_01_identify_hypotenuse_and_right_angle_position,
    arch_02_pythagoras_statement_formal_algebraic_equation,
    arch_03_pythagorean_squares_area_investigation,
    arch_04_calculate_hypotenuse_integer_triple_basic,
    arch_05_calculate_hypotenuse_integer_triple_scaled,
    arch_06_calculate_hypotenuse_primitive_triple_5_12_13,
    arch_07_calculate_hypotenuse_primitive_triple_8_15_17,
    arch_08_calculate_hypotenuse_primitive_triple_7_24_25,
    arch_09_calculate_hypotenuse_primitive_triple_9_40_41,
    arch_10_calculate_hypotenuse_irrational_surd_form,
    arch_11_calculate_hypotenuse_decimal_rounding_two_places,
    arch_12_calculate_shorter_side_integer_subtraction,
    arch_13_calculate_shorter_side_primitive_triple_12_from_13_and_5,
    arch_14_calculate_shorter_side_primitive_triple_15_from_17_and_8,
    arch_15_calculate_shorter_side_primitive_triple_24_from_25_and_7,
    arch_16_calculate_shorter_side_surd_simplification,
    arch_17_calculate_shorter_side_decimal_rounding,
    arch_18_converse_pythagoras_verify_right_angled_yes,
    arch_19_converse_pythagoras_verify_right_angled_no,
    arch_20_classify_triangle_acute_pythagoras_inequality,
    arch_21_classify_triangle_obtuse_pythagoras_inequality,
    arch_22_identify_which_angle_is_right_angle_from_converse,
    arch_23_pythagorean_triple_membership_test,
    arch_24_generate_pythagorean_triple_from_formula,
    arch_25_algebraic_pythagoras_linear_unknown_side,
)
from .pythagoras_archetypes_26_50 import (
    arch_26_ladder_against_wall_calculate_height,
    arch_27_ladder_against_wall_calculate_base_distance,
    arch_28_ladder_slipping_two_stage_movement,
    arch_29_rectangle_diagonal_calculation,
    arch_30_rectangle_breadth_from_diagonal_and_length,
    arch_31_square_diagonal_exact_surd_and_decimal,
    arch_32_square_side_and_area_from_diagonal,
    arch_33_rhombus_side_length_from_diagonals,
    arch_34_rhombus_perimeter_from_diagonals,
    arch_35_isosceles_triangle_altitude_calculation,
    arch_36_isosceles_triangle_area_calculation_via_pythagoras,
    arch_37_equilateral_triangle_altitude_and_area,
    arch_38_kite_side_length_from_perpendicular_diagonals,
    arch_39_trapezium_unknown_slanted_side_via_altitude,
    arch_40_trapezium_area_via_pythagoras_height,
    arch_41_distance_between_two_points_cartesian_plane_integer,
    arch_42_distance_between_two_points_cartesian_plane_surd_decimal,
    arch_43_two_connected_right_triangles_shared_hypotenuse,
    arch_44_stepped_spiral_of_theodorus_two_stages,
    arch_45_flagpole_and_guy_wire_length,
    arch_46_ship_navigation_north_east_displacement,
    arch_47_space_diagonal_of_rectangular_prism_box,
    arch_48_cube_space_diagonal_exact_and_rounded,
    arch_49_error_analysis_diagnose_pythagoras_misconception,
    arch_50_compound_multi_step_pythagoras_synthesis,
)

TOPIC = "grade9_math_theorem_of_pythagoras"
LO = "g9_math_pythagoras"

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_identify_hypotenuse_and_right_angle_position": arch_01_identify_hypotenuse_and_right_angle_position,
    "02_pythagoras_statement_formal_algebraic_equation": arch_02_pythagoras_statement_formal_algebraic_equation,
    "03_pythagorean_squares_area_investigation": arch_03_pythagorean_squares_area_investigation,
    "04_calculate_hypotenuse_integer_triple_basic": arch_04_calculate_hypotenuse_integer_triple_basic,
    "05_calculate_hypotenuse_integer_triple_scaled": arch_05_calculate_hypotenuse_integer_triple_scaled,
    "06_calculate_hypotenuse_primitive_triple_5_12_13": arch_06_calculate_hypotenuse_primitive_triple_5_12_13,
    "07_calculate_hypotenuse_primitive_triple_8_15_17": arch_07_calculate_hypotenuse_primitive_triple_8_15_17,
    "08_calculate_hypotenuse_primitive_triple_7_24_25": arch_08_calculate_hypotenuse_primitive_triple_7_24_25,
    "09_calculate_hypotenuse_primitive_triple_9_40_41": arch_09_calculate_hypotenuse_primitive_triple_9_40_41,
    "10_calculate_hypotenuse_irrational_surd_form": arch_10_calculate_hypotenuse_irrational_surd_form,
    "11_calculate_hypotenuse_decimal_rounding_two_places": arch_11_calculate_hypotenuse_decimal_rounding_two_places,
    "12_calculate_shorter_side_integer_subtraction": arch_12_calculate_shorter_side_integer_subtraction,
    "13_calculate_shorter_side_primitive_triple_12_from_13_and_5": arch_13_calculate_shorter_side_primitive_triple_12_from_13_and_5,
    "14_calculate_shorter_side_primitive_triple_15_from_17_and_8": arch_14_calculate_shorter_side_primitive_triple_15_from_17_and_8,
    "15_calculate_shorter_side_primitive_triple_24_from_25_and_7": arch_15_calculate_shorter_side_primitive_triple_24_from_25_and_7,
    "16_calculate_shorter_side_surd_simplification": arch_16_calculate_shorter_side_surd_simplification,
    "17_calculate_shorter_side_decimal_rounding": arch_17_calculate_shorter_side_decimal_rounding,
    "18_converse_pythagoras_verify_right_angled_yes": arch_18_converse_pythagoras_verify_right_angled_yes,
    "19_converse_pythagoras_verify_right_angled_no": arch_19_converse_pythagoras_verify_right_angled_no,
    "20_classify_triangle_acute_pythagoras_inequality": arch_20_classify_triangle_acute_pythagoras_inequality,
    "21_classify_triangle_obtuse_pythagoras_inequality": arch_21_classify_triangle_obtuse_pythagoras_inequality,
    "22_identify_which_angle_is_right_angle_from_converse": arch_22_identify_which_angle_is_right_angle_from_converse,
    "23_pythagorean_triple_membership_test": arch_23_pythagorean_triple_membership_test,
    "24_generate_pythagorean_triple_from_formula": arch_24_generate_pythagorean_triple_from_formula,
    "25_algebraic_pythagoras_linear_unknown_side": arch_25_algebraic_pythagoras_linear_unknown_side,
    "26_ladder_against_wall_calculate_height": arch_26_ladder_against_wall_calculate_height,
    "27_ladder_against_wall_calculate_base_distance": arch_27_ladder_against_wall_calculate_base_distance,
    "28_ladder_slipping_two_stage_movement": arch_28_ladder_slipping_two_stage_movement,
    "29_rectangle_diagonal_calculation": arch_29_rectangle_diagonal_calculation,
    "30_rectangle_breadth_from_diagonal_and_length": arch_30_rectangle_breadth_from_diagonal_and_length,
    "31_square_diagonal_exact_surd_and_decimal": arch_31_square_diagonal_exact_surd_and_decimal,
    "32_square_side_and_area_from_diagonal": arch_32_square_side_and_area_from_diagonal,
    "33_rhombus_side_length_from_diagonals": arch_33_rhombus_side_length_from_diagonals,
    "34_rhombus_perimeter_from_diagonals": arch_34_rhombus_perimeter_from_diagonals,
    "35_isosceles_triangle_altitude_calculation": arch_35_isosceles_triangle_altitude_calculation,
    "36_isosceles_triangle_area_calculation_via_pythagoras": arch_36_isosceles_triangle_area_calculation_via_pythagoras,
    "37_equilateral_triangle_altitude_and_area": arch_37_equilateral_triangle_altitude_and_area,
    "38_kite_side_length_from_perpendicular_diagonals": arch_38_kite_side_length_from_perpendicular_diagonals,
    "39_trapezium_unknown_slanted_side_via_altitude": arch_39_trapezium_unknown_slanted_side_via_altitude,
    "40_trapezium_area_via_pythagoras_height": arch_40_trapezium_area_via_pythagoras_height,
    "41_distance_between_two_points_cartesian_plane_integer": arch_41_distance_between_two_points_cartesian_plane_integer,
    "42_distance_between_two_points_cartesian_plane_surd_decimal": arch_42_distance_between_two_points_cartesian_plane_surd_decimal,
    "43_two_connected_right_triangles_shared_hypotenuse": arch_43_two_connected_right_triangles_shared_hypotenuse,
    "44_stepped_spiral_of_theodorus_two_stages": arch_44_stepped_spiral_of_theodorus_two_stages,
    "45_flagpole_and_guy_wire_length": arch_45_flagpole_and_guy_wire_length,
    "46_ship_navigation_north_east_displacement": arch_46_ship_navigation_north_east_displacement,
    "47_space_diagonal_of_rectangular_prism_box": arch_47_space_diagonal_of_rectangular_prism_box,
    "48_cube_space_diagonal_exact_and_rounded": arch_48_cube_space_diagonal_exact_and_rounded,
    "49_error_analysis_diagnose_pythagoras_misconception": arch_49_error_analysis_diagnose_pythagoras_misconception,
    "50_compound_multi_step_pythagoras_synthesis": arch_50_compound_multi_step_pythagoras_synthesis,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_pythagoras_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Theorem of Pythagoras question."""
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
    q["topic"] = "Pythagoras Theorem"
    q["term"] = 3
    q["caps_weight_percent"] = 10
    q["suggested_duration_mins"] = 3
    return q


# Backward compatibility aliases
generate_pythagoras_question = generate_grade9_pythagoras_question


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
        q = generate_grade9_pythagoras_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
