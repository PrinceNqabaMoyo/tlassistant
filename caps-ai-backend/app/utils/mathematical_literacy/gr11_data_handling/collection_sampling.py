"""Subskills 1 to 9: Research Questions, Sampling, Bias, Instruments & Ethics for Grade 11 Mathematical Literacy."""
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


def generate_subskill_1(r: random.Random) -> Dict[str, Any]:
    """Subskill 1: Formulate a specific, measurable research question vs a vague aim."""
    topic = r.choice([
        ("learner transport times", "What is the average commute time in minutes for Grade 11 learners travelling to school from Khayelitsha?"),
        ("tuckshop expenditure", "How much money in Rands do Senior Phase learners spend per week at the school tuckshop on sugary snacks?"),
        ("mobile data usage", "What is the average number of gigabytes (GB) of cell phone data consumed per month by high school learners for homework?"),
        ("study hours", "How many hours per week do Grade 11 learners spend studying Mathematical Literacy outside of class hours?"),
    ])
    t_name, good_q = topic

    prompt = (
        f"A Grade 11 learner is planning a data handling project investigating {t_name}. "
        f"Which of the following represents the most specific and mathematically measurable research question?"
    )

    correct_ans = good_q
    wrong_1 = f"Do learners like {t_name} at school?"
    wrong_2 = f"Everything there is to know about {t_name} in South Africa."
    wrong_3 = f"Is {t_name} good or bad for teenagers?"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand characteristics of a valid research question [1 mark].\n"
        f"A research question must be specific, objective, and clearly define the target population and quantifiable units.\n"
        f"Step 2: Evaluate options [1 mark].\n"
        f"Only '{good_q}' specifies exact measurable units and a defined group.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="1",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="A strong research question must specify exact measurable quantities and a defined population.",
        tier_2="Look for the option that includes measurable units (such as minutes, Rands, GB, or hours).",
        tier_3=f"The best question is: {good_q}.",
        r=r,
    )


def generate_subskill_2(r: random.Random) -> Dict[str, Any]:
    """Subskill 2: Distinguish between target population and sample."""
    school = r.choice(["Soweto High School", "Durban Secondary", "Polokwane Combined School", "Kimberley High"])
    total_learners = r.choice([800, 950, 1100, 1250, 1400])
    sample_size = r.choice([80, 100, 120, 150])

    prompt = (
        f"A researcher wants to investigate the breakfast eating habits of all learners at {school}. "
        f"The school has a total enrollment of {_fmt(total_learners)} learners. "
        f"The researcher selects and interviews {_fmt(sample_size)} learners representing different grades.\n"
        f"In statistical terminology, what are the 'population' and the 'sample' in this study?"
    )

    correct_ans = f"Population: All {_fmt(total_learners)} learners at {school}; Sample: The {_fmt(sample_size)} interviewed learners"
    wrong_1 = f"Population: The {_fmt(sample_size)} interviewed learners; Sample: All {_fmt(total_learners)} learners at {school}"
    wrong_2 = f"Population: All high school learners across South Africa; Sample: All {_fmt(total_learners)} learners at {school}"
    wrong_3 = f"Population: Only the Grade 11 learners; Sample: The school principal and teachers"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Define population and sample [1 mark].\n"
        f"Population = The entire group of individuals about whom conclusions are to be drawn ({_fmt(total_learners)} learners).\n"
        f"Sample = The smaller subset selected from the population from whom data is gathered ({_fmt(sample_size)} learners).\n"
        f"Step 2: Contrast roles [1 mark].\n"
        f"The sample represents the population.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="2",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Population is the entire group being studied; sample is the smaller group actually tested.",
        tier_2=f"The total group is {_fmt(total_learners)} learners, and the surveyed group is {_fmt(sample_size)} learners.",
        tier_3=f"Population: All {_fmt(total_learners)} learners; Sample: The {_fmt(sample_size)} learners.",
        r=r,
    )


