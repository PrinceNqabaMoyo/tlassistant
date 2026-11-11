"""Subskills 47 to 52 for Grade 12 Mathematical Literacy: INCOME TAX.
Covers IRP5 certificates, tax assessments (IT34), tax refunds, additional tax payable,
annual bonus taxation, and dual-employment consolidation.
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
    calculate_tax_before_rebate,
    get_rebates_for_age,
    REBATE_PRIMARY,
)


def gen_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: Interpreting IRP5 certificate fields and calculating taxable remuneration."""
    name = r.choice(SA_NAMES)
    tax_year = r.choice([2024, 2025])
    gross_salary = r.randint(24000, 55000) * 12
    pension = round(gross_salary * r.uniform(0.06, 0.08), 2)
    taxable_remun = gross_salary - pension
    paye_paid, bracket, base, rate, thresh = calculate_tax_before_rebate(taxable_remun)
    paye_net = max(0.0, round(paye_paid - REBATE_PRIMARY, 2))

    prompt = (
        f"{name} received an IRP5 / IT3(a) tax certificate from an employer for the {tax_year} tax year showing the following SARS codes:\n\n"
        f"• Code 3601 (Gross Remuneration): {_fmt_curr(gross_salary)}\n"
        f"• Code 4001 (Pension Fund Contributions): {_fmt_curr(pension)}\n"
        f"• Code 4102 (PAYE / Employees' Tax Withheld): {_fmt_curr(paye_net)}\n\n"
        f"Determine the Taxable Remuneration (Code 3699) that SARS uses to calculate {name}'s final income tax."
    )

    correct_ans = _fmt_curr(taxable_remun)
    explanation = (
        f"1. On a SARS IRP5 certificate, Taxable Remuneration (Code 3699) is calculated as Gross Remuneration (Code 3601) "
        f"minus allowable pension deductions (Code 4001).\n"
        f"2. Taxable Remuneration = {_fmt_curr(gross_salary)} - {_fmt_curr(pension)} = {_fmt_curr(taxable_remun)}."
    )
    t1 = "Identify Gross Remuneration (Code 3601) and Pension Contributions (Code 4001)."
    t2 = "Subtract allowable pension contributions from gross remuneration."
    t3 = f"Calculate: {_fmt_curr(gross_salary)} - {_fmt_curr(pension)} = {_fmt_curr(taxable_remun)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tax_subskill_47",
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


