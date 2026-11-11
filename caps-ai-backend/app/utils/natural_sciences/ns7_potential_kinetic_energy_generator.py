"""Grade 7 Natural Sciences: Term 3 - Potential and Kinetic Energy Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/02. Potential and kinetic energy.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .ns7_potential_kinetic_energy_archetypes_01_25 import (
    arch_01_definition_of_potential_energy,
    arch_02_gravitational_potential_energy_definition,
    arch_03_factors_affecting_gravitational_potential,
    arch_04_marble_ramp_investigation_variables,
    arch_05_marble_ramp_investigation_relationship,
    arch_06_elastic_potential_energy_compressed_spring,
    arch_07_elastic_potential_energy_stretched_rubber_band,
    arch_08_chemical_potential_energy_in_food,
    arch_09_chemical_potential_energy_in_batteries,
    arch_10_chemical_potential_energy_in_fuels,
    arch_11_definition_of_kinetic_energy,
    arch_12_factors_affecting_kinetic_energy_speed,
    arch_13_factors_affecting_kinetic_energy_mass,
    arch_14_forms_of_kinetic_energy_mechanical_motion,
    arch_15_forms_of_kinetic_energy_thermal_heat,
    arch_16_forms_of_kinetic_energy_sound_vibrations,
    arch_17_forms_of_kinetic_energy_electrical_current,
    arch_18_unit_of_energy_the_joule,
    arch_19_concept_of_a_system_definition,
    arch_20_energy_transfer_in_biological_systems,
    arch_21_falling_object_energy_transformation,
    arch_22_pendulum_highest_point_energy,
    arch_23_pendulum_lowest_point_energy,
    arch_24_roller_coaster_summit_to_dip_conversion,
    arch_25_bouncing_ball_energy_cycle,
)
from .ns7_potential_kinetic_energy_archetypes_26_50 import (
    arch_26_bow_and_arrow_energy_transformation,
    arch_27_catapult_mechanism_elastic_to_kinetic,
    arch_28_trampoline_elastic_potential_rebound,
    arch_29_windup_mechanical_clockwork_toy,
    arch_30_hydroelectric_dam_water_potential_to_kinetic,
    arch_31_falling_meteor_or_skydiver_terminal_velocity,
    arch_32_law_of_conservation_of_energy_statement,
    arch_33_conservation_of_energy_pendulum_system,
    arch_34_energy_dissipation_friction_and_sound,
    arch_35_sankey_diagram_energy_balance_concept,
    arch_36_calculating_proportional_potential_energy_height,
    arch_37_calculating_proportional_potential_energy_mass,
    arch_38_qualitative_kinetic_energy_comparison,
    arch_39_skateboarder_halfpipe_energy_exchange,
    arch_40_swing_playground_energy_transfer,
    arch_41_compressed_air_pneumatic_system,
    arch_42_chemical_to_mechanical_car_engine,
    arch_43_electric_kettle_energy_transformation,
    arch_44_battery_powered_flashlight_circuit,
    arch_45_misconception_energy_gets_used_up_disappears,
    arch_46_misconception_stationary_objects_have_no_energy,
    arch_47_misconception_heavier_objects_fall_with_more_energy,
    arch_48_misconception_potential_only_means_gravity,
    arch_49_energy_transformations_in_daily_appliances,
    arch_50_potential_and_kinetic_energy_comprehensive_diagnostic,
)

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    "01_definition_of_potential_energy": arch_01_definition_of_potential_energy,
    "02_gravitational_potential_energy_definition": arch_02_gravitational_potential_energy_definition,
    "03_factors_affecting_gravitational_potential": arch_03_factors_affecting_gravitational_potential,
    "04_marble_ramp_investigation_variables": arch_04_marble_ramp_investigation_variables,
    "05_marble_ramp_investigation_relationship": arch_05_marble_ramp_investigation_relationship,
    "06_elastic_potential_energy_compressed_spring": arch_06_elastic_potential_energy_compressed_spring,
    "07_elastic_potential_energy_stretched_rubber_band": arch_07_elastic_potential_energy_stretched_rubber_band,
    "08_chemical_potential_energy_in_food": arch_08_chemical_potential_energy_in_food,
    "09_chemical_potential_energy_in_batteries": arch_09_chemical_potential_energy_in_batteries,
    "10_chemical_potential_energy_in_fuels": arch_10_chemical_potential_energy_in_fuels,
    "11_definition_of_kinetic_energy": arch_11_definition_of_kinetic_energy,
    "12_factors_affecting_kinetic_energy_speed": arch_12_factors_affecting_kinetic_energy_speed,
    "13_factors_affecting_kinetic_energy_mass": arch_13_factors_affecting_kinetic_energy_mass,
    "14_forms_of_kinetic_energy_mechanical_motion": arch_14_forms_of_kinetic_energy_mechanical_motion,
    "15_forms_of_kinetic_energy_thermal_heat": arch_15_forms_of_kinetic_energy_thermal_heat,
    "16_forms_of_kinetic_energy_sound_vibrations": arch_16_forms_of_kinetic_energy_sound_vibrations,
    "17_forms_of_kinetic_energy_electrical_current": arch_17_forms_of_kinetic_energy_electrical_current,
    "18_unit_of_energy_the_joule": arch_18_unit_of_energy_the_joule,
    "19_concept_of_a_system_definition": arch_19_concept_of_a_system_definition,
    "20_energy_transfer_in_biological_systems": arch_20_energy_transfer_in_biological_systems,
    "21_falling_object_energy_transformation": arch_21_falling_object_energy_transformation,
    "22_pendulum_highest_point_energy": arch_22_pendulum_highest_point_energy,
    "23_pendulum_lowest_point_energy": arch_23_pendulum_lowest_point_energy,
    "24_roller_coaster_summit_to_dip_conversion": arch_24_roller_coaster_summit_to_dip_conversion,
    "25_bouncing_ball_energy_cycle": arch_25_bouncing_ball_energy_cycle,
    "26_bow_and_arrow_energy_transformation": arch_26_bow_and_arrow_energy_transformation,
    "27_catapult_mechanism_elastic_to_kinetic": arch_27_catapult_mechanism_elastic_to_kinetic,
    "28_trampoline_elastic_potential_rebound": arch_28_trampoline_elastic_potential_rebound,
    "29_windup_mechanical_clockwork_toy": arch_29_windup_mechanical_clockwork_toy,
    "30_hydroelectric_dam_water_potential_to_kinetic": arch_30_hydroelectric_dam_water_potential_to_kinetic,
    "31_falling_meteor_or_skydiver_terminal_velocity": arch_31_falling_meteor_or_skydiver_terminal_velocity,
    "32_law_of_conservation_of_energy_statement": arch_32_law_of_conservation_of_energy_statement,
    "33_conservation_of_energy_pendulum_system": arch_33_conservation_of_energy_pendulum_system,
    "34_energy_dissipation_friction_and_sound": arch_34_energy_dissipation_friction_and_sound,
    "35_sankey_diagram_energy_balance_concept": arch_35_sankey_diagram_energy_balance_concept,
    "36_calculating_proportional_potential_energy_height": arch_36_calculating_proportional_potential_energy_height,
    "37_calculating_proportional_potential_energy_mass": arch_37_calculating_proportional_potential_energy_mass,
    "38_qualitative_kinetic_energy_comparison": arch_38_qualitative_kinetic_energy_comparison,
    "39_skateboarder_halfpipe_energy_exchange": arch_39_skateboarder_halfpipe_energy_exchange,
    "40_swing_playground_energy_transfer": arch_40_swing_playground_energy_transfer,
    "41_compressed_air_pneumatic_system": arch_41_compressed_air_pneumatic_system,
    "42_chemical_to_mechanical_car_engine": arch_42_chemical_to_mechanical_car_engine,
    "43_electric_kettle_energy_transformation": arch_43_electric_kettle_energy_transformation,
    "44_battery_powered_flashlight_circuit": arch_44_battery_powered_flashlight_circuit,
    "45_misconception_energy_gets_used_up_disappears": arch_45_misconception_energy_gets_used_up_disappears,
    "46_misconception_stationary_objects_have_no_energy": arch_46_misconception_stationary_objects_have_no_energy,
    "47_misconception_heavier_objects_fall_with_more_energy": arch_47_misconception_heavier_objects_fall_with_more_energy,
    "48_misconception_potential_only_means_gravity": arch_48_misconception_potential_only_means_gravity,
    "49_energy_transformations_in_daily_appliances": arch_49_energy_transformations_in_daily_appliances,
    "50_potential_and_kinetic_energy_comprehensive_diagnostic": arch_50_potential_and_kinetic_energy_comprehensive_diagnostic,
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
