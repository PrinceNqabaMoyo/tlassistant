"""Grade 12 Mathematics — Statistics Archetypes 01 to 25.
Grounded in curriculum_docs_auto/Mathematics_Gr12/Term 3/01. Statistics.md:
Univariate dispersion (variance & standard deviation), box-and-whisker skewness,
normal distribution empirical rule, cumulative frequency ogives, and curve fitting foundations.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Tuple
import sympy as sp

from app.utils.grade12_mathematics._math_common import (
    make_math_question,
    num,
    solution_graph,
    step,
)

TOPIC = "grade12_math_bivariate_statistics"
LO_PREFIX = "math12_statistics"


# ---------------------------------------------------------------------------
# SVG Builders (Surface 1: Static 2D Exam Figures)
# ---------------------------------------------------------------------------
def _box_whisker_svg(min_v: float, q1: float, q2: float, q3: float, max_v: float, label: str = "Dataset") -> Dict[str, Any]:
    w, h = 440, 160
    pad_l, pad_r = 45, 35
    span = max(max_v - min_v, 1.0)
    def sx(val: float) -> float:
        return pad_l + ((val - min_v) / span) * (w - pad_l - pad_r)

    x_min, x_q1, x_q2, x_q3, x_max = sx(min_v), sx(q1), sx(q2), sx(q3), sx(max_v)
    cy = 70
    box_h = 38
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect width="{w}" height="{h}" fill="#ffffff" rx="6"/>'
        f'<text x="{w/2:.1f}" y="22" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e293b">{label}</text>'
        f'<line x1="{pad_l}" y1="125" x2="{w - pad_r}" y2="125" stroke="#475569" stroke-width="1.5"/>'
        f'<line x1="{x_min:.1f}" y1="{cy}" x2="{x_q1:.1f}" y2="{cy}" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="{x_q3:.1f}" y1="{cy}" x2="{x_max:.1f}" y2="{cy}" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="{x_min:.1f}" y1="{cy - 12}" x2="{x_min:.1f}" y2="{cy + 12}" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="{x_max:.1f}" y1="{cy - 12}" x2="{x_max:.1f}" y2="{cy + 12}" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="{x_q1:.1f}" y="{cy - box_h/2:.1f}" width="{max(x_q3 - x_q1, 2.0):.1f}" height="{box_h}" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
        f'<line x1="{x_q2:.1f}" y1="{cy - box_h/2:.1f}" x2="{x_q2:.1f}" y2="{cy + box_h/2:.1f}" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="{x_min:.1f}" y="143" font-family="sans-serif" font-size="11" text-anchor="middle" fill="#0f172a">{min_v}</text>'
        f'<text x="{x_q1:.1f}" y="42" font-family="sans-serif" font-size="11" text-anchor="middle" fill="#0369a1">{q1}</text>'
        f'<text x="{x_q2:.1f}" y="143" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#dc2626">{q2}</text>'
        f'<text x="{x_q3:.1f}" y="42" font-family="sans-serif" font-size="11" text-anchor="middle" fill="#0369a1">{q3}</text>'
        f'<text x="{x_max:.1f}" y="143" font-family="sans-serif" font-size="11" text-anchor="middle" fill="#0f172a">{max_v}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _normal_bell_svg(mean_v: int, sd_v: int) -> Dict[str, Any]:
    w, h = 440, 200
    pts = []
    for i in range(61):
        z = -3.0 + i * 0.1
        px = 50 + ((z + 3.0) / 6.0) * 340
        py = 155 - 110 * math.exp(-0.5 * z * z)
        pts.append(f"{px:.1f},{py:.1f}")
    poly = " ".join(pts)
    ticks = []
    for k in range(-3, 4):
        tx = 50 + ((k + 3) / 6.0) * 340
        val = mean_v + k * sd_v
        ticks.append(
            f'<line x1="{tx:.1f}" y1="155" x2="{tx:.1f}" y2="161" stroke="#334155" stroke-width="1.5"/>'
            f'<text x="{tx:.1f}" y="176" font-family="sans-serif" font-size="11" text-anchor="middle" fill="#0f172a">{val}</text>'
        )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect width="{w}" height="{h}" fill="#ffffff" rx="6"/>'
        f'<text x="220" y="22" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e293b">Normal Distribution (mean = {mean_v}, sd = {sd_v})</text>'
        f'<line x1="35" y1="155" x2="405" y2="155" stroke="#334155" stroke-width="1.5"/>'
        f'<line x1="220" y1="45" x2="220" y2="155" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/>'
        f'<polyline fill="none" stroke="#0284c7" stroke-width="2.5" points="{poly}"/>'
        f'{"".join(ticks)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _ogive_svg(boundaries: List[int], cum_freqs: List[int], q1_val: int, q2_val: int, q3_val: int) -> Dict[str, Any]:
    w, h = 440, 240
    pad_l, pad_r, pad_t, pad_b = 50, 30, 30, 40
    min_x, max_x = boundaries[0], boundaries[-1]
    max_y = cum_freqs[-1]
    def sx(x: float) -> float:
        return pad_l + ((x - min_x) / max(max_x - min_x, 1)) * (w - pad_l - pad_r)
    def sy(y: float) -> float:
        return (h - pad_b) - (y / max(max_y, 1)) * (h - pad_t - pad_b)

    pts = " ".join(f"{sx(bx):.1f},{sy(cf):.1f}" for bx, cf in zip(boundaries, cum_freqs))
    dots = "".join(
        f'<circle cx="{sx(bx):.1f}" cy="{sy(cf):.1f}" r="3.5" fill="#0284c7"/>'
        f'<text x="{sx(bx):.1f}" y="{h - 20}" font-family="sans-serif" font-size="10" text-anchor="middle" fill="#334155">{bx}</text>'
        for bx, cf in zip(boundaries, cum_freqs)
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect width="{w}" height="{h}" fill="#ffffff" rx="6"/>'
        f'<text x="220" y="20" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e293b">Cumulative Frequency Ogive (N = {max_y})</text>'
        f'<line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{h - pad_b}" stroke="#334155" stroke-width="1.5"/>'
        f'<line x1="{pad_l}" y1="{h - pad_b}" x2="{w - pad_r}" y2="{h - pad_b}" stroke="#334155" stroke-width="1.5"/>'
        f'<polyline fill="none" stroke="#0284c7" stroke-width="2.2" points="{pts}"/>'
        f'{dots}'
        f'<text x="{pad_l - 8}" y="{sy(max_y) + 4:.1f}" font-family="sans-serif" font-size="10" text-anchor="end" fill="#334155">{max_y}</text>'
        f'<text x="{sx(q1_val):.1f}" y="{sy(max_y * 0.25) - 6:.1f}" font-family="sans-serif" font-size="10" fill="#dc2626">Q1={q1_val}</text>'
        f'<text x="{sx(q2_val):.1f}" y="{sy(max_y * 0.50) - 6:.1f}" font-family="sans-serif" font-size="10" fill="#dc2626">Q2={q2_val}</text>'
        f'<text x="{sx(q3_val):.1f}" y="{sy(max_y * 0.75) - 6:.1f}" font-family="sans-serif" font-size="10" fill="#dc2626">Q3={q3_val}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _histogram_svg(freqs: List[int], title: str) -> Dict[str, Any]:
    w, h = 420, 210
    pad_l, pad_b = 45, 35
    max_f = max(freqs) if freqs else 1
    bw = 320 / max(len(freqs), 1)
    bars = []
    for idx, f in enumerate(freqs):
        bh = (f / max_f) * 130
        bx = pad_l + idx * bw
        by = (h - pad_b) - bh
        bars.append(
            f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw - 2:.1f}" height="{bh:.1f}" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5"/>'
            f'<text x="{bx + bw/2:.1f}" y="{by - 4:.1f}" font-family="sans-serif" font-size="10" text-anchor="middle" fill="#0f172a">{f}</text>'
        )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect width="{w}" height="{h}" fill="#ffffff" rx="6"/>'
        f'<text x="210" y="20" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e293b">{title}</text>'
        f'<line x1="{pad_l}" y1="30" x2="{pad_l}" y2="{h - pad_b}" stroke="#334155" stroke-width="1.5"/>'
        f'<line x1="{pad_l}" y1="{h - pad_b}" x2="{w - 25}" y2="{h - pad_b}" stroke="#334155" stroke-width="1.5"/>'
        f'{"".join(bars)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _curve_scatter_svg(points: List[Tuple[float, float]], label: str) -> Dict[str, Any]:
    w, h = 420, 220
    pad_l, pad_r, pad_t, pad_b = 48, 28, 32, 36
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    def sx(x: float) -> float:
        return pad_l + ((x - min_x) / max(max_x - min_x, 1.0)) * (w - pad_l - pad_r)
    def sy(y: float) -> float:
        return (h - pad_b) - ((y - min_y) / max(max_y - min_y, 1.0)) * (h - pad_t - pad_b)

    dots = "".join(
        f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="4" fill="#0284c7"/>'
        f'<text x="{sx(x):.1f}" y="{sy(y) - 6:.1f}" font-family="sans-serif" font-size="9" text-anchor="middle" fill="#334155">({x};{y})</text>'
        for x, y in points
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect width="{w}" height="{h}" fill="#ffffff" rx="6"/>'
        f'<text x="210" y="20" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e293b">{label}</text>'
        f'<line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{h - pad_b}" stroke="#334155" stroke-width="1.5"/>'
        f'<line x1="{pad_l}" y1="{h - pad_b}" x2="{w - pad_r}" y2="{h - pad_b}" stroke="#334155" stroke-width="1.5"/>'
        f'{dots}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _make_q(
    subskill: str,
    prompt: str,
    prompt_latex: str,
    answer_latex: str,
    answer_sympy: str,
    sample_answer: str,
    marks: int = 3,
    difficulty: str = "medium",
    diagram_spec: Dict[str, Any] | None = None,
    nudge: str = "Identify the relevant statistical formula and substitute the given values.",
    concept: str = "Apply the Grade 12 statistics definitions for central tendency, dispersion, or regression.",
) -> Dict[str, Any]:
    steps = [
        step(from_latex=prompt_latex, to_latex_str=answer_latex, op=f"solve {subskill}", rule=subskill),
    ]
    canonical = solution_graph(goal=subskill, steps=steps, final_latex=answer_latex)
    marking_schema = {
        "total_marks": marks,
        "marking_points": [
            {"id": "mp1", "desc": "Formula selection and substitution", "marks": max(1, marks - 1), "editable": True},
            {"id": "mp2", "desc": f"Final answer: {answer_latex}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": nudge,
        "concept": concept,
        "breakdown": sample_answer,
    }
    return make_math_question(
        prefix=f"stat12_{subskill[:12]}",
        topic=TOPIC,
        subskill=subskill,
        learning_objective_id=f"{LO_PREFIX}_{subskill}",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        answer_sympy=answer_sympy,
        sample_answer=sample_answer,
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["arithmetic_slip_in_summation", "premature_rounding_error"],
        keywords=["statistics", subskill.replace("_", " ")],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=max(3, marks),
        mode=subskill,
        difficulty=difficulty,
        diagram_spec=diagram_spec,
    )


# ---------------------------------------------------------------------------
# Archetypes 01 to 25
# ---------------------------------------------------------------------------
def build_01_mean_of_ungrouped_data(r: random.Random) -> Dict[str, Any]:
    n = 6
    base = r.randint(12, 35)
    offsets = [-5, -2, 0, 1, 2, 4]
    r.shuffle(offsets)
    vals = [base + d for d in offsets]
    total = sum(vals)
    vals_str = "; ".join(str(v) for v in vals)
    return _make_q(
        "01_mean_of_ungrouped_data",
        f"Calculate the mean ($\\bar{{x}}$) of the following dataset of {n} observations:\n\n$$\\{{{vals_str}\\}}$$",
        rf"\bar{{x}} = \frac{{{total}}}{{{n}}}",
        str(base),
        str(base),
        f"Sum of values = {total}. Mean $\\bar{{x}} = \\frac{{{total}}}{{{n}}} = {base}$.",
        marks=2,
        difficulty="easy",
    )


def build_02_median_even_and_odd_datasets(r: random.Random) -> Dict[str, Any]:
    a = r.randint(10, 25)
    vals = [a, a + 2, a + 5, a + 6, a + 8, a + 11, a + 14, a + 17]
    med = sp.Rational(vals[3] + vals[4], 2)
    med_str = num(float(med), 1)
    vals_str = "; ".join(str(v) for v in vals)
    return _make_q(
        "02_median_even_and_odd_datasets",
        f"Determine the median ($Q_2$) of the ordered dataset of 8 values:\n\n$$\\{{{vals_str}\\}}$$",
        rf"Q_2 = \frac{{{vals[3]} + {vals[4]}}}{{2}}",
        med_str,
        str(float(med)),
        f"Location of $Q_2 = \\frac{{1}}{{2}}(8 - 1) + 1 = 4{{,}}5$. Median = $\\frac{{{vals[3]} + {vals[4]}}}{{2}} = {med_str}$.",
        marks=2,
        difficulty="easy",
    )


def build_03_quartiles_and_interquartile_range(r: random.Random) -> Dict[str, Any]:
    b = r.randint(10, 30)
    vals = [b, b + 3, b + 4, b + 7, b + 10, b + 12, b + 15, b + 18, b + 20, b + 23, b + 27]
    q1, q3 = vals[2], vals[8]
    iqr = q3 - q1
    vals_str = "; ".join(str(v) for v in vals)
    return _make_q(
        "03_quartiles_and_interquartile_range",
        f"For the ordered dataset of 11 values:\n\n$$\\{{{vals_str}\\}}$$\n\nDetermine the lower quartile ($Q_1$), upper quartile ($Q_3$), and interquartile range ($\\text{{IQR}}$).",
        rf"\text{{IQR}} = Q_3 - Q_1 = {q3} - {q1}",
        rf"Q_1 = {q1}; \quad Q_3 = {q3}; \quad \text{{IQR}} = {iqr}",
        str(iqr),
        f"$Q_1$ is at position 3 ($Q_1 = {q1}$), $Q_3$ is at position 9 ($Q_3 = {q3}$). $\\text{{IQR}} = {q3} - {q1} = {iqr}$.",
        marks=3,
    )


def build_04_five_number_summary_extraction(r: random.Random) -> Dict[str, Any]:
    s = r.randint(5, 20)
    vals = [s, s + 4, s + 6, s + 9, s + 12, s + 15, s + 19, s + 22, s + 28]
    min_v = vals[0]
    q1 = sp.Rational(vals[1] + vals[2], 2)
    q2 = vals[4]
    q3 = sp.Rational(vals[6] + vals[7], 2)
    max_v = vals[-1]
    ans = f"({min_v}; {num(float(q1), 1)}; {q2}; {num(float(q3), 1)}; {max_v})"
    vals_str = "; ".join(str(v) for v in vals)
    return _make_q(
        "04_five_number_summary_extraction",
        f"Write down the five-number summary $(\\text{{min}}; Q_1; Q_2; Q_3; \\text{{max}})$ for the dataset:\n\n$$\\{{{vals_str}\\}}$$",
        rf"\text{{Five-number summary for }} n = 9",
        ans,
        ans,
        f"Min = {min_v}, $Q_1 = {num(float(q1), 1)}$, Median $Q_2 = {q2}$, $Q_3 = {num(float(q3), 1)}$, Max = {max_v}.",
        marks=3,
    )


def build_05_box_and_whisker_diagram_reading(r: random.Random) -> Dict[str, Any]:
    min_v = r.randint(8, 18)
    q1 = min_v + r.randint(6, 10)
    q2 = q1 + r.randint(5, 9)
    q3 = q2 + r.randint(6, 11)
    max_v = q3 + r.randint(7, 12)
    iqr = q3 - q1
    rng_v = max_v - min_v
    d_spec = _box_whisker_svg(min_v, q1, q2, q3, max_v, f"Test Marks Summary ({min_v} to {max_v})")
    return _make_q(
        "05_box_and_whisker_diagram_reading",
        f"Refer to the box-and-whisker plot with minimum {min_v} and maximum {max_v}. Write down the median ($Q_2$), the interquartile range ($\\text{{IQR}}$), and the range of the data.",
        rf"Q_2 = {q2}, \quad \text{{IQR}} = {q3} - {q1}, \quad \text{{Range}} = {max_v} - {min_v}",
        rf"Q_2 = {q2}; \quad \text{{IQR}} = {iqr}; \quad \text{{Range}} = {rng_v}",
        f"Q2={q2}, IQR={iqr}, Range={rng_v}",
        f"From the box-and-whisker plot: $Q_2 = {q2}$, $\\text{{IQR}} = {q3} - {q1} = {iqr}$, and $\\text{{Range}} = {max_v} - {min_v} = {rng_v}$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_06_skewness_from_mean_minus_median(r: random.Random) -> Dict[str, Any]:
    is_pos = r.choice([True, False])
    med = r.randint(45, 68)
    delta = r.randint(5, 11)
    mean_v = med + delta if is_pos else med - delta
    diff = mean_v - med
    skew_str = "positively skewed (skewed right)" if is_pos else "negatively skewed (skewed left)"
    return _make_q(
        "06_skewness_from_mean_minus_median",
        f"A Grade 12 examination dataset has a mean of $\\bar{{x}} = {mean_v}$ and a median of $Q_2 = {med}$. Calculate $\\bar{{x}} - Q_2$ and state the skewness of the data.",
        rf"\bar{{x}} - Q_2 = {mean_v} - {med} = {diff}",
        rf"\bar{{x}} - Q_2 = {diff} \implies \text{{{skew_str}}}",
        skew_str,
        f"$\\bar{{x}} - Q_2 = {mean_v} - {med} = {diff}$. Since $\\bar{{x}} {'>' if is_pos else '<'} Q_2$, the distribution is {skew_str}.",
        marks=2,
        difficulty="easy",
    )


def build_07_skewness_from_box_and_whisker_tails(r: random.Random) -> Dict[str, Any]:
    skew_right = r.choice([True, False])
    min_v = r.randint(10, 20)
    if skew_right:
        q1 = min_v + 4
        q2 = q1 + 4
        q3 = q2 + 12
        max_v = q3 + 16
        skew_ans = "positively skewed (skewed right)"
        reason = f"Q3 - Q2 = {q3 - q2} > Q2 - Q1 = {q2 - q1} and the right whisker is longer"
    else:
        q1 = min_v + 16
        q2 = q1 + 12
        q3 = q2 + 4
        max_v = q3 + 4
        skew_ans = "negatively skewed (skewed left)"
        reason = f"Q2 - Q1 = {q2 - q1} > Q3 - Q2 = {q3 - q2} and the left whisker is longer"
    d_spec = _box_whisker_svg(min_v, q1, q2, q3, max_v, f"Distribution ({min_v} to {max_v})")
    return _make_q(
        "07_skewness_from_box_and_whisker_tails",
        f"Refer to the box-and-whisker plot with five-number summary $({min_v}; {q1}; {q2}; {q3}; {max_v})$. State whether the distribution is skewed left or skewed right, and justify your answer.",
        rf"Q_2 - Q_1 = {q2 - q1}, \quad Q_3 - Q_2 = {q3 - q2}",
        rf"\text{{{skew_ans}}} \text{{ ({reason})}}",
        skew_ans,
        f"The distribution is {skew_ans} because {reason}.",
        marks=2,
        diagram_spec=d_spec,
    )


def build_08_variance_from_deviation_table(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(15, 30)
    devs = [-4, -2, 0, 2, 4]
    vals = [mean_v + d for d in devs]
    sq_sum = sum(d * d for d in devs)
    var_v = sq_sum / 5.0
    var_str = num(var_v, 1)
    vals_str = "; ".join(str(v) for v in vals)
    return _make_q(
        "08_variance_from_deviation_table",
        f"Consider the population dataset of 5 values with mean $\\bar{{x}} = {mean_v}$:\n\n$$\\{{{vals_str}\\}}$$\n\nCalculate $\\sum_{{i=1}}^{{5}} (x_i - \\bar{{x}})^2$ and the population variance $\\sigma^2$.",
        rf"\sigma^2 = \frac{{\sum (x_i - {mean_v})^2}}{{5}} = \frac{{{sq_sum}}}{{5}}",
        rf"\sum(x_i - \bar{{x}})^2 = {sq_sum}; \quad \sigma^2 = {var_str}",
        var_str,
        f"Squared deviations: $16 + 4 + 0 + 4 + 16 = {sq_sum}$. Variance $\\sigma^2 = \\frac{{{sq_sum}}}{{5}} = {var_str}$.",
        marks=3,
    )


def build_09_standard_deviation_calculation(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(20, 45)
    k = r.choice([2, 3, 4, 5])
    devs = [-2 * k, -k, 0, k, 2 * k]
    vals = [mean_v + d for d in devs]
    sq_sum = sum(d * d for d in devs)
    var_v = sq_sum / 5.0
    sd_v = math.sqrt(var_v)
    sd_str = num(round(sd_v, 2), 2)
    vals_str = "; ".join(str(v) for v in vals)
    return _make_q(
        "09_standard_deviation_calculation",
        f"Calculate the population standard deviation ($\\sigma$) of the dataset:\n\n$$\\{{{vals_str}\\}}$$\n\nRound your answer to two decimal places.",
        rf"\sigma = \sqrt{{\frac{{{sq_sum}}}{{5}}}}",
        rf"\sigma = {sd_str}",
        sd_str,
        f"Mean $\\bar{{x}} = {mean_v}$, $\\sum(x_i - \\bar{{x}})^2 = {sq_sum}$, so $\\sigma = \\sqrt{{\\frac{{{sq_sum}}}{{5}}}} \\approx {sd_str}$.",
        marks=3,
    )


def build_10_one_standard_deviation_interval_bounds(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(50, 78)
    sd_v = r.randint(6, 14)
    lo, hi = mean_v - sd_v, mean_v + sd_v
    return _make_q(
        "10_one_standard_deviation_interval_bounds",
        f"A dataset of mass measurements (in kg) has a mean of $\\bar{{x}} = {mean_v}\\text{{ kg}}$ and a standard deviation of $\\sigma = {sd_v}\\text{{ kg}}$. Determine the interval $(\\bar{{x}} - \\sigma; \\bar{{x}} + \\sigma)$ of values within one standard deviation of the mean.",
        rf"(\bar{{x}} - \sigma; \bar{{x}} + \sigma) = ({mean_v} - {sd_v}; {mean_v} + {sd_v})",
        rf"({lo}; {hi})",
        f"({lo}, {hi})",
        f"Lower bound $= {mean_v} - {sd_v} = {lo}$. Upper bound $= {mean_v} + {sd_v} = {hi}$. Interval: $({lo}; {hi})$.",
        marks=2,
        difficulty="easy",
    )


def build_11_count_within_one_standard_deviation(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(40, 60)
    sd_v = 5
    vals = [mean_v - 9, mean_v - 6, mean_v - 4, mean_v - 2, mean_v, mean_v + 1, mean_v + 3, mean_v + 7]
    lo, hi = mean_v - sd_v, mean_v + sd_v
    inside = [v for v in vals if lo <= v <= hi]
    vals_str = "; ".join(str(v) for v in vals)
    return _make_q(
        "11_count_within_one_standard_deviation",
        f"A dataset of 8 observations has mean $\\bar{{x}} = {mean_v}$ and standard deviation $\\sigma = {sd_v}$:\n\n$$\\{{{vals_str}\\}}$$\n\nHow many observations lie within one standard deviation of the mean?",
        rf"[{mean_v - sd_v}; {mean_v + sd_v}] = [{lo}; {hi}]",
        f"{len(inside)} observations",
        str(len(inside)),
        f"One standard deviation interval is $[{lo}; {hi}]$. The values inside are $\\{{{'; '.join(str(v) for v in inside)}\\}}$, giving {len(inside)} observations.",
        marks=3,
    )


def build_12_percentage_outside_k_standard_deviations(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(50, 75)
    sd_v = r.randint(4, 8)
    vals = [
        mean_v - sd_v - 3,
        mean_v - sd_v - 1,
        mean_v - 2,
        mean_v - 1,
        mean_v,
        mean_v + 1,
        mean_v + 2,
        mean_v + sd_v + 2,
    ]
    lo, hi = mean_v - sd_v, mean_v + sd_v
    outside = [v for v in vals if v < lo or v > hi]
    pct = (len(outside) / 8.0) * 100.0
    pct_str = num(pct, 1)
    vals_str = "; ".join(str(v) for v in vals)
    return _make_q(
        "12_percentage_outside_k_standard_deviations",
        f"Eight athletes recorded times with mean $\\bar{{x}} = {mean_v}\\text{{ s}}$ and standard deviation $\\sigma = {sd_v}\\text{{ s}}$:\n\n$$\\{{{vals_str}\\}}$$\n\nCalculate the percentage of athletes whose times lie more than one standard deviation away from the mean.",
        rf"\text{{Outside }} [{lo}; {hi}] \implies \frac{{{len(outside)}}}{{8}} \times 100\%",
        rf"{pct_str}\%",
        pct_str,
        f"Interval is $[{lo}; {hi}]$. Exactly {len(outside)} values ({', '.join(str(v) for v in outside)}) lie outside, which is $\\frac{{{len(outside)}}}{{8}} \\times 100\\% = {pct_str}\\%$.",
        marks=3,
    )


def build_13_normal_distribution_empirical_rule_68_95_99(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(120, 160)
    sd_v = r.randint(8, 15)
    lo = mean_v - 2 * sd_v
    hi = mean_v + sd_v
    d_spec = _normal_bell_svg(mean_v, sd_v)
    return _make_q(
        "13_normal_distribution_empirical_rule_68_95_99",
        f"Refer to the normal distribution curve with mean $\\bar{{x}} = {mean_v}$ and standard deviation $\\sigma = {sd_v}$ (where $68\\%$ lies within $1\\sigma$ and $95\\%$ within $2\\sigma$). Calculate the percentage of values that lie between {lo} and {hi}.",
        rf"[{mean_v} - 2({sd_v}); {mean_v} + {sd_v}] = [{lo}; {hi}]",
        r"81{,}5\%",
        "81.5",
        f"From ${lo} = \\bar{{x}} - 2\\sigma$ to ${mean_v} = \\bar{{x}}$ is $\\frac{{95\\%}}{{2}} = 47{{,}}5\\%$. From ${mean_v}$ to ${hi} = \\bar{{x}} + \\sigma$ is $\\frac{{68\\%}}{{2}} = 34\\%$. Total $= 47{{,}}5\\% + 34\\% = 81{{,}}5\\%$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_14_missing_value_from_known_mean(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(18, 34)
    known = [mean_v - 5, mean_v - 2, mean_v + 1, mean_v + 4, mean_v - 3]
    x_ans = 6 * mean_v - sum(known)
    known_str = "; ".join(str(v) for v in known)
    return _make_q(
        "14_missing_value_from_known_mean",
        f"The dataset $\\{{{known_str}; k\\}}$ consists of 6 values and has a mean of $\\bar{{x}} = {mean_v}$. Calculate the value of $k$.",
        rf"\frac{{{sum(known)} + k}}{{6}} = {mean_v}",
        rf"k = {x_ans}",
        str(x_ans),
        f"Sum of all 6 values $= 6 \\times {mean_v} = {6 * mean_v}$. Known sum $= {sum(known)}$, so $k = {6 * mean_v} - {sum(known)} = {x_ans}$.",
        marks=2,
        difficulty="easy",
    )


def build_15_two_missing_values_from_mean_and_variance(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(12, 24)
    d = r.randint(3, 6)
    a_val, b_val = mean_v - d, mean_v + d
    known = [mean_v - 2, mean_v, mean_v + 2]
    sq_sum = 4 + 0 + 4 + d * d + d * d
    var_v = sq_sum / 5.0
    var_str = num(var_v, 1)
    known_str = "; ".join(str(v) for v in known)
    return _make_q(
        "15_two_missing_values_from_mean_and_variance",
        f"A dataset of 5 numbers $\\{{{known_str}; a; b\\}}$ with $a < b$ has a mean of $\\bar{{x}} = {mean_v}$ and a population variance of $\\sigma^2 = {var_str}$. Calculate the values of $a$ and $b$.",
        rf"a + b = {2 * mean_v}, \quad (a - {mean_v})^2 + (b - {mean_v})^2 = {2 * d * d}",
        rf"a = {a_val}; \quad b = {b_val}",
        f"a={a_val}, b={b_val}",
        f"From the mean, $a + b = 5({mean_v}) - {sum(known)} = {2 * mean_v}$. From the variance, $(a-{mean_v})^2 + (b-{mean_v})^2 = {sq_sum} - 8 = {2 * d * d}$. Solving with $a < b$ gives $a = {a_val}$ and $b = {b_val}$.",
        marks=4,
        difficulty="hard",
    )


def build_16_effect_of_adding_constant_on_mean_and_sd(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(45, 65)
    sd_v = r.randint(5, 11)
    c_val = r.randint(4, 12)
    new_mean = mean_v + c_val
    return _make_q(
        "16_effect_of_adding_constant_on_mean_and_sd",
        f"A class of learners had a mean mark of $\\bar{{x}} = {mean_v}$ and a standard deviation of $\\sigma = {sd_v}$. If every learner is awarded an extra {c_val} marks, write down the new mean and the new standard deviation.",
        rf"\bar{{x}}_{{\text{{new}}}} = {mean_v} + {c_val}, \quad \sigma_{{\text{{new}}}} = {sd_v}",
        rf"\bar{{x}}_{{\text{{new}}}} = {new_mean}; \quad \sigma_{{\text{{new}}}} = {sd_v}",
        f"mean={new_mean}, sd={sd_v}",
        f"Adding a constant shifts the mean by $+{c_val}$ to ${new_mean}$, while the spread (standard deviation) remains unchanged at $\\sigma = {sd_v}$.",
        marks=2,
        difficulty="easy",
    )


def build_17_effect_of_scaling_data_on_mean_and_sd(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(20, 35)
    sd_v = r.randint(3, 7)
    k = r.choice([2, 3, 4])
    return _make_q(
        "17_effect_of_scaling_data_on_mean_and_sd",
        f"A dataset has a mean of $\\bar{{x}} = {mean_v}$ and a standard deviation of $\\sigma = {sd_v}$. If every data value is multiplied by {k}, determine the new mean and the new standard deviation.",
        rf"\bar{{x}}_{{\text{{new}}}} = {k} \times {mean_v}, \quad \sigma_{{\text{{new}}}} = {k} \times {sd_v}",
        rf"\bar{{x}}_{{\text{{new}}}} = {k * mean_v}; \quad \sigma_{{\text{{new}}}} = {k * sd_v}",
        f"mean={k*mean_v}, sd={k*sd_v}",
        f"Multiplying every observation by ${k}$ scales both the mean and the standard deviation by ${k}$: $\\bar{{x}}_{{\\text{{new}}}} = {k * mean_v}$ and $\\sigma_{{\\text{{new}}}} = {k * sd_v}$.",
        marks=2,
        difficulty="easy",
    )


def build_18_comparing_consistency_two_datasets_via_sd(r: random.Random) -> Dict[str, Any]:
    m_v = r.randint(15, 25)
    sd_a = round(r.uniform(1.2, 2.1), 2)
    sd_b = round(sd_a + r.uniform(1.1, 2.3), 2)
    sda_s, sdb_s = num(sd_a, 2), num(sd_b, 2)
    return _make_q(
        "18_comparing_consistency_two_datasets_via_sd",
        f"Two bread suppliers, Supplier A and Supplier B, both have a mean loaf price of $\\text{{R}}{m_v}{{,}}00$. Supplier A has a standard deviation of $\\sigma_A = \\text{{R}}{sda_s}$ and Supplier B has $\\sigma_B = \\text{{R}}{sdb_s}$. State which supplier has more consistent prices and give a mathematical reason.",
        rf"\sigma_A = {sda_s} < \sigma_B = {sdb_s}",
        rf"\text{{Supplier A, because }} \sigma_A = {sda_s} < \sigma_B = {sdb_s}",
        "Supplier A",
        f"Supplier A is more consistent because its standard deviation ($\\sigma_A = {sda_s}$) is smaller than Supplier B's ($\\sigma_B = {sdb_s}$), indicating less spread around the mean.",
        marks=2,
        difficulty="easy",
    )


def build_19_grouped_data_estimated_mean(r: random.Random) -> Dict[str, Any]:
    f1, f2, f3 = r.randint(4, 8), r.randint(7, 12), r.randint(3, 9)
    n = f1 + f2 + f3
    tot = f1 * 5 + f2 * 15 + f3 * 25
    est_m = round(tot / n, 2)
    est_s = num(est_m, 2)
    return _make_q(
        "19_grouped_data_estimated_mean",
        f"A grouped frequency table has three class intervals:\n\n"
        f"| Interval | $0 \\le x < 10$ | $10 \\le x < 20$ | $20 \\le x < 30$ |\n"
        f"|---|---|---|---|\n"
        f"| Frequency ($f_i$) | {f1} | {f2} | {f3} |\n\n"
        f"Calculate the estimated mean ($\\bar{{x}}$) rounded to two decimal places.",
        rf"\bar{{x}} = \frac{{{f1}(5) + {f2}(15) + {f3}(25)}}{{{n}}} = \frac{{{tot}}}{{{n}}}",
        est_s,
        est_s,
        f"Midpoints are 5, 15, and 25. $\\sum f_i m_i = {tot}$ and $n = {n}$. Estimated mean $\\bar{{x}} = \\frac{{{tot}}}{{{n}}} \\approx {est_s}$.",
        marks=3,
    )


def build_20_cumulative_frequency_table_completion(r: random.Random) -> Dict[str, Any]:
    f1, f2, f3, f4 = r.randint(5, 9), r.randint(10, 16), r.randint(12, 18), r.randint(4, 8)
    c1, c2, c3, c4 = f1, f1 + f2, f1 + f2 + f3, f1 + f2 + f3 + f4
    return _make_q(
        "20_cumulative_frequency_table_completion",
        f"Four consecutive class intervals have frequencies $f_1 = {f1}$, $f_2 = {f2}$, $f_3 = {f3}$, and $f_4 = {f4}$. Write down the four cumulative frequencies $(CF_1; CF_2; CF_3; CF_4)$.",
        rf"CF = ({c1}; {c2}; {c3}; {c4})",
        rf"({c1}; {c2}; {c3}; {c4})",
        f"({c1}, {c2}, {c3}, {c4})",
        f"Cumulative frequencies are obtained by successive addition: $CF_1 = {c1}$, $CF_2 = {c1} + {f2} = {c2}$, $CF_3 = {c2} + {f3} = {c3}$, $CF_4 = {c3} + {f4} = {c4}$.",
        marks=2,
        difficulty="easy",
    )


def build_21_ogive_median_and_quartiles_reading(r: random.Random) -> Dict[str, Any]:
    n_tot = r.choice([40, 60, 80, 100])
    q1_v = r.randint(22, 34)
    q2_v = q1_v + r.randint(12, 18)
    q3_v = q2_v + r.randint(12, 18)
    iqr = q3_v - q1_v
    bounds = [0, 20, 40, 60, 80, 100]
    cfs = [0, int(n_tot * 0.2), int(n_tot * 0.45), int(n_tot * 0.75), int(n_tot * 0.92), n_tot]
    d_spec = _ogive_svg(bounds, cfs, q1_v, q2_v, q3_v)
    return _make_q(
        "21_ogive_median_and_quartiles_reading",
        f"Refer to the cumulative frequency ogive for $N = {n_tot}$ learners, where the quartile readings on the horizontal axis are $Q_1 = {q1_v}$, $Q_2 = {q2_v}$, and $Q_3 = {q3_v}$. Write down the median mark and calculate the interquartile range ($\\text{{IQR}}$).",
        rf"Q_2 = {q2_v}, \quad \text{{IQR}} = {q3_v} - {q1_v}",
        rf"\text{{Median}} = {q2_v}; \quad \text{{IQR}} = {iqr}",
        f"Median={q2_v}, IQR={iqr}",
        f"At $\\frac{{N}}{{2}} = {n_tot // 2}$, the median is $Q_2 = {q2_v}$. The interquartile range is $\\text{{IQR}} = Q_3 - Q_1 = {q3_v} - {q1_v} = {iqr}$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_22_ogive_percentile_and_threshold_count(r: random.Random) -> Dict[str, Any]:
    n_tot = r.choice([60, 80, 100, 120])
    cf_at_60 = r.randint(int(n_tot * 0.55), int(n_tot * 0.80))
    above_60 = n_tot - cf_at_60
    bounds = [0, 20, 40, 60, 80, 100]
    cfs = [0, int(n_tot * 0.15), int(n_tot * 0.40), cf_at_60, int(n_tot * 0.90), n_tot]
    d_spec = _ogive_svg(bounds, cfs, 35, 52, 68)
    return _make_q(
        "22_ogive_percentile_and_threshold_count",
        f"Refer to the cumulative frequency ogive for $N = {n_tot}$ learners. Given that the cumulative frequency at a mark of $60$ is {cf_at_60}, determine how many learners scored strictly more than $60$ marks.",
        rf"N - CF(60) = {n_tot} - {cf_at_60}",
        f"{above_60} learners",
        str(above_60),
        f"Total learners $N = {n_tot}$ and $CF(60) = {cf_at_60}$ scored $60$ or less. Thus ${n_tot} - {cf_at_60} = {above_60}$ learners scored more than $60$.",
        marks=2,
        diagram_spec=d_spec,
    )


def build_23_histogram_and_frequency_polygon_skewness(r: random.Random) -> Dict[str, Any]:
    peak = r.randint(18, 28)
    freqs = [peak - 4, peak, peak - 5, peak - 9, peak - 12, peak - 15]
    tot = sum(freqs)
    d_spec = _histogram_svg(freqs, f"Histogram of {tot} Observations")
    return _make_q(
        "23_histogram_and_frequency_polygon_skewness",
        f"Refer to the histogram with class frequencies {', '.join(str(f) for f in freqs)} (total $N = {tot}$). State whether the distribution is positively skewed (skewed right) or negatively skewed (skewed left).",
        rf"\text{{Tail extends to the right from peak }} {peak}",
        r"\text{Positively skewed (skewed right)}",
        "positively skewed",
        f"The modal peak ({peak}) is on the left and the tail extends toward the higher intervals on the right, so the distribution is positively skewed (skewed right).",
        marks=2,
        diagram_spec=d_spec,
    )


def build_24_curve_fitting_model_identification(r: random.Random) -> Dict[str, Any]:
    k = r.randint(2, 5)
    pts = [(1, k), (2, 2 * k), (3, 4 * k), (4, 8 * k), (5, 16 * k)]
    d_spec = _curve_scatter_svg(pts, f"Bacterial Growth Curve (initial = {k})")
    return _make_q(
        "24_curve_fitting_model_identification",
        f"Refer to the scatter plot of points $(1; {k}), (2; {2*k}), (3; {4*k}), (4; {8*k}), (5; {16*k})$. Identify which type of function (linear, quadratic, or exponential) best fits the data.",
        rf"y = {k} \cdot 2^{{x-1}}",
        r"\text{Exponential function}",
        "exponential",
        f"Because the $y$-values double for each unit increase in $x$ (${k}, {2*k}, {4*k}, {8*k}, {16*k}$), an exponential function best fits the data.",
        marks=2,
        diagram_spec=d_spec,
    )


def build_25_quadratic_and_exponential_curve_fitting_prediction(r: random.Random) -> Dict[str, Any]:
    x_opt = r.randint(16, 22)
    y_max = r.randint(40, 65)
    c_val = y_max - x_opt * x_opt
    return _make_q(
        "25_quadratic_and_exponential_curve_fitting_prediction",
        f"An agricultural researcher models crop yield $y$ (in tonnes/ha) as a quadratic function of average summer temperature $x$ (in °C): $$y = -(x - {x_opt})^2 + {y_max}$$ Write down the optimal temperature $x$ that maximises crop yield and the maximum yield $y$.",
        rf"y = -(x - {x_opt})^2 + {y_max}",
        rf"x = {x_opt}^\circ\text{{C}}; \quad y_{{\max}} = {y_max}\text{{ tonnes/ha}}",
        f"x={x_opt}, y={y_max}",
        f"From vertex form $y = -(x - {x_opt})^2 + {y_max}$ with constant term ${c_val}$, the maximum occurs at $x = {x_opt}^\\circ\\text{{C}}$ with maximum yield $y = {y_max}\\text{{ tonnes/ha}}$.",
        marks=2,
    )


ARCHETYPES_01_25: Dict[str, Any] = {
    "01_mean_of_ungrouped_data": build_01_mean_of_ungrouped_data,
    "02_median_even_and_odd_datasets": build_02_median_even_and_odd_datasets,
    "03_quartiles_and_interquartile_range": build_03_quartiles_and_interquartile_range,
    "04_five_number_summary_extraction": build_04_five_number_summary_extraction,
    "05_box_and_whisker_diagram_reading": build_05_box_and_whisker_diagram_reading,
    "06_skewness_from_mean_minus_median": build_06_skewness_from_mean_minus_median,
    "07_skewness_from_box_and_whisker_tails": build_07_skewness_from_box_and_whisker_tails,
    "08_variance_from_deviation_table": build_08_variance_from_deviation_table,
    "09_standard_deviation_calculation": build_09_standard_deviation_calculation,
    "10_one_standard_deviation_interval_bounds": build_10_one_standard_deviation_interval_bounds,
    "11_count_within_one_standard_deviation": build_11_count_within_one_standard_deviation,
    "12_percentage_outside_k_standard_deviations": build_12_percentage_outside_k_standard_deviations,
    "13_normal_distribution_empirical_rule_68_95_99": build_13_normal_distribution_empirical_rule_68_95_99,
    "14_missing_value_from_known_mean": build_14_missing_value_from_known_mean,
    "15_two_missing_values_from_mean_and_variance": build_15_two_missing_values_from_mean_and_variance,
    "16_effect_of_adding_constant_on_mean_and_sd": build_16_effect_of_adding_constant_on_mean_and_sd,
    "17_effect_of_scaling_data_on_mean_and_sd": build_17_effect_of_scaling_data_on_mean_and_sd,
    "18_comparing_consistency_two_datasets_via_sd": build_18_comparing_consistency_two_datasets_via_sd,
    "19_grouped_data_estimated_mean": build_19_grouped_data_estimated_mean,
    "20_cumulative_frequency_table_completion": build_20_cumulative_frequency_table_completion,
    "21_ogive_median_and_quartiles_reading": build_21_ogive_median_and_quartiles_reading,
    "22_ogive_percentile_and_threshold_count": build_22_ogive_percentile_and_threshold_count,
    "23_histogram_and_frequency_polygon_skewness": build_23_histogram_and_frequency_polygon_skewness,
    "24_curve_fitting_model_identification": build_24_curve_fitting_model_identification,
    "25_quadratic_and_exponential_curve_fitting_prediction": build_25_quadratic_and_exponential_curve_fitting_prediction,
}
