"""Grade 12 Physical Sciences — Momentum and Impulse: Archetypes 01 to 25.
Ground truth curriculum:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 1/01. Momentum and Impulse.md

Covers:
- 01–08: Definition & vector nature of momentum, p = mv calculations, unit conversions, p vs Ek relations.
- 09–13: Change in momentum (Delta p = m(vf - vi)), 1D speed increase, braking, rebounds, vertical bounce, vector diagrams.
- 14–20: Newton's Second Law in terms of momentum (F_net = Delta p / Delta t), impulse definition, J = F_net * Delta t = Delta p.
- 21–24: Force-time (F-t) graphs (rectangular, triangular, trapezoidal, direction reversal) with seed-varied inline SVGs.
- 25: Momentum & impulse foundations diagnostic autopsy.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _fmt(val: float | int, decimals: int = 2) -> str:
    """Format numeric values with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    rounded = round(float(val), decimals)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _svg_momentum_vectors(pi: float, pf: float, dp: float) -> str:
    """Dynamic SVG showing initial, final, and change in momentum vectors for a 1D rebound."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 220" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Momentum Vector Diagram (Rebound)</text>'
        f'<text x="35" y="65" font-size="10" font-weight="bold" fill="#2563eb">p_i = +{_fmt(pi)} kg·m·s⁻¹ (Towards wall)</text>'
        f'<line x1="60" y1="80" x2="260" y2="80" stroke="#2563eb" stroke-width="3"/>'
        f'<polygon points="268,80 256,74 256,86" fill="#2563eb"/>'
        f'<text x="35" y="120" font-size="10" font-weight="bold" fill="#dc2626">p_f = -{_fmt(pf)} kg·m·s⁻¹ (Away from wall)</text>'
        f'<line x1="260" y1="135" x2="110" y2="135" stroke="#dc2626" stroke-width="3"/>'
        f'<polygon points="102,135 114,129 114,141" fill="#dc2626"/>'
        f'<text x="35" y="175" font-size="10" font-weight="bold" fill="#16a34a">Δp = p_f - p_i = -{_fmt(dp)} kg·m·s⁻¹</text>'
        f'<line x1="330" y1="190" x2="60" y2="190" stroke="#16a34a" stroke-width="3.5" stroke-dasharray="5,3"/>'
        f'<polygon points="52,190 64,184 64,196" fill="#16a34a"/>'
        f'</svg>'
    )


def _svg_ft_rect(f_max: float, dt: float) -> str:
    """Dynamic SVG for a rectangular Force-time graph."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 240" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Force vs Time Graph (Rectangular)</text>'
        f'<line x1="60" y1="35" x2="60" y2="195" stroke="#334155" stroke-width="2"/>'
        f'<line x1="60" y1="195" x2="345" y2="195" stroke="#334155" stroke-width="2"/>'
        f'<rect x="60" y="75" width="210" height="120" fill="#93c5fd" fill-opacity="0.45" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="52" y="80" text-anchor="end" font-size="10" font-weight="bold" fill="#1e40af">{_fmt(f_max)}</text>'
        f'<text x="60" y="212" text-anchor="middle" font-size="10" fill="#334155">0</text>'
        f'<text x="270" y="212" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e40af">{_fmt(dt)}</text>'
        f'<text x="335" y="215" font-size="10" font-weight="bold" fill="#334155">t (s)</text>'
        f'<text x="22" y="115" font-size="10" font-weight="bold" fill="#334155" transform="rotate(-90 22,115)">F (N)</text>'
        f'<text x="165" y="140" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e3a8a">Area = Impulse</text>'
        f'</svg>'
    )


def _svg_ft_triangle(f_peak: float, t_end: float) -> str:
    """Dynamic SVG for a triangular Force-time graph."""
    t_mid = round(t_end / 2.0, 3)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 240" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Force vs Time Graph (Collision Impact)</text>'
        f'<line x1="60" y1="35" x2="60" y2="195" stroke="#334155" stroke-width="2"/>'
        f'<line x1="60" y1="195" x2="345" y2="195" stroke="#334155" stroke-width="2"/>'
        f'<polygon points="60,195 170,60 280,195" fill="#fde68a" fill-opacity="0.5" stroke="#d97706" stroke-width="2.5"/>'
        f'<line x1="60" y1="60" x2="170" y2="60" stroke="#94a3b8" stroke-dasharray="4,4"/>'
        f'<line x1="170" y1="60" x2="170" y2="195" stroke="#94a3b8" stroke-dasharray="4,4"/>'
        f'<text x="52" y="64" text-anchor="end" font-size="10" font-weight="bold" fill="#b45309">{_fmt(f_peak)}</text>'
        f'<text x="60" y="212" text-anchor="middle" font-size="10" fill="#334155">0</text>'
        f'<text x="170" y="212" text-anchor="middle" font-size="10" fill="#475569">{_fmt(t_mid, 3)}</text>'
        f'<text x="280" y="212" text-anchor="middle" font-size="10" font-weight="bold" fill="#b45309">{_fmt(t_end, 3)}</text>'
        f'<text x="335" y="215" font-size="10" font-weight="bold" fill="#334155">t (s)</text>'
        f'<text x="22" y="115" font-size="10" font-weight="bold" fill="#334155" transform="rotate(-90 22,115)">F (N)</text>'
        f'</svg>'
    )


def _svg_ft_trapezoid(f_const: float, t1: float, t2: float, t3: float) -> str:
    """Dynamic SVG for a trapezoidal Force-time profile."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 240" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Force vs Time Graph (Trapezoidal Thrust)</text>'
        f'<line x1="55" y1="35" x2="55" y2="195" stroke="#334155" stroke-width="2"/>'
        f'<line x1="55" y1="195" x2="350" y2="195" stroke="#334155" stroke-width="2"/>'
        f'<polygon points="55,195 120,70 235,70 300,195" fill="#bbf7d0" fill-opacity="0.45" stroke="#15803d" stroke-width="2.5"/>'
        f'<line x1="55" y1="70" x2="120" y2="70" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<line x1="120" y1="70" x2="120" y2="195" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<line x1="235" y1="70" x2="235" y2="195" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<text x="48" y="74" text-anchor="end" font-size="10" font-weight="bold" fill="#166534">{_fmt(f_const)}</text>'
        f'<text x="55" y="212" text-anchor="middle" font-size="9" fill="#334155">0</text>'
        f'<text x="120" y="212" text-anchor="middle" font-size="9" font-weight="bold" fill="#166534">{_fmt(t1)}</text>'
        f'<text x="235" y="212" text-anchor="middle" font-size="9" font-weight="bold" fill="#166534">{_fmt(t2)}</text>'
        f'<text x="300" y="212" text-anchor="middle" font-size="9" font-weight="bold" fill="#166534">{_fmt(t3)}</text>'
        f'<text x="340" y="212" font-size="10" font-weight="bold" fill="#334155">t (s)</text>'
        f'<text x="20" y="115" font-size="10" font-weight="bold" fill="#334155" transform="rotate(-90 20,115)">F (N)</text>'
        f'</svg>'
    )


def _svg_ft_bidirectional(f_pos: float, f_neg: float, t1: float, t2: float) -> str:
    """Dynamic SVG for a Force-time graph with positive propulsion and negative braking force."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 250" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">Force vs Time Graph (Forward &amp; Reverse Impulse)</text>'
        f'<line x1="60" y1="30" x2="60" y2="225" stroke="#334155" stroke-width="2"/>'
        f'<line x1="60" y1="125" x2="345" y2="125" stroke="#334155" stroke-width="2"/>'
        f'<rect x="60" y="55" width="120" height="70" fill="#bfdbfe" fill-opacity="0.55" stroke="#2563eb" stroke-width="2"/>'
        f'<rect x="180" y="125" width="110" height="70" fill="#fecaca" fill-opacity="0.55" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="52" y="60" text-anchor="end" font-size="9" font-weight="bold" fill="#1d4ed8">+{_fmt(f_pos)}</text>'
        f'<text x="52" y="128" text-anchor="end" font-size="9" fill="#334155">0</text>'
        f'<text x="52" y="198" text-anchor="end" font-size="9" font-weight="bold" fill="#b91c1c">-{_fmt(f_neg)}</text>'
        f'<text x="172" y="140" font-size="9" font-weight="bold" fill="#1e293b">{_fmt(t1)}</text>'
        f'<text x="292" y="118" font-size="9" font-weight="bold" fill="#1e293b">{_fmt(t2)}</text>'
        f'<text x="335" y="142" font-size="10" font-weight="bold" fill="#334155">t (s)</text>'
        f'<text x="20" y="130" font-size="10" font-weight="bold" fill="#334155" transform="rotate(-90 20,130)">F (N)</text>'
        f'</svg>'
    )


