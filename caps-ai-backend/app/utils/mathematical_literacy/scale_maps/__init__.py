"""Scale maps and plans Subskills Package (52 distinct archetypes).

Covers Grade 10 Mathematical Literacy Term 2 Topic:
1. Number scale calculations & unit conversions (Subskills 1 to 9)
2. Bar scales, elevation & map resizing effects (Subskills 10 to 17)
3. Compass directions, bearings & grid coordinates (Subskills 18 to 26)
4. Travel time, speed, distance & fuel consumption (Subskills 27 to 35)
5. Strip maps, road routes, tolls & distance charts (Subskills 36 to 44)
6. Seating plans, indoor layouts & navigation (Subskills 45 to 52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .number_scales import (
    _gen_map_scale_unit_conversion_constants,
    _gen_map_scale_real_distance_from_cm_km,
    _gen_map_scale_real_distance_from_cm_metres,
    _gen_map_scale_inverse_drawing_length_from_km,
    _gen_map_scale_inverse_drawing_length_from_metres,
    _gen_map_scale_ratio_determination_from_measurements,
    _gen_map_scale_large_scale_vs_small_scale_comparison,
    _gen_map_scale_topographic_standard_fifty_thousand,
    _gen_map_scale_straight_line_vs_winding_road_distance,
)
from .bar_scales_resizing import (
    _gen_map_bar_scale_segment_measurement_reading,
    _gen_map_bar_scale_ratio_conversion_to_number_scale,
    _gen_map_bar_scale_resizing_photocopy_advantage,
    _gen_map_number_scale_distortion_under_magnification,
    _gen_map_contour_lines_and_elevation_height,
    _gen_map_gradient_slope_vertical_rise_horizontal_distance,
    _gen_map_inset_scale_comparison_overview_vs_detail,
    _gen_map_winding_distance_using_string_or_paper_edge,
)
from .compass_directions_bearings import (
    _gen_map_compass_eight_point_direction_from_a_to_b,
    _gen_map_compass_sixteen_point_intermediate_directions,
    _gen_map_compass_bearing_degrees_true_north,
    _gen_map_compass_back_bearing_reciprocal,
    _gen_map_grid_alphanumeric_street_guide_coordinates,
    _gen_map_navigational_turn_by_turn_directions,
    _gen_map_gps_latitude_longitude_south_african_hemisphere,
    _gen_map_magnetic_declination_true_vs_magnetic_north,
    _gen_map_cardinal_elevation_sun_exposure_aspect,
)
from .travel_speed_time_fuel import (
    _gen_map_travel_time_calculation_distance_speed,
    _gen_map_travel_time_fractional_hours_to_hours_minutes,
    _gen_map_travel_average_speed_calculation,
    _gen_map_travel_arrival_time_with_rest_stops,
    _gen_map_fuel_consumption_litres_per_hundred_km,
    _gen_map_fuel_total_cost_calculation,
    _gen_map_fuel_economy_comparison_two_vehicles,
    _gen_map_travel_total_trip_budget_fuel_tolls,
    _gen_map_travel_carpooling_vs_bus_cost_per_person,
)
from .strip_maps_road_routes import (
    _gen_map_strip_consecutive_segment_distances_sum,
    _gen_map_strip_distance_chart_matrix_reading,
    _gen_map_strip_toll_plaza_tariff_aggregation,
    _gen_map_strip_route_choice_toll_highway_vs_alternative,
    _gen_map_strip_safety_rest_stop_frequency,
    _gen_map_strip_fuel_range_refueling_stop_planning,
    _gen_map_strip_average_speed_enforcement_timing,
    _gen_map_strip_intermediate_town_distance_subtraction,
    _gen_map_strip_road_sign_speed_limit_and_distance,
)
from .seating_indoor_maps import (
    _gen_map_seat_cinema_theatre_grid_row_seat_number,
    _gen_map_seat_stadium_stands_turnstiles_gate,
    _gen_map_seat_classroom_exam_hall_spacing,
    _gen_map_seat_aeroplane_cabin_window_aisle,
    _gen_map_seat_event_banquet_round_tables,
    _gen_map_indoor_shopping_mall_directory_navigation,
    _gen_map_indoor_evacuation_shortest_emergency_exit,
    _gen_map_indoor_universal_wheelchair_accessibility,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Cluster 1: Number Scale Calculations (9)
    "map_scale_unit_conversion_constants": _gen_map_scale_unit_conversion_constants,
    "map_scale_real_distance_from_cm_km": _gen_map_scale_real_distance_from_cm_km,
    "map_scale_real_distance_from_cm_metres": _gen_map_scale_real_distance_from_cm_metres,
    "map_scale_inverse_drawing_length_from_km": _gen_map_scale_inverse_drawing_length_from_km,
    "map_scale_inverse_drawing_length_from_metres": _gen_map_scale_inverse_drawing_length_from_metres,
    "map_scale_ratio_determination_from_measurements": _gen_map_scale_ratio_determination_from_measurements,
    "map_scale_large_scale_vs_small_scale_comparison": _gen_map_scale_large_scale_vs_small_scale_comparison,
    "map_scale_topographic_standard_fifty_thousand": _gen_map_scale_topographic_standard_fifty_thousand,
    "map_scale_straight_line_vs_winding_road_distance": _gen_map_scale_straight_line_vs_winding_road_distance,

    # Cluster 2: Bar Scales & Map Resizing (8)
    "map_bar_scale_segment_measurement_reading": _gen_map_bar_scale_segment_measurement_reading,
    "map_bar_scale_ratio_conversion_to_number_scale": _gen_map_bar_scale_ratio_conversion_to_number_scale,
    "map_bar_scale_resizing_photocopy_advantage": _gen_map_bar_scale_resizing_photocopy_advantage,
    "map_number_scale_distortion_under_magnification": _gen_map_number_scale_distortion_under_magnification,
    "map_contour_lines_and_elevation_height": _gen_map_contour_lines_and_elevation_height,
    "map_gradient_slope_vertical_rise_horizontal_distance": _gen_map_gradient_slope_vertical_rise_horizontal_distance,
    "map_inset_scale_comparison_overview_vs_detail": _gen_map_inset_scale_comparison_overview_vs_detail,
    "map_winding_distance_using_string_or_paper_edge": _gen_map_winding_distance_using_string_or_paper_edge,

    # Cluster 3: Compass Directions & Bearings (9)
    "map_compass_eight_point_direction_from_a_to_b": _gen_map_compass_eight_point_direction_from_a_to_b,
    "map_compass_sixteen_point_intermediate_directions": _gen_map_compass_sixteen_point_intermediate_directions,
    "map_compass_bearing_degrees_true_north": _gen_map_compass_bearing_degrees_true_north,
    "map_compass_back_bearing_reciprocal": _gen_map_compass_back_bearing_reciprocal,
    "map_grid_alphanumeric_street_guide_coordinates": _gen_map_grid_alphanumeric_street_guide_coordinates,
    "map_navigational_turn_by_turn_directions": _gen_map_navigational_turn_by_turn_directions,
    "map_gps_latitude_longitude_south_african_hemisphere": _gen_map_gps_latitude_longitude_south_african_hemisphere,
    "map_magnetic_declination_true_vs_magnetic_north": _gen_map_magnetic_declination_true_vs_magnetic_north,
    "map_cardinal_elevation_sun_exposure_aspect": _gen_map_cardinal_elevation_sun_exposure_aspect,

    # Cluster 4: Travel Time, Speed & Fuel (9)
    "map_travel_time_calculation_distance_speed": _gen_map_travel_time_calculation_distance_speed,
    "map_travel_time_fractional_hours_to_hours_minutes": _gen_map_travel_time_fractional_hours_to_hours_minutes,
    "map_travel_average_speed_calculation": _gen_map_travel_average_speed_calculation,
    "map_travel_arrival_time_with_rest_stops": _gen_map_travel_arrival_time_with_rest_stops,
    "map_fuel_consumption_litres_per_hundred_km": _gen_map_fuel_consumption_litres_per_hundred_km,
    "map_fuel_total_cost_calculation": _gen_map_fuel_total_cost_calculation,
    "map_fuel_economy_comparison_two_vehicles": _gen_map_fuel_economy_comparison_two_vehicles,
    "map_travel_total_trip_budget_fuel_tolls": _gen_map_travel_total_trip_budget_fuel_tolls,
    "map_travel_carpooling_vs_bus_cost_per_person": _gen_map_travel_carpooling_vs_bus_cost_per_person,

    # Cluster 5: Strip Maps & Route Planning (9)
    "map_strip_consecutive_segment_distances_sum": _gen_map_strip_consecutive_segment_distances_sum,
    "map_strip_distance_chart_matrix_reading": _gen_map_strip_distance_chart_matrix_reading,
    "map_strip_toll_plaza_tariff_aggregation": _gen_map_strip_toll_plaza_tariff_aggregation,
    "map_strip_route_choice_toll_highway_vs_alternative": _gen_map_strip_route_choice_toll_highway_vs_alternative,
    "map_strip_safety_rest_stop_frequency": _gen_map_strip_safety_rest_stop_frequency,
    "map_strip_fuel_range_refueling_stop_planning": _gen_map_strip_fuel_range_refueling_stop_planning,
    "map_strip_average_speed_enforcement_timing": _gen_map_strip_average_speed_enforcement_timing,
    "map_strip_intermediate_town_distance_subtraction": _gen_map_strip_intermediate_town_distance_subtraction,
    "map_strip_road_sign_speed_limit_and_distance": _gen_map_strip_road_sign_speed_limit_and_distance,

    # Cluster 6: Seating Plans & Indoor Layouts (8)
    "map_seat_cinema_theatre_grid_row_seat_number": _gen_map_seat_cinema_theatre_grid_row_seat_number,
    "map_seat_stadium_stands_turnstiles_gate": _gen_map_seat_stadium_stands_turnstiles_gate,
    "map_seat_classroom_exam_hall_spacing": _gen_map_seat_classroom_exam_hall_spacing,
    "map_seat_aeroplane_cabin_window_aisle": _gen_map_seat_aeroplane_cabin_window_aisle,
    "map_seat_event_banquet_round_tables": _gen_map_seat_event_banquet_round_tables,
    "map_indoor_shopping_mall_directory_navigation": _gen_map_indoor_shopping_mall_directory_navigation,
    "map_indoor_evacuation_shortest_emergency_exit": _gen_map_indoor_evacuation_shortest_emergency_exit,
    "map_indoor_universal_wheelchair_accessibility": _gen_map_indoor_universal_wheelchair_accessibility,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def generate(seed: Optional[int] = None, count: int = 1, subskill: Optional[str] = None) -> List[Dict[str, Any]]:
    """Generate questions for Scale maps and plans."""
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
