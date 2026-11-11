"""Grade 12 Mathematical Literacy: SCALE AND MAP WORK (MAPS, PLANS, SCALE & TRAVEL COSTS).
Covers 52 distinct subskill archetypes strictly aligned with CAPS Grade 12 Paper 2 Maps & Plans:
1. Number Scale Calculations & Conversions (Subskills 01–08)
2. Strip Road Maps & Distance Matrix Charts (Subskills 09–16)
3. Vehicle Operating Costs — AA Rate Tables (Subskills 17–24)
4. Route Costing, Toll Plazas & Multi-Modal Travel (Subskills 25–32)
5. Fuel Consumption & Vehicle Range Planning (Subskills 33–40)
6. Compass Directions, Bearings & Elevation Views (Subskills 41–46)
7. Comprehensive Journey Plans, Multi-Stop Logistics & Itineraries (Subskills 47–52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .number_scale_calculations import (
    gen_subskill_01,
    gen_subskill_02,
    gen_subskill_03,
    gen_subskill_04,
    gen_subskill_05,
    gen_subskill_06,
    gen_subskill_07,
    gen_subskill_08,
)
from .strip_maps_distance_charts import (
    gen_subskill_09,
    gen_subskill_10,
    gen_subskill_11,
    gen_subskill_12,
    gen_subskill_13,
    gen_subskill_14,
    gen_subskill_15,
    gen_subskill_16,
)
from .aa_vehicle_operating_costs import (
    gen_subskill_17,
    gen_subskill_18,
    gen_subskill_19,
    gen_subskill_20,
    gen_subskill_21,
    gen_subskill_22,
    gen_subskill_23,
    gen_subskill_24,
)
from .route_costing_multi_modal import (
    gen_subskill_25,
    gen_subskill_26,
    gen_subskill_27,
    gen_subskill_28,
    gen_subskill_29,
    gen_subskill_30,
    gen_subskill_31,
    gen_subskill_32,
)
from .fuel_consumption_range import (
    gen_subskill_33,
    gen_subskill_34,
    gen_subskill_35,
    gen_subskill_36,
    gen_subskill_37,
    gen_subskill_38,
    gen_subskill_39,
    gen_subskill_40,
)
from .compass_bearings_elevations import (
    gen_subskill_41,
    gen_subskill_42,
    gen_subskill_43,
    gen_subskill_44,
    gen_subskill_45,
    gen_subskill_46,
)
from .journey_plans_itineraries import (
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
    # 01-08: Number Scale Calculations
    "01_topographical_map_scale_cm_to_km",
    "02_architectural_plan_scale_mm_to_m",
    "03_ground_km_to_map_cm_conversion",
    "04_determine_number_scale_from_km",
    "05_bar_scale_to_number_scale_conversion",
    "06_map_scale_accuracy_against_strip_markers",
    "07_comparing_large_scale_vs_small_scale_detail",
    "08_photocopy_enlargement_effect_on_scales",
    # 09-16: Strip Maps & Distance Matrices
    "09_sa_intercity_distance_matrix_lookup",
    "10_summing_strip_map_distance_markers",
    "11_route_distance_comparison_highway_vs_bypass",
    "12_identifying_strip_map_junction_towns",
    "13_travel_time_from_distance_and_speed",
    "14_decimal_hours_to_hours_and_minutes",
    "15_eta_scheduling_with_rest_stops",
    "16_required_speed_for_target_arrival_time",
    # 17-24: AA Vehicle Operating Costs
    "17_aa_fixed_cost_table_lookup",
    "18_aa_running_cost_factors_lookup",
    "19_tovc_cents_per_km_calculation",
    "20_tovc_cents_to_rands_per_km",
    "21_journey_operating_cost_distance_times_tovc",
    "22_fuel_only_vs_full_wear_and_tear_cost",
    "23_sars_reimbursement_rate_vs_actual_cost",
    "24_petrol_price_hike_tovc_percentage_increase",
    # 25-32: Route Costing & Multi-Modal Travel
    "25_sanral_toll_plaza_fees_calculation",
    "26_private_vehicle_total_journey_cost",
    "27_long_distance_bus_schedule_timetable",
    "28_bus_fare_costing_single_return_discounts",
    "29_passenger_train_vs_intercity_bus",
    "30_cost_comparison_solo_driver_vs_bus_vs_carpool",
    "31_minibus_taxi_operator_trip_budget",
    "32_minibus_taxi_passenger_fare_pricing_profit",
    # 33-40: Fuel Consumption & Range
    "33_trip_fuel_volume_from_consumption_rate",
    "34_total_fuel_cost_from_rate_and_price",
    "35_actual_consumption_rate_from_odometer",
    "36_full_tank_driving_range_calculation",
    "37_refueling_stop_planning_with_reserve",
    "38_urban_vs_open_road_fuel_expenditure",
    "39_cargo_trailer_fuel_consumption_impact",
    "40_electric_vehicle_vs_petrol_energy_cost_km",
    # 41-46: Compass Directions & Elevations
    "41_cardinal_and_intercardinal_directions",
    "42_three_figure_compass_bearings",
    "43_overhead_highway_gantry_lane_signage",
    "44_architectural_elevation_views_orientation",
    "45_southern_hemisphere_solar_room_orientation",
    "46_latitude_and_longitude_coordinates_topo",
    # 47-52: Journey Plans & Logistics
    "47_two_day_long_haul_itinerary_and_hotel",
    "48_freight_multi_drop_delivery_shift_duration",
    "49_holiday_travel_budget_with_contingency",
    "50_car_rental_package_quotation_comparison",
    "51_car_rental_break_even_driving_distance",
    "52_sports_team_transport_mode_optimization",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    i + 1: b for i, b in enumerate(BUILDERS)
}

# String key aliases
for i, b in enumerate(BUILDERS):
    DISPATCH_TABLE[f"gr12_scale_{i+1:02d}"] = b
    DISPATCH_TABLE[f"gr12_scale_subskill_{i+1:02d}"] = b
    DISPATCH_TABLE[SUBSKILLS[i]] = b

SUBSKILLS_METADATA = {
    f"gr12_scale_{i+1:02d}": {
        "index": i + 1,
        "name": SUBSKILLS[i],
        "category": (
            "Number Scales & Conversions" if i < 8 else
            "Strip Maps & Distance Matrices" if i < 16 else
            "AA Vehicle Operating Costs" if i < 24 else
            "Route Costing & Multi-Modal" if i < 32 else
            "Fuel Consumption & Range" if i < 40 else
            "Compass Directions & Elevations" if i < 46 else
            "Journey Plans & Logistics"
        ),
    }
    for i in range(len(SUBSKILLS))
}
