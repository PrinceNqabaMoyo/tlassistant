"""Grade 11 Mathematics — Term 4 — Statistics Archetypes 01–25.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 4: Chapter 10 Statistics).
Covers:
- Measures of central tendency: Mean, Median (odd & even N), Mode, missing values from mean/median
- Measures of dispersion: Range, Quartiles (Q1, Q3), Interquartile Range (IQR), Semi-IQR
- Five-number summary (Min, Q1, Median, Q3, Max)
- Outlier fences (Q1 - 1,5*IQR and Q3 + 1,5*IQR) and formal outlier identification
- Box-and-whisker diagrams (inline_svg): reading five-number summary, skewness classification, quartile percentages, parallel box plot comparison
- Linear data transformations (+k, *k), combined group means, adding/removing items, and stem-and-leaf summaries.
"""
from __future__ import annotations

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


def _box_and_whisker_svg(
    min_v: float,
    q1_v: float,
    med_v: float,
    q3_v: float,
    max_v: float,
    label: str = "Dataset",
    unit: str = "",
) -> Dict[str, Any]:
    """Generate a clean dynamic inline SVG box-and-whisker diagram."""
    span = max(max_v - min_v, 1.0)
    pad = span * 0.12
    lo_axis = min_v - pad
    hi_axis = max_v + pad
    axis_span = hi_axis - lo_axis

    def to_x(val: float) -> float:
        return 50.0 + ((val - lo_axis) / axis_span) * 340.0

    x_min = to_x(min_v)
    x_q1 = to_x(q1_v)
    x_med = to_x(med_v)
    x_q3 = to_x(q3_v)
    x_max = to_x(max_v)

    svg = (
        f'<svg viewBox="0 0 440 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="190" fill="#f8fafc" rx="8"/>'
        f'<text x="220" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">{label}</text>'
        # Number line axis
        f'<line x1="35" y1="145" x2="405" y2="145" stroke="#64748b" stroke-width="1.8"/>'
        # Vertical dashed guides
        f'<line x1="{x_min:.1f}" y1="80" x2="{x_min:.1f}" y2="145" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.2"/>'
        f'<line x1="{x_q1:.1f}" y1="105" x2="{x_q1:.1f}" y2="145" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.2"/>'
        f'<line x1="{x_med:.1f}" y1="105" x2="{x_med:.1f}" y2="145" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.2"/>'
        f'<line x1="{x_q3:.1f}" y1="105" x2="{x_q3:.1f}" y2="145" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.2"/>'
        f'<line x1="{x_max:.1f}" y1="80" x2="{x_max:.1f}" y2="145" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.2"/>'
        # Whiskers
        f'<line x1="{x_min:.1f}" y1="80" x2="{x_q1:.1f}" y2="80" stroke="#1e293b" stroke-width="2.2"/>'
        f'<line x1="{x_q3:.1f}" y1="80" x2="{x_max:.1f}" y2="80" stroke="#1e293b" stroke-width="2.2"/>'
        f'<line x1="{x_min:.1f}" y1="66" x2="{x_min:.1f}" y2="94" stroke="#1e293b" stroke-width="2.2"/>'
        f'<line x1="{x_max:.1f}" y1="66" x2="{x_max:.1f}" y2="94" stroke="#1e293b" stroke-width="2.2"/>'
        # Box
        f'<rect x="{x_q1:.1f}" y="55" width="{max(x_q3 - x_q1, 4.0):.1f}" height="50" fill="#dbeafe" stroke="#2563eb" stroke-width="2.2"/>'
        # Median line
        f'<line x1="{x_med:.1f}" y1="55" x2="{x_med:.1f}" y2="105" stroke="#dc2626" stroke-width="2.8"/>'
        # Value labels
        f'<text x="{x_min:.1f}" y="164" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{min_v:g}{unit}</text>'
        f'<text x="{x_q1:.1f}" y="47" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{q1_v:g}</text>'
        f'<text x="{x_med:.1f}" y="164" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">{med_v:g}</text>'
        f'<text x="{x_q3:.1f}" y="47" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{q3_v:g}</text>'
        f'<text x="{x_max:.1f}" y="164" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{max_v:g}{unit}</text>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "min": min_v,
        "q1": q1_v,
        "median": med_v,
        "q3": q3_v,
        "max": max_v,
    }


def _parallel_box_plots_svg(
    a_vals: Tuple[float, float, float, float, float],
    b_vals: Tuple[float, float, float, float, float],
    label_a: str = "Group A",
    label_b: str = "Group B",
) -> Dict[str, Any]:
    """Generate an inline SVG comparing two parallel box-and-whisker plots."""
    lo_all = min(a_vals[0], b_vals[0]) - 5
    hi_all = max(a_vals[4], b_vals[4]) + 5
    span = max(hi_all - lo_all, 1.0)

    def tx(v: float) -> float:
        return 70.0 + ((v - lo_all) / span) * 330.0

    ax0, ax1, ax2, ax3, ax4 = [tx(v) for v in a_vals]
    bx0, bx1, bx2, bx3, bx4 = [tx(v) for v in b_vals]

    svg = (
        f'<svg viewBox="0 0 440 230" width="100%" height="230" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="230" fill="#f8fafc" rx="8"/>'
        # Group A (top)
        f'<text x="12" y="68" font-size="12" font-weight="bold" fill="#1d4ed8">{label_a}</text>'
        f'<line x1="{ax0:.1f}" y1="64" x2="{ax1:.1f}" y2="64" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="{ax3:.1f}" y1="64" x2="{ax4:.1f}" y2="64" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="{ax1:.1f}" y="46" width="{max(ax3 - ax1, 4.0):.1f}" height="36" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="{ax2:.1f}" y1="46" x2="{ax2:.1f}" y2="82" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="{ax1:.1f}" y="40" font-size="10" fill="#1d4ed8" text-anchor="middle">{a_vals[1]:g}</text>'
        f'<text x="{ax2:.1f}" y="96" font-size="10" fill="#dc2626" text-anchor="middle">{a_vals[2]:g}</text>'
        f'<text x="{ax3:.1f}" y="40" font-size="10" fill="#1d4ed8" text-anchor="middle">{a_vals[3]:g}</text>'
        # Group B (bottom)
        f'<text x="12" y="148" font-size="12" font-weight="bold" fill="#047857">{label_b}</text>'
        f'<line x1="{bx0:.1f}" y1="144" x2="{bx1:.1f}" y2="144" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="{bx3:.1f}" y1="144" x2="{bx4:.1f}" y2="144" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="{bx1:.1f}" y="126" width="{max(bx3 - bx1, 4.0):.1f}" height="36" fill="#d1fae5" stroke="#059669" stroke-width="2"/>'
        f'<line x1="{bx2:.1f}" y1="126" x2="{bx2:.1f}" y2="162" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="{bx1:.1f}" y="120" font-size="10" fill="#047857" text-anchor="middle">{b_vals[1]:g}</text>'
        f'<text x="{bx2:.1f}" y="176" font-size="10" fill="#dc2626" text-anchor="middle">{b_vals[2]:g}</text>'
        f'<text x="{bx3:.1f}" y="120" font-size="10" fill="#047857" text-anchor="middle">{b_vals[3]:g}</text>'
        # Axis
        f'<line x1="60" y1="198" x2="415" y2="198" stroke="#64748b" stroke-width="1.8"/>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "group_a": a_vals,
        "group_b": b_vals,
    }


