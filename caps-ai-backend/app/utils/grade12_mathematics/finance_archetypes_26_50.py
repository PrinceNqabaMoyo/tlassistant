"""Grade 12 Mathematics - Financial Mathematics (Archetypes 26-50).
100% Aligned with South African National Curriculum Standards (CAPS Grade 12 Paper 1).
Grounded strictly in curriculum_docs_auto/Mathematics_Gr12/Term 2/01. Finance.md and Syllabus.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from .finance_archetypes_01_25 import (
    _fmt_decimal_sa,
    _fmt_zar,
    _mcq,
    _typed,
)


def _svg_timeline(
    events: List[Tuple[str, str, str]],
    t_max: str = "T_n",
) -> Dict[str, Any]:
    """Generates an inline SVG timeline for multi-stage financial problems."""
    n_pts = len(events)
    width = 540
    start_x = 60
    end_x = 480
    dx = (end_x - start_x) / max(1, n_pts - 1)

    points_svg = []
    labels_svg = []
    for idx, (t_lbl, top_lbl, bot_lbl) in enumerate(events):
        x = start_x + idx * dx
        points_svg.append(f'<circle cx="{x:.1f}" cy="80" r="5" fill="#2563eb"/>')
        points_svg.append(f'<text x="{x:.1f}" y="105" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{t_lbl}</text>')
        if top_lbl:
            points_svg.append(f'<text x="{x:.1f}" y="65" font-size="10" font-weight="bold" text-anchor="middle" fill="#dc2626">{top_lbl}</text>')
        if bot_lbl:
            points_svg.append(f'<text x="{x:.1f}" y="125" font-size="10" text-anchor="middle" fill="#16a34a">{bot_lbl}</text>')

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 160" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">'
        f'<line x1="40" y1="80" x2="500" y2="80" stroke="#334155" stroke-width="2"/>'
        f'<polygon points="505,80 495,75 495,85" fill="#334155"/>'
        + "".join(points_svg)
        + '</svg>'
    )
    return {
        "kind": "inline_svg",
        "title": "Financial Timeline",
        "svg": svg,
        "diagram_role": "context",
    }


# ---------------------------------------------------------------------------
# Archetypes 26 - 35 (Derivations, Rate Changes, Accelerated Loans, Sinking Funds)
# ---------------------------------------------------------------------------

def _b26_derivation_future_value_geometric_series(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Regular equal deposits of $x$ are made at the end of each period into an account earning interest at rate $i$ per period." + "\n"
        r"The accumulated future value after $n$ periods is the sum of a geometric series:" + "\n"
        r"$$F_v = x + x(1+i) + x(1+i)^2 + \dots + x(1+i)^{n-1}$$" + "\n"
        r"Using the geometric series sum formula $S_n = \frac{a(r^n - 1)}{r - 1}$, what is the first term $a$ and common ratio $r$?"
    )
    ans = r"First term $a = x$, Common ratio $r = 1 + i$"
    dist = [
        r"First term $a = x(1+i)$, Common ratio $r = i$",
        r"First term $a = x$, Common ratio $r = 1 - i$",
        r"First term $a = 1$, Common ratio $r = x(1+i)$",
    ]
    sol = (
        r"1. Write out the terms in reverse order starting from the last payment:" + "\n"
        r"$$T_1 = x, \quad T_2 = x(1+i), \quad T_3 = x(1+i)^2, \quad \dots, \quad T_n = x(1+i)^{n-1}$$" + "\n"
        r"2. First term $a = x$ and the multiplier between consecutive terms is $r = \frac{x(1+i)}{x} = 1 + i$." + "\n"
        r"3. Substituting into $S_n = \frac{a(r^n - 1)}{r - 1}$ gives:" + "\n"
        r"$$F_v = \frac{x\left[(1+i)^n - 1\right]}{(1+i) - 1} = \frac{x\left[(1+i)^n - 1\right]}{i}$$"
    )
    return _mcq(
        rng,
        subskill="26_derivation_future_value_geometric_series",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-26",
        concept_id="future_value_derivation",
        misconception_tags=["confused_first_term_with_compounded_amount"],
        hints=[
            "Identify the term that does not earn any interest (the final deposit made at maturity).",
            "Divide the second term by the first term to find the common ratio r.",
            r"First term is x and common ratio is 1 + i.",
        ],
        worked_solution=sol,
    )


def _b27_derivation_present_value_geometric_series(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"A loan is repaid through equal installments of $x$ starting one period after the loan is granted." + "\n"
        r"The present value of the loan is the sum of the discounted payments:" + "\n"
        r"$$P_v = x(1+i)^{-1} + x(1+i)^{-2} + \dots + x(1+i)^{-n}$$" + "\n"
        r"By summing this geometric series with $a = x(1+i)^{-1}$ and $r = (1+i)^{-1}$, derive the canonical present value formula $P_v$."
    )
    ans = r"P_v = \frac{x\left[1 - (1+i)^{-n}\right]}{i}"
    dist = [
        r"P_v = \frac{x\left[(1+i)^n - 1\right]}{i}",
        r"P_v = \frac{x\left[1 - (1+i)^n\right]}{i}",
        r"P_v = \frac{x(1+i)^{-n}}{i}",
    ]
    sol = (
        r"1. Use geometric series formula $S_n = \frac{a(1 - r^n)}{1 - r}$ with $a = x(1+i)^{-1}$ and $r = (1+i)^{-1}$:" + "\n"
        r"$$P_v = \frac{x(1+i)^{-1}\left[1 - (1+i)^{-n}\right]}{1 - (1+i)^{-1}}$$" + "\n"
        r"2. Multiply numerator and denominator by $(1+i)$:" + "\n"
        r"$$\text{Denominator} = (1+i)\left[1 - (1+i)^{-1}\right] = (1+i) - 1 = i$$" + "\n"
        r"$$\text{Numerator} = x(1+i)^{-1}(1+i)\left[1 - (1+i)^{-n}\right] = x\left[1 - (1+i)^{-n}\right]$$" + "\n"
        r"3. Hence $P_v = \frac{x\left[1 - (1+i)^{-n}\right]}{i}$."
    )
    return _mcq(
        rng,
        subskill="27_derivation_present_value_geometric_series",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-27",
        concept_id="present_value_derivation",
        misconception_tags=["sign_error_in_negative_exponent"],
        hints=[
            r"Recall that r = (1+i)^{-1} < 1, so use S_n = \frac{a(1 - r^n)}{1 - r}.",
            "Multiply numerator and denominator by (1 + i) to clear the fractional exponent.",
            r"The resulting canonical formula is P_v = \frac{x[1 - (1+i)^{-n}]}{i}.",
        ],
        worked_solution=sol,
    )


def _b28_fv_annuity_interest_rate_increase_two_stages(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([2000, 2500, 3000, 3500])
    r1 = rng.choice([8.0, 9.0, 10.0])
    r2 = r1 + 2.0
    n1 = 36  # 3 years
    n2 = 24  # 2 years
    i1 = (r1 / 100) / 12
    i2 = (r2 / 100) / 12

    # After 36 months, accumulated FV1
    fv1 = x * ((1 + i1)**n1 - 1) / i1
    # FV1 grows at i2 for 24 months, plus new annuity of x for 24 months at i2
    fv_total = fv1 * (1 + i2)**n2 + x * ((1 + i2)**n2 - 1) / i2
    ans = _fmt_zar(round(fv_total, 2))

    timeline = _svg_timeline([
        ("T0", "Start", f"R{x}/m"),
        ("T36", f"Rate: {int(r1)}% to {int(r2)}%", "FV1"),
        ("T60", "Maturity", "Total FV"),
    ])

    prompt = (
        f"Refer to the timeline below. An investor deposits {_fmt_zar(x)} at the end of each month into an investment account.\n"
        f"For the first 3 years (36 months), interest is earned at {int(r1)}\\% p.a. compounded monthly.\n"
        f"Thereafter, the interest rate increases to {int(r2)}\\% p.a. compounded monthly for the remaining 2 years (24 months).\n"
        f"The monthly deposit of {_fmt_zar(x)} continues unchanged.\n"
        f"Calculate the total accumulated future value at the end of the 5-year period."
    )
    sol = (
        f"1. Calculate the future value accumulated after the first 36 months at $i_1 = \\frac{{{r1/100}}}{{12}}$:\n"
        f"$$FV_1 = \\frac{{{x}\\left[(1 + i_1)^{{36}} - 1\\right]}}{{i_1}} \\approx {_fmt_zar(round(fv1, 2))}$$\n"
        f"2. Allow $FV_1$ to accumulate interest at $i_2 = \\frac{{{r2/100}}}{{12}}$ for 24 months:\n"
        f"$$FV_1 \\times (1 + i_2)^{{24}} \\approx {_fmt_zar(round(fv1 * (1 + i2)**n2, 2))}$$\n"
        f"3. Calculate the value of the 24 new deposits at $i_2$:\n"
        f"$$FV_2 = \\frac{{{x}\\left[(1 + i_2)^{{24}} - 1\\right]}}{{i_2}} \\approx {_fmt_zar(round(x * ((1 + i2)**n2 - 1) / i2, 2))}$$\n"
        f"4. Total Value $= {_fmt_zar(round(fv1 * (1 + i2)**n2, 2))} + {_fmt_zar(round(x * ((1 + i2)**n2 - 1) / i2, 2))} = {ans}$."
    )
    return _typed(
        subskill="28_fv_annuity_interest_rate_increase_two_stages",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{fv_total:.2f}", f"{fv_total:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-28",
        concept_id="two_stage_fv_rate_change",
        misconception_tags=["forgot_to_compound_first_annuity_during_second_stage"],
        hints=[
            "Compute FV at T36, then grow that lump sum over the remaining 24 months.",
            "Add the second annuity formed by the remaining 24 payments.",
            f"Total future value is {ans}.",
        ],
        worked_solution=sol,
        diagram_spec=timeline,
        marks=5,
    )


def _b29_home_loan_interest_rate_hike_new_installment(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([600000, 750000, 900000])
    r_initial = rng.choice([9.0, 10.0])
    r_new = r_initial + 1.5
    total_months = 240  # 20 years
    passed_months = 60  # 5 years
    rem_months = total_months - passed_months  # 180 months

    i1 = (r_initial / 100) / 12
    # Original installment
    x_orig = p * i1 / (1 - (1 + i1)**(-total_months))
    # Balance after 60 months
    bal = p * (1 + i1)**passed_months - x_orig * ((1 + i1)**passed_months - 1) / i1
    # New installment for remaining 180 months at r_new
    i2 = (r_new / 100) / 12
    x_new = bal * i2 / (1 - (1 + i2)**(-rem_months))
    ans = _fmt_zar(round(x_new, 2))

    prompt = (
        f"A homeowner takes out a home loan of {_fmt_zar(p)} over 20 years (240 months) at {int(r_initial)}\\% p.a. compounded monthly.\n"
        f"After exactly 5 years (60 monthly payments of {_fmt_zar(round(x_orig, 2))}), the bank raises the interest rate to "
        f"{_fmt_decimal_sa(r_new)}\\% p.a. compounded monthly.\n"
        f"Calculate the new monthly repayment required to settle the loan over the remaining 15 years (180 months)."
    )
    sol = (
        f"1. Determine the outstanding balance after 60 payments:\n"
        f"$$\\text{{Balance}} = {p}(1 + i_1)^{{60}} - \\frac{{{round(x_orig, 2)}\\left[(1 + i_1)^{{60}} - 1\\right]}}{{i_1}} \\approx {_fmt_zar(round(bal, 2))}$$\n"
        f"2. Solve for new monthly payment $x_{{\\text{{new}}}}$ over 180 remaining months at $i_2 = \\frac{{{r_new/100}}}{{12}}$:\n"
        f"$$P_v = \\frac{{x_{{\\text{{new}}}}\\left[1 - (1 + i_2)^{{-180}}\\right]}}{{i_2}} \\implies x_{{\\text{{new}}}} = \\frac{{{round(bal, 2)} \\times i_2}}{{1 - (1 + i_2)^{{-180}}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="29_home_loan_interest_rate_hike_new_installment",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{x_new:.2f}", f"{x_new:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-29",
        concept_id="loan_interest_rate_recalculation",
        misconception_tags=["used_original_principal_instead_of_outstanding_balance"],
        hints=[
            "First find the outstanding balance after 60 months using either the forward or backward method.",
            "Use the outstanding balance as Pv in the present value formula with n = 180 and the new interest rate.",
            f"The new monthly payment is {ans}.",
        ],
        worked_solution=sol,
        marks=5,
    )


def _b30_accelerated_loan_repayment_extra_monthly_amount(rng: random.Random) -> Dict[str, Any]:
    p = 500000
    r = 12.0
    i = (r / 100) / 12
    n_orig = 240
    x_orig = p * i / (1 - (1 + i)**(-n_orig))
    extra = rng.choice([500, 800, 1000])
    x_new = x_orig + extra

    # Solve for new n: P = x_new * (1 - (1+i)^-n) / i => 1 - P*i/x_new = (1+i)^-n
    term = 1 - (p * i) / x_new
    n_new = -math.log(term) / math.log(1 + i)
    n_ceil = math.ceil(n_new)
    months_saved = n_orig - n_ceil

    ans = f"{months_saved} months"
    dist = [
        f"{months_saved + 24} months",
        f"{months_saved - 12} months",
        f"{n_ceil} months",
    ]
    sol = (
        f"1. Original monthly repayment on {_fmt_zar(p)} over 240 months at 12% p.a.:\n"
        f"$$x_{{\\text{{orig}}}} = \\frac{{{p} \\times 0{{,}}01}}{{1 - (1{{,}}01)^{{-240}}}} \\approx {_fmt_zar(round(x_orig, 2))}$$\n"
        f"2. New repayment with extra {_fmt_zar(extra)}: $x_{{\\text{{new}}}} = {_fmt_zar(round(x_new, 2))}$.\n"
        f"3. Solve for new duration $n$:\n"
        f"$$1 - \\frac{{{p} \\times 0{{,}}01}}{{{round(x_new, 2)}}} = (1{{,}}01)^{{-n}} \\implies (1{{,}}01)^{{-n}} \\approx {round(term, 4)}$$\n"
        f"$$-n = \\frac{{\\ln({round(term, 4)})}}{{\\ln(1{{,}}01)}} \\approx {-round(n_new, 2)} \\implies n \\approx {n_ceil}\\text{{ payments}}$$\n"
        f"4. Months saved $= 240 - {n_ceil} = {months_saved}\\text{{ months}}$."
    )
    return _mcq(
        rng,
        subskill="30_accelerated_loan_repayment_extra_monthly_amount",
        prompt=(
            f"A borrower owes {_fmt_zar(p)} on a 20-year home loan at 12% p.a. compounded monthly (monthly payment {_fmt_zar(round(x_orig, 2))}).\n"
            f"If the borrower increases the monthly repayment by {_fmt_zar(extra)}, how many months earlier will the loan be paid off?"
        ),
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-30",
        concept_id="accelerated_amortization_log_n",
        misconception_tags=["reported_new_loan_term_instead_of_months_saved"],
        hints=[
            rf"Add R{extra} to the monthly repayment.",
            "Solve for n using logarithms: -n = ln(1 - P*i/x) / ln(1+i).",
            f"Subtract the new term ({n_ceil} months) from 240 months to find the time saved.",
        ],
        worked_solution=sol,
    )


def _b31_total_interest_saved_accelerated_loan_repayment(rng: random.Random) -> Dict[str, Any]:
    p = 400000
    r = 11.0
    i = (r / 100) / 12
    n1 = 240
    x1 = p * i / (1 - (1 + i)**(-n1))
    extra = rng.choice([600, 1000])
    x2 = x1 + extra

    term = 1 - (p * i) / x2
    n2 = math.ceil(-math.log(term) / math.log(1 + i))

    tot_repaid_1 = x1 * n1
    tot_repaid_2 = x2 * n2
    saved = round(tot_repaid_1 - tot_repaid_2, 2)
    ans = _fmt_zar(saved)

    prompt = (
        f"A homeowner repays a loan of {_fmt_zar(p)} at 11% p.a. compounded monthly over 20 years (monthly payment {_fmt_zar(round(x1, 2))}).\n"
        f"If the homeowner decides from the outset to pay an extra {_fmt_zar(extra)} each month, the loan is settled in {n2} months instead of 240.\n"
        f"Calculate the total interest saved over the life of the loan."
    )
    sol = (
        f"1. Total paid under original plan: $240 \\times {_fmt_zar(round(x1, 2))} = {_fmt_zar(round(tot_repaid_1, 2))}$.\n"
        f"2. Total paid under accelerated plan: ${n2} \\times {_fmt_zar(round(x2, 2))} = {_fmt_zar(round(tot_repaid_2, 2))}$.\n"
        f"3. Total savings $= {_fmt_zar(round(tot_repaid_1, 2))} - {_fmt_zar(round(tot_repaid_2, 2))} = {ans}$."
    )
    return _typed(
        subskill="31_total_interest_saved_accelerated_loan_repayment",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{saved:.2f}", f"{saved:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-31",
        concept_id="total_interest_saved",
        misconception_tags=["subtracted_only_principal_savings"],
        hints=[
            "Find the total amount paid in the original plan: 240 * original payment.",
            f"Find the total amount paid in the accelerated plan: {n2} * new payment.",
            f"The difference is {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b32_total_interest_paid_over_loan_lifetime(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([250000, 320000, 450000])
    r = rng.choice([10.5, 11.5, 12.0])
    years = rng.choice([15, 20])
    n = years * 12
    i = (r / 100) / 12
    x = p * i / (1 - (1 + i)**(-n))
    tot_paid = x * n
    tot_interest = round(tot_paid - p, 2)
    ans = _fmt_zar(tot_interest)

    prompt = (
        f"A personal loan of {_fmt_zar(p)} is repaid in monthly installments of {_fmt_zar(round(x, 2))} "
        f"over {years} years ({n} months) at {_fmt_decimal_sa(r)}\\% p.a. compounded monthly.\n"
        f"Calculate the total interest charged by the bank over the entire duration of the loan."
    )
    sol = (
        f"1. Total amount repaid to the bank:\n"
        f"$$\\text{{Total Repaid}} = {n} \\times {_fmt_zar(round(x, 2))} = {_fmt_zar(round(tot_paid, 2))}$$\n"
        f"2. Total interest paid:\n"
        f"$$\\text{{Total Interest}} = \\text{{Total Repaid}} - \\text{{Principal}} = {_fmt_zar(round(tot_paid, 2))} - {_fmt_zar(p)} = {ans}$$"
    )
    return _typed(
        subskill="32_total_interest_paid_over_loan_lifetime",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{tot_interest:.2f}", f"{tot_interest:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-32",
        concept_id="lifetime_loan_interest",
        misconception_tags=["forgot_to_subtract_principal_borrowed"],
        hints=[
            "Total Repaid = Number of Months * Monthly Payment.",
            "Total Interest = Total Repaid - Initial Loan Amount.",
            f"Total interest is {ans}.",
        ],
        worked_solution=sol,
    )


def _b33_amortization_split_principal_interest_payment_k(rng: random.Random) -> Dict[str, Any]:
    p = 300000
    r = 12.0
    i = (r / 100) / 12  # 0.01 per month
    n = 120
    x = p * i / (1 - (1 + i)**(-n))
    # For payment 1: interest = P * i
    int_1 = p * i
    princ_1 = x - int_1
    ans = f"Interest = {_fmt_zar(round(int_1, 2))}, Principal = {_fmt_zar(round(princ_1, 2))}"
    dist = [
        f"Interest = {_fmt_zar(round(princ_1, 2))}, Principal = {_fmt_zar(round(int_1, 2))}",
        f"Interest = {_fmt_zar(round(x * 0.5, 2))}, Principal = {_fmt_zar(round(x * 0.5, 2))}",
        f"Interest = {_fmt_zar(round(int_1 * 1.2, 2))}, Principal = {_fmt_zar(round(princ_1 * 0.8, 2))}",
    ]
    sol = (
        f"1. Monthly installment: $x = \\frac{{{p} \\times 0{{,}}01}}{{1 - (1{{,}}01)^{{-120}}}} \\approx {_fmt_zar(round(x, 2))}$.\n"
        f"2. During the very first month, interest is charged on the full principal:\n"
        f"$$\\text{{Interest}}_{{1}} = {_fmt_zar(p)} \\times 0{{,}}01 = {_fmt_zar(round(int_1, 2))}$$\n"
        f"3. The remainder of the payment reduces the principal debt:\n"
        f"$$\\text{{Principal Reduction}}_{{1}} = {_fmt_zar(round(x, 2))} - {_fmt_zar(round(int_1, 2))} = {_fmt_zar(round(princ_1, 2))}$$\n"
        f"4. Therefore: {ans}."
    )
    return _mcq(
        rng,
        subskill="33_amortization_split_principal_interest_payment_k",
        prompt=(
            f"A loan of {_fmt_zar(p)} is repaid over 10 years (120 months) at 12% p.a. compounded monthly (monthly installment {_fmt_zar(round(x, 2))}).\n"
            f"For the **first payment**, determine the exact portions that go towards paying interest and reducing the loan principal."
        ),
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-33",
        concept_id="amortization_payment_breakdown",
        misconception_tags=["inverted_principal_and_interest_shares"],
        hints=[
            "Interest for the month is calculated directly on the principal: P * i.",
            "Principal reduction is the monthly installment minus the interest portion.",
            f"Interest portion is {_fmt_zar(round(int_1, 2))}.",
        ],
        worked_solution=sol,
    )


def _b34_deferred_loan_payments_grace_period_interest_capitalised(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([150000, 200000, 250000])
    r = 12.0
    i = (r / 100) / 12  # 0.01 per month
    delay = rng.choice([3, 6])
    n_payments = 60
    # Interest capitalises for 'delay' months before first repayment
    p_compounded = p * (1 + i)**delay
    x = p_compounded * i / (1 - (1 + i)**(-n_payments))
    ans = _fmt_zar(round(x, 2))

    timeline = _svg_timeline([
        ("T0", "Loan Granted", f"R{p:,}"),
        (f"T{delay}", "Grace Period Ends", "First Payment"),
        (f"T{delay + n_payments}", "Loan Settled", f"{n_payments}th Payment"),
    ])

    prompt = (
        f"Refer to the timeline below. A student takes out a tertiary study loan of {_fmt_zar(p)} at 12% p.a. compounded monthly.\n"
        f"The bank grants a grace period of {delay} months during which no payments are made, but interest is capitalised monthly.\n"
        f"The borrower then begins repaying the loan in {n_payments} equal monthly installments starting at the end of month {delay}.\n"
        f"Calculate the monthly installment required to settle the loan."
    )
    sol = (
        f"1. During the {delay}-month grace period, the principal grows with compound interest:\n"
        f"$$P_{{\\text{{accumulated}}}} = {p} \\times (1 + 0{{,}}01)^{{{delay}}} \\approx {_fmt_zar(round(p_compounded, 2))}$$\n"
        f"2. Use this accumulated amount as the present value for the {n_payments} repayments:\n"
        f"$$x = \\frac{{P_{{\\text{{accumulated}}}} \\times i}}{{1 - (1 + i)^{{-{n_payments}}}}} = \\frac{{{round(p_compounded, 2)} \\times 0{{,}}01}}{{1 - (1{{,}}01)^{{-{n_payments}}}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="34_deferred_loan_payments_grace_period_interest_capitalised",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{x:.2f}", f"{x:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-34",
        concept_id="deferred_loan_interest_capitalisation",
        misconception_tags=["forgot_to_grow_principal_during_grace_period"],
        hints=[
            rf"First grow the principal using A = P(1+i)^{delay}.",
            rf"Then substitute the accumulated principal into the present value formula with n = {n_payments}.",
            f"Monthly payment is {ans}.",
        ],
        worked_solution=sol,
        diagram_spec=timeline,
        marks=4,
    )


def _b35_sinking_fund_lump_sum_initial_deposit_plus_annuity(rng: random.Random) -> Dict[str, Any]:
    target = 600000
    init_dep = rng.choice([50000, 80000, 100000])
    r = 10.0
    years = 5
    n = years * 12  # 60
    i = (r / 100) / 12

    # Initial deposit grows to init_dep * (1 + i)^n
    init_fv = init_dep * (1 + i)**n
    # Remainder needed from sinking fund annuity
    rem_target = target - init_fv
    x = rem_target * i / ((1 + i)**n - 1)
    ans = _fmt_zar(round(x, 2))

    prompt = (
        f"A transport company needs to accumulate {_fmt_zar(target)} in a sinking fund over 5 years ({n} months) "
        f"to replace a delivery truck. The fund earns 10% p.a. compounded monthly.\n"
        f"The company deposits an initial lump sum of {_fmt_zar(init_dep)} immediately into the fund, "
        f"and agrees to make regular monthly payments of $x$ starting one month later up to the end of the 5-year period.\n"
        f"Calculate the required monthly payment $x$."
    )
    sol = (
        f"1. The initial lump sum earns compound interest over the full 60 months:\n"
        f"$$FV_{{\\text{{lump}}}} = {_fmt_zar(init_dep)} \\times (1 + i)^{{60}} \\approx {_fmt_zar(round(init_fv, 2))}$$\n"
        f"2. The remaining amount that must be accumulated through monthly deposits:\n"
        f"$$\\text{{Remaining Target}} = {_fmt_zar(target)} - {_fmt_zar(round(init_fv, 2))} = {_fmt_zar(round(rem_target, 2))}$$\n"
        f"3. Calculate the monthly deposit $x$:\n"
        f"$$x = \\frac{{\\text{{Remaining Target}} \\times i}}{{(1 + i)^{{60}} - 1}} \\approx {ans}$$"
    )
    return _typed(
        subskill="35_sinking_fund_lump_sum_initial_deposit_plus_annuity",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{x:.2f}", f"{x:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-35",
        concept_id="sinking_fund_lump_sum_and_annuity",
        misconception_tags=["subtracted_initial_deposit_without_accumulating_interest"],
        hints=[
            "First compound the initial lump sum deposit over 60 months.",
            "Subtract that future value from the R600 000 target.",
            f"Solve for x in the FV formula using the remaining balance: {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


# ---------------------------------------------------------------------------
# Archetypes 36 - 50 (Retirement, Perpetuities, Vehicle Finance, Inflation & Synthesis)
# ---------------------------------------------------------------------------

def _b36_two_stage_retirement_accumulation_and_pension_drawdown(rng: random.Random) -> Dict[str, Any]:
    x_save = rng.choice([3000, 4000, 5000])
    r = 10.0
    i = (r / 100) / 12
    n_save = 300  # 25 years
    n_pension = 240  # 20 years

    # FV accumulated
    fv = x_save * ((1 + i)**n_save - 1) / i
    # Monthly pension payment from PV annuity of fv
    x_pension = fv * i / (1 - (1 + i)**(-n_pension))
    ans = _fmt_zar(round(x_pension, 2))

    timeline = _svg_timeline([
        ("T0", "Start Working", f"Save R{x_save}/m"),
        ("T300", "Retirement", f"Accumulated FV"),
        ("T540", "End of Pension", "Zero Balance"),
    ])

    prompt = (
        f"Refer to the timeline below. An individual saves {_fmt_zar(x_save)} at the end of each month for 25 years (300 months) "
        f"into a retirement annuity earning 10% p.a. compounded monthly.\n"
        f"Upon retiring at month 300, the full accumulated balance is transferred into a living annuity that continues to earn 10% p.a. compounded monthly.\n"
        f"The retiree intends to draw an equal monthly pension from the account for the next 20 years (240 months) until the balance reaches zero.\n"
        f"Calculate the monthly pension payment the retiree will receive."
    )
    sol = (
        f"1. Calculate accumulated retirement fund ($FV$) after 300 months:\n"
        f"$$FV = \\frac{{{x_save}\\left[(1 + i)^{{300}} - 1\\right]}}{{i}} \\approx {_fmt_zar(round(fv, 2))}$$\n"
        f"2. Use $FV$ as the present value $P_v$ for the 240-month pension drawdown:\n"
        f"$$P_v = \\frac{{x_{{\\text{{pension}}}}\\left[1 - (1 + i)^{{-240}}\\right]}}{{i}} \\implies x_{{\\text{{pension}}}} = \\frac{{{round(fv, 2)} \\times i}}{{1 - (1 + i)^{{-240}}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="36_two_stage_retirement_accumulation_and_pension_drawdown",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{x_pension:.2f}", f"{x_pension:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-36",
        concept_id="two_stage_retirement_annuity",
        misconception_tags=["used_fv_formula_for_pension_drawdown_stage"],
        hints=[
            "Step 1: Calculate the future value of the savings annuity over 300 months.",
            "Step 2: Use that lump sum as Pv in the present value annuity formula over 240 months.",
            f"Monthly pension is {ans}.",
        ],
        worked_solution=sol,
        diagram_spec=timeline,
        marks=5,
    )


def _b37_perpetuity_endowment_scholarship_fund(rng: random.Random) -> Dict[str, Any]:
    annual_scholarship = rng.choice([60000, 80000, 120000, 150000])
    r = rng.choice([8.0, 10.0, 12.0])
    i = r / 100
    p = round(annual_scholarship / i, 2)
    ans = _fmt_zar(p)

    prompt = (
        f"A philanthropic donor wishes to establish a university scholarship fund that will pay out "
        f"{_fmt_zar(annual_scholarship)} at the end of each year in perpetuity (forever).\n"
        f"The endowment investment fund earns a guaranteed {int(r)}\\% per annum compounded annually.\n"
        f"Calculate the lump-sum capital donation required today to endow this scholarship indefinitely."
    )
    dist = [
        _fmt_zar(round(p * 0.8, 2)),
        _fmt_zar(round(p * 1.25, 2)),
        _fmt_zar(round(annual_scholarship * 10, 2)),
    ]
    sol = (
        f"1. In a perpetuity where capital remains intact, the annual interest generated must equal the annual payout:\n"
        f"$$\\text{{Annual Interest}} = P \\times i = {annual_scholarship}$$\n"
        f"2. Solve for principal $P$:\n"
        f"$$P = \\frac{{{annual_scholarship}}}{{{i}}} = {ans}$$\n"
        f"3. Each year, {_fmt_zar(p)} generates exactly {_fmt_zar(annual_scholarship)} in interest, leaving the capital untouched forever."
    )
    return _mcq(
        rng,
        subskill="37_perpetuity_endowment_scholarship_fund",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-37",
        concept_id="perpetuity_capital_valuation",
        misconception_tags=["used_finite_n_annuity_formula"],
        hints=[
            "For a perpetuity, the annual payout equals the interest earned on the capital: P * i = Payout.",
            rf"Solve P = {annual_scholarship} / {i}.",
            f"The required donation is {ans}.",
        ],
        worked_solution=sol,
    )


def _b38_vehicle_finance_with_balloon_payment_residual(rng: random.Random) -> Dict[str, Any]:
    cash_price = rng.choice([300000, 350000, 400000])
    balloon_pct = rng.choice([20, 25, 30])
    balloon_val = cash_price * (balloon_pct / 100)
    r = 12.0
    i = (r / 100) / 12  # 0.01 per month
    n = 60  # 5 years

    # Cash price P = PV of annuity repayments + PV of balloon payment
    # P = x * [1 - (1+i)^-n]/i + balloon_val * (1+i)^-n
    pv_balloon = balloon_val * (1 + i)**(-n)
    pv_annuity = cash_price - pv_balloon
    x = pv_annuity * i / (1 - (1 + i)**(-n))
    ans = _fmt_zar(round(x, 2))

    prompt = (
        f"A buyer purchases a vehicle priced at {_fmt_zar(cash_price)} on a 5-year finance agreement (60 monthly payments).\n"
        f"The agreement includes a {balloon_pct}\\% balloon payment ({_fmt_zar(int(balloon_val))}) due at the end of the 5-year term.\n"
        f"Interest is charged at 12% p.a. compounded monthly.\n"
        f"Calculate the regular monthly installment $x$."
    )
    sol = (
        f"1. Discount the balloon payment back to present value ($T_0$):\n"
        f"$$PV_{{\\text{{balloon}}}} = {balloon_val} \\times (1{{,}}01)^{{-60}} \\approx {_fmt_zar(round(pv_balloon, 2))}$$\n"
        f"2. The remaining principal funded through monthly installments:\n"
        f"$$PV_{{\\text{{annuity}}}} = {_fmt_zar(cash_price)} - {_fmt_zar(round(pv_balloon, 2))} = {_fmt_zar(round(pv_annuity, 2))}$$\n"
        f"3. Calculate the monthly installment $x$:\n"
        f"$$x = \\frac{{{round(pv_annuity, 2)} \\times 0{{,}}01}}{{1 - (1{{,}}01)^{{-60}}}} \\approx {ans}$$"
    )
    return _typed(
        subskill="38_vehicle_finance_with_balloon_payment_residual",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{x:.2f}", f"{x:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-38",
        concept_id="balloon_payment_vehicle_financing",
        misconception_tags=["subtracted_balloon_directly_from_cash_price_without_discounting"],
        hints=[
            "Discount the balloon payment back to T0 using compound interest: Balloon * (1+i)^(-60).",
            "Subtract the discounted balloon value from the vehicle purchase price.",
            f"Solve for the monthly payment using the remaining loan principal: {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b39_break_even_depreciation_and_outstanding_loan_balance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"A company buys machinery for $R$ and finances 100% of the cost over 5 years." + "\n"
        r"The equipment depreciates on the reducing-balance method, while the loan is repaid via equal monthly installments." + "\n"
        r"In financial risk management, what is the term for the situation where the market value of the asset is **less** than the outstanding loan balance?"
    )
    ans = "Negative equity (or being in an 'underwater' / shortfall position)"
    dist = [
        "Positive amortised surplus",
        "Linear scrap salvage parity",
        "Sinking fund liquidity surplus",
    ]
    sol = (
        r"1. When an asset depreciates faster than the loan principal is amortised, the book/market value falls below the debt owed." + "\n"
        r"2. This financial shortfall position is termed **negative equity** (or being 'underwater')."
    )
    return _mcq(
        rng,
        subskill="39_break_even_depreciation_and_outstanding_loan_balance",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-39",
        concept_id="negative_equity_concept",
        misconception_tags=["confused_negative_equity_with_salvage_parity"],
        hints=[
            "Consider what happens when you owe more to the bank than what the car or machine is worth.",
            "This condition is known as negative equity or shortfall.",
            f"The correct term is: {ans}.",
        ],
        worked_solution=sol,
    )


def _b40_effective_annual_rate_comparison_credit_options(rng: random.Random) -> Dict[str, Any]:
    # Compare 12% compounded monthly vs 12.2% compounded semi-annually
    r_m = 12.0
    r_s = 12.2
    i_eff_m = (1 + (r_m / 100) / 12)**12 - 1
    i_eff_s = (1 + (r_s / 100) / 2)**2 - 1

    eff_m_pct = round(i_eff_m * 100, 2)
    eff_s_pct = round(i_eff_s * 100, 2)
    better = "Option A" if eff_m_pct > eff_s_pct else "Option B"
    diff = round(abs(eff_m_pct - eff_s_pct), 2)
    ans = f"{better} (Effective rate {_fmt_decimal_sa(max(eff_m_pct, eff_s_pct))}% vs {_fmt_decimal_sa(min(eff_m_pct, eff_s_pct))}%)"

    prompt = (
        f"An investor compares two fixed-deposit accounts:\n"
        f"- Option A: {int(r_m)}\\% p.a. compounded monthly\n"
        f"- Option B: {_fmt_decimal_sa(r_s)}\\% p.a. compounded semi-annually\n"
        f"Which option yields the higher effective annual return, and what are their respective effective rates?"
    )
    dist = [
        f"Option B (Effective rate 12{{,}}57% vs 12{{,}}68%)",
        f"Both have equal effective rate of 12{{,}}00%",
        f"Option A (Effective rate 12{{,}}00% vs 12{{,}}20%)",
    ]
    sol = (
        f"1. Effective rate for Option A ($m = 12$):\n"
        f"$$i_{{\\text{{eff}}}} = \\left(1 + \\frac{{0{{,}}12}}{{12}}\\right)^{{12}} - 1 = (1{{,}}01)^{{12}} - 1 \\approx {_fmt_decimal_sa(eff_m_pct)}\\%$$\n"
        f"2. Effective rate for Option B ($m = 2$):\n"
        f"$$i_{{\\text{{eff}}}} = \\left(1 + \\frac{{0{{,}}122}}{{2}}\\right)^{{2}} - 1 = (1{{,}}061)^{{2}} - 1 \\approx {_fmt_decimal_sa(eff_s_pct)}\\%$$\n"
        f"3. Since {_fmt_decimal_sa(eff_m_pct)}\\% > {_fmt_decimal_sa(eff_s_pct)}\\%, Option A yields the higher return."
    )
    return _mcq(
        rng,
        subskill="40_effective_annual_rate_comparison_credit_options",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-40",
        concept_id="comparative_effective_rate",
        misconception_tags=["compared_nominal_rates_directly_without_converting_to_effective"],
        hints=[
            "Convert both nominal rates into effective annual rates using (1 + i/m)^m - 1.",
            "Compare the two resulting annual percentages.",
            f"Option A effective rate is {_fmt_decimal_sa(eff_m_pct)}%.",
        ],
        worked_solution=sol,
    )


def _b41_purchasing_power_erosion_inflation_future_value(rng: random.Random) -> Dict[str, Any]:
    present_cost = rng.choice([100000, 200000, 500000])
    inflation = rng.choice([5.5, 6.0, 6.5])
    years = rng.choice([10, 15, 20])
    future_cost = round(present_cost * (1 + inflation / 100)**years, 2)
    ans = _fmt_zar(future_cost)

    prompt = (
        f"Due to inflation averaging {_fmt_decimal_sa(inflation)}\\% per annum, calculate how much an item that costs "
        f"{_fmt_zar(present_cost)} today will cost in {years} years' time."
    )
    sol = (
        f"1. Apply the compound growth formula with annual inflation rate $r = {_fmt_decimal_sa(inflation)}\\%$:\n"
        f"$$A = P(1 + i)^n = {present_cost} \\times \\left(1 + \\frac{{{inflation}}}{{100}}\\right)^{{{years}}}$$\n"
        f"2. $A \\approx {ans}$."
    )
    return _typed(
        subskill="41_purchasing_power_erosion_inflation_future_value",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{future_cost:.2f}", f"{future_cost:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-41",
        concept_id="inflation_cost_projection",
        misconception_tags=["used_simple_interest_for_multi_year_inflation"],
        hints=[
            "Use the compound inflation formula A = P(1 + i)^n.",
            rf"Substitute P = {present_cost}, i = {inflation/100}, n = {years}.",
            f"Future cost is {ans}.",
        ],
        worked_solution=sol,
    )


def _b42_straight_line_vs_reducing_balance_depreciation_crossover(rng: random.Random) -> Dict[str, Any]:
    p = 100000
    r_sl = 10.0
    r_rb = 15.0
    # After 3 years:
    # A_sl = P * (1 - 3 * 0.10) = 70 000
    # A_rb = P * (1 - 0.15)^3 = 100 000 * (0.85)^3 = 61 412.50
    sl_3 = p * (1 - 3 * (r_sl / 100))
    rb_3 = p * (1 - (r_rb / 100))**3
    diff = round(abs(sl_3 - rb_3), 2)
    ans = _fmt_zar(diff)

    prompt = (
        f"A piece of office equipment is bought for {_fmt_zar(p)}.\n"
        f"- Method 1: Straight-line depreciation at {int(r_sl)}\\% p.a.\n"
        f"- Method 2: Reducing-balance depreciation at {int(r_rb)}\\% p.a.\n"
        f"Calculate the difference in the book value of the equipment between the two methods at the end of 3 years."
    )
    sol = (
        f"1. Book value under straight-line depreciation after 3 years:\n"
        f"$$A_{{\\text{{SL}}}} = {p}(1 - 3 \\times 0{{,}}10) = {_fmt_zar(round(sl_3, 2))}$$\n"
        f"2. Book value under reducing-balance depreciation after 3 years:\n"
        f"$$A_{{\\text{{RB}}}} = {p}(1 - 0{{,}}15)^3 = {p}(0{{,}}85)^3 = {_fmt_zar(round(rb_3, 2))}$$\n"
        f"3. Difference in book values:\n"
        f"$$\\text{{Difference}} = {_fmt_zar(round(sl_3, 2))} - {_fmt_zar(round(rb_3, 2))} = {ans}$$"
    )
    return _typed(
        subskill="42_straight_line_vs_reducing_balance_depreciation_crossover",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{diff:.2f}", f"{diff:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-42",
        concept_id="comparative_depreciation_methods",
        misconception_tags=["confused_straight_line_and_reducing_balance_formulas"],
        hints=[
            "Calculate A_SL = P(1 - i*n).",
            "Calculate A_RB = P(1 - i)^n.",
            f"Find the difference between the two values: {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b43_loan_refinancing_lower_interest_rate_new_installment(rng: random.Random) -> Dict[str, Any]:
    bal = rng.choice([400000, 500000, 600000])
    r_old = 11.5
    r_new = 9.5
    years = 10
    n = years * 12  # 120
    i_old = (r_old / 100) / 12
    i_new = (r_new / 100) / 12

    x_old = bal * i_old / (1 - (1 + i_old)**(-n))
    x_new = bal * i_new / (1 - (1 + i_new)**(-n))
    monthly_saving = round(x_old - x_new, 2)
    ans = _fmt_zar(monthly_saving)

    prompt = (
        f"A business owner has an outstanding loan balance of {_fmt_zar(bal)} with 10 years (120 months) remaining at "
        f"{_fmt_decimal_sa(r_old)}\\% p.a. compounded monthly.\n"
        f"The owner refinances the loan with another lender at a reduced rate of {_fmt_decimal_sa(r_new)}\\% p.a. compounded monthly "
        f"over the same 10-year remaining period.\n"
        f"Calculate the monthly saving in the installment payment."
    )
    sol = (
        f"1. Current installment at {_fmt_decimal_sa(r_old)}\\% p.a.:\n"
        f"$$x_{{\\text{{old}}}} = \\frac{{{bal} \\times i_{{\\text{{old}}}}}}{{1 - (1 + i_{{\\text{{old}}}})^{{-120}}}} \\approx {_fmt_zar(round(x_old, 2))}$$\n"
        f"2. New installment at {_fmt_decimal_sa(r_new)}\\% p.a.:\n"
        f"$$x_{{\\text{{new}}}} = \\frac{{{bal} \\times i_{{\\text{{new}}}}}}{{1 - (1 + i_{{\\text{{new}}}})^{{-120}}}} \\approx {_fmt_zar(round(x_new, 2))}$$\n"
        f"3. Monthly savings $= {_fmt_zar(round(x_old, 2))} - {_fmt_zar(round(x_new, 2))} = {ans}$."
    )
    return _typed(
        subskill="43_loan_refinancing_lower_interest_rate_new_installment",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{monthly_saving:.2f}", f"{monthly_saving:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-43",
        concept_id="loan_refinance_installment_reduction",
        misconception_tags=["calculated_total_lifetime_saving_instead_of_monthly_saving"],
        hints=[
            "Compute monthly payment under the old rate.",
            "Compute monthly payment under the new refinanced rate.",
            f"The monthly saving is {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b44_lump_sum_capital_reduction_midway_recalculated_term(rng: random.Random) -> Dict[str, Any]:
    p = 500000
    r = 12.0
    i = (r / 100) / 12  # 0.01 per month
    n_orig = 240
    x = p * i / (1 - (1 + i)**(-n_orig))
    # After 60 months, balance:
    bal_60 = p * (1 + i)**60 - x * ((1 + i)**60 - 1) / i
    lump_sum = rng.choice([50000, 100000])
    new_bal = bal_60 - lump_sum
    # Solve for remaining n with same payment x
    term = 1 - (new_bal * i) / x
    rem_n = math.ceil(-math.log(term) / math.log(1 + i))

    ans = f"{rem_n} months"
    dist = [
        f"{rem_n + 36} months",
        f"{rem_n - 24} months",
        f"180 months",
    ]
    sol = (
        f"1. Balance after 60 payments of {_fmt_zar(round(x, 2))}:\n"
        f"$$\\text{{Balance}}_{{60}} \\approx {_fmt_zar(round(bal_60, 2))}$$\n"
        f"2. Reduce balance by the lump sum of {_fmt_zar(lump_sum)}:\n"
        f"$$\\text{{New Balance}} = {_fmt_zar(round(bal_60, 2))} - {_fmt_zar(lump_sum)} = {_fmt_zar(round(new_bal, 2))}$$\n"
        f"3. Solve for remaining months $n$ with installment $x = {_fmt_zar(round(x, 2))}$:\n"
        f"$$1 - \\frac{{{round(new_bal, 2)} \\times 0{{,}}01}}{{{round(x, 2)}}} = (1{{,}}01)^{{-n}} \\implies n \\approx {rem_n}\\text{{ months}}$."
    )
    return _mcq(
        rng,
        subskill="44_lump_sum_capital_reduction_midway_recalculated_term",
        prompt=(
            f"A homeowner owes {_fmt_zar(p)} on a 20-year bond at 12% p.a. compounded monthly (installment {_fmt_zar(round(x, 2))}).\n"
            f"After 5 years (60 payments), the homeowner pays an unexpected inheritance lump sum of {_fmt_zar(lump_sum)} directly into the loan account.\n"
            f"If the monthly payment remains unchanged, how many more months will it take to pay off the remaining loan balance?"
        ),
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-44",
        concept_id="capital_reduction_term_shortening",
        misconception_tags=["subtracted_lump_sum_from_initial_principal"],
        hints=[
            "Find the balance after 60 months, then subtract the lump sum.",
            "Use the new reduced balance as Pv and solve for n using logarithms.",
            f"Remaining term is {ans}.",
        ],
        worked_solution=sol,
    )


def _b45_deposit_calculation_to_meet_debt_to_income_ratio(rng: random.Random) -> Dict[str, Any]:
    house_price = rng.choice([1200000, 1500000, 1800000])
    gross_income = rng.choice([35000, 45000, 50000])
    max_payment = gross_income * 0.30  # 30% rule
    r = 10.5
    i = (r / 100) / 12
    n = 240  # 20 years

    # Max loan affordable
    max_loan = max_payment * (1 - (1 + i)**(-n)) / i
    min_deposit = max(0.0, round(house_price - max_loan, 2))
    ans = _fmt_zar(min_deposit)

    prompt = (
        f"A family with a combined gross monthly income of {_fmt_zar(gross_income)} wants to buy a home priced at {_fmt_zar(house_price)}.\n"
        f"Banks require that the monthly bond repayment cannot exceed 30% of gross monthly income.\n"
        f"The interest rate is {_fmt_decimal_sa(r)}\\% p.a. compounded monthly over 20 years (240 months).\n"
        f"Calculate the **minimum cash deposit** the family must pay upfront to qualify for the loan."
    )
    sol = (
        f"1. Maximum allowable monthly repayment (30% of income):\n"
        f"$$x_{{\\text{{max}}}} = 0{{,}}30 \\times {_fmt_zar(gross_income)} = {_fmt_zar(round(max_payment, 2))}$$\n"
        f"2. Maximum loan principal the bank will grant:\n"
        f"$$P_{{\\text{{max}}}} = \\frac{{{round(max_payment, 2)}\\left[1 - (1 + i)^{{-240}}\\right]}}{{i}} \\approx {_fmt_zar(round(max_loan, 2))}$$\n"
        f"3. Minimum cash deposit required:\n"
        f"$$\\text{{Deposit}} = \\text{{House Price}} - P_{{\\text{{max}}}} = {_fmt_zar(house_price)} - {_fmt_zar(round(max_loan, 2))} = {ans}$$"
    )
    return _typed(
        subskill="45_deposit_calculation_to_meet_debt_to_income_ratio",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{min_deposit:.2f}", f"{min_deposit:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-45",
        concept_id="debt_to_income_deposit_calculation",
        misconception_tags=["confused_max_loan_with_min_deposit"],
        hints=[
            "Find the maximum monthly repayment: 30% of gross monthly income.",
            "Calculate the maximum loan amount affordable with that payment over 240 months.",
            f"Subtract the maximum loan from the purchase price: {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b46_sinking_fund_interest_rate_drop_shortfall_analysis(rng: random.Random) -> Dict[str, Any]:
    target = 500000
    r_planned = 10.0
    r_actual = 8.0
    years = 5
    n = 60
    i_plan = (r_planned / 100) / 12
    i_act = (r_actual / 100) / 12

    # Monthly deposit planned
    x = target * i_plan / ((1 + i_plan)**n - 1)
    # Actual FV achieved with x at r_actual
    fv_actual = x * ((1 + i_act)**n - 1) / i_act
    shortfall = round(target - fv_actual, 2)
    ans = _fmt_zar(shortfall)

    prompt = (
        f"A firm sets up a sinking fund to accumulate {_fmt_zar(target)} in 5 years ({n} months).\n"
        f"The monthly deposit of {_fmt_zar(round(x, 2))} was calculated assuming an interest rate of {int(r_planned)}\\% p.a. compounded monthly.\n"
        f"However, interest rates fell and the fund earned only {int(r_actual)}\\% p.a. compounded monthly over the entire 5 years.\n"
        f"Calculate the **shortfall** in the fund at the end of the 5-year period."
    )
    sol = (
        f"1. Planned monthly deposit: $x = {_fmt_zar(round(x, 2))}$.\n"
        f"2. Actual future value accumulated at lower rate $i_{{\\text{{act}}}} = \\frac{{0{{,}}08}}{{12}}$:\n"
        f"$$FV_{{\\text{{actual}}}} = \\frac{{{round(x, 2)}\\left[(1 + i_{{\\text{{act}}}})^{{60}} - 1\\right]}}{{i_{{\\text{{act}}}}}} \\approx {_fmt_zar(round(fv_actual, 2))}$$\n"
        f"3. Shortfall $= {_fmt_zar(target)} - {_fmt_zar(round(fv_actual, 2))} = {ans}$."
    )
    return _typed(
        subskill="46_sinking_fund_interest_rate_drop_shortfall_analysis",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{shortfall:.2f}", f"{shortfall:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-46",
        concept_id="sinking_fund_shortfall_variance",
        misconception_tags=["calculated_shortfall_as_percentage_rather_than_monetary_amount"],
        hints=[
            "Calculate the actual FV accumulated using the planned payment at the lower 8% rate.",
            "Subtract the actual FV from the R500 000 target.",
            f"The shortfall is {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b47_pension_drawdown_solve_number_of_monthly_payouts(rng: random.Random) -> Dict[str, Any]:
    lump = 1000000
    payout = rng.choice([12000, 15000])
    r = 9.0
    i = (r / 100) / 12  # 0.0075 per month

    # P = payout * [1 - (1+i)^-n] / i => 1 - P*i/payout = (1+i)^-n
    term = 1 - (lump * i) / payout
    n_exact = -math.log(term) / math.log(1 + i)
    n_floor = math.floor(n_exact)

    ans = f"{n_floor} full payouts"
    dist = [
        f"{n_floor + 24} full payouts",
        f"{n_floor - 12} full payouts",
        f"120 full payouts",
    ]
    sol = (
        f"1. Set up present value equation for capital {_fmt_zar(lump)} paying {_fmt_zar(payout)} monthly at $i = 0{{,}}0075$:\n"
        f"$$1 - \\frac{{{lump} \\times 0{{,}}0075}}{{{payout}}} = (1{{,}}0075)^{{-n}} \\implies (1{{,}}0075)^{{-n}} = {round(term, 4)}$$\n"
        f"2. Solve for $n$ using logarithms:\n"
        f"$$-n = \\frac{{\\ln({round(term, 4)})}}{{\\ln(1{{,}}0075)}} \\approx {-round(n_exact, 2)} \\implies n \\approx {round(n_exact, 2)}$$\n"
        f"3. The fund will provide {n_floor} full monthly payouts (with a smaller final payout in month {n_floor + 1})."
    )
    return _mcq(
        rng,
        subskill="47_pension_drawdown_solve_number_of_monthly_payouts",
        prompt=(
            f"A retiree invests a lump sum of {_fmt_zar(lump)} into an account earning 9% p.a. compounded monthly.\n"
            f"If the retiree draws a fixed monthly pension of {_fmt_zar(payout)}, how many **full monthly payouts** will the fund support before it is exhausted?"
        ),
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-47",
        concept_id="pension_drawdown_duration_logarithm",
        misconception_tags=["rounded_up_instead_of_identifying_full_payouts"],
        hints=[
            "Use the present value formula with Pv = R1 000 000 and x = monthly payout.",
            "Solve for n using logarithms: -n = ln(1 - P*i/x) / ln(1+i).",
            f"Take the integer floor: {ans}.",
        ],
        worked_solution=sol,
    )


def _b48_loan_amortization_percentage_equity_after_half_term(rng: random.Random) -> Dict[str, Any]:
    p = 1000000
    r = 12.0
    i = (r / 100) / 12  # 0.01 per month
    n = 240  # 20 years
    half_n = 120
    x = p * i / (1 - (1 + i)**(-n))
    # Balance after 120 payments
    bal_120 = x * (1 - (1 + i)**(-(n - half_n))) / i
    equity = p - bal_120
    pct_equity = round((equity / p) * 100, 1)
    ans = f"{_fmt_decimal_sa(pct_equity)}%"

    prompt = (
        f"A homeowner repays a 20-year bond of {_fmt_zar(p)} at 12% p.a. compounded monthly (installment {_fmt_zar(round(x, 2))}).\n"
        f"Calculate the percentage of the original loan principal that has been paid off (homeowner's equity) after exactly 10 years (halfway through the term)."
    )
    dist = [
        "50{,}0%",
        "25{,}0%",
        "40{,}0%",
    ]
    sol = (
        f"1. Outstanding balance after 120 months (120 payments remaining):\n"
        f"$$\\text{{Balance}}_{{120}} = \\frac{{{round(x, 2)}\\left[1 - (1{{,}}01)^{{-120}}\\right]}}{{0{{,}}01}} \\approx {_fmt_zar(round(bal_120, 2))}$$\n"
        f"2. Principal paid off (Equity) $= {_fmt_zar(p)} - {_fmt_zar(round(bal_120, 2))} = {_fmt_zar(round(equity, 2))}$.\n"
        f"3. Percentage of principal paid off $= \\frac{{{round(equity, 2)}}}{{{p}}} \\times 100\\% \\approx {_fmt_decimal_sa(pct_equity)}\\%$.\n"
        f"(Notice that halfway through a 20-year loan, far less than 50% of the principal is paid off due to heavy early interest charges!)"
    )
    return _mcq(
        rng,
        subskill="48_loan_amortization_percentage_equity_after_half_term",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-48",
        concept_id="amortization_equity_curve",
        misconception_tags=["assumed_50_percent_of_principal_paid_at_halfway_mark"],
        hints=[
            "Calculate the remaining balance using the backward method with n = 120.",
            "Subtract the balance from R1 000 000 to find the principal repaid.",
            f"Divide by R1 000 000 and multiply by 100%: {_fmt_decimal_sa(pct_equity)}%.",
        ],
        worked_solution=sol,
    )


def _b49_capstone_sinking_fund_trade_in_and_residual_loan(rng: random.Random) -> Dict[str, Any]:
    old_cost = rng.choice([350000, 400000, 450000, 500000])
    r_dep = rng.choice([15.0, 18.0, 20.0])
    r_inf = rng.choice([6.0, 7.0, 8.0])
    years = 4
    n = years * 12  # 48
    i_fund = (9.0 / 100) / 12

    # Trade in value (scrap)
    scrap = old_cost * (1 - r_dep / 100)**years
    # New truck cost with inflation
    new_cost = old_cost * (1 + r_inf / 100)**years
    # Sinking fund target = new_cost - scrap
    fund_target = new_cost - scrap
    x = fund_target * i_fund / ((1 + i_fund)**n - 1)
    ans = _fmt_zar(round(x, 2))

    timeline = _svg_timeline([
        ("T0", "Old Vehicle Bought", f"R{old_cost:,}"),
        ("T48", "Trade-in & Replacement", f"Fund: {_fmt_zar(round(fund_target, 2))}"),
    ])

    prompt = (
        f"Refer to the timeline below. A courier company bought a fleet vehicle 4 years ago for {_fmt_zar(old_cost)}.\n"
        f"The company intends to trade in the old vehicle at its book value depreciated at {int(r_dep)}\\% p.a. on the reducing-balance method,\n"
        f"and buy a new replacement vehicle whose cost has inflated at {int(r_inf)}\\% p.a. over the 4 years.\n"
        f"The company set up a sinking fund 4 years ago earning 9% p.a. compounded monthly to cover the net replacement shortfall.\n"
        f"Calculate the monthly sinking fund deposit that was made over the 48 months."
    )
    sol = (
        f"1. Trade-in value (Scrap value) after 4 years:\n"
        f"$$\\text{{Scrap}} = {old_cost}(1 - 0{{,}}18)^4 \\approx {_fmt_zar(round(scrap, 2))}$$\n"
        f"2. Cost of new vehicle after 4 years of inflation:\n"
        f"$$\\text{{New Cost}} = {old_cost}(1 + 0{{,}}07)^4 \\approx {_fmt_zar(round(new_cost, 2))}$$\n"
        f"3. Sinking fund target $= \\text{{New Cost}} - \\text{{Scrap}} \\approx {_fmt_zar(round(fund_target, 2))}$.\n"
        f"4. Monthly deposit $x$:\n"
        f"$$x = \\frac{{{round(fund_target, 2)} \\times i}}{{(1 + i)^{{48}} - 1}} \\approx {ans}$$"
    )
    return _typed(
        subskill="49_capstone_sinking_fund_trade_in_and_residual_loan",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, f"{x:.2f}", f"{x:.2f}".replace(".", ",")],
        learning_objective_id="G12-MATH-FIN-49",
        concept_id="sinking_fund_capstone_synthesis",
        misconception_tags=["forgot_to_subtract_trade_in_value_from_new_cost"],
        hints=[
            "Calculate scrap value using reducing-balance depreciation: P(1-i)^4.",
            "Calculate replacement cost using inflation: P(1+i)^4.",
            f"Subtract scrap from new cost to find fund target, then solve for x: {ans}.",
        ],
        worked_solution=sol,
        diagram_spec=timeline,
        marks=6,
    )


def _b50_capstone_retirement_annuity_drawdown_and_bequest(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"A comprehensive retirement plan consists of two distinct financial phases:" + "\n"
        r"Phase 1: Accumulating wealth via regular monthly contributions into an account earning compound interest (Future Value Annuity)." + "\n"
        r"Phase 2: Drawing an equal monthly income from the accumulated capital over retirement until death or a planned bequest (Present Value Annuity)." + "\n"
        r"Which combination of financial formulas correctly models Phase 1 and Phase 2 respectively?"
    )
    ans = r"Phase 1: $F_v = \frac{x\left[(1+i)^n - 1\right]}{i}$ \quad and \quad Phase 2: $P_v = \frac{x\left[1 - (1+i)^{-n}\right]}{i}$"
    dist = [
        r"Phase 1: $P_v = \frac{x\left[1 - (1+i)^{-n}\right]}{i}$ \quad and \quad Phase 2: $F_v = \frac{x\left[(1+i)^n - 1\right]}{i}$",
        r"Phase 1: $A = P(1+i)^n$ \quad and \quad Phase 2: $A = P(1-in)$",
        r"Phase 1: $F_v = \frac{x\left[(1+i)^n - 1\right]}{i}$ \quad and \quad Phase 2: $A = P(1+i)^n$",
    ]
    sol = (
        r"1. **Phase 1 (Wealth Accumulation)**: Regular deposits build up to a larger future amount $\implies$ Future Value Annuity $F_v = \frac{x\left[(1+i)^n - 1\right]}{i}$." + "\n"
        r"2. **Phase 2 (Income Drawdown)**: A lump sum is disbursed in regular monthly payments over time $\implies$ Present Value Annuity $P_v = \frac{x\left[1 - (1+i)^{-n}\right]}{i}$."
    )
    return _mcq(
        rng,
        subskill="50_capstone_retirement_annuity_drawdown_and_bequest",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-FIN-50",
        concept_id="retirement_annuity_synthesis",
        misconception_tags=["inverted_future_value_and_present_value_models"],
        hints=[
            "Phase 1 accumulates money over time using equal deposits (Future Value).",
            "Phase 2 pays out an income from an existing capital sum (Present Value).",
            "Select the option with FV for Phase 1 and PV for Phase 2.",
        ],
        worked_solution=sol,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_derivation_future_value_geometric_series": _b26_derivation_future_value_geometric_series,
    "27_derivation_present_value_geometric_series": _b27_derivation_present_value_geometric_series,
    "28_fv_annuity_interest_rate_increase_two_stages": _b28_fv_annuity_interest_rate_increase_two_stages,
    "29_home_loan_interest_rate_hike_new_installment": _b29_home_loan_interest_rate_hike_new_installment,
    "30_accelerated_loan_repayment_extra_monthly_amount": _b30_accelerated_loan_repayment_extra_monthly_amount,
    "31_total_interest_saved_accelerated_loan_repayment": _b31_total_interest_saved_accelerated_loan_repayment,
    "32_total_interest_paid_over_loan_lifetime": _b32_total_interest_paid_over_loan_lifetime,
    "33_amortization_split_principal_interest_payment_k": _b33_amortization_split_principal_interest_payment_k,
    "34_deferred_loan_payments_grace_period_interest_capitalised": _b34_deferred_loan_payments_grace_period_interest_capitalised,
    "35_sinking_fund_lump_sum_initial_deposit_plus_annuity": _b35_sinking_fund_lump_sum_initial_deposit_plus_annuity,
    "36_two_stage_retirement_accumulation_and_pension_drawdown": _b36_two_stage_retirement_accumulation_and_pension_drawdown,
    "37_perpetuity_endowment_scholarship_fund": _b37_perpetuity_endowment_scholarship_fund,
    "38_vehicle_finance_with_balloon_payment_residual": _b38_vehicle_finance_with_balloon_payment_residual,
    "39_break_even_depreciation_and_outstanding_loan_balance": _b39_break_even_depreciation_and_outstanding_loan_balance,
    "40_effective_annual_rate_comparison_credit_options": _b40_effective_annual_rate_comparison_credit_options,
    "41_purchasing_power_erosion_inflation_future_value": _b41_purchasing_power_erosion_inflation_future_value,
    "42_straight_line_vs_reducing_balance_depreciation_crossover": _b42_straight_line_vs_reducing_balance_depreciation_crossover,
    "43_loan_refinancing_lower_interest_rate_new_installment": _b43_loan_refinancing_lower_interest_rate_new_installment,
    "44_lump_sum_capital_reduction_midway_recalculated_term": _b44_lump_sum_capital_reduction_midway_recalculated_term,
    "45_deposit_calculation_to_meet_debt_to_income_ratio": _b45_deposit_calculation_to_meet_debt_to_income_ratio,
    "46_sinking_fund_interest_rate_drop_shortfall_analysis": _b46_sinking_fund_interest_rate_drop_shortfall_analysis,
    "47_pension_drawdown_solve_number_of_monthly_payouts": _b47_pension_drawdown_solve_number_of_monthly_payouts,
    "48_loan_amortization_percentage_equity_after_half_term": _b48_loan_amortization_percentage_equity_after_half_term,
    "49_capstone_sinking_fund_trade_in_and_residual_loan": _b49_capstone_sinking_fund_trade_in_and_residual_loan,
    "50_capstone_retirement_annuity_drawdown_and_bequest": _b50_capstone_retirement_annuity_drawdown_and_bequest,
}
