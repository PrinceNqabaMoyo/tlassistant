"""Grade 11 Mathematics — Finance, Growth and Decay: Archetypes 01 to 25.

Grounded strictly in:
- curriculum_docs_auto/Mathematics_Gr11/Term 3/01. Finance growth and decay.md
- Official South African National Curriculum Standards for Grade 11 Mathematics Paper 1.

Zero-LLM, 100% deterministic Python & SymPy calculations with South African comma decimals ({,}).
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

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

TOPIC_NAME = "Finance growth and decay"
TOPIC_ID = "grade11_math_finance"
LEARNING_OBJECTIVE_ID = "math11_finance_growth_decay"

SA_NAMES = [
    "Bongani", "Thabo", "Nomsa", "Sipho", "Lerato", "Zanele",
    "Kagiso", "Nandi", "Andile", "Mpho", "Tshepo", "Keletso",
    "Farai", "Lindiwe", "Sibusiso", "Mandla", "Ayanda", "Dineo"
]

ASSETS = [
    "delivery vehicle", "printing machine", "industrial generator",
    "packaging equipment", "tractor", "heavy-duty forklift",
    "commercial oven", "computing server rack", "milling machine"
]


def fmt_r(val: float | int) -> str:
    """Format currency in Rand with comma decimals and space thousands separator."""
    rounded = round(float(val), 2)
    s = f"{rounded:,.2f}".replace(",", " ").replace(".", ",")
    return f"R {s}"


def fmt_pct(val: float | int) -> str:
    """Format percentage with comma decimal."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return f"{int(val)}\\%"
    return f"{str(round(val, 2)).replace('.', ',')}\\%"


