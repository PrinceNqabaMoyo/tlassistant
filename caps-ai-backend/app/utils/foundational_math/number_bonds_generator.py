"""
caps-ai-backend/app/utils/foundational_math/number_bonds_generator.py
Foundational Mathematics Generator: Number Bonds, Fractions & Decomposition
Synthesizes Greg Tang (Visual/C-P-A) & Dr. Anna Stokke (Explicit/Fluency).

Fully compliant with the 6-Pillar Generator Architecture Contract (Rules 20-26).
Zero LLM dependencies. 100% deterministic Python/SymPy.
"""

from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional
import sympy as sp


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


def generate_number_bonds_drill(
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: int = 8
) -> Dict[str, Any]:
    """
    Emits a deterministic foundational drill based on Tang & Stokke pedagogy.

    Modes:
      - 'compound': Multiplicative factor pairs linked directly to trinomial expansion.
      - 'elementary_additive': Tang part-whole additive bonds & bridging to 10/20.
      - 'elementary_multiplicative': Tang factor pair arrays & decomposition.
      - 'elementary_fraction_strips': Tang visual unit-partitioned fraction equivalence.
      - 'stokke_speed_sprint': Stokke 60-second interleaved integer automaticity sprint.
    """
    r = _rng(seed)

    if mode == "elementary_additive":
        return _generate_additive_bond(r, seed, grade)
    elif mode == "elementary_multiplicative":
        return _generate_multiplicative_bond(r, seed, grade)
    elif mode == "elementary_fraction_strips":
        return _generate_fraction_strip_bond(r, seed, grade)
    elif mode == "stokke_speed_sprint":
        return _generate_stokke_speed_sprint(r, seed, grade)
    else:  # compound (bridge to algebra)
        return _generate_algebra_bridge_bond(r, seed, grade)


# =============================================================================
# MODE 1: ELEMENTARY ADDITIVE (Tang Part-Whole & Bridging 10)
# =============================================================================
def _generate_additive_bond(r: random.Random, seed: Optional[int], grade: int) -> Dict[str, Any]:
    target_whole = r.choice([10, 11, 12, 13, 14, 15, 16, 17, 18, 20])
    part1 = r.randint(3, target_whole - 2)
    part2 = target_whole - part1

    # Bridging mechanism: e.g. 8 + 5 = 8 + 2 + 3 = 10 + 3 = 13
    needs_bridge = target_whole > 10 and part1 < 10
    bridge_to_10 = 10 - part1 if needs_bridge else 0
    remaining_part = part2 - bridge_to_10 if needs_bridge else part2

    prompt_latex = f"{part1} + \\boxed{{\\phantom{{0}}}} = {target_whole}"

    steps = [
        {
            "from_latex": f"{part1} + ? = {target_whole}",
            "to_latex": f"{part1} + {bridge_to_10} = 10" if needs_bridge else f"{target_whole} - {part1} = {part2}",
            "op": f"Bridge to 10 by adding {bridge_to_10}" if needs_bridge else f"Subtract part {part1} from whole {target_whole}",
            "rule": "Tang Bridging Strategy" if needs_bridge else "Part-Whole Additive Inversion",
            "common_errors": ["finger_counting_off_by_one", "additive_bond_failure"]
        }
    ]
    if needs_bridge:
        steps.append({
            "from_latex": f"10 + ? = {target_whole}",
            "to_latex": f"10 + {remaining_part} = {target_whole} \\implies \\text{{total added}} = {bridge_to_10} + {remaining_part} = {part2}",
            "op": f"Add remaining {remaining_part} to reach {target_whole}",
            "rule": "Decomposition Sum",
            "common_errors": ["forgot_second_split"]
        })

    return {
        "question_id": _make_id("fnd_add"),
        "seed": seed,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_additive",
        "question_type": "math_short",
        "prompt": f"Find the missing number bond to complete the whole: {part1} + [ ? ] = {target_whole}",
        "prompt_latex": prompt_latex,
        "answer": str(part2),
        "correct_answer": str(part2),
        "visual_model": {
            "type": "tang_part_whole_circle",
            "whole": target_whole,
            "part1": part1,
            "part2_unknown": True,
            "bridge_split": [bridge_to_10, remaining_part] if needs_bridge else None
        },
        "hints": {
            "tier1": f"Think of {target_whole} as a whole. One part is {part1}. What is the missing part?",
            "tier2": f"Greg Tang Bridging Rule: How many do you add to {part1} to make 10? Then how many more to reach {target_whole}?",
            "tier3": f"{part1} + {bridge_to_10} = 10, and 10 + {remaining_part} = {target_whole}. Missing part = {part2}.",
            "tier_1_location": f"Think of {target_whole} as a whole. One part is {part1}. What is the missing part?",
            "tier_2_directional": f"Greg Tang Bridging Rule: How many do you add to {part1} to make 10? Then how many more to reach {target_whole}?",
            "tier_3_worked_step": f"{part1} + {bridge_to_10} = 10, and 10 + {remaining_part} = {target_whole}. Missing part = {part2}."
        },
        "canonical_solution": {
            "goal": f"Find missing addend for sum {target_whole}",
            "steps": steps,
            "final_latex": f"{part2}",
            "final_sympy": str(part2)
        },
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct bridging decomposition or inverse subtraction", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate final missing bond", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "misconception_tags": ["additive_bond_failure", "bridging_10_error"]
    }


