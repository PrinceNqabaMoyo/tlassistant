"""Grade 12 Mathematics - Finance: Annuities, Sinking Funds & Loan Amortization (Archetypes 01-25).
100% Aligned with South African National Curriculum Standards (CAPS Grade 12 Paper 1).
Grounded strictly in curriculum_docs_auto/Mathematics_Gr12/Syllabus.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Common Contract & Helper Functions
# ---------------------------------------------------------------------------

def _fmt_zar(amount: float) -> str:
    """Format a Rand amount with space thousands and comma decimal for cents."""
    val = round(float(amount), 2)
    neg = val < 0
    val = abs(val)
    cents = int(round(val * 100)) % 100
    whole = int(round(val * 100)) // 100
    whole_str = f"{whole:,}".replace(",", " ")
    if cents == 0:
        res = f"R {whole_str}"
    else:
        res = f"R {whole_str},{cents:02d}"
    return f"-{res}" if neg else res


def _fmt_decimal_sa(val: float, decimals: int = 2) -> str:
    """Format decimal number using South African comma separator."""
    s = f"{val:.{decimals}f}"
    return s.replace(".", "{,}")


def _base_contract(
    *,
    subskill: str,
    qtype: str,
    prompt: str,
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    hints: List[str],
    worked_solution: str,
    sample_answer: str,
    marking_schema: Dict[str, Any],
    duration_mins: int = 5,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "topic_id": "grade12_mathematics",
        "subtopic_id": "grade12_math_finance",
        "subskill": subskill,
        "mode": f"elementary_{subskill}",
        "term": 2,
        "caps_weight_percent": 15.0,
        "suggested_duration_mins": duration_mins,
        "type": qtype,
        "question_type": qtype,
        "question": prompt,
        "question_text": prompt,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id,
        "misconception_tags": misconception_tags,
        "hints": hints,
        "worked_solution": worked_solution,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
    }
    if extra:
        q.update(extra)
    return q


def _mcq(
    rng: random.Random,
    *,
    subskill: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    hints: List[str],
    worked_solution: str,
    duration_mins: int = 4,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct] + list(distractors)
    rng.shuffle(options)
    extra: Dict[str, Any] = {
        "options": options,
        "correct_answer": correct,
        "answer": correct,
    }
    if diagram_spec:
        extra["diagram_spec"] = diagram_spec
    return _base_contract(
        subskill=subskill,
        qtype="mcq",
        prompt=prompt,
        learning_objective_id=learning_objective_id,
        concept_id=concept_id,
        misconception_tags=misconception_tags,
        hints=hints,
        worked_solution=worked_solution,
        sample_answer=f"Correct Option: {correct}\n\nWorking:\n{worked_solution}",
        marking_schema={"total_marks": 2, "rules": [{"step": "Correct option selected", "marks": 2}]},
        duration_mins=duration_mins,
        extra=extra,
    )


def _typed(
    *,
    subskill: str,
    prompt: str,
    correct_answer: str,
    accepted_answers: List[str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    hints: List[str],
    worked_solution: str,
    marks: int = 4,
    duration_mins: int = 5,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    extra: Dict[str, Any] = {
        "correct_answer": correct_answer,
        "answer": correct_answer,
        "accepted_answers": accepted_answers,
    }
    if diagram_spec:
        extra["diagram_spec"] = diagram_spec
    return _base_contract(
        subskill=subskill,
        qtype="typed",
        prompt=prompt,
        learning_objective_id=learning_objective_id,
        concept_id=concept_id,
        misconception_tags=misconception_tags,
        hints=hints,
        worked_solution=worked_solution,
        sample_answer=f"Answer: {correct_answer}\n\nWorking:\n{worked_solution}",
        marking_schema={"total_marks": marks, "rules": [{"step": "Accurate calculation and formula application", "marks": marks}]},
        duration_mins=duration_mins,
        extra=extra,
    )


# ---------------------------------------------------------------------------
# Archetypes 01 - 10 (Future Value Annuities)
# ---------------------------------------------------------------------------

def _b01_future_value_annuity_monthly_investment(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([1500, 2000, 2500, 3000, 3500])
    rate = rng.choice([8.5, 9.0, 9.5, 10.0, 10.5])
    years = rng.choice([5, 8, 10])
    n = years * 12
    i = (rate / 100) / 12
    fv = x * ((1 + i)**n - 1) / i
    fv_rounded = round(fv, 2)
    ans = _fmt_zar(fv_rounded)

    prompt = (
        f"Lerato deposits {_fmt_zar(x)} at the end of every month into a retirement annuity account.\n"
        f"The interest rate is {_fmt_decimal_sa(rate)}\\% per annum compounded monthly.\n"
        f"Calculate the total future value of her investment at the end of {years} years, rounded to 2 decimal places."
    )
    sol = (
        f"1. Identify parameters:\n"
        f"- Monthly deposit: $x = {_fmt_zar(x)}$\n"
        f"- Monthly interest rate: $i = \\frac{{{rate}}}{{1200}} = {_fmt_decimal_sa(i, 6)}$\n"
        f"- Number of payments: $n = {years} \\times 12 = {n}$\n"
        f"2. Apply Future Value annuity formula:\n"
        f"$$F = \\frac{{x[(1+i)^n - 1]}}{{i}} = \\frac{{{x}[(1 + {_fmt_decimal_sa(i, 6)})^{{{n}}} - 1]}}{{{_fmt_decimal_sa(i, 6)}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="01_future_value_annuity_monthly_investment",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{fv_rounded:.2f}", f"{fv_rounded:.2f}".replace(".", ","), str(round(fv))],
        learning_objective_id="G12-MATH-FIN-01",
        concept_id="future_value_annuity_basic",
        misconception_tags=["used_present_value_instead_of_future_value", "annual_rate_not_divided_by_12"],
        hints=[
            r"Use the Future Value annuity formula: F = \frac{x[(1+i)^n - 1]}{i}.",
            f"Remember to divide the interest rate by 12: i = {rate} / 1200.",
            f"Calculate for n = {n} months. The total is {ans}.",
        ],
        worked_solution=sol,
    )


def _b02_future_value_annuity_solve_monthly_deposit(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice([250000, 300000, 400000, 500000])
    rate = rng.choice([9.0, 9.6, 10.2, 10.8])
    years = rng.choice([4, 5, 6])
    n = years * 12
    i = (rate / 100) / 12
    # x = F * i / ((1 + i)^n - 1)
    x = target * i / ((1 + i)**n - 1)
    x_rounded = round(x, 2)
    ans = _fmt_zar(x_rounded)

    prompt = (
        f"Thabo wants to save {_fmt_zar(target)} in {years} years' time to start a business.\n"
        f"He opens an investment fund offering {_fmt_decimal_sa(rate)}\\% per annum compounded monthly.\n"
        f"Calculate the regular monthly amount he must deposit at the end of each month to reach his goal."
    )
    sol = (
        f"1. State the Future Value formula rearranged for $x$:\n"
        f"$$x = \\frac{{F \\cdot i}}{{(1+i)^n - 1}}$$\n"
        f"2. Substitute $F = {_fmt_zar(target)}$, $i = \\frac{{{rate}}}{{1200}}$, and $n = {n}$:\n"
        f"$$x = \\frac{{{target} \\times {_fmt_decimal_sa(i, 6)}}}{{(1 + {_fmt_decimal_sa(i, 6)})^{{{n}}} - 1}} \\approx {ans}$$"
    )
    return _typed(
        subskill="02_future_value_annuity_solve_monthly_deposit",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{x_rounded:.2f}", f"{x_rounded:.2f}".replace(".", ","), str(round(x))],
        learning_objective_id="G12-MATH-FIN-02",
        concept_id="future_value_solve_payment_x",
        misconception_tags=["inverted_fraction_when_solving_for_x"],
        hints=[
            r"Rearrange F = \frac{x[(1+i)^n - 1]}{i} to solve for x: x = \frac{F \cdot i}{(1+i)^n - 1}.",
            f"Here F = {target}, i = {rate}/1200, n = {n}.",
            f"Monthly deposit required is {ans}.",
        ],
        worked_solution=sol,
    )


def _b03_future_value_annuity_solve_time_period_n_log(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([1200, 1500, 1800])
    rate = 9.0
    i = (rate / 100) / 12
    target_months = rng.choice([48, 60, 72])
    fv = x * ((1 + i)**target_months - 1) / i
    target_round = round(fv, -2)
    # Solve exact n from target_round
    # (1 + i)^n = target * i / x + 1 => n = log(...) / log(1 + i)
    exact_n = math.log((target_round * i / x) + 1) / math.log(1 + i)
    n_months = math.ceil(exact_n)

    prompt = (
        f"Sipho deposits {_fmt_zar(x)} at the end of each month into a savings account earning "
        f"{_fmt_decimal_sa(rate)}\\% p.a. compounded monthly.\n"
        f"Using logarithms, calculate how many monthly payments are required to accumulate at least {_fmt_zar(target_round)}."
    )
    ans = f"{n_months} payments"
    accepted = [ans, f"{n_months}", f"{n_months} months"]
    sol = (
        f"1. Use the Future Value annuity formula:\n"
        f"$$F = \\frac{{x[(1+i)^n - 1]}}{{i}} \\implies \\frac{{{target_round} \\times {_fmt_decimal_sa(i, 6)}}}{{{x}}} + 1 = (1 + {_fmt_decimal_sa(i, 6)})^n$$\n"
        f"2. Apply logarithms to both sides:\n"
        f"$$n = \\frac{{\\log\\left(\\frac{{{target_round} \\times {_fmt_decimal_sa(i, 6)}}}{{{x}}} + 1\\right)}}{{\\log(1 + {_fmt_decimal_sa(i, 6)})}} \\approx {_fmt_decimal_sa(exact_n, 2)}$$\n"
        f"3. Since payments are made at month-end, round up to {n_months} payments."
    )
    return _typed(
        subskill="03_future_value_annuity_solve_time_period_n_log",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-FIN-03",
        concept_id="logarithms_solve_time_period",
        misconception_tags=["natural_log_base_error", "failed_to_round_up_for_target"],
        hints=[
            r"Isolate (1+i)^n: (1+i)^n = \frac{F \cdot i}{x} + 1.",
            r"Take logs of both sides: n = \frac{\log(\dots)}{\log(1+i)}.",
            f"Round up to the nearest whole payment: {n_months} payments.",
        ],
        worked_solution=sol,
    )


def _b04_future_value_annuity_quarterly_compounding(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([4000, 5000, 6000])
    rate = rng.choice([8.0, 10.0, 12.0])
    years = rng.choice([4, 5, 6])
    n = years * 4
    i = (rate / 100) / 4
    fv = x * ((1 + i)**n - 1) / i
    fv_rounded = round(fv, 2)
    ans = _fmt_zar(fv_rounded)

    prompt = (
        f"A company invests {_fmt_zar(x)} at the end of every quarter into an expansion fund.\n"
        f"Interest is paid at {_fmt_decimal_sa(rate)}\\% per annum compounded quarterly.\n"
        f"Calculate the future value of the fund after {years} years."
    )
    sol = (
        f"1. Compounding is quarterly:\n"
        f"- Number of quarters: $n = {years} \\times 4 = {n}$\n"
        f"- Quarterly interest rate: $i = \\frac{{{rate}}}{{400}} = {_fmt_decimal_sa(i, 4)}$\n"
        f"2. Future value:\n"
        f"$$F = \\frac{{{x}[(1 + {_fmt_decimal_sa(i, 4)})^{{{n}}} - 1]}}{{{_fmt_decimal_sa(i, 4)}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="04_future_value_annuity_quarterly_compounding",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{fv_rounded:.2f}", f"{fv_rounded:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-04",
        concept_id="quarterly_compounding_annuity",
        misconception_tags=["divided_by_12_instead_of_4_for_quarterly"],
        hints=[
            "For quarterly compounding, divide the interest rate by 4: i = rate / 400.",
            f"Multiply the number of years by 4: n = {years} * 4 = {n}.",
            f"Future value is {ans}.",
        ],
        worked_solution=sol,
    )


def _b05_future_value_payment_immediately_annuity_due(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([1000, 1200, 1500])
    rate = 9.0
    years = 5
    n = years * 12
    i = (rate / 100) / 12
    # First payment immediately (T0) and last payment at Tn => n+1 payments
    # Or standard formula multiplied by (1+i)
    fv = x * ((1 + i)**n - 1) / i * (1 + i)
    fv_rounded = round(fv, 2)
    ans = _fmt_zar(fv_rounded)

    prompt = (
        f"Bongani makes monthly payments of {_fmt_zar(x)} into an investment account earning "
        f"{_fmt_decimal_sa(rate)}\\% p.a. compounded monthly.\n"
        f"He makes his first payment **immediately** ($T_0$) and continues making monthly deposits for {years} years ($T_{{{n}}}$).\n"
        f"Calculate the accumulated future value of his investment immediately after the last deposit at $T_{{{n}}}$."
    )
    sol = (
        f"1. Since the first payment is made immediately at $T_0$, every deposit earns an extra month of interest (annuity due):\n"
        f"$$F = \\frac{{x[(1+i)^n - 1]}}{{i}} \\times (1 + i)$$\n"
        f"2. Substitute $x = {_fmt_zar(x)}$, $i = \\frac{{{rate}}}{{1200}} = {_fmt_decimal_sa(i, 6)}$, $n = {n}$:\n"
        f"$$F = \\frac{{{x}[(1 + {_fmt_decimal_sa(i, 6)})^{{{n}}} - 1]}}{{{_fmt_decimal_sa(i, 6)}}} \\times (1 + {_fmt_decimal_sa(i, 6)}) \\approx {ans}$$"
    )
    return _typed(
        subskill="05_future_value_payment_immediately_annuity_due",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{fv_rounded:.2f}", f"{fv_rounded:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-05",
        concept_id="annuity_due_immediate_first_payment",
        misconception_tags=["omitted_extra_compounding_factor_for_t0"],
        hints=[
            "When the first deposit is made immediately at T0, multiply the standard annuity formula by (1 + i).",
            f"Here n = {n} and i = {rate}/1200.",
            f"Total future value is {ans}.",
        ],
        worked_solution=sol,
    )


def _b06_future_value_payment_starts_one_month_later(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([2200, 2400, 2800])
    rate = 10.5
    years = 4
    n = years * 12
    i = (rate / 100) / 12
    fv = x * ((1 + i)**n - 1) / i
    fv_rounded = round(fv, 2)
    ans = _fmt_zar(fv_rounded)

    prompt = (
        f"Naledi starts an investment plan. She will make her first deposit of {_fmt_zar(x)} **one month from now** ($T_1$) "
        f"and continues with monthly deposits until the end of {years} years ($T_{{{n}}}$).\n"
        f"Interest is {_fmt_decimal_sa(rate)}\\% p.a. compounded monthly.\n"
        f"Calculate the accumulated future value at $T_{{{n}}}$."
    )
    sol = (
        f"1. This is the standard ordinary annuity: first payment at $T_1$, last payment at $T_n$.\n"
        f"2. Total number of deposits $= {n}$.\n"
        f"$$F = \\frac{{{x}[(1 + {_fmt_decimal_sa(i, 6)})^{{{n}}} - 1]}}{{{_fmt_decimal_sa(i, 6)}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="06_future_value_payment_starts_one_month_later",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{fv_rounded:.2f}", f"{fv_rounded:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-06",
        concept_id="ordinary_annuity_standard_timeline",
        misconception_tags=["confused_ordinary_annuity_with_annuity_due"],
        hints=[
            "First payment at T1 means exactly n payments with no additional (1+i) multiplier.",
            rf"Apply F = \frac{{{x}[(1+i)^{{{n}}} - 1]}}{{i}} directly.",
            f"Future value is {ans}.",
        ],
        worked_solution=sol,
    )


def _b07_future_value_final_payment_before_maturity(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([1500, 2000])
    rate = 9.0
    i = (rate / 100) / 12
    pay_years = 4
    n = pay_years * 12
    wait_years = 2
    wait_months = wait_years * 12
    # F after pay_years, then compounds for wait_months
    fv_annuity = x * ((1 + i)**n - 1) / i
    final_amt = fv_annuity * (1 + i)**wait_months
    final_rounded = round(final_amt, 2)
    ans = _fmt_zar(final_rounded)

    prompt = (
        f"Kagiso deposits {_fmt_zar(x)} at the end of each month for {pay_years} years.\n"
        f"After {pay_years} years, he makes no further deposits, but leaves the accumulated money in the account for another {wait_years} years to earn interest.\n"
        f"The interest rate remains {_fmt_decimal_sa(rate)}\\% p.a. compounded monthly throughout.\n"
        f"Calculate the final balance at the end of {pay_years + wait_years} years."
    )
    sol = (
        f"1. Calculate accumulated future value of annuity after {pay_years} years ($n = {n}$):\n"
        f"$$F_1 = \\frac{{{x}[(1 + {_fmt_decimal_sa(i, 6)})^{{{n}}} - 1]}}{{{_fmt_decimal_sa(i, 6)}}} \\approx {_fmt_zar(round(fv_annuity, 2))}$$\n"
        f"2. For the next {wait_years} years ($m = {wait_months}$ months), this lump sum grows with compound interest:\n"
        f"$$A = F_1 \\times (1 + i)^{{{wait_months}}} = {_fmt_zar(round(fv_annuity, 2))} \\times (1 + {_fmt_decimal_sa(i, 6)})^{{{wait_months}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="07_future_value_final_payment_before_maturity",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{final_rounded:.2f}", f"{final_rounded:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-07",
        concept_id="two_stage_investment_growth",
        misconception_tags=["continued_annuity_during_dormant_period"],
        hints=[
            f"Stage 1: Future Value annuity for {n} months.",
            f"Stage 2: Compound the lump sum for {wait_months} months with A = P(1+i)^m.",
            f"The final balance is {ans}.",
        ],
        worked_solution=sol,
    )


def _b08_future_value_annuity_interest_rate_change(rng: random.Random) -> Dict[str, Any]:
    x = 2000
    r1 = 8.4
    r2 = 9.6
    i1 = (r1 / 100) / 12
    i2 = (r2 / 100) / 12
    n1 = 36  # first 3 years
    n2 = 24  # next 2 years
    # Stage 1 annuity value at T36
    fv1 = x * ((1 + i1)**n1 - 1) / i1
    # Grows at i2 for n2 months, plus second annuity at i2 for n2 months
    final_amt = fv1 * (1 + i2)**n2 + x * ((1 + i2)**n2 - 1) / i2
    final_rounded = round(final_amt, 2)
    ans = _fmt_zar(final_rounded)

    prompt = (
        f"An investor deposits {_fmt_zar(x)} at the end of each month into a 5-year investment fund.\n"
        f"For the first 3 years, the interest rate is {_fmt_decimal_sa(r1)}\\% p.a. compounded monthly.\n"
        f"Thereafter, the interest rate changes to {_fmt_decimal_sa(r2)}\\% p.a. compounded monthly for the remaining 2 years.\n"
        f"Calculate the total future value of the investment at the end of the 5 years."
    )
    sol = (
        f"1. Stage 1 accumulated value at $T_{{36}}$:\n"
        f"$$F_1 = \\frac{{{x}[(1 + {_fmt_decimal_sa(i1, 6)})^{{36}} - 1]}}{{{_fmt_decimal_sa(i1, 6)}}} \\approx {_fmt_zar(round(fv1, 2))}$$\n"
        f"2. Stage 2 accumulated value at $T_{{60}}$:\n"
        f"- The first lump sum $F_1$ earns interest at new rate $i_2$ for 24 months: $F_1(1 + i_2)^{{24}}$\n"
        f"- A new annuity of 24 deposits is made at rate $i_2$: $\\frac{{{x}[(1+i_2)^{{24}} - 1]}}{{i_2}}$\n"
        f"3. Total Future Value $= F_1(1 + i_2)^{{24}} + F_2 \\approx {ans}$."
    )
    return _typed(
        subskill="08_future_value_annuity_interest_rate_change",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{final_rounded:.2f}", f"{final_rounded:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-08",
        concept_id="changing_interest_rates_annuity",
        misconception_tags=["blended_interest_rates_incorrectly"],
        hints=[
            "Calculate the future value at the end of Year 3 first.",
            "Compound that balance forward by 24 months at the new rate, and add the second 24-month annuity.",
            f"The final accumulated sum is {ans}.",
        ],
        worked_solution=sol,
        marks=5,
    )


def _b09_future_value_with_lump_sum_withdrawal(rng: random.Random) -> Dict[str, Any]:
    x = 3000
    rate = 9.0
    i = (rate / 100) / 12
    # 5 years total = 60 months
    # Withdraw 20000 at month 24
    w = 20000
    fv_total = x * ((1 + i)**60 - 1) / i
    withdrawal_compounded = w * (1 + i)**(60 - 24)
    net_final = fv_total - withdrawal_compounded
    net_rounded = round(net_final, 2)
    ans = _fmt_zar(net_rounded)

    prompt = (
        f"Siphiwe invests {_fmt_zar(x)} at the end of each month into an annuity paying "
        f"{_fmt_decimal_sa(rate)}\\% p.a. compounded monthly for 5 years.\n"
        f"At the end of year 2 (month 24), she withdraws {_fmt_zar(w)} to pay emergency medical bills.\n"
        f"She continues her regular monthly deposits of {_fmt_zar(x)} until month 60.\n"
        f"Calculate the final accumulated balance at the end of the 5 years."
    )
    sol = (
        f"1. Calculate the total value of all 60 regular deposits without withdrawal:\n"
        f"$$F_{{\\text{{all}}}} = \\frac{{{x}[(1 + {_fmt_decimal_sa(i, 6)})^{{60}} - 1]}}{{{_fmt_decimal_sa(i, 6)}}} \\approx {_fmt_zar(round(fv_total, 2))}$$\n"
        f"2. Subtract the withdrawal compounded for the remaining $60 - 24 = 36$ months:\n"
        f"$$W_{{\\text{{compounded}}}} = {w}(1 + {_fmt_decimal_sa(i, 6)})^{{36}} \\approx {_fmt_zar(round(withdrawal_compounded, 2))}$$\n"
        f"3. Final balance $= F_{{\\text{{all}}}} - W_{{\\text{{compounded}}}} \\approx {ans}$."
    )
    return _typed(
        subskill="09_future_value_with_lump_sum_withdrawal",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{net_rounded:.2f}", f"{net_rounded:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-09",
        concept_id="annuity_with_intermittent_withdrawal",
        misconception_tags=["simply_subtracted_uncompounded_withdrawal"],
        hints=[
            "Treat the withdrawal as losing both the principal and the interest it would have earned over the remaining 36 months.",
            "Subtract W * (1+i)^36 from the total 60-month annuity value.",
            f"The final balance is {ans}.",
        ],
        worked_solution=sol,
        marks=5,
    )


def _b10_future_value_with_additional_lump_sum_deposit(rng: random.Random) -> Dict[str, Any]:
    x = 1500
    rate = 8.4
    i = (rate / 100) / 12
    lump = 25000
    years = 4
    n = years * 12
    # Lump sum deposited today (T0) + regular deposits from T1 to Tn
    lump_growth = lump * (1 + i)**n
    annuity_growth = x * ((1 + i)**n - 1) / i
    tot = lump_growth + annuity_growth
    tot_rounded = round(tot, 2)
    ans = _fmt_zar(tot_rounded)

    prompt = (
        f"Vusi deposits an initial lump sum of {_fmt_zar(lump)} today ($T_0$) into an investment account.\n"
        f"He then makes monthly deposits of {_fmt_zar(x)} starting in one month's time ($T_1$) for {years} years ($T_{{{n}}}$).\n"
        f"The account earns {_fmt_decimal_sa(rate)}\\% p.a. compounded monthly.\n"
        f"Calculate the total future value at the end of {years} years."
    )
    sol = (
        f"1. Growth of the initial lump sum over {n} months:\n"
        f"$$A = P(1+i)^n = {lump}(1 + {_fmt_decimal_sa(i, 6)})^{{{n}}} \\approx {_fmt_zar(round(lump_growth, 2))}$$\n"
        f"2. Accumulated value of the regular monthly deposits:\n"
        f"$$F = \\frac{{{x}[(1 + {_fmt_decimal_sa(i, 6)})^{{{n}}} - 1]}}{{{_fmt_decimal_sa(i, 6)}}} \\approx {_fmt_zar(round(annuity_growth, 2))}$$\n"
        f"3. Total value $= A + F \\approx {ans}$."
    )
    return _typed(
        subskill="10_future_value_with_additional_lump_sum_deposit",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{tot_rounded:.2f}", f"{tot_rounded:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-10",
        concept_id="combined_lump_sum_and_annuity",
        misconception_tags=["treated_initial_lump_sum_as_annuity_deposit"],
        hints=[
            "Compound the lump sum with A = P(1+i)^n.",
            "Calculate the annuity separately with F = x[(1+i)^n - 1] / i.",
            f"Add both accumulated amounts: {ans}.",
        ],
        worked_solution=sol,
    )


# ---------------------------------------------------------------------------
# Archetypes 11 - 25 (Present Value Annuities, Loans & Sinking Funds)
# ---------------------------------------------------------------------------

def _b11_present_value_annuity_home_loan_monthly_payment(rng: random.Random) -> Dict[str, Any]:
    bond = rng.choice([750000, 850000, 1000000, 1200000])
    rate = rng.choice([10.5, 11.0, 11.5, 12.0])
    years = 20
    n = years * 12
    i = (rate / 100) / 12
    # P = x[1 - (1+i)^-n] / i => x = P * i / [1 - (1+i)^-n]
    x = bond * i / (1 - (1 + i)**(-n))
    x_rounded = round(x, 2)
    ans = _fmt_zar(x_rounded)

    prompt = (
        f"A family takes out a home loan of {_fmt_zar(bond)} to purchase a house.\n"
        f"The bank charges interest at {_fmt_decimal_sa(rate)}\\% per annum compounded monthly.\n"
        f"The loan is to be repaid over {years} years by equal monthly payments starting one month after the loan is granted.\n"
        f"Calculate the monthly bond repayment, correct to 2 decimal places."
    )
    sol = (
        f"1. State the Present Value annuity formula:\n"
        f"$$P = \\frac{{x[1 - (1+i)^{{-n}}]}}{{i}}$$\n"
        f"2. Rearrange for monthly payment $x$:\n"
        f"$$x = \\frac{{P \\cdot i}}{{1 - (1+i)^{{-n}}}}$$\n"
        f"3. Substitute $P = {_fmt_zar(bond)}$, $i = \\frac{{{rate}}}{{1200}}$, and $n = {n}$:\n"
        f"$$x = \\frac{{{bond} \\times {_fmt_decimal_sa(i, 6)}}}{{1 - (1 + {_fmt_decimal_sa(i, 6)})^{{-{n}}}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="11_present_value_annuity_home_loan_monthly_payment",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{x_rounded:.2f}", f"{x_rounded:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-11",
        concept_id="present_value_loan_monthly_payment",
        misconception_tags=["used_positive_exponent_instead_of_negative_in_pv"],
        hints=[
            r"Use the Present Value formula: P = \frac{x[1 - (1+i)^{-n}]}{i}.",
            f"Here n = {years} * 12 = {n} months and i = {rate} / 1200.",
            f"Monthly repayment is {ans}.",
        ],
        worked_solution=sol,
    )


def _b12_present_value_annuity_maximum_loan_affordable(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([7500, 8500, 9500, 11000])
    rate = 11.25
    years = 20
    n = years * 12
    i = (rate / 100) / 12
    p = x * (1 - (1 + i)**(-n)) / i
    p_rounded = round(p, 2)
    ans = _fmt_zar(p_rounded)

    prompt = (
        f"An applicant can afford a maximum monthly bond repayment of {_fmt_zar(x)}.\n"
        f"The current home loan interest rate is {_fmt_decimal_sa(rate)}\\% p.a. compounded monthly over 20 years.\n"
        f"Calculate the maximum loan amount the applicant qualifies for."
    )
    sol = (
        f"1. Apply the Present Value annuity formula:\n"
        f"$$P = \\frac{{x[1 - (1+i)^{{-n}}]}}{{i}}$$\n"
        f"2. Substitute $x = {_fmt_zar(x)}$, $i = \\frac{{{rate}}}{{1200}}$, $n = {n}$:\n"
        f"$$P = \\frac{{{x}[1 - (1 + {_fmt_decimal_sa(i, 6)})^{{-{n}}}]}}{{{_fmt_decimal_sa(i, 6)}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="12_present_value_annuity_maximum_loan_affordable",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{p_rounded:.2f}", f"{p_rounded:.2f}".replace(".", ","), str(round(p))],
        learning_objective_id="G12-MATH-FIN-12",
        concept_id="maximum_affordable_loan_pv",
        misconception_tags=["multiplied_payment_by_number_of_months_ignoring_interest"],
        hints=[
            r"Substitute directly into P = \frac{x[1 - (1+i)^{-n}]}{i}.",
            f"Here x = {x}, n = {n}, i = {rate}/1200.",
            f"Maximum loan affordable is {ans}.",
        ],
        worked_solution=sol,
    )


def _b13_present_value_annuity_solve_time_period_n_log(rng: random.Random) -> Dict[str, Any]:
    p = 150000
    x = 4200
    rate = 12.0
    i = (rate / 100) / 12
    # P = x[1 - (1+i)^-n] / i => 1 - P*i/x = (1+i)^-n => -n = log(1 - P*i/x) / log(1+i)
    term = 1 - (p * i / x)
    exact_n = -math.log(term) / math.log(1 + i)
    n_months = math.ceil(exact_n)

    prompt = (
        f"A student owes {_fmt_zar(p)} on a study loan at {_fmt_decimal_sa(rate)}\\% p.a. compounded monthly.\n"
        f"She decides to repay the loan by paying {_fmt_zar(x)} at the end of each month.\n"
        f"Using logarithms, calculate the number of monthly payments required to settle the debt completely."
    )
    ans = f"{n_months} payments"
    accepted = [ans, f"{n_months}", f"{n_months} months"]
    sol = (
        f"1. Present value equation:\n"
        f"$$P = \\frac{{x[1 - (1+i)^{{-n}}]}}{{i}} \\implies 1 - \\frac{{{p} \\times {_fmt_decimal_sa(i, 4)}}}{{{x}}} = (1 + {_fmt_decimal_sa(i, 4)})^{{-n}}$$\n"
        f"2. Apply logarithms:\n"
        f"$$-n = \\frac{{\\log(1 - \\frac{{{p} \\times {i}}}{{{x}}})}}{{\\log(1 + {i})}} \\implies n \\approx {_fmt_decimal_sa(exact_n, 2)}$$\n"
        f"3. Round up to the next payment: {n_months} payments."
    )
    return _typed(
        subskill="13_present_value_annuity_solve_time_period_n_log",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-FIN-13",
        concept_id="pv_solve_n_logarithms",
        misconception_tags=["negative_sign_error_in_pv_log"],
        hints=[
            r"Rearrange: (1+i)^{-n} = 1 - \frac{P \cdot i}{x}.",
            r"Take logs: -n = \frac{\log(1 - P \cdot i / x)}{\log(1+i)}.",
            f"Round up to {n_months} payments.",
        ],
        worked_solution=sol,
    )


def _b14_present_value_deferred_loan_repayment(rng: random.Random) -> Dict[str, Any]:
    loan = 200000
    rate = 10.5
    i = (rate / 100) / 12
    # Deferment: First payment made 4 months after loan granted (instead of 1 month)
    # Interest accrues for 3 months: P' = loan * (1+i)^3
    defer_months = 3
    loan_accrued = loan * (1 + i)**defer_months
    n_payments = 48  # 4 years
    x = loan_accrued * i / (1 - (1 + i)**(-n_payments))
    x_rounded = round(x, 2)
    ans = _fmt_zar(x_rounded)

    prompt = (
        f"A business borrows {_fmt_zar(loan)} on 1 January at {_fmt_decimal_sa(rate)}\\% p.a. compounded monthly.\n"
        f"Due to cash flow constraints, the first repayment is deferred and will only be made on 1 May (4 months after the loan was granted).\n"
        f"The loan must be settled in {n_payments} equal monthly installments starting on 1 May.\n"
        f"Calculate the required monthly payment $x$, correct to 2 decimal places."
    )
    sol = (
        f"1. The standard start of payments is at $T_1$. Since the first payment is at $T_4$, interest accumulates for 3 months ($T_0$ to $T_3$):\n"
        f"$$P' = P(1+i)^3 = {loan}(1 + {_fmt_decimal_sa(i, 6)})^3 \\approx {_fmt_zar(round(loan_accrued, 2))}$$\n"
        f"2. Apply the Present Value formula using the accrued loan balance $P'$ for {n_payments} payments:\n"
        f"$$x = \\frac{{P' \\cdot i}}{{1 - (1+i)^{{-{n_payments}}}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="14_present_value_deferred_loan_repayment",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{x_rounded:.2f}", f"{x_rounded:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-14",
        concept_id="deferred_annuity_interest_accrual",
        misconception_tags=["compounded_interest_for_4_months_instead_of_3"],
        hints=[
            "Remember: a normal loan payment starts at month 1. If it starts at month 4, interest accrues for 4 - 1 = 3 months.",
            f"Calculate the new principal: P' = {loan} * (1 + i)^3.",
            f"Solve for x over {n_payments} payments to get {ans}.",
        ],
        worked_solution=sol,
        marks=5,
    )


def _b15_loan_total_repayment_and_total_interest(rng: random.Random) -> Dict[str, Any]:
    p = 500000
    rate = 11.0
    years = 15
    n = years * 12
    i = (rate / 100) / 12
    x = p * i / (1 - (1 + i)**(-n))
    total_paid = x * n
    interest_paid = total_paid - p
    ans = _fmt_zar(round(interest_paid, 2))

    prompt = (
        f"A home buyer takes out a {_fmt_zar(p)} mortgage bond at {_fmt_decimal_sa(rate)}\\% p.a. compounded monthly over {years} years.\n"
        f"The monthly installment is {_fmt_zar(round(x, 2))}.\n"
        f"Calculate the total interest paid over the entire {years}-year life of the loan."
    )
    sol = (
        f"1. Total amount repaid $= n \\times x = {n} \\times {_fmt_zar(round(x, 2))} = {_fmt_zar(round(total_paid, 2))}$.\n"
        f"2. Total Interest Paid $= \\text{{Total Repaid}} - \\text{{Original Loan Principal}}$\n"
        f"$$\\text{{Total Interest}} = {_fmt_zar(round(total_paid, 2))} - {_fmt_zar(p)} = {ans}$$"
    )
    return _typed(
        subskill="15_loan_total_repayment_and_total_interest",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{round(interest_paid, 2):.2f}", f"{round(interest_paid, 2):.2f}".replace(".", ","), str(round(interest_paid))],
        learning_objective_id="G12-MATH-FIN-15",
        concept_id="total_finance_charges_calculation",
        misconception_tags=["forgot_to_subtract_principal"],
        hints=[
            "Total repaid is the monthly payment multiplied by the total number of payments (n).",
            "Total interest is Total Repaid minus the original loan amount P.",
            f"The total interest is {ans}.",
        ],
        worked_solution=sol,
    )


def _b16_outstanding_balance_loan_backward_method(rng: random.Random) -> Dict[str, Any]:
    p = 800000
    rate = 10.5
    years = 20
    n = years * 12
    i = (rate / 100) / 12
    x = p * i / (1 - (1 + i)**(-n))
    paid_years = 5
    paid_months = paid_years * 12
    remaining_n = n - paid_months
    # Backward method: Balance = PV of remaining payments
    bal = x * (1 - (1 + i)**(-remaining_n)) / i
    bal_rounded = round(bal, 2)
    ans = _fmt_zar(bal_rounded)

    prompt = (
        f"A homeowner borrows {_fmt_zar(p)} over 20 years at {_fmt_decimal_sa(rate)}\\% p.a. compounded monthly.\n"
        f"The monthly installment is {_fmt_zar(round(x, 2))}.\n"
        f"Using the backward method (present value of remaining installments), calculate the outstanding balance on the loan "
        f"immediately after making the {paid_months}th payment (end of year {paid_years})."
    )
    sol = (
        f"1. Number of remaining installments: $n_{{\\text{{remaining}}}} = {n} - {paid_months} = {remaining_n}$.\n"
        f"2. Apply the Present Value formula for the remaining payments:\n"
        f"$$\\text{{Balance}} = \\frac{{x[1 - (1+i)^{{-n_{{\\text{{remaining}}}}}}]}}{{i}} = \\frac{{{round(x, 2)}[1 - (1 + {_fmt_decimal_sa(i, 6)})^{{-{remaining_n}}}]}}{{{_fmt_decimal_sa(i, 6)}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="16_outstanding_balance_loan_backward_method",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{bal_rounded:.2f}", f"{bal_rounded:.2f}".replace(".", ","), str(round(bal))],
        learning_objective_id="G12-MATH-FIN-16",
        concept_id="loan_balance_backward_method",
        misconception_tags=["used_elapsed_months_instead_of_remaining_months"],
        hints=[
            f"Remaining months = 240 - {paid_months} = {remaining_n}.",
            r"Use Balance = \frac{x[1 - (1+i)^{-n_{\text{remaining}}}]}{i}.",
            f"Outstanding balance is {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b17_outstanding_balance_loan_forward_method(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"When using the **forward method** to determine the outstanding balance on a loan $P$ after $k$ payments, which formula is correctly applied?"
    )
    correct = r"\text{Balance} = P(1+i)^k - \frac{x[(1+i)^k - 1]}{i}"
    dist = [
        r"\text{Balance} = \frac{x[1 - (1+i)^{-k}]}{i}",
        r"\text{Balance} = P(1+i)^k - k \cdot x",
        r"\text{Balance} = \frac{x[(1+i)^k - 1]}{i} - P(1+i)^k",
    ]
    sol = (
        r"The forward method takes the accumulated loan value after $k$ months ($P(1+i)^k$) and subtracts the accumulated future value of all $k$ payments made ($\frac{x[(1+i)^k - 1]}{i}$)."
    )
    return _mcq(
        rng,
        subskill="17_outstanding_balance_loan_forward_method",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-17",
        concept_id="loan_balance_forward_method_formula",
        misconception_tags=["subtracted_uncompounded_payments_in_forward_method"],
        hints=[
            "The forward method looks from the past (T0) up to month k.",
            "Loan plus interest minus Future Value of payments made.",
            r"Formula: Balance = P(1+i)^k - \frac{x[(1+i)^k - 1]}{i}.",
        ],
        worked_solution=sol,
    )


def _b18_final_irregular_loan_payment(rng: random.Random) -> Dict[str, Any]:
    # Suppose loan is 50 000, installment is 1 500 at 12% p.a.
    # After 43 payments, find balance and add 1 month interest for final 44th payment
    bal_after_43 = 950.40
    i = 0.01  # 1% per month
    final_pmt = round(bal_after_43 * (1 + i), 2)
    ans = _fmt_zar(final_pmt)

    prompt = (
        f"A borrower owes an outstanding balance of {_fmt_zar(bal_after_43)} immediately after making the 43rd payment.\n"
        f"The interest rate is $12\\%$ p.a. compounded monthly ($1\\%$ per month).\n"
        f"Calculate the final 44th payment required to settle the loan balance in full one month later."
    )
    sol = (
        f"1. Interest accrues on the outstanding balance for one final month:\n"
        f"$$\\text{{Final Payment}} = \\text{{Balance}}_{{43}} \\times (1 + i) = {_fmt_zar(bal_after_43)} \\times (1 + 0{{,}}01) = {ans}$$"
    )
    return _typed(
        subskill="18_final_irregular_loan_payment",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{final_pmt:.2f}", f"{final_pmt:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-18",
        concept_id="final_irregular_payment",
        misconception_tags=["forgot_to_add_one_month_interest_to_final_payment"],
        hints=[
            "Remember that interest is charged during the final month on the remaining balance.",
            f"Multiply the remaining balance {_fmt_zar(bal_after_43)} by (1 + i).",
            f"Final payment is {ans}.",
        ],
        worked_solution=sol,
    )


def _b19_sinking_fund_scrap_value_reducing_balance(rng: random.Random) -> Dict[str, Any]:
    cost = rng.choice([350000, 450000, 600000])
    dep_rate = rng.choice([15, 18, 20])
    years = 5
    i = dep_rate / 100
    scrap = cost * (1 - i)**years
    scrap_rounded = round(scrap, 2)
    ans = _fmt_zar(scrap_rounded)

    prompt = (
        f"A company purchases heavy machinery for {_fmt_zar(cost)}.\n"
        f"The machinery depreciates at a rate of {dep_rate}\\% per annum on the **reducing-balance method**.\n"
        f"Calculate the scrap value (book value) of the machinery after {years} years."
    )
    sol = (
        f"1. State the reducing-balance depreciation formula:\n"
        f"$$A = P(1 - i)^n$$\n"
        f"2. Substitute $P = {_fmt_zar(cost)}$, $i = {_fmt_decimal_sa(i, 2)}$, $n = {years}$:\n"
        f"$$A = {cost}(1 - {_fmt_decimal_sa(i, 2)})^{{{years}}} = {cost}({_fmt_decimal_sa(1-i, 2)})^{{{years}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="19_sinking_fund_scrap_value_reducing_balance",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{scrap_rounded:.2f}", f"{scrap_rounded:.2f}".replace(".", ","), str(round(scrap))],
        learning_objective_id="G12-MATH-FIN-19",
        concept_id="reducing_balance_scrap_value",
        misconception_tags=["used_straight_line_depreciation"],
        hints=[
            r"Use reducing-balance formula: A = P(1 - i)^n.",
            f"Substitute P = {cost}, i = {dep_rate}/100, n = {years}.",
            f"Scrap value is {ans}.",
        ],
        worked_solution=sol,
    )


def _b20_sinking_fund_replacement_cost_inflation(rng: random.Random) -> Dict[str, Any]:
    cost = rng.choice([350000, 450000, 600000])
    inf_rate = rng.choice([6.0, 7.0, 8.0])
    years = 5
    i = inf_rate / 100
    repl = cost * (1 + i)**years
    repl_rounded = round(repl, 2)
    ans = _fmt_zar(repl_rounded)

    prompt = (
        f"New machinery currently costs {_fmt_zar(cost)}.\n"
        f"Inflation is expected to average {_fmt_decimal_sa(inf_rate)}\\% per annum over the next {years} years.\n"
        f"Calculate the estimated replacement cost of the machine in {years} years' time."
    )
    sol = (
        f"1. Apply compound interest inflation formula:\n"
        f"$$A = P(1 + i)^n$$\n"
        f"2. Substitute $P = {_fmt_zar(cost)}$, $i = {_fmt_decimal_sa(i, 2)}$, $n = {years}$:\n"
        f"$$A = {cost}(1 + {_fmt_decimal_sa(i, 2)})^{{{years}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="20_sinking_fund_replacement_cost_inflation",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{repl_rounded:.2f}", f"{repl_rounded:.2f}".replace(".", ","), str(round(repl))],
        learning_objective_id="G12-MATH-FIN-20",
        concept_id="replacement_cost_inflation",
        misconception_tags=["subtracted_inflation_instead_of_adding"],
        hints=[
            r"Use compound growth: A = P(1 + i)^n.",
            f"Substitute P = {cost}, i = {inf_rate}/100, n = {years}.",
            f"Replacement cost is {ans}.",
        ],
        worked_solution=sol,
    )


def _b21_sinking_fund_net_amount_required(rng: random.Random) -> Dict[str, Any]:
    cost = 500000
    scrap = 163840  # 500000 * 0.8^5
    repl = 734664   # 500000 * 1.08^5
    net_needed = repl - scrap
    ans = _fmt_zar(net_needed)

    prompt = (
        f"A factory will replace a machine in 5 years' time.\n"
        f"The estimated replacement cost is {_fmt_zar(repl)} and the trade-in / scrap value of the old machine will be {_fmt_zar(scrap)}.\n"
        f"Calculate the net amount that must be accumulated in the sinking fund."
    )
    sol = (
        f"1. Sinking Fund Target $= \\text{{Replacement Cost}} - \\text{{Scrap Value}}$\n"
        f"$$\\text{{Target}} = {_fmt_zar(repl)} - {_fmt_zar(scrap)} = {ans}$$"
    )
    return _typed(
        subskill="21_sinking_fund_net_amount_required",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, str(net_needed), f"{net_needed:.2f}"],
        learning_objective_id="G12-MATH-FIN-21",
        concept_id="sinking_fund_net_target",
        misconception_tags=["forgot_to_deduct_scrap_value"],
        hints=[
            "The trade-in/scrap value of the old machine offsets the cost of the new one.",
            "Net Sinking Fund Needed = Replacement Cost - Scrap Value.",
            f"Net target is {ans}.",
        ],
        worked_solution=sol,
        marks=2,
    )


def _b22_sinking_fund_monthly_deposit_calculation(rng: random.Random) -> Dict[str, Any]:
    target = 600000
    rate = 9.6
    years = 5
    n = years * 12
    i = (rate / 100) / 12
    x = target * i / ((1 + i)**n - 1)
    x_rounded = round(x, 2)
    ans = _fmt_zar(x_rounded)

    prompt = (
        f"A company needs to accumulate a net amount of {_fmt_zar(target)} in a sinking fund over {years} years.\n"
        f"The sinking fund earns interest at {_fmt_decimal_sa(rate)}\\% p.a. compounded monthly.\n"
        f"Calculate the monthly payment required into the sinking fund, starting in one month's time."
    )
    sol = (
        f"1. Sinking funds are Future Value annuities:\n"
        f"$$x = \\frac{{F \\cdot i}}{{(1+i)^n - 1}}$$\n"
        f"2. Substitute $F = {_fmt_zar(target)}$, $i = \\frac{{{rate}}}{{1200}}$, $n = {n}$:\n"
        f"$$x = \\frac{{{target} \\times {_fmt_decimal_sa(i, 6)}}}{{(1 + {_fmt_decimal_sa(i, 6)})^{{{n}}} - 1}} \\approx {ans}$$"
    )
    return _typed(
        subskill="22_sinking_fund_monthly_deposit_calculation",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{x_rounded:.2f}", f"{x_rounded:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-22",
        concept_id="sinking_fund_monthly_payment",
        misconception_tags=["used_present_value_for_sinking_fund"],
        hints=[
            "A sinking fund is a future savings fund, so use the Future Value formula.",
            f"Solve for x: x = F * i / ((1+i)^n - 1).",
            f"Monthly deposit is {ans}.",
        ],
        worked_solution=sol,
    )


def _b23_nominal_vs_effective_interest_rate_annual(rng: random.Random) -> Dict[str, Any]:
    nom_rate = rng.choice([10.0, 10.5, 11.0, 12.0])
    i_nom = nom_rate / 100
    # 1 + i_eff = (1 + i_nom / 12)^12
    i_eff = (1 + i_nom / 12)**12 - 1
    eff_pct = round(i_eff * 100, 2)
    ans = f"{eff_pct}%"
    ans_sa = f"{_fmt_decimal_sa(eff_pct)}\\%"

    prompt = (
        f"Convert a nominal interest rate of {_fmt_decimal_sa(nom_rate)}\\% per annum compounded monthly "
        f"to an effective annual interest rate, correct to 2 decimal places."
    )
    sol = (
        f"1. State the relationship between nominal and effective interest rates:\n"
        f"$$1 + i_{{\\text{{eff}}}} = \\left(1 + \\frac{{i_{{\\text{{nom}}}}}}{{m}}\\right)^m$$\n"
        f"2. Here $m = 12$ and $i_{{\\text{{nom}}}} = {_fmt_decimal_sa(i_nom, 4)}$:\n"
        f"$$1 + i_{{\\text{{eff}}}} = \\left(1 + \\frac{{{nom_rate}}}{{1200}}\\right)^{{12}} \\approx {round(1 + i_eff, 6)}$$\n"
        f"3. $i_{{\\text{{eff}}}} \\approx {_fmt_decimal_sa(i_eff, 4)} \\implies {ans_sa}$."
    )
    return _typed(
        subskill="23_nominal_vs_effective_interest_rate_annual",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{eff_pct}", f"{eff_pct:.2f}", f"{eff_pct:.2f}%", ans_sa],
        learning_objective_id="G12-MATH-FIN-23",
        concept_id="nominal_to_effective_rate_conversion",
        misconception_tags=["multiplied_instead_of_compounding_exponent"],
        hints=[
            r"Use the formula: 1 + i_{\text{eff}} = (1 + \frac{i_{\text{nom}}}{12})^{12}.",
            f"Subtract 1 and multiply by 100 to get percentage.",
            f"Effective annual rate is {eff_pct}%.",
        ],
        worked_solution=sol,
        marks=3,
    )


def _b24_effective_to_nominal_interest_rate_quarterly(rng: random.Random) -> Dict[str, Any]:
    eff_rate = 12.0
    i_eff = eff_rate / 100
    # (1 + i_nom / 4)^4 = 1 + i_eff => i_nom = 4 * ((1 + i_eff)^(1/4) - 1)
    i_nom = 4 * ((1 + i_eff)**0.25 - 1)
    nom_pct = round(i_nom * 100, 2)
    ans = f"{nom_pct}%"

    prompt = (
        f"An investment offers an effective interest rate of {_fmt_decimal_sa(eff_rate)}\\% per annum.\n"
        f"Calculate the equivalent nominal annual interest rate compounded quarterly, correct to 2 decimal places."
    )
    sol = (
        f"1. Relationship for quarterly compounding ($m = 4$):\n"
        f"$$\\left(1 + \\frac{{i_{{\\text{{nom}}}}}}{{4}}\\right)^4 = 1 + i_{{\\text{{eff}}}}$$\n"
        f"2. Solve for $i_{{\\text{{nom}}}}$:\n"
        f"$$\\frac{{i_{{\\text{{nom}}}}}}{{4}} = (1 + 0{{,}}12)^{{1/4}} - 1 \\implies i_{{\\text{{nom}}}} = 4\\left[(1{{,}}12)^{{0{{,}}25}} - 1\\right] \\approx {nom_pct}\\%$$"
    )
    return _typed(
        subskill="24_effective_to_nominal_interest_rate_quarterly",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{nom_pct}", f"{nom_pct:.2f}", f"{nom_pct:.2f}%"],
        learning_objective_id="G12-MATH-FIN-24",
        concept_id="effective_to_nominal_conversion",
        misconception_tags=["fourth_root_inversion_error"],
        hints=[
            r"Take the fourth root: 1 + \frac{i_{\text{nom}}}{4} = (1 + i_{\text{eff}})^{1/4}.",
            r"Subtract 1 and multiply by 4.",
            f"Nominal quarterly rate is {nom_pct}%.",
        ],
        worked_solution=sol,
        marks=3,
    )


def _b25_comparing_two_loan_options_total_cost(rng: random.Random) -> Dict[str, Any]:
    p = 100000
    # Option A: 4 years at 11% p.a.
    # Option B: 5 years at 10% p.a.
    r_a, r_b = 11.0, 10.0
    i_a = (r_a / 100) / 12
    i_b = (r_b / 100) / 12
    n_a, n_b = 48, 60
    x_a = p * i_a / (1 - (1 + i_a)**(-n_a))
    x_b = p * i_b / (1 - (1 + i_b)**(-n_b))
    tot_a = x_a * n_a
    tot_b = x_b * n_b
    diff = round(abs(tot_b - tot_a), 2)
    cheaper = "Option A" if tot_a < tot_b else "Option B"

    prompt = (
        f"A small business compares two financing options to borrow {_fmt_zar(p)}:\n"
        f"- Option A: Repay over 4 years at {int(r_a)}\\% p.a. compounded monthly (Monthly payment: {_fmt_zar(round(x_a, 2))})\n"
        f"- Option B: Repay over 5 years at {int(r_b)}\\% p.a. compounded monthly (Monthly payment: {_fmt_zar(round(x_b, 2))})\n"
        f"Which option has the lower total cost, and by how much is it cheaper?"
    )
    ans = f"{cheaper} by {_fmt_zar(diff)}"
    dist = [
        f"Option B by {_fmt_zar(diff)}",
        f"Option A by {_fmt_zar(round(diff * 1.5, 2))}",
        f"Both have equal total cost",
    ]
    sol = (
        f"1. Total repaid for Option A: $48 \\times {_fmt_zar(round(x_a, 2))} = {_fmt_zar(round(tot_a, 2))}$.\n"
        f"2. Total repaid for Option B: $60 \\times {_fmt_zar(round(x_b, 2))} = {_fmt_zar(round(tot_b, 2))}$.\n"
        f"3. Difference $= {_fmt_zar(round(tot_b, 2))} - {_fmt_zar(round(tot_a, 2))} = {_fmt_zar(diff)}$.\n"
        f"Therefore, {cheaper} is cheaper by {_fmt_zar(diff)}."
    )
    return _mcq(
        rng,
        subskill="25_comparing_two_loan_options_total_cost",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-25",
        concept_id="comparative_loan_cost_analysis",
        misconception_tags=["assumed_lower_monthly_payment_means_lower_total_cost"],
        hints=[
            "Calculate Total Cost = Monthly Payment * Number of Months for both options.",
            "Compare the two totals to find which is cheaper and by how much.",
            f"Option A is cheaper by {ans.split('by ')[-1]}.",
        ],
        worked_solution=sol,
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_future_value_annuity_monthly_investment": _b01_future_value_annuity_monthly_investment,
    "02_future_value_annuity_solve_monthly_deposit": _b02_future_value_annuity_solve_monthly_deposit,
    "03_future_value_annuity_solve_time_period_n_log": _b03_future_value_annuity_solve_time_period_n_log,
    "04_future_value_annuity_quarterly_compounding": _b04_future_value_annuity_quarterly_compounding,
    "05_future_value_payment_immediately_annuity_due": _b05_future_value_payment_immediately_annuity_due,
    "06_future_value_payment_starts_one_month_later": _b06_future_value_payment_starts_one_month_later,
    "07_future_value_final_payment_before_maturity": _b07_future_value_final_payment_before_maturity,
    "08_future_value_annuity_interest_rate_change": _b08_future_value_annuity_interest_rate_change,
    "09_future_value_with_lump_sum_withdrawal": _b09_future_value_with_lump_sum_withdrawal,
    "10_future_value_with_additional_lump_sum_deposit": _b10_future_value_with_additional_lump_sum_deposit,
    "11_present_value_annuity_home_loan_monthly_payment": _b11_present_value_annuity_home_loan_monthly_payment,
    "12_present_value_annuity_maximum_loan_affordable": _b12_present_value_annuity_maximum_loan_affordable,
    "13_present_value_annuity_solve_time_period_n_log": _b13_present_value_annuity_solve_time_period_n_log,
    "14_present_value_deferred_loan_repayment": _b14_present_value_deferred_loan_repayment,
    "15_loan_total_repayment_and_total_interest": _b15_loan_total_repayment_and_total_interest,
    "16_outstanding_balance_loan_backward_method": _b16_outstanding_balance_loan_backward_method,
    "17_outstanding_balance_loan_forward_method": _b17_outstanding_balance_loan_forward_method,
    "18_final_irregular_loan_payment": _b18_final_irregular_loan_payment,
    "19_sinking_fund_scrap_value_reducing_balance": _b19_sinking_fund_scrap_value_reducing_balance,
    "20_sinking_fund_replacement_cost_inflation": _b20_sinking_fund_replacement_cost_inflation,
    "21_sinking_fund_net_amount_required": _b21_sinking_fund_net_amount_required,
    "22_sinking_fund_monthly_deposit_calculation": _b22_sinking_fund_monthly_deposit_calculation,
    "23_nominal_vs_effective_interest_rate_annual": _b23_nominal_vs_effective_interest_rate_annual,
    "24_effective_to_nominal_interest_rate_quarterly": _b24_effective_to_nominal_interest_rate_quarterly,
    "25_comparing_two_loan_options_total_cost": _b25_comparing_two_loan_options_total_cost,
}
