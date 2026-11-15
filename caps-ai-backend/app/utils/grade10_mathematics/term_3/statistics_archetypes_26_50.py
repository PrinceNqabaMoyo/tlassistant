"""Grade 10 Mathematics — Term 3: Statistics Archetypes 26 to 50.
100% aligned with South African CAPS Curriculum (Grade 10 Mathematics: Statistics).
Covers:
- Box-and-whisker diagrams (reading 5-number summary, percentages, IQR, range)
- Skewness analysis (symmetrical, positively skewed, negatively skewed)
- Mean vs Median relationship under skewness
- Outlier detection via the 1.5 * IQR rule (fences and identification)
- Parallel box-and-whisker plot comparisons (medians, spread, performance)
- Histograms (reading frequencies, proportions, modal class, estimated mean)
- Frequency polygons (reading peaks, anchoring at zero)
- Stem-and-leaf displays (reading values, five-number summary)
- Cumulative frequency & percentile estimation
- Robustness of median vs mean under outliers
- Comprehensive statistical investigation
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

TOPIC = "Statistics"
TOPIC_ID = "grade10_math_statistics"
LO = "math10_statistics_measures"


def _fmt_dec(val: float | int, places: int = 2) -> str:
    """Format number with South African comma decimal."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _fmt_katex(val: float | int, places: int = 2) -> str:
    """Format number for KaTeX with {,} separator."""
    dec = _fmt_dec(val, places)
    return dec.replace(",", "{,}")


