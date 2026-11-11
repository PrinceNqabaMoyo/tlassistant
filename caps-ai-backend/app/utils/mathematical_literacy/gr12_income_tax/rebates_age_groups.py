"""Subskills 17 to 24: SARS Tax Rebates and Age-Based Tax Deductions (LB pages 224-226)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    REBATE_PRIMARY,
    REBATE_SECONDARY,
    REBATE_TERTIARY,
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    calculate_tax_before_rebate,
    get_rebates_for_age,
)


def gen_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Tax 17: Primary rebate calculation for taxpayers under 65 years."""
    name = r.choice(SA_NAMES)
    age = r.randint(22, 58)

    prompt = (
        f"{name} is {age} years of age and qualifies as an individual taxpayer in South Africa.\n\n"
        f"SARS Tax Rebate Schedule:\n"
        f"• Primary Rebate (all natural persons): R 11 440\n"
        f"• Secondary Rebate (65 years and older): R 6 390\n"
        f"• Tertiary Rebate (75 years and older): R 2 130\n\n"
        f"What is the total annual tax rebate amount that {name} is eligible to deduct from tax owed?"
    )
    correct_ans = _fmt_curr(REBATE_PRIMARY)
    custom_opts = [
        correct_ans,
        _fmt_curr(REBATE_PRIMARY + REBATE_SECONDARY),
        _fmt_curr(REBATE_PRIMARY + REBATE_SECONDARY + REBATE_TERTIARY),
        _fmt_curr(REBATE_SECONDARY),
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Check age qualification [1 Mark]: {name} is {age} years old (under 65 years of age).\n"
        f"Step 2: Rebate eligibility [1 Mark]: Taxpayers under 65 qualify for the Primary Rebate only.\n"
        f"Step 3: Solution [1 Mark]: Total rebate = {correct_ans}."
    )
    t1 = "Taxpayers under 65 only receive the Primary Rebate."
    t2 = f"{name} is {age} years old, so only the primary rebate applies."
    t3 = f"Rebate = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_17", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Tax 18: Secondary rebate calculation for taxpayers aged 65 to 74 years."""
    name = r.choice(SA_NAMES)
    age = r.randint(65, 74)
    total_rebate = REBATE_PRIMARY + REBATE_SECONDARY

    prompt = (
        f"{name} is {age} years old and earns taxable pension income.\n\n"
        f"SARS Tax Rebate Schedule:\n"
        f"• Primary Rebate: R 11 440\n"
        f"• Secondary Rebate (65 and older): R 6 390\n"
        f"• Tertiary Rebate (75 and older): R 2 130\n\n"
        f"Calculate {name}'s total allowable annual tax rebate."
    )
    correct_ans = _fmt_curr(total_rebate)
    custom_opts = [
        correct_ans,
        _fmt_curr(REBATE_PRIMARY),
        _fmt_curr(REBATE_SECONDARY),
        _fmt_curr(REBATE_PRIMARY + REBATE_SECONDARY + REBATE_TERTIARY),
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Age check [1 Mark]: {name} is {age} years old (65 to 74 years).\n"
        f"Step 2: Rebate eligibility [1 Mark]: Qualifies for Primary + Secondary rebate.\n"
        f"Step 3: Sum [1 Mark]: R 11 440 + R 6 390 = {correct_ans}."
    )
    t1 = "Taxpayers aged 65 to 74 qualify for both the Primary and Secondary rebates."
    t2 = f"Add Primary (R 11 440) and Secondary (R 6 390)."
    t3 = f"Total rebate = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_18", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Tax 19: Tertiary rebate calculation for taxpayers aged 75 years and older."""
    name = r.choice(SA_NAMES)
    age = r.randint(75, 88)
    total_rebate = REBATE_PRIMARY + REBATE_SECONDARY + REBATE_TERTIARY

    prompt = (
        f"{name} is a retired senior citizen aged {age} years.\n\n"
        f"SARS Tax Rebate Schedule:\n"
        f"• Primary Rebate: R 11 440\n"
        f"• Secondary Rebate (65 and older): R 6 390\n"
        f"• Tertiary Rebate (75 and older): R 2 130\n\n"
        f"Calculate the total annual tax rebate {name} receives."
    )
    correct_ans = _fmt_curr(total_rebate)
    custom_opts = [
        correct_ans,
        _fmt_curr(REBATE_PRIMARY + REBATE_SECONDARY),
        _fmt_curr(REBATE_PRIMARY),
        _fmt_curr(REBATE_TERTIARY),
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Age qualification [1 Mark]: {name} is {age} years old (75 and older).\n"
        f"Step 2: Rebate eligibility [1 Mark]: Qualifies for all three rebates (Primary + Secondary + Tertiary).\n"
        f"Step 3: Sum [1 Mark]: R 11 440 + R 6 390 + R 2 130 = {correct_ans}."
    )
    t1 = "Taxpayers 75 years and older qualify for all three rebates."
    t2 = f"R 11 440 + R 6 390 + R 2 130."
    t3 = f"Total rebate = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_19", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Tax 20: Calculating annual tax payable after applying age-appropriate rebate."""
    name = r.choice(SA_NAMES)
    age = r.choice([28, 45, 68, 76])
    taxable = r.choice([195000, 240000, 285000, 360000])

    tax_before, b_num, base, rate, thresh = calculate_tax_before_rebate(taxable)
    rebate, rebate_desc = get_rebates_for_age(age)
    net_tax = round(max(0.0, tax_before - rebate), 2)

    prompt = (
        f"{name} is {age} years old and has an annual taxable income of {_fmt_curr(taxable)}.\n"
        f"Their calculated tax before rebates is {_fmt_curr(tax_before)}.\n\n"
        f"Rebate Schedule:\n"
        f"• Primary Rebate: R 11 440 (all individuals)\n"
        f"• Secondary Rebate: R 6 390 (65 and older)\n"
        f"• Tertiary Rebate: R 2 130 (75 and older)\n\n"
        f"Calculate {name}'s Net Annual Tax Payable after deducting the appropriate rebate(s)."
    )
    correct_ans = _fmt_curr(net_tax)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Determine rebate [1 Mark]: Age {age} qualifies for {rebate_desc}.\n"
        f"Step 2: Subtraction [1 Mark]: {_fmt_curr(tax_before)} - {_fmt_curr(rebate)} = {tax_before - rebate:.2f}\n"
        f"Step 3: Solution [1 Mark]: Net Annual Tax = {correct_ans}"
    )
    t1 = f"Identify the total rebate for a {age}-year-old taxpayer."
    t2 = f"Subtract {_fmt_curr(rebate)} from {_fmt_curr(tax_before)}."
    t3 = f"Net tax payable = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_20", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Tax 21: Calculating monthly tax payable (PAYE) after rebates (/ 12)."""
    name = r.choice(SA_NAMES)
    age = r.choice([26, 38, 52])
    taxable = r.choice([221220.0, 283756.0, 350000.0])

    tax_before, _, _, _, _ = calculate_tax_before_rebate(taxable)
    rebate, _ = get_rebates_for_age(age)
    net_annual = max(0.0, tax_before - rebate)
    monthly_paye = round(net_annual / 12.0, 2)

    prompt = (
        f"{name} (age {age}) has an annual taxable income of {_fmt_curr(taxable)}.\n"
        f"• Annual Tax before rebate: {_fmt_curr(tax_before)}\n"
        f"• Applicable Rebate: {_fmt_curr(rebate)}\n\n"
        f"Calculate the monthly personal income tax (PAYE) deducted from {name}'s salary slip each month, "
        f"rounded to two decimal places."
    )
    correct_ans = _fmt_curr(monthly_paye)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Net Annual Tax [1 Mark]: {_fmt_curr(tax_before)} - {_fmt_curr(rebate)} = {_fmt_curr(net_annual)}\n"
        f"Step 2: Divide by 12 [1 Mark]: {_fmt_curr(net_annual)} ÷ 12 = {net_annual / 12.0:.4f}\n"
        f"Step 3: Solution [1 Mark]: Monthly PAYE = {correct_ans}"
    )
    t1 = "Subtract the rebate from the annual tax, then divide by 12."
    t2 = f"({_fmt_curr(tax_before)} - {_fmt_curr(rebate)}) ÷ 12."
    t3 = f"Monthly tax = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_21", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Tax 22: Comparing tax liability of a 30-year-old vs a 68-year-old earning the exact same taxable income."""
    taxable = r.choice([221220.0, 260000.0, 310000.0])
    tax_before, _, _, _, _ = calculate_tax_before_rebate(taxable)

    rebate_young = REBATE_PRIMARY
    rebate_senior = REBATE_PRIMARY + REBATE_SECONDARY

    tax_young = round(tax_before - rebate_young, 2)
    tax_senior = round(tax_before - rebate_senior, 2)
    diff = round(tax_young - tax_senior, 2)

    prompt = (
        f"Xolisa (age 26) and Banele (age 68) both earn the exact same annual taxable income of {_fmt_curr(taxable)}.\n"
        f"Both have an identical annual tax before rebates of {_fmt_curr(tax_before)}.\n\n"
        f"Rebates:\n"
        f"• Primary Rebate: R 11 440\n"
        f"• Secondary Rebate (65 and older): R 6 390\n\n"
        f"Calculate how much LESS annual tax Banele pays compared to Xolisa due to the secondary rebate."
    )
    correct_ans = _fmt_curr(diff)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Xolisa's tax [1 Mark]: {_fmt_curr(tax_before)} - R 11 440 = {_fmt_curr(tax_young)}\n"
        f"Step 2: Banele's tax [1 Mark]: {_fmt_curr(tax_before)} - (R 11 440 + R 6 390) = {_fmt_curr(tax_senior)}\n"
        f"Step 3: Difference [1 Mark]: {_fmt_curr(tax_young)} - {_fmt_curr(tax_senior)} = {correct_ans} (exactly the secondary rebate)"
    )
    t1 = "The difference in tax liability between a taxpayer under 65 and one aged 65-74 is the Secondary Rebate."
    t2 = f"Banele receives an additional R 6 390 rebate."
    t3 = f"Difference = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_22", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Tax 23: Comparing tax liability of a 68-year-old vs a 76-year-old earning the exact same taxable income."""
    taxable = r.choice([250000.0, 320000.0, 380000.0])
    diff = REBATE_TERTIARY

    prompt = (
        f"Mr Modise (age 68) and Mrs Khumalo (age 76) both receive the same annual taxable pension of {_fmt_curr(taxable)}.\n\n"
        f"Rebates:\n"
        f"• Primary Rebate: R 11 440\n"
        f"• Secondary Rebate (65 and older): R 6 390\n"
        f"• Tertiary Rebate (75 and older): R 2 130\n\n"
        f"Calculate the difference in their annual tax liabilities (how much less Mrs Khumalo pays than Mr Modise)."
    )
    correct_ans = _fmt_curr(diff)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Identify rebates [1 Mark]: Both receive Primary and Secondary rebates; Mrs Khumalo also receives the Tertiary rebate.\n"
        f"Step 2: Difference [1 Mark]: Difference is solely the Tertiary rebate of {_fmt_curr(REBATE_TERTIARY)}.\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}."
    )
    t1 = "Mrs Khumalo qualifies for the additional Tertiary Rebate because she is 75 or older."
    t2 = f"The difference is exactly the Tertiary Rebate (R 2 130)."
    t3 = f"Difference = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_23", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Tax 24: Tax rebate ceiling rule: tax cannot be negative when rebates exceed tax before rebates."""
    name = r.choice(SA_NAMES)
    taxable = 45000.0
    tax_before = round(taxable * 0.18, 2)  # R 8 100
    rebate = REBATE_PRIMARY  # R 11 440

    prompt = (
        f"{name} earns an annual taxable income of {_fmt_curr(taxable)} from casual part-time tutoring.\n"
        f"• Tax calculated before rebates: 18% of {_fmt_curr(taxable)} = {_fmt_curr(tax_before)}\n"
        f"• Primary Rebate: {_fmt_curr(rebate)}\n\n"
        f"If the rebate ({_fmt_curr(rebate)}) exceeds the tax calculated before rebates ({_fmt_curr(tax_before)}), "
        f"how much tax must {name} pay, and will SARS pay the negative difference to {name} in cash?"
    )
    correct_ans = "R 0,00 tax payable; SARS will NOT pay out the remaining rebate in cash"
    custom_opts = [
        correct_ans,
        f"R 0,00 tax payable; SARS will refund the {_fmt_curr(rebate - tax_before)} excess directly to {name}'s bank account",
        f"-{_fmt_curr(rebate - tax_before)} negative tax payable, which rolls over as mandatory UIF credit",
        f"{_fmt_curr(tax_before)} full tax payable, because rebates only apply to earnings above R 160 000",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Ceiling rule [1 Mark]: Tax rebates can reduce tax to zero, but never below zero.\n"
        f"Step 2: Calculation [1 Mark]: max(0, {_fmt_curr(tax_before)} - {_fmt_curr(rebate)}) = R 0,00.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "A tax rebate is not a cash grant; it can only reduce tax owed down to R 0,00."
    t2 = "SARS does not refund unused tax rebates in cash."
    t3 = f"Correct conclusion: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_24", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )
