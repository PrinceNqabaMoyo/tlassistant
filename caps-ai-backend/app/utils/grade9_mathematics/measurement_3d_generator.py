"""Grade 9 Mathematics - Surface Area, Volume & Capacity of 3D Objects Generator (50 Semantic Archetypes).
=======================================================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 4 Topic: Surface area volume and capacity of 3D objects
  - curriculum_docs_auto/Mathematics_Gr9/Term 4/01. Surface area volume and capacity of 3D objects.md
  - Surface area and volume of cubes, rectangular prisms, triangular prisms, and right cylinders.
  - Open vs closed containers, curved lateral pipe surfaces, paint coverage, and dimension scaling.
  - Capacity conversions (cm³ to ml, cm³ to L, m³ to L / kL) and rate of flow calculations.
  - Composite solids and real-world South African civil/reservoir costing synthesis.

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from .measurement_3d_archetypes_01_25 import (
    arch_01_surface_area_cube_integer_side,
    arch_02_surface_area_cube_decimal_side,
    arch_03_find_cube_edge_given_total_surface_area,
    arch_04_surface_area_rectangular_prism_integer_dims,
    arch_05_surface_area_rectangular_prism_decimal_dims,
    arch_06_surface_area_rectangular_box_without_lid,
    arch_07_find_rectangular_prism_height_given_surface_area,
    arch_08_surface_area_right_triangular_prism_pythagoras_needed,
    arch_09_surface_area_equilateral_triangular_prism,
    arch_10_surface_area_isosceles_triangular_prism,
    arch_11_surface_area_closed_cylinder_given_radius_and_height,
    arch_12_surface_area_closed_cylinder_given_diameter_and_height,
    arch_13_surface_area_cylinder_open_at_one_end,
    arch_14_curved_lateral_surface_area_of_cylinder_pipe,
    arch_15_find_cylinder_height_given_curved_surface_area,
    arch_16_find_cylinder_radius_given_curved_surface_area,
    arch_17_paint_coverage_calculation_for_rectangular_room_or_box,
    arch_18_paint_coverage_calculation_for_cylindrical_water_tank,
    arch_19_surface_area_scaling_effect_doubling_all_dimensions,
    arch_20_surface_area_scaling_effect_factor_k,
    arch_21_surface_area_of_t_net_unfolded_cube,
    arch_22_surface_area_of_triangular_prism_net,
    arch_23_surface_area_of_cylinder_net_rectangle_plus_two_circles,
    arch_24_surface_area_composite_cube_with_smaller_cube_on_top,
    arch_25_surface_area_composite_rectangular_prism_and_triangular_roof,
)
from .measurement_3d_archetypes_26_50 import (
    arch_26_volume_of_cube_integer_edge,
    arch_27_volume_of_cube_decimal_edge,
    arch_28_find_cube_edge_given_volume,
    arch_29_volume_of_rectangular_prism_integer_dims,
    arch_30_volume_of_rectangular_prism_decimal_dims,
    arch_31_find_rectangular_prism_missing_dimension_given_volume,
    arch_32_volume_of_right_triangular_prism,
    arch_33_volume_of_isosceles_triangular_prism,
    arch_34_find_triangular_prism_length_given_volume_and_base_area,
    arch_35_volume_of_cylinder_given_radius_and_height,
    arch_36_volume_of_cylinder_given_diameter_and_height,
    arch_37_find_cylinder_height_given_volume_and_radius,
    arch_38_find_cylinder_radius_given_volume_and_height,
    arch_39_capacity_conversion_cm3_to_millilitres,
    arch_40_capacity_conversion_cm3_to_litres,
    arch_41_capacity_conversion_m3_to_kilolitres,
    arch_42_capacity_conversion_litres_to_m3,
    arch_43_liquid_volume_in_partially_filled_rectangular_tank,
    arch_44_liquid_volume_in_partially_filled_cylindrical_jojo_tank,
    arch_45_rate_of_flow_time_to_fill_rectangular_or_cylindrical_tank,
    arch_46_volume_scaling_effect_doubling_all_dimensions,
    arch_47_volume_scaling_effect_tripling_or_factor_k,
    arch_48_volume_of_composite_l_shaped_prism,
    arch_49_volume_of_hollow_cylindrical_pipe,
    arch_50_compound_multi_stage_3d_mensuration_costing_and_capacity_synthesis,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_surface_area_cube_integer_side": arch_01_surface_area_cube_integer_side,
    "02_surface_area_cube_decimal_side": arch_02_surface_area_cube_decimal_side,
    "03_find_cube_edge_given_total_surface_area": arch_03_find_cube_edge_given_total_surface_area,
    "04_surface_area_rectangular_prism_integer_dims": arch_04_surface_area_rectangular_prism_integer_dims,
    "05_surface_area_rectangular_prism_decimal_dims": arch_05_surface_area_rectangular_prism_decimal_dims,
    "06_surface_area_rectangular_box_without_lid": arch_06_surface_area_rectangular_box_without_lid,
    "07_find_rectangular_prism_height_given_surface_area": arch_07_find_rectangular_prism_height_given_surface_area,
    "08_surface_area_right_triangular_prism_pythagoras_needed": arch_08_surface_area_right_triangular_prism_pythagoras_needed,
    "09_surface_area_equilateral_triangular_prism": arch_09_surface_area_equilateral_triangular_prism,
    "10_surface_area_isosceles_triangular_prism": arch_10_surface_area_isosceles_triangular_prism,
    "11_surface_area_closed_cylinder_given_radius_and_height": arch_11_surface_area_closed_cylinder_given_radius_and_height,
    "12_surface_area_closed_cylinder_given_diameter_and_height": arch_12_surface_area_closed_cylinder_given_diameter_and_height,
    "13_surface_area_cylinder_open_at_one_end": arch_13_surface_area_cylinder_open_at_one_end,
    "14_curved_lateral_surface_area_of_cylinder_pipe": arch_14_curved_lateral_surface_area_of_cylinder_pipe,
    "15_find_cylinder_height_given_curved_surface_area": arch_15_find_cylinder_height_given_curved_surface_area,
    "16_find_cylinder_radius_given_curved_surface_area": arch_16_find_cylinder_radius_given_curved_surface_area,
    "17_paint_coverage_calculation_for_rectangular_room_or_box": arch_17_paint_coverage_calculation_for_rectangular_room_or_box,
    "18_paint_coverage_calculation_for_cylindrical_water_tank": arch_18_paint_coverage_calculation_for_cylindrical_water_tank,
    "19_surface_area_scaling_effect_doubling_all_dimensions": arch_19_surface_area_scaling_effect_doubling_all_dimensions,
    "20_surface_area_scaling_effect_factor_k": arch_20_surface_area_scaling_effect_factor_k,
    "21_surface_area_of_t_net_unfolded_cube": arch_21_surface_area_of_t_net_unfolded_cube,
    "22_surface_area_of_triangular_prism_net": arch_22_surface_area_of_triangular_prism_net,
    "23_surface_area_of_cylinder_net_rectangle_plus_two_circles": arch_23_surface_area_of_cylinder_net_rectangle_plus_two_circles,
    "24_surface_area_composite_cube_with_smaller_cube_on_top": arch_24_surface_area_composite_cube_with_smaller_cube_on_top,
    "25_surface_area_composite_rectangular_prism_and_triangular_roof": arch_25_surface_area_composite_rectangular_prism_and_triangular_roof,
    "26_volume_of_cube_integer_edge": arch_26_volume_of_cube_integer_edge,
    "27_volume_of_cube_decimal_edge": arch_27_volume_of_cube_decimal_edge,
    "28_find_cube_edge_given_volume": arch_28_find_cube_edge_given_volume,
    "29_volume_of_rectangular_prism_integer_dims": arch_29_volume_of_rectangular_prism_integer_dims,
    "30_volume_of_rectangular_prism_decimal_dims": arch_30_volume_of_rectangular_prism_decimal_dims,
    "31_find_rectangular_prism_missing_dimension_given_volume": arch_31_find_rectangular_prism_missing_dimension_given_volume,
    "32_volume_of_right_triangular_prism": arch_32_volume_of_right_triangular_prism,
    "33_volume_of_isosceles_triangular_prism": arch_33_volume_of_isosceles_triangular_prism,
    "34_find_triangular_prism_length_given_volume_and_base_area": arch_34_find_triangular_prism_length_given_volume_and_base_area,
    "35_volume_of_cylinder_given_radius_and_height": arch_35_volume_of_cylinder_given_radius_and_height,
    "36_volume_of_cylinder_given_diameter_and_height": arch_36_volume_of_cylinder_given_diameter_and_height,
    "37_find_cylinder_height_given_volume_and_radius": arch_37_find_cylinder_height_given_volume_and_radius,
    "38_find_cylinder_radius_given_volume_and_height": arch_38_find_cylinder_radius_given_volume_and_height,
    "39_capacity_conversion_cm3_to_millilitres": arch_39_capacity_conversion_cm3_to_millilitres,
    "40_capacity_conversion_cm3_to_litres": arch_40_capacity_conversion_cm3_to_litres,
    "41_capacity_conversion_m3_to_kilolitres": arch_41_capacity_conversion_m3_to_kilolitres,
    "42_capacity_conversion_litres_to_m3": arch_42_capacity_conversion_litres_to_m3,
    "43_liquid_volume_in_partially_filled_rectangular_tank": arch_43_liquid_volume_in_partially_filled_rectangular_tank,
    "44_liquid_volume_in_partially_filled_cylindrical_jojo_tank": arch_44_liquid_volume_in_partially_filled_cylindrical_jojo_tank,
    "45_rate_of_flow_time_to_fill_rectangular_or_cylindrical_tank": arch_45_rate_of_flow_time_to_fill_rectangular_or_cylindrical_tank,
    "46_volume_scaling_effect_doubling_all_dimensions": arch_46_volume_scaling_effect_doubling_all_dimensions,
    "47_volume_scaling_effect_tripling_or_factor_k": arch_47_volume_scaling_effect_tripling_or_factor_k,
    "48_volume_of_composite_l_shaped_prism": arch_48_volume_of_composite_l_shaped_prism,
    "49_volume_of_hollow_cylindrical_pipe": arch_49_volume_of_hollow_cylindrical_pipe,
    "50_compound_multi_stage_3d_mensuration_costing_and_capacity_synthesis": arch_50_compound_multi_stage_3d_mensuration_costing_and_capacity_synthesis,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate_grade9_measurement_3d_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)

    selected_subskill = subskill
    if not selected_subskill or selected_subskill not in DISPATCH_TABLE:
        if archetype_index is not None and 0 <= archetype_index < len(SUBSKILLS):
            selected_subskill = SUBSKILLS[archetype_index]
        elif mode.startswith("elementary_"):
            target_stem = mode.replace("elementary_", "")
            candidates = [s for s in SUBSKILLS if target_stem in s]
            selected_subskill = candidates[0] if candidates else r.choice(SUBSKILLS)
        else:
            selected_subskill = r.choice(SUBSKILLS)

    builder = DISPATCH_TABLE[selected_subskill]
    q = builder(r)

    # 6-Pillar Metadata Enforcements
    q.setdefault("topic", "Surface area volume and capacity of 3D objects")
    q.setdefault("subject", "Mathematics")
    q.setdefault("grade", "9")
    q.setdefault("term", 4)
    q.setdefault("caps_weight_percent", 10.0)
    q.setdefault("suggested_duration_mins", 3)
    q.setdefault("difficulty", "medium")
    q.setdefault("subskill", selected_subskill)
    q.setdefault("archetype", selected_subskill)
    q.setdefault("interactive", False)

    return q


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    mode: str = "compound",
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]] | Dict[str, Any]:
    if count == 1:
        return generate_grade9_measurement_3d_question(
            seed=seed, subskill=subskill, archetype_index=archetype_index, mode=mode, **kwargs
        )
    base_seed = seed if seed is not None else random.randint(100, 999999)
    out: List[Dict[str, Any]] = []
    for i in range(count):
        sub_seed = base_seed + i * 37
        sub = subskill if subskill else (SUBSKILLS[i % len(SUBSKILLS)] if archetype_index is None else None)
        out.append(
            generate_grade9_measurement_3d_question(
                seed=sub_seed, subskill=sub, archetype_index=archetype_index, mode=mode, **kwargs
            )
        )
    return out
