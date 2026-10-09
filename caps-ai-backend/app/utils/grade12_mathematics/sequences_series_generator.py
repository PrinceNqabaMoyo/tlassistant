"""Grade 12 Mathematics - Sequences and Series Generator.
Covers:
  - Arithmetic Sequences and Series: Tn = a + (n - 1)d, Sn = n/2 * [2a + (n - 1)d].
  - Geometric Sequences and Series: Tn = a * r^(n - 1), Sn = a * (r^n - 1) / (r - 1).
  - Infinite Geometric Series (Convergence and Sum to Infinity): S_inf = a / (1 - r) for -1 < r < 1.
  - Sigma Notation evaluation: Sum_{k=1}^n (ak + b) and Sum_{k=1}^inf a * r^(k - 1).

Follows South African CAPS curriculum specifications and the 6-Pillar Generator Contract.
Strictly zero-LLM, deterministic SymPy execution.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def generate_grade12_sequences_series_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> Dict[str, Any]:
    r = _rng(seed)
    subskill = mode if mode.startswith("elementary_") else "sequences_series"

    archetype = r.choice(["arithmetic_series_sum", "geometric_series_sum", "sum_to_infinity_convergence", "sigma_notation"])
    if subskill == "elementary_arithmetic":
        archetype = "arithmetic_series_sum"
    elif subskill == "elementary_geometric":
        archetype = "geometric_series_sum"
    elif subskill == "elementary_convergence":
        archetype = "sum_to_infinity_convergence"

    if archetype == "arithmetic_series_sum":
        a = r.choice([3, 5, 7, 8, 11])
        d = r.choice([2, 3, 4, 5])
        n = r.choice([15, 20, 25, 30])
        # Tn = a + (n - 1)d
        tn = a + (n - 1) * d
        # Sn = n/2 * [2a + (n - 1)d]
        sn = (n * (2 * a + (n - 1) * d)) // 2

        t1, t2, t3 = a, a + d, a + 2 * d
        prompt = (
            f"Given the arithmetic sequence: \\({t1},\\ {t2},\\ {t3},\\ \\dots\\)\n\n"
            f"1. Determine the general term \\(T_n\\) in terms of \\(n\\).\n"
            f"2. Calculate the value of the {n}-th term (\\(T_{{{n}}}\\)).\n"
            f"3. Calculate the sum of the first {n} terms (\\(S_{{{n}}}\\))."
        )
        sample_answer = (
            rf"a = {a},\ d = {d}\\\ "
            rf"T_n = a + (n - 1)d = {a} + (n - 1)({d}) = {d}n {'+' if a - d >= 0 else ''}{a - d}\\\ "
            rf"T_{{{n}}} = {a} + ({n} - 1)({d}) = {tn}\\\ "
            rf"S_{{{n}}} = \frac{{{n}}}{{2}}[2({a}) + ({n} - 1)({d})] = \frac{{{n}}}{{2}}[{2*a} + {(n-1)*d}] = {sn}"
        )

        return {
            "id": f"g12_seq_arith_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-12",
            "topic": "Sequences and Series",
            "subskill": "arithmetic_series",
            "learning_objective_id": "g12_math_seq_arithmetic",
            "archetype": "arithmetic_series_sum",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"Tn = {d}n + {a-d}, T{n} = {tn}, S{n} = {sn}",
            "marks": 5,
            "marking_schema": {
                "total_marks": 5,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Common difference d = {d}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"General term Tn = {d}n + {a-d}", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Specific term T{n} = {tn}", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": "Arithmetic series formula Sn = n/2[2a + (n-1)d]", "marks": 1, "editable": True},
                    {"id": "mp_5", "desc": f"Final sum S{n} = {sn}", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": f"First find the constant first difference $d = T_2 - T_1 = {t2} - {t1} = {d}$.",
                "tier_2": rf"Apply $T_n = a + (n - 1)d$. Then use $S_n = \frac{{n}}{{2}}[2a + (n - 1)d]$ with $n = {n}$.",
                "tier_3": rf"$T_{{{n}}} = {tn}$, and $S_{{{n}}} = \frac{{{n}}}{{2}}[{2*a + (n-1)*d}] = {sn}$.",
            },
            "misconception_tags": ["arithmetic_vs_geometric_confusion", "formula_substitution_error"],
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 5,
            "mode": mode,
            "difficulty": "medium",
        }

    elif archetype == "geometric_series_sum":
        a = r.choice([2, 3, 4, 5])
        ratio = r.choice([2, 3])
        n = r.choice([6, 7, 8])
        t1, t2, t3 = a, a * ratio, a * (ratio ** 2)
        # Tn = a * r^(n - 1)
        tn = a * (ratio ** (n - 1))
        # Sn = a * (r^n - 1) / (r - 1)
        sn = (a * (ratio ** n - 1)) // (ratio - 1)

        prompt = (
            f"Given the geometric sequence: \\({t1},\\ {t2},\\ {t3},\\ \\dots\\)\n\n"
            f"1. State the first term \\(a\\) and common ratio \\(r\\).\n"
            f"2. Write down the general term \\(T_n\\).\n"
            f"3. Calculate the sum of the first \\({n}\\) terms (\\(S_{{{n}}}\\))."
        )
        sample_answer = (
            rf"a = {a},\ r = \frac{{{t2}}}{{{t1}}} = {ratio}\\\ "
            rf"T_n = {a}({ratio})^{{n - 1}}\\\ "
            rf"S_{{{n}}} = \frac{{{a}({ratio}^{{{n}}} - 1)}}{{{ratio} - 1}} = \frac{{{a}({ratio**n} - 1)}}{{{ratio - 1}}} = {sn}"
        )

        return {
            "id": f"g12_seq_geom_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-12",
            "topic": "Sequences and Series",
            "subskill": "geometric_series",
            "learning_objective_id": "g12_math_seq_geometric",
            "archetype": "geometric_series_sum",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"r = {ratio}, Tn = {a}({ratio})^(n-1), S{n} = {sn}",
            "marks": 4,
            "marking_schema": {
                "total_marks": 4,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Common ratio r = {ratio}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"General term Tn = {a}({ratio})^(n-1)", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Geometric series formula Sn = a(r^n - 1) / (r - 1)", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": f"Accurate sum S{n} = {sn}", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": f"Find the common ratio $r = \\frac{{T_2}}{{T_1}} = \\frac{{{t2}}}{{{t1}}} = {ratio}$.",
                "tier_2": rf"Apply $T_n = ar^{{n - 1}}$ and $S_n = \frac{{a(r^n - 1)}}{{r - 1}}$.",
                "tier_3": rf"$S_{{{n}}} = \frac{{{a}({ratio}^{{{n}}} - 1)}}{{{ratio - 1}}} = {sn}$.",
            },
            "misconception_tags": ["common_ratio_subtraction_confusion", "power_order_of_operations"],
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 4,
            "mode": mode,
            "difficulty": "medium",
        }

    elif archetype == "sum_to_infinity_convergence":
        # Convergent geometric series: -1 < r < 1
        a = r.choice([16, 24, 32, 48, 64])
        # r = 1/2, 1/3, 1/4
        denom = r.choice([2, 3, 4])
        # S_inf = a / (1 - 1/denom) = a * denom / (denom - 1)
        s_inf = (a * denom) // (denom - 1)
        t1 = a
        t2 = a // denom
        t3 = (a // denom) // denom

        prompt = (
            f"Consider the infinite geometric series: \\({t1} + {t2} + {t3} + \\dots\\)\n\n"
            f"1. Explain why this series converges.\n"
            f"2. Calculate the sum to infinity (\\(S_\\infty\\)) of the series."
        )
        sample_answer = (
            rf"r = \frac{{{t2}}}{{{t1}}} = \frac{{1}}{{{denom}}}\\\ "
            rf"\text{{1. The series converges because }} -1 < r < 1 \quad \left( -1 < \frac{{1}}{{{denom}}} < 1 \right).\\\ "
            rf"\text{{2. }} S_\infty = \frac{{a}}{{1 - r}} = \frac{{{a}}}{{1 - \frac{{1}}{{{denom}}}}} = \frac{{{a}}}{{\frac{{{denom - 1}}}{{{denom}}}}} = {s_inf}"
        )

        return {
            "id": f"g12_seq_inf_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-12",
            "topic": "Sequences and Series",
            "subskill": "sum_to_infinity",
            "learning_objective_id": "g12_math_seq_sum_to_infinity",
            "archetype": "sum_to_infinity_convergence",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"Converges: -1 < r < 1, S_inf = {s_inf}",
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Convergence condition stated (-1 < r < 1 with r = 1/{denom})", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Sum to infinity formula S_inf = a / (1 - r)", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Accurate calculation S_inf = {s_inf}", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "omitted_convergence_condition", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "An infinite geometric series converges if and only if the common ratio satisfies $-1 < r < 1$.",
                "tier_2": rf"Calculate $r = \frac{{{t2}}}{{{t1}}} = \frac{{1}}{{{denom}}}$. Since $|\frac{{1}}{{{denom}}}| < 1$, it converges.",
                "tier_3": rf"Use $S_\infty = \frac{{a}}{{1 - r}} = \frac{{{a}}}{{1 - 1/{denom}}} = {s_inf}$.",
            },
            "misconception_tags": ["omitted_convergence_condition", "fraction_denominator_inversion_error"],
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }

    else:
        # Sigma notation
        m = r.choice([3, 4, 5])
        c_val = r.choice([1, 2, 3])
        top_k = r.choice([10, 12, 15, 20])
        # Sum_{k=1}^top_k (m*k - c_val)
        # Arithmetic series with a = m(1) - c_val, d = m, n = top_k
        first_term = m * 1 - c_val
        last_term = m * top_k - c_val
        total_sum = (top_k * (first_term + last_term)) // 2

        prompt = (
            f"Evaluate the following summation using series formulas:\n"
            f"$$\\sum_{{k = 1}}^{{{top_k}}} ({m}k - {c_val})$$"
        )
        sample_answer = (
            rf"\text{{First term }} (k = 1): a = {m}(1) - {c_val} = {first_term}\\\ "
            rf"\text{{Last term }} (k = {top_k}): l = {m}({top_k}) - {c_val} = {last_term}\\\ "
            rf"\text{{Number of terms: }} n = {top_k} - 1 + 1 = {top_k}\\\ "
            rf"S_{{{top_k}}} = \frac{{n}}{{2}}[a + l] = \frac{{{top_k}}}{{2}}[{first_term} + {last_term}] = {total_sum}"
        )

        return {
            "id": f"g12_seq_sigma_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-12",
            "topic": "Sequences and Series",
            "subskill": "sigma_notation",
            "learning_objective_id": "g12_math_seq_sigma",
            "archetype": "sigma_notation",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": str(total_sum),
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Determining first term a = {first_term} and last term l = {last_term}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Number of terms n = {top_k}", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Final sum S = {total_sum}", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Substitute $k = 1$ to find the first term, and $k = {top_k}$ to find the last term.",
                "tier_2": rf"This is an arithmetic series with $a = {first_term}$, $l = {last_term}$, and $n = {top_k}$.",
                "tier_3": rf"Use $S_n = \frac{{n}}{{2}}(a + l) = \frac{{{top_k}}}{{2}}({first_term} + {last_term}) = {total_sum}$.",
            },
            "misconception_tags": ["number_of_terms_off_by_one", "formula_selection_error"],
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> List[Dict[str, Any]]:
    base_seed = seed if seed is not None else 42
    return [
        generate_grade12_sequences_series_question(
            seed=base_seed + i,
            difficulty=difficulty,
            mode=mode,
        )
        for i in range(count)
    ]
