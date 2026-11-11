"""Grade 9 Mathematics - Transformation Geometry Generator (50 Semantic Archetypes).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 3/01. Transformation geometry.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .transformation_geometry_archetypes_01_25 import (
    arch_01_symmetry_lines_regular_polygons,
    arch_02_symmetry_lines_quadrilaterals,
    arch_03_rotational_symmetry_order,
    arch_04_translation_point_single_axis,
    arch_05_translation_point_both_axes,
    arch_06_translation_find_vector,
    arch_07_translation_find_preimage,
    arch_08_translation_triangle_vertices,
    arch_09_translation_properties_isometry,
    arch_10_reflection_point_x_axis,
    arch_11_reflection_point_y_axis,
    arch_12_reflection_point_line_y_equals_x,
    arch_13_reflection_point_line_y_equals_neg_x,
    arch_14_reflection_point_horizontal_line,
    arch_15_reflection_point_vertical_line,
    arch_16_reflection_triangle_x_axis,
    arch_17_reflection_triangle_y_axis,
    arch_18_reflection_triangle_line_y_equals_x,
    arch_19_reflection_identify_mirror_line,
    arch_20_reflection_perpendicular_bisector,
    arch_21_rotation_point_origin_90_clockwise,
    arch_22_rotation_point_origin_90_anticlockwise,
    arch_23_rotation_point_origin_180,
    arch_24_rotation_triangle_origin_90_cw,
    arch_25_rotation_triangle_origin_90_ccw,
)
from .transformation_geometry_archetypes_26_50 import (
    arch_26_rotation_triangle_origin_180,
    arch_27_rotation_identify_angle_direction,
    arch_28_rotation_about_point_not_origin,
    arch_29_enlargement_point_origin,
    arch_30_reduction_point_origin,
    arch_31_enlargement_find_scale_factor,
    arch_32_enlargement_triangle_vertices,
    arch_33_reduction_triangle_vertices,
    arch_34_enlargement_side_lengths,
    arch_35_enlargement_perimeter_effect,
    arch_36_enlargement_area_factor_k_squared,
    arch_37_enlargement_find_area_given_original,
    arch_38_enlargement_find_original_area,
    arch_39_enlargement_find_k_from_areas,
    arch_40_enlargement_ratio_of_areas,
    arch_41_enlargement_angle_invariance,
    arch_42_composite_reflection_then_translation,
    arch_43_composite_translation_then_reflection,
    arch_44_composite_double_reflection_parallel_axes,
    arch_45_composite_double_reflection_perpendicular_axes,
    arch_46_composite_rotation_then_translation,
    arch_47_identify_transformation_type,
    arch_48_invariant_points_lines,
    arch_49_isometry_congruence_vs_similarity,
    arch_50_coordinate_mapping_notation_algebraic_rule,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random, int], Dict[str, Any]]] = {
    "01_symmetry_lines_regular_polygons": arch_01_symmetry_lines_regular_polygons,
    "02_symmetry_lines_quadrilaterals": arch_02_symmetry_lines_quadrilaterals,
    "03_rotational_symmetry_order": arch_03_rotational_symmetry_order,
    "04_translation_point_single_axis": arch_04_translation_point_single_axis,
    "05_translation_point_both_axes": arch_05_translation_point_both_axes,
    "06_translation_find_vector": arch_06_translation_find_vector,
    "07_translation_find_preimage": arch_07_translation_find_preimage,
    "08_translation_triangle_vertices": arch_08_translation_triangle_vertices,
    "09_translation_properties_isometry": arch_09_translation_properties_isometry,
    "10_reflection_point_x_axis": arch_10_reflection_point_x_axis,
    "11_reflection_point_y_axis": arch_11_reflection_point_y_axis,
    "12_reflection_point_line_y_equals_x": arch_12_reflection_point_line_y_equals_x,
    "13_reflection_point_line_y_equals_neg_x": arch_13_reflection_point_line_y_equals_neg_x,
    "14_reflection_point_horizontal_line": arch_14_reflection_point_horizontal_line,
    "15_reflection_point_vertical_line": arch_15_reflection_point_vertical_line,
    "16_reflection_triangle_x_axis": arch_16_reflection_triangle_x_axis,
    "17_reflection_triangle_y_axis": arch_17_reflection_triangle_y_axis,
    "18_reflection_triangle_line_y_equals_x": arch_18_reflection_triangle_line_y_equals_x,
    "19_reflection_identify_mirror_line": arch_19_reflection_identify_mirror_line,
    "20_reflection_perpendicular_bisector": arch_20_reflection_perpendicular_bisector,
    "21_rotation_point_origin_90_clockwise": arch_21_rotation_point_origin_90_clockwise,
    "22_rotation_point_origin_90_anticlockwise": arch_22_rotation_point_origin_90_anticlockwise,
    "23_rotation_point_origin_180": arch_23_rotation_point_origin_180,
    "24_rotation_triangle_origin_90_cw": arch_24_rotation_triangle_origin_90_cw,
    "25_rotation_triangle_origin_90_ccw": arch_25_rotation_triangle_origin_90_ccw,
    "26_rotation_triangle_origin_180": arch_26_rotation_triangle_origin_180,
    "27_rotation_identify_angle_direction": arch_27_rotation_identify_angle_direction,
    "28_rotation_about_point_not_origin": arch_28_rotation_about_point_not_origin,
    "29_enlargement_point_origin": arch_29_enlargement_point_origin,
    "30_reduction_point_origin": arch_30_reduction_point_origin,
    "31_enlargement_find_scale_factor": arch_31_enlargement_find_scale_factor,
    "32_enlargement_triangle_vertices": arch_32_enlargement_triangle_vertices,
    "33_reduction_triangle_vertices": arch_33_reduction_triangle_vertices,
    "34_enlargement_side_lengths": arch_34_enlargement_side_lengths,
    "35_enlargement_perimeter_effect": arch_35_enlargement_perimeter_effect,
    "36_enlargement_area_factor_k_squared": arch_36_enlargement_area_factor_k_squared,
    "37_enlargement_find_area_given_original": arch_37_enlargement_find_area_given_original,
    "38_enlargement_find_original_area": arch_38_enlargement_find_original_area,
    "39_enlargement_find_k_from_areas": arch_39_enlargement_find_k_from_areas,
    "40_enlargement_ratio_of_areas": arch_40_enlargement_ratio_of_areas,
    "41_enlargement_angle_invariance": arch_41_enlargement_angle_invariance,
    "42_composite_reflection_then_translation": arch_42_composite_reflection_then_translation,
    "43_composite_translation_then_reflection": arch_43_composite_translation_then_reflection,
    "44_composite_double_reflection_parallel_axes": arch_44_composite_double_reflection_parallel_axes,
    "45_composite_double_reflection_perpendicular_axes": arch_45_composite_double_reflection_perpendicular_axes,
    "46_composite_rotation_then_translation": arch_46_composite_rotation_then_translation,
    "47_identify_transformation_type": arch_47_identify_transformation_type,
    "48_invariant_points_lines": arch_48_invariant_points_lines,
    "49_isometry_congruence_vs_similarity": arch_49_isometry_congruence_vs_similarity,
    "50_coordinate_mapping_notation_algebraic_rule": arch_50_coordinate_mapping_notation_algebraic_rule,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
SUBSKILLS_TUPLES = [(k, k.replace("_", " ").title()) for k in SUBSKILLS]


def generate_grade9_transformation_geometry_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single Grade 9 Transformation Geometry question."""
    if seed is None:
        seed = random.randint(1, 1_000_000_000)
    rng = random.Random(seed)

    if subskill and subskill in ARCHETYPE_MAP:
        builder = ARCHETYPE_MAP[subskill]
        chosen_subskill = subskill
    else:
        chosen_subskill = rng.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(rng, seed)

    # Attach CAPS & Fundile platform metadata
    q["seed"] = seed
    q["grade"] = 9
    q["term"] = 3
    q["subject"] = "Mathematics"
    q["topic"] = "Transformation geometry"
    q["topic_slug"] = "grade9_math_transformation_geometry"
    q["subskill"] = chosen_subskill

    # Synchronize prompt fields
    if "question_text" in q and "prompt" not in q:
        q["prompt"] = q["question_text"]
    elif "prompt" in q and "question_text" not in q:
        q["question_text"] = q["prompt"]

    # Sync answer aliases
    if "correct_answer" in q:
        q["correct_value"] = q["correct_answer"]
        q["expected_answer"] = q["correct_answer"]
    elif "correct_value" in q:
        q["correct_answer"] = q["correct_value"]
        q["expected_answer"] = q["correct_value"]

    # Worked solution from hints or marking schema
    hints = q.get("hints", [])
    if hints and "sample_answer" not in q:
        q["sample_answer"] = hints[-1]
    if hints and "worked_solution" not in q:
        q["worked_solution"] = "\n".join(hints)

    schema = q.get("marking_schema")
    if isinstance(schema, list) and "marks" not in q:
        q["marks"] = sum(p.get("marks", 1) for p in schema if isinstance(p, dict)) or 2
    elif "marks" not in q:
        q["marks"] = 2

    q.setdefault("caps_weight_percent", 10)
    q.setdefault("suggested_duration_mins", 3)
    q.setdefault("mode", "compound")
    q.setdefault("difficulty", "medium")

    return q


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
        q = generate_grade9_transformation_geometry_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
