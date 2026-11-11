"""Grade 7 Natural Sciences: Term 3 - Energy Transfer to Surroundings Generator.
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
    intros = [
        "In physical science, energy can never be created out of nothing, nor can it disappear into nothing.",
        "Whether analyzing an electric motor, a hydroelectric turbine, or a falling apple, total energy remains invariant.",
        "The fundamental law governing all thermodynamic and mechanical transformations in the physical universe is stated below."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"State the **Law of Conservation of Energy** as formulated in natural science."
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
        "Law of Conservation of Energy (First Law of Thermodynamics):\n"
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
        f"In **{app}**, electrical/chemical energy is supplied as input.\n\n"
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
        f"Step 1: Identify purpose of appliance:\n"
        f"- The intended purpose of {app} defines the useful energy: {useful}.\n"
        f"- Unintended, unavoidable by-products represent wasted energy: {wasted}.\n\n"
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
        f"Step 1: Trace the transformation path:\n"
        f"For a {device}, energy converts in the sequence:\n"
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
        f"The diagram shows {useful_e} J directed to useful output and {wasted_e} J curving away into wasted heat.\n\n"
        f"Calculate the **energy efficiency percentage** of this appliance."
    )
    eff = (useful_e / in_e) * 100
    correct_opt = f"{eff:.0f}%"
    options = [f"{eff:.0f}%", f"{wasted_e:.0f}%", f"{100 - eff/2:.0f}%", f"{eff/2:.0f}%"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Formula for energy efficiency:\n"
        f"Efficiency = (Useful Energy Output / Total Energy Input) × 100%\n\n"
        f"Step 2: Calculation:\n"
        f"Efficiency = ({useful_e} J / {in_e} J) × 100% = {eff:.0f}%."
    )
    return {
        "id": f"ns7_trans_eff_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin_letter") or locals().get("target_pin") else "context",
            "kind": "sankey_energy",
            "input_j": in_e,
            "useful_j": useful_e,
            "wasted_j": wasted_e,
            "appliance": "Electric Filament Lamp",
            "useful_name": "Light Illumination",
            "wasted_name": "Dissipated Heat",
            "caption": f"Sankey Diagram: {in_e} J electrical input = {useful_e} J light + {wasted_e} J heat"
        },
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
    devices = [
        "An electric drill motor operating under load",
        "An incandescent light bulb shining in a desk lamp",
        "A car engine running during highway driving",
        "A laptop computer running heavy processing software"
    ]
    prompt = (
        f"During operation of {rng.choice(devices)}, significant heat is released into the surrounding air.\n\n"
        f"Explain what is meant by the phrase 'energy is dissipated to the surroundings', "
        f"and explain why this dissipated energy cannot easily be captured to do useful work. (4 marks)"
    )
    sample_answer = (
        "Dissipated energy refers to energy that spreads out into the surrounding environment, primarily in the form of "
        "low-temperature heat and sound waves. Because this thermal energy spreads thinly across billions of air and surface molecules, "
        "it becomes disordered and dispersed (low grade), meaning it cannot easily be concentrated back to drive engines or perform mechanical work."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Definition of dissipation: Energy spreads out into the surrounding air/environment as low-temperature heat/sound (2 marks).\n"
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
