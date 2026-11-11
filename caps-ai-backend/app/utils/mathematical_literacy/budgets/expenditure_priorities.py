"""Cluster 2: Expenditure Classification, Needs vs Wants & Prioritisation (9 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_budg_exp_fixed_var_occ_classification(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Monthly rent of R 4 800 paid to a landlord under a 12-month lease", "Fixed expenditure", ["Fixed expenditure", "Variable expenditure", "Occasional expenditure", "Fixed income"]),
        ("Monthly prepaid electricity purchase that fluctuates with summer/winter usage", "Variable expenditure", ["Fixed expenditure", "Variable expenditure", "Occasional expenditure", "Capital expenditure"]),
        ("Replacing four worn tyres on a vehicle after an annual roadworthy inspection", "Occasional expenditure", ["Fixed expenditure", "Variable expenditure", "Occasional expenditure", "Variable income"]),
        ("A contractual 24-month cellphone subscription debit order of R 499 per month", "Fixed expenditure", ["Fixed expenditure", "Variable expenditure", "Occasional expenditure", "Sundry expense"]),
        ("Weekly grocery shopping at the supermarket, varying with household consumption", "Variable expenditure", ["Fixed expenditure", "Variable expenditure", "Occasional expenditure", "Discretionary luxury"]),
        ("Purchasing a full set of prescribed Grade 10 textbooks and school uniforms in January", "Occasional expenditure", ["Fixed expenditure", "Variable expenditure", "Occasional expenditure", "Fixed income"]),
        ("Monthly vehicle finance repayment instalment of R 2 750", "Fixed expenditure", ["Fixed expenditure", "Variable expenditure", "Occasional expenditure", "Capital reserve"]),
        ("Minibus taxi fares to work that vary based on the number of working days each month", "Variable expenditure", ["Fixed expenditure", "Variable expenditure", "Occasional expenditure", "Investment deposit"])
    ]
    item, correct_cat, opts = r.choice(scenarios)
    prompt = (
        f"In personal financial budgeting, expenses are categorised by their regularity and contractual obligations.\n\n"
        f"Classify the following expenditure item: **{item}**.\n\n"
        f"Select whether this is **Fixed expenditure**, **Variable expenditure**, or **Occasional expenditure**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• **Fixed expenditure**: Contractual, regular expense where the exact amount is predetermined and must be paid every month (e.g. rent, bond repayments, fixed insurance policies).\n"
        f"• **Variable expenditure**: Essential or regular expense whose monetary amount changes from month to month depending on usage, price fluctuations, or consumption (e.g. groceries, electricity, fuel).\n"
        f"• **Occasional expenditure**: Expenses that occur irregularly, seasonally, or once-off (e.g. vehicle repairs, school uniforms, holiday travel).\n\n"
        f"**Step 2: Method Setup & Classification**\n"
        f"• For '{item}', the classification is **{correct_cat}**.\n"
        f"✓ **[1 Mark: Method – applying regularity and contractual obligation criteria]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{correct_cat}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct expenditure category]**"
    )
    return _make_q(
        subskill="budg_exp_fixed_var_occ_classification",
        prompt=prompt,
        answer=correct_cat,
        sol=sol,
        rubric=["1 Mark: Method – expenditure classification criteria", f"1 Mark: Accuracy – {correct_cat}"],
        hints={
            "tier_1": "Determine whether the cost is fixed by contract, varies with usage, or occurs only from time to time.",
            "tier_2": f"Does {item} stay identical every month, vary with consumption, or occur seasonally?",
            "tier_3": f"Correct classification: {correct_cat}."
        },
        options=opts,
        r=r
    )

def _gen_budg_exp_high_vs_low_priority(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Monthly prescription chronic medication and medical aid premium", "High priority (Need)", "Essential for preserving health and well-being", ["High priority (Need)", "Low priority (Want)", "Occasional income", "Variable income"]),
        ("Purchasing premium streaming entertainment subscription services (Netflix & Showmax)", "Low priority (Want)", "Non-essential entertainment that can be paused or canceled during financial hardship", ["High priority (Need)", "Low priority (Want)", "Fixed expenditure", "Capital reserve"]),
        ("Municipal electricity and water service payment to prevent disconnection", "High priority (Need)", "Basic physiological necessity required for daily hygiene, cooking, and survival", ["High priority (Need)", "Low priority (Want)", "Occasional expenditure", "Discretionary spending"]),
        ("Dining out at a sit-down restaurant every Friday evening", "Low priority (Want)", "Discretionary lifestyle choice that can be reduced to eliminate a household budget deficit", ["High priority (Need)", "Low priority (Want)", "Fixed necessity", "Essential expense"]),
        ("Monthly rent for family home accommodation", "High priority (Need)", "Basic need for shelter and safety to avoid eviction", ["High priority (Need)", "Low priority (Want)", "Discretionary want", "Variable income"]),
        ("Buying branded designer sneakers instead of durable standard school shoes", "Low priority (Want)", "A luxury preference rather than a fundamental physiological requirement", ["High priority (Need)", "Low priority (Want)", "Essential need", "Fixed contractual debt"])
    ]
    item, priority_type, reason, opts = r.choice(scenarios)
    prompt = (
        f"Financial wellness requires distinguishing between **Needs (High Priority)** and **Wants (Low Priority / Discretionary)**.\n\n"
        f"Classify the priority level of the following budget line item: **{item}**.\n\n"
        f"Select whether this is **High priority (Need)** or **Low priority (Want)**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• **Needs (High Priority)**: Essential goods and services required for survival, health, shelter, and sustaining employment (e.g. basic nutrition, accommodation, primary healthcare, debt obligations).\n"
        f"• **Wants (Low Priority / Discretionary)**: Items that enhance comfort, prestige, or recreation but are non-essential for survival (e.g. luxury dining, subscriptions, gaming).\n\n"
        f"**Step 2: Method Setup & Evaluation**\n"
        f"• Item evaluated: **{item}**.\n"
        f"• Justification: {reason}.\n"
        f"• Therefore, this is classified as **{priority_type}**.\n"
        f"✓ **[1 Mark: Method – evaluating essential survival vs discretionary lifestyle preference]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{priority_type}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct priority classification]**"
    )
    return _make_q(
        subskill="budg_exp_high_vs_low_priority",
        prompt=prompt,
        answer=priority_type,
        sol=sol,
        rubric=["1 Mark: Method – needs vs wants evaluation", f"1 Mark: Accuracy – {priority_type}"],
        hints={
            "tier_1": "Ask: Is this item strictly necessary for basic survival and health, or is it a lifestyle choice?",
            "tier_2": f"{item} is evaluated based on whether living without it would compromise basic safety, shelter, or health.",
            "tier_3": f"Classification: {priority_type}."
        },
        options=opts,
        r=r
    )

def _gen_budg_exp_percentage_allocation_split(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_exp = round(r.choice([12000.00, 15000.00, 16000.00, 18000.00, 20000.00, 24000.00]), 2)
    categories = [
        ("rent and accommodation", round(r.choice([0.25, 0.30, 0.35]) * total_exp, 2)),
        ("groceries and food", round(r.choice([0.18, 0.20, 0.22, 0.25]) * total_exp, 2)),
        ("transport and commuting", round(r.choice([0.12, 0.15, 0.16]) * total_exp, 2)),
        ("school fees and education", round(r.choice([0.10, 0.12, 0.15]) * total_exp, 2))
    ]
    cat_name, cat_amount = r.choice(categories)
    pct = round((cat_amount / total_exp) * 100, 1)
    ans_str = f"{_fmt(pct)}%"
    prompt = (
        f"{name}'s total monthly expenditure is **{_fmt_curr(total_exp)}**.\n\n"
        f"Out of this total, {name} spends **{_fmt_curr(cat_amount)}** on **{cat_name}**.\n\n"
        f"Calculate the percentage of total monthly expenditure allocated to {cat_name}.\n"
        f"Round your answer to **1 decimal place** if necessary."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• The percentage allocation of an expenditure item to the total budget is calculated as:\n"
        f"  $$\\text{{Percentage}} = \\left( \\frac{{\\text{{Category Amount}}}}{{\\text{{Total Expenditure}}}} \\right) \\times 100\\%$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Percentage}} = \\left( \\frac{{{_fmt_curr(cat_amount).replace('R ', '')}}}{{{_fmt_curr(total_exp).replace('R ', '')}}} \\right) \\times 100\\%$$\n"
        f"$$\\text{{Percentage}} = \\left( \\frac{{{_fmt(cat_amount)}}}{{{_fmt(total_exp)}}} \\right) \\times 100\\% = {pct:.4f}\\% \\approx {_fmt(pct)}\\%$$\n"
        f"✓ **[1 Mark: Method – dividing category cost by total expenditure and multiplying by 100]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct percentage rounded to 1 decimal place]**"
    )
    return _make_q(
        subskill="budg_exp_percentage_allocation_split",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (category / total) × 100", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide the {_fmt_curr(cat_amount)} spent on {cat_name} by the total expenditure {_fmt_curr(total_exp)}.",
            "tier_2": f"({cat_amount} ÷ {total_exp}) × 100 = {pct}%.",
            "tier_3": f"Percentage allocation = {ans_str}."
        },
        r=r
    )

def _gen_budg_exp_variable_expenses_subtotal(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    rent = round(r.choice([4200.00, 4800.00, 5200.00]), 2)  # Fixed
    groceries = round(r.choice([2600.00, 3100.00, 3400.00]), 2)  # Variable
    car_instalment = round(r.choice([2400.00, 2800.00, 3100.00]), 2)  # Fixed
    electricity = round(r.choice([650.00, 750.00, 850.00]), 2)  # Variable
    fuel_petrol = round(r.choice([1100.00, 1350.00, 1500.00]), 2)  # Variable
    life_insurance = round(r.choice([380.00, 420.00, 480.00]), 2)  # Fixed
    vehicle_tyres = round(r.choice([2100.00, 2500.00]), 2)  # Occasional

    var_total = round(groceries + electricity + fuel_petrol, 2)
    ans_str = _fmt_curr(var_total)

    prompt = (
        f"{name} lists the following expenses incurred during the month of May:\n\n"
        f"1. House rental debit order: **{_fmt_curr(rent)}**\n"
        f"2. Groceries & supermarket food: **{_fmt_curr(groceries)}**\n"
        f"3. Vehicle finance installment: **{_fmt_curr(car_instalment)}**\n"
        f"4. Prepaid electricity usage: **{_fmt_curr(electricity)}**\n"
        f"5. Petrol / fuel for commuting: **{_fmt_curr(fuel_petrol)}**\n"
        f"6. Life insurance premium: **{_fmt_curr(life_insurance)}**\n"
        f"7. Once-off replacement of two car tyres: **{_fmt_curr(vehicle_tyres)}**\n\n"
        f"Identify all the **Variable expenses** and calculate their total subtotal for May."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• **Fixed expenses**: House rental ({_fmt_curr(rent)}), vehicle installment ({_fmt_curr(car_instalment)}), and life insurance ({_fmt_curr(life_insurance)}) are regular and contractual.\n"
        f"• **Occasional expenses**: Replacement of tyres ({_fmt_curr(vehicle_tyres)}) occurs once-off/irregularly.\n"
        f"• **Variable expenses**: Groceries ({_fmt_curr(groceries)}), prepaid electricity ({_fmt_curr(electricity)}), and fuel ({_fmt_curr(fuel_petrol)}) fluctuate monthly with consumption.\n\n"
        f"**Step 2: Method Setup & Summation**\n"
        f"$$\\text{{Variable Total}} = \\text{{{_fmt_curr(groceries)}}} + \\text{{{_fmt_curr(electricity)}}} + \\text{{{_fmt_curr(fuel_petrol)}}}\\$$\n"
        f"$$\\text{{Variable Total}} = \\text{{{_fmt_curr(var_total)}}}\\$$\n"
        f"✓ **[1 Mark: Method – isolating exactly the 3 variable items and adding them]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total variable expenditure in Rands]**"
    )
    return _make_q(
        subskill="budg_exp_variable_expenses_subtotal",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – identifying variable items (groceries, electricity, fuel) and adding", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Variable expenses fluctuate based on consumption: groceries, prepaid electricity, and petrol.",
            "tier_2": f"Sum: {_fmt_curr(groceries)} + {_fmt_curr(electricity)} + {_fmt_curr(fuel_petrol)}.",
            "tier_3": f"Total variable expenses = {_fmt_curr(var_total)}."
        },
        r=r
    )

def _gen_budg_exp_fixed_expenses_ratio(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    fixed_exp = round(r.choice([6000.00, 7500.00, 8000.00, 9000.00]), 2)
    variable_exp = round(r.choice([4000.00, 4500.00, 5000.00, 6000.00]), 2)
    total_exp = round(fixed_exp + variable_exp, 2)
    ratio_val = round((fixed_exp / total_exp) * 100, 1)
    ans_str = f"{_fmt(ratio_val)}%"

    prompt = (
        f"{name}'s monthly budget shows total fixed expenses of **{_fmt_curr(fixed_exp)}** and total variable expenses of **{_fmt_curr(variable_exp)}**.\n\n"
        f"1. Calculate the total monthly expenditure.\n"
        f"2. Calculate the ratio of **fixed expenses to total expenditure**, expressed as a percentage rounded to **1 decimal place**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Total expenditure = $\\text{{Fixed expenses}} + \\text{{Variable expenses}}$.\n"
        f"• The fixed expense ratio indicates the proportion of unavoidable committed costs in a household budget:\n"
        f"  $$\\text{{Ratio (\\%)}} = \\left( \\frac{{\\text{{Fixed Expenses}}}}{{\\text{{Total Expenditure}}}} \\right) \\times 100\\%$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Total Expenditure}} = \\text{{{_fmt_curr(fixed_exp)}}} + \\text{{{_fmt_curr(variable_exp)}}} = \\text{{{_fmt_curr(total_exp)}}}$.\n"
        f"• $\\text{{Fixed Ratio}} = \\left( \\frac{{{_fmt(fixed_exp)}}}{{{_fmt(total_exp)}}} \\right) \\times 100\\% = {ratio_val:.4f}\\% \\approx {_fmt(ratio_val)}\\%$.\n"
        f"✓ **[1 Mark: Method – calculating total expenses and dividing fixed expenses by total]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct percentage rounded to 1 decimal place]**"
    )
    return _make_q(
        subskill="budg_exp_fixed_expenses_ratio",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (fixed expenses ÷ total expenses) × 100", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Total expenditure = {_fmt_curr(fixed_exp)} + {_fmt_curr(variable_exp)} = {_fmt_curr(total_exp)}.",
            "tier_2": f"Divide fixed expenses ({_fmt_curr(fixed_exp)}) by total expenditure ({_fmt_curr(total_exp)}) and multiply by 100.",
            "tier_3": f"Fixed expense ratio = {ans_str}."
        },
        r=r
    )

def _gen_budg_exp_cost_cutting_deficit_reduction(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    income = round(r.choice([14500.00, 16000.00, 18200.00]), 2)
    current_exp = round(income + r.choice([1200.00, 1500.00, 1850.00, 2100.00]), 2)
    deficit = round(current_exp - income, 2)
    target_savings = round(r.choice([500.00, 800.00, 1000.00]), 2)
    required_cut = round(deficit + target_savings, 2)
    ans_str = _fmt_curr(required_cut)

    prompt = (
        f"{name}'s monthly net income is **{_fmt_curr(income)}**, but current monthly expenses total **{_fmt_curr(current_exp)}**.\n\n"
        f"This results in a monthly budget deficit.\n\n"
        f"To restore financial stability, {name} aims not only to break even (eliminate the deficit), but also to achieve an active monthly emergency savings surplus of **{_fmt_curr(target_savings)}**.\n\n"
        f"Calculate the **total amount of expenditure that must be reduced (cut)** each month to reach this financial goal."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• When expenditure exceeds income, the budget runs at a **deficit**:\n"
        f"  $$\\text{{Deficit}} = \\text{{Current Expenses}} - \\text{{Net Income}}$$\n"
        f"• To achieve a target savings surplus, {name} must cut enough expenses to cover the entire deficit plus fund the new savings allocation:\n"
        f"  $$\\text{{Total Expenditure Cut}} = \\text{{Deficit}} + \\text{{Target Surplus}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Deficit}} = \\text{{{_fmt_curr(current_exp)}}} - \\text{{{_fmt_curr(income)}}} = \\text{{{_fmt_curr(deficit)}}}$.\n"
        f"• $\\text{{Required Reduction}} = \\text{{{_fmt_curr(deficit)}}} + \\text{{{_fmt_curr(target_savings)}}} = \\text{{{_fmt_curr(required_cut)}}}$.\n"
        f"✓ **[1 Mark: Method – finding deficit and adding required surplus savings]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct expenditure reduction amount in Rands]**"
    )
    return _make_q(
        subskill="budg_exp_cost_cutting_deficit_reduction",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – deficit + target surplus", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Current deficit = {_fmt_curr(current_exp)} - {_fmt_curr(income)} = {_fmt_curr(deficit)}.",
            "tier_2": f"To break even and save {_fmt_curr(target_savings)}, add {_fmt_curr(deficit)} + {_fmt_curr(target_savings)}.",
            "tier_3": f"Total reduction required = {_fmt_curr(required_cut)}."
        },
        r=r
    )

def _gen_budg_exp_food_grocery_weekly_to_monthly(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    weekly_grocery = round(r.choice([750.00, 850.00, 920.00, 1050.00, 1150.00]), 2)
    # CAPS Standard conversion: 52 weeks in a year divided by 12 months = 52/12 = 4.3333 weeks per month
    monthly_grocery = round((weekly_grocery * 52) / 12, 2)
    ans_str = _fmt_curr(monthly_grocery)

    prompt = (
        f"{name} spends an average of **{_fmt_curr(weekly_grocery)} per week** on groceries and household food items.\n\n"
        f"In South African mathematical literacy and personal budgeting, a year contains **52 weeks** and **12 months**.\n\n"
        f"Calculate {name}'s **budgeted monthly food expenditure**, rounded to 2 decimal places."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• A standard calendar year has 52 weeks and 12 months. Therefore, the average number of weeks per month is $\\frac{{52}}{{12}} \\approx 4,3333$.\n"
        f"• The exact monthly equivalent is calculated via the annual expenditure:\n"
        f"  $$\\text{{Monthly Expenditure}} = \\frac{{\\text{{Weekly Cost}} \\times 52}}{{12}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Annual Food Cost}} = \\text{{{_fmt_curr(weekly_grocery)}}} \\times 52 = \\text{{{_fmt_curr(weekly_grocery * 52)}}}$.\n"
        f"• $\\text{{Monthly Food Budget}} = \\frac{{\\text{{{_fmt_curr(weekly_grocery * 52)}}}}}{{12}} = \\text{{{_fmt_curr(monthly_grocery)}}}$.\n"
        f"✓ **[1 Mark: Method – multiplying weekly amount by 52 and dividing by 12]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct monthly food budget in Rands]**"
    )
    return _make_q(
        subskill="budg_exp_food_grocery_weekly_to_monthly",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – weekly × 52 ÷ 12", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Do not just multiply by 4 weeks! Multiply weekly spending by 52 weeks to get annual spending, then divide by 12 months.",
            "tier_2": f"Annual spending = {_fmt_curr(weekly_grocery)} × 52 = {_fmt_curr(weekly_grocery * 52)}. Divide by 12.",
            "tier_3": f"Monthly budget = {_fmt_curr(monthly_grocery)}."
        },
        r=r
    )

def _gen_budg_exp_public_transport_commuter_cost(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    single_taxi_fare = round(r.choice([16.00, 18.00, 20.00, 22.00, 25.00]), 2)
    daily_commute_cost = round(single_taxi_fare * 2, 2)
    work_days_per_month = r.choice([20, 21, 22])
    monthly_taxi_cost = round(daily_commute_cost * work_days_per_month, 2)
    monthly_train_pass = round(r.choice([250.00, 280.00, 320.00]), 2)
    total_transport_cost = round(monthly_taxi_cost + monthly_train_pass, 2)
    ans_str = _fmt_curr(total_transport_cost)

    prompt = (
        f"{name} travels to work using both a minibus taxi and a commuter train:\n\n"
        f"• Minibus taxi fare is **{_fmt_curr(single_taxi_fare)} per single trip** (return trip requires 2 taxi trips per day).\n"
        f"• {name} works **{work_days_per_month} days** during the month.\n"
        f"• In addition, {name} purchases a monthly train commuter card for **{_fmt_curr(monthly_train_pass)}**.\n\n"
        f"Calculate {name}'s **total monthly transport budget**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Daily taxi cost = $\\text{{Single fare}} \\times 2$.\n"
        f"• Monthly taxi expenditure = $\\text{{Daily taxi cost}} \\times \\text{{Working days}}$.\n"
        f"• Total monthly transport = $\\text{{Monthly taxi cost}} + \\text{{Monthly train card}}$.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Daily taxi fare}} = \\text{{{_fmt_curr(single_taxi_fare)}}} \\times 2 = \\text{{{_fmt_curr(daily_commute_cost)}}}$.\n"
        f"• $\\text{{Monthly taxi fare}} = \\text{{{_fmt_curr(daily_commute_cost)}}} \\times {work_days_per_month} = \\text{{{_fmt_curr(monthly_taxi_cost)}}}$.\n"
        f"• $\\text{{Total transport}} = \\text{{{_fmt_curr(monthly_taxi_cost)}}} + \\text{{{_fmt_curr(monthly_train_pass)}}} = \\text{{{_fmt_curr(total_transport_cost)}}}$.\n"
        f"✓ **[1 Mark: Method – calculating return taxi cost for working days and adding monthly train card]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total transport expenditure in Rands]**"
    )
    return _make_q(
        subskill="budg_exp_public_transport_commuter_cost",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (single fare × 2 × days) + train card", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Calculate the return taxi fare per day ({_fmt_curr(single_taxi_fare)} × 2), multiply by {work_days_per_month} working days, then add the train card.",
            "tier_2": f"Taxi total = {_fmt_curr(daily_commute_cost)} × {work_days_per_month} = {_fmt_curr(monthly_taxi_cost)}. Add {_fmt_curr(monthly_train_pass)}.",
            "tier_3": f"Total monthly transport = {_fmt_curr(total_transport_cost)}."
        },
        r=r
    )

def _gen_budg_exp_utility_prepaid_electricity_budget(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    tariff_per_kwh = round(r.choice([2.45, 2.65, 2.80, 3.10]), 2)  # Rands per kWh
    monthly_units_kwh = r.choice([350, 400, 450, 500])
    electricity_cost = round(tariff_per_kwh * monthly_units_kwh, 2)
    prompt = (
        f"{name}'s household uses a prepaid electricity meter. The local municipality charges a flat tariff of **{_fmt_curr(tariff_per_kwh)} per kWh** (kilowatt-hour) inclusive of VAT.\n\n"
        f"During the winter month of July, the family anticipates consuming **{_fmt(monthly_units_kwh)} kWh** of electricity.\n\n"
        f"Calculate the **budgeted amount** {name} must allocate for prepaid electricity in July."
    )
    ans_str = _fmt_curr(electricity_cost)
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• The cost of prepaid utility consumption is calculated as:\n"
        f"  $$\\text{{Total Cost}} = \\text{{Tariff rate per unit}} \\times \\text{{Total units consumed}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Electricity Budget}} = \\text{{{_fmt_curr(tariff_per_kwh)}}} \\times {_fmt(monthly_units_kwh)} = \\text{{{_fmt_curr(electricity_cost)}}}$.\n"
        f"✓ **[1 Mark: Method – multiplying tariff per kWh by estimated kWh units]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct prepaid electricity budget in Rands]**"
    )
    return _make_q(
        subskill="budg_exp_utility_prepaid_electricity_budget",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – tariff rate × consumption units", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Multiply the tariff rate ({_fmt_curr(tariff_per_kwh)}) by the total number of kWh units ({monthly_units_kwh}).",
            "tier_2": f"{tariff_per_kwh} × {monthly_units_kwh} = {electricity_cost}.",
            "tier_3": f"Budgeted electricity cost = {_fmt_curr(electricity_cost)}."
        },
        r=r
    )
