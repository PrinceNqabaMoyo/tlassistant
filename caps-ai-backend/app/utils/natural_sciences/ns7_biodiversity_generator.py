"""Grade 7 Natural Sciences: Term 1 - Biodiversity Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/02. Biodiversity.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "biodiversity_definition_and_importance",
    "five_kingdom_classification_system",
    "vertebrates_vs_invertebrates_classes",
    "binomial_nomenclature_naming",
    "dichotomous_keys_identification"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 1/02. Biodiversity.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_biodiversity_definition_and_importance(rng: random.Random) -> Dict[str, Any]:
    regions = [
        ("the Cape Floral Kingdom (Fynbos)", "over 9 000 plant species, of which approximately 69% are endemic and found nowhere else on Earth", "botanical hotspot"),
        ("the Succulent Karoo biome", "the world's richest succulent desert flora with high endemism adapted to arid conditions", "succulent biodiversity hotspot"),
        ("the iSimangaliso Wetland Park", "diverse coastal marine, estuarine, and freshwater ecosystems supporting loggerhead turtles and coelacanths", "marine and wetland biodiversity hotspot")
    ]
    region, fact, bio_type = rng.choice(regions)
    prompt = (
        f"In South Africa, {region} is internationally recognized for having {fact}.\n\n"
        f"What does the term **biodiversity** mean, and why is this region of global scientific importance?"
    )
    correct_opt = "Biodiversity is the variety of all living organisms, species, and ecosystems in an area, maintaining ecosystem stability."
    options = [
        correct_opt,
        "Biodiversity refers only to the number of non-living mineral deposits found in national parks.",
        "Biodiversity means that all animals and plants in the region belong to one single identical species.",
        "Biodiversity is the chemical process of generating artificial fertilisers in industrial laboratories."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Scientific definition from Curriculum Chapter 10:\n"
        f"Biodiversity (biological diversity) encompasses the variety of all forms of life on Earth, including diversity "
        f"within species (genetic diversity), between species, and across ecosystems.\n\n"
        f"Step 2: Connect to South African hotspot:\n"
        f"{region} is an irreplaceable {bio_type} whose diverse species maintain vital ecological services."
    )
    return {
        "id": f"ns7_bio_div_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "biodiversity_definition_and_importance",
        "question_family_id": "biodiversity_definition_and_importance",
        "hints": {
            "tier_1": "Think about 'Bio' (life) + 'diversity' (variety).",
            "tier_2": "Biodiversity includes all species, their genetics, and their natural habitats.",
            "tier_3": "It is the variety of all living organisms and ecosystems in an area."
        },
        "misconception_tags": ["biodiversity_monoculture_confusion"]
    }

def _build_five_kingdom_classification_system(rng: random.Random) -> Dict[str, Any]:
    kingdoms = [
        ("Microscopic single-celled organisms lacking a true membrane-bound nucleus (prokaryotic, e.g. Escherichia coli)", "Monera (Bacteria)"),
        ("Single-celled or simple multicellular eukaryotic organisms that do not fit into plants, animals, or fungi (e.g. Amoeba, Euglena, Algae)", "Protista"),
        ("Eukaryotic heterotrophic organisms with chitinous cell walls that absorb dissolved nutrients via saprophytic decomposition (e.g. Mushrooms, bread mould, yeast)", "Fungi"),
        ("Multicellular autotrophic organisms containing cellulose cell walls and chlorophyll to synthesise food via photosynthesis", "Plantae"),
        ("Multicellular heterotrophic organisms without cell walls that ingest food and typically possess sensory organs and locomotion", "Animalia")
    ]
    desc, kingdom = rng.choice(kingdoms)
    prompt = (
        f"In Robert Whittaker's five-kingdom classification system, which kingdom is defined by:\n"
        f"'{desc}'?"
    )
    correct_opt = kingdom
    distractors = [k[1] for k in kingdoms if k[1] != kingdom]
    options = [correct_opt] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Review 5-kingdom characteristics:\n"
        f"- Monera: Prokaryotes without nucleus.\n"
        f"- Protista: Simple single-celled eukaryotes.\n"
        f"- Fungi: Heterotrophs absorbing nutrients, chitin walls.\n"
        f"- Plantae: Autotrophic photosynthesizers, cellulose walls.\n"
        f"- Animalia: Multicellular heterotrophs, no cell walls.\n\n"
        f"Conclusion: '{desc}' defines {kingdom}."
    )
    return {
        "id": f"ns7_bio_5king_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "five_kingdom_classification_system",
        "question_family_id": "five_kingdom_classification_system",
        "hints": {
            "tier_1": "Check whether cells have a nucleus and whether the organism makes its own food or absorbs it.",
            "tier_2": "Recall the 5 kingdoms: Monera, Protista, Fungi, Plantae, Animalia.",
            "tier_3": f"The kingdom matching these characteristics is {kingdom}."
        },
        "misconception_tags": ["fungi_plantae_confusion", "prokaryote_eukaryote_confusion"]
    }

def _build_vertebrates_vs_invertebrates(rng: random.Random) -> Dict[str, Any]:
    animals = [
        ("Chacma baboon", "Vertebrate (Mammal)", "has an internal bony vertebral column/backbone, fur, and nurses young with milk"),
        ("African rock python", "Vertebrate (Reptile)", "has an internal bony backbone, dry scaly skin, and lays shelled amniotic eggs"),
        ("Emperor scorpion", "Invertebrate (Arthropod)", "lacks an internal backbone and possesses an external chitinous exoskeleton with jointed appendages"),
        ("African giant land snail", "Invertebrate (Mollusc)", "lacks a backbone and possesses a soft unsegmented body enclosed in a calcium carbonate shell"),
        ("Cape river crab", "Invertebrate (Crustacean)", "has an exoskeleton and jointed walking legs without an internal spine")
    ]
    name, group, feature = rng.choice(animals)
    prompt = (
        f"Classify the **{name}** as either a **vertebrate** or an **invertebrate**, "
        f"and state the defining anatomical reason."
    )
    correct_opt = f"{group}, because it {feature}."
    wrong_group = "Invertebrate" if "Vertebrate" in group else "Vertebrate"
    options = [
        correct_opt,
        f"{wrong_group}, because all indigenous African fauna belong to the same skeletal class.",
        f"{wrong_group}, because internal backbones are found only in birds and flying insects.",
        "Neither, because animals with legs are exempt from vertebral classification."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand the major division in Kingdom Animalia:\n"
        f"- Vertebrates: Animals possessing an internal vertebral column (backbone) made of bone or cartilage.\n"
        f"- Invertebrates: Animals lacking an internal backbone (many possess exoskeletons or hydrostatic skeletons).\n\n"
        f"Conclusion: The {name} is a {group} because it {feature}."
    )
    return {
        "id": f"ns7_bio_vert_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "vertebrates_vs_invertebrates_classes",
        "question_family_id": "vertebrates_vs_invertebrates_classes",
        "hints": {
            "tier_1": "Does this animal have a backbone inside its body or an outer shell/exoskeleton?",
            "tier_2": "Vertebrates have an internal spine; invertebrates do not.",
            "tier_3": f"The {name} is a {group}."
        },
        "misconception_tags": ["exoskeleton_backbone_confusion"]
    }

def _build_binomial_nomenclature(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("the African lion", "Panthera leo", "Panthera", "leo"),
        ("the Cheetah", "Acinonyx jubatus", "Acinonyx", "jubatus"),
        ("the Baobab tree", "Adansonia digitata", "Adansonia", "digitata"),
        ("the African elephant", "Loxodonta africana", "Loxodonta", "africana")
    ]
    common, scientific, genus, species = rng.choice(examples)
    prompt = (
        f"Carl Linnaeus developed the system of **binomial nomenclature** for naming living organisms. "
        f"The scientific name for {common} is *{scientific}*.\n\n"
        f"Which component represents the **Genus** and which represents the **species**?"
    )
    correct_opt = f"Genus: {genus} (capitalized) | species: {species} (lowercase)"
    options = [
        correct_opt,
        f"Genus: {species} | species: {genus}",
        f"Both words represent the kingdom and class simultaneously",
        f"Genus: Animalia | species: {common}"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Rules of binomial nomenclature:\n"
        "1. Two-part Latin name: First word = Genus (starts with a capital letter); Second word = species (all lowercase).\n"
        "2. Formatted in italics when printed, or underlined when handwritten.\n\n"
        f"Conclusion: In *{scientific}*, '{genus}' is the Genus and '{species}' is the species."
    )
    return {
        "id": f"ns7_bio_binom_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "binomial_nomenclature_naming",
        "question_family_id": "binomial_nomenclature_naming",
        "hints": {
            "tier_1": "The first word is the broader group (Genus); the second word is the specific organism (species).",
            "tier_2": "Genus is capitalized; species is lowercase.",
            "tier_3": f"Genus is {genus} and species is {species}."
        },
        "misconception_tags": ["genus_species_inversion"]
    }

def _build_dichotomous_keys(rng: random.Random) -> Dict[str, Any]:
    intros = [
        "During a biodiversity survey in a nature reserve, Grade 7 learners use a dichotomous identification key to categorize unknown insect specimens.",
        "Marine biologists working along the South African coastline utilize a dichotomous key to identify newly sampled fish species.",
        "In a life sciences practical session, learners examine indigenous fynbos leaf specimens using a printed classification key.",
        "Botanists at the Kirstenbosch National Botanical Garden rely on dichotomous keys to categorize diverse flora."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"What is the fundamental structural rule of a **dichotomous key** at each identification stage?"
    )
    correct_opt = "It presents exactly two contrasting choices based on observable physical characteristics."
    options = [
        correct_opt,
        "It presents five random opinions that learners vote on democratically.",
        "It lists all organisms alphabetically by their local common nicknames.",
        "It relies exclusively on guessing whether an animal is dangerous to humans."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Scientific principle of dichotomous keys ('di-' = two):\n"
        "A dichotomous key consists of a sequence of paired, contrasting statements (couplets) based on observable "
        "physical traits (e.g. 'Has wings' vs 'Does not have wings'). Each choice leads to the next step until "
        "the organism is uniquely identified."
    )
    return {
        "id": f"ns7_bio_key_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "dichotomous_keys_identification",
        "question_family_id": "dichotomous_keys_identification",
        "hints": {
            "tier_1": "The prefix 'di-' means two.",
            "tier_2": "A dichotomous key branches in pairs: two contrasting choices at each step.",
            "tier_3": "It offers two contrasting choices based on observable traits."
        },
        "misconception_tags": ["dichotomous_multiple_choice_confusion"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "biodiversity_definition_and_importance": _build_biodiversity_definition_and_importance,
        "five_kingdom_classification_system": _build_five_kingdom_classification_system,
        "vertebrates_vs_invertebrates_classes": _build_vertebrates_vs_invertebrates,
        "binomial_nomenclature_naming": _build_binomial_nomenclature,
        "dichotomous_keys_identification": _build_dichotomous_keys
    }
    if target in builders:
        return [builders[target](rng) for _ in range(count)]
    for k, fn in builders.items():
        if target and target in k:
            return [fn(rng) for _ in range(count)]
    res = []
    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        res.append(builders[sub](rng))
    return res
