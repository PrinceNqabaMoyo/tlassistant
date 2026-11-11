"""Grade 9 Mathematics - Area and Perimeter of 2D Shapes Generator (50 Semantic Archetypes).
========================================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 3 Topic: Area and perimeter of 2D shapes
  - curriculum_docs_auto/Mathematics_Gr9/Term 3/03. Area and perimeter of 2D shapes.md
  - Chapter 14: Squares, rectangles, triangles (acute, right-angled, obtuse), parallelograms,
    rhombi, kites, trapezia, circles, semicircles, quadrants, annuli, sectors, composite figures
    (L-shapes, running tracks, Norman windows, gables), shaded differences, unit conversions
    (linear, area, hectares), scaling factor effects ($k$ and $k^2$), real-world SA applications
    (fencing, tiling, painting), and diagnostic error analysis.

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from .area_perimeter_2d_archetypes_01_25 import (
    arch_01_perimeter_of_rectangles_and_squares,
    arch_02_area_of_squares_and_rectangles,
    arch_03_find_missing_dimension_given_area_or_perimeter,
    arch_04_perimeter_of_triangles_all_types,
    arch_05_area_of_right_angled_triangles,
    arch_06_area_of_acute_triangles_given_base_and_height,
    arch_07_area_of_obtuse_triangles_external_altitude,
    arch_08_find_base_or_height_of_triangle_given_area,
    arch_09_perimeter_of_parallelogram_and_rhombus,
    arch_10_area_of_parallelogram_base_times_height,
    arch_11_find_perpendicular_height_of_parallelogram,
    arch_12_area_of_rhombus_using_diagonals,
    arch_13_area_of_kite_using_diagonals,
    arch_14_find_missing_diagonal_of_rhombus_or_kite,
    arch_15_area_of_trapezium_parallel_sides_and_height,
    arch_16_find_height_or_parallel_side_of_trapezium,
    arch_17_circumference_of_circle_given_radius_or_diameter,
    arch_18_find_radius_or_diameter_given_circumference,
    arch_19_perimeter_of_semicircle_curved_plus_diameter,
    arch_20_perimeter_of_quarter_circle_quadrant,
    arch_21_area_of_circle_given_radius,
    arch_22_area_of_circle_given_diameter,
    arch_23_find_radius_of_circle_given_area,
    arch_24_area_of_semicircle,
    arch_25_area_of_quarter_circle_quadrant,
)
from .area_perimeter_2d_archetypes_26_50 import (
    arch_26_area_of_circular_ring_annulus_washer,
    arch_27_arc_length_of_circle_sector,
    arch_28_area_of_circle_sector,
    arch_29_perimeter_of_l_shaped_composite_figure,
    arch_30_area_of_l_shaped_composite_figure,
    arch_31_area_of_t_shaped_or_u_shaped_composite_polygon,
    arch_32_composite_rectangle_with_triangular_gable_area,
    arch_33_composite_rectangle_with_semicircular_end_perimeter,
    arch_34_composite_rectangle_with_semicircular_end_area,
    arch_35_shaded_area_square_minus_inscribed_circle,
    arch_36_shaded_area_circle_minus_inscribed_square,
    arch_37_shaded_area_rectangle_minus_internal_rectangle_path,
    arch_38_linear_unit_conversion_mm_cm_m_km,
    arch_39_area_unit_conversion_mm2_to_cm2_and_m2,
    arch_40_area_unit_conversion_m2_to_hectares_and_km2,
    arch_41_effect_of_scaling_dimensions_by_k_on_perimeter,
    arch_42_effect_of_scaling_dimensions_by_k_on_area,
    arch_43_calculate_scale_factor_given_ratio_of_areas,
    arch_44_contextual_fencing_cost_perimeter_application,
    arch_45_contextual_turfing_or_tiling_cost_area_application,
    arch_46_contextual_painting_walls_deducting_doors_windows,
    arch_47_error_analysis_confusing_perimeter_and_area,
    arch_48_error_analysis_slanted_side_used_as_perpendicular_height,
    arch_49_error_analysis_forgetting_flat_base_in_semicircle_perimeter,
    arch_50_compound_multi_stage_park_layout_synthesis,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_perimeter_of_rectangles_and_squares": arch_01_perimeter_of_rectangles_and_squares,
    "02_area_of_squares_and_rectangles": arch_02_area_of_squares_and_rectangles,
    "03_find_missing_dimension_given_area_or_perimeter": arch_03_find_missing_dimension_given_area_or_perimeter,
    "04_perimeter_of_triangles_all_types": arch_04_perimeter_of_triangles_all_types,
    "05_area_of_right_angled_triangles": arch_05_area_of_right_angled_triangles,
    "06_area_of_acute_triangles_given_base_and_height": arch_06_area_of_acute_triangles_given_base_and_height,
    "07_area_of_obtuse_triangles_external_altitude": arch_07_area_of_obtuse_triangles_external_altitude,
    "08_find_base_or_height_of_triangle_given_area": arch_08_find_base_or_height_of_triangle_given_area,
    "09_perimeter_of_parallelogram_and_rhombus": arch_09_perimeter_of_parallelogram_and_rhombus,
    "10_area_of_parallelogram_base_times_height": arch_10_area_of_parallelogram_base_times_height,
    "11_find_perpendicular_height_of_parallelogram": arch_11_find_perpendicular_height_of_parallelogram,
    "12_area_of_rhombus_using_diagonals": arch_12_area_of_rhombus_using_diagonals,
    "13_area_of_kite_using_diagonals": arch_13_area_of_kite_using_diagonals,
    "14_find_missing_diagonal_of_rhombus_or_kite": arch_14_find_missing_diagonal_of_rhombus_or_kite,
    "15_area_of_trapezium_parallel_sides_and_height": arch_15_area_of_trapezium_parallel_sides_and_height,
    "16_find_height_or_parallel_side_of_trapezium": arch_16_find_height_or_parallel_side_of_trapezium,
    "17_circumference_of_circle_given_radius_or_diameter": arch_17_circumference_of_circle_given_radius_or_diameter,
    "18_find_radius_or_diameter_given_circumference": arch_18_find_radius_or_diameter_given_circumference,
    "19_perimeter_of_semicircle_curved_plus_diameter": arch_19_perimeter_of_semicircle_curved_plus_diameter,
    "20_perimeter_of_quarter_circle_quadrant": arch_20_perimeter_of_quarter_circle_quadrant,
    "21_area_of_circle_given_radius": arch_21_area_of_circle_given_radius,
    "22_area_of_circle_given_diameter": arch_22_area_of_circle_given_diameter,
    "23_find_radius_of_circle_given_area": arch_23_find_radius_of_circle_given_area,
    "24_area_of_semicircle": arch_24_area_of_semicircle,
    "25_area_of_quarter_circle_quadrant": arch_25_area_of_quarter_circle_quadrant,
    "26_area_of_circular_ring_annulus_washer": arch_26_area_of_circular_ring_annulus_washer,
    "27_arc_length_of_circle_sector": arch_27_arc_length_of_circle_sector,
    "28_area_of_circle_sector": arch_28_area_of_circle_sector,
    "29_perimeter_of_l_shaped_composite_figure": arch_29_perimeter_of_l_shaped_composite_figure,
    "30_area_of_l_shaped_composite_figure": arch_30_area_of_l_shaped_composite_figure,
    "31_area_of_t_shaped_or_u_shaped_composite_polygon": arch_31_area_of_t_shaped_or_u_shaped_composite_polygon,
    "32_composite_rectangle_with_triangular_gable_area": arch_32_composite_rectangle_with_triangular_gable_area,
    "33_composite_rectangle_with_semicircular_end_perimeter": arch_33_composite_rectangle_with_semicircular_end_perimeter,
    "34_composite_rectangle_with_semicircular_end_area": arch_34_composite_rectangle_with_semicircular_end_area,
    "35_shaded_area_square_minus_inscribed_circle": arch_35_shaded_area_square_minus_inscribed_circle,
    "36_shaded_area_circle_minus_inscribed_square": arch_36_shaded_area_circle_minus_inscribed_square,
    "37_shaded_area_rectangle_minus_internal_rectangle_path": arch_37_shaded_area_rectangle_minus_internal_rectangle_path,
    "38_linear_unit_conversion_mm_cm_m_km": arch_38_linear_unit_conversion_mm_cm_m_km,
    "39_area_unit_conversion_mm2_to_cm2_and_m2": arch_39_area_unit_conversion_mm2_to_cm2_and_m2,
    "40_area_unit_conversion_m2_to_hectares_and_km2": arch_40_area_unit_conversion_m2_to_hectares_and_km2,
    "41_effect_of_scaling_dimensions_by_k_on_perimeter": arch_41_effect_of_scaling_dimensions_by_k_on_perimeter,
    "42_effect_of_scaling_dimensions_by_k_on_area": arch_42_effect_of_scaling_dimensions_by_k_on_area,
    "43_calculate_scale_factor_given_ratio_of_areas": arch_43_calculate_scale_factor_given_ratio_of_areas,
    "44_contextual_fencing_cost_perimeter_application": arch_44_contextual_fencing_cost_perimeter_application,
    "45_contextual_turfing_or_tiling_cost_area_application": arch_45_contextual_turfing_or_tiling_cost_area_application,
    "46_contextual_painting_walls_deducting_doors_windows": arch_46_contextual_painting_walls_deducting_doors_windows,
    "47_error_analysis_confusing_perimeter_and_area": arch_47_error_analysis_confusing_perimeter_and_area,
    "48_error_analysis_slanted_side_used_as_perpendicular_height": arch_48_error_analysis_slanted_side_used_as_perpendicular_height,
    "49_error_analysis_forgetting_flat_base_in_semicircle_perimeter": arch_49_error_analysis_forgetting_flat_base_in_semicircle_perimeter,
    "50_compound_multi_stage_park_layout_synthesis": arch_50_compound_multi_stage_park_layout_synthesis,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

SUBSKILLS_TUPLES: List[Tuple[str, str]] = [
    (key, key[3:].replace("_", " ").title()) for key in SUBSKILLS
]


def generate_grade9_area_perimeter_2d_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Area and perimeter of 2D shapes question."""
    r = random.Random(seed)
    if subskill and subskill in ARCHETYPE_MAP:
        builder = ARCHETYPE_MAP[subskill]
        chosen_subskill = subskill
    elif subskill:
        # Match by prefix or substring if requested
        s_clean = str(subskill).strip()
        matched = None
        for k, b in ARCHETYPE_MAP.items():
            if k.startswith(s_clean) or s_clean in k:
                matched = (k, b)
                break
        if matched:
            chosen_subskill, builder = matched
        else:
            chosen_subskill = r.choice(SUBSKILLS)
            builder = ARCHETYPE_MAP[chosen_subskill]
    else:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(r)
    q["subskill"] = chosen_subskill
    q["grade"] = "9"
    q["subject"] = "Mathematics"
    q["topic"] = "Area and perimeter of 2D shapes"
    q["term"] = 3
    q.setdefault("caps_weight_percent", 12)
    q.setdefault("suggested_duration_mins", 4)
    q.setdefault("difficulty", "medium")
    q.setdefault("mode", "compound")
    if not q.get("prompt"):
        q["prompt"] = q.get("question_text")
    if not q.get("sample_answer"):
        q["sample_answer"] = str(q.get("correct_answer"))
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
        q = generate_grade9_area_perimeter_2d_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
