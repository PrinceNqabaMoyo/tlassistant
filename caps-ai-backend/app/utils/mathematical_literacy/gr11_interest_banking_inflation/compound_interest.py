"""Compound interest, multi-period compounding, and exponential growth (Subskills 10-18) for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_BANKS,
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Step-by-step annual compound interest manual calculation without formula."""
    name = r.choice(SA_NAMES)
    principal = r.choice([5000, 8000, 10000, 12000])
    rate = r.choice([8.0, 10.0])
    factor = 1.0 + (rate / 100.0)

    # Year 1
    int_1 = round(principal * (rate / 100.0), 2)
    end_1 = round(principal + int_1, 2)
    # Year 2
    int_2 = round(end_1 * (rate / 100.0), 2)
    end_2 = round(end_1 + int_2, 2)
    # Year 3
    int_3 = round(end_2 * (rate / 100.0), 2)
    end_3 = round(end_2 + int_3, 2)

    ans_str = _fmt_curr(end_3)

    prompt = (
        f"{name} invests {_fmt_curr(principal)} in a 3-year fixed deposit account paying {_fmt(rate)}% interest compounded annually.\n"
        f"Perform the calculation step-by-step for each year (without using the compound interest formula):\n"
        f"• End of Year 1 balance\n"
        f"• End of Year 2 balance\n"
        f"• End of Year 3 balance\n\n"
        f"What is the final balance in the account at the end of Year 3?"
    )
    explanation = (
        f"Step 1: Calculate Year 1 interest and closing balance:\n"
        f"\\text{{Year 1 Interest}} = {principal} \\times {rate/100} = {_fmt_curr(int_1)}\n"
        f"\\text{{End Year 1}} = {principal} + {_fmt(int_1)} = {_fmt_curr(end_1)}. [1 mark]\n"
        f"Step 2: Calculate Year 2 interest and closing balance (compounding on Year 1 balance):\n"
        f"\\text{{Year 2 Interest}} = {_fmt(end_1)} \\times {rate/100} = {_fmt_curr(int_2)}\n"
        f"\\text{{End Year 2}} = {_fmt(end_1)} + {_fmt(int_2)} = {_fmt_curr(end_2)}. [1 mark]\n"
        f"Step 3: Calculate Year 3 interest and final balance:\n"
        f"\\text{{Year 3 Interest}} = {_fmt(end_2)} \\times {rate/100} = {_fmt_curr(int_3)}\n"
        f"\\text{{End Year 3}} = {_fmt(end_2)} + {_fmt(int_3)} = {end_3:.2f} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(principal + (int_1 * 3), 2)),  # Simple interest distractor
        _fmt_curr(round(end_2, 2)),
        _fmt_curr(round(end_3 + 500, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_10",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate interest each year and add it to the balance before calculating next year's interest.",
        f"Yr 1: {_fmt_curr(end_1)}. Yr 2: {_fmt_curr(end_2)}. Yr 3: {_fmt_curr(end_3)}.",
        f"Final balance = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Compound interest using formula A = P(1 + i)^n annually."""
    name = r.choice(SA_NAMES)
    principal = r.choice([8000, 10000, 15000, 20000, 25000])
    rate = r.choice([7.0, 7.5, 8.0, 8.5, 9.0])
    years = r.choice([3, 4, 5])
    amount = round(principal * ((1.0 + (rate / 100.0)) ** years), 2)
    ans_str = _fmt_curr(amount)

    prompt = (
        f"{name} deposits {_fmt_curr(principal)} into a growth investment fund paying {_fmt(rate)}% per annum "
        f"compounded annually for {years} years.\n"
        f"Calculate the total accumulated value of the investment at the end of {years} years.\n"
        f"*(Formula: A = P(1 + i)^n. Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: State the formula and identify parameters:\n"
        f"A = P(1 + i)^n, \\text{{ where }} P = {principal}, i = {_fmt(rate)}\\% = {rate/100}, n = {years}. [1 mark]\n"
        f"Step 2: Substitute values:\n"
        f"A = {principal}(1 + {rate/100})^{years} = {principal}({1 + rate/100:.4f})^{years} [1 mark]\n"
        f"Step 3: Evaluate and state final amount:\n"
        f"\\text{{Accumulated value}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(principal * (1.0 + (rate / 100.0) * years), 2)),  # Simple interest
        _fmt_curr(round(amount * 1.1, 2)),
        _fmt_curr(round(amount - 800, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_11",
        prompt,
        ans_str,
        options,
        explanation,
        f"Substitute into A = P(1 + i)^n: {principal} × (1 + {rate/100})^{years}.",
        f"Calculate {principal} × ({1 + rate/100})^{years}.",
        f"Accumulated value = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Total compound interest earned (I = A - P)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([10000, 12000, 16000, 20000])
    rate = 8.0
    years = r.choice([3, 4])
    amount = round(principal * ((1.0 + (rate / 100.0)) ** years), 2)
    interest = round(amount - principal, 2)
    ans_str = _fmt_curr(interest)

    prompt = (
        f"{name} invested {_fmt_curr(principal)} in a compound interest savings account for {years} years at "
        f"{_fmt(rate)}% per annum compounded annually.\n"
        f"Calculate the total interest earned over the {years} years.\n"
        f"*(Formula: I = A - P, where A = P(1 + i)^n.)*"
    )
    explanation = (
        f"Step 1: Calculate the total accumulated amount A:\n"
        f"A = {principal}(1 + 0,08)^{years} = {_fmt_curr(amount)}. [1 mark]\n"
        f"Step 2: Subtract the principal from the accumulated amount (I = A - P):\n"
        f"I = {_fmt(amount)} - {principal} = {interest:.2f} [1 mark]\n"
        f"Step 3: State the total compound interest earned:\n"
        f"\\text{{Interest earned}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(amount),
        _fmt_curr(round(principal * 0.08 * years, 2)),  # Simple interest
        _fmt_curr(round(interest + 350, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_12",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate accumulated amount A first, then subtract initial principal P.",
        f"A = {_fmt_curr(amount)}. Interest = {_fmt(amount)} - {principal}.",
        f"Interest = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Semi-annual (half-yearly) compounding (i = r / 2, n = t × 2)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([10000, 15000, 20000, 25000])
    annual_rate = 8.0
    half_rate = annual_rate / 2.0  # 4% per half year
    years = r.choice([2, 3])
    periods = years * 2
    amount = round(principal * ((1.0 + (half_rate / 100.0)) ** periods), 2)
    ans_str = _fmt_curr(amount)

    prompt = (
        f"{name} deposited {_fmt_curr(principal)} into a fixed deposit that pays an annual interest rate of "
        f"{_fmt(annual_rate)}% compounded half-yearly (semi-annually) for {years} years.\n"
        f"Calculate the accumulated balance in the account at the end of {years} years.\n"
        f"*(Given: Compounding half-yearly means interest is calculated twice a year: i = 8% ÷ 2 = 4% per half year; n = {years} × 2 = {periods} periods.)*"
    )
    explanation = (
        f"Step 1: Determine the periodic interest rate and number of compounding periods:\n"
        f"i = \\frac{{8\\%}}{{2}} = 4\\% = 0,04; n = {years} \\times 2 = {periods}. [1 mark]\n"
        f"Step 2: Substitute into the formula A = P(1 + i)^n:\n"
        f"A = {principal}(1 + 0,04)^{{{periods}}} = {principal}(1,04)^{{{periods}}} [1 mark]\n"
        f"Step 3: State the final accumulated balance:\n"
        f"\\text{{Accumulated balance}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(principal * ((1.0 + 0.08) ** years), 2)),  # Annual compounding
        _fmt_curr(round(amount * 1.1, 2)),
        _fmt_curr(round(amount - 600, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_13",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the annual rate by 2 (4%) and multiply years by 2 ({periods} periods).",
        f"Calculate {principal} × (1,04)^{periods}.",
        f"Final balance = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Quarterly compounding (i = r / 4, n = t × 4)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([12000, 16000, 20000, 30000])
    annual_rate = 10.0
    quarter_rate = annual_rate / 4.0  # 2.5% per quarter
    years = 2
    periods = years * 4  # 8 quarters
    amount = round(principal * ((1.0 + (quarter_rate / 100.0)) ** periods), 2)
    ans_str = _fmt_curr(amount)

    prompt = (
        f"{name} invests {_fmt_curr(principal)} in a corporate money market fund with an interest rate of "
        f"{_fmt(annual_rate)}% per annum compounded quarterly for {years} years.\n"
        f"Calculate the accumulated value of the investment after {years} years.\n"
        f"*(Given: Compounding quarterly means interest is calculated 4 times a year: i = 10% ÷ 4 = 2,5% per quarter; n = {years} × 4 = {periods} quarters.)*"
    )
    explanation = (
        f"Step 1: Calculate periodic rate i and total quarters n:\n"
        f"i = \\frac{{10\\%}}{{4}} = 2,5\\% = 0,025; n = {years} \\times 4 = {periods}\\text{{ quarters}}. [1 mark]\n"
        f"Step 2: Substitute into A = P(1 + i)^n:\n"
        f"A = {principal}(1 + 0,025)^8 = {principal}(1,025)^8 [1 mark]\n"
        f"Step 3: State the rounded final accumulated balance:\n"
        f"\\text{{Accumulated value}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(principal * ((1.0 + 0.10) ** years), 2)),
        _fmt_curr(round(amount * 1.1, 2)),
        _fmt_curr(round(amount - 500, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_14",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide annual rate by 4 (2,5%) and multiply years by 4 (8 quarters).",
        f"Calculate {principal} × (1,025)^8.",
        f"Accumulated value = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Monthly compounding on fixed savings account (i = r / 12, n = t × 12)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([10000, 15000, 20000])
    annual_rate = 12.0  # 1% per month
    month_rate = annual_rate / 12.0  # 1.0% per month
    years = r.choice([1, 2])
    months = years * 12
    amount = round(principal * ((1.0 + (month_rate / 100.0)) ** months), 2)
    ans_str = _fmt_curr(amount)

    prompt = (
        f"{name} places {_fmt_curr(principal)} into a 32-day notice deposit account at {r.choice(SA_BANKS)} paying "
        f"{_fmt(annual_rate)}% per annum compounded monthly for {years} year(s).\n"
        f"Calculate the accumulated value at the end of the investment term.\n"
        f"*(Given: Monthly compounding rate i = 12% ÷ 12 = 1% per month; n = {months} months.)*"
    )
    explanation = (
        f"Step 1: Determine monthly interest rate and number of months:\n"
        f"i = \\frac{{12\\%}}{{12}} = 1\\% = 0,01; n = {months}\\text{{ months}}. [1 mark]\n"
        f"Step 2: Substitute into A = P(1 + i)^n:\n"
        f"A = {principal}(1 + 0,01)^{{{months}}} = {principal}(1,01)^{{{months}}} [1 mark]\n"
        f"Step 3: State the final accumulated balance:\n"
        f"\\text{{Accumulated balance}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(principal * (1.0 + (annual_rate / 100.0) * years), 2)),  # Simple
        _fmt_curr(round(amount * 1.15, 2)),
        _fmt_curr(round(amount - 400, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_15",
        prompt,
        ans_str,
        options,
        explanation,
        f"Calculate with 1% monthly interest over {months} months: {principal} × (1,01)^{months}.",
        f"Calculate {principal} × (1,01)^{months}.",
        f"Balance = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Compound interest curve graph interpretation (exponential growth vs linear)."""
    prompt = (
        "When comparing graphs of simple interest and compound interest plotted against time (in years):\n\n"
        "Which of the following descriptions accurately characterizes the graphical behavior of compound interest?"
    )
    correct = (
        "It forms an upward-curving exponential graph that increases at an increasing rate over time."
    )
    distractors = [
        "It forms a straight horizontal line that remains constant over time.",
        "It forms a straight line with a constant slope and identical annual increments.",
        "It forms a step-function graph that decreases with transaction volume.",
    ]
    options, _ = _build_options(correct, r, [correct] + distractors)
    explanation = (
        "Step 1: Understand the nature of simple vs compound growth:\n"
        "Simple interest increases by the exact same Rand amount every year, forming a straight line (linear). [1 mark]\n"
        "Step 2: Contrast with compound interest:\n"
        "In compound interest, interest is earned on both the principal and previously accumulated interest, "
        "causing the balance to grow at an increasing rate each year. [1 mark]\n"
        "Step 3: Conclude the correct statement:\n"
        f"\\text{{Conclusion}} = {correct}. [1 mark]"
    )
    return _build_question_payload(
        "subskill_16",
        prompt,
        correct,
        options,
        explanation,
        "Recall that compound interest grows faster and faster because interest earns interest.",
        "Compound interest is an exponential curve increasing at an increasing rate.",
        f"Correct description = {correct}.",
        r,
        difficulty="easy",
    )


def generate_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Side-by-side comparison: Simple interest vs compound interest on the same principal over 5 years."""
    name = r.choice(SA_NAMES)
    principal = 20000.0
    rate = 8.0
    years = 5

    # Simple interest
    simple_total = principal * (1.0 + (rate / 100.0) * years)
    # Compound interest
    compound_total = round(principal * ((1.0 + (rate / 100.0)) ** years), 2)
    difference = round(compound_total - simple_total, 2)
    ans_str = f"Compound interest by {_fmt_curr(difference)}"

    prompt = (
        f"{name} is deciding between two investment products for a lump sum of {_fmt_curr(principal)} over a 5-year period:\n"
        f"• Product A: 8,0% per annum simple interest\n"
        f"• Product B: 8,0% per annum compound interest (compounded annually)\n\n"
        f"Which product yields a higher return at the end of 5 years, and by how much?"
    )
    explanation = (
        f"Step 1: Calculate the accumulated value for Product A (Simple Interest):\n"
        f"A_{{simple}} = 20\\,000(1 + 0,08 \\times 5) = 20\\,000 \\times 1,40 = {_fmt_curr(simple_total)}. [1 mark]\n"
        f"Step 2: Calculate the accumulated value for Product B (Compound Interest):\n"
        f"A_{{compound}} = 20\\,000(1 + 0,08)^5 = 20\\,000 \\times 1,469328 = {_fmt_curr(compound_total)}. [1 mark]\n"
        f"Step 3: Subtract to find the extra return from compound interest:\n"
        f"{_fmt(compound_total)} - {_fmt(simple_total)} = {difference:.2f}.\n"
        f"\\text{{Outcome}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Simple interest by {_fmt_curr(difference)}",
        f"Compound interest by {_fmt_curr(round(difference * 1.5, 2))}",
        "Both products yield the exact same return after 5 years",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_17",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate simple interest and compound interest for R 20 000 over 5 years and subtract.",
        f"Simple = {_fmt_curr(simple_total)}. Compound = {_fmt_curr(compound_total)}. Difference = {_fmt_curr(difference)}.",
        f"Result = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Calculate required starting investment (present value) to achieve a future target under compound interest."""
    name = r.choice(SA_NAMES)
    target_amount = 50000.0
    rate = 8.0
    years = 3
    # P = A / (1 + i)^n
    factor = (1.0 + (rate / 100.0)) ** years
    present_value = round(target_amount / factor, 2)
    ans_str = _fmt_curr(present_value)

    prompt = (
        f"{name} wants to have {_fmt_curr(target_amount)} saved in 3 years' time to pay for college fees.\n"
        f"An investment account offers a guaranteed compound interest rate of 8,0% per annum compounded annually.\n"
        f"Calculate the initial lump sum (principal) that {name} must deposit today to achieve this target.\n"
        f"*(Formula: P = A ÷ (1 + i)^n. Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: State the formula for present value P:\n"
        f"P = \\frac{{A}}{{(1 + i)^n}}, \\text{{ where }} A = 50\\,000, i = 0,08, n = 3. [1 mark]\n"
        f"Step 2: Calculate the compounding denominator:\n"
        f"(1 + 0,08)^3 = (1,08)^3 \\approx {factor:.6f} [1 mark]\n"
        f"Step 3: Divide to find the required deposit:\n"
        f"P = \\frac{{50\\,000}}{{{factor:.6f}}} = {present_value:.2f} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(target_amount * (1.0 - 0.08 * 3), 2)),
        _fmt_curr(round(present_value + 3000, 2)),
        _fmt_curr(round(present_value - 3000, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_18",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide the future target of R 50 000 by (1,08)^3.",
        f"Calculate 50 000 ÷ (1,08)^3.",
        f"Required deposit = {ans_str}.",
        r,
        difficulty="hard",
    )
