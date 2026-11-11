"""Subskills 09 to 16: Loan amortization tables, balance transitions, non-linear curve decay, and total acquisition cost."""
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


def generate_09_closing_balance_carryover(r: random.Random) -> Dict[str, Any]:
    """Verify that previous month closing balance becomes next month opening balance."""
    close_m1 = r.choice([759872.60, 680450.25, 842190.50, 915230.10])
    correct_ans = f"Opening balance for Month 2 is {_fmt_curr(close_m1)} (identical to Month 1 closing balance)"

    custom_options = [
        f"Opening balance for Month 2 is {_fmt_curr(close_m1)} (identical to Month 1 closing balance)",
        f"Opening balance for Month 2 is {_fmt_curr(close_m1 - 7850.94)} (after subtracting repayment early)",
        f"Opening balance for Month 2 resets to the original loan principal amount",
        f"Opening balance for Month 2 is {_fmt_curr(close_m1 * 1.00916)} (including next month interest)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a 20-year home loan amortization schedule, the closing balance at the end of Month 1 is recorded as {_fmt_curr(close_m1)}.\n\n"
        f"State the opening balance for Month 2 and explain the fundamental accounting rule governing month-to-month loan transitions."
    )
    explanation = (
        f"Step 1: In any loan amortization schedule, the closing balance of Month n becomes the opening balance of Month n+1 [M].\n"
        f"Step 2: The debtor owes exactly that remaining amount at the beginning of the next billing cycle [M].\n"
        f"Step 3: Opening Balance Month 2 = {_fmt_curr(close_m1)} [A]."
    )
    return _build_question_payload(
        subskill_id="09_closing_balance_carryover",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The closing balance at the end of one month carries forward unchanged to start the next month.",
        tier_2=f"The closing balance for Month 1 was {_fmt_curr(close_m1)}.",
        tier_3=f"Opening balance for Month 2 is {_fmt_curr(close_m1)}.",
        r=r,
    )


def generate_10_table_monthly_interest_calc(r: random.Random) -> Dict[str, Any]:
    """Calculate the monthly interest entry in an amortization table."""
    open_bal = r.choice([750000.00, 680000.00, 820000.00, 940000.00])
    annual_rate = r.choice([10.5, 11.0, 11.5, 12.0])
    monthly_interest = open_bal * (annual_rate / 100.0) / 12.0

    correct_ans = _fmt_curr(monthly_interest)
    custom_options = [
        _fmt_curr(monthly_interest),
        _fmt_curr(open_bal * (annual_rate / 100.0)),
        _fmt_curr(monthly_interest * 1.2),
        _fmt_curr(monthly_interest * 0.8),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Consider an amortization table extract for a home loan with an interest rate of {_fmt_pct(annual_rate)} p.a. (compounded monthly):\n"
        f"• Month Opening Balance: {_fmt_curr(open_bal)}\n\n"
        f"Calculate the interest charged for this specific month."
    )
    explanation = (
        f"Step 1: Monthly interest = Opening Balance × (Annual Rate ÷ 12) [M].\n"
        f"Step 2: Substitute: {_fmt_curr(open_bal)} × ({annual_rate}% ÷ 12) = {_fmt_curr(open_bal)} × {_fmt(annual_rate/1200.0, 6)} [M].\n"
        f"Step 3: Interest = {_fmt_curr(monthly_interest)} [A]."
    )
    return _build_question_payload(
        subskill_id="10_table_monthly_interest_calc",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the opening balance by the monthly interest rate (annual rate ÷ 12).",
        tier_2=f"Calculate {_fmt_curr(open_bal)} × ({annual_rate} ÷ 1200).",
        tier_3=f"The interest charge is {_fmt_curr(monthly_interest)}.",
        r=r,
    )


def generate_11_balance_with_interest(r: random.Random) -> Dict[str, Any]:
    """Calculate 'Balance with Interest' before the monthly repayment is subtracted."""
    open_bal = r.choice([760750.00, 759872.60, 650000.00, 890000.00])
    interest = r.choice([6973.54, 6965.50, 5958.33, 8158.33])
    bal_with_int = open_bal + interest

    correct_ans = _fmt_curr(bal_with_int)
    custom_options = [
        _fmt_curr(bal_with_int),
        _fmt_curr(open_bal - interest),
        _fmt_curr(bal_with_int - 7850.94),
        _fmt_curr(bal_with_int * 1.05),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a monthly loan ledger, the Opening Balance is {_fmt_curr(open_bal)} and the calculated interest "
        f"for the month is {_fmt_curr(interest)}.\n\n"
        f"Calculate the 'Balance with Interest' (the interim balance owed before the monthly repayment is deducted)."
    )
    explanation = (
        f"Step 1: Formula: Balance with Interest = Opening Balance + Monthly Interest [M].\n"
        f"Step 2: Substitute: {_fmt_curr(open_bal)} + {_fmt_curr(interest)} [M].\n"
        f"Step 3: Balance with Interest = {_fmt_curr(bal_with_int)} [A]."
    )
    return _build_question_payload(
        subskill_id="11_balance_with_interest",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the month's interest charge directly to the opening balance.",
        tier_2=f"Calculate {_fmt_curr(open_bal)} + {_fmt_curr(interest)}.",
        tier_3=f"The balance with interest is {_fmt_curr(bal_with_int)}.",
        r=r,
    )


