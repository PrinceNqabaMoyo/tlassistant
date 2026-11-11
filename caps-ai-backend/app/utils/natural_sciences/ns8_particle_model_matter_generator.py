"""Grade 8 Natural Sciences: Term 2 - Particle Model of Matter Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/02. Particle model of matter.md.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .ns8_particle_model_matter_archetypes_01_25 import (
    arch_01_particle_model_four_core_principles,
    arch_02_solids_particle_arrangement_and_vibration,
    arch_03_liquids_particle_arrangement_and_slip,
    arch_04_gases_particle_arrangement_and_rapid_motion,
    arch_05_particle_spacing_and_intermolecular_forces,
    arch_06_compressibility_in_gases_vs_solids_liquids,
    arch_07_shape_and_volume_fixed_vs_variable,
    arch_08_particle_model_diagram_identification,
    arch_09_brownian_motion_experimental_evidence,
    arch_10_diffusion_definition_and_concentration_gradient,
    arch_11_diffusion_in_gases_perfume_and_ammonia,
    arch_12_diffusion_in_liquids_potassium_permanganate,
    arch_13_why_diffusion_does_not_occur_in_solids,
    arch_14_effect_of_temperature_on_diffusion_rate,
    arch_15_diffusion_rate_and_particle_mass_grahams_concept,
    arch_16_everyday_diffusion_phenomena,
    arch_17_investigating_diffusion_variables_fair_test,
    arch_18_melting_and_freezing_microscopic_explanation,
    arch_19_evaporation_vs_boiling_distinction,
    arch_20_condensation_and_cooling_effect,
    arch_21_sublimation_and_deposition_dry_ice_iodine,
    arch_22_heating_curve_temperature_plateaus,
    arch_23_cooling_curve_solidification_plateau,
    arch_24_kinetic_energy_vs_temperature_relationship,
    arch_25_conservation_of_mass_during_phase_change,
)

from .ns8_particle_model_matter_archetypes_26_50 import (
    arch_26_density_definition_and_formula,
    arch_27_density_calculation_cube_or_block,
    arch_28_density_displacement_can_eureka_method,
    arch_29_comparing_densities_of_solids_liquids_gases,
    arch_30_factors_influencing_density_particle_mass_and_spacing,
    arch_31_the_density_anomaly_of_water_and_ice,
    arch_32_floating_and_sinking_density_principles,
    arch_33_density_column_stacking_liquids,
    arch_34_calculating_mass_or_volume_from_density,
    arch_35_thermal_expansion_particle_level_explanation,
    arch_36_thermal_contraction_particle_level_explanation,
    arch_37_ball_and_ring_apparatus_experiment,
    arch_38_bimetallic_strip_in_thermostats,
    arch_39_engineering_solutions_railway_expansion_gaps,
    arch_40_overhead_power_lines_seasonal_sagging,
    arch_41_liquid_expansion_in_thermometers,
    arch_42_gas_pressure_origin_particle_collisions,
    arch_43_gas_pressure_and_number_of_particles,
    arch_44_gas_pressure_and_volume_syringe_compression,
    arch_45_gas_pressure_and_temperature_heating_closed_can,
    arch_46_atmospheric_pressure_and_altitude_trends,
    arch_47_crushing_can_experiment_implosion,
    arch_48_evaluating_gas_pressure_data_table,
    arch_49_misconceptions_particles_expand_vs_spaces_expand,
    arch_50_particle_model_master_synthesis_challenge,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 09: Core Principles & States of Matter
    arch_01_particle_model_four_core_principles,
    arch_02_solids_particle_arrangement_and_vibration,
    arch_03_liquids_particle_arrangement_and_slip,
    arch_04_gases_particle_arrangement_and_rapid_motion,
    arch_05_particle_spacing_and_intermolecular_forces,
    arch_06_compressibility_in_gases_vs_solids_liquids,
    arch_07_shape_and_volume_fixed_vs_variable,
    arch_08_particle_model_diagram_identification,
    arch_09_brownian_motion_experimental_evidence,
    # 10 - 17: Diffusion in Gases and Liquids
    arch_10_diffusion_definition_and_concentration_gradient,
    arch_11_diffusion_in_gases_perfume_and_ammonia,
    arch_12_diffusion_in_liquids_potassium_permanganate,
    arch_13_why_diffusion_does_not_occur_in_solids,
    arch_14_effect_of_temperature_on_diffusion_rate,
    arch_15_diffusion_rate_and_particle_mass_grahams_concept,
    arch_16_everyday_diffusion_phenomena,
    arch_17_investigating_diffusion_variables_fair_test,
    # 18 - 25: Phase Changes & Thermal Curves
    arch_18_melting_and_freezing_microscopic_explanation,
    arch_19_evaporation_vs_boiling_distinction,
    arch_20_condensation_and_cooling_effect,
    arch_21_sublimation_and_deposition_dry_ice_iodine,
    arch_22_heating_curve_temperature_plateaus,
    arch_23_cooling_curve_solidification_plateau,
    arch_24_kinetic_energy_vs_temperature_relationship,
    arch_25_conservation_of_mass_during_phase_change,
    # 26 - 34: Density, Mass, and Volume
    arch_26_density_definition_and_formula,
    arch_27_density_calculation_cube_or_block,
    arch_28_density_displacement_can_eureka_method,
    arch_29_comparing_densities_of_solids_liquids_gases,
    arch_30_factors_influencing_density_particle_mass_and_spacing,
    arch_31_the_density_anomaly_of_water_and_ice,
    arch_32_floating_and_sinking_density_principles,
    arch_33_density_column_stacking_liquids,
    arch_34_calculating_mass_or_volume_from_density,
    # 35 - 41: Thermal Expansion and Contraction
    arch_35_thermal_expansion_particle_level_explanation,
    arch_36_thermal_contraction_particle_level_explanation,
    arch_37_ball_and_ring_apparatus_experiment,
    arch_38_bimetallic_strip_in_thermostats,
    arch_39_engineering_solutions_railway_expansion_gaps,
    arch_40_overhead_power_lines_seasonal_sagging,
    arch_41_liquid_expansion_in_thermometers,
    # 42 - 50: Gas Pressure & Inquiry
    arch_42_gas_pressure_origin_particle_collisions,
    arch_43_gas_pressure_and_number_of_particles,
    arch_44_gas_pressure_and_volume_syringe_compression,
    arch_45_gas_pressure_and_temperature_heating_closed_can,
    arch_46_atmospheric_pressure_and_altitude_trends,
    arch_47_crushing_can_experiment_implosion,
    arch_48_evaluating_gas_pressure_data_table,
    arch_49_misconceptions_particles_expand_vs_spaces_expand,
    arch_50_particle_model_master_synthesis_challenge,
]

SUBSKILLS: List[str] = [
    # 01 - 09
    "01_particle_model_four_core_principles",
    "02_solids_particle_arrangement_and_vibration",
    "03_liquids_particle_arrangement_and_slip",
    "04_gases_particle_arrangement_and_rapid_motion",
    "05_particle_spacing_and_intermolecular_forces",
    "06_compressibility_in_gases_vs_solids_liquids",
    "07_shape_and_volume_fixed_vs_variable",
    "08_particle_model_diagram_identification",
    "09_brownian_motion_experimental_evidence",
    # 10 - 17
    "10_diffusion_definition_and_concentration_gradient",
    "11_diffusion_in_gases_perfume_and_ammonia",
    "12_diffusion_in_liquids_potassium_permanganate",
    "13_why_diffusion_does_not_occur_in_solids",
    "14_effect_of_temperature_on_diffusion_rate",
    "15_diffusion_rate_and_particle_mass_grahams_concept",
    "16_everyday_diffusion_phenomena",
    "17_investigating_diffusion_variables_fair_test",
    # 18 - 25
    "18_melting_and_freezing_microscopic_explanation",
    "19_evaporation_vs_boiling_distinction",
    "20_condensation_and_cooling_effect",
    "21_sublimation_and_deposition_dry_ice_iodine",
    "22_heating_curve_temperature_plateaus",
    "23_cooling_curve_solidification_plateau",
    "24_kinetic_energy_vs_temperature_relationship",
    "25_conservation_of_mass_during_phase_change",
    # 26 - 34
    "26_density_definition_and_formula",
    "27_density_calculation_cube_or_block",
    "28_density_displacement_can_eureka_method",
    "29_comparing_densities_of_solids_liquids_gases",
    "30_factors_influencing_density_particle_mass_and_spacing",
    "31_the_density_anomaly_of_water_and_ice",
    "32_floating_and_sinking_density_principles",
    "33_density_column_stacking_liquids",
    "34_calculating_mass_or_volume_from_density",
    # 35 - 41
    "35_thermal_expansion_particle_level_explanation",
    "36_thermal_contraction_particle_level_explanation",
    "37_ball_and_ring_apparatus_experiment",
    "38_bimetallic_strip_in_thermostats",
    "39_engineering_solutions_railway_expansion_gaps",
    "40_overhead_power_lines_seasonal_sagging",
    "41_liquid_expansion_in_thermometers",
    # 42 - 50
    "42_gas_pressure_origin_particle_collisions",
    "43_gas_pressure_and_number_of_particles",
    "44_gas_pressure_and_volume_syringe_compression",
    "45_gas_pressure_and_temperature_heating_closed_can",
    "46_atmospheric_pressure_and_altitude_trends",
    "47_crushing_can_experiment_implosion",
    "48_evaluating_gas_pressure_data_table",
    "49_misconceptions_particles_expand_vs_spaces_expand",
    "50_particle_model_master_synthesis_challenge",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based integer and padded string aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["states_of_matter_particle_arrangement"] = arch_02_solids_particle_arrangement_and_vibration
DISPATCH_TABLE["diffusion_in_gases_and_liquids"] = arch_11_diffusion_in_gases_perfume_and_ammonia
DISPATCH_TABLE["changes_of_state_heating_cooling"] = arch_18_melting_and_freezing_microscopic_explanation
DISPATCH_TABLE["density_mass_volume_calculations"] = arch_27_density_calculation_cube_or_block
DISPATCH_TABLE["expansion_contraction_and_pressure"] = arch_35_thermal_expansion_particle_level_explanation


def get_subskills() -> List[str]:
    """Returns the list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 8 Natural Sciences: Particle Model of Matter Generator.
    Supports exact archetype dispatch via subskill or archetype_index, and compound mode.
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(count):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None

        if subskill is not None:
            sub_key = str(subskill).strip()
            if sub_key in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[sub_key]
            else:
                sub_lower = sub_key.lower()
                for k, b in DISPATCH_TABLE.items():
                    if isinstance(k, str) and (sub_lower in k.lower() or k.lower() in sub_lower):
                        builder = b
                        break

        if builder is None and archetype_index is not None:
            try:
                idx = int(archetype_index)
                if idx in DISPATCH_TABLE:
                    builder = DISPATCH_TABLE[idx]
                elif 1 <= idx <= len(BUILDERS):
                    builder = BUILDERS[idx - 1]
            except (ValueError, TypeError):
                pass

        if builder is None:
            builder = rng.choice(BUILDERS)

        q = builder(rng)
        q.setdefault("grade", 8)
        q.setdefault("subject", "Natural Sciences")
        q.setdefault("topic", "Particle model of matter")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
