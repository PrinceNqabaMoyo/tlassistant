"""Natural Sciences (Grades 8–9) — Electric Circuits & Ohm's Law (Deterministic 6-Pillar Generator).
Covers series and parallel resistors, current, potential difference, Ohm's law (V = IR), and power (P = VI).
Supports full compound circuit analysis and atomic elementary sub-drills for adaptive regression.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import (
    fmt_sa,
    make_science_question,
    rng,
)

TOPIC = "natural_sciences_electric_circuits"
LO = "ns_electric_circuits"

# Pre-calculated clean parallel pairs: (R2, R3, Rp)
PARALLEL_PAIRS = [
    (6, 3, 2),
    (12, 4, 3),
    (10, 10, 5),
    (12, 6, 4),
    (20, 5, 4),
    (8, 8, 4),
    (15, 10, 6),
]


# --------------------------------------------------------------------------- #
# Sub-Drill: Ohm's Law Single Component
# --------------------------------------------------------------------------- #
def _build_ohms_law_drill(r: random.Random, difficulty: str) -> Dict[str, Any]:
    target = r.choice(["V", "I", "R"])
    i_val = r.choice([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0])
    r_val = r.choice([2, 3, 4, 5, 6, 8, 10, 12])
    v_val = round(i_val * r_val, 2)

    if target == "V":
        prompt = (
            f"A resistor of resistance $R = {fmt_sa(r_val)}\\ \\Omega$ has an electric current of "
            f"$I = {fmt_sa(i_val)}\\text{{ A}}$ passing through it.\n\n"
            f"Calculate the potential difference (voltage) $V$ across the resistor."
        )
        ans_latex = rf"V = I \times R = ({fmt_sa(i_val)}\text{{ A}}) \times ({fmt_sa(r_val)}\ \Omega) = {fmt_sa(v_val)}\text{{ V}}"
        calc_step = f"V = {fmt_sa(v_val)} V"
    elif target == "I":
        prompt = (
            f"A potential difference of $V = {fmt_sa(v_val)}\\text{{ V}}$ is measured across a "
            f"resistor of resistance $R = {fmt_sa(r_val)}\\ \\Omega$.\n\n"
            f"Calculate the electric current $I$ passing through the resistor."
        )
        ans_latex = rf"I = \frac{{V}}{{R}} = \frac{{{fmt_sa(v_val)}\text{{ V}}}}{{{fmt_sa(r_val)}\ \Omega}} = {fmt_sa(i_val)}\text{{ A}}"
        calc_step = f"I = {fmt_sa(i_val)} A"
    else:
        prompt = (
            f"An electric current of $I = {fmt_sa(i_val)}\\text{{ A}}$ flows through a conductor when a "
            f"potential difference of $V = {fmt_sa(v_val)}\\text{{ V}}$ is applied across its ends.\n\n"
            f"Calculate the resistance $R$ of the conductor."
        )
        ans_latex = rf"R = \frac{{V}}{{I}} = \frac{{{fmt_sa(v_val)}\text{{ V}}}}{{{fmt_sa(i_val)}\text{{ A}}}} = {fmt_sa(r_val)}\ \Omega"
        calc_step = rf"R = {fmt_sa(r_val)}\ \Omega"

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Correct Ohm's Law formula (V = IR or rearrangement)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct numerical substitution", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Final answer with correct SI unit", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_or_incorrect_unit", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Identify which two quantities are given and which one is the unknown.",
        "concept": "Ohm's Law states that $V = I \\times R$, where $V$ is in volts (V), $I$ in amperes (A), and $R$ in ohms ($\\Omega$).",
        "breakdown": f"Substitute into Ohm's law: {ans_latex}",
    }

    return make_science_question(
        prefix="ns_circ_ohm",
        topic=TOPIC,
        subskill="ohms_law_elementary",
        learning_objective_id=f"{LO}_ohms_law",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=ans_latex,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["inverted_ohms_law_ratio", "omitted_or_incorrect_unit"],
        keywords=["Ohm's law", "resistance", "potential difference", "current", "volts", "amperes", "ohms"],
        term=3,
        caps_weight_percent=25,
        suggested_duration_mins=3,
        mode="elementary_ohms_law",
        difficulty="medium",
        marks=3,
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Series Resistance Calculation
# --------------------------------------------------------------------------- #
def _build_series_resistance_drill(r: random.Random, difficulty: str) -> Dict[str, Any]:
    n = r.choice([2, 3])
    vals = [r.choice([2, 3, 4, 5, 6, 8, 10, 12]) for _ in range(n)]
    total_r = sum(vals)

    resistors_str = ", ".join([f"$R_{i+1} = {v}\\ \\Omega$" for i, v in enumerate(vals)])
    formula_str = " + ".join([f"R_{i+1}" for i in range(n)])
    subst_str = " + ".join([f"{v}\\ \\Omega" for v in vals])

    prompt = (
        f"Three resistors are connected in series in an electric circuit: {resistors_str}.\n\n"
        f"Calculate the total equivalent resistance ($R_s$) of the combination."
    )
    ans_latex = rf"R_s = {formula_str} = {subst_str} = {total_r}\ \Omega"

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": "Formula $R_s = R_1 + R_2 + \\dots$ and substitution", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Final resistance with unit $\\Omega$", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_or_incorrect_unit", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "In a series circuit, there is only one pathway for the electric current.",
        "concept": "For resistors in series, the total resistance is simply the sum of individual resistances: $R_s = R_1 + R_2 + \\dots$.",
        "breakdown": f"Add the resistances: {ans_latex}",
    }

    return make_science_question(
        prefix="ns_circ_series",
        topic=TOPIC,
        subskill="series_resistance_elementary",
        learning_objective_id=f"{LO}_series_resistors",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=ans_latex,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["inverted_series_resistance_formula", "omitted_or_incorrect_unit"],
        keywords=["series circuit", "equivalent resistance", "resistors in series", "ohms"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=2,
        mode="elementary_series_resistance",
        difficulty="easy",
        marks=2,
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Parallel Resistance Calculation
# --------------------------------------------------------------------------- #
def _build_parallel_resistance_drill(r: random.Random, difficulty: str) -> Dict[str, Any]:
    r2, r3, rp = r.choice(PARALLEL_PAIRS)

    prompt = (
        f"Two resistors of resistance $R_1 = {r2}\\ \\Omega$ and $R_2 = {r3}\\ \\Omega$ "
        f"are connected in parallel across two points in a circuit.\n\n"
        f"Calculate the equivalent resistance ($R_p$) of this parallel combination."
    )

    prod_r = r2 * r3
    sum_r = r2 + r3
    ans_latex = (
        rf"\frac{{1}}{{R_p}} = \frac{{1}}{{R_1}} + \frac{{1}}{{R_2}} = \frac{{1}}{{{r2}}} + \frac{{1}}{{{r3}}} "
        rf"= \frac{{{sum_r}}}{{{prod_r}}} = \frac{{1}}{{{rp}}} \implies R_p = {rp}\ \Omega"
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula $\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2}$", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Substitution and fraction addition", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Inverting to find $R_p$ with correct unit $\\Omega$", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "forgot_to_invert_reciprocal", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Remember that adding resistors in parallel decreases the overall equivalent resistance.",
        "concept": "For parallel resistors: $\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2}$. Remember to invert the fraction at the end to find $R_p$.",
        "breakdown": f"$\\frac{{1}}{{R_p}} = \\frac{{1}}{{{r2}}} + \\frac{{1}}{{{r3}}} = \\frac{{1}}{{{rp}}} \\implies R_p = {rp}\\ \\Omega$.",
    }

    return make_science_question(
        prefix="ns_circ_par",
        topic=TOPIC,
        subskill="parallel_resistance_elementary",
        learning_objective_id=f"{LO}_parallel_resistors",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=ans_latex,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["added_parallel_resistors_directly", "forgot_to_invert_reciprocal"],
        keywords=["parallel circuit", "equivalent resistance", "reciprocal rule", "ohms"],
        term=3,
        caps_weight_percent=25,
        suggested_duration_mins=3,
        mode="elementary_parallel_resistance",
        difficulty="medium",
        marks=3,
    )


# --------------------------------------------------------------------------- #
# Compound: Authentic CAPS Exam Standard Circuit Analysis (8 Marks)
# --------------------------------------------------------------------------- #
def _build_compound_circuit(r: random.Random, difficulty: str) -> Dict[str, Any]:
    # Select clean parallel pair and series resistor
    r2, r3, rp = r.choice(PARALLEL_PAIRS)
    r1 = r.choice([1, 2, 3, 4, 6])
    r_total = r1 + rp

    # Pick integer total current It (1, 2, or 3 A)
    i_total = r.choice([1, 2, 3])
    v_total = i_total * r_total

    # Voltages
    v1 = i_total * r1
    vp = i_total * rp

    # Branch currents
    i2 = round(vp / r2, 2)
    i3 = round(vp / r3, 2)

    # Power in battery
    power_total = v_total * i_total

    prompt = (
        f"In the circuit diagram below, a battery of cells provides a constant potential difference of "
        f"$V = {v_total}\\text{{ V}}$. Connected to the battery is a series resistor $R_1 = {r1}\\ \\Omega$, "
        f"followed by a parallel branch consisting of two resistors, $R_2 = {r2}\\ \\Omega$ and $R_3 = {r3}\\ \\Omega$.\n\n"
        f"Calculate:\n"
        f"1. The equivalent resistance of the parallel combination ($R_p$).\n"
        f"2. The total resistance of the complete circuit ($R_{{\\text{{total}}}}$).\n"
        f"3. The reading on the main ammeter measuring the total circuit current ($I_{{\\text{{total}}}}$).\n"
        f"4. The potential difference across the parallel combination ($V_p$).\n"
        f"5. The electric current passing through resistor $R_2$ ($I_2$)."
    )

    sample_answer = (
        f"1. Parallel Resistance:\n"
        f"   $$\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_2}} + \\frac{{1}}{{R_3}} = \\frac{{1}}{{{r2}}} + \\frac{{1}}{{{r3}}} "
        f"   = \\frac{{1}}{{{rp}}} \\implies R_p = {rp}\\ \\Omega$$\n\n"
        f"2. Total Circuit Resistance:\n"
        f"   $$R_{{\\text{{total}}}} = R_1 + R_p = {r1}\\ \\Omega + {rp}\\ \\Omega = {r_total}\\ \\Omega$$\n\n"
        f"3. Total Circuit Current:\n"
        f"   $$I_{{\\text{{total}}}} = \\frac{{V}}{{R_{{\\text{{total}}}}}} = \\frac{{{v_total}\\text{{ V}}}}{{{r_total}\\ \\Omega}} = {i_total}\\text{{ A}}$$\n\n"
        f"4. Potential Difference across Parallel Branch:\n"
        f"   $$V_p = I_{{\\text{{total}}}} \\times R_p = ({i_total}\\text{{ A}}) \\times ({rp}\\ \\Omega) = {vp}\\text{{ V}}$$\n"
        f"   (Alternatively: $V_p = V_{{\\text{{total}}}} - V_1 = {v_total}\\text{{ V}} - ({i_total} \\times {r1}) = {vp}\\text{{ V}}$)\n\n"
        f"5. Current through $R_2$:\n"
        f"   $$I_2 = \\frac{{V_p}}{{R_2}} = \\frac{{{vp}\\text{{ V}}}}{{{r2}\\ \\Omega}} = {fmt_sa(i2)}\\text{{ A}}$$"
    )

    ans_latex = (
        rf"R_p = {rp}\ \Omega, \quad R_{{\text{{total}}}} = {r_total}\ \Omega, \quad "
        rf"I_{{\text{{total}}}} = {i_total}\text{{ A}}, \quad V_p = {vp}\text{{ V}}, \quad I_2 = {fmt_sa(i2)}\text{{ A}}"
    )

    marking_schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Parallel resistance formula and calculation: Rp = " + f"{rp} ohm", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Total circuit resistance: R_total = " + f"{r_total} ohm", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Total current using Ohm's Law: I_total = " + f"{i_total} A", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Parallel potential difference: V_p = " + f"{vp} V", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Branch current through R2: I_2 = " + f"{fmt_sa(i2)} A", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_or_incorrect_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Break the circuit into two stages: first simplify the parallel branch (R2 and R3), then add the series resistor R1.",
        "concept": (
            "1. Parallel: $\\frac{1}{R_p} = \\frac{1}{R_2} + \\frac{1}{R_3}$.\n"
            "2. Series: $R_{\\text{total}} = R_1 + R_p$.\n"
            "3. Total current: $I = V / R_{\\text{total}}$.\n"
            "4. The potential difference across parallel branches is equal: $V_p = I_{\\text{total}} \\times R_p$."
        ),
        "breakdown": (
            f"1. $R_p = {rp}\\ \\Omega$\n"
            f"2. $R_{{\\text{{total}}}} = {r1} + {rp} = {r_total}\\ \\Omega$\n"
            f"3. $I_{{\\text{{total}}}} = {v_total}/{r_total} = {i_total}\\text{{ A}}$\n"
            f"4. $V_p = {i_total} \\times {rp} = {vp}\\text{{ V}}$\n"
            f"5. $I_2 = {vp}/{r2} = {fmt_sa(i2)}\\text{{ A}}$"
        ),
    }

    return make_science_question(
        prefix="ns_circ_compound",
        topic=TOPIC,
        subskill="circuit_analysis_compound",
        learning_objective_id=f"{LO}_compound_circuit",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=[
            "added_parallel_resistors_directly",
            "current_split_equally_unequal_resistors",
            "confused_series_and_parallel_potential_difference",
        ],
        keywords=["electric circuit", "parallel resistors", "series resistor", "Ohm's law", "potential difference", "current"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=12,
        mode="compound",
        difficulty="hard",
        marks=8,
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_circuit,
    "elementary_ohms_law": _build_ohms_law_drill,
    "elementary_series_resistance": _build_series_resistance_drill,
    "elementary_parallel_resistance": _build_parallel_resistance_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 8-9 Natural Sciences Electric Circuit questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_circuit)

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
