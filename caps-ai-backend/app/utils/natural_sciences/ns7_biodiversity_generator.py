"""Grade 7 Natural Sciences: Term 1 - Biodiversity Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/02. Biodiversity.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_biodiversity_archetypes_01_25 import (
    arch_01_biodiversity_definition_and_three_levels,
    arch_02_south_african_biodiversity_hotspots_cape_floral,
    arch_03_south_african_biodiversity_hotspots_succulent_karoo,
    arch_04_south_african_biodiversity_hotspots_maputaland_albany,
    arch_05_threats_to_biodiversity_habitat_destruction,
    arch_06_threats_to_biodiversity_invasive_alien_species,
    arch_07_threats_to_biodiversity_poaching_and_overexploitation,
    arch_08_threats_to_biodiversity_pollution_and_climate_change,
    arch_09_iucn_red_list_conservation_status_categories,
    arch_10_indigenous_vs_exotic_vs_endemic_species,
    arch_11_importance_of_classification_in_science,
    arch_12_historical_classification_aristotle_limitations,
    arch_13_historical_classification_carolus_linnaeus_contribution,
    arch_14_historical_classification_ernst_haeckel_protista,
    arch_15_taxonomic_hierarchy_ranks_domain_to_species,
    arch_16_taxonomic_hierarchy_inclusive_vs_specific_relationships,
    arch_17_binomial_nomenclature_naming_rules,
    arch_18_binomial_nomenclature_common_vs_scientific_names,
    arch_19_biological_species_concept_interbreeding,
    arch_20_prokaryote_vs_eukaryote_cellular_differences,
    arch_21_five_kingdom_overview_diagnostic_criteria,
    arch_22_kingdom_monera_bacteria_characteristics,
    arch_23_kingdom_protista_single_celled_eukaryotes,
    arch_24_kingdom_fungi_absorptive_heterotrophs,
    arch_25_kingdom_plantae_autotrophic_chloroplasts,
)
from .ns7_biodiversity_archetypes_26_50 import (
    arch_26_kingdom_animalia_heterotrophic_multicellular,
    arch_27_invertebrates_vs_vertebrates_distinction,
    arch_28_invertebrate_phylum_porifera_sponges,
    arch_29_invertebrate_phylum_cnidaria_jellyfish_corals,
    arch_30_invertebrate_phylum_platyhelminthes_flatworms,
    arch_31_invertebrate_phylum_annelida_segmented_worms,
    arch_32_invertebrate_phylum_mollusca_soft_bodied,
    arch_33_invertebrate_phylum_echinodermata_spiny_skinned,
    arch_34_invertebrate_phylum_arthropoda_general_traits,
    arch_35_arthropod_class_insecta_diagnostic_features,
    arch_36_arthropod_class_arachnida_spiders_scorpions,
    arch_37_arthropod_class_crustacea_crabs_prawns,
    arch_38_arthropod_class_myriapoda_centipedes_millipedes,
    arch_39_compare_four_arthropod_classes_matrix,
    arch_40_vertebrate_class_pisces_fish_characteristics,
    arch_41_vertebrate_class_amphibia_frogs_metamorphosis,
    arch_42_vertebrate_class_reptilia_scaly_skin_amniotic_egg,
    arch_43_vertebrate_class_aves_birds_flight_adaptations,
    arch_44_vertebrate_class_mammalia_hair_and_mammary_glands,
    arch_45_ectothermic_vs_endothermic_vertebrates,
    arch_46_vertebrate_egg_adaptations_jelly_vs_leathery_vs_calcareous,
    arch_47_dichotomous_key_navigation_step_by_step,
    arch_48_dichotomous_key_construction_from_traits,
    arch_49_dichotomous_key_arthropod_identification,
    arch_50_synthetic_biodiversity_case_study_ecosystem_stability,
)

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_biodiversity_definition_and_three_levels": arch_01_biodiversity_definition_and_three_levels,
    "02_south_african_biodiversity_hotspots_cape_floral": arch_02_south_african_biodiversity_hotspots_cape_floral,
    "03_south_african_biodiversity_hotspots_succulent_karoo": arch_03_south_african_biodiversity_hotspots_succulent_karoo,
    "04_south_african_biodiversity_hotspots_maputaland_albany": arch_04_south_african_biodiversity_hotspots_maputaland_albany,
    "05_threats_to_biodiversity_habitat_destruction": arch_05_threats_to_biodiversity_habitat_destruction,
    "06_threats_to_biodiversity_invasive_alien_species": arch_06_threats_to_biodiversity_invasive_alien_species,
    "07_threats_to_biodiversity_poaching_and_overexploitation": arch_07_threats_to_biodiversity_poaching_and_overexploitation,
    "08_threats_to_biodiversity_pollution_and_climate_change": arch_08_threats_to_biodiversity_pollution_and_climate_change,
    "09_iucn_red_list_conservation_status_categories": arch_09_iucn_red_list_conservation_status_categories,
    "10_indigenous_vs_exotic_vs_endemic_species": arch_10_indigenous_vs_exotic_vs_endemic_species,
    "11_importance_of_classification_in_science": arch_11_importance_of_classification_in_science,
    "12_historical_classification_aristotle_limitations": arch_12_historical_classification_aristotle_limitations,
    "13_historical_classification_carolus_linnaeus_contribution": arch_13_historical_classification_carolus_linnaeus_contribution,
    "14_historical_classification_ernst_haeckel_protista": arch_14_historical_classification_ernst_haeckel_protista,
    "15_taxonomic_hierarchy_ranks_domain_to_species": arch_15_taxonomic_hierarchy_ranks_domain_to_species,
    "16_taxonomic_hierarchy_inclusive_vs_specific_relationships": arch_16_taxonomic_hierarchy_inclusive_vs_specific_relationships,
    "17_binomial_nomenclature_naming_rules": arch_17_binomial_nomenclature_naming_rules,
    "18_binomial_nomenclature_common_vs_scientific_names": arch_18_binomial_nomenclature_common_vs_scientific_names,
    "19_biological_species_concept_interbreeding": arch_19_biological_species_concept_interbreeding,
    "20_prokaryote_vs_eukaryote_cellular_differences": arch_20_prokaryote_vs_eukaryote_cellular_differences,
    "21_five_kingdom_overview_diagnostic_criteria": arch_21_five_kingdom_overview_diagnostic_criteria,
    "22_kingdom_monera_bacteria_characteristics": arch_22_kingdom_monera_bacteria_characteristics,
    "23_kingdom_protista_single_celled_eukaryotes": arch_23_kingdom_protista_single_celled_eukaryotes,
    "24_kingdom_fungi_absorptive_heterotrophs": arch_24_kingdom_fungi_absorptive_heterotrophs,
    "25_kingdom_plantae_autotrophic_chloroplasts": arch_25_kingdom_plantae_autotrophic_chloroplasts,
    "26_kingdom_animalia_heterotrophic_multicellular": arch_26_kingdom_animalia_heterotrophic_multicellular,
    "27_invertebrates_vs_vertebrates_distinction": arch_27_invertebrates_vs_vertebrates_distinction,
    "28_invertebrate_phylum_porifera_sponges": arch_28_invertebrate_phylum_porifera_sponges,
    "29_invertebrate_phylum_cnidaria_jellyfish_corals": arch_29_invertebrate_phylum_cnidaria_jellyfish_corals,
    "30_invertebrate_phylum_platyhelminthes_flatworms": arch_30_invertebrate_phylum_platyhelminthes_flatworms,
    "31_invertebrate_phylum_annelida_segmented_worms": arch_31_invertebrate_phylum_annelida_segmented_worms,
    "32_invertebrate_phylum_mollusca_soft_bodied": arch_32_invertebrate_phylum_mollusca_soft_bodied,
    "33_invertebrate_phylum_echinodermata_spiny_skinned": arch_33_invertebrate_phylum_echinodermata_spiny_skinned,
    "34_invertebrate_phylum_arthropoda_general_traits": arch_34_invertebrate_phylum_arthropoda_general_traits,
    "35_arthropod_class_insecta_diagnostic_features": arch_35_arthropod_class_insecta_diagnostic_features,
    "36_arthropod_class_arachnida_spiders_scorpions": arch_36_arthropod_class_arachnida_spiders_scorpions,
    "37_arthropod_class_crustacea_crabs_prawns": arch_37_arthropod_class_crustacea_crabs_prawns,
    "38_arthropod_class_myriapoda_centipedes_millipedes": arch_38_arthropod_class_myriapoda_centipedes_millipedes,
    "39_compare_four_arthropod_classes_matrix": arch_39_compare_four_arthropod_classes_matrix,
    "40_vertebrate_class_pisces_fish_characteristics": arch_40_vertebrate_class_pisces_fish_characteristics,
    "41_vertebrate_class_amphibia_frogs_metamorphosis": arch_41_vertebrate_class_amphibia_frogs_metamorphosis,
    "42_vertebrate_class_reptilia_scaly_skin_amniotic_egg": arch_42_vertebrate_class_reptilia_scaly_skin_amniotic_egg,
    "43_vertebrate_class_aves_birds_flight_adaptations": arch_43_vertebrate_class_aves_birds_flight_adaptations,
    "44_vertebrate_class_mammalia_hair_and_mammary_glands": arch_44_vertebrate_class_mammalia_hair_and_mammary_glands,
    "45_ectothermic_vs_endothermic_vertebrates": arch_45_ectothermic_vs_endothermic_vertebrates,
    "46_vertebrate_egg_adaptations_jelly_vs_leathery_vs_calcareous": arch_46_vertebrate_egg_adaptations_jelly_vs_leathery_vs_calcareous,
    "47_dichotomous_key_navigation_step_by_step": arch_47_dichotomous_key_navigation_step_by_step,
    "48_dichotomous_key_construction_from_traits": arch_48_dichotomous_key_construction_from_traits,
    "49_dichotomous_key_arthropod_identification": arch_49_dichotomous_key_arthropod_identification,
    "50_synthetic_biodiversity_case_study_ecosystem_stability": arch_50_synthetic_biodiversity_case_study_ecosystem_stability,
}

SUBSKILLS: List[str] = list(BUILDERS.keys())

LEGACY_MAP: Dict[str, str] = {
    "biodiversity_definition_and_importance": "01_biodiversity_definition_and_three_levels",
    "five_kingdom_classification_system": "21_five_kingdom_overview_diagnostic_criteria",
    "vertebrates_vs_invertebrates_classes": "27_invertebrates_vs_vertebrates_distinction",
    "binomial_nomenclature_naming": "17_binomial_nomenclature_naming_rules",
    "dichotomous_keys_identification": "47_dichotomous_key_navigation_step_by_step",
}


def _resolve_subskill(subskill: Optional[str]) -> str:
    if not subskill:
        return random.choice(SUBSKILLS)
    s = subskill.strip().lower()
    if s in BUILDERS:
        return s
    if s in LEGACY_MAP:
        return LEGACY_MAP[s]
    for k in SUBSKILLS:
        if k.startswith(s) or s in k:
            return k
    return SUBSKILLS[0]


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate deterministic questions for Grade 7 Natural Sciences: Biodiversity."""
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = rng.randint(1000, 999999) if count > 1 else seed
        sub_rng = random.Random(sub_seed) if sub_seed is not None else rng
        if subskill:
            chosen = _resolve_subskill(subskill)
        else:
            chosen = SUBSKILLS[i % len(SUBSKILLS)]
        builder = BUILDERS[chosen]
        q = builder(sub_rng)
        questions.append(q)

    return questions
