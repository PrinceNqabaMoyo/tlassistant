"""Grade 7 Natural Sciences: Term 2 - Periodic Table of Elements Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/04. The Periodic Table of Elements.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "element_definition_and_symbols",
    "metals_nonmetals_semimetals_classification",
    "atomic_number_and_arrangement",
    "first_twenty_elements_identification",
    "mendeleev_periodic_table_history"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 2/04. The Periodic Table of Elements.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_element_symbols(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Hydrogen", "H"), ("Helium", "He"), ("Carbon", "C"), ("Nitrogen", "N"),
        ("Oxygen", "O"), ("Sodium", "Na"), ("Magnesium", "Mg"), ("Aluminium", "Al"),
        ("Silicon", "Si"), ("Phosphorus", "P"), ("Sulfur", "S"), ("Chlorine", "Cl"),
        ("Potassium", "K"), ("Calcium", "Ca"), ("Iron", "Fe"), ("Copper", "Cu"), ("Gold", "Au")
    ]
    name, sym = rng.choice(elements)
    prompt = f"What is the correct chemical symbol for the element **{name}** on the Periodic Table?"
    correct_opt = sym
    distractors = [e[1] for e in elements if e[1] != sym]
    options = [correct_opt] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Chemical symbol convention:\n"
        f"Chemical symbols are written with the first letter in capital and the second letter (if present) in lowercase.\n\n"
        f"Conclusion: The symbol for {name} is {sym}."
    )
    return {
        "id": f"ns7_pt_sym_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "element_definition_and_symbols",
        "question_family_id": "element_definition_and_symbols",
        "hints": {
            "tier_1": "Recall the Latin or English root for this element.",
            "tier_2": "The first letter is always capital; second is lowercase.",
            "tier_3": f"The symbol for {name} is {sym}."
        },
        "misconception_tags": ["case_sensitivity_symbol_error"]
    }

def _build_metals_nonmetals_semimetals(rng: random.Random) -> Dict[str, Any]:
    groups = [
        ("Metals", "situated on the left and centre of the Periodic Table, typically shiny (lustrous), malleable, ductile, and good electrical and thermal conductors", "Copper (Cu), Iron (Fe), Gold (Au)"),
        ("Non-metals", "situated on the top right of the Periodic Table, dull in appearance, brittle when solid, and poor conductors of heat and electricity", "Oxygen (O), Carbon (C), Sulfur (S)"),
        ("Semi-metals (Metalloids)", "situated along the zigzag staircase dividing metals and non-metals, possessing intermediate properties and acting as semiconductors", "Silicon (Si), Boron (B), Germanium (Ge)")
    ]
    grp, desc, ex = rng.choice(groups)
    prompt = (
        f"On the Periodic Table of Elements, which group of elements is characterized as:\n"
        f"'{desc}'?"
    )
    correct_opt = grp
    options = ["Metals", "Non-metals", "Semi-metals (Metalloids)", "Noble radioactive isotopes"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Classification on the Periodic Table:\n"
        f"- Left/centre: Metals (shiny, conductors).\n"
        f"- Upper right: Non-metals (dull, brittle, insulators).\n"
        f"- Staircase border: Semi-metals / metalloids (semiconductors like Si).\n\n"
        f"Conclusion: '{desc}' describes {grp}."
    )
    return {
        "id": f"ns7_pt_grp_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "metals_nonmetals_semimetals_classification",
        "question_family_id": "metals_nonmetals_semimetals_classification",
        "hints": {
            "tier_1": "Look at where they are on the table and whether they conduct electricity.",
            "tier_2": "Shiny conductors are Metals; dull insulators are Non-metals; intermediate are Metalloids.",
            "tier_3": f"This describes {grp}."
        },
        "misconception_tags": ["semimetal_metal_confusion"]
    }

def _build_atomic_number(rng: random.Random) -> Dict[str, Any]:
    elements_at = [
        ("Hydrogen", 1), ("Helium", 2), ("Lithium", 3), ("Beryllium", 4),
        ("Boron", 5), ("Carbon", 6), ("Nitrogen", 7), ("Oxygen", 8),
        ("Fluorine", 9), ("Neon", 10), ("Sodium", 11), ("Magnesium", 12),
        ("Aluminium", 13), ("Silicon", 14), ("Phosphorus", 15), ("Sulfur", 16),
        ("Chlorine", 17), ("Argon", 18), ("Potassium", 19), ("Calcium", 20)
    ]
    name, at_num = rng.choice(elements_at)
    prompt = (
        f"What is the **atomic number** of **{name}**, and what does the atomic number tell us about an atom's nucleus?"
    )
    correct_opt = f"Atomic number {at_num}: It represents the number of protons inside the atom's nucleus."
    distractors = [
        f"Atomic number {at_num + 2}: It represents the number of water molecules inside the cell.",
        f"Atomic number {at_num}: It represents the total number of energy shells in kilograms.",
        f"Atomic number {max(1, at_num - 3)}: It represents the boiling point in Kelvin."
    ]
    options = [correct_opt] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand atomic number:\n"
        f"The atomic number (Z) is the unique identifying number of an element, representing the number of protons "
        f"found in the nucleus of each atom of that element.\n\n"
        f"Conclusion: For {name}, the atomic number is {at_num}."
    )
    return {
        "id": f"ns7_pt_num_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "atomic_number_and_arrangement",
        "question_family_id": "atomic_number_and_arrangement",
        "hints": {
            "tier_1": "Recall the first 20 elements in order.",
            "tier_2": "The atomic number is equal to the number of protons.",
            "tier_3": f"{name} has atomic number {at_num}."
        },
        "misconception_tags": ["atomic_number_mass_confusion"]
    }

def _build_first_twenty_elements(rng: random.Random) -> Dict[str, Any]:
    clues = [
        ("A noble gas with atomic number 2 used in party balloons and deep-sea diving mixtures", "Helium (He)"),
        ("An essential non-metal with atomic number 8 that supports animal respiration and combustion", "Oxygen (O)"),
        ("A lightweight metal with atomic number 13 used in aircraft bodies and beverage cans", "Aluminium (Al)"),
        ("A reactive alkali metal with atomic number 11 that reacts vigorously with water", "Sodium (Na)"),
        ("An alkaline earth metal with atomic number 20 essential for strong human bones and teeth", "Calcium (Ca)")
    ]
    clue, ans = rng.choice(clues)
    prompt = f"Identify the element from the first 20 elements of the Periodic Table based on this clue:\n'{clue}'."
    correct_opt = ans
    distractors = [c[1] for c in clues if c[1] != ans]
    options = [correct_opt] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify from clue:\n"
        f"'{clue}' describes {ans}."
    )
    return {
        "id": f"ns7_pt_twenty_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "first_twenty_elements_identification",
        "question_family_id": "first_twenty_elements_identification",
        "hints": {
            "tier_1": "Check the atomic number and chemical properties given in the clue.",
            "tier_2": "Recall the order H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca.",
            "tier_3": f"The element is {ans}."
        },
        "misconception_tags": ["element_symbol_guess"]
    }

def _build_mendeleev_history(rng: random.Random) -> Dict[str, Any]:
    intros = [
        "In 1869, Russian scientist **Dmitri Mendeleev** developed a revolutionary system to categorize all 63 known chemical elements.",
        "When **Dmitri Mendeleev** organized chemical elements by atomic mass and chemical properties, he created the foundation of modern chemistry.",
        "During the nineteenth century, chemical classification was chaotic until **Dmitri Mendeleev** discovered the periodic law."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"Why is Russian chemist **Dmitri Mendeleev** celebrated as the father of the modern Periodic Table?"
    )
    correct_opt = "He arranged elements by patterns in their properties and left gaps, accurately predicting the properties of undiscovered elements."
    options = [
        correct_opt,
        "He invented all the elements in his home laboratory using electricity.",
        "He discovered that all elements have identical masses and boiling points.",
        "He replaced chemical symbols with arbitrary cartoon drawings."
    ]
    rng.shuffle(options)
    sol = (
        "Historical Achievement of Dmitri Mendeleev (1869/1872):\n"
        "Mendeleev arranged elements in order of atomic mass and chemical families. Crucially, when an element "
        "did not fit the pattern, he had the insight to leave intentional empty gaps in his table and predicted the exact "
        "physical and chemical properties of elements (like Gallium and Germanium) that were discovered years later."
    )
    return {
        "id": f"ns7_pt_mend_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "mendeleev_periodic_table_history",
        "question_family_id": "mendeleev_periodic_table_history",
        "hints": {
            "tier_1": "Think about what Mendeleev did when an element hadn't been discovered yet.",
            "tier_2": "He left spaces and predicted their future discovery.",
            "tier_3": "He left gaps and accurately predicted undiscovered elements."
        },
        "misconception_tags": ["mendeleev_invention_fallacy"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "element_definition_and_symbols": _build_element_symbols,
        "metals_nonmetals_semimetals_classification": _build_metals_nonmetals_semimetals,
        "atomic_number_and_arrangement": _build_atomic_number,
        "first_twenty_elements_identification": _build_first_twenty_elements,
        "mendeleev_periodic_table_history": _build_mendeleev_history
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