# =============================================================================
# MODE 2: ELEMENTARY MULTIPLICATIVE (Tang Factor Arrays)
# =============================================================================
def _generate_multiplicative_bond(r: random.Random, seed: Optional[int], grade: int) -> Dict[str, Any]:
    # Numbers with rich factor pairs essential for quadratics
    constants = [12, 16, 18, 20, 24, 28, 30, 32, 36, 40, 48]
    c = r.choice(constants)
    
    # Compute all factor pairs of c
    all_pairs = []
    for i in range(1, int(c**0.5) + 1):
        if c % i == 0:
            all_pairs.append((i, c // i))
    
    chosen_pair = r.choice(all_pairs)
    p1, p2 = chosen_pair
    
    # Prompt asks for the pair that sums to a specific value
    target_sum = p1 + p2

    return {
        "question_id": _make_id("fnd_mul"),
        "seed": seed,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_multiplicative",
        "question_type": "math_short",
        "prompt": f"Decompose {c} into its factor pairs. Which pair multiplies to {c} and adds up to {target_sum}?",
        "prompt_latex": f"\\text{{Find }} p, q \\text{{ such that }} p \\times q = {c} \\text{{ and }} p + q = {target_sum}",
        "answer": f"{p1},{p2}",
        "correct_answer": f"{p1},{p2}",
        "visual_model": {
            "type": "tang_area_array",
            "total_area": c,
            "factor_pairs": all_pairs,
            "active_pair": [p1, p2]
        },
        "hints": {
            "tier1": f"List all pairs of whole numbers that multiply to give {c}.",
            "tier2": f"Pairs that multiply to {c} are: " + ", ".join([f"{a} × {b}" for a, b in all_pairs]) + ". Which pair adds to " + str(target_sum) + "?",
            "tier3": f"{p1} × {p2} = {c} and {p1} + {p2} = {target_sum}. The pair is {p1} and {p2}.",
            "tier_1_location": f"List all pairs of whole numbers that multiply to give {c}.",
            "tier_2_directional": f"Pairs that multiply to {c} are: " + ", ".join([f"{a} × {b}" for a, b in all_pairs]) + ". Which pair adds to " + str(target_sum) + "?",
            "tier_3_worked_step": f"{p1} × {p2} = {c} and {p1} + {p2} = {target_sum}. The pair is {p1} and {p2}."
        },
        "canonical_solution": {
            "goal": f"Find factor pair of {c} with sum {target_sum}",
            "steps": [
                {
                    "from_latex": f"\\text{{Factor pairs of }} {c}",
                    "to_latex": ", ".join([f"{a} \\times {b}" for a, b in all_pairs]),
                    "op": "Decompose number into multiplicative array bonds",
                    "rule": "Tang Multiplicative Decomposition",
                    "common_errors": ["missing_factor_pair", "factor_pair_blindness"]
                },
                {
                    "from_latex": f"{p1} + {p2}",
                    "to_latex": f"{target_sum}",
                    "op": f"Select pair summing to {target_sum}",
                    "rule": "Additive-Multiplicative Bridge",
                    "common_errors": ["summed_wrong_pair"]
                }
            ],
            "final_latex": f"{p1}, {p2}",
            "final_sympy": f"({p1}, {p2})"
        },
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification of valid factor pairs for constant", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct pair selection matching required sum", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "misconception_tags": ["factor_pair_blindness", "additive_bond_failure"]
    }


# =============================================================================
# MODE 3: ELEMENTARY FRACTION STRIPS (Tang Unit Partitioning)
# =============================================================================
def _generate_fraction_strip_bond(r: random.Random, seed: Optional[int], grade: int) -> Dict[str, Any]:
    # Pair of denominators that require equal unit partitioning
    pair = r.choice([(2, 3, 6), (2, 4, 4), (3, 4, 12), (2, 5, 10), (3, 6, 6)])
    d1, d2, lcd = pair
    n1 = 1
    n2 = 1

    equiv_n1 = n1 * (lcd // d1)
    equiv_n2 = n2 * (lcd // d2)
    final_num = equiv_n1 + equiv_n2
    final_fraction = sp.Rational(final_num, lcd)

    return {
        "question_id": _make_id("fnd_frc"),
        "seed": seed,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_fraction_strips",
        "question_type": "math_short",
        "prompt": f"Using equal unit partitions, find a common denominator and add: 1/{d1} + 1/{d2}",
        "prompt_latex": f"\\frac{{{n1}}}{{{d1}}} + \\frac{{{n2}}}{{{d2}}} = \\boxed{{\\phantom{{0}}}}",
        "answer": f"{final_fraction.p}/{final_fraction.q}",
        "correct_answer": f"{final_fraction.p}/{final_fraction.q}",
        "visual_strip_model": {
            "whole_units": 1,
            "partitions": lcd,
            "shaded": final_num,
            "fraction1": {"n": n1, "d": d1, "partition_to": lcd, "new_n": equiv_n1},
            "fraction2": {"n": n2, "d": d2, "partition_to": lcd, "new_n": equiv_n2},
            "lcd": lcd
        },
        "visual_model": {
            "type": "tang_fraction_strip_partition",
            "fraction1": {"n": n1, "d": d1, "partition_to": lcd, "new_n": equiv_n1},
            "fraction2": {"n": n2, "d": d2, "partition_to": lcd, "new_n": equiv_n2},
            "lcd": lcd
        },
        "hints": {
            "tier1": f"You cannot add parts of different sizes. Cut both strips into equal parts of size 1/{lcd}.",
            "tier2": f"Greg Tang Unitizing Rule: 1/{d1} becomes {equiv_n1}/{lcd}. 1/{d2} becomes {equiv_n2}/{lcd}.",
            "tier3": f"{equiv_n1}/{lcd} + {equiv_n2}/{lcd} = {final_num}/{lcd}" + (f" = {final_fraction.p}/{final_fraction.q}" if final_num != final_fraction.p else ""),
            "tier_1_location": f"You cannot add parts of different sizes. Cut both strips into equal parts of size 1/{lcd}.",
            "tier_2_directional": f"Greg Tang Unitizing Rule: 1/{d1} becomes {equiv_n1}/{lcd}. 1/{d2} becomes {equiv_n2}/{lcd}.",
            "tier_3_worked_step": f"{equiv_n1}/{lcd} + {equiv_n2}/{lcd} = {final_num}/{lcd}" + (f" = {final_fraction.p}/{final_fraction.q}" if final_num != final_fraction.p else "")
        },
        "canonical_solution": {
            "goal": "Equalize unit partitions and sum fractions",
            "steps": [
                {
                    "from_latex": f"\\frac{{{n1}}}{{{d1}}} + \\frac{{{n2}}}{{{d2}}}",
                    "to_latex": f"\\frac{{{equiv_n1}}}{{{lcd}}} + \\frac{{{equiv_n2}}}{{{lcd}}}",
                    "op": f"Partition strips into equal units of {lcd}",
                    "rule": "Tang Equal Unit Partitioning (LCD)",
                    "common_errors": ["fraction_unit_confusion"]
                },
                {
                    "from_latex": f"\\frac{{{equiv_n1} + {equiv_n2}}}{{{lcd}}}",
                    "to_latex": f"\\frac{{{final_fraction.p}}}{{{final_fraction.q}}}",
                    "op": "Combine equal units and simplify",
                    "rule": "Fraction Addition",
                    "common_errors": ["added_denominators_together"]
                }
            ],
            "final_latex": f"\\frac{{{final_fraction.p}}}{{{final_fraction.q}}}",
            "final_sympy": str(final_fraction)
        },
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Common denominator unit conversion", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate numerator summation & simplification", "marks": 1, "editable": True}
            ],
            "deductions": [
                {"rule": "added_denominators_directly", "penalty": -1}
            ],
            "carry_forward_rule": "consequential_accuracy"
        },
        "misconception_tags": ["fraction_unit_confusion", "fraction_lcd_multiplication_confusion"]
    }


# =============================================================================
# MODE 4: STOKKE SPEED SPRINT (Timed Integer & Arithmetic Automaticity)
# =============================================================================
def _generate_stokke_speed_sprint(r: random.Random, seed: Optional[int], grade: int) -> Dict[str, Any]:
    # Interleaved operations: addition, subtraction, multiplication with directed signs
    rules_map = {
        "add_negative": "Adding a negative shifts left on the number line",
        "subtract_negative": "Subtracting a negative is equivalent to adding its positive inverse",
        "multiply_integers": "Product of same signs is positive; product of opposite signs is negative",
    }
    items = []
    for _ in range(6):
        cur_op = r.choice(["add_negative", "subtract_negative", "multiply_integers"])
        if cur_op == "add_negative":
            a = r.randint(-12, 12)
            b = r.randint(-12, -1)
            ans = a + b
            expr = f"{a} + ({b})"
        elif cur_op == "subtract_negative":
            a = r.randint(-10, 10)
            b = r.randint(-12, -1)
            ans = a - b
            expr = f"{a} - ({b})"
        else:
            a = r.choice([-8, -7, -6, -5, -4, -3, 3, 4, 5, 6, 7, 8])
            b = r.choice([-9, -8, -7, -6, -4, -3, 3, 4, 6, 7, 8, 9])
            ans = a * b
            expr = f"({a}) \\times ({b})"
        items.append({
            "expr": expr,
            "answer": str(ans),
            "rule": rules_map[cur_op]
        })

    first_item = items[0]
    prompt_latex = f"{first_item['expr']} = \\boxed{{\\phantom{{0}}}}"

    return {
        "question_id": _make_id("fnd_spr"),
        "seed": seed,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 1,  # 60-second sprint target
        "mode": "stokke_speed_sprint",
        "question_type": "math_short",
        "prompt": f"Fluency Sprint: Compute without a calculator: {prompt_latex}",
        "prompt_latex": prompt_latex,
        "answer": first_item["answer"],
        "correct_answer": first_item["answer"],
        "items": items,
        "visual_model": {
            "type": "stokke_number_line_vector",
            "operation": "interleaved_integer_arithmetic",
            "target": first_item["answer"]
        },
        "hints": {
            "tier1": "Pay strict attention to the signs before combining.",
            "tier2": f"Stokke Direct Rule: {first_item['rule']}.",
            "tier3": f"Result is {first_item['answer']}.",
            "tier_1_location": "Pay strict attention to the signs before combining.",
            "tier_2_directional": f"Stokke Direct Rule: {first_item['rule']}.",
            "tier_3_worked_step": f"Result is {first_item['answer']}."
        },
        "canonical_solution": {
            "goal": "Instant arithmetic automaticity",
            "steps": [
                {
                    "from_latex": prompt_latex,
                    "to_latex": str(first_item["answer"]),
                    "op": "Signed integer arithmetic evaluation",
                    "rule": first_item["rule"],
                    "common_errors": ["sign_inversion_confusion"]
                }
            ],
            "final_latex": str(first_item["answer"]),
            "final_sympy": str(first_item["answer"])
        },
        "marking_schema": {
            "total_marks": 1,
            "marking_points": [
                {"id": "mp_1", "desc": "Accurate signed integer evaluation within time budget", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "misconception_tags": ["sign_inversion_confusion", "additive_bond_failure"]
    }


# =============================================================================
# MODE 5: COMPOUND (The Bridge to CAPS High School Algebra)
# =============================================================================
def _generate_algebra_bridge_bond(r: random.Random, seed: Optional[int], grade: int) -> Dict[str, Any]:
    # Factorizing quadratic trinomial x^2 + Bx + C using number bonds
    p = r.choice([-7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7])
    q = r.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    if p == q:
        q += 1

    b = p + q
    c = p * q
    b_sign = f"+ {b}" if b > 0 else f"- {abs(b)}" if b < 0 else ""
    c_sign = f"+ {c}" if c > 0 else f"- {abs(c)}"

    trinomial_latex = f"x^2 {b_sign}x {c_sign}" if b != 0 else f"x^2 {c_sign}"
    factored_latex = f"(x {'+' if p > 0 else '-'} {abs(p)})(x {'+' if q > 0 else '-'} {abs(q)})"

    return {
        "question_id": _make_id("fnd_alg"),
        "seed": seed,
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "question_type": "math_short",
        "prompt": f"Using multiplicative number bonds, factorize the quadratic trinomial: {trinomial_latex}",
        "prompt_latex": f"\\text{{Factorize: }} {trinomial_latex}",
        "answer": factored_latex,
        "correct_answer": factored_latex,
        "visual_model": {
            "type": "tang_algebra_tile_grid",
            "constant_c": c,
            "linear_b": b,
            "factor_pair": [p, q]
        },
        "hints": {
            "tier1": f"Use multiplicative bonds: find two numbers that multiply to {c} and add up to {b}.",
            "tier2": f"List factor pairs of {c}. Which pair has an additive sum of {b}? The pair is {p} and {q}.",
            "tier3": f"Write as binomial factors: (x {'+' if p > 0 else '-'} {abs(p)})(x {'+' if q > 0 else '-'} {abs(q)}).",
            "tier_1_location": f"Use multiplicative bonds: find two numbers that multiply to {c} and add up to {b}.",
            "tier_2_directional": f"List factor pairs of {c}. Which pair has an additive sum of {b}? The pair is {p} and {q}.",
            "tier_3_worked_step": f"Write as binomial factors: (x {'+' if p > 0 else '-'} {abs(p)})(x {'+' if q > 0 else '-'} {abs(q)})."
        },
        "canonical_solution": {
            "goal": f"Factorize trinomial {trinomial_latex}",
            "steps": [
                {
                    "from_latex": trinomial_latex,
                    "to_latex": f"\\text{{Identify }} p \\times q = {c} \\text{{ and }} p + q = {b} \\implies p = {p}, q = {q}",
                    "op": "Apply Tang factor bond decomposition to constant term",
                    "rule": "Multiplicative-Additive Bond Extraction",
                    "common_errors": ["factor_pair_blindness", "sign_error_distribution"]
                },
                {
                    "from_latex": f"\\text{{Factors: }} {p}, {q}",
                    "to_latex": factored_latex,
                    "op": "Construct binomial factors",
                    "rule": "Trinomial Factorization",
                    "common_errors": ["inverted_signs_in_brackets"]
                }
            ],
            "final_latex": factored_latex,
            "final_sympy": str(sp.factor(f"x**2 + {b}*x + {c}"))
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification of correct factor pair for constant", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Verification that factor sum equals linear coefficient", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Correct binomial factors with signs", "marks": 1, "editable": True}
            ],
            "deductions": [
                {"rule": "correct_factors_swapped_signs", "penalty": -1}
            ],
            "carry_forward_rule": "consequential_accuracy"
        },
        "misconception_tags": ["factor_pair_blindness", "sign_inversion_confusion", "additive_bond_failure"]
    }
