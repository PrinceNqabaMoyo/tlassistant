"""Natural Sciences Grade 8 Term 3: Static Electricity Generator.

Strictly grounded in curriculum_docs_auto/NaturalSciences_Gr8/Syllabus.md.
Covers:
- electrostatic_friction_electron_transfer: Friction causes electron transfer; protons/neutrons remain stationary in nuclei.
- laws_of_electrostatic_attraction_repulsion: Like charges repel, opposite charges attract, charged rods attract neutral paper.
- electrostatic_discharge_and_lightning: Sudden spark discharge, lightning formation between cloud and ground.
- materials_triboelectric_charging: Perspex, plastic rods, wool, silk, fur charging behaviors.
- electrostatic_hazards_and_grounding: Fuel tanker grounding, earthing, avoiding electronic component damage.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


SUBSKILLS = [
    "electrostatic_friction_electron_transfer",
    "laws_of_electrostatic_attraction_repulsion",
    "electrostatic_discharge_and_lightning",
    "materials_triboelectric_charging",
    "electrostatic_hazards_and_grounding",
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _build_electron_transfer(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    pairs = [
        ("a neutral plastic ruler with a dry woolen cloth", "wool onto the plastic ruler", "plastic ruler", "Negative", "woolen cloth", "Positive"),
        ("a glass rod with a piece of natural silk", "glass rod onto the silk", "glass rod", "Positive", "silk cloth", "Negative"),
        ("an inflated rubber balloon against human hair", "hair onto the balloon", "balloon", "Negative", "hair", "Positive")
    ]
    rub_text, trans_text, item1, charge1, item2, charge2 = rng.choice(pairs)
    prompt = (
        f"A learner vigorously rubs {rub_text}. During this friction, electrons are transferred from the {trans_text}.\n\n"
        f"1. What is the resulting electrical charge on the {item1}? (Positive or Negative)\n"
        f"2. What is the resulting electrical charge on the {item2}?\n"
        f"3. Explain why only electrons are transferred during friction while positive protons remain stationary inside the atom."
    )
    sample_answer = (
        "1. Plastic ruler: Negative charge (it gained excess electrons).\n"
        "2. Woolen cloth: Positive charge (it lost electrons, leaving excess protons).\n"
        "3. Electrons are loosely held in the outer electron shells and can easily be rubbed off by friction. Protons are bound tightly inside the central atomic nucleus by immense nuclear forces and cannot move."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        "1. Ruler charge: Negative [1 mark].\n"
        "2. Cloth charge: Positive [1 mark].\n"
        "3. Scientific mechanism: Outer electrons are mobile and transferred by friction, while protons are tightly bound in the nucleus by strong nuclear forces [1 mark]."
    )
    return {
        "id": _make_id("ns8_static_trans", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "electrostatic_friction_electron_transfer",
        "question_family_id": "electrostatic_friction_electron_transfer",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Static Electricity > Friction and electron transfer",
        "hints": {
            "tier_1": "Gaining electrons gives a negative charge; losing electrons gives a positive charge.",
            "tier_2": "Protons never move during rubbing; only electrons transfer.",
            "tier_3": "Ruler is negative, cloth is positive."
        },
        "misconception_tags": ["protons_transfer_during_friction_misconception"]
    }


def _build_attraction_repulsion(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    scenarios = [
        ("Two negatively charged balloons suspended on nylon threads brought close to each other", "They repel each other (push away) because like charges repel"),
        ("A negatively charged balloon brought close to a positively charged perspex rod", "They attract each other (pull together) because opposite charges attract"),
        ("A negatively charged plastic comb brought close to tiny uncharged pieces of tissue paper", "The comb attracts the neutral paper because it induces opposite charges on the paper's nearest surface (polarization)")
    ]
    situation, outcome = rng.choice(scenarios)
    prompt = (
        f"In an electrostatics experiment, a science student sets up the following arrangement:\n"
        f"*{situation}*\n\n"
        f"Predict and explain the observable electrostatic interaction according to the Fundamental Law of Charges."
    )
    correct_ans = outcome
    distractors = [
        "The objects violently spark and instantly lose all mass",
        "The objects remain completely stationary with zero force between them",
        "The objects demagnetize and transform into conductors"
    ]
    options = [correct_ans] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: State the Law of Electrostatics:\n"
        f"1. Like charges repel.\n"
        f"2. Opposite charges attract.\n"
        f"3. Charged objects attract neutral objects by charge polarization.\n\n"
        f"Step 2: Conclusion:\n"
        f"{outcome}."
    )
    return {
        "id": _make_id("ns8_static_law", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "laws_of_electrostatic_attraction_repulsion",
        "question_family_id": "laws_of_electrostatic_attraction_repulsion",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Static Electricity > Attraction and repulsion",
        "hints": {
            "tier_1": "Like charges (positive-positive or negative-negative) push apart; opposites pull together.",
            "tier_2": "Neutral objects are attracted to charged objects through induced polarization.",
            "tier_3": f"The answer is {correct_ans}."
        },
        "misconception_tags": ["neutral_objects_repel_charged_objects_misconception"]
    }


def _build_discharge_lightning(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    loc = rng.choice(["Gauteng Highveld", "Drakensberg mountain escarpment", "Free State plains", "Mpumalanga highveld region"])
    prompt = (
        f"During severe summer thunderstorms across the {loc} in South Africa, static electricity discharges as dramatic lightning strikes.\n\n"
        "1. Explain how friction within thunderclouds causes the separation and accumulation of electric charge.\n"
        "2. Explain what occurs during an electrostatic discharge (lightning stroke) between a cloud and the ground.\n"
        "3. Name the protective metal device installed on roofs and high buildings to safely conduct lightning strikes into the earth."
    )
    sample_answer = (
        "1. Rising warm air currents cause turbulent collisions between hail, ice crystals, and water droplets. Friction strips electrons, leaving the top of the cloud positively charged and the base negatively charged.\n"
        "2. When the potential difference becomes massive, air ionizes and a giant stream of electrons surges through the ionized air channel to the positively charged earth, creating a brilliant light spark and thunder.\n"
        "3. A lightning conductor / lightning rod connected to an earthing cable."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        "1. Charge separation in clouds: Friction between colliding ice/water particles in updrafts [1 mark].\n"
        "2. Discharge mechanism: Massive flow of electrons through ionized air channel between cloud and ground [1 mark].\n"
        "3. Protection: Lightning conductor / rod earthed into the ground [1 mark]."
    )
    return {
        "id": _make_id("ns8_lightning", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "electrostatic_discharge_and_lightning",
        "question_family_id": "electrostatic_discharge_and_lightning",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Static Electricity > Lightning and electrostatic discharge",
        "hints": {
            "tier_1": "Colliding particles in clouds create huge static charges.",
            "tier_2": "Lightning is a giant spark of electrons discharging to earth.",
            "tier_3": "A lightning rod protects buildings."
        },
        "misconception_tags": ["lightning_is_magnetic_energy_misconception"]
    }


def _build_triboelectric_charging(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    materials = [
        {"rod": "a Perspex rod", "cloth": "a silk cloth", "rod_charge": "Positive", "reason": "Perspex readily loses electrons to the silk"},
        {"rod": "a polythene (plastic) rod", "cloth": "a woolen cloth", "rod_charge": "Negative", "reason": "Plastic has a strong affinity for electrons and gains them from the wool"}
    ]
    m = rng.choice(materials)
    prompt = (
        f"A physics teacher demonstrates triboelectric charging by rubbing **{m['rod']}** with **{m['cloth']}**.\n\n"
        f"What electrical charge does the rod acquire, and why?"
    )
    correct_ans = f"Acquires a {m['rod_charge']} charge because {m['reason']}"
    distractors = [
        f"Acquires a neutral charge because protons flow through the air into the cloth",
        f"Acquires an alternating current voltage that continuously flips polarity",
        f"Destroys all atoms on the surface to produce pure neutron particles"
    ]
    options = [correct_ans] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify triboelectric properties:\n"
        f"When rubbing {m['rod']} with {m['cloth']}, {m['reason']}.\n\n"
        f"Step 2: Conclusion:\n"
        f"{correct_ans}."
    )
    return {
        "id": _make_id("ns8_tribo", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "materials_triboelectric_charging",
        "question_family_id": "materials_triboelectric_charging",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Static Electricity > Triboelectric series",
        "hints": {
            "tier_1": "Perspex becomes positive when rubbed with silk; polythene becomes negative when rubbed with wool.",
            "tier_2": "Remember that gaining electrons makes an object negative.",
            "tier_3": f"The answer is {correct_ans}."
        },
        "misconception_tags": ["friction_creates_new_charges_misconception"]
    }


def _build_hazards_grounding(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    loc = rng.choice(["When commercial aircraft are refueled at OR Tambo International Airport", "When bulk petrol tankers offload fuel at a Durban distribution depot", "When industrial road tankers transfer combustible hydrocarbons in Sasolburg"])
    prompt = (
        f"{loc}, a heavy copper grounding wire is always clamped from the vehicle's metal chassis to an earthing spike in the ground.\n\n"
        "1. Explain why fuel flowing through rubber hoses generates dangerous static electricity.\n"
        "2. Explain the catastrophic safety hazard if static electricity accumulates without being discharged.\n"
        "3. Explain scientifically how the grounding cable prevents this hazard."
    )
    sample_answer = (
        "1. Friction between the rapidly flowing fuel and the inner walls of the pipe/tank strips electrons and accumulates static electrical charge.\n"
        "2. An unexpected electrostatic spark discharge could ignite flammable fuel vapors, causing a massive explosion and fire.\n"
        "3. The copper grounding cable provides a safe low-resistance conducting pathway that allows accumulated electrons to flow harmlessly into the earth, preventing any spark from forming."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        "1. Charge cause: Friction between moving liquid fuel and pipe walls [1 mark].\n"
        "2. Explosion hazard: Static spark igniting volatile hydrocarbon vapor [1 mark].\n"
        "3. Grounding function: Provides low-resistance pathway to dissipate charge safely into the earth [1 mark]."
    )
    return {
        "id": _make_id("ns8_grounding", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "electrostatic_hazards_and_grounding",
        "question_family_id": "electrostatic_hazards_and_grounding",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Static Electricity > Grounding and safety",
        "hints": {
            "tier_1": "Flowing fuel rubs against pipes creating friction charge.",
            "tier_2": "Sparks near petrol vapors cause fire or explosion.",
            "tier_3": "Earthing conducts excess electrons safely away to the ground."
        },
        "misconception_tags": ["grounding_insulates_fuel_misconception"]
    }


def generate(archetype: Optional[str] = None, seed: Optional[int] = None, count: int = 1, **kwargs) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    results = []
    for idx in range(count):
        target = archetype or rng.choice(SUBSKILLS)
        if target == "electrostatic_friction_electron_transfer":
            item = _build_electron_transfer(rng, seed, idx)
        elif target == "laws_of_electrostatic_attraction_repulsion":
            item = _build_attraction_repulsion(rng, seed, idx)
        elif target == "electrostatic_discharge_and_lightning":
            item = _build_discharge_lightning(rng, seed, idx)
        elif target == "materials_triboelectric_charging":
            item = _build_triboelectric_charging(rng, seed, idx)
        elif target == "electrostatic_hazards_and_grounding":
            item = _build_hazards_grounding(rng, seed, idx)
        else:
            item = _build_electron_transfer(rng, seed, idx)
        results.append(item)
    return results


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)
