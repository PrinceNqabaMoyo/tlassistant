"""Grade 8 Natural Sciences: Term 3 - Static Electricity Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/01. Static electricity.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .ns8_static_electricity_archetypes_01_25 import (
    arch_01_atomic_structure_and_electrical_charges,
    arch_02_concept_of_neutral_uncharged_matter,
    arch_03_mechanism_of_charging_by_friction_triboelectric,
    arch_04_movement_of_electrons_versus_immobile_protons,
    arch_05_perspex_rod_rubbed_with_cloth_electron_transfer,
    arch_06_polythene_rod_rubbed_with_wool_electron_transfer,
    arch_07_identifying_positive_charge_from_electron_deficit,
    arch_08_identifying_negative_charge_from_electron_excess,
    arch_09_fundamental_law_of_charges_attraction_repulsion,
    arch_10_suspended_charged_rods_interaction,
    arch_11_charged_balloon_sticking_to_neutral_wall_induction,
    arch_12_charged_plastic_comb_attracting_paper_scraps,
    arch_13_bending_thin_stream_of_water_with_charged_rod,
    arch_14_electrostatic_induction_mechanism_in_neutral_objects,
    arch_15_gold_leaf_electroscope_structure_and_operation,
    arch_16_detecting_charge_using_an_electroscope,
    arch_17_electroscope_leaf_divergence_angle_and_charge_magnitude,
    arch_18_van_de_graaff_generator_belt_and_dome_mechanism,
    arch_19_hair_standing_on_end_van_de_graaff_demonstration,
    arch_20_standing_on_insulating_stool_during_van_de_graaff,
    arch_21_concept_of_earthing_or_grounding_a_conductor,
    arch_22_earthing_a_negatively_charged_body_electron_flow,
    arch_23_earthing_a_positively_charged_body_electron_flow,
    arch_24_electrostatic_shock_from_car_door_or_shopping_trolley,
    arch_25_crackling_and_sparks_when_removing_woollen_jersey,
)
from .ns8_static_electricity_archetypes_26_50 import (
    arch_26_charge_separation_in_thunderclouds,
    arch_27_lightning_as_giant_electrostatic_discharge,
    arch_28_thunder_as_acoustic_shockwave_of_heated_air,
    arch_29_function_and_design_of_lightning_conductor_rods,
    arch_30_lightning_safety_precautions_outdoors,
    arch_31_lightning_safety_precautions_indoors,
    arch_32_faraday_cage_effect_safety_inside_metal_car,
    arch_33_electrostatic_precipitators_in_smokestacks,
    arch_34_electrostatic_spray_painting_efficiency,
    arch_35_photocopier_laser_printer_toner_attraction,
    arch_36_fuel_tanker_earthing_grounding_safety,
    arch_37_aircraft_refuelling_static_bonding_clamp,
    arch_38_anti_static_wrist_straps_in_electronics_repair,
    arch_39_static_cling_in_clothes_dryers,
    arch_40_triboelectric_series_ranking_charge_tendency,
    arch_41_calculating_net_charge_from_protons_and_electrons,
    arch_42_predicting_interaction_between_multiple_charged_spheres,
    arch_43_charging_by_contact_conduction_between_spheres,
    arch_44_separating_two_neutral_spheres_in_presence_of_charged_rod,
    arch_45_misconception_positive_protons_move_during_charging,
    arch_46_misconception_neutral_objects_have_no_charges_at_all,
    arch_47_misconception_static_electricity_is_a_different_kind_of_energy,
    arch_48_misconception_lightning_never_strikes_the_same_place_twice,
    arch_49_investigating_factors_affecting_static_charge_strength,
    arch_50_static_electricity_comprehensive_diagnostic_evaluation,
)

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    "01_atomic_structure_and_electrical_charges": arch_01_atomic_structure_and_electrical_charges,
    "02_concept_of_neutral_uncharged_matter": arch_02_concept_of_neutral_uncharged_matter,
    "03_mechanism_of_charging_by_friction_triboelectric": arch_03_mechanism_of_charging_by_friction_triboelectric,
    "04_movement_of_electrons_versus_immobile_protons": arch_04_movement_of_electrons_versus_immobile_protons,
    "05_perspex_rod_rubbed_with_cloth_electron_transfer": arch_05_perspex_rod_rubbed_with_cloth_electron_transfer,
    "06_polythene_rod_rubbed_with_wool_electron_transfer": arch_06_polythene_rod_rubbed_with_wool_electron_transfer,
    "07_identifying_positive_charge_from_electron_deficit": arch_07_identifying_positive_charge_from_electron_deficit,
    "08_identifying_negative_charge_from_electron_excess": arch_08_identifying_negative_charge_from_electron_excess,
    "09_fundamental_law_of_charges_attraction_repulsion": arch_09_fundamental_law_of_charges_attraction_repulsion,
    "10_suspended_charged_rods_interaction": arch_10_suspended_charged_rods_interaction,
    "11_charged_balloon_sticking_to_neutral_wall_induction": arch_11_charged_balloon_sticking_to_neutral_wall_induction,
    "12_charged_plastic_comb_attracting_paper_scraps": arch_12_charged_plastic_comb_attracting_paper_scraps,
    "13_bending_thin_stream_of_water_with_charged_rod": arch_13_bending_thin_stream_of_water_with_charged_rod,
    "14_electrostatic_induction_mechanism_in_neutral_objects": arch_14_electrostatic_induction_mechanism_in_neutral_objects,
    "15_gold_leaf_electroscope_structure_and_operation": arch_15_gold_leaf_electroscope_structure_and_operation,
    "16_detecting_charge_using_an_electroscope": arch_16_detecting_charge_using_an_electroscope,
    "17_electroscope_leaf_divergence_angle_and_charge_magnitude": arch_17_electroscope_leaf_divergence_angle_and_charge_magnitude,
    "18_van_de_graaff_generator_belt_and_dome_mechanism": arch_18_van_de_graaff_generator_belt_and_dome_mechanism,
    "19_hair_standing_on_end_van_de_graaff_demonstration": arch_19_hair_standing_on_end_van_de_graaff_demonstration,
    "20_standing_on_insulating_stool_during_van_de_graaff": arch_20_standing_on_insulating_stool_during_van_de_graaff,
    "21_concept_of_earthing_or_grounding_a_conductor": arch_21_concept_of_earthing_or_grounding_a_conductor,
    "22_earthing_a_negatively_charged_body_electron_flow": arch_22_earthing_a_negatively_charged_body_electron_flow,
    "23_earthing_a_positively_charged_body_electron_flow": arch_23_earthing_a_positively_charged_body_electron_flow,
    "24_electrostatic_shock_from_car_door_or_shopping_trolley": arch_24_electrostatic_shock_from_car_door_or_shopping_trolley,
    "25_crackling_and_sparks_when_removing_woollen_jersey": arch_25_crackling_and_sparks_when_removing_woollen_jersey,
    "26_charge_separation_in_thunderclouds": arch_26_charge_separation_in_thunderclouds,
    "27_lightning_as_giant_electrostatic_discharge": arch_27_lightning_as_giant_electrostatic_discharge,
    "28_thunder_as_acoustic_shockwave_of_heated_air": arch_28_thunder_as_acoustic_shockwave_of_heated_air,
    "29_function_and_design_of_lightning_conductor_rods": arch_29_function_and_design_of_lightning_conductor_rods,
    "30_lightning_safety_precautions_outdoors": arch_30_lightning_safety_precautions_outdoors,
    "31_lightning_safety_precautions_indoors": arch_31_lightning_safety_precautions_indoors,
    "32_faraday_cage_effect_safety_inside_metal_car": arch_32_faraday_cage_effect_safety_inside_metal_car,
    "33_electrostatic_precipitators_in_smokestacks": arch_33_electrostatic_precipitators_in_smokestacks,
    "34_electrostatic_spray_painting_efficiency": arch_34_electrostatic_spray_painting_efficiency,
    "35_photocopier_laser_printer_toner_attraction": arch_35_photocopier_laser_printer_toner_attraction,
    "36_fuel_tanker_earthing_grounding_safety": arch_36_fuel_tanker_earthing_grounding_safety,
    "37_aircraft_refuelling_static_bonding_clamp": arch_37_aircraft_refuelling_static_bonding_clamp,
    "38_anti_static_wrist_straps_in_electronics_repair": arch_38_anti_static_wrist_straps_in_electronics_repair,
    "39_static_cling_in_clothes_dryers": arch_39_static_cling_in_clothes_dryers,
    "40_triboelectric_series_ranking_charge_tendency": arch_40_triboelectric_series_ranking_charge_tendency,
    "41_calculating_net_charge_from_protons_and_electrons": arch_41_calculating_net_charge_from_protons_and_electrons,
    "42_predicting_interaction_between_multiple_charged_spheres": arch_42_predicting_interaction_between_multiple_charged_spheres,
    "43_charging_by_contact_conduction_between_spheres": arch_43_charging_by_contact_conduction_between_spheres,
    "44_separating_two_neutral_spheres_in_presence_of_charged_rod": arch_44_separating_two_neutral_spheres_in_presence_of_charged_rod,
    "45_misconception_positive_protons_move_during_charging": arch_45_misconception_positive_protons_move_during_charging,
    "46_misconception_neutral_objects_have_no_charges_at_all": arch_46_misconception_neutral_objects_have_no_charges_at_all,
    "47_misconception_static_electricity_is_a_different_kind_of_energy": arch_47_misconception_static_electricity_is_a_different_kind_of_energy,
    "48_misconception_lightning_never_strikes_the_same_place_twice": arch_48_misconception_lightning_never_strikes_the_same_place_twice,
    "49_investigating_factors_affecting_static_charge_strength": arch_49_investigating_factors_affecting_static_charge_strength,
    "50_static_electricity_comprehensive_diagnostic_evaluation": arch_50_static_electricity_comprehensive_diagnostic_evaluation,
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