def generate_subskill_3(r: random.Random) -> Dict[str, Any]:
    """Subskill 3: Identify sampling method (Random, Stratified, Systematic, Convenience)."""
    method_data = r.choice([
        (
            "Stratified Sampling",
            "The researcher divides the school population into grade levels (Grades 8, 9, 10, 11, 12) and randomly selects 20 learners from each grade in proportion to their grade size."
        ),
        (
            "Systematic Sampling",
            "The researcher takes an alphabetical list of all registered learners and selects every 10th learner on the roster."
        ),
        (
            "Simple Random Sampling",
            "Every learner's admission number is placed into a computer program that generates 100 numbers completely by chance, giving each learner an equal opportunity of selection."
        ),
        (
            "Convenience Sampling",
            "The researcher stands at the tuckshop queue during first break and surveys the first 50 learners who walk past."
        ),
    ])
    method_name, scenario = method_data

    prompt = (
        f"Consider the following sampling procedure used in a school survey:\n"
        f"\"{scenario}\"\n"
        f"Which statistical sampling method is described here?"
    )

    correct_ans = method_name
    custom_opts = [
        "Stratified Sampling",
        "Systematic Sampling",
        "Simple Random Sampling",
        "Convenience Sampling",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Analyze the selection mechanism [1 mark].\n"
        f"The scenario states: \"{scenario}\".\n"
        f"Step 2: Match to formal definition [1 mark].\n"
        f"This matches the definition of {method_name}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="3",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Examine how the participants were selected: random draw, equal groups, fixed interval, or easiest access?",
        tier_2=f"This selection process corresponds directly to {method_name}.",
        tier_3=f"Answer: {method_name}.",
        r=r,
    )


def generate_subskill_4(r: random.Random) -> Dict[str, Any]:
    """Subskill 4: Identify and explain sampling bias in a survey scenario."""
    scenario = r.choice([
        (
            "surveying only learners who arrive at school in private cars",
            "household transport expenditure",
            "It excludes learners who walk or use public minibus taxis/trains, leading to an artificially high average transport cost"
        ),
        (
            "interviewing shoppers exclusively at an expensive organic boutique grocery store on a Tuesday morning",
            "average monthly household food spending in a city",
            "It over-represents high-income individuals and retirees who are free on weekday mornings, biasing the food budget upward"
        ),
        (
            "distributing an online internet survey about digital literacy exclusively via an Instagram link",
            "access to internet connectivity in a rural district",
            "It completely excludes people who lack smartphones or internet access, falsely overestimating digital connectivity"
        ),
    ])
    action, topic, bias_explanation = scenario

    prompt = (
        f"A researcher studying {topic} conducts data collection by {action}.\n"
        f"Why does this sampling procedure produce biased results?"
    )

    correct_ans = bias_explanation
    wrong_1 = "The sample size is always too large for statistical calculations"
    wrong_2 = "Mathematical literacy surveys require 100% of the entire national population to be surveyed"
    wrong_3 = "The researcher used electronic spreadsheets instead of manual paper questionnaires"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify the target population vs the actual sample selected [1 mark].\n"
        f"The target population includes all relevant participants, but the sample only captures a specific non-representative subgroup.\n"
        f"Step 2: Explain the systematic skew [1 mark].\n"
        f"{bias_explanation}.\n"
        f"Step 3: Conclude reason for bias [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="4",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about which groups of people are left out by this method.",
        tier_2=f"By {action}, certain segments of the population are systematically excluded.",
        tier_3=f"Correct reason: {bias_explanation}.",
        r=r,
    )


