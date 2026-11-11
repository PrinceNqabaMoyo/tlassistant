"""Grade 8 Natural Sciences: Term 3 - Energy Transfer in Electrical Systems Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/01. Energy transfer in electrical systems.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .ns8_energy_transfer_electrical_archetypes_01_25 import (
    arch_01_definition_of_electric_current_and_amperes,
    arch_02_role_of_delocalised_electrons_in_metals,
    arch_03_conventional_current_versus_electron_flow,
    arch_04_requirements_for_a_complete_closed_circuit,
    arch_05_identifying_circuit_symbols_cell_battery_switch,
    arch_06_identifying_circuit_symbols_bulb_resistor_meters,
    arch_07_distinguishing_single_cell_from_multi_cell_battery,
    arch_08_chemical_energy_conversion_inside_cells,
    arch_09_environmental_dangers_of_disposing_batteries,
    arch_10_definition_and_nature_of_electrical_resistance,
    arch_11_four_factors_affecting_wire_resistance_overview,
    arch_12_effect_of_wire_length_on_resistance,
    arch_13_effect_of_wire_thickness_cross_section_on_resistance,
    arch_14_effect_of_wire_material_copper_versus_nichrome,
    arch_15_effect_of_temperature_on_metallic_resistance,
    arch_16_anatomy_and_operation_of_incandescent_bulb,
    arch_17_function_of_argon_gas_inside_light_bulb,
    arch_18_nichrome_heating_element_in_appliances_kettle_toaster,
    arch_19_heating_effect_of_electric_current_joule_heating,
    arch_20_function_and_operation_of_an_electric_fuse,
    arch_21_selecting_correct_fuse_rating_for_appliance,
    arch_22_circuit_breakers_versus_disposable_fuses,
    arch_23_definition_and_dangers_of_a_short_circuit,
    arch_24_three_pin_plug_wiring_colour_codes_south_africa,
    arch_25_function_of_the_earth_wire_for_metal_appliances,
)
from .ns8_energy_transfer_electrical_archetypes_26_50 import (
    arch_26_magnetic_effect_of_an_electric_current_oersted,
    arch_27_shape_of_magnetic_field_around_straight_wire,
    arch_28_right_hand_grip_rule_for_wire_magnetic_field,
    arch_29_magnetic_field_pattern_of_a_solenoid_coil,
    arch_30_structure_and_definition_of_an_electromagnet,
    arch_31_role_of_soft_iron_core_in_electromagnet,
    arch_32_factors_affecting_electromagnet_strength_turns,
    arch_33_factors_affecting_electromagnet_strength_current,
    arch_34_comparing_permanent_magnets_and_electromagnets,
    arch_35_application_of_electromagnet_in_scrap_metal_crane,
    arch_36_operation_of_an_electric_bell_or_buzzer,
    arch_37_operation_of_an_electromagnetic_relay_switch,
    arch_38_chemical_effect_of_electric_current_definition,
    arch_39_electrolysis_of_water_into_hydrogen_and_oxygen,
    arch_40_identifying_gases_produced_at_cathode_and_anode,
    arch_41_concept_and_purpose_of_electroplating,
    arch_42_anode_cathode_and_electrolyte_in_copper_plating,
    arch_43_electroplating_jewellery_gold_and_silver,
    arch_44_industrial_electro_refining_of_blister_copper,
    arch_45_ammeter_series_connection_and_low_internal_resistance,
    arch_46_voltmeter_parallel_connection_and_high_internal_resistance,
    arch_47_misconception_electrons_are_consumed_in_circuit,
    arch_48_misconception_current_slows_down_after_passing_resistor,
    arch_49_misconception_battery_stores_actual_electrons,
    arch_50_energy_transfer_electrical_systems_comprehensive_diagnostic,
)

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    "01_definition_of_electric_current_and_amperes": arch_01_definition_of_electric_current_and_amperes,
    "02_role_of_delocalised_electrons_in_metals": arch_02_role_of_delocalised_electrons_in_metals,
    "03_conventional_current_versus_electron_flow": arch_03_conventional_current_versus_electron_flow,
    "04_requirements_for_a_complete_closed_circuit": arch_04_requirements_for_a_complete_closed_circuit,
    "05_identifying_circuit_symbols_cell_battery_switch": arch_05_identifying_circuit_symbols_cell_battery_switch,
    "06_identifying_circuit_symbols_bulb_resistor_meters": arch_06_identifying_circuit_symbols_bulb_resistor_meters,
    "07_distinguishing_single_cell_from_multi_cell_battery": arch_07_distinguishing_single_cell_from_multi_cell_battery,
    "08_chemical_energy_conversion_inside_cells": arch_08_chemical_energy_conversion_inside_cells,
    "09_environmental_dangers_of_disposing_batteries": arch_09_environmental_dangers_of_disposing_batteries,
    "10_definition_and_nature_of_electrical_resistance": arch_10_definition_and_nature_of_electrical_resistance,
    "11_four_factors_affecting_wire_resistance_overview": arch_11_four_factors_affecting_wire_resistance_overview,
    "12_effect_of_wire_length_on_resistance": arch_12_effect_of_wire_length_on_resistance,
    "13_effect_of_wire_thickness_cross_section_on_resistance": arch_13_effect_of_wire_thickness_cross_section_on_resistance,
    "14_effect_of_wire_material_copper_versus_nichrome": arch_14_effect_of_wire_material_copper_versus_nichrome,
    "15_effect_of_temperature_on_metallic_resistance": arch_15_effect_of_temperature_on_metallic_resistance,
    "16_anatomy_and_operation_of_incandescent_bulb": arch_16_anatomy_and_operation_of_incandescent_bulb,
    "17_function_of_argon_gas_inside_light_bulb": arch_17_function_of_argon_gas_inside_light_bulb,
    "18_nichrome_heating_element_in_appliances_kettle_toaster": arch_18_nichrome_heating_element_in_appliances_kettle_toaster,
    "19_heating_effect_of_electric_current_joule_heating": arch_19_heating_effect_of_electric_current_joule_heating,
    "20_function_and_operation_of_an_electric_fuse": arch_20_function_and_operation_of_an_electric_fuse,
    "21_selecting_correct_fuse_rating_for_appliance": arch_21_selecting_correct_fuse_rating_for_appliance,
    "22_circuit_breakers_versus_disposable_fuses": arch_22_circuit_breakers_versus_disposable_fuses,
    "23_definition_and_dangers_of_a_short_circuit": arch_23_definition_and_dangers_of_a_short_circuit,
    "24_three_pin_plug_wiring_colour_codes_south_africa": arch_24_three_pin_plug_wiring_colour_codes_south_africa,
    "25_function_of_the_earth_wire_for_metal_appliances": arch_25_function_of_the_earth_wire_for_metal_appliances,
    "26_magnetic_effect_of_an_electric_current_oersted": arch_26_magnetic_effect_of_an_electric_current_oersted,
    "27_shape_of_magnetic_field_around_straight_wire": arch_27_shape_of_magnetic_field_around_straight_wire,
    "28_right_hand_grip_rule_for_wire_magnetic_field": arch_28_right_hand_grip_rule_for_wire_magnetic_field,
    "29_magnetic_field_pattern_of_a_solenoid_coil": arch_29_magnetic_field_pattern_of_a_solenoid_coil,
    "30_structure_and_definition_of_an_electromagnet": arch_30_structure_and_definition_of_an_electromagnet,
    "31_role_of_soft_iron_core_in_electromagnet": arch_31_role_of_soft_iron_core_in_electromagnet,
    "32_factors_affecting_electromagnet_strength_turns": arch_32_factors_affecting_electromagnet_strength_turns,
    "33_factors_affecting_electromagnet_strength_current": arch_33_factors_affecting_electromagnet_strength_current,
    "34_comparing_permanent_magnets_and_electromagnets": arch_34_comparing_permanent_magnets_and_electromagnets,
    "35_application_of_electromagnet_in_scrap_metal_crane": arch_35_application_of_electromagnet_in_scrap_metal_crane,
    "36_operation_of_an_electric_bell_or_buzzer": arch_36_operation_of_an_electric_bell_or_buzzer,
    "37_operation_of_an_electromagnetic_relay_switch": arch_37_operation_of_an_electromagnetic_relay_switch,
    "38_chemical_effect_of_electric_current_definition": arch_38_chemical_effect_of_electric_current_definition,
    "39_electrolysis_of_water_into_hydrogen_and_oxygen": arch_39_electrolysis_of_water_into_hydrogen_and_oxygen,
    "40_identifying_gases_produced_at_cathode_and_anode": arch_40_identifying_gases_produced_at_cathode_and_anode,
    "41_concept_and_purpose_of_electroplating": arch_41_concept_and_purpose_of_electroplating,
    "42_anode_cathode_and_electrolyte_in_copper_plating": arch_42_anode_cathode_and_electrolyte_in_copper_plating,
    "43_electroplating_jewellery_gold_and_silver": arch_43_electroplating_jewellery_gold_and_silver,
    "44_industrial_electro_refining_of_blister_copper": arch_44_industrial_electro_refining_of_blister_copper,
    "45_ammeter_series_connection_and_low_internal_resistance": arch_45_ammeter_series_connection_and_low_internal_resistance,
    "46_voltmeter_parallel_connection_and_high_internal_resistance": arch_46_voltmeter_parallel_connection_and_high_internal_resistance,
    "47_misconception_electrons_are_consumed_in_circuit": arch_47_misconception_electrons_are_consumed_in_circuit,
    "48_misconception_current_slows_down_after_passing_resistor": arch_48_misconception_current_slows_down_after_passing_resistor,
    "49_misconception_battery_stores_actual_electrons": arch_49_misconception_battery_stores_actual_electrons,
    "50_energy_transfer_electrical_systems_comprehensive_diagnostic": arch_50_energy_transfer_electrical_systems_comprehensive_diagnostic,
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
