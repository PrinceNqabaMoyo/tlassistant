"""Grade 12 Mathematical Literacy: MAPS AND PLANS (MODELS).
Covers 52 distinct subskill archetypes strictly aligned with CAPS Grade 12 Paper 2 Maps & Plans (Models):
1. Scale Selection & Page Fit for 3D Models (Subskills 01–08)
2. Architectural Models (RDP House & Community Structures) (Subskills 09–16)
3. Nets, Materials & Fabrication Costing (Subskills 17–24)
4. Area & Volume Scaling Factors (k, k², k³) (Subskills 25–32)
5. Assembly Instructions & Packaging Models (Subskills 33–40)
6. Pallet Stacking & Shipping Container Loading (Subskills 41–46)
7. Topographic Site Models, Contours & Civil Layouts (Subskills 47–52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .scale_selection_page_fit import (
    gen_subskill_01,
    gen_subskill_02,
    gen_subskill_03,
    gen_subskill_04,
    gen_subskill_05,
    gen_subskill_06,
    gen_subskill_07,
    gen_subskill_08,
)
from .architectural_models_rdp_house import (
    gen_subskill_09,
    gen_subskill_10,
    gen_subskill_11,
    gen_subskill_12,
    gen_subskill_13,
    gen_subskill_14,
    gen_subskill_15,
    gen_subskill_16,
)
from .nets_materials_costing import (
    gen_subskill_17,
    gen_subskill_18,
    gen_subskill_19,
    gen_subskill_20,
    gen_subskill_21,
    gen_subskill_22,
    gen_subskill_23,
    gen_subskill_24,
)
from .area_volume_scaling_factors import (
    gen_subskill_25,
    gen_subskill_26,
    gen_subskill_27,
    gen_subskill_28,
    gen_subskill_29,
    gen_subskill_30,
    gen_subskill_31,
    gen_subskill_32,
)
from .assembly_instructions_packaging import (
    gen_subskill_33,
    gen_subskill_34,
    gen_subskill_35,
    gen_subskill_36,
    gen_subskill_37,
    gen_subskill_38,
    gen_subskill_39,
    gen_subskill_40,
)
from .pallet_stacking_container_loading import (
    gen_subskill_41,
    gen_subskill_42,
    gen_subskill_43,
    gen_subskill_44,
    gen_subskill_45,
    gen_subskill_46,
)
from .contour_topographic_site_models import (
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
    # 01-08: Scale Selection & Page Fit
    "01_comparing_model_scales_largest_justification",
    "02_best_scale_selection_a4_page_fit",
    "03_best_scale_selection_a3_poster_board_fit",
    "04_minimum_baseboard_dimensions_with_margin",
    "05_calculating_model_height_from_elevation",
    "06_evaluating_scale_detail_vs_feasibility",
    "07_converting_real_dimensions_to_model_mm_cm",
    "08_reverse_conversion_ruler_measurement_to_real",
    # 09-16: Architectural Models (RDP House)
    "09_rdp_house_scaled_exterior_wall_dimensions",
    "10_rdp_house_interior_partition_wall_offset",
    "11_scaled_window_door_cutout_dimensions",
    "12_gabled_roof_rafter_pitch_pythagoras",
    "13_south_vs_north_elevation_wall_height_symmetry",
    "14_doorway_wheelchair_accessibility_verification",
    "15_minimum_ceiling_height_sans_10400_check",
    "16_circulation_corridor_width_verification",
    # 17-24: Nets, Materials & Costing
    "17_prism_net_layout_surface_area",
    "18_gluing_tabs_joint_allowance_percentage",
    "19_foam_board_sheet_cutting_optimization",
    "20_costing_architectural_modeling_supplies",
    "21_spray_paint_surface_coverage_canisters",
    "22_laser_cutting_line_length_fabrication_cost",
    "23_scaled_3d_printing_filament_mass_and_cost",
    "24_total_model_production_budget_contingency",
    # 25-32: Area & Volume Scaling Factors
    "25_area_scale_factor_k_squared_calculation",
    "26_real_floor_area_from_model_plan_area",
    "27_volume_scale_factor_k_cubed_calculation",
    "28_reservoir_scale_model_capacity_litres",
    "29_model_mass_vs_real_mass_identical_density",
    "30_scale_factor_distortion_linear_vs_area_error",
    "31_acoustic_scale_model_testing_frequency",
    "32_wind_tunnel_model_frontal_area_calculation",
    # 33-40: Assembly Instructions & Packaging
    "33_component_sequence_exploded_assembly",
    "34_fastener_hardware_pack_inventory_count",
    "35_left_vs_right_panel_interior_symmetry",
    "36_flat_pack_carton_internal_volume_m3",
    "37_box_wall_thickness_deduction_net_capacity",
    "38_carton_gross_shipping_mass_with_tare",
    "39_flat_pack_panel_horizontal_orientation_reason",
    "40_flat_pack_assembly_safety_symbols_decoding",
    # 41-46: Pallet Stacking & Containers
    "41_cartons_per_layer_iso_pallet_grid",
    "42_interlocking_pallet_stacking_layers_height",
    "43_pallet_gross_mass_forklift_limit_check",
    "44_loading_pallets_into_20ft_container",
    "45_loading_pallets_into_40ft_container",
    "46_palletized_container_space_efficiency_pct",
    # 47-52: Topographic Site Models
    "47_stepped_contour_model_foam_layer_thickness",
    "48_identifying_hill_peaks_vs_valleys_contours",
    "49_slope_gradient_ratio_and_percentage",
    "50_cut_and_fill_earthworks_balance_surplus",
    "51_scaled_parking_bay_and_aisle_dimensions",
    "52_civil_site_model_tender_project_quotation",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    i + 1: b for i, b in enumerate(BUILDERS)
}

# String key aliases
for i, b in enumerate(BUILDERS):
    DISPATCH_TABLE[f"gr12_models_{i+1:02d}"] = b
    DISPATCH_TABLE[f"gr12_models_subskill_{i+1:02d}"] = b
    DISPATCH_TABLE[SUBSKILLS[i]] = b

SUBSKILLS_METADATA = {
    f"gr12_models_{i+1:02d}": {
        "index": i + 1,
        "name": SUBSKILLS[i],
        "category": (
            "Scale Selection & Page Fit" if i < 8 else
            "Architectural Models (RDP House)" if i < 16 else
            "Nets, Materials & Costing" if i < 24 else
            "Area & Volume Scaling Factors" if i < 32 else
            "Assembly Instructions & Packaging" if i < 40 else
            "Pallet Stacking & Containers" if i < 46 else
            "Topographic Site Models"
        ),
    }
    for i in range(len(SUBSKILLS))
}