# Archetype 01: Straight-Line Depreciation — Book Value
def arch_01_straight_line_depreciation_book_value(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(15, 60) * 10000
    n_years = r.randint(3, 7)
    rate_pct = r.choice([10, 12, 12.5, 14, 15, 18, 20])
    i_dec = rate_pct / 100.0

    a_val = p_val * (1.0 - i_dec * n_years)
    p_str = num(p_val)
    rate_str = num(rate_pct)
    ans_str = num(round(a_val, 2), 2)

    prompt = (
        f"{name} purchased a new {asset} for R {p_str}. "
        f"The equipment depreciates at a rate of {rate_str}% per annum on a straight-line basis. "
        f"Calculate the book value (scrap value) of the {asset} at the end of {n_years} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} bought a {asset} for R }}{p_str}\text{{. It depreciates at }}{rate_str}\% "
        rf"\text{{ p.a. straight-line. Find the book value after }}{n_years}\text{{ years.}}"
    )

    steps = [
        step(from_latex=r"A = P(1 - in)", to_latex_str=rf"A = {p_str}\left(1 - \frac{{{rate_str}}}{{100}} \times {n_years}\right)", op="substitute into straight-line depreciation formula", rule="straight-line depreciation formula",),
        step(from_latex=rf"A = {p_str}(1 - {num(round(i_dec * n_years, 4))})", to_latex_str=rf"A = {p_str}({num(round(1.0 - i_dec * n_years, 4))})", op="evaluate the bracket", rule="arithmetic subtraction",),
        step(from_latex=rf"A = {p_str}({num(round(1.0 - i_dec * n_years, 4))})", to_latex_str=rf"\text{{R }} {ans_str}", op="multiply to determine final book value", rule="multiplication",),
    ]
    canonical = solution_graph(
        goal=f"calculate straight-line book value after {n_years} years",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Correct formula A = P(1 - in)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution of P = {p_str}, i = {rate_str}%, n = {n_years}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate final book value R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_01",
        topic=TOPIC_NAME,
        subskill="01_straight_line_depreciation_book_value",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Straight-line depreciation uses the simple decay formula: A = P(1 - in).",
            "concept": "Substitute the initial purchase price, the decimal depreciation rate, and the number of years.",
            "breakdown": f"A = {p_val}(1 - ({rate_pct}/100)({n_years})) = R {round(a_val, 2):.2f}.",
        },
        misconception_tags=["used_reducing_balance_instead_of_straight_line"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 02: Straight-Line Depreciation — Solve Initial Cost P
def arch_02_straight_line_depreciation_initial_cost(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(20, 80) * 10000
    n_years = r.randint(3, 6)
    rate_pct = r.choice([10, 12, 15, 16])
    i_dec = rate_pct / 100.0

    a_val = p_val * (1.0 - i_dec * n_years)
    a_str = num(round(a_val, 2), 2)
    rate_str = num(rate_pct)
    ans_str = num(p_val)

    prompt = (
        f"A {asset} has a book value of R {a_str} after {n_years} years. "
        f"Depreciation was calculated at {rate_str}% per annum on a straight-line basis. "
        f"Determine the original purchase price of the {asset}."
    )
    prompt_latex = (
        rf"\text{{A {asset} has book value R }}{a_str}\text{{ after }}{n_years}\text{{ years at }} "
        rf"{rate_str}\% \text{{ p.a. straight-line. Find the original purchase price }} P."
    )

    factor = round(1.0 - i_dec * n_years, 4)
    steps = [
        step(from_latex=r"A = P(1 - in)", to_latex_str=rf"{a_str} = P(1 - {num(i_dec)} \times {n_years})", op="substitute known values into straight-line decay equation", rule="formula substitution",),
        step(from_latex=rf"{a_str} = P({num(factor)})", to_latex_str=rf"P = \frac{{{a_str}}}{{{num(factor)}}}", op="isolate P by dividing by the bracket factor", rule="algebraic division",),
        step(from_latex=rf"P = \frac{{{a_str}}}{{{num(factor)}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate original purchase price", rule="arithmetic division",),
    ]
    canonical = solution_graph(
        goal=f"solve for original purchase price P",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Correct formula substitution: A = P(1 - in)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correctly isolates P = {a_str} / (1 - in)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate purchase price R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_02",
        topic=TOPIC_NAME,
        subskill="02_straight_line_depreciation_initial_cost",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Rearrange A = P(1 - in) to solve for P: P = A / (1 - in).",
            "concept": "Calculate the factor (1 - in) first, then divide the current book value by this factor.",
            "breakdown": f"P = {a_val} / (1 - ({rate_pct}/100)({n_years})) = R {p_val}.",
        },
        misconception_tags=["multiplied_instead_of_dividing_by_decay_factor"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 03: Straight-Line Depreciation — Solve Annual Rate i
def arch_03_straight_line_depreciation_rate(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(18, 50) * 10000
    n_years = r.randint(4, 8)
    rate_pct = r.choice([10, 12, 12.5, 15, 17.5, 20])
    i_dec = rate_pct / 100.0

    a_val = p_val * (1.0 - i_dec * n_years)
    p_str = num(p_val)
    a_str = num(round(a_val, 2), 2)
    ans_str = num(rate_pct)

    prompt = (
        f"{name}'s business bought a {asset} for R {p_str}. "
        f"After {n_years} years, its depreciated value is R {a_str} on a straight-line basis. "
        f"Calculate the annual rate of depreciation as a percentage."
    )
    prompt_latex = (
        rf"\text{{{name} bought a {asset} for R }}{p_str}\text{{. Book value after }}{n_years} "
        rf"\text{{ years is R }}{a_str}\text{{ (straight-line). Find the annual rate }} r\%."
    )

    ratio = round(a_val / p_val, 4)
    steps = [
        step(from_latex=r"A = P(1 - in)", to_latex_str=rf"{a_str} = {p_str}(1 - i \cdot {n_years})", op="substitute known parameters into straight-line depreciation formula", rule="formula substitution",),
        step(from_latex=rf"\frac{{{a_str}}}{{{p_str}}} = 1 - {n_years}i", to_latex_str=rf"{num(ratio)} = 1 - {n_years}i", op="divide both sides by P", rule="algebraic division",),
        step(from_latex=rf"{n_years}i = 1 - {num(ratio)}", to_latex_str=rf"i = \frac{{{num(round(1.0 - ratio, 4))}}}{{{n_years}}} = {num(i_dec)}", op="isolate and solve for i", rule="linear equation solving",),
        step(from_latex=rf"r = {num(i_dec)} \times 100\%", to_latex_str=rf"{ans_str}\%", op="convert decimal rate to percentage", rule="percentage conversion",),
    ]
    canonical = solution_graph(
        goal=f"solve for annual straight-line depreciation rate",
        steps=steps,
        final_latex=rf"{ans_str}\%",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 - in)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct substitution into equation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Correct simplification to isolate i", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate rate {ans_str}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_03",
        topic=TOPIC_NAME,
        subskill="03_straight_line_depreciation_rate",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\%",
        sample_answer=rf"{ans_str}%",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "From A = P(1 - in), rearrange to get i = (1 - A/P) / n.",
            "concept": "Divide A by P, subtract from 1, and divide the result by the number of years.",
            "breakdown": f"i = (1 - {a_val}/{p_val}) / {n_years} = {i_dec} -> {rate_pct}%.",
        },
        misconception_tags=["inverted_ratio_p_over_a"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 04: Straight-Line Depreciation — Solve Period n
def arch_04_straight_line_depreciation_years_to_scrap(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(25, 60) * 10000
    n_years = r.randint(4, 8)
    rate_pct = r.choice([10, 12, 12.5, 15])
    i_dec = rate_pct / 100.0

    a_val = p_val * (1.0 - i_dec * n_years)
    p_str = num(p_val)
    a_str = num(round(a_val, 2), 2)
    rate_str = num(rate_pct)
    ans_str = str(n_years)

    prompt = (
        f"A {asset} with an original cost of R {p_str} is depreciated at {rate_str}% per annum on a straight-line basis. "
        f"How many years will it take for the book value of the {asset} to reach R {a_str}?"
    )
    prompt_latex = (
        rf"\text{{Cost = R }}{p_str}\text{{, straight-line rate = }}{rate_str}\% \text{{ p.a. How many years to reach R }}{a_str}\text{{?}}"
    )

    drop = p_val - a_val
    annual_dep = p_val * i_dec
    steps = [
        step(from_latex=r"A = P(1 - in)", to_latex_str=rf"{a_str} = {p_str}(1 - {num(i_dec)}n)", op="substitute known values into formula", rule="formula substitution",),
        step(from_latex=rf"{p_str} - {a_str} = {p_str} \times {num(i_dec)} \times n", to_latex_str=rf"{num(drop)} = {num(annual_dep)}n", op="calculate total depreciation and annual depreciation", rule="linear rearrangement",),
        step(from_latex=rf"n = \frac{{{num(drop)}}}{{{num(annual_dep)}}}", to_latex_str=rf"{ans_str}\text{{ years}}", op="divide total depreciation by annual depreciation to find n", rule="division",),
    ]
    canonical = solution_graph(
        goal=f"solve for time period n in years",
        steps=steps,
        final_latex=rf"{ans_str}\text{{ years}}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 - in) and substitution", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct annual depreciation R {num(annual_dep)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate number of years n = {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_04",
        topic=TOPIC_NAME,
        subskill="04_straight_line_depreciation_years_to_scrap",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\text{{ years}}",
        sample_answer=rf"{ans_str} years",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "In straight-line depreciation, the asset loses the exact same Rand amount every single year.",
            "concept": "Total depreciation = P - A. Annual depreciation = P x i. Then n = Total depreciation / Annual depreciation.",
            "breakdown": f"Annual depreciation = {p_val} x {rate_pct}% = R {annual_dep}. n = ({p_val} - {a_val}) / {annual_dep} = {n_years} years.",
        },
        misconception_tags=["used_logarithm_formula_for_simple_decay"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 05: Straight-Line Depreciation — Zero or Scrap Threshold
def arch_05_straight_line_zero_or_scrap_threshold(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    rate_pct = r.choice([10, 12.5, 20, 25])
    i_dec = rate_pct / 100.0
    n_zero = round(1.0 / i_dec, 2)
    rate_str = num(rate_pct)
    n_str = num(int(n_zero) if n_zero.is_integer() else n_zero)

    prompt = (
        f"An enterprise writes down the value of its {asset}s using the straight-line method at {rate_str}% per annum. "
        f"After how many years will the book value of the {asset} reach R 0 (be completely written off)?"
    )
    prompt_latex = (
        rf"\text{{Straight-line depreciation at }}{rate_str}\% \text{{ p.a. Find }} n \text{{ when book value }} A = 0."
    )

    steps = [
        step(from_latex=r"A = P(1 - in)", to_latex_str=r"0 = P(1 - in)", op="set book value A = 0", rule="zero book value condition",),
        step(from_latex=r"1 - in = 0", to_latex_str=rf"in = 1 \implies n = \frac{{1}}{{i}} = \frac{{1}}{{{num(i_dec)}}}", op="solve for n in terms of rate i", rule="algebraic solution",),
        step(from_latex=rf"n = \frac{{1}}{{{num(i_dec)}}}", to_latex_str=rf"{n_str}\text{{ years}}", op="evaluate the reciprocal to find number of years", rule="arithmetic division",),
    ]
    canonical = solution_graph(
        goal=f"find years until asset is completely written off",
        steps=steps,
        final_latex=rf"{n_str}\text{{ years}}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Sets A = 0: 0 = P(1 - in)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Solves n = 1 / i", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate time period {n_str} years", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_05",
        topic=TOPIC_NAME,
        subskill="05_straight_line_zero_or_scrap_threshold",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{n_str}\text{{ years}}",
        sample_answer=rf"{n_str} years",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "When book value is 0, the total percentage written off is 100%.",
            "concept": "Set 1 - in = 0, which means n = 1 / i.",
            "breakdown": f"n = 100 / {rate_pct} = {n_zero} years.",
        },
        misconception_tags=["assumed_reducing_balance_reaches_zero"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 06: Reducing-Balance Depreciation — Book Value
def arch_06_reducing_balance_book_value_basic(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(15, 50) * 10000
    n_years = r.randint(3, 6)
    rate_pct = r.choice([12, 14, 15, 17, 18, 20])
    i_dec = rate_pct / 100.0

    a_val = p_val * ((1.0 - i_dec) ** n_years)
    p_str = num(p_val)
    rate_str = num(rate_pct)
    ans_str = num(round(a_val, 2), 2)

    prompt = (
        f"{name} bought a {asset} for R {p_str}. "
        f"Its value depreciates at a rate of {rate_str}% per annum on a reducing-balance basis. "
        f"Calculate the book value of the {asset} after {n_years} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} bought a {asset} for R }}{p_str}\text{{. Depreciation: }}{rate_str}\% "
        rf"\text{{ p.a. reducing balance. Find book value after }}{n_years}\text{{ years.}}"
    )

    base = round(1.0 - i_dec, 4)
    steps = [
        step(from_latex=r"A = P(1 - i)^n", to_latex_str=rf"A = {p_str}\left(1 - \frac{{{rate_str}}}{{100}}\right)^{{{n_years}}}", op="substitute known values into reducing balance formula", rule="reducing balance formula",),
        step(from_latex=rf"A = {p_str}({num(base)})^{{{n_years}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate power and multiply by principal", rule="arithmetic calculation",),
    ]
    canonical = solution_graph(
        goal=f"calculate reducing balance book value after {n_years} years",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 - i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution P={p_str}, i={rate_str}%, n={n_years}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate final book value R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_06",
        topic=TOPIC_NAME,
        subskill="06_reducing_balance_book_value_basic",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Reducing-balance depreciation uses the formula: A = P(1 - i)^n.",
            "concept": "The base (1 - i) is raised to the power of the number of years.",
            "breakdown": f"A = {p_val}(1 - {i_dec})^{n_years} = R {round(a_val, 2):.2f}.",
        },
        misconception_tags=["used_simple_decay_instead_of_reducing_balance"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 07: Reducing-Balance Depreciation — Solve Purchase Price P
def arch_07_reducing_balance_solve_initial_cost(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(20, 70) * 10000
    n_years = r.randint(3, 5)
    rate_pct = r.choice([12, 15, 18, 20])
    i_dec = rate_pct / 100.0

    a_val = p_val * ((1.0 - i_dec) ** n_years)
    a_str = num(round(a_val, 2), 2)
    rate_str = num(rate_pct)
    ans_str = num(p_val)

    prompt = (
        f"A company's {asset} has a book value of R {a_str} after {n_years} years. "
        f"The asset depreciates at {rate_str}% per annum on the reducing-balance method. "
        f"Calculate the original purchase price of the {asset}."
    )
    prompt_latex = (
        rf"\text{{Book value after }}{n_years}\text{{ years is R }}{a_str}\text{{ (reducing-balance at }} "
        rf"{rate_str}\% \text{{ p.a.). Calculate initial price }} P."
    )

    base = round(1.0 - i_dec, 4)
    factor = round(base ** n_years, 6)
    steps = [
        step(from_latex=r"A = P(1 - i)^n", to_latex_str=rf"{a_str} = P(1 - {num(i_dec)})^{{{n_years}}}", op="substitute known values into reducing balance equation", rule="formula substitution",),
        step(from_latex=rf"P = \frac{{{a_str}}}{{({num(base)})^{{{n_years}}}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="divide book value by decay factor to solve for P", rule="algebraic solution",),
    ]
    canonical = solution_graph(
        goal=f"solve for original purchase price P using reducing-balance formula",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 - i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct rearrangement P = {a_str} / (1 - i)^n", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate purchase price R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_07",
        topic=TOPIC_NAME,
        subskill="07_reducing_balance_solve_initial_cost",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Rearrange A = P(1 - i)^n to solve for P: P = A / (1 - i)^n.",
            "concept": "Calculate (1 - i)^n and divide the scrap/book value by this number.",
            "breakdown": f"P = {a_val} / (1 - {i_dec})^{n_years} = R {p_val}.",
        },
        misconception_tags=["multiplied_instead_of_divided_by_power_factor"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 08: Reducing-Balance Depreciation — Solve Annual Rate i
def arch_08_reducing_balance_solve_annual_rate(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(20, 60) * 10000
    n_years = r.randint(3, 6)
    rate_pct = r.choice([12, 14, 15, 16, 18, 20])
    i_dec = rate_pct / 100.0

    a_val = p_val * ((1.0 - i_dec) ** n_years)
    p_str = num(p_val)
    a_str = num(round(a_val, 2), 2)
    ans_str = num(rate_pct)

    prompt = (
        f"{name} bought a {asset} for R {p_str}. "
        f"After {n_years} years, its book value on the reducing-balance method is R {a_str}. "
        f"Calculate the annual rate of depreciation as a percentage. "
        f"Round off your answer to ONE decimal place if necessary."
    )
    prompt_latex = (
        rf"\text{{{name} bought {asset} for R }}{p_str}\text{{. After }}{n_years}\text{{ years, book value is R }}{a_str} "
        rf"\text{{ (reducing-balance). Calculate annual depreciation rate }} r\%."
    )

    ratio = round(a_val / p_val, 6)
    root = round(ratio ** (1.0 / n_years), 6)
    steps = [
        step(from_latex=r"A = P(1 - i)^n", to_latex_str=rf"{a_str} = {p_str}(1 - i)^{{{n_years}}}", op="substitute into reducing-balance depreciation formula", rule="formula substitution",),
        step(from_latex=rf"(1 - i)^{{{n_years}}} = \frac{{{a_str}}}{{{p_str}}}", to_latex_str=rf"(1 - i)^{{{n_years}}} = {num(ratio)}", op="divide both sides by P", rule="algebraic division",),
        step(from_latex=rf"1 - i = \sqrt[{n_years}]{{{num(ratio)}}} = ({num(ratio)})^\frac{{1}}{{{n_years}}}", to_latex_str=rf"1 - i = {num(root)}", op="take the n-th root of both sides", rule="n-th root extraction",),
        step(from_latex=rf"i = 1 - {num(root)} = {num(round(1.0 - root, 4))}", to_latex_str=rf"{ans_str}\%", op="solve for i and convert to percentage", rule="percentage conversion",),
    ]
    canonical = solution_graph(
        goal=f"solve for annual reducing-balance depreciation rate",
        steps=steps,
        final_latex=rf"{ans_str}\%",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 - i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct substitution into equation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct n-th root extraction: (A/P)^(1/{n_years})", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate depreciation rate {ans_str}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_08",
        topic=TOPIC_NAME,
        subskill="08_reducing_balance_solve_annual_rate",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\%",
        sample_answer=rf"{ans_str}%",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "To solve for i in A = P(1 - i)^n, divide by P and take the n-th root.",
            "concept": "1 - i = (A/P)^(1/n), so i = 1 - (A/P)^(1/n).",
            "breakdown": f"1 - i = ({a_val}/{p_val})^(1/{n_years}) = {root}. i = 1 - {root} = {i_dec} -> {rate_pct}%.",
        },
        misconception_tags=["inverted_root_order_in_depreciation_rate"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 09: Reducing-Balance Depreciation — Solve Years Using Logs
def arch_09_reducing_balance_solve_years_using_logs(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(25, 75) * 10000
    n_years = r.randint(4, 8)
    rate_pct = r.choice([12, 14, 15, 18, 20])
    i_dec = rate_pct / 100.0

    a_val = p_val * ((1.0 - i_dec) ** n_years)
    p_str = num(p_val)
    a_str = num(round(a_val, 2), 2)
    rate_str = num(rate_pct)
    ans_str = str(n_years)

    prompt = (
        f"A {asset} was purchased for R {p_str}. "
        f"If the rate of depreciation is {rate_str}% per annum on a reducing-balance basis, "
        f"how many years will it take for the book value of the {asset} to decrease to R {a_str}? "
        f"Use logarithms to show your calculation."
    )
    prompt_latex = (
        rf"\text{{Cost R }}{p_str}\text{{, reducing-balance rate }}{rate_str}\% \text{{ p.a. Find }} n "
        rf"\text{{ using logs until book value is R }}{a_str}."
    )

    base = round(1.0 - i_dec, 4)
    ratio = round(a_val / p_val, 6)
    steps = [
        step(from_latex=r"A = P(1 - i)^n", to_latex_str=rf"{a_str} = {p_str}(1 - {num(i_dec)})^n", op="substitute known values into reducing balance formula", rule="formula substitution",),
        step(from_latex=rf"({num(base)})^n = \frac{{{a_str}}}{{{p_str}}} = {num(ratio)}", to_latex_str=rf"n = \log_{{{num(base)}}}\left({num(ratio)}\right) = \frac{{\log({num(ratio)})}}{{\log({num(base)})}}", op="apply logarithms to solve for exponent n", rule="logarithmic change of base",),
        step(from_latex=rf"n = \frac{{\log({num(ratio)})}}{{\log({num(base)})}}", to_latex_str=rf"{ans_str}\text{{ years}}", op="evaluate logarithmic quotient", rule="logarithm evaluation",),
    ]
    canonical = solution_graph(
        goal=f"solve for number of years n using logarithms",
        steps=steps,
        final_latex=rf"{ans_str}\text{{ years}}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 - i)^n and substitution", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Isolates base power: ({num(base)})^n = {num(ratio)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Correct application of logarithms: n = log(ratio) / log(base)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate time period n = {ans_str} years", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_09",
        topic=TOPIC_NAME,
        subskill="09_reducing_balance_solve_years_using_logs",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\text{{ years}}",
        sample_answer=rf"{ans_str} years",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Because the unknown n is in the exponent, you must use logarithms.",
            "concept": "If b^n = c, then n = log(c) / log(b). Remember b = 1 - i.",
            "breakdown": f"({base})^n = {a_val}/{p_val} = {ratio}. n = log({ratio}) / log({base}) = {n_years} years.",
        },
        misconception_tags=["inverted_log_numerator_and_denominator"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 10: Comparison of Straight-Line vs Reducing-Balance Depreciation
def arch_10_compare_straight_line_vs_reducing_balance(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(20, 50) * 10000
    n_years = r.randint(3, 5)
    rate_pct = r.choice([12, 14, 15, 18])
    i_dec = rate_pct / 100.0

    sl_val = p_val * (1.0 - i_dec * n_years)
    rb_val = p_val * ((1.0 - i_dec) ** n_years)
    diff = abs(rb_val - sl_val)

    p_str = num(p_val)
    rate_str = num(rate_pct)
    sl_str = num(round(sl_val, 2), 2)
    rb_str = num(round(rb_val, 2), 2)
    diff_str = num(round(diff, 2), 2)

    prompt = (
        f"{name} buys a {asset} for R {p_str}. "
        f"Calculate the difference in book value after {n_years} years if the asset is depreciated at {rate_str}% p.a. "
        f"on a straight-line basis compared to {rate_str}% p.a. on a reducing-balance basis. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} buys {asset} for R }}{p_str}\text{{. Compare book value after }}{n_years} "
        rf"\text{{ years between straight-line and reducing-balance at }}{rate_str}\% \text{{ p.a.}}"
    )

    steps = [
        step(from_latex=r"A_{\text{SL}} = P(1 - in)", to_latex_str=rf"A_{{\text{{SL}}}} = {p_str}(1 - {num(i_dec)} \times {n_years}) = \text{{R }} {sl_str}", op="calculate straight-line book value", rule="straight-line depreciation formula",),
        step(from_latex=r"A_{\text{RB}} = P(1 - i)^n", to_latex_str=rf"A_{{\text{{RB}}}} = {p_str}(1 - {num(i_dec)})^{{{n_years}}} = \text{{R }} {rb_str}", op="calculate reducing-balance book value", rule="reducing-balance depreciation formula",),
        step(from_latex=rf"\text{{Difference}} = |A_{{\text{{RB}}}} - A_{{\text{{SL}}}}|", to_latex_str=rf"\text{{R }} {rb_str} - \text{{R }} {sl_str} = \text{{R }} {diff_str}", op="subtract straight-line from reducing-balance book value", rule="subtraction",),
    ]
    canonical = solution_graph(
        goal=f"calculate difference between straight-line and reducing-balance book values",
        steps=steps,
        final_latex=rf"\text{{R }} {diff_str}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Straight-line book value R {sl_str}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Reducing-balance book value R {rb_str}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Accurate difference R {diff_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_10",
        topic=TOPIC_NAME,
        subskill="10_compare_straight_line_vs_reducing_balance",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {diff_str}",
        sample_answer=rf"R {diff_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Calculate the book value separately under each depreciation method, then subtract.",
            "concept": "Straight line: A = P(1 - in). Reducing balance: A = P(1 - i)^n.",
            "breakdown": f"SL = R {sl_val:.2f}, RB = R {rb_val:.2f}, Difference = R {diff:.2f}.",
        },
        misconception_tags=["confused_sl_and_rb_formulas"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 11: Depreciation — Equivalent Rate Comparison
def arch_11_depreciation_crossover_or_difference(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.randint(15, 45) * 10000
    n_years = r.randint(4, 6)
    sl_rate_pct = r.choice([12, 15, 18])
    i_sl = sl_rate_pct / 100.0

    sl_val = p_val * (1.0 - i_sl * n_years)
    rb_rate_dec = 1.0 - (sl_val / p_val) ** (1.0 / n_years)
    rb_rate_pct = round(rb_rate_dec * 100.0, 2)

    p_str = num(p_val)
    sl_str = num(sl_rate_pct)
    ans_str = num(rb_rate_pct, 2)

    prompt = (
        f"A business purchases equipment for R {p_str}. "
        f"Under straight-line depreciation at {sl_str}% per annum, the asset reaches a certain scrap value after {n_years} years. "
        f"What reducing-balance rate of depreciation (to TWO decimal places) would produce the exact same scrap value "
        f"over the same {n_years}-year period?"
    )
    prompt_latex = (
        rf"\text{{Equipment cost R }}{p_str}\text{{. Straight-line rate = }}{sl_str}\% \text{{ p.a. over }}{n_years} "
        rf"\text{{ years. Find reducing-balance rate }} r\% \text{{ yielding same scrap value.}}"
    )

    steps = [
        step(from_latex=r"A = P(1 - in)", to_latex_str=rf"A = {p_str}(1 - {num(i_sl)} \times {n_years}) = \text{{R }} {num(round(sl_val, 2), 2)}", op="calculate target scrap value using straight-line formula", rule="straight-line depreciation",),
        step(from_latex=r"P(1 - i_{\text{RB}})^n = A", to_latex_str=rf"(1 - i_{{\text{{RB}}}})^{{{n_years}}} = \frac{{{num(round(sl_val, 2), 2)}}}{{{p_str}}}", op="equate to reducing-balance formula and divide by P", rule="equation equating",),
        step(from_latex=rf"i_{{\text{{RB}}}} = 1 - \left(\frac{{{num(round(sl_val, 2), 2)}}}{{{p_str}}}\right)^\frac{{1}}{{{n_years}}}", to_latex_str=rf"{ans_str}\%", op="extract n-th root, solve for rate and convert to percentage", rule="root extraction",),
    ]
    canonical = solution_graph(
        goal=f"find equivalent reducing-balance depreciation rate",
        steps=steps,
        final_latex=rf"{ans_str}\%",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct scrap value calculation A = R {num(round(sl_val, 2), 2)}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Equates to reducing balance formula P(1 - i)^n = A", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Correct root extraction: 1 - (A/P)^(1/n)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate reducing-balance rate {ans_str}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_11",
        topic=TOPIC_NAME,
        subskill="11_depreciation_crossover_or_difference",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\%",
        sample_answer=rf"{ans_str}%",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "First find the scrap value using A = P(1 - in), then set P(1 - i)^n equal to that scrap value.",
            "concept": "Notice that P cancels out: 1 - i_sl * n = (1 - i_rb)^n.",
            "breakdown": f"Scrap value = {sl_val}. 1 - i = ({sl_val}/{p_val})^(1/{n_years}). i = {rb_rate_pct}%.",
        },
        misconception_tags=["assumed_sl_and_rb_rates_must_be_equal"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 12: Compound Growth — Annual Accumulated Amount
def arch_12_compound_growth_annual_accumulated(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(10, 45) * 5000
    n_years = r.randint(3, 7)
    rate_pct = r.choice([7, 8, 8.5, 9, 10, 10.5, 11])
    i_dec = rate_pct / 100.0

    a_val = p_val * ((1.0 + i_dec) ** n_years)
    p_str = num(p_val)
    rate_str = num(rate_pct)
    ans_str = num(round(a_val, 2), 2)

    prompt = (
        f"{name} deposits R {p_str} into a fixed deposit account earning {rate_str}% compound interest per annum. "
        f"Calculate the total accumulated amount at the end of {n_years} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} invests R }}{p_str}\text{{ at }}{rate_str}\% \text{{ p.a. compound interest for }}{n_years} "
        rf"\text{{ years. Calculate accumulated amount }} A."
    )

    steps = [
        step(from_latex=r"A = P(1 + i)^n", to_latex_str=rf"A = {p_str}\left(1 + \frac{{{rate_str}}}{{100}}\right)^{{{n_years}}}", op="substitute known values into compound interest formula", rule="compound interest formula",),
        step(from_latex=rf"A = {p_str}({num(round(1.0 + i_dec, 4))})^{{{n_years}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate power and multiply by principal", rule="arithmetic power and multiplication",),
    ]
    canonical = solution_graph(
        goal=f"calculate accumulated compound interest amount",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 + i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution P={p_str}, i={rate_str}%, n={n_years}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_12",
        topic=TOPIC_NAME,
        subskill="12_compound_growth_annual_accumulated",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Use the standard compound interest formula: A = P(1 + i)^n.",
            "concept": "Convert the interest rate into a decimal before adding 1.",
            "breakdown": f"A = {p_val}(1 + {i_dec})^{n_years} = R {round(a_val, 2):.2f}.",
        },
        misconception_tags=["used_simple_interest_instead_of_compound"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 13: Compound Growth — Solve Principal P
def arch_13_compound_growth_solve_principal(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(15, 60) * 5000
    n_years = r.randint(3, 6)
    rate_pct = r.choice([8, 9, 10, 11, 12])
    i_dec = rate_pct / 100.0

    a_val = p_val * ((1.0 + i_dec) ** n_years)
    a_str = num(round(a_val, 2), 2)
    rate_str = num(rate_pct)
    ans_str = num(p_val)

    prompt = (
        f"{name} needs R {a_str} in {n_years} years' time to pay for tertiary tuition fees. "
        f"How much money must be invested today into a savings account earning {rate_str}% compound interest per annum?"
    )
    prompt_latex = (
        rf"\text{{Future goal }} A = \text{{R }}{a_str}\text{{ in }}{n_years}\text{{ years at }} "
        rf"{rate_str}\% \text{{ p.a. compound interest. Calculate present principal }} P."
    )

    base = round(1.0 + i_dec, 4)
    steps = [
        step(from_latex=r"A = P(1 + i)^n", to_latex_str=rf"{a_str} = P(1 + {num(i_dec)})^{{{n_years}}}", op="substitute known values into compound interest formula", rule="formula substitution",),
        step(from_latex=rf"P = \frac{{{a_str}}}{{({num(base)})^{{{n_years}}}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="divide future value by growth factor to find present value P", rule="algebraic solution",),
    ]
    canonical = solution_graph(
        goal=f"solve for principal P required to accumulate target sum",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 + i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution A={a_str}, i={rate_str}%, n={n_years}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate principal P = R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_13",
        topic=TOPIC_NAME,
        subskill="13_compound_growth_solve_principal",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Rearrange the compound formula to solve for P: P = A(1 + i)^(-n) or P = A / (1 + i)^n.",
            "concept": "Divide the target amount by (1 + i)^n.",
            "breakdown": f"P = {a_val} / (1 + {i_dec})^{n_years} = R {p_val}.",
        },
        misconception_tags=["multiplied_future_value_by_growth_factor"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 14: Compound Growth — Solve Interest Rate i
def arch_14_compound_growth_solve_interest_rate(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(10, 40) * 5000
    n_years = r.randint(3, 6)
    rate_pct = r.choice([7.5, 8, 9, 9.5, 10, 11, 12])
    i_dec = rate_pct / 100.0

    a_val = p_val * ((1.0 + i_dec) ** n_years)
    p_str = num(p_val)
    a_str = num(round(a_val, 2), 2)
    ans_str = num(rate_pct)

    prompt = (
        f"{name} invested R {p_str} and it grew to R {a_str} in {n_years} years. "
        f"Calculate the annual compound interest rate achieved on this investment as a percentage. "
        f"Round off your answer to ONE decimal place if necessary."
    )
    prompt_latex = (
        rf"\text{{{name} invested R }}{p_str}\text{{ which grew to R }}{a_str}\text{{ in }}{n_years} "
        rf"\text{{ years. Find annual compound interest rate }} r\%."
    )

    ratio = round(a_val / p_val, 6)
    root = round(ratio ** (1.0 / n_years), 6)
    steps = [
        step(from_latex=r"A = P(1 + i)^n", to_latex_str=rf"{a_str} = {p_str}(1 + i)^{{{n_years}}}", op="substitute known values into compound interest formula", rule="formula substitution",),
        step(from_latex=rf"(1 + i)^{{{n_years}}} = \frac{{{a_str}}}{{{p_str}}} = {num(ratio)}", to_latex_str=rf"1 + i = \sqrt[{n_years}]{{{num(ratio)}}} = {num(root)}", op="isolate (1 + i) by taking the n-th root of the ratio A/P", rule="n-th root extraction",),
        step(from_latex=rf"i = {num(root)} - 1 = {num(round(root - 1.0, 4))}", to_latex_str=rf"{ans_str}\%", op="subtract 1 and convert to percentage", rule="percentage conversion",),
    ]
    canonical = solution_graph(
        goal=f"solve for annual compound interest rate",
        steps=steps,
        final_latex=rf"{ans_str}\%",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 + i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct substitution into equation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct n-th root extraction: (A/P)^(1/{n_years})", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate interest rate {ans_str}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_14",
        topic=TOPIC_NAME,
        subskill="14_compound_growth_solve_interest_rate",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\%",
        sample_answer=rf"{ans_str}%",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Divide A by P, then take the n-th root, and finally subtract 1.",
            "concept": "1 + i = (A/P)^(1/n) -> i = (A/P)^(1/n) - 1.",
            "breakdown": f"1 + i = ({a_val}/{p_val})^(1/{n_years}) = {root}. i = {i_dec} -> {rate_pct}%.",
        },
        misconception_tags=["forgot_to_subtract_one_from_root"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 15: Compound Growth — Solve Term n Using Logarithms
def arch_15_compound_growth_solve_years_using_logs(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(10, 30) * 5000
    n_years = r.randint(4, 9)
    rate_pct = r.choice([8, 9, 10, 11, 12])
    i_dec = rate_pct / 100.0

    a_val = p_val * ((1.0 + i_dec) ** n_years)
    p_str = num(p_val)
    a_str = num(round(a_val, 2), 2)
    rate_str = num(rate_pct)
    ans_str = str(n_years)

    prompt = (
        f"{name} invested R {p_str} in a bank at {rate_str}% interest per annum, compounded annually. "
        f"How long (in years) will it take for the investment to grow to R {a_str}? "
        f"Use logarithms to show your working."
    )
    prompt_latex = (
        rf"\text{{{name} invested R }}{p_str}\text{{ at }}{rate_str}\% \text{{ p.a. compounded annually. Find }} n "
        rf"\text{{ using logs until }} A = \text{{R }}{a_str}."
    )

    base = round(1.0 + i_dec, 4)
    ratio = round(a_val / p_val, 6)
    steps = [
        step(from_latex=r"A = P(1 + i)^n", to_latex_str=rf"{a_str} = {p_str}(1 + {num(i_dec)})^n", op="substitute known values into compound interest formula", rule="formula substitution",),
        step(from_latex=rf"({num(base)})^n = \frac{{{a_str}}}{{{p_str}}} = {num(ratio)}", to_latex_str=rf"n = \frac{{\log({num(ratio)})}}{{\log({num(base)})}}", op="apply logarithms to solve for exponent n", rule="logarithmic change of base rule",),
        step(from_latex=rf"n = \frac{{\log({num(ratio)})}}{{\log({num(base)})}}", to_latex_str=rf"{ans_str}\text{{ years}}", op="evaluate logarithmic quotient", rule="logarithm quotient evaluation",),
    ]
    canonical = solution_graph(
        goal=f"solve for investment period n using logarithms",
        steps=steps,
        final_latex=rf"{ans_str}\text{{ years}}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 + i)^n and substitution", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Isolates base power: ({num(base)})^n = {num(ratio)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Applies logarithms n = log(A/P) / log(1 + i)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate time period n = {ans_str} years", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_15",
        topic=TOPIC_NAME,
        subskill="15_compound_growth_solve_years_using_logs",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\text{{ years}}",
        sample_answer=rf"{ans_str} years",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Because the unknown is in the exponent, use logarithms: n = log(A/P) / log(1 + i).",
            "concept": "Isolate the bracket (1 + i)^n by dividing by P first, then take logs of both sides.",
            "breakdown": f"({base})^n = {ratio}. n = log({ratio}) / log({base}) = {n_years} years.",
        },
        misconception_tags=["divided_by_rate_instead_of_using_logs"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 16: Compound Growth — Doubling Time Calculation
def arch_16_compound_growth_doubling_time_calc(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    rate_pct = r.choice([8, 8.5, 9, 10, 11, 12, 12.5, 14])
    i_dec = rate_pct / 100.0

    n_exact = math.log(2.0) / math.log(1.0 + i_dec)
    ans_round = round(n_exact, 1)
    rate_str = num(rate_pct)
    ans_str = num(ans_round, 1)

    prompt = (
        f"{name} deposits money into a fixed investment account paying {rate_str}% interest per annum compounded annually. "
        f"How many years will it take for {name}'s investment to double in value? "
        f"Round off your answer to ONE decimal place."
    )
    prompt_latex = (
        rf"\text{{{name} invests money at }}{rate_str}\% \text{{ p.a. compounded annually. Find }} n "
        rf"\text{{ for investment to double (to 1 dec place).}}"
    )

    base = round(1.0 + i_dec, 4)
    steps = [
        step(from_latex=r"A = P(1 + i)^n", to_latex_str=rf"2P = P(1 + {num(i_dec)})^n", op="substitute A = 2P into compound growth formula", rule="doubling condition",),
        step(from_latex=rf"2 = ({num(base)})^n", to_latex_str=rf"n = \frac{{\log(2)}}{{\log({num(base)})}}", op="divide by P and take logarithms of both sides", rule="logarithmic change of base",),
        step(from_latex=rf"n = \frac{{\log(2)}}{{\log({num(base)})}}", to_latex_str=rf"{ans_str}\text{{ years}}", op="evaluate quotient and round to one decimal place", rule="arithmetic evaluation and rounding",),
    ]
    canonical = solution_graph(
        goal=f"calculate doubling time using logarithms",
        steps=steps,
        final_latex=rf"{ans_str}\text{{ years}}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Sets 2P = P(1 + i)^n and simplifies to 2 = (1 + i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Applies logarithms n = log(2) / log(1 + i)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate doubling time {ans_str} years", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_16",
        topic=TOPIC_NAME,
        subskill="16_compound_growth_doubling_time_calc",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\text{{ years}}",
        sample_answer=rf"{ans_str} years",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "For doubling, set A = 2P so that the principal P cancels out: 2 = (1 + i)^n.",
            "concept": "Apply logarithms: n = log(2) / log(1 + i).",
            "breakdown": f"n = log(2) / log(1 + {i_dec}) = {math.log(2):.4f} / {math.log(1+i_dec):.4f} = {ans_round} years.",
        },
        misconception_tags=["assumed_principal_is_required_to_find_doubling_time"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 17: Compounding Frequency — Half-Yearly (Semi-Annually)
def arch_17_compounding_frequency_half_yearly(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(12, 40) * 5000
    n_years = r.randint(3, 6)
    rate_pct = r.choice([8, 10, 11, 12, 14])
    i_annual = rate_pct / 100.0
    m = 2
    i_period = i_annual / m
    total_periods = n_years * m

    a_val = p_val * ((1.0 + i_period) ** total_periods)
    p_str = num(p_val)
    rate_str = num(rate_pct)
    ans_str = num(round(a_val, 2), 2)

    prompt = (
        f"{name} deposits R {p_str} into a savings account for {n_years} years. "
        f"Interest is calculated at {rate_str}% per annum, compounded half-yearly. "
        f"Calculate the accumulated balance at the end of the investment period. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} invests R }}{p_str}\text{{ for }}{n_years}\text{{ years at }}{rate_str}\% "
        rf"\text{{ p.a. compounded half-yearly. Calculate }} A."
    )

    steps = [
        step(from_latex=r"A = P\left(1 + \frac{i}{m}\right)^{m \times n}", to_latex_str=rf"A = {p_str}\left(1 + \frac{{{num(i_annual)}}}{{2}}\right)^{{2 \times {n_years}}}", op="substitute half-yearly compounding parameters into formula", rule="compounding frequency adjustment",),
        step(from_latex=rf"A = {p_str}\left(1 + {num(i_period)}\right)^{{{total_periods}}} = {p_str}({num(round(1.0 + i_period, 4))})^{{{total_periods}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate power for 2n periods and multiply by P", rule="power and multiplication",),
    ]
    canonical = solution_graph(
        goal=f"calculate accumulated amount with half-yearly compounding",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote and division of rate by 2: i/2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Multiplication of years by 2: total periods = {total_periods}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_17",
        topic=TOPIC_NAME,
        subskill="17_compounding_frequency_half_yearly",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Half-yearly means twice a year (m = 2). Divide rate by 2 and multiply years by 2.",
            "concept": "A = P(1 + i/2)^(2n).",
            "breakdown": f"i_period = {rate_pct}% / 2 = {i_period*100}%. n_periods = {n_years} x 2 = {total_periods}. A = R {round(a_val, 2):.2f}.",
        },
        misconception_tags=["forgot_to_multiply_years_by_compounding_frequency"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 18: Compounding Frequency — Quarterly
def arch_18_compounding_frequency_quarterly(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(15, 50) * 5000
    n_years = r.randint(3, 6)
    rate_pct = r.choice([8, 9, 10, 11, 12])
    i_annual = rate_pct / 100.0
    m = 4
    i_period = i_annual / m
    total_periods = n_years * m

    a_val = p_val * ((1.0 + i_period) ** total_periods)
    p_str = num(p_val)
    rate_str = num(rate_pct)
    ans_str = num(round(a_val, 2), 2)

    prompt = (
        f"{name} invests R {p_str} for {n_years} years at an interest rate of {rate_str}% p.a., compounded quarterly. "
        f"Calculate the accumulated value of the investment at the end of the term. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} invests R }}{p_str}\text{{ for }}{n_years}\text{{ years at }}{rate_str}\% "
        rf"\text{{ p.a. compounded quarterly. Find }} A."
    )

    steps = [
        step(from_latex=r"A = P\left(1 + \frac{i}{4}\right)^{4n}", to_latex_str=rf"A = {p_str}\left(1 + \frac{{{num(i_annual)}}}{{4}}\right)^{{4 \times {n_years}}}", op="substitute quarterly parameters into formula", rule="quarterly compounding formula",),
        step(from_latex=rf"A = {p_str}\left(1 + {num(i_period)}\right)^{{{total_periods}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate power for 4n quarters and multiply by P", rule="arithmetic calculation",),
    ]
    canonical = solution_graph(
        goal=f"calculate accumulated amount with quarterly compounding",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Divide annual rate by 4: i/4", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Multiply years by 4: total periods = {total_periods}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_18",
        topic=TOPIC_NAME,
        subskill="18_compounding_frequency_quarterly",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Quarterly means four times per year (m = 4). Divide rate by 4 and multiply years by 4.",
            "concept": "A = P(1 + i/4)^(4n).",
            "breakdown": f"Periodic rate = {rate_pct}/4 = {i_period*100}%. Quarters = {n_years} x 4 = {total_periods}. A = R {round(a_val, 2):.2f}.",
        },
        misconception_tags=["divided_years_by_4_instead_of_multiplying"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 19: Compounding Frequency — Monthly
def arch_19_compounding_frequency_monthly(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(10, 35) * 5000
    n_years = r.randint(2, 5)
    rate_pct = r.choice([9, 9.6, 10.2, 10.8, 12, 13.2])
    i_annual = rate_pct / 100.0
    m = 12
    i_period = i_annual / m
    total_periods = n_years * m

    a_val = p_val * ((1.0 + i_period) ** total_periods)
    p_str = num(p_val)
    rate_str = num(rate_pct)
    ans_str = num(round(a_val, 2), 2)

    prompt = (
        f"{name} deposits R {p_str} into a high-yield savings account for {n_years} years. "
        f"The bank offers {rate_str}% p.a. compounded monthly. "
        f"Calculate the value of the investment at the end of {n_years} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} deposits R }}{p_str}\text{{ for }}{n_years}\text{{ years at }}{rate_str}\% "
        rf"\text{{ p.a. compounded monthly. Find final amount }} A."
    )

    steps = [
        step(from_latex=r"A = P\left(1 + \frac{i}{12}\right)^{12n}", to_latex_str=rf"A = {p_str}\left(1 + \frac{{{num(i_annual)}}}{{12}}\right)^{{12 \times {n_years}}}", op="substitute monthly compounding parameters into formula", rule="monthly compounding formula",),
        step(from_latex=rf"A = {p_str}(1 + {num(i_period)})^{{{total_periods}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate power for 12n months and multiply by P", rule="power and multiplication",),
    ]
    canonical = solution_graph(
        goal=f"calculate accumulated balance with monthly compounding",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Divide annual rate by 12: i/12", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Multiply years by 12: total periods = {total_periods}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_19",
        topic=TOPIC_NAME,
        subskill="19_compounding_frequency_monthly",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Monthly compounding means m = 12. Divide rate by 12 and multiply years by 12.",
            "concept": "A = P(1 + i/12)^(12n).",
            "breakdown": f"Monthly rate = {rate_pct}/12 = {i_period*100}%. Months = {n_years} x 12 = {total_periods}. A = R {round(a_val, 2):.2f}.",
        },
        misconception_tags=["forgot_to_divide_rate_by_12"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 20: Compounding Frequency — Solve Principal with Monthly Compounding
def arch_20_compounding_frequency_solve_principal(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(15, 50) * 5000
    n_years = r.randint(3, 5)
    rate_pct = r.choice([9.6, 10.8, 12, 13.2])
    i_annual = rate_pct / 100.0
    m = 12
    i_period = i_annual / m
    total_periods = n_years * m

    a_val = p_val * ((1.0 + i_period) ** total_periods)
    a_str = num(round(a_val, 2), 2)
    rate_str = num(rate_pct)
    ans_str = num(p_val)

    prompt = (
        f"{name} needs R {a_str} in {n_years} years' time. "
        f"A bank offers an investment account with {rate_str}% p.a. interest, compounded monthly. "
        f"Calculate the lump sum {name} must deposit into the account today."
    )
    prompt_latex = (
        rf"\text{{Target }} A = \text{{R }}{a_str}\text{{ in }}{n_years}\text{{ years at }}{rate_str}\% "
        rf"\text{{ p.a. compounded monthly. Find principal }} P."
    )

    steps = [
        step(from_latex=r"A = P\left(1 + \frac{i}{12}\right)^{12n}", to_latex_str=rf"{a_str} = P\left(1 + \frac{{{num(i_annual)}}}{{12}}\right)^{{12 \times {n_years}}}", op="substitute values with monthly compounding", rule="formula substitution",),
        step(from_latex=rf"P = \frac{{{a_str}}}{{\left(1 + {num(i_period)}\right)^{{{total_periods}}}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="divide target amount by monthly compounding factor", rule="algebraic solution",),
    ]
    canonical = solution_graph(
        goal=f"solve for principal P required with monthly compounding",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote with i/12 and 12n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution A={a_str}, periods={total_periods}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate principal P = R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_20",
        topic=TOPIC_NAME,
        subskill="20_compounding_frequency_solve_principal",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "P = A / (1 + i/12)^(12n). Divide target amount by the monthly compounding factor.",
            "concept": "Total months = n x 12. Monthly rate = annual rate / 12.",
            "breakdown": f"P = {a_val} / (1 + {i_period})^{total_periods} = R {p_val}.",
        },
        misconception_tags=["multiplied_instead_of_divided_by_compound_factor"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 21: Compounding Frequency — Solve Time Using Logs
def arch_21_compounding_frequency_solve_time_using_logs(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(10, 30) * 5000
    n_years = r.randint(3, 6)
    rate_pct = r.choice([9, 10.2, 10.8, 12])
    i_annual = rate_pct / 100.0
    m = 12
    i_period = i_annual / m
    total_months = n_years * m

    a_val = p_val * ((1.0 + i_period) ** total_months)
    p_str = num(p_val)
    a_str = num(round(a_val, 2), 2)
    rate_str = num(rate_pct)
    ans_str = str(n_years)

    prompt = (
        f"{name} invested R {p_str} in an account earning {rate_str}% p.a. compounded monthly. "
        f"If the accumulated amount grew to R {a_str}, calculate how many years the money was invested. "
        f"Use logarithms to show your working."
    )
    prompt_latex = (
        rf"\text{{{name} invested R }}{p_str}\text{{ at }}{rate_str}\% \text{{ p.a. compounded monthly, growing to R }}{a_str}. "
        rf"\text{{ Find time in years }} n \text{{ using logs.}}"
    )

    base = round(1.0 + i_period, 6)
    ratio = round(a_val / p_val, 6)
    steps = [
        step(from_latex=r"A = P\left(1 + \frac{i}{12}\right)^{12n}", to_latex_str=rf"{a_str} = {p_str}\left(1 + {num(i_period)}\right)^{{12n}}", op="substitute known values into monthly compounding formula", rule="formula substitution",),
        step(from_latex=rf"({num(base)})^{{12n}} = \frac{{{a_str}}}{{{p_str}}} = {num(ratio)}", to_latex_str=rf"12n = \frac{{\log({num(ratio)})}}{{\log({num(base)})}}", op="apply logarithms to solve for total months 12n", rule="logarithmic change of base",),
        step(from_latex=rf"12n = {total_months}\text{{ months}}", to_latex_str=rf"n = \frac{{{total_months}}}{{12}} = {ans_str}\text{{ years}}", op="divide total months by 12 to find years n", rule="months to years conversion",),
    ]
    canonical = solution_graph(
        goal=f"solve for investment term n using logarithms with monthly compounding",
        steps=steps,
        final_latex=rf"{ans_str}\text{{ years}}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote with i/12 and 12n substitution", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Isolates base power: ({num(base)})^(12n) = {num(ratio)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculates total months 12n = {total_months}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Converts to years n = {ans_str} years", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_21",
        topic=TOPIC_NAME,
        subskill="21_compounding_frequency_solve_time_using_logs",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\text{{ years}}",
        sample_answer=rf"{ans_str} years",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "First solve for the total number of compounding periods (months = 12n) using logs.",
            "concept": "12n = log(A/P) / log(1 + i/12). Then divide by 12 to get years.",
            "breakdown": f"12n = log({ratio}) / log({base}) = {total_months} months -> n = {total_months}/12 = {n_years} years.",
        },
        misconception_tags=["forgot_to_divide_months_by_12_for_years"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 22: Nominal to Effective Rate — Half-Yearly Compounding
def arch_22_effective_rate_from_nominal_half_yearly(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    nom_pct = r.choice([8.5, 9, 10, 10.5, 11, 11.5, 12])
    i_nom = nom_pct / 100.0
    m = 2

    i_eff = ((1.0 + i_nom / m) ** m) - 1.0
    eff_pct = round(i_eff * 100.0, 2)
    nom_str = num(nom_pct)
    ans_str = num(eff_pct, 2)

    prompt = (
        f"A bank quotes an interest rate of {nom_str}% per annum, compounded half-yearly. "
        f"Calculate the equivalent effective annual interest rate as a percentage. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{Convert nominal rate }}{nom_str}\% \text{{ p.a. compounded half-yearly to effective annual rate }} i_{{\text{{eff}}}}."
    )

    half_rate = round(i_nom / 2.0, 6)
    steps = [
        step(from_latex=r"1 + i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{m}\right)^m", to_latex_str=rf"1 + i_{{\text{{eff}}}} = \left(1 + \frac{{{num(i_nom)}}}{{2}}\right)^2", op="substitute nominal rate and m = 2 into nominal-effective formula", rule="nominal to effective interest rate conversion",),
        step(from_latex=rf"1 + i_{{\text{{eff}}}} = (1 + {num(half_rate)})^2 = ({num(round(1.0 + half_rate, 4))})^2", to_latex_str=rf"1 + i_{{\text{{eff}}}} = {num(round((1.0 + half_rate)**2, 6))}", op="evaluate the square of the half-yearly growth factor", rule="squaring growth factor",),
        step(from_latex=rf"i_{{\text{{eff}}}} = {num(round((1.0 + half_rate)**2, 6))} - 1 = {num(round(i_eff, 4))}", to_latex_str=rf"{ans_str}\%", op="subtract 1 and convert to percentage", rule="percentage conversion",),
    ]
    canonical = solution_graph(
        goal=f"convert nominal rate to effective annual rate (half-yearly)",
        steps=steps,
        final_latex=rf"{ans_str}\%",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote 1 + i_eff = (1 + i_nom / m)^m", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Substitution of i_nom = {nom_str}% and m = 2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate effective rate {ans_str}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_22",
        topic=TOPIC_NAME,
        subskill="22_effective_rate_from_nominal_half_yearly",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\%",
        sample_answer=rf"{ans_str}%",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Use the formula: 1 + i_eff = (1 + i_nom / 2)^2.",
            "concept": "Calculate (1 + i_nom / 2)^2, then subtract 1, and multiply by 100 to get a percentage.",
            "breakdown": f"(1 + {nom_pct}/200)^2 - 1 = {eff_pct}%.",
        },
        misconception_tags=["forgot_to_subtract_one_for_effective_rate"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 23: Nominal to Effective Rate — Quarterly Compounding
def arch_23_effective_rate_from_nominal_quarterly(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    nom_pct = r.choice([9, 9.5, 10, 10.5, 11, 11.5, 12])
    i_nom = nom_pct / 100.0
    m = 4

    i_eff = ((1.0 + i_nom / m) ** m) - 1.0
    eff_pct = round(i_eff * 100.0, 2)
    nom_str = num(nom_pct)
    ans_str = num(eff_pct, 2)

    prompt = (
        f"An investment offers an interest rate of {nom_str}% p.a. compounded quarterly. "
        f"Determine the effective annual interest rate correct to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{Find effective annual rate }} i_{{\text{{eff}}}} \text{{ for nominal rate }} {nom_str}\% "
        rf"\text{{ p.a. compounded quarterly.}}"
    )

    q_rate = round(i_nom / 4.0, 6)
    steps = [
        step(from_latex=r"1 + i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{4}\right)^4", to_latex_str=rf"1 + i_{{\text{{eff}}}} = \left(1 + \frac{{{num(i_nom)}}}{{4}}\right)^4 = (1 + {num(q_rate)})^4", op="substitute nominal rate and m = 4 into formula", rule="effective rate formula for quarterly compounding",),
        step(from_latex=rf"1 + i_{{\text{{eff}}}} = ({num(round(1.0 + q_rate, 4))})^4", to_latex_str=rf"1 + i_{{\text{{eff}}}} = {num(round((1.0 + q_rate)**4, 6))}", op="evaluate growth factor to 4th power", rule="fourth power evaluation",),
        step(from_latex=rf"i_{{\text{{eff}}}} = {num(round((1.0 + q_rate)**4, 6))} - 1", to_latex_str=rf"{ans_str}\%", op="subtract 1 and convert to percentage", rule="percentage conversion",),
    ]
    canonical = solution_graph(
        goal=f"convert nominal rate to effective annual rate (quarterly)",
        steps=steps,
        final_latex=rf"{ans_str}\%",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote 1 + i_eff = (1 + i_nom / 4)^4", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Substitution of i_nom = {nom_str}% and m = 4", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate effective rate {ans_str}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_23",
        topic=TOPIC_NAME,
        subskill="23_effective_rate_from_nominal_quarterly",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\%",
        sample_answer=rf"{ans_str}%",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Quarterly means m = 4: 1 + i_eff = (1 + i_nom / 4)^4.",
            "concept": "Divide nominal rate by 4, add 1, raise to power 4, and subtract 1.",
            "breakdown": f"(1 + {nom_pct}/400)^4 - 1 = {eff_pct}%.",
        },
        misconception_tags=["used_power_of_12_instead_of_4"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 24: Nominal to Effective Rate — Monthly Compounding
def arch_24_effective_rate_from_nominal_monthly(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    nom_pct = r.choice([9.6, 10.2, 10.8, 11.4, 12, 12.6, 13.2])
    i_nom = nom_pct / 100.0
    m = 12

    i_eff = ((1.0 + i_nom / m) ** m) - 1.0
    eff_pct = round(i_eff * 100.0, 2)
    nom_str = num(nom_pct)
    ans_str = num(eff_pct, 2)

    prompt = (
        f"A commercial credit card charges an interest rate of {nom_str}% p.a. compounded monthly. "
        f"Calculate the effective annual interest rate. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{Calculate effective annual rate }} i_{{\text{{eff}}}} \text{{ for nominal rate }} {nom_str}\% "
        rf"\text{{ p.a. compounded monthly.}}"
    )

    m_rate = round(i_nom / 12.0, 6)
    steps = [
        step(from_latex=r"1 + i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{12}\right)^{12}", to_latex_str=rf"1 + i_{{\text{{eff}}}} = \left(1 + \frac{{{num(i_nom)}}}{{12}}\right)^{{12}} = (1 + {num(m_rate)})^{{12}}", op="substitute nominal rate and m = 12 into formula", rule="effective rate formula for monthly compounding",),
        step(from_latex=rf"1 + i_{{\text{{eff}}}} = ({num(round(1.0 + m_rate, 4))})^{{12}}", to_latex_str=rf"1 + i_{{\text{{eff}}}} = {num(round((1.0 + m_rate)**12, 6))}", op="evaluate growth factor to power 12", rule="power evaluation",),
        step(from_latex=rf"i_{{\text{{eff}}}} = {num(round((1.0 + m_rate)**12, 6))} - 1", to_latex_str=rf"{ans_str}\%", op="subtract 1 and convert to percentage", rule="percentage conversion",),
    ]
    canonical = solution_graph(
        goal=f"convert nominal rate to effective annual rate (monthly)",
        steps=steps,
        final_latex=rf"{ans_str}\%",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote 1 + i_eff = (1 + i_nom / 12)^12", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Substitution of i_nom = {nom_str}% and m = 12", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate effective rate {ans_str}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_24",
        topic=TOPIC_NAME,
        subskill="24_effective_rate_from_nominal_monthly",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\%",
        sample_answer=rf"{ans_str}%",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Monthly compounding means m = 12: 1 + i_eff = (1 + i_nom / 12)^12.",
            "concept": "Divide nominal rate by 12, add 1, raise to power 12, and subtract 1.",
            "breakdown": f"(1 + {nom_pct}/1200)^12 - 1 = {eff_pct}%.",
        },
        misconception_tags=["divided_by_100_instead_of_1200"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 25: Nominal to Effective Rate — Daily Compounding
def arch_25_effective_rate_from_nominal_daily(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    nom_pct = r.choice([9, 9.5, 10, 10.5, 11, 11.5, 12])
    i_nom = nom_pct / 100.0
    m = 365

    i_eff = ((1.0 + i_nom / m) ** m) - 1.0
    eff_pct = round(i_eff * 100.0, 2)
    nom_str = num(nom_pct)
    ans_str = num(eff_pct, 2)

    prompt = (
        f"A money market account pays {nom_str}% per annum, compounded daily (assume 365 days in a year). "
        f"Calculate the effective annual interest rate correct to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{Calculate effective annual rate }} i_{{\text{{eff}}}} \text{{ for nominal rate }} {nom_str}\% "
        rf"\text{{ p.a. compounded daily (365 days).}}"
    )

    steps = [
        step(from_latex=r"1 + i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{365}\right)^{365}", to_latex_str=rf"1 + i_{{\text{{eff}}}} = \left(1 + \frac{{{num(i_nom)}}}{{365}}\right)^{{365}}", op="substitute nominal rate and m = 365 into formula", rule="daily compounding formula",),
        step(from_latex=rf"1 + i_{{\text{{eff}}}} = \left(1 + {num(round(i_nom / 365.0, 6))}\right)^{{365}}", to_latex_str=rf"1 + i_{{\text{{eff}}}} = {num(round((1.0 + i_nom / 365.0)**365, 6))}", op="evaluate growth factor to power 365", rule="daily power evaluation",),
        step(from_latex=rf"i_{{\text{{eff}}}} = {num(round((1.0 + i_nom / 365.0)**365, 6))} - 1", to_latex_str=rf"{ans_str}\%", op="subtract 1 and convert to percentage", rule="percentage conversion",),
    ]
    canonical = solution_graph(
        goal=f"convert nominal rate to effective annual rate (daily compounding)",
        steps=steps,
        final_latex=rf"{ans_str}\%",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote 1 + i_eff = (1 + i_nom / 365)^365", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Substitution of i_nom = {nom_str}% and m = 365", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate effective rate {ans_str}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_25",
        topic=TOPIC_NAME,
        subskill="25_effective_rate_from_nominal_daily",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\%",
        sample_answer=rf"{ans_str}%",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Daily compounding uses m = 365: 1 + i_eff = (1 + i_nom / 365)^365.",
            "concept": "Divide nominal rate by 365, add 1, raise to power 365, and subtract 1.",
            "breakdown": f"(1 + {nom_pct}/36500)^365 - 1 = {eff_pct}%.",
        },
        misconception_tags=["assumed_360_days_instead_of_365"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


ARCHETYPE_BUILDERS_01_25: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "01_straight_line_depreciation_book_value": arch_01_straight_line_depreciation_book_value,
    "02_straight_line_depreciation_initial_cost": arch_02_straight_line_depreciation_initial_cost,
    "03_straight_line_depreciation_rate": arch_03_straight_line_depreciation_rate,
    "04_straight_line_depreciation_years_to_scrap": arch_04_straight_line_depreciation_years_to_scrap,
    "05_straight_line_zero_or_scrap_threshold": arch_05_straight_line_zero_or_scrap_threshold,
    "06_reducing_balance_book_value_basic": arch_06_reducing_balance_book_value_basic,
    "07_reducing_balance_solve_initial_cost": arch_07_reducing_balance_solve_initial_cost,
    "08_reducing_balance_solve_annual_rate": arch_08_reducing_balance_solve_annual_rate,
    "09_reducing_balance_solve_years_using_logs": arch_09_reducing_balance_solve_years_using_logs,
    "10_compare_straight_line_vs_reducing_balance": arch_10_compare_straight_line_vs_reducing_balance,
    "11_depreciation_crossover_or_difference": arch_11_depreciation_crossover_or_difference,
    "12_compound_growth_annual_accumulated": arch_12_compound_growth_annual_accumulated,
    "13_compound_growth_solve_principal": arch_13_compound_growth_solve_principal,
    "14_compound_growth_solve_interest_rate": arch_14_compound_growth_solve_interest_rate,
    "15_compound_growth_solve_years_using_logs": arch_15_compound_growth_solve_years_using_logs,
    "16_compound_growth_doubling_time_calc": arch_16_compound_growth_doubling_time_calc,
    "17_compounding_frequency_half_yearly": arch_17_compounding_frequency_half_yearly,
    "18_compounding_frequency_quarterly": arch_18_compounding_frequency_quarterly,
    "19_compounding_frequency_monthly": arch_19_compounding_frequency_monthly,
    "20_compounding_frequency_solve_principal": arch_20_compounding_frequency_solve_principal,
    "21_compounding_frequency_solve_time_using_logs": arch_21_compounding_frequency_solve_time_using_logs,
    "22_effective_rate_from_nominal_half_yearly": arch_22_effective_rate_from_nominal_half_yearly,
    "23_effective_rate_from_nominal_quarterly": arch_23_effective_rate_from_nominal_quarterly,
    "24_effective_rate_from_nominal_monthly": arch_24_effective_rate_from_nominal_monthly,
    "25_effective_rate_from_nominal_daily": arch_25_effective_rate_from_nominal_daily,
}
