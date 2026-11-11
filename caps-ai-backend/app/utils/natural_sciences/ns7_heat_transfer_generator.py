"""Grade 7 Natural Sciences: Term 3 - Heat Energy Transfer Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/03. Heat Energy transfer.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .ns7_heat_transfer_archetypes_01_25 import (
    arch_01_heat_versus_temperature_definitions,
    arch_02_measuring_temperature_degrees_celsius,
    arch_03_thermal_energy_and_particle_kinetic_energy,
    arch_04_direction_of_heat_transfer_gradient,
    arch_05_thermal_equilibrium_concept,
    arch_06_particle_mechanism_of_conduction_in_solids,
    arch_07_role_of_free_electrons_in_metal_conduction,
    arch_08_comparing_thermal_conductivity_of_different_metals,
    arch_09_wax_melting_pin_drop_conduction_experiment,
    arch_10_why_metal_feels_colder_than_wood_at_same_temp,
    arch_11_practical_design_of_cooking_pots_and_handles,
    arch_12_conduction_in_liquids_and_gases_poor_conductors,
    arch_13_particle_mechanism_of_convection_in_fluids,
    arch_14_density_changes_driving_convection_currents,
    arch_15_potassium_permanganate_convection_experiment,
    arch_16_smoke_box_chimney_air_convection_demonstration,
    arch_17_sea_breeze_daytime_convection_cycle,
    arch_18_land_breeze_nighttime_convection_cycle,
    arch_19_placement_of_heaters_near_floor,
    arch_20_placement_of_air_conditioners_near_ceiling,
    arch_21_geyser_heating_element_placement_at_bottom,
    arch_22_hot_water_circulation_in_domestic_pipes,
    arch_23_nature_of_thermal_radiation_infrared_waves,
    arch_24_heat_transfer_through_vacuum_from_the_sun,
    arch_25_comparing_medium_requirements_conduction_convection_radiation,
)
from .ns7_heat_transfer_archetypes_26_50 import (
    arch_26_matt_black_versus_shiny_white_absorbers_experiment,
    arch_27_matt_black_versus_shiny_white_emitters_experiment,
    arch_28_solar_collector_plates_black_surface_selection,
    arch_29_silver_emergency_space_blanket_reflection,
    arch_30_thermos_vacuum_flask_conduction_prevention,
    arch_31_thermos_vacuum_flask_convection_prevention,
    arch_32_thermos_vacuum_flask_radiation_prevention,
    arch_33_identifying_heat_transfer_in_boiling_kettle,
    arch_34_identifying_heat_transfer_around_a_campfire,
    arch_35_identifying_heat_transfer_in_domestic_oven,
    arch_36_heat_transfer_in_refrigerator_cooling_coils,
    arch_37_car_radiator_cooling_system_heat_loss,
    arch_38_greenhouse_effect_trapping_thermal_radiation,
    arch_39_hot_drink_cooling_rate_investigation_variables,
    arch_40_reading_cooling_curve_temperature_versus_time,
    arch_41_calculating_temperature_drop_over_time,
    arch_42_calculating_thermal_energy_transfer_rate_concept,
    arch_43_identifying_conduction_convection_radiation_in_daily_life,
    arch_44_traditional_african_thatch_roof_thermal_properties,
    arch_45_misconception_cold_is_transferred_not_heat,
    arch_46_misconception_temperature_and_heat_are_identical,
    arch_47_misconception_sweaters_and_blankets_generate_heat,
    arch_48_misconception_radiation_only_occurs_from_nuclear_sources,
    arch_49_improving_thermal_efficiency_of_home_appliance,
    arch_50_heat_energy_transfer_comprehensive_diagnostic,
)

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    "01_heat_versus_temperature_definitions": arch_01_heat_versus_temperature_definitions,
    "02_measuring_temperature_degrees_celsius": arch_02_measuring_temperature_degrees_celsius,
    "03_thermal_energy_and_particle_kinetic_energy": arch_03_thermal_energy_and_particle_kinetic_energy,
    "04_direction_of_heat_transfer_gradient": arch_04_direction_of_heat_transfer_gradient,
    "05_thermal_equilibrium_concept": arch_05_thermal_equilibrium_concept,
    "06_particle_mechanism_of_conduction_in_solids": arch_06_particle_mechanism_of_conduction_in_solids,
    "07_role_of_free_electrons_in_metal_conduction": arch_07_role_of_free_electrons_in_metal_conduction,
    "08_comparing_thermal_conductivity_of_different_metals": arch_08_comparing_thermal_conductivity_of_different_metals,
    "09_wax_melting_pin_drop_conduction_experiment": arch_09_wax_melting_pin_drop_conduction_experiment,
    "10_why_metal_feels_colder_than_wood_at_same_temp": arch_10_why_metal_feels_colder_than_wood_at_same_temp,
    "11_practical_design_of_cooking_pots_and_handles": arch_11_practical_design_of_cooking_pots_and_handles,
    "12_conduction_in_liquids_and_gases_poor_conductors": arch_12_conduction_in_liquids_and_gases_poor_conductors,
    "13_particle_mechanism_of_convection_in_fluids": arch_13_particle_mechanism_of_convection_in_fluids,
    "14_density_changes_driving_convection_currents": arch_14_density_changes_driving_convection_currents,
    "15_potassium_permanganate_convection_experiment": arch_15_potassium_permanganate_convection_experiment,
    "16_smoke_box_chimney_air_convection_demonstration": arch_16_smoke_box_chimney_air_convection_demonstration,
    "17_sea_breeze_daytime_convection_cycle": arch_17_sea_breeze_daytime_convection_cycle,
    "18_land_breeze_nighttime_convection_cycle": arch_18_land_breeze_nighttime_convection_cycle,
    "19_placement_of_heaters_near_floor": arch_19_placement_of_heaters_near_floor,
    "20_placement_of_air_conditioners_near_ceiling": arch_20_placement_of_air_conditioners_near_ceiling,
    "21_geyser_heating_element_placement_at_bottom": arch_21_geyser_heating_element_placement_at_bottom,
    "22_hot_water_circulation_in_domestic_pipes": arch_22_hot_water_circulation_in_domestic_pipes,
    "23_nature_of_thermal_radiation_infrared_waves": arch_23_nature_of_thermal_radiation_infrared_waves,
    "24_heat_transfer_through_vacuum_from_the_sun": arch_24_heat_transfer_through_vacuum_from_the_sun,
    "25_comparing_medium_requirements_conduction_convection_radiation": arch_25_comparing_medium_requirements_conduction_convection_radiation,
    "26_matt_black_versus_shiny_white_absorbers_experiment": arch_26_matt_black_versus_shiny_white_absorbers_experiment,
    "27_matt_black_versus_shiny_white_emitters_experiment": arch_27_matt_black_versus_shiny_white_emitters_experiment,
    "28_solar_collector_plates_black_surface_selection": arch_28_solar_collector_plates_black_surface_selection,
    "29_silver_emergency_space_blanket_reflection": arch_29_silver_emergency_space_blanket_reflection,
    "30_thermos_vacuum_flask_conduction_prevention": arch_30_thermos_vacuum_flask_conduction_prevention,
    "31_thermos_vacuum_flask_convection_prevention": arch_31_thermos_vacuum_flask_convection_prevention,
    "32_thermos_vacuum_flask_radiation_prevention": arch_32_thermos_vacuum_flask_radiation_prevention,
    "33_identifying_heat_transfer_in_boiling_kettle": arch_33_identifying_heat_transfer_in_boiling_kettle,
    "34_identifying_heat_transfer_around_a_campfire": arch_34_identifying_heat_transfer_around_a_campfire,
    "35_identifying_heat_transfer_in_domestic_oven": arch_35_identifying_heat_transfer_in_domestic_oven,
    "36_heat_transfer_in_refrigerator_cooling_coils": arch_36_heat_transfer_in_refrigerator_cooling_coils,
    "37_car_radiator_cooling_system_heat_loss": arch_37_car_radiator_cooling_system_heat_loss,
    "38_greenhouse_effect_trapping_thermal_radiation": arch_38_greenhouse_effect_trapping_thermal_radiation,
    "39_hot_drink_cooling_rate_investigation_variables": arch_39_hot_drink_cooling_rate_investigation_variables,
    "40_reading_cooling_curve_temperature_versus_time": arch_40_reading_cooling_curve_temperature_versus_time,
    "41_calculating_temperature_drop_over_time": arch_41_calculating_temperature_drop_over_time,
    "42_calculating_thermal_energy_transfer_rate_concept": arch_42_calculating_thermal_energy_transfer_rate_concept,
    "43_identifying_conduction_convection_radiation_in_daily_life": arch_43_identifying_conduction_convection_radiation_in_daily_life,
    "44_traditional_african_thatch_roof_thermal_properties": arch_44_traditional_african_thatch_roof_thermal_properties,
    "45_misconception_cold_is_transferred_not_heat": arch_45_misconception_cold_is_transferred_not_heat,
    "46_misconception_temperature_and_heat_are_identical": arch_46_misconception_temperature_and_heat_are_identical,
    "47_misconception_sweaters_and_blankets_generate_heat": arch_47_misconception_sweaters_and_blankets_generate_heat,
    "48_misconception_radiation_only_occurs_from_nuclear_sources": arch_48_misconception_radiation_only_occurs_from_nuclear_sources,
    "49_improving_thermal_efficiency_of_home_appliance": arch_49_improving_thermal_efficiency_of_home_appliance,
    "50_heat_energy_transfer_comprehensive_diagnostic": arch_50_heat_energy_transfer_comprehensive_diagnostic,
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
