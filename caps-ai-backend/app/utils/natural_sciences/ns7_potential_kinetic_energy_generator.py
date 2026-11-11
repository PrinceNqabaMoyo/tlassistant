"""Grade 7 Natural Sciences: Term 3 - Potential and Kinetic Energy Generator.
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
    prompt = f"Consider: **{scen}**.\n\nWhich form of mechanical energy is primarily represented?"
    correct_opt = correct_type
    options = [correct_opt, wrong_type, "Nuclear radiant fission", "Geothermal tectonic energy"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand energy definitions:\n"
        f"- Potential Energy: Energy stored within an object due to its position, state, or chemical configuration.\n"
        f"- Kinetic Energy: The energy possessed by an object due to its physical motion.\n\n"
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
        f"Brick A is placed at a height of {h1} m, while Brick B is placed at {h2} m.\n\n"
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
        f"Step 1: Formula for gravitational potential energy:\n"
        f"Ep = m × g × h (where m = mass, g = gravitational acceleration, h = height).\n\n"
        f"Step 2: Compare heights:\n"
        f"Brick B is at {h2} m, which is twice {h1} m. Since mass and gravity are constant, Ep doubles with height.\n\n"
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
    prompt = f"What specific form of potential energy is found in:\n'{item_desc}'?"
    correct_opt = form
    alt_form = "Elastic potential energy" if form == "Chemical potential energy" else "Chemical potential energy"
    options = [correct_opt, alt_form, "Gravitational potential energy", "Kinetic friction"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Classify stored potential energy types:\n"
        f"- Chemical potential: Energy in chemical bonds (food, fuels, batteries).\n"
        f"- Elastic potential: Energy in stretched/compressed objects.\n\n"
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
    systems = [
        ("a simple laboratory pendulum", "bob", "swings from its highest release point"),
        ("a playground swing", "child and swing seat", "swings back and forth from the highest point of release"),
        ("a grandfather clock pendulum", "brass weight", "oscillates between maximum displacement points"),
        ("a demolition crane suspended weight", "cable and steel sphere", "swings from its maximum raised position")
    ]
    sys_name, part, movement = rng.choice(systems)
    prompt = (
        f"Consider {sys_name} where the {part} {movement} "
        f"(Position 1), passes through the lowest centre point (Position 2), and rises to the opposite high point (Position 3).\n\n"
        f"Trace the mechanical energy transformations that take place between Positions 1, 2, and 3. (4 marks)"
    )
    sample_answer = (
        "1. Position 1 (Highest point): The pendulum is momentarily stationary at maximum height, possessing maximum gravitational potential energy and zero kinetic energy.\n"
        "2. Moving toward Position 2: As it falls, gravitational potential energy is converted into kinetic energy, and its speed increases.\n"
        "3. Position 2 (Lowest point): The pendulum reaches maximum speed and lowest height, possessing maximum kinetic energy and minimum potential energy.\n"
        "4. Rising to Position 3: Kinetic energy is converted back into gravitational potential energy until it stops momentarily at maximum height."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Position 1: Maximum gravitational potential energy, zero kinetic (1 mark).\n"
        "2. Transition: Potential converted to kinetic as speed increases (1 mark).\n"
        "3. Position 2: Maximum kinetic energy, minimum potential energy (1 mark).\n"
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
        f"A delivery minibus travels down a highway at {v1} km/h, then accelerates to {v2} km/h.\n\n"
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
        f"Step 1: Kinetic energy relationship:\n"
        f"Ek = 1/2 × m × v^2 (where m = mass, v = speed).\n\n"
        f"Step 2: Effect of increasing speed:\n"
        f"Kinetic energy increases with the square of speed. When speed doubles from {v1} to {v2} km/h, kinetic energy quadruples (2^2 = 4 times).\n\n"
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
