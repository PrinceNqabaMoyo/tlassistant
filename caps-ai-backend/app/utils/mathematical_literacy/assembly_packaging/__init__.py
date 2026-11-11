"""Assembly diagrams, floor plans and packaging Subskills Package (52 distinct archetypes).

Covers Grade 10 Mathematical Literacy Term 2 Topic:
1. Assembly diagrams & component hardware (Subskills 1 to 9)
2. Domestic electrical plug & appliance wiring (Subskills 10 to 17)
3. Floor plans — architectural symbols & layout analysis (Subskills 18 to 26)
4. Scaled floor plans & cost calculations (Subskills 27 to 35)
5. 3D packaging arrangements & orientation optimization (Subskills 36 to 44)
6. 2D nets, models & pallet stacking (Subskills 45 to 52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .assembly_diagrams import (
    _gen_asm_diag_parts_list_hardware_inventory,
    _gen_asm_diag_step_sequence_order_determination,
    _gen_asm_diag_tool_selection_and_usage,
    _gen_asm_diag_furniture_screw_pilot_hole_alignment,
    _gen_asm_diag_directional_arrows_action_interpretation,
    _gen_asm_diag_warning_symbols_safety_precautions,
    _gen_asm_diag_cell_phone_sim_battery_installation,
    _gen_asm_diag_flatpack_wardrobe_hinge_and_runner_mounting,
    _gen_asm_diag_modular_shelving_unit_tier_spacing,
)
from .electrical_wiring import (
    _gen_asm_elec_three_pin_plug_wire_colour_identification,
    _gen_asm_elec_three_pin_plug_terminal_prong_placement,
    _gen_asm_elec_cord_clamp_cable_arrester_safety,
    _gen_asm_elec_two_pin_vs_three_pin_comparison,
    _gen_asm_elec_stripping_and_twisting_copper_strands,
    _gen_asm_elec_fuse_rating_and_replacement_amperage,
    _gen_asm_elec_fault_identification_incorrect_wiring,
    _gen_asm_elec_cable_length_stripping_measurement,
)
from .floor_plan_analysis import (
    _gen_asm_plan_identify_architectural_symbols,
    _gen_asm_plan_door_swing_quarter_circle_arc,
    _gen_asm_plan_room_type_deduction_from_fixtures,
    _gen_asm_plan_compass_orientation_north_aspect,
    _gen_asm_plan_kitchen_work_triangle_layout,
    _gen_asm_plan_design_flaws_clearance_hazard_audit,
    _gen_asm_plan_furniture_space_planning_placement,
    _gen_asm_plan_ventilation_and_window_placement,
    _gen_asm_plan_doorway_clearance_furniture_delivery,
)
from .scaled_plans_costs import (
    _gen_asm_plan_scale_number_ratio_room_dimension,
    _gen_asm_plan_scale_inverse_real_to_drawing_length,
    _gen_asm_plan_bar_scale_measurement_conversion,
    _gen_asm_plan_total_floor_area_calculation,
    _gen_asm_plan_floor_tiling_box_estimate_and_wastage,
    _gen_asm_plan_floor_tiling_total_cost,
    _gen_asm_plan_skirting_board_perimeter_deducting_doors,
    _gen_asm_plan_wall_painting_surface_area_deducting_openings,
    _gen_asm_plan_rental_cost_per_square_metre,
)
from .packaging_arrangements import (
    _gen_asm_pack_single_layer_box_grid_length_width,
    _gen_asm_pack_multi_layer_3d_box_stacking,
    _gen_asm_pack_orientation_comparison_lengthwise_vs_widthwise,
    _gen_asm_pack_cylindrical_cans_in_rectangular_carton,
    _gen_asm_pack_area_division_fallacy_explanation,
    _gen_asm_pack_wasted_volume_void_space_percentage,
    _gen_asm_pack_mass_limit_vs_volume_capacity,
    _gen_asm_pack_shipping_carton_count_for_order,
    _gen_asm_pack_carton_and_postage_total_budget,
)
from .nets_models_pallets import (
    _gen_asm_net_rectangular_prism_face_identification,
    _gen_asm_net_cube_dice_opposite_faces_sum_seven,
    _gen_asm_net_cylinder_curved_surface_and_circular_bases,
    _gen_asm_net_triangular_prism_chocolate_box,
    _gen_asm_pack_pallet_layer_interlocking_pattern,
    _gen_asm_pack_pallet_maximum_height_stack_limit,
    _gen_asm_model_architectural_cardboard_scale,
    _gen_asm_pack_triangular_prism_tessellation_vs_cylinder,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Cluster 1: Assembly Diagrams & Component Hardware (9)
    "asm_diag_parts_list_hardware_inventory": _gen_asm_diag_parts_list_hardware_inventory,
    "asm_diag_step_sequence_order_determination": _gen_asm_diag_step_sequence_order_determination,
    "asm_diag_tool_selection_and_usage": _gen_asm_diag_tool_selection_and_usage,
    "asm_diag_furniture_screw_pilot_hole_alignment": _gen_asm_diag_furniture_screw_pilot_hole_alignment,
    "asm_diag_directional_arrows_action_interpretation": _gen_asm_diag_directional_arrows_action_interpretation,
    "asm_diag_warning_symbols_safety_precautions": _gen_asm_diag_warning_symbols_safety_precautions,
    "asm_diag_cell_phone_sim_battery_installation": _gen_asm_diag_cell_phone_sim_battery_installation,
    "asm_diag_flatpack_wardrobe_hinge_and_runner_mounting": _gen_asm_diag_flatpack_wardrobe_hinge_and_runner_mounting,
    "asm_diag_modular_shelving_unit_tier_spacing": _gen_asm_diag_modular_shelving_unit_tier_spacing,

    # Cluster 2: Domestic Electrical Wiring (8)
    "asm_elec_three_pin_plug_wire_colour_identification": _gen_asm_elec_three_pin_plug_wire_colour_identification,
    "asm_elec_three_pin_plug_terminal_prong_placement": _gen_asm_elec_three_pin_plug_terminal_prong_placement,
    "asm_elec_cord_clamp_cable_arrester_safety": _gen_asm_elec_cord_clamp_cable_arrester_safety,
    "asm_elec_two_pin_vs_three_pin_comparison": _gen_asm_elec_two_pin_vs_three_pin_comparison,
    "asm_elec_stripping_and_twisting_copper_strands": _gen_asm_elec_stripping_and_twisting_copper_strands,
    "asm_elec_fuse_rating_and_replacement_amperage": _gen_asm_elec_fuse_rating_and_replacement_amperage,
    "asm_elec_fault_identification_incorrect_wiring": _gen_asm_elec_fault_identification_incorrect_wiring,
    "asm_elec_cable_length_stripping_measurement": _gen_asm_elec_cable_length_stripping_measurement,

    # Cluster 3: Floor Plans — Symbols & Layout (9)
    "asm_plan_identify_architectural_symbols": _gen_asm_plan_identify_architectural_symbols,
    "asm_plan_door_swing_quarter_circle_arc": _gen_asm_plan_door_swing_quarter_circle_arc,
    "asm_plan_room_type_deduction_from_fixtures": _gen_asm_plan_room_type_deduction_from_fixtures,
    "asm_plan_compass_orientation_north_aspect": _gen_asm_plan_compass_orientation_north_aspect,
    "asm_plan_kitchen_work_triangle_layout": _gen_asm_plan_kitchen_work_triangle_layout,
    "asm_plan_design_flaws_clearance_hazard_audit": _gen_asm_plan_design_flaws_clearance_hazard_audit,
    "asm_plan_furniture_space_planning_placement": _gen_asm_plan_furniture_space_planning_placement,
    "asm_plan_ventilation_and_window_placement": _gen_asm_plan_ventilation_and_window_placement,
    "asm_plan_doorway_clearance_furniture_delivery": _gen_asm_plan_doorway_clearance_furniture_delivery,

    # Cluster 4: Scaled Floor Plans & Costs (9)
    "asm_plan_scale_number_ratio_room_dimension": _gen_asm_plan_scale_number_ratio_room_dimension,
    "asm_plan_scale_inverse_real_to_drawing_length": _gen_asm_plan_scale_inverse_real_to_drawing_length,
    "asm_plan_bar_scale_measurement_conversion": _gen_asm_plan_bar_scale_measurement_conversion,
    "asm_plan_total_floor_area_calculation": _gen_asm_plan_total_floor_area_calculation,
    "asm_plan_floor_tiling_box_estimate_and_wastage": _gen_asm_plan_floor_tiling_box_estimate_and_wastage,
    "asm_plan_floor_tiling_total_cost": _gen_asm_plan_floor_tiling_total_cost,
    "asm_plan_skirting_board_perimeter_deducting_doors": _gen_asm_plan_skirting_board_perimeter_deducting_doors,
    "asm_plan_wall_painting_surface_area_deducting_openings": _gen_asm_plan_wall_painting_surface_area_deducting_openings,
    "asm_plan_rental_cost_per_square_metre": _gen_asm_plan_rental_cost_per_square_metre,

    # Cluster 5: 3D Packaging Arrangements (9)
    "asm_pack_single_layer_box_grid_length_width": _gen_asm_pack_single_layer_box_grid_length_width,
    "asm_pack_multi_layer_3d_box_stacking": _gen_asm_pack_multi_layer_3d_box_stacking,
    "asm_pack_orientation_comparison_lengthwise_vs_widthwise": _gen_asm_pack_orientation_comparison_lengthwise_vs_widthwise,
    "asm_pack_cylindrical_cans_in_rectangular_carton": _gen_asm_pack_cylindrical_cans_in_rectangular_carton,
    "asm_pack_area_division_fallacy_explanation": _gen_asm_pack_area_division_fallacy_explanation,
    "asm_pack_wasted_volume_void_space_percentage": _gen_asm_pack_wasted_volume_void_space_percentage,
    "asm_pack_mass_limit_vs_volume_capacity": _gen_asm_pack_mass_limit_vs_volume_capacity,
    "asm_pack_shipping_carton_count_for_order": _gen_asm_pack_shipping_carton_count_for_order,
    "asm_pack_carton_and_postage_total_budget": _gen_asm_pack_carton_and_postage_total_budget,

    # Cluster 6: 2D Nets, Models & Pallets (8)
    "asm_net_rectangular_prism_face_identification": _gen_asm_net_rectangular_prism_face_identification,
    "asm_net_cube_dice_opposite_faces_sum_seven": _gen_asm_net_cube_dice_opposite_faces_sum_seven,
    "asm_net_cylinder_curved_surface_and_circular_bases": _gen_asm_net_cylinder_curved_surface_and_circular_bases,
    "asm_net_triangular_prism_chocolate_box": _gen_asm_net_triangular_prism_chocolate_box,
    "asm_pack_pallet_layer_interlocking_pattern": _gen_asm_pack_pallet_layer_interlocking_pattern,
    "asm_pack_pallet_maximum_height_stack_limit": _gen_asm_pack_pallet_maximum_height_stack_limit,
    "asm_model_architectural_cardboard_scale": _gen_asm_model_architectural_cardboard_scale,
    "asm_pack_triangular_prism_tessellation_vs_cylinder": _gen_asm_pack_triangular_prism_tessellation_vs_cylinder,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def generate(seed: Optional[int] = None, count: int = 1, subskill: Optional[str] = None) -> List[Dict[str, Any]]:
    """Generate questions for Assembly diagrams, floor plans and packaging."""
    r = random.Random(seed)
    questions = []

    for _ in range(count):
        if subskill and subskill in DISPATCH_TABLE:
            fn = DISPATCH_TABLE[subskill]
        else:
            chosen = r.choice(SUBSKILLS)
            fn = DISPATCH_TABLE[chosen]
        questions.append(fn(r))

    return questions
