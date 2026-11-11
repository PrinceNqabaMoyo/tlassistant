"""Grade 7 Natural Sciences: Term 1 - The Biosphere Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/01. The Biosphere.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "biosphere_definition_and_zones",
    "interlocking_spheres_atmosphere_hydrosphere_lithosphere",
    "seven_life_processes_mrs_gren",
    "requirements_for_sustaining_life",
    "habitats_and_environmental_adaptations"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 1/01. The Biosphere.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_biosphere_definition_and_zones(rng: random.Random) -> Dict[str, Any]:
    zones = [
        ("the global ecological zone of life on Earth where all living organisms interact with abiotic elements", "The Biosphere"),
        ("the layer of gases and air surrounding Earth necessary for respiration", "The Atmosphere"),
        ("all liquid water, ice, and groundwater reserves across the planet", "The Hydrosphere"),
        ("the solid rocky crust and upper mantle forming continents and ocean floors", "The Lithosphere")
    ]
    desc, term = rng.choice(zones)
    prompt = f"In Natural Sciences, which term specifically describes {desc}?"
    correct_opt = term
    distractors = [z[1] for z in zones if z[1] != term]
    options = [correct_opt] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand Earth's spheres from Curriculum Chapter 1:\n"
        f"- Biosphere: Zone of life integrating organisms with air, water, and soil.\n"
        f"- Atmosphere: Air layer.\n"
        f"- Hydrosphere: Water layer.\n"
        f"- Lithosphere: Solid rocky layer.\n\n"
        f"Conclusion: {desc} defines {term}."
    )
    return {
        "id": f"ns7_bio_zone_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "biosphere_definition_and_zones",
        "question_family_id": "biosphere_definition_and_zones",
        "hints": {
            "tier_1": "Notice the prefix: 'Bio-' means life, 'Hydro-' means water, 'Litho-' means stone/rock, 'Atmo-' means air.",
            "tier_2": "Match the described component directly to its Greek root word.",
            "tier_3": f"The correct classification is {term}."
        },
        "misconception_tags": ["sphere_interchange_error"]
    }

def _build_interlocking_spheres(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("A mangrove tree absorbs water from muddy coastal soil and releases water vapour into the air during transpiration", "Hydrosphere, Lithosphere, and Atmosphere interacting with the Biosphere"),
        ("A Nile crocodile basks on sandy riverbanks while absorbing solar heat and hunting fish underwater", "Lithosphere, Hydrosphere, and Atmosphere providing survival conditions"),
        ("Soil bacteria decompose fallen autumn leaves on rocky ground, releasing carbon dioxide into the air", "Biosphere cycling nutrients into the Lithosphere and Atmosphere")
    ]
    event, interaction = rng.choice(examples)
    prompt = (
        f"Consider the following ecological interaction:\n"
        f"'{event}'.\n\n"
        f"Which statement best explains how Earth's spheres interlock in this scenario?"
    )
    correct_opt = interaction
    options = [
        correct_opt,
        "The Biosphere operates completely isolated from non-living abiotic systems",
        "Only the Atmosphere is involved because trees and animals require only oxygen",
        "The Lithosphere prevents any living organisms from interacting with water or air"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify all abiotic components:\n"
        f"Living organisms cannot survive in a vacuum; they depend on interactions with soil/rock (Lithosphere), "
        f"water reserves (Hydrosphere), and atmospheric gases (Atmosphere).\n\n"
        f"Conclusion: '{event}' demonstrates {interaction}."
    )
    return {
        "id": f"ns7_bio_spheres_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "interlocking_spheres_atmosphere_hydrosphere_lithosphere",
        "question_family_id": "interlocking_spheres_atmosphere_hydrosphere_lithosphere",
        "hints": {
            "tier_1": "Break down which spheres provide soil, water, and gas in the scenario.",
            "tier_2": "The living organism bridges the gap between rocks, water, and air.",
            "tier_3": f"The interaction shows {interaction}."
        },
        "misconception_tags": ["isolated_biosphere_misconception"]
    }

def _build_seven_life_processes(rng: random.Random) -> Dict[str, Any]:
    processes = [
        ("Releasing energy from digested glucose inside cellular mitochondria", "Respiration", "Digestion"),
        ("Removing harmful metabolic waste products such as urea and carbon dioxide from the body", "Excretion", "Egestion / defaecation"),
        ("Detecting changes in temperature, light, or sound in the surrounding environment and responding", "Sensitivity", "Reproduction"),
        ("Permanently increasing in body size and dry mass by developing new cells", "Growth", "Movement")
    ]
    act_desc, correct_proc, wrong_proc = rng.choice(processes)
    prompt = (
        f"According to the seven vital life processes (MRS GREN), which process is defined as:\n"
        f"'{act_desc}'?"
    )
    correct_opt = correct_proc
    distractors = [p[1] for p in processes if p[1] != correct_proc] + [wrong_proc]
    options = [correct_opt] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Recall the MRS GREN life processes:\n"
        f"Movement, Respiration, Sensitivity, Growth, Reproduction, Excretion, Nutrition.\n\n"
        f"Step 2: Analysis:\n"
        f"'{act_desc}' is the scientific definition of {correct_proc}."
    )
    return {
        "id": f"ns7_bio_mrs_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "seven_life_processes_mrs_gren",
        "question_family_id": "seven_life_processes_mrs_gren",
        "hints": {
            "tier_1": "Recall the letters of MRS GREN and what each life process achieves.",
            "tier_2": "Look at the biological function: removing waste is excretion, releasing energy is respiration.",
            "tier_3": f"The process described is {correct_proc}."
        },
        "misconception_tags": ["respiration_breathing_confusion", "excretion_egestion_confusion"]
    }

def _build_requirements_for_sustaining_life(rng: random.Random) -> Dict[str, Any]:
    ecosystems = [
        ("a fynbos nature reserve in the Western Cape", "terrestrial green plants such as proteas and rooibos"),
        ("a savanna biome in the Kruger National Park", "trees such as the baobab and acacia"),
        ("an indigenous forest in Knysna", "canopy trees such as yellowwoods and stinkwoods"),
        ("a school agricultural vegetable garden in Gauteng", "cultivated crops such as spinach and maize")
    ]
    location, flora = rng.choice(ecosystems)
    prompt = (
        f"During an ecological field investigation in {location}, learners observe {flora}.\n\n"
        f"Name THREE essential non-living (abiotic) requirements that these green plants "
        f"must obtain from their physical environment to sustain life, and state the biological role of each. (6 marks)"
    )
    sample_answer = (
        "1. Sunlight (radiant energy): Absorbed by chlorophyll in leaves to drive photosynthesis.\n"
        "2. Water (H2O): Acts as a cellular solvent, provides turgor pressure support, and donates hydrogen for glucose production.\n"
        "3. Carbon dioxide (CO2): Absorbed through stomata from the atmosphere as the carbon source for synthesising carbohydrates."
    )
    sol = (
        "Marking Rubric (2 marks per requirement + function, total 6 marks):\n"
        "1. Sunlight / radiant energy: Required for photosynthesis (2 marks).\n"
        "2. Water: Solvent, turgor pressure, reactant in photosynthesis (2 marks).\n"
        "3. Carbon dioxide: Carbon backbone for glucose synthesis (2 marks)."
    )
    return {
        "id": f"ns7_bio_req_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 6,
        "subskill": "requirements_for_sustaining_life",
        "question_family_id": "requirements_for_sustaining_life",
        "hints": {
            "tier_1": "Think about what a plant needs to photosynthesise and grow.",
            "tier_2": "List sunlight, water, and carbon dioxide, and explain what the plant uses each for.",
            "tier_3": "Mention radiant energy for photosynthesis, water for transport/support, and CO2 for food production."
        },
        "misconception_tags": ["plant_food_absorption_misconception"]
    }

def _build_habitats_and_adaptations(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("The camel in hot arid deserts", "broad padded feet to walk on soft sand, hump storing fat for metabolic water, and slit nostrils to block dust", "Desert biome adaptation"),
        ("The water lily in freshwater ponds", "large flat floating leaves with stomata on the upper surface to capture maximum sunlight and air", "Aquatic wetland adaptation"),
        ("The camel thorn tree in the Kalahari", "extremely deep taproots reaching underground water tables up to 60 metres down", "Arid savanna adaptation")
    ]
    organism, adaptation, rationale = rng.choice(cases)
    prompt = (
        f"Consider {organism}. It possesses {adaptation}.\n\n"
        f"How does this specific structural adaptation increase the organism's survival in its habitat?"
    )
    correct_opt = f"It enables the organism to overcome harsh environmental conditions ({rationale.lower()})"
    options = [
        correct_opt,
        "It forces the organism to change into a completely different species within weeks",
        "It stops the organism from needing any water or oxygen to survive",
        "It allows the organism to survive without performing cellular respiration"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand biological adaptations:\n"
        f"An adaptation is a genetically inherited structural, functional, or behavioural characteristic that "
        f"improves an organism's chances of surviving and reproducing in its natural habitat.\n\n"
        f"Conclusion: {adaptation} directly supports survival in this {rationale.lower()}."
    )
    return {
        "id": f"ns7_bio_adapt_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "habitats_and_environmental_adaptations",
        "question_family_id": "habitats_and_environmental_adaptations",
        "hints": {
            "tier_1": "Think about the challenges of the organism's habitat (e.g. desert heat, waterlogged ponds).",
            "tier_2": "Adaptations are specialized physical features that help organisms thrive in specific conditions.",
            "tier_3": "The feature directly helps the organism survive the habitat's physical demands."
        },
        "misconception_tags": ["lamarckian_adaptation_misconception"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "biosphere_definition_and_zones": _build_biosphere_definition_and_zones,
        "interlocking_spheres_atmosphere_hydrosphere_lithosphere": _build_interlocking_spheres,
        "seven_life_processes_mrs_gren": _build_seven_life_processes,
        "requirements_for_sustaining_life": _build_requirements_for_sustaining_life,
        "habitats_and_environmental_adaptations": _build_habitats_and_adaptations
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
