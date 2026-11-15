"""Grade 11 Mathematics — Finance, Growth and Decay: Archetypes 26 to 50.

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
from .finance_growth_decay_archetypes_01_25 import (
    ASSETS,
    LEARNING_OBJECTIVE_ID,
    SA_NAMES,
    TOPIC_ID,
    TOPIC_NAME,
    fmt_pct,
    fmt_r,
)


def timeline_svg(
    total_years: int,
    intervals: List[Tuple[int, int, str]],
    cash_flows: List[Tuple[int, str, str]],  # (year, label, type: "deposit" | "withdrawal" | "initial")
    title: str = "Investment Cash Flow Timeline",
) -> str:
    """Generate clean vector horizontal timeline diagram for Grade 11 Finance."""
    w, h = 620, 160
    x_start, x_end = 60, 560
    y_line = 85
    span = max(1, total_years)

    def to_x(yr: int) -> float:
        return x_start + (yr / span) * (x_end - x_start)

    parts: List[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">',
        f'<rect x="4" y="4" width="{w-8}" height="{h-8}" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        f'<text x="{w//2}" y="24" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">{title}</text>',
        f'<line x1="{x_start}" y1="{y_line}" x2="{x_end}" y2="{y_line}" stroke="#334155" stroke-width="2.5"/>',
    ]

    # Year ticks
    for y in range(total_years + 1):
        x = to_x(y)
        parts.append(f'<line x1="{x}" y1="{y_line - 6}" x2="{x}" y2="{y_line + 6}" stroke="#334155" stroke-width="2"/>')
        parts.append(f'<text x="{x}" y="{y_line + 18}" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">T{y}</text>')

    # Interval rate labels above line
    for y1, y2, rate_label in intervals:
        mx = (to_x(y1) + to_x(y2)) / 2.0
        parts.append(f'<rect x="{mx - 48}" y="{y_line - 36}" width="96" height="20" rx="4" fill="#e0f2fe" stroke="#0284c7" stroke-width="1"/>')
        parts.append(f'<text x="{mx}" y="{y_line - 22}" font-size="10" font-weight="bold" fill="#0369a1" text-anchor="middle">{rate_label}</text>')

    # Cash flow indicators below line
    for yr, lbl, kind in cash_flows:
        x = to_x(yr)
        if kind == "deposit" or kind == "initial":
            color = "#16a34a"
            arrow = f'<polygon points="{x},{y_line+26} {x-4},{y_line+34} {x+4},{y_line+34}" fill="{color}"/>'
            parts.append(arrow)
            parts.append(f'<text x="{x}" y="{y_line + 46}" font-size="10" font-weight="bold" fill="{color}" text-anchor="middle">+{lbl}</text>')
        else:
            color = "#dc2626"
            arrow = f'<polygon points="{x},{y_line+34} {x-4},{y_line+26} {x+4},{y_line+26}" fill="{color}"/>'
            parts.append(arrow)
            parts.append(f'<text x="{x}" y="{y_line + 46}" font-size="10" font-weight="bold" fill="{color}" text-anchor="middle">-{lbl}</text>')

    parts.append("</svg>")
    return "".join(parts)


# Archetype 26: Nominal from Effective Annual Rate
def arch_26_nominal_rate_from_effective_annual_rate(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    eff_pct = r.choice([9.5, 10, 10.5, 11, 11.5, 12, 12.5])
    i_eff = eff_pct / 100.0
    freq_name, m = r.choice([("monthly", 12), ("quarterly", 4), ("half-yearly", 2)])

    i_nom = m * (((1.0 + i_eff) ** (1.0 / m)) - 1.0)
    nom_pct = round(i_nom * 100.0, 2)
    eff_str = num(eff_pct)
    ans_str = num(nom_pct, 2)

    prompt = (
        f"An investment yields an effective annual interest rate of {eff_str}%. "
        f"Calculate the nominal annual interest rate compounded {freq_name} that will yield the same return. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{Given effective rate }} i_{{\text{{eff}}}} = {eff_str}\%\text{{, calculate nominal rate }} "
        rf"i_{{\text{{nom}}}} \text{{ compounded {freq_name} (to 2 dec places).}}"
    )

    factor = round((1.0 + i_eff) ** (1.0 / m), 6)
    steps = [
        step(from_latex=r"1 + i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{m}\right)^m", to_latex_str=rf"1 + {num(i_eff)} = \left(1 + \frac{{i_{{\text{{nom}}}}}}{{{m}}}\right)^{{{m}}}", op="substitute known effective rate into conversion formula", rule="effective to nominal interest formula",),
        step(from_latex=rf"1 + \frac{{i_{{\text{{nom}}}}}}{{{m}}} = (1 + {num(i_eff)})^\frac{{1}}{{{m}}} = ({num(round(1.0 + i_eff, 4))})^\frac{{1}}{{{m}}}", to_latex_str=rf"1 + \frac{{i_{{\text{{nom}}}}}}{{{m}}} = {num(factor)}", op="take the m-th root of both sides", rule="m-th root extraction",),
        step(from_latex=rf"\frac{{i_{{\text{{nom}}}}}}{{{m}}} = {num(factor)} - 1 = {num(round(factor - 1.0, 6))}", to_latex_str=rf"i_{{\text{{nom}}}} = {m} \times {num(round(factor - 1.0, 6))} = {num(round(i_nom, 4))}", op="isolate and multiply by m", rule="algebraic solution",),
        step(from_latex=rf"r_{{\text{{nom}}}} = {num(round(i_nom, 4))} \times 100\%", to_latex_str=rf"{ans_str}\%", op="convert to percentage", rule="percentage conversion",),
    ]
    canonical = solution_graph(
        goal=f"calculate nominal rate compounded {freq_name} from effective rate",
        steps=steps,
        final_latex=rf"{ans_str}\%",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote 1 + i_eff = (1 + i_nom / m)^m", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Taking {m}-th root: (1 + i_eff)^(1/{m})", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Multiplication by m = {m}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate nominal rate {ans_str}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_26",
        topic=TOPIC_NAME,
        subskill="26_nominal_rate_from_effective_annual_rate",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\%",
        sample_answer=rf"{ans_str}%",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": f"To solve for i_nom: (1 + i_eff)^(1/{m}) - 1 = i_nom / {m}.",
            "concept": f"Multiply the result of (1 + i_eff)^(1/{m}) - 1 by {m}.",
            "breakdown": f"i_nom = {m} * ((1 + {i_eff})^(1/{m}) - 1) = {nom_pct}%.",
        },
        misconception_tags=["divided_by_m_instead_of_multiplying_at_end"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 27: Compare Two Bank Offers via Effective Rates
def arch_27_compare_two_bank_offers_via_effective_rates(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    nom_a = r.choice([9.6, 9.9, 10.2])
    m_a = 12
    eff_a = ((1.0 + (nom_a / 100.0) / m_a) ** m_a) - 1.0

    nom_b = round(nom_a + r.choice([0.2, 0.3, 0.4]), 2)
    m_b = 2
    eff_b = ((1.0 + (nom_b / 100.0) / m_b) ** m_b) - 1.0

    eff_a_pct = round(eff_a * 100.0, 2)
    eff_b_pct = round(eff_b * 100.0, 2)

    best_bank = "Bank A" if eff_a > eff_b else "Bank B"
    diff = abs(eff_a_pct - eff_b_pct)

    nom_a_str = num(nom_a)
    nom_b_str = num(nom_b)
    eff_a_str = num(eff_a_pct, 2)
    eff_b_str = num(eff_b_pct, 2)

    prompt = (
        f"{name} wants to open a fixed savings account and is comparing two investment options:\n"
        f"- **Bank A** offers {nom_a_str}% p.a. compounded monthly.\n"
        f"- **Bank B** offers {nom_b_str}% p.a. compounded half-yearly.\n\n"
        f"By calculating the effective annual interest rate for EACH bank, advise {name} on which bank offers "
        f"the better investment return."
    )
    prompt_latex = (
        rf"\text{{Bank A: }}{nom_a_str}\% \text{{ monthly vs Bank B: }}{nom_b_str}\% \text{{ half-yearly. "
        rf"Calculate effective rates and recommend superior bank.}}"
    )

    steps = [
        step(from_latex=r"1 + i_{\text{eff, A}} = \left(1 + \frac{i_{\text{nom}}}{12}\right)^{12}", to_latex_str=rf"i_{{\text{{eff, A}}}} = \left(1 + \frac{{{num(nom_a/100)}}}{{12}}\right)^{{12}} - 1 = {eff_a_str}\%", op="calculate effective annual rate for Bank A", rule="monthly effective rate conversion",),
        step(from_latex=r"1 + i_{\text{eff, B}} = \left(1 + \frac{i_{\text{nom}}}{2}\right)^2", to_latex_str=rf"i_{{\text{{eff, B}}}} = \left(1 + \frac{{{num(nom_b/100)}}}{{2}}\right)^2 - 1 = {eff_b_str}\%", op="calculate effective annual rate for Bank B", rule="half-yearly effective rate conversion",),
        step(from_latex=rf"\text{{Compare: }} {eff_a_str}\% \text{{ vs }} {eff_b_str}\%", to_latex_str=rf"\text{{{best_bank} is better with effective rate of }} {max(eff_a_str, eff_b_str)}\%", op="compare effective rates and make recommendation", rule="decision rule for investment returns",),
    ]
    canonical = solution_graph(
        goal=f"compare two bank offers via effective annual rates",
        steps=steps,
        final_latex=rf"\text{{{best_bank}}}",
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Bank A effective rate: {eff_a_str}%", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Bank B effective rate: {eff_b_str}%", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Correct conclusion: {best_bank}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_27",
        topic=TOPIC_NAME,
        subskill="27_compare_two_bank_offers_via_effective_rates",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{{best_bank}}}",
        sample_answer=rf"{best_bank} (Bank A: {eff_a_str}%, Bank B: {eff_b_str}%)",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Convert both nominal rates into effective annual rates before comparing.",
            "concept": "The account with the higher effective annual rate provides the greater return on investment.",
            "breakdown": f"Bank A = (1 + {nom_a}/1200)^12 - 1 = {eff_a_pct}%. Bank B = (1 + {nom_b}/200)^2 - 1 = {eff_b_pct}%. Best: {best_bank}.",
        },
        misconception_tags=["compared_nominal_rates_directly_without_converting_to_effective"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 28: Timeline — Single Interest Rate Change
def arch_28_timeline_single_interest_rate_change(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(12, 35) * 5000
    n1 = r.randint(2, 3)
    n2 = r.randint(3, 4)
    total_n = n1 + n2

    r1_pct = r.choice([8, 9, 10])
    r2_pct = r.choice([10.5, 11, 12])
    i1 = r1_pct / 100.0
    i2 = r2_pct / 100.0

    # Compounding: period 1 annually, period 2 monthly
    m1 = 1
    m2 = 12
    a_final = p_val * ((1.0 + i1 / m1) ** (n1 * m1)) * ((1.0 + i2 / m2) ** (n2 * m2))

    p_str = num(p_val)
    r1_str = num(r1_pct)
    r2_str = num(r2_pct)
    ans_str = num(round(a_final, 2), 2)

    diag_svg = timeline_svg(
        total_years=total_n,
        intervals=[(0, n1, f"{r1_str}% p.a."), (n1, total_n, f"{r2_str}% monthly")],
        cash_flows=[(0, f"R {p_str}", "initial")],
        title=f"{name}'s Investment Timeline ({total_n} Years)",
    )
    diagram_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Timeline of Interest Rate Change", "diagram_role": "context"}

    prompt = (
        f"{name} invested R {p_str} into a savings account for a total period of {total_n} years. "
        f"For the first {n1} years, the interest rate was {r1_str}% per annum compounded annually. "
        f"The interest rate then changed to {r2_str}% per annum compounded monthly for the remaining {n2} years. "
        f"Calculate the accumulated balance at the end of the {total_n}-year period. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} invests R }}{p_str}\text{{ for }}{total_n}\text{{ years: }}{r1_str}\% \text{{ p.a. for first }} "
        rf"{n1}\text{{ years, then }}{r2_str}\% \text{{ monthly for }}{n2}\text{{ years. Find final balance.}} "
    )

    steps = [
        step(from_latex=r"A = P(1 + i_1)^{n_1}\left(1 + \frac{i_2}{12}\right)^{12n_2}", to_latex_str=rf"A = {p_str}(1 + {num(i1)})^{{{n1}}}\left(1 + \frac{{{num(i2)}}}{{12}}\right)^{{12 \times {n2}}}", op="set up chained timeline compounding formula", rule="multi-stage timeline compound formula",),
        step(from_latex=rf"A = {p_str}({num(round(1.0 + i1, 4))})^{{{n1}}}\left(1 + {num(round(i2/12.0, 6))}\right)^{{{n2 * 12}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate chained growth factors and multiply by principal", rule="multiplication of compounding factors",),
    ]
    canonical = solution_graph(
        goal=f"calculate final amount after interest rate change",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"First period factor: (1 + {r1_str}%)^{n1}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Second period factor: (1 + {r2_str}%/12)^({n2*12})", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_28",
        topic=TOPIC_NAME,
        subskill="28_timeline_single_interest_rate_change",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diagram_spec,
        hints={
            "nudge": "Multiply the initial principal by the growth factors for both consecutive periods: A = P(1 + i1)^n1 * (1 + i2/m2)^(m2*n2).",
            "concept": "Do not round off intermediate balances; calculate the product in one continuous step.",
            "breakdown": f"A = {p_val}(1 + {i1})^{n1} * (1 + {i2}/12)^{n2*12} = R {round(a_final, 2):.2f}.",
        },
        misconception_tags=["added_growth_factors_instead_of_multiplying"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 29: Timeline — Two Interest Rate Changes (Three Phases)
def arch_29_timeline_two_interest_rate_changes(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(15, 30) * 5000
    n1, n2, n3 = 2, 2, 2
    total_n = n1 + n2 + n3

    r1_pct, r2_pct, r3_pct = 8.0, 9.6, 10.8
    i1, i2, i3 = r1_pct / 100.0, r2_pct / 100.0, r3_pct / 100.0

    # Phase 1: annual, Phase 2: quarterly, Phase 3: monthly
    a_final = p_val * ((1.0 + i1) ** n1) * ((1.0 + i2 / 4) ** (n2 * 4)) * ((1.0 + i3 / 12) ** (n3 * 12))

    p_str = num(p_val)
    ans_str = num(round(a_final, 2), 2)

    prompt = (
        f"{name} invested R {p_str} for a period of {total_n} years:\n"
        f"- For the first {n1} years, the rate was {num(r1_pct)}% p.a. compounded annually.\n"
        f"- For the next {n2} years, the rate was {num(r2_pct)}% p.a. compounded quarterly.\n"
        f"- For the final {n3} years, the rate was {num(r3_pct)}% p.a. compounded monthly.\n\n"
        f"Calculate the total accumulated balance at the end of {total_n} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} invests R }}{p_str}\text{{ over 3 stages (}}{n1}\text{{y at }}{num(r1_pct)}\%\text{{, }} "
        rf"{n2}\text{{y at }}{num(r2_pct)}\%\text{{ quarterly, }}{n3}\text{{y at }}{num(r3_pct)}\%\text{{ monthly). Find }} A."
    )

    steps = [
        step(from_latex=r"A = P(1 + i_1)^{n_1}\left(1 + \frac{i_2}{4}\right)^{4n_2}\left(1 + \frac{i_3}{12}\right)^{12n_3}", to_latex_str=rf"A = {p_str}(1 + {num(i1)})^{{{n1}}}\left(1 + \frac{{{num(i2)}}}{{4}}\right)^{{8}}\left(1 + \frac{{{num(i3)}}}{{12}}\right)^{{24}}", op="substitute all 3 compounding intervals into chained product formula", rule="three-stage timeline formula",),
        step(from_latex=rf"A = {p_str}({num(round(1.0 + i1, 4))})^2({num(round(1.0 + i2/4.0, 4))})^8({num(round(1.0 + i3/12.0, 4))})^{{24}}", to_latex_str=rf"\text{{R }} {ans_str}", op="multiply consecutive compounding factors", rule="multiplication",),
    ]
    canonical = solution_graph(
        goal=f"calculate final balance across 3 interest rate phases",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Phase 1 factor: (1 + {r1_pct}%)^{n1}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Phase 2 factor: (1 + {r2_pct}%/4)^8", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Phase 3 factor: (1 + {r3_pct}%/12)^24", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_29",
        topic=TOPIC_NAME,
        subskill="29_timeline_two_interest_rate_changes",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Chain all three growth factors together in a single multiplication.",
            "concept": "A = P * (factor 1) * (factor 2) * (factor 3).",
            "breakdown": f"A = {p_val} * (1 + {i1})^2 * (1 + {i2}/4)^8 * (1 + {i3}/12)^24 = R {round(a_final, 2):.2f}.",
        },
        misconception_tags=["reset_principal_at_each_phase"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=6,
    )


# Archetype 30: Timeline — Single Additional Deposit
def arch_30_timeline_single_additional_deposit(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(10, 25) * 5000
    dep_val = r.randint(8, 20) * 2500
    dep_yr = r.randint(2, 3)
    total_n = dep_yr + r.randint(2, 3)

    rate_pct = r.choice([9, 9.6, 10.2, 10.8, 12])
    i_dec = rate_pct / 100.0
    m = 12
    i_m = i_dec / m

    # Total accumulated = P*(1+i/m)^(12*total_n) + Dep*(1+i/m)^(12*(total_n - dep_yr))
    n_p = total_n * m
    n_dep = (total_n - dep_yr) * m
    a_final = p_val * ((1.0 + i_m) ** n_p) + dep_val * ((1.0 + i_m) ** n_dep)

    p_str = num(p_val)
    dep_str = num(dep_val)
    rate_str = num(rate_pct)
    ans_str = num(round(a_final, 2), 2)

    diag_svg = timeline_svg(
        total_years=total_n,
        intervals=[(0, total_n, f"{rate_str}% monthly")],
        cash_flows=[(0, f"R {p_str}", "initial"), (dep_yr, f"R {dep_str}", "deposit")],
        title=f"{name}'s Investment with Additional Deposit at T{dep_yr}",
    )
    diagram_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Timeline with Deposit", "diagram_role": "context"}

    prompt = (
        f"{name} deposited R {p_str} into a savings account paying {rate_str}% p.a. compounded monthly. "
        f"At the end of {dep_yr} years, {name} deposited a further R {dep_str} into the same account. "
        f"Calculate the total amount in the account at the end of {total_n} years from the initial deposit. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} deposits R }}{p_str}\text{{ initially, plus R }}{dep_str}\text{{ at }} T_{{{dep_yr}}} "
        rf"\text{{ (total }}{total_n}\text{{ years, rate }}{rate_str}\% \text{{ monthly). Find final balance.}} "
    )

    steps = [
        step(from_latex=r"A = P\left(1 + \frac{i}{12}\right)^{12n_1} + D\left(1 + \frac{i}{12}\right)^{12n_2}", to_latex_str=rf"A = {p_str}\left(1 + \frac{{{num(i_dec)}}}{{12}}\right)^{{{n_p}}} + {dep_str}\left(1 + \frac{{{num(i_dec)}}}{{12}}\right)^{{{n_dep}}}", op="grow each cash flow forward to the end of the investment horizon", rule="timeline accumulation rule",),
        step(from_latex=rf"A = {p_str}(1 + {num(i_m)})^{{{n_p}}} + {dep_str}(1 + {num(i_m)})^{{{n_dep}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate sum of compound growth streams", rule="addition of grown cash flows",),
    ]
    canonical = solution_graph(
        goal=f"calculate balance after additional deposit using timeline method",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Initial deposit compounded for {total_n} years ({n_p} months)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Second deposit compounded for {total_n - dep_yr} years ({n_dep} months)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate total accumulated balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_30",
        topic=TOPIC_NAME,
        subskill="30_timeline_single_additional_deposit",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diagram_spec,
        hints={
            "nudge": "Each deposit grows forward to the end of the timeline: A = P(1+i/12)^N1 + D(1+i/12)^N2.",
            "concept": f"The second deposit of R {dep_str} stays in the account for only {total_n - dep_yr} years ({n_dep} months).",
            "breakdown": f"A = {p_val}(1 + {i_m})^{n_p} + {dep_val}(1 + {i_m})^{n_dep} = R {round(a_final, 2):.2f}.",
        },
        misconception_tags=["compounded_second_deposit_for_full_time"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 31: Timeline — Single Withdrawal
def arch_31_timeline_single_withdrawal(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(20, 50) * 5000
    with_val = r.randint(5, 15) * 2000
    with_yr = r.randint(2, 3)
    total_n = with_yr + r.randint(2, 3)

    rate_pct = r.choice([9, 9.6, 10.2, 10.8, 12])
    i_dec = rate_pct / 100.0
    m = 12
    i_m = i_dec / m

    n_p = total_n * m
    n_with = (total_n - with_yr) * m
    a_final = p_val * ((1.0 + i_m) ** n_p) - with_val * ((1.0 + i_m) ** n_with)

    p_str = num(p_val)
    with_str = num(with_val)
    rate_str = num(rate_pct)
    ans_str = num(round(a_final, 2), 2)

    diag_svg = timeline_svg(
        total_years=total_n,
        intervals=[(0, total_n, f"{rate_str}% monthly")],
        cash_flows=[(0, f"R {p_str}", "initial"), (with_yr, f"R {with_str}", "withdrawal")],
        title=f"{name}'s Investment with Withdrawal at T{with_yr}",
    )
    diagram_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Timeline with Withdrawal", "diagram_role": "context"}

    prompt = (
        f"{name} invested R {p_str} into a fixed deposit account earning {rate_str}% p.a. compounded monthly. "
        f"At the end of {with_yr} years, {name} withdrew R {with_str} to pay an unexpected expense. "
        f"Calculate the balance remaining in the account at the end of {total_n} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} invests R }}{p_str}\text{{ initially, withdraws R }}{with_str}\text{{ at }} T_{{{with_yr}}} "
        rf"\text{{ (total }}{total_n}\text{{ years, rate }}{rate_str}\% \text{{ monthly). Find final balance.}} "
    )

    steps = [
        step(from_latex=r"A = P\left(1 + \frac{i}{12}\right)^{12n_1} - W\left(1 + \frac{i}{12}\right)^{12n_2}", to_latex_str=rf"A = {p_str}\left(1 + \frac{{{num(i_dec)}}}{{12}}\right)^{{{n_p}}} - {with_str}\left(1 + \frac{{{num(i_dec)}}}{{12}}\right)^{{{n_with}}}", op="grow initial deposit forward and subtract grown withdrawal", rule="timeline withdrawal subtraction rule",),
        step(from_latex=rf"A = {p_str}(1 + {num(i_m)})^{{{n_p}}} - {with_str}(1 + {num(i_m)})^{{{n_with}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate remaining balance after withdrawal", rule="subtraction of compound streams",),
    ]
    canonical = solution_graph(
        goal=f"calculate balance remaining after withdrawal using timeline method",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Initial deposit compounded for {total_n} years ({n_p} months)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Subtracted withdrawal compounded for {total_n - with_yr} years ({n_with} months)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_31",
        topic=TOPIC_NAME,
        subskill="31_timeline_single_withdrawal",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diagram_spec,
        hints={
            "nudge": "Subtract the grown withdrawal from the grown initial deposit: A = P(1+i/12)^N1 - W(1+i/12)^N2.",
            "concept": f"The withdrawal of R {with_str} loses compound growth for the remaining {total_n - with_yr} years ({n_with} months).",
            "breakdown": f"A = {p_val}(1 + {i_m})^{n_p} - {with_val}(1 + {i_m})^{n_with} = R {round(a_final, 2):.2f}.",
        },
        misconception_tags=["added_instead_of_subtracted_withdrawal"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 32: Timeline — Deposit and Withdrawal Combined
def arch_32_timeline_deposit_and_withdrawal_combined(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(20, 45) * 5000
    t_dep = 2
    dep_val = r.randint(6, 15) * 2500
    t_with = 4
    with_val = r.randint(4, 12) * 2000
    total_n = 6

    rate_pct = r.choice([9.6, 10.2, 10.8, 12])
    i_dec = rate_pct / 100.0
    m = 12
    i_m = i_dec / m

    n_p = total_n * m
    n_dep = (total_n - t_dep) * m
    n_with = (total_n - t_with) * m

    a_final = (
        p_val * ((1.0 + i_m) ** n_p)
        + dep_val * ((1.0 + i_m) ** n_dep)
        - with_val * ((1.0 + i_m) ** n_with)
    )

    p_str = num(p_val)
    dep_str = num(dep_val)
    with_str = num(with_val)
    rate_str = num(rate_pct)
    ans_str = num(round(a_final, 2), 2)

    diag_svg = timeline_svg(
        total_years=total_n,
        intervals=[(0, total_n, f"{rate_str}% monthly")],
        cash_flows=[(0, f"R {p_str}", "initial"), (t_dep, f"R {dep_str}", "deposit"), (t_with, f"R {with_str}", "withdrawal")],
        title=f"{name}'s Timeline with Deposit & Withdrawal",
    )
    diagram_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Deposit and Withdrawal Timeline", "diagram_role": "context"}

    prompt = (
        f"{name} opened a savings account with an initial deposit of R {p_str}. "
        f"The interest rate remained fixed at {rate_str}% p.a. compounded monthly throughout the investment.\n"
        f"- At the end of {t_dep} years, {name} deposited another R {dep_str}.\n"
        f"- At the end of {t_with} years, {name} withdrew R {with_str}.\n\n"
        f"Calculate the balance in {name}'s account at the end of {total_n} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name}: R }}{p_str}\text{{ at }} T_0\text{{, +R }}{dep_str}\text{{ at }} T_{{{t_dep}}}\text{{, -R }}{with_str} "
        rf"\text{{ at }} T_{{{t_with}}}\text{{ at }}{rate_str}\% \text{{ monthly over }}{total_n}\text{{ years. Find }} A."
    )

    steps = [
        step(from_latex=r"A = P\left(1 + \frac{i}{12}\right)^{12n_1} + D\left(1 + \frac{i}{12}\right)^{12n_2} - W\left(1 + \frac{i}{12}\right)^{12n_3}", to_latex_str=rf"A = {p_str}(1 + {num(i_m)})^{{{n_p}}} + {dep_str}(1 + {num(i_m)})^{{{n_dep}}} - {with_str}(1 + {num(i_m)})^{{{n_with}}}", op="apply timeline equation adding deposit and subtracting withdrawal", rule="combined timeline equation",),
        step(from_latex=rf"A = {p_str}(1 + {num(i_m)})^{{{n_p}}} + {dep_str}(1 + {num(i_m)})^{{{n_dep}}} - {with_str}(1 + {num(i_m)})^{{{n_with}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate total combined balance", rule="arithmetic calculation",),
    ]
    canonical = solution_graph(
        goal=f"calculate balance after deposit and withdrawal",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"P compounded for {n_p} months", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Deposit compounded for {n_dep} months", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Withdrawal compounded for {n_with} months", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Correct signs (+ deposit, - withdrawal)", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_32",
        topic=TOPIC_NAME,
        subskill="32_timeline_deposit_and_withdrawal_combined",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diagram_spec,
        hints={
            "nudge": "Add the grown additional deposit and subtract the grown withdrawal from the grown initial deposit.",
            "concept": "P(1+i)^72 + D(1+i)^48 - W(1+i)^24.",
            "breakdown": f"A = {p_val}(1+{i_m})^{n_p} + {dep_val}(1+{i_m})^{n_dep} - {with_val}(1+{i_m})^{n_with} = R {round(a_final, 2):.2f}.",
        },
        misconception_tags=["subtracted_deposit_or_added_withdrawal"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=6,
    )


# Archetype 33: Timeline — Two Deposits with Interest Rate Change
def arch_33_timeline_two_deposits_different_rates(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(15, 30) * 5000
    t_rate_change = 3
    dep2_val = r.randint(10, 25) * 2000
    total_n = 5

    r1_pct = 9.0
    r2_pct = 12.0
    i1 = r1_pct / 100.0 / 12.0
    i2 = r2_pct / 100.0 / 12.0

    # P grows for 36 months at i1, then full balance + dep2 grows for 24 months at i2
    bal_t3 = p_val * ((1.0 + i1) ** 36) + dep2_val
    a_final = bal_t3 * ((1.0 + i2) ** 24)

    p_str = num(p_val)
    dep_str = num(dep2_val)
    ans_str = num(round(a_final, 2), 2)

    prompt = (
        f"{name} invested R {p_str} into a bank account paying 9% p.a. compounded monthly. "
        f"After 3 years, the interest rate was increased to 12% p.a. compounded monthly, "
        f"and {name} simultaneously deposited an extra R {dep_str} into the account. "
        f"Determine the final amount in the account 5 years after the initial deposit. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name} invests R }}{p_str}\text{{ at 9\% monthly. At }} T_3\text{{, rate rises to 12\% and deposits R }}{dep_str}. "
        rf"\text{{ Find balance at }} T_5."
    )

    steps = [
        step(from_latex=r"A = \left[P\left(1 + \frac{i_1}{12}\right)^{36} + D\right]\left(1 + \frac{i_2}{12}\right)^{24}", to_latex_str=rf"A = \left[{p_str}(1 + {num(i1)})^{{36}} + {dep_str}\right](1 + {num(i2)})^{{24}}", op="accumulate to T3, add deposit, and grow combined amount to T5", rule="multi-stage rate change and deposit formula",),
        step(from_latex=rf"A = \left[{num(round(p_val * ((1.0 + i1)**36), 2))} + {dep_str}\right](1 + {num(i2)})^{{24}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate final accumulated balance", rule="multiplication",),
    ]
    canonical = solution_graph(
        goal=f"calculate balance with rate change and simultaneous deposit",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Compounding initial deposit at 9% monthly for 36 months", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Adding R dep at T3", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Compounding total balance at 12% monthly for 24 months", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_33",
        topic=TOPIC_NAME,
        subskill="33_timeline_two_deposits_different_rates",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Find the balance just before the deposit at T3, add the new deposit, and grow that total to T5.",
            "concept": "A = [P(1 + i1/12)^36 + D] * (1 + i2/12)^24.",
            "breakdown": f"Bal at T3 = R {bal_t3:.2f}. Bal at T5 = R {round(a_final, 2):.2f}.",
        },
        misconception_tags=["forgot_to_apply_second_rate_to_accumulated_first_balance"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=6,
    )


# Archetype 34: Timeline — Two Withdrawals
def arch_34_timeline_two_withdrawals(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(30, 60) * 5000
    w1 = r.randint(5, 12) * 2000
    w2 = r.randint(4, 10) * 2000
    total_n = 5

    rate_pct = 10.8
    i_m = (rate_pct / 100.0) / 12.0

    # Withdrawals at T2 (year 2) and T4 (year 4)
    a_final = (
        p_val * ((1.0 + i_m) ** 60)
        - w1 * ((1.0 + i_m) ** (3 * 12))
        - w2 * ((1.0 + i_m) ** (1 * 12))
    )

    p_str = num(p_val)
    w1_str = num(w1)
    w2_str = num(w2)
    ans_str = num(round(a_final, 2), 2)

    prompt = (
        f"{name} invested R {p_str} in an account earning {num(rate_pct)}% p.a. compounded monthly. "
        f"At the end of year 2, {name} withdrew R {w1_str}. At the end of year 4, a further R {w2_str} was withdrawn. "
        f"Calculate the balance at the end of year 5. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name}: R }}{p_str}\text{{ initially, -R }}{w1_str}\text{{ at }} T_2\text{{, -R }}{w2_str}\text{{ at }} T_4. "
        rf"\text{{Rate: }}{num(rate_pct)}\%\text{{ monthly over 5 years. Find }} A."
    )

    steps = [
        step(from_latex=r"A = P\left(1 + \frac{i}{12}\right)^{60} - W_1\left(1 + \frac{i}{12}\right)^{36} - W_2\left(1 + \frac{i}{12}\right)^{12}", to_latex_str=rf"A = {p_str}(1 + {num(i_m)})^{{60}} - {w1_str}(1 + {num(i_m)})^{{36}} - {w2_str}(1 + {num(i_m)})^{{12}}", op="subtract each grown withdrawal from the grown initial principal", rule="multi-withdrawal timeline rule",),
        step(from_latex=rf"A = {p_str}(1 + {num(i_m)})^{{60}} - {w1_str}(1 + {num(i_m)})^{{36}} - {w2_str}(1 + {num(i_m)})^{{12}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate remaining balance", rule="arithmetic evaluation",),
    ]
    canonical = solution_graph(
        goal=f"calculate balance after two withdrawals",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Initial deposit compounded for 60 months", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "First withdrawal compounded for 36 months", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Second withdrawal compounded for 12 months", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Correct subtraction of both withdrawals", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_34",
        topic=TOPIC_NAME,
        subskill="34_timeline_two_withdrawals",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Subtract both grown withdrawals from the grown principal: A = P(1+i)^60 - W1(1+i)^36 - W2(1+i)^12.",
            "concept": "The first withdrawal loses 3 years of interest; the second loses 1 year of interest.",
            "breakdown": f"A = R {round(a_final, 2):.2f}.",
        },
        misconception_tags=["subtracted_withdrawals_without_compounding_them"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=6,
    )


# Archetype 35: Timeline — Solve Initial Deposit Given Final Amount
def arch_35_timeline_solve_initial_deposit_given_final_amount(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(15, 35) * 5000
    dep_val = r.randint(8, 20) * 2000
    dep_yr = 2
    total_n = 5

    rate_pct = 9.6
    i_m = (rate_pct / 100.0) / 12.0

    n_p = total_n * 12
    n_dep = (total_n - dep_yr) * 12
    a_target = p_val * ((1.0 + i_m) ** n_p) + dep_val * ((1.0 + i_m) ** n_dep)

    a_str = num(round(a_target, 2), 2)
    dep_str = num(dep_val)
    ans_str = num(p_val)

    prompt = (
        f"{name} invested a sum of money, R P, into an account earning {num(rate_pct)}% p.a. compounded monthly. "
        f"At the end of {dep_yr} years, {name} added R {dep_str} into the account. "
        f"At the end of {total_n} years, the total balance in the account was R {a_str}. "
        f"Calculate the value of the initial deposit, P."
    )
    prompt_latex = (
        rf"\text{{{name} invested R }} P\text{{ at }}{num(rate_pct)}\%\text{{ monthly, added R }}{dep_str} "
        rf"\text{{ at }} T_{{{dep_yr}}}\text{{, reaching R }}{a_str}\text{{ at }} T_{{{total_n}}}\text{{. Find }} P."
    )

    grown_dep = round(dep_val * ((1.0 + i_m) ** n_dep), 2)
    rem_target = round(a_target - grown_dep, 2)
    steps = [
        step(from_latex=r"A = P\left(1 + \frac{i}{12}\right)^{60} + D\left(1 + \frac{i}{12}\right)^{36}", to_latex_str=rf"{a_str} = P(1 + {num(i_m)})^{{60}} + {dep_str}(1 + {num(i_m)})^{{36}}", op="write down timeline equation with unknown P", rule="timeline equation",),
        step(from_latex=rf"{a_str} - {dep_str}(1 + {num(i_m)})^{{36}} = P(1 + {num(i_m)})^{{60}}", to_latex_str=rf"{num(rem_target)} = P(1 + {num(i_m)})^{{60}}", op="subtract grown interim deposit from target balance", rule="subtraction",),
        step(from_latex=rf"P = \frac{{{num(rem_target)}}}{{(1 + {num(i_m)})^{{60}}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="divide remaining balance by initial growth factor to find P", rule="division",),
    ]
    canonical = solution_graph(
        goal=f"solve for initial principal P in timeline problem",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Sets up timeline equation with unknown P", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Compounding of second deposit for 36 months", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Subtracts grown deposit from final total", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Divides by (1 + i)^60 to isolate P", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Accurate initial deposit P = R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_35",
        topic=TOPIC_NAME,
        subskill="35_timeline_solve_initial_deposit_given_final_amount",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Subtract the grown value of the second deposit from the total amount, then discount back to T0.",
            "concept": "P = [A - D(1+i)^36] / (1+i)^60.",
            "breakdown": f"Grown deposit = R {grown_dep:.2f}. Balance from P = R {rem_target:.2f}. P = R {p_val}.",
        },
        misconception_tags=["subtracted_undepreciated_deposit_directly"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=6,
    )


# Archetype 36: Timeline — Solve Additional Deposit to Meet Target
def arch_36_timeline_solve_additional_deposit_to_meet_target(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(15, 30) * 5000
    dep_val = r.randint(8, 20) * 2000
    dep_yr = 2
    total_n = 5

    rate_pct = 10.8
    i_m = (rate_pct / 100.0) / 12.0
    a_target = p_val * ((1.0 + i_m) ** 60) + dep_val * ((1.0 + i_m) ** 36)

    p_str = num(p_val)
    a_str = num(round(a_target, 2), 2)
    ans_str = num(dep_val)

    prompt = (
        f"{name} invested R {p_str} in an account paying {num(rate_pct)}% p.a. compounded monthly. "
        f"At the end of {dep_yr} years, {name} makes an additional deposit of R x. "
        f"At the end of {total_n} years, the total investment reaches R {a_str}. "
        f"Determine the value of the additional deposit, x. "
        f"Round off your answer to the nearest Rand."
    )
    prompt_latex = (
        rf"\text{{{name}: R }}{p_str}\text{{ at }} T_0\text{{, adds R }} x \text{{ at }} T_{{{dep_yr}}}\text{{, reaches R }}{a_str} "
        rf"\text{{ at }} T_{{{total_n}}}\text{{ (rate }}{num(rate_pct)}\%\text{{ monthly). Find }} x."
    )

    grown_p = round(p_val * ((1.0 + i_m) ** 60), 2)
    diff = round(a_target - grown_p, 2)
    steps = [
        step(from_latex=r"P\left(1 + \frac{i}{12}\right)^{60} + x\left(1 + \frac{i}{12}\right)^{36} = A", to_latex_str=rf"{p_str}(1 + {num(i_m)})^{{60}} + x(1 + {num(i_m)})^{{36}} = {a_str}", op="write down timeline equation with unknown interim deposit x", rule="timeline equation",),
        step(from_latex=rf"x(1 + {num(i_m)})^{{36}} = {a_str} - {num(grown_p)} = {num(diff)}", to_latex_str=rf"x = \frac{{{num(diff)}}}{{(1 + {num(i_m)})^{{36}}}} = \text{{R }} {ans_str}", op="divide shortfall by 36-month growth factor to solve for x", rule="algebraic solution",),
    ]
    canonical = solution_graph(
        goal=f"solve for additional deposit x",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Compounding initial deposit to T5", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Forming shortfall equation A - grown P", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Dividing shortfall by (1 + i)^36", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate deposit x = R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_36",
        topic=TOPIC_NAME,
        subskill="36_timeline_solve_additional_deposit_to_meet_target",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Find how much the initial R P grows to by T5, then find the shortfall to the target.",
            "concept": "x = [A - P(1+i)^60] / (1+i)^36.",
            "breakdown": f"Grown P = R {grown_p:.2f}. Shortfall = R {diff:.2f}. x = {diff} / (1+{i_m})^36 = R {dep_val}.",
        },
        misconception_tags=["assumed_shortfall_is_the_actual_deposit_without_discounting"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 37: Timeline — Solve Withdrawal Amount
def arch_37_timeline_solve_withdrawal_amount(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(25, 50) * 5000
    with_val = r.randint(6, 18) * 2000
    with_yr = 2
    total_n = 5

    rate_pct = 10.2
    i_m = (rate_pct / 100.0) / 12.0
    a_final = p_val * ((1.0 + i_m) ** 60) - with_val * ((1.0 + i_m) ** 36)

    p_str = num(p_val)
    a_str = num(round(a_final, 2), 2)
    ans_str = num(with_val)

    prompt = (
        f"{name} invested R {p_str} in a bank at {num(rate_pct)}% p.a. compounded monthly. "
        f"At the end of {with_yr} years, {name} withdrew an amount of R w. "
        f"At the end of {total_n} years, the remaining balance was R {a_str}. "
        f"Calculate the value of the withdrawal, w. "
        f"Round off your answer to the nearest Rand."
    )
    prompt_latex = (
        rf"\text{{{name}: R }}{p_str}\text{{ initially, withdraws R }} w \text{{ at }} T_{{{with_yr}}}\text{{, leaving R }}{a_str} "
        rf"\text{{ at }} T_{{{total_n}}}\text{{ (rate }}{num(rate_pct)}\%\text{{ monthly). Find }} w."
    )

    grown_p = round(p_val * ((1.0 + i_m) ** 60), 2)
    diff = round(grown_p - a_final, 2)
    steps = [
        step(from_latex=r"P\left(1 + \frac{i}{12}\right)^{60} - w\left(1 + \frac{i}{12}\right)^{36} = A", to_latex_str=rf"{p_str}(1 + {num(i_m)})^{{60}} - w(1 + {num(i_m)})^{{36}} = {a_str}", op="write down timeline equation with unknown withdrawal w", rule="timeline withdrawal equation",),
        step(from_latex=rf"w(1 + {num(i_m)})^{{36}} = {num(grown_p)} - {a_str} = {num(diff)}", to_latex_str=rf"w = \frac{{{num(diff)}}}{{(1 + {num(i_m)})^{{36}}}} = \text{{R }} {ans_str}", op="divide lost amount by growth factor to find withdrawal w", rule="algebraic solution",),
    ]
    canonical = solution_graph(
        goal=f"solve for withdrawal amount w",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Compounding initial deposit to T5", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Finding difference between grown P and final balance", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Dividing difference by (1 + i)^36", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate withdrawal w = R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_37",
        topic=TOPIC_NAME,
        subskill="37_timeline_solve_withdrawal_amount",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Find the difference between what the account WOULD have had without withdrawals and what it actually has.",
            "concept": "w = [P(1+i)^60 - A] / (1+i)^36.",
            "breakdown": f"Without withdrawal = R {grown_p:.2f}. Deficit = R {diff:.2f}. w = {diff} / (1+{i_m})^36 = R {with_val}.",
        },
        misconception_tags=["subtracted_final_balance_directly_without_discounting"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 38: Inflation — Future Cost of Goods
def arch_38_inflation_future_cost_of_goods(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    goods = r.choice(["a loaf of bread", "a litre of petrol", "a basket of groceries", "a school uniform"])
    p_val = r.randint(15, 80) * 10
    n_years = r.randint(4, 8)
    inf_pct = r.choice([5, 5.5, 6, 6.5, 7])
    i_dec = inf_pct / 100.0

    a_val = p_val * ((1.0 + i_dec) ** n_years)
    p_str = num(p_val)
    inf_str = num(inf_pct)
    ans_str = num(round(a_val, 2), 2)

    prompt = (
        f"Currently, {goods} costs R {p_str}. "
        f"If the average annual inflation rate remains constant at {inf_str}% over the next {n_years} years, "
        f"calculate how much {goods} will cost at the end of {n_years} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{Cost R }}{p_str}\text{{. Inflation = }}{inf_str}\% \text{{ p.a. over }}{n_years} "
        rf"\text{{ years. Calculate future price }} A."
    )

    steps = [
        step(from_latex=r"A = P(1 + i)^n", to_latex_str=rf"A = {p_str}(1 + {num(i_dec)})^{{{n_years}}}", op="substitute current price and inflation rate into compound growth formula", rule="compound inflation formula",),
        step(from_latex=rf"A = {p_str}({num(round(1.0 + i_dec, 4))})^{{{n_years}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate power and multiply by present price", rule="arithmetic calculation",),
    ]
    canonical = solution_graph(
        goal=f"calculate future cost of goods after inflation",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 + i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution P={p_str}, i={inf_str}%, n={n_years}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate future price R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_38",
        topic=TOPIC_NAME,
        subskill="38_inflation_future_cost_of_goods",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Inflation causes prices to increase according to the compound growth formula: A = P(1 + i)^n.",
            "concept": "Treat current price as P, inflation rate as i, and years as n.",
            "breakdown": f"A = {p_val}(1 + {i_dec})^{n_years} = R {round(a_val, 2):.2f}.",
        },
        misconception_tags=["treated_inflation_as_simple_interest"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 39: Inflation — Purchasing Power Depreciation
def arch_39_inflation_purchasing_power_depreciation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(5, 20) * 10000
    n_years = r.randint(4, 7)
    inf_pct = r.choice([5, 6, 6.5, 7])
    i_dec = inf_pct / 100.0

    # Purchasing power of fixed cash amount drops to P / (1 + i)^n
    pv = p_val / ((1.0 + i_dec) ** n_years)
    p_str = num(p_val)
    inf_str = num(inf_pct)
    ans_str = num(round(pv, 2), 2)

    prompt = (
        f"{name} keeps R {p_str} cash in a home safe with zero interest for {n_years} years. "
        f"If the average annual inflation rate is {inf_str}%, calculate the real purchasing power "
        f"of this cash after {n_years} years (i.e. what this cash would be worth in today's money). "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{Cash R }}{p_str}\text{{ kept for }}{n_years}\text{{ years with zero interest at }}{inf_str}\% "
        rf"\text{{ inflation. Calculate real purchasing power today.}} "
    )

    factor = round((1.0 + i_dec) ** n_years, 6)
    steps = [
        step(from_latex=r"\text{Purchasing Power} = \frac{P}{(1 + i)^n}", to_latex_str=rf"\text{{Purchasing Power}} = \frac{{{p_str}}}{{(1 + {num(i_dec)})^{{{n_years}}}}}", op="deflate cash sum by compound inflation factor", rule="purchasing power deflation formula",),
        step(from_latex=rf"\frac{{{p_str}}}{{{num(factor)}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate present purchasing power", rule="arithmetic division",),
    ]
    canonical = solution_graph(
        goal=f"calculate real purchasing power of cash eroded by inflation",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote Purchasing Power = P / (1 + i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Substitution of P={p_str}, i={inf_str}%, n={n_years}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate purchasing power R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_39",
        topic=TOPIC_NAME,
        subskill="39_inflation_purchasing_power_depreciation",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Purchasing power of uninvested cash decreases: divide the amount by (1 + i)^n.",
            "concept": "Money in a safe buys less over time as prices inflate.",
            "breakdown": f"Purchasing power = {p_val} / (1 + {i_dec})^{n_years} = R {round(pv, 2):.2f}.",
        },
        misconception_tags=["multiplied_instead_of_divided_by_inflation_factor"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 40: Sinking Fund — Replacement Cost After Inflation
def arch_40_sinking_fund_replacement_cost_after_inflation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    asset = r.choice(ASSETS)
    p_val = r.randint(25, 70) * 10000
    n_years = r.randint(4, 6)
    inf_pct = r.choice([6, 6.5, 7, 7.5, 8])
    i_dec = inf_pct / 100.0

    a_rep = p_val * ((1.0 + i_dec) ** n_years)
    p_str = num(p_val)
    inf_str = num(inf_pct)
    ans_str = num(round(a_rep, 2), 2)

    prompt = (
        f"A factory purchases a new {asset} today for R {p_str}. "
        f"The factory plans to replace this {asset} in {n_years} years' time. "
        f"If the cost of new equipment increases at an average inflation rate of {inf_str}% per annum, "
        f"calculate the replacement cost of the {asset} in {n_years} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{asset} costs R }}{p_str}\text{{ today. Inflation = }}{inf_str}\% \text{{ p.a. over }}{n_years} "
        rf"\text{{ years. Calculate future replacement cost.}} "
    )

    steps = [
        step(from_latex=r"A = P(1 + i_{\text{inf}})^n", to_latex_str=rf"A = {p_str}(1 + {num(i_dec)})^{{{n_years}}}", op="substitute present cost and inflation rate into compound growth formula", rule="inflation growth formula",),
        step(from_latex=rf"A = {p_str}({num(round(1.0 + i_dec, 4))})^{{{n_years}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate future replacement cost", rule="arithmetic calculation",),
    ]
    canonical = solution_graph(
        goal=f"calculate replacement cost after inflation",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 + i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution P={p_str}, i={inf_str}%, n={n_years}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate replacement cost R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_40",
        topic=TOPIC_NAME,
        subskill="40_sinking_fund_replacement_cost_after_inflation",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Replacement cost grows with inflation: A = P(1 + i_inf)^n.",
            "concept": "Apply compound growth using the inflation rate.",
            "breakdown": f"Cost = {p_val}(1 + {i_dec})^{n_years} = R {round(a_rep, 2):.2f}.",
        },
        misconception_tags=["confused_replacement_inflation_with_depreciation"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 41: Sinking Fund — Trade-in Scrap Value via Reducing-Balance
def arch_41_sinking_fund_trade_in_value_reducing_balance(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    asset = r.choice(ASSETS)
    p_val = r.randint(25, 70) * 10000
    n_years = r.randint(4, 6)
    dep_pct = r.choice([15, 18, 20, 22])
    d_dec = dep_pct / 100.0

    scrap = p_val * ((1.0 - d_dec) ** n_years)
    p_str = num(p_val)
    dep_str = num(dep_pct)
    ans_str = num(round(scrap, 2), 2)

    prompt = (
        f"A firm purchased a new {asset} for R {p_str}. "
        f"The {asset} depreciates at {dep_str}% per annum on the reducing-balance method. "
        f"Determine the trade-in (scrap) value of this {asset} after {n_years} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{asset} cost R }}{p_str}\text{{. Reducing-balance depreciation = }}{dep_str}\% \text{{ p.a. over }}{n_years} "
        rf"\text{{ years. Calculate trade-in value.}} "
    )

    steps = [
        step(from_latex=r"A = P(1 - i)^n", to_latex_str=rf"A = {p_str}(1 - {num(d_dec)})^{{{n_years}}}", op="substitute into reducing-balance depreciation formula", rule="reducing-balance formula",),
        step(from_latex=rf"A = {p_str}({num(round(1.0 - d_dec, 4))})^{{{n_years}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate residual trade-in value", rule="arithmetic calculation",),
    ]
    canonical = solution_graph(
        goal=f"calculate trade-in value using reducing-balance depreciation",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 - i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution P={p_str}, i={dep_str}%, n={n_years}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate trade-in value R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_41",
        topic=TOPIC_NAME,
        subskill="41_sinking_fund_trade_in_value_reducing_balance",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "The trade-in value of the old asset is its depreciated book value: A = P(1 - i)^n.",
            "concept": "Reducing-balance depreciation uses (1 - i)^n.",
            "breakdown": f"Trade-in = {p_val}(1 - {d_dec})^{n_years} = R {round(scrap, 2):.2f}.",
        },
        misconception_tags=["used_straight_line_instead_of_reducing_balance"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 42: Sinking Fund — Net Replacement Shortfall
def arch_42_sinking_fund_net_replacement_shortfall(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    asset = r.choice(ASSETS)
    p_val = r.randint(25, 60) * 10000
    n_years = 5
    inf_pct = 7.0
    dep_pct = 18.0
    i_inf = inf_pct / 100.0
    d_dep = dep_pct / 100.0

    rep_cost = p_val * ((1.0 + i_inf) ** n_years)
    trade_in = p_val * ((1.0 - d_dep) ** n_years)
    shortfall = rep_cost - trade_in

    p_str = num(p_val)
    rep_str = num(round(rep_cost, 2), 2)
    trade_str = num(round(trade_in, 2), 2)
    ans_str = num(round(shortfall, 2), 2)

    prompt = (
        f"A firm bought a {asset} for R {p_str} and intends to replace it in {n_years} years' time.\n"
        f"- The replacement cost increases at {num(inf_pct)}% per annum due to inflation.\n"
        f"- The old {asset} depreciates at {num(dep_pct)}% per annum on the reducing-balance method, "
        f"and will be traded in when the new equipment is purchased.\n\n"
        f"Calculate the net amount (shortfall) the firm will need to fund the replacement in {n_years} years. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{asset} cost R }}{p_str}\text{{. Inflation = }}{num(inf_pct)}\%\text{{, depreciation = }}{num(dep_pct)}\% "
        rf"\text{{ reducing-balance (}}{n_years}\text{{ years). Find Net Shortfall = Replacement Cost - Trade-in.}} "
    )

    steps = [
        step(from_latex=r"\text{Replacement Cost} = P(1 + i_{\text{inf}})^n", to_latex_str=rf"\text{{Replacement Cost}} = {p_str}(1 + {num(i_inf)})^{{{n_years}}} = \text{{R }} {rep_str}", op="calculate inflated replacement cost", rule="inflation growth formula",),
        step(from_latex=r"\text{Trade-in Value} = P(1 - d)^n", to_latex_str=rf"\text{{Trade-in Value}} = {p_str}(1 - {num(d_dep)})^{{{n_years}}} = \text{{R }} {trade_str}", op="calculate depreciated trade-in scrap value", rule="reducing-balance depreciation formula",),
        step(from_latex=r"\text{Shortfall} = \text{Replacement Cost} - \text{Trade-in Value}", to_latex_str=rf"\text{{R }} {rep_str} - \text{{R }} {trade_str} = \text{{R }} {ans_str}", op="subtract trade-in value from replacement cost to find net sinking fund target", rule="subtraction",),
    ]
    canonical = solution_graph(
        goal=f"calculate net replacement shortfall for sinking fund",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Replacement cost calculation R {rep_str}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Trade-in value calculation R {trade_str}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Accurate net shortfall R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_42",
        topic=TOPIC_NAME,
        subskill="42_sinking_fund_net_replacement_shortfall",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Net shortfall = Future Replacement Cost - Future Trade-in Value.",
            "concept": "Calculate Replacement Cost = P(1 + i_inf)^n and Trade-in = P(1 - d)^n, then subtract.",
            "breakdown": f"Replacement = R {rep_cost:.2f}, Trade-in = R {trade_in:.2f}, Net Shortfall = R {shortfall:.2f}.",
        },
        misconception_tags=["added_trade_in_instead_of_subtracting"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=6,
    )


# Archetype 43: Demographic / Population Growth Model
def arch_43_population_growth_exponential_model(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    town = r.choice(["Polokwane", "Nelspruit", "Rustenburg", "George", "Mthatha"])
    p_val = r.randint(8, 25) * 10000
    n_years = r.randint(5, 10)
    rate_pct = r.choice([2.5, 3.0, 3.5, 4.0])
    i_dec = rate_pct / 100.0

    a_val = p_val * ((1.0 + i_dec) ** n_years)
    p_str = num(p_val)
    rate_str = num(rate_pct)
    ans_int = int(round(a_val))
    ans_str = num(ans_int)

    prompt = (
        f"The population of {town} is currently {p_str}. "
        f"If the population grows at a steady rate of {rate_str}% per annum, "
        f"calculate the estimated population in {n_years} years' time. "
        f"Round off your answer to the nearest whole number."
    )
    prompt_latex = (
        rf"\text{{Population }} P = {p_str}\text{{, growth rate }} r = {rate_str}\% \text{{ p.a. over }} {n_years} "
        rf"\text{{ years. Estimate future population (whole number).}}"
    )

    steps = [
        step(from_latex=r"A = P(1 + i)^n", to_latex_str=rf"A = {p_str}(1 + {num(i_dec)})^{{{n_years}}}", op="substitute known demographic values into compound growth formula", rule="compound demographic growth formula",),
        step(from_latex=rf"A = {p_str}({num(round(1.0 + i_dec, 4))})^{{{n_years}}}", to_latex_str=rf"{ans_str}\text{{ people}}", op="evaluate power and round to nearest integer", rule="arithmetic rounding",),
    ]
    canonical = solution_graph(
        goal=f"calculate projected population after exponential growth",
        steps=steps,
        final_latex=rf"{ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 + i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution P={p_str}, i={rate_str}%, n={n_years}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate population {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_43",
        topic=TOPIC_NAME,
        subskill="43_population_growth_exponential_model",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}",
        sample_answer=rf"{ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Population growth follows the compound growth formula: A = P(1 + i)^n.",
            "concept": "Substitute initial population as P and annual percentage growth as i.",
            "breakdown": f"A = {p_val}(1 + {i_dec})^{n_years} = {ans_int}.",
        },
        misconception_tags=["rounded_to_cents_instead_of_whole_people"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 44: Population / Resource Depletion Decay Model
def arch_44_population_decay_depletion_model(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    species = r.choice(["rhino population in a reserve", "fish stock in a lake", "ore reserve in a mine"])
    p_val = r.randint(10, 30) * 1000
    n_years = r.randint(4, 8)
    decay_pct = r.choice([6, 7.5, 8, 10])
    d_dec = decay_pct / 100.0

    a_val = p_val * ((1.0 - d_dec) ** n_years)
    p_str = num(p_val)
    decay_str = num(decay_pct)
    ans_int = int(round(a_val))
    ans_str = num(ans_int)

    prompt = (
        f"A conservation study estimates that the {species} is currently {p_str}. "
        f"Due to environmental pressures, the number is decreasing at a rate of {decay_str}% per annum on a compound basis. "
        f"Estimate the remaining number after {n_years} years. "
        f"Round off your answer to the nearest integer."
    )
    prompt_latex = (
        rf"\text{{{species}: initial }} P = {p_str}\text{{, annual decay rate }} d = {decay_str}\% \text{{ over }} "
        rf"{n_years}\text{{ years. Estimate remaining count.}}"
    )

    steps = [
        step(from_latex=r"A = P(1 - i)^n", to_latex_str=rf"A = {p_str}(1 - {num(d_dec)})^{{{n_years}}}", op="substitute into reducing-balance decay formula", rule="compound decay formula",),
        step(from_latex=rf"A = {p_str}({num(round(1.0 - d_dec, 4))})^{{{n_years}}}", to_latex_str=rf"{ans_str}", op="evaluate power and round to integer", rule="arithmetic rounding",),
    ]
    canonical = solution_graph(
        goal=f"calculate remaining population or resource after compound decay",
        steps=steps,
        final_latex=rf"{ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula quote A = P(1 - i)^n", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct substitution P={p_str}, i={decay_str}%, n={n_years}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate remaining count {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_44",
        topic=TOPIC_NAME,
        subskill="44_population_decay_depletion_model",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}",
        sample_answer=rf"{ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Natural decay and resource depletion use A = P(1 - i)^n.",
            "concept": "Substitute initial count as P and annual decay rate as i.",
            "breakdown": f"A = {p_val}(1 - {d_dec})^{n_years} = {ans_int}.",
        },
        misconception_tags=["used_addition_instead_of_subtraction_for_decay"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 45: Hire Purchase — Deposit, Interest & Monthly Instalments
def arch_45_hire_purchase_simple_interest_repayment(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(["lounge suite", "high-end laptop", "refrigerator", "smart television set"])
    cash_price = r.randint(12, 35) * 1000
    dep_pct = r.choice([10, 15, 20])
    n_years = r.randint(2, 4)
    rate_pct = r.choice([12, 14, 15, 18])

    dep_val = cash_price * (dep_pct / 100.0)
    loan_p = cash_price - dep_val
    interest_rate_dec = rate_pct / 100.0
    total_repay = loan_p * (1.0 + interest_rate_dec * n_years)
    months = n_years * 12
    monthly_inst = round(total_repay / months, 2)

    cp_str = num(cash_price)
    dep_str = num(dep_pct)
    rate_str = num(rate_pct)
    inst_str = num(monthly_inst, 2)

    prompt = (
        f"{name} buys a {asset} on hire purchase. The cash price is R {cp_str}.\n"
        f"- {name} pays a {dep_str}% cash deposit upfront.\n"
        f"- The balance is financed at a simple interest rate of {rate_str}% per annum over {n_years} years.\n\n"
        f"Calculate {name}'s monthly instalment. Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{Hire purchase: Cash = R }}{cp_str}\text{{, deposit = }}{dep_str}\%\text{{, simple interest = }} "
        rf"{rate_str}\% \text{{ p.a. over }}{n_years}\text{{ years. Find monthly instalment.}}"
    )

    steps = [
        step(from_latex=r"\text{Deposit} = \text{Cash Price} \times \text{Deposit } \%", to_latex_str=rf"\text{{Deposit}} = {cp_str} \times \frac{{{dep_str}}}{{100}} = \text{{R }} {num(dep_val)}", op="calculate initial deposit", rule="percentage calculation",),
        step(from_latex=r"P = \text{Cash Price} - \text{Deposit}", to_latex_str=rf"P = {cp_str} - {num(dep_val)} = \text{{R }} {num(loan_p)}", op="calculate loan principal remaining after deposit", rule="subtraction",),
        step(from_latex=r"A = P(1 + in)", to_latex_str=rf"A = {num(loan_p)}\left(1 + \frac{{{rate_str}}}{{100}} \times {n_years}\right) = \text{{R }} {num(round(total_repay, 2), 2)}", op="calculate total hire purchase repayment with simple interest", rule="hire purchase simple interest formula",),
        step(from_latex=rf"\text{{Monthly Instalment}} = \frac{{A}}{{{months}}}", to_latex_str=rf"\text{{R }} {inst_str}", op="divide total repayment by number of months", rule="instalment division",),
    ]
    canonical = solution_graph(
        goal=f"calculate monthly hire purchase instalment",
        steps=steps,
        final_latex=rf"\text{{R }} {inst_str}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Deposit and balance calculation P = R {num(loan_p)}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Total repayment using A = P(1 + in) = R {num(round(total_repay, 2), 2)}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Accurate monthly instalment R {inst_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_45",
        topic=TOPIC_NAME,
        subskill="45_hire_purchase_simple_interest_repayment",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {inst_str}",
        sample_answer=rf"R {inst_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Hire purchase ALWAYS uses simple interest (A = P(1 + in)) on the balance AFTER the deposit is deducted.",
            "concept": "Deposit = Cash x deposit%. Loan P = Cash - Deposit. Total A = P(1 + in). Monthly = A / (12n).",
            "breakdown": f"Deposit = R {dep_val}. Loan P = R {loan_p}. Total A = R {total_repay:.2f}. Monthly = R {monthly_inst:.2f}.",
        },
        misconception_tags=["applied_compound_interest_to_hire_purchase", "charged_interest_on_full_cash_price_ignoring_deposit"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 46: Hire Purchase — Total Cost & Insurance
def arch_46_hire_purchase_total_cost_and_insurance(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(["solar power inverter system", "commercial espresso machine", "commercial trailer"])
    cash_price = r.randint(20, 50) * 1000
    dep_pct = 15
    n_years = 3
    rate_pct = 14.0
    monthly_insurance = r.randint(35, 75) * 10

    dep_val = cash_price * 0.15
    loan_p = cash_price - dep_val
    interest_amt = loan_p * (rate_pct / 100.0) * n_years
    total_finance = loan_p + interest_amt
    months = n_years * 12
    base_monthly = total_finance / months
    total_monthly = round(base_monthly + monthly_insurance, 2)
    grand_total_cost = dep_val + total_monthly * months

    cp_str = num(cash_price)
    ins_str = num(monthly_insurance)
    ans_str = num(round(grand_total_cost, 2), 2)

    prompt = (
        f"{name} buys a {asset} with a cash price of R {cp_str} on hire purchase:\n"
        f"- A deposit of {dep_pct}% is paid.\n"
        f"- Simple interest of {num(rate_pct)}% p.a. is charged on the balance over {n_years} years.\n"
        f"- Mandatory monthly insurance of R {ins_str} is added to each monthly repayment.\n\n"
        f"Calculate the total actual cost {name} will pay for the {asset} by the end of the agreement. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{Hire purchase with insurance: Cash R }}{cp_str}\text{{, deposit 15\%, rate 14\% simple for 3 years, }} "
        rf"\text{{insurance R }}{ins_str}\text{{/month. Find total actual cost paid.}} "
    )

    steps = [
        step(from_latex=r"P = \text{Cash} - \text{Deposit}", to_latex_str=rf"P = {cp_str} - {num(dep_val)} = \text{{R }} {num(loan_p)}", op="deduct deposit to find principal", rule="subtraction",),
        step(from_latex=r"A = P(1 + in)", to_latex_str=rf"A = {num(loan_p)}(1 + 0{{,}}14 \times 3) = \text{{R }} {num(round(total_finance, 2), 2)}", op="calculate finance total", rule="simple interest formula",),
        step(from_latex=rf"\text{{Monthly Payment}} = \frac{{{num(round(total_finance, 2), 2)}}}{{36}} + \text{{R }} {ins_str}", to_latex_str=rf"\text{{R }} {num(round(base_monthly, 2), 2)} + \text{{R }} {ins_str} = \text{{R }} {num(total_monthly, 2)}", op="add monthly insurance to monthly instalment", rule="addition",),
        step(from_latex=rf"\text{{Total Cost}} = \text{{Deposit}} + 36 \times \text{{Total Monthly}}", to_latex_str=rf"\text{{R }} {ans_str}", op="sum deposit and all 36 monthly payments", rule="grand total calculation",),
    ]
    canonical = solution_graph(
        goal=f"calculate total cost of hire purchase agreement including insurance",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Loan balance P = R {num(loan_p)}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Finance amount A = R {num(round(total_finance, 2), 2)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Total monthly payment including insurance R {num(total_monthly, 2)}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Summing deposit and all monthly instalments", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Accurate total cost R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_46",
        topic=TOPIC_NAME,
        subskill="46_hire_purchase_total_cost_and_insurance",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Total cost = Deposit + (Number of months x Total monthly instalment).",
            "concept": "Total monthly instalment = (Loan P x (1 + in) / 36) + Monthly insurance.",
            "breakdown": f"Deposit = R {dep_val}. Total monthly = R {total_monthly:.2f}. Total cost = R {grand_total_cost:.2f}.",
        },
        misconception_tags=["forgot_to_include_upfront_deposit_in_total_cost"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=6,
    )


# Archetype 47: Misconception Drill — Simple vs Compound Decay Choice
def arch_47_spot_misconception_simple_vs_compound_decay(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    asset = r.choice(ASSETS)
    p_val = r.choice([80000, 100000, 120000, 150000])
    n_years = r.choice([4, 5, 6])
    rate_pct = r.choice([12, 14, 15, 18, 20])
    i_dec = rate_pct / 100.0

    sl_ans = p_val * (1.0 - i_dec * n_years)
    rb_ans = p_val * ((1.0 - i_dec) ** n_years)

    p_str = num(p_val)
    rate_str = num(rate_pct)
    sl_str = num(round(sl_ans))

    prompt = (
        f"{name} attempted to calculate the book value of a {asset} purchased for R {p_str} after {n_years} years, "
        f"depreciating at {rate_str}% p.a. on a reducing-balance basis. "
        f"{name}'s working was:\n"
        f"$$A = {p_str}(1 - {num(i_dec, 2)} \\times {n_years}) = \\text{{R }} {sl_str}$$\n\n"
        f"Explain why {name}'s solution is mathematically incorrect and calculate the correct book value to the nearest Rand."
    )
    prompt_latex = (
        r"\text{Identify error in using } A = P(1 - in) \text{ instead of } A = P(1 - i)^n \text{ and calculate correct } A."
    )

    ans_str = num(round(rb_ans))
    factor_str = num(round(1.0 - i_dec, 2), 2)
    explanation = (
        f"{name} incorrectly applied the straight-line (simple decay) formula $A = P(1 - in)$ instead of the "
        f"reducing-balance (compound decay) formula $A = P(1 - i)^n$.\n"
        f"Correct calculation: $A = {p_str}(1 - {num(i_dec, 2)})^{n_years} = {p_str}({factor_str})^{n_years} \\approx \\text{{R }} {ans_str}$."
    )

    steps = [
        step(from_latex=r"A = P(1 - i)^n", to_latex_str=rf"A = {p_str}(1 - {num(i_dec, 2)})^{{{n_years}}} = {p_str}({factor_str})^{{{n_years}}}", op="apply correct reducing-balance formula", rule="reducing balance formula",),
        step(from_latex=rf"{p_str}({factor_str})^{{{n_years}}}", to_latex_str=rf"\text{{R }} {ans_str}", op="evaluate power and multiply", rule="power evaluation",),
    ]
    canonical = solution_graph(
        goal=f"identify formula misconception and calculate correct reducing balance value",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Identifies that straight-line formula was wrongly used instead of reducing balance", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Uses correct formula A = P(1 - i)^n", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate book value R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_47",
        topic=TOPIC_NAME,
        subskill="47_spot_misconception_simple_vs_compound_decay",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=explanation,
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Check the formula used: straight-line is (1 - in), while reducing-balance is (1 - i)^n.",
            "concept": "Reducing-balance depreciation must use the exponent n, not multiplication by n.",
            "breakdown": f"Correct A = {p_str} * ({factor_str})^{n_years} = R {ans_str}.",
        },
        misconception_tags=["used_straight_line_for_reducing_balance"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 48: Misconception Drill — Nominal to Effective Conversion Errors
def arch_48_spot_misconception_nominal_effective_formula(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    nom_pct = r.choice([9.6, 10.5, 12.0, 13.5, 14.4, 15.0, 16.0, 18.0])
    i_nom = nom_pct / 100.0
    m = 12
    growth_val = (1.0 + i_nom / m) ** m
    growth_round = round(growth_val, 4)
    growth_str = num(growth_round, 4)
    growth_pct_str = num(round(growth_round * 100.0, 2), 2)
    correct_eff = (growth_val - 1.0) * 100.0

    nom_str = num(nom_pct, 1 if nom_pct % 1 != 0 else 0)
    ans_str = num(round(correct_eff, 2), 2)

    prompt = (
        f"A learner was asked to calculate the effective annual interest rate for a nominal rate of {nom_str}% p.a. "
        f"compounded monthly. The learner wrote:\n"
        f"$$i_{{\\text{{eff}}}} = \\left(1 + \\frac{{{num(i_nom, 4)}}}{{12}}\\right)^{{12}} = {growth_str} = {growth_pct_str}\\%$$\n\n"
        f"State the error in the learner's method and provide the correct effective annual rate (to 2 decimal places)."
    )
    prompt_latex = (
        r"\text{Identify the error where learner forgot to subtract 1 from } (1 + i/m)^m \text{ and state correct rate.}"
    )

    explanation = (
        f"The learner forgot to subtract 1 at the end of the formula: $i_{{\\text{{eff}}}} = \\left(1 + \\frac{{i_{{\\text{{nom}}}}}}{{m}}\\right)^m - 1$.\n"
        f"The value ${growth_str}$ represents the total growth factor $1 + i_{{\\text{{eff}}}}$.\n"
        f"The correct effective rate is ${growth_str} - 1 = {num(round(growth_round - 1.0, 4), 4)} \\approx {ans_str}\\%$."
    )

    steps = [
        step(from_latex=r"i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{12}\right)^{12} - 1", to_latex_str=rf"i_{{\text{{eff}}}} = (1 + {num(i_nom/12, 4)})^{{12}} - 1 = {growth_str} - 1", op="subtract 1 from growth factor", rule="effective rate definition",),
        step(from_latex=rf"{growth_str} - 1", to_latex_str=rf"{ans_str}\%", op="convert decimal to percentage", rule="percentage conversion",),
    ]
    canonical = solution_graph(
        goal=f"identify omission of subtracting 1 and state correct effective rate",
        steps=steps,
        final_latex=rf"{ans_str}\%",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Explains that the learner omitted subtracting 1 (gave 1 + i_eff instead of i_eff)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Applies correct formula subtracting 1", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate rate {ans_str}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_48",
        topic=TOPIC_NAME,
        subskill="48_spot_misconception_nominal_effective_formula",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{ans_str}\%",
        sample_answer=explanation,
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "The growth factor is 1 + i_eff. To get the interest rate alone, you MUST subtract 1.",
            "concept": "1 + i_eff = 1.1268 -> i_eff = 1.1268 - 1 = 0.1268 = 12.68%.",
            "breakdown": f"Correct effective rate = {round(correct_eff, 2)}%.",
        },
        misconception_tags=["forgot_to_subtract_one_for_effective_rate"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 49: Capstone — Timeline with Rate Change and Withdrawal
def arch_49_capstone_timeline_rate_change_and_withdrawal(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    p_val = r.randint(20, 45) * 5000
    with_val = r.randint(5, 12) * 2000
    n1 = 2  # Rate 1 for 2 years
    n2 = 3  # Rate 2 for 3 years
    total_n = 5

    r1_pct = 9.0   # compounded monthly
    r2_pct = 11.4  # compounded monthly
    i1 = (r1_pct / 100.0) / 12.0
    i2 = (r2_pct / 100.0) / 12.0

    # Withdrawal takes place at T2 (exact moment of rate change)
    bal_t2_pre = p_val * ((1.0 + i1) ** 24)
    bal_t2_post = bal_t2_pre - with_val
    a_final = bal_t2_post * ((1.0 + i2) ** 36)

    p_str = num(p_val)
    with_str = num(with_val)
    ans_str = num(round(a_final, 2), 2)

    diag_svg = timeline_svg(
        total_years=total_n,
        intervals=[(0, n1, f"{num(r1_pct)}% monthly"), (n1, total_n, f"{num(r2_pct)}% monthly")],
        cash_flows=[(0, f"R {p_str}", "initial"), (n1, f"R {with_str}", "withdrawal")],
        title=f"{name}'s Capstone Timeline (Withdrawal at T{n1})",
    )
    diagram_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Capstone Timeline Diagram", "diagram_role": "context"}

    prompt = (
        f"{name} invested R {p_str} in a fixed deposit account for 5 years.\n"
        f"- For the first 2 years, the interest rate was {num(r1_pct)}% p.a. compounded monthly.\n"
        f"- At the end of year 2, {name} withdrew R {with_str}.\n"
        f"- At the same time (end of year 2), the bank changed the interest rate to {num(r2_pct)}% p.a. compounded monthly "
        f"for the remaining 3 years.\n\n"
        f"Calculate the accumulated balance in the account at the end of the 5-year investment period. "
        f"Round off your answer to TWO decimal places."
    )
    prompt_latex = (
        rf"\text{{{name}: R }}{p_str}\text{{ for 2y at 9\% monthly, -R }}{with_str}\text{{ at }} T_2\text{{, then 11{{,}}4\% }} "
        rf"\text{{monthly for 3y. Calculate balance at }} T_5."
    )

    steps = [
        step(from_latex=r"A_{T2} = P\left(1 + \frac{i_1}{12}\right)^{24} - W", to_latex_str=rf"A_{{T2}} = {p_str}(1 + {num(i1)})^{{24}} - {with_str} = \text{{R }} {num(round(bal_t2_post, 2), 2)}", op="grow initial deposit to T2 and deduct withdrawal", rule="first stage compound growth and withdrawal",),
        step(from_latex=r"A_{T5} = A_{T2}\left(1 + \frac{i_2}{12}\right)^{36}", to_latex_str=rf"A_{{T5}} = {num(round(bal_t2_post, 2), 2)}(1 + {num(i2)})^{{36}} = \text{{R }} {ans_str}", op="grow net balance at T2 through second phase to T5", rule="second stage compound growth",),
    ]
    canonical = solution_graph(
        goal=f"calculate capstone timeline balance with rate change and simultaneous withdrawal",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Compounding P at 9% monthly for 24 months", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Subtracting withdrawal at T2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Compounding remaining balance at 11.4% monthly for 36 months", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Accurate final balance R {ans_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_49",
        topic=TOPIC_NAME,
        subskill="49_capstone_timeline_rate_change_and_withdrawal",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diagram_spec,
        hints={
            "nudge": "Step 1: Find balance at T2 before withdrawal. Step 2: Deduct R W. Step 3: Grow remaining balance at second rate to T5.",
            "concept": "A = [P(1 + i1/12)^24 - W] * (1 + i2/12)^36.",
            "breakdown": f"Bal at T2 pre = R {bal_t2_pre:.2f}. Post withdrawal = R {bal_t2_post:.2f}. Final at T5 = R {a_final:.2f}.",
        },
        misconception_tags=["applied_first_rate_to_entire_5_years"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=7,
    )


# Archetype 50: Capstone — Sinking Fund Full-Cycle Exam Question
def arch_50_capstone_sinking_fund_full_cycle_exam_question(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    asset = r.choice(ASSETS)
    p_val = r.randint(30, 70) * 10000
    n_years = 5
    inf_pct = 7.5
    dep_pct = 20.0
    fund_rate_pct = 9.6

    i_inf = inf_pct / 100.0
    d_dep = dep_pct / 100.0
    i_fund = (fund_rate_pct / 100.0) / 12.0

    rep_cost = p_val * ((1.0 + i_inf) ** n_years)
    trade_in = p_val * ((1.0 - d_dep) ** n_years)
    shortfall = rep_cost - trade_in

    # Lump sum needed today to fund this shortfall in 5 years with fund_rate monthly
    p_fund = shortfall / ((1.0 + i_fund) ** (n_years * 12))

    p_str = num(p_val)
    rep_str = num(round(rep_cost, 2), 2)
    trade_str = num(round(trade_in, 2), 2)
    short_str = num(round(shortfall, 2), 2)
    ans_str = num(round(p_fund, 2), 2)

    prompt = (
        f"A manufacturing company bought a new {asset} for R {p_str}.\n"
        f"The company plans to replace this machine at the end of {n_years} years.\n"
        f"- The cost of a new {asset} is expected to inflate at {num(inf_pct)}% per annum.\n"
        f"- The current {asset} will depreciate at {num(dep_pct)}% per annum on the reducing-balance method, "
        f"and will be traded in at book value when the new machine is purchased.\n"
        f"- The company opens a sinking fund today earning {num(fund_rate_pct)}% p.a. compounded monthly to cover the shortfall.\n\n"
        f"Calculate the single lump sum the company must deposit into the sinking fund today to fully fund the replacement in {n_years} years. "
        f"Round off your answer to the nearest Rand."
    )
    prompt_latex = (
        rf"\text{{{asset}: Cost R }}{p_str}\text{{. Inflation }}{num(inf_pct)}\%\text{{, depreciation }}{num(dep_pct)}\% "
        rf"\text{{ reducing balance. Sinking fund earns }}{num(fund_rate_pct)}\%\text{{ monthly over 5y. Find lump sum today.}} "
    )

    steps = [
        step(from_latex=r"\text{Replacement Cost} = P(1 + i_{\text{inf}})^n", to_latex_str=rf"\text{{Replacement Cost}} = {p_str}(1 + {num(i_inf)})^5 = \text{{R }} {rep_str}", op="calculate inflated replacement cost", rule="inflation formula",),
        step(from_latex=r"\text{Trade-in Value} = P(1 - d)^n", to_latex_str=rf"\text{{Trade-in Value}} = {p_str}(1 - {num(d_dep)})^5 = \text{{R }} {trade_str}", op="calculate depreciated trade-in value", rule="reducing balance formula",),
        step(from_latex=r"\text{Shortfall} = \text{Replacement Cost} - \text{Trade-in Value}", to_latex_str=rf"\text{{Shortfall}} = \text{{R }} {rep_str} - \text{{R }} {trade_str} = \text{{R }} {short_str}", op="calculate net shortfall to be funded", rule="subtraction",),
        step(from_latex=r"P_{\text{fund}} = \frac{\text{Shortfall}}{\left(1 + \frac{i_{\text{fund}}}{12}\right)^{60}}", to_latex_str=rf"P_{{\text{{fund}}}} = \frac{{{short_str}}}{{(1 + {num(i_fund)})^{{60}}}} = \text{{R }} {ans_str}", op="calculate present lump sum required to accumulate shortfall", rule="present value formula with monthly compounding",),
    ]
    canonical = solution_graph(
        goal=f"calculate full-cycle sinking fund lump sum requirement",
        steps=steps,
        final_latex=rf"\text{{R }} {ans_str}",
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": f"Replacement cost calculation R {rep_str}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Trade-in value calculation R {trade_str}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Net shortfall R {short_str}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Lump sum required today R {ans_str}", "marks": 2, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_fin_50",
        topic=TOPIC_NAME,
        subskill="50_capstone_sinking_fund_full_cycle_exam_question",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{R }} {ans_str}",
        sample_answer=rf"R {ans_str}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Step 1: Replacement cost (inflation). Step 2: Trade-in value (reducing balance). Step 3: Shortfall = Replacement - Trade-in. Step 4: P = Shortfall / (1 + i/12)^60.",
            "concept": "Full exam cycle: combine inflation, reducing-balance depreciation, and monthly compound growth discounting.",
            "breakdown": f"Replacement = R {rep_cost:.2f}, Trade-in = R {trade_in:.2f}, Shortfall = R {shortfall:.2f}, Lump sum = R {p_fund:.2f}.",
        },
        misconception_tags=["omitted_trade_in_value_from_sinking_fund_calculation"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=8,
    )


ARCHETYPE_BUILDERS_26_50: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "26_nominal_rate_from_effective_annual_rate": arch_26_nominal_rate_from_effective_annual_rate,
    "27_compare_two_bank_offers_via_effective_rates": arch_27_compare_two_bank_offers_via_effective_rates,
    "28_timeline_single_interest_rate_change": arch_28_timeline_single_interest_rate_change,
    "29_timeline_two_interest_rate_changes": arch_29_timeline_two_interest_rate_changes,
    "30_timeline_single_additional_deposit": arch_30_timeline_single_additional_deposit,
    "31_timeline_single_withdrawal": arch_31_timeline_single_withdrawal,
    "32_timeline_deposit_and_withdrawal_combined": arch_32_timeline_deposit_and_withdrawal_combined,
    "33_timeline_two_deposits_different_rates": arch_33_timeline_two_deposits_different_rates,
    "34_timeline_two_withdrawals": arch_34_timeline_two_withdrawals,
    "35_timeline_solve_initial_deposit_given_final_amount": arch_35_timeline_solve_initial_deposit_given_final_amount,
    "36_timeline_solve_additional_deposit_to_meet_target": arch_36_timeline_solve_additional_deposit_to_meet_target,
    "37_timeline_solve_withdrawal_amount": arch_37_timeline_solve_withdrawal_amount,
    "38_inflation_future_cost_of_goods": arch_38_inflation_future_cost_of_goods,
    "39_inflation_purchasing_power_depreciation": arch_39_inflation_purchasing_power_depreciation,
    "40_sinking_fund_replacement_cost_after_inflation": arch_40_sinking_fund_replacement_cost_after_inflation,
    "41_sinking_fund_trade_in_value_reducing_balance": arch_41_sinking_fund_trade_in_value_reducing_balance,
    "42_sinking_fund_net_replacement_shortfall": arch_42_sinking_fund_net_replacement_shortfall,
    "43_population_growth_exponential_model": arch_43_population_growth_exponential_model,
    "44_population_decay_depletion_model": arch_44_population_decay_depletion_model,
    "45_hire_purchase_simple_interest_repayment": arch_45_hire_purchase_simple_interest_repayment,
    "46_hire_purchase_total_cost_and_insurance": arch_46_hire_purchase_total_cost_and_insurance,
    "47_spot_misconception_simple_vs_compound_decay": arch_47_spot_misconception_simple_vs_compound_decay,
    "48_spot_misconception_nominal_effective_formula": arch_48_spot_misconception_nominal_effective_formula,
    "49_capstone_timeline_rate_change_and_withdrawal": arch_49_capstone_timeline_rate_change_and_withdrawal,
    "50_capstone_sinking_fund_full_cycle_exam_question": arch_50_capstone_sinking_fund_full_cycle_exam_question,
}
