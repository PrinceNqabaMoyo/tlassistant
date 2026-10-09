"""Grade 10 Mathematics — Term 3: Finance and Growth (Deterministic 6-Pillar Generator).
100% aligned with South African CAPS Curriculum (Grade 10 Mathematics Paper 1: Finance).
Covers:
- Simple interest: A = P(1 + in)
- Compound interest: A = P(1 + i)^n
- Hire purchase agreements: deposit, principal loan, simple interest over term, monthly instalments
- Foreign currency exchange conversions with South African Rand (ZAR)

Zero-LLM: 100% deterministic Python calculations with South African comma decimals ({,}).
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "Finance and growth"
TOPIC_ID = "grade10_math_finance"
LO = "math10_finance_growth"

SA_NAMES = ["Bongani", "Nomsa", "Thabo", "Lerato", "Sipho", "Zanele", "Kagiso", "Nandi", "Andile", "Mpho"]
PURCHASES = ["laptop computer", "refrigerator", "lounge suite", "television set", "solar inverter system"]
CURRENCIES = [
    ("US Dollar (USD)", "$", 18.50),
    ("British Pound (GBP)", "£", 23.40),
    ("Euro (EUR)", "€", 19.80),
]


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return f"{val:.{places}f}".replace(".", ",")


def _build_simple_vs_compound_drill(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(5, 30) * 1000  # R5 000 to R30 000
    n_years = r.randint(2, 6)
    rate_percent = r.choice([6.5, 7.0, 8.0, 8.5, 9.0, 10.0, 11.5])
    i_dec = rate_percent / 100.0

    is_compound = r.choice([True, False])
    p_str = f"{p_val:,}".replace(",", " ")
    rate_str = _fmt_sa(rate_percent, 1)

    if is_compound:
        a_val = p_val * ((1.0 + i_dec) ** n_years)
        ans_round = round(a_val, 2)
        ans_str = f"R {_fmt_sa(ans_round, 2)}"

        prompt = (
            rf"{name} invests R {p_str} in a fixed deposit account earning interest at "
            rf"{rate_str}\% per annum compounded annually for {n_years} years."
            rf"\n\nCalculate the total accumulated amount in the account at the end of the investment period. "
            rf"Round off your answer to TWO decimal places."
        )

        worked = (
            rf"**Formula:** $A = P(1 + i)^n$"
            rf"\n\n**Substitution:** $A = {p_str}\left(1 + \frac{{{rate_str}}}{{100}}\right)^{{{n_years}}}$"
            rf"\n\n**Calculation:** $A = {p_str}(1 + {_fmt_sa(i_dec, 4)})^{{{n_years}}} = \text{{R }} {_fmt_sa(ans_round, 2)}$"
        )

        return {
            "id": f"g10_fin_comp_{r.randint(100000, 999999)}",
            "question_type": "typed",
            "prompt": prompt,
            "prompt_latex": prompt,
            "answer_mode": "text",
            "correct_answer": ans_str,
            "answer_latex": ans_str,
            "worked_solution": worked,
            "marks": 3,
            "topic": TOPIC,
            "topic_id": TOPIC_ID,
            "learning_objective_id": LO,
            "subskill": "compound_interest",
            "term": 3,
            "caps_weight_percent": 10,
            "suggested_duration_mins": 4,
            "difficulty": "medium",
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": "Correct compound interest formula A = P(1+i)^n", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Accurate substitution of P, i, n", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Correct final accumulated amount ({ans_str})", "marks": 1, "editable": True},
                ],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hint_sections": {
                "1_nudge": "Use the compound interest formula $A = P(1 + i)^n$.",
                "2_concept": "Compound interest earns interest on interest; $P$ is principal and $n$ is years.",
                "3_breakdown": rf"Substitute: $A = {p_str}(1 + {_fmt_sa(i_dec, 4)})^{{{n_years}}} = {ans_str}$.",
            },
            "misconception_tags": ["simple_vs_compound_confusion", "rounding_error"],
        }
    else:
        a_val = p_val * (1.0 + i_dec * n_years)
        ans_round = round(a_val, 2)
        ans_str = f"R {_fmt_sa(ans_round, 2)}"

        prompt = (
            rf"{name} invests R {p_str} in a simple savings account paying "
            rf"{rate_str}\% simple interest per annum for {n_years} years."
            rf"\n\nCalculate the total accumulated amount at the end of {n_years} years."
        )

        worked = (
            rf"**Formula:** $A = P(1 + in)$"
            rf"\n\n**Substitution:** $A = {p_str}\left(1 + \left(\frac{{{rate_str}}}{{100}}\right)({n_years})\right)$"
            rf"\n\n**Calculation:** $A = {p_str}(1 + {_fmt_sa(round(i_dec * n_years, 4), 4)}) = \text{{R }} {_fmt_sa(ans_round, 2)}$"
        )

        return {
            "id": f"g10_fin_simp_{r.randint(100000, 999999)}",
            "question_type": "typed",
            "prompt": prompt,
            "prompt_latex": prompt,
            "answer_mode": "text",
            "correct_answer": ans_str,
            "answer_latex": ans_str,
            "worked_solution": worked,
            "marks": 3,
            "topic": TOPIC,
            "topic_id": TOPIC_ID,
            "learning_objective_id": LO,
            "subskill": "simple_interest",
            "term": 3,
            "caps_weight_percent": 10,
            "suggested_duration_mins": 3,
            "difficulty": "easy",
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": "Correct simple interest formula A = P(1+in)", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Accurate substitution of P, i, n", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Correct final accumulated amount ({ans_str})", "marks": 1, "editable": True},
                ],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hint_sections": {
                "1_nudge": "Use the simple interest formula $A = P(1 + in)$.",
                "2_concept": "Simple interest is calculated only on the original principal amount.",
                "3_breakdown": rf"Substitute: $A = {p_str}(1 + ({_fmt_sa(i_dec, 4)})({n_years})) = {ans_str}$.",
            },
            "misconception_tags": ["simple_interest_formula_error"],
        }


def _build_hire_purchase_drill(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    item = r.choice(PURCHASES)
    cash_price = r.randint(8, 25) * 1000
    deposit_pct = r.choice([10, 15, 20])
    interest_rate = r.choice([12.0, 14.0, 15.0, 16.5])
    years = r.choice([2, 3, 4])
    months = years * 12

    deposit_amt = round(cash_price * (deposit_pct / 100.0), 2)
    p_loan = cash_price - deposit_amt
    i_dec = interest_rate / 100.0
    total_repaid = round(p_loan * (1.0 + i_dec * years), 2)
    monthly_instalment = round(total_repaid / months, 2)

    prompt = (
        rf"{name} buys a {item} on a hire purchase agreement. "
        rf"The cash price is R {cash_price:,}. "
        rf"The agreement requires a {deposit_pct}\% cash deposit upfront, and the balance is financed "
        rf"at a simple interest rate of {_fmt_sa(interest_rate, 1)}\% per annum over {years} years ({months} months)."
        rf"\n\n"
        rf"1. Calculate the deposit paid in Rand."
        rf"\n"
        rf"2. Calculate the loan amount financed."
        rf"\n"
        rf"3. Calculate the monthly instalment payable."
    ).replace(",", " ")

    worked = (
        rf"**1. Deposit:** $\text{{Deposit}} = \text{{R }} {cash_price:,} \times {deposit_pct}\% = \text{{R }} {_fmt_sa(deposit_amt, 2)}$"
        rf"\n\n**2. Loan Balance:** $P = \text{{R }} {cash_price:,} - \text{{R }} {_fmt_sa(deposit_amt, 2)} = \text{{R }} {_fmt_sa(p_loan, 2)}$"
        rf"\n\n**3. Total Repayment:** $A = P(1 + in) = {_fmt_sa(p_loan, 2)}(1 + ({_fmt_sa(i_dec, 4)})({years})) = \text{{R }} {_fmt_sa(total_repaid, 2)}$"
        rf"\n\n**Monthly Instalment:** $\frac{{{_fmt_sa(total_repaid, 2)}}}{{{months}}} = \text{{R }} {_fmt_sa(monthly_instalment, 2)}$"
    ).replace(",", " ")

    return {
        "id": f"g10_fin_hp_{r.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"Deposit: R {_fmt_sa(deposit_amt, 2)}, Loan: R {_fmt_sa(p_loan, 2)}, Monthly: R {_fmt_sa(monthly_instalment, 2)}",
        "answer_latex": rf"\text{{Deposit: R }} {_fmt_sa(deposit_amt, 2)}, \text{{ Loan: R }} {_fmt_sa(p_loan, 2)}, \text{{ Monthly: R }} {_fmt_sa(monthly_instalment, 2)}",
        "worked_solution": worked,
        "marks": 6,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "hire_purchase",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "difficulty": "hard",
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": f"Deposit calculation (R {_fmt_sa(deposit_amt, 2)})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Loan principal P = Price - Deposit (R {_fmt_sa(p_loan, 2)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Total repayment using A = P(1+in) (R {_fmt_sa(total_repaid, 2)})", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": f"Monthly instalment calculation (R {_fmt_sa(monthly_instalment, 2)})", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "First calculate the deposit, then subtract it to find the loan principal $P$.",
            "2_concept": "Hire purchase agreements ALWAYS use simple interest $A = P(1 + in)$ on the unpaid balance.",
            "3_breakdown": rf"Deposit = R {_fmt_sa(deposit_amt, 2)}, Balance = R {_fmt_sa(p_loan, 2)}, Total = R {_fmt_sa(total_repaid, 2)}, Monthly = R {_fmt_sa(monthly_instalment, 2)}.",
        },
        "misconception_tags": ["hire_purchase_deposit_omitted", "hire_purchase_compound_error"],
    }


def _build_exchange_rate_drill(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    curr_name, symbol, base_rate = r.choice(CURRENCIES)
    rate = round(base_rate + r.choice([-0.8, -0.4, 0.0, 0.3, 0.7]), 2)
    foreign_amt = r.randint(50, 400) * 10
    rand_amt = round(foreign_amt * rate, 2)

    prompt = (
        rf"{name} travels abroad and converts {symbol} {foreign_amt:,} ({curr_name}) into South African Rand (ZAR). "
        rf"The exchange rate is {symbol} 1 = R {_fmt_sa(rate, 2)}."
        rf"\n\nCalculate the amount in South African Rand {name} receives."
    ).replace(",", " ")

    ans_str = f"R {_fmt_sa(rand_amt, 2)}"
    worked = rf"$$\text{{Amount in ZAR}} = {foreign_amt} \times {_fmt_sa(rate, 2)} = \text{{R }} {_fmt_sa(rand_amt, 2)}$$"

    return {
        "id": f"g10_fin_fx_{r.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans_str,
        "answer_latex": ans_str,
        "worked_solution": worked,
        "marks": 2,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "exchange_rates",
        "term": 3,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 2,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Method: Multiply foreign currency by exchange rate", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Accuracy: {ans_str}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Multiply foreign currency by the exchange rate in Rands.",
            "2_concept": "Rand value = Foreign amount x Exchange rate.",
            "3_breakdown": rf"Multiply: {foreign_amt} x {_fmt_sa(rate, 2)} = {ans_str}.",
        },
        "misconception_tags": ["currency_conversion_inversion"],
    }


def generate(subskill: Optional[str] = None, difficulty: str = "medium", count: int = 1, seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    r = _rng(seed)
    generators = [_build_simple_vs_compound_drill, _build_hire_purchase_drill, _build_exchange_rate_drill]
    if subskill in ("simple_interest", "compound_interest"):
        generators = [_build_simple_vs_compound_drill]
    elif subskill == "hire_purchase":
        generators = [_build_hire_purchase_drill]
    elif subskill == "exchange_rates":
        generators = [_build_exchange_rate_drill]

    questions = []
    for _ in range(count):
        gen_fn = r.choice(generators)
        questions.append(gen_fn(r))
    return questions
