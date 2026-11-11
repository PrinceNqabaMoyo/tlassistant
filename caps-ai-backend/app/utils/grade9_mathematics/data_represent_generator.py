"""Grade 9 Mathematics — Representing Data Generator (Deterministic 6-Pillar Contract).

Curriculum Alignment:
- Grade 9 Term 4: Representing data
- South African National Curriculum Standards (Senior Phase Mathematics)
- Graphical data displays:
  * Pie charts: sector angle calculations (Angle = f / N * 360°) and percentages
  * Histograms vs Bar graphs: continuous class intervals, no gaps between bars
  * Double bar graphs: comparing two categorical series side-by-side
  * Scatter plots: bivariate data, correlation (positive, negative, none) & line of best fit

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with formula, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs (kind: 'scatter_plot_regression', 'statistics_box_and_ogive', 'function_graph')
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng

TOPIC = "grade9_math_data_represent"
LO = "math9_data_represent"


def generate_grade9_data_represent_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "pie_chart_sector_angles",
        "histogram_vs_bar_graph",
        "scatter_plot_correlation",
        "double_bar_graph_comparison",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_datarep_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "pie_chart_sector_angles":
        # Total frequency chosen so fractions simplify cleanly (e.g. N = 60, 72, 90, 120, 180, 360)
        total_n = r.choice([60, 72, 90, 120, 180])
        # 4 categories (e.g. Sports: Soccer, Netball, Rugby, Cricket)
        f1 = int(total_n * r.choice([0.40, 0.35, 0.30]))
        f2 = int(total_n * 0.25)
        f3 = int(total_n * 0.20)
        f4 = total_n - (f1 + f2 + f3)
        
        categories = ["Soccer", "Netball", "Rugby", "Cricket"]
        counts = [f1, f2, f3, f4]
        
        # Calculate angles: (f / total_n) * 360
        angles = [int((c / total_n) * 360) for c in counts]
        percentages = [round((c / total_n) * 100, 1) for c in counts]

        question_text = (
            f"A survey was conducted among $N = {total_n}$ Grade 9 learners to determine their favourite sport:\n\n"
            f"| Sport | Number of Learners ($f$) |\n"
            f"| :--- | :---: |\n"
            f"| {categories[0]} | ${counts[0]}$ |\n"
            f"| {categories[1]} | ${counts[1]}$ |\n"
            f"| {categories[2]} | ${counts[2]}$ |\n"
            f"| {categories[3]} | ${counts[3]}$ |\n\n"
            f"1. Calculate the sector angle (in degrees) representing **{categories[0]}** on a pie chart.\n"
            f"2. Calculate the sector angle representing **{categories[1]}**.\n"
            f"3. What percentage of the learners chose **{categories[0]}**?"
        )

        steps = [
            {"id": "S1", "statement": f"Sector angle formula: $\\text{{Angle}} = \\frac{{f}}{{N}} \\times 360^\\circ$", "reason": "pie chart sector formula", "deps": []},
            {"id": "S2", "statement": f"{categories[0]} angle: $\\frac{{{counts[0]}}}{{{total_n}}} \\times 360^\\circ = {angles[0]}^\\circ$", "reason": "arithmetic", "deps": ["S1"]},
            {"id": "S3", "statement": f"{categories[1]} angle: $\\frac{{{counts[1]}}}{{{total_n}}} \\times 360^\\circ = {angles[1]}^\\circ$", "reason": "arithmetic", "deps": ["S1"]},
            {"id": "S4", "statement": f"Percentage: $\\frac{{{counts[0]}}}{{{total_n}}} \\times 100\\% = {percentages[0]}\\%$", "reason": "percentage formula", "deps": ["S2"]},
        ]

        hints = [
            "A complete circle comprises 360°. The size of each sector angle is proportional to its fraction of the total frequency N.",
            f"Sector Angle = $\\frac{{\\text{{Frequency}}}}{{{total_n}}} \\times 360^\\circ$.",
            f"{categories[0]}: $\\frac{{{counts[0]}}}{{{total_n}}} \\times 360^\\circ = {angles[0]}^\\circ$. Percentage: $\\frac{{{counts[0]}}}{{{total_n}}} \\times 100\\% = {percentages[0]}\\%$.",
        ]

        error_tax = [
            {
                "id": "err_used_100_degrees",
                "tag": "misconception_percentage_vs_degrees",
                "condition": f"Calculated (f / {total_n}) * 100 for the angle",
                "feedback": "A full pie chart has 360 degrees, not 100 degrees! Multiply by 360° to find sector angle in degrees.",
            },
        ]

        sample_answer = (
            f"1. {categories[0]} angle $= \\frac{{{counts[0]}}}{{{total_n}}} \\times 360^\\circ = {angles[0]}^\\circ$\n"
            f"2. {categories[1]} angle $= \\frac{{{counts[1]}}}{{{total_n}}} \\times 360^\\circ = {angles[1]}^\\circ$\n"
            f"3. Percentage for {categories[0]} $= \\frac{{{counts[0]}}}{{{total_n}}} \\times 100\\% = {percentages[0]}\\%$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "statistics_box_and_ogive",
            "caption": f"Pie chart distribution for N = {total_n} learners",
        }

        correct_ans = f"{categories[0]} = {angles[0]}°, {categories[1]} = {angles[1]}°, {percentages[0]}%"
        subskill_id = "pie_chart_sector_angles"
        reason_code = "Sector Angle = (f / N) * 360°"
        marks = 4

    elif archetype == "histogram_vs_bar_graph":
        # Key Grade 9 conceptual distinction: Bar graph (discrete/categorical, gaps between bars) vs Histogram (continuous data grouped into intervals, touching bars with no gaps)
        question_text = (
            f"A researcher collected two sets of data:\n"
            f"- **Dataset A:** Favourite fast-food restaurants chosen by learners (e.g. Steers, KFC, Nando's).\n"
            f"- **Dataset B:** Continuous heights of Grade 9 learners grouped into intervals (e.g. $140 \\le h < 150\\text{{ cm}}$, $150 \\le h < 160\\text{{ cm}}$).\n\n"
            f"1. Which type of graph (Bar Graph or Histogram) should be used to display Dataset A? Explain why.\n"
            f"2. Which type of graph should be used to display Dataset B? Explain why.\n"
            f"3. State the key visual difference between the bars of a bar graph and the bars of a histogram."
        )

        steps = [
            {"id": "S1", "statement": "Dataset A: Bar graph (discrete categorical data)", "reason": "graph selection criterion", "deps": []},
            {"id": "S2", "statement": "Dataset B: Histogram (continuous quantitative data grouped into class intervals)", "reason": "histogram definition", "deps": []},
            {"id": "S3", "statement": "Visual difference: Bar graphs have distinct gaps between bars; histograms have touching bars with no spaces between them.", "reason": "continuity representation", "deps": ["S1", "S2"]},
        ]

        hints = [
            "Bar graphs are used for separate, distinct categories (discrete data). Histograms are used for continuous measurement data grouped in numerical intervals.",
            "In a bar graph, categories are separate words/items, so spaces/gaps are drawn between bars.",
            "In a histogram, the data is continuous along a numerical axis, so the bars touch each other with no gaps between consecutive intervals.",
        ]

        error_tax = [
            {
                "id": "err_gaps_in_histogram",
                "tag": "misconception_histogram_gaps",
                "condition": "Stated that histograms have gaps between bars",
                "feedback": "Histograms NEVER have gaps between bars (unless a class interval has zero frequency). The touching bars visually represent continuous data.",
            },
        ]

        sample_answer = (
            f"1. **Dataset A:** Bar Graph. Favourite restaurants are discrete categorical data (separate non-numeric categories).\n"
            f"2. **Dataset B:** Histogram. Heights are continuous numerical data grouped into continuous class intervals.\n"
            f"3. **Key visual difference:** A bar graph has spaces/gaps between consecutive bars to show distinct categories, whereas a histogram has touching bars with NO gaps to represent continuous data."
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "statistics_box_and_ogive",
            "caption": "Comparison: Discrete Bar Graph vs Continuous Histogram",
        }

        correct_ans = "Dataset A: Bar graph; Dataset B: Histogram; Difference: Touching vs spaces"
        subskill_id = "histogram_vs_bar_graph"
        reason_code = "data classification: discrete vs continuous"
        marks = 3

    elif archetype == "scatter_plot_correlation":
        # Scatter plots: identifying correlation (positive, negative, no correlation)
        corr_type = r.choice(["positive", "negative", "none"])
        if corr_type == "positive":
            scenario = "Hours spent studying for a mathematics test ($x$) vs test mark percentage ($y$)"
            pattern_desc = "As study hours increase, test marks generally increase."
            corr_name = "Positive correlation"
            slope_sign = "positive"
        elif corr_type == "negative":
            scenario = "Number of missed classes / days absent ($x$) vs overall exam mark ($y$)"
            pattern_desc = "As the number of days absent increases, the exam mark generally decreases."
            corr_name = "Negative correlation"
            slope_sign = "negative"
        else:
            scenario = "Shoe size ($x$) vs mathematics test mark ($y$)"
            pattern_desc = "Points are scattered randomly with no clear upward or downward linear trend."
            corr_name = "No correlation (zero correlation)"
            slope_sign = "zero"

        question_text = (
            f"A scatter plot is drawn to investigate the relationship between two variables:\n"
            f"**Scenario:** {scenario}.\n\n"
            f"1. Identify the type of correlation ({corr_name.split()[0]} correlation, Negative correlation, or No correlation) described by this relationship.\n"
            f"2. Describe the trend of the data points and the direction of the line of best fit.\n"
            f"3. Does correlation between two variables prove that one variable causes the other (causation)? Explain briefly."
        )

        steps = [
            {"id": "S1", "statement": f"Correlation: {corr_name}", "reason": "bivariate trend analysis", "deps": []},
            {"id": "S2", "statement": f"Trend: {pattern_desc}. Line of best fit has a {slope_sign} slope.", "reason": "trendline slope", "deps": ["S1"]},
            {"id": "S3", "statement": "No, correlation does not imply causation (a third lurking variable could be responsible).", "reason": "correlation vs causation principle", "deps": []},
        ]

        hints = [
            "If both variables increase together, the correlation is positive. If one increases while the other decreases, the correlation is negative. If points are randomly scattered, there is no correlation.",
            f"Scenario: {scenario}. Pattern: {pattern_desc}.",
            "Crucial statistical rule: Correlation indicates a relationship or pattern, but does NOT prove that one variable directly causes the other (correlation ≠ causation).",
        ]

        error_tax = [
            {
                "id": "err_correlation_equals_causation",
                "tag": "misconception_correlation_causation",
                "condition": "Claimed that correlation proves causation",
                "feedback": "Correlation only shows an association between variables; it does NOT prove causation. Other factors or coincidence may be involved.",
            },
        ]

        sample_answer = (
            f"1. **{corr_name}**\n"
            f"2. {pattern_desc} The line of best fit slopes {'upwards from left to right' if corr_type == 'positive' else 'downwards from left to right' if corr_type == 'negative' else 'horizontally or cannot be drawn'}.\n"
            f"3. **No**, correlation does NOT prove causation. An observed relationship between two variables does not necessarily mean that changes in one variable cause changes in the other; both could be influenced by an external third factor."
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "scatter_plot_regression",
            "caption": f"Scatter plot: {scenario} ({corr_name})",
        }

        correct_ans = f"{corr_name}; Correlation != Causation"
        subskill_id = "scatter_plot_correlation"
        reason_code = "bivariate correlation analysis"
        marks = 3

    else:
        # double_bar_graph_comparison
        # Comparing two groups (e.g. Boys vs Girls or Term 1 vs Term 2) across 4 subjects
        subjects = ["Maths", "Science", "English", "History"]
        boys = [r.randint(55, 75) for _ in range(4)]
        girls = [r.randint(58, 80) for _ in range(4)]
        
        # Ask to compare which subject had highest difference
        diffs = [abs(g - b) for g, b in zip(girls, boys)]
        max_diff = max(diffs)
        max_idx = diffs.index(max_diff)
        max_subj = subjects[max_idx]

        question_text = (
            f"A double bar graph displays the average percentage marks of Boys and Girls across four subjects:\n\n"
            f"| Subject | Boys (%) | Girls (%) |\n"
            f"| :--- | :---: | :---: |\n"
            f"| {subjects[0]} | ${boys[0]}\\%$ | ${girls[0]}\\%$ |\n"
            f"| {subjects[1]} | ${boys[1]}\\%$ | ${girls[1]}\\%$ |\n"
            f"| {subjects[2]} | ${boys[2]}\\%$ | ${girls[2]}\\%$ |\n"
            f"| {subjects[3]} | ${boys[3]}\\%$ | ${girls[3]}\\%$ |\n\n"
            f"1. In which subject was the difference between Boys and Girls the greatest?\n"
            f"2. Calculate this greatest difference.\n"
            f"3. In how many of the four subjects did Girls outperform Boys?"
        )

        girls_higher_count = sum(1 for g, b in zip(girls, boys) if g > b)

        steps = [
            {"id": "S1", "statement": f"Differences: {', '.join(f'{s}: |{g}-{b}| = {d}%' for s, g, b, d in zip(subjects, girls, boys, diffs))}", "reason": "calculate differences", "deps": []},
            {"id": "S2", "statement": f"Greatest difference is in {max_subj} with difference of ${max_diff}\\%$", "reason": "maximum identification", "deps": ["S1"]},
            {"id": "S3", "statement": f"Girls outperformed Boys in ${girls_higher_count}$ subjects", "reason": "count comparison", "deps": []},
        ]

        hints = [
            "A double bar graph allows direct side-by-side comparison between two sub-groups for each category.",
            f"Calculate the absolute difference |Girls - Boys| for each subject: {', '.join(f'{s} = {d}%' for s, d in zip(subjects, diffs))}.",
            f"The largest difference is in {max_subj} ({max_diff}%). Count how many times the Girls' mark is higher than the Boys' mark ({girls_higher_count} subjects).",
        ]

        error_tax = [
            {
                "id": "err_misread_categories",
                "tag": "misconception_double_bar_reading",
                "condition": "Selected subject with highest absolute score instead of highest difference",
                "feedback": "The question asked for the subject with the GREATEST DIFFERENCE between boys and girls, not the subject with the highest overall score.",
            },
        ]

        sample_answer = (
            f"1. Greatest difference: **{max_subj}**\n"
            f"2. Difference $= |{girls[max_idx]} - {boys[max_idx]}| = {max_diff}\\%$\n"
            f"3. Girls outperformed Boys in **{girls_higher_count}** of the 4 subjects."
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "statistics_box_and_ogive",
            "caption": "Double Bar Graph comparing Boys and Girls performance",
        }

        correct_ans = f"{max_subj} ({max_diff}%); {girls_higher_count} subjects"
        subskill_id = "double_bar_graph_comparison"
        reason_code = "double bar graph comparative analysis"
        marks = 3

    q = {
        "id": qid,
        "subject": "Mathematics",
        "grade": 9,
        "topic": TOPIC,
        "subskill": subskill_id,
        "learning_objective_id": LO,
        "mode": mode,
        "difficulty": difficulty,
        "question_type": "free_response",
        "answer_mode": "free_response",
        "prompt": question_text,
        "question": question_text,
        "prompt_latex": question_text,
        "answer_latex": correct_ans,
        "correct_answer": correct_ans,
        "sample_answer": sample_answer,
        "worked_solution": sample_answer,
        "canonical_solution": sample_answer,
        "marking_schema": [
            {"criterion": f"Correct graphical concept and calculation [{reason_code}]", "marks": 1},
            {"criterion": f"Accurate values and answers {correct_ans}", "marks": marks - 1},
        ],
        "marks": marks,
        "hints": hints,
        "hint_sections": {
            "concept": hints[0],
            "rules": hints[1],
            "step_by_step": hints[2],
        },
        "misconception_tags": [m["tag"] for m in error_tax],
        "diagnostic_tags": [f"diag_{subskill_id}"],
        "keywords": ["representing data", "pie chart", "histogram", "bar graph", "double bar graph", "scatter plot", "correlation"],
        "term": 4,
        "caps_weight_percent": 10.0,
        "suggested_duration_mins": 5,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Construct and interpret data representations",
            "steps": steps,
        },
        "metadata": {
            "diagram_spec": diagram_spec,
            "answer_value": correct_ans,
            "reason_code": reason_code,
        },
    }
    return q


def generate(seed: Optional[int] = None, count: int = 1, **kwargs: Any) -> Dict[str, Any]:
    r = rng(seed)
    questions = []
    for _ in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        questions.append(generate_grade9_data_represent_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
