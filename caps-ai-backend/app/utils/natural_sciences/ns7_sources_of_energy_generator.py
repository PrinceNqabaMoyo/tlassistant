"""Grade 7 Natural Sciences: Term 3 - Sources of Energy Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/01. Sources of energy.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .ns7_sources_of_energy_archetypes_01_25 import (
    arch_01_concept_of_energy_source,
    arch_02_renewable_definition_and_criterion,
    arch_03_nonrenewable_definition_and_criterion,
    arch_04_classify_solar_and_wind_energy,
    arch_05_classify_coal_and_petroleum,
    arch_06_classify_natural_gas_and_methane,
    arch_07_classify_nuclear_uranium_fuel,
    arch_08_classify_biofuels_wood_and_manure,
    arch_09_fossil_fuel_formation_coal_swamps,
    arch_10_fossil_fuel_formation_crude_oil_marine,
    arch_11_fossil_fuel_formation_natural_gas,
    arch_12_geological_time_scale_fossil_fuels,
    arch_13_south_africa_coal_dependence_reasons,
    arch_14_eskom_thermal_power_stations_process,
    arch_15_crude_oil_fractionation_products,
    arch_16_natural_gas_methane_properties,
    arch_17_uranium_atomic_properties_and_symbol,
    arch_18_nuclear_fission_energy_release,
    arch_19_koeberg_nuclear_power_station_context,
    arch_20_nuclear_power_advantages_emissions,
    arch_21_nuclear_power_disadvantages_radioactive_waste,
    arch_22_natural_greenhouse_effect_mechanism,
    arch_23_greenhouse_gases_identification,
    arch_24_enhanced_greenhouse_effect_fossil_combustion,
    arch_25_global_warming_consequences_south_africa,
)
from .ns7_sources_of_energy_archetypes_26_50 import (
    arch_26_solar_energy_photovoltaic_conversion,
    arch_27_solar_thermal_water_heaters,
    arch_28_solar_potential_northern_cape,
    arch_29_wind_energy_turbine_mechanism,
    arch_30_wind_energy_geographic_location_coastal,
    arch_31_wind_energy_advantages_and_disadvantages,
    arch_32_hydropower_gravitational_potential_conversion,
    arch_33_gariep_dam_hydroelectric_scheme,
    arch_34_pumped_storage_schemes_drakensberg,
    arch_35_hydropower_advantages_and_limitations,
    arch_36_biofuel_definition_and_feedstocks,
    arch_37_biogas_anaerobic_digester_process,
    arch_38_biogas_case_study_farm_manure_benefits,
    arch_39_bioethanol_vs_petroleum_comparison,
    arch_40_wood_as_energy_source_sustainability,
    arch_41_indoor_air_pollution_wood_coal_braziers,
    arch_42_acid_rain_causes_coal_combustion,
    arch_43_acid_rain_impact_environment_materials,
    arch_44_energy_source_comparison_table_cost_reliability,
    arch_45_baseload_vs_intermittent_power_grid,
    arch_46_energy_conservation_in_households,
    arch_47_renewable_energy_myths_and_facts,
    arch_48_misconception_clean_infinite_vs_renewable,
    arch_49_misconception_nuclear_vs_fossil_smoke,
    arch_50_sources_of_energy_comprehensive_diagnostic,
)

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    "01_concept_of_energy_source": arch_01_concept_of_energy_source,
    "02_renewable_definition_and_criterion": arch_02_renewable_definition_and_criterion,
    "03_nonrenewable_definition_and_criterion": arch_03_nonrenewable_definition_and_criterion,
    "04_classify_solar_and_wind_energy": arch_04_classify_solar_and_wind_energy,
    "05_classify_coal_and_petroleum": arch_05_classify_coal_and_petroleum,
    "06_classify_natural_gas_and_methane": arch_06_classify_natural_gas_and_methane,
    "07_classify_nuclear_uranium_fuel": arch_07_classify_nuclear_uranium_fuel,
    "08_classify_biofuels_wood_and_manure": arch_08_classify_biofuels_wood_and_manure,
    "09_fossil_fuel_formation_coal_swamps": arch_09_fossil_fuel_formation_coal_swamps,
    "10_fossil_fuel_formation_crude_oil_marine": arch_10_fossil_fuel_formation_crude_oil_marine,
    "11_fossil_fuel_formation_natural_gas": arch_11_fossil_fuel_formation_natural_gas,
    "12_geological_time_scale_fossil_fuels": arch_12_geological_time_scale_fossil_fuels,
    "13_south_africa_coal_dependence_reasons": arch_13_south_africa_coal_dependence_reasons,
    "14_eskom_thermal_power_stations_process": arch_14_eskom_thermal_power_stations_process,
    "15_crude_oil_fractionation_products": arch_15_crude_oil_fractionation_products,
    "16_natural_gas_methane_properties": arch_16_natural_gas_methane_properties,
    "17_uranium_atomic_properties_and_symbol": arch_17_uranium_atomic_properties_and_symbol,
    "18_nuclear_fission_energy_release": arch_18_nuclear_fission_energy_release,
    "19_koeberg_nuclear_power_station_context": arch_19_koeberg_nuclear_power_station_context,
    "20_nuclear_power_advantages_emissions": arch_20_nuclear_power_advantages_emissions,
    "21_nuclear_power_disadvantages_radioactive_waste": arch_21_nuclear_power_disadvantages_radioactive_waste,
    "22_natural_greenhouse_effect_mechanism": arch_22_natural_greenhouse_effect_mechanism,
    "23_greenhouse_gases_identification": arch_23_greenhouse_gases_identification,
    "24_enhanced_greenhouse_effect_fossil_combustion": arch_24_enhanced_greenhouse_effect_fossil_combustion,
    "25_global_warming_consequences_south_africa": arch_25_global_warming_consequences_south_africa,
    "26_solar_energy_photovoltaic_conversion": arch_26_solar_energy_photovoltaic_conversion,
    "27_solar_thermal_water_heaters": arch_27_solar_thermal_water_heaters,
    "28_solar_potential_northern_cape": arch_28_solar_potential_northern_cape,
    "29_wind_energy_turbine_mechanism": arch_29_wind_energy_turbine_mechanism,
    "30_wind_energy_geographic_location_coastal": arch_30_wind_energy_geographic_location_coastal,
    "31_wind_energy_advantages_and_disadvantages": arch_31_wind_energy_advantages_and_disadvantages,
    "32_hydropower_gravitational_potential_conversion": arch_32_hydropower_gravitational_potential_conversion,
    "33_gariep_dam_hydroelectric_scheme": arch_33_gariep_dam_hydroelectric_scheme,
    "34_pumped_storage_schemes_drakensberg": arch_34_pumped_storage_schemes_drakensberg,
    "35_hydropower_advantages_and_limitations": arch_35_hydropower_advantages_and_limitations,
    "36_biofuel_definition_and_feedstocks": arch_36_biofuel_definition_and_feedstocks,
    "37_biogas_anaerobic_digester_process": arch_37_biogas_anaerobic_digester_process,
    "38_biogas_case_study_farm_manure_benefits": arch_38_biogas_case_study_farm_manure_benefits,
    "39_bioethanol_vs_petroleum_comparison": arch_39_bioethanol_vs_petroleum_comparison,
    "40_wood_as_energy_source_sustainability": arch_40_wood_as_energy_source_sustainability,
    "41_indoor_air_pollution_wood_coal_braziers": arch_41_indoor_air_pollution_wood_coal_braziers,
    "42_acid_rain_causes_coal_combustion": arch_42_acid_rain_causes_coal_combustion,
    "43_acid_rain_impact_environment_materials": arch_43_acid_rain_impact_environment_materials,
    "44_energy_source_comparison_table_cost_reliability": arch_44_energy_source_comparison_table_cost_reliability,
    "45_baseload_vs_intermittent_power_grid": arch_45_baseload_vs_intermittent_power_grid,
    "46_energy_conservation_in_households": arch_46_energy_conservation_in_households,
    "47_renewable_energy_myths_and_facts": arch_47_renewable_energy_myths_and_facts,
    "48_misconception_clean_infinite_vs_renewable": arch_48_misconception_clean_infinite_vs_renewable,
    "49_misconception_nuclear_vs_fossil_smoke": arch_49_misconception_nuclear_vs_fossil_smoke,
    "50_sources_of_energy_comprehensive_diagnostic": arch_50_sources_of_energy_comprehensive_diagnostic,
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
