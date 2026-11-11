"""Grade 7 Natural Sciences: Term 3 - Heat Insulation and Energy Saving Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/04. Heat insulation and energy saving.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .ns7_heat_insulation_archetypes_01_25 import (
    arch_01_definition_of_thermal_insulator,
    arch_02_distinguishing_thermal_conductors_from_insulators,
    arch_03_role_of_trapped_air_in_insulating_materials,
    arch_04_investigating_cup_insulation_materials_comparison,
    arch_05_identifying_variables_in_insulation_investigation,
    arch_06_polystyrene_cooler_box_thermal_mechanism,
    arch_07_bubble_wrap_and_cardboard_packaging_insulation,
    arch_08_mineral_wool_and_fibreglass_ceiling_insulation,
    arch_09_cellulose_and_recycled_paper_ceiling_batts,
    arch_10_reflective_foil_radiant_barrier_in_roofs,
    arch_11_hot_box_wonderbag_thermal_cooking_concept,
    arch_12_hot_box_food_safety_and_fuel_saving_benefits,
    arch_13_solar_water_heater_storage_tank_insulation,
    arch_14_evacuated_glass_tube_solar_collector_insulation,
    arch_15_insulating_hot_water_copper_pipes,
    arch_16_geyser_blanket_energy_conservation_impact,
    arch_17_setting_geyser_thermostat_temperature_efficiency,
    arch_18_thatch_grass_roof_versus_corrugated_iron_sheet,
    arch_19_mud_brick_thermal_mass_in_traditional_dwellings,
    arch_20_corrugated_iron_shack_temperature_extremes,
    arch_21_passive_solar_building_orientation_south_africa,
    arch_22_roof_overhangs_and_eaves_seasonal_sun_angles,
    arch_23_window_placement_and_sizing_for_solar_gain,
    arch_24_thermal_curtains_pelmets_and_double_glazing,
    arch_25_shading_with_deciduous_trees_seasonal_benefit,
)
from .ns7_heat_insulation_archetypes_26_50 import (
    arch_26_thermal_mass_of_concrete_and_stone_floors,
    arch_27_white_reflective_cool_roof_technology,
    arch_28_draught_proofing_doors_and_windows,
    arch_29_animal_insulation_fur_feathers_and_blubber,
    arch_30_penguin_feather_density_and_down_layer,
    arch_31_human_goosebumps_piloerection_evolutionary_purpose,
    arch_32_thermos_flask_as_insulation_case_study,
    arch_33_comparing_energy_consumption_insulated_vs_uninsulated_home,
    arch_34_calculating_electricity_cost_savings_from_geyser_insulation,
    arch_35_calculating_temperature_retention_over_time,
    arch_36_environmental_benefit_reducing_coal_power_demand,
    arch_37_reducing_greenhouse_gas_emissions_via_insulation,
    arch_38_energy_star_and_appliance_efficiency_labels,
    arch_39_efficient_cooking_pot_lids_and_matching_plate_sizes,
    arch_40_efficient_electric_kettle_water_volume_usage,
    arch_41_refrigerator_door_seal_maintenance_and_efficiency,
    arch_42_insulation_in_clothing_layering_principle,
    arch_43_down_feather_jackets_versus_compacted_cotton,
    arch_44_fire_safety_considerations_with_thermal_insulators,
    arch_45_misconception_insulators_only_keep_things_warm_not_cold,
    arch_46_misconception_insulators_produce_thermal_energy,
    arch_47_misconception_metals_cannot_be_insulated,
    arch_48_misconception_thicker_material_is_always_better_than_trapped_air,
    arch_49_designing_an_energy_efficient_house_in_south_africa,
    arch_50_heat_insulation_and_energy_saving_comprehensive_diagnostic,
)

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    "01_definition_of_thermal_insulator": arch_01_definition_of_thermal_insulator,
    "02_distinguishing_thermal_conductors_from_insulators": arch_02_distinguishing_thermal_conductors_from_insulators,
    "03_role_of_trapped_air_in_insulating_materials": arch_03_role_of_trapped_air_in_insulating_materials,
    "04_investigating_cup_insulation_materials_comparison": arch_04_investigating_cup_insulation_materials_comparison,
    "05_identifying_variables_in_insulation_investigation": arch_05_identifying_variables_in_insulation_investigation,
    "06_polystyrene_cooler_box_thermal_mechanism": arch_06_polystyrene_cooler_box_thermal_mechanism,
    "07_bubble_wrap_and_cardboard_packaging_insulation": arch_07_bubble_wrap_and_cardboard_packaging_insulation,
    "08_mineral_wool_and_fibreglass_ceiling_insulation": arch_08_mineral_wool_and_fibreglass_ceiling_insulation,
    "09_cellulose_and_recycled_paper_ceiling_batts": arch_09_cellulose_and_recycled_paper_ceiling_batts,
    "10_reflective_foil_radiant_barrier_in_roofs": arch_10_reflective_foil_radiant_barrier_in_roofs,
    "11_hot_box_wonderbag_thermal_cooking_concept": arch_11_hot_box_wonderbag_thermal_cooking_concept,
    "12_hot_box_food_safety_and_fuel_saving_benefits": arch_12_hot_box_food_safety_and_fuel_saving_benefits,
    "13_solar_water_heater_storage_tank_insulation": arch_13_solar_water_heater_storage_tank_insulation,
    "14_evacuated_glass_tube_solar_collector_insulation": arch_14_evacuated_glass_tube_solar_collector_insulation,
    "15_insulating_hot_water_copper_pipes": arch_15_insulating_hot_water_copper_pipes,
    "16_geyser_blanket_energy_conservation_impact": arch_16_geyser_blanket_energy_conservation_impact,
    "17_setting_geyser_thermostat_temperature_efficiency": arch_17_setting_geyser_thermostat_temperature_efficiency,
    "18_thatch_grass_roof_versus_corrugated_iron_sheet": arch_18_thatch_grass_roof_versus_corrugated_iron_sheet,
    "19_mud_brick_thermal_mass_in_traditional_dwellings": arch_19_mud_brick_thermal_mass_in_traditional_dwellings,
    "20_corrugated_iron_shack_temperature_extremes": arch_20_corrugated_iron_shack_temperature_extremes,
    "21_passive_solar_building_orientation_south_africa": arch_21_passive_solar_building_orientation_south_africa,
    "22_roof_overhangs_and_eaves_seasonal_sun_angles": arch_22_roof_overhangs_and_eaves_seasonal_sun_angles,
    "23_window_placement_and_sizing_for_solar_gain": arch_23_window_placement_and_sizing_for_solar_gain,
    "24_thermal_curtains_pelmets_and_double_glazing": arch_24_thermal_curtains_pelmets_and_double_glazing,
    "25_shading_with_deciduous_trees_seasonal_benefit": arch_25_shading_with_deciduous_trees_seasonal_benefit,
    "26_thermal_mass_of_concrete_and_stone_floors": arch_26_thermal_mass_of_concrete_and_stone_floors,
    "27_white_reflective_cool_roof_technology": arch_27_white_reflective_cool_roof_technology,
    "28_draught_proofing_doors_and_windows": arch_28_draught_proofing_doors_and_windows,
    "29_animal_insulation_fur_feathers_and_blubber": arch_29_animal_insulation_fur_feathers_and_blubber,
    "30_penguin_feather_density_and_down_layer": arch_30_penguin_feather_density_and_down_layer,
    "31_human_goosebumps_piloerection_evolutionary_purpose": arch_31_human_goosebumps_piloerection_evolutionary_purpose,
    "32_thermos_flask_as_insulation_case_study": arch_32_thermos_flask_as_insulation_case_study,
    "33_comparing_energy_consumption_insulated_vs_uninsulated_home": arch_33_comparing_energy_consumption_insulated_vs_uninsulated_home,
    "34_calculating_electricity_cost_savings_from_geyser_insulation": arch_34_calculating_electricity_cost_savings_from_geyser_insulation,
    "35_calculating_temperature_retention_over_time": arch_35_calculating_temperature_retention_over_time,
    "36_environmental_benefit_reducing_coal_power_demand": arch_36_environmental_benefit_reducing_coal_power_demand,
    "37_reducing_greenhouse_gas_emissions_via_insulation": arch_37_reducing_greenhouse_gas_emissions_via_insulation,
    "38_energy_star_and_appliance_efficiency_labels": arch_38_energy_star_and_appliance_efficiency_labels,
    "39_efficient_cooking_pot_lids_and_matching_plate_sizes": arch_39_efficient_cooking_pot_lids_and_matching_plate_sizes,
    "40_efficient_electric_kettle_water_volume_usage": arch_40_efficient_electric_kettle_water_volume_usage,
    "41_refrigerator_door_seal_maintenance_and_efficiency": arch_41_refrigerator_door_seal_maintenance_and_efficiency,
    "42_insulation_in_clothing_layering_principle": arch_42_insulation_in_clothing_layering_principle,
    "43_down_feather_jackets_versus_compacted_cotton": arch_43_down_feather_jackets_versus_compacted_cotton,
    "44_fire_safety_considerations_with_thermal_insulators": arch_44_fire_safety_considerations_with_thermal_insulators,
    "45_misconception_insulators_only_keep_things_warm_not_cold": arch_45_misconception_insulators_only_keep_things_warm_not_cold,
    "46_misconception_insulators_produce_thermal_energy": arch_46_misconception_insulators_produce_thermal_energy,
    "47_misconception_metals_cannot_be_insulated": arch_47_misconception_metals_cannot_be_insulated,
    "48_misconception_thicker_material_is_always_better_than_trapped_air": arch_48_misconception_thicker_material_is_always_better_than_trapped_air,
    "49_designing_an_energy_efficient_house_in_south_africa": arch_49_designing_an_energy_efficient_house_in_south_africa,
    "50_heat_insulation_and_energy_saving_comprehensive_diagnostic": arch_50_heat_insulation_and_energy_saving_comprehensive_diagnostic,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed) if seed is not None else random.Random()
    if subskill is None or subskill not in ARCHETYPE_BUILDERS:
        subskill = rng.choice(SUBSKILLS)
    builder = ARCHETYPE_BUILDERS[subskill]
    return builder(rng)


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    target = str(subskill or "").strip().lower()
    chosen_sub: Optional[str] = None
    if target in ARCHETYPE_BUILDERS:
        chosen_sub = target
    else:
        for k in ARCHETYPE_BUILDERS:
            if target and (target in k.lower() or k.lower() in target):
                chosen_sub = k
                break

    for i in range(count):
        active = chosen_sub if chosen_sub else SUBSKILLS[(i + (seed or 0)) % len(SUBSKILLS)]
        builder = ARCHETYPE_BUILDERS[active]
        q = builder(rng)
        questions.append(q)

    return questions
