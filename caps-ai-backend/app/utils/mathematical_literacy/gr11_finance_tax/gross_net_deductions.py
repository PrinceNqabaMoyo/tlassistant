"""Cluster 2: Gross Income, Deductions & Net Salary (Subskills 10 to 18)."""
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


def _gen_gross_salary_basic_plus_allowances(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_gross_salary_basic_plus_allowances"
    name = r.choice(SA_NAMES)
    basic = r.randint(14000, 28000)
    travel = r.choice([1500, 2000, 2500, 3000])
    housing = r.choice([1200, 1800, 2200])
    gross = basic + travel + housing
    correct_ans = _fmt_curr(gross)

    prompt = (
        f"{name}'s employment contract details the following monthly remuneration items:\n"
        f"  • Basic salary: {_fmt_curr(basic)}\n"
        f"  • Travel allowance: {_fmt_curr(travel)}\n"
        f"  • Housing subsidy: {_fmt_curr(housing)}\n\n"
        f"Calculate {name}'s **gross monthly salary**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Gross salary is the total remuneration earned before any deductions are subtracted: "
        f"$$\\text{{Gross Salary}} = \\text{{Basic Salary}} + \\text{{Allowances}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Gross Salary}} = {_fmt_curr(basic)} + {_fmt_curr(travel)} + {_fmt_curr(housing)}$$ "
        f"✓ [1 Mark: Method – summing basic salary and all allowances]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Gross Salary}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency sum]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the basic salary and all allowances together.",
        tier_2=f"{_fmt_curr(basic)} + {_fmt_curr(travel)} + {_fmt_curr(housing)}.",
        tier_3=f"Gross salary = {correct_ans}.",
        r=r,
    )


def _gen_pension_fund_percentage_deduction(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_pension_fund_percentage_deduction"
    name = r.choice(SA_NAMES)
    basic = r.randint(12000, 25000)
    pct = r.choice([7.5, 8.0, 7.0])
    pension = round(basic * (pct / 100.0), 2)
    correct_ans = _fmt_curr(pension)

    prompt = (
        f"{name} earns a basic monthly salary of {_fmt_curr(basic)}.\n"
        f"The company pension fund rules require an employee contribution of **{_fmt(pct)}% of basic salary**.\n\n"
        f"Calculate the monthly pension fund deduction from {name}'s pay."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Pension contributions are calculated as a percentage of basic salary.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Pension Deduction}} = {_fmt_curr(basic)} \\times \\frac{{{_fmt(pct)}}}{{100}} = {_fmt_curr(basic)} \\times {_fmt(pct / 100, 4)}$$ "
        f"✓ [1 Mark: Method – multiplying basic salary by percentage]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Pension Deduction}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency rounded to 2 decimals]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Multiply {_fmt_curr(basic)} by {_fmt(pct)}% (or divide by 100).",
        tier_2=f"{_fmt_curr(basic)} × {_fmt(pct/100, 3)} = {correct_ans}.",
        tier_3=f"Pension deduction = {correct_ans}.",
        r=r,
    )