def _make_q(
    r: random.Random,
    subskill: str,
    idx: int,
    prompt: str,
    correct_answer: str,
    solution_text: str,
    marks: int,
    tags: List[str],
    rubric: List[Dict[str, Any]],
    hints: Dict[str, str],
    svg: Optional[str] = None,
) -> Dict[str, Any]:
    q_id = f"g12_mom_{idx:02d}_{r.randint(100000, 999999)}"
    marking_points = [
        {
            "id": f"mp_{i + 1}",
            "desc": item.get("criterion", f"Step {i + 1}"),
            "marks": item.get("marks", 1),
            "editable": True,
        }
        for i, item in enumerate(rubric)
    ]
    out: Dict[str, Any] = {
        "id": q_id,
        "topic": "Momentum and Impulse",
        "subskill": subskill,
        "archetype_id": subskill,
        "question_type": "numeric_input",
        "modality": "physics_calculation",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": correct_answer,
        "ideal_answer": correct_answer,
        "sample_answer": solution_text,
        "solution": solution_text,
        "explanation": solution_text,
        "marks": marks,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "learning_objective_id": f"g12_mom_{subskill}",
        "mode": subskill,
        "misconception_tags": tags,
        "rubric": rubric,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
    }
    if svg:
        out["diagram_spec"] = {
            "kind": "inline_svg",
            "svg": svg,
            "width": 380,
            "height": 240,
        }
    return out


