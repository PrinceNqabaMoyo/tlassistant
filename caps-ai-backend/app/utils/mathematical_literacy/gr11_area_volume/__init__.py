"""Package initializing Grade 11 Mathematical Literacy: AREA AND VOLUME (52 Archetypes)."""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .perimeter_2d_areas import (
    generate_subskill_1,
    generate_subskill_2,
    generate_subskill_3,
    generate_subskill_4,
    generate_subskill_5,
    generate_subskill_6,
    generate_subskill_7,
    generate_subskill_8,
    generate_subskill_9,
)
from .surface_area_prisms import (
    generate_subskill_10,
    generate_subskill_11,
    generate_subskill_12,
    generate_subskill_13,
    generate_subskill_14,
    generate_subskill_15,
    generate_subskill_16,
    generate_subskill_17,
    generate_subskill_18,
)
from .surface_area_cylinders import (
    generate_subskill_19,
    generate_subskill_20,
    generate_subskill_21,
    generate_subskill_22,
    generate_subskill_23,
    generate_subskill_24,
    generate_subskill_25,
    generate_subskill_26,
    generate_subskill_27,
)
from .volume_capacity import (
    generate_subskill_28,
    generate_subskill_29,
    generate_subskill_30,
    generate_subskill_31,
    generate_subskill_32,
    generate_subskill_33,
    generate_subskill_34,
    generate_subskill_35,
    generate_subskill_36,
)
from .material_costing_packaging import (
    generate_subskill_37,
    generate_subskill_38,
    generate_subskill_39,
    generate_subskill_40,
    generate_subskill_41,
    generate_subskill_42,
    generate_subskill_43,
    generate_subskill_44,
)
from .dimensions_scaling_analysis import (
    generate_subskill_45,
    generate_subskill_46,
    generate_subskill_47,
    generate_subskill_48,
    generate_subskill_49,
    generate_subskill_50,
    generate_subskill_51,
    generate_subskill_52,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    f"subskill_{i}": fn
    for i, fn in enumerate(
        [
            generate_subskill_1,
            generate_subskill_2,
            generate_subskill_3,
            generate_subskill_4,
            generate_subskill_5,
            generate_subskill_6,
            generate_subskill_7,
            generate_subskill_8,
            generate_subskill_9,
            generate_subskill_10,
            generate_subskill_11,
            generate_subskill_12,
            generate_subskill_13,
            generate_subskill_14,
            generate_subskill_15,
            generate_subskill_16,
            generate_subskill_17,
            generate_subskill_18,
            generate_subskill_19,
            generate_subskill_20,
            generate_subskill_21,
            generate_subskill_22,
            generate_subskill_23,
            generate_subskill_24,
            generate_subskill_25,
            generate_subskill_26,
            generate_subskill_27,
            generate_subskill_28,
            generate_subskill_29,
            generate_subskill_30,
            generate_subskill_31,
            generate_subskill_32,
            generate_subskill_33,
            generate_subskill_34,
            generate_subskill_35,
            generate_subskill_36,
            generate_subskill_37,
            generate_subskill_38,
            generate_subskill_39,
            generate_subskill_40,
            generate_subskill_41,
            generate_subskill_42,
            generate_subskill_43,
            generate_subskill_44,
            generate_subskill_45,
            generate_subskill_46,
            generate_subskill_47,
            generate_subskill_48,
            generate_subskill_49,
            generate_subskill_50,
            generate_subskill_51,
            generate_subskill_52,
        ],
        start=1,
    )
}

SUBSKILLS: List[str] = [
    "01_rectangle_perimeter_fencing_cost_estimation_gate",
    "02_circular_garden_bed_circumference_border_edging",
    "03_semi_circular_driveway_turning_circle_perimeter",
    "04_rectangular_room_floor_area_skirting_board",
    "05_triangular_gable_wall_area",
    "06_circular_pond_pool_surface_area",
    "07_trapezoidal_flower_bed_area",
    "08_l_shaped_composite_room_floor_area",
    "09_wall_take_home_area_calculation_doors_windows",
    "10_total_surface_area_closed_rectangular_cardboard",
    "11_surface_area_open_top_rectangular_toy",
    "12_four_interior_walls_rectangular_classroom_painting",
    "13_total_surface_area_triangular_prism_camping",
    "14_triangular_prism_roof_truss_surface_area",
    "15_exterior_plastering_area_rectangular_building_foundation",
    "16_surface_area_comparison_two_rectangular_prisms",
    "17_gift_wrapping_paper_requirement_percentage_overlap",
    "18_surface_area_stepped_rectangular_display_podium",
    "19_total_surface_area_closed_cylindrical_tin",
    "20_curved_surface_area_open_cylindrical_concrete",
    "21_surface_area_open_top_cylindrical_water",
    "22_tin_can_paper_label_area_calculation",
    "23_painting_exterior_curved_side_top_lid",
    "24_painting_internal_walls_circular_floor_cylindrical",
    "25_thermal_insulation_jacket_surface_area_cylindrical",
    "26_cylindrical_grain_silo_corrugated_iron_sheet",
    "27_ratio_curved_surface_area_total_surface",
    "28_volume_rectangular_shipping_container_m",
    "29_capacity_rectangular_swimming_pool_litres_m",
    "30_swimming_pool_water_volume_filled_freeboard",
    "31_volume_closed_cylindrical_jojo_water_tank",
    "32_volume_cylindrical_beverage_can_millilitres_cm",
    "33_volume_triangular_prism_water_trough_litres",
    "34_time_required_fill_swimming_pool_at",
    "35_rainwater_harvesting_collection_potential_roof_catchment",
    "36_municipal_water_step_tariff_bill_calculation",
    "37_wall_paint_quantity_calculation_spread_rate",
    "38_paint_purchasing_optimization_comparing_l_l",
    "39_floor_tiling_calculation_tile_dimensions_box",
    "40_total_cost_floor_tiling_including_tile",
    "41_concrete_slab_volume_ready_mix_delivery",
    "42_paving_rectangular_driveway_brick_pavers",
    "43_carton_packing_small_rectangular_boxes_into_master",
    "44_carton_packing_cylindrical_food_cans_into_rectangular",
    "45_effect_perimeter_area_when_doubling_length",
    "46_effect_area_when_both_length_width",
    "47_effect_volume_rectangular_prism_when_all",
    "48_effect_cylinder_volume_when_doubling_radius",
    "49_surface_area_volume_ratio_sa_v",
    "50_cost_efficiency_comparison_price_per_litre",
    "51_irregular_composite_building_excavation_soil_volume",
    "52_comprehensive_home_renovation_project_budgeting",
]

for _idx, _sem_id in enumerate(SUBSKILLS, 1):
    DISPATCH_TABLE[_sem_id] = DISPATCH_TABLE[f"subskill_{_idx}"]



def generate_subskill(subskill_id: str, r: random.Random) -> Dict[str, Any]:
    """Generate a specific archetype question by subskill id."""
    if subskill_id not in DISPATCH_TABLE:
        raise ValueError(f"Unknown subskill '{subskill_id}'. Valid subskills: {SUBSKILLS}")
    return DISPATCH_TABLE[subskill_id](r)


def generate_random_question(r: random.Random) -> Dict[str, Any]:
    """Generate a random question from across all 52 AREA AND VOLUME archetypes."""
    chosen = r.choice(SUBSKILLS)
    return DISPATCH_TABLE[chosen](r)
