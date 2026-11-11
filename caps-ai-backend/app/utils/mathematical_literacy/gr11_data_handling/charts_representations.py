"""Subskills 37 to 44: Bar Charts, Histograms, Pie Charts, Line Graphs & Scatter Plots for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Single bar chart reading and category comparison with diagram_spec."""
    name = r.choice(SA_NAMES)
    categories = ["Groceries", "Transport", "Rent", "Electricity", "Entertainment"]
    amounts = [r.choice([2500, 3000]), r.choice([1200, 1500]), r.choice([4000, 4500]), r.choice([800, 1000]), r.choice([500, 600])]

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "bar_chart",
        "title": f"Monthly Household Expenditure Breakdown for {name}",
        "x_label": "Expenditure Category",
        "y_label": "Amount in Rands (R)",
        "bars": [{"category": c, "value": a} for c, a in zip(categories, amounts)],
    }

    max_idx = amounts.index(max(amounts))
    max_cat = categories[max_idx]
    max_amt = amounts[max_idx]

    prompt = (
        f"Refer to the accompanying bar chart showing {name}'s monthly expenditure.\n"
        f"Which category accounts for the largest expenditure, and what is the exact amount in Rands?"
    )

    correct_ans = f"{max_cat} ({_fmt_curr(max_amt)})"
    distractors = [f"{c} ({_fmt_curr(a)})" for c, a in zip(categories, amounts) if c != max_cat][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Locate the tallest bar on the chart [1 mark].\n"
        f"The tallest vertical bar corresponds to '{max_cat}'.\n"
        f"Step 2: Read the y-axis height [1 mark].\n"
        f"The height of the {max_cat} bar aligns with {_fmt_curr(max_amt)}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="37",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look for the tallest bar on the vertical bar chart and read its value from the vertical axis.",
        tier_2=f"The highest bar is '{max_cat}' reaching {_fmt_curr(max_amt)}.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )


def generate_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: Double (compound) bar chart interpretation comparing two groups."""
    years = ["2022", "2023", "2024"]
    ml_23 = r.choice([78, 80, 82, 84, 86])
    pm_23 = r.choice([58, 60, 62, 64])
    pass_mathlit = [ml_23 - r.randint(2, 4), ml_23, ml_23 + r.randint(1, 3)]
    pass_puremath = [pm_23 + r.randint(1, 2), pm_23, pm_23 + r.randint(2, 4)]

    diff_2023 = pass_mathlit[1] - pass_puremath[1]

    diagram_spec = {
        "diagram_role": "context",
        "kind": "double_bar_graph",
        "diagram_type": "double_bar_chart",
        "title": "National Matric Pass Rate Comparison: Mathematical Literacy vs Mathematics",
        "categories": years,
        "values": pass_mathlit,
        "values2": pass_puremath,
        "x_label": "Examination Year",
        "y_label": "Pass Rate (%)",
        "series": [
            {"name": "Mathematical Literacy", "data": [{"label": y, "value": v} for y, v in zip(years, pass_mathlit)]},
            {"name": "Mathematics (Pure)", "data": [{"label": y, "value": v} for y, v in zip(years, pass_puremath)]},
        ],
    }

    prompt = (
        f"A double bar chart compares the matric pass rates for Mathematical Literacy (blue bars) "
        f"and Pure Mathematics (orange bars) from 2022 to 2024. "
        f"In 2023, the pass rate was {pass_mathlit[1]}% for Mathematical Literacy and {pass_puremath[1]}% for Pure Mathematics.\n"
        f"By how many percentage points did Mathematical Literacy exceed Pure Mathematics in 2023?"
    )

    correct_ans = f"{diff_2023} percentage points"
    wrong_1 = f"{diff_2023 + 5} percentage points"
    wrong_2 = f"{diff_2023 - 4} percentage points"
    wrong_3 = f"{pass_mathlit[1]} percentage points"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Read the two bar heights for 2023 [1 mark].\n"
        f"Mathematical Literacy = {pass_mathlit[1]}%; Pure Mathematics = {pass_puremath[1]}%.\n"
        f"Step 2: Calculate difference [1 mark].\n"
        f"Difference = {pass_mathlit[1]}% - {pass_puremath[1]}% = {diff_2023} percentage points.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="38",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the height of the Pure Mathematics bar from the Mathematical Literacy bar for 2023.",
        tier_2=f"{pass_mathlit[1]} - {pass_puremath[1]} = {diff_2023}.",
        tier_3=f"Difference = {diff_2023} percentage points.",
        r=r,
        diagram_spec=diagram_spec,
    )


def generate_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Stacked (component) bar chart reading."""
    total_bill = r.choice([1500, 1800, 2000, 2400])
    elec_part = r.choice([900, 1000, 1200])
    water_part = total_bill - elec_part

    pct_elec = round((elec_part / total_bill) * 100, 1)

    prompt = (
        f"In a stacked component bar chart showing a municipal utility bill of {_fmt_curr(total_bill)}, "
        f"the lower section represents electricity ({_fmt_curr(elec_part)}) and the upper stacked section "
        f"represents water ({_fmt_curr(water_part)}).\n"
        f"What percentage of the total municipal bill is accounted for by electricity?"
    )

    correct_ans = f"{_fmt(pct_elec, 1)}%"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: State component percentage formula [1 mark].\n"
        f"\\text{{Percentage}} = \\left( \\frac{{\\text{{Electricity Amount}}}}{{\\text{{Total Bill}}}} \\right) \\times 100\\%.\n"
        f"Step 2: Substitute values [1 mark].\n"
        f"({_fmt(elec_part)} ÷ {_fmt(total_bill)}) × 100% = {_fmt(pct_elec, 1)}%.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="39",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the electricity portion by the total stacked bar height and multiply by 100.",
        tier_2=f"({_fmt(elec_part)} ÷ {_fmt(total_bill)}) × 100% = {_fmt(pct_elec, 1)}%.",
        tier_3=f"Answer: {_fmt(pct_elec, 1)}%.",
        r=r,
    )


