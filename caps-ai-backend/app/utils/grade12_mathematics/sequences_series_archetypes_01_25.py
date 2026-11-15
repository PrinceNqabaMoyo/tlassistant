"""Grade 12 Mathematics - Sequences and Series Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/Mathematics_Gr12/Term 1/01. Sequences and series.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional
import sympy as sp


def _svg_spec(svg_body: str, width: int = 580, height: int = 240) -> Dict[str, Any]:
    return {
        "kind": "inline_svg",
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="100%" height="{height}" style="background:#ffffff;border-radius:8px;border:1px solid #cbd5e1;">'
            f'{svg_body}</svg>'
        ),
        "diagram_role": "context",
    }


def _mcq_q(
    rng: random.Random,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 3,
    curriculum_ref: str = "Term 1 > Sequences and Series",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    opts = [correct] + distractors[:3]
    rng.shuffle(opts)
    q: Dict[str, Any] = {
        "id": qid,
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "multiple_choice",
        "prompt": prompt,
        "options": opts,
        "expected_answer": correct,
        "sample_answer": correct,
        "worked_solution": worked_solution,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct selection: {correct}", "marks": marks, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "misconception_tags": misconception_tags,
        "curriculum_reference": curriculum_ref,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
        q["modality"] = "diagram"
    return q


def _calc_q(
    rng: random.Random,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    expected_value: str,
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 4,
    curriculum_ref: str = "Term 1 > Sequences and Series",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": qid,
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": expected_value,
        "sample_answer": expected_value,
        "worked_solution": worked_solution,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{i+1}", "desc": pt, "marks": 1, "editable": True}
                for i, pt in enumerate(worked_solution.strip().split("\n")[:marks])
            ] or [{"id": "mp_1", "desc": f"Accurate calculation: {expected_value}", "marks": marks, "editable": True}],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "misconception_tags": misconception_tags,
        "curriculum_reference": curriculum_ref,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
        q["modality"] = "diagram"
    return q


# =========================================================================== #
# Archetypes 01 - 25
# =========================================================================== #

def arch_01_arithmetic_common_diff_and_next_terms(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-15, -9, -5, 3, 7, 12])
    d = rng.choice([-7, -4, -3, 3, 5, 8])
    t1, t2, t3 = a, a + d, a + 2 * d
    t4, t5, t6 = a + 3 * d, a + 4 * d, a + 5 * d
    prompt = (
        f"Consider the sequence: ${t1};\\ {t2};\\ {t3};\\ \\dots$\n\n"
        f"1. Verify that this is an arithmetic sequence by finding the constant difference $d$.\n"
        f"2. Write down the next three terms of the sequence ($T_4, T_5, T_6$)."
    )
    correct = f"d = {d}; T4 = {t4}, T5 = {t5}, T6 = {t6}"
    distractors = [
        f"d = {d + 1}; T4 = {t4 + 1}, T5 = {t5 + 2}, T6 = {t6 + 3}",
        f"d = {-d}; T4 = {a - 3*d}, T5 = {a - 4*d}, T6 = {a - 5*d}",
        f"d = {d}; T4 = {t4}, T5 = {t4 + d + 2}, T6 = {t4 + 2*d + 4}",
    ]
    sol = (
        f"Step 1: Check difference: $d = T_2 - T_1 = {t2} - ({t1}) = {d}$. Also $T_3 - T_2 = {t3} - ({t2}) = {d}$.\n"
        f"Step 2: Next terms:\n"
        f"$T_4 = T_3 + d = {t3} + ({d}) = {t4}$\n"
        f"$T_5 = T_4 + d = {t4} + ({d}) = {t5}$\n"
        f"$T_6 = T_5 + d = {t5} + ({d}) = {t6}$."
    )
    return _mcq_q(
        rng, f"g12_seq_01_{rng.randint(100000, 999999)}", "01_arithmetic_common_diff_and_next_terms",
        "Arithmetic Common Difference and Successive Terms", prompt, correct, distractors, sol,
        {"tier_1": "Subtract the first term from the second term to obtain d.",
         "tier_2": f"d = {t2} - ({t1}). Add this value consecutively to find T4, T5, and T6.",
         "tier_3": correct},
        ["arithmetic_difference_sign_error"]
    )


def arch_02_arithmetic_general_term_formula(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-11, -4, 2, 5, 8, 14])
    d = rng.choice([-6, -5, 3, 4, 7])
    t1, t2, t3 = a, a + d, a + 2 * d
    c = a - d
    sign = "+" if c >= 0 else "-"
    abs_c = abs(c)
    formula_str = f"T_n = {d}n {sign} {abs_c}" if abs_c != 0 else f"T_n = {d}n"

    prompt = (
        f"Given the linear arithmetic sequence: ${t1};\\ {t2};\\ {t3};\\ \\dots$\n\n"
        f"Determine the general term formula $T_n$ in terms of $n$, simplified into the form $T_n = dn + c$."
    )
    correct = formula_str
    distractors = [
        f"T_n = {d}n {'+' if a >= 0 else '-'} {abs(a)}",
        f"T_n = {a}n {'+' if d >= 0 else '-'} {abs(d)}",
        f"T_n = {d}n {'-' if c >= 0 else '+'} {abs_c}",
    ]
    sol = (
        f"Step 1: Identify parameters: $a = T_1 = {t1}$, and $d = T_2 - T_1 = {t2} - ({t1}) = {d}$.\n"
        f"Step 2: Apply the general term formula:\n"
        f"$T_n = a + (n - 1)d$\n"
        f"$T_n = {a} + (n - 1)({d}) = {a} + {d}n - {d} = {formula_str}$."
    )
    return _mcq_q(
        rng, f"g12_seq_02_{rng.randint(100000, 999999)}", "02_arithmetic_general_term_formula",
        "General Term of an Arithmetic Sequence", prompt, correct, distractors, sol,
        {"tier_1": "Use the formula Tn = a + (n - 1)d and expand the brackets.",
         "tier_2": f"Here a = {a} and d = {d}. Simplify {a} + {d}(n - 1).",
         "tier_3": correct},
        ["failure_to_distribute_d_in_general_term"]
    )


def arch_03_arithmetic_find_specific_term(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-8, -3, 4, 7, 15])
    d = rng.choice([-5, -3, 3, 6, 8])
    n = rng.choice([24, 35, 42, 50, 75])
    val = a + (n - 1) * d
    t1, t2, t3 = a, a + d, a + 2 * d
    prompt = (
        f"Consider the arithmetic sequence: ${t1};\\ {t2};\\ {t3};\\ \\dots$\n\n"
        f"Calculate the value of the {n}-th term ($T_{{{n}}}$)."
    )
    ans = str(val)
    sol = (
        f"Step 1: First term $a = {a}$, common difference $d = {t2} - ({t1}) = {d}$.\n"
        f"Step 2: Apply $T_n = a + (n - 1)d$ with $n = {n}$:\n"
        f"$T_{{{n}}} = {a} + ({n} - 1)({d}) = {a} + ({n - 1})({d}) = {a} + {(n - 1)*d} = {val}$."
    )
    return _calc_q(
        rng, f"g12_seq_03_{rng.randint(100000, 999999)}", "03_arithmetic_find_specific_term",
        "Finding a Specific Term in an Arithmetic Sequence", prompt, ans, sol,
        {"tier_1": f"Identify a = {a}, d = {d}, and substitute n = {n} into Tn = a + (n-1)d.",
         "tier_2": f"Compute ({n} - 1)*({d}) then add {a}.",
         "tier_3": f"T_{{{n}}} = {val}."},
        ["off_by_one_term_index"]
    )


def arch_04_arithmetic_find_term_position(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-14, -7, 5, 8, 12])
    d = rng.choice([3, 4, 6, 7])
    n = rng.choice([25, 32, 45, 60, 81])
    target = a + (n - 1) * d
    t1, t2, t3 = a, a + d, a + 2 * d
    prompt = (
        f"Given the arithmetic sequence: ${t1};\\ {t2};\\ {t3};\\ \\dots$\n\n"
        f"Which term in the sequence is equal to ${target}$? (Solve for the position $n$)."
    )
    ans = f"n = {n}"
    sol = (
        f"Step 1: Identify $a = {a}$ and $d = {d}$. Set $T_n = {target}$.\n"
        f"Step 2: Substitute into $T_n = a + (n - 1)d$:\n"
        f"${target} = {a} + (n - 1)({d})$\n"
        f"${target - a} = (n - 1)({d})$\n"
        f"${(target - a) // d} = n - 1$\n"
        f"$n = {n}$."
    )
    return _calc_q(
        rng, f"g12_seq_04_{rng.randint(100000, 999999)}", "04_arithmetic_find_term_position",
        "Determining Position n of a Given Term", prompt, ans, sol,
        {"tier_1": f"Set Tn = {target} in Tn = a + (n - 1)d and isolate n.",
         "tier_2": f"Subtract {a} from {target} and divide the result by {d}.",
         "tier_3": f"n = {n}."},
        ["incorrect_algebra_isolating_n"]
    )


def arch_05_arithmetic_solve_unknown_terms_linear(rng: random.Random) -> Dict[str, Any]:
    # Consecutive terms in terms of x: T1 = c1*x + k1, T2 = c2*x + k2, T3 = c3*x + k3
    # T2 - T1 = T3 - T2  =>  2*T2 = T1 + T3
    x_val = rng.choice([2, 3, 4, 5, 6])
    c1, c2, c3 = 2, 5, 7
    # 2*(5x + k2) = (2x + k1) + (7x + k3) => 10x + 2*k2 = 9x + k1 + k3 => x = k1 + k3 - 2*k2
    k2 = rng.choice([1, 2, 3])
    k1 = rng.choice([1, 3, 5])
    k3 = x_val + 2 * k2 - k1
    t1_str = f"2x + {k1}"
    t2_str = f"5x + {k2}"
    t3_str = f"7x + {k3}"
    val_t1 = 2 * x_val + k1
    val_t2 = 5 * x_val + k2
    val_t3 = 7 * x_val + k3
    prompt = (
        f"The first three terms of an arithmetic sequence are:\n"
        f"$${t1_str};\\ {t2_str};\\ {t3_str}$$\n\n"
        f"1. Solve for the value of $x$.\n"
        f"2. Hence, determine the numerical values of the three terms."
    )
    correct = f"x = {x_val}; terms are {val_t1}, {val_t2}, {val_t3}"
    distractors = [
        f"x = {x_val + 1}; terms are {val_t1 + 2}, {val_t2 + 5}, {val_t3 + 7}",
        f"x = {x_val - 1}; terms are {val_t1 - 2}, {val_t2 - 5}, {val_t3 - 7}",
        f"x = {x_val}; terms are {val_t1}, {val_t1 + 4}, {val_t1 + 8}",
    ]
    sol = (
        f"Step 1: Set constant difference condition: $T_2 - T_1 = T_3 - T_2$.\n"
        f"$$({t2_str}) - ({t1_str}) = ({t3_str}) - ({t2_str})$$\n"
        f"$$3x + ({k2 - k1}) = 2x + ({k3 - k2})$$\n"
        f"$$3x - 2x = ({k3 - k2}) - ({k2 - k1}) \\implies x = {x_val}$$.\n"
        f"Step 2: Substitute $x = {x_val}$:\n"
        f"$T_1 = 2({x_val}) + {k1} = {val_t1}$\n"
        f"$T_2 = 5({x_val}) + {k2} = {val_t2}$\n"
        f"$T_3 = 7({x_val}) + {k3} = {val_t3}$\n"
        f"Common difference $d = {val_t2} - {val_t1} = {val_t2 - val_t1}$."
    )
    return _mcq_q(
        rng, f"g12_seq_05_{rng.randint(100000, 999999)}", "05_arithmetic_solve_unknown_terms_linear",
        "Solving for Unknown Variable in Arithmetic Sequence", prompt, correct, distractors, sol,
        {"tier_1": "Use the property that consecutive differences are equal: T2 - T1 = T3 - T2.",
         "tier_2": "Equate (T2 - T1) to (T3 - T2) and solve the linear equation for x.",
         "tier_3": correct},
        ["arithmetic_ratio_instead_of_difference"]
    )


def arch_06_arithmetic_solve_simultaneous_a_and_d(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-6, 2, 5, 8, 12])
    d = rng.choice([3, 4, 5, 7])
    p = rng.choice([4, 5, 6])
    q = rng.choice([11, 12, 14])
    tp = a + (p - 1) * d
    tq = a + (q - 1) * d
    prompt = (
        f"In an arithmetic sequence, the {p}-th term is ${tp}$ ($T_{{{p}}} = {tp}$) "
        f"and the {q}-th term is ${tq}$ ($T_{{{q}}} = {tq}$).\n\n"
        f"Determine the first term $a$ and the common difference $d$ of the sequence."
    )
    correct = f"a = {a}, d = {d}"
    distractors = [
        f"a = {a + d}, d = {d - 1}",
        f"a = {a - 2}, d = {d + 1}",
        f"a = {d}, d = {a}",
    ]
    sol = (
        f"Step 1: Set up two linear equations using $T_n = a + (n - 1)d$:\n"
        f"(1) $a + ({p} - 1)d = {tp} \\implies a + {p-1}d = {tp}$\n"
        f"(2) $a + ({q} - 1)d = {tq} \\implies a + {q-1}d = {tq}$\n"
        f"Step 2: Subtract equation (1) from (2):\n"
        f"$({q - 1} - {p - 1})d = {tq} - {tp}$\n"
        f"${q - p}d = {tq - tp} \\implies d = \\frac{{{tq - tp}}}{{{q - p}}} = {d}$\n"
        f"Step 3: Substitute $d = {d}$ into equation (1):\n"
        f"$a + {p-1}({d}) = {tp} \\implies a = {tp} - {(p-1)*d} = {a}$."
    )
    return _mcq_q(
        rng, f"g12_seq_06_{rng.randint(100000, 999999)}", "06_arithmetic_solve_simultaneous_a_and_d",
        "Solving Simultaneous Equations for Arithmetic a and d", prompt, correct, distractors, sol,
        {"tier_1": f"Express both terms as a + {p-1}d = {tp} and a + {q-1}d = {tq}.",
         "tier_2": "Subtract the two equations to eliminate a and solve for d.",
         "tier_3": correct},
        ["simultaneous_subtraction_sign_error"]
    )


def arch_07_arithmetic_negative_terms_first_negative(rng: random.Random) -> Dict[str, Any]:
    # Decreasing sequence: a > 0, d < 0
    a = rng.choice([85, 92, 104, 115, 128])
    d_abs = rng.choice([4, 6, 7, 8])
    d = -d_abs
    t1, t2, t3 = a, a + d, a + 2 * d
    # Tn < 0 => a + (n - 1)d < 0 => (n - 1)*(-d_abs) < -a => n - 1 > a / d_abs
    n_first = math.floor(a / d_abs) + 2 if a % d_abs != 0 else (a // d_abs) + 2
    # Check Tn at n_first
    val_first_neg = a + (n_first - 1) * d
    val_prev = a + (n_first - 2) * d
    prompt = (
        f"Consider the decreasing arithmetic sequence: ${t1};\\ {t2};\\ {t3};\\ \\dots$\n\n"
        f"1. Determine which term position $n$ is the first negative term in the sequence.\n"
        f"2. Calculate the value of this first negative term."
    )
    correct = f"n = {n_first}, T_{{{n_first}}} = {val_first_neg}"
    distractors = [
        f"n = {n_first - 1}, T_{{{n_first - 1}}} = {val_prev}",
        f"n = {n_first + 1}, T_{{{n_first + 1}}} = {val_first_neg - d_abs}",
        f"n = {n_first}, T_{{{n_first}}} = {-val_first_neg}",
    ]
    sol = (
        f"Step 1: Set up the inequality $T_n < 0$:\n"
        f"$a + (n - 1)d < 0$\n"
        f"${a} + (n - 1)({d}) < 0$\n"
        f"${a} - {d_abs}(n - 1) < 0$\n"
        f"${d_abs}(n - 1) > {a} \\implies n - 1 > \\frac{{{a}}}{{{d_abs}}} = {a / d_abs:.2f}$\n"
        f"$n > {a / d_abs + 1:.2f}$\n"
        f"Since $n$ must be a natural number ($n \\in \\mathbb{{N}}$), the first integer is $n = {n_first}$.\n"
        f"Step 2: Value: $T_{{{n_first}}} = {a} + ({n_first} - 1)({d}) = {val_first_neg}$."
    )
    return _mcq_q(
        rng, f"g12_seq_07_{rng.randint(100000, 999999)}", "07_arithmetic_negative_terms_first_negative",
        "First Negative Term in Decreasing Arithmetic Sequence", prompt, correct, distractors, sol,
        {"tier_1": f"Set Tn < 0, i.e., {a} + (n - 1)({d}) < 0, and remember inequality flips when dividing by negative.",
         "tier_2": f"n > {a / d_abs + 1:.2f}. Choose the smallest natural number strictly greater than this value.",
         "tier_3": correct},
        ["inequality_direction_error_when_dividing_negative"]
    )


def arch_08_arithmetic_between_multiples_count(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([6, 7, 8, 9, 11])
    lo = rng.choice([50, 75, 100])
    hi = lo + rng.choice([250, 300, 400])
    first_term = ((lo // k) + 1) * k
    last_term = (hi // k) * k
    count = (last_term - first_term) // k + 1
    prompt = (
        f"Determine how many integers between ${lo}$ and ${hi}$ are divisible by ${k}$."
    )
    ans = f"{count} terms"
    sol = (
        f"Step 1: First multiple of {k} strictly greater than {lo} is $a = {first_term}$.\n"
        f"Step 2: Last multiple of {k} less than or equal to {hi} is $l = {last_term}$.\n"
        f"Step 3: This forms an arithmetic sequence with $d = {k}$:\n"
        f"$T_n = a + (n - 1)d$\n"
        f"${last_term} = {first_term} + (n - 1)({k})$\n"
        f"${last_term - first_term} = (n - 1)({k})$\n"
        f"$n - 1 = {(last_term - first_term) // k} \\implies n = {count}$."
    )
    return _calc_q(
        rng, f"g12_seq_08_{rng.randint(100000, 999999)}", "08_arithmetic_between_multiples_count",
        "Counting Multiples in an Interval", prompt, ans, sol,
        {"tier_1": f"Find the first multiple a >= {lo} and last multiple l <= {hi}.",
         "tier_2": f"First is {first_term}, last is {last_term}. Use Tn = a + (n-1)d with d = {k}.",
         "tier_3": f"{count} terms."},
        ["interval_boundary_counting_error"]
    )


def arch_09_geometric_common_ratio_and_next_terms(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5, 6, 8])
    r = rng.choice([-3, -2, 2, 3, 4])
    t1, t2, t3 = a, a * r, a * r**2
    t4, t5, t6 = a * r**3, a * r**4, a * r**5
    prompt = (
        f"Consider the geometric sequence: ${t1};\\ {t2};\\ {t3};\\ \\dots$\n\n"
        f"1. Determine the constant common ratio $r$.\n"
        f"2. Write down the values of the next three terms ($T_4, T_5, T_6$)."
    )
    correct = f"r = {r}; T4 = {t4}, T5 = {t5}, T6 = {t6}"
    distractors = [
        f"r = {r}; T4 = {t4}, T5 = {-t5}, T6 = {t6}",
        f"r = {t2 - t1}; T4 = {t3 + (t2 - t1)}, T5 = {t3 + 2*(t2 - t1)}, T6 = {t3 + 3*(t2 - t1)}",
        f"r = {r + 1}; T4 = {a * (r+1)**3}, T5 = {a * (r+1)**4}, T6 = {a * (r+1)**5}",
    ]
    sol = (
        f"Step 1: Calculate ratio: $r = \\frac{{T_2}}{{T_1}} = \\frac{{{t2}}}{{{t1}}} = {r}$.\n"
        f"Verify: $\\frac{{T_3}}{{T_2}} = \\frac{{{t3}}}{{{t2}}} = {r}$.\n"
        f"Step 2: Next terms:\n"
        f"$T_4 = T_3 \\cdot r = {t3} \\cdot ({r}) = {t4}$\n"
        f"$T_5 = T_4 \\cdot r = {t4} \\cdot ({r}) = {t5}$\n"
        f"$T_6 = T_5 \\cdot r = {t5} \\cdot ({r}) = {t6}$."
    )
    return _mcq_q(
        rng, f"g12_seq_09_{rng.randint(100000, 999999)}", "09_geometric_common_ratio_and_next_terms",
        "Geometric Common Ratio and Successive Terms", prompt, correct, distractors, sol,
        {"tier_1": "Divide the second term by the first term to find r = T2 / T1.",
         "tier_2": f"r = {t2}/{t1} = {r}. Multiply consecutively by r to get T4, T5, T6.",
         "tier_3": correct},
        ["confuses_common_ratio_with_common_difference"]
    )


def arch_10_geometric_general_term_formula(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 5, 7, 9, 12])
    r = rng.choice([-3, -2, 2, 3, 5])
    t1, t2, t3 = a, a * r, a * r**2
    prompt = (
        f"Given the geometric sequence: ${t1};\\ {t2};\\ {t3};\\ \\dots$\n\n"
        f"Determine the general term formula $T_n$ in terms of $n$."
    )
    correct = f"T_n = {a} \\cdot ({r})^{{n - 1}}" if r < 0 else f"T_n = {a} \\cdot {r}^{{n - 1}}"
    distractors = [
        f"T_n = {a * r}^{{n - 1}}",
        f"T_n = {a} + (n - 1)({r})",
        f"T_n = {r} \\cdot ({a})^{{n - 1}}",
    ]
    sol = (
        f"Step 1: First term $a = {a}$.\n"
        f"Step 2: Common ratio $r = \\frac{{{t2}}}{{{t1}}} = {r}$.\n"
        f"Step 3: General term formula $T_n = a r^{{n - 1}}$:\n"
        f"$T_n = {correct}$."
    )
    return _mcq_q(
        rng, f"g12_seq_10_{rng.randint(100000, 999999)}", "10_geometric_general_term_formula",
        "General Term of a Geometric Sequence", prompt, correct, distractors, sol,
        {"tier_1": "Recall the geometric formula Tn = a * r^(n - 1).",
         "tier_2": f"Here a = {a} and r = {r}. Do not multiply a and r together prematurely!",
         "tier_3": correct},
        ["multiplying_base_and_first_term_violating_bodmas"]
    )


def arch_11_geometric_find_specific_term(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5, 6])
    r = rng.choice([2, 3])
    k = rng.choice([7, 8, 9, 10])
    val = a * (r ** (k - 1))
    t1, t2, t3 = a, a * r, a * r**2
    prompt = (
        f"Consider the geometric sequence: ${t1};\\ {t2};\\ {t3};\\ \\dots$\n\n"
        f"Calculate the numerical value of the {k}-th term ($T_{{{k}}}$)."
    )
    ans = str(val)
    sol = (
        f"Step 1: Identify $a = {a}$ and $r = \\frac{{{t2}}}{{{t1}}} = {r}$.\n"
        f"Step 2: Use $T_n = a r^{{n - 1}}$ with $n = {k}$:\n"
        f"$T_{{{k}}} = {a} \\cdot ({r})^{{{k} - 1}} = {a} \\cdot ({r}^{{{k - 1}}}) = {a} \\cdot {r**(k-1)} = {val}$."
    )
    return _calc_q(
        rng, f"g12_seq_11_{rng.randint(100000, 999999)}", "11_geometric_find_specific_term",
        "Calculating Specific Term in Geometric Sequence", prompt, ans, sol,
        {"tier_1": f"Substitute a = {a}, r = {r}, and n = {k} into Tn = a * r^(n-1).",
         "tier_2": f"Calculate {r}^{{{k-1}}} first, then multiply by {a}.",
         "tier_3": f"T_{{{k}}} = {val}."},
        ["exponent_off_by_one_using_n_instead_of_n_minus_1"]
    )


def arch_12_geometric_find_term_position_log(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5, 7])
    r = rng.choice([2, 3, 4])
    n = rng.choice([6, 7, 8, 9])
    target = a * (r ** (n - 1))
    t1, t2, t3 = a, a * r, a * r**2
    prompt = (
        f"Given the geometric sequence: ${t1};\\ {t2};\\ {t3};\\ \\dots$\n\n"
        f"Determine the position $n$ for which the term equals ${target}$."
    )
    ans = f"n = {n}"
    sol = (
        f"Step 1: Identify $a = {a}$ and $r = {r}$. Set $T_n = {target}$.\n"
        f"Step 2: Substitute into $T_n = a r^{{n - 1}}$:\n"
        f"${target} = {a} \\cdot ({r})^{{n - 1}}$\n"
        f"${target // a} = {r}^{{n - 1}}$\n"
        f"Step 3: Solve exponential equation by equating bases or logarithms:\n"
        f"${r}^{{{n - 1}}} = {r}^{{n - 1}} \\implies n - 1 = {n - 1} \\implies n = {n}$."
    )
    return _calc_q(
        rng, f"g12_seq_12_{rng.randint(100000, 999999)}", "12_geometric_find_term_position_log",
        "Determining Geometric Term Position via Logarithms/Exponents", prompt, ans, sol,
        {"tier_1": f"Divide {target} by {a} to isolate the base {r}^(n - 1).",
         "tier_2": f"{target // a} = {r}^(n - 1). Express {target // a} as a power of {r}.",
         "tier_3": f"n = {n}."},
        ["logarithm_base_mismatch"]
    )


def arch_13_geometric_solve_unknown_terms_ratio(rng: random.Random) -> Dict[str, Any]:
    # Geometric sequence consecutive terms in terms of x:
    # (x - p), (x + q), (x + k) or similar.
    # T2^2 = T1 * T3
    # Let x = 6. (x - 2) = 4, (x + 2) = 8, (x + 10) = 16.
    # (x + 2)^2 = (x - 2)(x + 10) => x^2 + 4x + 4 = x^2 + 8x - 20 => 4x = 24 => x = 6.
    x_val = rng.choice([4, 6, 8, 10])
    q_val = 2
    # (x + q)^2 = (x - p)(x + k) => x^2 + 2qx + q^2 = x^2 + (k - p)x - kp
    # Let p = 2. Then (k - 2)x - 2k = 4x + 4 => (k - 6)x = 2k + 4
    # When x = 6: 6k - 36 = 2k + 4 => 4k = 40 => k = 10.
    # Let's parameterize based on a chosen ratio r:
    r = rng.choice([2, 3])
    # T1 = x - c, T2 = r*(x - c), T3 = r^2*(x - c)
    # T1 = x - 1, T2 = x + 3, T3 = 2x + 10 for r=2:
    # (x + 3)/(x - 1) = 2 => x + 3 = 2x - 2 => x = 5.
    # Terms: 4, 8, 16 (r = 2). T3 = 2(5) + 6 = 16.
    # Let T1 = x - 1, T2 = x + 3, T3 = 2x + 6.
    # T2^2 = (x + 3)^2 = x^2 + 6x + 9.
    # T1*T3 = (x - 1)(2x + 6) = 2x^2 + 4x - 6.
    # That gives a quadratic. Let's make it direct linear:
    # T1 = x - 2, T2 = x + 2, T3 = 2x + 4 when r=2, x=6: T1=4, T2=8, T3=16.
    # T2 / T1 = (x + 2)/(x - 2). T3 / T2 = (2x + 4)/(x + 2) = 2.
    # So (x + 2)/(x - 2) = 2 => x + 2 = 2x - 4 => x = 6.
    p_offset = rng.choice([2, 3, 4])
    r_choice = rng.choice([2, 3])
    # (x + k)/(x - p) = r => x + k = r*x - r*p => (r - 1)x = k + r*p
    # Pick x such that terms are positive integers
    x_sol = rng.choice([5, 6, 7, 8])
    k_offset = (r_choice - 1) * x_sol - r_choice * p_offset
    t1_term = f"x - {p_offset}"
    t2_term = f"x + {k_offset}" if k_offset >= 0 else f"x - {abs(k_offset)}"
    v1 = x_sol - p_offset
    v2 = v1 * r_choice
    v3 = v2 * r_choice
    t3_term = f"{r_choice}x + {v3 - r_choice * x_sol}" if (v3 - r_choice * x_sol) >= 0 else f"{r_choice}x - {abs(v3 - r_choice * x_sol)}"

    prompt = (
        f"The first three terms of a geometric sequence are:\n"
        f"$${t1_term};\\ {t2_term};\\ {t3_term}$$\n\n"
        f"Determine the value of $x$ (given $x > {p_offset}$) and write down the numerical values of the three terms."
    )
    correct = f"x = {x_sol}; terms are {v1}, {v2}, {v3}"
    distractors = [
        f"x = {x_sol + 1}; terms are {v1 + 1}, {v2 + 2}, {v3 + 4}",
        f"x = {x_sol - 1}; terms are {v1 - 1}, {v2 - 2}, {v3 - 4}",
        f"x = {x_sol}; terms are {v1}, {v1 + 4}, {v1 + 8}",
    ]
    sol = (
        f"Step 1: Set constant ratio condition: $\\frac{{T_2}}{{T_1}} = \\frac{{T_3}}{{T_2}} = r$.\n"
        f"$$\\frac{{{t2_term}}}{{{t1_term}}} = {r_choice}$$\n"
        f"$${t2_term} = {r_choice}({t1_term})$$\n"
        f"Solving for $x$ yields $x = {x_sol}$.\n"
        f"Step 2: Calculate numerical terms:\n"
        f"$T_1 = {x_sol} - {p_offset} = {v1}$\n"
        f"$T_2 = {v2}$\n"
        f"$T_3 = {v3}$."
    )
    return _mcq_q(
        rng, f"g12_seq_13_{rng.randint(100000, 999999)}", "13_geometric_solve_unknown_terms_ratio",
        "Solving for Unknown Variable in Geometric Sequence", prompt, correct, distractors, sol,
        {"tier_1": "In a geometric sequence, T2 / T1 = T3 / T2 = r.",
         "tier_2": "Cross-multiply or equate the ratio to solve the equation for x.",
         "tier_3": correct},
        ["treated_geometric_as_arithmetic_subtraction"]
    )


def arch_14_geometric_solve_simultaneous_a_and_r(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5, 6])
    r = rng.choice([2, 3])
    t3 = a * (r ** 2)
    t6 = a * (r ** 5)
    prompt = (
        f"In a geometric sequence of positive terms, the 3rd term is ${t3}$ ($T_3 = {t3}$) "
        f"and the 6th term is ${t6}$ ($T_6 = {t6}$).\n\n"
        f"Determine the first term $a$ and common ratio $r$."
    )
    correct = f"a = {a}, r = {r}"
    distractors = [
        f"a = {a + 1}, r = {r}",
        f"a = {a}, r = {r + 1}",
        f"a = {r}, r = {a}",
    ]
    sol = (
        f"Step 1: Express terms using $T_n = a r^{{n-1}}$:\n"
        f"(1) $a r^2 = {t3}$\n"
        f"(2) $a r^5 = {t6}$\n"
        f"Step 2: Divide equation (2) by equation (1):\n"
        f"$$\\frac{{a r^5}}{{a r^2}} = \\frac{{{t6}}}{{{t3}}}$$\n"
        f"$$r^3 = {t6 // t3} \\implies r = \\sqrt[3]{{{t6 // t3}}} = {r}$$\n"
        f"Step 3: Substitute $r = {r}$ back into equation (1):\n"
        f"$$a ({r}^2) = {t3} \\implies a({r**2}) = {t3} \\implies a = \\frac{{{t3}}}{{{r**2}}} = {a}$$."
    )
    return _mcq_q(
        rng, f"g12_seq_14_{rng.randint(100000, 999999)}", "14_geometric_solve_simultaneous_a_and_r",
        "Solving Simultaneous Equations for Geometric a and r", prompt, correct, distractors, sol,
        {"tier_1": "Write a * r^2 = T3 and a * r^5 = T6.",
         "tier_2": "Divide the higher equation by the lower equation to eliminate a and solve r^3.",
         "tier_3": correct},
        ["subtracted_instead_of_divided_geometric_equations"]
    )


def arch_15_geometric_alternating_signs_analysis(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    r = rng.choice([-3, -2])
    terms = [a * (r ** i) for i in range(5)]
    prompt = (
        f"Consider the sequence: ${terms[0]};\\ {terms[1]};\\ {terms[2]};\\ {terms[3]};\\ {terms[4]};\\ \\dots$\n\n"
        f"Explain why the signs of the terms alternate, state the common ratio $r$, and deduce whether $T_{{50}}$ is positive or negative."
    )
    correct = f"r = {r}; signs alternate because r < 0; T50 is negative"
    distractors = [
        f"r = {abs(r)}; signs alternate due to addition; T50 is positive",
        f"r = {r}; signs alternate because r < 0; T50 is positive",
        f"r = {-r}; signs alternate because a > 0; T50 is negative",
    ]
    sol = (
        f"Step 1: Common ratio $r = \\frac{{{terms[1]}}}{{{terms[0]}}} = {r}$.\n"
        f"Step 2: Since $r = {r} < 0$, multiplying by a negative number reverses the sign at every step.\n"
        f"Step 3: General term is $T_n = a r^{{n-1}} = {a} \\cdot ({r})^{{n - 1}}$.\n"
        f"For $n = 50$, the exponent $n - 1 = 49$ is odd.\n"
        f"A negative number raised to an odd power remains negative, so $T_{{50}} < 0$ (negative)."
    )
    return _mcq_q(
        rng, f"g12_seq_15_{rng.randint(100000, 999999)}", "15_geometric_alternating_signs_analysis",
        "Alternating Geometric Sequences and Sign Parity", prompt, correct, distractors, sol,
        {"tier_1": "Look at the ratio between consecutive terms and recall (-1)^odd is negative.",
         "tier_2": "For T50, the power on r is 50 - 1 = 49, which is odd.",
         "tier_3": correct},
        ["forgot_exponent_is_n_minus_one_for_parity"]
    )


def arch_16_arithmetic_mean_insertion(rng: random.Random) -> Dict[str, Any]:
    # Insert k arithmetic means between X and Y
    # Means form an arithmetic sequence of k + 2 terms: T1 = X, T_{k+2} = Y
    x = rng.choice([3, 5, 8, 12])
    k_means = rng.choice([3, 4, 5])
    d = rng.choice([3, 4, 6, 7])
    n_total = k_means + 2
    y = x + (n_total - 1) * d
    means = [x + i * d for i in range(1, k_means + 1)]
    means_str = ", ".join(str(m) for m in means)
    prompt = (
        f"Insert ${k_means}$ arithmetic means between ${x}$ and ${y}$."
    )
    ans = f"{means_str}"
    sol = (
        f"Step 1: Total number of terms in the arithmetic sequence is $n = {k_means} + 2 = {n_total}$.\n"
        f"Step 2: First term $a = {x}$, last term $T_{{{n_total}}} = {y}$.\n"
        f"$T_{{{n_total}}} = a + ({n_total} - 1)d$\n"
        f"${y} = {x} + {n_total - 1}d \\implies {y - x} = {n_total - 1}d \\implies d = {d}$.\n"
        f"Step 3: The inserted means are:\n"
        f"{means_str}."
    )
    return _calc_q(
        rng, f"g12_seq_16_{rng.randint(100000, 999999)}", "16_arithmetic_mean_insertion",
        "Inserting Arithmetic Means Between Two Values", prompt, ans, sol,
        {"tier_1": f"The full sequence has {k_means} + 2 = {n_total} terms with T1 = {x} and T{n_total} = {y}.",
         "tier_2": f"Find d = ({y} - {x}) / {n_total - 1}.",
         "tier_3": f"Means: {means_str}."},
        ["incorrect_total_terms_excluding_endpoints"]
    )


def arch_17_geometric_mean_insertion(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([2, 3, 5])
    r = rng.choice([2, 3])
    k_means = rng.choice([2, 3])
    n_total = k_means + 2
    y = x * (r ** (n_total - 1))
    means = [x * (r ** i) for i in range(1, k_means + 1)]
    means_str = ", ".join(str(m) for m in means)
    prompt = (
        f"Insert ${k_means}$ positive geometric means between ${x}$ and ${y}$."
    )
    ans = f"{means_str}"
    sol = (
        f"Step 1: Total number of terms is $n = {k_means} + 2 = {n_total}$.\n"
        f"Step 2: $T_1 = a = {x}$ and $T_{{{n_total}}} = a r^{{{n_total - 1}}} = {y}$.\n"
        f"$${x} r^{{{n_total - 1}}} = {y} \\implies r^{{{n_total - 1}}} = {y // x} \\implies r = {r}$$.\n"
        f"Step 3: Multiply consecutively by $r = {r}$ to find the means:\n"
        f"{means_str}."
    )
    return _calc_q(
        rng, f"g12_seq_17_{rng.randint(100000, 999999)}", "17_geometric_mean_insertion",
        "Inserting Geometric Means Between Two Values", prompt, ans, sol,
        {"tier_1": f"Total terms = {n_total}. Set {x} * r^{{{n_total - 1}}} = {y}.",
         "tier_2": f"Solve r^{{{n_total - 1}}} = {y // x} to find r.",
         "tier_3": f"Means: {means_str}."},
        ["arithmetic_difference_used_instead_of_ratio"]
    )


def arch_18_series_definition_partial_sums(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    d = rng.choice([3, 4, 5])
    terms = [a + i * d for i in range(4)]
    s1 = terms[0]
    s2 = s1 + terms[1]
    s3 = s2 + terms[2]
    s4 = s3 + terms[3]
    prompt = (
        f"Given the sequence with general term $T_n = {d}n {'+' if a - d >= 0 else '-'} {abs(a - d)}$:\n\n"
        f"Calculate the first four partial sums: $S_1, S_2, S_3, S_4$."
    )
    correct = f"S1 = {s1}, S2 = {s2}, S3 = {s3}, S4 = {s4}"
    distractors = [
        f"S1 = {terms[0]}, S2 = {terms[1]}, S3 = {terms[2]}, S4 = {terms[3]}",
        f"S1 = {s1}, S2 = {s2 + 1}, S3 = {s3 + 2}, S4 = {s4 + 3}",
        f"S1 = {s1}, S2 = {s1 * 2}, S3 = {s1 * 3}, S4 = {s1 * 4}",
    ]
    sol = (
        f"Step 1: Write the first four terms $T_n$:\n"
        f"$T_1 = {terms[0]},\\ T_2 = {terms[1]},\\ T_3 = {terms[2]},\\ T_4 = {terms[3]}$.\n"
        f"Step 2: Calculate partial sums by cumulative addition:\n"
        f"$S_1 = T_1 = {s1}$\n"
        f"$S_2 = T_1 + T_2 = {s1} + {terms[1]} = {s2}$\n"
        f"$S_3 = S_2 + T_3 = {s2} + {terms[2]} = {s3}$\n"
        f"$S_4 = S_3 + T_4 = {s3} + {terms[3]} = {s4}$."
    )
    return _mcq_q(
        rng, f"g12_seq_18_{rng.randint(100000, 999999)}", "18_series_definition_partial_sums",
        "Partial Sums of a Series", prompt, correct, distractors, sol,
        {"tier_1": "Partial sums Sn accumulate the sum of all terms from T1 up to Tn.",
         "tier_2": "Calculate T1..T4 first, then sum cumulatively: S2 = T1 + T2, etc.",
         "tier_3": correct},
        ["confuses_terms_Tn_with_partial_sums_Sn"]
    )


def arch_19_term_from_sum_formula_tn_sn_sn_minus_1(rng: random.Random) -> Dict[str, Any]:
    # Sn = A*n^2 + B*n
    # Tn = Sn - S_{n-1} = A*n^2 + B*n - [A*(n-1)^2 + B*(n-1)]
    # = A*n^2 + B*n - [A*(n^2 - 2n + 1) + Bn - B]
    # = 2A*n - A + B
    A = rng.choice([2, 3, 4])
    B = rng.choice([-3, 1, 2, 5])
    twoA = 2 * A
    const = B - A
    sign = "+" if const >= 0 else "-"
    abs_const = abs(const)
    tn_formula = f"{twoA}n {sign} {abs_const}" if abs_const != 0 else f"{twoA}n"

    # Evaluate for n = 10
    t10 = twoA * 10 + const
    prompt = (
        f"The sum of the first $n$ terms of a certain series is given by:\n"
        f"$$S_n = {A}n^2 {'+' if B >= 0 else '-'} {abs(B)}n$$\n\n"
        f"1. Determine the expression for the general term $T_n$ by using $T_n = S_n - S_{{n-1}}$.\n"
        f"2. Hence, calculate the value of $T_{{10}}$."
    )
    correct = f"T_n = {tn_formula}; T10 = {t10}"
    distractors = [
        f"T_n = {A}n {'+' if B >= 0 else '-'} {abs(B)}; T10 = {A*10 + B}",
        f"T_n = {twoA}n {'+' if B >= 0 else '-'} {abs(B)}; T10 = {twoA*10 + B}",
        f"T_n = {tn_formula}; T10 = {t10 + 5}",
    ]
    sol = (
        f"Step 1: Apply the fundamental relation $T_n = S_n - S_{{n-1}}$ (for $n \\ge 2$):\n"
        f"$$S_{{n-1}} = {A}(n - 1)^2 + {B}(n - 1) = {A}(n^2 - 2n + 1) + {B}n - {B}$$\n"
        f"$$S_{{n-1}} = {A}n^2 - {2*A}n + {A} + {B}n - {B}$$\n"
        f"Subtract $S_{{n-1}}$ from $S_n$:\n"
        f"$$T_n = [{A}n^2 + {B}n] - [{A}n^2 + ({B} - {2*A})n + ({A} - {B})]$$\n"
        f"$$T_n = {twoA}n + ({B} - {A}) = {tn_formula}$$.\n"
        f"Step 2: For $n = 10$:\n"
        f"$$T_{{10}} = {twoA}(10) {'+' if const >= 0 else '-'} {abs_const} = {t10}$$."
    )
    return _mcq_q(
        rng, f"g12_seq_19_{rng.randint(100000, 999999)}", "19_term_from_sum_formula_tn_sn_sn_minus_1",
        "Finding Tn from Sn Formula via Subtraction", prompt, correct, distractors, sol,
        {"tier_1": "Recall the identity Tn = Sn - S(n - 1).",
         "tier_2": f"Expand S(n - 1) = {A}(n - 1)^2 + {B}(n - 1) carefully before subtracting.",
         "tier_3": correct},
        ["forgot_to_expand_binomial_in_s_n_minus_1"]
    )


def arch_20_arithmetic_series_sum_formula_basic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 5, 8, 12])
    d = rng.choice([3, 4, 6, 7])
    n = rng.choice([15, 20, 24, 30])
    sn = (n * (2 * a + (n - 1) * d)) // 2
    t1, t2, t3 = a, a + d, a + 2 * d
    prompt = (
        f"Calculate the sum of the first ${n}$ terms of the arithmetic series:\n"
        f"$${t1} + {t2} + {t3} + \\dots$$"
    )
    ans = str(sn)
    sol = (
        f"Step 1: First term $a = {t1}$, common difference $d = {t2} - {t1} = {d}$, and $n = {n}$.\n"
        f"Step 2: Substitute into the arithmetic sum formula:\n"
        f"$$S_n = \\frac{{n}}{{2}}[2a + (n - 1)d]$$\n"
        f"$$S_{{{n}}} = \\frac{{{n}}}{{2}}[2({a}) + ({n} - 1)({d})]$$\n"
        f"$$S_{{{n}}} = \\frac{{{n}}}{{2}}[{2*a} + {(n-1)*d}] = \\frac{{{n}}}{{2}}[{2*a + (n-1)*d}] = {sn}$$."
    )
    return _calc_q(
        rng, f"g12_seq_20_{rng.randint(100000, 999999)}", "20_arithmetic_series_sum_formula_basic",
        "Sum of an Arithmetic Series", prompt, ans, sol,
        {"tier_1": "Use the formula Sn = n/2 * [2a + (n - 1)d].",
         "tier_2": f"Substitute a = {a}, d = {d}, and n = {n}.",
         "tier_3": f"S_{{{n}}} = {sn}."},
        ["arithmetic_sum_formula_substitution_error"]
    )


def arch_21_arithmetic_series_sum_with_last_term(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([4, 7, 11, 15])
    d = rng.choice([3, 5, 6])
    n = rng.choice([25, 30, 40])
    l = a + (n - 1) * d
    sn = (n * (a + l)) // 2
    t1, t2, t3 = a, a + d, a + 2 * d
    prompt = (
        f"Evaluate the sum of the arithmetic series:\n"
        f"$${t1} + {t2} + {t3} + \\dots + {l}$$\n\n"
        f"(Hint: Find the number of terms $n$ first, then calculate $S_n$)."
    )
    ans = str(sn)
    sol = (
        f"Step 1: Find $n$ using $T_n = a + (n - 1)d = l$:\n"
        f"${l} = {a} + (n - 1)({d}) \\implies {l - a} = {d}(n - 1) \\implies n - 1 = {(l - a) // d} \\implies n = {n}$.\n"
        f"Step 2: Use $S_n = \\frac{{n}}{{2}}(a + l)$:\n"
        f"$$S_{{{n}}} = \\frac{{{n}}}{{2}}({a} + {l}) = \\frac{{{n}}}{{2}}({a + l}) = {sn}$$."
    )
    return _calc_q(
        rng, f"g12_seq_21_{rng.randint(100000, 999999)}", "21_arithmetic_series_sum_with_last_term",
        "Arithmetic Series Sum with Known Last Term", prompt, ans, sol,
        {"tier_1": "First find n from Tn = l = a + (n - 1)d.",
         "tier_2": f"Here n = {n}. Then apply Sn = (n / 2) * (a + l).",
         "tier_3": f"S = {sn}."},
        ["omitted_finding_n_before_summing"]
    )


def arch_22_arithmetic_series_solve_for_n_quadratic(rng: random.Random) -> Dict[str, Any]:
    # Sn = n/2 * [2a + (n - 1)d] = target
    # d*n^2 + (2a - d)*n - 2*target = 0
    a = rng.choice([3, 5, 7])
    d = rng.choice([2, 4])
    n = rng.choice([12, 15, 18, 20])
    target = (n * (2 * a + (n - 1) * d)) // 2
    prompt = (
        f"The sum of the first $n$ terms of the sequence $T_n = {d}n {'+' if a - d >= 0 else '-'} {abs(a - d)}$ is ${target}$.\n\n"
        f"Calculate the value of $n$."
    )
    ans = f"n = {n}"
    sol = (
        f"Step 1: Set up the formula $S_n = \\frac{{n}}{{2}}[2a + (n - 1)d] = {target}$:\n"
        f"$$\\frac{{n}}{{2}}[2({a}) + ({d})(n - 1)] = {target}$$\n"
        f"$$n[{2*a} + {d}n - {d}] = {2 * target}$$\n"
        f"$$n[{d}n + {2*a - d}] = {2 * target} \\implies {d}n^2 + {2*a - d}n - {2 * target} = 0$$\n"
        f"Step 2: Factorise or apply the quadratic formula:\n"
        f"$(n - {n})(...) = 0 \\implies n = {n}$ (reject negative root since $n \\in \\mathbb{{N}}$)."
    )
    return _calc_q(
        rng, f"g12_seq_22_{rng.randint(100000, 999999)}", "22_arithmetic_series_solve_for_n_quadratic",
        "Solving for Number of Terms n in Arithmetic Series", prompt, ans, sol,
        {"tier_1": f"Equate n/2 * [2({a}) + (n - 1)({d})] = {target} and simplify into a quadratic equation in n.",
         "tier_2": "Solve the quadratic equation and keep only the positive integer solution.",
         "tier_3": f"n = {n}."},
        ["accepted_negative_root_for_term_count"]
    )


def arch_23_arithmetic_sum_multiples_in_range(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([4, 6, 8])
    lo = 100
    hi = 300
    first = ((lo // k) + 1) * k
    last = (hi // k) * k
    n = (last - first) // k + 1
    total = (n * (first + last)) // 2
    prompt = (
        f"Find the sum of all natural numbers between ${lo}$ and ${hi}$ that are divisible by ${k}$."
    )
    ans = str(total)
    sol = (
        f"Step 1: First multiple strictly between {lo} and {hi}: $a = {first}$.\n"
        f"Step 2: Last multiple strictly between {lo} and {hi}: $l = {last}$.\n"
        f"Step 3: Number of terms: $n = \\frac{{{last} - {first}}}{{{k}}} + 1 = {n}$.\n"
        f"Step 4: Sum: $S_{{{n}}} = \\frac{{{n}}}{{2}}(a + l) = \\frac{{{n}}}{{2}}({first} + {last}) = {total}$."
    )
    return _calc_q(
        rng, f"g12_seq_23_{rng.randint(100000, 999999)}", "23_arithmetic_sum_multiples_in_range",
        "Sum of Multiples in an Interval", prompt, ans, sol,
        {"tier_1": f"Identify the first multiple >= {lo} and last multiple <= {hi}.",
         "tier_2": f"First term = {first}, last term = {last}. Use Sn = n/2 * (a + l).",
         "tier_3": f"Sum = {total}."},
        ["incorrect_number_of_multiples_boundary"]
    )


def arch_24_arithmetic_sum_multiples_excluding_others(rng: random.Random) -> Dict[str, Any]:
    # Sum of multiples of 3 not divisible by 6 (or odd multiples of 3) up to N
    limit = rng.choice([60, 90, 120])
    # Multiples of 3: 3, 6, 9, 12 ... limit
    # Those NOT divisible by 2 are: 3, 9, 15, 21 ... (arithmetic with a=3, d=6)
    last_odd_mult = ((limit // 3) if (limit // 3) % 2 != 0 else (limit // 3) - 1) * 3
    n = (last_odd_mult - 3) // 6 + 1
    sum_val = (n * (3 + last_odd_mult)) // 2
    prompt = (
        f"Calculate the sum of all multiples of $3$ between $1$ and ${limit}$ that are **not** divisible by $2$."
    )
    ans = str(sum_val)
    sol = (
        f"Step 1: Multiples of 3 that are not even form an arithmetic sequence:\n"
        f"$3;\\ 9;\\ 15;\\ 21;\\ \\dots;\\ {last_odd_mult}$.\n"
        f"Step 2: Parameters: $a = 3$, $d = 6$, and last term $l = {last_odd_mult}$.\n"
        f"Step 3: Number of terms: $n = \\frac{{{last_odd_mult} - 3}}{{6}} + 1 = {n}$.\n"
        f"Step 4: Sum: $S_{{{n}}} = \\frac{{{n}}}{{2}}(3 + {last_odd_mult}) = {sum_val}$."
    )
    return _calc_q(
        rng, f"g12_seq_24_{rng.randint(100000, 999999)}", "24_arithmetic_sum_multiples_excluding_others",
        "Sum of Filtered Multiples", prompt, ans, sol,
        {"tier_1": "Recognise that odd multiples of 3 have a common difference of d = 6.",
         "tier_2": f"First is 3, last is {last_odd_mult}. Find n and apply Sn.",
         "tier_3": f"Sum = {sum_val}."},
        ["failure_to_recognise_new_common_difference"]
    )


def arch_25_arithmetic_series_word_problem_savings(rng: random.Random) -> Dict[str, Any]:
    start_amount = rng.choice([50, 100, 150])
    monthly_increase = rng.choice([20, 30, 50])
    months = rng.choice([12, 18, 24])
    total = (months * (2 * start_amount + (months - 1) * monthly_increase)) // 2
    last_month = start_amount + (months - 1) * monthly_increase
    prompt = (
        f"A learner begins saving money for university. In the 1st month they save R{start_amount}. "
        f"Each subsequent month, they increase their savings deposit by R{monthly_increase}.\n\n"
        f"1. How much money do they deposit in the {months}-th month?\n"
        f"2. What is the total accumulated savings after {months} months?"
    )
    correct = f"Month {months}: R{last_month}; Total: R{total}"
    distractors = [
        f"Month {months}: R{last_month + 50}; Total: R{total + 300}",
        f"Month {months}: R{last_month}; Total: R{start_amount * months}",
        f"Month {months}: R{start_amount + months * monthly_increase}; Total: R{total}",
    ]
    sol = (
        f"Step 1: Monthly deposits form an arithmetic series with $a = {start_amount}$, $d = {monthly_increase}$, and $n = {months}$.\n"
        f"Step 2: Deposit in month {months}:\n"
        f"$T_{{{months}}} = a + ({months} - 1)d = {start_amount} + ({months - 1})({monthly_increase}) = {last_month}$.\n"
        f"Step 3: Total accumulated savings:\n"
        f"$S_{{{months}}} = \\frac{{{months}}}{{2}}[2({start_amount}) + ({months} - 1)({monthly_increase})] = {total}$."
    )
    return _mcq_q(
        rng, f"g12_seq_25_{rng.randint(100000, 999999)}", "25_arithmetic_series_word_problem_savings",
        "Applied Word Problem on Arithmetic Savings", prompt, correct, distractors, sol,
        {"tier_1": f"Model deposits as an arithmetic progression with a = {start_amount} and d = {monthly_increase}.",
         "tier_2": f"Find T_{{{months}}} for part 1, and S_{{{months}}} for part 2.",
         "tier_3": correct},
        ["confuses_specific_month_deposit_with_total_sum"]
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_arithmetic_common_diff_and_next_terms": arch_01_arithmetic_common_diff_and_next_terms,
    "02_arithmetic_general_term_formula": arch_02_arithmetic_general_term_formula,
    "03_arithmetic_find_specific_term": arch_03_arithmetic_find_specific_term,
    "04_arithmetic_find_term_position": arch_04_arithmetic_find_term_position,
    "05_arithmetic_solve_unknown_terms_linear": arch_05_arithmetic_solve_unknown_terms_linear,
    "06_arithmetic_solve_simultaneous_a_and_d": arch_06_arithmetic_solve_simultaneous_a_and_d,
    "07_arithmetic_negative_terms_first_negative": arch_07_arithmetic_negative_terms_first_negative,
    "08_arithmetic_between_multiples_count": arch_08_arithmetic_between_multiples_count,
    "09_geometric_common_ratio_and_next_terms": arch_09_geometric_common_ratio_and_next_terms,
    "10_geometric_general_term_formula": arch_10_geometric_general_term_formula,
    "11_geometric_find_specific_term": arch_11_geometric_find_specific_term,
    "12_geometric_find_term_position_log": arch_12_geometric_find_term_position_log,
    "13_geometric_solve_unknown_terms_ratio": arch_13_geometric_solve_unknown_terms_ratio,
    "14_geometric_solve_simultaneous_a_and_r": arch_14_geometric_solve_simultaneous_a_and_r,
    "15_geometric_alternating_signs_analysis": arch_15_geometric_alternating_signs_analysis,
    "16_arithmetic_mean_insertion": arch_16_arithmetic_mean_insertion,
    "17_geometric_mean_insertion": arch_17_geometric_mean_insertion,
    "18_series_definition_partial_sums": arch_18_series_definition_partial_sums,
    "19_term_from_sum_formula_tn_sn_sn_minus_1": arch_19_term_from_sum_formula_tn_sn_sn_minus_1,
    "20_arithmetic_series_sum_formula_basic": arch_20_arithmetic_series_sum_formula_basic,
    "21_arithmetic_series_sum_with_last_term": arch_21_arithmetic_series_sum_with_last_term,
    "22_arithmetic_series_solve_for_n_quadratic": arch_22_arithmetic_series_solve_for_n_quadratic,
    "23_arithmetic_sum_multiples_in_range": arch_23_arithmetic_sum_multiples_in_range,
    "24_arithmetic_sum_multiples_excluding_others": arch_24_arithmetic_sum_multiples_excluding_others,
    "25_arithmetic_series_word_problem_savings": arch_25_arithmetic_series_word_problem_savings,
}
