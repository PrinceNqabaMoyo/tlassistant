"""Grade 7 Mathematics - Interpret, Analyse and Report on Data: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 4/01. Interpret analyse and report on data.md
Focus: Histograms (intervals), Pie charts (angles, percentages), Line graphs (trends), Stem-and-leaf plots, Bias and misleading data representations, choosing appropriate measures, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_histogram_display(intervals: List[str], freqs: List[int], title: str) -> str:
    """Renders a clean static 2D SVG histogram with contiguous bars."""
    w, h = 340, 220
    max_f = max(freqs) if freqs else 10
    scale_y = 120 / max_f

    bars = []
    n = len(intervals)
    bar_w = 48
    start_x = 55

    for i, (intl, frq) in enumerate(zip(intervals, freqs)):
        bx = start_x + i * bar_w
        bh = int(frq * scale_y)
        by = 170 - bh
        bars.append(f'<rect x="{bx}" y="{by}" width="{bar_w}" height="{bh}" fill="#6366f1" stroke="#4338ca" stroke-width="1.5"/>')
        bars.append(f'<text x="{bx + bar_w // 2}" y="{by - 4}" text-anchor="middle" font-size="10" font-weight="bold" fill="#312e81">{frq}</text>')
        bars.append(f'<text x="{bx + bar_w // 2}" y="185" text-anchor="middle" font-size="9" fill="#475569">{intl}</text>')

    axes = [
        '<line x1="45" y1="30" x2="45" y2="170" stroke="#64748b" stroke-width="1.5"/>',
        f'<line x1="45" y1="170" x2="{start_x + n * bar_w + 15}" y2="170" stroke="#64748b" stroke-width="1.5"/>',
        f'<text x="170" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">{title}</text>',
        '<text x="15" y="100" text-anchor="middle" font-size="10" fill="#64748b" transform="rotate(-90 15 100)">Frequency</text>'
    ]

    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'{"".join(axes)}{"".join(bars)}'
        f'</svg>'
    )


def _svg_stem_and_leaf(last_leaf: int = 6) -> str:
    """Renders a clean static 2D SVG stem-and-leaf plot."""
    w, h = 300, 180
    lines = [
        '<line x1="75" y1="35" x2="75" y2="155" stroke="#475569" stroke-width="2"/>',
        '<text x="45" y="30" font-size="11" font-weight="bold" fill="#1e293b">Stem</text>',
        '<text x="95" y="30" font-size="11" font-weight="bold" fill="#1e293b">Leaf</text>',
        '<text x="50" y="60" font-size="12" fill="#334155">1</text><text x="95" y="60" font-size="12" fill="#0284c7">2  5  8</text>',
        '<text x="50" y="90" font-size="12" fill="#334155">2</text><text x="95" y="90" font-size="12" fill="#0284c7">0  3  3  7</text>',
        '<text x="50" y="120" font-size="12" fill="#334155">3</text><text x="95" y="120" font-size="12" fill="#0284c7">1  4  9</text>',
        f'<text x="50" y="150" font-size="12" fill="#334155">4</text><text x="95" y="150" font-size="12" fill="#0284c7">2  {last_leaf}</text>',
        '<text x="150" y="172" text-anchor="middle" font-size="10" fill="#64748b">Key: 2 | 3 = 23 marks</text>'
    ]
    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'{"".join(lines)}'
        f'</svg>'
    )


# 26. Double bar graph gender comparison census
def arch_26_double_bar_graph_gender_comparison_census(rng: random.Random) -> Dict[str, Any]:
    ans = "Grade 8 has the highest percentage of females (51,1%); Grade 4 has the lowest (47,9%)"
    prompt = (
        "Based on the national *Census @ School Results*, the table below shows the percentage distribution "
        "of male and female learners from Grade 3 to Grade 8:\n\n"
        "| Grade | Male (%) | Female (%) |\n"
        "| :--- | :--- | :--- |\n"
        "| 3 | 51,6 | 48,4 |\n"
        "| 4 | 52,1 | 47,9 |\n"
        "| 5 | 51,0 | 49,0 |\n"
        "| 6 | 50,3 | 49,7 |\n"
        "| 7 | 50,6 | 49,4 |\n"
        "| 8 | 48,9 | 51,1 |\n\n"
        "1. Which grade has the highest percentage of females?\n"
        "2. Which grade has the lowest percentage of females?\n"
        "3. Describe the overall trend in female enrollment percentage from Grade 4 to Grade 8."
    )
    sol = (
        "**Analysis of the Data Table:**\n"
        "1. **Highest Female Percentage:** Grade 8 with $51{,}1\\%$.\n"
        "2. **Lowest Female Percentage:** Grade 4 with $47{,}9\\%$.\n"
        "3. **Trend:** The percentage of female learners steadily increases as the grade level increases "
        "(from $47{,}9\\%$ in Grade 4 up to $51{,}1\\%$ in Grade 8)."
    )
    return {
        "id": f"g7_dm_26_{rng.randint(100000, 999999)}",
        "subskill": "26_double_bar_graph_gender_comparison_census",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Highest: Grade 8 (51,1%); Lowest: Grade 4 (47,9%); Trend: Female percentage increases with grade",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_26",
        "hints": {
            "tier_1": "Look down the 'Female (%)' column to find the largest and smallest numbers.",
            "tier_2": "Largest is 51,1% in Grade 8; smallest is 47,9% in Grade 4.",
            "tier_3": f"{ans}"
        },
        "misconception_tags": ["reading_male_instead_of_female_column"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies Grade 8 highest (51,1%)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identifies Grade 4 lowest (47,9%)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Describes increasing female trend with higher grade", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 27. Histogram interpretation grouped intervals SVG
def arch_27_histogram_interpretation_grouped_intervals_svg(rng: random.Random) -> Dict[str, Any]:
    intervals = ["10-19", "20-29", "30-39", "40-49"]
    f1 = rng.choice([6, 8, 9, 11])
    f2 = rng.choice([14, 15, 16])
    f3 = rng.choice([20, 22, 24])
    f4 = rng.choice([10, 12])
    freqs = [f1, f2, f3, f4]
    svg = _svg_histogram_display(intervals, freqs, "Mathematics Exam Mark Intervals")
    total = sum(freqs)
    ans = f"{total} learners; contiguous bars represent continuous grouped numerical data"
    prompt = (
        "Inspect the histogram diagram below showing learner exam marks in grouped intervals:\n\n"
        "1. How many total learners wrote the examination?\n"
        "2. Why do the bars in a histogram touch each other with no gaps, unlike a bar graph?"
    )
    sol = (
        f"**1. Total Number of Learners:**\n"
        f"$$\\text{{Total}} = {f1} + {f2} + {f3} + {f4} = {total}\\text{{ learners}}$$\n\n"
        f"**2. Touching Bars Explanation:**\n"
        f"The bars touch with no gaps because the horizontal axis represents continuous grouped numerical data. "
        f"There are no empty spaces between consecutive score class intervals."
    )
    return {
        "id": f"g7_dm_27_{rng.randint(100000, 999999)}",
        "subskill": "27_histogram_interpretation_grouped_intervals_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Total: {total} learners; bars touch because data is continuous grouped numerical data",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_27",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Add the frequencies of all four bars together.",
            "tier_2": f"{f1} + {f2} + {f3} + {f4} = {total}.",
            "tier_3": f"Total = {total}; bars touch because intervals are continuous."
        },
        "misconception_tags": ["confusing_histogram_with_bar_graph"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates total learners = {total}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains continuous grouped data has no gaps between intervals", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 28. Histogram modal interval identification
def arch_28_histogram_modal_interval_identification(rng: random.Random) -> Dict[str, Any]:
    intervals = ["0-9", "10-19", "20-29", "30-39"]
    mod_f = rng.choice([30, 32, 35, 38])
    freqs = [rng.randint(4, 8), rng.randint(15, 20), mod_f, rng.randint(12, 16)]
    svg = _svg_histogram_display(intervals, freqs, "Weekly Hours of Screen Time")
    ans = f"20-29 hours (frequency = {mod_f})"
    prompt = (
        "Refer to the histogram diagram showing weekly hours of screen time for a Grade 7 cohort:\n\n"
        "1. Identify the **modal interval** (the class interval with the highest frequency).\n"
        "2. What is the frequency of this modal interval?"
    )
    sol = (
        "**Analysis:**\n"
        "1. The tallest bar on the histogram corresponds to the interval **20-29 hours**.\n"
        f"2. The height of this bar indicates a frequency of **{mod_f} learners**.\n\n"
        "$$\\therefore \\text{Modal Interval} = 20-29 \\text{ hours}$$"
    )
    return {
        "id": f"g7_dm_28_{rng.randint(100000, 999999)}",
        "subskill": "28_histogram_modal_interval_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Modal interval is 20-29 hours with frequency {mod_f}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_28",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Find the tallest bar in the histogram.",
            "tier_2": f"The tallest bar is 20-29 with height {mod_f}.",
            "tier_3": f"{ans}"
        },
        "misconception_tags": ["reading_frequency_instead_of_interval_for_mode"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies modal interval: 20-29", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"States frequency = {mod_f}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 29. Histogram count learners above threshold
def arch_29_histogram_count_learners_above_threshold(rng: random.Random) -> Dict[str, Any]:
    intervals = ["0-19", "20-39", "40-59", "60-79", "80-100"]
    freqs = [4, 8, 16, 24, 12]
    total_passed = 24 + 12
    ans = f"{total_passed} learners"
    prompt = (
        "A histogram of test percentages shows the following frequencies across mark bins:\n\n"
        "- $0-19\\%$: $4$\n"
        "- $20-39\\%$: $8$\n"
        "- $40-59\\%$: $16$\n"
        "- $60-79\\%$: $24$\n"
        "- $80-100\\%$: $12$\n\n"
        "How many learners achieved a mark of **$60\\%$ or higher**?"
    )
    sol = (
        "**Calculation:**\n"
        "Mark bins containing $60\\%$ or higher are:\n"
        "- $60-79\\%$: $24$ learners\n"
        "- $80-100\\%$: $12$ learners\n\n"
        f"$$\\text{{Total}} = 24 + 12 = {total_passed}\\text{{ learners}}$$"
    )
    return {
        "id": f"g7_dm_29_{rng.randint(100000, 999999)}",
        "subskill": "29_histogram_count_learners_above_threshold",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{total_passed}",
        "sample_answer": f"{total_passed} learners",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_29",
        "hints": {
            "tier_1": "Add the counts for the two intervals 60-79% and 80-100%.",
            "tier_2": f"24 + 12 = {total_passed}.",
            "tier_3": f"{total_passed} learners."
        },
        "misconception_tags": ["omitting_highest_bin_in_threshold"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies intervals 60-79 and 80-100", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates sum = {total_passed}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 30. Pie chart interpretation percentage sectors SVG
def arch_30_pie_chart_interpretation_percentage_sectors_svg(rng: random.Random) -> Dict[str, Any]:
    ans = "Savings = 10% (R500); Food is the largest expense (40%)"
    prompt = (
        "A family's monthly budget of $\\text{R}5\\,000$ is represented in a pie chart with percentage sectors:\n\n"
        "- Rent: $30\\%$\n"
        "- Food: $40\\%$\n"
        "- Transport: $20\\%$\n"
        "- Savings: Remaining sector\n\n"
        "1. What percentage of the budget is allocated to Savings?\n"
        "2. How much money in Rands (R) is saved each month?"
    )
    sol = (
        "**1. Savings Percentage:**\n"
        "The complete pie chart equals $100\\%$:\n"
        "$$\\text{Savings} = 100\\% - (30\\% + 40\\% + 20\\%) = 100\\% - 90\\% = 10\\%$$\n\n"
        "**2. Rand Amount for Savings:**\n"
        "$$\\text{Amount} = 10\\% \\text{ of } \\text{R}5\\,000 = \\frac{10}{100} \\times 5\\,000 = \\text{R}500$$"
    )
    return {
        "id": f"g7_dm_30_{rng.randint(100000, 999999)}",
        "subskill": "30_pie_chart_interpretation_percentage_sectors_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Savings is 10%; amount is R500",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_30",
        "hints": {
            "tier_1": "All sectors in a pie chart add up to 100%.",
            "tier_2": "100 - (30 + 40 + 20) = 10%. 10% of R5 000 is R500.",
            "tier_3": "10% and R500."
        },
        "misconception_tags": ["pie_chart_not_summing_to_100"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates savings percentage = 10%", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates savings amount = R500", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 31. Pie chart calculate sector angle
def arch_31_pie_chart_calculate_sector_angle(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([15, 20, 25, 30, 40])
    angle = int((pct / 100) * 360)
    ans = f"{angle} degrees"
    prompt = (
        f"In a school survey, **{pct}\\%** of learners chose soccer as their favorite sport.\n\n"
        f"Calculate the **size of the sector angle** (in degrees) that will represent soccer in a pie chart."
    )
    sol = (
        f"**Step 1: Formula for Pie Chart Sector Angle:**\n"
        f"$$\\text{{Angle}} = \\frac{{\\text{{Percentage}}}}{{100}} \\times 360^\\circ$$\n\n"
        f"**Step 2: Calculate:**\n"
        f"$$\\text{{Angle}} = \\frac{{{pct}}}{{100}} \\times 360^\\circ = {pct} \\times 3{{,}}6^\\circ = {angle}^\\circ$$"
    )
    return {
        "id": f"g7_dm_31_{rng.randint(100000, 999999)}",
        "subskill": "31_pie_chart_calculate_sector_angle",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{angle}",
        "sample_answer": f"{angle} degrees",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_31",
        "hints": {
            "tier_1": "A full circle has 360 degrees.",
            "tier_2": f"Find {pct}% of 360° by computing ({pct} / 100) × 360.",
            "tier_3": f"Sector angle = {angle}°."
        },
        "misconception_tags": ["multiplying_by_180_instead_of_360_for_pie_chart"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Multiplies percentage fraction by 360 degrees", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates sector angle = {angle} degrees", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 32. Pie chart convert percentage to raw frequency
def arch_32_pie_chart_convert_percentage_to_raw_frequency(rng: random.Random) -> Dict[str, Any]:
    total_learners = 400
    pct = rng.choice([15, 25, 35])
    raw_count = int((pct / 100) * total_learners)
    ans = f"{raw_count} learners"
    prompt = (
        f"A total of {total_learners} learners participated in a subject choice survey. "
        f"On a pie chart displaying the results, the sector for Art represents **{pct}\\%**.\n\n"
        f"How many individual learners chose Art?"
    )
    sol = (
        f"**Calculation:**\n"
        f"$$\\text{{Number of learners}} = {pct}\\% \\text{{ of }} {total_learners}$$\n"
        f"$$= \\frac{{{pct}}}{{100}} \\times {total_learners} = {pct} \\times 4 = {raw_count}\\text{{ learners}}$$"
    )
    return {
        "id": f"g7_dm_32_{rng.randint(100000, 999999)}",
        "subskill": "32_pie_chart_convert_percentage_to_raw_frequency",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{raw_count}",
        "sample_answer": f"{raw_count} learners",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_32",
        "hints": {
            "tier_1": f"Calculate {pct} / 100 × {total_learners}.",
            "tier_2": f"{pct} × 4 = {raw_count}.",
            "tier_3": f"{raw_count} learners."
        },
        "misconception_tags": ["percentage_multiplication_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Sets up ({pct}/100) * {total_learners}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates count = {raw_count}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 33. Pie chart fractional shares budget
def arch_33_pie_chart_fractional_shares_budget(rng: random.Random) -> Dict[str, Any]:
    ans = "1/4 or 25%"
    prompt = (
        "A pie chart shows that half (1/2) of a municipal budget goes to Health, "
        "one quarter (1/4) goes to Education, and the remaining equal amount is shared between Housing and Roads.\n\n"
        "What fraction of the budget is allocated to Housing and Roads combined?"
    )
    sol = (
        "**Calculation:**\n"
        "$$\\text{Combined Health and Education} = \\frac{1}{2} + \\frac{1}{4} = \\frac{2}{4} + \\frac{1}{4} = \\frac{3}{4}$$\n\n"
        "$$\\text{Remaining for Housing and Roads} = 1 - \\frac{3}{4} = \\frac{1}{4} \\text{ (or } 25\\%)$$ \n"
    )
    return {
        "id": f"g7_dm_33_{rng.randint(100000, 999999)}",
        "subskill": "33_pie_chart_fractional_shares_budget",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1/4 or 25%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_33",
        "hints": {
            "tier_1": "Add 1/2 + 1/4 = 3/4.",
            "tier_2": "Subtract 3/4 from the whole 1.",
            "tier_3": "1/4 (or 25%)."
        },
        "misconception_tags": ["fraction_subtraction_from_whole_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates combined known fraction = 3/4", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Finds remaining fraction = 1/4 (25%)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 34. Line graph temperature trend over time SVG
def arch_34_line_graph_temperature_trend_over_time_svg(rng: random.Random) -> Dict[str, Any]:
    ans = "Temperature increases from 06:00 to 14:00 (peaks at 28 °C), then decreases until 18:00"
    prompt = (
        "A broken line graph records hourly temperatures in Durban on a summer day:\n\n"
        "- 06:00: $18^\\circ\\text{C}$\n"
        "- 10:00: $24^\\circ\\text{C}$\n"
        "- 14:00: $28^\\circ\\text{C}$\n"
        "- 18:00: $22^\\circ\\text{C}$\n\n"
        "1. At what time was the maximum temperature recorded, and what was its value?\n"
        "2. Describe the overall temperature trend across the 12-hour period."
    )
    sol = (
        "**Analysis:**\n"
        "1. **Peak Temperature:** Recorded at **14:00** with a value of **$28^\\circ\\text{C}$**.\n"
        "2. **Trend:** The temperature rose steadily during the morning and early afternoon from $18^\\circ\\text{C}$ to $28^\\circ\\text{C}$, "
        "and then cooled down towards the evening to $22^\\circ\\text{C}$."
    )
    return {
        "id": f"g7_dm_34_{rng.randint(100000, 999999)}",
        "subskill": "34_line_graph_temperature_trend_over_time_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Peak at 14:00 (28 °C); rises to midday then cools in late afternoon",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_34",
        "hints": {
            "tier_1": "Which time has 28 °C?",
            "tier_2": "Look at how the values go up and then down.",
            "tier_3": f"{ans}"
        },
        "misconception_tags": ["misreading_line_graph_peak"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies peak at 14:00 (28 °C)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Describes rise followed by decline", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 35. Line graph interpolate and predict
def arch_35_line_graph_interpolate_and_predict(rng: random.Random) -> Dict[str, Any]:
    ans = "Interpolate: estimate within data range; Extrapolate: predict beyond data range"
    prompt = (
        "In data analysis and line graph interpretation:\n\n"
        "1. Define what it means to **interpolate** a value from a line graph.\n"
        "2. Define what it means to **extrapolate** (predict) a value from a line graph.\n"
        "3. Which estimation is generally more reliable: interpolation or extrapolation? Why?"
    )
    sol = (
        "**1. Interpolation:**\n"
        "Estimating an unknown value *between* two known recorded data points on a graph.\n\n"
        "**2. Extrapolation:**\n"
        "Predicting a future or unknown value *beyond* the range of the existing recorded data points by extending the trend.\n\n"
        "**3. Reliability:**\n"
        "**Interpolation** is much more reliable because it is constrained within known boundaries, whereas extrapolation assumes "
        "trends will continue indefinitely without unexpected changes."
    )
    return {
        "id": f"g7_dm_35_{rng.randint(100000, 999999)}",
        "subskill": "35_line_graph_interpolate_and_predict",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Interpolate is inside data range, extrapolate is outside; interpolation is more reliable",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_35",
        "hints": {
            "tier_1": "'Inter' means between or inside. 'Extra' means outside or beyond.",
            "tier_2": "Interpolation estimates between known points; extrapolation extends beyond known points.",
            "tier_3": "Interpolation is more reliable because it is within known limits."
        },
        "misconception_tags": ["confusing_interpolation_with_extrapolation"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Defines interpolation as estimation within known points", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Defines extrapolation as prediction beyond data range", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Explains interpolation is more reliable", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 36. Stem and leaf display reading values SVG
def arch_36_stem_and_leaf_display_reading_values_svg(rng: random.Random) -> Dict[str, Any]:
    last_l = rng.choice([5, 6, 7, 8, 9])
    svg = _svg_stem_and_leaf(last_l)
    hi_v = 40 + last_l
    ans = f"12 values; Lowest = 12, Highest = {hi_v}"
    prompt = (
        "Inspect the stem-and-leaf plot diagram below:\n\n"
        "1. What is the total number of data values represented in the plot?\n"
        "2. What are the lowest and highest values in the dataset?\n"
        "3. Read and list all data values in the second row (Stem 2)."
    )
    sol = (
        "**1. Total Values:**\n"
        "Counting each leaf: $3 + 4 + 3 + 2 = 12$ data values.\n\n"
        "**2. Lowest and Highest:**\n"
        "- Lowest value: Stem $1$, Leaf $2 = 12$.\n"
        f"- Highest value: Stem $4$, Leaf ${last_l} = {hi_v}$.\n\n"
        "**3. Second Row (Stem 2):**\n"
        "Values are: $20, 23, 23, 27$."
    )
    return {
        "id": f"g7_dm_36_{rng.randint(100000, 999999)}",
        "subskill": "36_stem_and_leaf_display_reading_values_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"12 values; Lowest is 12, Highest is {hi_v}; Stem 2 values are 20, 23, 23, 27",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_36",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Count each leaf number across all rows.",
            "tier_2": f"Stem 1 has 12, 15, 18. Stem 4 has 42, {hi_v}.",
            "tier_3": f"{ans}"
        },
        "misconception_tags": ["reading_leaf_without_stem"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Counts 12 values", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"States lowest = 12 and highest = {hi_v}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Lists Stem 2 values: 20, 23, 23, 27", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 37. Stem and leaf find median and mode
def arch_37_stem_and_leaf_find_median_and_mode(rng: random.Random) -> Dict[str, Any]:
    # Dataset from SVG: 12, 15, 18, 20, 23, 23, 27, 31, 34, 39, 42, 46 (n = 12)
    # Middle two: 6th (23) and 7th (27) -> median = 25
    # Mode: 23 (repeats twice)
    ans = "Median = 25; Mode = 23"
    prompt = (
        "Refer to the stem-and-leaf plot showing test marks:\n\n"
        "Key: $2 \\mid 3 = 23$\n\n"
        "- Stem 1: $2, 5, 8$\n"
        "- Stem 2: $0, 3, 3, 7$\n"
        "- Stem 3: $1, 4, 9$\n"
        "- Stem 4: $2, 6$\n\n"
        "1. Determine the **median** mark.\n"
        "2. Determine the **mode** of the dataset."
    )
    sol = (
        "**Step 1: Find the Median ($n = 12$):**\n"
        "The values are already ordered:\n"
        "$$12, 15, 18, 20, 23, \\mathbf{23}, \\mathbf{27}, 31, 34, 39, 42, 46$$\n"
        "The two middle values (positions $6$ and $7$) are $23$ and $27$:\n"
        "$$\\text{Median} = \\frac{23 + 27}{2} = \\frac{50}{2} = 25$$\n\n"
        "**Step 2: Find the Mode:**\n"
        "The value **23** appears twice (two 3s in Stem 2), while every other value appears once.\n"
        "$$\\therefore \\text{Mode} = 23$$"
    )
    return {
        "id": f"g7_dm_37_{rng.randint(100000, 999999)}",
        "subskill": "37_stem_and_leaf_find_median_and_mode",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Median = 25; Mode = 23",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_37",
        "hints": {
            "tier_1": "There are 12 items. Find the average of the 6th and 7th numbers.",
            "tier_2": "6th number is 23, 7th is 27. (23 + 27) / 2 = 25.",
            "tier_3": "Median is 25; Mode is 23."
        },
        "misconception_tags": ["picking_single_leaf_as_mode"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies 6th and 7th values as 23 and 27", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates median = 25", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Identifies mode = 23", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 38. Stem and leaf calculate range
def arch_38_stem_and_leaf_calculate_range(rng: random.Random) -> Dict[str, Any]:
    # 46 - 12 = 34
    ans = "34 marks"
    prompt = (
        "Using the stem-and-leaf plot:\n\n"
        "- Stem 1: $2, 5, 8$\n"
        "- Stem 2: $0, 3, 3, 7$\n"
        "- Stem 3: $1, 4, 9$\n"
        "- Stem 4: $2, 6$\n\n"
        "Key: $2 \\mid 3 = 23$ marks\n\n"
        "Calculate the **range** of marks in this dataset."
    )
    sol = (
        "**Calculation:**\n"
        "- Highest mark: Stem $4$, Leaf $6 = 46$\n"
        "- Lowest mark: Stem $1$, Leaf $2 = 12$\n\n"
        "$$\\text{Range} = \\text{Maximum} - \\text{Minimum} = 46 - 12 = 34\\text{ marks}$$"
    )
    return {
        "id": f"g7_dm_38_{rng.randint(100000, 999999)}",
        "subskill": "38_stem_and_leaf_calculate_range",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": "34",
        "sample_answer": "34 marks",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_38",
        "hints": {
            "tier_1": "Find the highest mark (46) and lowest mark (12).",
            "tier_2": "Subtract 12 from 46.",
            "tier_3": "Range = 46 - 12 = 34."
        },
        "misconception_tags": ["subtracting_leaves_only_for_range"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies max 46 and min 12", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates range = 34", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 39. Identifying bias in survey sample
def arch_39_identifying_bias_in_survey_sample(rng: random.Random) -> Dict[str, Any]:
    ans = "Sample is biased because only rugby team members were surveyed, not representative of whole school"
    prompt = (
        "A school newspaper journalist wants to determine the most popular sport among all $800$ learners in a school.\n"
        "The journalist surveys $50$ learners immediately after rugby practice outside the school rugby clubhouse.\n\n"
        "1. Is this sample **biased** or **unbiased**? Explain why.\n"
        "2. How could the journalist select an unbiased, representative sample of the school?"
    )
    sol = (
        "**1. Bias Identification:**\n"
        "The sample is **biased**. Learners attending rugby practice are far more likely to favor rugby than the general school population. "
        "The sample excludes learners who do not play rugby, girls (if it is a boys' team), or learners participating in other cultural and sporting activities.\n\n"
        "**2. Unbiased Alternative:**\n"
        "The journalist should use **random sampling**, for example selecting every 10th learner from the official school attendance register, "
        "ensuring all grades, genders, and interest groups have an equal chance of being selected."
    )
    return {
        "id": f"g7_dm_39_{rng.randint(100000, 999999)}",
        "subskill": "39_identifying_bias_in_survey_sample",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Biased because surveying rugby players favors rugby; use random sampling from school register instead",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_39",
        "hints": {
            "tier_1": "Are rugby players likely to choose rugby as their favorite sport?",
            "tier_2": "Yes. This creates bias because it doesn't represent everyone in the school.",
            "tier_3": "Biased sample; fix by selecting random learners from the school register."
        },
        "misconception_tags": ["assuming_convenience_sample_is_unbiased"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "States sample is biased", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains why (over-represents rugby players, excludes others)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Suggests valid random sampling method across register", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 40. Identifying bias in leading survey questions
def arch_40_identifying_bias_in_leading_survey_questions(rng: random.Random) -> Dict[str, Any]:
    ans = "Leading question that nudges respondent towards agreeing; rephrase neutrally without loaded words"
    prompt = (
        "Consider the following survey question written by a learner:\n\n"
        "*'Don't you agree that homework is boring and should be completely banned?'*\n\n"
        "1. Explain why this question is considered a **leading (biased) question**.\n"
        "2. Rewrite the question so that it is neutral and unbiased."
    )
    sol = (
        "**1. Why It Is Biased:**\n"
        "The phrasing is leading because it uses negative emotional language ('boring') and nudges the respondent "
        "toward agreeing with the author's viewpoint ('Don't you agree...').\n\n"
        "**2. Neutral Rephrasing:**\n"
        "*'What is your opinion on homework? (A) It is very beneficial, (B) It is somewhat beneficial, (C) It is not beneficial.'* "
        "or: *'Do you support or oppose homework? Explain your views.'*"
    )
    return {
        "id": f"g7_dm_40_{rng.randint(100000, 999999)}",
        "subskill": "40_identifying_bias_in_leading_survey_questions",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Leading question nudging an answer; neutral rewrite: What is your opinion regarding homework?",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_40",
        "hints": {
            "tier_1": "Does the question push the person to say yes?",
            "tier_2": "Phrases like 'Don't you agree...' influence the respondent.",
            "tier_3": "It is leading/biased. Rewrite neutrally."
        },
        "misconception_tags": ["authoring_leading_survey_questions"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Explains leading phrasing pushes respondent to agree", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Provides neutral rephrased question", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 41. Misleading graph truncated axis trap SVG
def arch_41_misleading_graph_truncated_axis_trap_svg(rng: random.Random) -> Dict[str, Any]:
    y_sales = rng.choice([97, 98, 99])
    x_sales = y_sales + 4
    base_y = y_sales - 2
    svg = (
        f'<svg viewBox="0 0 280 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<line x1="50" y1="20" x2="50" y2="150" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="50" y1="150" x2="240" y2="150" stroke="#64748b" stroke-width="1.5"/>'
        f'<text x="42" y="153" text-anchor="end" font-size="10" fill="#dc2626">{base_y}</text>'
        f'<text x="42" y="123" text-anchor="end" font-size="10" fill="#475569">{y_sales}</text>'
        f'<text x="42" y="45" text-anchor="end" font-size="10" fill="#475569">{x_sales}</text>'
        f'<rect x="80" y="120" width="45" height="30" fill="#94a3b8" stroke="#475569"/>'
        f'<text x="102" y="165" text-anchor="middle" font-size="10" font-weight="bold">Brand Y ({y_sales})</text>'
        f'<rect x="155" y="40" width="45" height="110" fill="#2563eb" stroke="#1d4ed8"/>'
        f'<text x="177" y="165" text-anchor="middle" font-size="10" font-weight="bold">Brand X ({x_sales})</text>'
        f'</svg>'
    )
    ans = "Vertical axis does not start at 0 (truncated axis), making small differences look massive"
    prompt = (
        f"A company advertises that Brand X sales skyrocketed compared to Brand Y.\n"
        f"The chart illustrates:\n"
        f"- Brand Y bar height = 2 cm (representing {y_sales} sales)\n"
        f"- Brand X bar height = 8 cm (representing {x_sales} sales)\n"
        f"The vertical axis starts at {base_y} instead of 0.\n\n"
        f"1. What visual trick makes this chart misleading?\n"
        f"2. What is the actual numerical difference in sales between Brand X and Brand Y?"
    )
    sol = (
        f"**1. Misleading Feature:**\n"
        f"The chart uses a **truncated vertical axis** (it starts at {base_y} instead of 0). "
        f"This exaggerates the visual difference: Brand X looks 4 times taller than Brand Y, "
        f"even though the actual difference is only ${x_sales} - {y_sales} = 4$ sales.\n\n"
        f"**2. Actual Difference:**\n"
        f"$$\\text{{Difference}} = {x_sales} - {y_sales} = 4\\text{{ sales}}$$"
    )
    return {
        "id": f"g7_dm_41_{rng.randint(100000, 999999)}",
        "subskill": "41_misleading_graph_truncated_axis_trap_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": "Truncated vertical axis exaggerates small differences; actual difference is only 4 sales",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_41",
        "hints": {
            "tier_1": "Where does the vertical axis begin? Does it start at zero?",
            "tier_2": f"Starting at {base_y} makes {x_sales} look huge compared to {y_sales}.",
            "tier_3": "Truncated axis exaggerates tiny differences."
        },
        "misconception_tags": ["falling_for_truncated_axis_trick"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies truncated vertical axis not starting at 0", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains visual exaggeration (looks 4x bigger)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Calculates real difference is only 4 sales", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 42. Misleading graph unequal scaling or width
def arch_42_misleading_graph_unequal_scaling_or_width(rng: random.Random) -> Dict[str, Any]:
    ans = "Bars of unequal width deceive the eye by increasing area disproportionately"
    prompt = (
        "In a presentation, one bar on a bar chart is drawn twice as wide as all the other bars.\n\n"
        "Explain why drawing bars of unequal widths on a bar chart is mathematically misleading."
    )
    sol = (
        "**Why Unequal Widths are Misleading:**\n"
        "The human eye perceives the total **area** of a bar, not just its height. "
        "If a bar is drawn twice as wide, its area is doubled even if its height is unchanged. "
        "This visually exaggerates the importance or frequency of that category, deceiving the reader."
    )
    return {
        "id": f"g7_dm_42_{rng.randint(100000, 999999)}",
        "subskill": "42_misleading_graph_unequal_scaling_or_width",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Unequal bar widths make the area disproportionate, misleading the viewer's perception",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_42",
        "hints": {
            "tier_1": "Do wider bars look bigger than thinner bars of the same height?",
            "tier_2": "Yes, because area = width × height.",
            "tier_3": "Unequal widths distort the visual area."
        },
        "misconception_tags": ["varying_bar_widths_in_graphs"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Explains human eye perceives area", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains wider bar exaggerates category importance", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 43. Misleading graph 3D perspective distortion
def arch_43_misleading_graph_3d_perspective_distortion(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([25, 30, 35])
    ans = "3D tilted perspective makes front sectors look bigger than rear sectors"
    prompt = (
        f"Many computer programs allow users to tilt circular sector displays (where two categories each represent {pct}%) into a 3D perspective view.\n\n"
        f"Explain how a 3D perspective view distorts the visual comparison of the two {pct}% categories."
    )
    sol = (
        "**3D Distortion:**\n"
        f"When tilted in 3D, the {pct}% sector in the foreground (front) appears much larger than "
        f"the {pct}% sector in the background (rear) due to visual perspective and the added 3D edge. "
        "This creates a misleading impression of the relative proportions."
    )
    return {
        "id": f"g7_dm_43_{rng.randint(100000, 999999)}",
        "subskill": "43_misleading_graph_3d_perspective_distortion",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Foreground sectors appear larger than background sectors due to tilt and 3D thickness",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_43",
        "hints": {
            "tier_1": "Does an object look bigger when tilted towards you?",
            "tier_2": "Front sectors look larger than rear sectors.",
            "tier_3": "3D tilt exaggerates front sectors and shrinks rear sectors."
        },
        "misconception_tags": ["preferring_3d_distorted_graphs"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Explains foreground sectors appear larger than background", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States 3D thickness distorts true mathematical proportions", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 44. Choosing appropriate measure mean vs median
def arch_44_choosing_appropriate_measure_mean_vs_median(rng: random.Random) -> Dict[str, Any]:
    ans = "Median: when data has extreme outliers or is skewed; Mean: when data is evenly distributed without outliers"
    prompt = (
        "A statistician must choose between reporting the **mean** or the **median**.\n\n"
        "1. In what scenario is the **mean** the best measure of central tendency?\n"
        "2. In what scenario is the **median** the best measure of central tendency?"
    )
    sol = (
        "**1. When to Use Mean:**\n"
        "When the dataset is relatively symmetrical and contains **no extreme outliers**, "
        "because the mean uses every numerical value.\n\n"
        "**2. When to Use Median:**\n"
        "When the dataset contains **extreme outliers** or is heavily skewed (such as household income or property prices), "
        "because the median is unaffected by extreme values."
    )
    return {
        "id": f"g7_dm_44_{rng.randint(100000, 999999)}",
        "subskill": "44_choosing_appropriate_measure_mean_vs_median",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Mean for symmetrical data with no outliers; Median when outliers or skewness are present",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_44",
        "hints": {
            "tier_1": "Think about income in South Africa. Does a billionaire change the median or the mean?",
            "tier_2": "The billionaire pulls the mean up, so median is better for skewed data.",
            "tier_3": "Mean for uniform data without outliers; median for skewed data with outliers."
        },
        "misconception_tags": ["always_using_mean_by_default"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Specifies mean for symmetric data without outliers", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Specifies median for data with outliers / skewed", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 45. Choosing appropriate measure mode for shoe inventory
def arch_45_choosing_appropriate_measure_mode_for_shoe_sizes(rng: random.Random) -> Dict[str, Any]:
    ans = "Mode; knowing the most popular shoe size tells the store which size to stock most"
    prompt = (
        "A shoe store manager wants to decide which size of school shoes to order the most of.\n\n"
        "1. Which measure of central tendency should the manager use: mean, median, or mode?\n"
        "2. Explain why the other two measures would be unhelpful or nonsensical in this business context."
    )
    sol = (
        "**1. Best Measure:**\n"
        "The **mode**.\n\n"
        "**2. Explanation:**\n"
        "- The mode indicates the most frequently purchased shoe size, which is exactly the size the manager needs to stock most.\n"
        "- The **mean** might calculate an un-manufactured size (e.g. Size 6,42), which cannot be stocked.\n"
        "- The **median** only shows the middle size, which might not be frequently requested."
    )
    return {
        "id": f"g7_dm_45_{rng.randint(100000, 999999)}",
        "subskill": "45_choosing_appropriate_measure_mode_for_shoe_sizes",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Mode; it identifies the most frequently bought size, whereas a decimal mean shoe size is meaningless",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_45",
        "hints": {
            "tier_1": "Can a shoe shop sell size 6,42?",
            "tier_2": "No, shoes come in whole or half sizes. You want to stock the most popular size.",
            "tier_3": "Mode is best for inventory."
        },
        "misconception_tags": ["using_mean_for_discrete_sizes"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Selects mode", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains mode identifies most popular stock size, unlike decimal mean", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 46. Drawing valid statistical conclusions
def arch_46_drawing_valid_statistical_conclusions(rng: random.Random) -> Dict[str, Any]:
    ans = "Correlation does not imply causation; having more ice cream does not cause more drowning"
    prompt = (
        "A study observes that on days when ice cream sales increase, the number of people who drown at beaches also increases.\n"
        "A journalist concludes: *'Eating ice cream causes drowning.'*\n\n"
        "1. Is the journalist's conclusion mathematically valid?\n"
        "2. What underlying lurking variable (common cause) explains this correlation?"
    )
    sol = (
        "**1. Validity:**\n"
        "No, the conclusion is invalid. **Correlation does not imply causation**.\n\n"
        "**2. Common Cause:**\n"
        "Hot summer weather is the underlying common factor:\n"
        "- Hot weather causes more people to buy ice cream.\n"
        "- Hot weather causes more people to swim in the sea, increasing the likelihood of drowning accidents."
    )
    return {
        "id": f"g7_dm_46_{rng.randint(100000, 999999)}",
        "subskill": "46_drawing_valid_statistical_conclusions",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Invalid; correlation does not mean causation; hot weather is the common factor",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_46",
        "hints": {
            "tier_1": "Does eating ice cream make you drown?",
            "tier_2": "What kind of weather makes people swim and eat ice cream?",
            "tier_3": "Invalid conclusion; hot weather causes both."
        },
        "misconception_tags": ["confusing_correlation_with_causation"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States conclusion is invalid (correlation != causation)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identifies hot weather as common underlying variable", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 47. Data summary report writing three points
def arch_47_data_summary_report_writing_three_points(rng: random.Random) -> Dict[str, Any]:
    ans = "Central tendency (mean/median), spread (range), and notable trends or outliers"
    prompt = (
        "When writing a concise 3 to 5-line summary report to interpret and report on a dataset, "
        "what **three key statistical elements** should always be included?"
    )
    sol = (
        "**Three Key Elements in a Statistical Summary Report:**\n"
        "1. **Measure of Central Tendency:** State the typical value using the mean or median.\n"
        "2. **Measure of Spread:** State the range (maximum and minimum values) to describe the variability of the data.\n"
        "3. **Overall Trend or Notable Findings:** Identify any dominant mode, general trend (e.g. increase over time), or unusual outliers."
    )
    return {
        "id": f"g7_dm_47_{rng.randint(100000, 999999)}",
        "subskill": "47_data_summary_report_writing_three_points",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Central tendency (mean/median), spread (range), and notable trends or outliers",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_47",
        "hints": {
            "tier_1": "What is the average? What are the extremes? What is the pattern?",
            "tier_2": "Center, spread, and trends.",
            "tier_3": "Central tendency, range/spread, and trends/outliers."
        },
        "misconception_tags": ["omitting_spread_in_summary_report"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Specifies central tendency (mean/median)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Specifies spread (range/extremes)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Specifies trends, mode, or outliers", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 48. Common error forgetting to order for median
def arch_48_common_error_forgetting_to_order_for_median(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: Picked middle number of unordered list (2); correct median is 5"
    prompt = (
        "A learner is asked to find the median of the dataset:\n\n"
        "$$9;\\; 1;\\; 2;\\; 8;\\; 5$$\n\n"
        "The learner says: *'The middle number is 2, so the median is 2.'*\n\n"
        "1. What critical mistake did the learner make?\n"
        "2. What is the correct median?"
    )
    sol = (
        "**1. Mistake:**\n"
        "The learner selected the number in the physical middle of the list **without sorting** the data first.\n\n"
        "**2. Correct Calculation:**\n"
        "Arrange the data in ascending order:\n"
        "$$1;\\; 2;\\; \\mathbf{5};\\; 8;\\; 9$$\n"
        "The true middle value (position 3 out of 5) is **5**.\n\n"
        "$$\\therefore \\text{Correct Median} = 5$$"
    )
    return {
        "id": f"g7_dm_48_{rng.randint(100000, 999999)}",
        "subskill": "48_common_error_forgetting_to_order_for_median",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Did not order the numbers first; correct median is 5",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_48",
        "hints": {
            "tier_1": "You must sort numbers before finding the middle.",
            "tier_2": "Sorted list: 1, 2, 5, 8, 9.",
            "tier_3": "Correct median is 5."
        },
        "misconception_tags": ["finding_median_without_sorting"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies failure to arrange in ascending order", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates correct median = 5", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 49. Common error confusing mode with frequency count
def arch_49_common_error_confusing_mode_with_frequency_count(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: Stated the frequency count (4) instead of the actual data value (15); Mode is 15"
    prompt = (
        "In a survey of ages, the age $15$ appeared $4$ times, which was more than any other age.\n"
        "A learner writes: *'The mode is 4.'*\n\n"
        "1. Identify the conceptual error made by the learner.\n"
        "2. State the correct mode."
    )
    sol = (
        "**1. Error Identification:**\n"
        "The learner confused the **frequency count** (how many times the value repeats) with the **mode itself** (the data value). "
        "The number $4$ is the frequency, not the data item.\n\n"
        "**2. Correct Mode:**\n"
        "$$\\text{Mode} = 15\\text{ years old}$$"
    )
    return {
        "id": f"g7_dm_49_{rng.randint(100000, 999999)}",
        "subskill": "49_common_error_confusing_mode_with_frequency_count",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Confused frequency (4) with mode (15); Mode is 15",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_49",
        "hints": {
            "tier_1": "Is the mode the number of times it happens or the actual value that repeats?",
            "tier_2": "Mode is the data value: age 15.",
            "tier_3": "Learner reported the frequency 4; the mode is 15."
        },
        "misconception_tags": ["confusing_mode_with_frequency_count"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Explains learner reported frequency instead of data value", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States correct mode = 15", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 50. Data measures comprehensive diagnostic autopsy
def arch_50_data_measures_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    ans = "Mean uses all values; Median resists outliers; Mode is most frequent; Range is spread"
    prompt = (
        "A diagnostic statistics evaluation asks you to assess three common learner claims:\n\n"
        "1. **Claim A:** 'If two datasets have the same mean of 50, their values must be distributed identically.'\n"
        "2. **Claim B:** 'Adding 10 to every score in a dataset will increase both the mean and the range by 10.'\n"
        "3. **Claim C:** 'In any dataset, the mean, median, and mode are always equal.'\n\n"
        "Evaluate each claim as True or False, and provide a short mathematical justification."
    )
    sol = (
        "**Diagnostic Autopsy:**\n\n"
        "**1. Claim A: False.**\n"
        "Two datasets can have the exact same mean but completely different spreads (ranges). "
        "For example, $\\{50, 50, 50\\}$ has mean $50$ and range $0$, whereas $\\{0, 50, 100\\}$ has mean $50$ and range $100$.\n\n"
        "**2. Claim B: False.**\n"
        "The mean increases by $10$, but the **range remains unchanged** because both the maximum and minimum values increase by $10$: "
        "$(x_{\\text{max}} + 10) - (x_{\\text{min}} + 10) = x_{\\text{max}} - x_{\\text{min}}$.\n\n"
        "**3. Claim C: False.**\n"
        "The mean, median, and mode are only equal in perfectly symmetrical distributions. In skewed datasets or datasets with outliers, "
        "they are generally different."
    )
    return {
        "id": f"g7_dm_50_{rng.randint(100000, 999999)}",
        "subskill": "50_data_measures_comprehensive_diagnostic_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Claim A: False (spreads can differ); Claim B: False (range does not change); Claim C: False (only equal in symmetrical data)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_50",
        "hints": {
            "tier_1": "Does adding a constant to every number change the distance between the highest and lowest?",
            "tier_2": "Claim A is False, Claim B is False, Claim C is False.",
            "tier_3": "All three claims are False."
        },
        "misconception_tags": ["assuming_range_shifts_with_constant_addition", "confusing_equal_mean_with_equal_distribution"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Refutes Claim A (same mean does not imply same spread)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Refutes Claim B (range remains invariant under shift)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Refutes Claim C (measures differ in skewed data)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }
