"""Subskills 25 to 32: Tax Thresholds and Effective vs Marginal Rates (LB pages 224, 230)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    REBATE_PRIMARY,
    REBATE_SECONDARY,
    REBATE_TERTIARY,
    SA_NAMES,
    THRESHOLD_65_TO_74,
    THRESHOLD_75_AND_OLDER,
    THRESHOLD_UNDER_65,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    calculate_tax_before_rebate,
    get_rebates_for_age,
)


def gen_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Tax 25: Understanding the Tax Threshold: minimum earnings before tax is payable."""
    prompt = (
        f"In South African personal income tax tables, SARS publishes 'Tax Threshold' values for different age categories.\n\n"
        f"Which statement correctly describes what the 'Tax Threshold' represents?"
    )
    correct_ans = (
        "The minimum annual taxable income an individual must earn before becoming liable to pay personal income tax"
    )
    custom_opts = [
        correct_ans,
        "The maximum salary an individual can earn before being moved into the 45% top tax bracket",
        "The flat percentage rate of tax charged on all pension fund payouts",
        "The statutory limit on how much money an employer may deposit into an employee's account",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Curriculum concept [1 Mark]: Tax threshold definition.\n"
        f"Step 2: Economic meaning [1 Mark]: Earnings below this level have all calculated tax cancelled by the tax rebate.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "Look at the definition of tax threshold in the curriculum notes."
    t2 = "It is the income level below which no income tax is owed."
    t3 = f"The tax threshold is: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_25", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Tax 26: Determining if a worker earns below the tax threshold."""
    name = r.choice(SA_NAMES)
    age = r.choice([24, 32, 67, 78])
    if age < 65:
        thresh = THRESHOLD_UNDER_65
        cat = "Under 65"
    elif age < 75:
        thresh = THRESHOLD_65_TO_74
        cat = "Age 65 to 74"
    else:
        thresh = THRESHOLD_75_AND_OLDER
        cat = "Age 75 and older"

    # Half the time below threshold, half above
    below = r.choice([True, False])
    if below:
        income = round(thresh - r.uniform(4000, 12000), 2)
    else:
        income = round(thresh + r.uniform(5000, 15000), 2)

    prompt = (
        f"{name} is {age} years of age and earns an annual taxable income of {_fmt_curr(income)}.\n\n"
        f"SARS Tax Thresholds:\n"
        f"• Under 65: R 63 556\n"
        f"• 65 to 74: R 99 056\n"
        f"• 75 and older: R 110 889\n\n"
        f"Does {name} owe any personal income tax to SARS?"
    )
    if below:
        correct_ans = f"No, because {name}'s taxable income ({_fmt_curr(income)}) is below the {cat} threshold of {_fmt_curr(thresh)}"
    else:
        correct_ans = f"Yes, because {name}'s taxable income ({_fmt_curr(income)}) exceeds the {cat} threshold of {_fmt_curr(thresh)}"

    custom_opts = [
        f"No, because {name}'s taxable income ({_fmt_curr(income)}) is below the {cat} threshold of {_fmt_curr(thresh)}",
        f"Yes, because {name}'s taxable income ({_fmt_curr(income)}) exceeds the {cat} threshold of {_fmt_curr(thresh)}",
        f"No, because all individuals under age 80 are automatically exempt from SARS filing",
        f"Yes, because all employed South Africans must pay a mandatory flat tax of 18%",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Identify applicable threshold [1 Mark]: Age {age} falls in '{cat}' with threshold {_fmt_curr(thresh)}.\n"
        f"Step 2: Comparison [1 Mark]: Income {_fmt_curr(income)} {'<' if below else '>'} {_fmt_curr(thresh)}.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = f"Compare the income with the threshold for age {age} ({_fmt_curr(thresh)})."
    t2 = f"{_fmt_curr(income)} is {'below' if below else 'above'} {_fmt_curr(thresh)}."
    t3 = f"{correct_ans}."

    return _build_question_payload(
        "tax_gr12_26", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Tax 27: Calculating the exact tax threshold for a taxpayer under 65 (Rebate / 18%)."""
    prompt = (
        f"For a taxpayer under 65 years of age, the Primary Rebate is R 11 440.\n"
        f"In Bracket 1 (R 0 to R 160 000), tax is charged at a flat rate of 18%.\n\n"
        f"The tax threshold is the exact income where the 18% tax equals the Primary Rebate:\n"
        f"Tax Threshold × 18% = R 11 440\n\n"
        f"Calculate the exact tax threshold for a person under 65, rounded to the nearest whole Rand."
    )
    thresh = round(REBATE_PRIMARY / 0.18)
    correct_ans = _fmt_curr(thresh)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Threshold = Primary Rebate ÷ 0,18\n"
        f"Step 2: Substitution [1 Mark]: R 11 440 ÷ 0,18 = {REBATE_PRIMARY / 0.18:.4f}\n"
        f"Step 3: Rounding [1 Mark]: {correct_ans} (official SARS threshold: R 63 556)"
    )
    t1 = "Divide the Primary Rebate (R 11 440) by 0,18."
    t2 = f"11 440 ÷ 0,18 = {REBATE_PRIMARY / 0.18:.2f}."
    t3 = f"Threshold = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_27", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Tax 28: Calculating the exact tax threshold for a taxpayer aged 65-74."""
    tot_rebate = REBATE_PRIMARY + REBATE_SECONDARY
    thresh = round(tot_rebate / 0.18)

    prompt = (
        f"For a senior citizen aged between 65 and 74 years:\n"
        f"• Total Rebate (Primary + Secondary): R 11 440 + R 6 390 = {_fmt_curr(tot_rebate)}\n"
        f"• Initial Tax Rate: 18%\n\n"
        f"Calculate the tax threshold for this age group: Total Rebate ÷ 18%."
    )
    correct_ans = _fmt_curr(thresh)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Total rebate [1 Mark]: R 11 440 + R 6 390 = {_fmt_curr(tot_rebate)}\n"
        f"Step 2: Divide by rate [1 Mark]: {_fmt_curr(tot_rebate)} ÷ 0,18 = {tot_rebate / 0.18:.4f}\n"
        f"Step 3: Rounding [1 Mark]: {correct_ans} (official SARS threshold: R 99 056)"
    )
    t1 = "Divide the combined Primary and Secondary rebate by 0,18."
    t2 = f"{_fmt_curr(tot_rebate)} ÷ 0,18."
    t3 = f"Tax threshold = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_28", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Tax 29: Calculating the exact tax threshold for a taxpayer aged 75 and older."""
    tot_rebate = REBATE_PRIMARY + REBATE_SECONDARY + REBATE_TERTIARY
    thresh = round(tot_rebate / 0.18)

    prompt = (
        f"For a taxpayer aged 75 years and older:\n"
        f"• Total Rebate (Primary + Secondary + Tertiary): R 11 440 + R 6 390 + R 2 130 = {_fmt_curr(tot_rebate)}\n"
        f"• Initial Tax Rate: 18%\n\n"
        f"Calculate the tax threshold for taxpayers 75 and older: Total Rebate ÷ 18%."
    )
    correct_ans = _fmt_curr(thresh)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Total rebate [1 Mark]: R 11 440 + R 6 390 + R 2 130 = {_fmt_curr(tot_rebate)}\n"
        f"Step 2: Divide by 18% [1 Mark]: {_fmt_curr(tot_rebate)} ÷ 0,18 = {tot_rebate / 0.18:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans} (official SARS threshold: R 110 889)"
    )
    t1 = "Sum all three rebates and divide by 0,18."
    t2 = f"{_fmt_curr(tot_rebate)} ÷ 0,18."
    t3 = f"Threshold = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_29", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Tax 30: Evaluating the effect of working overtime on pushing taxable income past the tax threshold."""
    name = r.choice(SA_NAMES)
    base_annual = 60000.0
    overtime_annual = 8500.0
    total_taxable = base_annual + overtime_annual
    thresh = THRESHOLD_UNDER_65

    prompt = (
        f"{name} (age 24) has a normal annual taxable salary of {_fmt_curr(base_annual)}, which is below "
        f"the SARS tax threshold of {_fmt_curr(thresh)} (paying R 0,00 tax).\n\n"
        f"During the year, {name} works overtime and earns an additional {_fmt_curr(overtime_annual)}, "
        f"bringing total taxable income to {_fmt_curr(total_taxable)}.\n"
        f"Explain whether {name} now becomes liable to pay income tax, and why."
    )
    tax_before = round(total_taxable * 0.18, 2)
    tax_due = round(tax_before - REBATE_PRIMARY, 2)

    correct_ans = f"Yes, {name} now owes {_fmt_curr(tax_due)} in tax because total income exceeds the threshold by {_fmt_curr(total_taxable - thresh)}"
    custom_opts = [
        correct_ans,
        f"No, because overtime earnings are completely tax-exempt under the Basic Conditions of Employment Act",
        f"Yes, {name} must pay a flat penalty of 40% on all earnings including base salary",
        f"No, because the employer must absorb all tax liabilities exceeding the primary threshold",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Compare with threshold [1 Mark]: Total income {_fmt_curr(total_taxable)} exceeds threshold {_fmt_curr(thresh)} by {_fmt_curr(total_taxable - thresh)}.\n"
        f"Step 2: Tax calculation [1 Mark]: (18% × {_fmt_curr(total_taxable)}) - R 11 440 = {_fmt_curr(tax_before)} - R 11 440 = {_fmt_curr(tax_due)}.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "Check whether the new total income is higher than the threshold (R 63 556)."
    t2 = f"New income = {_fmt_curr(total_taxable)}, which exceeds R 63 556."
    t3 = f"Tax is now payable: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_30", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Tax 31: Effective tax rate calculation: (Net Tax Payable / Taxable Income) * 100%."""
    name = r.choice(SA_NAMES)
    taxable = r.choice([180000.0, 225000.0, 280000.0, 350000.0])
    tax_before, _, _, _, _ = calculate_tax_before_rebate(taxable)
    net_tax = tax_before - REBATE_PRIMARY
    effective_rate = round((net_tax / taxable) * 100.0, 2)

    prompt = (
        f"{name} (age 35) earns an annual taxable income of {_fmt_curr(taxable)}.\n"
        f"After deducting the primary rebate, {name}'s net annual tax payable is {_fmt_curr(net_tax)}.\n\n"
        f"Calculate {name}'s Effective Tax Rate, rounded to two decimal places, using the formula:\n"
        f"Effective Tax Rate = (Net Tax Payable ÷ Taxable Income) × 100%"
    )
    correct_ans = f"{_fmt(effective_rate, 2)}%"
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: ({_fmt_curr(net_tax)} ÷ {_fmt_curr(taxable)}) × 100%\n"
        f"Step 2: Division [1 Mark]: {net_tax:.2f} ÷ {taxable:.2f} = {net_tax / taxable:.6f}\n"
        f"Step 3: Solution [1 Mark]: Effective Tax Rate = {correct_ans}"
    )
    t1 = "Divide the net tax payable by the taxable income, then multiply by 100%."
    t2 = f"({_fmt_curr(net_tax)} ÷ {_fmt_curr(taxable)}) × 100."
    t3 = f"Effective rate = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_31", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Tax 32: Marginal tax rate vs Effective tax rate comparison."""
    prompt = (
        f"A taxpayer's salary advice slip shows that their top slice of income is taxed at a "
        f"Marginal Rate of 30%, but their overall Effective Tax Rate is only 14,2%.\n\n"
        f"What is the mathematical reason why a person's Effective Tax Rate is always lower than their Marginal Tax Rate?"
    )
    correct_ans = (
        "Because of South Africa's progressive tax brackets and rebates: the lower portions of income are taxed "
        "at 0%, 18%, and 25%, pulling down the overall average percentage paid"
    )
    custom_opts = [
        correct_ans,
        "Because SARS refunds 50% of all tax collections at the end of the financial year",
        "Because the employee's company pays the remainder of the tax on their behalf",
        "Because the marginal rate is only paid during the 13th bonus cheque month",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Understand marginal rate [1 Mark]: Marginal rate is the rate applied only to the last Rand earned.\n"
        f"Step 2: Understand effective rate [1 Mark]: Effective rate is the average percentage across all earnings.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "Marginal rate applies only to the highest bracket; earlier brackets are taxed at much lower rates."
    t2 = "Rebates also reduce total tax, making the average (effective) rate significantly lower."
    t3 = f"Reason: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_32", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )
