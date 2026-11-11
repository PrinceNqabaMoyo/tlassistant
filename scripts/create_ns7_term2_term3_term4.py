"""
Script to create the remaining 10 Grade 7 Natural Sciences generators:
Term 2:
- ns7_properties_of_materials_generator.py
- ns7_periodic_table_generator.py

Term 3:
- ns7_sources_of_energy_generator.py
- ns7_potential_kinetic_energy_generator.py
- ns7_energy_transfer_generator.py
- ns7_heat_transfer_generator.py
- ns7_heat_insulation_generator.py

Term 4:
- ns7_moon_earth_generator.py
- ns7_sun_earth_generator.py
- ns7_astronomy_history_generator.py
"""

import os

ns_dir = os.path.join("caps-ai-backend", "app", "utils", "natural_sciences")

def write_gen(filename, code):
    path = os.path.join(ns_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Wrote {filename}")

# ============================================================================
# TERM 2: PROPERTIES OF MATERIALS
# ============================================================================
code_properties = '''"""Grade 7 Natural Sciences: Term 2 - Properties of Materials Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/01. Properties of materials.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "physical_properties_malleability_ductility",
    "thermal_and_electrical_conductivity",
    "strength_tensile_and_compressive",
    "boiling_and_melting_points_pure_substances",
    "environmental_impact_and_recycling"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 2/01. Properties of materials.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_malleability_ductility(rng: random.Random) -> Dict[str, Any]:
    props = [
        ("can be hammered, rolled, or pressed into thin flat sheets without shattering (e.g. aluminium foil, corrugated iron roofing)", "Malleability"),
        ("can be drawn out or stretched into long thin flexible wires without snapping (e.g. copper electrical wiring)", "Ductility"),
        ("resists wear, scratching, or denting and lasts a very long time without decaying", "Durability"),
        ("can bend easily without breaking and returns to its original shape", "Flexibility")
    ]
    desc, term = rng.choice(props)
    prompt = f"In material science, which property is specifically defined as the ability of a substance to:\\n'{desc}'?"
    correct_opt = term
    distractors = [p[1] for p in props if p[1] != term]
    options = [correct_opt] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Properties of matter definitions:\\n"
        f"- Malleability: Ability to be hammered into sheets.\\n"
        f"- Ductility: Ability to be drawn into wires.\\n"
        f"- Durability: Resistance to wear/decay.\\n"
        f"- Flexibility: Ability to bend without snapping.\\n\\n"
        f"Conclusion: '{desc}' defines {term}."
    )
    return {
        "id": f"ns7_mat_prop_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "physical_properties_malleability_ductility",
        "question_family_id": "physical_properties_malleability_ductility",
        "hints": {
            "tier_1": "Think about hammering into sheets vs drawing into wires.",
            "tier_2": "Malleable = sheets; Ductile = wires.",
            "tier_3": f"The property is {term}."
        },
        "misconception_tags": ["malleability_ductility_confusion"]
    }

def _build_conductivity(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Copper is used for household electrical cabling, but is coated in a polyvinyl chloride (PVC) plastic sheath.", "Copper is an electrical conductor; PVC plastic is an electrical insulator that prevents shocks."),
        ("Cooking pots are made of stainless steel or cast iron, while the handles are made of Bakelite or silicone.", "Metals are thermal conductors transferring heat to food; Bakelite is a thermal insulator protecting hands from burns."),
        ("Aluminium heat sinks are attached to computer microprocessors.", "Aluminium conducts heat rapidly away from delicate electronic microchips to prevent overheating.")
    ]
    appl, rationale = rng.choice(scenarios)
    prompt = f"Explain the choice of materials in this practical application:\\n'{appl}'\\n\\nWhich statement correctly explains the scientific principle?"
    correct_opt = rationale
    options = [
        correct_opt,
        "Plastics conduct electricity faster than copper wires.",
        "Metals are thermal insulators that trap heat inside cold handles.",
        "All materials conduct heat and electricity at identical rates."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Scientific principles of conductivity:\\n"
        f"- Thermal conductors (metals like Cu, Al, Fe) allow heat to pass easily.\\n"
        f"- Thermal insulators (plastics, wood, rubber) resist the transfer of heat.\\n"
        f"- Electrical conductors allow electric charges to flow; insulators block current.\\n\\n"
        f"Conclusion: {rationale}"
    )
    return {
        "id": f"ns7_mat_cond_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "thermal_and_electrical_conductivity",
        "question_family_id": "thermal_and_electrical_conductivity",
        "hints": {
            "tier_1": "Conductors allow heat/current to pass; insulators block it.",
            "tier_2": "Metals conduct; plastics and rubber insulate.",
            "tier_3": f"The correct explanation is: {rationale}"
        },
        "misconception_tags": ["insulator_conductor_confusion"]
    }

def _build_strength_tensile_compressive(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("Tensile strength", "resisting being pulled apart or stretched under tension (e.g. steel elevator cables, nylon climbing ropes)"),
        ("Compressive strength", "resisting being crushed or pushed together under heavy downward weight (e.g. concrete pillars, kiln-fired building bricks)")
    ]
    strength_type, desc = rng.choice(types)
    prompt = f"Which type of mechanical strength is defined as:\\n'{desc}'?"
    correct_opt = strength_type
    alt_type = "Compressive strength" if strength_type == "Tensile strength" else "Tensile strength"
    options = [correct_opt, alt_type, "Thermal elasticity", "Magnetic permeability"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Distinguish mechanical strengths:\\n"
        f"- Tensile strength: Resistance to pulling forces (tension).\\n"
        f"- Compressive strength: Resistance to crushing forces (compression).\\n\\n"
        f"Conclusion: '{desc}' defines {strength_type}."
    )
    return {
        "id": f"ns7_mat_str_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "strength_tensile_and_compressive",
        "question_family_id": "strength_tensile_and_compressive",
        "hints": {
            "tier_1": "Tension = pulling apart; Compression = crushing together.",
            "tier_2": "Cables have tensile strength; pillars have compressive strength.",
            "tier_3": f"This is {strength_type}."
        },
        "misconception_tags": ["tensile_compressive_confusion"]
    }

def _build_boiling_melting_points(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("Pure water at standard sea-level atmospheric pressure", 0, 100),
        ("Pure ethanol (ethyl alcohol)", -114, 78),
        ("Pure iron metal", 1538, 2862)
    ]
    sub, mp, bp = rng.choice(substances)
    prompt = (
        f"Consider **{sub}**. At sea level, its melting point is {mp}°C and its boiling point is {bp}°C.\\n\\n"
        f"What is the physical state of this substance at a room temperature of 25°C?"
    )
    if 25 < mp:
        state = "Solid"
    elif mp <= 25 <= bp:
        state = "Liquid"
    else:
        state = "Gas"
    correct_opt = f"{state}, because 25°C is {'below the melting point' if state=='Solid' else ('between the melting point and boiling point' if state=='Liquid' else 'above the boiling point')}."
    options = [
        correct_opt,
        "Gas, because all pure substances boil at room temperature.",
        "Solid, because substances are only liquid when heated on a stove.",
        "Plasma, because sea-level pressure ionises all compounds."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Check substance temperature thresholds:\\n"
        f"- Below melting point ({mp}°C): Solid.\\n"
        f"- Between melting point ({mp}°C) and boiling point ({bp}°C): Liquid.\\n"
        f"- Above boiling point ({bp}°C): Gas.\\n\\n"
        f"Step 2: Compare 25°C:\\n"
        f"25°C lies {'below' if 25<mp else ('between' if mp<=25<=bp else 'above')} the phase change boundaries.\\n"
        f"Conclusion: It is a {state}."
    )
    return {
        "id": f"ns7_mat_phase_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "boiling_and_melting_points_pure_substances",
        "question_family_id": "boiling_and_melting_points_pure_substances",
        "hints": {
            "tier_1": "Compare 25°C to the melting and boiling points.",
            "tier_2": "If temp is between MP and BP, it is a liquid.",
            "tier_3": f"At 25°C, the substance is a {state}."
        },
        "misconception_tags": ["phase_change_temp_error"]
    }

def _build_environmental_impact_recycling(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain TWO major environmental problems caused by the widespread use of non-biodegradable plastics, "
        "and state how recycling plastics helps address these issues. (4 marks)"
    )
    sample_answer = (
        "1. Environmental pollution and landfill accumulation: Non-biodegradable plastics do not decompose naturally, "
        "filling up municipal landfills and persisting in ecosystems for centuries where they break into toxic microplastics.\\n"
        "2. Harm to marine wildlife: Discarded plastics wash into rivers and oceans, where sea turtles and fish ingest them or get entangled.\\n"
        "3. Recycling solution: Recycling repurposes existing plastic polymers into new products, conserving crude oil resources and reducing waste sent to landfills."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. Two environmental impacts of plastic waste (e.g. non-decomposition in landfills, harm to marine animals) (2 marks).\\n"
        "2. Role of recycling: Reduces extraction of raw crude oil, cuts landfill waste, and protects natural habitats (2 marks)."
    )
    return {
        "id": f"ns7_mat_env_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "environmental_impact_and_recycling",
        "question_family_id": "environmental_impact_and_recycling",
        "hints": {
            "tier_1": "Think about plastic waste in rivers, oceans, and landfills.",
            "tier_2": "Plastics take centuries to break down and harm wildlife. Recycling reuses plastic to conserve oil.",
            "tier_3": "Mention persistent landfill waste, ingestion by marine animals, and raw resource conservation."
        },
        "misconception_tags": ["biodegradable_plastic_misconception"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "physical_properties_malleability_ductility": _build_malleability_ductility,
        "thermal_and_electrical_conductivity": _build_conductivity,
        "strength_tensile_and_compressive": _build_strength_tensile_compressive,
        "boiling_and_melting_points_pure_substances": _build_boiling_melting_points,
        "environmental_impact_and_recycling": _build_environmental_impact_recycling
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
write_gen("ns7_properties_of_materials_generator.py", code_properties)

# ============================================================================
# TERM 2: PERIODIC TABLE OF ELEMENTS
# ============================================================================
code_periodic = '''"""Grade 7 Natural Sciences: Term 2 - Periodic Table of Elements Generator.
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
        f"Step 1: Chemical symbol convention:\\n"
        f"Chemical symbols are written with the first letter in capital and the second letter (if present) in lowercase.\\n\\n"
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
        f"On the Periodic Table of Elements, which group of elements is characterized as:\\n"
        f"'{desc}'?"
    )
    correct_opt = grp
    options = ["Metals", "Non-metals", "Semi-metals (Metalloids)", "Noble radioactive isotopes"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Classification on the Periodic Table:\\n"
        f"- Left/centre: Metals (shiny, conductors).\\n"
        f"- Upper right: Non-metals (dull, brittle, insulators).\\n"
        f"- Staircase border: Semi-metals / metalloids (semiconductors like Si).\\n\\n"
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
        f"Step 1: Understand atomic number:\\n"
        f"The atomic number (Z) is the unique identifying number of an element, representing the number of protons "
        f"found in the nucleus of each atom of that element.\\n\\n"
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
    prompt = f"Identify the element from the first 20 elements of the Periodic Table based on this clue:\\n'{clue}'."
    correct_opt = ans
    distractors = [c[1] for c in clues if c[1] != ans]
    options = [correct_opt] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify from clue:\\n"
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
    prompt = (
        "Why is Russian chemist **Dmitri Mendeleev** celebrated as the father of the modern Periodic Table?"
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
        "Historical Achievement of Dmitri Mendeleev (1869/1872):\\n"
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
'''
write_gen("ns7_periodic_table_generator.py", code_periodic)

# ============================================================================
# TERM 3: SOURCES OF ENERGY
# ============================================================================
code_sources_energy = '''"""Grade 7 Natural Sciences: Term 3 - Sources of Energy Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/01. Sources of energy.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "renewable_vs_nonrenewable_energy_sources",
    "fossil_fuels_formation_and_types",
    "south_african_coal_dependence_eskom",
    "environmental_impact_greenhouse_gases",
    "alternative_clean_energy_solutions"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 3/01. Sources of energy.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_renewable_vs_nonrenewable(rng: random.Random) -> Dict[str, Any]:
    sources = [
        ("Solar photovoltaic radiation from the Sun", "Renewable source", "replenished naturally on a continuous basis and cannot be permanently exhausted"),
        ("Coal mined from underground seams in Mpumalanga", "Non-renewable source", "takes hundreds of millions of years to form and will eventually be permanently depleted"),
        ("Wind kinetic energy captured by turbine blades in the Eastern Cape", "Renewable source", "replenished constantly by solar atmospheric heating and never runs out"),
        ("Crude petroleum oil extracted from offshore drilling rigs", "Non-renewable source", "a finite fossil fuel that cannot be replaced once combusted")
    ]
    src, cat, expl = rng.choice(sources)
    prompt = f"Classify **{src}** as a renewable or non-renewable energy source, and state the scientific reason."
    correct_opt = f"{cat}, because it is {expl}."
    alt_cat = "Non-renewable source" if cat == "Renewable source" else "Renewable source"
    options = [
        correct_opt,
        f"{alt_cat}, because all commercial power sources are legally classified as identical.",
        f"{alt_cat}, because solar and wind energy produce nuclear radioactive fallout.",
        "Neither, because electricity generation does not depend on natural resources."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand energy resource categories:\\n"
        f"- Renewable: Resources replenished naturally by Earth's cycles (solar, wind, hydro, biomass).\\n"
        f"- Non-renewable: Finite resources consumed faster than Earth can recreate them (coal, oil, gas, uranium).\\n\\n"
        f"Conclusion: {src} is a {cat} because it is {expl}."
    )
    return {
        "id": f"ns7_en_ren_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "renewable_vs_nonrenewable_energy_sources",
        "question_family_id": "renewable_vs_nonrenewable_energy_sources",
        "hints": {
            "tier_1": "Can Earth recreate this resource quickly, or will it run out forever when used up?",
            "tier_2": "Sunlight and wind are inexhaustible; coal and oil are finite fossil fuels.",
            "tier_3": f"This is classified as a {cat}."
        },
        "misconception_tags": ["renewable_clean_infinite_confusion"]
    }

def _build_fossil_fuels_formation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "How did **coal deposits** in South Africa form over geological time?"
    )
    correct_opt = "Ancient swamp forests died millions of years ago, were buried under sediments, and were compressed under immense heat and pressure."
    options = [
        correct_opt,
        "Volcanic magma rapidly cooled on the surface of the ocean over the last decade.",
        "Dead dinosaur skeletons melted into black oil during ancient ice ages.",
        "Rainwater reacted with atmospheric oxygen to form solid black carbon rocks."
    ]
    rng.shuffle(options)
    sol = (
        "Formation of Coal (Carboniferous Period, ~300 million years ago):\\n"
        "1. Ancient giant fern and tree swamps died in waterlogged, oxygen-poor bogs.\\n"
        "2. Layers of mud, silt, and sand buried the organic matter, preventing complete decay.\\n"
        "3. Over millions of years, tectonic pressure and geothermal heat drove out moisture and gases, transforming peat into lignite and bituminous coal."
    )
    return {
        "id": f"ns7_en_coal_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "fossil_fuels_formation_and_types",
        "question_family_id": "fossil_fuels_formation_and_types",
        "hints": {
            "tier_1": "Coal comes from ancient plant swamps, not dinosaur bones.",
            "tier_2": "Heat, pressure, and time over millions of years compressed the plant matter.",
            "tier_3": "Ancient swamp forests were compressed under sediment, heat, and pressure."
        },
        "misconception_tags": ["dinosaur_coal_fallacy"]
    }

