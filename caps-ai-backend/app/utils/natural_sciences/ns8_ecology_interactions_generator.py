"""Natural Sciences Grade 8 Term 1: Interactions and Interdependence within the Environment Generator.

Strictly grounded in curriculum_docs_auto/NaturalSciences_Gr8/Term 1/02. Interactions and interdependence within the environment.md.
Covers:
- ecological_levels_organisation: Individual -> Population -> Community -> Ecosystem -> Biosphere.
- food_webs_and_trophic_levels: Producers, primary/secondary/tertiary consumers, decomposers, energy flow arrows.
- ecological_pyramid_energy_loss: Trophic energy transfer (~10% rule), pyramid of numbers and biomass.
- abiotic_biotic_ecosystem_balance: Interactions between non-living (abiotic) and living (biotic) factors, carrying capacity.
- human_impact_and_adaptation: Conservation, alien invasive species, poaching, structural and behavioral adaptations in SA biomes.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


SUBSKILLS = [
    "ecological_levels_organisation",
    "food_webs_and_trophic_levels",
    "ecological_pyramid_energy_loss",
    "abiotic_biotic_ecosystem_balance",
    "human_impact_and_adaptation",
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _build_ecological_levels(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    levels = [
        {
            "term": "Population",
            "example": "a group of African elephants living and interbreeding in the Kruger National Park at the same time",
            "definition": "A group of individuals of the same species living in a specific geographical area and interbreeding",
            "distractors": [
                "All the different animal and plant species living together in an area",
                "A community interacting with all non-living physical factors",
                "The entire global zone of life on Earth spanning atmosphere and oceans"
            ]
        },
        {
            "term": "Community",
            "example": "all the zebras, acacia trees, lions, vultures, and grass species coexisting in the Hluhluwe-iMfolozi Park",
            "definition": "All the different populations of different species interacting together in a defined habitat",
            "distractors": [
                "A single species of organism living in isolation",
                "The non-living climatic components like rainfall and temperature",
                "A laboratory specimen grown on an agar plate"
            ]
        },
        {
            "term": "Ecosystem",
            "example": "a freshwater wetland including frogs, reeds, water lilies, dragonfly larvae, dissolved oxygen, water, and sunlight",
            "definition": "A biological community of interacting living organisms together with their non-living physical environment",
            "distractors": [
                "A collection of organisms belonging to only one kingdom",
                "Only the abiotic rock minerals present in the soil",
                "A group of organisms of the same species born in the same season"
            ]
        }
    ]
    lvl = rng.choice(levels)
    prompt = (
        f"In ecological field studies, scientists classify biological systems into hierarchal levels.\n\n"
        f"Consider the following example:\n"
        f"*{lvl['example']}*\n\n"
        f"Which ecological level of organisation does this group represent?"
    )
    correct_ans = f"{lvl['term']} ({lvl['definition']})"
    options = [correct_ans] + [f"{d} (Incorrect level)" for d in lvl["distractors"]]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand the hierarchy of ecological organisation:\n"
        f"Individual -> Population (same species) -> Community (different species) -> Ecosystem (community + abiotic factors) -> Biosphere (all ecosystems).\n\n"
        f"Step 2: Classify the scenario:\n"
        f"The description describes {lvl['example']}. This corresponds to a **{lvl['term']}** because it represents {lvl['definition']}."
    )
    return {
        "id": _make_id("ns8_eco_levels", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "ecological_levels_organisation",
        "question_family_id": "ecological_levels_organisation",
        "curriculum_reference": "Natural Sciences Gr8 Term 1 > Interactions in Environment > Levels of organisation",
        "hints": {
            "tier_1": "Determine whether the example involves one species, multiple living species, or living organisms combined with abiotic factors.",
            "tier_2": "Population = one species; Community = multiple species; Ecosystem = community + physical surroundings.",
            "tier_3": f"The correct classification is {lvl['term']}."
        },
        "misconception_tags": ["confuses_population_with_community"]
    }


def _build_food_webs_trophic(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    habitats = [
        ("Savannah Grassland", "Acacia grass -> Impala -> Cheetah -> Lion / Vulture", "Impala", "Herbivore / Primary consumer"),
        ("Fynbos Shrubland", "Protea nectar -> Cape Sugarbird -> Boomslang -> Secretary Bird", "Boomslang", "Carnivore / Secondary consumer"),
        ("Freshwater Pond", "Phytoplankton -> Water flea (Daphnia) -> Tilapia fish -> African Fish Eagle", "Phytoplankton", "Autotroph / Producer")
    ]
    biome, chain, target_org, target_role = rng.choice(habitats)
    prompt = (
        f"Examine the following feeding relationship in a South African {biome} ecosystem:\n\n"
        f"$$\\text{{{chain}}}$$\n\n"
        f"1. What do the arrows in a food chain or food web represent?\n"
        f"2. Identify the trophic role and feeding level of the **{target_org}** in this chain.\n"
        f"3. Explain what would happen to the ecosystem if decomposers (like soil bacteria and fungi) were completely removed."
    )
    sample_answer = (
        "1. The arrows represent the direction of energy flow (transfer of energy from organism eaten to the consumer).\n"
        f"2. {target_org}: {target_role}.\n"
        "3. Without decomposers, dead plant and animal matter would accumulate without rotting, trapped nutrients (nitrogen, phosphorus, carbon) "
        "would not be recycled back into the soil, and plants would starve of essential mineral nutrients, collapsing the food web."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Direction of arrows: Transfer of energy / nutrients from prey/food to predator/consumer [1 mark].\n"
        f"2. Trophic identification: {target_org} is a {target_role} [1 mark].\n"
        "3. Role of decomposers: Breakdown of organic matter and recycling of mineral nutrients into the soil [1 mark].\n"
        "4. Ecosystem collapse consequence: Soil depletion and starvation of autotrophic producers [1 mark]."
    )
    return {
        "id": _make_id("ns8_food_web", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "food_webs_and_trophic_levels",
        "question_family_id": "food_webs_and_trophic_levels",
        "curriculum_reference": "Natural Sciences Gr8 Term 1 > Interactions in Environment > Food chains and food webs",
        "hints": {
            "tier_1": "Remember: The arrow points INTO the mouth of the consumer that gains the energy.",
            "tier_2": "Producers make food via sunlight; herbivores eat plants; carnivores eat animals; decomposers recycle nutrients.",
            "tier_3": f"{target_org} is a {target_role}."
        },
        "misconception_tags": ["arrow_direction_misconception", "decomposers_not_needed_misconception"]
    }


def _build_ecological_pyramid_energy(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    producer_energy = rng.choice([10000, 20000, 50000])
    herbivore_energy = producer_energy // 10
    carnivore_energy = herbivore_energy // 10
    top_predator_energy = carnivore_energy // 10
    prompt = (
        f"In an ecological pyramid of energy, the grasses in a nature reserve trap and convert solar radiation into "
        f"**{producer_energy:,} kJ** of chemical potential energy.\n\n"
        f"According to ecological energy transfer principles (the 10% rule):\n"
        f"1. Calculate how much energy is available to the primary consumers (herbivores).\n"
        f"2. Calculate how much energy reaches the tertiary consumers (apex predators).\n"
        f"3. Explain why approximately 90% of energy is lost between each consecutive trophic level."
    )
    sample_answer = (
        f"1. Primary consumers: {producer_energy:,} kJ x 10% = {herbivore_energy:,} kJ\n"
        f"2. Tertiary consumers: {top_predator_energy:,} kJ (after 3 trophic transfers: {producer_energy:,} -> {herbivore_energy:,} -> {carnivore_energy:,} -> {top_predator_energy:,} kJ)\n"
        "3. Energy is lost because organisms use energy for cellular respiration, movement, reproduction, and metabolic heat, "
        "and some energy is lost in undigested waste matter (feces and urine)."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        f"1. Primary consumer energy: {herbivore_energy:,} kJ [1 mark].\n"
        f"2. Tertiary consumer energy: {top_predator_energy:,} kJ [1 mark].\n"
        "3. Reason for 90% loss: Energy expended in metabolic life processes (cellular respiration, locomotion, heat loss) [1 mark].\n"
        "4. Ingestion inefficiency: Energy locked in unconsumed or undigested matter/excretion [1 mark]."
    )
    return {
        "id": _make_id("ns8_eco_pyramid", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "ecological_pyramid_energy_loss",
        "question_family_id": "ecological_pyramid_energy_loss",
        "curriculum_reference": "Natural Sciences Gr8 Term 1 > Interactions in Environment > Pyramids of biomass and energy",
        "hints": {
            "tier_1": "Apply the 10% rule: each trophic level receives only 10% of the energy from the level below it.",
            "tier_2": "Calculate 10% of the previous value for each step upwards.",
            "tier_3": f"Primary = {herbivore_energy:,} kJ; Tertiary = {top_predator_energy:,} kJ."
        },
        "misconception_tags": ["energy_created_in_pyramid_misconception"]
    }


def _build_abiotic_biotic_balance(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    factors = [
        ("Prolonged severe drought with zero rainfall for 18 months", "Abiotic factor (water shortage)", "Carrying capacity decreases dramatically, vegetation wilts, herbivores starve or migrate, causing predator starvation"),
        ("An outbreak of Anthrax bacterium in a buffalo herd", "Biotic factor (pathogen infection)", "Buffalo population density declines sharply, reducing food for apex carnivores and increasing scavenger populations"),
        ("Wildfire ignited by dry lightning burning through grassland", "Abiotic factor (thermal disturbance)", "Top layer vegetation burns, releasing soil nutrients in ash and stimulating fire-adapted seed germination")
    ]
    event, factor_type, ecological_impact = rng.choice(factors)
    prompt = (
        f"Ecosystems remain balanced through continuous interactions between living organisms and physical conditions.\n\n"
        f"Consider this scenario:\n"
        f"*{event}*\n\n"
        f"Classify this disturbance as an **abiotic** or **biotic** factor, and explain its immediate impact on the carrying capacity of the ecosystem."
    )
    sample_answer = (
        f"1. Classification: {factor_type}.\n"
        f"2. Impact on ecosystem: {ecological_impact}."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        f"1. Classification: Correctly identified as {factor_type} [1 mark].\n"
        f"2. Carrying capacity explanation: Explaining how the limiting resource impacts population size and reproductive survival [2 marks]."
    )
    return {
        "id": _make_id("ns8_abio_bio", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "abiotic_biotic_ecosystem_balance",
        "question_family_id": "abiotic_biotic_ecosystem_balance",
        "curriculum_reference": "Natural Sciences Gr8 Term 1 > Interactions in Environment > Biotic and abiotic factors",
        "hints": {
            "tier_1": "Bio- means living (organisms, pathogens, plants). A-bio- means non-living physical (rain, soil, fire, heat).",
            "tier_2": "Determine if the cause originated from a living organism or physical environmental factor.",
            "tier_3": f"It is an {factor_type}."
        },
        "misconception_tags": ["confuses_abiotic_with_biotic"]
    }


def _build_human_impact_adaptation(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    cases = [
        {
            "issue": "Invasion of Black Wattle and Eucalyptus trees in the Western Cape water catchment areas",
            "threat": "Depleting groundwater reservoirs and outcompeting native Fynbos floral biodiversity",
            "action": "Biological and mechanical clearing (Working for Water program) to restore native vegetation",
            "category": "Invasive alien vegetation"
        },
        {
            "issue": "Illegal poaching of White and Black Rhinoceros for their keratin horns",
            "threat": "Severe population decline leading towards species extinction and disrupting herbivory balance",
            "action": "Dehorning initiatives, satellite tracking collars, armed ranger patrols, and community stewardship",
            "category": "Poaching and biodiversity loss"
        },
        {
            "issue": "Agricultural runoff carrying synthetic nitrogen fertilizers into a river system",
            "threat": "Eutrophication: massive algal blooms that block sunlight and deplete dissolved oxygen when rotting, suffocating aquatic life",
            "action": "Riparian buffer zones of wetland reeds to filter runoff and adopting sustainable organic farming",
            "category": "Water pollution and eutrophication"
        }
    ]
    c = rng.choice(cases)
    prompt = (
        f"Human activities frequently disrupt the natural equilibrium of South African biomes.\n\n"
        f"Case study: **{c['issue']}**\n\n"
        f"1. Name the ecological category of this environmental challenge.\n"
        f"2. Explain the ecological damage caused to local species and habitats.\n"
        f"3. Propose two practical conservation measures used in South Africa to mitigate this threat."
    )
    sample_answer = (
        f"1. Category: {c['category']}.\n"
        f"2. Ecological damage: {c['threat']}.\n"
        f"3. Conservation measures: {c['action']}."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        f"1. Environmental category: {c['category']} [1 mark].\n"
        f"2. Ecological consequence: Explains specific impact on biodiversity/habitat balance ({c['threat']}) [2 marks].\n"
        f"3. Mitigation strategy: Proposes valid conservation or rehabilitation action ({c['action']}) [1 mark]."
    )
    return {
        "id": _make_id("ns8_human_impact", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "human_impact_and_adaptation",
        "question_family_id": "human_impact_and_adaptation",
        "curriculum_reference": "Natural Sciences Gr8 Term 1 > Interactions in Environment > Human influence on ecosystems",
        "hints": {
            "tier_1": "Focus on the specific threat named in the case study and its downstream effects on biodiversity.",
            "tier_2": "Consider how South African conservation programs tackle alien plants, poaching, or pollution.",
            "tier_3": f"Category is {c['category']}."
        },
        "misconception_tags": ["alien_species_always_harmless_misconception"]
    }


def generate(archetype: Optional[str] = None, seed: Optional[int] = None, count: int = 1, **kwargs) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    results = []
    for idx in range(count):
        target = archetype or rng.choice(SUBSKILLS)
        if target == "ecological_levels_organisation":
            item = _build_ecological_levels(rng, seed, idx)
        elif target == "food_webs_and_trophic_levels":
            item = _build_food_webs_trophic(rng, seed, idx)
        elif target == "ecological_pyramid_energy_loss":
            item = _build_ecological_pyramid_energy(rng, seed, idx)
        elif target == "abiotic_biotic_ecosystem_balance":
            item = _build_abiotic_biotic_balance(rng, seed, idx)
        elif target == "human_impact_and_adaptation":
            item = _build_human_impact_adaptation(rng, seed, idx)
        else:
            item = _build_ecological_levels(rng, seed, idx)
        results.append(item)
    return results


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)
