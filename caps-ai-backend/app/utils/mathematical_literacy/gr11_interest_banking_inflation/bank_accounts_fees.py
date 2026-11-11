"""Bank account types, fee formulas, and statement audits (Subskills 19-27) for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import math
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


def generate_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Compare bank account types: Savings vs Cheque vs 32-Day Notice accounts."""
    prompt = (
        "An individual wants an account that earns a higher interest rate than a regular savings account, "
        "requires giving the bank 32 days' prior warning before withdrawing any funds, and does not have debit order capabilities.\n\n"
        "Which type of bank account best matches this description?"
    )
    correct = "32-Day Notice Deposit Account"
    distractors = [
        "Cheque / Current Account",
        "Credit Card Account",
        "Overdraft Facility Account",
    ]
    options, _ = _build_options(correct, r, [correct] + distractors)
    explanation = (
        "Step 1: Review characteristics of major bank account types:\n"
        "• Cheque/Current Account: For day-to-day transactions and debit orders, with minimal interest.\n"
        "• Savings Account: Easy access, low-to-moderate interest.\n"
        "• Notice Deposit (e.g. 32-Day Notice): Higher interest rate, but funds are locked until the client gives advance notice of withdrawal. [1 mark]\n"
        "Step 2: Match the criteria: The required 32 days' advance notice uniquely identifies a notice account. [1 mark]\n"
        "Step 3: State the matching account:\n"
        f"\\text{{Account type}} = {correct}. [1 mark]"
    )
    return _build_question_payload(
        "subskill_19",
        prompt,
        correct,
        options,
        explanation,
        "Notice deposit accounts require advance notice before withdrawing money.",
        "A 32-day notice deposit account matches all given criteria.",
        f"Answer = {correct}.",
        r,
        difficulty="easy",
    )


