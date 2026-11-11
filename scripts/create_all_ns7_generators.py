"""
Complete script to generate all remaining Grade 7 Natural Sciences generators.
"""

import os

ns_dir = os.path.join("caps-ai-backend", "app", "utils", "natural_sciences")

# Helper to write files
def write_gen(filename, code):
    path = os.path.join(ns_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Wrote {filename}")

# ============================================================================
# TERM 1: BIODIVERSITY
# ============================================================================
code_biodiversity = '''"""Grade 7 Natural Sciences: Term 1 - Biodiversity Generator.
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
        f"In South Africa, {region} is internationally recognized for having {fact}.\\n\\n"
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
        f"Step 1: Scientific definition from Curriculum Chapter 10:\\n"
        f"Biodiversity (biological diversity) encompasses the variety of all forms of life on Earth, including diversity "
        f"within species (genetic diversity), between species, and across ecosystems.\\n\\n"
        f"Step 2: Connect to South African hotspot:\\n"
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
        f"In Robert Whittaker's five-kingdom classification system, which kingdom is defined by:\\n"
        f"'{desc}'?"
    )
    correct_opt = kingdom
    distractors = [k[1] for k in kingdoms if k[1] != kingdom]
    options = [correct_opt] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Review 5-kingdom characteristics:\\n"
        f"- Monera: Prokaryotes without nucleus.\\n"
        f"- Protista: Simple single-celled eukaryotes.\\n"
        f"- Fungi: Heterotrophs absorbing nutrients, chitin walls.\\n"
        f"- Plantae: Autotrophic photosynthesizers, cellulose walls.\\n"
        f"- Animalia: Multicellular heterotrophs, no cell walls.\\n\\n"
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
        f"Step 1: Understand the major division in Kingdom Animalia:\\n"
        f"- Vertebrates: Animals possessing an internal vertebral column (backbone) made of bone or cartilage.\\n"
        f"- Invertebrates: Animals lacking an internal backbone (many possess exoskeletons or hydrostatic skeletons).\\n\\n"
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
        f"The scientific name for {common} is *{scientific}*.\\n\\n"
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
        "Step 1: Rules of binomial nomenclature:\\n"
        "1. Two-part Latin name: First word = Genus (starts with a capital letter); Second word = species (all lowercase).\\n"
        "2. Formatted in italics when printed, or underlined when handwritten.\\n\\n"
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
    prompt = (
        "A dichotomous key is used by biologists to identify unknown organisms. "
        "What is the key structural rule of a **dichotomous key** at each identification stage?"
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
        "Step 1: Scientific principle of dichotomous keys ('di-' = two):\\n"
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
'''
write_gen("ns7_biodiversity_generator.py", code_biodiversity)

# ============================================================================
# TERM 1: SEXUAL REPRODUCTION (ANGIOSPERMS)
# ============================================================================
code_reproduction = '''"""Grade 7 Natural Sciences: Term 1 - Sexual Reproduction Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/03. Sexual reproduction.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "flower_anatomy_and_functions",
    "pollination_mechanisms_wind_vs_insect",
    "fertilisation_process_ovule_to_seed",
    "fruit_and_seed_dispersal_strategies",
    "sexual_vs_asexual_reproduction_comparison"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 1/03. Sexual reproduction.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_flower_anatomy(rng: random.Random) -> Dict[str, Any]:
    parts = [
        ("Petals (corolla)", "often brightly coloured and scented with nectar guides", "attract insect and bird pollinators"),
        ("Anther (part of stamen)", "contains pollen sacs at the top of the filament", "produce and release male pollen grains"),
        ("Stigma (part of pistil/carpel)", "sticky or feathery surface situated at the top of the style", "receive and trap pollen grains during pollination"),
        ("Ovary (base of pistil/carpel)", "swollen basal chamber containing ovules", "protect ovules and develop into the fruit after fertilisation"),
        ("Sepals (calyx)", "small green leaf-like structures enclosing the flower bud", "protect the delicate internal floral organs before the bud opens")
    ]
    part, appearance, role = rng.choice(parts)
    prompt = (
        f"In flowering plants (angiosperms), what is the primary biological function of the **{part}**?"
    )
    correct_opt = f"To {role}."
    distractors = [f"To {p[2]}." for p in parts if p[0] != part]
    options = [correct_opt] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Anatomical function from Curriculum Chapter on Angiosperms:\\n"
        f"- {part} is {appearance}.\\n\\n"
        f"Step 2: Biological function:\\n"
        f"The primary role is to {role}."
    )
    return {
        "id": f"ns7_rep_anat_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "flower_anatomy_and_functions",
        "question_family_id": "flower_anatomy_and_functions",
        "hints": {
            "tier_1": "Recall whether this part is male (stamen), female (pistil), or protective (sepals/petals).",
            "tier_2": "Look at its position on the flower and its physical appearance.",
            "tier_3": f"The function of {part} is to {role}."
        },
        "misconception_tags": ["stigma_anther_confusion", "sepal_petal_confusion"]
    }

def _build_pollination_mechanisms(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("Wind-pollinated flowers (e.g. maize, grass)", "small dull green petals with no scent or nectar, large feathery stigmas hanging outside, and abundant light dry pollen grains", "Wind pollination"),
        ("Insect-pollinated flowers (e.g. hibiscus, protea)", "large brightly coloured petals with sweet nectar and strong scents, sticky stigmas enclosed inside, and heavy sticky pollen grains", "Insect pollination")
    ]
    desc, features, mode = rng.choice(types)
    prompt = (
        f"A botanist examines a plant with the following floral adaptations:\\n"
        f"'{features}'.\\n\\n"
        f"What is the predominant mechanism of **pollination** for this flower?"
    )
    correct_opt = mode
    alt_mode = "Insect pollination" if mode == "Wind pollination" else "Wind pollination"
    options = [
        correct_opt,
        alt_mode,
        "Water surface pollination exclusively",
        "Asexual self-cloning with zero pollen transfer"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Compare pollination syndromes:\\n"
        f"- Wind-pollinated: No need for colour/nectar; needs feathery exposed stigmas and massive light pollen.\\n"
        f"- Insect-pollinated: Bright petals, nectar rewards, sticky pollen adhering to insect bodies.\\n\\n"
        f"Conclusion: '{features}' is adapted for {mode}."
    )
    return {
        "id": f"ns7_rep_poll_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "pollination_mechanisms_wind_vs_insect",
        "question_family_id": "pollination_mechanisms_wind_vs_insect",
        "hints": {
            "tier_1": "Does the flower invest energy in attracting animals (nectar/colour) or produce light windblown pollen?",
            "tier_2": "Feathery stigmas and dull flowers rely on wind; bright petals and nectar rely on insects.",
            "tier_3": f"This syndrome indicates {mode}."
        },
        "misconception_tags": ["pollination_fertilisation_confusion"]
    }

def _build_fertilisation_process(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Describe the sequence of events that occurs after a compatible pollen grain lands on the stigma of a flower, "
        "leading to **fertilisation** and seed development. (4 marks)"
    )
    sample_answer = (
        "1. Pollen germination: The pollen grain absorbs moisture on the sticky stigma and germinates, growing a pollen tube down through the style.\\n"
        "2. Growth toward ovary: The pollen tube enters the ovary through a microscopic opening called the micropyle.\\n"
        "3. Fusion of gametes: The male sex cell (gamete) travels down the tube and fuses with the female ovule (egg cell) to form a zygote (fertilisation).\\n"
        "4. Development: The fertilised ovule develops into a seed, while the surrounding ovary wall swells and ripens into a fruit."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. Growth of pollen tube down through the style (1 mark).\\n"
        "2. Entry into ovary and ovule (1 mark).\\n"
        "3. Fusion of male gamete nucleus with female ovule nucleus (fertilisation) (1 mark).\\n"
        "4. Ovule develops into seed, ovary develops into fruit (1 mark)."
    )
    return {
        "id": f"ns7_rep_fert_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "fertilisation_process_ovule_to_seed",
        "question_family_id": "fertilisation_process_ovule_to_seed",
        "hints": {
            "tier_1": "Trace the path of the male sex cell from the stigma down to the ovule.",
            "tier_2": "Mention pollen tube growth, fusion of gametes, and the transformation of ovule to seed and ovary to fruit.",
            "tier_3": "Explain pollen tube germination, gamete fusion in the ovary, and seed/fruit formation."
        },
        "misconception_tags": ["ovary_ovule_fruit_seed_confusion"]
    }

def _build_seed_dispersal(rng: random.Random) -> Dict[str, Any]:
    mechanisms = [
        ("Dandelion parachutes and maple winged seeds", "Wind dispersal", "light structures or wings that catch air currents to travel far from the parent plant"),
        ("Blackjack burrs with hooked spines", "Animal dispersal (external adhesion)", "hooks that cling to animal fur or human clothing to be carried away"),
        ("Fleshy sweet berries and figs", "Animal dispersal (ingestion)", "edible nutritious fruits eaten by birds and mammals, with indigestible seeds deposited in droppings"),
        ("Pea pods and touch-me-not balsam", "Explosive / self-dispersal mechanism", "drying pods that build internal mechanical tension and burst open suddenly")
    ]
    fruit_example, mechanism, feature = rng.choice(mechanisms)
    prompt = (
        f"Consider **{fruit_example}**. By which mechanism are these seeds dispersed, and why is seed dispersal essential for plant survival?"
    )
    correct_opt = f"{mechanism}: It prevents overcrowding and competition with the parent plant for light, water, and soil nutrients."
    options = [
        correct_opt,
        f"{mechanism}: It guarantees that all seedlings grow underneath the parent tree's shadow without sunlight.",
        "Asexual vegetative cloning: It ensures seeds never leave the flower bud.",
        "Artificial germination: Seeds cannot survive outdoors without commercial human greenhouse irrigation."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify dispersal adaptation:\\n"
        f"{fruit_example} possesses {feature}, which enables {mechanism}.\\n\\n"
        f"Step 2: Evolutionary importance of seed dispersal:\\n"
        f"Dispersal spreads offspring away from parent plants, reducing intraspecific competition for water, space, and nutrients."
    )
    return {
        "id": f"ns7_rep_disp_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "fruit_and_seed_dispersal_strategies",
        "question_family_id": "fruit_and_seed_dispersal_strategies",
        "hints": {
            "tier_1": "Look at the shape of the seed (hooks, wings, sweet flesh, or popping pod).",
            "tier_2": "Dispersal prevents seedlings from choking each other in competition under the parent plant.",
            "tier_3": f"This adaptation utilizes {mechanism} to reduce resource competition."
        },
        "misconception_tags": ["dispersal_vs_pollination_confusion"]
    }

def _build_sexual_vs_asexual(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Which statement correctly compares **sexual reproduction** with **asexual reproduction** in plants?"
    )
    correct_opt = "Sexual reproduction involves two parents and fusion of gametes, producing genetically varied offspring; asexual reproduction involves one parent producing genetically identical clones."
    options = [
        correct_opt,
        "Sexual reproduction produces clones that are 100% identical to the parent; asexual reproduction creates high genetic variety.",
        "Asexual reproduction requires flowers, pollination, and seeds; sexual reproduction uses only tubers and runners.",
        "Both reproduction modes require male and female sex cells to fertilise each other."
    ]
    rng.shuffle(options)
    sol = (
        "Comparison of Reproduction Modes:\\n"
        "- Sexual reproduction: Fusion of male and female sex cells (gametes) -> genetic variation -> better survival in changing environments.\\n"
        "- Asexual reproduction: Single parent using vegetative parts (runners, bulbs, cuttings) -> offspring are genetically identical clones."
    )
    return {
        "id": f"ns7_rep_comp_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "sexual_vs_asexual_reproduction_comparison",
        "question_family_id": "sexual_vs_asexual_reproduction_comparison",
        "hints": {
            "tier_1": "Think about how many parents are needed and whether the offspring are clones or varied.",
            "tier_2": "Sexual reproduction generates genetic diversity; asexual reproduction creates clones.",
            "tier_3": "Sexual reproduction involves gamete fusion and genetic variation."
        },
        "misconception_tags": ["clone_variation_inversion"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "flower_anatomy_and_functions": _build_flower_anatomy,
        "pollination_mechanisms_wind_vs_insect": _build_pollination_mechanisms,
        "fertilisation_process_ovule_to_seed": _build_fertilisation_process,
        "fruit_and_seed_dispersal_strategies": _build_seed_dispersal,
        "sexual_vs_asexual_reproduction_comparison": _build_sexual_vs_asexual
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
'''
write_gen("ns7_sexual_reproduction_generator.py", code_reproduction)

# ============================================================================
# TERM 1: VARIATION
# ============================================================================
code_variation = '''"""Grade 7 Natural Sciences: Term 1 - Variation Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/04. Variation.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "variation_within_species_definition",
    "inherited_vs_environmental_variation",
    "continuous_vs_discontinuous_variation",
    "survival_value_of_variation",
    "species_concept_and_interbreeding"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 1/04. Variation.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_variation_definition(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("domestic dogs (Canis lupus familiaris)", "different coat colours, hair lengths, muzzle shapes, and body sizes despite all belonging to the same single species"),
        ("human beings (Homo sapiens)", "variations in eye colour, skin tone, natural height, and fingerprint patterns"),
        ("sunflower plants in an agricultural field", "subtle differences in stem height, leaf surface area, and seed yield")
    ]
    org, traits = rng.choice(examples)
    prompt = (
        f"Consider {org}. Individuals display {traits}.\\n\\n"
        f"What scientific term describes these physical differences among individuals of the same species?"
    )
    correct_opt = "Variation"
    options = ["Variation", "Speciation", "Extinction", "Metamorphosis"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand concept from Curriculum Chapter 4:\\n"
        f"Variation refers to the natural differences in physical, physiological, or genetic characteristics "
        f"between individuals of the exact same species.\\n\\n"
        f"Conclusion: These differences are termed Variation."
    )
    return {
        "id": f"ns7_var_def_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "variation_within_species_definition",
        "question_family_id": "variation_within_species_definition",
        "hints": {
            "tier_1": "Think of the word that means 'differences' among members of a group.",
            "tier_2": "It comes from the word 'vary'.",
            "tier_3": "The correct term is Variation."
        },
        "misconception_tags": ["variation_speciation_confusion"]
    }

def _build_inherited_vs_environmental(rng: random.Random) -> Dict[str, Any]:
    traits = [
        ("Natural human eye colour (brown, blue, green)", "Inherited variation", "passed down from biological parents through genes in DNA"),
        ("A surgical scar on a learner's knee from playing soccer", "Environmental variation", "caused by external life events, injuries, or lifestyle and cannot be passed to offspring"),
        ("Human ABO blood group (A, B, AB, O)", "Inherited variation", "genetically determined by inherited alleles from birth"),
        ("Speaking fluent isiZulu, English, and Afrikaans", "Environmental variation", "acquired through learning, culture, and environmental upbringing")
    ]
    trait, class_type, reason = rng.choice(traits)
    prompt = (
        f"Classify **{trait}** as either **inherited variation** or **environmental variation**, "
        f"and state the biological reason."
    )
    correct_opt = f"{class_type}, because it is {reason}."
    alt_class = "Environmental variation" if class_type == "Inherited variation" else "Inherited variation"
    options = [
        correct_opt,
        f"{alt_class}, because all human characteristics can be acquired at will during adulthood.",
        f"{alt_class}, because physical traits do not involve genetics.",
        "Neither, because human traits cannot be classified scientifically."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Distinguish between the two sources of variation:\\n"
        f"- Inherited: Determined by genetic information in DNA received from parents at fertilisation.\\n"
        f"- Environmental: Influenced by climate, diet, injury, culture, or lifestyle during an organism's lifetime.\\n\\n"
        f"Conclusion: {trait} is {class_type} because it is {reason}."
    )
    return {
        "id": f"ns7_var_inh_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "inherited_vs_environmental_variation",
        "question_family_id": "inherited_vs_environmental_variation",
        "hints": {
            "tier_1": "Were you born with this feature due to DNA, or did life experiences cause it?",
            "tier_2": "Inherited traits come from parents' genes; environmental traits come from lifestyle/injuries.",
            "tier_3": f"This is an example of {class_type}."
        },
        "misconception_tags": ["environmental_inheritance_lamarck"]
    }

def _build_continuous_vs_discontinuous(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("Human height (e.g. from 1.3 m to 2.1 m with every intermediate measurement possible)", "Continuous variation", "measured on a continuous numerical scale with a full gradient of values and no distinct categories"),
        ("Ability to roll the tongue (either you can roll your tongue or you cannot)", "Discontinuous variation", "falls into distinct separate categories with no in-between states"),
        ("Human body mass (measured in kilograms)", "Continuous variation", "can take any value along a continuous quantitative range"),
        ("Human ABO blood group (A, B, AB, or O)", "Discontinuous variation", "divided into clear-cut discrete categories determined by a single gene")
    ]
    char_desc, var_type, rationale = rng.choice(examples)
    prompt = (
        f"A Grade 7 science class measures learner characteristics. Consider **{char_desc}**.\\n\\n"
        f"Is this an example of **continuous variation** or **discontinuous variation**, and why?"
    )
    correct_opt = f"{var_type}, because it is {rationale}."
    alt_type = "Discontinuous variation" if var_type == "Continuous variation" else "Continuous variation"
    options = [
        correct_opt,
        f"{alt_type}, because all measurements in biology are purely random categories.",
        f"{alt_type}, because this characteristic is completely invisible to scientists.",
        "Neither, because human traits cannot be graphed."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand data distribution types:\\n"
        f"- Continuous variation: Quantitative traits showing a complete range of values (forms a bell-shaped normal curve, e.g. height, mass).\\n"
        f"- Discontinuous variation: Qualitative traits falling into distinct non-overlapping categories (plotted as bar graphs, e.g. blood group, tongue rolling).\\n\\n"
        f"Conclusion: {char_desc} demonstrates {var_type} because it is {rationale}."
    )
    return {
        "id": f"ns7_var_cont_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "continuous_vs_discontinuous_variation",
        "question_family_id": "continuous_vs_discontinuous_variation",
        "hints": {
            "tier_1": "Can you measure it as a continuous number on a ruler/scale, or is it an 'either/or' category?",
            "tier_2": "Height/mass is continuous; tongue rolling/blood group is discontinuous.",
            "tier_3": f"This is an example of {var_type}."
        },
        "misconception_tags": ["continuous_discontinuous_graph_inversion"]
    }

def _build_survival_value(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain how genetic variation within a species increases its chances of surviving when a catastrophic "
        "disease or environmental change strikes a population. (4 marks)"
    )
    sample_answer = (
        "If all individuals in a population were genetically identical clones, a single lethal disease or drought "
        "could wipe out the entire population because none would possess resistance. Genetic variation ensures that some "
        "individuals carry naturally resistant alleles or advantageous traits. These resistant individuals survive the catastrophe, "
        "reproduce, and pass their survival traits to the next generation, preventing species extinction."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. Genetic uniformity risk: Identical individuals all perish from the same pathogen/threat (2 marks).\\n"
        "2. Survival advantage: Varied individuals carry resistant traits, survive, reproduce, and prevent extinction (2 marks)."
    )
    return {
        "id": f"ns7_var_surv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "survival_value_of_variation",
        "question_family_id": "survival_value_of_variation",
        "hints": {
            "tier_1": "What happens if every individual is identical and a new disease arrives?",
            "tier_2": "Variation means some individuals have natural resistance and will survive to reproduce.",
            "tier_3": "Explain that variation prevents total extinction by providing resistant survivors."
        },
        "misconception_tags": ["monoculture_immunity_fallacy"]
    }

def _build_species_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In biological science, what is the single defining characteristic that determines whether two organisms "
        "belong to the exact same **species**?"
    )
    correct_opt = "They can interbreed naturally with each other to produce fertile offspring."
    options = [
        correct_opt,
        "They have identical coat colours and eat the exact same food.",
        "They live in the exact same physical cage or geographical city.",
        "They both possess four legs and can breathe atmospheric oxygen."
    ]
    rng.shuffle(options)
    sol = (
        "Definition of a Biological Species:\\n"
        "A biological species is a group of organisms that can naturally interbreed and produce viable, "
        "fertile offspring (offspring that are capable of reproducing themselves). Mating between different species "
        "(such as a horse and a donkey producing a mule) results in sterile offspring."
    )
    return {
        "id": f"ns7_var_spec_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "species_concept_and_interbreeding",
        "question_family_id": "species_concept_and_interbreeding",
        "hints": {
            "tier_1": "Think about what happens when organisms reproduce.",
            "tier_2": "The key word is 'fertile' offspring.",
            "tier_3": "Members of the same species must produce fertile offspring."
        },
        "misconception_tags": ["species_appearance_similarity_error"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "variation_within_species_definition": _build_variation_definition,
        "inherited_vs_environmental_variation": _build_inherited_vs_environmental,
        "continuous_vs_discontinuous_variation": _build_continuous_vs_discontinuous,
        "survival_value_of_variation": _build_survival_value,
        "species_concept_and_interbreeding": _build_species_concept
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
'''
write_gen("ns7_variation_generator.py", code_variation)
