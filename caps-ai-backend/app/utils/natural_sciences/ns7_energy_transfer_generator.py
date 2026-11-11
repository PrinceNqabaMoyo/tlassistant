"""Grade 7 Natural Sciences: Term 3 - Energy Transfer to Surroundings Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/03. Energy transfer to surroundings.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .ns7_energy_transfer_archetypes_01_25 import (
    arch_01_concept_of_useful_vs_wasted_energy,
    arch_02_scientific_meaning_of_wasted_energy,
    arch_03_origin_and_definition_of_sankey_diagram,
    arch_04_sankey_diagram_arrow_width_significance,
    arch_05_sankey_diagram_conservation_law_principle,
    arch_06_incandescent_light_bulb_energy_flow,
    arch_07_fluorescent_cfl_light_bulb_comparison,
    arch_08_modern_led_lighting_efficiency,
    arch_09_electric_drill_useful_and_wasted_outputs,
    arch_10_electric_kettle_energy_flow_analysis,
    arch_11_electric_iron_energy_transfers,
    arch_12_electric_fan_energy_analysis,
    arch_13_car_petrol_engine_energy_balance,
    arch_14_television_screen_energy_transfers,
    arch_15_hairdryer_dual_useful_outputs,
    arch_16_bicycle_mechanical_energy_transfer,
    arch_17_burning_candle_useful_vs_wasted,
    arch_18_electric_toaster_energy_flow,
    arch_19_refrigerator_cooling_energy_displacement,
    arch_20_audio_speaker_energy_transfers,
    arch_21_calculating_efficiency_percentage_basic,
    arch_22_calculating_wasted_energy_from_input_useful,
    arch_23_calculating_input_energy_from_outputs,
    arch_24_interpreting_sankey_proportions_visually,
    arch_25_distinguishing_efficient_from_inefficient_systems,
)
from .ns7_energy_transfer_archetypes_26_50 import (
    arch_26_mechanical_friction_as_cause_of_wasted_heat,
    arch_27_lubrication_to_reduce_wasted_thermal_energy,
    arch_28_sound_energy_as_wasted_mechanical_vibration,
    arch_29_electrical_resistance_heating_in_conductors,
    arch_30_improving_car_aerodynamics_to_reduce_waste,
    arch_31_household_energy_audit_appliance_waste,
    arch_32_standby_power_vampire_energy_waste,
    arch_33_economic_consequences_of_wasted_energy,
    arch_34_environmental_cost_of_power_plant_waste,
    arch_35_sankey_diagram_for_electric_motor,
    arch_36_sankey_diagram_for_coal_power_station,
    arch_37_thermal_insulation_to_trap_useful_heat,
    arch_38_comparison_of_cooling_technologies,
    arch_39_blender_chopping_food_energy_flow,
    arch_40_vacuum_cleaner_energy_transfers,
    arch_41_smartphone_battery_drain_and_heating,
    arch_42_washing_machine_spin_cycle_balance,
    arch_43_energy_star_rating_labels_interpretation,
    arch_44_misconception_wasted_energy_is_destroyed,
    arch_45_misconception_sound_is_useful_in_appliances,
    arch_46_misconception_100_percent_efficient_machine,
    arch_47_misconception_heat_is_always_wasted,
    arch_48_calculating_efficiency_from_fuel_joules,
    arch_49_designing_a_more_efficient_system_challenge,
    arch_50_energy_transfer_surroundings_comprehensive_diagnostic,
)

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    "01_concept_of_useful_vs_wasted_energy": arch_01_concept_of_useful_vs_wasted_energy,
    "02_scientific_meaning_of_wasted_energy": arch_02_scientific_meaning_of_wasted_energy,
    "03_origin_and_definition_of_sankey_diagram": arch_03_origin_and_definition_of_sankey_diagram,
    "04_sankey_diagram_arrow_width_significance": arch_04_sankey_diagram_arrow_width_significance,
    "05_sankey_diagram_conservation_law_principle": arch_05_sankey_diagram_conservation_law_principle,
    "06_incandescent_light_bulb_energy_flow": arch_06_incandescent_light_bulb_energy_flow,
    "07_fluorescent_cfl_light_bulb_comparison": arch_07_fluorescent_cfl_light_bulb_comparison,
    "08_modern_led_lighting_efficiency": arch_08_modern_led_lighting_efficiency,
    "09_electric_drill_useful_and_wasted_outputs": arch_09_electric_drill_useful_and_wasted_outputs,
    "10_electric_kettle_energy_flow_analysis": arch_10_electric_kettle_energy_flow_analysis,
    "11_electric_iron_energy_transfers": arch_11_electric_iron_energy_transfers,
    "12_electric_fan_energy_analysis": arch_12_electric_fan_energy_analysis,
    "13_car_petrol_engine_energy_balance": arch_13_car_petrol_engine_energy_balance,
    "14_television_screen_energy_transfers": arch_14_television_screen_energy_transfers,
    "15_hairdryer_dual_useful_outputs": arch_15_hairdryer_dual_useful_outputs,
    "16_bicycle_mechanical_energy_transfer": arch_16_bicycle_mechanical_energy_transfer,
    "17_burning_candle_useful_vs_wasted": arch_17_burning_candle_useful_vs_wasted,
    "18_electric_toaster_energy_flow": arch_18_electric_toaster_energy_flow,
    "19_refrigerator_cooling_energy_displacement": arch_19_refrigerator_cooling_energy_displacement,
    "20_audio_speaker_energy_transfers": arch_20_audio_speaker_energy_transfers,
    "21_calculating_efficiency_percentage_basic": arch_21_calculating_efficiency_percentage_basic,
    "22_calculating_wasted_energy_from_input_useful": arch_22_calculating_wasted_energy_from_input_useful,
    "23_calculating_input_energy_from_outputs": arch_23_calculating_input_energy_from_outputs,
    "24_interpreting_sankey_proportions_visually": arch_24_interpreting_sankey_proportions_visually,
    "25_distinguishing_efficient_from_inefficient_systems": arch_25_distinguishing_efficient_from_inefficient_systems,
    "26_mechanical_friction_as_cause_of_wasted_heat": arch_26_mechanical_friction_as_cause_of_wasted_heat,
    "27_lubrication_to_reduce_wasted_thermal_energy": arch_27_lubrication_to_reduce_wasted_thermal_energy,
    "28_sound_energy_as_wasted_mechanical_vibration": arch_28_sound_energy_as_wasted_mechanical_vibration,
    "29_electrical_resistance_heating_in_conductors": arch_29_electrical_resistance_heating_in_conductors,
    "30_improving_car_aerodynamics_to_reduce_waste": arch_30_improving_car_aerodynamics_to_reduce_waste,
    "31_household_energy_audit_appliance_waste": arch_31_household_energy_audit_appliance_waste,
    "32_standby_power_vampire_energy_waste": arch_32_standby_power_vampire_energy_waste,
    "33_economic_consequences_of_wasted_energy": arch_33_economic_consequences_of_wasted_energy,
    "34_environmental_cost_of_power_plant_waste": arch_34_environmental_cost_of_power_plant_waste,
    "35_sankey_diagram_for_electric_motor": arch_35_sankey_diagram_for_electric_motor,
    "36_sankey_diagram_for_coal_power_station": arch_36_sankey_diagram_for_coal_power_station,
    "37_thermal_insulation_to_trap_useful_heat": arch_37_thermal_insulation_to_trap_useful_heat,
    "38_comparison_of_cooling_technologies": arch_38_comparison_of_cooling_technologies,
    "39_blender_chopping_food_energy_flow": arch_39_blender_chopping_food_energy_flow,
    "40_vacuum_cleaner_energy_transfers": arch_40_vacuum_cleaner_energy_transfers,
    "41_smartphone_battery_drain_and_heating": arch_41_smartphone_battery_drain_and_heating,
    "42_washing_machine_spin_cycle_balance": arch_42_washing_machine_spin_cycle_balance,
    "43_energy_star_rating_labels_interpretation": arch_43_energy_star_rating_labels_interpretation,
    "44_misconception_wasted_energy_is_destroyed": arch_44_misconception_wasted_energy_is_destroyed,
    "45_misconception_sound_is_useful_in_appliances": arch_45_misconception_sound_is_useful_in_appliances,
    "46_misconception_100_percent_efficient_machine": arch_46_misconception_100_percent_efficient_machine,
    "47_misconception_heat_is_always_wasted": arch_47_misconception_heat_is_always_wasted,
    "48_calculating_efficiency_from_fuel_joules": arch_48_calculating_efficiency_from_fuel_joules,
    "49_designing_a_more_efficient_system_challenge": arch_49_designing_a_more_efficient_system_challenge,
    "50_energy_transfer_surroundings_comprehensive_diagnostic": arch_50_energy_transfer_surroundings_comprehensive_diagnostic,
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