# -----------------------------------------------------------------------------
# SVG Generation Utilities for Publication-Grade Statistics Figures
# -----------------------------------------------------------------------------
def _make_box_plot_svg(
    min_v: int,
    q1: float | int,
    med: float | int,
    q3: float | int,
    max_v: int,
    axis_min: Optional[int] = None,
    axis_max: Optional[int] = None,
    title: str = "Data Distribution",
) -> str:
    """Generates an SVG box-and-whisker plot on a calibrated axis."""
    if axis_min is None:
        axis_min = max(0, int(min_v - 10))
    if axis_max is None:
        axis_max = int(max_v + 10)

    # Scale mapping: [axis_min, axis_max] -> [60, 460]
    span = max(1, axis_max - axis_min)

    def tx(val: float | int) -> float:
        return 60.0 + (float(val) - axis_min) * (400.0 / span)

    x_min = tx(min_v)
    x_q1 = tx(q1)
    x_med = tx(med)
    x_q3 = tx(q3)
    x_max = tx(max_v)

    # Ticks along axis
    tick_step = 10 if span <= 80 else 20
    first_tick = ((axis_min // tick_step) + 1) * tick_step
    ticks_svg = []
    curr = first_tick
    while curr < axis_max:
        cx = tx(curr)
        ticks_svg.append(f'<line x1="{cx:.1f}" y1="95" x2="{cx:.1f}" y2="103" stroke="#4A5568" stroke-width="1.5"/>')
        ticks_svg.append(f'<text x="{cx:.1f}" y="118" text-anchor="middle" font-size="11" fill="#4A5568">{curr}</text>')
        curr += tick_step

    ticks_str = "\n    ".join(ticks_svg)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 135" width="100%" height="auto" style="background:#FFFFFF; font-family:sans-serif;">
    <text x="260" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#1A202C">{title}</text>
    <!-- Number line axis -->
    <line x1="50" y1="95" x2="470" y2="95" stroke="#2D3748" stroke-width="2"/>
    <polygon points="475,95 465,91 465,99" fill="#2D3748"/>
    {ticks_str}
    <!-- Whiskers -->
    <line x1="{x_min:.1f}" y1="55" x2="{x_q1:.1f}" y2="55" stroke="#2B6CB0" stroke-width="2.5"/>
    <line x1="{x_q3:.1f}" y1="55" x2="{x_max:.1f}" y2="55" stroke="#2B6CB0" stroke-width="2.5"/>
    <!-- Min and Max endcaps -->
    <line x1="{x_min:.1f}" y1="42" x2="{x_min:.1f}" y2="68" stroke="#2B6CB0" stroke-width="2.5"/>
    <line x1="{x_max:.1f}" y1="42" x2="{x_max:.1f}" y2="68" stroke="#2B6CB0" stroke-width="2.5"/>
    <!-- Interquartile Box -->
    <rect x="{x_q1:.1f}" y="35" width="{max(2.0, x_q3 - x_q1):.1f}" height="40" fill="#EBF8FF" stroke="#2B6CB0" stroke-width="2.5"/>
    <!-- Median Line -->
    <line x1="{x_med:.1f}" y1="35" x2="{x_med:.1f}" y2="75" stroke="#C53030" stroke-width="3"/>
    <!-- Key value indicator labels -->
    <text x="{x_min:.1f}" y="32" text-anchor="middle" font-size="11" font-weight="bold" fill="#2B6CB0">{min_v}</text>
    <text x="{x_q1:.1f}" y="32" text-anchor="middle" font-size="11" font-weight="bold" fill="#2B6CB0">{_fmt_dec(q1)}</text>
    <text x="{x_med:.1f}" y="32" text-anchor="middle" font-size="11" font-weight="bold" fill="#C53030">{_fmt_dec(med)}</text>
    <text x="{x_q3:.1f}" y="32" text-anchor="middle" font-size="11" font-weight="bold" fill="#2B6CB0">{_fmt_dec(q3)}</text>
    <text x="{x_max:.1f}" y="32" text-anchor="middle" font-size="11" font-weight="bold" fill="#2B6CB0">{max_v}</text>
</svg>"""
    return svg


def _make_parallel_box_plot_svg(
    stats_a: Dict[str, Any],
    stats_b: Dict[str, Any],
    label_a: str = "Group A",
    label_b: str = "Group B",
) -> str:
    """Generates two parallel box-and-whisker plots sharing a single calibrated axis."""
    all_vals = [stats_a["min"], stats_a["max"], stats_b["min"], stats_b["max"]]
    axis_min = max(0, int(min(all_vals) - 10))
    axis_max = int(max(all_vals) + 10)
    span = max(1, axis_max - axis_min)

    def tx(val: float | int) -> float:
        return 90.0 + (float(val) - axis_min) * (370.0 / span)

    tick_step = 10 if span <= 80 else 20
    first_tick = ((axis_min // tick_step) + 1) * tick_step
    ticks_svg = []
    curr = first_tick
    while curr < axis_max:
        cx = tx(curr)
        ticks_svg.append(f'<line x1="{cx:.1f}" y1="165" x2="{cx:.1f}" y2="173" stroke="#4A5568" stroke-width="1.5"/>')
        ticks_svg.append(f'<text x="{cx:.1f}" y="188" text-anchor="middle" font-size="11" fill="#4A5568">{curr}</text>')
        curr += tick_step

    ticks_str = "\n    ".join(ticks_svg)

    # Plot A (y centered at 50)
    xa_min, xa_q1, xa_med, xa_q3, xa_max = tx(stats_a["min"]), tx(stats_a["q1"]), tx(stats_a["med"]), tx(stats_a["q3"]), tx(stats_a["max"])
    # Plot B (y centered at 115)
    xb_min, xb_q1, xb_med, xb_q3, xb_max = tx(stats_b["min"]), tx(stats_b["q1"]), tx(stats_b["med"]), tx(stats_b["q3"]), tx(stats_b["max"])

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 205" width="100%" height="auto" style="background:#FFFFFF; font-family:sans-serif;">
    <text x="260" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#1A202C">Comparison of Distributions</text>
    <!-- Axis -->
    <line x1="80" y1="165" x2="475" y2="165" stroke="#2D3748" stroke-width="2"/>
    <polygon points="480,165 470,161 470,169" fill="#2D3748"/>
    {ticks_str}
    <!-- Group A -->
    <text x="15" y="55" font-size="12" font-weight="bold" fill="#2B6CB0">{label_a}</text>
    <line x1="{xa_min:.1f}" y1="50" x2="{xa_q1:.1f}" y2="50" stroke="#2B6CB0" stroke-width="2"/>
    <line x1="{xa_q3:.1f}" y1="50" x2="{xa_max:.1f}" y2="50" stroke="#2B6CB0" stroke-width="2"/>
    <line x1="{xa_min:.1f}" y1="40" x2="{xa_min:.1f}" y2="60" stroke="#2B6CB0" stroke-width="2"/>
    <line x1="{xa_max:.1f}" y1="40" x2="{xa_max:.1f}" y2="60" stroke="#2B6CB0" stroke-width="2"/>
    <rect x="{xa_q1:.1f}" y="35" width="{max(2.0, xa_q3 - xa_q1):.1f}" height="30" fill="#EBF8FF" stroke="#2B6CB0" stroke-width="2"/>
    <line x1="{xa_med:.1f}" y1="35" x2="{xa_med:.1f}" y2="65" stroke="#C53030" stroke-width="2.5"/>

    <!-- Group B -->
    <text x="15" y="120" font-size="12" font-weight="bold" fill="#2F855A">{label_b}</text>
    <line x1="{xb_min:.1f}" y1="115" x2="{xb_q1:.1f}" y2="115" stroke="#2F855A" stroke-width="2"/>
    <line x1="{xb_q3:.1f}" y1="115" x2="{xb_max:.1f}" y2="115" stroke="#2F855A" stroke-width="2"/>
    <line x1="{xb_min:.1f}" y1="105" x2="{xb_min:.1f}" y2="125" stroke="#2F855A" stroke-width="2"/>
    <line x1="{xb_max:.1f}" y1="105" x2="{xb_max:.1f}" y2="125" stroke="#2F855A" stroke-width="2"/>
    <rect x="{xb_q1:.1f}" y="100" width="{max(2.0, xb_q3 - xb_q1):.1f}" height="30" fill="#F0FFF4" stroke="#2F855A" stroke-width="2"/>
    <line x1="{xb_med:.1f}" y1="100" x2="{xb_med:.1f}" y2="130" stroke="#C53030" stroke-width="2.5"/>
</svg>"""
    return svg


def _make_histogram_svg(bins: List[Tuple[int, int]], freqs: List[int], title: str = "Histogram of Marks") -> str:
    """Generates an SVG histogram with adjacent bars."""
    max_f = max(freqs)
    y_top = max(10, ((max_f // 5) + 1) * 5)
    bar_count = len(bins)
    x_start = 65.0
    total_w = 400.0
    bar_w = total_w / bar_count

    bars_svg = []
    ticks_x = [f'<line x1="{x_start:.1f}" y1="170" x2="{x_start:.1f}" y2="176" stroke="#4A5568" stroke-width="1.5"/>',
               f'<text x="{x_start:.1f}" y="190" text-anchor="middle" font-size="11" fill="#4A5568">{bins[0][0]}</text>']

    for i, ((low, high), f) in enumerate(zip(bins, freqs)):
        bx = x_start + i * bar_w
        bh = (f / y_top) * 130.0
        by = 170.0 - bh
        bars_svg.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_w:.1f}" height="{bh:.1f}" fill="#BEE3F8" stroke="#2B6CB0" stroke-width="2"/>')
        if f > 0:
            bars_svg.append(f'<text x="{bx + bar_w/2.0:.1f}" y="{by - 5:.1f}" text-anchor="middle" font-size="11" font-weight="bold" fill="#2B6CB0">{f}</text>')
        # x tick at right boundary
        rx = bx + bar_w
        ticks_x.append(f'<line x1="{rx:.1f}" y1="170" x2="{rx:.1f}" y2="176" stroke="#4A5568" stroke-width="1.5"/>')
        ticks_x.append(f'<text x="{rx:.1f}" y="190" text-anchor="middle" font-size="11" fill="#4A5568">{high}</text>')

    # Y ticks
    ticks_y = []
    y_step = 2 if y_top <= 10 else 5
    curr_y = 0
    while curr_y <= y_top:
        py = 170.0 - (curr_y / y_top) * 130.0
        ticks_y.append(f'<line x1="60" y1="{py:.1f}" x2="65" y2="{py:.1f}" stroke="#4A5568" stroke-width="1.5"/>')
        ticks_y.append(f'<text x="54" y="{py + 4:.1f}" text-anchor="end" font-size="11" fill="#4A5568">{curr_y}</text>')
        curr_y += y_step

    bars_str = "\n    ".join(bars_svg)
    tx_str = "\n    ".join(ticks_x)
    ty_str = "\n    ".join(ticks_y)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 215" width="100%" height="auto" style="background:#FFFFFF; font-family:sans-serif;">
    <text x="260" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#1A202C">{title}</text>
    <!-- Axes -->
    <line x1="65" y1="170" x2="480" y2="170" stroke="#2D3748" stroke-width="2"/>
    <line x1="65" y1="35" x2="65" y2="170" stroke="#2D3748" stroke-width="2"/>
    <polygon points="485,170 475,166 475,174" fill="#2D3748"/>
    <polygon points="65,30 61,40 69,40" fill="#2D3748"/>
    <text x="260" y="208" text-anchor="middle" font-size="11" fill="#4A5568">Class Intervals</text>
    <text x="18" y="100" text-anchor="middle" font-size="11" fill="#4A5568" transform="rotate(-90 18 100)">Frequency</text>
    {ty_str}
    {tx_str}
    {bars_str}
</svg>"""
    return svg


def _make_frequency_polygon_svg(midpoints: List[float], freqs: List[int], title: str = "Frequency Polygon") -> str:
    """Generates an SVG frequency polygon anchored to 0 on both ends."""
    step = midpoints[1] - midpoints[0]
    full_midpoints = [midpoints[0] - step] + list(midpoints) + [midpoints[-1] + step]
    full_freqs = [0] + list(freqs) + [0]

    max_f = max(freqs)
    y_top = max(10, ((max_f // 5) + 1) * 5)
    x_start = 65.0
    total_w = 400.0
    span_pts = len(full_midpoints) - 1

    def get_pt(i: int) -> Tuple[float, float]:
        px = x_start + i * (total_w / span_pts)
        py = 170.0 - (full_freqs[i] / y_top) * 130.0
        return px, py

    pts = [get_pt(i) for i in range(len(full_midpoints))]
    pts_str = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)

    dots_svg = []
    ticks_x = []
    for i, (m, f) in enumerate(zip(full_midpoints, full_freqs)):
        px, py = pts[i]
        dots_svg.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="#2B6CB0"/>')
        if f > 0:
            dots_svg.append(f'<text x="{px:.1f}" y="{py - 8:.1f}" text-anchor="middle" font-size="11" font-weight="bold" fill="#2B6CB0">{f}</text>')
        ticks_x.append(f'<line x1="{px:.1f}" y1="170" x2="{px:.1f}" y2="175" stroke="#4A5568" stroke-width="1.5"/>')
        ticks_x.append(f'<text x="{px:.1f}" y="190" text-anchor="middle" font-size="10" fill="#4A5568">{_fmt_dec(m)}</text>')

    ticks_y = []
    y_step = 2 if y_top <= 10 else 5
    curr_y = 0
    while curr_y <= y_top:
        py = 170.0 - (curr_y / y_top) * 130.0
        ticks_y.append(f'<line x1="60" y1="{py:.1f}" x2="65" y2="{py:.1f}" stroke="#4A5568" stroke-width="1.5"/>')
        ticks_y.append(f'<text x="54" y="{py + 4:.1f}" text-anchor="end" font-size="11" fill="#4A5568">{curr_y}</text>')
        curr_y += y_step

    dots_str = "\n    ".join(dots_svg)
    tx_str = "\n    ".join(ticks_x)
    ty_str = "\n    ".join(ticks_y)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 215" width="100%" height="auto" style="background:#FFFFFF; font-family:sans-serif;">
    <text x="260" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#1A202C">{title}</text>
    <!-- Axes -->
    <line x1="65" y1="170" x2="480" y2="170" stroke="#2D3748" stroke-width="2"/>
    <line x1="65" y1="35" x2="65" y2="170" stroke="#2D3748" stroke-width="2"/>
    <polygon points="485,170 475,166 475,174" fill="#2D3748"/>
    <polygon points="65,30 61,40 69,40" fill="#2D3748"/>
    <text x="260" y="208" text-anchor="middle" font-size="11" fill="#4A5568">Class Midpoints</text>
    <text x="18" y="100" text-anchor="middle" font-size="11" fill="#4A5568" transform="rotate(-90 18 100)">Frequency</text>
    {ty_str}
    {tx_str}
    <polyline points="{pts_str}" fill="none" stroke="#2B6CB0" stroke-width="2.5"/>
    {dots_str}
</svg>"""
    return svg


# -----------------------------------------------------------------------------
# 26. Box whisker read five number summary
# -----------------------------------------------------------------------------
def arch_26_box_whisker_read_five_number_summary(rng: random.Random) -> Dict[str, Any]:
    min_v = rng.randint(15, 30)
    q1 = min_v + rng.randint(8, 14)
    med = q1 + rng.randint(8, 14)
    q3 = med + rng.randint(8, 14)
    max_v = q3 + rng.randint(8, 16)

    svg = _make_box_plot_svg(min_v, q1, med, q3, max_v, title="Test Marks Distribution")

    prompt = (
        "A box-and-whisker plot summarizes the results of an exam:\n\n"
        "1. Write down the five-number summary values indicated on the plot: "
        "Minimum, Lower Quartile ($Q_1$), Median ($Q_2$), Upper Quartile ($Q_3$), and Maximum.\n"
        "2. State what value marks the 50th percentile."
    )

    worked = (
        "**1. Five-Number Summary:**\n"
        f"- Minimum = {min_v}\n"
        f"- Lower Quartile ($Q_1$) = {q1}\n"
        f"- Median ($Q_2$) = {med}\n"
        f"- Upper Quartile ($Q_3$) = {q3}\n"
        f"- Maximum = {max_v}\n\n"
        f"**2. 50th Percentile:** The median represents the 50th percentile, which is **{med}**."
    )

    ans = f"Min={min_v}, Q1={q1}, Med={med}, Q3={q3}, Max={max_v}"

    return {
        "id": f"g10_stat_26_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 5,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "26_box_whisker_read_five_number_summary",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct Minimum ({min_v}) and Maximum ({max_v})", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Correct Q1 ({q1}) and Q3 ({q3})", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": f"Correct Median Q2 = {med}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Read the left whisker tip, left box edge, median line, right box edge, and right whisker tip.",
            "2_concept": "The five points are Min, Q1, Median, Q3, Max.",
            "3_breakdown": f"Summary: Min={min_v}, Q1={q1}, Med={med}, Q3={q3}, Max={max_v}.",
        },
        "misconception_tags": ["box_plot_reading_key_values"],
    }


# -----------------------------------------------------------------------------
# 27. Box whisker read percentages
# -----------------------------------------------------------------------------
def arch_27_box_whisker_read_percentages(rng: random.Random) -> Dict[str, Any]:
    min_v = rng.randint(20, 35)
    q1 = min_v + 10
    med = q1 + 12
    q3 = med + 10
    max_v = q3 + 15

    svg = _make_box_plot_svg(min_v, q1, med, q3, max_v, title="Learner Scores")

    prompt = (
        "A box-and-whisker plot summarizes the scores of a class:\n\n"
        f"The five-number summary values are: Minimum = {min_v}, $Q_1 = {q1}$, "
        f"Median = {med}, $Q_3 = {q3}$, Maximum = {max_v}.\n\n"
        f"1. What percentage of learners scored below {q1}?\n"
        f"2. What percentage of learners scored between {q1} and {q3}?\n"
        f"3. What percentage of learners scored above {med}?"
    )

    worked = (
        f"**1. Below $Q_1$ ({q1}):** $Q_1$ marks the 25th percentile, so exactly **25%** scored below.\n\n"
        f"**2. Between $Q_1$ ({q1}) and $Q_3$ ({q3}):** The interquartile range contains exactly **50%** of the data.\n\n"
        f"**3. Above Median ({med}):** Exactly **50%** of the data lies above the median."
    )

    ans = "Below Q1: 25%, Middle: 50%, Above Median: 50%"

    return {
        "id": f"g10_stat_27_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "27_box_whisker_read_percentages",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Percentage below Q1 is 25%", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Percentage between Q1 and Q3 is 50%", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Percentage above median is 50%", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Each quartile interval (Min to Q1, Q1 to Med, Med to Q3, Q3 to Max) contains exactly 25% of the data.",
            "2_concept": "Quartiles divide the data into 4 equal quarters of 25% each.",
            "3_breakdown": "Below Q1 is 25%. Between Q1 and Q3 is 50%. Above median is 50%.",
        },
        "misconception_tags": ["quartile_percentage_misinterpretation"],
    }


# -----------------------------------------------------------------------------
# 28. Box whisker calculate IQR and range
# -----------------------------------------------------------------------------
def arch_28_box_whisker_calculate_iqr_and_range(rng: random.Random) -> Dict[str, Any]:
    min_v = rng.randint(10, 25)
    q1 = min_v + rng.randint(8, 15)
    med = q1 + rng.randint(6, 12)
    q3 = med + rng.randint(8, 15)
    max_v = q3 + rng.randint(10, 20)

    iqr = q3 - q1
    rng_val = max_v - min_v

    svg = _make_box_plot_svg(min_v, q1, med, q3, max_v, title="Distribution of Scores")

    prompt = (
        "A box-and-whisker plot summarizes the scores of a test:\n\n"
        f"The five summary points are {min_v}, {q1}, {med}, {q3}, and {max_v}.\n\n"
        "1. Calculate the range of the scores.\n"
        "2. Calculate the Interquartile Range (IQR).\n"
        "3. Which measure of spread is more resistant to extreme values?"
    )

    worked = (
        f"**1. Range:**\n"
        f"$$\\text{{Range}} = \\text{{Maximum}} - \\text{{Minimum}} = {max_v} - {min_v} = {rng_val}$$\n\n"
        f"**2. Interquartile Range (IQR):**\n"
        f"$$\\text{{IQR}} = Q_3 - Q_1 = {q3} - {q1} = {iqr}$$\n\n"
        f"**3. Resistance to extreme values:**\n"
        f"The **IQR** is more resistant because it only measures the spread of the middle 50% of the data "
        f"and is unaffected by unusually high or low extreme values."
    )

    ans = f"Range={rng_val}, IQR={iqr}"

    return {
        "id": f"g10_stat_28_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "28_box_whisker_calculate_iqr_and_range",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct Range ({rng_val})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct IQR ({iqr})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Statement that IQR is resistant to extreme values", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Range = Max - Min. IQR = Q3 - Q1.",
            "2_concept": "IQR measures the middle 50%, ignoring the extremes at the ends.",
            "3_breakdown": f"Range = {max_v} - {min_v} = {rng_val}. IQR = {q3} - {q1} = {iqr}.",
        },
        "misconception_tags": ["iqr_vs_range_formula_confusion"],
    }


# -----------------------------------------------------------------------------
# 29. Box whisker construct from raw data
# -----------------------------------------------------------------------------
def arch_29_box_whisker_construct_from_raw_data(rng: random.Random) -> Dict[str, Any]:
    n = 11
    raw = [rng.randint(20, 75) for _ in range(n)]
    sorted_d = sorted(raw)
    min_v = sorted_d[0]
    q1 = sorted_d[2]
    med = sorted_d[5]
    q3 = sorted_d[8]
    max_v = sorted_d[-1]

    raw_str = ", ".join(str(x) for x in raw)
    sorted_str = ", ".join(str(x) for x in sorted_d)
    svg = _make_box_plot_svg(min_v, q1, med, q3, max_v, title="Constructed Box Plot")

    prompt = (
        f"A group of {n} learners scored the following marks in an assignment:\n\n"
        f"$$\\{{{raw_str}\\}}$$\n\n"
        f"1. Order the data and determine the five-number summary.\n"
        f"2. Calculate the IQR.\n"
        f"3. Verify that the box-and-whisker plot accurately represents these five points."
    )

    iqr = q3 - q1
    worked = (
        f"**1. Ordered data:** [{sorted_str}]\n\n"
        f"**Five-Number Summary:**\n"
        f"- Minimum = {min_v}\n"
        f"- $Q_1$ = {q1}\n"
        f"- Median = {med}\n"
        f"- $Q_3$ = {q3}\n"
        f"- Maximum = {max_v}\n\n"
        f"**2. IQR:** $\\text{{IQR}} = {q3} - {q1} = {iqr}$"
    )

    ans = f"Min={min_v}, Q1={q1}, Med={med}, Q3={q3}, Max={max_v}, IQR={iqr}"

    return {
        "id": f"g10_stat_29_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 6,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "29_box_whisker_construct_from_raw_data",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Data sorted in ascending order", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Min ({min_v}) and Max ({max_v})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Median ({med})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Quartiles Q1 ({q1}) and Q3 ({q3})", "marks": 2, "editable": True},
                {"id": "mp_5", "desc": f"IQR ({iqr})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Sort the data to locate the 5 summary values, then compare with the plot.",
            "2_concept": "A box plot visually marks Min, Q1, Med, Q3, and Max.",
            "3_breakdown": f"Summary: Min={min_v}, Q1={q1}, Med={med}, Q3={q3}, Max={max_v}, IQR={iqr}.",
        },
        "misconception_tags": ["box_plot_construction_error"],
    }


# -----------------------------------------------------------------------------
# 30. Skewness identification symmetrical
# -----------------------------------------------------------------------------
def arch_30_skewness_identification_symmetrical(rng: random.Random) -> Dict[str, Any]:
    min_v = rng.randint(20, 35)
    whisker = rng.randint(12, 18)
    q1 = min_v + whisker
    half_box = rng.randint(8, 14)
    med = q1 + half_box
    q3 = med + half_box
    max_v = q3 + whisker

    svg = _make_box_plot_svg(min_v, q1, med, q3, max_v, title="Symmetrical Distribution")

    prompt = (
        "A box-and-whisker plot has the following summary statistics:\n\n"
        f"$$\\text{{Minimum}} = {min_v}, \\quad Q_1 = {q1}, \\quad \\text{{Median}} = {med}, \\quad Q_3 = {q3}, \\quad \\text{{Maximum}} = {max_v}$$\n\n"
        "1. Compare the distances $(Q_3 - \\text{Median})$ and $(\\text{Median} - Q_1)$.\n"
        "2. Compare the lengths of the left and right whiskers.\n"
        "3. Conclude whether the distribution is symmetrical, skewed to the right, or skewed to the left."
    )

    d_left = med - q1
    d_right = q3 - med
    w_left = q1 - min_v
    w_right = max_v - q3

    worked = (
        f"**1. Box distances:**\n"
        f"- Median $- Q_1 = {med} - {q1} = {d_left}$\n"
        f"- $Q_3 -$ Median $= {q3} - {med} = {d_right}$\n"
        f"Both distances are equal ({d_left}).\n\n"
        f"**2. Whisker lengths:**\n"
        f"- Left whisker: $Q_1 - \\text{{Min}} = {q1} - {min_v} = {w_left}$\n"
        f"- Right whisker: $\\text{{Max}} - Q_3 = {max_v} - {q3} = {w_right}$\n"
        f"Both whiskers are equal in length ({w_left}).\n\n"
        f"**3. Conclusion:**\n"
        f"The distribution is **symmetrical**."
    )

    return {
        "id": f"g10_stat_30_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": "symmetrical",
        "answer_latex": r"\text{symmetrical}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "30_skewness_identification_symmetrical",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct box distances comparison ({d_left} = {d_right})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct whisker lengths comparison ({w_left} = {w_right})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Correct conclusion (symmetrical)", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Compare the left half of the box with the right half, and compare both whiskers.",
            "2_concept": "When the median is centered and whiskers are equal, the distribution is symmetrical.",
            "3_breakdown": f"Med - Q1 = {d_left}, Q3 - Med = {d_right}. Whiskers = {w_left}. The distribution is symmetrical.",
        },
        "misconception_tags": ["skewness_symmetry_identification"],
    }


# -----------------------------------------------------------------------------
# 31. Skewness identification positive skew
# -----------------------------------------------------------------------------
def arch_31_skewness_identification_positive_skew(rng: random.Random) -> Dict[str, Any]:
    min_v = rng.randint(15, 25)
    q1 = min_v + 8
    med = q1 + 5
    q3 = med + 16
    max_v = q3 + rng.randint(25, 40)

    svg = _make_box_plot_svg(min_v, q1, med, q3, max_v, title="Positively Skewed Distribution")

    prompt = (
        "A box-and-whisker plot represents test marks:\n\n"
        f"$$\\text{{Minimum}} = {min_v}, \\quad Q_1 = {q1}, \\quad \\text{{Median}} = {med}, \\quad Q_3 = {q3}, \\quad \\text{{Maximum}} = {max_v}$$\n\n"
        "1. Calculate the distance $(Q_3 - \\text{Median})$ and the distance $(\\text{Median} - Q_1)$.\n"
        "2. State whether the distribution is positively skewed (skewed to the right) or negatively skewed (skewed to the left).\n"
        "3. Provide two mathematical reasons from the plot to justify your answer."
    )

    d_right = q3 - med
    d_left = med - q1
    w_right = max_v - q3
    w_left = q1 - min_v

    worked = (
        f"**1. Distances:**\n"
        f"- $Q_3 -$ Median $= {q3} - {med} = {d_right}$\n"
        f"- Median $- Q_1 = {med} - {q1} = {d_left}$\n\n"
        f"**2. Skewness:** **Positively skewed (skewed to the right)**.\n\n"
        f"**3. Justifications:**\n"
        f"1. $Q_3 - \\text{{Median}} ({d_right}) > \\text{{Median}} - Q_1 ({d_left})$, meaning the data is more spread out in the upper 50%.\n"
        f"2. The right whisker ({w_right}) is noticeably longer than the left whisker ({w_left})."
    )

    ans = "positively skewed (skewed right)"

    return {
        "id": f"g10_stat_31_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": r"\text{positively skewed (skewed right)}",
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "31_skewness_identification_positive_skew",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct distances: Q3 - Med = {d_right}, Med - Q1 = {d_left}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct skewness: positively skewed / right-skewed", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Reason 1: Q3 - Med > Med - Q1", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Reason 2: Right whisker longer than left whisker", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Look at which whisker is longer and which side of the box has more spread.",
            "2_concept": "A longer right tail (whisker) indicates positive skewness (skewed right).",
            "3_breakdown": f"Right whisker = {w_right}, left whisker = {w_left}. It is positively skewed.",
        },
        "misconception_tags": ["skewness_direction_inverted"],
    }


# -----------------------------------------------------------------------------
# 32. Skewness identification negative skew
# -----------------------------------------------------------------------------
def arch_32_skewness_identification_negative_skew(rng: random.Random) -> Dict[str, Any]:
    min_v = rng.randint(5, 15)
    q1 = min_v + rng.randint(25, 35)
    med = q1 + 14
    q3 = med + 5
    max_v = q3 + 6

    svg = _make_box_plot_svg(min_v, q1, med, q3, max_v, title="Negatively Skewed Distribution")

    prompt = (
        "A box-and-whisker plot represents test marks:\n\n"
        f"$$\\text{{Minimum}} = {min_v}, \\quad Q_1 = {q1}, \\quad \\text{{Median}} = {med}, \\quad Q_3 = {q3}, \\quad \\text{{Maximum}} = {max_v}$$\n\n"
        "1. Calculate the distance $(\\text{Median} - Q_1)$ and the distance $(Q_3 - \\text{Median})$.\n"
        "2. State whether the distribution is positively skewed or negatively skewed (skewed to the left).\n"
        "3. Provide two mathematical reasons from the plot to justify your answer."
    )

    d_left = med - q1
    d_right = q3 - med
    w_left = q1 - min_v
    w_right = max_v - q3

    worked = (
        f"**1. Distances:**\n"
        f"- Median $- Q_1 = {med} - {q1} = {d_left}$\n"
        f"- $Q_3 -$ Median $= {q3} - {med} = {d_right}$\n\n"
        f"**2. Skewness:** **Negatively skewed (skewed to the left)**.\n\n"
        f"**3. Justifications:**\n"
        f"1. $\\text{{Median}} - Q_1 ({d_left}) > Q_3 - \\text{{Median}} ({d_right})$.\n"
        f"2. The left whisker ({w_left}) is significantly longer than the right whisker ({w_right})."
    )

    ans = "negatively skewed (skewed left)"

    return {
        "id": f"g10_stat_32_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": r"\text{negatively skewed (skewed left)}",
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "32_skewness_identification_negative_skew",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct distances: Med - Q1 = {d_left}, Q3 - Med = {d_right}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct skewness: negatively skewed / left-skewed", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Reason 1: Med - Q1 > Q3 - Med", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Reason 2: Left whisker longer than right whisker", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Look at which whisker is longer and which side of the box has more spread.",
            "2_concept": "A longer left tail (whisker) indicates negative skewness (skewed left).",
            "3_breakdown": f"Left whisker = {w_left}, right whisker = {w_right}. It is negatively skewed.",
        },
        "misconception_tags": ["negative_skewness_identification_error"],
    }


# -----------------------------------------------------------------------------
# 33. Skewness mean vs median relationship
# -----------------------------------------------------------------------------
def arch_33_skewness_mean_vs_median_relationship(rng: random.Random) -> Dict[str, Any]:
    skew = rng.choice(["positive", "negative", "symmetrical"])
    if skew == "positive":
        med = rng.randint(45, 55)
        mean_v = med + rng.randint(6, 12)
        skew_str = "positively skewed (skewed to the right)"
        rel = f"\\text{{Mean}} ({mean_v}) > \\text{{Median}} ({med})"
    elif skew == "negative":
        med = rng.randint(55, 65)
        mean_v = med - rng.randint(6, 12)
        skew_str = "negatively skewed (skewed to the left)"
        rel = f"\\text{{Mean}} ({mean_v}) < \\text{{Median}} ({med})"
    else:
        med = rng.randint(50, 60)
        mean_v = med
        skew_str = "symmetrical"
        rel = f"\\text{{Mean}} ({mean_v}) \\approx \\text{{Median}} ({med})"

    prompt = (
        f"A statistical analysis of an exam yields a mean of {mean_v} and a median of {med}.\n\n"
        "1. State the relationship between the mean and median.\n"
        "2. Deduce the skewness of the distribution.\n"
        "3. Explain why extreme values pull the mean in the direction of the skew, while the median remains stable."
    )

    worked = (
        f"**1. Relationship:** ${rel}$\n\n"
        f"**2. Skewness:** The distribution is **{skew_str}**.\n\n"
        "**3. Explanation:**\n"
        "The mean takes every data value into account, so high extreme scores pull the mean upwards "
        "(or low scores pull it downwards). The median only depends on rank order and is resistant to extreme values."
    )

    return {
        "id": f"g10_stat_33_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": skew_str,
        "answer_latex": rf"\text{{{skew_str}}}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "33_skewness_mean_vs_median_relationship",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct inequality relation between mean and median", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct skewness conclusion ({skew_str})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Explanation of mean sensitivity vs median resistance", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "If Mean > Median, the distribution is skewed right. If Mean < Median, it is skewed left.",
            "2_concept": "The tail pulls the mean towards the extreme values.",
            "3_breakdown": f"Mean is {mean_v} and Median is {med}. Skewness is {skew_str}.",
        },
        "misconception_tags": ["mean_median_skewness_order_confusion"],
    }


# -----------------------------------------------------------------------------
# 34. Outliers 1.5 IQR rule fences
# -----------------------------------------------------------------------------
def arch_34_outliers_1_5_iqr_rule_fences(rng: random.Random) -> Dict[str, Any]:
    q1 = rng.randint(30, 50)
    iqr = rng.choice([16, 20, 24, 28])
    q3 = q1 + iqr

    fence_factor = 1.5 * iqr
    lower_fence = q1 - fence_factor
    upper_fence = q3 + fence_factor

    prompt = (
        f"A data set has a lower quartile $Q_1 = {q1}$ and an upper quartile $Q_3 = {q3}$.\n\n"
        f"1. Calculate the Interquartile Range (IQR).\n"
        f"2. Calculate $1{{,}}5 \\times \\text{{IQR}}$.\n"
        f"3. State the formulas for the lower fence and upper fence used to detect statistical outliers.\n"
        f"4. Calculate the lower fence and upper fence."
    )

    worked = (
        f"**1. Interquartile Range (IQR):**\n"
        f"$$\\text{{IQR}} = Q_3 - Q_1 = {q3} - {q1} = {iqr}$$\n\n"
        f"**2. Fence factor:**\n"
        f"$$1{{,}}5 \\times \\text{{IQR}} = 1{{,}}5 \\times {iqr} = {_fmt_katex(fence_factor)}$$\n\n"
        f"**3. Formulas:**\n"
        f"- $\\text{{Lower fence}} = Q_1 - 1{{,}}5 \\times \\text{{IQR}}$\n"
        f"- $\\text{{Upper fence}} = Q_3 + 1{{,}}5 \\times \\text{{IQR}}$\n\n"
        f"**4. Fence calculations:**\n"
        f"- $\\text{{Lower fence}} = {q1} - {_fmt_katex(fence_factor)} = {_fmt_katex(lower_fence)}$\n"
        f"- $\\text{{Upper fence}} = {q3} + {_fmt_katex(fence_factor)} = {_fmt_katex(upper_fence)}$"
    )

    ans = f"Lower fence={_fmt_dec(lower_fence)}, Upper fence={_fmt_dec(upper_fence)}"

    return {
        "id": f"g10_stat_34_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "34_outliers_1_5_iqr_rule_fences",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct IQR = {iqr}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct 1.5 * IQR = {_fmt_dec(fence_factor)}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Lower fence = {_fmt_dec(lower_fence)}", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Upper fence = {_fmt_dec(upper_fence)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Lower fence = Q1 - 1,5 * IQR; Upper fence = Q3 + 1,5 * IQR.",
            "2_concept": "Values outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR] are considered outliers.",
            "3_breakdown": f"IQR = {iqr}, 1.5*IQR = {_fmt_dec(fence_factor)}. Lower fence = {_fmt_dec(lower_fence)}, Upper fence = {_fmt_dec(upper_fence)}.",
        },
        "misconception_tags": ["outlier_fence_formula_error"],
    }


# -----------------------------------------------------------------------------
# 35. Outliers identification in dataset
# -----------------------------------------------------------------------------
def arch_35_outliers_identification_in_dataset(rng: random.Random) -> Dict[str, Any]:
    q1 = rng.randint(25, 40)
    iqr = 20
    q3 = q1 + iqr
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    outlier_low = int(lower_fence - rng.randint(4, 10))
    normal_val = q1 + 5
    outlier_high = int(upper_fence + rng.randint(5, 12))

    prompt = (
        f"A survey has quartiles $Q_1 = {q1}$ and $Q_3 = {q3}$.\n\n"
        f"Three candidate values from the survey are: {outlier_low}, {normal_val}, and {outlier_high}.\n\n"
        f"1. Calculate the lower and upper fences using the $1{{,}}5 \\times \\text{{IQR}}$ rule.\n"
        f"2. Test each candidate value against the fences.\n"
        f"3. State which of these candidate values are classified as statistical outliers."
    )

    worked = (
        f"**1. Fences:**\n"
        f"$$\\text{{IQR}} = {q3} - {q1} = {iqr}$$\n"
        f"$$1{{,}}5 \\times \\text{{IQR}} = 1{{,}}5 \\times {iqr} = 30$$\n"
        f"$$\\text{{Lower fence}} = {q1} - 30 = {lower_fence}$$\n"
        f"$$\\text{{Upper fence}} = {q3} + 30 = {upper_fence}$$\n\n"
        f"**2. Testing candidates:**\n"
        f"- {outlier_low} $< {lower_fence}$ (below lower fence $\\rightarrow$ **Outlier**)\n"
        f"- {normal_val} lies between {lower_fence} and {upper_fence} (not an outlier)\n"
        f"- {outlier_high} $> {upper_fence}$ (above upper fence $\\rightarrow$ **Outlier**)\n\n"
        f"**3. Outliers identified:** **{outlier_low} and {outlier_high}**."
    )

    ans = f"{outlier_low} and {outlier_high}"

    return {
        "id": f"g10_stat_35_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "35_outliers_identification_in_dataset",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct fences ({lower_fence} and {upper_fence})", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Testing candidate values against fences", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct identification of outliers ({ans})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Any value smaller than the lower fence or larger than the upper fence is an outlier.",
            "2_concept": "Check whether each candidate value falls outside the interval [Lower fence, Upper fence].",
            "3_breakdown": f"Fences are {lower_fence} and {upper_fence}. Outliers are {outlier_low} and {outlier_high}.",
        },
        "misconception_tags": ["outlier_testing_boundary_error"],
    }


# -----------------------------------------------------------------------------
# 36. Parallel box whisker comparison medians
# -----------------------------------------------------------------------------
def arch_36_parallel_box_whisker_comparison_medians(rng: random.Random) -> Dict[str, Any]:
    diff = rng.randint(6, 12)
    stats_a = {"min": 25, "q1": 40, "med": 55, "q3": 70, "max": 85}
    stats_b = {"min": 30, "q1": 45, "med": 55 + diff, "q3": 78, "max": 92}

    svg = _make_parallel_box_plot_svg(stats_a, stats_b, label_a="Class A", label_b="Class B")

    prompt = (
        "Two parallel box-and-whisker plots summarize the marks for Class A and Class B in the same examination:\n\n"
        f"- Class A: Minimum = {stats_a['min']}, $Q_1 = {stats_a['q1']}$, Median = {stats_a['med']}, $Q_3 = {stats_a['q3']}$, Maximum = {stats_a['max']}\n"
        f"- Class B: Minimum = {stats_b['min']}, $Q_1 = {stats_b['q1']}$, Median = {stats_b['med']}, $Q_3 = {stats_b['q3']}$, Maximum = {stats_b['max']}\n\n"
        "1. Write down the median for Class A and Class B.\n"
        "2. Which class had a higher median mark?\n"
        "3. Interpret what the higher median indicates about the typical performance of the two classes."
    )

    worked = (
        f"**1. Medians:**\n"
        f"- Class A Median = {stats_a['med']}\n"
        f"- Class B Median = {stats_b['med']}\n\n"
        f"**2. Higher median:** **Class B** ({stats_b['med']} vs {stats_a['med']}).\n\n"
        f"**3. Interpretation:**\n"
        f"On average (typically), Class B performed better than Class A because 50% of Class B scored {stats_b['med']} "
        f"or higher, compared to a median of only {stats_a['med']} in Class A."
    )

    ans = f"Class A={stats_a['med']}, Class B={stats_b['med']}, Class B higher"

    return {
        "id": f"g10_stat_36_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "36_parallel_box_whisker_comparison_medians",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"State medians: Class A = {stats_a['med']}, Class B = {stats_b['med']}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Identify Class B as having higher median", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Valid interpretation of typical performance", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Compare the central vertical lines in each box plot.",
            "2_concept": "The median represents the center or typical score of each class.",
            "3_breakdown": f"Medians are {stats_a['med']} and {stats_b['med']}. Class B performed better.",
        },
        "misconception_tags": ["box_plot_comparison_median_confusion"],
    }


# -----------------------------------------------------------------------------
# 37. Parallel box whisker comparison spread
# -----------------------------------------------------------------------------
def arch_37_parallel_box_whisker_comparison_spread(rng: random.Random) -> Dict[str, Any]:
    base_a = rng.randint(15, 25)
    stats_a = {
        "min": base_a,
        "q1": base_a + rng.randint(12, 16),
        "med": base_a + rng.randint(28, 35),
        "q3": base_a + rng.randint(50, 60),
        "max": base_a + rng.randint(68, 78),
    }  # larger spread
    base_b = base_a + rng.randint(10, 16)
    stats_b = {
        "min": base_b,
        "q1": base_b + rng.randint(8, 12),
        "med": base_b + rng.randint(15, 18),
        "q3": base_b + rng.randint(22, 26),
        "max": base_b + rng.randint(32, 38),
    }  # smaller spread (more consistent)

    iqr_a = stats_a["q3"] - stats_a["q1"]
    iqr_b = stats_b["q3"] - stats_b["q1"]
    rng_a = stats_a["max"] - stats_a["min"]
    rng_b = stats_b["max"] - stats_b["min"]

    svg = _make_parallel_box_plot_svg(stats_a, stats_b, label_a="School A", label_b="School B")

    prompt = (
        "Two parallel box-and-whisker plots summarize examination marks for School A and School B:\n\n"
        f"- School A: Minimum = {stats_a['min']}, $Q_1 = {stats_a['q1']}$, Median = {stats_a['med']}, $Q_3 = {stats_a['q3']}$, Maximum = {stats_a['max']}\n"
        f"- School B: Minimum = {stats_b['min']}, $Q_1 = {stats_b['q1']}$, Median = {stats_b['med']}, $Q_3 = {stats_b['q3']}$, Maximum = {stats_b['max']}\n\n"
        "1. Calculate the IQR for School A and School B.\n"
        "2. Calculate the range for School A and School B.\n"
        "3. Which school achieved more consistent marks? Justify your choice mathematically."
    )

    worked = (
        f"**1. Interquartile Range (IQR):**\n"
        f"- School A: $\\text{{IQR}} = {stats_a['q3']} - {stats_a['q1']} = {iqr_a}$\n"
        f"- School B: $\\text{{IQR}} = {stats_b['q3']} - {stats_b['q1']} = {iqr_b}$\n\n"
        f"**2. Range:**\n"
        f"- School A: $\\text{{Range}} = {stats_a['max']} - {stats_a['min']} = {rng_a}$\n"
        f"- School B: $\\text{{Range}} = {stats_b['max']} - {stats_b['min']} = {rng_b}$\n\n"
        f"**3. Consistency:**\n"
        f"**School B** achieved more consistent marks because both its IQR ({iqr_b}) and Range ({rng_b}) "
        f"are smaller than School A's ({iqr_a} and {rng_a}), indicating less variability/spread in marks."
    )

    ans = f"School A IQR={iqr_a}, School B IQR={iqr_b}, School B more consistent"

    return {
        "id": f"g10_stat_37_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "37_parallel_box_whisker_comparison_spread",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct IQRs: School A = {iqr_a}, School B = {iqr_b}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct Ranges: School A = {rng_a}, School B = {rng_b}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Identification of School B as more consistent", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Justification based on smaller IQR and range", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Consistency means less spread; calculate the IQR and range for each school.",
            "2_concept": "A smaller IQR and range indicate greater consistency (less spread).",
            "3_breakdown": f"School B has smaller IQR ({iqr_b} < {iqr_a}) and smaller range ({rng_b} < {rng_a}), so it is more consistent.",
        },
        "misconception_tags": ["consistency_iqr_inversion_error"],
    }


# -----------------------------------------------------------------------------
# 38. Parallel box whisker overall performance
# -----------------------------------------------------------------------------
def arch_38_parallel_box_whisker_overall_performance(rng: random.Random) -> Dict[str, Any]:
    base = rng.randint(20, 30)
    stats_m = {
        "min": base,
        "q1": base + rng.randint(14, 18),
        "med": base + rng.randint(28, 35),
        "q3": base + rng.randint(45, 52),
        "max": base + rng.randint(60, 68),
    }
    shift = rng.randint(8, 14)
    stats_f = {
        "min": stats_m["min"] + shift,
        "q1": stats_m["q1"] + shift,
        "med": stats_m["med"] + shift,
        "q3": stats_m["q3"] + shift,
        "max": min(100, stats_m["max"] + shift),
    }

    svg = _make_parallel_box_plot_svg(stats_m, stats_f, label_a="Boys", label_b="Girls")

    prompt = (
        "Two parallel box-and-whisker plots show the distribution of scores for Boys and Girls in a science test:\n\n"
        f"- Boys: Minimum = {stats_m['min']}, $Q_1 = {stats_m['q1']}$, Median = {stats_m['med']}, $Q_3 = {stats_m['q3']}$, Maximum = {stats_m['max']}\n"
        f"- Girls: Minimum = {stats_f['min']}, $Q_1 = {stats_f['q1']}$, Median = {stats_f['med']}, $Q_3 = {stats_f['q3']}$, Maximum = {stats_f['max']}\n\n"
        "1. Compare the medians of both groups.\n"
        f"2. What percentage of Girls scored above the Boys' median ({stats_m['med']})?\n"
        "3. Provide an overall conclusion comparing the performance of the two groups."
    )

    diff_med = stats_f['med'] - stats_m['med']
    worked = (
        f"**1. Median Comparison:**\n"
        f"- Girls' median ({stats_f['med']}) is {diff_med} marks higher than Boys' median ({stats_m['med']}).\n\n"
        f"**2. Percentage above {stats_m['med']}:**\n"
        f"Since the Girls' lower quartile $Q_1$ is {stats_f['q1']} (which is close to or below {stats_m['med']}), "
        f"approximately **75%** of the girls scored above {stats_f['q1']}, meaning more than 50% "
        f"of the girls scored higher than the boys' median.\n\n"
        f"**3. Overall conclusion:**\n"
        f"The Girls outperformed the Boys overall, having higher values across all five summary points (Min, Q1, Median, Q3, Max)."
    )

    ans = "Girls outperformed Boys overall"

    return {
        "id": f"g10_stat_38_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "38_parallel_box_whisker_overall_performance",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct median comparison (Girls {stats_f['med']} > Boys {stats_m['med']})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Interpretation of quartile overlap", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Valid conclusion that Girls outperformed Boys", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Compare the positions of the medians and quartiles of both groups.",
            "2_concept": "When all five points of one group are shifted higher, that group performed better overall.",
            "3_breakdown": f"Girls median {stats_f['med']} > Boys median {stats_m['med']}. Girls performed higher overall.",
        },
        "misconception_tags": ["distribution_comparison_overlap_error"],
    }


