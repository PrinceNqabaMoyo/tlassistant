"""Subskills 25 to 32: Vehicle finance, balloon payments, refinancing, total ownership cost, and depreciation."""
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


def generate_25_vehicle_net_financed_amount(r: random.Random) -> Dict[str, Any]:
    """Calculate net financed amount: Cash Price - Trade-in Value - Deposit + Initiation Fee."""
    cash_price = r.choice([280000, 320000, 360000, 420000])
    trade_in = r.choice([40000, 50000, 60000])
    deposit = r.choice([20000, 30000])
    initiation_fee = 1207.50
    net_financed = cash_price - trade_in - deposit + initiation_fee

    d_spec_25 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Vehicle Financing Structure ({_fmt_curr(cash_price)})",
        "categories": ["Cash Price", "Trade-in", "Deposit", "Net Financed"],
        "series": [
            {"name": "Amount", "values": [cash_price, trade_in, deposit, net_financed]}
        ],
    }

    correct_ans = _fmt_curr(net_financed)
    custom_options = [
        _fmt_curr(net_financed),
        _fmt_curr(cash_price - trade_in - deposit),
        _fmt_curr(net_financed + 10000.00),
        _fmt_curr(cash_price - trade_in),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the vehicle financing structure with a vehicle sticker cash price of {_fmt_curr(cash_price)}.\n"
        f"• The dealer allows a trade-in value of {_fmt_curr(trade_in)} for their old car.\n"
        f"• The buyer pays a cash deposit of {_fmt_curr(deposit)}.\n"
        f"• A mandatory bank initiation fee of {_fmt_curr(initiation_fee)} is capitalized onto the loan.\n\n"
        f"Calculate the net principal amount that must be financed by the vehicle finance bank."
    )
    explanation = (
        f"Step 1: Formula: Net Financed = Cash Price - Trade-in - Deposit + Initiation Fee [M].\n"
        f"Step 2: Substitute: {_fmt_curr(cash_price)} - {_fmt_curr(trade_in)} - {_fmt_curr(deposit)} + {_fmt_curr(initiation_fee)} [M].\n"
        f"Step 3: Net Financed Amount = {_fmt_curr(net_financed)} [A]."
    )
    return _build_question_payload(
        subskill_id="25_vehicle_net_financed_amount",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract trade-in and deposit from the cash price, then add the capitalized initiation fee.",
        tier_2=f"Calculate {_fmt_curr(cash_price)} - {_fmt_curr(trade_in)} - {_fmt_curr(deposit)} + {_fmt_curr(initiation_fee)}.",
        tier_3=f"The net financed amount is {_fmt_curr(net_financed)}.",
        r=r,
        diagram_spec=d_spec_25,
    )


def generate_26_calculating_balloon_payment_rands(r: random.Random) -> Dict[str, Any]:
    """Calculate the balloon payment (residual value) in Rands from a given percentage."""
    purchase_price = r.choice([250000, 300000, 350000, 400000])
    balloon_pct = r.choice([20, 25, 30, 35])
    balloon_rands = (balloon_pct / 100.0) * purchase_price

    correct_ans = _fmt_curr(balloon_rands)
    custom_options = [
        _fmt_curr(balloon_rands),
        _fmt_curr(balloon_rands * 1.2),
        _fmt_curr(purchase_price - balloon_rands),
        _fmt_curr(balloon_rands * 0.8),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A vehicle finance contract for a car priced at {_fmt_curr(purchase_price)} specifies a {balloon_pct}% "
        f"balloon payment (residual value) payable as a lump sum at the end of the 60-month loan term.\n\n"
        f"Calculate the exact monetary value (in Rands) of the balloon payment."
    )
    explanation = (
        f"Step 1: Formula: Balloon in Rands = Purchase Price × (Balloon % ÷ 100) [M].\n"
        f"Step 2: Substitute: {_fmt_curr(purchase_price)} × ({balloon_pct} ÷ 100) [M].\n"
        f"Step 3: Balloon Payment = {_fmt_curr(balloon_rands)} [A]."
    )
    return _build_question_payload(
        subskill_id="26_calculating_balloon_payment_rands",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the vehicle purchase price by the balloon percentage.",
        tier_2=f"Calculate {balloon_pct}% of {_fmt_curr(purchase_price)}.",
        tier_3=f"The balloon payment amount is {_fmt_curr(balloon_rands)}.",
        r=r,
    )


def generate_27_vehicle_monthly_instalment_balloon(r: random.Random) -> Dict[str, Any]:
    """Calculate vehicle monthly instalment when a balloon payment lowers the financed portion."""
    principal = 300000.00
    balloon_rands = 90000.00  # 30% balloon
    term_months = 60
    # Interest is charged on the whole amount, but principal amortizes only (principal - balloon)
    # Standard formula approximation used in MathLit textbooks:
    # Monthly = ((Principal - Balloon) / Months) + (Principal * Monthly Rate)
    annual_rate = 12.0
    monthly_rate = annual_rate / 1200.0  # 1% per month

    amortizing_part = (principal - balloon_rands) / term_months
    interest_part = principal * monthly_rate
    monthly_instalment = amortizing_part + interest_part

    correct_ans = _fmt_curr(monthly_instalment)
    custom_options = [
        _fmt_curr(monthly_instalment),
        _fmt_curr(monthly_instalment * 1.25),
        _fmt_curr(principal / term_months),
        _fmt_curr(monthly_instalment * 0.8),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A car of {_fmt_curr(principal)} is financed over {term_months} months at {_fmt_pct(annual_rate)} p.a. (1,0% per month) "
        f"with a {_fmt_curr(balloon_rands)} balloon payment.\n"
        f"The monthly instalment comprises:\n"
        f"• Capital repayment: (Financed Amount - Balloon) ÷ {term_months}\n"
        f"• Monthly interest: Financed Amount × 1,0%\n\n"
        f"Calculate the monthly instalment amount."
    )
    explanation = (
        f"Step 1: Capital repayment = ({_fmt_curr(principal)} - {_fmt_curr(balloon_rands)}) ÷ {term_months} = {_fmt_curr(amortizing_part)} [M].\n"
        f"Step 2: Monthly interest = {_fmt_curr(principal)} × 1,0% = {_fmt_curr(interest_part)} [M].\n"
        f"Step 3: Monthly instalment = {_fmt_curr(amortizing_part)} + {_fmt_curr(interest_part)} = {_fmt_curr(monthly_instalment)} [A]."
    )
    return _build_question_payload(
        subskill_id="27_vehicle_monthly_instalment_balloon",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the capital repayment part and the monthly interest part, then add them together.",
        tier_2=f"Capital: ({_fmt_curr(principal)} - {_fmt_curr(balloon_rands)}) ÷ 60 = {_fmt_curr(amortizing_part)}. Interest: {_fmt_curr(principal)} × 1% = {_fmt_curr(interest_part)}.",
        tier_3=f"The monthly instalment is {_fmt_curr(monthly_instalment)}.",
        r=r,
    )


def generate_28_total_cost_vehicle_finance(r: random.Random) -> Dict[str, Any]:
    """Calculate total cost of vehicle purchase including deposit, instalments, and balloon payment."""
    deposit = 30000.00
    monthly_pmt = 6500.00
    months = 60
    balloon_settlement = 90000.00
    total_cost = deposit + (monthly_pmt * months) + balloon_settlement

    correct_ans = _fmt_curr(total_cost)
    custom_options = [
        _fmt_curr(total_cost),
        _fmt_curr(deposit + (monthly_pmt * months)),
        _fmt_curr(monthly_pmt * months),
        _fmt_curr(total_cost * 1.15),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A motorist finances a vehicle under the following structure:\n"
        f"• Cash deposit: {_fmt_curr(deposit)}\n"
        f"• Monthly instalments: {_fmt_curr(monthly_pmt)} per month for {months} months\n"
        f"• Final balloon payment: {_fmt_curr(balloon_settlement)}\n\n"
        f"Calculate the total cost of ownership for this vehicle across the 60-month agreement."
    )
    explanation = (
        f"Step 1: Total monthly instalments = {months} × {_fmt_curr(monthly_pmt)} = {_fmt_curr(monthly_pmt * months)} [M].\n"
        f"Step 2: Add deposit and balloon: {_fmt_curr(deposit)} + {_fmt_curr(monthly_pmt * months)} + {_fmt_curr(balloon_settlement)} [M].\n"
        f"Step 3: Total Cost = {_fmt_curr(total_cost)} [A]."
    )
    return _build_question_payload(
        subskill_id="28_total_cost_vehicle_finance",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the monthly payment by 60 months, then add the upfront deposit and the final balloon payment.",
        tier_2=f"Instalments: {_fmt_curr(monthly_pmt * months)}. Add deposit ({_fmt_curr(deposit)}) and balloon ({_fmt_curr(balloon_settlement)}).",
        tier_3=f"Total cost is {_fmt_curr(total_cost)}.",
        r=r,
    )


def generate_29_refinancing_balloon_payment(r: random.Random) -> Dict[str, Any]:
    """Calculate the additional interest cost when refinancing a balloon payment over an extra 24 months."""
    balloon_amount = 90000.00
    refinance_months = 24
    refinance_pmt = 4350.00  # monthly repayment for the 24-month refinance
    total_refinance_cost = refinance_pmt * refinance_months
    extra_interest = total_refinance_cost - balloon_amount

    correct_ans = f"Extra interest = {_fmt_curr(extra_interest)} (Total refinance cost: {_fmt_curr(total_refinance_cost)})"
    custom_options = [
        correct_ans,
        f"Extra interest = R 0,00 (the bank does not charge interest on refinanced balloons)",
        f"Extra interest = {_fmt_curr(balloon_amount * 0.12)}",
        f"Extra interest = {_fmt_curr(extra_interest * 1.5)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"At the end of a 5-year car contract, a driver cannot afford the {_fmt_curr(balloon_amount)} cash lump sum "
        f"to settle the balloon payment. The bank agrees to refinance the {_fmt_curr(balloon_amount)} over an additional "
        f"{refinance_months} months at {_fmt_curr(refinance_pmt)} per month.\n\n"
        f"Calculate the extra interest cost incurred by having to refinance the balloon payment."
    )
    explanation = (
        f"Step 1: Total refinanced payments = {refinance_months} × {_fmt_curr(refinance_pmt)} = {_fmt_curr(total_refinance_cost)} [M].\n"
        f"Step 2: Extra interest = Total payments - Original balloon = {_fmt_curr(total_refinance_cost)} - {_fmt_curr(balloon_amount)} [M].\n"
        f"Step 3: Extra Interest = {_fmt_curr(extra_interest)} [A]."
    )
    return _build_question_payload(
        subskill_id="29_refinancing_balloon_payment",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the refinanced monthly instalment by 24 months, then subtract the original balloon amount.",
        tier_2=f"Total paid = 24 × {_fmt_curr(refinance_pmt)} = {_fmt_curr(total_refinance_cost)}. Subtract {_fmt_curr(balloon_amount)}.",
        tier_3=f"The additional interest cost is {_fmt_curr(extra_interest)}.",
        r=r,
    )


def generate_30_comprehensive_vehicle_budget(r: random.Random) -> Dict[str, Any]:
    """Calculate the true monthly cost of running a vehicle: Instalment + Insurance + Fuel + Maintenance."""
    instalment = r.choice([4850.00, 5200.00, 5600.00])
    insurance = r.choice([1250.00, 1450.00, 1600.00])
    fuel = r.choice([2200.00, 2500.00, 2800.00])
    maintenance = r.choice([450.00, 550.00, 650.00])
    total_monthly = instalment + insurance + fuel + maintenance

    correct_ans = _fmt_curr(total_monthly)
    custom_options = [
        _fmt_curr(total_monthly),
        _fmt_curr(instalment + fuel),
        _fmt_curr(total_monthly * 1.2),
        _fmt_curr(total_monthly - insurance),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A young professional purchases a car and budgets for total monthly operating costs:\n"
        f"• Bank loan instalment: {_fmt_curr(instalment)}\n"
        f"• Comprehensive vehicle insurance: {_fmt_curr(insurance)}\n"
        f"• Estimated monthly fuel expenditure: {_fmt_curr(fuel)}\n"
        f"• Monthly service plan / tyre reserve: {_fmt_curr(maintenance)}\n\n"
        f"Calculate the true total monthly financial commitment required to own and run this vehicle."
    )
    explanation = (
        f"Step 1: Formula: Total Cost = Instalment + Insurance + Fuel + Maintenance [M].\n"
        f"Step 2: Substitute: {_fmt_curr(instalment)} + {_fmt_curr(insurance)} + {_fmt_curr(fuel)} + {_fmt_curr(maintenance)} [M].\n"
        f"Step 3: Total Monthly Cost = {_fmt_curr(total_monthly)} [A]."
    )
    return _build_question_payload(
        subskill_id="30_comprehensive_vehicle_budget",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add all four ongoing vehicle expenses together.",
        tier_2=f"Calculate {_fmt_curr(instalment)} + {_fmt_curr(insurance)} + {_fmt_curr(fuel)} + {_fmt_curr(maintenance)}.",
        tier_3=f"The true monthly cost is {_fmt_curr(total_monthly)}.",
        r=r,
    )


def generate_31_vehicle_depreciation_negative_equity(r: random.Random) -> Dict[str, Any]:
    """Explain negative equity: when market value of vehicle drops below outstanding loan balance."""
    correct_ans = "Negative equity (under water): The vehicle depreciated faster than the loan was amortized, meaning the owner owes more than the car is worth"

    custom_options = [
        correct_ans,
        "Positive equity: The car has appreciated in value relative to the loan balance",
        "Breakeven balance: The vehicle and the loan cancel each other out on the credit bureau",
        "Asset surplus: The bank must refund the difference to the vehicle owner",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"After 3 years of vehicle ownership, a driver wants to trade in their car.\n"
        f"• Outstanding loan balance owed to the bank: R 215 000,00\n"
        f"• Current retail book value of the car: R 165 000,00\n\n"
        f"State the financial term used to describe this situation (a R 50 000 shortfall) and explain why it occurs."
    )
    explanation = (
        f"Step 1: Outstanding debt (R 215 000) exceeds current asset value (R 165 000) by R 50 000 [M].\n"
        f"Step 2: This condition is known as negative equity or being 'under water' on the loan [M].\n"
        f"Step 3: It is typically caused by low deposits, high balloon payments, and steep vehicle depreciation [A]."
    )
    return _build_question_payload(
        subskill_id="31_vehicle_depreciation_negative_equity",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Compare the remaining debt to the current market value of the car.",
        tier_2="When you owe more than the car is worth, the shortfall is called negative equity.",
        tier_3="Negative equity means owing more on the loan than the car's market value.",
        r=r,
    )


def generate_32_comparing_cash_vs_instalment_finance(r: random.Random) -> Dict[str, Any]:
    """Compare total cost of buying a car cash versus financing over 60 months."""
    cash_price = 280000.00
    monthly_instalment = 5850.00
    deposit = 28000.00  # 10%
    months = 60
    finance_total = deposit + (monthly_instalment * months)
    finance_premium = finance_total - cash_price

    correct_ans = f"Financing costs {_fmt_curr(finance_premium)} more than cash (Total finance cost: {_fmt_curr(finance_total)})"
    custom_options = [
        correct_ans,
        f"Cash purchase costs {_fmt_curr(finance_premium)} more due to immediate bank transfer tax",
        f"Both methods cost exactly the same because the car value is identical",
        f"Financing saves {_fmt_curr(deposit)} because the deposit is refunded at the end",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A buyer has the cash available to purchase a car outright for {_fmt_curr(cash_price)}, or can finance it:\n"
        f"• Deposit: {_fmt_curr(deposit)}\n"
        f"• Monthly instalment: {_fmt_curr(monthly_instalment)} for {months} months\n\n"
        f"Calculate how much extra the buyer will pay in finance charges and interest if they choose the 5-year finance agreement."
    )
    explanation = (
        f"Step 1: Total financed cost = {_fmt_curr(deposit)} + ({months} × {_fmt_curr(monthly_instalment)}) = {_fmt_curr(finance_total)} [M].\n"
        f"Step 2: Difference = Financed cost - Cash price = {_fmt_curr(finance_total)} - {_fmt_curr(cash_price)} = {_fmt_curr(finance_premium)} [M].\n"
        f"Step 3: Conclusion: Financing costs {_fmt_curr(finance_premium)} more [A]."
    )
    return _build_question_payload(
        subskill_id="32_comparing_cash_vs_instalment_finance",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the total cost of the finance deal (deposit + 60 instalments) and compare to cash price.",
        tier_2=f"Total finance = {_fmt_curr(deposit)} + (60 × {_fmt_curr(monthly_instalment)}) = {_fmt_curr(finance_total)}. Subtract {_fmt_curr(cash_price)}.",
        tier_3=f"Financing costs an extra {_fmt_curr(finance_premium)} in interest.",
        r=r,
    )
