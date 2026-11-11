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

SUBSKILLS = [
    "linear_numeric_patterns",
    "general_rule_formula",
    "calculate_large_term",
    "find_term_position",
    "geometric_matchstick_patterns"
]


def _generate_general_rule_question(rng: random.Random) -> Dict[str, Any]:
    """Generates question asking specifically for the general rule Tn."""
    diff = rng.randint(3, 8)
    first_term = rng.randint(1, 12)
    c = first_term - diff
    terms = [first_term + diff * i for i in range(4)]
    terms_str = ", ".join(str(t) for t in terms) + ", \\dots"
    rule_str = f"{diff}n {'+' if c > 0 else '-'} {abs(c)}" if c != 0 else f"{diff}n"

    prompt = (
        f"Study the following linear sequence of numbers:\n\n"
        f"$${terms_str}$$\n\n"
        f"1. What is the constant difference ($d$) between successive terms?\n"
        f"2. Write down the algebraic formula for the **general rule ($T_n$)** in terms of $n$."
    )
    sol = (
        f"**Step 1:** Calculate constant difference:\n\n"
        f"$$d = {terms[1]} - {terms[0]} = {diff}$$\n\n"
        f"**Step 2:** Formulate general rule:\n\n"
        f"$$T_n = d \\times n + c$$\n\n"
        f"Using $T_1 = {first_term}$: $${diff}(1) + c = {first_term} \\implies c = {c}$$\n\n"
        f"$$\\therefore T_n = \\mathbf{{{rule_str}}}$$"
    )
    return {
        "id": f"g7_math_pat_rule_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"d = {diff}; Tn = {rule_str}",
        "answer_latex": f"T_n = {rule_str}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": "numeric_patterns_subskill_2",
        "learning_objective_id": "math_g7_patterns_rule_formula",
        "misconception_tags": ["first_difference_multiplication_omission"],
        "diagnostic_tags": ["patterns", "general_rule"],
        "minimum_mastery_score": 75,
        "keywords": ["general rule", "Tn", "formula"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Identification of difference d = {diff}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct formula Tn = {rule_str}", "marks": 2, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Find the constant difference d first.",
            "tier_2": f"The formula is Tn = d*n + c. Here d = {diff}.",
            "tier_3": f"Tn = {rule_str}."
        }
    }


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
        "subskill": "geometric_matchstick_patterns",
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


def _generate_next_terms_question(rng: random.Random) -> Dict[str, Any]:
    """Generates next three terms question from a given linear sequence."""
    diff = rng.randint(4, 11)
    t1 = rng.randint(3, 19)
    terms = [t1 + diff * i for i in range(4)]
    next_3 = [t1 + diff * (4 + i) for i in range(3)]
    terms_str = ", ".join(str(t) for t in terms) + ", \\dots"
    ans_str = ", ".join(str(t) for t in next_3)

    prompt = (
        f"Consider the number sequence:\n\n"
        f"$${terms_str}$$\n\n"
        f"1. Write down the constant difference ($d$) between consecutive terms.\n"
        f"2. Write down the next THREE terms of the sequence."
    )
    sol = (
        f"**Step 1:** The constant difference is:\n\n"
        f"$$d = {terms[1]} - {terms[0]} = {diff}$$\n\n"
        f"**Step 2:** Add $d = {diff}$ to find the next three terms:\n\n"
        f"- Next term: ${terms[3]} + {diff} = {next_3[0]}$\n"
        f"- Next term: ${next_3[0]} + {diff} = {next_3[1]}$\n"
        f"- Next term: ${next_3[1]} + {diff} = {next_3[2]}$\n\n"
        f"$$\\therefore \\text{{Next 3 terms are }} \\mathbf{{{ans_str}}}$$"
    )
    return {
        "id": f"g7_math_pat_next_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"d = {diff}; {ans_str}",
        "answer_latex": f"d = {diff};\\ {ans_str}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": "linear_numeric_patterns",
        "learning_objective_id": "math_g7_patterns_next_terms",
        "misconception_tags": ["arithmetic_addition_error"],
        "diagnostic_tags": ["patterns", "sequences"],
        "minimum_mastery_score": 75,
        "keywords": ["constant difference", "next terms", "linear sequence"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct difference d = {diff}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct calculation of 3 consecutive terms", "marks": 3, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Find how much is added from one number to the next.",
            "tier_2": f"The difference is {diff}. Add {diff} to the last given number ({terms[3]}).",
            "tier_3": f"Next terms are {ans_str}."
        }
    }


def _generate_term_position_question(rng: random.Random) -> Dict[str, Any]:
    """Determines the position n of a given term value in a sequence."""
    diff = rng.randint(3, 8)
    first_term = rng.randint(2, 10)
    c = first_term - diff
    target_pos = rng.randint(12, 30)
    target_val = first_term + diff * (target_pos - 1)
    terms = [first_term + diff * i for i in range(4)]
    terms_str = ", ".join(str(t) for t in terms) + ", \\dots"
    rule_str = f"{diff}n {'+' if c > 0 else '-'} {abs(c)}" if c != 0 else f"{diff}n"

    prompt = (
        f"A number pattern begins:\n\n"
        f"$${terms_str}$$\n\n"
        f"Which term of the pattern has a value of **{target_val}**? (Find the position $n$ where $T_n = {target_val}$)."
    )
    sol = (
        f"**Step 1:** The general rule is:\n\n"
        f"$$T_n = {diff}n + ({c}) = {rule_str}$$\n\n"
        f"**Step 2:** Set $T_n = {target_val}$ and solve for $n$:\n\n"
        f"$${rule_str} = {target_val}$$\n\n"
        f"$${diff}n = {target_val} - ({c}) = {target_val - c}$$\n\n"
        f"$$n = \\frac{{{target_val - c}}}{{{diff}}} = {target_pos}$$\n\n"
        f"$$\\therefore \\text{{The }} \\mathbf{{{target_pos}\\text{{th term}}}} \\text{{ has a value of }} {target_val}$$"
    )
    return {
        "id": f"g7_math_pat_pos_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(target_pos),
        "answer_latex": f"n = {target_pos}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": "numeric_patterns_subskill_4",
        "learning_objective_id": "math_g7_patterns_term_position",
        "misconception_tags": ["confused_term_value_with_position"],
        "diagnostic_tags": ["patterns", "equations"],
        "minimum_mastery_score": 75,
        "keywords": ["term position", "solve for n", "general rule"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Setting up equation with general rule", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Isolating n", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct position n = {target_pos}", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"First find the general rule Tn = {rule_str}.",
            "tier_2": f"Set {rule_str} = {target_val} and solve for n.",
            "tier_3": f"n = {target_pos}."
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
    - linear_numeric_patterns
    - numeric_patterns_subskill_2 (general rule)
    - numeric_patterns_subskill_3 (large position term)
    - numeric_patterns_subskill_4 (find term position)
    - numeric_patterns_subskill_5 (geometric matchsticks)
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions = []

    sub_str = str(subskill or "").lower()

    for _ in range(count):
        if "matchstick" in sub_str or "subskill_5" in sub_str or "geometric" in sub_str:
            q = _generate_geometric_matchstick_question(rng)
        elif "position" in sub_str or "subskill_4" in sub_str:
            q = _generate_term_position_question(rng)
        elif "large" in sub_str or "subskill_3" in sub_str:
            q = _generate_numeric_sequence_question(rng, difficulty="hard")
        elif "rule" in sub_str or "subskill_2" in sub_str:
            q = _generate_general_rule_question(rng)
        elif sub_str:
            q = _generate_next_terms_question(rng)
        elif mode == "elementary_matchsticks":
            q = _generate_geometric_matchstick_question(rng)
        else: # compound / numeric
            q = rng.choice([
                _generate_next_terms_question,
                _generate_numeric_sequence_question,
                _generate_term_position_question,
                _generate_geometric_matchstick_question
            ])(rng)
        questions.append(q)

    return questions
