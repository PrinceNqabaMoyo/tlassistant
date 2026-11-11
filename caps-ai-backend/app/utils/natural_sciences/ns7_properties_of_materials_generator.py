"""Grade 7 Natural Sciences: Term 2 - Properties of Materials Generator.
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
    prompt = f"In material science, which property is specifically defined as the ability of a substance to:\n'{desc}'?"
    correct_opt = term
    distractors = [p[1] for p in props if p[1] != term]
    options = [correct_opt] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Properties of matter definitions:\n"
        f"- Malleability: Ability to be hammered into sheets.\n"
        f"- Ductility: Ability to be drawn into wires.\n"
        f"- Durability: Resistance to wear/decay.\n"
        f"- Flexibility: Ability to bend without snapping.\n\n"
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
    prompt = f"Explain the choice of materials in this practical application:\n'{appl}'\n\nWhich statement correctly explains the scientific principle?"
    correct_opt = rationale
    options = [
        correct_opt,
        "Plastics conduct electricity faster than copper wires.",
        "Metals are thermal insulators that trap heat inside cold handles.",
        "All materials conduct heat and electricity at identical rates."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Scientific principles of conductivity:\n"
        f"- Thermal conductors (metals like Cu, Al, Fe) allow heat to pass easily.\n"
        f"- Thermal insulators (plastics, wood, rubber) resist the transfer of heat.\n"
        f"- Electrical conductors allow electric charges to flow; insulators block current.\n\n"
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
    prompt = f"Which type of mechanical strength is defined as:\n'{desc}'?"
    correct_opt = strength_type
    alt_type = "Compressive strength" if strength_type == "Tensile strength" else "Tensile strength"
    options = [correct_opt, alt_type, "Thermal elasticity", "Magnetic permeability"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Distinguish mechanical strengths:\n"
        f"- Tensile strength: Resistance to pulling forces (tension).\n"
        f"- Compressive strength: Resistance to crushing forces (compression).\n\n"
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
        f"Consider **{sub}**. At sea level, its melting point is {mp}°C and its boiling point is {bp}°C.\n\n"
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
        f"Step 1: Check substance temperature thresholds:\n"
        f"- Below melting point ({mp}°C): Solid.\n"
        f"- Between melting point ({mp}°C) and boiling point ({bp}°C): Liquid.\n"
        f"- Above boiling point ({bp}°C): Gas.\n\n"
        f"Step 2: Compare 25°C:\n"
        f"25°C lies {'below' if 25<mp else ('between' if mp<=25<=bp else 'above')} the phase change boundaries.\n"
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
    contexts = [
        "In South African urban centres such as Johannesburg and Durban, municipal landfill sites are rapidly reaching maximum capacity.",
        "Environmental surveys along South African coastlines show plastic waste threatening marine turtles, seals, and coastal seabirds.",
        "Mining raw crude oil to produce virgin polymer packaging consumes vast energy and generates high carbon emissions.",
        "Buy-back waste recycling cooperatives recover thousands of tonnes of post-consumer plastic bottles and crates across townships."
    ]
    prompt = (
        f"{rng.choice(contexts)}\n\n"
        f"Explain TWO major environmental problems caused by the widespread use of non-biodegradable plastics, "
        f"and state how recycling plastics helps address these issues. (4 marks)"
    )
    sample_answer = (
        "1. Environmental pollution and landfill accumulation: Non-biodegradable plastics do not decompose naturally, "
        "filling up municipal landfills and persisting in ecosystems for centuries where they break into toxic microplastics.\n"
        "2. Harm to marine wildlife: Discarded plastics wash into rivers and oceans, where sea turtles and fish ingest them or get entangled.\n"
        "3. Recycling solution: Recycling repurposes existing plastic polymers into new products, conserving crude oil resources and reducing waste sent to landfills."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Two environmental impacts of plastic waste (e.g. non-decomposition in landfills, harm to marine animals) (2 marks).\n"
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