# -----------------------------------------------------------------------------
# 39. Histogram reading frequencies
# -----------------------------------------------------------------------------
def arch_39_histogram_reading_frequencies(rng: random.Random) -> Dict[str, Any]:
    bins = [(10, 20), (20, 30), (30, 40), (40, 50), (50, 60)]
    freqs = [rng.randint(3, 10) for _ in bins]

    svg = _make_histogram_svg(bins, freqs, title="Class Test Mark Frequencies")

    target_idx = rng.randint(1, 3)
    target_bin = bins[target_idx]
    target_f = freqs[target_idx]

    prompt = (
        "A histogram displays the test results of a group of learners:\n\n"
        f"The mark intervals are 10-20, 20-30, 30-40, 40-50, and 50-60.\n\n"
        f"1. Read the frequency for the mark interval ${target_bin[0]} \\le x < {target_bin[1]}$.\n"
        "2. State why there are no gaps between the bars in a histogram."
    )

    worked = (
        f"**1. Frequency for ${target_bin[0]} \\le x < {target_bin[1]}$:**\n"
        f"The bar corresponding to the interval ${target_bin[0]} \\le x < {target_bin[1]}$ has a height of **{target_f}**.\n\n"
        f"**2. No gaps explanation:**\n"
        f"There are no gaps between bars because the data represented is **continuous** (each interval starts "
        f"immediately where the previous one ends)."
    )

    ans = f"Frequency={target_f}, Continuous data"

    return {
        "id": f"g10_stat_39_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(target_f),
        "answer_latex": str(target_f),
        "worked_solution": worked,
        "marks": 2,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "39_histogram_reading_frequencies",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 2,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct frequency ({target_f})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Valid reason: continuous data has no gaps", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Read the height of the bar on the vertical axis.",
            "2_concept": "In a histogram, bar heights represent frequencies for continuous class intervals.",
            "3_breakdown": f"Height for {target_bin[0]}-{target_bin[1]} is {target_f}.",
        },
        "misconception_tags": ["histogram_bar_graph_confusion"],
    }


# -----------------------------------------------------------------------------
# 40. Histogram total frequency and proportions
# -----------------------------------------------------------------------------
def arch_40_histogram_total_frequency_and_proportions(rng: random.Random) -> Dict[str, Any]:
    bins = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50)]
    freqs = [rng.randint(4, 9) for _ in bins]
    total_n = sum(freqs)

    svg = _make_histogram_svg(bins, freqs, title="Assignment Marks Histogram")

    target_f = freqs[3] + freqs[4]  # learners scoring >= 30
    pct = (target_f / total_n) * 100.0
    pct_str = _fmt_katex(pct)

    prompt = (
        "A histogram displays the scores of learners:\n\n"
        f"The frequencies for the 5 intervals are: {freqs[0]}, {freqs[1]}, {freqs[2]}, {freqs[3]}, and {freqs[4]}.\n\n"
        "1. Calculate the total number of learners surveyed ($n$).\n"
        "2. How many learners scored 30 marks or higher?\n"
        "3. Calculate the percentage of learners who scored 30 marks or higher, rounded to one decimal place."
    )

    worked = (
        f"**1. Total learners ($n$):**\n"
        f"$$n = {freqs[0]} + {freqs[1]} + {freqs[2]} + {freqs[3]} + {freqs[4]} = {total_n}$$\n\n"
        f"**2. Learners scoring $\\ge 30$:**\n"
        f"Add the frequencies for intervals 30-40 and 40-50:\n"
        f"$$\\text{{Count}} = {freqs[3]} + {freqs[4]} = {target_f}$$\n\n"
        f"**3. Percentage:**\n"
        f"$$\\text{{Percentage}} = \\frac{{{target_f}}}{{{total_n}}} \\times 100\\% = {pct_str}\\%$$"
    )

    ans = f"Total={total_n}, Count={target_f}, Pct={_fmt_dec(pct)}%"

    return {
        "id": f"g10_stat_40_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "40_histogram_total_frequency_and_proportions",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct total frequency n = {total_n}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct count >= 30 ({target_f})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Percentage calculation ({_fmt_dec(pct)}%)", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Add all bar frequencies together to get the total, then divide the target bars by the total.",
            "2_concept": "Proportion = (sum of target bars) / (total frequency).",
            "3_breakdown": f"Total = {total_n}, target count = {target_f}, percentage = {_fmt_dec(pct)}%.",
        },
        "misconception_tags": ["histogram_total_frequency_sum_error"],
    }


# -----------------------------------------------------------------------------
# 41. Histogram modal class identification
# -----------------------------------------------------------------------------
def arch_41_histogram_modal_class_identification(rng: random.Random) -> Dict[str, Any]:
    bins = [(10, 20), (20, 30), (30, 40), (40, 50), (50, 60)]
    freqs = [rng.randint(3, 7) for _ in bins]
    modal_idx = rng.randint(1, 3)
    freqs[modal_idx] = max(freqs) + rng.randint(4, 8)

    svg = _make_histogram_svg(bins, freqs, title="Test Performance")
    modal_bin = bins[modal_idx]

    prompt = (
        "A histogram displays test marks across five intervals:\n\n"
        f"The frequencies are: {freqs[0]}, {freqs[1]}, {freqs[2]}, {freqs[3]}, and {freqs[4]}.\n\n"
        "1. Identify the modal class interval from the histogram.\n"
        "2. State the frequency of the modal class.\n"
        "3. Explain why the tallest bar identifies the modal class."
    )

    worked = (
        f"**1. Modal class:** **${modal_bin[0]} \\le x < {modal_bin[1]}$**\n\n"
        f"**2. Modal frequency:** **{freqs[modal_idx]}**\n\n"
        f"**3. Explanation:**\n"
        f"The modal class is the interval containing the greatest frequency, which corresponds "
        f"directly to the tallest bar in the histogram."
    )

    ans = f"{modal_bin[0]} <= x < {modal_bin[1]}"

    return {
        "id": f"g10_stat_41_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": rf"{modal_bin[0]} \le x < {modal_bin[1]}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "41_histogram_modal_class_identification",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct modal class ({ans})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct frequency ({freqs[modal_idx]})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Reason based on tallest bar / greatest frequency", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Find the tallest bar in the histogram.",
            "2_concept": "The tallest bar has the highest frequency and corresponds to the modal class.",
            "3_breakdown": f"Tallest bar is at {modal_bin[0]}-{modal_bin[1]} with frequency {freqs[modal_idx]}.",
        },
        "misconception_tags": ["modal_class_bar_height_reading_error"],
    }


# -----------------------------------------------------------------------------
# 42. Histogram estimate mean from visual
# -----------------------------------------------------------------------------
def arch_42_histogram_estimate_mean_from_visual(rng: random.Random) -> Dict[str, Any]:
    bins = [(0, 10), (10, 20), (20, 30), (30, 40)]
    freqs = [rng.randint(3, 8) for _ in bins]
    midpoints = [(low + high) / 2.0 for low, high in bins]
    fm = [f * m for f, m in zip(freqs, midpoints)]

    sum_f = sum(freqs)
    sum_fm = sum(fm)
    est_mean = sum_fm / sum_f
    est_mean_str = _fmt_katex(est_mean)

    svg = _make_histogram_svg(bins, freqs, title="Weekly Travel Times")

    prompt = (
        "A histogram shows travel times across four intervals:\n\n"
        f"The intervals are 0-10, 10-20, 20-30, and 30-40 with frequencies "
        f"{freqs[0]}, {freqs[1]}, {freqs[2]}, and {freqs[3]}.\n\n"
        "1. Write down the midpoint ($m$) for each of the four bars.\n"
        "2. Calculate $\\sum f$ and $\\sum (f \\times m)$.\n"
        "3. Calculate the estimated mean travel time."
    )

    worked = (
        "**1. Midpoints:**\n"
        + "\n".join(f"- {low}-{high}: $m = {_fmt_katex(m)}$" for (low, high), m in zip(bins, midpoints))
        + f"\n\n**2. Totals:**\n"
        f"- $\\sum f = {sum_f}$\n"
        f"- $\\sum (f \\times m) = {_fmt_katex(sum_fm)}$\n\n"
        f"**3. Estimated Mean:**\n"
        f"$$\\bar{{x}} \\approx \\frac{{{_fmt_katex(sum_fm)}}}{{{sum_f}}} = {est_mean_str}$$"
    )

    return {
        "id": f"g10_stat_42_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_dec(est_mean),
        "answer_latex": rf"\bar{{x}} \approx {est_mean_str}",
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "42_histogram_estimate_mean_from_visual",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct midpoints for all 4 bars", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct sum of f ({sum_f})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct sum of fm ({_fmt_dec(sum_fm)})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Correct estimated mean quotient ({_fmt_dec(est_mean)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Multiply each bar's midpoint by its frequency, sum them, and divide by the total frequency.",
            "2_concept": "Estimated mean = sum(f * m) / sum(f).",
            "3_breakdown": f"sum(f) = {sum_f}, sum(fm) = {_fmt_dec(sum_fm)}. Estimated mean = {_fmt_dec(est_mean)}.",
        },
        "misconception_tags": ["histogram_estimated_mean_calculation_error"],
    }


