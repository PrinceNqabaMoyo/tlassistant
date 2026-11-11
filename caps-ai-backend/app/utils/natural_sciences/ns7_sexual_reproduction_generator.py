"""Grade 7 Natural Sciences: Term 1 - Sexual Reproduction Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/03. Sexual reproduction.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_sexual_reproduction_archetypes_01_25 import (
    arch_01_flower_outer_structures_calyx_corolla,
    arch_02_flower_male_structures_stamen_anther_filament,
    arch_03_flower_female_structures_pistil_stigma_style_ovary,
    arch_04_distinguish_male_vs_female_floral_organs,
    arch_05_pollination_definition_self_vs_cross,
    arch_06_insect_pollination_adaptations_floral_traits,
    arch_07_bird_pollination_adaptations_sunbirds,
    arch_08_wind_pollination_adaptations_grasses,
    arch_09_water_pollination_adaptations_aquatic_plants,
    arch_10_pollinator_mutualism_and_agricultural_food_security,
    arch_11_pollen_tube_germination_down_style,
    arch_12_plant_fertilisation_male_gamete_ovule_fusion,
    arch_13_post_fertilisation_fate_ovary_to_fruit_ovule_to_seed,
    arch_14_seed_structure_testa_cotyledon_embryo,
    arch_15_seed_dispersal_importance_preventing_competition,
    arch_16_seed_dispersal_wind_mechanisms_wings_parachutes,
    arch_17_seed_dispersal_animal_mechanisms_fleshy_fruits,
    arch_18_seed_dispersal_animal_mechanisms_hooks_and_burs,
    arch_19_seed_dispersal_water_mechanisms_buoyant_husks,
    arch_20_seed_dispersal_explosive_mechanical_dehiscence,
    arch_21_seed_germination_requirements_water_oxygen_warmth,
    arch_22_investigation_growing_bean_seedlings,
    arch_23_sexual_vs_asexual_reproduction_in_plants,
    arch_24_angiosperm_life_cycle_chronological_sequence,
    arch_25_flower_dissection_morphology_diagram,
)
from .ns7_sexual_reproduction_archetypes_26_50 import (
    arch_26_purpose_of_human_reproduction_species_continuation,
    arch_27_puberty_definition_and_hormonal_trigger,
    arch_28_male_secondary_sexual_characteristics,
    arch_29_female_secondary_sexual_characteristics,
    arch_30_growth_spurt_curve_graph_interpretation,
    arch_31_emotional_and_psychological_changes_during_puberty,
    arch_32_male_reproductive_organs_testes_and_scrotum,
    arch_33_male_reproductive_organs_epididymis_and_vas_deferens,
    arch_34_male_reproductive_organs_accessory_glands_and_semen,
    arch_35_male_reproductive_organs_penis_and_urethra,
    arch_36_female_reproductive_organs_ovaries_and_ova,
    arch_37_female_reproductive_organs_fallopian_tubes_site_of_fertilisation,
    arch_38_female_reproductive_organs_uterus_and_endometrium,
    arch_39_female_reproductive_organs_cervix_and_vagina,
    arch_40_menstrual_cycle_four_phases_timeline,
    arch_41_human_fertilisation_sperm_egg_fusion_in_oviduct,
    arch_42_embryo_implantation_in_uterine_lining,
    arch_43_gestation_placenta_and_umbilical_cord_functions,
    arch_44_gestation_amniotic_sac_and_fluid_protection,
    arch_45_childbirth_stages_labour_dilation_and_delivery,
    arch_46_contraception_barrier_methods_condoms,
    arch_47_contraception_hormonal_and_permanent_methods,
    arch_48_sexually_transmitted_infections_pathogens_and_symptoms,
    arch_49_addressing_menstruation_and_pregnancy_myths,
    arch_50_synthetic_case_study_teenage_reproductive_health_counselling,
)

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_flower_outer_structures_calyx_corolla": arch_01_flower_outer_structures_calyx_corolla,
    "02_flower_male_structures_stamen_anther_filament": arch_02_flower_male_structures_stamen_anther_filament,
    "03_flower_female_structures_pistil_stigma_style_ovary": arch_03_flower_female_structures_pistil_stigma_style_ovary,
    "04_distinguish_male_vs_female_floral_organs": arch_04_distinguish_male_vs_female_floral_organs,
    "05_pollination_definition_self_vs_cross": arch_05_pollination_definition_self_vs_cross,
    "06_insect_pollination_adaptations_floral_traits": arch_06_insect_pollination_adaptations_floral_traits,
    "07_bird_pollination_adaptations_sunbirds": arch_07_bird_pollination_adaptations_sunbirds,
    "08_wind_pollination_adaptations_grasses": arch_08_wind_pollination_adaptations_grasses,
    "09_water_pollination_adaptations_aquatic_plants": arch_09_water_pollination_adaptations_aquatic_plants,
    "10_pollinator_mutualism_and_agricultural_food_security": arch_10_pollinator_mutualism_and_agricultural_food_security,
    "11_pollen_tube_germination_down_style": arch_11_pollen_tube_germination_down_style,
    "12_plant_fertilisation_male_gamete_ovule_fusion": arch_12_plant_fertilisation_male_gamete_ovule_fusion,
    "13_post_fertilisation_fate_ovary_to_fruit_ovule_to_seed": arch_13_post_fertilisation_fate_ovary_to_fruit_ovule_to_seed,
    "14_seed_structure_testa_cotyledon_embryo": arch_14_seed_structure_testa_cotyledon_embryo,
    "15_seed_dispersal_importance_preventing_competition": arch_15_seed_dispersal_importance_preventing_competition,
    "16_seed_dispersal_wind_mechanisms_wings_parachutes": arch_16_seed_dispersal_wind_mechanisms_wings_parachutes,
    "17_seed_dispersal_animal_mechanisms_fleshy_fruits": arch_17_seed_dispersal_animal_mechanisms_fleshy_fruits,
    "18_seed_dispersal_animal_mechanisms_hooks_and_burs": arch_18_seed_dispersal_animal_mechanisms_hooks_and_burs,
    "19_seed_dispersal_water_mechanisms_buoyant_husks": arch_19_seed_dispersal_water_mechanisms_buoyant_husks,
    "20_seed_dispersal_explosive_mechanical_dehiscence": arch_20_seed_dispersal_explosive_mechanical_dehiscence,
    "21_seed_germination_requirements_water_oxygen_warmth": arch_21_seed_germination_requirements_water_oxygen_warmth,
    "22_investigation_growing_bean_seedlings": arch_22_investigation_growing_bean_seedlings,
    "23_sexual_vs_asexual_reproduction_in_plants": arch_23_sexual_vs_asexual_reproduction_in_plants,
    "24_angiosperm_life_cycle_chronological_sequence": arch_24_angiosperm_life_cycle_chronological_sequence,
    "25_flower_dissection_morphology_diagram": arch_25_flower_dissection_morphology_diagram,
    "26_purpose_of_human_reproduction_species_continuation": arch_26_purpose_of_human_reproduction_species_continuation,
    "27_puberty_definition_and_hormonal_trigger": arch_27_puberty_definition_and_hormonal_trigger,
    "28_male_secondary_sexual_characteristics": arch_28_male_secondary_sexual_characteristics,
    "29_female_secondary_sexual_characteristics": arch_29_female_secondary_sexual_characteristics,
    "30_growth_spurt_curve_graph_interpretation": arch_30_growth_spurt_curve_graph_interpretation,
    "31_emotional_and_psychological_changes_during_puberty": arch_31_emotional_and_psychological_changes_during_puberty,
    "32_male_reproductive_organs_testes_and_scrotum": arch_32_male_reproductive_organs_testes_and_scrotum,
    "33_male_reproductive_organs_epididymis_and_vas_deferens": arch_33_male_reproductive_organs_epididymis_and_vas_deferens,
    "34_male_reproductive_organs_accessory_glands_and_semen": arch_34_male_reproductive_organs_accessory_glands_and_semen,
    "35_male_reproductive_organs_penis_and_urethra": arch_35_male_reproductive_organs_penis_and_urethra,
    "36_female_reproductive_organs_ovaries_and_ova": arch_36_female_reproductive_organs_ovaries_and_ova,
    "37_female_reproductive_organs_fallopian_tubes_site_of_fertilisation": arch_37_female_reproductive_organs_fallopian_tubes_site_of_fertilisation,
    "38_female_reproductive_organs_uterus_and_endometrium": arch_38_female_reproductive_organs_uterus_and_endometrium,
    "39_female_reproductive_organs_cervix_and_vagina": arch_39_female_reproductive_organs_cervix_and_vagina,
    "40_menstrual_cycle_four_phases_timeline": arch_40_menstrual_cycle_four_phases_timeline,
    "41_human_fertilisation_sperm_egg_fusion_in_oviduct": arch_41_human_fertilisation_sperm_egg_fusion_in_oviduct,
    "42_embryo_implantation_in_uterine_lining": arch_42_embryo_implantation_in_uterine_lining,
    "43_gestation_placenta_and_umbilical_cord_functions": arch_43_gestation_placenta_and_umbilical_cord_functions,
    "44_gestation_amniotic_sac_and_fluid_protection": arch_44_gestation_amniotic_sac_and_fluid_protection,
    "45_childbirth_stages_labour_dilation_and_delivery": arch_45_childbirth_stages_labour_dilation_and_delivery,
    "46_contraception_barrier_methods_condoms": arch_46_contraception_barrier_methods_condoms,
    "47_contraception_hormonal_and_permanent_methods": arch_47_contraception_hormonal_and_permanent_methods,
    "48_sexually_transmitted_infections_pathogens_and_symptoms": arch_48_sexually_transmitted_infections_pathogens_and_symptoms,
    "49_addressing_menstruation_and_pregnancy_myths": arch_49_addressing_menstruation_and_pregnancy_myths,
    "50_synthetic_case_study_teenage_reproductive_health_counselling": arch_50_synthetic_case_study_teenage_reproductive_health_counselling,
}

SUBSKILLS: List[str] = list(BUILDERS.keys())

LEGACY_MAP: Dict[str, str] = {
    "flower_anatomy_and_functions": "01_flower_outer_structures_calyx_corolla",
    "pollination_mechanisms_wind_vs_insect": "06_insect_pollination_adaptations_floral_traits",
    "fertilisation_process_ovule_to_seed": "12_plant_fertilisation_male_gamete_ovule_fusion",
    "fruit_and_seed_dispersal_strategies": "15_seed_dispersal_importance_preventing_competition",
    "sexual_vs_asexual_reproduction_comparison": "23_sexual_vs_asexual_reproduction_in_plants",
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
    """Generate deterministic questions for Grade 7 Natural Sciences: Sexual reproduction."""
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
