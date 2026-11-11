"""Grade 9 Mathematics - Representing Data Archetypes 26-50 (CAPS Term 4).
Focus: Double Bar Graphs, Histograms, Scatter Plots, Correlation, Lines of Best Fit, and Representation Synthesis.
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
# 26. Scatter plot: Identify independent vs dependent variable
# -----------------------------------------------------------------------------
def arch_26_scatter_plot_independent_vs_dependent_variable(r: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Hours of study before an exam", "Exam mark achieved", "Hours of study", "Exam mark achieved"),
        ("Distance driven by a car", "Amount of fuel consumed", "Distance driven", "Amount of fuel consumed"),
        ("Age of a child", "Height of the child", "Age", "Height"),
        ("Temperature of an oven", "Time taken to bake bread", "Temperature", "Baking time"),
    ]
    var_x, var_y, indep, dep = r.choice(pairs)
    ask_for = r.choice(["independent", "dependent"])
    target_ans = indep if ask_for == "independent" else dep

    prompt = (
        f"A scatter plot investigates the relationship between: **{var_x}** and **{var_y}**.\n"
        f"Identify the **{ask_for} variable** (the variable plotted on the {'horizontal x-axis' if ask_for == 'independent' else 'vertical y-axis'})."
    )
    ans_str = target_ans
    sol = (
        f"• The **independent variable** (plotted on the horizontal x-axis) is **{indep}** because it is the presumed cause or controlled input.\n"
        f"• The **dependent variable** (plotted on the vertical y-axis) is **{dep}** because it responds to changes in the independent variable.\n"
        f"Therefore, the {ask_for} variable is **{target_ans}**."
    )
    return {
        "subskill": "26_scatter_plot_independent_vs_dependent_variable",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify {ask_for} variable: {target_ans}", "marks": 1},
        ],
        "hints": [
            "The independent variable is on the horizontal x-axis.",
            "The dependent variable is on the vertical y-axis.",
            f"The {ask_for} variable is {target_ans}.",
        ],
        "misconception_tags": ["independent_dependent_axis_confusion"],
    }


# -----------------------------------------------------------------------------
# 27. Scatter plot: Positive correlation identification
# -----------------------------------------------------------------------------
def arch_27_scatter_plot_positive_correlation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A scatter plot shows that as the number of hours a learner studies increases, "
        f"their test marks also consistently increase.\n"
        f"What type of correlation does this scatter plot show: **'Positive correlation'**, **'Negative correlation'**, or **'No correlation'**?"
    )
    ans_str = "Positive correlation"
    sol = (
        f"Since both variables increase together (as $x$ increases, $y$ increases), "
        f"the points slope upward from left to right, indicating a **Positive correlation**."
    )
    return {
        "subskill": "27_scatter_plot_positive_correlation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": "Positive correlation",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify positive correlation", "marks": 1},
        ],
        "hints": [
            "When both variables increase together, the correlation is positive.",
        ],
        "misconception_tags": ["correlation_type_confusion"],
    }


# -----------------------------------------------------------------------------
# 28. Scatter plot: Negative correlation identification
# -----------------------------------------------------------------------------
def arch_28_scatter_plot_negative_correlation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A scatter plot shows that as the outdoor temperature increases, "
        f"the sales of electric heaters decrease significantly.\n"
        f"What type of correlation does this scatter plot show: **'Positive correlation'**, **'Negative correlation'**, or **'No correlation'**?"
    )
    ans_str = "Negative correlation"
    sol = (
        f"As one variable increases, the other variable decreases (points slope downward from left to right). "
        f"This indicates a **Negative correlation**."
    )
    return {
        "subskill": "28_scatter_plot_negative_correlation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": "Negative correlation",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify negative correlation", "marks": 1},
        ],
        "hints": [
            "When one variable goes up while the other goes down, the correlation is negative.",
        ],
        "misconception_tags": ["negative_correlation_misidentification"],
    }


# -----------------------------------------------------------------------------
# 29. Scatter plot: No correlation identification
# -----------------------------------------------------------------------------
def arch_29_scatter_plot_no_correlation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A scatter plot compares learners' shoe sizes with their mathematics exam marks. "
        f"The plotted points are scattered randomly across the grid with no clear upward or downward pattern.\n"
        f"What type of correlation is demonstrated?"
    )
    ans_str = "No correlation"
    sol = (
        f"Because there is no discernible trend or linear relationship between shoe size and math marks, "
        f"the data exhibits **No correlation**."
    )
    return {
        "subskill": "29_scatter_plot_no_correlation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": "No correlation",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify zero/no correlation", "marks": 1},
        ],
        "hints": [
            "Randomly scattered points without a pattern indicate no correlation.",
        ],
        "misconception_tags": ["assumed_correlation_in_random_data"],
    }


# -----------------------------------------------------------------------------
# 30. Scatter plot: Line of best fit purpose
# -----------------------------------------------------------------------------
def arch_30_scatter_plot_line_of_best_fit_purpose(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When analyzing a scatter plot with a strong linear correlation, a researcher draws a straight line "
        f"that passes as close to as many points as possible (with approximately equal points above and below the line).\n"
        f"What is this line called?"
    )
    ans_str = "Line of best fit"
    sol = (
        f"This line is called the **Line of best fit** (or trend line). "
        f"It is used to model the linear trend and make predictions."
    )
    return {
        "subskill": "30_scatter_plot_line_of_best_fit_purpose",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": "Line of best fit (trend line)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State 'Line of best fit' or 'Trend line'", "marks": 1},
        ],
        "hints": [
            "It is the straight line drawn through the middle of the scatter plot points.",
            "It is called the line of best fit.",
        ],
        "misconception_tags": ["line_of_best_fit_terminology_error"],
    }


# -----------------------------------------------------------------------------
# 31. Scatter plot prediction using line of best fit
# -----------------------------------------------------------------------------
def arch_31_scatter_plot_prediction_using_line_of_best_fit(r: random.Random) -> Dict[str, Any]:
    hours = r.choice([2, 3, 4, 5, 6])
    # Model: mark = 30 + 10 * hours
    predicted_mark = 30 + 10 * hours
    prompt = (
        f"A line of best fit on a study-time scatter plot is modeled by the linear relationship:\n"
        f"$$\\text{{Exam Mark}} = 30 + 10 \\times (\\text{{Hours of Study}})$$\n"
        f"Use this line to predict the exam mark of a learner who studies for **{hours} hours**."
    )
    ans_str = str(predicted_mark)
    sol = (
        f"Substitute $\\text{{Hours}} = {hours}$ into the equation:\n"
        f"$$\\text{{Mark}} = 30 + (10 \\times {hours}) = 30 + {10 * hours} = {predicted_mark}\\%$$"
    )
    return {
        "subskill": "31_scatter_plot_prediction_using_line_of_best_fit",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str}%",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitution: 30 + 10 × {hours}", "marks": 1},
            {"step": f"Answer: {predicted_mark}%", "marks": 1},
        ],
        "hints": [
            f"Multiply {hours} by 10 and add 30: $30 + {10 * hours} = {predicted_mark}$.",
        ],
        "misconception_tags": ["linear_model_substitution_error"],
    }


# -----------------------------------------------------------------------------
# 32. Interpolation vs Extrapolation
# -----------------------------------------------------------------------------
def arch_32_interpolation_vs_extrapolation(r: random.Random) -> Dict[str, Any]:
    choice = r.choice(["inside", "outside"])
    if choice == "inside":
        term = "Interpolation"
        desc = "estimating a value *within* the range of the existing collected data points"
    else:
        term = "Extrapolation"
        desc = "estimating a value *outside* the range of the existing collected data points"

    prompt = (
        f"In data analysis, what is the term for: **{desc}**? "
        f"Choose between **'Interpolation'** and **'Extrapolation'**."
    )
    ans_str = term
    sol = (
        f"• **Interpolation**: Making predictions within the existing data range (more reliable).\n"
        f"• **Extrapolation**: Making predictions beyond the existing data range (less reliable).\n"
        f"Therefore, the correct term is **{term}**."
    )
    return {
        "subskill": "32_interpolation_vs_extrapolation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": term,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify {term}", "marks": 1},
        ],
        "hints": [
            "'Inter' means inside/within; 'Extra' means beyond/outside.",
            f"The answer is {term}.",
        ],
        "misconception_tags": ["interpolation_extrapolation_confusion"],
    }


# -----------------------------------------------------------------------------
# 33. Frequency polygon concept
# -----------------------------------------------------------------------------
def arch_33_frequency_polygon_concept(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"To construct a **frequency polygon** from a histogram, at what point above each class interval "
        f"is the frequency plotted?\n"
        f"Choose from: ['Left boundary', 'Midpoint (class midpoint)', 'Right boundary']."
    )
    ans_str = "Midpoint (class midpoint)"
    sol = (
        f"In a frequency polygon, points are plotted at the **midpoint of each class interval** "
        f"at a height corresponding to the frequency, and joined with straight lines."
    )
    return {
        "subskill": "33_frequency_polygon_concept",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Midpoint (class midpoint)",
        "sample_answer": "Midpoint",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State class midpoint", "marks": 1},
        ],
        "hints": [
            "The points in a frequency polygon are centered on each interval (at the midpoint).",
        ],
        "misconception_tags": ["frequency_polygon_plotted_on_boundary"],
    }


# -----------------------------------------------------------------------------
# 34. Calculate midpoint of a class interval
# -----------------------------------------------------------------------------
def arch_34_calculate_midpoint_of_class_interval(r: random.Random) -> Dict[str, Any]:
    lower = r.choice([10, 20, 30, 40, 50, 60])
    width_val = r.choice([10, 20])
    upper = lower + width_val
    midpoint = (lower + upper) / 2.0

    prompt = (
        f"Calculate the **midpoint** of the class interval: **${lower} \\le x < {upper}$**."
    )
    ans_str = f"{midpoint:.1f}".rstrip("0").rstrip(".")
    sol = (
        f"$$\\text{{Midpoint}} = \\frac{{\\text{{Lower boundary}} + \\text{{Upper boundary}}}}{{2}} = \\frac{{{lower} + {upper}}}{{2}} = \\frac{{{lower + upper}}}{{2}} = {ans_str}$$"
    )
    return {
        "subskill": "34_calculate_midpoint_of_class_interval",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Formula: ({lower} + {upper}) / 2", "marks": 1},
            {"step": f"Answer: {ans_str}", "marks": 1},
        ],
        "hints": [
            "Add the lower and upper limits and divide by 2.",
            f"$({lower} + {upper}) \\div 2 = {ans_str}$.",
        ],
        "misconception_tags": ["midpoint_formula_error"],
    }


# -----------------------------------------------------------------------------
# 35. Cumulative frequency calculation
# -----------------------------------------------------------------------------
def arch_35_cumulative_frequency_calculation(r: random.Random) -> Dict[str, Any]:
    f1, f2, f3, f4 = 5, 8, 12, 10
    cum_f = [5, 13, 25, 35]

    prompt = (
        f"A frequency table has successive frequencies: $5$, $8$, $12$, and $10$.\n"
        f"Calculate the **cumulative frequency** at the third interval."
    )
    ans_str = str(cum_f[2])
    sol = (
        f"Cumulative frequency is the running total of frequencies:\n"
        f"• Interval 1: $5$\n"
        f"• Interval 2: $5 + 8 = 13$\n"
        f"• Interval 3: $13 + 12 = **{cum_f[2]}**$"
    )
    return {
        "subskill": "35_cumulative_frequency_calculation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": str(cum_f[2]),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Sum first three frequencies: 5 + 8 + 12 = {cum_f[2]}", "marks": 1},
        ],
        "hints": [
            "Add all frequencies up to and including the third interval: $5 + 8 + 12$.",
            f"The cumulative frequency is {cum_f[2]}.",
        ],
        "misconception_tags": ["cumulative_frequency_summation_error"],
    }


# -----------------------------------------------------------------------------
# 36. Double bar graph: Combined total
# -----------------------------------------------------------------------------
def arch_36_double_bar_graph_combined_total(r: random.Random) -> Dict[str, Any]:
    b = r.randint(20, 45)
    g = r.randint(20, 45)
    total = b + g
    prompt = (
        f"In a double bar graph for Grade 9 science enrollment, the bar for boys is at **{b}** "
        f"and the bar for girls is at **{g}**.\n"
        f"Calculate the total number of learners enrolled."
    )
    ans_str = str(total)
    sol = (
        f"$$\\text{{Total}} = \\text{{Boys}} + \\text{{Girls}} = {b} + {g} = {total}\\text{{ learners}}$$"
    )
    return {
        "subskill": "36_double_bar_graph_combined_total",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": str(total),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Add {b} + {g} = {total}", "marks": 1},
        ],
        "hints": [
            f"Add the counts together: ${b} + {g} = {total}$.",
        ],
        "misconception_tags": ["double_bar_addition_error"],
    }


# -----------------------------------------------------------------------------
# 37. Reading pie chart with unknown slice (degrees sum to 360)
# -----------------------------------------------------------------------------
def arch_37_pie_chart_unknown_slice_degrees(r: random.Random) -> Dict[str, Any]:
    a1 = r.choice([60, 90, 100])
    a2 = r.choice([70, 80, 90])
    a3 = r.choice([50, 60, 70])
    a4 = 360 - (a1 + a2 + a3)

    prompt = (
        f"A pie chart is divided into 4 sectors with angles: "
        f"${a1}^\\circ$, ${a2}^\\circ$, ${a3}^\\circ$, and $x^\\circ$.\n"
        f"Calculate the value of $x$ in degrees."
    )
    ans_str = str(a4)
    sol = (
        f"The angles around a complete circle sum to $360^\\circ$:\n"
        f"$$x = 360^\\circ - ({a1}^\\circ + {a2}^\\circ + {a3}^\\circ) = 360^\\circ - {a1+a2+a3}^\\circ = {a4}^\\circ$$"
    )
    return {
        "subskill": "37_pie_chart_unknown_slice_degrees",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str}°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Sum known angles: {a1+a2+a3}°", "marks": 1},
            {"step": f"Subtract from 360: {a4}°", "marks": 1},
        ],
        "hints": [
            "The sum of all angles in a pie chart is $360^\\circ$.",
            f"Subtract the known angles from $360^\\circ$: $360 - {a1+a2+a3} = {a4}^\\circ$.",
        ],
        "misconception_tags": ["circle_angles_sum_to_180_confusion"],
    }


# -----------------------------------------------------------------------------
# 38. Reading pie chart with unknown percentage (percentages sum to 100)
# -----------------------------------------------------------------------------
def arch_38_pie_chart_unknown_slice_percentage(r: random.Random) -> Dict[str, Any]:
    p1 = 30
    p2 = 25
    p3 = 20
    p4 = 100 - (p1 + p2 + p3)  # 25

    prompt = (
        f"A municipal budget pie chart allocates $30\\%$ to sanitation, $25\\%$ to water, "
        f"$20\\%$ to electricity, and the remainder ($x\\%$) to road maintenance.\n"
        f"Calculate the percentage allocated to road maintenance ($x$)."
    )
    ans_str = str(p4)
    sol = (
        f"All percentage sectors in a pie chart must sum to $100\\%$:\n"
        f"$$x = 100\\% - (30\\% + 25\\% + 20\\%) = 100\\% - 75\\% = {p4}\\%$$"
    )
    return {
        "subskill": "38_pie_chart_unknown_slice_percentage",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str}%",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Subtract from 100%: 100 - 75 = {p4}%", "marks": 1},
        ],
        "hints": [
            "All percentages in a complete pie chart must sum to $100\\%$.",
            f"$100 - 75 = {p4}\\%$.",
        ],
        "misconception_tags": ["percentage_sum_not_100"],
    }


# -----------------------------------------------------------------------------
# 39. Interpreting slope of broken line graph
# -----------------------------------------------------------------------------
def arch_39_interpreting_slope_of_broken_line_graph(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"On a line graph tracking company profits over 12 months, the line between Month 4 and Month 5 "
        f"is completely horizontal (flat).\n"
        f"What does a horizontal segment indicate about the profit during that period?"
    )
    explanation = "There was no change in profit (profit remained constant/unchanged)."
    return {
        "subskill": "39_interpreting_slope_of_broken_line_graph",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Profit remained constant / unchanged (no change)",
        "sample_answer": explanation,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State profit remained constant / zero change", "marks": 1},
        ],
        "hints": [
            "A horizontal line has a slope of 0.",
            "This means the value did not increase or decrease.",
        ],
        "misconception_tags": ["assumed_horizontal_means_zero_profit"],
    }


# -----------------------------------------------------------------------------
# 40. Steepest increase on broken-line graph
# -----------------------------------------------------------------------------
def arch_40_steepest_increase_on_broken_line_graph(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A line graph shows water levels rising over 4 intervals:\n"
        f"• Day 1 to 2: rises $10\\text{{ cm}}$\n"
        f"• Day 2 to 3: rises $35\\text{{ cm}}$\n"
        f"• Day 3 to 4: rises $15\\text{{ cm}}$\n\n"
        f"During which interval did the water level rise at the **fastest rate** (steepest slope)?"
    )
    ans_str = "Day 2 to 3"
    sol = (
        f"The steepest slope corresponds to the greatest change over the same 1-day time span: "
        f"**Day 2 to 3** had the greatest rise of $35\\text{{ cm}}$."
    )
    return {
        "subskill": "40_steepest_increase_on_broken_line_graph",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} (35 cm rise)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify Day 2 to 3 as steepest slope", "marks": 1},
        ],
        "hints": [
            "The fastest rate of change corresponds to the largest increase in the same time period.",
            "Day 2 to 3 had a rise of 35 cm.",
        ],
        "misconception_tags": ["confused_height_with_rate_of_change"],
    }


# -----------------------------------------------------------------------------
# 41. Identifying outliers on a scatter plot
# -----------------------------------------------------------------------------
def arch_41_identifying_outliers_on_scatter_plot(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"On a scatter plot showing study hours versus test marks, most points cluster tightly "
        f"along an upward line between marks of 50% and 90%. However, one learner who studied for "
        f"12 hours received a mark of 15%.\n"
        f"What is this unusual, isolated data point called?"
    )
    ans_str = "Outlier"
    sol = (
        f"A data point that lies significantly far away from the overall pattern or cluster of the data "
        f"is called an **Outlier**."
    )
    return {
        "subskill": "41_identifying_outliers_on_scatter_plot",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": "Outlier",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State 'Outlier'", "marks": 1},
        ],
        "hints": [
            "An isolated point far from the cluster is called an outlier.",
        ],
        "misconception_tags": ["outlier_terminology_error"],
    }


# -----------------------------------------------------------------------------
# 42. Effect of outliers on mean vs median
# -----------------------------------------------------------------------------
def arch_42_effect_of_outliers_on_mean_vs_median(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A single extreme high score (outlier) is added to a dataset of test marks.\n"
        f"Which measure will increase significantly: the **'Mean'** or the **'Median'**?"
    )
    ans_str = "Mean"
    sol = (
        f"The **Mean** uses the sum of all numerical values, so an extreme outlier significantly pulls "
        f"the mean upward. The **Median** is based only on positional rank and remains largely resistant."
    )
    return {
        "subskill": "42_effect_of_outliers_on_mean_vs_median",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": "Mean",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify Mean as sensitive to outliers", "marks": 1},
        ],
        "hints": [
            "The mean is calculated from the numerical sum of all items.",
            "An extreme value changes the sum drastically, increasing the mean.",
        ],
        "misconception_tags": ["median_affected_by_outliers"],
    }


# -----------------------------------------------------------------------------
# 43. Pictogram misleading representation
# -----------------------------------------------------------------------------
def arch_43_pictogram_misleading_representation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a pictogram, a car company wants to show that its sales doubled compared to last year. "
        f"Instead of drawing two identical cars, it doubles both the height AND the width of a single car graphic.\n"
        f"By what factor does the area of the graphic actually increase?"
    )
    ans_str = "4"
    sol = (
        f"When both the width and height of an image are doubled ($2 \\times 2$), "
        f"the surface area of the graphic increases by a factor of $2^2 = **4**$.\n"
        f"This misleads readers into perceiving the sales as 4 times greater rather than double."
    )
    return {
        "subskill": "43_pictogram_misleading_representation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": "4 (2² = 4)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Area scale factor = 2 × 2 = 4", "marks": 1},
        ],
        "hints": [
            "Doubling both linear dimensions multiplies area by $2^2 = 4$.",
        ],
        "misconception_tags": ["pictogram_area_scaling_misconception"],
    }


# -----------------------------------------------------------------------------
# 44. Histogram: Total count from multiple intervals
# -----------------------------------------------------------------------------
def arch_44_histogram_total_count_from_intervals(r: random.Random) -> Dict[str, Any]:
    counts = [8, 14, 22, 16, 10]
    total = sum(counts)
    prompt = (
        f"A histogram with 5 class intervals has bin heights: $8$, $14$, $22$, $16$, and $10$.\n"
        f"Calculate the total number of data values represented."
    )
    ans_str = str(total)
    sol = (
        f"$$\\text{{Total}} = 8 + 14 + 22 + 16 + 10 = {total}$$"
    )
    return {
        "subskill": "44_histogram_total_count_from_intervals",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": str(total),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Sum bin counts: {total}", "marks": 1},
        ],
        "hints": [
            f"Add all 5 frequencies: $8 + 14 + 22 + 16 + 10 = {total}$.",
        ],
        "misconception_tags": ["histogram_total_omission"],
    }


# -----------------------------------------------------------------------------
# 45. Converting table to pie chart sector fraction
# -----------------------------------------------------------------------------
def arch_45_converting_table_to_pie_chart_fraction(r: random.Random) -> Dict[str, Any]:
    freq = r.choice([15, 20, 25, 30])
    total = 60
    # simplified fraction
    gcd = math.gcd(freq, total)
    num = freq // gcd
    den = total // gcd

    prompt = (
        f"Out of a survey of ${total}$ learners, ${freq}$ chose blue as their favourite colour.\n"
        f"Express the sector fraction representing blue in **simplest fractional form** (e.g. 1/4)."
    )
    ans_str = f"{num}/{den}"
    sol = (
        f"$$\\text{{Fraction}} = \\frac{{{freq}}}{{{total}}} = \\frac{{{num}}}{{{den}}}$$"
    )
    return {
        "subskill": "45_converting_table_to_pie_chart_fraction",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Simplify {freq}/{total} to {num}/{den}", "marks": 1},
        ],
        "hints": [
            f"Write $\\frac{{{freq}}}{{{total}}}$ and divide both numerator and denominator by {gcd}.",
        ],
        "misconception_tags": ["fraction_simplification_error"],
    }


# -----------------------------------------------------------------------------
# 46. Estimating mean from grouped frequency histogram
# -----------------------------------------------------------------------------
def arch_46_estimating_mean_from_grouped_frequency_histogram(r: random.Random) -> Dict[str, Any]:
    # 2 intervals: 10-20 (midpoint 15, count 4), 20-30 (midpoint 25, count 6)
    # Estimated mean = (4*15 + 6*25) / (4+6) = (60 + 150) / 10 = 21.0
    c1, c2 = 4, 6
    m1, m2 = 15, 25
    sum_fx = c1 * m1 + c2 * m2  # 210
    total_n = c1 + c2  # 10
    est_mean = sum_fx / total_n

    prompt = (
        f"A grouped distribution has two intervals:\n"
        f"• $10 \\le x < 20$: midpoint $15$, frequency $4$\n"
        f"• $20 \\le x < 30$: midpoint $25$, frequency $6$\n\n"
        f"Calculate the **estimated mean** ($\\bar{{x}}$)."
    )
    ans_str = f"{est_mean:.1f}".rstrip("0").rstrip(".")
    sol = (
        f"$$\\bar{{x}} = \\frac{{\\sum (f \\times m)}}{{\\sum f}} = \\frac{{(4 \\times 15) + (6 \\times 25)}}{{4 + 6}} = \\frac{{60 + 150}}{{10}} = \\frac{{210}}{{10}} = {ans_str}$$"
    )
    return {
        "subskill": "46_estimating_mean_from_grouped_frequency_histogram",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate sum(f × m): 60 + 150 = 210", "marks": 1},
            {"step": f"Divide by total frequency: 210 / 10 = {ans_str}", "marks": 1},
        ],
        "hints": [
            "Multiply each midpoint by its frequency, sum them, and divide by total frequency.",
            f"$(4 \\times 15 + 6 \\times 25) \\div 10 = 21$.",
        ],
        "misconception_tags": ["estimated_mean_midpoint_calculation_error"],
    }


# -----------------------------------------------------------------------------
# 47. Reading interval with highest frequency from histogram
# -----------------------------------------------------------------------------
def arch_47_reading_interval_with_highest_frequency(r: random.Random) -> Dict[str, Any]:
    intervals = ["0–9", "10–19", "20–29", "30–39"]
    counts = [5, 18, 12, 7]
    prompt = (
        "A histogram has frequencies: $0\\text{--}9$ ($5$), $10\\text{--}19$ ($18$), $20\\text{--}29$ ($12$), $30\\text{--}39$ ($7$).\n"
        "Which class interval has the highest frequency?"
    )
    ans_str = "10–19"
    sol = "The interval **10–19** has the highest frequency of 18."
    return {
        "subskill": "47_reading_interval_with_highest_frequency",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} (frequency 18)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify 10–19", "marks": 1},
        ],
        "hints": [
            "Find the largest number among the frequencies: 18.",
            "The corresponding interval is 10–19.",
        ],
        "misconception_tags": ["highest_frequency_interval_error"],
    }


# -----------------------------------------------------------------------------
# 48. Identifying cluster of data on a scatter plot
# -----------------------------------------------------------------------------
def arch_48_identifying_cluster_of_data_on_scatter_plot(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"On a scatter plot showing ages and reaction times of 100 athletes, "
        f"75 of the points are densely grouped between ages 18–25 with reaction times under 0.25 seconds.\n"
        f"What is such a dense grouping of data points called?"
    )
    ans_str = "Cluster"
    sol = "A dense grouping of data points close together is called a **Cluster**."
    return {
        "subskill": "48_identifying_cluster_of_data_on_scatter_plot",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": "Cluster",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State 'Cluster'", "marks": 1},
        ],
        "hints": [
            "A tight grouping of points is called a cluster.",
        ],
        "misconception_tags": ["cluster_terminology_error"],
    }


# -----------------------------------------------------------------------------
# 49. Comparing two datasets using double bar graph totals
# -----------------------------------------------------------------------------
def arch_49_comparing_two_datasets_using_double_bar_graph_totals(r: random.Random) -> Dict[str, Any]:
    team_a = [10, 15, 20]
    team_b = [12, 14, 18]
    tot_a = sum(team_a)  # 45
    tot_b = sum(team_b)  # 44
    diff = abs(tot_a - tot_b)  # 1

    prompt = (
        f"A double bar graph compares points scored across 3 rounds:\n"
        f"• Team A: $10$, $15$, $20$\n"
        f"• Team B: $12$, $14$, $18$\n\n"
        f"Calculate the difference between the total points scored by Team A and Team B."
    )
    ans_str = str(diff)
    sol = (
        f"Team A total: $10 + 15 + 20 = {tot_a}$.\n"
        f"Team B total: $12 + 14 + 18 = {tot_b}$.\n"
        f"$$\\text{{Difference}} = |{tot_a} - {tot_b}| = {diff}\\text{{ point}}$$"
    )
    return {
        "subskill": "49_comparing_two_datasets_using_double_bar_graph_totals",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} point",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Team A sum: {tot_a}", "marks": 1},
            {"step": f"Team B sum: {tot_b}", "marks": 1},
            {"step": f"Difference: {diff}", "marks": 1},
        ],
        "hints": [
            f"Team A: $10 + 15 + 20 = {tot_a}$.",
            f"Team B: $12 + 14 + 18 = {tot_b}$.",
            f"Difference: ${tot_a} - {tot_b} = {diff}$.",
        ],
        "misconception_tags": ["series_total_difference_error"],
    }


# -----------------------------------------------------------------------------
# 50. Compound multi-stage data representation synthesis
# -----------------------------------------------------------------------------
def arch_50_compound_multi_stage_data_representation_synthesis(r: random.Random) -> Dict[str, Any]:
    # 3 categories: A=40, B=35, C=25 (total 100)
    # 1. angle for C: (25/100)*360 = 90 deg
    # 2. modal category: A
    cat_c_pct = 25
    angle_c = int((cat_c_pct / 100.0) * 360)  # 90
    modal_cat = "Science"

    prompt = (
        f"A survey of 100 learners on favourite subjects gave: Science (40), Maths (35), and English (25).\n"
        f"1. Identify the **modal subject**.\n"
        f"2. Calculate the **sector angle in degrees** for English (25 learners) on a pie chart."
    )
    ans_str = f"Science, {angle_c}°"
    sol = (
        f"1. **Modal Subject**: Science has the highest frequency ($40$).\n"
        f"2. **Sector Angle for English**:\n"
        f"$$\\text{{Angle}} = \\frac{{25}}{{100}} \\times 360^\\circ = {angle_c}^\\circ$$\n"
        f"Answer: **Science, {angle_c}°**."
    )
    return {
        "subskill": "50_compound_multi_stage_data_representation_synthesis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(angle_c),
        "sample_answer": f"Modal: {modal_cat}, English: {angle_c}°",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify mode: {modal_cat}", "marks": 1},
            {"step": f"Calculate angle: (25/100) × 360° = {angle_c}°", "marks": 1},
        ],
        "hints": [
            "Modal subject is the one with the highest count (Science).",
            f"Angle for English: $\\frac{{25}}{{100}} \\times 360^\\circ = {angle_c}^\\circ$.",
        ],
        "misconception_tags": ["multi_stage_representation_error"],
    }
