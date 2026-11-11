"""Grade 8 Natural Sciences: Term 2 - Atoms Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/01. Atoms.md.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .ns8_atoms_subatomic_archetypes_01_25 import (
    arch_01_democritus_atomos_concept,
    arch_02_daltons_atomic_postulates,
    arch_03_scientific_models_evolution,
    arch_04_thomson_plum_pudding_model,
    arch_05_rutherford_gold_foil_scattering,
    arch_06_bohr_planetary_atomic_model,
    arch_07_subatomic_particles_charges,
    arch_08_subatomic_particles_locations,
    arch_09_subatomic_particles_relative_masses,
    arch_10_atomic_number_protons_element_identity,
    arch_11_atomic_mass_protons_plus_neutrons,
    arch_12_electrical_neutrality_of_atoms,
    arch_13_deducing_p_n_e_counts_from_nuclide_symbol,
    arch_14_electron_energy_levels_capacity_2_8_8,
    arch_15_drawing_bohr_rutherford_diagram,
    arch_16_first_twenty_elements_z1_to_z5,
    arch_17_first_twenty_elements_z6_to_z10,
    arch_18_first_twenty_elements_z11_to_z15,
    arch_19_first_twenty_elements_z16_to_z20,
    arch_20_chemical_symbols_rules_and_origins,
    arch_21_periodic_table_periods_and_groups_gr8,
    arch_22_periodic_table_metals_vs_non_metals_gr8,
    arch_23_atomic_size_trends_concept,
    arch_24_isotopes_concept_introductory,
    arch_25_evaluating_atomic_data_cards_gr8,
)

from .ns8_atoms_subatomic_archetypes_26_50 import (
    arch_26_molecules_of_elements_definition,
    arch_27_diatomic_elements_the_septet,
    arch_28_chemical_bonding_forces_between_atoms,
    arch_29_particle_model_diatomic_molecules,
    arch_30_monoatomic_noble_gases_vs_diatomic_gases,
    arch_31_subscript_notation_in_element_molecules,
    arch_32_gaseous_diatomic_elements_in_atmosphere,
    arch_33_compounds_definition_fixed_ratio,
    arch_34_properties_of_compound_differ_from_elements,
    arch_35_interpreting_formulas_binary_compounds,
    arch_36_counting_atoms_in_polyatomic_formulas,
    arch_37_particle_diagram_compounds_vs_elements,
    arch_38_naming_binary_compounds_rules,
    arch_39_naming_covalent_compounds_prefixes,
    arch_40_lattice_compounds_vs_covalent_molecules,
    arch_41_mixture_vs_compound_distinction_iron_sulfur,
    arch_42_physical_vs_chemical_separation_methods,
    arch_43_decomposition_reactions_definition,
    arch_44_electrolysis_of_water,
    arch_45_electrolysis_of_copper_chloride,
    arch_46_thermal_decomposition_copper_carbonate,
    arch_47_thermal_decomposition_mercury_oxide,
    arch_48_testing_gases_from_decomposition,
    arch_49_scientific_inquiry_identifying_unknown_substance,
    arch_50_atoms_compounds_master_synthesis_challenge,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 06: Historical Models & Atomic Postulates
    arch_01_democritus_atomos_concept,
    arch_02_daltons_atomic_postulates,
    arch_03_scientific_models_evolution,
    arch_04_thomson_plum_pudding_model,
    arch_05_rutherford_gold_foil_scattering,
    arch_06_bohr_planetary_atomic_model,
    # 07 - 15: Subatomic Particles & Atomic Structure
    arch_07_subatomic_particles_charges,
    arch_08_subatomic_particles_locations,
    arch_09_subatomic_particles_relative_masses,
    arch_10_atomic_number_protons_element_identity,
    arch_11_atomic_mass_protons_plus_neutrons,
    arch_12_electrical_neutrality_of_atoms,
    arch_13_deducing_p_n_e_counts_from_nuclide_symbol,
    arch_14_electron_energy_levels_capacity_2_8_8,
    arch_15_drawing_bohr_rutherford_diagram,
    # 16 - 25: First 20 Elements & Periodic Table Grounding
    arch_16_first_twenty_elements_z1_to_z5,
    arch_17_first_twenty_elements_z6_to_z10,
    arch_18_first_twenty_elements_z11_to_z15,
    arch_19_first_twenty_elements_z16_to_z20,
    arch_20_chemical_symbols_rules_and_origins,
    arch_21_periodic_table_periods_and_groups_gr8,
    arch_22_periodic_table_metals_vs_non_metals_gr8,
    arch_23_atomic_size_trends_concept,
    arch_24_isotopes_concept_introductory,
    arch_25_evaluating_atomic_data_cards_gr8,
    # 26 - 32: Molecules of Elements & Diatomic Gases
    arch_26_molecules_of_elements_definition,
    arch_27_diatomic_elements_the_septet,
    arch_28_chemical_bonding_forces_between_atoms,
    arch_29_particle_model_diatomic_molecules,
    arch_30_monoatomic_noble_gases_vs_diatomic_gases,
    arch_31_subscript_notation_in_element_molecules,
    arch_32_gaseous_diatomic_elements_in_atmosphere,
    # 33 - 40: Compounds & Chemical Formulas
    arch_33_compounds_definition_fixed_ratio,
    arch_34_properties_of_compound_differ_from_elements,
    arch_35_interpreting_formulas_binary_compounds,
    arch_36_counting_atoms_in_polyatomic_formulas,
    arch_37_particle_diagram_compounds_vs_elements,
    arch_38_naming_binary_compounds_rules,
    arch_39_naming_covalent_compounds_prefixes,
    arch_40_lattice_compounds_vs_covalent_molecules,
    # 41 - 50: Mixtures vs Compounds & Chemical Decomposition
    arch_41_mixture_vs_compound_distinction_iron_sulfur,
    arch_42_physical_vs_chemical_separation_methods,
    arch_43_decomposition_reactions_definition,
    arch_44_electrolysis_of_water,
    arch_45_electrolysis_of_copper_chloride,
    arch_46_thermal_decomposition_copper_carbonate,
    arch_47_thermal_decomposition_mercury_oxide,
    arch_48_testing_gases_from_decomposition,
    arch_49_scientific_inquiry_identifying_unknown_substance,
    arch_50_atoms_compounds_master_synthesis_challenge,
]

SUBSKILLS: List[str] = [
    # 01 - 06
    "01_democritus_atomos_concept",
    "02_daltons_atomic_postulates",
    "03_scientific_models_evolution",
    "04_thomson_plum_pudding_model",
    "05_rutherford_gold_foil_scattering",
    "06_bohr_planetary_atomic_model",
    # 07 - 15
    "07_subatomic_particles_charges",
    "08_subatomic_particles_locations",
    "09_subatomic_particles_relative_masses",
    "10_atomic_number_protons_element_identity",
    "11_atomic_mass_protons_plus_neutrons",
    "12_electrical_neutrality_of_atoms",
    "13_deducing_p_n_e_counts_from_nuclide_symbol",
    "14_electron_energy_levels_capacity_2_8_8",
    "15_drawing_bohr_rutherford_diagram",
    # 16 - 25
    "16_first_twenty_elements_z1_to_z5",
    "17_first_twenty_elements_z6_to_z10",
    "18_first_twenty_elements_z11_to_z15",
    "19_first_twenty_elements_z16_to_z20",
    "20_chemical_symbols_rules_and_origins",
    "21_periodic_table_periods_and_groups_gr8",
    "22_periodic_table_metals_vs_non_metals_gr8",
    "23_atomic_size_trends_concept",
    "24_isotopes_concept_introductory",
    "25_evaluating_atomic_data_cards_gr8",
    # 26 - 32
    "26_molecules_of_elements_definition",
    "27_diatomic_elements_the_septet",
    "28_chemical_bonding_forces_between_atoms",
    "29_particle_model_diatomic_molecules",
    "30_monoatomic_noble_gases_vs_diatomic_gases",
    "31_subscript_notation_in_element_molecules",
    "32_gaseous_diatomic_elements_in_atmosphere",
    # 33 - 40
    "33_compounds_definition_fixed_ratio",
    "34_properties_of_compound_differ_from_elements",
    "35_interpreting_formulas_binary_compounds",
    "36_counting_atoms_in_polyatomic_formulas",
    "37_particle_diagram_compounds_vs_elements",
    "38_naming_binary_compounds_rules",
    "39_naming_covalent_compounds_prefixes",
    "40_lattice_compounds_vs_covalent_molecules",
    # 41 - 50
    "41_mixture_vs_compound_distinction_iron_sulfur",
    "42_physical_vs_chemical_separation_methods",
    "43_decomposition_reactions_definition",
    "44_electrolysis_of_water",
    "45_electrolysis_of_copper_chloride",
    "46_thermal_decomposition_copper_carbonate",
    "47_thermal_decomposition_mercury_oxide",
    "48_testing_gases_from_decomposition",
    "49_scientific_inquiry_identifying_unknown_substance",
    "50_atoms_compounds_master_synthesis_challenge",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based integer and padded string aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["subatomic_particles_and_charges"] = arch_07_subatomic_particles_charges
DISPATCH_TABLE["atomic_number_and_neutrality"] = arch_10_atomic_number_protons_element_identity
DISPATCH_TABLE["first_twenty_elements_and_symbols"] = arch_16_first_twenty_elements_z1_to_z5
DISPATCH_TABLE["elements_compounds_diatomic_molecules"] = arch_27_diatomic_elements_the_septet
DISPATCH_TABLE["decomposition_of_compounds_electrolysis"] = arch_44_electrolysis_of_water


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
    Main entry point for Grade 8 Natural Sciences: Atoms Generator.
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
        q.setdefault("topic", "Atoms")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
