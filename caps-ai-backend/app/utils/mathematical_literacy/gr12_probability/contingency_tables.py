"""Subskills 17 to 24: Two-way contingency tables, marginal totals, joint and conditional probabilities, and demographic risk."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_frac,
    _fmt_pct,
)


def generate_17_contingency_marginal_totals(r: random.Random) -> Dict[str, Any]:
    """Calculate missing marginal row and column totals in a two-way contingency table."""
    c11 = 45  # Male - Pass
    c12 = 15  # Male - Fail
    c21 = 55  # Female - Pass
    c22 = 5   # Female - Fail

    row1_tot = c11 + c12  # 60
    row2_tot = c21 + c22  # 60
    col1_tot = c11 + c21  # 100
    col2_tot = c12 + c22  # 20
    grand_tot = row1_tot + row2_tot  # 120

    correct_ans = f"Total Males = {row1_tot}; Total Pass = {col1_tot}; Grand Total = {grand_tot}"
    custom_options = [
        correct_ans,
        f"Total Males = {col1_tot}; Total Pass = {row1_tot}; Grand Total = 100",
        f"Total Males = {row1_tot - 10}; Total Pass = {col1_tot + 10}; Grand Total = {grand_tot}",
        f"Total Males = {c11}; Total Pass = {c21}; Grand Total = {grand_tot}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    table_md = (
        "| Gender | Pass | Fail | Total |\n"
        "|---|---|---|---|\n"
        f"| Male | {c11} | {c12} | **A** |\n"
        f"| Female | {c21} | {c22} | {row2_tot} |\n"
        f"| **Total** | **B** | {col2_tot} | **C** |\n"
    )

    prompt = (
        f"Consider the two-way contingency table below recording driver license test results:\n\n"
        f"{table_md}\n"
        f"Calculate missing values A (Total Males), B (Total Pass), and C (Grand Total)."
    )
    explanation = (
        f"Step 1: Row 1 Total A = {c11} + {c12} = {row1_tot} [M].\n"
        f"Step 2: Column 1 Total B = {c11} + {c21} = {col1_tot} [M].\n"
        f"Step 3: Grand Total C = {row1_tot} + {row2_tot} = {grand_tot} [A]."
    )
    return _build_question_payload(
        subskill_id="17_contingency_marginal_totals",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add across the rows and down the columns.",
        tier_2=f"A = {c11} + {c12} = {row1_tot}; B = {c11} + {c21} = {col1_tot}.",
        tier_3=f"Grand total C = {grand_tot}.",
        r=r,
    )


def generate_18_contingency_joint_probability(r: random.Random) -> Dict[str, Any]:
    """Calculate joint probability P(A and B) directly from a two-way contingency table."""
    c_fav = 45  # Male and Pass
    n_total = 120
    frac_str = _fmt_frac(c_fav, n_total)
    pct = (c_fav / n_total) * 100.0

    correct_ans = f"P(Male and Pass) = 45/120 = {frac_str} ({_fmt_pct(pct, 1)})"
    custom_options = [
        correct_ans,
        f"P(Male and Pass) = 45/60 = 3/4 (75,0%)",
        f"P(Male and Pass) = 45/100 = 9/20 (45,0%)",
        f"P(Male and Pass) = 1/120 (0,8%)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a sample of 120 learner drivers:\n"
        f"• 45 males passed the test\n"
        f"• 15 males failed\n"
        f"• 55 females passed\n"
        f"• 5 females failed\n\n"
        f"If one individual is selected at random from the entire sample of 120 learners, "
        f"calculate the joint probability that the person is Male AND Passed the test."
    )
    explanation = (
        f"Step 1: Identify cell count for (Male and Pass) = 45 [M].\n"
        f"Step 2: Grand total of sample = 120 [M].\n"
        f"Step 3: P(Male and Pass) = 45/120 = {frac_str} ({_fmt_pct(pct, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="18_contingency_joint_probability",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the number in the specific intersection cell by the grand total.",
        tier_2=f"45 males passed out of 120 total learners.",
        tier_3=f"45/120 simplifies to {frac_str} ({_fmt_pct(pct, 1)}).",
        r=r,
    )


def generate_19_contingency_conditional_probability(r: random.Random) -> Dict[str, Any]:
    """Calculate conditional probability P(A given B) from a restricted row/column total."""
    # P(Pass given Male): 45 / 60
    male_pass = 45
    total_male = 60
    frac_str = _fmt_frac(male_pass, total_male)
    pct = (male_pass / total_male) * 100.0

    correct_ans = f"P(Pass | Male) = 45/60 = {frac_str} ({_fmt_pct(pct, 1)})"
    custom_options = [
        correct_ans,
        f"P(Pass | Male) = 45/120 = 3/8 (37,5%)",
        f"P(Pass | Male) = 45/100 = 9/20 (45,0%)",
        f"P(Pass | Male) = 60/120 = 1/2 (50,0%)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"From the driving test survey of 120 individuals:\n"
        f"• Total males who wrote = 60 (of which 45 passed and 15 failed)\n"
        f"• Total females who wrote = 60 (of which 55 passed and 5 failed)\n\n"
        f"Calculate the conditional probability that a randomly chosen candidate passed the test, GIVEN THAT the candidate is male."
    )
    explanation = (
        f"Step 1: Restrict the sample space strictly to the given condition (Males): Total Males = 60 [M].\n"
        f"Step 2: Number of passing males = 45 [M].\n"
        f"Step 3: P(Pass | Male) = 45 ÷ 60 = {frac_str} ({_fmt_pct(pct, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="19_contingency_conditional_probability",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Notice the condition: 'GIVEN THAT the candidate is male'. Look only at the Male row.",
        tier_2="Divide the passing males (45) by total males (60).",
        tier_3=f"45/60 = {frac_str} ({_fmt_pct(pct, 1)}).",
        r=r,
    )


def generate_20_evaluating_independence_contingency(r: random.Random) -> Dict[str, Any]:
    """Test whether two categorical attributes are statistically independent using contingency table rates."""
    # Female pass rate: 55/60 = 91.7%, Male pass rate: 45/60 = 75.0%
    correct_ans = "Dependent: Passing rates differ by gender (Female: 91,7% vs Male: 75,0%), so gender influences the probability of passing"

    custom_options = [
        correct_ans,
        "Independent: Because exactly 60 males and 60 females wrote the test",
        "Mutually exclusive: No candidate could write both male and female tests",
        "Complementary: The sum of passing males and failing females equals 50",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a driver examination center:\n"
        f"• Male pass rate: P(Pass | Male) = 45/60 = 75,0%\n"
        f"• Female pass rate: P(Pass | Female) = 55/60 = 91,7%\n\n"
        f"State whether the event of passing the driving test is independent of gender, with statistical justification."
    )
    explanation = (
        f"Step 1: Check conditional probabilities: P(Pass | Male) = 75,0% vs P(Pass | Female) = 91,7% [M].\n"
        f"Step 2: If independent, P(Pass | Male) would equal P(Pass | Female) = overall P(Pass) [M].\n"
        f"Step 3: Because the rates differ, the attributes are dependent [A]."
    )
    return _build_question_payload(
        subskill_id="20_evaluating_independence_contingency",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Compare the pass percentage for males with the pass percentage for females.",
        tier_2="Females had a 91,7% pass rate while males had a 75,0% pass rate.",
        tier_3="Because the pass probabilities are different, the outcome depends on gender.",
        r=r,
    )


def generate_21_missing_cell_deduction(r: random.Random) -> Dict[str, Any]:
    """Deduce an internal cell value in a contingency table using row and column sums."""
    tot_row = 150
    tot_col = 180
    known_other = 80
    missing = tot_row - known_other  # 70

    correct_ans = f"{missing} participants"
    custom_options = [
        f"{missing} participants",
        f"{missing + 15} participants",
        f"{missing - 15} participants",
        f"{tot_row} participants",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a survey of 300 hospital patients:\n"
        f"• Total rural patients = {tot_row}\n"
        f"• Rural patients with chronic illness = {known_other}\n"
        f"• Rural patients without chronic illness = X\n\n"
        f"Deduce the missing value X."
    )
    explanation = (
        f"Step 1: In a contingency table row: Total = Cell 1 + Cell 2 [M].\n"
        f"Step 2: Substitute: {tot_row} = {known_other} + X [M].\n"
        f"Step 3: X = {tot_row} - {known_other} = {missing} participants [A]."
    )
    return _build_question_payload(
        subskill_id="21_missing_cell_deduction",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the known cell from the row total.",
        tier_2=f"Calculate {tot_row} - {known_other}.",
        tier_3=f"X = {missing} participants.",
        r=r,
    )


def generate_22_driver_demographics_accident_risk(r: random.Random) -> Dict[str, Any]:
    """Calculate and compare accident risk probabilities across age brackets from insurance data."""
    young_accidents = r.choice([36, 40, 42, 48])
    young_total = 200
    older_accidents = r.choice([15, 18, 21, 24])
    older_total = 300

    d_spec_22 = {
        "diagram_role": "context",
        "kind": "contingency_table",
        "title": "Driver Insurance Claims by Age Bracket",
        "rows": ["< 25 yrs", ">= 25 yrs"],
        "columns": ["Accident Claim", "No Claim", "Total"],
        "matrix": [
            [young_accidents, young_total - young_accidents, young_total],
            [older_accidents, older_total - older_accidents, older_total],
        ],
    }

    p_young = (young_accidents / young_total) * 100.0  # 21.0%
    p_older = (older_accidents / older_total) * 100.0  # 6.0%

    correct_ans = f"Young drivers (<25 yrs): {_fmt_pct(p_young, 1)}; Older drivers (≥25 yrs): {_fmt_pct(p_older, 1)}; Young drivers are 3,5 times more likely to claim"
    custom_options = [
        correct_ans,
        f"Young drivers: {_fmt_pct(p_older, 1)}; Older drivers: {_fmt_pct(p_young, 1)}",
        f"Young drivers: 50,0%; Older drivers: 50,0%",
        f"Young drivers: {_fmt_pct(p_young * 2, 1)}; Older drivers: {_fmt_pct(p_older / 2, 1)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the driver insurance claims contingency table.\n"
        f"• Drivers under 25 years old: {young_accidents} claims out of {young_total} insured drivers\n"
        f"• Drivers 25 years and older: {older_accidents} claims out of {older_total} insured drivers\n\n"
        f"Calculate the claim probability percentage for both demographic groups and explain why insurers charge higher premiums to drivers under 25."
    )
    explanation = (
        f"Step 1: Young driver claim rate = ({young_accidents} ÷ {young_total}) × 100% = {_fmt_pct(p_young, 1)} [M].\n"
        f"Step 2: Older driver claim rate = ({older_accidents} ÷ {older_total}) × 100% = {_fmt_pct(p_older, 1)} [M].\n"
        f"Step 3: Ratio = {_fmt(p_young/p_older, 1)} times higher risk, justifying higher insurance premiums [A]."
    )
    return _build_question_payload(
        subskill_id="22_driver_demographics_accident_risk",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the percentage claim rate for each age group by dividing claims by total drivers.",
        tier_2=f"Young: {young_accidents}/{young_total} = {_fmt_pct(p_young, 1)}. Older: {older_accidents}/{older_total} = {_fmt_pct(p_older, 1)}.",
        tier_3="Young drivers have a significantly higher risk, which drives higher premiums.",
        r=r,
        diagram_spec=d_spec_22,
    )


def generate_23_school_pass_rates_contingency(r: random.Random) -> Dict[str, Any]:
    """Calculate overall school pass probability versus grade-specific conditional probability."""
    gr10_pass = 180
    gr10_total = 200
    gr12_pass = 140
    gr12_total = 150
    total_pass = gr10_pass + gr12_pass
    grand_total = gr10_total + gr12_total

    p_overall = (total_pass / grand_total) * 100.0
    p_gr12 = (gr12_pass / gr12_total) * 100.0

    correct_ans = f"Overall school pass rate = {_fmt_pct(p_overall, 1)}; Grade 12 pass rate = {_fmt_pct(p_gr12, 1)}"
    custom_options = [
        correct_ans,
        f"Overall school pass rate = {_fmt_pct(p_gr12, 1)}; Grade 12 pass rate = {_fmt_pct(p_overall, 1)}",
        f"Overall school pass rate = 50,0%; Grade 12 pass rate = 100,0%",
        f"Overall school pass rate = {_fmt_pct(p_overall - 10, 1)}; Grade 12 pass rate = {_fmt_pct(p_gr12 - 5, 1)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A secondary school tracks end-of-year examination results:\n"
        f"• Grade 10: {gr10_pass} passed out of {gr10_total} learners\n"
        f"• Grade 12: {gr12_pass} passed out of {gr12_total} learners\n\n"
        f"Calculate the overall pass probability for both grades combined, and the conditional probability of passing GIVEN THAT a learner is in Grade 12."
    )
    explanation = (
        f"Step 1: Total passed = {gr10_pass} + {gr12_pass} = {total_pass}; Grand Total = {gr10_total} + {gr12_total} = {grand_total} [M].\n"
        f"Step 2: Overall pass probability = ({total_pass} ÷ {grand_total}) × 100% = {_fmt_pct(p_overall, 1)} [M].\n"
        f"Step 3: Grade 12 conditional pass = ({gr12_pass} ÷ {gr12_total}) × 100% = {_fmt_pct(p_gr12, 1)} [A]."
    )
    return _build_question_payload(
        subskill_id="23_school_pass_rates_contingency",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the grand total pass rate first, then look strictly at Grade 12 learners.",
        tier_2=f"Overall: {total_pass}/{grand_total} = {_fmt_pct(p_overall, 1)}. Grade 12: {gr12_pass}/{gr12_total} = {_fmt_pct(p_gr12, 1)}.",
        tier_3=f"Overall: {_fmt_pct(p_overall, 1)}, Grade 12: {_fmt_pct(p_gr12, 1)}.",
        r=r,
    )


def generate_24_employment_by_education_qualification(r: random.Random) -> Dict[str, Any]:
    """Calculate the probability of employment conditioned on obtaining tertiary education."""
    employed_deg = 360
    total_deg = 400
    p_deg_employed = (employed_deg / total_deg) * 100.0

    employed_matric = 250
    total_matric = 500
    p_matric_employed = (employed_matric / total_matric) * 100.0

    correct_ans = f"Tertiary graduate employment probability: {_fmt_pct(p_deg_employed, 1)} vs Matric-only: {_fmt_pct(p_matric_employed, 1)}"
    custom_options = [
        correct_ans,
        f"Tertiary graduate employment probability: {_fmt_pct(p_matric_employed, 1)} vs Matric-only: {_fmt_pct(p_deg_employed, 1)}",
        f"Tertiary graduate employment probability: 100,0% vs Matric-only: 0,0%",
        f"Tertiary graduate employment probability: 50,0% vs Matric-only: 50,0%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a Stats SA labour survey of youth job-seekers:\n"
        f"• Group A (Tertiary diploma/degree): {employed_deg} employed out of {total_deg} candidates\n"
        f"• Group B (Matric only): {employed_matric} employed out of {total_matric} candidates\n\n"
        f"Calculate the employment probability for both educational qualification cohorts."
    )
    explanation = (
        f"Step 1: Tertiary employment probability = ({employed_deg} ÷ {total_deg}) × 100% = {_fmt_pct(p_deg_employed, 1)} [M].\n"
        f"Step 2: Matric-only employment probability = ({employed_matric} ÷ {total_matric}) × 100% = {_fmt_pct(p_matric_employed, 1)} [M].\n"
        f"Step 3: Graduates have a {_fmt_pct(p_deg_employed, 1)} employment rate compared to {_fmt_pct(p_matric_employed, 1)} for Matric-only [A]."
    )
    return _build_question_payload(
        subskill_id="24_employment_by_education_qualification",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the employment percentage for tertiary graduates and for matriculants separately.",
        tier_2=f"Graduates: {employed_deg}/{total_deg} = {_fmt_pct(p_deg_employed, 1)}. Matric: {employed_matric}/{total_matric} = {_fmt_pct(p_matric_employed, 1)}.",
        tier_3=f"Graduates: {_fmt_pct(p_deg_employed, 1)}; Matric: {_fmt_pct(p_matric_employed, 1)}.",
        r=r,
    )