def _build_sa_coal_dependence(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In South Africa, the majority of electricity generated by Eskom power stations comes from burning coal. "
        "State ONE reason for this historical dependence and ONE major operational challenge associated with coal-fired power stations. (4 marks)"
    )
    sample_answer = (
        "Historical reason: South Africa possesses vast, easily accessible, and inexpensive domestic bituminous coal reserves, "
        "mainly in Mpumalanga and Limpopo, which allowed the country to build large-scale baseload thermal power stations.\\n"
        "Operational challenge: Burning coal generates severe atmospheric emissions (carbon dioxide, sulfur dioxide, particulate ash), "
        "consumes enormous quantities of cooling water in a water-stressed country, and relies on aging power plants that suffer breakdowns."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. Reason for dependence: Abundant, cheap domestic coal deposits in Mpumalanga/Limpopo (2 marks).\\n"
        "2. Challenge: Air pollution/greenhouse gas emissions, massive water consumption, or breakdowns/maintenance backlog (2 marks)."
    )
    return {
        "id": f"ns7_en_eskom_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "south_african_coal_dependence_eskom",
        "question_family_id": "south_african_coal_dependence_eskom",
        "hints": {
            "tier_1": "Why does SA have so many coal power stations, and what problems do they cause?",
            "tier_2": "Abundant local coal reserves provided cheap baseload; challenges include emissions and water use.",
            "tier_3": "Discuss cheap domestic coal reserves and the resulting greenhouse emissions and maintenance issues."
        },
        "misconception_tags": ["infinite_coal_assumption"]
    }

def _build_environmental_impact(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "What is the primary global environmental concern associated with combusting fossil fuels (coal, petrol, and gas) "
        "for electricity and transport?"
    )
    correct_opt = "It releases massive volumes of carbon dioxide (CO2), intensifying the enhanced greenhouse effect and driving global climate change."
    options = [
        correct_opt,
        "It causes the ozone layer to turn permanently purple across the equator.",
        "It stops the Earth from rotating on its axis every 24 hours.",
        "It creates massive amounts of liquid oxygen that freeze the oceans."
    ]
    rng.shuffle(options)
    sol = (
        "Environmental Impact of Fossil Fuel Combustion:\\n"
        "Combusting hydrocarbons (C + O2 -> CO2) releases trapped ancient carbon into the atmosphere as greenhouse gases. "
        "This traps outgoing infrared radiation, causing global atmospheric warming, rising sea levels, and extreme weather events."
    )
    return {
        "id": f"ns7_en_co2_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "environmental_impact_greenhouse_gases",
        "question_family_id": "environmental_impact_greenhouse_gases",
        "hints": {
            "tier_1": "Think about CO2 and the greenhouse effect.",
            "tier_2": "Combustion produces carbon dioxide which traps atmospheric heat.",
            "tier_3": "It increases CO2, causing the enhanced greenhouse effect and climate change."
        },
        "misconception_tags": ["greenhouse_ozone_confusion"]
    }

