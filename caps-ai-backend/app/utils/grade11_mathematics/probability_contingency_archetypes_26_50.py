"""Grade 11 Mathematics — Probability Archetypes 26 to 50.
Part 2 of 2: Grounded in official South African curriculum standards:
- Three-set Venn diagrams with reading regions, solving for central unknown x, and computing compound probabilities.
- Two-way contingency tables: completing missing cells, calculating joint/marginal probabilities, and formal independence testing P(A and B) = P(A) * P(B).
- Tree diagrams for multi-stage experiments: independent (with replacement) vs dependent (without replacement).
- Comprehensive exam capstones synthesizing Venn diagrams, contingency tables, and algebraic proofs.
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
from .probability_contingency_archetypes_01_25 import (
    LEARNING_OBJECTIVE_ID,
    SA_NAMES,
    SUBJECT_PAIRS,
    TOPIC_ID,
    TOPIC_NAME,
    fmt_frac,
    venn_2_svg,
)


def venn_3_svg(
    only_a: Any,
    only_b: Any,
    only_c: Any,
    ab: Any,
    ac: Any,
    bc: Any,
    abc: Any,
    outside: Any,
    label_a: str = "A",
    label_b: str = "B",
    label_c: str = "C",
    title: str = "Three-Set Venn Diagram",
) -> str:
    """Generate publication-grade 3-circle Venn diagram SVG."""
    w, h = 540, 420
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">',
        f'<rect x="15" y="25" width="{w-30}" height="{h-40}" rx="12" fill="#ffffff" stroke="#334155" stroke-width="2"/>',
        f'<text x="35" y="52" font-size="16" font-weight="bold" fill="#0f172a">S</text>',
        f'<text x="{w//2}" y="20" font-size="13" font-weight="bold" fill="#334155" text-anchor="middle">{title}</text>',
        # Circle A (top-left)
        '<circle cx="220" cy="180" r="105" fill="#3b82f6" fill-opacity="0.16" stroke="#1d4ed8" stroke-width="2.5"/>',
        # Circle B (top-right)
        '<circle cx="320" cy="180" r="105" fill="#10b981" fill-opacity="0.16" stroke="#047857" stroke-width="2.5"/>',
        # Circle C (bottom)
        '<circle cx="270" cy="270" r="105" fill="#f59e0b" fill-opacity="0.16" stroke="#d97706" stroke-width="2.5"/>',
        # Set Labels
        f'<text x="150" y="100" font-size="14" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{label_a}</text>',
        f'<text x="390" y="100" font-size="14" font-weight="bold" fill="#047857" text-anchor="middle">{label_b}</text>',
        f'<text x="270" y="400" font-size="14" font-weight="bold" fill="#d97706" text-anchor="middle">{label_c}</text>',
        # Region values
        f'<text x="180" y="150" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">{only_a}</text>',
        f'<text x="360" y="150" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">{only_b}</text>',
        f'<text x="270" y="345" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">{only_c}</text>',
        f'<text x="270" y="145" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">{ab}</text>',
        f'<text x="215" y="240" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">{ac}</text>',
        f'<text x="325" y="240" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">{bc}</text>',
        f'<text x="270" y="215" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">{abc}</text>',
        f'<text x="470" y="375" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">{outside}</text>',
        '</svg>',
    ]
    return "".join(parts)


def tree_2_svg(
    p_b1: str,
    p_b2: str,
    p_b1_b1: str,
    p_b1_b2: str,
    p_b2_b1: str,
    p_b2_b2: str,
    lbl1: str = "A",
    lbl2: str = "B",
    title: str = "Two-Stage Probability Tree Diagram",
) -> str:
    """Generate publication-grade 2-stage tree diagram SVG."""
    w, h = 540, 280
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">',
        f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="10" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>',
        f'<text x="{w//2}" y="28" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">{title}</text>',
        # Stage 1 branches from (60, 140)
        '<line x1="60" y1="140" x2="220" y2="75" stroke="#2563eb" stroke-width="2"/>',
        '<line x1="60" y1="140" x2="220" y2="205" stroke="#2563eb" stroke-width="2"/>',
        f'<text x="130" y="95" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{p_b1}</text>',
        f'<text x="130" y="190" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{p_b2}</text>',
        f'<circle cx="220" cy="75" r="5" fill="#1d4ed8"/>',
        f'<circle cx="220" cy="205" r="5" fill="#1d4ed8"/>',
        f'<text x="220" y="62" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">{lbl1}</text>',
        f'<text x="220" y="225" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">{lbl2}</text>',
        # Stage 2 branches from top node (220, 75)
        '<line x1="220" y1="75" x2="380" y2="45" stroke="#059669" stroke-width="2"/>',
        '<line x1="220" y1="75" x2="380" y2="105" stroke="#059669" stroke-width="2"/>',
        f'<text x="300" y="52" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">{p_b1_b1}</text>',
        f'<text x="300" y="105" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">{p_b1_b2}</text>',
        f'<text x="400" y="49" font-size="12" font-weight="bold" fill="#0f172a">{lbl1}</text>',
        f'<text x="400" y="109" font-size="12" font-weight="bold" fill="#0f172a">{lbl2}</text>',
        # Stage 2 branches from bottom node (220, 205)
        '<line x1="220" y1="205" x2="380" y2="175" stroke="#059669" stroke-width="2"/>',
        '<line x1="220" y1="205" x2="380" y2="235" stroke="#059669" stroke-width="2"/>',
        f'<text x="300" y="182" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">{p_b2_b1}</text>',
        f'<text x="300" y="235" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">{p_b2_b2}</text>',
        f'<text x="400" y="179" font-size="12" font-weight="bold" fill="#0f172a">{lbl1}</text>',
        f'<text x="400" y="239" font-size="12" font-weight="bold" fill="#0f172a">{lbl2}</text>',
        '</svg>',
    ]
    return "".join(parts)


# --------------------------------------------------------------------------- #
# Archetype 26: Three-Set Venn Diagram — Reading All Three and None
# --------------------------------------------------------------------------- #
def arch_26_venn_3_read_all_three_and_none(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    only_a = r.randint(15, 25)
    only_b = r.randint(12, 22)
    only_c = r.randint(14, 24)
    ab = r.randint(6, 12)
    ac = r.randint(5, 10)
    bc = r.randint(7, 12)
    abc = r.randint(4, 9)
    outside = r.randint(10, 20)
    n_tot = only_a + only_b + only_c + ab + ac + bc + abc + outside

    diag_svg = venn_3_svg(only_a, only_b, only_c, ab, ac, bc, abc, outside, "A", "B", "C", "Three-Set Venn Diagram")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Three-Set Venn Diagram", "diagram_role": "context"}

    frac_all_three = Fraction(abc, n_tot)
    frac_none = Fraction(outside, n_tot)

    prompt = (
        f"The Venn diagram below displays the distribution of {n_tot} learners in sample space $S$ "
        f"across three events $A$, $B$, and $C$.\n\n"
        f"1. Calculate the probability that a learner participates in ALL THREE events, $P(A \\cap B \\cap C)$. (2)\n"
        f"2. Calculate the probability that a learner participates in NONE of the three events. (1)"
    )
    prompt_latex = rf"\text{{Read 3-set Venn with }} N={n_tot}. \text{{ Find }} P(A \cap B \cap C) \text{{ and }} P(\text{{none}})."

    steps = [
        step(
            from_latex=rf"P(A \cap B \cap C) = \frac{{n(A \cap B \cap C)}}{{n(S)}} = \frac{{{abc}}}{{{n_tot}}}",
            to_latex_str=fmt_frac(frac_all_three),
            op="read central intersection count and simplify",
            rule="classical probability definition",
        ),
        step(
            from_latex=rf"P(\text{{None}}) = \frac{{n(\text{{outside}})}}{{n(S)}} = \frac{{{outside}}}{{{n_tot}}}",
            to_latex_str=fmt_frac(frac_none),
            op="read outside count and simplify",
            rule="classical probability definition",
        ),
    ]
    canonical = solution_graph(
        goal="determine P(all three) and P(none) from 3-set Venn diagram",
        steps=steps,
        final_latex=rf"P(A \cap B \cap C) = {fmt_frac(frac_all_three)}; \quad P(\text{{None}}) = {fmt_frac(frac_none)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Setup for all three: {abc}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate fraction P(all 3) = {fmt_frac(frac_all_three)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate fraction P(none) = {fmt_frac(frac_none)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_26",
        topic=TOPIC_NAME,
        subskill="26_venn_3_read_all_three_and_none",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_all_three),
        sample_answer=rf"P(A \cap B \cap C) = {fmt_frac(frac_all_three)}; \quad P(\text{{None}}) = {fmt_frac(frac_none)}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "The central overlapping region belongs to all three sets. The number outside the circles belongs to none.",
            "concept": "P = count / total.",
            "breakdown": f"All three = {abc}/{n_tot} = {fmt_frac(frac_all_three)}. None = {outside}/{n_tot} = {fmt_frac(frac_none)}.",
        },
        misconception_tags=["confused_central_intersection_with_two_set_intersection"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 27: Three-Set Venn Diagram — Exactly One Activity
# --------------------------------------------------------------------------- #
def arch_27_venn_3_read_exactly_one_subject(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    only_a = r.randint(18, 28)
    only_b = r.randint(15, 25)
    only_c = r.randint(16, 26)
    ab = r.randint(6, 10)
    ac = r.randint(5, 9)
    bc = r.randint(7, 11)
    abc = r.randint(4, 8)
    outside = r.randint(12, 20)
    n_tot = only_a + only_b + only_c + ab + ac + bc + abc + outside

    diag_svg = venn_3_svg(only_a, only_b, only_c, ab, ac, bc, abc, outside, "A", "B", "C", "Three-Set Venn Diagram")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Three-Set Venn Diagram", "diagram_role": "context"}

    n_exactly_one = only_a + only_b + only_c
    frac_ans = Fraction(n_exactly_one, n_tot)

    prompt = (
        f"Refer to the 3-set Venn diagram below showing {n_tot} learners across categories $A$, $B$, and $C$.\n\n"
        f"Calculate the probability that a randomly chosen learner participates in EXACTLY ONE activity. "
        f"Write your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Refer to 3-set Venn. Calculate }} P(\text{{exactly one activity}})."

    steps = [
        step(
            from_latex=r"n(\text{Exactly one}) = \text{Only } A + \text{Only } B + \text{Only } C",
            to_latex_str=rf"{only_a} + {only_b} + {only_c} = {n_exactly_one}",
            op="sum outer non-overlapping regions",
            rule="exactly one region definition",
        ),
        step(
            from_latex=rf"P(\text{{Exactly one}}) = \frac{{{n_exactly_one}}}{{{n_tot}}}",
            to_latex_str=fmt_frac(frac_ans),
            op="calculate probability fraction",
            rule="classical probability definition",
        ),
    ]
    canonical = solution_graph(
        goal="determine probability of exactly one activity in 3-set Venn",
        steps=steps,
        final_latex=fmt_frac(frac_ans),
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Summing only A, only B, only C: {only_a} + {only_b} + {only_c} = {n_exactly_one}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Fraction setup: {n_exactly_one}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified fraction {fmt_frac(frac_ans)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_27",
        topic=TOPIC_NAME,
        subskill="27_venn_3_read_exactly_one_subject",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_ans),
        sample_answer=fmt_frac(frac_ans),
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "'Exactly one' means only A, only B, or only C. Exclude all overlapping regions.",
            "concept": "P(exactly one) = (only A + only B + only C) / N.",
            "breakdown": f"{only_a} + {only_b} + {only_c} = {n_exactly_one}. P = {n_exactly_one}/{n_tot} = {fmt_frac(frac_ans)}.",
        },
        misconception_tags=["included_two_set_intersections_in_exactly_one"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 28: Three-Set Venn Diagram — At Least Two Subjects
# --------------------------------------------------------------------------- #
def arch_28_venn_3_read_at_least_two_subjects(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    only_a = r.randint(16, 26)
    only_b = r.randint(14, 24)
    only_c = r.randint(15, 25)
    ab = r.randint(6, 11)
    ac = r.randint(5, 10)
    bc = r.randint(7, 12)
    abc = r.randint(4, 9)
    outside = r.randint(10, 18)
    n_tot = only_a + only_b + only_c + ab + ac + bc + abc + outside

    diag_svg = venn_3_svg(only_a, only_b, only_c, ab, ac, bc, abc, outside, "A", "B", "C", "Three-Set Venn Diagram")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Three-Set Venn Diagram", "diagram_role": "context"}

    n_at_least_two = ab + ac + bc + abc
    frac_ans = Fraction(n_at_least_two, n_tot)

    prompt = (
        f"Refer to the 3-set Venn diagram below showing the distribution of {n_tot} participants.\n\n"
        f"Calculate the probability that a participant chosen at random participates in AT LEAST TWO of the activities. "
        f"Write your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Refer to 3-set Venn. Calculate }} P(\text{{at least two activities}})."

    steps = [
        step(
            from_latex=r"n(\text{At least two}) = (A \cap B\text{ only}) + (A \cap C\text{ only}) + (B \cap C\text{ only}) + (A \cap B \cap C)",
            to_latex_str=rf"{ab} + {ac} + {bc} + {abc} = {n_at_least_two}",
            op="sum all 4 intersection regions",
            rule="at least two regions definition",
        ),
        step(
            from_latex=rf"P(\text{{At least two}}) = \frac{{{n_at_least_two}}}{{{n_tot}}}",
            to_latex_str=fmt_frac(frac_ans),
            op="evaluate probability fraction",
            rule="classical probability definition",
        ),
    ]
    canonical = solution_graph(
        goal="determine probability of at least two activities in 3-set Venn",
        steps=steps,
        final_latex=fmt_frac(frac_ans),
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Summing all four overlap regions: {ab} + {ac} + {bc} + {abc} = {n_at_least_two}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Fraction setup: {n_at_least_two}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified fraction {fmt_frac(frac_ans)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_28",
        topic=TOPIC_NAME,
        subskill="28_venn_3_read_at_least_two_subjects",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_ans),
        sample_answer=fmt_frac(frac_ans),
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "'At least two' includes those who do exactly two AND those who do all three.",
            "concept": "Add the 3 pairwise intersections and the central triple intersection.",
            "breakdown": f"{ab} + {ac} + {bc} + {abc} = {n_at_least_two}. P = {n_at_least_two}/{n_tot} = {fmt_frac(frac_ans)}.",
        },
        misconception_tags=["forgot_to_include_all_three_in_at_least_two"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 29: Three-Set Venn Diagram — Two Subjects Only (Excluding Third)
# --------------------------------------------------------------------------- #
def arch_29_venn_3_read_two_subjects_only(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    only_a = r.randint(18, 28)
    only_b = r.randint(15, 25)
    only_c = r.randint(16, 26)
    ab = r.randint(8, 14)
    ac = r.randint(6, 12)
    bc = r.randint(7, 13)
    abc = r.randint(5, 10)
    outside = r.randint(10, 18)
    n_tot = only_a + only_b + only_c + ab + ac + bc + abc + outside

    diag_svg = venn_3_svg(only_a, only_b, only_c, ab, ac, bc, abc, outside, "A", "B", "C", "Three-Set Venn Diagram")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Three-Set Venn Diagram", "diagram_role": "context"}

    frac_ab_only = Fraction(ab, n_tot)

    prompt = (
        f"Refer to the 3-set Venn diagram below showing {n_tot} learners across activities $A$, $B$, and $C$.\n\n"
        f"Calculate the probability that a learner chosen at random participates in activities $A$ and $B$, "
        f"but NOT activity $C$, i.e. $P(A \\cap B \\cap C')$. Write your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Refer to 3-set Venn. Calculate }} P(A \cap B \cap C')."

    steps = [
        step(
            from_latex=r"n(A \cap B \cap C') = \text{Intersection region of } A \text{ and } B \text{ outside } C",
            to_latex_str=rf"{ab}",
            op="read pairwise intersection excluding third set",
            rule="set region identification",
        ),
        step(
            from_latex=rf"P(A \cap B \cap C') = \frac{{{ab}}}{{{n_tot}}}",
            to_latex_str=fmt_frac(frac_ab_only),
            op="divide by sample space size and simplify",
            rule="classical probability definition",
        ),
    ]
    canonical = solution_graph(
        goal="calculate P(A and B only, not C)",
        steps=steps,
        final_latex=fmt_frac(frac_ab_only),
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": rf"Identification of region count = {ab}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate simplified fraction {fmt_frac(frac_ab_only)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_29",
        topic=TOPIC_NAME,
        subskill="29_venn_3_read_two_subjects_only",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_ab_only),
        sample_answer=fmt_frac(frac_ab_only),
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "Look at the region where circles A and B overlap, but outside circle C.",
            "concept": "P(A ∩ B ∩ C') = (A and B only) / N.",
            "breakdown": f"Count is {ab}. Total is {n_tot}. P = {ab}/{n_tot} = {fmt_frac(frac_ab_only)}.",
        },
        misconception_tags=["included_all_three_in_two_only"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=2,
    )


# --------------------------------------------------------------------------- #
# Archetype 30: Three-Set Venn Diagram — Union Probability P(A or B or C)
# --------------------------------------------------------------------------- #
def arch_30_venn_3_union_formula_verification(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    only_a = r.randint(15, 25)
    only_b = r.randint(12, 22)
    only_c = r.randint(14, 24)
    ab = r.randint(6, 12)
    ac = r.randint(5, 10)
    bc = r.randint(7, 12)
    abc = r.randint(4, 9)
    outside = r.randint(12, 22)
    n_tot = only_a + only_b + only_c + ab + ac + bc + abc + outside

    n_union = n_tot - outside
    frac_union = Fraction(n_union, n_tot)

    diag_svg = venn_3_svg(only_a, only_b, only_c, ab, ac, bc, abc, outside, "A", "B", "C", "Three-Set Venn Diagram")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Three-Set Venn Diagram", "diagram_role": "context"}

    prompt = (
        f"Refer to the 3-set Venn diagram below showing the distribution of {n_tot} learners.\n\n"
        f"Calculate $P(A \\cup B \\cup C)$, the probability that a randomly selected learner participates "
        f"in AT LEAST ONE of the three activities. Write your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Refer to 3-set Venn with }} N={n_tot}. \text{{ Calculate }} P(A \cup B \cup C)."

    steps = [
        step(
            from_latex=r"n(A \cup B \cup C) = n(S) - n(\text{None})",
            to_latex_str=rf"{n_tot} - {outside} = {n_union}",
            op="calculate union by subtracting outside region from total",
            rule="complement rule for union",
        ),
        step(
            from_latex=rf"P(A \cup B \cup C) = \frac{{{n_union}}}{{{n_tot}}}",
            to_latex_str=fmt_frac(frac_union),
            op="form probability and simplify fraction",
            rule="classical probability definition",
        ),
    ]
    canonical = solution_graph(
        goal="calculate union of three events in Venn diagram",
        steps=steps,
        final_latex=fmt_frac(frac_union),
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": rf"Union count: {n_tot} - {outside} = {n_union}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate simplified fraction {fmt_frac(frac_union)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_30",
        topic=TOPIC_NAME,
        subskill="30_venn_3_union_formula_verification",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_union),
        sample_answer=fmt_frac(frac_union),
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "The easiest way to find the union is 1 - P(none), or total minus outside.",
            "concept": "P(A ∪ B ∪ C) = (N - outside) / N.",
            "breakdown": f"Union count = {n_tot} - {outside} = {n_union}. P = {n_union}/{n_tot} = {fmt_frac(frac_union)}.",
        },
        misconception_tags=["added_all_circle_totals_without_deducting_overlaps"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 31: Three-Set Venn Diagram — Algebraic Unknown x in Center
# --------------------------------------------------------------------------- #
def arch_31_venn_3_algebraic_x_central_intersection(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    x_val = r.randint(5, 12)
    only_a = r.randint(15, 25)
    only_b = r.randint(12, 22)
    only_c = r.randint(14, 24)
    ab = r.randint(6, 12)
    ac = r.randint(5, 10)
    bc = r.randint(7, 12)
    outside = r.randint(10, 20)
    n_tot = only_a + only_b + only_c + ab + ac + bc + x_val + outside

    # Emits diagram showing 'x' in the center
    diag_svg = venn_3_svg(only_a, only_b, only_c, ab, ac, bc, "x", outside, "A", "B", "C", "Venn Diagram with Unknown Central Intersection x")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Algebraic 3-Set Venn Diagram", "diagram_role": "context"}

    known_sum = only_a + only_b + only_c + ab + ac + bc + outside
    frac_x = Fraction(x_val, n_tot)

    prompt = (
        f"A survey of {n_tot} learners was conducted regarding three subjects $A$, $B$, and $C$. "
        f"The number of learners participating in each region is shown in the Venn diagram below, "
        f"where the number of learners who participate in ALL THREE subjects is represented by $x$.\n\n"
        f"1. Set up an equation and solve for $x$. (2)\n"
        f"2. Hence, calculate the probability that a randomly chosen learner participates in all three subjects. (1)"
    )
    prompt_latex = rf"\text{{Solve for }} x \text{{ from }} {known_sum} + x = {n_tot}\text{{, and find }} P(A \cap B \cap C)."

    steps = [
        step(
            from_latex=rf"({only_a} + {only_b} + {only_c} + {ab} + {ac} + {bc} + {outside}) + x = {n_tot}",
            to_latex_str=rf"{known_sum} + x = {n_tot}",
            op="sum all 8 disjoint regions to equal total sample space",
            rule="linear equation setup",
        ),
        step(
            from_latex=rf"x = {n_tot} - {known_sum}",
            to_latex_str=rf"x = {x_val}",
            op="subtract known sum to solve for x",
            rule="linear equation solution",
        ),
        step(
            from_latex=rf"P(A \cap B \cap C) = \frac{{{x_val}}}{{{n_tot}}}",
            to_latex_str=fmt_frac(frac_x),
            op="evaluate probability fraction",
            rule="probability definition",
        ),
    ]
    canonical = solution_graph(
        goal="solve for central unknown x in 3-set Venn and compute probability",
        steps=steps,
        final_latex=rf"x = {x_val}; \quad P(A \cap B \cap C) = {fmt_frac(frac_x)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct equation setup: {known_sum} + x = {n_tot}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate solution x = {x_val}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Probability = {fmt_frac(frac_x)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_31",
        topic=TOPIC_NAME,
        subskill="31_venn_3_algebraic_x_central_intersection",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"x = {x_val}; \quad {fmt_frac(frac_x)}",
        sample_answer=rf"x = {x_val}; \quad P(A \cap B \cap C) = {fmt_frac(frac_x)}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "The sum of all 8 regions (the 7 interior regions plus the outside region) must equal N.",
            "concept": "Total = (sum of known regions) + x.",
            "breakdown": f"Known regions sum to {known_sum}. Total is {n_tot}. x = {n_tot} - {known_sum} = {x_val}. P = {x_val}/{n_tot} = {fmt_frac(frac_x)}.",
        },
        misconception_tags=["omitted_outside_region_in_sum"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# --------------------------------------------------------------------------- #
# Archetype 32: Three-Set Venn Diagram — Unknown x with Union Given
# --------------------------------------------------------------------------- #
def arch_32_venn_3_algebraic_x_given_at_least_one(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    x_val = r.randint(6, 14)
    only_a = r.randint(16, 24)
    only_b = r.randint(14, 22)
    only_c = r.randint(15, 23)
    ab = r.randint(7, 12)
    ac = r.randint(6, 11)
    bc = r.randint(8, 13)
    n_union = only_a + only_b + only_c + ab + ac + bc + x_val
    outside = r.randint(10, 18)
    n_tot = n_union + outside

    diag_svg = venn_3_svg(only_a, only_b, only_c, ab, ac, bc, "x", outside, "A", "B", "C", "Three-Set Venn Diagram")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Three-Set Venn Diagram", "diagram_role": "context"}

    known_interior = only_a + only_b + only_c + ab + ac + bc

    prompt = (
        f"In a cohort of {n_tot} learners, exactly {n_union} learners participate in at least one of three sports $A$, $B$, or $C$.\n"
        f"The non-overlapping sub-regions are given as shown in the diagram, with the central intersection $A \\cap B \\cap C = x$.\n\n"
        f"Determine the value of $x$."
    )
    prompt_latex = rf"\text{{Given }} n(A \cup B \cup C) = {n_union}\text{{, solve for }} x."

    steps = [
        step(
            from_latex=rf"{known_interior} + x = n(A \cup B \cup C)",
            to_latex_str=rf"{known_interior} + x = {n_union}",
            op="equate interior regions sum to union total",
            rule="union decomposition",
        ),
        step(
            from_latex=rf"x = {n_union} - {known_interior}",
            to_latex_str=rf"x = {x_val}",
            op="evaluate linear difference",
            rule="subtraction",
        ),
    ]
    canonical = solution_graph(
        goal="solve for x from union cardinality",
        steps=steps,
        final_latex=rf"x = {x_val}",
    )
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": rf"Equation {known_interior} + x = {n_union}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate solution x = {x_val}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_32",
        topic=TOPIC_NAME,
        subskill="32_venn_3_algebraic_x_given_at_least_one",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"x = {x_val}",
        sample_answer=rf"x = {x_val}",
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "The 7 regions inside the circles sum to the union n(A ∪ B ∪ C).",
            "concept": "Union = sum of 6 known regions + x.",
            "breakdown": f"{known_interior} + x = {n_union} ==> x = {n_union} - {known_interior} = {x_val}.",
        },
        misconception_tags=["included_outside_when_equating_to_union"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 33: Three-Set Venn Diagram — Relation Between Outside & Center
# --------------------------------------------------------------------------- #
def arch_33_venn_3_algebraic_x_outside_and_center(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    x_val = r.randint(5, 14)
    only_a = r.randint(15, 25)
    only_b = r.randint(14, 22)
    only_c = r.randint(16, 26)
    ab = r.randint(6, 12)
    ac = r.randint(5, 11)
    bc = r.randint(7, 13)
    outside_str = "2x"
    interior_known = only_a + only_b + only_c + ab + ac + bc
    n_tot = interior_known + 3 * x_val

    diag_svg = venn_3_svg(only_a, only_b, only_c, ab, ac, bc, "x", outside_str, "A", "B", "C", "Three-Set Venn Diagram (Outside = 2x)")
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Three-Set Venn Diagram", "diagram_role": "context"}

    prompt = (
        f"A survey of {n_tot} learners shows the distributions depicted in the Venn diagram below. "
        f"The number of learners participating in all three activities is $x$, and the number of learners "
        f"participating in none of the activities is $2x$.\n\n"
        f"1. Set up an equation in terms of $x$ and determine the value of $x$. (2)\n"
        f"2. How many learners participate in NONE of the three activities? (1)"
    )
    prompt_latex = rf"\text{{Solve for }} x \text{{ from }} {interior_known} + 3x = {n_tot}."
    steps = [
        step(from_latex=rf"{interior_known} + x + 2x = {n_tot}", to_latex_str=rf"{interior_known} + 3x = {n_tot}", op="combine like terms across all regions", rule="linear equation setup"),
        step(from_latex=rf"3x = {n_tot - interior_known}", to_latex_str=rf"x = {x_val}", op="divide to solve for x", rule="linear equation solution"),
        step(from_latex=rf"n(\text{{None}}) = 2({x_val})", to_latex_str=rf"{2 * x_val}", op="evaluate none count", rule="multiplication"),
    ]
    canonical = solution_graph(goal="solve for x and determine outside count in 3-set Venn", steps=steps, final_latex=rf"x = {x_val}; \quad n(\text{{None}}) = {2 * x_val}")
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Equation setup: {interior_known} + 3x = {n_tot}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate solution x = {x_val}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Number who do none = {2 * x_val}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_33", topic=TOPIC_NAME, subskill="33_venn_3_algebraic_x_outside_and_center",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=rf"x = {x_val}; \quad {2 * x_val}", sample_answer=rf"x = {x_val}; \quad n(\text{{None}}) = {2 * x_val}",
        canonical_solution=canonical, marking_schema=schema, diagram_spec=diag_spec,
        hints={
            "nudge": "Add the 6 known interior numbers plus x plus 2x. Set equal to total N.",
            "concept": "Total = known + 3x ==> 3x = Total - known.",
            "breakdown": f"{interior_known} + 3x = {n_tot} ==> 3x = {n_tot - interior_known} ==> x = {x_val}. None = 2x = {2 * x_val}.",
        },
        misconception_tags=["forgot_factor_of_two_for_outside"], term=3, caps_weight_percent=15, suggested_duration_mins=4,
    )


# --------------------------------------------------------------------------- #
# Archetype 34: Three-Set Venn Context — School Clubs Survey
# --------------------------------------------------------------------------- #
def arch_34_venn_3_contextual_survey_school_clubs(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    sports_only = r.randint(25, 42)
    culture_only = r.randint(20, 34)
    service_only = r.randint(18, 30)
    sp_cul = r.randint(8, 16)
    sp_ser = r.randint(7, 15)
    cul_ser = r.randint(9, 17)
    all_three = r.randint(5, 12)
    none_count = r.randint(10, 22)
    n_tot = sports_only + culture_only + service_only + sp_cul + sp_ser + cul_ser + all_three + none_count

    diag_svg = venn_3_svg(
        sports_only, culture_only, service_only, sp_cul, sp_ser, cul_ser, all_three, none_count,
        "Sports", "Culture", "Service", "School Extra-Curricular Clubs"
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "School Clubs Venn Diagram", "diagram_role": "context"}

    n_sports_tot = sports_only + sp_cul + sp_ser + all_three
    frac_sports = Fraction(n_sports_tot, n_tot)

    prompt = (
        f"A high school surveyed {n_tot} Grade 11 learners regarding participation in three club categories: "
        f"Sports ($S$), Culture ($C$), and Service ($V$). The findings are shown in the Venn diagram below.\n\n"
        f"1. How many learners participate in Sports in total? (1)\n"
        f"2. Calculate the probability that a randomly chosen learner participates in Sports. "
        f"Write your answer as a simplified fraction. (2)"
    )
    prompt_latex = rf"\text{{Refer to Clubs Venn. Find }} n(S) \text{{ and }} P(S)."
    steps = [
        step(from_latex=rf"n(S) = {sports_only} + {sp_cul} + {sp_ser} + {all_three}", to_latex_str=rf"{n_sports_tot}", op="sum all 4 regions forming the Sports circle", rule="circle total summation"),
        step(from_latex=rf"P(S) = \frac{{{n_sports_tot}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_sports), op="divide by sample space and simplify", rule="classical probability definition"),
    ]
    canonical = solution_graph(goal="calculate total sports count and probability", steps=steps, final_latex=rf"n(S) = {n_sports_tot}; \quad P(S) = {fmt_frac(frac_sports)}")
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Summing circle S: {sports_only} + {sp_cul} + {sp_ser} + {all_three} = {n_sports_tot}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Fraction setup: {n_sports_tot}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified fraction {fmt_frac(frac_sports)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_34", topic=TOPIC_NAME, subskill="34_venn_3_contextual_survey_school_clubs",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_sports), sample_answer=rf"n(S) = {n_sports_tot}; \quad P(S) = {fmt_frac(frac_sports)}",
        canonical_solution=canonical, marking_schema=schema, diagram_spec=diag_spec,
        hints={
            "nudge": "The Sports circle contains 4 distinct regions: sports only, sports & culture only, sports & service only, and all three.",
            "concept": "Add all 4 numbers in the Sports circle.",
            "breakdown": f"n(S) = {sports_only} + {sp_cul} + {sp_ser} + {all_three} = {n_sports_tot}. P(S) = {n_sports_tot}/{n_tot} = {fmt_frac(frac_sports)}.",
        },
        misconception_tags=["used_sports_only_instead_of_total_sports"], term=3, caps_weight_percent=15, suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 35: Three-Set Venn Context — Digital Platforms Survey
# --------------------------------------------------------------------------- #
def arch_35_venn_3_contextual_survey_streaming_services(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    only_a = r.randint(20, 32)
    only_b = r.randint(14, 24)
    only_c = r.randint(16, 26)
    ab_only = r.randint(7, 14)
    ac_only = r.randint(8, 15)
    bc_only = r.randint(6, 13)
    abc = r.randint(6, 14)
    outside = r.randint(8, 18)
    n_tot = only_a + only_b + only_c + ab_only + ac_only + bc_only + abc + outside

    diag_svg = venn_3_svg(
        only_a, only_b, only_c, ab_only, ac_only, bc_only, abc, outside,
        "Netflix", "Showmax", "YouTube", "Streaming Services Survey"
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Streaming Services Venn Diagram", "diagram_role": "context"}
    frac_abc = Fraction(abc, n_tot)

    prompt = (
        f"A media survey investigated the subscriptions of {n_tot} households to three streaming platforms: "
        f"Netflix, Showmax, and YouTube Premium. The results are illustrated in the Venn diagram below.\n\n"
        f"Calculate the probability that a household chosen at random subscribes to ALL THREE streaming platforms. "
        f"Write your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Refer to Streaming Venn. Calculate }} P(\text{{all three platforms}})."
    steps = [
        step(from_latex=rf"n(\text{{All three}}) = {abc}", to_latex_str=rf"{abc}", op="read central intersection count", rule="region reading"),
        step(from_latex=rf"P(\text{{All three}}) = \frac{{{abc}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_abc), op="divide by sample space size and simplify", rule="classical probability definition"),
    ]
    canonical = solution_graph(goal="calculate probability of subscribing to all three platforms", steps=steps, final_latex=fmt_frac(frac_abc))
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct fraction setup: {abc}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate simplified fraction {fmt_frac(frac_abc)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_35", topic=TOPIC_NAME, subskill="35_venn_3_contextual_survey_streaming_services",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_abc), sample_answer=fmt_frac(frac_abc),
        canonical_solution=canonical, marking_schema=schema, diagram_spec=diag_spec,
        hints={
            "nudge": "The central intersection shows the count of households subscribing to all three platforms.",
            "concept": "P(all three) = central count / total.",
            "breakdown": f"Central count is {abc}. Total is {n_tot}. P = {abc}/{n_tot} = {fmt_frac(frac_abc)}.",
        },
        misconception_tags=["read_two_set_overlap_instead_of_three_set_center"], term=3, caps_weight_percent=15, suggested_duration_mins=2,
    )


# --------------------------------------------------------------------------- #
# Archetype 36: Two-Way Contingency Table — Complete Missing Totals
# --------------------------------------------------------------------------- #
def arch_36_contingency_table_complete_missing_totals(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_tot = r.choice([100, 120, 150, 200])
    m_tot = r.randint(45, n_tot - 45)
    f_tot = n_tot - m_tot

    pass_tot = r.randint(60, n_tot - 25)
    fail_tot = n_tot - pass_tot

    # Male pass
    a = r.randint(max(20, m_tot + pass_tot - n_tot + 5), min(m_tot - 10, pass_tot - 10))
    b = m_tot - a  # male fail
    c = pass_tot - a  # female pass
    d = f_tot - c  # female fail

    # Table with row and column totals
    tbl_latex = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Gender} & \textbf{Passed } (P) & \textbf{Failed } (F) & \textbf{Total} \\ \hline"
        rf"\text{{Male }} (M) & {a} & {b} & {m_tot} \\ \hline"
        rf"\text{{Female }} (W) & {c} & {d} & {f_tot} \\ \hline"
        rf"\textbf{{Total}} & {pass_tot} & {fail_tot} & {n_tot} \\ \hline"
        r"\end{array}"
    )

    frac_male_pass = Fraction(a, n_tot)
    frac_female = Fraction(f_tot, n_tot)

    prompt = (
        f"The two-way contingency table below summarizes the performance of {n_tot} learners in a driving test:\n\n"
        f"$${tbl_latex}$$\n\n"
        f"1. Calculate the probability that a learner selected at random is Female, $P(W)$. (1)\n"
        f"2. Calculate the probability that a learner selected at random is Male AND passed the test, $P(M \\cap P)$. "
        f"Write your answer as a simplified fraction. (2)"
    )
    prompt_latex = rf"\text{{Contingency table with }} N={n_tot}. \text{{ Calculate }} P(W) \text{{ and }} P(M \cap P)."

    steps = [
        step(
            from_latex=rf"P(W) = \frac{{n(W)}}{{N}} = \frac{{{f_tot}}}{{{n_tot}}}",
            to_latex_str=fmt_frac(frac_female),
            op="calculate marginal probability for females",
            rule="marginal probability definition",
        ),
        step(
            from_latex=rf"P(M \cap P) = \frac{{n(M \cap P)}}{{N}} = \frac{{{a}}}{{{n_tot}}}",
            to_latex_str=fmt_frac(frac_male_pass),
            op="calculate joint intersection probability",
            rule="joint probability definition",
        ),
    ]
    canonical = solution_graph(
        goal="calculate marginal and joint probabilities from contingency table",
        steps=steps,
        final_latex=rf"P(W) = {fmt_frac(frac_female)}; \quad P(M \cap P) = {fmt_frac(frac_male_pass)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Marginal probability P(W) = {fmt_frac(frac_female)}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Joint probability setup: {a}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified joint probability {fmt_frac(frac_male_pass)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_36",
        topic=TOPIC_NAME,
        subskill="36_contingency_table_complete_missing_totals",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_male_pass),
        sample_answer=rf"P(W) = {fmt_frac(frac_female)}; \quad P(M \cap P) = {fmt_frac(frac_male_pass)}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "For marginal probability P(W), take the female total over grand total. For joint P(M ∩ P), take the Male-Passed cell over grand total.",
            "concept": "Joint probability uses the specific cell; marginal probability uses the row or column total.",
            "breakdown": f"P(W) = {f_tot}/{n_tot} = {fmt_frac(frac_female)}. P(M ∩ P) = {a}/{n_tot} = {fmt_frac(frac_male_pass)}.",
        },
        misconception_tags=["divided_by_row_total_instead_of_grand_total"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 37: Contingency Table — Solve Unknown Interior Cell x
# --------------------------------------------------------------------------- #
def arch_37_contingency_table_solve_unknown_cell_x(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_tot = r.choice([120, 140, 160, 200])
    m_tot = r.randint(50, n_tot - 50)
    f_tot = n_tot - m_tot

    l_tot = r.randint(50, n_tot - 50)
    nl_tot = n_tot - l_tot

    a = r.randint(max(20, m_tot + l_tot - n_tot + 5), min(m_tot - 10, l_tot - 10))
    b = m_tot - a  # 'x'
    c = l_tot - a
    d = f_tot - c

    tbl_latex = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Group} & \textbf{Sport } (S) & \textbf{No Sport } (S') & \textbf{Total} \\ \hline"
        rf"\text{{Grade 10}} & {a} & x & {m_tot} \\ \hline"
        rf"\text{{Grade 11}} & {c} & {d} & {f_tot} \\ \hline"
        rf"\textbf{{Total}} & {l_tot} & {nl_tot} & {n_tot} \\ \hline"
        r"\end{array}"
    )

    frac_gr11_sport = Fraction(c, n_tot)

    prompt = (
        f"A physical education department surveyed {n_tot} learners across Grades 10 and 11:\n\n"
        f"$${tbl_latex}$$\n\n"
        f"1. Determine the value of $x$. (1)\n"
        f"2. Calculate the probability that a learner selected at random is in Grade 11 AND plays sport. "
        f"Write your answer as a simplified fraction. (2)"
    )
    prompt_latex = rf"\text{{Contingency table. Determine }} x \text{{ and calculate }} P(\text{{Gr11}} \cap S)."

    steps = [
        step(
            from_latex=rf"x = {m_tot} - {a}",
            to_latex_str=rf"x = {b}",
            op="subtract cell from row total to solve for x",
            rule="row sum balance",
        ),
        step(
            from_latex=rf"P(\text{{Gr11}} \cap S) = \frac{{{c}}}{{{n_tot}}}",
            to_latex_str=fmt_frac(frac_gr11_sport),
            op="divide cell value by grand total and simplify",
            rule="joint probability definition",
        ),
    ]
    canonical = solution_graph(
        goal="solve for unknown cell x and calculate joint probability",
        steps=steps,
        final_latex=rf"x = {b}; \quad P(\text{{Gr11}} \cap S) = {fmt_frac(frac_gr11_sport)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct value x = {b}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Probability fraction setup: {c}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified fraction {fmt_frac(frac_gr11_sport)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_37",
        topic=TOPIC_NAME,
        subskill="37_contingency_table_solve_unknown_cell_x",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=rf"x = {b}; \quad {fmt_frac(frac_gr11_sport)}",
        sample_answer=rf"x = {b}; \quad P(\text{{Gr11}} \cap S) = {fmt_frac(frac_gr11_sport)}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "The Grade 10 row must sum to its row total: a + x = total.",
            "concept": "x = Grade 10 Total - Grade 10 Sport.",
            "breakdown": f"x = {m_tot} - {a} = {b}. For Grade 11 and Sport, P = {c}/{n_tot} = {fmt_frac(frac_gr11_sport)}.",
        },
        misconception_tags=["subtracted_from_wrong_marginal_total"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 38: Contingency Table — Joint and Union Probabilities
# --------------------------------------------------------------------------- #
def arch_38_contingency_table_joint_and_marginal_probabilities(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(25, 45)
    b = r.randint(15, 30)
    c = r.randint(20, 35)
    d = r.randint(18, 32)
    m_tot = a + b
    f_tot = c + d
    l_tot = a + c
    nl_tot = b + d
    n_tot = m_tot + f_tot

    tbl_latex = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Gender} & \textbf{Licensed } (L) & \textbf{Unlicensed } (L') & \textbf{Total} \\ \hline"
        rf"\text{{Male }} (M) & {a} & {b} & {m_tot} \\ \hline"
        rf"\text{{Female }} (F) & {c} & {d} & {f_tot} \\ \hline"
        rf"\textbf{{Total}} & {l_tot} & {nl_tot} & {n_tot} \\ \hline"
        r"\end{array}"
    )
    union_cnt = a + b + c
    frac_union = Fraction(union_cnt, n_tot)

    prompt = (
        f"Refer to the two-way table below:\n\n$${tbl_latex}$$\n\n"
        f"Calculate the probability that a randomly selected learner is Male OR holds a license, $P(M \\cup L)$. "
        f"Write your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Contingency table. Calculate }} P(M \cup L)."
    steps = [
        step(from_latex=r"P(M \cup L) = P(M) + P(L) - P(M \cap L)", to_latex_str=rf"\frac{{{m_tot}}}{{{n_tot}}} + \frac{{{l_tot}}}{{{n_tot}}} - \frac{{{a}}}{{{n_tot}}} = \frac{{{union_cnt}}}{{{n_tot}}}", op="apply addition rule with table values", rule="addition rule for contingency tables"),
        step(from_latex=rf"\frac{{{union_cnt}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_union), op="simplify fraction", rule="fraction reduction"),
    ]
    canonical = solution_graph(goal="calculate union probability from contingency table", steps=steps, final_latex=fmt_frac(frac_union))
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Addition rule substitution: ({m_tot} + {l_tot} - {a})/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Fraction: {union_cnt}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified fraction {fmt_frac(frac_union)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_38", topic=TOPIC_NAME, subskill="38_contingency_table_joint_and_marginal_probabilities",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_union), sample_answer=fmt_frac(frac_union),
        canonical_solution=canonical, marking_schema=schema,
        hints={
            "nudge": "P(M ∪ L) = P(M) + P(L) - P(M ∩ L), or add the 3 favorable cells: Male-Licensed + Male-Unlicensed + Female-Licensed.",
            "concept": "Add row total and column total, then subtract the double-counted intersection cell.",
            "breakdown": f"({m_tot} + {l_tot} - {a}) / {n_tot} = {union_cnt}/{n_tot} = {fmt_frac(frac_union)}.",
        },
        misconception_tags=["forgot_to_subtract_intersection_cell_in_union"], term=3, caps_weight_percent=15, suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 39: Contextual Contingency Table — Learner License Survey
# --------------------------------------------------------------------------- #
def arch_39_contingency_table_driver_license_survey(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(35, 55)
    b = r.randint(20, 35)
    c = r.randint(30, 48)
    d = r.randint(22, 38)
    m_tot = a + b
    f_tot = c + d
    l_tot = a + c
    nl_tot = b + d
    n_tot = m_tot + f_tot

    tbl_latex = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Gender} & \textbf{Learner's License } (L) & \textbf{No License } (L') & \textbf{Total} \\ \hline"
        rf"\text{{Male }} (M) & {a} & {b} & {m_tot} \\ \hline"
        rf"\text{{Female }} (F) & {c} & {d} & {f_tot} \\ \hline"
        rf"\textbf{{Total}} & {l_tot} & {nl_tot} & {n_tot} \\ \hline"
        r"\end{array}"
    )
    frac_ans = Fraction(d, n_tot)

    prompt = (
        f"A sample of {n_tot} Grade 11 learners was surveyed to determine whether they had obtained a learner's license:\n\n"
        f"$${tbl_latex}$$\n\n"
        f"Calculate the probability that a learner selected at random is Female AND has NO learner's license, $P(F \\cap L')$. "
        f"Write your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Survey of }} {n_tot}. \text{{ Calculate }} P(F \cap L')."
    steps = [
        step(from_latex=rf"n(F \cap L') = {d}", to_latex_str=rf"{d}", op="identify cell for Female and No License", rule="table cell lookup"),
        step(from_latex=rf"P(F \cap L') = \frac{{{d}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_ans), op="form fraction and reduce", rule="classical probability definition"),
    ]
    canonical = solution_graph(goal="determine joint probability from license survey contingency table", steps=steps, final_latex=fmt_frac(frac_ans))
    schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct fraction setup: {d}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate simplified fraction {fmt_frac(frac_ans)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_39", topic=TOPIC_NAME, subskill="39_contingency_table_driver_license_survey",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_ans), sample_answer=fmt_frac(frac_ans),
        canonical_solution=canonical, marking_schema=schema,
        hints={
            "nudge": f"Find the cell where the 'Female' row and the 'No License' column meet, and divide by {n_tot}.",
            "concept": "P(F ∩ L') = cell count / grand total.",
            "breakdown": f"Cell count is {d}. Grand total is {n_tot}. P = {d}/{n_tot} = {fmt_frac(frac_ans)}.",
        },
        misconception_tags=["divided_by_female_total_instead_of_grand_total"], term=3, caps_weight_percent=15, suggested_duration_mins=2,
    )


# --------------------------------------------------------------------------- #
# Archetype 40: Contextual Contingency Table — Health Clinic Survey
# --------------------------------------------------------------------------- #
def arch_40_contingency_table_medical_test_or_vaccine(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(12, 24)
    b = r.randint(85, 115)
    c = r.randint(20, 35)
    d = r.randint(45, 65)
    vax_tot = a + b
    novax_tot = c + d
    flu_tot = a + c
    noflu_tot = b + d
    n_tot = vax_tot + novax_tot

    tbl_latex = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Vaccination} & \textbf{Contracted Flu } (F) & \textbf{No Flu } (F') & \textbf{Total} \\ \hline"
        rf"\text{{Vaccinated }} (V) & {a} & {b} & {vax_tot} \\ \hline"
        rf"\text{{Not Vaccinated }} (V') & {c} & {d} & {novax_tot} \\ \hline"
        rf"\textbf{{Total}} & {flu_tot} & {noflu_tot} & {n_tot} \\ \hline"
        r"\end{array}"
    )
    frac_vax = Fraction(vax_tot, n_tot)
    frac_vax_noflu = Fraction(b, n_tot)

    prompt = (
        f"A medical study observed {n_tot} patients regarding seasonal flu vaccination:\n\n$${tbl_latex}$$\n\n"
        f"1. What is the probability that a randomly chosen patient was vaccinated, $P(V)$? (1)\n"
        f"2. What is the probability that a patient was vaccinated AND did not contract the flu, $P(V \\cap F')$? (2)"
    )
    prompt_latex = rf"\text{{Medical contingency table. Find }} P(V) \text{{ and }} P(V \cap F')."
    steps = [
        step(from_latex=rf"P(V) = \frac{{{vax_tot}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_vax), op="calculate marginal probability of vaccination", rule="marginal probability definition"),
        step(from_latex=rf"P(V \cap F') = \frac{{{b}}}{{{n_tot}}}", to_latex_str=fmt_frac(frac_vax_noflu), op="calculate joint probability of vaccinated and no flu", rule="joint probability definition"),
    ]
    canonical = solution_graph(goal="calculate marginal and joint probabilities from medical study table", steps=steps, final_latex=rf"P(V) = {fmt_frac(frac_vax)}; \quad P(V \cap F') = {fmt_frac(frac_vax_noflu)}")
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Marginal P(V) = {fmt_frac(frac_vax)}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Joint setup: {b}/{n_tot}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified fraction {fmt_frac(frac_vax_noflu)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_40", topic=TOPIC_NAME, subskill="40_contingency_table_medical_test_or_vaccine",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_vax_noflu), sample_answer=rf"P(V) = {fmt_frac(frac_vax)}; \quad P(V \cap F') = {fmt_frac(frac_vax_noflu)}",
        canonical_solution=canonical, marking_schema=schema,
        hints={
            "nudge": "P(V) uses the total vaccinated row. P(V ∩ F') uses the intersection cell (Vaccinated, No Flu).",
            "concept": f"Divide by the grand total {n_tot}.",
            "breakdown": f"P(V) = {vax_tot}/{n_tot} = {fmt_frac(frac_vax)}. P(V ∩ F') = {b}/{n_tot} = {fmt_frac(frac_vax_noflu)}.",
        },
        misconception_tags=["confused_marginal_and_joint_probability"], term=3, caps_weight_percent=15, suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 41: Testing Independence in Contingency Table (Gender & Subject)
# --------------------------------------------------------------------------- #
def arch_41_contingency_independence_test_gender_subject(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    is_indep = r.choice([True, False])
    k = r.randint(2, 5)
    m_tot = 30 * k
    f_tot = 30 * k
    n_tot = m_tot + f_tot
    maths_tot = 20 * k
    lit_tot = 40 * k

    if is_indep:
        a = 10 * k
        b = 20 * k
        c = 10 * k
        d = 20 * k
    else:
        a = 10 * k + 3
        b = m_tot - a
        c = maths_tot - a
        d = f_tot - c

    tbl_latex = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Gender} & \textbf{Mathematics } (M) & \textbf{Mathematical Literacy } (L) & \textbf{Total} \\ \hline"
        rf"\text{{Male }} (B) & {a} & {b} & {m_tot} \\ \hline"
        rf"\text{{Female }} (G) & {c} & {d} & {f_tot} \\ \hline"
        rf"\textbf{{Total}} & {maths_tot} & {lit_tot} & {n_tot} \\ \hline"
        r"\end{array}"
    )
    p_b = Fraction(m_tot, n_tot)
    p_m = Fraction(maths_tot, n_tot)
    prod = p_b * p_m
    p_both = Fraction(a, n_tot)
    verdict = "INDEPENDENT" if is_indep else "DEPENDENT"
    comp_sym = "=" if is_indep else rf"\neq"

    prompt = (
        f"A survey of {n_tot} Grade 11 learners analyzed gender and subject choice:\n\n$${tbl_latex}$$\n\n"
        f"Determine, showing all mathematical calculations, whether the event of being Male ($B$) "
        f"and the event of choosing Mathematics ($M$) are independent or dependent."
    )
    prompt_latex = rf"\text{{Contingency table. Prove whether }} B \text{{ and }} M \text{{ are independent.}}"
    steps = [
        step(from_latex=rf"P(B) \times P(M) = \frac{{{m_tot}}}{{{n_tot}}} \times \frac{{{maths_tot}}}{{{n_tot}}}", to_latex_str=rf"{fmt_frac(p_b)} \times {fmt_frac(p_m)} = {fmt_frac(prod)}", op="calculate product of marginal probabilities", rule="multiplication"),
        step(from_latex=rf"P(B \cap M) = \frac{{{a}}}{{{n_tot}}} = {fmt_frac(p_both)}", to_latex_str=rf"P(B \cap M) {comp_sym} P(B) \times P(M) \implies \text{{Events are }} \textbf{{{verdict}}}", op="compare intersection with product and state conclusion", rule="independence test"),
    ]
    canonical = solution_graph(goal="determine if gender and subject choice are independent from contingency table", steps=steps, final_latex=rf"\text{{{verdict}}}")
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": rf"Marginal product P(B) × P(M) = {fmt_frac(prod)}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Joint probability P(B ∩ M) = {fmt_frac(p_both)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"Comparison statement: {fmt_frac(p_both)} {comp_sym} {fmt_frac(prod)}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate conclusion: {verdict}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_41", topic=TOPIC_NAME, subskill="41_contingency_independence_test_gender_subject",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=rf"\text{{{verdict}}}", sample_answer=rf"P(B \cap M) = {fmt_frac(p_both)}; \quad P(B) \times P(M) = {fmt_frac(prod)}; \quad \text{{{verdict}}}",
        canonical_solution=canonical, marking_schema=schema,
        hints={
            "nudge": "Calculate P(Male) × P(Mathematics) and compare it to P(Male and Mathematics).",
            "concept": "Events are independent iff P(B ∩ M) = P(B) × P(M).",
            "breakdown": f"P(B) = {fmt_frac(p_b)}, P(M) = {fmt_frac(p_m)}, Product = {fmt_frac(prod)}. P(B ∩ M) = {fmt_frac(p_both)}. Conclusion: {verdict}.",
        },
        misconception_tags=["concluded_independent_without_multiplying_marginals"], term=3, caps_weight_percent=15, suggested_duration_mins=4,
    )


# --------------------------------------------------------------------------- #
# Archetype 42: Contingency Independence Test — Device Preference
# --------------------------------------------------------------------------- #
def arch_42_contingency_independence_test_phone_brand(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    k = r.randint(2, 6)
    a = 15 * k
    b = 10 * k
    c = 15 * k
    d = 10 * k
    row_x = a + b
    row_y = c + d
    col_a = a + c
    col_i = b + d
    n_tot = row_x + row_y

    tbl_latex = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Age Group} & \textbf{Android } (A) & \textbf{iOS } (I) & \textbf{Total} \\ \hline"
        rf"\text{{Adult }} (X) & {a} & {b} & {row_x} \\ \hline"
        rf"\text{{Youth }} (Y) & {c} & {d} & {row_y} \\ \hline"
        rf"\textbf{{Total}} & {col_a} & {col_i} & {n_tot} \\ \hline"
        r"\end{array}"
    )
    prompt = (
        f"A consumer study of {n_tot} mobile phone users recorded the following data:\n\n$${tbl_latex}$$\n\n"
        f"Prove whether being an Adult ($X$) and preferring Android ($A$) are independent events."
    )
    prompt_latex = rf"\text{{Study of {n_tot} users. Prove if being Adult and preferring Android are independent.}}"
    steps = [
        step(from_latex=rf"P(X) = \frac{{{row_x}}}{{{n_tot}}} = 0{{,}}5, \quad P(A) = \frac{{{col_a}}}{{{n_tot}}} = 0{{,}}6", to_latex_str=r"P(X) \times P(A) = 0{,}5 \times 0{,}6 = 0{,}30", op="calculate marginal product", rule="multiplication"),
        step(from_latex=rf"P(X \cap A) = \frac{{{a}}}{{{n_tot}}} = 0{{,}}30", to_latex_str=r"P(X \cap A) = P(X) \times P(A) \implies \text{Events are } \textbf{INDEPENDENT}", op="compare with joint probability and conclude", rule="independence test"),
    ]
    canonical = solution_graph(goal="prove events are independent from contingency table", steps=steps, final_latex=r"\text{INDEPENDENT}")
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Product P(X) × P(A) = 0,30", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Joint P(X ∩ A) = 0,30", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Accurate conclusion: INDEPENDENT", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_42", topic=TOPIC_NAME, subskill="42_contingency_independence_test_phone_brand",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=r"\text{INDEPENDENT}", sample_answer=r"P(X \cap A) = 0{,}30 = P(X) \times P(A) \implies \text{INDEPENDENT}",
        canonical_solution=canonical, marking_schema=schema,
        hints={
            "nudge": f"P(Adult) = {row_x}/{n_tot}, P(Android) = {col_a}/{n_tot}. Multiply them and compare to {a}/{n_tot}.",
            "concept": "If the product equals the intersection, they are independent.",
            "breakdown": "0,5 × 0,6 = 0,30. P(Adult ∩ Android) = 0,30. Since 0,30 = 0,30, they are independent.",
        },
        misconception_tags=["assumed_dependent_due_to_non_zero_intersection"], term=3, caps_weight_percent=15, suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 43: Contingency Independence — Strictly Dependent Case
# --------------------------------------------------------------------------- #
def arch_43_contingency_independence_show_dependent(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = r.randint(2, 6)
    a = 18 * k
    b = 7 * k
    c = 7 * k
    d = 18 * k
    row_s = a + b
    col_h = a + c
    n_tot = 50 * k

    tbl_latex = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Diet} & \textbf{High Blood Pressure } (H) & \textbf{Normal } (H') & \textbf{Total} \\ \hline"
        rf"\text{{High Sodium }} (S) & {a} & {b} & {row_s} \\ \hline"
        rf"\text{{Low Sodium }} (S') & {c} & {d} & {row_s} \\ \hline"
        rf"\textbf{{Total}} & {col_h} & {col_h} & {n_tot} \\ \hline"
        r"\end{array}"
    )
    prompt = (
        f"A clinical study evaluated diet and blood pressure among {n_tot} adults:\n\n$${tbl_latex}$$\n\n"
        f"Use mathematical probability formulas to show that following a high-sodium diet ($S$) "
        f"and having high blood pressure ($H$) are DEPENDENT events."
    )
    prompt_latex = rf"\text{{Clinical study of {n_tot} adults. Prove that }} S \text{{ and }} H \text{{ are dependent events.}}"
    steps = [
        step(from_latex=rf"P(S) \times P(H) = \frac{{{row_s}}}{{{n_tot}}} \times \frac{{{col_h}}}{{{n_tot}}} = 0{{,}}5 \times 0{{,}}5 = 0{{,}}25", to_latex_str=r"0{,}25", op="calculate theoretical independent product", rule="multiplication"),
        step(from_latex=rf"P(S \cap H) = \frac{{{a}}}{{{n_tot}}} = 0{{,}}36", to_latex_str=r"0{,}36 \neq 0{,}25 \implies \text{Events are } \textbf{DEPENDENT}", op="show inequality and conclude dependent", rule="dependence proof"),
    ]
    canonical = solution_graph(goal="prove diet and blood pressure are dependent events", steps=steps, final_latex=r"\text{DEPENDENT}")
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Product P(S) × P(H) = 0,25", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Joint P(S ∩ H) = 0,36", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Inequality statement and conclusion: DEPENDENT", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_43", topic=TOPIC_NAME, subskill="43_contingency_independence_show_dependent",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=r"\text{DEPENDENT}", sample_answer=r"P(S \cap H) = 0{,}36 \neq 0{,}25 = P(S) \times P(H) \implies \text{DEPENDENT}",
        canonical_solution=canonical, marking_schema=schema,
        hints={
            "nudge": "Find P(S) × P(H) and show that it does not equal P(S ∩ H).",
            "concept": "If P(A ∩ B) ≠ P(A) × P(B), the events are dependent.",
            "breakdown": "P(S) × P(H) = 0,5 × 0,5 = 0,25. P(S ∩ H) = 0,36. Since 0,36 ≠ 0,25, the events are dependent.",
        },
        misconception_tags=["claimed_independent_without_comparing_numbers"], term=3, caps_weight_percent=15, suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 44: Find Missing Cell Value for Independence
# --------------------------------------------------------------------------- #
def arch_44_contingency_independence_find_missing_for_independence(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    n_tot = 200
    row_a = r.choice([60, 80, 100, 120])
    col_b = r.choice([40, 50, 60, 80])
    x_val = (row_a * col_b) // n_tot

    tbl_latex = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"& \textbf{Option } B & \textbf{Option } B' & \textbf{Total} \\ \hline"
        rf"\textbf{{Group }} A & x & \dots & {row_a} \\ \hline"
        rf"\textbf{{Group }} A' & \dots & \dots & {n_tot - row_a} \\ \hline"
        rf"\textbf{{Total}} & {col_b} & {n_tot - col_b} & {n_tot} \\ \hline"
        r"\end{array}"
    )
    prompt = (
        f"In the contingency table below with grand total {n_tot}:\n\n$${tbl_latex}$$\n\n"
        f"Given that event $A$ and event $B$ are INDEPENDENT, determine the exact value of $x$."
    )
    prompt_latex = rf"\text{{Given }} A \text{{ and }} B \text{{ independent, find }} x."
    steps = [
        step(from_latex=r"P(A \cap B) = P(A) \times P(B)", to_latex_str=rf"\frac{{x}}{{{n_tot}}} = \frac{{{row_a}}}{{{n_tot}}} \times \frac{{{col_b}}}{{{n_tot}}}", op="apply independence product rule in terms of counts", rule="independence product rule"),
        step(from_latex=rf"x = \frac{{{row_a} \times {col_b}}}{{{n_tot}}}", to_latex_str=rf"x = {x_val}", op="multiply and divide to solve for cell value x", rule="algebraic solution"),
    ]
    canonical = solution_graph(goal="determine missing cell value x for events to be independent", steps=steps, final_latex=rf"x = {x_val}")
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Formula setup: x/{n_tot} = ({row_a}/{n_tot}) × ({col_b}/{n_tot})", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Cross-multiplication: x = ({row_a} × {col_b}) / {n_tot}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate integer value x = {x_val}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_44", topic=TOPIC_NAME, subskill="44_contingency_independence_find_missing_for_independence",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=rf"x = {x_val}", sample_answer=rf"x = {x_val}",
        canonical_solution=canonical, marking_schema=schema,
        hints={
            "nudge": "For independence, the intersection cell must equal (row total × column total) / grand total.",
            "concept": "x = (Row Total × Column Total) / N.",
            "breakdown": f"x = ({row_a} × {col_b}) / {n_tot} = {row_a * col_b} / {n_tot} = {x_val}.",
        },
        misconception_tags=["inverted_fraction_in_independence_formula"], term=3, caps_weight_percent=15, suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 45: Contingency Table — Conditional Row Proportion vs Overall
# --------------------------------------------------------------------------- #
def arch_45_contingency_independence_ratio_comparison(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = r.randint(2, 6)
    a = 18 * k
    b = 12 * k
    m_tot = 30 * k
    l_tot = 36 * k
    nl_tot = 24 * k
    n_tot = 60 * k
    p_cond = Fraction(a, m_tot)
    p_overall = Fraction(l_tot, n_tot)

    tbl_latex = (
        r"\begin{array}{|l|c|c|c|}"
        r"\hline"
        r"\textbf{Gender} & \textbf{Licensed } (L) & \textbf{Unlicensed } (L') & \textbf{Total} \\ \hline"
        rf"\text{{Male }} (M) & {a} & {b} & {m_tot} \\ \hline"
        rf"\text{{Female }} (F) & {a} & {b} & {m_tot} \\ \hline"
        rf"\textbf{{Total}} & {l_tot} & {nl_tot} & {n_tot} \\ \hline"
        r"\end{array}"
    )
    prompt = (
        f"Refer to the two-way table below:\n\n$${tbl_latex}$$\n\n"
        f"1. What fraction of Male learners hold a driver's license? (1)\n"
        f"2. What fraction of ALL learners hold a driver's license? (1)\n"
        f"3. Explain what your answers in (1) and (2) tell you about the independence of gender and licensing. (1)"
    )
    prompt_latex = rf"\text{{Compare conditional proportion }} \frac{{{a}}}{{{m_tot}}} \text{{ with overall }} \frac{{{l_tot}}}{{{n_tot}}}."
    steps = [
        step(from_latex=rf"\frac{{n(M \cap L)}}{{n(M)}} = \frac{{{a}}}{{{m_tot}}}", to_latex_str=fmt_frac(p_cond), op="calculate row proportion", rule="conditional proportion"),
        step(from_latex=rf"\frac{{n(L)}}{{N}} = \frac{{{l_tot}}}{{{n_tot}}}", to_latex_str=fmt_frac(p_overall), op="calculate overall proportion", rule="marginal proportion"),
        step(from_latex=rf"\frac{{{a}}}{{{m_tot}}} = \frac{{{l_tot}}}{{{n_tot}}} = {fmt_frac(p_cond)}", to_latex_str=r"\text{Gender has no effect on holding a license } \implies \textbf{INDEPENDENT}", op="compare proportions and deduce independence", rule="proportional independence"),
    ]
    canonical = solution_graph(goal="compare row proportion and overall proportion to deduce independence", steps=steps, final_latex=r"\text{INDEPENDENT}")
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Male proportion = {fmt_frac(p_cond)}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Overall proportion = {fmt_frac(p_overall)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Conclusion: Since proportions are equal, events are independent", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_45", topic=TOPIC_NAME, subskill="45_contingency_independence_ratio_comparison",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=r"\text{INDEPENDENT}", sample_answer=rf"\frac{{{a}}}{{{m_tot}}} = \frac{{{l_tot}}}{{{n_tot}}} = {fmt_frac(p_cond)} \implies \text{{INDEPENDENT}}",
        canonical_solution=canonical, marking_schema=schema,
        hints={
            "nudge": f"Compare {a}/{m_tot} with {l_tot}/{n_tot}. If the proportion is the same across groups, the variables are independent.",
            "concept": "P(L | M) = P(L) implies independence.",
            "breakdown": f"{a}/{m_tot} = 3/5. {l_tot}/{n_tot} = 3/5. Since they are equal, gender and license status are independent.",
        },
        misconception_tags=["confused_conditional_with_joint_probability"], term=3, caps_weight_percent=15, suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 46: Tree Diagram — Independent Trials (With Replacement) (SVG)
# --------------------------------------------------------------------------- #
def arch_46_tree_diagram_two_stage_independent_with_replacement(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_red = r.randint(3, 5)
    n_blue = r.randint(3, 5)
    n_tot = n_red + n_blue

    p_r = Fraction(n_red, n_tot)
    p_b = Fraction(n_blue, n_tot)

    # With replacement => probabilities remain unchanged on stage 2
    p_rr = p_r * p_r
    p_bb = p_b * p_b
    p_same = p_rr + p_bb

    diag_svg = tree_2_svg(
        p_b1=fmt_frac(p_r),
        p_b2=fmt_frac(p_b),
        p_b1_b1=fmt_frac(p_r),
        p_b1_b2=fmt_frac(p_b),
        p_b2_b1=fmt_frac(p_r),
        p_b2_b2=fmt_frac(p_b),
        lbl1="R",
        lbl2="B",
        title="Two-Stage Tree Diagram (With Replacement)",
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Tree Diagram (With Replacement)", "diagram_role": "context"}

    prompt = (
        f"A bag contains {n_red} red marbles and {n_blue} blue marbles (total of {n_tot} marbles).\n"
        f"A marble is drawn at random, its color is recorded, and it is REPLACED in the bag before a second marble is drawn.\n\n"
        f"Refer to the tree diagram below and calculate the probability that BOTH marbles drawn are of the SAME color. "
        f"Write your answer as a simplified fraction."
    )
    prompt_latex = rf"\text{{Draw 2 marbles with replacement: }} {n_red}R, {n_blue}B. \text{{ Calculate }} P(\text{{same color}})."

    steps = [
        step(
            from_latex=r"P(\text{Same}) = P(RR) + P(BB)",
            to_latex_str=rf"\left({fmt_frac(p_r)} \times {fmt_frac(p_r)}\right) + \left({fmt_frac(p_b)} \times {fmt_frac(p_b)}\right)",
            op="multiply branch probabilities and add mutually exclusive outcomes",
            rule="tree diagram multiplication and addition law",
        ),
        step(
            from_latex=rf"{fmt_frac(p_rr)} + {fmt_frac(p_bb)}",
            to_latex_str=fmt_frac(p_same),
            op="sum fractional outcomes",
            rule="fraction addition",
        ),
    ]
    canonical = solution_graph(
        goal="calculate probability of same color with replacement",
        steps=steps,
        final_latex=fmt_frac(p_same),
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"P(RR) = ({fmt_frac(p_r)})^2 and P(BB) = ({fmt_frac(p_b)})^2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Summing both same-color branches", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate simplified fraction {fmt_frac(p_same)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_46",
        topic=TOPIC_NAME,
        subskill="46_tree_diagram_two_stage_independent_with_replacement",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_same),
        sample_answer=fmt_frac(p_same),
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "With replacement, probabilities do not change for the second draw: P(RR) + P(BB).",
            "concept": "Multiply along branches, then add the paths for the same color.",
            "breakdown": f"P(RR) = {fmt_frac(p_r)} × {fmt_frac(p_r)} = {fmt_frac(p_rr)}. P(BB) = {fmt_frac(p_b)} × {fmt_frac(p_b)} = {fmt_frac(p_bb)}. Total = {fmt_frac(p_same)}.",
        },
        misconception_tags=["decreased_denominator_despite_replacement"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 47: Tree Diagram — Dependent Trials (Without Replacement) (SVG)
# --------------------------------------------------------------------------- #
def arch_47_tree_diagram_two_stage_dependent_without_replacement(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    n_red = r.randint(4, 6)
    n_blue = r.randint(3, 5)
    n_tot = n_red + n_blue

    # Stage 1
    p_r1 = Fraction(n_red, n_tot)
    p_b1 = Fraction(n_blue, n_tot)

    # Stage 2 after Red
    p_r2_given_r1 = Fraction(n_red - 1, n_tot - 1)
    p_b2_given_r1 = Fraction(n_blue, n_tot - 1)

    # Stage 2 after Blue
    p_r2_given_b1 = Fraction(n_red, n_tot - 1)
    p_b2_given_b1 = Fraction(n_blue - 1, n_tot - 1)

    # P(at least one red) = 1 - P(BB)
    p_bb = p_b1 * p_b2_given_b1
    p_at_least_one_red = 1 - p_bb

    diag_svg = tree_2_svg(
        p_b1=fmt_frac(p_r1),
        p_b2=fmt_frac(p_b1),
        p_b1_b1=fmt_frac(p_r2_given_r1),
        p_b1_b2=fmt_frac(p_b2_given_r1),
        p_b2_b1=fmt_frac(p_r2_given_b1),
        p_b2_b2=fmt_frac(p_b2_given_b1),
        lbl1="R",
        lbl2="B",
        title="Two-Stage Tree Diagram (WITHOUT Replacement)",
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Tree Diagram (Without Replacement)", "diagram_role": "context"}

    prompt = (
        f"A box contains {n_red} red counters and {n_blue} blue counters (total {n_tot}).\n"
        f"Two counters are drawn one after the other WITHOUT REPLACEMENT.\n\n"
        f"1. Explain why the second draw is dependent on the first draw. (1)\n"
        f"2. Calculate the probability that AT LEAST ONE red counter is drawn. "
        f"Write your answer as a simplified fraction. (3)"
    )
    prompt_latex = rf"\text{{Draw 2 counters without replacement: }} {n_red}R, {n_blue}B. \text{{ Find }} P(\text{{at least one red}})."

    steps = [
        step(
            from_latex=r"\text{Without replacement, both the total number of counters and the number of that color change}",
            to_latex_str=r"\text{Dependent events}",
            op="state reasoning for dependent trials",
            rule="dependent sampling definition",
        ),
        step(
            from_latex=rf"P(BB) = \frac{{{n_blue}}}{{{n_tot}}} \times \frac{{{n_blue - 1}}}{{{n_tot - 1}}}",
            to_latex_str=fmt_frac(p_bb),
            op="calculate probability of drawing two blue counters",
            rule="multiplication rule without replacement",
        ),
        step(
            from_latex=r"P(\text{At least one } R) = 1 - P(BB)",
            to_latex_str=rf"1 - {fmt_frac(p_bb)} = {fmt_frac(p_at_least_one_red)}",
            op="apply complementary rule for at least one",
            rule="complement rule",
        ),
    ]
    canonical = solution_graph(
        goal="calculate probability of at least one red counter without replacement",
        steps=steps,
        final_latex=fmt_frac(p_at_least_one_red),
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Statement that the total and available counters change for the second draw", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Correct second stage fraction {n_blue - 1}/{n_tot - 1}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"P(BB) calculation = {fmt_frac(p_bb)}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate final fraction 1 - P(BB) = {fmt_frac(p_at_least_one_red)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_47",
        topic=TOPIC_NAME,
        subskill="47_tree_diagram_two_stage_dependent_without_replacement",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_at_least_one_red),
        sample_answer=fmt_frac(p_at_least_one_red),
        canonical_solution=canonical,
        marking_schema=schema,
        diagram_spec=diag_spec,
        hints={
            "nudge": "Without replacement, the total becomes N - 1 on the second draw. 'At least one red' is 1 - P(BB).",
            "concept": "P(at least one R) = 1 - P(no R).",
            "breakdown": f"P(BB) = ({n_blue}/{n_tot}) × ({n_blue - 1}/{n_tot - 1}) = {fmt_frac(p_bb)}. P(at least one R) = 1 - {fmt_frac(p_bb)} = {fmt_frac(p_at_least_one_red)}.",
        },
        misconception_tags=["kept_original_denominator_for_second_draw"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
    )


# --------------------------------------------------------------------------- #
# Archetype 48: Tree Diagram — Three-Stage Experiment (Tossing 3 Coins)
# --------------------------------------------------------------------------- #
def arch_48_tree_diagram_three_stage_coins_or_items(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    target_h = r.choice([1, 2])
    # 3 coin tosses => 8 outcomes:
    # 0 H: TTT (1)
    # 1 H: HTT, THT, TTH (3)
    # 2 H: HHT, HTH, THH (3)
    # 3 H: HHH (1)
    n_fav = 3
    frac_ans = Fraction(n_fav, 8)

    prompt = (
        f"A fair coin is tossed THREE times consecutively.\n\n"
        f"1. How many possible outcomes are in the sample space $S$? (1)\n"
        f"2. Calculate the probability of getting EXACTLY {target_h} Heads. "
        f"Write your answer as a simplified fraction. (2)"
    )
    prompt_latex = rf"\text{{Toss coin 3 times. Find }} n(S) \text{{ and }} P(\text{{exactly }}{target_h}\text{{ Heads}})."

    steps = [
        step(
            from_latex=r"n(S) = 2 \times 2 \times 2 = 2^3",
            to_latex_str=r"8",
            op="calculate total sample space outcomes",
            rule="fundamental counting principle",
        ),
        step(
            from_latex=rf"\text{{Favorable outcomes with {target_h} Heads: 3 out of 8}}",
            to_latex_str=fmt_frac(frac_ans),
            op="form probability fraction",
            rule="classical probability definition",
        ),
    ]
    canonical = solution_graph(
        goal="determine sample space and probability for 3 coin tosses",
        steps=steps,
        final_latex=rf"n(S) = 8; \quad P(\text{{exactly {target_h} Heads}}) = {fmt_frac(frac_ans)}",
    )
    schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "n(S) = 8 outcomes", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Listing or counting 3 favorable branches", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate fraction {fmt_frac(frac_ans)}", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_48",
        topic=TOPIC_NAME,
        subskill="48_tree_diagram_three_stage_coins_or_items",
        learning_objective_id=LEARNING_OBJECTIVE_ID,
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=fmt_frac(frac_ans),
        sample_answer=rf"n(S) = 8; \quad P = {fmt_frac(frac_ans)}",
        canonical_solution=canonical,
        marking_schema=schema,
        hints={
            "nudge": "Each toss has 2 outcomes, so 2 × 2 × 2 = 8 total outcomes.",
            "concept": "List the outcomes with the target number of heads: e.g. HHT, HTH, THH.",
            "breakdown": f"Total outcomes = 8. Exactly {target_h} Heads appears in 3 outcomes. P = {fmt_frac(frac_ans)}.",
        },
        misconception_tags=["miscounted_three_stage_outcomes"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
    )


# --------------------------------------------------------------------------- #
# Archetype 49: Capstone — Integrated Venn Diagram & Independence Test (SVG)
# --------------------------------------------------------------------------- #
def arch_49_capstone_integrated_venn_and_independence(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    k = r.randint(2, 5)
    n_tot = 60 * k
    n_a = 30 * k
    n_b = 24 * k
    x_val = 9 * k
    only_a = n_a - x_val
    only_b = n_b - x_val
    outside = n_tot - (only_a + x_val + only_b)
    n_union = n_tot - outside

    diag_svg = venn_2_svg(
        only_a=rf"{n_a} - x",
        only_b=rf"{n_b} - x",
        both="x",
        outside=str(outside),
        label_a="A",
        label_b="B",
        title="Comprehensive Capstone Venn Diagram",
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Capstone Venn Diagram", "diagram_role": "context"}

    p_a = Fraction(n_a, n_tot)
    p_b = Fraction(n_b, n_tot)
    prod = p_a * p_b
    p_both = Fraction(x_val, n_tot)
    p_union = Fraction(n_union, n_tot)

    prompt = (
        f"In a cohort of {n_tot} Grade 11 learners, events $A$ and $B$ satisfy:\n"
        f"- $n(A) = {n_a}$\n"
        f"- $n(B) = {n_b}$\n"
        f"- $n(A \\cap B) = x$\n"
        f"- {outside} learners participate in neither event.\n\n"
        f"1. Set up an equation and show that $x = {x_val}$. (2)\n"
        f"2. Calculate $P(A \\cup B)$. (2)\n"
        f"3. Prove mathematically whether events $A$ and $B$ are independent or dependent. (3)"
    )
    prompt_latex = rf"\text{{Capstone: Total }} {n_tot}, n(A)={n_a}, n(B)={n_b}, n(\text{{neither}})={outside}. \text{{ Solve }} x, P(A \cup B), \text{{ and test independence.}}"
    steps = [
        step(from_latex=rf"({n_a} - x) + x + ({n_b} - x) + {outside} = {n_tot}", to_latex_str=rf"{n_a + n_b + outside} - x = {n_tot} \implies x = {x_val}", op="solve linear equation for intersection count x", rule="linear equation solution"),
        step(from_latex=rf"P(A \cup B) = \frac{{{n_union}}}{{{n_tot}}}", to_latex_str=fmt_frac(p_union), op="calculate union probability", rule="union definition"),
        step(from_latex=rf"P(A) \times P(B) = \frac{{{n_a}}}{{{n_tot}}} \times \frac{{{n_b}}}{{{n_tot}}} = {fmt_frac(prod)}", to_latex_str=rf"P(A \cap B) = \frac{{{x_val}}}{{{n_tot}}} = {fmt_frac(p_both)} \neq {fmt_frac(prod)} \implies \textbf{{DEPENDENT}}", op="compare intersection with product of marginals and conclude", rule="independence test"),
    ]
    canonical = solution_graph(goal="solve for x, evaluate union, and prove events are dependent", steps=steps, final_latex=rf"x = {x_val}; \quad P(A \cup B) = {fmt_frac(p_union)}; \quad \text{{DEPENDENT}}")
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": rf"Equation setup: ({n_a} - x) + x + ({n_b} - x) + {outside} = {n_tot}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate solution x = {x_val}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Union count: {n_union}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate simplified union: {fmt_frac(p_union)}", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Product P(A) × P(B) = {fmt_frac(prod)}", "marks": 1, "editable": True},
            {"id": "mp6", "desc": f"Intersection P(A ∩ B) = {fmt_frac(p_both)}", "marks": 1, "editable": True},
            {"id": "mp7", "desc": "Comparison and conclusion: DEPENDENT", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_49", topic=TOPIC_NAME, subskill="49_capstone_integrated_venn_and_independence",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=rf"x = {x_val}; \quad {fmt_frac(p_union)}; \quad \text{{DEPENDENT}}",
        sample_answer=rf"x = {x_val}; \quad P(A \cup B) = {fmt_frac(p_union)}; \quad \text{{DEPENDENT}}",
        canonical_solution=canonical, marking_schema=schema, diagram_spec=diag_spec,
        hints={
            "nudge": "1. Sum the 4 regions to find x. 2. Union is 1 - P(neither). 3. Compare P(A) × P(B) with P(A ∩ B).",
            "concept": "A and B are independent iff P(A ∩ B) = P(A) × P(B).",
            "breakdown": f"x = {x_val}. P(A ∪ B) = {fmt_frac(p_union)}. P(A) × P(B) = {fmt_frac(prod)}. P(A ∩ B) = {fmt_frac(p_both)}. Conclusion: DEPENDENT.",
        },
        misconception_tags=["assumed_independence_without_algebraic_test"], term=3, caps_weight_percent=15, suggested_duration_mins=8,
    )


# --------------------------------------------------------------------------- #
# Archetype 50: Capstone — Comprehensive Tree & Contingency Synthesis (SVG)
# --------------------------------------------------------------------------- #
def arch_50_capstone_contingency_tree_dependent_synthesis(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    n_black = r.randint(5, 8)
    n_blue = r.randint(3, 6)
    n_pens = n_black + n_blue

    p_bb = Fraction(n_black, n_pens) * Fraction(n_black - 1, n_pens - 1)
    p_blue_blue = Fraction(n_blue, n_pens) * Fraction(n_blue - 1, n_pens - 1)
    p_diff = 1 - (p_bb + p_blue_blue)

    diag_svg = tree_2_svg(
        p_b1=f"{n_black}/{n_pens}",
        p_b2=f"{n_blue}/{n_pens}",
        p_b1_b1=f"{n_black-1}/{n_pens-1}",
        p_b1_b2=f"{n_blue}/{n_pens-1}",
        p_b2_b1=f"{n_black}/{n_pens-1}",
        p_b2_b2=f"{n_blue-1}/{n_pens-1}",
        lbl1="Black",
        lbl2="Blue",
        title="Pen Selection Tree Diagram (Without Replacement)",
    )
    diag_spec = {"kind": "inline_svg", "svg": diag_svg, "title": "Tree Diagram Synthesis", "diagram_role": "context"}

    prompt = (
        f"A pencil case contains {n_black} black pens and {n_blue} blue pens (total of {n_pens} pens).\n"
        f"A learner draws two pens at random, one after the other, WITHOUT replacement.\n\n"
        f"1. Refer to the tree diagram below and calculate the probability that BOTH pens drawn are black. (2)\n"
        f"2. Calculate the probability that the two pens drawn are of DIFFERENT colors. (3)\n"
        f"3. Explain why the events 'First pen is black' and 'Second pen is black' are dependent. (1)"
    )
    prompt_latex = rf"\text{{Draw 2 pens without replacement: }} {n_black}\text{{ Black, }} {n_blue}\text{{ Blue. Calculate }} P(\text{{both Black}}) \text{{ and }} P(\text{{different colors}})."
    steps = [
        step(from_latex=rf"P(\text{{Both Black}}) = \frac{{{n_black}}}{{{n_pens}}} \times \frac{{{n_black-1}}}{{{n_pens-1}}}", to_latex_str=fmt_frac(p_bb), op="multiply black branch probabilities without replacement", rule="multiplication rule without replacement"),
        step(from_latex=r"P(\text{Different}) = P(\text{Black, Blue}) + P(\text{Blue, Black})", to_latex_str=rf"\left(\frac{{{n_black}}}{{{n_pens}}} \times \frac{{{n_blue}}}{{{n_pens-1}}}\right) + \left(\frac{{{n_blue}}}{{{n_pens}}} \times \frac{{{n_black}}}{{{n_pens-1}}}\right) = {fmt_frac(p_diff)}", op="sum mutually exclusive paths for different colors", rule="tree diagram path summation"),
        step(from_latex=r"\text{The outcome of the first draw alters the total number of pens and black pens available}", to_latex_str=r"\text{Dependent events}", op="state dependency condition", rule="dependent trials"),
    ]
    canonical = solution_graph(goal="calculate both black and different color probabilities without replacement", steps=steps, final_latex=rf"P(\text{{Both Black}}) = {fmt_frac(p_bb)}; \quad P(\text{{Different}}) = {fmt_frac(p_diff)}")
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Setup: ({n_black}/{n_pens}) × ({n_black-1}/{n_pens-1})", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accurate fraction P(Both Black) = {fmt_frac(p_bb)}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Setup for different colors: ({n_black}/{n_pens})({n_blue}/{n_pens-1}) + ({n_blue}/{n_pens})({n_black}/{n_pens-1})", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Adding the two path products", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Accurate simplified fraction {fmt_frac(p_diff)}", "marks": 1, "editable": True},
            {"id": "mp6", "desc": "Explanation of dependent condition (changing totals)", "marks": 1, "editable": True},
        ],
    }
    return make_math_question(
        prefix="g11_prob_50", topic=TOPIC_NAME, subskill="50_capstone_contingency_tree_dependent_synthesis",
        learning_objective_id=LEARNING_OBJECTIVE_ID, prompt=prompt, prompt_latex=prompt_latex,
        answer_latex=fmt_frac(p_diff), sample_answer=rf"P(\text{{Both Black}}) = {fmt_frac(p_bb)}; \quad P(\text{{Different}}) = {fmt_frac(p_diff)}",
        canonical_solution=canonical, marking_schema=schema, diagram_spec=diag_spec,
        hints={
            "nudge": f"Without replacement, the second draw is out of {n_pens-1} pens. Different colors means Black-then-Blue OR Blue-then-Black.",
            "concept": "P(diff) = P(Black, Blue) + P(Blue, Black).",
            "breakdown": f"P(Both Black) = ({n_black}/{n_pens}) × ({n_black-1}/{n_pens-1}) = {fmt_frac(p_bb)}. P(Diff) = {fmt_frac(p_diff)}.",
        },
        misconception_tags=["omitted_one_of_the_two_different_color_orders"], term=3, caps_weight_percent=15, suggested_duration_mins=7,
    )


# --------------------------------------------------------------------------- #
# Export Dictionary for Archetypes 26 to 50
# --------------------------------------------------------------------------- #
ARCHETYPE_BUILDERS_26_50 = {
    "26_venn_3_read_all_three_and_none": arch_26_venn_3_read_all_three_and_none,
    "27_venn_3_read_exactly_one_subject": arch_27_venn_3_read_exactly_one_subject,
    "28_venn_3_read_at_least_two_subjects": arch_28_venn_3_read_at_least_two_subjects,
    "29_venn_3_read_two_subjects_only": arch_29_venn_3_read_two_subjects_only,
    "30_venn_3_union_formula_verification": arch_30_venn_3_union_formula_verification,
    "31_venn_3_algebraic_x_central_intersection": arch_31_venn_3_algebraic_x_central_intersection,
    "32_venn_3_algebraic_x_given_at_least_one": arch_32_venn_3_algebraic_x_given_at_least_one,
    "33_venn_3_algebraic_x_outside_and_center": arch_33_venn_3_algebraic_x_outside_and_center,
    "34_venn_3_contextual_survey_school_clubs": arch_34_venn_3_contextual_survey_school_clubs,
    "35_venn_3_contextual_survey_streaming_services": arch_35_venn_3_contextual_survey_streaming_services,
    "36_contingency_table_complete_missing_totals": arch_36_contingency_table_complete_missing_totals,
    "37_contingency_table_solve_unknown_cell_x": arch_37_contingency_table_solve_unknown_cell_x,
    "38_contingency_table_joint_and_marginal_probabilities": arch_38_contingency_table_joint_and_marginal_probabilities,
    "39_contingency_table_driver_license_survey": arch_39_contingency_table_driver_license_survey,
    "40_contingency_table_medical_test_or_vaccine": arch_40_contingency_table_medical_test_or_vaccine,
    "41_contingency_independence_test_gender_subject": arch_41_contingency_independence_test_gender_subject,
    "42_contingency_independence_test_phone_brand": arch_42_contingency_independence_test_phone_brand,
    "43_contingency_independence_show_dependent": arch_43_contingency_independence_show_dependent,
    "44_contingency_independence_find_missing_for_independence": arch_44_contingency_independence_find_missing_for_independence,
    "45_contingency_independence_ratio_comparison": arch_45_contingency_independence_ratio_comparison,
    "46_tree_diagram_two_stage_independent_with_replacement": arch_46_tree_diagram_two_stage_independent_with_replacement,
    "47_tree_diagram_two_stage_dependent_without_replacement": arch_47_tree_diagram_two_stage_dependent_without_replacement,
    "48_tree_diagram_three_stage_coins_or_items": arch_48_tree_diagram_three_stage_coins_or_items,
    "49_capstone_integrated_venn_and_independence": arch_49_capstone_integrated_venn_and_independence,
    "50_capstone_contingency_tree_dependent_synthesis": arch_50_capstone_contingency_tree_dependent_synthesis,
}
