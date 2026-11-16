"""Technical Mathematics (Grades 11–12) — Mensuration & Integration Archetypes 26–38.
Covers:
- 26–30: Mid-ordinate rule for irregular areas and cross-sections (formula direct, midpoint calculation, river cross-section, reservoir depth, earthwork volume).
- 31–35: Trapezoidal rule for irregular technical areas (direct boundary formula, odd ordinates, metal plate sheet, embankment cut-and-fill, comparison with mid-ordinate).
- 36–38: Definite integrals as area under curves (polynomial linear/quadratic, cubic, and fractional power curves).
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp

def make_math_question(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    sub = kwargs.get("subskill", "subskill")
    p = kwargs.get("prompt") or kwargs.get("question_text", "")
    ans = kwargs.get("answer_latex") or kwargs.get("expected_answer") or kwargs.get("sample_answer", "")
    h = kwargs.get("hints", [])
    if isinstance(h, list):
        h_dict = {
            "tier_1": h[0] if len(h) > 0 else "Recall the formula.",
            "tier_2": h[1] if len(h) > 1 else "Apply step-by-step substitution.",
            "tier_3": h[2] if len(h) > 2 else f"The final answer is {ans}.",
        }
    elif isinstance(h, dict):
        h_dict = h
    else:
        h_dict = {"tier_1": "Hint 1", "tier_2": "Hint 2", "tier_3": "Hint 3"}

    ms = kwargs.get("marking_schema") or {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Method step", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Final answer", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    diag = kwargs.get("diagram_spec")

    return {
        "id": f"tech_mens_{random.randint(100000, 999999)}",
        "question_id": f"tech_mens_{random.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": sub,
        "learning_objective_id": kwargs.get("learning_objective_id") or kwargs.get("lo_id", f"tech_mens_{sub}"),
        "prompt": p,
        "prompt_latex": p,
        "answer_latex": ans,
        "sample_answer": ans,
        "marking_schema": ms,
        "hints": h_dict,
        "misconception_tags": kwargs.get("misconception_tags", ["general_error"]),
        "keywords": ["mensuration", "integration", "technical mathematics"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": kwargs.get("difficulty", "medium"),
        "marks": ms.get("total_marks", 4),
        "diagram_spec": diag,
    }


def step(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    fl = kwargs.get("from_latex")
    tl = kwargs.get("to_latex_str") or kwargs.get("to_latex")
    if args and fl is None:
        fl = str(args[0])
    return {
        "from_latex": fl or "",
        "to_latex": tl or "",
        "from_sympy": "",
        "to_sympy": "",
        "op": kwargs.get("op", "step"),
        "rule": kwargs.get("rule", ""),
        "common_errors": list(kwargs.get("common_errors") or []),
    }


def solution_graph(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    steps_list = args[0] if args else kwargs.get("steps", [])
    fl = kwargs.get("final_latex") or kwargs.get("canonical_form") or ""
    return {
        "goal": kwargs.get("goal", "solve"),
        "chain_type": kwargs.get("chain_type", "expression"),
        "var": kwargs.get("var", "x"),
        "steps": list(steps_list),
        "final_latex": fl,
        "final_sympy": "",
    }

TOPIC = "Mensuration"
LO_PREFIX = "tech11_mens_calc"


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


# ---------------------------------------------------------------------------
# 26. Mid-ordinate Rule: Direct Application from Given Mid-ordinates
# ---------------------------------------------------------------------------
def build_26_mid_ordinate_rule_formula_direct(r: random.Random) -> Dict[str, Any]:
    # Area = h * (m1 + m2 + ... + mn)
    h = r.choice([2, 3, 4, 5])
    n_mid = r.choice([4, 5, 6])
    m_list = [round(r.uniform(2.5, 9.5), 1) for _ in range(n_mid)]
    sum_m = round(sum(m_list), 2)
    area = round(h * sum_m, 2)

    m_str = ", \\; ".join(f"m_{{{i+1}}} = {_fmt_sa(m)}\\text{{ m}}" for i, m in enumerate(m_list))
    m_sum_str = " + ".join(_fmt_sa(m) for m in m_list)

    ans_latex = f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2"
    prompt = (
        f"An irregular technical cross-section is divided into {n_mid} equal strips of common width $h = {h}\\text{{ m}}$. "
        f"The measured mid-ordinates are:\n$${m_str}$$\n\n"
        f"Use the **mid-ordinate rule** to calculate the estimated area of the cross-section."
    )

    sg = solution_graph(
        [
            step(
                f"Recall the mid-ordinate rule formula for area: $\\text{{Area}} = h \\times \\sum m = h \\times (m_1 + m_2 + \\dots + m_n)$.",
                to_latex="\\text{Area} = h \\sum m",
                op="state_mid_ordinate_formula",
                rule="mid_ordinate_rule",
            ),
            step(
                f"Sum the mid-ordinates: $\\sum m = {m_sum_str} = {_fmt_sa(sum_m)}\\text{{ m}}$.",
                to_latex=f"\\sum m = {_fmt_sa(sum_m)}\\text{{ m}}",
                op="sum_mid_ordinates",
                rule="sum_m",
            ),
            step(
                f"Multiply by the common interval width $h = {h}\\text{{ m}}$: $\\text{{Area}} = {h} \\times {_fmt_sa(sum_m)} = {_fmt_sa(area)}\\text{{ m}}^2$.",
                to_latex=ans_latex,
                op="calculate_area",
                rule="A = h * sum(m)",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"The mid-ordinate rule formula is: $\\text{{Area}} = \\text{{interval width}} \\times (\\text{{sum of mid-ordinates}})$.",
        f"Add all {n_mid} mid-ordinates together: ${m_sum_str} = {_fmt_sa(sum_m)}$.",
        f"Multiply the sum by $h = {h}$: ${h} \\times {_fmt_sa(sum_m)} = {_fmt_sa(area)}\\text{{ m}}^2$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="26_mid_ordinate_rule_formula_direct",
        lo_id=f"{LO_PREFIX}_26",
        difficulty="easy",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["divided_by_2_unnecessarily_in_mid_ordinate", "arithmetic_addition_error"],
    )


# ---------------------------------------------------------------------------
# 27. Mid-ordinate Rule: Calculate Mid-ordinates from Boundary Ordinates
# ---------------------------------------------------------------------------
def build_27_mid_ordinate_rule_calculate_midpoints(r: random.Random) -> Dict[str, Any]:
    # Given 5 boundary ordinates (4 intervals), find 4 mid-ordinates: m_i = (y_i + y_{i+1})/2
    h = r.choice([2, 4, 5])
    y = [round(r.uniform(1.0, 8.0), 1) for _ in range(5)]
    m = [round((y[i] + y[i + 1]) / 2, 2) for i in range(4)]
    sum_m = round(sum(m), 2)
    area = round(h * sum_m, 2)

    y_str = ", \\; ".join(f"y_{{{i+1}}} = {_fmt_sa(val)}\\text{{ m}}" for i, val in enumerate(y))
    m_calc_str = ", \\; ".join(f"m_{{{i+1}}} = \\frac{{{_fmt_sa(y[i])} + {_fmt_sa(y[i+1])}}}{{2}} = {_fmt_sa(m[i])}" for i in range(4))

    ans_latex = f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2"
    prompt = (
        f"Five consecutive boundary ordinates spaced at equal intervals of $h = {h}\\text{{ m}}$ measure:\n"
        f"$${y_str}$$\n\n"
        f"1. Calculate the four corresponding mid-ordinates ($m_1, m_2, m_3, m_4$).\n"
        f"2. Use the mid-ordinate rule to calculate the area of the shape."
    )

    sg = solution_graph(
        [
            step(
                f"Calculate each mid-ordinate by averaging adjacent boundary ordinates: {m_calc_str}.",
                to_latex=f"\\text{{Mid-ordinates: }} {', '.join(_fmt_sa(val) for val in m)}",
                op="average_adjacent_ordinates",
                rule="m_i = (y_i + y_{i+1})/2",
            ),
            step(
                f"Sum the mid-ordinates: $\\sum m = {' + '.join(_fmt_sa(val) for val in m)} = {_fmt_sa(sum_m)}\\text{{ m}}$.",
                to_latex=f"\\sum m = {_fmt_sa(sum_m)}",
                op="sum_mid_ordinates",
                rule="sum_m",
            ),
            step(
                f"Calculate total area: $\\text{{Area}} = h \\times \\sum m = {h} \\times {_fmt_sa(sum_m)} = {_fmt_sa(area)}\\text{{ m}}^2$.",
                to_latex=ans_latex,
                op="calculate_area",
                rule="A = h * sum(m)",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"Find each mid-ordinate by taking the average of two adjacent boundary ordinates: $m_1 = \\frac{{y_1 + y_2}}{{2}}$.",
        f"Sum the four mid-ordinates: $\\sum m = {_fmt_sa(sum_m)}$.",
        f"Multiply by the strip width $h = {h}$: $\\text{{Area}} = {h} \\times {_fmt_sa(sum_m)} = {_fmt_sa(area)}\\text{{ m}}^2$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="27_mid_ordinate_rule_calculate_midpoints",
        lo_id=f"{LO_PREFIX}_27",
        difficulty="medium",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["using_boundary_ordinates_directly_in_mid_ordinate_formula"],
    )


# ---------------------------------------------------------------------------
# 28. Mid-ordinate Rule: River Bed Cross-Section Depth Profile
# ---------------------------------------------------------------------------
def build_28_mid_ordinate_rule_river_cross_section(r: random.Random) -> Dict[str, Any]:
    # Baseline width L = 24m or 30m, intervals = 6, h = L/6
    total_width = r.choice([24, 30, 36])
    n_intervals = 6
    h = total_width // n_intervals
    # Depths at midpoints (m)
    depths = [round(r.uniform(1.2, 4.8), 2) for _ in range(n_intervals)]
    sum_depths = round(sum(depths), 2)
    area = round(h * sum_depths, 2)

    svg_code = (
        '<svg viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg">'
        '<rect width="600" height="220" fill="#f8fafc" rx="8"/>'
        '<!-- Water surface line -->'
        '<line x1="50" y1="60" x2="550" y2="60" stroke="#0284c7" stroke-width="3"/>'
        '<text x="300" y="50" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#0369a1" font-weight="bold">Water Surface (Baseline = ' + str(total_width) + ' m)</text>'
        '<!-- Riverbed profile -->'
        '<path d="M 50 60 Q 150 160 300 170 T 550 60 Z" fill="#bae6fd" opacity="0.6"/>'
        '<path d="M 50 60 Q 150 160 300 170 T 550 60" fill="none" stroke="#0f172a" stroke-width="2.5"/>'
        '<!-- Strips -->'
        + "".join(f'<line x1="{50 + i * (500 // n_intervals)}" y1="60" x2="{50 + i * (500 // n_intervals)}" y2="150" stroke="#94a3b8" stroke-dasharray="4,4"/>' for i in range(1, n_intervals))
        + f'<text x="300" y="200" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#475569">6 Equal Intervals: h = {h} m each</text>'
        '</svg>'
    )

    d_spec = {
        "kind": "inline_svg",
        "svg": svg_code,
        "diagram_role": "context",
        "title": "Riverbed Irregular Cross-Section",
    }

    depth_str = ", \\; ".join(f"d_{{{i+1}}} = {_fmt_sa(d)}\\text{{ m}}" for i, d in enumerate(depths))
    ans_latex = f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2"

    prompt = (
        f"A civil engineer surveys the cross-section of a river channel of total width ${total_width}\\text{{ m}}$. "
        f"The riverbed is divided into {n_intervals} equal strips. The soundings of depth at the center of each strip are:\n"
        f"$${depth_str}$$\n\n"
        f"Calculate the cross-sectional area of the river channel using the mid-ordinate rule."
    )

    sg = solution_graph(
        [
            step(
                f"Calculate the common interval width: $h = \\frac{{\\text{{total width}}}}{{\\text{{number of strips}}}} = \\frac{{{total_width}}}{{{n_intervals}}} = {h}\\text{{ m}}$.",
                to_latex=f"h = {h}\\text{{ m}}",
                op="calculate_interval_width",
                rule="h = Total / n",
            ),
            step(
                f"Sum the measured mid-ordinate depths: $\\sum d = {' + '.join(_fmt_sa(d) for d in depths)} = {_fmt_sa(sum_depths)}\\text{{ m}}$.",
                to_latex=f"\\sum d = {_fmt_sa(sum_depths)}\\text{{ m}}",
                op="sum_depths",
                rule="sum_d",
            ),
            step(
                f"Calculate cross-sectional area: $\\text{{Area}} = h \\times \\sum d = {h} \\times {_fmt_sa(sum_depths)} = {_fmt_sa(area)}\\text{{ m}}^2$.",
                to_latex=ans_latex,
                op="evaluate_area",
                rule="A = h * sum(d)",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"Determine the width of each strip: $h = {total_width} / {n_intervals} = {h}\\text{{ m}}$.",
        f"Add all {n_intervals} depth soundings together: $\\sum d = {_fmt_sa(sum_depths)}$.",
        f"Multiply the sum of depths by $h = {h}$ to obtain the cross-sectional area in $\\text{{m}}^2$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="28_mid_ordinate_rule_river_cross_section",
        lo_id=f"{LO_PREFIX}_28",
        difficulty="medium",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["confusing_channel_width_with_interval_width"],
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 29. Mid-ordinate Rule: Water Reservoir Dam Depth Profile
# ---------------------------------------------------------------------------
def build_29_mid_ordinate_rule_water_reservoir_cross_section(r: random.Random) -> Dict[str, Any]:
    h = r.choice([5, 8, 10])
    n_strips = 5
    total_span = h * n_strips
    depths = [round(r.uniform(4.0, 15.0), 1) for _ in range(n_strips)]
    sum_depths = round(sum(depths), 1)
    area = round(h * sum_depths, 2)

    depth_str = ", \\; ".join(f"y_{{m{i+1}}} = {_fmt_sa(d)}\\text{{ m}}" for i, d in enumerate(depths))
    ans_latex = f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2"

    prompt = (
        f"A municipal water reservoir wall of baseline span ${total_span}\\text{{ m}}$ is partitioned into {n_strips} strips "
        f"of equal width $h = {h}\\text{{ m}}$. The recorded mid-ordinate water depths are:\n"
        f"$${depth_str}$$\n\n"
        f"Use the mid-ordinate rule to estimate the water-retaining cross-sectional area of the reservoir."
    )

    sg = solution_graph(
        [
            step(
                f"Formula: $\\text{{Area}} = h \\times \\sum y_m$.",
                to_latex="\\text{Area} = h \\sum y_m",
                op="state_formula",
                rule="mid_ordinate_rule",
            ),
            step(
                f"Sum the mid-ordinate depths: $\\sum y_m = {' + '.join(_fmt_sa(d) for d in depths)} = {_fmt_sa(sum_depths)}\\text{{ m}}$.",
                to_latex=f"\\sum y_m = {_fmt_sa(sum_depths)}\\text{{ m}}",
                op="sum_ordinates",
                rule="sum_ym",
            ),
            step(
                f"Compute area: $\\text{{Area}} = {h} \\times {_fmt_sa(sum_depths)} = {_fmt_sa(area)}\\text{{ m}}^2$.",
                to_latex=ans_latex,
                op="evaluate_area",
                rule="A = h * sum(ym)",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"Recall the mid-ordinate rule: $\\text{{Area}} = h \\sum y_m$.",
        f"Sum the five depths: ${_fmt_sa(sum_depths)}$.",
        f"Multiply by $h = {h}$: ${h} \\times {_fmt_sa(sum_depths)} = {_fmt_sa(area)}\\text{{ m}}^2$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="29_mid_ordinate_rule_water_reservoir_cross_section",
        lo_id=f"{LO_PREFIX}_29",
        difficulty="medium",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["using_total_span_instead_of_interval_width"],
    )


# ---------------------------------------------------------------------------
# 30. Mid-ordinate Rule: Earthwork Excavation Prismoidal Volume
# ---------------------------------------------------------------------------
def build_30_mid_ordinate_rule_with_prismoidal_volume(r: random.Random) -> Dict[str, Any]:
    # Cross-sectional area from mid-ordinates, then Volume = Area * Length
    h = r.choice([3, 4, 5])
    length = r.choice([40, 50, 60, 80, 100])
    m_list = [round(r.uniform(3.0, 7.0), 1) for _ in range(5)]
    sum_m = round(sum(m_list), 1)
    area = round(h * sum_m, 2)
    volume = round(area * length, 2)

    m_str = ", \\; ".join(f"m_{{{i+1}}} = {_fmt_sa(m)}\\text{{ m}}" for i, m in enumerate(m_list))
    ans_latex = f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2, \\quad \\text{{Volume}} = {_fmt_sa(volume)}\\text{{ m}}^3"

    prompt = (
        f"An irregular road trench has a uniform cross-section along its entire length of $L = {length}\\text{{ m}}$. "
        f"The cross-section is divided into 5 strips of width $h = {h}\\text{{ m}}$ with mid-ordinates:\n"
        f"$${m_str}$$\n\n"
        f"1. Determine the cross-sectional area of the trench using the mid-ordinate rule.\n"
        f"2. Hence, calculate the total volume of earth that must be excavated (in $\\text{{m}}^3$)."
    )

    sg = solution_graph(
        [
            step(
                f"Calculate cross-sectional area: $\\text{{Area}} = h \\times \\sum m = {h} \\times ({' + '.join(_fmt_sa(m) for m in m_list)}) = {h} \\times {_fmt_sa(sum_m)} = {_fmt_sa(area)}\\text{{ m}}^2$.",
                to_latex=f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2",
                op="calculate_area",
                rule="A = h * sum(m)",
            ),
            step(
                f"Calculate excavation volume: $V = \\text{{Area}} \\times L = {_fmt_sa(area)} \\times {length} = {_fmt_sa(volume)}\\text{{ m}}^3$.",
                to_latex=ans_latex,
                op="calculate_volume",
                rule="V = A * L",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"First calculate the area using the mid-ordinate rule: $\\text{{Area}} = h \\times \\sum m$.",
        f"Multiply the area by the length of the trench ($L = {length}\\text{{ m}}$) to get the volume.",
        f"Total volume $= {_fmt_sa(area)} \\times {length} = {_fmt_sa(volume)}\\text{{ m}}^3$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="30_mid_ordinate_rule_with_prismoidal_volume",
        lo_id=f"{LO_PREFIX}_30",
        difficulty="hard",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["confusing_area_with_volume_units", "arithmetic_multiplication_error"],
        diagram_spec={
            "kind": "inline_svg",
            "diagram_role": "context",
            "plate": "/diagrams/blender_3d_rectangular_prism_textbook.jpg",
            "blender_plate": "/diagrams/blender_3d_rectangular_prism_textbook.jpg",
            "model_glb": "/models/blender_3d_rectangular_prism.glb",
            "length": length,
            "h": h,
            "volume": volume,
            "svg": f"""<svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg"><rect width="300" height="150" fill="#f8fafc"/><text x="20" y="30" font-size="12" fill="#0f172a">Trench Section: L={length}m, h={h}m</text><polygon points="40,110 80,60 220,60 260,110" fill="#e2e8f0" stroke="#475569" stroke-width="2"/></svg>""",
        },
    )


