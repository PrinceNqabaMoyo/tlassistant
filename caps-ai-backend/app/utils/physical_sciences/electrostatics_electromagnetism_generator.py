"""Physical Sciences (Grades 10 & 11) — Electrostatics & Electromagnetism.
Strictly complies with the 6-Pillar Generator Contract:
- Term & Calendar metadata (Term 2)
- Procedural seeded PRNG determinism (random.Random(seed))
- Atomic elementary sub-drills (mode="compound" | "elementary_*")
- Standardized misconception taxonomy
- Teacher-editable marking schema with [M] and [A] marks
- Deterministic 3-tier pre-baked hints
- South African comma decimal convention (",")
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

K_COULOMB = 9.0e9  # N*m^2/C^2
E_CHARGE = 1.6e-19  # C


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    """Formats number using South African comma decimal separator."""
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_gr10_electrostatics(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 10: Principle of conservation of charge and quantization of charge."""
    # Two identical insulated spheres on stands with initial charges in nC
    q1 = r.choice([-8, -6, -4, -2, 2, 4, 6, 8, 10])
    q2 = r.choice([-6, -4, -2, 2, 4, 6, 8, 12])
    while q1 == q2 or (q1 + q2) % 2 != 0:
        q2 = r.choice([-6, -4, -2, 2, 4, 6, 8, 12])

    q_new = (q1 + q2) // 2
    delta_q_nc = abs(q_new - q1)
    delta_q_c = delta_q_nc * 1e-9
    num_electrons = int(round(delta_q_c / E_CHARGE))

    qid = _make_id("ps10_electrostatics", seed, idx)

    if mode == "elementary_charge_conservation":
        prompt = (
            f"Two identical conducting spheres, A and B, on insulated stands carry charges of "
            f"${_fmt_sa(q1)}\\text{{ nC}}$ and ${_fmt_sa(q2)}\\text{{ nC}}$ respectively. "
            f"The spheres are brought into contact and then separated.\n\n"
            f"Calculate the new charge $Q_{{\\text{{new}}}}$ on each sphere after contact."
        )
        ans_str = f"{_fmt_sa(q_new)} nC"
        memo = (
            f"1. Principle of conservation of charge: $Q_{{\\text{{new}}}} = \\frac{{Q_1 + Q_2}}{{2}}$ [M]\n"
            f"2. Substitution: $Q_{{\\text{{new}}}} = \\frac{{({q1}) + ({q2})}}{{2}} = {_fmt_sa(q_new)}\\text{{ nC}}$ [A]"
        )
        hints = {
            "tier_1": "Recall the formula for charge sharing when identical spheres touch.",
            "tier_2": "Use the Principle of Conservation of Charge: $Q_\\text{new} = (Q_1 + Q_2) / 2$.",
            "tier_3": f"Calculate: ({q1} + {q2}) / 2 = {q_new} nC.",
        }
        marks = 2
    else:
        # Full compound question: new charge + number of electrons transferred
        prompt = (
            f"Two identical conducting spheres, $P$ and $Q$, on insulated stands carry charges of "
            f"${_fmt_sa(q1)}\\text{{ nC}}$ and ${_fmt_sa(q2)}\\text{{ nC}}$ respectively.\n"
            f"The spheres are allowed to touch and are then returned to their original positions.\n\n"
            f"1. State the Principle of Conservation of Charge.\n"
            f"2. Calculate the charge on each sphere after separation.\n"
            f"3. Calculate the number of electrons transferred during contact."
        )
        ans_str = f"{_fmt_sa(q_new)} nC; {num_electrons:.2e} electrons"
        memo = (
            f"1. The net charge of an isolated system remains constant during any physical process. [2]\n"
            f"2. $Q_{{\\text{{new}}}} = \\frac{{Q_1 + Q_2}}{{2}} = \\frac{{{q1} + {q2}}}{{2}} = {_fmt_sa(q_new)}\\text{{ nC}}$ [2]\n"
            f"3. $n = \\frac{{\\Delta Q}}{{e}} = \\frac{{{_fmt_sa(delta_q_nc)} \\times 10^{{-9}}}}{{1{{,}}6 \\times 10^{{-19}}}} = {num_electrons:.2e}\\text{{ electrons}}$ [2]"
        )
        hints = {
            "tier_1": "Divide into two steps: find the final shared charge, then calculate the change in charge for one sphere.",
            "tier_2": "Quantization of charge formula: $n = \\frac{\\Delta Q}{e}$, where $e = 1{,}6 \\times 10^{-19}\\text{ C}$.",
            "tier_3": f"Shared charge is {_fmt_sa(q_new)} nC. Charge transferred is {_fmt_sa(delta_q_nc)} nC = {delta_q_nc}e-9 C. Then n = {num_electrons:.2e}.",
        }
        marks = 6

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["net_charge_inversion", "forgot_charge_quantization_constant", "forgot_nano_conversion"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of conservation or formula", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Calculated shared charge", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Number of electrons transferred", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "omitted_units", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr11_coulombs_law(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11: Coulomb's Law and Electric Field strength."""
    q1_micro = r.choice([2, 3, 4, 5, 6])
    q2_micro = r.choice([-8, -6, -5, -4, 3, 4, 6])
    r_cm = r.choice([2, 4, 5, 6, 8, 10, 12, 15])
    r_m = r_cm / 100.0

    # F = k * |q1 * q2| / r^2
    f_force = (K_COULOMB * (q1_micro * 1e-6) * (abs(q2_micro) * 1e-6)) / (r_m ** 2)
    force_nature = "attractive" if (q1_micro * q2_micro < 0) else "repulsive"

    # E at sphere 2 due to sphere 1
    e_field = (K_COULOMB * (q1_micro * 1e-6)) / (r_m ** 2)

    qid = _make_id("ps11_coulomb", seed, idx)

    if mode == "elementary_coulomb_force":
        prompt = (
            f"Two small point charges $q_1 = +{_fmt_sa(q1_micro)}\\ \\mu\\text{{C}}$ and "
            f"$q_2 = {_fmt_sa(q2_micro)}\\ \\mu\\text{{C}}$ are placed a distance of "
            f"${_fmt_sa(r_cm)}\\text{{ cm}}$ apart in a vacuum.\n\n"
            f"Calculate the magnitude of the electrostatic force exerted by $q_1$ on $q_2$."
        )
        ans_str = f"{_fmt_sa(round(f_force, 2))} N ({force_nature})"
        memo = (
            f"1. Formula: $F = \\frac{{k |q_1 q_2|}}{{r^2}}$ [M]\n"
            f"2. Convert $r$: ${_fmt_sa(r_cm)}\\text{{ cm}} = {_fmt_sa(r_m)}\\text{{ m}}$ [M]\n"
            f"3. Substitution: $F = \\frac{{(9 \\times 10^9)({q1_micro} \\times 10^{{-6}})({abs(q2_micro)} \\times 10^{{-6}})}}{{({_fmt_sa(r_m)})^2}}$ [M]\n"
            f"4. Force: $F = {_fmt_sa(round(f_force, 2))}\\text{{ N}}$ ({force_nature}) [A]"
        )
        hints = {
            "tier_1": "Apply Coulomb's Law: $F = \\frac{k Q_1 Q_2}{r^2}$. Remember to convert cm to m and $\\mu\\text{C}$ to C.",
            "tier_2": "Convert $r = " + f"{r_cm}\\text{{ cm}} = {r_m}\\text{{ m}}$ and charges by multiplying by $10^{{-6}}$.",
            "tier_3": f"Calculate: (9e9 * {q1_micro}e-6 * {abs(q2_micro)}e-6) / ({r_m}^2) = {_fmt_sa(round(f_force, 2))} N.",
        }
        marks = 4
    else:
        # Full compound: Coulomb force + Electric field
        prompt = (
            f"Two point charges, $A = +{_fmt_sa(q1_micro)}\\ \\mu\\text{{C}}$ and "
            f"$B = {_fmt_sa(q2_micro)}\\ \\mu\\text{{C}}$, are separated by a distance of "
            f"${_fmt_sa(r_cm)}\\text{{ cm}}$ in free space.\n\n"
            f"1. State Coulomb's Law in words.\n"
            f"2. Calculate the electrostatic force that charge $A$ exerts on charge $B$, and state whether it is attractive or repulsive.\n"
            f"3. Calculate the electric field strength at the position of charge $B$ due to charge $A$ alone."
        )
        ans_str = f"{_fmt_sa(round(f_force, 2))} N ({force_nature}); E = {_fmt_sa(round(e_field, 1))} N/C"
        memo = (
            f"1. Coulomb's Law: The magnitude of the electrostatic force between two point charges is directly proportional "
            f"to the product of the magnitudes of the charges and inversely proportional to the square of the distance between them. [2]\n"
            f"2. $F = \\frac{{k q_1 q_2}}{{r^2}} = \\frac{{(9 \\times 10^9)({q1_micro} \\times 10^{{-6}})({abs(q2_micro)} \\times 10^{{-6}})}}{{({_fmt_sa(r_m)})^2}} = {_fmt_sa(round(f_force, 2))}\\text{{ N}}$ ({force_nature}) [4]\n"
            f"3. $E = \\frac{{k Q}}{{r^2}} = \\frac{{(9 \\times 10^9)({q1_micro} \\times 10^{{-6}})}}{{({_fmt_sa(r_m)})^2}} = {_fmt_sa(round(e_field, 1))}\\text{{ N/C}}$ (away from $A$) [3]"
        )
        hints = {
            "tier_1": "State Coulomb's Law, then use $F = k q_1 q_2 / r^2$ and $E = k Q / r^2$.",
            "tier_2": "Opposite signs attract; like signs repel. Convert $\\mu\\text{C} \\to 10^{-6}\\text{ C}$ and $\\text{cm} \\to \\text{m}$.",
            "tier_3": f"F = {_fmt_sa(round(f_force, 2))} N ({force_nature}). E = {_fmt_sa(round(e_field, 1))} N/C away from A.",
        }
        marks = 9

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["inverse_square_omitted", "forgot_micro_conversion", "coulomb_constant_miscalculated"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Coulomb's Law statement", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Electrostatic force calculation and direction", "marks": 4, "editable": True},
                {"id": "mp_3", "desc": "Electric field strength calculation", "marks": 3, "editable": True},
            ],
            "deductions": [{"rule": "omitted_units", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr11_electromagnetism(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11: Magnetic Flux and Faraday's Law of Electromagnetic Induction."""
    n_turns = r.choice([50, 100, 150, 200, 250, 500])
    area_cm2 = r.choice([10, 20, 25, 40, 50, 100])
    area_m2 = area_cm2 * 1e-4

    b1 = round(r.uniform(0.1, 0.4), 2)
    b2 = round(b1 + r.uniform(0.2, 0.8), 2)
    delta_t = round(r.uniform(0.02, 0.10), 2)

    delta_b = b2 - b1
    delta_phi = delta_b * area_m2
    induced_emf = n_turns * (delta_phi / delta_t)

    qid = _make_id("ps11_electromagnetism", seed, idx)

    prompt = (
        f"A coil consisting of ${n_turns}$ turns of insulated copper wire has an effective cross-sectional "
        f"area of ${area_cm2}\\text{{ cm}}^2$.\n"
        f"The coil is placed perpendicular to a uniform magnetic field.\n"
        f"The magnetic field strength increases uniformly from ${_fmt_sa(b1)}\\text{{ T}}$ to "
        f"${_fmt_sa(b2)}\\text{{ T}}$ in a time interval of ${_fmt_sa(delta_t)}\\text{{ s}}$.\n\n"
        f"1. State Faraday's Law of electromagnetic induction in words.\n"
        f"2. Calculate the change in magnetic flux ($\\Delta \\Phi$) through the coil.\n"
        f"3. Calculate the magnitude of the induced emf ($\\mathcal{{E}}$) across the coil."
    )
    ans_str = f"Delta Phi = {delta_phi:.2e} Wb; emf = {_fmt_sa(round(induced_emf, 2))} V"
    memo = (
        f"1. Faraday's Law: The magnitude of the induced emf across a conductor is directly proportional "
        f"to the rate of change of magnetic flux linkage. [2]\n"
        f"2. $\\Delta \\Phi = \\Delta B \\cdot A = ({_fmt_sa(b2)} - {_fmt_sa(b1)}) \\times ({area_cm2} \\times 10^{{-4}}) = {delta_phi:.2e}\\text{{ Wb}}$ [2]\n"
        f"3. $\\mathcal{{E}} = -N \\frac{{\\Delta \\Phi}}{{\\Delta t}} = -({n_turns}) \\frac{{{delta_phi:.2e}}}{{{_fmt_sa(delta_t)}}} = {_fmt_sa(round(induced_emf, 2))}\\text{{ V}}$ [3]"
    )
    hints = {
        "tier_1": "Convert area from cm^2 to m^2 (multiply by 10^-4), then find change in magnetic flux: Delta Phi = Delta B * A.",
        "tier_2": "Apply Faraday's Law formula: emf = -N * (Delta Phi / Delta t).",
        "tier_3": f"Delta Phi = {delta_phi:.2e} Wb. Induced emf = {_fmt_sa(round(induced_emf, 2))} V.",
    }
    marks = 7

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["forgot_area_conversion_cm2_m2", "faradays_law_sign_confusion", "rate_of_change_inverted"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Faraday's Law definition", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Change in magnetic flux calculation", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Induced emf magnitude calculation", "marks": 3, "editable": True},
            ],
            "deductions": [{"rule": "omitted_units", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Physical Sciences Electrostatics & Electromagnetism."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill == "electrostatics_gr10" or mode == "elementary_charge_conservation":
            q = _generate_gr10_electrostatics(sub_r, sub_seed, i, mode)
        elif subskill == "coulomb_law" or mode == "elementary_coulomb_force":
            q = _generate_gr11_coulombs_law(sub_r, sub_seed, i, mode)
        elif subskill == "electromagnetism" or mode == "elementary_faradays_law":
            q = _generate_gr11_electromagnetism(sub_r, sub_seed, i, mode)
        else:
            archetype = sub_r.choice(["gr10", "coulomb", "magnetism"])
            if archetype == "gr10":
                q = _generate_gr10_electrostatics(sub_r, sub_seed, i, mode)
            elif archetype == "coulomb":
                q = _generate_gr11_coulombs_law(sub_r, sub_seed, i, mode)
            else:
                q = _generate_gr11_electromagnetism(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
