"""Grade 9 Mathematics - Whole Numbers Archetypes 26 to 50.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 1/01. Whole numbers.md.
Covers:
  - Rates: speed, best-buy unit price comparisons.
  - Financial Mathematics (Grade 9 core):
    * Simple Interest: I = P * r * t / 100, Total A = P(1 + in).
    * Compound Interest: A = P(1 + i)^n.
    * Comparative growth: Simple vs Compound interest.
    * Hire Purchase: Deposit, loan balance, simple interest on balance, monthly installments.
    * Inflation: Compound price growth over time.
    * Percentages: Markup, profit/loss, selling price, discounts, VAT (15% SA).
    * Exchange Rates: ZAR to/from USD, GBP, EUR.
    * Error Analysis & Multi-step Financial Investment Problems.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from .whole_numbers_svg import draw_interest_comparison_bar_chart_svg


def _fmt_dec(val: float, decimals: int = 2) -> str:
    s = f"{val:.{decimals}f}"
    return s.replace(".", "{,}")


# ----------------------------------------------------------------------
# 26. Average Speed: Distance, Time, Rate Calculation
# ----------------------------------------------------------------------
def arch_26_average_speed_distance_time_rate_calculation(rng: random.Random) -> Dict[str, Any]:
    speed = rng.choice([75, 80, 90, 105, 120])
    hours = rng.choice([2.5, 3.5, 4.0, 4.5])
    distance = speed * hours

    prompt = (
        f"A cross-country bus covers a distance of **{distance:g} km** in **{hours:g} hours**.\n\n"
        f"Calculate the average speed of the bus in **km/h**."
    )
    sol = (
        f"**Average Speed Calculation:**\n"
        f"\\[ \\text{{Speed}} = \\frac{{\\text{{Distance}}}}{{\\text{{Time}}}} = \\frac{{{distance:g} \\text{{ km}}}}{{{hours:g} \\text{{ hours}}}} = {speed} \\text{{ km/h}} \\]"
    )
    ans = f"{speed} km/h"
    return {
        "id": f"g9_fin_speed_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "26_average_speed_distance_time_rate_calculation",
        "learning_objective_id": "math_g9_fin_speed",
        "hints": {
            "tier_1": "Formula: Average Speed = Distance / Time.",
            "tier_2": f"Divide {distance:g} by {hours:g}.",
            "tier_3": ans,
        },
        "misconception_tags": ["multiplying_distance_by_time_instead_of_dividing"],
    }


# ----------------------------------------------------------------------
# 27. Unit Rate: Best Buy Comparison (Per Gram or Litre)
# ----------------------------------------------------------------------
def arch_27_unit_rate_best_buy_comparison_per_gram_or_litre(rng: random.Random) -> Dict[str, Any]:
    # Option A: 500g for R 35.00 -> 0.070/g
    # Option B: 800g for R 52.00 -> 0.065/g
    a_g = 500
    a_price = rng.choice([32.50, 35.00, 37.50])
    b_g = 800
    b_price = rng.choice([48.00, 52.00, 54.40])

    rate_a = a_price / a_g
    rate_b = b_price / b_g

    best = "Brand B" if rate_b < rate_a else "Brand A"

    prompt = (
        f"A supermarket sells cereal in two sizes:\n"
        f"- **Brand A:** {a_g} g box for **R {a_price:.2f}**\n"
        f"- **Brand B:** {b_g} g box for **R {b_price:.2f}**\n\n"
        f"1. Calculate the unit price per gram for both options.\n"
        f"2. Which option represents the better value for money?"
    )
    sol = (
        f"**Unit Rate Comparison:**\n"
        f"1. Brand A unit price: \\(\\frac{{\\text{{R }}{a_price:.2f}}}{{{a_g} \\text{{ g}}}} = \\text{{R }}{_fmt_dec(rate_a, 4)} / \\text{{g}}\\).\n"
        f"2. Brand B unit price: \\(\\frac{{\\text{{R }}{b_price:.2f}}}{{{b_g} \\text{{ g}}}} = \\text{{R }}{_fmt_dec(rate_b, 4)} / \\text{{g}}\\).\n"
        f"3. Conclusion: **{best}** is the better buy because it has a lower cost per gram."
    )
    ans = f"Brand A: R {_fmt_dec(rate_a, 4)}/g, Brand B: R {_fmt_dec(rate_b, 4)}/g, Better buy: {best}"
    return {
        "id": f"g9_fin_best_buy_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "27_unit_rate_best_buy_comparison_per_gram_or_litre",
        "learning_objective_id": "math_g9_fin_best_buy",
        "hints": {
            "tier_1": "Divide total price by total mass to get cost per 1 gram.",
            "tier_2": "The smaller cost per gram is the better value.",
            "tier_3": ans,
        },
        "misconception_tags": ["dividing_grams_by_rands_giving_grams_per_rand_without_realising"],
    }


# ----------------------------------------------------------------------
# 28. Simple Interest: Calculate Interest Amount
# ----------------------------------------------------------------------
def arch_28_simple_interest_calculate_interest_amount(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([5000, 8000, 12000, 15000, 20000])
    r = rng.choice([7.5, 8.0, 9.0, 10.5, 12.0])
    t = rng.choice([2, 3, 4, 5])
    interest = (p * r * t) / 100

    prompt = (
        f"A learner invests **R {p}** at a **simple interest rate of {r:g}% per annum** for **{t} years**.\n\n"
        f"Calculate the total **simple interest ($I$)** earned over the {t} years."
    )
    sol = (
        f"**Simple Interest Formula:**\n"
        f"\\[ I = \\frac{{P \\times r \\times t}}{{100}} \\]\n"
        f"\\[ I = \\frac{{{p} \\times {r:g} \\times {t}}}{{100}} = \\text{{R }}{_fmt_dec(interest, 2)} \\]"
    )
    ans = f"R {_fmt_dec(interest, 2)}"
    return {
        "id": f"g9_si_interest_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "28_simple_interest_calculate_interest_amount",
        "learning_objective_id": "math_g9_si_interest",
        "hints": {
            "tier_1": "Use the formula I = (P * r * t) / 100.",
            "tier_2": f"P = {p}, r = {r:g}, t = {t}.",
            "tier_3": ans,
        },
        "misconception_tags": ["forgetting_to_divide_rate_by_100"],
    }


# ----------------------------------------------------------------------
# 29. Simple Interest: Calculate Total Repayment Amount
# ----------------------------------------------------------------------
def arch_29_simple_interest_calculate_total_repayment_amount(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([6000, 9000, 14000, 18000])
    r = rng.choice([8.5, 9.5, 11.0, 12.5])
    t = rng.choice([3, 4, 5])
    i = (p * r * t) / 100
    a = p + i

    prompt = (
        f"Naledi borrows **R {p}** from a financial institution that charges **simple interest at {r:g}% p.a.**\n"
        f"The loan is taken over a period of **{t} years**.\n\n"
        f"Calculate the **total accumulated amount ($A$)** Naledi must repay at the end of the loan period."
    )
    sol = (
        f"**Accumulated Amount Formula ($A = P(1 + in)$):**\n"
        f"1. Interest earned: \\(I = \\frac{{{p} \\times {r:g} \\times {t}}}{{100}} = \\text{{R }}{_fmt_dec(i, 2)}\\).\n"
        f"2. Total amount: \\(A = P + I = {p} + {_fmt_dec(i, 2)} = \\text{{R }}{_fmt_dec(a, 2)}\\)."
    )
    ans = f"R {_fmt_dec(a, 2)}"
    return {
        "id": f"g9_si_total_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "29_simple_interest_calculate_total_repayment_amount",
        "learning_objective_id": "math_g9_si_total",
        "hints": {
            "tier_1": "Total accumulated amount = Principal + Interest.",
            "tier_2": f"Calculate I = (P * r * t)/100, then add P = {p}.",
            "tier_3": ans,
        },
        "misconception_tags": ["giving_only_interest_instead_of_total_amount_a"],
    }


# ----------------------------------------------------------------------
# 30. Simple Interest: Calculate Principal, Rate, or Time
# ----------------------------------------------------------------------
def arch_30_simple_interest_calculate_principal_or_rate_or_time(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([4000, 5000, 8000, 10000])
    r = rng.choice([6.0, 8.0, 10.0, 12.0])
    t = rng.choice([2, 3, 4, 5])
    interest = int((p * r * t) / 100)

    prompt = (
        f"An investment earns **R {interest}** in simple interest over **{t} years** at a rate of **{r:g}% per annum**.\n\n"
        f"Calculate the **original principal amount ($P$)** that was invested."
    )
    sol = (
        f"**Rearranging Simple Interest Formula:**\n"
        f"\\[ I = \\frac{{P \\times r \\times t}}{{100}} \\implies P = \\frac{{100 \\times I}}{{r \\times t}} \\]\n"
        f"\\[ P = \\frac{{100 \\times {interest}}}{{{r:g} \\times {t}}} = \\text{{R }}{p} \\]"
    )
    ans = f"R {p}"
    return {
        "id": f"g9_si_find_p_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "30_simple_interest_calculate_principal_or_rate_or_time",
        "learning_objective_id": "math_g9_si_find_p",
        "hints": {
            "tier_1": "Rearrange I = (P * r * t)/100 to make P the subject.",
            "tier_2": f"P = (100 * {interest}) / ({r:g} * {t}).",
            "tier_3": ans,
        },
        "misconception_tags": ["inverting_formula_rearrangement"],
    }


# ----------------------------------------------------------------------
# 31. Compound Interest: Annual Compounding Total Amount
# ----------------------------------------------------------------------
def arch_31_compound_interest_annual_compounding_total_amount(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([5000, 8000, 10000, 15000, 20000])
    r = rng.choice([6.0, 7.5, 8.0, 9.0, 10.0])
    n = rng.choice([2, 3])
    i = r / 100.0
    a = p * ((1.0 + i) ** n)

    prompt = (
        f"Calculate the **total accumulated amount ($A$)** if **R {p}** is invested for **{n} years** "
        f"at **{r:g}% per annum compound interest**, compounded annually.\n\n"
        f"Use the compound interest formula $A = P(1 + i)^n$ and round to two decimal places."
    )
    sol = (
        f"**Compound Interest Formula:**\n"
        f"\\[ A = P(1 + i)^n \\]\n"
        f"Where $P = {p}$, $i = \\frac{{{r:g}}}{{100}} = {i}$, and $n = {n}$:\n"
        f"\\[ A = {p}(1 + {i})^{{{n}}} = {p}({1 + i:.4f})^{{{n}}} = \\text{{R }}{_fmt_dec(a, 2)} \\]"
    )
    ans = f"R {_fmt_dec(a, 2)}"
    return {
        "id": f"g9_ci_total_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "31_compound_interest_annual_compounding_total_amount",
        "learning_objective_id": "math_g9_ci_total",
        "hints": {
            "tier_1": "Formula: A = P(1 + i)^n.",
            "tier_2": f"Calculate (1 + {i})^{n}, then multiply by {p}.",
            "tier_3": ans,
        },
        "misconception_tags": ["using_simple_interest_formula_instead_of_compound_interest"],
    }


# ----------------------------------------------------------------------
# 32. Compound Interest: Calculate Interest Earned
# ----------------------------------------------------------------------
def arch_32_compound_interest_calculate_interest_earned(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([6000, 12000, 16000, 25000])
    r = rng.choice([7.0, 8.5, 9.5, 11.0])
    n = rng.choice([2, 3])
    i = r / 100.0
    a = p * ((1.0 + i) ** n)
    ci_earned = a - p

    prompt = (
        f"An investor deposits **R {p}** into a fixed growth account yielding **{r:g}% per annum compound interest**.\n"
        f"After **{n} years**, calculate the **compound interest earned** (growth only, excluding the principal)."
    )
    sol = (
        f"**Compound Interest Earned Calculation:**\n"
        f"1. Total accumulated amount: \\(A = P(1 + i)^n = {p}(1 + {i})^{{{n}}} = \\text{{R }}{_fmt_dec(a, 2)}\\).\n"
        f"2. Interest earned: \\(I = A - P = {_fmt_dec(a, 2)} - {p} = \\text{{R }}{_fmt_dec(ci_earned, 2)}\\)."
    )
    ans = f"R {_fmt_dec(ci_earned, 2)}"
    return {
        "id": f"g9_ci_earned_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "32_compound_interest_calculate_interest_earned",
        "learning_objective_id": "math_g9_ci_earned",
        "hints": {
            "tier_1": "Calculate the final amount A using A = P(1 + i)^n.",
            "tier_2": f"Subtract the starting principal ({p}) from A.",
            "tier_3": ans,
        },
        "misconception_tags": ["forgetting_to_subtract_principal_when_asked_for_interest_earned"],
    }


# ----------------------------------------------------------------------
# 33. Compare Simple Interest vs Compound Interest Growth
# ----------------------------------------------------------------------
def arch_33_compare_simple_interest_vs_compound_interest_growth(rng: random.Random) -> Dict[str, Any]:
    p = 10000
    r = rng.choice([8.0, 10.0, 12.0])
    n = 3
    i = r / 100.0

    si_amount = p * (1 + i * n)
    ci_amount = p * ((1 + i) ** n)
    diff = ci_amount - si_amount

    svg = draw_interest_comparison_bar_chart_svg(
        principal=float(p),
        rate_pct=r,
        years=n,
        si_amount=si_amount,
        ci_amount=ci_amount,
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"An amount of **R {p}** is invested for **{n} years** at **{r:g}% per annum**.\n\n"
        f"1. Calculate the final amount using **Simple Interest** ($A_{{SI}} = P(1 + in)$).\n"
        f"2. Calculate the final amount using **Compound Interest** ($A_{{CI}} = P(1 + i)^n$).\n"
        f"3. Calculate the difference between the two returns, and state which investment method yields more money."
    )
    sol = (
        f"**Comparative Analysis ({n} Years @ {r:g}%):**\n"
        f"1. Simple Interest: \\(A_{{SI}} = {p}(1 + {i} \\times {n}) = \\text{{R }}{_fmt_dec(si_amount, 2)}\\).\n"
        f"2. Compound Interest: \\(A_{{CI}} = {p}(1 + {i})^{{{n}}} = \\text{{R }}{_fmt_dec(ci_amount, 2)}\\).\n"
        f"3. Difference: \\({_fmt_dec(ci_amount, 2)} - {_fmt_dec(si_amount, 2)} = \\text{{R }}{_fmt_dec(diff, 2)}\\).\n"
        f"Compound interest yields more money because interest is earned on previously accumulated interest."
    )
    ans = f"SI: R {_fmt_dec(si_amount, 2)}, CI: R {_fmt_dec(ci_amount, 2)}, Difference: R {_fmt_dec(diff, 2)}"
    return {
        "id": f"g9_si_vs_ci_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "33_compare_simple_interest_vs_compound_interest_growth",
        "learning_objective_id": "math_g9_si_vs_ci",
        "hints": {
            "tier_1": "Calculate SI with P(1 + in) and CI with P(1 + i)^n.",
            "tier_2": "Subtract the two final amounts to find the difference.",
            "tier_3": ans,
        },
        "misconception_tags": ["assuming_simple_and_compound_interest_yield_the_same_amount"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 34. Hire Purchase: Calculate Deposit Percentage
# ----------------------------------------------------------------------
def arch_34_hire_purchase_calculate_deposit_percentage(rng: random.Random) -> Dict[str, Any]:
    cash_price = rng.choice([4500, 6000, 8500, 12000, 15000])
    dep_pct = rng.choice([10, 15, 20])
    deposit = (cash_price * dep_pct) / 100
    balance = cash_price - deposit

    prompt = (
        f"A television set has a cash price of **R {cash_price}**.\n"
        f"To buy it on hire purchase, the store requires a **{dep_pct}% deposit** upfront.\n\n"
        f"1. Calculate the deposit amount in Rands.\n"
        f"2. Calculate the remaining balance to be financed."
    )
    sol = (
        f"**Deposit and Balance:**\n"
        f"1. Deposit: \\(\\frac{{{dep_pct}}}{{100}} \\times \\text{{R }}{cash_price} = \\text{{R }}{_fmt_dec(deposit, 2)}\\).\n"
        f"2. Balance remaining: \\(\\text{{R }}{cash_price} - \\text{{R }}{_fmt_dec(deposit, 2)} = \\text{{R }}{_fmt_dec(balance, 2)}\\)."
    )
    ans = f"Deposit: R {_fmt_dec(deposit, 2)}, Balance: R {_fmt_dec(balance, 2)}"
    return {
        "id": f"g9_hp_deposit_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "34_hire_purchase_calculate_deposit_percentage",
        "learning_objective_id": "math_g9_hp_deposit",
        "hints": {
            "tier_1": f"Deposit = {dep_pct}% of R {cash_price}.",
            "tier_2": "Subtract the deposit from cash price to find the balance.",
            "tier_3": ans,
        },
        "misconception_tags": ["adding_deposit_to_cash_price_instead_of_subtracting"],
    }


# ----------------------------------------------------------------------
# 35. Hire Purchase: Calculate Monthly Installment Amount
# ----------------------------------------------------------------------
def arch_35_hire_purchase_calculate_monthly_installment_amount(rng: random.Random) -> Dict[str, Any]:
    cash_price = rng.choice([8000, 10000, 12000, 14000])
    dep_pct = 10
    deposit = cash_price * 0.10
    balance = cash_price - deposit

    rate = rng.choice([12.0, 15.0, 18.0])
    years = rng.choice([2, 3])
    months = years * 12

    interest = (balance * rate * years) / 100.0
    total_repaid = balance + interest
    monthly_installment = total_repaid / months

    prompt = (
        f"Mr Khumalo purchases a refrigerator on **Hire Purchase**:\n"
        f"- Cash price: **R {cash_price}**\n"
        f"- Deposit: **10%**\n"
        f"- Simple interest on balance: **{rate:g}% p.a.**\n"
        f"- Repayment period: **{years} years** ({months} monthly payments)\n\n"
        f"Calculate his **monthly installment amount**."
    )
    sol = (
        f"**Hire Purchase Steps:**\n"
        f"1. Deposit (10%): \\(0{{,}}\\!10 \\times {cash_price} = \\text{{R }}{_fmt_dec(deposit, 2)}\\).\n"
        f"2. Balance to finance: \\({cash_price} - {_fmt_dec(deposit, 2)} = \\text{{R }}{_fmt_dec(balance, 2)}\\).\n"
        f"3. Simple interest on balance: \\(I = \\frac{{{balance} \\times {rate:g} \\times {years}}}{{100}} = \\text{{R }}{_fmt_dec(interest, 2)}\\).\n"
        f"4. Total amount to pay on loan: \\({balance} + {_fmt_dec(interest, 2)} = \\text{{R }}{_fmt_dec(total_repaid, 2)}\\).\n"
        f"5. Monthly installment: \\(\\frac{{\\text{{R }}{_fmt_dec(total_repaid, 2)}}}{{{months}}} = \\text{{R }}{_fmt_dec(monthly_installment, 2)}\\)."
    )
    ans = f"R {_fmt_dec(monthly_installment, 2)}"
    return {
        "id": f"g9_hp_installment_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "35_hire_purchase_calculate_monthly_installment_amount",
        "learning_objective_id": "math_g9_hp_installment",
        "hints": {
            "tier_1": "1. Subtract deposit to find balance. 2. Calculate simple interest on balance.",
            "tier_2": f"3. Add interest to balance. 4. Divide by {months} months.",
            "tier_3": ans,
        },
        "misconception_tags": ["calculating_hire_purchase_interest_on_the_full_cash_price_instead_of_balance"],
    }


# ----------------------------------------------------------------------
# 36. Hire Purchase: Total Cost and Finance Charges
# ----------------------------------------------------------------------
def arch_36_hire_purchase_total_cost_and_finance_charges(rng: random.Random) -> Dict[str, Any]:
    cash_price = rng.choice([6000, 9000, 12000])
    dep = cash_price * 0.15
    balance = cash_price - dep
    r = 14.0
    t = 2
    i = (balance * r * t) / 100.0
    total_loan_repaid = balance + i
    total_hp_cost = dep + total_loan_repaid
    finance_cost = total_hp_cost - cash_price  # equals i

    prompt = (
        f"A sound system has a cash price of **R {cash_price}**.\n"
        f"Under hire purchase, a **15% deposit** is paid, and simple interest of **{r:g}% p.a.** is charged "
        f"on the remaining balance over **{t} years**.\n\n"
        f"1. Calculate the **total cost** of the sound system on hire purchase (including deposit).\n"
        f"2. Calculate the **extra finance cost** paid above the cash price."
    )
    sol = (
        f"**Total Hire Purchase Cost:**\n"
        f"1. Deposit: \\(0{{,}}\\!15 \\times {cash_price} = \\text{{R }}{_fmt_dec(dep, 2)}\\).\n"
        f"2. Balance: \\({cash_price} - {_fmt_dec(dep, 2)} = \\text{{R }}{_fmt_dec(balance, 2)}\\).\n"
        f"3. Interest: \\(I = \\frac{{{balance} \\times {r:g} \\times {t}}}{{100}} = \\text{{R }}{_fmt_dec(i, 2)}\\).\n"
        f"4. Total HP cost = Deposit + Balance + Interest = \\({_fmt_dec(dep, 2)} + {_fmt_dec(balance, 2)} + {_fmt_dec(i, 2)} = \\text{{R }}{_fmt_dec(total_hp_cost, 2)}\\).\n"
        f"5. Extra finance cost = Total HP Cost - Cash Price = \\({_fmt_dec(total_hp_cost, 2)} - {cash_price} = \\text{{R }}{_fmt_dec(finance_cost, 2)}\\)."
    )
    ans = f"1. R {_fmt_dec(total_hp_cost, 2)}; 2. R {_fmt_dec(finance_cost, 2)}"
    return {
        "id": f"g9_hp_finance_cost_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "36_hire_purchase_total_cost_and_finance_charges",
        "learning_objective_id": "math_g9_hp_finance_cost",
        "hints": {
            "tier_1": "Total HP Cost = Deposit + All installments.",
            "tier_2": "Extra finance charges = Total HP Cost - Cash Price.",
            "tier_3": ans,
        },
        "misconception_tags": ["forgetting_to_add_the_deposit_when_finding_total_hire_purchase_cost"],
    }


# ----------------------------------------------------------------------
# 37. Difference Between Cash Price and Hire Purchase
# ----------------------------------------------------------------------
def arch_37_hire_purchase_difference_between_cash_price_and_hire_purchase(rng: random.Random) -> Dict[str, Any]:
    cash = 15000
    dep = 1500  # 10%
    installment = rng.choice([550, 580, 620])
    months = 36
    total_inst = installment * months
    total_hp = dep + total_inst
    diff = total_hp - cash

    prompt = (
        f"A lounge suite has a cash price of **R {cash}**.\n"
        f"On hire purchase, the customer pays a deposit of **R {dep}**, followed by **36 monthly installments of R {installment}**.\n\n"
        f"How much **more** does the customer pay by purchasing the suite on hire purchase instead of paying cash?"
    )
    sol = (
        f"**Cost Difference:**\n"
        f"1. Total monthly installments: \\(36 \\times \\text{{R }}{installment} = \\text{{R }}{total_inst}\\).\n"
        f"2. Total HP cost: \\(\\text{{R }}{dep} + \\text{{R }}{total_inst} = \\text{{R }}{total_hp}\\).\n"
        f"3. Additional cost: \\(\\text{{R }}{total_hp} - \\text{{R }}{cash} = \\text{{R }}{diff}\\)."
    )
    ans = f"R {diff}"
    return {
        "id": f"g9_hp_diff_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "37_hire_purchase_difference_between_cash_price_and_hire_purchase",
        "learning_objective_id": "math_g9_hp_diff",
        "hints": {
            "tier_1": "Calculate total HP = deposit + (36 * installment).",
            "tier_2": f"Subtract cash price (R {cash}) from total HP.",
            "tier_3": ans,
        },
        "misconception_tags": ["subtracting_deposit_from_total_installments_instead_of_adding"],
    }


# ----------------------------------------------------------------------
# 38. Inflation Rate: Calculate Future Price of Goods
# ----------------------------------------------------------------------
def arch_38_inflation_rate_calculate_future_price_of_goods(rng: random.Random) -> Dict[str, Any]:
    curr_price = rng.choice([25.00, 40.00, 85.00, 120.00])
    inf_rate = rng.choice([5.0, 6.0, 6.5, 7.0])
    years = rng.choice([2, 3])
    i = inf_rate / 100.0
    future_price = curr_price * ((1.0 + i) ** years)

    prompt = (
        f"A basket of essential groceries currently costs **R {curr_price:.2f}**.\n"
        f"If inflation averages **{inf_rate:g}% per annum**, calculate the expected price of the same basket in **{years} years**.\n\n"
        f"(Note: Inflation compounds annually: $A = P(1 + i)^n$)."
    )
    sol = (
        f"**Inflation Compounding:**\n"
        f"\\[ A = P(1 + i)^n \\]\n"
        f"\\[ A = {curr_price:.2f}(1 + {i})^{{{years}}} = \\text{{R }}{_fmt_dec(future_price, 2)} \\]"
    )
    ans = f"R {_fmt_dec(future_price, 2)}"
    return {
        "id": f"g9_fin_inflation_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "38_inflation_rate_calculate_future_price_of_goods",
        "learning_objective_id": "math_g9_fin_inflation",
        "hints": {
            "tier_1": "Inflation behaves as compound interest: A = P(1 + i)^n.",
            "tier_2": f"Calculate {curr_price:.2f} * (1 + {i})^{years}.",
            "tier_3": ans,
        },
        "misconception_tags": ["treating_inflation_as_simple_interest_instead_of_compounding"],
    }


# ----------------------------------------------------------------------
# 39. Percentage Increase and Decrease Calculation
# ----------------------------------------------------------------------
def arch_39_percentage_increase_and_decrease_calculation(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["increase", "decrease"])
    orig = rng.choice([400, 500, 650, 800, 1200])
    pct = rng.choice([10, 15, 20, 25])
    change = (orig * pct) / 100

    if choice == "increase":
        final_val = orig + change
        prompt = f"Increase **R {orig}** by **{pct}%**."
        sol = (
            f"**Percentage Increase:**\n"
            f"1. Amount of increase: \\(\\frac{{{pct}}}{{100}} \\times \\text{{R }}{orig} = \\text{{R }}{_fmt_dec(change, 2)}\\).\n"
            f"2. New price: \\(\\text{{R }}{orig} + \\text{{R }}{_fmt_dec(change, 2)} = \\text{{R }}{_fmt_dec(final_val, 2)}\\)."
        )
    else:
        final_val = orig - change
        prompt = f"Decrease **R {orig}** by **{pct}%**."
        sol = (
            f"**Percentage Decrease:**\n"
            f"1. Amount of decrease: \\(\\frac{{{pct}}}{{100}} \\times \\text{{R }}{orig} = \\text{{R }}{_fmt_dec(change, 2)}\\).\n"
            f"2. New price: \\(\\text{{R }}{orig} - \\text{{R }}{_fmt_dec(change, 2)} = \\text{{R }}{_fmt_dec(final_val, 2)}\\)."
        )

    ans = f"R {_fmt_dec(final_val, 2)}"
    return {
        "id": f"g9_pct_change_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "39_percentage_increase_and_decrease_calculation",
        "learning_objective_id": "math_g9_pct_change",
        "hints": {
            "tier_1": f"Find {pct}% of R {orig}.",
            "tier_2": "Add (for increase) or subtract (for decrease).",
            "tier_3": ans,
        },
        "misconception_tags": ["subtracting_percentage_directly_as_rands"],
    }


# ----------------------------------------------------------------------
# 40. Percentage Profit and Loss on Cost Price
# ----------------------------------------------------------------------
def arch_40_percentage_profit_and_loss_on_cost_price(rng: random.Random) -> Dict[str, Any]:
    cp = rng.choice([150, 200, 250, 400])
    is_profit = rng.choice([True, False])
    pct = rng.choice([15, 20, 25, 30])
    diff = (cp * pct) // 100

    if is_profit:
        sp = cp + diff
        kind = "profit"
    else:
        sp = cp - diff
        kind = "loss"

    prompt = (
        f"A storekeeper buys an article for **R {cp}** and sells it for **R {sp}**.\n\n"
        f"1. State whether this transaction represents a **profit** or a **loss**.\n"
        f"2. Calculate the **percentage {kind}** based on the cost price."
    )
    sol = (
        f"**Percentage {kind.capitalize()} Calculation:**\n"
        f"1. {kind.capitalize()} amount = \\(|{sp} - {cp}| = \\text{{R }}{diff}\\).\n"
        f"2. Percentage {kind}:\n"
        f"\\[ \\% \\text{{{kind}}} = \\frac{{\\text{{{kind.capitalize()}}}}}{{\\text{{Cost Price}}}} \\times 100 = \\frac{{{diff}}}{{{cp}}} \\times 100 = {pct}\\% \\]"
    )
    ans = f"1. {kind.capitalize()}; 2. {pct}%"
    return {
        "id": f"g9_profit_loss_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "40_percentage_profit_and_loss_on_cost_price",
        "learning_objective_id": "math_g9_profit_loss",
        "hints": {
            "tier_1": "Percentage profit or loss is ALWAYS calculated over the Cost Price.",
            "tier_2": f"Formula: (Profit or Loss / Cost Price) * 100.",
            "tier_3": ans,
        },
        "misconception_tags": ["calculating_profit_percentage_over_selling_price_instead_of_cost_price"],
    }


# ----------------------------------------------------------------------
# 41. Calculate Selling Price Given Markup Percentage
# ----------------------------------------------------------------------
def arch_41_calculate_selling_price_given_markup_percentage(rng: random.Random) -> Dict[str, Any]:
    cp = rng.choice([120, 240, 350, 480, 600])
    markup_pct = rng.choice([25, 30, 40, 50])
    markup_val = (cp * markup_pct) / 100
    sp = cp + markup_val

    prompt = (
        f"A merchant buys running shoes at a cost price of **R {cp}**.\n"
        f"The store applies a **{markup_pct}% markup** on cost price to establish the selling price.\n\n"
        f"Calculate the **selling price** of the shoes."
    )
    sol = (
        f"**Selling Price Calculation:**\n"
        f"1. Markup amount: \\(\\frac{{{markup_pct}}}{{100}} \\times \\text{{R }}{cp} = \\text{{R }}{_fmt_dec(markup_val, 2)}\\).\n"
        f"2. Selling Price = Cost Price + Markup = \\({cp} + {_fmt_dec(markup_val, 2)} = \\text{{R }}{_fmt_dec(sp, 2)}\\)."
    )
    ans = f"R {_fmt_dec(sp, 2)}"
    return {
        "id": f"g9_markup_sp_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "41_calculate_selling_price_given_markup_percentage",
        "learning_objective_id": "math_g9_markup_sp",
        "hints": {
            "tier_1": f"Find {markup_pct}% of R {cp}.",
            "tier_2": "Add the markup to the cost price.",
            "tier_3": ans,
        },
        "misconception_tags": ["leaving_only_the_markup_amount_without_adding_cost_price"],
    }


# ----------------------------------------------------------------------
# 42. Calculate Cost Price from Selling Price and Profit Percentage
# ----------------------------------------------------------------------
def arch_42_calculate_cost_price_from_selling_price_and_profit(rng: random.Random) -> Dict[str, Any]:
    cp = rng.choice([200, 300, 400, 500])
    profit_pct = rng.choice([20, 25, 50])
    sp = int(cp * (1 + profit_pct / 100))

    prompt = (
        f"A dealer sells a bicycle for **R {sp}**, making a **{profit_pct}% profit** on cost price.\n\n"
        f"Calculate the original **cost price** of the bicycle."
    )
    sol = (
        f"**Reverse Percentage Calculation:**\n"
        f"Since selling price represents $100\\% + {profit_pct}\\% = {100 + profit_pct}\\%$ of cost price:\n"
        f"\\[ \\text{{Selling Price}} = \\text{{Cost Price}} \\times \\left(1 + \\frac{{{profit_pct}}}{{100}}\\right) \\]\n"
        f"\\[ {sp} = \\text{{Cost Price}} \\times {1 + profit_pct/100:.2f} \\]\n"
        f"\\[ \\text{{Cost Price}} = \\frac{{{sp}}}{{{1 + profit_pct/100:.2f}}} = \\text{{R }}{cp} \\]"
    )
    ans = f"R {cp}"
    return {
        "id": f"g9_rev_cost_price_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "42_calculate_cost_price_from_selling_price_and_profit",
        "learning_objective_id": "math_g9_rev_cost_price",
        "hints": {
            "tier_1": f"R {sp} represents {100 + profit_pct}% of the cost price.",
            "tier_2": f"Divide R {sp} by {1 + profit_pct/100:.2f}.",
            "tier_3": ans,
        },
        "misconception_tags": ["subtracting_profit_percentage_from_selling_price_instead_of_dividing"],
    }


# ----------------------------------------------------------------------
# 43. Calculate VAT Inclusive and Exclusive Amounts (15% SA)
# ----------------------------------------------------------------------
def arch_43_calculate_vat_inclusive_and_exclusive_amounts_15_percent(rng: random.Random) -> Dict[str, Any]:
    excl = rng.choice([200, 400, 600, 800, 1200])
    vat = excl * 0.15
    incl = excl + vat

    prompt = (
        f"In South Africa, Value Added Tax (VAT) is charged at **15%**.\n"
        f"An invoice lists a service at **R {excl:.2f} excluding VAT**.\n\n"
        f"1. Calculate the VAT amount.\n"
        f"2. Calculate the total price including VAT."
    )
    sol = (
        f"**VAT Calculation (15%):**\n"
        f"1. VAT amount: \\(0{{,}}\\!15 \\times \\text{{R }}{excl:.2f} = \\text{{R }}{_fmt_dec(vat, 2)}\\).\n"
        f"2. Total VAT inclusive: \\(\\text{{R }}{excl:.2f} + \\text{{R }}{_fmt_dec(vat, 2)} = \\text{{R }}{_fmt_dec(incl, 2)}\\)."
    )
    ans = f"VAT: R {_fmt_dec(vat, 2)}, Total: R {_fmt_dec(incl, 2)}"
    return {
        "id": f"g9_vat_calc_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "43_calculate_vat_inclusive_and_exclusive_amounts_15_percent",
        "learning_objective_id": "math_g9_vat_calc",
        "hints": {
            "tier_1": "Multiply the exclusive amount by 0.15 to find the VAT.",
            "tier_2": "Add the VAT to the exclusive amount to find the inclusive price.",
            "tier_3": ans,
        },
        "misconception_tags": ["using_old_14_percent_vat_rate_instead_of_15_percent"],
    }


# ----------------------------------------------------------------------
# 44. Calculate Discount Percentage and Sale Price
# ----------------------------------------------------------------------
def arch_44_calculate_discount_percentage_and_sale_price(rng: random.Random) -> Dict[str, Any]:
    marked_price = rng.choice([350, 450, 600, 800, 1000])
    disc_pct = rng.choice([15, 20, 25, 30])
    discount = (marked_price * disc_pct) / 100
    sale_price = marked_price - discount

    prompt = (
        f"A jacket has a marked price of **R {marked_price}**.\n"
        f"During a seasonal sale, the store offers a **{disc_pct}% discount**.\n\n"
        f"1. Calculate the discount amount in Rands.\n"
        f"2. Calculate the final sale price of the jacket."
    )
    sol = (
        f"**Discount & Sale Price:**\n"
        f"1. Discount: \\(\\frac{{{disc_pct}}}{{100}} \\times \\text{{R }}{marked_price} = \\text{{R }}{_fmt_dec(discount, 2)}\\).\n"
        f"2. Sale Price = Marked Price - Discount = \\({marked_price} - {_fmt_dec(discount, 2)} = \\text{{R }}{_fmt_dec(sale_price, 2)}\\)."
    )
    ans = f"Discount: R {_fmt_dec(discount, 2)}, Sale Price: R {_fmt_dec(sale_price, 2)}"
    return {
        "id": f"g9_discount_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "44_calculate_discount_percentage_and_sale_price",
        "learning_objective_id": "math_g9_discount",
        "hints": {
            "tier_1": f"Discount = {disc_pct}% of R {marked_price}.",
            "tier_2": "Subtract the discount from marked price.",
            "tier_3": ans,
        },
        "misconception_tags": ["adding_discount_instead_of_subtracting"],
    }


# ----------------------------------------------------------------------
# 45. Exchange Rate: Convert ZAR to Foreign Currency
# ----------------------------------------------------------------------
def arch_45_exchange_rate_convert_zar_to_foreign_currency(rng: random.Random) -> Dict[str, Any]:
    currency, symbol, rate = rng.choice([
        ("US Dollars", "$", 18.50),
        ("British Pounds", "£", 23.50),
        ("Euros", "€", 20.00),
    ])
    zar_amount = rng.choice([3700, 4700, 7400, 9250, 11750])
    foreign = zar_amount / rate

    prompt = (
        f"A traveler has **R {zar_amount}** to exchange into **{currency} ({symbol})**.\n"
        f"The bank exchange rate is **{symbol} 1 = R {rate:.2f}**.\n\n"
        f"Calculate how many {currency} the traveler receives (round to two decimal places)."
    )
    sol = (
        f"**Currency Conversion (ZAR to Foreign):**\n"
        f"To convert South African Rands into foreign currency when the rate is 1 unit = R {rate:.2f}, divide by the exchange rate:\n"
        f"\\[ \\text{{Foreign Amount}} = \\frac{{\\text{{R }}{zar_amount}}}{{\\text{{R }}{rate:.2f}}} = {symbol} {_fmt_dec(foreign, 2)} \\]"
    )
    ans = f"{symbol} {_fmt_dec(foreign, 2)}"
    return {
        "id": f"g9_fx_to_foreign_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "45_exchange_rate_convert_zar_to_foreign_currency",
        "learning_objective_id": "math_g9_fx_to_foreign",
        "hints": {
            "tier_1": f"Divide ZAR amount by the exchange rate ({rate:.2f}).",
            "tier_2": f"R {zar_amount} / {rate:.2f}.",
            "tier_3": ans,
        },
        "misconception_tags": ["multiplying_by_rate_instead_of_dividing_when_converting_zar_to_stronger_currency"],
    }


# ----------------------------------------------------------------------
# 46. Exchange Rate: Convert Foreign Currency to ZAR
# ----------------------------------------------------------------------
def arch_46_exchange_rate_convert_foreign_currency_to_zar(rng: random.Random) -> Dict[str, Any]:
    currency, symbol, rate = rng.choice([
        ("US Dollars", "$", 18.20),
        ("British Pounds", "£", 23.40),
        ("Euros", "€", 19.80),
    ])
    f_amount = rng.choice([150, 250, 400, 500])
    zar = f_amount * rate

    prompt = (
        f"A tourist returning from abroad exchanges **{symbol} {f_amount}** back into South African Rands (ZAR).\n"
        f"If the current exchange rate is **{symbol} 1 = R {rate:.2f}**, calculate the amount received in Rands."
    )
    sol = (
        f"**Currency Conversion (Foreign to ZAR):**\n"
        f"Multiply foreign currency amount by the exchange rate:\n"
        f"\\[ \\text{{ZAR Amount}} = {f_amount} \\times \\text{{R }}{rate:.2f} = \\text{{R }}{_fmt_dec(zar, 2)} \\]"
    )
    ans = f"R {_fmt_dec(zar, 2)}"
    return {
        "id": f"g9_fx_to_zar_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "46_exchange_rate_convert_foreign_currency_to_zar",
        "learning_objective_id": "math_g9_fx_to_zar",
        "hints": {
            "tier_1": f"Multiply {f_amount} by the exchange rate ({rate:.2f}).",
            "tier_2": f"{f_amount} * {rate:.2f}.",
            "tier_3": ans,
        },
        "misconception_tags": ["dividing_by_rate_instead_of_multiplying_when_converting_to_zar"],
    }


# ----------------------------------------------------------------------
# 47. Exchange Rate: Traveler Budget Comparison
# ----------------------------------------------------------------------
def arch_47_exchange_rate_traveler_budget_comparison(rng: random.Random) -> Dict[str, Any]:
    rate_usd = 18.50
    hotel_usd = rng.choice([120, 150, 200])
    hotel_zar = hotel_usd * rate_usd

    budget_zar = rng.choice([3000, 4000, 5000])

    can_afford = budget_zar >= hotel_zar
    diff = abs(budget_zar - hotel_zar)

    prompt = (
        f"A traveler in New York wants to book a hotel room costing **$ {hotel_usd} per night**.\n"
        f"The exchange rate is **$ 1 = R {rate_usd:.2f}**.\n"
        f"The traveler has budgeted **R {budget_zar}** for the night's accommodation.\n\n"
        f"1. Convert the hotel cost to South African Rands.\n"
        f"2. Determine whether the traveler's budget is sufficient, and by how much."
    )
    sol = (
        f"**Budget Comparison:**\n"
        f"1. Cost in ZAR: \\({hotel_usd} \\times \\text{{R }}{rate_usd:.2f} = \\text{{R }}{_fmt_dec(hotel_zar, 2)}\\).\n"
        f"2. Comparison with budget: Budget is R {budget_zar}. "
        + (f"Yes, the budget is sufficient with R {_fmt_dec(diff, 2)} remaining." if can_afford else f"No, the traveler is short by R {_fmt_dec(diff, 2)}.")
    )
    ans = f"Hotel: R {_fmt_dec(hotel_zar, 2)}, Sufficient: {'Yes' if can_afford else 'No'}"
    return {
        "id": f"g9_fx_budget_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "47_exchange_rate_traveler_budget_comparison",
        "learning_objective_id": "math_g9_fx_budget",
        "hints": {
            "tier_1": f"Multiply $ {hotel_usd} by {rate_usd:.2f} to get ZAR cost.",
            "tier_2": f"Compare with R {budget_zar}.",
            "tier_3": ans,
        },
        "misconception_tags": ["dividing_usd_by_exchange_rate_when_converting_to_zar"],
    }


# ----------------------------------------------------------------------
# 48. Error Analysis: Distributive Multiplication Error
# ----------------------------------------------------------------------
def arch_48_error_analysis_diagnosing_distributive_multiplication_error(rng: random.Random) -> Dict[str, Any]:
    a = 4
    b = 12
    c = 5
    correct = a * (b + c)
    flawed = a * b + c  # forgot to multiply second term

    prompt = (
        f"A learner was asked to evaluate **{a} \\times ({b} + {c})** using the distributive property.\n\n"
        f"The learner wrote:\n"
        f"\\[ {a} \\times ({b} + {c}) = ({a} \\times {b}) + {c} = {a * b} + {c} = {flawed} \\]\n\n"
        f"1. Identify the mathematical error in the learner's working.\n"
        f"2. Provide the correct calculation and answer."
    )
    sol = (
        f"**Error Diagnosis:**\n"
        f"1. Error: The learner failed to distribute the factor {a} to the second term inside the brackets ({c}).\n"
        f"2. Correct working:\n"
        f"\\[ {a} \\times ({b} + {c}) = ({a} \\times {b}) + ({a} \\times {c}) = {a * b} + {a * c} = {correct} \\]"
    )
    ans = f"Did not multiply {c} by {a}; correct = {correct}"
    return {
        "id": f"g9_err_distrib_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "48_error_analysis_diagnosing_distributive_multiplication_error",
        "learning_objective_id": "math_g9_err_distrib",
        "hints": {
            "tier_1": f"The distributive rule requires a(b + c) = ab + ac.",
            "tier_2": f"Notice {c} was not multiplied by {a}.",
            "tier_3": ans,
        },
        "misconception_tags": ["distributing_factor_only_to_first_bracketed_term"],
    }


# ----------------------------------------------------------------------
# 49. Error Analysis: Hire Purchase Interest on Deposit Error
# ----------------------------------------------------------------------
def arch_49_error_analysis_diagnosing_hire_purchase_interest_on_deposit_error(rng: random.Random) -> Dict[str, Any]:
    cash = 10000
    dep = 2000
    bal = 8000
    r = 10.0
    t = 2

    correct_int = (bal * r * t) / 100.0  # 1600
    flawed_int = (cash * r * t) / 100.0   # 2000 (calculated on full cash price)

    prompt = (
        f"A customer buys a lounge suite for **R {cash}** on hire purchase, paying a **R {dep} deposit**.\n"
        f"The interest rate is **{r:g}% p.a. simple interest** over **{t} years**.\n\n"
        f"The salesperson calculates the interest as:\n"
        f"\\[ I = \\frac{{\\text{{R }}{cash} \\times {r:g} \\times {t}}}{{100}} = \\text{{R }}{flawed_int:.2f} \\]\n\n"
        f"1. Explain why this interest calculation is flawed.\n"
        f"2. Calculate the correct interest amount that should be charged on the balance."
    )
    sol = (
        f"**Hire Purchase Error Analysis:**\n"
        f"1. Flaw: Interest on hire purchase must only be charged on the **remaining balance** after the deposit is paid, "
        f"not on the original full cash price.\n"
        f"2. Correct balance: \\(\\text{{R }}{cash} - \\text{{R }}{dep} = \\text{{R }}{bal}\\).\n"
        f"3. Correct interest:\n"
        f"\\[ I = \\frac{{{bal} \\times {r:g} \\times {t}}}{{100}} = \\text{{R }}{_fmt_dec(correct_int, 2)} \\]"
    )
    ans = f"Charged interest on full cash price instead of balance; correct interest = R {_fmt_dec(correct_int, 2)}"
    return {
        "id": f"g9_err_hp_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "49_error_analysis_diagnosing_hire_purchase_interest_on_deposit_error",
        "learning_objective_id": "math_g9_err_hp",
        "hints": {
            "tier_1": "Customers do not pay interest on money they have already paid as a deposit.",
            "tier_2": f"Calculate interest on R {bal} instead of R {cash}.",
            "tier_3": ans,
        },
        "misconception_tags": ["charging_interest_on_deposit_portion_of_hire_purchase"],
    }


# ----------------------------------------------------------------------
# 50. Compound Financial Word Problem: Investment Comparison
# ----------------------------------------------------------------------
def arch_50_compound_financial_word_problem_investment_comparison(rng: random.Random) -> Dict[str, Any]:
    principal = 20000
    years = 3

    # Bank A: Simple interest 11% p.a.
    r_si = 11.0
    si_total = principal * (1 + (r_si / 100.0) * years)

    # Bank B: Compound interest 9.5% p.a.
    r_ci = 9.5
    ci_total = principal * ((1 + (r_ci / 100.0)) ** years)

    better = "Bank A" if si_total > ci_total else "Bank B"
    diff = abs(si_total - ci_total)

    prompt = (
        f"Kagiso has **R {principal}** to invest for **{years} years** and compares two banks:\n"
        f"- **Bank A:** Offers **{r_si:g}% p.a. Simple Interest**.\n"
        f"- **Bank B:** Offers **{r_ci:g}% p.a. Compound Interest** (compounded annually).\n\n"
        f"1. Calculate the final accumulated amount at Bank A.\n"
        f"2. Calculate the final accumulated amount at Bank B.\n"
        f"3. Which bank should Kagiso choose, and how much more money will he make?"
    )
    sol = (
        f"**Investment Evaluation:**\n"
        f"1. Bank A (Simple Interest):\n"
        f"\\[ A_A = {principal}\\left(1 + \\frac{{{r_si:g} \\times {years}}}{{100}}\\right) = \\text{{R }}{_fmt_dec(si_total, 2)} \\]\n"
        f"2. Bank B (Compound Interest):\n"
        f"\\[ A_B = {principal}\\left(1 + \\frac{{{r_ci:g}}}{{100}}\\right)^{{{years}}} = \\text{{R }}{_fmt_dec(ci_total, 2)} \\]\n"
        f"3. Comparison:\n"
        f"Difference = \\(|{_fmt_dec(si_total, 2)} - {_fmt_dec(ci_total, 2)}| = \\text{{R }}{_fmt_dec(diff, 2)}\\).\n"
        f"Kagiso should choose **{better}**."
    )
    ans = f"Bank A: R {_fmt_dec(si_total, 2)}, Bank B: R {_fmt_dec(ci_total, 2)}, Choice: {better} (by R {_fmt_dec(diff, 2)})"
    return {
        "id": f"g9_fin_compare_banks_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "50_compound_financial_word_problem_investment_comparison",
        "learning_objective_id": "math_g9_fin_compare_banks",
        "hints": {
            "tier_1": "Calculate final amount for Bank A using P(1 + in).",
            "tier_2": "Calculate final amount for Bank B using P(1 + i)^n.",
            "tier_3": ans,
        },
        "misconception_tags": ["assuming_compound_interest_always_beats_simple_interest_regardless_of_rate"],
    }
