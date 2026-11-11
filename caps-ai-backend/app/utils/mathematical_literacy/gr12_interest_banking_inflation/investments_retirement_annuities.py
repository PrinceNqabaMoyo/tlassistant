"""Subskills 33 to 40: Investments, retirement annuities, compound interest tables, tax deductions, and compounding horizons."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_pct,
)


def generate_33_retirement_annuity_table_row(r: random.Random) -> Dict[str, Any]:
    """Calculate the closing balance of an investment table row: (Opening + Payment) + Interest."""
    open_bal = r.choice([402.00, 806.01, 1214.04, 1626.11])
    pmt = 400.00
    bal_with_pmt = open_bal + pmt
    monthly_rate = 0.06 / 12.0  # 6% p.a. -> 0.5% per month
    interest_earned = bal_with_pmt * monthly_rate
    closing_bal = bal_with_pmt + interest_earned

    correct_ans = _fmt_curr(closing_bal)
    custom_options = [
        _fmt_curr(closing_bal),
        _fmt_curr(bal_with_pmt),
        _fmt_curr(closing_bal + pmt),
        _fmt_curr(closing_bal * 0.9),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a retirement annuity investment ledger earning 6,0% p.a. (0,5% per month):\n"
        f"• Month Opening Balance: {_fmt_curr(open_bal)}\n"
        f"• Monthly Contribution: {_fmt_curr(pmt)}\n\n"
        f"Calculate the Closing Balance for this month after interest is earned and credited to the account."
    )
    explanation = (
        f"Step 1: Balance with contribution = {_fmt_curr(open_bal)} + {_fmt_curr(pmt)} = {_fmt_curr(bal_with_pmt)} [M].\n"
        f"Step 2: Interest earned = {_fmt_curr(bal_with_pmt)} × 0,5% = {_fmt_curr(interest_earned)} [M].\n"
        f"Step 3: Closing Balance = {_fmt_curr(bal_with_pmt)} + {_fmt_curr(interest_earned)} = {_fmt_curr(closing_bal)} [A]."
    )
    return _build_question_payload(
        subskill_id="33_retirement_annuity_table_row",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the contribution to the opening balance, calculate 0,5% interest, and add it on.",
        tier_2=f"Balance with payment = {_fmt_curr(bal_with_pmt)}. Interest = {_fmt_curr(interest_earned)}.",
        tier_3=f"The closing balance is {_fmt_curr(closing_bal)}.",
        r=r,
    )


def generate_34_compounding_accelerating_growth(r: random.Random) -> Dict[str, Any]:
    """Explain why the investment curve accelerates upwards ('increasing at an increasing rate')."""
    correct_ans = "Compound growth: Each month, interest is earned on both the accumulated contributions and on all previous interest earned"

    custom_options = [
        correct_ans,
        "Simple growth: The monthly interest payment remains permanently fixed at R 2,00 per month",
        "Inflation bonus: The government supplements long-term pension funds with bonus grant deposits",
        "Linear growth: The balance increases in a perfect straight line indefinitely",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A graph tracking the value of a retirement annuity over 40 years starts with a gentle slope and curves "
        f"upward dramatically in the final 10 years, gaining more value between years 30 and 40 than in the first 30 years combined.\n\n"
        f"Explain the mathematical reason why compound investment growth accelerates upward so steeply over time."
    )
    explanation = (
        f"Step 1: In compound interest, growth is earned on the total current balance, not just the principal [M].\n"
        f"Step 2: As the balance expands, each percentage yield generates progressively larger monetary sums ('interest on interest') [M].\n"
        f"Step 3: This causes exponential growth ('increasing at an increasing rate') [A]."
    )
    return _build_question_payload(
        subskill_id="34_compounding_accelerating_growth",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about what happens to the interest earned every month.",
        tier_2="Because interest is reinvested, the capital base grows larger and larger each year.",
        tier_3="This creates compound growth: interest earning interest.",
        r=r,
    )


def generate_35_contributions_vs_accumulated_capital(r: random.Random) -> Dict[str, Any]:
    """Calculate total contributions made versus total interest earned in a long-term annuity."""
    pmt = 400.00
    months = 480  # 40 years
    total_invested = pmt * months
    final_fund_value = 800579.27
    total_interest_earned = final_fund_value - total_invested

    correct_ans = f"Total invested: {_fmt_curr(total_invested)}; Total interest earned: {_fmt_curr(total_interest_earned)}"
    custom_options = [
        correct_ans,
        f"Total invested: {_fmt_curr(final_fund_value)}; Total interest earned: {_fmt_curr(total_invested)}",
        f"Total invested: {_fmt_curr(total_invested)}; Total interest earned: {_fmt_curr(total_invested * 0.06)}",
        f"Total invested: {_fmt_curr(total_invested * 2)}; Total interest earned: {_fmt_curr(total_interest_earned / 2)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An individual contributed {_fmt_curr(pmt)} per month into a retirement fund for 40 years ({months} contributions).\n"
        f"Upon retiring at age 65, the fund had accumulated to {_fmt_curr(final_fund_value)}.\n\n"
        f"Calculate the total personal contributions paid in by the investor and the total interest generated by compound growth."
    )
    explanation = (
        f"Step 1: Total personal contributions = {months} × {_fmt_curr(pmt)} = {_fmt_curr(total_invested)} [M].\n"
        f"Step 2: Interest earned = Accumulated Value - Total Contributions = {_fmt_curr(final_fund_value)} - {_fmt_curr(total_invested)} [M].\n"
        f"Step 3: Total invested: {_fmt_curr(total_invested)}; Interest: {_fmt_curr(total_interest_earned)} [A]."
    )
    return _build_question_payload(
        subskill_id="35_contributions_vs_accumulated_capital",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the monthly payment by 480 months to find total contributions.",
        tier_2=f"Contributions: 480 × {_fmt_curr(pmt)} = {_fmt_curr(total_invested)}. Subtract this from the final fund value.",
        tier_3=f"Total invested: {_fmt_curr(total_invested)}; Total interest: {_fmt_curr(total_interest_earned)}.",
        r=r,
    )


def generate_36_compound_formula_monthly_compounding(r: random.Random) -> Dict[str, Any]:
    """Calculate future value of a lump-sum fixed deposit using A = P(1 + i)^n with monthly compounding."""
    p = r.choice([50000, 75000, 100000, 120000])
    annual_rate = r.choice([8.0, 9.0, 10.0])
    years = r.choice([3, 5])
    n_months = years * 12
    monthly_i = (annual_rate / 100.0) / 12.0

    accumulated = p * ((1.0 + monthly_i) ** n_months)
    correct_ans = _fmt_curr(accumulated)

    simple_growth = p * (1.0 + (annual_rate / 100.0) * years)
    custom_options = [
        _fmt_curr(accumulated),
        _fmt_curr(simple_growth),
        _fmt_curr(accumulated * 1.15),
        _fmt_curr(accumulated * 0.85),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A saver deposits a lump sum of {_fmt_curr(p)} into a 5-year fixed deposit account earning {_fmt_pct(annual_rate)} p.a. "
        f"interest compounded monthly for {years} years ({n_months} compounding periods).\n\n"
        f"Using the compound interest formula:\n"
        f"A = P(1 + i)^n\n"
        f"where i is the monthly interest rate and n is the total number of months, calculate the accumulated maturity value."
    )
    explanation = (
        f"Step 1: Calculate monthly interest i = {annual_rate}% ÷ 12 = {_fmt(monthly_i, 6)} [M].\n"
        f"Step 2: Total periods n = {years} × 12 = {n_months} [M].\n"
        f"Step 3: A = {_fmt_curr(p)} × (1 + {_fmt(monthly_i, 6)})^{n_months} = {_fmt_curr(accumulated)} [A]."
    )
    return _build_question_payload(
        subskill_id="36_compound_formula_monthly_compounding",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the monthly interest rate (annual rate ÷ 1200) and number of months (years × 12).",
        tier_2=f"Calculate {_fmt_curr(p)} × (1 + {annual_rate}/1200)^{n_months}.",
        tier_3=f"The maturity value is {_fmt_curr(accumulated)}.",
        r=r,
    )


def generate_37_comparing_simple_vs_compound(r: random.Random) -> Dict[str, Any]:
    """Compare investment returns of simple interest versus compound interest over 20 years."""
    p = 50000.00
    r_pct = 9.0
    years = 20

    simple_val = p * (1.0 + (r_pct / 100.0) * years)
    compound_val = p * ((1.0 + (r_pct / 100.0)) ** years)
    diff = compound_val - simple_val

    correct_ans = f"Compound interest yields {_fmt_curr(diff)} more than simple interest ({_fmt_curr(compound_val)} vs {_fmt_curr(simple_val)})"
    custom_options = [
        correct_ans,
        f"Simple interest yields {_fmt_curr(diff)} more because it avoids reinvestment risk",
        f"Both yield identical returns because the 9,0% annual rate is unchanged",
        f"Compound interest yields {_fmt_curr(diff * 2)} more due to quarterly dividend bonuses",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An investor compares two 20-year investment accounts for a {_fmt_curr(p)} deposit at {_fmt_pct(r_pct)} p.a.:\n"
        f"• Account A earns Simple Interest: A = P(1 + r × t)\n"
        f"• Account B earns Annual Compound Interest: A = P(1 + r)^t\n\n"
        f"Calculate the difference in accumulated value between the two accounts after 20 years."
    )
    explanation = (
        f"Step 1: Simple Interest = {_fmt_curr(p)} × (1 + 0,09 × 20) = {_fmt_curr(simple_val)} [M].\n"
        f"Step 2: Compound Interest = {_fmt_curr(p)} × (1 + 0,09)²⁰ = {_fmt_curr(compound_val)} [M].\n"
        f"Step 3: Difference = {_fmt_curr(compound_val)} - {_fmt_curr(simple_val)} = {_fmt_curr(diff)} [A]."
    )
    return _build_question_payload(
        subskill_id="37_comparing_simple_vs_compound",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the maturity value using the simple interest formula and the compound interest formula.",
        tier_2=f"Simple: {_fmt_curr(simple_val)}. Compound: {_fmt_curr(compound_val)}.",
        tier_3=f"Compound interest earns {_fmt_curr(diff)} more.",
        r=r,
    )


def generate_38_retirement_annuity_tax_deduction(r: random.Random) -> Dict[str, Any]:
    """Calculate taxable income reduction from retirement annuity contributions under Section 11F."""
    annual_income = r.choice([360000.00, 420000.00, 480000.00])
    monthly_ra = r.choice([2500.00, 3000.00, 3500.00])
    annual_ra = monthly_ra * 12
    max_deduction = 0.275 * annual_income  # 27.5% cap up to R350 000

    actual_deduction = min(annual_ra, max_deduction, 350000.00)
    taxable_income = annual_income - actual_deduction

    correct_ans = f"Deduction: {_fmt_curr(actual_deduction)}; Net Taxable Income: {_fmt_curr(taxable_income)}"
    custom_options = [
        correct_ans,
        f"Deduction: {_fmt_curr(monthly_ra)}; Net Taxable Income: {_fmt_curr(annual_income - monthly_ra)}",
        f"Deduction: R 0,00; Net Taxable Income: {_fmt_curr(annual_income)}",
        f"Deduction: {_fmt_curr(actual_deduction * 2)}; Net Taxable Income: {_fmt_curr(annual_income - actual_deduction * 2)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A taxpayer earns a gross annual remuneration of {_fmt_curr(annual_income)} and contributes {_fmt_curr(monthly_ra)} "
        f"every month to an approved Retirement Annuity (RA).\n"
        f"Under South African Income Tax rules (Section 11F), retirement contributions are tax-deductible up to a limit of 27,5% of gross income.\n\n"
        f"Calculate the total annual tax deduction and the taxpayer's resulting taxable income."
    )
    explanation = (
        f"Step 1: Total annual RA contributions = 12 × {_fmt_curr(monthly_ra)} = {_fmt_curr(annual_ra)} [M].\n"
        f"Step 2: Check 27,5% cap = 27,5% of {_fmt_curr(annual_income)} = {_fmt_curr(max_deduction)} (contributions are within cap) [M].\n"
        f"Step 3: Taxable Income = {_fmt_curr(annual_income)} - {_fmt_curr(actual_deduction)} = {_fmt_curr(taxable_income)} [A]."
    )
    return _build_question_payload(
        subskill_id="38_retirement_annuity_tax_deduction",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the monthly contribution by 12, then subtract it from the gross annual income.",
        tier_2=f"Annual RA = {_fmt_curr(annual_ra)}. Subtract from {_fmt_curr(annual_income)}.",
        tier_3=f"Deduction is {_fmt_curr(actual_deduction)}, reducing taxable income to {_fmt_curr(taxable_income)}.",
        r=r,
    )


def generate_39_fixed_deposit_tiered_rates(r: random.Random) -> Dict[str, Any]:
    """Calculate maturity value under tiered bank interest rates based on deposit size."""
    deposit = 120000.00
    # Tier: R 100 000+ earns 9.25% p.a., below earns 8.5%
    rate = 9.25
    years = 2
    maturity_val = deposit * ((1.0 + (rate / 100.0)) ** years)

    correct_ans = _fmt_curr(maturity_val)
    custom_options = [
        _fmt_curr(maturity_val),
        _fmt_curr(deposit * ((1.0 + 0.085) ** years)),
        _fmt_curr(deposit + (deposit * 0.0925 * years)),
        _fmt_curr(maturity_val * 1.1),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A bank offers tiered annual interest rates for 24-month fixed deposits:\n"
        f"• Deposits from R 10 000 to R 99 999: 8,50% p.a. compounded annually\n"
        f"• Deposits from R 100 000 and above: 9,25% p.a. compounded annually\n\n"
        f"Calculate the maturity value of a {_fmt_curr(deposit)} investment after 2 years."
    )
    explanation = (
        f"Step 1: Identify tier: {_fmt_curr(deposit)} qualifies for the higher rate of 9,25% p.a. [M].\n"
        f"Step 2: Compound formula: A = P(1 + r)² = {_fmt_curr(deposit)} × (1 + 0,0925)² [M].\n"
        f"Step 3: Maturity Value = {_fmt_curr(maturity_val)} [A]."
    )
    return _build_question_payload(
        subskill_id="39_fixed_deposit_tiered_rates",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine which interest rate tier applies to the R 120 000 deposit.",
        tier_2=f"Apply 9,25% compound interest for 2 years: {_fmt_curr(deposit)} × (1,0925)².",
        tier_3=f"The maturity value is {_fmt_curr(maturity_val)}.",
        r=r,
    )


def generate_40_delaying_savings_opportunity_cost(r: random.Random) -> Dict[str, Any]:
    """Calculate the opportunity cost of delaying retirement contributions by 10 years."""
    correct_ans = "Delaying by 10 years reduces final retirement wealth by more than 50% due to loss of the most powerful compounding years"

    custom_options = [
        correct_ans,
        "Delaying savings has zero impact because you can easily double your contributions in the final 2 years",
        "Starting later is more profitable because older savers qualify for higher senior citizen interest rates",
        "The fund will be identical because both savers contribute for the same number of days",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Two friends earn equal salaries. Saver A starts investing R 500 per month at age 25. "
        f"Saver B waits until age 35 to start investing R 500 per month. Both retire at age 65 earning 8% p.a. compound growth.\n\n"
        f"Explain from a compound interest perspective why Saver A accumulates more than double the wealth of Saver B."
    )
    explanation = (
        f"Step 1: Saver A benefits from 40 years of compounding versus 30 years for Saver B [M].\n"
        f"Step 2: In compound growth, the final decade produces the largest monetary leaps ('exponential curve') [M].\n"
        f"Step 3: Saver B loses 10 years of compounding that cannot be made up without massive increases in contributions [A]."
    )
    return _build_question_payload(
        subskill_id="40_delaying_savings_opportunity_cost",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about how compounding works over 40 years compared to 30 years.",
        tier_2="The extra 10 years at the end of the timeline produce enormous exponential gains.",
        tier_3="Starting 10 years earlier more than doubles final retirement capital.",
        r=r,
    )
