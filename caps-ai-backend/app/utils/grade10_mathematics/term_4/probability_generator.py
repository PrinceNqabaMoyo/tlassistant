"""Grade 10 Mathematics — Term 4: Probability (Deterministic 6-Pillar Generator).
100% aligned with South African CAPS Curriculum (Grade 10 Mathematics Paper 1: Probability).
Covers:
- Relative frequency and theoretical probability: P(E) = n(E) / n(S)
- Two-event Venn diagrams: union, intersection, and complement
- Addition rule for any two events: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- Mutually exclusive events: P(A ∩ B) = 0 => P(A ∪ B) = P(A) + P(B)
- Complementary events: P(not A) = 1 - P(A)

Zero-LLM: 100% deterministic Python calculations with South African comma decimals ({,}).
"""
from __future__ import annotations

from fractions import Fraction
import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "Probability"
TOPIC_ID = "grade10_math_probability"
LO = "math10_probability_venn"


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_frac(f: Fraction) -> str:
    if f.denominator == 1:
        return str(f.numerator)
    return rf"\frac{{{f.numerator}}}{{{f.denominator}}}"


def _build_venn_diagram_drill(r: random.Random) -> Dict[str, Any]:
    total = r.choice([80, 100, 120, 150])
    inter = r.randint(12, 28)
    only_a = r.randint(20, total // 2 - inter)
    only_b = r.randint(18, total // 2 - inter)
    neither = total - (only_a + only_b + inter)

    tot_a = only_a + inter
    tot_b = only_b + inter

    context_type = r.choice([
        ("play Soccer", "play Cricket", "S", "C"),
        ("study History", "study Geography", "H", "G"),
        ("take Art", "take Music", "A", "M"),
    ])
    act_a, act_b, sym_a, sym_b = context_type

    p_union = Fraction(only_a + inter + only_b, total)

    prompt = (
        rf"In a survey of {total} Grade 10 learners at a South African school:\n\n"
        rf"- {tot_a} learners {act_a} ({sym_a})\n"
        rf"- {tot_b} learners {act_b} ({sym_b})\n"
        rf"- {inter} learners do BOTH\n"
        rf"- {neither} learners do NEITHER\n\n"
        rf"1. Calculate the number of learners who {act_a} ONLY.\n"
        rf"2. Calculate the probability $P({sym_a} \cup {sym_b})$ that a randomly chosen learner does AT LEAST ONE of the activities.\n"
        rf"3. State whether events {sym_a} and {sym_b} are mutually exclusive. Give a reason."
    )

    worked = (
        rf"**1. {act_a} ONLY:** $n({sym_a} \text{{ only}}) = n({sym_a}) - n({sym_a} \cap {sym_b}) = {tot_a} - {inter} = {only_a}$"
        rf"\n\n**2. Union Probability:**"
        rf"$$P({sym_a} \cup {sym_b}) = \frac{{{only_a} + {inter} + {only_b}}}{{{total}}} = \frac{{{only_a + inter + only_b}}}{{{total}}} = {_fmt_frac(p_union)}$$"
        rf"\n\n**3. Mutually Exclusive:** No, because $n({sym_a} \cap {sym_b}) = {inter} \neq 0$ (the events can happen at the same time)."
    )

    ans_str = f"{sym_a} only: {only_a}, P(union): {_fmt_frac(p_union)}, Mutually exclusive: No"

    return {
        "id": f"g10_prob_venn_{r.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans_str,
        "answer_latex": rf"n({sym_a}\text{{ only}}) = {only_a}, \, P({sym_a} \cup {sym_b}) = {_fmt_frac(p_union)}, \, \text{{Not mutually exclusive}}",
        "worked_solution": worked,
        "marks": 5,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "two_event_venn",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": f"Learners who {act_a} only ({only_a})", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Probability of union ({_fmt_frac(p_union)})", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct mutually exclusive classification and reason", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Draw a two-circle Venn diagram and fill in the middle intersection first.",
            "2_concept": "Learners in event A only = total in A minus the intersection.",
            "3_breakdown": rf"A only = {tot_a} - {inter} = {only_a}. Union = {only_a + inter + only_b}. P(union) = {_fmt_frac(p_union)}.",
        },
        "misconception_tags": ["union_intersection_double_count", "mutually_exclusive_confusion"],
    }


def _build_addition_rule_drill(r: random.Random) -> Dict[str, Any]:
    is_mutually_exclusive = r.choice([True, False])
    denom = r.choice([10, 12, 15, 20])

    num_a = r.randint(2, denom // 2)
    p_a = Fraction(num_a, denom)

    if is_mutually_exclusive:
        num_b = r.randint(2, denom - num_a - 1)
        p_b = Fraction(num_b, denom)
        p_union = p_a + p_b

        prompt = (
            rf"Given two mutually exclusive events $A$ and $B$, such that "
            rf"$P(A) = {_fmt_frac(p_a)}$ and $P(B) = {_fmt_frac(p_b)}$.\n\n"
            rf"1. Write down the value of $P(A \cap B)$.\n"
            rf"2. Calculate $P(A \cup B)$."
        )

        worked = (
            rf"**1. Intersection:** For mutually exclusive events, $P(A \cap B) = 0$."
            rf"\n\n**2. Union:** $P(A \cup B) = P(A) + P(B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} = {_fmt_frac(p_union)}$"
        )

        ans_str = f"P(A ∩ B) = 0, P(A ∪ B) = {_fmt_frac(p_union)}"
    else:
        num_inter = r.randint(1, min(num_a - 1, 3))
        p_inter = Fraction(num_inter, denom)
        num_b = r.randint(num_inter + 1, denom - num_a + num_inter - 1)
        p_b = Fraction(num_b, denom)
        p_union = p_a + p_b - p_inter
        p_not_a = 1 - p_a

        prompt = (
            rf"Given two events $A$ and $B$ in a sample space $S$, such that "
            rf"$P(A) = {_fmt_frac(p_a)}$, $P(B) = {_fmt_frac(p_b)}$, and "
            rf"$P(A \cap B) = {_fmt_frac(p_inter)}$.\n\n"
            rf"1. Calculate $P(A \cup B)$.\n"
            rf"2. Calculate $P(\text{{not }} A)$."
        )

        worked = (
            rf"**1. Addition Rule:** $$P(A \cup B) = P(A) + P(B) - P(A \cap B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} - {_fmt_frac(p_inter)} = {_fmt_frac(p_union)}$$"
            rf"\n\n**2. Complement:** $$P(A') = 1 - P(A) = 1 - {_fmt_frac(p_a)} = {_fmt_frac(p_not_a)}$$"
        )

        ans_str = f"P(A ∪ B) = {_fmt_frac(p_union)}, P(not A) = {_fmt_frac(p_not_a)}"

    return {
        "id": f"g10_prob_add_{r.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans_str,
        "answer_latex": ans_str,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "addition_rule",
        "term": 4,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 4,
        "difficulty": "easy" if is_mutually_exclusive else "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "First sub-question calculation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Second sub-question calculation", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": r"Use the addition rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.",
            "2_concept": r"If events are mutually exclusive, $P(A \cap B) = 0$. For complementary events, $P(A') = 1 - P(A)$.",
            "3_breakdown": rf"Substitute into formula: result is {ans_str}.",
        },
        "misconception_tags": ["addition_rule_formula_error"],
    }


def generate(subskill: Optional[str] = None, difficulty: str = "medium", count: int = 1, seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    r = _rng(seed)
    generators = [_build_venn_diagram_drill, _build_addition_rule_drill]
    if subskill == "two_event_venn":
        generators = [_build_venn_diagram_drill]
    elif subskill == "addition_rule":
        generators = [_build_addition_rule_drill]

    questions = []
    for _ in range(count):
        gen_fn = r.choice(generators)
        questions.append(gen_fn(r))
    return questions
