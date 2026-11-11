"""Subskills 33 to 40: Banking Fee Structures & Account Statements.
Covers Pay-As-You-Transact (PAYT) fee schedules, ATM withdrawal formulas,
Saswitch interbank network penalties, bundled vs PAYT comparisons, debit order dishonour fees,
POS card swipe efficiency, credit card finance charges, and annual account fee audits.
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Subskill 33: Itemised Pay-As-You-Transact (PAYT) bank statement fee audit."""
    name = r.choice(SA_NAMES)
    swipes = r.randint(8, 14)
    efts = r.randint(4, 7)
    debit_orders = r.randint(3, 5)

    base_acc_fee = 7.00
    fee_swipe = 1.60
    fee_eft = 2.50
    fee_debit = 3.80

    total_fees = round(
        base_acc_fee + (swipes * fee_swipe) + (efts * fee_eft) + (debit_orders * fee_debit), 2
    )

    prompt = (
        f"{name}'s PAYT transactional bank account has the following fee pricing:\n"
        f"• Monthly account maintenance: R 7,00\n"
        f"• Card swipe (POS purchase): R 1,60 each ({swipes} transactions)\n"
        f"• Electronic Funds Transfer (EFT): R 2,50 each ({efts} transactions)\n"
        f"• External debit order: R 3,80 each ({debit_orders} transactions)\n\n"
        f"Calculate the total bank service fees charged to {name}'s account for the month."
    )

    correct_ans = _fmt_curr(total_fees)
    explanation = (
        f"1. Base maintenance = {_fmt_curr(base_acc_fee)}.\n"
        f"2. Card swipes = {swipes} × R 1,60 = {_fmt_curr(swipes * fee_swipe)}.\n"
        f"3. EFT payments = {efts} × R 2,50 = {_fmt_curr(efts * fee_eft)}.\n"
        f"4. Debit orders = {debit_orders} × R 3,80 = {_fmt_curr(debit_orders * fee_debit)}.\n"
        f"5. Total fees = R 7,00 + {_fmt_curr(swipes * fee_swipe)} + {_fmt_curr(efts * fee_eft)} + {_fmt_curr(debit_orders * fee_debit)} = {_fmt_curr(total_fees)}."
    )
    t1 = "Calculate the subtotal fee for each transaction category."
    t2 = "Don't forget to include the monthly account maintenance fee of R 7,00."
    t3 = f"Total = 7,00 + {swipes * fee_swipe:.2f} + {efts * fee_eft:.2f} + {debit_orders * fee_debit:.2f} = {_fmt_curr(total_fees)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_33",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Subskill 34: ATM cash withdrawal fee formula: Base fee + rate per R100."""
    name = r.choice(SA_NAMES)
    amount_withdrawn = r.choice([800.0, 1200.0, 1500.0, 2000.0])

    # Formula: R 9,00 + R 2,20 per R 100 (or part thereof)
    base_fee = 9.00
    rate_per_hundred = 2.20
    hundreds = int(amount_withdrawn / 100)
    variable_fee = hundreds * rate_per_hundred
    total_atm_fee = round(base_fee + variable_fee, 2)

    prompt = (
        f"A bank charges the following fee formula for cash withdrawals at its own branded ATMs:\n"
        f"Fee = R 9,00 + R 2,20 per R 100 (or part thereof) withdrawn\n\n"
        f"{name} withdraws exactly {_fmt_curr(amount_withdrawn)} from the ATM.\n"
        f"Calculate the bank fee charged for this withdrawal."
    )

    correct_ans = _fmt_curr(total_atm_fee)
    explanation = (
        f"1. Number of R 100 units in {_fmt_curr(amount_withdrawn)} = {int(amount_withdrawn)} ÷ 100 = {hundreds} units.\n"
        f"2. Variable fee = {hundreds} × R 2,20 = {_fmt_curr(variable_fee)}.\n"
        f"3. Total fee = Base fee ({_fmt_curr(base_fee)}) + Variable fee ({_fmt_curr(variable_fee)}) = {_fmt_curr(total_atm_fee)}."
    )
    t1 = f"Divide {_fmt_curr(amount_withdrawn)} by 100 to determine the number of R 100 units ({hundreds})."
    t2 = f"Multiply {hundreds} by R 2,20 to find the variable fee."
    t3 = f"Add the base fee: R 9,00 + {_fmt_curr(variable_fee)} = {_fmt_curr(total_atm_fee)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_34",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Subskill 35: Own-bank ATM vs Saswitch network fee comparison."""
    withdrawal = r.choice([1000.0, 1500.0, 2000.0])
    hundreds = int(withdrawal / 100)

    # Own ATM: R 8,00 + R 2,00 per R100
    own_fee = round(8.00 + (hundreds * 2.00), 2)

    # Saswitch (Another Bank's ATM): R 14,00 + R 2,80 per R100
    saswitch_fee = round(14.00 + (hundreds * 2.80), 2)
    penalty_diff = round(saswitch_fee - own_fee, 2)

    prompt = (
        f"A banking fee guide provides the following cash withdrawal fee formulas:\n"
        f"• Own-Bank ATM: R 8,00 + R 2,00 per R 100\n"
        f"• Other Bank's ATM (Saswitch Network): R 14,00 + R 2,80 per R 100\n\n"
        f"Calculate how much extra a client pays in transaction fees when withdrawing {_fmt_curr(withdrawal)} "
        f"from another bank's ATM instead of an own-bank ATM."
    )

    correct_ans = _fmt_curr(penalty_diff)
    explanation = (
        f"1. Own-bank fee = R 8,00 + ({hundreds} × R 2,00) = R 8,00 + R {hundreds * 2:.2f} = {_fmt_curr(own_fee)}.\n"
        f"2. Saswitch fee = R 14,00 + ({hundreds} × R 2,80) = R 14,00 + R {hundreds * 2.8:.2f} = {_fmt_curr(saswitch_fee)}.\n"
        f"3. Difference = {_fmt_curr(saswitch_fee)} - {_fmt_curr(own_fee)} = {_fmt_curr(penalty_diff)}."
    )
    t1 = f"Calculate the own-bank fee for {_fmt_curr(withdrawal)} ({hundreds} units of R 100)."
    t2 = f"Calculate the Saswitch fee for {_fmt_curr(withdrawal)}."
    t3 = f"Find difference: {_fmt_curr(saswitch_fee)} - {_fmt_curr(own_fee)} = {_fmt_curr(penalty_diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_35",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Subskill 36: Fixed bundled account fee vs PAYT comparison."""
    # Monthly activity: 12 card swipes, 6 EFTs, 4 debit orders, 2 cash withdrawals of R500
    swipes = 12
    efts = 6
    debits = 4
    withdrawals = 2

    # PAYT rates:
    # Base = R 6,00; Swipe = R 1,50; EFT = R 2,20; Debit = R 3,50; Withdrawal = R 10,00 + (5 * R 2,00) = R 20,00 each
    payt_total = round(
        6.00 + (swipes * 1.50) + (efts * 2.20) + (debits * 3.50) + (withdrawals * 20.00), 2
    )

    # Bundled option: R 115,00/month flat (unlimited electronic transactions + 2 free withdrawals)
    bundle_fee = 115.00
    diff = round(abs(payt_total - bundle_fee), 2)
    cheaper = "Bundled Account" if bundle_fee < payt_total else "PAYT Account"

    prompt = (
        f"A client conducts the following monthly banking transactions:\n"
        f"• 12 card swipes @ R 1,50 each\n"
        f"• 6 online EFTs @ R 2,20 each\n"
        f"• 4 debit orders @ R 3,50 each\n"
        f"• 2 own-ATM cash withdrawals of R 500 @ R 20,00 each\n"
        f"• Monthly base fee for PAYT account: R 6,00\n\n"
        f"The bank also offers a Bundled Account package at a flat R 115,00 per month covering all these transactions.\n"
        f"Calculate how much the client saves each month by choosing the cheaper account option."
    )

    correct_ans = _fmt_curr(diff)
    explanation = (
        f"1. PAYT Total = R 6,00 + (12 × R 1,50) + (6 × R 2,20) + (4 × R 3,50) + (2 × R 20,00)\n"
        f"   = R 6,00 + R 18,00 + R 13,20 + R 14,00 + R 40,00 = {_fmt_curr(payt_total)}.\n"
        f"2. Bundled fee = {_fmt_curr(bundle_fee)}.\n"
        f"3. Savings = |{_fmt_curr(payt_total)} - {_fmt_curr(bundle_fee)}| = {_fmt_curr(diff)}.\n"
        f"   {cheaper} is cheaper by {_fmt_curr(diff)}."
    )
    t1 = "Sum all individual PAYT charges including the base fee of R 6,00."
    t2 = f"Compare PAYT total ({_fmt_curr(payt_total)}) with the flat bundle fee ({_fmt_curr(bundle_fee)})."
    t3 = f"Savings = |{_fmt_curr(payt_total)} - {_fmt_curr(bundle_fee)}| = {_fmt_curr(diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_36",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )


def gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Penalty fees calculation: dishonoured debit order charge and late interest."""
    name = r.choice(SA_NAMES)
    debit_order_amount = r.choice([650.0, 850.0, 1200.0])
    dishonour_fee = 115.00  # bank unpaid fee
    merchant_penalty = 150.00  # service provider penalty

    total_penalties = round(dishonour_fee + merchant_penalty, 2)

    prompt = (
        f"{name}'s bank account had insufficient funds when a scheduled insurance debit order of {_fmt_curr(debit_order_amount)} was processed.\n"
        f"As a result:\n"
        f"• The bank charged an unpaid / dishonoured debit order fee of R 115,00\n"
        f"• The insurance provider levied an administrative failed-payment penalty of R 150,00\n\n"
        f"Calculate the total penalty costs incurred by {name} as a result of this single failed transaction."
    )

    correct_ans = _fmt_curr(total_penalties)
    explanation = (
        f"1. Bank penalty fee = {_fmt_curr(dishonour_fee)}.\n"
        f"2. Merchant penalty fee = {_fmt_curr(merchant_penalty)}.\n"
        f"3. Total penalty costs = {_fmt_curr(dishonour_fee)} + {_fmt_curr(merchant_penalty)} = {_fmt_curr(total_penalties)}."
    )
    t1 = "Add both penalty fees together."
    t2 = f"R 115,00 (bank) + R 150,00 (merchant)."
    t3 = f"Total = {_fmt_curr(total_penalties)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_37",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: Card swipe / POS point-of-sale efficiency vs cash withdrawal."""
    grocery_bill = r.choice([1500.0, 1800.0, 2200.0])
    pos_swipe_fee = 0.00  # free point-of-sale card swipes
    atm_cash_fee = round(9.00 + (int(grocery_bill / 100) * 2.20), 2)

    prompt = (
        f"A shopper purchases groceries totaling {_fmt_curr(grocery_bill)} at a supermarket.\n"
        f"The shopper evaluates two payment options:\n"
        f"• Option 1: Swiping a debit card at the point of sale (POS) which is Free (R 0,00 fee)\n"
        f"• Option 2: Withdrawing {_fmt_curr(grocery_bill)} in cash at an ATM beforehand at a fee of "
        f"R 9,00 + R 2,20 per R 100 withdrawn\n\n"
        f"Calculate how much money the shopper saves in bank fees by swiping the card directly instead of withdrawing cash."
    )

    correct_ans = _fmt_curr(atm_cash_fee)
    explanation = (
        f"1. Option 1 (POS swipe fee) = R 0,00.\n"
        f"2. Option 2 (ATM cash fee) = R 9,00 + ({int(grocery_bill / 100)} × R 2,20) = {_fmt_curr(atm_cash_fee)}.\n"
        f"3. Savings = {_fmt_curr(atm_cash_fee)} - R 0,00 = {_fmt_curr(atm_cash_fee)}."
    )
    t1 = f"Calculate the ATM withdrawal fee for {_fmt_curr(grocery_bill)}."
    t2 = "Subtract the zero POS swipe fee from the ATM fee."
    t3 = f"Savings = {_fmt_curr(atm_cash_fee)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_38",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Credit card statement reconciliation: minimum payment due calculation."""
    closing_balance = r.choice([4500.0, 6800.0, 8400.0, 10500.0])
    min_pct = 5.0  # 5% of closing balance or R100 whichever is greater
    min_payment = max(100.0, round(closing_balance * (min_pct / 100.0), 2))

    prompt = (
        f"A credit card monthly statement displays a closing outstanding balance of {_fmt_curr(closing_balance)}.\n"
        f"The credit agreement mandates a minimum monthly repayment of 5% of the closing balance (or R 100, whichever is greater).\n\n"
        f"Calculate the minimum payment due for this billing cycle."
    )

    correct_ans = _fmt_curr(min_payment)
    explanation = (
        f"1. Calculate 5% of the closing balance: {_fmt_curr(closing_balance)} × 0,05 = {_fmt_curr(min_payment)}.\n"
        f"2. Compare with R 100: Since {_fmt_curr(min_payment)} > R 100, the required minimum payment is {_fmt_curr(min_payment)}."
    )
    t1 = f"Multiply {_fmt_curr(closing_balance)} by 0,05 (5%)."
    t2 = "Verify that the result exceeds the minimum statutory threshold of R 100."
    t3 = f"Minimum payment = {_fmt_curr(min_payment)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_39",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: Annual bank fee comparison across different entry-level cheque accounts."""
    # Bank A: Fixed R 65/month all inclusive (65 * 12 = R 780/yr)
    # Bank B: Zero monthly fee, but transactions average R 85/month (85 * 12 = R 1 020/yr)
    monthly_a = 65.00
    monthly_b = 85.00
    annual_a = round(monthly_a * 12, 2)
    annual_b = round(monthly_b * 12, 2)
    annual_diff = round(abs(annual_b - annual_a), 2)

    prompt = (
        f"A young professional compares two bank account fee packages over a 12-month period:\n\n"
        f"• Bank A: Fixed bundled fee of R 65,00 per month covering all transactional activity\n"
        f"• Bank B: R 0,00 monthly maintenance fee, but PAYT fees average R 85,00 per month based on the client's usage profile\n\n"
        f"Calculate how much money the client saves over a full year (12 months) by choosing Bank A."
    )

    correct_ans = _fmt_curr(annual_diff)
    explanation = (
        f"1. Bank A annual cost = R 65,00 × 12 = {_fmt_curr(annual_a)}.\n"
        f"2. Bank B annual cost = R 85,00 × 12 = {_fmt_curr(annual_b)}.\n"
        f"3. Annual savings = {_fmt_curr(annual_b)} - {_fmt_curr(annual_a)} = {_fmt_curr(annual_diff)}."
    )
    t1 = "Multiply both monthly fees by 12 to find the total annual cost."
    t2 = f"Bank A: 65 × 12 = {_fmt_curr(annual_a)}; Bank B: 85 × 12 = {_fmt_curr(annual_b)}."
    t3 = f"Savings = {_fmt_curr(annual_b)} - {_fmt_curr(annual_a)} = {_fmt_curr(annual_diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_40",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )
