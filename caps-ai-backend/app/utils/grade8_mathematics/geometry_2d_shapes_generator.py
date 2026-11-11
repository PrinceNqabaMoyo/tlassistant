"""Grade 8 Mathematics - Geometry of 2D Shapes Generator.
Fully expanded to 50 distinct semantic archetypes grounded in the South African CAPS curriculum:
  - Triangles: Interior angle sum (180 deg), exterior angle theorem, isosceles, equilateral, right-angled.
  - Quadrilaterals: Interior sum (360 deg), parallelogram, rectangle, rhombus, square, trapezium, kite.
  - Circles: Radius, diameter, chord, tangent, sector, segment.
  - Similarity and Congruence: Conditions (SSS, SAS, AAS, RHS, AAA) and proportional side calculations.
  - Polygons: Convex/concave, interior and exterior angle sums of regular and irregular polygons.
  - Multi-step composite geometric proofs and deductions.

Follows the 6-Pillar Generator Contract:
  1. Authentic South African CAPS curriculum alignment.
  2. 50 distinct semantic subskills (01 to 50), zero shims.
  3. Deterministic execution via random.Random(seed).
  4. Publication-grade SVG diagrams via DiagramSpec.
  5. 3-tier deterministic pre-baked hint system.
  6. Standard marking scheme with consequential accuracy.
Strictly zero-LLM, deterministic execution.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .geometry_2d_shapes_archetypes_01_25 import (
    arch_01_triangle_interior_angle_sum_numerical,
    arch_02_triangle_exterior_angle_theorem_numerical,
    arch_03_triangle_interior_angle_sum_algebraic_linear,
    arch_04_triangle_exterior_angle_algebraic,
    arch_05_isosceles_triangle_base_angles_given_apex,
    arch_06_isosceles_triangle_apex_given_base_angle,
    arch_07_isosceles_triangle_algebraic_base_angles,
    arch_08_equilateral_triangle_all_angles_and_sides,
    arch_09_right_angled_triangle_complementary_acute_angles,
    arch_10_classify_triangle_by_angles_and_sides,
    arch_11_triangle_exterior_angle_with_adjacent_supplementary,
    arch_12_quadrilateral_interior_angle_sum_numerical,
    arch_13_quadrilateral_interior_angle_sum_algebraic,
    arch_14_parallelogram_opposite_angles_equal,
    arch_15_parallelogram_co_interior_adjacent_angles,
    arch_16_parallelogram_opposite_sides_equal_algebraic,
    arch_17_parallelogram_diagonals_bisect_each_other,
    arch_18_rectangle_properties_right_angles_and_equal_diagonals,
    arch_19_rhombus_properties_all_sides_equal_and_opposite_angles,
    arch_20_rhombus_diagonals_perpendicular_bisectors,
    arch_21_square_properties_regular_quadrilateral,
    arch_22_trapezium_co_interior_angles_between_parallel_sides,
    arch_23_isosceles_trapezium_base_angles_and_diagonals,
    arch_24_kite_properties_two_pairs_adjacent_sides_equal,
    arch_25_kite_diagonals_perpendicular_and_axis_of_symmetry,
)
from .geometry_2d_shapes_archetypes_26_50 import (
    arch_26_circle_parts_identification_radius_diameter_chord,
    arch_27_circle_radius_diameter_relationship_calculations,
    arch_28_circle_tangent_and_secant_definitions,
    arch_29_circle_sector_and_segment_identification,
    arch_30_congruent_triangles_condition_sss,
    arch_31_congruent_triangles_condition_sas,
    arch_32_congruent_triangles_condition_aas,
    arch_33_congruent_triangles_condition_rhs,
    arch_34_congruent_triangles_deduce_corresponding_parts,
    arch_35_similar_triangles_condition_equiangular_aaa,
    arch_36_similar_triangles_proportional_sides_ratio,
    arch_37_similar_triangles_calculate_missing_side_length,
    arch_38_similar_triangles_scale_factor_enlargement_reduction,
    arch_39_polygon_classification_by_number_of_sides,
    arch_40_convex_vs_concave_polygons,
    arch_41_polygon_interior_angle_sum_formula,
    arch_42_regular_polygon_each_interior_angle,
    arch_43_regular_polygon_each_exterior_angle,
    arch_44_polygon_exterior_angle_sum_always_360,
    arch_45_regular_polygon_determine_sides_from_interior_angle,
    arch_46_composite_triangle_and_straight_line_multistep,
    arch_47_composite_triangle_and_parallel_lines_multistep,
    arch_48_quadrilateral_with_parallel_lines_multistep,
    arch_49_hierarchy_of_quadrilaterals_true_false_reasoning,
    arch_50_geometric_proof_isosceles_triangle_base_angles,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_triangle_interior_angle_sum_numerical": arch_01_triangle_interior_angle_sum_numerical,
    "02_triangle_exterior_angle_theorem_numerical": arch_02_triangle_exterior_angle_theorem_numerical,
    "03_triangle_interior_angle_sum_algebraic_linear": arch_03_triangle_interior_angle_sum_algebraic_linear,
    "04_triangle_exterior_angle_algebraic": arch_04_triangle_exterior_angle_algebraic,
    "05_isosceles_triangle_base_angles_given_apex": arch_05_isosceles_triangle_base_angles_given_apex,
    "06_isosceles_triangle_apex_given_base_angle": arch_06_isosceles_triangle_apex_given_base_angle,
    "07_isosceles_triangle_algebraic_base_angles": arch_07_isosceles_triangle_algebraic_base_angles,
    "08_equilateral_triangle_all_angles_and_sides": arch_08_equilateral_triangle_all_angles_and_sides,
    "09_right_angled_triangle_complementary_acute_angles": arch_09_right_angled_triangle_complementary_acute_angles,
    "10_classify_triangle_by_angles_and_sides": arch_10_classify_triangle_by_angles_and_sides,
    "11_triangle_exterior_angle_with_adjacent_supplementary": arch_11_triangle_exterior_angle_with_adjacent_supplementary,
    "12_quadrilateral_interior_angle_sum_numerical": arch_12_quadrilateral_interior_angle_sum_numerical,
    "13_quadrilateral_interior_angle_sum_algebraic": arch_13_quadrilateral_interior_angle_sum_algebraic,
    "14_parallelogram_opposite_angles_equal": arch_14_parallelogram_opposite_angles_equal,
    "15_parallelogram_co_interior_adjacent_angles": arch_15_parallelogram_co_interior_adjacent_angles,
    "16_parallelogram_opposite_sides_equal_algebraic": arch_16_parallelogram_opposite_sides_equal_algebraic,
    "17_parallelogram_diagonals_bisect_each_other": arch_17_parallelogram_diagonals_bisect_each_other,
    "18_rectangle_properties_right_angles_and_equal_diagonals": arch_18_rectangle_properties_right_angles_and_equal_diagonals,
    "19_rhombus_properties_all_sides_equal_and_opposite_angles": arch_19_rhombus_properties_all_sides_equal_and_opposite_angles,
    "20_rhombus_diagonals_perpendicular_bisectors": arch_20_rhombus_diagonals_perpendicular_bisectors,
    "21_square_properties_regular_quadrilateral": arch_21_square_properties_regular_quadrilateral,
    "22_trapezium_co_interior_angles_between_parallel_sides": arch_22_trapezium_co_interior_angles_between_parallel_sides,
    "23_isosceles_trapezium_base_angles_and_diagonals": arch_23_isosceles_trapezium_base_angles_and_diagonals,
    "24_kite_properties_two_pairs_adjacent_sides_equal": arch_24_kite_properties_two_pairs_adjacent_sides_equal,
    "25_kite_diagonals_perpendicular_and_axis_of_symmetry": arch_25_kite_diagonals_perpendicular_and_axis_of_symmetry,
    "26_circle_parts_identification_radius_diameter_chord": arch_26_circle_parts_identification_radius_diameter_chord,
    "27_circle_radius_diameter_relationship_calculations": arch_27_circle_radius_diameter_relationship_calculations,
    "28_circle_tangent_and_secant_definitions": arch_28_circle_tangent_and_secant_definitions,
    "29_circle_sector_and_segment_identification": arch_29_circle_sector_and_segment_identification,
    "30_congruent_triangles_condition_sss": arch_30_congruent_triangles_condition_sss,
    "31_congruent_triangles_condition_sas": arch_31_congruent_triangles_condition_sas,
    "32_congruent_triangles_condition_aas": arch_32_congruent_triangles_condition_aas,
    "33_congruent_triangles_condition_rhs": arch_33_congruent_triangles_condition_rhs,
    "34_congruent_triangles_deduce_corresponding_parts": arch_34_congruent_triangles_deduce_corresponding_parts,
    "35_similar_triangles_condition_equiangular_aaa": arch_35_similar_triangles_condition_equiangular_aaa,
    "36_similar_triangles_proportional_sides_ratio": arch_36_similar_triangles_proportional_sides_ratio,
    "37_similar_triangles_calculate_missing_side_length": arch_37_similar_triangles_calculate_missing_side_length,
    "38_similar_triangles_scale_factor_enlargement_reduction": arch_38_similar_triangles_scale_factor_enlargement_reduction,
    "39_polygon_classification_by_number_of_sides": arch_39_polygon_classification_by_number_of_sides,
    "40_convex_vs_concave_polygons": arch_40_convex_vs_concave_polygons,
    "41_polygon_interior_angle_sum_formula": arch_41_polygon_interior_angle_sum_formula,
    "42_regular_polygon_each_interior_angle": arch_42_regular_polygon_each_interior_angle,
    "43_regular_polygon_each_exterior_angle": arch_43_regular_polygon_each_exterior_angle,
    "44_polygon_exterior_angle_sum_always_360": arch_44_polygon_exterior_angle_sum_always_360,
    "45_regular_polygon_determine_sides_from_interior_angle": arch_45_regular_polygon_determine_sides_from_interior_angle,
    "46_composite_triangle_and_straight_line_multistep": arch_46_composite_triangle_and_straight_line_multistep,
    "47_composite_triangle_and_parallel_lines_multistep": arch_47_composite_triangle_and_parallel_lines_multistep,
    "48_quadrilateral_with_parallel_lines_multistep": arch_48_quadrilateral_with_parallel_lines_multistep,
    "49_hierarchy_of_quadrilaterals_true_false_reasoning": arch_49_hierarchy_of_quadrilaterals_true_false_reasoning,
    "50_geometric_proof_isosceles_triangle_base_angles": arch_50_geometric_proof_isosceles_triangle_base_angles,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())


def generate_grade8_geometry_2d_question(
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
    q_data["topic"] = "Geometry of 2D Shapes"
    q_data["term"] = 2
    q_data["caps_weight_percent"] = 12
    q_data["suggested_duration_mins"] = 3
    q_data["difficulty"] = difficulty
    q_data["mode"] = mode
    q_data["subskill"] = target_subskill

    if "marking_schema" not in q_data:
        m = q_data.get("marks", 3)
        q_data["marking_schema"] = {
            "total_marks": m,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct geometric theorem / reason", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate calculation or deduction", "marks": m - 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_geometric_reason", "penalty": 1}],
            "carry_forward_rule": "consequential_accuracy",
        }

    return q_data


generate = generate_grade8_geometry_2d_question