def _build_alternative_clean_energy(rng: random.Random) -> Dict[str, Any]:
    alternatives = [
        ("Solar photovoltaic farms in the Northern Cape", "abundant sunny cloudless skies (>300 days per year) generating electricity without emissions"),
        ("Wind turbine farms along the Eastern and Western Cape coastlines", "strong, consistent coastal onshore winds driving turbine generators"),
        ("Hydroelectric pumped-storage schemes (e.g. Drakensberg Pumped Storage)", "pumping water to high reservoirs at night and releasing it through turbines during peak demand")
    ]
    sol_type, adv = rng.choice(alternatives)
    prompt = f"Why is **{sol_type}** a promising alternative energy solution for South Africa?"
    correct_opt = f"It harnesses South Africa's natural geographic advantages ({adv})."
    options = [
        correct_opt,
        "It consumes more coal than standard thermal power stations.",
        "It guarantees that electricity will only work during winter nights.",
        "It replaces all electricity with wood-burning braai fires."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Renewable energy potential in South Africa:\\n"
        f"South Africa has world-class solar irradiance (Northern Cape) and coastal wind regimes (Eastern/Western Cape).\\n\\n"
        f"Conclusion: {sol_type} is effective because {adv}."
    )
    return {
        "id": f"ns7_en_alt_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "alternative_clean_energy_solutions",
        "question_family_id": "alternative_clean_energy_solutions",
        "hints": {
            "tier_1": "Consider South Africa's climate: lots of sunshine and windy coastal plains.",
            "tier_2": "Renewables harness abundant sun and wind to generate clean electricity.",
            "tier_3": f"It harnesses SA's natural geographic conditions ({adv})."
        },
        "misconception_tags": ["renewable_unreliability_myth"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "renewable_vs_nonrenewable_energy_sources": _build_renewable_vs_nonrenewable,
        "fossil_fuels_formation_and_types": _build_fossil_fuels_formation,
        "south_african_coal_dependence_eskom": _build_sa_coal_dependence,
        "environmental_impact_greenhouse_gases": _build_environmental_impact,
        "alternative_clean_energy_solutions": _build_alternative_clean_energy
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
write_gen("ns7_sources_of_energy_generator.py", code_sources_energy)

# ============================================================================
# TERM 3: POTENTIAL AND KINETIC ENERGY
# ============================================================================
code_potential_kinetic = '''"""Grade 7 Natural Sciences: Term 3 - Potential and Kinetic Energy Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/02. Potential and kinetic energy.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "potential_vs_kinetic_energy_concepts",
    "gravitational_potential_energy_factors",
    "chemical_and_elastic_potential_energy",
    "energy_conversions_rollercoaster_and_pendulum",
    "qualitative_kinetic_energy_relationships"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 3/02. Potential and kinetic energy.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_potential_vs_kinetic(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("A heavy boulder perched stationary at the edge of a cliff", "Potential energy (stored energy due to position in a gravitational field)", "Kinetic energy"),
        ("A cheetah sprinting at top speed across the savanna", "Kinetic energy (energy possessed by an object due to its motion)", "Potential energy"),
        ("A stretched rubber catapult loaded with a stone", "Potential energy (stored elastic energy ready to be released)", "Kinetic energy"),
        ("A soccer ball flying through the air toward the goal", "Both kinetic energy (motion) and gravitational potential energy (height above ground)", "Chemical energy exclusively")
    ]
    scen, correct_type, wrong_type = rng.choice(examples)
    prompt = f"Consider: **{scen}**.\\n\\nWhich form of mechanical energy is primarily represented?"
    correct_opt = correct_type
    options = [correct_opt, wrong_type, "Nuclear radiant fission", "Geothermal tectonic energy"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand energy definitions:\\n"
        f"- Potential Energy: Energy stored within an object due to its position, state, or chemical configuration.\\n"
        f"- Kinetic Energy: The energy possessed by an object due to its physical motion.\\n\\n"
        f"Conclusion: '{scen}' represents {correct_type}."
    )
    return {
        "id": f"ns7_pk_mech_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "potential_vs_kinetic_energy_concepts",
        "question_family_id": "potential_vs_kinetic_energy_concepts",
        "hints": {
            "tier_1": "Is the object moving (kinetic) or stationary with stored energy (potential)?",
            "tier_2": "Motion is kinetic; stored/elevated is potential.",
            "tier_3": f"This scenario primarily demonstrates {correct_type}."
        },
        "misconception_tags": ["stored_motion_energy_confusion"]
    }

def _build_gravitational_factors(rng: random.Random) -> Dict[str, Any]:
    h1 = rng.choice([2, 5, 10])
    h2 = h1 * 2
    prompt = (
        f"Two identical 5 kg bricks, Brick A and Brick B, are lifted onto shelves in a workshop. "
        f"Brick A is placed at a height of {h1} m, while Brick B is placed at {h2} m.\\n\\n"
        f"How does the **gravitational potential energy** of Brick B compare to Brick A, and why?"
    )
    correct_opt = f"Brick B has twice as much potential energy as Brick A, because gravitational potential energy is directly proportional to height."
    options = [
        correct_opt,
        "Brick B has less potential energy than Brick A, because higher objects lose mass.",
        "Both bricks have identical potential energy, because they have the same 5 kg mass.",
        "Neither brick has potential energy, because they are not moving."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Formula for gravitational potential energy:\\n"
        f"Ep = m × g × h (where m = mass, g = gravitational acceleration, h = height).\\n\\n"
        f"Step 2: Compare heights:\\n"
        f"Brick B is at {h2} m, which is twice {h1} m. Since mass and gravity are constant, Ep doubles with height.\\n\\n"
        f"Conclusion: Brick B has twice the gravitational potential energy of Brick A."
    )
    return {
        "id": f"ns7_pk_grav_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "gravitational_potential_energy_factors",
        "question_family_id": "gravitational_potential_energy_factors",
        "hints": {
            "tier_1": "Potential energy increases as height increases.",
            "tier_2": "Ep = mgh. If height doubles, potential energy doubles.",
            "tier_3": "Brick B has twice the potential energy because its height is doubled."
        },
        "misconception_tags": ["potential_energy_height_independence"]
    }

def _build_chemical_elastic_energy(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Energy stored in food (like a banana or slice of bread) and torch batteries", "Chemical potential energy", "stored in the chemical bonds between atoms and released during cellular respiration or chemical reactions"),
        ("Energy stored in a compressed mattress spring or stretched rubber band", "Elastic potential energy", "stored when an elastic material is deformed, ready to snap back to its rest shape")
    ]
    item_desc, form, expl = rng.choice(cases)
    prompt = f"What specific form of potential energy is found in:\\n'{item_desc}'?"
    correct_opt = form
    alt_form = "Elastic potential energy" if form == "Chemical potential energy" else "Chemical potential energy"
    options = [correct_opt, alt_form, "Gravitational potential energy", "Kinetic friction"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Classify stored potential energy types:\\n"
        f"- Chemical potential: Energy in chemical bonds (food, fuels, batteries).\\n"
        f"- Elastic potential: Energy in stretched/compressed objects.\\n\\n"
        f"Conclusion: '{item_desc}' is {form} because it is {expl}."
    )
    return {
        "id": f"ns7_pk_chem_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "chemical_and_elastic_potential_energy",
        "question_family_id": "chemical_and_elastic_potential_energy",
        "hints": {
            "tier_1": "Is it stored in food/batteries (chemical) or stretched springs/rubber (elastic)?",
            "tier_2": "Food and batteries hold chemical energy; springs hold elastic energy.",
            "tier_3": f"This is {form}."
        },
        "misconception_tags": ["chemical_elastic_confusion"]
    }

def _build_energy_conversions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Trace the energy transformations that take place as a pendulum swings from its highest release point "
        "(Position 1), passes through the lowest centre point (Position 2), and rises to the opposite high point (Position 3). (4 marks)"
    )
    sample_answer = (
        "1. Position 1 (Highest point): The pendulum is momentarily stationary at maximum height, possessing maximum gravitational potential energy and zero kinetic energy.\\n"
        "2. Moving toward Position 2: As it falls, gravitational potential energy is converted into kinetic energy, and its speed increases.\\n"
        "3. Position 2 (Lowest point): The pendulum reaches maximum speed and lowest height, possessing maximum kinetic energy and minimum potential energy.\\n"
        "4. Rising to Position 3: Kinetic energy is converted back into gravitational potential energy until it stops momentarily at maximum height."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. Position 1: Maximum gravitational potential energy, zero kinetic (1 mark).\\n"
        "2. Transition: Potential converted to kinetic as speed increases (1 mark).\\n"
        "3. Position 2: Maximum kinetic energy, minimum potential energy (1 mark).\\n"
        "4. Position 3: Kinetic converted back into potential energy at maximum height (1 mark)."
    )
    return {
        "id": f"ns7_pk_conv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "energy_conversions_rollercoaster_and_pendulum",
        "question_family_id": "energy_conversions_rollercoaster_and_pendulum",
        "hints": {
            "tier_1": "At the top it has potential energy; at the bottom it has maximum speed (kinetic energy).",
            "tier_2": "Trace how potential energy turns into kinetic energy and back into potential energy.",
            "tier_3": "Mention max potential at top, max kinetic at bottom, and continuous conversion."
        },
        "misconception_tags": ["pendulum_energy_loss_confusion"]
    }

def _build_qualitative_kinetic(rng: random.Random) -> Dict[str, Any]:
    v1 = rng.choice([40, 60])
    v2 = v1 * 2
    prompt = (
        f"A delivery minibus travels down a highway at {v1} km/h, then accelerates to {v2} km/h.\\n\\n"
        f"What happens to the minibus's **kinetic energy** as its speed increases, and why?"
    )
    correct_opt = "The kinetic energy increases substantially, because kinetic energy depends directly on the square of the speed."
    options = [
        correct_opt,
        "The kinetic energy decreases, because moving faster drains the engine's weight.",
        "The kinetic energy remains completely unchanged, because the mass of the minibus did not change.",
        "The kinetic energy converts immediately into nuclear radioactive energy."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Kinetic energy relationship:\\n"
        f"Ek = 1/2 × m × v^2 (where m = mass, v = speed).\\n\\n"
        f"Step 2: Effect of increasing speed:\\n"
        f"Kinetic energy increases with the square of speed. When speed doubles from {v1} to {v2} km/h, kinetic energy quadruples (2^2 = 4 times).\\n\\n"
        f"Conclusion: Kinetic energy increases substantially with speed."
    )
    return {
        "id": f"ns7_pk_speed_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "qualitative_kinetic_energy_relationships",
        "question_family_id": "qualitative_kinetic_energy_relationships",
        "hints": {
            "tier_1": "Does a faster vehicle have more or less energy of motion?",
            "tier_2": "Kinetic energy increases with speed: Ek = 1/2 m v^2.",
            "tier_3": "Kinetic energy increases with speed squared."
        },
        "misconception_tags": ["kinetic_speed_independence"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "potential_vs_kinetic_energy_concepts": _build_potential_vs_kinetic,
        "gravitational_potential_energy_factors": _build_gravitational_factors,
        "chemical_and_elastic_potential_energy": _build_chemical_elastic_energy,
        "energy_conversions_rollercoaster_and_pendulum": _build_energy_conversions,
        "qualitative_kinetic_energy_relationships": _build_qualitative_kinetic
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
write_gen("ns7_potential_kinetic_energy_generator.py", code_potential_kinetic)

# ============================================================================
# TERM 3: ENERGY TRANSFER TO SURROUNDINGS
# ============================================================================
code_energy_transfer = '''"""Grade 7 Natural Sciences: Term 3 - Energy Transfer to Surroundings Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/03. Energy transfer to surroundings.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "law_of_conservation_of_energy",
    "useful_vs_wasted_energy_output",
    "energy_chains_and_flow_diagrams",
    "sankey_diagrams_energy_efficiency",
    "thermal_dissipation_to_surroundings"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 3/03. Energy transfer to surroundings.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_conservation_law(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "State the **Law of Conservation of Energy** as formulated in natural science."
    )
    correct_opt = "Energy cannot be created or destroyed; it can only be transferred or transformed from one form to another, with total energy remaining constant."
    options = [
        correct_opt,
        "Energy is permanently destroyed whenever electrical appliances get hot.",
        "Energy is spontaneously created out of nothing whenever a motor is switched on.",
        "Total energy in the universe decreases by 10% each year due to battery usage."
    ]
    rng.shuffle(options)
    sol = (
        "Law of Conservation of Energy (First Law of Thermodynamics):\\n"
        "Energy cannot be created or destroyed. In any closed system, the total amount of energy remains constant. "
        "When energy appears to be 'lost', it has simply been transformed into less useful forms (typically heat and sound dissipated into the surroundings)."
    )
    return {
        "id": f"ns7_trans_law_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "law_of_conservation_of_energy",
        "question_family_id": "law_of_conservation_of_energy",
        "hints": {
            "tier_1": "Can energy be created out of nothing or destroyed completely?",
            "tier_2": "Energy only changes form; total energy never changes.",
            "tier_3": "Energy cannot be created or destroyed, only transformed."
        },
        "misconception_tags": ["energy_destruction_fallacy"]
    }

def _build_useful_vs_wasted(rng: random.Random) -> Dict[str, Any]:
    appliances = [
        ("an incandescent filament lightbulb", "Electrical energy", "Light energy (illumination)", "Thermal heat energy dissipated to surrounding air"),
        ("an electric blender in a kitchen", "Electrical energy", "Kinetic mechanical energy (spinning blades)", "Sound energy (noise) and thermal heat in the motor"),
        ("a petrol car engine", "Chemical potential energy in petrol", "Kinetic motion energy of the wheels", "Heat radiated from exhaust/radiator and loud engine sound")
    ]
    app, input_e, useful, wasted = rng.choice(appliances)
    prompt = (
        f"In **{app}**, electrical/chemical energy is supplied as input.\\n\\n"
        f"Which pair correctly identifies the **useful energy output** versus the **wasted energy output**?"
    )
    correct_opt = f"Useful: {useful} | Wasted: {wasted}"
    options = [
        correct_opt,
        f"Useful: {wasted} | Wasted: {useful}",
        "Both outputs are 100% useful with zero energy dissipation",
        "Neither output occurs because energy disappears upon entry"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify purpose of appliance:\\n"
        f"- The intended purpose of {app} defines the useful energy: {useful}.\\n"
        f"- Unintended, unavoidable by-products represent wasted energy: {wasted}.\\n\\n"
        f"Conclusion: Useful is {useful}; Wasted is {wasted}."
    )
    return {
        "id": f"ns7_trans_use_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "useful_vs_wasted_energy_output",
        "question_family_id": "useful_vs_wasted_energy_output",
        "hints": {
            "tier_1": "What was the appliance designed to do? That is the useful energy.",
            "tier_2": "Heat and noise that do not contribute to the main task are wasted energy.",
            "tier_3": f"Useful: {useful}; Wasted: {wasted}."
        },
        "misconception_tags": ["useful_wasted_inversion"]
    }

def _build_energy_chains(rng: random.Random) -> Dict[str, Any]:
    chains = [
        ("Hydroelectric power plant", "Gravitational potential energy (elevated water) → Kinetic energy (flowing water through turbine) → Electrical energy (generator)"),
        ("Coal-fired thermal power station", "Chemical potential energy (coal) → Thermal energy (boiling steam) → Kinetic energy (steam turbine) → Electrical energy (generator)"),
        ("Solar watch", "Radiant solar light energy → Electrical energy (photovoltaic cell) → Kinetic mechanical energy (moving watch hands)")
    ]
    device, chain = rng.choice(chains)
    prompt = f"Which sequence correctly outlines the **energy chain (flow diagram)** for a **{device}**?"
    correct_opt = chain
    options = [
        correct_opt,
        "Electrical energy → Nuclear energy → Chemical energy",
        "Kinetic energy → Sound energy → Gravitational potential energy",
        "Thermal energy → Solar energy → Chemical coal energy"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Trace the transformation path:\\n"
        f"For a {device}, energy converts in the sequence:\\n"
        f"{chain}."
    )
    return {
        "id": f"ns7_trans_chain_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "energy_chains_and_flow_diagrams",
        "question_family_id": "energy_chains_and_flow_diagrams",
        "hints": {
            "tier_1": "Trace where energy starts and what it transforms into step by step.",
            "tier_2": "Follow the sequence of components from fuel/source to output.",
            "tier_3": f"The chain is {chain}."
        },
        "misconception_tags": ["energy_chain_order_reversal"]
    }

def _build_sankey_diagrams(rng: random.Random) -> Dict[str, Any]:
    in_e = 100
    useful_e = rng.choice([15, 20, 25, 75, 80])
    wasted_e = in_e - useful_e
    prompt = (
        f"An energy Sankey diagram tracks an appliance supplied with {in_e} J of electrical energy. "
        f"The diagram shows {useful_e} J directed to useful output and {wasted_e} J curving away into wasted heat.\\n\\n"
        f"Calculate the **energy efficiency percentage** of this appliance."
    )
    eff = (useful_e / in_e) * 100
    correct_opt = f"{eff:.0f}%"
    options = [f"{eff:.0f}%", f"{wasted_e:.0f}%", f"{100 - eff/2:.0f}%", f"{eff/2:.0f}%"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Formula for energy efficiency:\\n"
        f"Efficiency = (Useful Energy Output / Total Energy Input) × 100%\\n\\n"
        f"Step 2: Calculation:\\n"
        f"Efficiency = ({useful_e} J / {in_e} J) × 100% = {eff:.0f}%."
    )
    return {
        "id": f"ns7_trans_eff_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "sankey_diagrams_energy_efficiency",
        "question_family_id": "sankey_diagrams_energy_efficiency",
        "hints": {
            "tier_1": "Efficiency = (Useful output / Total input) × 100%.",
            "tier_2": f"Divide {useful_e} by {in_e} and multiply by 100.",
            "tier_3": f"The efficiency is {eff:.0f}%."
        },
        "misconception_tags": ["efficiency_wasted_ratio_error"]
    }

def _build_thermal_dissipation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain what is meant by the phrase 'energy is dissipated to the surroundings', "
        "and explain why this dissipated energy cannot easily be captured to do useful work. (4 marks)"
    )
    sample_answer = (
        "Dissipated energy refers to energy that spreads out into the surrounding environment, primarily in the form of "
        "low-temperature heat and sound waves. Because this thermal energy spreads thinly across billions of air and surface molecules, "
        "it becomes disordered and dispersed (low grade), meaning it cannot easily be concentrated back to drive engines or perform mechanical work."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. Definition of dissipation: Energy spreads out into the surrounding air/environment as low-temperature heat/sound (2 marks).\\n"
        "2. Irreversibility: Thermal energy becomes diluted and disordered (entropy), making it impossible to concentrate back into useful work (2 marks)."
    )
    return {
        "id": f"ns7_trans_diss_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "thermal_dissipation_to_surroundings",
        "question_family_id": "thermal_dissipation_to_surroundings",
        "hints": {
            "tier_1": "Think about heat escaping into the air and spreading out.",
            "tier_2": "Dissipated energy spreads out as low-temperature heat that is too diluted to concentrate back.",
            "tier_3": "Explain that energy spreads into surrounding air molecules and becomes too disordered to recapture."
        },
        "misconception_tags": ["dissipated_energy_disappearance_myth"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "law_of_conservation_of_energy": _build_conservation_law,
        "useful_vs_wasted_energy_output": _build_useful_vs_wasted,
        "energy_chains_and_flow_diagrams": _build_energy_chains,
        "sankey_diagrams_energy_efficiency": _build_sankey_diagrams,
        "thermal_dissipation_to_surroundings": _build_thermal_dissipation
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
write_gen("ns7_energy_transfer_generator.py", code_energy_transfer)

# ============================================================================
# TERM 3: HEAT ENERGY TRANSFER
# ============================================================================
code_heat_transfer = '''"""Grade 7 Natural Sciences: Term 3 - Heat Energy Transfer Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/03. Heat Energy transfer.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "conduction_in_solids_mechanics",
    "convection_currents_in_fluids",
    "radiation_through_vacuums",
    "comparing_three_heat_transfer_modes",
    "heat_transfer_practical_experiments"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 3/03. Heat Energy transfer.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_conduction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A metal teaspoon is placed in a hot cup of tea. After two minutes, the top of the handle feels hot.\\n\\n"
        "How does heat transfer through the metal spoon by **conduction** at the particle level?"
    )
    correct_opt = "Particles in the hot liquid vibrate faster and collide with neighbouring metal particles, transferring kinetic energy along the spoon."
    options = [
        correct_opt,
        "Hot particles from the bottom of the spoon physically detach and swim up to the handle.",
        "The spoon emits bright visible gamma rays that heat the handle from the outside.",
        "Cold particles in the handle are absorbed into the tea and disappear forever."
    ]
    rng.shuffle(options)
    sol = (
        "Mechanism of Thermal Conduction:\\n"
        "1. Conduction occurs mainly in solids where particles are packed tightly in fixed positions.\\n"
        "2. Thermal energy causes particles at the heated end to vibrate more vigorously.\\n"
        "3. These vibrating particles collide with neighbouring particles, passing kinetic energy along the material.\\n"
        "4. In metals, delocalised free electrons also move rapidly through the lattice, transferring heat much faster."
    )
    return {
        "id": f"ns7_ht_cond_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "conduction_in_solids_mechanics",
        "question_family_id": "conduction_in_solids_mechanics",
        "hints": {
            "tier_1": "Think about particles vibrating and bumping into their neighbours.",
            "tier_2": "In solids, particles don't move from place to place; they pass vibrations through collisions.",
            "tier_3": "Vibrating particles collide with neighbouring particles, transferring kinetic energy."
        },
        "misconception_tags": ["particle_movement_conduction_error"]
    }

def _build_convection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain how a **convection current** forms when water is heated at the bottom of a pot on an electric stove. (4 marks)"
    )
    sample_answer = (
        "1. Heating and expansion: Water at the bottom heats up, its particles gain kinetic energy and spread further apart, causing the warm water to expand.\\n"
        "2. Density change: Because the warm water expands, its density decreases (it becomes less dense than surrounding water).\\n"
        "3. Rising: The less dense warm water rises towards the surface.\\n"
        "4. Circulation: Denser, cooler water at the surface sinks to the bottom to take its place, where it is heated, creating a continuous circulating convection current."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. Water at bottom warms, particles spread out and water expands (1 mark).\\n"
        "2. Warm water becomes less dense (1 mark).\\n"
        "3. Less dense warm water rises (1 mark).\\n"
        "4. Cooler, denser water sinks, forming a continuous circular flow (convection current) (1 mark)."
    )
    return {
        "id": f"ns7_ht_conv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "convection_currents_in_fluids",
        "question_family_id": "convection_currents_in_fluids",
        "hints": {
            "tier_1": "Warm fluid expands -> less dense -> rises; cool fluid -> denser -> sinks.",
            "tier_2": "Follow the cycle: warm liquid expands, density drops, rises; cooler liquid sinks to replace it.",
            "tier_3": "Explain expansion, lower density, rising of warm water, and sinking of cool dense water."
        },
        "misconception_tags": ["heat_rises_vs_warm_fluid_density"]
    }