def gen_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Reconciling annual assessed tax vs total monthly PAYE withheld."""
    name = r.choice(SA_NAMES)
    monthly_salary = r.randint(22000, 48000)
    annual_gross = monthly_salary * 12
    pension = round(annual_gross * 0.075, 2)
    taxable_inc = annual_gross - pension

    tax_calc, _, _, _, _ = calculate_tax_before_rebate(taxable_inc)
    annual_tax_due = max(0.0, round(tax_calc - REBATE_PRIMARY, 2))

    monthly_paye_deducted = round(annual_tax_due / 12, 2)
    diff = r.choice([-1500.0, -850.0, -420.0, 680.0, 1250.0, 2100.0])
    total_paye_paid = round(annual_tax_due + diff, 2)

    if diff > 0:
        correct_status = "Refund from SARS"
        diff_abs = diff
        correct_ans = f"Refund of {_fmt_curr(diff_abs)} from SARS"
    else:
        correct_status = "Amount payable to SARS"
        diff_abs = abs(diff)
        correct_ans = f"Payment of {_fmt_curr(diff_abs)} to SARS"

    prompt = (
        f"{name}'s SARS Notice of Assessment (IT34) for the tax year shows:\n\n"
        f"• Final Tax Assessed Liability: {_fmt_curr(annual_tax_due)}\n"
        f"• Total PAYE already paid via employer payroll: {_fmt_curr(total_paye_paid)}\n\n"
        f"Determine the final assessment result for {name}."
    )

    explanation = (
        f"1. Compare total PAYE paid ({_fmt_curr(total_paye_paid)}) with final assessed tax ({_fmt_curr(annual_tax_due)}).\n"
        f"2. Difference = {_fmt_curr(total_paye_paid)} - {_fmt_curr(annual_tax_due)} = {_fmt_curr(diff)}.\n"
        f"3. Since PAYE paid is {'greater' if diff > 0 else 'less'} than tax liability, {name} receives a {correct_ans}."
    )
    t1 = "Compare total tax paid via PAYE against final assessed liability."
    t2 = "If PAYE paid > liability, SARS owes a refund; if PAYE paid < liability, taxpayer owes SARS."
    t3 = f"Calculate difference: |{_fmt_curr(total_paye_paid)} - {_fmt_curr(annual_tax_due)}| = {_fmt_curr(diff_abs)}. Result: {correct_ans}."

    custom_opts = [
        f"Refund of {_fmt_curr(diff_abs)} from SARS",
        f"Payment of {_fmt_curr(diff_abs)} to SARS",
        f"Refund of {_fmt_curr(round(diff_abs * 1.1, 2))} from SARS",
        f"Payment of {_fmt_curr(round(diff_abs * 1.1, 2))} to SARS",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_tax_subskill_48",
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


def gen_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Tax refund calculation from Section 18A donation / private RA deduction."""
    name = r.choice(SA_NAMES)
    salary_annual = r.randint(300000, 550000)
    tax_orig, _, _, _, _ = calculate_tax_before_rebate(salary_annual)
    paye_paid = max(0.0, round(tax_orig - REBATE_PRIMARY, 2))

    donation = r.randint(8, 25) * 1000
    revised_taxable = salary_annual - donation
    tax_new, _, _, _, _ = calculate_tax_before_rebate(revised_taxable)
    revised_tax_liability = max(0.0, round(tax_new - REBATE_PRIMARY, 2))
    refund_due = round(paye_paid - revised_tax_liability, 2)

    prompt = (
        f"{name} (age 35) had an annual salary of {_fmt_curr(salary_annual)} on which PAYE of {_fmt_curr(paye_paid)} "
        f"was deducted by the employer.\n"
        f"At tax year-end, {name} claimed an allowable Section 18A donation deduction of {_fmt_curr(donation)} to a registered charity.\n\n"
        f"Calculate the refund due to {name} from SARS after this deduction is assessed."
    )

    correct_ans = _fmt_curr(refund_due)
    explanation = (
        f"1. Original PAYE paid = {_fmt_curr(paye_paid)}.\n"
        f"2. Revised taxable income = {_fmt_curr(salary_annual)} - {_fmt_curr(donation)} = {_fmt_curr(revised_taxable)}.\n"
        f"3. Revised tax before rebate = {_fmt_curr(tax_new)}.\n"
        f"4. Revised tax after primary rebate ({_fmt_curr(REBATE_PRIMARY)}) = {_fmt_curr(revised_tax_liability)}.\n"
        f"5. SARS Refund = PAYE paid - Revised tax = {_fmt_curr(paye_paid)} - {_fmt_curr(revised_tax_liability)} = {_fmt_curr(refund_due)}."
    )
    t1 = "Subtract the donation from original taxable income to find revised taxable income."
    t2 = "Calculate new tax from SARS brackets and subtract the primary rebate."
    t3 = f"Refund = {_fmt_curr(paye_paid)} - {_fmt_curr(revised_tax_liability)} = {_fmt_curr(refund_due)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tax_subskill_49",
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


