"""Subskills 33 to 40: Medical Scheme Fees Tax Credits (MTC) (LB pages 231, 240)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    MTC_ADDITIONAL_DEPENDANT,
    MTC_FIRST_DEPENDANT,
    MTC_MAIN_MEMBER,
    REBATE_PRIMARY,
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    calculate_tax_before_rebate,
)


def gen_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Tax 33: Calculating monthly Medical Scheme Tax Credit for main member only."""
    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is a single individual with no dependants and is the principal (main) member of a registered medical scheme.\n\n"
        f"SARS Medical Scheme Fees Tax Credit Rates:\n"
        f"• For the taxpayer (main member): R 230,00 per month\n"
        f"• For the first dependant: R 230,00 per month\n"
        f"• For each additional dependant: R 154,00 per month\n\n"
        f"Calculate {name}'s total monthly Medical Scheme Fees Tax Credit."
    )
    correct_ans = _fmt_curr(MTC_MAIN_MEMBER)
    custom_opts = [
        correct_ans,
        _fmt_curr(MTC_MAIN_MEMBER + MTC_FIRST_DEPENDANT),
        _fmt_curr(MTC_ADDITIONAL_DEPENDANT),
        _fmt_curr(MTC_MAIN_MEMBER * 12),
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Identify members [1 Mark]: Main member only (1 person).\n"
        f"Step 2: Apply rate [1 Mark]: R 230,00 for principal member.\n"
        f"Step 3: Solution [1 Mark]: Monthly tax credit = {correct_ans}."
    )
    t1 = "For a single main member with no dependants, only the principal member rate applies."
    t2 = "The rate is R 230,00 per month."
    t3 = f"Credit = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_33", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Tax 34: Calculating monthly Medical Scheme Tax Credit for main member + first dependant."""
    name = r.choice(SA_NAMES)
    spouse = "spouse"

    prompt = (
        f"{name} pays medical scheme contributions covering two people: {name} (main member) and their {spouse} (first dependant).\n\n"
        f"SARS Medical Scheme Fees Tax Credit Rates:\n"
        f"• Main member: R 230,00 per month\n"
        f"• First dependant: R 230,00 per month\n"
        f"• Each additional dependant: R 154,00 per month\n\n"
        f"Calculate the total monthly medical tax credit for this couple."
    )
    tot = MTC_MAIN_MEMBER + MTC_FIRST_DEPENDANT
    correct_ans = _fmt_curr(tot)
    custom_opts = [
        correct_ans,
        _fmt_curr(MTC_MAIN_MEMBER),
        _fmt_curr(MTC_MAIN_MEMBER + MTC_ADDITIONAL_DEPENDANT),
        _fmt_curr(tot * 12),
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Identify rates [1 Mark]: Main member (R 230,00) + First dependant (R 230,00)\n"
        f"Step 2: Sum [1 Mark]: R 230,00 + R 230,00 = {tot:.2f}\n"
        f"Step 3: Solution [1 Mark]: Total monthly credit = {correct_ans}"
    )
    t1 = "Add the main member credit and the first dependant credit."
    t2 = "R 230,00 + R 230,00."
    t3 = f"Credit = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_34", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Tax 35: Calculating monthly Medical Scheme Tax Credit for a family (main + spouse + N children)."""
    name = r.choice(SA_NAMES)
    children = r.choice([2, 3, 4, 5])

    # LB p.231 example 3.5: R230 x 2 + R154 x 4 = R1076
    tot = (MTC_MAIN_MEMBER + MTC_FIRST_DEPENDANT) + (children * MTC_ADDITIONAL_DEPENDANT)

    prompt = (
        f"{name} is the principal member of a medical scheme covering {name}, a spouse, and {children} children.\n\n"
        f"SARS Monthly Medical Tax Credit Allowances:\n"
        f"• Principal member: R 230,00\n"
        f"• First dependant (spouse): R 230,00\n"
        f"• Each additional dependant (child): R 154,00\n\n"
        f"Calculate {name}'s total monthly Medical Scheme Fees Tax Credit."
    )
    correct_ans = _fmt_curr(tot)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Adults credit [1 Mark]: R 230,00 (main) + R 230,00 (spouse) = R 460,00\n"
        f"Step 2: Children credit [1 Mark]: {children} children × R 154,00 = {_fmt_curr(children * MTC_ADDITIONAL_DEPENDANT)}\n"
        f"Step 3: Total [1 Mark]: R 460,00 + {_fmt_curr(children * MTC_ADDITIONAL_DEPENDANT)} = {correct_ans}"
    )
    t1 = "Main member = R 230, First dependant = R 230, and each child = R 154."
    t2 = f"(2 × R 230) + ({children} × R 154)."
    t3 = f"Total = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_35", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Tax 36: Calculating annual Medical Scheme Tax Credit (x 12)."""
    name = r.choice(SA_NAMES)
    children = r.choice([1, 2, 3])
    monthly_mtc = (MTC_MAIN_MEMBER + MTC_FIRST_DEPENDANT) + (children * MTC_ADDITIONAL_DEPENDANT)
    annual_mtc = round(monthly_mtc * 12.0, 2)

    prompt = (
        f"{name}'s family qualifies for a monthly Medical Scheme Fees Tax Credit of {_fmt_curr(monthly_mtc)}.\n\n"
        f"Calculate the total annual Medical Tax Credit that {name} will be credited on their annual tax return."
    )
    correct_ans = _fmt_curr(annual_mtc)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Annual MTC = Monthly MTC × 12\n"
        f"Step 2: Substitution [1 Mark]: {_fmt_curr(monthly_mtc)} × 12 = {monthly_mtc * 12:.2f}\n"
        f"Step 3: Solution [1 Mark]: Annual Medical Tax Credit = {correct_ans}"
    )
    t1 = "Multiply the monthly medical tax credit by 12 months."
    t2 = f"{_fmt_curr(monthly_mtc)} × 12."
    t3 = f"Annual credit = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_36", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Tax 37: Applying MTC to reduce annual personal income tax liability."""
    name = r.choice(SA_NAMES)
    tax_after_rebates = r.choice([32500.0, 48000.0, 65000.0, 81815.43])
    children = r.choice([2, 3, 4])
    monthly_mtc = 460.0 + (children * 154.0)
    annual_mtc = monthly_mtc * 12.0
    final_tax = round(max(0.0, tax_after_rebates - annual_mtc), 2)

    prompt = (
        f"{name}'s annual personal income tax after applying the primary rebate is {_fmt_curr(tax_after_rebates)}.\n"
        f"In addition, {name} qualifies for an annual Medical Scheme Tax Credit of {_fmt_curr(annual_mtc)}.\n\n"
        f"Calculate {name}'s final net annual tax payable to SARS."
    )
    correct_ans = _fmt_curr(final_tax)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Identify tax credit [1 Mark]: MTC is deducted directly from the tax liability.\n"
        f"Step 2: Subtraction [1 Mark]: {_fmt_curr(tax_after_rebates)} - {_fmt_curr(annual_mtc)} = {tax_after_rebates - annual_mtc:.2f}\n"
        f"Step 3: Solution [1 Mark]: Final net annual tax = {correct_ans}"
    )
    t1 = "Subtract the annual medical tax credit directly from the annual tax liability."
    t2 = f"{_fmt_curr(tax_after_rebates)} - {_fmt_curr(annual_mtc)}."
    t3 = f"Net tax = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_37", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Tax 38: Applying MTC to reduce monthly PAYE on a payslip."""
    name = r.choice(SA_NAMES)
    paye_before_mtc = r.choice([3450.0, 4820.0, 5650.0, 6792.95])
    children = r.choice([2, 3, 4])
    monthly_mtc = 460.0 + (children * 154.0)
    paye_after_mtc = round(max(0.0, paye_before_mtc - monthly_mtc), 2)

    prompt = (
        f"An employer calculates that {name}'s monthly tax deduction before medical tax credits is {_fmt_curr(paye_before_mtc)}.\n"
        f"{name} is eligible for a monthly Medical Scheme Fees Tax Credit of {_fmt_curr(monthly_mtc)}.\n\n"
        f"Calculate the actual monthly PAYE amount deducted from {name}'s salary slip."
    )
    correct_ans = _fmt_curr(paye_after_mtc)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Monthly PAYE = Monthly Tax before MTC - Monthly MTC\n"
        f"Step 2: Substitution [1 Mark]: {_fmt_curr(paye_before_mtc)} - {_fmt_curr(monthly_mtc)} = {paye_before_mtc - monthly_mtc:.2f}\n"
        f"Step 3: Solution [1 Mark]: Net monthly PAYE = {correct_ans}"
    )
    t1 = "Subtract the monthly medical tax credit from the preliminary monthly PAYE."
    t2 = f"{_fmt_curr(paye_before_mtc)} - {_fmt_curr(monthly_mtc)}."
    t3 = f"Actual PAYE deducted = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_38", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Tax 39: Comparing medical aid deductions (reduces net pay) vs medical tax credit (reduces tax)."""
    prompt = (
        f"A learner is reviewing a monthly salary advice slip and notices two different medical-related items:\n"
        f"• Item 1: 'Medical Aid Contribution Deduction: -R 5 423,00'\n"
        f"• Item 2: 'Medical Scheme Fees Tax Credit: +R 1 076,00'\n\n"
        f"Which statement correctly explains the difference between these two financial items?"
    )
    correct_ans = (
        "The Medical Aid Contribution is a payroll deduction that reduces net take-home pay, "
        "while the Medical Tax Credit is a direct rebate from SARS that reduces the tax payable"
    )
    custom_opts = [
        correct_ans,
        "Both items are tax deductions that reduce the taxable income before applying the tax brackets",
        "The Medical Aid Contribution is refunded by SARS, while the Medical Tax Credit is paid to the medical scheme",
        "The Medical Tax Credit is an extra tax surcharge paid to SARS for having private health insurance",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Medical contribution role [1 Mark]: Paid to the private medical scheme; reduces employee's bank deposit.\n"
        f"Step 2: Medical tax credit role [1 Mark]: Granted by SARS as a credit against income tax liability.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "Medical aid contribution is what you pay the medical scheme; medical tax credit is a tax relief given by SARS."
    t2 = "Contribution reduces take-home pay; tax credit reduces tax owed."
    t3 = f"Correct explanation: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_39", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Tax 40: Calculating tax payable after both age rebates and medical scheme tax credits."""
    name = r.choice(SA_NAMES)
    age = 42
    taxable = r.choice([280000, 340000, 390000])

    tax_before, _, _, _, _ = calculate_tax_before_rebate(taxable)
    rebate = REBATE_PRIMARY
    tax_after_rebate = tax_before - rebate
    children = 3
    annual_mtc = (460.0 + (children * 154.0)) * 12.0
    final_tax = round(max(0.0, tax_after_rebate - annual_mtc), 2)

    prompt = (
        f"{name} (age {age}) has an annual taxable income of {_fmt_curr(taxable)}.\n"
        f"• Tax before rebates: {_fmt_curr(tax_before)}\n"
        f"• Primary Rebate: R 11 440\n"
        f"• Annual Medical Scheme Fees Tax Credit (family of 5): {_fmt_curr(annual_mtc)}\n\n"
        f"Calculate {name}'s Final Annual Tax Payable after both the primary rebate and medical tax credit."
    )
    correct_ans = _fmt_curr(final_tax)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Tax after primary rebate [1 Mark]: {_fmt_curr(tax_before)} - R 11 440 = {_fmt_curr(tax_after_rebate)}\n"
        f"Step 2: Deduct annual MTC [1 Mark]: {_fmt_curr(tax_after_rebate)} - {_fmt_curr(annual_mtc)} = {tax_after_rebate - annual_mtc:.2f}\n"
        f"Step 3: Solution [1 Mark]: Final tax payable = {correct_ans}"
    )
    t1 = "Subtract the primary rebate, then subtract the annual medical tax credit."
    t2 = f"{_fmt_curr(tax_before)} - R 11 440 - {_fmt_curr(annual_mtc)}."
    t3 = f"Final tax = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_40", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )
