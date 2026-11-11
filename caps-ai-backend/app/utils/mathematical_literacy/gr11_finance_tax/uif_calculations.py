"""Cluster 1: Unemployment Insurance Fund (UIF) Calculations & Caps (Subskills 1 to 9)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    UIF_CEILING_MONTHLY,
    UIF_MAX_DEDUCTION,
    UIF_RATE_EMPLOYEE,
    UIF_RATE_EMPLOYER,
    UIF_RATE_TOTAL,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def _gen_uif_employee_contribution_below_ceiling(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_uif_employee_contribution_below_ceiling"
    name = r.choice(SA_NAMES)
    salary = r.randint(4500, 11500)
    uif_val = round(salary * UIF_RATE_EMPLOYEE, 2)
    correct_ans = _fmt_curr(uif_val)

    prompt = (
        f"{name} earns a gross monthly salary of {_fmt_curr(salary)}.\n"
        f"In South Africa, the statutory Unemployment Insurance Fund (UIF) deduction for an employee is **1% of gross earnings**.\n\n"
        f"Calculate the monthly UIF amount that must be deducted from {name}'s salary."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Because the gross salary of {_fmt_curr(salary)} is below the statutory ceiling of {_fmt_curr(UIF_CEILING_MONTHLY)}, "
        f"the deduction is calculated directly as 1% of the full gross salary.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{UIF Deduction}} = \\text{{Gross Salary}} \\times 1\\% = {_fmt_curr(salary)} \\times 0,01$$ "
        f"✓ [1 Mark: Method – multiplying gross salary by 1%]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{UIF Deduction}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency formatted to 2 decimals]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the gross salary by 1% (or divide by 100).",
        tier_2=f"{_fmt_curr(salary)} × 0,01 = {correct_ans}.",
        tier_3=f"UIF = {correct_ans}.",
        r=r,
    )


def _gen_uif_employer_contribution_match(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_uif_employer_contribution_match"
    name = r.choice(SA_NAMES)
    salary = r.randint(5000, 12000)
    uif_val = round(salary * UIF_RATE_EMPLOYER, 2)
    correct_ans = _fmt_curr(uif_val)

    prompt = (
        f"{name}'s employer deducts 1% from their gross monthly salary of {_fmt_curr(salary)} for the Unemployment Insurance Fund (UIF).\n"
        f"According to South African labour legislation, the **employer must match this contribution** with an additional 1% paid from company funds.\n\n"
        f"Calculate the amount that the employer must contribute towards {name}'s UIF this month."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The employer must contribute an equal 1% of the employee's gross monthly remuneration.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Employer Contribution}} = {_fmt_curr(salary)} \\times 1\\% = {_fmt_curr(salary)} \\times 0,01$$ "
        f"✓ [1 Mark: Method – calculating employer matching 1%]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Employer Contribution}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency formatted to 2 decimals]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The employer matches the employee's 1% exactly.",
        tier_2=f"Calculate 1% of {_fmt_curr(salary)}.",
        tier_3=f"Employer contribution = {correct_ans}.",
        r=r,
    )


def _gen_uif_total_monthly_fund_contribution(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_uif_total_monthly_fund_contribution"
    name = r.choice(SA_NAMES)
    salary = r.randint(6000, 12200)
    total_uif = round(salary * UIF_RATE_TOTAL, 2)
    correct_ans = _fmt_curr(total_uif)

    prompt = (
        f"{name} is employed at a manufacturing firm with a gross salary of {_fmt_curr(salary)} per month.\n"
        f"For each worker, the Unemployment Insurance Fund receives 1% from the employee and 1% from the employer (total 2%).\n\n"
        f"Calculate the **total combined monthly amount** deposited into the UIF on behalf of {name}."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Total UIF contribution equals Employee contribution (1%) + Employer contribution (1%) = 2% of gross salary.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total UIF}} = {_fmt_curr(salary)} \\times 2\\% = {_fmt_curr(salary)} \\times 0,02$$ "
        f"✓ [1 Mark: Method – multiplying gross salary by 2% (or doubling 1%)]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total UIF}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate total contribution]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate 2% of the gross salary.",
        tier_2=f"{_fmt_curr(salary)} × 0,02 = {correct_ans}.",
        tier_3=f"Total UIF = {correct_ans}.",
        r=r,
    )


def _gen_uif_salary_exceeding_ceiling_deduction(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_uif_salary_exceeding_ceiling_deduction"
    name = r.choice(SA_NAMES)
    salary = r.randint(15000, 45000)
    correct_ans = _fmt_curr(UIF_MAX_DEDUCTION)

    prompt = (
        f"{name} works as a senior software consultant and earns a gross monthly salary of {_fmt_curr(salary)}.\n"
        f"In South Africa, the Unemployment Insurance Fund (UIF) has a statutory remuneration ceiling of **{_fmt_curr(UIF_CEILING_MONTHLY)}** per month.\n"
        f"Any earnings above this ceiling are exempt from UIF deductions.\n\n"
        f"Calculate the monthly UIF amount that will be deducted from {name}'s salary."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Because {name}'s gross salary ({_fmt_curr(salary)}) exceeds the statutory ceiling of {_fmt_curr(UIF_CEILING_MONTHLY)}, "
        f"UIF is calculated strictly on the ceiling amount, not the full salary.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{UIF Deduction}} = \\text{{Ceiling}} \\times 1\\% = {_fmt_curr(UIF_CEILING_MONTHLY)} \\times 0,01$$ "
        f"✓ [1 Mark: Method – capping calculation at ceiling threshold of {_fmt_curr(UIF_CEILING_MONTHLY)}]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{UIF Deduction}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – maximum deduction of {_fmt_curr(UIF_MAX_DEDUCTION)}]"
    )

    d1 = _fmt_curr(salary * 0.01)  # uncapped misconception
    d2 = _fmt_curr(UIF_MAX_DEDUCTION * 2)  # total fund
    d3 = _fmt_curr(UIF_MAX_DEDUCTION * 0.5)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Any salary above {_fmt_curr(UIF_CEILING_MONTHLY)} is capped at the ceiling.",
        tier_2=f"Calculate 1% of {_fmt_curr(UIF_CEILING_MONTHLY)}.",
        tier_3=f"Maximum deduction = {correct_ans}.",
        r=r,
    )


def _gen_uif_employer_cap_above_ceiling(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_uif_employer_cap_above_ceiling"
    name = r.choice(SA_NAMES)
    salary = r.randint(22000, 60000)
    correct_ans = _fmt_curr(UIF_MAX_DEDUCTION)

    prompt = (
        f"An executive director at an logistics firm earns a monthly salary of {_fmt_curr(salary)}.\n"
        f"The statutory monthly UIF ceiling is **{_fmt_curr(UIF_CEILING_MONTHLY)}**.\n\n"
        f"Determine the maximum monthly UIF contribution that the employer must pay on behalf of this executive."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The employer's matching contribution is also legally capped at 1% of the statutory ceiling threshold.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Employer Contribution}} = {_fmt_curr(UIF_CEILING_MONTHLY)} \\times 0,01$$ "
        f"✓ [1 Mark: Method – applying 1% to statutory ceiling threshold]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Employer Contribution}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – capped employer contribution]"
    )

    d1 = _fmt_curr(salary * 0.01)
    d2 = _fmt_curr(UIF_MAX_DEDUCTION * 2)
    d3 = _fmt_curr(UIF_CEILING_MONTHLY)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Both employee and employer contributions are capped at 1% of the ceiling.",
        tier_2=f"1% of {_fmt_curr(UIF_CEILING_MONTHLY)} = {correct_ans}.",
        tier_3=f"Employer contribution = {correct_ans}.",
        r=r,
    )


def _gen_uif_annual_contribution_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_uif_annual_contribution_calculation"
    name = r.choice(SA_NAMES)
    salary = r.randint(6500, 11500)
    monthly_uif = round(salary * 0.01, 2)
    annual_uif = round(monthly_uif * 12, 2)
    correct_ans = _fmt_curr(annual_uif)

    prompt = (
        f"{name} earns a consistent gross salary of {_fmt_curr(salary)} per month throughout the tax year.\n\n"
        f"Calculate the **total annual UIF deductions** taken from {name}'s salary over the 12-month period."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Annual UIF deduction is obtained by calculating the monthly 1% deduction and multiplying by 12 months.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Monthly UIF}} = {_fmt_curr(salary)} \\times 0,01 = {_fmt_curr(monthly_uif)}$$\n"
        f"$$\\text{{Annual UIF}} = {_fmt_curr(monthly_uif)} \\times 12$$ ✓ [1 Mark: Method – multiplying monthly UIF by 12]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Annual UIF}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate annual currency]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the monthly 1% deduction, then multiply by 12.",
        tier_2=f"Monthly = {_fmt_curr(monthly_uif)}. Annual = {_fmt_curr(monthly_uif)} × 12.",
        tier_3=f"Annual UIF = {correct_ans}.",
        r=r,
    )


def _gen_uif_piecewise_graph_interpretation(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_uif_piecewise_graph_interpretation"
    ceiling = r.choice([12478.0, 14872.0, 17712.0])
    max_ded = round(ceiling * 0.01, 2)
    correct_ans = f"UIF deductions are capped at {_fmt_curr(max_ded)} for any salary of {_fmt_curr(ceiling)} or higher"

    prompt = (
        f"Study the graph below representing Monthly Gross Salary (x-axis) versus Monthly UIF Deduction (y-axis).\n"
        f"The line rises steadily from R 0 up to a point at $x = \\text{{{_fmt_curr(ceiling)}}}$, and then becomes completely **flat and horizontal** for all values of $x > \\text{{{_fmt_curr(ceiling)}}}$.\n\n"
        f"What is the mathematical and legal reason for this flat horizontal line?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A horizontal line on a function graph indicates that the dependent variable (UIF deduction) remains constant regardless of increases in the independent variable (Salary).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"South African legislation caps UIF contributions at a salary ceiling of {_fmt_curr(ceiling)}. "
        f"Employees earning above this threshold pay a fixed maximum of {_fmt_curr(max_ded)}. "
        f"✓ [1 Mark: Method – recognizing legislative ceiling threshold]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct explanation of ceiling cap]"
    )

    custom = [
        correct_ans,
        f"Employees earning over {_fmt_curr(ceiling)} are completely exempt from paying any UIF",
        f"The employer stops paying salaries once earnings exceed {_fmt_curr(ceiling)}",
        "The graph is an error and should continue rising diagonally without limit",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    diag_spec = {
        "kind": "cartesian_system",
        "diagram_type": "cartesian_system",
        "title": "Monthly Salary vs. Statutory UIF Deduction",
        "caption": f"UIF Statutory Remuneration Ceiling ({_fmt_curr(ceiling)} Cap)",
        "x_label": "Monthly Gross Salary (R)",
        "y_label": "Monthly UIF Deduction (R)",
        "x_range": [0, 25000],
        "y_range": [0, round(max_ded * 1.5, 1)],
        "lines": [
            {
                "label": "1% UIF Contribution",
                "color": "#2563EB",
                "points": [[0, 0], [ceiling, max_ded], [25000, max_ded]],
            }
        ],
        "points_of_interest": [
            {"x": ceiling, "y": max_ded, "label": f"Cap ({_fmt_curr(ceiling)}; {_fmt_curr(max_ded)})"}
        ],
    }

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about why deductions would stop increasing above a certain salary.",
        tier_2=f"The ceiling cap ensures high earners pay no more than {_fmt_curr(max_ded)}.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
        diagram_spec=diag_spec,
    )


def _gen_uif_hourly_wage_weekly_deduction(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_uif_hourly_wage_weekly_deduction"
    name = r.choice(SA_NAMES)
    hours = r.choice([38, 40, 42, 45])
    rate = r.choice([45.0, 50.0, 55.0, 60.0])
    gross_weekly = round(hours * rate, 2)
    uif_weekly = round(gross_weekly * 0.01, 2)
    correct_ans = _fmt_curr(uif_weekly)

    prompt = (
        f"{name} is a wage worker paid an hourly rate of {_fmt_curr(rate)}.\n"
        f"In one week, {name} worked for **{hours} hours**.\n\n"
        f"Calculate the UIF contribution (1%) that must be deducted from {name}'s weekly wage packet."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First calculate gross weekly earnings by multiplying hours worked by the hourly wage rate, then take 1%.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Gross Weekly Wage}} = {hours}\\text{{ hours}} \\times {_fmt_curr(rate)} = {_fmt_curr(gross_weekly)}$$\n"
        f"$$\\text{{Weekly UIF}} = {_fmt_curr(gross_weekly)} \\times 0,01$$ ✓ [1 Mark: Method – calculating gross wage and applying 1%]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Weekly UIF}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency deduction]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Multiply {hours} hours by {_fmt_curr(rate)} to get gross wage, then take 1%.",
        tier_2=f"Gross = {_fmt_curr(gross_weekly)}. UIF = {_fmt_curr(gross_weekly)} × 0,01.",
        tier_3=f"Weekly UIF = {correct_ans}.",
        r=r,
    )


def _gen_uif_qualifying_conditions_claims(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_uif_qualifying_conditions_claims"
    correct_ans = "Dismissal due to retrenchment or operational company closure"

    prompt = (
        f"Under South African labour law, an employee who contributed to the Unemployment Insurance Fund (UIF) "
        f"is entitled to claim benefits from the fund in which of the following scenarios?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The UIF exists to protect workers against involuntary loss of income (retrenchment, illness, maternity, adoption).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"A worker who voluntarily resigns without valid legal reason or is dismissed for gross misconduct is generally disqualified from claiming. "
        f"Retrenchment or business closure is a valid involuntary claim reason. ✓ [1 Mark: Method – distinguishing qualifying involuntary termination]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct qualifying event]"
    )

    custom = [
        "Dismissal due to retrenchment or operational company closure",
        "Voluntary resignation to take an extended holiday",
        "Quitting a job because of disliking the office decor",
        "Suspension without pay due to criminal conviction at the workplace",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="UIF covers involuntary unemployment.",
        tier_2="Voluntary resignation is not covered by UIF.",
        tier_3=f"Qualifying event: {correct_ans}.",
        r=r,
    )

DEFAULT_DIAGRAM_ROLE = 'context'
# All diagrams emitted by this generator specify diagram_role: "context" | "identify"