# 01. Mean of ungrouped discrete data
def build_01_mean_of_ungrouped_discrete_data(r: random.Random) -> Dict[str, Any]:
    base = r.randint(12, 35)
    offsets = [-6, -3, -1, 0, 2, 3, 5]
    data = [base + d for d in offsets]
    r.shuffle(data)
    total = sum(data)
    mean_v = total // len(data)
    data_str = "; ".join(str(x) for x in data)

    prompt = (
        f"The number of SMS messages sent by $7$ learners in one day was recorded as:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"Calculate the arithmetic mean ($\\bar{{x}}$) of this data set."
    )
    sol = solution_graph(
        goal=r"\text{Calculate } \bar{x}",
        steps=[
            step(from_latex=r"\sum x", to_latex_str=str(total), op="sum_data", rule="Add all 7 data values"),
            step(from_latex=rf"\bar{{x}} = \frac{{{total}}}{{7}}", to_latex_str=str(mean_v), op="divide_by_n", rule="Divide sum by n = 7"),
        ],
        final_latex=str(mean_v),
    )
    return make_math_question(
        prefix="stat11_01",
        topic=TOPIC,
        subskill="01_mean_of_ungrouped_discrete_data",
        learning_objective_id=f"{LO_PREFIX}_01",
        prompt=prompt,
        prompt_latex=rf"\bar{{x}} \text{{ of }} \{{{data_str}\}}",
        answer_latex=str(mean_v),
        answer_sympy=str(mean_v),
        sample_answer=f"Mean = {mean_v}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"Sum = {total}"}, {"mark": "A1", "criterion": f"Mean = {mean_v}"}]},
        hints={"nudge": "Add all 7 values together and divide by 7.", "concept": r"$\bar{x} = \frac{\sum x}{n}$", "breakdown": f"{total} / 7 = {mean_v}"},
        misconception_tags=["divided_by_wrong_count", "confused_mean_with_median"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="01_mean_of_ungrouped_discrete_data",
        difficulty="easy",
    )


# 02. Find unknown data value from mean
def build_02_find_unknown_data_value_from_mean(r: random.Random) -> Dict[str, Any]:
    mean_target = r.randint(15, 30)
    known = [mean_target - 5, mean_target - 2, mean_target + 1, mean_target + 4, mean_target + 6]
    x_val = 6 * mean_target - sum(known)
    known_sum = sum(known)
    total_req = 6 * mean_target
    data_str = "; ".join(str(v) for v in known) + "; x"

    prompt = (
        f"The arithmetic mean of the following $6$ data values is ${mean_target}$:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"Determine the value of $x$."
    )
    sol = solution_graph(
        goal="Solve for x from given mean",
        steps=[
            step(from_latex=rf"\frac{{{known_sum} + x}}{{6}} = {mean_target}", to_latex_str=rf"{known_sum} + x = {total_req}", op="multiply_by_n", rule="Multiply mean by n = 6"),
            step(from_latex=rf"x = {total_req} - {known_sum}", to_latex_str=f"x = {x_val}", op="isolate_x", rule="Subtract sum of known values"),
        ],
        final_latex=str(x_val),
    )
    return make_math_question(
        prefix="stat11_02",
        topic=TOPIC,
        subskill="02_find_unknown_data_value_from_mean",
        learning_objective_id=f"{LO_PREFIX}_02",
        prompt=prompt,
        prompt_latex=rf"\bar{{x}} = {mean_target}",
        answer_latex=str(x_val),
        answer_sympy=str(x_val),
        sample_answer=f"x = {x_val}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": f"Set up sum = 6 * {mean_target} = {total_req}"}, {"mark": "M1", "criterion": f"Sum known values = {known_sum}"}, {"mark": "A1", "criterion": f"x = {x_val}"}]},
        hints={"nudge": f"Multiply the mean ({mean_target}) by 6 to get the total sum.", "concept": r"$\sum x = n \bar{x}$", "breakdown": f"x = {total_req} - {known_sum} = {x_val}"},
        misconception_tags=["divided_by_5_instead_of_6", "forgot_x_in_count"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="02_find_unknown_data_value_from_mean",
        difficulty="easy",
    )


# 03. Median of odd-count dataset
def build_03_median_odd_count_dataset(r: random.Random) -> Dict[str, Any]:
    med = r.randint(25, 55)
    s_data = [med - 14, med - 9, med - 5, med - 2, med, med + 3, med + 7, med + 11, med + 16]
    shuffled = list(s_data)
    r.shuffle(shuffled)
    if shuffled == s_data:
        shuffled[0], shuffled[-1] = shuffled[-1], shuffled[0]

    raw_str = "; ".join(str(x) for x in shuffled)
    ord_str = "; ".join(str(x) for x in s_data)

    prompt = (
        f"Determine the median of the following $9$ test scores:\n"
        f"$$\\{{{raw_str}\\}}$$"
    )
    sol = solution_graph(
        goal="Determine median of odd-count data",
        steps=[
            step(from_latex=rf"\{{{raw_str}\}}", to_latex_str=rf"\{{{ord_str}\}}", op="sort_ascending", rule="Arrange data in ascending order"),
            step(from_latex=r"\text{Position} = \frac{9+1}{2} = 5", to_latex_str=str(med), op="locate_middle", rule="Read 5th ordered value"),
        ],
        final_latex=str(med),
    )
    return make_math_question(
        prefix="stat11_03",
        topic=TOPIC,
        subskill="03_median_odd_count_dataset",
        learning_objective_id=f"{LO_PREFIX}_03",
        prompt=prompt,
        prompt_latex=rf"\text{{Median of }} \{{{raw_str}\}}",
        answer_latex=str(med),
        answer_sympy=str(med),
        sample_answer=f"Median = {med}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": "Order data in ascending order"}, {"mark": "A1", "criterion": f"Median = {med}"}]},
        hints={"nudge": "Always sort the values from smallest to largest first!", "concept": "For n = 9, the median is the 5th value in the ordered list.", "breakdown": f"Ordered: {ord_str} -> Median = {med}"},
        misconception_tags=["failed_to_sort_before_median"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="03_median_odd_count_dataset",
        difficulty="easy",
    )


