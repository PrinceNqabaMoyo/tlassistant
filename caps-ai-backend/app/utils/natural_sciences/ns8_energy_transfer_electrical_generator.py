"""Natural Sciences Grade 8 Term 3: Energy Transfer in Electrical Systems Generator.

Strictly grounded in curriculum_docs_auto/NaturalSciences_Gr8/Syllabus.md.
Covers:
- circuit_components_and_conduction_path: Cells/batteries, closed circuit pathways, electron flow, standard symbols.
- resistance_and_heating_effects: Resistance concept, filament bulbs, nichrome wire in kettles and stoves.
- short_circuits_and_fuse_safety: Short circuit dynamics (path of least resistance), fuse melting mechanism, circuit breakers.
- magnetic_effect_and_electromagnets: Magnetic field around conductors, making an electromagnet, electric bells and cranes.
- chemical_effect_electrolysis_applications: Electrolysis of CuCl2, electroplating silver/copper onto cutlery, metal refining.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


SUBSKILLS = [
    "circuit_components_and_conduction_path",
    "resistance_and_heating_effects",
    "short_circuits_and_fuse_safety",
    "magnetic_effect_and_electromagnets",
    "chemical_effect_electrolysis_applications",
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _build_circuit_components(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    components = [
        {"name": "Electric cell / battery", "function": "Stores chemical potential energy and converts it into electrical potential energy to push charges", "symbol": "Long parallel line (positive) and shorter thicker line (negative)"},
        {"name": "Switch", "function": "Provides a controllable break in the circuit to safely open (stop current) or close (allow current) the conducting pathway", "symbol": "Two circles connected by a hinged lever line"},
        {"name": "Resistor", "function": "Opposes or limits the flow of electric charge, converting electrical energy into heat or light", "symbol": "A simple open rectangle or zigzag line"}
    ]
    c = rng.choice(components)
    prompt = (
        f"In electric circuit diagrams, standard symbols represent functional components.\n\n"
        f"Which electrical component has the primary function of *{c['function']}*?"
    )
    correct_ans = c["name"]
    distractors = [x["name"] for x in components if x["name"] != correct_ans]
    distractors.append("Voltmeter connected in series")
    options = [correct_ans] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Analyze component function:\n"
        f"{c['function']}.\n\n"
        f"Step 2: Match:\n"
        f"This corresponds to the **{correct_ans}**."
    )
    return {
        "id": _make_id("ns8_circ_comp", seed, idx),
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
        "subskill": "circuit_components_and_conduction_path",
        "question_family_id": "circuit_components_and_conduction_path",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Energy Transfer in Electrical Systems > Circuit components",
        "hints": {
            "tier_1": "Recall the main parts of an electric circuit: source of energy, conductor, switch, load.",
            "tier_2": "Batteries supply energy; switches open/close paths; resistors oppose current.",
            "tier_3": f"The component is {correct_ans}."
        },
        "misconception_tags": ["open_switch_allows_current_misconception"]
    }


def _build_resistance_heating(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    appliances = [
        ("an electric kettle heating water", "nichrome wire coil", "high electrical resistance causes moving electrons to collide with metal lattice ions, generating thermal heat"),
        ("a tungsten filament incandescent light bulb", "coiled thin tungsten filament", "extremely high resistance causes the fine wire to glow white-hot, emitting radiant heat and visible light"),
        ("a domestic geyser heating element", "corrosion-resistant alloy element", "electrical energy is converted into thermal heat energy through high resistance")
    ]
    device, material, mechanism = rng.choice(appliances)
    prompt = (
        f"Domestic heating appliances make use of the heating effect of an electric current.\n\n"
        f"Consider **{device}**:\n"
        f"1. Name a high-resistance metal alloy or element commonly used in its construction ({material}).\n"
        f"2. Explain scientifically how high electrical resistance converts electrical energy into heat at a microscopic level.\n"
        f"3. State what energy transformation takes place in this appliance."
    )
    sample_answer = (
        f"1. Material: Nichrome wire (an alloy of nickel and chromium) / Tungsten.\n"
        f"2. Mechanism: {mechanism}.\n"
        "3. Energy conversion: Electrical energy -> Thermal heat energy (and light energy)."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        "1. Conductor material: Nichrome / Tungsten [1 mark].\n"
        "2. Microscopic mechanism: Collision of flowing electrons with metal atoms/lattice ions transforms kinetic energy into heat vibrations [1 mark].\n"
        "3. Energy conversion: Electrical energy transformed into thermal energy [1 mark]."
    )
    return {
        "id": _make_id("ns8_heat_effect", seed, idx),
        "question_type": "paragraph",
        "diagram_spec": {
            "image_type": "geyser_heating_element",
            "master": "geyser_heating_element",
            "diagram_id": "geyser_heating_element",
            "view": "textbook",
            "diagram_role": "context",
            "allowViewSwitch": False,
            "pins": [],
        },
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "resistance_and_heating_effects",
        "question_family_id": "resistance_and_heating_effects",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Energy Transfer in Electrical Systems > Heating effect of current",
        "hints": {
            "tier_1": "Resistance is friction for electric current.",
            "tier_2": "Colliding electrons make metal atoms vibrate faster, producing heat.",
            "tier_3": "Electrical energy becomes thermal energy; nichrome is the common element material."
        },
        "misconception_tags": ["electrons_are_consumed_in_resistor_misconception"]
    }


def _build_short_circuits_fuses(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    appliances = [
        "In a domestic kitchen, an old electric kettle has a frayed cord, allowing the bare live and neutral copper conductors to touch directly.",
        "In a school woodwork workshop, a handheld power drill cord is pinched under a metal bench, causing live and neutral wires to make contact.",
        "In a residential lounge, an overloaded extension lead gets damaged, causing internal live and neutral wires to short-circuit before reaching the television."
    ]
    chosen_app = rng.choice(appliances)
    prompt = (
        f"{chosen_app}\n\n"
        f"1. What is the technical term for this dangerous electrical fault?\n"
        f"2. Explain why this fault causes the current in the circuit to surge to an extremely high, dangerous level.\n"
        f"3. Explain how a safety **fuse** protects the home from an electrical fire when this fault occurs."
    )
    sample_answer = (
        "1. Short circuit.\n"
        "2. When wires touch directly, current bypasses the high-resistance appliance. Because resistance drops to almost zero, current surges to an extremely high level (I = V / R).\n"
        "3. The fuse contains a thin wire with a low melting point. The massive current generates intense heat that rapidly melts the fuse wire, breaking the circuit and instantly cutting off power before wires overheat and ignite a fire."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Term: Short circuit [1 mark].\n"
        "2. Mechanism: Current takes the path of near-zero resistance, causing current to surge dangerously [1 mark].\n"
        "3. Fuse function: Thin wire heats up and melts (blows) [1 mark].\n"
        "4. Fire prevention: Breaks the circuit, cutting off current and preventing wire combustion [1 mark]."
    )
    return {
        "id": _make_id("ns8_fuse_safety", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "short_circuits_and_fuse_safety",
        "question_family_id": "short_circuits_and_fuse_safety",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Energy Transfer in Electrical Systems > Short circuits and fuses",
        "hints": {
            "tier_1": "Bypassing the load is a short circuit.",
            "tier_2": "Near zero resistance leads to huge current and extreme heat.",
            "tier_3": "The fuse wire melts to break the circuit and stop the fire."
        },
        "misconception_tags": ["fuse_generates_more_electricity_misconception"]
    }


def _build_magnetic_electromagnets(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    turns = rng.choice([30, 50, 75, 100])
    volts = rng.choice([3, 6, 9])
    core = rng.choice(["an iron nail", "a soft iron bolt", "a solid steel rod"])
    prompt = (
        f"A student wraps {turns} turns of insulated copper wire around {core} and connects the wire ends to a {volts} V DC battery pack and switch.\n\n"
        f"1. What temporary magnetic device has the student constructed?\n"
        f"2. What observable magnetic effect occurs when the switch is closed and paper clips are brought near the core?\n"
        f"3. State two ways the student can increase the magnetic strength of this device."
    )
    sample_answer = (
        "1. An electromagnet.\n"
        "2. The iron nail becomes magnetized and attracts the steel paper clips.\n"
        "3. Two ways to increase strength:\n"
        "- Increase the number of wire coils/turns around the nail.\n"
        "- Increase the electric current (e.g. by adding more cells in series)."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Device name: Electromagnet [1 mark].\n"
        "2. Observation: Nail attracts magnetic paper clips [1 mark].\n"
        "3. Strengthening method 1: Increase the number of coil turns [1 mark].\n"
        "4. Strengthening method 2: Increase the electrical current / voltage (add more cells) [1 mark]."
    )
    return {
        "id": _make_id("ns8_electromagnet", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "magnetic_effect_and_electromagnets",
        "question_family_id": "magnetic_effect_and_electromagnets",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Energy Transfer in Electrical Systems > Electromagnets",
        "hints": {
            "tier_1": "A coil around iron connected to a battery is an electromagnet.",
            "tier_2": "Closing the switch creates a magnetic field that picks up iron clips.",
            "tier_3": "Add more turns or more cells to make it stronger."
        },
        "misconception_tags": ["electromagnet_stays_magnetic_permanently_misconception"]
    }


def _build_chemical_electrolysis_app(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    items = [
        ("steel cutlery with a thin layer of pure silver", "silver", "cutlery"),
        ("brass car door handles with a protective layer of shiny chromium", "chromium", "door handles"),
        ("iron screws and bolts with a corrosion-resistant coating of pure zinc", "zinc", "fasteners")
    ]
    plating_text, metal, obj = rng.choice(items)
    prompt = (
        f"In commercial manufacturing, the chemical effect of an electric current is used for **electroplating** {plating_text}.\n\n"
        f"1. Explain how an electric current is used in electroplating.\n"
        f"2. State at which electrode (cathode or anode) the {obj} to be coated must be connected.\n"
        f"3. Give two reasons why everyday metal objects are electroplated."
    )
    sample_answer = (
        "1. Current passes through an electrolyte solution containing metal ions, causing metal ions to gain electrons and deposit as a solid thin layer on the object.\n"
        "2. The object to be plated must be connected to the negative electrode (cathode).\n"
        "3. Two reasons: To prevent corrosion/rusting, and to improve aesthetic appearance (make it shiny/decorative)."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        "1. Electroplating process: Metal deposition via electrical current passing through electrolyte [1 mark].\n"
        "2. Electrode: Negative cathode [1 mark].\n"
        "3. Reasons: Corrosion protection and decorative/aesthetic value [1 mark]."
    )
    return {
        "id": _make_id("ns8_electroplate", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "chemical_effect_electrolysis_applications",
        "question_family_id": "chemical_effect_electrolysis_applications",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Energy Transfer in Electrical Systems > Electrolysis and electroplating",
        "hints": {
            "tier_1": "Electroplating coats one metal onto another using electricity.",
            "tier_2": "Cations move to the negative cathode.",
            "tier_3": "It prevents rust and looks attractive."
        },
        "misconception_tags": ["electroplating_melts_metal_misconception"]
    }


def generate(archetype: Optional[str] = None, seed: Optional[int] = None, count: int = 1, **kwargs) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    results = []
    for idx in range(count):
        target = archetype or rng.choice(SUBSKILLS)
        if target == "circuit_components_and_conduction_path":
            item = _build_circuit_components(rng, seed, idx)
        elif target == "resistance_and_heating_effects":
            item = _build_resistance_heating(rng, seed, idx)
        elif target == "short_circuits_and_fuse_safety":
            item = _build_short_circuits_fuses(rng, seed, idx)
        elif target == "magnetic_effect_and_electromagnets":
            item = _build_magnetic_electromagnets(rng, seed, idx)
        elif target == "chemical_effect_electrolysis_applications":
            item = _build_chemical_electrolysis_app(rng, seed, idx)
        else:
            item = _build_circuit_components(rng, seed, idx)
        results.append(item)
    return results


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)
