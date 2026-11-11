"""Grade 7 Natural Sciences: Term 1 - Variation Generator.
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
        f"Consider {org}. Individuals display {traits}.\n\n"
        f"What scientific term describes these physical differences among individuals of the same species?"
    )
    correct_opt = "Variation"
    options = ["Variation", "Speciation", "Extinction", "Metamorphosis"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand concept from Curriculum Chapter 4:\n"
        f"Variation refers to the natural differences in physical, physiological, or genetic characteristics "
        f"between individuals of the exact same species.\n\n"
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
        f"Step 1: Distinguish between the two sources of variation:\n"
        f"- Inherited: Determined by genetic information in DNA received from parents at fertilisation.\n"
        f"- Environmental: Influenced by climate, diet, injury, culture, or lifestyle during an organism's lifetime.\n\n"
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
        f"A Grade 7 science class measures learner characteristics. Consider **{char_desc}**.\n\n"
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
        f"Step 1: Understand data distribution types:\n"
        f"- Continuous variation: Quantitative traits showing a complete range of values (forms a bell-shaped normal curve, e.g. height, mass).\n"
        f"- Discontinuous variation: Qualitative traits falling into distinct non-overlapping categories (plotted as bar graphs, e.g. blood group, tongue rolling).\n\n"
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
    cases = [
        "a wild African cheetah population in the Kruger National Park facing an infectious viral disease",
        "a cultivated agricultural crop of genetically identical bananas attacked by fungal disease",
        "a population of acacia trees in the Karoo experiencing a multi-year severe drought",
        "a colony of honeybees in the Western Cape exposed to a novel parasitic mite"
    ]
    context = rng.choice(cases)
    prompt = (
        f"Consider the ecological scenario of {context}.\n\n"
        f"Explain how genetic variation within a population increases its chances of surviving when an environmental "
        f"catastrophe or virulent disease strikes. (4 marks)"
    )
    sample_answer = (
        "If all individuals in a population were genetically identical clones, a single lethal disease or drought "
        "could wipe out the entire population because none would possess resistance. Genetic variation ensures that some "
        "individuals carry naturally resistant alleles or advantageous traits. These resistant individuals survive the catastrophe, "
        "reproduce, and pass their survival traits to the next generation, preventing species extinction."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Genetic uniformity risk: Identical individuals all perish from the same pathogen/threat (2 marks).\n"
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
    cases = [
        "a horse and a donkey can mate to produce a mule, but the mule is sterile and cannot reproduce",
        "lions and tigers in captivity can produce a liger, but ligers are typically infertile",
        "all domestic dog breeds from Chihuahuas to Great Danes can interbreed to produce healthy, fertile puppies",
        "different species of zebra share similar habitats in southern Africa but do not naturally produce fertile offspring"
    ]
    context = rng.choice(cases)
    prompt = (
        f"Consider the biological observation that {context}.\n\n"
        f"In biological science, what is the single defining characteristic that determines whether two organisms "
        f"belong to the exact same **species**?"
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
        "Definition of a Biological Species:\n"
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