def gen_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: Additional tax payable on assessment due to unwithheld rental / freelance income."""
    name = r.choice(SA_NAMES)
    salary_annual = r.randint(280000, 450000)
    tax_orig, _, _, _, _ = calculate_tax_before_rebate(salary_annual)
    paye_paid = max(0.0, round(tax_orig - REBATE_PRIMARY, 2))

    freelance_profit = r.randint(30, 80) * 1000
    revised_taxable = salary_annual + freelance_profit
    tax_new, _, _, _, _ = calculate_tax_before_rebate(revised_taxable)
    revised_tax_liability = max(0.0, round(tax_new - REBATE_PRIMARY, 2))
    extra_tax_due = round(revised_tax_liability - paye_paid, 2)

    prompt = (
        f"{name} (age 42) earned an annual salary of {_fmt_curr(salary_annual)} on which the employer deducted {_fmt_curr(paye_paid)} PAYE.\n"
        f"During the same tax year, {name} earned net freelance consulting income of {_fmt_curr(freelance_profit)} with zero tax deducted at source.\n\n"
        f"Calculate the additional tax {name} must pay to SARS on final assessment."
    )

    correct_ans = _fmt_curr(extra_tax_due)
    explanation = (
        f"1. Total taxable income = Salary ({_fmt_curr(salary_annual)}) + Freelance ({_fmt_curr(freelance_profit)}) = {_fmt_curr(revised_taxable)}.\n"
        f"2. Total tax liability from table before rebate = {_fmt_curr(tax_new)}.\n"
        f"3. Total tax after primary rebate ({_fmt_curr(REBATE_PRIMARY)}) = {_fmt_curr(revised_tax_liability)}.\n"
        f"4. Additional tax payable to SARS = Total tax ({_fmt_curr(revised_tax_liability)}) - PAYE already paid ({_fmt_curr(paye_paid)}) = {_fmt_curr(extra_tax_due)}."
    )
    t1 = "Add freelance income to salary to find total annual taxable income."
    t2 = "Calculate total tax liability on combined income and subtract the primary rebate."
    t3 = f"Subtract PAYE already paid from total liability: {_fmt_curr(revised_tax_liability)} - {_fmt_curr(paye_paid)} = {_fmt_curr(extra_tax_due)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tax_subskill_50",
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


def gen_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: Taxation of an annual bonus (13th cheque) using SARS annualised tax method."""
    name = r.choice(SA_NAMES)
    monthly_basic = r.randint(20, 45) * 1000
    annual_basic = monthly_basic * 12
    bonus = monthly_basic  # 13th cheque equals one month salary

    tax_no_bonus, _, _, _, _ = calculate_tax_before_rebate(annual_basic)
    net_tax_no_bonus = max(0.0, round(tax_no_bonus - REBATE_PRIMARY, 2))

    total_with_bonus = annual_basic + bonus
    tax_with_bonus, _, _, _, _ = calculate_tax_before_rebate(total_with_bonus)
    net_tax_with_bonus = max(0.0, round(tax_with_bonus - REBATE_PRIMARY, 2))

    bonus_tax = round(net_tax_with_bonus - net_tax_no_bonus, 2)
    net_bonus = round(bonus - bonus_tax, 2)

    d_spec_51 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Annual Bonus Tax Breakdown ({_fmt_curr(bonus)})",
        "categories": ["Gross Bonus", "Bonus Tax (SARS)", "Net Bonus"],
        "series": [
            {"name": "Amount", "values": [bonus, bonus_tax, net_bonus]}
        ],
    }

    prompt = (
        f"Refer to the bonus taxation structure for {name} (age 30) earning {_fmt_curr(monthly_basic)} per month.\n"
        f"In December, {name} receives a 13th cheque bonus of {_fmt_curr(bonus)}.\n"
        f"SARS rules require tax on the bonus to be calculated as the difference between the annual tax on total earnings (including bonus) "
        f"and annual tax on regular earnings without bonus.\n\n"
        f"Calculate the net bonus {name} receives in cash after bonus tax is deducted."
    )

    correct_ans = _fmt_curr(net_bonus)
    explanation = (
        f"1. Annual tax without bonus: on {_fmt_curr(annual_basic)} is {_fmt_curr(net_tax_no_bonus)} after rebate.\n"
        f"2. Annual tax with bonus: total earnings = {_fmt_curr(total_with_bonus)}. Tax is {_fmt_curr(net_tax_with_bonus)} after rebate.\n"
        f"3. Tax deducted on bonus = {_fmt_curr(net_tax_with_bonus)} - {_fmt_curr(net_tax_no_bonus)} = {_fmt_curr(bonus_tax)}.\n"
        f"4. Net bonus received = Bonus ({_fmt_curr(bonus)}) - Tax on bonus ({_fmt_curr(bonus_tax)}) = {_fmt_curr(net_bonus)}."
    )
    t1 = "Calculate annual tax on salary alone and on salary + bonus."
    t2 = "Find tax on the bonus by subtracting tax without bonus from tax with bonus."
    t3 = f"Calculate net bonus: {_fmt_curr(bonus)} - {_fmt_curr(bonus_tax)} = {_fmt_curr(net_bonus)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tax_subskill_51",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_51,
    )


