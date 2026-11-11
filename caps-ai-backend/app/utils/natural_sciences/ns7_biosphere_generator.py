"""Grade 7 Natural Sciences: Term 1 - The Biosphere Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/01. The Biosphere.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_biosphere_archetypes_01_25 import (
    arch_01_biosphere_definition_and_scope,
    arch_02_atmosphere_composition_and_function,
    arch_03_hydrosphere_distribution_and_water_cycle,
    arch_04_lithosphere_soil_and_mineral_foundation,
    arch_05_interlocking_spheres_ecological_interaction,
    arch_06_distinguish_living_nonliving_dead_matter,
    arch_07_life_process_movement_plants_vs_animals,
    arch_08_life_process_cellular_respiration_vs_breathing,
    arch_09_life_process_sensitivity_and_stimulus_response,
    arch_10_life_process_growth_and_development,
    arch_11_life_process_reproduction_species_survival,
    arch_12_life_process_excretion_vs_egestion,
    arch_13_life_process_nutrition_autotrophs_vs_heterotrophs,
    arch_14_identify_missing_life_process_scenario,
    arch_15_requirement_energy_solar_to_chemical,
    arch_16_requirement_gases_oxygen_carbon_dioxide_roles,
    arch_17_requirement_water_biological_functions,
    arch_18_requirement_soil_nutrients_nitrogen_phosphorus_potassium,
    arch_19_requirement_temperature_range_and_enzyme_limits,
    arch_20_scientific_investigation_aim_and_hypothesis,
    arch_21_scientific_investigation_identifying_variables,
    arch_22_scientific_investigation_control_group_necessity,
    arch_23_scientific_investigation_seed_germination_data,
    arch_24_scientific_investigation_light_vs_dark_plant_growth,
    arch_25_scientific_investigation_evaluating_fair_test,
)
from .ns7_biosphere_archetypes_26_50 import (
    arch_26_structural_adaptation_desert_animals_camel,
    arch_27_structural_adaptation_aquatic_animals_fish,
    arch_28_structural_adaptation_predatory_birds_raptors,
    arch_29_structural_adaptation_arid_plants_succulents,
    arch_30_structural_adaptation_aquatic_plants_water_lily,
    arch_31_behavioural_adaptation_nocturnal_desert_survival,
    arch_32_behavioural_adaptation_migration_and_hibernation,
    arch_33_functional_adaptation_water_conservation_excretion,
    arch_34_south_african_adaptation_fynbos_protea_fire,
    arch_35_south_african_adaptation_karoo_aloe_drought,
    arch_36_south_african_adaptation_savanna_baobab_water_storage,
    arch_37_south_african_adaptation_acacia_thorns_and_taproots,
    arch_38_south_african_adaptation_springbok_arid_physiology,
    arch_39_compare_polar_vs_desert_mammal_adaptations,
    arch_40_biosphere_altitude_and_depth_limits_of_life,
    arch_41_abiotic_factors_shaping_habitats_temperature_moisture,
    arch_42_closed_ecological_system_biosphere_2_lessons,
    arch_43_decomposers_recycling_dead_matter_to_lithosphere,
    arch_44_photosynthesis_and_respiration_gas_exchange_cycle,
    arch_45_soil_erosion_impact_on_biosphere_sustainability,
    arch_46_water_pollution_impact_on_hydrosphere_organisms,
    arch_47_air_quality_impact_on_atmosphere_and_living_things,
    arch_48_microorganisms_role_as_living_agents_in_biosphere,
    arch_49_classify_organism_requirements_matrix,
    arch_50_synthetic_case_study_ecosystem_disruption_analysis,
)

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_biosphere_definition_and_scope": arch_01_biosphere_definition_and_scope,
    "02_atmosphere_composition_and_function": arch_02_atmosphere_composition_and_function,
    "03_hydrosphere_distribution_and_water_cycle": arch_03_hydrosphere_distribution_and_water_cycle,
    "04_lithosphere_soil_and_mineral_foundation": arch_04_lithosphere_soil_and_mineral_foundation,
    "05_interlocking_spheres_ecological_interaction": arch_05_interlocking_spheres_ecological_interaction,
    "06_distinguish_living_nonliving_dead_matter": arch_06_distinguish_living_nonliving_dead_matter,
    "07_life_process_movement_plants_vs_animals": arch_07_life_process_movement_plants_vs_animals,
    "08_life_process_cellular_respiration_vs_breathing": arch_08_life_process_cellular_respiration_vs_breathing,
    "09_life_process_sensitivity_and_stimulus_response": arch_09_life_process_sensitivity_and_stimulus_response,
    "10_life_process_growth_and_development": arch_10_life_process_growth_and_development,
    "11_life_process_reproduction_species_survival": arch_11_life_process_reproduction_species_survival,
    "12_life_process_excretion_vs_egestion": arch_12_life_process_excretion_vs_egestion,
    "13_life_process_nutrition_autotrophs_vs_heterotrophs": arch_13_life_process_nutrition_autotrophs_vs_heterotrophs,
    "14_identify_missing_life_process_scenario": arch_14_identify_missing_life_process_scenario,
    "15_requirement_energy_solar_to_chemical": arch_15_requirement_energy_solar_to_chemical,
    "16_requirement_gases_oxygen_carbon_dioxide_roles": arch_16_requirement_gases_oxygen_carbon_dioxide_roles,
    "17_requirement_water_biological_functions": arch_17_requirement_water_biological_functions,
    "18_requirement_soil_nutrients_nitrogen_phosphorus_potassium": arch_18_requirement_soil_nutrients_nitrogen_phosphorus_potassium,
    "19_requirement_temperature_range_and_enzyme_limits": arch_19_requirement_temperature_range_and_enzyme_limits,
    "20_scientific_investigation_aim_and_hypothesis": arch_20_scientific_investigation_aim_and_hypothesis,
    "21_scientific_investigation_identifying_variables": arch_21_scientific_investigation_identifying_variables,
    "22_scientific_investigation_control_group_necessity": arch_22_scientific_investigation_control_group_necessity,
    "23_scientific_investigation_seed_germination_data": arch_23_scientific_investigation_seed_germination_data,
    "24_scientific_investigation_light_vs_dark_plant_growth": arch_24_scientific_investigation_light_vs_dark_plant_growth,
    "25_scientific_investigation_evaluating_fair_test": arch_25_scientific_investigation_evaluating_fair_test,
    "26_structural_adaptation_desert_animals_camel": arch_26_structural_adaptation_desert_animals_camel,
    "27_structural_adaptation_aquatic_animals_fish": arch_27_structural_adaptation_aquatic_animals_fish,
    "28_structural_adaptation_predatory_birds_raptors": arch_28_structural_adaptation_predatory_birds_raptors,
    "29_structural_adaptation_arid_plants_succulents": arch_29_structural_adaptation_arid_plants_succulents,
    "30_structural_adaptation_aquatic_plants_water_lily": arch_30_structural_adaptation_aquatic_plants_water_lily,
    "31_behavioural_adaptation_nocturnal_desert_survival": arch_31_behavioural_adaptation_nocturnal_desert_survival,
    "32_behavioural_adaptation_migration_and_hibernation": arch_32_behavioural_adaptation_migration_and_hibernation,
    "33_functional_adaptation_water_conservation_excretion": arch_33_functional_adaptation_water_conservation_excretion,
    "34_south_african_adaptation_fynbos_protea_fire": arch_34_south_african_adaptation_fynbos_protea_fire,
    "35_south_african_adaptation_karoo_aloe_drought": arch_35_south_african_adaptation_karoo_aloe_drought,
    "36_south_african_adaptation_savanna_baobab_water_storage": arch_36_south_african_adaptation_savanna_baobab_water_storage,
    "37_south_african_adaptation_acacia_thorns_and_taproots": arch_37_south_african_adaptation_acacia_thorns_and_taproots,
    "38_south_african_adaptation_springbok_arid_physiology": arch_38_south_african_adaptation_springbok_arid_physiology,
    "39_compare_polar_vs_desert_mammal_adaptations": arch_39_compare_polar_vs_desert_mammal_adaptations,
    "40_biosphere_altitude_and_depth_limits_of_life": arch_40_biosphere_altitude_and_depth_limits_of_life,
    "41_abiotic_factors_shaping_habitats_temperature_moisture": arch_41_abiotic_factors_shaping_habitats_temperature_moisture,
    "42_closed_ecological_system_biosphere_2_lessons": arch_42_closed_ecological_system_biosphere_2_lessons,
    "43_decomposers_recycling_dead_matter_to_lithosphere": arch_43_decomposers_recycling_dead_matter_to_lithosphere,
    "44_photosynthesis_and_respiration_gas_exchange_cycle": arch_44_photosynthesis_and_respiration_gas_exchange_cycle,
    "45_soil_erosion_impact_on_biosphere_sustainability": arch_45_soil_erosion_impact_on_biosphere_sustainability,
    "46_water_pollution_impact_on_hydrosphere_organisms": arch_46_water_pollution_impact_on_hydrosphere_organisms,
    "47_air_quality_impact_on_atmosphere_and_living_things": arch_47_air_quality_impact_on_atmosphere_and_living_things,
    "48_microorganisms_role_as_living_agents_in_biosphere": arch_48_microorganisms_role_as_living_agents_in_biosphere,
    "49_classify_organism_requirements_matrix": arch_49_classify_organism_requirements_matrix,
    "50_synthetic_case_study_ecosystem_disruption_analysis": arch_50_synthetic_case_study_ecosystem_disruption_analysis,
}

SUBSKILLS: List[str] = list(BUILDERS.keys())

LEGACY_MAP: Dict[str, str] = {
    "biosphere_definition_and_zones": "01_biosphere_definition_and_scope",
    "interlocking_spheres_atmosphere_hydrosphere_lithosphere": "05_interlocking_spheres_ecological_interaction",
    "seven_life_processes_mrs_gren": "14_identify_missing_life_process_scenario",
    "requirements_for_sustaining_life": "15_requirement_energy_solar_to_chemical",
    "habitats_and_environmental_adaptations": "26_structural_adaptation_desert_animals_camel",
}


def _resolve_subskill(subskill: Optional[str]) -> str:
    if not subskill:
        return random.choice(SUBSKILLS)
    s = subskill.strip().lower()
    if s in BUILDERS:
        return s
    if s in LEGACY_MAP:
        return LEGACY_MAP[s]
    # Check prefix or partial match
    for k in SUBSKILLS:
        if k.startswith(s) or s in k:
            return k
    return SUBSKILLS[0]


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate deterministic questions for Grade 7 Natural Sciences: The Biosphere."""
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        # Vary seed deterministically across count
        sub_seed = rng.randint(1000, 999999) if count > 1 else seed
        sub_rng = random.Random(sub_seed) if sub_seed is not None else rng
        if subskill:
            chosen = _resolve_subskill(subskill)
        else:
            chosen = SUBSKILLS[i % len(SUBSKILLS)]
        builder = BUILDERS[chosen]
        q = builder(sub_rng)
        questions.append(q)

    return questions
