"""Grade 10 Physical Sciences — Electric Circuits & Electrostatics Generator.
Deterministic 6-pillar CAPS question generator covering Paper 1 (Physics Term 2):
- Charge quantisation: Q = n * e (e = 1.6 x 10^-19 C).
- Principle of conservation of charge: Q_new = (Q1 + Q2) / 2 upon contact and separation.
- Electric current: I = Q / Delta t (in Amperes, C/s).
- Potential difference and emf: V = W / Q (in Volts, J/C).
- Resistance & Ohm's law: R = V / I.
- Series and parallel resistor combinations: Rs = R1 + R2; 1/Rp = 1/R1 + 1/R2.
- Instrument connection: ammeters in series, voltmeters in parallel.

Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{{,}}")


E_CHARGE = 1.6e-19


def _build_charge_drill(r: random.Random) -> Dict[str, Any]:
    # Two identical metal spheres on insulated stands
    q1_nc = r.choice([-8, -6, -4, -2, 2, 4, 6, 8, 10])
    q2_nc = r.choice([-6, -4, -2, 2, 4, 6, 12])
    while q1_nc == q2_nc:
        q2_nc = r.choice([-6, -4, -2, 2, 4, 6, 12])

    q_new_nc = (q1_nc + q2_nc) / 2
    delta_q_nc = abs(q_new_nc - q1_nc)
    delta_q_c = delta_q_nc * 1e-9
    num_electrons = int(round(delta_q_c / E_CHARGE))

    from_sphere = "A to B" if q1_nc < q2_nc else "B to A"

    prompt = (
        f"Two identical conducting spheres, **A** and **B**, on insulated stands carry charges of "
        f"**${q1_nc}\\text{{ nC}}$** and **${q2_nc}\\text{{ nC}}$** respectively.\n"
        f"The spheres are brought into contact and then separated back to their original positions.\n\n"
        f"1. State the **Principle of Conservation of Charge**.\n"
        f"2. Calculate the new charge ($Q_{{\\text{{new}}}}$) on each sphere after separation.\n"
        f"3. Calculate the number of electrons transferred between the spheres during contact.\n"
        f"4. State the direction of electron transfer (from sphere A to B or from sphere B to A)."
    )

    sol = (
        f"1. **Principle of Conservation of Charge:** The net charge of an isolated system remains constant during any physical process.\n\n"
        f"2. $Q_{{\\text{{new}}}} = \\frac{{Q_1 + Q_2}}{{2}} = \\frac{{{q1_nc} + ({q2_nc})}}{{2}} = {_fmt_sa(q_new_nc)}\\text{{ nC}}$\n\n"
        f"3. $\\Delta Q = |Q_{{\\text{{new}}}} - Q_1| = |{_fmt_sa(q_new_nc)} - ({q1_nc})| = {_fmt_sa(delta_q_nc)}\\text{{ nC}} = {_fmt_sa(delta_q_nc)} \\times 10^{{-9}}\\text{{ C}}$\n"
        f"   $n = \\frac{{\\Delta Q}}{{e}} = \\frac{{{_fmt_sa(delta_q_nc)} \\times 10^{{-9}}}}{{1{{,}}6 \\times 10^{{-19}}}} = {num_electrons:.2e}\\text{{ electrons}}$\n\n"
        f"4. Electrons move from the sphere with more negative (or less positive) potential: **from sphere {from_sphere}**."
    )

    return {
        "id": f"g10_ps_circ_charge_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Qnew={_fmt_sa(q_new_nc)} nC, n={num_electrons:.2e}",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Statement of Conservation of Charge", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula: Qnew = (Q1 + Q2)/2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate Qnew = {_fmt_sa(q_new_nc)} nC", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculate electrons transferred = {num_electrons:.2e}", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"State direction of electron transfer: {from_sphere}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "forgot_elementary_charge_constant", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "$Q_{\\text{new}} = \\frac{Q_1 + Q_2}{2}$ and $n = \\frac{\\Delta Q}{e}$ where $e = 1{{,}}6 \\times 10^{-19}\\text{ C}$.",
            "tier_2": "Remember $1\\text{ nC} = 10^{-9}\\text{ C}$. Only negative electrons move between conductors.",
            "tier_3": f"$Q_{{\\text{{new}}}} = {_fmt_sa(q_new_nc)}\\text{{ nC}}$. Electrons transferred: $n = {num_electrons:.2e}$.",
        },
        "misconception_tags": ["forgot_elementary_charge_constant", "proton_transfer_fallacy"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


def _build_circuit_drill(r: random.Random) -> Dict[str, Any]:
    r1 = r.choice([2, 3, 4, 6])
    r2 = r.choice([2, 4, 6])
    rs = r1 + r2
    current = r.choice([1.0, 1.5, 2.0, 2.5])
    v_batt = round(current * rs, 1)
    v1 = round(current * r1, 1)
    v2 = round(current * r2, 1)
    time_s = r.choice([30, 60, 120])
    q_tot = round(current * time_s, 1)
    w_tot = round(v_batt * q_tot, 1)

    prompt = (
        f"A simple series circuit contains a battery of potential difference **${_fmt_sa(v_batt)}\\text{{ V}}$**, "
        f"two resistors **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$** connected in series, "
        f"an ammeter, and a closed switch.\n\n"
        f"1. Calculate the total equivalent resistance ($R_s$) of the circuit.\n"
        f"2. Calculate the reading on the ammeter ($I$).\n"
        f"3. Calculate the potential difference ($V_1$) across resistor $R_1$.\n"
        f"4. Calculate the total charge ($Q$) passing through the battery in **{time_s} seconds**.\n"
        f"5. Calculate the total work done (energy supplied) by the battery in this time."
    )

    sol = (
        f"1. $R_s = R_1 + R_2 = {r1} + {r2} = {rs}\\ \\Omega$\n\n"
        f"2. $I = \\frac{{V}}{{R_s}} = \\frac{{{_fmt_sa(v_batt)}}}{{{rs}}} = {_fmt_sa(current)}\\text{{ A}}$\n\n"
        f"3. $V_1 = I \\times R_1 = {_fmt_sa(current)} \\times {r1} = {_fmt_sa(v1)}\\text{{ V}}$\n\n"
        f"4. $Q = I \\times \\Delta t = {_fmt_sa(current)} \\times {time_s} = {_fmt_sa(q_tot)}\\text{{ C}}$\n\n"
        f"5. $W = V \\times Q = {_fmt_sa(v_batt)} \\times {_fmt_sa(q_tot)} = {_fmt_sa(w_tot)}\\text{{ J}}$"
    )

    return {
        "id": f"g10_ps_circ_ohm_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Rs={rs} Ohm, I={_fmt_sa(current)} A, V1={_fmt_sa(v1)} V, Q={_fmt_sa(q_tot)} C, W={_fmt_sa(w_tot)} J",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculate Rs = {rs} Ohm", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula: I = V / R", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate I = {_fmt_sa(current)} A", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculate V1 = {_fmt_sa(v1)} V", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculate Q = {_fmt_sa(q_tot)} C", "marks": 1, "editable": True},
                {"id": "mp6", "desc": f"Calculate W = {_fmt_sa(w_tot)} J", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "confused_current_and_potential_difference", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "$R_s = R_1 + R_2$, $I = \\frac{V}{R_s}$, and $Q = I \\Delta t$.",
            "tier_2": "Work done by the battery is $W = V Q$. In a series circuit, current is the same everywhere.",
            "tier_3": f"$R_s = {rs}\\ \\Omega$, $I = {_fmt_sa(current)}\\text{{ A}}$, $V_1 = {_fmt_sa(v1)}\\text{{ V}}$, $Q = {_fmt_sa(q_tot)}\\text{{ C}}$, $W = {_fmt_sa(w_tot)}\\text{{ J}}$.",
        },
        "misconception_tags": ["confused_current_and_potential_difference"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)
    if mode == "elementary_charge":
        return _build_charge_drill(r)
    elif mode == "elementary_circuit":
        return _build_circuit_drill(r)
    else:
        choice = r.choice(["charge", "circuit"])
        if choice == "charge":
            return _build_charge_drill(r)
        else:
            return _build_circuit_drill(r)
