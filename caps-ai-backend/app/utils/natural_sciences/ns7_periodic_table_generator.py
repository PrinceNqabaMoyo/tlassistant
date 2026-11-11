"""Grade 7 Natural Sciences: Term 2 - The Periodic Table of Elements Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/04. The Periodic Table of Elements.md.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_periodic_table_archetypes_01_25 import (
    arch_01_element_definition_pure_substance,
    arch_02_atom_as_building_block_of_element,
    arch_03_periodic_table_mendeleev_history,
    arch_04_atomic_number_definition_protons,
    arch_05_chemical_symbol_capitalization_rules,
    arch_06_latin_origin_symbols_iron_copper,
    arch_07_latin_origin_symbols_sodium_potassium,
    arch_08_latin_origin_symbols_gold_silver_lead,
    arch_09_first_twenty_elements_names_symbols_1_5,
    arch_10_first_twenty_elements_names_symbols_6_10,
    arch_11_first_twenty_elements_names_symbols_11_15,
    arch_12_first_twenty_elements_names_symbols_16_20,
    arch_13_identifying_element_from_atomic_number,
    arch_14_periods_definition_horizontal_rows,
    arch_15_groups_definition_vertical_columns,
    arch_16_metals_position_on_periodic_table,
    arch_17_non_metals_position_on_periodic_table,
    arch_18_semi_metals_zigzag_border_elements,
    arch_19_physical_properties_metals_lustre,
    arch_20_physical_properties_metals_conduction,
    arch_21_physical_properties_metals_malleability,
    arch_22_physical_properties_metals_ductility,
    arch_23_physical_properties_metals_melting_points,
    arch_24_liquid_elements_mercury_and_bromine,
    arch_25_density_comparison_metals_vs_non_metals,
)

from .ns7_periodic_table_archetypes_26_50 import (
    arch_26_non_metals_physical_states_room_temp,
    arch_27_non_metals_dull_and_brittle_solids,
    arch_28_non_metals_electrical_insulators_exception_graphite,
    arch_29_carbon_allotropes_diamond_and_graphite,
    arch_30_semi_metals_semiconductor_properties,
    arch_31_silicon_in_modern_computer_technology,
    arch_32_group_1_alkali_metals_properties,
    arch_33_group_1_alkali_metals_reactivity_trend,
    arch_34_group_2_alkaline_earth_metals,
    arch_35_group_17_halogens_properties,
    arch_36_group_18_noble_gases_inert_nature,
    arch_37_noble_gases_practical_applications,
    arch_38_element_vs_compound_distinction,
    arch_39_interpreting_chemical_formulas_atom_ratios,
    arch_40_diatomic_non_metal_molecules,
    arch_41_gaseous_elements_at_room_temperature,
    arch_42_mineral_ores_and_indigenous_metal_smelting,
    arch_43_abundance_of_elements_in_earth_crust,
    arch_44_abundance_of_elements_in_human_body,
    arch_45_transition_metals_overview,
    arch_46_evaluating_element_data_cards,
    arch_47_predicting_element_properties_from_position,
    arch_48_misconceptions_element_names_vs_brand_names,
    arch_49_scientific_inquiry_classifying_mystery_element,
    arch_50_periodic_table_master_classification_challenge,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 08: Elements, Atoms, History & Symbols
    arch_01_element_definition_pure_substance,
    arch_02_atom_as_building_block_of_element,
    arch_03_periodic_table_mendeleev_history,
    arch_04_atomic_number_definition_protons,
    arch_05_chemical_symbol_capitalization_rules,
    arch_06_latin_origin_symbols_iron_copper,
    arch_07_latin_origin_symbols_sodium_potassium,
    arch_08_latin_origin_symbols_gold_silver_lead,
    # 09 - 15: First 20 Elements & Table Structure
    arch_09_first_twenty_elements_names_symbols_1_5,
    arch_10_first_twenty_elements_names_symbols_6_10,
    arch_11_first_twenty_elements_names_symbols_11_15,
    arch_12_first_twenty_elements_names_symbols_16_20,
    arch_13_identifying_element_from_atomic_number,
    arch_14_periods_definition_horizontal_rows,
    arch_15_groups_definition_vertical_columns,
    # 16 - 25: Regions & Physical Properties of Metals
    arch_16_metals_position_on_periodic_table,
    arch_17_non_metals_position_on_periodic_table,
    arch_18_semi_metals_zigzag_border_elements,
    arch_19_physical_properties_metals_lustre,
    arch_20_physical_properties_metals_conduction,
    arch_21_physical_properties_metals_malleability,
    arch_22_physical_properties_metals_ductility,
    arch_23_physical_properties_metals_melting_points,
    arch_24_liquid_elements_mercury_and_bromine,
    arch_25_density_comparison_metals_vs_non_metals,
    # 26 - 31: Non-metals & Semi-metals Properties
    arch_26_non_metals_physical_states_room_temp,
    arch_27_non_metals_dull_and_brittle_solids,
    arch_28_non_metals_electrical_insulators_exception_graphite,
    arch_29_carbon_allotropes_diamond_and_graphite,
    arch_30_semi_metals_semiconductor_properties,
    arch_31_silicon_in_modern_computer_technology,
    # 32 - 37: Key Element Groups & Periodic Patterns
    arch_32_group_1_alkali_metals_properties,
    arch_33_group_1_alkali_metals_reactivity_trend,
    arch_34_group_2_alkaline_earth_metals,
    arch_35_group_17_halogens_properties,
    arch_36_group_18_noble_gases_inert_nature,
    arch_37_noble_gases_practical_applications,
    # 38 - 41: Elements vs Compounds & Formulas
    arch_38_element_vs_compound_distinction,
    arch_39_interpreting_chemical_formulas_atom_ratios,
    arch_40_diatomic_non_metal_molecules,
    arch_41_gaseous_elements_at_room_temperature,
    # 42 - 45: Real-world Abundance & Metallurgy
    arch_42_mineral_ores_and_indigenous_metal_smelting,
    arch_43_abundance_of_elements_in_earth_crust,
    arch_44_abundance_of_elements_in_human_body,
    arch_45_transition_metals_overview,
    # 46 - 50: Scientific Inquiry & Master Challenges
    arch_46_evaluating_element_data_cards,
    arch_47_predicting_element_properties_from_position,
    arch_48_misconceptions_element_names_vs_brand_names,
    arch_49_scientific_inquiry_classifying_mystery_element,
    arch_50_periodic_table_master_classification_challenge,
]

SUBSKILLS: List[str] = [
    # 01 - 08
    "01_element_definition_pure_substance",
    "02_atom_as_building_block_of_element",
    "03_periodic_table_mendeleev_history",
    "04_atomic_number_definition_protons",
    "05_chemical_symbol_capitalization_rules",
    "06_latin_origin_symbols_iron_copper",
    "07_latin_origin_symbols_sodium_potassium",
    "08_latin_origin_symbols_gold_silver_lead",
    # 09 - 15
    "09_first_twenty_elements_names_symbols_1_5",
    "10_first_twenty_elements_names_symbols_6_10",
    "11_first_twenty_elements_names_symbols_11_15",
    "12_first_twenty_elements_names_symbols_16_20",
    "13_identifying_element_from_atomic_number",
    "14_periods_definition_horizontal_rows",
    "15_groups_definition_vertical_columns",
    # 16 - 25
    "16_metals_position_on_periodic_table",
    "17_non_metals_position_on_periodic_table",
    "18_semi_metals_zigzag_border_elements",
    "19_physical_properties_metals_lustre",
    "20_physical_properties_metals_conduction",
    "21_physical_properties_metals_malleability",
    "22_physical_properties_metals_ductility",
    "23_physical_properties_metals_melting_points",
    "24_liquid_elements_mercury_and_bromine",
    "25_density_comparison_metals_vs_non_metals",
    # 26 - 31
    "26_non_metals_physical_states_room_temp",
    "27_non_metals_dull_and_brittle_solids",
    "28_non_metals_electrical_insulators_exception_graphite",
    "29_carbon_allotropes_diamond_and_graphite",
    "30_semi_metals_semiconductor_properties",
    "31_silicon_in_modern_computer_technology",
    # 32 - 37
    "32_group_1_alkali_metals_properties",
    "33_group_1_alkali_metals_reactivity_trend",
    "34_group_2_alkaline_earth_metals",
    "35_group_17_halogens_properties",
    "36_group_18_noble_gases_inert_nature",
    "37_noble_gases_practical_applications",
    # 38 - 41
    "38_element_vs_compound_distinction",
    "39_interpreting_chemical_formulas_atom_ratios",
    "40_diatomic_non_metal_molecules",
    "41_gaseous_elements_at_room_temperature",
    # 42 - 45
    "42_mineral_ores_and_indigenous_metal_smelting",
    "43_abundance_of_elements_in_earth_crust",
    "44_abundance_of_elements_in_human_body",
    "45_transition_metals_overview",
    # 46 - 50
    "46_evaluating_element_data_cards",
    "47_predicting_element_properties_from_position",
    "48_misconceptions_element_names_vs_brand_names",
    "49_scientific_inquiry_classifying_mystery_element",
    "50_periodic_table_master_classification_challenge",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based integer and padded string aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["element_definition_and_symbols"] = arch_01_element_definition_pure_substance
DISPATCH_TABLE["metals_nonmetals_semimetals_classification"] = arch_16_metals_position_on_periodic_table
DISPATCH_TABLE["atomic_number_and_arrangement"] = arch_04_atomic_number_definition_protons
DISPATCH_TABLE["first_twenty_elements_identification"] = arch_09_first_twenty_elements_names_symbols_1_5
DISPATCH_TABLE["mendeleev_periodic_table_history"] = arch_03_periodic_table_mendeleev_history


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
    Main entry point for Grade 7 Natural Sciences: The Periodic Table of Elements Generator.
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
        q.setdefault("topic", "The Periodic Table of Elements")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
