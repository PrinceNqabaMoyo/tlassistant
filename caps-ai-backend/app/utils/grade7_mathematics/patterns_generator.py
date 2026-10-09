"""
Grade 7 Mathematics - Numeric and Geometric Patterns Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.

Topics Covered (Grade 7 Terms 1 & 2):
- Numeric patterns with constant difference
- General rule formulation in words and algebraic notation (Tn = an + b)
- Finding the next terms in a sequence
- Calculating the value of large position terms (e.g. 20th or 50th term)
- Determining the position of a given term
- Geometric patterns (matchsticks, tile tables)
"""

from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


def _generate_numeric_sequence_question(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    """Generates linear sequence questions with constant difference."""
    diff = rng.randint(3, 9) if difficulty != "easy" else rng.randint(2, 5)
    first_term = rng.randint(2, 15)
    # T_n = diff * n + (first_term - diff)
    c = first_term - diff

    terms = [first_term + diff * i for i in range(4)]
    target_n = rng.choice([15, 20, 25, 50])
    target_val = first_term + diff * (target_n - 1)

    terms_str = ", ".join(str(t) for t in terms) + ", \\dots"

    rule_str = f"{diff}n {'+' if c > 0 else '-'} {abs(c)}" if c != 0 else f"{diff}n"

    prompt = (
        f"Consider the number pattern:\n\n"
        f"$${terms_str}$$\n\n"
        f"1. Determine the constant difference between consecutive terms.\n"
        f"2. Write down the general rule ($T_n$) for the pattern.\n"
        f"3. Hence, calculate the value of the **{target_n}th term** ($T_{{{target_n}}}$)."
    )

    sol = (
        f"**Step 1:** The constant difference is:\n\n"
        f"$$d = {terms[1]} - {terms[0]} = {diff}$$\n\n"
        f"**Step 2:** Formulate the general rule:\n\n"
        f"$$T_n = d \\times n + c$$\n\n"
        f"For $n = 1$: $T_1 = {diff}(1) + c = {first_term} \\implies c = {c}$\n\n"
        f"$$\\therefore T_n = {rule_str}$$\n\n"
        f"**Step 3:** Calculate $T_{{{target_n}}}$:\n\n"
        f"$$T_{{{target_n}}} = {diff}({target_n}) {'+' if c > 0 else '-'} {abs(c)} = {target_val}$$"
    )

    return {
        "id": f"g7_math_pat_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"d = {diff}; Tn = {rule_str}; T{target_n} = {target_val}",
        "answer_latex": f"T_{{n}} = {rule_str};\\ T_{{{target_n}}} = {target_val}",
        "answer_sympy": str(target_val),
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "subskill": "linear_numeric_patterns",
        "learning_objective_id": "math_g7_patterns_general_rule",
        "misconception_tags": [
            "confused_term_value_with_position",
            "first_difference_multiplication_omission",
            "sign_error_in_constant_term"
        ],
        "diagnostic_tags": ["arithmetic_patterns", "algebraic_generalisation"],
        "minimum_mastery_score": 75,
        "keywords": ["constant difference", "general rule", "position", "term"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification of constant difference d", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Derivation of constant term c", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Correct general rule Tn formula", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Correct substitution into general rule", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Accurate evaluated target term", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Subtract the first term from the second term to find the constant difference d.",
            "tier_2": f"The general rule for a linear pattern is Tn = d*n + c, where d is {diff}.",
            "tier_3": f"d = {diff}, Tn = {rule_str}, and T_{target_n} = {target_val}."
        }
    }


def _generate_geometric_matchstick_question(rng: random.Random) -> Dict[str, Any]:
    """Generates geometric pattern questions based on shapes (triangles or squares formed by matchsticks)."""
    shape_type = rng.choice(["triangles", "squares"])
    if shape_type == "triangles":
        # 1 triangle = 3 sticks, 2 triangles = 5 sticks, 3 = 7 sticks (diff = 2, c = 1)
        name = "triangles"
        diff = 2
        c = 1
        terms = [3, 5, 7, 9]
    else:
        # 1 square = 4 sticks, 2 squares = 7 sticks, 3 = 10 sticks (diff = 3, c = 1)
        name = "squares"
        diff = 3
        c = 1
        terms = [4, 7, 10, 13]

    target_shapes = rng.choice([12, 15, 20])
    target_sticks = diff * target_shapes + c

    prompt = (
        f"A pattern of connected {name} is built using matchsticks:\n\n"
        f"- Figure 1 has **{terms[0]}** matchsticks.\n"
        f"- Figure 2 has **{terms[1]}** matchsticks.\n"
        f"- Figure 3 has **{terms[2]}** matchsticks.\n\n"
        f"1. How many additional matchsticks are needed for each new {name[:-1]}?\n"
        f"2. Write a formula connecting the number of matchsticks ($M$) to the figure number ($n$).\n"
        f"3. Calculate the total number of matchsticks required to build Figure {target_shapes}."
    )

    sol = (
        f"**Step 1:** The number of matchsticks added per figure is the constant difference:\n\n"
        f"$$d = {terms[1]} - {terms[0]} = {diff}$$\n\n"
        f"**Step 2:** General formula: $$M = {diff}n + {c}$$\n\n"
        f"**Step 3:** For Figure {target_shapes} ($n = {target_shapes}$):\n\n"
        f"$$M = {diff}({target_shapes}) + {c} = {target_sticks}$$ matchsticks."
    )

    return {
        "id": f"g7_math_geom_pat_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"Difference = {diff}; M = {diff}n + {c}; M = {target_sticks}",
        "answer_latex": f"M = {diff}n + {c};\\ M({target_shapes}) = {target_sticks}",
        "answer_sympy": str(target_sticks),
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "subskill": "geometric_patterns",
        "learning_objective_id": "math_g7_patterns_geometric_matchsticks",
        "misconception_tags": [
            "multiplied_without_accounting_for_shared_sides",
            "overcounting_shared_edges"
        ],
        "diagnostic_tags": ["spatial_patterns", "formula_modeling"],
        "minimum_mastery_score": 75,
        "keywords": ["matchstick pattern", "figure number", "shared sides", "formula"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification of additional sticks per shape", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct formula relating M and n", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Accurate calculation of sticks for target figure", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Notice how each new figure shares a side with the previous figure.",
            "tier_2": f"Each extra {name[:-1]} adds {diff} sticks. The formula is M = {diff}n + 1.",
            "tier_3": f"For n = {target_shapes}, M = {diff}({target_shapes}) + 1 = {target_sticks}."
        }
    }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Patterns Question Generator.
    Supports atomic micro-drills:
    - mode="elementary_constant_difference"
    - mode="elementary_matchsticks"
    - mode="compound"
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions = []

    for _ in range(count):
        if mode == "elementary_matchsticks" or subskill == "matchsticks":
            q = _generate_geometric_matchstick_question(rng)
        else: # compound / numeric
            q = _generate_numeric_sequence_question(rng, difficulty)
        questions.append(q)

    return questions
