"""Measuring sub-package consolidating all 5 clusters for Grade 10 Mathematical Literacy."""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

from .length_distance import (
    _gen_meas_len_est_body_parts,
    _gen_meas_len_instrument_selection,
    _gen_meas_len_ruler_reading_subdivisions,
    _gen_meas_len_tape_measure_furniture,
    _gen_meas_len_trundle_wheel_sports_field,
    _gen_meas_len_odometer_reading_trip,
    _gen_meas_len_cost_per_metre_fabric,
    _gen_meas_len_cost_ribbon_binding,
    _gen_meas_len_fencing_perimeter_wire,
    _gen_meas_len_fencing_poles_spacing,
    _gen_meas_len_timber_planks_cutting_wastage,
    _gen_meas_len_tablecloth_overhang,
)

from .mass_weight import (
    _gen_meas_mass_scale_instrument_selection,
    _gen_meas_mass_analog_kitchen_dial_subdivisions,
    _gen_meas_mass_gross_tare_net_calculation,
    _gen_meas_mass_bathroom_scale_tracking,
    _gen_meas_mass_schoolbag_health_ratio,
    _gen_meas_mass_loose_produce_cost_per_kg,
    _gen_meas_mass_fertilizer_field_bulk_cost,
    _gen_meas_mass_building_sand_tonnes_bags,
    _gen_meas_mass_butchery_meat_portioning,
    _gen_meas_mass_postage_courier_tier_pricing,
    _gen_meas_mass_unit_price_best_value,
    _gen_meas_mass_baby_clinic_growth_chart,
    _gen_meas_mass_animal_veterinary_dosage,
)

from .volume_capacity import (
    _gen_meas_vol_jug_meniscus_reading,
    _gen_meas_vol_measuring_cylinder_precision,
    _gen_meas_vol_office_urn_tea_servings,
    _gen_meas_vol_urn_percentage_remaining,
    _gen_meas_vol_garden_bucket_trips,
    _gen_meas_vol_medicine_liquid_dosage_duration,
    _gen_meas_vol_medicine_dosage_bottles_to_buy,
    _gen_meas_vol_paint_spreading_rate_litres,
    _gen_meas_vol_paint_can_sizes_selection,
    _gen_meas_vol_fuel_tank_fillup_cost,
    _gen_meas_vol_fuel_litres_from_cash_budget,
    _gen_meas_vol_paraffin_lamp_refills,
    _gen_meas_vol_beverage_cost_per_litre,
)

from .temperature_integrated import (
    _gen_meas_temp_thermometer_types,
    _gen_meas_temp_reading_mercury_alcohol_column,
    _gen_meas_temp_fever_threshold_interpretation,
    _gen_meas_temp_daily_body_temp_fluctuation,
    _gen_meas_temp_weather_report_min_max,
    _gen_meas_temp_weather_sub_zero_frost,
    _gen_meas_temp_oven_preheating_adjustment,
    _gen_meas_temp_food_safety_danger_zone,
    _gen_meas_integ_recipe_multi_cake_scaling,
    _gen_meas_integ_recipe_liquid_volume_litres,
    _gen_meas_integ_recipe_eggs_box_packaging,
    _gen_meas_integ_recipe_ingredient_costing,
    _gen_meas_integ_garden_lawn_fertilizer_coverage,
    _gen_meas_integ_rainwater_harvesting_tank_days,
)

SUBSKILLS = [
    # Cluster 1: Length & Distance Measurement & Estimation (12 Archetypes)
    "meas_len_est_body_parts",
    "meas_len_instrument_selection",
    "meas_len_ruler_reading_subdivisions",
    "meas_len_tape_measure_furniture",
    "meas_len_trundle_wheel_sports_field",
    "meas_len_odometer_reading_trip",
    "meas_len_cost_per_metre_fabric",
    "meas_len_cost_ribbon_binding",
    "meas_len_fencing_perimeter_wire",
    "meas_len_fencing_poles_spacing",
    "meas_len_timber_planks_cutting_wastage",
    "meas_len_tablecloth_overhang",

    # Cluster 2: Mass & Weight Measurement, Scales & Practical Costs (13 Archetypes)
    "meas_mass_scale_instrument_selection",
    "meas_mass_analog_kitchen_dial_subdivisions",
    "meas_mass_gross_tare_net_calculation",
    "meas_mass_bathroom_scale_tracking",
    "meas_mass_schoolbag_health_ratio",
    "meas_mass_loose_produce_cost_per_kg",
    "meas_mass_fertilizer_field_bulk_cost",
    "meas_mass_building_sand_tonnes_bags",
    "meas_mass_butchery_meat_portioning",
    "meas_mass_postage_courier_tier_pricing",
    "meas_mass_unit_price_best_value",
    "meas_mass_baby_clinic_growth_chart",
    "meas_mass_animal_veterinary_dosage",

    # Cluster 3: Volume & Capacity Measurement & Liquid Costing (13 Archetypes)
    "meas_vol_jug_meniscus_reading",
    "meas_vol_measuring_cylinder_precision",
    "meas_vol_office_urn_tea_servings",
    "meas_vol_urn_percentage_remaining",
    "meas_vol_garden_bucket_trips",
    "meas_vol_medicine_liquid_dosage_duration",
    "meas_vol_medicine_dosage_bottles_to_buy",
    "meas_vol_paint_spreading_rate_litres",
    "meas_vol_paint_can_sizes_selection",
    "meas_vol_fuel_tank_fillup_cost",
    "meas_vol_fuel_litres_from_cash_budget",
    "meas_vol_paraffin_lamp_refills",
    "meas_vol_beverage_cost_per_litre",

    # Cluster 4: Temperature Measurement, Weather & Thermal Applications (8 Archetypes)
    "meas_temp_thermometer_types",
    "meas_temp_reading_mercury_alcohol_column",
    "meas_temp_fever_threshold_interpretation",
    "meas_temp_daily_body_temp_fluctuation",
    "meas_temp_weather_report_min_max",
    "meas_temp_weather_sub_zero_frost",
    "meas_temp_oven_preheating_adjustment",
    "meas_temp_food_safety_danger_zone",

    # Cluster 5: Integrated Measurement, Recipe Costing & Multi-Step Applications (6 Archetypes)
    "meas_integ_recipe_multi_cake_scaling",
    "meas_integ_recipe_liquid_volume_litres",
    "meas_integ_recipe_eggs_box_packaging",
    "meas_integ_recipe_ingredient_costing",
    "meas_integ_garden_lawn_fertilizer_coverage",
    "meas_integ_rainwater_harvesting_tank_days",
]

DISPATCH_TABLE = {
    # Cluster 1
    "meas_len_est_body_parts": _gen_meas_len_est_body_parts,
    "meas_len_instrument_selection": _gen_meas_len_instrument_selection,
    "meas_len_ruler_reading_subdivisions": _gen_meas_len_ruler_reading_subdivisions,
    "meas_len_tape_measure_furniture": _gen_meas_len_tape_measure_furniture,
    "meas_len_trundle_wheel_sports_field": _gen_meas_len_trundle_wheel_sports_field,
    "meas_len_odometer_reading_trip": _gen_meas_len_odometer_reading_trip,
    "meas_len_cost_per_metre_fabric": _gen_meas_len_cost_per_metre_fabric,
    "meas_len_cost_ribbon_binding": _gen_meas_len_cost_ribbon_binding,
    "meas_len_fencing_perimeter_wire": _gen_meas_len_fencing_perimeter_wire,
    "meas_len_fencing_poles_spacing": _gen_meas_len_fencing_poles_spacing,
    "meas_len_timber_planks_cutting_wastage": _gen_meas_len_timber_planks_cutting_wastage,
    "meas_len_tablecloth_overhang": _gen_meas_len_tablecloth_overhang,

    # Cluster 2
    "meas_mass_scale_instrument_selection": _gen_meas_mass_scale_instrument_selection,
    "meas_mass_analog_kitchen_dial_subdivisions": _gen_meas_mass_analog_kitchen_dial_subdivisions,
    "meas_mass_gross_tare_net_calculation": _gen_meas_mass_gross_tare_net_calculation,
    "meas_mass_bathroom_scale_tracking": _gen_meas_mass_bathroom_scale_tracking,
    "meas_mass_schoolbag_health_ratio": _gen_meas_mass_schoolbag_health_ratio,
    "meas_mass_loose_produce_cost_per_kg": _gen_meas_mass_loose_produce_cost_per_kg,
    "meas_mass_fertilizer_field_bulk_cost": _gen_meas_mass_fertilizer_field_bulk_cost,
    "meas_mass_building_sand_tonnes_bags": _gen_meas_mass_building_sand_tonnes_bags,
    "meas_mass_butchery_meat_portioning": _gen_meas_mass_butchery_meat_portioning,
    "meas_mass_postage_courier_tier_pricing": _gen_meas_mass_postage_courier_tier_pricing,
    "meas_mass_unit_price_best_value": _gen_meas_mass_unit_price_best_value,
    "meas_mass_baby_clinic_growth_chart": _gen_meas_mass_baby_clinic_growth_chart,
    "meas_mass_animal_veterinary_dosage": _gen_meas_mass_animal_veterinary_dosage,

    # Cluster 3
    "meas_vol_jug_meniscus_reading": _gen_meas_vol_jug_meniscus_reading,
    "meas_vol_measuring_cylinder_precision": _gen_meas_vol_measuring_cylinder_precision,
    "meas_vol_office_urn_tea_servings": _gen_meas_vol_office_urn_tea_servings,
    "meas_vol_urn_percentage_remaining": _gen_meas_vol_urn_percentage_remaining,
    "meas_vol_garden_bucket_trips": _gen_meas_vol_garden_bucket_trips,
    "meas_vol_medicine_liquid_dosage_duration": _gen_meas_vol_medicine_liquid_dosage_duration,
    "meas_vol_medicine_dosage_bottles_to_buy": _gen_meas_vol_medicine_dosage_bottles_to_buy,
    "meas_vol_paint_spreading_rate_litres": _gen_meas_vol_paint_spreading_rate_litres,
    "meas_vol_paint_can_sizes_selection": _gen_meas_vol_paint_can_sizes_selection,
    "meas_vol_fuel_tank_fillup_cost": _gen_meas_vol_fuel_tank_fillup_cost,
    "meas_vol_fuel_litres_from_cash_budget": _gen_meas_vol_fuel_litres_from_cash_budget,
    "meas_vol_paraffin_lamp_refills": _gen_meas_vol_paraffin_lamp_refills,
    "meas_vol_beverage_cost_per_litre": _gen_meas_vol_beverage_cost_per_litre,

    # Cluster 4
    "meas_temp_thermometer_types": _gen_meas_temp_thermometer_types,
    "meas_temp_reading_mercury_alcohol_column": _gen_meas_temp_reading_mercury_alcohol_column,
    "meas_temp_fever_threshold_interpretation": _gen_meas_temp_fever_threshold_interpretation,
    "meas_temp_daily_body_temp_fluctuation": _gen_meas_temp_daily_body_temp_fluctuation,
    "meas_temp_weather_report_min_max": _gen_meas_temp_weather_report_min_max,
    "meas_temp_weather_sub_zero_frost": _gen_meas_temp_weather_sub_zero_frost,
    "meas_temp_oven_preheating_adjustment": _gen_meas_temp_oven_preheating_adjustment,
    "meas_temp_food_safety_danger_zone": _gen_meas_temp_food_safety_danger_zone,

    # Cluster 5
    "meas_integ_recipe_multi_cake_scaling": _gen_meas_integ_recipe_multi_cake_scaling,
    "meas_integ_recipe_liquid_volume_litres": _gen_meas_integ_recipe_liquid_volume_litres,
    "meas_integ_recipe_eggs_box_packaging": _gen_meas_integ_recipe_eggs_box_packaging,
    "meas_integ_recipe_ingredient_costing": _gen_meas_integ_recipe_ingredient_costing,
    "meas_integ_garden_lawn_fertilizer_coverage": _gen_meas_integ_garden_lawn_fertilizer_coverage,
    "meas_integ_rainwater_harvesting_tank_days": _gen_meas_integ_rainwater_harvesting_tank_days,
}

def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 10 Mathematical Literacy: Measuring Length, Weight, Volume & Temperature."""
    actual_seed = seed if seed is not None else random.randint(1, 1_000_000)
    r = random.Random(actual_seed)

    if archetype_index is not None and 0 <= archetype_index < len(SUBSKILLS):
        chosen_subskill = SUBSKILLS[archetype_index]
    elif subskill and subskill in DISPATCH_TABLE:
        chosen_subskill = subskill
    else:
        chosen_subskill = r.choice(SUBSKILLS)

    generator_fn = DISPATCH_TABLE[chosen_subskill]
    q = generator_fn(r)
    return [q]
