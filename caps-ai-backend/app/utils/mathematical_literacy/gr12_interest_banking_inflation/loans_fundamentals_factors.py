"""Subskills 01 to 08: Loan fundamentals, deposits, monthly rates, repayment factors, and real cost."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    LOAN_FACTOR_TABLE,
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_pct,
)


def generate_01_deposit_and_net_loan(r: random.Random) -> Dict[str, Any]:
    """Calculate the deposit and resultant net loan principal amount."""
    name = r.choice(SA_NAMES)
    sale_price = r.choice([750000, 850000, 895000, 950000, 1200000])
    dep_pct = r.choice([10, 15, 20])
    deposit = (dep_pct / 100) * sale_price
    loan_principal = sale_price - deposit

    d_spec_01 = {
        "diagram_role": "context",
        "kind": "pie_chart",
        "title": f"Property Financing ({_fmt_curr(sale_price)})",
        "slices": [
            {"name": "Deposit", "value": deposit},
            {"name": "Loan Principal", "value": loan_principal},
        ],
    }

    correct_ans = f"Deposit: {_fmt_curr(deposit)}; Loan Principal: {_fmt_curr(loan_principal)}"
    custom_options = [
        f"Deposit: {_fmt_curr(deposit)}; Loan Principal: {_fmt_curr(loan_principal)}",
        f"Deposit: {_fmt_curr(deposit * 1.2)}; Loan Principal: {_fmt_curr(sale_price)}",
        f"Deposit: {_fmt_curr(deposit * 0.8)}; Loan Principal: {_fmt_curr(loan_principal + deposit * 0.2)}",
        f"Deposit: {_fmt_curr(sale_price - deposit)}; Loan Principal: {_fmt_curr(deposit)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the property financing scheme with a selling price of {_fmt_curr(sale_price)} for {name}.\n"
        f"The mortgage lender requires a mandatory upfront cash deposit of {dep_pct}% before approving the bond.\n\n"
        f"Calculate the deposit required and the resulting net loan amount (principal borrowed) to be financed."
    )
    explanation = (
        f"Step 1: Calculate deposit = {dep_pct}% of {_fmt_curr(sale_price)} = {_fmt_curr(deposit)} [M].\n"
        f"Step 2: Calculate loan principal = Sale Price - Deposit = {_fmt_curr(sale_price)} - {_fmt_curr(deposit)} = {_fmt_curr(loan_principal)} [M].\n"
        f"Step 3: Deposit: {_fmt_curr(deposit)}; Loan Principal: {_fmt_curr(loan_principal)} [A]."
    )
    return _build_question_payload(
        subskill_id="01_deposit_and_net_loan",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="First find the deposit amount by calculating the required percentage of the sale price.",
        tier_2=f"Calculate {dep_pct}% of {_fmt_curr(sale_price)}.",
        tier_3=f"Subtract the deposit ({_fmt_curr(deposit)}) from {_fmt_curr(sale_price)} to find the net loan: {_fmt_curr(loan_principal)}.",
        r=r,
        diagram_spec=d_spec_01,
    )


def generate_02_monthly_interest_rate(r: random.Random) -> Dict[str, Any]:
    """Convert an annual nominal mortgage interest rate to an equivalent monthly percentage."""
    annual_rate = r.choice([10.5, 11.0, 11.5, 11.75, 12.0])
    monthly_rate = annual_rate / 12.0

    correct_ans = f"{_fmt(monthly_rate, 4)}% per month (or {_fmt(monthly_rate, 2)}% rounded)"
    custom_options = [
        f"{_fmt(monthly_rate, 4)}% per month (or {_fmt(monthly_rate, 2)}% rounded)",
        f"{_fmt(annual_rate, 2)}% per month (or {_fmt(annual_rate, 1)}% rounded)",
        f"{_fmt(monthly_rate * 2, 4)}% per month (or {_fmt(monthly_rate * 2, 2)}% rounded)",
        f"{_fmt(monthly_rate / 2, 4)}% per month (or {_fmt(monthly_rate / 2, 2)}% rounded)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A commercial bank quotes a home loan interest rate of {_fmt_pct(annual_rate)} per annum (p.a.) compounded monthly.\n\n"
        f"Calculate the effective monthly interest rate applied to the loan account balance at the end of each month."
    )
    explanation = (
        f"Step 1: Recall the formula for monthly interest rate: Monthly rate = Annual rate ÷ 12 [M].\n"
        f"Step 2: Substitute: {_fmt_pct(annual_rate)} ÷ 12 [M].\n"
        f"Step 3: Monthly rate = {_fmt(monthly_rate, 4)}% per month [A]."
    )
    return _build_question_payload(
        subskill_id="02_monthly_interest_rate",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the annual percentage interest rate by 12 months.",
        tier_2=f"Calculate {_fmt_pct(annual_rate)} ÷ 12.",
        tier_3=f"The monthly rate is {_fmt(monthly_rate, 4)}% per month.",
        r=r,
    )


def generate_03_first_month_interest_charge(r: random.Random) -> Dict[str, Any]:
    """Calculate the opening interest charge for the first month of a loan."""
    principal = r.choice([600000, 750000, 800000, 920000, 1050000])
    annual_rate = r.choice([10.5, 11.0, 11.5, 12.0])
    first_month_interest = principal * (annual_rate / 100.0) / 12.0

    correct_ans = _fmt_curr(first_month_interest)
    custom_options = [
        _fmt_curr(first_month_interest),
        _fmt_curr(principal * (annual_rate / 100.0)),
        _fmt_curr(first_month_interest * 1.15),
        _fmt_curr(first_month_interest * 0.85),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A borrower secures a home loan with a starting principal of {_fmt_curr(principal)} at an interest rate "
        f"of {_fmt_pct(annual_rate)} p.a. compounded monthly.\n\n"
        f"Calculate the interest charged to the loan account at the end of the very first month, before any repayment is deducted."
    )
    explanation = (
        f"Step 1: Monthly interest formula: Interest = Opening Balance × (Annual Rate ÷ 12) [M].\n"
        f"Step 2: Substitute: {_fmt_curr(principal)} × ({annual_rate}% ÷ 12) = {_fmt_curr(principal)} × {_fmt(annual_rate/1200.0, 6)} [M].\n"
        f"Step 3: First month interest = {_fmt_curr(first_month_interest)} [A]."
    )
    return _build_question_payload(
        subskill_id="03_first_month_interest_charge",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the loan principal by the annual interest rate, then divide by 12.",
        tier_2=f"Calculate {_fmt_curr(principal)} × ({annual_rate} / 100) ÷ 12.",
        tier_3=f"The first month's interest charge is {_fmt_curr(first_month_interest)}.",
        r=r,
    )


def generate_04_reading_repayment_factor(r: random.Random) -> Dict[str, Any]:
    """Read the correct monthly repayment factor from a standard loan table."""
    term_years = r.choice([15, 20, 25, 30])
    rate = r.choice([10.0, 10.5, 11.0, 11.5])
    factor = LOAN_FACTOR_TABLE[term_years][rate]

    correct_ans = f"{_fmt(factor, 2)} per R 1 000 borrowed"
    distractor_factors = [
        LOAN_FACTOR_TABLE[15 if term_years != 15 else 20][rate],
        LOAN_FACTOR_TABLE[term_years][10.0 if rate != 10.0 else 11.0],
        LOAN_FACTOR_TABLE[30 if term_years != 30 else 25][rate],
    ]
    custom_options = [correct_ans] + [f"{_fmt(df, 2)} per R 1 000 borrowed" for df in distractor_factors]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A bank provides the following monthly repayment factors (per R 1 000 borrowed):\n\n"
        f"| Loan Period | 10,0% | 10,5% | 11,0% | 11,5% |\n"
        f"|---|---|---|---|---|\n"
        f"| 15 years | 10,75 | 11,05 | 11,37 | 11,68 |\n"
        f"| 20 years | 9,65 | 9,98 | 10,32 | 10,66 |\n"
        f"| 25 years | 9,09 | 9,44 | 9,80 | 10,17 |\n"
        f"| 30 years | 8,78 | 9,15 | 9,52 | 9,90 |\n\n"
        f"Read and state the monthly repayment factor for a loan with a repayment term of {term_years} years "
        f"at an annual interest rate of {_fmt_pct(rate)}."
    )
    explanation = (
        f"Step 1: Locate the row corresponding to a loan period of {term_years} years [M].\n"
        f"Step 2: Locate the column for an interest rate of {_fmt_pct(rate)} [M].\n"
        f"Step 3: The intersection value is {_fmt(factor, 2)} [A]."
    )
    return _build_question_payload(
        subskill_id="04_reading_repayment_factor",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the intersection of the given loan period row and the interest rate column in the table.",
        tier_2=f"Look along the '{term_years} years' row under the '{_fmt_pct(rate)}' column.",
        tier_3=f"The repayment factor is {_fmt(factor, 2)} per R 1 000 borrowed.",
        r=r,
    )


def generate_05_calculating_monthly_repayment_formula(r: random.Random) -> Dict[str, Any]:
    """Calculate monthly repayment using the formula: Loan Amount ÷ 1 000 × Factor."""
    loan_principal = r.choice([650000, 720000, 800000, 850000, 950000])
    term_years = r.choice([20, 25])
    rate = r.choice([10.0, 10.5, 11.0])
    factor = LOAN_FACTOR_TABLE[term_years][rate]
    monthly_repayment = (loan_principal / 1000.0) * factor

    correct_ans = _fmt_curr(monthly_repayment)
    custom_options = [
        _fmt_curr(monthly_repayment),
        _fmt_curr(monthly_repayment * 1.15),
        _fmt_curr((loan_principal / (term_years * 12))),
        _fmt_curr(monthly_repayment * 0.85),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A homeowner is granted a bond of {_fmt_curr(loan_principal)} for {term_years} years at an interest rate "
        f"of {_fmt_pct(rate)} p.a. The monthly loan factor from the bank's table is {_fmt(factor, 2)} per R 1 000.\n\n"
        f"Using the standard formula:\n"
        f"Monthly Repayment = (Loan Amount ÷ 1 000) × Factor\n"
        f"calculate the monthly repayment amount required by the bank."
    )
    explanation = (
        f"Step 1: Formula: Monthly Repayment = (Loan Amount ÷ 1 000) × Factor [M].\n"
        f"Step 2: Substitute: ({_fmt_curr(loan_principal)} ÷ 1 000) × {_fmt(factor, 2)} = {_fmt(loan_principal/1000.0, 1)} × {_fmt(factor, 2)} [M].\n"
        f"Step 3: Monthly Repayment = {_fmt_curr(monthly_repayment)} [A]."
    )
    return _build_question_payload(
        subskill_id="05_calculating_monthly_repayment_formula",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the loan amount by 1 000, then multiply by the factor.",
        tier_2=f"Calculate ({loan_principal} ÷ 1 000) × {_fmt(factor, 2)}.",
        tier_3=f"The required monthly repayment is {_fmt_curr(monthly_repayment)}.",
        r=r,
    )


def generate_06_real_cost_of_loan(r: random.Random) -> Dict[str, Any]:
    """Calculate the real cost of a loan over its entire lifespan."""
    monthly_repayment = r.choice([7450.50, 7850.94, 8240.25, 9150.80])
    years = r.choice([15, 20, 25])
    total_months = years * 12
    real_cost = monthly_repayment * total_months

    correct_ans = _fmt_curr(real_cost)
    custom_options = [
        _fmt_curr(real_cost),
        _fmt_curr(monthly_repayment * years),
        _fmt_curr(real_cost * 1.1),
        _fmt_curr(real_cost * 0.9),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A family pays a fixed monthly mortgage instalment of {_fmt_curr(monthly_repayment)} over a loan period "
        f"of {years} years ({total_months} monthly instalments).\n\n"
        f"Calculate the Real Cost of the loan (the total amount repaid to the bank over the full duration of the loan)."
    )
    explanation = (
        f"Step 1: Formula: Real Cost = Monthly Repayment × Total Number of Months [M].\n"
        f"Step 2: Total Months = {years} × 12 = {total_months} months [M].\n"
        f"Step 3: Real Cost = {_fmt_curr(monthly_repayment)} × {total_months} = {_fmt_curr(real_cost)} [A]."
    )
    return _build_question_payload(
        subskill_id="06_real_cost_of_loan",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the monthly repayment by the total number of months in the loan term.",
        tier_2=f"First find the total months: {years} × 12 = {total_months}. Then multiply by {_fmt_curr(monthly_repayment)}.",
        tier_3=f"The Real Cost is {_fmt_curr(real_cost)}.",
        r=r,
    )


def generate_07_total_interest_paid(r: random.Random) -> Dict[str, Any]:
    """Calculate total interest paid over the life of a loan: Real Cost - Principal."""
    principal = r.choice([700000, 760000, 850000, 900000])
    monthly_pay = r.choice([7200.00, 7850.94, 8400.50])
    months = 240  # 20 years
    real_cost = monthly_pay * months
    total_interest = real_cost - principal

    correct_ans = _fmt_curr(total_interest)
    custom_options = [
        _fmt_curr(total_interest),
        _fmt_curr(real_cost),
        _fmt_curr(total_interest * 0.8),
        _fmt_curr(principal * 0.11),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A home buyer borrowed an initial principal of {_fmt_curr(principal)} from a financial institution. "
        f"Over the 20-year term (240 monthly payments), the total repayments made (Real Cost) amounted to {_fmt_curr(real_cost)}.\n\n"
        f"Calculate the total interest paid to the bank over the entire life of the loan."
    )
    explanation = (
        f"Step 1: Formula: Total Interest Paid = Real Cost - Loan Principal [M].\n"
        f"Step 2: Substitute: {_fmt_curr(real_cost)} - {_fmt_curr(principal)} [M].\n"
        f"Step 3: Total Interest = {_fmt_curr(total_interest)} [A]."
    )
    return _build_question_payload(
        subskill_id="07_total_interest_paid",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the original amount borrowed from the total amount repaid.",
        tier_2=f"Calculate {_fmt_curr(real_cost)} - {_fmt_curr(principal)}.",
        tier_3=f"The total interest charged is {_fmt_curr(total_interest)}.",
        r=r,
    )


def generate_08_comparing_15_vs_20_year_terms(r: random.Random) -> Dict[str, Any]:
    """Compare real costs and interest between 15-year and 20-year loan options."""
    loan_amount = 750000
    rate = 11.0
    factor_15 = LOAN_FACTOR_TABLE[15][rate]
    factor_20 = LOAN_FACTOR_TABLE[20][rate]

    pmt_15 = (loan_amount / 1000.0) * factor_15
    pmt_20 = (loan_amount / 1000.0) * factor_20

    cost_15 = pmt_15 * (15 * 12)
    cost_20 = pmt_20 * (20 * 12)
    saving = cost_20 - cost_15

    correct_ans = f"15-year term saves {_fmt_curr(saving)} in total interest, despite higher monthly payment by {_fmt_curr(pmt_15 - pmt_20)}"
    custom_options = [
        correct_ans,
        f"20-year term is cheaper overall by {_fmt_curr(saving)} because the monthly payment is lower",
        f"Both loan terms cost the exact same amount because the interest rate is identical ({_fmt_pct(rate)})",
        f"15-year term saves {_fmt_curr(saving * 1.5)} because bank fees are waived",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A borrower compares two financing terms for a {_fmt_curr(loan_amount)} bond at {_fmt_pct(rate)} p.a.:\n"
        f"• Option A (15 years, Factor = {_fmt(factor_15, 2)}): Monthly instalment = {_fmt_curr(pmt_15)}; Real Cost = {_fmt_curr(cost_15)}\n"
        f"• Option B (20 years, Factor = {_fmt(factor_20, 2)}): Monthly instalment = {_fmt_curr(pmt_20)}; Real Cost = {_fmt_curr(cost_20)}\n\n"
        f"Calculate the total financial saving achieved by choosing the 15-year term instead of the 20-year term, "
        f"and explain the trade-off involved."
    )
    explanation = (
        f"Step 1: Calculate Real Cost difference: {_fmt_curr(cost_20)} - {_fmt_curr(cost_15)} = {_fmt_curr(saving)} [M].\n"
        f"Step 2: Monthly payment increase for 15-year term: {_fmt_curr(pmt_15)} - {_fmt_curr(pmt_20)} = {_fmt_curr(pmt_15 - pmt_20)} [M].\n"
        f"Step 3: Conclusion: The 15-year term saves {_fmt_curr(saving)} in interest at the cost of a higher monthly payment [A]."
    )
    return _build_question_payload(
        subskill_id="08_comparing_15_vs_20_year_terms",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the total cost of the 15-year loan from the total cost of the 20-year loan.",
        tier_2=f"Calculate {_fmt_curr(cost_20)} - {_fmt_curr(cost_15)} = {_fmt_curr(saving)}.",
        tier_3=f"Choosing the 15-year loan saves {_fmt_curr(saving)} in total interest.",
        r=r,
    )
