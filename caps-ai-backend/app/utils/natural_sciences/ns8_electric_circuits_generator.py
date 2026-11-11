"""Grade 8 Natural Sciences: Term 3 - Series and Parallel Circuits Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/03. Series and parallel circuits.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .ns8_electric_circuits_archetypes_01_25 import (
    arch_01_definition_and_structure_of_series_circuit,
    arch_02_current_constancy_at_all_points_in_series_circuit,
    arch_03_effect_of_adding_resistors_in_series_on_total_resistance,
    arch_04_effect_of_adding_bulbs_in_series_on_brightness_and_current,
    arch_05_ammeter_connection_in_series_and_low_internal_resistance,
    arch_06_effect_of_adding_cells_in_series_on_current_and_voltage,
    arch_07_broken_component_or_open_switch_consequence_in_series,
    arch_08_delocalised_electrons_instantaneous_conduction_in_circuit,
    arch_09_definition_and_branch_structure_of_parallel_circuit,
    arch_10_current_division_across_branches_in_parallel_circuit,
    arch_11_sum_of_branch_currents_equals_total_main_current,
    arch_12_effect_of_adding_resistors_in_parallel_on_total_resistance,
    arch_13_doorway_school_hall_analogy_for_parallel_resistance_decrease,
    arch_14_brightness_of_identical_bulbs_in_parallel_branches,
    arch_15_independent_operation_of_parallel_branches_when_one_fails,
    arch_16_effect_of_adding_cells_in_parallel_on_voltage_and_current,
    arch_17_longevity_and_capacity_of_cells_connected_in_parallel,
    arch_18_switch_placement_in_main_circuit_versus_parallel_branch,
    arch_19_domestic_household_wiring_rationale_for_parallel_circuits,
    arch_20_comparing_battery_drain_rate_in_series_versus_parallel,
    arch_21_ranking_bulb_brightness_in_series_versus_parallel_configurations,
    arch_22_calculating_branch_currents_from_total_and_other_branches,
    arch_23_calculating_total_current_from_identical_parallel_branches,
    arch_24_relative_resistance_of_copper_aluminium_zinc_nichrome_wires,
    arch_25_investigating_qualitative_resistance_using_bulb_brightness,
)
from .ns8_electric_circuits_archetypes_26_50 import (
    arch_26_why_copper_is_used_for_electrical_connecting_wires,
    arch_27_why_nichrome_is_used_in_electric_heaters_and_toasters,
    arch_28_definition_and_examples_of_circuit_output_devices,
    arch_29_structure_and_operating_principle_of_led_diodes,
    arch_30_comparing_led_efficiency_versus_filament_incandescent_bulbs,
    arch_31_interpreting_sankey_diagram_for_incandescent_filament_bulb,
    arch_32_interpreting_sankey_diagram_for_high_efficiency_led_bulb,
    arch_33_calculating_electrical_device_percentage_efficiency_from_sankey,
    arch_34_calculating_wasted_heat_energy_from_input_and_useful_light,
    arch_35_history_electricity_amber_triboelectric_to_william_gilbert,
    arch_36_history_electricity_benjamin_franklin_lightning_kite_discovery,
    arch_37_history_electricity_volta_first_chemical_cell_and_galvani,
    arch_38_history_electricity_andre_marie_ampere_electrodynamics,
    arch_39_history_electricity_georg_ohm_relationship_voltage_current,
    arch_40_history_electricity_michael_faraday_electromagnetic_induction,
    arch_41_history_electricity_edison_dc_versus_tesla_ac_generators,
    arch_42_short_circuits_mechanism_and_extreme_current_overheating_danger,
    arch_43_fuses_and_circuit_breakers_overcurrent_protection_mechanism,
    arch_44_misconception_electric_current_gets_used_up_by_bulbs,
    arch_45_misconception_current_is_greater_before_a_bulb_than_after,
    arch_46_misconception_adding_resistors_in_parallel_increases_resistance,
    arch_47_misconception_connecting_cells_in_parallel_multiplies_voltage,
    arch_48_misconception_electrons_originate_only_from_the_battery_chemical,
    arch_49_experimental_design_variables_in_series_parallel_investigations,
    arch_50_electric_circuits_comprehensive_diagnostic_evaluation,
)

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    "01_definition_and_structure_of_series_circuit": arch_01_definition_and_structure_of_series_circuit,
    "02_current_constancy_at_all_points_in_series_circuit": arch_02_current_constancy_at_all_points_in_series_circuit,
    "03_effect_of_adding_resistors_in_series_on_total_resistance": arch_03_effect_of_adding_resistors_in_series_on_total_resistance,
    "04_effect_of_adding_bulbs_in_series_on_brightness_and_current": arch_04_effect_of_adding_bulbs_in_series_on_brightness_and_current,
    "05_ammeter_connection_in_series_and_low_internal_resistance": arch_05_ammeter_connection_in_series_and_low_internal_resistance,
    "06_effect_of_adding_cells_in_series_on_current_and_voltage": arch_06_effect_of_adding_cells_in_series_on_current_and_voltage,
    "07_broken_component_or_open_switch_consequence_in_series": arch_07_broken_component_or_open_switch_consequence_in_series,
    "08_delocalised_electrons_instantaneous_conduction_in_circuit": arch_08_delocalised_electrons_instantaneous_conduction_in_circuit,
    "09_definition_and_branch_structure_of_parallel_circuit": arch_09_definition_and_branch_structure_of_parallel_circuit,
    "10_current_division_across_branches_in_parallel_circuit": arch_10_current_division_across_branches_in_parallel_circuit,
    "11_sum_of_branch_currents_equals_total_main_current": arch_11_sum_of_branch_currents_equals_total_main_current,
    "12_effect_of_adding_resistors_in_parallel_on_total_resistance": arch_12_effect_of_adding_resistors_in_parallel_on_total_resistance,
    "13_doorway_school_hall_analogy_for_parallel_resistance_decrease": arch_13_doorway_school_hall_analogy_for_parallel_resistance_decrease,
    "14_brightness_of_identical_bulbs_in_parallel_branches": arch_14_brightness_of_identical_bulbs_in_parallel_branches,
    "15_independent_operation_of_parallel_branches_when_one_fails": arch_15_independent_operation_of_parallel_branches_when_one_fails,
    "16_effect_of_adding_cells_in_parallel_on_voltage_and_current": arch_16_effect_of_adding_cells_in_parallel_on_voltage_and_current,
    "17_longevity_and_capacity_of_cells_connected_in_parallel": arch_17_longevity_and_capacity_of_cells_connected_in_parallel,
    "18_switch_placement_in_main_circuit_versus_parallel_branch": arch_18_switch_placement_in_main_circuit_versus_parallel_branch,
    "19_domestic_household_wiring_rationale_for_parallel_circuits": arch_19_domestic_household_wiring_rationale_for_parallel_circuits,
    "20_comparing_battery_drain_rate_in_series_versus_parallel": arch_20_comparing_battery_drain_rate_in_series_versus_parallel,
    "21_ranking_bulb_brightness_in_series_versus_parallel_configurations": arch_21_ranking_bulb_brightness_in_series_versus_parallel_configurations,
    "22_calculating_branch_currents_from_total_and_other_branches": arch_22_calculating_branch_currents_from_total_and_other_branches,
    "23_calculating_total_current_from_identical_parallel_branches": arch_23_calculating_total_current_from_identical_parallel_branches,
    "24_relative_resistance_of_copper_aluminium_zinc_nichrome_wires": arch_24_relative_resistance_of_copper_aluminium_zinc_nichrome_wires,
    "25_investigating_qualitative_resistance_using_bulb_brightness": arch_25_investigating_qualitative_resistance_using_bulb_brightness,
    "26_why_copper_is_used_for_electrical_connecting_wires": arch_26_why_copper_is_used_for_electrical_connecting_wires,
    "27_why_nichrome_is_used_in_electric_heaters_and_toasters": arch_27_why_nichrome_is_used_in_electric_heaters_and_toasters,
    "28_definition_and_examples_of_circuit_output_devices": arch_28_definition_and_examples_of_circuit_output_devices,
    "29_structure_and_operating_principle_of_led_diodes": arch_29_structure_and_operating_principle_of_led_diodes,
    "30_comparing_led_efficiency_versus_filament_incandescent_bulbs": arch_30_comparing_led_efficiency_versus_filament_incandescent_bulbs,
    "31_interpreting_sankey_diagram_for_incandescent_filament_bulb": arch_31_interpreting_sankey_diagram_for_incandescent_filament_bulb,
    "32_interpreting_sankey_diagram_for_high_efficiency_led_bulb": arch_32_interpreting_sankey_diagram_for_high_efficiency_led_bulb,
    "33_calculating_electrical_device_percentage_efficiency_from_sankey": arch_33_calculating_electrical_device_percentage_efficiency_from_sankey,
    "34_calculating_wasted_heat_energy_from_input_and_useful_light": arch_34_calculating_wasted_heat_energy_from_input_and_useful_light,
    "35_history_electricity_amber_triboelectric_to_william_gilbert": arch_35_history_electricity_amber_triboelectric_to_william_gilbert,
    "36_history_electricity_benjamin_franklin_lightning_kite_discovery": arch_36_history_electricity_benjamin_franklin_lightning_kite_discovery,
    "37_history_electricity_volta_first_chemical_cell_and_galvani": arch_37_history_electricity_volta_first_chemical_cell_and_galvani,
    "38_history_electricity_andre_marie_ampere_electrodynamics": arch_38_history_electricity_andre_marie_ampere_electrodynamics,
    "39_history_electricity_georg_ohm_relationship_voltage_current": arch_39_history_electricity_georg_ohm_relationship_voltage_current,
    "40_history_electricity_michael_faraday_electromagnetic_induction": arch_40_history_electricity_michael_faraday_electromagnetic_induction,
    "41_history_electricity_edison_dc_versus_tesla_ac_generators": arch_41_history_electricity_edison_dc_versus_tesla_ac_generators,
    "42_short_circuits_mechanism_and_extreme_current_overheating_danger": arch_42_short_circuits_mechanism_and_extreme_current_overheating_danger,
    "43_fuses_and_circuit_breakers_overcurrent_protection_mechanism": arch_43_fuses_and_circuit_breakers_overcurrent_protection_mechanism,
    "44_misconception_electric_current_gets_used_up_by_bulbs": arch_44_misconception_electric_current_gets_used_up_by_bulbs,
    "45_misconception_current_is_greater_before_a_bulb_than_after": arch_45_misconception_current_is_greater_before_a_bulb_than_after,
    "46_misconception_adding_resistors_in_parallel_increases_resistance": arch_46_misconception_adding_resistors_in_parallel_increases_resistance,
    "47_misconception_connecting_cells_in_parallel_multiplies_voltage": arch_47_misconception_connecting_cells_in_parallel_multiplies_voltage,
    "48_misconception_electrons_originate_only_from_the_battery_chemical": arch_48_misconception_electrons_originate_only_from_the_battery_chemical,
    "49_experimental_design_variables_in_series_parallel_investigations": arch_49_experimental_design_variables_in_series_parallel_investigations,
    "50_electric_circuits_comprehensive_diagnostic_evaluation": arch_50_electric_circuits_comprehensive_diagnostic_evaluation,
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


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
