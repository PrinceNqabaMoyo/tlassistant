"""Grade 11 Mathematics — Probability & Two-Way Contingency Tables (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (Paper 1, Question 8 / 9: 10–15 marks):
- Two-way contingency tables (marginal totals, joint probabilities, union & intersection).
- Formal algebraic and numerical proof of event independence: P(A ∩ B) = P(A) × P(B) vs dependent events.
- Mutually exclusive events rule: P(A ∪ B) = P(A) + P(B) - P(A ∩ B).
- Tree diagrams with dependent sampling without replacement.
Supports full 10-mark compound exam questions and atomic 3-mark elementary sub-drills for adaptive scaffolding.
Zero-LLM: 100% deterministic Python & SymPy calculations with South African comma decimals ({,}).
"""
from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple
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

TOPIC = "grade11_math_probability"
LO = "math11_probability_contingency"


# --------------------------------------------------------------------------- #
# Sub-drill 1: elementary_contingency_table (3 marks)
# --------------------------------------------------------------------------- #
def _build_contingency_table_drill(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding drill: Complete unknown in a 2x2 contingency table and compute probabilities."""
    total = r.choice([100, 120, 150, 200])
    m_tot = r.randint(45, total - 45)
    f_tot = total - m_tot

    l_tot = r.randint(40, total - 40)
    nl_tot = total - l_tot

    # Pick valid intersection male with license
    a = r.randint(max(15, m_tot + l_tot - total + 5), min(m_tot - 10, l_tot - 10))
    b = m_tot - a
    c = l_tot - a
    d = f_tot - c

    # Hide b as 'x'
    prompt_table = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Gender} & \textbf{Licensed } (L) & \textbf{Unlicensed } (L') & \textbf{Total} \\ \hline"
        rf"\text{{Male }} (M) & {a} & x & {m_tot} \\ \hline"
        rf"\text{{Female }} (F) & {c} & {d} & {f_tot} \\ \hline"
        rf"\textbf{{Total}} & {l_tot} & {nl_tot} & {total} \\ \hline"
        r"\end{array}"
    )

    p_fem_lic_frac = Fraction(c, total)
    p_fem_lic_dec = round(c / total, 4)
    p_fem_lic_str = num(p_fem_lic_dec, 3)

    prompt = (
        f"A survey of {total} Grade 11 learners recorded whether each learner holds a valid learner's license:\n\n"
        f"$${prompt_table}$$\n\n"
        f"1. Determine the value of $x$. (1)\n"
        f"2. Calculate the probability that a randomly chosen learner is Female AND holds a license, $P(F \\cap L)$. "
        f"Express your answer as a simplified fraction or decimal. (2)"
    )

    steps = [
        step(
            from_latex=rf"x = {m_tot} - {a}",
            to_latex_str=rf"x = {b}",
            op="solve for unknown table cell x by marginal row subtraction",
            rule="contingency table row balance",
        ),
        step(
            from_latex=rf"P(F \cap L) = \frac{{{c}}}{{{total}}}",
            to_latex_str=rf"= \frac{{{p_fem_lic_frac.numerator}}}{{{p_fem_lic_frac.denominator}}} \approx {p_fem_lic_str}",
            op="calculate intersection probability of female and licensed",
            rule="classical relative frequency definition",
        ),
    ]

    canonical = solution_graph(
        goal="determine missing cell and calculate joint probability from contingency table",
        steps=steps,
        final_latex=rf"x = {b}; \quad P(F \cap L) = \frac{{{p_fem_lic_frac.numerator}}}{{{p_fem_lic_frac.denominator}}}",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct value of x: {b}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Correct fraction setup: {c}/{total}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"Correct simplified fraction {p_fem_lic_frac.numerator}/{p_fem_lic_frac.denominator} or decimal", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "arithmetic_error", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "The sum of the cells in the 'Male' row must equal the row total.",
        "concept": "For joint probability $P(F \\cap L)$, divide the number of females with a license by the grand total $N$.",
        "breakdown": f"1. $x = {m_tot} - {a} = {b}$.\n2. Number of licensed females is {c}.\n3. $P(F \\cap L) = \\frac{{{c}}}{{{total}}} = \\frac{{{p_fem_lic_frac.numerator}}}{{{p_fem_lic_frac.denominator}}}$.",
    }

    diag = {
        "kind": "contingency_table",
        "rows": ["Male", "Female", "Total"],
        "cols": ["Licensed", "Unlicensed", "Total"],
        "matrix": [
            [a, "x", m_tot],
            [c, d, f_tot],
            [l_tot, nl_tot, total],
        ],
    }

    return make_math_question(
        prefix="prob_table",
        topic=TOPIC,
        subskill="elementary_contingency_table",
        learning_objective_id=f"{LO}_contingency_basics",
        prompt=prompt,
        prompt_latex=prompt_table,
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        diagram_spec=diag,
        misconception_tags=["divided_by_subtotal_instead_of_grand_total", "row_column_confusion"],
        keywords=["contingency table", "joint probability", "marginal totals", "probability"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_contingency_table",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Sub-drill 2: elementary_mutually_exclusive_test (3 marks)
# --------------------------------------------------------------------------- #
def _build_mutually_exclusive_drill(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding drill: Test whether two events are mutually exclusive."""
    is_mut_excl = r.choice([True, False])

    p_a = r.choice([0.25, 0.30, 0.35, 0.40, 0.45])
    p_b = r.choice([0.20, 0.25, 0.30, 0.35])

    if is_mut_excl:
        p_inter = 0.0
        p_union = round(p_a + p_b, 2)
        conclusion_str = r"\text{Since } P(A \cap B) = 0, \text{ the events are MUTUALLY EXCLUSIVE.}"
        concl_word = "MUTUALLY EXCLUSIVE"
    else:
        p_inter = r.choice([0.05, 0.08, 0.10, 0.12])
        p_union = round(p_a + p_b - p_inter, 2)
        conclusion_str = rf"\text{{Since }} P(A \cap B) = {num(p_inter, 2)} \neq 0, \text{{ the events are NOT mutually exclusive.}}"
        concl_word = "NOT MUTUALLY EXCLUSIVE"

    p_a_str = num(p_a, 2)
    p_b_str = num(p_b, 2)
    p_union_str = num(p_union, 2)
    p_inter_str = num(p_inter, 2)

    prompt = (
        f"Two events $A$ and $B$ have probabilities $P(A) = {p_a_str}$, $P(B) = {p_b_str}$, "
        f"and $P(A \\cup B) = {p_union_str}$.\n\n"
        f"1. Calculate $P(A \\cap B)$. (2)\n"
        f"2. Hence, state whether events $A$ and $B$ are mutually exclusive. Justify your answer. (1)"
    )

    steps = [
        step(
            from_latex=r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
            to_latex_str=rf"{p_union_str} = {p_a_str} + {p_b_str} - P(A \cap B)",
            op="substitute known probabilities into general addition rule",
            rule="addition rule of probability",
        ),
        step(
            from_latex=rf"P(A \cap B) = {p_a_str} + {p_b_str} - {p_union_str}",
            to_latex_str=rf"P(A \cap B) = {p_inter_str}",
            op="solve for intersection probability P(A and B)",
            rule="algebraic transposition",
        ),
        step(
            from_latex=rf"P(A \cap B) = {p_inter_str}",
            to_latex_str=conclusion_str,
            op="evaluate condition P(A and B) = 0",
            rule="definition of mutually exclusive events",
        ),
    ]

    canonical = solution_graph(
        goal="determine intersection probability and test mutual exclusivity",
        steps=steps,
        final_latex=rf"P(A \cap B) = {p_inter_str}; \quad {concl_word}",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Formula setup: {p_union_str} = {p_a_str} + {p_b_str} - P(A \cap B)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Correct calculation of P(A \cap B) = {p_inter_str}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"Correct conclusion ({concl_word}) with valid reason based on P(A \cap B)", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "confused_mutually_exclusive_with_independent", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    rel_sym = '=' if is_mut_excl else r'\neq'
    hints = {
        "nudge": r"Use the addition rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.",
        "concept": "Events $A$ and $B$ are mutually exclusive if and only if they cannot occur at the same time, meaning $P(A \\cap B) = 0$.",
        "breakdown": f"1. $P(A \\cap B) = P(A) + P(B) - P(A \\cup B) = {p_a_str} + {p_b_str} - {p_union_str} = {p_inter_str}$.\n2. Since $P(A \\cap B) {rel_sym} 0$, the events are {concl_word}.",
    }

    return make_math_question(
        prefix="prob_mut_excl",
        topic=TOPIC,
        subskill="elementary_mutually_exclusive_test",
        learning_objective_id=f"{LO}_mutually_exclusive",
        prompt=prompt,
        prompt_latex=r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_mutually_exclusive_with_independent", "subtracted_union_incorrectly"],
        keywords=["mutually exclusive", "addition rule", "intersection", "probability"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_mutually_exclusive_test",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Sub-drill 3: elementary_independent_events (3 marks)
# --------------------------------------------------------------------------- #
def _build_independent_events_drill(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding drill: Test event independence with full numerical proof."""
    is_independent = r.choice([True, False])

    p_a_num = r.choice([2, 3, 4, 5])
    p_a_den = 10
    p_b_num = r.choice([3, 4, 5, 6])
    p_b_den = 10

    p_a = p_a_num / p_a_den
    p_b = p_b_num / p_b_den
    prod = round(p_a * p_b, 4)

    if is_independent:
        p_inter = prod
        concl_str = rf"P(A) \times P(B) = {num(p_a, 2)} \times {num(p_b, 2)} = {num(prod, 4)} = P(A \cap B) \implies \text{{Events are INDEPENDENT}}"
        concl_word = "INDEPENDENT"
    else:
        delta = r.choice([-0.06, -0.04, 0.04, 0.06])
        p_inter = round(prod + delta, 4)
        concl_str = rf"P(A) \times P(B) = {num(p_a, 2)} \times {num(p_b, 2)} = {num(prod, 4)} \neq {num(p_inter, 4)} = P(A \cap B) \implies \text{{Events are DEPENDENT}}"
        concl_word = "DEPENDENT"

    p_a_str = num(p_a, 2)
    p_b_str = num(p_b, 2)
    p_inter_str = num(p_inter, 4)
    prod_str = num(prod, 4)

    prompt = (
        f"Two events $A$ and $B$ have probabilities $P(A) = {p_a_str}$, $P(B) = {p_b_str}$, "
        f"and $P(A \\cap B) = {p_inter_str}$.\n\n"
        f"Show whether events $A$ and $B$ are INDEPENDENT or DEPENDENT. Show ALL numerical working to justify your answer. (3)"
    )

    steps = [
        step(
            from_latex=r"P(A) \times P(B)",
            to_latex_str=rf"= {p_a_str} \times {p_b_str} = {prod_str}",
            op="calculate the product P(A) * P(B)",
            rule="multiplication rule test for independence",
        ),
        step(
            from_latex=rf"P(A \cap B) = {p_inter_str} \quad \text{{vs}} \quad P(A) \times P(B) = {prod_str}",
            to_latex_str=concl_str,
            op="compare intersection with product and state conclusion",
            rule="definition of independent events",
        ),
    ]

    canonical = solution_graph(
        goal="evaluate product rule test to determine event independence",
        steps=steps,
        final_latex=concl_str,
    )

    comp_sym = '=' if is_independent else r'\neq'
    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct calculation of P(A) x P(B) = {prod_str}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Direct comparison: {p_inter_str} {comp_sym} {prod_str}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"Correct conclusion: Events are {concl_word}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "stated_conclusion_without_numerical_proof", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": r"Calculate $P(A) \times P(B)$ and compare it directly to $P(A \cap B)$.",
        "concept": "Two events are independent if and only if $P(A \\cap B) = P(A) \\times P(B)$. If the two values differ, the events are dependent.",
        "breakdown": f"1. Compute $P(A) \\times P(B) = {p_a_str} \\times {p_b_str} = {prod_str}$.\n2. Note $P(A \\cap B) = {p_inter_str}$.\n3. Since they are {'EQUAL' if is_independent else 'NOT EQUAL'}, the events are {concl_word}.",
    }

    return make_math_question(
        prefix="prob_indep",
        topic=TOPIC,
        subskill="elementary_independent_events",
        learning_objective_id=f"{LO}_independent_events",
        prompt=prompt,
        prompt_latex=r"P(A \cap B) = P(A) \times P(B)",
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["tested_independence_using_addition_rule", "confused_mutually_exclusive_with_independent"],
        keywords=["independent events", "dependent events", "product rule", "probability"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_independent_events",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Compound Exam Ceiling: mode="compound" (10 marks)
# --------------------------------------------------------------------------- #
def _build_compound_probability_exam(r, difficulty: str) -> Dict[str, Any]:
    """10-Mark NSC Paper 1 Comprehensive Probability Examination Question:
    Part 1 (2 marks): Two-way contingency table completion (finding unknowns a and b).
    Part 2 (2 marks): Marginal and union probabilities: P(Female or Licensed) = P(F) + P(L) - P(F ∩ L).
    Part 3 (3 marks): Formal independence proof with numerical evidence: P(M ∩ L) vs P(M) × P(L).
    Part 4 (3 marks): Dependent sampling without replacement tree diagram problem.
    """
    # ------------------ Parts 1 to 3: Contingency Table Setup ------------------ #
    total_learners = 120
    m_tot = r.choice([48, 50, 52, 60])
    f_tot = total_learners - m_tot

    l_tot = r.choice([40, 48, 60])
    nl_tot = total_learners - l_tot

    # Determine whether events are independent or dependent
    make_indep = r.choice([True, False])
    if make_indep and (m_tot * l_tot) % total_learners == 0:
        a_val = (m_tot * l_tot) // total_learners
    else:
        # Dependent
        base = (m_tot * l_tot) // total_learners
        a_val = base + r.choice([-4, -3, 3, 4])
        # Ensure bounds
        a_val = max(10, min(a_val, min(m_tot - 10, l_tot - 10)))

    b_val = m_tot - a_val
    c_val = l_tot - a_val
    d_val = f_tot - c_val

    # Table layout: hide a as 'p' and d as 'q'
    prompt_table = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Gender} & \textbf{Learner's License } (L) & \textbf{No License } (L') & \textbf{Total} \\ \hline"
        rf"\text{{Male }} (M) & p & {b_val} & {m_tot} \\ \hline"
        rf"\text{{Female }} (F) & {c_val} & q & {f_tot} \\ \hline"
        rf"\textbf{{Total}} & {l_tot} & {nl_tot} & {total_learners} \\ \hline"
        r"\end{array}"
    )

    # 1.2 Union probability: P(Female or Licensed) = P(F) + P(L) - P(F ∩ L)
    # F = f_tot, L = l_tot, F ∩ L = c_val
    n_f_or_l = f_tot + l_tot - c_val
    p_union_frac = Fraction(n_f_or_l, total_learners)
    p_union_dec = round(n_f_or_l / total_learners, 4)
    p_union_str = num(p_union_dec, 3)

    # 1.3 Independence proof for Male and Licensed:
    # P(M) = m_tot / 120, P(L) = l_tot / 120, P(M ∩ L) = a_val / 120
    p_m_frac = Fraction(m_tot, total_learners)
    p_l_frac = Fraction(l_tot, total_learners)
    p_inter_frac = Fraction(a_val, total_learners)
    p_prod_frac = p_m_frac * p_l_frac

    is_indep = (p_inter_frac == p_prod_frac)
    concl_word = "INDEPENDENT" if is_indep else "DEPENDENT"
    relation_symbol = "=" if is_indep else r"\neq"

    # ------------------ Part 4: Tree Diagram (Dependent Sampling) --------------- #
    # School leadership council: n_b boys and n_g girls
    n_b = r.randint(6, 8)
    n_g = r.randint(4, 6)
    n_t = n_b + n_g

    # Probability of selecting at least one girl when 2 are selected without replacement:
    # P(at least 1 girl) = 1 - P(two boys) = 1 - (n_b / n_t) * ((n_b - 1) / (n_t - 1))
    p_bb = Fraction(n_b * (n_b - 1), n_t * (n_t - 1))
    p_at_least_1_g = 1 - p_bb
    p_tree_dec = round(float(p_at_least_1_g), 4)
    p_tree_str = num(p_tree_dec, 3)

    prompt = (
        f"QUESTION 2 (10 MARKS)\n\n"
        f"2.1 A group of {total_learners} Grade 11 learners were surveyed regarding their driver's learner's license status.\n"
        f"    The results are summarized in the contingency table below:\n\n"
        f"$${prompt_table}$$\n\n"
        f"    (a) Calculate the values of $p$ and $q$. (2)\n"
        f"    (b) Calculate the probability that a learner chosen at random from this group is Female OR has a learner's license, "
        f"$P(F \\cup L)$. (2)\n"
        f"    (c) Determine, with complete mathematical proof, whether the events of being 'Male' and 'having a learner's license' "
        f"are INDEPENDENT or DEPENDENT. (3)\n\n"
        f"2.2 A committee of 2 learners is to be chosen at random, without replacement, from a council of {n_t} learners "
        f"consisting of {n_b} boys and {n_g} girls.\n"
        f"    Use a tree diagram or probability principles to determine the probability that AT LEAST ONE girl is selected. (3)"
    )

    steps = [
        # 2.1 (a)
        step(
            from_latex=rf"p = {m_tot} - {b_val} = {a_val}, \quad q = {f_tot} - {c_val} = {d_val}",
            to_latex_str=rf"p = {a_val}, \; q = {d_val}",
            op="calculate unknown table entries using row subtractions",
            rule="contingency table balance",
        ),
        # 2.1 (b)
        step(
            from_latex=rf"P(F \cup L) = P(F) + P(L) - P(F \cap L) = \frac{{{f_tot}}}{{{total_learners}}} + \frac{{{l_tot}}}{{{total_learners}}} - \frac{{{c_val}}}{{{total_learners}}}",
            to_latex_str=rf"= \frac{{{n_f_or_l}}}{{{total_learners}}} = \frac{{{p_union_frac.numerator}}}{{{p_union_frac.denominator}}} \approx {p_union_str}",
            op="calculate union probability using addition rule",
            rule="general probability addition rule",
        ),
        # 2.1 (c)
        step(
            from_latex=(
                rf"P(M) \times P(L) = \frac{{{m_tot}}}{{{total_learners}}} \times \frac{{{l_tot}}}{{{total_learners}}} "
                rf"= \frac{{{p_prod_frac.numerator}}}{{{p_prod_frac.denominator}}}"
            ),
            to_latex_str=(
                rf"P(M \cap L) = \frac{{{a_val}}}{{{total_learners}}} = \frac{{{p_inter_frac.numerator}}}{{{p_inter_frac.denominator}}}; \quad "
                rf"P(M \cap L) {relation_symbol} P(M) \times P(L) \implies \text{{{concl_word}}}"
            ),
            op="compare intersection with product of marginals",
            rule="independent events test P(A and B) = P(A) * P(B)",
        ),
        # 2.2
        step(
            from_latex=(
                rf"P(\text{{two boys}}) = \frac{{{n_b}}}{{{n_t}}} \times \frac{{{n_b - 1}}}{{{n_t - 1}}} = \frac{{{p_bb.numerator}}}{{{p_bb.denominator}}}"
            ),
            to_latex_str=(
                rf"P(\text{{at least 1 girl}}) = 1 - P(BB) = 1 - \frac{{{p_bb.numerator}}}{{{p_bb.denominator}}} "
                rf"= \frac{{{p_at_least_1_g.numerator}}}{{{p_at_least_1_g.denominator}}} \approx {p_tree_str}"
            ),
            op="evaluate complementary probability for sampling without replacement",
            rule="tree diagram and complementary event rule",
            common_errors=["sampled_with_replacement", "forgot_to_subtract_one_from_denominator"],
        ),
    ]

    canonical = solution_graph(
        goal="complete 10-mark Grade 11 probability examination question",
        steps=steps,
        final_latex=(
            rf"2.1(a) \; p = {a_val}, \; q = {d_val}; \quad "
            rf"2.1(b) \; P(F \cup L) = \frac{{{p_union_frac.numerator}}}{{{p_union_frac.denominator}}}; \quad "
            rf"2.1(c) \; \text{{{concl_word}}}; \quad "
            rf"2.2 \; P(\ge 1 \text{{ girl}}) = \frac{{{p_at_least_1_g.numerator}}}{{{p_at_least_1_g.denominator}}}"
        ),
    )

    marking_schema = {
        "total_marks": 10,
        "marking_points": [
            # 2.1 (a) - 2 marks
            {"id": "mp1", "desc": f"2.1(a) Correct value of p: {a_val}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"2.1(a) Correct value of q: {d_val}", "marks": 1, "editable": True},
            # 2.1 (b) - 2 marks
            {"id": "mp3", "desc": rf"2.1(b) Addition formula substitution: {f_tot}/{total_learners} + {l_tot}/{total_learners} - {c_val}/{total_learners}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": rf"2.1(b) Correct simplified answer: {p_union_frac.numerator}/{p_union_frac.denominator}", "marks": 1, "editable": True},
            # 2.1 (c) - 3 marks
            {"id": "mp5", "desc": rf"2.1(c) Correct product: P(M) x P(L) = {p_prod_frac.numerator}/{p_prod_frac.denominator}", "marks": 1, "editable": True},
            {"id": "mp6", "desc": rf"2.1(c) Stating P(M ∩ L) = {p_inter_frac.numerator}/{p_inter_frac.denominator} and explicit comparison", "marks": 1, "editable": True},
            {"id": "mp7", "desc": rf"2.1(c) Correct conclusion: Events are {concl_word}", "marks": 1, "editable": True},
            # 2.2 - 3 marks
            {"id": "mp8", "desc": rf"2.2 Correct first and second stage probabilities without replacement: {n_b}/{n_t} and {n_b-1}/{n_t-1}", "marks": 1, "editable": True},
            {"id": "mp9", "desc": rf"2.2 Calculating complementary event 1 - P(BB) or summing PG + GP + GG", "marks": 1, "editable": True},
            {"id": "mp10", "desc": rf"2.2 Correct final simplified fraction: {p_at_least_1_g.numerator}/{p_at_least_1_g.denominator}", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "sampled_with_replacement", "penalty": -1},
            {"rule": "stated_independence_without_calculation", "penalty": -2},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Use the table totals to solve for $p$ and $q$, the addition rule for $P(F \\cup L)$, and $P(M \\cap L) = P(M) \\times P(L)$ to test independence.",
        "concept": (
            "Key CAPS Probability rules:\n"
            "• Addition rule: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$\n"
            "• Independence condition: $P(A \\cap B) = P(A) \\times P(B)$\n"
            "• Dependent sampling without replacement reduces both numerator and denominator in the second draw."
        ),
        "breakdown": (
            f"2.1(a) $p = {m_tot} - {b_val} = {a_val}$, $q = {f_tot} - {c_val} = {d_val}$.\n"
            f"2.1(b) $P(F \\cup L) = \\frac{{{f_tot} + {l_tot} - {c_val}}}{{{total_learners}}} = \\frac{{{p_union_frac.numerator}}}{{{p_union_frac.denominator}}}$.\n"
            f"2.1(c) $P(M) \\times P(L) = \\frac{{{p_prod_frac.numerator}}}{{{p_prod_frac.denominator}}}$ vs $P(M \\cap L) = \\frac{{{p_inter_frac.numerator}}}{{{p_inter_frac.denominator}}} \\implies \\text{{{concl_word}}}$.\n"
            f"2.2 $P(\\ge 1 \\text{{ girl}}) = 1 - P(BB) = 1 - \\left(\\frac{{{n_b}}}{{{n_t}}} \\times \\frac{{{n_b-1}}}{{{n_t-1}}}\\right) = \\frac{{{p_at_least_1_g.numerator}}}{{{p_at_least_1_g.denominator}}}$."
        ),
    }

    diag = {
        "kind": "contingency_table_and_tree",
        "table": {
            "rows": ["Male", "Female", "Total"],
            "cols": ["Licensed", "Unlicensed", "Total"],
            "matrix": [
                [a_val, b_val, m_tot],
                [c_val, d_val, f_tot],
                [l_tot, nl_tot, total_learners],
            ],
        },
        "tree": {
            "root": "Selection",
            "branches_stage1": [
                {"choice": "Boy", "prob": f"{n_b}/{n_t}"},
                {"choice": "Girl", "prob": f"{n_g}/{n_t}"},
            ],
            "branches_stage2": [
                {"parent": "Boy", "choice": "Boy", "prob": f"{n_b-1}/{n_t-1}"},
                {"parent": "Boy", "choice": "Girl", "prob": f"{n_g}/{n_t-1}"},
                {"parent": "Girl", "choice": "Boy", "prob": f"{n_b}/{n_t-1}"},
                {"parent": "Girl", "choice": "Girl", "prob": f"{n_g-1}/{n_t-1}"},
            ],
        },
    }

    return make_math_question(
        prefix="prob_exam_compound",
        topic=TOPIC,
        subskill="probability_contingency_compound",
        learning_objective_id=f"{LO}_compound_exam",
        prompt=prompt,
        prompt_latex=prompt_table,
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        diagram_spec=diag,
        misconception_tags=[
            "confused_mutually_exclusive_with_independent",
            "sampled_with_replacement",
            "divided_by_subtotal_instead_of_grand_total",
            "forgot_to_subtract_intersection_in_union",
        ],
        keywords=["contingency table", "independent events", "tree diagram", "without replacement", "NSC Paper 1"],
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
    "compound": _build_compound_probability_exam,
    "elementary_contingency_table": _build_contingency_table_drill,
    "elementary_mutually_exclusive_test": _build_mutually_exclusive_drill,
    "elementary_independent_events": _build_independent_events_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 11 Probability questions meeting the 6-pillar contract."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_probability_exam)

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