def _build_radiation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "How does heat from the Sun travel through the vacuum of outer space to reach the Earth?"
    )
    correct_opt = "By thermal radiation (infrared electromagnetic waves), which does not require any particles or physical medium to travel."
    options = [
        correct_opt,
        "By thermal conduction through millions of kilometres of solid copper pipes in space.",
        "By convection currents carried by strong winds blowing through the vacuum of space.",
        "By sound waves travelling through the planetary magnetic field."
    ]
    rng.shuffle(options)
    sol = (
        "Thermal Radiation in a Vacuum:\\n"
        "Conduction and convection both require particles (matter) to transfer heat. Outer space is a vacuum containing "
        "no particles. Radiation transfers thermal energy via electromagnetic waves (infrared radiation), which can travel "
        "freely across empty space at the speed of light."
    )
    return {
        "id": f"ns7_ht_rad_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "radiation_through_vacuums",
        "question_family_id": "radiation_through_vacuums",
        "hints": {
            "tier_1": "Can conduction or convection work without any particles in space?",
            "tier_2": "Only radiation can travel through a vacuum without particles.",
            "tier_3": "Thermal radiation travels as electromagnetic waves through a vacuum."
        },
        "misconception_tags": ["space_convection_fallacy"]
    }

def _build_comparing_modes(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Warming hands in front of an glowing electric fireplace without touching it", "Radiation"),
        ("A hot-air balloon rising gracefully into the morning sky", "Convection"),
        ("An iron pressing collar seams on a cotton shirt", "Conduction"),
        ("Sea breezes blowing inland along the Durban coast on a hot sunny day", "Convection")
    ]
    scen, mode = rng.choice(cases)
    prompt = f"Identify the primary mode of heat transfer occurring in this scenario:\\n'{scen}'."
    correct_opt = mode
    options = ["Conduction", "Convection", "Radiation", "Sublimation"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Check mechanism:\\n"
        f"- Conduction = direct contact through solids.\\n"
        f"- Convection = bulk movement of fluid (liquid/gas).\\n"
        f"- Radiation = infrared waves across air or vacuum.\\n\\n"
        f"Conclusion: '{scen}' operates primarily by {mode}."
    )
    return {
        "id": f"ns7_ht_comp_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "comparing_three_heat_transfer_modes",
        "question_family_id": "comparing_three_heat_transfer_modes",
        "hints": {
            "tier_1": "Is heat transferring through physical contact (solid), moving fluid (gas/liquid), or radiating rays?",
            "tier_2": "Solid contact = conduction; fluid currents = convection; radiant rays = radiation.",
            "tier_3": f"This is an example of {mode}."
        },
        "misconception_tags": ["heat_transfer_mode_confusion"]
    }

