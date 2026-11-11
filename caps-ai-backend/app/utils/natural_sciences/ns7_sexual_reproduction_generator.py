"""Grade 7 Natural Sciences: Term 1 - Sexual Reproduction Generator.
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
        f"Step 1: Anatomical function from Curriculum Chapter on Angiosperms:\n"
        f"- {part} is {appearance}.\n\n"
        f"Step 2: Biological function:\n"
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
        f"A botanist examines a plant with the following floral adaptations:\n"
        f"'{features}'.\n\n"
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
        f"Step 1: Compare pollination syndromes:\n"
        f"- Wind-pollinated: No need for colour/nectar; needs feathery exposed stigmas and massive light pollen.\n"
        f"- Insect-pollinated: Bright petals, nectar rewards, sticky pollen adhering to insect bodies.\n\n"
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
    flowers = ["a hibiscus flower", "a sweet pea flower", "a wild protea blossom", "a sunflower head"]
    flower = rng.choice(flowers)
    prompt = (
        f"A pollinating insect deposits compatible pollen onto the sticky stigma of {flower}.\n\n"
        f"Describe the sequential biological events that occur from this moment, "
        f"leading to **fertilisation** inside the ovary and subsequent seed development. (4 marks)"
    )
    sample_answer = (
        "1. Pollen germination: The pollen grain absorbs moisture on the sticky stigma and germinates, growing a pollen tube down through the style.\n"
        "2. Growth toward ovary: The pollen tube enters the ovary through a microscopic opening called the micropyle.\n"
        "3. Fusion of gametes: The male sex cell (gamete) travels down the tube and fuses with the female ovule (egg cell) to form a zygote (fertilisation).\n"
        "4. Development: The fertilised ovule develops into a seed, while the surrounding ovary wall swells and ripens into a fruit."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Growth of pollen tube down through the style (1 mark).\n"
        "2. Entry into ovary and ovule (1 mark).\n"
        "3. Fusion of male gamete nucleus with female ovule nucleus (fertilisation) (1 mark).\n"
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
        f"Step 1: Identify dispersal adaptation:\n"
        f"{fruit_example} possesses {feature}, which enables {mechanism}.\n\n"
        f"Step 2: Evolutionary importance of seed dispersal:\n"
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
    intros = [
        "In plant biology, species reproduce using either sexual or asexual mechanisms.",
        "Agricultural botanists compare seed propagation with vegetative cuttings in crop plants.",
        "During a plant reproduction study, learners analyze differences between gamete fusion and vegetative propagation.",
        "Horticulturists propagate roses through both cross-pollinated seeds and stem cuttings."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"Which statement correctly compares **sexual reproduction** with **asexual reproduction** in plants?"
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
        "Comparison of Reproduction Modes:\n"
        "- Sexual reproduction: Fusion of male and female sex cells (gametes) -> genetic variation -> better survival in changing environments.\n"
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
