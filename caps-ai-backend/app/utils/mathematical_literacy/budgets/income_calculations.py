"""Cluster 1: Personal Income Streams, Calculations & Classification (10 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_budg_inc_fixed_var_occ_classification(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A permanent employee's basic monthly salary of R 18 500", "Fixed income", ["Fixed income", "Variable income", "Occasional income", "Capital investment"]),
        ("Commission earned on varying monthly sales of electronics", "Variable income", ["Fixed income", "Variable income", "Occasional income", "Fixed expenditure"]),
        ("A cash gift received from grandparents for a 16th birthday", "Occasional income", ["Fixed income", "Variable income", "Occasional income", "State grant"]),
        ("Monthly rental income received from tenant in a garden cottage", "Fixed income", ["Fixed income", "Variable income", "Occasional income", "Casual wage"]),
        ("An annual company performance bonus paid in December", "Occasional income", ["Fixed income", "Variable income", "Occasional income", "Variable expenditure"]),
        ("Weekly wages that fluctuate based on variable shift hours worked", "Variable income", ["Fixed income", "Variable income", "Occasional income", "Sundry allowance"])
    ]
    item, correct_cat, opts = r.choice(scenarios)
    prompt = (
        f"In personal financial literacy, sources of money are classified by their regularity and predictability.\n\n"
        f"Classify the following income stream: **{item}**.\n\n"
        f"Select whether this is **Fixed income**, **Variable income**, or **Occasional income**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• **Fixed income**: Predictable amount that does not change month to month (e.g. permanent basic salary, fixed rental contract).\n"
        f"• **Variable income**: Received regularly, but the numerical amount fluctuates depending on performance or hours (e.g. sales commission, overtime).\n"
        f"• **Occasional income**: Received irregularly or from time to time (e.g. birthday gifts, inheritances, annual bonuses).\n\n"
        f"**Step 2: Method Setup & Classification**\n"
        f"• For '{item}', the classification is **{correct_cat}**.\n"
        f"✓ **[1 Mark: Method – applying regularity and predictability criteria]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{correct_cat}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct income category]**"
    )
    return _make_q(
        subskill="budg_inc_fixed_var_occ_classification",
        prompt=prompt,
        answer=correct_cat,
        sol=sol,
        rubric=["1 Mark: Method – definition matching", f"1 Mark: Accuracy – {correct_cat}"],
        hints={
            "tier_1": "Consider whether the amount is fixed, varies monthly, or only occurs from time to time.",
            "tier_2": f"Does {item} stay the same every month or change?",
            "tier_3": f"Correct classification: {correct_cat}."
        },
        options=opts,
        r=r
    )

def _gen_budg_inc_salary_vs_wage_calculation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    hourly_rate = round(r.choice([38.50, 42.00, 45.00, 48.50, 52.00]), 2)
    hours_per_week = r.choice([40, 45])
    weekly_wage = round(hourly_rate * hours_per_week, 2)
    # Official standard conversion: 52 weeks / 12 months = 4.3333 weeks per month
    monthly_equivalent = round(weekly_wage * 52 / 12, 2)
    prompt = (
        f"{name} works as a welder and earns an hourly wage of **{_fmt_curr(hourly_rate)}** for a standard **{hours_per_week}-hour working week**.\n\n"
        f"1. Calculate {name}'s weekly wage.\n"
        f"2. Using the standard financial convention that there are **52 weeks in a year**, calculate {name}'s equivalent **average monthly wage**."
    )
    ans_str = _fmt_curr(monthly_equivalent)
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Weekly wage = $\\text{{Hourly rate}} \\times \\text{{Hours per week}} = {_fmt_curr(hourly_rate)} \\times {hours_per_week} = {_fmt_curr(weekly_wage)}$.\n"
        f"• To convert weekly wage to monthly, calculate annual wage first, then divide by 12 months:\n"
        f"  $$\\text{{Monthly wage}} = \\frac{{\\text{{Weekly wage}} \\times 52}}{12}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Weekly Wage}} = {_fmt_curr(hourly_rate)} \\times {hours_per_week} = {_fmt_curr(weekly_wage)}$$\n"
        f"$$\\text{{Monthly Equivalent}} = \\frac{{{_fmt_curr(weekly_wage)} \\times 52}}{12} = \\frac{{\\text{{{_fmt_curr(weekly_wage * 52)}}}}}{12} = {_fmt_curr(monthly_equivalent)}$$\n"
        f"✓ **[1 Mark: Method – multiplying hourly rate by weekly hours, then multiplying by 52 and dividing by 12]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct monthly equivalent to 2 decimal places]**"
    )
    return _make_q(
        subskill="budg_inc_salary_vs_wage_calculation",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – weekly × 52 ÷ 12", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Weekly wage = {hours_per_week} hrs × {_fmt_curr(hourly_rate)}.",
            "tier_2": "Monthly wage = (Weekly wage × 52) ÷ 12.",
            "tier_3": f"Monthly equivalent = {_fmt_curr(monthly_equivalent)}."
        },
        r=r
    )

def _gen_budg_inc_hourly_overtime_pay(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    normal_rate = round(r.choice([65.00, 75.00, 80.00, 90.00]), 2)
    normal_hours = 160
    ot_multiplier = 1.5
    ot_hours = r.choice([10, 12, 15, 20])
    normal_pay = round(normal_hours * normal_rate, 2)
    ot_rate = round(normal_rate * ot_multiplier, 2)
    ot_pay = round(ot_hours * ot_rate, 2)
    total_gross = round(normal_pay + ot_pay, 2)
    prompt = (
        f"{name} works in an agricultural machinery workshop. During October, {name} works **{normal_hours} normal hours** at a standard rate of **{_fmt_curr(normal_rate)} per hour**. "
        f"{name} also works **{ot_hours} overtime hours** paid at **time-and-a-half (1,5 times the normal rate)**.\n\n"
        f"1. Calculate the overtime hourly rate.\n"
        f"2. Calculate {name}'s total gross earnings for October."
    )
    ans_str = _fmt_curr(total_gross)
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Overtime rate at time-and-a-half = $\\text{{Normal rate}} \\times 1,5 = {_fmt_curr(normal_rate)} \\times 1,5 = {_fmt_curr(ot_rate)}$.\n"
        f"• Total earnings = $\\text{{Normal pay}} + \\text{{Overtime pay}}$.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Normal Pay}} = {normal_hours}\\text{{ hrs}} \\times \\text{{{_fmt_curr(normal_rate)}}} = \\text{{{_fmt_curr(normal_pay)}}}\\$$\n"
        f"$$\\text{{Overtime Pay}} = {ot_hours}\\text{{ hrs}} \\times \\text{{{_fmt_curr(ot_rate)}}} = \\text{{{_fmt_curr(ot_pay)}}}\\$$\n"
        f"$$\\text{{Total Gross Earnings}} = \\text{{{_fmt_curr(normal_pay)}}} + \\text{{{_fmt_curr(ot_pay)}}} = \\text{{{_fmt_curr(total_gross)}}}\\$$\n"
        f"✓ **[1 Mark: Method – calculating normal pay, overtime rate × hours, and summing]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total gross earnings in Rands]**"
    )
    return _make_q(
        subskill="budg_inc_hourly_overtime_pay",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – normal pay + (OT rate × OT hours)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Overtime rate = {_fmt_curr(normal_rate)} × 1,5 = {_fmt_curr(ot_rate)}/hr.",
            "tier_2": f"Normal pay: {normal_hours} × {_fmt_curr(normal_rate)}. Overtime pay: {ot_hours} × {_fmt_curr(ot_rate)}.",
            "tier_3": f"Total gross: {_fmt_curr(normal_pay)} + {_fmt_curr(ot_pay)} = {_fmt_curr(total_gross)}."
        },
        r=r
    )

def _gen_budg_inc_sales_commission_tiered(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    basic_salary = round(r.choice([6500.00, 7500.00, 8000.00, 9500.00]), 2)
    comm_pct = r.choice([4.0, 5.0, 6.0])
    sales_total = round(r.choice([60000.00, 75000.00, 85000.00, 120000.00]), 2)
    comm_amount = round(sales_total * (comm_pct / 100.0), 2)
    total_income = round(basic_salary + comm_amount, 2)
    prompt = (
        f"{name} works as a sales representative at a farm equipment dealership. "
        f"{name} receives a fixed basic salary of **{_fmt_curr(basic_salary)} per month**, plus **{_fmt(comm_pct)}% commission** on all monthly sales achieved.\n\n"
        f"In November, {name} achieves total sales of **{_fmt_curr(sales_total)}**.\n\n"
        f"Calculate {name}'s total monthly income for November."
    )
    ans_str = _fmt_curr(total_income)
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Commission is a variable incentive based on percentage of sales volume:\n"
        f"  $$\\text{{Commission}} = \\text{{Commission percentage}} \\times \\text{{Sales Volume}}$$\n"
        f"• Total income = $\\text{{Basic salary}} + \\text{{Commission}}$.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Commission}} = {_fmt(comm_pct)}\\% \\times \\text{{{_fmt_curr(sales_total)}}} = \\frac{{{_fmt(comm_pct)}}}{{100}} \\times {_fmt(sales_total)} = \\text{{{_fmt_curr(comm_amount)}}}\\$$\n"
        f"$$\\text{{Total Income}} = \\text{{{_fmt_curr(basic_salary)}}} + \\text{{{_fmt_curr(comm_amount)}}} = \\text{{{_fmt_curr(total_income)}}}\\$$\n"
        f"✓ **[1 Mark: Method – finding commission percentage and adding to basic salary]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total monthly income]**"
    )
    return _make_q(
        subskill="budg_inc_sales_commission_tiered",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – basic + (comm% × sales)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Commission = {_fmt(comm_pct)}% of {_fmt_curr(sales_total)}.",
            "tier_2": f"Commission = {_fmt_curr(comm_amount)}. Add this to basic salary ({_fmt_curr(basic_salary)}).",
            "tier_3": f"Total income = {_fmt_curr(total_income)}."
        },
        r=r
    )

def _gen_budg_inc_restaurant_waiter_tips(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    fri_shifts = 4
    fri_hrs = 5
    fri_rate = 25.00
    sat_shifts = 4
    sat_hrs = 8
    sat_rate = 35.00
    sun_shifts = 2
    sun_hrs = 6
    sun_rate = 45.00
    fri_pay = fri_shifts * fri_hrs * fri_rate
    sat_pay = sat_shifts * sat_hrs * sat_rate
    sun_pay = sun_shifts * sun_hrs * sun_rate
    shift_wages = fri_pay + sat_pay + sun_pay
    tips_multiplier = r.choice([1.2, 1.5, 1.8])
    tips_earned = round(shift_wages * tips_multiplier, 2)
    total_earnings = round(shift_wages + tips_earned, 2)
    prompt = (
        f"{name} is a student working weekend shifts as a restaurant waiter to earn extra income. "
        f"During one month, {name} works the following shifts:\n\n"
        f"• **4 Friday shifts** of 5 hours each @ **R 25,00 per hour**\n"
        f"• **4 Saturday shifts** of 8 hours each @ **R 35,00 per hour**\n"
        f"• **2 Sunday shifts** of 6 hours each @ **R 45,00 per hour**\n"
        f"• Monthly customer gratuities (tips) earned equal **{_fmt(tips_multiplier)} times the shift wages**.\n\n"
        f"Calculate {name}'s total monthly earnings (shift wages plus tips)."
    )
    ans_str = _fmt_curr(total_earnings)
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• First calculate shift wages for each day:\n"
        f"  - Friday: $4 \\times 5\\text{{ hrs}} \\times \\text{{R 25,00}} = \\text{{{_fmt_curr(fri_pay)}}}\\$\n"
        f"  - Saturday: $4 \\times 8\\text{{ hrs}} \\times \\text{{R 35,00}} = \\text{{{_fmt_curr(sat_pay)}}}\\$\n"
        f"  - Sunday: $2 \\times 6\\text{{ hrs}} \\times \\text{{R 45,00}} = \\text{{{_fmt_curr(sun_pay)}}}\\$\n"
        f"  - Total shift wages = $\\text{{{_fmt_curr(fri_pay)}}} + \\text{{{_fmt_curr(sat_pay)}}} + \\text{{{_fmt_curr(sun_pay)}}} = \\text{{{_fmt_curr(shift_wages)}}}\\$\n\n"
        f"**Step 2: Method Setup & Tips Calculation**\n"
        f"$$\\text{{Tips earned}} = {_fmt(tips_multiplier)} \\times \\text{{{_fmt_curr(shift_wages)}}} = \\text{{{_fmt_curr(tips_earned)}}}\\$$\n"
        f"$$\\text{{Total Monthly Income}} = \\text{{{_fmt_curr(shift_wages)}}} + \\text{{{_fmt_curr(tips_earned)}}} = \\text{{{_fmt_curr(total_earnings)}}}\\$$\n"
        f"✓ **[1 Mark: Method – summing shift wages and calculating tips multiplier correctly]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total monthly income in Rands]**"
    )
    return _make_q(
        subskill="budg_inc_restaurant_waiter_tips",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – shift wage subtotal + (multiplier × shift wage)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Calculate shift wages: Friday ({_fmt_curr(fri_pay)}) + Saturday ({_fmt_curr(sat_pay)}) + Sunday ({_fmt_curr(sun_pay)}) = {_fmt_curr(shift_wages)}.",
            "tier_2": f"Calculate tips: {_fmt(tips_multiplier)} × {_fmt_curr(shift_wages)} = {_fmt_curr(tips_earned)}.",
            "tier_3": f"Total earnings = {_fmt_curr(shift_wages)} + {_fmt_curr(tips_earned)} = {_fmt_curr(total_earnings)}."
        },
        r=r
    )

def _gen_budg_inc_piecework_casual_earnings(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    rate_per_unit = round(r.choice([35.00, 45.00, 50.00, 65.00]), 2)
    units_completed = r.randint(45, 90)
    total_earned = round(units_completed * rate_per_unit, 2)
    activity = r.choice([
        "sewing traditional Shweshwe aprons for a local craft market",
        "hand-harvesting crates of fresh Roma tomatoes on an agricultural farm",
        "washing and detailing customer vehicles at a township car wash",
        "packaging cartons of farm-fresh free-range eggs"
    ])
    prompt = (
        f"{name} earns casual piecework income by **{activity}**. "
        f"The agreed piecework payment rate is **{_fmt_curr(rate_per_unit)} per completed unit**.\n\n"
        f"During the month, {name} completes **{units_completed} units**.\n\n"
        f"Calculate {name}'s total piecework earnings for the month."
    )
    ans_str = _fmt_curr(total_earned)
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• In piecework remuneration, earnings are directly proportional to output completed:\n"
        f"  $$\\text{{Total Earnings}} = \\text{{Number of completed units}} \\times \\text{{Rate per unit}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total Earnings}} = {units_completed} \\times \\text{{{_fmt_curr(rate_per_unit)}}} = \\text{{{_fmt_curr(total_earned)}}}\\$$\n"
        f"✓ **[1 Mark: Method – multiplying units produced by piecework unit rate]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct piecework earnings in Rands]**"
    )
    return _make_q(
        subskill="budg_inc_piecework_casual_earnings",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – units × rate per unit", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Multiply the number of completed units by the rate per unit.",
            "tier_2": f"Calculate {units_completed} × {_fmt_curr(rate_per_unit)}.",
            "tier_3": f"Total earnings = {_fmt_curr(total_earned)}."
        },
        r=r
    )

def _gen_budg_inc_rental_income_and_levies(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    gross_rent = round(r.choice([4800.00, 5500.00, 6200.00, 7500.00]), 2)
    body_corp_levy = round(r.choice([850.00, 950.00, 1100.00, 1250.00]), 2)
    rates_tax = round(r.choice([450.00, 520.00, 600.00]), 2)
    net_rent = round(gross_rent - body_corp_levy - rates_tax, 2)
    prompt = (
        f"{name} owns an investment flat and receives a **gross rental income of {_fmt_curr(gross_rent)} per month** from a tenant. "
        f"Each month, {name} must pay **{_fmt_curr(body_corp_levy)}** in sectional title levies and **{_fmt_curr(rates_tax)}** in municipal property rates.\n\n"
        f"Calculate {name}'s **net rental income** for the month."
    )
    ans_str = _fmt_curr(net_rent)
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• **Gross Rental**: Total rent received before property expenses are deducted.\n"
        f"• **Net Rental**: Actual profit remaining after subtracting monthly maintenance levies and municipal rates:\n"
        f"  $$\\text{{Net Rental}} = \\text{{Gross Rent}} - \\text{{Levies}} - \\text{{Municipal Rates}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total Property Expenses}} = \\text{{{_fmt_curr(body_corp_levy)}}} + \\text{{{_fmt_curr(rates_tax)}}} = \\text{{{_fmt_curr(round(body_corp_levy + rates_tax, 2))}}}$$\n"
        f"$$\\text{{Net Rental Income}} = \\text{{{_fmt_curr(gross_rent)}}} - \\text{{{_fmt_curr(round(body_corp_levy + rates_tax, 2))}}} = \\text{{{_fmt_curr(net_rent)}}}$$\n"
        f"✓ **[1 Mark: Method – subtracting levies and municipal rates from gross rental]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct net rental income in Rands]**"
    )
    return _make_q(
        subskill="budg_inc_rental_income_and_levies",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – gross rent minus levies minus rates", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Net rental income = Gross rent - Levies - Municipal rates.",
            "tier_2": f"Subtract {_fmt_curr(body_corp_levy)} and {_fmt_curr(rates_tax)} from {_fmt_curr(gross_rent)}.",
            "tier_3": f"Net rental = {_fmt_curr(net_rent)}."
        },
        r=r
    )

def _gen_budg_inc_state_grants_combination(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    pension_count = r.choice([1, 2])
    pension_grant = 2180.00  # Older Person's Grant
    csg_children = r.choice([2, 3, 4])
    csg_grant = 530.00       # Child Support Grant
    stipend = round(r.choice([1200.00, 1500.00, 1800.00]), 2)
    total_pension = round(pension_count * pension_grant, 2)
    total_csg = round(csg_children * csg_grant, 2)
    total_income = round(total_pension + total_csg + stipend, 2)
    prompt = (
        f"{name}'s multi-generational household relies on South African government social assistance and a part-time community stipend:\n\n"
        f"• **{pension_count} Older Person's Grant(s)** of **{_fmt_curr(pension_grant)}** each per month\n"
        f"• **Child Support Grants for {csg_children} children** at **{_fmt_curr(csg_grant)}** per child per month\n"
        f"• Part-time stipend from community crèche of **{_fmt_curr(stipend)}** per month\n\n"
        f"Calculate the total combined monthly income supporting the household."
    )
    ans_str = _fmt_curr(total_income)
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Calculate the subtotal for each state grant type, then add the part-time stipend:\n"
        f"  - Older Person Grants: ${pension_count} \\times \\text{{{_fmt_curr(pension_grant)}}} = \\text{{{_fmt_curr(total_pension)}}}\\$\n"
        f"  - Child Support Grants: ${csg_children} \\times \\text{{{_fmt_curr(csg_grant)}}} = \\text{{{_fmt_curr(total_csg)}}}\\$\n\n"
        f"**Step 2: Method Setup & Summation**\n"
        f"$$\\text{{Total Income}} = \\text{{{_fmt_curr(total_pension)}}} + \\text{{{_fmt_curr(total_csg)}}} + \\text{{{_fmt_curr(stipend)}}} = \\text{{{_fmt_curr(total_income)}}}\\$$\n"
        f"✓ **[1 Mark: Method – multiplying grant counts by respective grant rates and summing all sources]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct combined household monthly income]**"
    )
    return _make_q(
        subskill="budg_inc_state_grants_combination",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – sum of (pension × count) + (CSG × count) + stipend", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Pensions: {pension_count} × {_fmt_curr(pension_grant)}. CSG: {csg_children} × {_fmt_curr(csg_grant)}.",
            "tier_2": f"Add {_fmt_curr(total_pension)} + {_fmt_curr(total_csg)} + {_fmt_curr(stipend)}.",
            "tier_3": f"Total income = {_fmt_curr(total_income)}."
        },
        r=r
    )

def _gen_budg_inc_annual_bonus_13th_cheque(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    monthly_salary = round(r.choice([14500.00, 16000.00, 18500.00, 21000.00]), 2)
    months_worked = r.choice([5, 7, 8, 9, 10])
    pro_rata_bonus = round(monthly_salary * (months_worked / 12.0), 2)
    december_total = round(monthly_salary + pro_rata_bonus, 2)
    prompt = (
        f"{name} earns a basic salary of **{_fmt_curr(monthly_salary)} per month**. {name} joined the company during the year "
        f"and completed **{months_worked} months of service** before the financial year-end.\n\n"
        f"Company policy grants a 13th-cheque annual bonus equivalent to one month's salary, calculated **pro-rata** based on months worked ($Bonus = \\text{{Monthly Salary}} \\times \\frac{{{months_worked}}}{{12}}$).\n\n"
        f"1. Calculate {name}'s pro-rata annual bonus.\n"
        f"2. Calculate {name}'s total gross income for December (monthly salary + bonus)."
    )
    ans_str = _fmt_curr(december_total)
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• A pro-rata bonus represents a proportional share of an annual bonus based on time served:\n"
        f"  $$\\text{{Pro-rata Bonus}} = \\text{{Monthly Salary}} \\times \\frac{{\\text{{Months worked}}}}{{12}}$$\n"
        f"• December gross income = $\\text{{Monthly salary}} + \\text{{Pro-rata bonus}}$.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Pro-rata Bonus}} = \\text{{{_fmt_curr(monthly_salary)}}} \\times \\frac{{{months_worked}}}{{12}} = \\text{{{_fmt_curr(pro_rata_bonus)}}}$$\n"
        f"$$\\text{{December Gross Total}} = \\text{{{_fmt_curr(monthly_salary)}}} + \\text{{{_fmt_curr(pro_rata_bonus)}}} = \\text{{{_fmt_curr(december_total)}}}$$\n"
        f"✓ **[1 Mark: Method – multiplying monthly salary by (months/12) and adding to monthly salary]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct December gross income in Rands]**"
    )
    return _make_q(
        subskill="budg_inc_annual_bonus_13th_cheque",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – salary + pro-rata bonus (salary × months ÷ 12)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Pro-rata bonus = {_fmt_curr(monthly_salary)} × ({months_worked} ÷ 12) = {_fmt_curr(pro_rata_bonus)}.",
            "tier_2": f"Add the bonus ({_fmt_curr(pro_rata_bonus)}) to the monthly salary ({_fmt_curr(monthly_salary)}).",
            "tier_3": f"December total = {_fmt_curr(december_total)}."
        },
        r=r
    )

def _gen_budg_inc_multiple_income_streams_total(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    salary = round(r.choice([16500.00, 18000.00, 20500.00, 22000.00]), 2)
    weekend_gig = round(r.choice([1200.00, 1500.00, 1800.00, 2200.00]), 2)
    cell_allowance = 450.00
    flatlet_rent = round(r.choice([3200.00, 3600.00, 4000.00]), 2)
    fixed_interest = round(r.choice([85.00, 120.00, 165.00]), 2)
    total_inc = round(salary + weekend_gig + cell_allowance + flatlet_rent + fixed_interest, 2)
    prompt = (
        f"{name} compiles a comprehensive list of all monthly cash inflows for personal budgeting:\n\n"
        f"• Primary employer basic salary: **{_fmt_curr(salary)}**\n"
        f"• Employer cellphone & travel allowance: **{_fmt_curr(cell_allowance)}**\n"
        f"• Weekend small business music sound hire & DJing: **{_fmt_curr(weekend_gig)}**\n"
        f"• Backyard cottage rental income: **{_fmt_curr(flatlet_rent)}**\n"
        f"• Interest from fixed 32-day notice savings deposit: **{_fmt_curr(fixed_interest)}**\n\n"
        f"Calculate {name}'s total combined monthly personal income."
    )
    ans_str = _fmt_curr(total_inc)
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Total personal income is the arithmetic sum of all formal salaries, allowances, secondary enterprise profits, rentals, and investment returns:\n"
        f"  $$\\text{{Total Income}} = \\sum \\text{{All Income Streams}}$$\n\n"
        f"**Step 2: Method Setup & Summation**\n"
        f"$$\\text{{Total Income}} = \\text{{{_fmt_curr(salary)}}} + \\text{{{_fmt_curr(cell_allowance)}}} + \\text{{{_fmt_curr(weekend_gig)}}} + \\text{{{_fmt_curr(flatlet_rent)}}} + \\text{{{_fmt_curr(fixed_interest)}}}$$\n"
        f"$$\\text{{Total Income}} = \\text{{{_fmt_curr(total_inc)}}}$$\n"
        f"✓ **[1 Mark: Method – correctly identifying and summing all 5 distinct income streams]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total monthly income in Rands]**"
    )
    return _make_q(
        subskill="budg_inc_multiple_income_streams_total",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – summing all 5 income sources", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Add all 5 income amounts together.",
            "tier_2": f"{_fmt_curr(salary)} + {_fmt_curr(cell_allowance)} + {_fmt_curr(weekend_gig)} + {_fmt_curr(flatlet_rent)} + {_fmt_curr(fixed_interest)}.",
            "tier_3": f"Total income = {_fmt_curr(total_inc)}."
        },
        r=r
    )
