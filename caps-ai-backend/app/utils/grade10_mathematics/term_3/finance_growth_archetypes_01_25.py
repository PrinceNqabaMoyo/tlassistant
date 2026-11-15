"""Grade 10 Mathematics — Term 3: Finance and Growth (Archetypes 01 to 25).

Grounded strictly in curriculum_docs_auto/Mathematics_Gr10/Term 3/01. Finance and growth.md.
Deterministic SymPy / math calculations with authentic South African Rand (R) and comma decimals ({,}).
Zero-LLM, 100% curriculum aligned.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

TOPIC_NAME = "Finance and growth"
TOPIC_ID = "grade10_math_finance"
SUBTOPIC_ID = "term3_finance_growth"

SA_NAMES = [
    "Sipho", "Nandi", "Thabo", "Lerato", "Kagiso", "Zanele", "Bongani", "Nomsa",
    "Mpho", "Andile", "Tshepo", "Keletso", "Farai", "Amina", "Pieter", "Johan"
]

ASSETS = [
    "refrigerator", "laptop computer", "lounge suite", "television set",
    "solar inverter system", "washing machine", "generator", "dining room set"
]

CURRENCY_RATES = [
    ("US Dollar (USD)", "$", 18.50),
    ("British Pound (GBP)", "£", 23.60),
    ("Euro (EUR)", "€", 20.10),
    ("Australian Dollar (AUD)", "A$", 12.20),
    ("Botswana Pula (BWP)", "P", 1.38),
]


def _fmt_r(amount: float | int) -> str:
    """Format Rand amount with space thousand separators and comma decimals."""
    rounded = round(amount, 2)
    if isinstance(amount, int) or rounded.is_integer():
        val_str = f"{int(rounded):,}".replace(",", " ")
        return f"R {val_str}"
    val_str = f"{rounded:,.2f}".replace(",", " ").replace(".", ",")
    return f"R {val_str}"


def _fmt_dec(val: float | int, decimals: int = 2) -> str:
    """Format decimal with comma for South African convention."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer() and decimals == 0):
        return str(int(val))
    return f"{val:.{decimals}f}".replace(".", ",")


def _interest_comparison_svg(p: int, r_pct: float, years: int, a_simple: float, a_comp: float) -> str:
    """Context SVG line graph comparing simple interest vs compound interest curves."""
    w, h = 560, 240
    # Coordinate system: x from 0 to years, y from 0 to a_comp * 1.15
    pad_l, pad_r, pad_t, pad_b = 60, 40, 30, 40
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b
    max_y = a_comp * 1.15

    def to_pt(yr: float, amt: float) -> Tuple[float, float]:
        x = pad_l + (yr / years) * plot_w
        y = pad_t + plot_h - (amt / max_y) * plot_h
        return (round(x, 1), round(y, 1))

    # Points for simple interest (linear)
    pts_s = [to_pt(y, p * (1 + (r_pct / 100) * y)) for y in range(years + 1)]
    str_s = " ".join(f"{x},{y}" for x, y in pts_s)

    # Points for compound interest (exponential)
    pts_c = [to_pt(y, p * ((1 + (r_pct / 100)) ** y)) for y in range(years + 1)]
    str_c = " ".join(f"{x},{y}" for x, y in pts_c)

    p_pt = to_pt(0, p)
    as_pt = to_pt(years, a_simple)
    ac_pt = to_pt(years, a_comp)

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
        f'<rect width="{w}" height="{h}" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<text x="{w // 2}" y="20" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">Growth Over {years} Years at {_fmt_dec(r_pct, 1)}% p.a.</text>'
        f'<line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{pad_t + plot_h}" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{pad_l + plot_w}" y2="{pad_t + plot_h}" stroke="#64748b" stroke-width="1.5"/>'
        f'<text x="{pad_l - 8}" y="{pad_t + 10}" font-size="10" text-anchor="end" fill="#475569">{_fmt_r(max_y)}</text>'
        f'<text x="{pad_l - 8}" y="{p_pt[1] + 4}" font-size="10" text-anchor="end" fill="#475569">{_fmt_r(p)}</text>'
        f'<polyline fill="none" stroke="#2563eb" stroke-width="2.5" points="{str_s}"/>'
        f'<polyline fill="none" stroke="#059669" stroke-width="2.5" points="{str_c}"/>'
        f'<circle cx="{as_pt[0]}" cy="{as_pt[1]}" r="4" fill="#2563eb"/>'
        f'<circle cx="{ac_pt[0]}" cy="{ac_pt[1]}" r="4" fill="#059669"/>'
        f'<text x="{as_pt[0] - 8}" y="{as_pt[1] + 16}" font-size="10" font-weight="bold" fill="#2563eb">Simple: {_fmt_r(a_simple)}</text>'
        f'<text x="{ac_pt[0] - 8}" y="{ac_pt[1] - 8}" font-size="10" font-weight="bold" fill="#059669">Compound: {_fmt_r(a_comp)}</text>'
        f'<text x="{pad_l}" y="{pad_t + plot_h + 18}" font-size="10" fill="#475569">0</text>'
        f'<text x="{pad_l + plot_w}" y="{pad_t + plot_h + 18}" font-size="10" text-anchor="middle" fill="#475569">{years} yrs</text>'
        f'</svg>'
    )