# ---------------------------------------------------------------------------
# 31. Trapezoidal Rule: Direct Boundary Formula Application
# ---------------------------------------------------------------------------
def build_31_trapezoidal_rule_boundary_ordinates_direct(r: random.Random) -> Dict[str, Any]:
    # A = h * [ (y1 + yn)/2 + y2 + y3 + ... + y_{n-1} ]
    h = r.choice([2, 3, 4, 5])
    # 6 boundary ordinates (5 intervals)
    y1 = round(r.uniform(0.0, 3.0), 1)
    y2 = round(r.uniform(4.0, 7.0), 1)
    y3 = round(r.uniform(6.0, 9.0), 1)
    y4 = round(r.uniform(5.0, 8.0), 1)
    y5 = round(r.uniform(3.0, 6.0), 1)
    y6 = round(r.uniform(0.0, 2.5), 1)

    ends = round((y1 + y6) / 2, 2)
    intermediates = round(y2 + y3 + y4 + y5, 2)
    area = round(h * (ends + intermediates), 2)

    ordinates_str = f"y_1 = {_fmt_sa(y1)}, \\; y_2 = {_fmt_sa(y2)}, \\; y_3 = {_fmt_sa(y3)}, \\; y_4 = {_fmt_sa(y4)}, \\; y_5 = {_fmt_sa(y5)}, \\; y_6 = {_fmt_sa(y6)}"
    ans_latex = f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2"

    prompt = (
        f"Six boundary ordinates measured at equal intervals of $h = {h}\\text{{ m}}$ have lengths:\n"
        f"$${ordinates_str}\\text{{ (in metres)}}$$\n\n"
        f"Use the **trapezoidal rule** to determine the area enclosed by the shape."
    )

    sg = solution_graph(
        [
            step(
                f"Recall the trapezoidal rule: $\\text{{Area}} = h \\left[ \\frac{{y_1 + y_n}}{{2}} + y_2 + y_3 + \\dots + y_{{n-1}} \\right]$.",
                to_latex="\\text{Area} = h \\left[ \\frac{y_1 + y_n}{2} + \\sum y_{\\text{intermediate}} \\right]",
                op="state_trapezoidal_formula",
                rule="trapezoidal_rule",
            ),
            step(
                f"Calculate average of first and last ordinates: $\\frac{{{_fmt_sa(y1)} + {_fmt_sa(y6)}}}{{2}} = {_fmt_sa(ends)}$.",
                to_latex=f"\\frac{{y_1 + y_6}}{{2}} = {_fmt_sa(ends)}",
                op="first_and_last_average",
                rule="(y1 + yn)/2",
            ),
            step(
                f"Sum the intermediate ordinates: ${y2} + {y3} + {y4} + {y5} = {_fmt_sa(intermediates)}$.",
                to_latex=f"\\sum y_{{\\text{{intermediate}}}} = {_fmt_sa(intermediates)}",
                op="sum_intermediates",
                rule="intermediate_ordinates",
            ),
            step(
                f"Multiply by interval width $h = {h}$: $\\text{{Area}} = {h} \\times ({_fmt_sa(ends)} + {_fmt_sa(intermediates)}) = {h} \\times {_fmt_sa(ends + intermediates)} = {_fmt_sa(area)}\\text{{ m}}^2$.",
                to_latex=ans_latex,
                op="calculate_area",
                rule="A = h * [ends + intermediates]",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"The trapezoidal formula takes half of the first and last ordinates: $\\frac{{y_1 + y_6}}{{2}} = {_fmt_sa(ends)}$.",
        f"Add all the intermediate ordinates ($y_2$ through $y_5$): ${_fmt_sa(intermediates)}$.",
        f"Multiply the total bracket sum by $h = {h}$ to get the area: ${_fmt_sa(area)}\\text{{ m}}^2$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="31_trapezoidal_rule_boundary_ordinates_direct",
        lo_id=f"{LO_PREFIX}_31",
        difficulty="medium",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["omitted_dividing_first_last_by_2", "included_all_ordinates_equally"],
    )


# ---------------------------------------------------------------------------
# 32. Trapezoidal Rule: Application with Odd Number of Ordinates (7 Ordinates)
# ---------------------------------------------------------------------------
def build_32_trapezoidal_rule_odd_number_of_ordinates(r: random.Random) -> Dict[str, Any]:
    h = r.choice([2.5, 3.0, 4.0, 5.0])
    # 7 ordinates (6 intervals)
    y = [round(r.uniform(1.0, 9.0), 1) for _ in range(7)]
    ends = round((y[0] + y[-1]) / 2, 2)
    intermediates = round(sum(y[1:-1]), 2)
    area = round(h * (ends + intermediates), 2)

    y_str = ", \\; ".join(f"y_{{{i+1}}} = {_fmt_sa(val)}\\text{{ m}}" for i, val in enumerate(y))
    ans_latex = f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2"

    prompt = (
        f"Seven boundary ordinates measured at regular intervals of $h = {_fmt_sa(h)}\\text{{ m}}$ are recorded as:\n"
        f"$${y_str}$$\n\n"
        f"Calculate the approximate area using the trapezoidal rule."
    )

    sg = solution_graph(
        [
            step(
                f"Trapezoidal rule formula: $\\text{{Area}} = h \\left[ \\frac{{y_1 + y_7}}{{2}} + (y_2 + y_3 + y_4 + y_5 + y_6) \\right]$.",
                to_latex="\\text{Area} = h \\left[ \\frac{y_1 + y_7}{2} + \\sum_{i=2}^{6} y_i \\right]",
                op="state_trapezoidal_formula",
                rule="trapezoidal_rule_7_ordinates",
            ),
            step(
                f"Half sum of ends: $\\frac{{{_fmt_sa(y[0])} + {_fmt_sa(y[-1])}}}{{2}} = {_fmt_sa(ends)}$. Intermediate sum: ${_fmt_sa(intermediates)}$.",
                to_latex=f"\\text{{Bracket sum}} = {_fmt_sa(ends + intermediates)}",
                op="sum_bracket_terms",
                rule="bracket_evaluation",
            ),
            step(
                f"Multiply by $h = {_fmt_sa(h)}$: $\\text{{Area}} = {_fmt_sa(h)} \\times {_fmt_sa(ends + intermediates)} = {_fmt_sa(area)}\\text{{ m}}^2$.",
                to_latex=ans_latex,
                op="calculate_area",
                rule="A = h * bracket",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"First find $\\frac{{y_1 + y_7}}{{2}} = \\frac{{{_fmt_sa(y[0])} + {_fmt_sa(y[-1])}}}{{2}} = {_fmt_sa(ends)}$.",
        f"Add intermediate ordinates $y_2$ to $y_6$: ${_fmt_sa(intermediates)}$.",
        f"Multiply by $h = {_fmt_sa(h)}$ to calculate the area: ${_fmt_sa(area)}\\text{{ m}}^2$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="32_trapezoidal_rule_odd_number_of_ordinates",
        lo_id=f"{LO_PREFIX}_32",
        difficulty="medium",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["misidentifying_number_of_intervals"],
    )


# ---------------------------------------------------------------------------
# 33. Trapezoidal Rule: Technical Metal Sheet Plate Area
# ---------------------------------------------------------------------------
def build_33_trapezoidal_rule_metal_sheet_plate_area(r: random.Random) -> Dict[str, Any]:
    # Technical mechanical plate with straight baseline and curved boundary
    h = r.choice([10, 15, 20])  # in cm
    y_cm = [round(r.uniform(15.0, 45.0), 1) for _ in range(6)]
    ends = round((y_cm[0] + y_cm[-1]) / 2, 2)
    intermediates = round(sum(y_cm[1:-1]), 2)
    area_cm2 = round(h * (ends + intermediates), 1)

    svg_code = (
        '<svg viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg">'
        '<rect width="600" height="200" fill="#f8fafc" rx="8"/>'
        '<!-- Flat steel base -->'
        '<line x1="60" y1="160" x2="540" y2="160" stroke="#334155" stroke-width="4"/>'
        '<!-- Curved profile plate -->'
        '<path d="M 60 160 L 60 110 Q 200 40 350 70 T 540 120 L 540 160 Z" fill="#94a3b8" opacity="0.5"/>'
        '<path d="M 60 110 Q 200 40 350 70 T 540 120" fill="none" stroke="#0f172a" stroke-width="3"/>'
        '<text x="300" y="185" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#1e293b">Machined Steel Plate Profile (Intervals h = ' + str(h) + ' cm)</text>'
        '</svg>'
    )

    d_spec = {
        "kind": "inline_svg",
        "svg": svg_code,
        "diagram_role": "context",
        "title": "Machined Steel Plate Irregular Profile",
    }

    y_str = ", \\; ".join(f"y_{{{i+1}}} = {_fmt_sa(val)}\\text{{ cm}}" for i, val in enumerate(y_cm))
    ans_latex = f"\\text{{Area}} = {_fmt_sa(area_cm2)}\\text{{ cm}}^2"

    prompt = (
        f"A template for a machined steel bracket shown above has a flat base with 6 ordinates measured at "
        f"equal intervals of $h = {h}\\text{{ cm}}$:\n$${y_str}$$\n\n"
        f"Use the trapezoidal rule to calculate the surface area of the steel bracket."
    )

    sg = solution_graph(
        [
            step(
                f"Trapezoidal rule: $\\text{{Area}} = h \\left[ \\frac{{y_1 + y_6}}{{2}} + y_2 + y_3 + y_4 + y_5 \\right]$.",
                to_latex="\\text{Area} = h \\left[ \\frac{y_1 + y_6}{2} + \\sum_{i=2}^5 y_i \\right]",
                op="formula",
                rule="trapezoidal_rule",
            ),
            step(
                f"Bracket sum: $\\frac{{{_fmt_sa(y_cm[0])} + {_fmt_sa(y_cm[-1])}}}{{2}} + ({' + '.join(_fmt_sa(v) for v in y_cm[1:-1])}) = {_fmt_sa(ends)} + {_fmt_sa(intermediates)} = {_fmt_sa(ends + intermediates)}\\text{{ cm}}$.",
                to_latex=f"\\text{{Bracket sum}} = {_fmt_sa(ends + intermediates)}\\text{{ cm}}",
                op="evaluate_bracket",
                rule="bracket_sum",
            ),
            step(
                f"Multiply by $h = {h}\\text{{ cm}}$: $\\text{{Area}} = {h} \\times {_fmt_sa(ends + intermediates)} = {_fmt_sa(area_cm2)}\\text{{ cm}}^2$.",
                to_latex=ans_latex,
                op="multiply_h",
                rule="A = h * bracket",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"Find $\\frac{{y_1 + y_6}}{{2}} = {_fmt_sa(ends)}$.",
        f"Sum intermediate ordinates: ${_fmt_sa(intermediates)}$.",
        f"Multiply by $h = {h}$: ${h} \\times {_fmt_sa(ends + intermediates)} = {_fmt_sa(area_cm2)}\\text{{ cm}}^2$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="33_trapezoidal_rule_metal_sheet_plate_area",
        lo_id=f"{LO_PREFIX}_33",
        difficulty="medium",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["unit_conversion_error_cm_to_m"],
        diagram_spec=d_spec,
    )


# ---------------------------------------------------------------------------
# 34. Trapezoidal Rule: Volume of Railway Embankment Cut-and-Fill
# ---------------------------------------------------------------------------
def build_34_trapezoidal_rule_volume_of_embankment(r: random.Random) -> Dict[str, Any]:
    h = r.choice([4, 5, 6])
    length_m = r.choice([50, 75, 100, 120])
    y = [round(r.uniform(2.0, 8.5), 1) for _ in range(6)]
    ends = round((y[0] + y[-1]) / 2, 2)
    intermediates = round(sum(y[1:-1]), 2)
    area = round(h * (ends + intermediates), 2)
    volume = round(area * length_m, 2)

    y_str = ", \\; ".join(f"y_{{{i+1}}} = {_fmt_sa(val)}\\text{{ m}}" for i, val in enumerate(y))
    ans_latex = f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2, \\quad \\text{{Volume}} = {_fmt_sa(volume)}\\text{{ m}}^3"

    prompt = (
        f"A railway embankment has a uniform cross-section along a stretch of $L = {length_m}\\text{{ m}}$. "
        f"The cross-section profile is surveyed using 6 boundary ordinates at equal intervals of $h = {h}\\text{{ m}}$:\n"
        f"$${y_str}$$\n\n"
        f"1. Use the trapezoidal rule to calculate the cross-sectional area of the embankment.\n"
        f"2. Hence, calculate the total volume of fill material in $\\text{{m}}^3$."
    )

    sg = solution_graph(
        [
            step(
                f"Cross-sectional area: $\\text{{Area}} = h \\left[ \\frac{{y_1 + y_6}}{{2}} + \\sum_{{i=2}}^5 y_i \\right] = {h} \\times ({_fmt_sa(ends)} + {_fmt_sa(intermediates)}) = {_fmt_sa(area)}\\text{{ m}}^2$.",
                to_latex=f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2",
                op="calculate_area",
                rule="trapezoidal_rule",
            ),
            step(
                f"Calculate embankment volume: $V = \\text{{Area}} \\times L = {_fmt_sa(area)} \\times {length_m} = {_fmt_sa(volume)}\\text{{ m}}^3$.",
                to_latex=ans_latex,
                op="calculate_volume",
                rule="V = A * L",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"First compute the area using the trapezoidal rule: $A = h [ (y_1 + y_6)/2 + y_2 + y_3 + y_4 + y_5 ]$.",
        f"Multiply the resulting area by the length $L = {length_m}\\text{{ m}}$ to find the volume.",
        f"Volume $= {_fmt_sa(area)} \\times {length_m} = {_fmt_sa(volume)}\\text{{ m}}^3$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="34_trapezoidal_rule_volume_of_embankment",
        lo_id=f"{LO_PREFIX}_34",
        difficulty="hard",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["confusing_cross_section_area_with_surface_area"],
        diagram_spec={
            "kind": "inline_svg",
            "diagram_role": "context",
            "plate": "/diagrams/blender_3d_triangular_prism_textbook.jpg",
            "blender_plate": "/diagrams/blender_3d_triangular_prism_textbook.jpg",
            "model_glb": "/models/blender_3d_triangular_prism.glb",
            "length": length_m,
            "h": h,
            "volume": volume,
            "svg": f"""<svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg"><rect width="300" height="150" fill="#f8fafc"/><text x="20" y="30" font-size="12" fill="#0f172a">Embankment: L={length_m}m, h={h}m</text><polygon points="40,120 150,40 260,120" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/></svg>""",
        },
    )


# ---------------------------------------------------------------------------
# 35. Trapezoidal vs Mid-ordinate Rule Comparison
# ---------------------------------------------------------------------------
def build_35_trapezoidal_vs_mid_ordinate_comparison(r: random.Random) -> Dict[str, Any]:
    # 5 boundary ordinates -> 4 intervals
    h = r.choice([2, 4])
    y = [round(r.uniform(2.0, 7.0), 1) for _ in range(5)]
    # Trapezoidal:
    a_trap = round(h * ((y[0] + y[-1]) / 2 + sum(y[1:-1])), 2)
    # Mid-ordinates derived from boundary ordinates:
    m = [(y[i] + y[i + 1]) / 2 for i in range(4)]
    a_mid = round(h * sum(m), 2)
    diff = round(abs(a_trap - a_mid), 2)

    y_str = ", \\; ".join(f"y_{{{i+1}}} = {_fmt_sa(val)}\\text{{ m}}" for i, val in enumerate(y))
    ans_latex = f"A_{{\\text{{trap}}}} = {_fmt_sa(a_trap)}\\text{{ m}}^2, \\quad A_{{\\text{{mid}}}} = {_fmt_sa(a_mid)}\\text{{ m}}^2, \\quad \\text{{Difference}} = {_fmt_sa(diff)}\\text{{ m}}^2"

    prompt = (
        f"Five boundary ordinates spaced at $h = {h}\\text{{ m}}$ measure:\n$${y_str}$$\n\n"
        f"1. Calculate the area using the **trapezoidal rule** ($A_{{\\text{{trap}}}}$).\n"
        f"2. Calculate the area using the **mid-ordinate rule** ($A_{{\\text{{mid}}}}$) by averaging adjacent boundary ordinates.\n"
        f"3. State the absolute difference between the two approximations."
    )

    sg = solution_graph(
        [
            step(
                f"Trapezoidal area: $A_{{\\text{{trap}}}} = {h} \\left[ \\frac{{{_fmt_sa(y[0])} + {_fmt_sa(y[-1])}}}{{2}} + {' + '.join(_fmt_sa(v) for v in y[1:-1])} \\right] = {_fmt_sa(a_trap)}\\text{{ m}}^2$.",
                to_latex=f"A_{{\\text{{trap}}}} = {_fmt_sa(a_trap)}\\text{{ m}}^2",
                op="calculate_trapezoidal",
                rule="trapezoidal_rule",
            ),
            step(
                f"Mid-ordinates: {', '.join(_fmt_sa(val) for val in m)}. Sum = {_fmt_sa(sum(m))}. Mid-ordinate area: $A_{{\\text{{mid}}}} = {h} \\times {_fmt_sa(sum(m))} = {_fmt_sa(a_mid)}\\text{{ m}}^2$.",
                to_latex=f"A_{{\\text{{mid}}}} = {_fmt_sa(a_mid)}\\text{{ m}}^2",
                op="calculate_mid_ordinate",
                rule="mid_ordinate_rule",
            ),
            step(
                f"Difference: $|{_fmt_sa(a_trap)} - {_fmt_sa(a_mid)}| = {_fmt_sa(diff)}\\text{{ m}}^2$.",
                to_latex=ans_latex,
                op="compare_approximations",
                rule="abs_difference",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"Evaluate the trapezoidal rule: $A_{{\\text{{trap}}}} = {_fmt_sa(a_trap)}\\text{{ m}}^2$.",
        f"Calculate the 4 mid-ordinates by averaging pairs of boundary ordinates, then multiply by $h$: $A_{{\\text{{mid}}}} = {_fmt_sa(a_mid)}\\text{{ m}}^2$.",
        f"Subtract the two areas to find the difference: ${_fmt_sa(diff)}\\text{{ m}}^2$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="35_trapezoidal_vs_mid_ordinate_comparison",
        lo_id=f"{LO_PREFIX}_35",
        difficulty="hard",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["confusing_the_two_numerical_integration_rules"],
    )


# ---------------------------------------------------------------------------
# 36. Definite Integral: Linear / Quadratic Area Under Curve
# ---------------------------------------------------------------------------
def build_36_definite_integral_polynomial_area_under_curve(r: random.Random) -> Dict[str, Any]:
    # Area under y = a*x^2 + b between x = p and x = q (p >= 0)
    a = r.choice([1, 2, 3])
    b = r.choice([1, 2, 4])
    p = r.choice([0, 1])
    q = r.choice([3, 4, 5])

    # \int_p^q (a*x^2 + b) dx = [ (a/3)*x^3 + b*x ]_p^q
    # Let's ensure a is a multiple of 3 or compute exact fraction / decimal:
    area_exact = (a * (q**3 - p**3)) / 3 + b * (q - p)
    s_area = _fmt_sa(area_exact)

    a_str = f"{a}x^2" if a != 1 else "x^2"
    fx_latex = f"{a_str} + {b}"
    ans_latex = f"\\text{{Area}} = \\int_{{{p}}}^{{{q}}} ({fx_latex}) \\, dx = {s_area} \\text{{ square units}}"

    prompt = (
        f"Use definite integration to calculate the exact area under the curve:\n"
        f"$$y = {fx_latex}$$\n"
        f"between $x = {p}$ and $x = {q}$ and bounded by the $x$-axis."
    )

    sg = solution_graph(
        [
            step(
                f"Set up the definite integral: $\\text{{Area}} = \\int_{{{p}}}^{{{q}}} ({fx_latex}) \\, dx$.",
                to_latex=f"\\int_{{{p}}}^{{{q}}} ({fx_latex}) \\, dx",
                op="set_up_integral",
                rule="area_under_curve_integral",
            ),
            step(
                f"Find the antiderivative: $\\int ({fx_latex}) \\, dx = \\left[ \\frac{{{a}}}{{3}}x^3 + {b}x \\right]_{{{p}}}^{{{q}}}$.",
                to_latex=f"\\left[ \\frac{{{a}}}{{3}}x^3 + {b}x \\right]_{{{p}}}^{{{q}}}",
                op="integrate_polynomial",
                rule="power_rule_of_integration",
            ),
            step(
                f"Evaluate at upper limit $x = {q}$ and subtract value at lower limit $x = {p}$: "
                f"$\\left( \\frac{{{a}}}{{3}}({q})^3 + {b}({q}) \\right) - \\left( \\frac{{{a}}}{{3}}({p})^3 + {b}({p}) \\right) = {s_area}$.",
                to_latex=ans_latex,
                op="fundamental_theorem_of_calculus",
                rule="F(b) - F(a)",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"Integrate each term using the power rule: $\\int x^n dx = \\frac{{x^{{n+1}}}}{{n+1}}$.",
        f"The antiderivative is $F(x) = \\frac{{{a}}}{{3}}x^3 + {b}x$.",
        f"Evaluate $F({q}) - F({p}) = {s_area}$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="36_definite_integral_polynomial_area_under_curve",
        lo_id=f"{LO_PREFIX}_36",
        difficulty="medium",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["differentiating_instead_of_integrating", "power_rule_subtraction_error"],
    )


# ---------------------------------------------------------------------------
# 37. Definite Integral: Cubic Curve Area Under Curve (y = ax^3)
# ---------------------------------------------------------------------------
def build_37_definite_integral_cubic_curve_area(r: random.Random) -> Dict[str, Any]:
    # y = a*x^3, a in {1, 2, 4}
    a = r.choice([1, 2, 4])
    p = 0
    q = r.choice([2, 3, 4])

    # \int_0^q a*x^3 dx = [ (a/4)*x^4 ]_0^q = (a/4) * q^4
    area_val = (a * (q**4)) / 4
    s_area = _fmt_sa(area_val)

    a_str = f"{a}x^3" if a != 1 else "x^3"
    ans_latex = f"\\text{{Area}} = \\int_{{0}}^{{{q}}} {a_str} \\, dx = {s_area} \\text{{ square units}}"

    prompt = (
        f"Determine the exact area bounded by the cubic curve:\n"
        f"$$y = {a_str}$$\n"
        f"the $x$-axis, and the vertical lines $x = 0$ and $x = {q}$."
    )

    sg = solution_graph(
        [
            step(
                f"Set up the area integral: $\\text{{Area}} = \\int_{{0}}^{{{q}}} {a_str} \\, dx$.",
                to_latex=f"\\int_{{0}}^{{{q}}} {a_str} \\, dx",
                op="set_up_integral",
                rule="definite_integral_area",
            ),
            step(
                f"Apply the power rule: $\\int {a_str} \\, dx = \\left[ \\frac{{{a}}}{{4}}x^4 \\right]_{{0}}^{{{q}}}$.",
                to_latex=f"\\left[ \\frac{{{a}}}{{4}}x^4 \\right]_{{0}}^{{{q}}}",
                op="integrate_cubic",
                rule="power_rule_n_equals_3",
            ),
            step(
                f"Substitute limits: $\\frac{{{a}}}{{4}}({q})^4 - 0 = \\frac{{{a}}}{{4}}({q**4}) = {s_area}$.",
                to_latex=ans_latex,
                op="evaluate_limits",
                rule="F(q) - F(0)",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"Apply the power rule of integration to $x^3$: $\\int x^3 dx = \\frac{{x^4}}{{4}}$.",
        f"Multiply by the coefficient ${a}$: $F(x) = \\frac{{{a}}}{{4}}x^4$.",
        f"Substitute $x = {q}$ to obtain the area: ${s_area}$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="37_definite_integral_cubic_curve_area",
        lo_id=f"{LO_PREFIX}_37",
        difficulty="medium",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["dividing_by_3_instead_of_4_for_cubic_integral"],
    )


# ---------------------------------------------------------------------------
# 38. Definite Integral: Fractional Power Curve Area (y = k * sqrt(x))
# ---------------------------------------------------------------------------
def build_38_definite_integral_fractional_power_curve_area(r: random.Random) -> Dict[str, Any]:
    # y = k * x^(1/2)
    # \int_0^q k * x^(1/2) dx = [ k * (2/3) * x^(3/2) ]_0^q
    # Choose q = 4 or 9 (perfect squares) and k a multiple of 3:
    k = r.choice([3, 6])
    q = r.choice([4, 9])
    # x^(3/2) at q:
    root_q = math.isqrt(q)
    q_pow_1_5 = root_q ** 3
    area_val = k * (2 / 3) * q_pow_1_5
    s_area = _fmt_sa(area_val)

    ans_latex = f"\\text{{Area}} = \\int_{{0}}^{{{q}}} {k}\\sqrt{{x}} \\, dx = {s_area} \\text{{ square units}}"
    prompt = (
        f"Calculate the area bounded by the radical curve:\n"
        f"$$y = {k}\\sqrt{{x}}$$\n"
        f"the $x$-axis, and the vertical line $x = {q}$."
    )

    sg = solution_graph(
        [
            step(
                f"Express the square root in fractional index form: $y = {k}x^{{\\frac{{1}}{{2}}}}$.",
                to_latex=f"y = {k}x^{{1/2}}",
                op="convert_to_power",
                rule="sqrt_x = x^(1/2)",
            ),
            step(
                f"Integrate using the power rule: $\\int {k}x^{{\\frac{{1}}{{2}}}} \\, dx = \\left[ {k} \\times \\frac{{x^{{\\frac{{3}}{{2}}}}}}{{\\frac{{3}}{{2}}}} \\right]_{{0}}^{{{q}}} = \\left[ \\frac{{{2 * k}}}{{3}} x^{{\\frac{{3}}{{2}}}} \\right]_{{0}}^{{{q}}}$.",
                to_latex=f"\\left[ {int(2 * k / 3)} x^{{3/2}} \\right]_{{0}}^{{{q}}}",
                op="integrate_fractional_power",
                rule="power_rule_half",
            ),
            step(
                f"Evaluate at $x = {q}$: since ${q}^{{\\frac{{3}}{{2}}}} = (\\sqrt{{{q}}})^3 = {root_q}^3 = {q_pow_1_5}$, the area is ${int(2 * k / 3)} \\times {q_pow_1_5} = {s_area}$.",
                to_latex=ans_latex,
                op="evaluate_at_bound",
                rule="fractional_power_evaluation",
            ),
        ],
        canonical_form=ans_latex,
    )

    hints = [
        f"Write $\\sqrt{{x}}$ as $x^{{\\frac{{1}}{{2}}}}$.",
        f"The antiderivative is $\\frac{{{k} x^{{3/2}}}}{{3/2}} = \\frac{{{2 * k}}}{{3}} x^{{3/2}}$.",
        f"Substitute $x = {q}$: evaluate $(\\sqrt{{{q}}})^3 = {q_pow_1_5}$ and multiply to get ${s_area}$.",
    ]

    return make_math_question(
        topic=TOPIC,
        subskill="38_definite_integral_fractional_power_curve_area",
        lo_id=f"{LO_PREFIX}_38",
        difficulty="hard",
        question_text=prompt,
        expected_answer=ans_latex,
        canonical_solution=sg,
        hints=hints,
        misconception_tags=["fractional_exponent_integration_error", "evaluating_fractional_power_incorrectly"],
    )


# Export dictionary of Archetypes 26–38
BUILDERS_26_38: Dict[str, Any] = {
    "26_mid_ordinate_rule_formula_direct": build_26_mid_ordinate_rule_formula_direct,
    "27_mid_ordinate_rule_calculate_midpoints": build_27_mid_ordinate_rule_calculate_midpoints,
    "28_mid_ordinate_rule_river_cross_section": build_28_mid_ordinate_rule_river_cross_section,
    "29_mid_ordinate_rule_water_reservoir_cross_section": build_29_mid_ordinate_rule_water_reservoir_cross_section,
    "30_mid_ordinate_rule_with_prismoidal_volume": build_30_mid_ordinate_rule_with_prismoidal_volume,
    "31_trapezoidal_rule_boundary_ordinates_direct": build_31_trapezoidal_rule_boundary_ordinates_direct,
    "32_trapezoidal_rule_odd_number_of_ordinates": build_32_trapezoidal_rule_odd_number_of_ordinates,
    "33_trapezoidal_rule_metal_sheet_plate_area": build_33_trapezoidal_rule_metal_sheet_plate_area,
    "34_trapezoidal_rule_volume_of_embankment": build_34_trapezoidal_rule_volume_of_embankment,
    "35_trapezoidal_vs_mid_ordinate_comparison": build_35_trapezoidal_vs_mid_ordinate_comparison,
    "36_definite_integral_polynomial_area_under_curve": build_36_definite_integral_polynomial_area_under_curve,
    "37_definite_integral_cubic_curve_area": build_37_definite_integral_cubic_curve_area,
    "38_definite_integral_fractional_power_curve_area": build_38_definite_integral_fractional_power_curve_area,
}
