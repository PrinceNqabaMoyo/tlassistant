"""Grade 11–12 Technical Mathematics — Mensuration & Calculus Archetypes 01 to 25.

Grounded strictly in CAPS Technical Mathematics:
- Grade 11 Term 4 Mensuration (right prisms, cylinders, hollow cylinders, pyramids, cones, spheres, composite solids, dimensional scaling)
- Numerical Integration (common interval width h, mid-ordinate rule, trapezoidal rule, engineering excavation volumes and masses)
- Grade 12 Term 1 Integration (indefinite integrals, power rule, negative/fractional powers, definite integrals, area under curve)

100% deterministic, zero-LLM, South African National Curriculum Standards compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

TERM = 4
CAPS_WEIGHT = 25
SUGGESTED_DURATION = 8
TOPIC_ID = "technical_mathematics_mensuration"
LEARNING_OBJECTIVE = "techmath_mensuration_calculus"


def _fmt_sa(val: float | int, places: int = 2) -> str:
    """Format number with SA comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _base_contract(
    subskill: str,
    prompt: str,
    answer: str,
    options: Optional[List[str]],
    sol_steps: List[Dict[str, str]],
    t1: str,
    t2: str,
    t3: str,
    misconceptions: List[str],
    marks: int = 4,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Helper to enforce universal 6-pillar contract."""
    q: Dict[str, Any] = {
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT,
        "suggested_duration_mins": SUGGESTED_DURATION,
        "topic": TOPIC_ID,
        "learning_objective_id": LEARNING_OBJECTIVE,
        "subskill": subskill,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "mcq" if options else "short_answer",
        "total_marks": marks,
        "misconception_tags": misconceptions,
        "hints": [
            {"tier": 1, "title": "Key Concept", "text": t1},
            {"tier": 2, "title": "Formula / Method", "text": t2},
            {"tier": 3, "title": "Worked Step", "text": t3},
        ],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{subskill}_{i+1}", "desc": s.get("rule", "Correct calculation step"), "marks": 1, "editable": True}
                for i, s in enumerate(sol_steps[:marks])
            ],
            "deductions": [{"rule": "omitted_units", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "solution_steps": sol_steps,
        "sample_answer": answer,
        "worked_solution": "\n".join([f"- **Step {i+1}**: {s.get('op', '')} $\\implies$ ${s.get('to', '')}$" for i, s in enumerate(sol_steps)]),
    }
    if options:
        q["options"] = options
        q["correct_index"] = options.index(answer)
        q["options_latex"] = options
    else:
        q["answer_latex"] = answer
        q["answer_value"] = answer
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


def _make_svg_trapezoid_rule(
    h: float | int,
    ordinates: List[float],
    unit: str = "m",
    viewbox: str = "0 0 500 240",
) -> str:
    """Build dynamic SVG for Trapezoidal / Mid-ordinate rule cross-section."""
    n = len(ordinates)
    dx = 400.0 / max(1, n - 1)
    max_y = max(ordinates) if ordinates else 10.0
    scale_y = 140.0 / max(max_y, 1.0)
    base_y = 190.0

    svg_parts = [
        f'<svg viewBox="{viewbox}" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">',
        '<style>',
        '  .baseline { stroke: #0f172a; stroke-width: 2.5; stroke-linecap: round; }',
        '  .curve { stroke: #2563eb; stroke-width: 2.5; fill: #eff6ff; fill-opacity: 0.6; }',
        '  .ord { stroke: #3b82f6; stroke-width: 1.5; stroke-dasharray: 4,3; }',
        '  .dim { stroke: #64748b; stroke-width: 1; }',
        '  .txt { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: 600; text-anchor: middle; }',
        '  .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; fill: #1e293b; font-weight: bold; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
    ]

    # Curve path points
    pts = []
    for i, y in enumerate(ordinates):
        px = 50.0 + i * dx
        py = base_y - y * scale_y
        pts.append((px, py))

    # Fill polygon
    poly_d = [f"M 50.0 {base_y}"]
    for px, py in pts:
        poly_d.append(f"L {px:.1f} {py:.1f}")
    poly_d.append(f"L {50.0 + (n-1)*dx:.1f} {base_y} Z")
    svg_parts.append(f'<path d="{" ".join(poly_d)}" class="curve" />')

    # Baseline
    svg_parts.append(f'<line x1="40" y1="{base_y}" x2="{50 + (n-1)*dx + 10}" y2="{base_y}" class="baseline" />')

    # Ordinates & Labels
    for i, (px, py) in enumerate(pts):
        svg_parts.append(f'<line x1="{px:.1f}" y1="{base_y}" x2="{px:.1f}" y2="{py:.1f}" class="ord" />')
        val_str = _fmt_sa(ordinates[i])
        svg_parts.append(f'<text x="{px:.1f}" y="{py - 6:.1f}" class="txt">y_{i+1}={val_str}</text>')
        svg_parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.5" fill="#2563eb" />')

    # Interval width marker
    if n >= 2:
        x_mid = 50.0 + 0.5 * dx
        svg_parts.append(f'<line x1="50" y1="{base_y + 16}" x2="{50 + dx}" y2="{base_y + 16}" class="dim" />')
        svg_parts.append(f'<text x="{x_mid:.1f}" y="{base_y + 28}" class="txt">h = {h} {unit}</text>')

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


def _make_svg_solid_isometric(solid_type: str, d1: float, d2: float, d3: float = 0.0) -> str:
    """Build clean dynamic vector SVG for 3D technical solids."""
    viewbox = "0 0 400 220"
    svg_parts = [
        f'<svg viewBox="{viewbox}" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">',
        '<style>',
        '  .face { fill: #e0f2fe; stroke: #0284c7; stroke-width: 1.8; fill-opacity: 0.7; }',
        '  .face-dark { fill: #bae6fd; stroke: #0284c7; stroke-width: 1.8; fill-opacity: 0.8; }',
        '  .face-top { fill: #f0f9ff; stroke: #0284c7; stroke-width: 1.8; }',
        '  .dashed { stroke: #64748b; stroke-width: 1.2; stroke-dasharray: 4,3; }',
        '  .dim { stroke: #dc2626; stroke-width: 1.2; }',
        '  .dim-txt { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #dc2626; font-weight: bold; text-anchor: middle; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
    ]

    if solid_type == "cylinder":
        # Cylinder: r = d1, h = d2
        svg_parts.append('<ellipse cx="200" cy="50" rx="70" ry="22" class="face-top" />')
        svg_parts.append('<path d="M 130 50 L 130 150 A 70 22 0 0 0 270 150 L 270 50 Z" class="face" />')
        svg_parts.append('<ellipse cx="200" cy="150" rx="70" ry="22" class="face" fill="none" stroke="#0284c7" stroke-width="1.8" />')
        svg_parts.append('<line x1="200" y1="50" x2="270" y2="50" class="dim" />')
        svg_parts.append(f'<text x="235" y="44" class="dim-txt">r = {_fmt_sa(d1)}</text>')
        svg_parts.append('<line x1="285" y1="50" x2="285" y2="150" class="dim" />')
        svg_parts.append(f'<text x="315" y="105" class="dim-txt">h = {_fmt_sa(d2)}</text>')
    elif solid_type == "cone":
        # Cone: r = d1, h = d2
        svg_parts.append('<ellipse cx="200" cy="160" rx="75" ry="22" class="face" />')
        svg_parts.append('<polygon points="200,35 125,160 275,160" class="face-dark" />')
        svg_parts.append('<line x1="200" y1="35" x2="200" y2="160" class="dashed" />')
        svg_parts.append('<line x1="200" y1="160" x2="275" y2="160" class="dim" />')
        svg_parts.append(f'<text x="240" y="154" class="dim-txt">r = {_fmt_sa(d1)}</text>')
        svg_parts.append(f'<text x="180" y="105" class="dim-txt">h = {_fmt_sa(d2)}</text>')
    elif solid_type == "sphere":
        # Sphere: r = d1
        svg_parts.append('<circle cx="200" cy="110" r="70" class="face" />')
        svg_parts.append('<ellipse cx="200" cy="110" rx="70" ry="20" class="dashed" fill="none" />')
        svg_parts.append('<line x1="200" y1="110" x2="270" y2="110" class="dim" />')
        svg_parts.append(f'<text x="235" y="104" class="dim-txt">r = {_fmt_sa(d1)}</text>')
    else:
        # Rectangular / general prism: l = d1, w = d2, h = d3
        svg_parts.append('<polygon points="120,80 220,80 220,160 120,160" class="face" />')
        svg_parts.append('<polygon points="220,80 280,45 280,125 220,160" class="face-dark" />')
        svg_parts.append('<polygon points="120,80 180,45 280,45 220,80" class="face-top" />')
        svg_parts.append(f'<text x="170" y="175" class="dim-txt">L = {_fmt_sa(d1)}</text>')
        svg_parts.append(f'<text x="260" y="150" class="dim-txt">W = {_fmt_sa(d2)}</text>')
        if d3 > 0:
            svg_parts.append(f'<text x="105" y="125" class="dim-txt">H = {_fmt_sa(d3)}</text>')

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


def _make_svg_area_under_curve(func_name: str, a: float, b: float) -> str:
    """Build dynamic SVG for definite integral area under curve."""
    viewbox = "0 0 400 220"
    svg_parts = [
        f'<svg viewBox="{viewbox}" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">',
        '<style>',
        '  .axis { stroke: #0f172a; stroke-width: 1.5; }',
        '  .grid { stroke: #e2e8f0; stroke-width: 1; }',
        '  .curve { stroke: #2563eb; stroke-width: 2.5; fill: none; }',
        '  .shaded { fill: #3b82f6; fill-opacity: 0.35; stroke: #2563eb; stroke-width: 1.5; }',
        '  .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; fill: #0f172a; font-weight: bold; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '<line x1="40" y1="170" x2="360" y2="170" class="axis" />',
        '<line x1="80" y1="20" x2="80" y2="190" class="axis" />',
        '<text x="365" y="174" class="lbl">x</text>',
        '<text x="84" y="25" class="lbl">y</text>',
    ]
    # Parabolic curve y = 0.08 x^2
    d_path = []
    shade_path = [f"M {120} 170"]
    for x_val in range(20, 280, 5):
        px = 80 + x_val
        py = 170 - (0.0022 * (x_val**2))
        cmd = "M" if x_val == 20 else "L"
        d_path.append(f"{cmd} {px:.1f} {py:.1f}")
        if 60 <= x_val <= 180:
            shade_path.append(f"L {px:.1f} {py:.1f}")

    shade_path.append(f"L {80 + 180} 170 Z")
    svg_parts.append(f'<path d="{" ".join(shade_path)}" class="shaded" />')
    svg_parts.append(f'<path d="{" ".join(d_path)}" class="curve" />')
    svg_parts.append(f'<text x="140" y="185" class="lbl">x = {_fmt_sa(a)}</text>')
    svg_parts.append(f'<text x="260" y="185" class="lbl">x = {_fmt_sa(b)}</text>')
    svg_parts.append(f'<text x="210" y="60" class="lbl">{func_name}</text>')
    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


# =========================================================================== #
# Archetypes 01 to 25
# =========================================================================== #

def _build_01(rng: random.Random) -> Dict[str, Any]:
    sub = "01_interval_width_and_ordinate_count"
    total_span = rng.choice([18, 24, 30, 36, 42, 48, 54, 60, 72])
    num_intervals = rng.choice([3, 4, 5, 6, 8])
    h = round(total_span / num_intervals, 2)
    num_ordinates = num_intervals + 1

    ans = f"$N = {num_ordinates}\\quad\\text{{and}}\\quad h = {_fmt_sa(h)}\\text{{ m}}$"
    d1 = f"$N = {num_intervals}\\quad\\text{{and}}\\quad h = {_fmt_sa(h)}\\text{{ m}}$"
    d2 = f"$N = {num_ordinates}\\quad\\text{{and}}\\quad h = {_fmt_sa(round(total_span / num_ordinates, 2))}\\text{{ m}}$"
    d3 = f"$N = {num_intervals + 2}\\quad\\text{{and}}\\quad h = {_fmt_sa(h)}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    prompt = (
        f"An irregular civil engineering road cutting has a total baseline span of ${total_span}\\text{{ m}}$. "
        f"The span is divided into **{num_intervals} equal intervals** to measure transverse boundary ordinates. "
        f"Determine the total number of boundary ordinates ($N$) and the common interval width ($h$)."
    )
    steps = [
        {"rule": "Identify total number of ordinates", "op": f"N = n + 1 = {num_intervals} + 1", "to": f"N = {num_ordinates}"},
        {"rule": "Calculate common interval width h", "op": f"h = \\frac{{\\text{{total span}}}}{{n}} = \\frac{{{total_span}}}{{{num_intervals}}}", "to": f"h = {_fmt_sa(h)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="For n equal intervals, there are exactly N = n + 1 boundary ordinates.",
        t2=f"The interval width is h = total span / n = {total_span} / {num_intervals}.",
        t3=f"N = {num_ordinates} and h = {_fmt_sa(h)} m.",
        misconceptions=["counted_intervals_as_ordinates", "divided_by_ordinates_count", "unit_confusion"],
        marks=2,
    )


def _build_02(rng: random.Random) -> Dict[str, Any]:
    sub = "02_mid_ordinate_rule_calculation"
    h = rng.choice([2, 3, 4, 5])
    m1 = rng.choice([3.2, 4.0, 4.5])
    m2 = rng.choice([5.8, 6.2, 7.0])
    m3 = rng.choice([8.0, 8.5, 9.4])
    m4 = rng.choice([6.4, 7.1, 7.8])
    m_list = [m1, m2, m3, m4]
    sum_m = round(sum(m_list), 2)
    area = round(h * sum_m, 2)

    ans = f"$\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2$"
    d1 = f"$\\text{{Area}} = {_fmt_sa(round(area / 2, 2))}\\text{{ m}}^2$"
    d2 = f"$\\text{{Area}} = {_fmt_sa(round(sum_m, 2))}\\text{{ m}}^2$"
    d3 = f"$\\text{{Area}} = {_fmt_sa(round(area * 2, 2))}\\text{{ m}}^2$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    m_str = ", ".join([f"m_{i+1} = {_fmt_sa(v)}\\text{{ m}}" for i, v in enumerate(m_list)])
    svg = _make_svg_trapezoid_rule(h, m_list)
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Mid-ordinate rule irregular cross section"}

    prompt = (
        f"In the accompanying diagram, an irregular cross-sectional area is measured using four equal intervals of width $h = {h}\\text{{ m}}$. "
        f"The measured mid-ordinates are: $${m_str}$$\n"
        f"Use the **Mid-ordinate Rule** ($\\text{{Area}} = h \\sum m$) to calculate the total cross-sectional area."
    )
    steps = [
        {"rule": "Sum all mid-ordinates", "op": f"\\sum m = {_fmt_sa(m1)} + {_fmt_sa(m2)} + {_fmt_sa(m3)} + {_fmt_sa(m4)}", "to": f"\\sum m = {_fmt_sa(sum_m)}\\text{{ m}}"},
        {"rule": "Multiply by common interval width h", "op": f"\\text{{Area}} = h \\times \\sum m = {h} \\times {_fmt_sa(sum_m)}", "to": f"\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The Mid-ordinate Rule states: Area = h * (sum of mid-ordinates).",
        t2=f"Add all mid-ordinates: {_fmt_sa(m1)} + {_fmt_sa(m2)} + {_fmt_sa(m3)} + {_fmt_sa(m4)} = {_fmt_sa(sum_m)}.",
        t3=f"Multiply by interval width h = {h}: Area = {h} * {_fmt_sa(sum_m)} = {_fmt_sa(area)} m^2.",
        misconceptions=["divided_first_last_by_two_mid_ordinate", "forgot_to_multiply_by_h", "arithmetic_sum_error"],
        marks=3,
        diagram_spec=diag,
    )


def _build_03(rng: random.Random) -> Dict[str, Any]:
    sub = "03_trapezoidal_rule_four_intervals"
    h = rng.choice([2, 3, 4, 5])
    y1 = rng.choice([1.0, 2.0, 2.5])
    y2 = rng.choice([4.2, 5.0, 5.6])
    y3 = rng.choice([6.8, 7.5, 8.2])
    y4 = rng.choice([4.0, 5.2, 6.0])
    y5 = rng.choice([0.8, 1.6, 2.2])
    ords = [y1, y2, y3, y4, y5]

    ends_avg = round((y1 + y5) / 2, 2)
    mids = round(y2 + y3 + y4, 2)
    area = round(h * (ends_avg + mids), 2)

    ans = f"$\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2$"
    d1 = f"$\\text{{Area}} = {_fmt_sa(round(h * sum(ords), 2))}\\text{{ m}}^2$"
    d2 = f"$\\text{{Area}} = {_fmt_sa(round(area / 2, 2))}\\text{{ m}}^2$"
    d3 = f"$\\text{{Area}} = {_fmt_sa(round(ends_avg + mids, 2))}\\text{{ m}}^2$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_trapezoid_rule(h, ords)
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Trapezoidal rule with 5 boundary ordinates"}

    ords_str = ", ".join([f"y_{i+1} = {_fmt_sa(v)}\\text{{ m}}" for i, v in enumerate(ords)])
    prompt = (
        f"In the accompanying diagram, an irregular boundary has $5$ measured ordinates spaced at equal intervals of $h = {h}\\text{{ m}}$:\n"
        f"$${ords_str}$$\n"
        f"Calculate the approximate area using the **Trapezoidal Rule**."
    )
    steps = [
        {"rule": "Calculate average of first and last ordinates", "op": f"\\frac{{y_1 + y_5}}{{2}} = \\frac{{{_fmt_sa(y1)} + {_fmt_sa(y5)}}}{{2}}", "to": f"{_fmt_sa(ends_avg)}"},
        {"rule": "Sum intermediate ordinates", "op": f"y_2 + y_3 + y_4 = {_fmt_sa(y2)} + {_fmt_sa(y3)} + {_fmt_sa(y4)}", "to": f"{_fmt_sa(mids)}"},
        {"rule": "Apply Trapezoidal formula", "op": f"\\text{{Area}} = {h} \\left[ {_fmt_sa(ends_avg)} + {_fmt_sa(mids)} \\right]", "to": f"{_fmt_sa(area)}\\text{{ m}}^2"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Trapezoidal Rule formula: Area = h * [(y_1 + y_n)/2 + y_2 + ... + y_{n-1}].",
        t2=f"Ends average: ({_fmt_sa(y1)} + {_fmt_sa(y5)})/2 = {_fmt_sa(ends_avg)}. Intermediate sum = {_fmt_sa(mids)}.",
        t3=f"Area = {h} * ({_fmt_sa(ends_avg)} + {_fmt_sa(mids)}) = {_fmt_sa(area)} m^2.",
        misconceptions=["omitted_half_first_last_ordinates", "added_all_ordinates_equally", "multiplication_error"],
        marks=4,
        diagram_spec=diag,
    )


def _build_04(rng: random.Random) -> Dict[str, Any]:
    sub = "04_trapezoidal_rule_five_intervals"
    h = rng.choice([2, 3, 4, 6])
    y1 = rng.choice([0.0, 1.5, 2.0])
    y2 = rng.choice([3.6, 4.4, 5.2])
    y3 = rng.choice([6.2, 7.0, 8.1])
    y4 = rng.choice([7.4, 8.5, 9.0])
    y5 = rng.choice([4.8, 5.6, 6.2])
    y6 = rng.choice([0.0, 1.8, 2.4])
    ords = [y1, y2, y3, y4, y5, y6]

    ends_avg = round((y1 + y6) / 2, 2)
    mids = round(y2 + y3 + y4 + y5, 2)
    area = round(h * (ends_avg + mids), 2)

    ans = f"$\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2$"
    d1 = f"$\\text{{Area}} = {_fmt_sa(round(h * sum(ords), 2))}\\text{{ m}}^2$"
    d2 = f"$\\text{{Area}} = {_fmt_sa(round(area + h * 2, 2))}\\text{{ m}}^2$"
    d3 = f"$\\text{{Area}} = {_fmt_sa(round(area - h * 2, 2))}\\text{{ m}}^2$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_trapezoid_rule(h, ords)
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Trapezoidal rule with 6 ordinates"}

    ords_str = ", ".join([f"y_{i+1} = {_fmt_sa(v)}" for i, v in enumerate(ords)])
    prompt = (
        f"In the accompanying diagram, an irregular embankment profile has $6$ boundary ordinates measured at equal intervals of $h = {h}\\text{{ m}}$:\n"
        f"$${ords_str}\\text{{ (all in metres)}}$$\n"
        f"Apply the **Trapezoidal Rule** to calculate the area of the profile."
    )
    steps = [
        {"rule": "Calculate average of end ordinates", "op": f"\\frac{{y_1 + y_6}}{{2}} = \\frac{{{_fmt_sa(y1)} + {_fmt_sa(y6)}}}{{2}}", "to": f"{_fmt_sa(ends_avg)}"},
        {"rule": "Sum interior ordinates", "op": f"\\sum y_{{mid}} = {_fmt_sa(y2)} + {_fmt_sa(y3)} + {_fmt_sa(y4)} + {_fmt_sa(y5)}", "to": f"{_fmt_sa(mids)}"},
        {"rule": "Multiply by h", "op": f"\\text{{Area}} = {h} \\times ({_fmt_sa(ends_avg)} + {_fmt_sa(mids)})", "to": f"{_fmt_sa(area)}\\text{{ m}}^2"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="For 6 ordinates (5 intervals), average y_1 and y_6, then add y_2, y_3, y_4, y_5.",
        t2=f"Ends: ({_fmt_sa(y1)} + {_fmt_sa(y6)})/2 = {_fmt_sa(ends_avg)}. Middle sum = {_fmt_sa(mids)}.",
        t3=f"Area = {h} * ({_fmt_sa(ends_avg)} + {_fmt_sa(mids)}) = {_fmt_sa(area)} m^2.",
        misconceptions=["divided_all_by_two", "omitted_y5", "arithmetic_sum_error"],
        marks=4,
        diagram_spec=diag,
    )


def _build_05(rng: random.Random) -> Dict[str, Any]:
    sub = "05_trapezoidal_rule_six_intervals"
    h = rng.choice([2.5, 3.0, 4.0, 5.0])
    ords = [rng.choice([1.2, 2.0]), rng.choice([3.8, 4.5]), rng.choice([5.6, 6.2]), rng.choice([7.0, 7.8]), rng.choice([6.4, 7.2]), rng.choice([4.0, 4.8]), rng.choice([1.0, 1.8])]
    ends_avg = round((ords[0] + ords[-1]) / 2, 2)
    mids = round(sum(ords[1:-1]), 2)
    area = round(h * (ends_avg + mids), 2)

    ans = f"$\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2$"
    d1 = f"$\\text{{Area}} = {_fmt_sa(round(h * sum(ords), 2))}\\text{{ m}}^2$"
    d2 = f"$\\text{{Area}} = {_fmt_sa(round(area * 1.1, 2))}\\text{{ m}}^2$"
    d3 = f"$\\text{{Area}} = {_fmt_sa(round(area * 0.9, 2))}\\text{{ m}}^2$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_trapezoid_rule(h, ords)
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Trapezoidal rule with 7 ordinates"}

    ords_str = ", ".join([f"y_{i+1} = {_fmt_sa(v)}" for i, v in enumerate(ords)])
    prompt = (
        f"In the accompanying diagram, an irregular cross-section is surveyed using $6$ equal intervals of width $h = {_fmt_sa(h)}\\text{{ m}}$. "
        f"The $7$ measured ordinates are: $${ords_str}\\text{{ m}}$$\n"
        f"Calculate the cross-sectional area using the **Trapezoidal Rule**."
    )
    steps = [
        {"rule": "Average ends", "op": f"\\frac{{{_fmt_sa(ords[0])} + {_fmt_sa(ords[-1])}}}{{2}}", "to": f"{_fmt_sa(ends_avg)}"},
        {"rule": "Sum interior ordinates", "op": f"\\sum_{{i=2}}^6 y_i", "to": f"{_fmt_sa(mids)}"},
        {"rule": "Evaluate area", "op": f"{_fmt_sa(h)} \\times ({_fmt_sa(ends_avg)} + {_fmt_sa(mids)})", "to": f"{_fmt_sa(area)}\\text{{ m}}^2"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Apply Area = h * [(y_1 + y_7)/2 + y_2 + y_3 + y_4 + y_5 + y_6].",
        t2=f"Ends average = {_fmt_sa(ends_avg)}, internal sum = {_fmt_sa(mids)}.",
        t3=f"Area = {_fmt_sa(h)} * ({_fmt_sa(ends_avg)} + {_fmt_sa(mids)}) = {_fmt_sa(area)} m^2.",
        misconceptions=["omitted_one_interior_ordinate", "arithmetic_multiplication_error", "rounding_error"],
        marks=4,
        diagram_spec=diag,
    )


def _build_06(rng: random.Random) -> Dict[str, Any]:
    sub = "06_irregular_excavation_volume_from_cross_section"
    h = rng.choice([3, 4, 5])
    L = rng.choice([30, 40, 50, 60, 80])
    ords = [rng.choice([1.0, 2.0]), rng.choice([4.2, 5.0]), rng.choice([6.8, 7.5]), rng.choice([5.4, 6.0]), rng.choice([1.2, 2.2])]
    ends = round((ords[0] + ords[-1]) / 2, 2)
    mids = round(sum(ords[1:-1]), 2)
    area = round(h * (ends + mids), 2)
    vol = round(area * L, 2)

    ans = f"$V = {_fmt_sa(vol)}\\text{{ m}}^3$"
    d1 = f"$V = {_fmt_sa(round(area * L * 0.5, 2))}\\text{{ m}}^3$"
    d2 = f"$V = {_fmt_sa(round(area + L, 2))}\\text{{ m}}^3$"
    d3 = f"$V = {_fmt_sa(round(vol * 1.5, 2))}\\text{{ m}}^3$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_trapezoid_rule(h, ords)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_rectangular_prism_textbook.jpg",
        "model_glb": "/models/blender_3d_rectangular_prism.glb",
        "alt_text": "Excavation trench rectangular prism 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, an irregular ditch cross-section has $5$ ordinates measured at intervals of $h = {h}\\text{{ m}}$: "
        f"${', '.join([_fmt_sa(v) for v in ords])}\\text{{ m}}$. "
        f"If the ditch is excavated over a uniform length of $L = {L}\\text{{ m}}$, calculate the total volume of excavation in $\\text{{m}}^3$."
    )
    steps = [
        {"rule": "Calculate cross-sectional area A using Trapezoidal Rule", "op": f"A = {h} \\left[ \\frac{{{_fmt_sa(ords[0])} + {_fmt_sa(ords[-1])}}}{{2}} + {_fmt_sa(mids)} \\right]", "to": f"A = {_fmt_sa(area)}\\text{{ m}}^2"},
        {"rule": "Calculate excavation volume", "op": f"V = A \\times L = {_fmt_sa(area)} \\times {L}", "to": f"V = {_fmt_sa(vol)}\\text{{ m}}^3"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="First calculate the cross-sectional area A via the Trapezoidal Rule, then multiply by length L to get volume V.",
        t2=f"A = {_fmt_sa(area)} m^2. Then V = A * L = {_fmt_sa(area)} * {L}.",
        t3=f"V = {_fmt_sa(vol)} m^3.",
        misconceptions=["divided_volume_by_three_pyramid", "forgot_to_multiply_by_length", "unit_m2_instead_of_m3"],
        marks=4,
        diagram_spec=diag,
    )


def _build_07(rng: random.Random) -> Dict[str, Any]:
    sub = "07_civil_engineering_earthwork_mass_calculation"
    h = rng.choice([2, 3, 4])
    L = rng.choice([20, 25, 30, 40])
    density = rng.choice([1.6, 1.8, 2.2, 2.4])  # tonnes/m^3
    ords = [rng.choice([1.0, 1.5]), rng.choice([3.2, 4.0]), rng.choice([5.5, 6.0]), rng.choice([3.0, 3.8]), rng.choice([0.8, 1.2])]
    ends = round((ords[0] + ords[-1]) / 2, 2)
    mids = round(sum(ords[1:-1]), 2)
    area = round(h * (ends + mids), 2)
    vol = round(area * L, 2)
    mass = round(vol * density, 1)

    ans = f"$\\text{{Mass}} = {_fmt_sa(mass)}\\text{{ tonnes}}$"
    d1 = f"$\\text{{Mass}} = {_fmt_sa(round(vol / density, 1))}\\text{{ tonnes}}$"
    d2 = f"$\\text{{Mass}} = {_fmt_sa(round(area * density, 1))}\\text{{ tonnes}}$"
    d3 = f"$\\text{{Mass}} = {_fmt_sa(round(mass * 1.2, 1))}\\text{{ tonnes}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_trapezoid_rule(h, ords)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_rectangular_prism_textbook.jpg",
        "model_glb": "/models/blender_3d_rectangular_prism.glb",
        "alt_text": "Earthwork excavation rectangular prism 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, an earthwork cutting has $5$ measured ordinates spaced at $h = {h}\\text{{ m}}$: "
        f"${', '.join([_fmt_sa(v) for v in ords])}\\text{{ m}}$. "
        f"The cutting extends over a length of $L = {L}\\text{{ m}}$. "
        f"Given that the excavated soil has a density of $\\rho = {_fmt_sa(density)}\\text{{ tonnes/m}}^3$, calculate the total mass in tonnes."
    )
    steps = [
        {"rule": "Calculate cross-sectional area A", "op": f"A = {h} \\left[ {_fmt_sa(ends)} + {_fmt_sa(mids)} \\right]", "to": f"A = {_fmt_sa(area)}\\text{{ m}}^2"},
        {"rule": "Compute volume V", "op": f"V = {_fmt_sa(area)} \\times {L}", "to": f"V = {_fmt_sa(vol)}\\text{{ m}}^3"},
        {"rule": "Compute total mass M", "op": f"M = V \\times \\rho = {_fmt_sa(vol)} \\times {_fmt_sa(density)}", "to": f"M = {_fmt_sa(mass)}\\text{{ tonnes}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Mass = Volume * Density, where Volume = Cross-sectional Area * Length.",
        t2=f"A = {_fmt_sa(area)} m^2, V = {_fmt_sa(vol)} m^3.",
        t3=f"Mass = {_fmt_sa(vol)} * {_fmt_sa(density)} = {_fmt_sa(mass)} tonnes.",
        misconceptions=["divided_by_density_instead_of_multiplying", "multiplied_area_directly_by_density", "arithmetic_error"],
        marks=4,
        diagram_spec=diag,
    )


def _build_08(rng: random.Random) -> Dict[str, Any]:
    sub = "08_trapezoidal_rule_from_plotted_grid_ordinates"
    h = rng.choice([2, 3, 4])
    y_vals = [rng.choice([2, 3]), rng.choice([5, 6]), rng.choice([7, 8]), rng.choice([4, 5]), rng.choice([1, 2])]
    ends = (y_vals[0] + y_vals[-1]) / 2.0
    mids = sum(y_vals[1:-1])
    area = round(h * (ends + mids), 2)

    ans = f"$\\text{{Area}} = {_fmt_sa(area)}\\text{{ m}}^2$"
    d1 = f"$\\text{{Area}} = {_fmt_sa(round(h * sum(y_vals), 2))}\\text{{ m}}^2$"
    d2 = f"$\\text{{Area}} = {_fmt_sa(round(area / 2, 2))}\\text{{ m}}^2$"
    d3 = f"$\\text{{Area}} = {_fmt_sa(round(area + 4, 2))}\\text{{ m}}^2$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_trapezoid_rule(h, [float(y) for y in y_vals])
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Plotted grid ordinates"}

    prompt = (
        f"In the accompanying diagram, an irregular shape has ordinates plotted at equal interval widths of $h = {h}\\text{{ m}}$: "
        f"$y_1 = {y_vals[0]},\\; y_2 = {y_vals[1]},\\; y_3 = {y_vals[2]},\\; y_4 = {y_vals[3]},\\; y_5 = {y_vals[4]}\\text{{ m}}$. "
        f"Calculate the approximate area using the **Trapezoidal Rule**."
    )
    steps = [
        {"rule": "Average first and last ordinates", "op": f"\\frac{{{y_vals[0]} + {y_vals[-1]}}}{{2}}", "to": f"{_fmt_sa(ends)}"},
        {"rule": "Sum middle ordinates", "op": f"{y_vals[1]} + {y_vals[2]} + {y_vals[3]}", "to": f"{_fmt_sa(mids)}"},
        {"rule": "Multiply by h", "op": f"{h} \\times ({_fmt_sa(ends)} + {_fmt_sa(mids)})", "to": f"{_fmt_sa(area)}\\text{{ m}}^2"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Apply Area = h * [(first + last)/2 + sum of middle].",
        t2=f"Ends = ({y_vals[0]} + {y_vals[-1]})/2 = {_fmt_sa(ends)}. Middle = {_fmt_sa(mids)}.",
        t3=f"Area = {h} * ({_fmt_sa(ends)} + {_fmt_sa(mids)}) = {_fmt_sa(area)} m^2.",
        misconceptions=["omitted_half_factor", "misread_ordinates_from_diagram", "arithmetic_error"],
        marks=3,
        diagram_spec=diag,
    )


def _build_09(rng: random.Random) -> Dict[str, Any]:
    sub = "09_right_prism_volume_and_surface_area_triangular"
    # Right-angled triangular base
    b = rng.choice([3, 6, 8, 5])
    hb = rng.choice([4, 8, 6, 12])
    hyp = math.isqrt(b**2 + hb**2)
    H = rng.choice([10, 15, 20, 25])

    base_area = 0.5 * b * hb
    vol = round(base_area * H, 2)
    perim = b + hb + hyp
    tsa = round(2 * base_area + perim * H, 2)

    ans = f"$V = {_fmt_sa(vol)}\\text{{ cm}}^3,\\; TSA = {_fmt_sa(tsa)}\\text{{ cm}}^2$"
    d1 = f"$V = {_fmt_sa(round(vol * 2, 2))}\\text{{ cm}}^3,\\; TSA = {_fmt_sa(tsa)}\\text{{ cm}}^2$"
    d2 = f"$V = {_fmt_sa(vol)}\\text{{ cm}}^3,\\; TSA = {_fmt_sa(round(perim * H, 2))}\\text{{ cm}}^2$"
    d3 = f"$V = {_fmt_sa(round(vol / 3, 2))}\\text{{ cm}}^3,\\; TSA = {_fmt_sa(tsa)}\\text{{ cm}}^2$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("prism", b, hb, H)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_triangular_prism_textbook.jpg",
        "model_glb": "/models/blender_3d_triangular_prism.glb",
        "alt_text": "Right triangular prism technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a right triangular prism has a right-angled triangular base with perpendicular sides "
        f"$b = {b}\\text{{ cm}}$ and $h_b = {hb}\\text{{ cm}}$ (hypotenuse $= {hyp}\\text{{ cm}}$). "
        f"The prism has a length of $H = {H}\\text{{ cm}}$. "
        f"Calculate both the **volume** ($V$) and the **total surface area** ($TSA$)."
    )
    steps = [
        {"rule": "Calculate base triangle area", "op": f"A_{{base}} = \\frac{{1}}{{2}} \\times {b} \\times {hb}", "to": f"{_fmt_sa(base_area)}\\text{{ cm}}^2"},
        {"rule": "Calculate prism volume", "op": f"V = A_{{base}} \\times H = {_fmt_sa(base_area)} \\times {H}", "to": f"{_fmt_sa(vol)}\\text{{ cm}}^3"},
        {"rule": "Calculate total surface area", "op": f"TSA = 2(A_{{base}}) + ({b} + {hb} + {hyp})({H})", "to": f"{_fmt_sa(tsa)}\\text{{ cm}}^2"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Volume = Base Area * Height. Total Surface Area = 2 * (Base Area) + (Perimeter * Height).",
        t2=f"Base area = 1/2 * {b} * {hb} = {_fmt_sa(base_area)} cm^2. Perimeter = {perim} cm.",
        t3=f"V = {_fmt_sa(vol)} cm^3, TSA = 2({_fmt_sa(base_area)}) + {perim}({H}) = {_fmt_sa(tsa)} cm^2.",
        misconceptions=["forgot_two_triangular_ends", "omitted_hypotenuse_in_perimeter", "divided_volume_by_three"],
        marks=4,
        diagram_spec=diag,
    )


def _build_10(rng: random.Random) -> Dict[str, Any]:
    sub = "10_right_prism_trapezoidal_cross_section"
    a = rng.choice([4, 6, 8])
    b = a + rng.choice([4, 6, 8])
    h = rng.choice([3, 4, 5])
    L = rng.choice([20, 30, 40, 50])

    area_trap = round(0.5 * (a + b) * h, 2)
    vol = round(area_trap * L, 2)

    ans = f"$V = {_fmt_sa(vol)}\\text{{ m}}^3$"
    d1 = f"$V = {_fmt_sa(round(area_trap + L, 2))}\\text{{ m}}^3$"
    d2 = f"$V = {_fmt_sa(round((a + b) * h * L, 2))}\\text{{ m}}^3$"
    d3 = f"$V = {_fmt_sa(round(vol / 2, 2))}\\text{{ m}}^3$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("prism", a, b, h)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_hexagonal_prism_textbook.jpg",
        "model_glb": "/models/blender_3d_hexagonal_prism.glb",
        "alt_text": "Prism channel technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a concrete drainage channel has a uniform trapezoidal cross-section with parallel sides "
        f"$a = {a}\\text{{ m}}$ and $b = {b}\\text{{ m}}$, and depth $h = {h}\\text{{ m}}$. "
        f"If the channel is $L = {L}\\text{{ m}}$ long, calculate the total volume of water it can hold when full."
    )
    steps = [
        {"rule": "Calculate trapezoidal cross-sectional area", "op": f"A = \\frac{{{a} + {b}}}{{2}} \\times {h}", "to": f"A = {_fmt_sa(area_trap)}\\text{{ m}}^2"},
        {"rule": "Calculate channel volume", "op": f"V = A \\times L = {_fmt_sa(area_trap)} \\times {L}", "to": f"V = {_fmt_sa(vol)}\\text{{ m}}^3"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Volume = Cross-sectional Area * Length. Area of a trapezium is (a + b)/2 * h.",
        t2=f"Cross-sectional area = ({a} + {b})/2 * {h} = {_fmt_sa(area_trap)} m^2.",
        t3=f"Volume = {_fmt_sa(area_trap)} * {L} = {_fmt_sa(vol)} m^3.",
        misconceptions=["omitted_half_in_trapezium_area", "multiplied_a_and_b", "unit_confusion"],
        marks=3,
        diagram_spec=diag,
    )


def _build_11(rng: random.Random) -> Dict[str, Any]:
    sub = "11_cylinder_volume_and_total_surface_area"
    r = rng.choice([3, 4, 5, 7, 10])
    h = rng.choice([6, 8, 10, 12, 14])

    vol = round(math.pi * (r**2) * h, 2)
    tsa = round(2 * math.pi * r * (r + h), 2)

    ans = f"$V = {_fmt_sa(vol)}\\text{{ cm}}^3,\\; TSA = {_fmt_sa(tsa)}\\text{{ cm}}^2$"
    d1 = f"$V = {_fmt_sa(round(math.pi * r * h, 2))}\\text{{ cm}}^3,\\; TSA = {_fmt_sa(tsa)}\\text{{ cm}}^2$"
    d2 = f"$V = {_fmt_sa(vol)}\\text{{ cm}}^3,\\; TSA = {_fmt_sa(round(2 * math.pi * r * h, 2))}\\text{{ cm}}^2$"
    d3 = f"$V = {_fmt_sa(round(vol / 3, 2))}\\text{{ cm}}^3,\\; TSA = {_fmt_sa(tsa)}\\text{{ cm}}^2$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("cylinder", r, h)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_cylinder_textbook.jpg",
        "model_glb": "/models/blender_3d_cylinder.glb",
        "alt_text": "Solid cylinder technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a solid metal cylinder has radius $r = {r}\\text{{ cm}}$ and height $h = {h}\\text{{ cm}}$. "
        f"Calculate both the **volume** ($V$) and the **total surface area** ($TSA$) to two decimal places."
    )
    steps = [
        {"rule": "Calculate cylinder volume", "op": f"V = \\pi r^2 h = \\pi ({r})^2 ({h})", "to": f"{_fmt_sa(vol)}\\text{{ cm}}^3"},
        {"rule": "Calculate total surface area", "op": f"TSA = 2\\pi r(r + h) = 2\\pi ({r})({r} + {h})", "to": f"{_fmt_sa(tsa)}\\text{{ cm}}^2"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="For a cylinder: V = pi * r^2 * h and TSA = 2 * pi * r * h + 2 * pi * r^2.",
        t2=f"V = pi * {r}^2 * {h} = {_fmt_sa(vol)} cm^3.",
        t3=f"TSA = 2 * pi * {r} * ({r} + {h}) = {_fmt_sa(tsa)} cm^2.",
        misconceptions=["forgot_two_circular_bases_in_TSA", "used_diameter_instead_of_radius", "formula_swap_with_cone"],
        marks=4,
        diagram_spec=diag,
    )


def _build_12(rng: random.Random) -> Dict[str, Any]:
    sub = "12_hollow_cylinder_pipe_material_volume"
    R = rng.choice([6, 8, 10, 12])
    thickness = rng.choice([1, 2])
    r = R - thickness
    L = rng.choice([50, 100, 150, 200])

    area_cross = math.pi * (R**2 - r**2)
    vol_mat = round(area_cross * L, 2)

    ans = f"$V_{{material}} = {_fmt_sa(vol_mat)}\\text{{ cm}}^3$"
    d1 = f"$V_{{material}} = {_fmt_sa(round(math.pi * (R**2) * L, 2))}\\text{{ cm}}^3$"
    d2 = f"$V_{{material}} = {_fmt_sa(round(math.pi * ((R - r)**2) * L, 2))}\\text{{ cm}}^3$"
    d3 = f"$V_{{material}} = {_fmt_sa(round(vol_mat / 2, 2))}\\text{{ cm}}^3$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("cylinder", R, L)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_cylinder_textbook.jpg",
        "model_glb": "/models/blender_3d_cylinder.glb",
        "alt_text": "Hollow cylinder pipe technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a hollow cylindrical steel pipe has an outer radius of $R = {R}\\text{{ cm}}$ and an inner radius of $r = {r}\\text{{ cm}}$. "
        f"The pipe has a length of $L = {L}\\text{{ cm}}$. "
        f"Calculate the volume of steel needed to manufacture the pipe (to two decimal places)."
    )
    steps = [
        {"rule": "Calculate cross-sectional annular area", "op": f"A = \\pi(R^2 - r^2) = \\pi(({R})^2 - ({r})^2)", "to": f"{_fmt_sa(round(area_cross, 2))}\\text{{ cm}}^2"},
        {"rule": "Calculate volume of steel", "op": f"V = \\pi(R^2 - r^2)L = \\pi({R**2 - r**2})({L})", "to": f"{_fmt_sa(vol_mat)}\\text{{ cm}}^3"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Volume of material in a hollow pipe = pi * (R^2 - r^2) * L.",
        t2=f"R^2 - r^2 = {R}^2 - {r}^2 = {R**2 - r**2}.",
        t3=f"V = pi * {R**2 - r**2} * {L} = {_fmt_sa(vol_mat)} cm^3.",
        misconceptions=["used_pi_times_R_minus_r_squared", "forgot_to_subtract_inner_volume", "swapped_inner_outer"],
        marks=3,
        diagram_spec=diag,
    )


def _build_13(rng: random.Random) -> Dict[str, Any]:
    sub = "13_right_pyramid_square_base_volume_and_slant_height"
    b = rng.choice([6, 8, 10, 12])
    h = rng.choice([4, 6, 8, 10])
    half_b = b / 2.0
    slant_s = round(math.sqrt(h**2 + half_b**2), 2)
    vol = round((1.0 / 3.0) * (b**2) * h, 2)
    tsa = round(b**2 + 2 * b * slant_s, 2)

    ans = f"$V = {_fmt_sa(vol)}\\text{{ cm}}^3,\\; s = {_fmt_sa(slant_s)}\\text{{ cm}}$"
    d1 = f"$V = {_fmt_sa(round((b**2) * h, 2))}\\text{{ cm}}^3,\\; s = {_fmt_sa(slant_s)}\\text{{ cm}}$"
    d2 = f"$V = {_fmt_sa(vol)}\\text{{ cm}}^3,\\; s = {_fmt_sa(round(math.sqrt(h**2 + b**2), 2))}\\text{{ cm}}$"
    d3 = f"$V = {_fmt_sa(round(vol / 2, 2))}\\text{{ cm}}^3,\\; s = {_fmt_sa(slant_s)}\\text{{ cm}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("prism", b, b, h)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_square_pyramid_textbook.jpg",
        "model_glb": "/models/blender_3d_square_pyramid.glb",
        "alt_text": "Right square pyramid technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a right pyramid has a square base with sides $b = {b}\\text{{ cm}}$ and a perpendicular height of $h = {h}\\text{{ cm}}$. "
        f"Calculate the **slant height** ($s$) of a triangular face and the **volume** ($V$) of the pyramid."
    )
    steps = [
        {"rule": "Apply Pythagoras to find slant height s", "op": f"s = \\sqrt{{h^2 + (b/2)^2}} = \\sqrt{{{h}^2 + ({_fmt_sa(half_b)})^2}}", "to": f"s = {_fmt_sa(slant_s)}\\text{{ cm}}"},
        {"rule": "Calculate pyramid volume", "op": f"V = \\frac{{1}}{{3}} b^2 h = \\frac{{1}}{{3}} ({b})^2 ({h})", "to": f"V = {_fmt_sa(vol)}\\text{{ cm}}^3"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Slant height s = sqrt(h^2 + (b/2)^2). Volume = 1/3 * base_area * height.",
        t2=f"s = sqrt({h}^2 + {_fmt_sa(half_b)}^2) = {_fmt_sa(slant_s)} cm.",
        t3=f"V = 1/3 * {b}^2 * {h} = {_fmt_sa(vol)} cm^3.",
        misconceptions=["used_full_b_in_slant_pythagoras", "forgot_one_third_factor_in_volume", "swapped_h_and_s"],
        marks=4,
        diagram_spec=diag,
    )


def _build_14(rng: random.Random) -> Dict[str, Any]:
    sub = "14_right_cone_slant_height_curved_surface_area"
    # Pythagorean triples for r, h, s
    triple = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)])
    r, h, s = triple
    csa = round(math.pi * r * s, 2)
    tsa = round(math.pi * r * (r + s), 2)

    ans = f"$s = {s}\\text{{ cm}},\\; CSA = {_fmt_sa(csa)}\\text{{ cm}}^2$"
    d1 = f"$s = {h + r}\\text{{ cm}},\\; CSA = {_fmt_sa(csa)}\\text{{ cm}}^2$"
    d2 = f"$s = {s}\\text{{ cm}},\\; CSA = {_fmt_sa(tsa)}\\text{{ cm}}^2$"
    d3 = f"$s = {s}\\text{{ cm}},\\; CSA = {_fmt_sa(round(math.pi * (r**2) * h, 2))}\\text{{ cm}}^2$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("cone", r, h)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_cone_textbook.jpg",
        "model_glb": "/models/blender_3d_cone.glb",
        "alt_text": "Right circular cone technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a right circular cone has a base radius of $r = {r}\\text{{ cm}}$ and a perpendicular height of $h = {h}\\text{{ cm}}$. "
        f"Calculate the **slant height** ($s$) and the **curved surface area** ($CSA$) to two decimal places."
    )
    steps = [
        {"rule": "Calculate slant height s using Pythagoras", "op": f"s = \\sqrt{{r^2 + h^2}} = \\sqrt{{{r}^2 + {h}^2}}", "to": f"s = {s}\\text{{ cm}}"},
        {"rule": "Calculate curved surface area", "op": f"CSA = \\pi r s = \\pi ({r})({s})", "to": f"{_fmt_sa(csa)}\\text{{ cm}}^2"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Slant height s = sqrt(r^2 + h^2). Curved surface area CSA = pi * r * s.",
        t2=f"s = sqrt({r}^2 + {h}^2) = {s} cm.",
        t3=f"CSA = pi * {r} * {s} = {_fmt_sa(csa)} cm^2.",
        misconceptions=["used_h_instead_of_s_in_CSA", "included_circular_base_in_curved_area", "arithmetic_error"],
        marks=3,
        diagram_spec=diag,
    )


def _build_15(rng: random.Random) -> Dict[str, Any]:
    sub = "15_right_cone_volume_calculation"
    r = rng.choice([3, 4, 6, 7, 9])
    h = rng.choice([5, 8, 10, 12, 15])
    vol = round((1.0 / 3.0) * math.pi * (r**2) * h, 2)

    ans = f"$V = {_fmt_sa(vol)}\\text{{ cm}}^3$"
    d1 = f"$V = {_fmt_sa(round(math.pi * (r**2) * h, 2))}\\text{{ cm}}^3$"
    d2 = f"$V = {_fmt_sa(round(vol * 2, 2))}\\text{{ cm}}^3$"
    d3 = f"$V = {_fmt_sa(round((4.0/3.0) * math.pi * (r**3), 2))}\\text{{ cm}}^3$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("cone", r, h)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_cone_textbook.jpg",
        "model_glb": "/models/blender_3d_cone.glb",
        "alt_text": "Right cone hopper technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, an industrial hopper in the shape of an inverted right cone has a radius of $r = {r}\\text{{ cm}}$ and a height of $h = {h}\\text{{ cm}}$. "
        f"Calculate the **volume** ($V$) of the cone to two decimal places."
    )
    steps = [
        {"rule": "Apply cone volume formula", "op": f"V = \\frac{{1}}{{3}} \\pi r^2 h = \\frac{{1}}{{3}} \\pi ({r})^2 ({h})", "to": f"V = {_fmt_sa(vol)}\\text{{ cm}}^3"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Volume of a right cone = 1/3 * pi * r^2 * h.",
        t2=f"V = 1/3 * pi * ({r})^2 * {h}.",
        t3=f"V = {_fmt_sa(vol)} cm^3.",
        misconceptions=["omitted_one_third_factor", "squared_height_instead_of_radius", "used_sphere_formula"],
        marks=2,
        diagram_spec=diag,
    )


def _build_16(rng: random.Random) -> Dict[str, Any]:
    sub = "16_sphere_surface_area_and_volume"
    r = rng.choice([3, 4, 5, 6, 7, 9])
    sa = round(4 * math.pi * (r**2), 2)
    vol = round((4.0 / 3.0) * math.pi * (r**3), 2)

    ans = f"$SA = {_fmt_sa(sa)}\\text{{ cm}}^2,\\; V = {_fmt_sa(vol)}\\text{{ cm}}^3$"
    d1 = f"$SA = {_fmt_sa(round(2 * math.pi * (r**2), 2))}\\text{{ cm}}^2,\\; V = {_fmt_sa(vol)}\\text{{ cm}}^3$"
    d2 = f"$SA = {_fmt_sa(sa)}\\text{{ cm}}^2,\\; V = {_fmt_sa(round(math.pi * (r**3), 2))}\\text{{ cm}}^3$"
    d3 = f"$SA = {_fmt_sa(round(4 * math.pi * r, 2))}\\text{{ cm}}^2,\\; V = {_fmt_sa(vol)}\\text{{ cm}}^3$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("sphere", r, 0)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_sphere_textbook.jpg",
        "model_glb": "/models/blender_3d_sphere.glb",
        "alt_text": "Solid sphere technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a solid spherical bearing has a radius of $r = {r}\\text{{ cm}}$. "
        f"Calculate its **surface area** ($SA$) and **volume** ($V$) to two decimal places."
    )
    steps = [
        {"rule": "Calculate sphere surface area", "op": f"SA = 4\\pi r^2 = 4\\pi ({r})^2", "to": f"{_fmt_sa(sa)}\\text{{ cm}}^2"},
        {"rule": "Calculate sphere volume", "op": f"V = \\frac{{4}}{{3}} \\pi r^3 = \\frac{{4}}{{3}} \\pi ({r})^3", "to": f"{_fmt_sa(vol)}\\text{{ cm}}^3"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="For a sphere: Surface Area = 4 * pi * r^2 and Volume = (4/3) * pi * r^3.",
        t2=f"SA = 4 * pi * {r}^2 = {_fmt_sa(sa)} cm^2.",
        t3=f"V = (4/3) * pi * {r}^3 = {_fmt_sa(vol)} cm^3.",
        misconceptions=["used_r_squared_in_volume", "omitted_factor_of_4_in_surface_area", "used_diameter_instead_of_radius"],
        marks=4,
        diagram_spec=diag,
    )


def _build_17(rng: random.Random) -> Dict[str, Any]:
    sub = "17_hemisphere_open_and_closed_surface_area"
    r = rng.choice([3, 4, 5, 6, 8])
    # Closed hemisphere: curved (2 pi r^2) + circular base (pi r^2) = 3 pi r^2
    tsa_closed = round(3 * math.pi * (r**2), 2)
    vol = round((2.0 / 3.0) * math.pi * (r**3), 2)

    ans = f"$TSA_{{closed}} = {_fmt_sa(tsa_closed)}\\text{{ cm}}^2,\\; V = {_fmt_sa(vol)}\\text{{ cm}}^3$"
    d1 = f"$TSA_{{closed}} = {_fmt_sa(round(2 * math.pi * (r**2), 2))}\\text{{ cm}}^2,\\; V = {_fmt_sa(vol)}\\text{{ cm}}^3$"
    d2 = f"$TSA_{{closed}} = {_fmt_sa(round(4 * math.pi * (r**2), 2))}\\text{{ cm}}^2,\\; V = {_fmt_sa(vol)}\\text{{ cm}}^3$"
    d3 = f"$TSA_{{closed}} = {_fmt_sa(tsa_closed)}\\text{{ cm}}^2,\\; V = {_fmt_sa(round(vol * 2, 2))}\\text{{ cm}}^3$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("sphere", r, 0)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_sphere_textbook.jpg",
        "model_glb": "/models/blender_3d_sphere.glb",
        "alt_text": "Solid hemisphere technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a solid closed hemisphere has a radius of $r = {r}\\text{{ cm}}$. "
        f"Calculate both its **total surface area** ($TSA_{{closed}}$) including the flat circular base, "
        f"and its **volume** ($V$) to two decimal places."
    )
    steps = [
        {"rule": "Calculate closed hemisphere total surface area", "op": f"TSA = 2\\pi r^2 + \\pi r^2 = 3\\pi r^2 = 3\\pi ({r})^2", "to": f"{_fmt_sa(tsa_closed)}\\text{{ cm}}^2"},
        {"rule": "Calculate hemisphere volume", "op": f"V = \\frac{{2}}{{3}} \\pi r^3 = \\frac{{2}}{{3}} \\pi ({r})^3", "to": f"{_fmt_sa(vol)}\\text{{ cm}}^3"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A closed hemisphere has curved surface area 2*pi*r^2 plus flat base area pi*r^2 = 3*pi*r^2.",
        t2=f"TSA = 3 * pi * {r}^2 = {_fmt_sa(tsa_closed)} cm^2.",
        t3=f"V = (2/3) * pi * {r}^3 = {_fmt_sa(vol)} cm^3.",
        misconceptions=["omitted_flat_circular_base_in_closed_hemisphere", "used_4_thirds_volume", "squared_radius_in_volume"],
        marks=4,
        diagram_spec=diag,
    )


def _build_18(rng: random.Random) -> Dict[str, Any]:
    sub = "18_composite_solid_cylinder_with_conical_roof"
    r = rng.choice([3, 4, 6])
    h_cyl = rng.choice([8, 10, 12])
    h_cone = rng.choice([4, 6, 8])

    s_cone = round(math.sqrt(r**2 + h_cone**2), 2)
    v_cyl = math.pi * (r**2) * h_cyl
    v_cone = (1.0 / 3.0) * math.pi * (r**2) * h_cone
    total_vol = round(v_cyl + v_cone, 2)

    # External surface area: flat floor (pi r^2) + curved cylinder (2 pi r h_cyl) + curved cone roof (pi r s)
    sa_ext = round(math.pi * (r**2) + 2 * math.pi * r * h_cyl + math.pi * r * s_cone, 2)

    ans = f"$V_{{total}} = {_fmt_sa(total_vol)}\\text{{ m}}^3,\\; A_{{ext}} = {_fmt_sa(sa_ext)}\\text{{ m}}^2$"
    d1 = f"$V_{{total}} = {_fmt_sa(round(v_cyl, 2))}\\text{{ m}}^3,\\; A_{{ext}} = {_fmt_sa(sa_ext)}\\text{{ m}}^2$"
    d2 = f"$V_{{total}} = {_fmt_sa(total_vol)}\\text{{ m}}^3,\\; A_{{ext}} = {_fmt_sa(round(sa_ext + math.pi * (r**2), 2))}\\text{{ m}}^2$"
    d3 = f"$V_{{total}} = {_fmt_sa(round(total_vol * 1.2, 2))}\\text{{ m}}^3,\\; A_{{ext}} = {_fmt_sa(sa_ext)}\\text{{ m}}^2$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("cylinder", r, h_cyl)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_cylinder_textbook.jpg",
        "model_glb": "/models/blender_3d_cylinder.glb",
        "alt_text": "Composite grain silo technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a grain silo comprises a vertical cylindrical body of radius $r = {r}\\text{{ m}}$ and height $h_{{cyl}} = {h_cyl}\\text{{ m}}$, "
        f"topped with a right conical roof of height $h_{{cone}} = {h_cone}\\text{{ m}}$. "
        f"Calculate the **total storage capacity (volume)** and the **total external surface area** (including the flat ground base)."
    )
    steps = [
        {"rule": "Calculate cylinder and cone volumes", "op": f"V_{{cyl}} = \\pi ({r})^2 ({h_cyl}),\\; V_{{cone}} = \\frac{{1}}{{3}}\\pi ({r})^2 ({h_cone})", "to": f"V_{{total}} = {_fmt_sa(total_vol)}\\text{{ m}}^3"},
        {"rule": "Calculate cone roof slant height", "op": f"s = \\sqrt{{{r}^2 + {h_cone}^2}}", "to": f"s = {_fmt_sa(s_cone)}\\text{{ m}}"},
        {"rule": "Calculate external surface area", "op": f"A = \\pi r^2 + 2\\pi r h_{{cyl}} + \\pi r s", "to": f"A = {_fmt_sa(sa_ext)}\\text{{ m}}^2"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Total volume = V_cylinder + V_cone. External surface area = base + curved cylinder + curved cone.",
        t2=f"V = pi * {r}^2 * {h_cyl} + (1/3) * pi * {r}^2 * {h_cone} = {_fmt_sa(total_vol)} m^3.",
        t3=f"Slant height s = {_fmt_sa(s_cone)} m, Total external area = {_fmt_sa(sa_ext)} m^2.",
        misconceptions=["included_internal_joint_circle_in_surface_area", "omitted_cone_roof_volume", "used_h_instead_of_slant_s"],
        marks=4,
        diagram_spec=diag,
    )


def _build_19(rng: random.Random) -> Dict[str, Any]:
    sub = "19_composite_solid_cylinder_with_hemispherical_ends"
    r = rng.choice([2, 3, 4, 5])
    h = rng.choice([10, 12, 15, 20])

    # Cylinder + 2 hemispheres = cylinder + 1 sphere
    vol = round(math.pi * (r**2) * h + (4.0 / 3.0) * math.pi * (r**3), 2)
    # Total external surface area: curved cylinder + sphere surface
    sa = round(2 * math.pi * r * h + 4 * math.pi * (r**2), 2)

    ans = f"$V = {_fmt_sa(vol)}\\text{{ m}}^3,\\; SA = {_fmt_sa(sa)}\\text{{ m}}^2$"
    d1 = f"$V = {_fmt_sa(round(math.pi * (r**2) * h, 2))}\\text{{ m}}^3,\\; SA = {_fmt_sa(sa)}\\text{{ m}}^2$"
    d2 = f"$V = {_fmt_sa(vol)}\\text{{ m}}^3,\\; SA = {_fmt_sa(round(2 * math.pi * r * h, 2))}\\text{{ m}}^2$"
    d3 = f"$V = {_fmt_sa(round(vol * 1.25, 2))}\\text{{ m}}^3,\\; SA = {_fmt_sa(sa)}\\text{{ m}}^2$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("cylinder", r, h)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_cylinder_textbook.jpg",
        "model_glb": "/models/blender_3d_cylinder.glb",
        "alt_text": "Cylindrical storage tank composite technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a liquid petroleum gas (LPG) storage tank consists of a cylindrical central section of radius $r = {r}\\text{{ m}}$ and length $h = {h}\\text{{ m}}$, "
        f"capped at both ends with hemispherical caps of the same radius $r = {r}\\text{{ m}}$. "
        f"Calculate the **total volume** ($V$) and the **total exterior surface area** ($SA$) to two decimal places."
    )
    steps = [
        {"rule": "Combine volume (cylinder + 1 full sphere)", "op": f"V = \\pi r^2 h + \\frac{{4}}{{3}}\\pi r^3 = \\pi ({r})^2 ({h}) + \\frac{{4}}{{3}}\\pi ({r})^3", "to": f"{_fmt_sa(vol)}\\text{{ m}}^3"},
        {"rule": "Combine exterior surface area (curved cylinder + 1 full sphere)", "op": f"SA = 2\\pi r h + 4\\pi r^2 = 2\\pi ({r})({h}) + 4\\pi ({r})^2", "to": f"{_fmt_sa(sa)}\\text{{ m}}^2"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Two hemispherical ends combine to form exactly one full sphere of radius r.",
        t2=f"V = pi * {r}^2 * {h} + (4/3) * pi * {r}^3 = {_fmt_sa(vol)} m^3.",
        t3=f"SA = 2 * pi * {r} * {h} + 4 * pi * {r}^2 = {_fmt_sa(sa)} m^2.",
        misconceptions=["added_circular_flat_faces_inside_tank", "only_added_one_hemisphere", "radius_cubed_error"],
        marks=4,
        diagram_spec=diag,
    )


def _build_20(rng: random.Random) -> Dict[str, Any]:
    sub = "20_composite_solid_prism_with_cylindrical_borehole"
    L = rng.choice([12, 14, 16])
    W = rng.choice([8, 10, 12])
    H = rng.choice([6, 8, 10])
    r = rng.choice([2, 3])

    vol_prism = L * W * H
    vol_hole = math.pi * (r**2) * H
    vol_rem = round(vol_prism - vol_hole, 2)

    ans = f"$V_{{remaining}} = {_fmt_sa(vol_rem)}\\text{{ cm}}^3$"
    d1 = f"$V_{{remaining}} = {_fmt_sa(vol_prism)}\\text{{ cm}}^3$"
    d2 = f"$V_{{remaining}} = {_fmt_sa(round(vol_rem * 0.8, 2))}\\text{{ cm}}^3$"
    d3 = f"$V_{{remaining}} = {_fmt_sa(round(vol_prism + vol_hole, 2))}\\text{{ cm}}^3$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("prism", L, W, H)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_rectangular_prism_textbook.jpg",
        "model_glb": "/models/blender_3d_rectangular_prism.glb",
        "alt_text": "Rectangular block with borehole technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a solid rectangular metal block has dimensions $L = {L}\\text{{ cm}}$, $W = {W}\\text{{ cm}}$, and $H = {H}\\text{{ cm}}$. "
        f"A cylindrical hole of radius $r = {r}\\text{{ cm}}$ is bored completely through the block parallel to its height $H$. "
        f"Calculate the **remaining volume** of the metal block to two decimal places."
    )
    steps = [
        {"rule": "Calculate volume of solid rectangular block", "op": f"V_{{block}} = L \\times W \\times H = {L} \\times {W} \\times {H}", "to": f"{vol_prism}\\text{{ cm}}^3"},
        {"rule": "Calculate volume of cylindrical borehole", "op": f"V_{{hole}} = \\pi r^2 H = \\pi ({r})^2 ({H})", "to": f"{_fmt_sa(round(vol_hole, 2))}\\text{{ cm}}^3"},
        {"rule": "Subtract borehole from block volume", "op": f"V_{{rem}} = V_{{block}} - V_{{hole}}", "to": f"{_fmt_sa(vol_rem)}\\text{{ cm}}^3"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Remaining volume = Volume of rectangular block - Volume of cylindrical hole.",
        t2=f"V_block = {L} * {W} * {H} = {vol_prism}. V_hole = pi * {r}^2 * {H} = {_fmt_sa(round(vol_hole, 2))}.",
        t3=f"V_rem = {vol_prism} - {_fmt_sa(round(vol_hole, 2))} = {_fmt_sa(vol_rem)} cm^3.",
        misconceptions=["added_borehole_instead_of_subtracting", "forgot_to_multiply_by_height_H", "arithmetic_error"],
        marks=3,
        diagram_spec=diag,
    )


def _build_21(rng: random.Random) -> Dict[str, Any]:
    sub = "21_scaling_factor_effect_on_surface_area_and_volume"
    k = rng.choice([2, 3, 4, 5])
    orig_area = rng.choice([25, 40, 50, 80])
    orig_vol = rng.choice([60, 100, 120, 200])

    new_area = orig_area * (k**2)
    new_vol = orig_vol * (k**3)

    ans = f"$\\text{{New Area}} = {new_area}\\text{{ cm}}^2,\\; \\text{{New Volume}} = {new_vol}\\text{{ cm}}^3$"
    d1 = f"$\\text{{New Area}} = {orig_area * k}\\text{{ cm}}^2,\\; \\text{{New Volume}} = {orig_vol * k}\\text{{ cm}}^3$"
    d2 = f"$\\text{{New Area}} = {orig_area * (k**3)}\\text{{ cm}}^2,\\; \\text{{New Volume}} = {orig_vol * (k**2)}\\text{{ cm}}^3$"
    d3 = f"$\\text{{New Area}} = {new_area}\\text{{ cm}}^2,\\; \\text{{New Volume}} = {orig_vol * (k**2)}\\text{{ cm}}^3$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_solid_isometric("prism", k, k, k)
    diag = {
        "diagram_role": "context",
        "kind": "blender_3d",
        "plate": "/diagrams/blender_3d_cube_textbook.jpg",
        "model_glb": "/models/blender_3d_cube.glb",
        "alt_text": "Cubic prototype casing technical 3D model",
        "svg": svg,
    }

    prompt = (
        f"In the accompanying diagram, a prototype machine casing in the shape of a cube has an initial surface area of ${orig_area}\\text{{ cm}}^2$ and a volume of ${orig_vol}\\text{{ cm}}^3$. "
        f"If all linear dimensions of the casing are scaled up by a factor of $k = {k}$, "
        f"determine the new surface area and new volume of the enlarged casing."
    )
    steps = [
        {"rule": "Apply area scaling law (k^2 factor)", "op": f"\\text{{New Area}} = \\text{{Area}}_{{orig}} \\times k^2 = {orig_area} \\times {k}^2", "to": f"{new_area}\\text{{ cm}}^2"},
        {"rule": "Apply volume scaling law (k^3 factor)", "op": f"\\text{{New Volume}} = \\text{{Vol}}_{{orig}} \\times k^3 = {orig_vol} \\times {k}^3", "to": f"{new_vol}\\text{{ cm}}^3"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Linear scale factor k: Area scales by k^2 and Volume scales by k^3.",
        t2=f"New Area = {orig_area} * {k}^2 = {new_area} cm^2.",
        t3=f"New Volume = {orig_vol} * {k}^3 = {new_vol} cm^3.",
        misconceptions=["multiplied_both_by_linear_k", "swapped_k2_and_k3_exponents", "added_k_instead_of_multiplying"],
        marks=2,
        diagram_spec=diag,
    )


def _build_22(rng: random.Random) -> Dict[str, Any]:
    sub = "22_indefinite_integral_power_rule_polynomial"
    a = rng.choice([2, 3, 4, 6])
    n = rng.choice([2, 3])
    b = rng.choice([2, 4, 6, 8])
    c = rng.choice([1, 3, 5, 7])

    # Integrate a x^n + b x + c
    # int = (a / (n+1)) x^(n+1) + (b / 2) x^2 + c x + C
    b_half = b // 2

    if n == 2:
        ans = f"$\\frac{{{a}}}{{3}}x^3 + {b_half}x^2 + {c}x + C$"
        d1 = f"${a}x^3 + {b}x^2 + {c}x + C$"
        d2 = f"${2*a}x + {b} + C$"
        d3 = f"$\\frac{{{a}}}{{3}}x^3 + {b}x^2 + {c} + C$"
        integrand = f"{a}x^2 + {b}x + {c}"
    else:
        ans = f"\\frac{{{a}}}{{4}}x^4 + {b_half}x^2 + {c}x + C"
        if a % 4 == 0:
            ans = f"{a//4}x^4 + {b_half}x^2 + {c}x + C"
        ans = f"${ans}$"
        d1 = f"${a}x^4 + {b}x^2 + {c}x + C$"
        d2 = f"${3*a}x^2 + {b} + C$"
        d3 = f"$\\frac{{{a}}}{{4}}x^4 + {b}x^2 + C$"
        integrand = f"{a}x^3 + {b}x + {c}"

    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    prompt = f"Evaluate the indefinite integral: $$\\int ({integrand})\\, dx$$"
    steps = [
        {"rule": "Apply power rule of integration term by term", "op": "\\int x^n dx = \\frac{x^{n+1}}{n+1} + C", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The power rule of integration states: int x^n dx = x^{n+1} / (n+1) + C.",
        t2=f"Increase the exponent of each term by 1 and divide by the new exponent.",
        t3=f"Result: {ans}.",
        misconceptions=["differentiated_instead_of_integrated", "forgot_constant_of_integration_C", "forgot_to_divide_by_new_power"],
        marks=3,
    )


def _build_23(rng: random.Random) -> Dict[str, Any]:
    sub = "23_indefinite_integral_fractional_and_negative_powers"
    # Integral of a x^(-2) + b / x
    a = rng.choice([2, 3, 4, 5])
    b = rng.choice([2, 3, 4, 6])

    # int a x^(-2) dx = -a x^(-1) = -a / x
    # int b / x dx = b ln x
    ans = f"$-\\frac{{{a}}}{{x}} + {b}\\ln|x| + C$"
    d1 = f"$\\frac{{{a}}}{{x}} + {b}\\ln|x| + C$"
    d2 = f"$-\\frac{{{a}}}{{x^3}} + {b}x + C$"
    d3 = f"$-\\frac{{{a}}}{{x}} + \\frac{{{b}}}{{x^2}} + C$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    prompt = f"Evaluate the indefinite integral: $$\\int \\left( \\frac{{{a}}}{{x^2}} + \\frac{{{b}}}{{x}} \\right) dx$$"
    steps = [
        {"rule": "Rewrite with negative exponents", "op": f"\\int ({a}x^{{-2}} + {b}x^{{-1}})\\, dx", "to": f"{a}\\frac{{x^{{-1}}}}{{-1}} + {b}\\ln|x| + C"},
        {"rule": "Simplify terms", "op": f"-{a}x^{{-1}} + {b}\\ln|x| + C", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Rewrite a / x^2 as a * x^{-2}. Note that the integral of 1/x is ln|x|.",
        t2=f"int {a}x^{{-2}} dx = {a} * (x^{{-1}} / -1) = -{a}/x.",
        t3=f"int {b}/x dx = {b}*ln|x|. Overall result: {ans}.",
        misconceptions=["applied_power_rule_to_1_over_x", "sign_error_negative_power", "forgot_ln_x"],
        marks=3,
    )


def _build_24(rng: random.Random) -> Dict[str, Any]:
    sub = "24_definite_integral_polynomial_evaluation"
    m = rng.choice([2, 4, 6])
    c = rng.choice([1, 2, 3, 4])
    a = 1
    b = rng.choice([3, 4, 5])

    # int_1^b (m x + c) dx = [ (m/2) x^2 + c x ]_1^b
    m_half = m // 2
    F_b = m_half * (b**2) + c * b
    F_a = m_half * (a**2) + c * a
    val = F_b - F_a

    ans = f"${val}$"
    d1 = f"${val + 4}$"
    d2 = f"${F_b}$"
    d3 = f"${val - 2}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    prompt = f"Evaluate the definite integral: $$\\int_{{{a}}}^{{{b}}} ({m}x + {c})\\, dx$$"
    steps = [
        {"rule": "Find antiderivative F(x)", "op": f"F(x) = {m_half}x^2 + {c}x", "to": f"\\left[ {m_half}x^2 + {c}x \\right]_{{{a}}}^{{{b}}}"},
        {"rule": "Evaluate F(b) - F(a)", "op": f"({m_half}({b})^2 + {c}({b})) - ({m_half}({a})^2 + {c}({a})) = {F_b} - {F_a}", "to": ans.replace("$", "")},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Fundamental Theorem of Calculus: int_a^b f(x) dx = F(b) - F(a).",
        t2=f"Antiderivative F(x) = {m_half}x^2 + {c}x.",
        t3=f"F({b}) - F({a}) = {F_b} - {F_a} = {val}.",
        misconceptions=["added_F_a_instead_of_subtracting", "forgot_to_evaluate_lower_bound", "arithmetic_square_error"],
        marks=3,
    )


def _build_25(rng: random.Random) -> Dict[str, Any]:
    sub = "25_definite_integral_area_under_parabola_or_line"
    # Area under y = a x^2 from x = 0 to x = b
    a = rng.choice([3, 6, 9])
    b = rng.choice([2, 3, 4])
    # int_0^b a x^2 dx = [ (a/3) x^3 ]_0^b = (a/3) * b^3
    a_third = a // 3
    area = a_third * (b**3)

    ans = f"$\\text{{Area}} = {area}\\text{{ sq units}}$"
    d1 = f"$\\text{{Area}} = {a * b**2}\\text{{ sq units}}$"
    d2 = f"$\\text{{Area}} = {area * 2}\\text{{ sq units}}$"
    d3 = f"$\\text{{Area}} = {area // 2}\\text{{ sq units}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    svg = _make_svg_area_under_curve(f"y = {a}x^2", 0, b)
    diag = {"kind": "inline_svg", "svg": svg, "alt_text": "Area under parabolic curve"}

    prompt = (
        f"In the accompanying diagram, the shaded region is bounded by the parabolic curve $y = {a}x^2$, "
        f"the $x$-axis, and the vertical lines $x = 0$ and $x = {b}$. "
        f"Calculate the exact area of the shaded region using definite integration."
    )
    steps = [
        {"rule": "Set up definite integral for area", "op": f"\\text{{Area}} = \\int_0^{{{b}}} {a}x^2\\, dx", "to": f"\\left[ \\frac{{{a}}}{{3}}x^3 \\right]_0^{{{b}}}"},
        {"rule": "Evaluate antiderivative at limits", "op": f"\\left[ {a_third}x^3 \\right]_0^{{{b}}} = {a_third}({b})^3 - 0", "to": f"\\text{{Area}} = {area}\\text{{ sq units}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The area under a curve y = f(x) above the x-axis is given by int_a^b f(x) dx.",
        t2=f"Antiderivative of {a}x^2 is ({a}/3)x^3 = {a_third}x^3.",
        t3=f"Area = {a_third}({b})^3 - 0 = {area} sq units.",
        misconceptions=["used_differentiation_instead_of_integration", "forgot_to_cube_limit", "divided_by_two_instead_of_three"],
        marks=3,
        diagram_spec=diag,
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_interval_width_and_ordinate_count": _build_01,
    "02_mid_ordinate_rule_calculation": _build_02,
    "03_trapezoidal_rule_four_intervals": _build_03,
    "04_trapezoidal_rule_five_intervals": _build_04,
    "05_trapezoidal_rule_six_intervals": _build_05,
    "06_irregular_excavation_volume_from_cross_section": _build_06,
    "07_civil_engineering_earthwork_mass_calculation": _build_07,
    "08_trapezoidal_rule_from_plotted_grid_ordinates": _build_08,
    "09_right_prism_volume_and_surface_area_triangular": _build_09,
    "10_right_prism_trapezoidal_cross_section": _build_10,
    "11_cylinder_volume_and_total_surface_area": _build_11,
    "12_hollow_cylinder_pipe_material_volume": _build_12,
    "13_right_pyramid_square_base_volume_and_slant_height": _build_13,
    "14_right_cone_slant_height_curved_surface_area": _build_14,
    "15_right_cone_volume_calculation": _build_15,
    "16_sphere_surface_area_and_volume": _build_16,
    "17_hemisphere_open_and_closed_surface_area": _build_17,
    "18_composite_solid_cylinder_with_conical_roof": _build_18,
    "19_composite_solid_cylinder_with_hemispherical_ends": _build_19,
    "20_composite_solid_prism_with_cylindrical_borehole": _build_20,
    "21_scaling_factor_effect_on_surface_area_and_volume": _build_21,
    "22_indefinite_integral_power_rule_polynomial": _build_22,
    "23_indefinite_integral_fractional_and_negative_powers": _build_23,
    "24_definite_integral_polynomial_evaluation": _build_24,
    "25_definite_integral_area_under_parabola_or_line": _build_25,
}
