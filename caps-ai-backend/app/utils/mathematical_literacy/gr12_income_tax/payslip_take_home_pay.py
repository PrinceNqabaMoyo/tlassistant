"""Subskills 41 to 46: Payslip Take-Home Pay and Salary Increase Analysis (LB pages 231-233)."""
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


def gen_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Tax 41: Total monthly payslip deductions calculation (LB p. 231 example 3.6)."""
    name = r.choice(SA_NAMES)
    pension = 3250.0
    uif = 348.57
    med_aid = 5423.0
    loan = 2500.0
    total_deductions = round(pension + uif + med_aid + loan, 2)

    prompt = (
        f"{name}'s monthly salary advice slip lists the following deductions from gross salary:\n"
        f"• Pension fund: {_fmt_curr(pension)}\n"
        f"• UIF contribution: {_fmt_curr(uif)}\n"
        f"• Medical Aid contribution: {_fmt_curr(med_aid)}\n"
        f"• Repayment of an employer staff loan: {_fmt_curr(loan)}\n\n"
        f"Calculate the total non-tax deductions taken off {name}'s monthly salary (excluding PAYE)."
    )
    correct_ans = _fmt_curr(total_deductions)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Total Deductions = Pension + UIF + Medical Aid + Loan\n"
        f"Step 2: Substitution [1 Mark]: {_fmt_curr(pension)} + {_fmt_curr(uif)} + {_fmt_curr(med_aid)} + {_fmt_curr(loan)} = {total_deductions:.2f}\n"
        f"Step 3: Solution [1 Mark]: Total non-tax deductions = {correct_ans}"
    )
    t1 = "Sum all four listed payroll deduction amounts."
    t2 = f"{_fmt_curr(pension)} + {_fmt_curr(uif)} + {_fmt_curr(med_aid)} + {_fmt_curr(loan)}."
    t3 = f"Total = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_41", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Tax 42: Calculating Net Monthly Take-Home Pay (LB p. 231 example 3.6)."""
    name = r.choice(SA_NAMES)
    gross = 34857.0
    deductions = 11521.57
    tax_owed = 6792.95
    mtc = 1076.0

    # In LB p.231: Take-home Pay = Gross - Deductions - Income Tax + MTC
    # = 34857 - 11521.57 - 6792.95 + 1076 = 17618.48
    take_home = round(gross - deductions - tax_owed + mtc, 2)

    prompt = (
        f"{name} has the following monthly financial breakdown:\n"
        f"• Gross Monthly Income: {_fmt_curr(gross)}\n"
        f"• Total payroll deductions (Pension, UIF, Medical Aid, Loan): {_fmt_curr(deductions)}\n"
        f"• Monthly personal income tax: {_fmt_curr(tax_owed)}\n"
        f"• Monthly Medical Scheme Fees Tax Credit: {_fmt_curr(mtc)}\n\n"
        f"Using the standard formula:\n"
        f"Take-Home Pay = Gross Income - Deductions - Income Tax + Medical Tax Credit\n\n"
        f"Calculate {name}'s net monthly take-home pay."
    )
    correct_ans = _fmt_curr(take_home)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Take-home = Gross - Deductions - Tax + MTC\n"
        f"Step 2: Substitution [1 Mark]: {_fmt_curr(gross)} - {_fmt_curr(deductions)} - {_fmt_curr(tax_owed)} + {_fmt_curr(mtc)} = {take_home:.2f}\n"
        f"Step 3: Solution [1 Mark]: Net take-home pay = {correct_ans}"
    )
    t1 = "Subtract deductions and income tax from gross income, then add the medical tax credit."
    t2 = f"{_fmt_curr(gross)} - {_fmt_curr(deductions)} - {_fmt_curr(tax_owed)} + {_fmt_curr(mtc)}."
    t3 = f"Take-home pay = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_42", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Tax 43: Calculating Net Annual Take-Home Pay."""
    name = r.choice(SA_NAMES)
    gross_taxable = 221220.0
    annual_tax = 32665.0
    net_annual = round(gross_taxable - annual_tax, 2)
    net_monthly = round(net_annual / 12.0, 2)

    prompt = (
        f"{name} has an annual taxable income of {_fmt_curr(gross_taxable)} and pays an annual "
        f"income tax of {_fmt_curr(annual_tax)} (after rebates).\n\n"
        f"1. Calculate {name}'s Net Annual Income (Annual Taxable Income - Annual Tax).\n"
        f"2. Calculate {name}'s equivalent Net Monthly Income (Net Annual ÷ 12)."
    )
    correct_ans = f"Net Annual: {_fmt_curr(net_annual)}; Net Monthly: {_fmt_curr(net_monthly)}"
    custom_opts = [
        correct_ans,
        f"Net Annual: {_fmt_curr(net_annual + annual_tax)}; Net Monthly: {_fmt_curr(round((net_annual + annual_tax) / 12.0, 2))}",
        f"Net Annual: {_fmt_curr(net_annual - 11440.0)}; Net Monthly: {_fmt_curr(round((net_annual - 11440.0) / 12.0, 2))}",
        f"Net Annual: {_fmt_curr(net_annual)}; Net Monthly: {_fmt_curr(round(net_annual / 10.0, 2))}",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Net Annual [1 Mark]: {_fmt_curr(gross_taxable)} - {_fmt_curr(annual_tax)} = {_fmt_curr(net_annual)}\n"
        f"Step 2: Net Monthly [1 Mark]: {_fmt_curr(net_annual)} ÷ 12 = {_fmt_curr(net_monthly)}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Subtract annual tax from annual income, then divide the result by 12."
    t2 = f"{_fmt_curr(gross_taxable)} - {_fmt_curr(annual_tax)} = {_fmt_curr(net_annual)}; divide by 12."
    t3 = f"Results: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_43", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Tax 44: Salary increase impact: calculating net increase in take-home pay."""
    name = r.choice(SA_NAMES)
    old_gross = 25000.0
    increase = r.choice([2500.0, 3000.0, 3500.0, 4000.0])
    new_gross = old_gross + increase

    # In bracket 2: marginal rate is 25%, pension is 7.5%, UIF is 1%
    marginal_tax_rate = 0.25
    pension_rate = 0.075
    uif_rate = 0.01

    tax_on_increase = increase * marginal_tax_rate
    pension_on_increase = increase * pension_rate
    uif_on_increase = increase * uif_rate

    total_deductions_on_inc = tax_on_increase + pension_on_increase + uif_on_increase
    net_increase = round(increase - total_deductions_on_inc, 2)

    d_spec_44 = {
        "diagram_role": "context",
        "kind": "pie_chart",
        "title": f"Gross Increase Deductions ({_fmt_curr(increase)})",
        "slices": [
            {"name": "Net Increase", "value": net_increase},
            {"name": "Income Tax (25%)", "value": tax_on_increase},
            {"name": "Pension (7,5%)", "value": pension_on_increase},
            {"name": "UIF (1%)", "value": uif_on_increase},
        ],
    }

    prompt = (
        f"Refer to the salary increase deduction breakdown for {name} receiving a monthly increase of {_fmt_curr(increase)} (gross).\n"
        f"On this additional amount, the following deductions apply:\n"
        f"• Marginal Income Tax: 25%\n"
        f"• Pension Fund: 7,5%\n"
        f"• UIF: 1%\n\n"
        f"Calculate the actual NET increase that {name} will see in their monthly take-home pay."
    )
    correct_ans = _fmt_curr(net_increase)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Total deduction rate [1 Mark]: 25% + 7,5% + 1% = 33,5%\n"
        f"Step 2: Total deductions on increase [1 Mark]: 33,5% × {_fmt_curr(increase)} = {_fmt_curr(total_deductions_on_inc)}\n"
        f"Step 3: Net increase [1 Mark]: {_fmt_curr(increase)} - {_fmt_curr(total_deductions_on_inc)} = {correct_ans}"
    )
    t1 = "Calculate total deductions on the increase (25% + 7.5% + 1% = 33.5%)."
    t2 = f"Deductions = {_fmt_curr(increase)} × 33,5% = {_fmt_curr(total_deductions_on_inc)}."
    t3 = f"Net increase = {_fmt_curr(increase)} - {_fmt_curr(total_deductions_on_inc)} = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_44", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard",
        diagram_spec=d_spec_44,
    )


def gen_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Tax 45: Debunking bracket creep myth: proving a salary raise never decreases take-home pay."""
    prompt = (
        f"A colleague claims: 'I do not want a promotion with a R 5 000 salary increase because moving into a higher "
        f"tax bracket will cause my take-home pay to decrease.'\n\n"
        f"Based on South Africa's progressive marginal tax bracket system, is this claim true or false, and why?"
    )
    correct_ans = (
        "False. Only the portion of income that exceeds the higher bracket threshold is taxed at the higher marginal rate; "
        "therefore, take-home pay always increases"
    )
    custom_opts = [
        correct_ans,
        "True. Entering a higher bracket causes the higher tax rate to be retroactively applied to all earnings from R 0",
        "True. The secondary rebate is forfeited whenever an employee receives an annual promotion",
        "False. Tax brackets only apply to public sector employees, not private sector companies",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Marginal tax mechanics [1 Mark]: Higher rates apply only to the marginal excess above the threshold.\n"
        f"Step 2: Take-home calculation [1 Mark]: If marginal rate is 35%, the employee keeps 65% of the increase.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "Remember that tax brackets in South Africa are marginal, not retroactive."
    t2 = "The higher rate only applies to the extra money earned above the boundary."
    t3 = f"Correct conclusion: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_45", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Tax 46: Percentage of gross salary lost to total deductions and tax."""
    gross = 30000.0
    total_deductions = 9600.0  # includes tax, pension, uif, medical aid
    take_home = gross - total_deductions
    pct_deducted = round((total_deductions / gross) * 100.0, 2)

    prompt = (
        f"An employee earns a gross monthly salary of {_fmt_curr(gross)}.\n"
        f"After all statutory taxes and payroll deductions, total deductions equal {_fmt_curr(total_deductions)}, "
        f"leaving a take-home pay of {_fmt_curr(take_home)}.\n\n"
        f"Calculate the percentage of the gross salary lost to deductions, rounded to two decimal places."
    )
    correct_ans = f"{_fmt(pct_deducted, 2)}%"
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: (Total Deductions ÷ Gross Salary) × 100%\n"
        f"Step 2: Substitution [1 Mark]: ({total_deductions:.2f} ÷ {gross:.2f}) × 100% = {pct_deducted:.4f}%\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Divide total deductions by gross salary and multiply by 100%."
    t2 = f"({_fmt_curr(total_deductions)} ÷ {_fmt_curr(gross)}) × 100."
    t3 = f"Percentage = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_46", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )
