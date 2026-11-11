"""Grade 12 Mathematical Literacy — CONVERSIONS AND TIME Subskill Modules.
Subskills 01–52 dispatch registry and metadata.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Tuple

from .solid_liquid_volume import (
    generate_01_calculated_volume_to_liquid_litres,
    generate_02_cubic_metres_to_kilolitres,
    generate_03_millimetres_cubed_to_millilitres,
    generate_04_liquid_volume_to_mass_density,
    generate_05_cylindrical_tank_capacity_litres,
    generate_06_swimming_pool_drainage_time,
    generate_07_municipal_water_meter_kl_to_litres,
    generate_08_aggregate_sand_weight_to_volume,
)
from .spread_rates_chemicals import (
    generate_09_paint_spread_rate_single_coat,
    generate_10_multi_coat_paint_tin_packaging,
    generate_11_costing_paint_tins_total,
    generate_12_agricultural_pesticide_ratio_coverage,
    generate_13_lawn_fertilizer_application_rate,
    generate_14_tile_adhesive_spread_rate,
    generate_15_roof_sealant_waterproofing_volume,
    generate_16_pool_chlorination_chemical_dosing,
)
from .building_concrete_ratios import (
    generate_17_concrete_bags_per_cubic_metre,
    generate_18_wheelbarrows_of_stone_and_sand,
    generate_19_wheelbarrow_litres_to_cubic_metres,
    generate_20_total_cement_bags_floor_and_walls,
    generate_21_converting_wheelbarrows_to_bucket_ratio,
    generate_22_brick_mortar_mix_volume,
    generate_23_plastering_sand_cement_ratio,
    generate_24_costing_foundation_concrete_materials,
)
from .cooking_imperial_units import (
    generate_25_recipe_cups_tablespoons_to_ml,
    generate_26_scaling_recipe_yield_quantities,
    generate_27_dry_ingredient_cup_to_grams,
    generate_28_oven_temperature_celsius_to_fahrenheit,
    generate_29_oven_temperature_fahrenheit_to_celsius,
    generate_30_mass_pounds_ounces_to_kg,
    generate_31_liquid_fluid_ounces_pints_to_litres,
    generate_32_cost_per_unit_volume_comparison,
)
from .travel_timetables_transit import (
    generate_33_reading_transit_timetable_departures,
    generate_34_calculating_arrival_time_given_duration,
    generate_35_total_travel_fare_family_group,
    generate_36_feasibility_of_day_trip_excursion,
    generate_37_latest_departure_time_with_buffer,
    generate_38_elapsed_time_crossing_midnight,
    generate_39_multi_leg_journey_layover_scheduling,
    generate_40_delay_impact_on_scheduled_itinerary,
)
from .speed_distance_time import (
    generate_41_decimal_hours_to_hours_and_minutes,
    generate_42_hours_and_minutes_to_decimal_hours,
    generate_43_average_speed_calculation,
    generate_44_travel_time_with_rest_stops,
    generate_45_estimated_arrival_with_traffic_slowdown,
    generate_46_fuel_consumption_during_journey,
)
from .tides_daylight_timezones import (
    generate_47_reading_high_and_low_tide_times,
    generate_48_calculating_tidal_range,
    generate_49_elapsed_time_between_tides,
    generate_50_safe_boating_water_depth_window,
    generate_51_sunrise_sunset_daylight_duration,
    generate_52_international_time_zones_travel,
)

SUBSKILL_LIST: List[Tuple[str, str, Callable[[random.Random], Dict[str, Any]]]] = [
    ("01_calculated_volume_to_liquid_litres", "Calculated volume cm3 to ml and litres conversion", generate_01_calculated_volume_to_liquid_litres),
    ("02_cubic_metres_to_kilolitres", "Cubic metres to kilolitres and litres conversion", generate_02_cubic_metres_to_kilolitres),
    ("03_millimetres_cubed_to_millilitres", "Millimetres cubed to millilitres laboratory conversion", generate_03_millimetres_cubed_to_millilitres),
    ("04_liquid_volume_to_mass_density", "Liquid volume to mass in kg using liquid density", generate_04_liquid_volume_to_mass_density),
    ("05_cylindrical_tank_capacity_litres", "Cylindrical JoJo rainwater harvesting tank capacity", generate_05_cylindrical_tank_capacity_litres),
    ("06_swimming_pool_drainage_time", "Swimming pool drainage duration given pump discharge rate", generate_06_swimming_pool_drainage_time),
    ("07_municipal_water_meter_kl_to_litres", "Municipal water meter consumption kl to daily litres", generate_07_municipal_water_meter_kl_to_litres),
    ("08_aggregate_sand_weight_to_volume", "Bulk aggregate sand tonnes to m3 and tipper truck loads", generate_08_aggregate_sand_weight_to_volume),
    ("09_paint_spread_rate_single_coat", "Wall paint spread rate calculation for single coat", generate_09_paint_spread_rate_single_coat),
    ("10_multi_coat_paint_tin_packaging", "Multi-coat paint volume and 5-litre tin packaging", generate_10_multi_coat_paint_tin_packaging),
    ("11_costing_paint_tins_total", "Costing complete paint requirements across tin sizes", generate_11_costing_paint_tins_total),
    ("12_agricultural_pesticide_ratio_coverage", "Agricultural weed pesticide concentrate ratio coverage", generate_12_agricultural_pesticide_ratio_coverage),
    ("13_lawn_fertilizer_application_rate", "Granular lawn fertilizer spread rate and bag requirements", generate_13_lawn_fertilizer_application_rate),
    ("14_tile_adhesive_spread_rate", "Tile adhesive floor area spread rate and bag packaging", generate_14_tile_adhesive_spread_rate),
    ("15_roof_sealant_waterproofing_volume", "Roof waterproofing liquid membrane volume and drums", generate_15_roof_sealant_waterproofing_volume),
    ("16_pool_chlorination_chemical_dosing", "Pool shock treatment chemical dosing per 10 000 litres", generate_16_pool_chlorination_chemical_dosing),
    ("17_concrete_bags_per_cubic_metre", "Medium strength concrete slab cement bags per m3", generate_17_concrete_bags_per_cubic_metre),
    ("18_wheelbarrows_of_stone_and_sand", "Foundation trench concrete wheelbarrows of stone and sand", generate_18_wheelbarrows_of_stone_and_sand),
    ("19_wheelbarrow_litres_to_cubic_metres", "Wheelbarrow volume in litres to cubic metres to order", generate_19_wheelbarrow_litres_to_cubic_metres),
    ("20_total_cement_bags_floor_and_walls", "Combined floor and wall foundation cement bags rounding", generate_20_total_cement_bags_floor_and_walls),
    ("21_converting_wheelbarrows_to_bucket_ratio", "Converting wheelbarrow proportions to bucket volume ratio", generate_21_converting_wheelbarrows_to_bucket_ratio),
    ("22_brick_mortar_mix_volume", "Mortar volume and cement bags required for brickwork", generate_22_brick_mortar_mix_volume),
    ("23_plastering_sand_cement_ratio", "Plastering 1:4 volumetric sand and cement requirements", generate_23_plastering_sand_cement_ratio),
    ("24_costing_foundation_concrete_materials", "Material quotation invoice costing with VAT", generate_24_costing_foundation_concrete_materials),
    ("25_recipe_cups_tablespoons_to_ml", "Recipe cups, tablespoons, and teaspoons converted to ml", generate_25_recipe_cups_tablespoons_to_ml),
    ("26_scaling_recipe_yield_quantities", "Proportionally scaling recipe yields for large events", generate_26_scaling_recipe_yield_quantities),
    ("27_dry_ingredient_cup_to_grams", "Converting dry ingredient volume in cups to mass in grams", generate_27_dry_ingredient_cup_to_grams),
    ("28_oven_temperature_celsius_to_fahrenheit", "Oven temperature conversion Celsius to Fahrenheit", generate_28_oven_temperature_celsius_to_fahrenheit),
    ("29_oven_temperature_fahrenheit_to_celsius", "Oven temperature conversion Fahrenheit to Celsius", generate_29_oven_temperature_fahrenheit_to_celsius),
    ("30_mass_pounds_ounces_to_kg", "Imperial pounds and ounces converted to kilograms", generate_30_mass_pounds_ounces_to_kg),
    ("31_liquid_fluid_ounces_pints_to_litres", "US fluid ounces and pints converted to litres", generate_31_liquid_fluid_ounces_pints_to_litres),
    ("32_cost_per_unit_volume_comparison", "Supermarket price per 100 ml unit volume comparison", generate_32_cost_per_unit_volume_comparison),
    ("33_reading_transit_timetable_departures", "Reading departure and arrival times from transit timetables", generate_33_reading_transit_timetable_departures),
    ("34_calculating_arrival_time_given_duration", "Calculating arrival time by adding journey duration", generate_34_calculating_arrival_time_given_duration),
    ("35_total_travel_fare_family_group", "Total passenger travel fares for family tour groups", generate_35_total_travel_fare_family_group),
    ("36_feasibility_of_day_trip_excursion", "Evaluating feasibility of day trip excursion duration", generate_36_feasibility_of_day_trip_excursion),
    ("37_latest_departure_time_with_buffer", "Latest hotel departure time with travel time and buffer", generate_37_latest_departure_time_with_buffer),
    ("38_elapsed_time_crossing_midnight", "Elapsed journey time for overnight transit crossing midnight", generate_38_elapsed_time_crossing_midnight),
    ("39_multi_leg_journey_layover_scheduling", "Multi-leg journey layover waiting times and total transit", generate_39_multi_leg_journey_layover_scheduling),
    ("40_delay_impact_on_scheduled_itinerary", "Transit departure delay impact on arrival schedule", generate_40_delay_impact_on_scheduled_itinerary),
    ("41_decimal_hours_to_hours_and_minutes", "Converting decimal hours into exact hours and minutes", generate_41_decimal_hours_to_hours_and_minutes),
    ("42_hours_and_minutes_to_decimal_hours", "Converting hours and minutes to decimal hours for formulas", generate_42_hours_and_minutes_to_decimal_hours),
    ("43_average_speed_calculation", "Calculating average speed in km/h from distance and time", generate_43_average_speed_calculation),
    ("44_travel_time_with_rest_stops", "Total travel time including highway driver rest stops", generate_44_travel_time_with_rest_stops),
    ("45_estimated_arrival_with_traffic_slowdown", "Travel delay resulting from speed reduction in roadworks", generate_45_estimated_arrival_with_traffic_slowdown),
    ("46_fuel_consumption_during_journey", "Total fuel consumption in litres and petrol cost on journey", generate_46_fuel_consumption_during_journey),
    ("47_reading_high_and_low_tide_times", "Reading high and low tide times and heights from tide table", generate_47_reading_high_and_low_tide_times),
    ("48_calculating_tidal_range", "Calculating tidal range from high and low tide water levels", generate_48_calculating_tidal_range),
    ("49_elapsed_time_between_tides", "Elapsed time duration between consecutive high and low tides", generate_49_elapsed_time_between_tides),
    ("50_safe_boating_water_depth_window", "Assessing safe water depth draft window for boat launch", generate_50_safe_boating_water_depth_window),
    ("51_sunrise_sunset_daylight_duration", "Calculating daylight duration from sunrise and sunset times", generate_51_sunrise_sunset_daylight_duration),
    ("52_international_time_zones_travel", "International flight destination arrival time across time zones", generate_52_international_time_zones_travel),
]

SUBSKILL_DISPATCH: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
SUBSKILL_METADATA: Dict[str, Dict[str, str]] = {}

for idx, (subskill_key, name, fn) in enumerate(SUBSKILL_LIST, start=1):
    num_str = f"{idx:02d}"
    SUBSKILL_DISPATCH[subskill_key] = fn
    SUBSKILL_DISPATCH[num_str] = fn
    SUBSKILL_DISPATCH[str(idx)] = fn
    SUBSKILL_DISPATCH[f"gr12_conv_{num_str}"] = fn

    SUBSKILL_METADATA[subskill_key] = {
        "index": num_str,
        "name": name,
        "topic": "grade12_mathlit_conversions_and_time",
        "key": f"gr12_conv_{num_str}",
    }


def generate_subskill(subskill: str | int, r: random.Random) -> Dict[str, Any]:
    """Generate a question for the requested subskill."""
    key = str(subskill).strip()
    fn = SUBSKILL_DISPATCH.get(key)
    if fn is None:
        fn = r.choice(list(SUBSKILL_DISPATCH.values()))
    return fn(r)
