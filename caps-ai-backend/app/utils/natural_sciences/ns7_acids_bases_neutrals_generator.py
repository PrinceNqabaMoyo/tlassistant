"""Grade 7 Natural Sciences: Term 2 - Acids, Bases and Neutral Substances Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/03. Acids bases and neutral substances.md.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_acids_bases_neutrals_archetypes_01_25 import (
    arch_01_tongue_taste_buds_and_papillae,
    arch_02_four_primary_tastes_identification,
    arch_03_evolutionary_survival_taste_sour_bitter,
    arch_04_laboratory_safety_rule_no_tasting,
    arch_05_acid_definition_and_sensory_properties,
    arch_06_everyday_household_acids_examples,
    arch_07_laboratory_acids_identification_formulas,
    arch_08_corrosive_nature_of_strong_acids,
    arch_09_base_definition_and_sensory_properties,
    arch_10_alkali_definition_soluble_bases,
    arch_11_everyday_household_bases_examples,
    arch_12_laboratory_bases_identification_formulas,
    arch_13_caustic_nature_of_strong_bases,
    arch_14_neutral_substance_definition_properties,
    arch_15_red_litmus_paper_reaction_acid_base,
    arch_16_blue_litmus_paper_reaction_acid_base,
    arch_17_two_litmus_test_identifying_neutral,
    arch_18_interpreting_litmus_test_data_table,
    arch_19_plant_indicator_red_cabbage_preparation,
    arch_20_red_cabbage_indicator_colour_changes,
    arch_21_alternative_natural_indicators_turmeric_tea,
    arch_22_universal_indicator_concept_and_colours,
    arch_23_ph_scale_range_and_neutral_point,
    arch_24_ranking_substances_by_ph_scale,
    arch_25_strong_vs_weak_acids_ph_comparison,
)

from .ns7_acids_bases_neutrals_archetypes_26_50 import (
    arch_26_strong_vs_weak_bases_ph_comparison,
    arch_27_neutralisation_reaction_word_equation,
    arch_28_neutralisation_ph_change_curve,
    arch_29_antacids_relieving_stomach_hyperacidity,
    arch_30_treating_insect_stings_bee_vs_wasp,
    arch_31_agricultural_lime_treating_acid_soils,
    arch_32_acid_mine_drainage_neutralisation_slaked_lime,
    arch_33_toothpaste_preventing_dental_decay,
    arch_34_acid_rain_causes_emissions_so2_nox,
    arch_35_acid_rain_effects_ecosystems_and_stonework,
    arch_36_baking_powder_reaction_producing_co2,
    arch_37_acid_reaction_with_metals_hydrogen_gas,
    arch_38_acid_reaction_with_carbonates_co2_gas,
    arch_39_safety_diluting_acids_rule_acid_to_water,
    arch_40_first_aid_acid_and_base_spills,
    arch_41_neutralisation_experiment_indicator_colour_endpoint,
    arch_42_citrus_farming_fruit_acidity_ripening,
    arch_43_swimming_pool_water_ph_maintenance,
    arch_44_vinegar_as_descaling_agent_kettles,
    arch_45_rust_removal_with_phosphoric_acid,
    arch_46_comparing_cleaning_agents_acidic_vs_alkaline,
    arch_47_evaluating_experimental_reliability_indicators,
    arch_48_investigating_ph_of_common_beverages,
    arch_49_troubleshooting_indicator_test_anomalies,
    arch_50_comprehensive_acid_base_neutral_classification_matrix,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 04: Taste & Sensory Adaptation
    arch_01_tongue_taste_buds_and_papillae,
    arch_02_four_primary_tastes_identification,
    arch_03_evolutionary_survival_taste_sour_bitter,
    arch_04_laboratory_safety_rule_no_tasting,
    # 05 - 14: Properties of Acids & Bases
    arch_05_acid_definition_and_sensory_properties,
    arch_06_everyday_household_acids_examples,
    arch_07_laboratory_acids_identification_formulas,
    arch_08_corrosive_nature_of_strong_acids,
    arch_09_base_definition_and_sensory_properties,
    arch_10_alkali_definition_soluble_bases,
    arch_11_everyday_household_bases_examples,
    arch_12_laboratory_bases_identification_formulas,
    arch_13_caustic_nature_of_strong_bases,
    arch_14_neutral_substance_definition_properties,
    # 15 - 25: Litmus, Indicators & The pH Scale
    arch_15_red_litmus_paper_reaction_acid_base,
    arch_16_blue_litmus_paper_reaction_acid_base,
    arch_17_two_litmus_test_identifying_neutral,
    arch_18_interpreting_litmus_test_data_table,
    arch_19_plant_indicator_red_cabbage_preparation,
    arch_20_red_cabbage_indicator_colour_changes,
    arch_21_alternative_natural_indicators_turmeric_tea,
    arch_22_universal_indicator_concept_and_colours,
    arch_23_ph_scale_range_and_neutral_point,
    arch_24_ranking_substances_by_ph_scale,
    arch_25_strong_vs_weak_acids_ph_comparison,
    # 26 - 33: Neutralisation Reactions & Applications
    arch_26_strong_vs_weak_bases_ph_comparison,
    arch_27_neutralisation_reaction_word_equation,
    arch_28_neutralisation_ph_change_curve,
    arch_29_antacids_relieving_stomach_hyperacidity,
    arch_30_treating_insect_stings_bee_vs_wasp,
    arch_31_agricultural_lime_treating_acid_soils,
    arch_32_acid_mine_drainage_neutralisation_slaked_lime,
    arch_33_toothpaste_preventing_dental_decay,
    # 34 - 42: Environmental Acidity & Chemical Reactions
    arch_34_acid_rain_causes_emissions_so2_nox,
    arch_35_acid_rain_effects_ecosystems_and_stonework,
    arch_36_baking_powder_reaction_producing_co2,
    arch_37_acid_reaction_with_metals_hydrogen_gas,
    arch_38_acid_reaction_with_carbonates_co2_gas,
    arch_39_safety_diluting_acids_rule_acid_to_water,
    arch_40_first_aid_acid_and_base_spills,
    arch_41_neutralisation_experiment_indicator_colour_endpoint,
    arch_42_citrus_farming_fruit_acidity_ripening,
    # 43 - 50: Practical Cleaning & Real-World Acidity
    arch_43_swimming_pool_water_ph_maintenance,
    arch_44_vinegar_as_descaling_agent_kettles,
    arch_45_rust_removal_with_phosphoric_acid,
    arch_46_comparing_cleaning_agents_acidic_vs_alkaline,
    arch_47_evaluating_experimental_reliability_indicators,
    arch_48_investigating_ph_of_common_beverages,
    arch_49_troubleshooting_indicator_test_anomalies,
    arch_50_comprehensive_acid_base_neutral_classification_matrix,
]

SUBSKILLS: List[str] = [
    # 01 - 04
    "01_tongue_taste_buds_and_papillae",
    "02_four_primary_tastes_identification",
    "03_evolutionary_survival_taste_sour_bitter",
    "04_laboratory_safety_rule_no_tasting",
    # 05 - 14
    "05_acid_definition_and_sensory_properties",
    "06_everyday_household_acids_examples",
    "07_laboratory_acids_identification_formulas",
    "08_corrosive_nature_of_strong_acids",
    "09_base_definition_and_sensory_properties",
    "10_alkali_definition_soluble_bases",
    "11_everyday_household_bases_examples",
    "12_laboratory_bases_identification_formulas",
    "13_caustic_nature_of_strong_bases",
    "14_neutral_substance_definition_properties",
    # 15 - 25
    "15_red_litmus_paper_reaction_acid_base",
    "16_blue_litmus_paper_reaction_acid_base",
    "17_two_litmus_test_identifying_neutral",
    "18_interpreting_litmus_test_data_table",
    "19_plant_indicator_red_cabbage_preparation",
    "20_red_cabbage_indicator_colour_changes",
    "21_alternative_natural_indicators_turmeric_tea",
    "22_universal_indicator_concept_and_colours",
    "23_ph_scale_range_and_neutral_point",
    "24_ranking_substances_by_ph_scale",
    "25_strong_vs_weak_acids_ph_comparison",
    # 26 - 33
    "26_strong_vs_weak_bases_ph_comparison",
    "27_neutralisation_reaction_word_equation",
    "28_neutralisation_ph_change_curve",
    "29_antacids_relieving_stomach_hyperacidity",
    "30_treating_insect_stings_bee_vs_wasp",
    "31_agricultural_lime_treating_acid_soils",
    "32_acid_mine_drainage_neutralisation_slaked_lime",
    "33_toothpaste_preventing_dental_decay",
    # 34 - 42
    "34_acid_rain_causes_emissions_so2_nox",
    "35_acid_rain_effects_ecosystems_and_stonework",
    "36_baking_powder_reaction_producing_co2",
    "37_acid_reaction_with_metals_hydrogen_gas",
    "38_acid_reaction_with_carbonates_co2_gas",
    "39_safety_diluting_acids_rule_acid_to_water",
    "40_first_aid_acid_and_base_spills",
    "41_neutralisation_experiment_indicator_colour_endpoint",
    "42_citrus_farming_fruit_acidity_ripening",
    # 43 - 50
    "43_swimming_pool_water_ph_maintenance",
    "44_vinegar_as_descaling_agent_kettles",
    "45_rust_removal_with_phosphoric_acid",
    "46_comparing_cleaning_agents_acidic_vs_alkaline",
    "47_evaluating_experimental_reliability_indicators",
    "48_investigating_ph_of_common_beverages",
    "49_troubleshooting_indicator_test_anomalies",
    "50_comprehensive_acid_base_neutral_classification_matrix",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based integer and padded string aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["taste_acids_bases"] = arch_02_four_primary_tastes_identification
DISPATCH_TABLE["properties_acids"] = arch_05_acid_definition_and_sensory_properties
DISPATCH_TABLE["properties_bases"] = arch_09_base_definition_and_sensory_properties
DISPATCH_TABLE["acid_base_indicators"] = arch_15_red_litmus_paper_reaction_acid_base
DISPATCH_TABLE["neutralisation"] = arch_27_neutralisation_reaction_word_equation


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
    Main entry point for Grade 7 Natural Sciences: Acids, Bases and Neutral Substances Generator.
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
        q.setdefault("topic", "Acids bases and neutral substances")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
