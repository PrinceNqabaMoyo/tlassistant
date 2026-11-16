"""Grade 11-12 Technical Mathematics - Mensuration & Integration Archetypes 39-50.
Subskills 39 to 50:
39: Area between parabola and horizontal line
40: Area between parabola and linear line
41: Area between two intersecting parabolas
42: Volume of revolution about x-axis: cylindrical disc (V = pi * int(r^2 dx))
43: Volume of revolution about x-axis: straight line (right circular cone V = 1/3 pi r^2 h)
44: Volume of revolution about x-axis: parabola / paraboloid spindle
45: Volume of revolution about x-axis: polynomial spindle
46: Volume of revolution about x-axis: washer method (hollow solid)
47: Technical engineering cross-section: piecewise integration
48: Engineering application: Work done by expanding gas (W = int P dV)
49: Engineering application: Hydrostatic fluid pressure force
50: Comprehensive technical calculus & mensuration synthesis (autopsy & repair)

Fully compliant with 6-pillar contract, zero-LLM deterministic SymPy/math,
South African comma decimal notation {{,}}, and dynamic seed-varied inline SVGs.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    """Format numbers with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _fmt_katex(val: float | int, places: int = 2) -> str:
    """Format numbers for KaTeX with {{,}} decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


# --------------------------------------------------------------------------- #
# Archetype 39: Area between parabola and horizontal line
# --------------------------------------------------------------------------- #
def _b39_area_parabola_horizontal_line(r: random.Random) -> Dict[str, Any]:
    # Parabola y = k - a*x^2 and horizontal line y = y0
    # Enclosed between -x0 and x0 where k - a*x0^2 = y0 => a*x0^2 = k - y0
    x0 = r.choice([2, 3, 4])
    a = r.choice([1, 2])
    diff = a * (x0 ** 2)
    y0 = r.choice([1, 2, 3])
    k = y0 + diff

    # Area = int_{-x0}^{x0} ((k - a*x^2) - y0) dx = 2 * int_0^{x0} (diff - a*x^2) dx
    # = 2 * [ diff*x - a*x^3/3 ]_0^x0 = 2 * (diff*x0 - a*x0^3 / 3) = 2 * a * x0^3 * (1 - 1/3) = 4/3 * a * x0^3
    area_exact_num = 4 * a * (x0 ** 3)
    area_exact_den = 3
    area_val = round(area_exact_num / area_exact_den, 2)

    # SVG Diagram
    # ViewBox 0 0 400 260
    # Map x in [-x0-1.5, x0+1.5] -> [40, 360], y in [0, k+2] -> [220, 30]
    xmin, xmax = -x0 - 1.5, x0 + 1.5
    ymin, ymax = 0, k + 2
    def to_svg(x_val: float, y_val: float) -> tuple[float, float]:
        sx = 40 + (x_val - xmin) / (xmax - xmin) * 320
        sy = 220 - (y_val - ymin) / (ymax - ymin) * 190
        return round(sx, 1), round(sy, 1)

    ox, oy = to_svg(0, 0)
    # Generate points for curve
    curve_pts = []
    fill_pts = []
    steps = 20
    for i in range(steps + 1):
        xv = -x0 + (2 * x0 * i / steps)
        yv = k - a * (xv ** 2)
        sx, sy = to_svg(xv, yv)
        fill_pts.append(f"{sx},{sy}")
    # close fill path back along y0
    x_right, y_right = to_svg(x0, y0)
    x_left, y_left = to_svg(-x0, y0)
    fill_path = f"M {fill_pts[0]} " + " ".join(f"L {p}" for p in fill_pts[1:]) + f" L {x_right},{y_right} L {x_left},{y_left} Z"

    # Full parabola curve for plotting
    plot_pts = []
    for i in range(31):
        xv = xmin + 0.5 + (xmax - xmin - 1.0) * i / 30
        yv = max(0, k - a * (xv ** 2))
        sx, sy = to_svg(xv, yv)
        plot_pts.append(f"{sx},{sy}")
    curve_d = f"M {plot_pts[0]} " + " ".join(f"L {p}" for p in plot_pts[1:])

    lx1, ly1 = to_svg(xmin + 0.5, y0)
    lx2, ly2 = to_svg(xmax - 0.5, y0)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260" width="100%" height="100%">
  <rect width="400" height="260" fill="#f8fafc" rx="8"/>
  <path d="{fill_path}" fill="#38bdf8" fill-opacity="0.35" stroke="#0284c7" stroke-dasharray="3,3"/>
  <line x1="20" y1="{oy}" x2="380" y2="{oy}" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="380,{oy-4} 388,{oy} 380,{oy+4}" fill="#64748b"/>
  <text x="385" y="{oy+16}" font-size="12" fill="#64748b" font-family="sans-serif">x</text>
  <line x1="{ox}" y1="240" x2="{ox}" y2="20" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="{ox-4},20 {ox},12 {ox+4},20" fill="#64748b"/>
  <text x="{ox+8}" y="24" font-size="12" fill="#64748b" font-family="sans-serif">y</text>
  <path d="{curve_d}" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" stroke="#dc2626" stroke-width="2"/>
  <circle cx="{x_left}" cy="{y_left}" r="4" fill="#0f172a"/>
  <circle cx="{x_right}" cy="{y_right}" r="4" fill="#0f172a"/>
  <text x="{ox+10}" y="{to_svg(0, k)[1]-6}" font-size="11" fill="#2563eb" font-family="sans-serif">y = {k} - {a if a > 1 else ''}x²</text>
  <text x="{lx2-45}" y="{ly2-6}" font-size="11" fill="#dc2626" font-family="sans-serif">y = {y0}</text>
  <text x="{ox+15}" y="{oy-18}" font-size="12" font-weight="bold" fill="#0369a1" font-family="sans-serif">Area</text>
</svg>"""

    a_str = f"{a}" if a > 1 else ""
    neg_x0 = -x0
    prompt = (
        f"In the accompanying diagram, the curve of the parabola $y = {k} - {a_str}x^2$ intersects "
        f"the horizontal line $y = {y0}$ at two symmetric points where $x = -{x0}$ and $x = {x0}$.\n\n"
        f"1. Set up the definite integral expression representing the shaded area bounded between the parabola and the line.\n"
        f"2. Evaluate the integral to determine the exact area enclosed between the two graphs."
    )

    ans_latex = (
        rf"\text{{Area}} = \int_{{{neg_x0}}}^{{{x0}}} \left[ ({k} - {a_str}x^2) - {y0} \right] dx "
        rf"= \int_{{{neg_x0}}}^{{{x0}}} ({diff} - {a_str}x^2) dx "
        rf"= \left[ {diff}x - \frac{{{a_str}x^3}}{{3}} \right]_{{{neg_x0}}}^{{{x0}}} "
        rf"= \frac{{{area_exact_num}}}{{{area_exact_den}}} \approx {_fmt_katex(area_val)}\text{{ square units}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct definite integral formulation with limits [-{x0}; {x0}]", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Simplify integrand to ({diff} - {a_str}x^2)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Antiderivative with correct power rule integration", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Substitute limits and compute area = {area_exact_num}/{area_exact_den} or {_fmt_sa(area_val)}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "negative_area", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: The area between two curves from $x = a$ to $x = b$ is $\\int_a^b [f_{\\text{top}}(x) - g_{\\text{bottom}}(x)] dx$.",
        "tier_2": f"Here, $f(x) = {k} - {a_str}x^2$ is above the line $y = {y0}$. The integrand is $({k} - {a_str}x^2) - {y0} = {diff} - {a_str}x^2$.",
        "tier_3": f"Evaluate $\\left[ {diff}x - \\frac{{{a}x^3}}{{3}} \\right]_{{{neg_x0}}}^{{{x0}}}$. Substituting limits yields $\\frac{{{area_exact_num}}}{{{area_exact_den}}} \\approx {_fmt_sa(area_val)}\\text{{ units}}^2$.",
    }

    return {
        "id": f"tech_calc_pab_h_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_pab_h_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "39_area_between_parabola_and_horizontal_line",
        "learning_objective_id": "techmath_calc_area_parabola_line",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cone_textbook.jpg",
            "model_glb": "/models/blender_3d_cone.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["inverted_top_and_bottom_functions", "forgot_to_subtract_lower_boundary", "incorrect_limits_of_integration"],
        "keywords": ["integration", "area between curves", "parabola", "definite integral"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# --------------------------------------------------------------------------- #
# Archetype 40: Area between parabola and linear line
# --------------------------------------------------------------------------- #
def _b40_area_parabola_linear_line(r: random.Random) -> Dict[str, Any]:
    # Parabola y = x^2 and line y = mx + c intersecting at x1, x2
    # Roots: x^2 - mx - c = 0 => (x - x1)(x - x2) = 0 where x1 < 0 < x2
    x1 = r.choice([-1, -2])
    x2 = r.choice([2, 3])
    # x^2 - (x1 + x2)x + x1*x2 = 0 => m = (x1 + x2), c = -x1*x2
    m = x1 + x2
    c = -x1 * x2

    # Area = int_{x1}^{x2} ((mx + c) - x^2) dx
    # = [ m*x^2/2 + c*x - x^3/3 ]_{x1}^{x2}
    def _F(x: float) -> float:
        return (m * (x ** 2) / 2) + (c * x) - ((x ** 3) / 3)

    area_val = round(_F(x2) - _F(x1), 2)
    # Exact fraction: (x2 - x1)^3 / 6
    diff = x2 - x1
    num = diff ** 3
    den = 6
    g = math.gcd(num, den)
    frac_num, frac_den = num // g, den // g

    # SVG Diagram
    xmin, xmax = x1 - 1.2, x2 + 1.2
    ymin, ymax = -1.0, max(x1 ** 2, x2 ** 2, m * x2 + c) + 2.0
    def to_svg(xv: float, yv: float) -> tuple[float, float]:
        sx = 50 + (xv - xmin) / (xmax - xmin) * 300
        sy = 220 - (yv - ymin) / (ymax - ymin) * 190
        return round(sx, 1), round(sy, 1)

    ox, oy = to_svg(0, 0)
    # Shaded enclosed region
    fill_pts = []
    steps = 20
    for i in range(steps + 1):
        xv = x1 + (x2 - x1) * i / steps
        yv = xv ** 2
        sx, sy = to_svg(xv, yv)
        fill_pts.append(f"{sx},{sy}")
    # line points from x2 to x1
    x2_s, y2_s = to_svg(x2, m * x2 + c)
    x1_s, y1_s = to_svg(x1, m * x1 + c)
    fill_path = f"M {fill_pts[0]} " + " ".join(f"L {p}" for p in fill_pts[1:]) + f" L {x2_s},{y2_s} L {x1_s},{y1_s} Z"

    # Full parabola
    parab_pts = []
    for i in range(31):
        xv = xmin + 0.3 + (xmax - xmin - 0.6) * i / 30
        yv = xv ** 2
        sx, sy = to_svg(xv, yv)
        parab_pts.append(f"{sx},{sy}")
    parab_d = f"M {parab_pts[0]} " + " ".join(f"L {p}" for p in parab_pts[1:])

    lx1, ly1 = to_svg(xmin + 0.3, m * (xmin + 0.3) + c)
    lx2, ly2 = to_svg(xmax - 0.3, m * (xmax - 0.3) + c)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260" width="100%" height="100%">
  <rect width="400" height="260" fill="#f8fafc" rx="8"/>
  <path d="{fill_path}" fill="#a855f7" fill-opacity="0.3" stroke="#9333ea" stroke-dasharray="3,3"/>
  <line x1="20" y1="{oy}" x2="380" y2="{oy}" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="380,{oy-4} 388,{oy} 380,{oy+4}" fill="#64748b"/>
  <text x="385" y="{oy+16}" font-size="12" fill="#64748b" font-family="sans-serif">x</text>
  <line x1="{ox}" y1="240" x2="{ox}" y2="20" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="{ox-4},20 {ox},12 {ox+4},20" fill="#64748b"/>
  <text x="{ox+8}" y="24" font-size="12" fill="#64748b" font-family="sans-serif">y</text>
  <path d="{parab_d}" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" stroke="#16a34a" stroke-width="2"/>
  <circle cx="{x1_s}" cy="{y1_s}" r="4" fill="#0f172a"/>
  <circle cx="{x2_s}" cy="{y2_s}" r="4" fill="#0f172a"/>
  <text x="{x1_s-35}" y="{y1_s-6}" font-size="11" fill="#0f172a" font-family="sans-serif">({x1}; {x1**2})</text>
  <text x="{x2_s+6}" y="{y2_s}" font-size="11" fill="#0f172a" font-family="sans-serif">({x2}; {x2**2})</text>
  <text x="{ox-45}" y="50" font-size="11" fill="#2563eb" font-family="sans-serif">y = x²</text>
</svg>"""

    line_eq = f"{m}x + {c}" if m != 1 and m != 0 else (f"x + {c}" if m == 1 else f"{c}")
    prompt = (
        f"In the accompanying diagram, the straight line $g(x) = {line_eq}$ intersects "
        f"the parabola $f(x) = x^2$ at points where $x = {x1}$ and $x = {x2}$.\n\n"
        f"1. State the upper function and lower function over the interval $[{x1}; {x2}]$.\n"
        f"2. Calculate the exact area of the region enclosed between the two curves."
    )

    ans_latex = (
        rf"\text{{Over }}[{x1}; {x2}], \text{{ the line }} g(x) \ge f(x).\n"
        rf"\text{{Area}} = \int_{{{x1}}}^{{{x2}}} \left( ({line_eq}) - x^2 \right) dx "
        rf"= \left[ \frac{{{m}x^2}}{{2}} + {c}x - \frac{{x^3}}{{3}} \right]_{{{x1}}}^{{{x2}}} "
        rf"= \frac{{{frac_num}}}{{{frac_den}}} \approx {_fmt_katex(area_val)}\text{{ square units}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Identify line g(x) as top curve and parabola f(x) as bottom curve", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Set up integral from {x1} to {x2}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Antiderivative terms correct", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Evaluate limits correctly to get {frac_num}/{frac_den} or {_fmt_sa(area_val)}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "swapped_boundaries", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Identify which function lies above the other on the interval of interest.",
        "tier_2": f"Here $g(x) = {line_eq}$ is above $f(x) = x^2$. Calculate $\\int_{{{x1}}}^{{{x2}}} ({line_eq} - x^2) dx$.",
        "tier_3": f"Antiderivative: $\\left[ \\frac{{{m}x^2}}{{2}} + {c}x - \\frac{{x^3}}{{3}} \\right]_{{{x1}}}^{{{x2}}}$. Result is $\\frac{{{frac_num}}}{{{frac_den}}} \\approx {_fmt_sa(area_val)}$.",
    }

    return {
        "id": f"tech_calc_pab_lin_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_pab_lin_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "40_area_between_parabola_and_linear_line",
        "learning_objective_id": "techmath_calc_area_parabola_linear",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cone_textbook.jpg",
            "model_glb": "/models/blender_3d_cone.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["subtracted_line_from_parabola", "incorrect_limit_substitution", "sign_error_with_negative_limit"],
        "keywords": ["definite integral", "area between curves", "parabola", "linear function"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# --------------------------------------------------------------------------- #
# Archetype 41: Area between two intersecting parabolas
# --------------------------------------------------------------------------- #
def _b41_area_two_intersecting_parabolas(r: random.Random) -> Dict[str, Any]:
    # y1 = c - a*x^2 (opens downward)
    # y2 = b*x^2 - d (opens upward)
    # Intersect at roots: c - a*x^2 = b*x^2 - d => (a+b)*x^2 = c+d => x = +- x0
    x0 = r.choice([1, 2, 3])
    k_tot = r.choice([2, 4, 6]) # (a + b)
    tot_const = k_tot * (x0 ** 2) # c + d
    c = r.choice([tot_const // 2, tot_const // 2 + 1])
    d = tot_const - c
    a = k_tot // 2
    b = k_tot - a

    # Area = int_{-x0}^{x0} [ (c - a*x^2) - (b*x^2 - d) ] dx
    # = int_{-x0}^{x0} [ tot_const - k_tot * x^2 ] dx
    # = 2 * [ tot_const * x - k_tot * x^3 / 3 ]_0^x0
    # = 2 * ( tot_const * x0 - k_tot * x0^3 / 3 )
    # Since tot_const = k_tot * x0^2, this is 2 * (k_tot * x0^3 - 1/3 k_tot * x0^3) = 4/3 * k_tot * x0^3
    num = 4 * k_tot * (x0 ** 3)
    den = 3
    area_val = round(num / den, 2)

    # SVG Diagram
    xmin, xmax = -x0 - 1.2, x0 + 1.2
    ymin, ymax = -d - 1.5, c + 1.5
    def to_svg(xv: float, yv: float) -> tuple[float, float]:
        sx = 40 + (xv - xmin) / (xmax - xmin) * 320
        sy = 220 - (yv - ymin) / (ymax - ymin) * 190
        return round(sx, 1), round(sy, 1)

    ox, oy = to_svg(0, 0)
    # Lens shape fill
    steps = 20
    top_pts = []
    bot_pts = []
    for i in range(steps + 1):
        xv = -x0 + (2 * x0 * i / steps)
        yt = c - a * (xv ** 2)
        yb = b * (xv ** 2) - d
        top_pts.append(to_svg(xv, yt))
        bot_pts.append(to_svg(xv, yb))

    fill_d = f"M {top_pts[0][0]},{top_pts[0][1]} " + " ".join(f"L {p[0]},{p[1]}" for p in top_pts[1:])
    fill_d += " " + " ".join(f"L {p[0]},{p[1]}" for p in reversed(bot_pts)) + " Z"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260" width="100%" height="100%">
  <rect width="400" height="260" fill="#f8fafc" rx="8"/>
  <path d="{fill_d}" fill="#0ea5e9" fill-opacity="0.35" stroke="#0284c7" stroke-width="1.5"/>
  <line x1="20" y1="{oy}" x2="380" y2="{oy}" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="380,{oy-4} 388,{oy} 380,{oy+4}" fill="#64748b"/>
  <text x="385" y="{oy+16}" font-size="12" fill="#64748b" font-family="sans-serif">x</text>
  <line x1="{ox}" y1="240" x2="{ox}" y2="20" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="{ox-4},20 {ox},12 {ox+4},20" fill="#64748b"/>
  <text x="{ox+8}" y="24" font-size="12" fill="#64748b" font-family="sans-serif">y</text>
  <circle cx="{top_pts[0][0]}" cy="{top_pts[0][1]}" r="4" fill="#0f172a"/>
  <circle cx="{top_pts[-1][0]}" cy="{top_pts[-1][1]}" r="4" fill="#0f172a"/>
  <text x="{ox+10}" y="{to_svg(0, c)[1]-6}" font-size="11" fill="#2563eb" font-family="sans-serif">y = {c} - {a}x²</text>
  <text x="{ox+10}" y="{to_svg(0, -d)[1]+16}" font-size="11" fill="#d97706" font-family="sans-serif">y = {b}x² - {d}</text>
  <text x="{ox-28}" y="{oy-10}" font-size="12" font-weight="bold" fill="#0369a1" font-family="sans-serif">Area</text>
</svg>"""

    neg_x0 = -x0
    prompt = (
        f"In the accompanying diagram, a symmetrical closed region is bounded between two parabolas: "
        f"$f(x) = {c} - {a}x^2$ (upper curve) and $g(x) = {b}x^2 - {d}$ (lower curve).\n\n"
        f"1. Determine the $x$-coordinates of the intersection points by equating $f(x) = g(x)$.\n"
        f"2. Calculate the total enclosed area using definite integration."
    )

    ans_latex = (
        rf"1.\; {c} - {a}x^2 = {b}x^2 - {d} \implies {k_tot}x^2 = {tot_const} \implies x = \pm {x0}\n"
        rf"2.\; \text{{Area}} = \int_{{{neg_x0}}}^{{{x0}}} \left[ ({c} - {a}x^2) - ({b}x^2 - {d}) \right] dx "
        rf"= \int_{{{neg_x0}}}^{{{x0}}} ({tot_const} - {k_tot}x^2) dx "
        rf"= \left[ {tot_const}x - \frac{{{k_tot}x^3}}{{3}} \right]_{{{neg_x0}}}^{{{x0}}} "
        rf"= \frac{{{num}}}{{{den}}} \approx {_fmt_katex(area_val)}\text{{ square units}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Equate curves and solve for limits x = -{x0} and x = {x0}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Formulate integral: int [({tot_const} - {k_tot}x^2)] dx", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Perform antiderivative integration correctly", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Substitute limits to obtain {num}/{den} or {_fmt_sa(area_val)}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "incorrect_roots", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Set the equations equal to each other to solve for the boundary $x$-values.",
        "tier_2": f"Equating gives ${k_tot}x^2 = {tot_const} \\implies x = \\pm {x0}$. The upper curve is $f(x) = {c} - {a}x^2$.",
        "tier_3": f"Evaluate $\\int_{{{neg_x0}}}^{{{x0}}} ({tot_const} - {k_tot}x^2) dx = \\left[ {tot_const}x - \\frac{{{k_tot}x^3}}{{3}} \\right]_{{{neg_x0}}}^{{{x0}}} = \\frac{{{num}}}{{{den}}} \\approx {_fmt_sa(area_val)}$.",
    }

    return {
        "id": f"tech_calc_two_pab_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_two_pab_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "41_area_between_two_intersecting_parabolas",
        "learning_objective_id": "techmath_calc_area_intersecting_parabolas",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cone_textbook.jpg",
            "model_glb": "/models/blender_3d_cone.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["failed_to_find_intersection_limits", "subtracted_upper_from_lower", "forgot_to_multiply_doubled_area"],
        "keywords": ["definite integral", "intersecting parabolas", "area enclosed", "roots"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# --------------------------------------------------------------------------- #
# Archetype 42: Volume of revolution - cylindrical disc derivation
# --------------------------------------------------------------------------- #
def _b42_volume_solid_of_revolution_cylindrical_disc(r: random.Random) -> Dict[str, Any]:
    # Constant function y = R rotated about x-axis from x = 0 to x = H
    # V = pi * int_0^H y^2 dx = pi * R^2 * H
    radius = r.choice([2, 3, 4, 5, 6])
    height = r.choice([5, 8, 10, 12, 15])
    vol_exact = (radius ** 2) * height
    vol_float = round(math.pi * vol_exact, 2)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <rect width="400" height="240" fill="#f8fafc" rx="8"/>
  <ellipse cx="100" cy="120" rx="20" ry="50" fill="#cbd5e1" stroke="#475569" stroke-width="1.5"/>
  <path d="M 100,70 L 280,70 A 20,50 0 0,1 280,170 L 100,170 Z" fill="#93c5fd" fill-opacity="0.4" stroke="#2563eb" stroke-width="1.8"/>
  <ellipse cx="280" cy="120" rx="20" ry="50" fill="#60a5fa" fill-opacity="0.5" stroke="#2563eb" stroke-width="1.8"/>
  <line x1="40" y1="120" x2="360" y2="120" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="365" y="124" font-size="12" fill="#64748b" font-family="sans-serif">x-axis</text>
  <line x1="280" y1="120" x2="280" y2="70" stroke="#dc2626" stroke-width="2"/>
  <text x="290" y="98" font-size="11" fill="#dc2626" font-weight="bold" font-family="sans-serif">R = {radius} m</text>
  <line x1="100" y1="190" x2="280" y2="190" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="100,187 92,190 100,193" fill="#0f172a"/>
  <polygon points="280,187 288,190 280,193" fill="#0f172a"/>
  <text x="175" y="208" font-size="12" font-weight="bold" fill="#0f172a" font-family="sans-serif">H = {height} m</text>
</svg>"""

    prompt = (
        f"A straight boundary line segment $y = {radius}\\text{{ m}}$ over the interval "
        f"$x \\in [0; {height}]\\text{{ m}}$ is rotated $360^\\circ$ about the $x$-axis to generate a solid cylinder.\n\n"
        f"1. Apply the formula for the volume of a solid of revolution, $V = \\pi \\int_a^b [f(x)]^2 dx$, to set up the integral.\n"
        f"2. Evaluate the integral to determine the exact volume in terms of $\\pi$, and calculate the value to 2 decimal places."
    )

    ans_latex = (
        rf"V = \pi \int_{{0}}^{{{height}}} ({radius})^2 dx = \pi \int_{{0}}^{{{height}}} {radius**2} dx "
        rf"= \pi \left[ {radius**2}x \right]_{{0}}^{{{height}}} "
        rf"= {vol_exact}\pi \approx {_fmt_katex(vol_float)}\text{{ m}}^3"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Substitute f(x) = R into volume of revolution formula", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Perform integration: [R^2 * x] from 0 to H", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"State exact volume {vol_exact}*pi m^3", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Evaluate decimal approximation {_fmt_sa(vol_float)} m^3", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "forgot_pi", "penalty": -1}, {"rule": "omitted_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: For rotation about the $x$-axis, $V = \\pi \\int_a^b [y(x)]^2 dx$.",
        "tier_2": f"Here, $y = {radius}$, so $[y]^2 = {radius**2}$. Integrate ${radius**2}$ with respect to $x$ from $0$ to ${height}$.",
        "tier_3": f"$V = \\pi [{radius**2}x]_0^{{{height}}} = {vol_exact}\\pi \\approx {_fmt_sa(vol_float)}\\text{{ m}}^3$.",
    }

    return {
        "id": f"tech_calc_vol_cyl_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_vol_cyl_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "42_volume_solid_of_revolution_cylindrical_disc",
        "learning_objective_id": "techmath_calc_vol_revolution_cylinder",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cylinder_textbook.jpg",
            "model_glb": "/models/blender_3d_cylinder.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_pi_factor", "forgot_to_square_function", "incorrect_power_rule_integration"],
        "keywords": ["solid of revolution", "volume", "cylinder", "definite integral"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# --------------------------------------------------------------------------- #
# Archetype 43: Volume of revolution - linear boundary (cone)
# --------------------------------------------------------------------------- #
def _b43_volume_solid_of_revolution_linear_cone(r: random.Random) -> Dict[str, Any]:
    # y = m*x rotated from x = 0 to x = h generates a cone
    # V = pi * int_0^h (m*x)^2 dx = pi * m^2 * [x^3/3]_0^h = 1/3 * pi * m^2 * h^3 = 1/3 * pi * R^2 * h (where R = m*h)
    m_num = r.choice([1, 2, 3])
    m_den = r.choice([2, 3, 4])
    g = math.gcd(m_num, m_den)
    m_num, m_den = m_num // g, m_den // g
    h = r.choice([3, 6, 9, 12])

    radius = (m_num * h) / m_den
    # V = pi * (m_num/m_den)^2 * h^3 / 3
    vol_num = (m_num ** 2) * (h ** 3)
    vol_den = 3 * (m_den ** 2)
    g_vol = math.gcd(vol_num, vol_den)
    v_num_red = vol_num // g_vol
    v_den_red = vol_den // g_vol
    vol_float = round(math.pi * v_num_red / v_den_red, 2)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <rect width="400" height="240" fill="#f8fafc" rx="8"/>
  <line x1="40" y1="120" x2="360" y2="120" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="365" y="124" font-size="12" fill="#64748b" font-family="sans-serif">x-axis</text>
  <path d="M 80,120 L 260,60 A 15,60 0 0,1 260,180 Z" fill="#fdba74" fill-opacity="0.45" stroke="#ea580c" stroke-width="2"/>
  <ellipse cx="260" cy="120" rx="15" ry="60" fill="#fb923c" fill-opacity="0.5" stroke="#ea580c" stroke-width="1.8"/>
  <circle cx="80" cy="120" r="4" fill="#0f172a"/>
  <text x="65" y="140" font-size="11" fill="#0f172a" font-family="sans-serif">(0; 0)</text>
  <line x1="260" y1="120" x2="260" y2="60" stroke="#dc2626" stroke-width="2"/>
  <text x="270" y="95" font-size="11" fill="#dc2626" font-weight="bold" font-family="sans-serif">R = {_fmt_sa(radius)} m</text>
  <line x1="80" y1="200" x2="260" y2="200" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="80,197 72,200 80,203" fill="#0f172a"/>
  <polygon points="260,197 268,200 260,203" fill="#0f172a"/>
  <text x="160" y="218" font-size="12" font-weight="bold" fill="#0f172a" font-family="sans-serif">h = {h} m</text>
</svg>"""

    frac_str = f"\\frac{{{m_num}}}{{{m_den}}}" if m_den > 1 else f"{m_num}"
    prompt = (
        f"A straight line $y = {frac_str}x$ from $x = 0\\text{{ m}}$ to $x = {h}\\text{{ m}}$ "
        f"is rotated through $360^\\circ$ about the $x$-axis, forming a solid right circular cone.\n\n"
        f"1. Use calculus of solids of revolution ($V = \\pi \\int_a^b y^2 dx$) to set up and evaluate the definite integral.\n"
        f"2. Give the exact volume in terms of $\\pi$ and correct to two decimal places."
    )

    ans_latex = (
        rf"V = \pi \int_{{0}}^{{{h}}} \left( {frac_str}x \right)^2 dx "
        rf"= \pi \frac{{{m_num**2}}}{{{m_den**2}}} \int_{{0}}^{{{h}}} x^2 dx "
        rf"= \pi \frac{{{m_num**2}}}{{{m_den**2}}} \left[ \frac{{x^3}}{{3}} \right]_{{0}}^{{{h}}} "
        rf"= \frac{{{v_num_red}\pi}}{{{v_den_red}}} \approx {_fmt_katex(vol_float)}\text{{ m}}^3"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Square the function: (m*x)^2 = m^2 * x^2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Integrate x^2 to x^3/3", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Substitute limits 0 to {h}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Final answer: {v_num_red}pi/{v_den_red} or {_fmt_sa(vol_float)} m^3", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_pi", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: $V = \\pi \\int_a^b [f(x)]^2 dx$. Here $f(x) = " + frac_str + "x$.",
        "tier_2": "Square the coefficient and the variable before integrating: $\\left(" + frac_str + "x\\right)^2 = \\frac{" + str(m_num**2) + "}{" + str(m_den**2) + "} x^2$.",
        "tier_3": f"Evaluating gives $\\frac{{{v_num_red}\\pi}}{{{v_den_red}}} \\approx {_fmt_sa(vol_float)}\\text{{ m}}^3$.",
    }

    return {
        "id": f"tech_calc_vol_cone_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_vol_cone_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "43_volume_solid_of_revolution_linear_cone",
        "learning_objective_id": "techmath_calc_vol_revolution_cone",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cone_textbook.jpg",
            "model_glb": "/models/blender_3d_cone.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_to_square_slope", "integrated_x_instead_of_x_squared", "forgot_pi_multiplier"],
        "keywords": ["volume of revolution", "cone", "linear boundary", "calculus"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# --------------------------------------------------------------------------- #
# Archetype 44: Volume of revolution - parabola / paraboloid
# --------------------------------------------------------------------------- #
def _b44_volume_solid_of_revolution_paraboloid(r: random.Random) -> Dict[str, Any]:
    # y = sqrt(k * x) rotated about x-axis from x = 0 to x = b
    # => y^2 = k*x => V = pi * int_0^b k*x dx = pi * k * [x^2/2]_0^b = 1/2 * pi * k * b^2
    k = r.choice([2, 4, 6, 8])
    b = r.choice([3, 4, 5, 6])
    vol_exact = (k * (b ** 2)) // 2
    vol_float = round(math.pi * vol_exact, 2)
    radius_end = round(math.sqrt(k * b), 2)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <rect width="400" height="240" fill="#f8fafc" rx="8"/>
  <line x1="40" y1="120" x2="360" y2="120" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="365" y="124" font-size="12" fill="#64748b" font-family="sans-serif">x-axis</text>
  <path d="M 80,120 Q 180,60 280,50 A 15,70 0 0,1 280,190 Q 180,180 80,120 Z" fill="#38bdf8" fill-opacity="0.35" stroke="#0284c7" stroke-width="2"/>
  <ellipse cx="280" cy="120" rx="15" ry="70" fill="#0284c7" fill-opacity="0.4" stroke="#0284c7" stroke-width="1.8"/>
  <line x1="280" y1="120" x2="280" y2="50" stroke="#dc2626" stroke-width="2"/>
  <text x="290" y="90" font-size="11" fill="#dc2626" font-weight="bold" font-family="sans-serif">R = {_fmt_sa(radius_end)} cm</text>
  <line x1="80" y1="210" x2="280" y2="210" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="80,207 72,210 80,213" fill="#0f172a"/>
  <polygon points="280,207 288,210 280,213" fill="#0f172a"/>
  <text x="170" y="228" font-size="12" font-weight="bold" fill="#0f172a" font-family="sans-serif">b = {b} cm</text>
  <text x="140" y="45" font-size="12" fill="#0284c7" font-weight="bold" font-family="sans-serif">y = √({k}x)</text>
</svg>"""

    prompt = (
        f"A parabolic profile curve given by $y = \\sqrt{{{k}x}}$ (where $x$ and $y$ are in centimetres) "
        f"over the interval $x \\in [0; {b}]$ is rotated through $360^\\circ$ about the $x$-axis to produce a technical paraboloid reflector.\n\n"
        f"1. Set up the definite integral for the volume of revolution.\n"
        f"2. Evaluate the integral to determine the internal volume in terms of $\\pi$, and calculate the volume correct to two decimal places."
    )

    ans_latex = (
        rf"V = \pi \int_{{0}}^{{{b}}} \left( \sqrt{{{k}x}} \right)^2 dx "
        rf"= \pi \int_{{0}}^{{{b}}} {k}x \, dx "
        rf"= \pi \left[ \frac{{{k}x^2}}{{2}} \right]_{{0}}^{{{b}}} "
        rf"= {vol_exact}\pi \approx {_fmt_katex(vol_float)}\text{{ cm}}^3"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Square the radical: [sqrt(kx)]^2 = kx", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Integrate kx to (k*x^2)/2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Substitute limits 0 to {b}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculate exact volume {vol_exact}pi and decimal {_fmt_sa(vol_float)} cm^3", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Squaring a square root cancels the radical: $[\\sqrt{kx}]^2 = kx$.",
        "tier_2": f"Integrate $V = \\pi \\int_0^{{{b}}} {k}x \\, dx = \\pi \\left[ \\frac{{{k}x^2}}{{2}} \\right]_0^{{{b}}}$.",
        "tier_3": f"Substitute $x = {b}$: $V = \\frac{{{k}({b}^2)}}{{2}}\\pi = {vol_exact}\\pi \\approx {_fmt_sa(vol_float)}\\text{{ cm}}^3$.",
    }

    return {
        "id": f"tech_calc_vol_pab_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_vol_pab_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "44_volume_solid_of_revolution_paraboloid",
        "learning_objective_id": "techmath_calc_vol_revolution_paraboloid",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cone_textbook.jpg",
            "model_glb": "/models/blender_3d_cone.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["failed_to_square_square_root", "forgot_to_divide_by_two", "omitted_pi_factor"],
        "keywords": ["solid of revolution", "paraboloid", "square root curve", "definite integral"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# --------------------------------------------------------------------------- #
# Archetype 45: Volume of revolution - polynomial spindle
# --------------------------------------------------------------------------- #
def _b45_volume_solid_of_revolution_polynomial_spindle(r: random.Random) -> Dict[str, Any]:
    # y = a*(x^2 - x^3) or y = x*(L - x) from x = 0 to L
    # Let y = x*(L - x) from x = 0 to L
    # y^2 = x^2 * (L^2 - 2Lx + x^2) = L^2 x^2 - 2L x^3 + x^4
    # int_0^L y^2 dx = [ L^2 x^3/3 - 2L x^4/4 + x^5/5 ]_0^L = L^5 * (1/3 - 1/2 + 1/5)
    # 1/3 - 1/2 + 1/5 = (10 - 15 + 6)/30 = 1/30
    # So V = pi * L^5 / 30
    L = r.choice([2, 3, 4, 5])
    num = L ** 5
    den = 30
    g = math.gcd(num, den)
    red_num = num // g
    red_den = den // g
    vol_float = round(math.pi * red_num / red_den, 2)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <rect width="400" height="240" fill="#f8fafc" rx="8"/>
  <line x1="40" y1="120" x2="360" y2="120" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="365" y="124" font-size="12" fill="#64748b" font-family="sans-serif">x-axis</text>
  <path d="M 80,120 Q 200,40 320,120 Q 200,200 80,120 Z" fill="#a78bfa" fill-opacity="0.4" stroke="#7c3aed" stroke-width="2.2"/>
  <ellipse cx="200" cy="120" rx="14" ry="40" fill="none" stroke="#7c3aed" stroke-dasharray="3,3"/>
  <circle cx="80" cy="120" r="4" fill="#0f172a"/>
  <circle cx="320" cy="120" r="4" fill="#0f172a"/>
  <text x="70" y="140" font-size="11" fill="#0f172a" font-family="sans-serif">x = 0</text>
  <text x="310" y="140" font-size="11" fill="#0f172a" font-family="sans-serif">x = {L}</text>
  <line x1="80" y1="210" x2="320" y2="210" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="80,207 72,210 80,213" fill="#0f172a"/>
  <polygon points="320,207 328,210 320,213" fill="#0f172a"/>
  <text x="190" y="228" font-size="12" font-weight="bold" fill="#0f172a" font-family="sans-serif">L = {L} m</text>
  <text x="160" y="35" font-size="12" fill="#7c3aed" font-weight="bold" font-family="sans-serif">y = x({L} - x)</text>
</svg>"""

    prompt = (
        f"A symmetrical spindle solid is generated by rotating the parabolic arch "
        f"$y = x({L} - x)$ (where measurements are in metres) about the $x$-axis from $x = 0$ to $x = {L}$.\n\n"
        f"1. Expand $y^2 = [x({L} - x)]^2$ as a polynomial in powers of $x$.\n"
        f"2. Use the volume of revolution formula $V = \\pi \\int_0^{L} y^2 dx$ to evaluate the exact volume."
    )

    ans_latex = (
        rf"y^2 = x^2({L**2} - {2*L}x + x^2) = {L**2}x^2 - {2*L}x^3 + x^4\n"
        rf"V = \pi \int_{{0}}^{{{L}}} ({L**2}x^2 - {2*L}x^3 + x^4) dx "
        rf"= \pi \left[ \frac{{{L**2}x^3}}{{3}} - \frac{{{2*L}x^4}}{{4}} + \frac{{x^5}}{{5}} \right]_{{0}}^{{{L}}} "
        rf"= \frac{{{red_num}\pi}}{{{red_den}}} \approx {_fmt_katex(vol_float)}\text{{ m}}^3"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct expansion of y^2 = {L**2}x^2 - {2*L}x^3 + x^4", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Antiderivative terms with power rule", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Substitute limits 0 to {L}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Final simplified fraction {red_num}pi/{red_den} or {_fmt_sa(vol_float)} m^3", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "algebraic_expansion_error", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Expand $y^2 = [x(" + str(L) + " - x)]^2 = x^2(" + str(L**2) + " - " + str(2*L) + "x + x^2)$ first.",
        "tier_2": "Integrate each term individually using $\\int x^n dx = \\frac{x^{n+1}}{n+1}$.",
        "tier_3": f"Evaluating at $x = {L}$ yields $\\pi \\left( \\frac{{{L**5}}}{{3}} - \\frac{{{L**5}}}{{2}} + \\frac{{{L**5}}}{{5}} \\right) = \\frac{{{red_num}\\pi}}{{{red_den}}} \\approx {_fmt_sa(vol_float)}\\text{{ m}}^3$.",
    }

    return {
        "id": f"tech_calc_vol_spindle_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_vol_spindle_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "45_volume_solid_of_revolution_polynomial_spindle",
        "learning_objective_id": "techmath_calc_vol_revolution_spindle",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cone_textbook.jpg",
            "model_glb": "/models/blender_3d_cone.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["incorrect_binomial_expansion", "integrated_without_squaring", "fraction_addition_error"],
        "keywords": ["solid of revolution", "polynomial", "spindle", "definite integration"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# --------------------------------------------------------------------------- #
# Archetype 46: Volume of revolution - washer method (hollow solid)
# --------------------------------------------------------------------------- #
def _b46_volume_solid_of_revolution_washer_method(r: random.Random) -> Dict[str, Any]:
    # Region between y_outer = R2 and y_inner = R1 rotated from x = 0 to H
    # Or y_outer = sqrt(x) and y_inner = x/k
    # Let's use two concentric boundaries y_outer = R2 and y_inner = R1
    # V = pi * int_a^b (y_outer^2 - y_inner^2) dx = pi * (R2^2 - R1^2) * (b - a)
    r1 = r.choice([2, 3, 4])
    r2 = r1 + r.choice([2, 3, 4])
    height = r.choice([6, 8, 10, 12])
    diff_sq = (r2 ** 2) - (r1 ** 2)
    vol_exact = diff_sq * height
    vol_float = round(math.pi * vol_exact, 2)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <rect width="400" height="240" fill="#f8fafc" rx="8"/>
  <ellipse cx="100" cy="120" rx="20" ry="60" fill="#94a3b8" stroke="#475569" stroke-width="1.5"/>
  <ellipse cx="100" cy="120" rx="10" ry="30" fill="#f8fafc" stroke="#475569" stroke-width="1.5"/>
  <path d="M 100,60 L 280,60 A 20,60 0 0,1 280,180 L 100,180 Z" fill="#38bdf8" fill-opacity="0.35" stroke="#0284c7" stroke-width="1.8"/>
  <path d="M 100,90 L 280,90 A 10,30 0 0,1 280,150 L 100,150 Z" fill="#f8fafc" stroke="#475569" stroke-dasharray="3,3"/>
  <ellipse cx="280" cy="120" rx="20" ry="60" fill="#0284c7" fill-opacity="0.4" stroke="#0284c7" stroke-width="1.8"/>
  <ellipse cx="280" cy="120" rx="10" ry="30" fill="#f8fafc" stroke="#475569" stroke-width="1.5"/>
  <line x1="280" y1="120" x2="280" y2="90" stroke="#16a34a" stroke-width="2"/>
  <text x="290" y="108" font-size="11" fill="#16a34a" font-weight="bold" font-family="sans-serif">r₁ = {r1} mm</text>
  <line x1="280" y1="120" x2="280" y2="60" stroke="#dc2626" stroke-width="2"/>
  <text x="290" y="75" font-size="11" fill="#dc2626" font-weight="bold" font-family="sans-serif">r₂ = {r2} mm</text>
  <line x1="100" y1="200" x2="280" y2="200" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="100,197 92,200 100,203" fill="#0f172a"/>
  <polygon points="280,197 288,200 280,203" fill="#0f172a"/>
  <text x="175" y="218" font-size="12" font-weight="bold" fill="#0f172a" font-family="sans-serif">h = {height} mm</text>
</svg>"""

    prompt = (
        f"A hollow cylindrical bronze bushing of length $h = {height}\\text{{ mm}}$ has an outer radius of "
        f"$r_2 = {r2}\\text{{ mm}}$ and an inner bore radius of $r_1 = {r1}\\text{{ mm}}$.\n\n"
        f"1. State the washer method formula for the volume of revolution of a hollow solid about the $x$-axis.\n"
        f"2. Apply integration to calculate the volume of metal in the bushing in terms of $\\pi$ and to 2 decimal places."
    )

    ans_latex = (
        rf"V = \pi \int_{{0}}^{{{height}}} \left( r_2^2 - r_1^2 \right) dx "
        rf"= \pi \int_{{0}}^{{{height}}} ({r2**2} - {r1**2}) dx "
        rf"= \pi \int_{{0}}^{{{height}}} {diff_sq} \, dx "
        rf"= \pi \left[ {diff_sq}x \right]_{{0}}^{{{height}}} "
        rf"= {vol_exact}\pi \approx {_fmt_katex(vol_float)}\text{{ mm}}^3"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "State washer formula V = pi * int (R2^2 - R1^2) dx", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Compute difference of squares: {r2}^2 - {r1}^2 = {diff_sq}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Integrate constant difference over interval [0; h]", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"State exact volume {vol_exact}pi and decimal {_fmt_sa(vol_float)} mm^3", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "squared_difference_instead_of_difference_of_squares", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: For hollow solids, $V = \\pi \\int_a^b [y_{\\text{outer}}^2 - y_{\\text{inner}}^2] dx$.",
        "tier_2": f"Here $r_2^2 - r_1^2 = {r2}^2 - {r1}^2 = {r2**2} - {r1**2} = {diff_sq}$.",
        "tier_3": f"Multiply by height: $V = \\pi \\times {diff_sq} \\times {height} = {vol_exact}\\pi \\approx {_fmt_sa(vol_float)}\\text{{ mm}}^3$.",
    }

    return {
        "id": f"tech_calc_vol_washer_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_vol_washer_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "46_volume_solid_of_revolution_washer_method",
        "learning_objective_id": "techmath_calc_vol_revolution_washer",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cylinder_textbook.jpg",
            "model_glb": "/models/blender_3d_cylinder.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["squared_the_difference_r2_minus_r1", "forgot_pi_factor", "incorrect_inner_outer_order"],
        "keywords": ["washer method", "hollow cylinder", "volume of revolution", "calculus"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# --------------------------------------------------------------------------- #
# Archetype 47: Engineering cross-section: piecewise integration
# --------------------------------------------------------------------------- #
def _b47_engineering_cross_section_piecewise_area(r: random.Random) -> Dict[str, Any]:
    # Bracket profile with two segments:
    # 0 <= x <= x1: y1 = m1*x
    # x1 <= x <= x2: y2 = y_max - m2*(x - x1)
    x1 = r.choice([2, 3, 4])
    x2 = x1 + r.choice([3, 4, 5])
    y_max = r.choice([6, 8, 10])

    # A1 = int_0^x1 (y_max / x1)*x dx = 1/2 * y_max * x1
    # A2 = int_x1^x2 (horizontal or sloped)
    # Let y2 be constant y_max: A2 = y_max * (x2 - x1)
    a1 = 0.5 * y_max * x1
    a2 = y_max * (x2 - x1)
    total_area = round(a1 + a2, 2)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <rect width="400" height="240" fill="#f8fafc" rx="8"/>
  <polygon points="60,190 {60 + x1*25},{190 - y_max*15} {60 + x2*25},{190 - y_max*15} {60 + x2*25},190" fill="#6ee7b7" fill-opacity="0.4" stroke="#059669" stroke-width="2"/>
  <line x1="40" y1="190" x2="360" y2="190" stroke="#64748b" stroke-width="1.5"/>
  <line x1="60" y1="210" x2="60" y2="40" stroke="#64748b" stroke-width="1.5"/>
  <line x1="{60 + x1*25}" y1="190" x2="{60 + x1*25}" y2="{190 - y_max*15}" stroke="#059669" stroke-dasharray="3,3"/>
  <text x="60" y="205" font-size="11" fill="#64748b" font-family="sans-serif">0</text>
  <text x="{60 + x1*25 - 5}" y="205" font-size="11" fill="#64748b" font-family="sans-serif">{x1}</text>
  <text x="{60 + x2*25 - 5}" y="205" font-size="11" fill="#64748b" font-family="sans-serif">{x2}</text>
  <text x="35" y="{190 - y_max*15 + 4}" font-size="11" fill="#64748b" font-family="sans-serif">{y_max}</text>
  <text x="{60 + x1*12}" y="{190 - y_max*6}" font-size="12" font-weight="bold" fill="#047857" font-family="sans-serif">A₁</text>
  <text x="{60 + x1*25 + (x2-x1)*12}" y="{190 - y_max*7}" font-size="12" font-weight="bold" fill="#047857" font-family="sans-serif">A₂</text>
</svg>"""

    slope = round(y_max / x1, 2)
    prompt = (
        f"A machined engineering steel bracket profile shown in the figure is bounded below by the $x$-axis and "
        f"above by a piecewise function: $f_1(x) = {_fmt_sa(slope)}x$ for $0 \\le x \\le {x1}$, and $f_2(x) = {y_max}$ for ${x1} \\le x \\le {x2}$ (all dimensions in centimetres).\n\n"
        f"1. Set up the two definite integrals representing the areas $A_1$ and $A_2$.\n"
        f"2. Calculate the total cross-sectional area of the bracket."
    )

    ans_latex = (
        rf"A_1 = \int_{{0}}^{{{x1}}} {_fmt_katex(slope)}x \, dx = \left[ \frac{{{_fmt_katex(slope)}x^2}}{{2}} \right]_{{0}}^{{{x1}}} = {_fmt_katex(a1)}\text{{ cm}}^2\n"
        rf"A_2 = \int_{{{x1}}}^{{{x2}}} {y_max} \, dx = \left[ {y_max}x \right]_{{{x1}}}^{{{x2}}} = {y_max}({x2} - {x1}) = {_fmt_katex(a2)}\text{{ cm}}^2\n"
        rf"\text{{Total Area}} = A_1 + A_2 = {_fmt_katex(a1)} + {_fmt_katex(a2)} = {_fmt_katex(total_area)}\text{{ cm}}^2"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Set up integral for A1 over [0; {x1}]", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Compute A1 = {_fmt_sa(a1)} cm^2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Set up and compute A2 over [{x1}; {x2}] = {_fmt_sa(a2)} cm^2", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Add areas to obtain total area = {_fmt_sa(total_area)} cm^2", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Split the area into two intervals: from $0$ to $" + str(x1) + "$ and from $" + str(x1) + "$ to $" + str(x2) + "$.",
        "tier_2": f"Integrate $f_1(x) = {_fmt_sa(slope)}x$ on the first interval and $f_2(x) = {y_max}$ on the second.",
        "tier_3": f"$A_1 = {_fmt_sa(a1)}\\text{{ cm}}^2$ and $A_2 = {_fmt_sa(a2)}\\text{{ cm}}^2$. Sum: {_fmt_sa(total_area)}\\text{{ cm}}^2$.",
    }

    return {
        "id": f"tech_calc_piecewise_area_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_piecewise_area_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "47_engineering_cross_section_piecewise_area",
        "learning_objective_id": "techmath_calc_piecewise_area",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cone_textbook.jpg",
            "model_glb": "/models/blender_3d_cone.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["integrated_over_single_wrong_interval", "incorrect_constant_integration", "omitted_units"],
        "keywords": ["piecewise integration", "cross-section", "engineering profile", "definite integral"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# --------------------------------------------------------------------------- #
# Archetype 48: Engineering application: Work done by expanding gas
# --------------------------------------------------------------------------- #
def _b48_engineering_work_done_expanding_gas(r: random.Random) -> Dict[str, Any]:
    # W = int_{V1}^{V2} P(V) dV
    # Linear pressure drop model: P(V) = P0 - k*V
    # Or constant k: P(V) = c / V (isothermal)
    # Technical math standard polynomial: P(V) = A - B*V in kPa
    p0 = r.choice([500, 600, 800, 1000])
    b_rate = r.choice([50, 100, 150])
    v1 = r.choice([1, 2])
    v2 = v1 + r.choice([2, 3, 4])

    # W = int_{v1}^{v2} (p0 - b_rate*V) dV = [ p0*V - b_rate*V^2 / 2 ]_{v1}^{v2}
    w_exact = (p0 * (v2 - v1)) - (0.5 * b_rate * ((v2 ** 2) - (v1 ** 2)))
    work_val = round(w_exact, 2)

    # SVG Diagram - P-V indicator diagram
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <rect width="400" height="240" fill="#f8fafc" rx="8"/>
  <line x1="60" y1="200" x2="360" y2="200" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="360,196 368,200 360,204" fill="#64748b"/>
  <text x="340" y="220" font-size="12" fill="#64748b" font-family="sans-serif">Volume V (m³)</text>
  <line x1="60" y1="200" x2="60" y2="30" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="56,30 60,22 64,30" fill="#64748b"/>
  <text x="70" y="35" font-size="12" fill="#64748b" font-family="sans-serif">Pressure P (kPa)</text>
  <polygon points="120,200 120,80 280,130 280,200" fill="#fef08a" fill-opacity="0.5" stroke="#ca8a04" stroke-width="1.8"/>
  <line x1="100" y1="74" x2="300" y2="136" stroke="#b45309" stroke-width="2.5"/>
  <line x1="120" y1="200" x2="120" y2="80" stroke="#64748b" stroke-dasharray="3,3"/>
  <line x1="280" y1="200" x2="280" y2="130" stroke="#64748b" stroke-dasharray="3,3"/>
  <text x="110" y="218" font-size="11" fill="#0f172a" font-family="sans-serif">V₁ = {v1}</text>
  <text x="270" y="218" font-size="11" fill="#0f172a" font-family="sans-serif">V₂ = {v2}</text>
  <text x="180" y="160" font-size="12" font-weight="bold" fill="#854d0e" font-family="sans-serif">Work (W)</text>
</svg>"""

    prompt = (
        f"In a reciprocating engine cylinder, a gas expands from volume $V_1 = {v1}\\text{{ m}}^3$ "
        f"to $V_2 = {v2}\\text{{ m}}^3$. The pressure during the expansion follows the linear relation "
        f"$P(V) = ({p0} - {b_rate}V)\\text{{ kPa}}$, as shown in the indicator diagram.\n\n"
        f"1. Write down the definite integral expression for the work done: $W = \\int_{{V_1}}^{{V_2}} P(V) \\, dV$.\n"
        f"2. Evaluate the integral to determine the work done in kilojoules (kJ)."
    )

    ans_latex = (
        rf"W = \int_{{{v1}}}^{{{v2}}} ({p0} - {b_rate}V) \, dV "
        rf"= \left[ {p0}V - \frac{{{b_rate}V^2}}{{2}} \right]_{{{v1}}}^{{{v2}}} "
        rf"= \left( {p0}({v2}) - \frac{{{b_rate}({v2}^2)}}{{2}} \right) - \left( {p0}({v1}) - \frac{{{b_rate}({v1}^2)}}{{2}} \right) "
        rf"= {_fmt_katex(work_val)}\text{{ kJ}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Set up integral W = int_{v1}^{v2} ({p0} - {b_rate}V) dV", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Perform antiderivative integration correctly", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Substitute limits V1 = {v1} and V2 = {v2}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"State final work = {_fmt_sa(work_val)} kJ", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Work done by an expanding gas is the area under the $P-V$ diagram: $W = \\int_{V_1}^{V_2} P(V) dV$.",
        "tier_2": f"Integrate: $\\int_{{{v1}}}^{{{v2}}} ({p0} - {b_rate}V) dV = \\left[ {p0}V - \\frac{{{b_rate}V^2}}{{2}} \\right]_{{{v1}}}^{{{v2}}}$.",
        "tier_3": f"Substitute the limits to obtain $W = {_fmt_sa(work_val)}\\text{{ kJ}}$.",
    }

    return {
        "id": f"tech_calc_work_gas_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_work_gas_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "48_engineering_work_done_expanding_gas",
        "learning_objective_id": "techmath_calc_work_gas",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cone_textbook.jpg",
            "model_glb": "/models/blender_3d_cone.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_to_integrate_pressure", "incorrect_power_rule_on_V", "inverted_integration_limits"],
        "keywords": ["thermodynamics", "work done", "P-V diagram", "definite integration"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# --------------------------------------------------------------------------- #
# Archetype 49: Engineering application: Hydrostatic fluid pressure force
# --------------------------------------------------------------------------- #
def _b49_engineering_fluid_hydrostatic_force(r: random.Random) -> Dict[str, Any]:
    # Hydrostatic force on vertical rectangular gate of width W submerged from depth d1 to d2:
    # F = rho * g * W * int_{d1}^{d2} y dy
    # Let rho = 1000 kg/m^3, g = 9.8 m/s^2 => rho*g = 9.8 kN/m^3
    width = r.choice([2, 3, 4, 5])
    d1 = r.choice([0, 1, 2])
    d2 = d1 + r.choice([2, 3, 4])
    # int_{d1}^{d2} y dy = (d2^2 - d1^2)/2
    integral_val = (d2 ** 2 - d1 ** 2) / 2.0
    # Force in kN: 9.8 * width * integral_val
    force_kn = round(9.8 * width * integral_val, 2)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <rect width="400" height="240" fill="#f8fafc" rx="8"/>
  <rect x="50" y="40" width="220" height="170" fill="#bae6fd" fill-opacity="0.45"/>
  <line x1="40" y1="40" x2="280" y2="40" stroke="#0284c7" stroke-width="2.5"/>
  <text x="290" y="45" font-size="12" fill="#0284c7" font-weight="bold" font-family="sans-serif">Water Surface (y = 0)</text>
  <rect x="220" y="{40 + d1*25}" width="20" height="{(d2 - d1)*25}" fill="#64748b" stroke="#334155" stroke-width="2"/>
  <text x="250" y="{40 + d1*25 + 15}" font-size="11" fill="#334155" font-weight="bold" font-family="sans-serif">Gate</text>
  <line x1="200" y1="40" x2="200" y2="{40 + d1*25}" stroke="#dc2626" stroke-width="1.5"/>
  <text x="160" y="{40 + d1*12 + 5}" font-size="11" fill="#dc2626" font-family="sans-serif">d₁ = {d1} m</text>
  <line x1="180" y1="40" x2="180" y2="{40 + d2*25}" stroke="#dc2626" stroke-width="1.5"/>
  <text x="140" y="{40 + d2*15 + 5}" font-size="11" fill="#dc2626" font-family="sans-serif">d₂ = {d2} m</text>
  <polygon points="170,{40 + d1*25 + (d2-d1)*12} 210,{40 + d1*25 + (d2-d1)*12}" stroke="#2563eb" stroke-width="2.5"/>
  <polygon points="210,{40 + d1*25 + (d2-d1)*12 - 4} 218,{40 + d1*25 + (d2-d1)*12} 210,{40 + d1*25 + (d2-d1)*12 + 4}" fill="#2563eb"/>
  <text x="110" y="{40 + d1*25 + (d2-d1)*12 - 6}" font-size="12" font-weight="bold" fill="#2563eb" font-family="sans-serif">Hydrostatic Thrust F</text>
</svg>"""

    prompt = (
        f"A vertical rectangular sluice gate of width $W = {width}\\text{{ m}}$ retains fresh water "
        f"($\\rho g = 9{{,}}8\\text{{ kN/m}}^3$). The top of the gate is at a depth of $y = {d1}\\text{{ m}}$ "
        f"below the water surface and the bottom is at $y = {d2}\\text{{ m}}$, as shown in the diagram.\n\n"
        f"The hydrostatic pressure force is given by $F = \\rho g W \\int_{{d_1}}^{{d_2}} y \\, dy$.\n\n"
        f"1. Set up and evaluate the definite integral $\\int_{{{d1}}}^{{{d2}}} y \\, dy$.\n"
        f"2. Calculate the total hydrostatic thrust force $F$ acting on the gate in kilonewtons (kN)."
    )

    ans_latex = (
        rf"\int_{{{d1}}}^{{{d2}}} y \, dy = \left[ \frac{{y^2}}{{2}} \right]_{{{d1}}}^{{{d2}}} "
        rf"= \frac{{{d2}^2 - {d1}^2}}{{2}} = {_fmt_katex(integral_val)}\text{{ m}}^2\n"
        rf"F = 9{{,}}8 \times {width} \times {_fmt_katex(integral_val)} = {_fmt_katex(force_kn)}\text{{ kN}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Integrate y to y^2/2 with limits [{d1}; {d2}]", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Evaluate integral value = {_fmt_sa(integral_val)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Multiply by unit weight rho*g and width W", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Compute total thrust force = {_fmt_sa(force_kn)} kN", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Hydrostatic force is $F = \\rho g W \\int_{d_1}^{d_2} y dy$.",
        "tier_2": f"First integrate $\\int_{{{d1}}}^{{{d2}}} y dy = \\left[ \\frac{{y^2}}{{2}} \\right]_{{{d1}}}^{{{d2}}} = \\frac{{{d2**2} - {d1**2}}}{{2}} = {_fmt_sa(integral_val)}$.",
        "tier_3": f"Multiply: $F = 9{{,}}8 \\times {width} \\times {_fmt_sa(integral_val)} = {_fmt_sa(force_kn)}\\text{{ kN}}$.",
    }

    return {
        "id": f"tech_calc_hydrostatic_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_hydrostatic_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "49_engineering_fluid_hydrostatic_force",
        "learning_objective_id": "techmath_calc_hydrostatic_force",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cone_textbook.jpg",
            "model_glb": "/models/blender_3d_cone.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["treated_depth_as_constant_pressure", "forgot_to_divide_y_squared_by_two", "omitted_width_factor"],
        "keywords": ["hydrostatic pressure", "fluid mechanics", "sluice gate", "definite integral"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# --------------------------------------------------------------------------- #
# Archetype 50: Comprehensive technical calculus & mensuration synthesis
# --------------------------------------------------------------------------- #
def _b50_technical_calculus_mensuration_synthesis(r: random.Random) -> Dict[str, Any]:
    # Comparison of Trapezoidal approximation vs Exact definite integral for y = x^2 from 0 to 4 with n intervals
    n = r.choice([2, 4])
    b = 4
    h = b / n
    ordinates = [(i * h) ** 2 for i in range(n + 1)]

    # Trapezoidal rule: h * [ (y0 + yn)/2 + sum(y1..yn-1) ]
    ends = (ordinates[0] + ordinates[-1]) / 2.0
    middle = sum(ordinates[1:-1])
    trap_area = round(h * (ends + middle), 2)

    # Exact integral: int_0^b x^2 dx = b^3 / 3
    exact_num = b ** 3
    exact_den = 3
    exact_val = round(exact_num / exact_den, 2)

    # Absolute error and percentage error
    err = round(trap_area - exact_val, 2)
    pct_err = round((err / exact_val) * 100, 2)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <rect width="400" height="240" fill="#f8fafc" rx="8"/>
  <line x1="40" y1="200" x2="360" y2="200" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="360,196 368,200 360,204" fill="#64748b"/>
  <text x="365" y="215" font-size="12" fill="#64748b" font-family="sans-serif">x</text>
  <line x1="60" y1="210" x2="60" y2="30" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="56,30 60,22 64,30" fill="#64748b"/>
  <text x="70" y="35" font-size="12" fill="#64748b" font-family="sans-serif">y</text>
  <path d="M 60,200 Q 180,185 300,50" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  <!-- Trapezoids -->
  <polygon points="60,200 120,200 120,{200 - ordinates[1 if n==4 else 1]*9} 60,200" fill="#fbcfe8" fill-opacity="0.4" stroke="#db2777" stroke-dasharray="3,3"/>
  <polygon points="120,200 300,200 300,50 120,{200 - ordinates[1 if n==4 else 1]*9}" fill="#fbcfe8" fill-opacity="0.4" stroke="#db2777" stroke-dasharray="3,3"/>
  <text x="180" y="40" font-size="12" fill="#2563eb" font-weight="bold" font-family="sans-serif">y = x²</text>
  <text x="140" y="160" font-size="11" fill="#db2777" font-weight="bold" font-family="sans-serif">Trapezoidal Strips</text>
</svg>"""

    prompt = (
        f"Consider the area bounded by the curve $y = x^2$, the $x$-axis, and the ordinate $x = {b}$.\n\n"
        f"1. Estimate the area using the Trapezoidal Rule with $n = {n}$ equal intervals ($h = {_fmt_sa(h)}$).\n"
        f"2. Calculate the exact area using the definite integral $\\int_{{0}}^{{{b}}} x^2 \\, dx$.\n"
        f"3. Calculate the percentage error of the trapezoidal approximation compared to the exact integral."
    )

    ord_str = ", ".join(f"y_{i} = {_fmt_sa(v)}" for i, v in enumerate(ordinates))
    ans_latex = (
        rf"1.\; \text{{Ordinates: }} {ord_str}\n"
        rf"\text{{Area}}_{{\text{{trap}}}} = {_fmt_katex(h)} \times \left( \frac{{{ordinates[0]} + {ordinates[-1]}}}{{2}} + {middle} \right) = {_fmt_katex(trap_area)}\text{{ units}}^2\n"
        rf"2.\; \text{{Area}}_{{\text{{exact}}}} = \int_{{0}}^{{{b}}} x^2 dx = \left[ \frac{{x^3}}{{3}} \right]_{{0}}^{{{b}}} = \frac{{{exact_num}}}{{{exact_den}}} \approx {_fmt_katex(exact_val)}\text{{ units}}^2\n"
        rf"3.\; \text{{Percentage Error}} = \frac{{{_fmt_katex(trap_area)} - {_fmt_katex(exact_val)}}}{{{_fmt_katex(exact_val)}}} \times 100\% = {_fmt_katex(pct_err)}\%"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Compute boundary and interior ordinates: {ord_str}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Apply trapezoidal rule to obtain {_fmt_sa(trap_area)}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Compute exact integral: {exact_num}/{exact_den} or {_fmt_sa(exact_val)}", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Calculate percentage error = {_fmt_sa(pct_err)}%", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_percentage_sign", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Apply the Trapezoidal Rule: $A \\approx h \\left( \\frac{y_0 + y_n}{2} + \\sum_{i=1}^{n-1} y_i \\right)$.",
        "tier_2": f"Find exact area: $\\int_0^{{{b}}} x^2 dx = \\frac{{{b}^3}}{{3}} = \\frac{{{exact_num}}}{{{exact_den}}} \\approx {_fmt_sa(exact_val)}$.",
        "tier_3": f"Percentage error is $\\frac{{\\text{{approx}} - \\text{{exact}}}}{{\\text{{exact}}}} \\times 100\\% = {_fmt_sa(pct_err)}\\%$.",
    }

    return {
        "id": f"tech_calc_synthesis_{r.randint(100000, 999999)}",
        "question_id": f"tech_calc_synthesis_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "50_technical_calculus_mensuration_synthesis",
        "learning_objective_id": "techmath_calc_mensuration_synthesis",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
            "blender_plate": "/diagrams/blender_3d_cone_textbook.jpg",
            "model_glb": "/models/blender_3d_cone.glb",
        },
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_trapezoidal_with_mid_ordinate", "divided_percentage_error_by_approx", "power_rule_arithmetic_error"],
        "keywords": ["trapezoidal rule", "definite integral", "percentage error", "calculus synthesis"],
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 7,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Export dictionary of builders 39-50
BUILDERS_39_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "39_area_between_parabola_and_horizontal_line": _b39_area_parabola_horizontal_line,
    "40_area_between_parabola_and_linear_line": _b40_area_parabola_linear_line,
    "41_area_between_two_intersecting_parabolas": _b41_area_two_intersecting_parabolas,
    "42_volume_solid_of_revolution_cylindrical_disc": _b42_volume_solid_of_revolution_cylindrical_disc,
    "43_volume_solid_of_revolution_linear_cone": _b43_volume_solid_of_revolution_linear_cone,
    "44_volume_solid_of_revolution_paraboloid": _b44_volume_solid_of_revolution_paraboloid,
    "45_volume_solid_of_revolution_polynomial_spindle": _b45_volume_solid_of_revolution_polynomial_spindle,
    "46_volume_solid_of_revolution_washer_method": _b46_volume_solid_of_revolution_washer_method,
    "47_engineering_cross_section_piecewise_area": _b47_engineering_cross_section_piecewise_area,
    "48_engineering_work_done_expanding_gas": _b48_engineering_work_done_expanding_gas,
    "49_engineering_fluid_hydrostatic_force": _b49_engineering_fluid_hydrostatic_force,
    "50_technical_calculus_mensuration_synthesis": _b50_technical_calculus_mensuration_synthesis,
}
