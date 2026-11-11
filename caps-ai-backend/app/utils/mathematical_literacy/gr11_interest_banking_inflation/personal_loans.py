"""Personal loans, credit agreements, and National Credit Act (NCA) regulations (Subskills 37-44) for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_BANKS,
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_37(r: random.Random) -> Dict[str, Any]:
    """National Credit Act (NCA) maximum loan initiation fee calculation."""
    name = r.choice(SA_NAMES)
    loan_amount = r.choice([3000, 5000, 8000, 10000])
    base_fee = 165.0
    pct = 0.10  # 10% of amount in excess of R 1 000
    excess = loan_amount - 1000.0
    calc_fee = base_fee + (excess * pct)
    max_cap = 1050.0
    actual_fee = min(calc_fee, max_cap)
    ans_str = _fmt_curr(actual_fee)

    prompt = (
        f"{name} applies for an unsecured personal loan of {_fmt_curr(loan_amount)} from a registered South African credit provider.\n"
        f"Under the National Credit Act (NCA) regulations, the maximum initiation fee is determined by:\n"
        f"Initiation Fee = R 165,00 + 10% of the loan amount in excess of R 1 000,00 (maximum cap: R 1 050,00).\n\n"
        f"Calculate the legal maximum initiation fee that the credit provider may charge {name}."
    )
    explanation = (
        f"Step 1: Calculate the amount in excess of R 1 000:\n"
        f"\\text{{Excess}} = {loan_amount} - 1\\,000 = {_fmt_curr(excess)}. [1 mark]\n"
        f"Step 2: Calculate 10% of the excess and add R 165,00:\n"
        f"\\text{{Fee}} = 165,00 + ({_fmt(excess)} \\times 0,10) = 165,00 + {_fmt(excess * 0.10)} = {_fmt_curr(calc_fee)}. [1 mark]\n"
        f"Step 3: Check against the R 1 050 cap and state the final fee:\n"
        f"\\text{{Initiation fee}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(loan_amount * 0.10, 2)),
        _fmt_curr(max_cap),
        _fmt_curr(round(actual_fee + 120, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_37",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract R 1 000 from the loan amount, take 10% of the remainder, and add R 165.",
        f"Excess = {_fmt_curr(excess)}. Fee = 165 + ({_fmt(excess)} × 0,10).",
        f"Initiation fee = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Monthly credit administration service fee addition over loan term."""
    name = r.choice(SA_NAMES)
    service_fee = 69.0  # Max NCA monthly service fee is R 69/month
    term_months = r.choice([12, 24, 36, 48])
    total_service_fees = round(service_fee * term_months, 2)
    ans_str = _fmt_curr(total_service_fees)

    prompt = (
        f"{name} took out a personal loan repayable over a {term_months}-month term.\n"
        f"The credit agreement includes a statutory monthly account service fee of {_fmt_curr(service_fee)} per month.\n"
        f"Calculate the total cumulative service fees that {name} will pay over the entire {term_months}-month life of the loan."
    )
    explanation = (
        f"Step 1: Identify the monthly fee and the number of months:\n"
        f"\\text{{Monthly fee}} = {_fmt_curr(service_fee)}; \\text{{Term}} = {term_months}\\text{{ months}}. [1 mark]\n"
        f"Step 2: Multiply monthly fee by number of months:\n"
        f"\\text{{Total}} = 69,00 \\times {term_months} = {total_service_fees:.2f} [1 mark]\n"
        f"Step 3: State the total cumulative service fees:\n"
        f"\\text{{Total service fees}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(service_fee),
        _fmt_curr(round(total_service_fees + 250, 2)),
        _fmt_curr(round(total_service_fees - 150, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_38",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the monthly service fee of R 69,00 by {term_months} months.",
        f"Calculate 69,00 × {term_months}.",
        f"Total service fees = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Personal bank loan monthly repayment calculation given total amount and loan term."""
    name = r.choice(SA_NAMES)
    total_repayable = r.choice([18000, 24000, 30000, 36000, 42000])
    term_months = r.choice([24, 36, 48])
    monthly_payment = round(total_repayable / term_months, 2)
    ans_str = _fmt_curr(monthly_payment)

    prompt = (
        f"A bank approves {name}'s home improvement loan with a fixed total repayment obligation of {_fmt_curr(total_repayable)} "
        f"spread equally over {term_months} months.\n"
        f"Calculate the fixed monthly instalment that {name} must budget to pay each month."
    )
    explanation = (
        f"Step 1: Set up the division (Total Repayable ÷ Term in Months):\n"
        f"\\text{{Monthly Instalment}} = \\frac{{{total_repayable}}}{{{term_months}}}. [1 mark]\n"
        f"Step 2: Divide the values:\n"
        f"{total_repayable} \\div {term_months} = {monthly_payment:.2f} [1 mark]\n"
        f"Step 3: State the monthly instalment:\n"
        f"\\text{{Monthly instalment}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(total_repayable / 12, 2)),
        _fmt_curr(round(monthly_payment + 150, 2)),
        _fmt_curr(round(monthly_payment - 100, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_39",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the total repayable amount by {term_months} months.",
        f"Calculate {total_repayable} ÷ {term_months}.",
        f"Monthly instalment = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Total loan repayment over full term and total finance charges."""
    name = r.choice(SA_NAMES)
    principal_borrowed = 15000.0
    monthly_instalment = 585.0
    months = 36
    total_paid = monthly_instalment * months  # 21 060
    finance_charges = round(total_paid - principal_borrowed, 2)
    ans_str = _fmt_curr(finance_charges)

    prompt = (
        f"{name} borrowed {_fmt_curr(principal_borrowed)} as a personal loan and repaid it in 36 monthly instalments of {_fmt_curr(monthly_instalment)}.\n"
        f"Calculate the total finance charges (total interest and fees) paid by {name} above the original amount borrowed."
    )
    explanation = (
        f"Step 1: Calculate the total amount repaid over 36 months:\n"
        f"\\text{{Total Paid}} = 585 \\times 36 = {_fmt_curr(total_paid)}. [1 mark]\n"
        f"Step 2: Subtract the principal borrowed from the total paid:\n"
        f"\\text{{Finance Charges}} = {_fmt(total_paid)} - 15\\,000 = {finance_charges:.2f} [1 mark]\n"
        f"Step 3: State the final finance charges:\n"
        f"\\text{{Finance charges}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(total_paid),
        _fmt_curr(principal_borrowed),
        _fmt_curr(round(finance_charges + 1000, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_40",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply the monthly instalment by 36, then subtract the R 15 000 borrowed.",
        f"Total paid = 585 × 36 = {_fmt_curr(total_paid)}. Charges = {_fmt(total_paid)} - 15 000.",
        f"Finance charges = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Micro-lender / payday loan high-interest short-term loan trap calculation."""
    name = r.choice(SA_NAMES)
    borrowed = 2000.0
    fee_pct = 20.0  # 20% interest for 1 month
    admin_fee = 150.0
    interest = borrowed * (fee_pct / 100.0)  # R 400
    total_repayable = round(borrowed + interest + admin_fee, 2)
    ans_str = _fmt_curr(total_repayable)

    prompt = (
        f"{name} borrows {_fmt_curr(borrowed)} from a short-term payday micro-lender repayable in full at month-end.\n"
        f"The lender charges 20% interest for the single month plus a {_fmt_curr(admin_fee)} documentation processing fee.\n"
        f"Calculate the total amount {name} must repay at the end of the month."
    )
    explanation = (
        f"Step 1: Calculate the 20% one-month interest:\n"
        f"\\text{{Interest}} = 2\\,000 \\times 0,20 = {_fmt_curr(interest)}. [1 mark]\n"
        f"Step 2: Add principal, interest, and processing fee:\n"
        f"\\text{{Total Repayable}} = 2\\,000 + 400 + 150 = {total_repayable:.2f} [1 mark]\n"
        f"Step 3: State the total repayable amount:\n"
        f"\\text{{Total repayable}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(borrowed + interest, 2)),
        _fmt_curr(round(borrowed + admin_fee, 2)),
        _fmt_curr(round(total_repayable + 200, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_41",
        prompt,
        ans_str,
        options,
        explanation,
        "Add 20% of R 2 000 (R 400) and the R 150 fee to the R 2 000 principal.",
        f"Total = 2 000 + 400 + 150.",
        f"Total repayable = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Impact of increasing loan repayment term (lower instalment vs higher total interest)."""
    loan_amount = 30000.0
    # Option 1: 24 months at R 1 550/month -> Total paid = R 37 200 (Interest = R 7 200)
    # Option 2: 48 months at R 950/month -> Total paid = R 45 600 (Interest = R 15 600)
    total_1 = 1550.0 * 24
    total_2 = 950.0 * 48
    extra_interest = round(total_2 - total_1, 2)
    ans_str = _fmt_curr(extra_interest)

    prompt = (
        f"A borrower compares two repayment options for a {_fmt_curr(loan_amount)} loan:\n"
        f"• Option 1 (24-month term): Monthly instalment is R 1 550,00.\n"
        f"• Option 2 (48-month term): Monthly instalment is R 950,00.\n\n"
        f"Although Option 2 has a lower monthly instalment, calculate how much MORE in total interest and charges "
        f"the borrower pays overall under Option 2 compared to Option 1."
    )
    explanation = (
        f"Step 1: Calculate total amount repaid under Option 1:\n"
        f"\\text{{Total 1}} = 1\\,550 \\times 24 = {_fmt_curr(total_1)}. [1 mark]\n"
        f"Step 2: Calculate total amount repaid under Option 2:\n"
        f"\\text{{Total 2}} = 950 \\times 48 = {_fmt_curr(total_2)}. [1 mark]\n"
        f"Step 3: Subtract Option 1 total from Option 2 total:\n"
        f"\\text{{Extra Interest}} = {_fmt(total_2)} - {_fmt(total_1)} = {extra_interest:.2f} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(total_2 - loan_amount, 2)),
        _fmt_curr(round(total_1 - loan_amount, 2)),
        _fmt_curr(round(extra_interest + 1500, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_42",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate total repaid for both options (instalment × months) and find the difference.",
        f"Opt 1 = 1 550 × 24 = {_fmt_curr(total_1)}. Opt 2 = 950 × 48 = {_fmt_curr(total_2)}. Difference = {_fmt_curr(extra_interest)}.",
        f"Extra cost = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Comparing two personal loan quotations with different interest rates and origination fees."""
    # Quotation A: Total repayment R 18 500 + R 850 origination fee = R 19 350
    # Quotation B: Total repayment R 17 800 + R 1 050 origination fee = R 18 850
    tot_a = 18500.0 + 850.0   # 19 350
    tot_b = 17800.0 + 1050.0  # 18 850
    diff = round(tot_a - tot_b, 2)
    ans_str = f"Quotation B is cheaper by {_fmt_curr(diff)}"

    prompt = (
        f"A consumer receives two loan quotations for borrowing R 15 000,00:\n"
        f"• Quotation A: Total repayments of R 18 500,00 plus an initiation fee of R 850,00\n"
        f"• Quotation B: Total repayments of R 17 800,00 plus an initiation fee of R 1 050,00\n\n"
        f"Determine which quotation is cheaper overall, and by how much."
    )
    explanation = (
        f"Step 1: Calculate grand total cost for Quotation A:\n"
        f"\\text{{Total A}} = 18\\,500 + 850 = {_fmt_curr(tot_a)}. [1 mark]\n"
        f"Step 2: Calculate grand total cost for Quotation B:\n"
        f"\\text{{Total B}} = 17\\,800 + 1\\,050 = {_fmt_curr(tot_b)}. [1 mark]\n"
        f"Step 3: Subtract to compare:\n"
        f"{_fmt(tot_a)} - {_fmt(tot_b)} = {diff:.2f}.\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Quotation A is cheaper by {_fmt_curr(diff)}",
        f"Quotation B is cheaper by {_fmt_curr(round(diff * 1.5, 2))}",
        "Both quotations cost the exact same amount",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_43",
        prompt,
        ans_str,
        options,
        explanation,
        "Add the initiation fee to the repayments for each quotation and compare.",
        f"A = {_fmt_curr(tot_a)}, B = {_fmt_curr(tot_b)}. Difference = {_fmt_curr(diff)}.",
        f"Conclusion = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Credit score impact on personal loan interest rate (prime minus vs prime plus)."""
    prime_rate = 11.75  # Current SA prime overdraft rate
    # Borrower 1: Excellent credit score -> Prime - 1,0% = 10,75%
    # Borrower 2: Low credit score -> Prime + 4,5% = 16,25%
    rate_good = prime_rate - 1.0
    rate_poor = prime_rate + 4.5
    spread = round(rate_poor - rate_good, 2)
    ans_str = f"{_fmt(spread)} percentage points"

    prompt = (
        f"In South Africa, commercial banks price personal loans relative to the Prime Lending Rate (currently {_fmt(prime_rate)}%):\n"
        f"• Borrower A has an excellent credit score and qualifies for an interest rate of 'Prime minus 1,0%'.\n"
        f"• Borrower B has a poor credit history and is offered an interest rate of 'Prime plus 4,5%'.\n\n"
        f"Calculate the difference in interest rates (in percentage points) between Borrower B and Borrower A."
    )
    explanation = (
        f"Step 1: Calculate Borrower A's interest rate:\n"
        f"\\text{{Rate A}} = {_fmt(prime_rate)}\\% - 1,0\\% = {_fmt(rate_good)}\\%. [1 mark]\n"
        f"Step 2: Calculate Borrower B's interest rate:\n"
        f"\\text{{Rate B}} = {_fmt(prime_rate)}\\% + 4,5\\% = {_fmt(rate_poor)}\\%. [1 mark]\n"
        f"Step 3: Subtract Rate A from Rate B:\n"
        f"{_fmt(rate_poor)}\\% - {_fmt(rate_good)}\\% = {_fmt(spread)}\\text{{ percentage points}}.\n"
        f"\\text{{Difference}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(spread - 1.0, 2))} percentage points",
        f"{_fmt(round(spread + 2.0, 2))} percentage points",
        f"{_fmt(prime_rate)} percentage points",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_44",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate both interest rates from prime, then find the difference.",
        f"Good = {_fmt(rate_good)}%. Poor = {_fmt(rate_poor)}%. Difference = {_fmt(spread)}%.",
        f"Difference = {ans_str}.",
        r,
        difficulty="medium",
    )
