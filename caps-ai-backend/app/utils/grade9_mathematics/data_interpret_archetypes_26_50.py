"""Grade 9 Mathematics - Interpret, Analyse and Report on Data Archetypes 26-50 (CAPS Term 4).
Focus: Misleading statistics, extrapolation risks, confounding variables, sample size scaling,
mean/median adjustments, linear transformations of data, and formal reporting synthesis.
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
# 26. Evaluate Representativeness of School Tuckshop Sample
# -----------------------------------------------------------------------------
def arch_26_evaluate_representativeness_of_school_tuckshop_sample(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A student council rep surveys 30 Grade 9 learners standing in the tuckshop queue on Friday about "
        "whether cold drinks should be sold on campus. 28 say 'Yes'.\n"
        "Explain two reasons why this sample does NOT represent all 1 000 learners at the school."
    )
    concept = "1. Grade bias: Only Grade 9s were surveyed, excluding Grades 8, 10, 11, and 12. 2. Self-selection / location bias: Tuckshop customers are already buying snacks/drinks, excluding learners who bring food from home."
    return {
        "subskill": "26_evaluate_representativeness_of_school_tuckshop_sample",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Grade bias and location self-selection bias",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify grade restriction (Grade 9 only)", "marks": 1},
            {"step": "Identify location bias (tuckshop customers only)", "marks": 1},
        ],
        "hints": [
            "Are all grades (Grades 8 to 12) represented in this sample?",
            "Do learners who pack lunch from home queue at the tuckshop?",
        ],
        "misconception_tags": ["representativeness_flaw_unrecognised"],
    }


# -----------------------------------------------------------------------------
# 27. Evaluate Representativeness of Online Social Media Poll
# -----------------------------------------------------------------------------
def arch_27_evaluate_representativeness_of_online_poll(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A local municipal councillor runs a poll on Instagram asking whether property taxes should increase "
        "to fund road repairs. 90% of respondents vote 'No'.\n"
        "Explain why this Instagram poll is not representative of all registered municipal voters."
    )
    concept = "Instagram users skew heavily toward younger demographics who may not be property owners; also, citizens without smartphones or internet access are completely excluded."
    return {
        "subskill": "27_evaluate_representativeness_of_online_poll",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Digital exclusion and age demographic bias",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify demographic bias (younger app users vs rate-paying homeowners)", "marks": 1},
            {"step": "Identify digital exclusion (those without internet access excluded)", "marks": 1},
        ],
        "hints": [
            "Who uses Instagram most often, and do they own taxable property?",
            "Are elderly residents or underprivileged households with no internet included?",
        ],
        "misconception_tags": ["online_poll_generalisation_error"],
    }


# -----------------------------------------------------------------------------
# 28. Detect Suppression of Negative Data in Report
# -----------------------------------------------------------------------------
def arch_28_detect_suppression_of_negative_data_in_report(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A cell phone provider advertises: 'Our network delivered 99% uptime in Sandton last month!' "
        "However, they fail to mention that network uptime was below 70% in three neighbouring townships.\n"
        "Identify the statistical reporting manipulation used here (cherry-picking data)."
    )
    concept = "Selective reporting or cherry-picking: reporting only favorable data from one specific wealthy area while omitting poor results from other service areas."
    return {
        "subskill": "28_detect_suppression_of_negative_data_in_report",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Selective reporting / cherry-picking favorable data",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify cherry-picking / selective reporting", "marks": 1},
            {"step": "Explain that suppressing unfavourable data gives a false general impression", "marks": 1},
        ],
        "hints": [
            "What happened to the data from the other areas?",
            "Highlighting only the best result while hiding the rest is called cherry-picking.",
        ],
        "misconception_tags": ["cherry_picking_bias_unnoticed"],
    }


# -----------------------------------------------------------------------------
# 29. Calculate Percentage Increase Misleadingly Reported
# -----------------------------------------------------------------------------
def arch_29_calculate_percentage_increase_misleadingly_reported(r: random.Random) -> Dict[str, Any]:
    # Incidence from 1 per 10 000 to 2 per 10 000
    prompt = (
        "A tabloid headline screams: 'Risk of rare disease increases by 100%!' "
        "In reality, the incidence rose from 1 in 10 000 people to 2 in 10 000 people.\n"
        "1. Calculate the absolute increase in risk per person (as a decimal or fraction).\n"
        "2. Explain why reporting '100% increase' creates unwarranted panic."
    )
    ans_str = "Absolute increase: 1 in 10 000 (0,0001 or 0,01%)"
    sol = (
        "1. Absolute increase: $\\frac{2}{10\\,000} - \\frac{1}{10\\,000} = \\frac{1}{10\\,000} = 0,01\\%$.\n"
        "2. Relative increase is 100% because 2 is double 1, but the absolute probability remains extremely tiny (0,02%). "
        "Presenting relative risk without absolute context sensationalises negligible differences."
    )
    return {
        "subskill": "29_calculate_percentage_increase_misleadingly_reported",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State absolute risk increase of 1 in 10 000 (0,01%)", "marks": 1},
            {"step": "Explain difference between relative risk and absolute baseline", "marks": 1},
        ],
        "hints": [
            "What is the difference between 2/10 000 and 1/10 000?",
            "Although 2 is double 1, both numbers are virtually zero.",
        ],
        "misconception_tags": ["relative_vs_absolute_risk_confusion"],
    }


# -----------------------------------------------------------------------------
# 30. Absolute vs Relative Change Interpretation
# -----------------------------------------------------------------------------
def arch_30_absolute_vs_relative_change_interpretation(r: random.Random) -> Dict[str, Any]:
    old_p = 5.0
    new_p = 10.0
    abs_change = new_p - old_p  # 5 percentage points
    rel_change = round(((new_p - old_p) / old_p) * 100)  # 100%

    prompt = (
        f"A municipal unemployment rate rises from {int(old_p)}% to {int(new_p)}%.\n"
        f"1. State the **percentage point increase**.\n"
        f"2. Calculate the **percentage increase** relative to the original rate."
    )
    ans_str = f"Percentage points: {int(abs_change)} points; Percentage increase: {rel_change}%"
    sol = (
        f"1. Percentage point change: ${int(new_p)}\\% - {int(old_p)}\\% = {int(abs_change)}\\text{{ percentage points}}$.\n"
        f"2. Percentage increase: $\\frac{{{int(new_p)} - {int(old_p)}}}{{{int(old_p)}}} \\times 100\\% = \\frac{{{int(abs_change)}}}{{{int(old_p)}}} \\times 100\\% = {rel_change}\\%$."
    )
    return {
        "subskill": "30_absolute_vs_relative_change_interpretation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Percentage points: {int(abs_change)}", "marks": 1},
            {"step": f"Relative percentage increase: {rel_change}%", "marks": 1},
        ],
        "hints": [
            "Percentage points = simply subtract the two percentage values.",
            "Percentage increase = (Change ÷ Original) × 100.",
        ],
        "misconception_tags": ["percentage_points_vs_percentage_increase"],
    }


# -----------------------------------------------------------------------------
# 31. Continuous Trend and Extrapolation Risk
# -----------------------------------------------------------------------------
def arch_31_distinguish_between_continuous_trend_and_extrapolation_risk(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A toddler grew from 75 cm at age 1 to 87 cm at age 2 (gaining 12 cm per year). "
        "A family member calculates: 'At this rate of 12 cm per year, by age 30 she will be 435 cm tall!'\n"
        "Explain the statistical error known as **extrapolation** and why it produces absurd results here."
    )
    concept = "Extrapolation assumes that a trend observed over a short, specific range (ages 1–2) will continue indefinitely into conditions where the underlying biology changes (human growth stops after adolescence)."
    return {
        "subskill": "31_distinguish_between_continuous_trend_and_extrapolation_risk",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Unwarranted extrapolation beyond observed data domain",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify extrapolation beyond observed range", "marks": 1},
            {"step": "Explain that biological growth rates slow down and stop", "marks": 1},
        ],
        "hints": [
            "Extrapolation means predicting far beyond the recorded data points.",
            "Do humans grow at a constant speed forever?",
        ],
        "misconception_tags": ["extrapolation_validity_fallacy"],
    }


# -----------------------------------------------------------------------------
# 32. Identify Confounding Variable in Health Claim
# -----------------------------------------------------------------------------
def arch_32_identify_confounding_variable_in_health_claim(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A study reports that people who sleep with their shoes on are significantly more likely "
        "to wake up with a severe headache. A student claims that wearing shoes in bed causes headaches.\n"
        "Identify the real underlying confounding factor that explains both going to bed with shoes on and waking up with a headache."
    )
    concept = "Going to bed intoxicated (alcohol consumption). Heavy drinking leads to collapsing in bed fully clothed/shod, and also causes a dehydration hangover headache the next morning."
    return {
        "subskill": "32_identify_confounding_variable_in_health_claim",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Alcohol intoxication / hangover",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify confounding variable (intoxication / exhaustion / illness)", "marks": 1},
            {"step": "Explain that confounding variable causes both phenomena", "marks": 1},
        ],
        "hints": [
            "What state makes someone forget to take off their shoes before sleeping?",
            "That same state causes dehydration and a headache next morning.",
        ],
        "misconception_tags": ["third_variable_omission_error"],
    }


# -----------------------------------------------------------------------------
# 33. Compare Bimodal Distribution Interpretations
# -----------------------------------------------------------------------------
def arch_33_compare_bimodal_distribution_interpretations(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a physics test, test marks show two distinct peaks: one cluster around 35% and another cluster around 85%, "
        "with very few marks in between. The calculated mean mark is 60%.\n"
        "Explain why reporting the single mean mark of 60% is misleading for this **bimodal distribution**."
    )
    concept = "Almost no learner actually scored 60%. The bimodal distribution reveals two distinct sub-populations (learners who mastered the material vs learners who struggled completely). A single mean masks this critical split."
    return {
        "subskill": "33_compare_bimodal_distribution_interpretations",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Mean masks two distinct performance groups in bimodal data",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that data is bimodal (two separate clusters)", "marks": 1},
            {"step": "Explain that 60% represents neither group accurately", "marks": 1},
        ],
        "hints": [
            "Did anyone actually score 60%?",
            "The class is divided into two distinct groups, which the average hides.",
        ],
        "misconception_tags": ["bimodal_mean_sufficiency_misconception"],
    }


# -----------------------------------------------------------------------------
# 34. Assess Impact of Changing Class Intervals on Histogram Shape
# -----------------------------------------------------------------------------
def arch_34_assess_impact_of_changing_class_intervals_on_histogram_shape(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A researcher groups 50 test marks into very wide class intervals: 0–49% and 50–100% (only 2 intervals).\n"
        "Explain how using class intervals that are too wide conceals important details in data analysis."
    )
    concept = "Excessively wide intervals obscure the distribution's shape, spread, modal peaks, and clusters, reducing nuanced continuous data to a crude binary split."
    return {
        "subskill": "34_assess_impact_of_changing_class_intervals_on_histogram_shape",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Wide intervals obscure distribution details and skewness",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that data distribution shape and peaks are lost", "marks": 1},
            {"step": "Explain that optimal interval widths balance summary with detail", "marks": 1},
        ],
        "hints": [
            "Can you tell if learners scored 55% or 95% within the 50–100% interval?",
            "Information about variation and spread is lost.",
        ],
        "misconception_tags": ["class_interval_resolution_blindness"],
    }


# -----------------------------------------------------------------------------
# 35. Compare Two Teams Performance Using Median and Range
# -----------------------------------------------------------------------------
def arch_35_compare_two_teams_performance_using_median_and_range(r: random.Random) -> Dict[str, Any]:
    # Team Alpha: median 72, range 15
    # Team Beta: median 72, range 40
    prompt = (
        "Two cricket teams have their batting run totals analyzed over 10 matches:\n"
        "• Lions: Median = 180 runs, Range = 25 runs\n"
        "• Tigers: Median = 180 runs, Range = 110 runs\n\n"
        "1. Compare their typical performance using the median.\n"
        "2. Compare their consistency using the range.\n"
        "3. Which team is more predictable, and why?"
    )
    ans_str = "Equal median (180); Lions much more consistent (range 25 vs 110); Lions are more predictable"
    sol = (
        "1. **Typical Performance**: Both teams have the identical median of 180 runs, meaning their average/midpoint scores are equal.\n"
        "2. **Consistency**: The Lions have a much smaller range (25 runs vs 110 runs for Tigers), showing far less variation.\n"
        "3. **Predictability**: **Lions** are more predictable because their scores cluster tightly within a 25-run band."
    )
    return {
        "subskill": "35_compare_two_teams_performance_using_median_and_range",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State medians are equal", "marks": 1},
            {"step": "Identify Lions have smaller range and higher consistency", "marks": 1},
            {"step": "Select Lions as more predictable", "marks": 1},
        ],
        "hints": [
            "Look at the medians: both are 180.",
            "Compare ranges: 25 vs 110. Smaller range = more consistent.",
        ],
        "misconception_tags": ["dual_statistic_comparison_confusion"],
    }


# -----------------------------------------------------------------------------
# 36. Evaluate Conclusion Drawn from Biased Phone Survey
# -----------------------------------------------------------------------------
def arch_36_evaluate_conclusion_drawn_from_biased_phone_survey(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A radio station conducts a live call-in poll during work hours on a Tuesday afternoon asking listeners: "
        "'Do you support introducing a 4-day working week?' 92% of callers answer 'Yes'.\n"
        "Explain why this conclusion cannot be applied to the working population as a whole."
    )
    concept = "People working regular full-time jobs are at work and cannot listen or call in during Tuesday afternoon hours. The sample over-represents unemployed, shift workers, or retirees."
    return {
        "subskill": "36_evaluate_conclusion_drawn_from_biased_phone_survey",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Time-of-day sampling bias excludes full-time workers",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify daytime timing bias", "marks": 1},
            {"step": "Explain that working individuals are unable to participate", "marks": 1},
        ],
        "hints": [
            "Who has time to listen to the radio and call in on a Tuesday afternoon?",
            "Most full-time employees are busy working at that time.",
        ],
        "misconception_tags": ["time_of_day_sampling_bias"],
    }


# -----------------------------------------------------------------------------
# 37. Identify Circular Reasoning or Unsubstantiated Claim
# -----------------------------------------------------------------------------
def arch_37_identify_circular_reasoning_or_unsubstantiated_claim(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "An energy drink company states in a report: 'Energy Boost is the best energy drink because it has superior "
        "ingredients, and we know its ingredients are superior because it is the best energy drink.'\n"
        "Identify the logical reasoning fallacy demonstrated in this argument."
    )
    return {
        "subskill": "37_identify_circular_reasoning_or_unsubstantiated_claim",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Circular reasoning (begging the question)",
        "sample_answer": "Circular reasoning: the conclusion is used to justify the premise without independent empirical evidence.",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify circular reasoning / begging the question", "marks": 1},
            {"step": "Note the absence of independent empirical evidence", "marks": 1},
        ],
        "hints": [
            "The argument goes in a loop without proving anything.",
            "This is known as circular reasoning.",
        ],
        "misconception_tags": ["circular_reasoning_fallacy"],
    }


# -----------------------------------------------------------------------------
# 38. Interpret Effect of Doubling Sample Size on Reliability
# -----------------------------------------------------------------------------
def arch_38_interpret_effect_of_doubling_sample_size_on_reliability(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A political pollster increases their random sample size from 500 voters to 2 000 voters.\n"
        "Explain how increasing the sample size affects the **margin of error** and the **reliability** of the survey results."
    )
    concept = "A larger random sample reduces random sampling error and narrows the margin of error, making sample statistics more reliable estimates of the true population parameters."
    return {
        "subskill": "38_interpret_effect_of_doubling_sample_size_on_reliability",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Reduces margin of error and increases reliability",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that margin of error decreases", "marks": 1},
            {"step": "State that reliability / precision of estimate increases", "marks": 1},
        ],
        "hints": [
            "As sample size grows, does random error increase or decrease?",
            "Larger samples provide a closer reflection of the overall population.",
        ],
        "misconception_tags": ["sample_size_precision_inverse_misunderstanding"],
    }


# -----------------------------------------------------------------------------
# 39. Critique Marketing Claim: 9 Out of 10 Dentists
# -----------------------------------------------------------------------------
def arch_39_critique_marketing_claim_based_on_9_out_of_10_dentists(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A toothpaste advert says: '9 out of 10 dentists recommend Sparkle Paste!'\n"
        "An investigation reveals dentists were asked to recommend *several* acceptable toothpastes, "
        "and 90% included Sparkle Paste on their list of 6 approved brands.\n"
        "Explain how the wording of the advert misleads the public into thinking dentists chose Sparkle Paste *above all other brands*."
    )
    concept = "The advertisement implies exclusivity (that Sparkle Paste was preferred over competitors), whereas dentists simply agreed it was one of many acceptable fluoride toothpastes."
    return {
        "subskill": "39_critique_marketing_claim_based_on_9_out_of_10_dentists",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Implies exclusive preference when question allowed multiple selections",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify false implication of exclusive preference", "marks": 1},
            {"step": "Explain that dentists merely listed it alongside other brands", "marks": 1},
        ],
        "hints": [
            "Did the dentists choose Sparkle Paste as their favourite brand?",
            "No, it was just one of many acceptable options checked off.",
        ],
        "misconception_tags": ["multi_selection_recommendation_distortion"],
    }


# -----------------------------------------------------------------------------
# 40. Identify Non-Response Bias
# -----------------------------------------------------------------------------
def arch_40_identify_omission_of_non_respondents_non_response_bias(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A hospital sends satisfaction questionnaires to 1 000 discharged patients. Only 80 patients reply, "
        "and 72 of them report being dissatisfied.\n"
        "Explain the concept of **non-response bias** and why concluding that 90% of all hospital patients were unhappy is flawed."
    )
    concept = "Dissatisfied patients are strongly motivated to vent complaints, whereas the 920 satisfied or neutral patients did not bother filling in the form. The non-respondents may have had completely different experiences."
    return {
        "subskill": "40_identify_omission_of_non_respondents_non_response_bias",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Non-response bias: unhappy patients are more motivated to reply",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Define non-response bias (low response rate 8%)", "marks": 1},
            {"step": "Explain that non-respondents likely had different (more satisfied) experiences", "marks": 1},
        ],
        "hints": [
            "What percentage of patients actually replied? (80 ÷ 1 000 = 8%).",
            "People who had a normal, peaceful stay rarely fill out complaint surveys.",
        ],
        "misconception_tags": ["non_response_bias_ignored"],
    }


# -----------------------------------------------------------------------------
# 41. Recalculate Mean After Correcting Data Entry Error
# -----------------------------------------------------------------------------
def arch_41_recalculate_mean_after_removing_data_entry_error(r: random.Random) -> Dict[str, Any]:
    # 5 test marks reported with mean 64. One mark entered as 90 was actually 50.
    n = 5
    old_mean = 64.0
    old_sum = old_mean * n  # 320
    err_val = 90
    corr_val = 50
    new_sum = old_sum - err_val + corr_val  # 320 - 90 + 50 = 280
    new_mean = round(new_sum / n, 1)  # 56.0

    prompt = (
        f"A teacher calculated the mean mark of 5 learners to be {int(old_mean)}%.\n"
        f"She then discovered a recording error: a mark entered as {err_val}% was actually {corr_val}%.\n"
        f"Calculate the correct mean mark for the 5 learners."
    )
    ans_str = f"{_fmt(new_mean)}%"
    sol = (
        f"1. Original Sum = $5 \\times {int(old_mean)} = {int(old_sum)}$\n"
        f"2. Corrected Sum = ${int(old_sum)} - {err_val} + {corr_val} = {int(new_sum)}$\n"
        f"3. Corrected Mean = $\\frac{{{int(new_sum)}}}{{5}} = {_fmt(new_mean)}\\%$"
    )
    return {
        "subskill": "41_recalculate_mean_after_removing_data_entry_error",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.1,
        "marking_schema": [
            {"step": f"Calculate original total: {int(old_sum)}", "marks": 1},
            {"step": f"Adjust total: {int(new_sum)}", "marks": 1},
            {"step": f"Calculate new mean: {_fmt(new_mean)}%", "marks": 1},
        ],
        "hints": [
            f"Find the original total sum: 5 × {int(old_mean)} = {int(old_sum)}.",
            f"Subtract {err_val}, add {corr_val}, and divide by 5.",
        ],
        "misconception_tags": ["mean_recalculation_sum_error"],
    }


# -----------------------------------------------------------------------------
# 42. Recalculate Median After Adding New Learner Score
# -----------------------------------------------------------------------------
def arch_42_recalculate_median_after_adding_new_learner_score(r: random.Random) -> Dict[str, Any]:
    # 5 scores: 45, 52, 60, 68, 75 (median = 60)
    # Add new score 64 -> 45, 52, 60, 64, 68, 75 -> median = (60 + 64) / 2 = 62
    orig = [45, 52, 60, 68, 75]
    new_val = 64
    combined = sorted(orig + [new_val])
    med_new = round((combined[2] + combined[3]) / 2, 1)

    prompt = (
        f"Five learners scored the following marks (in ascending order): {orig}.\n"
        f"The original median is 60.\n"
        f"A learner who was absent writes the test later and scores {new_val}%.\n"
        f"Calculate the **new median** of the 6 scores."
    )
    ans_str = str(med_new)
    sol = (
        f"1. Insert {new_val} into the ordered list: {combined}.\n"
        f"2. For $n = 6$, the median is the mean of the 3rd and 4th terms:\n"
        f"$$\\text{{Median}} = \\frac{{{combined[2]} + {combined[3]}}}{{2}} = \\frac{{{combined[2] + combined[3]}}}{{2}} = {med_new}$$"
    )
    return {
        "subskill": "42_recalculate_median_after_adding_new_learner_score",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Order 6 scores: {combined}", "marks": 1},
            {"step": f"Average 3rd and 4th terms: ({combined[2]} + {combined[3]})/2 = {med_new}", "marks": 1},
        ],
        "hints": [
            f"Insert {new_val} into the list in the correct position.",
            f"Find the middle two numbers: {combined[2]} and {combined[3]}.",
        ],
        "misconception_tags": ["median_even_count_average_error"],
    }


# -----------------------------------------------------------------------------
# 43. Effect on Mean When All Scores Increase by a Constant
# -----------------------------------------------------------------------------
def arch_43_determine_effect_on_mean_when_all_scores_increase_by_constant(r: random.Random) -> Dict[str, Any]:
    mean_orig = r.randint(50, 65)
    c = r.randint(3, 8)
    mean_new = mean_orig + c

    prompt = (
        f"A class has a mean test mark of {mean_orig}%.\n"
        f"The teacher decides to award a bonus of {c} marks to every single learner in the class.\n"
        f"1. What is the new mean mark?\n"
        f"2. State the general statistical rule for the mean when a constant $c$ is added to every data point."
    )
    ans_str = f"New mean: {mean_new}%; Rule: New Mean = Old Mean + c"
    sol = (
        f"1. New Mean = ${mean_orig} + {c} = {mean_new}\\%$\n"
        f"2. **Rule**: If a constant $c$ is added to every observation in a dataset, "
        f"the mean increases by exactly that same constant $c$."
    )
    return {
        "subskill": "43_determine_effect_on_mean_when_all_scores_increase_by_constant",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": f"{mean_new}%",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate new mean: {mean_new}%", "marks": 1},
            {"step": "State rule: Mean increases by constant c", "marks": 1},
        ],
        "hints": [
            f"Add {c} to the original mean: {mean_orig} + {c}.",
            "Every learner gains {c}, so the entire average shifts up by {c}.",
        ],
        "misconception_tags": ["linear_transformation_mean_rule"],
    }


# -----------------------------------------------------------------------------
# 44. Effect on Range When All Scores Increase by a Constant
# -----------------------------------------------------------------------------
def arch_44_determine_effect_on_range_when_all_scores_increase_by_constant(r: random.Random) -> Dict[str, Any]:
    range_orig = r.randint(25, 45)
    c = r.randint(5, 10)

    prompt = (
        f"A dataset has a range of {range_orig}.\n"
        f"If every single score in the dataset is increased by {c}, what is the **new range**? Explain your answer."
    )
    ans_str = str(range_orig)
    sol = (
        f"**New Range = {range_orig}** (remains unchanged).\n\n"
        f"**Explanation**: Both the maximum and the minimum increase by {c}:\n"
        f"$$\\text{{New Range}} = (\\text{{Max}} + {c}) - (\\text{{Min}} + {c}) = \\text{{Max}} - \\text{{Min}} = {range_orig}$$\n"
        f"Adding a constant shifts the distribution without altering its spread/dispersion."
    )
    return {
        "subskill": "44_determine_effect_on_range_when_all_scores_increase_by_constant",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State that new range is still {range_orig}", "marks": 1},
            {"step": "Explain that both max and min shift by c, keeping spread identical", "marks": 1},
        ],
        "hints": [
            "Does adding a number to everyone change the distance between the highest and lowest scores?",
            "Both top and bottom values move by the same amount, so the difference stays the same.",
        ],
        "misconception_tags": ["range_shift_by_constant_fallacy"],
    }


# -----------------------------------------------------------------------------
# 45. Effect on Mean When Scores Multiplied by a Factor
# -----------------------------------------------------------------------------
def arch_45_determine_effect_on_mean_when_all_scores_multiplied_by_factor(r: random.Random) -> Dict[str, Any]:
    mean_orig = 30.0
    factor = 2.0
    mean_new = mean_orig * factor

    prompt = (
        f"A test was out of 50 marks and the class mean was {int(mean_orig)}.\n"
        f"To convert the marks to percentages (out of 100), every learner's mark is doubled (multiplied by 2).\n"
        f"1. What is the new class mean percentage?\n"
        f"2. State the general rule when all data points are multiplied by a factor $k$."
    )
    ans_str = f"New mean: {int(mean_new)}%; Rule: New Mean = Old Mean * k"
    sol = (
        f"1. New Mean = ${int(mean_orig)} \\times 2 = {int(mean_new)}\\%$\n"
        f"2. **Rule**: If every value in a dataset is multiplied by a scale factor $k$, "
        f"the new mean is multiplied by the same factor: $\\bar{{x}}_{{\\text{{new}}}} = k \\cdot \\bar{{x}}_{{\\text{{old}}}}$."
    )
    return {
        "subskill": "45_determine_effect_on_mean_when_all_scores_multiplied_by_factor",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": f"{int(mean_new)}%",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate new mean: {int(mean_new)}%", "marks": 1},
            {"step": "State rule: Mean scales by factor k", "marks": 1},
        ],
        "hints": [
            f"Multiply the original mean ({int(mean_orig)}) by 2.",
            "Scaling all numbers scales the average by the exact same multiplier.",
        ],
        "misconception_tags": ["multiplicative_scaling_mean_rule"],
    }


# -----------------------------------------------------------------------------
# 46. Compare Variability Between Two Weather Stations
# -----------------------------------------------------------------------------
def arch_46_compare_variability_between_two_weather_stations(r: random.Random) -> Dict[str, Any]:
    # Coastal: Durban mean 24, range 6
    # Inland: Kimberley mean 24, range 22
    prompt = (
        "Two South African cities recorded their maximum daily temperatures over 14 days in winter:\n"
        "• Durban (Coastal): Mean = 23°C, Range = 5°C (Min = 21°C, Max = 26°C)\n"
        "• Kimberley (Inland): Mean = 23°C, Range = 18°C (Min = 14°C, Max = 32°C)\n\n"
        "1. Compare the temperatures of both cities using their mean.\n"
        "2. Compare their temperature variability using the range.\n"
        "3. Explain what this means in practical terms for someone planning outdoor activities."
    )
    ans_str = "Means are equal (23°C); Kimberley has much higher variability (range 18°C vs 5°C); Durban has stable weather while Kimberley has extreme swings"
    sol = (
        "1. Both cities have the same average daily temperature of 23°C.\n"
        "2. Kimberley experiences far greater variability (range 18°C vs Durban's 5°C).\n"
        "3. In practical terms, Durban's daily weather is steady and predictable, whereas Kimberley swings between "
        "very cold mornings and hot afternoons, requiring diverse clothing."
    )
    return {
        "subskill": "46_compare_variability_between_two_weather_stations",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that means are identical (23°C)", "marks": 1},
            {"step": "Note Kimberley's much larger range (18°C vs 5°C)", "marks": 1},
            {"step": "Interpret practically (stable vs fluctuating climate)", "marks": 1},
        ],
        "hints": [
            "Mean gives the central value (both 23°C).",
            "Range shows the spread between cold and warm days.",
        ],
        "misconception_tags": ["variability_contextual_interpretation_error"],
    }


# -----------------------------------------------------------------------------
# 47. Draw Reasoned Conclusion from Customer Feedback Table
# -----------------------------------------------------------------------------
def arch_47_draw_reasoned_conclusion_from_customer_feedback_table(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A fast-food restaurant surveyed 200 customers regarding service ratings:\n\n"
        "| Rating Category | Number of Customers |\n"
        "| :--- | :---: |\n"
        "| Excellent (5) | 120 |\n"
        "| Good (4) | 50 |\n"
        "| Average (3) | 18 |\n"
        "| Poor (2) | 8 |\n"
        "| Terrible (1) | 4 |\n\n"
        "1. What percentage of customers rated the service as 'Good' or 'Excellent'?\n"
        "2. Based on this statistical evidence, write a brief, objective conclusion for the store manager."
    )
    pct = round(((120 + 50) / 200) * 100, 1)  # 85.0%
    ans_str = f"{_fmt(pct)}% satisfied; Strongly positive customer satisfaction"
    sol = (
        f"1. Good + Excellent = $120 + 50 = 170$ customers.\n"
        f"$$\\text{{Percentage}} = \\frac{{170}}{{200}} \\times 100\\% = {_fmt(pct)}\\%$$\n"
        f"2. **Conclusion**: An overwhelming majority ({_fmt(pct)}%) of patrons report positive satisfaction, "
        f"indicating high operational service quality with only 6% expressing dissatisfaction."
    )
    return {
        "subskill": "47_draw_reasoned_conclusion_from_customer_feedback_table",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": f"{_fmt(pct)}%",
        "sample_answer": ans_str,
        "tolerance": 0.1,
        "marking_schema": [
            {"step": f"Calculate 170/200 = {_fmt(pct)}%", "marks": 1},
            {"step": "Provide objective data-backed conclusion", "marks": 1},
        ],
        "hints": [
            "Add the counts for Excellent and Good: 120 + 50.",
            "Divide 170 by the total of 200 and multiply by 100.",
        ],
        "misconception_tags": ["data_aggregation_percentage_error"],
    }


# -----------------------------------------------------------------------------
# 48. Recommend Policy Decision Based on Bimodal Transport Survey
# -----------------------------------------------------------------------------
def arch_48_recommend_policy_decision_based_on_bimodal_transport_survey(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A municipal commuter travel time survey shows two distinct rush hour clusters: "
        "peak morning arrivals occur strictly between 06:30–07:15 and 08:00–08:45, with almost no passengers between 07:15–08:00.\n"
        "Explain why scheduling buses at constant, equal intervals all morning is inefficient, and recommend a better schedule."
    )
    concept = "Constant intervals waste empty buses during the 07:15–08:00 lull while causing severe overcrowding during the two peaks. The municipality should deploy high-frequency buses during the two peak windows and reduce service during the trough."
    return {
        "subskill": "48_recommend_policy_decision_based_on_bimodal_transport_survey",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Concentrate bus frequency during peak intervals and reduce during trough",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify inefficiency of uniform scheduling for non-uniform demand", "marks": 1},
            {"step": "Recommend targeted peak-hour bus deployment", "marks": 1},
        ],
        "hints": [
            "When are people actually travelling? (Two distinct rush hour peaks).",
            "Buses should be scheduled to match actual commuter demand patterns.",
        ],
        "misconception_tags": ["policy_alignment_to_distribution_shape"],
    }


# -----------------------------------------------------------------------------
# 49. Summarise Key Findings for Formal Statistical Report
# -----------------------------------------------------------------------------
def arch_49_summarise_key_findings_for_formal_statistical_report(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner presents a statistical report on school electricity consumption.\n"
        "List three essential components that must always be included in a formal data report "
        "(e.g. sample size/data source, summary measures, critical evaluation of limitations)."
    )
    concept = "1. Clear description of data source and sample size (N). 2. Key summary statistics (mean/median and measure of spread). 3. Explicit discussion of limitations or sources of error."
    return {
        "subskill": "49_summarise_key_findings_for_formal_statistical_report",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Data source/N, summary statistics, discussion of limitations",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State data source and sample size", "marks": 1},
            {"step": "State summary measures of center and spread", "marks": 1},
            {"step": "State discussion of limitations / potential bias", "marks": 1},
        ],
        "hints": [
            "A complete report states where the data came from, what the numbers summarize, and what flaws exist.",
            "Include sample size, averages, and limitations.",
        ],
        "misconception_tags": ["formal_report_structure_incompleteness"],
    }


# -----------------------------------------------------------------------------
# 50. Compound Multi-Stage Data Interpretation & Reporting Synthesis
# -----------------------------------------------------------------------------
def arch_50_compound_multi_stage_data_interpretation_and_reporting_synthesis(r: random.Random) -> Dict[str, Any]:
    # Two clinics comparing patient wait times
    clinic_a = [15, 20, 25, 30, 35]  # symmetric, mean = 25, median = 25, range = 20
    clinic_b = [10, 15, 20, 25, 110]  # skewed with outlier, mean = 36, median = 20, range = 100

    prompt = (
        "Two municipal health clinics record patient wait times (in minutes) for 5 patients:\n"
        f"• Clinic A: {clinic_a}\n"
        f"• Clinic B: {clinic_b}\n\n"
        "1. Calculate the mean wait time for Clinic A and for Clinic B.\n"
        "2. Identify the median wait time for Clinic A and for Clinic B.\n"
        "3. An administrator claims: 'Clinic A is more efficient because its mean wait time is 25 minutes compared to 36 minutes for Clinic B.' "
        "Provide a detailed statistical critique of this claim, referencing the median and the outlier."
    )
    ans_str = "Mean A = 25, Mean B = 36; Median A = 25, Median B = 20; Claim flawed because Clinic B's mean is distorted by 110 min outlier"
    sol = (
        "1. **Means**:\n"
        "• Clinic A Mean = $\\frac{15 + 20 + 25 + 30 + 35}{5} = \\frac{125}{5} = 25\\text{ min}$\n"
        "• Clinic B Mean = $\\frac{10 + 15 + 20 + 25 + 110}{5} = \\frac{180}{5} = 36\\text{ min}$\n\n"
        "2. **Medians**:\n"
        "• Clinic A Median = 25 min\n"
        "• Clinic B Median = 20 min\n\n"
        "3. **Critique**: The administrator's claim is misleading. 4 out of 5 patients at Clinic B waited 25 minutes or less "
        "(median 20 min, which is faster than Clinic A's median of 25 min). A single severe outlier (110 min) heavily inflated "
        "Clinic B's mean. The median is the more appropriate statistic here because of the extreme positive skew."
    )
    return {
        "subskill": "50_compound_multi_stage_data_interpretation_and_reporting_synthesis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Calculate Clinic A mean = 25, Clinic B mean = 36", "marks": 1},
            {"step": "Identify Clinic A median = 25, Clinic B median = 20", "marks": 1},
            {"step": "Explain that Clinic B's mean is distorted by outlier of 110 min", "marks": 1},
            {"step": "Conclude that median (20 vs 25) shows Clinic B typically has faster wait times", "marks": 1},
        ],
        "hints": [
            "Calculate both means and both medians.",
            "Look at the single 110-minute wait time at Clinic B: how does it affect the mean vs median?",
        ],
        "misconception_tags": ["compound_synthesis_outlier_critique_error"],
    }