# -----------------------------------------------------------------------------
# 43. Frequency polygon read class peaks
# -----------------------------------------------------------------------------
def arch_43_frequency_polygon_read_class_peaks(rng: random.Random) -> Dict[str, Any]:
    midpoints = [15.0, 25.0, 35.0, 45.0, 55.0]
    freqs = [rng.randint(3, 6) for _ in midpoints]
    peak_idx = rng.randint(1, 3)
    freqs[peak_idx] = max(freqs) + rng.randint(4, 7)

    svg = _make_frequency_polygon_svg(midpoints, freqs, title="Frequency Polygon of Test Results")
    peak_m = midpoints[peak_idx]

    prompt = (
        "A frequency polygon displays the test results for Grade 10 learners:\n\n"
        f"The plotted midpoints are 15, 25, 35, 45, and 55 with frequencies "
        f"{freqs[0]}, {freqs[1]}, {freqs[2]}, {freqs[3]}, and {freqs[4]}.\n\n"
        "1. Identify the class midpoint corresponding to the peak of the polygon.\n"
        "2. State the maximum frequency at this peak.\n"
        "3. If the class interval width is 10, write down the interval represented by this peak midpoint."
    )

    low = int(peak_m - 5)
    high = int(peak_m + 5)
    worked = (
        f"**1. Peak Midpoint:** $m = {_fmt_katex(peak_m)}$\n\n"
        f"**2. Maximum Frequency:** **{freqs[peak_idx]}**\n\n"
        f"**3. Class Interval:**\n"
        f"With width 10, the interval centered at {peak_m} is **${low} \\le x < {high}$**."
    )

    ans = f"Midpoint={_fmt_dec(peak_m)}, Freq={freqs[peak_idx]}, Interval={low} <= x < {high}"

    return {
        "id": f"g10_stat_43_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "43_frequency_polygon_read_class_peaks",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct peak midpoint ({_fmt_dec(peak_m)})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct peak frequency ({freqs[peak_idx]})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct interval ({low} <= x < {high})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Find the highest point on the polygon line and read its x and y coordinates.",
            "2_concept": "The peak of a frequency polygon represents the class midpoint with the greatest frequency.",
            "3_breakdown": f"Peak at midpoint {_fmt_dec(peak_m)} with frequency {freqs[peak_idx]}. Interval is {low}-{high}.",
        },
        "misconception_tags": ["frequency_polygon_peak_misread"],
    }


# -----------------------------------------------------------------------------
# 44. Frequency polygon anchoring concept
# -----------------------------------------------------------------------------
def arch_44_frequency_polygon_anchoring_concept(rng: random.Random) -> Dict[str, Any]:
    midpoints = [20.0, 30.0, 40.0, 50.0]
    freqs = [rng.randint(3, 8) for _ in midpoints]

    svg = _make_frequency_polygon_svg(midpoints, freqs, title="Anchored Frequency Polygon")

    prompt = (
        "A frequency polygon is constructed from grouped data with midpoints 20, 30, 40, and 50:\n\n"
        f"The frequencies are {freqs[0]}, {freqs[1]}, {freqs[2]}, and {freqs[3]}.\n\n"
        "1. Identify the midpoints of the two anchoring points on the horizontal axis where the frequency is 0.\n"
        "2. Explain why a frequency polygon must be anchored to the horizontal axis at both ends."
    )

    step = 10
    left_anchor = midpoints[0] - step
    right_anchor = midpoints[-1] + step

    worked = (
        f"**1. Anchoring Midpoints:**\n"
        f"- Left anchor: ${midpoints[0]} - {step} = {_fmt_katex(left_anchor)}$\n"
        f"- Right anchor: ${midpoints[-1]} + {step} = {_fmt_katex(right_anchor)}$\n\n"
        f"**2. Mathematical explanation:**\n"
        f"Anchoring closes the polygon and ensures that the total area under the frequency polygon "
        f"is equal to the total area of the corresponding histogram (which represents the total frequency $n$)."
    )

    ans = f"Left={_fmt_dec(left_anchor)}, Right={_fmt_dec(right_anchor)}"

    return {
        "id": f"g10_stat_44_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "44_frequency_polygon_anchoring_concept",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct left anchor ({_fmt_dec(left_anchor)})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct right anchor ({_fmt_dec(right_anchor)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Explanation: area under curve equals total frequency / closes shape", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Go one step below the first midpoint and one step above the last midpoint.",
            "2_concept": "Anchoring creates a closed polygon whose area equals the histogram area.",
            "3_breakdown": f"Anchors are at {_fmt_dec(left_anchor)} and {_fmt_dec(right_anchor)}.",
        },
        "misconception_tags": ["frequency_polygon_anchoring_omission"],
    }


# -----------------------------------------------------------------------------
# 45. Stem and leaf read data values
# -----------------------------------------------------------------------------
def arch_45_stem_and_leaf_read_data_values(rng: random.Random) -> Dict[str, Any]:
    stems = [2, 3, 4]
    leaves_by_stem = {
        2: sorted([rng.randint(1, 9) for _ in range(3)]),
        3: sorted([rng.randint(0, 9) for _ in range(4)]),
        4: sorted([rng.randint(0, 8) for _ in range(3)]),
    }

    raw_values: List[int] = []
    rows = []
    for s in stems:
        l_str = " ".join(str(x) for x in leaves_by_stem[s])
        rows.append(f"| {s} | {l_str} |")
        for leaf in leaves_by_stem[s]:
            raw_values.append(s * 10 + leaf)

    total_n = len(raw_values)
    rows_str = "\n".join(rows)

    prompt = (
        "The following stem-and-leaf display shows test marks for a group of learners:\n\n"
        "| Stem | Leaves |\n"
        "| :--- | :--- |\n"
        f"{rows_str}\n\n"
        "**Key:** $2 \\mid 4 = 24$ marks\n\n"
        "1. How many learners took the test?\n"
        "2. List all the data values in ascending order.\n"
        "3. State the minimum and maximum scores recorded."
    )

    vals_str = ", ".join(str(x) for x in raw_values)
    worked = (
        f"**1. Total learners ($n$):** Counting all leaves gives $n = {total_n}$.\n\n"
        f"**2. Data values in ascending order:**\n"
        f"[{vals_str}]\n\n"
        f"**3. Extremes:**\n"
        f"- Minimum = {raw_values[0]}\n"
        f"- Maximum = {raw_values[-1]}"
    )

    ans = f"n={total_n}, Min={raw_values[0]}, Max={raw_values[-1]}"

    return {
        "id": f"g10_stat_45_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "45_stem_and_leaf_read_data_values",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct total count n = {total_n}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct ordered list of values", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct Min ({raw_values[0]}) and Max ({raw_values[-1]})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Combine each stem with each leaf to reconstruct the two-digit numbers.",
            "2_concept": "The key 2 | 4 = 24 tells you that the stem represents tens and the leaf represents units.",
            "3_breakdown": f"Total values = {total_n}, Min = {raw_values[0]}, Max = {raw_values[-1]}.",
        },
        "misconception_tags": ["stem_and_leaf_key_misinterpretation"],
    }


# -----------------------------------------------------------------------------
# 46. Stem and leaf five number summary
# -----------------------------------------------------------------------------
def arch_46_stem_and_leaf_five_number_summary(rng: random.Random) -> Dict[str, Any]:
    stems = [1, 2, 3, 4]
    leaves_by_stem = {
        1: [2, 5],
        2: [1, 4, 8],
        3: [2, 5, 7],
        4: [0, 3, 6],
    }
    raw_values: List[int] = []
    rows = []
    for s in stems:
        l_str = " ".join(str(x) for x in leaves_by_stem[s])
        rows.append(f"| {s} | {l_str} |")
        for leaf in leaves_by_stem[s]:
            raw_values.append(s * 10 + leaf)

    n = len(raw_values)  # 11 values
    min_v = raw_values[0]
    max_v = raw_values[-1]
    med = raw_values[5]
    q1 = raw_values[2]
    q3 = raw_values[8]
    iqr = q3 - q1

    rows_str = "\n".join(rows)

    prompt = (
        "The following stem-and-leaf plot displays 11 test marks:\n\n"
        "| Stem | Leaves |\n"
        "| :--- | :--- |\n"
        f"{rows_str}\n\n"
        "**Key:** $1 \\mid 2 = 12$\n\n"
        "1. Write down the five-number summary values directly from the display.\n"
        "2. Calculate the Interquartile Range (IQR)."
    )

    worked = (
        "**1. Five-Number Summary:**\n"
        f"- Minimum = {min_v}\n"
        f"- $Q_1$ (3rd value) = {q1}\n"
        f"- Median (6th value) = {med}\n"
        f"- $Q_3$ (9th value) = {q3}\n"
        f"- Maximum = {max_v}\n\n"
        f"**2. Interquartile Range:**\n"
        f"$$\\text{{IQR}} = Q_3 - Q_1 = {q3} - {q1} = {iqr}$$"
    )

    ans = f"Min={min_v}, Q1={q1}, Med={med}, Q3={q3}, Max={max_v}, IQR={iqr}"

    return {
        "id": f"g10_stat_46_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 5,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "46_stem_and_leaf_five_number_summary",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": f"Min ({min_v}) and Max ({max_v})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Median ({med})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Quartiles Q1 ({q1}) and Q3 ({q3})", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": f"IQR ({iqr})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Because the leaves are already ordered, you can count positions directly to find quartiles and median.",
            "2_concept": "Count leaves from top to bottom: 3rd leaf is Q1, 6th is Median, 9th is Q3.",
            "3_breakdown": f"Min={min_v}, Q1={q1}, Med={med}, Q3={q3}, Max={max_v}, IQR={iqr}.",
        },
        "misconception_tags": ["stem_and_leaf_positional_counting_error"],
    }


# -----------------------------------------------------------------------------
# 47. Grouped data cumulative frequency table
# -----------------------------------------------------------------------------
def arch_47_grouped_data_cumulative_frequency_table(rng: random.Random) -> Dict[str, Any]:
    intervals = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50)]
    freqs = [rng.randint(3, 8) for _ in intervals]
    cum_f: List[int] = []
    run = 0
    for f in freqs:
        run += f
        cum_f.append(run)

    rows = "\n".join(f"| ${low} \\le x < {high}$ | {f} |" for (low, high), f in zip(intervals, freqs))

    prompt = (
        "The following frequency table shows the marks of learners in a test:\n\n"
        "| Interval | Frequency ($f$) |\n"
        "| :--- | :--- |\n"
        f"{rows}\n\n"
        "1. Complete a cumulative frequency table for the data.\n"
        "2. State the total number of learners ($n$).\n"
        "3. How many learners scored less than 30 marks?"
    )

    worked_rows = "\n".join(f"| ${low} \\le x < {high}$ | {f} | {cf} |" for (low, high), f, cf in zip(intervals, freqs, cum_f))
    less_than_30 = cum_f[2]
    worked = (
        "**1. Cumulative Frequency Table:**\n\n"
        "| Interval | Frequency ($f$) | Cumulative Frequency |\n"
        "| :--- | :--- | :--- |\n"
        f"{worked_rows}\n\n"
        f"**2. Total learners:** $n = {cum_f[-1]}$\n\n"
        f"**3. Learners scoring less than 30 marks:**\n"
        f"Looking at the upper boundary 30, the cumulative frequency is **{less_than_30}**."
    )

    ans = f"Total={cum_f[-1]}, Less than 30={less_than_30}"

    return {
        "id": f"g10_stat_47_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "47_grouped_data_cumulative_frequency_table",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Accurate cumulative frequencies across all rows", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Correct total n = {cum_f[-1]}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct count scoring < 30 ({less_than_30})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Add each row's frequency to the running total from the row above.",
            "2_concept": "Cumulative frequency is the running total of frequencies up to that interval.",
            "3_breakdown": f"Cumulative values: {cum_f}. Total = {cum_f[-1]}. Less than 30 = {less_than_30}.",
        },
        "misconception_tags": ["cumulative_frequency_addition_error"],
    }