# 01. Definition and vector nature of momentum
def build_01_definition_and_vector_nature_of_momentum(r: random.Random) -> Dict[str, Any]:
    obj, m, v, d = r.choice([
        ("minibus taxi", 2200, 20, "east"),
        ("freight locomotive", 45000, 12, "north"),
        ("sprinter", 75, 9.5, "west"),
        ("delivery van", 1800, 15, "south"),
    ])
    p = round(m * v, 1)
    prompt = (
        f"A {obj} of mass ${m}\\text{{ kg}}$ travels at a constant velocity of ${_fmt(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ {d}.\n\n"
        f"1. Define the term **momentum** in words.\n"
        f"2. State whether momentum is a vector or a scalar quantity, and give the SI unit of momentum.\n"
        f"3. State the direction of the momentum of the {obj}."
    )
    ans = f"Product of mass and velocity; Vector; kg·m·s⁻¹; {d}"
    sol = (
        f"1. **Momentum** is the product of the mass and velocity of an object ($\\vec{{p}} = m\\vec{{v}}$).\n"
        f"2. Momentum is a **vector** quantity with SI unit $\\text{{kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"3. The direction of momentum is always the same as the direction of the velocity: **{d}** (with magnitude ${_fmt(p)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$)."
    )
    return _make_q(
        r, "01_definition_and_vector_nature_of_momentum", 1, prompt, ans, sol, 3,
        ["treated_momentum_as_scalar", "used_newton_as_unit_of_momentum"],
        [{"step": 1, "criterion": "Definition: product of mass and velocity", "marks": 1}, {"step": 2, "criterion": "Vector quantity with unit kg·m·s⁻¹", "marks": 1}, {"step": 3, "criterion": f"Direction: {d}", "marks": 1}],
        {"tier_1": "Recall the formula p = mv.", "tier_2": "Since velocity is a vector and mass is a positive scalar, momentum shares the direction of velocity.", "tier_3": ans},
    )


# 02. Linear momentum direct calculation
def build_02_linear_momentum_direct_calculation(r: random.Random) -> Dict[str, Any]:
    item, m, v, d = r.choice([
        ("rugby forward", 105, 7.5, "east"),
        ("motorcar", 1250, 22.0, "north"),
        ("cheetah", 55, 26.0, "west"),
        ("cyclist", 82, 11.5, "south"),
        ("bowling ball", 6.5, 8.0, "to the right"),
    ])
    p = round(m * v, 2)
    prompt = (
        f"A {item} of mass ${_fmt(m)}\\text{{ kg}}$ is moving at ${_fmt(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ {d}.\n\n"
        f"Calculate the linear momentum of the {item} (include both magnitude and direction)."
    )
    ans = f"{_fmt(p)} kg·m·s⁻¹ {d}"
    sol = (
        f"$$p = m v = ({_fmt(m)})({_fmt(v)}) = {_fmt(p)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}\\text{{ {d}}}$$"
    )
    return _make_q(
        r, "02_linear_momentum_direct_calculation", 2, prompt, ans, sol, 3,
        ["omitted_vector_direction", "used_kinetic_energy_formula_instead_of_momentum"],
        [{"step": 1, "criterion": "Formula p = mv", "marks": 1}, {"step": 2, "criterion": f"Substitution ({_fmt(m)})({_fmt(v)})", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(p)} kg·m·s⁻¹ {d}", "marks": 1}],
        {"tier_1": "Use the linear momentum formula p = m * v.", "tier_2": "Multiply mass in kg by velocity in m/s and state the direction.", "tier_3": ans},
    )


# 03. Linear momentum with gram to kg conversion
def build_03_linear_momentum_with_gram_to_kg_conversion(r: random.Random) -> Dict[str, Any]:
    item, m_g, v, d = r.choice([
        ("cricket ball", 156, 35.0, "towards the boundary"),
        ("tennis ball", 58, 45.0, "across the net"),
        ("golf ball", 45, 60.0, "down the fairway"),
        ("hockey ball", 160, 28.0, "towards the goal"),
        ("bullet", 25, 420.0, "east"),
    ])
    m_kg = m_g / 1000.0
    p = round(m_kg * v, 3)
    prompt = (
        f"A {item} of mass ${m_g}\\text{{ g}}$ travels at a velocity of ${_fmt(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ {d}.\n\n"
        f"1. Convert the mass of the {item} to kilograms.\n"
        f"2. Calculate the magnitude and direction of the momentum of the {item}."
    )
    ans = f"{_fmt(p, 3)} kg·m·s⁻¹ {d}"
    sol = (
        f"1. $m = \\frac{{{m_g}}}{{1000}} = {_fmt(m_kg, 3)}\\text{{ kg}}$.\n"
        f"2. $p = m v = ({_fmt(m_kg, 3)})({_fmt(v)}) = {_fmt(p, 3)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ {d}."
    )
    return _make_q(
        r, "03_linear_momentum_with_gram_to_kg_conversion", 3, prompt, ans, sol, 3,
        ["forgot_to_convert_grams_to_kg"],
        [{"step": 1, "criterion": f"Convert mass to {_fmt(m_kg, 3)} kg", "marks": 1}, {"step": 2, "criterion": "Formula p = mv and substitution", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(p, 3)} kg·m·s⁻¹ {d}", "marks": 1}],
        {"tier_1": "Divide mass in grams by 1000 to get kilograms.", "tier_2": f"p = {_fmt(m_kg, 3)} * {_fmt(v)}.", "tier_3": ans},
    )


# 04. Linear momentum with km/h to m/s conversion
def build_04_linear_momentum_with_kmh_to_ms_conversion(r: random.Random) -> Dict[str, Any]:
    m = r.choice([1000, 1200, 1500, 1800, 2400])
    v_kmh = r.choice([54, 72, 90, 108, 126])
    v_ms = v_kmh / 3.6
    d = r.choice(["north", "south", "east", "west"])
    p = round(m * v_ms, 1)
    prompt = (
        f"A sedan of mass ${m}\\text{{ kg}}$ is cruising at ${v_kmh}\\text{{ km}}\\cdot\\text{{h}}^{{-1}}$ {d} along a national highway.\n\n"
        f"1. Convert the speed from $\\text{{km}}\\cdot\\text{{h}}^{{-1}}$ to $\\text{{m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"2. Calculate the momentum of the sedan."
    )
    ans = f"{_fmt(p)} kg·m·s⁻¹ {d}"
    sol = (
        f"1. $v = \\frac{{{v_kmh}}}{{3{{,}}6}} = {_fmt(v_ms)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"2. $p = m v = ({m})({_fmt(v_ms)}) = {_fmt(p)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ {d}."
    )
    return _make_q(
        r, "04_linear_momentum_with_kmh_to_ms_conversion", 4, prompt, ans, sol, 3,
        ["multiplied_by_3_6_instead_of_dividing"],
        [{"step": 1, "criterion": f"Convert speed to {_fmt(v_ms)} m·s⁻¹", "marks": 1}, {"step": 2, "criterion": "Formula p = mv and substitution", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(p)} kg·m·s⁻¹ {d}", "marks": 1}],
        {"tier_1": "Divide speed in km/h by 3,6 to convert to m/s.", "tier_2": f"v = {_fmt(v_ms)} m/s, then p = m * v.", "tier_3": ans},
    )


# 05. Solving for mass or velocity from momentum
def build_05_solving_for_mass_or_velocity_from_momentum(r: random.Random) -> Dict[str, Any]:
    solve_for = r.choice(["velocity", "mass"])
    m = r.choice([80, 120, 400, 1500])
    v = r.choice([6.0, 12.0, 15.0, 25.0])
    p = round(m * v, 1)
    if solve_for == "velocity":
        prompt = (
            f"An object of mass ${m}\\text{{ kg}}$ has a linear momentum of magnitude ${_fmt(p)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ east.\n\n"
            f"Calculate the velocity of the object."
        )
        ans = f"{_fmt(v)} m·s⁻¹ east"
        sol = f"$$v = \\frac{{p}}{{m}} = \\frac{{{_fmt(p)}}}{{{m}}} = {_fmt(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ east}}$$"
    else:
        prompt = (
            f"A moving trolley travelling at ${_fmt(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ north has a momentum of magnitude ${_fmt(p)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
            f"Calculate the mass of the trolley."
        )
        ans = f"{_fmt(m)} kg"
        sol = f"$$m = \\frac{{p}}{{v}} = \\frac{{{_fmt(p)}}}{{{_fmt(v)}}} = {_fmt(m)}\\text{{ kg}}$$"
    return _make_q(
        r, "05_solving_for_mass_or_velocity_from_momentum", 5, prompt, ans, sol, 2,
        ["inverted_division_when_rearranging_momentum_formula"],
        [{"step": 1, "criterion": "Formula p = mv rearranged", "marks": 1}, {"step": 2, "criterion": f"Final answer {ans}", "marks": 1}],
        {"tier_1": "Rearrange p = m * v to isolate the unknown variable.", "tier_2": "Divide momentum p by the known variable.", "tier_3": ans},
    )


# 06. Comparing momenta of different objects
def build_06_comparing_momenta_of_different_objects(r: random.Random) -> Dict[str, Any]:
    m_truck = r.choice([4000, 5000, 6000])
    v_truck = r.choice([8.0, 10.0, 12.0])
    p_truck = m_truck * v_truck
    m_car = r.choice([1000, 1200, 1600])
    v_car = round(p_truck / m_car, 2)

    prompt = (
        f"A truck of mass ${m_truck}\\text{{ kg}}$ moves at ${_fmt(v_truck)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ east.\n\n"
        f"1. Calculate the magnitude of the truck's momentum.\n"
        f"2. At what speed must a smaller car of mass ${m_car}\\text{{ kg}}$ travel so that it has the **same magnitude of momentum** as the truck?"
    )
    ans = f"p = {_fmt(p_truck)} kg·m·s⁻¹; v_car = {_fmt(v_car)} m·s⁻¹"
    sol = (
        f"1. $p_{{\\text{{truck}}}} = m_{{\\text{{truck}}}} v_{{\\text{{truck}}}} = ({m_truck})({_fmt(v_truck)}) = {_fmt(p_truck)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"2. Set $p_{{\\text{{car}}}} = p_{{\\text{{truck}}}}$:\n"
        f"   $$v_{{\\text{{car}}}} = \\frac{{{_fmt(p_truck)}}}{{{m_car}}} = {_fmt(v_car)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "06_comparing_momenta_of_different_objects", 6, prompt, ans, sol, 3,
        ["equated_kinetic_energies_instead_of_momenta"],
        [{"step": 1, "criterion": f"Truck momentum = {_fmt(p_truck)} kg·m·s⁻¹", "marks": 1}, {"step": 2, "criterion": "Equate p_car = p_truck", "marks": 1}, {"step": 3, "criterion": f"Car speed = {_fmt(v_car)} m·s⁻¹", "marks": 1}],
        {"tier_1": "First find p = m * v for the truck.", "tier_2": "Divide the truck's momentum by the car's mass.", "tier_3": ans},
    )


# 07. Momentum and kinetic energy relationship
def build_07_momentum_and_kinetic_energy_relationship(r: random.Random) -> Dict[str, Any]:
    m = r.choice([2.0, 4.0, 5.0, 8.0, 10.0])
    v = r.choice([3.0, 4.0, 6.0, 8.0, 10.0])
    p = round(m * v, 2)
    ek = round(0.5 * m * v * v, 2)

    prompt = (
        f"A dynamics cart of mass ${_fmt(m)}\\text{{ kg}}$ has a linear momentum of magnitude ${_fmt(p)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Calculate the speed of the cart.\n"
        f"2. Calculate the kinetic energy ($E_k$) of the cart (using $E_k = \\frac{{1}}{{2}}mv^2$ or $E_k = \\frac{{p^2}}{{2m}}$)."
    )
    ans = f"v = {_fmt(v)} m·s⁻¹; Ek = {_fmt(ek)} J"
    sol = (
        f"1. $v = \\frac{{p}}{{m}} = \\frac{{{_fmt(p)}}}{{{_fmt(m)}}} = {_fmt(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"2. $E_k = \\frac{{1}}{{2}} m v^2 = \\frac{{1}}{{2}} ({_fmt(m)})({_fmt(v)})^2 = {_fmt(ek)}\\text{{ J}}$ "
        f"(or $E_k = \\frac{{p^2}}{{2m}} = \\frac{{{_fmt(p)}^2}}{{2({_fmt(m)})}} = {_fmt(ek)}\\text{{ J}}$)."
    )
    return _make_q(
        r, "07_momentum_and_kinetic_energy_relationship", 7, prompt, ans, sol, 3,
        ["confused_momentum_and_kinetic_energy_formulas"],
        [{"step": 1, "criterion": f"Speed v = {_fmt(v)} m·s⁻¹", "marks": 1}, {"step": 2, "criterion": "Kinetic energy formula", "marks": 1}, {"step": 3, "criterion": f"Ek = {_fmt(ek)} J", "marks": 1}],
        {"tier_1": "Find v = p / m first.", "tier_2": "Substitute m and v into Ek = 0,5 * m * v^2.", "tier_3": ans},
    )


# 08. Momentum scaling when mass or velocity changes
def build_08_momentum_scaling_when_mass_or_velocity_changes(r: random.Random) -> Dict[str, Any]:
    k_m = r.choice([1, 2, 3])
    k_v = r.choice([2, 3, 4])
    p_init = r.choice([12, 15, 20, 25, 30])
    factor_p = k_m * k_v
    factor_ek = k_m * (k_v ** 2)
    p_new = p_init * factor_p

    prompt = (
        f"A particle traveling along a horizontal path has a momentum of magnitude $p = {p_init}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"and kinetic energy $E_k$.\n"
        f"Its mass is scaled by a factor of ${k_m}$ and its velocity is scaled by a factor of ${k_v}$.\n\n"
        f"1. Determine the new magnitude of the particle's momentum.\n"
        f"2. By what factor does its kinetic energy increase?"
    )
    ans = f"p_new = {p_new} kg·m·s⁻¹; Ek increases by factor of {factor_ek}"
    sol = (
        f"1. Since $p \\propto m v$, multiplying mass by ${k_m}$ and speed by ${k_v}$ scales momentum by ${k_m} \\times {k_v} = {factor_p}$:\n"
        f"   $$p_{{\\text{{new}}}} = {factor_p} \\times {p_init} = {p_new}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"2. Since $E_k = \\frac{{1}}{{2}}mv^2 \\propto m v^2$, kinetic energy scales by ${k_m} \\times {k_v}^2 = {factor_ek}$."
    )
    return _make_q(
        r, "08_momentum_scaling_when_mass_or_velocity_changes", 8, prompt, ans, sol, 3,
        ["failed_to_square_velocity_factor_for_kinetic_energy"],
        [{"step": 1, "criterion": f"Momentum scale factor = {factor_p}", "marks": 1}, {"step": 2, "criterion": f"New momentum = {p_new} kg·m·s⁻¹", "marks": 1}, {"step": 3, "criterion": f"Ek scale factor = {factor_ek}", "marks": 1}],
        {"tier_1": "Momentum is linear in both m and v: p_new = (k_m * k_v) * p.", "tier_2": "Kinetic energy is proportional to m * v^2.", "tier_3": ans},
    )


# 09. Change in momentum same direction speed increase
def build_09_change_in_momentum_same_direction_speed_increase(r: random.Random) -> Dict[str, Any]:
    m = r.choice([800, 1000, 1200, 1500])
    vi = r.choice([10.0, 12.0, 15.0])
    vf = r.choice([22.0, 25.0, 28.0, 30.0])
    d = r.choice(["east", "north", "to the right"])
    dp = round(m * (vf - vi), 1)

    prompt = (
        f"A car of mass ${m}\\text{{ kg}}$ accelerates uniformly from ${_fmt(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ {d} "
        f"to ${_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ {d}.\n\n"
        f"Taking {d} as positive, calculate the change in momentum ($\\Delta\\vec{{p}}$) of the car."
    )
    ans = f"{_fmt(dp)} kg·m·s⁻¹ {d}"
    sol = (
        f"Choose {d} as positive ($+$):\n"
        f"$$\\Delta p = m(v_f - v_i) = {m}({_fmt(vf)} - {_fmt(vi)}) = +{_fmt(dp)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"Therefore, $\\Delta\\vec{{p}} = {_fmt(dp)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ {d}."
    )
    return _make_q(
        r, "09_change_in_momentum_same_direction_speed_increase", 9, prompt, ans, sol, 3,
        ["swapped_initial_and_final_velocities_in_delta_p"],
        [{"step": 1, "criterion": "Formula Δp = m(vf - vi)", "marks": 1}, {"step": 2, "criterion": f"Substitution {m}({_fmt(vf)} - {_fmt(vi)})", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(dp)} kg·m·s⁻¹ {d}", "marks": 1}],
        {"tier_1": "Use Δp = m(vf - vi) with a chosen positive direction.", "tier_2": "Since both velocities are in the same direction, both are positive.", "tier_3": ans},
    )


# 10. Change in momentum same direction braking
def build_10_change_in_momentum_same_direction_braking(r: random.Random) -> Dict[str, Any]:
    m = r.choice([1200, 1400, 1600, 2000])
    vi = r.choice([25.0, 30.0, 20.0])
    vf = r.choice([5.0, 8.0, 10.0, 0.0])
    dp = round(m * (vf - vi), 1)

    prompt = (
        f"A vehicle of mass ${m}\\text{{ kg}}$ travelling east at ${_fmt(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ applies its brakes "
        f"and slows down to ${_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ east.\n\n"
        f"Taking east as positive, calculate the change in momentum ($\\Delta\\vec{{p}}$) of the vehicle and state its direction."
    )
    ans = f"{_fmt(abs(dp))} kg·m·s⁻¹ west"
    sol = (
        f"Take east as positive ($+$):\n"
        f"$$\\Delta p = m(v_f - v_i) = {m}({_fmt(vf)} - {_fmt(vi)}) = {_fmt(dp)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"Therefore, $\\Delta\\vec{{p}} = {_fmt(abs(dp))}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ **west** (opposite to motion)."
    )
    return _make_q(
        r, "10_change_in_momentum_same_direction_braking", 10, prompt, ans, sol, 3,
        ["failed_to_interpret_negative_sign_as_opposite_direction"],
        [{"step": 1, "criterion": "Formula Δp = m(vf - vi)", "marks": 1}, {"step": 2, "criterion": f"Calculation gives {_fmt(dp)}", "marks": 1}, {"step": 3, "criterion": f"Magnitude {_fmt(abs(dp))} kg·m·s⁻¹ west", "marks": 1}],
        {"tier_1": "Substitute vf and vi with east as positive.", "tier_2": "A negative answer means the change in momentum is directed west.", "tier_3": ans},
    )


# 11. Change in momentum rebound opposite direction
def build_11_change_in_momentum_rebound_opposite_direction(r: random.Random) -> Dict[str, Any]:
    m = r.choice([0.15, 0.20, 0.25, 0.40, 0.50])
    vi = r.choice([12.0, 15.0, 18.0, 20.0])
    vf_mag = r.choice([8.0, 10.0, 12.0, 14.0])
    dp = round(m * (-vf_mag - vi), 2)

    prompt = (
        f"A rubber ball of mass ${_fmt(m)}\\text{{ kg}}$ strikes a vertical wall horizontally at ${_fmt(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"towards the wall and rebounds horizontally at ${_fmt(vf_mag)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ away from the wall.\n\n"
        f"Taking the direction towards the wall as positive, calculate the change in momentum ($\\Delta\\vec{{p}}$) of the ball."
    )
    ans = f"{_fmt(abs(dp))} kg·m·s⁻¹ away from the wall"
    sol = (
        f"Choose towards the wall as positive ($+$):\n"
        f"- $v_i = +{_fmt(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n"
        f"- $v_f = -{_fmt(vf_mag)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n"
        f"$$\\Delta p = m(v_f - v_i) = {_fmt(m)}(-{_fmt(vf_mag)} - {_fmt(vi)}) = {_fmt(dp)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"Therefore, $\\Delta\\vec{{p}} = {_fmt(abs(dp))}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ **away from the wall**."
    )
    return _make_q(
        r, "11_change_in_momentum_rebound_opposite_direction", 11, prompt, ans, sol, 4,
        ["omitted_negative_sign_for_rebound_velocity"],
        [{"step": 1, "criterion": "Formula Δp = m(vf - vi)", "marks": 1}, {"step": 2, "criterion": f"Assign negative sign to rebound velocity (-{_fmt(vf_mag)})", "marks": 1}, {"step": 3, "criterion": f"Magnitude {_fmt(abs(dp))} kg·m·s⁻¹", "marks": 1}, {"step": 4, "criterion": "Direction: away from the wall", "marks": 1}],
        {"tier_1": "Velocity is a vector! Rebound is in the opposite direction, so vf must be negative.", "tier_2": f"Δp = {_fmt(m)} * (-{_fmt(vf_mag)} - {_fmt(vi)}).", "tier_3": ans},
    )


# 12. Vector diagram for change in momentum (with SVG)
def build_12_vector_diagram_for_change_in_momentum_svg(r: random.Random) -> Dict[str, Any]:
    m = r.choice([0.2, 0.5, 0.8, 1.0])
    vi = r.choice([10.0, 14.0, 16.0, 20.0])
    vf = r.choice([6.0, 8.0, 10.0, 12.0])
    pi = round(m * vi, 2)
    pf = round(m * vf, 2)
    dp = round(pi + pf, 2)
    svg = _svg_momentum_vectors(pi, pf, dp)

    prompt = (
        f"Refer to the momentum vector diagram for a ball of mass ${_fmt(m)}\\text{{ kg}}$ that hits a barrier with initial momentum "
        f"$\\vec{{p}}_i = +{_fmt(pi)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ towards the barrier and rebounds with "
        f"$\\vec{{p}}_f = -{_fmt(pf)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ away from the barrier.\n\n"
        f"1. Calculate the initial speed and rebound speed of the ball.\n"
        f"2. Explain why the magnitude of $\\Delta\\vec{{p}}$ is equal to the sum $|p_i| + |p_f| = {_fmt(dp)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ rather than the difference."
    )
    ans = f"v_i = {_fmt(vi)} m·s⁻¹, v_f = {_fmt(vf)} m·s⁻¹; Δp = p_f - p_i = -{_fmt(dp)} kg·m·s⁻¹ because p_f is negative"
    sol = (
        f"1. $v_i = \\frac{{p_i}}{{m}} = \\frac{{{_fmt(pi)}}}{{{_fmt(m)}}} = {_fmt(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$; "
        f"$v_f = \\frac{{|p_f|}}{{m}} = \\frac{{{_fmt(pf)}}}{{{_fmt(m)}}} = {_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"2. Because $\\vec{{p}}_f$ and $\\vec{{p}}_i$ are in opposite directions, subtracting $+{_fmt(pi)}$ from $-{_fmt(pf)}$ yields "
        f"$\\Delta p = -{_fmt(pf)} - (+{_fmt(pi)}) = -{_fmt(dp)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$, so the magnitudes add."
    )
    return _make_q(
        r, "12_vector_diagram_for_change_in_momentum_svg", 12, prompt, ans, sol, 3,
        ["subtracted_magnitudes_for_rebound_momentum_change"],
        [{"step": 1, "criterion": f"Initial speed {_fmt(vi)} m·s⁻¹ and rebound speed {_fmt(vf)} m·s⁻¹", "marks": 1}, {"step": 2, "criterion": "Vector subtraction Δp = pf - pi explained", "marks": 1}, {"step": 3, "criterion": f"Magnitude {_fmt(dp)} kg·m·s⁻¹ away from barrier", "marks": 1}],
        {"tier_1": "Divide momentum by mass to find speed.", "tier_2": "Subtracting a positive vector from a negative vector increases the negative magnitude.", "tier_3": ans},
        svg=svg,
    )


# 13. Vertical bounce change in momentum
def build_13_vertical_bounce_change_in_momentum(r: random.Random) -> Dict[str, Any]:
    m = r.choice([0.10, 0.25, 0.40, 0.50, 0.60])
    v_down = r.choice([6.0, 8.0, 9.0, 10.0])
    v_up = r.choice([4.0, 5.0, 6.0, 7.0])
    dp = round(m * (v_up - (-v_down)), 2)

    prompt = (
        f"A basketball of mass ${_fmt(m)}\\text{{ kg}}$ strikes the gymnasium floor vertically downwards at ${_fmt(v_down)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"and bounces vertically upwards at ${_fmt(v_up)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Taking upwards as positive, calculate the change in momentum ($\\Delta\\vec{{p}}$) of the basketball during its contact with the floor."
    )
    ans = f"{_fmt(dp)} kg·m·s⁻¹ upwards"
    sol = (
        f"Take upwards as positive ($+$):\n"
        f"- $v_i = -{_fmt(v_down)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n"
        f"- $v_f = +{_fmt(v_up)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n"
        f"$$\\Delta p = m(v_f - v_i) = {_fmt(m)}({_fmt(v_up)} - (-{_fmt(v_down)})) = +{_fmt(dp)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"Therefore, $\\Delta\\vec{{p}} = {_fmt(dp)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ **upwards**."
    )
    return _make_q(
        r, "13_vertical_bounce_change_in_momentum", 13, prompt, ans, sol, 4,
        ["omitted_negative_sign_for_downward_velocity"],
        [{"step": 1, "criterion": "Formula Δp = m(vf - vi)", "marks": 1}, {"step": 2, "criterion": f"Substitute vi = -{_fmt(v_down)} and vf = +{_fmt(v_up)}", "marks": 2}, {"step": 3, "criterion": f"Answer {_fmt(dp)} kg·m·s⁻¹ upwards", "marks": 1}],
        {"tier_1": "With upwards as positive, downward impact velocity is negative.", "tier_2": f"Δp = {_fmt(m)} * ({_fmt(v_up)} - (-{_fmt(v_down)})).", "tier_3": ans},
    )


# 14. Newton's second law in terms of momentum statement
def build_14_newtons_second_law_in_terms_of_momentum_statement(r: random.Random) -> Dict[str, Any]:
    dp = r.choice([24.0, 36.0, 48.0, 60.0, 90.0])
    dt = r.choice([0.2, 0.3, 0.4, 0.5, 0.6])
    f_res = round(dp / dt, 1)

    prompt = (
        f"During an interaction lasting ${_fmt(dt)}\\text{{ s}}$, an object experiences a change in momentum of magnitude "
        f"${_fmt(dp)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ east.\n\n"
        f"1. State **Newton's Second Law of Motion in terms of momentum** in words.\n"
        f"2. Calculate the resultant force ($\\vec{{F}}_{{\\text{{net}}}}$) acting on the object."
    )
    ans = f"Resultant force equals rate of change of momentum; {_fmt(f_res)} N east"
    sol = (
        f"1. **Newton's Second Law in terms of momentum:** The resultant force acting on an object is equal to the rate of change of momentum of the object ($\\vec{{F}}_{{\\text{{net}}}} = \\frac{{\\Delta\\vec{{p}}}}{{\\Delta t}}$).\n"
        f"2. $$F_{{\\text{{net}}}} = \\frac{{\\Delta p}}{{\\Delta t}} = \\frac{{{_fmt(dp)}}}{{{_fmt(dt)}}} = {_fmt(f_res)}\\text{{ N east}}$$"
    )
    return _make_q(
        r, "14_newtons_second_law_in_terms_of_momentum_statement", 14, prompt, ans, sol, 4,
        ["omitted_rate_of_in_newtons_second_law_momentum_statement"],
        [{"step": 1, "criterion": "Complete law statement including 'rate of change of momentum'", "marks": 2}, {"step": 2, "criterion": "Formula F_net = Δp / Δt", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(f_res)} N east", "marks": 1}],
        {"tier_1": "Be careful to include the words 'rate of change of momentum' in the definition.", "tier_2": f"Divide Δp ({_fmt(dp)}) by Δt ({_fmt(dt)}).", "tier_3": ans},
    )


# 15. Resultant force from rate of change of momentum
def build_15_resultant_force_from_rate_of_change_of_momentum(r: random.Random) -> Dict[str, Any]:
    m = r.choice([1000, 1200, 1500, 1800])
    vi = r.choice([20.0, 24.0, 30.0])
    vf = r.choice([0.0, 5.0, 8.0])
    dt = r.choice([2.0, 4.0, 5.0])
    f_res = round((m * (vf - vi)) / dt, 1)

    prompt = (
        f"A car of mass ${m}\\text{{ kg}}$ moving at ${_fmt(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ north slows uniformly to "
        f"${_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ north in ${_fmt(dt)}\\text{{ s}}$.\n\n"
        f"Use Newton's Second Law in terms of momentum to calculate the magnitude and direction of the resultant force ($\\vec{{F}}_{{\\text{{net}}}}$) acting on the car."
    )
    ans = f"{_fmt(abs(f_res))} N south"
    sol = (
        f"Take north as positive ($+$):\n"
        f"$$F_{{\\text{{net}}}} = \\frac{{m(v_f - v_i)}}{{\\Delta t}} = \\frac{{{m}({_fmt(vf)} - {_fmt(vi)})}}{{{_fmt(dt)}}} = {_fmt(f_res)}\\text{{ N}}$$\n"
        f"Therefore, $\\vec{{F}}_{{\\text{{net}}}} = {_fmt(abs(f_res))}\\text{{ N}}$ **south**."
    )
    return _make_q(
        r, "15_resultant_force_from_rate_of_change_of_momentum", 15, prompt, ans, sol, 4,
        ["multiplied_by_time_instead_of_dividing_for_force"],
        [{"step": 1, "criterion": "Formula F_net = Δp / Δt", "marks": 1}, {"step": 2, "criterion": f"Substitution {m}({_fmt(vf)} - {_fmt(vi)}) / {_fmt(dt)}", "marks": 2}, {"step": 3, "criterion": f"Answer {_fmt(abs(f_res))} N south", "marks": 1}],
        {"tier_1": "Use F_net = m(vf - vi) / Δt.", "tier_2": "A negative value indicates a braking force acting south.", "tier_3": ans},
    )


# 16. Contact time from resultant force and momentum change
def build_16_contact_time_from_resultant_force_and_momentum_change(r: random.Random) -> Dict[str, Any]:
    m = r.choice([0.05, 0.15, 0.45])
    vi = 0.0
    vf = r.choice([20.0, 30.0, 40.0])
    f_res = r.choice([150.0, 200.0, 300.0, 450.0])
    dt = round((m * (vf - vi)) / f_res, 4)

    prompt = (
        f"A stationary ball of mass ${_fmt(m)}\\text{{ kg}}$ is kicked and leaves the player's boot with a speed of "
        f"${_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. The average resultant force exerted on the ball is ${_fmt(f_res)}\\text{{ N}}$.\n\n"
        f"Calculate the contact time ($\\Delta t$) between the boot and the ball."
    )
    ans = f"{_fmt(dt, 4)} s"
    sol = (
        f"$$F_{{\\text{{net}}}} \\Delta t = m(v_f - v_i)$$\n"
        f"$$\\Delta t = \\frac{{m(v_f - v_i)}}{{F_{{\\text{{net}}}}}} = \\frac{{{_fmt(m)}({_fmt(vf)} - 0)}}{{{_fmt(f_res)}}} = {_fmt(dt, 4)}\\text{{ s}}$$"
    )
    return _make_q(
        r, "16_contact_time_from_resultant_force_and_momentum_change", 16, prompt, ans, sol, 3,
        ["inverted_time_formula_in_impulse_equation"],
        [{"step": 1, "criterion": "Formula F_net * Δt = Δp", "marks": 1}, {"step": 2, "criterion": "Substitution of mass, velocity and force", "marks": 1}, {"step": 3, "criterion": f"Contact time = {_fmt(dt, 4)} s", "marks": 1}],
        {"tier_1": "Rearrange F_net * Δt = m(vf - vi) to solve for Δt.", "tier_2": f"Δt = ({_fmt(m)} * {_fmt(vf)}) / {_fmt(f_res)}.", "tier_3": ans},
    )


# 17. Final velocity from resultant force and contact time
def build_17_final_velocity_from_resultant_force_and_contact_time(r: random.Random) -> Dict[str, Any]:
    m = r.choice([2.0, 4.0, 5.0, 10.0])
    vi = r.choice([3.0, 5.0, 6.0])
    f_res = r.choice([12.0, 20.0, 30.0])
    dt = r.choice([2.0, 3.0, 4.0])
    vf = round(vi + (f_res * dt) / m, 2)

    prompt = (
        f"A crate of mass ${_fmt(m)}\\text{{ kg}}$ is sliding east at ${_fmt(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ on a frictionless surface.\n"
        f"A constant resultant force of ${_fmt(f_res)}\\text{{ N}}$ east acts on the crate for ${_fmt(dt)}\\text{{ s}}$.\n\n"
        f"Calculate the final velocity of the crate after ${_fmt(dt)}\\text{{ s}}$."
    )
    ans = f"{_fmt(vf)} m·s⁻¹ east"
    sol = (
        f"Take east as positive ($+$):\n"
        f"$$F_{{\\text{{net}}}} \\Delta t = m(v_f - v_i)$$\n"
        f"$${_fmt(f_res)} \\times {_fmt(dt)} = {_fmt(m)}(v_f - {_fmt(vi)})$$\n"
        f"$$v_f = {_fmt(vi)} + \\frac{{{_fmt(f_res * dt)}}}{{{_fmt(m)}}} = {_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ east}}$$"
    )
    return _make_q(
        r, "17_final_velocity_from_resultant_force_and_contact_time", 17, prompt, ans, sol, 3,
        ["forgot_to_add_initial_velocity_after_impulse_calculation"],
        [{"step": 1, "criterion": "Formula F_net * Δt = m(vf - vi)", "marks": 1}, {"step": 2, "criterion": "Correct substitution", "marks": 1}, {"step": 3, "criterion": f"Final velocity = {_fmt(vf)} m·s⁻¹ east", "marks": 1}],
        {"tier_1": "Use F_net * Δt = m(vf - vi).", "tier_2": "Solve for vf = vi + (F_net * Δt) / m.", "tier_3": ans},
    )


# 18. Impulse definition and units equivalence
def build_18_impulse_definition_and_units_equivalence(r: random.Random) -> Dict[str, Any]:
    f_val = r.choice([40, 60, 80, 120])
    dt = r.choice([0.5, 1.5, 2.5])
    imp = round(f_val * dt, 1)

    prompt = (
        f"A resultant force of ${f_val}\\text{{ N}}$ west acts on a body for ${_fmt(dt)}\\text{{ s}}$.\n\n"
        f"1. Define **impulse** in words.\n"
        f"2. Show using base SI units that the unit of impulse ($\\text{{N}}\\cdot\\text{{s}}$) is equivalent to the unit of momentum ($\\text{{kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$).\n"
        f"3. Calculate the impulse exerted on the body."
    )
    ans = f"Product of resultant force and contact time; 1 N·s = 1 (kg·m·s⁻²)·s = 1 kg·m·s⁻¹; {_fmt(imp)} N·s west"
    sol = (
        f"1. **Impulse** is the product of the resultant force acting on an object and the time for which the force acts ($\\text{{Impulse}} = \\vec{{F}}_{{\\text{{net}}}}\\Delta t$).\n"
        f"2. Since $1\\text{{ N}} = 1\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-2}}$, multiplying by time in seconds ($\\text{{s}}$) gives:\n"
        f"   $$1\\text{{ N}}\\cdot\\text{{s}} = (1\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-2}}) \\cdot \\text{{s}} = 1\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"3. $\\text{{Impulse}} = F_{{\\text{{net}}}}\\Delta t = {f_val} \\times {_fmt(dt)} = {_fmt(imp)}\\text{{ N}}\\cdot\\text{{s}}$ west."
    )
    return _make_q(
        r, "18_impulse_definition_and_units_equivalence", 18, prompt, ans, sol, 4,
        ["confused_impulse_definition_with_force_definition"],
        [{"step": 1, "criterion": "Definition: product of resultant force and contact time", "marks": 1}, {"step": 2, "criterion": "Unit equivalence N·s = kg·m·s⁻¹ shown", "marks": 1}, {"step": 3, "criterion": f"Impulse = {_fmt(imp)} N·s west", "marks": 2}],
        {"tier_1": "Impulse = F_net * Δt.", "tier_2": "Replace N with kg·m·s⁻² and multiply by s.", "tier_3": ans},
    )


# 19. Impulse from constant force and contact time
def build_19_impulse_from_constant_force_and_contact_time(r: random.Random) -> Dict[str, Any]:
    f_val = r.choice([250, 400, 600, 850, 1200])
    dt = r.choice([0.02, 0.04, 0.05, 0.08, 0.10])
    d = r.choice(["east", "west", "upwards", "forward"])
    imp = round(f_val * dt, 2)

    prompt = (
        f"A hockey stick exerts an average resultant force of ${f_val}\\text{{ N}}$ {d} on a ball for a contact duration of ${_fmt(dt)}\\text{{ s}}$.\n\n"
        f"1. Calculate the impulse delivered to the ball.\n"
        f"2. State the magnitude and direction of the change in momentum ($\\Delta\\vec{{p}}$) of the ball."
    )
    ans = f"Impulse = {_fmt(imp)} N·s {d}; Δp = {_fmt(imp)} kg·m·s⁻¹ {d}"
    sol = (
        f"1. $\\text{{Impulse}} = F_{{\\text{{net}}}}\\Delta t = {f_val} \\times {_fmt(dt)} = {_fmt(imp)}\\text{{ N}}\\cdot\\text{{s}}$ {d}.\n"
        f"2. By the impulse-momentum theorem ($\\text{{Impulse}} = \\Delta\\vec{{p}}$), "
        f"$\\Delta\\vec{{p}} = {_fmt(imp)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ {d}."
    )
    return _make_q(
        r, "19_impulse_from_constant_force_and_contact_time", 19, prompt, ans, sol, 3,
        ["divided_force_by_time_for_impulse"],
        [{"step": 1, "criterion": "Formula Impulse = F_net * Δt", "marks": 1}, {"step": 2, "criterion": f"Impulse = {_fmt(imp)} N·s {d}", "marks": 1}, {"step": 3, "criterion": f"Δp = {_fmt(imp)} kg·m·s⁻¹ {d}", "marks": 1}],
        {"tier_1": "Multiply force by contact time to find impulse.", "tier_2": "Impulse is equal to the change in momentum Δp.", "tier_3": ans},
    )


# 20. Impulse momentum theorem ball struck by bat
def build_20_impulse_momentum_theorem_ball_struck_by_bat(r: random.Random) -> Dict[str, Any]:
    m = r.choice([0.15, 0.16, 0.20])
    vi = r.choice([25.0, 30.0, 35.0])
    vf = r.choice([40.0, 45.0, 50.0])
    dt = r.choice([0.01, 0.02, 0.025])
    imp = round(m * (vf + vi), 2)
    f_ave = round(imp / dt, 1)

    prompt = (
        f"A cricket ball of mass ${_fmt(m)}\\text{{ kg}}$ approaches a batter horizontally at ${_fmt(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"and is struck directly back in the opposite direction at ${_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"The ball remains in contact with the bat for ${_fmt(dt, 3)}\\text{{ s}}$.\n\n"
        f"1. Calculate the magnitude of the impulse exerted by the bat on the ball.\n"
        f"2. Calculate the magnitude of the average resultant force exerted by the bat on the ball."
    )
    ans = f"Impulse = {_fmt(imp)} N·s; F_net = {_fmt(f_ave)} N"
    sol = (
        f"1. Take the direction away from the batter as positive ($+$): $v_i = -{_fmt(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, $v_f = +{_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"   $$\\text{{Impulse}} = \\Delta p = m(v_f - v_i) = {_fmt(m)}({_fmt(vf)} - (-{_fmt(vi)})) = {_fmt(imp)}\\text{{ N}}\\cdot\\text{{s}}$$\n"
        f"2. $$F_{{\\text{{net}}}} = \\frac{{\\text{{Impulse}}}}{{\\Delta t}} = \\frac{{{_fmt(imp)}}}{{{_fmt(dt, 3)}}} = {_fmt(f_ave)}\\text{{ N}}$$"
    )
    return _make_q(
        r, "20_impulse_momentum_theorem_ball_struck_by_bat", 20, prompt, ans, sol, 4,
        ["omitted_negative_sign_for_approaching_ball_velocity"],
        [{"step": 1, "criterion": "Formula Impulse = m(vf - vi)", "marks": 1}, {"step": 2, "criterion": f"Opposite signs for vi and vf -> Impulse = {_fmt(imp)} N·s", "marks": 2}, {"step": 3, "criterion": f"Average force = {_fmt(f_ave)} N", "marks": 1}],
        {"tier_1": "Choose a positive direction; the incoming and outgoing velocities have opposite signs.", "tier_2": "Once you find Δp, divide by contact time Δt to get F_net.", "tier_3": ans},
    )


# 21. Force-time graph rectangular area impulse (with SVG)
def build_21_force_time_graph_rectangular_area_impulse_svg(r: random.Random) -> Dict[str, Any]:
    f_max = r.choice([50.0, 80.0, 120.0, 150.0, 200.0])
    dt = r.choice([2.0, 3.0, 4.0, 5.0])
    m = r.choice([10.0, 20.0, 25.0])
    imp = round(f_max * dt, 1)
    dv = round(imp / m, 2)
    svg = _svg_ft_rect(f_max, dt)

    prompt = (
        f"Refer to the Force-time graph for a constant resultant force acting on a stationary trolley of mass ${_fmt(m)}\\text{{ kg}}$ on a frictionless track.\n\n"
        f"1. State the physical quantity represented by the **area under a Force-time graph**.\n"
        f"2. Calculate the impulse delivered to the trolley from $t = 0\\text{{ s}}$ to $t = {_fmt(dt)}\\text{{ s}}$.\n"
        f"3. Calculate the speed of the trolley at $t = {_fmt(dt)}\\text{{ s}}$."
    )
    ans = f"Impulse (or change in momentum); {_fmt(imp)} N·s; {_fmt(dv)} m·s⁻¹"
    sol = (
        f"1. The area under a Force-time graph represents **impulse** (or **change in momentum**, $\\Delta p$).\n"
        f"2. $\\text{{Impulse}} = \\text{{Area}} = F \\times \\Delta t = {_fmt(f_max)} \\times {_fmt(dt)} = {_fmt(imp)}\\text{{ N}}\\cdot\\text{{s}}$.\n"
        f"3. $\\Delta p = m(v_f - 0) \\implies v_f = \\frac{{{_fmt(imp)}}}{{{_fmt(m)}}} = {_fmt(dv)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    return _make_q(
        r, "21_force_time_graph_rectangular_area_impulse_svg", 21, prompt, ans, sol, 3,
        ["calculated_gradient_instead_of_area_for_impulse"],
        [{"step": 1, "criterion": "Area represents impulse / change in momentum", "marks": 1}, {"step": 2, "criterion": f"Impulse = {_fmt(imp)} N·s", "marks": 1}, {"step": 3, "criterion": f"Final speed = {_fmt(dv)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Impulse equals the area between the F-t curve and the time axis.", "tier_2": f"Area = {_fmt(f_max)} * {_fmt(dt)}, then divide by mass {_fmt(m)} kg.", "tier_3": ans},
        svg=svg,
    )


# 22. Force-time graph triangular peak force (with SVG)
def build_22_force_time_graph_triangular_peak_force_svg(r: random.Random) -> Dict[str, Any]:
    f_peak = r.choice([400.0, 600.0, 800.0, 1000.0, 1200.0])
    t_end = r.choice([0.02, 0.04, 0.06, 0.08, 0.10])
    imp = round(0.5 * f_peak * t_end, 2)
    f_ave = round(f_peak / 2.0, 1)
    svg = _svg_ft_triangle(f_peak, t_end)

    prompt = (
        f"Refer to the triangular Force-time graph recorded by a force sensor during a collision lasting ${_fmt(t_end, 3)}\\text{{ s}}$, "
        f"where the peak force reaches ${_fmt(f_peak)}\\text{{ N}}$.\n\n"
        f"1. Calculate the magnitude of the impulse exerted during the collision.\n"
        f"2. Determine the magnitude of the **average resultant force** over the ${_fmt(t_end, 3)}\\text{{ s}}$ interval."
    )
    ans = f"Impulse = {_fmt(imp)} N·s; F_ave = {_fmt(f_ave)} N"
    sol = (
        f"1. $\\text{{Impulse}} = \\text{{Area of triangle}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} = \\frac{{1}}{{2}} \\times {_fmt(t_end, 3)} \\times {_fmt(f_peak)} = {_fmt(imp)}\\text{{ N}}\\cdot\\text{{s}}$.\n"
        f"2. $F_{{\\text{{ave}}}} = \\frac{{\\text{{Impulse}}}}{{\\Delta t}} = \\frac{{{_fmt(imp)}}}{{{_fmt(t_end, 3)}}} = {_fmt(f_ave)}\\text{{ N}}$."
    )
    return _make_q(
        r, "22_force_time_graph_triangular_peak_force_svg", 22, prompt, ans, sol, 3,
        ["omitted_half_factor_in_triangle_area_impulse"],
        [{"step": 1, "criterion": "Area = 0,5 * base * height", "marks": 1}, {"step": 2, "criterion": f"Impulse = {_fmt(imp)} N·s", "marks": 1}, {"step": 3, "criterion": f"Average force = {_fmt(f_ave)} N", "marks": 1}],
        {"tier_1": "Calculate the area of the triangle: 0,5 * Δt * F_peak.", "tier_2": "Average force is total impulse divided by total contact time.", "tier_3": ans},
        svg=svg,
    )


# 23. Force-time graph trapezoidal velocity change (with SVG)
def build_23_force_time_graph_trapezoidal_velocity_change_svg(r: random.Random) -> Dict[str, Any]:
    f_const = r.choice([20.0, 30.0, 40.0, 50.0])
    t1, t2, t3 = 2.0, 6.0, 8.0
    m = r.choice([4.0, 5.0, 8.0, 10.0])
    # Area = 0.5*2*F + 4*F + 0.5*2*F = 6*F
    imp = round(6.0 * f_const, 1)
    vf = round(imp / m, 2)
    svg = _svg_ft_trapezoid(f_const, t1, t2, t3)

    prompt = (
        f"Refer to the trapezoidal Force-time graph for a model rocket sled of mass ${_fmt(m)}\\text{{ kg}}$ starting from rest at $t = 0\\text{{ s}}$.\n\n"
        f"1. Calculate the total impulse delivered to the sled over the $8\\text{{ s}}$ interval.\n"
        f"2. Calculate the speed of the sled at $t = 8\\text{{ s}}$."
    )
    ans = f"Impulse = {_fmt(imp)} N·s; v_f = {_fmt(vf)} m·s⁻¹"
    sol = (
        f"1. Total area under the graph from $t = 0\\text{{ s}}$ to $t = 8\\text{{ s}}$:\n"
        f"   $$\\text{{Impulse}} = \\frac{{1}}{{2}}(2)({_fmt(f_const)}) + (4)({_fmt(f_const)}) + \\frac{{1}}{{2}}(2)({_fmt(f_const)}) = {_fmt(imp)}\\text{{ N}}\\cdot\\text{{s}}$$\n"
        f"2. Since $v_i = 0$:\n"
        f"   $$v_f = \\frac{{\\Delta p}}{{m}} = \\frac{{{_fmt(imp)}}}{{{_fmt(m)}}} = {_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "23_force_time_graph_trapezoidal_velocity_change_svg", 23, prompt, ans, sol, 4,
        ["treated_trapezoid_as_simple_rectangle"],
        [{"step": 1, "criterion": "Split area into triangles and rectangle (or trapezoid formula)", "marks": 1}, {"step": 2, "criterion": f"Total impulse = {_fmt(imp)} N·s", "marks": 1}, {"step": 3, "criterion": "Apply Δp = m(vf - vi)", "marks": 1}, {"step": 4, "criterion": f"Final speed = {_fmt(vf)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Find the sum of the areas of the three sections (0–2 s, 2–6 s, and 6–8 s).", "tier_2": f"Total impulse = 6 * {_fmt(f_const)} = {_fmt(imp)} N·s; divide by mass {_fmt(m)} kg.", "tier_3": ans},
        svg=svg,
    )


# 24. Force-time graph with direction reversal (with SVG)
def build_24_force_time_graph_with_direction_reversal_svg(r: random.Random) -> Dict[str, Any]:
    f_pos = r.choice([30.0, 40.0, 50.0, 60.0])
    f_neg = r.choice([15.0, 20.0, 25.0])
    t1, t2 = 4.0, 6.0
    m = r.choice([2.0, 5.0])
    imp_pos = f_pos * t1
    imp_neg = -f_neg * (t2 - t1)
    imp_total = round(imp_pos + imp_neg, 1)
    vf = round(imp_total / m, 2)
    svg = _svg_ft_bidirectional(f_pos, f_neg, t1, t2)

    prompt = (
        f"Refer to the Force-time graph for an object of mass ${_fmt(m)}\\text{{ kg}}$ initially at rest at $t = 0\\text{{ s}}$.\n\n"
        f"1. Calculate the impulse from $t = 0\\text{{ s}}$ to $t = {_fmt(t1)}\\text{{ s}}$.\n"
        f"2. Calculate the overall impulse over the full ${_fmt(t2)}\\text{{ s}}$ interval.\n"
        f"3. Calculate the final velocity of the object at $t = {_fmt(t2)}\\text{{ s}}$."
    )
    ans = f"J(0-4s) = +{_fmt(imp_pos)} N·s; J_total = +{_fmt(imp_total)} N·s; v_f = {_fmt(vf)} m·s⁻¹"
    sol = (
        f"1. $\\text{{Impulse}}_{{0-4}} = (+{_fmt(f_pos)})(4) = +{_fmt(imp_pos)}\\text{{ N}}\\cdot\\text{{s}}$.\n"
        f"2. $\\text{{Impulse}}_{{4-6}} = (-{_fmt(f_neg)})(2) = {_fmt(imp_neg)}\\text{{ N}}\\cdot\\text{{s}}$.\n"
        f"   $\\text{{Total impulse}} = {_fmt(imp_pos)} + ({_fmt(imp_neg)}) = +{_fmt(imp_total)}\\text{{ N}}\\cdot\\text{{s}}$.\n"
        f"3. $v_f = \\frac{{\\text{{Total impulse}}}}{{m}} = \\frac{{{_fmt(imp_total)}}}{{{_fmt(m)}}} = {_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ in the positive direction."
    )
    return _make_q(
        r, "24_force_time_graph_with_direction_reversal_svg", 24, prompt, ans, sol, 4,
        ["added_area_below_time_axis_as_positive_impulse"],
        [{"step": 1, "criterion": f"Positive area = +{_fmt(imp_pos)} N·s", "marks": 1}, {"step": 2, "criterion": f"Negative area = {_fmt(imp_neg)} N·s subtracted", "marks": 1}, {"step": 3, "criterion": f"Total impulse = +{_fmt(imp_total)} N·s", "marks": 1}, {"step": 4, "criterion": f"Final velocity = {_fmt(vf)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Area above the time axis is positive impulse; area below the time axis is negative impulse.", "tier_2": f"Total impulse = {_fmt(imp_pos)} - {_fmt(abs(imp_neg))} = {_fmt(imp_total)} N·s.", "tier_3": ans},
        svg=svg,
    )


# 25. Momentum and impulse foundations diagnostic autopsy
def build_25_momentum_and_impulse_foundations_diagnostic_autopsy(r: random.Random) -> Dict[str, Any]:
    cases = [
        (
            "Sign omission on rebound velocity",
            "A 0,5 kg ball hits a wall at 10 m·s⁻¹ and rebounds at 8 m·s⁻¹. A learner writes: Δp = m(vf - vi) = 0,5(8 - 10) = -1,0 kg·m·s⁻¹.",
            "Velocity is a vector quantity. Taking towards the wall as positive (+10 m·s⁻¹), the rebound velocity is in the opposite direction (-8 m·s⁻¹). Correct calculation: Δp = 0,5(-8 - 10) = -9,0 kg·m·s⁻¹ (or 9,0 kg·m·s⁻¹ away from the wall)."
        ),
        (
            "Incomplete statement of Newton's Second Law in terms of momentum",
            "When asked to state Newton's Second Law in terms of momentum, a learner writes: 'The resultant force acting on an object is equal to the change in momentum of the object.'",
            "Resultant force is equal to the **rate of change of momentum** (F_net = Δp / Δt), NOT the change in momentum itself. Change in momentum equals impulse (F_net * Δt)."
        ),
        (
            "Gradient vs area confusion on a Force-time graph",
            "To find the impulse delivered over 4 s from a Force-time graph where force increases from 0 N to 80 N, a learner calculates: Impulse = 80 / 4 = 20 N·s.",
            "The learner calculated the gradient (rate of change of force) instead of the area under the Force-time graph. Impulse is the area under the F-t graph: Area = 0,5 * 4 * 80 = 160 N·s."
        ),
    ]
    title, err_desc, fix = r.choice(cases)
    prompt = (
        f"**Diagnostic Autopsy:** Analyse the following common Grade 12 learner error in Momentum & Impulse:\n\n"
        f"**Learner's Work:** {err_desc}\n\n"
        f"1. Identify the specific physical misconception made by the learner.\n"
        f"2. Provide the corrected physical statement or calculation."
    )
    ans = fix
    sol = f"1. **Misconception:** {title}.\n2. **Correction:** {fix}"
    return _make_q(
        r, "25_momentum_and_impulse_foundations_diagnostic_autopsy", 25, prompt, ans, sol, 3,
        ["rebound_vector_sign_omission", "omitted_rate_of_in_newtons_second_law"],
        [{"step": 1, "criterion": f"Identified misconception: {title}", "marks": 1}, {"step": 2, "criterion": "Physical principle explained", "marks": 1}, {"step": 3, "criterion": "Corrected solution provided", "marks": 1}],
        {"tier_1": "Check vector direction signs, definitions of rate vs change, and area vs gradient.", "tier_2": f"Focus on: {title}.", "tier_3": ans},
    )


BUILDERS_01_25 = {
    "01_definition_and_vector_nature_of_momentum": build_01_definition_and_vector_nature_of_momentum,
    "02_linear_momentum_direct_calculation": build_02_linear_momentum_direct_calculation,
    "03_linear_momentum_with_gram_to_kg_conversion": build_03_linear_momentum_with_gram_to_kg_conversion,
    "04_linear_momentum_with_kmh_to_ms_conversion": build_04_linear_momentum_with_kmh_to_ms_conversion,
    "05_solving_for_mass_or_velocity_from_momentum": build_05_solving_for_mass_or_velocity_from_momentum,
    "06_comparing_momenta_of_different_objects": build_06_comparing_momenta_of_different_objects,
    "07_momentum_and_kinetic_energy_relationship": build_07_momentum_and_kinetic_energy_relationship,
    "08_momentum_scaling_when_mass_or_velocity_changes": build_08_momentum_scaling_when_mass_or_velocity_changes,
    "09_change_in_momentum_same_direction_speed_increase": build_09_change_in_momentum_same_direction_speed_increase,
    "10_change_in_momentum_same_direction_braking": build_10_change_in_momentum_same_direction_braking,
    "11_change_in_momentum_rebound_opposite_direction": build_11_change_in_momentum_rebound_opposite_direction,
    "12_vector_diagram_for_change_in_momentum_svg": build_12_vector_diagram_for_change_in_momentum_svg,
    "13_vertical_bounce_change_in_momentum": build_13_vertical_bounce_change_in_momentum,
    "14_newtons_second_law_in_terms_of_momentum_statement": build_14_newtons_second_law_in_terms_of_momentum_statement,
    "15_resultant_force_from_rate_of_change_of_momentum": build_15_resultant_force_from_rate_of_change_of_momentum,
    "16_contact_time_from_resultant_force_and_momentum_change": build_16_contact_time_from_resultant_force_and_momentum_change,
    "17_final_velocity_from_resultant_force_and_contact_time": build_17_final_velocity_from_resultant_force_and_contact_time,
    "18_impulse_definition_and_units_equivalence": build_18_impulse_definition_and_units_equivalence,
    "19_impulse_from_constant_force_and_contact_time": build_19_impulse_from_constant_force_and_contact_time,
    "20_impulse_momentum_theorem_ball_struck_by_bat": build_20_impulse_momentum_theorem_ball_struck_by_bat,
    "21_force_time_graph_rectangular_area_impulse_svg": build_21_force_time_graph_rectangular_area_impulse_svg,
    "22_force_time_graph_triangular_peak_force_svg": build_22_force_time_graph_triangular_peak_force_svg,
    "23_force_time_graph_trapezoidal_velocity_change_svg": build_23_force_time_graph_trapezoidal_velocity_change_svg,
    "24_force_time_graph_with_direction_reversal_svg": build_24_force_time_graph_with_direction_reversal_svg,
    "25_momentum_and_impulse_foundations_diagnostic_autopsy": build_25_momentum_and_impulse_foundations_diagnostic_autopsy,
}
