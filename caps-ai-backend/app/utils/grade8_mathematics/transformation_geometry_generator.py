"""Grade 8 Mathematics — Transformation Geometry Generator.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 3/01. Transformation geometry.md

Expanded to 50 distinct semantic archetypes covering:
  - Lines of symmetry: quadrilaterals, triangles, regular polygons.
  - Reflections: x-axis, y-axis, line y=x, triangle reflections, invariant points.
  - Translations: horizontal, vertical, vector combinations, triangle mapping, inverse translations.
  - Rotations: 90° clockwise, 90° counter-clockwise, 180°, triangle rotations, order/angle of symmetry.
  - Enlargements and reductions (dilations): scale factor k, coordinate dilations, perimeter (k), area (k²), similarity.
  - Composite transformations, isometries, error analysis, tessellations, applications.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .transformation_geometry_archetypes_01_25 import (
    arch_01_identify_lines_of_symmetry_quadrilaterals,
    arch_02_identify_lines_of_symmetry_triangles,
    arch_03_identify_lines_of_symmetry_regular_polygons,
    arch_04_reflection_across_x_axis_single_point,
    arch_05_reflection_across_y_axis_single_point,
    arch_06_reflection_across_line_y_equals_x,
    arch_07_reflection_triangle_across_x_axis_vertices,
    arch_08_reflection_triangle_across_y_axis_vertices,
    arch_09_reflection_identify_mirror_line_from_coordinates,
    arch_10_reflection_invariant_points_on_mirror_line,
    arch_11_translation_horizontal_units_rule,
    arch_12_translation_vertical_units_rule,
    arch_13_translation_combined_vector_rule,
    arch_14_translation_apply_rule_to_triangle_vertices,
    arch_15_translation_determine_rule_from_point_and_image,
    arch_16_translation_inverse_find_original_from_image,
    arch_17_translation_preservation_of_congruence,
    arch_18_translation_word_problem_movement_on_grid,
    arch_19_translation_parallelogram_coordinates,
    arch_20_translation_coordinate_mapping_algebraic_notation,
    arch_21_rotation_90_degrees_clockwise_origin,
    arch_22_rotation_90_degrees_counter_clockwise_origin,
    arch_23_rotation_180_degrees_origin_half_turn,
    arch_24_rotation_triangle_vertices_90_clockwise,
    arch_25_rotation_triangle_vertices_180_degrees,
)
from .transformation_geometry_archetypes_26_50 import (
    arch_26_rotation_identify_angle_and_direction_from_coordinates,
    arch_27_rotation_invariant_center_point,
    arch_28_rotation_quadrant_location_after_turn,
    arch_29_rotation_order_of_rotational_symmetry_2d_shapes,
    arch_30_rotation_angle_of_rotational_symmetry_calculation,
    arch_31_enlargement_scale_factor_coordinates_origin,
    arch_32_reduction_scale_factor_coordinates_origin,
    arch_33_enlargement_triangle_vertices_scale_factor_2,
    arch_34_reduction_triangle_vertices_fractional_scale_factor,
    arch_35_determine_scale_factor_from_original_and_image_lengths,
    arch_36_determine_scale_factor_from_coordinates,
    arch_37_enlargement_perimeter_relationship_k,
    arch_38_enlargement_area_relationship_k_squared,
    arch_39_reduction_area_relationship_k_squared,
    arch_40_similar_figures_properties_angles_equal_sides_proportional,
    arch_41_composite_translation_then_reflection_across_x_axis,
    arch_42_composite_reflection_then_translation,
    arch_43_composite_rotation_180_then_translation,
    arch_44_identify_transformation_type_from_coordinate_rule,
    arch_45_congruence_vs_similarity_classification_table,
    arch_46_isometry_definition_and_properties,
    arch_47_coordinate_geometry_distance_after_translation,
    arch_48_transformation_error_analysis_incorrect_reflection_sign,
    arch_49_tessellation_basic_patterns_using_translations,
    arch_50_transformation_word_problem_computer_graphics_scaling,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_identify_lines_of_symmetry_quadrilaterals": arch_01_identify_lines_of_symmetry_quadrilaterals,
    "02_identify_lines_of_symmetry_triangles": arch_02_identify_lines_of_symmetry_triangles,
    "03_identify_lines_of_symmetry_regular_polygons": arch_03_identify_lines_of_symmetry_regular_polygons,
    "04_reflection_across_x_axis_single_point": arch_04_reflection_across_x_axis_single_point,
    "05_reflection_across_y_axis_single_point": arch_05_reflection_across_y_axis_single_point,
    "06_reflection_across_line_y_equals_x": arch_06_reflection_across_line_y_equals_x,
    "07_reflection_triangle_across_x_axis_vertices": arch_07_reflection_triangle_across_x_axis_vertices,
    "08_reflection_triangle_across_y_axis_vertices": arch_08_reflection_triangle_across_y_axis_vertices,
    "09_reflection_identify_mirror_line_from_coordinates": arch_09_reflection_identify_mirror_line_from_coordinates,
    "10_reflection_invariant_points_on_mirror_line": arch_10_reflection_invariant_points_on_mirror_line,
    "11_translation_horizontal_units_rule": arch_11_translation_horizontal_units_rule,
    "12_translation_vertical_units_rule": arch_12_translation_vertical_units_rule,
    "13_translation_combined_vector_rule": arch_13_translation_combined_vector_rule,
    "14_translation_apply_rule_to_triangle_vertices": arch_14_translation_apply_rule_to_triangle_vertices,
    "15_translation_determine_rule_from_point_and_image": arch_15_translation_determine_rule_from_point_and_image,
    "16_translation_inverse_find_original_from_image": arch_16_translation_inverse_find_original_from_image,
    "17_translation_preservation_of_congruence": arch_17_translation_preservation_of_congruence,
    "18_translation_word_problem_movement_on_grid": arch_18_translation_word_problem_movement_on_grid,
    "19_translation_parallelogram_coordinates": arch_19_translation_parallelogram_coordinates,
    "20_translation_coordinate_mapping_algebraic_notation": arch_20_translation_coordinate_mapping_algebraic_notation,
    "21_rotation_90_degrees_clockwise_origin": arch_21_rotation_90_degrees_clockwise_origin,
    "22_rotation_90_degrees_counter_clockwise_origin": arch_22_rotation_90_degrees_counter_clockwise_origin,
    "23_rotation_180_degrees_origin_half_turn": arch_23_rotation_180_degrees_origin_half_turn,
    "24_rotation_triangle_vertices_90_clockwise": arch_24_rotation_triangle_vertices_90_clockwise,
    "25_rotation_triangle_vertices_180_degrees": arch_25_rotation_triangle_vertices_180_degrees,
    "26_rotation_identify_angle_and_direction_from_coordinates": arch_26_rotation_identify_angle_and_direction_from_coordinates,
    "27_rotation_invariant_center_point": arch_27_rotation_invariant_center_point,
    "28_rotation_quadrant_location_after_turn": arch_28_rotation_quadrant_location_after_turn,
    "29_rotation_order_of_rotational_symmetry_2d_shapes": arch_29_rotation_order_of_rotational_symmetry_2d_shapes,
    "30_rotation_angle_of_rotational_symmetry_calculation": arch_30_rotation_angle_of_rotational_symmetry_calculation,
    "31_enlargement_scale_factor_coordinates_origin": arch_31_enlargement_scale_factor_coordinates_origin,
    "32_reduction_scale_factor_coordinates_origin": arch_32_reduction_scale_factor_coordinates_origin,
    "33_enlargement_triangle_vertices_scale_factor_2": arch_33_enlargement_triangle_vertices_scale_factor_2,
    "34_reduction_triangle_vertices_fractional_scale_factor": arch_34_reduction_triangle_vertices_fractional_scale_factor,
    "35_determine_scale_factor_from_original_and_image_lengths": arch_35_determine_scale_factor_from_original_and_image_lengths,
    "36_determine_scale_factor_from_coordinates": arch_36_determine_scale_factor_from_coordinates,
    "37_enlargement_perimeter_relationship_k": arch_37_enlargement_perimeter_relationship_k,
    "38_enlargement_area_relationship_k_squared": arch_38_enlargement_area_relationship_k_squared,
    "39_reduction_area_relationship_k_squared": arch_39_reduction_area_relationship_k_squared,
    "40_similar_figures_properties_angles_equal_sides_proportional": arch_40_similar_figures_properties_angles_equal_sides_proportional,
    "41_composite_translation_then_reflection_across_x_axis": arch_41_composite_translation_then_reflection_across_x_axis,
    "42_composite_reflection_then_translation": arch_42_composite_reflection_then_translation,
    "43_composite_rotation_180_then_translation": arch_43_composite_rotation_180_then_translation,
    "44_identify_transformation_type_from_coordinate_rule": arch_44_identify_transformation_type_from_coordinate_rule,
    "45_congruence_vs_similarity_classification_table": arch_45_congruence_vs_similarity_classification_table,
    "46_isometry_definition_and_properties": arch_46_isometry_definition_and_properties,
    "47_coordinate_geometry_distance_after_translation": arch_47_coordinate_geometry_distance_after_translation,
    "48_transformation_error_analysis_incorrect_reflection_sign": arch_48_transformation_error_analysis_incorrect_reflection_sign,
    "49_tessellation_basic_patterns_using_translations": arch_49_tessellation_basic_patterns_using_translations,
    "50_transformation_word_problem_computer_graphics_scaling": arch_50_transformation_word_problem_computer_graphics_scaling,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())


def generate_grade8_transformation_geometry_question(
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
    q_data["topic"] = "Transformation geometry"
    q_data["term"] = 3
    q_data["caps_weight_percent"] = 8
    q_data["suggested_duration_mins"] = 3
    q_data["difficulty"] = difficulty
    q_data["mode"] = mode
    q_data["subskill"] = target_subskill

    if "marking_schema" not in q_data:
        m = q_data.get("marks", 2)
        q_data["marking_schema"] = {
            "total_marks": m,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct transformation rule, property, or formula setup", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate coordinates, explanation, or calculation", "marks": m - 1, "editable": True},
            ],
            "deductions": [{"rule": "incorrect_sign_or_coordinate_swap", "penalty": 1}],
            "carry_forward_rule": "consequential_accuracy",
        }

    return q_data


generate = generate_grade8_transformation_geometry_question
generate_grade8_transformations_question = generate_grade8_transformation_geometry_question
