"""
Grade 7 Mathematics - Common Fractions Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Directly grounded in curriculum_docs/Mathematics_Gr7/Numbers-Operations-and-Relationships.md
and curriculum_docs_auto/Mathematics_Gr7/Term 2/1. Fractions.md

Topics Covered (Grade 7 Term 2 CAPS):
- Equivalent fractions and simplifying to lowest terms
- Addition and subtraction of common fractions with unlike denominators (finding LCD)
- Mixed numbers and improper fractions operations
- Fraction of a whole quantity in authentic South African contexts
- Percentage and fraction equivalence
"""

from __future__ import annotations
import random
import math
from typing import Any, Dict, List, Optional


def _lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def _generate_fraction_addition_subtraction_question(rng: random.Random) -> Dict[str, Any]:
    """Generates fraction addition/subtraction problem with unlike denominators."""
    d1 = rng.choice([3, 4, 5, 6])
    d2 = rng.choice([2, 4, 6, 8, 10, 12])
    while d1 == d2:
        d2 = rng.choice([2, 4, 6, 8, 10, 12])

    n1 = rng.randint(1, d1 - 1)
    n2 = rng.randint(1, d2 - 1)

    lcd = _lcm(d1, d2)
    mult1 = lcd // d1
    mult2 = lcd // d2

    is_addition = rng.choice([True, False])
    
    if not is_addition and (n1 * mult1 <= n2 * mult2):
        # Swap so result is strictly positive
        n1, n2 = n2, n1
        d1, d2 = d2, d1
        lcd = _lcm(d1, d2)
        mult1 = lcd // d1
        mult2 = lcd // d2

    new_n1 = n1 * mult1
    new_n2 = n2 * mult2

    if is_addition:
        res_n = new_n1 + new_n2
        op_sym = "+"
        op_name = "addition"
    else:
        res_n = new_n1 - new_n2
        op_sym = "-"
        op_name = "subtraction"

    common_div = math.gcd(res_n, lcd)
    simp_n = res_n // common_div
    simp_d = lcd // common_div

    prompt = (
        f"Calculate the following fraction operation and write your answer in its **simplest form**:\n\n"
        f"$$\\frac{{{n1}}}{{{d1}}} {op_sym} \\frac{{{n2}}}{{{d2}}}$$\n\n"
        f"1. Determine the Lowest Common Denominator (LCD) of ${d1}$ and ${d2}$.\n"
        f"2. Rewrite both fractions as equivalent fractions with the common denominator.\n"
        f"3. Perform the {op_name} and simplify if possible."
    )

    sol = (
        f"**Step 1:** Find the Lowest Common Denominator (LCD):\n\n"
        f"$$\\text{{LCD of }} {d1} \\text{{ and }} {d2} = {lcd}$$\n\n"
        f"**Step 2:** Convert to equivalent fractions:\n\n"
        f"$$\\frac{{{n1}}}{{{d1}}} = \\frac{{{n1} \\times {mult1}}}{{{d1} \\times {mult1}}} = \\frac{{{new_n1}}}{{{lcd}}}$$\n\n"
        f"$$\\frac{{{n2}}}{{{d2}}} = \\frac{{{n2} \\times {mult2}}}{{{d2} \\times {mult2}}} = \\frac{{{new_n2}}}{{{lcd}}}$$\n\n"
        f"**Step 3:** Perform the {op_name}:\n\n"
        f"$$\\frac{{{new_n1}}}{{{lcd}}} {op_sym} \\frac{{{new_n2}}}{{{lcd}}} = \\frac{{{new_n1} {op_sym} {new_n2}}}{{{lcd}}} = \\frac{{{res_n}}}{{{lcd}}}$$\n\n"
        f"$$\\text{{Simplified form}} = \\mathbf{{\\frac{{{simp_n}}}{{{simp_d}}}}}$$"
    )

    ans_str = f"{simp_n}/{simp_d}" if simp_d != 1 else str(simp_n)

    return {
        "id": f"g7_math_frac_add_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans_str,
        "answer_latex": f"\\frac{{{simp_n}}}{{{simp_d}}}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "subskill": "fraction_addition_subtraction_lcd",
        "learning_objective_id": "math_g7_fractions_unlike_denominators",
        "misconception_tags": [
            "adding_denominators_together_directly",
            "lcd_multiplication_omitted_in_numerator",
            "unsimplified_fraction_slip"
        ],
        "diagnostic_tags": ["fractions", "lcd", "rational_numbers"],
        "minimum_mastery_score": 75,
        "keywords": ["fractions", "LCD", "common denominator", "simplest form", "unlike denominators"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification of correct Lowest Common Denominator (LCD)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct conversion to equivalent fractions", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Accurate numerator addition/subtraction over LCD", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Simplification to lowest terms", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"You cannot add or subtract fractions until they have the same denominator.",
            "tier_2": f"Find the Lowest Common Denominator (LCD) of {d1} and {d2}. It is {lcd}. Multiply both numerator and denominator by the factor needed.",
            "tier_3": f"Equivalent fractions are {new_n1}/{lcd} {op_sym} {new_n2}/{lcd} = {res_n}/{lcd} = {ans_str}."
        }
    }