def generate_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: Histogram vs Bar Chart structural distinction."""
    prompt = (
        f"Which of the following statements correctly describes the fundamental structural differences "
        f"between a Histogram and a standard Bar Chart?"
    )

    correct_ans = (
        "A histogram represents continuous numerical data where the vertical bars touch with no gaps between them, whereas a bar chart represents discrete/categorical data with spaces between bars"
    )
    wrong_1 = "A histogram is always circular while a bar chart is always rectangular"
    wrong_2 = "A bar chart has bars that must touch each other, while a histogram always separates bars with wide gaps"
    wrong_3 = "Histograms can only be drawn by government statisticians while bar charts are for school learners"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand histogram design principles [1 mark].\n"
        f"Histograms display continuous numerical data divided into class intervals; because the data flows continuously, adjacent bars touch.\n"
        f"Step 2: Understand bar chart conventions [1 mark].\n"
        f"Bar charts represent distinct discrete categories; spaces between bars emphasize separate categories.\n"
        f"Step 3: Stated distinction [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="40",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember: histograms display continuous data and have touching bars; bar charts display distinct categories with gaps.",
        tier_2="Identify the statement distinguishing continuous touching bars from separated categorical bars.",
        tier_3=f"Correct distinction: {correct_ans}.",
        r=r,
    )


def generate_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Pie chart sector angle calculation: (part / total) * 360°."""
    name = r.choice(SA_NAMES)
    total_learners = r.choice([120, 180, 240, 360, 480])
    part_learners = r.choice([30, 45, 60, 90])

    sector_angle = round((part_learners / total_learners) * 360, 1)

    prompt = (
        f"In a school of {_fmt(total_learners)} Grade 11 learners, exactly {_fmt(part_learners)} "
        f"travel to school by bicycle. "
        f"When representing this data on a pie chart, what should be the angle (in degrees) of the sector "
        f"representing bicycle commuters?"
    )

    correct_ans = f"{_fmt(sector_angle, 1)}°"
    wrong_1 = f"{_fmt(sector_angle * 0.5, 1)}°"
    wrong_2 = f"{_fmt(sector_angle + 20, 1)}°"
    wrong_3 = f"{_fmt(round((part_learners / total_learners) * 100, 1))}%"  # percentage mistake
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State the pie chart sector angle formula [1 mark].\n"
        f"\\text{{Angle}} = \\left( \\frac{{\\text{{Category Count}}}}{{\\text{{Total Count}}}} \\right) \\times 360^\\circ.\n"
        f"Step 2: Substitute values [1 mark].\n"
        f"\\text{{Angle}} = \\left( \\frac{{{part_learners}}}{{{total_learners}}} \\right) \\times 360^\\circ = {_fmt(sector_angle, 1)}^\\circ.\n"
        f"Step 3: Stated angle [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "pie_chart",
        "title": f"Learner Transport Modes ({name})",
        "sectors": [{"label": "Bicycle", "value": 60}, {"label": "Other", "value": 120}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="41",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Sector Angle = (Category Frequency ÷ Total) × 360°.",
        tier_2=f"Divide {part_learners} by {total_learners} and multiply by 360°.",
        tier_3=f"Angle = {_fmt(sector_angle, 1)}°.",
        r=r,
    )


def generate_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Subskill 42: Pie chart percentage to frequency conversion: (pct / 100) * Total."""
    total_people = r.choice([400, 500, 600, 800, 1000])
    pct = r.choice([25, 30, 35, 40, 45])
    count = int(total_people * (pct / 100))

    prompt = (
        f"A municipal council budget pie chart shows that {_fmt(pct)}% of the total budget of "
        f"{_fmt_curr(total_people * 10000)} is allocated to water infrastructure maintenance.\n"
        f"Calculate the exact amount allocated to water infrastructure in Rands."
    )

    correct_ans = _fmt_curr(count * 10000)
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Convert percentage to a decimal or fraction [1 mark].\n"
        f"{pct}% = {pct} ÷ 100 = {pct / 100}.\n"
        f"Step 2: Multiply by the total budget [1 mark].\n"
        f"Allocation = {pct / 100} × {_fmt_curr(total_people * 10000)} = {_fmt_curr(count * 10000)}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="42",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply total budget by the percentage divided by 100.",
        tier_2=f"{pct}% of {_fmt_curr(total_people * 10000)} = ({pct} ÷ 100) × {_fmt_curr(total_people * 10000)}.",
        tier_3=f"Allocation = {_fmt_curr(count * 10000)}.",
        r=r,
    )


def generate_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Subskill 43: Broken line graph interpretation: analyzing trends over time."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    rf_base = r.choice([115, 120, 125]); rainfall = [rf_base, rf_base - 10, 85, 45, 20, 10]  # Summer rainfall region trend

    prompt = (
        f"A broken line graph displays the average monthly rainfall (mm) in Pretoria from January to June:\n"
        f"• Jan: 120 mm | Feb: 110 mm | Mar: 85 mm | Apr: 45 mm | May: 20 mm | Jun: 10 mm\n"
        f"What overall climatic trend is shown by this broken line graph, and between which two consecutive months was the steepest decrease?"
    )

    correct_ans = "Overall decreasing rainfall trend; steepest decrease occurred between March and April (drop of 40 mm)"
    wrong_1 = "Overall increasing rainfall trend; steepest increase occurred between May and June"
    wrong_2 = "Constant uniform rainfall throughout all 6 months"
    wrong_3 = "Overall decreasing rainfall trend; steepest decrease occurred between January and February"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Inspect the slope of the line graph [1 mark].\n"
        f"The line slopes continuously downward from 120 mm to 10 mm (decreasing trend).\n"
        f"Step 2: Calculate consecutive monthly decreases [1 mark].\n"
        f"Jan–Feb: 10 mm; Feb–Mar: 25 mm; Mar–Apr: 85 - 45 = 40 mm; Apr–May: 25 mm; May–Jun: 10 mm.\n"
        f"The largest drop is 40 mm between March and April.\n"
        f"Step 3: Stated conclusion [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "broken_line_graph",
        "title": f"Average Monthly Rainfall in Pretoria (Base {rf_base} mm)",
        "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "values": [120, 110, 85, 45, 20, 10],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="43",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Check the overall direction of the line and calculate the difference between adjacent monthly points.",
        tier_2="Rainfall decreases from Jan to Jun. The biggest drop is from 85 mm to 45 mm (40 mm) between March and April.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Scatter plots: correlation direction and strength."""
    correlation_scenario = r.choice([
        (
            "Study hours per week vs Mathematics examination mark",
            "Strong Positive Correlation",
            "as study hours increase, exam marks generally increase; points slope upwards from left to right"
        ),
        (
            "Age of a second-hand motor vehicle vs its resale market value",
            "Strong Negative Correlation",
            "as vehicle age increases, resale value depreciates and decreases; points slope downwards from left to right"
        ),
        (
            "Learner shoe size vs performance score on a history quiz",
            "Zero Correlation (No Relationship)",
            "shoe size has no logical or mathematical connection to history knowledge; points are scattered randomly with no line trend"
        ),
    ])
    variables, corr_type, corr_reason = correlation_scenario

    prompt = (
        f"A scatter plot is plotted showing bivariate data for: **{variables}**.\n"
        f"How is the correlation between these two variables described?"
    )

    correct_ans = f"{corr_type} ({corr_reason})"
    distractors = [
        f"{other[1]} ({other[2]})"
        for other in [
            ("", "Strong Positive Correlation", "points slope upwards from left to right"),
            ("", "Strong Negative Correlation", "points slope downwards from left to right"),
            ("", "Zero Correlation (No Relationship)", "points are scattered randomly with no line trend"),
        ]
        if other[1] != corr_type
    ][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Analyze the relationship between the two variables [1 mark].\n"
        f"Variables: {variables}.\n"
        f"Step 2: Determine trend direction [1 mark].\n"
        f"{corr_reason}.\n"
        f"Step 3: Stated correlation [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="44",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine whether an increase in one variable leads to an increase, decrease, or has no effect on the other.",
        tier_2=f"{corr_reason}.",
        tier_3=f"Correlation: {corr_type}.",
        r=r,
    )
