"""Grade 7 Natural Sciences: Term 3 - Heat Energy Transfer Generator.
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
    spoons = [
        "A solid silver teaspoon resting in a freshly poured mug of hot rooibos tea",
        "A stainless steel cooking ladle dipped into a pot of simmering soup on a stove",
        "A copper stirring rod submerged in a beaker of boiling water in a science lab"
    ]
    prompt = (
        f"{rng.choice(spoons)} quickly conducts heat from the submerged tip to the handle.\n\n"
        f"How does heat transfer through the metal by **conduction** at the particle level?"
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
        "Mechanism of Thermal Conduction:\n"
        "1. Conduction occurs mainly in solids where particles are packed tightly in fixed positions.\n"
        "2. Thermal energy causes particles at the heated end to vibrate more vigorously.\n"
        "3. These vibrating particles collide with neighbouring particles, passing kinetic energy along the material.\n"
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
    pots = [
        "a stainless steel cooking pot filled with soup on a hot electric stove plate",
        "a transparent Pyrex beaker of water containing food coloring heated over a Bunsen flame",
        "an electric kettle warming cold tap water from a submerged base heating element"
    ]
    prompt = (
        f"Consider {rng.choice(pots)}.\n\n"
        f"Explain in detail how a **convection current** forms and circulates heat energy throughout the fluid. (4 marks)"
    )
    sample_answer = (
        "1. Heating and expansion: Water at the bottom heats up, its particles gain kinetic energy and spread further apart, causing the warm water to expand.\n"
        "2. Density change: Because the warm water expands, its density decreases (it becomes less dense than surrounding water).\n"
        "3. Rising: The less dense warm water rises towards the surface.\n"
        "4. Circulation: Denser, cooler water at the surface sinks to the bottom to take its place, where it is heated, creating a continuous circulating convection current."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Water at bottom warms, particles spread out and water expands (1 mark).\n"
        "2. Warm water becomes less dense (1 mark).\n"
        "3. Less dense warm water rises (1 mark).\n"
        "4. Cooler, denser water sinks, forming a continuous circular flow (convection current) (1 mark)."
    )
    return {
        "id": f"ns7_ht_conv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "correct_answer": sample_answer,
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
    intros = [
        "Outer space between the Sun and Earth's atmosphere is an almost complete vacuum with no physical air particles.",
        "Radiant solar energy travels roughly 150 million kilometres across empty interplanetary space.",
        "Unlike conduction and convection which require material particles, solar heat reaches Earth across open space."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"How does heat from the Sun travel through the vacuum of outer space to reach the Earth?"
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
        "Thermal Radiation in a Vacuum:\n"
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
    prompt = f"Identify the primary mode of heat transfer occurring in this scenario:\n'{scen}'."
    correct_opt = mode
    options = ["Conduction", "Convection", "Radiation", "Sublimation"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Check mechanism:\n"
        f"- Conduction = direct contact through solids.\n"
        f"- Convection = bulk movement of fluid (liquid/gas).\n"
        f"- Radiation = infrared waves across air or vacuum.\n\n"
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
    containers = [
        ("two identical metal tin cans", "a radiant electric bar heater"),
        ("two aluminium beverage containers filled with water", "an infrared heating lamp"),
        ("two identical cylindrical metal test vessels", "a central radiant heating filament"),
        ("two copper calorimetric beakers", "a focused radiant thermal lamp")
    ]
    cont, src = rng.choice(containers)
    prompt = (
        f"In a laboratory investigation, Grade 7 learners test the absorption of radiant heat by placing thermometers into {cont}: "
        f"one painted matte black and the other painted shiny silver, placed equidistant from {src}.\n\n"
        f"Which container will show the fastest temperature increase, and why?"
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
        "Principles of Thermal Absorption and Reflection:\n"
        "- Dark, matte (dull) surfaces are excellent absorbers and emitters of radiant heat.\n"
        "- Light, shiny surfaces are excellent reflectors and poor absorbers of radiant heat.\n\n"
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