def _build_experiments(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a laboratory investigation, learners test the absorption of radiant heat by placing thermometers into two identical cans: "
        "one painted matte black and the other painted shiny silver, placed equidistant from a radiant heater.\\n\\n"
        "Which can will show the fastest temperature increase, and why?"
    )
    correct_opt = "The matte black can, because dark matte surfaces are excellent absorbers of radiant heat, whereas shiny silver surfaces reflect radiation."
    options = [
        correct_opt,
        "The shiny silver can, because shiny surfaces trap and amplify infrared rays.",
        "Both cans will heat up identically, because surface colour has no effect on thermal absorption.",
        "Neither can will heat up, because heat cannot transfer across air."
    ]
    rng.shuffle(options)
    sol = (
        "Principles of Thermal Absorption and Reflection:\\n"
        "- Dark, matte (dull) surfaces are excellent absorbers and emitters of radiant heat.\\n"
        "- Light, shiny surfaces are excellent reflectors and poor absorbers of radiant heat.\\n\\n"
        "Conclusion: The black can absorbs radiant energy much faster, heating up first."
    )
    return {
        "id": f"ns7_ht_exp_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "heat_transfer_practical_experiments",
        "question_family_id": "heat_transfer_practical_experiments",
        "hints": {
            "tier_1": "Do dark clothes feel hotter in the sun than white clothes?",
            "tier_2": "Black absorbs radiant heat; silver reflects it.",
            "tier_3": "The matte black can absorbs radiation fastest."
        },
        "misconception_tags": ["black_surface_reflection_fallacy"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "conduction_in_solids_mechanics": _build_conduction,
        "convection_currents_in_fluids": _build_convection,
        "radiation_through_vacuums": _build_radiation,
        "comparing_three_heat_transfer_modes": _build_comparing_modes,
        "heat_transfer_practical_experiments": _build_experiments
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
write_gen("ns7_heat_transfer_generator.py", code_heat_transfer)

# ============================================================================
# TERM 3: HEAT INSULATION AND ENERGY SAVING
# ============================================================================
code_heat_insulation = '''"""Grade 7 Natural Sciences: Term 3 - Heat Insulation and Energy Saving Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/04. Heat insulation and energy saving.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "thermal_insulators_definition_and_examples",
    "vacuum_flask_design_and_mechanics",
    "passive_solar_building_design",
    "household_energy_saving_strategies",
    "animal_thermal_adaptations"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 3/04. Heat insulation and energy saving.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_thermal_insulators(rng: random.Random) -> Dict[str, Any]:
    materials = [
        ("Glass fibre ceiling batts", "traps pockets of still air, which is a very poor thermal conductor, preventing heat loss through the roof in winter"),
        ("Expanded polystyrene cooler box", "contains millions of microscopic trapped air bubbles that resist the conduction of heat into the cold interior"),
        ("Thick woollen winter blankets", "the crimped wool fibres trap warm air close to the human body, reducing convective and conductive heat loss"),
        ("Double-glazed window panes", "a sealed air or argon gas gap between two glass sheets prevents conductive heat transfer between inside and outside")
    ]
    mat, role = rng.choice(materials)
    prompt = f"Why is **{mat}** an effective thermal insulator?"
    correct_opt = f"Because it {role}."
    options = [
        correct_opt,
        "Because it produces its own internal electrical heat via nuclear fusion.",
        "Because it converts incoming heat into liquid water.",
        "Because it conducts thermal energy ten times faster than solid silver."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Principles of thermal insulation:\\n"
        f"Gases like air are extremely poor conductors of heat if prevented from circulating.\\n"
        f"Materials like {mat} work because they {role}."
    )
    return {
        "id": f"ns7_ins_mat_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "thermal_insulators_definition_and_examples",
        "question_family_id": "thermal_insulators_definition_and_examples",
        "hints": {
            "tier_1": "Think about trapped air pockets that resist heat flow.",
            "tier_2": "Air is a poor conductor; trapping it prevents conduction and convection.",
            "tier_3": f"It works because it {role}."
        },
        "misconception_tags": ["insulator_active_heating_myth"]
    }

def _build_vacuum_flask(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A double-walled vacuum flask keeps hot drinks hot and cold drinks cold for hours. "
        "Explain how the flask's design features minimise all THREE modes of heat transfer: conduction, convection, and radiation. (6 marks)"
    )
    sample_answer = (
        "1. Conduction and Convection minimised by the vacuum: The space between the inner and outer glass/steel walls is an evacuated vacuum with all air removed. Because conduction and convection both require particles to transfer thermal energy, heat cannot travel across this vacuum.\\n"
        "2. Radiation minimised by silvered walls: The internal walls are coated in reflective silvering. Shiny surfaces reflect radiant infrared heat back into a hot liquid (or reflect external radiation away from a cold liquid).\\n"
        "3. Convection prevented by the insulating stopper: The tight plastic or cork stopper prevents warm air/steam from rising out of the top by convection."
    )
    sol = (
        "Marking Rubric (2 marks per heat transfer mode, total 6 marks):\\n"
        "1. Vacuum prevents conduction and convection because there are no particles (2 marks).\\n"
        "2. Silvered reflective lining reflects infrared radiation back into flask (2 marks).\\n"
        "3. Tight insulating stopper stops convective heat loss through the opening (2 marks)."
    )
    return {
        "id": f"ns7_ins_flask_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 6,
        "subskill": "vacuum_flask_design_and_mechanics",
        "question_family_id": "vacuum_flask_design_and_mechanics",
        "hints": {
            "tier_1": "Address each feature: vacuum, silver lining, and stopper.",
            "tier_2": "Vacuum stops conduction and convection; silver stops radiation; stopper stops convective escape.",
            "tier_3": "Explain how the vacuum, silvered lining, and stopper counteract each specific mode of heat transfer."
        },
        "misconception_tags": ["vacuum_radiation_blocking_fallacy"]
    }

def _build_passive_solar(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In South Africa (Southern Hemisphere), which architectural design feature allows a house to stay naturally warmer in winter and cooler in summer?"
    )
    correct_opt = "Facing main living area windows towards the North with calculated roof overhangs that block high summer sun while admitting low winter sun."
    options = [
        correct_opt,
        "Facing all windows strictly South to catch maximum direct midday sunlight in winter.",
        "Painting all external walls matte black and removing the ceiling entirely.",
        "Installing single-pane unshaded windows facing west to maximize extreme afternoon heat."
    ]
    rng.shuffle(options)
    sol = (
        "Principles of Passive Solar Building Design in the Southern Hemisphere:\\n"
        "In South Africa, the sun is always in the northern sky at solar noon.\\n"
        "1. North-facing windows capture maximum winter solar radiation when the sun is at a low angle.\\n"
        "2. Roof overhangs shade the windows during summer when the sun is high overhead, keeping the house cool."
    )
    return {
        "id": f"ns7_ins_solar_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "passive_solar_building_design",
        "question_family_id": "passive_solar_building_design",
        "hints": {
            "tier_1": "In South Africa, which direction does the midday sun face?",
            "tier_2": "The sun is in the north in SA. North-facing windows let in winter sun.",
            "tier_3": "North-facing windows with roof overhangs provide natural seasonal temperature control."
        },
        "misconception_tags": ["south_facing_sun_confusion_southern_hemisphere"]
    }

def _build_household_energy_saving(rng: random.Random) -> Dict[str, Any]:
    strategies = [
        ("Installing an insulating geyser blanket around an electric hot water cylinder", "Reduces heat dissipation from the water tank into the surrounding roof space, saving up to 20% on geyser electricity."),
        ("Replacing standard incandescent filament lightbulbs with Light Emitting Diodes (LEDs)", "LEDs convert over 85% of electrical energy into useful light rather than wasting it as heat."),
        ("Installing thick insulated curtains and closing them at sunset in winter", "Creates an insulating dead-air buffer against cold glass window panes, preventing indoor heat loss.")
    ]
    strat, benefit = rng.choice(strategies)
    prompt = f"How does **{strat}** save household electrical energy?"
    correct_opt = benefit
    options = [
        correct_opt,
        "It eliminates the need for any electricity by generating free perpetual energy.",
        "It forces the municipal electric grid to run backwards at night.",
        "It increases thermal heat waste to heat the neighborhood."
    ]
    rng.shuffle(options)
    sol = (
        f"Energy Conservation in Households:\\n"
        f"{strat} works because {benefit}"
    )
    return {
        "id": f"ns7_ins_home_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "household_energy_saving_strategies",
        "question_family_id": "household_energy_saving_strategies",
        "hints": {
            "tier_1": "Think about cutting down on wasted heat loss.",
            "tier_2": "Insulation stops heat leaking out; efficient bulbs produce light instead of heat.",
            "tier_3": f"{benefit}"
        },
        "misconception_tags": ["geyser_blanket_waste_confusion"]
    }

def _build_animal_thermal_adaptations(rng: random.Random) -> Dict[str, Any]:
    animals = [
        ("The African penguin in cold sub-Antarctic waters", "a dense double layer of waterproof, overlapping feathers and a thick subcutaneous blubber fat layer to insulate against freezing seas"),
        ("The Arctic fox in sub-zero tundra", "thick hollow fur that traps insulating air, small compact rounded ears to reduce surface-area-to-volume heat loss"),
        ("The African elephant in hot savanna climates", "enormous vascularized ear flaps that act as thermal radiators to cool blood through convection and radiation")
    ]
    animal, adaptation = rng.choice(animals)
    prompt = f"Consider **{animal}**. How does its physiological adaptation ({adaptation}) regulate body temperature?"
    correct_opt = f"It controls the rate of conductive, convective, or radiative heat transfer with the external environment."
    options = [
        correct_opt,
        "It completely stops all internal blood circulation during hot or cold weather.",
        "It allows the animal to absorb zero oxygen while staying underwater for years.",
        "It transforms the animal from a mammal into a cold-blooded reptile."
    ]
    rng.shuffle(options)
    sol = (
        f"Thermoregulation Adaptations in Animals:\\n"
        f"{animal} uses {adaptation} to balance metabolic heat production with environmental heat exchange, "
        f"preventing hypothermia or hyperthermia."
    )
    return {
        "id": f"ns7_ins_anim_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "animal_thermal_adaptations",
        "question_family_id": "animal_thermal_adaptations",
        "hints": {
            "tier_1": "Does this adaptation trap heat (insulate) or shed heat (radiate)?",
            "tier_2": "Blubber and fur insulate against cold; large ears radiate heat in the heat.",
            "tier_3": "It regulates heat transfer rates with the environment."
        },
        "misconception_tags": ["blubber_food_insulation_confusion"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "thermal_insulators_definition_and_examples": _build_thermal_insulators,
        "vacuum_flask_design_and_mechanics": _build_vacuum_flask,
        "passive_solar_building_design": _build_passive_solar,
        "household_energy_saving_strategies": _build_household_energy_saving,
        "animal_thermal_adaptations": _build_animal_thermal_adaptations
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
write_gen("ns7_heat_insulation_generator.py", code_heat_insulation)

# ============================================================================
# TERM 4: RELATIONSHIP OF THE MOON TO THE EARTH
# ============================================================================
code_moon_earth = '''"""Grade 7 Natural Sciences: Term 4 - Relationship of the Moon to the Earth Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the moon to the earth.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "moon_orbit_and_revolution_period",
    "lunar_phases_sequence_and_causes",
    "ocean_tides_spring_and_neap",
    "lunar_and_solar_eclipses_mechanics",
    "gravity_and_weight_on_the_moon"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the moon to the earth.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_moon_orbit(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Approximately how long does it take for the Moon to complete ONE full orbit (revolution) around the Earth, "
        "and does the Moon emit its own light?"
    )
    correct_opt = "Approximately 28 days (one month): The Moon does not emit light; it reflects sunlight."
    options = [
        correct_opt,
        "Exactly 365.25 days: The Moon burns nuclear fuel like a small star.",
        "Exactly 24 hours: The Moon generates light from hot volcanic magma.",
        "Approximately 12 hours: The Moon is completely transparent to cosmic rays."
    ]
    rng.shuffle(options)
    sol = (
        "Moon Orbital Mechanics:\\n"
        "1. The Moon revolves around Earth in an elliptical orbit taking approximately 27.3 to 29.5 days (~28 days / 1 lunar cycle).\\n"
        "2. The Moon is a non-luminous rocky body that does not generate its own light; it reflects light from the Sun."
    )
    return {
        "id": f"ns7_moon_orb_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "moon_orbit_and_revolution_period",
        "question_family_id": "moon_orbit_and_revolution_period",
        "hints": {
            "tier_1": "Think about the word 'month' which comes from 'moon'.",
            "tier_2": "The Moon takes ~28 days to orbit and reflects sunlight.",
            "tier_3": "Approximately 28 days, and it reflects sunlight."
        },
        "misconception_tags": ["moon_luminous_body_fallacy"]
    }

def _build_lunar_phases(rng: random.Random) -> Dict[str, Any]:
    phases = [
        ("New Moon", "the Moon is situated between the Earth and the Sun, with its unlit dark side facing Earth", "zero illumination visible from Earth"),
        ("First Quarter", "half of the visible lunar surface is illuminated on the western side one week after New Moon", "half disc illuminated"),
        ("Full Moon", "the Earth is situated between the Sun and Moon, with the fully illuminated lunar surface facing Earth", "complete illuminated disc visible"),
        ("Third (Last) Quarter", "half of the visible lunar surface is illuminated on the eastern side three weeks after New Moon", "waning half disc illuminated")
    ]
    phase_name, desc, view = rng.choice(phases)
    prompt = f"Which phase of the Moon occurs when {desc}?"
    correct_opt = phase_name
    distractors = [p[0] for p in phases if p[0] != phase_name]
    options = [correct_opt] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand lunar phases cause:\\n"
        f"Lunar phases are caused by changing angles between Earth, Moon, and Sun as the Moon orbits Earth.\\n\\n"
        f"Conclusion: '{desc}' describes the {phase_name}."
    )
    return {
        "id": f"ns7_moon_phase_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "lunar_phases_sequence_and_causes",
        "question_family_id": "lunar_phases_sequence_and_causes",
        "hints": {
            "tier_1": "Is the illuminated face completely visible (Full), invisible (New), or half visible (Quarter)?",
            "tier_2": "Look at the alignment of Earth, Moon, and Sun.",
            "tier_3": f"This corresponds to the {phase_name}."
        },
        "misconception_tags": ["earth_shadow_moon_phases_myth"]
    }

def _build_ocean_tides(rng: random.Random) -> Dict[str, Any]:
    tides = [
        ("Spring tides (highest high tides and lowest low tides)", "the Sun, Moon, and Earth align in a straight line (syzygy) during New Moon and Full Moon, combining their gravitational pulls"),
        ("Neap tides (lowest tidal range with moderate high and low tides)", "the Sun and Moon are positioned at right angles (90°) relative to Earth during First and Third Quarter moons, partially cancelling each other's gravitational pull")
    ]
    tide_type, cause = rng.choice(tides)
    prompt = f"What causes **{tide_type}** in Earth's oceans?"
    correct_opt = f"They occur because {cause}."
    alt_tide = tides[1] if tide_type == tides[0][0] else tides[0]
    options = [
        correct_opt,
        f"They occur because {alt_tide[1]}.",
        "They are caused strictly by undersea earthquakes and volcanic eruptions.",
        "They are caused by strong municipal water pumping stations in coastal cities."
    ]
    rng.shuffle(options)
    sol = (
        f"Tidal Mechanics:\\n"
        f"- Spring tides: Occur twice a month at New/Full Moon when Sun and Moon gravity combine in line -> maximum tidal range.\\n"
        f"- Neap tides: Occur twice a month at Quarter Moons when Sun and Moon pull at 90° -> minimum tidal range.\\n\\n"
        f"Conclusion: {tide_type} occurs because {cause}."
    )
    return {
        "id": f"ns7_moon_tide_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "ocean_tides_spring_and_neap",
        "question_family_id": "ocean_tides_spring_and_neap",
        "hints": {
            "tier_1": "Spring tides have the biggest tidal range; neap tides have the smallest.",
            "tier_2": "Spring tides align in a line (New/Full Moon); neap tides pull at 90 degrees.",
            "tier_3": f"{tide_type} occurs because {cause}."
        },
        "misconception_tags": ["spring_season_spring_tide_confusion"]
    }

def _build_eclipses(rng: random.Random) -> Dict[str, Any]:
    eclipses = [
        ("A Solar Eclipse", "the Moon passes directly between the Earth and the Sun, casting a shadow (umbra/penumbra) on Earth and blocking sunlight", "Daytime during New Moon"),
        ("A Lunar Eclipse", "the Earth passes directly between the Sun and the Moon, casting Earth's shadow across the lunar surface", "Nighttime during Full Moon")
    ]
    ecl_type, mech, timing = rng.choice(eclipses)
    prompt = f"Explain the astronomical geometry of **{ecl_type}**."
    correct_opt = f"{ecl_type} occurs when {mech} ({timing})."
    alt_ecl = eclipses[1] if ecl_type == eclipses[0][0] else eclipses[0]
    options = [
        correct_opt,
        f"{ecl_type} occurs when {alt_ecl[1]} ({alt_ecl[2]}).",
        "It occurs when the Sun explodes and shrinks for two hours.",
        "It happens when clouds completely cover all seven continents simultaneously."
    ]
    rng.shuffle(options)
    sol = (
        f"Eclipse Mechanics:\\n"
        f"- Solar Eclipse: Sun - Moon - Earth. The Moon casts its shadow on Earth.\\n"
        f"- Lunar Eclipse: Sun - Earth - Moon. The Earth casts its shadow on the Moon.\\n\\n"
        f"Conclusion: {ecl_type} occurs when {mech}."
    )
    return {
        "id": f"ns7_moon_ecl_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "lunar_and_solar_eclipses_mechanics",
        "question_family_id": "lunar_and_solar_eclipses_mechanics",
        "hints": {
            "tier_1": "Which body is in the middle: the Moon (solar eclipse) or the Earth (lunar eclipse)?",
            "tier_2": "Solar eclipse = Moon blocks the Sun; Lunar eclipse = Earth shadows the Moon.",
            "tier_3": f"{ecl_type} occurs when {mech}."
        },
        "misconception_tags": ["solar_lunar_eclipse_inversion"]
    }

def _build_gravity_and_weight(rng: random.Random) -> Dict[str, Any]:
    earth_mass = rng.choice([60, 72, 84, 90])
    prompt = (
        f"An astronaut has a mass of {earth_mass} kg on Earth. The Moon has approximately 1/6th of Earth's gravity.\\n\\n"
        f"What will the astronaut's **mass** and approximate **weight** be on the surface of the Moon? (Take Earth gravity g = 10 N/kg)."
    )
    earth_wt = earth_mass * 10
    moon_wt = earth_wt / 6
    correct_opt = f"Mass: {earth_mass} kg (unchanged) | Weight: approximately {moon_wt:.0f} N (1/6th of Earth weight)"
    options = [
        correct_opt,
        f"Mass: {earth_mass/6:.1f} kg | Weight: {earth_wt} N",
        f"Mass: 0 kg | Weight: 0 N (zero gravity exists on the Moon)",
        f"Mass: {earth_mass * 6} kg | Weight: {moon_wt:.0f} N"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand Mass vs Weight:\\n"
        f"- Mass is the amount of matter in an object, measured in kilograms (kg). It never changes regardless of location: Mass = {earth_mass} kg.\\n"
        f"- Weight is the gravitational force acting on that mass, measured in Newtons (N): W = m × g.\\n\\n"
        f"Step 2: Calculate Moon Weight:\\n"
        f"Earth weight = {earth_mass} kg × 10 N/kg = {earth_wt} N.\\n"
        f"Moon weight = {earth_wt} / 6 = approximately {moon_wt:.0f} N."
    )
    return {
        "id": f"ns7_moon_wt_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "gravity_and_weight_on_the_moon",
        "question_family_id": "gravity_and_weight_on_the_moon",
        "hints": {
            "tier_1": "Mass is the amount of matter and never changes. Weight is gravitational force.",
            "tier_2": "Mass stays the same ({earth_mass} kg); weight is divided by 6.",
            "tier_3": f"Mass is {earth_mass} kg and weight is ~{moon_wt:.0f} N."
        },
        "misconception_tags": ["mass_weight_confusion", "moon_zero_gravity_myth"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "moon_orbit_and_revolution_period": _build_moon_orbit,
        "lunar_phases_sequence_and_causes": _build_lunar_phases,
        "ocean_tides_spring_and_neap": _build_ocean_tides,
        "lunar_and_solar_eclipses_mechanics": _build_eclipses,
        "gravity_and_weight_on_the_moon": _build_gravity_and_weight
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
write_gen("ns7_moon_earth_generator.py", code_moon_earth)

# ============================================================================
# TERM 4: RELATIONSHIP OF THE SUN TO THE EARTH
# ============================================================================
code_sun_earth = '''"""Grade 7 Natural Sciences: Term 4 - Relationship of the Sun to the Earth Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the sun to the Earth.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "earth_rotation_day_and_night",
    "earth_revolution_and_year_length",
    "axial_tilt_and_seasons_mechanics",
    "solstices_and_equinoxes_southern_hemisphere",
    "solar_energy_driving_earth_climate"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the sun to the Earth.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_earth_rotation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "What astronomical motion causes the cycle of **day and night** on Earth, "
        "and how long does one complete cycle take?"
    )
    correct_opt = "Earth's rotation on its own internal axis once every 24 hours."
    options = [
        correct_opt,
        "Earth's orbital revolution around the Sun once every 365.25 days.",
        "The Sun physically travelling in a circle around the equator every 12 hours.",
        "The Moon passing in front of the Sun once every 28 days."
    ]
    rng.shuffle(options)
    sol = (
        "Day and Night Mechanics:\\n"
        "Earth spins (rotates) from west to east on its imaginary axis. It takes 24 hours (1 day) to complete "
        "one 360° rotation. The side facing the Sun experiences daylight, while the side facing away experiences darkness (night)."
    )
    return {
        "id": f"ns7_sun_rot_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "earth_rotation_day_and_night",
        "question_family_id": "earth_rotation_day_and_night",
        "hints": {
            "tier_1": "Rotation on its axis causes day/night; revolution around the sun causes years.",
            "tier_2": "Rotation takes 24 hours.",
            "tier_3": "Earth rotating on its axis once every 24 hours."
        },
        "misconception_tags": ["rotation_revolution_confusion"]
    }

def _build_earth_revolution(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "How long does it take for Earth to complete ONE full **revolution (orbit)** around the Sun, "
        "and why do we have a leap year every four years?"
    )
    correct_opt = "365 and 1/4 days (365.25 days): The four quarter-days add up to one extra day (February 29) every four years."
    options = [
        correct_opt,
        "Exactly 300 days: The leap year compensates for summer holidays.",
        "24 hours: Earth completes one orbit around the Sun every single day.",
        "28 days: Earth matches the exact revolution period of the Moon."
    ]
    rng.shuffle(options)
    sol = (
        "Revolution and Leap Years:\\n"
        "1. Earth takes 365 days, 5 hours, 48 minutes, and 46 seconds (~365.25 days) to orbit the Sun.\\n"
        "2. A calendar year has 365 days. The leftover ~0.25 days (6 hours) per year accumulates to 24 hours (1 full day) every 4 years, added as February 29 (Leap Year)."
    )
    return {
        "id": f"ns7_sun_rev_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "earth_revolution_and_year_length",
        "question_family_id": "earth_revolution_and_year_length",
        "hints": {
            "tier_1": "How many days in a normal year plus leap year compensation?",
            "tier_2": "It takes 365.25 days; four quarters equal one extra leap day.",
            "tier_3": "365 and 1/4 days, producing a leap year every 4 years."
        },
        "misconception_tags": ["leap_year_calendar_myth"]
    }

def _build_axial_tilt_seasons(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain why South Africa experiences **summer** in December and **winter** in June. "
        "Reference Earth's axial tilt and angle of sunlight in your answer. (4 marks)"
    )
    sample_answer = (
        "1. Earth's axis is tilted at an angle of 23.5° relative to its orbital plane around the Sun.\\n"
        "2. In December (Summer in SA): The Southern Hemisphere is tilted towards the Sun. Sunlight strikes South Africa at a steep, direct angle (concentrating heat energy over a smaller surface area), and daylight hours are longer than night.\\n"
        "3. In June (Winter in SA): The Southern Hemisphere is tilted away from the Sun. Sunlight strikes at a shallow, slanted angle (spreading solar energy over a much larger area), and daylight hours are shorter."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. Earth's axis is tilted at 23.5° as it orbits the Sun (1 mark).\\n"
        "2. Summer (Dec): Southern Hemisphere tilts toward Sun -> direct, concentrated sunlight and longer days (2 marks).\\n"
        "3. Winter (June): Southern Hemisphere tilts away from Sun -> slanted, spread-out sunlight and shorter days (1 mark)."
    )
    return {
        "id": f"ns7_sun_tilt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "axial_tilt_and_seasons_mechanics",
        "question_family_id": "axial_tilt_and_seasons_mechanics",
        "hints": {
            "tier_1": "Seasons are caused by Earth's 23.5 degree tilt, NOT distance from the Sun.",
            "tier_2": "When tilted toward the sun, rays strike directly (summer); when tilted away, rays are slanted (winter).",
            "tier_3": "Explain 23.5 degree tilt, direct concentrated rays in December, and slanted rays in June."
        },
        "misconception_tags": ["seasons_distance_to_sun_fallacy"]
    }

def _build_solstices_equinoxes(rng: random.Random) -> Dict[str, Any]:
    events = [
        ("Summer Solstice in South Africa (around 21 December)", "the longest day and shortest night of the year in the Southern Hemisphere, with the Sun directly overhead at the Tropic of Capricorn"),
        ("Winter Solstice in South Africa (around 21 June)", "the shortest day and longest night of the year in the Southern Hemisphere, with the Sun directly overhead at the Tropic of Cancer in the north"),
        ("Autumn Equinox in South Africa (around 21 March)", "day and night are of equal duration (12 hours day, 12 hours night) as the Sun is directly overhead at the Equator"),
        ("Spring Equinox in South Africa (around 22 September)", "day and night are of equal duration (12 hours each) worldwide as the Sun crosses the Equator heading south")
    ]
    ev_name, desc = rng.choice(events)
    prompt = f"Which seasonal astronomical event in South Africa is defined as:\\n'{desc}'?"
    correct_opt = ev_name
    distractors = [e[0] for e in events if e[0] != ev_name]
    options = [correct_opt] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand solstices and equinoxes:\\n"
        f"- Solstice ('sun stands still'): Extreme day length (Dec 21 = longest day; June 21 = shortest day in SA).\\n"
        f"- Equinox ('equal night'): Exactly 12 hours day and 12 hours night (March 21 and Sept 22).\\n\\n"
        f"Conclusion: '{desc}' defines {ev_name}."
    )
    return {
        "id": f"ns7_sun_solst_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "solstices_and_equinoxes_southern_hemisphere",
        "question_family_id": "solstices_and_equinoxes_southern_hemisphere",
        "hints": {
            "tier_1": "Equinox = equal day and night; Solstice = extreme day length.",
            "tier_2": "Dec 21 is summer solstice in SA; June 21 is winter solstice.",
            "tier_3": f"This event is {ev_name}."
        },
        "misconception_tags": ["hemisphere_solstice_inversion"]
    }

