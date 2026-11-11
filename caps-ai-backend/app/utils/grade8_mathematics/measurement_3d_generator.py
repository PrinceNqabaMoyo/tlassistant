"""Grade 8 Mathematics — Surface Area and Volume of 3D Objects Generator.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 4/01. Surface area and volume of 3D objects.md

Expanded to 50 distinct semantic archetypes covering:
  - Surface area and volume concepts and distinctions.
  - Cubes: surface area (closed, open), side from SA, volume, side from volume (cube root).
  - Rectangular prisms: surface area (closed, open, perimeter formula), volume, missing dimensions.
  - Triangular prisms: right-angled, isosceles, equilateral base SA and Volume; missing dimensions.
  - Unfoldings: surface area of cubes, rectangular prisms, triangular prisms from flat face layouts.
  - Conversions: cm³ <-> mm³, m³ <-> cm³, mixed unit addition.
  - Capacity: ml, litres, kilolitres; fish tanks, pools, hollow containers with wall thickness.
  - Water displacement: submerged stones, water level rises.
  - Scaling: doubling dimensions (SA ×4, Vol ×8), tripling dimensions (Vol ×27).
  - Synthesis: same volume different SA; composite shapes (cube glued to prism, L-shaped steps).
  - Practical contexts: room painting, packaging cubes in cartons, tap flow rates.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .measurement_3d_archetypes_01_25 import (
    arch_01_concept_surface_area_vs_volume_definition_distinction,
    arch_02_cube_surface_area_given_side_length,
    arch_03_cube_surface_area_open_top_five_faces,
    arch_04_cube_find_side_length_from_surface_area,
    arch_05_cube_volume_given_side_length,
    arch_06_cube_find_side_length_from_volume_cube_root,
    arch_07_rectangular_prism_surface_area_integer_dimensions,
    arch_08_rectangular_prism_surface_area_open_top_box,
    arch_09_rectangular_prism_surface_area_base_perimeter_formula,
    arch_10_rectangular_prism_volume_integer_dimensions,
    arch_11_rectangular_prism_find_height_given_volume_length_breadth,
    arch_12_rectangular_prism_find_breadth_given_volume_length_height,
    arch_13_triangular_prism_right_angled_base_surface_area,
    arch_14_triangular_prism_isosceles_base_surface_area,
    arch_15_triangular_prism_equilateral_base_surface_area,
    arch_16_triangular_prism_right_angled_base_volume,
    arch_17_triangular_prism_isosceles_base_volume,
    arch_18_triangular_prism_find_height_given_volume_and_base_area,
    arch_19_triangular_prism_find_triangle_height_given_volume_and_base_length,
    arch_20_triangular_prism_distinguish_triangle_height_vs_prism_height,
    arch_21_net_of_cube_calculate_surface_area_from_faces,
    arch_22_net_of_rectangular_prism_calculate_surface_area_from_faces,
    arch_23_net_of_triangular_prism_calculate_surface_area_from_faces,
    arch_24_convert_cubic_cm_to_cubic_mm,
    arch_25_convert_cubic_mm_to_cubic_cm,
)
from .measurement_3d_archetypes_26_50 import (
    arch_26_convert_cubic_m_to_cubic_cm,
    arch_27_convert_cubic_cm_to_cubic_m,
    arch_28_convert_mixed_cubic_units_addition,
    arch_29_capacity_definition_and_relation_to_volume,
    arch_30_convert_cubic_cm_to_millilitres,
    arch_31_convert_cubic_cm_to_litres,
    arch_32_convert_litres_to_cubic_cm,
    arch_33_convert_cubic_m_to_kilolitres,
    arch_34_convert_kilolitres_to_litres,
    arch_35_capacity_fish_tank_volume_in_litres,
    arch_36_capacity_swimming_pool_volume_in_kilolitres,
    arch_37_internal_vs_external_dimensions_wall_thickness,
    arch_38_hollow_container_capacity_given_wall_thickness,
    arch_39_water_displacement_by_submerged_solid_object,
    arch_40_water_level_rise_in_rectangular_container_from_added_object,
    arch_41_doubling_side_of_cube_effect_on_surface_area_fourfold,
    arch_42_doubling_side_of_cube_effect_on_volume_eightfold,
    arch_43_tripling_dimensions_of_rectangular_prism_effect_on_volume,
    arch_44_same_volume_different_surface_areas_comparison_table,
    arch_45_composite_object_cube_glued_to_rectangular_prism_volume,
    arch_46_composite_object_cube_glued_to_rectangular_prism_surface_area,
    arch_47_composite_object_l_shaped_prism_volume,
    arch_48_cost_of_painting_walls_and_ceiling_of_room_surface_area,
    arch_49_packaging_number_of_small_cubes_fitting_into_large_box,
    arch_50_rate_of_filling_tank_with_water_given_tap_flow_rate,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_concept_surface_area_vs_volume_definition_distinction": arch_01_concept_surface_area_vs_volume_definition_distinction,
    "02_cube_surface_area_given_side_length": arch_02_cube_surface_area_given_side_length,
    "03_cube_surface_area_open_top_five_faces": arch_03_cube_surface_area_open_top_five_faces,
    "04_cube_find_side_length_from_surface_area": arch_04_cube_find_side_length_from_surface_area,
    "05_cube_volume_given_side_length": arch_05_cube_volume_given_side_length,
    "06_cube_find_side_length_from_volume_cube_root": arch_06_cube_find_side_length_from_volume_cube_root,
    "07_rectangular_prism_surface_area_integer_dimensions": arch_07_rectangular_prism_surface_area_integer_dimensions,
    "08_rectangular_prism_surface_area_open_top_box": arch_08_rectangular_prism_surface_area_open_top_box,
    "09_rectangular_prism_surface_area_base_perimeter_formula": arch_09_rectangular_prism_surface_area_base_perimeter_formula,
    "10_rectangular_prism_volume_integer_dimensions": arch_10_rectangular_prism_volume_integer_dimensions,
    "11_rectangular_prism_find_height_given_volume_length_breadth": arch_11_rectangular_prism_find_height_given_volume_length_breadth,
    "12_rectangular_prism_find_breadth_given_volume_length_height": arch_12_rectangular_prism_find_breadth_given_volume_length_height,
    "13_triangular_prism_right_angled_base_surface_area": arch_13_triangular_prism_right_angled_base_surface_area,
    "14_triangular_prism_isosceles_base_surface_area": arch_14_triangular_prism_isosceles_base_surface_area,
    "15_triangular_prism_equilateral_base_surface_area": arch_15_triangular_prism_equilateral_base_surface_area,
    "16_triangular_prism_right_angled_base_volume": arch_16_triangular_prism_right_angled_base_volume,
    "17_triangular_prism_isosceles_base_volume": arch_17_triangular_prism_isosceles_base_volume,
    "18_triangular_prism_find_height_given_volume_and_base_area": arch_18_triangular_prism_find_height_given_volume_and_base_area,
    "19_triangular_prism_find_triangle_height_given_volume_and_base_length": arch_19_triangular_prism_find_triangle_height_given_volume_and_base_length,
    "20_triangular_prism_distinguish_triangle_height_vs_prism_height": arch_20_triangular_prism_distinguish_triangle_height_vs_prism_height,
    "21_net_of_cube_calculate_surface_area_from_faces": arch_21_net_of_cube_calculate_surface_area_from_faces,
    "22_net_of_rectangular_prism_calculate_surface_area_from_faces": arch_22_net_of_rectangular_prism_calculate_surface_area_from_faces,
    "23_net_of_triangular_prism_calculate_surface_area_from_faces": arch_23_net_of_triangular_prism_calculate_surface_area_from_faces,
    "24_convert_cubic_cm_to_cubic_mm": arch_24_convert_cubic_cm_to_cubic_mm,
    "25_convert_cubic_mm_to_cubic_cm": arch_25_convert_cubic_mm_to_cubic_cm,
    "26_convert_cubic_m_to_cubic_cm": arch_26_convert_cubic_m_to_cubic_cm,
    "27_convert_cubic_cm_to_cubic_m": arch_27_convert_cubic_cm_to_cubic_m,
    "28_convert_mixed_cubic_units_addition": arch_28_convert_mixed_cubic_units_addition,
    "29_capacity_definition_and_relation_to_volume": arch_29_capacity_definition_and_relation_to_volume,
    "30_convert_cubic_cm_to_millilitres": arch_30_convert_cubic_cm_to_millilitres,
    "31_convert_cubic_cm_to_litres": arch_31_convert_cubic_cm_to_litres,
    "32_convert_litres_to_cubic_cm": arch_32_convert_litres_to_cubic_cm,
    "33_convert_cubic_m_to_kilolitres": arch_33_convert_cubic_m_to_kilolitres,
    "34_convert_kilolitres_to_litres": arch_34_convert_kilolitres_to_litres,
    "35_capacity_fish_tank_volume_in_litres": arch_35_capacity_fish_tank_volume_in_litres,
    "36_capacity_swimming_pool_volume_in_kilolitres": arch_36_capacity_swimming_pool_volume_in_kilolitres,
    "37_internal_vs_external_dimensions_wall_thickness": arch_37_internal_vs_external_dimensions_wall_thickness,
    "38_hollow_container_capacity_given_wall_thickness": arch_38_hollow_container_capacity_given_wall_thickness,
    "39_water_displacement_by_submerged_solid_object": arch_39_water_displacement_by_submerged_solid_object,
    "40_water_level_rise_in_rectangular_container_from_added_object": arch_40_water_level_rise_in_rectangular_container_from_added_object,
    "41_doubling_side_of_cube_effect_on_surface_area_fourfold": arch_41_doubling_side_of_cube_effect_on_surface_area_fourfold,
    "42_doubling_side_of_cube_effect_on_volume_eightfold": arch_42_doubling_side_of_cube_effect_on_volume_eightfold,
    "43_tripling_dimensions_of_rectangular_prism_effect_on_volume": arch_43_tripling_dimensions_of_rectangular_prism_effect_on_volume,
    "44_same_volume_different_surface_areas_comparison_table": arch_44_same_volume_different_surface_areas_comparison_table,
    "45_composite_object_cube_glued_to_rectangular_prism_volume": arch_45_composite_object_cube_glued_to_rectangular_prism_volume,
    "46_composite_object_cube_glued_to_rectangular_prism_surface_area": arch_46_composite_object_cube_glued_to_rectangular_prism_surface_area,
    "47_composite_object_l_shaped_prism_volume": arch_47_composite_object_l_shaped_prism_volume,
    "48_cost_of_painting_walls_and_ceiling_of_room_surface_area": arch_48_cost_of_painting_walls_and_ceiling_of_room_surface_area,
    "49_packaging_number_of_small_cubes_fitting_into_large_box": arch_49_packaging_number_of_small_cubes_fitting_into_large_box,
    "50_rate_of_filling_tank_with_water_given_tap_flow_rate": arch_50_rate_of_filling_tank_with_water_given_tap_flow_rate,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())


def generate_grade8_measurement_3d_question(
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
    q_data["topic"] = "Surface area and volume of 3D objects"
    q_data["term"] = 4
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
                {"id": "mp_1", "desc": "Correct surface area or volume formula statement", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate calculation and conversion with correct units", "marks": m - 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_units", "penalty": 1}],
            "carry_forward_rule": "consequential_accuracy",
        }

    return q_data


generate = generate_grade8_measurement_3d_question