# -----------------------------------------------------------------------------
# 48. Grouped data percentile estimation
# -----------------------------------------------------------------------------
def arch_48_grouped_data_percentile_estimation(rng: random.Random) -> Dict[str, Any]:
    intervals = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50)]
    freqs = [6, 12, 18, 14, 10]
    cum_f = [6, 18, 36, 50, 60]
    total_n = 60

    rows = "\n".join(f"| ${low} \\le x < {high}$ | {f} | {cf} |" for (low, high), f, cf in zip(intervals, freqs, cum_f))

    prompt = (
        "The cumulative frequency table summarizes the results of 60 learners in a test:\n\n"
        "| Mark Interval | Frequency ($f$) | Cumulative Frequency |\n"
        "| :--- | :--- | :--- |\n"
        f"{rows}\n\n"
        "1. State the position of the 25th percentile ($Q_1$) using $\\frac{25}{100} \\times 60$.\n"
        "2. Identify the class interval containing the 25th percentile ($Q_1$).\n"
        "3. Identify the class interval containing the 75th percentile ($Q_3$)."
    )

    pos_25 = int(0.25 * total_n)  # 15
    pos_75 = int(0.75 * total_n)  # 45

    int_25 = "$10 \\le x < 20$"  # cum_f goes from 6 to 18
    int_75 = "$30 \\le x < 40$"  # cum_f goes from 36 to 50

    worked = (
        f"**1. Position of $Q_1$:**\n"
        f"$$\\text{{Position}} = \\frac{{25}}{{100}} \\times 60 = {pos_25}\\text{{th learner}}$$\n\n"
        f"**2. Class interval for $Q_1$:**\n"
        f"The {pos_25}th learner falls in **{int_25}** (since cumulative frequency reaches 18 $\\ge {pos_25}$).\n\n"
        f"**3. Class interval for $Q_3$:**\n"
        f"Position: $\\frac{{75}}{{100}} \\times 60 = {pos_75}$th learner.\n"
        f"The {pos_75}th learner falls in **{int_75}** (since cumulative frequency reaches 50 $\\ge {pos_75}$)."
    )

    ans = f"Q1 interval: {int_25}, Q3 interval: {int_75}"

    return {
        "id": f"g10_stat_48_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "48_grouped_data_percentile_estimation",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct position of Q1 ({pos_25}th)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct interval for Q1 ({int_25})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct interval for Q3 ({int_75})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Find 25% of 60 (15) and 75% of 60 (45), then see which cumulative frequency rows contain them.",
            "2_concept": "Use cumulative frequencies to locate percentile intervals.",
            "3_breakdown": f"15th position is in {int_25}. 45th position is in {int_75}.",
        },
        "misconception_tags": ["percentile_interval_lookup_error"],
    }


# -----------------------------------------------------------------------------
# 49. Data cleaning and impact of extreme values
# -----------------------------------------------------------------------------
def arch_49_data_cleaning_and_impact_of_extreme_values(rng: random.Random) -> Dict[str, Any]:
    base_salaries = [12000, 14000, 15000, 16000, 18000]
    outlier_ceo = 150000
    all_salaries = base_salaries + [outlier_ceo]

    mean_without = sum(base_salaries) / len(base_salaries)
    med_without = base_salaries[2]

    mean_with = sum(all_salaries) / len(all_salaries)
    med_with = (all_salaries[2] + all_salaries[3]) / 2.0

    prompt = (
        "A small company has five employees earning monthly salaries:\n\n"
        "$$\\{R12\\,000, \\quad R14\\,000, \\quad R15\\,000, \\quad R16\\,000, \\quad R18\\,000\\}$$\n\n"
        f"A new CEO joins the company earning R{outlier_ceo:,}. The updated salary list is:\n\n"
        f"$$\\{{R12\\,000, \\quad R14\\,000, \\quad R15\\,000, \\quad R16\\,000, \\quad R18\\,000, \\quad R150\\,000\\}}$$\n\n"
        "1. Calculate the mean and median salary before the CEO joined.\n"
        "2. Calculate the mean and median salary after the CEO joined.\n"
        "3. Which measure of central tendency provides a more realistic representation of typical employee earnings? Explain why."
    )

    worked = (
        f"**1. Before CEO:**\n"
        f"- $\\text{{Mean}} = \\frac{{{sum(base_salaries)}}}{{5}} = R{int(mean_without):,}$\n"
        f"- $\\text{{Median}} = R{med_without:,}$\n\n"
        f"**2. After CEO:**\n"
        f"- $\\text{{Mean}} = \\frac{{{sum(all_salaries)}}}{{6}} = R{int(mean_with):,}$\n"
        f"- $\\text{{Median}} = \\frac{{15\\,000 + 16\\,000}}{{2}} = R{int(med_with):,}$\n\n"
        f"**3. Evaluation:**\n"
        f"The **Median** (R{int(med_with):,}) is much more realistic. The extreme salary of R{outlier_ceo:,} "
        f"drastically inflates the mean to R{int(mean_with):,}, which is higher than what 5 out of 6 employees earn. "
        f"The median is resistant to outliers."
    )

    ans = "Median is more realistic because it is resistant to extreme outliers"

    return {
        "id": f"g10_stat_49_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 5,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "49_data_cleaning_and_impact_of_extreme_values",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct initial mean (R{int(mean_without):,}) and median (R{med_without:,})", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Correct updated mean (R{int(mean_with):,}) and median (R{int(med_with):,})", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Valid reasoning: median resists outlier distortion", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Compare how much the mean changed compared to how much the median changed.",
            "2_concept": "The mean is sensitive to extreme values, while the median is resistant.",
            "3_breakdown": f"Mean jumps to R{int(mean_with):,}, while median only shifts slightly to R{int(med_with):,}.",
        },
        "misconception_tags": ["mean_outlier_sensitivity_confusion"],
    }


# -----------------------------------------------------------------------------
# 50. Comprehensive statistical analysis summary
# -----------------------------------------------------------------------------
def arch_50_comprehensive_statistical_analysis_summary(rng: random.Random) -> Dict[str, Any]:
    min_v = rng.randint(12, 20)
    q1 = min_v + rng.randint(10, 15)
    med = q1 + rng.randint(8, 12)
    iqr = rng.choice([24, 28, 32, 36])
    q3 = q1 + iqr
    upper_fence = q3 + int(1.5 * iqr)

    # 50% chance max_v is an outlier or not
    is_outlier = rng.choice([True, False])
    if is_outlier:
        max_v = upper_fence + rng.randint(4, 10)
    else:
        max_v = upper_fence - rng.randint(4, 10)

    svg = _make_box_plot_svg(min_v, q1, med, q3, max_v, title="Comprehensive Marks Study")

    prompt = (
        "A comprehensive statistical study of 200 learners produced the following summary:\n\n"
        f"$$\\text{{Minimum}} = {min_v}, \\quad Q_1 = {q1}, \\quad \\text{{Median}} = {med}, \\quad Q_3 = {q3}, \\quad \\text{{Maximum}} = {max_v}$$\n\n"
        "1. Calculate the Interquartile Range (IQR).\n"
        f"2. Calculate the upper fence using the $1{{,}}5 \\times \\text{{IQR}}$ rule to determine if the maximum mark ({max_v}) is an outlier.\n"
        "3. Comment on the skewness of the distribution and provide mathematical justification."
    )

    d_right = q3 - med
    d_left = med - q1
    w_right = max_v - q3
    w_left = q1 - min_v

    outlier_status = "is an outlier" if is_outlier else "is NOT an outlier"
    comp_sym = ">" if is_outlier else "\\le"
    fence_step = int(1.5 * iqr)

    worked = (
        f"**1. Interquartile Range:**\n"
        f"$$\\text{{IQR}} = Q_3 - Q_1 = {q3} - {q1} = {iqr}$$\n\n"
        f"**2. Upper Fence Check:**\n"
        f"$$\\text{{Upper fence}} = Q_3 + 1{{,}}5 \\times \\text{{IQR}} = {q3} + 1{{,}}5({iqr}) = {q3} + {fence_step} = {upper_fence}$$\n"
        f"Since {max_v} ${comp_sym} {upper_fence}$, the maximum mark {outlier_status}.\n\n"
        f"**3. Skewness:**\n"
        f"The distribution is **positively skewed (skewed to the right)** because:\n"
        f"- $Q_3 - \\text{{Median}} ({d_right}) > \\text{{Median}} - Q_1 ({d_left})$\n"
        f"- The right whisker ({w_right}) is longer than the left whisker ({w_left})."
    )

    ans = f"IQR={iqr}, Upper fence={upper_fence}, Positively skewed"

    return {
        "id": f"g10_stat_50_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 5,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "50_comprehensive_statistical_analysis_summary",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "difficulty": "hard",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct IQR ({iqr})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct upper fence calculation ({upper_fence})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct outlier conclusion ({outlier_status})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Identification of positive skewness", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Valid mathematical justification based on distances and whiskers", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "IQR = Q3 - Q1. Upper fence = Q3 + 1,5 * IQR. Check if Max exceeds the fence.",
            "2_concept": "Compare Q3 - Med with Med - Q1 to determine the skewness.",
            "3_breakdown": f"IQR = {iqr}, Upper fence = {upper_fence}. Distribution is positively skewed.",
        },
        "misconception_tags": ["comprehensive_statistics_synthesis_error"],
    }
