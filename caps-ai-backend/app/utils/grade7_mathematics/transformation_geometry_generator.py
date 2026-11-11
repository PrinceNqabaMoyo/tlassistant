"""Grade 7 Mathematics - Transformation Geometry Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/04. Transformation geometry.md
Focus: Lines of symmetry of 2D shapes, translations on square grids, coordinate rules, reflections across axes and mirror lines, rotations (90°, 180°), enlargements/reductions (scale factor k, area effect k²), and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .transformation_geometry_archetypes_01_25 import (
    arch_01_line_of_symmetry_definition_and_verification,
    arch_02_square_lines_of_symmetry,
    arch_03_rectangle_lines_of_symmetry_diagonal_trap,
    arch_04_equilateral_triangle_lines_of_symmetry,
    arch_05_isosceles_triangle_lines_of_symmetry,
    arch_06_scalene_triangle_lines_of_symmetry,
    arch_07_parallelogram_lines_of_symmetry,
    arch_08_rhombus_lines_of_symmetry,
    arch_09_kite_lines_of_symmetry,
    arch_10_isosceles_trapezium_lines_of_symmetry,
    arch_11_regular_hexagon_lines_of_symmetry,
    arch_12_circle_lines_of_symmetry,
    arch_13_completing_symmetric_figure_vertical_line,
    arch_14_completing_symmetric_figure_horizontal_line,
    arch_15_translation_concept_and_isometry,
    arch_16_translation_horizontal_units,
    arch_17_translation_vertical_units,
    arch_18_translation_combined_coordinate_rule,
    arch_19_translation_point_from_description,
    arch_20_translation_triangle_vertices,
    arch_21_determining_translation_vector,
    arch_22_preserved_properties_under_translation,
    arch_23_translation_svg_visual_grid,
    arch_24_word_problem_map_grid_translation,
    arch_25_common_error_translation_sign_trap,
)
from .transformation_geometry_archetypes_26_50 import (
    arch_26_reflection_definition_and_mirror_concept,
    arch_27_reflection_across_vertical_line,
    arch_28_reflection_across_horizontal_line,
    arch_29_reflection_across_y_axis,
    arch_30_reflection_across_x_axis,
    arch_31_reflection_across_line_y_equals_x,
    arch_32_perpendicular_distance_property,
    arch_33_orientation_reversal_lateral_inversion,
    arch_34_finding_mirror_line_from_points,
    arch_35_reflection_svg_visual_grid,
    arch_36_double_reflection_across_parallel_lines,
    arch_37_rotation_definition_and_elements,
    arch_38_rotation_90_degrees_clockwise,
    arch_39_rotation_90_degrees_anticlockwise,
    arch_40_rotation_180_degrees_about_origin,
    arch_41_rotation_about_vertex,
    arch_42_direction_of_rotation_conventions,
    arch_43_preserved_properties_under_rotation,
    arch_44_rotational_symmetry_order_and_angle,
    arch_45_scale_factor_definition_and_formula,
    arch_46_enlargement_side_lengths,
    arch_47_reduction_side_lengths,
    arch_48_effect_of_scale_factor_on_area,
    arch_49_similar_vs_congruent_distinction,
    arch_50_transformation_geometry_comprehensive_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_line_of_symmetry_definition_and_verification": arch_01_line_of_symmetry_definition_and_verification,
    "02_square_lines_of_symmetry": arch_02_square_lines_of_symmetry,
    "03_rectangle_lines_of_symmetry_diagonal_trap": arch_03_rectangle_lines_of_symmetry_diagonal_trap,
    "04_equilateral_triangle_lines_of_symmetry": arch_04_equilateral_triangle_lines_of_symmetry,
    "05_isosceles_triangle_lines_of_symmetry": arch_05_isosceles_triangle_lines_of_symmetry,
    "06_scalene_triangle_lines_of_symmetry": arch_06_scalene_triangle_lines_of_symmetry,
    "07_parallelogram_lines_of_symmetry": arch_07_parallelogram_lines_of_symmetry,
    "08_rhombus_lines_of_symmetry": arch_08_rhombus_lines_of_symmetry,
    "09_kite_lines_of_symmetry": arch_09_kite_lines_of_symmetry,
    "10_isosceles_trapezium_lines_of_symmetry": arch_10_isosceles_trapezium_lines_of_symmetry,
    "11_regular_hexagon_lines_of_symmetry": arch_11_regular_hexagon_lines_of_symmetry,
    "12_circle_lines_of_symmetry": arch_12_circle_lines_of_symmetry,
    "13_completing_symmetric_figure_vertical_line": arch_13_completing_symmetric_figure_vertical_line,
    "14_completing_symmetric_figure_horizontal_line": arch_14_completing_symmetric_figure_horizontal_line,
    "15_translation_concept_and_isometry": arch_15_translation_concept_and_isometry,
    "16_translation_horizontal_units": arch_16_translation_horizontal_units,
    "17_translation_vertical_units": arch_17_translation_vertical_units,
    "18_translation_combined_coordinate_rule": arch_18_translation_combined_coordinate_rule,
    "19_translation_point_from_description": arch_19_translation_point_from_description,
    "20_translation_triangle_vertices": arch_20_translation_triangle_vertices,
    "21_determining_translation_vector": arch_21_determining_translation_vector,
    "22_preserved_properties_under_translation": arch_22_preserved_properties_under_translation,
    "23_translation_svg_visual_grid": arch_23_translation_svg_visual_grid,
    "24_word_problem_map_grid_translation": arch_24_word_problem_map_grid_translation,
    "25_common_error_translation_sign_trap": arch_25_common_error_translation_sign_trap,
    "26_reflection_definition_and_mirror_concept": arch_26_reflection_definition_and_mirror_concept,
    "27_reflection_across_vertical_line": arch_27_reflection_across_vertical_line,
    "28_reflection_across_horizontal_line": arch_28_reflection_across_horizontal_line,
    "29_reflection_across_y_axis": arch_29_reflection_across_y_axis,
    "30_reflection_across_x_axis": arch_30_reflection_across_x_axis,
    "31_reflection_across_line_y_equals_x": arch_31_reflection_across_line_y_equals_x,
    "32_perpendicular_distance_property": arch_32_perpendicular_distance_property,
    "33_orientation_reversal_lateral_inversion": arch_33_orientation_reversal_lateral_inversion,
    "34_finding_mirror_line_from_points": arch_34_finding_mirror_line_from_points,
    "35_reflection_svg_visual_grid": arch_35_reflection_svg_visual_grid,
    "36_double_reflection_across_parallel_lines": arch_36_double_reflection_across_parallel_lines,
    "37_rotation_definition_and_elements": arch_37_rotation_definition_and_elements,
    "38_rotation_90_degrees_clockwise": arch_38_rotation_90_degrees_clockwise,
    "39_rotation_90_degrees_anticlockwise": arch_39_rotation_90_degrees_anticlockwise,
    "40_rotation_180_degrees_about_origin": arch_40_rotation_180_degrees_about_origin,
    "41_rotation_about_vertex": arch_41_rotation_about_vertex,
    "42_direction_of_rotation_conventions": arch_42_direction_of_rotation_conventions,
    "43_preserved_properties_under_rotation": arch_43_preserved_properties_under_rotation,
    "44_rotational_symmetry_order_and_angle": arch_44_rotational_symmetry_order_and_angle,
    "45_scale_factor_definition_and_formula": arch_45_scale_factor_definition_and_formula,
    "46_enlargement_side_lengths": arch_46_enlargement_side_lengths,
    "47_reduction_side_lengths": arch_47_reduction_side_lengths,
    "48_effect_of_scale_factor_on_area": arch_48_effect_of_scale_factor_on_area,
    "49_similar_vs_congruent_distinction": arch_49_similar_vs_congruent_distinction,
    "50_transformation_geometry_comprehensive_autopsy": arch_50_transformation_geometry_comprehensive_autopsy,
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
