"""Package initializing Grade 11 Mathematical Literacy: MAPS (52 Archetypes)."""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .scale_distances import (
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
from .directions_bearings import (
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
from .travel_speed_fuel import (
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
from .strip_maps_tolls import (
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
from .topographic_contours import (
    generate_subskill_37,
    generate_subskill_38,
    generate_subskill_39,
    generate_subskill_40,
    generate_subskill_41,
    generate_subskill_42,
    generate_subskill_43,
    generate_subskill_44,
)
from .seating_stadiums import (
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
    "01_contour_relief_ratio_factor_conversion_route_distance_cm_real",
    "02_town_town_road_route_distance_ratio_factor_conversion_route_distance",
    "03_regional_road_map_scale_map_cm",
    "04_national_route_distance_ratio_factor_route_distance_cm_real",
    "05_reverse_scale_calculation_real_distance_map",
    "06_measure_straight_line_distance_using_graphic",
    "07_number_scale_ratio_n_known_benchmark",
    "08_as_crow_flies_vs_actual_winding",
    "09_map_resizing_zoom_implications_bar_scale",
    "10_cardinal_inter_cardinal_compass_directions_between",
    "11_opposite_direction_return_travel",
    "12_alphanumeric_grid_coordinate_lookup_street_map",
    "13_identify_facility_located_at_given_alphanumeric",
    "14_step_step_turn_turn_navigation_directions",
    "15_compass_bearing_estimation_degrees",
    "16_relative_position_description_combining_distance_direction",
    "17_gps_coordinate_format_interpretation_latitude_longitude",
    "18_shortest_grid_walking_distance_along_town_roads",
    "19_travel_time_calculation_t_d_v",
    "20_arrival_time_calculation_including_rest_stops",
    "21_average_speed_calculation_v_d_t",
    "22_required_average_speed_arrive_appointment_deadline",
    "23_fuel_consumption_calculation_litres_rate_l",
    "24_fuel_cost_calculation_rands_litres_price",
    "25_fuel_efficiency_comparison_between_two_vehicles",
    "26_number_refuelling_stops_required_based_tank",
    "27_carpooling_cost_sharing_fuel_toll_fees",
    "28_distance_table_matrix_lookup_between_major",
    "29_multi_leg_road_trip_calculation_distance",
    "30_reading_intermediate_town_distances_strip_route_distance",
    "31_cumulative_strip_route_distance_distance_calculation_between",
    "32_national_route_corridor_identification",
    "33_toll_plaza_tariff_summation_along_national",
    "34_toll_plaza_vehicle_class_classification_under",
    "35_alternative_route_comparison_toll_highway_vs",
    "36_round_trip_total_logistics_cost_fuel",
    "37_contour_line_interval_determination_index_contours",
    "38_spot_height_trigonometrical_station_altitude_lookup",
    "39_steep_vs_gentle_slope_identification_based",
    "40_v_shaped_river_contour_flow_direction",
    "41_gradient_calculation_as_ratio_n_rise",
    "42_intervisibility_between_two_points_contour_relief_profile",
    "43_hiking_trail_elevation_gain_loss_across",
    "44_impact_steep_gradient_hiking_time_or",
    "45_stadium_block_row_seat_allocation_coordinate",
    "46_stadium_ticketing_revenue_calculation_across_seating",
    "47_cinema_auditorium_seating_schedule_scheme_layout_wheelchair",
    "48_aircraft_seating_chart_layout_aisle_vs",
    "49_shopping_mall_multi_level_floor_schedule_scheme",
    "50_building_emergency_evacuation_route_analysis",
    "51_wheelchair_ramp_accessibility_slope_compliance_vs",
    "52_multi_modal_transport_route_itinerary_evaluation",
]

for _idx, _sem_id in enumerate(SUBSKILLS, 1):
    DISPATCH_TABLE[_sem_id] = DISPATCH_TABLE[f"subskill_{_idx}"]



def generate_subskill(subskill_id: str, r: random.Random) -> Dict[str, Any]:
    """Generate a specific archetype question by subskill id."""
    if subskill_id not in DISPATCH_TABLE:
        raise ValueError(f"Unknown subskill '{subskill_id}'. Valid subskills: {SUBSKILLS}")
    return DISPATCH_TABLE[subskill_id](r)


def generate_random_question(r: random.Random) -> Dict[str, Any]:
    """Generate a random question from across all 52 MAPS archetypes."""
    chosen = r.choice(SUBSKILLS)
    return DISPATCH_TABLE[chosen](r)