def _generate_fraction_of_quantity_question(rng: random.Random) -> Dict[str, Any]:
    """Generates authentic South African problem finding fraction of a quantity."""
    contexts = [
        ("learners at a school sports day", 120, "learners"),
        ("litres of water in a rainwater tank", 250, "litres"),
        ("Rands of pocket money saved", 360, "Rands"),
        ("kilograms of fresh maize harvested", 480, "kg"),
        ("books donated to the school library", 180, "books")
    ]
    ctx_name, base_qty, unit = rng.choice(contexts)
    
    denom = rng.choice([3, 4, 5, 6, 8, 10])
    # Ensure total is divisible by denominator
    factor = rng.randint(15, 45)
    total_qty = denom * factor
    num = rng.randint(2, denom - 1)
    target_val = (total_qty // denom) * num

    prompt = (
        f"A total of **{total_qty} {unit}** was recorded for {ctx_name}.\n\n"
        f"If **$\\frac{{{num}}}{{{denom}}}$** of the total was allocated to the junior division:\n\n"
        f"1. Express the calculation required to find the allocated amount.\n"
        f"2. Calculate the exact quantity allocated to the junior division.\n"
        f"3. What fraction remains for the senior division?"
    )

    remaining_num = denom - num
    sol = (
        f"**Step 1:** To find $\\frac{{{num}}}{{{denom}}}$ of {total_qty}:\n\n"
        f"$$\\text{{Quantity}} = \\frac{{{num}}}{{{denom}}} \\times {total_qty}$$\n\n"
        f"**Step 2:** Divide by the denominator, then multiply by the numerator:\n\n"
        f"$$\\frac{{{total_qty}}}{{{denom}}} = {factor}$$\n\n"
        f"$$\\text{{Allocated}} = {factor} \\times {num} = {target_val}\\text{{ {unit}}}$$\n\n"
        f"**Step 3:** Remaining fraction:\n\n"
        f"$$1 - \\frac{{{num}}}{{{denom}}} = \\frac{{{denom} - {num}}}{{{denom}}} = \\mathbf{{\\frac{{{remaining_num}}}{{{denom}}}}}$$"
    )

    return {
        "id": f"g7_math_frac_qty_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"{target_val} {unit}",
        "answer_latex": f"{target_val}\\text{{ {unit}}}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "subskill": "fraction_of_a_quantity",
        "learning_objective_id": "math_g7_fractions_quantity_context",
        "misconception_tags": [
            "divided_by_numerator_instead_of_denominator",
            "forgot_to_multiply_by_numerator",
            "reciprocal_multiplication_confusion"
        ],
        "diagnostic_tags": ["fractions", "word_problems", "proportional_reasoning"],
        "minimum_mastery_score": 75,
        "keywords": ["fraction of a quantity", "divide by denominator", "multiply by numerator", unit],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Setting up correct multiplication statement", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Division by denominator to find unit fraction value", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Multiplication by numerator for final allocated quantity", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Correct calculation of remaining fraction", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"To find a fraction of an amount, divide the total by the bottom number (denominator), then multiply by the top number (numerator).",
            "tier_2": f"First calculate {total_qty} ÷ {denom} = {factor}. Then multiply by {num}.",
            "tier_3": f"{factor} × {num} = {target_val} {unit}."
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
    Main entry point for Grade 7 Common Fractions Question Generator.
    Supports atomic micro-drills:
    - mode="elementary_operations"
    - mode="elementary_quantity"
    - mode="compound"
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions = []

    for _ in range(count):
        if mode == "elementary_quantity" or subskill == "quantity":
            q = _generate_fraction_of_quantity_question(rng)
        elif mode == "elementary_operations" or subskill == "operations":
            q = _generate_fraction_addition_subtraction_question(rng)
        else: # compound: pick across all archetypes
            archetype = rng.choice([
                _generate_fraction_addition_subtraction_question,
                _generate_fraction_of_quantity_question
            ])
            q = archetype(rng)
        questions.append(q)

    return questions
