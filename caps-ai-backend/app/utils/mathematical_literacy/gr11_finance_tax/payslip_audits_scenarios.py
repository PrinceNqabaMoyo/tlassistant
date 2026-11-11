"""Cluster 6: Payslip Audits, Financial Decision Making & Real-World Scenarios (Subskills 45 to 52)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_COMPANIES,
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def _gen_payslip_comprehensive_audit(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_payslip_comprehensive_audit"
    name = r.choice(SA_NAMES)
    company = r.choice(SA_COMPANIES)
    basic = 22000.00
    allowance = 2500.00
    gross = basic + allowance  # 24500

    paye = 3450.00
    uif = 124.78  # capped at 124.78
    pension = 1650.00
    medical = 2400.00
    total_deductions = round(paye + uif + pension + medical, 2)
    net_pay = round(gross - total_deductions, 2)
    correct_ans = _fmt_curr(net_pay)

    prompt = (
        f"Examine the official monthly payslip extract for {name} employed at {company}:\n\n"
        f"| EARNINGS | AMOUNT | DEDUCTIONS | AMOUNT |\n"
        f"| :--- | :--- | :--- | :--- |\n"
        f"| Basic Salary | {_fmt_curr(basic)} | PAYE (Income Tax) | {_fmt_curr(paye)} |\n"
        f"| Travel Allowance | {_fmt_curr(allowance)} | UIF (1% statutory) | {_fmt_curr(uif)} |\n"
        f"| | | Pension Fund (7,5%) | {_fmt_curr(pension)} |\n"
        f"| | | Medical Aid Contribution | {_fmt_curr(medical)} |\n"
        f"| **Gross Pay** | **{_fmt_curr(gross)}** | **Total Deductions** | **{_fmt_curr(total_deductions)}** |\n\n"
        f"Calculate the **Net Pay** deposited into {name}'s bank account for this pay period."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Net Pay is determined by subtracting Total Deductions from Gross Pay: "
        f"$$\\text{{Net Pay}} = \\text{{Gross Pay}} - \\text{{Total Deductions}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Net Pay}} = {_fmt_curr(gross)} - {_fmt_curr(total_deductions)}$$ "
        f"✓ [1 Mark: Method – subtracting verified total deductions from gross pay]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net Pay}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency net take-home pay]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract Total Deductions from Gross Pay.",
        tier_2=f"{_fmt_curr(gross)} - {_fmt_curr(total_deductions)} = {correct_ans}.",
        tier_3=f"Net pay = {correct_ans}.",
        r=r,
    )


def _gen_salary_increase_net_impact(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_salary_increase_net_impact"
    name = r.choice(SA_NAMES)
    old_gross = 20000.00
    increase_pct = r.choice([6, 7, 8, 10])
    gross_increase = old_gross * (increase_pct / 100.0)
    # Deductions on increase: 26% marginal tax + 0% UIF (already above ceiling) + 7.5% pension = 33.5%
    marginal_deductions = round(gross_increase * 0.335, 2)
    net_increase = round(gross_increase - marginal_deductions, 2)
    correct_ans = _fmt_curr(net_increase)

    prompt = (
        f"{name} earns a gross monthly salary of {_fmt_curr(old_gross)} and receives a **{increase_pct}% annual salary increase**.\n"
        f"Because of higher PAYE income tax (26%) and pension deductions (7,5%), total additional deductions on this raise "
        f"equal **33,5%** of the increase amount.\n\n"
        f"Calculate the **actual net increase** in take-home pay {name} will receive each month."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First calculate the gross increase: $\\text{{Gross Increase}} = {_fmt_curr(old_gross)} \\times {increase_pct}\\%$.\n"
        f"Then subtract the 33,5% marginal deductions: $\\text{{Net Increase}} = \\text{{Gross Increase}} \\times (1 - 0,335) = \\text{{Gross Increase}} \\times 66,5\\%$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Gross Raise}} = {_fmt_curr(old_gross)} \\times {_fmt(increase_pct / 100)} = {_fmt_curr(gross_increase)}$$\n"
        f"$$\\text{{Net Raise}} = {_fmt_curr(gross_increase)} \\times (1 - 0,335) = {_fmt_curr(gross_increase)} \\times 0,665$$ "
        f"✓ [1 Mark: Method – calculating gross raise and deducting 33,5% marginal deductions]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net Increase}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency net increase]"
    )

    options, _ = _build_options(correct_ans, r)
    d_spec = {
        "diagram_role": "context",
        "kind": "double_bar_graph",
        "title": f"Salary Increase Impact Comparison ({name})",
        "categories": ["Old Gross", "New Gross"],
        "values": [int(old_gross), int(old_gross + gross_increase)],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Gross raise = {_fmt_curr(old_gross)} × {increase_pct}%. Take 66,5% of this raise.",
        tier_2=f"Gross raise = {_fmt_curr(gross_increase)}. Net raise = {_fmt_curr(gross_increase)} × 0,665 = {correct_ans}.",
        tier_3=f"Net increase = {correct_ans}.",
        r=r,
    )


def _gen_bracket_creep_inflation_impact(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_bracket_creep_inflation_impact"
    correct_ans = "A worker's salary increases to match inflation, but pushes them into a higher tax bracket, reducing real purchasing power"

    prompt = (
        f"In personal finance and economics, the phenomenon known as **'bracket creep' (fiscal drag)** refers to which of the following scenarios?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Bracket creep occurs in progressive income tax systems when inflation causes salary increases that push taxpayers into higher marginal tax brackets, "
        f"even though their real purchasing power has not actually grown.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Because tax thresholds are fixed unless adjusted for inflation by the Minister of Finance, "
        f"workers pay a higher effective tax percentage despite having unchanged real standard of living. "
        f"✓ [1 Mark: Method – identifying inflationary fiscal drag definition]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct definition]"
    )

    custom = [
        "A worker's salary increases to match inflation, but pushes them into a higher tax bracket, reducing real purchasing power",
        "An employee illegally evades taxes by moving assets to an offshore bank account",
        "A business charges 20% VAT instead of the statutory 15% rate",
        "A bank increases home loan interest rates due to a higher repo rate",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Bracket creep connects inflation-based raises with progressive tax brackets.",
        tier_2="Moving into a higher tax bracket without real purchasing growth is fiscal drag.",
        tier_3=f"Correct definition: {correct_ans}.",
        r=r,
    )


def _gen_salary_package_restructuring(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_salary_package_restructuring"
    name = r.choice(SA_NAMES)
    car_allowance = 6000.00
    # In South Africa, 80% of a travel/car allowance is subject to monthly PAYE withholding
    taxable_portion = round(car_allowance * 0.80, 2)
    correct_ans = _fmt_curr(taxable_portion)

    prompt = (
        f"{name} receives a fixed monthly car travel allowance of **{_fmt_curr(car_allowance)}** as part of an employment package.\n"
        f"Under SARS fringe benefit regulations, **80% of a travel allowance** must be included in monthly taxable income for PAYE withholding purposes.\n\n"
        f"Calculate the monthly amount of this car allowance that is subject to PAYE tax."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To calculate the taxable portion of a travel allowance, take 80% of the gross allowance: "
        f"$$\\text{{Taxable Allowance}} = {_fmt_curr(car_allowance)} \\times 80\\%$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Taxable Allowance}} = {_fmt_curr(car_allowance)} \\times 0,80$$ "
        f"✓ [1 Mark: Method – applying statutory 80% inclusion rate to travel allowance]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Taxable Allowance}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency calculation]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the car allowance by 80% (0,80).",
        tier_2=f"{_fmt_curr(car_allowance)} × 0,80 = {correct_ans}.",
        tier_3=f"Taxable portion = {correct_ans}.",
        r=r,
    )


def _gen_independent_contractor_vs_employee(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_independent_contractor_vs_employee"
    correct_ans = "Permanent employees have PAYE and UIF deducted monthly by the employer, whereas independent contractors pay provisional tax directly to SARS twice a year"

    prompt = (
        f"Which of the following correctly describes the fundamental difference in tax and payroll statutory obligations "
        f"between a **permanent employee** and a **freelance independent contractor** in South Africa?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Employers are legally obligated to deduct PAYE and UIF from permanent employees each month. "
        f"Independent contractors invoice for services without PAYE/UIF and must register as Provisional Taxpayers to submit returns directly to SARS.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Identify the statutory distinction between employer PAYE deduction versus provisional self-assessment. "
        f"✓ [1 Mark: Method – identifying employment tax status legal distinctions]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct tax classification]"
    )

    custom = [
        "Permanent employees have PAYE and UIF deducted monthly by the employer, whereas independent contractors pay provisional tax directly to SARS twice a year",
        "Independent contractors pay 0% tax because they do not have an employment contract",
        "Permanent employees must register as VAT vendors regardless of how much they earn",
        "Independent contractors cannot claim any legitimate business expenses against their income",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about who pays tax directly: the employer or the freelancer.",
        tier_2="Freelancers pay provisional tax directly to SARS.",
        tier_3=f"Correct answer: {correct_ans}.",
        r=r,
    )


def _gen_tax_avoidance_vs_evasion_legal(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_tax_avoidance_vs_evasion_legal"
    correct_ans = "Tax avoidance is legal financial structuring within tax law (e.g. retirement annuity contributions), whereas tax evasion is illegal fraud (e.g. concealing cash income)"

    prompt = (
        f"In South African law and financial ethics, what is the critical legal distinction between **tax avoidance** and **tax evasion**?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Tax avoidance utilizes legal deductions and tax incentives provided in the Income Tax Act (such as Section 11F pension deductions). "
        f"Tax evasion involves criminal deception, falsifying records, or deliberately concealing income.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Tax avoidance = legal planning; Tax evasion = criminal offence punishable by heavy penalties and imprisonment. "
        f"✓ [1 Mark: Method – distinguishing legal avoidance from criminal evasion]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct legal distinction]"
    )

    custom = [
        "Tax avoidance is legal financial structuring within tax law (e.g. retirement annuity contributions), whereas tax evasion is illegal fraud (e.g. concealing cash income)",
        "Both tax avoidance and tax evasion carry mandatory 15-year prison sentences in South Africa",
        "Tax evasion is legal for companies, but tax avoidance is strictly illegal for individuals",
        "There is no legal difference; both terms describe non-payment of Value Added Tax",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Avoidance uses legal rules to minimize tax. Evasion is illegal fraud.",
        tier_2="Contributing to a pension is legal avoidance. Hiding cash is illegal evasion.",
        tier_3=f"Distinction: {correct_ans}.",
        r=r,
    )


def _gen_tax_return_reconciliation_refund(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_tax_return_reconciliation_refund"
    name = r.choice(SA_NAMES)
    actual_liability = r.randint(34000, 52000)
    overpayment = r.randint(1800, 5500)
    paye_deducted = actual_liability + overpayment  # Employer deducted more than owed
    correct_ans = f"SARS Tax Refund of {_fmt_curr(overpayment)}"

    prompt = (
        f"At the end of the tax year, {name} submits an annual ITR12 tax return to SARS.\n"
        f"The SARS tax assessment (ITA34) reveals:\n"
        f"  • Final verified income tax liability for the year: {_fmt_curr(actual_liability)}\n"
        f"  • Total PAYE already deducted by employer and paid to SARS: {_fmt_curr(paye_deducted)}\n\n"
        f"Determine the **tax assessment outcome** for {name}."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Compare actual tax liability with total PAYE deducted: "
        f"$$\\text{{Difference}} = \\text{{PAYE Paid}} - \\text{{Actual Tax Liability}}$$\n"
        f"If PAYE paid exceeds actual liability, SARS must refund the excess to the taxpayer.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Refund}} = {_fmt_curr(paye_deducted)} - {_fmt_curr(actual_liability)} = {_fmt_curr(overpayment)}$$ "
        f"✓ [1 Mark: Method – comparing tax paid against liability to deduce refund amount]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate refund outcome and amount]"
    )

    d1 = f"{name} owes SARS {_fmt_curr(overpayment)}"
    d2 = f"Zero balance (neither party owes anything)"
    d3 = f"SARS Tax Refund of {_fmt_curr(actual_liability)}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="PAYE deducted was greater than actual liability.",
        tier_2=f"{_fmt_curr(paye_deducted)} - {_fmt_curr(actual_liability)} = {_fmt_curr(overpayment)} refund.",
        tier_3=f"Outcome = {correct_ans}.",
        r=r,
    )


def _gen_budgeting_net_income_living_expenses(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_budgeting_net_income_living_expenses"
    name = r.choice(SA_NAMES)
    net_income = r.randint(18000, 26000)
    rent = r.choice([6500, 7000, 7500, 8000])
    groceries = r.choice([3500, 4000, 4500])
    transport = r.choice([2000, 2500, 3000])
    utilities = r.choice([1200, 1500, 1800])
    insurance = 950.00

    total_expenses = round(rent + groceries + transport + utilities + insurance, 2)
    surplus = round(net_income - total_expenses, 2)
    correct_ans = f"Surplus of {_fmt_curr(surplus)}"

    prompt = (
        f"{name}'s net monthly take-home salary after all statutory deductions is **{_fmt_curr(net_income)}**.\n"
        f"{name}'s planned monthly living expenses are:\n"
        f"  • Rent / Housing: {_fmt_curr(rent)}\n"
        f"  • Groceries & Household: {_fmt_curr(groceries)}\n"
        f"  • Transport & Fuel: {_fmt_curr(transport)}\n"
        f"  • Water & Electricity: {_fmt_curr(utilities)}\n"
        f"  • Funeral & Life Insurance: {_fmt_curr(insurance)}\n\n"
        f"Calculate the **net monthly financial balance** (Surplus or Deficit) remaining for savings."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First calculate total living expenses by summing all expense categories, then subtract from net take-home income: "
        f"$$\\text{{Balance}} = \\text{{Net Income}} - \\text{{Total Living Expenses}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total Expenses}} = {_fmt_curr(rent)} + {_fmt_curr(groceries)} + {_fmt_curr(transport)} + {_fmt_curr(utilities)} + {_fmt_curr(insurance)} = {_fmt_curr(total_expenses)}$$\n"
        f"$$\\text{{Balance}} = {_fmt_curr(net_income)} - {_fmt_curr(total_expenses)} = {_fmt_curr(surplus)}$$ "
        f"✓ [1 Mark: Method – summing expenses and subtracting from net income]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate surplus balance]"
    )

    d1 = f"Deficit of {_fmt_curr(surplus)}"
    d2 = f"Surplus of {_fmt_curr(surplus + 1000)}"
    d3 = f"Deficit of {_fmt_curr(500.00)}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Monthly Living Expenses Budget ({name})",
        "categories": ["Housing", "Groceries", "Transport", "Utilities"],
        "values": [rent, groceries, transport, utilities],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Sum all the living expenses, then subtract from net income.",
        tier_2=f"Total expenses = {_fmt_curr(total_expenses)}. {_fmt_curr(net_income)} - {_fmt_curr(total_expenses)} = {_fmt_curr(surplus)} surplus.",
        tier_3=f"Balance = {correct_ans}.",
        r=r,
    )
