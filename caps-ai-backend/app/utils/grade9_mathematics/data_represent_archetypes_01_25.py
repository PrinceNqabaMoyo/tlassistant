"""Grade 9 Mathematics - Representing Data Archetypes 01-25 (CAPS Term 4).
Focus: Discrete vs Continuous Data, Bar Graphs, Double Bar Graphs, Histograms, Pie Charts, and Line Graphs.
100% deterministic, zero LLM calls.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.grade9_mathematics.data_represent_svg import (
    draw_bar_chart_svg,
    draw_broken_line_graph_svg,
    draw_histogram_svg,
    draw_pie_chart_svg,
)


def _fmt(val: float, decimals: int = 1) -> str:
    s = f"{val:.{decimals}f}"
    return s.replace(".", "{,}")


# -----------------------------------------------------------------------------
# 01. Discrete vs Continuous Data Identification
# -----------------------------------------------------------------------------
def arch_01_discrete_vs_continuous_data_identification(r: random.Random) -> Dict[str, Any]:
    examples = [
        ("the number of learners absent from school each day", "Discrete", "Counts can only be whole numbers (integers), with no in-between values."),
        ("the height of Grade 9 learners in centimetres", "Continuous", "Height is a measured physical quantity that can take any decimal value along a continuous scale."),
        ("the time taken to run a 100-metre sprint", "Continuous", "Time is a continuous measurement that can be measured to fractions of a second."),
        ("the number of cars passing a toll gate per hour", "Discrete", "Cars are counted in whole numbers; you cannot have a fraction of a car."),
        ("the daily maximum temperature in Durban", "Continuous", "Temperature is measured on a continuous real-number scale."),
        ("the shoe sizes of a soccer team (e.g. size 6, 7, 8)", "Discrete", "Shoe sizes come in distinct predefined discrete values."),
    ]
    scenario, data_type, explanation = r.choice(examples)

    prompt = (
        f"Consider the statistical variable: **{scenario}**.\n"
        f"Classify whether this data is **'Discrete'** or **'Continuous'**."
    )
    ans_str = data_type
    sol = (
        f"**Definition**:\n"
        f"• **Discrete data** results from counting and takes distinct, separate values (usually integers).\n"
        f"• **Continuous data** results from measuring and can take any value within a given continuous range.\n\n"
        f"For *{scenario}*:\n"
        f"{explanation}\n"
        f"Therefore, the data is **{data_type}**."
    )
    return {
        "subskill": "01_discrete_vs_continuous_data_identification",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{data_type} ({explanation})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Correct classification: {data_type}", "marks": 1},
            {"step": "Reason based on counting vs measuring", "marks": 1},
        ],
        "hints": [
            "Ask yourself: Is this variable *counted* in separate items or *measured* on a continuous scale?",
            f"The answer is {data_type}.",
        ],
        "misconception_tags": ["discrete_continuous_confusion"],
    }


# -----------------------------------------------------------------------------
# 02. Selecting Appropriate Graph for Data Type
# -----------------------------------------------------------------------------
def arch_02_select_appropriate_graph_for_data_type(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Continuous data grouped into class intervals (e.g. test marks 40–49, 50–59)", "Histogram", "A histogram is used for grouped continuous data with no gaps between bars."),
        ("Categorical survey data (e.g. favourite sports of learners)", "Bar Graph", "A bar graph with spaces between bars is appropriate for separate categories."),
        ("Parts of a whole expressing percentages (e.g. household budget allocation)", "Pie Chart", "A pie chart displays proportions of a total 100% sum."),
        ("Continuous change over time (e.g. temperature recorded every hour over 24 hours)", "Broken-line Graph", "A broken-line graph shows trends and continuous changes over time."),
        ("Comparing two categories across groups (e.g. boys vs girls scores)", "Double Bar Graph", "A double bar graph allows side-by-side comparison of two subsets."),
    ]
    data_context, graph_choice, reason = r.choice(scenarios)

    prompt = (
        f"A researcher wants to represent: **{data_context}**.\n"
        f"Which data display format is most appropriate for this scenario? Choose from: "
        f"['Bar Graph', 'Histogram', 'Pie Chart', 'Broken-line Graph', 'Double Bar Graph']."
    )
    ans_str = graph_choice
    sol = (
        f"The best representation is a **{graph_choice}**.\n"
        f"**Reason**: {reason}."
    )
    return {
        "subskill": "02_select_appropriate_graph_for_data_type",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{graph_choice} ({reason})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Correct graph type: {graph_choice}", "marks": 1},
            {"step": "Justification based on data structure", "marks": 1},
        ],
        "hints": [
            "Consider whether the data is grouped intervals, separate categories, or time-series.",
            f"The best choice is {graph_choice}.",
        ],
        "misconception_tags": ["inappropriate_graph_selection"],
    }


# -----------------------------------------------------------------------------
# 03. Read frequency from single bar graph
# -----------------------------------------------------------------------------
def arch_03_read_frequency_from_single_bar_graph(r: random.Random) -> Dict[str, Any]:
    cats = ["Soccer", "Netball", "Rugby", "Cricket", "Athletics"]
    counts = [r.randint(15, 45) for _ in cats]
    target_idx = r.randint(0, len(cats) - 1)
    target_cat = cats[target_idx]
    target_count = counts[target_idx]

    seed_val = r.randint(100, 999999)
    svg = draw_bar_chart_svg(cats, counts, title="Favourite Sports of Learners", y_label="Number of Learners", seed=seed_val)

    prompt = (
        f"The bar chart displays the favourite sports chosen by a group of learners. "
        f"How many learners chose **{target_cat}** as their favourite sport?"
    )
    ans_str = str(target_count)
    sol = (
        f"Locating **{target_cat}** on the horizontal axis and reading the height of the bar "
        f"against the vertical axis gives **{target_count} learners**."
    )
    return {
        "subskill": "03_read_frequency_from_single_bar_graph",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} learners",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Read vertical height for {target_cat}: {target_count}", "marks": 1},
        ],
        "hints": [
            f"Look along the horizontal axis to find the bar labeled '{target_cat}'.",
            f"Read across to the vertical axis: the height is {target_count}.",
        ],
        "misconception_tags": ["bar_graph_scale_reading_error"],
    }


# -----------------------------------------------------------------------------
# 04. Identify most and least popular category from bar graph
# -----------------------------------------------------------------------------
def arch_04_identify_most_and_least_popular_category(r: random.Random) -> Dict[str, Any]:
    cats = ["Apples", "Bananas", "Oranges", "Grapes", "Pears"]
    # Distinct values
    counts = r.sample(range(10, 50), 5)
    max_idx = counts.index(max(counts))
    min_idx = counts.index(min(counts))

    target = r.choice(["most", "least"])
    target_cat = cats[max_idx] if target == "most" else cats[min_idx]
    target_count = counts[max_idx] if target == "most" else counts[min_idx]

    seed_val = r.randint(100, 999999)
    svg = draw_bar_chart_svg(cats, counts, title="Fruit Sold at Tuckshop", y_label="Quantity Sold", seed=seed_val)

    prompt = (
        f"The bar chart shows the fruit quantities sold at a school tuckshop. "
        f"Which fruit was the **{target} popular** item?"
    )
    ans_str = target_cat
    sol = (
        f"The **{target} popular** fruit corresponds to the "
        f"{'tallest' if target == 'most' else 'shortest'} bar on the chart, "
        f"which is **{target_cat}** with {target_count} sales."
    )
    return {
        "subskill": "04_identify_most_and_least_popular_category",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{target_cat} ({target_count})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify {target} bar: {target_cat}", "marks": 1},
        ],
        "hints": [
            f"Find the {'tallest' if target == 'most' else 'shortest'} bar in the chart.",
            f"The {target} popular fruit is {target_cat}.",
        ],
        "misconception_tags": ["confused_most_and_least"],
    }


# -----------------------------------------------------------------------------
# 05. Difference in frequency between two bars
# -----------------------------------------------------------------------------
def arch_05_difference_in_frequency_between_two_bars(r: random.Random) -> Dict[str, Any]:
    cats = ["Grade 8", "Grade 9", "Grade 10", "Grade 11"]
    counts = r.sample(range(20, 80), 4)
    i1, i2 = 0, 1
    diff = abs(counts[i1] - counts[i2])

    seed_val = r.randint(100, 999999)
    svg = draw_bar_chart_svg(cats, counts, title="Library Books Borrowed", y_label="Books Borrowed", seed=seed_val)

    prompt = (
        f"Refer to the bar chart showing library books borrowed by different grades. "
        f"Calculate the difference between the number of books borrowed by **{cats[i1]}** ({counts[i1]}) "
        f"and **{cats[i2]}** ({counts[i2]})."
    )
    ans_str = str(diff)
    sol = (
        f"$$\\text{{Difference}} = |{counts[i1]} - {counts[i2]}| = {diff}\\text{{ books}}$$"
    )
    return {
        "subskill": "05_difference_in_frequency_between_two_bars",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} books",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Subtract frequencies: |{counts[i1]} - {counts[i2]}|", "marks": 1},
            {"step": f"Answer: {diff}", "marks": 1},
        ],
        "hints": [
            f"Subtract the smaller value from the larger value: $|{counts[i1]} - {counts[i2]}|$.",
            f"The difference is {diff}.",
        ],
        "misconception_tags": ["subtraction_order_confusion"],
    }


# -----------------------------------------------------------------------------
# 06. Total sample size from bar chart
# -----------------------------------------------------------------------------
def arch_06_total_sample_size_from_bar_chart(r: random.Random) -> Dict[str, Any]:
    cats = ["Red", "Blue", "Green", "Yellow"]
    counts = [r.randint(10, 40) for _ in cats]
    total_n = sum(counts)

    seed_val = r.randint(100, 999999)
    svg = draw_bar_chart_svg(cats, counts, title="Preferred T-Shirt Colours", y_label="Learners", seed=seed_val)

    prompt = (
        f"The bar chart represents the preferred colours of T-shirts for a group of learners. "
        f"Calculate the **total number of learners** surveyed."
    )
    ans_str = str(total_n)
    sum_expr = " + ".join(str(c) for c in counts)
    sol = (
        f"Sum the frequencies of all categories:\n"
        f"$$\\text{{Total}} = {sum_expr} = {total_n}\\text{{ learners}}$$"
    )
    return {
        "subskill": "06_total_sample_size_from_bar_chart",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} learners",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Sum all bar values: {sum_expr}", "marks": 1},
            {"step": f"Total: {total_n}", "marks": 1},
        ],
        "hints": [
            "Add the heights of all the bars together.",
            f"${sum_expr} = {total_n}$.",
        ],
        "misconception_tags": ["omitted_category_in_sum"],
    }


# -----------------------------------------------------------------------------
# 07. Calculate percentage of category from bar chart
# -----------------------------------------------------------------------------
def arch_07_calculate_percentage_of_category_from_bar_chart(r: random.Random) -> Dict[str, Any]:
    # Ensure total is clean (e.g. 50, 100, or 200)
    total = r.choice([50, 100, 200])
    p1 = r.randint(10, 25)
    p2 = r.randint(15, 30)
    p3 = r.randint(15, 25)
    p4 = 100 - (p1 + p2 + p3)

    cats = ["Walk", "Bus", "Car", "Bicycle"]
    counts = [int((p / 100.0) * total) for p in [p1, p2, p3, p4]]
    target_idx = r.randint(0, 3)
    target_cat = cats[target_idx]
    target_pct = [p1, p2, p3, p4][target_idx]

    seed_val = r.randint(100, 999999)
    svg = draw_bar_chart_svg(cats, counts, title="Mode of Transport to School", y_label="Number of Learners", seed=seed_val)

    prompt = (
        f"The bar chart shows how a sample of ${total}$ learners travel to school. "
        f"What percentage of the learners travel by **{target_cat}**?"
    )
    ans_str = str(target_pct)
    sol = (
        f"$$\\text{{Percentage}} = \\frac{{\\text{{Frequency}}}}{{\\text{{Total}}}} \\times 100\\% = \\frac{{{counts[target_idx]}}}{{{total}}} \\times 100\\% = {target_pct}\\%$$"
    )
    return {
        "subskill": "07_calculate_percentage_of_category_from_bar_chart",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str}%",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Fraction: {counts[target_idx]} / {total}", "marks": 1},
            {"step": f"Percentage: {target_pct}%", "marks": 1},
        ],
        "hints": [
            f"Frequency of {target_cat} is {counts[target_idx]} out of a total of {total}.",
            f"Divide ${counts[target_idx]} \\div {total}$ and multiply by $100\\%$.",
        ],
        "misconception_tags": ["percentage_conversion_error"],
    }


# -----------------------------------------------------------------------------
# 08. Histogram class interval identification
# -----------------------------------------------------------------------------
def arch_08_histogram_class_interval_identification(r: random.Random) -> Dict[str, Any]:
    bins = ["0–9", "10–19", "20–29", "30–39", "40–49"]
    counts = [r.randint(5, 25) for _ in bins]
    target_idx = r.randint(0, len(bins) - 1)
    target_bin = bins[target_idx]
    target_count = counts[target_idx]

    seed_val = r.randint(100, 999999)
    svg = draw_histogram_svg(bins, counts, title="Test Marks Distribution", x_label="Marks Interval", y_label="Number of Learners", seed=seed_val)

    prompt = (
        f"The histogram displays the test mark distribution for a Grade 9 class. "
        f"How many learners scored within the class interval **{target_bin}**?"
    )
    ans_str = str(target_count)
    sol = (
        f"Finding the bar for class interval **{target_bin}** and reading its height gives **{target_count} learners**."
    )
    return {
        "subskill": "08_histogram_class_interval_identification",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} learners",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Read height of bin {target_bin}: {target_count}", "marks": 1},
        ],
        "hints": [
            f"Locate the bar labeled '{target_bin}' on the horizontal axis.",
            f"Its height is {target_count}.",
        ],
        "misconception_tags": ["histogram_bin_reading_error"],
    }


# -----------------------------------------------------------------------------
# 09. Histogram modal class identification
# -----------------------------------------------------------------------------
def arch_09_histogram_modal_class_identification(r: random.Random) -> Dict[str, Any]:
    bins = ["20–29", "30–39", "40–49", "50–59", "60–69"]
    counts = r.sample(range(6, 35), 5)
    max_idx = counts.index(max(counts))
    modal_class = bins[max_idx]

    seed_val = r.randint(100, 999999)
    svg = draw_histogram_svg(bins, counts, title="Ages of Community Volunteers", x_label="Age Group", y_label="Frequency", seed=seed_val)

    prompt = (
        f"A histogram represents the ages of community volunteers. "
        f"Identify the **modal class** of the distribution."
    )
    ans_str = modal_class
    sol = (
        f"The **modal class** is the class interval with the highest frequency (tallest bar):\n"
        f"The tallest bar corresponds to **{modal_class}** with a frequency of {counts[max_idx]}."
    )
    return {
        "subskill": "09_histogram_modal_class_identification",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} (frequency {counts[max_idx]})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify highest frequency bin: {modal_class}", "marks": 1},
        ],
        "hints": [
            "The modal class is the interval with the tallest bar.",
            f"The tallest bar is {modal_class}.",
        ],
        "misconception_tags": ["modal_class_vs_mode_confusion"],
    }


# -----------------------------------------------------------------------------
# 10. Histogram total learners scoring above a threshold
# -----------------------------------------------------------------------------
def arch_10_histogram_learners_above_threshold(r: random.Random) -> Dict[str, Any]:
    bins = ["0–19", "20–39", "40–59", "60–79", "80–99"]
    counts = [r.randint(5, 20) for _ in bins]
    # Above 60%: bins 3 and 4
    above_60 = counts[3] + counts[4]

    seed_val = r.randint(100, 999999)
    svg = draw_histogram_svg(bins, counts, title="Examination Performance", x_label="Percentage Marks", y_label="Learners", seed=seed_val)

    prompt = (
        f"The histogram displays exam scores across 5 percentage intervals. "
        f"How many learners achieved a mark of **60% or higher** (intervals 60–79% and 80–99%)?"
    )
    ans_str = str(above_60)
    sol = (
        f"Add the frequencies of the intervals $\\ge 60\\%$:\n"
        f"$$\\text{{Total}} = {counts[3]} + {counts[4]} = {above_60}\\text{{ learners}}$$"
    )
    return {
        "subskill": "10_histogram_learners_above_threshold",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} learners",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify relevant intervals: {counts[3]} and {counts[4]}", "marks": 1},
            {"step": f"Sum: {above_60}", "marks": 1},
        ],
        "hints": [
            f"Combine the bars for 60–79% ({counts[3]}) and 80–99% ({counts[4]}).",
            f"${counts[3]} + {counts[4]} = {above_60}$.",
        ],
        "misconception_tags": ["threshold_boundary_reading_error"],
    }


# -----------------------------------------------------------------------------
# 11. Pie chart angle calculation (fraction times 360)
# -----------------------------------------------------------------------------
def arch_11_pie_chart_angle_calculation(r: random.Random) -> Dict[str, Any]:
    total_n = r.choice([20, 24, 30, 36, 40, 60, 72, 120])
    freq = r.choice([2, 3, 4, 5, 6, 8, 10])
    angle = round((freq / total_n) * 360)
    cat = r.choice(["Bicycle", "Car", "Bus", "Walking", "Train"])

    prompt = (
        f"In a survey of ${total_n}$ people, ${freq}$ people chose **{cat}**. "
        f"Calculate the **sector angle in degrees** ($^\\circ$) that represents this category in a circular statistical sector."
    )
    ans_str = str(angle)
    sol = (
        f"$$\\text{{Sector Angle}} = \\frac{{\\text{{Frequency}}}}{{\\text{{Total}}}} \\times 360^\\circ = \\frac{{{freq}}}{{{total_n}}} \\times 360^\\circ = {angle}^\\circ$$"
    )
    return {
        "subskill": "11_pie_chart_angle_calculation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str}°",
        "tolerance": 0.5,
        "marking_schema": [
            {"step": f"Formula: ({freq} / {total_n}) × 360°", "marks": 1},
            {"step": f"Answer: {angle}°", "marks": 1},
        ],
        "hints": [
            "A full circle has $360^\\circ$.",
            f"Multiply the fraction $\\frac{{{freq}}}{{{total_n}}}$ by $360^\\circ$.",
            f"Angle is {angle}°.",
        ],
        "misconception_tags": ["multiplied_by_100_instead_of_360_for_angle"],
    }


# -----------------------------------------------------------------------------
# 12. Pie chart percentage from degrees
# -----------------------------------------------------------------------------
def arch_12_pie_chart_percentage_from_degrees(r: random.Random) -> Dict[str, Any]:
    angle = r.choice([36, 54, 72, 90, 108, 144, 180])
    pct = round((angle / 360.0) * 100)

    prompt = (
        f"On a pie chart, a sector representing household expenditure on rent has an angle of **${angle}^\\circ$**. "
        f"What percentage of the total budget does this sector represent?"
    )
    ans_str = str(pct)
    sol = (
        f"$$\\text{{Percentage}} = \\frac{{\\text{{Sector Angle}}}}{{360^\\circ}} \\times 100\\% = \\frac{{{angle}^\\circ}}{{360^\\circ}} \\times 100\\% = {pct}\\%$$"
    )
    return {
        "subskill": "12_pie_chart_percentage_from_degrees",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str}%",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide angle by 360: {angle} / 360", "marks": 1},
            {"step": f"Multiply by 100%: {pct}%", "marks": 1},
        ],
        "hints": [
            f"Divide the sector angle by the total circle angle ($360^\\circ$): $\\frac{{{angle}}}{{360}}$.",
            f"Multiply by $100\\%$ to get {pct}%.",
        ],
        "misconception_tags": ["angle_to_percentage_formula_confusion"],
    }


# -----------------------------------------------------------------------------
# 13. Determine frequency from pie chart percentage and total
# -----------------------------------------------------------------------------
def arch_13_determine_frequency_from_pie_chart_percentage_and_total(r: random.Random) -> Dict[str, Any]:
    total_people = r.choice([200, 300, 400, 500, 600, 800])
    pct = r.choice([15, 20, 25, 30, 35, 40])
    freq = int((pct / 100.0) * total_people)
    cat = "Drama Club"

    slices = [
        (cat, freq),
        ("Sports", int(total_people * 0.4)),
        ("Art", total_people - freq - int(total_people * 0.4)),
    ]
    seed_val = r.randint(100, 999999)
    svg = draw_pie_chart_svg(slices, title="School Club Memberships", seed=seed_val)

    prompt = (
        f"A survey of ${total_people}$ learners is shown in the pie chart. "
        f"If **{pct}%** of the learners belong to the **{cat}**, "
        f"calculate how many learners belong to this club."
    )
    ans_str = str(freq)
    sol = (
        f"$$\\text{{Frequency}} = {pct}\\% \\times {total_people} = \\frac{{{pct}}}{{100}} \\times {total_people} = {freq}\\text{{ learners}}$$"
    )
    return {
        "subskill": "13_determine_frequency_from_pie_chart_percentage_and_total",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} learners",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply total by percentage: {pct}/100 × {total_people}", "marks": 1},
            {"step": f"Answer: {freq}", "marks": 1},
        ],
        "hints": [
            f"Calculate ${pct}\\%$ of ${total_people}$.",
            f"$\\frac{{{pct}}}{{100}} \\times {total_people} = {freq}$.",
        ],
        "misconception_tags": ["percentage_of_total_calculation_error"],
    }


# -----------------------------------------------------------------------------
# 14. Determine frequency from pie chart angle and total
# -----------------------------------------------------------------------------
def arch_14_determine_frequency_from_pie_chart_angle_and_total(r: random.Random) -> Dict[str, Any]:
    total_items = r.choice([120, 180, 240, 360, 480])
    angle = r.choice([30, 45, 60, 90, 120])
    freq = int((angle / 360.0) * total_items)
    cat = "Action"

    slices = [
        (cat, freq),
        ("Comedy", int(total_items * 0.4)),
        ("Drama", total_items - freq - int(total_items * 0.4)),
    ]
    seed_val = r.randint(100, 999999)
    svg = draw_pie_chart_svg(slices, title="Movie Genre Preferences", seed=seed_val)

    prompt = (
        f"A total of ${total_items}$ movie fans were surveyed. "
        f"In the pie chart, the sector representing **{cat}** has an angle of **${angle}^\\circ$**. "
        f"How many people chose {cat}?"
    )
    ans_str = str(freq)
    sol = (
        f"$$\\text{{Frequency}} = \\frac{{{angle}^\\circ}}{{360^\\circ}} \\times {total_items} = {freq}\\text{{ people}}$$"
    )
    return {
        "subskill": "14_determine_frequency_from_pie_chart_angle_and_total",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} people",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Fraction: {angle} / 360", "marks": 1},
            {"step": f"Multiply by total: ({angle}/360) × {total_items} = {freq}", "marks": 1},
        ],
        "hints": [
            f"The fraction of the circle is $\\frac{{{angle}}}{{360}}$.",
            f"Multiply this fraction by the total ${total_items}$: $\\frac{{{angle}}}{{360}} \\times {total_items} = {freq}$.",
        ],
        "misconception_tags": ["angle_fraction_multiplication_error"],
    }


# -----------------------------------------------------------------------------
# 15. Broken-line graph reading: value at a specific time
# -----------------------------------------------------------------------------
def arch_15_broken_line_graph_reading_value(r: random.Random) -> Dict[str, Any]:
    times = ["08:00", "10:00", "12:00", "14:00", "16:00"]
    temps = [r.randint(14, 18), r.randint(19, 23), r.randint(25, 29), r.randint(24, 28), r.randint(18, 22)]
    idx = r.randint(0, len(times) - 1)
    target_time = times[idx]
    target_temp = temps[idx]

    seed_val = r.randint(100, 999999)
    svg = draw_broken_line_graph_svg(times, temps, title="Hourly Temperature Readings", x_label="Time of Day", y_label="Temperature (°C)", seed=seed_val)

    prompt = (
        f"The line graph shows temperatures recorded at various times on a summer day. "
        f"What was the recorded temperature at **{target_time}** in degrees Celsius?"
    )
    ans_str = str(target_temp)
    sol = (
        f"Looking at **{target_time}** on the horizontal axis and following up to the line graph point "
        f"shows a temperature of **{target_temp}°C**."
    )
    return {
        "subskill": "15_broken_line_graph_reading_value",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str}°C",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Read value at {target_time}: {target_temp}", "marks": 1},
        ],
        "hints": [
            f"Find '{target_time}' on the horizontal axis.",
            f"Read the value on the vertical axis: {target_temp}°C.",
        ],
        "misconception_tags": ["line_graph_point_reading_error"],
    }


# -----------------------------------------------------------------------------
# 16. Broken-line graph: Maximum and minimum values
# -----------------------------------------------------------------------------
def arch_16_broken_line_graph_max_and_min(r: random.Random) -> Dict[str, Any]:
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    sales = r.sample(range(50, 150), 5)
    max_idx = sales.index(max(sales))
    min_idx = sales.index(min(sales))

    target = r.choice(["highest", "lowest"])
    target_day = days[max_idx] if target == "highest" else days[min_idx]
    target_val = sales[max_idx] if target == "highest" else sales[min_idx]

    seed_val = r.randint(100, 999999)
    svg = draw_broken_line_graph_svg(days, sales, title="Daily Canteen Sales", x_label="Day of Week", y_label="Sales (Rands)", seed=seed_val)

    prompt = (
        f"The line graph illustrates canteen sales over 5 consecutive days. "
        f"On which day were sales the **{target}**?"
    )
    ans_str = target_day
    sol = (
        f"The **{target}** point on the graph occurs on **{target_day}** with a sales value of R{target_val}."
    )
    return {
        "subskill": "16_broken_line_graph_max_and_min",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{target_day} (R{target_val})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify {target} point: {target_day}", "marks": 1},
        ],
        "hints": [
            f"Find the {'highest' if target == 'highest' else 'lowest'} peak on the line graph.",
            f"It occurs on {target_day}.",
        ],
        "misconception_tags": ["peak_trough_misidentification"],
    }


# -----------------------------------------------------------------------------
# 17. Broken-line graph: Rate of change between two intervals
# -----------------------------------------------------------------------------
def arch_17_broken_line_graph_rate_of_change(r: random.Random) -> Dict[str, Any]:
    hours = ["Hour 1", "Hour 2", "Hour 3", "Hour 4"]
    y_vals = [20, 35, 65, 80]
    # change between Hour 2 and Hour 3: 65 - 35 = 30
    i1, i2 = 1, 2
    change = y_vals[i2] - y_vals[i1]

    seed_val = r.randint(100, 999999)
    svg = draw_broken_line_graph_svg(hours, y_vals, title="Distance Travelled Over Time", x_label="Time Elapsed", y_label="Distance (km)", seed=seed_val)

    prompt = (
        f"A cyclist's cumulative distance is tracked on a line graph. "
        f"At {hours[i1]}, the distance was ${y_vals[i1]}\\text{{ km}}$, and at {hours[i2]}, it was ${y_vals[i2]}\\text{{ km}}$. "
        f"How many kilometres did the cyclist travel during this 1-hour interval?"
    )
    ans_str = str(change)
    sol = (
        f"$$\\text{{Distance}} = {y_vals[i2]} - {y_vals[i1]} = {change}\\text{{ km}}$$"
    )
    return {
        "subskill": "17_broken_line_graph_rate_of_change",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} km",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Subtract distances: {y_vals[i2]} - {y_vals[i1]} = {change}", "marks": 1},
        ],
        "hints": [
            f"Subtract the distance at {hours[i1]} from the distance at {hours[i2]}.",
            f"${y_vals[i2]} - {y_vals[i1]} = {change}\\text{{ km}}$.",
        ],
        "misconception_tags": ["interval_subtraction_error"],
    }


# -----------------------------------------------------------------------------
# 18. Misleading graphs: Truncated vertical axis identification
# -----------------------------------------------------------------------------
def arch_18_misleading_graphs_truncated_vertical_axis(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A company publishes a bar chart comparing sales between Product A (50 units) and Product B (55 units). "
        f"However, the vertical axis begins at 45 instead of 0, making Product B look twice as tall as Product A.\n"
        f"Explain why this presentation format is **misleading**."
    )
    correct_concept = "The vertical axis does not start at 0, exaggerating the visual difference between the products."
    return {
        "subskill": "18_misleading_graphs_truncated_vertical_axis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Axis does not start at zero (exaggerates differences)",
        "sample_answer": correct_concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify vertical axis truncation (does not start at 0)", "marks": 1},
            {"step": "Explain effect: exaggerates the visual difference between categories", "marks": 1},
        ],
        "hints": [
            "Look at the origin of the vertical axis.",
            "When an axis starts above 0, small differences appear disproportionately large.",
        ],
        "misconception_tags": ["unaware_of_axis_truncation_bias"],
    }


# -----------------------------------------------------------------------------
# 19. Misleading graphs: Non-uniform scale intervals
# -----------------------------------------------------------------------------
def arch_19_misleading_graphs_non_uniform_scale(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"On a line graph, the intervals along the horizontal axis are spaced equally, "
        f"but the labels represent: Year 2018, Year 2019, Year 2020, and Year 2024 (a jump of 4 years).\n"
        f"Explain why this representation creates a **misleading trend**."
    )
    explanation = "The time intervals are inconsistent (a jump of 4 years is given the same spacing as 1 year), distorting the apparent rate of change."
    return {
        "subskill": "19_misleading_graphs_non_uniform_scale",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Inconsistent time spacing distorts rate of change",
        "sample_answer": explanation,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify uneven time interval gap", "marks": 1},
            {"step": "Explain that rate of change / slope is distorted", "marks": 1},
        ],
        "hints": [
            "Notice that the jump from 2020 to 2024 is 4 years, while previous steps are only 1 year.",
            "Equal physical spacing for unequal time intervals distorts the slope of the line.",
        ],
        "misconception_tags": ["unaware_of_non_uniform_scaling"],
    }


# -----------------------------------------------------------------------------
# 20. Stem-and-leaf plot key reading
# -----------------------------------------------------------------------------
def arch_20_stem_and_leaf_plot_key_reading(r: random.Random) -> Dict[str, Any]:
    stem_val = r.choice([3, 4, 5, 6, 7])
    leaf_val = r.choice([2, 5, 8])
    real_val = stem_val * 10 + leaf_val

    prompt = (
        f"In an ordered stem-and-leaf plot, the key is given as:\n"
        f"**Key: {stem_val} | {leaf_val} represents {real_val}**.\n\n"
        f"What number does the entry **{stem_val + 1} | {leaf_val + 1}** represent?"
    )
    ans = (stem_val + 1) * 10 + (leaf_val + 1)
    ans_str = str(ans)
    sol = (
        f"Using the key, the stem represents tens and the leaf represents units:\n"
        f"$$\\text{{Value}} = ({stem_val + 1} \\times 10) + {leaf_val + 1} = {ans}$$"
    )
    return {
        "subskill": "20_stem_and_leaf_plot_key_reading",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply key to stem and leaf: {ans}", "marks": 1},
        ],
        "hints": [
            f"The stem represents the tens digit and the leaf represents the units digit.",
            f"Stem {stem_val + 1} and leaf {leaf_val + 1} make {ans}.",
        ],
        "misconception_tags": ["stem_and_leaf_place_value_error"],
    }


# -----------------------------------------------------------------------------
# 21. Reconstructing raw dataset from stem-and-leaf plot
# -----------------------------------------------------------------------------
def arch_21_reconstruct_data_from_stem_and_leaf(r: random.Random) -> Dict[str, Any]:
    stems = {
        2: [1, 4, 7],
        3: [0, 5],
        4: [2, 8],
    }
    # List of all numbers: 21, 24, 27, 30, 35, 42, 48
    all_nums = [21, 24, 27, 30, 35, 42, 48]
    total_items = len(all_nums)

    prompt = (
        f"A stem-and-leaf plot displays test scores:\n"
        f"```\n"
        f"2 | 1  4  7\n"
        f"3 | 0  5\n"
        f"4 | 2  8\n"
        f"Key: 2 | 1 = 21\n"
        f"```\n"
        f"How many total observations are represented in this stem-and-leaf plot?"
    )
    ans_str = str(total_items)
    sol = (
        f"Each leaf represents one distinct data value.\n"
        f"Counting all the leaves: $3 + 2 + 2 = {total_items}$ observations."
    )
    return {
        "subskill": "21_reconstruct_data_from_stem_and_leaf",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} observations",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Count number of leaves: {total_items}", "marks": 1},
        ],
        "hints": [
            "Count each digit in the 'leaf' columns; each leaf represents one data point.",
            f"There are {total_items} leaves in total.",
        ],
        "misconception_tags": ["counted_stems_instead_of_leaves"],
    }


# -----------------------------------------------------------------------------
# 22. Finding median from stem-and-leaf plot
# -----------------------------------------------------------------------------
def arch_22_finding_median_from_stem_and_leaf(r: random.Random) -> Dict[str, Any]:
    # 9 ordered values: e.g. 12, 15, 18, 20, 24, 26, 31, 33, 37 -> median is 5th value: 24
    base = r.choice([10, 20, 30])
    vals = [base + 2, base + 5, base + 8, base + 11, base + 14, base + 17, base + 21, base + 23, base + 29]
    median_val = vals[4]

    s1 = base // 10
    s2 = s1 + 1
    s3 = s1 + 2

    l1 = [v % 10 for v in vals if v // 10 == s1]
    l2 = [v % 10 for v in vals if v // 10 == s2]
    l3 = [v % 10 for v in vals if v // 10 == s3]

    l1_str = "  ".join(str(x) for x in l1)
    l2_str = "  ".join(str(x) for x in l2)
    l3_str = "  ".join(str(x) for x in l3)

    plot_str = (
        f"{s1} | {l1_str}\n"
        f"{s2} | {l2_str}\n"
        f"{s3} | {l3_str}\n"
        f"Key: {s1} | {l1[0]} = {vals[0]}"
    )

    prompt = (
        f"An ordered stem-and-leaf plot contains 9 observations:\n"
        f"```\n{plot_str}\n```\n"
        f"Determine the **median** of this dataset."
    )
    ans_str = str(median_val)
    sol = (
        f"Since there are 9 ordered observations, the median is the 5th value:\n"
        f"The ordered data is: {', '.join(str(x) for x in vals)}.\n"
        f"The 5th value is **{median_val}**."
    )
    return {
        "subskill": "22_finding_median_from_stem_and_leaf",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify 5th ordered position for 9 items", "marks": 1},
            {"step": f"Answer: {median_val}", "marks": 1},
        ],
        "hints": [
            "With 9 items, the median is the 5th item from the top: $\\frac{9+1}{2} = 5$.",
            f"The 5th value is {median_val}.",
        ],
        "misconception_tags": ["median_position_reading_error"],
    }


# -----------------------------------------------------------------------------
# 23. Finding range from stem-and-leaf plot
# -----------------------------------------------------------------------------
def arch_23_finding_range_from_stem_and_leaf(r: random.Random) -> Dict[str, Any]:
    min_v = r.randint(12, 19)
    max_v = r.randint(52, 59)
    range_val = max_v - min_v

    prompt = (
        f"In a stem-and-leaf plot, the minimum value is **{min_v}** and the maximum value is **{max_v}**.\n"
        f"Calculate the **range** of the data."
    )
    ans_str = str(range_val)
    sol = (
        f"$$\\text{{Range}} = \\text{{Maximum}} - \\text{{Minimum}} = {max_v} - {min_v} = {range_val}$$"
    )
    return {
        "subskill": "23_finding_range_from_stem_and_leaf",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Subtract min from max: {max_v} - {min_v} = {range_val}", "marks": 1},
        ],
        "hints": [
            "Range = Maximum value − Minimum value.",
            f"${max_v} - {min_v} = {range_val}$.",
        ],
        "misconception_tags": ["range_formula_error"],
    }


# -----------------------------------------------------------------------------
# 24. Double bar graph comparison
# -----------------------------------------------------------------------------
def arch_24_double_bar_graph_comparison(r: random.Random) -> Dict[str, Any]:
    boys = [r.randint(15, 30) for _ in range(3)]
    girls = [r.randint(15, 30) for _ in range(3)]
    grades = ["Grade 7", "Grade 8", "Grade 9"]

    i = r.randint(0, 2)
    b_val = boys[i]
    g_val = girls[i]
    diff = abs(b_val - g_val)
    more_group = "Boys" if b_val > g_val else ("Girls" if g_val > b_val else "Equal")

    prompt = (
        f"In a school sports survey comparing two groups, participant records in {grades[i]} show:\n"
        f"• Boys: {b_val}\n"
        f"• Girls: {g_val}\n\n"
        f"Calculate the difference between the number of boys and girls in {grades[i]}."
    )
    ans_str = str(diff)
    sol = (
        f"$$\\text{{Difference}} = |{b_val} - {g_val}| = {diff}\\text{{ learners}}$$"
    )
    return {
        "subskill": "24_double_bar_graph_comparison",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} learners",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate difference: |{b_val} - {g_val}| = {diff}", "marks": 1},
        ],
        "hints": [
            f"Subtract the smaller count from the larger count: $|{b_val} - {g_val}|$.",
            f"The difference is {diff}.",
        ],
        "misconception_tags": ["double_bar_series_confusion"],
    }


# -----------------------------------------------------------------------------
# 25. Choosing between mean and median for skewed data representation
# -----------------------------------------------------------------------------
def arch_25_choosing_mean_vs_median_for_skewed_data(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A company's salaries are skewed by two executives earning over R2 000 000 while all other workers earn R15 000.\n"
        f"Which measure of central tendency provides a more realistic representation of typical worker earnings: "
        f"the **'Mean'** or the **'Median'**?"
    )
    ans_str = "Median"
    sol = (
        f"The **Median** is the better measure because the extreme high salaries (outliers) "
        f"greatly distort and inflate the mean, making it unrepresentative of typical earnings."
    )
    return {
        "subskill": "25_choosing_mean_vs_median_for_skewed_data",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": "Median (not affected by extreme outliers)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify Median as appropriate measure", "marks": 1},
            {"step": "Explain that median is resistant to extreme outliers", "marks": 1},
        ],
        "hints": [
            "Outliers strongly distort the mean.",
            "The median is not affected by extreme high values.",
        ],
        "misconception_tags": ["mean_preferred_for_skewed_data"],
    }