def _build_typed_math(
    rng: random.Random,
    *,
    qid_prefix: str,
    subskill: str,
    title: str,
    prompt: str,
    ans_str: str,
    worked: str,
    marks: int,
    hints: Dict[str, str],
    marking_points: List[Dict[str, Any]],
    misconception_tags: List[str],
    difficulty: str = "medium",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g10_fin_{subskill}",
        "question_type": "math_short",
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": worked,
        "explanation": worked,
        "canonical_solution": worked,
        "marks": marks,
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": max(3, marks),
        "difficulty": difficulty,
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["mathematics", "grade10", "finance_and_growth"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


# ---------------------------------------------------------------------------
# Archetypes 01 - 25
# ---------------------------------------------------------------------------

def build_01_simple_interest_accumulated_amount(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(4, 25) * 1000
    r_pct = rng.choice([6.0, 7.5, 8.0, 8.5, 9.0, 10.5, 11.0, 12.0])
    n = rng.randint(2, 6)
    i = r_pct / 100.0
    a = p * (1 + i * n)
    ans = _fmt_r(a)

    prompt = (
        f"{name} invests {_fmt_r(p)} in a savings account paying simple interest at "
        f"{_fmt_dec(r_pct, 1)}% per annum for {n} years. "
        f"Calculate the accumulated balance in the account at the end of the investment period."
    )
    worked = (
        f"**Formula:** $A = P(1 + in)$\n\n"
        f"**Given:** $P = {_fmt_r(p)}$, $i = {_fmt_dec(i, 4)}$, $n = {n}$\n\n"
        f"**Substitution:** $A = {p}(1 + {_fmt_dec(i, 4)} \\times {n})$\n\n"
        f"**Calculation:** $A = {p}(1 + {_fmt_dec(i * n, 4)}) = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin01",
        subskill="01_simple_interest_accumulated_amount",
        title="Simple Interest: Accumulated Amount",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Recall the simple interest formula $A = P(1 + in)$.",
            "tier_2": f"Substitute $P = {p}$, $i = {r_pct}/100 = {_fmt_dec(i, 4)}$, and $n = {n}$.",
            "tier_3": f"Evaluate {p} * (1 + {_fmt_dec(i * n, 4)}).",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Correct formula $A = P(1 + in)$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct substitution of P, i, n", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Accurate final answer {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["used_compound_instead_of_simple", "interest_rate_decimal_conversion_error"],
    )


def build_02_simple_interest_earned_only(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(5, 30) * 1000
    r_pct = rng.choice([7.0, 8.0, 9.5, 10.0, 11.5])
    n = rng.randint(3, 7)
    i = r_pct / 100.0
    interest = p * i * n
    ans = _fmt_r(interest)

    prompt = (
        f"{name} deposits {_fmt_r(p)} into a fixed deposit account at a simple interest rate of "
        f"{_fmt_dec(r_pct, 1)}% p.a. for {n} years. "
        f"Calculate the total interest earned over the {n} years."
    )
    worked = (
        f"**Formula:** $I = P \\times i \\times n$\n\n"
        f"**Given:** $P = {_fmt_r(p)}$, $i = {_fmt_dec(i, 4)}$, $n = {n}$\n\n"
        f"**Calculation:** $I = {p} \\times {_fmt_dec(i, 4)} \\times {n} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin02",
        subskill="02_simple_interest_earned_only",
        title="Simple Interest: Interest Earned Only",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=2,
        hints={
            "tier_1": "Notice the question asks for the interest earned ($I$), not the final total balance ($A$).",
            "tier_2": "Use the formula $I = P \\cdot i \\cdot n$ (or calculate $A - P$).",
            "tier_3": f"Compute {p} * {_fmt_dec(i, 4)} * {n}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Uses $I = P \\cdot i \\cdot n$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct interest amount {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["calculated_accumulated_instead_of_interest"],
    )


def build_03_simple_interest_solve_for_principal(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(3, 20) * 1000
    r_pct = rng.choice([6.0, 8.0, 10.0, 12.0])
    n = rng.randint(2, 5)
    i = r_pct / 100.0
    a = p * (1 + i * n)
    ans = _fmt_r(p)

    prompt = (
        f"{name} wants to accumulate {_fmt_r(a)} in {n} years' time to pay for tertiary studies. "
        f"A bank offers a fixed deposit rate of {_fmt_dec(r_pct, 1)}% per annum simple interest. "
        f"How much principal money ($P$) must {name} invest today?"
    )
    worked = (
        f"**Formula:** $A = P(1 + in) \\implies P = \\frac{{A}}{{1 + in}}$\n\n"
        f"**Substitution:** $P = \\frac{{{_fmt_r(a)}}}{{1 + {_fmt_dec(i, 4)} \\times {n}}} = \\frac{{{_fmt_r(a)}}}{{{_fmt_dec(1 + i * n, 4)}}}$\n\n"
        f"**Calculation:** $P = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin03",
        subskill="03_simple_interest_solve_for_principal",
        title="Simple Interest: Solving for Principal ($P$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Rearrange the simple interest formula to isolate $P$: $P = \\frac{A}{1 + in}$.",
            "tier_2": f"Divide {_fmt_r(a)} by (1 + {_fmt_dec(i, 4)} * {n}).",
            "tier_3": f"P = {a} / {_fmt_dec(1 + i * n, 4)}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Rearranges formula to solve for P", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes A, i, n correctly", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct principal value {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["multiplied_instead_of_divided_for_principal"],
    )


def build_04_simple_interest_solve_for_interest_rate(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(4, 15) * 1000
    r_pct = rng.choice([6.5, 7.5, 8.0, 9.0, 10.5, 12.0])
    n = rng.randint(3, 6)
    i = r_pct / 100.0
    a = p * (1 + i * n)
    ans = f"{_fmt_dec(r_pct, 1)}%"

    prompt = (
        f"{name} invested {_fmt_r(p)} in a savings club and received {_fmt_r(a)} at the end of {n} years. "
        f"Calculate the annual simple interest rate ($r\\%$) earned on this investment. "
        f"State your answer as a percentage."
    )
    worked = (
        f"**Formula:** $A = P(1 + in) \\implies i = \\frac{{A - P}}{{P \\times n}}$\n\n"
        f"**Substitution:** $i = \\frac{{{a} - {p}}}{{{p} \\times {n}}} = \\frac{{{a - p}}}{{{p * n}}}$\n\n"
        f"**Calculation:** $i = {_fmt_dec(i, 4)} \\implies r = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin04",
        subskill="04_simple_interest_solve_for_interest_rate",
        title="Simple Interest: Solving for Interest Rate ($i$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Find total interest earned first: $I = A - P$.",
            "tier_2": "Then use $I = P \\cdot i \\cdot n$ to solve for $i = \\frac{I}{P \\cdot n}$.",
            "tier_3": f"Multiply the decimal $i$ by 100 to state the answer as a percentage: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates interest earned $I = A - P$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Solves for decimal rate $i$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct percentage rate {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["forgot_to_convert_decimal_to_percent"],
    )


def build_05_simple_interest_solve_for_time_period(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(5, 20) * 1000
    r_pct = rng.choice([5.0, 7.5, 8.0, 10.0, 12.5])
    n = rng.randint(2, 8)
    i = r_pct / 100.0
    a = p * (1 + i * n)
    ans = f"{n} years"

    prompt = (
        f"{name} invested an amount of {_fmt_r(p)} at a simple interest rate of {_fmt_dec(r_pct, 1)}% p.a. "
        f"How many years did it take for the investment to grow to {_fmt_r(a)}?"
    )
    worked = (
        f"**Formula:** $A = P(1 + in) \\implies n = \\frac{{A - P}}{{P \\times i}}$\n\n"
        f"**Interest earned:** $I = {_fmt_r(a)} - {_fmt_r(p)} = {_fmt_r(a - p)}$\n\n"
        f"**Substitution:** $n = \\frac{{{a - p}}}{{{p} \\times {_fmt_dec(i, 4)}}} = \\frac{{{a - p}}}{{{p * i}}} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin05",
        subskill="05_simple_interest_solve_for_time_period",
        title="Simple Interest: Solving for Time Period ($n$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Calculate the interest earned $I = A - P$.",
            "tier_2": "Use $n = \\frac{I}{P \\cdot i}$.",
            "tier_3": f"Divide {a - p} by ({p} * {_fmt_dec(i, 4)}) to get {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates interest earned $I = A - P$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes into $n = I / (P \\cdot i)$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct number of years: {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["divided_by_rate_percentage_without_converting_to_decimal"],
    )


def build_06_simple_interest_months_conversion(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(6, 24) * 1000
    r_pct = rng.choice([8.0, 9.0, 10.0, 12.0])
    months = rng.choice([6, 9, 18, 30, 42])
    n = months / 12.0
    i = r_pct / 100.0
    a = p * (1 + i * n)
    ans = _fmt_r(a)

    prompt = (
        f"{name} took out a personal short-term loan of {_fmt_r(p)} at a simple interest rate of "
        f"{_fmt_dec(r_pct, 1)}% per annum for {months} months. "
        f"Calculate the total amount that must be repaid at the end of {months} months."
    )
    worked = (
        f"**Step 1 — Convert time to years:** $n = \\frac{{{months}}}{{12}} = {_fmt_dec(n, 2)}$ years\n\n"
        f"**Step 2 — Apply simple interest formula:** $A = P(1 + in)$\n\n"
        f"**Substitution:** $A = {p}(1 + {_fmt_dec(i, 4)} \\times {_fmt_dec(n, 2)}) = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin06",
        subskill="06_simple_interest_months_conversion",
        title="Simple Interest: Converting Months to Years",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "The interest rate is per annum (yearly), so time $n$ must be converted from months to years.",
            "tier_2": f"Divide months by 12: $n = {months} / 12 = {_fmt_dec(n, 2)}$ years.",
            "tier_3": f"Calculate $A = {p} \\cdot (1 + {_fmt_dec(i, 4)} \\cdot {_fmt_dec(n, 2)})$.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Converts {months} months to {months}/12 years", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes into $A = P(1 + in)$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct total repayment {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["used_months_directly_as_years"],
    )


def build_07_simple_interest_doubling_investment(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    r_pct = rng.choice([5.0, 8.0, 10.0, 12.5, 20.0])
    i = r_pct / 100.0
    n = round(1.0 / i, 2)
    ans = f"{_fmt_dec(n, 1)} years" if not n.is_integer() else f"{int(n)} years"

    prompt = (
        f"{name} invests a sum of money at {_fmt_dec(r_pct, 1)}% per annum simple interest. "
        f"How many years will it take for the investment to DOUBLE in value?"
    )
    worked = (
        f"**Concept:** For an investment to double, $A = 2P$.\n\n"
        f"**Formula:** $2P = P(1 + in) \\implies 2 = 1 + in \\implies in = 1$\n\n"
        f"**Solve for $n$:** $n = \\frac{{1}}{{i}} = \\frac{{1}}{{{_fmt_dec(i, 4)}}} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin07",
        subskill="07_simple_interest_doubling_investment",
        title="Simple Interest: Doubling an Investment",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Set the final amount $A = 2P$. The principal $P$ cancels out on both sides.",
            "tier_2": "Solve $2 = 1 + in$, which simplifies to $in = 1$.",
            "tier_3": f"Divide 1 by decimal rate {_fmt_dec(i, 4)}: 1 / {_fmt_dec(i, 4)} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Sets $A = 2P$ and simplifies to $in = 1$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Substitutes $i = {_fmt_dec(i, 4)}$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct time to double: {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["doubling_formula_confused_with_rule_of_72"],
    )


def build_08_compound_interest_annual_accumulation(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(8, 35) * 1000
    r_pct = rng.choice([6.0, 7.5, 8.0, 8.5, 9.5, 10.0, 11.0])
    n = rng.randint(2, 5)
    i = r_pct / 100.0
    a = p * ((1.0 + i) ** n)
    ans = _fmt_r(a)

    prompt = (
        f"{name} deposits {_fmt_r(p)} into a long-term fixed deposit yielding {_fmt_dec(r_pct, 1)}% per annum "
        f"compound interest, compounded annually for {n} years. "
        f"Calculate the accumulated value of the investment at the end of {n} years."
    )
    worked = (
        f"**Formula:** $A = P(1 + i)^n$\n\n"
        f"**Given:** $P = {_fmt_r(p)}$, $i = {_fmt_dec(i, 4)}$, $n = {n}$\n\n"
        f"**Substitution:** $A = {p}(1 + {_fmt_dec(i, 4)})^{{{n}}} = {p}({_fmt_dec(1 + i, 4)})^{{{n}}}$\n\n"
        f"**Calculation:** $A = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin08",
        subskill="08_compound_interest_annual_accumulation",
        title="Compound Interest: Annual Accumulation",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Recall the compound interest formula $A = P(1 + i)^n$.",
            "tier_2": f"Substitute $P = {p}$, $i = {_fmt_dec(i, 4)}$, and $n = {n}$.",
            "tier_3": f"Evaluate {p} * ({_fmt_dec(1 + i, 4)})^{n} to two decimal places.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "States compound interest formula $A = P(1 + i)^n$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes values correctly", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Accurate final answer {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["used_simple_interest_formula_for_compound"],
    )


def build_09_compound_interest_interest_earned_only(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(10, 40) * 1000
    r_pct = rng.choice([7.0, 8.5, 9.0, 10.5, 12.0])
    n = rng.randint(3, 6)
    i = r_pct / 100.0
    a = p * ((1.0 + i) ** n)
    interest = a - p
    ans = _fmt_r(interest)

    prompt = (
        f"{name} invests {_fmt_r(p)} at a compound interest rate of {_fmt_dec(r_pct, 1)}% p.a. compounded annually for {n} years. "
        f"Calculate the total compound interest earned on this investment."
    )
    worked = (
        f"**Step 1 — Calculate accumulated amount:**\n"
        f"$A = P(1 + i)^n = {p}(1 + {_fmt_dec(i, 4)})^{{{n}}} = {_fmt_r(a)}$\n\n"
        f"**Step 2 — Deduct initial principal to find interest:**\n"
        f"$I = A - P = {_fmt_r(a)} - {_fmt_r(p)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin09",
        subskill="09_compound_interest_interest_earned_only",
        title="Compound Interest: Total Interest Earned Only",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Calculate the total accumulated amount $A$ first, then subtract the principal $P$.",
            "tier_2": f"Use $A = {p}(1 + {_fmt_dec(i, 4)})^{n}$.",
            "tier_3": f"Subtract {p} from the accumulated balance to get {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates accumulated amount $A = P(1 + i)^n$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Subtracts principal $I = A - P$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct interest earned {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["gave_accumulated_amount_instead_of_interest"],
    )


def build_10_compound_interest_solve_for_principal(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(12, 35) * 1000
    r_pct = rng.choice([7.0, 8.0, 9.0, 10.0, 11.5])
    n = rng.randint(3, 6)
    i = r_pct / 100.0
    a = p * ((1.0 + i) ** n)
    ans = _fmt_r(p)

    prompt = (
        f"{name} needs {_fmt_r(a)} in {n} years' time to buy equipment. "
        f"If the bank pays compound interest at {_fmt_dec(r_pct, 1)}% p.a. compounded annually, "
        f"how much must {name} invest now as the initial principal?"
    )
    worked = (
        f"**Formula:** $A = P(1 + i)^n \\implies P = \\frac{{A}}{{(1 + i)^n}}$\n\n"
        f"**Substitution:** $P = \\frac{{{_fmt_r(a)}}}{{(1 + {_fmt_dec(i, 4)})^{{{n}}}}} = \\frac{{{_fmt_r(a)}}}{{{_fmt_dec((1 + i) ** n, 6)}}}$\n\n"
        f"**Calculation:** $P = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin10",
        subskill="10_compound_interest_solve_for_principal",
        title="Compound Interest: Solving for Principal ($P$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Rearrange $A = P(1 + i)^n$ to solve for $P$: $P = \\frac{A}{(1 + i)^n}$.",
            "tier_2": f"Divide {_fmt_r(a)} by ({_fmt_dec(1 + i, 4)})^{n}.",
            "tier_3": f"Evaluate the division to obtain {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "States formula $P = A / (1 + i)^n$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes values correctly", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct principal {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["multiplied_by_compound_factor_instead_of_dividing"],
    )


def build_11_compound_interest_solve_for_interest_rate(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(10, 25) * 1000
    r_pct = rng.choice([7.0, 8.0, 9.5, 10.0, 11.5, 12.0])
    n = rng.choice([2, 3, 4])
    i = r_pct / 100.0
    a = p * ((1.0 + i) ** n)
    ans = f"{_fmt_dec(r_pct, 1)}%"

    prompt = (
        f"{name} invested {_fmt_r(p)}, which grew to {_fmt_r(a)} after {n} years with interest compounded annually. "
        f"Calculate the annual compound interest rate ($r\\%$). State your answer as a percentage."
    )
    worked = (
        f"**Formula:** $A = P(1 + i)^n \\implies \\frac{{A}}{{P}} = (1 + i)^n \\implies 1 + i = \\sqrt[{n}]{{\\frac{{A}}{{P}}}}$\n\n"
        f"**Substitution:** $1 + i = \\sqrt[{n}]{{\\frac{{{round(a, 2)}}}{{{p}}}}} = \\sqrt[{n}]{{{_fmt_dec(a / p, 6)}}} = {_fmt_dec(1 + i, 4)}$\n\n"
        f"**Solve for $r$:** $i = {_fmt_dec(i, 4)} \\implies r = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin11",
        subskill="11_compound_interest_solve_for_interest_rate",
        title="Compound Interest: Solving for Interest Rate ($i$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Divide $A$ by $P$ first: $\\frac{A}{P} = (1 + i)^n$.",
            "tier_2": f"Take the {n}-th root on both sides: $1 + i = (A / P)^{{1/{n}}}$.",
            "tier_3": f"Subtract 1 and multiply by 100 to get the percentage: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Divides $A / P$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Takes {n}-th root of $(A / P)$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Subtracts 1 to find $i$", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Converts to percentage: {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["divided_by_n_instead_of_taking_nth_root"],
    )


def build_12_simple_vs_compound_interest_difference(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    p = rng.randint(8, 25) * 1000
    r_pct = rng.choice([7.0, 8.0, 9.0, 10.0, 11.0])
    n = rng.randint(3, 6)
    i = r_pct / 100.0
    a_simple = p * (1 + i * n)
    a_comp = p * ((1.0 + i) ** n)
    diff = a_comp - a_simple
    ans = _fmt_r(diff)
    svg = _interest_comparison_svg(p, r_pct, n, a_simple, a_comp)

    prompt = (
        f"{name} has {_fmt_r(p)} to invest for {n} years at an interest rate of {_fmt_dec(r_pct, 1)}% per annum. "
        f"Examine the comparison curves between simple interest and compound interest below. "
        f"Calculate how much MORE money {name} will accumulate under compound interest compared to simple interest."
    )
    worked = (
        f"**1. Simple Interest:**\n"
        f"$A_{{simple}} = P(1 + in) = {p}(1 + {_fmt_dec(i, 4)} \\times {n}) = {_fmt_r(a_simple)}$\n\n"
        f"**2. Compound Interest:**\n"
        f"$A_{{compound}} = P(1 + i)^n = {p}(1 + {_fmt_dec(i, 4)})^{{{n}}} = {_fmt_r(a_comp)}$\n\n"
        f"**3. Difference:**\n"
        f"$\\text{{Difference}} = {_fmt_r(a_comp)} - {_fmt_r(a_simple)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin12",
        subskill="12_simple_vs_compound_interest_difference",
        title="Simple vs Compound Interest: Comparative Difference",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Calculate the accumulated balance using simple interest and compound interest separately.",
            "tier_2": f"Simple: $A = {p}(1 + {_fmt_dec(i, 4)} \\times {n})$; Compound: $A = {p}(1 + {_fmt_dec(i, 4)})^{n}$.",
            "tier_3": f"Subtract the two results to find the extra growth: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates simple interest total", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Calculates compound interest total", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Subtracts $A_{compound} - A_{simple}$", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct difference {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["subtracted_simple_interest_rate_from_compound_rate"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_13_hire_purchase_deposit_calculation(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(4, 25) * 1000
    dep_pct = rng.choice([10, 15, 20])
    deposit = cash_price * (dep_pct / 100.0)
    ans = _fmt_r(deposit)

    prompt = (
        f"{name} buys a {asset} on hire purchase. "
        f"The cash price is {_fmt_r(cash_price)}. "
        f"The store requires a {dep_pct}% upfront cash deposit. "
        f"Calculate the deposit amount in Rand."
    )
    worked = (
        f"$$\\text{{Deposit}} = \\text{{Cash Price}} \\times \\text{{Deposit \\%}}$$\n\n"
        f"$$\\text{{Deposit}} = {_fmt_r(cash_price)} \\times \\frac{{{dep_pct}}}{{100}} = \\mathbf{{{ans}}}$$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin13",
        subskill="13_hire_purchase_deposit_calculation",
        title="Hire Purchase: Deposit Calculation",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=2,
        hints={
            "tier_1": "The deposit is a percentage of the cash price.",
            "tier_2": f"Multiply {_fmt_r(cash_price)} by {dep_pct}/100.",
            "tier_3": f"{cash_price} * {dep_pct / 100} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Multiplies cash price by {dep_pct}%", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct deposit amount {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["subtracted_percentage_from_price_directly"],
    )


def build_14_hire_purchase_loan_principal(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(5, 28) * 1000
    dep_pct = rng.choice([10, 12, 15, 20])
    deposit = cash_price * (dep_pct / 100.0)
    loan_p = cash_price - deposit
    ans = _fmt_r(loan_p)

    prompt = (
        f"{name} purchases a {asset} with a cash price of {_fmt_r(cash_price)} on hire purchase. "
        f"After paying a {dep_pct}% deposit, what is the principal loan balance ($P$) that will be financed?"
    )
    worked = (
        f"**Step 1 — Calculate deposit:**\n"
        f"$\\text{{Deposit}} = {_fmt_r(cash_price)} \\times {dep_pct}\\% = {_fmt_r(deposit)}$\n\n"
        f"**Step 2 — Calculate financed loan balance:**\n"
        f"$P = \\text{{Cash Price}} - \\text{{Deposit}} = {_fmt_r(cash_price)} - {_fmt_r(deposit)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin14",
        subskill="14_hire_purchase_loan_principal",
        title="Hire Purchase: Loan Principal ($P = \\text{Price} - \\text{Deposit}$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=2,
        hints={
            "tier_1": "The amount financed is the cash price minus the deposit paid upfront.",
            "tier_2": f"Calculate deposit: {_fmt_r(deposit)}, then subtract it from {_fmt_r(cash_price)}.",
            "tier_3": f"{cash_price} - {deposit} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates deposit amount", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Deducts deposit to find loan balance {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["charged_interest_on_cash_price_without_subtracting_deposit"],
    )


def build_15_hire_purchase_total_repayment(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(6, 24) * 1000
    dep_pct = rng.choice([10, 15, 20])
    r_pct = rng.choice([8.0, 9.5, 10.0, 12.0, 14.0])
    years = rng.choice([2, 3, 4])
    deposit = cash_price * (dep_pct / 100.0)
    p_loan = cash_price - deposit
    i = r_pct / 100.0
    a_repay = p_loan * (1 + i * years)
    ans = _fmt_r(a_repay)

    prompt = (
        f"{name} buys a {asset} priced at {_fmt_r(cash_price)} on a {years}-year hire purchase contract. "
        f"A {dep_pct}% deposit is paid, and the simple interest rate on the loan is {_fmt_dec(r_pct, 1)}% p.a. "
        f"Calculate the total amount to be repaid on the loan balance ($A$)."
    )
    worked = (
        f"**Step 1 — Deposit:** $\\text{{Deposit}} = {_fmt_r(cash_price)} \\times {dep_pct}\\% = {_fmt_r(deposit)}$\n\n"
        f"**Step 2 — Principal loan:** $P = {_fmt_r(cash_price)} - {_fmt_r(deposit)} = {_fmt_r(p_loan)}$\n\n"
        f"**Step 3 — Simple interest repayment on loan:**\n"
        f"$A = P(1 + in) = {p_loan}(1 + {_fmt_dec(i, 4)} \\times {years}) = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin15",
        subskill="15_hire_purchase_total_repayment",
        title="Hire Purchase: Total Repayment on Loan",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Hire purchase agreements ALWAYS charge simple interest on the remaining loan balance.",
            "tier_2": f"Find loan $P = {_fmt_r(cash_price)} - {_fmt_r(deposit)} = {_fmt_r(p_loan)}$.",
            "tier_3": f"Use $A = P(1 + in)$ with $P = {p_loan}$, $i = {_fmt_dec(i, 4)}$, $n = {years}$.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates loan balance $P$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes into simple interest formula $A = P(1 + in)$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct total loan repayment {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["used_compound_interest_for_hire_purchase"],
    )


def build_16_hire_purchase_monthly_instalment(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(5, 20) * 1000
    dep_pct = rng.choice([10, 15, 20])
    r_pct = rng.choice([8.0, 10.0, 12.0, 15.0])
    years = rng.choice([2, 3])
    months = years * 12
    deposit = cash_price * (dep_pct / 100.0)
    p_loan = cash_price - deposit
    i = r_pct / 100.0
    a_repay = p_loan * (1 + i * years)
    monthly = a_repay / months
    ans = _fmt_r(monthly)

    prompt = (
        f"{name} purchases a {asset} costing {_fmt_r(cash_price)} on hire purchase over {months} months ({years} years). "
        f"{name} pays a {dep_pct}% deposit upfront, and simple interest is charged at {_fmt_dec(r_pct, 1)}% p.a. on the balance. "
        f"Calculate the monthly instalment amount."
    )
    worked = (
        f"**Step 1 — Deposit:** ${dep_pct}\\% \\times {_fmt_r(cash_price)} = {_fmt_r(deposit)}$\n\n"
        f"**Step 2 — Principal loan:** $P = {_fmt_r(cash_price)} - {_fmt_r(deposit)} = {_fmt_r(p_loan)}$\n\n"
        f"**Step 3 — Total loan to repay:** $A = {p_loan}(1 + {_fmt_dec(i, 4)} \\times {years}) = {_fmt_r(a_repay)}$\n\n"
        f"**Step 4 — Monthly instalment:** $\\text{{Instalment}} = \\frac{{{_fmt_r(a_repay)}}}{{{months}}} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin16",
        subskill="16_hire_purchase_monthly_instalment",
        title="Hire Purchase: Monthly Instalment",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Calculate the loan amount, find the accumulated repayment using simple interest, then divide by the number of months.",
            "tier_2": f"Total loan repayment $A = {_fmt_r(a_repay)}$.",
            "tier_3": f"Divide $A$ by {months} months: {_fmt_r(a_repay)} / {months} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates loan principal $P$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Calculates total repayment $A = P(1 + in)$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Divides total by {months} months", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct monthly instalment {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["divided_by_years_instead_of_months"],
    )


def build_17_hire_purchase_total_cost_of_agreement(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(8, 25) * 1000
    dep_pct = rng.choice([10, 15, 20])
    r_pct = rng.choice([9.0, 10.5, 12.0, 13.5])
    years = rng.choice([2, 3])
    deposit = cash_price * (dep_pct / 100.0)
    p_loan = cash_price - deposit
    i = r_pct / 100.0
    a_repay = p_loan * (1 + i * years)
    total_cost = deposit + a_repay
    ans = _fmt_r(total_cost)

    prompt = (
        f"{name} buys a {asset} with a cash price of {_fmt_r(cash_price)} on hire purchase. "
        f"{name} pays a {dep_pct}% deposit and finances the rest over {years} years at {_fmt_dec(r_pct, 1)}% p.a. simple interest. "
        f"Calculate the TOTAL cost of the purchase (deposit + all loan repayments)."
    )
    worked = (
        f"**Step 1 — Deposit:** $\\text{{Deposit}} = {_fmt_r(cash_price)} \\times {dep_pct}\\% = {_fmt_r(deposit)}$\n\n"
        f"**Step 2 — Financed balance:** $P = {_fmt_r(cash_price)} - {_fmt_r(deposit)} = {_fmt_r(p_loan)}$\n\n"
        f"**Step 3 — Total repayments on loan:** $A = {p_loan}(1 + {_fmt_dec(i, 4)} \\times {years}) = {_fmt_r(a_repay)}$\n\n"
        f"**Step 4 — Total cost:** $\\text{{Total Cost}} = \\text{{Deposit}} + A = {_fmt_r(deposit)} + {_fmt_r(a_repay)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin17",
        subskill="17_hire_purchase_total_cost_of_agreement",
        title="Hire Purchase: Total Cost (Deposit + Repayments)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "The total cost includes the upfront deposit PLUS the total loan repayments.",
            "tier_2": f"Deposit = {_fmt_r(deposit)}, Loan repayments = {_fmt_r(a_repay)}.",
            "tier_3": f"Add both amounts: {_fmt_r(deposit)} + {_fmt_r(a_repay)} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates deposit", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Calculates total repayments $A = P(1+in)$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Adds deposit + total repayments", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct total cost {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["forgot_to_add_deposit_to_total_cost"],
    )


def build_18_hire_purchase_cost_of_credit_difference(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(6, 22) * 1000
    dep_pct = rng.choice([10, 15, 20])
    r_pct = rng.choice([9.0, 11.0, 12.5, 14.0])
    years = rng.choice([2, 3])
    deposit = cash_price * (dep_pct / 100.0)
    p_loan = cash_price - deposit
    i = r_pct / 100.0
    interest_extra = p_loan * i * years
    ans = _fmt_r(interest_extra)

    prompt = (
        f"{name} buys a {asset} costing {_fmt_r(cash_price)} cash. "
        f"Under hire purchase, a {dep_pct}% deposit is paid, and the balance is settled over {years} years at {_fmt_dec(r_pct, 1)}% p.a. simple interest. "
        f"Calculate the EXTRA cost of buying on credit compared to paying upfront in cash."
    )
    worked = (
        f"**Method 1 (Total interest on loan):**\n"
        f"Loan Principal: $P = {_fmt_r(cash_price)} - {dep_pct}\\% = {_fmt_r(p_loan)}$\n\n"
        f"Extra Cost of Credit = Interest charged on loan: $I = P \\times i \\times n$\n"
        f"$I = {p_loan} \\times {_fmt_dec(i, 4)} \\times {years} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin18",
        subskill="18_hire_purchase_cost_of_credit_difference",
        title="Hire Purchase: Cost of Credit (Extra Amount Paid)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "The extra cost of credit is simply the total interest charged on the loan balance.",
            "tier_2": f"Find loan $P = {_fmt_r(p_loan)}$ and calculate $I = P \\cdot i \\cdot n$.",
            "tier_3": f"{p_loan} * {_fmt_dec(i, 4)} * {years} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates loan balance $P$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Uses $I = P \\cdot i \\cdot n$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct extra credit cost {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["confused_cost_of_credit_with_total_cost"],
    )


def build_19_hire_purchase_insurance_and_admin_fee(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    asset = rng.choice(ASSETS)
    cash_price = rng.randint(6, 20) * 1000
    dep_pct = 10
    r_pct = 12.0
    years = 2
    months = years * 12
    monthly_insurance = rng.choice([35, 45, 50, 60])
    deposit = cash_price * 0.10
    p_loan = cash_price - deposit
    i = 0.12
    a_repay = p_loan * (1 + i * years)
    base_instalment = a_repay / months
    total_monthly = base_instalment + monthly_insurance
    ans = _fmt_r(total_monthly)

    prompt = (
        f"{name} enters a hire purchase agreement for a {asset} with cash price {_fmt_r(cash_price)}. "
        f"{name} pays a 10% deposit and finances the balance over 24 months at 12% p.a. simple interest. "
        f"In addition, the store charges a mandatory insurance and admin fee of {_fmt_r(monthly_insurance)} per month. "
        f"Calculate the TOTAL monthly payment {name} must make."
    )
    worked = (
        f"**Step 1 — Financed balance:** $P = {_fmt_r(cash_price)} - 10\\% = {_fmt_r(p_loan)}$\n\n"
        f"**Step 2 — Total loan repayment:** $A = {p_loan}(1 + 0,12 \\times 2) = {_fmt_r(a_repay)}$\n\n"
        f"**Step 3 — Base monthly instalment:** $\\frac{{{_fmt_r(a_repay)}}}{{24}} = {_fmt_r(base_instalment)}$\n\n"
        f"**Step 4 — Add monthly insurance:** ${_fmt_r(base_instalment)} + {_fmt_r(monthly_insurance)} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin19",
        subskill="19_hire_purchase_insurance_and_admin_fee",
        title="Hire Purchase: Instalment with Monthly Insurance & Admin Fee",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": "Calculate the base monthly instalment on the loan first, then add the monthly insurance fee.",
            "tier_2": f"Base instalment = {_fmt_r(base_instalment)}.",
            "tier_3": f"Add {_fmt_r(monthly_insurance)}: {_fmt_r(base_instalment)} + {_fmt_r(monthly_insurance)} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Calculates loan balance $P$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Calculates base instalment $A / 24$", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Adds monthly insurance fee", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct total monthly payment {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["added_insurance_fee_to_principal_loan_before_interest"],
    )


def build_20_inflation_future_price_compound_growth(rng: random.Random) -> Dict[str, Any]:
    goods = rng.choice(["a loaf of bread", "a 2-litre carton of milk", "a private school fee", "a new economy car"])
    base_price = rng.choice([16.50, 32.00, 2400.00, 185000.00])
    inf_pct = rng.choice([4.5, 5.0, 5.5, 6.0, 6.5])
    years = rng.randint(3, 7)
    i = inf_pct / 100.0
    future_price = base_price * ((1.0 + i) ** years)
    ans = _fmt_r(future_price)

    prompt = (
        f"Currently, {goods} costs {_fmt_r(base_price)}. "
        f"Assuming an average annual inflation rate of {_fmt_dec(inf_pct, 1)}% over the next {years} years, "
        f"calculate the estimated future price of the {goods}."
    )
    worked = (
        f"**Concept:** Inflation causes prices to rise according to compound growth: $A = P(1 + i)^n$.\n\n"
        f"**Substitution:** $A = {_fmt_r(base_price)}(1 + {_fmt_dec(i, 4)})^{{{years}}}$\n\n"
        f"**Calculation:** $A = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin20",
        subskill="20_inflation_future_price_compound_growth",
        title="Inflation: Future Cost of Goods ($A = P(1 + i)^n$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Inflation is modelled using the compound growth formula $A = P(1 + i)^n$.",
            "tier_2": f"Substitute $P = {_fmt_r(base_price)}$, $i = {_fmt_dec(i, 4)}$, $n = {years}$.",
            "tier_3": f"Calculate {base_price} * ({_fmt_dec(1 + i, 4)})^{years} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Uses compound growth formula for inflation", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes base price, inflation rate, and years", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct future price {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["used_simple_interest_for_inflation"],
    )


def build_21_inflation_past_price_reverse_calculation(rng: random.Random) -> Dict[str, Any]:
    goods = rng.choice(["a residential home in Durban", "a gym membership", "a medical aid contribution"])
    p_past = rng.randint(15, 60) * 10000
    inf_pct = rng.choice([5.0, 6.0, 7.0])
    years = rng.choice([4, 5, 6])
    i = inf_pct / 100.0
    p_current = p_past * ((1.0 + i) ** years)
    ans = _fmt_r(p_past)

    prompt = (
        f"The current price of {goods} is {_fmt_r(p_current)}. "
        f"If the average annual inflation rate over the past {years} years was {_fmt_dec(inf_pct, 1)}%, "
        f"calculate what this {goods} cost {years} years ago."
    )
    worked = (
        f"**Formula:** $A = P(1 + i)^n \\implies P = \\frac{{A}}{{(1 + i)^n}}$\n\n"
        f"**Substitution:** $P = \\frac{{{_fmt_r(p_current)}}}{{(1 + {_fmt_dec(i, 4)})^{{{years}}}}} = \\mathbf{{{ans}}}$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin21",
        subskill="21_inflation_past_price_reverse_calculation",
        title="Inflation: Deducing Past Price ($P = A / (1 + i)^n$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "To find what an item cost in the past, divide the current price by $(1 + i)^n$.",
            "tier_2": f"Formula: $P = {_fmt_r(p_current)} / (1 + {_fmt_dec(i, 4)})^{years}$.",
            "tier_3": f"Evaluate the division to find the past cost: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Sets up formula $P = A / (1 + i)^n$", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes current price and inflation rate", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct past price {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["multiplied_by_inflation_instead_of_dividing"],
    )


def build_22_population_compound_growth(rng: random.Random) -> Dict[str, Any]:
    town = rng.choice(["Polokwane", "Nelspruit", "George", "Rustenburg", "Upington"])
    p0 = rng.randint(45, 120) * 1000
    g_pct = rng.choice([2.0, 2.5, 3.0, 3.5, 4.0])
    years = rng.randint(5, 10)
    i = g_pct / 100.0
    p_future = int(round(p0 * ((1.0 + i) ** years)))
    ans = f"{p_future:,}".replace(",", " ")

    prompt = (
        f"The population of {town} is currently {p0:,}. "
        f"If the population is projected to grow at an average rate of {_fmt_dec(g_pct, 1)}% per annum, "
        f"estimate the population in {years} years' time (rounded to the nearest whole person)."
    ).replace(",", " ")

    worked = (
        f"**Formula:** $A = P(1 + i)^n$\n\n"
        f"**Substitution:** $A = {p0:,}(1 + {_fmt_dec(i, 4)})^{{{years}}}$\n\n"
        f"**Calculation:** $A \\approx \\mathbf{{{ans}}}$ people"
    ).replace(",", " ")

    return _build_typed_math(
        rng,
        qid_prefix="fin22",
        subskill="22_population_compound_growth",
        title="Population Growth Modelling ($A = P(1 + i)^n$)",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=3,
        hints={
            "tier_1": "Population growth follows the compound growth model $A = P(1 + i)^n$.",
            "tier_2": f"Substitute $P = {p0}$, $i = {_fmt_dec(i, 4)}$, $n = {years}$.",
            "tier_3": f"Round the final answer to the nearest whole person: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Applies compound growth formula to population", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Substitutes values accurately", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct rounded population {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["left_population_as_decimal_places"],
    )


def build_23_foreign_exchange_convert_zar_to_foreign(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    curr_name, sym, base = rng.choice(CURRENCY_RATES)
    rate = round(base + rng.choice([-0.7, -0.3, 0.0, 0.4, 0.8]), 2)
    foreign_amt = rng.randint(20, 80) * 10
    zar_amt = round(foreign_amt * rate, 2)
    ans = f"{sym} {_fmt_dec(foreign_amt, 2)}"

    prompt = (
        f"{name} travels abroad and exchanges {_fmt_r(zar_amt)} for {curr_name}. "
        f"The exchange rate is {sym} 1 = R {_fmt_dec(rate, 2)}. "
        f"How much in {curr_name} does {name} receive?"
    )
    worked = (
        f"$$\\text{{Foreign Currency}} = \\frac{{\\text{{Amount in ZAR}}}}{{\\text{{Exchange Rate}}}}$$\n\n"
        f"$$\\text{{Amount in {curr_name}}} = \\frac{{{zar_amt}}}{{{_fmt_dec(rate, 2)}}} = \\mathbf{{{ans}}}$$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin23",
        subskill="23_foreign_exchange_convert_zar_to_foreign",
        title="Foreign Exchange: Converting ZAR to Foreign Currency",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=2,
        hints={
            "tier_1": f"To convert from Rand to {curr_name}, divide the Rand amount by the exchange rate.",
            "tier_2": f"Divide {_fmt_r(zar_amt)} by {_fmt_dec(rate, 2)}.",
            "tier_3": f"{zar_amt} / {rate} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Divides Rand amount by exchange rate", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct foreign currency amount {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["multiplied_instead_of_divided_for_foreign_conversion"],
    )


def build_24_foreign_exchange_convert_foreign_to_zar(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(SA_NAMES)
    curr_name, sym, base = rng.choice(CURRENCY_RATES)
    rate = round(base + rng.choice([-0.5, -0.2, 0.0, 0.3, 0.6]), 2)
    foreign_amt = rng.randint(15, 60) * 10
    zar_amt = round(foreign_amt * rate, 2)
    ans = _fmt_r(zar_amt)

    prompt = (
        f"{name} returns to South Africa with {sym} {foreign_amt} ({curr_name}) remaining from a trip. "
        f"If the current bank exchange rate is {sym} 1 = R {_fmt_dec(rate, 2)}, "
        f"how much in South African Rand will {name} receive upon converting this money?"
    )
    worked = (
        f"$$\\text{{Amount in ZAR}} = \\text{{Foreign Amount}} \\times \\text{{Exchange Rate}}$$\n\n"
        f"$$\\text{{Amount in ZAR}} = {foreign_amt} \\times {_fmt_dec(rate, 2)} = \\mathbf{{{ans}}}$$"
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin24",
        subskill="24_foreign_exchange_convert_foreign_to_zar",
        title="Foreign Exchange: Converting Foreign Currency to ZAR",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=2,
        hints={
            "tier_1": f"Each unit of {curr_name} is worth R {_fmt_dec(rate, 2)}.",
            "tier_2": f"Multiply {foreign_amt} by the exchange rate {_fmt_dec(rate, 2)}.",
            "tier_3": f"{foreign_amt} * {rate} = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Multiplies foreign amount by exchange rate", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct Rand amount {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["divided_foreign_amount_by_rate_instead_of_multiplying"],
    )


def build_25_foreign_exchange_cross_price_comparison(rng: random.Random) -> Dict[str, Any]:
    curr_name, sym, rate = ("British Pound (GBP)", "£", 23.50)
    uk_price_gbp = rng.randint(45, 95) * 10
    sa_price_zar = int(round(uk_price_gbp * rate + rng.choice([-1500, 1500, 2200, -2200])))
    uk_in_zar = round(uk_price_gbp * rate, 2)
    is_sa_cheaper = sa_price_zar < uk_in_zar
    cheaper_place = "South Africa" if is_sa_cheaper else "the United Kingdom"
    diff = abs(uk_in_zar - sa_price_zar)
    ans = f"{cheaper_place} by {_fmt_r(diff)}"

    prompt = (
        f"A smartphone is sold in London for {sym} {uk_price_gbp} and in Johannesburg for {_fmt_r(sa_price_zar)}. "
        f"The current exchange rate is {sym} 1 = R {_fmt_dec(rate, 2)}. "
        f"Determine in which country the smartphone is cheaper, and by how much in South African Rand."
    )
    worked = (
        f"**Step 1 — Convert UK price to ZAR:**\n"
        f"$\\text{{London price in ZAR}} = {uk_price_gbp} \\times {_fmt_dec(rate, 2)} = {_fmt_r(uk_in_zar)}$\n\n"
        f"**Step 2 — Compare with Johannesburg price:**\n"
        f"Johannesburg price: {_fmt_r(sa_price_zar)}\n"
        f"London price: {_fmt_r(uk_in_zar)}\n\n"
        f"**Step 3 — Difference:**\n"
        f"$|{_fmt_r(uk_in_zar)} - {_fmt_r(sa_price_zar)}| = {_fmt_r(diff)}$\n\n"
        f"**Conclusion:** Cheaper in **{ans}**."
    )
    return _build_typed_math(
        rng,
        qid_prefix="fin25",
        subskill="25_foreign_exchange_cross_price_comparison",
        title="Foreign Exchange: Price Comparison Between Two Countries",
        prompt=prompt,
        ans_str=ans,
        worked=worked,
        marks=4,
        hints={
            "tier_1": f"Convert the London price from {sym} to Rand first using {sym} 1 = R {_fmt_dec(rate, 2)}.",
            "tier_2": f"London price in ZAR = {uk_price_gbp} * {_fmt_dec(rate, 2)} = {_fmt_r(uk_in_zar)}.",
            "tier_3": f"Compare with {_fmt_r(sa_price_zar)} and calculate the difference: {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Converts foreign price to ZAR", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Compares both prices in the same currency", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Identifies cheaper country ({cheaper_place})", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Correct difference {_fmt_r(diff)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["compared_raw_currency_numbers_without_converting"],
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_simple_interest_accumulated_amount": build_01_simple_interest_accumulated_amount,
    "02_simple_interest_earned_only": build_02_simple_interest_earned_only,
    "03_simple_interest_solve_for_principal": build_03_simple_interest_solve_for_principal,
    "04_simple_interest_solve_for_interest_rate": build_04_simple_interest_solve_for_interest_rate,
    "05_simple_interest_solve_for_time_period": build_05_simple_interest_solve_for_time_period,
    "06_simple_interest_months_conversion": build_06_simple_interest_months_conversion,
    "07_simple_interest_doubling_investment": build_07_simple_interest_doubling_investment,
    "08_compound_interest_annual_accumulation": build_08_compound_interest_annual_accumulation,
    "09_compound_interest_interest_earned_only": build_09_compound_interest_interest_earned_only,
    "10_compound_interest_solve_for_principal": build_10_compound_interest_solve_for_principal,
    "11_compound_interest_solve_for_interest_rate": build_11_compound_interest_solve_for_interest_rate,
    "12_simple_vs_compound_interest_difference": build_12_simple_vs_compound_interest_difference,
    "13_hire_purchase_deposit_calculation": build_13_hire_purchase_deposit_calculation,
    "14_hire_purchase_loan_principal": build_14_hire_purchase_loan_principal,
    "15_hire_purchase_total_repayment": build_15_hire_purchase_total_repayment,
    "16_hire_purchase_monthly_instalment": build_16_hire_purchase_monthly_instalment,
    "17_hire_purchase_total_cost_of_agreement": build_17_hire_purchase_total_cost_of_agreement,
    "18_hire_purchase_cost_of_credit_difference": build_18_hire_purchase_cost_of_credit_difference,
    "19_hire_purchase_insurance_and_admin_fee": build_19_hire_purchase_insurance_and_admin_fee,
    "20_inflation_future_price_compound_growth": build_20_inflation_future_price_compound_growth,
    "21_inflation_past_price_reverse_calculation": build_21_inflation_past_price_reverse_calculation,
    "22_population_compound_growth": build_22_population_compound_growth,
    "23_foreign_exchange_convert_zar_to_foreign": build_23_foreign_exchange_convert_zar_to_foreign,
    "24_foreign_exchange_convert_foreign_to_zar": build_24_foreign_exchange_convert_foreign_to_zar,
    "25_foreign_exchange_cross_price_comparison": build_25_foreign_exchange_cross_price_comparison,
}