# 04. Median of even-count dataset
def build_04_median_even_count_dataset(r: random.Random) -> Dict[str, Any]:
    m1 = r.randint(20, 48)
    gap = r.choice([2, 3, 4, 5, 6])
    m2 = m1 + gap
    med_v = (m1 + m2) / 2.0
    s_data = [m1 - 11, m1 - 7, m1 - 3, m1, m2, m2 + 4, m2 + 8, m2 + 13]
    shuffled = list(s_data)
    r.shuffle(shuffled)
    if shuffled == s_data:
        shuffled[0], shuffled[-1] = shuffled[-1], shuffled[0]

    raw_str = "; ".join(str(x) for x in shuffled)
    ord_str = "; ".join(str(x) for x in s_data)
    med_str = num(med_v)

    prompt = (
        f"Calculate the median of the following $8$ measurements:\n"
        f"$$\\{{{raw_str}\\}}$$"
    )
    sol = solution_graph(
        goal="Calculate median of even-count data",
        steps=[
            step(from_latex=rf"\{{{raw_str}\}}", to_latex_str=rf"\{{{ord_str}\}}", op="sort_ascending", rule="Arrange data from smallest to largest"),
            step(from_latex=rf"\frac{{{m1} + {m2}}}{{2}}", to_latex_str=med_str, op="average_middle_pair", rule="Average the 4th and 5th ordered values"),
        ],
        final_latex=med_str,
    )
    return make_math_question(
        prefix="stat11_04",
        topic=TOPIC,
        subskill="04_median_even_count_dataset",
        learning_objective_id=f"{LO_PREFIX}_04",
        prompt=prompt,
        prompt_latex=rf"\text{{Median of }} \{{{raw_str}\}}",
        answer_latex=med_str,
        answer_sympy=str(med_v),
        sample_answer=f"Median = {med_str}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"Sort and identify middle pair {m1} and {m2}"}, {"mark": "A1", "criterion": f"Median = {med_str}"}]},
        hints={"nudge": "Sort the 8 numbers first, then average the 4th and 5th values.", "concept": r"$\text{Median} = \frac{x_4 + x_5}{2}$", "breakdown": f"({m1} + {m2})/2 = {med_str}"},
        misconception_tags=["failed_to_sort_before_median", "picked_only_one_middle_value"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="04_median_even_count_dataset",
        difficulty="easy",
    )


# 05. Find unknown ordered value from median
def build_05_find_unknown_ordered_value_from_median(r: random.Random) -> Dict[str, Any]:
    v4 = r.randint(18, 40)
    x_val = v4 + r.choice([4, 6, 8, 10])
    med_v = (v4 + x_val) // 2
    s_list = [v4 - 10, v4 - 6, v4 - 2, str(v4), "x", x_val + 3, x_val + 7, x_val + 12]
    data_str = "; ".join(str(i) for i in s_list)

    prompt = (
        f"The following $8$ data values are already arranged in ascending order:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"If the median of the data set is ${med_v}$, calculate the value of $x$."
    )
    sol = solution_graph(
        goal="Solve for x from given median",
        steps=[
            step(from_latex=rf"\frac{{{v4} + x}}{{2}} = {med_v}", to_latex_str=rf"{v4} + x = {2 * med_v}", op="setup_median_equation", rule="Average of 4th and 5th terms equals median"),
            step(from_latex=rf"x = {2 * med_v} - {v4}", to_latex_str=f"x = {x_val}", op="solve_x", rule="Subtract 4th term"),
        ],
        final_latex=str(x_val),
    )
    return make_math_question(
        prefix="stat11_05",
        topic=TOPIC,
        subskill="05_find_unknown_ordered_value_from_median",
        learning_objective_id=f"{LO_PREFIX}_05",
        prompt=prompt,
        prompt_latex=rf"\frac{{{v4} + x}}{{2}} = {med_v}",
        answer_latex=str(x_val),
        answer_sympy=str(x_val),
        sample_answer=f"x = {x_val}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"({v4} + x)/2 = {med_v}"}, {"mark": "A1", "criterion": f"x = {x_val}"}]},
        hints={"nudge": f"The 4th and 5th numbers are {v4} and x.", "concept": f"({v4} + x) / 2 = {med_v}", "breakdown": f"x = {2 * med_v} - {v4} = {x_val}"},
        misconception_tags=["equated_x_directly_to_median"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="05_find_unknown_ordered_value_from_median",
        difficulty="easy",
    )


# 06. Mode and bimodal identification
def build_06_mode_and_bimodal_identification(r: random.Random) -> Dict[str, Any]:
    mode_val = r.randint(12, 38)
    other_rep = mode_val + r.choice([3, 5, 7])
    data = [mode_val - 4, mode_val - 2, mode_val, mode_val, mode_val, other_rep, other_rep, other_rep + 4, other_rep + 7]
    r.shuffle(data)
    data_str = "; ".join(str(x) for x in data)

    prompt = (
        f"Determine the mode of the following data set:\n"
        f"$$\\{{{data_str}\\}}$$"
    )
    sol = solution_graph(
        goal="Find the mode (most frequent value)",
        steps=[
            step(from_latex=rf"\{{{data_str}\}}", to_latex_str=rf"\text{{Frequency of }} {mode_val} = 3", op="count_frequencies", rule="Count occurrences of each value"),
            step(from_latex=rf"\text{{Max frequency}} = 3", to_latex_str=str(mode_val), op="select_mode", rule="Value with highest frequency"),
        ],
        final_latex=str(mode_val),
    )
    return make_math_question(
        prefix="stat11_06",
        topic=TOPIC,
        subskill="06_mode_and_bimodal_identification",
        learning_objective_id=f"{LO_PREFIX}_06",
        prompt=prompt,
        prompt_latex=rf"\text{{Mode of }} \{{{data_str}\}}",
        answer_latex=str(mode_val),
        answer_sympy=str(mode_val),
        sample_answer=f"Mode = {mode_val}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"Identify {mode_val} appears 3 times"}, {"mark": "A1", "criterion": f"Mode = {mode_val}"}]},
        hints={"nudge": "Count which number appears the greatest number of times.", "concept": "The mode is the most frequent observation.", "breakdown": f"{mode_val} appears 3 times -> Mode = {mode_val}"},
        misconception_tags=["reported_frequency_instead_of_value"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="06_mode_and_bimodal_identification",
        difficulty="easy",
    )


# 07. Range of ungrouped dataset
def build_07_range_of_ungrouped_dataset(r: random.Random) -> Dict[str, Any]:
    min_v = r.randint(11, 29)
    rng_v = r.randint(25, 55)
    max_v = min_v + rng_v
    mids = [min_v + 4, min_v + 9, min_v + 14, max_v - 8, max_v - 3]
    data = [min_v] + mids + [max_v]
    r.shuffle(data)
    data_str = "; ".join(str(x) for x in data)

    prompt = (
        f"Calculate the range of the following data set:\n"
        f"$$\\{{{data_str}\\}}$$"
    )
    sol = solution_graph(
        goal="Calculate Range = Max - Min",
        steps=[
            step(from_latex=rf"\text{{Min}} = {min_v}, \text{{ Max}} = {max_v}", to_latex_str=rf"{max_v} - {min_v}", op="identify_extremes", rule="Find maximum and minimum values"),
            step(from_latex=rf"{max_v} - {min_v}", to_latex_str=str(rng_v), op="subtract", rule="Range = Max - Min"),
        ],
        final_latex=str(rng_v),
    )
    return make_math_question(
        prefix="stat11_07",
        topic=TOPIC,
        subskill="07_range_of_ungrouped_dataset",
        learning_objective_id=f"{LO_PREFIX}_07",
        prompt=prompt,
        prompt_latex=rf"\text{{Range of }} \{{{data_str}\}}",
        answer_latex=str(rng_v),
        answer_sympy=str(rng_v),
        sample_answer=f"Range = {rng_v}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"Max = {max_v}, Min = {min_v}"}, {"mark": "A1", "criterion": f"Range = {rng_v}"}]},
        hints={"nudge": "Find the largest and smallest values in the set.", "concept": r"$\text{Range} = \text{Max} - \text{Min}$", "breakdown": f"{max_v} - {min_v} = {rng_v}"},
        misconception_tags=["subtracted_last_minus_first_unsorted"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="07_range_of_ungrouped_dataset",
        difficulty="easy",
    )


# 08. Find unknown extreme from range
def build_08_find_unknown_extreme_from_range(r: random.Random) -> Dict[str, Any]:
    min_v = r.randint(8, 24)
    rng_v = r.randint(30, 52)
    x_max = min_v + rng_v
    data_str = f"{min_v}; {min_v+5}; {min_v+11}; {min_v+18}; {min_v+22}; x"

    prompt = (
        f"The following $6$ positive integers are arranged in ascending order:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"If the range of the data set is ${rng_v}$, determine the value of $x$."
    )
    sol = solution_graph(
        goal="Solve for maximum x given range and minimum",
        steps=[
            step(from_latex=rf"x - {min_v} = {rng_v}", to_latex_str=rf"x = {rng_v} + {min_v}", op="setup_range_eq", rule="Range = Max - Min"),
            step(from_latex=rf"{rng_v} + {min_v}", to_latex_str=str(x_max), op="add", rule="Compute x"),
        ],
        final_latex=str(x_max),
    )
    return make_math_question(
        prefix="stat11_08",
        topic=TOPIC,
        subskill="08_find_unknown_extreme_from_range",
        learning_objective_id=f"{LO_PREFIX}_08",
        prompt=prompt,
        prompt_latex=rf"x - {min_v} = {rng_v}",
        answer_latex=str(x_max),
        answer_sympy=str(x_max),
        sample_answer=f"x = {x_max}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"x - {min_v} = {rng_v}"}, {"mark": "A1", "criterion": f"x = {x_max}"}]},
        hints={"nudge": f"Since the list is ordered, {min_v} is the minimum and x is the maximum.", "concept": r"$\text{Max} = \text{Min} + \text{Range}$", "breakdown": f"x = {min_v} + {rng_v} = {x_max}"},
        misconception_tags=["subtracted_instead_of_adding_min"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="08_find_unknown_extreme_from_range",
        difficulty="easy",
    )


# 09. Lower and upper quartiles for odd dataset
def build_09_lower_and_upper_quartiles_odd_dataset(r: random.Random) -> Dict[str, Any]:
    q1 = r.randint(18, 30)
    med = q1 + r.randint(6, 12)
    q3 = med + r.randint(6, 14)
    # 7 values: [min, q1, v3, med, v5, q3, max]
    s_data = [q1 - 5, q1, q1 + 3, med, q3 - 2, q3, q3 + 6]
    data_str = "; ".join(str(x) for x in s_data)
    ans_str = f"Q_1 = {q1}, Q_3 = {q3}"

    prompt = (
        f"Given the ordered data set of $7$ values:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"Determine the lower quartile ($Q_1$) and the upper quartile ($Q_3$)."
    )
    sol = solution_graph(
        goal="Find Q1 and Q3 for n = 7",
        steps=[
            step(from_latex=rf"\text{{Lower half}} = \{{{s_data[0]}; {s_data[1]}; {s_data[2]}\}}", to_latex_str=f"Q_1 = {q1}", op="find_q1", rule="Median of lower 3 values"),
            step(from_latex=rf"\text{{Upper half}} = \{{{s_data[4]}; {s_data[5]}; {s_data[6]}\}}", to_latex_str=f"Q_3 = {q3}", op="find_q3", rule="Median of upper 3 values"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_09",
        topic=TOPIC,
        subskill="09_lower_and_upper_quartiles_odd_dataset",
        learning_objective_id=f"{LO_PREFIX}_09",
        prompt=prompt,
        prompt_latex=rf"Q_1, Q_3 \text{{ of }} \{{{data_str}\}}",
        answer_latex=ans_str,
        answer_sympy=f"({q1}, {q3})",
        sample_answer=f"Q1 = {q1}, Q3 = {q3}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"Q1 = {q1}"}, {"mark": "A1", "criterion": f"Q3 = {q3}"}]},
        hints={"nudge": f"Exclude the median ({med}) to form the lower half of 3 values and upper half of 3 values.", "concept": "Q1 is the middle of the lower half; Q3 is the middle of the upper half.", "breakdown": f"Q1 = {q1}, Q3 = {q3}"},
        misconception_tags=["included_median_in_halves_for_odd_n"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="09_lower_and_upper_quartiles_odd_dataset",
        difficulty="easy",
    )


# 10. Lower and upper quartiles for even dataset
def build_10_lower_and_upper_quartiles_even_dataset(r: random.Random) -> Dict[str, Any]:
    # 8 values: lower half 4 values, upper half 4 values
    a2 = r.randint(14, 26)
    a3 = a2 + r.choice([2, 4])
    q1 = (a2 + a3) // 2
    b2 = a3 + r.randint(8, 14)
    b3 = b2 + r.choice([2, 4])
    q3 = (b2 + b3) // 2
    s_data = [a2 - 4, a2, a3, a3 + 2, b2 - 2, b2, b3, b3 + 5]
    data_str = "; ".join(str(x) for x in s_data)
    ans_str = f"Q_1 = {q1}, Q_3 = {q3}"

    prompt = (
        f"Given the ordered data set of $8$ values:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"Calculate the lower quartile ($Q_1$) and the upper quartile ($Q_3$)."
    )
    sol = solution_graph(
        goal="Find Q1 and Q3 for n = 8",
        steps=[
            step(from_latex=rf"Q_1 = \frac{{{a2} + {a3}}}{{2}}", to_latex_str=str(q1), op="avg_lower_half", rule="Average 2nd and 3rd values"),
            step(from_latex=rf"Q_3 = \frac{{{b2} + {b3}}}{{2}}", to_latex_str=str(q3), op="avg_upper_half", rule="Average 6th and 7th values"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_10",
        topic=TOPIC,
        subskill="10_lower_and_upper_quartiles_even_dataset",
        learning_objective_id=f"{LO_PREFIX}_10",
        prompt=prompt,
        prompt_latex=rf"Q_1, Q_3 \text{{ of }} \{{{data_str}\}}",
        answer_latex=ans_str,
        answer_sympy=f"({q1}, {q3})",
        sample_answer=f"Q1 = {q1}, Q3 = {q3}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": "Split into two halves of 4 values"}, {"mark": "A1", "criterion": f"Q1 = {q1}"}, {"mark": "A1", "criterion": f"Q3 = {q3}"}]},
        hints={"nudge": "Split the 8 ordered values into a lower group of 4 and an upper group of 4.", "concept": "Find the median of each group of 4.", "breakdown": f"Q1 = ({a2}+{a3})/2 = {q1}; Q3 = ({b2}+{b3})/2 = {q3}"},
        misconception_tags=["wrong_quartile_positions_for_even_n"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="10_lower_and_upper_quartiles_even_dataset",
        difficulty="medium",
    )


# 11. Interquartile range calculation
def build_11_interquartile_range_calculation(r: random.Random) -> Dict[str, Any]:
    q1 = r.randint(20, 35)
    iqr = r.randint(12, 26)
    q3 = q1 + iqr
    med = q1 + iqr // 2
    s_data = [q1 - 7, q1, q1 + 2, med, q3 - 2, q3, q3 + 8]
    data_str = "; ".join(str(x) for x in s_data)

    prompt = (
        f"Consider the ordered data set of $7$ values:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"Calculate the interquartile range ($\\text{{IQR}}$)."
    )
    sol = solution_graph(
        goal="Calculate IQR = Q3 - Q1",
        steps=[
            step(from_latex=rf"Q_1 = {q1}, \quad Q_3 = {q3}", to_latex_str=rf"\text{{IQR}} = {q3} - {q1}", op="identify_quartiles", rule="Find Q1 (2nd term) and Q3 (6th term)"),
            step(from_latex=rf"{q3} - {q1}", to_latex_str=str(iqr), op="subtract", rule="IQR = Q3 - Q1"),
        ],
        final_latex=str(iqr),
    )
    return make_math_question(
        prefix="stat11_11",
        topic=TOPIC,
        subskill="11_interquartile_range_calculation",
        learning_objective_id=f"{LO_PREFIX}_11",
        prompt=prompt,
        prompt_latex=rf"\text{{IQR of }} \{{{data_str}\}}",
        answer_latex=str(iqr),
        answer_sympy=str(iqr),
        sample_answer=f"IQR = {iqr}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "A1", "criterion": f"Q1 = {q1}"}, {"mark": "A1", "criterion": f"Q3 = {q3}"}, {"mark": "A1", "criterion": f"IQR = {iqr}"}]},
        hints={"nudge": f"Find Q1 and Q3 first, then subtract Q1 from Q3.", "concept": r"$\text{IQR} = Q_3 - Q_1$", "breakdown": f"{q3} - {q1} = {iqr}"},
        misconception_tags=["computed_max_minus_min_instead_of_iqr"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="11_interquartile_range_calculation",
        difficulty="easy",
    )


# 12. Semi-interquartile range calculation
def build_12_semi_interquartile_range_calculation(r: random.Random) -> Dict[str, Any]:
    q1 = r.randint(22, 40)
    iqr = r.choice([10, 14, 16, 18, 22, 24])
    q3 = q1 + iqr
    semi_iqr = iqr // 2
    med = q1 + semi_iqr
    s_data = [q1 - 6, q1, q1 + 3, med, q3 - 3, q3, q3 + 9]
    data_str = "; ".join(str(x) for x in s_data)

    prompt = (
        f"For the ordered data set:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"Calculate the **semi-interquartile range**."
    )
    sol = solution_graph(
        goal="Calculate semi-IQR = (Q3 - Q1)/2",
        steps=[
            step(from_latex=rf"Q_1 = {q1}, \quad Q_3 = {q3}", to_latex_str=rf"\text{{IQR}} = {q3} - {q1} = {iqr}", op="find_iqr", rule="Calculate IQR = Q3 - Q1"),
            step(from_latex=rf"\frac{{{iqr}}}{{2}}", to_latex_str=str(semi_iqr), op="halve_iqr", rule="Semi-IQR = IQR / 2"),
        ],
        final_latex=str(semi_iqr),
    )
    return make_math_question(
        prefix="stat11_12",
        topic=TOPIC,
        subskill="12_semi_interquartile_range_calculation",
        learning_objective_id=f"{LO_PREFIX}_12",
        prompt=prompt,
        prompt_latex=rf"\frac{{Q_3 - Q_1}}{{2}}",
        answer_latex=str(semi_iqr),
        answer_sympy=str(semi_iqr),
        sample_answer=f"Semi-IQR = {semi_iqr}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": f"Q1 = {q1}, Q3 = {q3}"}, {"mark": "M1", "criterion": f"IQR = {iqr}"}, {"mark": "A1", "criterion": f"Semi-IQR = {semi_iqr}"}]},
        hints={"nudge": "Find the IQR first, then divide by 2.", "concept": r"$\text{Semi-IQR} = \frac{Q_3 - Q_1}{2}$", "breakdown": f"({q3} - {q1}) / 2 = {semi_iqr}"},
        misconception_tags=["forgot_to_divide_iqr_by_2", "averaged_q3_plus_q1_instead_of_difference"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="12_semi_interquartile_range_calculation",
        difficulty="easy",
    )


# 13. Complete five-number summary
def build_13_complete_five_number_summary(r: random.Random) -> Dict[str, Any]:
    min_v = r.randint(10, 25)
    q1_v = min_v + r.randint(5, 10)
    med_v = q1_v + r.randint(6, 12)
    q3_v = med_v + r.randint(6, 12)
    max_v = q3_v + r.randint(6, 14)
    # 7 values: [min_v, q1_v, med_v-2, med_v, q3_v-2, q3_v, max_v]
    s_data = [min_v, q1_v, med_v - 2, med_v, q3_v - 2, q3_v, max_v]
    data_str = "; ".join(str(x) for x in s_data)
    ans_str = f"({min_v}; {q1_v}; {med_v}; {q3_v}; {max_v})"

    prompt = (
        f"Write down the complete **five-number summary** $(\\text{{Min}}; Q_1; \\text{{Median}}; Q_3; \\text{{Max}})$ "
        f"for the ordered data set:\n"
        f"$$\\{{{data_str}\\}}$$"
    )
    sol = solution_graph(
        goal="State the five-number summary",
        steps=[
            step(from_latex=rf"\text{{Min}} = {min_v}, \text{{ Max}} = {max_v}", to_latex_str=rf"\text{{Median}} = {med_v}", op="extremes_and_median", rule="Read 1st, 4th, and 7th values"),
            step(from_latex=rf"Q_1 = {q1_v}, \quad Q_3 = {q3_v}", to_latex_str=ans_str, op="quartiles", rule="Read 2nd and 6th values"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_13",
        topic=TOPIC,
        subskill="13_complete_five_number_summary",
        learning_objective_id=f"{LO_PREFIX}_13",
        prompt=prompt,
        prompt_latex=r"\text{Five-number summary}",
        answer_latex=ans_str,
        answer_sympy=ans_str,
        sample_answer=f"Min = {min_v}, Q1 = {q1_v}, Median = {med_v}, Q3 = {q3_v}, Max = {max_v}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "A1", "criterion": f"Min = {min_v}, Max = {max_v}"}, {"mark": "A1", "criterion": f"Median = {med_v}"}, {"mark": "A1", "criterion": f"Q1 = {q1_v}, Q3 = {q3_v}"}]},
        hints={"nudge": "A five-number summary consists of Min, Q1, Median, Q3, and Max.", "concept": "For 7 ordered values, these are at positions 1, 2, 4, 6, and 7.", "breakdown": ans_str},
        misconception_tags=["included_mean_in_five_number_summary"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="13_complete_five_number_summary",
        difficulty="easy",
    )


# 14. Outlier lower and upper fences
def build_14_outlier_lower_and_upper_fences(r: random.Random) -> Dict[str, Any]:
    q1 = r.randint(30, 50)
    iqr = r.choice([10, 12, 14, 16, 20])
    q3 = q1 + iqr
    step_val = int(1.5 * iqr)
    lo_fence = q1 - step_val
    hi_fence = q3 + step_val
    ans_str = f"[{lo_fence}; {hi_fence}]"

    prompt = (
        f"A data set has a lower quartile of $Q_1 = {q1}$ and an upper quartile of $Q_3 = {q3}$.\n\n"
        f"Calculate the lower and upper outlier fences $[Q_1 - 1{{,}}5 \\times \\text{{IQR}}; Q_3 + 1{{,}}5 \\times \\text{{IQR}}]$."
    )
    sol = solution_graph(
        goal="Compute lower and upper outlier fences",
        steps=[
            step(from_latex=rf"\text{{IQR}} = {q3} - {q1} = {iqr}", to_latex_str=rf"1{{,}}5 \times \text{{IQR}} = {step_val}", op="compute_1_5_iqr", rule="Multiply IQR by 1,5"),
            step(from_latex=rf"[{q1} - {step_val}; {q3} + {step_val}]", to_latex_str=ans_str, op="compute_fences", rule="Subtract from Q1 and add to Q3"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_14",
        topic=TOPIC,
        subskill="14_outlier_lower_and_upper_fences",
        learning_objective_id=f"{LO_PREFIX}_14",
        prompt=prompt,
        prompt_latex=r"[Q_1 - 1{,}5\text{IQR}; Q_3 + 1{,}5\text{IQR}]",
        answer_latex=ans_str,
        answer_sympy=ans_str,
        sample_answer=f"Lower fence = {lo_fence}, Upper fence = {hi_fence}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": f"IQR = {iqr} and 1,5*IQR = {step_val}"}, {"mark": "A1", "criterion": f"Lower fence = {lo_fence}"}, {"mark": "A1", "criterion": f"Upper fence = {hi_fence}"}]},
        hints={"nudge": f"First find IQR = {q3} - {q1} = {iqr}.", "concept": r"$\text{Fences} = Q_1 - 1{,}5\text{IQR}$ and $Q_3 + 1{,}5\text{IQR}$", "breakdown": f"Lower = {lo_fence}, Upper = {hi_fence}"},
        misconception_tags=["added_and_subtracted_from_median_instead_of_quartiles"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="14_outlier_lower_and_upper_fences",
        difficulty="medium",
    )


# 15. Identify outliers using 1,5 * IQR rule
def build_15_identify_outliers_using_iqr_rule(r: random.Random) -> Dict[str, Any]:
    q1 = r.randint(24, 38)
    iqr = r.choice([8, 10, 12, 14])
    q3 = q1 + iqr
    med = q1 + iqr // 2
    hi_fence = int(q3 + 1.5 * iqr)
    outlier_val = hi_fence + r.randint(4, 12)
    s_data = [q1 - 3, q1, q1 + 2, med, q3 - 1, q3, outlier_val]
    data_str = "; ".join(str(x) for x in s_data)

    prompt = (
        f"Consider the ordered data set of $7$ values:\n"
        f"$$\\{{{data_str}\\}}$$\n"
        f"Given $Q_1 = {q1}$ and $Q_3 = {q3}$, use the formal $1{{,}}5 \\times \\text{{IQR}}$ rule to identify the outlier in the data set."
    )
    sol = solution_graph(
        goal="Identify outlier using upper fence",
        steps=[
            step(from_latex=rf"\text{{IQR}} = {q3} - {q1} = {iqr}", to_latex_str=rf"Q_3 + 1{{,}}5({iqr}) = {hi_fence}", op="upper_fence", rule="Calculate upper outlier threshold"),
            step(from_latex=rf"{outlier_val} > {hi_fence}", to_latex_str=str(outlier_val), op="identify_outlier", rule="Value exceeding upper fence is an outlier"),
        ],
        final_latex=str(outlier_val),
    )
    return make_math_question(
        prefix="stat11_15",
        topic=TOPIC,
        subskill="15_identify_outliers_using_iqr_rule",
        learning_objective_id=f"{LO_PREFIX}_15",
        prompt=prompt,
        prompt_latex=rf"\text{{Outlier in }} \{{{data_str}\}}",
        answer_latex=str(outlier_val),
        answer_sympy=str(outlier_val),
        sample_answer=f"Outlier = {outlier_val} (since {outlier_val} > {hi_fence})",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": f"IQR = {iqr}"}, {"mark": "M1", "criterion": f"Upper fence = {hi_fence}"}, {"mark": "A1", "criterion": f"Identify {outlier_val} as outlier"}]},
        hints={"nudge": f"Calculate the upper fence Q3 + 1,5*IQR.", "concept": f"Upper fence = {q3} + 1,5({iqr}) = {hi_fence}.", "breakdown": f"Since {outlier_val} > {hi_fence}, {outlier_val} is an outlier."},
        misconception_tags=["stated_outlier_without_calculating_fence"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="15_identify_outliers_using_iqr_rule",
        difficulty="medium",
    )


# 16. Box-and-whisker read five-number summary (with inline_svg)
def build_16_box_and_whisker_read_five_number_summary_svg(r: random.Random) -> Dict[str, Any]:
    min_v = r.randint(12, 28)
    q1_v = min_v + r.randint(8, 14)
    med_v = q1_v + r.randint(6, 12)
    q3_v = med_v + r.randint(8, 15)
    max_v = q3_v + r.randint(7, 14)
    iqr_v = q3_v - q1_v

    diag = _box_and_whisker_svg(min_v, q1_v, med_v, q3_v, max_v, label="Test Scores (%)")
    prompt = (
        f"Refer to the box-and-whisker diagram of learner test scores.\n\n"
        f"Write down the median ($Q_2$) and calculate the interquartile range ($\\text{{IQR}}$)."
    )
    ans_str = f"\\text{{Median}} = {med_v}, \\text{{IQR}} = {iqr_v}"
    sol = solution_graph(
        goal="Read median and compute IQR from box plot",
        steps=[
            step(from_latex=r"\text{Vertical line inside box}", to_latex_str=f"Q_2 = {med_v}", op="read_median", rule="Read median line"),
            step(from_latex=rf"Q_3 - Q_1 = {q3_v} - {q1_v}", to_latex_str=f"\\text{{IQR}} = {iqr_v}", op="compute_iqr", rule="Subtract box left edge from right edge"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_16",
        topic=TOPIC,
        subskill="16_box_and_whisker_read_five_number_summary_svg",
        learning_objective_id=f"{LO_PREFIX}_16",
        prompt=prompt,
        prompt_latex=r"\text{Median and IQR from Box Plot}",
        answer_latex=ans_str,
        answer_sympy=f"({med_v}, {iqr_v})",
        sample_answer=f"Median = {med_v}, IQR = {iqr_v}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"Median = {med_v}"}, {"mark": "A1", "criterion": f"IQR = {iqr_v}"}]},
        hints={"nudge": "The red vertical line inside the box marks the median, and the box edges mark Q1 and Q3.", "concept": f"Q1 = {q1_v}, Median = {med_v}, Q3 = {q3_v}", "breakdown": f"Median = {med_v}, IQR = {q3_v} - {q1_v} = {iqr_v}"},
        misconception_tags=["read_whisker_tips_instead_of_box_edges"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="16_box_and_whisker_read_five_number_summary_svg",
        difficulty="easy",
    )


# 17. Box-and-whisker skewness classification (with inline_svg)
def build_17_box_and_whisker_skewness_classification_svg(r: random.Random) -> Dict[str, Any]:
    skew_type = r.choice(["right", "left", "sym"])
    min_v = r.randint(10, 20)
    q1_v = min_v + r.randint(6, 10)
    if skew_type == "right":
        d1 = r.randint(4, 7)
        d2 = d1 + r.randint(8, 14)
        med_v = q1_v + d1
        q3_v = med_v + d2
        max_v = q3_v + r.randint(12, 18)
        ans = "Positively skewed (skewed to the right)"
    elif skew_type == "left":
        d1 = r.randint(12, 18)
        d2 = r.randint(4, 7)
        med_v = q1_v + d1
        q3_v = med_v + d2
        max_v = q3_v + r.randint(5, 8)
        ans = "Negatively skewed (skewed to the left)"
    else:
        d1 = r.randint(8, 12)
        d2 = d1
        med_v = q1_v + d1
        q3_v = med_v + d2
        max_v = q3_v + (q1_v - min_v)
        ans = "Symmetrical"

    diag = _box_and_whisker_svg(min_v, q1_v, med_v, q3_v, max_v, label="Distribution Analysis")
    prompt = (
        f"Refer to the box-and-whisker diagram with $Q_1 = {q1_v}$, $\\text{{Median}} = {med_v}$, and $Q_3 = {q3_v}$.\n\n"
        f"Compare $(Q_3 - \\text{{Median}})$ with $(\\text{{Median}} - Q_1)$ and state whether the distribution is "
        f"**positively skewed**, **negatively skewed**, or **symmetrical**."
    )
    sol = solution_graph(
        goal="Classify skewness of box plot",
        steps=[
            step(from_latex=rf"\text{{Median}} - Q_1 = {med_v} - {q1_v} = {d1}", to_latex_str=rf"Q_3 - \text{{Median}} = {q3_v} - {med_v} = {d2}", op="compare_half_boxes", rule="Calculate left and right box widths"),
            step(from_latex=rf"\text{{Left}} = {d1}, \text{{ Right}} = {d2}", to_latex_str=ans, op="classify_skew", rule="Compare right side vs left side of median"),
        ],
        final_latex=ans,
    )
    return make_math_question(
        prefix="stat11_17",
        topic=TOPIC,
        subskill="17_box_and_whisker_skewness_classification_svg",
        learning_objective_id=f"{LO_PREFIX}_17",
        prompt=prompt,
        prompt_latex=r"\text{Skewness from Box Plot}",
        answer_latex=ans,
        answer_sympy=ans,
        sample_answer=f"{ans} (since Q3 - Median = {d2} and Median - Q1 = {d1})",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"Compare {d2} and {d1}"}, {"mark": "A1", "criterion": ans}]},
        hints={"nudge": "Compare the width of the box to the right of the median with the width to the left.", "concept": "If Q3 - Median > Median - Q1, the data are skewed to the right (positively skewed).", "breakdown": ans},
        misconception_tags=["inverted_skewness_direction"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="17_box_and_whisker_skewness_classification_svg",
        difficulty="easy",
    )


# 18. Skewness from Mean minus Median relation
def build_18_skewness_from_mean_minus_median_relation(r: random.Random) -> Dict[str, Any]:
    med_v = r.randint(45, 72)
    diff = r.choice([-8, -6, -4, 4, 6, 8])
    mean_v = med_v + diff
    if diff > 0:
        ans = "Positively skewed (skewed to the right)"
        rel = rf"\bar{{x}} ({mean_v}) > \text{{Median}} ({med_v})"
    else:
        ans = "Negatively skewed (skewed to the left)"
        rel = rf"\bar{{x}} ({mean_v}) < \text{{Median}} ({med_v})"

    prompt = (
        f"A data set of examination marks has a mean of $\\bar{{x}} = {mean_v}$ and a median of $M = {med_v}$.\n\n"
        f"Based on the relationship between the mean and the median, state whether the data are "
        f"**positively skewed** or **negatively skewed**, and justify your answer."
    )
    sol = solution_graph(
        goal="Determine skewness from mean vs median",
        steps=[
            step(from_latex=rf"\bar{{x}} - M = {mean_v} - {med_v} = {diff}", to_latex_str=rel, op="compare_mean_median", rule="Compare mean and median"),
            step(from_latex=rel, to_latex_str=ans, op="conclude_skew", rule="Mean is pulled in the direction of the tail"),
        ],
        final_latex=ans,
    )
    return make_math_question(
        prefix="stat11_18",
        topic=TOPIC,
        subskill="18_skewness_from_mean_minus_median_relation",
        learning_objective_id=f"{LO_PREFIX}_18",
        prompt=prompt,
        prompt_latex=rf"\bar{{x}} = {mean_v}, M = {med_v}",
        answer_latex=ans,
        answer_sympy=ans,
        sample_answer=f"{ans} because {rel}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": rel}, {"mark": "A1", "criterion": ans}]},
        hints={"nudge": "Remember that extreme values in the tail pull the mean toward the tail.", "concept": "If Mean > Median, the data are positively skewed; if Mean < Median, negatively skewed.", "breakdown": ans},
        misconception_tags=["inverted_mean_median_skewness_rule"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="18_skewness_from_mean_minus_median_relation",
        difficulty="easy",
    )


# 19. Box-and-whisker percentage in intervals (with inline_svg)
def build_19_box_and_whisker_percentage_in_intervals_svg(r: random.Random) -> Dict[str, Any]:
    n_total = r.choice([40, 60, 80, 120, 160])
    min_v = r.randint(15, 25)
    q1_v = min_v + r.randint(8, 12)
    med_v = q1_v + r.randint(8, 12)
    q3_v = med_v + r.randint(8, 12)
    max_v = q3_v + r.randint(8, 14)

    pct_choice = r.choice([25, 50, 75])
    if pct_choice == 25:
        interval_desc = f"between ${q3_v}$ and ${max_v}$"
        count_ans = n_total // 4
    elif pct_choice == 50:
        interval_desc = f"between ${q1_v}$ and ${q3_v}$"
        count_ans = n_total // 2
    else:
        interval_desc = f"less than or equal to ${q3_v}$"
        count_ans = (3 * n_total) // 4

    diag = _box_and_whisker_svg(min_v, q1_v, med_v, q3_v, max_v, label=f"Sample of {n_total} Observations")
    prompt = (
        f"The box-and-whisker diagram represents the masses (in kg) of ${n_total}$ bags of maize.\n\n"
        f"How many bags have a mass {interval_desc}?"
    )
    sol = solution_graph(
        goal="Calculate count using quartile percentages",
        steps=[
            step(from_latex=rf"\text{{Proportion}} = {pct_choice}\%", to_latex_str=rf"\frac{{{pct_choice}}}{{100}} \times {n_total}", op="quartile_percentage", rule="Each quartile section contains 25% of the data"),
            step(from_latex=rf"\frac{{{pct_choice}}}{{100}} \times {n_total}", to_latex_str=str(count_ans), op="multiply", rule="Calculate number of bags"),
        ],
        final_latex=str(count_ans),
    )
    return make_math_question(
        prefix="stat11_19",
        topic=TOPIC,
        subskill="19_box_and_whisker_percentage_in_intervals_svg",
        learning_objective_id=f"{LO_PREFIX}_19",
        prompt=prompt,
        prompt_latex=rf"{pct_choice}\% \text{{ of }} {n_total}",
        answer_latex=str(count_ans),
        answer_sympy=str(count_ans),
        sample_answer=f"{count_ans} bags ({pct_choice}% of {n_total})",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "M1", "criterion": f"Identify {pct_choice}% of data"}, {"mark": "A1", "criterion": f"{count_ans} bags"}]},
        hints={"nudge": "Each section of a box-and-whisker diagram represents 25% of the observations.", "concept": f"This interval covers {pct_choice}% of the {n_total} bags.", "breakdown": f"{pct_choice}% of {n_total} = {count_ans}"},
        misconception_tags=["used_interval_width_instead_of_quartile_percentage"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="19_box_and_whisker_percentage_in_intervals_svg",
        difficulty="medium",
    )


# 20. Parallel box plots compare spread and consistency (with inline_svg)
def build_20_parallel_box_plots_compare_spread_and_consistency_svg(r: random.Random) -> Dict[str, Any]:
    med = r.randint(50, 68)
    iqr_a = r.randint(22, 32)
    iqr_b = r.randint(8, 14)
    a_q1 = med - iqr_a // 2
    a_q3 = a_q1 + iqr_a
    b_q1 = med - iqr_b // 2
    b_q3 = b_q1 + iqr_b

    a_vals = (a_q1 - 10, a_q1, med, a_q3, a_q3 + 12)
    b_vals = (b_q1 - 6, b_q1, med, b_q3, b_q3 + 7)
    diag = _parallel_box_plots_svg(a_vals, b_vals, label_a="Class A", label_b="Class B")

    prompt = (
        f"The parallel box-and-whisker diagrams compare the test percentages of Class A and Class B.\n\n"
        f"Calculate the interquartile range ($\\text{{IQR}}$) for each class and state which class performed more **consistently**."
    )
    ans_str = f"\\text{{Class B}} (\\text{{IQR}}_B = {iqr_b} < \\text{{IQR}}_A = {iqr_a})"
    sol = solution_graph(
        goal="Compare IQRs and identify more consistent group",
        steps=[
            step(from_latex=rf"\text{{IQR}}_A = {a_q3} - {a_q1} = {iqr_a}", to_latex_str=rf"\text{{IQR}}_B = {b_q3} - {b_q1} = {iqr_b}", op="compute_both_iqrs", rule="Calculate IQR for both classes"),
            step(from_latex=rf"\text{{IQR}}_B ({iqr_b}) < \text{{IQR}}_A ({iqr_a})", to_latex_str="Class B is more consistent", op="compare_consistency", rule="Smaller IQR indicates less dispersion and higher consistency"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_20",
        topic=TOPIC,
        subskill="20_parallel_box_plots_compare_spread_and_consistency_svg",
        learning_objective_id=f"{LO_PREFIX}_20",
        prompt=prompt,
        prompt_latex=r"\text{Compare }\text{IQR}_A \text{ and } \text{IQR}_B",
        answer_latex=ans_str,
        answer_sympy=ans_str,
        sample_answer=f"IQR_A = {iqr_a}, IQR_B = {iqr_b}; Class B is more consistent",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "A1", "criterion": f"IQR_A = {iqr_a}"}, {"mark": "A1", "criterion": f"IQR_B = {iqr_b}"}, {"mark": "A1", "criterion": "Class B is more consistent (smaller IQR)"}]},
        hints={"nudge": "Consistency is measured by spread: a smaller IQR means more consistent performance.", "concept": f"IQR_A = {a_q3} - {a_q1} = {iqr_a}; IQR_B = {b_q3} - {b_q1} = {iqr_b}.", "breakdown": f"Class B is more consistent because {iqr_b} < {iqr_a}."},
        misconception_tags=["chose_larger_iqr_as_more_consistent"],
        diagram_spec=diag,
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="20_parallel_box_plots_compare_spread_and_consistency_svg",
        difficulty="medium",
    )


# 21. Effect of adding a constant on mean and standard deviation
def build_21_effect_of_adding_constant_on_mean_and_sd(r: random.Random) -> Dict[str, Any]:
    old_mean = r.randint(42, 68)
    old_sd = r.randint(5, 14)
    k = r.randint(4, 15)
    new_mean = old_mean + k
    new_sd = old_sd
    ans_str = f"\\text{{New Mean}} = {new_mean}, \\text{{New SD}} = {new_sd}"

    prompt = (
        f"A set of marks has a mean of $\\bar{{x}} = {old_mean}$ and a standard deviation of $\\sigma = {old_sd}$.\n\n"
        f"If every learner is awarded an extra ${k}$ marks (so ${k}$ is added to every value in the data set), "
        f"write down the **new mean** and the **new standard deviation**."
    )
    sol = solution_graph(
        goal="Determine new mean and SD after adding constant k",
        steps=[
            step(from_latex=rf"\bar{{x}}_{{\text{{new}}}} = {old_mean} + {k}", to_latex_str=str(new_mean), op="shift_mean", rule="Adding k shifts the mean by +k"),
            step(from_latex=rf"\sigma_{{\text{{new}}}} = \sigma_{{\text{{old}}}}", to_latex_str=str(new_sd), op="invariant_sd", rule="Adding a constant does not change dispersion (SD)"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_21",
        topic=TOPIC,
        subskill="21_effect_of_adding_constant_on_mean_and_sd",
        learning_objective_id=f"{LO_PREFIX}_21",
        prompt=prompt,
        prompt_latex=rf"y_i = x_i + {k}",
        answer_latex=ans_str,
        answer_sympy=f"({new_mean}, {new_sd})",
        sample_answer=f"New Mean = {new_mean}, New SD = {new_sd}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"New Mean = {new_mean}"}, {"mark": "A1", "criterion": f"New SD = {new_sd} (unchanged)"}]},
        hints={"nudge": "Shifting all values up by k shifts the average up by k, but does the spread between scores change?", "concept": "Adding k increases the mean by k and leaves standard deviation unchanged.", "breakdown": ans_str},
        misconception_tags=["added_constant_to_standard_deviation"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="21_effect_of_adding_constant_on_mean_and_sd",
        difficulty="easy",
    )


# 22. Effect of multiplying by a constant on mean and standard deviation
def build_22_effect_of_multiplying_constant_on_mean_and_sd(r: random.Random) -> Dict[str, Any]:
    old_mean = r.randint(15, 35)
    old_sd = r.randint(3, 9)
    k = r.choice([2, 3, 4, 5])
    new_mean = old_mean * k
    new_sd = old_sd * k
    ans_str = f"\\text{{New Mean}} = {new_mean}, \\text{{New SD}} = {new_sd}"

    prompt = (
        f"A data set has a mean of $\\bar{{x}} = {old_mean}$ and a standard deviation of $\\sigma = {old_sd}$.\n\n"
        f"If every data value in the set is multiplied by ${k}$, determine the **new mean** and the **new standard deviation**."
    )
    sol = solution_graph(
        goal="Determine new mean and SD after multiplying by k",
        steps=[
            step(from_latex=rf"\bar{{x}}_{{\text{{new}}}} = {k} \times {old_mean}", to_latex_str=str(new_mean), op="scale_mean", rule="Multiplying by k scales the mean by k"),
            step(from_latex=rf"\sigma_{{\text{{new}}}} = |{k}| \times {old_sd}", to_latex_str=str(new_sd), op="scale_sd", rule="Multiplying by k scales the standard deviation by |k|"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_22",
        topic=TOPIC,
        subskill="22_effect_of_multiplying_constant_on_mean_and_sd",
        learning_objective_id=f"{LO_PREFIX}_22",
        prompt=prompt,
        prompt_latex=rf"y_i = {k}x_i",
        answer_latex=ans_str,
        answer_sympy=f"({new_mean}, {new_sd})",
        sample_answer=f"New Mean = {new_mean}, New SD = {new_sd}",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"mark": "A1", "criterion": f"New Mean = {new_mean}"}, {"mark": "A1", "criterion": f"New SD = {new_sd}"}]},
        hints={"nudge": "Scaling every observation by a factor k scales both location and spread by k.", "concept": r"$\bar{x}_{\text{new}} = k\bar{x}$ and $\sigma_{\text{new}} = |k|\sigma$", "breakdown": ans_str},
        misconception_tags=["kept_sd_unchanged_under_multiplication"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="22_effect_of_multiplying_constant_on_mean_and_sd",
        difficulty="easy",
    )


# 23. Combined mean of two merged groups
def build_23_combined_mean_of_two_merged_groups(r: random.Random) -> Dict[str, Any]:
    n1 = r.choice([10, 15, 20])
    n2 = r.choice([20, 25, 30])
    m1 = r.randint(50, 65)
    m2 = r.randint(68, 82)
    sum1 = n1 * m1
    sum2 = n2 * m2
    total_n = n1 + n2
    total_sum = sum1 + sum2
    comb_mean = round(total_sum / total_n, 2)
    ans_str = num(comb_mean, 2) if not comb_mean.is_integer() else str(int(comb_mean))

    prompt = (
        f"Group A consists of ${n1}$ learners with a mean mark of ${m1}$. "
        f"Group B consists of ${n2}$ learners with a mean mark of ${m2}$.\n\n"
        f"Calculate the combined mean mark of all ${total_n}$ learners together (correct to two decimal places where necessary)."
    )
    sol = solution_graph(
        goal="Compute combined mean of two groups",
        steps=[
            step(from_latex=rf"\sum x_A = {n1} \times {m1} = {sum1}", to_latex_str=rf"\sum x_B = {n2} \times {m2} = {sum2}", op="group_totals", rule="Compute sum for each group"),
            step(from_latex=rf"\bar{{x}}_{{\text{{combined}}}} = \frac{{{sum1} + {sum2}}}{{{n1} + {n2}}} = \frac{{{total_sum}}}{{{total_n}}}", to_latex_str=ans_str, op="divide_total", rule="Divide combined sum by combined sample size"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_23",
        topic=TOPIC,
        subskill="23_combined_mean_of_two_merged_groups",
        learning_objective_id=f"{LO_PREFIX}_23",
        prompt=prompt,
        prompt_latex=rf"\frac{{{n1}({m1}) + {n2}({m2})}}{{{total_n}}}",
        answer_latex=ans_str,
        answer_sympy=str(comb_mean),
        sample_answer=f"Combined mean = {ans_str}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": f"Total sum = {sum1} + {sum2} = {total_sum}"}, {"mark": "M1", "criterion": f"Divide by {total_n}"}, {"mark": "A1", "criterion": f"Mean = {ans_str}"}]},
        hints={"nudge": "Do not just average the two means! Find the total sum of marks across both groups first.", "concept": r"$\bar{x} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1 + n_2}$", "breakdown": f"{total_sum} / {total_n} = {ans_str}"},
        misconception_tags=["unweighted_average_of_two_group_means"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="23_combined_mean_of_two_merged_groups",
        difficulty="medium",
    )


# 24. Mean after removing or adding an item
def build_24_mean_after_removing_or_adding_item(r: random.Random) -> Dict[str, Any]:
    n_orig = r.randint(6, 12)
    m_orig = r.randint(14, 28)
    m_new = m_orig - r.randint(1, 3)
    sum_orig = n_orig * m_orig
    sum_new = (n_orig - 1) * m_new
    removed_val = sum_orig - sum_new

    prompt = (
        f"The mean mass of ${n_orig}$ parcels is ${m_orig}\\text{{ kg}}$. When one parcel is removed, "
        f"the mean mass of the remaining ${n_orig - 1}$ parcels becomes ${m_new}\\text{{ kg}}$.\n\n"
        f"Calculate the mass of the parcel that was removed."
    )
    sol = solution_graph(
        goal="Find value of removed item from change in mean",
        steps=[
            step(from_latex=rf"\text{{Sum}}_{{\text{{before}}}} = {n_orig} \times {m_orig} = {sum_orig}", to_latex_str=rf"\text{{Sum}}_{{\text{{after}}}} = {n_orig - 1} \times {m_new} = {sum_new}", op="compute_sums", rule="Calculate total mass before and after removal"),
            step(from_latex=rf"{sum_orig} - {sum_new}", to_latex_str=str(removed_val), op="subtract_sums", rule="Mass of removed parcel = Sum_before - Sum_after"),
        ],
        final_latex=str(removed_val),
    )
    return make_math_question(
        prefix="stat11_24",
        topic=TOPIC,
        subskill="24_mean_after_removing_or_adding_item",
        learning_objective_id=f"{LO_PREFIX}_24",
        prompt=prompt,
        prompt_latex=rf"{n_orig}({m_orig}) - {n_orig-1}({m_new})",
        answer_latex=str(removed_val),
        answer_sympy=str(removed_val),
        sample_answer=f"{removed_val} kg",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "M1", "criterion": f"Sum before = {sum_orig}"}, {"mark": "M1", "criterion": f"Sum after = {sum_new}"}, {"mark": "A1", "criterion": f"Removed parcel = {removed_val} kg"}]},
        hints={"nudge": "Find the total mass of all parcels before and after the parcel is removed.", "concept": "Removed value = (n * old_mean) - ((n - 1) * new_mean).", "breakdown": f"{sum_orig} - {sum_new} = {removed_val} kg"},
        misconception_tags=["subtracted_means_instead_of_total_sums"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="24_mean_after_removing_or_adding_item",
        difficulty="medium",
    )


# 25. Stem-and-leaf five-number summary and IQR
def build_25_stem_and_leaf_five_number_summary_and_iqr(r: random.Random) -> Dict[str, Any]:
    s1 = r.choice([2, 3, 4])
    # 9 ordered values across 3 stems
    v = [
        s1 * 10 + 2,
        s1 * 10 + 5,
        s1 * 10 + 8,
        (s1 + 1) * 10 + 1,
        (s1 + 1) * 10 + 4,
        (s1 + 1) * 10 + 7,
        (s1 + 2) * 10 + 0,
        (s1 + 2) * 10 + 3,
        (s1 + 2) * 10 + 6,
    ]
    # For n = 9: Q1 = (v[1] + v[2])/2, Med = v[4], Q3 = (v[6] + v[7])/2
    q1_v = (v[1] + v[2]) / 2.0
    med_v = v[4]
    q3_v = (v[6] + v[7]) / 2.0
    iqr_v = q3_v - q1_v
    iqr_str = num(iqr_v)

    table_md = (
        f"| Stem | Leaves |\n"
        f"| :---: | :--- |\n"
        f"| ${s1}$ | $2 \\quad 5 \\quad 8$ |\n"
        f"| ${s1+1}$ | $1 \\quad 4 \\quad 7$ |\n"
        f"| ${s1+2}$ | $0 \\quad 3 \\quad 6$ |\n\n"
        f"**Key:** ${s1} \\mid 2 = {s1*10 + 2}$"
    )
    prompt = (
        f"The stem-and-leaf table below records the ages of $9$ participants in a community workshop:\n\n"
        f"{table_md}\n\n"
        f"Determine the median age and the interquartile range ($\\text{{IQR}}$)."
    )
    ans_str = f"\\text{{Median}} = {med_v}, \\text{{IQR}} = {iqr_str}"
    sol = solution_graph(
        goal="Determine median and IQR from stem-and-leaf data",
        steps=[
            step(from_latex=r"\text{5th value}", to_latex_str=f"\\text{{Median}} = {med_v}", op="find_median", rule="Middle (5th) value of 9 ordered observations"),
            step(from_latex=rf"Q_1 = {num(q1_v)}, \quad Q_3 = {num(q3_v)}", to_latex_str=f"\\text{{IQR}} = {iqr_str}", op="compute_iqr", rule="IQR = Q3 - Q1"),
        ],
        final_latex=ans_str,
    )
    return make_math_question(
        prefix="stat11_25",
        topic=TOPIC,
        subskill="25_stem_and_leaf_five_number_summary_and_iqr",
        learning_objective_id=f"{LO_PREFIX}_25",
        prompt=prompt,
        prompt_latex=r"\text{Median and IQR from Stem-and-Leaf}",
        answer_latex=ans_str,
        answer_sympy=f"({med_v}, {iqr_v})",
        sample_answer=f"Median = {med_v}, IQR = {iqr_str}",
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"mark": "A1", "criterion": f"Median = {med_v}"}, {"mark": "M1", "criterion": f"Q1 = {num(q1_v)}, Q3 = {num(q3_v)}"}, {"mark": "A1", "criterion": f"IQR = {iqr_str}"}]},
        hints={"nudge": "List the 9 two-digit numbers in order using the stem-and-leaf key.", "concept": f"Q1 = ({v[1]}+{v[2]})/2 = {num(q1_v)}, Q3 = ({v[6]}+{v[7]})/2 = {num(q3_v)}.", "breakdown": ans_str},
        misconception_tags=["read_leaves_without_stems"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="25_stem_and_leaf_five_number_summary_and_iqr",
        difficulty="medium",
    )


ARCHETYPES_01_25 = {
    "01_mean_of_ungrouped_discrete_data": build_01_mean_of_ungrouped_discrete_data,
    "02_find_unknown_data_value_from_mean": build_02_find_unknown_data_value_from_mean,
    "03_median_odd_count_dataset": build_03_median_odd_count_dataset,
    "04_median_even_count_dataset": build_04_median_even_count_dataset,
    "05_find_unknown_ordered_value_from_median": build_05_find_unknown_ordered_value_from_median,
    "06_mode_and_bimodal_identification": build_06_mode_and_bimodal_identification,
    "07_range_of_ungrouped_dataset": build_07_range_of_ungrouped_dataset,
    "08_find_unknown_extreme_from_range": build_08_find_unknown_extreme_from_range,
    "09_lower_and_upper_quartiles_odd_dataset": build_09_lower_and_upper_quartiles_odd_dataset,
    "10_lower_and_upper_quartiles_even_dataset": build_10_lower_and_upper_quartiles_even_dataset,
    "11_interquartile_range_calculation": build_11_interquartile_range_calculation,
    "12_semi_interquartile_range_calculation": build_12_semi_interquartile_range_calculation,
    "13_complete_five_number_summary": build_13_complete_five_number_summary,
    "14_outlier_lower_and_upper_fences": build_14_outlier_lower_and_upper_fences,
    "15_identify_outliers_using_iqr_rule": build_15_identify_outliers_using_iqr_rule,
    "16_box_and_whisker_read_five_number_summary_svg": build_16_box_and_whisker_read_five_number_summary_svg,
    "17_box_and_whisker_skewness_classification_svg": build_17_box_and_whisker_skewness_classification_svg,
    "18_skewness_from_mean_minus_median_relation": build_18_skewness_from_mean_minus_median_relation,
    "19_box_and_whisker_percentage_in_intervals_svg": build_19_box_and_whisker_percentage_in_intervals_svg,
    "20_parallel_box_plots_compare_spread_and_consistency_svg": build_20_parallel_box_plots_compare_spread_and_consistency_svg,
    "21_effect_of_adding_constant_on_mean_and_sd": build_21_effect_of_adding_constant_on_mean_and_sd,
    "22_effect_of_multiplying_constant_on_mean_and_sd": build_22_effect_of_multiplying_constant_on_mean_and_sd,
    "23_combined_mean_of_two_merged_groups": build_23_combined_mean_of_two_merged_groups,
    "24_mean_after_removing_or_adding_item": build_24_mean_after_removing_or_adding_item,
    "25_stem_and_leaf_five_number_summary_and_iqr": build_25_stem_and_leaf_five_number_summary_and_iqr,
}
