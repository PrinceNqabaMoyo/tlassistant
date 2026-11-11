"""Cluster 1: Data Handling Cycle, Collection & Classification (Subskills 1 to 8).

Covers:
1. The 6 stages of the Data Handling Cycle in logical sequence
2. Population vs Sample distinction and representative sampling
3. Sample bias detection and convenience sampling flaws
4. Data collection instruments: questionnaires, interviews, observations
5. Questionnaire question design: identifying biased/leading questions
6. Categorical (qualitative) vs Numerical (quantitative) data classification
7. Discrete (countable) vs Continuous (measurable) numerical data
8. Statistical ethics: confidentiality, anonymity, and informed consent
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_data_cycle_stages_sequence_identification(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In Mathematical Literacy, investigating a real-world statistical problem follows the "
        f"official CAPS **Data Handling Cycle**.\n\n"
        f"Study the following 5 stages arranged in random order:\n"
        f"1. Summarise data (calculate mean, median, mode, range)\n"
        f"2. Formulate questions and identify research aim\n"
        f"3. Represent data (draw bar graphs, histograms, pie charts)\n"
        f"4. Collect and record raw data (surveys, questionnaires)\n"
        f"5. Organise and classify data (tally tables, frequency tables)\n\n"
        f"Which of the following represents the correct, logical sequence of the first 5 steps?"
    )
    ans = "2 → 4 → 5 → 1 → 3"
    opts = [
        "2 → 4 → 5 → 1 → 3",
        "4 → 2 → 5 → 3 → 1",
        "2 → 5 → 4 → 1 → 3",
        "5 → 4 → 2 → 1 → 3",
    ]

    s1 = f"The scientific data handling cycle follows an immutable order: First formulate the research question (2), then collect raw data (4), then classify/organise into tables (5), then calculate summary statistics (1), then represent graphically (3)."
    s2 = f"✓ [1 Mark: Method – Logical chronological deduction of the data handling cycle]\n1st: Formulate questions (2)\n2nd: Collect data (4)\n3rd: Organise data (5)\n4th: Summarise data (1)\n5th: Represent data (3)."
    s3 = f"✓ [1 Mark: Accuracy – Correct stage sequence]\nSequence: 2 → 4 → 5 → 1 → 3."

    return _build_question_payload(
        "data_cycle_stages_sequence_identification",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="You must formulate a question before you can collect answers.",
        tier_2_hint="After collecting data, you must organise it into a table before calculating the mean or drawing a graph.",
        tier_3_hint="Correct sequence: 2 → 4 → 5 → 1 → 3.",
    )


def _gen_data_pop_vs_sample_identification(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_school = r.choice([800, 950, 1100, 1200])
    sample_size = r.choice([50, 80, 100, 120])

    prompt = (
        f"{name} wants to investigate the average amount of pocket money spent weekly at the school tuckshop.\n\n"
        f"• The high school has a total enrollment of {total_school} learners across Grades 8 to 12.\n"
        f"• {name} randomly selects and surveys {sample_size} learners from various classes during break.\n\n"
        f"In this statistical investigation, identify the **target population** and the **sample**."
    )
    ans = f"Population: All {total_school} learners in the school; Sample: The {sample_size} randomly surveyed learners."
    opts = [
        f"Population: All {total_school} learners in the school; Sample: The {sample_size} randomly surveyed learners.",
        f"Population: The {sample_size} surveyed learners; Sample: All {total_school} learners in the school.",
        f"Population: Only the Grade 10 learners; Sample: All tuckshop workers.",
        f"Population: The tuckshop manager; Sample: The school governing body.",
    ]

    s1 = f"Define population: the entire complete group of individuals under investigation ({total_school} learners). Define sample: a representative subset selected from the population to participate ({sample_size} learners)."
    s2 = f"✓ [1 Mark: Method – Identifying entire group as population and surveyed subset as sample]\nTarget Population = Total {total_school} enrolled learners.\nSample = {sample_size} surveyed learners."
    s3 = f"✓ [1 Mark: Accuracy – Correct population and sample matching]\n{ans}"

    return _build_question_payload(
        "data_pop_vs_sample_identification",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="The population is the entire group of interest; the sample is the smaller group actually asked.",
        tier_2_hint=f"Total enrolled = {total_school} (population); surveyed = {sample_size} (sample).",
        tier_3_hint=f"{ans}",
    )


def _gen_data_sample_bias_and_fairness_audit(r: random.Random) -> Dict[str, Any]:
    scenario = r.choice([
        (
            "standing outside an expensive private golf club on a weekday morning and asking members how much they spend on groceries each month",
            "Biased sample: Wealthy golf club members do not represent the general South African population; the sample excludes middle- and low-income households.",
            "Fair sample: Golfers eat a wide variety of foodstuffs.",
            "Unbiased sample: Anyone is allowed to play golf in South Africa.",
            "Random sample: The surveyor asked the first 50 people who walked past."
        ),
        (
            "conducting an online survey about access to municipal electricity on a website that requires high-speed home fibre internet",
            "Biased sample: It completely excludes informal settlement residents and households without computers or internet access who are most affected by electricity poverty.",
            "Fair sample: Everyone who uses internet uses electricity.",
            "Unbiased sample: Online surveys are completely automated.",
            "Representative sample: Internet websites reach all nine provinces equally."
        ),
        (
            "surveying only Grade 12 learners in a high school about whether Grade 8 initiation games should be banned",
            "Biased sample: Grade 12 seniors have a vested interest in maintaining traditions, while Grade 8 junior victims are excluded from giving their opinions.",
            "Fair sample: Grade 12 learners have been at the school longest and have the most wisdom.",
            "Unbiased sample: Senior learners represent the school leadership.",
            "Random sample: 50 Grade 12 learners were selected randomly from the register."
        ),
    ])
    survey_method, critique, d1, d2, d3 = scenario

    prompt = (
        f"A student researcher collects data by **{survey_method}**.\n\n"
        f"Critically evaluate this data collection method in terms of sampling bias and fairness."
    )
    ans = critique
    opts = [critique, d1, d2, d3]

    s1 = f"Evaluate sampling methodology for systemic exclusion, convenience bias, and lack of representative cross-sectional diversity."
    s2 = f"✓ [1 Mark: Method – Identifying specific demographic exclusion and convenience bias]\nA sample is biased if certain key segments of the target population have zero probability of being selected."
    s3 = f"✓ [1 Mark: Accuracy – Correct statistical critique]\nEvaluation: {critique}"

    return _build_question_payload(
        "data_sample_bias_and_fairness_audit",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Who is excluded from this sample? Does the sample reflect the whole target group?",
        tier_2_hint="A convenience sample taken from a specific unrepresentative location creates bias.",
        tier_3_hint=f"Correct critique: {critique}",
    )


def _gen_data_collection_instruments_selection(r: random.Random) -> Dict[str, Any]:
    research_task = r.choice([
        (
            "determining the exact volume of water leaking per minute from dripping municipal communal taps across a township",
            "Physical scientific measurement log (using a graduated measuring jug and a stopwatch)",
            "Self-administered written questionnaire",
            "Telephonic interview survey",
            "Postal mail-in survey"
        ),
        (
            "gathering private opinions and emotional perceptions of trauma survivors regarding community safety",
            "One-on-one structured or semi-structured personal interview",
            "Tally observation sheet at a traffic intersection",
            "Stopwatch timing log",
            "Laboratory mass scale"
        ),
        (
            "gathering quick multiple-choice feedback from 1 000 consumers nationwide regarding a new soft drink flavour",
            "Online or printed multiple-choice questionnaire",
            "In-depth 2-hour clinical interview",
            "Physical tape measure observation",
            "Thermometer temperature log"
        ),
        (
            "counting the number of heavy delivery trucks vs passenger cars passing through a toll gantry between 07:00 and 09:00",
            "Direct visual observation sheet using a tally counter",
            "Mailed paper questionnaire",
            "Focus group discussion",
            "Personal interview with pedestrians"
        ),
    ])
    task_desc, best_tool, d1, d2, d3 = research_task

    prompt = (
        f"A research team is planning an investigation: **{task_desc}**.\n\n"
        f"Which data collection instrument is most scientifically appropriate, accurate, and practical?"
    )
    ans = best_tool
    opts = [best_tool, d1, d2, d3]

    s1 = f"Select appropriate data collection instruments (questionnaire, interview, observation sheet, measurement device) based on the nature of the data."
    s2 = f"✓ [1 Mark: Method – Matching data type with optimal recording instrument]\nQuantitative physical flows require measurement instruments; large-scale opinions require questionnaires; behavioral counts require observation sheets."
    s3 = f"✓ [1 Mark: Accuracy – Correct instrument choice]\nAppropriate instrument: {best_tool}."

    return _build_question_payload(
        "data_collection_instruments_selection",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"What kind of data is being collected in: {task_desc}?",
        tier_2_hint="Physical measurements need measuring tools; opinions need surveys; traffic counts need tally sheets.",
        tier_3_hint=f"The most appropriate tool is: {best_tool}.",
    )


def _gen_data_questionnaire_design_leading_questions(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A community researcher drafts questions for a survey on school uniform policies.\n\n"
        f"Study the following four proposed questions:\n"
        f"Question A: 'Do you agree that school uniforms are terribly old-fashioned and should be abolished?'\n"
        f"Question B: 'What is your opinion on the school uniform policy? (Support / Neutral / Oppose)'\n"
        f"Question C: 'Isn't it true that strict uniforms create unnecessary financial strain on poor parents?'\n"
        f"Question D: 'Don't you think only bad schools force learners to wear ties in hot weather?'\n\n"
        f"Which of these questions is properly designed as an **unbiased, neutral question**?"
    )
    ans = "Question B: 'What is your opinion on the school uniform policy? (Support / Neutral / Oppose)'"
    opts = [
        "Question B: 'What is your opinion on the school uniform policy? (Support / Neutral / Oppose)'",
        "Question A: 'Do you agree that school uniforms are terribly old-fashioned and should be abolished?'",
        "Question C: 'Isn't it true that strict uniforms create unnecessary financial strain on poor parents?'",
        "Question D: 'Don't you think only bad schools force learners to wear ties in hot weather?'",
    ]

    s1 = f"Identify leading/biased questions containing loaded emotional words ('terribly old-fashioned', 'isn't it true', 'don't you think') versus neutral, balanced phrasing."
    s2 = f"✓ [1 Mark: Method – Identifying neutral framing and balanced response options]\nUnbiased questions do not steer the respondent towards an intended answer and offer balanced choices."
    s3 = f"✓ [1 Mark: Accuracy – Selection of the neutral question]\nUnbiased question: Question B."

    return _build_question_payload(
        "data_questionnaire_design_leading_questions",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="A leading question nudges the respondent toward a specific point of view using emotional words.",
        tier_2_hint="Look for the only question that does not use biased words and offers balanced choices.",
        tier_3_hint="Question B is neutral and unbiased.",
    )


def _gen_data_classification_categorical_vs_numerical(r: random.Random) -> Dict[str, Any]:
    var_scenario = r.choice([
        ("Monthly household electricity bill in Rands (e.g. R 850,50)", "Numerical (Quantitative) data", "Categorical (Qualitative) data"),
        ("Brand of cell phone owned (e.g. Samsung, Apple, Huawei, Nokia)", "Categorical (Qualitative) data", "Numerical (Quantitative) data"),
        ("South African province of birth (e.g. Gauteng, Limpopo, Eastern Cape)", "Categorical (Qualitative) data", "Numerical (Quantitative) data"),
        ("Height of high school netball players measured in centimetres (e.g. 172 cm)", "Numerical (Quantitative) data", "Categorical (Qualitative) data"),
        ("Commuting transport mode to work (e.g. Minibus taxi, Train, Bus, Private Car)", "Categorical (Qualitative) data", "Numerical (Quantitative) data"),
    ])
    var_name, correct_type, other_type = var_scenario

    prompt = (
        f"In a statistical survey, researchers record the following variable from respondents:\n"
        f"**'{var_name}'**\n\n"
        f"Classify this variable as either Categorical (Qualitative) data or Numerical (Quantitative) data, with motivation."
    )
    if "Numerical" in correct_type:
        ans = f"{correct_type} — The values are meaningful numbers obtained from counting or measuring on which mathematical calculations (like mean) can be performed."
        opts = [
            f"{correct_type} — The values are meaningful numbers obtained from counting or measuring on which mathematical calculations (like mean) can be performed.",
            f"{other_type} — The values represent descriptive categories or qualities described in words.",
            "Ordinal data with no numerical meaning.",
            "Binary boolean data only.",
        ]
    else:
        ans = f"{correct_type} — The values represent descriptive categories, names, or labels described in words rather than numerical quantities."
        opts = [
            f"{correct_type} — The values represent descriptive categories, names, or labels described in words rather than numerical quantities.",
            f"{other_type} — The values represent continuous physical quantities that can be added together.",
            "Continuous numerical data that can be multiplied.",
            "Ratio-scale data.",
        ]

    s1 = f"Distinguish between Categorical data (words, categories, qualities) and Numerical data (numbers representing counts or measurements)."
    s2 = f"✓ [1 Mark: Method – Distinguishing between qualitative categories and quantitative numbers]\nCategories are descriptive labels; numerical values are quantities subject to arithmetic operations."
    s3 = f"✓ [1 Mark: Accuracy – Correct classification and motivation]\nClassification: {ans}"

    return _build_question_payload(
        "data_classification_categorical_vs_numerical",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Are the values recorded in words/labels or in numbers?",
        tier_2_hint="Words = Categorical (Qualitative); Numbers = Numerical (Quantitative).",
        tier_3_hint=f"{ans}",
    )


def _gen_data_classification_discrete_vs_continuous(r: random.Random) -> Dict[str, Any]:
    scenario = r.choice([
        ("Number of siblings in a family (e.g. 0, 1, 2, 3)", "Discrete numerical data", "The variable can only take whole integer values resulting from counting; you cannot have 2,37 siblings.", "Continuous numerical data"),
        ("Time taken to complete a 10 km marathon race in minutes and seconds (e.g. 42 min 15,4 s)", "Continuous numerical data", "The variable is measured on a continuous scale and can take any value, including fractions and decimals.", "Discrete numerical data"),
        ("Number of goals scored by a soccer team in a league match (e.g. 0, 1, 2)", "Discrete numerical data", "Goals are counted in indivisible whole numbers with no intermediate fractional values.", "Continuous numerical data"),
        ("Mass of a newborn baby weighed on a hospital scale in kilograms (e.g. 3,425 kg)", "Continuous numerical data", "Mass is a physical measurement that can take any value along a continuous range depending on scale precision.", "Discrete numerical data"),
        ("Number of passengers boarding a Metrorail train at Park Station", "Discrete numerical data", "Passengers are counted as individual discrete persons; fractional passengers are impossible.", "Continuous numerical data"),
    ])
    var_name, correct_type, motivation, other_type = scenario

    prompt = (
        f"Consider the following numerical variable:\n"
        f"**'{var_name}'**\n\n"
        f"Classify whether this variable is **Discrete** numerical data or **Continuous** numerical data, and provide the mathematical reason."
    )
    ans = f"{correct_type} — {motivation}"
    opts = [
        f"{correct_type} — {motivation}",
        f"{other_type} — The variable can only be described in words rather than numbers.",
        f"{other_type} — The variable cannot be plotted on a graph.",
        "Categorical data with no numeric value.",
    ]

    s1 = f"Distinguish between Discrete data (countable whole integer values with jumps) and Continuous data (measurable quantities that take any real value on a continuous interval)."
    s2 = f"✓ [1 Mark: Method – Identifying counting vs measurement]\nCounting objects yields discrete integers; measuring physical properties (time, mass, length) yields continuous decimals."
    s3 = f"✓ [1 Mark: Accuracy – Correct classification and technical motivation]\n{ans}"

    return _build_question_payload(
        "data_classification_discrete_vs_continuous",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Can this variable have decimal fractions, or is it obtained only by counting whole units?",
        tier_2_hint="Counted = Discrete (whole numbers); Measured = Continuous (decimals/fractions).",
        tier_3_hint=f"{ans}",
    )


def _gen_data_ethics_privacy_and_consent(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When researchers conduct statistical surveys involving human participants in South Africa "
        f"(regulated under the Protection of Personal Information Act / POPIA and ethical research codes), "
        f"which of the following is a mandatory ethical requirement?"
    )
    ans = "Participants must be fully informed about the survey purpose, participate voluntarily, and their personal data must be kept confidential and anonymized."
    opts = [
        "Participants must be fully informed about the survey purpose, participate voluntarily, and their personal data must be kept confidential and anonymized.",
        "Researchers must publish the full names and home addresses of all respondents online.",
        "Participants must be legally forced to answer every question under penalty of a municipal fine.",
        "Researchers must sell survey responses to commercial advertisers without consent.",
    ]

    s1 = f"Understand ethical protocols in data collection: informed consent, voluntary participation, confidentiality, right to withdraw, and anonymity."
    s2 = f"✓ [1 Mark: Method – Identifying core ethical principles in statistical investigations]\nResearch ethics require transparency, voluntary informed consent, and protection of privacy."
    s3 = f"✓ [1 Mark: Accuracy – Correct ethical requirement]\nRequirement: Participants must be fully informed about the survey purpose, participate voluntarily, and their personal data must be kept confidential and anonymized."

    return _build_question_payload(
        "data_ethics_privacy_and_consent",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Think about privacy, voluntary choice, and keeping personal data safe.",
        tier_2_hint="Participants must give informed voluntary consent and their identities must be protected.",
        tier_3_hint="Informed consent and confidentiality are mandatory.",
    )
