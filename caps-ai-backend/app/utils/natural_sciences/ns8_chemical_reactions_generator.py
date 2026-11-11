"""Grade 8 Natural Sciences: Term 2 - Chemical Reactions Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/PDF - Chemical reactions.md.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .ns8_chemical_reactions_archetypes_01_25 import (
    arch_01_physical_vs_chemical_change_definition,
    arch_02_classifying_everyday_changes_physical_vs_chemical,
    arch_03_signs_of_chemical_reaction_color_and_gas,
    arch_04_signs_of_chemical_reaction_precipitate,
    arch_05_signs_of_chemical_reaction_temperature_and_light,
    arch_06_eggshell_and_vinegar_investigation,
    arch_07_exothermic_vs_endothermic_reactions,
    arch_08_reversibility_physical_vs_chemical,
    arch_09_reactants_and_products_definition_left_right,
    arch_10_interpreting_word_equations,
    arch_11_writing_word_equations_combustion,
    arch_12_writing_word_equations_metal_synthesis,
    arch_13_writing_word_equations_acid_carbonate,
    arch_14_writing_word_equations_decomposition,
    arch_15_interpreting_subscripts_vs_coefficients,
    arch_16_particle_diagram_reactants_to_products,
    arch_17_identifying_leftover_reactants_limiting_excess,
    arch_18_chemical_reaction_as_atomic_rearrangement,
    arch_19_bond_breaking_endothermic_vs_bond_making_exothermic,
    arch_20_law_of_conservation_of_atoms,
    arch_21_law_of_conservation_of_mass_closed_system,
    arch_22_mass_loss_in_open_vessel_gas_escape,
    arch_23_counting_atoms_reactant_side_vs_product_side,
    arch_24_particle_model_synthesis_of_water,
    arch_25_particle_model_combustion_of_methane,
)

from .ns8_chemical_reactions_archetypes_26_50 import (
    arch_26_why_equations_must_be_balanced,
    arch_27_balancing_synthesis_reactions_magnesium_oxide,
    arch_28_balancing_synthesis_reactions_water,
    arch_29_balancing_synthesis_reactions_iron_sulfide,
    arch_30_balancing_combustion_carbon_and_carbon_monoxide,
    arch_31_balancing_decomposition_hydrogen_peroxide,
    arch_32_balancing_metal_acid_reaction_zinc_hydrochloric,
    arch_33_balancing_rusting_reaction_iron_oxygen,
    arch_34_common_mistakes_changing_subscripts_vs_coefficients,
    arch_35_fermentation_definition_and_microorganisms,
    arch_36_indigenous_brewing_umqombothi_and_ginger_beer,
    arch_37_fermentation_in_baking_bread,
    arch_38_fermentation_in_dairy_amasi_and_yoghurt,
    arch_39_indigenous_metal_smelting_iron_and_copper,
    arch_40_combustion_of_fossil_fuels_coal_and_paraffin,
    arch_41_rusting_corrosion_conditions_water_and_oxygen,
    arch_42_rust_prevention_methods_painting_galvanising,
    arch_43_testing_reaction_products_gases_summary,
    arch_44_investigating_temperature_change_exothermic_reaction,
    arch_45_investigating_rusting_factors_fair_test,
    arch_46_evaluating_chemical_reaction_rate_factors,
    arch_47_chemical_reactions_in_daily_cleaning_and_safety,
    arch_48_misconceptions_mass_destroyed_when_ash_forms,
    arch_49_scientific_inquiry_identifying_mystery_reaction,
    arch_50_chemical_reactions_master_synthesis_challenge,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 08: Physical vs Chemical Changes & Reaction Signs
    arch_01_physical_vs_chemical_change_definition,
    arch_02_classifying_everyday_changes_physical_vs_chemical,
    arch_03_signs_of_chemical_reaction_color_and_gas,
    arch_04_signs_of_chemical_reaction_precipitate,
    arch_05_signs_of_chemical_reaction_temperature_and_light,
    arch_06_eggshell_and_vinegar_investigation,
    arch_07_exothermic_vs_endothermic_reactions,
    arch_08_reversibility_physical_vs_chemical,
    # 09 - 15: Reactants, Products, and Word Equations
    arch_09_reactants_and_products_definition_left_right,
    arch_10_interpreting_word_equations,
    arch_11_writing_word_equations_combustion,
    arch_12_writing_word_equations_metal_synthesis,
    arch_13_writing_word_equations_acid_carbonate,
    arch_14_writing_word_equations_decomposition,
    arch_15_interpreting_subscripts_vs_coefficients,
    # 16 - 25: Atomic Rearrangement & Conservation of Mass/Atoms
    arch_16_particle_diagram_reactants_to_products,
    arch_17_identifying_leftover_reactants_limiting_excess,
    arch_18_chemical_reaction_as_atomic_rearrangement,
    arch_19_bond_breaking_endothermic_vs_bond_making_exothermic,
    arch_20_law_of_conservation_of_atoms,
    arch_21_law_of_conservation_of_mass_closed_system,
    arch_22_mass_loss_in_open_vessel_gas_escape,
    arch_23_counting_atoms_reactant_side_vs_product_side,
    arch_24_particle_model_synthesis_of_water,
    arch_25_particle_model_combustion_of_methane,
    # 26 - 34: Balancing Chemical Equations
    arch_26_why_equations_must_be_balanced,
    arch_27_balancing_synthesis_reactions_magnesium_oxide,
    arch_28_balancing_synthesis_reactions_water,
    arch_29_balancing_synthesis_reactions_iron_sulfide,
    arch_30_balancing_combustion_carbon_and_carbon_monoxide,
    arch_31_balancing_decomposition_hydrogen_peroxide,
    arch_32_balancing_metal_acid_reaction_zinc_hydrochloric,
    arch_33_balancing_rusting_reaction_iron_oxygen,
    arch_34_common_mistakes_changing_subscripts_vs_coefficients,
    # 35 - 42: Fermentation, Indigenous Technology, Rusting & Combustion
    arch_35_fermentation_definition_and_microorganisms,
    arch_36_indigenous_brewing_umqombothi_and_ginger_beer,
    arch_37_fermentation_in_baking_bread,
    arch_38_fermentation_in_dairy_amasi_and_yoghurt,
    arch_39_indigenous_metal_smelting_iron_and_copper,
    arch_40_combustion_of_fossil_fuels_coal_and_paraffin,
    arch_41_rusting_corrosion_conditions_water_and_oxygen,
    arch_42_rust_prevention_methods_painting_galvanising,
    # 43 - 50: Scientific Inquiry, Gas Testing & Master Synthesis
    arch_43_testing_reaction_products_gases_summary,
    arch_44_investigating_temperature_change_exothermic_reaction,
    arch_45_investigating_rusting_factors_fair_test,
    arch_46_evaluating_chemical_reaction_rate_factors,
    arch_47_chemical_reactions_in_daily_cleaning_and_safety,
    arch_48_misconceptions_mass_destroyed_when_ash_forms,
    arch_49_scientific_inquiry_identifying_mystery_reaction,
    arch_50_chemical_reactions_master_synthesis_challenge,
]

SUBSKILLS: List[str] = [
    # 01 - 08
    "01_physical_vs_chemical_change_definition",
    "02_classifying_everyday_changes_physical_vs_chemical",
    "03_signs_of_chemical_reaction_color_and_gas",
    "04_signs_of_chemical_reaction_precipitate",
    "05_signs_of_chemical_reaction_temperature_and_light",
    "06_eggshell_and_vinegar_investigation",
    "07_exothermic_vs_endothermic_reactions",
    "08_reversibility_physical_vs_chemical",
    # 09 - 15
    "09_reactants_and_products_definition_left_right",
    "10_interpreting_word_equations",
    "11_writing_word_equations_combustion",
    "12_writing_word_equations_metal_synthesis",
    "13_writing_word_equations_acid_carbonate",
    "14_writing_word_equations_decomposition",
    "15_interpreting_subscripts_vs_coefficients",
    # 16 - 25
    "16_particle_diagram_reactants_to_products",
    "17_identifying_leftover_reactants_limiting_excess",
    "18_chemical_reaction_as_atomic_rearrangement",
    "19_bond_breaking_endothermic_vs_bond_making_exothermic",
    "20_law_of_conservation_of_atoms",
    "21_law_of_conservation_of_mass_closed_system",
    "22_mass_loss_in_open_vessel_gas_escape",
    "23_counting_atoms_reactant_side_vs_product_side",
    "24_particle_model_synthesis_of_water",
    "25_particle_model_combustion_of_methane",
    # 26 - 34
    "26_why_equations_must_be_balanced",
    "27_balancing_synthesis_reactions_magnesium_oxide",
    "28_balancing_synthesis_reactions_water",
    "29_balancing_synthesis_reactions_iron_sulfide",
    "30_balancing_combustion_carbon_and_carbon_monoxide",
    "31_balancing_decomposition_hydrogen_peroxide",
    "32_balancing_metal_acid_reaction_zinc_hydrochloric",
    "33_balancing_rusting_reaction_iron_oxygen",
    "34_common_mistakes_changing_subscripts_vs_coefficients",
    # 35 - 42
    "35_fermentation_definition_and_microorganisms",
    "36_indigenous_brewing_umqombothi_and_ginger_beer",
    "37_fermentation_in_baking_bread",
    "38_fermentation_in_dairy_amasi_and_yoghurt",
    "39_indigenous_metal_smelting_iron_and_copper",
    "40_combustion_of_fossil_fuels_coal_and_paraffin",
    "41_rusting_corrosion_conditions_water_and_oxygen",
    "42_rust_prevention_methods_painting_galvanising",
    # 43 - 50
    "43_testing_reaction_products_gases_summary",
    "44_investigating_temperature_change_exothermic_reaction",
    "45_investigating_rusting_factors_fair_test",
    "46_evaluating_chemical_reaction_rate_factors",
    "47_chemical_reactions_in_daily_cleaning_and_safety",
    "48_misconceptions_mass_destroyed_when_ash_forms",
    "49_scientific_inquiry_identifying_mystery_reaction",
    "50_chemical_reactions_master_synthesis_challenge",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based integer and padded string aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["reactants_products_and_chemical_change"] = arch_01_physical_vs_chemical_change_definition
DISPATCH_TABLE["atomic_rearrangement_bond_breaking"] = arch_18_chemical_reaction_as_atomic_rearrangement
DISPATCH_TABLE["word_equations_representation"] = arch_10_interpreting_word_equations
DISPATCH_TABLE["fermentation_indigenous_knowledge"] = arch_35_fermentation_definition_and_microorganisms
DISPATCH_TABLE["carbon_dioxide_limewater_precipitation"] = arch_06_eggshell_and_vinegar_investigation


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
    Main entry point for Grade 8 Natural Sciences: Chemical Reactions Generator.
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
        q.setdefault("topic", "Chemical reactions")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
