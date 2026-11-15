"""Grade 10 Mathematics — Term 3: Finance and Growth (Archetypes 26 to 50).

Grounded strictly in curriculum_docs_auto/Mathematics_Gr10/Term 3/01. Finance and growth.md.
Deterministic SymPy / math calculations with authentic South African Rand (R) and comma decimals ({,}).
Zero-LLM, 100% curriculum aligned.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from .finance_growth_archetypes_01_25 import (
    ASSETS,
    CURRENCY_RATES,
    SA_NAMES,
    SUBTOPIC_ID,
    TOPIC_ID,
    TOPIC_NAME,
    _build_typed_math,
    _fmt_dec,
    _fmt_r,
)


def _timeline_svg(p: int, p2: int, t1: int, t_tot: int) -> str:
    """Context SVG timeline diagram for split deposits."""
    w, h = 540, 110
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
        f'<rect width="{w}" height="{h}" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<line x1="50" y1="55" x2="490" y2="55" stroke="#334155" stroke-width="2.5"/>'
        f'<circle cx="50" cy="55" r="5" fill="#2563eb"/>'
        f'<circle cx="270" cy="55" r="5" fill="#059669"/>'
        f'<circle cx="490" cy="55" r="5" fill="#dc2626"/>'
        f'<text x="50" y="38" font-size="11" font-weight="bold" text-anchor="middle" fill="#2563eb">t = 0: {_fmt_r(p)}</text>'
        f'<text x="270" y="38" font-size="11" font-weight="bold" text-anchor="middle" fill="#059669">t = {t1} yrs: +{_fmt_r(p2)}</text>'
        f'<text x="490" y="38" font-size="11" font-weight="bold" text-anchor="middle" fill="#dc2626">t = {t_tot} yrs: A = ?</text>'
        f'<text x="50" y="78" font-size="10" text-anchor="middle" fill="#64748b">Start</text>'
        f'<text x="270" y="78" font-size="10" text-anchor="middle" fill="#64748b">Deposit added</text>'
        f'<text x="490" y="78" font-size="10" text-anchor="middle" fill="#64748b">Final withdrawal</text>'
        f'</svg>'
    )


# ---------------------------------------------------------------------------
# Archetypes 26 - 50
# ---------------------------------------------------------------------------

def build_26_compound_interest_stepwise_table_derivation(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(4, 15) * 1000
    r_pct = rng.choice([5.0, 6.0, 8.0, 10.0])
    i = r_pct / 100.0
    a1 = p * (1 + i)
    a2 = a1 * (1 + i)
    ans = _fmt_r(a2)

    prompt = (
        f"{name} invests {_fmt_r(p)} at a compound interest rate of {_fmt_dec(r_pct, 1)}% p.a. compounded annually. "
        f"By calculating the balance at the end of Year 1 first ($A_1$), and then using $A_1$ as the new principal for Year 2, "
        f"determine the exact accumulated balance at the end of Year 2."
    )
    worked = (
        f"**Step 1 — Year 1 Balance ($A_1$):**\n"
        f"$A_1 = P(1 + i) = {p}(1 + {_fmt_dec(i, 4)}) = {_fmt_r(a1)}$\n\n"
        f"**Step 2 — Year 2 Balance ($A_2$ using $A_1$ as principal):**\n"
        f"$A_2 = A_1(1 + i) = {_fmt_r(a1)}(1 + {_fmt_dec(i, 4)}) = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin26",
        subskill="26_compound_interest_stepwise_table_derivation",
        title="Compound Interest: Step-by-Step Year-by-Year Derivation",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Calculate the end of Year 1 balance first: $A_1 = P(1 + i)$.",
            "tier_2": f"Year 1 balance = {_fmt_r(a1)}.",
            "tier_3": f"Multiply {_fmt_r(a1)} by (1 + {_fmt_dec(i, 4)}) to find Year 2: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Calculates Year 1 balance $A_1 = {_fmt_r(a1)}$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Applies interest to $A_1$ for Year 2", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct Year 2 balance {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["calculated_simple_interest_instead_of_stepwise_compound"],
    )


def build_27_compound_interest_graph_linear_vs_exponential(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(5, 20) * 1000
    ans = "Simple interest is linear (straight line) while compound interest is exponential (curve)"

    prompt = (
        f"{name} plots two financial growth graphs on the Cartesian plane representing an investment of {_fmt_r(p)} over 20 years: "
        f"one graph shows simple interest and the other shows compound interest. "
        f"Describe the geometric shape of each graph and explain why compound interest curves upwards."
    )
    worked = (
        f"- **Simple interest** forms a **linear graph (straight line)** because the rate of change is constant ($P \\cdot i$ added each year).\n"
        f"- **Compound interest** forms an **exponential graph (concave upwards curve)** because interest is calculated on an ever-increasing balance (interest on interest)."
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin27",
        subskill="27_compound_interest_graph_linear_vs_exponential",
        title="Graphical Comparison: Linear vs Exponential Growth",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=2,
        hints={
            "tier_1": "Think about whether the growth amount added each year stays constant or increases.",
            "tier_2": "Constant additions create a straight line; multiplying by $(1+i)$ creates an exponential curve.",
            "tier_3": "Simple = linear straight line; Compound = exponential curve.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Identifies simple interest as linear / straight line", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Identifies compound interest as exponential curve due to interest on interest", "marks": 1, "editable": True},
        ],
        misconception_tags=["confused_linear_and_exponential_graphs"],
    )


def build_28_simple_interest_days_conversion(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(4, 16) * 1000
    r_pct = rng.choice([7.3, 8.0, 10.95, 14.6])  # clean multiples of 365
    days = rng.choice([90, 120, 180, 240])
    i = r_pct / 100.0
    interest = p * i * (days / 365.0)
    ans = _fmt_r(interest)

    prompt = (
        f"{name} takes a bridge loan of {_fmt_r(p)} for exactly {days} days at a simple interest rate of "
        f"{_fmt_dec(r_pct, 2)}% per annum. "
        f"Calculate the interest charged on the loan (assume 365 days in a year)."
    )
    worked = (
        f"**Step 1 — Convert days to years:** $n = \\frac{{{days}}}{{365}}$\n\n"
        f"**Step 2 — Calculate interest:** $I = P \\times i \\times n$\n\n"
        f"**Substitution:** $I = {p} \\times {_fmt_dec(i, 5)} \\times \\frac{{{days}}}{{365}} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin28",
        subskill="28_simple_interest_days_conversion",
        title="Simple Interest: Converting Days to Years ($n = d / 365$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Divide the number of days by 365 to convert the time period into years.",
            "tier_2": f"Use $I = P \\cdot i \\cdot (days / 365)$ with $P = {p}$, $i = {_fmt_dec(i, 4)}$.",
            "tier_3": f"Calculate {p} * {_fmt_dec(i, 4)} * ({days} / 365) = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Divides {days} by 365", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes into $I = P \\cdot i \\cdot n$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct interest {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["divided_by_360_instead_of_365"],
    )


def build_29_compound_interest_fractional_years(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(8, 25) * 1000
    r_pct = rng.choice([6.0, 8.0, 10.0])
    months = rng.choice([18, 30, 42])
    n = months / 12.0
    i = r_pct / 100.0
    a = p * ((1.0 + i) ** n)
    ans = _fmt_r(a)

    prompt = (
        f"{name} invested {_fmt_r(p)} at {_fmt_dec(r_pct, 1)}% per annum compound interest for {months} months. "
        f"Calculate the accumulated amount at the end of the investment period."
    )
    worked = (
        f"**Step 1 — Convert months to years:** $n = \\frac{{{months}}}{{12}} = {_fmt_dec(n, 1)}$ years\n\n"
        f"**Step 2 — Apply compound formula:** $A = P(1 + i)^n$\n\n"
        f"**Substitution:** $A = {p}(1 + {_fmt_dec(i, 4)})^{{{_fmt_dec(n, 1)}}} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin29",
        subskill="29_compound_interest_fractional_years",
        title="Compound Interest: Fractional Years ($n = \\text{months} / 12$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Convert months to years by dividing by 12.",
            "tier_2": f"$n = {months} / 12 = {_fmt_dec(n, 1)}$ years.",
            "tier_3": f"Calculate $A = {p}(1 + {_fmt_dec(i, 4)})^{{{_fmt_dec(n, 1)}}} = {ans}$.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Converts {months} months to {_fmt_dec(n, 1)} years", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes into $A = P(1+i)^n$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct accumulated amount {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["used_months_as_exponent_directly"],
    )


def build_30_hire_purchase_solve_for_deposit_percentage(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(4, 20) * 1000
    dep_pct = rng.choice([10, 15, 20, 25])
    deposit = int(cash_price * (dep_pct / 100.0))
    ans = f"{dep_pct}%"

    prompt = (
        f"{name} bought a {asset} with a cash price of {_fmt_r(cash_price)} on hire purchase. "
        f"If the upfront deposit paid was {_fmt_r(deposit)}, calculate the deposit percentage required by the store."
    )
    worked = (
        f"$$\\text{{Deposit \\%}} = \\frac{{\\text{{Deposit Amount}}}}{{\\text{{Cash Price}}}} \\times 100$$\n\n"
        f"$$\\text{{Deposit \\%}} = \\frac{{{deposit}}}{{{cash_price}}} \\times 100 = \\mathbf{{{ans}}}$$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin30",
        subskill="30_hire_purchase_solve_for_deposit_percentage",
        title="Hire Purchase: Solving for Deposit Percentage",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=2,
        hints={
            "tier_1": "Divide the deposit amount by the cash price, then multiply by 100.",
            "tier_2": f"({deposit} / {cash_price}) * 100.",
            "tier_3": f"Result is {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Sets up ratio (Deposit / Cash Price) * 100", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct percentage {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["divided_by_loan_balance_instead_of_cash_price"],
    )


def build_31_hire_purchase_reverse_cash_price(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(5, 25) * 1000
    dep_pct = rng.choice([10, 15, 20])
    deposit = int(cash_price * (dep_pct / 100.0))
    ans = _fmt_r(cash_price)

    prompt = (
        f"{name} paid a {dep_pct}% deposit of {_fmt_r(deposit)} when buying a {asset} on hire purchase. "
        f"What was the original cash price of the {asset}?"
    )
    worked = (
        f"$$\\text{{Cash Price}} = \\frac{{\\text{{Deposit}}}}{{\\text{{Deposit \\%}}}} = \\frac{{{_fmt_r(deposit)}}}{{{dep_pct} / 100}} = \\mathbf{{{ans}}}$$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin31",
        subskill="31_hire_purchase_reverse_cash_price",
        title="Hire Purchase: Reverse Finding Cash Price from Deposit",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=2,
        hints={
            "tier_1": f"If {dep_pct}% equals {_fmt_r(deposit)}, then 100% equals {_fmt_r(deposit)} / ({dep_pct}/100).",
            "tier_2": f"Divide {deposit} by {dep_pct / 100}.",
            "tier_3": f"{deposit} / {dep_pct / 100} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Divides deposit by decimal percentage", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct cash price {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["multiplied_deposit_by_percentage"],
    )


def build_32_hire_purchase_total_interest_rate_reverse(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(8, 20) * 1000
    dep_pct = 10
    r_pct = rng.choice([10.0, 12.0, 15.0])
    years = 2
    months = 24
    deposit = cash_price * 0.10
    p_loan = cash_price - deposit
    i = r_pct / 100.0
    a_repay = p_loan * (1 + i * years)
    monthly = a_repay / months
    ans = f"{_fmt_dec(r_pct, 1)}%"

    prompt = (
        f"{name} bought a {asset} for {_fmt_r(cash_price)} cash. "
        f"After paying a 10% deposit, the balance was settled over 24 months in monthly instalments of {_fmt_r(monthly)}. "
        f"Calculate the simple interest rate per annum ($r\\%$) charged on the hire purchase agreement."
    )
    worked = (
        f"**Step 1 — Financed balance:** $P = {_fmt_r(cash_price)} - 10\\% = {_fmt_r(p_loan)}$\n\n"
        f"**Step 2 — Total repaid:** $A = 24 \\times {_fmt_r(monthly)} = {_fmt_r(a_repay)}$\n\n"
        f"**Step 3 — Interest charged:** $I = {_fmt_r(a_repay)} - {_fmt_r(p_loan)} = {_fmt_r(a_repay - p_loan)}$\n\n"
        f"**Step 4 — Simple interest rate:** $i = \\frac{{I}}{{P \\times n}} = \\frac{{{a_repay - p_loan}}}{{{p_loan} \\times 2}} = {_fmt_dec(i, 4)} \\implies \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin32",
        subskill="32_hire_purchase_total_interest_rate_reverse",
        title="Hire Purchase: Reverse Finding the Interest Rate",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Find total repayment ($24 \\times \\text{instalment}$) and principal loan ($P$).",
            "tier_2": "Find interest $I = A - P$, then use $i = \\frac{I}{P \\cdot n}$ with $n = 2$.",
            "tier_3": f"Convert decimal to percentage: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates total repaid $A = 24 \\times \\text{instalment}$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Finds total interest $I = A - P$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Solves for $i = I / (P \\cdot n)$", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct interest rate {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["divided_by_total_repayment_instead_of_principal"],
    )


def build_33_hire_purchase_loan_term_in_months(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(6, 18) * 1000
    dep_pct = 15
    deposit = cash_price * 0.15
    p_loan = cash_price - deposit
    r_pct = 12.0
    years = rng.choice([2, 3])
    months = years * 12
    a_repay = p_loan * (1 + (r_pct / 100.0) * years)
    monthly = a_repay / months
    ans = f"{months} months"

    prompt = (
        f"{name} bought a {asset} costing {_fmt_r(cash_price)}. "
        f"A 15% deposit was paid, and the store added 12% p.a. simple interest on the loan balance, resulting in total repayments of {_fmt_r(a_repay)}. "
        f"If {name} pays monthly instalments of {_fmt_r(monthly)}, how many months will the agreement run for?"
    )
    worked = (
        f"$$\\text{{Number of months}} = \\frac{{\\text{{Total Amount Repaid ($A$)}}}}{{\\text{{Monthly Instalment}}}}\n\n"
        f"$$\\text{{Number of months}} = \\frac{{{_fmt_r(a_repay)}}}{{{_fmt_r(monthly)}}} = \\mathbf{{{ans}}}$$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin33",
        subskill="33_hire_purchase_loan_term_in_months",
        title="Hire Purchase: Calculating Loan Term in Months",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=2,
        hints={
            "tier_1": "Divide the total repayments $A$ by the monthly instalment amount.",
            "tier_2": f"Divide {_fmt_r(a_repay)} by {_fmt_r(monthly)}.",
            "tier_3": f"{a_repay} / {monthly} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Sets up total repayment / monthly instalment", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct number of months: {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["gave_years_instead_of_months"],
    )


def build_34_inflation_average_annual_rate_calculation(rng: random.Random) -> Dict[str, Any]:
    goods = "a basket of staple groceries"
    p0 = rng.randint(4, 9) * 100
    inf_pct = rng.choice([5.0, 6.0, 7.0, 8.0])
    years = rng.choice([3, 4, 5])
    i = inf_pct / 100.0
    p_now = p0 * ((1.0 + i) ** years)
    ans = f"{_fmt_dec(inf_pct, 1)}%"

    prompt = (
        f"Five years ago, {goods} cost {_fmt_r(p0)}. "
        f"Today, the same basket costs {_fmt_r(p_now)}. "
        f"Calculate the average annual inflation rate over this {years}-year period."
    )
    worked = (
        f"**Formula:** $A = P(1 + i)^n \\implies 1 + i = \\sqrt[{years}]{{\\frac{{A}}{{P}}}}$\n\n"
        f"**Substitution:** $1 + i = \\sqrt[{years}]{{\\frac{{{_fmt_r(p_now)}}}{{{_fmt_r(p0)}}}}} = {_fmt_dec(1 + i, 4)}$\n\n"
        f"**Inflation rate:** $i = {_fmt_dec(i, 4)} \\implies \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin34",
        subskill="34_inflation_average_annual_rate_calculation",
        title="Inflation: Calculating Average Annual Inflation Rate",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Use the compound growth formula $A = P(1 + i)^n$ and solve for $i$.",
            "tier_2": f"Divide $A / P$, then take the {years}-th root.",
            "tier_3": f"Subtract 1 and multiply by 100 to get {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Uses $A = P(1 + i)^n$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Takes {years}-th root of $(A / P)$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Subtracts 1 to isolate $i$", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct inflation rate {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["divided_price_increase_by_n_years_linearly"],
    )


def build_35_inflation_purchasing_power_erosion(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    amount = rng.randint(5, 20) * 1000
    inf_pct = rng.choice([5.0, 6.0, 7.0])
    years = rng.randint(4, 8)
    i = inf_pct / 100.0
    real_power = amount / ((1.0 + i) ** years)
    ans = _fmt_r(real_power)

    prompt = (
        f"{name} hides {_fmt_r(amount)} in cash under a mattress. "
        f"If the average annual inflation rate is {_fmt_dec(inf_pct, 1)}% over the next {years} years, "
        f"calculate what this cash will be worth in real purchasing power (in terms of today's money) at the end of {years} years."
    )
    worked = (
        f"**Concept:** Inflation reduces purchasing power so that $P = \\frac{{A}}{{(1 + i)^n}}$\n\n"
        f"**Calculation:** $\\text{{Real value}} = \\frac{{{_fmt_r(amount)}}}{{(1 + {_fmt_dec(i, 4)})^{{{years}}}}} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin35",
        subskill="35_inflation_purchasing_power_erosion",
        title="Inflation: Erosion of Cash Purchasing Power",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Because inflation reduces what money can buy, divide the fixed cash by $(1 + i)^n$.",
            "tier_2": f"Divide {_fmt_r(amount)} by (1 + {_fmt_dec(i, 4)})^{years}.",
            "tier_3": f"Result is {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Sets up division by $(1 + i)^n$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes inflation rate and time", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct real purchasing power {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["multiplied_by_inflation_factor_instead_of_dividing"],
    )


def build_36_population_percentage_growth_rate_reverse(rng: random.Random) -> Dict[str, Any]:
    town = rng.choice(["Kimberley", "Mthatha", "Klerksdorp", "Paarl"])
    p0 = rng.randint(40, 90) * 1000
    g_pct = rng.choice([2.5, 3.0, 3.5, 4.0])
    years = rng.choice([5, 6, 7])
    i = g_pct / 100.0
    p_end = int(round(p0 * ((1.0 + i) ** years)))
    ans = f"{_fmt_dec(g_pct, 1)}%"

    prompt = (
        f"The population of {town} was {p0:,} in 2015 and grew to {p_end:,} in {2015 + years}. "
        f"Assuming compound population growth, calculate the annual percentage growth rate of {town}."
    ).replace(",", " ")

    worked = (
        f"**Formula:** $A = P(1 + i)^n \\implies 1 + i = \\left(\\frac{{A}}{{P}}\\right)^{{1/{years}}}$\n\n"
        f"**Substitution:** $1 + i = \\left(\\frac{{{p_end}}}{{{p0}}}\\right)^{{1/{years}}} = {_fmt_dec(1 + i, 4)}$\n\n"
        f"**Growth rate:** $i = {_fmt_dec(i, 4)} \\implies \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin36",
        subskill="36_population_percentage_growth_rate_reverse",
        title="Population: Deducing Annual Growth Rate",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Divide final population by initial population, then take the $n$-th root.",
            "tier_2": f"Calculate ({p_end} / {p0})^(1/{years}).",
            "tier_3": f"Subtract 1 to find the decimal rate, then multiply by 100: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Uses compound growth equation for population", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Takes {years}-th root", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct growth rate {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["divided_growth_linearly"],
    )


def build_37_foreign_exchange_bank_buying_vs_selling_margin(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    curr_name, sym, base = ("US Dollar (USD)", "$", 18.50)
    bank_sell = base + 0.40  # bank sells USD to traveller at R18.90
    bank_buy = base - 0.40   # bank buys USD from traveller at R18.10
    usd_amount = rng.choice([200, 300, 400])
    cost_to_buy_zar = round(usd_amount * bank_sell, 2)
    payout_on_return_zar = round(usd_amount * bank_buy, 2)
    bank_profit = cost_to_buy_zar - payout_on_return_zar
    ans = _fmt_r(bank_profit)

    prompt = (
        f"A South African commercial bank quotes the following exchange rates for {curr_name}:\n"
        f"- Bank Selling Rate: {sym} 1 = R {_fmt_dec(bank_sell, 2)}\n"
        f"- Bank Buying Rate: {sym} 1 = R {_fmt_dec(bank_buy, 2)}\n\n"
        f"{name} buys {sym} {usd_amount} from the bank before travelling, but cancels the trip and immediately sells all {sym} {usd_amount} back to the bank. "
        f"How much money in South African Rand did {name} lose due to the bank's exchange margin?"
    )
    worked = (
        f"**Step 1 — Cost to buy {sym} {usd_amount} from the bank (Bank Selling Rate):**\n"
        f"$\\text{{Cost}} = {usd_amount} \\times {_fmt_dec(bank_sell, 2)} = {_fmt_r(cost_to_buy_zar)}$\n\n"
        f"**Step 2 — Payout when selling {sym} {usd_amount} back to the bank (Bank Buying Rate):**\n"
        f"$\\text{{Payout}} = {usd_amount} \\times {_fmt_dec(bank_buy, 2)} = {_fmt_r(payout_on_return_zar)}$\n\n"
        f"**Step 3 — Loss (Bank margin):**\n"
        f"$\\text{{Loss}} = {_fmt_r(cost_to_buy_zar)} - {_fmt_r(payout_on_return_zar)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin37",
        subskill="37_foreign_exchange_bank_buying_vs_selling_margin",
        title="Foreign Exchange: Bank Buying vs Selling Rates (Bid-Ask Spread)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "The bank SELLS foreign currency at the higher rate, and BUYS foreign currency back at the lower rate.",
            "tier_2": f"Cost to buy: {usd_amount} * {_fmt_dec(bank_sell, 2)}; Payout on return: {usd_amount} * {_fmt_dec(bank_buy, 2)}.",
            "tier_3": f"Subtract the payout from the initial cost: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates purchase cost using selling rate", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Calculates return payout using buying rate", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Subtracts payout from cost", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct Rand loss {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["reversed_bank_buying_and_selling_rates"],
    )


def build_38_foreign_exchange_commission_fee_deduction(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    zar_budget = rng.randint(15, 40) * 1000
    comm_pct = rng.choice([1.5, 2.0, 2.5])
    rate = 18.60
    comm_fee = zar_budget * (comm_pct / 100.0)
    net_zar = zar_budget - comm_fee
    usd_received = round(net_zar / rate, 2)
    ans = f"$ {_fmt_dec(usd_received, 2)}"

    prompt = (
        f"{name} has {_fmt_r(zar_budget)} to exchange for US Dollars ($). "
        f"The foreign exchange bureau charges a {comm_pct}% commission fee on the Rand value exchanged. "
        f"If the exchange rate is $ 1 = R {_fmt_dec(rate, 2)}, how many US Dollars does {name} receive after the commission is deducted?"
    )
    worked = (
        f"**Step 1 — Calculate bureau commission fee:**\n"
        f"$\\text{{Commission}} = {_fmt_r(zar_budget)} \\times {comm_pct}\\% = {_fmt_r(comm_fee)}$\n\n"
        f"**Step 2 — Net Rand available for exchange:**\n"
        f"$\\text{{Net ZAR}} = {_fmt_r(zar_budget)} - {_fmt_r(comm_fee)} = {_fmt_r(net_zar)}$\n\n"
        f"**Step 3 — Convert to USD:**\n"
        f"$\\text{{USD received}} = \\frac{{{_fmt_r(net_zar)}}}{{{_fmt_dec(rate, 2)}}} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin38",
        subskill="38_foreign_exchange_commission_fee_deduction",
        title="Foreign Exchange: Deducting Bureau Commission Fees",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Calculate the commission fee first and subtract it from the initial Rand budget.",
            "tier_2": f"Net Rand = {_fmt_r(zar_budget)} - {_fmt_r(comm_fee)} = {_fmt_r(net_zar)}.",
            "tier_3": f"Divide net Rand by {_fmt_dec(rate, 2)} to get {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates commission fee in Rand", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Deducts commission from initial budget", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Divides net Rand by exchange rate", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct USD received: {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["converted_raw_rand_without_deducting_commission"],
    )


def build_39_foreign_exchange_multi_currency_trip_conversion(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    rate_usd = 18.50
    rate_eur = 20.00
    usd_spent = rng.randint(4, 9) * 100
    eur_spent = rng.randint(3, 7) * 100
    total_zar = round(usd_spent * rate_usd + eur_spent * rate_eur, 2)
    ans = _fmt_r(total_zar)

    prompt = (
        f"{name} goes on an overseas business trip and spends $ {usd_spent} in New York and € {eur_spent} in Frankfurt. "
        f"Given exchange rates of $ 1 = R {_fmt_dec(rate_usd, 2)} and € 1 = R {_fmt_dec(rate_eur, 2)}, "
        f"calculate the total trip expenditure in South African Rand (ZAR)."
    )
    worked = (
        f"**1. New York expenditure in ZAR:**\n"
        f"${usd_spent} \\times {_fmt_dec(rate_usd, 2)} = {_fmt_r(usd_spent * rate_usd)}$\n\n"
        f"**2. Frankfurt expenditure in ZAR:**\n"
        f"€{eur_spent} \\times {_fmt_dec(rate_eur, 2)} = {_fmt_r(eur_spent * rate_eur)}$\n\n"
        f"**3. Total expenditure in ZAR:**\n"
        f"${_fmt_r(usd_spent * rate_usd)} + {_fmt_r(eur_spent * rate_eur)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin39",
        subskill="39_foreign_exchange_multi_currency_trip_conversion",
        title="Foreign Exchange: Multi-Currency Overseas Itinerary",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Convert each foreign currency amount into Rand separately, then add the results.",
            "tier_2": f"USD in ZAR = {usd_spent} * {_fmt_dec(rate_usd, 2)}; EUR in ZAR = {eur_spent} * {_fmt_dec(rate_eur, 2)}.",
            "tier_3": f"Sum both Rand values to get {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Converts USD expenditure to ZAR", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Converts EUR expenditure to ZAR", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct total Rand expenditure {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["added_foreign_currencies_directly_before_converting"],
    )


def build_40_foreign_exchange_currency_depreciation_impact(rng: random.Random) -> Dict[str, Any]:
    comp_price_usd = rng.randint(8, 20) * 100
    rate_before = 18.00
    rate_after = 19.50
    zar_before = comp_price_usd * rate_before
    zar_after = comp_price_usd * rate_after
    increase = zar_after - zar_before
    ans = _fmt_r(increase)

    prompt = (
        f"A South African electronics distributor imports computer components priced at $ {comp_price_usd}. "
        f"Initially, the exchange rate was $ 1 = R {_fmt_dec(rate_before, 2)}. "
        f"Following market shifts, the Rand depreciated so that $ 1 = R {_fmt_dec(rate_after, 2)}. "
        f"How much MORE in South African Rand must the distributor pay for the components due to the depreciation?"
    )
    worked = (
        f"**Initial cost in ZAR:** ${comp_price_usd} \\times {_fmt_dec(rate_before, 2)} = {_fmt_r(zar_before)}$\n\n"
        f"**New cost in ZAR:** ${comp_price_usd} \\times {_fmt_dec(rate_after, 2)} = {_fmt_r(zar_after)}$\n\n"
        f"**Increase in cost:** ${_fmt_r(zar_after)} - {_fmt_r(zar_before)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin40",
        subskill="40_foreign_exchange_currency_depreciation_impact",
        title="Foreign Exchange: Impact of Rand Depreciation on Import Costs",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Calculate the Rand cost before and after the exchange rate change.",
            "tier_2": f"Initial cost: {_fmt_r(zar_before)}; New cost: {_fmt_r(zar_after)}.",
            "tier_3": f"Subtract to find the extra cost: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates initial cost in Rand", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Calculates new cost in Rand", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct cost increase {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["subtracted_exchange_rates_without_multiplying_by_usd"],
    )


def build_41_simple_interest_multiple_deposits_timeline(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p1 = rng.randint(4, 12) * 1000
    p2 = rng.randint(3, 8) * 1000
    r_pct = 8.0
    i = 0.08
    t_add = 2
    t_tot = 5
    # P1 earns for 5 years, P2 earns for (5 - 2) = 3 years
    a1 = p1 * (1 + i * t_tot)
    a2 = p2 * (1 + i * (t_tot - t_add))
    tot_a = a1 + a2
    ans = _fmt_r(tot_a)
    svg = _timeline_svg(p1, p2, t_add, t_tot)

    prompt = (
        f"{name} deposits {_fmt_r(p1)} into a simple interest savings account at 8% p.a. "
        f"Two years later, {name} deposits a further {_fmt_r(p2)} into the same account. "
        f"Inspect the timeline diagram below. "
        f"Calculate the total balance accumulated in the account 5 years after the initial deposit."
    )
    worked = (
        f"**1. Initial deposit ({_fmt_r(p1)}) earns interest for 5 years:**\n"
        f"$A_1 = {p1}(1 + 0,08 \\times 5) = {_fmt_r(a1)}$\n\n"
        f"**2. Second deposit ({_fmt_r(p2)}) earns interest for $5 - 2 = 3$ years:**\n"
        f"$A_2 = {p2}(1 + 0,08 \\times 3) = {_fmt_r(a2)}$\n\n"
        f"**3. Total accumulated balance:**\n"
        f"$A = A_1 + A_2 = {_fmt_r(a1)} + {_fmt_r(a2)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin41",
        subskill="41_simple_interest_multiple_deposits_timeline",
        title="Simple Interest: Multiple Deposits on a Timeline",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Calculate the accumulated value of each deposit separately over its respective investment time.",
            "tier_2": f"Deposit 1 earns for 5 years; Deposit 2 earns for 5 - 2 = 3 years.",
            "tier_3": f"Add the two accumulated amounts: {_fmt_r(a1)} + {_fmt_r(a2)} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates growth of first deposit over 5 years", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Calculates growth of second deposit over 3 years", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Adds both accumulated amounts", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct total balance {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["assumed_second_deposit_earned_for_full_5_years"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_42_compound_interest_timeline_single_rate_change(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(10, 30) * 1000
    r1 = 7.0
    r2 = 9.0
    i1, i2 = 0.07, 0.09
    t1 = 3
    t2 = 2
    a1 = p * ((1.0 + i1) ** t1)
    a_final = a1 * ((1.0 + i2) ** t2)
    ans = _fmt_r(a_final)

    prompt = (
        f"{name} invested {_fmt_r(p)} in a compound interest account for 5 years. "
        f"For the first 3 years, the rate was 7% p.a. compounded annually. "
        f"For the remaining 2 years, the rate changed to 9% p.a. compounded annually. "
        f"Calculate the final accumulated value after 5 years."
    )
    worked = (
        f"**Step 1 — Value after first 3 years:**\n"
        f"$A_3 = P(1 + i_1)^3 = {p}(1 + 0,07)^3 = {_fmt_r(a1)}$\n\n"
        f"**Step 2 — Value after final 2 years:**\n"
        f"$A_5 = A_3(1 + i_2)^2 = {_fmt_r(a1)}(1 + 0,09)^2 = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin42",
        subskill="42_compound_interest_timeline_single_rate_change",
        title="Compound Interest: Single Interest Rate Change",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Calculate the accumulated value at the end of the first rate period, then compound that balance at the second rate.",
            "tier_2": f"After 3 years at 7%: $A = {p}(1,07)^3 = {_fmt_r(a1)}$.",
            "tier_3": f"Compound {_fmt_r(a1)} at 9% for 2 years: {_fmt_r(a1)} * (1,09)^2 = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates balance after first 3 years", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Applies new 9% interest rate to balance", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Compounds over remaining 2 years", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct final balance {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["averaged_the_two_interest_rates"],
    )


def build_43_compound_interest_tripling_investment_estimation(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    r_pct = rng.choice([8.0, 10.0, 12.0])
    i = r_pct / 100.0
    # Solve (1 + i)^n >= 3
    n = math.ceil(math.log(3) / math.log(1 + i))
    ans = f"{n} years"

    prompt = (
        f"{name} invests a lump sum at {_fmt_dec(r_pct, 1)}% per annum compound interest. "
        f"Determine the minimum number of full years it will take for the investment to TRIPLE in value."
    )
    worked = (
        f"**Concept:** For an investment to triple, $(1 + i)^n \\ge 3$.\n\n"
        f"With $i = {_fmt_dec(i, 4)}$:\n"
        f"- At $n = {n-1}$ years: $(1 + {_fmt_dec(i, 4)})^{{{n-1}}} \\approx {_fmt_dec((1+i)**(n-1), 3)} < 3$\n"
        f"- At $n = {n}$ years: $(1 + {_fmt_dec(i, 4)})^{{{n}}} \\approx {_fmt_dec((1+i)**n, 3)} \\ge 3$\n\n"
        f"Therefore, it will take at least **{ans}** to triple."
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin43",
        subskill="43_compound_interest_tripling_investment_estimation",
        title="Compound Interest: Minimum Years to Triple Investment",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Test integer values of $n$ in $(1 + i)^n$ until the growth factor reaches or exceeds 3.",
            "tier_2": f"Evaluate ({_fmt_dec(1 + i, 4)})^n for successive values of $n$.",
            "tier_3": f"The smallest integer year where the factor exceeds 3 is {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Sets up inequality $(1 + i)^n \\ge 3$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Tests values of $n$ accurately", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct minimum full years: {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["rounded_down_leaving_investment_short_of_tripling"],
    )


def build_44_hire_purchase_residual_balloon_comparison(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(10, 25) * 1000
    dep_pct = 10
    deposit = cash_price * 0.10
    p_loan = cash_price - deposit
    r_pct = 11.0
    years = 2
    a_hp = deposit + p_loan * (1 + 0.11 * years)
    discount_pct = 5.0
    cash_discounted = cash_price * (1 - 0.05)
    saving = a_hp - cash_discounted
    ans = _fmt_r(saving)

    prompt = (
        f"{name} wants to buy a {asset} priced at {_fmt_r(cash_price)}. "
        f"Option A: Pay cash and receive an immediate 5% discount.\n"
        f"Option B: Buy on hire purchase with a 10% deposit and the balance financed over 2 years at 11% p.a. simple interest.\n\n"
        f"How much money does {name} save by choosing Option A (cash discount) over Option B (hire purchase)?"
    )
    worked = (
        f"**Option A (Discounted Cash):**\n"
        f"$\\text{{Cash}} = {_fmt_r(cash_price)} \\times 0,95 = {_fmt_r(cash_discounted)}$\n\n"
        f"**Option B (Hire Purchase):**\n"
        f"Deposit: {_fmt_r(deposit)}; Loan: {_fmt_r(p_loan)}\n"
        f"Total Repaid: $A = {p_loan}(1 + 0,11 \\times 2) = {_fmt_r(p_loan * 1.22)}$\n"
        f"Total HP Cost: ${_fmt_r(deposit)} + {_fmt_r(p_loan * 1.22)} = {_fmt_r(a_hp)}$\n\n"
        f"**Savings:** ${_fmt_r(a_hp)} - {_fmt_r(cash_discounted)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin44",
        subskill="44_hire_purchase_residual_balloon_comparison",
        title="Financial Decision: Cash Discount vs Hire Purchase",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Calculate the total cost of each option separately, then find the difference.",
            "tier_2": f"Option A = {_fmt_r(cash_discounted)}; Option B = {_fmt_r(a_hp)}.",
            "tier_3": f"Subtract Option A from Option B: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates discounted cash price (Option A)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Calculates total hire purchase cost (Option B)", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Subtracts the two total costs", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct savings {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["forgot_to_include_deposit_in_hp_total_cost"],
    )


def build_45_inflation_salary_adjustment_parity(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    salary = rng.randint(18, 45) * 1000
    inf_pct = rng.choice([5.5, 6.0, 6.5, 7.0])
    years = rng.randint(2, 4)
    i = inf_pct / 100.0
    new_sal = salary * ((1.0 + i) ** years)
    ans = _fmt_r(new_sal)

    prompt = (
        f"{name} currently earns a monthly salary of {_fmt_r(salary)}. "
        f"To maintain the same real standard of living against inflation averaging {_fmt_dec(inf_pct, 1)}% per annum, "
        f"what should {name}'s monthly salary be in {years} years' time?"
    )
    worked = (
        f"**Concept:** Salaries must compound with inflation to preserve purchasing power: $A = P(1 + i)^n$\n\n"
        f"**Substitution:** $A = {_fmt_r(salary)}(1 + {_fmt_dec(i, 4)})^{{{years}}} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin45",
        subskill="45_inflation_salary_adjustment_parity",
        title="Inflation: Cost-of-Living Salary Parity",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Apply the compound growth formula to increase the salary at the inflation rate.",
            "tier_2": f"Use $A = {salary}(1 + {_fmt_dec(i, 4)})^{years}$.",
            "tier_3": f"Result is {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Applies compound growth model $A = P(1+i)^n$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes salary, inflation rate, and years", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct adjusted salary {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["used_simple_interest_for_cost_of_living_adjustments"],
    )


def build_46_simple_vs_compound_effective_rate_one_year(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(10, 50) * 1000
    r_pct = rng.choice([7.0, 8.5, 9.0, 10.5])
    i = r_pct / 100.0
    ans = "R 0,00"

    prompt = (
        f"{name} compares investing {_fmt_r(p)} for exactly ONE year ($n = 1$) at {_fmt_dec(r_pct, 1)}% p.a. simple interest "
        f"versus {_fmt_dec(r_pct, 1)}% p.a. compound interest (compounded annually). "
        f"What is the difference in interest earned between the two options at the end of the first year?"
    )
    worked = (
        f"- Simple interest after 1 year: $A = P(1 + i(1)) = P(1 + i)$\n"
        f"- Compound interest after 1 year: $A = P(1 + i)^1 = P(1 + i)$\n\n"
        f"Because $P(1 + i) = P(1 + i)$, both methods yield the exact same amount for $n = 1$.\n"
        f"Therefore, the difference is **{ans}**."
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin46",
        subskill="46_simple_vs_compound_effective_rate_one_year",
        title="Simple vs Compound Interest: Identity at Year 1 ($n = 1$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=2,
        hints={
            "tier_1": "Recall that simple and compound interest give identical results over exactly one annual period.",
            "tier_2": "$P(1 + i \\cdot 1) = P(1 + i)^1$.",
            "tier_3": "The difference between identical values is R 0,00.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Shows simple and compound interest are equal for n = 1", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "States difference is R 0,00", "marks": 1, "editable": True},
        ],
        misconception_tags=["assumed_compound_interest_is_greater_in_year_one"],
    )


def build_47_compound_interest_interest_rate_comparison_fixed_p(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(15, 30) * 1000
    years = 4
    r_a = 8.5
    r_b = 9.2
    a_a = p * ((1 + r_a / 100.0) ** years)
    a_b = p * ((1 + r_b / 100.0) ** years)
    diff = a_b - a_a
    ans = _fmt_r(diff)

    prompt = (
        f"{name} considers two competing investment accounts for a principal of {_fmt_r(p)} over {years} years:\n"
        f"- Bank A offers {_fmt_dec(r_a, 1)}% p.a. compound interest.\n"
        f"- Bank B offers {_fmt_dec(r_b, 1)}% p.a. compound interest.\n\n"
        f"Calculate how much extra interest Bank B pays over Bank A at the end of {years} years."
    )
    worked = (
        f"**Bank A:** $A_A = {p}(1 + {_fmt_dec(r_a/100, 3)})^{{{years}}} = {_fmt_r(a_a)}$\n\n"
        f"**Bank B:** $A_B = {p}(1 + {_fmt_dec(r_b/100, 3)})^{{{years}}} = {_fmt_r(a_b)}$\n\n"
        f"**Extra interest from Bank B:** ${_fmt_r(a_b)} - {_fmt_r(a_a)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin47",
        subskill="47_compound_interest_interest_rate_comparison_fixed_p",
        title="Compound Interest: Comparing Competing Bank Rates",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Calculate the accumulated value at both rates, then subtract.",
            "tier_2": f"Bank A = {_fmt_r(a_a)}; Bank B = {_fmt_r(a_b)}.",
            "tier_3": f"Subtract: {_fmt_r(a_b)} - {_fmt_r(a_a)} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates Bank A total", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Calculates Bank B total", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Subtracts Bank A from Bank B", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct difference {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["subtracted_interest_rates_and_multiplied_by_p_linearly"],
    )


def build_48_hire_purchase_trade_in_allowance(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(8, 22) * 1000
    trade_in = rng.randint(12, 35) * 100
    dep_cash = rng.randint(8, 20) * 100
    total_deposit = trade_in + dep_cash
    p_loan = cash_price - total_deposit
    r_pct = 12.0
    years = 2
    a_repay = p_loan * (1 + 0.12 * years)
    monthly = a_repay / 24
    ans = _fmt_r(monthly)

    prompt = (
        f"{name} buys a new {asset} costing {_fmt_r(cash_price)} on hire purchase. "
        f"The store accepts an old appliance trade-in valued at {_fmt_r(trade_in)}, and {name} pays a further {_fmt_r(dep_cash)} in cash as deposit. "
        f"The remaining loan balance is financed over 24 months at 12% p.a. simple interest. "
        f"Calculate the monthly instalment."
    )
    worked = (
        f"**Step 1 — Total deposit credited:** ${_fmt_r(trade_in)} + {_fmt_r(dep_cash)} = {_fmt_r(total_deposit)}$\n\n"
        f"**Step 2 — Financed loan balance:** $P = {_fmt_r(cash_price)} - {_fmt_r(total_deposit)} = {_fmt_r(p_loan)}$\n\n"
        f"**Step 3 — Total repayments:** $A = {p_loan}(1 + 0,12 \\times 2) = {_fmt_r(a_repay)}$\n\n"
        f"**Step 4 — Monthly instalment:** $\\frac{{{_fmt_r(a_repay)}}}{{24}} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin48",
        subskill="48_hire_purchase_trade_in_allowance",
        title="Hire Purchase: Trade-In Allowance Credited to Deposit",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Add the trade-in allowance to the cash deposit to find the total deposit deducted.",
            "tier_2": f"Total deposit = {_fmt_r(total_deposit)}; Loan $P = {_fmt_r(p_loan)}$.",
            "tier_3": f"Repayment $A = {_fmt_r(a_repay)}$; divide by 24 = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates total deposit (trade-in + cash)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Deducts total deposit to find principal loan $P$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Calculates total loan repayment $A = P(1+in)$", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct monthly instalment {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["subtracted_trade_in_from_monthly_instalment_instead_of_deposit"],
    )


def build_49_foreign_exchange_percentage_change_in_rate(rng: random.Random) -> Dict[str, Any]:
    curr_name, sym = ("US Dollar (USD)", "$")
    old_rate = 18.00
    new_rate = rng.choice([19.26, 19.44, 19.80, 20.16])
    pct_change = round(((new_rate - old_rate) / old_rate) * 100, 1)
    ans = f"{_fmt_dec(pct_change, 1)}%"

    prompt = (
        f"At the beginning of the year, the exchange rate was {sym} 1 = R {_fmt_dec(old_rate, 2)}. "
        f"By the end of the year, the rate was {sym} 1 = R {_fmt_dec(new_rate, 2)}. "
        f"Calculate the percentage increase in the Rand cost of purchasing one {curr_name}."
    )
    worked = (
        f"$$\\text{{Percentage Increase}} = \\frac{{\\text{{New Rate}} - \\text{{Old Rate}}}}{{\\text{{Old Rate}}}} \\times 100$$\n\n"
        f"$$\\text{{Percentage Increase}} = \\frac{{{_fmt_dec(new_rate, 2)} - {_fmt_dec(old_rate, 2)}}}{{{_fmt_dec(old_rate, 2)}}} \\times 100 = \\frac{{{_fmt_dec(new_rate - old_rate, 2)}}}{{{_fmt_dec(old_rate, 2)}}} \\times 100 = \\mathbf{{{ans}}}$$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin49",
        subskill="49_foreign_exchange_percentage_change_in_rate",
        title="Foreign Exchange: Percentage Rate Fluctuation",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Use the percentage change formula: $\\frac{\\text{Change}}{\\text{Original}} \\times 100$.",
            "tier_2": f"Change = {_fmt_dec(new_rate - old_rate, 2)}; Original = {_fmt_dec(old_rate, 2)}.",
            "tier_3": f"Divide change by original and multiply by 100: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates difference between rates", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Divides by original baseline rate", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct percentage change {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["divided_by_new_rate_instead_of_old_rate"],
    )


def build_50_finance_growth_integrated_case_study(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = 15000
    dep_pct = 10
    deposit = 1500
    p_loan = 13500
    r_hp = 12.0
    years = 2
    a_hp = p_loan * (1 + 0.12 * years)
    total_hp = deposit + a_hp
    hp_extra = total_hp - cash_price
    ans = _fmt_r(hp_extra)

    prompt = (
        f"{name} needs a new {asset} costing R 15 000 cash. "
        f"Under a hire purchase agreement, {name} pays a 10% deposit (R 1 500) and finances the remaining R 13 500 over 24 months at 12% p.a. simple interest. "
        f"Calculate the total finance charges (extra interest cost) incurred by choosing hire purchase rather than paying the full cash price upfront."
    )
    worked = (
        f"**1. Deposit:** R 1 500\n\n"
        f"**2. Loan balance:** $P = \\text{{R 15 000}} - \\text{{R 1 500}} = \\text{{R 13 500}}$\n\n"
        f"**3. Simple interest on loan:**\n"
        f"$I = P \\times i \\times n = 13500 \\times 0,12 \\times 2 = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin50",
        subskill="50_finance_growth_integrated_case_study",
        title="Integrated Financial Case Study: Evaluating Credit Cost",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "The extra finance charge is the interest accrued on the financed loan amount.",
            "tier_2": "Calculate $I = P \\cdot i \\cdot n$ on the R 13 500 loan balance.",
            "tier_3": f"13500 * 0,12 * 2 = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates financed principal balance (R 13 500)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Applies $I = P \\cdot i \\cdot n$ with $i = 0,12$ and $n = 2$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct total finance charge {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["charged_interest_on_initial_15000_without_deducting_deposit"],
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_compound_interest_stepwise_table_derivation": build_26_compound_interest_stepwise_table_derivation,
    "27_compound_interest_graph_linear_vs_exponential": build_27_compound_interest_graph_linear_vs_exponential,
    "28_simple_interest_days_conversion": build_28_simple_interest_days_conversion,
    "29_compound_interest_fractional_years": build_29_compound_interest_fractional_years,
    "30_hire_purchase_solve_for_deposit_percentage": build_30_hire_purchase_solve_for_deposit_percentage,
    "31_hire_purchase_reverse_cash_price": build_31_hire_purchase_reverse_cash_price,
    "32_hire_purchase_total_interest_rate_reverse": build_32_hire_purchase_total_interest_rate_reverse,
    "33_hire_purchase_loan_term_in_months": build_33_hire_purchase_loan_term_in_months,
    "34_inflation_average_annual_rate_calculation": build_34_inflation_average_annual_rate_calculation,
    "35_inflation_purchasing_power_erosion": build_35_inflation_purchasing_power_erosion,
    "36_population_percentage_growth_rate_reverse": build_36_population_percentage_growth_rate_reverse,
    "37_foreign_exchange_bank_buying_vs_selling_margin": build_37_foreign_exchange_bank_buying_vs_selling_margin,
    "38_foreign_exchange_commission_fee_deduction": build_38_foreign_exchange_commission_fee_deduction,
    "39_foreign_exchange_multi_currency_trip_conversion": build_39_foreign_exchange_multi_currency_trip_conversion,
    "40_foreign_exchange_currency_depreciation_impact": build_40_foreign_exchange_currency_depreciation_impact,
    "41_simple_interest_multiple_deposits_timeline": build_41_simple_interest_multiple_deposits_timeline,
    "42_compound_interest_timeline_single_rate_change": build_42_compound_interest_timeline_single_rate_change,
    "43_compound_interest_tripling_investment_estimation": build_43_compound_interest_tripling_investment_estimation,
    "44_hire_purchase_residual_balloon_comparison": build_44_hire_purchase_residual_balloon_comparison,
    "45_inflation_salary_adjustment_parity": build_45_inflation_salary_adjustment_parity,
    "46_simple_vs_compound_effective_rate_one_year": build_46_simple_vs_compound_effective_rate_one_year,
    "47_compound_interest_interest_rate_comparison_fixed_p": build_47_compound_interest_interest_rate_comparison_fixed_p,
    "48_hire_purchase_trade_in_allowance": build_48_hire_purchase_trade_in_allowance,
    "49_foreign_exchange_percentage_change_in_rate": build_49_foreign_exchange_percentage_change_in_rate,
    "50_finance_growth_integrated_case_study": build_50_finance_growth_integrated_case_study,
}
