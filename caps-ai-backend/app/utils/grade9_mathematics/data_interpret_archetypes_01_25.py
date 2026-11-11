"""Grade 9 Mathematics - Interpret, Analyse and Report on Data Archetypes 01-25 (CAPS Term 4).
Focus: Sampling bias, leading questions, truncated axes, scale manipulation, central tendency comparison,
and outlier impacts.
100% deterministic, zero LLM calls.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple


def _fmt(val: float, decimals: int = 1) -> str:
    s = f"{val:.{decimals}f}"
    return s.replace(".", "{,}")


# -----------------------------------------------------------------------------
# 01. Sampling Bias: Convenience Sample
# -----------------------------------------------------------------------------
def arch_01_identify_sampling_bias_convenience_sample(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("surveying only learners standing outside the tuckshop at break about healthy food options",
         "Convenience sampling / Location bias",
         "Learners queuing at the tuckshop already prefer tuckshop foods and do not represent the entire school population."),
        ("surveying spectators at a Saturday rugby match about the school's most popular sport",
         "Sampling bias / Unrepresentative sample",
         "People attending a rugby match are naturally biased toward rugby, neglecting learners interested in netball, soccer, or chess."),
        ("asking only learners arriving at school in private cars about public transport satisfaction",
         "Socioeconomic bias / Irrelevant sample",
         "Learners driven to school in private cars do not use buses or minibus taxis and cannot provide informed feedback on public transport."),
    ]
    situation, bias_type, explanation = r.choice(scenarios)

    prompt = (
        f"A learner researcher collects data by **{situation}**.\n"
        f"Identify the major source of bias in this data collection method and explain why the sample is unrepresentative."
    )
    ans_str = bias_type
    sol = (
        f"**Source of Bias**: {bias_type}.\n\n"
        f"**Reason**: {explanation}\n"
        f"A valid random sample must give every member of the target population an equal chance of being selected."
    )
    return {
        "subskill": "01_identify_sampling_bias_convenience_sample",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{bias_type}: {explanation}",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify bias: {bias_type}", "marks": 1},
            {"step": "Explain why sample is unrepresentative", "marks": 1},
        ],
        "hints": [
            "Consider whether every person in the school community had an equal chance of being surveyed.",
            "Selecting people from a specific convenient location introduces convenience sampling bias.",
        ],
        "misconception_tags": ["sampling_bias_unrecognised"],
    }


# -----------------------------------------------------------------------------
# 02. Sampling Bias: Voluntary Response
# -----------------------------------------------------------------------------
def arch_02_identify_sampling_bias_voluntary_response(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A principal posts an optional online poll on the school communicator app asking parents: "
        "'Should school start 30 minutes earlier?' Out of 800 families, only 45 parents respond, with 80% voting 'No'.\n"
        "Explain why this result cannot be generalized to the entire parent body."
    )
    concept = "Voluntary response bias with a very small response rate (45 out of 800); parents with strong negative feelings are much more likely to respond."
    return {
        "subskill": "02_identify_sampling_bias_voluntary_response",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Voluntary response bias / sample size too small",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify voluntary response bias", "marks": 1},
            {"step": "Note that 45/800 is unrepresentative (low response rate)", "marks": 1},
        ],
        "hints": [
            "Voluntary response polls attract individuals with passionate or extreme opinions.",
            "A sample of 45 out of 800 parents is less than 6% of the population.",
        ],
        "misconception_tags": ["voluntary_response_bias_confusion"],
    }


# -----------------------------------------------------------------------------
# 03. Sampling Bias: Sample Size Too Small
# -----------------------------------------------------------------------------
def arch_03_identify_sampling_bias_sample_size_too_small(r: random.Random) -> Dict[str, Any]:
    n_sample = r.randint(3, 6)
    prompt = (
        f"A cosmetics brand claims: '4 out of 5 teenagers prefer our acne face wash!' "
        f"The fine print reveals that exactly ${n_sample}$ teenagers were interviewed.\n"
        f"Why is this statistical claim unreliable for drawing a conclusion about all teenagers?"
    )
    concept = f"The sample size ($n = {n_sample}$) is far too small to be statistically significant or representative of millions of teenagers."
    return {
        "subskill": "03_identify_sampling_bias_sample_size_too_small",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Sample size is far too small",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that the sample size is inadequate", "marks": 1},
            {"step": "Explain that small samples produce extreme variability and cannot represent the population", "marks": 1},
        ],
        "hints": [
            f"Think about testing only {n_sample} individuals out of a huge population.",
            "Small samples have high random margin of error and cannot justify broad generalisations.",
        ],
        "misconception_tags": ["sample_size_significance_error"],
    }


# -----------------------------------------------------------------------------
# 04. Evaluate Leading Question in Survey
# -----------------------------------------------------------------------------
def arch_04_evaluate_leading_question_in_survey(r: random.Random) -> Dict[str, Any]:
    questions = [
        ("Do you agree that junk food should be banned because it causes obesity and poor health?",
         "It uses emotionally charged words ('causes obesity and poor health') that nudge the respondent toward agreeing.",
         "What is your opinion on whether junk food should be sold at school?"),
        ("Don't you agree that homework is stressful and should be reduced?",
         "The phrase 'Don't you agree' and 'stressful' biases the respondent toward answering yes.",
         "How many hours of homework do you think is appropriate each day?"),
        ("Given the brilliant performance of our soccer team, shouldn't sports funding be increased?",
         "The adjective 'brilliant' pre-judges the issue and influences the respondent.",
         "Should sports funding be increased, decreased, or kept the same?"),
    ]
    leading_q, flaw, neutral_q = r.choice(questions)

    prompt = (
        f"Examine this survey question:\n"
        f"**\"{leading_q}\"**\n\n"
        f"1. Explain why this is classified as a **leading question**.\n"
        f"2. Suggest an alternative neutral, unbiased wording."
    )
    return {
        "subskill": "04_evaluate_leading_question_in_survey",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Leading question / loaded wording",
        "sample_answer": f"Flaw: {flaw} Neutral rewrite: \"{neutral_q}\"",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify leading/loaded wording", "marks": 1},
            {"step": "Provide neutral alternative question", "marks": 1},
        ],
        "hints": [
            "A leading question guides or pressures the respondent to give a specific desired answer.",
            "Rephrase it using balanced, objective language without loaded adjectives.",
        ],
        "misconception_tags": ["leading_question_blindness"],
    }


# -----------------------------------------------------------------------------
# 05. Distinguish Between Population and Sample
# -----------------------------------------------------------------------------
def arch_05_distinguish_between_population_and_sample(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A municipal researcher tests water quality in 20 residential taps across Soweto to check municipal tap water safety for all 1.3 million residents.",
         "All residential tap water in Soweto (1.3 million residents)",
         "The 20 specific tap water samples collected"),
        ("A national retailer tests the battery life of 150 smartphones selected at random from a factory shipment of 10 000 units.",
         "The full shipment of 10 000 smartphones",
         "The 150 randomly selected smartphones"),
        ("A school with 1 200 learners surveys 60 learners selected at random about library opening hours.",
         "All 1 200 learners in the school",
         "The 60 randomly chosen learners"),
    ]
    context, pop, samp = r.choice(scenarios)

    prompt = (
        f"Consider this research scenario:\n"
        f"*{context}*\n\n"
        f"1. Identify the **target population**.\n"
        f"2. Identify the **sample**."
    )
    ans_str = f"Population: {pop}; Sample: {samp}"
    return {
        "subskill": "05_distinguish_between_population_and_sample",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Correct population: {pop}", "marks": 1},
            {"step": f"Correct sample: {samp}", "marks": 1},
        ],
        "hints": [
            "The population is the complete group being investigated.",
            "The sample is the subset of individuals or items actually measured.",
        ],
        "misconception_tags": ["population_vs_sample_confusion"],
    }


# -----------------------------------------------------------------------------
# 06. Detect Truncated Vertical Axis
# -----------------------------------------------------------------------------
def arch_06_detect_truncated_vertical_axis_in_bar_display(r: random.Random) -> Dict[str, Any]:
    val_a = r.randint(80, 85)
    val_b = val_a + r.randint(2, 5)
    axis_start = val_a - 1

    prompt = (
        f"In an advertisement, Brand A scored {val_a}% customer satisfaction and Brand B scored {val_b}%.\n"
        f"The vertical percentage scale begins at {axis_start}% instead of 0%.\n"
        f"Explain how this vertical scaling choice distorts the viewer's perception."
    )
    sol = (
        f"Because the vertical scale starts at {axis_start}% instead of 0%, the baseline is suppressed. "
        f"The bar for Brand B appears several times taller than Brand A, even though the actual difference "
        f"is only {val_b - val_a}%."
    )
    return {
        "subskill": "06_detect_truncated_vertical_axis_in_bar_display",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Truncated axis exaggerates differences",
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that vertical axis does not start at zero (truncated)", "marks": 1},
            {"step": "Explain that small differences appear exaggerated", "marks": 1},
        ],
        "hints": [
            "Check where the vertical scale starts.",
            "Starting above zero cuts off the bottom of the bars, magnifying tiny differences.",
        ],
        "misconception_tags": ["truncated_axis_distortion_error"],
    }


# -----------------------------------------------------------------------------
# 07. Calculate Actual vs Visual Ratio for Truncated Axis
# -----------------------------------------------------------------------------
def arch_07_calculate_actual_vs_visual_ratio_truncated_axis(r: random.Random) -> Dict[str, Any]:
    val_a = 50
    val_b = 55
    axis_start = 45

    vis_a = val_a - axis_start  # 5
    vis_b = val_b - axis_start  # 10
    vis_ratio = vis_b / vis_a   # 2.0
    actual_ratio = round(val_b / val_a, 2)  # 1.10

    prompt = (
        f"Two competitors have market shares of Brand A = 50% and Brand B = 55%.\n"
        f"A chart truncates the vertical axis to start at 45%.\n"
        f"1. Calculate the **actual ratio** of Brand B's share to Brand A's share ($\\frac{{55}}{{50}}$).\n"
        f"2. Calculate the **visual ratio** of the heights of the bars from the 45% baseline ($\\frac{{55 - 45}}{{50 - 45}}$)."
    )
    ans_str = f"Actual: {actual_ratio}; Visual: {vis_ratio}"
    sol = (
        f"1. Actual ratio: $\\frac{{55}}{{50}} = {actual_ratio}$ (Brand B is 10% larger).\n"
        f"2. Visual height ratio: $\\frac{{55 - 45}}{{50 - 45}} = \\frac{{10}}{{5}} = {vis_ratio:.1f}$ "
        f"(Brand B visually appears twice as large as Brand A!)."
    )
    return {
        "subskill": "07_calculate_actual_vs_visual_ratio_truncated_axis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.05,
        "marking_schema": [
            {"step": f"Actual ratio: 55/50 = {actual_ratio}", "marks": 1},
            {"step": f"Visual ratio: 10/5 = {vis_ratio}", "marks": 1},
        ],
        "hints": [
            "Actual ratio = 55 ÷ 50.",
            "Visual height = measured value − axis start value.",
        ],
        "misconception_tags": ["visual_vs_numerical_ratio_confusion"],
    }


# -----------------------------------------------------------------------------
# 08. Detect Non-Uniform Axis Scaling
# -----------------------------------------------------------------------------
def arch_08_detect_non_uniform_axis_scaling(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A chart displays sales over four years. The horizontal intervals are marked: "
        "2020, 2021, 2022, 2026, with equal physical spacing between each tick mark.\n"
        "Identify the deliberate flaw in this timeline display and explain how it misleads the reader."
    )
    concept = "The horizontal intervals are non-uniform: the gap between 2022 and 2026 is 4 years, but has the same physical width as 1-year intervals, making growth appear faster than it was."
    return {
        "subskill": "08_detect_non_uniform_axis_scaling",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Non-uniform horizontal scaling / irregular time intervals",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify non-uniform time interval (4-year gap drawn same size as 1-year gap)", "marks": 1},
            {"step": "Explain effect: distorts the apparent rate of change", "marks": 1},
        ],
        "hints": [
            "Check the difference between consecutive years on the horizontal axis.",
            "2022 to 2026 is a 4-year leap, while earlier gaps are 1 year each.",
        ],
        "misconception_tags": ["irregular_interval_misinterpretation"],
    }


# -----------------------------------------------------------------------------
# 09. Detect Pictogram Area/Volume Distortion
# -----------------------------------------------------------------------------
def arch_09_detect_pictogram_area_volume_distortion(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A company doubled its annual oil production from 10 000 barrels to 20 000 barrels. "
        "In a pictorial report, the artist doubled both the height AND the width of the oil barrel icon.\n"
        "1. By what factor did the **2D area** of the icon increase?\n"
        "2. Explain why this pictorial representation is mathematically misleading."
    )
    ans_str = "Area increased by a factor of 4 (quadrupled)"
    sol = (
        "1. When linear dimensions are doubled (scale factor $k = 2$), the area increases by $k^2 = 2^2 = 4$ times.\n"
        "2. Although production only doubled ($2\\times$), the visual area of the barrel quadrupled ($4\\times$), "
        "creating an exaggerated impression of growth."
    )
    return {
        "subskill": "09_detect_pictogram_area_volume_distortion",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Calculate area factor: 2^2 = 4 times", "marks": 1},
            {"step": "Explain that area quadrupled while data only doubled", "marks": 1},
        ],
        "hints": [
            "If height is multiplied by 2 and width is multiplied by 2, area = 2 × 2.",
            "The area of the image grows fourfold, misleading the visual reader.",
        ],
        "misconception_tags": ["pictogram_dimension_scaling_error"],
    }


# -----------------------------------------------------------------------------
# 10. Detect Omitted Baseline or Missing Scale
# -----------------------------------------------------------------------------
def arch_10_detect_omitted_baseline_or_scale_distortion(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A newspaper prints two bars comparing matric pass rates between School A and School B. "
        "There are no numbers, percentage labels, or tick marks on the vertical axis.\n"
        "Explain why this statistical presentation is invalid and cannot support a reliable conclusion."
    )
    concept = "Without numerical axis values or scale labels, the reader cannot determine the actual percentages, the baseline, or whether the difference is 0.1% or 50%."
    return {
        "subskill": "10_detect_omitted_baseline_or_scale_distortion",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Missing numerical scale and axis values",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify lack of numerical scale and labels", "marks": 1},
            {"step": "Explain that actual values and significance cannot be determined", "marks": 1},
        ],
        "hints": [
            "What information is missing from the axes?",
            "Without numbers or units, heights can represent anything.",
        ],
        "misconception_tags": ["omitted_scale_unnoticed"],
    }


# -----------------------------------------------------------------------------
# 11. Compare Two Groups Using Mean
# -----------------------------------------------------------------------------
def arch_11_compare_two_groups_using_mean(r: random.Random) -> Dict[str, Any]:
    # Group A: 5 scores
    base_a = r.randint(55, 65)
    scores_a = [base_a + r.randint(-8, 8) for _ in range(5)]
    mean_a = round(sum(scores_a) / 5, 1)

    base_b = base_a + r.randint(4, 9)
    scores_b = [base_b + r.randint(-8, 8) for _ in range(5)]
    mean_b = round(sum(scores_b) / 5, 1)

    diff = round(abs(mean_b - mean_a), 1)
    better_grp = "Group B" if mean_b > mean_a else "Group A"

    prompt = (
        f"Two Grade 9 mathematics classes wrote the same 100-mark test. The scores of 5 learners from each class are:\n"
        f"• Class A: {scores_a}\n"
        f"• Class B: {scores_b}\n\n"
        f"1. Calculate the mean score for Class A.\n"
        f"2. Calculate the mean score for Class B.\n"
        f"3. State which class performed better on average."
    )
    ans_str = f"Class A: {_fmt(mean_a)}; Class B: {_fmt(mean_b)}; Better: {better_grp}"
    sol = (
        f"1. $\\text{{Mean A}} = \\frac{{{sum(scores_a)}}}{{5}} = {_fmt(mean_a)}$\n"
        f"2. $\\text{{Mean B}} = \\frac{{{sum(scores_b)}}}{{5}} = {_fmt(mean_b)}$\n"
        f"3. {better_grp} performed better on average by {_fmt(diff)} marks."
    )
    return {
        "subskill": "11_compare_two_groups_using_mean",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.2,
        "marking_schema": [
            {"step": f"Mean A: {_fmt(mean_a)}", "marks": 1},
            {"step": f"Mean B: {_fmt(mean_b)}", "marks": 1},
            {"step": f"Conclusion: {better_grp}", "marks": 1},
        ],
        "hints": [
            "Mean = sum of scores ÷ number of scores.",
            f"Compare the two calculated means: {_fmt(mean_a)} vs {_fmt(mean_b)}.",
        ],
        "misconception_tags": ["mean_comparison_calculation_error"],
    }


# -----------------------------------------------------------------------------
# 12. Compare Two Groups Using Median
# -----------------------------------------------------------------------------
def arch_12_compare_two_groups_using_median(r: random.Random) -> Dict[str, Any]:
    scores_a = sorted([r.randint(40, 75) for _ in range(5)])
    scores_b = sorted([r.randint(50, 85) for _ in range(5)])
    med_a = scores_a[2]
    med_b = scores_b[2]

    higher_grp = "Group B" if med_b > med_a else ("Group A" if med_a > med_b else "Equal")

    prompt = (
        f"Two soccer teams recorded their goals scored across 5 matches (ordered from least to greatest):\n"
        f"• Team A: {scores_a}\n"
        f"• Team B: {scores_b}\n\n"
        f"1. Identify the median goals for Team A.\n"
        f"2. Identify the median goals for Team B.\n"
        f"3. Which team had the higher median?"
    )
    ans_str = f"Team A: {med_a}; Team B: {med_b}; Higher: {higher_grp}"
    sol = (
        f"For 5 ordered values, the median is the 3rd value:\n"
        f"• Team A Median: {med_a}\n"
        f"• Team B Median: {med_b}\n"
        f"Higher median: {higher_grp}."
    )
    return {
        "subskill": "12_compare_two_groups_using_median",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Team A median: {med_a}", "marks": 1},
            {"step": f"Team B median: {med_b}", "marks": 1},
            {"step": f"Comparison: {higher_grp}", "marks": 1},
        ],
        "hints": [
            "The data is already sorted. The median is the middle (3rd) number.",
            f"Team A median is {med_a}, Team B median is {med_b}.",
        ],
        "misconception_tags": ["median_positional_error"],
    }


# -----------------------------------------------------------------------------
# 13. Compare Two Groups Using Range (Consistency)
# -----------------------------------------------------------------------------
def arch_13_compare_two_groups_using_range(r: random.Random) -> Dict[str, Any]:
    # Consistent shooter: tight range
    min_a = r.randint(18, 22)
    max_a = min_a + r.randint(3, 6)
    range_a = max_a - min_a

    # Inconsistent shooter: wide range
    min_b = r.randint(10, 15)
    max_b = min_b + r.randint(15, 25)
    range_b = max_b - min_b

    prompt = (
        f"Two netball goal shooters scored points across several league games:\n"
        f"• Player A: Minimum = {min_a}, Maximum = {max_a}\n"
        f"• Player B: Minimum = {min_b}, Maximum = {max_b}\n\n"
        f"1. Calculate the range for Player A.\n"
        f"2. Calculate the range for Player B.\n"
        f"3. Which player is more consistent, and why?"
    )
    ans_str = f"Player A Range: {range_a}; Player B Range: {range_b}; More consistent: Player A"
    sol = (
        f"1. Player A Range = ${max_a} - {min_a} = {range_a}$\n"
        f"2. Player B Range = ${max_b} - {min_b} = {range_b}$\n"
        f"3. **Player A is more consistent** because a smaller range indicates less spread/variability in scoring."
    )
    return {
        "subskill": "13_compare_two_groups_using_range",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Player A Range: {range_a}", "marks": 1},
            {"step": f"Player B Range: {range_b}", "marks": 1},
            {"step": "Identify Player A as more consistent due to smaller range", "marks": 1},
        ],
        "hints": [
            "Range = Maximum − Minimum.",
            "A smaller range means scores are closer together, representing greater consistency.",
        ],
        "misconception_tags": ["consistency_range_inverse_misunderstanding"],
    }


# -----------------------------------------------------------------------------
# 14. Analyse Effect of High Outlier on Mean
# -----------------------------------------------------------------------------
def arch_14_analyse_effect_of_high_outlier_on_mean(r: random.Random) -> Dict[str, Any]:
    scores = [12, 14, 15, 16, 18]
    mean_orig = round(sum(scores) / 5, 1)  # 15.0
    outlier = 75
    scores_with_outlier = scores + [outlier]
    mean_new = round(sum(scores_with_outlier) / 6, 1)  # 25.0

    prompt = (
        f"A group of 5 workers earn daily tips of R12, R14, R15, R16, R18 (mean = R{_fmt(mean_orig)}).\n"
        f"A 6th worker joins who received a huge one-off bonus tip of R{outlier}.\n"
        f"1. Calculate the new mean tips for all 6 workers.\n"
        f"2. Explain how this extreme high value (outlier) affects the mean."
    )
    ans_str = f"New mean: R{_fmt(mean_new)}; Effect: Significantly increases the mean"
    sol = (
        f"1. New Mean = $\\frac{{12 + 14 + 15 + 16 + 18 + {outlier}}}{{6}} = \\frac{{{sum(scores_with_outlier)}}}{{6}} = \\text{{R}}{_fmt(mean_new)}$\n"
        f"2. The high outlier of R{outlier} drastically pulls the mean upward (from R{_fmt(mean_orig)} to R{_fmt(mean_new)}), "
        f"making it no longer representative of what most workers typically earn."
    )
    return {
        "subskill": "14_analyse_effect_of_high_outlier_on_mean",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.1,
        "marking_schema": [
            {"step": f"New mean: R{_fmt(mean_new)}", "marks": 1},
            {"step": "Explain that high outlier pulls the mean up", "marks": 1},
        ],
        "hints": [
            "Sum all 6 values and divide by 6.",
            "Compare the new mean to the typical values of 12 to 18.",
        ],
        "misconception_tags": ["outlier_mean_distortion_unrecognised"],
    }


# -----------------------------------------------------------------------------
# 15. Analyse Effect of Low Outlier on Mean
# -----------------------------------------------------------------------------
def arch_15_analyse_effect_of_low_outlier_on_mean(r: random.Random) -> Dict[str, Any]:
    scores = [70, 72, 75, 78, 80]
    mean_orig = round(sum(scores) / 5, 1)  # 75.0
    outlier = 5
    scores_with_outlier = scores + [outlier]
    mean_new = round(sum(scores_with_outlier) / 6, 1)  # 63.3

    prompt = (
        f"A learner scored {scores} across 5 term tests (mean = {_fmt(mean_orig)}%).\n"
        f"On the 6th test, the learner was ill and only managed {outlier}%.\n"
        f"1. Calculate the new mean test mark across all 6 tests.\n"
        f"2. Does the new mean accurately reflect the learner's normal performance? Explain."
    )
    ans_str = f"New mean: {_fmt(mean_new)}%; Does not reflect normal performance"
    sol = (
        f"1. New Mean = $\\frac{{{sum(scores_with_outlier)}}}{{6}} = {_fmt(mean_new)}\\%$\n"
        f"2. No. The extreme low mark of {outlier}% heavily depresses the mean to {_fmt(mean_new)}%, "
        f"even though all other tests were 70% or higher."
    )
    return {
        "subskill": "15_analyse_effect_of_low_outlier_on_mean",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.2,
        "marking_schema": [
            {"step": f"New mean calculation: {_fmt(mean_new)}%", "marks": 1},
            {"step": "Explain that extreme low value distorts true average ability", "marks": 1},
        ],
        "hints": [
            "Add the 5% score to the sum and divide by 6.",
            "Notice how one single bad day drops the entire average mark.",
        ],
        "misconception_tags": ["low_outlier_depression_error"],
    }


# -----------------------------------------------------------------------------
# 16. Resistance of Median to Extreme Outliers
# -----------------------------------------------------------------------------
def arch_16_resistance_of_median_to_extreme_outliers(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider this ordered dataset of 5 monthly rents in a township: R1 200, R1 500, R1 800, R2 000, R2 500.\n"
        "The median rent is R1 800.\n"
        "If a luxury mansion renting for R50 000 per month is added to the list, what is the new median rent?"
    )
    # New list: 1200, 1500, 1800, 2000, 2500, 50000 -> median = (1800 + 2000) / 2 = 1900
    ans_str = "R1 900"
    sol = (
        "New ordered list: R1 200, R1 500, **R1 800**, **R2 000**, R2 500, R50 000.\n"
        "With 6 items, the median is the average of the 3rd and 4th values:\n"
        "$$\\text{Median} = \\frac{1800 + 2000}{2} = \\text{R}1\\,900$$\n"
        "Notice that while the mean jumped enormously, the median barely changed from R1 800 to R1 900. "
        "The median is **resistant (robust) to extreme outliers**."
    )
    return {
        "subskill": "16_resistance_of_median_to_extreme_outliers",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify 3rd and 4th terms: 1800 and 2000", "marks": 1},
            {"step": "Calculate median: (1800 + 2000)/2 = R1 900", "marks": 1},
        ],
        "hints": [
            "List the 6 values in ascending order.",
            "Average the 3rd and 4th numbers: (1 800 + 2 000) ÷ 2.",
        ],
        "misconception_tags": ["median_resistance_property_unrecognised"],
    }


# -----------------------------------------------------------------------------
# 17. Choose Appropriate Measure for Skewed Income
# -----------------------------------------------------------------------------
def arch_17_choose_appropriate_measure_for_skewed_income(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a small company of 10 employees, 9 factory workers earn R8 000 per month, "
        "while the CEO earns R200 000 per month.\n"
        "1. Which measure of central tendency (mean, median, or mode) best describes a typical worker's income?\n"
        "2. Explain why the mean is misleading in this situation."
    )
    concept = "Median (or mode); the mean is heavily skewed upward by the CEO's R200 000 salary, giving a false impression that a typical employee earns over R27 000."
    return {
        "subskill": "17_choose_appropriate_measure_for_skewed_income",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Median (or Mode)",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State Median (or Mode)", "marks": 1},
            {"step": "Explain that mean is skewed upward by the extreme CEO salary", "marks": 1},
        ],
        "hints": [
            "Calculate what the mean would be: (9 × 8000 + 200000) ÷ 10 = R27 200.",
            "Does any factory worker earn anywhere near R27 200? No.",
        ],
        "misconception_tags": ["mean_chosen_for_skewed_distribution"],
    }


# -----------------------------------------------------------------------------
# 18. Choose Appropriate Measure for Symmetric Test Scores
# -----------------------------------------------------------------------------
def arch_18_choose_appropriate_measure_for_symmetric_test_scores(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A class of 30 learners writes a standardised test. The marks are normally distributed "
        "and form a symmetric bell curve with no extreme outliers.\n"
        "Which measure of central tendency is generally preferred when data is symmetric without outliers, and why?"
    )
    concept = "The mean is preferred because it takes into account every single mark in the dataset and has strong mathematical properties when data is symmetric."
    return {
        "subskill": "18_choose_appropriate_measure_for_symmetric_test_scores",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Mean",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify Mean", "marks": 1},
            {"step": "Explain that mean uses all data points and is reliable for symmetric distributions", "marks": 1},
        ],
        "hints": [
            "When there are no extreme outliers, which average utilizes every single numerical value?",
            "The mean is the standard statistical measure for symmetric distributions.",
        ],
        "misconception_tags": ["measure_preference_rationale_confusion"],
    }


# -----------------------------------------------------------------------------
# 19. Determine Mode Importance for Inventory Ordering
# -----------------------------------------------------------------------------
def arch_19_determine_mode_importance_for_inventory_ordering(r: random.Random) -> Dict[str, Any]:
    sizes = [5, 6, 7, 7, 7, 7, 8, 9, 10]
    prompt = (
        f"A shoe store manager records the shoe sizes sold yesterday: {sizes}.\n"
        f"1. Identify the mode of this dataset.\n"
        f"2. Explain why the manager would find the **mode** much more useful than the mean when re-ordering stock."
    )
    ans_str = "Mode: 7"
    sol = (
        "1. **Mode = 7** (size 7 occurred 4 times, which is the highest frequency).\n"
        "2. The manager needs to order the most popular physical shoe size that customers buy. "
        "A mean shoe size (e.g. 7,3) does not exist in store inventory, whereas the mode identifies the exact stock item in highest demand."
    )
    return {
        "subskill": "19_determine_mode_importance_for_inventory_ordering",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify Mode = 7", "marks": 1},
            {"step": "Explain relevance to inventory ordering (shoe sizes must be discrete integers)", "marks": 1},
        ],
        "hints": [
            "Which shoe size occurs most often?",
            "Can a shoe store order size 7,3? No, shoes are manufactured in discrete integer sizes.",
        ],
        "misconception_tags": ["mode_practical_application_unrecognised"],
    }


# -----------------------------------------------------------------------------
# 20. Critique Graph with Missing Sample Size
# -----------------------------------------------------------------------------
def arch_20_critique_graph_with_missing_sample_size(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "An advertisement claims '75% of doctors recommend Brand X headache pills' accompanied by a pie chart "
        "showing a 75% sector. However, the advertisement does not state how many doctors were surveyed ($N$).\n"
        "Why is omitting the sample size $N$ considered statistically deceptive?"
    )
    concept = "If only 4 doctors were surveyed and 3 recommended it, 75% is technically true but statistically meaningless. Omitting N conceals whether the sample is large enough to be reliable."
    return {
        "subskill": "20_critique_graph_with_missing_sample_size",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Omitting sample size conceals statistical unreliability",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that percentage depends on sample size N", "marks": 1},
            {"step": "Explain that 75% of 4 doctors is meaningless compared to 75% of 1 000 doctors", "marks": 1},
        ],
        "hints": [
            "What if N = 4? Then 3 out of 4 is 75%.",
            "Without N, readers cannot judge whether the evidence is robust.",
        ],
        "misconception_tags": ["sample_size_omission_bias"],
    }


# -----------------------------------------------------------------------------
# 21. Critique Claim Confusing Correlation with Causation
# -----------------------------------------------------------------------------
def arch_21_critique_claim_confusing_correlation_with_causation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A study observes that towns with higher ice cream sales also report higher numbers of swimming pool drownings. "
        "A journalist headlines: 'Eating ice cream causes people to drown!'\n"
        "1. Identify the logical fallacy in the journalist's conclusion.\n"
        "2. Suggest a third (confounding) variable that explains both high ice cream sales and swimming drownings."
    )
    concept = "Correlation does not imply causation. The confounding variable is hot summer weather (heat causes more people to buy ice cream AND more people to swim, leading to drownings)."
    return {
        "subskill": "21_critique_claim_confusing_correlation_with_causation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Correlation does not equal causation; Summer heat is confounding factor",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify correlation != causation fallacy", "marks": 1},
            {"step": "Identify hot weather / summer temperature as confounding variable", "marks": 1},
        ],
        "hints": [
            "Just because two variables rise together does not mean one caused the other.",
            "What seasonal factor increases both ice cream eating and swimming?",
        ],
        "misconception_tags": ["correlation_implies_causation_fallacy"],
    }


# -----------------------------------------------------------------------------
# 22. Interpret Trend and Predict Next Period
# -----------------------------------------------------------------------------
def arch_22_interpret_trend_and_predict_next_period(r: random.Random) -> Dict[str, Any]:
    years = [2021, 2022, 2023, 2024]
    base = r.randint(120, 160)
    inc = r.randint(15, 25)
    counts = [base + i * inc for i in range(4)]
    next_val = base + 4 * inc

    prompt = (
        f"A community library recorded annual registrations over 4 consecutive years:\n"
        f"• 2021: {counts[0]} members\n"
        f"• 2022: {counts[1]} members\n"
        f"• 2023: {counts[2]} members\n"
        f"• 2024: {counts[3]} members\n\n"
        f"1. Describe the trend in library registrations.\n"
        f"2. Assuming this constant rate of growth continues, predict the registrations for **2025**."
    )
    ans_str = f"Trend: Upward (increasing by {inc} per year); 2025: {next_val}"
    sol = (
        f"1. **Trend**: Upward / positive linear trend, increasing by exactly ${inc}$ members each year.\n"
        f"2. **Prediction for 2025**: ${counts[3]} + {inc} = {next_val}$ members."
    )
    return {
        "subskill": "22_interpret_trend_and_predict_next_period",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(next_val),
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify annual increase of {inc}", "marks": 1},
            {"step": f"Predict 2025: {next_val}", "marks": 1},
        ],
        "hints": [
            f"Find the constant difference between successive years: {counts[1]} − {counts[0]}.",
            f"Add {inc} to the 2024 total ({counts[3]}).",
        ],
        "misconception_tags": ["linear_trend_prediction_error"],
    }


# -----------------------------------------------------------------------------
# 23. Compare Spread and Consistency Between Two Athletes
# -----------------------------------------------------------------------------
def arch_23_compare_spread_consistency_between_two_athletes(r: random.Random) -> Dict[str, Any]:
    times_a = [10.8, 10.9, 11.0, 11.1, 11.2]
    times_b = [10.2, 10.6, 11.0, 11.4, 11.8]
    range_a = round(times_a[-1] - times_a[0], 1)  # 0.4
    range_b = round(times_b[-1] - times_b[0], 1)  # 1.6

    prompt = (
        f"Two 100m sprinters recorded their times (in seconds) over 5 races:\n"
        f"• Athlete A: {times_a} (Mean = 11,0s)\n"
        f"• Athlete B: {times_b} (Mean = 11,0s)\n\n"
        f"1. Calculate the range of times for Athlete A.\n"
        f"2. Calculate the range of times for Athlete B.\n"
        f"3. Both athletes have the exact same mean (11,0s). Which athlete is more dependable/consistent for a relay team, and why?"
    )
    ans_str = f"Athlete A Range: {_fmt(range_a)}s; Athlete B Range: {_fmt(range_b)}s; Athlete A is more consistent"
    sol = (
        f"1. Range A = $11,2 - 10,8 = {_fmt(range_a)}\\text{{s}}$\n"
        f"2. Range B = $11,8 - 10,2 = {_fmt(range_b)}\\text{{s}}$\n"
        f"3. **Athlete A is more dependable** because their range ({_fmt(range_a)}s) is much smaller, "
        f"meaning their race times show far less variation."
    )
    return {
        "subskill": "23_compare_spread_consistency_between_two_athletes",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.05,
        "marking_schema": [
            {"step": f"Athlete A range: {_fmt(range_a)}s", "marks": 1},
            {"step": f"Athlete B range: {_fmt(range_b)}s", "marks": 1},
            {"step": "Select Athlete A based on smaller range/variability", "marks": 1},
        ],
        "hints": [
            "Range = Maximum − Minimum.",
            "Lower range indicates tighter performance and higher predictability.",
        ],
        "misconception_tags": ["range_interpretation_in_real_world_context"],
    }


# -----------------------------------------------------------------------------
# 24. Compare Pass Rates Between Two Classes
# -----------------------------------------------------------------------------
def arch_24_compare_pass_rates_between_two_classes(r: random.Random) -> Dict[str, Any]:
    n_a = 40
    pass_a = 32
    pct_a = round((pass_a / n_a) * 100, 1)  # 80.0%

    n_b = 25
    pass_b = 22
    pct_b = round((pass_b / n_b) * 100, 1)  # 88.0%

    prompt = (
        f"Two Grade 9 classes wrote the Term 4 exam:\n"
        f"• Class 9A: {pass_a} out of {n_a} learners passed.\n"
        f"• Class 9B: {pass_b} out of {n_b} learners passed.\n\n"
        f"1. Calculate the pass percentage for Class 9A.\n"
        f"2. Calculate the pass percentage for Class 9B.\n"
        f"3. A teacher says: 'Class 9A did better because 32 passed compared to only 22 in Class 9B.' "
        f"Explain why this statement is mathematically flawed."
    )
    ans_str = f"Class 9A: {_fmt(pct_a)}%; Class 9B: {_fmt(pct_b)}%; Comparison flawed because class sizes differ"
    sol = (
        f"1. Class 9A: $\\frac{{{pass_a}}}{{{n_a}}} \\times 100\\% = {_fmt(pct_a)}\\%$\n"
        f"2. Class 9B: $\\frac{{{pass_b}}}{{{n_b}}} \\times 100\\% = {_fmt(pct_b)}\\%$\n"
        f"3. The teacher's statement ignores the different class totals. Comparing absolute counts is misleading "
        f"when total sample sizes differ; proportionally, Class 9B achieved a higher success rate ({_fmt(pct_b)}% vs {_fmt(pct_a)}%)."
    )
    return {
        "subskill": "24_compare_pass_rates_between_two_classes",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.1,
        "marking_schema": [
            {"step": f"Class 9A percentage: {_fmt(pct_a)}%", "marks": 1},
            {"step": f"Class 9B percentage: {_fmt(pct_b)}%", "marks": 1},
            {"step": "Explain that relative percentage must be used when base sizes differ", "marks": 1},
        ],
        "hints": [
            f"Divide {pass_a} by {n_a} and multiply by 100.",
            f"Divide {pass_b} by {n_b} and multiply by 100.",
        ],
        "misconception_tags": ["absolute_count_vs_relative_frequency_error"],
    }


# -----------------------------------------------------------------------------
# 25. Identify Modal Category from Survey Summary
# -----------------------------------------------------------------------------
def arch_25_identify_modal_category_from_survey_summary(r: random.Random) -> Dict[str, Any]:
    categories = ["Minibus Taxi", "Walking", "Train", "Bicycle", "Private Car"]
    counts = [142, 98, 45, 12, 63]
    r.shuffle(categories)

    data_summary = "\n".join([f"• {c}: {n}" for c, n in zip(categories, counts)])
    mode_cat = categories[0]
    mode_count = counts[0]
    for c, n in zip(categories, counts):
        if n > mode_count:
            mode_cat = c
            mode_count = n

    prompt = (
        f"A transport survey asked 360 commuters how they travel to work each morning:\n"
        f"{data_summary}\n\n"
        f"1. Identify the **modal category** of transport.\n"
        f"2. Explain what the modal category tells the city transport planner."
    )
    ans_str = f"Modal category: {mode_cat}"
    sol = (
        f"1. **Modal category = {mode_cat}** with {mode_count} commuters (the highest frequency).\n"
        f"2. It informs the transport planner that {mode_cat} is the single most widely used transit mode, "
        f"so infrastructure and safety improvements should prioritize this sector."
    )
    return {
        "subskill": "25_identify_modal_category_from_survey_summary",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": mode_cat,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify {mode_cat}", "marks": 1},
            {"step": "Explain that it represents the most frequent transit mode", "marks": 1},
        ],
        "hints": [
            "The modal category is the category with the highest frequency.",
            f"Look for the largest number in the list: {mode_count}.",
        ],
        "misconception_tags": ["modal_category_identification_error"],
    }
