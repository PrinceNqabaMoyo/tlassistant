"""Subskills 17 to 24: Loan optimization, deposit increases, interest rate fluctuations, extra repayments, and early settlements."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    LOAN_FACTOR_TABLE,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_pct,
)


def generate_17_increasing_deposit_savings(r: random.Random) -> Dict[str, Any]:
    """Calculate the overall interest saved by paying a higher deposit."""
    sale_price = 895000.00
    rate = 11.0
    factor = LOAN_FACTOR_TABLE[20][rate]  # 10.32

    # Dep A: 10% vs Dep B: 20%
    dep_a = 0.10 * sale_price
    loan_a = sale_price - dep_a
    cost_a = (loan_a / 1000.0) * factor * 240

    dep_b = 0.20 * sale_price
    loan_b = sale_price - dep_b
    cost_b = (loan_b / 1000.0) * factor * 240

    savings = cost_a - cost_b
    correct_ans = _fmt_curr(savings)

    custom_options = [
        _fmt_curr(savings),
        _fmt_curr(dep_b - dep_a),
        _fmt_curr(savings * 1.25),
        _fmt_curr(savings * 0.75),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A property buyer purchases a house for {_fmt_curr(sale_price)} on a 20-year bond at {_fmt_pct(rate)} p.a. (Factor = {_fmt(factor, 2)}).\n"
        f"• If they pay a 10% deposit, the Real Cost of the loan is {_fmt_curr(cost_a)}.\n"
        f"• If they pay a 20% deposit, the Real Cost of the loan is {_fmt_curr(cost_b)}.\n\n"
        f"Calculate the total financial saving in loan repayments achieved over the 20-year term by paying a 20% deposit instead of 10%."
    )
    explanation = (
        f"Step 1: Real Cost with 10% deposit = {_fmt_curr(cost_a)} [M].\n"
        f"Step 2: Real Cost with 20% deposit = {_fmt_curr(cost_b)} [M].\n"
        f"Step 3: Total saving = {_fmt_curr(cost_a)} - {_fmt_curr(cost_b)} = {_fmt_curr(savings)} [A]."
    )
    return _build_question_payload(
        subskill_id="17_increasing_deposit_savings",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the total loan cost of the 20% deposit scenario from the 10% deposit scenario.",
        tier_2=f"Calculate {_fmt_curr(cost_a)} - {_fmt_curr(cost_b)}.",
        tier_3=f"The total repayment savings is {_fmt_curr(savings)}.",
        r=r,
    )


def generate_18_rate_hike_monthly_impact(r: random.Random) -> Dict[str, Any]:
    """Calculate the increase in monthly mortgage payment following a 1% interest rate hike."""
    loan_amount = r.choice([750000, 800000, 900000, 1000000])
    factor_old = LOAN_FACTOR_TABLE[20][10.0]  # 9.65
    factor_new = LOAN_FACTOR_TABLE[20][11.0]  # 10.32

    pmt_old = (loan_amount / 1000.0) * factor_old
    pmt_new = (loan_amount / 1000.0) * factor_new
    increase = pmt_new - pmt_old

    correct_ans = f"Monthly repayment increases by {_fmt_curr(increase)} (from {_fmt_curr(pmt_old)} to {_fmt_curr(pmt_new)})"
    custom_options = [
        correct_ans,
        f"Monthly repayment increases by {_fmt_curr(loan_amount * 0.01)}",
        f"Monthly repayment increases by {_fmt_curr(increase * 1.5)}",
        f"Monthly repayment remains unchanged because existing bonds are permanently locked",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"The South African Reserve Bank (SARB) raises the repo rate, causing mortgage interest rates to climb "
        f"from 10,0% p.a. (Factor = {_fmt(factor_old, 2)}) to 11,0% p.a. (Factor = {_fmt(factor_new, 2)}).\n\n"
        f"For a 20-year bond of {_fmt_curr(loan_amount)}, calculate the monthly repayment increase required from the borrower."
    )
    explanation = (
        f"Step 1: Old payment = ({loan_amount} ÷ 1 000) × {_fmt(factor_old, 2)} = {_fmt_curr(pmt_old)} [M].\n"
        f"Step 2: New payment = ({loan_amount} ÷ 1 000) × {_fmt(factor_new, 2)} = {_fmt_curr(pmt_new)} [M].\n"
        f"Step 3: Increase = {_fmt_curr(pmt_new)} - {_fmt_curr(pmt_old)} = {_fmt_curr(increase)} [A]."
    )
    return _build_question_payload(
        subskill_id="18_rate_hike_monthly_impact",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the monthly payment under both interest rates and find the difference.",
        tier_2=f"Old payment: {_fmt_curr(pmt_old)}; New payment: {_fmt_curr(pmt_new)}.",
        tier_3=f"The monthly increase is {_fmt_curr(increase)}.",
        r=r,
    )


def generate_19_rate_cut_total_savings(r: random.Random) -> Dict[str, Any]:
    """Calculate the total savings over the life of a loan from a 1% rate reduction."""
    loan_amount = 850000.00
    factor_old = LOAN_FACTOR_TABLE[20][11.5]  # 10.66
    factor_new = LOAN_FACTOR_TABLE[20][10.5]  # 9.98

    pmt_old = (loan_amount / 1000.0) * factor_old
    pmt_new = (loan_amount / 1000.0) * factor_new

    cost_old = pmt_old * 240
    cost_new = pmt_new * 240
    savings = cost_old - cost_new

    correct_ans = _fmt_curr(savings)
    custom_options = [
        _fmt_curr(savings),
        _fmt_curr(pmt_old - pmt_new),
        _fmt_curr(savings * 1.15),
        _fmt_curr(loan_amount * 0.10),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A homeowner with a {_fmt_curr(loan_amount)} 20-year bond negotiates a 1,0% rate concession with their bank, "
        f"lowering the interest rate from 11,5% (Factor = {_fmt(factor_old, 2)}) to 10,5% (Factor = {_fmt(factor_new, 2)}).\n\n"
        f"Calculate the total money saved over the entire 240-month life of the loan."
    )
    explanation = (
        f"Step 1: Total cost at 11,5% = ({loan_amount} ÷ 1 000) × {_fmt(factor_old, 2)} × 240 = {_fmt_curr(cost_old)} [M].\n"
        f"Step 2: Total cost at 10,5% = ({loan_amount} ÷ 1 000) × {_fmt(factor_new, 2)} × 240 = {_fmt_curr(cost_new)} [M].\n"
        f"Step 3: Total saving = {_fmt_curr(cost_old)} - {_fmt_curr(cost_new)} = {_fmt_curr(savings)} [A]."
    )
    return _build_question_payload(
        subskill_id="19_rate_cut_total_savings",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the difference in monthly payment, then multiply by 240 months.",
        tier_2=f"Monthly saving = {_fmt_curr(pmt_old - pmt_new)}. Multiply by 240.",
        tier_3=f"Total saving is {_fmt_curr(savings)}.",
        r=r,
    )


def generate_20_extra_monthly_payment_term_reduction(r: random.Random) -> Dict[str, Any]:
    """Analyze how paying an additional monthly contribution shortens the loan term."""
    extra = r.choice([500, 1000, 1500])
    correct_ans = f"Paying an extra {_fmt_curr(extra)} per month reduces the loan term by approximately 4 to 6 years and saves hundreds of thousands in interest"

    custom_options = [
        correct_ans,
        f"Paying an extra {_fmt_curr(extra)} increases the loan term because the bank charges penalty interest",
        f"The loan term remains strictly fixed at 240 months regardless of overpayments",
        f"The borrower pays off the entire loan within 12 months",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A borrower with a 20-year (240-month) home loan decides to pay an extra {_fmt_curr(extra)} into their bond "
        f"every month above the mandatory monthly instalment.\n\n"
        f"Describe the effect of this regular extra payment on the remaining loan term and total interest."
    )
    explanation = (
        f"Step 1: The extra {_fmt_curr(extra)} goes 100% directly toward reducing the principal balance [M].\n"
        f"Step 2: A reduced principal generates less compound interest each subsequent month [M].\n"
        f"Step 3: The loan is paid off several years early, yielding substantial interest savings [A]."
    )
    return _build_question_payload(
        subskill_id="20_extra_monthly_payment_term_reduction",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Any extra payment above the required instalment goes directly toward reducing capital debt.",
        tier_2="Less capital debt generates less interest each month.",
        tier_3="This significantly shortens the repayment period and saves massive interest.",
        r=r,
    )


def generate_21_interest_saved_extra_payment(r: random.Random) -> Dict[str, Any]:
    """Calculate the exact total saving when a loan is settled early due to extra payments."""
    orig_total_cost = r.choice([1884225.60, 2150000.00, 2400000.00])
    new_months = 180  # 15 years instead of 20
    new_pmt = r.choice([8850.94, 9500.00, 10200.00])
    new_total_cost = new_pmt * new_months
    total_saved = orig_total_cost - new_total_cost

    d_spec_21 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": "Mortgage Total Outlay Comparison",
        "categories": ["Standard (20 yr)", "With Extra Payments (15 yr)"],
        "series": [
            {"name": "Total Cost", "values": [orig_total_cost, new_total_cost]}
        ],
    }

    correct_ans = _fmt_curr(total_saved)
    custom_options = [
        _fmt_curr(total_saved),
        _fmt_curr(total_saved * 1.2),
        _fmt_curr(new_pmt * 12),
        _fmt_curr(orig_total_cost * 0.15),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the mortgage comparison chart showing total repayments over time.\n"
        f"A 20-year bond would normally cost {_fmt_curr(orig_total_cost)} over 240 months.\n"
        f"By paying an extra R 1 000,00 each month (total repayment {_fmt_curr(new_pmt)}), the bond is settled "
        f"in full after only {new_months} months (15 years).\n\n"
        f"Calculate the net total interest saving achieved over the life of the loan."
    )
    explanation = (
        f"Step 1: Calculate new total outlay: {new_months} × {_fmt_curr(new_pmt)} = {_fmt_curr(new_total_cost)} [M].\n"
        f"Step 2: Subtract new total outlay from original total cost: {_fmt_curr(orig_total_cost)} - {_fmt_curr(new_total_cost)} [M].\n"
        f"Step 3: Net saving = {_fmt_curr(total_saved)} [A]."
    )
    return _build_question_payload(
        subskill_id="21_interest_saved_extra_payment",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the new total cost by multiplying the new monthly payment by 180 months.",
        tier_2=f"New total = 180 × {_fmt_curr(new_pmt)} = {_fmt_curr(new_total_cost)}. Subtract from {_fmt_curr(orig_total_cost)}.",
        tier_3=f"The net saving is {_fmt_curr(total_saved)}.",
        r=r,
        diagram_spec=d_spec_21,
    )


def generate_22_fixed_vs_variable_rate_risk(r: random.Random) -> Dict[str, Any]:
    """Compare the risk profiles of fixed versus variable interest rates in South Africa."""
    correct_ans = "Fixed rate provides payment certainty during rising rate cycles; variable rate benefits the borrower when the SARB cuts interest rates"

    custom_options = [
        correct_ans,
        "Fixed rates automatically drop whenever the national inflation rate decreases",
        "Variable rates guarantee that the monthly repayment will never change",
        "Banks in South Africa are legally prohibited from offering variable rates on residential bonds",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"When applying for a home loan, a borrower is offered a choice between a Fixed Interest Rate and a Variable Interest Rate.\n\n"
        f"Evaluate the financial risks and advantages of both options in the South African economic context."
    )
    explanation = (
        f"Step 1: Fixed rate locks the interest rate, protecting the borrower against rate hikes but usually set higher initially [M].\n"
        f"Step 2: Variable rate fluctuates with the prime lending rate, offering lower initial costs but exposure to rate hike shocks [M].\n"
        f"Step 3: Correct synthesis: Fixed gives certainty; variable allows savings if rates drop [A]."
    )
    return _build_question_payload(
        subskill_id="22_fixed_vs_variable_rate_risk",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Consider what happens when the Reserve Bank raises or lowers interest rates.",
        tier_2="Fixed rate keeps instalments unchanged; variable rate rises or falls with the market.",
        tier_3="Fixed provides stability; variable offers savings during rate cuts.",
        r=r,
    )


def generate_23_prime_lending_rate_adjustments(r: random.Random) -> Dict[str, Any]:
    """Calculate the new interest rate when prime changes on a 'Prime + X%' home loan."""
    margin = r.choice([0.5, 1.0, 1.25, 1.5])
    old_prime = 11.75
    new_prime = old_prime + r.choice([0.25, 0.50])
    new_rate = new_prime + margin

    correct_ans = f"New rate = {_fmt_pct(new_rate)} (Prime {_fmt_pct(new_prime)} + {_fmt_pct(margin)})"
    custom_options = [
        f"New rate = {_fmt_pct(new_rate)} (Prime {_fmt_pct(new_prime)} + {_fmt_pct(margin)})",
        f"New rate = {_fmt_pct(new_prime)} (Margin is waived by the bank)",
        f"New rate = {_fmt_pct(new_rate + 1.0)} (Additional administrative penalty)",
        f"New rate = {_fmt_pct(old_prime + margin)} (Existing loans ignore prime rate changes)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A homeowner's bond is linked to the prime lending rate at 'Prime + {_fmt_pct(margin)}'.\n"
        f"The Reserve Bank announces an interest rate adjustment, increasing the Prime Lending Rate from {_fmt_pct(old_prime)} "
        f"to {_fmt_pct(new_prime)}.\n\n"
        f"Calculate the new interest rate applied to this homeowner's mortgage."
    )
    explanation = (
        f"Step 1: Formula: Customer Rate = New Prime Rate + Agreed Margin [M].\n"
        f"Step 2: Substitute: {_fmt_pct(new_prime)} + {_fmt_pct(margin)} = {_fmt_pct(new_rate)} [M].\n"
        f"Step 3: New Rate = {_fmt_pct(new_rate)} [A]."
    )
    return _build_question_payload(
        subskill_id="23_prime_lending_rate_adjustments",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the agreed margin to the new Prime lending rate.",
        tier_2=f"Calculate {_fmt_pct(new_prime)} + {_fmt_pct(margin)}.",
        tier_3=f"The new interest rate is {_fmt_pct(new_rate)}.",
        r=r,
    )


def generate_24_early_settlement_quotations(r: random.Random) -> Dict[str, Any]:
    """Calculate early settlement balance: Outstanding Principal + 90-day early termination interest."""
    outstanding_bal = r.choice([450000.00, 520000.00, 600000.00])
    annual_rate = 11.0
    penalty_days = 90
    early_interest = outstanding_bal * (annual_rate / 100.0) * (penalty_days / 365.0)
    settlement_quote = outstanding_bal + early_interest

    d_spec_24 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Early Settlement Quotation ({_fmt_curr(settlement_quote)})",
        "categories": ["Outstanding Principal", "90-Day Penalty Interest"],
        "series": [
            {"name": "Amount", "values": [outstanding_bal, early_interest]}
        ],
    }

    correct_ans = _fmt_curr(settlement_quote)
    custom_options = [
        _fmt_curr(settlement_quote),
        _fmt_curr(outstanding_bal),
        _fmt_curr(settlement_quote * 1.1),
        _fmt_curr(outstanding_bal * (annual_rate / 100.0)),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the early settlement quotation summary.\n"
        f"A borrower sells their house and requests a settlement figure for their bond:\n"
        f"• Outstanding balance: {_fmt_curr(outstanding_bal)}\n"
        f"• Interest rate: {_fmt_pct(annual_rate)} p.a.\n"
        f"Under the National Credit Act (NCA), the bank charges a 90-day penalty interest fee for early cancellation.\n\n"
        f"Calculate the total early settlement figure (Outstanding balance + 90 days interest based on a 365-day year)."
    )
    explanation = (
        f"Step 1: Calculate 90-day interest penalty: {_fmt_curr(outstanding_bal)} × ({annual_rate}% ÷ 100) × (90 ÷ 365) = {_fmt_curr(early_interest)} [M].\n"
        f"Step 2: Add penalty to outstanding balance: {_fmt_curr(outstanding_bal)} + {_fmt_curr(early_interest)} [M].\n"
        f"Step 3: Settlement figure = {_fmt_curr(settlement_quote)} [A]."
    )
    return _build_question_payload(
        subskill_id="24_early_settlement_quotations",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate 90 days of interest on the outstanding balance and add it to the principal.",
        tier_2=f"Interest penalty = {_fmt_curr(outstanding_bal)} × {annual_rate}% × (90/365) = {_fmt_curr(early_interest)}.",
        tier_3=f"Total settlement quote = {_fmt_curr(settlement_quote)}.",
        r=r,
        diagram_spec=d_spec_24,
    )
