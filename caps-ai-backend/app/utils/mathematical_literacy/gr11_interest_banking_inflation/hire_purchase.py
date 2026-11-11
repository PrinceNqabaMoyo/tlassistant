"""Hire purchase (HP) agreements, deposits, and credit costs (Subskills 28-36) for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Calculate cash deposit required on a hire purchase item."""
    name = r.choice(SA_NAMES)
    cash_price = r.choice([6500, 8000, 9500, 12000, 15000, 18000])
    deposit_pct = r.choice([10.0, 15.0, 20.0])
    deposit_amount = round(cash_price * (deposit_pct / 100.0), 2)
    ans_str = _fmt_curr(deposit_amount)

    prompt = (
        f"{name} wants to purchase a refrigerator on hire purchase with a cash price of {_fmt_curr(cash_price)}.\n"
        f"The retail store requires an upfront cash deposit of {_fmt(deposit_pct)}% before the agreement is approved.\n"
        f"Calculate the deposit amount in Rands that {name} must pay upfront."
    )
    explanation = (
        f"Step 1: Convert deposit percentage to a decimal:\n"
        f"{_fmt(deposit_pct)}\\% = \\frac{{{deposit_pct}}}{{100}} = {deposit_pct/100:.2f}. [1 mark]\n"
        f"Step 2: Multiply the cash price by the deposit percentage:\n"
        f"\\text{{Deposit}} = {cash_price} \\times {deposit_pct/100:.2f} = {deposit_amount:.2f} [1 mark]\n"
        f"Step 3: State the final deposit required:\n"
        f"\\text{{Deposit required}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(cash_price - deposit_amount, 2)),
        _fmt_curr(round(deposit_amount * 1.5, 2)),
        _fmt_curr(round(cash_price * 0.05, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_28",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the cash price by {_fmt(deposit_pct)}%.",
        f"Calculate {cash_price} × {deposit_pct/100:.2f}.",
        f"Deposit = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Calculate the balance to be financed after paying deposit."""
    name = r.choice(SA_NAMES)
    cash_price = r.choice([8000, 10000, 12000, 15000, 20000])
    deposit_pct = 10.0
    deposit_amount = cash_price * 0.10
    balance = round(cash_price - deposit_amount, 2)
    ans_str = _fmt_curr(balance)

    prompt = (
        f"A living room lounge suite has a cash price of {_fmt_curr(cash_price)}.\n"
        f"{name} pays a 10% deposit upfront and enters into a hire purchase agreement for the remaining amount.\n"
        f"Calculate the balance that {name} needs to finance through the store."
    )
    explanation = (
        f"Step 1: Calculate the 10% deposit amount:\n"
        f"\\text{{Deposit}} = {cash_price} \\times 0,10 = {_fmt_curr(deposit_amount)}. [1 mark]\n"
        f"Step 2: Subtract the deposit from the cash price:\n"
        f"\\text{{Balance}} = {cash_price} - {_fmt(deposit_amount)} = {balance:.2f} [1 mark]\n"
        f"Step 3: State the remaining financed balance:\n"
        f"\\text{{Balance to be financed}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(deposit_amount),
        _fmt_curr(round(cash_price * 1.1, 2)),
        _fmt_curr(round(balance - 500, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_29",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the 10% deposit and subtract it from the cash price.",
        f"Deposit = {_fmt_curr(deposit_amount)}. Balance = {cash_price} - {_fmt(deposit_amount)}.",
        f"Balance = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Calculate simple interest charged on hire purchase balance over 24/36 months."""
    name = r.choice(SA_NAMES)
    balance = r.choice([6000, 8000, 10000, 12000, 15000])
    interest_rate = r.choice([12.0, 14.0, 15.0, 18.0])
    months = r.choice([24, 36])
    years = months // 12
    interest = round(balance * (interest_rate / 100.0) * years, 2)
    ans_str = _fmt_curr(interest)

    prompt = (
        f"{name} finances a balance of {_fmt_curr(balance)} on a hire purchase agreement over {months} months ({years} years).\n"
        f"The store charges simple interest at a rate of {_fmt(interest_rate)}% per annum on the financed balance.\n"
        f"Calculate the total interest charged on this hire purchase contract.\n"
        f"*(Formula: I = P × r × t.)*"
    )
    explanation = (
        f"Step 1: Identify P, r, and t:\n"
        f"P = {balance}, r = {_fmt(interest_rate)}\\% = {interest_rate/100}, t = {years}\\text{{ years}}. [1 mark]\n"
        f"Step 2: Multiply balance by rate and years:\n"
        f"I = {balance} \\times {interest_rate/100} \\times {years} = {interest:.2f} [1 mark]\n"
        f"Step 3: State the total interest:\n"
        f"\\text{{Total interest}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(balance * (interest_rate / 100.0), 2)),  # 1 year only
        _fmt_curr(round(balance + interest, 2)),
        _fmt_curr(round(interest * 1.5, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_30",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the balance by {interest_rate}% and then by {years} years.",
        f"Calculate {balance} × {interest_rate/100} × {years}.",
        f"Total interest = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Total hire purchase loan amount including interest (Total Financed = Balance + Interest)."""
    name = r.choice(SA_NAMES)
    balance = 9000.0
    interest_rate = 15.0
    years = 2  # 24 months
    interest = balance * (interest_rate / 100.0) * years
    total_financed = round(balance + interest, 2)
    ans_str = _fmt_curr(total_financed)

    prompt = (
        f"A washing machine hire purchase deal has a financed balance of {_fmt_curr(balance)} after paying the deposit.\n"
        f"The store charges {_fmt(interest_rate)}% simple interest per year over a 24-month (2-year) repayment period.\n"
        f"Calculate the total loan amount (financed balance plus total interest) to be repaid."
    )
    explanation = (
        f"Step 1: Calculate total interest over 2 years:\n"
        f"I = 9\\,000 \\times 0,15 \\times 2 = {_fmt_curr(interest)}. [1 mark]\n"
        f"Step 2: Add total interest to the financed balance:\n"
        f"\\text{{Total Financed}} = 9\\,000 + {_fmt(interest)} = {total_financed:.2f} [1 mark]\n"
        f"Step 3: State the total amount to be repaid:\n"
        f"\\text{{Total to be repaid}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(interest),
        _fmt_curr(balance),
        _fmt_curr(round(total_financed + 1000, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_31",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the interest for 2 years and add it to the balance of R 9 000.",
        f"Interest = 9 000 × 0,15 × 2 = {_fmt_curr(interest)}. Total = 9 000 + {_fmt(interest)}.",
        f"Total financed = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Monthly repayment instalment calculation before insurance (Instalment = Total Financed ÷ Months)."""
    name = r.choice(SA_NAMES)
    total_financed = r.choice([7200, 8640, 10800, 12960, 14400, 18000])
    months = r.choice([24, 36])
    instalment = round(total_financed / months, 2)
    ans_str = _fmt_curr(instalment)

    prompt = (
        f"{name}'s hire purchase contract has a total repayment obligation of {_fmt_curr(total_financed)} "
        f"payable in equal monthly instalments over {months} months.\n"
        f"Calculate {name}'s basic monthly instalment (excluding insurance and admin fees)."
    )
    explanation = (
        f"Step 1: Set up the division (Total Financed ÷ Number of Months):\n"
        f"\\text{{Monthly Instalment}} = \\frac{{{total_financed}}}{{{months}}}. [1 mark]\n"
        f"Step 2: Divide the values:\n"
        f"{total_financed} \\div {months} = {instalment:.2f} [1 mark]\n"
        f"Step 3: State the basic monthly instalment:\n"
        f"\\text{{Monthly instalment}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(total_financed / 12, 2)),
        _fmt_curr(round(instalment + 50, 2)),
        _fmt_curr(round(instalment - 50, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_32",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the total financed amount by {months} months.",
        f"Calculate {total_financed} ÷ {months}.",
        f"Monthly instalment = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Compulsory monthly credit life insurance and monthly admin fee addition to instalment."""
    name = r.choice(SA_NAMES)
    base_instalment = 425.0
    credit_life = 32.50
    admin_fee = 45.00
    total_monthly = round(base_instalment + credit_life + admin_fee, 2)
    ans_str = _fmt_curr(total_monthly)

    prompt = (
        f"{name} signed a hire purchase agreement for a sound system with a base instalment of {_fmt_curr(base_instalment)} per month.\n"
        f"The credit provider adds:\n"
        f"• Compulsory credit life protection insurance: {_fmt_curr(credit_life)} per month\n"
        f"• Monthly account administration service fee: {_fmt_curr(admin_fee)} per month\n\n"
        f"Calculate the total actual monthly amount {name} must pay each month."
    )
    explanation = (
        f"Step 1: Identify all recurring monthly charges:\n"
        f"\\text{{Base instalment}} = {_fmt_curr(base_instalment)}; \\text{{Credit life}} = {_fmt_curr(credit_life)}; \\text{{Admin fee}} = {_fmt_curr(admin_fee)}. [1 mark]\n"
        f"Step 2: Add all monthly items together:\n"
        f"\\text{{Total Monthly}} = 425,00 + 32,50 + 45,00 = {total_monthly:.2f} [1 mark]\n"
        f"Step 3: State the final total monthly repayment:\n"
        f"\\text{{Total monthly repayment}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(base_instalment),
        _fmt_curr(round(base_instalment + credit_life, 2)),
        _fmt_curr(round(base_instalment + admin_fee, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_33",
        prompt,
        ans_str,
        options,
        explanation,
        "Add the base instalment, credit life insurance, and monthly admin fee.",
        f"Calculate 425 + 32,50 + 45.",
        f"Total monthly amount = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Grand total cost of hire purchase (Deposit + (Monthly Instalment × Months))."""
    name = r.choice(SA_NAMES)
    deposit = 1200.0
    monthly_payment = 480.0
    months = 24
    total_instalments = monthly_payment * months
    grand_total = round(deposit + total_instalments, 2)
    ans_str = _fmt_curr(grand_total)

    prompt = (
        f"{name} purchased bedroom furniture on hire purchase under the following terms:\n"
        f"• Upfront deposit: {_fmt_curr(deposit)}\n"
        f"• Monthly payment: {_fmt_curr(monthly_payment)} for {months} months\n\n"
        f"Calculate the grand total cost of the furniture paid by {name} at the end of the 24 months."
    )
    explanation = (
        f"Step 1: Calculate total amount paid across all 24 instalments:\n"
        f"\\text{{Total Instalments}} = 480 \\times 24 = {_fmt_curr(total_instalments)}. [1 mark]\n"
        f"Step 2: Add the upfront deposit to the total instalments:\n"
        f"\\text{{Grand Total}} = 1\\,200 + {_fmt(total_instalments)} = {grand_total:.2f} [1 mark]\n"
        f"Step 3: State the grand total cost:\n"
        f"\\text{{Grand total cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(total_instalments),
        _fmt_curr(deposit),
        _fmt_curr(round(grand_total + 1200, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_34",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the monthly payment by {months}, then add the deposit.",
        f"Instalments = 480 × 24 = {_fmt_curr(total_instalments)}. Grand total = 1 200 + {_fmt(total_instalments)}.",
        f"Total cost = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Hire purchase cost comparison against cash purchase: calculating the extra cost of credit."""
    name = r.choice(SA_NAMES)
    cash_price = 7999.0
    deposit = 800.0
    monthly = 420.0
    months = 24
    total_hp = deposit + (monthly * months)  # 800 + 10 080 = 10 880
    extra_cost = round(total_hp - cash_price, 2)
    ans_str = _fmt_curr(extra_cost)

    prompt = (
        f"{name} is considering buying a television:\n"
        f"• Cash price: {_fmt_curr(cash_price)}\n"
        f"• Hire purchase deal: Deposit of {_fmt_curr(deposit)} plus 24 monthly payments of {_fmt_curr(monthly)}\n\n"
        f"Calculate the extra cost of buying the television on credit rather than paying cash."
    )
    explanation = (
        f"Step 1: Calculate total hire purchase cost:\n"
        f"\\text{{HP Total}} = 800 + (420 \\times 24) = 800 + 10\\,080 = {_fmt_curr(total_hp)}. [1 mark]\n"
        f"Step 2: Subtract the cash price from the total HP cost:\n"
        f"\\text{{Extra Cost}} = {_fmt(total_hp)} - 7\\,999 = {extra_cost:.2f} [1 mark]\n"
        f"Step 3: State the extra cost of credit:\n"
        f"\\text{{Extra credit cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(total_hp),
        _fmt_curr(round(extra_cost + 500, 2)),
        _fmt_curr(round(extra_cost - 500, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_35",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the total hire purchase cost and subtract the cash price.",
        f"HP Total = 800 + (420 × 24) = {_fmt_curr(total_hp)}. Extra cost = {_fmt(total_hp)} - 7 999.",
        f"Extra cost = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Percentage extra cost of credit over cash price."""
    cash_price = 8000.0
    total_hp = 11200.0
    extra_cost = total_hp - cash_price  # 3200
    pct_extra = round((extra_cost / cash_price) * 100, 1)
    ans_str = f"{_fmt(pct_extra)}%"

    prompt = (
        f"A home appliance has a cash price of {_fmt_curr(cash_price)}.\n"
        f"On hire purchase, the total amount paid (including deposit and all instalments) comes to {_fmt_curr(total_hp)}.\n"
        f"Calculate the percentage extra that a customer pays by choosing the hire purchase option instead of paying cash.\n"
        f"*(Formula: \\text{{Percentage Extra}} = \\frac{{\\text{{Total HP Cost}} - \\text{{Cash Price}}}}{{\\text{{Cash Price}}}} \\times 100\\%.)*"
    )
    explanation = (
        f"Step 1: Calculate the extra cost in Rands:\n"
        f"\\text{{Extra}} = 11\\,200 - 8\\,000 = {_fmt_curr(extra_cost)}. [1 mark]\n"
        f"Step 2: Divide the extra cost by the cash price and multiply by 100%:\n"
        f"\\text{{Percentage Extra}} = \\frac{{{extra_cost:.0f}}}{{8\\,000}} \\times 100\\% = {pct_extra:.1f}\\% [1 mark]\n"
        f"Step 3: State the final percentage:\n"
        f"\\text{{Percentage extra}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round((extra_cost / total_hp) * 100, 1))}%",
        f"{_fmt(round(pct_extra + 10, 1))}%",
        f"{_fmt(round(pct_extra - 5, 1))}%",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_36",
        prompt,
        ans_str,
        options,
        explanation,
        "Find the extra cost (R 3 200), divide by the cash price (R 8 000), and multiply by 100.",
        f"(3 200 ÷ 8 000) × 100 = {_fmt(pct_extra)}%.",
        f"Percentage extra = {ans_str}.",
        r,
        difficulty="hard",
    )