def gen_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Dual-employment tax consolidation and shortfall calculation."""
    name = r.choice(SA_NAMES)
    job1_annual = r.randint(18, 30) * 10000
    job2_annual = r.randint(10, 20) * 10000

    # Job 1 PAYE calculated with primary rebate
    tax1, _, _, _, _ = calculate_tax_before_rebate(job1_annual)
    paye_job1 = max(0.0, round(tax1 - REBATE_PRIMARY, 2))

    # Job 2 PAYE calculated also with primary rebate (standard employer error)
    tax2, _, _, _, _ = calculate_tax_before_rebate(job2_annual)
    paye_job2 = max(0.0, round(tax2 - REBATE_PRIMARY, 2))

    total_paye_withheld = round(paye_job1 + paye_job2, 2)
    consolidated_income = job1_annual + job2_annual

    # True SARS liability allows ONLY ONE primary rebate
    true_tax, _, _, _, _ = calculate_tax_before_rebate(consolidated_income)
    true_liability = max(0.0, round(true_tax - REBATE_PRIMARY, 2))

    tax_shortfall = round(true_liability - total_paye_withheld, 2)

    prompt = (
        f"{name} (age 28) worked two part-time jobs during the tax year:\n\n"
        f"• Employer A: Taxable earnings {_fmt_curr(job1_annual)}, PAYE withheld {_fmt_curr(paye_job1)}\n"
        f"• Employer B: Taxable earnings {_fmt_curr(job2_annual)}, PAYE withheld {_fmt_curr(paye_job2)}\n\n"
        f"Both employers applied the primary rebate of {_fmt_curr(REBATE_PRIMARY)} independently.\n"
        f"When SARS consolidates {name}'s tax return, only ONE primary rebate is allowed.\n\n"
        f"Calculate the tax shortfall {name} owes to SARS on final assessment."
    )

    correct_ans = _fmt_curr(tax_shortfall)
    explanation = (
        f"1. Consolidated annual taxable income = {_fmt_curr(job1_annual)} + {_fmt_curr(job2_annual)} = {_fmt_curr(consolidated_income)}.\n"
        f"2. Total tax from SARS table before rebates = {_fmt_curr(true_tax)}.\n"
        f"3. True tax liability after single primary rebate ({_fmt_curr(REBATE_PRIMARY)}) = {_fmt_curr(true_liability)}.\n"
        f"4. Total PAYE already paid by both employers = {_fmt_curr(paye_job1)} + {_fmt_curr(paye_job2)} = {_fmt_curr(total_paye_withheld)}.\n"
        f"5. Tax shortfall owed to SARS = {_fmt_curr(true_liability)} - {_fmt_curr(total_paye_withheld)} = {_fmt_curr(tax_shortfall)}."
    )
    t1 = "Sum earnings from both employers to find consolidated taxable income."
    t2 = "Calculate true tax on consolidated income and subtract exactly one primary rebate."
    t3 = f"Subtract total PAYE paid ({_fmt_curr(total_paye_withheld)}) from true tax ({_fmt_curr(true_liability)}) = {_fmt_curr(tax_shortfall)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tax_subskill_52",
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