def generate_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Calculate ATM cash withdrawal fee with base fee + percentage."""
    name = r.choice(SA_NAMES)
    base_fee = 3.90
    pct = 0.75  # 0,75%
    withdrawal_val = r.choice([400, 600, 800, 1000, 1200])
    pct_fee = round(withdrawal_val * (pct / 100.0), 2)
    total_fee = round(base_fee + pct_fee, 2)
    ans_str = _fmt_curr(total_fee)

    prompt = (
        f"{name} withdraws {_fmt_curr(withdrawal_val)} in cash from an ATM belonging to {r.choice(SA_BANKS)}.\n"
        f"The bank's tariff schedule specifies an ATM cash withdrawal fee formula of:\n"
        f"Fee = R 3,90 + 0,75% of withdrawal value (capped at R 17,00).\n\n"
        f"Calculate the total withdrawal fee charged to {name}'s account."
    )
    explanation = (
        f"Step 1: Calculate 0,75% of the withdrawal amount:\n"
        f"\\text{{Variable Fee}} = {withdrawal_val} \\times 0,0075 = {_fmt_curr(pct_fee)}. [1 mark]\n"
        f"Step 2: Add the fixed base fee of R 3,90:\n"
        f"\\text{{Total Fee}} = 3,90 + {_fmt(pct_fee)} = {total_fee:.2f} [1 mark]\n"
        f"Step 3: Check against the R 17,00 cap (since {_fmt_curr(total_fee)} < R 17,00, the fee is unchanged):\n"
        f"\\text{{Fee payable}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(pct_fee),
        _fmt_curr(base_fee),
        _fmt_curr(round(total_fee + 5.0, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_20",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate 0,75% of the withdrawal amount, then add the R 3,90 base fee.",
        f"Variable fee = {withdrawal_val} × 0,0075 = {_fmt_curr(pct_fee)}. Add R 3,90.",
        f"Total fee = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Applying the maximum bank fee cap when calculated fee exceeds the cap."""
    name = r.choice(SA_NAMES)
    base_fee = 3.90
    pct = 0.75  # 0,75%
    max_cap = 17.00
    withdrawal_val = r.choice([2500, 3000, 4000, 5000])  # Variable fee alone will be 18,75 to 37,50
    pct_fee = round(withdrawal_val * (pct / 100.0), 2)
    uncapped_fee = round(base_fee + pct_fee, 2)
    ans_str = _fmt_curr(max_cap)

    prompt = (
        f"{name} withdraws a large cash amount of {_fmt_curr(withdrawal_val)} from an ATM.\n"
        f"The bank's fee rule is:\n"
        f"Fee = R 3,90 + 0,75% of transaction value (maximum fee: R 17,00).\n\n"
        f"What is the actual fee charged to {name}'s bank account?"
    )
    explanation = (
        f"Step 1: Calculate the formula fee without the cap:\n"
        f"\\text{{Formula Fee}} = 3,90 + ({withdrawal_val} \\times 0,0075) = 3,90 + {_fmt(pct_fee)} = {_fmt_curr(uncapped_fee)}. [1 mark]\n"
        f"Step 2: Compare against the maximum fee limit of R 17,00:\n"
        f"Since the uncapped fee ({_fmt_curr(uncapped_fee)}) exceeds the maximum cap of R 17,00, the fee is capped at R 17,00. [1 mark]\n"
        f"Step 3: State the final fee charged:\n"
        f"\\text{{Fee charged}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(uncapped_fee),
        _fmt_curr(round(uncapped_fee - max_cap, 2)),
        _fmt_curr(base_fee),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_21",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the formula fee, but remember that the fee cannot exceed the maximum cap of R 17,00.",
        f"Calculated fee = {_fmt_curr(uncapped_fee)}, which is greater than the R 17,00 cap.",
        f"Fee charged = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Tiered step-function withdrawal fee: R 1,05 per R 100 or part thereof."""
    name = r.choice(SA_NAMES)
    step_rate = 1.05
    withdrawal_val = r.choice([240, 350, 420, 680, 850, 1150])
    hundreds = math.ceil(withdrawal_val / 100.0)
    fee = round(hundreds * step_rate, 2)
    ans_str = _fmt_curr(fee)

    prompt = (
        f"A bank charges an ATM cash withdrawal fee calculated as:\n"
        f"R 1,05 per R 100,00 or part thereof.\n\n"
        f"{name} makes a cash withdrawal of {_fmt_curr(withdrawal_val)}.\n"
        f"Calculate the bank fee charged for this withdrawal."
    )
    explanation = (
        f"Step 1: Determine the number of R 100 units (rounding up for any partial hundred):\n"
        f"\\text{{Units}} = \\lceil {withdrawal_val} \\div 100 \\rceil = {hundreds}\\text{{ units of R 100}}. [1 mark]\n"
        f"Step 2: Multiply the units by R 1,05 per hundred:\n"
        f"\\text{{Fee}} = {hundreds} \\times 1,05 = {fee:.2f} [1 mark]\n"
        f"Step 3: State the final withdrawal fee:\n"
        f"\\text{{Fee payable}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round((withdrawal_val / 100.0) * step_rate, 2)),  # Without rounding up
        _fmt_curr(round((hundreds - 1) * step_rate, 2)),
        _fmt_curr(round(fee + 2.10, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_22",
        prompt,
        ans_str,
        options,
        explanation,
        f"Round up the withdrawal to the next whole hundred (e.g. R {withdrawal_val} is {hundreds} hundreds) and multiply by R 1,05.",
        f"{withdrawal_val} requires {hundreds} × R 1,05.",
        f"Fee = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Cash-back at retail till point (e.g. Pick n Pay R 2,00) vs ATM withdrawal savings."""
    name = r.choice(SA_NAMES)
    withdrawal_val = 500.0
    atm_fee = 7.65  # Base + % at ATM
    till_fee = 2.00  # Retail till-point cashback fee
    savings = round(atm_fee - till_fee, 2)
    ans_str = _fmt_curr(savings)

    prompt = (
        f"{name} needs to withdraw {_fmt_curr(withdrawal_val)} in cash.\n"
        f"• Option 1 (Bank ATM): Withdrawal fee is {_fmt_curr(atm_fee)}.\n"
        f"• Option 2 (Supermarket till-point cash-back at Shoprite / Pick n Pay): Fixed service fee is {_fmt_curr(till_fee)}.\n\n"
        f"Calculate how much money {name} saves by choosing the till-point cash-back option instead of the ATM."
    )
    explanation = (
        f"Step 1: Identify the fees for both options:\n"
        f"\\text{{ATM Fee}} = {_fmt_curr(atm_fee)}; \\text{{Till-point Fee}} = {_fmt_curr(till_fee)}. [1 mark]\n"
        f"Step 2: Subtract the till-point fee from the ATM fee:\n"
        f"\\text{{Savings}} = {atm_fee:.2f} - {till_fee:.2f} = {savings:.2f} [1 mark]\n"
        f"Step 3: State the savings:\n"
        f"\\text{{Money saved}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(atm_fee),
        _fmt_curr(round(atm_fee + till_fee, 2)),
        _fmt_curr(round(savings * 1.5, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_23",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract the supermarket till-point fee from the ATM withdrawal fee.",
        f"Calculate {atm_fee:.2f} - {till_fee:.2f}.",
        f"Savings = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Own bank ATM vs Saswitch (Other bank's ATM) network penalty fee."""
    name = r.choice(SA_NAMES)
    own_bank = "Nedbank"
    other_bank = "Absa"
    withdrawal_val = 800.0
    own_atm_fee = 9.90
    saswitch_penalty = 12.50
    other_atm_fee = own_atm_fee + saswitch_penalty
    ans_str = _fmt_curr(other_atm_fee)

    prompt = (
        f"{name} holds an account with {own_bank}. A cash withdrawal of {_fmt_curr(withdrawal_val)} at a {own_bank} ATM costs {_fmt_curr(own_atm_fee)}.\n"
        f"Because there was no {own_bank} ATM nearby, {name} used an {other_bank} ATM connected to the Saswitch network.\n"
        f"Using another bank's ATM incurs a Saswitch interbank network surcharge fee of {_fmt_curr(saswitch_penalty)} in addition to the standard withdrawal fee.\n\n"
        f"Calculate the total withdrawal fee charged to {name}."
    )
    explanation = (
        f"Step 1: Set up the total fee components:\n"
        f"\\text{{Total}} = \\text{{Standard ATM Fee}} + \\text{{Saswitch Surcharge}}. [1 mark]\n"
        f"Step 2: Add the fees:\n"
        f"\\text{{Total}} = {own_atm_fee:.2f} + {saswitch_penalty:.2f} = {other_atm_fee:.2f} [1 mark]\n"
        f"Step 3: State the final total fee:\n"
        f"\\text{{Total fee}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(own_atm_fee),
        _fmt_curr(saswitch_penalty),
        _fmt_curr(round(other_atm_fee + 5.0, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_24",
        prompt,
        ans_str,
        options,
        explanation,
        "Add the standard fee and the Saswitch interbank network surcharge.",
        f"Calculate {own_atm_fee:.2f} + {saswitch_penalty:.2f}.",
        f"Total fee = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Comprehensive monthly bank account fee calculation."""
    name = r.choice(SA_NAMES)
    monthly_admin = 45.0
    debit_order_count = 4
    debit_order_fee_each = 3.50
    atm_withdrawals_count = 2
    atm_fee_each = 8.50
    card_swipes_count = 8
    card_swipe_fee = 0.0  # Free POS swipes in modern SA banking

    total_fees = monthly_admin + (debit_order_count * debit_order_fee_each) + (atm_withdrawals_count * atm_fee_each)
    ans_str = _fmt_curr(total_fees)

    prompt = (
        f"During September, {name}'s bank account incurred the following transactions:\n"
        f"• Monthly account maintenance fee: {_fmt_curr(monthly_admin)}\n"
        f"• {debit_order_count} debit orders at {_fmt_curr(debit_order_fee_each)} each\n"
        f"• {atm_withdrawals_count} ATM cash withdrawals at {_fmt_curr(atm_fee_each)} each\n"
        f"• {card_swipes_count} point-of-sale card swipes (Free of charge)\n\n"
        f"Calculate the total bank service fees charged to {name}'s account for the month."
    )
    explanation = (
        f"Step 1: Calculate fees for each category:\n"
        f"- Monthly admin fee = {_fmt_curr(monthly_admin)}\n"
        f"- Debit orders = {debit_order_count} \\times 3,50 = {_fmt_curr(debit_order_count * debit_order_fee_each)}\n"
        f"- ATM withdrawals = {atm_withdrawals_count} \\times 8,50 = {_fmt_curr(atm_withdrawals_count * atm_fee_each)}\n"
        f"- Card swipes = Free (R 0,00). [1 mark]\n"
        f"Step 2: Add all fees together:\n"
        f"\\text{{Total}} = 45,00 + 14,00 + 17,00 = {total_fees:.2f} [1 mark]\n"
        f"Step 3: State the final total monthly bank fee:\n"
        f"\\text{{Total fees}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(total_fees + 15, 2)),
        _fmt_curr(round(total_fees - 10, 2)),
        _fmt_curr(monthly_admin),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_25",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the cost of each item and sum them up.",
        f"Sum: 45 + ({debit_order_count} × 3,50) + ({atm_withdrawals_count} × 8,50).",
        f"Total bank fees = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Bank statement audit: Calculating missing closing balance given opening balance, debits, credits."""
    name = r.choice(SA_NAMES)
    opening_bal = 3450.0
    salary_credit = 14200.0
    rent_debit = 5500.0
    groceries_debit = 1850.0
    fees_debit = 78.50

    closing_bal = round(opening_bal + salary_credit - rent_debit - groceries_debit - fees_debit, 2)
    ans_str = _fmt_curr(closing_bal)

    prompt = (
        f"Refer to the summary of {name}'s bank statement for October:\n"
        f"• Opening Balance: {_fmt_curr(opening_bal)}\n"
        f"• Salary Deposit (Credit): {_fmt_curr(salary_credit)}\n"
        f"• Debit Order (Rent): {_fmt_curr(rent_debit)}\n"
        f"• Card Purchase (Groceries): {_fmt_curr(groceries_debit)}\n"
        f"• Total Bank Charges: {_fmt_curr(fees_debit)}\n\n"
        f"Calculate the Closing Balance on the account."
    )
    explanation = (
        f"Step 1: Set up the formula: Closing Balance = Opening Balance + Credits - Debits. [1 mark]\n"
        f"Step 2: Substitute statement entries:\n"
        f"\\text{{Closing}} = 3\\,450 + 14\\,200 - 5\\,500 - 1\\,850 - 78,50 [1 mark]\n"
        f"Step 3: State the final closing balance:\n"
        f"\\text{{Closing balance}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(closing_bal + 200, 2)),
        _fmt_curr(round(closing_bal - 150, 2)),
        _fmt_curr(round(opening_bal + salary_credit, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_26",
        prompt,
        ans_str,
        options,
        explanation,
        "Add all credits to the opening balance, then subtract all debits and bank fees.",
        f"Closing = 3 450 + 14 200 - 5 500 - 1 850 - 78,50.",
        f"Closing balance = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Evaluating two bank accounts: Fixed monthly bundled option vs Pay-As-You-Transact (PAYT)."""
    name = r.choice(SA_NAMES)
    bundled_fee = 115.0  # R 115/month fixed, all standard transactions included
    # PAYT option: R 6,00 monthly maintenance + R 3,50 per electronic transfer + R 9,00 per withdrawal
    payt_base = 6.0
    transfers = 8
    withdrawals = 4
    payt_total = payt_base + (transfers * 3.50) + (withdrawals * 9.00)
    # 6 + 28 + 36 = 70
    diff = round(abs(bundled_fee - payt_total), 2)
    better = "Pay-As-You-Transact (PAYT)" if payt_total < bundled_fee else "Bundled Option"
    ans_str = f"{better} by {_fmt_curr(diff)}"

    prompt = (
        f"{name} is choosing a pricing plan for a new bank account:\n"
        f"• Plan A (Bundled fee): Fixed fee of {_fmt_curr(bundled_fee)} per month (includes all transfers and ATM withdrawals)\n"
        f"• Plan B (Pay-As-You-Transact): Fixed fee of {_fmt_curr(payt_base)} per month + R 3,50 per transfer + R 9,00 per ATM withdrawal\n\n"
        f"If {name} expects to make {transfers} electronic transfers and {withdrawals} ATM cash withdrawals each month,\n"
        f"which plan is cheaper, and by how much?"
    )
    explanation = (
        f"Step 1: Calculate total monthly cost for Plan B (PAYT):\n"
        f"\\text{{PAYT Total}} = 6,00 + ({transfers} \\times 3,50) + ({withdrawals} \\times 9,00) = 6 + 28 + 36 = {_fmt_curr(payt_total)}. [1 mark]\n"
        f"Step 2: Compare against Plan A ({_fmt_curr(bundled_fee)}):\n"
        f"Plan B ({_fmt_curr(payt_total)}) is cheaper than Plan A ({_fmt_curr(bundled_fee)}). [1 mark]\n"
        f"Step 3: Subtract to find the difference:\n"
        f"{_fmt(bundled_fee)} - {_fmt(payt_total)} = {diff:.2f}.\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{'Bundled Option' if better == 'Pay-As-You-Transact (PAYT)' else 'Pay-As-You-Transact (PAYT)'} by {_fmt_curr(diff)}",
        f"{better} by {_fmt_curr(round(diff * 1.5, 2))}",
        "Both plans cost the exact same amount",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_27",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the cost of the PAYT option and compare it with the R 115 bundled fee.",
        f"PAYT = 6 + ({transfers} × 3,50) + ({withdrawals} × 9) = {_fmt_curr(payt_total)}. Difference = {_fmt_curr(diff)}.",
        f"Outcome = {ans_str}.",
        r,
        difficulty="hard",
    )