def _build_solar_energy_climate(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Why is solar radiation from the Sun considered the primary engine driving Earth's weather, winds, and ocean currents?"
    )
    correct_opt = "Unequal heating of Earth's surface (warm equator vs cold poles) causes density and pressure differences that drive atmospheric winds and ocean currents."
    options = [
        correct_opt,
        "Solar radiation pushes the continents like physical conveyor belts across the oceans.",
        "The Sun burns liquid oxygen in the clouds to create thunderstorms.",
        "Solar energy stops rain by evaporating all water from the oceans permanently."
    ]
    rng.shuffle(options)
    sol = (
        "Solar Energy and Global Climate Systems:\\n"
        "Because Earth is curved, equatorial regions receive direct, intense solar heating, whereas polar regions receive "
        "spread-out, slanted sunlight. This thermal gradient creates warm, rising air at the equator and cold, sinking air at the poles, "
        "generating global atmospheric wind belts and driving major ocean conveyor currents."
    )
    return {
        "id": f"ns7_sun_clim_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "solar_energy_driving_earth_climate",
        "question_family_id": "solar_energy_driving_earth_climate",
        "hints": {
            "tier_1": "Think about how unequal heating of the equator vs poles creates wind.",
            "tier_2": "Warm air rises at equator and cool air sinks at poles, creating winds and currents.",
            "tier_3": "Unequal heating causes pressure and density differences driving winds and currents."
        },
        "misconception_tags": ["uniform_solar_heating_myth"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "earth_rotation_day_and_night": _build_earth_rotation,
        "earth_revolution_and_year_length": _build_earth_revolution,
        "axial_tilt_and_seasons_mechanics": _build_axial_tilt_seasons,
        "solstices_and_equinoxes_southern_hemisphere": _build_solstices_equinoxes,
        "solar_energy_driving_earth_climate": _build_solar_energy_climate
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
write_gen("ns7_sun_earth_generator.py", code_sun_earth)

# ============================================================================
# TERM 4: HISTORICAL DEVELOPMENT OF ASTRONOMY
# ============================================================================
code_astronomy = '''"""Grade 7 Natural Sciences: Term 4 - Historical Development of Astronomy Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 4/02. Historical development of astronomy.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "indigenous_african_astronomy_and_star_lore",
    "galileo_and_the_telescope_revolution",
    "optical_vs_radio_telescopes",
    "south_african_large_telescope_salt",
    "square_kilometre_array_ska_karoo"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 4/02. Historical development of astronomy.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_indigenous_astronomy(rng: random.Random) -> Dict[str, Any]:
    lores = [
        ("the Pleiades star cluster (known as 'Isilimela' in isiXhosa / isiZulu and 'Selemela' in Sesotho)", "the onset of the agricultural plowing and planting season in spring"),
        ("the Southern Cross (Crux) and its two pointer stars (Alpha and Beta Centauri)", "a celestial navigational compass indicating true south across the African veld at night"),
        ("the morning star (Venus / 'iKhwezi')", "signalling the approaching dawn for rural herders and early morning travelers")
    ]
    celest, role = rng.choice(lores)
    prompt = (
        f"In indigenous South African astronomical knowledge systems, **{celest}** was traditionally used as a celestial calendar for:\\n\\n"
        f"Which practical cultural or agricultural purpose?"
    )
    correct_opt = f"Signalling {role}."
    options = [
        correct_opt,
        "Determining which minerals to mine in deep shafts.",
        "Predicting modern satellite internet coverage.",
        "Guaranteed warning of undersea tsunamis in the Atlantic ocean."
    ]
    rng.shuffle(options)
    sol = (
        f"Indigenous Knowledge Systems (IKS) in Astronomy:\\n"
        f"Long before modern telescopes, African indigenous communities observed patterns in celestial movements "
        f"to manage agriculture, navigation, and ceremonies.\\n\\n"
        f"Conclusion: {celest} was used for signalling {role}."
    )
    return {
        "id": f"ns7_astro_iks_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "indigenous_african_astronomy_and_star_lore",
        "question_family_id": "indigenous_african_astronomy_and_star_lore",
        "hints": {
            "tier_1": "Think about traditional farming and seasonal stars like Isilimela (Pleiades).",
            "tier_2": "Stars were used to mark planting seasons and guide night navigation.",
            "tier_3": f"It was used for signalling {role}."
        },
        "misconception_tags": ["iks_astronomy_dismissal_bias"]
    }

def _build_galileo_revolution(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In 1609, **Galileo Galilei** pointed a newly improved optical telescope at the night sky. "
        "Which major discovery provided definitive evidence supporting the heliocentric (Sun-centred) model of the solar system?"
    )
    correct_opt = "He discovered four large moons orbiting Jupiter, proving that not all celestial bodies revolve around the Earth."
    options = [
        correct_opt,
        "He discovered human footprints and artificial roads on the Moon.",
        "He proved that the Sun is made of solid cold granite.",
        "He showed that Earth is completely stationary at the exact center of the universe."
    ]
    rng.shuffle(options)
    sol = (
        "Galilean Discoveries (1609-1610):\\n"
        "Galileo discovered the four largest moons of Jupiter (Io, Europa, Ganymede, Callisto). "
        "This disproved the ancient geocentric Ptolemaic model (which held that everything revolved strictly around Earth) "
        "and provided empirical proof supporting Copernicus's heliocentric model."
    )
    return {
        "id": f"ns7_astro_gal_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "galileo_and_the_telescope_revolution",
        "question_family_id": "galileo_and_the_telescope_revolution",
        "hints": {
            "tier_1": "Think about Jupiter's moons.",
            "tier_2": "Seeing moons orbit Jupiter proved that not everything revolves around Earth.",
            "tier_3": "He discovered Jupiter's moons, proving bodies can orbit other planets."
        },
        "misconception_tags": ["geocentric_galileo_confusion"]
    }

def _build_optical_vs_radio(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Which statement correctly distinguishes an **optical telescope** from a **radio telescope**?"
    )
    correct_opt = "Optical telescopes collect visible light rays using glass lenses or mirrors; radio telescopes collect long-wavelength radio waves using curved metal dish antennae."
    options = [
        correct_opt,
        "Optical telescopes listen to radio music; radio telescopes shoot visible laser beams into deep space.",
        "Radio telescopes can only operate inside dark underwater submarines.",
        "Both telescopes collect only audible sound waves made by exploding stars."
    ]
    rng.shuffle(options)
    sol = (
        "Types of Astronomical Telescopes:\\n"
        "- Optical Telescopes: Capture visible electromagnetic light using glass refractive lenses or primary parabolic mirrors.\\n"
        "- Radio Telescopes: Detect invisible, long-wavelength radio emissions from celestial objects using curved parabolic metal dishes."
    )
    return {
        "id": f"ns7_astro_types_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "optical_vs_radio_telescopes",
        "question_family_id": "optical_vs_radio_telescopes",
        "hints": {
            "tier_1": "Optical = visible light; Radio = radio wave frequencies.",
            "tier_2": "Optical uses lenses/mirrors; radio uses metal dish antennae.",
            "tier_3": "Optical collects visible light; radio collects radio waves."
        },
        "misconception_tags": ["radio_telescope_sound_wave_myth"]
    }

def _build_salt_sutherland(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **Southern African Large Telescope (SALT)** is the largest single optical telescope in the Southern Hemisphere. "
        "Why was the small town of Sutherland in the Karoo chosen as the location for SALT? (4 marks)"
    )
    sample_answer = (
        "1. Dark skies with minimal light pollution: Sutherland has a tiny population and strict lighting bylaws, ensuring dark skies free from city glare.\\n"
        "2. Arid climate and low cloud cover: The Karoo has very low rainfall, resulting in cloudless nights for over 75% of the year.\\n"
        "3. High elevation: Sutherland sits at approximately 1 800 metres above sea level, placing the telescope above low-lying atmospheric haze and moisture.\\n"
        "4. Clean, stable air: Stable atmospheric conditions ensure minimal optical distortion (atmospheric seeing)."
    )
    sol = (
        "Marking Rubric (4 marks total, any 4 points):\\n"
        "1. Absence of city light pollution / dark skies (1 mark).\\n"
        "2. Dry Karoo climate / high number of cloudless clear nights (1 mark).\\n"
        "3. High altitude (1 800 m) above atmospheric moisture and haze (1 mark).\\n"
        "4. Stable, unpolluted atmosphere reducing twinkling/distortion (1 mark)."
    )
    return {
        "id": f"ns7_astro_salt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "south_african_large_telescope_salt",
        "question_family_id": "south_african_large_telescope_salt",
        "hints": {
            "tier_1": "Why is the Karoo good for looking at stars through a giant mirror?",
            "tier_2": "Think about darkness, lack of city lights, clear cloudless skies, and high elevation.",
            "tier_3": "Mention zero light pollution, cloudless Karoo nights, high altitude, and clean stable air."
        },
        "misconception_tags": ["telescope_city_center_fallacy"]
    }

def _build_ska_karoo(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "What is the **Square Kilometre Array (SKA)** being constructed in the Karoo region of South Africa?"
    )
    correct_opt = "The world's largest and most sensitive radio telescope array, combining thousands of interconnected antennae to explore the early universe."
    options = [
        correct_opt,
        "A nuclear weapons testing site hidden under the desert sands.",
        "A commercial space airport designed for luxury passenger flights to Mars.",
        "A coal-burning power station that supplies electricity to deep-space probes."
    ]
    rng.shuffle(options)
    sol = (
        "The Square Kilometre Array (SKA) Project:\\n"
        "The SKA is a massive international scientific mega-project co-hosted by South Africa (Karoo) and Australia. "
        "It connects thousands of mid-frequency radio dish antennae to create an effective collecting area of one square kilometre, "
        "enabling scientists to study the formation of the first stars, dark energy, and cosmic magnetism."
    )
    return {
        "id": f"ns7_astro_ska_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "square_kilometre_array_ska_karoo",
        "question_family_id": "square_kilometre_array_ska_karoo",
        "hints": {
            "tier_1": "It is an international radio telescope project in the Karoo.",
            "tier_2": "It uses thousands of dish antennae to study the early universe.",
            "tier_3": "The world's largest radio telescope array exploring the early universe."
        },
        "misconception_tags": ["ska_optical_confusion"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "indigenous_african_astronomy_and_star_lore": _build_indigenous_astronomy,
        "galileo_and_the_telescope_revolution": _build_galileo_revolution,
        "optical_vs_radio_telescopes": _build_optical_vs_radio,
        "south_african_large_telescope_salt": _build_salt_sutherland,
        "square_kilometre_array_ska_karoo": _build_ska_karoo
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
write_gen("ns7_astronomy_history_generator.py", code_astronomy)
