"""Grade 7 Mathematics - Perimeter and Area of 2D Shapes Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 4/01. Perimeter and area of 2D shapes.md & Syllabus.md
Focus: Perimeter of squares, rectangles, triangles, polygons, circles; area of squares, rectangles, triangles (right/acute/obtuse); composite L/T shapes; shaded regions; metric conversions (mm², cm², m², km²); scaling effects (k and k²); and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .perimeter_area_2d_archetypes_01_25 import (
    arch_01_perimeter_of_square_formula,
    arch_02_perimeter_of_square_find_side_from_perimeter,
    arch_03_perimeter_of_rectangle_standard,
    arch_04_perimeter_of_rectangle_find_breadth_from_perimeter,
    arch_05_perimeter_of_rectangle_find_length_from_perimeter,
    arch_06_perimeter_of_equilateral_triangle,
    arch_07_perimeter_of_isosceles_triangle,
    arch_08_perimeter_of_scalene_triangle,
    arch_09_perimeter_of_regular_pentagon,
    arch_10_perimeter_of_regular_hexagon,
    arch_11_perimeter_of_regular_octagon,
    arch_12_perimeter_of_irregular_polygon_missing_side,
    arch_13_circumference_of_circle_given_radius,
    arch_14_circumference_of_circle_given_diameter,
    arch_15_perimeter_word_problem_fencing_cost,
    arch_16_perimeter_word_problem_running_track_laps,
    arch_17_area_of_square_standard,
    arch_18_area_of_square_find_side_from_area,
    arch_19_area_of_rectangle_standard,
    arch_20_area_of_rectangle_with_decimal_dimensions,
    arch_21_area_of_rectangle_find_breadth_from_area,
    arch_22_area_of_rectangle_find_length_from_area,
    arch_23_area_of_right_angled_triangle,
    arch_24_area_of_acute_triangle_interior_height,
    arch_25_area_of_obtuse_triangle_exterior_height,
)
from .perimeter_area_2d_archetypes_26_50 import (
    arch_26_area_of_triangle_find_height_from_area,
    arch_27_area_of_triangle_find_base_from_area,
    arch_28_area_triangle_identifying_correct_perpendicular_height,
    arch_29_area_of_composite_l_shaped_polygon,
    arch_30_area_of_composite_t_shaped_polygon,
    arch_31_area_of_composite_rectangle_plus_triangle,
    arch_32_area_of_shaded_region_rectangle_with_inner_rectangle,
    arch_33_area_of_shaded_region_square_with_inner_triangle,
    arch_34_perimeter_of_composite_l_shaped_polygon,
    arch_35_area_unit_conversion_cm2_to_mm2,
    arch_36_area_unit_conversion_mm2_to_cm2,
    arch_37_area_unit_conversion_m2_to_cm2,
    arch_38_area_unit_conversion_cm2_to_m2,
    arch_39_area_unit_conversion_km2_to_m2,
    arch_40_word_problem_tiling_floor_number_of_tiles,
    arch_41_word_problem_carpeting_room_cost,
    arch_42_word_problem_fertilizing_lawn_area,
    arch_43_word_problem_painting_wall_area_litres,
    arch_44_scaling_effect_doubling_dimensions_on_perimeter,
    arch_45_scaling_effect_doubling_dimensions_on_area,
    arch_46_scaling_effect_tripling_dimensions_on_area,
    arch_47_common_error_confusing_perimeter_and_area,
    arch_48_common_error_using_slant_height_for_triangle_area,
    arch_49_common_error_metric_area_conversion_100_trap,
    arch_50_perimeter_and_area_2d_comprehensive_diagnostic_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_perimeter_of_square_formula": arch_01_perimeter_of_square_formula,
    "02_perimeter_of_square_find_side_from_perimeter": arch_02_perimeter_of_square_find_side_from_perimeter,
    "03_perimeter_of_rectangle_standard": arch_03_perimeter_of_rectangle_standard,
    "04_perimeter_of_rectangle_find_breadth_from_perimeter": arch_04_perimeter_of_rectangle_find_breadth_from_perimeter,
    "05_perimeter_of_rectangle_find_length_from_perimeter": arch_05_perimeter_of_rectangle_find_length_from_perimeter,
    "06_perimeter_of_equilateral_triangle": arch_06_perimeter_of_equilateral_triangle,
    "07_perimeter_of_isosceles_triangle": arch_07_perimeter_of_isosceles_triangle,
    "08_perimeter_of_scalene_triangle": arch_08_perimeter_of_scalene_triangle,
    "09_perimeter_of_regular_pentagon": arch_09_perimeter_of_regular_pentagon,
    "10_perimeter_of_regular_hexagon": arch_10_perimeter_of_regular_hexagon,
    "11_perimeter_of_regular_octagon": arch_11_perimeter_of_regular_octagon,
    "12_perimeter_of_irregular_polygon_missing_side": arch_12_perimeter_of_irregular_polygon_missing_side,
    "13_circumference_of_circle_given_radius": arch_13_circumference_of_circle_given_radius,
    "14_circumference_of_circle_given_diameter": arch_14_circumference_of_circle_given_diameter,
    "15_perimeter_word_problem_fencing_cost": arch_15_perimeter_word_problem_fencing_cost,
    "16_perimeter_word_problem_running_track_laps": arch_16_perimeter_word_problem_running_track_laps,
    "17_area_of_square_standard": arch_17_area_of_square_standard,
    "18_area_of_square_find_side_from_area": arch_18_area_of_square_find_side_from_area,
    "19_area_of_rectangle_standard": arch_19_area_of_rectangle_standard,
    "20_area_of_rectangle_with_decimal_dimensions": arch_20_area_of_rectangle_with_decimal_dimensions,
    "21_area_of_rectangle_find_breadth_from_area": arch_21_area_of_rectangle_find_breadth_from_area,
    "22_area_of_rectangle_find_length_from_area": arch_22_area_of_rectangle_find_length_from_area,
    "23_area_of_right_angled_triangle": arch_23_area_of_right_angled_triangle,
    "24_area_of_acute_triangle_interior_height": arch_24_area_of_acute_triangle_interior_height,
    "25_area_of_obtuse_triangle_exterior_height": arch_25_area_of_obtuse_triangle_exterior_height,
    "26_area_of_triangle_find_height_from_area": arch_26_area_of_triangle_find_height_from_area,
    "27_area_of_triangle_find_base_from_area": arch_27_area_of_triangle_find_base_from_area,
    "28_area_triangle_identifying_correct_perpendicular_height": arch_28_area_triangle_identifying_correct_perpendicular_height,
    "29_area_of_composite_l_shaped_polygon": arch_29_area_of_composite_l_shaped_polygon,
    "30_area_of_composite_t_shaped_polygon": arch_30_area_of_composite_t_shaped_polygon,
    "31_area_of_composite_rectangle_plus_triangle": arch_31_area_of_composite_rectangle_plus_triangle,
    "32_area_of_shaded_region_rectangle_with_inner_rectangle": arch_32_area_of_shaded_region_rectangle_with_inner_rectangle,
    "33_area_of_shaded_region_square_with_inner_triangle": arch_33_area_of_shaded_region_square_with_inner_triangle,
    "34_perimeter_of_composite_l_shaped_polygon": arch_34_perimeter_of_composite_l_shaped_polygon,
    "35_area_unit_conversion_cm2_to_mm2": arch_35_area_unit_conversion_cm2_to_mm2,
    "36_area_unit_conversion_mm2_to_cm2": arch_36_area_unit_conversion_mm2_to_cm2,
    "37_area_unit_conversion_m2_to_cm2": arch_37_area_unit_conversion_m2_to_cm2,
    "38_area_unit_conversion_cm2_to_m2": arch_38_area_unit_conversion_cm2_to_m2,
    "39_area_unit_conversion_km2_to_m2": arch_39_area_unit_conversion_km2_to_m2,
    "40_word_problem_tiling_floor_number_of_tiles": arch_40_word_problem_tiling_floor_number_of_tiles,
    "41_word_problem_carpeting_room_cost": arch_41_word_problem_carpeting_room_cost,
    "42_word_problem_fertilizing_lawn_area": arch_42_word_problem_fertilizing_lawn_area,
    "43_word_problem_painting_wall_area_litres": arch_43_word_problem_painting_wall_area_litres,
    "44_scaling_effect_doubling_dimensions_on_perimeter": arch_44_scaling_effect_doubling_dimensions_on_perimeter,
    "45_scaling_effect_doubling_dimensions_on_area": arch_45_scaling_effect_doubling_dimensions_on_area,
    "46_scaling_effect_tripling_dimensions_on_area": arch_46_scaling_effect_tripling_dimensions_on_area,
    "47_common_error_confusing_perimeter_and_area": arch_47_common_error_confusing_perimeter_and_area,
    "48_common_error_using_slant_height_for_triangle_area": arch_48_common_error_using_slant_height_for_triangle_area,
    "49_common_error_metric_area_conversion_100_trap": arch_49_common_error_metric_area_conversion_100_trap,
    "50_perimeter_and_area_2d_comprehensive_diagnostic_autopsy": arch_50_perimeter_and_area_2d_comprehensive_diagnostic_autopsy,
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


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    questions = []
    target_sub = str(subskill or "").strip().lower()

    if target_sub and target_sub not in ("compound", "all", "mixed", "auto", "default", "none"):
        matched = None
        for k in ARCHETYPE_BUILDERS:
            if target_sub == k.lower() or target_sub in k.lower():
                matched = k
                break
        for _ in range(count):
            if matched:
                questions.append(ARCHETYPE_BUILDERS[matched](rng))
            else:
                s = rng.choice(SUBSKILLS)
                questions.append(ARCHETYPE_BUILDERS[s](rng))
        return questions

    for i in range(count):
        s = SUBSKILLS[i % len(SUBSKILLS)]
        questions.append(ARCHETYPE_BUILDERS[s](rng))

    return questions
