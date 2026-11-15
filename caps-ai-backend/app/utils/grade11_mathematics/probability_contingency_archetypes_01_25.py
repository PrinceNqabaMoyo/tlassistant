"""Grade 11 Mathematics — Probability Archetypes 01 to 25.
Part 1 of 2: Grounded in official South African curriculum standards:
- Revision of probability definitions, sample spaces, complementary events, mutually exclusive events.
- The addition rule for any two events: P(A or B) = P(A) + P(B) - P(A and B).
- Two-set Venn diagrams with counts, probabilities, and algebraic unknowns (x in intersection).
- Independent vs dependent events: mathematical proof using P(A and B) = P(A) * P(B).
Zero-LLM: 100% deterministic Python & SymPy calculations with South African comma decimals ({{,}}).
"""

from __future__ import annotations

import math
import random
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import sympy as sp

from app.utils.grade11_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    num,
    solution_graph,
    step,
    to_latex,
)

TOPIC_ID = "grade11_math_probability"
TOPIC_NAME = "Probability"
LEARNING_OBJECTIVE_ID = "math11_probability_foundations"

SA_NAMES = ["Bongani", "Thabo", "Nomsa", "Sipho", "Lerato", "Zanele", "Kagiso", "Nandi", "Andile", "Mpho", "Sindi", "Jabulani"]
SUBJECT_PAIRS = [("Mathematics", "Physical Sciences"), ("Accounting", "Economics"), ("Life Sciences", "Geography"), ("History", "English")]


def fmt_frac(f: Fraction) -> str:
    """Format fraction as LaTeX string."""
    if f.denominator == 1:
        return str(f.numerator)
    return rf"\frac{{{f.numerator}}}{{{f.denominator}}}"


def venn_2_svg(
    only_a: Any,
    only_b: Any,
    both: Any,
    outside: Any,
    label_a: str = "A",
    label_b: str = "B",
    title: str = "Two-Set Venn Diagram",
) -> str:
    """Generate publication-grade 2-circle Venn diagram SVG."""
    w, h = 500, 320
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">',
        f'<rect x="15" y="25" width="{w-30}" height="{h-40}" rx="12" fill="#ffffff" stroke="#334155" stroke-width="2"/>',
        f'<text x="35" y="52" font-size="16" font-weight="bold" fill="#0f172a">S</text>',
        f'<text x="{w//2}" y="20" font-size="13" font-weight="bold" fill="#334155" text-anchor="middle">{title}</text>',
        # Circle A
        '<circle cx="190" cy="165" r="95" fill="#3b82f6" fill-opacity="0.18" stroke="#1d4ed8" stroke-width="2.5"/>',
        # Circle B
        '<circle cx="310" cy="165" r="95" fill="#10b981" fill-opacity="0.18" stroke="#047857" stroke-width="2.5"/>',
        # Set Labels
        f'<text x="140" y="85" font-size="14" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{label_a}</text>',
        f'<text x="360" y="85" font-size="14" font-weight="bold" fill="#047857" text-anchor="middle">{label_b}</text>',
        # Values
        f'<text x="145" y="172" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{only_a}</text>',
        f'<text x="250" y="172" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{both}</text>',
        f'<text x="355" y="172" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{only_b}</text>',
        f'<text x="440" y="280" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{outside}</text>',
        '</svg>',
    ]
    return "".join(parts)


# Archetype 01: Single Event Sample Space & Probability (Dice / Tiles)
def arch_01_single_event_sample_space_and_probability(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    n_total = r.choice([20, 24, 30, 36])
    # Multiples of k or prime numbers
    k = r.choice([3, 4, 5])
    favorable = [x for x in range(1, n_total + 1) if x % k == 0]
    n_fav = len(favorable)
    frac = Fraction(n_fav, n_total)
    dec_val = round(n_fav / n_total, 4)
    dec_str = num(dec_val, 2)

    prompt = (
        f"A bag contains {n_total} identical cards numbered sequentially from 1 to {n_total}. "
        f"One card is drawn at random from the bag.\n\n"
        f"Calculate the probability that the number on the card is a multiple of {k}. "
        f"Write your answer as a simplified common fraction."
    )
    fav_str = '; '.join(str(x) for x in favorable)
    prompt_latex = rf"\text{{Draw card from }} S = (1; 2; \dots; {n_total}). \text{{ Find }} P(\text{{multiple of }}{k})."

    steps = [
        step(from_latex=rf"n(S) = {n_total}", to_latex_str=rf"E = ({fav_str}) \implies n(E) = {n_fav}", op=f"list multiples of {k} in sample space", rule="event cardinality",),
        step(from_latex=rf"P(E) = \frac{{n(E)}}{{n(S)}} = \frac{{{n_fav}}}{{{n_total}}}", to_latex_str=fmt_frac(frac), op="simplify fraction", rule="classical probability definition",),
    ]
    canonical = solution_graph(
        goal=f"calculate probability of multiple of {k}",
        steps=steps,
        final_latex=fmt_frac(frac),
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct favorable outcomes count n(E) = {n_fav}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate simplified fraction {fmt_frac(frac)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_01",
        topic=TOPIC_NAME,
        subskill="01_single_event_sample_space_and_probability",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac),
        sample_answer=fmt_frac(frac),
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": f"Count how many numbers between 1 and {n_total} divide evenly by {k}.",
            "concept": "P(E) = favorable outcomes / total outcomes.",
            "breakdown": f"Multiples of {k} up to {n_total} are {favorable}. Total is {n_fav}. P = {n_fav}/{n_total} = {fmt_frac(frac)}.",
        },
        misconception_tags=["miscounted_favorable_outcomes", "inverted_probability_fraction"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 02: Complementary Events P(not A) = 1 - P(A)
def arch_02_complementary_event_probability(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    denom = r.choice([8, 10, 12, 16, 20, 25])
    num_a = r.randint(1, denom - 1)
    p_a = Fraction(num_a, denom)
    p_not_a = 1 - p_a

    prompt = (
        f"The probability that event $A$ will occur is given as $P(A) = {fmt_frac(p_a)}$.\n\n"
        f"Determine $P(A')$, the probability that event $A$ will NOT occur. "
        f"Give your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Given }} P(A) = {fmt_frac(p_a)}\text{{, find }} P(A')."

    steps = [
        step(from_latex=r"P(A') = 1 - P(A)", to_latex_str=rf"P(A') = 1 - {fmt_frac(p_a)}", op="apply complementary rule", rule="complement rule",),
        step(from_latex=rf"1 - {fmt_frac(p_a)} = \frac{{{denom} - {p_a.numerator}}}{{{denom}}}", to_latex_str=fmt_frac(p_not_a), op="evaluate fraction subtraction", rule="fraction arithmetic",),
    ]
    canonical = solution_graph(
        goal="determine complementary event probability",
        steps=steps,
        final_latex=fmt_frac(p_not_a),
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": "Statement or substitution of P(A') = 1 - P(A)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct simplified fraction {fmt_frac(p_not_a)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_02",
        topic=TOPIC_NAME,
        subskill="02_complementary_event_probability",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_not_a),
        sample_answer=fmt_frac(p_not_a),
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "The sum of the probabilities of an event and its complement is 1.",
            "concept": "P(A') = 1 - P(A).",
            "breakdown": f"P(A') = 1 - {fmt_frac(p_a)} = {fmt_frac(p_not_a)}.",
        },
        misconception_tags=["forgot_to_subtract_from_one"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=2,
    )


# Archetype 03: Mutually Exclusive Events Addition Rule
def arch_03_mutually_exclusive_two_events_addition(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    denom = r.choice([10, 12, 15, 20])
    num_a = r.randint(2, denom // 2 - 1)
    num_b = r.randint(1, denom - num_a - 1)
    p_a = Fraction(num_a, denom)
    p_b = Fraction(num_b, denom)
    p_union = p_a + p_b

    prompt = (
        f"Events $A$ and $B$ are mutually exclusive events in a sample space.\n"
        f"It is given that $P(A) = {fmt_frac(p_a)}$ and $P(B) = {fmt_frac(p_b)}$.\n\n"
        f"1. State the value of $P(A \\cap B)$. (1)\n"
        f"2. Calculate $P(A \\cup B)$. (2)"
    )
    prompt_latex = rf"\text{{Mutually exclusive: }} P(A) = {fmt_frac(p_a)}, P(B) = {fmt_frac(p_b)}. \text{{ Find }} P(A \cap B) \text{{ and }} P(A \cup B)."

    steps = [
        step(from_latex=r"P(A \cap B) = 0", to_latex_str=r"0", op="state intersection for mutually exclusive events", rule="mutually exclusive definition",),
        step(from_latex=r"P(A \cup B) = P(A) + P(B)", to_latex_str=rf"{fmt_frac(p_a)} + {fmt_frac(p_b)} = {fmt_frac(p_union)}", op="add individual probabilities", rule="addition rule for mutually exclusive events",),
    ]
    canonical = solution_graph(
        goal="evaluate intersection and union for mutually exclusive events",
        steps=steps,
        final_latex=rf"P(A \cap B) = 0; \quad P(A \cup B) = {fmt_frac(p_union)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "P(A ∩ B) = 0 due to mutually exclusive condition", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Addition formula setup P(A ∪ B) = P(A) + P(B)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate union fraction {fmt_frac(p_union)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_03",
        topic=TOPIC_NAME,
        subskill="03_mutually_exclusive_two_events_addition",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_union),
        sample_answer=rf"P(A \cap B) = 0; \quad P(A \cup B) = {fmt_frac(p_union)}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Mutually exclusive events cannot happen at the same time, so their intersection is 0.",
            "concept": "For mutually exclusive events, P(A or B) = P(A) + P(B).",
            "breakdown": f"P(A ∩ B) = 0. P(A ∪ B) = {fmt_frac(p_a)} + {fmt_frac(p_b)} = {fmt_frac(p_union)}.",
        },
        misconception_tags=["assumed_independent_instead_of_mutually_exclusive"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 04: Three Mutually Exclusive Events
def arch_04_mutually_exclusive_three_events(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    denom = r.choice([12, 16, 20])
    a = r.randint(2, 4)
    b = r.randint(2, 4)
    c = r.randint(2, 4)
    p_a = Fraction(a, denom)
    p_b = Fraction(b, denom)
    p_c = Fraction(c, denom)
    p_union = p_a + p_b + p_c

    prompt = (
        f"A spinner has sectors colored Red, Blue, Green, and Yellow.\n"
        f"The events of landing on Red ($R$), Blue ($B$), and Green ($G$) are mutually exclusive with "
        f"$P(R) = {fmt_frac(p_a)}$, $P(B) = {fmt_frac(p_b)}$, and $P(G) = {fmt_frac(p_c)}$.\n\n"
        f"Calculate the probability that the spinner lands on Red OR Blue OR Green, $P(R \\cup B \\cup G)$."
    )
    prompt_latex = rf"\text{{Mutually exclusive: }} P(R) = {fmt_frac(p_a)}, P(B) = {fmt_frac(p_b)}, P(G) = {fmt_frac(p_c)}. \text{{ Find }} P(R \cup B \cup G)."

    steps = [
        step(from_latex=r"P(R \cup B \cup G) = P(R) + P(B) + P(G)", to_latex_str=rf"{fmt_frac(p_a)} + {fmt_frac(p_b)} + {fmt_frac(p_c)} = {fmt_frac(p_union)}", op="sum probabilities of pairwise disjoint events", rule="extended addition rule",),
    ]
    canonical = solution_graph(
        goal="sum probabilities of 3 mutually exclusive events",
        steps=steps,
        final_latex=fmt_frac(p_union),
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": "Summing all three probabilities", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate simplified sum {fmt_frac(p_union)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_04",
        topic=TOPIC_NAME,
        subskill="04_mutually_exclusive_three_events",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_union),
        sample_answer=fmt_frac(p_union),
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Since the outcomes cannot occur together, simply add their individual probabilities.",
            "concept": "P(A ∪ B ∪ C) = P(A) + P(B) + P(C).",
            "breakdown": f"{fmt_frac(p_a)} + {fmt_frac(p_b)} + {fmt_frac(p_c)} = {fmt_frac(p_union)}.",
        },
        misconception_tags=["multiplied_instead_of_added_mutually_exclusive"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=2,
    )


# Archetype 05: Addition Rule — Find Union P(A or B)
def arch_05_addition_rule_find_union(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    denom = r.choice([10, 12, 15, 20])
    num_both = r.randint(2, 4)
    num_a = r.randint(num_both + 1, num_both + 5)
    num_b = r.randint(num_both + 1, num_both + 4)

    p_a = Fraction(num_a, denom)
    p_b = Fraction(num_b, denom)
    p_both = Fraction(num_both, denom)
    p_union = p_a + p_b - p_both

    prompt = (
        f"For two events $A$ and $B$, it is given that:\n"
        f"$$P(A) = {fmt_frac(p_a)}, \\quad P(B) = {fmt_frac(p_b)}, \\quad P(A \\cap B) = {fmt_frac(p_both)}$$\n\n"
        f"Calculate $P(A \\cup B)$, the probability that event $A$ or event $B$ occurs. "
        f"Write your answer as a simplified fraction."
    )
    prompt_latex = rf"P(A) = {fmt_frac(p_a)}, P(B) = {fmt_frac(p_b)}, P(A \cap B) = {fmt_frac(p_both)}. \text{{ Find }} P(A \cup B)."

    steps = [
        step(from_latex=r"P(A \cup B) = P(A) + P(B) - P(A \cap B)", to_latex_str=rf"P(A \cup B) = {fmt_frac(p_a)} + {fmt_frac(p_b)} - {fmt_frac(p_both)}", op="substitute into addition rule", rule="general addition rule",),
        step(from_latex=rf"{fmt_frac(p_a)} + {fmt_frac(p_b)} - {fmt_frac(p_both)}", to_latex_str=fmt_frac(p_union), op="evaluate arithmetic sum and difference", rule="fraction subtraction",),
    ]
    canonical = solution_graph(
        goal="calculate union probability using addition rule",
        steps=steps,
        final_latex=fmt_frac(p_union),
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": "Correct substitution into addition rule formula", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate simplified union {fmt_frac(p_union)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_05",
        topic=TOPIC_NAME,
        subskill="05_addition_rule_find_union",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_union),
        sample_answer=fmt_frac(p_union),
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Use the general addition rule: P(A or B) = P(A) + P(B) - P(A and B).",
            "concept": "We must subtract the intersection so that elements in both are not counted twice.",
            "breakdown": f"P(A ∪ B) = {fmt_frac(p_a)} + {fmt_frac(p_b)} - {fmt_frac(p_both)} = {fmt_frac(p_union)}.",
        },
        misconception_tags=["forgot_to_subtract_intersection"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 06: Addition Rule — Find Intersection P(A and B)
def arch_06_addition_rule_find_intersection(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    denom = r.choice([10, 12, 15, 20])
    num_both = r.randint(2, 4)
    num_a = r.randint(num_both + 1, num_both + 4)
    num_b = r.randint(num_both + 1, num_both + 4)

    p_a = Fraction(num_a, denom)
    p_b = Fraction(num_b, denom)
    p_both = Fraction(num_both, denom)
    p_union = p_a + p_b - p_both

    prompt = (
        f"Two events $A$ and $B$ satisfy:\n"
        f"$$P(A) = {fmt_frac(p_a)}, \\quad P(B) = {fmt_frac(p_b)}, \\quad P(A \\cup B) = {fmt_frac(p_union)}$$\n\n"
        f"Calculate $P(A \\cap B)$, the probability that BOTH events $A$ and $B$ occur."
    )
    prompt_latex = rf"P(A) = {fmt_frac(p_a)}, P(B) = {fmt_frac(p_b)}, P(A \cup B) = {fmt_frac(p_union)}. \text{{ Find }} P(A \cap B)."

    steps = [
        step(from_latex=r"P(A \cap B) = P(A) + P(B) - P(A \cup B)", to_latex_str=rf"P(A \cap B) = {fmt_frac(p_a)} + {fmt_frac(p_b)} - {fmt_frac(p_union)}", op="rearrange addition rule to solve for intersection", rule="addition rule rearrangement",),
        step(from_latex=rf"{fmt_frac(p_a)} + {fmt_frac(p_b)} - {fmt_frac(p_union)}", to_latex_str=fmt_frac(p_both), op="evaluate fraction calculation", rule="arithmetic evaluation",),
    ]
    canonical = solution_graph(
        goal="solve for intersection probability from addition rule",
        steps=steps,
        final_latex=fmt_frac(p_both),
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": "Formula rearrangement or correct substitution", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate simplified intersection {fmt_frac(p_both)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_06",
        topic=TOPIC_NAME,
        subskill="06_addition_rule_find_intersection",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_both),
        sample_answer=fmt_frac(p_both),
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Rearrange P(A ∪ B) = P(A) + P(B) - P(A ∩ B) to solve for P(A ∩ B).",
            "concept": "P(A ∩ B) = P(A) + P(B) - P(A ∪ B).",
            "breakdown": f"P(A ∩ B) = {fmt_frac(p_a)} + {fmt_frac(p_b)} - {fmt_frac(p_union)} = {fmt_frac(p_both)}.",
        },
        misconception_tags=["assumed_independent_multiplication"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 07: Addition Rule — Solve for P(A)
def arch_07_addition_rule_find_single_event(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    denom = r.choice([10, 12, 16, 20])
    num_both = r.randint(2, 4)
    num_a = r.randint(num_both + 1, num_both + 4)
    num_b = r.randint(num_both + 1, num_both + 4)

    p_a = Fraction(num_a, denom)
    p_b = Fraction(num_b, denom)
    p_both = Fraction(num_both, denom)
    p_union = p_a + p_b - p_both

    prompt = (
        f"It is given that for events $A$ and $B$:\n"
        f"$$P(A \\cup B) = {fmt_frac(p_union)}, \\quad P(B) = {fmt_frac(p_b)}, \\quad P(A \\cap B) = {fmt_frac(p_both)}$$\n\n"
        f"Calculate $P(A)$. Write your answer as a simplified fraction."
    )
    prompt_latex = rf"P(A \cup B) = {fmt_frac(p_union)}, P(B) = {fmt_frac(p_b)}, P(A \cap B) = {fmt_frac(p_both)}. \text{{ Find }} P(A)."

    steps = [
        step(from_latex=r"P(A \cup B) = P(A) + P(B) - P(A \cap B)", to_latex_str=rf"{fmt_frac(p_union)} = P(A) + {fmt_frac(p_b)} - {fmt_frac(p_both)}", op="substitute knowns into addition rule", rule="addition rule substitution",),
        step(from_latex=rf"P(A) = {fmt_frac(p_union)} - {fmt_frac(p_b)} + {fmt_frac(p_both)}", to_latex_str=fmt_frac(p_a), op="isolate P(A) and evaluate", rule="algebraic isolation",),
    ]
    canonical = solution_graph(
        goal="solve for single event probability P(A)",
        steps=steps,
        final_latex=fmt_frac(p_a),
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": "Correct algebraic setup", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate value P(A) = {fmt_frac(p_a)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_07",
        topic=TOPIC_NAME,
        subskill="07_addition_rule_find_single_event",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_a),
        sample_answer=fmt_frac(p_a),
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "P(A) = P(A ∪ B) - P(B) + P(A ∩ B).",
            "concept": "Rearrange the addition rule to isolate the unknown event probability.",
            "breakdown": f"P(A) = {fmt_frac(p_union)} - {fmt_frac(p_b)} + {fmt_frac(p_both)} = {fmt_frac(p_a)}.",
        },
        misconception_tags=["sign_error_in_rearrangement"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 08: Addition Rule — Contextual Problem (School Subjects)
def arch_08_addition_rule_word_problem_sports_or_subjects(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    sub_a, sub_b = r.choice(SUBJECT_PAIRS)
    denom = 100
    p_a_pct = r.randint(55, 75)
    p_b_pct = r.randint(45, 65)
    p_both_pct = r.randint(30, min(p_a_pct, p_b_pct) - 10)

    p_union_pct = p_a_pct + p_b_pct - p_both_pct
    ans_dec = round(p_union_pct / 100.0, 2)
    ans_str = num(ans_dec, 2)

    prompt = (
        f"In a Grade 11 class, the probability that a learner takes {sub_a} is {p_a_pct}%, "
        f"the probability that a learner takes {sub_b} is {p_b_pct}%, and the probability that a learner "
        f"takes both {sub_a} and {sub_b} is {p_both_pct}%.\n\n"
        f"Calculate the probability that a randomly chosen learner takes {sub_a} OR {sub_b}. "
        f"Express your answer as a percentage."
    )
    prompt_latex = rf"P(A) = {p_a_pct}\%, P(B) = {p_b_pct}\%, P(A \cap B) = {p_both_pct}\%. \text{{ Find }} P(A \cup B)."

    steps = [
        step(from_latex=r"P(A \cup B) = P(A) + P(B) - P(A \cap B)", to_latex_str=rf"{p_a_pct}\% + {p_b_pct}\% - {p_both_pct}\%", op="apply addition rule with percentages", rule="addition rule",),
        step(from_latex=rf"{p_a_pct}\% + {p_b_pct}\% - {p_both_pct}\%", to_latex_str=rf"{p_union_pct}\%", op="evaluate percentage sum", rule="arithmetic addition and subtraction",),
    ]
    canonical = solution_graph(
        goal="determine union probability in context",
        steps=steps,
        final_latex=rf"{p_union_pct}\%",
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": "Correct addition rule substitution", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate answer {p_union_pct}%", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_08",
        topic=TOPIC_NAME,
        subskill="08_addition_rule_word_problem_sports_or_subjects",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"{p_union_pct}\%",
        sample_answer=rf"{p_union_pct}%",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Add the two percentages and subtract the percentage of learners taking both.",
            "concept": "P(A ∪ B) = P(A) + P(B) - P(A ∩ B).",
            "breakdown": f"{p_a_pct}% + {p_b_pct}% - {p_both_pct}% = {p_union_pct}%.",
        },
        misconception_tags=["forgot_to_subtract_overlap_percentage"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 09: Addition Rule with Decimal Comma Values
def arch_09_addition_rule_with_percentages(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # Decimal probabilities like 0,65, 0,45, 0,30
    p_a_val = r.choice([0.55, 0.60, 0.65, 0.70])
    p_b_val = r.choice([0.35, 0.40, 0.45, 0.50])
    p_both_val = r.choice([0.20, 0.25, 0.30])
    p_union_val = round(p_a_val + p_b_val - p_both_val, 2)

    pa_str = num(p_a_val, 2)
    pb_str = num(p_b_val, 2)
    pboth_str = num(p_both_val, 2)
    punion_str = num(p_union_val, 2)

    prompt = (
        f"Events $E_1$ and $E_2$ are such that $P(E_1) = {pa_str}$, $P(E_2) = {pb_str}$, "
        f"and $P(E_1 \\cap E_2) = {pboth_str}$.\n\n"
        f"Calculate $P(E_1 \\cup E_2)$. Round off your answer to TWO decimal places."
    )
    prompt_latex = rf"P(E_1) = {pa_str}, P(E_2) = {pb_str}, P(E_1 \cap E_2) = {pboth_str}. \text{{ Find }} P(E_1 \cup E_2)."

    steps = [
        step(from_latex=r"P(E_1 \cup E_2) = P(E_1) + P(E_2) - P(E_1 \cap E_2)", to_latex_str=rf"{pa_str} + {pb_str} - {pboth_str} = {punion_str}", op="apply addition rule with decimals", rule="addition rule",),
    ]
    canonical = solution_graph(
        goal="calculate union probability using decimals",
        steps=steps,
        final_latex=punion_str,
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": "Correct substitution into addition rule", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate decimal value {punion_str}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_09",
        topic=TOPIC_NAME,
        subskill="09_addition_rule_with_percentages",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=punion_str,
        sample_answer=punion_str,
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "P(E_1 ∪ E_2) = P(E_1) + P(E_2) - P(E_1 ∩ E_2).",
            "concept": "Add the probabilities and subtract the intersection.",
            "breakdown": f"{pa_str} + {pb_str} - {pboth_str} = {punion_str}.",
        },
        misconception_tags=["decimal_addition_error"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=2,
    )


# Archetype 10: Addition Rule with Frequencies out of N
def arch_10_addition_rule_with_frequencies(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_total = r.choice([60, 80, 100, 120])
    n_both = r.randint(12, 22)
    n_a = r.randint(n_both + 10, n_both + 25)
    n_b = r.randint(n_both + 8, n_both + 20)

    n_union = n_a + n_b - n_both
    frac = Fraction(n_union, n_total)

    prompt = (
        f"In a cohort of {n_total} learners:\n"
        f"- {n_a} learners participate in drama ($D$).\n"
        f"- {n_b} learners participate in music ($M$).\n"
        f"- {n_both} learners participate in both drama and music.\n\n"
        f"Calculate the probability that a randomly chosen learner participates in drama OR music. "
        f"Write your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Total }} {n_total}, n(D) = {n_a}, n(M) = {n_b}, n(D \cap M) = {n_both}. \text{{ Find }} P(D \cup M)."

    steps = [
        step(from_latex=r"n(D \cup M) = n(D) + n(M) - n(D \cap M)", to_latex_str=rf"{n_a} + {n_b} - {n_both} = {n_union}", op="calculate number of learners in union", rule="inclusion-exclusion principle for counts",),
        step(from_latex=rf"P(D \cup M) = \frac{{n(D \cup M)}}{{n(S)}} = \frac{{{n_union}}}{{{n_total}}}", to_latex_str=fmt_frac(frac), op="divide by total and simplify", rule="probability definition",),
    ]
    canonical = solution_graph(
        goal="determine union probability from counts",
        steps=steps,
        final_latex=fmt_frac(frac),
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct union count n(D ∪ M) = {n_union}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Probability fraction setup: {n_union}/{n_total}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Simplified fraction {fmt_frac(frac)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_10",
        topic=TOPIC_NAME,
        subskill="10_addition_rule_with_frequencies",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac),
        sample_answer=fmt_frac(frac),
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Find the total number of learners in drama or music first: n(D) + n(M) - n(both).",
            "concept": "Divide n(D ∪ M) by the grand total N.",
            "breakdown": f"n(D ∪ M) = {n_a} + {n_b} - {n_both} = {n_union}. P = {n_union}/{n_total} = {fmt_frac(frac)}.",
        },
        misconception_tags=["double_counted_intersection_in_frequency"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 11: Two-Set Venn Diagram — Reading Count Regions (Emits SVG)
def arch_11_venn_2_counts_read_regions(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    only_a = r.randint(15, 30)
    both = r.randint(10, 25)
    only_b = r.randint(12, 28)
    outside = r.randint(8, 20)
    n_total = only_a + both + only_b + outside

    diag_svg = venn_2_svg(only_a=only_a, only_b=only_b, both=both, outside=outside, label_a="A", label_b="B", title="Two-Set Venn Diagram (Counts)")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Two-Set Venn Diagram", "diagram_role": "context"}

    frac_only_a = Fraction(only_a, n_total)
    frac_neither = Fraction(outside, n_total)

    prompt = (
        f"The Venn diagram below illustrates the distribution of {n_total} learners in sample space $S$ "
        f"participating in events $A$ and $B$.\n\n"
        f"1. Determine the number of learners who participate in $A$ ONLY. (1)\n"
        f"2. Calculate the probability that a randomly chosen learner participates in NEITHER $A$ NOR $B$, "
        f"$P(A' \\cap B')$. Express your answer as a simplified fraction. (2)"
    )
    prompt_latex = rf"\text{{Read Venn diagram with total }} {n_total}. \text{{ Find }} n(A\text{{ only}}) \text{{ and }} P((A \cup B)')."

    steps = [
        step(from_latex=rf"n(A\text{{ only}}) = {only_a}", to_latex_str=rf"{only_a}", op="read only A region directly from diagram", rule="Venn region interpretation",),
        step(from_latex=rf"P(A' \cap B') = \frac{{\text{{outside}}}}{{n(S)}} = \frac{{{outside}}}{{{n_total}}}", to_latex_str=fmt_frac(frac_neither), op="divide outside region by total and simplify", rule="classical probability definition",),
    ]
    canonical = solution_graph(
        goal="read counts and compute neither probability from Venn diagram",
        steps=steps,
        final_latex=rf"n(A\text{{ only}}) = {only_a}; \quad P(A' \cap B') = {fmt_frac(frac_neither)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct count n(A only) = {only_a}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Correct fraction setup {outside}/{n_total}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified fraction {fmt_frac(frac_neither)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_11",
        topic=TOPIC_NAME,
        subskill="11_venn_2_counts_read_regions",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_neither),
        sample_answer=rf"n(A\text{{ only}}) = {only_a}; \quad P(A' \cap B') = {fmt_frac(frac_neither)}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "The crescent on the left contains learners in A only. The region outside both circles represents neither.",
            "concept": "P(neither) = outside count / grand total.",
            "breakdown": f"n(A only) = {only_a}. Outside = {outside}. Total = {n_total}. P = {outside}/{n_total} = {fmt_frac(frac_neither)}.",
        },
        misconception_tags=["confused_a_only_with_total_a"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 12: Two-Set Venn Diagram — Regional Probabilities (Emits SVG)
def arch_12_venn_2_probabilities_read_regions(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # Decimal probabilities summing to 1.0
    p_only_a = r.choice([0.25, 0.30, 0.35])
    p_both = r.choice([0.15, 0.20, 0.25])
    p_only_b = r.choice([0.20, 0.25, 0.30])
    p_outside = round(1.0 - (p_only_a + p_both + p_only_b), 2)

    pa_tot = round(p_only_a + p_both, 2)
    punion = round(p_only_a + p_both + p_only_b, 2)

    diag_svg = venn_2_svg(
        only_a=num(p_only_a, 2),
        only_b=num(p_only_b, 2),
        both=num(p_both, 2),
        outside=num(p_outside, 2),
        label_a="A",
        label_b="B",
        title="Venn Diagram with Regional Probabilities",
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Regional Probabilities Venn Diagram", "diagram_role": "context"}

    prompt = (
        f"The Venn diagram below displays the probabilities of the distinct regions for events $A$ and $B$ "
        f"(with $P(A\\text{{ only}}) = {num(p_only_a, 2)}$, $P(A \\cap B) = {num(p_both, 2)}$, and $P(B\\text{{ only}}) = {num(p_only_b, 2)}$).\n\n"
        f"1. Calculate $P(A)$, the total probability of event $A$. (1)\n"
        f"2. Calculate $P(A \\cup B)$, the probability of event $A$ or event $B$. (2)"
    )
    prompt_latex = rf"\text{{Read Venn diagram. Calculate }} P(A) \text{{ and }} P(A \cup B)."

    steps = [
        step(from_latex=r"P(A) = P(A\text{ only}) + P(A \cap B)", to_latex_str=rf"{num(p_only_a, 2)} + {num(p_both, 2)} = {num(pa_tot, 2)}", op="sum regions making up circle A", rule="set decomposition",),
        step(from_latex=r"P(A \cup B) = P(A\text{ only}) + P(A \cap B) + P(B\text{ only})", to_latex_str=rf"{num(p_only_a, 2)} + {num(p_both, 2)} + {num(p_only_b, 2)} = {num(punion, 2)}", op="sum all three interior regions", rule="union of disjoint regions",),
    ]
    canonical = solution_graph(
        goal="determine P(A) and P(A or B) from probability Venn diagram",
        steps=steps,
        final_latex=rf"P(A) = {num(pa_tot, 2)}; \quad P(A \cup B) = {num(punion, 2)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"P(A) = {num(pa_tot, 2)}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Summing all three disjoint regions for union", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate union P(A ∪ B) = {num(punion, 2)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_12",
        topic=TOPIC_NAME,
        subskill="12_venn_2_probabilities_read_regions",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=num(punion, 2),
        sample_answer=rf"P(A) = {num(pa_tot, 2)}; \quad P(A \cup B) = {num(punion, 2)}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "For P(A), add the 'only A' value and the intersection value. For union, add all three regions inside the circles.",
            "concept": "P(A) = P(A only) + P(A ∩ B). P(A ∪ B) = 1 - P(outside).",
            "breakdown": f"P(A) = {p_only_a} + {p_both} = {pa_tot}. P(A ∪ B) = 1 - {p_outside} = {punion}.",
        },
        misconception_tags=["forgot_to_include_intersection_in_p_a"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 13: Construct Venn Diagram from Cardinalities (Emits SVG)
def arch_13_venn_2_construct_from_cardinalities(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_tot = r.choice([50, 60, 75, 80])
    n_both = r.randint(8, 15)
    n_a = r.randint(n_both + 10, n_both + 20)
    n_b = r.randint(n_both + 8, n_both + 18)

    only_a = n_a - n_both
    only_b = n_b - n_both
    n_union = only_a + n_both + only_b
    outside = n_tot - n_union

    diag_svg = venn_2_svg(only_a=only_a, only_b=only_b, both=n_both, outside=outside, label_a="A", label_b="B", title="Constructed Two-Set Venn Diagram")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Two-Set Venn Diagram", "diagram_role": "context"}

    frac_union = Fraction(n_union, n_tot)

    prompt = (
        f"In a survey of {n_tot} learners, the following information was recorded:\n"
        f"- $n(A) = {n_a}$\n"
        f"- $n(B) = {n_b}$\n"
        f"- $n(A \\cap B) = {n_both}$\n\n"
        f"1. Determine the number of learners who participate in $B$ only. (1)\n"
        f"2. Calculate the probability that a randomly chosen learner participates in at least one of the two events, "
        f"$P(A \\cup B)$. Write your answer as a simplified fraction. (2)"
    )
    prompt_latex = rf"\text{{Survey of }} {n_tot}: n(A) = {n_a}, n(B) = {n_b}, n(A \cap B) = {n_both}. \text{{ Find }} n(B\text{{ only}}) \text{{ and }} P(A \cup B)."

    steps = [
        step(from_latex=rf"n(B\text{{ only}}) = n(B) - n(A \cap B)", to_latex_str=rf"{n_b} - {n_both} = {only_b}", op="subtract intersection from n(B)", rule="subtraction",),
        step(from_latex=rf"n(A \cup B) = (n(A) - n(A \cap B)) + n(A \cap B) + n(B\text{{ only}})", to_latex_str=rf"{only_a} + {n_both} + {only_b} = {n_union}", op="sum disjoint regions", rule="inclusion-exclusion",),
        step(from_latex=rf"P(A \cup B) = \frac{{{n_union}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_union), op="form probability and simplify", rule="probability definition",),
    ]
    canonical = solution_graph(
        goal="determine only B count and union probability",
        steps=steps,
        final_latex=rf"n(B\text{{ only}}) = {only_b}; \quad P(A \cup B) = {fmt_frac(frac_union)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct n(B only) = {only_b}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Correct fraction setup {n_union}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified fraction {fmt_frac(frac_union)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_13",
        topic=TOPIC_NAME,
        subskill="13_venn_2_construct_from_cardinalities",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_union),
        sample_answer=rf"n(B\text{{ only}}) = {only_b}; \quad P(A \cup B) = {fmt_frac(frac_union)}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "Always subtract the intersection from n(A) and n(B) to get the 'only' counts.",
            "concept": "n(B only) = n(B) - n(both). n(A ∪ B) = n(only A) + n(both) + n(only B).",
            "breakdown": f"n(B only) = {n_b} - {n_both} = {only_b}. Union count = {n_union}. P = {n_union}/{n_tot} = {fmt_frac(frac_union)}.",
        },
        misconception_tags=["did_not_subtract_intersection_from_circle_totals"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 14: Construct Venn Diagram with 'Neither' Count Given (Emits SVG)
def arch_14_venn_2_construct_with_neither_count(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_tot = r.choice([60, 70, 80, 100])
    outside = r.randint(10, 20)
    n_union = n_tot - outside

    n_both = r.randint(10, 18)
    only_a = r.randint(12, 25)
    only_b = n_union - only_a - n_both
    n_a = only_a + n_both
    n_b = only_b + n_both

    diag_svg = venn_2_svg(only_a=only_a, only_b=only_b, both=n_both, outside=outside, label_a="A", label_b="B", title="Two-Set Venn Diagram")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Two-Set Venn Diagram", "diagram_role": "context"}

    frac_both = Fraction(n_both, n_tot)

    prompt = (
        f"A group of {n_tot} learners were surveyed. It was found that:\n"
        f"- {n_a} learners like tea ($A$).\n"
        f"- {n_b} learners like coffee ($B$).\n"
        f"- {outside} learners like neither tea nor coffee.\n\n"
        f"1. Calculate the number of learners who like both tea and coffee. (2)\n"
        f"2. Hence, calculate the probability that a learner selected at random likes both tea and coffee. (1)"
    )
    prompt_latex = rf"\text{{Survey of }} {n_tot}: n(A) = {n_a}, n(B) = {n_b}, n(\text{{neither}}) = {outside}. \text{{ Find }} n(A \cap B) \text{{ and }} P(A \cap B)."

    steps = [
        step(from_latex=rf"n(A \cup B) = n(S) - n(\text{{neither}})", to_latex_str=rf"{n_tot} - {outside} = {n_union}", op="calculate union by subtracting neither count from total", rule="complement subtraction",),
        step(from_latex=r"n(A \cap B) = n(A) + n(B) - n(A \cup B)", to_latex_str=rf"{n_a} + {n_b} - {n_union} = {n_both}", op="solve for intersection cardinality", rule="inclusion-exclusion principle",),
        step(from_latex=rf"P(A \cap B) = \frac{{{n_both}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_both), op="convert to probability fraction", rule="probability definition",),
    ]
    canonical = solution_graph(
        goal="determine intersection count and probability from neither count",
        steps=steps,
        final_latex=rf"n(A \cap B) = {n_both}; \quad P(A \cap B) = {fmt_frac(frac_both)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct union count n(A ∪ B) = {n_union}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate intersection count n(A ∩ B) = {n_both}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Probability P(A ∩ B) = {fmt_frac(frac_both)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_14",
        topic=TOPIC_NAME,
        subskill="14_venn_2_construct_with_neither_count",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_both),
        sample_answer=rf"n(A \cap B) = {n_both}; \quad P(A \cap B) = {fmt_frac(frac_both)}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "First find how many learners are inside the circles: total minus neither.",
            "concept": "n(A ∩ B) = n(A) + n(B) - n(A ∪ B).",
            "breakdown": f"n(A ∪ B) = {n_tot} - {outside} = {n_union}. Intersection = {n_a} + {n_b} - {n_union} = {n_both}. P = {n_both}/{n_tot} = {fmt_frac(frac_both)}.",
        },
        misconception_tags=["forgot_to_subtract_neither_from_sample_space"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 15: Two-Set Venn Diagram — 'At Most One' Probability (Emits SVG)
def arch_15_venn_2_find_at_most_one(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    only_a = r.randint(18, 28)
    both = r.randint(12, 22)
    only_b = r.randint(15, 25)
    outside = r.randint(10, 20)
    n_tot = only_a + both + only_b + outside

    # 'at most one' = only_a + only_b + outside = n_tot - both
    n_at_most_one = n_tot - both
    frac_ans = Fraction(n_at_most_one, n_tot)

    diag_svg = venn_2_svg(only_a=only_a, only_b=only_b, both=both, outside=outside, label_a="A", label_b="B", title="Two-Set Venn Diagram")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Two-Set Venn Diagram", "diagram_role": "context"}

    prompt = (
        f"Refer to the Venn diagram below showing the distribution of {n_tot} participants in sample space $S$.\n\n"
        f"Calculate the probability that a randomly chosen participant is involved in AT MOST ONE of the two events ($A$ or $B$). "
        f"Write your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Refer to Venn diagram. Calculate }} P(\text{{at most one of }} A \text{{ or }} B)."

    steps = [
        step(from_latex=r"\text{At most one} = \text{Only } A + \text{Only } B + \text{Neither}", to_latex_str=rf"{only_a} + {only_b} + {outside} = {n_at_most_one}", op="sum regions with 0 or 1 event", rule="at most one event definition",),
        step(from_latex=rf"P(\text{{at most one}}) = \frac{{{n_at_most_one}}}{{{n_tot}}} = 1 - \frac{{{both}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_ans), op="evaluate probability fraction", rule="complement of intersection",),
    ]
    canonical = solution_graph(
        goal="determine probability of at most one event from Venn diagram",
        steps=steps,
        final_latex=fmt_frac(frac_ans),
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct favorable count n(at most one) = {n_at_most_one} or 1 - P(both)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate simplified fraction {fmt_frac(frac_ans)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_15",
        topic=TOPIC_NAME,
        subskill="15_venn_2_find_at_most_one",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_ans),
        sample_answer=fmt_frac(frac_ans),
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "'At most one' means 0 events or 1 event. Only the intersection (both) is excluded.",
            "concept": "P(at most one) = 1 - P(both) = (only A + only B + outside) / N.",
            "breakdown": f"Exclude both ({both}). Favorable count = {n_tot} - {both} = {n_at_most_one}. P = {n_at_most_one}/{n_tot} = {fmt_frac(frac_ans)}.",
        },
        misconception_tags=["excluded_neither_from_at_most_one"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 16: Algebraic Unknown x in Venn Intersection (Emits SVG)
def arch_16_venn_2_algebraic_x_intersection(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    n_tot = r.choice([80, 90, 100, 120])
    x_val = r.randint(12, 25)
    outside = r.randint(10, 20)
    only_a = r.randint(18, 30)
    only_b = n_tot - outside - x_val - only_a

    n_a = only_a + x_val
    n_b = only_b + x_val

    diag_svg = venn_2_svg(
        only_a=rf"{n_a} - x",
        only_b=rf"{n_b} - x",
        both="x",
        outside=str(outside),
        label_a="A",
        label_b="B",
        title="Venn Diagram with Unknown Intersection x",
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Algebraic Venn Diagram", "diagram_role": "context"}

    frac_only_b = Fraction(only_b, n_tot)

    prompt = (
        f"A group of {n_tot} learners were asked about their involvement in two cultural activities, $A$ and $B$.\n"
        f"- $n(A) = {n_a}$\n"
        f"- $n(B) = {n_b}$\n"
        f"- $n(A \\cap B) = x$\n"
        f"- {outside} learners participate in neither activity.\n\n"
        f"1. Set up an equation in terms of $x$ and show that $x = {x_val}$. (2)\n"
        f"2. Hence, calculate the probability that a learner chosen at random participates in activity $B$ ONLY. (2)"
    )
    prompt_latex = rf"\text{{Total }} {n_tot}, n(A) = {n_a}, n(B) = {n_b}, n(A \cap B) = x, n(\text{{neither}}) = {outside}. \text{{ Solve for }} x \text{{ and find }} P(B\text{{ only}})."

    steps = [
        step(from_latex=rf"({n_a} - x) + x + ({n_b} - x) + {outside} = {n_tot}", to_latex_str=rf"{n_a + n_b + outside} - x = {n_tot}", op="sum all 4 disjoint regions to equal total sample space", rule="linear equation setup",),
        step(from_latex=rf"x = {n_a + n_b + outside} - {n_tot}", to_latex_str=rf"x = {x_val}", op="solve linear equation for x", rule="algebraic solution",),
        step(from_latex=rf"n(B\text{{ only}}) = {n_b} - {x_val} = {only_b}", to_latex_str=rf"P(B\text{{ only}}) = \frac{{{only_b}}}{{{n_tot}}} = {fmt_frac(frac_only_b)}", op="substitute x to find only B probability", rule="probability evaluation",),
    ]
    canonical = solution_graph(
        goal="solve for unknown x in Venn intersection and compute B only probability",
        steps=steps,
        final_latex=rf"x = {x_val}; \quad P(B\text{{ only}}) = {fmt_frac(frac_only_b)}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct equation setup: ({n_a} - x) + x + ({n_b} - x) + {outside} = {n_tot}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate solution x = {x_val}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Number in B only = {only_b}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Probability P(B only) = {fmt_frac(frac_only_b)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_16",
        topic=TOPIC_NAME,
        subskill="16_venn_2_algebraic_x_intersection",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"x = {x_val}; \quad {fmt_frac(frac_only_b)}",
        sample_answer=rf"x = {x_val}; \quad P(B\text{{ only}}) = {fmt_frac(frac_only_b)}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "The sum of the 4 regions: (n(A) - x) + x + (n(B) - x) + outside must equal N.",
            "concept": "Total = only A + intersection + only B + outside.",
            "breakdown": f"({n_a} - x) + x + ({n_b} - x) + {outside} = {n_tot} ==> {n_a + n_b + outside} - x = {n_tot} ==> x = {x_val}. n(B only) = {n_b} - {x_val} = {only_b}. P = {only_b}/{n_tot} = {fmt_frac(frac_only_b)}.",
        },
        misconception_tags=["double_counted_x_in_algebraic_sum"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 17: Algebraic Unknown with Ratio / Multiple of x (Emits SVG)
def arch_17_venn_2_algebraic_x_with_ratio(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    # only_a = 2x, both = x, only_b = 3x, outside = 10
    n_outside = r.choice([8, 10, 12, 16])
    x_val = r.choice([6, 8, 10, 12])
    k_a = 2
    k_b = 3
    only_a = k_a * x_val
    only_b = k_b * x_val
    both = x_val
    n_tot = only_a + both + only_b + n_outside

    diag_svg = venn_2_svg(
        only_a=f"{k_a}x",
        only_b=f"{k_b}x",
        both="x",
        outside=str(n_outside),
        label_a="A",
        label_b="B",
        title="Venn Diagram with Algebraic Multiples of x",
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Algebraic Multiples Venn Diagram", "diagram_role": "context"}

    prompt = (
        f"In a survey of {n_tot} consumers, the numbers of people purchasing brand $A$ only, "
        f"brand $B$ only, and both brands are represented in terms of $x$ as shown in the Venn diagram below. "
        f"Exactly {n_outside} people purchase neither brand.\n\n"
        f"1. Determine the value of $x$. (2)\n"
        f"2. Calculate the probability that a consumer purchases brand $A$. (2)"
    )
    prompt_latex = rf"\text{{Solve for }} x \text{{ from }} 2x + x + 3x + {n_outside} = {n_tot}\text{{, and find }} P(A)."

    pa_count = only_a + both
    frac_pa = Fraction(pa_count, n_tot)

    steps = [
        step(from_latex=rf"{k_a}x + x + {k_b}x + {n_outside} = {n_tot}", to_latex_str=rf"{k_a + 1 + k_b}x + {n_outside} = {n_tot}", op="combine like terms in linear equation", rule="algebraic summation",),
        step(from_latex=rf"{k_a + 1 + k_b}x = {n_tot - n_outside}", to_latex_str=rf"x = {x_val}", op="divide to solve for x", rule="linear equation solution",),
        step(from_latex=rf"n(A) = {k_a}({x_val}) + {x_val} = {pa_count}", to_latex_str=rf"P(A) = \frac{{{pa_count}}}{{{n_tot}}} = {fmt_frac(frac_pa)}", op="compute probability of event A", rule="probability definition",),
    ]
    canonical = solution_graph(
        goal="solve for x and compute event A probability",
        steps=steps,
        final_latex=rf"x = {x_val}; \quad P(A) = {fmt_frac(frac_pa)}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": rf"Equation setup {k_a}x + x + {k_b}x + {n_outside} = {n_tot}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Value x = {x_val}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Cardinality n(A) = {pa_count}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate probability P(A) = {fmt_frac(frac_pa)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_17",
        topic=TOPIC_NAME,
        subskill="17_venn_2_algebraic_x_with_ratio",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"x = {x_val}; \quad {fmt_frac(frac_pa)}",
        sample_answer=rf"x = {x_val}; \quad P(A) = {fmt_frac(frac_pa)}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "Add all 4 regions: 2x + x + 3x + outside = grand total.",
            "concept": "6x + outside = N ==> 6x = N - outside ==> x = (N - outside) / 6.",
            "breakdown": f"6x + {n_outside} = {n_tot} ==> 6x = {n_tot - n_outside} ==> x = {x_val}. n(A) = 3x = {pa_count}. P(A) = {pa_count}/{n_tot} = {fmt_frac(frac_pa)}.",
        },
        misconception_tags=["forgot_to_include_outside_in_sum"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 18: Algebraic Unknown in Probability Equations
def arch_18_venn_2_algebraic_x_probability_equation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    denom = r.choice([10, 12, 15, 20])
    x_num = r.randint(2, 4)
    p_x = Fraction(x_num, denom)
    p_a = Fraction(x_num + 3, denom)
    p_b = Fraction(x_num + 2, denom)
    p_union = p_a + p_b - p_x

    prompt = (
        f"Two events $A$ and $B$ are such that:\n"
        f"$$P(A) = {fmt_frac(p_a)}, \\quad P(B) = {fmt_frac(p_b)}, \\quad P(A \\cap B) = x, \\quad P(A \\cup B) = {fmt_frac(p_union)}$$\n\n"
        f"1. Write down an equation using the addition rule to solve for $x$. (1)\n"
        f"2. Hence, determine the value of $x$ as a simplified fraction. (2)"
    )
    prompt_latex = rf"P(A) = {fmt_frac(p_a)}, P(B) = {fmt_frac(p_b)}, P(A \cap B) = x, P(A \cup B) = {fmt_frac(p_union)}. \text{{ Solve for }} x."

    steps = [
        step(from_latex=r"P(A \cup B) = P(A) + P(B) - P(A \cap B)", to_latex_str=rf"{fmt_frac(p_union)} = {fmt_frac(p_a)} + {fmt_frac(p_b)} - x", op="substitute known probabilities into addition rule", rule="addition rule substitution",),
        step(from_latex=rf"x = {fmt_frac(p_a)} + {fmt_frac(p_b)} - {fmt_frac(p_union)}", to_latex_str=rf"x = {fmt_frac(p_x)}", op="isolate and calculate x", rule="fraction arithmetic",),
    ]
    canonical = solution_graph(
        goal="solve for unknown x using probability addition rule",
        steps=steps,
        final_latex=rf"x = {fmt_frac(p_x)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct equation setup: {fmt_frac(p_union)} = {fmt_frac(p_a)} + {fmt_frac(p_b)} - x", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Isolating x correctly", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified value x = {fmt_frac(p_x)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_18",
        topic=TOPIC_NAME,
        subskill="18_venn_2_algebraic_x_probability_equation",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_x),
        sample_answer=rf"x = {fmt_frac(p_x)}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Replace P(A ∩ B) with x in the addition formula.",
            "concept": "x = P(A) + P(B) - P(A ∪ B).",
            "breakdown": f"x = {fmt_frac(p_a)} + {fmt_frac(p_b)} - {fmt_frac(p_union)} = {fmt_frac(p_x)}.",
        },
        misconception_tags=["sign_error_solving_for_x"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 19: Contextual Venn Problem — Learner Exam Pass Rates (Emits SVG)
def arch_19_venn_2_word_problem_survey_pass_rates(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_tot = 120
    n_pass_both = r.randint(45, 65)
    only_maths = r.randint(20, 35)
    only_phys = r.randint(15, 30)
    failed_both = n_tot - (only_maths + n_pass_both + only_phys)

    n_maths = only_maths + n_pass_both
    n_phys = only_phys + n_pass_both

    diag_svg = venn_2_svg(
        only_a=only_maths,
        only_b=only_phys,
        both=n_pass_both,
        outside=failed_both,
        label_a="Maths",
        label_b="Physics",
        title="Pass Rates in Mathematics and Physics",
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Pass Rates Venn Diagram", "diagram_role": "context"}

    frac_both = Fraction(n_pass_both, n_tot)

    prompt = (
        f"In a mid-year examination, a group of {n_tot} Grade 11 learners wrote examinations in Mathematics and Physical Sciences:\n"
        f"- {n_maths} learners passed Mathematics.\n"
        f"- {n_phys} learners passed Physical Sciences.\n"
        f"- {failed_both} learners failed both subjects.\n\n"
        f"1. How many learners passed BOTH Mathematics and Physical Sciences? (2)\n"
        f"2. Calculate the probability that a learner chosen at random passed BOTH subjects. (1)"
    )
    prompt_latex = rf"\text{{Cohort of }} {n_tot}: n(M) = {n_maths}, n(P) = {n_phys}, n(\text{{failed both}}) = {failed_both}. \text{{ Find }} n(M \cap P) \text{{ and }} P(M \cap P)."

    steps = [
        step(from_latex=rf"n(M \cup P) = {n_tot} - {failed_both}", to_latex_str=rf"{n_tot - failed_both}", op="calculate learners passing at least one subject", rule="subtraction",),
        step(from_latex=rf"n(M \cap P) = {n_maths} + {n_phys} - {n_tot - failed_both}", to_latex_str=rf"{n_pass_both}", op="apply inclusion-exclusion formula", rule="inclusion-exclusion",),
        step(from_latex=rf"P(M \cap P) = \frac{{{n_pass_both}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_both), op="calculate probability fraction", rule="classical probability definition",),
    ]
    canonical = solution_graph(
        goal="determine number and probability passing both subjects",
        steps=steps,
        final_latex=rf"n(M \cap P) = {n_pass_both}; \quad P(M \cap P) = {fmt_frac(frac_both)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct union count n(M ∪ P) = {n_tot - failed_both}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct number passing both = {n_pass_both}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Probability = {fmt_frac(frac_both)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_19",
        topic=TOPIC_NAME,
        subskill="19_venn_2_word_problem_survey_pass_rates",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_both),
        sample_answer=rf"n(M \cap P) = {n_pass_both}; \quad P(M \cap P) = {fmt_frac(frac_both)}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "First find how many passed at least one subject: 120 minus failed both.",
            "concept": "n(both) = n(Maths) + n(Physics) - n(passed at least one).",
            "breakdown": f"Passed at least one = {n_tot - failed_both}. Both = {n_maths} + {n_phys} - {n_tot - failed_both} = {n_pass_both}. P = {n_pass_both}/{n_tot} = {fmt_frac(frac_both)}.",
        },
        misconception_tags=["confused_union_with_total_sample_space"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 20: Contextual Venn Problem — Device Ownership (Emits SVG)
def arch_20_venn_2_word_problem_device_ownership(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_tot = 80
    only_phone = r.randint(25, 38)
    both = r.randint(15, 25)
    only_tab = r.randint(10, 20)
    neither = n_tot - (only_phone + both + only_tab)

    diag_svg = venn_2_svg(
        only_a=only_phone,
        only_b=only_tab,
        both=both,
        outside=neither,
        label_a="Phone",
        label_b="Tablet",
        title="Device Ownership Survey",
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Device Ownership Venn Diagram", "diagram_role": "context"}

    frac_only_phone = Fraction(only_phone, n_tot)

    prompt = (
        f"A technology survey was conducted among {n_tot} learners regarding their device ownership:\n"
        f"- {only_phone + both} learners own a smartphone.\n"
        f"- {only_tab + both} learners own a tablet.\n"
        f"- {both} learners own both a smartphone and a tablet.\n\n"
        f"1. Determine how many learners own a smartphone ONLY. (1)\n"
        f"2. Calculate the probability that a randomly chosen learner owns a smartphone ONLY. "
        f"Write your answer as a simplified fraction. (2)"
    )
    prompt_latex = rf"\text{{Survey of }} {n_tot}: n(\text{{Phone}}) = {only_phone + both}, n(\text{{both}}) = {both}. \text{{ Find }} n(\text{{Phone only}}) \text{{ and }} P(\text{{Phone only}})."

    steps = [
        step(from_latex=rf"n(\text{{Phone only}}) = {only_phone + both} - {both}", to_latex_str=rf"{only_phone}", op="deduct intersection from total phone owners", rule="subtraction",),
        step(from_latex=rf"P(\text{{Phone only}}) = \frac{{{only_phone}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_only_phone), op="divide by total and simplify fraction", rule="classical probability definition",),
    ]
    canonical = solution_graph(
        goal="determine smartphone only count and probability",
        steps=steps,
        final_latex=rf"n(\text{{Phone only}}) = {only_phone}; \quad P(\text{{Phone only}}) = {fmt_frac(frac_only_phone)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct count n(Phone only) = {only_phone}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Fraction setup: {only_phone}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified fraction {fmt_frac(frac_only_phone)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_20",
        topic=TOPIC_NAME,
        subskill="20_venn_2_word_problem_device_ownership",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_only_phone),
        sample_answer=rf"n(\text{{Phone only}}) = {only_phone}; \quad P(\text{{Phone only}}) = {fmt_frac(frac_only_phone)}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "Subtract the learners who own both from the total who own a smartphone.",
            "concept": "n(Phone only) = n(Phone) - n(both).",
            "breakdown": f"n(Phone only) = {only_phone + both} - {both} = {only_phone}. P = {only_phone}/{n_tot} = {fmt_frac(frac_only_phone)}.",
        },
        misconception_tags=["gave_total_phone_instead_of_phone_only"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 21: Independent Events — Product Rule Definition
def arch_21_independent_events_product_rule_definition(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    pa_v = round(r.randint(2, 7) / 10, 1)
    pb_v = round(r.randint(2, 8) / 10, 1)
    prod_v = round(pa_v * pb_v, 2)
    prompt = (
        f"1. State the necessary and sufficient algebraic condition relating $P(A)$, $P(B)$, and $P(A \\cap B)$ for independent events $A$ and $B$. (1)\n"
        f"2. Hence, if $A$ and $B$ are independent with $P(A) = {num(pa_v, 1)}$ and $P(B) = {num(pb_v, 1)}$, calculate $P(A \\cap B)$. (1)"
    )
    prompt_latex = rf"\text{{State independence condition and calculate }} P(A \cap B) \text{{ if }} P(A)={num(pa_v,1)}, P(B)={num(pb_v,1)}."

    steps = [
        step(from_latex=r"P(A \cap B) = P(A) \times P(B)", to_latex_str=rf"P(A \cap B) = {num(pa_v, 1)} \times {num(pb_v, 1)} = {num(prod_v, 2)}", op="state formal mathematical product rule and evaluate", rule="independent events definition",),
    ]
    canonical = solution_graph(
        goal="state condition for independent events and evaluate product",
        steps=steps,
        final_latex=rf"P(A \cap B) = P(A) \times P(B) = {num(prod_v, 2)}",
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": "Accurate algebraic formula P(A ∩ B) = P(A) × P(B)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate product P(A ∩ B) = {num(prod_v, 2)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_21",
        topic=TOPIC_NAME,
        subskill="21_independent_events_product_rule_definition",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=num(prod_v, 2),
        sample_answer=rf"P(A \cap B) = P(A) \times P(B) = {num(prod_v, 2)}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Independent events multiply: the intersection probability equals the product of their individual probabilities.",
            "concept": "A and B are independent iff P(A ∩ B) = P(A) × P(B).",
            "breakdown": f"P(A ∩ B) = P(A) × P(B) = {num(pa_v, 1)} × {num(pb_v, 1)} = {num(prod_v, 2)}.",
        },
        misconception_tags=["confused_independent_with_mutually_exclusive"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=2,
    )


# Archetype 22: Testing Event Independence Given Probabilities
def arch_22_independent_events_test_given_probabilities(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    is_indep = r.choice([True, False])
    pa_val = r.choice([0.4, 0.5, 0.6])
    pb_val = r.choice([0.3, 0.5])
    prod = round(pa_val * pb_val, 3)

    if is_indep:
        p_both = prod
    else:
        # Deliberately different
        p_both = round(prod + r.choice([-0.05, 0.05, 0.08]), 3)

    pa_str = num(pa_val, 1)
    pb_str = num(pb_val, 1)
    pboth_str = num(p_both, 3)
    prod_str = num(prod, 3)

    verdict = "INDEPENDENT" if is_indep else "DEPENDENT"
    comp_sym = "=" if is_indep else rf"\neq"

    prompt = (
        f"For two events $A$ and $B$, it is given that:\n"
        f"$$P(A) = {pa_str}, \\quad P(B) = {pb_str}, \\quad P(A \\cap B) = {pboth_str}$$\n\n"
        f"Determine, showing full mathematical working, whether events $A$ and $B$ are independent or dependent."
    )
    prompt_latex = rf"P(A) = {pa_str}, P(B) = {pb_str}, P(A \cap B) = {pboth_str}. \text{{ Test if independent.}}"

    steps = [
        step(from_latex=r"P(A) \times P(B)", to_latex_str=rf"{pa_str} \times {pb_str} = {prod_str}", op="calculate product of individual probabilities", rule="multiplication",),
        step(from_latex=rf"P(A \cap B) {comp_sym} P(A) \times P(B)", to_latex_str=rf"{pboth_str} {comp_sym} {prod_str} \implies \text{{Events are }} \textbf{{{verdict}}}", op="compare intersection with product and conclude", rule="independence test",),
    ]
    canonical = solution_graph(
        goal="determine whether events are independent",
        steps=steps,
        final_latex=rf"\text{{{verdict}}}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Calculation of product P(A) × P(B) = {prod_str}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Comparison statement: {pboth_str} {comp_sym} {prod_str}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct conclusion: {verdict}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_22",
        topic=TOPIC_NAME,
        subskill="22_independent_events_test_given_probabilities",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"\text{{{verdict}}}",
        sample_answer=rf"P(A) \times P(B) = {prod_str}; \quad \text{{{verdict}}}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Calculate P(A) × P(B) and compare it to P(A ∩ B).",
            "concept": "If P(A ∩ B) = P(A) × P(B), the events are independent; otherwise they are dependent.",
            "breakdown": f"P(A) × P(B) = {pa_str} × {pb_str} = {prod_str}. P(A ∩ B) = {pboth_str}. Since {pboth_str} {comp_sym} {prod_str}, the events are {verdict}.",
        },
        misconception_tags=["checked_if_intersection_equals_zero_instead_of_product"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Archetype 23: Independent Events — Find Intersection & Union
def arch_23_independent_events_find_intersection(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    denom = r.choice([5, 8, 10, 12])
    num_a = r.randint(1, denom // 2)
    num_b = r.randint(1, denom // 2)
    p_a = Fraction(num_a, denom)
    p_b = Fraction(num_b, denom)

    p_both = p_a * p_b
    p_union = p_a + p_b - p_both

    prompt = (
        f"It is given that $A$ and $B$ are INDEPENDENT events such that:\n"
        f"$$P(A) = {fmt_frac(p_a)} \\quad \\text{{and}} \\quad P(B) = {fmt_frac(p_b)}$$\n\n"
        f"1. Calculate $P(A \\cap B)$. (2)\n"
        f"2. Calculate $P(A \\cup B)$. (2)"
    )
    prompt_latex = rf"A, B \text{{ independent: }} P(A) = {fmt_frac(p_a)}, P(B) = {fmt_frac(p_b)}. \text{{ Find }} P(A \cap B) \text{{ and }} P(A \cup B)."

    steps = [
        step(from_latex=r"P(A \cap B) = P(A) \times P(B)", to_latex_str=rf"{fmt_frac(p_a)} \times {fmt_frac(p_b)} = {fmt_frac(p_both)}", op="apply independent product rule", rule="product rule for independent events",),
        step(from_latex=r"P(A \cup B) = P(A) + P(B) - P(A \cap B)", to_latex_str=rf"{fmt_frac(p_a)} + {fmt_frac(p_b)} - {fmt_frac(p_both)} = {fmt_frac(p_union)}", op="apply addition rule with computed intersection", rule="addition rule",),
    ]
    canonical = solution_graph(
        goal="calculate intersection and union for independent events",
        steps=steps,
        final_latex=rf"P(A \cap B) = {fmt_frac(p_both)}; \quad P(A \cup B) = {fmt_frac(p_union)}",
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Product rule formula setup P(A ∩ B) = P(A) × P(B)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate intersection {fmt_frac(p_both)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Addition rule setup", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate union {fmt_frac(p_union)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_23",
        topic=TOPIC_NAME,
        subskill="23_independent_events_find_intersection",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_union),
        sample_answer=rf"P(A \cap B) = {fmt_frac(p_both)}; \quad P(A \cup B) = {fmt_frac(p_union)}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Because the events are independent, P(A and B) = P(A) × P(B). Then use the addition rule for the union.",
            "concept": "P(A ∩ B) = P(A) × P(B). P(A ∪ B) = P(A) + P(B) - P(A ∩ B).",
            "breakdown": f"Intersection = {fmt_frac(p_a)} × {fmt_frac(p_b)} = {fmt_frac(p_both)}. Union = {fmt_frac(p_a)} + {fmt_frac(p_b)} - {fmt_frac(p_both)} = {fmt_frac(p_union)}.",
        },
        misconception_tags=["assumed_mutually_exclusive_with_zero_intersection"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# Archetype 24: Independent Events — Solve for P(A) Given Union
def arch_24_independent_events_find_single_event(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    # P(A ∪ B) = P(A) + P(B) - P(A)*P(B) = P(A)(1 - P(B)) + P(B)
    # P(A) = (P(A ∪ B) - P(B)) / (1 - P(B))
    pb_val = r.choice([Fraction(1, 3), Fraction(1, 4), Fraction(2, 5), Fraction(1, 2)])
    pa_val = r.choice([Fraction(1, 4), Fraction(1, 3), Fraction(3, 5), Fraction(2, 3)])
    p_both = pa_val * pb_val
    p_union = pa_val + pb_val - p_both

    prompt = (
        f"Two events $A$ and $B$ are INDEPENDENT.\n"
        f"It is given that $P(B) = {fmt_frac(pb_val)}$ and $P(A \\cup B) = {fmt_frac(p_union)}$.\n\n"
        f"Calculate $P(A)$. Write your answer as a simplified fraction."
    )
    prompt_latex = rf"A, B \text{{ independent: }} P(B) = {fmt_frac(pb_val)}, P(A \cup B) = {fmt_frac(p_union)}. \text{{ Find }} P(A)."

    steps = [
        step(from_latex=r"P(A \cup B) = P(A) + P(B) - P(A) \cdot P(B)", to_latex_str=rf"{fmt_frac(p_union)} = P(A) + {fmt_frac(pb_val)} - P(A)\left({fmt_frac(pb_val)}\right)", op="substitute independent product into addition rule", rule="independent addition rule",),
        step(from_latex=rf"{fmt_frac(p_union)} - {fmt_frac(pb_val)} = P(A)\left(1 - {fmt_frac(pb_val)}\right)", to_latex_str=rf"{fmt_frac(p_union - pb_val)} = P(A)\left({fmt_frac(1 - pb_val)}\right)", op="factor out P(A)", rule="common factor grouping",),
        step(from_latex=rf"P(A) = \frac{{{fmt_frac(p_union - pb_val)}}}{{{fmt_frac(1 - pb_val)}}}", to_latex_str=fmt_frac(pa_val), op="divide to solve for P(A)", rule="fraction division",),
    ]
    canonical = solution_graph(
        goal="solve for P(A) given independence and union",
        steps=steps,
        final_latex=fmt_frac(pa_val),
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Substitution P(A ∩ B) = P(A) × P(B)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Factoring out P(A)[1 - P(B)]", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Isolating P(A)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate fraction P(A) = {fmt_frac(pa_val)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_24",
        topic=TOPIC_NAME,
        subskill="24_independent_events_find_single_event",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(pa_val),
        sample_answer=fmt_frac(pa_val),
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Replace P(A ∩ B) with P(A) · P(B), then factor out P(A): P(A ∪ B) - P(B) = P(A)(1 - P(B)).",
            "concept": "P(A) = [P(A ∪ B) - P(B)] / [1 - P(B)].",
            "breakdown": f"P(A ∪ B) - P(B) = {fmt_frac(p_union - pb_val)}. 1 - P(B) = {fmt_frac(1 - pb_val)}. P(A) = {fmt_frac(p_union - pb_val)} / {fmt_frac(1 - pb_val)} = {fmt_frac(pa_val)}.",
        },
        misconception_tags=["failed_to_factor_out_p_a"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
    )


# Archetype 25: Independent Events — Dice and Coins Experiment
def arch_25_independent_events_dice_and_coins(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    coin_outcome = r.choice(["Heads", "Tails"])
    target_condition = r.choice(["prime number", "even number", "number greater than 4"])

    p_coin = Fraction(1, 2)
    if target_condition == "prime number":
        favorable_die = [2, 3, 5]
    elif target_condition == "even number":
        favorable_die = [2, 4, 6]
    else:  # greater than 4
        favorable_die = [5, 6]

    p_die = Fraction(len(favorable_die), 6)
    p_both = p_coin * p_die

    prompt = (
        f"A fair six-sided die is rolled and a fair coin is tossed simultaneously.\n\n"
        f"1. Explain why the result on the coin and the result on the die are independent events. (1)\n"
        f"2. Calculate the probability of getting {coin_outcome} on the coin AND a {target_condition} on the die. "
        f"Give your answer as a simplified fraction. (2)"
    )
    prompt_latex = rf"\text{{Roll die and toss coin. Find }} P(\text{{{coin_outcome and {target_condition}}}})."

    steps = [
        step(from_latex=r"\text{The outcome of rolling the die has no influence on the coin toss}", to_latex_str=r"\text{Independent events}", op="state physical independence of independent trials", rule="physical independence",),
        step(from_latex=rf"P(\text{{{coin_outcome}}}) = \frac{{1}}{{2}}, \quad P(\text{{{target_condition}}}) = \frac{{{len(favorable_die)}}}{{6}} = {fmt_frac(p_die)}", to_latex_str=rf"P(\text{{Both}}) = \frac{{1}}{{2}} \times {fmt_frac(p_die)} = {fmt_frac(p_both)}", op="multiply independent probabilities", rule="product rule",),
    ]
    canonical = solution_graph(
        goal="determine joint probability of independent coin and die outcomes",
        steps=steps,
        final_latex=fmt_frac(p_both),
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Statement that one outcome does not affect the other", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Individual probabilities: 1/2 and {fmt_frac(p_die)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate joint product {fmt_frac(p_both)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_25",
        topic=TOPIC_NAME,
        subskill="25_independent_events_dice_and_coins",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_both),
        sample_answer=fmt_frac(p_both),
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Because the coin and die do not affect each other, multiply their probabilities: P(coin) × P(die).",
            "concept": "P(A and B) = P(A) × P(B).",
            "breakdown": f"P({coin_outcome}) = 1/2. Favorable die outcomes: {favorable_die}, so P(die) = {len(favorable_die)}/6 = {fmt_frac(p_die)}. Joint P = 1/2 × {fmt_frac(p_die)} = {fmt_frac(p_both)}.",
        },
        misconception_tags=["added_probabilities_of_independent_trials"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# Export Dictionary for Archetypes 01 to 25
ARCHETYPE_BUILDERS_01_25 = {
    "01_single_event_sample_space_and_probability": arch_01_single_event_sample_space_and_probability,
    "02_complementary_event_probability": arch_02_complementary_event_probability,
    "03_mutually_exclusive_two_events_addition": arch_03_mutually_exclusive_two_events_addition,
    "04_mutually_exclusive_three_events": arch_04_mutually_exclusive_three_events,
    "05_addition_rule_find_union": arch_05_addition_rule_find_union,
    "06_addition_rule_find_intersection": arch_06_addition_rule_find_intersection,
    "07_addition_rule_find_single_event": arch_07_addition_rule_find_single_event,
    "08_addition_rule_word_problem_sports_or_subjects": arch_08_addition_rule_word_problem_sports_or_subjects,
    "09_addition_rule_with_percentages": arch_09_addition_rule_with_percentages,
    "10_addition_rule_with_frequencies": arch_10_addition_rule_with_frequencies,
    "11_venn_2_counts_read_regions": arch_11_venn_2_counts_read_regions,
    "12_venn_2_probabilities_read_regions": arch_12_venn_2_probabilities_read_regions,
    "13_venn_2_construct_from_cardinalities": arch_13_venn_2_construct_from_cardinalities,
    "14_venn_2_construct_with_neither_count": arch_14_venn_2_construct_with_neither_count,
    "15_venn_2_find_at_most_one": arch_15_venn_2_find_at_most_one,
    "16_venn_2_algebraic_x_intersection": arch_16_venn_2_algebraic_x_intersection,
    "17_venn_2_algebraic_x_with_ratio": arch_17_venn_2_algebraic_x_with_ratio,
    "18_venn_2_algebraic_x_probability_equation": arch_18_venn_2_algebraic_x_probability_equation,
    "19_venn_2_word_problem_survey_pass_rates": arch_19_venn_2_word_problem_survey_pass_rates,
    "20_venn_2_word_problem_device_ownership": arch_20_venn_2_word_problem_device_ownership,
    "21_independent_events_product_rule_definition": arch_21_independent_events_product_rule_definition,
    "22_independent_events_test_given_probabilities": arch_22_independent_events_test_given_probabilities,
    "23_independent_events_find_intersection": arch_23_independent_events_find_intersection,
    "24_independent_events_find_single_event": arch_24_independent_events_find_single_event,
    "25_independent_events_dice_and_coins": arch_25_independent_events_dice_and_coins,
}
