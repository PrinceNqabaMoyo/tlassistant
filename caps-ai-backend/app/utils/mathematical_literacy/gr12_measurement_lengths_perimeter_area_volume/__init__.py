"""Grade 12 Mathematical Literacy: MEASUREMENT (LENGTHS, PERIMETER, AREA, VOLUME & PACKAGING).
Covers 52 distinct subskill archetypes strictly aligned with CAPS Grade 12 Paper 2 Measurement:
1. Lengths, Perimeters & Boundaries (Subskills 01–08)
2. Areas, Paving & Tiling (Subskills 09–16)
3. Surface Areas, Painting & Sheeting (Subskills 17–24)
4. Volumes, Liquid Capacity & Fill-Time (Subskills 25–32)
5. Earthworks, Bulk Materials & Dam Capacities (Subskills 33–40)
6. Packaging, 3D Stacking & Volumetric Packing Efficiency (Subskills 41–46)
7. Multi-step Project Costing, Quotations & Optimization (Subskills 47–52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .lengths_perimeters import (
    gen_subskill_01,
    gen_subskill_02,
    gen_subskill_03,
    gen_subskill_04,
    gen_subskill_05,
    gen_subskill_06,
    gen_subskill_07,
    gen_subskill_08,
)
from .areas_tiling import (
    gen_subskill_09,
    gen_subskill_10,
    gen_subskill_11,
    gen_subskill_12,
    gen_subskill_13,
    gen_subskill_14,
    gen_subskill_15,
    gen_subskill_16,
)
from .surface_areas_painting import (
    gen_subskill_17,
    gen_subskill_18,
    gen_subskill_19,
    gen_subskill_20,
    gen_subskill_21,
    gen_subskill_22,
    gen_subskill_23,
    gen_subskill_24,
)
from .volumes_capacity import (
    gen_subskill_25,
    gen_subskill_26,
    gen_subskill_27,
    gen_subskill_28,
    gen_subskill_29,
    gen_subskill_30,
    gen_subskill_31,
    gen_subskill_32,
)
from .earthworks_materials import (
    gen_subskill_33,
    gen_subskill_34,
    gen_subskill_35,
    gen_subskill_36,
    gen_subskill_37,
    gen_subskill_38,
    gen_subskill_39,
    gen_subskill_40,
)
from .packaging_stacking import (
    gen_subskill_41,
    gen_subskill_42,
    gen_subskill_43,
    gen_subskill_44,
    gen_subskill_45,
    gen_subskill_46,
)
from .costing_projects import (
    gen_subskill_47,
    gen_subskill_48,
    gen_subskill_49,
    gen_subskill_50,
    gen_subskill_51,
    gen_subskill_52,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    gen_subskill_01, gen_subskill_02, gen_subskill_03, gen_subskill_04,
    gen_subskill_05, gen_subskill_06, gen_subskill_07, gen_subskill_08,
    gen_subskill_09, gen_subskill_10, gen_subskill_11, gen_subskill_12,
    gen_subskill_13, gen_subskill_14, gen_subskill_15, gen_subskill_16,
    gen_subskill_17, gen_subskill_18, gen_subskill_19, gen_subskill_20,
    gen_subskill_21, gen_subskill_22, gen_subskill_23, gen_subskill_24,
    gen_subskill_25, gen_subskill_26, gen_subskill_27, gen_subskill_28,
    gen_subskill_29, gen_subskill_30, gen_subskill_31, gen_subskill_32,
    gen_subskill_33, gen_subskill_34, gen_subskill_35, gen_subskill_36,
    gen_subskill_37, gen_subskill_38, gen_subskill_39, gen_subskill_40,
    gen_subskill_41, gen_subskill_42, gen_subskill_43, gen_subskill_44,
    gen_subskill_45, gen_subskill_46, gen_subskill_47, gen_subskill_48,
    gen_subskill_49, gen_subskill_50, gen_subskill_51, gen_subskill_52,
]

SUBSKILLS = [
    # 01-08: Lengths & Perimeters
    "01_body_benchmarks_estimation",
    "02_soccer_pitch_dimensions",
    "03_rectangular_boundary_perimeter",
    "04_circular_roundabout_circumference",
    "05_running_track_composite_perimeter",
    "06_border_tiling_linear_grout",
    "07_fencing_with_gate_deductions",
    "08_multi_strand_barbed_wire_fencing",
    # 09-16: Areas & Tiling
    "09_rectangular_driveway_area",
    "10_triangular_garden_bed_area",
    "11_circular_swimming_pool_cover",
    "12_trapezoidal_land_plot_area",
    "13_l_shaped_composite_floor_area",
    "14_tile_box_counts_with_wastage",
    "15_paving_brick_counts_per_m2",
    "16_kikuyu_turf_rolls_coverage",
    # 17-24: Surface Areas & Painting
    "17_closed_rectangular_carton_surface_area",
    "18_open_top_swimming_pool_interior_area",
    "19_closed_cylindrical_geyser_surface_area",
    "20_open_cylindrical_culvert_curved_area",
    "21_wall_painting_minus_doors_and_windows",
    "22_paint_spread_rates_two_coats",
    "23_paint_can_cost_optimization_5L_1L",
    "24_corrugated_roof_sheeting_with_overlap",
    # 25-32: Volumes & Capacities
    "25_rectangular_water_reservoir_volume",
    "26_m3_to_litres_and_kilolitres_conversion",
    "27_cylindrical_jojo_tank_volume",
    "28_jojo_tank_holding_capacity_litres",
    "29_borehole_pump_flow_rate_fill_time",
    "30_daily_water_drawdown_depth",
    "31_trapezoidal_waste_skip_volume",
    "32_stepped_concrete_slab_volume",
    # 33-40: Earthworks & Materials
    "33_driveway_crushed_stone_gravel_volume",
    "34_bulk_sand_bags_and_total_cost",
    "35_raised_vegetable_planter_topsoil_volume",
    "36_garden_compost_dm3_bag_conversion",
    "37_utility_trench_excavation_volume",
    "38_rainwater_harvesting_collection_potential",
    "39_municipal_dam_storage_capacity_ML",
    "40_open_farm_dam_evaporation_loss",
    # 41-46: Packaging & Stacking
    "41_carton_packing_1D_axis_division",
    "42_package_orientation_comparison",
    "43_cylindrical_cans_packed_in_carton",
    "44_wasted_airspace_volume_in_box",
    "45_volumetric_packing_efficiency_percentage",
    "46_standard_pallets_in_shipping_container",
    # 47-52: Project Costing & Optimization
    "47_pool_renovation_interior_and_mosaic_cost",
    "48_paving_project_bricks_sand_and_kerbing",
    "49_room_decorating_ceiling_walls_and_skirting",
    "50_smallholder_dam_capacity_and_crop_days",
    "51_warehouse_pallet_racking_storage_density",
    "52_concrete_slab_casting_quotation_and_shuttering",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    i + 1: b for i, b in enumerate(BUILDERS)
}

# String key aliases
for i, b in enumerate(BUILDERS):
    DISPATCH_TABLE[f"gr12_meas_{i+1:02d}"] = b
    DISPATCH_TABLE[f"gr12_meas_subskill_{i+1:02d}"] = b
    DISPATCH_TABLE[SUBSKILLS[i]] = b

SUBSKILLS_METADATA = {
    f"gr12_meas_{i+1:02d}": {
        "index": i + 1,
        "name": SUBSKILLS[i],
        "category": (
            "Lengths & Perimeters" if i < 8 else
            "Areas & Tiling" if i < 16 else
            "Surface Areas & Painting" if i < 24 else
            "Volumes & Capacities" if i < 32 else
            "Earthworks & Bulk Materials" if i < 40 else
            "Packaging & Stacking" if i < 46 else
            "Project Costing & Optimization"
        ),
    }
    for i in range(len(SUBSKILLS))
}
