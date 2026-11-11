"""Subskills 1 to 8: Tax Foundations & Taxable Income Determination (LB pages 216-221)."""
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


def gen_subskill_01(r: random.Random) -> Dict[str, Any]:
    """Tax 01: Identifying Gross Income vs Net Salary vs Taxable Income."""
    name = r.choice(SA_NAMES)
    gross = r.choice([28500, 34000, 42000, 56000])

    prompt = (
        f"{name} receives a monthly salary slip showing a total earnings figure of {_fmt_curr(gross)}.\n\n"
        f"Which of the following definitions correctly distinguishes between 'Gross Salary', 'Taxable Income', "
        f"and 'Net Salary' in South African tax law?"
    )
    correct_ans = (
        "Gross Salary is total earnings; Taxable Income is Gross minus tax-deductible items; "
        "Net Salary is take-home pay after all deductions and tax"
    )
    custom_opts = [
        correct_ans,
        "Gross Salary is take-home pay; Taxable Income is total deductions; Net Salary is total earnings",
        "Gross Salary and Taxable Income are always identical; Net Salary includes company medical contributions",
        "Taxable Income is take-home pay; Net Salary is gross earnings multiplied by the standard VAT rate",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Gross definition [1 Mark]: Total earnings before any subtractions = Gross Salary.\n"
        f"Step 2: Taxable Income definition [1 Mark]: Gross Income minus allowable tax deductions = Taxable Income.\n"
        f"Step 3: Net Salary definition [1 Mark]: Gross Salary minus all deductions (including PAYE) = Net Salary."
    )
    t1 = "Gross is total earnings, Taxable Income is what SARS taxes, and Net is what enters your bank account."
    t2 = "Taxable Income subtracts only tax-deductible contributions (e.g. pension, UIF), not all deductions."
    t3 = f"The correct distinction is: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_01", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_02(r: random.Random) -> Dict[str, Any]:
    """Tax 02: Classifying deductions: Tax-deductible vs Non-tax-deductible."""
    item = r.choice([
        ("monthly contribution to an approved Pension Fund", "Tax-deductible deduction (reduces taxable income before tax calculation)"),
        ("repayment of a personal loan from the employer", "Non-tax-deductible deduction (paid from after-tax income, does not reduce tax)"),
        ("monthly subscription fee for a Trade Union", "Non-tax-deductible deduction (paid from after-tax income, does not reduce tax)"),
        ("mandatory 1% UIF contribution", "Tax-deductible deduction (reduces taxable income before tax calculation)"),
        ("monthly repayment on a garnishee court order", "Non-tax-deductible deduction (paid from after-tax income, does not reduce tax)"),
    ])
    desc, cat = item

    prompt = (
        f"On a South African employee's monthly payslip, a deduction is made for:\n"
        f"'{desc}'.\n\n"
        f"How is this item classified when determining the employee's personal income tax liability?"
    )
    correct_ans = cat
    custom_opts = [
        cat,
        "Direct medical scheme tax credit (deducted directly from tax owed)",
        "Zero-rated capital rebate exempt from SARS reporting",
        "Fully taxable fringe benefit that increases gross salary",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Identify nature of deduction [1 Mark]: '{desc}' is an employee payslip line item.\n"
        f"Step 2: Tax deductibility rule [1 Mark]: SARS only allows retirement funds, UIF, and approved donations to reduce taxable income.\n"
        f"Step 3: Classification [1 Mark]: {correct_ans}."
    )
    t1 = "Check whether this item reduces taxable income under SARS rules."
    t2 = "Personal loans, court orders, and union fees do not reduce taxable income."
    t3 = f"Classification: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_02", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_03(r: random.Random) -> Dict[str, Any]:
    """Tax 03: Calculating statutory 1% UIF contribution."""
    name = r.choice(SA_NAMES)
    gross = r.choice([12500, 14800, 16200, 17712])

    prompt = (
        f"{name} earns a gross monthly salary of {_fmt_curr(gross)}.\n"
        f"In South Africa, the employee's mandatory Unemployment Insurance Fund (UIF) contribution "
        f"is calculated at 1% of the gross salary (below the statutory remuneration ceiling).\n\n"
        f"Calculate {name}'s monthly UIF deduction in Rands."
    )
    uif = round(gross * 0.01, 2)
    correct_ans = _fmt_curr(uif)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: UIF = 1% × Gross Salary\n"
        f"Step 2: Substitution [1 Mark]: 0,01 × {_fmt_curr(gross)} = {uif:.2f}\n"
        f"Step 3: Solution [1 Mark]: Monthly UIF contribution = {correct_ans}"
    )
    t1 = "UIF is 1% of gross income."
    t2 = f"Multiply {_fmt_curr(gross)} by 0,01."
    t3 = f"UIF = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_03", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_04(r: random.Random) -> Dict[str, Any]:
    """Tax 04: Calculating allowable pension fund contribution deduction (up to 7.5%)."""
    name = r.choice(SA_NAMES)
    gross = r.choice([28000, 34857, 42500, 51000])

    prompt = (
        f"{name} earns a gross monthly salary of {_fmt_curr(gross)} and contributes to a registered pension fund.\n"
        f"According to standard curriculum tax rules, a maximum of 7,5% of gross income is allowable "
        f"as a tax-deductible pension contribution.\n\n"
        f"Calculate the maximum monthly tax-deductible pension deduction for {name}, rounded to the nearest cent."
    )
    pension_cap = round(gross * 0.075, 2)
    correct_ans = _fmt_curr(pension_cap)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Allowable Pension = 7,5% × Gross Salary\n"
        f"Step 2: Substitution [1 Mark]: 0,075 × {_fmt_curr(gross)} = {gross * 0.075:.4f}\n"
        f"Step 3: Rounding [1 Mark]: Allowable deduction = {correct_ans}"
    )
    t1 = "Multiply gross income by 7,5% (0,075)."
    t2 = f"{_fmt_curr(gross)} × 0,075."
    t3 = f"Maximum deductible pension = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_04", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_05(r: random.Random) -> Dict[str, Any]:
    """Tax 05: Calculating monthly Taxable Income from Gross Salary and allowable deductions."""
    name = r.choice(SA_NAMES)
    gross = r.choice([32000, 34857, 38500, 45000])
    uif = round(gross * 0.01, 2)
    pension_deduct = round(gross * 0.075, 2)
    taxable_monthly = round(gross - uif - pension_deduct, 2)

    prompt = (
        f"{name} earns a monthly gross salary of {_fmt_curr(gross)}.\n\n"
        f"The following allowable tax deductions are subtracted before calculating tax:\n"
        f"• UIF contribution (1% of gross): {_fmt_curr(uif)}\n"
        f"• Tax-deductible pension contribution (7,5% of gross): {_fmt_curr(pension_deduct)}\n\n"
        f"Calculate {name}'s monthly Taxable Income (Gross Income - Tax Deductions)."
    )
    correct_ans = _fmt_curr(taxable_monthly)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Taxable Income = Gross Salary - (UIF + Pension Deductions)\n"
        f"Step 2: Substitution [1 Mark]: {_fmt_curr(gross)} - ({_fmt_curr(uif)} + {_fmt_curr(pension_deduct)}) = {_fmt_curr(gross)} - {_fmt_curr(uif + pension_deduct)}\n"
        f"Step 3: Solution [1 Mark]: Monthly Taxable Income = {correct_ans}"
    )
    t1 = "Subtract both allowable deductions (UIF and Pension) from the gross salary."
    t2 = f"{_fmt_curr(gross)} - {_fmt_curr(uif)} - {_fmt_curr(pension_deduct)}."
    t3 = f"Monthly taxable income = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_05", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_06(r: random.Random) -> Dict[str, Any]:
    """Tax 06: Converting monthly Taxable Income to Annual Taxable Income (x 12)."""
    name = r.choice(SA_NAMES)
    monthly_taxable = r.choice([14803.0, 18435.0, 22150.0, 28750.0, 31894.15])
    annual_taxable = round(monthly_taxable * 12.0, 2)

    prompt = (
        f"{name} determines that their monthly taxable income is {_fmt_curr(monthly_taxable)}.\n\n"
        f"SARS tax tables and brackets are structured on an annual basis.\n"
        f"Calculate {name}'s Annual Taxable Income."
    )
    correct_ans = _fmt_curr(annual_taxable)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Annual Taxable Income = Monthly Taxable Income × 12\n"
        f"Step 2: Substitution [1 Mark]: {_fmt_curr(monthly_taxable)} × 12 = {monthly_taxable * 12:.2f}\n"
        f"Step 3: Solution [1 Mark]: Annual Taxable Income = {correct_ans}"
    )
    t1 = "Multiply the monthly taxable income by 12 months."
    t2 = f"{_fmt_curr(monthly_taxable)} × 12."
    t3 = f"Annual taxable income = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_06", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_07(r: random.Random) -> Dict[str, Any]:
    """Tax 07: Converting annual amounts to monthly amounts (/ 12)."""
    name = r.choice(SA_NAMES)
    annual_tax = r.choice([15379.0, 26275.0, 32665.0, 49986.80, 81815.43])
    monthly_tax = round(annual_tax / 12.0, 2)

    prompt = (
        f"After consulting the statutory tax tables and applying all eligible rebates, "
        f"{name}'s total annual income tax liability is calculated as {_fmt_curr(annual_tax)} per year.\n\n"
        f"Calculate the monthly tax deduction (PAYE) that will be deducted from {name}'s salary advice each month."
    )
    correct_ans = _fmt_curr(monthly_tax)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Monthly Tax = Annual Tax ÷ 12\n"
        f"Step 2: Substitution [1 Mark]: {_fmt_curr(annual_tax)} ÷ 12 = {annual_tax / 12.0:.4f}\n"
        f"Step 3: Solution [1 Mark]: Monthly PAYE = {correct_ans}"
    )
    t1 = "Divide the annual tax amount by 12 to find the monthly tax deduction."
    t2 = f"{_fmt_curr(annual_tax)} ÷ 12."
    t3 = f"Monthly tax = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_07", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_08(r: random.Random) -> Dict[str, Any]:
    """Tax 08: Additional income sources (rental income, royalties) added to taxable income."""
    name = r.choice(SA_NAMES)
    salary_taxable = r.choice([240000, 310000, 380000])
    rental_profit = r.choice([36000, 48000, 60000])
    total_taxable = salary_taxable + rental_profit

    prompt = (
        f"{name} earns an annual employment taxable income of {_fmt_curr(salary_taxable)}.\n"
        f"In addition, {name} rents out a garden cottage and generates a net rental profit of "
        f"{_fmt_curr(rental_profit)} during the tax year.\n\n"
        f"Calculate {name}'s Total Annual Taxable Income assessed by SARS."
    )
    correct_ans = _fmt_curr(total_taxable)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Income rule [1 Mark]: Income tax is levied on all sources of income (salary, rent, business profit).\n"
        f"Step 2: Sum [1 Mark]: {_fmt_curr(salary_taxable)} + {_fmt_curr(rental_profit)} = {_fmt_curr(total_taxable)}\n"
        f"Step 3: Solution [1 Mark]: Total Taxable Income = {correct_ans}"
    )
    t1 = "All sources of income are added together to determine total taxable income."
    t2 = f"Add the salary income ({_fmt_curr(salary_taxable)}) and rental profit ({_fmt_curr(rental_profit)})."
    t3 = f"Total = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_08", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )
