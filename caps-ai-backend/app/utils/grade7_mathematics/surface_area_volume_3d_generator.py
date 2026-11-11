"""Grade 7 Mathematics - Surface Area and Volume of 3D Objects Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/01. Surface area and volume of 3D objects.md
Focus: Cubes and rectangular prisms, surface area (closed/open-top/nets), volume, isometric 3D & net SVGs, metric & capacity conversions (cm3, mm3, m3, litres, ml, kl), word problems, scaling factors, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .surface_area_volume_3d_archetypes_01_25 import (
    arch_01_cube_surface_area_integer,
    arch_02_cube_surface_area_from_face_area,
    arch_03_cube_edge_from_surface_area,
    arch_04_cube_open_top_surface_area,
    arch_05_cube_volume_integer,
    arch_06_cube_edge_from_volume,
    arch_07_cube_volume_and_surface_area_comparison,
    arch_08_prism_volume,
    arch_09_rectangular_prism_volume_from_base_area,
    arch_10_rectangular_prism_height_from_volume,
    arch_11_rectangular_prism_width_from_volume,
    arch_12_prism_surface_area,
    arch_13_rectangular_prism_surface_area_open_top,
    arch_14_rectangular_prism_net_face_sum,
    arch_15_count_unit_cubes_in_prism_layer,
    arch_16_isometric_cube_svg_volume,
    arch_17_isometric_rectangular_prism_svg_sa,
    arch_18_isometric_rectangular_prism_svg_volume,
    arch_19_net_of_cube_svg_surface_area,
    arch_20_net_of_rectangular_prism_svg_sa,
    arch_21_unit_conversion_cm3_to_mm3,
    arch_22_unit_conversion_mm3_to_cm3,
    arch_23_unit_conversion_m3_to_cm3,
    arch_24_unit_conversion_cm3_to_m3,
    arch_25_volume_capacity_conversion,
)
from .surface_area_volume_3d_archetypes_26_50 import (
    arch_26_capacity_conversion_cm3_to_litres,
    arch_27_capacity_conversion_litres_to_cm3,
    arch_28_capacity_conversion_m3_to_litres,
    arch_29_capacity_conversion_litres_to_m3,
    arch_30_capacity_conversion_m3_to_kilolitres,
    arch_31_word_problem_fish_tank_capacity_litres,
    arch_32_word_problem_swimming_pool_capacity_m3_litres,
    arch_33_word_problem_water_tank_rate_of_filling,
    arch_34_word_problem_painting_outer_walls_surface_area,
    arch_35_word_problem_packaging_small_boxes_into_carton,
    arch_36_word_problem_gift_wrapping_surface_area,
    arch_37_effect_of_doubling_dimensions_on_volume,
    arch_38_effect_of_doubling_dimensions_on_surface_area,
    arch_39_effect_of_tripling_dimensions_on_volume,
    arch_40_composite_solid_two_prisms_volume,
    arch_41_composite_solid_hollow_prism_volume,
    arch_42_liquid_depth_in_rectangular_container,
    arch_43_common_error_cubic_conversion_trap_1m3,
    arch_44_common_error_forgetting_pairs_in_surface_area_trap,
    arch_45_common_error_confusing_volume_and_surface_area_trap,
    arch_46_common_error_open_box_six_faces_trap,
    arch_47_ratio_of_volumes_two_cubes,
    arch_48_ratio_of_surface_areas_two_cubes,
    arch_49_cost_of_tin_plate_surface_area,
    arch_50_surface_area_and_volume_3d_comprehensive_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_cube_surface_area_integer": arch_01_cube_surface_area_integer,
    "02_cube_surface_area_from_face_area": arch_02_cube_surface_area_from_face_area,
    "03_cube_edge_from_surface_area": arch_03_cube_edge_from_surface_area,
    "04_cube_open_top_surface_area": arch_04_cube_open_top_surface_area,
    "05_cube_volume_integer": arch_05_cube_volume_integer,
    "06_cube_edge_from_volume": arch_06_cube_edge_from_volume,
    "07_cube_volume_and_surface_area_comparison": arch_07_cube_volume_and_surface_area_comparison,
    "08_prism_volume": arch_08_prism_volume,
    "09_rectangular_prism_volume_from_base_area": arch_09_rectangular_prism_volume_from_base_area,
    "10_rectangular_prism_height_from_volume": arch_10_rectangular_prism_height_from_volume,
    "11_rectangular_prism_width_from_volume": arch_11_rectangular_prism_width_from_volume,
    "12_prism_surface_area": arch_12_prism_surface_area,
    "13_rectangular_prism_surface_area_open_top": arch_13_rectangular_prism_surface_area_open_top,
    "14_rectangular_prism_net_face_sum": arch_14_rectangular_prism_net_face_sum,
    "15_count_unit_cubes_in_prism_layer": arch_15_count_unit_cubes_in_prism_layer,
    "16_isometric_cube_svg_volume": arch_16_isometric_cube_svg_volume,
    "17_isometric_rectangular_prism_svg_sa": arch_17_isometric_rectangular_prism_svg_sa,
    "18_isometric_rectangular_prism_svg_volume": arch_18_isometric_rectangular_prism_svg_volume,
    "19_net_of_cube_svg_surface_area": arch_19_net_of_cube_svg_surface_area,
    "20_net_of_rectangular_prism_svg_sa": arch_20_net_of_rectangular_prism_svg_sa,
    "21_unit_conversion_cm3_to_mm3": arch_21_unit_conversion_cm3_to_mm3,
    "22_unit_conversion_mm3_to_cm3": arch_22_unit_conversion_mm3_to_cm3,
    "23_unit_conversion_m3_to_cm3": arch_23_unit_conversion_m3_to_cm3,
    "24_unit_conversion_cm3_to_m3": arch_24_unit_conversion_cm3_to_m3,
    "25_volume_capacity_conversion": arch_25_volume_capacity_conversion,
    "26_capacity_conversion_cm3_to_litres": arch_26_capacity_conversion_cm3_to_litres,
    "27_capacity_conversion_litres_to_cm3": arch_27_capacity_conversion_litres_to_cm3,
    "28_capacity_conversion_m3_to_litres": arch_28_capacity_conversion_m3_to_litres,
    "29_capacity_conversion_litres_to_m3": arch_29_capacity_conversion_litres_to_m3,
    "30_capacity_conversion_m3_to_kilolitres": arch_30_capacity_conversion_m3_to_kilolitres,
    "31_word_problem_fish_tank_capacity_litres": arch_31_word_problem_fish_tank_capacity_litres,
    "32_word_problem_swimming_pool_capacity_m3_litres": arch_32_word_problem_swimming_pool_capacity_m3_litres,
    "33_word_problem_water_tank_rate_of_filling": arch_33_word_problem_water_tank_rate_of_filling,
    "34_word_problem_painting_outer_walls_surface_area": arch_34_word_problem_painting_outer_walls_surface_area,
    "35_word_problem_packaging_small_boxes_into_carton": arch_35_word_problem_packaging_small_boxes_into_carton,
    "36_word_problem_gift_wrapping_surface_area": arch_36_word_problem_gift_wrapping_surface_area,
    "37_effect_of_doubling_dimensions_on_volume": arch_37_effect_of_doubling_dimensions_on_volume,
    "38_effect_of_doubling_dimensions_on_surface_area": arch_38_effect_of_doubling_dimensions_on_surface_area,
    "39_effect_of_tripling_dimensions_on_volume": arch_39_effect_of_tripling_dimensions_on_volume,
    "40_composite_solid_two_prisms_volume": arch_40_composite_solid_two_prisms_volume,
    "41_composite_solid_hollow_prism_volume": arch_41_composite_solid_hollow_prism_volume,
    "42_liquid_depth_in_rectangular_container": arch_42_liquid_depth_in_rectangular_container,
    "43_common_error_cubic_conversion_trap_1m3": arch_43_common_error_cubic_conversion_trap_1m3,
    "44_common_error_forgetting_pairs_in_surface_area_trap": arch_44_common_error_forgetting_pairs_in_surface_area_trap,
    "45_common_error_confusing_volume_and_surface_area_trap": arch_45_common_error_confusing_volume_and_surface_area_trap,
    "46_common_error_open_box_six_faces_trap": arch_46_common_error_open_box_six_faces_trap,
    "47_ratio_of_volumes_two_cubes": arch_47_ratio_of_volumes_two_cubes,
    "48_ratio_of_surface_areas_two_cubes": arch_48_ratio_of_surface_areas_two_cubes,
    "49_cost_of_tin_plate_surface_area": arch_49_cost_of_tin_plate_surface_area,
    "50_surface_area_and_volume_3d_comprehensive_autopsy": arch_50_surface_area_and_volume_3d_comprehensive_autopsy,
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


generate = generate_question
