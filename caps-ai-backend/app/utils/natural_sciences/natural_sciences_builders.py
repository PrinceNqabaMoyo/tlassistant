"""Natural Sciences Grade 7-9 Diagram Subskill Builders.

Provides deterministic, 3-layer subskill builders for:
1. Distillation Apparatus Setup (distillation_apparatus) - Grade 7 Term 2 Matter & Materials
2. Particle Model of Matter (particle_model) - Grade 8 Term 2 Matter & Materials
3. Electric Circuit Series & Parallel (electric_circuits_ns) - Grade 8/9 Term 3 Energy & Change
4. Solar System & Planetary Mechanics (solar_system_earth_space) - Grade 7/8 Term 4 Planet Earth & Beyond

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import json
import os
import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

ANCHORS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "data",
    "diagram_anchors",
)


def _load_anchors(master_name: str) -> Dict[str, Any]:
    path = os.path.join(ANCHORS_DIR, f"{master_name}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


DISTILLATION_DATA = _load_anchors("distillation_apparatus")
PARTICLE_DATA = _load_anchors("particle_model")
CIRCUIT_DATA = _load_anchors("electric_circuits_ns")
SOLAR_DATA = _load_anchors("solar_system_earth_space")
ATOMIC_BOHR_DATA = _load_anchors("atomic_bohr_structure")
CHEMICAL_BONDING_DATA = _load_anchors("chemical_bonding_molecules")
ELECTROLYTIC_CELL_DATA = _load_anchors("electrolytic_cell_apparatus")
GAS_EVOLUTION_DATA = _load_anchors("gas_evolution_rate_apparatus")
PULLEY_INCLINE_DATA = _load_anchors("pulley_incline_masses_system")
AC_DC_GENERATOR_DATA = _load_anchors("ac_dc_generator_motor_apparatus")
EARTH_LITHOSPHERE_DATA = _load_anchors("earth_lithosphere_layers")


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns_salt"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


DOMAIN_TERMINOLOGY: Dict[str, Dict[str, str]] = {
    "distillation_apparatus": {
        "intro": "Refer to the laboratory fractional/simple distillation apparatus diagram.",
        "noun": "laboratory apparatus component",
        "context": "during the thermal separation of a liquid mixture",
    },
    "electric_circuits_ns": {
        "intro": "Refer to the electric circuit diagram.",
        "noun": "circuit component or measuring instrument",
        "context": "within the electrical circuit",
    },
    "solar_system_earth_space": {
        "intro": "Refer to the Solar System and celestial mechanics diagram.",
        "noun": "celestial body or orbital region",
        "context": "within the Solar System",
    },
    "earth_lithosphere_layers": {
        "intro": "Refer to the cross-sectional diagram of the Earth's internal layers and spheres.",
        "noun": "concentric Earth layer or geological region",
        "context": "within the structure of Planet Earth",
    },
}


def _build_generic_diagram_question(
    data: Dict[str, Any],
    master_name: str,
    component_name: str,
    seed: int,
    grade: int,
    term: int,
    qid_prefix: str,
    subskill_choices: List[str],
    subskill: Optional[str] = None,
    mode: str = "practice",
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = data["anchors"]
    grade_str = f"g{grade}"
    allowed_keys = [
        k for k, v in anchors.items()
        if grade_str in v.get("grades", [grade_str])
    ]
    if len(allowed_keys) < 4:
        allowed_keys = list(anchors.keys())

    if subskill is None or subskill not in subskill_choices:
        subskill = subskill_choices[seed % len(subskill_choices)]

    target_key = allowed_keys[seed % len(allowed_keys)]
    target = anchors[target_key]
    target_name = target.get("name") or target.get("acceptable", [target_key])[0]

    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    active_keys = [target_key] + other_keys[:3]
    r.shuffle(active_keys)

    pin_letters = ["A", "B", "C", "D"]
    client_pins: List[Dict[str, Any]] = []
    server_solution_map: Dict[str, str] = {}
    target_pin_letter = ""

    for idx, key in enumerate(active_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, key, idx)
        if key == target_key:
            target_pin_letter = letter

        akey_name = anchors[key].get("name") or anchors[key].get("acceptable", [key])[0]
        server_solution_map[letter] = akey_name
        client_pins.append({
            "pin": letter,
            "ref": ref,
            "anchor": anchors[key]["anchor"],
            "default_box": anchors[key]["default_box"],
            "side": anchors[key]["side"],
            "role": "target" if key == target_key else "distractor",
        })

    domain = DOMAIN_TERMINOLOGY.get(master_name, {
        "intro": "Refer to the scientific diagram.",
        "noun": "structure or component",
        "context": "in the scientific system shown",
    })

    qid = f"{qid_prefix}_{seed}_{subskill[:4]}"
    prompt = (
        f"{domain['intro']}\n\n"
        f"1. Identify the {domain['noun']} labeled with callout ({target_pin_letter}).\n"
        f"2. Describe the key scientific property, role, or physical principle of this {domain['noun']} {domain['context']}."
    )
    correct_ans = f"1. {target_name}\n2. {target['description']}"
    memo = (
        f"Step 1: Identify callout ({target_pin_letter}):\n"
        f"{target_name} (1 mark)\n\n"
        f"Step 2: Scientific property / function:\n"
        f"{target['description']} (2 marks)"
    )
    hints = {
        "tier_1": f"Observe where callout ({target_pin_letter}) points on the diagram.",
        "tier_2": f"Callout ({target_pin_letter}) indicates {target_name.lower()}.",
        "tier_3": f"1. {target_name}. 2. {target['description']}",
    }
    marks = 3

    return {
        "id": qid,
        "question_id": qid,
        "prompt": prompt,
        "term": term,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 8,
        "mode": mode,
        "subskill": subskill,
        "question_type": "diagram_short_answer",
        "question": prompt,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "sample_answer": memo,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["component_misidentification", "incorrect_functional_role"],
        "modality": "bio_diagram",
        "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin_letter") or locals().get("target_pin") else "context",
            "image_type": master_name,
            "master": master_name,
            "view": "textbook",
            "grade_mask": grade_str,
            "component": component_name,
            "viewBox": "0 0 600 480",
            "locked_view": True,
            "pins": client_pins,
            "landmarks": [],
            "target_pin": target_pin_letter,
            "target_key": target_key,
        },
        "diagram_meta": {
            "master": master_name,
            "view": "textbook",
            "grade_mask": grade_str,
            "target_pin": target_pin_letter,
            "target_key": target_key,
        },
        "diagram": {
            "master": master_name,
            "view": "textbook",
            "grade_mask": grade_str,
            "component": component_name,
            "viewBox": "0 0 600 480",
            "locked_view": True,
            "pins": client_pins,
            "landmarks": [],
        },
        "_server_solution": {
            "target_key": target_key,
            "target_pin": target_pin_letter,
            "pin_map": server_solution_map,
        },
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"1. Identification of callout ({target_pin_letter}): {target_name}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"2. Scientific property or function: {target['description']}", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_distillation_apparatus_question(
    seed: int,
    grade: int = 7,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 7 Term 2: Separating mixtures using simple distillation apparatus."""
    sub_choices = ["apparatus_identification", "thermal_separation_principle", "cooling_water_flow"]
    if subskill is None or subskill not in sub_choices:
        subskill = sub_choices[seed % len(sub_choices)]

    if subskill == "apparatus_identification":
        return _build_generic_diagram_question(
            data=DISTILLATION_DATA,
            master_name="distillation_apparatus",
            component_name="DistillationApparatusSvg",
            seed=seed,
            grade=grade,
            term=2,
            qid_prefix=f"ns{grade}_distill_app",
            subskill_choices=["apparatus_identification"],
            subskill="apparatus_identification",
            mode=mode,
        )

    grade_str = f"g{grade}"
    landmarks = [
        {"text": "Thermometer", "name": "Thermometer", "anchor": [219, 130], "default_box": [60, 85], "side": "left"},
        {"text": "Distillation Flask", "name": "Distillation Flask", "anchor": [195, 225], "default_box": [60, 165], "side": "left"},
        {"text": "Heat Source", "name": "Heat Source", "anchor": [219, 345], "default_box": [60, 405], "side": "left"},
        {"text": "Liebig Condenser", "name": "Liebig Condenser", "anchor": [357, 230], "default_box": [540, 185], "side": "right"},
        {"text": "Cooling Water In", "name": "Cooling Water In", "anchor": [405, 270], "default_box": [540, 275], "side": "right"},
        {"text": "Receiving Flask", "name": "Receiving Flask", "anchor": [465, 345], "default_box": [540, 365], "side": "right"},
    ]

    if subskill == "thermal_separation_principle":
        mixture_scenarios = [
            ("ethanol and water", 78, 100, "ethanol"),
            ("acetone and water", 56, 100, "acetone"),
            ("pure water from salty sea water", 100, 1465, "pure water"),
        ]
        mix_name, bp_a, bp_b, volatile = mixture_scenarios[seed % len(mixture_scenarios)]

        prompt = (
            f"Refer to the simple distillation apparatus diagram used to separate a mixture of {mix_name}.\n\n"
            f"1. State the fundamental physical property that enables components of a liquid mixture to be separated by distillation. (1)\n"
            f"2. Name the component in the diagram where **evaporation** takes place and the component where **condensation** takes place. (2)\n"
            f"3. In separating {mix_name} (boiling points: {bp_a} °C and {bp_b} °C), explain why {volatile} distils and collects in the receiving flask first. (2)"
        )
        sample_ans = (
            f"1. Difference in boiling points between the components.\n"
            f"2. Evaporation occurs in the Distillation Flask; Condensation occurs in the Liebig Condenser.\n"
            f"3. {volatile.capitalize()} has a lower boiling point ({bp_a} °C) than the other component ({bp_b} °C). "
            f"When thermal energy is applied, {volatile} reaches its boiling point first, vaporises, passes into the condenser, and condenses into a liquid."
        )
        memo = (
            f"Step 1: Physical property:\n"
            f"Difference in **boiling points** [1]\n\n"
            f"Step 2: Apparatus phase change locations:\n"
            f"- Evaporation: **Distillation flask** (round-bottomed flask) [1]\n"
            f"- Condensation: **Liebig condenser** [1]\n\n"
            f"Step 3: Why {volatile} separates first:\n"
            f"{volatile.capitalize()} has the lower boiling point ({bp_a} °C) [1]. "
            f"It reaches its boiling point first, vaporises into a gas, and passes into the condenser before the second component boils [1]."
        )
        qid = f"ns{grade}_distill_thermal_{seed}"
        return {
            "id": qid,
            "question_id": qid,
            "term": 2,
            "caps_weight_percent": 18,
            "suggested_duration_mins": 8,
            "mode": mode,
            "subskill": "thermal_separation_principle",
            "question_type": "diagram_short_answer",
            "question": prompt,
            "question_text": prompt,
            "prompt": prompt,
            "correct_answer": sample_ans,
            "sample_answer": sample_ans,
            "worked_solution": memo,
            "explanation": memo,
            "marks": 5,
            "hints": {
                "tier_1": "Distillation relies on differences in boiling points between substances.",
                "tier_2": "Evaporation happens in the heated flask; condensation happens in the cold Liebig condenser.",
                "tier_3": f"1. Boiling point difference. 2. Flask (evaporation), Condenser (condensation). 3. {volatile} boils at a lower temperature.",
            },
            "misconception_tags": ["confused_evaporation_with_condensation", "boiling_point_order_inversion"],
            "modality": "bio_diagram",
            "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin_letter") or locals().get("target_pin") else "context",
                "image_type": "distillation_apparatus",
                "master": "distillation_apparatus",
                "view": "textbook",
                "grade_mask": grade_str,
                "component": "DistillationApparatusSvg",
                "viewBox": "0 0 600 480",
                "locked_view": True,
                "pins": [],
                "landmarks": landmarks,
            },
            "marking_schema": {
                "total_marks": 5,
                "marking_points": [
                    {"id": "mp_1", "desc": "Difference in boiling points", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Evaporation in distillation flask", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Condensation in Liebig condenser", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": f"Identification of lower boiling point ({bp_a} °C)", "marks": 1, "editable": True},
                    {"id": "mp_5", "desc": "Vaporises first and enters condenser", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
        }

    else:  # cooling_water_flow
        apparatus_scenarios = [
            ("during a laboratory distillation of muddy river water into potable drinking water", "river water distillate"),
            ("while purifying an ethanol-water fermented solution in a high school chemistry practical", "ethanol vapour"),
            ("in an environmental science investigation testing water samples from a local borehole", "distilled freshwater"),
            ("during an experiment testing the efficiency of Liebig condenser heat exchange", "condensing steam vapour"),
        ]
        context_desc, vapour_type = apparatus_scenarios[seed % len(apparatus_scenarios)]

        prompt = (
            f"Refer to the Liebig condenser in the laboratory distillation apparatus diagram {context_desc}.\n\n"
            f"1. State whether cold cooling water must enter at the bottom (lower inlet) or at the top (upper outlet) of the condenser jacket to condense the {vapour_type}. (1)\n"
            f"2. Give two scientific reasons why the cooling water must enter at the lowest point and leave at the highest point. (2)\n"
            f"3. State what would happen inside the condenser jacket if water entered from the top instead. (1)"
        )
        sample_ans = (
            "1. Cold water enters at the bottom (lower inlet).\n"
            "2. Reasons: (a) It ensures the outer jacket is completely filled with cold water without air pockets or bubbles; "
            "(b) It creates an efficient counter-current temperature gradient where the coldest water meets the cooler vapour at the exit.\n"
            "3. If water enters at the top, water would run straight down by gravity, leaving air pockets and resulting in incomplete condensation."
        )
        memo = (
            "Step 1: Water inlet direction:\n"
            "Cold water enters at the **bottom** (lower connection) [1]\n\n"
            "Step 2: Two scientific reasons:\n"
            "- Reason 1: Completely fills the glass jacket with water, preventing air locks/bubbles [1]\n"
            "- Reason 2: Ensures counter-current cooling, maintaining maximum temperature difference along the tube for complete condensation [1]\n\n"
            "Step 3: Consequence of reversed flow:\n"
            "Water drains too quickly by gravity, leaving large air gaps that reduce cooling efficiency, allowing hot vapour to escape uncondensed [1]"
        )
        qid = f"ns{grade}_distill_water_{seed}"
        return {
            "id": qid,
            "question_id": qid,
            "term": 2,
            "caps_weight_percent": 18,
            "suggested_duration_mins": 6,
            "mode": mode,
            "subskill": "cooling_water_flow",
            "question_type": "diagram_short_answer",
            "question": prompt,
            "question_text": prompt,
            "prompt": prompt,
            "correct_answer": sample_ans,
            "sample_answer": sample_ans,
            "worked_solution": memo,
            "explanation": memo,
            "marks": 4,
            "hints": {
                "tier_1": "Water flows from bottom to top against gravity so the condenser jacket stays completely full.",
                "tier_2": "Entering at the bottom prevents air bubbles and keeps the inner tube surrounded by cold water.",
                "tier_3": "1. Bottom inlet. 2. Keeps jacket completely full and prevents air locks. 3. Vapour escapes uncondensed.",
            },
            "misconception_tags": ["condenser_water_flow_reversal", "confused_inner_and_outer_tube"],
            "modality": "bio_diagram",
            "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin_letter") or locals().get("target_pin") else "context",
                "image_type": "distillation_apparatus",
                "master": "distillation_apparatus",
                "view": "textbook",
                "grade_mask": grade_str,
                "component": "DistillationApparatusSvg",
                "viewBox": "0 0 600 480",
                "locked_view": True,
                "pins": [],
                "landmarks": landmarks,
            },
            "marking_schema": {
                "total_marks": 4,
                "marking_points": [
                    {"id": "mp_1", "desc": "Cold water enters at bottom / lower inlet", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Keeps jacket completely filled without air bubbles", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Maintains counter-current thermal gradient for complete condensation", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": "Reversal causes air pockets and hot vapour escape", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
        }


def build_particle_model_question(
    seed: int,
    grade: int = 8,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 8 Term 2: Particle model of matter (Role P: Process/State Comparison, zero A-D pins)."""
    subskill_choices = ["particle_arrangement", "kinetic_energy_states", "phase_change_transitions"]
    if subskill is None or subskill not in subskill_choices:
        subskill = subskill_choices[seed % len(subskill_choices)]

    grade_str = f"g{grade}"
    landmarks = [
        {"text": "Solid State", "name": "Solid State", "anchor": [179, 283], "default_box": [60, 260], "side": "left"},
        {"text": "Melting", "name": "Melting", "anchor": [237, 105], "default_box": [60, 100], "side": "left"},
        {"text": "Freezing", "name": "Freezing", "anchor": [237, 375], "default_box": [60, 385], "side": "left"},
        {"text": "Liquid State", "name": "Liquid State", "anchor": [301, 282], "default_box": [540, 280], "side": "right"},
        {"text": "Evaporation / Boiling", "name": "Evaporation / Boiling", "anchor": [363, 105], "default_box": [540, 100], "side": "right"},
        {"text": "Gas State", "name": "Gas State", "anchor": [414, 221], "default_box": [540, 185], "side": "right"},
        {"text": "Condensation", "name": "Condensation", "anchor": [363, 375], "default_box": [540, 385], "side": "right"},
    ]

    scenarios = [
        {
            "sub": "particle_arrangement",
            "prompt": (
                "Refer to the Particle Model of Matter diagram showing the Solid State, Liquid State, and Gas State.\n\n"
                "1. Compare the arrangement and spacing of particles in the Solid State versus the Gas State. (2)\n"
                "2. Explain why a gas can be easily compressed into a smaller volume, whereas a solid cannot be compressed. (2)"
            ),
            "sample_answer": (
                "1. In the Solid State, particles are closely packed in a regular, fixed lattice with minimal spaces between them. "
                "In the Gas State, particles are randomly arranged and very far apart with large empty spaces between them.\n"
                "2. A gas has large empty spaces between its particles, allowing the particles to be pushed closer together under pressure. "
                "In a solid, particles are already tightly packed with almost no empty space between them."
            ),
            "marking_points": [
                {"id": "mp_1", "desc": "Solid state: closely packed in a regular/fixed lattice with minimal spaces", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Gas state: randomly arranged and very far apart", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Gas compressibility explained by large empty spaces between gas particles vs tightly packed solid particles", "marks": 2, "editable": True},
            ],
            "h1": "Compare how closely the spheres are packed in the Solid State container versus the Gas State container.",
            "h2": "Compression requires empty space between particles so they can be pushed closer together.",
            "h3": "1. Solid: regular fixed lattice, closely packed; Gas: random, widely spaced. 2. Gases have large empty spaces between particles that can be reduced under pressure.",
        },
        {
            "sub": "kinetic_energy_states",
            "prompt": (
                "Refer to the Particle Model of Matter diagram showing the transitions from Solid State to Liquid State (Melting) and from Liquid State to Gas State (Evaporation / Boiling).\n\n"
                "1. Describe how the movement and kinetic energy of the particles change when a substance is heated from the Solid State to the Liquid State during Melting. (2)\n"
                "2. State how the strength of the forces of attraction between particles in the Gas State compares to those in the Solid State. (2)"
            ),
            "sample_answer": (
                "1. When heated during Melting, particles absorb thermal energy and their average kinetic energy increases. "
                "They vibrate more vigorously until they overcome their fixed lattice positions and slide past one another in the Liquid State.\n"
                "2. The forces of attraction between particles in the Gas State are very weak (negligible), whereas the forces of attraction in the Solid State are very strong."
            ),
            "marking_points": [
                {"id": "mp_1", "desc": "Particles absorb heat / average kinetic energy increases during Melting", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Particles break free from fixed positions to slide past one another as a liquid", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Forces of attraction are very weak/negligible in Gas State compared to very strong forces in Solid State", "marks": 2, "editable": True},
            ],
            "h1": "Heating adds thermal energy to the particles, affecting how fast they vibrate and move.",
            "h2": "In a solid, particles only vibrate in fixed positions; in a liquid, they have enough kinetic energy to slide past each other.",
            "h3": "1. Kinetic energy increases and particles overcome fixed lattice positions to slide past one another. 2. Attractive forces are very weak in a gas and very strong in a solid.",
        },
        {
            "sub": "phase_change_transitions",
            "prompt": (
                "Refer to the Particle Model of Matter phase-transition pathways shown in the diagram.\n\n"
                "1. Identify which two phase transitions shown on the diagram require heat energy to be removed (cooling) from the substance. (2)\n"
                "2. Explain what happens to the speed and spacing of gas particles during Condensation to form a liquid. (2)"
            ),
            "sample_answer": (
                "1. Condensation (Gas State to Liquid State) and Freezing (Liquid State to Solid State) require heat energy to be removed.\n"
                "2. During Condensation, gas particles lose kinetic energy and move more slowly, allowing attractive forces to pull the particles much closer together into a disordered liquid cluster."
            ),
            "marking_points": [
                {"id": "mp_1", "desc": "Identifies Condensation and Freezing as cooling phase transitions", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Gas particles lose kinetic energy / slow down and move closer together due to attractive forces", "marks": 2, "editable": True},
            ],
            "h1": "Follow the arrows that move from higher-energy states (Gas, Liquid) to lower-energy states (Liquid, Solid).",
            "h2": "Cooling removes kinetic energy, causing fast-moving gas particles to slow down.",
            "h3": "1. Condensation and Freezing. 2. Gas particles slow down (lose kinetic energy) and attractive forces draw them closer together into a liquid.",
        },
    ]

    scen = scenarios[seed % len(scenarios)]
    qid = f"ns{grade}_particle_{seed}_{subskill[:4]}"

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 8,
        "mode": mode,
        "subskill": subskill,
        "question_type": "diagram_short_answer",
        "question": scen["prompt"],
        "question_text": scen["prompt"],
        "correct_answer": scen["sample_answer"],
        "sample_answer": scen["sample_answer"],
        "worked_solution": scen["sample_answer"],
        "explanation": scen["sample_answer"],
        "marks": 4,
        "hints": {
            "tier_1": scen["h1"],
            "tier_2": scen["h2"],
            "tier_3": scen["h3"],
        },
        "misconception_tags": ["particles_expand_when_heated", "confused_phase_transition_direction"],
        "modality": "bio_diagram",
        "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin_letter") or locals().get("target_pin") else "context",
            "image_type": "particle_model",
            "master": "particle_model",
            "view": "textbook",
            "grade_mask": grade_str,
            "component": "ParticleModelSvg",
            "viewBox": "0 0 600 480",
            "locked_view": True,
            "pins": [],
            "landmarks": landmarks,
        },
        "diagram_meta": {
            "master": "particle_model",
            "view": "textbook",
            "grade_mask": grade_str,
        },
        "diagram": {
            "master": "particle_model",
            "view": "textbook",
            "grade_mask": grade_str,
            "component": "ParticleModelSvg",
            "viewBox": "0 0 600 480",
            "locked_view": True,
            "pins": [],
            "landmarks": landmarks,
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": scen["marking_points"],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_electric_circuit_ns_question(
    seed: int,
    grade: int = 8,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 8/9 Term 3: Electric circuits (series vs parallel, meters, resistance)."""
    return _build_generic_diagram_question(
        data=CIRCUIT_DATA,
        master_name="electric_circuits_ns",
        component_name="ElectricCircuitsNsSvg",
        seed=seed,
        grade=grade,
        term=3,
        qid_prefix=f"ns{grade}_circuit",
        subskill_choices=["circuit_components", "meter_connection_rules", "parallel_vs_series_behavior"],
        subskill=subskill,
        mode=mode,
    )


def build_solar_system_question(
    seed: int,
    grade: int = 8,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 7/8 Term 4: Solar system and celestial mechanics."""
    return _build_generic_diagram_question(
        data=SOLAR_DATA,
        master_name="solar_system_earth_space",
        component_name="SolarSystemEarthSpaceSvg",
        seed=seed,
        grade=grade,
        term=4,
        qid_prefix=f"ns{grade}_solar",
        subskill_choices=["planetary_order", "axial_tilt_seasons", "eclipses_and_lunar_phases"],
        subskill=subskill,
        mode=mode,
    )


def build_atomic_bohr_ns_question(
    seed: int,
    grade: int = 8,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 8/9 Term 2: Atoms and the Periodic Table (subatomic particles & Bohr shells)."""
    return _build_generic_diagram_question(
        data=ATOMIC_BOHR_DATA,
        master_name="atomic_bohr_structure",
        component_name="AtomicBohrStructureSvg",
        seed=seed,
        grade=grade,
        term=2,
        qid_prefix=f"ns{grade}_bohr",
        subskill_choices=["subatomic_particles", "nucleus_vs_electron_shells", "atomic_number_identity"],
        subskill=subskill,
        mode=mode,
    )


def build_chemical_bonding_ns_question(
    seed: int,
    grade: int = 9,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 8/9 Term 2: Compounds and chemical reactions (diatomic/triatomic molecules & lattices)."""
    return _build_generic_diagram_question(
        data=CHEMICAL_BONDING_DATA,
        master_name="chemical_bonding_molecules",
        component_name="ChemicalBondingMoleculesSvg",
        seed=seed,
        grade=grade,
        term=2,
        qid_prefix=f"ns{grade}_bonding",
        subskill_choices=["molecular_compounds", "chemical_bonds", "crystal_lattice_structure"],
        subskill=subskill,
        mode=mode,
    )


def build_electrolytic_cell_ns_question(
    seed: int,
    grade: int = 8,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 8/9 Term 3: Chemical effect of an electric current (electrolysis of CuCl₂)."""
    return _build_generic_diagram_question(
        data=ELECTROLYTIC_CELL_DATA,
        master_name="electrolytic_cell_apparatus",
        component_name="ElectrolyticCellApparatusSvg",
        seed=seed,
        grade=grade,
        term=3,
        qid_prefix=f"ns{grade}_electrolysis",
        subskill_choices=["electrolysis_electrodes", "chlorine_gas_evolution", "copper_metal_plating"],
        subskill=subskill,
        mode=mode,
    )


def build_gas_evolution_ns_question(
    seed: int,
    grade: int = 9,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 9 Term 2: Reactions of acids with metals and carbonates (gas collection)."""
    return _build_generic_diagram_question(
        data=GAS_EVOLUTION_DATA,
        master_name="gas_evolution_rate_apparatus",
        component_name="GasEvolutionRateApparatusSvg",
        seed=seed,
        grade=grade,
        term=2,
        qid_prefix=f"ns{grade}_gas_evol",
        subskill_choices=["acid_metal_gas_collection", "delivery_tube_syringe", "reaction_rate_observation"],
        subskill=subskill,
        mode=mode,
    )


def build_pulley_incline_ns_question(
    seed: int,
    grade: int = 9,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 7/9 Term 3: Forces, tension, and mechanical energy systems."""
    return _build_generic_diagram_question(
        data=PULLEY_INCLINE_DATA,
        master_name="pulley_incline_masses_system",
        component_name="PulleyInclineMassesSystemSvg",
        seed=seed,
        grade=grade,
        term=3,
        qid_prefix=f"ns{grade}_pulley",
        subskill_choices=["contact_and_field_forces", "tension_and_pulley", "gravitational_potential_energy"],
        subskill=subskill,
        mode=mode,
    )


def build_generator_grid_ns_question(
    seed: int,
    grade: int = 9,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 9 Term 3: Energy and the national electricity grid (AC generator turbines)."""
    return _build_generic_diagram_question(
        data=AC_DC_GENERATOR_DATA,
        master_name="ac_dc_generator_motor_apparatus",
        component_name="AcDcGeneratorMotorApparatusSvg",
        seed=seed,
        grade=grade,
        term=3,
        qid_prefix=f"ns{grade}_generator",
        subskill_choices=["generator_coil_and_magnets", "mechanical_to_electrical_energy", "national_grid_generation"],
        subskill=subskill,
        mode=mode,
    )


def build_earth_lithosphere_layers_question(
    seed: int,
    grade: int = 9,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Grade 7/9 Term 4: The Earth as a system & Concentric layers of the lithosphere."""
    return _build_generic_diagram_question(
        data=EARTH_LITHOSPHERE_DATA,
        master_name="earth_lithosphere_layers",
        component_name="EarthLithosphereLayersSvg",
        seed=seed,
        grade=grade,
        term=4,
        qid_prefix=f"ns{grade}_earth_layers",
        subskill_choices=["four_earth_spheres", "concentric_internal_layers", "lithosphere_and_rock_cycle"],
        subskill=subskill,
        mode=mode,
    )
