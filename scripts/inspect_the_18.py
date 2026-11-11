import sys
sys.path.insert(0, 'caps-ai-backend')
import inspect
from app.utils.mathematical_literacy.scale_maps import (
    number_scales,
    bar_scales_resizing,
    compass_directions_bearings,
    travel_speed_time_fuel,
    strip_maps_road_routes,
    seating_indoor_maps,
)
from app.utils.mathematical_literacy.assembly_packaging import scaled_plans_costs

targets = [
    (number_scales, "_gen_map_scale_real_distance_from_cm_km"),
    (number_scales, "_gen_map_scale_large_scale_vs_small_scale_comparison"),
    (number_scales, "_gen_map_scale_topographic_standard_fifty_thousand"),
    (bar_scales_resizing, "_gen_map_bar_scale_resizing_photocopy_advantage"),
    (bar_scales_resizing, "_gen_map_number_scale_distortion_under_magnification"),
    (bar_scales_resizing, "_gen_map_contour_lines_and_elevation_height"),
    (bar_scales_resizing, "_gen_map_inset_scale_comparison_overview_vs_detail"),
    (bar_scales_resizing, "_gen_map_winding_distance_using_string_or_paper_edge"),
    (compass_directions_bearings, "_gen_map_navigational_turn_by_turn_directions"),
    (compass_directions_bearings, "_gen_map_magnetic_declination_true_vs_magnetic_north"),
    (compass_directions_bearings, "_gen_map_cardinal_elevation_sun_exposure_aspect"),
    (travel_speed_time_fuel, "_gen_map_fuel_economy_comparison_two_vehicles"),
    (strip_maps_road_routes, "_gen_map_strip_toll_plaza_tariff_aggregation"),
    (strip_maps_road_routes, "_gen_map_strip_route_choice_toll_highway_vs_alternative"),
    (seating_indoor_maps, "_gen_map_indoor_shopping_mall_directory_navigation"),
    (seating_indoor_maps, "_gen_map_indoor_evacuation_shortest_emergency_exit"),
    (seating_indoor_maps, "_gen_map_indoor_universal_wheelchair_accessibility"),
    (scaled_plans_costs, "_gen_asm_plan_scale_number_ratio_room_dimension"),
]

for mod, fname in targets:
    fn = getattr(mod, fname)
    src = inspect.getsource(fn)
    print("=" * 60)
    print(f"{fname} in {mod.__name__}")
    print("=" * 60)
    print(src)
