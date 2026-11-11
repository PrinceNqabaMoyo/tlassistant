"""Physical Sciences Grade 12 — Electrochemical Reactions & Galvanic Cells Dedicated Generator.

Curriculum Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 3/04. Electrochemical reactions.md
- Standard Reduction Potentials Table (Table 4A / 4B)

Complies with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=3, caps_weight_percent=20, suggested_duration_mins=10.
2. Deconstructible compound questions & atomic sub-drills.
3. Standardized Misconceptions.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Hints.
6. South African comma decimal convention (",").
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.physical_sciences.physical_sciences_builders import (
    build_electrolytic_cell_apparatus_question,
    build_galvanic_cell_question,
)

TOPIC = "grade12_electrochemistry_galvanic"

STANDARD_REDUCTION_POTENTIALS = {
    "Zn": {"symbol": "Zn", "half_rx": "\\text{Zn}^{2+} + 2e^- \\rightleftharpoons \\text{Zn}", "e0": -0.76, "name": "zinc"},
    "Cu": {"symbol": "Cu", "half_rx": "\\text{Cu}^{2+} + 2e^- \\rightleftharpoons \\text{Cu}", "e0": 0.34, "name": "copper"},
    "Mg": {"symbol": "Mg", "half_rx": "\\text{Mg}^{2+} + 2e^- \\rightleftharpoons \\text{Mg}", "e0": -2.37, "name": "magnesium"},
    "Ag": {"symbol": "Ag", "half_rx": "\\text{Ag}^+ + e^- \\rightleftharpoons \\text{Ag}", "e0": 0.80, "name": "silver"},
    "Pb": {"symbol": "Pb", "half_rx": "\\text{Pb}^{2+} + 2e^- \\rightleftharpoons \\text{Pb}", "e0": -0.13, "name": "lead"},
    "Ni": {"symbol": "Ni", "half_rx": "\\text{Ni}^{2+} + 2e^- \\rightleftharpoons \\text{Ni}", "e0": -0.27, "name": "nickel"},
    "Al": {"symbol": "Al", "half_rx": "\\text{Al}^{3+} + 3e^- \\rightleftharpoons \\text{Al}", "e0": -1.66, "name": "aluminium"},
}

PAIRS = [
    ("Zn", "Cu"),
    ("Mg", "Cu"),
    ("Al", "Cu"),
    ("Pb", "Ag"),
    ("Ni", "Ag"),
    ("Zn", "Ag"),
]


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_galvanic_derivation_question(
    r: random.Random, seed: Optional[int], idx: int, mode: str
) -> Dict[str, Any]:
    """Grade 12 Galvanic cell derivations, half-reactions, and standard EMF calculation."""
    anode_key, cathode_key = r.choice(PAIRS)
    anode_data = STANDARD_REDUCTION_POTENTIALS[anode_key]
    cathode_data = STANDARD_REDUCTION_POTENTIALS[cathode_key]

    e0_anode = anode_data["e0"]
    e0_cathode = cathode_data["e0"]
    e0_cell = round(e0_cathode - e0_anode, 2)

    qid = _make_id("ps12_galvanic_calc", seed, idx)

    prompt = (
        f"A standard electrochemical galvanic cell is set up consisting of a {anode_data['name']} ({anode_key}) half-cell "
        f"dipped in a $1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ {anode_key}$^{{2+}}$ electrolyte solution,\n"
        f"and a {cathode_data['name']} ({cathode_key}) half-cell dipped in a $1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ {cathode_key}$^{{2+}}$ electrolyte solution at $25^\\circ\\text{{C}}$.\n"
        f"Standard reduction potentials:\n"
        f"- $E^\\circ_{{\\text{{{anode_key}}}}} = {_fmt_sa(e0_anode)}\\text{{ V}}$\n"
        f"- $E^\\circ_{{\\text{{{cathode_key}}}}} = {_fmt_sa(e0_cathode)}\\text{{ V}}$\n\n"
        f"1. Identify the anode electrode and write down the oxidation half-reaction.\n"
        f"2. Write down the reduction half-reaction occurring at the cathode.\n"
        f"3. Write down the overall balanced cell reaction.\n"
        f"4. Write down the standard cell notation for this galvanic cell.\n"
        f"5. Calculate the standard cell potential ($E^\\circ_{{\\text{{cell}}}}$) in Volts.\n"
        f"6. State TWO vital functions of the salt bridge in this operating cell."
    )

    ans_str = (
        f"1. Anode: {anode_key}, {anode_key} -> {anode_key}^(2+) + 2e-; "
        f"2. {cathode_key}^(2+) + 2e- -> {cathode_key}; "
        f"3. {anode_key}(s) + {cathode_key}^(2+)(aq) -> {anode_key}^(2+)(aq) + {cathode_key}(s); "
        f"4. {anode_key}(s) | {anode_key}^(2+)(1 mol/dm3) || {cathode_key}^(2+)(1 mol/dm3) | {cathode_key}(s); "
        f"5. E0_cell = {_fmt_sa(e0_cell)} V; "
        f"6. Completes circuit, maintains electrical neutrality."
    )

    memo = (
        f"1. Anode identification & Oxidation [2]:\n"
        f"   - Anode: **{anode_data['name']} ({anode_key})** (lower reduction potential ${_fmt_sa(e0_anode)}\\text{{ V}}$) [1]\n"
        f"   - Oxidation half-reaction: $$\\text{{{anode_key}(s)}} \\to \\text{{{anode_key}}}^{{2+}}\\text{{(aq)}} + 2e^-$$ [1]\n"
        f"2. Cathode Reduction half-reaction [1]:\n"
        f"   $$\\text{{{cathode_key}}}^{{2+}}\\text{{(aq)}} + 2e^- \\to \\text{{{cathode_key}(s)}}$$ [1]\n"
        f"3. Balanced net cell equation [2]:\n"
        f"   $$\\text{{{anode_key}(s)}} + \\text{{{cathode_key}}}^{{2+}}\\text{{(aq)}} \\to \\text{{{anode_key}}}^{{2+}}\\text{{(aq)}} + \\text{{{cathode_key}(s)}}$$ [2]\n"
        f"4. Standard cell notation [2]:\n"
        f"   $$\\text{{{anode_key}(s)}} \\mid \\text{{{anode_key}}}^{{2+}}\\text{{(aq, 1 mol}}\\cdot\\text{{dm}}^{{-3}}\\text{{)}} \\parallel \\text{{{cathode_key}}}^{{2+}}\\text{{(aq, 1 mol}}\\cdot\\text{{dm}}^{{-3}}\\text{{)}} \\mid \\text{{{cathode_key}(s)}}$$ [2]\n"
        f"5. Standard cell potential [2]:\n"
        f"   $$E^\\circ_{{\\text{{cell}}}} = E^\\circ_{{\\text{{cathode}}}} - E^\\circ_{{\\text{{anode}}}} = ({_fmt_sa(e0_cathode)}) - ({_fmt_sa(e0_anode)}) = {_fmt_sa(e0_cell)}\\text{{ V}}$$ [1M + 1A]\n"
        f"6. Functions of the salt bridge [2]:\n"
        f"   - Completes the electric circuit [1]\n"
        f"   - Maintains electrical neutrality in both half-cells through migration of ions [1]"
    )

    hints = {
        "tier_1": "Recall: Anode is oxidation (loss of electrons). Cathode is reduction (gain of electrons).",
        "tier_2": f"Formula: E0_cell = E0_cathode - E0_anode = ({_fmt_sa(e0_cathode)}) - ({_fmt_sa(e0_anode)}).",
        "tier_3": f"E0_cell = {_fmt_sa(e0_cell)} V. Electrons flow from {anode_key} to {cathode_key}.",
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "diagram_spec": {
            "diagram_role": "context","kind": "galvanic_cell", "anode": anode_key, "cathode": cathode_key, "voltage": e0_cell},
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 11,
        "hints": hints,
        "misconception_tags": [
            "anode_cathode_inversion",
            "sign_error_standard_potential",
            "cell_notation_phase_boundary_inverted",
            "salt_bridge_function_misunderstood",
        ],
        "marking_schema": {
            "total_marks": 11,
            "marking_points": [
                {"id": "mp_1", "desc": "Anode identification and oxidation half-reaction", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Cathode reduction half-reaction", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Balanced net cell reaction", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Standard cell notation formatting", "marks": 2, "editable": True},
                {"id": "mp_5", "desc": "Standard cell potential calculation", "marks": 2, "editable": True},
                {"id": "mp_6", "desc": "Functions of salt bridge", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "omitted_volt_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "concepts",
    difficulty: str = "medium",
    count: int = 1,
    grade: str = "12",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Grade 12 Electrochemistry & Galvanic Cells."""
    r = random.Random(seed)
    questions = []

    for i in range(count):
        sub_seed = (seed + i * 43) if seed is not None else random.randint(1000, 99999)

        if mode == "scaffold" or subskill in ("galvanic_cell_diagram", "galvanic_cell_apparatus", "galvanic_cell"):
            q = build_galvanic_cell_question(seed=sub_seed, grade=12, mode=mode)
        elif subskill in ("electrolytic_cell", "electrolytic_cell_apparatus", "electrolysis_apparatus"):
            q = build_electrolytic_cell_apparatus_question(seed=sub_seed, grade=12, mode=mode)
        elif mode == "elementary_galvanic_potential":
            q = _generate_galvanic_derivation_question(r, sub_seed, i, mode)
        else:
            # Deterministic subskill cycling between Galvanic Cell, Electrolytic Cell, and cell potential calculations
            slot = (sub_seed + i) % 3
            if slot == 0:
                q = build_galvanic_cell_question(seed=sub_seed, grade=12, mode=mode)
            elif slot == 1:
                q = build_electrolytic_cell_apparatus_question(seed=sub_seed, grade=12, mode=mode)
            else:
                q = _generate_galvanic_derivation_question(r, sub_seed, i, mode)

        questions.append(q)

    return questions
