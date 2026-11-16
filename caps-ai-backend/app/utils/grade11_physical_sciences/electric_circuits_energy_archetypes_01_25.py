"""Grade 11 Physical Sciences — Term 3: Electric Circuits (Archetypes 01–25).
Deterministic 6-pillar generators grounded in South African National Curriculum Standards:
- Subskills 01–12: Potential difference (V = W/Q), electric current (I = Q/dt), electron quantization,
  ammeter & voltmeter placement, Ohm's Law, ohmic vs non-ohmic conductors, I-V and V-I graph gradient
  analysis, experimental verification of Ohm's Law, EMF vs terminal potential difference, and internal
  resistance (E = I(R + r)).
- Subskills 13–25: Series resistor networks, voltage dividers, parallel resistor networks (2, 3, and 4
  resistors), current dividers, finding unknown resistors, identical resistor combinations, composite
  series-parallel networks, working backwards from branch readings, switch toggling, and short-circuit
  bypass analysis.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional


TOPIC_NAME = "Electric circuits"


def rng(seed: Optional[Any] = None) -> random.Random:
    if isinstance(seed, random.Random):
        return seed
    return random.Random(seed)


def fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and round(val, places).is_integer()):
        return str(int(round(val, places)))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def make_payload(
    subskill_id: str,
    seed: Optional[int],
    prompt: str,
    answer_latex: str,
    sample_answer: str,
    marking_points: List[tuple[str, int]],
    tier_hints: List[str],
    misconception_tags: List[str],
    keywords: List[str],
    difficulty: str = "medium",
    diagram_spec: Optional[Dict[str, Any]] = None,
    sub_parts: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    total_marks = sum(m for _, m in marking_points)
    mp_list = [
        {"id": f"mp_{i + 1}", "desc": desc, "marks": m, "editable": True}
        for i, (desc, m) in enumerate(marking_points)
    ]
    hints_dict = {
        "tier_1": tier_hints[0] if len(tier_hints) > 0 else "Identify the relevant circuit formula.",
        "tier_2": tier_hints[1] if len(tier_hints) > 1 else "Substitute known quantities in SI units.",
        "tier_3": tier_hints[2] if len(tier_hints) > 2 else sample_answer,
    }
    res: Dict[str, Any] = {
        "id": f"ps11_elec_{subskill_id}_{seed if seed is not None else 0}",
        "question_id": f"ps11_elec_{subskill_id}_{seed if seed is not None else 0}",
        "topic": TOPIC_NAME,
        "subskill": subskill_id,
        "learning_objective_id": f"PS11.T3.ELEC.{subskill_id}",
        "type": "compound",
        "modality": "circuit",
        "prompt": prompt,
        "prompt_latex": prompt,
        "question": prompt,
        "question_text": prompt,
        "answer_latex": answer_latex,
        "expected_answer": answer_latex,
        "correct_answer": answer_latex,
        "sample_answer": sample_answer,
        "ideal_answer": sample_answer,
        "worked_solution": sample_answer,
        "explanation": sample_answer,
        "marking_schema": {
            "total_marks": total_marks,
            "marking_points": mp_list,
            "deductions": [
                {"rule": tag, "penalty": -1} for tag in misconception_tags[:2]
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints_dict,
        "misconception_tags": misconception_tags,
        "keywords": keywords,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, total_marks),
        "mode": f"elementary_{subskill_id}",
        "difficulty": difficulty,
        "marks": total_marks,
        "seed": seed,
    }
    if diagram_spec is not None:
        res["diagram_spec"] = diagram_spec
    if sub_parts is not None:
        res["sub_parts"] = sub_parts
    return res


def _svg_iv_graph(r_ohm: int, v_max: int) -> str:
    i_max = round(v_max / r_ohm, 2)
    i_mid = round(i_max / 2, 2)
    v_mid = round(v_max / 2, 1)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 280">'
        f'<rect width="420" height="280" fill="#ffffff"/>'
        f'<text x="210" y="24" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e293b">'
        f'Current (I) vs Potential Difference (V) for Conductor X</text>'
        f'<line x1="65" y1="230" x2="375" y2="230" stroke="#334155" stroke-width="2"/>'
        f'<line x1="65" y1="230" x2="65" y2="40" stroke="#334155" stroke-width="2"/>'
        f'<line x1="210" y1="230" x2="210" y2="140" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>'
        f'<line x1="65" y1="140" x2="210" y2="140" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>'
        f'<line x1="355" y1="230" x2="355" y2="50" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>'
        f'<line x1="65" y1="50" x2="355" y2="50" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>'
        f'<line x1="65" y1="230" x2="355" y2="50" stroke="#2563eb" stroke-width="3"/>'
        f'<circle cx="210" cy="140" r="4" fill="#1d4ed8"/>'
        f'<circle cx="355" cy="50" r="4" fill="#1d4ed8"/>'
        f'<text x="60" y="246" text-anchor="end" font-family="sans-serif" font-size="11" fill="#334155">0</text>'
        f'<text x="210" y="248" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#334155">{v_mid}</text>'
        f'<text x="355" y="248" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#334155">{v_max}</text>'
        f'<text x="220" y="270" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">Potential Difference V (V)</text>'
        f'<text x="55" y="144" text-anchor="end" font-family="sans-serif" font-size="11" fill="#334155">{i_mid}</text>'
        f'<text x="55" y="54" text-anchor="end" font-family="sans-serif" font-size="11" fill="#334155">{i_max}</text>'
        f'<text x="18" y="135" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b" transform="rotate(-90 18 135)">Current I (A)</text>'
        f'</svg>'
    )


def _svg_two_resistors_vi(ra: int, rb: int, i_max: int) -> str:
    va_max = ra * i_max
    vb_max = rb * i_max
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 280">'
        f'<rect width="420" height="280" fill="#ffffff"/>'
        f'<text x="215" y="24" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e293b">'
        f'Potential Difference (V) vs Current (I) for Conductors P and Q</text>'
        f'<line x1="65" y1="230" x2="375" y2="230" stroke="#334155" stroke-width="2"/>'
        f'<line x1="65" y1="230" x2="65" y2="40" stroke="#334155" stroke-width="2"/>'
        f'<line x1="65" y1="230" x2="330" y2="55" stroke="#dc2626" stroke-width="3"/>'
        f'<line x1="65" y1="230" x2="330" y2="135" stroke="#16a34a" stroke-width="3"/>'
        f'<text x="340" y="58" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">P ({va_max} V at {i_max} A)</text>'
        f'<text x="340" y="138" font-family="sans-serif" font-size="12" font-weight="bold" fill="#16a34a">Q ({vb_max} V at {i_max} A)</text>'
        f'<text x="330" y="248" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#334155">{i_max}</text>'
        f'<text x="220" y="270" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">Current I (A)</text>'
        f'<text x="55" y="58" text-anchor="end" font-family="sans-serif" font-size="11" fill="#334155">{va_max}</text>'
        f'<text x="55" y="138" text-anchor="end" font-family="sans-serif" font-size="11" fill="#334155">{vb_max}</text>'
        f'<text x="18" y="135" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b" transform="rotate(-90 18 135)">Potential Difference V (V)</text>'
        f'</svg>'
    )


def _svg_series_circuit(v_tot: float, r1: int, r2: int, r3: int) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 240">'
        f'<rect width="460" height="240" fill="#ffffff"/>'
        f'<line x1="60" y1="50" x2="200" y2="50" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="200" y1="35" x2="200" y2="65" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="212" y1="42" x2="212" y2="58" stroke="#1e293b" stroke-width="4"/>'
        f'<text x="206" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{v_tot} V</text>'
        f'<line x1="212" y1="50" x2="400" y2="50" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="60" y1="50" x2="60" y2="180" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="400" y1="50" x2="400" y2="180" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="60" y1="180" x2="110" y2="180" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="110" y="166" width="60" height="28" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="140" y="184" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a">R1={r1} Ω</text>'
        f'<line x1="170" y1="180" x2="200" y2="180" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="200" y="166" width="60" height="28" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="230" y="184" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a">R2={r2} Ω</text>'
        f'<line x1="260" y1="180" x2="290" y2="180" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="290" y="166" width="60" height="28" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="320" y="184" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a">R3={r3} Ω</text>'
        f'<line x1="350" y1="180" x2="400" y2="180" stroke="#1e293b" stroke-width="2"/>'
        f'</svg>'
    )


def _svg_parallel_circuit(v_tot: float, r1: int, r2: int) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 260">'
        f'<rect width="440" height="260" fill="#ffffff"/>'
        f'<line x1="70" y1="45" x2="200" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="200" y1="30" x2="200" y2="60" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="212" y1="37" x2="212" y2="53" stroke="#1e293b" stroke-width="4"/>'
        f'<text x="206" y="22" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{v_tot} V</text>'
        f'<line x1="212" y1="45" x2="370" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="70" y1="45" x2="70" y2="170" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="370" y1="45" x2="370" y2="170" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="130" y1="120" x2="130" y2="215" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="310" y1="120" x2="310" y2="215" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="70" y1="170" x2="130" y2="170" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="310" y1="170" x2="370" y2="170" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="130" y1="120" x2="180" y2="120" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="180" y="106" width="80" height="28" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="220" y="124" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#92400e">R1 = {r1} Ω</text>'
        f'<line x1="260" y1="120" x2="310" y2="120" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="130" y1="215" x2="180" y2="215" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="180" y="201" width="80" height="28" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="220" y="219" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#92400e">R2 = {r2} Ω</text>'
        f'<line x1="260" y1="215" x2="310" y2="215" stroke="#1e293b" stroke-width="2"/>'
        f'</svg>'
    )


def _svg_composite_circuit(v_tot: float, rs: int, r1: int, r2: int) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 260">'
        f'<rect width="480" height="260" fill="#ffffff"/>'
        f'<line x1="50" y1="45" x2="210" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="210" y1="30" x2="210" y2="60" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="222" y1="37" x2="222" y2="53" stroke="#1e293b" stroke-width="4"/>'
        f'<text x="216" y="22" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{v_tot} V</text>'
        f'<line x1="222" y1="45" x2="430" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="50" y1="45" x2="50" y2="170" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="430" y1="45" x2="430" y2="170" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="50" y1="170" x2="90" y2="170" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="90" y="156" width="75" height="28" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="127" y="174" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#166534">Rs = {rs} Ω</text>'
        f'<line x1="165" y1="170" x2="215" y2="170" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="215" y1="120" x2="215" y2="220" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="385" y1="120" x2="385" y2="220" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="385" y1="170" x2="430" y2="170" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="215" y1="120" x2="260" y2="120" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="260" y="106" width="80" height="28" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="300" y="124" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a">R1 = {r1} Ω</text>'
        f'<line x1="340" y1="120" x2="385" y2="120" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="215" y1="220" x2="260" y2="220" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="260" y="206" width="80" height="28" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="300" y="224" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a">R2 = {r2} Ω</text>'
        f'<line x1="340" y1="220" x2="385" y2="220" stroke="#1e293b" stroke-width="2"/>'
        f'</svg>'
    )


# ---------------------------------------------------------------------------
# Subskill 01: Potential difference work per unit charge (V = W / Q)
# ---------------------------------------------------------------------------
def arch_01_potential_difference_work_per_charge(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    v_val = r.choice([6, 9, 12, 15, 18, 24])
    q_val = r.choice([4, 5, 8, 12, 15, 20, 25])
    w_val = v_val * q_val
    comp = r.choice(["a light bulb", "a heating element", "a fixed resistor", "an electric motor"])

    prompt = (
        f"A charge of **${q_val}\\text{{ C}}$** passes through {comp} in a closed circuit, "
        f"transferring **${w_val}\\text{{ J}}$** of electrical energy into other forms of energy.\n\n"
        f"1. Define the term **potential difference**.\n"
        f"2. Calculate the potential difference ($V$) across {comp}.\n"
        f"3. Calculate how much electrical work is done when **${q_val * 3}\\text{{ C}}$** of charge passes through the same component."
    )

    w_new = v_val * (q_val * 3)
    ans_latex = rf"V = {v_val}\text{{ V}}; \quad W = {w_new}\text{{ J}}"
    sample_answer = (
        f"1. **Definition:** Potential difference across the ends of a conductor is the work done (or energy transferred) "
        f"per unit positive charge moving between the two points ($V = \\frac{{W}}{{Q}}$).\n\n"
        f"2. $$V = \\frac{{W}}{{Q}} = \\frac{{{w_val}}}{{{q_val}}} = {v_val}\\text{{ V}}$$\n\n"
        f"3. $$W = V \\cdot Q = {v_val} \\times {q_val * 3} = {w_new}\\text{{ J}}$$"
    )

    return make_payload(
        "01_potential_difference_work_per_charge",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Correct definition of potential difference (work done per unit charge)", 2),
            (f"Formula V = W / Q and substitution {w_val} / {q_val}", 1),
            (f"Correct potential difference V = {v_val} V", 1),
            (f"Correct work W = {w_new} J", 1),
        ],
        [
            "Potential difference is defined by the formula $V = \\frac{W}{Q}$, where $W$ is in joules and $Q$ is in coulombs.",
            f"Divide $W = {w_val}\\text{{ J}}$ by $Q = {q_val}\\text{{ C}}$ to obtain $V$.",
            f"$V = {v_val}\\text{{ V}}$ and $W = {v_val} \\times {q_val * 3} = {w_new}\\text{{ J}}$.",
        ],
        ["multiplying_work_and_charge_for_voltage", "unit_confusion_joules_vs_volts"],
        ["potential difference", "volt", "work", "charge"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 02: Electric current rate of charge flow (I = Q / dt)
# ---------------------------------------------------------------------------
def arch_02_electric_current_rate_of_charge_flow(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    i_val = r.choice([0.5, 1.2, 1.5, 2.0, 2.5, 3.2, 4.0])
    t_mins = r.choice([2, 3, 4, 5, 6])
    t_secs = t_mins * 60
    q_val = round(i_val * t_secs, 1)

    prompt = (
        f"A steady electric current of **${fmt_sa(i_val)}\\text{{ A}}$** flows through a conductor for **${t_mins}\\text{{ minutes}}$**.\n\n"
        f"1. Define **electric current**.\n"
        f"2. Convert the time interval into SI units (seconds).\n"
        f"3. Calculate the total quantity of electric charge ($Q$) that passes a fixed cross-section of the conductor during this time.\n"
        f"4. State the direction of conventional current relative to the terminals of a battery."
    )

    ans_latex = rf"\Delta t = {t_secs}\text{{ s}}; \quad Q = {fmt_sa(q_val)}\text{{ C}}"
    sample_answer = (
        f"1. **Definition:** Electric current is the rate of flow of electric charge past a fixed point in a circuit ($I = \\frac{{Q}}{{\\Delta t}}$).\n\n"
        f"2. $$\\Delta t = {t_mins} \\times 60 = {t_secs}\\text{{ s}}$$\n\n"
        f"3. $$Q = I \\cdot \\Delta t = {fmt_sa(i_val)} \\times {t_secs} = {fmt_sa(q_val)}\\text{{ C}}$$\n\n"
        f"4. Conventional current is directed from the **positive terminal** of the battery, through the external circuit, to the **negative terminal**."
    )

    return make_payload(
        "02_electric_current_rate_of_charge_flow",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Correct definition of electric current (rate of flow of charge)", 2),
            (f"Convert {t_mins} min to {t_secs} s", 1),
            (f"Calculate Q = {fmt_sa(q_val)} C using Q = I * dt", 2),
            ("Conventional current flows from positive to negative terminal", 1),
        ],
        [
            "Remember to convert time from minutes to seconds ($\\times 60$) before using $Q = I \\Delta t$.",
            f"Multiply $I = {fmt_sa(i_val)}\\text{{ A}}$ by $\\Delta t = {t_secs}\\text{{ s}}$.",
            f"$Q = {fmt_sa(q_val)}\\text{{ C}}$; conventional current flows from positive to negative.",
        ],
        ["forgetting_minutes_to_seconds_conversion", "reversing_conventional_current_direction"],
        ["electric current", "ampere", "coulomb", "conventional current"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 03: Electron quantization and current (n = I * dt / e)
# ---------------------------------------------------------------------------
def arch_03_electron_quantization_and_current(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    i_val = r.choice([0.32, 0.48, 0.64, 0.80, 1.60, 2.40, 3.20])
    dt_val = r.choice([2, 4, 5, 8, 10, 20])
    q_val = round(i_val * dt_val, 2)
    # n = q_val / 1.6e-19
    coeff = round(q_val / 1.6, 3)

    prompt = (
        f"A current of **${fmt_sa(i_val)}\\text{{ A}}$** flows through a metallic wire for **${dt_val}\\text{{ s}}$**.\n"
        f"(Take the magnitude of the charge on an electron as $e = 1{{,}}6 \\times 10^{{-19}}\\text{{ C}}$.)\n\n"
        f"1. Calculate the total charge ($Q$) that moves past a point in the wire in ${dt_val}\\text{{ s}}$.\n"
        f"2. Calculate the number of electrons ($n$) that pass this point during the ${dt_val}\\text{{ s}}$ interval.\n"
        f"3. Compare the direction of electron drift with the direction of conventional current."
    )

    ans_latex = rf"Q = {fmt_sa(q_val)}\text{{ C}}; \quad n = {fmt_sa(coeff, 3)} \times 10^{{19}}\text{{ electrons}}"
    sample_answer = (
        f"1. $$Q = I \\Delta t = {fmt_sa(i_val)} \\times {dt_val} = {fmt_sa(q_val)}\\text{{ C}}$$\n\n"
        f"2. $$n = \\frac{{Q}}{{e}} = \\frac{{{fmt_sa(q_val)}}}{{1{{,}}6 \\times 10^{{-19}}}} = {fmt_sa(coeff, 3)} \\times 10^{{19}}\\text{{ electrons}}$$\n\n"
        f"3. Electrons are negatively charged and drift from the **negative terminal to the positive terminal**, "
        f"which is opposite to the direction of conventional current."
    )

    return make_payload(
        "03_electron_quantization_and_current",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate total charge Q = {fmt_sa(q_val)} C", 2),
            ("Formula n = Q / e and substitution", 1),
            (f"Calculate n = {fmt_sa(coeff, 3)} x 10^19 electrons", 1),
            ("State electron drift is opposite to conventional current (negative to positive)", 1),
        ],
        [
            "First find the total charge $Q = I \\Delta t$, then apply charge quantization $Q = n \\cdot e$.",
            f"Divide $Q = {fmt_sa(q_val)}\\text{{ C}}$ by $1{{,}}6 \\times 10^{{-19}}\\text{{ C}}$.",
            f"$n = {fmt_sa(coeff, 3)} \\times 10^{{19}}\\text{{ electrons}}$.",
        ],
        ["multiplying_by_electron_charge_instead_of_dividing", "confusing_electron_flow_with_conventional_current"],
        ["quantization", "electron", "charge", "current"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 04: Voltmeter and ammeter connections
# ---------------------------------------------------------------------------
def arch_04_voltmeter_and_ammeter_connections(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    scenario = r.choice([
        {
            "error": "connects an ammeter in parallel across a resistor and a voltmeter in series with the battery",
            "obs": "The circuit current drops to nearly zero across the load, while the ammeter branch draws a dangerously high current.",
            "r_v": "very high (ideally infinite)",
            "r_a": "very low (ideally zero)",
        },
        {
            "error": "connects a voltmeter in series in the main branch of a simple circuit containing a bulb",
            "obs": "The bulb fails to glow and the ammeter reads almost $0\\text{ A}$, while the voltmeter reads the full emf of the battery.",
            "r_v": "extremely high",
            "r_a": "extremely low",
        },
        {
            "error": "connects a low-resistance ammeter directly in parallel across a $12\\text{ V}$ battery",
            "obs": "A short circuit occurs through the ammeter, blowing the protective fuse inside the meter.",
            "r_v": "very high",
            "r_a": "very low",
        },
    ])

    prompt = (
        f"During a practical investigation, a learner mistakenly {scenario['error']}.\n"
        f"Observation: *{scenario['obs']}*\n\n"
        f"1. State how an **ammeter** and a **voltmeter** must be connected in a circuit.\n"
        f"2. Compare the internal resistance of an ideal ammeter with that of an ideal voltmeter.\n"
        f"3. Explain why the learner observed the behaviour described above.\n"
        f"4. When using a multi-scale meter to measure an unknown current, which scale should be selected first? Give a reason."
    )

    ans_latex = r"\text{Ammeter in series (low } R\text{); Voltmeter in parallel (high } R\text{); start on largest scale}"
    sample_answer = (
        f"1. An **ammeter** must be connected in **series** with the component; a **voltmeter** must be connected in **parallel** across the component.\n\n"
        f"2. An ideal ammeter has **{scenario['r_a']}** internal resistance so it does not reduce circuit current. "
        f"An ideal voltmeter has **{scenario['r_v']}** internal resistance so it draws negligible current from the circuit.\n\n"
        f"3. Because a voltmeter has very high resistance, placing it in series blocks almost all current flow. "
        f"Because an ammeter has very low resistance, placing it in parallel creates a short circuit.\n\n"
        f"4. Always start on the **largest scale** first to prevent damaging or burning out the meter if the current or voltage exceeds a smaller scale limit."
    )

    return make_payload(
        "04_voltmeter_and_ammeter_connections",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Ammeter in series; voltmeter in parallel", 2),
            ("Ammeter has very low resistance; voltmeter has very high resistance", 2),
            ("Explanation of short circuit / blocked current due to meter resistance", 1),
            ("Select largest scale first to avoid damaging the meter", 1),
        ],
        [
            "Think about how much current should flow through each measuring instrument.",
            "An ammeter measures current passing through a branch (series, low $R$); a voltmeter measures potential difference between two points (parallel, high $R$).",
            "Ammeter: series, low $R$. Voltmeter: parallel, high $R$. Start on the largest scale.",
        ],
        ["swapping_series_and_parallel_meter_connections", "confusing_internal_resistance_of_voltmeter_and_ammeter"],
        ["ammeter", "voltmeter", "series", "parallel", "internal resistance"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 05: Ohm's Law statement and direct calculations
# ---------------------------------------------------------------------------
def arch_05_ohms_law_statement_and_conditions(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r_val = r.choice([4, 6, 8, 10, 12, 15, 20, 25])
    i_val = r.choice([0.5, 0.8, 1.2, 1.5, 2.0, 2.5, 3.0])
    v_val = round(i_val * r_val, 2)
    v_new = round(v_val * 1.5, 2)
    i_new = round(i_val * 1.5, 2)

    prompt = (
        f"An ohmic resistor carries a current of **${fmt_sa(i_val)}\\text{{ A}}$** when the potential difference across its terminals is **${fmt_sa(v_val)}\\text{{ V}}$**.\n\n"
        f"1. State **Ohm's Law** in words.\n"
        f"2. Calculate the resistance ($R$) of the resistor.\n"
        f"3. If the potential difference across this resistor is increased to **${fmt_sa(v_new)}\\text{{ V}}$** while its temperature is kept constant, "
        f"state the new resistance and calculate the new current."
    )

    ans_latex = rf"R = {r_val}\ \Omega; \quad I_{{\text{{new}}}} = {fmt_sa(i_new)}\text{{ A}}"
    sample_answer = (
        f"1. **Ohm's Law:** The potential difference across a conductor is directly proportional to the current in the conductor at constant temperature.\n\n"
        f"2. $$R = \\frac{{V}}{{I}} = \\frac{{{fmt_sa(v_val)}}}{{{fmt_sa(i_val)}}} = {r_val}\\ \\Omega$$\n\n"
        f"3. At constant temperature, the resistance remains **${r_val}\\ \\Omega$**.\n"
        f"   $$I_{{\\text{{new}}}} = \\frac{{V_{{\\text{{new}}}}}}{{R}} = \\frac{{{fmt_sa(v_new)}}}{{{r_val}}} = {fmt_sa(i_new)}\\text{{ A}}$$"
    )

    return make_payload(
        "05_ohms_law_statement_and_conditions",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Correct statement of Ohm's Law including 'at constant temperature'", 2),
            (f"Formula R = V / I and calculation R = {r_val} Ohm", 2),
            (f"State R remains {r_val} Ohm and calculate I_new = {fmt_sa(i_new)} A", 2),
        ],
        [
            "Ohm's Law requires a crucial physical condition to remain constant.",
            f"Use $R = \\frac{{V}}{{I}} = \\frac{{{fmt_sa(v_val)}}}{{{fmt_sa(i_val)}}}$. Since temperature is constant, $R$ does not change when $V$ increases.",
            f"$R = {r_val}\\ \\Omega$ and $I_{{\\text{{new}}}} = {fmt_sa(i_new)}\\text{{ A}}$.",
        ],
        ["omitting_constant_temperature_in_ohms_law", "assuming_resistance_increases_with_voltage_for_ohmic_resistor"],
        ["Ohm's Law", "resistance", "constant temperature", "proportionality"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 06: Ohmic vs non-ohmic conductors
# ---------------------------------------------------------------------------
def arch_06_ohmic_vs_non_ohmic_conductors(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    v1, i1 = r.choice([(2.0, 0.40), (3.0, 0.50), (4.0, 0.80)])
    r1 = round(v1 / i1, 2)
    v2 = v1 * 3
    i2 = round(i1 * 2.0, 2)  # less than 3*i1 because resistance increases as bulb heats up
    r2 = round(v2 / i2, 2)

    prompt = (
        f"A learner investigates the relationship between potential difference and current for a tungsten filament light bulb.\n"
        f"At a potential difference of **${fmt_sa(v1)}\\text{{ V}}$**, the current is **${fmt_sa(i1)}\\text{{ A}}$**.\n"
        f"When the potential difference is increased to **${fmt_sa(v2)}\\text{{ V}}$**, the current is **${fmt_sa(i2)}\\text{{ A}}$**.\n\n"
        f"1. Calculate the resistance of the tungsten filament at ${fmt_sa(v1)}\\text{{ V}}$ and at ${fmt_sa(v2)}\\text{{ V}}$.\n"
        f"2. Classify the tungsten filament as an **ohmic** or **non-ohmic** conductor. Justify your answer.\n"
        f"3. Explain on a microscopic level why the resistance of the filament changes as the current increases."
    )

    ans_latex = rf"R_1 = {fmt_sa(r1)}\ \Omega, \ R_2 = {fmt_sa(r2)}\ \Omega \ (\text{{Non-ohmic}})"
    sample_answer = (
        f"1. At ${fmt_sa(v1)}\\text{{ V}}$:\n"
        f"   $$R_1 = \\frac{{V_1}}{{I_1}} = \\frac{{{fmt_sa(v1)}}}{{{fmt_sa(i1)}}} = {fmt_sa(r1)}\\ \\Omega$$\n"
        f"   At ${fmt_sa(v2)}\\text{{ V}}$:\n"
        f"   $$R_2 = \\frac{{V_2}}{{I_2}} = \\frac{{{fmt_sa(v2)}}}{{{fmt_sa(i2)}}} = {fmt_sa(r2)}\\ \\Omega$$\n\n"
        f"2. **Non-ohmic conductor**, because the ratio $\\frac{{V}}{{I}}$ (resistance) is not constant — it increases from ${fmt_sa(r1)}\\ \\Omega$ to ${fmt_sa(r2)}\\ \\Omega$.\n\n"
        f"3. As current increases, the temperature of the filament rises. The positive metal ions in the crystal lattice vibrate with greater amplitude, "
        f"causing more frequent collisions with drifting electrons and increasing resistance."
    )

    return make_payload(
        "06_ohmic_vs_non_ohmic_conductors",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate R1 = {fmt_sa(r1)} Ohm and R2 = {fmt_sa(r2)} Ohm", 2),
            ("Classify as non-ohmic because resistance is not constant", 2),
            ("Microscopic explanation: higher temperature increases lattice ion vibrations and electron collisions", 2),
        ],
        [
            "Calculate $R = V/I$ at both operating points and compare the values.",
            "An ohmic conductor has a constant resistance; a non-ohmic conductor has a changing resistance.",
            f"$R_1 = {fmt_sa(r1)}\\ \\Omega$, $R_2 = {fmt_sa(r2)}\\ \\Omega$ (non-ohmic due to heating and increased lattice vibrations).",
        ],
        ["classifying_bulb_filament_as_ohmic", "confusing_electron_speed_with_lattice_vibration"],
        ["ohmic", "non-ohmic", "filament", "temperature", "lattice vibrations"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 07: I-V characteristic graph gradient analysis (with inline SVG)
# ---------------------------------------------------------------------------
def arch_07_iv_characteristic_graph_gradient_analysis(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r_ohm = r.choice([2, 4, 5, 8, 10, 20])
    v_max = r.choice([8, 10, 12, 16, 20])
    i_max = round(v_max / r_ohm, 2)
    grad = round(i_max / v_max, 4)

    svg = _svg_iv_graph(r_ohm, v_max)

    prompt = (
        f"An experiment is performed on **Conductor X** at constant temperature. "
        f"Current ($I$) is plotted on the vertical axis against potential difference ($V$) on the horizontal axis, "
        f"reaching $I = {fmt_sa(i_max)}\\text{{ A}}$ at $V = {v_max}\\text{{ V}}$.\n\n"
        f"1. State what physical quantity is represented by the gradient ($\\frac{{\\Delta I}}{{\\Delta V}}$) of this plot.\n"
        f"2. Calculate the gradient of the line.\n"
        f"3. Hence determine the resistance ($R$) of Conductor X.\n"
        f"4. Calculate the current through Conductor X when a potential difference of **${v_max + 4}\\text{{ V}}$** is applied."
    )

    i_ext = round((v_max + 4) / r_ohm, 2)
    ans_latex = rf"\text{{Gradient}} = {fmt_sa(grad, 3)}\ \Omega^{{-1}}; \quad R = {r_ohm}\ \Omega; \quad I = {fmt_sa(i_ext)}\text{{ A}}"
    sample_answer = (
        f"1. Because $I$ is on the y-axis and $V$ is on the x-axis, the gradient $\\frac{{\\Delta I}}{{\\Delta V}}$ represents the **reciprocal of resistance** ($\\frac{{1}}{{R}}$, or conductance).\n\n"
        f"2. $$\\text{{Gradient}} = \\frac{{\\Delta I}}{{\\Delta V}} = \\frac{{{fmt_sa(i_max)} - 0}}{{{v_max} - 0}} = {fmt_sa(grad, 3)}\\ \\Omega^{{-1}}$$\n\n"
        f"3. $$R = \\frac{{1}}{{\\text{{gradient}}}} = \\frac{{{v_max}}}{{{fmt_sa(i_max)}}} = {r_ohm}\\ \\Omega$$\n\n"
        f"4. $$I = \\frac{{V}}{{R}} = \\frac{{{v_max + 4}}}{{{r_ohm}}} = {fmt_sa(i_ext)}\\text{{ A}}$$"
    )

    return make_payload(
        "07_iv_characteristic_graph_gradient_analysis",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Identify gradient of I vs V as 1/R (reciprocal of resistance)", 1),
            (f"Calculate gradient = {fmt_sa(grad, 3)} Ohm^-1", 2),
            (f"Determine resistance R = {r_ohm} Ohm", 1),
            (f"Calculate current I = {fmt_sa(i_ext)} A at {v_max + 4} V", 2),
        ],
        [
            "Check which variable is on the vertical axis ($I$) and which is on the horizontal axis ($V$).",
            f"Since $\\text{{gradient}} = \\frac{{\\Delta I}}{{\\Delta V}} = \\frac{{1}}{{R}}$, take the reciprocal of the gradient to find $R$.",
            f"$R = {r_ohm}\\ \\Omega$ and $I = \\frac{{{v_max + 4}}}{{{r_ohm}}} = {fmt_sa(i_ext)}\\text{{ A}}$.",
        ],
        ["equating_iv_gradient_directly_to_resistance_instead_of_reciprocal", "axis_swap_error"],
        ["I-V characteristic", "gradient", "reciprocal of resistance", "ohmic"],
        difficulty="medium",
        diagram_spec={"kind": "inline_svg", "diagram_role": "context", "svg": svg},
    )


# ---------------------------------------------------------------------------
# Subskill 08: Comparing two resistors on V-I axes (with inline SVG)
# ---------------------------------------------------------------------------
def arch_08_comparing_two_resistors_on_iv_axes(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    rp, rq = r.choice([(6, 3), (8, 4), (10, 5), (12, 4), (9, 3), (15, 5)])
    i_max = r.choice([2, 3, 4])
    vp_max = rp * i_max
    vq_max = rq * i_max

    svg = _svg_two_resistors_vi(rp, rq, i_max)

    prompt = (
        f"Potential difference ($V$, vertical axis) versus current ($I$, horizontal axis) is plotted for two ohmic conductors **P** and **Q**.\n"
        f"At $I = {i_max}\\text{{ A}}$, conductor P has $V_P = {vp_max}\\text{{ V}}$ and conductor Q has $V_Q = {vq_max}\\text{{ V}}$.\n\n"
        f"1. Without calculating, state which conductor (**P** or **Q**) has the greater resistance. Give a reason based on the gradient.\n"
        f"2. Calculate the resistance $R_P$ and $R_Q$.\n"
        f"3. Calculate the equivalent resistance if P and Q are connected in **series**."
    )

    r_ser = rp + rq
    ans_latex = rf"R_P = {rp}\ \Omega, \ R_Q = {rq}\ \Omega, \ R_s = {r_ser}\ \Omega"
    sample_answer = (
        f"1. **Conductor P** has the greater resistance. On a $V\\text{{ vs }}I$ plot, the gradient $\\frac{{\\Delta V}}{{\\Delta I}}$ equals the resistance $R$, and line P has a steeper gradient than line Q.\n\n"
        f"2. $$R_P = \\frac{{V_P}}{{I}} = \\frac{{{vp_max}}}{{{i_max}}} = {rp}\\ \\Omega$$\n"
        f"   $$R_Q = \\frac{{V_Q}}{{I}} = \\frac{{{vq_max}}}{{{i_max}}} = {rq}\\ \\Omega$$\n\n"
        f"3. $$R_s = R_P + R_Q = {rp} + {rq} = {r_ser}\\ \\Omega$$"
    )

    return make_payload(
        "08_comparing_two_resistors_on_iv_axes",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Identify P as having greater resistance because V vs I gradient = R and P is steeper", 2),
            (f"Calculate R_P = {rp} Ohm and R_Q = {rq} Ohm", 2),
            (f"Calculate series resistance R_s = {r_ser} Ohm", 1),
        ],
        [
            "With $V$ on the vertical axis and $I$ on the horizontal axis, $\\text{gradient} = \\frac{\\Delta V}{\\Delta I} = R$.",
            f"Divide $V_P = {vp_max}\\text{{ V}}$ and $V_Q = {vq_max}\\text{{ V}}$ by $I = {i_max}\\text{{ A}}$.",
            f"$R_P = {rp}\\ \\Omega$, $R_Q = {rq}\\ \\Omega$, $R_s = {r_ser}\\ \\Omega$.",
        ],
        ["confusing_v_vs_i_slope_with_i_vs_v_slope", "parallel_formula_used_for_series"],
        ["V-I plot", "gradient", "resistance comparison"],
        difficulty="medium",
        diagram_spec={"kind": "inline_svg", "diagram_role": "context", "svg": svg},
    )


# ---------------------------------------------------------------------------
# Subskill 09: Experimental verification of Ohm's Law
# ---------------------------------------------------------------------------
def arch_09_experimental_verification_of_ohms_law(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r_target = r.choice([5, 8, 10, 12, 15])
    i_vals = [0.2, 0.4, 0.6, 0.8]
    v_vals = [round(i * r_target, 1) for i in i_vals]
    metal = r.choice(["nichrome", "constantan", "manganin"])

    prompt = (
        f"A group of learners conducts an experiment to verify Ohm's Law using a **{metal} wire resistor**, a battery, a rheostat (variable resistor), "
        f"an ammeter, a voltmeter, and a switch. They record pairs of $(V; I)$ values: "
        f"$({fmt_sa(v_vals[0])}\\text{{ V}}; {fmt_sa(i_vals[0])}\\text{{ A}})$, "
        f"$({fmt_sa(v_vals[1])}\\text{{ V}}; {fmt_sa(i_vals[1])}\\text{{ A}})$, "
        f"$({fmt_sa(v_vals[2])}\\text{{ V}}; {fmt_sa(i_vals[2])}\\text{{ A}})$, and "
        f"$({fmt_sa(v_vals[3])}\\text{{ V}}; {fmt_sa(i_vals[3])}\\text{{ A}})$.\n\n"
        f"1. Identify the **independent variable**, **dependent variable**, and **controlled variable** in this investigation.\n"
        f"2. State the purpose of the **rheostat** in the experimental setup.\n"
        f"3. Explain why the learners open the switch immediately after taking each reading.\n"
        f"4. Calculate the resistance of the {metal} resistor from the recorded data."
    )

    ans_latex = rf"R = {r_target}\ \Omega; \quad \text{{Controlled variable: temperature}}"
    sample_answer = (
        f"1. **Independent variable:** Potential difference ($V$) [or current $I$].\n"
        f"   **Dependent variable:** Current ($I$) [or potential difference $V$].\n"
        f"   **Controlled variable:** Temperature of the {metal} resistor.\n\n"
        f"2. The **rheostat** varies the total resistance of the circuit so that the current and the potential difference across the {metal} resistor can be adjusted to obtain multiple readings.\n\n"
        f"3. Opening the switch between readings prevents the wire from heating up, ensuring that the **temperature remains constant**.\n\n"
        f"4. $$R = \\frac{{V}}{{I}} = \\frac{{{fmt_sa(v_vals[1])}}}{{{fmt_sa(i_vals[1])}}} = {r_target}\\ \\Omega$$"
    )

    return make_payload(
        "09_experimental_verification_of_ohms_law",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Identify independent, dependent, and controlled (temperature) variables", 3),
            ("Purpose of rheostat: vary circuit resistance/current to take multiple V and I readings", 1),
            ("Reason for opening switch: prevent heating / keep temperature constant", 1),
            (f"Calculate resistance R = {r_target} Ohm", 1),
        ],
        [
            "In Ohm's Law, temperature must be kept constant while $V$ and $I$ are varied.",
            "A rheostat adjusts the total resistance so multiple $(V, I)$ data points can be measured.",
            f"Controlled variable: temperature. $R = {r_target}\\ \\Omega$.",
        ],
        ["listing_resistance_as_independent_variable", "forgetting_thermal_heating_effect_when_switch_closed"],
        ["Ohm's Law experiment", "rheostat", "controlled variable", "temperature"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 10: EMF vs terminal potential difference and lost volts
# ---------------------------------------------------------------------------
def arch_10_emf_vs_terminal_potential_difference(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    emf = r.choice([9.0, 12.0, 15.0, 18.0, 24.0])
    v_term = round(emf - r.choice([1.2, 1.5, 1.8, 2.0, 2.4]), 2)
    v_lost = round(emf - v_term, 2)
    i_curr = r.choice([1.5, 2.0, 2.5, 3.0])
    r_int = round(v_lost / i_curr, 2)

    prompt = (
        f"A voltmeter connected directly across the terminals of a battery reads **${fmt_sa(emf)}\\text{{ V}}$** when the switch is **open**.\n"
        f"When the switch is **closed**, a current of **${fmt_sa(i_curr)}\\text{{ A}}$** flows through the circuit and the voltmeter reading drops to **${fmt_sa(v_term)}\\text{{ V}}$**.\n\n"
        f"1. Define the **emf** ($\\mathcal{{E}}$) of a battery.\n"
        f"2. Write down the emf and the terminal potential difference of this battery.\n"
        f"3. Explain why the voltmeter reading decreases when the switch is closed.\n"
        f"4. Calculate the internal resistance ($r$) of the battery."
    )

    ans_latex = rf"\mathcal{{E}} = {fmt_sa(emf)}\text{{ V}}, \ V_{{\text{{term}}}} = {fmt_sa(v_term)}\text{{ V}}, \ r = {fmt_sa(r_int)}\ \Omega"
    sample_answer = (
        f"1. **Definition:** Emf ($\\mathcal{{E}}$) is the maximum energy provided (or total work done) by a battery per coulomb of charge passing through it (measured when no current flows).\n\n"
        f"2. $\\mathcal{{E}} = {fmt_sa(emf)}\\text{{ V}}$ and $V_{{\\text{{terminal}}}} = {fmt_sa(v_term)}\\text{{ V}}$.\n\n"
        f"3. The battery itself has internal resistance ($r$). When current flows, some energy per coulomb ('lost volts', $V_{{\\text{{internal}}}} = Ir = {fmt_sa(v_lost)}\\text{{ V}}$) is used to overcome the internal resistance of the battery.\n\n"
        f"4. $$V_{{\\text{{lost}}}} = \\mathcal{{E}} - V_{{\\text{{terminal}}}} = {fmt_sa(emf)} - {fmt_sa(v_term)} = {fmt_sa(v_lost)}\\text{{ V}}$$\n"
        f"   $$r = \\frac{{V_{{\\text{{lost}}}}}}{{I}} = \\frac{{{fmt_sa(v_lost)}}}{{{fmt_sa(i_curr)}}} = {fmt_sa(r_int)}\\ \\Omega$$"
    )

    return make_payload(
        "10_emf_vs_terminal_potential_difference",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Correct definition of emf (maximum energy/work per unit charge by battery)", 2),
            (f"Identify emf = {fmt_sa(emf)} V and terminal PD = {fmt_sa(v_term)} V", 1),
            ("Explain voltage drop due to internal resistance (lost volts V_lost = Ir)", 1),
            (f"Calculate internal resistance r = {fmt_sa(r_int)} Ohm", 2),
        ],
        [
            "The open-switch reading gives the emf ($\\mathcal{E}$); the closed-switch reading gives the terminal potential difference ($V_{\\text{ext}}$).",
            f"Find the 'lost volts' $V_{{\\text{{lost}}}} = \\mathcal{{E}} - V_{{\\text{{ext}}}} = {fmt_sa(v_lost)}\\text{{ V}}$, then divide by $I = {fmt_sa(i_curr)}\\text{{ A}}$.",
            f"$r = \\frac{{{fmt_sa(v_lost)}}}{{{fmt_sa(i_curr)}}} = {fmt_sa(r_int)}\\ \\Omega$.",
        ],
        ["confusing_emf_with_terminal_potential_difference", "using_terminal_voltage_to_find_internal_resistance"],
        ["emf", "terminal potential difference", "lost volts", "internal resistance"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 11: Internal resistance single load calculation (E = I(R + r))
# ---------------------------------------------------------------------------
def arch_11_internal_resistance_single_load_calculation(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r_ext = r.choice([4.0, 5.0, 7.0, 9.0, 11.0])
    r_int = r.choice([0.5, 1.0, 1.5, 2.0])
    i_curr = r.choice([1.2, 1.5, 2.0, 2.4, 3.0])
    emf = round(i_curr * (r_ext + r_int), 2)
    v_ext = round(i_curr * r_ext, 2)
    v_lost = round(i_curr * r_int, 2)

    prompt = (
        f"A battery with an emf of **$\\mathcal{{E}} = {fmt_sa(emf)}\\text{{ V}}$** and internal resistance **$r = {fmt_sa(r_int)}\\ \\Omega$** "
        f"is connected in series with an external resistor of resistance **$R = {fmt_sa(r_ext)}\\ \\Omega$** and a closed switch.\n\n"
        f"1. Calculate the total resistance of the circuit.\n"
        f"2. Calculate the current ($I$) flowing in the circuit.\n"
        f"3. Calculate the terminal potential difference ($V_{{\\text{{ext}}}}$) across the battery.\n"
        f"4. Calculate the 'lost volts' ($V_{{\\text{{internal}}}}$) inside the battery."
    )

    ans_latex = rf"I = {fmt_sa(i_curr)}\text{{ A}}, \ V_{{\text{{ext}}}} = {fmt_sa(v_ext)}\text{{ V}}, \ V_{{\text{{lost}}}} = {fmt_sa(v_lost)}\text{{ V}}"
    sample_answer = (
        f"1. $$R_{{\\text{{total}}}} = R + r = {fmt_sa(r_ext)} + {fmt_sa(r_int)} = {fmt_sa(r_ext + r_int)}\\ \\Omega$$\n\n"
        f"2. $$\\mathcal{{E}} = I(R + r) \\implies I = \\frac{{\\mathcal{{E}}}}{{R + r}} = \\frac{{{fmt_sa(emf)}}}{{{fmt_sa(r_ext + r_int)}}} = {fmt_sa(i_curr)}\\text{{ A}}$$\n\n"
        f"3. $$V_{{\\text{{ext}}}} = I \\cdot R = {fmt_sa(i_curr)} \\times {fmt_sa(r_ext)} = {fmt_sa(v_ext)}\\text{{ V}}$$\n\n"
        f"4. $$V_{{\\text{{internal}}}} = I \\cdot r = {fmt_sa(i_curr)} \\times {fmt_sa(r_int)} = {fmt_sa(v_lost)}\\text{{ V}}$$"
    )

    return make_payload(
        "11_internal_resistance_single_load_calculation",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Total resistance R + r = {fmt_sa(r_ext + r_int)} Ohm", 1),
            (f"Formula E = I(R + r) and current I = {fmt_sa(i_curr)} A", 2),
            (f"Terminal PD V_ext = {fmt_sa(v_ext)} V", 1),
            (f"Lost volts V_internal = {fmt_sa(v_lost)} V", 1),
        ],
        [
            "Use the complete circuit Ohm's Law equation: $\\mathcal{E} = I(R + r)$.",
            f"Divide $\\mathcal{{E}} = {fmt_sa(emf)}\\text{{ V}}$ by $(R + r) = {fmt_sa(r_ext + r_int)}\\ \\Omega$ to get $I$.",
            f"$I = {fmt_sa(i_curr)}\\text{{ A}}$, $V_{{\\text{{ext}}}} = {fmt_sa(v_ext)}\\text{{ V}}$, $V_{{\\text{{lost}}}} = {fmt_sa(v_lost)}\\text{{ V}}$.",
        ],
        ["ignoring_internal_resistance_in_current_calculation", "adding_lost_volts_to_emf"],
        ["internal resistance", "emf", "terminal voltage", "lost volts"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 12: Internal resistance dual switch / load state equations
# ---------------------------------------------------------------------------
def arch_12_internal_resistance_dual_switch_readings(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r_int = r.choice([1.0, 1.5, 2.0, 2.5])
    emf = r.choice([12.0, 15.0, 18.0, 24.0])
    # Choose two currents I1 and I2
    i1, i2 = r.choice([(1.0, 2.0), (1.5, 3.0), (2.0, 4.0), (1.2, 2.4)])
    v1 = round(emf - i1 * r_int, 2)
    v2 = round(emf - i2 * r_int, 2)

    prompt = (
        f"A battery of unknown emf $\\mathcal{{E}}$ and internal resistance $r$ is connected to a variable external load.\n"
        f"- In State 1, the ammeter reads **$I_1 = {fmt_sa(i1)}\\text{{ A}}$** and the terminal voltmeter reads **$V_1 = {fmt_sa(v1)}\\text{{ V}}$**.\n"
        f"- In State 2, the load is adjusted so the ammeter reads **$I_2 = {fmt_sa(i2)}\\text{{ A}}$** and the terminal voltmeter reads **$V_2 = {fmt_sa(v2)}\\text{{ V}}$**.\n\n"
        f"1. Write down two equations relating $\\mathcal{{E}}$, $r$, $V$, and $I$ for State 1 and State 2.\n"
        f"2. Solve the simultaneous equations to calculate the internal resistance ($r$) of the battery.\n"
        f"3. Calculate the emf ($\\mathcal{{E}}$) of the battery."
    )

    ans_latex = rf"r = {fmt_sa(r_int)}\ \Omega; \quad \mathcal{{E}} = {fmt_sa(emf)}\text{{ V}}"
    sample_answer = (
        f"1. Using $\\mathcal{{E}} = V + Ir$:\n"
        f"   - State 1: $\\mathcal{{E}} = {fmt_sa(v1)} + {fmt_sa(i1)}r$\n"
        f"   - State 2: $\\mathcal{{E}} = {fmt_sa(v2)} + {fmt_sa(i2)}r$\n\n"
        f"2. Equating the two expressions for $\\mathcal{{E}}$:\n"
        f"   $${fmt_sa(v1)} + {fmt_sa(i1)}r = {fmt_sa(v2)} + {fmt_sa(i2)}r$$\n"
        f"   $${fmt_sa(v1 - v2)} = {fmt_sa(i2 - i1)}r \\implies r = \\frac{{{fmt_sa(v1 - v2)}}}{{{fmt_sa(i2 - i1)}}} = {fmt_sa(r_int)}\\ \\Omega$$\n\n"
        f"3. Substitute $r = {fmt_sa(r_int)}\\ \\Omega$ into State 1:\n"
        f"   $$\\mathcal{{E}} = {fmt_sa(v1)} + ({fmt_sa(i1)})({fmt_sa(r_int)}) = {fmt_sa(emf)}\\text{{ V}}$$"
    )

    return make_payload(
        "12_internal_resistance_dual_switch_readings",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Set up two simultaneous equations E = V1 + I1*r and E = V2 + I2*r", 2),
            (f"Solve for internal resistance r = {fmt_sa(r_int)} Ohm", 2),
            (f"Calculate emf E = {fmt_sa(emf)} V", 2),
        ],
        [
            "The emf $\\mathcal{E}$ and internal resistance $r$ of the battery remain constant between State 1 and State 2.",
            f"Equate $V_1 + I_1 r = V_2 + I_2 r$, so $r = \\frac{{V_1 - V_2}}{{I_2 - I_1}}$.",
            f"$r = {fmt_sa(r_int)}\\ \\Omega$ and $\\mathcal{{E}} = {fmt_sa(emf)}\\text{{ V}}$.",
        ],
        ["sign_error_in_simultaneous_internal_resistance_equations", "assuming_terminal_voltage_is_constant"],
        ["simultaneous equations", "internal resistance", "emf"],
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Subskill 13: Series resistors equivalent resistance and current (with SVG)
# ---------------------------------------------------------------------------
def arch_13_series_resistors_equivalent_and_current(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r1 = r.choice([2, 3, 4, 5])
    r2 = r.choice([4, 6, 8])
    r3 = r.choice([3, 5, 6, 10])
    rs = r1 + r2 + r3
    i_tot = r.choice([0.5, 1.0, 1.5, 2.0, 2.5])
    v_tot = round(i_tot * rs, 1)
    v2 = round(i_tot * r2, 2)

    svg = _svg_series_circuit(v_tot, r1, r2, r3)

    prompt = (
        f"Three resistors of resistance **$R_1 = {r1}\\ \\Omega$**, **$R_2 = {r2}\\ \\Omega$**, and **$R_3 = {r3}\\ \\Omega$** "
        f"are connected in series with a battery of terminal potential difference **${fmt_sa(v_tot)}\\text{{ V}}$**.\n\n"
        f"1. Calculate the total equivalent resistance ($R_s$) of the series combination.\n"
        f"2. Calculate the current ($I$) flowing through resistor $R_1$.\n"
        f"3. Write down the current flowing through resistor $R_3$. Give a reason.\n"
        f"4. Calculate the potential difference ($V_2$) across resistor $R_2$."
    )

    ans_latex = rf"R_s = {rs}\ \Omega, \ I = {fmt_sa(i_tot)}\text{{ A}}, \ V_2 = {fmt_sa(v2)}\text{{ V}}"
    sample_answer = (
        f"1. $$R_s = R_1 + R_2 + R_3 = {r1} + {r2} + {r3} = {rs}\\ \\Omega$$\n\n"
        f"2. $$I = \\frac{{V_{{\\text{{total}}}}}}{{R_s}} = \\frac{{{fmt_sa(v_tot)}}}{{{rs}}} = {fmt_sa(i_tot)}\\text{{ A}}$$\n\n"
        f"3. **$I_3 = {fmt_sa(i_tot)}\\text{{ A}}$**, because the current is the **same at all points** in a series circuit.\n\n"
        f"4. $$V_2 = I \\cdot R_2 = {fmt_sa(i_tot)} \\times {r2} = {fmt_sa(v2)}\\text{{ V}}$$"
    )

    return make_payload(
        "13_series_resistors_equivalent_and_current",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate R_s = {rs} Ohm", 1),
            (f"Calculate series current I = {fmt_sa(i_tot)} A", 2),
            (f"State I_3 = {fmt_sa(i_tot)} A because current is constant in series", 1),
            (f"Calculate V_2 = {fmt_sa(v2)} V", 2),
        ],
        [
            "In a series circuit, resistances add directly: $R_s = R_1 + R_2 + R_3$.",
            f"Find total current $I = V_{{\\text{{tot}}}} / R_s = {fmt_sa(v_tot)} / {rs}$. The same current flows through every series resistor.",
            f"$R_s = {rs}\\ \\Omega$, $I = {fmt_sa(i_tot)}\\text{{ A}}$, $V_2 = {fmt_sa(v2)}\\text{{ V}}$.",
        ],
        ["thinking_current_decreases_after_each_series_resistor", "using_total_resistance_for_single_resistor_voltage"],
        ["series circuit", "equivalent resistance", "constant current"],
        difficulty="easy",
        diagram_spec={"kind": "inline_svg", "diagram_role": "context", "svg": svg},
    )


# ---------------------------------------------------------------------------
# Subskill 14: Series potential divider ratios
# ---------------------------------------------------------------------------
def arch_14_series_potential_divider_ratios(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r1 = r.choice([4, 6, 8, 10, 12])
    rx = r.choice([6, 8, 12, 15, 18, 20])
    i_ser = r.choice([0.5, 1.0, 1.5, 2.0])
    v1 = round(i_ser * r1, 1)
    vx = round(i_ser * rx, 1)
    v_tot = round(v1 + vx, 1)

    prompt = (
        f"Two resistors, **$R_1 = {r1}\\ \\Omega$** and an unknown resistor **$R_x$**, are connected in series across a **${fmt_sa(v_tot)}\\text{{ V}}$** supply.\n"
        f"A high-resistance voltmeter connected across $R_1$ reads **${fmt_sa(v1)}\\text{{ V}}$**.\n\n"
        f"1. State why a series circuit is described as a **potential divider**.\n"
        f"2. Calculate the potential difference ($V_x$) across resistor $R_x$.\n"
        f"3. Calculate the current ($I$) in the series circuit.\n"
        f"4. Determine the resistance of the unknown resistor $R_x$."
    )

    ans_latex = rf"V_x = {fmt_sa(vx)}\text{{ V}}, \ I = {fmt_sa(i_ser)}\text{{ A}}, \ R_x = {rx}\ \Omega"
    sample_answer = (
        f"1. Series resistors divide the total potential difference in direct proportion to their resistances ($V_{{\\text{{total}}}} = V_1 + V_x$ and $V_i \\propto R_i$).\n\n"
        f"2. $$V_x = V_{{\\text{{total}}}} - V_1 = {fmt_sa(v_tot)} - {fmt_sa(v1)} = {fmt_sa(vx)}\\text{{ V}}$$\n\n"
        f"3. $$I = \\frac{{V_1}}{{R_1}} = \\frac{{{fmt_sa(v1)}}}{{{r1}}} = {fmt_sa(i_ser)}\\text{{ A}}$$\n\n"
        f"4. $$R_x = \\frac{{V_x}}{{I}} = \\frac{{{fmt_sa(vx)}}}{{{fmt_sa(i_ser)}}} = {rx}\\ \\Omega$$"
    )

    return make_payload(
        "14_series_potential_divider_ratios",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Explain potential division: total PD is shared proportionally to resistance", 1),
            (f"Calculate V_x = {fmt_sa(vx)} V", 1),
            (f"Calculate series current I = {fmt_sa(i_ser)} A", 2),
            (f"Calculate unknown resistance R_x = {rx} Ohm", 2),
        ],
        [
            "In series, $V_{\\text{total}} = V_1 + V_x$ and the current through both resistors is identical.",
            f"First find $V_x = {fmt_sa(v_tot)} - {fmt_sa(v1)} = {fmt_sa(vx)}\\text{{ V}}$ and $I = V_1 / R_1 = {fmt_sa(v1)} / {r1}$.",
            f"$V_x = {fmt_sa(vx)}\\text{{ V}}$, $I = {fmt_sa(i_ser)}\\text{{ A}}$, $R_x = {rx}\\ \\Omega$.",
        ],
        ["using_total_voltage_across_single_series_resistor", "inverting_voltage_ratio_in_potential_divider"],
        ["potential divider", "voltage ratio", "series resistors"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 15: Parallel two resistors product-over-sum (with inline SVG)
# ---------------------------------------------------------------------------
def arch_15_parallel_two_resistors_product_over_sum(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r1, r2 = r.choice([(6, 3), (12, 4), (12, 6), (20, 5), (15, 30), (10, 40), (8, 24)])
    rp = round((r1 * r2) / (r1 + r2), 2)
    v_tot = r.choice([12, 18, 24, 30, 36])
    i_tot = round(v_tot / rp, 2)

    svg = _svg_parallel_circuit(v_tot, r1, r2)

    prompt = (
        f"Two resistors of resistance **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$** are connected in parallel "
        f"across a battery supplying a terminal potential difference of **${v_tot}\\text{{ V}}$**.\n\n"
        f"1. Calculate the equivalent resistance ($R_p$) of the parallel combination.\n"
        f"2. Compare $R_p$ with the smaller individual resistor and state the general rule for parallel resistance.\n"
        f"3. Calculate the total current ($I_{{\\text{{main}}}}$) leaving the battery."
    )

    ans_latex = rf"R_p = {fmt_sa(rp)}\ \Omega; \quad I_{{\text{{main}}}} = {fmt_sa(i_tot)}\text{{ A}}"
    sample_answer = (
        f"1. $$\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_2}} = \\frac{{1}}{{{r1}}} + \\frac{{1}}{{{r2}}}$$\n"
        f"   $$R_p = \\frac{{R_1 \\cdot R_2}}{{R_1 + R_2}} = \\frac{{{r1} \\times {r2}}}{{{r1} + {r2}}} = {fmt_sa(rp)}\\ \\Omega$$\n\n"
        f"2. $R_p = {fmt_sa(rp)}\\ \\Omega$ is **smaller than the smallest individual resistor** ($\\min({r1}, {r2}) = {min(r1, r2)}\\ \\Omega$), "
        f"because adding parallel branches provides additional pathways for current.\n\n"
        f"3. $$I_{{\\text{{main}}}} = \\frac{{V}}{{R_p}} = \\frac{{{v_tot}}}{{{fmt_sa(rp)}}} = {fmt_sa(i_tot)}\\text{{ A}}$$"
    )

    return make_payload(
        "15_parallel_two_resistors_product_over_sum",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Formula 1/Rp = 1/R1 + 1/R2 and substitution", 1),
            (f"Calculate Rp = {fmt_sa(rp)} Ohm", 1),
            ("State Rp is always less than the smallest branch resistance", 1),
            (f"Calculate main current I_main = {fmt_sa(i_tot)} A", 2),
        ],
        [
            "For two resistors in parallel, $\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2}$, or $R_p = \\frac{R_1 R_2}{R_1 + R_2}$.",
            "Remember to invert $\\frac{1}{R_p}$ at the end! Check that $R_p$ is smaller than both $R_1$ and $R_2$.",
            f"$R_p = {fmt_sa(rp)}\\ \\Omega$ and $I_{{\\text{{main}}}} = {fmt_sa(i_tot)}\\text{{ A}}$.",
        ],
        ["forgetting_to_invert_1_over_rp", "adding_parallel_resistors_directly"],
        ["parallel resistors", "equivalent resistance", "main current"],
        difficulty="easy",
        diagram_spec={"kind": "inline_svg", "diagram_role": "context", "svg": svg},
    )


# ---------------------------------------------------------------------------
# Subskill 16: Parallel three or four resistors
# ---------------------------------------------------------------------------
def arch_16_parallel_three_or_four_resistors(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    combo = r.choice([
        (6, 12, 4, 2.0),
        (10, 20, 4, 2.5),
        (12, 6, 4, 2.0),
        (15, 30, 10, 5.0),
        (8, 8, 4, 2.0),
        (12, 12, 6, 3.0),
    ])
    r1, r2, r3, rp = combo
    v_supply = r.choice([10, 12, 15, 20, 24])
    i_tot = round(v_supply / rp, 2)
    i1 = round(v_supply / r1, 2)

    prompt = (
        f"Three resistors of resistance **$R_1 = {r1}\\ \\Omega$**, **$R_2 = {r2}\\ \\Omega$**, and **$R_3 = {r3}\\ \\Omega$** "
        f"are connected in parallel across a **${v_supply}\\text{{ V}}$** power supply of negligible internal resistance.\n\n"
        f"1. Calculate the equivalent resistance ($R_p$) of the three parallel branches.\n"
        f"2. Write down the potential difference across each of the three resistors.\n"
        f"3. Calculate the current ($I_1$) in branch 1 (through $R_1$) and the total current ($I_{{\\text{{total}}}}$) drawn from the supply."
    )

    ans_latex = rf"R_p = {fmt_sa(rp)}\ \Omega, \ V = {v_supply}\text{{ V}}, \ I_1 = {fmt_sa(i1)}\text{{ A}}, \ I_{{\text{{total}}}} = {fmt_sa(i_tot)}\text{{ A}}"
    sample_answer = (
        f"1. $$\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_2}} + \\frac{{1}}{{R_3}} = \\frac{{1}}{{{r1}}} + \\frac{{1}}{{{r2}}} + \\frac{{1}}{{{r3}}} = \\frac{{1}}{{{fmt_sa(rp)}}}$$\n"
        f"   $$R_p = {fmt_sa(rp)}\\ \\Omega$$\n\n"
        f"2. Each parallel branch has the same potential difference: **$V_1 = V_2 = V_3 = {v_supply}\\text{{ V}}$**.\n\n"
        f"3. $$I_1 = \\frac{{V}}{{R_1}} = \\frac{{{v_supply}}}{{{r1}}} = {fmt_sa(i1)}\\text{{ A}}$$\n"
        f"   $$I_{{\\text{{total}}}} = \\frac{{V}}{{R_p}} = \\frac{{{v_supply}}}{{{fmt_sa(rp)}}} = {fmt_sa(i_tot)}\\text{{ A}}$$"
    )

    return make_payload(
        "16_parallel_three_or_four_resistors",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Correct reciprocal sum 1/Rp = 1/R1 + 1/R2 + 1/R3", 1),
            (f"Invert to find Rp = {fmt_sa(rp)} Ohm", 1),
            (f"State potential difference across each branch is {v_supply} V", 1),
            (f"Calculate I_1 = {fmt_sa(i1)} A and I_total = {fmt_sa(i_tot)} A", 2),
        ],
        [
            "Do not use $R_1 R_2 R_3 / (R_1 + R_2 + R_3)$ for three resistors! Sum the reciprocals: $\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}$.",
            f"Find the common denominator for $\\frac{{1}}{{{r1}}} + \\frac{{1}}{{{r2}}} + \\frac{{1}}{{{r3}}}$, then take the reciprocal.",
            f"$R_p = {fmt_sa(rp)}\\ \\Omega$, $I_1 = {fmt_sa(i1)}\\text{{ A}}$, $I_{{\\text{{total}}}} = {fmt_sa(i_tot)}\\text{{ A}}$.",
        ],
        ["using_product_over_sum_for_three_resistors", "forgetting_to_invert_reciprocal_sum"],
        ["three parallel resistors", "reciprocal formula", "branch current"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 17: Parallel current divider branch currents
# ---------------------------------------------------------------------------
def arch_17_parallel_current_divider_branch_currents(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r1, r2 = r.choice([(4, 12), (6, 12), (5, 15), (8, 24), (10, 30), (6, 18)])
    rp = (r1 * r2) / (r1 + r2)
    i_tot = r.choice([2.0, 3.0, 4.0, 6.0, 8.0])
    v_par = round(i_tot * rp, 2)
    i1 = round(v_par / r1, 2)
    i2 = round(v_par / r2, 2)

    prompt = (
        f"A total main-branch current of **$I_{{\\text{{total}}}} = {fmt_sa(i_tot)}\\text{{ A}}$** enters a parallel combination "
        f"of two resistors: **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**.\n\n"
        f"1. State why a parallel combination of resistors acts as a **current divider**.\n"
        f"2. Calculate the equivalent resistance ($R_p$) and the potential difference ($V_p$) across the parallel network.\n"
        f"3. Calculate the branch currents **$I_1$** (through $R_1$) and **$I_2$** (through $R_2$).\n"
        f"4. Verify that $I_1 + I_2 = I_{{\\text{{total}}}}$. Which resistor carries the larger current?"
    )

    ans_latex = rf"V_p = {fmt_sa(v_par)}\text{{ V}}, \ I_1 = {fmt_sa(i1)}\text{{ A}}, \ I_2 = {fmt_sa(i2)}\text{{ A}}"
    sample_answer = (
        f"1. At a parallel junction, the total current splits into the branches inversely proportional to the branch resistances ($I_i = \\frac{{V_p}}{{R_i}}$).\n\n"
        f"2. $$R_p = \\frac{{{r1} \\times {r2}}}{{{r1} + {r2}}} = {fmt_sa(rp)}\\ \\Omega$$\n"
        f"   $$V_p = I_{{\\text{{total}}}} \\cdot R_p = {fmt_sa(i_tot)} \\times {fmt_sa(rp)} = {fmt_sa(v_par)}\\text{{ V}}$$\n\n"
        f"3. $$I_1 = \\frac{{V_p}}{{R_1}} = \\frac{{{fmt_sa(v_par)}}}{{{r1}}} = {fmt_sa(i1)}\\text{{ A}}$$\n"
        f"   $$I_2 = \\frac{{V_p}}{{R_2}} = \\frac{{{fmt_sa(v_par)}}}{{{r2}}} = {fmt_sa(i2)}\\text{{ A}}$$\n\n"
        f"4. ${fmt_sa(i1)} + {fmt_sa(i2)} = {fmt_sa(i_tot)}\\text{{ A}}$. The **smaller resistor ($R_1 = {r1}\\ \\Omega$)** carries the larger current."
    )

    return make_payload(
        "17_parallel_current_divider_branch_currents",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Explain current division: current splits inversely proportional to resistance", 1),
            (f"Calculate Rp = {fmt_sa(rp)} Ohm and Vp = {fmt_sa(v_par)} V", 2),
            (f"Calculate I_1 = {fmt_sa(i1)} A and I_2 = {fmt_sa(i2)} A", 2),
            ("Identify smaller resistance R1 as carrying larger current", 1),
        ],
        [
            "First find the equivalent resistance $R_p$, then find the voltage across the parallel branches $V_p = I_{\\text{total}} R_p$.",
            f"Once you have $V_p = {fmt_sa(v_par)}\\text{{ V}}$, divide by $R_1$ and $R_2$ respectively.",
            f"$V_p = {fmt_sa(v_par)}\\text{{ V}}$, $I_1 = {fmt_sa(i1)}\\text{{ A}}$, $I_2 = {fmt_sa(i2)}\\text{{ A}}$.",
        ],
        ["assuming_parallel_current_splits_equally_regardless_of_resistance", "direct_instead_of_inverse_current_ratio"],
        ["current divider", "branch current", "parallel junction"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 18: Finding an unknown parallel resistor
# ---------------------------------------------------------------------------
def arch_18_finding_unknown_parallel_resistor(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r1, rx, rp = r.choice([
        (12, 6, 4),
        (15, 10, 6),
        (20, 5, 4),
        (24, 8, 6),
        (30, 15, 10),
        (12, 4, 3),
    ])
    v_par = r.choice([12, 24, 30, 36])
    i_tot = round(v_par / rp, 2)
    i1 = round(v_par / r1, 2)
    ix = round(v_par / rx, 2)

    prompt = (
        f"A resistor of known resistance **$R_1 = {r1}\\ \\Omega$** is connected in parallel with an unknown resistor **$R_x$** "
        f"across a **${v_par}\\text{{ V}}$** source. The equivalent resistance of the parallel combination is **$R_p = {rp}\\ \\Omega$**.\n\n"
        f"1. Use the parallel resistance formula to calculate the resistance of the unknown resistor **$R_x$**.\n"
        f"2. Calculate the current through $R_1$ and the current through $R_x$ to verify your answer."
    )

    ans_latex = rf"R_x = {rx}\ \Omega; \quad I_1 = {fmt_sa(i1)}\text{{ A}}, \ I_x = {fmt_sa(ix)}\text{{ A}}"
    sample_answer = (
        f"1. $$\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_x}}$$\n"
        f"   $$\\frac{{1}}{{{rp}}} = \\frac{{1}}{{{r1}}} + \\frac{{1}}{{R_x}} \\implies \\frac{{1}}{{R_x}} = \\frac{{1}}{{{rp}}} - \\frac{{1}}{{{r1}}} = \\frac{{1}}{{{rx}}}$$\n"
        f"   $$R_x = {rx}\\ \\Omega$$\n\n"
        f"2. $$I_1 = \\frac{{{v_par}}}{{{r1}}} = {fmt_sa(i1)}\\text{{ A}}, \\quad I_x = \\frac{{{v_par}}}{{{rx}}} = {fmt_sa(ix)}\\text{{ A}}$$\n"
        f"   Total current $I_{{\\text{{total}}}} = {fmt_sa(i1)} + {fmt_sa(ix)} = {fmt_sa(i_tot)}\\text{{ A}} = \\frac{{{v_par}}}{{{rp}}}\\text{{ A}}$."
    )

    return make_payload(
        "18_finding_unknown_parallel_resistor",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Formula 1/Rp = 1/R1 + 1/Rx and rearrangement 1/Rx = 1/Rp - 1/R1", 2),
            (f"Calculate Rx = {rx} Ohm", 1),
            (f"Verify currents I_1 = {fmt_sa(i1)} A and I_x = {fmt_sa(ix)} A", 2),
        ],
        [
            "Rearrange the reciprocal equation: $\\frac{1}{R_x} = \\frac{1}{R_p} - \\frac{1}{R_1}$.",
            f"Compute $\\frac{{1}}{{{rp}}} - \\frac{{1}}{{{r1}}}$, then invert to obtain $R_x$.",
            f"$R_x = {rx}\\ \\Omega$.",
        ],
        ["subtracting_resistances_directly_rx_equals_rp_minus_r1", "forgetting_to_invert_for_rx"],
        ["unknown resistor", "parallel formula", "reciprocal subtraction"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 19: Identical n resistors in series vs parallel
# ---------------------------------------------------------------------------
def arch_19_identical_n_resistors_series_vs_parallel(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    n_res = r.choice([2, 3, 4])
    r_each = r.choice([6, 8, 12, 16, 24])
    r_ser = n_res * r_each
    r_par = round(r_each / n_res, 2)
    ratio = n_res * n_res

    prompt = (
        f"A learner has **${n_res}$ identical resistors**, each of resistance **$R = {r_each}\\ \\Omega$**.\n\n"
        f"1. Calculate the equivalent resistance ($R_s$) when all ${n_res}$ resistors are connected in **series**.\n"
        f"2. Calculate the equivalent resistance ($R_p$) when all ${n_res}$ resistors are connected in **parallel**.\n"
        f"3. Determine the ratio $\\frac{{R_s}}{{R_p}}$."
    )

    ans_latex = rf"R_s = {r_ser}\ \Omega, \ R_p = {fmt_sa(r_par)}\ \Omega, \ \frac{{R_s}}{{R_p}} = {ratio}"
    sample_answer = (
        f"1. For $n = {n_res}$ identical resistors in series:\n"
        f"   $$R_s = n \\cdot R = {n_res} \\times {r_each} = {r_ser}\\ \\Omega$$\n\n"
        f"2. For $n = {n_res}$ identical resistors in parallel:\n"
        f"   $$R_p = \\frac{{R}}{{n}} = \\frac{{{r_each}}}{{{n_res}}} = {fmt_sa(r_par)}\\ \\Omega$$\n\n"
        f"3. $$\\frac{{R_s}}{{R_p}} = \\frac{{{r_ser}}}{{{fmt_sa(r_par)}}} = n^2 = {ratio}$$"
    )

    return make_payload(
        "19_identical_n_resistors_series_vs_parallel",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate series resistance R_s = {r_ser} Ohm", 2),
            (f"Calculate parallel resistance R_p = {fmt_sa(r_par)} Ohm", 2),
            (f"Determine ratio R_s / R_p = {ratio}", 1),
        ],
        [
            "For $n$ identical resistors of resistance $R$: $R_s = nR$ and $R_p = \\frac{R}{n}$.",
            f"Multiply ${r_each}$ by ${n_res}$ for series; divide ${r_each}$ by ${n_res}$ for parallel.",
            f"$R_s = {r_ser}\\ \\Omega$, $R_p = {fmt_sa(r_par)}\\ \\Omega$, ratio $= {ratio}$.",
        ],
        ["confusing_nR_with_R_over_n", "forgetting_identical_resistor_shortcut"],
        ["identical resistors", "series vs parallel", "resistance ratio"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 20: Series-parallel network total resistance (with inline SVG)
# ---------------------------------------------------------------------------
def arch_20_series_parallel_network_total_resistance(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    rs = r.choice([2, 3, 4, 5, 6, 8])
    r1, r2 = r.choice([(6, 3), (12, 4), (12, 6), (20, 5), (15, 30), (8, 8)])
    rp = round((r1 * r2) / (r1 + r2), 2)
    r_tot = round(rs + rp, 2)
    v_tot = round(r.choice([1.5, 2.0, 2.5, 3.0]) * r_tot, 1)

    svg = _svg_composite_circuit(v_tot, rs, r1, r2)

    prompt = (
        f"A composite circuit consists of a series resistor **$R_s = {rs}\\ \\Omega$** connected in series with a parallel bank "
        f"made up of **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$** across a **${fmt_sa(v_tot)}\\text{{ V}}$** battery.\n\n"
        f"1. Calculate the equivalent resistance ($R_p$) of the parallel bank ($R_1 \\parallel R_2$).\n"
        f"2. Calculate the total external resistance ($R_{{\\text{{total}}}}$) of the circuit.\n"
        f"3. Calculate the main-branch current ($I_{{\\text{{total}}}}$) supplied by the battery."
    )

    i_tot = round(v_tot / r_tot, 2)
    ans_latex = rf"R_p = {fmt_sa(rp)}\ \Omega, \ R_{{\text{{total}}}} = {fmt_sa(r_tot)}\ \Omega, \ I_{{\text{{total}}}} = {fmt_sa(i_tot)}\text{{ A}}"
    sample_answer = (
        f"1. $$R_p = \\frac{{R_1 \\cdot R_2}}{{R_1 + R_2}} = \\frac{{{r1} \\times {r2}}}{{{r1} + {r2}}} = {fmt_sa(rp)}\\ \\Omega$$\n\n"
        f"2. $$R_{{\\text{{total}}}} = R_s + R_p = {rs} + {fmt_sa(rp)} = {fmt_sa(r_tot)}\\ \\Omega$$\n\n"
        f"3. $$I_{{\\text{{total}}}} = \\frac{{V_{{\\text{{total}}}}}}{{R_{{\\text{{total}}}}}} = \\frac{{{fmt_sa(v_tot)}}}{{{fmt_sa(r_tot)}}} = {fmt_sa(i_tot)}\\text{{ A}}$$"
    )

    return make_payload(
        "20_series_parallel_network_total_resistance",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate parallel equivalent resistance Rp = {fmt_sa(rp)} Ohm", 2),
            (f"Add series resistor to get R_total = {fmt_sa(r_tot)} Ohm", 1),
            (f"Calculate main current I_total = {fmt_sa(i_tot)} A", 2),
        ],
        [
            "Reduce the parallel bank ($R_1 \\parallel R_2$) to a single equivalent resistance $R_p$ first.",
            f"Add $R_s = {rs}\\ \\Omega$ to $R_p = {fmt_sa(rp)}\\ \\Omega$ to obtain $R_{{\\text{{total}}}}$.",
            f"$R_p = {fmt_sa(rp)}\\ \\Omega$, $R_{{\\text{{total}}}} = {fmt_sa(r_tot)}\\ \\Omega$, $I_{{\\text{{total}}}} = {fmt_sa(i_tot)}\\text{{ A}}$.",
        ],
        ["adding_all_resistors_in_series", "putting_series_resistor_into_parallel_reciprocal_formula"],
        ["series-parallel network", "composite circuit", "equivalent resistance"],
        difficulty="medium",
        diagram_spec={"kind": "inline_svg", "diagram_role": "context", "svg": svg},
    )


# ---------------------------------------------------------------------------
# Subskill 21: Series-parallel full circuit analysis
# ---------------------------------------------------------------------------
def arch_21_series_parallel_full_circuit_analysis(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    rs = r.choice([2, 3, 4, 5])
    r1, r2 = r.choice([(6, 3), (12, 4), (12, 6), (20, 5)])
    rp = int((r1 * r2) // (r1 + r2))
    r_tot = rs + rp
    i_tot = r.choice([1.5, 2.0, 2.5, 3.0])
    v_tot = round(i_tot * r_tot, 1)
    v_s = round(i_tot * rs, 2)
    v_p = round(i_tot * rp, 2)
    i1 = round(v_p / r1, 2)
    i2 = round(v_p / r2, 2)

    prompt = (
        f"A battery of negligible internal resistance supplies **${fmt_sa(v_tot)}\\text{{ V}}$** to a series resistor **$R_s = {rs}\\ \\Omega$** "
        f"connected in series with a parallel combination of **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**.\n\n"
        f"1. Calculate the total resistance ($R_{{\\text{{total}}}}$) of the circuit.\n"
        f"2. Calculate the main-branch current ($I_{{\\text{{total}}}}$).\n"
        f"3. Calculate the potential difference across $R_s$ ($V_s$) and across the parallel bank ($V_p$).\n"
        f"4. Calculate the current $I_1$ through $R_1$ and $I_2$ through $R_2$."
    )

    ans_latex = rf"R_{{\text{{tot}}}} = {r_tot}\ \Omega, \ I_{{\text{{tot}}}} = {fmt_sa(i_tot)}\text{{ A}}, \ V_p = {fmt_sa(v_p)}\text{{ V}}, \ I_1 = {fmt_sa(i1)}\text{{ A}}, \ I_2 = {fmt_sa(i2)}\text{{ A}}"
    sample_answer = (
        f"1. $$R_p = \\frac{{{r1} \\times {r2}}}{{{r1} + {r2}}} = {rp}\\ \\Omega \\implies R_{{\\text{{total}}}} = {rs} + {rp} = {r_tot}\\ \\Omega$$\n\n"
        f"2. $$I_{{\\text{{total}}}} = \\frac{{{fmt_sa(v_tot)}}}{{{r_tot}}} = {fmt_sa(i_tot)}\\text{{ A}}$$\n\n"
        f"3. $$V_s = I_{{\\text{{total}}}} \\cdot R_s = {fmt_sa(i_tot)} \\times {rs} = {fmt_sa(v_s)}\\text{{ V}}$$\n"
        f"   $$V_p = I_{{\\text{{total}}}} \\cdot R_p = {fmt_sa(i_tot)} \\times {rp} = {fmt_sa(v_p)}\\text{{ V}}$$\n\n"
        f"4. $$I_1 = \\frac{{V_p}}{{R_1}} = \\frac{{{fmt_sa(v_p)}}}{{{r1}}} = {fmt_sa(i1)}\\text{{ A}}, \\quad I_2 = \\frac{{V_p}}{{R_2}} = \\frac{{{fmt_sa(v_p)}}}{{{r2}}} = {fmt_sa(i2)}\\text{{ A}}$$"
    )

    return make_payload(
        "21_series_parallel_full_circuit_analysis",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate Rp = {rp} Ohm and R_total = {r_tot} Ohm", 2),
            (f"Calculate I_total = {fmt_sa(i_tot)} A", 1),
            (f"Calculate V_s = {fmt_sa(v_s)} V and V_p = {fmt_sa(v_p)} V", 2),
            (f"Calculate branch currents I_1 = {fmt_sa(i1)} A and I_2 = {fmt_sa(i2)} A", 2),
        ],
        [
            "Find $R_p$, then $R_{\\text{total}} = R_s + R_p$, and use $I_{\\text{total}} = V_{\\text{total}} / R_{\\text{total}}$.",
            f"The parallel voltage is $V_p = V_{{\\text{{total}}}} - V_s = {fmt_sa(v_p)}\\text{{ V}}$. Use $V_p$ (not $V_{{\\text{{total}}}}$) to find $I_1$ and $I_2$.",
            f"$R_{{\\text{{tot}}}} = {r_tot}\\ \\Omega$, $I_{{\\text{{tot}}}} = {fmt_sa(i_tot)}\\text{{ A}}$, $V_p = {fmt_sa(v_p)}\\text{{ V}}$, $I_1 = {fmt_sa(i1)}\\text{{ A}}$, $I_2 = {fmt_sa(i2)}\\text{{ A}}$.",
        ],
        ["using_battery_voltage_instead_of_vp_for_branch_currents", "inverted_parallel_resistance_formula"],
        ["full circuit analysis", "branch current", "parallel voltage"],
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Subskill 22: Working backwards from branch ammeter reading
# ---------------------------------------------------------------------------
def arch_22_working_backwards_from_branch_ammeter(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r1, r2 = r.choice([(4, 8), (6, 12), (5, 10), (8, 16), (6, 18), (4, 12)])
    i1 = r.choice([1.5, 2.0, 2.4, 3.0])
    v_p = round(i1 * r1, 2)
    i2 = round(v_p / r2, 2)
    i_tot = round(i1 + i2, 2)
    rs = r.choice([2, 3, 4, 5])
    v_s = round(i_tot * rs, 2)
    v_bat = round(v_p + v_s, 2)

    prompt = (
        f"In a composite circuit, a resistor **$R_s = {rs}\\ \\Omega$** is in series with a parallel combination of **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**.\n"
        f"An ammeter in the $R_1$ branch reads **$I_1 = {fmt_sa(i1)}\\text{{ A}}$**.\n\n"
        f"1. Calculate the potential difference ($V_p$) across the parallel combination.\n"
        f"2. Calculate the current ($I_2$) flowing through resistor $R_2$.\n"
        f"3. Calculate the total current ($I_{{\\text{{total}}}}$) in the main branch.\n"
        f"4. Calculate the terminal potential difference ($V_{{\\text{{battery}}}}$) of the supply."
    )

    ans_latex = rf"V_p = {fmt_sa(v_p)}\text{{ V}}, \ I_2 = {fmt_sa(i2)}\text{{ A}}, \ I_{{\text{{total}}}} = {fmt_sa(i_tot)}\text{{ A}}, \ V_{{\text{{battery}}}} = {fmt_sa(v_bat)}\text{{ V}}"
    sample_answer = (
        f"1. $$V_p = I_1 \\cdot R_1 = {fmt_sa(i1)} \\times {r1} = {fmt_sa(v_p)}\\text{{ V}}$$\n\n"
        f"2. Since $R_1$ and $R_2$ are in parallel, $V_2 = V_p = {fmt_sa(v_p)}\\text{{ V}}$:\n"
        f"   $$I_2 = \\frac{{V_p}}{{R_2}} = \\frac{{{fmt_sa(v_p)}}}{{{r2}}} = {fmt_sa(i2)}\\text{{ A}}$$\n\n"
        f"3. $$I_{{\\text{{total}}}} = I_1 + I_2 = {fmt_sa(i1)} + {fmt_sa(i2)} = {fmt_sa(i_tot)}\\text{{ A}}$$\n\n"
        f"4. $$V_s = I_{{\\text{{total}}}} \\cdot R_s = {fmt_sa(i_tot)} \\times {rs} = {fmt_sa(v_s)}\\text{{ V}}$$\n"
        f"   $$V_{{\\text{{battery}}}} = V_s + V_p = {fmt_sa(v_s)} + {fmt_sa(v_p)} = {fmt_sa(v_bat)}\\text{{ V}}$$"
    )

    return make_payload(
        "22_working_backwards_from_branch_ammeter",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate Vp = I1 * R1 = {fmt_sa(v_p)} V", 2),
            (f"Calculate I2 = Vp / R2 = {fmt_sa(i2)} A", 1),
            (f"Calculate I_total = I1 + I2 = {fmt_sa(i_tot)} A", 1),
            (f"Calculate V_battery = V_s + V_p = {fmt_sa(v_bat)} V", 2),
        ],
        [
            "Start with the branch where both $I_1$ and $R_1$ are known: $V_p = I_1 R_1$.",
            f"Use $V_p = {fmt_sa(v_p)}\\text{{ V}}$ to find $I_2 = V_p / R_2$, then add $I_1 + I_2$ to get $I_{{\\text{{total}}}}$.",
            f"$V_p = {fmt_sa(v_p)}\\text{{ V}}$, $I_2 = {fmt_sa(i2)}\\text{{ A}}$, $I_{{\\text{{total}}}} = {fmt_sa(i_tot)}\\text{{ A}}$, $V_{{\\text{{battery}}}} = {fmt_sa(v_bat)}\\text{{ V}}$.",
        ],
        ["using_branch_current_as_total_series_current", "forgetting_voltage_across_series_resistor"],
        ["working backwards", "branch ammeter", "parallel voltage"],
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Subskill 23: Working backwards from branch voltmeter reading
# ---------------------------------------------------------------------------
def arch_23_working_backwards_from_branch_voltmeter(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    rs = r.choice([3, 4, 5, 6])
    r1, r2 = r.choice([(6, 3), (12, 4), (12, 6), (20, 5)])
    rp = int((r1 * r2) // (r1 + r2))
    i_tot = r.choice([1.5, 2.0, 2.5, 3.0, 4.0])
    v_s = round(i_tot * rs, 2)
    v_p = round(i_tot * rp, 2)
    v_tot = round(v_s + v_p, 2)
    i1 = round(v_p / r1, 2)

    prompt = (
        f"A series resistor **$R_s = {rs}\\ \\Omega$** is connected in series with a parallel bank (**$R_1 = {r1}\\ \\Omega$** in parallel with **$R_2 = {r2}\\ \\Omega$**).\n"
        f"A voltmeter connected across $R_s$ reads **$V_s = {fmt_sa(v_s)}\\text{{ V}}$**.\n\n"
        f"1. Calculate the total current ($I_{{\\text{{total}}}}$) flowing through $R_s$.\n"
        f"2. Calculate the equivalent resistance ($R_p$) of the parallel bank.\n"
        f"3. Calculate the potential difference ($V_p$) across the parallel bank and the total supply voltage ($V_{{\\text{{supply}}}}$).\n"
        f"4. Calculate the current ($I_1$) flowing through $R_1$."
    )

    ans_latex = rf"I_{{\text{{tot}}}} = {fmt_sa(i_tot)}\text{{ A}}, \ R_p = {rp}\ \Omega, \ V_p = {fmt_sa(v_p)}\text{{ V}}, \ V_{{\text{{supply}}}} = {fmt_sa(v_tot)}\text{{ V}}, \ I_1 = {fmt_sa(i1)}\text{{ A}}"
    sample_answer = (
        f"1. $$I_{{\\text{{total}}}} = \\frac{{V_s}}{{R_s}} = \\frac{{{fmt_sa(v_s)}}}{{{rs}}} = {fmt_sa(i_tot)}\\text{{ A}}$$\n\n"
        f"2. $$R_p = \\frac{{{r1} \\times {r2}}}{{{r1} + {r2}}} = {rp}\\ \\Omega$$\n\n"
        f"3. $$V_p = I_{{\\text{{total}}}} \\cdot R_p = {fmt_sa(i_tot)} \\times {rp} = {fmt_sa(v_p)}\\text{{ V}}$$\n"
        f"   $$V_{{\\text{{supply}}}} = V_s + V_p = {fmt_sa(v_s)} + {fmt_sa(v_p)} = {fmt_sa(v_tot)}\\text{{ V}}$$\n\n"
        f"4. $$I_1 = \\frac{{V_p}}{{R_1}} = \\frac{{{fmt_sa(v_p)}}}{{{r1}}} = {fmt_sa(i1)}\\text{{ A}}$$"
    )

    return make_payload(
        "23_working_backwards_from_branch_voltmeter",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate I_total = V_s / R_s = {fmt_sa(i_tot)} A", 2),
            (f"Calculate Rp = {rp} Ohm", 1),
            (f"Calculate V_p = {fmt_sa(v_p)} V and V_supply = {fmt_sa(v_tot)} V", 2),
            (f"Calculate I_1 = {fmt_sa(i1)} A", 1),
        ],
        [
            "Apply Ohm's Law directly to $R_s$ to find the main current: $I_{\\text{total}} = \\frac{V_s}{R_s}$.",
            f"Multiply $I_{{\\text{{total}}}} = {fmt_sa(i_tot)}\\text{{ A}}$ by $R_p = {rp}\\ \\Omega$ to find $V_p$.",
            f"$I_{{\\text{{total}}}} = {fmt_sa(i_tot)}\\text{{ A}}$, $V_p = {fmt_sa(v_p)}\\text{{ V}}$, $V_{{\\text{{supply}}}} = {fmt_sa(v_tot)}\\text{{ V}}$, $I_1 = {fmt_sa(i1)}\\text{{ A}}$.",
        ],
        ["assuming_vs_equals_vp", "dividing_vs_by_r1_to_find_i1"],
        ["working backwards", "series voltmeter", "composite network"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 24: Switch opening/closing in a parallel branch effect
# ---------------------------------------------------------------------------
def arch_24_switch_opening_closing_parallel_branch_effect(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    rs = r.choice([2, 3, 4])
    r1, r2 = r.choice([(6, 6), (12, 4), (12, 6), (8, 8)])
    rp = int((r1 * r2) // (r1 + r2))
    r_open = rs + r1
    r_closed = rs + rp
    v_supply = r.choice([18, 24, 30, 36])
    i_open = round(v_supply / r_open, 2)
    i_closed = round(v_supply / r_closed, 2)

    prompt = (
        f"A circuit with a constant **${v_supply}\\text{{ V}}$** supply has a series resistor **$R_s = {rs}\\ \\Omega$** connected to "
        f"two parallel branches: branch 1 contains **$R_1 = {r1}\\ \\Omega$**, and branch 2 contains **$R_2 = {r2}\\ \\Omega$** in series with switch **$S$**.\n\n"
        f"1. With switch $S$ **open**, calculate the total resistance ($R_{{\\text{{open}}}}$) and main ammeter reading ($I_{{\\text{{open}}}}$).\n"
        f"2. Switch $S$ is now **closed**. Calculate the new total resistance ($R_{{\\text{{closed}}}}$) and new main ammeter reading ($I_{{\\text{{closed}}}}$).\n"
        f"3. State whether the voltmeter reading across $R_s$ **increases, decreases, or remains the same** when switch $S$ is closed. Explain briefly."
    )

    ans_latex = rf"I_{{\text{{open}}}} = {fmt_sa(i_open)}\text{{ A}}, \ I_{{\text{{closed}}}} = {fmt_sa(i_closed)}\text{{ A}}; \ \text{{V across }} R_s \text{{ INCREASES}}"
    sample_answer = (
        f"1. With $S$ open, no current flows through $R_2$:\n"
        f"   $$R_{{\\text{{open}}}} = R_s + R_1 = {rs} + {r1} = {r_open}\\ \\Omega$$\n"
        f"   $$I_{{\\text{{open}}}} = \\frac{{{v_supply}}}{{{r_open}}} = {fmt_sa(i_open)}\\text{{ A}}$$\n\n"
        f"2. With $S$ closed, $R_1$ and $R_2$ are in parallel ($R_p = \\frac{{{r1} \\times {r2}}}{{{r1} + {r2}}} = {rp}\\ \\Omega$):\n"
        f"   $$R_{{\\text{{closed}}}} = R_s + R_p = {rs} + {rp} = {r_closed}\\ \\Omega$$\n"
        f"   $$I_{{\\text{{closed}}}} = \\frac{{{v_supply}}}{{{r_closed}}} = {fmt_sa(i_closed)}\\text{{ A}}$$\n\n"
        f"3. **Increases.** Closing $S$ adds a resistor in parallel, which **decreases total resistance**, causing the **main current $I$ to increase**. "
        f"Since $V_s = I \\cdot R_s$ and $R_s$ is constant, $V_s$ increases."
    )

    return make_payload(
        "24_switch_opening_closing_parallel_branch_effect",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate R_open = {r_open} Ohm and I_open = {fmt_sa(i_open)} A", 2),
            (f"Calculate R_closed = {r_closed} Ohm and I_closed = {fmt_sa(i_closed)} A", 2),
            ("State V_s INCREASES and explain (R_total decreases -> I_main increases -> V_s = I*Rs increases)", 2),
        ],
        [
            "When switch $S$ in branch 2 is open, branch 2 is disconnected and only $R_s$ and $R_1$ are in series.",
            "When $S$ closes, $R_2$ is connected in parallel with $R_1$, lowering the equivalent resistance of the circuit.",
            f"$I_{{\\text{{open}}}} = {fmt_sa(i_open)}\\text{{ A}}$, $I_{{\\text{{closed}}}} = {fmt_sa(i_closed)}\\text{{ A}}$, and $V_s$ increases.",
        ],
        ["thinking_adding_resistor_in_parallel_increases_total_resistance", "including_open_branch_in_parallel_calculation"],
        ["switch toggling", "parallel branch", "circuit resistance change"],
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Subskill 25: Short-circuit bypass analysis
# ---------------------------------------------------------------------------
def arch_25_short_circuit_bypass_analysis(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r1 = r.choice([4, 6, 8, 10])
    r2 = r.choice([6, 8, 10, 12])
    v_supply = r.choice([12, 18, 24, 30, 36])
    i_before = round(v_supply / (r1 + r2), 2)
    i_after = round(v_supply / r1, 2)

    prompt = (
        f"Two resistors, **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**, are connected in series with a **${v_supply}\\text{{ V}}$** battery of negligible internal resistance.\n"
        f"A conducting wire of negligible resistance ($0\\ \\Omega$) containing an open switch **$S$** is connected in parallel across **$R_2$**.\n\n"
        f"1. Calculate the ammeter reading in the main circuit while switch $S$ is **open**.\n"
        f"2. Switch $S$ is now **closed**, creating a short circuit across $R_2$. State the current through $R_2$ and the potential difference across $R_2$.\n"
        f"3. Calculate the new ammeter reading in the main circuit when $S$ is closed."
    )

    ans_latex = rf"I_{{\text{{open}}}} = {fmt_sa(i_before)}\text{{ A}}, \ I_{{R_2}} = 0\text{{ A}}, \ I_{{\text{{closed}}}} = {fmt_sa(i_after)}\text{{ A}}"
    sample_answer = (
        f"1. With $S$ open, $R_1$ and $R_2$ are in series:\n"
        f"   $$I_{{\\text{{open}}}} = \\frac{{V}}{{R_1 + R_2}} = \\frac{{{v_supply}}}{{{r1 + r2}}} = {fmt_sa(i_before)}\\text{{ A}}$$\n\n"
        f"2. When $S$ is closed, the $0\\ \\Omega$ wire bypasses $R_2$ completely (short-circuits $R_2$). "
        f"Therefore, **$I_{{R_2}} = 0\\text{{ A}}$** and **$V_{{R_2}} = 0\\text{{ V}}$**.\n\n"
        f"3. Only $R_1 = {r1}\\ \\Omega$ remains active in the circuit:\n"
        f"   $$I_{{\\text{{closed}}}} = \\frac{{V}}{{R_1}} = \\frac{{{v_supply}}}{{{r1}}} = {fmt_sa(i_after)}\\text{{ A}}$$"
    )

    return make_payload(
        "25_short_circuit_bypass_analysis",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate I_open = {fmt_sa(i_before)} A", 2),
            ("State I_R2 = 0 A and V_R2 = 0 V due to short-circuit bypass", 2),
            (f"Calculate I_closed = {fmt_sa(i_after)} A", 2),
        ],
        [
            "A closed switch in a wire of zero resistance connected in parallel across a resistor creates a short circuit across that resistor.",
            f"All current takes the zero-resistance path around $R_2$, so $R_2$ is bypassed and only $R_1 = {r1}\\ \\Omega$ limits the current.",
            f"$I_{{\\text{{open}}}} = {fmt_sa(i_before)}\\text{{ A}}$, $I_{{R_2}} = 0\\text{{ A}}$, $I_{{\\text{{closed}}}} = {fmt_sa(i_after)}\\text{{ A}}$.",
        ],
        ["assuming_current_still_flows_through_shorted_resistor", "keeping_r2_in_total_resistance_when_shorted"],
        ["short circuit", "bypass wire", "zero resistance"],
        difficulty="medium",
    )


BUILDERS_01_25: Dict[str, Callable[[Optional[int]], Dict[str, Any]]] = {
    "01_potential_difference_work_per_charge": arch_01_potential_difference_work_per_charge,
    "02_electric_current_rate_of_charge_flow": arch_02_electric_current_rate_of_charge_flow,
    "03_electron_quantization_and_current": arch_03_electron_quantization_and_current,
    "04_voltmeter_and_ammeter_connections": arch_04_voltmeter_and_ammeter_connections,
    "05_ohms_law_statement_and_conditions": arch_05_ohms_law_statement_and_conditions,
    "06_ohmic_vs_non_ohmic_conductors": arch_06_ohmic_vs_non_ohmic_conductors,
    "07_iv_characteristic_graph_gradient_analysis": arch_07_iv_characteristic_graph_gradient_analysis,
    "08_comparing_two_resistors_on_iv_axes": arch_08_comparing_two_resistors_on_iv_axes,
    "09_experimental_verification_of_ohms_law": arch_09_experimental_verification_of_ohms_law,
    "10_emf_vs_terminal_potential_difference": arch_10_emf_vs_terminal_potential_difference,
    "11_internal_resistance_single_load_calculation": arch_11_internal_resistance_single_load_calculation,
    "12_internal_resistance_dual_switch_readings": arch_12_internal_resistance_dual_switch_readings,
    "13_series_resistors_equivalent_and_current": arch_13_series_resistors_equivalent_and_current,
    "14_series_potential_divider_ratios": arch_14_series_potential_divider_ratios,
    "15_parallel_two_resistors_product_over_sum": arch_15_parallel_two_resistors_product_over_sum,
    "16_parallel_three_or_four_resistors": arch_16_parallel_three_or_four_resistors,
    "17_parallel_current_divider_branch_currents": arch_17_parallel_current_divider_branch_currents,
    "18_finding_unknown_parallel_resistor": arch_18_finding_unknown_parallel_resistor,
    "19_identical_n_resistors_series_vs_parallel": arch_19_identical_n_resistors_series_vs_parallel,
    "20_series_parallel_network_total_resistance": arch_20_series_parallel_network_total_resistance,
    "21_series_parallel_full_circuit_analysis": arch_21_series_parallel_full_circuit_analysis,
    "22_working_backwards_from_branch_ammeter": arch_22_working_backwards_from_branch_ammeter,
    "23_working_backwards_from_branch_voltmeter": arch_23_working_backwards_from_branch_voltmeter,
    "24_switch_opening_closing_parallel_branch_effect": arch_24_switch_opening_closing_parallel_branch_effect,
    "25_short_circuit_bypass_analysis": arch_25_short_circuit_bypass_analysis,
}
