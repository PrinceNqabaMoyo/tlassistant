"""Subskills 01 to 08: Sampling methods, survey design, and bias detection for Grade 12 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    SA_PROVINCES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_pct,
)


def generate_01_stratified_sampling_proportions(r: random.Random) -> Dict[str, Any]:
    """Calculate proportional sample size for a stratum in stratified random sampling."""
    province = r.choice(SA_PROVINCES)
    total_population = r.choice([12000, 15000, 20000, 25000, 30000])
    stratum_pop = r.choice([2400, 3000, 4500, 5000, 6000])
    sample_size = r.choice([400, 500, 600, 800, 1000])

    prop = stratum_pop / total_population
    expected_sample = int(round(prop * sample_size))
    correct_ans = f"{expected_sample} learners"

    custom_options = [
        f"{expected_sample} learners",
        f"{int(round(sample_size / 4))} learners",
        f"{int(round(expected_sample * 1.5))} learners",
        f"{int(round(expected_sample * 0.7))} learners",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A national educational research council is conducting a stratified survey of {sample_size} Grade 12 learners "
        f"across South Africa. In the target population of {_fmt(total_population)} learners, {_fmt(stratum_pop)} learners "
        f"are enrolled in schools in {province}.\n\n"
        f"Calculate the number of learners that must be selected from {province} so that the sample is strictly proportional."
    )
    explanation = (
        f"Step 1: Calculate the proportion of learners in {province}: {_fmt(stratum_pop)} ÷ {_fmt(total_population)} = {_fmt(prop, 4)} [M].\n"
        f"Step 2: Multiply the proportion by the total sample size: {_fmt(prop, 4)} × {sample_size} = {expected_sample} learners [A]."
    )
    return _build_question_payload(
        subskill_id="01_stratified_sampling_proportions",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Identify the proportion of the target province relative to the national population.",
        tier_2=f"Divide the provincial learners ({_fmt(stratum_pop)}) by the total population ({_fmt(total_population)}).",
        tier_3=f"Multiply that fraction by the overall sample size ({sample_size}) to find the provincial quota: {expected_sample}.",
        r=r,
    )


def generate_02_systematic_sampling_interval(r: random.Random) -> Dict[str, Any]:
    """Determine the sampling interval k in systematic sampling."""
    n_pop = r.choice([1200, 1500, 2400, 3600, 4800, 5000])
    n_sample = r.choice([60, 80, 100, 120, 150])
    k = n_pop // n_sample
    correct_ans = f"Every {k}th person (k = {k})"

    custom_options = [
        f"Every {k}th person (k = {k})",
        f"Every {k + 5}th person (k = {k + 5})",
        f"Every {max(2, k - 5)}th person (k = {max(2, k - 5)})",
        f"Every {k * 2}th person (k = {k * 2})",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A quality auditor at a food processing plant in KwaZulu-Natal needs to inspect a systematic sample "
        f"of {n_sample} pre-packaged food hampers from a production batch of {_fmt(n_pop)} numbered boxes.\n\n"
        f"Determine the sampling interval (k) that the auditor must use after choosing a random starting point."
    )
    explanation = (
        f"Step 1: Systematic sampling interval formula: k = N ÷ n [M].\n"
        f"Step 2: Calculate k = {_fmt(n_pop)} ÷ {n_sample} = {k} [M].\n"
        f"Step 3: The auditor must inspect every {k}th hamper on the packing line [A]."
    )
    return _build_question_payload(
        subskill_id="02_systematic_sampling_interval",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Recall the systematic sampling formula: k = Population size (N) / Sample size (n).",
        tier_2=f"Divide {_fmt(n_pop)} by {n_sample}.",
        tier_3=f"{_fmt(n_pop)} ÷ {n_sample} = {k}, so select every {k}th person/box.",
        r=r,
    )


def generate_03_convenience_sampling_bias(r: random.Random) -> Dict[str, Any]:
    """Identify selection bias resulting from convenience sampling."""
    location = r.choice([
        "outside an upscale shopping mall in Sandton at 11:00 on a Tuesday",
        "at a private golf estate clubhouse on a Sunday morning",
        "outside a university library during exam week",
        "at a luxury car dealership showroom"
    ])
    topic = r.choice([
        "household food security and social grant adequacy",
        "average national household monthly income",
        "public transport satisfaction and minibus taxi safety",
        "youth unemployment rates in informal settlements"
    ])

    correct_ans = "Convenience bias: The sample excludes lower-income and working-class citizens who do not frequent this venue during work hours"
    custom_options = [
        correct_ans,
        "Measurement bias: The respondents will give inaccurate calculations of their expenses",
        "Non-response bias: Only people who agree with the researcher will answer the survey",
        "Zero bias: Anyone present in the public venue has an equal probability of being surveyed",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A researcher surveying opinions on '{topic}' interviews the first 100 people encountered {location}.\n\n"
        f"Which statement best explains why this convenience sampling strategy produces severe statistical bias?"
    )
    explanation = (
        f"Step 1: Convenience sampling selects individuals who are easy to reach rather than a representative cross-section [M].\n"
        f"Step 2: The location and timing disproportionately over-represent wealthy or non-working individuals while excluding key demographics [M].\n"
        f"Step 3: Conclusion: This produces convenience/selection bias [A]."
    )
    return _build_question_payload(
        subskill_id="03_convenience_sampling_bias",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Consider whether all members of the South African population have an equal chance of being surveyed at that specific place and time.",
        tier_2="Identify which demographic groups are systematically excluded from that venue during regular working hours.",
        tier_3="Selecting people purely because they are nearby creates convenience/selection bias and invalidates generalisation.",
        r=r,
    )


def generate_04_questionnaire_leading_question(r: random.Random) -> Dict[str, Any]:
    """Identify leading questions and select an objective, neutral alternative."""
    biased_q = r.choice([
        "Do you agree that school uniforms are far too expensive and place an unfair burden on poor parents?",
        "Do you agree that matric exams are excessively difficult and cause unnecessary mental stress?",
        "Don't you agree that fast food should be heavily taxed because it causes childhood obesity?",
        "Wouldn't you agree that public transport fares are unreasonably high for daily commuters?"
    ])
    neutral_q = r.choice([
        "To what extent do you agree or disagree that school uniforms are affordable for your family?",
        "How would you rate the difficulty level of the matric examination papers on a scale of 1 to 5?",
        "What is your view on the taxation of fast food products?",
        "How satisfied are you with the current cost of your daily public transport commute?"
    ])

    correct_ans = f"Biased/Leading: It prompts the respondent toward agreement. Neutral alternative: '{neutral_q}'"
    custom_options = [
        correct_ans,
        "Neutral: The question offers a clear opinion that helps the respondent make up their mind",
        "Biased: The question is open-ended and cannot be recorded in a frequency table",
        "Neutral: It contains standard emotive adjectives common in South African journalism",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Evaluate the following question drafted for a national school survey:\n"
        f"\"{biased_q}\"\n\n"
        f"State whether this question is statistically sound or biased, and identify the most appropriate correction."
    )
    explanation = (
        f"Step 1: The question uses leading phrasing ('Do you agree that... far too expensive/unfair') prompting agreement [M].\n"
        f"Step 2: A valid statistical questionnaire must frame questions neutrally without presupposing an outcome [M].\n"
        f"Step 3: Correct choice is the neutral framing [A]."
    )
    return _build_question_payload(
        subskill_id="04_questionnaire_leading_question",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Check whether the question nudges the respondent toward a specific answer.",
        tier_2="Words like 'Do you agree that...' or 'far too expensive' introduce bias.",
        tier_3="A good survey question must allow respondents to express either agreement, disagreement, or neutrality.",
        r=r,
    )


def generate_05_sample_size_margin_of_error(r: random.Random) -> Dict[str, Any]:
    """Analyze the relationship between sample size and statistical confidence/margin of error."""
    n_small = r.choice([15, 20, 25])
    n_large = r.choice([400, 500, 600])
    cohort = r.choice([1200, 1800, 2500])

    correct_ans = f"Increasing sample size from {n_small} to {n_large} reduces sampling variability and narrows the margin of error"
    custom_options = [
        correct_ans,
        f"Increasing sample size increases the standard error because more data points create more errors",
        f"A sample of {n_small} is sufficient because any random selection yields identical percentages",
        f"Sample size has no effect on survey accuracy as long as the sample is drawn randomly",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A school principal with a matric cohort of {_fmt(cohort)} learners wishes to investigate learner study habits. "
        f"The teacher suggests surveying {n_small} learners, while the deputy principal recommends surveying {n_large} learners.\n\n"
        f"Explain from a statistical perspective why the deputy principal's larger sample size is superior."
    )
    explanation = (
        f"Step 1: A very small sample ({n_small}) has high sampling error and can easily be skewed by a few outliers [M].\n"
        f"Step 2: As sample size increases toward {n_large}, the sample statistics converge more closely to the population parameters [M].\n"
        f"Step 3: A larger sample reduces variance and narrows the margin of error [A]."
    )
    return _build_question_payload(
        subskill_id="05_sample_size_margin_of_error",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about how representative a tiny group of 15–20 learners can be of a large cohort.",
        tier_2="Larger samples capture the full diversity of the population and minimize the impact of individual anomalies.",
        tier_3="Increasing sample size reduces sampling variability and narrows the margin of error.",
        r=r,
    )


def generate_06_variable_classification(r: random.Random) -> Dict[str, Any]:
    """Classify statistical variables as categorical, numerical discrete, or numerical continuous."""
    variables = [
        ("Province of residence (e.g. Gauteng, Limpopo)", "Categorical (Nominal)"),
        ("Number of siblings living in the household", "Numerical Discrete"),
        ("Time spent travelling to school in minutes (e.g. 24,5 min)", "Numerical Continuous"),
        ("Monthly household electricity expenditure in Rands (e.g. R 845,60)", "Numerical Continuous"),
        ("Number of motor vehicles owned by a family", "Numerical Discrete"),
        ("Learner satisfaction rating (Poor, Fair, Good, Excellent)", "Categorical (Ordinal)"),
    ]
    var_text, correct_type = r.choice(variables)
    correct_ans = f"{var_text} is {correct_type}"

    all_types = ["Categorical (Nominal)", "Categorical (Ordinal)", "Numerical Discrete", "Numerical Continuous"]
    distractor_types = [t for t in all_types if t != correct_type]
    custom_options = [correct_ans] + [f"{var_text} is {t}" for t in distractor_types[:3]]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a national census questionnaire administered by Statistics South Africa, the following variable is recorded:\n"
        f"• {var_text}\n\n"
        f"Classify this statistical variable accurately."
    )
    explanation = (
        f"Step 1: Check whether the data is a label/category or a number [M].\n"
        f"Step 2: If numerical, determine whether it is counted in discrete integers or measured on a continuous scale [M].\n"
        f"Step 3: {var_text} is classified as {correct_type} [A]."
    )
    return _build_question_payload(
        subskill_id="06_variable_classification",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Distinguish between measured quantities (continuous), counted quantities (discrete), and descriptions/categories.",
        tier_2="Counts (like number of cars or people) are discrete; measurements (time, weight, money) are continuous.",
        tier_3=f"Therefore, {var_text} is {correct_type}.",
        r=r,
    )


def generate_07_non_response_bias(r: random.Random) -> Dict[str, Any]:
    """Analyze non-response rate and voluntary response bias in postal/online surveys."""
    sent = r.choice([2000, 2500, 3000, 5000])
    returned = r.choice([180, 240, 300, 450])
    return_rate = (returned / sent) * 100
    non_return_rate = 100.0 - return_rate

    correct_ans = f"Non-response rate: {_fmt(non_return_rate, 1)}%; creates voluntary response bias because only strongly motivated individuals reply"
    custom_options = [
        correct_ans,
        f"Non-response rate: {_fmt(return_rate, 1)}%; results are valid because {_fmt(returned)} is a statistically large sample",
        f"Non-response rate: {_fmt(non_return_rate, 1)}%; represents zero bias because non-respondents are assumed indifferent",
        f"Non-response rate: {_fmt(return_rate, 1)}%; causes measurement error due to questionnaire misinterpretation",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A municipal water authority distributed {_fmt(sent)} postal feedback questionnaires to residents. "
        f"Only {_fmt(returned)} questionnaires were completed and returned.\n\n"
        f"Calculate the non-response rate and explain the primary risk to the survey's validity."
    )
    explanation = (
        f"Step 1: Non-response count = {_fmt(sent)} - {_fmt(returned)} = {_fmt(sent - returned)} [M].\n"
        f"Step 2: Non-response percentage = ({_fmt(sent - returned)} ÷ {_fmt(sent)}) × 100% = {_fmt(non_return_rate, 1)}% [M].\n"
        f"Step 3: A high non-response rate causes voluntary response bias: those with strong grievances are far more likely to respond [A]."
    )
    return _build_question_payload(
        subskill_id="07_non_response_bias",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the percentage of people who did not return the questionnaire.",
        tier_2=f"Divide the unreturned forms ({_fmt(sent - returned)}) by the total sent ({_fmt(sent)}) and multiply by 100%.",
        tier_3=f"Non-response rate is {_fmt(non_return_rate, 1)}%, which leads to voluntary response bias.",
        r=r,
    )


def generate_08_census_vs_sample_stats_sa(r: random.Random) -> Dict[str, Any]:
    """Distinguish between a complete census and a sample survey in South African statistics."""
    correct_ans = "A census collects data from every individual in the entire population; a sample collects data from a representative subset"
    custom_options = [
        correct_ans,
        "A census collects only demographic data; a sample survey collects economic and financial data",
        "A census is voluntary for all citizens; a sample survey is legally mandatory under the Statistics Act",
        "A census is carried out every quarter; a sample survey is conducted once every ten years",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Statistics South Africa (Stats SA) conducts both the National Population Census and regular surveys "
        f"such as the General Household Survey (GHS).\n\n"
        f"Which statement correctly defines the difference between a census and a sample survey?"
    )
    explanation = (
        f"Step 1: Recall the statistical definition of a census: data collection from 100% of the population [M].\n"
        f"Step 2: Recall the definition of a sample: a representative sub-group selected to infer population characteristics [M].\n"
        f"Step 3: The correct definition is that a census covers everyone, while a sample covers a representative subset [A]."
    )
    return _build_question_payload(
        subskill_id="08_census_vs_sample_stats_sa",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Consider the scope of data collection in a census versus a sample survey.",
        tier_2="A census aims to count every single citizen in the country (e.g. Census 2011 or Census 2022).",
        tier_3="A sample survey selects a representative group of households to estimate population trends.",
        r=r,
    )
