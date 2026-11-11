"""
Grade 8 Mathematics - Represent Data Archetypes (01 to 25).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/03. Represent data.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .svg_diagrams import draw_bar_chart_svg, draw_histogram_svg


def arch_01_bar_graph_reading_category_frequency(rng: random.Random) -> Dict[str, Any]:
    categories = ["Soccer", "Netball", "Rugby", "Cricket"]
    values = [float(rng.randint(15, 45)) for _ in categories]
    target_idx = rng.randint(0, 3)
    target_cat = categories[target_idx]
    target_val = int(values[target_idx])

    seed_val = rng.randint(1, 1000000)
    svg = draw_bar_chart_svg(
        categories=categories,
        values=values,
        title="Favorite Sports Survey",
        y_label="Number of Learners",
        seed=seed_val,
    )

    return {
        "title": "Reading Category Frequency from Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "01_bar_graph_reading_category_frequency",
        "difficulty": "easy",
        "question_text": (
            "Refer to the bar graph below showing the favorite sports of Grade 8 learners.\n\n"
            f"How many learners chose **{target_cat}** as their favorite sport?"
        ),
        "correct_answer": str(target_val),
        "marking_schema": [
            f"Read height of {target_cat} bar: {target_val} (1 mark)",
        ],
        "hints": [
            f"Find the bar labeled '{target_cat}' on the horizontal axis.",
            "Trace horizontally from the top of the bar to the vertical frequency axis.",
            f"Frequency = {target_val}.",
        ],
        "misconception_tags": ["bar_graph_axis_scale_reading_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_02_bar_graph_identifying_highest_or_lowest_category(rng: random.Random) -> Dict[str, Any]:
    categories = ["Drama", "Art", "Music", "Debating"]
    values = [float(rng.randint(12, 38)) for _ in categories]
    target_type = rng.choice(["highest", "lowest"])
    if target_type == "highest":
        target_val = max(values)
        target_cat = categories[values.index(target_val)]
    else:
        target_val = min(values)
        target_cat = categories[values.index(target_val)]

    seed_val = rng.randint(1, 1000000)
    svg = draw_bar_chart_svg(
        categories=categories,
        values=values,
        title="Extramural Clubs Enrolment",
        y_label="Learners",
        seed=seed_val,
    )

    return {
        "title": "Identifying Highest or Lowest Category",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "02_bar_graph_identifying_highest_or_lowest_category",
        "difficulty": "easy",
        "question_text": (
            "Refer to the bar graph below.\n\n"
            f"Which extramural club has the **{target_type}** enrolment?"
        ),
        "correct_answer": target_cat,
        "marking_schema": [
            f"Identify {target_type} bar: {target_cat} (height {int(target_val)}) (1 mark)",
        ],
        "hints": [
            f"Look for the {('tallest' if target_type == 'highest' else 'shortest')} vertical bar in the graph.",
            f"The {('tallest' if target_type == 'highest' else 'shortest')} bar is {target_cat}.",
            f"Club with {target_type} enrolment: {target_cat}.",
        ],
        "misconception_tags": ["bar_height_comparison_slip"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_03_bar_graph_calculating_difference_between_categories(rng: random.Random) -> Dict[str, Any]:
    categories = ["Bus", "Taxi", "Walking", "Car"]
    values = [float(rng.randint(18, 55)) for _ in categories]
    # Pick two distinct categories
    idx1, idx2 = 0, 1
    cat1, cat2 = categories[idx1], categories[idx2]
    val1, val2 = int(values[idx1]), int(values[idx2])
    diff = abs(val1 - val2)

    seed_val = rng.randint(1, 1000000)
    svg = draw_bar_chart_svg(
        categories=categories,
        values=values,
        title="Transport Modes to School",
        y_label="Learner Count",
        seed=seed_val,
    )

    return {
        "title": "Calculating Difference Between Categories on Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "03_bar_graph_calculating_difference_between_categories",
        "difficulty": "medium",
        "question_text": (
            "Refer to the bar graph below.\n\n"
            f"Calculate the difference between the number of learners who travel by **{cat1}** ({val1}) and by **{cat2}** ({val2})."
        ),
        "correct_answer": str(diff),
        "marking_schema": [
            f"Subtract frequencies: |{val1} - {val2}| = {diff} (1 mark)",
        ],
        "hints": [
            f"Read height of {cat1}: {val1}.",
            f"Read height of {cat2}: {val2}.",
            f"Difference = $|{val1} - {val2}| = {diff}$.",
        ],
        "misconception_tags": ["bar_frequency_subtraction_slip"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_04_bar_graph_calculating_total_sample_frequency(rng: random.Random) -> Dict[str, Any]:
    categories = ["Grade 8A", "Grade 8B", "Grade 8C", "Grade 8D"]
    values = [float(rng.randint(28, 36)) for _ in categories]
    total = int(sum(values))

    seed_val = rng.randint(1, 1000000)
    svg = draw_bar_chart_svg(
        categories=categories,
        values=values,
        title="Grade 8 Class Sizes",
        y_label="Learners",
        seed=seed_val,
    )

    return {
        "title": "Total Frequency from Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "04_bar_graph_calculating_total_sample_frequency",
        "difficulty": "medium",
        "question_text": (
            "Refer to the bar graph below showing class sizes across Grade 8.\n\n"
            "Calculate the total number of learners across all four Grade 8 classes combined."
        ),
        "correct_answer": str(total),
        "marking_schema": [
            f"Sum all bar heights: {int(values[0])} + {int(values[1])} + {int(values[2])} + {int(values[3])} = {total} (2 marks)",
        ],
        "hints": [
            "Read the frequency of each bar from the vertical axis.",
            f"Sum = {int(values[0])} + {int(values[1])} + {int(values[2])} + {int(values[3])}.",
            f"Total = {total}.",
        ],
        "misconception_tags": ["bar_chart_total_sum_omission"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_05_bar_graph_calculating_percentage_for_category(rng: random.Random) -> Dict[str, Any]:
    categories = ["Red", "Blue", "Green", "Yellow"]
    # Values that sum nicely to 50 or 40
    counts = [15, 20, 10, 5]
    total = sum(counts)
    target_idx = rng.randint(0, 3)
    target_cat = categories[target_idx]
    target_val = counts[target_idx]
    pct = int((target_val / total) * 100)

    seed_val = rng.randint(1, 1000000)
    svg = draw_bar_chart_svg(
        categories=categories,
        values=[float(c) for c in counts],
        title="T-Shirt Color Preferences (Total = 50)",
        y_label="Frequency",
        seed=seed_val,
    )

    return {
        "title": "Calculating Percentage from Bar Chart",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "05_bar_graph_calculating_percentage_for_category",
        "difficulty": "medium",
        "question_text": (
            f"Refer to the bar graph below showing preferences for a total of **{total} learners**.\n\n"
            f"What percentage of the surveyed learners chose **{target_cat}**?"
        ),
        "correct_answer": f"{pct}%",
        "marking_schema": [
            f"Divide category frequency by total: ({target_val}/{total}) * 100% = {pct}% (2 marks)",
        ],
        "hints": [
            f"Read the frequency of {target_cat}: {target_val}.",
            f"Divide by total sample size ({total}) and multiply by 100%: $\\frac{{{target_val}}}{{{total}}} \\times 100\\%$.",
            f"Percentage = {pct}%.",
        ],
        "misconception_tags": ["percentage_from_bar_scaling_slip"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_06_bar_graph_features_axes_labels_and_scales(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Essential Features of a Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "06_bar_graph_features_axes_labels_and_scales",
        "difficulty": "easy",
        "question_text": (
            "Name **three essential features** that must always be included when constructing an accurate bar graph."
        ),
        "correct_answer": "1. A descriptive title; 2. Clearly labeled horizontal and vertical axes; 3. A uniform, numbered scale on the vertical frequency axis.",
        "marking_schema": [
            "Title [1 mark], labeled axes with units/categories [1 mark], and uniform numbered scale [1 mark]",
        ],
        "hints": [
            "A reader must know what the graph is about (title).",
            "Each axis must indicate what is being measured or categorized (axis labels).",
            "The vertical axis must have evenly spaced numbers starting from zero (scale).",
        ],
        "misconception_tags": ["bar_graph_construction_criteria_omission"],
        "diagram_spec": None,
    }


def arch_07_bar_graph_why_bars_have_equal_spaces(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Why Spaces Exist Between Bars in Bar Graphs",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "07_bar_graph_why_bars_have_equal_spaces",
        "difficulty": "medium",
        "question_text": (
            "Explain why spaces (gaps) are placed between bars when displaying categorical data, unlike in a histogram."
        ),
        "correct_answer": "Spaces separate distinct, discrete categories that do not form a continuous numerical measurement scale.",
        "marking_schema": [
            "Explain that discrete separate categories require gaps, whereas continuous data touches: 1 mark",
        ],
        "hints": [
            "Bar graphs represent categorical or discrete data (like favorite colors or sports).",
            "Because colors or sports are separate distinct items, gaps are placed between bars to show they do not blend continuously.",
            "Spaces indicate separate discrete categories.",
        ],
        "misconception_tags": ["bar_graph_histogram_spacing_confusion"],
        "diagram_spec": None,
    }


def arch_08_bar_graph_identifying_mode_category(rng: random.Random) -> Dict[str, Any]:
    categories = ["Cat", "Dog", "Bird", "Fish"]
    counts = [14, 28, 9, 12]
    mode_cat = "Dog"

    seed_val = rng.randint(1, 1000000)
    svg = draw_bar_chart_svg(
        categories=categories,
        values=[float(c) for c in counts],
        title="Favorite Pets Survey",
        y_label="Number of Votes",
        seed=seed_val,
    )

    return {
        "title": "Identifying Mode from Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "08_bar_graph_identifying_mode_category",
        "difficulty": "easy",
        "question_text": (
            "Refer to the bar graph below.\n\n"
            "Which pet is the **mode** (modal choice) in this survey?"
        ),
        "correct_answer": mode_cat,
        "marking_schema": [
            f"Identify tallest bar as mode: {mode_cat} (1 mark)",
        ],
        "hints": [
            "The mode is the category with the highest frequency.",
            f"The tallest bar corresponds to '{mode_cat}' with 28 votes.",
            f"Mode = {mode_cat}.",
        ],
        "misconception_tags": ["mode_bar_height_identification_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_09_bar_graph_frequency_ratio_comparison(rng: random.Random) -> Dict[str, Any]:
    categories = ["Fiction", "Comics", "Science", "Biography"]
    counts = [30, 15, 20, 10]
    # Ratio Fiction : Comics = 30 : 15 = 2 : 1
    seed_val = rng.randint(1, 1000000)
    svg = draw_bar_chart_svg(
        categories=categories,
        values=[float(c) for c in counts],
        title="Books Borrowed from Library",
        y_label="Books Borrowed",
        seed=seed_val,
    )

    return {
        "title": "Frequency Ratio from Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "09_bar_graph_frequency_ratio_comparison",
        "difficulty": "medium",
        "question_text": (
            "Refer to the bar graph below.\n\n"
            "Express the ratio of **Fiction books** to **Comics** in its simplest form."
        ),
        "correct_answer": "2 : 1",
        "marking_schema": [
            "Ratio 30 : 15 simplified to 2 : 1: 1 mark",
        ],
        "hints": [
            "Fiction = 30; Comics = 15.",
            "Write the ratio: $30 : 15$.",
            "Divide both sides by 15: $2 : 1$.",
        ],
        "misconception_tags": ["ratio_simplification_order_inversion"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_10_bar_graph_data_ordering_category_ranking(rng: random.Random) -> Dict[str, Any]:
    categories = ["Walking", "Bicycle", "Bus", "Taxi"]
    counts = [42, 18, 35, 25]
    ranked = ["Walking", "Bus", "Taxi", "Bicycle"]
    ans = "; ".join(ranked)

    seed_val = rng.randint(1, 1000000)
    svg = draw_bar_chart_svg(
        categories=categories,
        values=[float(c) for c in counts],
        title="Commuting Modes Survey",
        y_label="Learners",
        seed=seed_val,
    )

    return {
        "title": "Ranking Categories from Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "10_bar_graph_data_ordering_category_ranking",
        "difficulty": "medium",
        "question_text": (
            "Refer to the bar graph below.\n\n"
            "Rank the four commuting modes in **descending order** of popularity (from most to least popular)."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"List in descending order: {ans} (1 mark)",
        ],
        "hints": [
            "Descending order means from tallest bar to shortest bar.",
            "Walking (42), Bus (35), Taxi (25), Bicycle (18).",
            f"Order: {ans}.",
        ],
        "misconception_tags": ["ranking_order_inversion"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_11_double_bar_graph_reading_comparative_values(rng: random.Random) -> Dict[str, Any]:
    b_val = rng.randint(22, 38)
    g_val = rng.randint(25, 42)

    return {
        "title": "Reading Double Bar Graph Comparative Data",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "11_double_bar_graph_reading_comparative_values",
        "difficulty": "easy",
        "question_text": (
            "A double bar graph compares textbook numbers between Boys and Girls in Grade 8A:\n\n"
            f"| Subject | Boys | Girls |\n"
            f"| :--- | :---: | :---: |\n"
            f"| Mathematics | {b_val} | {g_val} |\n\n"
            "How many **girls** in Grade 8A have Mathematics textbooks?"
        ),
        "correct_answer": str(g_val),
        "marking_schema": [
            f"Read Girls column value: {g_val} (1 mark)",
        ],
        "hints": [
            "Locate the category 'Mathematics' and check the column corresponding to Girls.",
            f"Number of girls = {g_val}.",
        ],
        "misconception_tags": ["double_bar_series_legend_inversion"],
        "diagram_spec": None,
    }


def arch_12_double_bar_graph_identifying_largest_gap(rng: random.Random) -> Dict[str, Any]:
    cats = ["Athletics", "Swimming", "Chess"]
    b_counts = [35, 20, 15]
    g_counts = [32, 38, 14]
    diffs = [abs(b - g) for b, g in zip(b_counts, g_counts)]  # [3, 18, 1]
    max_cat = "Swimming"

    return {
        "title": "Finding Largest Disparity in Double Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "12_double_bar_graph_identifying_largest_gap",
        "difficulty": "medium",
        "question_text": (
            "A comparative double bar graph shows club participation by gender:\n\n"
            "| Club | Boys | Girls |\n"
            "| :--- | :---: | :---: |\n"
            f"| Athletics | {b_counts[0]} | {g_counts[0]} |\n"
            f"| Swimming | {b_counts[1]} | {g_counts[1]} |\n"
            f"| Chess | {b_counts[2]} | {g_counts[2]} |\n\n"
            "In which club is the **difference** between boys and girls the greatest?"
        ),
        "correct_answer": f"{max_cat} (difference of {diffs[1]} learners)",
        "marking_schema": [
            f"Calculate differences and identify {max_cat}: 1 mark",
        ],
        "hints": [
            f"Athletics difference: |{b_counts[0]} - {g_counts[0]}| = {diffs[0]}.",
            f"Swimming difference: |{b_counts[1]} - {g_counts[1]}| = {diffs[1]}.",
            f"Chess difference: |{b_counts[2]} - {g_counts[2]}| = {diffs[2]}.",
            f"Greatest disparity: {max_cat}.",
        ],
        "misconception_tags": ["disparity_magnitude_calculation_error"],
        "diagram_spec": None,
    }


def arch_13_double_bar_graph_calculating_overall_total_both_groups(rng: random.Random) -> Dict[str, Any]:
    b = [rng.randint(15, 25), rng.randint(20, 30)]
    g = [rng.randint(18, 28), rng.randint(22, 32)]
    total = sum(b) + sum(g)

    return {
        "title": "Total Frequency Across Both Series in Double Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "13_double_bar_graph_calculating_overall_total_both_groups",
        "difficulty": "medium",
        "question_text": (
            "A comparative double bar graph shows participants across two grades:\n\n"
            "| Grade | Boys | Girls |\n"
            "| :--- | :---: | :---: |\n"
            f"| Grade 8 | {b[0]} | {g[0]} |\n"
            f"| Grade 9 | {b[1]} | {g[1]} |\n\n"
            "Calculate the grand total of learners surveyed across both grades and genders."
        ),
        "correct_answer": str(total),
        "marking_schema": [
            f"Sum all four entries: {b[0]} + {g[0]} + {b[1]} + {g[1]} = {total} (1 mark)",
        ],
        "hints": [
            "Add all frequencies from both the Boys series and Girls series.",
            f"${b[0]} + {g[0]} + {b[1]} + {g[1]} = {total}$.",
            f"Grand total = {total}.",
        ],
        "misconception_tags": ["double_bar_partial_sum_slip"],
        "diagram_spec": None,
    }


def arch_14_double_bar_graph_purpose_of_legend(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Purpose of a Legend in Comparative Graphs",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "14_double_bar_graph_purpose_of_legend",
        "difficulty": "easy",
        "question_text": (
            "Explain why a **legend (key)** is essential in a double bar graph."
        ),
        "correct_answer": "It identifies which color or shading represents each of the two comparative data sets.",
        "marking_schema": [
            "Explain that the legend distinguishes between the two sets of data: 1 mark",
        ],
        "hints": [
            "In a double bar graph, each category has two side-by-side bars of different colors.",
            "Without a key, a reader cannot tell which bar represents which group (e.g. boys vs girls).",
            "The legend clarifies which color represents each data set.",
        ],
        "misconception_tags": ["legend_function_misunderstanding"],
        "diagram_spec": None,
    }


def arch_15_double_bar_graph_category_comparison_ratio(rng: random.Random) -> Dict[str, Any]:
    b = 24
    g = 36
    # 24 : 36 = 2 : 3

    return {
        "title": "Category Comparison Ratio from Double Bar Data",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "15_double_bar_graph_category_comparison_ratio",
        "difficulty": "medium",
        "question_text": (
            f"In a science club, there are **{b} boys** and **{g} girls**.\n\n"
            "Express the ratio of boys to girls in its simplest form."
        ),
        "correct_answer": "2 : 3",
        "marking_schema": [
            "Simplify ratio 24 : 36 = 2 : 3: 1 mark",
        ],
        "hints": [
            f"Write the ratio: ${b} : {g}$.",
            "Divide both terms by their highest common factor (12).",
            "Simplified ratio = 2 : 3.",
        ],
        "misconception_tags": ["ratio_simplification_order_inversion"],
        "diagram_spec": None,
    }


def arch_16_double_bar_graph_determining_which_group_has_higher_overall_sum(rng: random.Random) -> Dict[str, Any]:
    b_vals = [25, 30, 20]
    g_vals = [22, 35, 24]
    tot_b = sum(b_vals)
    tot_g = sum(g_vals)
    higher = "Girls" if tot_g > tot_b else "Boys"

    return {
        "title": "Comparing Overall Series Totals",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "16_double_bar_graph_determining_which_group_has_higher_overall_sum",
        "difficulty": "medium",
        "question_text": (
            "A survey across three activities recorded:\n"
            f"- Boys: {b_vals[0]}, {b_vals[1]}, {b_vals[2]}\n"
            f"- Girls: {g_vals[0]}, {g_vals[1]}, {g_vals[2]}\n\n"
            "Which group (Boys or Girls) had the higher total participation?"
        ),
        "correct_answer": f"{higher} (Total: {max(tot_b, tot_g)} vs {min(tot_b, tot_g)})",
        "marking_schema": [
            f"Sum each series: Boys={tot_b}, Girls={tot_g} and state {higher}: 1 mark",
        ],
        "hints": [
            f"Total Boys = ${b_vals[0]} + {b_vals[1]} + {b_vals[2]} = {tot_b}$.",
            f"Total Girls = ${g_vals[0]} + {g_vals[1]} + {g_vals[2]} = {tot_g}$.",
            f"{higher} had the higher total.",
        ],
        "misconception_tags": ["series_total_comparison_error"],
        "diagram_spec": None,
    }


def arch_17_double_bar_graph_trend_comparison_across_grades(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Trend Comparison Across Grades",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "17_double_bar_graph_trend_comparison_across_grades",
        "difficulty": "easy",
        "question_text": (
            "In Grade 8, 40 learners participate in music. In Grade 9, 25 learners participate in music.\n\n"
            "Did music participation **increase** or **decrease** from Grade 8 to Grade 9?"
        ),
        "correct_answer": "Decrease",
        "marking_schema": [
            "State decrease from 40 to 25: 1 mark",
        ],
        "hints": [
            "Compare the two values: 25 < 40.",
            "Participation decreased by 15 learners.",
        ],
        "misconception_tags": ["trend_direction_inversion"],
        "diagram_spec": None,
    }


def arch_18_double_bar_graph_interpreting_percentage_scales(rng: random.Random) -> Dict[str, Any]:
    p_a = rng.choice([70, 75, 80])
    p_b = p_a - rng.choice([15, 20, 25])

    return {
        "title": "Comparing Percentages in Double Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "18_double_bar_graph_interpreting_percentage_scales",
        "difficulty": "easy",
        "question_text": (
            f"In a comparative study of school facilities, **{p_a}%** of schools in Province A have electricity, "
            f"compared to **{p_b}%** of schools in Province B.\n\n"
            "By how many percentage points does Province A exceed Province B?"
        ),
        "correct_answer": f"{p_a - p_b} percentage points",
        "marking_schema": [
            f"Subtract percentages: {p_a}% - {p_b}% = {p_a - p_b} percentage points (1 mark)",
        ],
        "hints": [
            f"Subtract Province B's percentage from Province A's: ${p_a} - {p_b}$.",
            f"Difference = {p_a - p_b} percentage points.",
        ],
        "misconception_tags": ["percentage_point_difference_slip"],
        "diagram_spec": None,
    }


def arch_19_double_bar_graph_identifying_category_where_group_b_exceeds_group_a(rng: random.Random) -> Dict[str, Any]:
    cats = ["Maths", "Science", "History"]
    a_vals = [35, 30, 22]
    b_vals = [28, 38, 20]
    # In Science, B (38) > A (30)

    return {
        "title": "Identifying Where Series B Exceeds Series A",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "19_double_bar_graph_identifying_category_where_group_b_exceeds_group_a",
        "difficulty": "medium",
        "question_text": (
            "Refer to the comparative data below:\n\n"
            "| Subject | Group A | Group B |\n"
            "| :--- | :---: | :---: |\n"
            "| Maths | 35 | 28 |\n"
            "| Science | 30 | 38 |\n"
            "| History | 22 | 20 |\n\n"
            "In which subject did **Group B** achieve a higher score than Group A?"
        ),
        "correct_answer": "Science",
        "marking_schema": [
            "Identify Science where Group B (38) > Group A (30): 1 mark",
        ],
        "hints": [
            "Compare Group B and Group A for each subject.",
            "For Science: 38 > 30.",
            "Subject = Science.",
        ],
        "misconception_tags": ["comparative_column_inversion"],
        "diagram_spec": None,
    }


def arch_20_double_bar_graph_constructing_comparison_table_from_bars(rng: random.Random) -> Dict[str, Any]:
    b_maths = rng.randint(20, 30)
    g_maths = rng.randint(22, 32)

    return {
        "title": "Constructing Table Entry from Comparative Bars",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "20_double_bar_graph_constructing_comparison_table_from_bars",
        "difficulty": "easy",
        "question_text": (
            f"On a double bar graph for Mathematics, the blue bar (Boys) reaches a height of **{b_maths}** "
            f"and the red bar (Girls) reaches a height of **{g_maths}**.\n\n"
            "State the total number of learners represented by both bars for Mathematics."
        ),
        "correct_answer": str(b_maths + g_maths),
        "marking_schema": [
            f"Add boys and girls: {b_maths} + {g_maths} = {b_maths + g_maths} (1 mark)",
        ],
        "hints": [
            f"Add the heights of the two bars: ${b_maths} + {g_maths}$.",
            f"Total = {b_maths + g_maths}.",
        ],
        "misconception_tags": ["comparative_bar_sum_error"],
        "diagram_spec": None,
    }


def arch_21_histogram_reading_interval_frequency(rng: random.Random) -> Dict[str, Any]:
    intervals = ["10 - 19", "20 - 29", "30 - 39", "40 - 49"]
    freqs = [float(rng.randint(5, 20)) for _ in intervals]
    target_idx = rng.randint(0, 3)
    target_int = intervals[target_idx]
    target_f = int(freqs[target_idx])

    seed_val = rng.randint(1, 1000000)
    svg = draw_histogram_svg(
        intervals=intervals,
        frequencies=freqs,
        title="Mathematics Test Score Histogram",
        x_label="Marks (%)",
        y_label="Frequency",
        seed=seed_val,
    )

    return {
        "title": "Reading Class Interval Frequency from Histogram",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "21_histogram_reading_interval_frequency",
        "difficulty": "easy",
        "question_text": (
            "Refer to the histogram below representing test marks.\n\n"
            f"What is the frequency of learners who scored in the interval **{target_int}**?"
        ),
        "correct_answer": str(target_f),
        "marking_schema": [
            f"Read height of interval {target_int}: {target_f} (1 mark)",
        ],
        "hints": [
            f"Find the bar corresponding to interval '{target_int}'.",
            "Trace its height to the vertical frequency axis.",
            f"Frequency = {target_f}.",
        ],
        "misconception_tags": ["histogram_interval_reading_slip"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_22_histogram_why_bars_touch_no_spaces(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Why Histogram Bars Touch Without Spaces",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "22_histogram_why_bars_touch_no_spaces",
        "difficulty": "medium",
        "question_text": (
            "Explain why the vertical bars in a histogram **touch each other without spaces** between them."
        ),
        "correct_answer": "Because a histogram represents continuous numerical data where intervals form an unbroken, continuous scale.",
        "marking_schema": [
            "Explain that continuous numerical data forms an unbroken scale with no gaps between intervals: 1 mark",
        ],
        "hints": [
            "Think about the type of data shown in histograms (measurements like time, mass, continuous intervals).",
            "Since the scale flows continuously from one interval directly into the next, there are no gaps.",
            "Bars touch because the data is continuous.",
        ],
        "misconception_tags": ["histogram_continuous_scale_gap_concept_gap"],
        "diagram_spec": None,
    }


def arch_23_histogram_identifying_modal_class_interval(rng: random.Random) -> Dict[str, Any]:
    intervals = ["0 - 9", "10 - 19", "20 - 29", "30 - 39"]
    freqs = [6.0, 14.0, 22.0, 8.0]
    modal_int = "20 - 29"

    seed_val = rng.randint(1, 1000000)
    svg = draw_histogram_svg(
        intervals=intervals,
        frequencies=freqs,
        title="Speed of Vehicles Recorded",
        x_label="Speed (km/h)",
        y_label="Frequency",
        seed=seed_val,
    )

    return {
        "title": "Identifying Modal Class from Histogram",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "23_histogram_identifying_modal_class_interval",
        "difficulty": "easy",
        "question_text": (
            "Refer to the histogram below.\n\n"
            "Identify the **modal class interval**."
        ),
        "correct_answer": modal_int,
        "marking_schema": [
            f"Identify tallest bar interval: {modal_int} (1 mark)",
        ],
        "hints": [
            "The modal class interval is represented by the tallest bar in the histogram.",
            f"The tallest bar has height 22, corresponding to {modal_int}.",
            f"Modal class interval: {modal_int}.",
        ],
        "misconception_tags": ["modal_interval_identification_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_24_histogram_calculating_total_sample_size(rng: random.Random) -> Dict[str, Any]:
    intervals = ["10 - 19", "20 - 29", "30 - 39"]
    freqs = [float(rng.randint(8, 16)) for _ in intervals]
    tot = int(sum(freqs))

    seed_val = rng.randint(1, 1000000)
    svg = draw_histogram_svg(
        intervals=intervals,
        frequencies=freqs,
        title="Weekly Study Hours",
        x_label="Hours",
        y_label="Learners",
        seed=seed_val,
    )

    return {
        "title": "Calculating Total Sample Size from Histogram",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "24_histogram_calculating_total_sample_size",
        "difficulty": "medium",
        "question_text": (
            "Refer to the histogram below.\n\n"
            "Calculate the total number of learners represented across all three intervals combined."
        ),
        "correct_answer": str(tot),
        "marking_schema": [
            f"Sum all bar heights: {int(freqs[0])} + {int(freqs[1])} + {int(freqs[2])} = {tot} (1 mark)",
        ],
        "hints": [
            "Add the heights of all the bars in the histogram.",
            f"${int(freqs[0])} + {int(freqs[1])} + {int(freqs[2])} = {tot}$.",
            f"Total = {tot}.",
        ],
        "misconception_tags": ["histogram_total_frequency_sum_slip"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_25_histogram_counting_values_above_or_below_interval_threshold(rng: random.Random) -> Dict[str, Any]:
    intervals = ["40 - 49", "50 - 59", "60 - 69", "70 - 79"]
    freqs = [5.0, 12.0, 18.0, 10.0]
    # Scoring >= 60%: intervals 60-69 and 70-79 => 18 + 10 = 28
    tot_pass = 28

    seed_val = rng.randint(1, 1000000)
    svg = draw_histogram_svg(
        intervals=intervals,
        frequencies=freqs,
        title="Grade 8 Exam Results",
        x_label="Marks (%)",
        y_label="Frequency",
        seed=seed_val,
    )

    return {
        "title": "Counting Above a Threshold on Histogram",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "25_histogram_counting_values_above_or_below_interval_threshold",
        "difficulty": "medium",
        "question_text": (
            "Refer to the histogram below.\n\n"
            "How many learners achieved a mark of **60% or higher**?"
        ),
        "correct_answer": str(tot_pass),
        "marking_schema": [
            f"Sum frequencies for intervals 60-69 and 70-79: 18 + 10 = {tot_pass} (2 marks)",
        ],
        "hints": [
            "Marks >= 60% include the intervals '60 - 69' and '70 - 79'.",
            f"Frequency 60-69 = 18; Frequency 70-79 = 10.",
            f"Total = $18 + 10 = {tot_pass}$.",
        ],
        "misconception_tags": ["histogram_threshold_single_bar_omission"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


BUILDERS_01_25 = [
    arch_01_bar_graph_reading_category_frequency,
    arch_02_bar_graph_identifying_highest_or_lowest_category,
    arch_03_bar_graph_calculating_difference_between_categories,
    arch_04_bar_graph_calculating_total_sample_frequency,
    arch_05_bar_graph_calculating_percentage_for_category,
    arch_06_bar_graph_features_axes_labels_and_scales,
    arch_07_bar_graph_why_bars_have_equal_spaces,
    arch_08_bar_graph_identifying_mode_category,
    arch_09_bar_graph_frequency_ratio_comparison,
    arch_10_bar_graph_data_ordering_category_ranking,
    arch_11_double_bar_graph_reading_comparative_values,
    arch_12_double_bar_graph_identifying_largest_gap,
    arch_13_double_bar_graph_calculating_overall_total_both_groups,
    arch_14_double_bar_graph_purpose_of_legend,
    arch_15_double_bar_graph_category_comparison_ratio,
    arch_16_double_bar_graph_determining_which_group_has_higher_overall_sum,
    arch_17_double_bar_graph_trend_comparison_across_grades,
    arch_18_double_bar_graph_interpreting_percentage_scales,
    arch_19_double_bar_graph_identifying_category_where_group_b_exceeds_group_a,
    arch_20_double_bar_graph_constructing_comparison_table_from_bars,
    arch_21_histogram_reading_interval_frequency,
    arch_22_histogram_why_bars_touch_no_spaces,
    arch_23_histogram_identifying_modal_class_interval,
    arch_24_histogram_calculating_total_sample_size,
    arch_25_histogram_counting_values_above_or_below_interval_threshold,
]
