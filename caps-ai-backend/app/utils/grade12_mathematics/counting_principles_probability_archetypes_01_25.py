"""Grade 12 Mathematics — Probability Archetypes 01 to 25.
Grounded in curriculum_docs_auto/Mathematics_Gr12/Term 3/02. Probability.md:
Probability identities, addition rule, complementary rule, mutually exclusive vs exhaustive events,
independent vs dependent events, 2-set & 3-set Venn diagrams (inline SVG), tree diagrams (inline SVG),
and two-way contingency tables.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade12_mathematics._math_common import (
    make_math_question,
    num,
    solution_graph,
    step,
    to_latex,
)

TOPIC = "grade12_math_counting_probability"
LO_PREFIX = "math12_probability"


# ---------------------------------------------------------------------------
# SVG Builders (Surface 1: Static 2D Exam Figures)
# ---------------------------------------------------------------------------
def _venn_2_sets_svg(only_a: str, inter: str, only_b: str, outside: str, total_label: str) -> Dict[str, Any]:
    w, h = 420, 220
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect x="10" y="10" width="400" height="200" fill="#ffffff" stroke="#334155" stroke-width="2" rx="6"/>'
        f'<text x="25" y="32" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">S ({total_label})</text>'
        f'<circle cx="165" cy="115" r="68" fill="#bae6fd" fill-opacity="0.45" stroke="#0284c7" stroke-width="2"/>'
        f'<circle cx="255" cy="115" r="68" fill="#fecdd3" fill-opacity="0.45" stroke="#e11d48" stroke-width="2"/>'
        f'<text x="125" y="65" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0369a1">A</text>'
        f'<text x="295" y="65" font-family="sans-serif" font-size="12" font-weight="bold" fill="#be123c">B</text>'
        f'<text x="130" y="120" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{only_a}</text>'
        f'<text x="210" y="120" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{inter}</text>'
        f'<text x="290" y="120" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{only_b}</text>'
        f'<text x="370" y="190" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#475569">{outside}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _venn_3_sets_svg(
    only_r: str,
    only_s: str,
    only_c: str,
    rs_only: str,
    rc_only: str,
    sc_only: str,
    all_three: str,
    outside: str,
    title: str,
) -> Dict[str, Any]:
    w, h = 440, 260
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect x="8" y="8" width="424" height="244" fill="#ffffff" stroke="#334155" stroke-width="2" rx="6"/>'
        f'<text x="22" y="28" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">{title}</text>'
        f'<circle cx="175" cy="105" r="62" fill="#bae6fd" fill-opacity="0.4" stroke="#0284c7" stroke-width="2"/>'
        f'<circle cx="265" cy="105" r="62" fill="#bbf7d0" fill-opacity="0.4" stroke="#16a34a" stroke-width="2"/>'
        f'<circle cx="220" cy="170" r="62" fill="#fde68a" fill-opacity="0.4" stroke="#d97706" stroke-width="2"/>'
        f'<text x="125" y="60" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0369a1">R</text>'
        f'<text x="315" y="60" font-family="sans-serif" font-size="11" font-weight="bold" fill="#15803d">S</text>'
        f'<text x="220" y="242" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#b45309">C</text>'
        f'<text x="145" y="95" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{only_r}</text>'
        f'<text x="295" y="95" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{only_s}</text>'
        f'<text x="220" y="202" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{only_c}</text>'
        f'<text x="220" y="88" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{rs_only}</text>'
        f'<text x="182" y="150" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{rc_only}</text>'
        f'<text x="258" y="150" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{sc_only}</text>'
        f'<text x="220" y="128" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#dc2626">{all_three}</text>'
        f'<text x="390" y="232" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#475569">{outside}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _tree_2_stage_svg(p1_top: str, p1_bot: str, p2_tt: str, p2_tb: str, p2_bt: str, p2_bb: str, title: str) -> Dict[str, Any]:
    w, h = 440, 230
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect width="{w}" height="{h}" fill="#ffffff" rx="6"/>'
        f'<text x="220" y="20" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e293b">{title}</text>'
        f'<line x1="40" y1="120" x2="170" y2="65" stroke="#0284c7" stroke-width="2"/>'
        f'<line x1="40" y1="120" x2="170" y2="175" stroke="#0284c7" stroke-width="2"/>'
        f'<text x="100" y="82" font-family="sans-serif" font-size="11" fill="#0f172a">{p1_top}</text>'
        f'<text x="100" y="162" font-family="sans-serif" font-size="11" fill="#0f172a">{p1_bot}</text>'
        f'<text x="182" y="69" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0369a1">R</text>'
        f'<text x="182" y="179" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0369a1">B</text>'
        f'<line x1="195" y1="65" x2="330" y2="40" stroke="#16a34a" stroke-width="1.8"/>'
        f'<line x1="195" y1="65" x2="330" y2="90" stroke="#16a34a" stroke-width="1.8"/>'
        f'<line x1="195" y1="175" x2="330" y2="150" stroke="#16a34a" stroke-width="1.8"/>'
        f'<line x1="195" y1="175" x2="330" y2="200" stroke="#16a34a" stroke-width="1.8"/>'
        f'<text x="260" y="46" font-family="sans-serif" font-size="10" fill="#0f172a">{p2_tt}</text>'
        f'<text x="260" y="88" font-family="sans-serif" font-size="10" fill="#0f172a">{p2_tb}</text>'
        f'<text x="260" y="156" font-family="sans-serif" font-size="10" fill="#0f172a">{p2_bt}</text>'
        f'<text x="260" y="198" font-family="sans-serif" font-size="10" fill="#0f172a">{p2_bb}</text>'
        f'<text x="345" y="44" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">RR</text>'
        f'<text x="345" y="94" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">RB</text>'
        f'<text x="345" y="154" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">BR</text>'
        f'<text x="345" y="204" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">BB</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _make_p(
    subskill: str,
    prompt: str,
    prompt_latex: str,
    answer_latex: str,
    answer_sympy: str,
    sample_answer: str,
    marks: int = 3,
    difficulty: str = "medium",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    steps = [
        step(from_latex=prompt_latex, to_latex_str=answer_latex, op=f"compute {subskill}", rule=subskill),
    ]
    canonical = solution_graph(goal=subskill, steps=steps, final_latex=answer_latex)
    marking_schema = {
        "total_marks": marks,
        "marking_points": [
            {"id": "mp1", "desc": "Correct probability identity or setup", "marks": max(1, marks - 1), "editable": True},
            {"id": "mp2", "desc": f"Final answer: {answer_latex}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Apply the probability addition rule $P(A \\text{ or } B) = P(A) + P(B) - P(A \\text{ and } B)$ or product rule $P(A \\text{ and } B) = P(A) \\times P(B)$.",
        "concept": "Mutually exclusive means $P(A \\cap B) = 0$; independent means $P(A \\cap B) = P(A) \\times P(B)$.",
        "breakdown": sample_answer,
    }
    return make_math_question(
        prefix=f"prob12_{subskill[:12]}",
        topic=TOPIC,
        subskill=subskill,
        learning_objective_id=f"{LO_PREFIX}_{subskill}",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        answer_sympy=answer_sympy,
        sample_answer=sample_answer,
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_mutually_exclusive_with_independent", "added_probabilities_instead_of_multiplying"],
        keywords=["probability", subskill.replace("_", " ")],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=max(3, marks),
        mode=subskill,
        difficulty=difficulty,
        diagram_spec=diagram_spec,
    )


# ---------------------------------------------------------------------------
# Archetypes 01 to 25
# ---------------------------------------------------------------------------
def build_01_classical_probability_equally_likely_outcomes(r: random.Random) -> Dict[str, Any]:
    n_tot = r.choice([15, 18, 20, 24, 25])
    primes = [p for p in [2, 3, 5, 7, 11, 13, 17, 19, 23] if p <= n_tot]
    prob = sp.Rational(len(primes), n_tot)
    return _make_p(
        "01_classical_probability_equally_likely_outcomes",
        f"A sample space $S = \\{{1; 2; 3; ...; {n_tot}\\}}$ contains the first {n_tot} natural numbers. If one number is chosen at random, calculate the probability that it is a prime number.",
        rf"P(\text{{prime}}) = \frac{{{len(primes)}}}{{{n_tot}}}",
        to_latex(prob),
        str(prob),
        f"Primes in $S$ are $\\{{{'; '.join(str(p) for p in primes)}\\}}$, giving {len(primes)} outcomes. $P(\\text{{prime}}) = \\frac{{{len(primes)}}}{{{n_tot}}} = {to_latex(prob)}$.",
        marks=2,
        difficulty="easy",
    )


def build_02_complementary_event_rule(r: random.Random) -> Dict[str, Any]:
    pa = round(r.choice([0.18, 0.24, 0.32, 0.37, 0.43, 0.65]), 2)
    p_not = round(1.0 - pa, 2)
    pa_s, pn_s = num(pa, 2), num(p_not, 2)
    return _make_p(
        "02_complementary_event_rule",
        f"Given that the probability of event $A$ occurring is $P(A) = {pa_s}$, calculate $P(\\text{{not }} A)$.",
        rf"P(A') = 1 - {pa_s}",
        pn_s,
        pn_s,
        f"By the complementary rule, $P(\\text{{not }} A) = 1 - P(A) = 1 - {pa_s} = {pn_s}$.",
        marks=2,
        difficulty="easy",
    )


def build_03_addition_rule_union_of_two_events(r: random.Random) -> Dict[str, Any]:
    pa = r.choice([0.45, 0.50, 0.55, 0.60])
    pb = r.choice([0.35, 0.40, 0.45])
    pab = r.choice([0.15, 0.20, 0.25])
    pu = round(pa + pb - pab, 2)
    pa_s, pb_s, pab_s, pu_s = num(pa, 2), num(pb, 2), num(pab, 2), num(pu, 2)
    return _make_p(
        "03_addition_rule_union_of_two_events",
        f"For two events $A$ and $B$, $P(A) = {pa_s}$, $P(B) = {pb_s}$, and $P(A \\text{{ and }} B) = {pab_s}$. Calculate $P(A \\text{{ or }} B)$.",
        rf"P(A \cup B) = {pa_s} + {pb_s} - {pab_s}",
        pu_s,
        pu_s,
        f"$P(A \\text{{ or }} B) = P(A) + P(B) - P(A \\text{{ and }} B) = {pa_s} + {pb_s} - {pab_s} = {pu_s}$.",
        marks=2,
        difficulty="easy",
    )


def build_04_addition_rule_intersection_from_union(r: random.Random) -> Dict[str, Any]:
    pa = r.choice([0.50, 0.55, 0.60, 0.65])
    pb = r.choice([0.40, 0.45, 0.50])
    pu = round(pa + pb - r.choice([0.12, 0.18, 0.22]), 2)
    pab = round(pa + pb - pu, 2)
    pa_s, pb_s, pu_s, pab_s = num(pa, 2), num(pb, 2), num(pu, 2), num(pab, 2)
    return _make_p(
        "04_addition_rule_intersection_from_union",
        f"Given $P(A) = {pa_s}$, $P(B) = {pb_s}$, and $P(A \\text{{ or }} B) = {pu_s}$, calculate $P(A \\text{{ and }} B)$.",
        rf"P(A \cap B) = {pa_s} + {pb_s} - {pu_s}",
        pab_s,
        pab_s,
        f"$P(A \\text{{ and }} B) = P(A) + P(B) - P(A \\text{{ or }} B) = {pa_s} + {pb_s} - {pu_s} = {pab_s}$.",
        marks=2,
    )


def build_05_mutually_exclusive_events_test_and_union(r: random.Random) -> Dict[str, Any]:
    pa = r.choice([0.25, 0.30, 0.35, 0.40])
    pb = r.choice([0.35, 0.45, 0.50])
    pu = round(pa + pb, 2)
    pa_s, pb_s, pu_s = num(pa, 2), num(pb, 2), num(pu, 2)
    return _make_p(
        "05_mutually_exclusive_events_test_and_union",
        f"Events $A$ and $B$ are mutually exclusive with $P(A) = {pa_s}$ and $P(B) = {pb_s}$. Write down $P(A \\text{{ and }} B)$ and calculate $P(A \\text{{ or }} B)$.",
        rf"P(A \cap B) = 0, \quad P(A \cup B) = {pa_s} + {pb_s}",
        rf"P(A \text{{ and }} B) = 0; \quad P(A \text{{ or }} B) = {pu_s}",
        pu_s,
        f"Since $A$ and $B$ are mutually exclusive, $P(A \\text{{ and }} B) = 0$, and $P(A \\text{{ or }} B) = {pa_s} + {pb_s} = {pu_s}$.",
        marks=2,
        difficulty="easy",
    )


def build_06_exhaustive_events_sum_to_unity(r: random.Random) -> Dict[str, Any]:
    pa = r.choice([0.55, 0.60, 0.65, 0.70])
    pab = r.choice([0.15, 0.20, 0.25])
    pb = round(1.0 + pab - pa, 2)
    pa_s, pab_s, pb_s = num(pa, 2), num(pab, 2), num(pb, 2)
    return _make_p(
        "06_exhaustive_events_sum_to_unity",
        f"Events $A$ and $B$ are exhaustive events in a sample space $S$, with $P(A) = {pa_s}$ and $P(A \\text{{ and }} B) = {pab_s}$. Calculate $P(B)$.",
        rf"1 = {pa_s} + P(B) - {pab_s}",
        pb_s,
        pb_s,
        f"For exhaustive events, $P(A \\text{{ or }} B) = 1$. Thus $1 = {pa_s} + P(B) - {pab_s} \\implies P(B) = {pb_s}$.",
        marks=3,
    )


def build_07_complementary_events_mutually_exclusive_and_exhaustive(r: random.Random) -> Dict[str, Any]:
    pa = r.choice([0.35, 0.40, 0.45, 0.60, 0.65])
    pb = round(1.0 - pa, 2)
    pa_s, pb_s = num(pa, 2), num(pb, 2)
    return _make_p(
        "07_complementary_events_mutually_exclusive_and_exhaustive",
        f"Two events $A$ and $B$ satisfy $P(A) = {pa_s}$, $P(B) = {pb_s}$, and $P(A \\text{{ and }} B) = 0$. Prove that $A$ and $B$ are complementary events.",
        rf"P(A \cap B) = 0 \text{{ and }} P(A) + P(B) = {pa_s} + {pb_s} = 1",
        r"\text{Complementary: mutually exclusive } (P(A\cap B)=0) \text{ and exhaustive } (P(A\cup B)=1)",
        "complementary",
        f"Since $P(A \\text{{ and }} B) = 0$, the events are mutually exclusive. Since $P(A \\text{{ or }} B) = {pa_s} + {pb_s} = 1$, they are exhaustive. Therefore $A$ and $B$ are complementary.",
        marks=2,
    )


def build_08_independent_events_product_rule_calculation(r: random.Random) -> Dict[str, Any]:
    pa = r.choice([0.4, 0.5, 0.6, 0.7])
    pb = r.choice([0.3, 0.4, 0.5])
    pab = round(pa * pb, 2)
    pu = round(pa + pb - pab, 2)
    pa_s, pb_s, pab_s, pu_s = num(pa, 2), num(pb, 2), num(pab, 2), num(pu, 2)
    return _make_p(
        "08_independent_events_product_rule_calculation",
        f"Events $A$ and $B$ are independent with $P(A) = {pa_s}$ and $P(B) = {pb_s}$. Calculate $P(A \\text{{ and }} B)$ and $P(A \\text{{ or }} B)$.",
        rf"P(A \cap B) = {pa_s} \times {pb_s} = {pab_s}",
        rf"P(A \text{{ and }} B) = {pab_s}; \quad P(A \text{{ or }} B) = {pu_s}",
        f"P(A and B)={pab_s}, P(A or B)={pu_s}",
        f"Since $A$ and $B$ are independent, $P(A \\text{{ and }} B) = {pa_s} \\times {pb_s} = {pab_s}$. Then $P(A \\text{{ or }} B) = {pa_s} + {pb_s} - {pab_s} = {pu_s}$.",
        marks=3,
    )


def build_09_testing_independence_from_probabilities(r: random.Random) -> Dict[str, Any]:
    indep = r.choice([True, False])
    pa = r.choice([0.4, 0.5, 0.6])
    pb = r.choice([0.3, 0.5])
    prod = round(pa * pb, 2)
    pab = prod if indep else round(prod + 0.06, 2)
    pa_s, pb_s, prod_s, pab_s = num(pa, 2), num(pb, 2), num(prod, 2), num(pab, 2)
    word = "independent" if indep else "dependent (not independent)"
    sym = "=" if indep else r"\neq"
    return _make_p(
        "09_testing_independence_from_probabilities",
        f"Given $P(A) = {pa_s}$, $P(B) = {pb_s}$, and $P(A \\text{{ and }} B) = {pab_s}$, determine by calculation whether $A$ and $B$ are independent.",
        rf"P(A) \times P(B) = {prod_s} {sym} P(A \cap B) = {pab_s}",
        rf"P(A)\times P(B) = {prod_s} {sym} {pab_s} \implies \text{{{word}}}",
        word,
        f"$P(A) \\times P(B) = {pa_s} \\times {pb_s} = {prod_s}$. Since $P(A \\text{{ and }} B) = {pab_s} {sym} {prod_s}$, the events are {word}.",
        marks=3,
    )


def build_10_solving_unknown_k_for_mutually_exclusive_events(r: random.Random) -> Dict[str, Any]:
    pa = r.choice([0.22, 0.28, 0.34, 0.42])
    k_val = r.choice([0.31, 0.38, 0.45])
    pu = round(pa + k_val, 2)
    pa_s, k_s, pu_s = num(pa, 2), num(k_val, 2), num(pu, 2)
    return _make_p(
        "10_solving_unknown_k_for_mutually_exclusive_events",
        f"Events $A$ and $B$ are mutually exclusive with $P(A) = {pa_s}$, $P(B) = k$, and $P(A \\text{{ or }} B) = {pu_s}$. Calculate the value of $k$.",
        rf"{pa_s} + k = {pu_s}",
        rf"k = {k_s}",
        k_s,
        f"For mutually exclusive events, $P(A \\text{{ or }} B) = P(A) + P(B) \\implies {pu_s} = {pa_s} + k \\implies k = {k_s}$.",
        marks=2,
        difficulty="easy",
    )


def build_11_solving_unknown_k_for_independent_events(r: random.Random) -> Dict[str, Any]:
    pa = r.choice([0.2, 0.4, 0.5])
    k_val = r.choice([0.3, 0.4, 0.5, 0.6])
    pu = round(pa + k_val - pa * k_val, 2)
    pa_s, k_s, pu_s = num(pa, 2), num(k_val, 2), num(pu, 2)
    coeff = num(round(1.0 - pa, 2), 2)
    return _make_p(
        "11_solving_unknown_k_for_independent_events",
        f"Events $A$ and $B$ are independent with $P(A) = {pa_s}$, $P(B) = k$, and $P(A \\text{{ or }} B) = {pu_s}$. Calculate the value of $k$.",
        rf"{pa_s} + k - {pa_s}k = {pu_s}",
        rf"k = {k_s}",
        k_s,
        f"$P(A \\cup B) = P(A) + P(B) - P(A)P(B) \\implies {pu_s} = {pa_s} + {coeff}k \\implies k = {k_s}$.",
        marks=3,
    )


def build_12_probability_only_a_or_only_b(r: random.Random) -> Dict[str, Any]:
    pa = r.choice([0.45, 0.50, 0.55])
    pb = r.choice([0.40, 0.45])
    pab = r.choice([0.12, 0.15, 0.18])
    only_one = round(pa + pb - 2 * pab, 2)
    pa_s, pb_s, pab_s, ans_s = num(pa, 2), num(pb, 2), num(pab, 2), num(only_one, 2)
    return _make_p(
        "12_probability_only_a_or_only_b",
        f"In a learner beverage survey, $P(C) = {pa_s}$, $P(L) = {pb_s}$, and $P(C \\text{{ and }} L) = {pab_s}$. Calculate the probability that a learner drinks ONLY $C$ or ONLY $L$ (not both).",
        rf"P(\text{{only }} C) + P(\text{{only }} L) = ({pa_s} - {pab_s}) + ({pb_s} - {pab_s})",
        ans_s,
        ans_s,
        f"$P(\\text{{only }} C) = {pa_s} - {pab_s} = {num(round(pa-pab, 2), 2)}$ and $P(\\text{{only }} L) = {pb_s} - {pab_s} = {num(round(pb-pab, 2), 2)}$. Sum $= {ans_s}$.",
        marks=3,
    )


def build_13_probability_neither_a_nor_b_de_morgan(r: random.Random) -> Dict[str, Any]:
    pa = r.choice([0.42, 0.48, 0.52])
    pb = r.choice([0.35, 0.40])
    pab = r.choice([0.10, 0.15])
    pu = round(pa + pb - pab, 2)
    neither = round(1.0 - pu, 2)
    pa_s, pb_s, pab_s, n_s = num(pa, 2), num(pb, 2), num(pab, 2), num(neither, 2)
    return _make_p(
        "13_probability_neither_a_nor_b_de_morgan",
        f"Given $P(A) = {pa_s}$, $P(B) = {pb_s}$, and $P(A \\text{{ and }} B) = {pab_s}$, calculate $P(\\text{{not}}(A \\text{{ or }} B))$.",
        rf"1 - ({pa_s} + {pb_s} - {pab_s})",
        n_s,
        n_s,
        f"$P(A \\text{{ or }} B) = {pa_s} + {pb_s} - {pab_s} = {num(pu, 2)}$. Thus $P(\\text{{not}}(A \\text{{ or }} B)) = 1 - {num(pu, 2)} = {n_s}$.",
        marks=3,
    )


def build_14_sampling_with_replacement_independent_draws(r: random.Random) -> Dict[str, Any]:
    red = r.randint(3, 6)
    blue = r.randint(4, 7)
    tot = red + blue
    prob = sp.Rational(red * blue, tot * tot)
    return _make_p(
        "14_sampling_with_replacement_independent_draws",
        f"A bag contains {red} red beads and {blue} blue beads. A bead is drawn at random, its colour recorded, and it is replaced in the bag before a second bead is drawn. Calculate the probability that the first bead is red and the second bead is blue.",
        rf"\frac{{{red}}}{{{tot}}} \times \frac{{{blue}}}{{{tot}}}",
        to_latex(prob),
        str(prob),
        f"With replacement, the draws are independent: $P(R_1 \\text{{ and }} B_2) = \\frac{{{red}}}{{{tot}}} \\times \\frac{{{blue}}}{{{tot}}} = {to_latex(prob)}$.",
        marks=2,
    )


def build_15_sampling_without_replacement_dependent_draws(r: random.Random) -> Dict[str, Any]:
    red = r.randint(3, 6)
    green = r.randint(4, 7)
    tot = red + green
    prob = sp.Rational(red * green, tot * (tot - 1))
    return _make_p(
        "15_sampling_without_replacement_dependent_draws",
        f"A bag contains {red} red beads and {green} green beads. Two beads are drawn consecutively WITHOUT replacement. Calculate the probability that the first bead is red and the second bead is green.",
        rf"\frac{{{red}}}{{{tot}}} \times \frac{{{green}}}{{{tot - 1}}}",
        to_latex(prob),
        str(prob),
        f"Without replacement: $P(R_1 \\text{{ and }} G_2) = \\frac{{{red}}}{{{tot}}} \\times \\frac{{{green}}}{{{tot - 1}}} = {to_latex(prob)}$.",
        marks=3,
    )


def build_16_venn_diagram_two_sets_region_extraction(r: random.Random) -> Dict[str, Any]:
    oa = r.randint(12, 22)
    inter = r.randint(6, 14)
    ob = r.randint(10, 20)
    out = r.randint(5, 12)
    tot = oa + inter + ob + out
    prob = sp.Rational(oa + inter + ob, tot)
    d_spec = _venn_2_sets_svg(str(oa), str(inter), str(ob), str(out), f"N = {tot}")
    return _make_p(
        "16_venn_diagram_two_sets_region_extraction",
        f"Refer to the two-event set figure where {oa} candidates study Accounting exclusively, {inter} study both Accounting ($A$) and Business ($B$), {ob} study Business exclusively, and {out} study neither subject. Calculate the total sample space size $N$ and the union probability $P(A \\text{{ or }} B)$.",
        rf"N = {tot}, \quad P(A \cup B) = \frac{{{oa + inter + ob}}}{{{tot}}}",
        rf"N = {tot}; \quad P(A \text{{ or }} B) = {to_latex(prob)}",
        str(prob),
        f"$N = {oa} + {inter} + {ob} + {out} = {tot}$. $P(A \\text{{ or }} B) = \\frac{{{oa + inter + ob}}}{{{tot}}} = {to_latex(prob)}$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_17_venn_diagram_two_sets_solve_unknown_x(r: random.Random) -> Dict[str, Any]:
    x_val = r.randint(8, 18)
    na = x_val + r.randint(15, 25)
    nb = x_val + r.randint(12, 22)
    out = r.randint(6, 14)
    tot = (na - x_val) + x_val + (nb - x_val) + out
    d_spec = _venn_2_sets_svg(f"{na} - x", "x", f"{nb} - x", str(out), f"N = {tot}")
    return _make_p(
        "17_venn_diagram_two_sets_solve_unknown_x",
        f"Refer to the Venn diagram for $N = {tot}$ learners where $n(A) = {na}$, $n(B) = {nb}$, $n(A \\text{{ and }} B) = x$, and {out} learners take neither. Solve for $x$.",
        rf"({na} - x) + x + ({nb} - x) + {out} = {tot}",
        rf"x = {x_val}",
        str(x_val),
        f"Summing the disjoint regions gives ${na + nb + out} - x = {tot} \\implies x = {x_val}$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_18_venn_diagram_three_sets_total_and_complement(r: random.Random) -> Dict[str, Any]:
    or_v, os_v, oc_v = r.randint(15, 25), r.randint(18, 28), r.randint(12, 22)
    rs, rc, sc = r.randint(5, 9), r.randint(4, 8), r.randint(6, 10)
    all3 = r.randint(4, 9)
    out = r.randint(8, 16)
    tot = or_v + os_v + oc_v + rs + rc + sc + all3 + out
    prob_not_r = sp.Rational(tot - (or_v + rs + rc + all3), tot)
    d_spec = _venn_3_sets_svg(str(or_v), str(os_v), str(oc_v), str(rs), str(rc), str(sc), str(all3), str(out), f"3-Set Survey (N = {tot})")
    return _make_p(
        "18_venn_diagram_three_sets_total_and_complement",
        f"Refer to the three-event set figure recording club membership with single-club frequencies {or_v}, {os_v}, {oc_v}, dual-club frequencies {rs}, {rc}, {sc}, triple-club frequency {all3}, and non-member count {out}. Determine the total cohort size $N$ and the complement probability $P(\\text{{not }} R)$.",
        rf"N = {tot}, \quad P(R') = \frac{{{tot - (or_v + rs + rc + all3)}}}{{{tot}}}",
        rf"N = {tot}; \quad P(\text{{not }} R) = {to_latex(prob_not_r)}",
        str(prob_not_r),
        f"Adding all 8 disjoint partitions gives $N = {tot}$. Since $n(R) = {or_v + rs + rc + all3}$, $P(\\text{{not }} R) = {to_latex(prob_not_r)}$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_19_venn_diagram_three_sets_solve_unknown_intersection(r: random.Random) -> Dict[str, Any]:
    or_v, os_v, oc_v = r.randint(20, 35), r.randint(18, 30), r.randint(15, 25)
    rs, rc = r.randint(6, 12), r.randint(5, 10)
    x_val = r.randint(7, 15)
    all3 = r.randint(5, 11)
    out = r.randint(6, 12)
    tot = or_v + os_v + oc_v + rs + rc + x_val + all3 + out
    d_spec = _venn_3_sets_svg(str(or_v), str(os_v), str(oc_v), str(rs), str(rc), "x", str(all3), str(out), f"Survey Total N = {tot}")
    return _make_p(
        "19_venn_diagram_three_sets_solve_unknown_intersection",
        f"Refer to the 3-set Venn diagram for $N = {tot}$ learners, where the region for $S \\text{{ and }} C \\text{{ only}}$ is $x$ and the other 7 disjoint regions are {or_v}, {os_v}, {oc_v}, {rs}, {rc}, {all3}, and {out}. Calculate the value of $x$.",
        rf"{tot - x_val} + x = {tot}",
        rf"x = {x_val}",
        str(x_val),
        f"Sum of the 7 known regions is ${tot - x_val}$. Thus ${tot - x_val} + x = {tot} \\implies x = {x_val}$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_20_venn_diagram_three_sets_at_least_two_events(r: random.Random) -> Dict[str, Any]:
    or_v, os_v, oc_v = r.randint(20, 30), r.randint(18, 28), r.randint(16, 24)
    rs, rc, sc = r.randint(7, 12), r.randint(5, 10), r.randint(6, 11)
    all3 = r.randint(5, 10)
    out = r.randint(8, 14)
    tot = or_v + os_v + oc_v + rs + rc + sc + all3 + out
    ge2 = rs + rc + sc + all3
    prob = sp.Rational(ge2, tot)
    d_spec = _venn_3_sets_svg(str(or_v), str(os_v), str(oc_v), str(rs), str(rc), str(sc), str(all3), str(out), f"3-Set Survey (N = {tot})")
    return _make_p(
        "20_venn_diagram_three_sets_at_least_two_events",
        f"Refer to the 3-set Venn diagram for $N = {tot}$ learners with pairwise-only counts {rs}, {rc}, {sc} and three-way intersection {all3}. Calculate the probability that a randomly selected learner participates in at least two of the three activities.",
        rf"P(\ge 2) = \frac{{{rs} + {rc} + {sc} + {all3}}}{{{tot}}} = \frac{{{ge2}}}{{{tot}}}",
        to_latex(prob),
        str(prob),
        f"Learners in at least two sets $= {rs} + {rc} + {sc} + {all3} = {ge2}$. Probability $= \\frac{{{ge2}}}{{{tot}}} = {to_latex(prob)}$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_21_venn_diagram_three_sets_exactly_one_event(r: random.Random) -> Dict[str, Any]:
    or_v, os_v, oc_v = r.randint(22, 34), r.randint(18, 28), r.randint(15, 25)
    rs, rc, sc = r.randint(6, 10), r.randint(5, 9), r.randint(6, 11)
    all3 = r.randint(4, 8)
    out = r.randint(7, 13)
    tot = or_v + os_v + oc_v + rs + rc + sc + all3 + out
    ex1 = or_v + os_v + oc_v
    prob = sp.Rational(ex1, tot)
    d_spec = _venn_3_sets_svg(str(or_v), str(os_v), str(oc_v), str(rs), str(rc), str(sc), str(all3), str(out), f"3-Set Survey (N = {tot})")
    return _make_p(
        "21_venn_diagram_three_sets_exactly_one_event",
        f"Refer to the 3-set Venn diagram for $N = {tot}$ learners where the 'only $R$', 'only $S$', and 'only $C$' regions are {or_v}, {os_v}, and {oc_v}. Calculate the probability that a randomly chosen learner participates in EXCACTLY one activity.",
        rf"P(\text{{exactly 1}}) = \frac{{{or_v} + {os_v} + {oc_v}}}{{{tot}}} = \frac{{{ex1}}}{{{tot}}}",
        to_latex(prob),
        str(prob),
        f"Exactly one activity $= {or_v} + {os_v} + {oc_v} = {ex1}$. Probability $= \\frac{{{ex1}}}{{{tot}}} = {to_latex(prob)}$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_22_tree_diagram_two_stage_independent_branches(r: random.Random) -> Dict[str, Any]:
    n_r = r.randint(2, 5)
    n_b = r.randint(3, 6)
    tot = n_r + n_b
    pr_str = f"{n_r}/{tot}"
    pb_str = f"{n_b}/{tot}"
    prob_same = sp.Rational(n_r * n_r + n_b * n_b, tot * tot)
    d_spec = _tree_2_stage_svg(pr_str, pb_str, pr_str, pb_str, pr_str, pb_str, f"Draws With Replacement ({n_r}R, {n_b}B)")
    return _make_p(
        "22_tree_diagram_two_stage_independent_branches",
        f"Refer to the tree diagram for two draws WITH replacement from a bag of {n_r} red ($R$) and {n_b} blue ($B$) marbles. Calculate the probability of drawing two marbles of the same colour ($RR$ or $BB$).",
        rf"P(RR) + P(BB) = \left(\frac{{{n_r}}}{{{tot}}}\right)^2 + \left(\frac{{{n_b}}}{{{tot}}}\right)^2",
        to_latex(prob_same),
        str(prob_same),
        f"$P(RR) + P(BB) = \\frac{{{n_r*n_r}}}{{{tot*tot}}} + \\frac{{{n_b*n_b}}}{{{tot*tot}}} = {to_latex(prob_same)}$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_23_tree_diagram_two_stage_dependent_without_replacement(r: random.Random) -> Dict[str, Any]:
    n_r = r.randint(3, 6)
    n_b = r.randint(4, 7)
    tot = n_r + n_b
    prob_diff = sp.Rational(2 * n_r * n_b, tot * (tot - 1))
    d_spec = _tree_2_stage_svg(
        f"{n_r}/{tot}", f"{n_b}/{tot}",
        f"{n_r-1}/{tot-1}", f"{n_b}/{tot-1}",
        f"{n_r}/{tot-1}", f"{n_b-1}/{tot-1}",
        f"Draws Without Replacement ({n_r}R, {n_b}B)",
    )
    return _make_p(
        "23_tree_diagram_two_stage_dependent_without_replacement",
        f"Refer to the tree diagram for two draws WITHOUT replacement from {n_r} red ($R$) and {n_b} blue ($B$) marbles. Calculate the probability of drawing one marble of each colour ($RB$ or $BR$).",
        rf"P(RB) + P(BR) = \frac{{{n_r}}}{{{tot}}}\cdot\frac{{{n_b}}}{{{tot-1}}} + \frac{{{n_b}}}{{{tot}}}\cdot\frac{{{n_r}}}{{{tot-1}}}",
        to_latex(prob_diff),
        str(prob_diff),
        f"$P(RB \\text{{ or }} BR) = \\frac{{{2 * n_r * n_b}}}{{{tot * (tot - 1)}}} = {to_latex(prob_diff)}$.",
        marks=3,
        diagram_spec=d_spec,
    )


def build_24_two_way_contingency_table_missing_totals(r: random.Random) -> Dict[str, Any]:
    a1, a2 = r.randint(18, 32), r.randint(12, 24)
    b1, b2 = r.randint(15, 28), r.randint(20, 35)
    r1, r2 = a1 + a2, b1 + b2
    c1, c2 = a1 + b1, a2 + b2
    tot = r1 + r2
    prob = sp.Rational(a1, tot)
    return _make_p(
        "24_two_way_contingency_table_missing_totals",
        f"Consider the two-way contingency table for $N = {tot}$ learners:\n\n"
        f"| | Plays Sport ($S$) | No Sport ($S'$) | Total |\n"
        f"|---|---|---|---|\n"
        f"| **Boys ($B$)** | $a$ | {a2} | {r1} |\n"
        f"| **Girls ($G$)** | {b1} | {b2} | {r2} |\n"
        f"| **Total** | {c1} | {c2} | {tot} |\n\n"
        f"Determine the value of $a$ and the probability $P(B \\text{{ and }} S)$.",
        rf"a = {r1} - {a2} = {a1}, \quad P(B \cap S) = \frac{{{a1}}}{{{tot}}}",
        rf"a = {a1}; \quad P(B \text{{ and }} S) = {to_latex(prob)}",
        str(a1),
        f"$a = {r1} - {a2} = {a1}$. Then $P(B \\text{{ and }} S) = \\frac{{{a1}}}{{{tot}}} = {to_latex(prob)}$.",
        marks=3,
    )


def build_25_two_way_contingency_table_independence_test(r: random.Random) -> Dict[str, Any]:
    # Construct exact independent contingency table: a1/r1 == c1/tot
    k1 = r.randint(2, 4)
    k2 = r.randint(2, 4)
    base_a, base_b = r.randint(6, 10), r.randint(4, 8)
    a1, a2 = k1 * base_a, k1 * base_b
    b1, b2 = k2 * base_a, k2 * base_b
    r1, r2 = a1 + a2, b1 + b2
    c1, c2 = a1 + b1, a2 + b2
    tot = r1 + r2
    p_inter = sp.Rational(a1, tot)
    return _make_p(
        "25_two_way_contingency_table_independence_test",
        f"A two-way contingency table of {tot} individuals is given below:\n\n"
        f"| | Event $X$ | Event $X'$ | Total |\n"
        f"|---|---|---|---|\n"
        f"| **Event $Y$** | {a1} | {a2} | {r1} |\n"
        f"| **Event $Y'$** | {b1} | {b2} | {r2} |\n"
        f"| **Total** | {c1} | {c2} | {tot} |\n\n"
        f"Show by calculation that events $X$ and $Y$ are independent.",
        rf"P(X \cap Y) = \frac{{{a1}}}{{{tot}}} = {to_latex(p_inter)}, \quad P(X)\times P(Y) = \frac{{{c1}}}{{{tot}}}\times\frac{{{r1}}}{{{tot}}} = {to_latex(p_inter)}",
        rf"P(X \cap Y) = P(X)\times P(Y) = {to_latex(p_inter)} \implies \text{{independent}}",
        "independent",
        f"$P(X \\cap Y) = \\frac{{{a1}}}{{{tot}}} = {to_latex(p_inter)}$ and $P(X) \\times P(Y) = \\frac{{{c1}}}{{{tot}}} \\times \\frac{{{r1}}}{{{tot}}} = {to_latex(p_inter)}$. Since they are equal, $X$ and $Y$ are independent.",
        marks=3,
    )


ARCHETYPES_01_25: Dict[str, Any] = {
    "01_classical_probability_equally_likely_outcomes": build_01_classical_probability_equally_likely_outcomes,
    "02_complementary_event_rule": build_02_complementary_event_rule,
    "03_addition_rule_union_of_two_events": build_03_addition_rule_union_of_two_events,
    "04_addition_rule_intersection_from_union": build_04_addition_rule_intersection_from_union,
    "05_mutually_exclusive_events_test_and_union": build_05_mutually_exclusive_events_test_and_union,
    "06_exhaustive_events_sum_to_unity": build_06_exhaustive_events_sum_to_unity,
    "07_complementary_events_mutually_exclusive_and_exhaustive": build_07_complementary_events_mutually_exclusive_and_exhaustive,
    "08_independent_events_product_rule_calculation": build_08_independent_events_product_rule_calculation,
    "09_testing_independence_from_probabilities": build_09_testing_independence_from_probabilities,
    "10_solving_unknown_k_for_mutually_exclusive_events": build_10_solving_unknown_k_for_mutually_exclusive_events,
    "11_solving_unknown_k_for_independent_events": build_11_solving_unknown_k_for_independent_events,
    "12_probability_only_a_or_only_b": build_12_probability_only_a_or_only_b,
    "13_probability_neither_a_nor_b_de_morgan": build_13_probability_neither_a_nor_b_de_morgan,
    "14_sampling_with_replacement_independent_draws": build_14_sampling_with_replacement_independent_draws,
    "15_sampling_without_replacement_dependent_draws": build_15_sampling_without_replacement_dependent_draws,
    "16_venn_diagram_two_sets_region_extraction": build_16_venn_diagram_two_sets_region_extraction,
    "17_venn_diagram_two_sets_solve_unknown_x": build_17_venn_diagram_two_sets_solve_unknown_x,
    "18_venn_diagram_three_sets_total_and_complement": build_18_venn_diagram_three_sets_total_and_complement,
    "19_venn_diagram_three_sets_solve_unknown_intersection": build_19_venn_diagram_three_sets_solve_unknown_intersection,
    "20_venn_diagram_three_sets_at_least_two_events": build_20_venn_diagram_three_sets_at_least_two_events,
    "21_venn_diagram_three_sets_exactly_one_event": build_21_venn_diagram_three_sets_exactly_one_event,
    "22_tree_diagram_two_stage_independent_branches": build_22_tree_diagram_two_stage_independent_branches,
    "23_tree_diagram_two_stage_dependent_without_replacement": build_23_tree_diagram_two_stage_dependent_without_replacement,
    "24_two_way_contingency_table_missing_totals": build_24_two_way_contingency_table_missing_totals,
    "25_two_way_contingency_table_independence_test": build_25_two_way_contingency_table_independence_test,
}
