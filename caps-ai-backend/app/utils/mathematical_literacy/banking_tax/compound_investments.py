"""Compound Interest & Investment Growth Subskills (Subskills 36 to 44).

36. bank_int_compound_annual_growth_formula
37. bank_int_compound_year_by_year_stepwise_table
38. bank_int_simple_vs_compound_numeric_comparison
39. bank_int_compound_interest_earned_subtraction
40. bank_int_fixed_deposit_tier_rate_selection
41. bank_int_inflation_purchasing_power_erosion
42. bank_int_rule_of_72_doubling_time
43. bank_int_compound_semi_annual_compounding
44. bank_int_endowment_policy_maturity_lump_sum
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_BANKS, SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_bank_int_compound_annual_growth_formula(r: random.Random) -> Dict[str, Any]:
    """Calculate compound interest future value using annual formula: A = P(1 + i)^n."""
    name = r.choice(SA_NAMES)
    principal = r.choice([5000, 8000, 10000, 12000, 15000, 20000])
    rate = r.choice([5.0, 6.0, 7.5, 8.0, 10.0])
    years = r.choice([2, 3, 4])

    acc_val = round(principal * ((1 + rate / 100) ** years), 2)
    ans_str = _fmt_curr(acc_val)

    prompt = (
        f"{name} invests {_fmt_curr(principal)} in a fixed deposit account earning "
        f"{_fmt(rate)}% compound interest per annum, compounded annually, for {years} years.\n\n"
        f"Calculate the **total accumulated amount (A)** in the account at the end of {years} years.\n"
        f"Use the formula: $$A = P(1 + i)^n$$"
    )
    sol = (
        f"Step 1: Identify given variables:\n"
        f"• Principal ($P$) = {_fmt_curr(principal)}\n"
        f"• Annual interest rate ($i$) = {_fmt(rate)}% = {rate / 100}\n"
        f"• Term ($n$) = {years} years\n\n"
        f"Step 2: Method setup using compound interest formula:\n"
        f"• $A = P(1 + i)^n = {principal} \\times (1 + {rate / 100})^{{{years}}}$\n"
        f"• $A = {principal} \\times ({1 + rate / 100:.4f})^{{{years}}}$ "
        f"✓ [1 Mark: Method – applying formula $A = P(1 + i)^n$ with correct substitution]\n\n"
        f"Step 3: Calculate accumulated value:\n"
        f"$$A = {ans_str}$$\n"
        f"✓ [1 Mark: Accuracy – correct compound value in Rands]"
    )
    rubric = [
        f"1 Mark: Method – substituting {principal} × (1 + {rate/100})^{years}",
        f"1 Mark: Accuracy – correct accumulated amount {ans_str}"
    ]
    hints = {
        "tier_1": f"Calculate (1 + {rate/100}) = {1 + rate/100:.2f}.",
        "tier_2": f"Raise {1 + rate/100:.2f} to the power of {years}, then multiply by {_fmt_curr(principal)}.",
        "tier_3": f"{principal} × ({1 + rate/100})^{years} = {acc_val:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_compound_annual_growth_formula", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_compound_year_by_year_stepwise_table(r: random.Random) -> Dict[str, Any]:
    """Calculate compound interest manually year-by-year showing intermediate principal and interest."""
    name = r.choice(SA_NAMES)
    p0 = r.choice([4000, 5000, 6000, 8000, 10000])
    rate = r.choice([5.0, 8.0, 10.0])

    # Year 1
    int_yr1 = round(p0 * (rate / 100), 2)
    p1 = round(p0 + int_yr1, 2)

    # Year 2
    int_yr2 = round(p1 * (rate / 100), 2)
    p2 = round(p1 + int_yr2, 2)

    ans_str = _fmt_curr(p2)

    prompt = (
        f"{name} invests {_fmt_curr(p0)} at {_fmt(rate)}% compound interest per annum for 2 years.\n\n"
        f"Below is a year-by-year calculation table showing the growth of the investment:\n\n"
        f"| Year | Starting Balance | Interest Earned ({_fmt(rate)}%) | Ending Balance |\n"
        f"| :---: | :---: | :---: | :---: |\n"
        f"| Year 1 | {_fmt_curr(p0)} | {_fmt_curr(int_yr1)} | {_fmt_curr(p1)} |\n"
        f"| Year 2 | {_fmt_curr(p1)} | **[ Interest ]** | **[ Final Balance ]** |\n\n"
        f"Calculate the **Final Ending Balance** at the end of Year 2."
    )
    sol = (
        f"Step 1: Understand year-by-year compounding:\n"
        f"• For Year 2, interest is calculated on the NEW balance from the end of Year 1 ({_fmt_curr(p1)}).\n\n"
        f"Step 2: Method setup for Year 2:\n"
        f"• Year 2 Interest = {_fmt_curr(p1)} × ({rate}/100) = {_fmt_curr(int_yr2)}\n"
        f"• Ending Balance Year 2 = {_fmt_curr(p1)} + {_fmt_curr(int_yr2)} "
        f"✓ [1 Mark: Method – applying {_fmt(rate)}% to Year 1 closing balance and summing]\n\n"
        f"Step 3: Calculate final balance:\n"
        f"Ending Balance Year 2 = {ans_str} ✓ [1 Mark: Accuracy – correct year 2 ending balance in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating Year 2 interest on {_fmt_curr(p1)} and adding to balance",
        f"1 Mark: Accuracy – correct balance {ans_str}"
    ]
    hints = {
        "tier_1": f"Do not use {_fmt_curr(p0)} for Year 2! In compound interest, use the new balance of {_fmt_curr(p1)}.",
        "tier_2": f"Find {_fmt(rate)}% of {_fmt_curr(p1)}, then add it to {_fmt_curr(p1)}.",
        "tier_3": f"{p1:.2f} + ({p1:.2f} × {rate/100}) = {p2:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_compound_year_by_year_stepwise_table", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_simple_vs_compound_numeric_comparison(r: random.Random) -> Dict[str, Any]:
    """Compare the numerical difference in total return between simple and compound interest."""
    name = r.choice(SA_NAMES)
    principal = r.choice([5000, 10000, 15000, 20000])
    rate = r.choice([8.0, 10.0, 12.0])
    years = 3

    # Simple interest
    simple_int = round(principal * (rate / 100) * years, 2)
    simple_tot = round(principal + simple_int, 2)

    # Compound interest
    compound_tot = round(principal * ((1 + rate / 100) ** years), 2)
    compound_int = round(compound_tot - principal, 2)

    diff = round(compound_tot - simple_tot, 2)
    ans_str = _fmt_curr(diff)

    prompt = (
        f"{name} compares two investment options for a principal of {_fmt_curr(principal)} over 3 years:\n"
        f"• **Option A (Simple Interest)**: {_fmt(rate)}% simple interest per annum\n"
        f"• **Option B (Compound Interest)**: {_fmt(rate)}% compound interest per annum, compounded annually\n\n"
        f"Calculate **how much more money** {name} will have earned with Option B (Compound) "
        f"compared to Option A (Simple) after 3 years."
    )
    sol = (
        f"Step 1: Calculate future value for each option:\n"
        f"• **Option A (Simple Interest)**:\n"
        f"  $A_S = P(1 + i \\times n) = {principal} \\times (1 + {rate / 100} \\times 3) = {_fmt_curr(simple_tot)}$\n"
        f"• **Option B (Compound Interest)**:\n"
        f"  $A_C = P(1 + i)^n = {principal} \\times (1 + {rate / 100})^3 = {_fmt_curr(compound_tot)}$\n\n"
        f"Step 2: Method setup – calculate the difference:\n"
        f"• Difference = $A_C - A_S$\n"
        f"• Difference = {_fmt_curr(compound_tot)} - {_fmt_curr(simple_tot)} "
        f"✓ [1 Mark: Method – evaluating both simple and compound totals and setting up difference]\n\n"
        f"Step 3: Calculate difference:\n"
        f"Difference = {ans_str} ✓ [1 Mark: Accuracy – correct difference in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating simple total ({_fmt_curr(simple_tot)}) and compound total ({_fmt_curr(compound_tot)})",
        f"1 Mark: Accuracy – correct difference {ans_str}"
    ]
    hints = {
        "tier_1": f"Simple total = {principal} × (1 + {rate/100} × 3) = {_fmt_curr(simple_tot)}.",
        "tier_2": f"Compound total = {principal} × (1 + {rate/100})^3 = {_fmt_curr(compound_tot)}.",
        "tier_3": f"{compound_tot:.2f} - {simple_tot:.2f} = {diff:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_simple_vs_compound_numeric_comparison", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_compound_interest_earned_subtraction(r: random.Random) -> Dict[str, Any]:
    """Calculate the compound interest portion only (I = A - P)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([6000, 8000, 10000, 12000, 15000])
    rate = r.choice([6.0, 7.0, 8.0, 9.0, 10.0])
    years = r.choice([2, 3, 4])

    acc_val = round(principal * ((1 + rate / 100) ** years), 2)
    interest_only = round(acc_val - principal, 2)
    ans_str = _fmt_curr(interest_only)

    prompt = (
        f"{name} invested {_fmt_curr(principal)} in a fixed deposit for {years} years at "
        f"{_fmt(rate)}% compound interest per annum. At maturity, the investment grew to {_fmt_curr(acc_val)}.\n\n"
        f"Calculate the **total compound interest earned** (in Rands) on this investment.\n"
        f"Use the formula: $$I = A - P$$"
    )
    sol = (
        f"Step 1: Identify accumulated total ($A$) and original principal ($P$):\n"
        f"• Accumulated total ($A$) = {_fmt_curr(acc_val)}\n"
        f"• Principal ($P$) = {_fmt_curr(principal)}\n\n"
        f"Step 2: Method setup – subtract principal from accumulated value:\n"
        f"• Interest = $A - P$\n"
        f"• Interest = {_fmt_curr(acc_val)} - {_fmt_curr(principal)} "
        f"✓ [1 Mark: Method – subtracting principal from final maturity amount]\n\n"
        f"Step 3: Calculate interest earned:\n"
        f"Interest = {ans_str} ✓ [1 Mark: Accuracy – correct compound interest in Rands]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {_fmt_curr(principal)} from {_fmt_curr(acc_val)}",
        f"1 Mark: Accuracy – correct interest {ans_str}"
    ]
    hints = {
        "tier_1": f"Subtract the money originally deposited ({_fmt_curr(principal)}) from the final amount ({_fmt_curr(acc_val)}).",
        "tier_2": f"Calculate: {acc_val:.2f} - {principal:.2f}.",
        "tier_3": f"{acc_val:.2f} - {principal:.2f} = {interest_only:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_compound_interest_earned_subtraction", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_fixed_deposit_tier_rate_selection(r: random.Random) -> Dict[str, Any]:
    """Select the correct interest rate from a fixed deposit rate table and calculate 1-year annual interest."""
    name = r.choice(SA_NAMES)
    deposit = r.choice([15000, 25000, 45000, 60000, 85000, 120000])

    if deposit < 25000:
        rate = 7.25
        tier_desc = "R 10 000 – R 24 999"
    elif deposit < 50000:
        rate = 8.10
        tier_desc = "R 25 000 – R 49 999"
    elif deposit < 100000:
        rate = 8.75
        tier_desc = "R 50 000 – R 99 999"
    else:
        rate = 9.20
        tier_desc = "R 100 000+"

    interest_1yr = round(deposit * (rate / 100), 2)
    ans_str = _fmt_curr(interest_1yr)

    prompt = (
        f"{name} visits a bank to open a 12-month fixed deposit with a lump-sum amount of {_fmt_curr(deposit)}.\n"
        f"The bank publishes the following 12-month fixed deposit interest rate tier table:\n\n"
        f"| Deposit Range | Annual Interest Rate |\n"
        f"| :--- | :---: |\n"
        f"| R 10 000 – R 24 999 | 7,25% |\n"
        f"| R 25 000 – R 49 999 | 8,10% |\n"
        f"| R 50 000 – R 99 999 | 8,75% |\n"
        f"| R 100 000 and above | 9,20% |\n\n"
        f"1. Identify the applicable interest rate tier for {name}'s deposit of {_fmt_curr(deposit)}.\n"
        f"2. Calculate the **total interest earned** at the end of the 12-month period."
    )
    sol = (
        f"Step 1: Locate {name}'s deposit amount in the rate tier table:\n"
        f"• {_fmt_curr(deposit)} falls in the tier \"{tier_desc}\", qualifying for {_fmt(rate)}% per annum.\n\n"
        f"Step 2: Method setup – calculate 12-month interest:\n"
        f"• Interest = ({rate} ÷ 100) × {_fmt_curr(deposit)}\n"
        f"• Interest = {rate / 100} × {deposit} "
        f"✓ [1 Mark: Method – selecting {_fmt(rate)}% from table and multiplying by deposit]\n\n"
        f"Step 3: Calculate interest earned:\n"
        f"Interest = {ans_str} ✓ [1 Mark: Accuracy – correct interest in Rands]"
    )
    rubric = [
        f"1 Mark: Method – identifying {_fmt(rate)}% from tier table and multiplying by {_fmt_curr(deposit)}",
        f"1 Mark: Accuracy – correct interest {ans_str}"
    ]
    hints = {
        "tier_1": f"Look at the table to find which row contains {_fmt_curr(deposit)}.",
        "tier_2": f"The rate is {_fmt(rate)}%. Multiply {_fmt_curr(deposit)} by {rate / 100}.",
        "tier_3": f"{deposit} × {rate/100:.4f} = {interest_1yr:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_fixed_deposit_tier_rate_selection", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_inflation_purchasing_power_erosion(r: random.Random) -> Dict[str, Any]:
    """Calculate the real interest rate after subtracting South African CPI inflation rate."""
    name = r.choice(SA_NAMES)
    nominal_rate = r.choice([7.0, 7.5, 8.0, 8.5, 9.0])
    cpi_inflation = r.choice([4.5, 5.0, 5.2, 5.5, 6.0])

    real_rate = round(nominal_rate - cpi_inflation, 2)
    ans_str = f"{_fmt(real_rate)}%"

    prompt = (
        f"{name}'s investment portfolio earns a nominal interest rate of {_fmt(nominal_rate)}% per annum. "
        f"During the same period, Statistics South Africa (Stats SA) reports an annual Consumer Price Index (CPI) "
        f"inflation rate of {_fmt(cpi_inflation)}%.\n\n"
        f"Calculate the **real annual interest rate** earned by {name}'s portfolio after accounting for inflation.\n"
        f"Use the formula: $$\\text{{Real Rate}} = \\text{{Nominal Interest Rate}} - \\text{{Inflation Rate}}$$"
    )
    sol = (
        f"Step 1: Understand real rate vs nominal rate:\n"
        f"• Nominal interest rate = {_fmt(nominal_rate)}%\n"
        f"• Inflation rate (CPI) = {_fmt(cpi_inflation)}%\n"
        f"• Inflation erodes the purchasing power of money over time.\n\n"
        f"Step 2: Method setup – subtract inflation from nominal return:\n"
        f"• Real Rate = Nominal Rate - Inflation Rate\n"
        f"• Real Rate = {_fmt(nominal_rate)}% - {_fmt(cpi_inflation)}% "
        f"✓ [1 Mark: Method – subtracting CPI inflation rate from nominal interest rate]\n\n"
        f"Step 3: Calculate real rate:\n"
        f"Real Rate = {ans_str} ✓ [1 Mark: Accuracy – correct real interest rate percentage]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {_fmt(cpi_inflation)}% from {_fmt(nominal_rate)}%",
        f"1 Mark: Accuracy – correct real rate {ans_str}"
    ]
    hints = {
        "tier_1": "Subtract the inflation percentage from the investment interest rate.",
        "tier_2": f"Calculate: {_fmt(nominal_rate)} - {_fmt(cpi_inflation)}.",
        "tier_3": f"{nominal_rate:.2f} - {cpi_inflation:.2f} = {real_rate:.2f}%, giving {ans_str}."
    }
    return _make_q("bank_int_inflation_purchasing_power_erosion", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_rule_of_72_doubling_time(r: random.Random) -> Dict[str, Any]:
    """Estimate the doubling time of an investment using the Rule of 72."""
    name = r.choice(SA_NAMES)
    rate = r.choice([6.0, 8.0, 9.0, 12.0])
    doubling_years = round(72 / rate, 1)
    if doubling_years.is_integer():
        ans_str = f"{int(doubling_years)} years"
    else:
        ans_str = f"{_fmt(doubling_years)} years"

    prompt = (
        f"{name} invests money in a compound growth unit trust yielding an annual return of {_fmt(rate)}%.\n\n"
        f"Using the financial **Rule of 72**, estimate how many **years** it will take for {name}'s investment to double in value.\n"
        f"Use the formula: $$\\text{{Years to Double}} \\approx \\frac{{72}}{{\\text{{Interest Rate (\\%)}}}}$$"
    )
    sol = (
        f"Step 1: Identify formula and variable:\n"
        f"• Annual interest rate ($r$) = {_fmt(rate)}%\n"
        f"• Rule of 72 constant = 72\n\n"
        f"Step 2: Method setup – divide 72 by the percentage rate:\n"
        f"• $\\text{{Years to Double}} = \\frac{{72}}{{{rate}}}$ "
        f"✓ [1 Mark: Method – dividing 72 by the annual percentage rate {_fmt(rate)}]\n\n"
        f"Step 3: Calculate estimated doubling duration:\n"
        f"Years to Double = {ans_str} ✓ [1 Mark: Accuracy – correct doubling years]"
    )
    rubric = [
        f"1 Mark: Method – dividing 72 by {rate}",
        f"1 Mark: Accuracy – correct years {ans_str}"
    ]
    hints = {
        "tier_1": "In the Rule of 72, divide 72 by the interest rate number directly (without converting to decimal).",
        "tier_2": f"Calculate: 72 ÷ {rate}.",
        "tier_3": f"72 ÷ {rate} = {doubling_years}, so the answer is {ans_str}."
    }
    return _make_q("bank_int_rule_of_72_doubling_time", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_compound_semi_annual_compounding(r: random.Random) -> Dict[str, Any]:
    """Calculate compound interest future value with semi-annual compounding (compounded twice a year)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([5000, 10000, 12000, 15000])
    annual_rate = r.choice([8.0, 10.0, 12.0])
    years = 2

    # Semi-annual: rate per period = annual_rate / 2, total periods = years * 2
    rate_per_period = (annual_rate / 2) / 100
    periods = years * 2  # 4 periods

    future_val = round(principal * ((1 + rate_per_period) ** periods), 2)
    ans_str = _fmt_curr(future_val)

    prompt = (
        f"{name} invests {_fmt_curr(principal)} in a fixed notice account at an annual interest rate of {_fmt(annual_rate)}% "
        f"compounded **semi-annually (twice a year)** for {years} years.\n\n"
        f"1. Rate per half-year period: $i = \\frac{{{_fmt(annual_rate)}\\%}}{{2}} = {_fmt(annual_rate / 2)}\\% = {rate_per_period}$\n"
        f"2. Total compounding periods: $n = {years} \\times 2 = {periods}$\n\n"
        f"Calculate the **total accumulated future value** at the end of {years} years using: $$A = P(1 + i)^n$$"
    )
    sol = (
        f"Step 1: Identify periodic rate and number of compounding periods:\n"
        f"• Semi-annual rate ($i$) = {annual_rate}% ÷ 2 = {annual_rate / 2}% = {rate_per_period}\n"
        f"• Total periods ($n$) = {years} years × 2 = {periods} periods\n\n"
        f"Step 2: Method setup using compound formula:\n"
        f"• $A = P(1 + i)^n = {principal} \\times (1 + {rate_per_period})^{{{periods}}}$\n"
        f"• $A = {principal} \\times ({1 + rate_per_period:.4f})^{{{periods}}}$ "
        f"✓ [1 Mark: Method – applying semi-annual rate and {periods} compounding periods]\n\n"
        f"Step 3: Calculate accumulated future value:\n"
        f"$$A = {ans_str}$$\n"
        f"✓ [1 Mark: Accuracy – correct semi-annually compounded amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – substituting {principal} × (1 + {rate_per_period})^{periods}",
        f"1 Mark: Accuracy – correct accumulated amount {ans_str}"
    ]
    hints = {
        "tier_1": f"Divide the annual rate by 2: {annual_rate}% / 2 = {annual_rate / 2}%.",
        "tier_2": f"Multiply the years by 2: {years} × 2 = {periods} periods.",
        "tier_3": f"{principal} × (1 + {rate_per_period})^{periods} = {future_val:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_compound_semi_annual_compounding", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_endowment_policy_maturity_lump_sum(r: random.Random) -> Dict[str, Any]:
    """Calculate the maturity payout of a 5-year endowment savings policy with guaranteed return and terminal bonus."""
    name = r.choice(SA_NAMES)
    total_premiums = r.choice([30000, 45000, 60000, 75000])
    growth_pct = r.choice([25.0, 30.0, 35.0, 40.0])
    terminal_bonus = r.choice([2500, 3500, 5000])

    guaranteed_growth = round(total_premiums * (growth_pct / 100), 2)
    payout = round(total_premiums + guaranteed_growth + terminal_bonus, 2)
    ans_str = _fmt_curr(payout)

    prompt = (
        f"{name} completes a 5-year endowment savings policy. Over the 5 years, {name} contributed "
        f"a total of {_fmt_curr(total_premiums)} in premiums. At maturity, the policy contract pays:\n"
        f"• The original contributed premiums: {_fmt_curr(total_premiums)}\n"
        f"• Guaranteed growth bonus of {_fmt(growth_pct)}% on total premiums contributed\n"
        f"• A terminal loyalty bonus of {_fmt_curr(terminal_bonus)}\n\n"
        f"Calculate the **total maturity lump-sum payout** {name} will receive."
    )
    sol = (
        f"Step 1: Calculate the guaranteed growth bonus:\n"
        f"• Guaranteed Growth = {_fmt(growth_pct)}% of {_fmt_curr(total_premiums)} = ({growth_pct} ÷ 100) × {total_premiums} = {_fmt_curr(guaranteed_growth)}\n\n"
        f"Step 2: Method setup – sum all payout components:\n"
        f"• Total Payout = Premiums + Guaranteed Growth + Terminal Bonus\n"
        f"• Total Payout = {_fmt_curr(total_premiums)} + {_fmt_curr(guaranteed_growth)} + {_fmt_curr(terminal_bonus)} "
        f"✓ [1 Mark: Method – calculating growth bonus and summing all maturity benefits]\n\n"
        f"Step 3: Calculate total payout:\n"
        f"Total Payout = {ans_str} ✓ [1 Mark: Accuracy – correct maturity payout in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating growth bonus ({_fmt_curr(guaranteed_growth)}) and summing components",
        f"1 Mark: Accuracy – correct total payout {ans_str}"
    ]
    hints = {
        "tier_1": f"First find {_fmt(growth_pct)}% of {_fmt_curr(total_premiums)}.",
        "tier_2": f"Add the premiums ({_fmt_curr(total_premiums)}), the growth bonus, and the {_fmt_curr(terminal_bonus)} bonus together.",
        "tier_3": f"{total_premiums} + {guaranteed_growth:.2f} + {terminal_bonus} = {payout:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_endowment_policy_maturity_lump_sum", prompt, ans_str, sol, rubric, hints, 2, r=r)