def _gen_medical_aid_tiered_contribution(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_medical_aid_tiered_contribution"
    name = r.choice(SA_NAMES)
    main_member = 2850.00
    adult_dep = 2150.00
    child_dep = 980.00
    num_children = r.randint(1, 3)
    total_med = round(main_member + adult_dep + (num_children * child_dep), 2)
    correct_ans = _fmt_curr(total_med)

    prompt = (
        f"{name} belongs to a medical aid scheme with the following monthly contribution structure:\n"
        f"  • Principal (main) member: {_fmt_curr(main_member)}\n"
        f"  • Adult dependant (spouse): {_fmt_curr(adult_dep)}\n"
        f"  • Child dependant: {_fmt_curr(child_dep)} per child\n\n"
        f"{name} registers a spouse and **{num_children} child dependants** on the policy.\n\n"
        f"Calculate the total monthly medical aid contribution."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Total contribution is the sum of the main member fee, spouse fee, and child fees: "
        f"$$\\text{{Total}} = \\text{{Main}} + \\text{{Spouse}} + ({num_children} \\times \\text{{Child}})$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Children Cost}} = {num_children} \\times {_fmt_curr(child_dep)} = {_fmt_curr(num_children * child_dep)}$$\n"
        f"$$\\text{{Total Medical Aid}} = {_fmt_curr(main_member)} + {_fmt_curr(adult_dep)} + {_fmt_curr(num_children * child_dep)}$$ "
        f"✓ [1 Mark: Method – summing main member, spouse, and scaled child contributions]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Medical Aid}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency sum]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Multiply {num_children} by {_fmt_curr(child_dep)}, then add the main member and spouse fees.",
        tier_2=f"{_fmt_curr(main_member)} + {_fmt_curr(adult_dep)} + {_fmt_curr(num_children * child_dep)} = {correct_ans}.",
        tier_3=f"Total medical aid = {correct_ans}.",
        r=r,
    )


def _gen_total_deductions_summation(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_total_deductions_summation"
    name = r.choice(SA_NAMES)
    paye = r.randint(2200, 4800)
    uif = r.choice([115.50, 124.78, 108.20])
    pension = r.randint(1200, 2100)
    medical = r.randint(1800, 3200)
    union = 55.00
    total = round(paye + uif + pension + medical + union, 2)
    correct_ans = _fmt_curr(total)

    prompt = (
        f"{name}'s monthly salary slip itemizes the following payroll deductions:\n"
        f"  • PAYE (Income Tax): {_fmt_curr(paye)}\n"
        f"  • UIF contribution: {_fmt_curr(uif)}\n"
        f"  • Pension fund: {_fmt_curr(pension)}\n"
        f"  • Medical aid: {_fmt_curr(medical)}\n"
        f"  • Trade union subscription: {_fmt_curr(union)}\n\n"
        f"Calculate {name}'s **total monthly deductions**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Total deductions are the sum of all statutory (PAYE, UIF) and voluntary deductions.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total Deductions}} = {_fmt_curr(paye)} + {_fmt_curr(uif)} + {_fmt_curr(pension)} + {_fmt_curr(medical)} + {_fmt_curr(union)}$$ "
        f"✓ [1 Mark: Method – summing all listed payroll deduction line items]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Deductions}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency sum]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add all 5 deduction values together.",
        tier_2=f"Sum PAYE, UIF, pension, medical, and union dues.",
        tier_3=f"Total deductions = {correct_ans}.",
        r=r,
    )


def _gen_net_salary_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_net_salary_calculation"
    name = r.choice(SA_NAMES)
    gross = r.randint(18000, 32000)
    deductions = r.randint(4200, 8500)
    net_salary = gross - deductions
    correct_ans = _fmt_curr(net_salary)

    prompt = (
        f"{name} earns a gross monthly salary of {_fmt_curr(gross)}.\n"
        f"The total statutory and non-statutory deductions from {name}'s payslip amount to {_fmt_curr(deductions)}.\n\n"
        f"Calculate {name}'s **net monthly salary** (take-home pay)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Net salary is the actual amount received after subtracting total deductions from gross earnings: "
        f"$$\\text{{Net Salary}} = \\text{{Gross Salary}} - \\text{{Total Deductions}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Net Salary}} = {_fmt_curr(gross)} - {_fmt_curr(deductions)}$$ "
        f"✓ [1 Mark: Method – subtracting deductions from gross pay]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net Salary}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate net take-home salary]"
    )

    options, _ = _build_options(correct_ans, r)
    d_spec = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Gross vs Net Salary Breakdown ({name})",
        "categories": ["Gross Salary", "Deductions", "Net Salary"],
        "values": [gross, deductions, net_salary],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract total deductions from gross salary.",
        tier_2=f"{_fmt_curr(gross)} - {_fmt_curr(deductions)} = {correct_ans}.",
        tier_3=f"Net salary = {correct_ans}.",
        r=r,
    )


def _gen_deductions_as_percentage_of_gross(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_deductions_as_percentage_of_gross"
    name = r.choice(SA_NAMES)
    gross = r.choice([20000, 24000, 25000, 30000])
    deductions = r.choice([5000, 6000, 7200, 7500])
    pct = round((deductions / gross) * 100.0, 1)
    correct_ans = f"{_fmt(pct)}%"

    prompt = (
        f"{name} has a gross monthly remuneration of {_fmt_curr(gross)}.\n"
        f"Total payroll deductions for the month equal {_fmt_curr(deductions)}.\n\n"
        f"Calculate the **total deductions expressed as a percentage** of {name}'s gross salary.\n"
        f"$$\\text{{Percentage}} = \\frac{{\\text{{Total Deductions}}}}{{\\text{{Gross Salary}}}} \\times 100\\%$$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Express the fraction $\\frac{{\\text{{Total Deductions}}}}{{\\text{{Gross Salary}}}}$ as a percentage by multiplying by 100%.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Percentage}} = \\frac{{{deductions}}}{{{gross}}} \\times 100\\%$$ "
        f"✓ [1 Mark: Method – dividing deductions by gross salary and multiplying by 100]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Percentage}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate percentage rounded to 1 decimal]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide total deductions by gross salary and multiply by 100.",
        tier_2=f"({deductions} ÷ {gross}) × 100 = {correct_ans}.",
        tier_3=f"Percentage = {correct_ans}.",
        r=r,
    )


def _gen_taxable_income_pension_deduction(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_taxable_income_pension_deduction"
    name = r.choice(SA_NAMES)
    gross = r.randint(18000, 32000)
    pension = r.randint(1300, 2400)
    taxable = gross - pension
    correct_ans = _fmt_curr(taxable)

    prompt = (
        f"{name} earns a gross monthly remuneration of {_fmt_curr(gross)}.\n"
        f"Under South African tax law, approved pension fund contributions of {_fmt_curr(pension)} "
        f"are tax-deductible before calculating PAYE income tax.\n\n"
        f"Calculate {name}'s **taxable monthly income**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Pension contributions reduce gross income to determine taxable income: "
        f"$$\\text{{Taxable Income}} = \\text{{Gross Salary}} - \\text{{Allowable Pension Deduction}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Taxable Income}} = {_fmt_curr(gross)} - {_fmt_curr(pension)}$$ "
        f"✓ [1 Mark: Method – deducting allowable pension from gross income]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Taxable Income}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency calculation]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract allowable pension from gross salary.",
        tier_2=f"{_fmt_curr(gross)} - {_fmt_curr(pension)} = {correct_ans}.",
        tier_3=f"Taxable income = {correct_ans}.",
        r=r,
    )


def _gen_payslip_missing_value_deduction(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_payslip_missing_value_deduction"
    name = r.choice(SA_NAMES)
    gross = r.randint(22000, 35000)
    net_pay = r.randint(16000, gross - 3000)
    total_deductions = gross - net_pay
    correct_ans = _fmt_curr(total_deductions)

    prompt = (
        f"A portion of {name}'s monthly pay advice is damaged, obscuring the Total Deductions figure:\n\n"
        f"| Payroll Field | Amount |\n"
        f"| :--- | :--- |\n"
        f"| Gross Remuneration | {_fmt_curr(gross)} |\n"
        f"| Total Deductions | **[VALUE A]** |\n"
        f"| Net Pay (Bank Credit) | {_fmt_curr(net_pay)} |\n\n"
        f"Calculate the missing amount **[VALUE A]** representing Total Deductions."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Using the payroll identity: $\\text{{Gross Salary}} - \\text{{Total Deductions}} = \\text{{Net Pay}}$, "
        f"rearrange to solve for deductions: $\\text{{Total Deductions}} = \\text{{Gross Salary}} - \\text{{Net Pay}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{[VALUE A]}} = {_fmt_curr(gross)} - {_fmt_curr(net_pay)}$$ "
        f"✓ [1 Mark: Method – subtracting net pay from gross pay]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{[VALUE A]}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate deductions currency]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract Net Pay from Gross Remuneration.",
        tier_2=f"{_fmt_curr(gross)} - {_fmt_curr(net_pay)} = {correct_ans}.",
        tier_3=f"Value A = {correct_ans}.",
        r=r,
    )


def _gen_overtime_pay_normal_vs_sunday(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_overtime_pay_normal_vs_sunday"
    name = r.choice(SA_NAMES)
    hourly_rate = r.choice([75.0, 80.0, 90.0, 100.0])
    normal_ot_hours = r.choice([6, 8, 10])
    sunday_ot_hours = r.choice([4, 5, 6])

    # South African Basic Conditions of Employment Act (BCEA):
    # Normal overtime (Mon–Sat) = 1.5 x hourly rate
    # Sunday / Public Holiday overtime = 2.0 x hourly rate
    norm_ot_pay = round(normal_ot_hours * (hourly_rate * 1.5), 2)
    sun_ot_pay = round(sunday_ot_hours * (hourly_rate * 2.0), 2)
    total_ot = round(norm_ot_pay + sun_ot_pay, 2)
    correct_ans = _fmt_curr(total_ot)

    prompt = (
        f"{name} earns an ordinary hourly wage rate of {_fmt_curr(hourly_rate)}.\n"
        f"According to South African labour regulations (BCEA):\n"
        f"  • Overtime on weekdays and Saturdays is paid at **1,5 times** normal rate.\n"
        f"  • Overtime on Sundays and Public Holidays is paid at **double time (2,0 times)** normal rate.\n\n"
        f"In one month, {name} worked **{normal_ot_hours} hours** normal weekday overtime and **{sunday_ot_hours} hours** on Sundays.\n\n"
        f"Calculate {name}'s total overtime pay for the month."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate weekday overtime at $1,5\\times$ rate and Sunday overtime at $2,0\\times$ rate, then sum the two amounts.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Weekday Overtime Rate}} = 1,5 \\times {_fmt_curr(hourly_rate)} = {_fmt_curr(hourly_rate * 1.5)}$$\n"
        f"$$\\text{{Weekday Overtime Pay}} = {normal_ot_hours} \\times {_fmt_curr(hourly_rate * 1.5)} = {_fmt_curr(norm_ot_pay)}$$\n"
        f"$$\\text{{Sunday Overtime Rate}} = 2,0 \\times {_fmt_curr(hourly_rate)} = {_fmt_curr(hourly_rate * 2.0)}$$\n"
        f"$$\\text{{Sunday Overtime Pay}} = {sunday_ot_hours} \\times {_fmt_curr(hourly_rate * 2.0)} = {_fmt_curr(sun_ot_pay)}$$\n"
        f"$$\\text{{Total Overtime}} = {_fmt_curr(norm_ot_pay)} + {_fmt_curr(sun_ot_pay)}$$ "
        f"✓ [1 Mark: Method – applying 1,5x and 2,0x multipliers correctly and summing]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Overtime}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate total overtime currency]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Weekday OT = {normal_ot_hours} × 1,5 × {_fmt_curr(hourly_rate)}. Sunday OT = {sunday_ot_hours} × 2 × {_fmt_curr(hourly_rate)}.",
        tier_2=f"{_fmt_curr(norm_ot_pay)} + {_fmt_curr(sun_ot_pay)} = {correct_ans}.",
        tier_3=f"Total overtime = {correct_ans}.",
        r=r,
    )
