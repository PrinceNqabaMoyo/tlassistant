"""Grade 7 Natural Sciences: Term 2 - Separating Mixtures Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/PDF - Separating mixtures.md.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_separating_mixtures_archetypes_01_25 import (
    arch_01_mixture_definition_physical_combination,
    arch_02_types_of_mixtures_solid_solid,
    arch_03_suspension_definition_and_properties,
    arch_04_solution_definition_solute_solvent,
    arch_05_suspension_vs_solution_comparison,
    arch_06_miscible_vs_immiscible_liquids,
    arch_07_emulsions_and_layer_separation,
    arch_08_gas_gas_mixtures_air_composition,
    arch_09_solid_gas_liquid_gas_mixtures,
    arch_10_hand_sorting_principles_and_uses,
    arch_11_sieving_particle_size_separation,
    arch_12_magnetic_separation_iron_sand,
    arch_13_magnetic_separation_industrial_scrap,
    arch_14_filtration_residue_and_filtrate,
    arch_15_filtration_insoluble_solid_liquid,
    arch_16_filtration_apparatus_setup,
    arch_17_sedimentation_and_settling_principle,
    arch_18_decanting_technique_and_limits,
    arch_19_centrifuging_speed_separation,
    arch_20_evaporation_recovering_solute,
    arch_21_rate_of_evaporation_factors,
    arch_22_crystallisation_from_solution,
    arch_23_simple_distillation_apparatus_parts,
    arch_24_simple_distillation_water_flow_direction,
    arch_25_simple_distillation_pure_water_recovery,
)

from .ns7_separating_mixtures_archetypes_26_50 import (
    arch_26_fractional_distillation_differing_boiling_points,
    arch_27_fractional_distillation_crude_oil,
    arch_28_fractionating_column_condensation_cycles,
    arch_29_paper_chromatography_baseline_pencil,
    arch_30_paper_chromatography_solvent_level,
    arch_31_paper_chromatography_pigment_separation,
    arch_32_paper_chromatography_interpreting_spots,
    arch_33_paper_chromatography_forensic_ink_match,
    arch_34_paper_chromatography_retention_factor_rf,
    arch_35_separating_funnel_immiscible_liquids,
    arch_36_multi_step_separation_sand_salt_water,
    arch_37_multi_step_separation_iron_salt_sand,
    arch_38_separating_sawdust_and_sand_flotation,
    arch_39_water_purification_municipal_steps,
    arch_40_water_treatment_flocculation_coagulation,
    arch_41_water_treatment_disinfection_chlorine,
    arch_42_desalination_reverse_osmosis_distillation,
    arch_43_separation_at_source_waste_management,
    arch_44_mechanical_recycling_trommel_screens,
    arch_45_eddy_current_separators_aluminium,
    arch_46_optical_sensor_sorting_near_infrared,
    arch_47_air_classification_winnowing_density,
    arch_48_evaluating_separation_efficiency_percentage,
    arch_49_troubleshooting_separation_method_errors,
    arch_50_designing_separation_strategy_novel_mixture,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 09: Concepts & Types of Mixtures
    arch_01_mixture_definition_physical_combination,
    arch_02_types_of_mixtures_solid_solid,
    arch_03_suspension_definition_and_properties,
    arch_04_solution_definition_solute_solvent,
    arch_05_suspension_vs_solution_comparison,
    arch_06_miscible_vs_immiscible_liquids,
    arch_07_emulsions_and_layer_separation,
    arch_08_gas_gas_mixtures_air_composition,
    arch_09_solid_gas_liquid_gas_mixtures,
    # 10 - 19: Mechanical Separation & Filtration
    arch_10_hand_sorting_principles_and_uses,
    arch_11_sieving_particle_size_separation,
    arch_12_magnetic_separation_iron_sand,
    arch_13_magnetic_separation_industrial_scrap,
    arch_14_filtration_residue_and_filtrate,
    arch_15_filtration_insoluble_solid_liquid,
    arch_16_filtration_apparatus_setup,
    arch_17_sedimentation_and_settling_principle,
    arch_18_decanting_technique_and_limits,
    arch_19_centrifuging_speed_separation,
    # 20 - 25: Evaporation, Distillation & Thermal Separation
    arch_20_evaporation_recovering_solute,
    arch_21_rate_of_evaporation_factors,
    arch_22_crystallisation_from_solution,
    arch_23_simple_distillation_apparatus_parts,
    arch_24_simple_distillation_water_flow_direction,
    arch_25_simple_distillation_pure_water_recovery,
    # 26 - 34: Fractional Distillation & Chromatography
    arch_26_fractional_distillation_differing_boiling_points,
    arch_27_fractional_distillation_crude_oil,
    arch_28_fractionating_column_condensation_cycles,
    arch_29_paper_chromatography_baseline_pencil,
    arch_30_paper_chromatography_solvent_level,
    arch_31_paper_chromatography_pigment_separation,
    arch_32_paper_chromatography_interpreting_spots,
    arch_33_paper_chromatography_forensic_ink_match,
    arch_34_paper_chromatography_retention_factor_rf,
    # 35 - 42: Multi-Step Separation & Water Purification
    arch_35_separating_funnel_immiscible_liquids,
    arch_36_multi_step_separation_sand_salt_water,
    arch_37_multi_step_separation_iron_salt_sand,
    arch_38_separating_sawdust_and_sand_flotation,
    arch_39_water_purification_municipal_steps,
    arch_40_water_treatment_flocculation_coagulation,
    arch_41_water_treatment_disinfection_chlorine,
    arch_42_desalination_reverse_osmosis_distillation,
    # 43 - 50: Sorting Waste & Separation Strategy
    arch_43_separation_at_source_waste_management,
    arch_44_mechanical_recycling_trommel_screens,
    arch_45_eddy_current_separators_aluminium,
    arch_46_optical_sensor_sorting_near_infrared,
    arch_47_air_classification_winnowing_density,
    arch_48_evaluating_separation_efficiency_percentage,
    arch_49_troubleshooting_separation_method_errors,
    arch_50_designing_separation_strategy_novel_mixture,
]

SUBSKILLS: List[str] = [
    # 01 - 09
    "01_mixture_definition_physical_combination",
    "02_types_of_mixtures_solid_solid",
    "03_suspension_definition_and_properties",
    "04_solution_definition_solute_solvent",
    "05_suspension_vs_solution_comparison",
    "06_miscible_vs_immiscible_liquids",
    "07_emulsions_and_layer_separation",
    "08_gas_gas_mixtures_air_composition",
    "09_solid_gas_liquid_gas_mixtures",
    # 10 - 19
    "10_hand_sorting_principles_and_uses",
    "11_sieving_particle_size_separation",
    "12_magnetic_separation_iron_sand",
    "13_magnetic_separation_industrial_scrap",
    "14_filtration_residue_and_filtrate",
    "15_filtration_insoluble_solid_liquid",
    "16_filtration_apparatus_setup",
    "17_sedimentation_and_settling_principle",
    "18_decanting_technique_and_limits",
    "19_centrifuging_speed_separation",
    # 20 - 25
    "20_evaporation_recovering_solute",
    "21_rate_of_evaporation_factors",
    "22_crystallisation_from_solution",
    "23_simple_distillation_apparatus_parts",
    "24_simple_distillation_water_flow_direction",
    "25_simple_distillation_pure_water_recovery",
    # 26 - 34
    "26_fractional_distillation_differing_boiling_points",
    "27_fractional_distillation_crude_oil",
    "28_fractionating_column_condensation_cycles",
    "29_paper_chromatography_baseline_pencil",
    "30_paper_chromatography_solvent_level",
    "31_paper_chromatography_pigment_separation",
    "32_paper_chromatography_interpreting_spots",
    "33_paper_chromatography_forensic_ink_match",
    "34_paper_chromatography_retention_factor_rf",
    # 35 - 42
    "35_separating_funnel_immiscible_liquids",
    "36_multi_step_separation_sand_salt_water",
    "37_multi_step_separation_iron_salt_sand",
    "38_separating_sawdust_and_sand_flotation",
    "39_water_purification_municipal_steps",
    "40_water_treatment_flocculation_coagulation",
    "41_water_treatment_disinfection_chlorine",
    "42_desalination_reverse_osmosis_distillation",
    # 43 - 50
    "43_separation_at_source_waste_management",
    "44_mechanical_recycling_trommel_screens",
    "45_eddy_current_separators_aluminium",
    "46_optical_sensor_sorting_near_infrared",
    "47_air_classification_winnowing_density",
    "48_evaluating_separation_efficiency_percentage",
    "49_troubleshooting_separation_method_errors",
    "50_designing_separation_strategy_novel_mixture",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based integer and padded string aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["methods_hand_sorting"] = arch_10_hand_sorting_principles_and_uses
DISPATCH_TABLE["methods_sieving_filtration"] = arch_11_sieving_particle_size_separation
DISPATCH_TABLE["methods_evaporation_distillation"] = arch_20_evaporation_recovering_solute
DISPATCH_TABLE["chromatography"] = arch_31_paper_chromatography_pigment_separation
DISPATCH_TABLE["recycling_waste_management"] = arch_43_separation_at_source_waste_management


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
    Main entry point for Grade 7 Natural Sciences: Separating Mixtures Generator.
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
        q.setdefault("grade", 7)
        q.setdefault("subject", "Natural Sciences")
        q.setdefault("topic", "Separating mixtures")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
