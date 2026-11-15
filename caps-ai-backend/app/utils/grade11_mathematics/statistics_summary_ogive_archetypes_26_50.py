"""Grade 11 Mathematics — Term 4 — Statistics Archetypes 26–50.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 4: Chapter 10 Statistics).
Covers:
- Deviations from the mean, Population Variance (sigma^2), and Standard Deviation (sigma)
- One and two standard deviation intervals (x_bar ± sigma, x_bar ± 2*sigma) and percentage within 1 SD
- Comparing consistency using standard deviation
- Grouped frequency tables: class midpoints, estimated mean, modal class, median class
- Cumulative frequency tables: forward accumulation and backward recovery of individual frequencies
- Ogive (cumulative frequency) curves (inline_svg): grounding point, reading N, estimating median, Q1, Q3, IQR, percentiles, and counts above a threshold
- Histograms and Frequency Polygons (inline_svg): reading frequencies, midpoints, and identifying skewness
- Linear transformation of summary statistics (y = ax + b) and diagnostic misconception autopsy.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.grade11_mathematics._math_common import (
    make_math_question,
    num,
    solution_graph,
    step,
)

TOPIC = "Statistics"
LO_PREFIX = "math11_stats"


def _ogive_svg(
    bounds: List[int],
    cum_freqs: List[int],
    title: str = "Cumulative Frequency Curve (Ogive)",
    x_label: str = "Value",
    highlight_cf: Optional[float] = None,
    highlight_x: Optional[float] = None,
) -> Dict[str, Any]:
    """Generate a dynamic inline SVG of an Ogive (cumulative frequency curve) grounded at (bounds[0], 0)."""
    # bounds has length k+1, cum_freqs has length k+1 with cum_freqs[0] = 0
    x_min, x_max = bounds[0], bounds[-1]
    y_max = max(cum_freqs[-1], 1)

    def tx(x: float) -> float:
        return 65.0 + ((x - x_min) / max(x_max - x_min, 1.0)) * 335.0

    def ty(y: float) -> float:
        return 210.0 - (y / y_max) * 165.0

    pts = [(tx(b), ty(cf)) for b, cf in zip(bounds, cum_freqs)]
    poly_pts = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)

    grid_and_labels = []
    for b, cf in zip(bounds, cum_freqs):
        px, py = tx(b), ty(cf)
        grid_and_labels.append(
            f'<line x1="{px:.1f}" y1="45" x2="{px:.1f}" y2="210" stroke="#e2e8f0" stroke-width="1"/>'
            f'<text x="{px:.1f}" y="226" font-size="10" fill="#334155" text-anchor="middle">{b}</text>'
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="#1d4ed8"/>'
            f'<text x="{px - 6:.1f}" y="{py - 7:.1f}" font-size="10" font-weight="bold" fill="#1e293b">({b}; {cf})</text>'
        )

    for frac in [0.25, 0.5, 0.75, 1.0]:
        yv = round(y_max * frac)
        py = ty(yv)
        grid_and_labels.append(
            f'<line x1="65" y1="{py:.1f}" x2="400" y2="{py:.1f}" stroke="#e2e8f0" stroke-width="1"/>'
            f'<text x="58" y="{py + 4:.1f}" font-size="10" fill="#334155" text-anchor="end">{yv}</text>'
        )

    hl_svg = ""
    if highlight_cf is not None and highlight_x is not None:
        hx, hy = tx(highlight_x), ty(highlight_cf)
        hl_svg = (
            f'<line x1="65" y1="{hy:.1f}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="#dc2626" stroke-dasharray="4,3" stroke-width="1.8"/>'
            f'<line x1="{hx:.1f}" y1="{hy:.1f}" x2="{hx:.1f}" y2="210" stroke="#dc2626" stroke-dasharray="4,3" stroke-width="1.8"/>'
            f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="4.5" fill="#dc2626"/>'
        )

    svg = (
        f'<svg viewBox="0 0 440 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="250" fill="#f8fafc" rx="8"/>'
        f'<text x="230" y="22" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>'
        + "".join(grid_and_labels)
        + f'<line x1="65" y1="210" x2="410" y2="210" stroke="#475569" stroke-width="2"/>'
        f'<line x1="65" y1="210" x2="65" y2="38" stroke="#475569" stroke-width="2"/>'
        f'<polyline fill="none" stroke="#2563eb" stroke-width="2.6" points="{poly_pts}"/>'
        + hl_svg
        + f'<text x="235" y="244" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">{x_label}</text>'
        f'<text x="18" y="130" font-size="11" font-weight="bold" fill="#334155" transform="rotate(-90 18 130)" text-anchor="middle">Cumulative Freq</text>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "bounds": bounds,
        "cum_freqs": cum_freqs,
    }


def _histogram_svg(
    bounds: List[int],
    freqs: List[int],
    title: str = "Frequency Histogram",
    show_polygon: bool = False,
) -> Dict[str, Any]:
    """Generate a dynamic inline SVG of a Histogram (and optional Frequency Polygon)."""
    k = len(freqs)
    max_f = max(max(freqs), 1)
    bar_w = 300.0 / k

    bars_svg = []
    poly_pts = []
    for i, f in enumerate(freqs):
        x0 = 65.0 + i * bar_w
        h = (f / max_f) * 150.0
        y0 = 205.0 - h
        bars_svg.append(
            f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="1.8"/>'
            f'<text x="{x0 + bar_w/2:.1f}" y="{y0 - 6:.1f}" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{f}</text>'
            f'<text x="{x0:.1f}" y="222" font-size="10" fill="#334155" text-anchor="middle">{bounds[i]}</text>'
        )
        poly_pts.append((x0 + bar_w / 2.0, y0))

    bars_svg.append(
        f'<text x="{65.0 + k * bar_w:.1f}" y="222" font-size="10" fill="#334155" text-anchor="middle">{bounds[-1]}</text>'
    )

    poly_svg = ""
    if show_polygon:
        pts_str = " ".join(f"{px:.1f},{py:.1f}" for px, py in poly_pts)
        dots = "".join(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="#dc2626"/>' for px, py in poly_pts)
        poly_svg = f'<polyline fill="none" stroke="#dc2626" stroke-width="2.5" points="{pts_str}"/>' + dots

    svg = (
        f'<svg viewBox="0 0 430 240" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="240" fill="#f8fafc" rx="8"/>'
        f'<text x="215" y="24" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>'
        + "".join(bars_svg)
        + poly_svg
        + f'<line x1="55" y1="205" x2="385" y2="205" stroke="#334155" stroke-width="2"/>'
        f'<line x1="65" y1="205" x2="65" y2="40" stroke="#334155" stroke-width="2"/>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "bounds": bounds,
        "freqs": freqs,
    }


# 26. Deviations from mean sum to zero
def build_26_deviations_from_mean_sum_to_zero(r: random.Random) -> Dict[str, Any]:
    d1 = r.randint(-9, -3)
    d2 = r.randint(-5, -1)
    d3 = r.randint(2, 7)
    d4 = r.randint(1, 6)
    known_sum = d1 + d2 + d3 + d4
    d5 = -known_sum
    devs_str = f"{d1}; {d2}; {d3}; {d4}; d_5"

    prompt = (
        f"For a data set of $5$ observations, the deviations from the mean $(x_i - \\bar{{x}})$ are:\n"
        f"$$\\{{{devs_str}\\}}$$\n"
        f"Using the fundamental property of deviations from the mean, determine the value of $d_5$."
    )
    sol = solution_graph(
        goal="Find missing deviation using sum(x_i - x_bar) = 0",
        steps=[
            step(from_latex=r"\sum_{i=1}^{5} (x_i - \bar{x}) = 0", to_latex_str=rf"({known_sum}) + d_5 = 0", op="sum_deviations_zero", rule="The sum of deviations from the mean is always 0"),
            step(from_latex=rf"({known_sum}) + d_5 = 0", to_latex_str=f"d_5 = {d5}", op="solve_d5", rule="Isolate d_5"),
        ],
        final_latex=str(d5),
    )
    return make_math_question(
        prefix="stat11_26",
        topic=TOPIC,
        subskill="26_deviations_from_mean_sum_to_zero",
        learning_objective_id=f"{LO_PREFIX}_26",
        prompt=prompt,
        prompt_latex=r"\sum (x_i - \bar{x}) = 0",
        answer_latex=str(d5),
        answer_sympy=str(d5),
        sample_answer=f"d_5 = {d5}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": "Set sum of deviations equal to 0"}, {"mark": "A1", "criterion": f"d_5 = {d5}"}]},
        hints={"nudge": "What do the signed deviations (x_i - x_bar) always add up to?", "concept": r"$\sum (x_i - \bar{x}) = 0$", "breakdown": f"{known_sum} + d_5 = 0 => d_5 = {d5}"},
        misconception_tags=["forgot_deviations_sum_to_zero"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="26_deviations_from_mean_sum_to_zero",
        difficulty="easy",
    )


# 27. Variance calculation from ungrouped data
def build_27_variance_calculation_from_ungrouped_data(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(10, 25)
    k = r.choice([2, 3, 4, 5])
    # 5 values: [mean - 2k, mean - k, mean, mean + k, mean + 2k]
    # Squared deviations: 4k^2 + k^2 + 0 + k^2 + 4k^2 = 10k^2
    # Variance = 10k^2 / 5 = 2k^2
    data = [mean_v - 2 * k, mean_v - k, mean_v, mean_v + k, mean_v + 2 * k]
    sum_sq = 10 * (k ** 2)
    var_v = 2 * (k ** 2)
    data_str = "; ".join(str(x) for x in data)

    prompt = (
        f"Calculate the population **variance** ($\\sigma^2$) of the following $5$ data values:\n"
        f"$$\\{{{data_str}\\}}$$"
    )
    sol = solution_graph(
        goal=r"\text{Calculate variance } \sigma^2",
        steps=[
            step(from_latex=rf"\bar{{x}} = {mean_v}", to_latex_str=rf"\sum (x_i - \bar{{x}})^2 = {sum_sq}", op="sum_squared_devs", rule="Compute mean and sum of squared deviations"),
            step(from_latex=rf"\sigma^2 = \frac{{{sum_sq}}}{{5}}", to_latex_str=str(var_v), op="divide_by_n", rule="Divide by n = 5"),
        ],
        final_latex=str(var_v),
    )
    return make_math_question(
        prefix="stat11_27",
        topic=TOPIC,
        subskill="27_variance_calculation_from_ungrouped_data",
        learning_objective_id=f"{LO_PREFIX}_27",
        prompt=prompt,
        prompt_latex=rf"\sigma^2 \text{{ of }} \{{{data_str}\}}",
        answer_latex=str(var_v),
        answer_sympy=str(var_v),
        sample_answer=f"Variance = {var_v}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": f"Mean = {mean_v}"}, {"mark": "M1", "criterion": f"Sum of squared deviations = {sum_sq}"}, {"mark": "A1", "criterion": f"Variance = {var_v}"}]},
        hints={"nudge": f"First verify the mean is {mean_v}, then square each deviation from {mean_v}.", "concept": r"$\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{n}$", "breakdown": f"{sum_sq} / 5 = {var_v}"},
        misconception_tags=["took_square_root_when_asked_for_variance"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="27_variance_calculation_from_ungrouped_data",
        difficulty="medium",
    )


# 28. Standard deviation from ungrouped data
def build_28_standard_deviation_from_ungrouped_data(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(15, 35)
    k = r.choice([2, 3, 4, 6])
    # 4 values: [mean - k, mean - k, mean + k, mean + k] -> sum sq = 4k^2 -> var = k^2 -> sd = k
    data = [mean_v - k, mean_v - k, mean_v + k, mean_v + k]
    sum_sq = 4 * (k ** 2)
    var_v = k ** 2
    sd_v = k
    data_str = "; ".join(str(x) for x in data)

    prompt = (
        f"Calculate the population **standard deviation** ($\\sigma$) of the following $4$ data values:\n"
        f"$$\\{{{data_str}\\}}$$"
    )
    sol = solution_graph(
        goal=r"\text{Calculate standard deviation } \sigma",
        steps=[
            step(from_latex=rf"\bar{{x}} = {mean_v}", to_latex_str=rf"\sigma^2 = \frac{{{sum_sq}}}{{4}} = {var_v}", op="compute_variance", rule="Find mean and variance"),
            step(from_latex=rf"\sigma = \sqrt{{{var_v}}}", to_latex_str=str(sd_v), op="sqrt_variance", rule="Take positive square root of variance"),
        ],
        final_latex=str(sd_v),
    )
    return make_math_question(
        prefix="stat11_28",
        topic=TOPIC,
        subskill="28_standard_deviation_from_ungrouped_data",
        learning_objective_id=f"{LO_PREFIX}_28",
        prompt=prompt,
        prompt_latex=rf"\sigma \text{{ of }} \{{{data_str}\}}",
        answer_latex=str(sd_v),
        answer_sympy=str(sd_v),
        sample_answer=f"Standard deviation = {sd_v}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": f"Mean = {mean_v}"}, {"mark": "M1", "criterion": f"Variance = {var_v}"}, {"mark": "A1", "criterion": f"SD = {sd_v}"}]},
        hints={"nudge": f"Find the variance first, then take the square root.", "concept": r"$\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$", "breakdown": f"sqrt({var_v}) = {sd_v}"},
        misconception_tags=["forgot_square_root_for_standard_deviation"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="28_standard_deviation_from_ungrouped_data",
        difficulty="medium",
    )


# 29. Standard deviation from variance and vice versa
def build_29_standard_deviation_from_variance_and_vice_versa(r: random.Random) -> Dict[str, Any]:
    sd_val = r.choice([1.5, 2.4, 3.2, 4.5, 5.5, 6.4])
    var_val = round(sd_val ** 2, 2)
    sd_str = num(sd_val)
    var_str = num(var_val)

    prompt = (
        f"A data set has a variance of $\\sigma^2 = {var_str}$ and a second data set has a standard deviation of $\\sigma = {sd_str}$.\n\n"
        f"Determine:\n"
        f"1. The standard deviation ($\\sigma$) of the first data set.\n"
        f"2. The variance ($\\sigma^2$) of the second data set."
    )
    ans_str = f"\\sigma = {sd_str}, \\sigma^2 = {var_str}"
    sol = solution_graph(
        goal="Convert between variance and standard deviation",
        steps=[
            step(from_latex=rf"\sigma = \sqrt{{{var_str}}}", to_latex_str=sd_str, op="sqrt", rule="Standard deviation is the square root of variance"),
            step(from_latex=rf"\sigma^2 = ({sd_str})^2", to_latex_str=var_str, op="square", rule="Variance is the square of standard deviation"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_29",
        topic=TOPIC,
        subskill="29_standard_deviation_from_variance_and_vice_versa",
        learning_objective_id=f"{LO_PREFIX}_29",
        prompt=prompt,
        prompt_latex=rf"\sqrt{{{var_str}}} \text{{ and }} ({sd_str})^2",
        answer_latex=ans_str,
        answer_sympy=f"({sd_val}, {var_val})",
        sample_answer=f"1. SD = {sd_str}; 2. Variance = {var_str}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"SD = {sd_str}"}, {"mark": "A1", "criterion": f"Variance = {var_str}"}]},
        hints={"nudge": "Standard deviation is the square root of variance.", "concept": r"$\sigma = \sqrt{\sigma^2}$", "breakdown": ans_str},
        misconception_tags=["confused_square_and_square_root_for_variance"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="29_standard_deviation_from_variance_and_vice_versa",
        difficulty="easy",
    )


# 30. One standard deviation interval bounds
def build_30_one_standard_deviation_interval_bounds(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(45, 78)
    sd_v = r.choice([4.2, 5.6, 6.8, 7.4, 8.5, 9.2])
    lo_b = round(mean_v - sd_v, 1)
    hi_b = round(mean_v + sd_v, 1)
    lo_str = num(lo_b, 1)
    hi_str = num(hi_b, 1)
    sd_str = num(sd_v, 1)
    ans_str = f"({lo_str}; {hi_str})"

    prompt = (
        f"A sample of measurements has a mean of $\\bar{{x}} = {mean_v}$ and a standard deviation of $\\sigma = {sd_str}$.\n\n"
        f"Determine the **one standard deviation interval** $(\\bar{{x}} - \\sigma; \\bar{{x}} + \\sigma)$."
    )
    sol = solution_graph(
        goal=r"\text{Compute } (\bar{x} - \sigma; \bar{x} + \sigma)",
        steps=[
            step(from_latex=rf"\bar{{x}} - \sigma = {mean_v} - {sd_str}", to_latex_str=lo_str, op="lower_bound", rule="Subtract 1 SD from mean"),
            step(from_latex=rf"\bar{{x}} + \sigma = {mean_v} + {sd_str}", to_latex_str=hi_str, op="upper_bound", rule="Add 1 SD to mean"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_30",
        topic=TOPIC,
        subskill="30_one_standard_deviation_interval_bounds",
        learning_objective_id=f"{LO_PREFIX}_30",
        prompt=prompt,
        prompt_latex=r"(\bar{x} - \sigma; \bar{x} + \sigma)",
        answer_latex=ans_str,
        answer_sympy=f"({lo_b}, {hi_b})",
        sample_answer=f"({lo_str}; {hi_str})",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"Lower bound = {lo_str}"}, {"mark": "A1", "criterion": f"Upper bound = {hi_str}"}]},
        hints={"nudge": "Subtract sigma from the mean for the lower limit, and add sigma to the mean for the upper limit.", "concept": r"$(\bar{x} - \sigma; \bar{x} + \sigma)$", "breakdown": ans_str},
        misconception_tags=["added_variance_instead_of_sd"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="30_one_standard_deviation_interval_bounds",
        difficulty="easy",
    )


# 31. Count values within one standard deviation
def build_31_count_values_within_one_standard_deviation(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(40, 65)
    sd_v = r.randint(6, 10)
    lo_b = mean_v - sd_v
    hi_b = mean_v + sd_v
    # 8 values: 2 below lo_b, 5 inside, 1 above hi_b
    data = [
        lo_b - 5,
        lo_b - 2,
        lo_b + 1,
        mean_v - 2,
        mean_v,
        mean_v + 1,
        hi_b - 1,
        hi_b + 4,
    ]
    data_str = "; ".join(str(x) for x in data)
    count_in = 5

    prompt = (
        f"Consider the ordered data set of $8$ scores:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"Given that the mean is $\\bar{{x}} = {mean_v}$ and the standard deviation is $\\sigma = {sd_v}$, "
        f"determine how many scores lie **within one standard deviation** of the mean."
    )
    sol = solution_graph(
        goal="Count values in (x_bar - sigma; x_bar + sigma)",
        steps=[
            step(from_latex=rf"({mean_v} - {sd_v}; {mean_v} + {sd_v})", to_latex_str=rf"({lo_b}; {hi_b})", op="interval_bounds", rule="Determine 1 SD interval"),
            step(from_latex=rf"\{{{lo_b+1}; {mean_v-2}; {mean_v}; {mean_v+1}; {hi_b-1}\}}", to_latex_str=str(count_in), op="count_values", rule="Count data points strictly within interval"),
        ],
        final_latex=str(count_in),
    )
    return make_math_question(
        prefix="stat11_31",
        topic=TOPIC,
        subskill="31_count_values_within_one_standard_deviation",
        learning_objective_id=f"{LO_PREFIX}_31",
        prompt=prompt,
        prompt_latex=rf"\text{{Count in }} ({lo_b}; {hi_b})",
        answer_latex=str(count_in),
        answer_sympy=str(count_in),
        sample_answer=f"{count_in} scores (interval [{lo_b}; {hi_b}])",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": f"Interval ({lo_b}; {hi_b})"}, {"mark": "M1", "criterion": "Identify values in interval"}, {"mark": "A1", "criterion": f"{count_in} scores"}]},
        hints={"nudge": f"First compute the interval ({mean_v} - {sd_v}; {mean_v} + {sd_v}) = ({lo_b}; {hi_b}).", "concept": "Count how many values from the list fall between the lower and upper bounds.", "breakdown": f"There are {count_in} values in ({lo_b}; {hi_b})."},
        misconception_tags=["counted_values_outside_interval"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="31_count_values_within_one_standard_deviation",
        difficulty="medium",
    )


# 32. Percentage within one standard deviation
def build_32_percentage_within_one_standard_deviation(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(50, 75)
    sd_v = r.randint(5, 9)
    lo_b = mean_v - sd_v
    hi_b = mean_v + sd_v
    # 10 values: k_in inside
    k_in = r.choice([6, 7, 8])
    inside = [mean_v - 2 + (i % 5) for i in range(k_in)]
    outside = [lo_b - 6, hi_b + 5, hi_b + 9, lo_b - 3][: (10 - k_in)]
    data = sorted(inside + outside)
    data_str = "; ".join(str(x) for x in data)
    pct = k_in * 10

    prompt = (
        f"Ten learners achieved the following marks:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"Using $\\bar{{x}} = {mean_v}$ and $\\sigma = {sd_v}$, calculate the **percentage** of learners whose marks "
        f"lie within one standard deviation of the mean."
    )
    sol = solution_graph(
        goal="Calculate percentage within 1 SD of mean",
        steps=[
            step(from_latex=rf"(\bar{{x}} - \sigma; \bar{{x}} + \sigma) = ({lo_b}; {hi_b})", to_latex_str=rf"\text{{Count}} = {k_in} \text{{ out of }} 10", op="count_in_interval", rule="Count values inside 1 SD interval"),
            step(from_latex=rf"\frac{{{k_in}}}{{10}} \times 100\%", to_latex_str=f"{pct}\\%", op="to_percentage", rule="Convert fraction to percentage"),
        ],
        final_latex=f"{pct}\\%",
    )
    return make_math_question(
        prefix="stat11_32",
        topic=TOPIC,
        subskill="32_percentage_within_one_standard_deviation",
        learning_objective_id=f"{LO_PREFIX}_32",
        prompt=prompt,
        prompt_latex=rf"\frac{{\text{{Count in }} ({lo_b}; {hi_b})}}{{10}} \times 100\%",
        answer_latex=f"{pct}\\%",
        answer_sympy=str(pct),
        sample_answer=f"{pct}% ({k_in} out of 10 learners)",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": f"Interval ({lo_b}; {hi_b})"}, {"mark": "M1", "criterion": f"Count = {k_in}/10"}, {"mark": "A1", "criterion": f"{pct}%"}]},
        hints={"nudge": f"Count how many of the 10 numbers lie between {lo_b} and {hi_b}, then multiply by 10%.", "concept": r"$\text{Percentage} = \frac{\text{count}}{n} \times 100\%$", "breakdown": f"{k_in}/10 * 100% = {pct}%"},
        misconception_tags=["reported_raw_count_instead_of_percentage"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="32_percentage_within_one_standard_deviation",
        difficulty="medium",
    )


# 33. Two standard deviation interval and outlier check
def build_33_two_standard_deviation_interval_and_outlier_check(r: random.Random) -> Dict[str, Any]:
    mean_v = r.randint(60, 85)
    sd_v = r.randint(4, 8)
    lo_2sd = mean_v - 2 * sd_v
    hi_2sd = mean_v + 2 * sd_v
    extreme_val = hi_2sd + r.randint(3, 9)
    ans_str = f"[{lo_2sd}; {hi_2sd}], \\text{{Extreme value}} = {extreme_val}"

    prompt = (
        f"A manufacturing process produces bolts with a mean length of $\\bar{{x}} = {mean_v}\\text{{ mm}}$ and a standard deviation of $\\sigma = {sd_v}\\text{{ mm}}$.\n\n"
        f"Any bolt outside the interval $[\\bar{{x}} - 2\\sigma; \\bar{{x}} + 2\\sigma]$ is rejected.\n"
        f"Determine the acceptable interval $[\\bar{{x}} - 2\\sigma; \\bar{{x}} + 2\\sigma]$ and state whether a bolt of length ${extreme_val}\\text{{ mm}}$ is rejected."
    )
    sol = solution_graph(
        goal="Compute 2 SD interval and test candidate value",
        steps=[
            step(from_latex=rf"[{mean_v} - 2({sd_v}); {mean_v} + 2({sd_v})]", to_latex_str=rf"[{lo_2sd}; {hi_2sd}]", op="compute_2sd_bounds", rule="Add and subtract 2*sigma"),
            step(from_latex=rf"{extreme_val} > {hi_2sd}", to_latex_str=f"Rejected ({extreme_val} mm > {hi_2sd} mm)", op="test_candidate", rule="Compare candidate to upper bound"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_33",
        topic=TOPIC,
        subskill="33_two_standard_deviation_interval_and_outlier_check",
        learning_objective_id=f"{LO_PREFIX}_33",
        prompt=prompt,
        prompt_latex=r"[\bar{x} - 2\sigma; \bar{x} + 2\sigma]",
        answer_latex=ans_str,
        answer_sympy=f"({lo_2sd}, {hi_2sd})",
        sample_answer=f"[{lo_2sd}; {hi_2sd}] mm; Yes, {extreme_val} mm is rejected",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "A1", "criterion": f"Lower = {lo_2sd}"}, {"mark": "A1", "criterion": f"Upper = {hi_2sd}"}, {"mark": "A1", "criterion": f"Rejected since {extreme_val} > {hi_2sd}"}]},
        hints={"nudge": f"Multiply the standard deviation ({sd_v}) by 2 before subtracting from and adding to {mean_v}.", "concept": r"$[\bar{x} - 2\sigma; \bar{x} + 2\sigma]$", "breakdown": f"[{lo_2sd}; {hi_2sd}] -> {extreme_val} is outside and rejected."},
        misconception_tags=["used_1_sd_instead_of_2_sd"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="33_two_standard_deviation_interval_and_outlier_check",
        difficulty="medium",
    )


# 34. Compare consistency using standard deviation
def build_34_compare_consistency_using_standard_deviation(r: random.Random) -> Dict[str, Any]:
    mean_score = r.randint(48, 72)
    sd_a = num(r.choice([3.1, 3.8, 4.2, 4.6]), 1)
    sd_b = num(r.choice([8.4, 9.2, 10.5, 11.3]), 1)

    prompt = (
        f"Two batsmen, Player A and Player B, both have a mean score of ${mean_score}$ runs over $10$ matches.\n"
        f"- Player A has a standard deviation of $\\sigma_A = {sd_a}$ runs.\n"
        f"- Player B has a standard deviation of $\\sigma_B = {sd_b}$ runs.\n\n"
        f"Which player is the more **consistent** run-scorer? Justify your answer."
    )
    ans = f"Player A (since \\sigma_A = {sd_a} < \\sigma_B = {sd_b})"
    sol = solution_graph(
        goal="Compare consistency using standard deviation",
        steps=[
            step(from_latex=rf"\sigma_A = {sd_a}, \quad \sigma_B = {sd_b}", to_latex_str=rf"\sigma_A < \sigma_B", op="compare_sds", rule="Compare standard deviations"),
            step(from_latex=rf"\sigma_A < \sigma_B", to_latex_str="Player A is more consistent", op="conclude", rule="Smaller standard deviation means scores are clustered closer to the mean"),
        ],
        final_latex=ans,
    )
    return make_math_question(
        prefix="stat11_34",
        topic=TOPIC,
        subskill="34_compare_consistency_using_standard_deviation",
        learning_objective_id=f"{LO_PREFIX}_34",
        prompt=prompt,
        prompt_latex=rf"\sigma_A = {sd_a} \text{{ vs }} \sigma_B = {sd_b}",
        answer_latex=ans,
        answer_sympy="Player A",
        sample_answer=f"Player A is more consistent because his standard deviation ({sd_a}) is smaller than Player B's ({sd_b}).",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": "Select Player A"}, {"mark": "A1", "criterion": f"Reason: smaller standard deviation ({sd_a} < {sd_b})"}]},
        hints={"nudge": "A lower standard deviation means values vary less around the mean.", "concept": "Smaller SD = greater consistency.", "breakdown": ans},
        misconception_tags=["selected_higher_sd_as_more_consistent"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="34_compare_consistency_using_standard_deviation",
        difficulty="easy",
    )


# 35. Grouped frequency table class midpoints
def build_35_grouped_frequency_table_class_midpoints(r: random.Random) -> Dict[str, Any]:
    w = r.choice([10, 20])
    start = r.choice([0, 10, 20])
    f1, f2, f3 = r.randint(4, 9), r.randint(10, 16), r.randint(5, 11)
    tot_n = f1 + f2 + f3
    m1 = start + w // 2
    m2 = start + w + w // 2
    m3 = start + 2 * w + w // 2

    table_md = (
        f"| Class Interval | Frequency ($f_i$) | Midpoint ($x_i$) |\n"
        f"| :---: | :---: | :---: |\n"
        f"| ${start} \\le x < {start+w}$ | ${f1}$ | $m_1$ |\n"
        f"| ${start+w} \\le x < {start+2*w}$ | ${f2}$ | $m_2$ |\n"
        f"| ${start+2*w} \\le x < {start+3*w}$ | ${f3}$ | $m_3$ |"
    )
    ans_str = f"m_1 = {m1}, m_2 = {m2}, m_3 = {m3}, N = {tot_n}"
    prompt = (
        f"Consider the grouped frequency table below:\n\n"
        f"{table_md}\n\n"
        f"Determine the three class midpoints ($m_1, m_2, m_3$) and the total frequency ($N = \\sum f_i$)."
    )
    sol = solution_graph(
        goal="Compute class midpoints and total frequency N",
        steps=[
            step(from_latex=r"x_i = \frac{\text{lower} + \text{upper}}{2}", to_latex_str=f"m_1 = {m1}, m_2 = {m2}, m_3 = {m3}", op="midpoints", rule="Average lower and upper class boundaries"),
            step(from_latex=rf"N = {f1} + {f2} + {f3}", to_latex_str=str(tot_n), op="sum_frequencies", rule="Add all class frequencies"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_35",
        topic=TOPIC,
        subskill="35_grouped_frequency_table_class_midpoints",
        learning_objective_id=f"{LO_PREFIX}_35",
        prompt=prompt,
        prompt_latex=r"\text{Midpoints } x_i \text{ and } N",
        answer_latex=ans_str,
        answer_sympy=f"({m1}, {m2}, {m3}, {tot_n})",
        sample_answer=f"m1 = {m1}, m2 = {m2}, m3 = {m3}; Total N = {tot_n}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"Midpoints {m1}, {m2}, {m3}"}, {"mark": "A1", "criterion": f"Total N = {tot_n}"}]},
        hints={"nudge": "The midpoint of a class [a; b) is (a + b) / 2.", "concept": r"$x_i = \frac{a + b}{2}$", "breakdown": ans_str},
        misconception_tags=["used_upper_bound_as_midpoint"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="35_grouped_frequency_table_class_midpoints",
        difficulty="easy",
    )


# 36. Estimated mean from grouped frequency table
def build_36_estimated_mean_from_grouped_frequency_table(r: random.Random) -> Dict[str, Any]:
    # 3 classes: [0, 10), [10, 20), [20, 30) with midpoints 5, 15, 25
    f1 = r.randint(3, 8)
    f3 = f1 + r.choice([0, 2, 4])
    f2 = 20 - (f1 + f3)
    if f2 <= 0:
        f1, f2, f3 = 4, 10, 6
    tot_n = f1 + f2 + f3
    sum_fx = f1 * 5 + f2 * 15 + f3 * 25
    est_mean = sum_fx / tot_n
    ans_str = num(est_mean)

    table_md = (
        f"| Interval | Frequency ($f_i$) |\n"
        f"| :---: | :---: |\n"
        f"| $0 \\le x < 10$ | ${f1}$ |\n"
        f"| $10 \\le x < 20$ | ${f2}$ |\n"
        f"| $20 \\le x < 30$ | ${f3}$ |"
    )
    prompt = (
        f"Calculate the **estimated mean** ($\\bar{{x}}$) for the grouped frequency table below:\n\n"
        f"{table_md}"
    )
    sol = solution_graph(
        goal=r"\text{Calculate estimated mean } \frac{\sum f_i x_i}{N}",
        steps=[
            step(from_latex=r"\text{Midpoints} = 5; 15; 25", to_latex_str=rf"\sum f_i x_i = {f1}(5) + {f2}(15) + {f3}(25) = {sum_fx}", op="sum_fx", rule="Multiply each frequency by its class midpoint"),
            step(from_latex=rf"\bar{{x}} = \frac{{{sum_fx}}}{{{tot_n}}}", to_latex_str=ans_str, op="divide_by_N", rule=f"Divide by total frequency N = {tot_n}"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_36",
        topic=TOPIC,
        subskill="36_estimated_mean_from_grouped_frequency_table",
        learning_objective_id=f"{LO_PREFIX}_36",
        prompt=prompt,
        prompt_latex=rf"\frac{{\sum f_i x_i}}{{{tot_n}}}",
        answer_latex=ans_str,
        answer_sympy=str(est_mean),
        sample_answer=f"Estimated mean = {ans_str}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": "Midpoints 5, 15, 25"}, {"mark": "M1", "criterion": f"Sum(f*x) = {sum_fx}"}, {"mark": "A1", "criterion": f"Estimated mean = {ans_str}"}]},
        hints={"nudge": "Find the midpoint of each interval (5, 15, 25), multiply by the frequencies, and divide by total N.", "concept": r"$\bar{x} \approx \frac{\sum f_i x_i}{\sum f_i}$", "breakdown": f"{sum_fx} / {tot_n} = {ans_str}"},
        misconception_tags=["divided_by_number_of_classes_instead_of_total_frequency"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="36_estimated_mean_from_grouped_frequency_table",
        difficulty="medium",
    )


# 37. Modal class and median class from grouped table
def build_37_modal_class_and_median_class_from_grouped_table(r: random.Random) -> Dict[str, Any]:
    f1 = r.randint(4, 7)
    f2 = r.randint(8, 11)
    f3 = r.randint(15, 22)
    f4 = r.randint(5, 9)
    tot_n = f1 + f2 + f3 + f4

    table_md = (
        f"| Mass ($m$ in kg) | Frequency ($f_i$) |\n"
        f"| :---: | :---: |\n"
        f"| $40 \\le m < 50$ | ${f1}$ |\n"
        f"| $50 \\le m < 60$ | ${f2}$ |\n"
        f"| $60 \\le m < 70$ | ${f3}$ |\n"
        f"| $70 \\le m < 80$ | ${f4}$ |"
    )
    ans_str = "60 \\le m < 70"
    prompt = (
        f"Refer to the grouped frequency table of learner masses below (total $N = {tot_n}$):\n\n"
        f"{table_md}\n\n"
        f"Identify the **modal class interval**."
    )
    sol = solution_graph(
        goal="Identify the modal class interval",
        steps=[
            step(from_latex=rf"\max(f_i) = {f3}", to_latex_str=ans_str, op="find_max_freq", rule="The modal class is the interval with the highest frequency"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_37",
        topic=TOPIC,
        subskill="37_modal_class_and_median_class_from_grouped_table",
        learning_objective_id=f"{LO_PREFIX}_37",
        prompt=prompt,
        prompt_latex=r"\text{Modal class}",
        answer_latex=ans_str,
        answer_sympy="60 <= m < 70",
        sample_answer=f"60 <= m < 70 (highest frequency = {f3})",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"Highest frequency is {f3}"}, {"mark": "A1", "criterion": "60 <= m < 70"}]},
        hints={"nudge": "Look for the class interval with the largest frequency.", "concept": f"The highest frequency is {f3}.", "breakdown": "60 <= m < 70"},
        misconception_tags=["wrote_frequency_number_instead_of_class_interval"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="37_modal_class_and_median_class_from_grouped_table",
        difficulty="easy",
    )


# 38. Cumulative frequency table completion
def build_38_cumulative_frequency_table_completion(r: random.Random) -> Dict[str, Any]:
    f1 = r.randint(5, 10)
    f2 = r.randint(11, 18)
    f3 = r.randint(12, 20)
    f4 = r.randint(6, 12)
    cf1 = f1
    cf2 = cf1 + f2
    cf3 = cf2 + f3
    cf4 = cf3 + f4

    table_md = (
        f"| Interval | Frequency ($f_i$) | Cumulative Frequency ($CF$) |\n"
        f"| :---: | :---: | :---: |\n"
        f"| $0 \\le x < 10$ | ${f1}$ | ${cf1}$ |\n"
        f"| $10 \\le x < 20$ | ${f2}$ | $A$ |\n"
        f"| $20 \\le x < 30$ | ${f3}$ | $B$ |\n"
        f"| $30 \\le x < 40$ | ${f4}$ | ${cf4}$ |"
    )
    ans_str = f"A = {cf2}, B = {cf3}"
    prompt = (
        f"Complete the cumulative frequency table below by determining the missing values $A$ and $B$:\n\n"
        f"{table_md}"
    )
    sol = solution_graph(
        goal="Compute missing cumulative frequencies A and B",
        steps=[
            step(from_latex=rf"A = {cf1} + {f2}", to_latex_str=str(cf2), op="accumulate_A", rule="Add class 2 frequency to previous cumulative frequency"),
            step(from_latex=rf"B = {cf2} + {f3}", to_latex_str=str(cf3), op="accumulate_B", rule="Add class 3 frequency to A"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_38",
        topic=TOPIC,
        subskill="38_cumulative_frequency_table_completion",
        learning_objective_id=f"{LO_PREFIX}_38",
        prompt=prompt,
        prompt_latex=r"\text{Cumulative Frequencies } A \text{ and } B",
        answer_latex=ans_str,
        answer_sympy=f"({cf2}, {cf3})",
        sample_answer=f"A = {cf2}, B = {cf3}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"A = {cf2}"}, {"mark": "A1", "criterion": f"B = {cf3}"}]},
        hints={"nudge": "Add each row's frequency to the running total from the row above.", "concept": r"$CF_k = CF_{k-1} + f_k$", "breakdown": f"A = {cf1} + {f2} = {cf2}; B = {cf2} + {f3} = {cf3}"},
        misconception_tags=["copied_individual_frequency_into_cf"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="38_cumulative_frequency_table_completion",
        difficulty="easy",
    )


# 39. Recover individual frequencies from cumulative frequency
def build_39_recover_individual_frequencies_from_cumulative_frequency(r: random.Random) -> Dict[str, Any]:
    cf1 = r.randint(6, 12)
    f2 = r.randint(14, 24)
    cf2 = cf1 + f2
    f3 = r.randint(15, 25)
    cf3 = cf2 + f3

    table_md = (
        f"| Interval | Frequency ($f_i$) | Cumulative Frequency ($CF$) |\n"
        f"| :---: | :---: | :---: |\n"
        f"| $10 \\le t < 20$ | ${cf1}$ | ${cf1}$ |\n"
        f"| $20 \\le t < 30$ | $p$ | ${cf2}$ |\n"
        f"| $30 \\le t < 40$ | $q$ | ${cf3}$ |"
    )
    ans_str = f"p = {f2}, q = {f3}"
    prompt = (
        f"Use the cumulative frequency column in the table below to determine the individual class frequencies $p$ and $q$:\n\n"
        f"{table_md}"
    )
    sol = solution_graph(
        goal="Recover individual class frequencies from CF",
        steps=[
            step(from_latex=rf"p = {cf2} - {cf1}", to_latex_str=str(f2), op="subtract_cf2", rule="f_2 = CF_2 - CF_1"),
            step(from_latex=rf"q = {cf3} - {cf2}", to_latex_str=str(f3), op="subtract_cf3", rule="f_3 = CF_3 - CF_2"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_39",
        topic=TOPIC,
        subskill="39_recover_individual_frequencies_from_cumulative_frequency",
        learning_objective_id=f"{LO_PREFIX}_39",
        prompt=prompt,
        prompt_latex=r"f_k = CF_k - CF_{k-1}",
        answer_latex=ans_str,
        answer_sympy=f"({f2}, {f3})",
        sample_answer=f"p = {f2}, q = {f3}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"p = {f2}"}, {"mark": "A1", "criterion": f"q = {f3}"}]},
        hints={"nudge": "Subtract consecutive cumulative frequencies to find each class frequency.", "concept": r"$f_k = CF_k - CF_{k-1}$", "breakdown": f"p = {cf2} - {cf1} = {f2}; q = {cf3} - {cf2} = {f3}"},
        misconception_tags=["added_cumulative_frequencies_instead_of_subtracting"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="39_recover_individual_frequencies_from_cumulative_frequency",
        difficulty="easy",
    )


# 40. Ogive grounding point and upper bound plotting (with inline_svg)
def build_40_ogive_grounding_point_and_upper_bound_plotting(r: random.Random) -> Dict[str, Any]:
    start = r.choice([10, 15, 20, 25])
    w = 10
    bounds = [start + i * w for i in range(5)]
    cfs = [0, r.randint(5, 9), r.randint(16, 22), r.randint(30, 38), r.choice([40, 50, 60])]
    diag = _ogive_svg(bounds, cfs, title="Ogive Grounding & Upper Boundaries")
    ans_str = f"({start}; 0) \\text{{ and }} ({bounds[2]}; {cfs[2]})"

    prompt = (
        f"An ogive (cumulative frequency curve) is plotted for grouped intervals starting at ${start} \\le x < {start+w}$.\n\n"
        f"Refer to the ogive and write down:\n"
        f"1. The coordinates of the **grounding point** on the horizontal axis.\n"
        f"2. The coordinates plotted for the class ${bounds[1]} \\le x < {bounds[2]}$ with cumulative frequency ${cfs[2]}$."
    )
    sol = solution_graph(
        goal="Identify ogive grounding coordinate and upper-boundary coordinate",
        steps=[
            step(from_latex=r"\text{Lower bound of first class}", to_latex_str=f"({start}; 0)", op="grounding_point", rule="Ogive is grounded at (lower bound of 1st class; 0)"),
            step(from_latex=r"(\text{Upper bound}; CF)", to_latex_str=f"({bounds[2]}; {cfs[2]})", op="upper_bound_point", rule="Plot cumulative frequency against the upper class boundary"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_40",
        topic=TOPIC,
        subskill="40_ogive_grounding_point_and_upper_bound_plotting",
        learning_objective_id=f"{LO_PREFIX}_40",
        prompt=prompt,
        prompt_latex=r"\text{Ogive Coordinates}",
        answer_latex=ans_str,
        answer_sympy=f"(({start}, 0), ({bounds[2]}, {cfs[2]}))",
        sample_answer=f"1. ({start}; 0); 2. ({bounds[2]}; {cfs[2]})",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"Grounding point ({start}; 0)"}, {"mark": "A1", "criterion": f"Plotted point ({bounds[2]}; {cfs[2]})"}]},
        hints={"nudge": "An ogive starts at cumulative frequency 0 at the lower boundary of the first interval, and plots each CF at the upper boundary.", "concept": f"Grounding = ({start}; 0), Class point = ({bounds[2]}; {cfs[2]}).", "breakdown": ans_str},
        misconception_tags=["plotted_ogive_at_midpoints_instead_of_upper_boundaries"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="40_ogive_grounding_point_and_upper_bound_plotting",
        difficulty="easy",
    )


# 41. Ogive read total sample size and modal class (with inline_svg)
def build_41_ogive_read_total_sample_size_and_modal_class_svg(r: random.Random) -> Dict[str, Any]:
    bounds = [10, 20, 30, 40, 50]
    f1 = r.randint(4, 8)
    f2 = r.randint(8, 12)
    f3 = r.randint(20, 28)  # steepest segment: [30, 40)
    f4 = r.randint(5, 9)
    cfs = [0, f1, f1 + f2, f1 + f2 + f3, f1 + f2 + f3 + f4]
    tot_n = cfs[-1]
    diag = _ogive_svg(bounds, cfs, title="Cumulative Frequency Curve")
    ans_str = f"N = {tot_n}, \\text{{Modal class}}: 30 \\le x < 40"

    prompt = (
        f"Use the cumulative frequency curve (ogive) to determine:\n"
        f"1. The total number of observations ($N$).\n"
        f"2. The **modal class interval** (where the curve is steepest) and its frequency."
    )
    sol = solution_graph(
        goal="Read total N and steepest modal class from ogive",
        steps=[
            step(from_latex=r"\text{Maximum cumulative frequency}", to_latex_str=f"N = {tot_n}", op="read_max_cf", rule="Read top endpoint of ogive"),
            step(from_latex=rf"CF(40) - CF(30) = {cfs[3]} - {cfs[2]} = {f3}", to_latex_str="30 \\le x < 40", op="steepest_segment", rule="Largest vertical jump gives modal class"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_41",
        topic=TOPIC,
        subskill="41_ogive_read_total_sample_size_and_modal_class_svg",
        learning_objective_id=f"{LO_PREFIX}_41",
        prompt=prompt,
        prompt_latex=r"N \text{ and Modal Class from Ogive}",
        answer_latex=ans_str,
        answer_sympy=f"({tot_n}, {f3})",
        sample_answer=f"N = {tot_n}; Modal class is 30 <= x < 40 with frequency {f3}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "A1", "criterion": f"N = {tot_n}"}, {"mark": "A1", "criterion": "Modal class 30 <= x < 40"}, {"mark": "A1", "criterion": f"Frequency = {f3}"}]},
        hints={"nudge": "The highest y-value gives N, and the interval with the largest vertical increase is the modal class.", "concept": f"Jump on [30; 40) is {cfs[3]} - {cfs[2]} = {f3}.", "breakdown": ans_str},
        misconception_tags=["read_last_class_as_modal_class"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="41_ogive_read_total_sample_size_and_modal_class_svg",
        difficulty="medium",
    )


# 42. Ogive estimate median from curve (with inline_svg)
def build_42_ogive_estimate_median_from_curve_svg(r: random.Random) -> Dict[str, Any]:
    tot_n = r.choice([40, 60, 80, 100])
    half_n = tot_n // 2
    med_x = r.choice([30, 40, 50])
    bounds = [med_x - 20, med_x - 10, med_x, med_x + 10, med_x + 20]
    cfs = [0, half_n // 2, half_n, (3 * tot_n) // 4, tot_n]
    diag = _ogive_svg(bounds, cfs, title=f"Ogive (N = {tot_n})", highlight_cf=half_n, highlight_x=med_x)

    prompt = (
        f"The ogive represents ${tot_n}$ observations, with key points labelled.\n\n"
        f"Determine the cumulative frequency position $\\frac{{N}}{{2}}$ and read off the **median** ($Q_2$) from the ogive."
    )
    ans_str = str(med_x)
    sol = solution_graph(
        goal="Estimate median from ogive at CF = N/2",
        steps=[
            step(from_latex=rf"\frac{{N}}{{2}} = \frac{{{tot_n}}}{{2}}", to_latex_str=str(half_n), op="median_cf_pos", rule="Locate 50% cumulative frequency on vertical axis"),
            step(from_latex=rf"CF = {half_n}", to_latex_str=f"Q_2 = {med_x}", op="read_horizontal", rule="Read corresponding value on horizontal axis"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_42",
        topic=TOPIC,
        subskill="42_ogive_estimate_median_from_curve_svg",
        learning_objective_id=f"{LO_PREFIX}_42",
        prompt=prompt,
        prompt_latex=rf"Q_2 \text{{ at }} CF = {half_n}",
        answer_latex=ans_str,
        answer_sympy=ans_str,
        sample_answer=f"At CF = {half_n}, Median = {med_x}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"Locate CF = {half_n}"}, {"mark": "A1", "criterion": f"Median = {med_x}"}]},
        hints={"nudge": f"Find N/2 = {half_n} on the vertical axis and trace across to the curve.", "concept": f"The point ({med_x}; {half_n}) lies on the curve.", "breakdown": f"Median = {med_x}"},
        misconception_tags=["read_vertical_axis_instead_of_horizontal_for_median"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="42_ogive_estimate_median_from_curve_svg",
        difficulty="easy",
    )


# 43. Ogive estimate quartiles and IQR (with inline_svg)
def build_43_ogive_estimate_quartiles_and_iqr_svg(r: random.Random) -> Dict[str, Any]:
    tot_n = r.choice([40, 60, 80, 120])
    q1_cf = tot_n // 4
    med_cf = tot_n // 2
    q3_cf = (3 * tot_n) // 4
    b0 = r.choice([10, 20])
    w = r.choice([10, 15])
    bounds = [b0, b0 + w, b0 + 2 * w, b0 + 3 * w, b0 + 4 * w]
    cfs = [0, q1_cf, med_cf, q3_cf, tot_n]
    q1_v = bounds[1]
    q3_v = bounds[3]
    iqr_v = q3_v - q1_v
    diag = _ogive_svg(bounds, cfs, title=f"Quartiles on Ogive (N = {tot_n})", highlight_cf=q3_cf, highlight_x=q3_v)

    prompt = (
        f"Refer to the ogive for $N = {tot_n}$ learners.\n\n"
        f"Read off the lower quartile ($Q_1$) and upper quartile ($Q_3$), and hence calculate the **interquartile range** ($\\text{{IQR}}$)."
    )
    ans_str = f"Q_1 = {q1_v}, Q_3 = {q3_v}, \\text{{IQR}} = {iqr_v}"
    sol = solution_graph(
        goal="Read Q1 and Q3 from ogive and compute IQR",
        steps=[
            step(from_latex=rf"\text{{At }} CF = {q1_cf} \implies Q_1 = {q1_v}", to_latex_str=rf"\text{{At }} CF = {q3_cf} \implies Q_3 = {q3_v}", op="read_quartiles", rule="Read x at 0,25N and 0,75N"),
            step(from_latex=rf"\text{{IQR}} = {q3_v} - {q1_v}", to_latex_str=str(iqr_v), op="subtract", rule="IQR = Q3 - Q1"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_43",
        topic=TOPIC,
        subskill="43_ogive_estimate_quartiles_and_iqr_svg",
        learning_objective_id=f"{LO_PREFIX}_43",
        prompt=prompt,
        prompt_latex=r"\text{IQR} = Q_3 - Q_1 \text{ from Ogive}",
        answer_latex=ans_str,
        answer_sympy=str(iqr_v),
        sample_answer=f"Q1 = {q1_v}, Q3 = {q3_v}, IQR = {iqr_v}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "A1", "criterion": f"Q1 = {q1_v}"}, {"mark": "A1", "criterion": f"Q3 = {q3_v}"}, {"mark": "A1", "criterion": f"IQR = {iqr_v}"}]},
        hints={"nudge": f"Q1 is at CF = {q1_cf} and Q3 is at CF = {q3_cf}.", "concept": r"$\text{IQR} = Q_3 - Q_1$", "breakdown": ans_str},
        misconception_tags=["subtracted_cumulative_frequencies_instead_of_x_values"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="43_ogive_estimate_quartiles_and_iqr_svg",
        difficulty="medium",
    )


# 44. Ogive estimate percentile value (with inline_svg)
def build_44_ogive_estimate_percentile_value_svg(r: random.Random) -> Dict[str, Any]:
    tot_n = r.choice([50, 100, 150, 200])
    p_80_cf = int(0.8 * tot_n)
    b0 = r.choice([20, 30, 40])
    bounds = [b0, b0 + 10, b0 + 20, b0 + 30, b0 + 40]
    cfs = [0, int(0.2 * tot_n), int(0.5 * tot_n), p_80_cf, tot_n]
    ans_val = bounds[3]
    diag = _ogive_svg(bounds, cfs, title=f"Percentile Estimation (N = {tot_n})", highlight_cf=p_80_cf, highlight_x=ans_val)

    prompt = (
        f"Using the cumulative frequency curve for $N = {tot_n}$ observations, determine the **$80^\\text{{th}}$ percentile** ($P_{{80}}$)."
    )
    sol = solution_graph(
        goal="Find 80th percentile from ogive",
        steps=[
            step(from_latex=rf"0{{,}}80 \times {tot_n}", to_latex_str=f"CF = {p_80_cf}", op="percentile_cf", rule="Calculate 80% of N"),
            step(from_latex=rf"CF = {p_80_cf}", to_latex_str=str(ans_val), op="read_x", rule="Read x-coordinate on ogive"),
        ],
        final_latex=str(ans_val),
    )
    return make_math_question(
        prefix="stat11_44",
        topic=TOPIC,
        subskill="44_ogive_estimate_percentile_value_svg",
        learning_objective_id=f"{LO_PREFIX}_44",
        prompt=prompt,
        prompt_latex=rf"P_{{80}} \text{{ at }} CF = {p_80_cf}",
        answer_latex=str(ans_val),
        answer_sympy=str(ans_val),
        sample_answer=f"P_80 = {ans_val} (at CF = {p_80_cf})",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"80% of {tot_n} = {p_80_cf}"}, {"mark": "A1", "criterion": f"P_80 = {ans_val}"}]},
        hints={"nudge": f"Find 80% of {tot_n} = {p_80_cf} on the vertical axis, then read the x-value.", "concept": f"The point ({ans_val}; {p_80_cf}) is on the ogive.", "breakdown": str(ans_val)},
        misconception_tags=["read_cf_instead_of_horizontal_variable"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="44_ogive_estimate_percentile_value_svg",
        difficulty="medium",
    )


# 45. Ogive count exceeding threshold (with inline_svg)
def build_45_ogive_count_exceeding_threshold_svg(r: random.Random) -> Dict[str, Any]:
    tot_n = r.choice([60, 80, 100])
    cf_at_thresh = r.randint(tot_n - 28, tot_n - 12)
    above_count = tot_n - cf_at_thresh
    b0 = r.choice([10, 20])
    bounds = [b0, b0 + 15, b0 + 30, b0 + 45, b0 + 60]
    thresh_x = bounds[3]
    cfs = [0, 12, 32, cf_at_thresh, tot_n]
    diag = _ogive_svg(bounds, cfs, title=f"Threshold Query on Ogive (N = {tot_n})", highlight_cf=cf_at_thresh, highlight_x=thresh_x)

    prompt = (
        f"The ogive shows the marks of ${tot_n}$ learners. A distinction requires **more than ${thresh_x}$ marks**.\n\n"
        f"Use the ogive to determine how many learners achieved a distinction."
    )
    sol = solution_graph(
        goal="Calculate count above threshold using N - CF(threshold)",
        steps=[
            step(from_latex=rf"x = {thresh_x}", to_latex_str=rf"CF({thresh_x}) = {cf_at_thresh}", op="read_cf", rule="Read cumulative frequency at threshold"),
            step(from_latex=rf"{tot_n} - {cf_at_thresh}", to_latex_str=str(above_count), op="subtract_from_total", rule="Subtract from total N to find number exceeding threshold"),
        ],
        final_latex=str(above_count),
    )
    return make_math_question(
        prefix="stat11_45",
        topic=TOPIC,
        subskill="45_ogive_count_exceeding_threshold_svg",
        learning_objective_id=f"{LO_PREFIX}_45",
        prompt=prompt,
        prompt_latex=rf"{tot_n} - CF({thresh_x})",
        answer_latex=str(above_count),
        answer_sympy=str(above_count),
        sample_answer=f"{above_count} learners ({tot_n} - {cf_at_thresh})",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"Read CF({thresh_x}) = {cf_at_thresh}"}, {"mark": "A1", "criterion": f"{tot_n} - {cf_at_thresh} = {above_count}"}]},
        hints={"nudge": f"The ogive gives how many learners scored {thresh_x} OR LESS ({cf_at_thresh}). Subtract this from {tot_n}!", "concept": r"$\text{Count above } k = N - CF(k)$", "breakdown": f"{tot_n} - {cf_at_thresh} = {above_count}"},
        misconception_tags=["gave_cumulative_frequency_instead_of_subtracting_from_N"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="45_ogive_count_exceeding_threshold_svg",
        difficulty="medium",
    )


# 46. Histogram read frequencies and total (with inline_svg)
def build_46_histogram_read_frequencies_and_total_svg(r: random.Random) -> Dict[str, Any]:
    bounds = [0, 10, 20, 30, 40]
    freqs = [r.randint(4, 9), r.randint(12, 18), r.randint(10, 15), r.randint(3, 8)]
    tot_n = sum(freqs)
    f_ge_20 = freqs[2] + freqs[3]
    diag = _histogram_svg(bounds, freqs, title="Histogram of Travel Times (minutes)")
    ans_str = f"N = {tot_n}, \\text{{Count}}(\\ge 20) = {f_ge_20}"

    prompt = (
        f"Refer to the histogram of learner travel times (in minutes).\n\n"
        f"Determine:\n"
        f"1. The total number of learners surveyed ($N$).\n"
        f"2. The number of learners whose travel time is $20\\text{{ minutes}}$ or more."
    )
    sol = solution_graph(
        goal="Read bar heights from histogram",
        steps=[
            step(from_latex=rf"N = {' + '.join(str(x) for x in freqs)}", to_latex_str=str(tot_n), op="sum_all_bars", rule="Add frequencies of all 4 bars"),
            step(from_latex=rf"{freqs[2]} + {freqs[3]}", to_latex_str=str(f_ge_20), op="sum_upper_bars", rule="Add frequencies for [20; 30) and [30; 40)"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_46",
        topic=TOPIC,
        subskill="46_histogram_read_frequencies_and_total_svg",
        learning_objective_id=f"{LO_PREFIX}_46",
        prompt=prompt,
        prompt_latex=r"N \text{ and Count}(\ge 20)",
        answer_latex=ans_str,
        answer_sympy=f"({tot_n}, {f_ge_20})",
        sample_answer=f"1. N = {tot_n}; 2. {f_ge_20} learners",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"N = {tot_n}"}, {"mark": "A1", "criterion": f"{f_ge_20} learners"}]},
        hints={"nudge": "Add the numbers above all bars for the total, and add the last two bars for >= 20 minutes.", "concept": f"Total = {tot_n}, >= 20 min = {freqs[2]} + {freqs[3]} = {f_ge_20}.", "breakdown": ans_str},
        misconception_tags=["read_only_one_bar_for_inequality_range"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="46_histogram_read_frequencies_and_total_svg",
        difficulty="easy",
    )


# 47. Frequency polygon midpoints and interpretation (with inline_svg)
def build_47_frequency_polygon_midpoints_and_interpretation_svg(r: random.Random) -> Dict[str, Any]:
    b0 = r.choice([10, 20, 30])
    bounds = [b0, b0 + 10, b0 + 20, b0 + 30, b0 + 40]
    freqs = [r.randint(5, 8), r.randint(16, 23), r.randint(10, 14), r.randint(4, 7)]
    peak_mid = b0 + 15
    peak_f = freqs[1]
    diag = _histogram_svg(bounds, freqs, title="Histogram & Frequency Polygon", show_polygon=True)
    ans_str = f"({peak_mid}; {peak_f})"

    prompt = (
        f"A frequency polygon (red line) is superposed on the histogram by joining the midpoints of the tops of the bars.\n\n"
        f"Write down the coordinates $(\\text{{midpoint}}; \\text{{frequency}})$ of the **highest vertex (peak)** of the frequency polygon."
    )
    sol = solution_graph(
        goal="Determine coordinates of peak vertex of frequency polygon",
        steps=[
            step(from_latex=rf"\text{{Midpoint of }} [{b0+10}; {b0+20})", to_latex_str=str(peak_mid), op="midpoint", rule="Average lower and upper boundaries of modal bar"),
            step(from_latex=rf"\text{{Max frequency}} = {peak_f}", to_latex_str=ans_str, op="vertex_coords", rule="Combine midpoint and peak frequency"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_47",
        topic=TOPIC,
        subskill="47_frequency_polygon_midpoints_and_interpretation_svg",
        learning_objective_id=f"{LO_PREFIX}_47",
        prompt=prompt,
        prompt_latex=r"\text{Peak vertex of Frequency Polygon}",
        answer_latex=ans_str,
        answer_sympy=f"({peak_mid}, {peak_f})",
        sample_answer=f"({peak_mid}; {peak_f})",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"Midpoint = {peak_mid}"}, {"mark": "A1", "criterion": f"Frequency = {peak_f}"}]},
        hints={"nudge": "A frequency polygon plots class midpoints on the x-axis and frequencies on the y-axis.", "concept": f"The tallest bar spans {b0+10} to {b0+20}, so its midpoint is {peak_mid}.", "breakdown": ans_str},
        misconception_tags=["used_upper_boundary_instead_of_midpoint_for_polygon"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="47_frequency_polygon_midpoints_and_interpretation_svg",
        difficulty="easy",
    )


# 48. Symmetric vs skewed histogram identification (with inline_svg)
def build_48_symmetric_vs_skewed_histogram_identification_svg(r: random.Random) -> Dict[str, Any]:
    shape = r.choice(["right", "left", "sym"])
    bounds = [10, 20, 30, 40, 50, 60]
    if shape == "right":
        f_peak = r.randint(20, 26)
        freqs = [f_peak - 4, f_peak, 12, 6, 3]
        ans = "Positively skewed (skewed to the right)"
    elif shape == "left":
        f_peak = r.randint(20, 26)
        freqs = [3, 6, 12, f_peak, f_peak - 4]
        ans = "Negatively skewed (skewed to the left)"
    else:
        f_peak = r.randint(20, 26)
        freqs = [5, 12, f_peak, 12, 5]
        ans = "Symmetrical"

    diag = _histogram_svg(bounds, freqs, title="Distribution Shape Analysis")
    prompt = (
        f"Examine the shape of the frequency histogram.\n\n"
        f"State whether the distribution is **positively skewed (skewed to the right)**, "
        f"**negatively skewed (skewed to the left)**, or **symmetrical**."
    )
    sol = solution_graph(
        goal="Classify skewness from histogram tail",
        steps=[
            step(from_latex=rf"\text{{Frequencies}} = {freqs}", to_latex_str=ans, op="inspect_tail", rule="Direction of the longer tail determines skewness"),
        ],
        final_latex=ans,
    )
    return make_math_question(
        prefix="stat11_48",
        topic=TOPIC,
        subskill="48_symmetric_vs_skewed_histogram_identification_svg",
        learning_objective_id=f"{LO_PREFIX}_48",
        prompt=prompt,
        prompt_latex=r"\text{Histogram Skewness}",
        answer_latex=ans,
        answer_sympy=ans,
        sample_answer=ans,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": "Identify direction of tail"}, {"mark": "A1", "criterion": ans}]},
        hints={"nudge": "Look at which side has the longer tail of smaller bars.", "concept": "Tail to the right = positively skewed; tail to the left = negatively skewed; mirror image = symmetrical.", "breakdown": ans},
        misconception_tags=["named_skewness_after_peak_side_instead_of_tail_side"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="48_symmetric_vs_skewed_histogram_identification_svg",
        difficulty="easy",
    )


# 49. Linear transformation of summary statistics table
def build_49_linear_transformation_of_summary_statistics_table(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3, 4])
    b = r.randint(5, 15)
    old_mean = r.randint(20, 35)
    old_iqr = r.randint(6, 12)
    old_sd = r.randint(3, 7)

    new_mean = a * old_mean + b
    new_iqr = a * old_iqr
    new_sd = a * old_sd
    ans_str = f"\\bar{{y}} = {new_mean}, \\text{{IQR}}_y = {new_iqr}, \\sigma_y = {new_sd}"

    table_md = (
        f"| Statistic | Original ($x$) | Transformed ($y = {a}x + {b}$) |\n"
        f"| :--- | :---: | :---: |\n"
        f"| Mean | ${old_mean}$ | $\\bar{{y}}$ |\n"
        f"| Interquartile Range ($\\text{{IQR}}$) | ${old_iqr}$ | $\\text{{IQR}}_y$ |\n"
        f"| Standard Deviation ($\\sigma$) | ${old_sd}$ | $\\sigma_y$ |"
    )
    prompt = (
        f"Every value $x$ in a data set is transformed according to the linear rule $y = {a}x + {b}$.\n\n"
        f"{table_md}\n\n"
        f"Determine the values of $\\bar{{y}}$, $\\text{{IQR}}_y$, and $\\sigma_y$."
    )
    sol = solution_graph(
        goal=f"Transform summary statistics under y = {a}x + {b}",
        steps=[
            step(from_latex=rf"\bar{{y}} = {a}({old_mean}) + {b}", to_latex_str=str(new_mean), op="transform_mean", rule="Mean is affected by both multiplication and addition"),
            step(from_latex=rf"\text{{IQR}}_y = {a}({old_iqr}), \quad \sigma_y = {a}({old_sd})", to_latex_str=f"\\text{{IQR}}_y = {new_iqr}, \\sigma_y = {new_sd}", op="transform_spread", rule="Measures of dispersion are scaled by |a| only (unaffected by +b)"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_49",
        topic=TOPIC,
        subskill="49_linear_transformation_of_summary_statistics_table",
        learning_objective_id=f"{LO_PREFIX}_49",
        prompt=prompt,
        prompt_latex=rf"y = {a}x + {b}",
        answer_latex=ans_str,
        answer_sympy=f"({new_mean}, {new_iqr}, {new_sd})",
        sample_answer=f"Mean = {new_mean}, IQR = {new_iqr}, SD = {new_sd}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "A1", "criterion": f"new Mean = {new_mean}"}, {"mark": "A1", "criterion": f"new IQR = {new_iqr}"}, {"mark": "A1", "criterion": f"new SD = {new_sd}"}]},
        hints={"nudge": "Measures of central tendency scale by a and shift by +b, whereas measures of dispersion only scale by |a|.", "concept": f"y_bar = {a}*{old_mean} + {b}; IQR_y = {a}*{old_iqr}; SD_y = {a}*{old_sd}.", "breakdown": ans_str},
        misconception_tags=["added_constant_b_to_iqr_and_sd"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="49_linear_transformation_of_summary_statistics_table",
        difficulty="hard",
    )


# 50. Statistics diagnostic autopsy and misconception repair
def build_50_statistics_diagnostic_autopsy_and_misconception_repair(r: random.Random) -> Dict[str, Any]:
    lo = r.choice([10, 20, 30, 40])
    hi = lo + 10
    mid = lo + 5
    cf = r.randint(15, 45)
    ans_str = f"({hi}; {cf})"

    prompt = (
        f"A learner is constructing a cumulative frequency table and ogive. For the class interval "
        f"${lo} \\le x < {hi}$ with cumulative frequency ${cf}$, the learner plots the point $({mid}; {cf})$.\n\n"
        f"1. Identify the error in the learner's method.\n"
        f"2. Write down the correct coordinates that must be plotted for this class interval."
    )
    sol = solution_graph(
        goal="Diagnose midpoint-plotting error on ogive and state upper-boundary point",
        steps=[
            step(from_latex=rf"\text{{Learner plotted midpoint }} x = {mid}", to_latex_str=rf"\text{{Must use upper boundary }} x = {hi}", op="diagnose_error", rule="Cumulative frequency counts all observations below the upper class boundary"),
            step(from_latex=rf"(\text{{Upper bound}}; CF)", to_latex_str=ans_str, op="correct_point", rule="Plot (upper boundary; cumulative frequency)"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_50",
        topic=TOPIC,
        subskill="50_statistics_diagnostic_autopsy_and_misconception_repair",
        learning_objective_id=f"{LO_PREFIX}_50",
        prompt=prompt,
        prompt_latex=rf"\text{{Correct ogive point for }} {lo} \le x < {hi}, CF = {cf}",
        answer_latex=ans_str,
        answer_sympy=f"({hi}, {cf})",
        sample_answer=f"The learner used the class midpoint ({mid}) instead of the upper class boundary ({hi}). Correct point: ({hi}; {cf}).",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": "Explain that ogives use upper boundaries, not midpoints"}, {"mark": "A1", "criterion": f"({hi}; {cf})"}]},
        hints={"nudge": "Midpoints are used for frequency polygons and estimated means, NOT for ogives!", "concept": "Cumulative frequencies are always plotted against the upper boundary of each class interval.", "breakdown": f"Correct point is ({hi}; {cf})."},
        misconception_tags=["plotted_ogive_at_midpoints_instead_of_upper_boundaries"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="50_statistics_diagnostic_autopsy_and_misconception_repair",
        difficulty="medium",
    )


ARCHETYPES_26_50 = {
    "26_deviations_from_mean_sum_to_zero": build_26_deviations_from_mean_sum_to_zero,
    "27_variance_calculation_from_ungrouped_data": build_27_variance_calculation_from_ungrouped_data,
    "28_standard_deviation_from_ungrouped_data": build_28_standard_deviation_from_ungrouped_data,
    "29_standard_deviation_from_variance_and_vice_versa": build_29_standard_deviation_from_variance_and_vice_versa,
    "30_one_standard_deviation_interval_bounds": build_30_one_standard_deviation_interval_bounds,
    "31_count_values_within_one_standard_deviation": build_31_count_values_within_one_standard_deviation,
    "32_percentage_within_one_standard_deviation": build_32_percentage_within_one_standard_deviation,
    "33_two_standard_deviation_interval_and_outlier_check": build_33_two_standard_deviation_interval_and_outlier_check,
    "34_compare_consistency_using_standard_deviation": build_34_compare_consistency_using_standard_deviation,
    "35_grouped_frequency_table_class_midpoints": build_35_grouped_frequency_table_class_midpoints,
    "36_estimated_mean_from_grouped_frequency_table": build_36_estimated_mean_from_grouped_frequency_table,
    "37_modal_class_and_median_class_from_grouped_table": build_37_modal_class_and_median_class_from_grouped_table,
    "38_cumulative_frequency_table_completion": build_38_cumulative_frequency_table_completion,
    "39_recover_individual_frequencies_from_cumulative_frequency": build_39_recover_individual_frequencies_from_cumulative_frequency,
    "40_ogive_grounding_point_and_upper_bound_plotting": build_40_ogive_grounding_point_and_upper_bound_plotting,
    "41_ogive_read_total_sample_size_and_modal_class_svg": build_41_ogive_read_total_sample_size_and_modal_class_svg,
    "42_ogive_estimate_median_from_curve_svg": build_42_ogive_estimate_median_from_curve_svg,
    "43_ogive_estimate_quartiles_and_iqr_svg": build_43_ogive_estimate_quartiles_and_iqr_svg,
    "44_ogive_estimate_percentile_value_svg": build_44_ogive_estimate_percentile_value_svg,
    "45_ogive_count_exceeding_threshold_svg": build_45_ogive_count_exceeding_threshold_svg,
    "46_histogram_read_frequencies_and_total_svg": build_46_histogram_read_frequencies_and_total_svg,
    "47_frequency_polygon_midpoints_and_interpretation_svg": build_47_frequency_polygon_midpoints_and_interpretation_svg,
    "48_symmetric_vs_skewed_histogram_identification_svg": build_48_symmetric_vs_skewed_histogram_identification_svg,
    "49_linear_transformation_of_summary_statistics_table": build_49_linear_transformation_of_summary_statistics_table,
    "50_statistics_diagnostic_autopsy_and_misconception_repair": build_50_statistics_diagnostic_autopsy_and_misconception_repair,
}
