"""Grade 8 Mathematics — Perimeter and Area of 2D Shapes Generator.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 2/04. Perimeter and area of 2D shapes.md

Expanded to 50 distinct semantic archetypes covering:
  - Perimeter: Square, rectangle, triangles (equilateral, isosceles, scalene), regular polygons,
    parallelogram, rhombus, trapezium, kite, circle circumference, semicircle, quadrant,
    composite L-shapes, and realistic fencing/track word problems.
  - Area: Square, rectangle, triangles (acute, obtuse, right-angled, inverse dimensions),
    parallelogram, rhombus, kite, trapezium, circle area, semicircle, quadrant,
    unit conversions (mm, cm, m, km, hectares), composite areas, shaded areas, and tiling costs.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .perimeter_area_2d_archetypes_01_25 import (
    arch_01_perimeter_square_formula_and_calculation,
    arch_02_perimeter_rectangle_formula_and_calculation,
    arch_03_perimeter_square_inverse_find_side_length,
    arch_04_perimeter_rectangle_inverse_find_breadth_or_length,
    arch_05_perimeter_equilateral_triangle,
    arch_06_perimeter_isosceles_triangle,
    arch_07_perimeter_scalene_triangle,
    arch_08_perimeter_regular_pentagon_and_hexagon,
    arch_09_perimeter_parallelogram_and_rhombus,
    arch_10_perimeter_trapezium_sum_all_sides,
    arch_11_perimeter_kite_adjacent_pairs,
    arch_12_circumference_circle_given_radius,
    arch_13_circumference_circle_given_diameter,
    arch_14_circumference_circle_inverse_find_radius,
    arch_15_circumference_circle_inverse_find_diameter,
    arch_16_perimeter_semicircle_curved_plus_diameter,
    arch_17_perimeter_quadrant_quarter_circle_plus_two_radii,
    arch_18_perimeter_composite_l_shaped_polygon,
    arch_19_perimeter_word_problem_fencing_garden_with_gate,
    arch_20_perimeter_word_problem_athletic_track_straight_and_semicircles,
    arch_21_area_square_direct_formula,
    arch_22_area_square_inverse_square_root_side,
    arch_23_area_rectangle_direct_formula,
    arch_24_area_rectangle_inverse_find_length_or_breadth,
    arch_25_area_right_angled_triangle,
)
from .perimeter_area_2d_archetypes_26_50 import (
    arch_26_area_acute_triangle_interior_perpendicular_height,
    arch_27_area_obtuse_triangle_exterior_perpendicular_height,
    arch_28_area_triangle_inverse_find_height,
    arch_29_area_triangle_inverse_find_base,
    arch_30_area_parallelogram_base_times_perpendicular_height,
    arch_31_area_parallelogram_inverse_find_base_or_height,
    arch_32_area_rhombus_using_diagonals,
    arch_33_area_kite_using_diagonals,
    arch_34_area_trapezium_half_sum_parallel_sides_times_height,
    arch_35_area_trapezium_inverse_find_height,
    arch_36_area_circle_given_radius,
    arch_37_area_circle_given_diameter,
    arch_38_area_circle_inverse_find_radius,
    arch_39_area_semicircle_half_pi_r_squared,
    arch_40_area_quadrant_quarter_pi_r_squared,
    arch_41_unit_conversion_length_mm_cm_m_km,
    arch_42_unit_conversion_area_cm2_to_mm2,
    arch_43_unit_conversion_area_m2_to_cm2,
    arch_44_unit_conversion_area_hectares_to_m2,
    arch_45_composite_area_l_shaped_partition_two_rectangles,
    arch_46_composite_area_rectangle_plus_triangle_gable_end,
    arch_47_composite_area_rectangle_with_semicircle_attached,
    arch_48_shaded_area_square_with_inscribed_circle,
    arch_49_shaded_area_annulus_ring_between_concentric_circles,
    arch_50_area_word_problem_flooring_tiling_cost_calculation,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_perimeter_square_formula_and_calculation": arch_01_perimeter_square_formula_and_calculation,
    "02_perimeter_rectangle_formula_and_calculation": arch_02_perimeter_rectangle_formula_and_calculation,
    "03_perimeter_square_inverse_find_side_length": arch_03_perimeter_square_inverse_find_side_length,
    "04_perimeter_rectangle_inverse_find_breadth_or_length": arch_04_perimeter_rectangle_inverse_find_breadth_or_length,
    "05_perimeter_equilateral_triangle": arch_05_perimeter_equilateral_triangle,
    "06_perimeter_isosceles_triangle": arch_06_perimeter_isosceles_triangle,
    "07_perimeter_scalene_triangle": arch_07_perimeter_scalene_triangle,
    "08_perimeter_regular_pentagon_and_hexagon": arch_08_perimeter_regular_pentagon_and_hexagon,
    "09_perimeter_parallelogram_and_rhombus": arch_09_perimeter_parallelogram_and_rhombus,
    "10_perimeter_trapezium_sum_all_sides": arch_10_perimeter_trapezium_sum_all_sides,
    "11_perimeter_kite_adjacent_pairs": arch_11_perimeter_kite_adjacent_pairs,
    "12_circumference_circle_given_radius": arch_12_circumference_circle_given_radius,
    "13_circumference_circle_given_diameter": arch_13_circumference_circle_given_diameter,
    "14_circumference_circle_inverse_find_radius": arch_14_circumference_circle_inverse_find_radius,
    "15_circumference_circle_inverse_find_diameter": arch_15_circumference_circle_inverse_find_diameter,
    "16_perimeter_semicircle_curved_plus_diameter": arch_16_perimeter_semicircle_curved_plus_diameter,
    "17_perimeter_quadrant_quarter_circle_plus_two_radii": arch_17_perimeter_quadrant_quarter_circle_plus_two_radii,
    "18_perimeter_composite_l_shaped_polygon": arch_18_perimeter_composite_l_shaped_polygon,
    "19_perimeter_word_problem_fencing_garden_with_gate": arch_19_perimeter_word_problem_fencing_garden_with_gate,
    "20_perimeter_word_problem_athletic_track_straight_and_semicircles": arch_20_perimeter_word_problem_athletic_track_straight_and_semicircles,
    "21_area_square_direct_formula": arch_21_area_square_direct_formula,
    "22_area_square_inverse_square_root_side": arch_22_area_square_inverse_square_root_side,
    "23_area_rectangle_direct_formula": arch_23_area_rectangle_direct_formula,
    "24_area_rectangle_inverse_find_length_or_breadth": arch_24_area_rectangle_inverse_find_length_or_breadth,
    "25_area_right_angled_triangle": arch_25_area_right_angled_triangle,
    "26_area_acute_triangle_interior_perpendicular_height": arch_26_area_acute_triangle_interior_perpendicular_height,
    "27_area_obtuse_triangle_exterior_perpendicular_height": arch_27_area_obtuse_triangle_exterior_perpendicular_height,
    "28_area_triangle_inverse_find_height": arch_28_area_triangle_inverse_find_height,
    "29_area_triangle_inverse_find_base": arch_29_area_triangle_inverse_find_base,
    "30_area_parallelogram_base_times_perpendicular_height": arch_30_area_parallelogram_base_times_perpendicular_height,
    "31_area_parallelogram_inverse_find_base_or_height": arch_31_area_parallelogram_inverse_find_base_or_height,
    "32_area_rhombus_using_diagonals": arch_32_area_rhombus_using_diagonals,
    "33_area_kite_using_diagonals": arch_33_area_kite_using_diagonals,
    "34_area_trapezium_half_sum_parallel_sides_times_height": arch_34_area_trapezium_half_sum_parallel_sides_times_height,
    "35_area_trapezium_inverse_find_height": arch_35_area_trapezium_inverse_find_height,
    "36_area_circle_given_radius": arch_36_area_circle_given_radius,
    "37_area_circle_given_diameter": arch_37_area_circle_given_diameter,
    "38_area_circle_inverse_find_radius": arch_38_area_circle_inverse_find_radius,
    "39_area_semicircle_half_pi_r_squared": arch_39_area_semicircle_half_pi_r_squared,
    "40_area_quadrant_quarter_pi_r_squared": arch_40_area_quadrant_quarter_pi_r_squared,
    "41_unit_conversion_length_mm_cm_m_km": arch_41_unit_conversion_length_mm_cm_m_km,
    "42_unit_conversion_area_cm2_to_mm2": arch_42_unit_conversion_area_cm2_to_mm2,
    "43_unit_conversion_area_m2_to_cm2": arch_43_unit_conversion_area_m2_to_cm2,
    "44_unit_conversion_area_hectares_to_m2": arch_44_unit_conversion_area_hectares_to_m2,
    "45_composite_area_l_shaped_partition_two_rectangles": arch_45_composite_area_l_shaped_partition_two_rectangles,
    "46_composite_area_rectangle_plus_triangle_gable_end": arch_46_composite_area_rectangle_plus_triangle_gable_end,
    "47_composite_area_rectangle_with_semicircle_attached": arch_47_composite_area_rectangle_with_semicircle_attached,
    "48_shaded_area_square_with_inscribed_circle": arch_48_shaded_area_square_with_inscribed_circle,
    "49_shaded_area_annulus_ring_between_concentric_circles": arch_49_shaded_area_annulus_ring_between_concentric_circles,
    "50_area_word_problem_flooring_tiling_cost_calculation": arch_50_area_word_problem_flooring_tiling_cost_calculation,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())


def generate_grade8_perimeter_and_area_of_2d_shapes_question(
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
    q_data["topic"] = "Perimeter and area of 2D shapes"
    q_data["term"] = 2
    q_data["caps_weight_percent"] = 12
    q_data["suggested_duration_mins"] = 3
    q_data["difficulty"] = difficulty
    q_data["mode"] = mode
    q_data["subskill"] = target_subskill

    if "marking_schema" not in q_data:
        m = q_data.get("marks", 2)
        q_data["marking_schema"] = {
            "total_marks": m,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct perimeter/area formula or setup", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate calculation and correct unit", "marks": m - 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_or_wrong_unit", "penalty": 1}],
            "carry_forward_rule": "consequential_accuracy",
        }

    return q_data


generate = generate_grade8_perimeter_and_area_of_2d_shapes_question
