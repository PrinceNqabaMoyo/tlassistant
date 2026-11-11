"""Simple interest and linear investment growth (Subskills 1-9) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_1(r: random.Random) -> Dict[str, Any]:
    """Basic annual simple interest calculation (I = P × r × t)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([3000, 4500, 6000, 8000, 12000, 15000])
    rate = r.choice([6.5, 7.0, 7.5, 8.0, 8.5, 9.0])
    years = r.choice([2, 3, 4, 5])
    interest = round(principal * (rate / 100.0) * years, 2)
    ans_str = _fmt_curr(interest)

    prompt = (
        f"{name} invests {_fmt_curr(principal)} in a fixed notice savings account offering a simple interest rate of "
        f"{_fmt(rate)}% per annum for a period of {years} years.\n"
        f"Calculate the total simple interest earned over the {years} years.\n"
        f"*(Formula: I = P × r × t.)*"
    )
    explanation = (
        f"Step 1: State the simple interest formula:\n"
        f"I = P \\times r \\times t, \\text{{ where }} P = {principal}, r = {_fmt(rate)}\\% = {rate/100}, t = {years}. [1 mark]\n"
        f"Step 2: Substitute the values and calculate:\n"
        f"I = {principal} \\times {rate/100} \\times {years} = {interest:.2f} [1 mark]\n"
        f"Step 3: State the final interest amount:\n"
        f"\\text{{Total interest}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(principal * (rate / 100.0), 2)),
        _fmt_curr(round(principal + interest, 2)),
        _fmt_curr(round(interest * 1.5, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_1",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply the principal by the interest rate (as a decimal) and then by the number of years.",
        f"Calculate {principal} × {rate/100} × {years}.",
        f"Interest earned = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_2(r: random.Random) -> Dict[str, Any]:
    """Total accumulated amount under simple interest (A = P + I)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([5000, 7500, 10000, 14000, 20000])
    rate = r.choice([6.0, 7.5, 8.0, 9.0])
    years = r.choice([3, 4, 5])
    interest = round(principal * (rate / 100.0) * years, 2)
    accumulated = round(principal + interest, 2)
    ans_str = _fmt_curr(accumulated)

    prompt = (
        f"{name} deposits {_fmt_curr(principal)} into a {r.choice(SA_BANKS)} investment plan earning "
        f"{_fmt(rate)}% simple interest per year.\n"
        f"Calculate the total accumulated amount in the account at the end of {years} years.\n"
        f"*(Formula: A = P(1 + r × t).)*"
    )
    explanation = (
        f"Step 1: Calculate the simple interest earned:\n"
        f"I = {principal} \\times {rate/100} \\times {years} = {_fmt_curr(interest)}. [1 mark]\n"
        f"Step 2: Add the interest to the principal (A = P + I):\n"
        f"A = {principal} + {_fmt(interest)} = {accumulated:.2f} [1 mark]\n"
        f"Step 3: State the final accumulated balance:\n"
        f"\\text{{Accumulated amount}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(interest),
        _fmt_curr(round(accumulated + 1000, 2)),
        _fmt_curr(round(accumulated - 500, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_2",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate simple interest first, then add it to the initial principal.",
        f"Interest = {_fmt_curr(interest)}. Accumulated = {principal} + {_fmt(interest)}.",
        f"Total amount = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_3(r: random.Random) -> Dict[str, Any]:
    """Simple interest with time given in months (t = m / 12)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([4000, 6000, 9000, 12000])
    rate = 8.5
    months = r.choice([6, 9, 15, 18, 30])
    years_fraction = months / 12.0
    interest = round(principal * (rate / 100.0) * years_fraction, 2)
    ans_str = _fmt_curr(interest)

    prompt = (
        f"{name} invested {_fmt_curr(principal)} in a short-term money market facility at a simple interest rate of "
        f"{_fmt(rate)}% per annum for a term of {months} months.\n"
        f"Calculate the simple interest earned over this {months}-month period.\n"
        f"*(Note: Convert months to years by dividing by 12: t = {months} ÷ 12.)*"
    )
    explanation = (
        f"Step 1: Convert months to years:\n"
        f"t = \\frac{{{months}}}{{12}} = {_fmt(years_fraction)}\\text{{ years}}. [1 mark]\n"
        f"Step 2: Substitute into I = P × r × t:\n"
        f"I = {principal} \\times 0,085 \\times {_fmt(years_fraction)} = {interest:.2f} [1 mark]\n"
        f"Step 3: State the final interest:\n"
        f"\\text{{Interest earned}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(principal * (rate / 100.0) * months, 2)),
        _fmt_curr(round(interest * 1.5, 2)),
        _fmt_curr(round(principal + interest, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_3",
        prompt,
        ans_str,
        options,
        explanation,
        f"First convert {months} months to years ({months} ÷ 12), then apply I = P × r × t.",
        f"t = {months}/12 = {_fmt(years_fraction)}. Calculate {principal} × 0,085 × {_fmt(years_fraction)}.",
        f"Interest = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_4(r: random.Random) -> Dict[str, Any]:
    """Calculate principal P given interest earned and rate."""
    name = r.choice(SA_NAMES)
    principal = r.choice([4000, 5000, 8000, 10000, 15000])
    rate = r.choice([6.0, 7.5, 8.0, 10.0])
    years = r.choice([2, 3, 4])
    interest = round(principal * (rate / 100.0) * years, 2)
    ans_str = _fmt_curr(principal)

    prompt = (
        f"{name} invested a sum of money into a fixed deposit account earning {_fmt(rate)}% simple interest per year.\n"
        f"At the end of {years} years, the total simple interest earned was {_fmt_curr(interest)}.\n"
        f"Determine the initial principal amount that {name} invested.\n"
        f"*(Formula: P = I ÷ (r × t).)*"
    )
    explanation = (
        f"Step 1: Rearrange the simple interest formula to solve for P:\n"
        f"P = \\frac{{I}}{{r \\times t}}. [1 mark]\n"
        f"Step 2: Substitute given values:\n"
        f"P = \\frac{{{interest:.2f}}}{{{rate/100} \\times {years}}} = \\frac{{{interest:.2f}}}{{{(rate/100)*years:.4f}}} [1 mark]\n"
        f"Step 3: State the initial principal:\n"
        f"\\text{{Principal amount}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(principal * 1.25, 2)),
        _fmt_curr(round(principal * 0.75, 2)),
        _fmt_curr(round(interest * years, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_4",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the interest ({_fmt_curr(interest)}) by (rate × years).",
        f"Calculate {_fmt(interest)} ÷ ({rate/100} × {years}).",
        f"Principal = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_5(r: random.Random) -> Dict[str, Any]:
    """Calculate simple interest rate r given principal, interest earned, and term."""
    name = r.choice(SA_NAMES)
    principal = r.choice([5000, 8000, 10000, 12000, 16000])
    rate = r.choice([6.5, 7.0, 7.5, 8.0, 8.5, 9.0])
    years = r.choice([2, 3, 4])
    interest = round(principal * (rate / 100.0) * years, 2)
    ans_str = f"{_fmt(rate)}%"

    prompt = (
        f"{name} invested {_fmt_curr(principal)} for {years} years and received a total simple interest payout of {_fmt_curr(interest)}.\n"
        f"Calculate the annual simple interest rate (as a percentage per annum) earned on this investment.\n"
        f"*(Formula: r = (I ÷ (P × t)) × 100%.)*"
    )
    explanation = (
        f"Step 1: Rearrange the formula to solve for the rate r:\n"
        f"r = \\frac{{I}}{{P \\times t}} \\times 100\\%. [1 mark]\n"
        f"Step 2: Substitute values:\n"
        f"r = \\frac{{{interest:.2f}}}{{{principal} \\times {years}}} \\times 100\\% = \\frac{{{interest:.2f}}}{{{principal * years}}} \\times 100\\% [1 mark]\n"
        f"Step 3: State the final interest rate percentage:\n"
        f"\\text{{Annual interest rate}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(rate + 1.5)}%",
        f"{_fmt(rate - 1.0)}%",
        f"{_fmt(round(rate * 1.25, 1))}%",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_5",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide the interest by (principal × years), then multiply by 100%.",
        f"Calculate ({_fmt(interest)} ÷ ({principal} × {years})) × 100.",
        f"Rate = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_6(r: random.Random) -> Dict[str, Any]:
    """Calculate investment term t in years given principal and future amount."""
    name = r.choice(SA_NAMES)
    principal = 10000.0
    rate = 8.0
    years = r.choice([2, 3, 4, 5, 6])
    interest = round(principal * (rate / 100.0) * years, 2)
    accumulated = principal + interest
    ans_str = f"{years} years"

    prompt = (
        f"{name} deposited {_fmt_curr(principal)} into a special savings product paying {_fmt(rate)}% simple interest per year.\n"
        f"When {name} closed the account, the total accumulated balance was {_fmt_curr(accumulated)}.\n"
        f"For how many years was the money invested?"
    )
    explanation = (
        f"Step 1: Calculate the interest earned:\n"
        f"I = A - P = {_fmt(accumulated)} - 10\\,000 = {_fmt_curr(interest)}. [1 mark]\n"
        f"Step 2: Solve for time t using t = I ÷ (P × r):\n"
        f"t = \\frac{{{interest:.2f}}}{{10\\,000 \\times 0,08}} = \\frac{{{interest:.2f}}}{{800}} = {years} [1 mark]\n"
        f"Step 3: State the term in years:\n"
        f"\\text{{Investment term}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{years + 1} years",
        f"{max(1, years - 1)} years",
        f"{years + 2} years",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_6",
        prompt,
        ans_str,
        options,
        explanation,
        "Find the interest (A - P), then divide by (P × r).",
        f"Interest = {_fmt_curr(interest)}. Years = {_fmt(interest)} ÷ (10 000 × 0,08).",
        f"Term = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_7(r: random.Random) -> Dict[str, Any]:
    """Simple interest piecewise timeline with an additional deposit."""
    name = r.choice(SA_NAMES)
    p1 = 6000.0
    rate = 7.5
    years1 = 2
    extra_deposit = 4000.0
    years2 = 3

    # Period 1 interest
    i1 = p1 * (rate / 100.0) * years1
    # Period 2 principal and interest
    p2 = p1 + i1 + extra_deposit
    i2 = p2 * (rate / 100.0) * years2
    final_amount = round(p2 + i2, 2)
    ans_str = _fmt_curr(final_amount)

    prompt = (
        f"{name} opens an investment account with an initial deposit of {_fmt_curr(p1)} earning {_fmt(rate)}% simple interest per year.\n"
        f"After {years1} years, the accumulated balance is reinvested, and {name} deposits an additional {_fmt_curr(extra_deposit)}.\n"
        f"The new total remains invested for another {years2} years at the same simple interest rate.\n"
        f"Calculate the final accumulated balance in the account at the end of the 5 years."
    )
    explanation = (
        f"Step 1: Calculate the balance at the end of the first {years1} years:\n"
        f"\\text{{Interest 1}} = 6\\,000 \\times 0,075 \\times 2 = {_fmt_curr(i1)}\n"
        f"\\text{{Balance after 2 years}} = 6\\,000 + {_fmt(i1)} = {_fmt_curr(p1 + i1)}. [1 mark]\n"
        f"Step 2: Add the additional deposit to form the new principal for Period 2:\n"
        f"\\text{{New Principal}} = {_fmt(p1 + i1)} + 4\\,000 = {_fmt_curr(p2)}\n"
        f"\\text{{Interest 2}} = {_fmt(p2)} \\times 0,075 \\times 3 = {_fmt_curr(i2)}. [1 mark]\n"
        f"Step 3: Sum the new principal and Interest 2 for the final balance:\n"
        f"\\text{{Final Balance}} = {_fmt(p2)} + {_fmt(i2)} = {final_amount:.2f} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(p1 + extra_deposit + (p1 + extra_deposit) * 0.075 * 5, 2)),
        _fmt_curr(round(final_amount - 1200, 2)),
        _fmt_curr(round(final_amount + 1500, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_7",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the balance after 2 years, add R 4 000, then compute simple interest for the remaining 3 years.",
        f"Balance at yr 2 = {_fmt_curr(p1 + i1)}. New principal = {_fmt_curr(p2)}. Final balance = {_fmt_curr(p2)} + {_fmt_curr(i2)}.",
        f"Final balance = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_8(r: random.Random) -> Dict[str, Any]:
    """Linear graph interpretation of simple interest (reading vertical intercept and annual slope)."""
    principal = float(r.choice([4000, 5000, 6000, 8000]))
    rate = float(r.choice([5, 6, 8, 10]))
    annual_interest = principal * (rate / 100.0)
    ans_str = f"R {_fmt(principal)},00 (initial deposit) and R {_fmt(annual_interest)},00 (annual interest)"

    prompt = (
        f"Refer to the simple interest investment growth graph shown in the diagram:\n"
        f"• The vertical axis starts at R {_fmt(principal)},00 at time t = 0.\n"
        f"• At the end of Year 1 (t = 1), the balance reaches R {_fmt(principal + annual_interest)},00.\n"
        f"• At the end of Year 2 (t = 2), the balance reaches R {_fmt(principal + 2 * annual_interest)},00.\n\n"
        f"Identify the initial principal invested and the constant annual interest earned from the graph."
    )
    explanation = (
        f"Step 1: Identify the vertical intercept (t = 0):\n"
        f"At t = 0, the balance represents the initial principal P = R {_fmt(principal)},00. [1 mark]\n"
        f"Step 2: Calculate the constant rate of increase (slope of the line):\n"
        f"\\text{{Slope}} = {_fmt(principal + annual_interest)} - {_fmt(principal)} = {_fmt(annual_interest)}\\text{{ Rands/year}}. [1 mark]\n"
        f"Step 3: State the combined interpretation:\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"R {_fmt(annual_interest)},00 (initial deposit) and R {_fmt(principal)},00 (annual interest)",
        f"R {_fmt(principal + annual_interest)},00 (initial deposit) and R {_fmt(annual_interest)},00 (annual interest)",
        f"R {_fmt(principal)},00 (initial deposit) and R {_fmt(2 * annual_interest)},00 (annual interest)",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    d_spec = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"Simple Interest Growth Graph (Principal R {int(principal)})",
        "categories": ["Year 0", "Year 1", "Year 2", "Year 3"],
        "values": [int(principal), int(principal + annual_interest), int(principal + 2 * annual_interest), int(principal + 3 * annual_interest)],
    }
    return _build_question_payload(
        "subskill_8",
        prompt,
        ans_str,
        options,
        explanation,
        "The value at t = 0 is the principal; the yearly jump is the annual simple interest.",
        f"Initial principal = R {_fmt(principal)}, annual interest = R {_fmt(annual_interest)}.",
        f"Result = {ans_str}.",
        r,
        difficulty="easy",
        diagram_spec=d_spec,
    )


def generate_subskill_9(r: random.Random) -> Dict[str, Any]:
    """Comparing two simple interest investment accounts with different rates and terms."""
    principal = 10000.0
    # Option A: 8,5% for 3 years
    rate_a = 8.5
    years_a = 3
    interest_a = round(principal * (rate_a / 100.0) * years_a, 2)

    # Option B: 7,0% for 4 years
    rate_b = 7.0
    years_b = 4
    interest_b = round(principal * (rate_b / 100.0) * years_b, 2)

    diff = abs(interest_b - interest_a)
    better_opt = "Option B" if interest_b > interest_a else "Option A"
    ans_str = f"{better_opt} by {_fmt_curr(diff)}"

    prompt = (
        f"An investor has {_fmt_curr(principal)} to invest and compares two simple interest bank options:\n"
        f"• Option A: {_fmt(rate_a)}% simple interest per year for {years_a} years\n"
        f"• Option B: {_fmt(rate_b)}% simple interest per year for {years_b} years\n\n"
        f"Which option yields more total interest, and by how much?"
    )
    explanation = (
        f"Step 1: Calculate total interest for Option A:\n"
        f"\\text{{Interest A}} = 10\\,000 \\times {rate_a/100} \\times {years_a} = {_fmt_curr(interest_a)}. [1 mark]\n"
        f"Step 2: Calculate total interest for Option B:\n"
        f"\\text{{Interest B}} = 10\\,000 \\times {rate_b/100} \\times {years_b} = {_fmt_curr(interest_b)}. [1 mark]\n"
        f"Step 3: Compare and find the difference:\n"
        f"{_fmt(interest_b)} - {_fmt(interest_a)} = {diff:.2f}.\n"
        f"\\text{{Outcome}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{'Option A' if better_opt == 'Option B' else 'Option B'} by {_fmt_curr(diff)}",
        f"{better_opt} by {_fmt_curr(round(diff * 1.5, 2))}",
        "Both options yield the exact same interest",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_9",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate simple interest for both options and compare the results.",
        f"A = {_fmt_curr(interest_a)}, B = {_fmt_curr(interest_b)}. Difference = {_fmt_curr(diff)}.",
        f"Conclusion = {ans_str}.",
        r,
        difficulty="medium",
    )