def generate_subskill_5(r: random.Random) -> Dict[str, Any]:
    """Subskill 5: Identify leading / loaded survey questions vs neutral questions."""
    prompt = (
        f"A school committee wants to survey learners about school uniform rules. "
        f"Which of the following survey questions is UNBIASED and NEUTRAL?"
    )

    correct_ans = "To what extent do you support or oppose the current school uniform policy? (Strongly Support / Support / Neutral / Oppose / Strongly Oppose)"
    wrong_1 = "Don't you agree that our uncomfortable school uniform is completely outdated and should be abolished?"
    wrong_2 = "Since every good learner loves our traditional uniform, how proud are you to wear it every day?"
    wrong_3 = "Why do you think the uniform is the worst part of attending this school?"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand criteria for neutral question design [1 mark].\n"
        f"A neutral survey question does not lead the respondent towards a preferred answer or use emotive adjectives.\n"
        f"Step 2: Evaluate options [1 mark].\n"
        f"Questions using phrases like 'Don't you agree that...' or 'Since every good learner loves...' are loaded questions.\n"
        f"Step 3: Stated neutral question [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="5",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="An unbiased question does not suggest an answer or use emotionally charged words.",
        tier_2="Look for the balanced question that allows respondents to choose both positive and negative options equally.",
        tier_3=f"Unbiased question: {correct_ans}.",
        r=r,
    )


def generate_subskill_6(r: random.Random) -> Dict[str, Any]:
    """Subskill 6: Select the most appropriate data collection instrument."""
    scenario = r.choice([
        (
            "Investigating how many cars pass through a busy intersection between 07:00 and 08:00 without stopping at the stop sign",
            "Direct Observation (tallying vehicles in real time at the intersection)",
            "observation captures actual physical behaviour without relying on self-reporting"
        ),
        (
            "Gathering detailed personal experiences and emotions from senior citizens regarding community healthcare services",
            "In-depth Face-to-Face Interview (structured or semi-structured)",
            "interviews allow open-ended follow-up questions and sensitive discussion"
        ),
        (
            "Gathering quantitative opinions from 500 learners across 10 classes in one day about tuckshop menu preferences",
            "Self-administered Written Questionnaire (printed or electronic form)",
            "questionnaires allow rapid, low-cost data collection from a large group"
        ),
        (
            "Analyzing the national inflation rate (CPI) and unemployment trends over the past 10 years in South Africa",
            "Official Secondary Database (Statistics South Africa / Stats SA reports)",
            "Stats SA compiles rigorous, comprehensive nationwide longitudinal census and economic data"
        ),
    ])
    research_task, instrument, reason = scenario

    prompt = (
        f"A researcher undertakes the following investigation:\n"
        f"\"{research_task}\"\n"
        f"Which data collection instrument is the most appropriate and reliable for this specific task?"
    )

    correct_ans = instrument
    all_instruments = [
        "Direct Observation (tallying vehicles in real time at the intersection)",
        "In-depth Face-to-Face Interview (structured or semi-structured)",
        "Self-administered Written Questionnaire (printed or electronic form)",
        "Official Secondary Database (Statistics South Africa / Stats SA reports)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=all_instruments)

    explanation = (
        f"Step 1: Identify the nature of the data needed [1 mark].\n"
        f"The task involves: \"{research_task}\".\n"
        f"Step 2: Match to optimal instrument [1 mark].\n"
        f"Because {reason}, {instrument} is optimal.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="6",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine whether the study requires watching events live, asking deep questions, surveying many people quickly, or using historical records.",
        tier_2=f"For this scenario: {reason}.",
        tier_3=f"Most appropriate instrument: {instrument}.",
        r=r,
    )


def generate_subskill_7(r: random.Random) -> Dict[str, Any]:
    """Subskill 7: Classify data as Categorical vs Numerical, and Discrete vs Continuous."""
    var_info = r.choice([
        ("Height of high school learners in centimetres", "Numerical Continuous", "can take any decimal value along a continuous scale of measurement"),
        ("Number of siblings each learner has", "Numerical Discrete", "consists of distinct whole counting numbers with no fractions"),
        ("T-shirt sizes (Small, Medium, Large, Extra Large)", "Categorical Ordinal", "consists of descriptive non-numerical labels that possess a natural ranked order"),
        ("Province of birth (Gauteng, KwaZulu-Natal, Limpopo, etc.)", "Categorical Nominal", "consists of descriptive names or labels with no inherent numerical order"),
    ])
    var_name, data_type, type_desc = var_info

    prompt = (
        f"Consider the statistical variable: \"{var_name}\".\n"
        f"How is this data variable classified in terms of type?"
    )

    correct_ans = data_type
    custom_opts = [
        "Numerical Continuous",
        "Numerical Discrete",
        "Categorical Ordinal",
        "Categorical Nominal",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Check if the variable is a number or a category [1 mark].\n"
        f"\"{var_name}\" is {'numerical' if 'Numerical' in data_type else 'categorical'}.\n"
        f"Step 2: Determine subtype [1 mark].\n"
        f"It is {data_type} because it {type_desc}.\n"
        f"Step 3: Stated classification [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="7",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Decide first whether it is measured in numbers (numerical) or words/categories (categorical).",
        tier_2=f"If numerical, can it have decimals (continuous) or only whole counts (discrete)? If categorical, does it have an order (ordinal) or not (nominal)?",
        tier_3=f"Classification: {data_type}.",
        r=r,
    )


def generate_subskill_8(r: random.Random) -> Dict[str, Any]:
    """Subskill 8: Interpret tally marks and convert to frequency count."""
    name = r.choice(SA_NAMES)
    sport = r.choice(["Soccer", "Netball", "Rugby", "Athletics", "Cricket"])

    # Number of bundles of 5 plus remaining tallies
    bundles_of_5 = r.choice([2, 3, 4, 5])
    rem_tallies = r.choice([1, 2, 3, 4])
    total_count = bundles_of_5 * 5 + rem_tallies

    # Text representation of tallies
    tally_repr = " ".join(["卌" for _ in range(bundles_of_5)]) + " " + "|" * rem_tallies

    prompt = (
        f"{name} records preferences for {sport} using standard tally marks:\n\n"
        f"**Tally Recorded:** `{tally_repr}`\n\n"
        f"What is the exact numerical frequency represented by these tally marks?"
    )

    correct_ans = f"{total_count}"
    wrong_1 = f"{total_count + 5}"
    wrong_2 = f"{total_count - 1}"
    wrong_3 = f"{bundles_of_5 * 5}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Count full bundles of five tallies [1 mark].\n"
        f"{bundles_of_5} bundles × 5 = {bundles_of_5 * 5}.\n"
        f"Step 2: Add single tally marks [1 mark].\n"
        f"{bundles_of_5 * 5} + {rem_tallies} = {total_count}.\n"
        f"Step 3: Stated frequency [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="8",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Each crossed bundle equals 5, and each single vertical line equals 1.",
        tier_2=f"({bundles_of_5} × 5) + {rem_tallies} = {total_count}.",
        tier_3=f"Frequency = {total_count}.",
        r=r,
    )


