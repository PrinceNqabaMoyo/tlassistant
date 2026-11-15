"""Grade 11 Mathematics — Linear Programming & Investigations (Archetypes 01 to 25).
 aligned with South African National Curriculum Standards.
Reference: curriculum_docs_auto/Mathematics_Gr11/Term 1/01. Linear programming.md

Covers:
- Formulating linear inequality constraints and objective functions from word contexts (01..10)
- Graphing linear inequalities, boundary lines, feasible regions, and corner vertices (11..25)
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple


def _fmt(val: float, decimals: int = 2) -> str:
    rounded = round(val, decimals)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _svg_lp_quad_region(
    y_int_1: int,
    x_int_1: int,
    y_int_2: int,
    x_int_2: int,
    ix: int,
    iy: int,
    title: str = "Feasible Region S",
    search_m: Optional[ Tuple[int, int] ] = None,
) -> str:
    """Dynamic Cartesian plane SVG showing first-quadrant feasible region with two intersecting constraints."""
    max_x = max(x_int_1, x_int_2, ix + 2, 10)
    max_y = max(y_int_1, y_int_2, iy + 2, 10)
    ox, oy = 60, 220
    pw, ph = 260, 175

    def tx(x: float) -> float:
        return round(ox + (x / max_x) * pw, 1)

    def ty(y: float) -> float:
        return round(oy - (y / max_y) * ph, 1)

    # Polygon vertices: (0,0) -> (0, min(y_int_1, y_int_2)) -> (ix, iy) -> (min(x_int_1, x_int_2), 0)
    top_y = min(y_int_1, y_int_2)
    right_x = min(x_int_1, x_int_2)
    pts = f"{tx(0)},{ty(0)} {tx(0)},{ty(top_y)} {tx(ix)},{ty(iy)} {tx(right_x)},{ty(0)}"

    search_svg = ""
    if search_m is not None:
        px, py = search_m
        # Draw dashed search line passing near (ix, iy)
        x_s1 = max(0.0, ix - 3.0)
        y_s1 = iy + (px / max(py, 1)) * (ix - x_s1)
        x_s2 = min(float(max_x), ix + 3.0)
        y_s2 = max(0.0, iy - (px / max(py, 1)) * (x_s2 - ix))
        search_svg = (
            f'<line x1="{tx(x_s1)}" y1="{ty(y_s1)}" x2="{tx(x_s2)}" y2="{ty(y_s2)}" '
            f'stroke="#dc2626" stroke-width="2" stroke-dasharray="5,4"/>'
            f'<text x="{tx(x_s2) + 4}" y="{ty(y_s2)}" font-size="10" fill="#dc2626">Search line</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 265" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="20" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">{title}</text>'
        f'<line x1="{ox}" y1="30" x2="{ox}" y2="{oy}" stroke="#334155" stroke-width="1.8"/>'
        f'<line x1="{ox}" y1="{oy}" x2="{ox + pw + 15}" y2="{oy}" stroke="#334155" stroke-width="1.8"/>'
        f'<polygon points="{pts}" fill="#bfdbfe" fill-opacity="0.55" stroke="#1d4ed8" stroke-width="1.5"/>'
        f'<line x1="{tx(0)}" y1="{ty(y_int_1)}" x2="{tx(x_int_1)}" y2="{ty(0)}" stroke="#2563eb" stroke-width="1.8"/>'
        f'<line x1="{tx(0)}" y1="{ty(y_int_2)}" x2="{tx(x_int_2)}" y2="{ty(0)}" stroke="#0d9488" stroke-width="1.8"/>'
        f'{search_svg}'
        f'<circle cx="{tx(0)}" cy="{ty(top_y)}" r="3.5" fill="#1e3a8a"/>'
        f'<text x="{tx(0) - 8}" y="{ty(top_y) + 4}" text-anchor="end" font-size="10" fill="#1e3a8a">(0; {top_y})</text>'
        f'<circle cx="{tx(ix)}" cy="{ty(iy)}" r="4" fill="#dc2626"/>'
        f'<text x="{tx(ix) + 6}" y="{ty(iy) - 5}" font-size="10" font-weight="bold" fill="#991b1b">({ix}; {iy})</text>'
        f'<circle cx="{tx(right_x)}" cy="{ty(0)}" r="3.5" fill="#1e3a8a"/>'
        f'<text x="{tx(right_x)}" y="{ty(0) + 15}" text-anchor="middle" font-size="10" fill="#1e3a8a">({right_x}; 0)</text>'
        f'<text x="{ox - 10}" y="{oy + 14}" font-size="10" fill="#475569">O(0;0)</text>'
        f'<text x="{ox + pw + 10}" y="{oy + 15}" font-size="11" font-weight="bold" fill="#1e293b">x</text>'
        f'<text x="{ox - 15}" y="38" font-size="11" font-weight="bold" fill="#1e293b">y</text>'
        f'</svg>'
    )


def _svg_single_line_region(
    a: int,
    b: int,
    c: int,
    shade_below: bool = True,
    dashed: bool = False,
    test_pt: Optional[Tuple[int, int]] = None,
) -> str:
    """Dynamic Cartesian plane SVG for a single linear inequality boundary ax + by <= c or >= c."""
    x_int = round(c / a, 2)
    y_int = round(c / b, 2)
    max_x = max(x_int * 1.25, 10)
    max_y = max(y_int * 1.25, 10)
    ox, oy = 60, 215
    pw, ph = 250, 170

    def tx(x: float) -> float:
        return round(ox + (x / max_x) * pw, 1)

    def ty(y: float) -> float:
        return round(oy - (y / max_y) * ph, 1)

    if shade_below:
        poly = f"{tx(0)},{ty(0)} {tx(0)},{ty(y_int)} {tx(x_int)},{ty(0)}"
    else:
        poly = f"{tx(0)},{ty(y_int)} {tx(0)},{ty(max_y)} {tx(max_x)},{ty(max_y)} {tx(max_x)},{ty(0)} {tx(x_int)},{ty(0)}"

    dash_attr = ' stroke-dasharray="6,4"' if dashed else ""
    pt_svg = ""
    if test_pt is not None:
        px, py = test_pt
        pt_svg = (
            f'<circle cx="{tx(px)}" cy="{ty(py)}" r="4" fill="#dc2626"/>'
            f'<text x="{tx(px) + 6}" y="{ty(py) - 5}" font-size="10" font-weight="bold" fill="#991b1b">P({px}; {py})</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 370 255" width="100%" style="max-width:370px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<polygon points="{poly}" fill="#dcfce7" fill-opacity="0.65"/>'
        f'<line x1="{ox}" y1="25" x2="{ox}" y2="{oy}" stroke="#334155" stroke-width="1.8"/>'
        f'<line x1="{ox}" y1="{oy}" x2="{ox + pw + 15}" y2="{oy}" stroke="#334155" stroke-width="1.8"/>'
        f'<line x1="{tx(0)}" y1="{ty(y_int)}" x2="{tx(x_int)}" y2="{ty(0)}" stroke="#16a34a" stroke-width="2.2"{dash_attr}/>'
        f'<circle cx="{tx(0)}" cy="{ty(y_int)}" r="3.5" fill="#15803d"/>'
        f'<text x="{tx(0) - 6}" y="{ty(y_int) + 4}" text-anchor="end" font-size="10" fill="#15803d">(0; {_fmt(y_int)})</text>'
        f'<circle cx="{tx(x_int)}" cy="{ty(0)}" r="3.5" fill="#15803d"/>'
        f'<text x="{tx(x_int)}" y="{ty(0) + 15}" text-anchor="middle" font-size="10" fill="#15803d">({_fmt(x_int)}; 0)</text>'
        f'{pt_svg}'
        f'<text x="{ox + pw + 10}" y="{oy + 14}" font-size="11" font-weight="bold" fill="#1e293b">x</text>'
        f'<text x="{ox - 14}" y="34" font-size="11" font-weight="bold" fill="#1e293b">y</text>'
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
    q_id = f"g11_lp_{idx:02d}_{r.randint(100000, 999999)}"
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
        "topic": "Linear programming",
        "subskill": subskill,
        "archetype_id": subskill,
        "question_type": "numeric_input",
        "modality": "math_steps",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": correct_answer,
        "sample_answer": solution_text,
        "solution": solution_text,
        "explanation": solution_text,
        "marks": marks,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "learning_objective_id": f"g11_lp_{subskill}",
        "mode": subskill,
        "misconception_tags": tags,
        "Rubric": rubric,
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
            "height": 265,
        }
    return out


# 01. Translate 'at most' and 'maximum' resource constraint
def build_01_translate_at_most_and_maximum_resource_constraint(r: random.Random) -> Dict[str, Any]:
    hrs_x = r.randint(2, 6)
    hrs_y = r.randint(3, 8)
    max_hrs = r.randint(60, 180)
    prompt = (
        f"A carpentry workshop manufactures standard tables ($x$) and deluxe cabinets ($y$).\n"
        f"• Each table requires ${hrs_x}\\text{{ hours}}$ of cutting time.\n"
        f"• Each cabinet requires ${hrs_y}\\text{{ hours}}$ of cutting time.\n"
        f"• The cutting machine is available for **at most** ${max_hrs}\\text{{ hours}}$ per week.\n\n"
        f"Write down the linear inequality in terms of $x$ and $y$ that represents the cutting time constraint."
    )
    ans = f"{hrs_x}x + {hrs_y}y \\le {max_hrs}"
    sol = f"Total cutting time is ${hrs_x}x + {hrs_y}y$. Since 'at most ${max_hrs}$' means less than or equal to ${max_hrs}$, the constraint is ${ans}$."
    return _make_q(
        r, "01_translate_at_most_and_maximum_resource_constraint", 1, prompt, ans, sol, 2,
        ["inequality_direction_inversion", "used_strict_less_than_instead_of_less_equal"],
        [{"step": 1, "criterion": f"Expression {hrs_x}x + {hrs_y}y", "marks": 1}, {"step": 2, "criterion": f"Inequality <= {max_hrs}", "marks": 1}],
        {"tier_1": "Multiply the hours per item by the number of items and sum them.", "tier_2": "'At most' translates to '<='.", "tier_3": ans},
    )


# 02. Translate 'at least' and 'minimum' demand constraint
def build_02_translate_at_least_and_minimum_demand_constraint(r: random.Random) -> Dict[str, Any]:
    min_x = r.randint(12, 35)
    min_total = min_x + r.randint(25, 60)
    prompt = (
        f"A bakery bakes rye loaves ($x$) and sourdough loaves ($y$) each morning.\n"
        f"• Standing café orders require **at least** ${min_x}$ rye loaves.\n"
        f"• The total number of loaves baked must be **no fewer than** ${min_total}$.\n\n"
        f"Write down the two linear inequalities representing these minimum demand conditions."
    )
    ans = f"x \\ge {min_x},\\quad x + y \\ge {min_total}"
    sol = f"'At least ${min_x}$' gives $x \\ge {min_x}$, and 'no fewer than ${min_total}$ in total' gives $x + y \\ge {min_total}$."
    return _make_q(
        r, "02_translate_at_least_and_minimum_demand_constraint", 2, prompt, ans, sol, 2,
        ["reversed_at_least_inequality_sign"],
        [{"step": 1, "criterion": f"x >= {min_x}", "marks": 1}, {"step": 2, "criterion": f"x + y >= {min_total}", "marks": 1}],
        {"tier_1": "Both 'at least' and 'no fewer than' mean greater than or equal to (>=).", "tier_2": f"First condition: x >= {min_x}. Second condition: x + y >= {min_total}.", "tier_3": ans},
    )


# 03. Translate ratio and proportional production constraint
def build_03_translate_ratio_and_proportional_production_constraint(r: random.Random) -> Dict[str, Any]:
    m_v = r.randint(2, 5)
    n_v = r.choice([p for p in [2, 3, 4, 5] if p != m_v])
    prompt = (
        f"A paint factory blends base coat ($x$ litres) and hardener ($y$ litres).\n"
        f"For quality control, the ratio of base coat to hardener ($x : y$) must be **at least** ${m_v} : {n_v}$.\n\n"
        f"Write this constraint as a linear inequality without fractions, and express $y$ in terms of $x$."
    )
    ans = f"{n_v}x \\ge {m_v}y \\implies y \\le \\frac{{{n_v}}}{{{m_v}}}x"
    sol = f"$\\frac{{x}}{{y}} \\ge \\frac{{{m_v}}}{{{n_v}}} \\implies {n_v}x \\ge {m_v}y$, or equivalently $y \\le \\frac{{{n_v}}}{{{m_v}}}x$."
    return _make_q(
        r, "03_translate_ratio_and_proportional_production_constraint", 3, prompt, ans, sol, 3,
        ["swapped_ratio_coefficients_between_x_and_y"],
        [{"step": 1, "criterion": f"x/y >= {m_v}/{n_v}", "marks": 1}, {"step": 2, "criterion": f"{n_v}x >= {m_v}y", "marks": 1}, {"step": 3, "criterion": f"y <= ({n_v}/{m_v})x", "marks": 1}],
        {"tier_1": f"Write the ratio as a fraction: x / y >= {m_v} / {n_v} (since x, y > 0).", "tier_2": f"Cross-multiply by positive quantities: {n_v}x >= {m_v}y.", "tier_3": ans},
    )


# 04. Translate 'at least k times as many y as x' constraint
def build_04_translate_at_least_twice_as_many_y_as_x_constraint(r: random.Random) -> Dict[str, Any]:
    k_factor = r.randint(2, 6)
    max_diff = r.randint(10, 30)
    prompt = (
        f"A school sports department orders netballs ($x$) and soccer balls ($y$).\n"
        f"• The number of soccer balls ($y$) must be **at least ${k_factor}$ times** the number of netballs ($x$).\n"
        f"• The number of soccer balls may **not exceed** the number of netballs by more than ${max_diff}$.\n\n"
        f"Write down the two inequalities in terms of $x$ and $y$."
    )
    ans = f"y \\ge {k_factor}x,\\quad y - x \\le {max_diff}"
    sol = f"1) 'At least ${k_factor}$ times as many $y$ as $x$' means $y \\ge {k_factor}x$.\n2) '$y$ exceeds $x$ by at most ${max_diff}$' means $y - x \\le {max_diff}$ (or $y \\le x + {max_diff}$)."
    return _make_q(
        r, "04_translate_at_least_twice_as_many_y_as_x_constraint", 4, prompt, ans, sol, 3,
        ["multiplied_wrong_variable_by_k_in_word_translation"],
        [{"step": 1, "criterion": f"y >= {k_factor}x", "marks": 2}, {"step": 2, "criterion": f"y - x <= {max_diff}", "marks": 1}],
        {"tier_1": f"Test with numbers: if x = 10, then y must be at least {10 * k_factor}, so y >= {k_factor}x.", "tier_2": f"Difference condition: y - x <= {max_diff}.", "tier_3": ans},
    )


# 05. Implicit non-negativity and integer domain constraints
def build_05_implicit_non_negativity_and_integer_domain_constraints(r: random.Random) -> Dict[str, Any]:
    cap_x = r.randint(15, 45)
    cap_y = r.randint(20, 50)
    prompt = (
        f"An electronics plant assembles $x$ laptops and $y$ tablets per shift, with daily assembly caps of "
        f"${cap_x}$ laptops and ${cap_y}$ tablets.\n\n"
        f"State the complete bounded domain inequalities for $x$ and $y$ as well as the number-system restriction required because partial devices cannot be sold."
    )
    ans = f"0 \\le x \\le {cap_x},\\quad 0 \\le y \\le {cap_y},\\quad x, y \\in \\mathbb{{Z}}_0^+"
    sol = f"Since negative quantities cannot be produced, $0 \\le x \\le {cap_x}$ and $0 \\le y \\le {cap_y}$ with $x, y \\in \\mathbb{{N}}_0$ (whole numbers / non-negative integers)."
    return _make_q(
        r, "05_implicit_non_negativity_and_integer_domain_constraints", 5, prompt, ans, sol, 2,
        ["omitted_non_negativity_constraints", "forgot_integer_domain_restriction"],
        [{"step": 1, "criterion": f"0 <= x <= {cap_x} and 0 <= y <= {cap_y}", "marks": 1}, {"step": 2, "criterion": "Integer restriction x, y in Z", "marks": 1}],
        {"tier_1": "Physical items cannot be negative, so x >= 0 and y >= 0.", "tier_2": "Include the upper bounds and specify that x and y must be whole numbers (integers).", "tier_3": ans},
    )


# 06. Formulate two-resource manufacturing system from table
def build_06_formulate_two_resource_manufacturing_system_from_table(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(2, 5)
    b1 = r.randint(3, 6)
    tot1 = r.randint(60, 120)
    a2 = r.randint(1, 4)
    b2 = r.randint(2, 5)
    tot2 = r.randint(40, 90)
    prompt = (
        f"A garment factory produces jackets ($x$) and trousers ($y$). The resource requirements per item are:\n\n"
        f"| Department | Jacket ($x$) | Trousers ($y$) | Maximum Daily Hours |\n"
        f"| :--- | :---: | :---: | :---: |\n"
        f"| Cutting | ${a1}\\text{{ h}}$ | ${b1}\\text{{ h}}$ | ${tot1}\\text{{ h}}$ |\n"
        f"| Stitching | ${a2}\\text{{ h}}$ | ${b2}\\text{{ h}}$ | ${tot2}\\text{{ h}}$ |\n\n"
        f"Write down the two department constraint inequalities in terms of $x$ and $y$."
    )
    ans = f"{a1}x + {b1}y \\le {tot1},\\quad {a2}x + {b2}y \\le {tot2}"
    sol = f"Cutting constraint: ${a1}x + {b1}y \\le {tot1}$.\nStitching constraint: ${a2}x + {b2}y \\le {tot2}$."
    return _make_q(
        r, "06_formulate_two_resource_manufacturing_system_from_table", 6, prompt, ans, sol, 3,
        ["mixed_up_rows_and_columns_when_reading_resource_table"],
        [{"step": 1, "criterion": f"Cutting: {a1}x + {b1}y <= {tot1}", "marks": 1}, {"step": 2, "criterion": f"Stitching: {a2}x + {b2}y <= {tot2}", "marks": 2}],
        {"tier_1": "Read across each row of the table to form one constraint inequality.", "tier_2": f"Row 1 gives {a1}x + {b1}y <= {tot1}; Row 2 gives {a2}x + {b2}y <= {tot2}.", "tier_3": ans},
    )


# 07. Formulate dietary and nutritional minimum constraints
def build_07_formulate_dietary_and_nutritional_minimum_constraints(r: random.Random) -> Dict[str, Any]:
    p_x = r.randint(10, 25)
    p_y = r.randint(15, 30)
    min_p = r.randint(120, 240)
    c_x = r.randint(20, 40)
    c_y = r.randint(10, 25)
    min_c = r.randint(150, 300)
    prompt = (
        f"A dietitian blends Scoop A ($x$) and Scoop B ($y$) to prepare a recovery meal.\n"
        f"• Scoop A contains ${p_x}\\text{{ g}}$ of protein and ${c_x}\\text{{ g}}$ of carbohydrates.\n"
        f"• Scoop B contains ${p_y}\\text{{ g}}$ of protein and ${c_y}\\text{{ g}}$ of carbohydrates.\n"
        f"• The meal must supply **at least** ${min_p}\\text{{ g}}$ of protein and **at least** ${min_c}\\text{{ g}}$ of carbohydrates.\n\n"
        f"Write down the protein and carbohydrate constraint inequalities."
    )
    ans = f"{p_x}x + {p_y}y \\ge {min_p},\\quad {c_x}x + {c_y}y \\ge {min_c}"
    sol = f"Protein: ${p_x}x + {p_y}y \\ge {min_p}$. Carbohydrates: ${c_x}x + {c_y}y \\ge {min_c}$."
    return _make_q(
        r, "07_formulate_dietary_and_nutritional_minimum_constraints", 7, prompt, ans, sol, 3,
        ["used_less_equal_for_minimum_nutritional_requirement"],
        [{"step": 1, "criterion": f"Protein: {p_x}x + {p_y}y >= {min_p}", "marks": 1}, {"step": 2, "criterion": f"Carbohydrate: {c_x}x + {c_y}y >= {min_c}", "marks": 2}],
        {"tier_1": "Group the protein amounts together for the first inequality and carbohydrate amounts for the second.", "tier_2": "'At least' means >= for both nutritional requirements.", "tier_3": ans},
    )


# 08. Formulate transport fleet capacity and budget constraints
def build_08_formulate_transport_fleet_capacity_and_budget_constraints(r: random.Random) -> Dict[str, Any]:
    cap_x = r.choice([14, 16, 20])
    cap_y = r.choice([45, 50, 60])
    learners = r.randint(240, 420)
    drivers = r.randint(9, 15)
    prompt = (
        f"A school hires $x$ minibuses (each seating ${cap_x}$ learners) and $y$ luxury coaches (each seating ${cap_y}$ learners) "
        f"to transport **at least** ${learners}$ learners.\n"
        f"Only ${drivers}$ qualified drivers are available (each vehicle requires $1$ driver).\n\n"
        f"Write down the seating capacity inequality and the driver availability inequality."
    )
    ans = f"{cap_x}x + {cap_y}y \\ge {learners},\\quad x + y \\le {drivers}"
    sol = f"Seating capacity (at least ${learners}$ learners): ${cap_x}x + {cap_y}y \\ge {learners}$.\nDriver availability (at most ${drivers}$ drivers): $x + y \\le {drivers}$."
    return _make_q(
        r, "08_formulate_transport_fleet_capacity_and_budget_constraints", 8, prompt, ans, sol, 3,
        ["used_same_inequality_sign_for_both_minimum_passengers_and_maximum_drivers"],
        [{"step": 1, "criterion": f"Capacity: {cap_x}x + {cap_y}y >= {learners}", "marks": 2}, {"step": 2, "criterion": f"Drivers: x + y <= {drivers}", "marks": 1}],
        {"tier_1": "Total seats must be >= learners; total vehicles must be <= drivers.", "tier_2": f"Seats: {cap_x}x + {cap_y}y >= {learners}. Vehicles: x + y <= {drivers}.", "tier_3": ans},
    )


# 09. Formulate agricultural land, water and labour constraints
def build_09_formulate_agricultural_land_water_and_labour_constraints(r: random.Random) -> Dict[str, Any]:
    land = r.randint(50, 120)
    w_x = r.randint(3, 6)
    w_y = r.randint(4, 8)
    max_w = r.randint(250, 500)
    prompt = (
        f"A farmer in the Free State plants $x$ hectares of maize and $y$ hectares of sunflowers on a farm of **at most** ${land}$ hectares.\n"
        f"Each hectare of maize requires ${w_x}\\text{{ ML}}$ of irrigation water, and each hectare of sunflowers requires ${w_y}\\text{{ ML}}$. "
        f"The irrigation quota is ${max_w}\\text{{ ML}}$.\n\n"
        f"Write down the land constraint and the water constraint in simplified form."
    )
    ans = f"x + y \\le {land},\\quad {w_x}x + {w_y}y \\le {max_w}"
    sol = f"Total land: $x + y \\le {land}$. Total irrigation water: ${w_x}x + {w_y}y \\le {max_w}$."
    return _make_q(
        r, "09_formulate_agricultural_land_water_and_labour_constraints", 9, prompt, ans, sol, 2,
        ["combined_hectares_and_water_into_single_inequality"],
        [{"step": 1, "criterion": f"Land: x + y <= {land}", "marks": 1}, {"step": 2, "criterion": f"Water: {w_x}x + {w_y}y <= {max_w}", "marks": 1}],
        {"tier_1": "Keep hectares and megalitres in separate constraint inequalities.", "tier_2": f"Land: x + y <= {land}. Water: {w_x}x + {w_y}y <= {max_w}.", "tier_3": ans},
    )


# 10. Formulate objective function for profit, revenue or cost
def build_10_formulate_objective_function_for_profit_revenue_or_cost(r: random.Random) -> Dict[str, Any]:
    rev_x = r.randint(40, 90) * 10
    cost_x = r.randint(15, 35) * 10
    rev_y = r.randint(60, 120) * 10
    cost_y = r.randint(25, 50) * 10
    net_x = rev_x - cost_x
    net_y = rev_y - cost_y
    prompt = (
        f"A workshop sells $x$ bookshelves at $\\text{{R }}{rev_x}$ each (production cost $\\text{{R }}{cost_x}$ each) "
        f"and $y$ study desks at $\\text{{R }}{rev_y}$ each (production cost $\\text{{R }}{cost_y}$ each).\n\n"
        f"Write down the simplified **net profit objective function** $P$ in terms of $x$ and $y$, and express $y$ as the subject of the formula."
    )
    ans = f"P = {net_x}x + {net_y}y,\\quad y = -\\frac{{{net_x}}}{{{net_y}}}x + \\frac{{P}}{{{net_y}}}"
    sol = (
        f"Net profit per bookshelf $= {rev_x} - {cost_x} = \\text{{R }}{net_x}$. "
        f"Net profit per desk $= {rev_y} - {cost_y} = \\text{{R }}{net_y}$.\n"
        f"Thus $P = {net_x}x + {net_y}y \\implies y = -\\frac{{{net_x}}}{{{net_y}}}x + \\frac{{P}}{{{net_y}}}$."
    )
    return _make_q(
        r, "10_formulate_objective_function_for_profit_revenue_or_cost", 10, prompt, ans, sol, 3,
        ["used_selling_price_instead_of_net_profit", "included_inequality_sign_in_objective_function"],
        [{"step": 1, "criterion": f"Unit profits R{net_x} and R{net_y}", "marks": 1}, {"step": 2, "criterion": f"P = {net_x}x + {net_y}y", "marks": 1}, {"step": 3, "criterion": "Subject y isolated", "marks": 1}],
        {"tier_1": "Profit = Selling Price - Production Cost for each item.", "tier_2": f"P = {net_x}x + {net_y}y. Rearrange to isolate y.", "tier_3": ans},
    )


# 11. x- and y-intercepts of constraint boundary line (with SVG)
def build_11_x_and_y_intercepts_of_constraint_boundary_line_svg(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(2, 6)
    b_v = r.randint(3, 8)
    mult = r.randint(2, 5)
    c_v = a_v * b_v * mult
    x_int = c_v // a_v
    y_int = c_v // b_v
    svg = _svg_single_line_region(a_v, b_v, c_v, shade_below=True)
    prompt = (
        f"The boundary line for the constraint ${a_v}x + {b_v}y \\le {c_v}$ in the first quadrant is shown in the diagram.\n\n"
        f"Determine the exact coordinates of the $x$-intercept and the $y$-intercept of the boundary line ${a_v}x + {b_v}y = {c_v}$."
    )
    ans = f"({x_int}; 0) \\text{{ and }} (0; {y_int})"
    sol = f"For $x$-intercept ($y = 0$): ${a_v}x = {c_v} \\implies x = {x_int} \\implies ({x_int}; 0)$.\nFor $y$-intercept ($x = 0$): ${b_v}y = {c_v} \\implies y = {y_int} \\implies (0; {y_int})$."
    return _make_q(
        r, "11_x_and_y_intercepts_of_constraint_boundary_line_svg", 11, prompt, ans, sol, 2,
        ["intercept_inversion_x_y"],
        [{"step": 1, "criterion": f"x-intercept ({x_int}; 0)", "marks": 1}, {"step": 2, "criterion": f"y-intercept (0; {y_int})", "marks": 1}],
        {"tier_1": "Set y = 0 to find the x-intercept and x = 0 to find the y-intercept.", "tier_2": f"{a_v}x = {c_v} => x = {x_int}; {b_v}y = {c_v} => y = {y_int}.", "tier_3": ans},
        svg=svg,
    )


# 12. Gradient-intercept form of constraint inequality
def build_12_gradient_intercept_form_of_constraint_inequality(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(2, 9)
    b_v = r.randint(2, 7)
    c_v = b_v * r.randint(5, 15)
    y_int = c_v // b_v
    prompt = (
        f"Rewrite the linear constraint inequality ${a_v}x + {b_v}y \\le {c_v}$ in gradient-intercept form ($y \\le mx + c$), "
        f"and state the gradient $m$ and $y$-intercept $c$ of its boundary line."
    )
    ans = f"y \\le -\\frac{{{a_v}}}{{{b_v}}}x + {y_int},\\quad m = -\\frac{{{a_v}}}{{{b_v}}},\\quad c = {y_int}"
    sol = f"${b_v}y \\le -{a_v}x + {c_v} \\implies y \\le -\\frac{{{a_v}}}{{{b_v}}}x + {y_int}$. Thus $m = -\\frac{{{a_v}}}{{{b_v}}}$ and $c = {y_int}$."
    return _make_q(
        r, "12_gradient_intercept_form_of_constraint_inequality", 12, prompt, ans, sol, 3,
        ["sign_error_when_transposing_ax_term"],
        [{"step": 1, "criterion": f"Transpose {a_v}x to get -{a_v}x", "marks": 1}, {"step": 2, "criterion": f"Divide by {b_v}", "marks": 1}, {"step": 3, "criterion": f"m = -{a_v}/{b_v}, c = {y_int}", "marks": 1}],
        {"tier_1": f"Subtract {a_v}x from both sides, then divide every term by {b_v}.", "tier_2": f"{b_v}y <= -{a_v}x + {c_v}.", "tier_3": ans},
    )


# 13. Identify half-plane shading above or below boundary (with SVG)
def build_13_identify_half_plane_shading_above_or_below_boundary_svg(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(2, 5)
    b_v = r.randint(2, 6)
    c_v = a_v * b_v * r.randint(2, 4)
    shade_below = r.choice([True, False])
    sym = "\\le" if shade_below else "\\ge"
    word = "on and below (including the origin)" if shade_below else "on and above (away from the origin)"
    svg = _svg_single_line_region(a_v, b_v, c_v, shade_below=shade_below)
    prompt = (
        f"Consider the graphed inequality ${a_v}x + {b_v}y {sym} {c_v}$ ($x \\ge 0, y \\ge 0$) shown in the diagram.\n\n"
        f"Test the origin $(0; 0)$ in the inequality and state whether the feasible half-plane lies **on and below** or **on and above** the boundary line."
    )
    ans = f"{word}"
    sol = (
        f"Substituting $(0; 0)$ gives $0 {sym} {c_v}$, which is {'TRUE' if shade_below else 'FALSE'}. "
        f"Hence the feasible region lies **{word}** the boundary line."
    )
    return _make_q(
        r, "13_identify_half_plane_shading_above_or_below_boundary_svg", 13, prompt, ans, sol, 2,
        ["shaded_wrong_side_of_boundary_line"],
        [{"step": 1, "criterion": "Test (0; 0)", "marks": 1}, {"step": 2, "criterion": f"Region is {word}", "marks": 1}],
        {"tier_1": "Substitute (0; 0) into the left-hand side of the inequality.", "tier_2": f"0 <= {c_v} is true (shade towards origin); 0 >= {c_v} is false (shade away from origin).", "tier_3": ans},
        svg=svg,
    )


# 14. Solid vs dashed boundary line and strict inequality
def build_14_solid_vs_dashed_boundary_line_and_strict_inequality(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(2, 6)
    b_v = r.randint(3, 7)
    c_v = a_v * b_v * r.randint(2, 4)
    svg = _svg_single_line_region(a_v, b_v, c_v, shade_below=True, dashed=True)
    prompt = (
        f"Refer to the graphed region in the diagram, where the boundary line through $(0; {c_v // b_v})$ and $({c_v // a_v}; 0)$ is drawn as a **dashed** line.\n\n"
        f"Write down the strict linear inequality represented by this region in the first quadrant, and state whether points on the boundary line are included."
    )
    ans = f"{a_v}x + {b_v}y < {c_v}\\text{{ (boundary excluded because inequality is strict)}}"
    sol = f"Line equation: ${a_v}x + {b_v}y = {c_v}$. Since the boundary line is dashed and the region lies below it, the strict inequality is ${a_v}x + {b_v}y < {c_v}$ (points on the line do not satisfy $<$)."
    return _make_q(
        r, "14_solid_vs_dashed_boundary_line_and_strict_inequality", 14, prompt, ans, sol, 2,
        ["used_non_strict_inequality_for_dashed_boundary_line"],
        [{"step": 1, "criterion": f"Strict inequality {a_v}x + {b_v}y < {c_v}", "marks": 1}, {"step": 2, "criterion": "Dashed line excludes boundary points", "marks": 1}],
        {"tier_1": "A dashed boundary line indicates a strict inequality (< or >).", "tier_2": f"Using intercepts ({c_v // a_v}; 0) and (0; {c_v // b_v}), the line is {a_v}x + {b_v}y = {c_v}.", "tier_3": ans},
        svg=svg,
    )


# 15. Verify whether candidate point lies in feasible region (with SVG)
def build_15_verify_whether_candidate_point_lies_in_feasible_region_svg(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(2, 5)
    b_v = r.randint(2, 5)
    c_v = a_v * b_v * r.randint(3, 5)
    px = r.randint(2, 8)
    py = r.randint(2, 8)
    lhs = a_v * px + b_v * py
    is_feasible = lhs <= c_v
    status = "Feasible" if is_feasible else "Not feasible"
    svg = _svg_single_line_region(a_v, b_v, c_v, shade_below=True, test_pt=(px, py))
    prompt = (
        f"A feasible region is defined by ${a_v}x + {b_v}y \\le {c_v}$ with $x \\ge 0, y \\ge 0$, as shown in the diagram.\n\n"
        f"By algebraic substitution, determine whether the candidate point $P({px}; {py})$ is **Feasible** or **Not feasible**."
    )
    ans = f"{status} (\\text{{LHS}} = {lhs} {'\\le' if is_feasible else '>'} {c_v})"
    sol = f"Substitute $P({px}; {py})$: ${a_v}({px}) + {b_v}({py}) = {a_v * px} + {b_v * py} = {lhs}$. Compare with ${c_v}$: ${lhs} {'\\le' if is_feasible else '>'} {c_v}$, so $P$ is **{status}**."
    return _make_q(
        r, "15_verify_whether_candidate_point_lies_in_feasible_region_svg", 15, prompt, ans, sol, 3,
        ["guessed_feasibility_visually_without_algebraic_substitution"],
        [{"step": 1, "criterion": f"Substitute ({px}; {py}) -> LHS = {lhs}", "marks": 2}, {"step": 2, "criterion": f"Conclusion: {status}", "marks": 1}],
        {"tier_1": f"Calculate {a_v}*({px}) + {b_v}*({py}) and compare the result with {c_v}.", "tier_2": f"LHS = {lhs}, RHS = {c_v}.", "tier_3": ans},
        svg=svg,
    )


# 16. Determine inequality from graphed boundary line (with SVG)
def build_16_determine_inequality_from_graphed_boundary_line_svg(r: random.Random) -> Dict[str, Any]:
    x_int = r.randint(4, 12)
    y_int = r.randint(4, 12)
    g = math.gcd(x_int, y_int)
    a_v = y_int // g
    b_v = x_int // g
    c_v = (x_int * y_int) // g
    svg = _svg_single_line_region(a_v, b_v, c_v, shade_below=True)
    prompt = (
        f"The shaded region in the diagram is bounded by the axes and a solid line passing through $(0; {y_int})$ and $({x_int}; 0)$.\n\n"
        f"Determine the inequality representing this constraint in simplified standard form $ax + by \\le c$ (where $a, b, c$ are coprime integers)."
    )
    ans = f"{a_v}x + {b_v}y \\le {c_v}"
    sol = (
        f"Gradient $m = \\frac{{0 - {y_int}}}{{{x_int} - 0}} = -\\frac{{{a_v}}}{{{b_v}}}$. "
        f"Line equation: $y = -\\frac{{{a_v}}}{{{b_v}}}x + {y_int} \\implies {a_v}x + {b_v}y = {c_v}$. "
        f"Since the region lies below the solid line, ${a_v}x + {b_v}y \\le {c_v}$."
    )
    return _make_q(
        r, "16_determine_inequality_from_graphed_boundary_line_svg", 16, prompt, ans, sol, 3,
        ["swapped_x_and_y_intercepts_in_double_intercept_formula"],
        [{"step": 1, "criterion": f"Gradient m = -{a_v}/{b_v}", "marks": 1}, {"step": 2, "criterion": f"Line {a_v}x + {b_v}y = {c_v}", "marks": 1}, {"step": 3, "criterion": f"Inequality {ans}", "marks": 1}],
        {"tier_1": f"Use the intercept form x/{x_int} + y/{y_int} <= 1.", "tier_2": f"Multiply through by {c_v} to clear fractions.", "tier_3": ans},
        svg=svg,
    )


# 17. Determine system of inequalities for shaded triangle (with SVG)
def build_17_determine_system_of_inequalities_for_shaded_triangle_svg(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(1, 4)
    b_v = r.randint(2, 5)
    c_v = a_v * b_v * r.randint(2, 4)
    svg = _svg_single_line_region(a_v, b_v, c_v, shade_below=True)
    prompt = (
        f"Write down the complete system of **three** linear inequalities that defines the shaded triangular feasible region "
        f"with vertices $(0; 0)$, $(0; {c_v // b_v})$, and $({c_v // a_v}; 0)$ shown in the diagram."
    )
    ans = f"{a_v}x + {b_v}y \\le {c_v},\\quad x \\ge 0,\\quad y \\ge 0"
    sol = f"The slanted boundary is ${a_v}x + {b_v}y \\le {c_v}$, and the axes bounds are $x \\ge 0$ and $y \\ge 0$."
    return _make_q(
        r, "17_determine_system_of_inequalities_for_shaded_triangle_svg", 17, prompt, ans, sol, 3,
        ["omitted_first_quadrant_non_negativity_inequalities"],
        [{"step": 1, "criterion": f"{a_v}x + {b_v}y <= {c_v}", "marks": 2}, {"step": 2, "criterion": "x >= 0, y >= 0", "marks": 1}],
        {"tier_1": "Find the inequality for the slanted line and include both axis constraints.", "tier_2": f"Slanted boundary: {a_v}x + {b_v}y <= {c_v}; axes: x >= 0, y >= 0.", "tier_3": ans},
        svg=svg,
    )


# 18. Determine system of inequalities for shaded quadrilateral (with SVG)
def build_18_determine_system_of_inequalities_for_shaded_quadrilateral_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(3, 8)
    iy = r.randint(3, 8)
    c1 = ix + iy
    c2 = 2 * ix + iy
    svg = _svg_lp_quad_region(c1, c1, c2, c2 // 2, ix, iy, "Shaded Quadrilateral Feasible Region")
    prompt = (
        f"The shaded quadrilateral feasible region shown in the diagram has vertices $(0; 0)$, $(0; {c1})$, $({ix}; {iy})$, and $({c2 // 2}; 0)$.\n"
        f"The two slanted boundary lines have $y$-intercepts ${c1}$ and ${c2}$ respectively.\n\n"
        f"Write down the two slanted constraint inequalities in the form $ax + by \\le c$."
    )
    ans = f"x + y \\le {c1},\\quad 2x + y \\le {c2}"
    sol = (
        f"Line 1 through $(0; {c1})$ and $({ix}; {iy})$ has gradient $m_1 = \\frac{{{iy} - {c1}}}{{{ix}}} = -1 \\implies x + y \\le {c1}$.\n"
        f"Line 2 through $(0; {c2})$ and $({ix}; {iy})$ has gradient $m_2 = \\frac{{{iy} - {c2}}}{{{ix}}} = -2 \\implies 2x + y \\le {c2}$."
    )
    return _make_q(
        r, "18_determine_system_of_inequalities_for_shaded_quadrilateral_svg", 18, prompt, ans, sol, 4,
        ["calculated_wrong_gradient_for_boundary_line"],
        [{"step": 1, "criterion": f"First constraint x + y <= {c1}", "marks": 2}, {"step": 2, "criterion": f"Second constraint 2x + y <= {c2}", "marks": 2}],
        {"tier_1": f"Find the gradient of each line using (0; y_int) and ({ix}; {iy}).", "tier_2": f"Line 1: m = -1 => x + y <= {c1}. Line 2: m = -2 => 2x + y <= {c2}.", "tier_3": ans},
        svg=svg,
    )


# 19. Horizontal and vertical strip constraints on graph (with SVG)
def build_19_horizontal_and_vertical_strip_constraints_on_graph_svg(r: random.Random) -> Dict[str, Any]:
    x_min = r.randint(2, 5)
    x_max = x_min + r.randint(5, 10)
    y_min = r.randint(3, 6)
    y_max = y_min + r.randint(4, 9)
    area = (x_max - x_min) * (y_max - y_min)
    svg = _svg_lp_quad_region(y_max, x_max, y_max, x_max, x_max, y_min, f"Box Constraints [{x_min}..{x_max}] x [{y_min}..{y_max}]")
    prompt = (
        f"A rectangular feasible region in the Cartesian plane (illustrated in the diagram) is bounded by the vertical lines $x = {x_min}$ and $x = {x_max}$ "
        f"and the horizontal lines $y = {y_min}$ and $y = {y_max}$.\n\n"
        f"Write down the compound inequalities for $x$ and $y$, and calculate the area of this rectangular feasible region."
    )
    ans = f"{x_min} \\le x \\le {x_max},\\quad {y_min} \\le y \\le {y_max},\\quad \\text{{Area}} = {area}"
    sol = f"Constraints: ${x_min} \\le x \\le {x_max}$ and ${y_min} \\le y \\le {y_max}$. Area $= ({x_max} - {x_min})({y_max} - {y_min}) = {x_max - x_min} \\times {y_max - y_min} = {area}$ square units."
    return _make_q(
        r, "19_horizontal_and_vertical_strip_constraints_on_graph_svg", 19, prompt, ans, sol, 3,
        ["confused_horizontal_line_y_equals_k_with_vertical_line_x_equals_k"],
        [{"step": 1, "criterion": f"{x_min} <= x <= {x_max} and {y_min} <= y <= {y_max}", "marks": 2}, {"step": 2, "criterion": f"Area = {area}", "marks": 1}],
        {"tier_1": "Vertical lines constrain x; horizontal lines constrain y.", "tier_2": f"Width = {x_max} - {x_min} = {x_max - x_min}; Height = {y_max} - {y_min} = {y_max - y_min}.", "tier_3": ans},
        svg=svg,
    )


# 20. Count discrete integer lattice points in feasible region (with SVG)
def build_20_count_discrete_integer_lattice_points_in_feasible_region_svg(r: random.Random) -> Dict[str, Any]:
    c_v = r.randint(3, 7)
    # Region: x >= 0, y >= 0, x + y <= c_v. Number of integer points = (c_v + 1)(c_v + 2) // 2
    n_pts = (c_v + 1) * (c_v + 2) // 2
    svg = _svg_single_line_region(1, 1, c_v, shade_below=True)
    prompt = (
        f"The feasible region shown in the diagram is defined by $x + y \\le {c_v}$ with $x \\ge 0, y \\ge 0$.\n\n"
        f"If $x$ and $y$ must both be **whole numbers (non-negative integers)**, calculate the total number of feasible integer combinations $(x; y)$ in the region (including boundary points)."
    )
    ans = f"{n_pts}"
    sol = (
        f"For $x = 0$, $y \\in \\{{0, 1, \\dots, {c_v}\\}}$ (${c_v + 1}$ points); for $x = 1$, ${c_v}$ points; ...; for $x = {c_v}$, $1$ point.\n"
        f"Total lattice points $= 1 + 2 + \\dots + ({c_v + 1}) = \\frac{{({c_v + 1})({c_v + 2})}}{{2}} = {n_pts}$."
    )
    return _make_q(
        r, "20_count_discrete_integer_lattice_points_in_feasible_region_svg", 20, prompt, ans, sol, 3,
        ["forgot_zero_coordinates_when_counting_lattice_points"],
        [{"step": 1, "criterion": f"Sum 1 + 2 + ... + {c_v + 1}", "marks": 2}, {"step": 2, "criterion": f"Total = {n_pts}", "marks": 1}],
        {"tier_1": f"Count how many integer y-values are valid for each x from 0 to {c_v}.", "tier_2": f"Sum = ({c_v + 1})*({c_v + 2})/2.", "tier_3": ans},
        svg=svg,
    )


# 21. Intersection vertex of two constraint lines simultaneous (with SVG)
def build_21_intersection_vertex_of_two_constraint_lines_simultaneous_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(3, 10)
    iy = r.randint(4, 11)
    a1, b1 = 1, 1
    c1 = ix + iy
    a2 = r.choice([2, 3])
    b2 = 1
    c2 = a2 * ix + iy
    svg = _svg_lp_quad_region(c1, c1, c2, c2 // a2, ix, iy, "Intersection of Boundary Lines")
    prompt = (
        f"Two boundary lines of the feasible region shown in the diagram are given by:\n"
        f"$$x + y = {c1} \\quad \\text{{and}} \\quad {a2}x + y = {c2}$$\n\n"
        f"Solve these equations simultaneously to determine the coordinates of the intersection vertex $C$."
    )
    ans = f"({ix}; {iy})"
    sol = (
        f"Subtract the first equation from the second: $({a2}x + y) - (x + y) = {c2} - {c1} \\implies {a2 - 1}x = {c2 - c1} \\implies x = {ix}$.\n"
        f"Substitute $x = {ix}$ into $x + y = {c1} \\implies y = {c1} - {ix} = {iy}$. Vertex $C({ix}; {iy})$."
    )
    return _make_q(
        r, "21_intersection_vertex_of_two_constraint_lines_simultaneous_svg", 21, prompt, ans, sol, 3,
        ["simultaneous_equations_sign_error"],
        [{"step": 1, "criterion": f"Eliminate y to find x = {ix}", "marks": 2}, {"step": 2, "criterion": f"Substitute to find y = {iy}", "marks": 1}],
        {"tier_1": "Subtract the first equation from the second to eliminate y.", "tier_2": f"{a2 - 1}x = {c2 - c1} => x = {ix}, then y = {c1} - {ix}.", "tier_3": ans},
        svg=svg,
    )


# 22. List all corner point vertices of bounded feasible region (with SVG)
def build_22_list_all_corner_point_vertices_of_bounded_feasible_region_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(4, 10)
    iy = r.randint(3, 9)
    if ix % 2 != iy % 2:
        iy += 1
    c1 = ix + iy
    c2 = 2 * ix + iy
    x_int_2 = c2 // 2
    svg = _svg_lp_quad_region(c1, c1, c2, x_int_2, ix, iy, "Vertices of Bounded Feasible Region")
    prompt = (
        f"A feasible region $S$ (shown in the diagram) is defined by:\n"
        f"$$x + y \\le {c1},\\quad 2x + y \\le {c2},\\quad x \\ge 0,\\quad y \\ge 0$$\n\n"
        f"Determine the coordinates of all **four** corner-point vertices of the feasible region $S$."
    )
    ans = f"(0; 0),\\ (0; {c1}),\\ ({ix}; {iy}),\\ ({x_int_2}; 0)"
    sol = (
        f"1. Origin: $(0; 0)$.\n"
        f"2. $y$-axis corner (smaller $y$-intercept of ${c1}$ and ${c2}$): $(0; {c1})$.\n"
        f"3. Intersection of $x + y = {c1}$ and $2x + y = {c2}$: $({ix}; {iy})$.\n"
        f"4. $x$-axis corner (smaller $x$-intercept of ${c1}$ and ${x_int_2}$): $({x_int_2}; 0)$."
    )
    return _make_q(
        r, "22_list_all_corner_point_vertices_of_bounded_feasible_region_svg", 22, prompt, ans, sol, 4,
        ["selected_non_feasible_outer_intercept_as_vertex"],
        [{"step": 1, "criterion": f"(0; 0) and (0; {c1})", "marks": 1}, {"step": 2, "criterion": f"Intersection ({ix}; {iy})", "marks": 2}, {"step": 3, "criterion": f"({x_int_2}; 0)", "marks": 1}],
        {"tier_1": "Choose the smaller intercept on each axis so both <= constraints are satisfied.", "tier_2": f"y-axis vertex is (0; {c1}), x-axis vertex is ({x_int_2}; 0), and intersection is ({ix}; {iy}).", "tier_3": ans},
        svg=svg,
    )


# 23. Unbounded feasible region vertices for cost minimisation (with SVG)
def build_23_unbounded_feasible_region_vertices_for_cost_minimisation_svg(r: random.Random) -> Dict[str, Any]:
    ix = r.randint(4, 10)
    iy = r.randint(4, 10)
    if ix % 2 != iy % 2:
        iy += 1
    c1 = ix + iy
    c2 = 2 * ix + iy
    svg = _svg_lp_quad_region(c1, c1, c2, c2 // 2, ix, iy, "Unbounded Lower-Border Vertices")
    prompt = (
        f"An unbounded first-quadrant feasible region (whose boundary lines are shown in the diagram) is defined by:\n"
        f"$$x + y \\ge {c1},\\quad 2x + y \\ge {c2},\\quad x \\ge 0,\\quad y \\ge 0$$\n\n"
        f"Determine the **three** corner points forming the lower boundary of this unbounded feasible region."
    )
    ans = f"(0; {c2}),\\ ({ix}; {iy}),\\ ({c1}; 0)"
    sol = (
        f"For $\\ge$ constraints, we take the larger intercept on each axis so both inequalities hold:\n"
        f"• On the $y$-axis: $\\max({c1}, {c2}) = {c2} \\implies (0; {c2})$.\n"
        f"• Intersection of $x + y = {c1}$ and $2x + y = {c2}$: $({ix}; {iy})$.\n"
        f"• On the $x$-axis: $\\max({c1}, {c2 // 2}) = {c1} \\implies ({c1}; 0)$."
    )
    return _make_q(
        r, "23_unbounded_feasible_region_vertices_for_cost_minimisation_svg", 23, prompt, ans, sol, 3,
        ["chose_smaller_intercept_for_greater_equal_unbounded_region"],
        [{"step": 1, "criterion": f"y-axis vertex (0; {c2})", "marks": 1}, {"step": 2, "criterion": f"Intersection ({ix}; {iy})", "marks": 1}, {"step": 3, "criterion": f"x-axis vertex ({c1}; 0)", "marks": 1}],
        {"tier_1": "For >= constraints, an axis intercept must satisfy BOTH inequalities, so pick the larger intercept.", "tier_2": f"y-axis: (0; {c2}); intersection: ({ix}; {iy}); x-axis: ({c1}; 0).", "tier_3": ans},
        svg=svg,
    )


# 24. Effect of tightening or relaxing a resource constraint on area (with SVG)
def build_24_effect_of_tightening_or_relaxing_a_resource_constraint_on_area_svg(r: random.Random) -> Dict[str, Any]:
    c1 = r.choice([6, 8, 10, 12])
    c2 = c1 + r.choice([4, 6, 8])
    area1 = (c1 * c1) // 2
    area2 = (c2 * c2) // 2
    diff = area2 - area1
    svg = _svg_single_line_region(1, 1, c2, shade_below=True)
    prompt = (
        f"A triangular feasible region is initially bounded by $x \\ge 0, y \\ge 0$, and $x + y \\le {c1}$.\n"
        f"When overtime hours are approved, the constraint is relaxed to $x + y \\le {c2}$ (shown in the diagram).\n\n"
        f"Calculate the **increase in the area** of the feasible region."
    )
    ans = f"{diff}"
    sol = (
        f"Initial area $= \\frac{{1}}{{2}}({c1})({c1}) = {area1}$.\n"
        f"New area $= \\frac{{1}}{{2}}({c2})({c2}) = {area2}$.\n"
        f"Increase in area $= {area2} - {area1} = {diff}$ square units."
    )
    return _make_q(
        r, "24_effect_of_tightening_or_relaxing_a_resource_constraint_on_area_svg", 24, prompt, ans, sol, 3,
        ["subtracted_intercepts_before_squaring_in_area_difference"],
        [{"step": 1, "criterion": f"Initial area = {area1}", "marks": 1}, {"step": 2, "criterion": f"New area = {area2}", "marks": 1}, {"step": 3, "criterion": f"Increase = {diff}", "marks": 1}],
        {"tier_1": "Each region is a right-angled triangle with base = c and height = c.", "tier_2": f"Area_new - Area_old = 0.5*{c2}^2 - 0.5*{c1}^2 = {area2} - {area1}.", "tier_3": ans},
        svg=svg,
    )


# 25. Redundant constraint identification outside feasible region (with SVG)
def build_25_redundant_constraint_identification_outside_feasible_region_svg(r: random.Random) -> Dict[str, Any]:
    c_tight = r.randint(6, 12)
    c_red = c_tight + r.randint(5, 10)
    svg = _svg_single_line_region(1, 1, c_tight, shade_below=True)
    prompt = (
        f"Consider the system of constraints in the first quadrant ($x \\ge 0, y \\ge 0$) shown in the diagram:\n"
        f"$$\\text{{Constraint A: }} x + y \\le {c_tight} \\qquad \\text{{Constraint B: }} x + y \\le {c_red}$$\n\n"
        f"State which constraint is **redundant** (does not affect the feasible region) and calculate the maximum value of $x + y$ in the feasible region."
    )
    ans = f"\\text{{Constraint B }} (x + y \\le {c_red})\\text{{ is redundant; max}}(x + y) = {c_tight}"
    sol = (
        f"Every point satisfying $x + y \\le {c_tight}$ automatically satisfies $x + y \\le {c_red}$ since ${c_tight} < {c_red}$.\n"
        f"Therefore **Constraint B** ($x + y \\le {c_red}$) is redundant, and $\\max(x + y) = {c_tight}$."
    )
    return _make_q(
        r, "25_redundant_constraint_identification_outside_feasible_region_svg", 25, prompt, ans, sol, 2,
        ["identified_tighter_constraint_as_redundant"],
        [{"step": 1, "criterion": f"Constraint B (x + y <= {c_red}) is redundant", "marks": 1}, {"step": 2, "criterion": f"Maximum x + y = {c_tight}", "marks": 1}],
        {"tier_1": "A constraint is redundant if it lies completely outside the tighter boundary.", "tier_2": f"Since x + y <= {c_tight} is stricter than x + y <= {c_red}, Constraint B is redundant.", "tier_3": ans},
        svg=svg,
    )


ARCHETYPES_01_25 = {
    "01_translate_at_most_and_maximum_resource_constraint": build_01_translate_at_most_and_maximum_resource_constraint,
    "02_translate_at_least_and_minimum_demand_constraint": build_02_translate_at_least_and_minimum_demand_constraint,
    "03_translate_ratio_and_proportional_production_constraint": build_03_translate_ratio_and_proportional_production_constraint,
    "04_translate_at_least_twice_as_many_y_as_x_constraint": build_04_translate_at_least_twice_as_many_y_as_x_constraint,
    "05_implicit_non_negativity_and_integer_domain_constraints": build_05_implicit_non_negativity_and_integer_domain_constraints,
    "06_formulate_two_resource_manufacturing_system_from_table": build_06_formulate_two_resource_manufacturing_system_from_table,
    "07_formulate_dietary_and_nutritional_minimum_constraints": build_07_formulate_dietary_and_nutritional_minimum_constraints,
    "08_formulate_transport_fleet_capacity_and_budget_constraints": build_08_formulate_transport_fleet_capacity_and_budget_constraints,
    "09_formulate_agricultural_land_water_and_labour_constraints": build_09_formulate_agricultural_land_water_and_labour_constraints,
    "10_formulate_objective_function_for_profit_revenue_or_cost": build_10_formulate_objective_function_for_profit_revenue_or_cost,
    "11_x_and_y_intercepts_of_constraint_boundary_line_svg": build_11_x_and_y_intercepts_of_constraint_boundary_line_svg,
    "12_gradient_intercept_form_of_constraint_inequality": build_12_gradient_intercept_form_of_constraint_inequality,
    "13_identify_half_plane_shading_above_or_below_boundary_svg": build_13_identify_half_plane_shading_above_or_below_boundary_svg,
    "14_solid_vs_dashed_boundary_line_and_strict_inequality": build_14_solid_vs_dashed_boundary_line_and_strict_inequality,
    "15_verify_whether_candidate_point_lies_in_feasible_region_svg": build_15_verify_whether_candidate_point_lies_in_feasible_region_svg,
    "16_determine_inequality_from_graphed_boundary_line_svg": build_16_determine_inequality_from_graphed_boundary_line_svg,
    "17_determine_system_of_inequalities_for_shaded_triangle_svg": build_17_determine_system_of_inequalities_for_shaded_triangle_svg,
    "18_determine_system_of_inequalities_for_shaded_quadrilateral_svg": build_18_determine_system_of_inequalities_for_shaded_quadrilateral_svg,
    "19_horizontal_and_vertical_strip_constraints_on_graph_svg": build_19_horizontal_and_vertical_strip_constraints_on_graph_svg,
    "20_count_discrete_integer_lattice_points_in_feasible_region_svg": build_20_count_discrete_integer_lattice_points_in_feasible_region_svg,
    "21_intersection_vertex_of_two_constraint_lines_simultaneous_svg": build_21_intersection_vertex_of_two_constraint_lines_simultaneous_svg,
    "22_list_all_corner_point_vertices_of_bounded_feasible_region_svg": build_22_list_all_corner_point_vertices_of_bounded_feasible_region_svg,
    "23_unbounded_feasible_region_vertices_for_cost_minimisation_svg": build_23_unbounded_feasible_region_vertices_for_cost_minimisation_svg,
    "24_effect_of_tightening_or_relaxing_a_resource_constraint_on_area_svg": build_24_effect_of_tightening_or_relaxing_a_resource_constraint_on_area_svg,
    "25_redundant_constraint_identification_outside_feasible_region_svg": build_25_redundant_constraint_identification_outside_feasible_region_svg,
}
