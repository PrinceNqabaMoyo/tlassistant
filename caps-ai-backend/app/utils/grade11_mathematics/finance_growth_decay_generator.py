"""Grade 11 Mathematics — Finance, Growth and Decay (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (Paper 1, Question 6 / 7: 10–15 marks):
- Reducing-balance depreciation (A = P(1 - i)^n) vs Straight-line depreciation (A = P(1 - in)).
- Nominal vs Effective interest rate conversions (1 + i_eff = (1 + i_nom / m)^m).
- Multi-stage timelines with deposits, withdrawals, and compounding rate changes.
Supports full 10-mark compound exam questions and atomic 3-mark / 4-mark elementary sub-drills for adaptive scaffolding.
Zero-LLM: 100% deterministic Python & SymPy calculations with South African comma decimals ({,}).
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade11_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    num,
    rng,
    solution_graph,
    step,
    to_latex,
)

TOPIC = "grade11_math_finance"
LO = "math11_finance_growth_decay"

SA_NAMES = ["Bongani", "Thabo", "Nomsa", "Sipho", "Lerato", "Zanele", "Kagiso", "Nandi", "Andile", "Mpho"]
ASSETS = ["delivery vehicle", "printing machine", "industrial generator", "packaging equipment", "tractor"]


# --------------------------------------------------------------------------- #
# Sub-drill 1: elementary_depreciation (3 marks)
# --------------------------------------------------------------------------- #
def _build_depreciation_drill(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding drill: Reducing-balance or straight-line depreciation."""
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(12, 35) * 10000  # R 120 000 to R 350 000
    n_years = r.randint(3, 6)
    rate_percent = r.choice([10, 12, 14, 15, 17, 20])
    i_dec = rate_percent / 100.0

    mode_choice = r.choice(["reducing_balance", "straight_line", "solve_rate"])

    if mode_choice == "reducing_balance":
        book_val = p_val * ((1.0 - i_dec) ** n_years)
        ans_round = round(book_val, 2)
        ans_str = num(ans_round, 2)
        p_str = num(p_val)
        rate_str = num(rate_percent)

        prompt = (
            f"{name} purchased a new {asset} for R {p_str}. "
            f"The value of the {asset} depreciates at a rate of {rate_str}% per annum on a reducing-balance basis. "
            f"Calculate the book value of the {asset} at the end of {n_years} years. "
            f"Round off your answer to TWO decimal places."
        )

        steps = [
            step(
                from_latex=r"A = P(1 - i)^n",
                to_latex_str=rf"A = {p_str}\left(1 - \frac{{{rate_str}}}{{100}}\right)^{{{n_years}}}",
                op="substitute known values into reducing balance formula",
                rule="reducing balance depreciation formula",
            ),
            step(
                from_latex=rf"A = {p_str}(1 - {num(i_dec, 2)})^{{{n_years}}}",
                to_latex_str=rf"A = {p_str}({num(round(1.0 - i_dec, 2), 2)})^{{{n_years}}}",
                op="evaluate bracket base",
                rule="subtraction",
            ),
            step(
                from_latex=rf"A = {p_str}({num(round(1.0 - i_dec, 2), 2)})^{{{n_years}}}",
                to_latex_str=rf"\text{{R }} {ans_str}",
                op="calculate final book value and round to cents",
                rule="arithmetic power and multiplication",
            ),
        ]

        canonical = solution_graph(
            goal=f"calculate reducing balance book value after {n_years} years",
            steps=steps,
            final_latex=rf"\text{{R }} {ans_str}",
        )

        marking_schema = {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Correct formula quote and substitution: A = P(1 - i)^n", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct substitution of i = {i_dec} and n = {n_years}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct final book value: R {ans_str}", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "used_simple_decay_instead_of_reducing_balance", "penalty": -2},
                {"rule": "rounding_error", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        }

        hints = {
            "nudge": "Use the reducing-balance decay formula $A = P(1 - i)^n$.",
            "concept": "Reducing-balance depreciation applies the percentage rate to the remaining book value at each step, so $A = P(1 - i)^n$.",
            "breakdown": f"1. Write $A = P(1 - i)^n$.\n2. Substitute $P = {p_str}$, $i = {num(i_dec, 2)}$, $n = {n_years}$.\n3. Compute $A = {p_str}({num(round(1.0 - i_dec, 2), 2)})^{{{n_years}}} = \\text{{R }} {ans_str}$.",
        }

        misconception_tags = ["used_simple_decay_instead_of_reducing_balance", "decay_added_instead_of_subtracted"]

    elif mode_choice == "straight_line":
        book_val = p_val * (1.0 - i_dec * n_years)
        ans_round = round(book_val, 2)
        ans_str = num(ans_round, 2)
        p_str = num(p_val)
        rate_str = num(rate_percent)

        prompt = (
            f"A business purchased a {asset} for R {p_str}. "
            f"The {asset} depreciates on the straight-line method at {rate_str}% per annum. "
            f"Determine the book value of the {asset} after {n_years} years."
        )

        steps = [
            step(
                from_latex=r"A = P(1 - in)",
                to_latex_str=rf"A = {p_str}\left(1 - {num(i_dec, 2)} \times {n_years}\right)",
                op="substitute known values into straight-line depreciation formula",
                rule="straight-line depreciation formula",
            ),
            step(
                from_latex=rf"A = {p_str}(1 - {num(round(i_dec * n_years, 2), 2)})",
                to_latex_str=rf"\text{{R }} {ans_str}",
                op="evaluate linear decay and multiply by principal",
                rule="arithmetic multiplication and subtraction",
            ),
        ]

        canonical = solution_graph(
            goal=f"calculate straight line book value after {n_years} years",
            steps=steps,
            final_latex=rf"\text{{R }} {ans_str}",
        )

        marking_schema = {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Correct formula quote and substitution: A = P(1 - in)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct substitution: i = {i_dec} and n = {n_years}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct final book value: R {ans_str}", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "used_reducing_balance_instead_of_straight_line", "penalty": -2},
            ],
            "carry_forward_rule": "consequential_accuracy",
        }

        hints = {
            "nudge": "Straight-line depreciation uses the simple decay formula $A = P(1 - in)$.",
            "concept": "Under straight-line depreciation, the asset loses a constant fixed amount of value each year based on original cost $P$.",
            "breakdown": f"1. Formula: $A = P(1 - in)$.\n2. Substitute $P = {p_str}$, $i = {num(i_dec, 2)}$, $n = {n_years}$.\n3. Calculate $A = {p_str}(1 - {num(round(i_dec*n_years, 2), 2)}) = \\text{{R }} {ans_str}$.",
        }

        misconception_tags = ["used_reducing_balance_instead_of_straight_line", "decay_added_instead_of_subtracted"]

    else:
        # Solve for rate i under reducing balance
        end_val = p_val * ((1.0 - i_dec) ** n_years)
        end_round = round(end_val, 2)
        end_str = num(end_round, 2)
        p_str = num(p_val)

        prompt = (
            f"An asset was bought for R {p_str}. After {n_years} years of reducing-balance depreciation, "
            f"its book value is R {end_str}. Calculate the annual rate of depreciation as a percentage. "
            f"Round off your answer to ONE decimal place."
        )

        steps = [
            step(
                from_latex=rf"{end_str} = {p_str}(1 - i)^{{{n_years}}}",
                to_latex_str=rf"(1 - i)^{{{n_years}}} = \frac{{{end_str}}}{{{p_str}}}",
                op="divide both sides by principal P",
                rule="algebraic transposition",
            ),
            step(
                from_latex=rf"1 - i = \sqrt[{{{n_years}}}]" + rf"{{\frac{{{end_str}}}{{{p_str}}}}}",
                to_latex_str=rf"i = 1 - \sqrt[{{{n_years}}}]" + rf"{{\frac{{{end_str}}}{{{p_str}}}}}",
                op="take the nth root and isolate i",
                rule="nth root property",
            ),
            step(
                from_latex=rf"i \approx {num(i_dec, 4)}",
                to_latex_str=rf"r = {num(rate_percent, 1)}\%",
                op="convert decimal to percentage",
                rule="percentage conversion",
            ),
        ]

        canonical = solution_graph(
            goal="solve for annual reducing-balance depreciation rate",
            steps=steps,
            final_latex=rf"{num(rate_percent, 1)}\%",
        )

        marking_schema = {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Correct substitution into A = P(1 - i)^n", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct algebraic isolation of (1 - i) with nth root", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct depreciation rate: {rate_percent}%", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "rounding_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        }

        hints = {
            "nudge": "Substitute $A$, $P$, and $n$ into $A = P(1 - i)^n$ and solve for $i$.",
            "concept": "Divide by $P$ first: $\\frac{A}{P} = (1 - i)^n$. Then take the $n$-th root: $1 - i = \\sqrt[n]{\\frac{A}{P}}$, so $i = 1 - \\sqrt[n]{\\frac{A}{P}}$.",
            "breakdown": f"1. $\\frac{{{end_str}}}{{{p_str}}} = (1 - i)^{{{n_years}}}$.\n2. $1 - i = ({end_str} / {p_str})^{{1/{n_years}}}$.\n3. $i = {num(i_dec, 3)} \\implies r = {num(rate_percent, 1)}\\%$.",
        }

        misconception_tags = ["forgot_to_take_nth_root", "confused_decay_rate_with_growth"]

    return make_math_question(
        prefix="fin_depr",
        topic=TOPIC,
        subskill="elementary_depreciation",
        learning_objective_id=f"{LO}_depreciation",
        prompt=prompt,
        prompt_latex=r"A = P(1 - i)^n",
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=misconception_tags,
        keywords=["depreciation", "reducing-balance", "straight-line", "book value", "finance"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_depreciation",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Sub-drill 2: elementary_effective_rate (3 marks)
# --------------------------------------------------------------------------- #
def _build_effective_rate_drill(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding drill: Nominal to effective interest rate conversion."""
    freq_choices = [
        ("monthly", 12, "per month"),
        ("quarterly", 4, "per quarter"),
        ("half-yearly (semi-annually)", 2, "per half-year"),
    ]
    freq_name, m, freq_desc = r.choice(freq_choices)
    nom_rate = r.choice([8.5, 9.0, 9.6, 10.2, 10.5, 11.4, 12.0, 12.5, 13.2])
    i_nom = nom_rate / 100.0

    # 1 + i_eff = (1 + i_nom / m)^m => i_eff = (1 + i_nom / m)^m - 1
    i_eff = ((1.0 + (i_nom / m)) ** m) - 1.0
    eff_rate_percent = i_eff * 100.0
    eff_round = round(eff_rate_percent, 2)

    nom_str = num(nom_rate, 1 if nom_rate % 1 != 0 else 0)
    eff_str = num(eff_round, 2)

    prompt = (
        f"A bank offers an investment account at an interest rate of {nom_str}% per annum, compounded {freq_name}. "
        f"Calculate the effective annual interest rate. "
        f"Give your answer as a percentage rounded to TWO decimal places."
    )

    steps = [
        step(
            from_latex=r"1 + i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{m}\right)^m",
            to_latex_str=rf"1 + i_{{\text{{eff}}}} = \left(1 + \frac{{{nom_str}\%}}{{{m}}}\right)^{{{m}}}",
            op="state conversion formula and substitute compounding frequency",
            rule="nominal to effective interest rate relationship",
        ),
        step(
            from_latex=rf"1 + i_{{\text{{eff}}}} = \left(1 + \frac{{{num(i_nom, 4)}}}{{{m}}}\right)^{{{m}}}",
            to_latex_str=rf"1 + i_{{\text{{eff}}}} = \left(1 + {num(round(i_nom/m, 6), 6)}\right)^{{{m}}}",
            op="divide nominal rate by compounding frequency m",
            rule="periodic interest rate calculation",
        ),
        step(
            from_latex=rf"i_{{\text{{eff}}}} = ({num(round(1.0 + i_nom/m, 6), 6)})^{{{m}}} - 1",
            to_latex_str=rf"i_{{\text{{eff}}}} \approx {num(round(i_eff, 6), 6)} \implies r_{{\text{{eff}}}} = {eff_str}\%",
            op="subtract 1 and convert decimal to percentage",
            rule="effective percentage conversion",
        ),
    ]

    canonical = solution_graph(
        goal=f"convert nominal rate {nom_str}% compounded {freq_name} to effective rate",
        steps=steps,
        final_latex=rf"{eff_str}\%",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct formula and substitution: 1 + i_eff = (1 + {i_nom}/{m})^{m}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Correct periodic calculation: (1 + {round(i_nom/m, 5)})^{m} - 1", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct effective annual percentage: {eff_str}%", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "inverted_compounding_frequency", "penalty": -1},
            {"rule": "forgot_to_subtract_one", "penalty": -1},
            {"rule": "rounding_error", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": r"Use the standard conversion formula: $1 + i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{m}\right)^m$.",
        "concept": f"Since interest is compounded {freq_name}, $m = {m}$. The effective rate is the actual interest earned over a full year.",
        "breakdown": f"1. Formula: $1 + i_{{\\text{{eff}}}} = \\left(1 + \\frac{{{num(i_nom, 4)}}}{{{m}}}\\right)^{{{m}}}$.\n2. Compute $\\left(1 + {num(round(i_nom/m, 5), 5)}\\right)^{{{m}}} - 1 = {num(round(i_eff, 4), 4)}$.\n3. Multiply by $100\\%$ to get ${eff_str}\\%$.",
    }

    return make_math_question(
        prefix="fin_eff_rate",
        topic=TOPIC,
        subskill="elementary_effective_rate",
        learning_objective_id=f"{LO}_nominal_effective_rate",
        prompt=prompt,
        prompt_latex=r"1 + i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{m}\right)^m",
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["inverted_compounding_frequency", "forgot_to_subtract_one", "confused_nominal_effective_rate"],
        keywords=["nominal interest", "effective interest rate", "compounding frequency", "finance"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_effective_rate",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Sub-drill 3: elementary_timeline_step (4 marks)
# --------------------------------------------------------------------------- #
def _build_timeline_step_drill(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding drill: 2-period investment timeline with deposit or withdrawal and rate change."""
    name = r.choice(SA_NAMES)
    p_val = r.randint(20, 60) * 1000  # R 20 000 to R 60 000
    p_str = num(p_val)

    # Period 1: n1 years at r1% compounded monthly
    n1 = r.randint(2, 3)
    r1 = r.choice([8.0, 9.0, 9.6, 10.0])
    i1 = r1 / 1200.0

    # Period 2: n2 years at r2% compounded quarterly
    n2 = r.randint(2, 3)
    r2 = r.choice([10.5, 11.0, 11.5, 12.0])
    i2 = r2 / 400.0

    # Transaction at T1 (end of Period 1)
    is_deposit = r.choice([True, False])
    trans_val = r.randint(5, 15) * 1000
    trans_str = num(trans_val)
    trans_action = "deposits" if is_deposit else "withdraws"
    trans_sign = "+" if is_deposit else "-"

    total_years = n1 + n2

    # Stepwise calculation:
    bal_t1_before = p_val * ((1.0 + i1) ** (n1 * 12))
    bal_t1_after = bal_t1_before + trans_val if is_deposit else bal_t1_before - trans_val
    final_balance = bal_t1_after * ((1.0 + i2) ** (n2 * 4))
    final_round = round(final_balance, 2)
    final_str = num(final_round, 2)

    prompt = (
        f"{name} invests R {p_str} in a savings account paying {num(r1, 1)}% p.a. compounded monthly for {n1} years. "
        f"At the end of year {n1}, {name} {trans_action} R {trans_str}, and the interest rate changes to "
        f"{num(r2, 1)}% p.a. compounded quarterly for the remaining {n2} years. "
        f"Calculate the accumulated balance in the account at the end of {total_years} years. "
        f"Round off your answer to the nearest cent."
    )

    t1_before_str = num(round(bal_t1_before, 2), 2)
    t1_after_str = num(round(bal_t1_after, 2), 2)
    n1_months = n1 * 12
    n2_quarters = n2 * 4

    steps = [
        step(
            from_latex=rf"A_{{1}} = {p_str}\left(1 + \frac{{{num(r1, 1)}}}{{1200}}\right)^{{{n1_months}}}",
            to_latex_str=rf"A_{{1}} = \text{{R }} {t1_before_str}",
            op=f"calculate balance at end of year {n1} before transaction",
            rule="compound interest formula",
        ),
        step(
            from_latex=rf"\text{{Balance at }} T_{{{n1}}} = {t1_before_str} {trans_sign} {trans_str}",
            to_latex_str=rf"= \text{{R }} {t1_after_str}",
            op=f"apply {trans_action} of R {trans_str}",
            rule="account balance adjustment",
        ),
        step(
            from_latex=rf"A_{{\text{{final}}}} = {t1_after_str}\left(1 + \frac{{{num(r2, 1)}}}{{400}}\right)^{{{n2_quarters}}}",
            to_latex_str=rf"= \text{{R }} {final_str}",
            op=f"compound adjusted balance for remaining {n2} years at new rate",
            rule="compound interest under new rate",
        ),
    ]

    canonical = solution_graph(
        goal=f"calculate accumulated balance after {total_years} years with rate change and transaction",
        steps=steps,
        final_latex=rf"\text{{R }} {final_str}",
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": rf"Compounding initial principal P for {n1} years: P(1 + r1/1200)^{{{n1*12}}}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Accurate application of transaction ({trans_sign} R {trans_str})", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"Compounding second period for {n2} years: (1 + r2/400)^{{{n2*4}}}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": rf"Correct final accumulated balance: R {final_str}", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "added_withdrawal_or_subtracted_deposit", "penalty": -1},
            {"rule": "incorrect_compounding_periods", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": f"Calculate the balance at year {n1} first, adjust for the {trans_action}, then compound for the remaining {n2} years.",
        "concept": "A timeline can be solved period-by-period: calculate the value just before the event, apply the transaction, and carry forward as the new principal.",
        "breakdown": (
            f"1. Year {n1} balance: ${p_str}(1 + {num(r1,1)}/1200)^{{{n1*12}}} = \\text{{R }} {t1_before_str}$.\n"
            f"2. Apply {trans_action}: $\\text{{R }} {t1_before_str} {trans_sign} \\text{{R }} {trans_str} = \\text{{R }} {t1_after_str}$.\n"
            f"3. Compound for {n2} years: ${t1_after_str}(1 + {num(r2,1)}/400)^{{{n2*4}}} = \\text{{R }} {final_str}$."
        ),
    }

    diag = {
        "kind": "timeline_finance",
        "total_years": total_years,
        "events": [
            {"year": 0, "label": f"Deposit: R {p_str}", "rate": f"{num(r1, 1)}% p.a. monthly"},
            {"year": n1, "label": f"{trans_action.capitalize()}: R {trans_str}", "rate": f"Rate changes to {num(r2, 1)}% p.a. quarterly"},
            {"year": total_years, "label": f"Final Balance: R {final_str}"},
        ],
    }

    return make_math_question(
        prefix="fin_time_step",
        topic=TOPIC,
        subskill="elementary_timeline_step",
        learning_objective_id=f"{LO}_timeline_step",
        prompt=prompt,
        prompt_latex=rf"A = P(1 + i)^n",
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        diagram_spec=diag,
        misconception_tags=["added_instead_of_subtracted_withdrawal", "incorrect_compounding_periods", "confused_rates_between_stages"],
        keywords=["timeline", "multi-stage investment", "deposit", "withdrawal", "interest rate change"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=6,
        mode="elementary_timeline_step",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Compound Exam Ceiling: mode="compound" (10 marks)
# --------------------------------------------------------------------------- #
def _build_compound_finance_exam(r, difficulty: str) -> Dict[str, Any]:
    """10-Mark NSC Paper 1 Comprehensive Finance Examination Question:
    Part 1 (3 marks): Reducing-balance depreciation vs straight-line depreciation comparison.
    Part 2 (3 marks): Nominal to effective interest rate conversion.
    Part 3 (4 marks): Full multi-transaction timeline (Initial P, deposit, rate change, withdrawal).
    """
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)

    # ------------------ Part 1: Depreciation (3 marks) ------------------ #
    p_asset = r.randint(22, 45) * 10000  # e.g. R 280 000
    n_depr = r.randint(4, 5)
    r_red = r.choice([12, 14, 15, 16, 18])
    r_sl = r.choice([10, 11, 12, 13])
    i_red = r_red / 100.0
    i_sl = r_sl / 100.0

    book_red = p_asset * ((1.0 - i_red) ** n_depr)
    book_sl = p_asset * (1.0 - i_sl * n_depr)
    diff_depr = abs(book_sl - book_red)

    p_asset_str = num(p_asset)
    book_red_str = num(round(book_red, 2), 2)
    book_sl_str = num(round(book_sl, 2), 2)
    diff_str = num(round(diff_depr, 2), 2)

    # ------------------ Part 2: Nominal vs Effective Rate (3 marks) ----- #
    r_nom = r.choice([9.6, 10.2, 10.8, 11.4, 12.0])
    m_nom = 12  # monthly
    i_nom = r_nom / 100.0
    i_eff = ((1.0 + i_nom / m_nom) ** m_nom) - 1.0
    r_eff_percent = i_eff * 100.0
    r_eff_str = num(round(r_eff_percent, 2), 2)
    r_nom_str = num(r_nom, 1 if r_nom % 1 != 0 else 0)

    # ------------------ Part 3: Complex Timeline (4 marks) -------------- #
    p_inv = r.randint(40, 80) * 1000  # Initial deposit e.g. R 50 000
    t_dep = 2  # Deposit at T2 (2 years)
    d_val = r.randint(15, 30) * 1000  # Additional deposit e.g. R 20 000
    t_rate_change = 3  # Rate changes at T3 (3 years)
    r_time1 = r.choice([8.4, 9.0, 9.6])  # Period 1: compounded monthly
    i_time1 = r_time1 / 1200.0
    r_time2 = r.choice([10.4, 10.8, 11.2])  # Period 2: compounded quarterly
    i_time2 = r_time2 / 400.0
    t_w = 5  # Withdrawal at T5 (5 years)
    w_val = r.randint(10, 20) * 1000  # Withdrawal e.g. R 15 000
    t_final = 7  # Total duration 7 years

    # Timeline stage calculation:
    # 1. Initial deposit P_inv grows from 0 to 3 under rate 1 (36 months), then 3 to 7 under rate 2 (16 quarters)
    term1 = p_inv * ((1.0 + i_time1) ** (3 * 12)) * ((1.0 + i_time2) ** (4 * 4))
    # 2. Deposit D made at T=2: grows from 2 to 3 under rate 1 (12 months), then 3 to 7 under rate 2 (16 quarters)
    term2 = d_val * ((1.0 + i_time1) ** (1 * 12)) * ((1.0 + i_time2) ** (4 * 4))
    # 3. Withdrawal W made at T=5: subtracted, compounded from 5 to 7 under rate 2 (8 quarters)
    term3 = w_val * ((1.0 + i_time2) ** (2 * 4))

    total_accumulated = term1 + term2 - term3
    total_round = round(total_accumulated, 2)
    total_str = num(total_round, 2)

    p_inv_str = num(p_inv)
    d_str = num(d_val)
    w_str = num(w_val)
    r1_str = num(r_time1, 1 if r_time1 % 1 != 0 else 0)
    r2_str = num(r_time2, 1 if r_time2 % 1 != 0 else 0)

    prompt = (
        f"QUESTION 1 (10 MARKS)\n\n"
        f"{name} operates an expanding logistics business and manages both capital assets and investments.\n\n"
        f"1.1 The business purchased a new {asset} for R {p_asset_str}.\n"
        f"    (a) Calculate the book value of the {asset} after {n_depr} years if depreciation is calculated at "
        f"{r_red}% p.a. on a reducing-balance basis. (2)\n"
        f"    (b) Determine how much greater or smaller the book value would be if straight-line depreciation at "
        f"{r_sl}% p.a. was applied over the same {n_depr}-year period instead. (1)\n\n"
        f"1.2 To accumulate capital, the company considers an investment portfolio offering an interest rate of "
        f"{r_nom_str}% p.a., compounded monthly. Calculate the effective annual interest rate, correct to TWO decimal places. (3)\n\n"
        f"1.3 {name} deposits R {p_inv_str} into a dedicated growth fund at $T_0$.\n"
        f"    - At $T_1$ ({t_dep} years later), {name} deposits an additional R {d_str} into the account.\n"
        f"    - At $T_2$ ({t_rate_change} years from the initial deposit), the interest rate changes from {r1_str}% p.a. "
        f"compounded monthly to {r2_str}% p.a. compounded quarterly.\n"
        f"    - At $T_3$ ({t_w} years from the initial deposit), {name} withdraws R {w_str} for emergency fleet servicing.\n"
        f"    Calculate the accumulated balance in the investment account at the end of {t_final} years. (4)"
    )

    steps = [
        # Part 1.1 (a)
        step(
            from_latex=rf"A = {p_asset_str}\left(1 - \frac{{{r_red}}}{{100}}\right)^{{{n_depr}}}",
            to_latex_str=rf"= \text{{R }} {book_red_str}",
            op="calculate reducing-balance book value",
            rule="reducing balance depreciation formula",
        ),
        # Part 1.1 (b)
        step(
            from_latex=rf"A_{{\text{{sl}}}} = {p_asset_str}\left(1 - \frac{{{r_sl}}}{{100}} \times {n_depr}\right)",
            to_latex_str=rf"= \text{{R }} {book_sl_str} \implies |\text{{Difference}}| = |{book_sl_str} - {book_red_str}| = \text{{R }} {diff_str}",
            op="calculate straight-line book value and difference",
            rule="straight-line depreciation and difference comparison",
        ),
        # Part 1.2
        step(
            from_latex=r"1 + i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{12}\right)^{12}",
            to_latex_str=rf"1 + i_{{\text{{eff}}}} = \left(1 + \frac{{{num(i_nom, 4)}}}{{12}}\right)^{{12}} \implies r_{{\text{{eff}}}} = {r_eff_str}\%",
            op="convert nominal monthly rate to effective annual rate",
            rule="nominal-effective rate conversion formula",
        ),
        # Part 1.3
        step(
            from_latex=(
                rf"A = {p_inv_str}\left(1+\frac{{{r1_str}}}{{1200}}\right)^{{36}}\left(1+\frac{{{r2_str}}}{{400}}\right)^{{16}} "
                rf"+ {d_str}\left(1+\frac{{{r1_str}}}{{1200}}\right)^{{12}}\left(1+\frac{{{r2_str}}}{{400}}\right)^{{16}} "
                rf"- {w_str}\left(1+\frac{{{r2_str}}}{{400}}\right)^{{8}}"
            ),
            to_latex_str=rf"= \text{{R }} {total_str}",
            op="compound all timeline cash flows and subtract compounded withdrawal",
            rule="continuous multi-stage timeline equation",
            common_errors=["added_withdrawal_instead_of_subtracting", "incorrect_number_of_compounding_periods"],
        ),
    ]

    canonical = solution_graph(
        goal="complete 10-mark comprehensive Grade 11 finance exam question",
        steps=steps,
        final_latex=(
            rf"1.1(a) \text{{ R }} {book_red_str}, \; 1.1(b) \text{{ R }} {diff_str}; \quad "
            rf"1.2 \; {r_eff_str}\%; \quad "
            rf"1.3 \text{{ R }} {total_str}"
        ),
    )

    marking_schema = {
        "total_marks": 10,
        "marking_points": [
            # 1.1 (a) - 2 marks
            {"id": "mp1", "desc": rf"1.1(a) Correct substitution: A = {p_asset_str}(1 - {r_red}/100)^{{{n_depr}}}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"1.1(a) Correct reducing-balance book value: R {book_red_str}", "marks": 1, "editable": True},
            # 1.1 (b) - 1 mark
            {"id": "mp3", "desc": rf"1.1(b) Straight-line calculation and difference: R {diff_str}", "marks": 1, "editable": True},
            # 1.2 - 3 marks
            {"id": "mp4", "desc": rf"1.2 Correct formula: 1 + i_eff = (1 + i_nom/12)^12", "marks": 1, "editable": True},
            {"id": "mp5", "desc": rf"1.2 Correct substitution and decimal expansion: (1 + {round(i_nom/12, 5)})^12 - 1", "marks": 1, "editable": True},
            {"id": "mp6", "desc": rf"1.2 Correct effective percentage: {r_eff_str}%", "marks": 1, "editable": True},
            # 1.3 - 4 marks
            {"id": "mp7", "desc": rf"1.3 Correct compounding of P = R {p_inv_str} over both rate periods", "marks": 1, "editable": True},
            {"id": "mp8", "desc": rf"1.3 Correct compounding of deposit D = R {d_str} over both rate periods", "marks": 1, "editable": True},
            {"id": "mp9", "desc": rf"1.3 Correct subtraction and compounding of withdrawal W = R {w_str}", "marks": 1, "editable": True},
            {"id": "mp10", "desc": rf"1.3 Correct final balance: R {total_str}", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "added_withdrawal", "penalty": -1},
            {"rule": "incorrect_frequency_conversion", "penalty": -1},
            {"rule": "rounding_error", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Break down each question part: 1.1 uses depreciation formulas, 1.2 converts nominal to effective rate, and 1.3 requires a timeline equation.",
        "concept": (
            "Key CAPS formulas:\n"
            "• Reducing-balance decay: $A = P(1 - i)^n$\n"
            "• Straight-line decay: $A = P(1 - in)$\n"
            "• Effective rate: $1 + i_{\\text{eff}} = \\left(1 + \\frac{i_{\\text{nom}}}{m}\\right)^m$\n"
            "• Timeline: compound each payment/withdrawal to the horizon $T_n$ individually."
        ),
        "breakdown": (
            f"1.1(a) $A = {p_asset_str}(1 - {r_red}/100)^{{{n_depr}}} = \\text{{R }} {book_red_str}$.\n"
            f"1.1(b) Straight-line: ${p_asset_str}(1 - {r_sl}/100 \\times {n_depr}) = \\text{{R }} {book_sl_str}$. "
            f"Difference $= \\text{{R }} {diff_str}$.\n"
            f"1.2 $1 + i_{{\\text{{eff}}}} = (1 + {num(i_nom, 4)}/12)^{{12}} \\implies r_{{\\text{{eff}}}} = {r_eff_str}\\%$.\n"
            f"1.3 Compound $P$, add compounded $D$, subtract compounded $W$: Final balance $= \\text{{R }} {total_str}$."
        ),
    }

    diag = {
        "kind": "timeline_finance",
        "total_years": t_final,
        "events": [
            {"year": 0, "label": f"P = R {p_inv_str}", "type": "initial_deposit", "rate": f"{r1_str}% p.a. monthly"},
            {"year": t_dep, "label": f"+ Deposit R {d_str}", "type": "deposit", "rate": f"{r1_str}% p.a. monthly"},
            {"year": t_rate_change, "label": "Rate change", "type": "rate_change", "rate": f"Becomes {r2_str}% p.a. quarterly"},
            {"year": t_w, "label": f"- Withdrawal R {w_str}", "type": "withdrawal", "rate": f"{r2_str}% p.a. quarterly"},
            {"year": t_final, "label": f"Final Balance = R {total_str}", "type": "balance"},
        ],
    }

    return make_math_question(
        prefix="fin_exam_compound",
        topic=TOPIC,
        subskill="finance_growth_decay_compound",
        learning_objective_id=f"{LO}_compound_exam",
        prompt=prompt,
        prompt_latex=r"A = P(1 \pm i)^n",
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        diagram_spec=diag,
        misconception_tags=[
            "used_simple_decay_instead_of_reducing_balance",
            "confused_nominal_effective_rate",
            "added_instead_of_subtracted_withdrawal",
            "incorrect_compounding_periods",
        ],
        keywords=["reducing balance", "straight-line depreciation", "effective interest", "timeline problem", "NSC Paper 1"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=15,
        mode="compound",
        difficulty="hard",
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher & API
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_finance_exam,
    "elementary_depreciation": _build_depreciation_drill,
    "elementary_effective_rate": _build_effective_rate_drill,
    "elementary_timeline_step": _build_timeline_step_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 11 Finance questions meeting the 6-pillar contract."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_finance_exam)

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
