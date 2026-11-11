"""Grade 12 Mathematical Literacy: PLANS AND SCALE.
Covers 52 distinct subskill archetypes strictly aligned with CAPS Grade 12 Paper 2 Maps & Plans (Plans and Scale):
1. Determining Number Scales & Conversions (Subskills 01–08)
2. Bar Scale Construction & Conversion (Subskills 09–16)
3. Elevation Plans & Multi-View Projections (Subskills 17–24)
4. Architectural Floor Plans, Symbols & SANS Compliance (Subskills 25–32)
5. Site Plans, Boundaries & Municipal Bylaws (Subskills 33–40)
6. Cross-Sectional Technical Details (Subskills 41–46)
7. Material Takeoffs & Construction Costing (Subskills 47–52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .determining_number_scale import (
    gen_subskill_01,
    gen_subskill_02,
    gen_subskill_03,
    gen_subskill_04,
    gen_subskill_05,
    gen_subskill_06,
    gen_subskill_07,
    gen_subskill_08,
)
from .bar_scale_construction_conversion import (
    gen_subskill_09,
    gen_subskill_10,
    gen_subskill_11,
    gen_subskill_12,
    gen_subskill_13,
    gen_subskill_14,
    gen_subskill_15,
    gen_subskill_16,
)
from .elevation_plans_multi_view import (
    gen_subskill_17,
    gen_subskill_18,
    gen_subskill_19,
    gen_subskill_20,
    gen_subskill_21,
    gen_subskill_22,
    gen_subskill_23,
    gen_subskill_24,
)
from .architectural_floor_plans_symbols import (
    gen_subskill_25,
    gen_subskill_26,
    gen_subskill_27,
    gen_subskill_28,
    gen_subskill_29,
    gen_subskill_30,
    gen_subskill_31,
    gen_subskill_32,
)
from .site_plans_boundaries_servitudes import (
    gen_subskill_33,
    gen_subskill_34,
    gen_subskill_35,
    gen_subskill_36,
    gen_subskill_37,
    gen_subskill_38,
    gen_subskill_39,
    gen_subskill_40,
)
from .cross_sectional_details import (
    gen_subskill_41,
    gen_subskill_42,
    gen_subskill_43,
    gen_subskill_44,
    gen_subskill_45,
    gen_subskill_46,
)
from .material_takeoffs_costing import (
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
    # 01-08: Determining Number Scales & Conversions
    "01_determining_scale_measured_cm_to_real_m",
    "02_determining_scale_elevation_roof_height",
    "03_rounding_scale_to_nearest_standard",
    "04_calculating_ground_distance_scale_1_to_50",
    "05_calculating_ground_distance_scale_1_to_100",
    "06_calculating_ground_distance_scale_1_to_200",
    "07_plan_measurement_mm_for_ground_distance",
    "08_precision_limits_ruler_measurement_small_scale",
    # 09-16: Bar Scale Construction & Conversion
    "09_converting_number_scale_50_to_bar_scale_1m",
    "10_converting_number_scale_100_to_bar_scale_2m",
    "11_converting_number_scale_500_to_bar_scale_10m",
    "12_converting_number_scale_10000_to_bar_scale_200m",
    "13_measuring_distance_using_bar_scale_directly",
    "14_two_key_advantages_bar_scale_over_number_scale",
    "15_photocopy_enlargement_impact_number_vs_bar_scale",
    "16_recalibrating_number_scale_from_photocopied_bar",
    # 17-24: Elevation Plans & Multi-View Projections
    "17_identifying_north_south_east_west_elevations",
    "18_identifying_front_rear_left_right_elevations",
    "19_shared_measurements_front_vs_left_side_view",
    "20_deducing_missing_front_view_dimensions",
    "21_roof_overhang_eaves_dimension_from_elevation",
    "22_window_sill_height_above_finished_floor_level",
    "23_top_of_door_to_ceiling_clearance_measurement",
    "24_verifying_building_height_limit_municipal_bylaws",
    # 25-32: Architectural Floor Plans & Symbols
    "25_decoding_architectural_door_symbols_and_swings",
    "26_decoding_window_symbols_sills_and_frames",
    "27_decoding_sanitary_fittings_plumbing_symbols",
    "28_wall_thickness_deduction_internal_dimensions",
    "29_calculating_net_internal_room_floor_area",
    "30_window_glazing_natural_lighting_sans_10_percent",
    "31_openable_window_natural_ventilation_sans_5_percent",
    "32_circulation_flow_and_door_swing_conflict_safety",
    # 33-40: Site Plans, Boundaries & Municipal Bylaws
    "33_reading_erf_boundary_dimensions_stand_area",
    "34_building_footprint_coverage_percentage_bylaw",
    "35_building_line_setback_compliance_street_frontage",
    "36_municipal_sewer_servitude_easement_clearance",
    "37_driveway_turning_circle_diameter_and_gate_width",
    "38_boundary_wall_perimeter_deducting_gate_openings",
    "39_true_north_orientation_passive_solar_heating",
    "40_stormwater_runoff_drainage_fall_away_from_slab",
    # 41-46: Cross-Sectional Technical Details
    "41_foundation_trench_depth_footing_slab_thickness",
    "42_damp_proof_course_dpc_location_and_purpose",
    "43_wall_construction_layers_double_brick_vs_cavity",
    "44_brandering_timber_spacing_for_ceiling_boards",
    "45_finished_floor_level_ffl_above_ground_level",
    "46_rainwater_gutter_fall_gradient_and_downpipes",
    # 47-52: Material Takeoffs & Costing
    "47_brick_quantity_takeoff_wall_area_and_openings",
    "48_skirting_board_timber_length_deducting_doors",
    "49_ceiling_board_sheet_takeoff_with_wastage",
    "50_ceramic_floor_tile_quantity_boxes_and_cost",
    "51_interior_wall_paint_takeoff_drums_and_cost",
    "52_comprehensive_bill_of_quantities_boq_quote",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    i + 1: b for i, b in enumerate(BUILDERS)
}

# String key aliases
for i, b in enumerate(BUILDERS):
    DISPATCH_TABLE[f"gr12_plans_{i+1:02d}"] = b
    DISPATCH_TABLE[f"gr12_plans_subskill_{i+1:02d}"] = b
    DISPATCH_TABLE[SUBSKILLS[i]] = b

SUBSKILLS_METADATA = {
    f"gr12_plans_{i+1:02d}": {
        "index": i + 1,
        "name": SUBSKILLS[i],
        "category": (
            "Determining Number Scales" if i < 8 else
            "Bar Scale Construction" if i < 16 else
            "Elevation Plans & Views" if i < 24 else
            "Floor Plans & SANS Symbols" if i < 32 else
            "Site Plans & Municipal Bylaws" if i < 40 else
            "Cross-Sectional Technical Details" if i < 46 else
            "Material Takeoffs & Costing"
        ),
    }
    for i in range(len(SUBSKILLS))
}
