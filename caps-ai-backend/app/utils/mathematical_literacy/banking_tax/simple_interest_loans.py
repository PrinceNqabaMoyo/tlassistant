"""Simple Interest & Hire Purchase Loans Subskills (Subskills 26 to 35).

26. bank_int_simple_interest_investment_future_value
27. bank_int_simple_interest_months_fractional_year
28. bank_int_simple_interest_rate_determination
29. bank_int_simple_interest_term_duration_years
30. bank_int_hire_purchase_total_repayment_cost
31. bank_int_hire_purchase_total_interest_amount
32. bank_int_hire_purchase_cash_vs_credit_difference
33. bank_int_hire_purchase_effective_interest_rate
34. bank_int_personal_unsecured_loan_monthly_installment
35. bank_int_layby_zero_interest_cancellation_penalty
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_bank_int_simple_interest_investment_future_value(r: random.Random) -> Dict[str, Any]:
    """Calculate future value of an investment using simple interest: A = P(1 + i * n)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([3500, 5000, 7500, 10000, 12000, 15000, 20000])
    rate = r.choice([6.0, 7.5, 8.0, 9.5, 10.0, 12.0])
    years = r.choice([2, 3, 4, 5])

    interest = round(principal * (rate / 100) * years, 2)
    future_val = round(principal + interest, 2)
    ans_str = _fmt_curr(future_val)

    prompt = (
        f"{name} invests {_fmt_curr(principal)} in a fixed savings account earning "
        f"{_fmt(rate)}% simple interest per annum for a period of {years} years.\n\n"
        f"Calculate the **total accumulated future value (A)** of the investment at the end of {years} years.\n"
        f"Use the formula: $$A = P(1 + i \\times n)$$"
    )
    sol = (
        f"Step 1: Identify formula variables:\n"
        f"• Principal ($P$) = {_fmt_curr(principal)}\n"
        f"• Annual interest rate ($i$) = {_fmt(rate)}% = {rate / 100}\n"
        f"• Duration ($n$) = {years} years\n\n"
        f"Step 2: Method setup using simple interest formula:\n"
        f"• Interest = $P \\times i \\times n = {principal} \\times {rate / 100} \\times {years} = {_fmt_curr(interest)}$\n"
        f"• $A = P + \\text{{Interest}} = {_fmt_curr(principal)} + {_fmt_curr(interest)}$\n"
        f"✓ [1 Mark: Method – applying simple interest formula $A = P(1 + i \\times n)$]\n\n"
        f"Step 3: Calculate accumulated total:\n"
        f"$$A = {ans_str}$$\n"
        f"✓ [1 Mark: Accuracy – correct future value in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating {principal} × (1 + {rate/100} × {years})",
        f"1 Mark: Accuracy – correct future value {ans_str}"
    ]
    hints = {
        "tier_1": f"First calculate the interest: {principal} × ({rate}/100) × {years}.",
        "tier_2": f"Add the interest ({_fmt_curr(interest)}) to the principal ({_fmt_curr(principal)}).",
        "tier_3": f"{principal} + {interest:.2f} = {future_val:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_simple_interest_investment_future_value", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_simple_interest_months_fractional_year(r: random.Random) -> Dict[str, Any]:
    """Calculate simple interest earned over a fractional year (given in months)."""
    name = r.choice(SA_NAMES)
    principal = r.choice([2400, 3600, 4800, 6000, 7200, 9600])
    rate = r.choice([6.0, 8.0, 9.0, 10.0, 12.0])
    months = r.choice([3, 6, 8, 9, 10])

    interest = round(principal * (rate / 100) * (months / 12), 2)
    ans_str = _fmt_curr(interest)

    prompt = (
        f"{name} deposits {_fmt_curr(principal)} into a notice deposit account offering "
        f"{_fmt(rate)}% simple interest per annum. {name} leaves the money in the account for {months} months.\n\n"
        f"Calculate the **simple interest earned** over these {months} months.\n"
        f"Use the formula: $$I = P \\times i \\times \\frac{{m}}{{12}}$$"
    )
    sol = (
        f"Step 1: Identify given financial values:\n"
        f"• Principal ($P$) = {_fmt_curr(principal)}\n"
        f"• Annual interest rate ($i$) = {_fmt(rate)}% = {rate / 100}\n"
        f"• Time in years = {months}/12 years = {months / 12:.4f}\n\n"
        f"Step 2: Method setup – apply fractional year simple interest:\n"
        f"• Interest = $P \\times i \\times (m \\div 12)$\n"
        f"• Interest = {_fmt_curr(principal)} × ({rate}/100) × ({months}/12) "
        f"✓ [1 Mark: Method – converting {months} months to fraction of year and multiplying by $P \\times i$]\n\n"
        f"Step 3: Calculate interest amount:\n"
        f"Interest = {ans_str} ✓ [1 Mark: Accuracy – correct interest amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {principal} × {rate/100} × ({months}/12)",
        f"1 Mark: Accuracy – correct interest {ans_str}"
    ]
    hints = {
        "tier_1": f"Convert {months} months to years by dividing by 12: {months} / 12.",
        "tier_2": f"Multiply: {principal} × ({rate}/100) × ({months}/12).",
        "tier_3": f"{principal} × {rate/100} × {months/12:.4f} = {interest:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_simple_interest_months_fractional_year", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_simple_interest_rate_determination(r: random.Random) -> Dict[str, Any]:
    """Determine the annual simple interest rate given principal, duration, and interest earned."""
    name = r.choice(SA_NAMES)
    principal = r.choice([2000, 3000, 4000, 5000, 8000, 10000])
    rate = r.choice([6.0, 7.0, 8.0, 9.0, 10.0, 12.0])
    years = r.choice([2, 3, 4])
    interest = round(principal * (rate / 100) * years, 2)
    ans_str = f"{_fmt(rate)}%"

    prompt = (
        f"{name} invested {_fmt_curr(principal)} in a fixed investment for a duration of {years} years. "
        f"At the end of the term, {name} received total simple interest of {_fmt_curr(interest)}.\n\n"
        f"Calculate the **annual simple interest rate (r)** earned on this investment.\n"
        f"Use the formula: $$r = \\frac{{I}}{{P \\times n}} \\times 100\\%$$"
    )
    sol = (
        f"Step 1: Identify known values:\n"
        f"• Interest earned ($I$) = {_fmt_curr(interest)}\n"
        f"• Principal ($P$) = {_fmt_curr(principal)}\n"
        f"• Term ($n$) = {years} years\n\n"
        f"Step 2: Method setup – solve for interest rate:\n"
        f"• $r = \\frac{{{interest}}}{{{principal} \\times {years}}} \\times 100\\%$\n"
        f"• $r = \\frac{{{interest}}}{{{principal * years}}} \\times 100\\%$ "
        f"✓ [1 Mark: Method – dividing total interest by $(P \\times n)$ and multiplying by 100%]\n\n"
        f"Step 3: Calculate rate percentage:\n"
        f"$$r = {ans_str}$$\n"
        f"✓ [1 Mark: Accuracy – correct annual interest rate percentage]"
    )
    rubric = [
        f"1 Mark: Method – setting up ({interest} / ({principal} × {years})) × 100%",
        f"1 Mark: Accuracy – correct rate {ans_str}"
    ]
    hints = {
        "tier_1": f"Divide total interest ({_fmt_curr(interest)}) by the product of Principal and Years: ({principal} × {years}).",
        "tier_2": f"Multiply the resulting fraction by 100 to get the percentage.",
        "tier_3": f"({interest} / {principal * years}) × 100 = {rate}%, giving {ans_str}."
    }
    return _make_q("bank_int_simple_interest_rate_determination", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_simple_interest_term_duration_years(r: random.Random) -> Dict[str, Any]:
    """Calculate the investment term in years required to earn a specific simple interest."""
    name = r.choice(SA_NAMES)
    principal = r.choice([4000, 5000, 6000, 8000, 10000])
    rate = r.choice([5.0, 8.0, 10.0, 12.0])
    years = r.choice([2, 3, 4, 5])
    interest = round(principal * (rate / 100) * years, 2)
    ans_str = f"{years} years"

    prompt = (
        f"{name} deposits {_fmt_curr(principal)} into a savings account that pays "
        f"{_fmt(rate)}% simple interest per annum. {name} wishes to earn exactly {_fmt_curr(interest)} in interest.\n\n"
        f"Calculate how many **years (n)** the money must remain invested to reach this interest goal.\n"
        f"Use the formula: $$n = \\frac{{I}}{{P \\times i}}$$"
    )
    sol = (
        f"Step 1: Identify variables:\n"
        f"• Target interest ($I$) = {_fmt_curr(interest)}\n"
        f"• Principal ($P$) = {_fmt_curr(principal)}\n"
        f"• Rate ($i$) = {_fmt(rate)}% = {rate / 100}\n\n"
        f"Step 2: Method setup – solve for $n$:\n"
        f"• Annual interest earned = $P \\times i = {principal} \\times {rate / 100} = {_fmt_curr(principal * rate / 100)}$ per year\n"
        f"• $n = \\frac{{{interest}}}{{{principal * rate / 100}}}$ "
        f"✓ [1 Mark: Method – dividing target interest by annual interest per year]\n\n"
        f"Step 3: Calculate duration in years:\n"
        f"$$n = {ans_str}$$\n"
        f"✓ [1 Mark: Accuracy – correct number of years]"
    )
    rubric = [
        f"1 Mark: Method – dividing {_fmt_curr(interest)} by ({principal} × {rate/100})",
        f"1 Mark: Accuracy – correct term {ans_str}"
    ]
    hints = {
        "tier_1": f"First find how much interest is earned in ONE year: {principal} × ({rate}/100).",
        "tier_2": f"Divide the target interest ({_fmt_curr(interest)}) by that annual interest.",
        "tier_3": f"{interest} / {principal * rate / 100} = {years}, so the answer is {ans_str}."
    }
    return _make_q("bank_int_simple_interest_term_duration_years", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_hire_purchase_total_repayment_cost(r: random.Random) -> Dict[str, Any]:
    """Calculate the total cost of a hire purchase agreement: Deposit + (Installment * Months)."""
    name = r.choice(SA_NAMES)
    item = r.choice(["lounge suite", "3-piece wall unit", "refrigerator", "plasma television", "laptop computer"])
    deposit = r.choice([450, 650, 800, 1000, 1200, 1500])
    monthly_installment = round(r.choice([299.00, 349.00, 399.00, 449.00, 520.00]), 2)
    months = r.choice([24, 30, 36])

    installments_total = round(monthly_installment * months, 2)
    total_paid = round(deposit + installments_total, 2)
    ans_str = _fmt_curr(total_paid)

    prompt = (
        f"{name} buys a {item} on a hire purchase agreement with the following terms:\n"
        f"• **Cash deposit**: {_fmt_curr(deposit)}\n"
        f"• **Monthly installments**: {_fmt_curr(monthly_installment)} per month for **{months} months**\n\n"
        f"Calculate the **total amount** {name} will have paid for the {item} by the end of the contract.\n"
        f"Use the formula: $$\\text{{Total}} = \\text{{Deposit}} + (\\text{{Monthly Installment}} \\times \\text{{Number of Months}})$$"
    )
    sol = (
        f"Step 1: Identify hire purchase components:\n"
        f"• Upfront deposit = {_fmt_curr(deposit)}\n"
        f"• Monthly installment = {_fmt_curr(monthly_installment)}\n"
        f"• Number of monthly installments = {months}\n\n"
        f"Step 2: Method setup – calculate installment sum and add deposit:\n"
        f"• Installment Total = {months} × {_fmt_curr(monthly_installment)} = {_fmt_curr(installments_total)}\n"
        f"• Total Paid = {_fmt_curr(deposit)} + {_fmt_curr(installments_total)} "
        f"✓ [1 Mark: Method – multiplying monthly installment by {months} months and adding deposit]\n\n"
        f"Step 3: Calculate total cost:\n"
        f"Total Paid = {deposit} + {installments_total:.2f} = {ans_str}\n"
        f"✓ [1 Mark: Accuracy – correct total hire purchase cost in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating ({months} × {_fmt_curr(monthly_installment)}) + {_fmt_curr(deposit)}",
        f"1 Mark: Accuracy – correct total repayment {ans_str}"
    ]
    hints = {
        "tier_1": f"Multiply the monthly installment ({_fmt_curr(monthly_installment)}) by {months} months.",
        "tier_2": f"Add the upfront deposit ({_fmt_curr(deposit)}) to that installment total.",
        "tier_3": f"{deposit} + ({monthly_installment:.2f} × {months}) = {total_paid:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_hire_purchase_total_repayment_cost", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_hire_purchase_total_interest_amount(r: random.Random) -> Dict[str, Any]:
    """Calculate the total interest paid in Rands on a hire purchase agreement."""
    name = r.choice(SA_NAMES)
    item = r.choice(["washing machine", "dining room suite", "sound system", "double bed base set"])
    cash_price = r.choice([4999.00, 5499.00, 6499.00, 7999.00, 8999.00])
    deposit = r.choice([500.00, 650.00, 800.00, 1000.00])
    monthly_installment = round(r.choice([285.00, 345.00, 395.00, 445.00]), 2)
    months = 36

    total_hp = round(deposit + (monthly_installment * months), 2)
    interest_paid = round(total_hp - cash_price, 2)
    ans_str = _fmt_curr(interest_paid)

    prompt = (
        f"{name} sees an advertisement for a {item}:\n"
        f"• **Cash Price**: {_fmt_curr(cash_price)}\n"
        f"• **Hire Purchase Option**: Deposit of {_fmt_curr(deposit)} + 36 monthly installments of {_fmt_curr(monthly_installment)}\n\n"
        f"Calculate the **total interest (in Rands)** {name} will pay if choosing the hire purchase option.\n"
        f"Use the formula: $$\\text{{Interest}} = \\text{{Total HP Cost}} - \\text{{Cash Price}}$$"
    )
    sol = (
        f"Step 1: Calculate total hire purchase repayment:\n"
        f"• Total HP = Deposit + (36 × Monthly Installment)\n"
        f"• Total HP = {_fmt_curr(deposit)} + (36 × {_fmt_curr(monthly_installment)}) = {_fmt_curr(deposit)} + {_fmt_curr(monthly_installment * 36)} = {_fmt_curr(total_hp)}\n\n"
        f"Step 2: Method setup – subtract cash price from total hire purchase repayments:\n"
        f"• Interest = Total HP - Cash Price\n"
        f"• Interest = {_fmt_curr(total_hp)} - {_fmt_curr(cash_price)} "
        f"✓ [1 Mark: Method – calculating total HP repayment and subtracting cash price]\n\n"
        f"Step 3: Calculate interest paid:\n"
        f"Interest = {total_hp:.2f} - {cash_price:.2f} = {ans_str}\n"
        f"✓ [1 Mark: Accuracy – correct interest amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {_fmt_curr(cash_price)} from total HP cost ({_fmt_curr(total_hp)})",
        f"1 Mark: Accuracy – correct total interest {ans_str}"
    ]
    hints = {
        "tier_1": f"First find total HP paid: {_fmt_curr(deposit)} + (36 × {_fmt_curr(monthly_installment)}).",
        "tier_2": f"Subtract the original cash price ({_fmt_curr(cash_price)}) from that total HP cost.",
        "tier_3": f"{total_hp:.2f} - {cash_price:.2f} = {interest_paid:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_hire_purchase_total_interest_amount", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_hire_purchase_cash_vs_credit_difference(r: random.Random) -> Dict[str, Any]:
    """Compare buying cash vs hire purchase to quantify how much more expensive credit is."""
    name = r.choice(SA_NAMES)
    item = r.choice(["4-burner gas stove", "smart television", "deep freezer", "generator"])
    cash_price = r.choice([3999.00, 4999.00, 5999.00, 6999.00])
    deposit = round(cash_price * 0.10, 2)
    monthly_installment = round(r.choice([250.00, 310.00, 380.00, 450.00]), 2)
    months = 24

    total_hp = round(deposit + (monthly_installment * months), 2)
    diff = round(total_hp - cash_price, 2)
    ans_str = _fmt_curr(diff)

    prompt = (
        f"{name} is considering purchasing a {item}.\n"
        f"• Paying **Cash**: {_fmt_curr(cash_price)}\n"
        f"• Buying on **Credit (Hire Purchase)**: A 10% deposit of {_fmt_curr(deposit)} followed by 24 monthly installments of {_fmt_curr(monthly_installment)}\n\n"
        f"Calculate **how much more expensive** it is to buy the {item} on hire purchase rather than paying cash."
    )
    sol = (
        f"Step 1: Calculate the total cost under hire purchase:\n"
        f"• Total HP = Deposit + (24 × {_fmt_curr(monthly_installment)}) = {_fmt_curr(deposit)} + {_fmt_curr(monthly_installment * 24)} = {_fmt_curr(total_hp)}\n\n"
        f"Step 2: Method setup – calculate the difference between credit and cash cost:\n"
        f"• Difference = Total HP - Cash Price\n"
        f"• Difference = {_fmt_curr(total_hp)} - {_fmt_curr(cash_price)} "
        f"✓ [1 Mark: Method – finding difference between hire purchase total and cash price]\n\n"
        f"Step 3: Calculate difference:\n"
        f"Difference = {ans_str} ✓ [1 Mark: Accuracy – correct cost difference in Rands]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {_fmt_curr(cash_price)} from total HP cost ({_fmt_curr(total_hp)})",
        f"1 Mark: Accuracy – correct difference {ans_str}"
    ]
    hints = {
        "tier_1": f"Work out total HP price: {_fmt_curr(deposit)} + (24 × {_fmt_curr(monthly_installment)}).",
        "tier_2": f"Subtract the cash price ({_fmt_curr(cash_price)}) from that HP total.",
        "tier_3": f"{total_hp:.2f} - {cash_price:.2f} = {diff:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_hire_purchase_cash_vs_credit_difference", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_hire_purchase_effective_interest_rate(r: random.Random) -> Dict[str, Any]:
    """Calculate the total percentage of interest paid relative to the initial balance financed."""
    name = r.choice(SA_NAMES)
    cash_price = 10000.00
    deposit = 1000.00
    loan_balance = cash_price - deposit  # R 9 000
    monthly_installment = round(r.choice([380.00, 410.00, 440.00, 480.00]), 2)
    months = 36

    total_installments = round(monthly_installment * months, 2)
    interest = round(total_installments - loan_balance, 2)
    eff_rate = round((interest / loan_balance) * 100, 1)
    ans_str = f"{_fmt(eff_rate)}%"

    prompt = (
        f"{name} purchases home furniture with a cash price of {_fmt_curr(cash_price)}. "
        f"{name} pays an upfront deposit of {_fmt_curr(deposit)}, leaving a loan balance of {_fmt_curr(loan_balance)}. "
        f"{name} agrees to repay the remaining balance over 36 monthly installments of {_fmt_curr(monthly_installment)}.\n\n"
        f"1. Calculate the total interest paid: $$\\text{{Interest}} = (36 \\times {_fmt_curr(monthly_installment)}) - {_fmt_curr(loan_balance)}$$\n"
        f"2. Express this total interest as a percentage of the financed loan balance ({_fmt_curr(loan_balance)}), rounded to one decimal place."
    )
    sol = (
        f"Step 1: Calculate the total interest paid on the financed balance:\n"
        f"• Total paid in installments = 36 × {_fmt_curr(monthly_installment)} = {_fmt_curr(total_installments)}\n"
        f"• Interest paid = {_fmt_curr(total_installments)} - {_fmt_curr(loan_balance)} = {_fmt_curr(interest)}\n\n"
        f"Step 2: Method setup – calculate interest percentage relative to loan balance:\n"
        f"• Percentage = (Interest ÷ Loan Balance) × 100%\n"
        f"• Percentage = ({interest} ÷ {loan_balance}) × 100% "
        f"✓ [1 Mark: Method – dividing total interest by loan balance and multiplying by 100%]\n\n"
        f"Step 3: Calculate percentage:\n"
        f"Percentage = {ans_str} ✓ [1 Mark: Accuracy – correct percentage rounded to 1 dp]"
    )
    rubric = [
        f"1 Mark: Method – setting up ({interest} / {loan_balance}) × 100%",
        f"1 Mark: Accuracy – correct percentage {ans_str}"
    ]
    hints = {
        "tier_1": f"First find total interest: (36 × {_fmt_curr(monthly_installment)}) - {_fmt_curr(loan_balance)}.",
        "tier_2": f"Divide that interest by the financed loan balance of {_fmt_curr(loan_balance)}, then multiply by 100.",
        "tier_3": f"({interest:.2f} / {loan_balance}) × 100 = {eff_rate}%, giving {ans_str}."
    }
    return _make_q("bank_int_hire_purchase_effective_interest_rate", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_personal_unsecured_loan_monthly_installment(r: random.Random) -> Dict[str, Any]:
    """Calculate the monthly installment for an unsecured personal loan with simple interest."""
    name = r.choice(SA_NAMES)
    loan_amt = r.choice([6000, 8000, 10000, 12000, 15000])
    annual_rate = r.choice([12.0, 15.0, 18.0, 20.0])
    years = r.choice([1, 2, 3])
    months = years * 12

    interest = round(loan_amt * (annual_rate / 100) * years, 2)
    total_repay = round(loan_amt + interest, 2)
    installment = round(total_repay / months, 2)
    ans_str = _fmt_curr(installment)

    prompt = (
        f"{name} borrows an unsecured personal loan of {_fmt_curr(loan_amt)} from a financial institution. "
        f"The loan charges simple interest at {_fmt(annual_rate)}% per annum and must be repaid in equal monthly installments "
        f"over {years} year(s) ({months} months).\n\n"
        f"Calculate the **monthly installment amount** {name} must pay."
    )
    sol = (
        f"Step 1: Calculate total simple interest and total repayment:\n"
        f"• Interest = Principal × Rate × Years = {loan_amt} × ({annual_rate}/100) × {years} = {_fmt_curr(interest)}\n"
        f"• Total Repayment = Loan Amount + Interest = {_fmt_curr(loan_amt)} + {_fmt_curr(interest)} = {_fmt_curr(total_repay)}\n\n"
        f"Step 2: Method setup – divide total repayment by number of months ({months}):\n"
        f"• Monthly Installment = Total Repayment ÷ {months}\n"
        f"• Monthly Installment = {_fmt_curr(total_repay)} ÷ {months} "
        f"✓ [1 Mark: Method – dividing total repayment by {months} months]\n\n"
        f"Step 3: Calculate monthly installment:\n"
        f"Monthly Installment = {ans_str} ✓ [1 Mark: Accuracy – correct monthly installment in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating total repayment ({_fmt_curr(total_repay)}) divided by {months}",
        f"1 Mark: Accuracy – correct installment {ans_str}"
    ]
    hints = {
        "tier_1": f"First calculate the total interest: {loan_amt} × ({annual_rate}/100) × {years}.",
        "tier_2": f"Add the interest to the loan amount, then divide by {months} months.",
        "tier_3": f"{total_repay:.2f} / {months} = {installment:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_personal_unsecured_loan_monthly_installment", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_int_layby_zero_interest_cancellation_penalty(r: random.Random) -> Dict[str, Any]:
    """Calculate refund amount on a cancelled lay-by agreement after deducting the 10% statutory penalty fee."""
    name = r.choice(SA_NAMES)
    item = r.choice(["winter wardrobe package", "school uniform bundle", "kitchen cookware set"])
    item_price = r.choice([1500, 2000, 2500, 3000, 3500])
    deposit = round(item_price * 0.20, 2)
    installments_paid = round(r.choice([400.00, 600.00, 800.00]), 2)
    total_paid_so_far = round(deposit + installments_paid, 2)

    # Cancellation fee: 10% of total item price (statutory Consumer Protection Act guideline)
    cancellation_fee = round(item_price * 0.10, 2)
    refund = round(total_paid_so_far - cancellation_fee, 2)
    ans_str = _fmt_curr(refund)

    prompt = (
        f"{name} placed a {item} valued at {_fmt_curr(item_price)} on lay-by (a zero-interest purchasing option). "
        f"So far, {name} has paid a 20% deposit of {_fmt_curr(deposit)} plus monthly installments of {_fmt_curr(installments_paid)}, "
        f"totaling {_fmt_curr(total_paid_so_far)}.\n\n"
        f"Due to financial hardship, {name} cancels the lay-by agreement. Under the Consumer Protection Act, "
        f"the store deducts a cancellation administration fee of 10% of the total purchase price ({_fmt_curr(cancellation_fee)}) "
        f"and refunds the balance. Calculate the **refund amount** {name} will receive."
    )
    sol = (
        f"Step 1: Identify total payments made and cancellation penalty fee:\n"
        f"• Total payments made = {_fmt_curr(total_paid_so_far)}\n"
        f"• Cancellation fee = 10% of {_fmt_curr(item_price)} = {_fmt_curr(cancellation_fee)}\n\n"
        f"Step 2: Method setup – deduct cancellation fee from total payments:\n"
        f"• Refund = Total Payments - Cancellation Fee\n"
        f"• Refund = {_fmt_curr(total_paid_so_far)} - {_fmt_curr(cancellation_fee)} "
        f"✓ [1 Mark: Method – subtracting 10% cancellation fee from payments made]\n\n"
        f"Step 3: Calculate refund:\n"
        f"Refund = {ans_str} ✓ [1 Mark: Accuracy – correct net refund in Rands]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {_fmt_curr(cancellation_fee)} from {_fmt_curr(total_paid_so_far)}",
        f"1 Mark: Accuracy – correct refund {ans_str}"
    ]
    hints = {
        "tier_1": f"The customer paid {_fmt_curr(total_paid_so_far)} in total so far.",
        "tier_2": f"Subtract the cancellation penalty fee of {_fmt_curr(cancellation_fee)} from that total.",
        "tier_3": f"{total_paid_so_far:.2f} - {cancellation_fee:.2f} = {refund:.2f}, giving {ans_str}."
    }
    return _make_q("bank_int_layby_zero_interest_cancellation_penalty", prompt, ans_str, sol, rubric, hints, 2, r=r)
