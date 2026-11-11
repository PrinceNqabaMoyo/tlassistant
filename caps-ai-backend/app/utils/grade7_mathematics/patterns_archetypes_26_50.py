"""
Grade 7 Mathematics - Numeric and Geometric Patterns Generator (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/03. Numeric and geometric patterns.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Tile, Dot and Grid Arrays (26 - 34)
# ==============================================================================

def arch_26_square_dot_arrays(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([6, 7, 8, 9, 10])
    total = n ** 2

    prompt = (
        f"Dots are arranged in growing solid square arrays:\n"
        f"- Pattern 1: $1 \\times 1 = 1$ dot\n"
        f"- Pattern 2: $2 \\times 2 = 4$ dots\n"
        f"- Pattern 3: $3 \\times 3 = 9$ dots\n\n"
        f"Calculate the total number of dots in **Pattern {n}**."
    )
    sol = (
        f"**Step 1:** The number of dots in Pattern $n$ is given by $D = n^2$ [1 Mark: Method].\n\n"
        f"**Step 2:** For Pattern {n}: $$D = {n}^2 = {n} \\times {n} = \\mathbf{{{total}}} \\text{{ dots [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "26_square_dot_arrays",
        "hints": {
            "tier_1": f"Multiply {n} by itself.",
            "tier_2": f"{n} * {n} = {total}.",
            "tier_3": f"{total} dots."
        }
    }


def arch_27_rectangular_dot_arrays(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 5, 6, 7])
    total = n * (n + 1)

    prompt = (
        f"Rectangular dot arrays grow such that Pattern $n$ has $n$ rows and $(n + 1)$ columns:\n"
        f"- Pattern 1: $1 \\times 2 = 2$ dots\n"
        f"- Pattern 2: $2 \\times 3 = 6$ dots\n"
        f"- Pattern 3: $3 \\times 4 = 12$ dots\n\n"
        f"Calculate the number of dots in **Pattern {n}**."
    )
    sol = (
        f"**Step 1:** Formula: $D = n(n + 1)$ [1 Mark: Method].\n\n"
        f"**Step 2:** For $n = {n}$: $$D = {n} \\times ({n} + 1) = {n} \\times {n+1} = \\mathbf{{{total}}} \\text{{ dots [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "27_rectangular_dot_arrays",
        "hints": {
            "tier_1": f"Multiply {n} by {n+1}.",
            "tier_2": f"{n} * {n+1} = {total}.",
            "tier_3": f"{total} dots."
        }
    }


def arch_28_l_shaped_dot_patterns(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 7, 9, 12])
    total = 2 * n - 1

    prompt = (
        f"L-shaped dot patterns are formed by adding a new outer layer of dots at each stage:\n"
        f"- Pattern 1: 1 dot\n"
        f"- Pattern 2: 3 dots\n"
        f"- Pattern 3: 5 dots\n"
        f"- Pattern 4: 7 dots\n\n"
        f"Calculate the number of dots in **Pattern {n}**."
    )
    sol = (
        f"**Step 1:** The sequence of odd numbers follows the rule $D = 2n - 1$ [1 Mark: Method].\n\n"
        f"**Step 2:** For $n = {n}$: $$D = 2({n}) - 1 = {2*n} - 1 = \\mathbf{{{total}}} \\text{{ dots [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "28_l_shaped_dot_patterns",
        "hints": {
            "tier_1": "These are the odd numbers: 2n - 1.",
            "tier_2": f"2 * {n} - 1 = {total}.",
            "tier_3": f"{total} dots."
        }
    }


def arch_29_border_tiles_around_square_pool(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 6, 8, 10])
    border_tiles = 4 * n + 4

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<rect x="30" y="30" width="140" height="140" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>'
            f'<rect x="55" y="55" width="90" height="90" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>'
            f'<text x="100" y="105" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">Pool ({n}x{n})</text>'
            f'<text x="100" y="47" font-size="11" fill="#475569" text-anchor="middle">Border Tiles</text>'
            f'</svg>'
        ),
        "caption": f"Square swimming pool of size {n}x{n} surrounded by 1-unit border tiles",
        "diagram_role": "context"
    }

    prompt = (
        f"A square swimming pool of side length $n$ meters is surrounded by a border of $1\\text{{ m}} \\times 1\\text{{ m}}$ paving tiles:\n"
        f"- Pool $1 \\times 1$: 8 border tiles\n"
        f"- Pool $2 \\times 2$: 12 border tiles\n"
        f"- Pool $3 \\times 3$: 16 border tiles\n\n"
        f"1. State the formula for the number of border tiles $B$ for a pool of size $n \\times n$.\n"
        f"2. How many border tiles are needed for an **{n} x {n} meter pool**?"
    )
    sol = (
        f"**Step 1:** The formula is $B = 4n + 4$ (4 sides of $n$ tiles plus 4 corner tiles) [1 Mark: Formula].\n\n"
        f"**Step 2:** For $n = {n}$: $$B = 4({n}) + 4 = {4*n} + 4 = \\mathbf{{{border_tiles}}} \\text{{ tiles [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. B = 4n + 4; 2. {border_tiles}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "29_border_tiles_around_square_pool",
        "hints": {
            "tier_1": "Formula is 4n + 4.",
            "tier_2": f"4 * {n} + 4 = {border_tiles}.",
            "tier_3": f"B = 4n + 4; {border_tiles} tiles."
        }
    }


def arch_30_t_shaped_tile_patterns(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 5, 6, 8])
    total = 3 * n + 1

    prompt = (
        f"T-shaped tile figures grow such that:\n"
        f"- Pattern 1: 4 tiles\n"
        f"- Pattern 2: 7 tiles\n"
        f"- Pattern 3: 10 tiles\n\n"
        f"Calculate the number of tiles in **Pattern {n}**."
    )
    sol = (
        f"**Step 1:** Constant difference is 3 tiles. Rule: $T_n = 3n + 1$ [1 Mark: Method].\n\n"
        f"**Step 2:** For Pattern {n}: $$T_{{{n}}} = 3({n}) + 1 = {3*n} + 1 = \\mathbf{{{total}}} \\text{{ tiles [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "30_t_shaped_tile_patterns",
        "hints": {
            "tier_1": "Multiply by 3 and add 1.",
            "tier_2": f"3 * {n} + 1 = {total}.",
            "tier_3": f"{total} tiles."
        }
    }


def arch_31_plus_shaped_tile_patterns(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 6, 8, 10])
    total = 4 * n + 1

    prompt = (
        f"A plus-shaped (+) pattern has 4 arms extending from a central tile:\n"
        f"- Pattern 1 (arm length 1): $4(1) + 1 = 5$ tiles\n"
        f"- Pattern 2 (arm length 2): $4(2) + 1 = 9$ tiles\n"
        f"- Pattern 3 (arm length 3): $4(3) + 1 = 13$ tiles\n\n"
        f"Calculate the number of tiles needed for **Pattern {n}**."
    )
    sol = (
        f"**Step 1:** Rule is $P = 4n + 1$ [1 Mark: Method].\n\n"
        f"**Step 2:** For $n = {n}$: $$P = 4({n}) + 1 = {4*n} + 1 = \\mathbf{{{total}}} \\text{{ tiles [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "31_plus_shaped_tile_patterns",
        "hints": {
            "tier_1": "Rule is 4n + 1.",
            "tier_2": f"4 * {n} + 1 = {total}.",
            "tier_3": f"{total} tiles."
        }
    }


def arch_32_triangular_dot_pattern_formation(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 5, 6, 7])
    total = (n * (n + 1)) // 2

    prompt = (
        f"Bowling pins or dots in a triangular arrangement follow the formula:\n\n"
        f"$$T_n = \\frac{{n(n + 1)}}{{2}}$$\n\n"
        f"Calculate the number of dots in a triangle with **{n} rows**."
    )
    sol = (
        f"**Step 1:** Substitute $n = {n}$: $T_{{{n}}} = \\frac{{{n}({n} + 1)}}{{2}} = \\frac{{{n} \\times {n+1}}}{{2}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$\\frac{{{n * (n+1)}}}{{2}} = \\mathbf{{{total}}} \\text{{ dots [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "32_triangular_dot_pattern_formation",
        "hints": {
            "tier_1": f"Multiply {n} by {n+1} and divide by 2.",
            "tier_2": f"({n} * {n+1}) / 2 = {total}.",
            "tier_3": f"{total} dots."
        }
    }


def arch_33_hexagonal_honeycomb_pattern(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a honeycomb pattern, 1 central hex tile is surrounded by 6 tiles in Ring 1, 12 tiles in Ring 2, and 18 tiles in Ring 3.\n\n"
        f"How many tiles will be in **Ring 4**?"
    )
    sol = (
        f"**Step 1:** The number of tiles per ring follows multiples of 6: $6, 12, 18, \\dots$ ($6r$) [1 Mark: Method].\n\n"
        f"**Step 2:** For Ring 4: $$6 \\times 4 = \\mathbf{{24}} \\text{{ tiles [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "24",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "33_hexagonal_honeycomb_pattern",
        "hints": {
            "tier_1": "The sequence of ring counts is 6, 12, 18... Next multiple of 6.",
            "tier_2": "6 * 4 = 24.",
            "tier_3": "24 tiles."
        }
    }


def arch_34_inverse_tile_problem(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([7, 9, 11, 13])
    tiles = 4 * n + 4  # border pool rule

    prompt = (
        f"A border tile pattern uses the rule $B = 4n + 4$.\n\n"
        f"If a builder used exactly **{tiles} border tiles**, what was the size $n$ of the pool?"
    )
    sol = (
        f"**Step 1:** Set up equation: $4n + 4 = {tiles}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Solve for $n$:\n"
        f"$$4n = {tiles} - 4 = {tiles - 4}$$\n"
        f"$$n = \\frac{{{tiles - 4}}}{{4}} = \\mathbf{{{n}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{n}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "34_inverse_tile_problem",
        "hints": {
            "tier_1": f"Subtract 4 from {tiles}, then divide by 4.",
            "tier_2": f"({tiles} - 4) / 4 = {n}.",
            "tier_3": f"{n}."
        }
    }


# ==============================================================================
# CLUSTER 5: General Formula & Large Term Calculation (35 - 42)
# ==============================================================================

def arch_35_deriving_linear_formula_tn(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 6])
    c = rng.choice([1, 2, 3, 4])
    # Tn = d*n + c
    t1 = d * 1 + c
    t2 = d * 2 + c
    t3 = d * 3 + c
    t4 = d * 4 + c

    prompt = (
        f"Given the arithmetic progression: $${t1}; {t2}; {t3}; {t4}; ...$$\n\n"
        f"Derive the algebraic formula ($T_n$) in terms of index $n$."
    )
    sol = (
        f"**Step 1:** The constant difference is $d = {t2} - {t1} = {d}$ [1 Mark].\n\n"
        f"**Step 2:** Zero term / constant: $c = T_1 - d = {t1} - {d} = {c}$ [1 Mark: Method].\n\n"
        f"$$\\mathbf{{T_n = {d}n + {c}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Tn = {d}n + {c}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "35_deriving_linear_formula_tn",
        "hints": {
            "tier_1": f"Find common difference d = {d}. Formula is Tn = {d}n + c.",
            "tier_2": f"For n=1: {d}(1) + c = {t1} => c = {c}.",
            "tier_3": f"Tn = {d}n + {c}."
        }
    }


def arch_36_calculate_twentieth_term(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 7])
    c = rng.choice([1, 2, 5])
    t20 = d * 20 + c
    t1, t2, t3 = d + c, 2 * d + c, 3 * d + c

    prompt = (
        f"An arithmetic progression begins: $${t1}; {t2}; {t3}; ...$$\n\n"
        f"1. State the algebraic formula for $T_n$.\n"
        f"2. Evaluate the **20th entry ($T_{{20}}$)**."
    )
    sol = (
        f"**Step 1:** Rule: $T_n = {d}n + {c}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Substitute $n = 20$: "
        f"$$T_{{20}} = {d}(20) + {c} = {d * 20} + {c} = \\mathbf{{{t20}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. Tn = {d}n + {c}; 2. {t20}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "36_calculate_twentieth_term",
        "hints": {
            "tier_1": f"Find Tn = {d}n + {c}, then plug in n = 20.",
            "tier_2": f"{d} * 20 + {c} = {t20}.",
            "tier_3": f"Tn = {d}n + {c}; {t20}."
        }
    }


def arch_37_calculate_fiftieth_term(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([2, 4, 6])
    c = rng.choice([3, 5, 7])
    t50 = d * 50 + c

    prompt = (
        f"The general term of a sequence is given by: $$T_n = {d}n + {c}$$\n\n"
        f"Calculate the value of the **50th term ($T_{{50}}$)**."
    )
    sol = (
        f"**Step 1:** Substitute $n = 50$: $T_{{50}} = {d}(50) + {c}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$T_{{50}} = {d * 50} + {c} = \\mathbf{{{t50}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{t50}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "37_calculate_fiftieth_term",
        "hints": {
            "tier_1": f"Multiply 50 by {d} and add {c}.",
            "tier_2": f"{d * 50} + {c} = {t50}.",
            "tier_3": f"{t50}."
        }
    }


def arch_38_calculate_hundredth_term(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 5, 8])
    c = rng.choice([2, 4])
    t100 = d * 100 + c

    prompt = (
        f"For the sequence $T_n = {d}n + {c}$, calculate the value of the **100th term**."
    )
    sol = (
        f"**Step 1:** Substitute $n = 100$: $T_{{100}} = {d}(100) + {c}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$T_{{100}} = {d * 100} + {c} = \\mathbf{{{t100}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{t100}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "38_calculate_hundredth_term",
        "hints": {
            "tier_1": f"Multiply 100 by {d} and add {c}.",
            "tier_2": f"{d * 100} + {c} = {t100}.",
            "tier_3": f"{t100}."
        }
    }


def arch_39_solve_for_position_n(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 6])
    c = rng.choice([1, 2, 3])
    n = rng.choice([15, 18, 22, 25])
    target_val = d * n + c

    prompt = (
        f"A sequence has the rule: $$T_n = {d}n + {c}$$\n\n"
        f"Which term in the sequence has a value of **{target_val}**? (Find position $n$)."
    )
    sol = (
        f"**Step 1:** Set up equation: ${d}n + {c} = {target_val}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Solve for $n$:\n"
        f"$${d}n = {target_val} - {c} = {target_val - c}$$\n"
        f"$$n = \\frac{{{target_val - c}}}{{{d}}} = \\mathbf{{{n}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"n = {n}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "39_solve_for_position_n",
        "hints": {
            "tier_1": f"Subtract {c} from {target_val}, then divide by {d}.",
            "tier_2": f"({target_val} - {c}) / {d} = {n}.",
            "tier_3": f"n = {n}."
        }
    }


def arch_40_is_number_a_term_in_sequence(rng: random.Random) -> Dict[str, Any]:
    d = 4
    c = 1  # Tn = 4n + 1 (terms: 5, 9, 13, 17, 21...)
    is_term = rng.choice([True, False])
    if is_term:
        n = 12
        val = 4 * n + 1  # 49
        ans = "Yes; it is the 12th term (n = 12)"
        reason = f"(49 - 1) / 4 = 48 / 4 = 12 (whole number)"
    else:
        val = 50  # 50 - 1 = 49, not divisible by 4
        ans = "No; not a term in the sequence"
        reason = f"(50 - 1) / 4 = 49 / 4 = 12,25 (not a whole number)"

    prompt = (
        f"A sequence is given by $T_n = 4n + 1$.\n\n"
        f"Is the number **{val}** a term in this sequence? Justify your answer."
    )
    sol = (
        f"**Step 1:** Set $4n + 1 = {val} \\implies 4n = {val - 1} \\implies n = \\frac{{{val - 1}}}{{4}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** {reason}. Therefore: **{ans}** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_pat_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "40_is_number_a_term_in_sequence",
        "hints": {
            "tier_1": f"Subtract 1 from {val} and see if it divides evenly by 4.",
            "tier_2": reason,
            "tier_3": ans
        }
    }


def arch_41_compare_two_growing_patterns(rng: random.Random) -> Dict[str, Any]:
    # Pattern A: Tn = 2n + 10 (starts higher, grows slower)
    # Pattern B: Tn = 4n + 2 (starts lower, grows faster)
    # Equal when 2n + 10 = 4n + 2 => 2n = 8 => n = 4. Overtakes at n = 5
    prompt = (
        f"Pattern A grows by rule $A_n = 2n + 10$.\n"
        f"Pattern B grows by rule $B_n = 4n + 2$.\n\n"
        f"1. Calculate the value of both patterns at $n = 3$.\n"
        f"2. At which term $n$ does Pattern B first become **strictly greater** than Pattern A?"
    )
    a3 = 2 * 3 + 10  # 16
    b3 = 4 * 3 + 2   # 14
    sol = (
        f"**Step 1:** At $n = 3$:\n"
        f"- $A_3 = 2(3) + 10 = 16$\n"
        f"- $B_3 = 4(3) + 2 = 14$ [1 Mark].\n\n"
        f"**Step 2:** Equating $4n + 2 = 2n + 10 \\implies 2n = 8 \\implies n = 4$ (both equal 18).\n"
        f"At **$n = 5$**, $B_5 = 22 > A_5 = 20$. Pattern B overtakes at **$n = 5$** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_pat_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. A3 = 16, B3 = 14; 2. n = 5",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "41_compare_two_growing_patterns",
        "hints": {
            "tier_1": "Calculate for n = 3, 4, 5.",
            "tier_2": "At n = 4, both equal 18. At n = 5, B=22 and A=20.",
            "tier_3": "1. A3 = 16, B3 = 14; 2. n = 5."
        }
    }


def arch_42_differences_of_square_numbers(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Consider the first five square numbers: $1; 4; 9; 16; 25$.\n\n"
        f"1. Calculate the consecutive differences ($4 - 1$, $9 - 4$, $16 - 9$, $25 - 16$).\n"
        f"2. What special sequence of numbers do these differences form?"
    )
    sol = (
        f"**Step 1:** Differences: $3; 5; 7; 9$ [1 Mark: Method].\n\n"
        f"**Step 2:** The consecutive differences of square numbers form the sequence of **odd numbers** (starting from 3) [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_pat_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. 3; 5; 7; 9; 2. Consecutive odd numbers",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "42_differences_of_square_numbers",
        "hints": {
            "tier_1": "Subtract each square from the next: 4-1, 9-4, 16-9, 25-16.",
            "tier_2": "3, 5, 7, 9 are odd numbers.",
            "tier_3": "1. 3, 5, 7, 9; 2. Odd numbers."
        }
    }


# ==============================================================================
# CLUSTER 6: Tables, Seating and Practical Contexts (43 - 50)
# ==============================================================================

def arch_43_restaurant_tables_in_a_row(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([6, 8, 10, 12, 14])
    people = 2 * n + 2

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 240 120" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<rect x="40" y="40" width="160" height="40" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
            f'<line x1="80" y1="40" x2="80" y2="80" stroke="#94a3b8" stroke-width="1.5"/>'
            f'<line x1="120" y1="40" x2="120" y2="80" stroke="#94a3b8" stroke-width="1.5"/>'
            f'<line x1="160" y1="40" x2="160" y2="80" stroke="#94a3b8" stroke-width="1.5"/>'
            f'<circle cx="25" cy="60" r="6" fill="#2563eb"/>'
            f'<circle cx="215" cy="60" r="6" fill="#2563eb"/>'
            f'<circle cx="60" cy="25" r="6" fill="#2563eb"/><circle cx="100" cy="25" r="6" fill="#2563eb"/>'
            f'<circle cx="140" cy="25" r="6" fill="#2563eb"/><circle cx="180" cy="25" r="6" fill="#2563eb"/>'
            f'<circle cx="60" cy="95" r="6" fill="#2563eb"/><circle cx="100" cy="95" r="6" fill="#2563eb"/>'
            f'<circle cx="140" cy="95" r="6" fill="#2563eb"/><circle cx="180" cy="95" r="6" fill="#2563eb"/>'
            f'<text x="120" y="65" font-size="11" fill="#64748b" text-anchor="middle">Row of {n} Tables</text>'
            f'</svg>'
        ),
        "caption": f"Square tables pushed together in a single row (n = {n})",
        "diagram_role": "context"
    }

    prompt = (
        f"Square tables seating 1 person per side are pushed together in a long single row:\n"
        f"- 1 table seats 4 people\n"
        f"- 2 tables pushed together seat 6 people\n"
        f"- 3 tables pushed together seat 8 people\n\n"
        f"1. Write down the general formula $P$ for the number of people seated around $n$ tables.\n"
        f"2. How many people can be seated if **{n} tables** are pushed together?"
    )
    sol = (
        f"**Step 1:** Each table provides 2 seats (top and bottom), plus 2 seats at the two ends: "
        f"$$\\mathbf{{P = 2n + 2}} \\text{{ [1 Mark: Formula]}}$$\n\n"
        f"**Step 2:** For $n = {n}$: $$P = 2({n}) + 2 = {2*n} + 2 = \\mathbf{{{people}}} \\text{{ people [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. P = 2n + 2; 2. {people}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "43_restaurant_tables_in_a_row",
        "hints": {
            "tier_1": "Formula is 2n + 2.",
            "tier_2": f"2 * {n} + 2 = {people}.",
            "tier_3": f"P = 2n + 2; {people} people."
        }
    }


def arch_44_separate_tables_seating(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([8, 12, 15, 20])
    total = 4 * n

    prompt = (
        f"If {n} tables in a restaurant are left **completely separate** (not pushed together), and each separate square table seats 4 people:\n\n"
        f"Calculate the total number of people that can be seated."
    )
    sol = (
        f"**Step 1:** Each table seats 4 people independently: $P = 4n$ [1 Mark: Method].\n\n"
        f"**Step 2:** $${n} \\times 4 = \\mathbf{{{total}}} \\text{{ people [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "44_separate_tables_seating",
        "hints": {
            "tier_1": f"Multiply {n} by 4.",
            "tier_2": f"{n} * 4 = {total}.",
            "tier_3": f"{total} people."
        }
    }


def arch_45_hexagonal_tables_in_a_line(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 5, 6, 8])
    people = 4 * n + 2

    prompt = (
        f"Regular hexagonal tables seating 1 person per side are pushed together end-to-end in a line:\n"
        f"- 1 table seats 6 people\n"
        f"- 2 tables pushed together seat 10 people\n"
        f"- 3 tables pushed together seat 14 people\n\n"
        f"Calculate the number of people seated around a line of **{n} hexagonal tables**."
    )
    sol = (
        f"**Step 1:** Each additional table adds 4 seats, plus 2 end seats: $P = 4n + 2$ [1 Mark: Method].\n\n"
        f"**Step 2:** For $n = {n}$: $$P = 4({n}) + 2 = {4*n} + 2 = \\mathbf{{{people}}} \\text{{ people [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{people}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "45_hexagonal_tables_in_a_line",
        "hints": {
            "tier_1": "Rule is 4n + 2.",
            "tier_2": f"4 * {n} + 2 = {people}.",
            "tier_3": f"{people} people."
        }
    }


def arch_46_fence_posts_and_rails(rng: random.Random) -> Dict[str, Any]:
    sections = rng.choice([5, 8, 12, 15])
    posts = sections + 1
    rails = 2 * sections  # 2 rails per section

    prompt = (
        f"A straight garden fence has sections:\n"
        f"- 1 section needs 2 posts and 2 rails\n"
        f"- 2 sections need 3 posts and 4 rails\n"
        f"- 3 sections need 4 posts and 6 rails\n\n"
        f"How many posts and how many rails are needed for a fence with **{sections} sections**?"
    )
    sol = (
        f"**Step 1:** Number of posts: $P = n + 1 = {sections} + 1 = \\mathbf{{{posts}}} \\text{{ posts}}$ [1 Mark].\n\n"
        f"**Step 2:** Number of rails: $R = 2n = 2 \\times {sections} = \\mathbf{{{rails}}} \\text{{ rails}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_pat_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{posts} posts; {rails} rails",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "46_fence_posts_and_rails",
        "hints": {
            "tier_1": f"Posts = sections + 1; Rails = 2 * sections.",
            "tier_2": f"Posts: {sections}+1={posts}; Rails: 2*{sections}={rails}.",
            "tier_3": f"{posts} posts; {rails} rails."
        }
    }


def arch_47_savings_linear_pattern(rng: random.Random) -> Dict[str, Any]:
    init = rng.choice([50, 100, 150])
    weekly = rng.choice([20, 25, 30])
    w = rng.choice([6, 8, 10, 12])
    total = init + weekly * w

    prompt = (
        f"A learner opens a savings account with an initial deposit of R{init}.\n"
        f"Every week, they add R{weekly} to the account.\n\n"
        f"1. Write down a formula for the savings $S$ after $w$ weeks.\n"
        f"2. Calculate the total savings after **{w} weeks**."
    )
    sol = (
        f"**Step 1:** Formula: $$\\mathbf{{S = {weekly}w + {init}}} \\text{{ [1 Mark: Formula]}}$$\n\n"
        f"**Step 2:** For $w = {w}$: $$S = {weekly}({w}) + {init} = {weekly * w} + {init} = \\mathbf{{\\text{{R}}{total}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. S = {weekly}w + {init}; 2. R{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "47_savings_linear_pattern",
        "hints": {
            "tier_1": f"Multiply weekly amount by {w} and add initial deposit.",
            "tier_2": f"{weekly} * {w} + {init} = {total}.",
            "tier_3": f"S = {weekly}w + {init}; R{total}."
        }
    }


def arch_48_stacking_cans_triangular_display(rng: random.Random) -> Dict[str, Any]:
    rows = rng.choice([4, 5, 6])
    total = sum(range(1, rows + 1))

    prompt = (
        f"A grocery store stacks cans in a triangular pyramid display:\n"
        f"- Top row 1: 1 can\n"
        f"- Row 2: 2 cans\n"
        f"- Row 3: 3 cans\n\n"
        f"If the display has **{rows} rows** in total, calculate the total number of cans in the display."
    )
    sol = (
        f"**Step 1:** Sum the cans in all {rows} rows: $1 + 2 + \\dots + {rows}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Total = $$\\frac{{{rows}({rows} + 1)}}{{2}} = \\frac{{{rows * (rows + 1)}}}{{2}} = \\mathbf{{{total}}} \\text{{ cans [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "48_stacking_cans_triangular_display",
        "hints": {
            "tier_1": f"Sum numbers from 1 to {rows}.",
            "tier_2": f"Total is {total}.",
            "tier_3": f"{total} cans."
        }
    }


def arch_49_cellular_division_powers_of_two(rng: random.Random) -> Dict[str, Any]:
    gen = rng.choice([4, 5, 6, 7])
    bacteria = 2 ** gen

    prompt = (
        f"A bacterium divides into two bacteria every 30 minutes (exponential doubling):\n"
        f"- Start (0 min): 1 bacterium\n"
        f"- Generation 1 (30 min): 2 bacteria\n"
        f"- Generation 2 (60 min): 4 bacteria\n"
        f"- Generation 3 (90 min): 8 bacteria\n\n"
        f"How many bacteria will there be after **{gen} generations**?"
    )
    sol = (
        f"**Step 1:** The number of bacteria follows the rule $B = 2^g$ [1 Mark: Method].\n\n"
        f"**Step 2:** For generation {gen}: $$B = 2^{{{gen}}} = \\mathbf{{{bacteria}}} \\text{{ bacteria [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{bacteria}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "49_cellular_division_powers_of_two",
        "hints": {
            "tier_1": f"Calculate 2^{gen}.",
            "tier_2": f"2^{gen} = {bacteria}.",
            "tier_3": f"{bacteria} bacteria."
        }
    }


def arch_50_flawed_rule_diagnosis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"For the sequence $4; 7; 10; 13; \\dots$, a learner notices the constant difference is 3 and claims the general rule is simply $T_n = 3n$.\n\n"
        f"1. Test the learner's rule for $n = 1$. What value does it produce?\n"
        f"2. What is the correct general rule for this sequence?"
    )
    sol = (
        f"**Step 1:** For $n = 1$, the learner's rule gives $T_1 = 3(1) = 3$, but the actual first term is 4 (error of 1) [1 Mark].\n\n"
        f"**Step 2:** The correct rule requires adding 1 to match the sequence: $$\\mathbf{{T_n = 3n + 1}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Gives 3 instead of 4; 2. Tn = 3n + 1",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "50_flawed_rule_diagnosis",
        "hints": {
            "tier_1": "Plug n = 1 into 3n: 3 * 1 = 3.",
            "tier_2": "Actual first term is 4, so add 1.",
            "tier_3": "1. Gives 3 (should be 4); 2. Tn = 3n + 1."
        }
    }