def generate_subskill_9(r: random.Random) -> Dict[str, Any]:
    """Subskill 9: Ethical considerations in data handling (POPIA, privacy, consent)."""
    prompt = (
        f"Under South African data privacy principles (Protection of Personal Information Act - POPIA), "
        f"which ethical guideline MUST a researcher follow when collecting personal data from learners?"
    )

    correct_ans = (
        "Obtain informed consent, ensure voluntary participation, and protect confidentiality by keeping individual responses anonymous"
    )
    wrong_1 = "Publish full names, phone numbers, and home addresses of all participants on public social media"
    wrong_2 = "Force all learners to participate under penalty of failing their term report"
    wrong_3 = "Sell the learners' contact details to commercial advertising companies without permission"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand ethical standards in statistical research [1 mark].\n"
        f"Participants have the legal and moral right to privacy, informed consent, and confidential handling of data.\n"
        f"Step 2: Align with POPIA [1 mark].\n"
        f"Data must be processed lawfully, securely, and with strict anonymity for minors.\n"
        f"Step 3: Conclusion [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="9",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Ethics in research requires respecting participant privacy, ensuring consent, and keeping data confidential.",
        tier_2="Identify the statement promoting informed consent and anonymity.",
        tier_3=f"Correct guideline: {correct_ans}.",
        r=r,
    )