def generate_12_end_of_month_closing_balance(r: random.Random) -> Dict[str, Any]:
    """Calculate the closing balance after subtracting the monthly repayment."""
    bal_with_int = r.choice([767723.54, 766838.10, 655958.33, 898158.33])
    repayment = r.choice([7850.94, 8200.00, 6850.50, 9150.00])
    closing_bal = bal_with_int - repayment

    correct_ans = _fmt_curr(closing_bal)
    custom_options = [
        _fmt_curr(closing_bal),
        _fmt_curr(bal_with_int + repayment),
        _fmt_curr(closing_bal * 0.95),
        _fmt_curr(closing_bal + 2500.00),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"At the end of a monthly cycle, a loan account has a 'Balance with Interest' of {_fmt_curr(bal_with_int)}. "
        f"The borrower's standard monthly debit order repayment of {_fmt_curr(repayment)} is processed.\n\n"
        f"Calculate the Closing Balance on the loan account."
    )
    explanation = (
        f"Step 1: Formula: Closing Balance = Balance with Interest - Repayment Amount [M].\n"
        f"Step 2: Substitute: {_fmt_curr(bal_with_int)} - {_fmt_curr(repayment)} [M].\n"
        f"Step 3: Closing Balance = {_fmt_curr(closing_bal)} [A]."
    )
    return _build_question_payload(
        subskill_id="12_end_of_month_closing_balance",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the monthly repayment from the balance with interest.",
        tier_2=f"Calculate {_fmt_curr(bal_with_int)} - {_fmt_curr(repayment)}.",
        tier_3=f"The closing balance is {_fmt_curr(closing_bal)}.",
        r=r,
    )


def generate_13_final_month_adjustment_payment(r: random.Random) -> Dict[str, Any]:
    """Calculate the final month balloon/settlement adjustment payment in Month 240."""
    open_last = r.choice([8900.50, 9008.78, 9250.00, 9500.20])
    interest_last = r.choice([81.50, 82.58, 84.80, 87.10])
    final_pmt = open_last + interest_last

    correct_ans = f"Final payment = {_fmt_curr(final_pmt)} (to bring the closing balance to exactly R 0,00)"
    custom_options = [
        correct_ans,
        f"Final payment = {_fmt_curr(open_last)} (the interest is waived by the bank)",
        f"Final payment = {_fmt_curr(7850.94)} (the standard monthly payment remains unchanged)",
        f"Final payment = {_fmt_curr(final_pmt + 1000.00)} (including bond cancellation fee)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In the 240th and final month of a 20-year bond, the opening balance is {_fmt_curr(open_last)} "
        f"and the final interest charged is {_fmt_curr(interest_last)}.\n\n"
        f"Calculate the exact repayment required in Month 240 so that the closing balance reaches exactly R 0,00."
    )
    explanation = (
        f"Step 1: Balance before payment = Opening Balance + Interest = {_fmt_curr(open_last)} + {_fmt_curr(interest_last)} = {_fmt_curr(final_pmt)} [M].\n"
        f"Step 2: To reduce the balance to R 0,00, the repayment must equal the full remaining amount [M].\n"
        f"Step 3: Final repayment = {_fmt_curr(final_pmt)} [A]."
    )
    return _build_question_payload(
        subskill_id="13_final_month_adjustment_payment",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the final month's interest to the opening balance.",
        tier_2=f"Calculate {_fmt_curr(open_last)} + {_fmt_curr(interest_last)}.",
        tier_3=f"The final payment required is {_fmt_curr(final_pmt)}.",
        r=r,
    )


def generate_14_non_linear_loan_balance_curve(r: random.Random) -> Dict[str, Any]:
    """Explain why the loan balance curve decreases slowly at first and accelerates toward the end."""
    principal = r.choice([850000, 1000000, 1200000])
    d_spec_14 = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"20-Year Mortgage Balance Curve ({_fmt_curr(principal)})",
        "x_label": "Month",
        "y_label": "Loan Balance (R)",
        "series": [
            {"name": "Closing Balance", "points": [[0, principal], [60, int(principal * 0.92)], [120, int(principal * 0.78)], [180, int(principal * 0.52)], [240, 0]]}
        ],
    }
    correct_ans = "Non-linear decay: Early instalments consist mostly of interest, so principal drops slowly; as balance shrinks, interest decreases and principal repayments accelerate"

    custom_options = [
        correct_ans,
        "Linear decay: The bank deducts an identical fixed amount of capital every single month",
        "Steep initial drop: Borrowers pay 80% of the principal during the first 5 years",
        "Random fluctuation: The monthly balance changes arbitrarily depending on inflation rates",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the loan balance graph tracking the closing balance of a 20-year mortgage over 240 months.\n"
        f"Explain from an amortization perspective why this loan balance curve decreases gradually at first and accelerates toward the end."
    )
    explanation = (
        f"Step 1: Interest is calculated on the outstanding balance, which is very high in early years [M].\n"
        f"Step 2: Consequently, early instalments cover mostly interest with little going toward capital reduction [M].\n"
        f"Step 3: In later years, lower balances produce low interest, directing most of each payment to capital, accelerating the decline [A]."
    )
    return _build_question_payload(
        subskill_id="14_non_linear_loan_balance_curve",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about how much of each monthly payment goes to interest versus paying off the actual debt.",
        tier_2="At the start, the debt is huge, so almost all of your monthly repayment pays interest.",
        tier_3="As the debt decreases, interest drops, allowing more capital to be paid off each month.",
        r=r,
        diagram_spec=d_spec_14,
    )


def generate_15_principal_reduction_ratio(r: random.Random) -> Dict[str, Any]:
    """Calculate the proportion of monthly instalment that pays interest versus principal in Month 1."""
    pmt = 7850.94
    interest_m1 = 6973.54
    capital_m1 = pmt - interest_m1
    interest_share_pct = (interest_m1 / pmt) * 100

    correct_ans = f"Interest: {_fmt_curr(interest_m1)} ({_fmt(interest_share_pct, 1)}%); Principal reduction: {_fmt_curr(capital_m1)} ({_fmt(100 - interest_share_pct, 1)}%)"
    custom_options = [
        correct_ans,
        f"Interest: {_fmt_curr(capital_m1)} ({_fmt(100 - interest_share_pct, 1)}%); Principal reduction: {_fmt_curr(interest_m1)} ({_fmt(interest_share_pct, 1)}%)",
        f"Interest: 50,0%; Principal reduction: 50,0%",
        f"Interest: 100,0%; Principal reduction: 0,0%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In Month 1 of a home loan, the borrower pays a monthly instalment of {_fmt_curr(pmt)}.\n"
        f"The interest charged for Month 1 is {_fmt_curr(interest_m1)}.\n\n"
        f"Calculate the actual amount and percentage of the instalment that goes toward reducing the principal debt."
    )
    explanation = (
        f"Step 1: Principal reduced = Instalment - Interest = {_fmt_curr(pmt)} - {_fmt_curr(interest_m1)} = {_fmt_curr(capital_m1)} [M].\n"
        f"Step 2: Interest share = ({_fmt_curr(interest_m1)} ÷ {_fmt_curr(pmt)}) × 100% = {_fmt(interest_share_pct, 1)}% [M].\n"
        f"Step 3: Principal share = 100% - {_fmt(interest_share_pct, 1)}% = {_fmt(100 - interest_share_pct, 1)}% [A]."
    )
    return _build_question_payload(
        subskill_id="15_principal_reduction_ratio",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the month's interest charge from the monthly repayment amount.",
        tier_2=f"Capital reduction = {_fmt_curr(pmt)} - {_fmt_curr(interest_m1)} = {_fmt_curr(capital_m1)}.",
        tier_3=f"Over {_fmt(interest_share_pct, 1)}% of the first payment goes purely to interest.",
        r=r,
    )


def generate_16_total_property_acquisition_cost(r: random.Random) -> Dict[str, Any]:
    """Calculate total property acquisition cost: Real Cost + Deposit + Final Extra Payment."""
    real_cost = 1884225.60
    deposit = 132450.00
    extra_final = 1240.42  # final payment minus standard payment
    total_cost = real_cost + deposit + extra_final

    correct_ans = _fmt_curr(total_cost)
    custom_options = [
        _fmt_curr(total_cost),
        _fmt_curr(real_cost + deposit),
        _fmt_curr(real_cost - deposit),
        _fmt_curr(total_cost * 1.14),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A homeowner reviews the total lifetime outlay for purchasing their home:\n"
        f"• Upfront deposit paid: {_fmt_curr(deposit)}\n"
        f"• Total standard monthly repayments (Real Cost): {_fmt_curr(real_cost)}\n"
        f"• Extra balance adjustment on final month: {_fmt_curr(extra_final)}\n\n"
        f"Calculate the comprehensive Total Cost of Acquisition for this home."
    )
    explanation = (
        f"Step 1: Formula: Total Cost = Deposit + Real Cost + Extra Final Adjustment [M].\n"
        f"Step 2: Substitute: {_fmt_curr(deposit)} + {_fmt_curr(real_cost)} + {_fmt_curr(extra_final)} [M].\n"
        f"Step 3: Total Cost = {_fmt_curr(total_cost)} [A]."
    )
    return _build_question_payload(
        subskill_id="16_total_property_acquisition_cost",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the upfront deposit, total standard repayments, and final adjustment together.",
        tier_2=f"Calculate {_fmt_curr(deposit)} + {_fmt_curr(real_cost)} + {_fmt_curr(extra_final)}.",
        tier_3=f"The total acquisition cost is {_fmt_curr(total_cost)}.",
        r=r,
    )
