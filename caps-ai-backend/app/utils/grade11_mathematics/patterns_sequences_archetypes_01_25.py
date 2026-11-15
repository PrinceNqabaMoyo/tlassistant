"""Grade 11 Mathematics — Number Patterns Archetypes 01–25.
100% Aligned with South African National Curriculum Standards (Grade 11 Term 1).
Grounded in curriculum_docs_auto/Mathematics_Gr11/Term 1/03. Number patterns.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade11_mathematics._math_common import (
    make_math_question,
    num,
    solution_graph,
    step,
)

TOPIC = "Number patterns"
LO_PREFIX = "math11_patterns"


def _svg_spec(svg: str) -> Dict[str, Any]:
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _fmt_linear(d: int, c: int, var: str = "n") -> str:
    if c == 0:
        return f"{d}{var}"
    if c > 0:
        return f"{d}{var} + {c}"
    return f"{d}{var} - {abs(c)}"


def _fmt_quad(a: int, b: int, c: int, var: str = "n") -> str:
    if a == 1:
        lead = f"{var}^2"
    elif a == -1:
        lead = f"-{var}^2"
    else:
        lead = f"{a}{var}^2"
    parts = [lead]
    if b != 0:
        if abs(b) == 1:
            parts.append(f"+ {var}" if b > 0 else f"- {var}")
        else:
            parts.append(f"+ {b}{var}" if b > 0 else f"- {abs(b)}{var}")
    if c != 0:
        parts.append(f"+ {c}" if c > 0 else f"- {abs(c)}")
    return " ".join(parts)


def _q(
    subskill: str,
    idx: int,
    prompt: str,
    ans_latex: str,
    steps_list: List[Dict[str, Any]],
    nudge: str,
    concept: str,
    breakdown: str,
    tags: List[str],
    difficulty: str = "medium",
    marks: int = 3,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    sol = solution_graph(
        goal=f"Solve {subskill}",
        chain_type="expression",
        var="n",
        steps=steps_list,
        final_latex=ans_latex,
    )
    marking = {
        "total_marks": marks,
        "marking_points": [
            {"id": f"mp_{i+1}", "desc": st.get("op", f"Step {i+1}"), "marks": 1, "editable": True}
            for i, st in enumerate(steps_list[:marks])
        ] or [{"id": "mp_1", "desc": "Correct answer", "marks": marks, "editable": True}],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    return make_math_question(
        prefix=f"g11_pat_{idx:02d}",
        topic=TOPIC,
        subskill=subskill,
        learning_objective_id=f"{LO_PREFIX}_{idx:02d}",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema=marking,
        hints={"nudge": nudge, "concept": concept, "breakdown": breakdown},
        misconception_tags=tags,
        term=1,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        difficulty=difficulty,
        diagram_spec=diagram_spec,
    )


# 01. Linear sequence common difference and next three terms
def build_01_linear_sequence_common_difference_and_next_terms(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(-25, 35)
    d = r.choice([-9, -7, -6, -5, -4, 3, 4, 6, 7, 8, 9, 11])
    terms = [a1 + i * d for i in range(7)]
    shown = "; ".join(str(t) for t in terms[:4])
    nxt = "; ".join(str(t) for t in terms[4:])
    ans = f"d = {d}; \\quad \\text{{next terms: }} {nxt}"
    prompt = f"Consider the linear sequence: ${shown}; ...$\n\nDetermine the common difference $d$ and write down the next three terms."
    steps = [
        step(from_latex=f"T_1 = {terms[0]},\\; T_2 = {terms[1]}", to_latex_str=f"d = T_2 - T_1 = {terms[1]} - ({terms[0]}) = {d}", op="Calculate common difference d = T2 - T1", rule="Arithmetic common difference"),
        step(from_latex=f"T_4 = {terms[3]}", to_latex_str=ans, op="Add d repeatedly to find T5, T6, and T7", rule="Recursive linear progression"),
    ]
    return _q("01_linear_sequence_common_difference_and_next_terms", 1, prompt, ans, steps,
              "Subtract T1 from T2 to get the constant difference d.",
              "In a linear sequence, d = T2 - T1 = T3 - T2.",
              f"d = {d}, so the next three terms are {nxt}.",
              ["subtracted_t1_minus_t2_sign_inversion"], "easy", 2)


# 02. Linear sequence general term formula
def build_02_linear_sequence_general_term_formula(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(-20, 30)
    d = r.choice([-8, -6, -5, -3, 3, 4, 5, 7, 9])
    terms = [a1 + i * d for i in range(4)]
    c = a1 - d
    tn_str = _fmt_linear(d, c)
    ans = f"T_n = {tn_str}"
    prompt = f"Given the linear number pattern: ${terms[0]}; {terms[1]}; {terms[2]}; {terms[3]}; ...$\n\nDetermine an expression for the general term $T_n$ in the form $T_n = dn + c$."
    steps = [
        step(from_latex=f"T_2 - T_1 = {terms[1]} - ({terms[0]})", to_latex_str=f"d = {d}", op="Find common difference d", rule="d = T2 - T1"),
        step(from_latex=f"T_n = {terms[0]} + (n - 1)({d})", to_latex_str=ans, op="Substitute into T_n = a + (n - 1)d and simplify", rule="Linear general term formula"),
    ]
    return _q("02_linear_sequence_general_term_formula", 2, prompt, ans, steps,
              "First calculate d = T2 - T1, then use T_n = T1 + (n - 1)d.",
              "For any linear sequence, T_n = dn + c where d is the common difference and c = T1 - d.",
              f"d = {d} and c = {terms[0]} - ({d}) = {c}, so {ans}.",
              ["used_t1_as_constant_c_without_subtracting_d"], "easy", 3)


# 03. Linear sequence calculate specific high-index term
def build_03_linear_sequence_calculate_specific_term(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(-15, 25)
    d = r.choice([-7, -5, -4, 4, 6, 8, 11])
    k = r.randint(18, 45)
    terms = [a1 + i * d for i in range(4)]
    c = a1 - d
    tk = d * k + c
    ans = f"T_{{{k}}} = {tk}"
    prompt = f"Consider the linear sequence: ${terms[0]}; {terms[1]}; {terms[2]}; {terms[3]}; ...$\n\nDetermine the value of the ${k}^{{\\text{{th}}}}$ term ($T_{{{k}}}$)."
    steps = [
        step(from_latex=f"a = {a1},\\; d = {d}", to_latex_str=f"T_n = {_fmt_linear(d, c)}", op="Find general term T_n", rule="T_n = a + (n - 1)d"),
        step(from_latex=f"n = {k}", to_latex_str=f"T_{{{k}}} = {d}({k}) + ({c}) = {tk}", op=f"Substitute n = {k}", rule="Direct evaluation"),
    ]
    return _q("03_linear_sequence_calculate_specific_term", 3, prompt, ans, steps,
              f"Find the formula T_n first, then substitute n = {k}.",
              "T_n = a + (n - 1)d.",
              f"T_{k} = {a1} + ({k} - 1)({d}) = {tk}.",
              ["substituted_n_instead_of_n_minus_1"], "easy", 3)


# 04. Linear sequence solve for term position n
def build_04_linear_sequence_solve_for_term_position_n(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(-30, 20)
    d = r.choice([-9, -7, -6, 5, 6, 8, 10, 12])
    n_val = r.randint(14, 38)
    c = a1 - d
    target = d * n_val + c
    terms = [a1 + i * d for i in range(4)]
    ans = f"n = {n_val}"
    prompt = f"Given the linear sequence: ${terms[0]}; {terms[1]}; {terms[2]}; {terms[3]}; ...$\n\nDetermine the value of $n$ for which $T_n = {target}$."
    steps = [
        step(from_latex=f"a = {a1},\\; d = {d}", to_latex_str=f"T_n = {_fmt_linear(d, c)}", op="Derive general term T_n", rule="Linear formula"),
        step(from_latex=f"{_fmt_linear(d, c)} = {target}", to_latex_str=f"{d}n = {target - c} \\implies n = {n_val}", op="Equate T_n to target value and solve for n", rule="Linear equation"),
    ]
    return _q("04_linear_sequence_solve_for_term_position_n", 4, prompt, ans, steps,
              f"Set T_n = {target} and solve the linear equation for n.",
              "n represents the position of the term, whereas T_n is the value of the term.",
              f"{d}n + ({c}) = {target} gives {d}n = {target - c}, so n = {n_val}.",
              ["substituted_target_value_into_n_instead_of_tn"], "easy", 3)


# 05. Linear sequence number of terms in finite list
def build_05_linear_sequence_number_of_terms_in_finite_list(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(-20, 40)
    d = r.choice([-8, -6, -4, 4, 6, 7, 9])
    n_tot = r.randint(15, 42)
    last_term = a1 + (n_tot - 1) * d
    terms = [a1 + i * d for i in range(3)]
    ans = f"n = {n_tot}"
    prompt = f"A finite linear sequence is given by: ${terms[0]}; {terms[1]}; {terms[2]}; ... ; {last_term}$.\n\nDetermine how many terms are in this sequence."
    steps = [
        step(from_latex=f"T_1 = {a1},\\; d = {d}", to_latex_str=f"T_n = {_fmt_linear(d, a1 - d)}", op="Determine general formula", rule="T_n = a + (n - 1)d"),
        step(from_latex=f"{_fmt_linear(d, a1 - d)} = {last_term}", to_latex_str=ans, op="Set T_n equal to the last term and solve for n", rule="Finite sequence term count"),
    ]
    return _q("05_linear_sequence_number_of_terms_in_finite_list", 5, prompt, ans, steps,
              f"The last term {last_term} is T_n. Solve for n.",
              "Use T_n = a + (n - 1)d = last term.",
              f"{a1} + (n - 1)({d}) = {last_term} leads to n - 1 = {n_tot - 1}, so n = {n_tot}.",
              ["forgot_plus_one_when_dividing_range_by_d"], "easy", 3)


# 06. Linear sequence unknown variable in consecutive terms
def build_06_linear_sequence_unknown_variable_consecutive_terms(r: random.Random) -> Dict[str, Any]:
    k_val = r.choice([-5, -4, -3, -2, 2, 3, 4, 5, 6, 7])
    c1 = r.randint(-8, 8)
    c2 = r.randint(-8, 8)
    # Let T1 = k + c1, T2 = 3k + c2, and we want T2 - T1 = T3 - T2
    # Let T3 have coefficient 6k + c3 so (3k + c2) - (k + c1) = (6k + c3) - (3k + c2)
    # 2k + (c2 - c1) = 3k + (c3 - c2) => k = 2*c2 - c1 - c3 => c3 = 2*c2 - c1 - k_val
    c3 = 2 * c2 - c1 - k_val
    t1_str = _fmt_linear(1, c1, "k")
    t2_str = _fmt_linear(3, c2, "k")
    t3_str = _fmt_linear(6, c3, "k")
    t1_num = k_val + c1
    t2_num = 3 * k_val + c2
    t3_num = 6 * k_val + c3
    ans = f"k = {k_val}; \\quad T_1 = {t1_num},\\; T_2 = {t2_num},\\; T_3 = {t3_num}"
    prompt = f"The first three terms of a linear number pattern are:\n\n$${t1_str}; \\quad {t2_str}; \\quad {t3_str}$$\n\nCalculate the value of $k$ and hence write down the numeric values of the first three terms."
    steps = [
        step(from_latex="T_2 - T_1 = T_3 - T_2", to_latex_str=f"({t2_str}) - ({t1_str}) = ({t3_str}) - ({t2_str})", op="Equate consecutive first differences", rule="Constant first difference in linear sequence"),
        step(from_latex=f"2k + ({c2 - c1}) = 3k + ({c3 - c2})", to_latex_str=ans, op="Solve for k and substitute into T1, T2, T3", rule="Linear equation solution"),
    ]
    return _q("06_linear_sequence_unknown_variable_consecutive_terms", 6, prompt, ans, steps,
              "In a linear sequence, the difference between consecutive terms is constant: T2 - T1 = T3 - T2.",
              "Set (second term) - (first term) = (third term) - (second term) and solve for k.",
              f"2k + ({c2 - c1}) = 3k + ({c3 - c2}) gives k = {k_val}. Substituting gives {t1_num}; {t2_num}; {t3_num}.",
              ["sign_error_distributing_minus_over_brackets"], "medium", 4)


# 07. Linear sequence with fractional algebraic expressions
def build_07_linear_sequence_fractional_algebraic_unknown(r: random.Random) -> Dict[str, Any]:
    y_val = r.choice([-6, -4, -2, 2, 4, 6, 8])
    a_num = r.choice([1, 3, 5])
    b_num = r.choice([3, 5, 7])
    # T1 = y - a_num/2, T2 = 2y + b_num/2, T3 = 4y + c_num/2
    # T2 - T1 = y + (a_num + b_num)/2
    # T3 - T2 = 2y + (c_num - b_num)/2
    # Equal when y = (a_num + 2*b_num - c_num)/2 => c_num = a_num + 2*b_num - 2*y_val
    c_num = a_num + 2 * b_num - 2 * y_val
    ans = f"y = {y_val}"
    prompt = (
        f"Given the linear sequence:\n\n"
        f"$$y - \\frac{{{a_num}}}{{2}}; \\quad 2y + \\frac{{{b_num}}}{{2}}; \\quad 4y + \\frac{{{c_num}}}{{2}}; \\quad ...$$\n\n"
        f"Determine the value of $y$."
    )
    steps = [
        step(from_latex="T_2 - T_1 = T_3 - T_2", to_latex_str=f"\\left(2y + \\frac{{{b_num}}}{{2}}\\right) - \\left(y - \\frac{{{a_num}}}{{2}}\\right) = \\left(4y + \\frac{{{c_num}}}{{2}}\\right) - \\left(2y + \\frac{{{b_num}}}{{2}}\\right)", op="Equate consecutive differences", rule="Constant common difference"),
        step(from_latex=f"2y + {b_num + a_num} = 4y + {c_num - b_num}", to_latex_str=ans, op="Multiply through by 2 to clear fractions and solve for y", rule="Clearing LCD in linear equation"),
    ]
    return _q("07_linear_sequence_fractional_algebraic_unknown", 7, prompt, ans, steps,
              "Set T2 - T1 = T3 - T2 and multiply the entire equation by 2 to clear the denominators.",
              "A sequence is linear if and only if T2 - T1 = T3 - T2.",
              f"y + {(a_num + b_num)}/2 = 2y + {(c_num - b_num)}/2, so y = {y_val}.",
              ["fraction_subtraction_sign_error"], "medium", 4)


# 08. Linear sequence with South African comma decimals
def build_08_linear_sequence_decimal_common_difference(r: random.Random) -> Dict[str, Any]:
    a1_tenths = r.randint(-150, 250)
    d_tenths = r.choice([-45, -35, -25, -18, 15, 24, 35, 42])
    terms_str = [num(round((a1_tenths + i * d_tenths) / 10, 1), 1) for i in range(6)]
    d_str = num(round(d_tenths / 10, 1), 1)
    ans = f"d = {d_str}; \\quad T_5 = {terms_str[4]}; \\quad T_6 = {terms_str[5]}"
    prompt = f"Consider the decimal number pattern: ${terms_str[0]};\\; {terms_str[1]};\\; {terms_str[2]};\\; {terms_str[3]};\\; ...$\n\nCalculate the common difference $d$ and write down the next two terms."
    steps = [
        step(from_latex=f"d = T_2 - T_1 = {terms_str[1]} - ({terms_str[0]})", to_latex_str=f"d = {d_str}", op="Subtract T1 from T2", rule="Decimal common difference"),
        step(from_latex=f"T_4 = {terms_str[3]}", to_latex_str=ans, op="Add d to find T5 and T6", rule="Sequential addition"),
    ]
    return _q("08_linear_sequence_decimal_common_difference", 8, prompt, ans, steps,
              "Calculate T2 - T1 carefully with the signs.",
              "d = T2 - T1 = T3 - T2.",
              f"d = {d_str}, T5 = {terms_str[4]}, T6 = {terms_str[5]}.",
              ["decimal_place_alignment_error"], "easy", 3)


# 09. Linear sequence from two non-consecutive terms
def build_09_linear_sequence_from_two_non_consecutive_terms(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(-20, 25)
    d = r.choice([-7, -5, -4, 3, 5, 6, 8])
    p = r.randint(3, 6)
    q_idx = p + r.randint(4, 8)
    tp = a1 + (p - 1) * d
    tq = a1 + (q_idx - 1) * d
    c = a1 - d
    ans = f"d = {d}, \\quad T_n = {_fmt_linear(d, c)}"
    prompt = f"In a linear number pattern, the ${p}^{{\\text{{th}}}}$ term is ${tp}$ ($T_{{{p}}} = {tp}$) and the ${q_idx}^{{\\text{{th}}}}$ term is ${tq}$ ($T_{{{q_idx}}} = {tq}$).\n\nDetermine the common difference $d$ and the general term $T_n$."
    steps = [
        step(from_latex=f"T_{{{q_idx}}} - T_{{{p}}} = ({q_idx} - {p})d", to_latex_str=f"{tq} - ({tp}) = {q_idx - p}d \\implies d = {d}", op="Use difference of positions to find d", rule="d = (T_q - T_p) / (q - p)"),
        step(from_latex=f"T_{{{p}}} = {d}({p}) + c = {tp}", to_latex_str=ans, op="Solve for c and state T_n", rule="T_n = dn + c"),
    ]
    return _q("09_linear_sequence_from_two_non_consecutive_terms", 9, prompt, ans, steps,
              f"Notice that moving from T_{p} to T_{q_idx} adds d exactly {q_idx - p} times.",
              "T_q - T_p = (q - p)d.",
              f"({tq} - ({tp})) / ({q_idx} - {p}) = {d}. Then T_n = {_fmt_linear(d, c)}.",
              ["divided_by_wrong_index_gap"], "medium", 4)


# 10. Linear modelling: study tables and chairs with seeded SVG
def build_10_linear_modelling_study_tables_and_chairs(r: random.Random) -> Dict[str, Any]:
    per_table_add = r.choice([2, 4])
    ends = 2
    # T_n = per_table_add * n + ends
    n_ask = r.randint(11, 24)
    t_ask = per_table_add * n_ask + ends
    t1 = per_table_add + ends
    t2 = 2 * per_table_add + ends
    t3 = 3 * per_table_add + ends
    w_box = 42 + (n_ask % 11)
    svg = (
        f'<svg viewBox="0 0 460 150" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="460" height="150" fill="#f8fafc" rx="8"/>'
        f'<rect x="45" y="50" width="{w_box}" height="42" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="{45 + w_box//2}" y="118" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">n=1 ({t1} seats)</text>'
        f'<rect x="165" y="50" width="{w_box}" height="42" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<rect x="{165+w_box}" y="50" width="{w_box}" height="42" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="{165 + w_box}" y="118" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">n=2 ({t2} seats)</text>'
        f'<rect x="305" y="50" width="{w_box}" height="42" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<rect x="{305+w_box}" y="50" width="{w_box}" height="42" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<rect x="{305+2*w_box}" y="50" width="{w_box}" height="42" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="{305 + int(1.5*w_box)}" y="118" font-size="11" font-family="sans-serif" fill="#1e293b" text-anchor="middle">n=3 ({t3} seats)</text>'
        f'</svg>'
    )
    ans = f"T_n = {per_table_add}n + {ends}; \\quad T_{{{n_ask}}} = {t_ask}"
    prompt = (
        f"Refer to the diagram of rectangular study tables placed end-to-end in a single row. "
        f"One table seats ${t1}$ learners, two joined tables seat ${t2}$ learners, and three joined tables seat ${t3}$ learners.\n\n"
        f"Determine the general formula $T_n$ for $n$ tables and calculate how many learners can sit around ${n_ask}$ tables."
    )
    steps = [
        step(from_latex=f"{t1};\\; {t2};\\; {t3};\\; ...", to_latex_str=f"T_n = {per_table_add}n + {ends}", op="Identify linear sequence with d and c", rule="Linear table pattern"),
        step(from_latex=f"n = {n_ask}", to_latex_str=f"T_{{{n_ask}}} = {per_table_add}({n_ask}) + {ends} = {t_ask}", op=f"Substitute n = {n_ask}", rule="Direct substitution"),
    ]
    return _q("10_linear_modelling_study_tables_and_chairs", 10, prompt, ans, steps,
              f"Each added table contributes {per_table_add} additional seats, while the {ends} end seats stay fixed.",
              "T_n = dn + c.",
              f"T_n = {per_table_add}n + {ends}, so T_{n_ask} = {t_ask} learners.",
              ["multiplied_t1_by_n_ignoring_shared_table_sides"], "easy", 3, _svg_spec(svg))


# 11. Linear modelling: data plan cost threshold
def build_11_linear_modelling_data_plan_cost_threshold(r: random.Random) -> Dict[str, Any]:
    base_cost = r.choice([95, 110, 120, 135, 150])
    step_cost = r.choice([12, 15, 18, 20, 25])
    n_thresh = r.randint(18, 32)
    unlimited_cost = base_cost + step_cost * (n_thresh - 1)
    t2 = base_cost + step_cost
    t3 = base_cost + 2 * step_cost
    c = base_cost - step_cost
    ans = f"T_n = {_fmt_linear(step_cost, c)}; \\quad n = {n_thresh}\\text{{ GB}}"
    prompt = (
        f"A mobile service provider charges $\\text{{R }}{base_cost}$ for $1\\text{{ GB}}$ of data, "
        f"$\\text{{R }}{t2}$ for $2\\text{{ GB}}$, and $\\text{{R }}{t3}$ for $3\\text{{ GB}}$.\n\n"
        f"1. Write down a formula $T_n$ for the cost (in Rands) of $n\\text{{ GB}}$ of data.\n"
        f"2. An unlimited package costs $\\text{{R }}{unlimited_cost}$. For what number of gigabytes $n$ does the capped data package equal $\\text{{R }}{unlimited_cost}$?"
    )
    steps = [
        step(from_latex=f"T_1 = {base_cost},\\; d = {step_cost}", to_latex_str=f"T_n = {base_cost} + {step_cost}(n - 1) = {_fmt_linear(step_cost, c)}", op="Formulate linear cost formula", rule="T_n = a + (n - 1)d"),
        step(from_latex=f"{_fmt_linear(step_cost, c)} = {unlimited_cost}", to_latex_str=f"{step_cost}n = {unlimited_cost - c} \\implies n = {n_thresh}", op="Equate cost to unlimited package price and solve for n", rule="Threshold equation"),
    ]
    return _q("11_linear_modelling_data_plan_cost_threshold", 11, prompt, ans, steps,
              f"First find d = {t2} - {base_cost} = {step_cost}, then solve T_n = {unlimited_cost}.",
              "Cost for n GB follows an arithmetic sequence with T1 = cost of 1 GB.",
              f"T_n = {_fmt_linear(step_cost, c)}. Setting T_n = {unlimited_cost} gives n = {n_thresh} GB.",
              ["used_n_instead_of_n_minus_1_for_additional_gb"], "medium", 4)


# 12. Linear modelling: matchstick polygon row with seeded SVG
def build_12_linear_modelling_matchstick_row_squares(r: random.Random) -> Dict[str, Any]:
    d = r.choice([3, 4, 5])
    shape_name = {3: "squares", 4: "pentagons", 5: "hexagons"}[d]
    t1 = d + 1
    t2 = 2 * d + 1
    t3 = 3 * d + 1
    n_ask = r.randint(16, 35)
    t_ask = d * n_ask + 1
    sz = 30 + (n_ask % 9)
    svg = (
        f'<svg viewBox="0 0 420 130" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="420" height="130" fill="#fffbeb" rx="8"/>'
        f'<rect x="40" y="35" width="{sz}" height="{sz}" fill="none" stroke="#b45309" stroke-width="3"/>'
        f'<text x="{40+sz//2}" y="98" font-size="11" font-family="sans-serif" fill="#78350f" text-anchor="middle">Stage 1: {t1}</text>'
        f'<rect x="145" y="35" width="{sz}" height="{sz}" fill="none" stroke="#b45309" stroke-width="3"/>'
        f'<rect x="{145+sz}" y="35" width="{sz}" height="{sz}" fill="none" stroke="#b45309" stroke-width="3"/>'
        f'<text x="{145+sz}" y="98" font-size="11" font-family="sans-serif" fill="#78350f" text-anchor="middle">Stage 2: {t2}</text>'
        f'<rect x="265" y="35" width="{sz}" height="{sz}" fill="none" stroke="#b45309" stroke-width="3"/>'
        f'<rect x="{265+sz}" y="35" width="{sz}" height="{sz}" fill="none" stroke="#b45309" stroke-width="3"/>'
        f'<rect x="{265+2*sz}" y="35" width="{sz}" height="{sz}" fill="none" stroke="#b45309" stroke-width="3"/>'
        f'<text x="{265+int(1.5*sz)}" y="98" font-size="11" font-family="sans-serif" fill="#78350f" text-anchor="middle">Stage 3: {t3}</text>'
        f'</svg>'
    )
    ans = f"T_n = {d}n + 1; \\quad T_{{{n_ask}}} = {t_ask}"
    prompt = (
        f"Refer to the matchstick pattern where connected {shape_name} are built in a row. "
        f"Stage 1 uses ${t1}$ matchsticks, Stage 2 uses ${t2}$ matchsticks, and Stage 3 uses ${t3}$ matchsticks.\n\n"
        f"Determine the general formula $T_n$ and calculate the number of matchsticks required for Stage ${n_ask}$."
    )
    steps = [
        step(from_latex=f"T_1 = {t1},\\; d = {d}", to_latex_str=f"T_n = {d}n + 1", op="Derive linear formula for connected matchstick shapes", rule="T_n = dn + c"),
        step(from_latex=f"n = {n_ask}", to_latex_str=f"T_{{{n_ask}}} = {d}({n_ask}) + 1 = {t_ask}", op=f"Calculate T_{n_ask}", rule="Direct substitution"),
    ]
    return _q("12_linear_modelling_matchstick_row_squares", 12, prompt, ans, steps,
              f"Each new shape shares 1 matchstick with the previous shape, so {d} matchsticks are added per stage.",
              "Sequence is arithmetic with first term d + 1 and common difference d.",
              f"T_n = {d}n + 1 and T_{n_ask} = {t_ask}.",
              ["counted_shared_interior_matchstick_twice"], "easy", 3, _svg_spec(svg))


# 13. Cyclic repeating word and letter pattern
def build_13_cyclic_repeating_word_and_letter_pattern(r: random.Random) -> Dict[str, Any]:
    word = r.choice(["PATTERN", "ALGEBRA", "NUMBERS", "SEQUENCE", "FUNCTION", "CALCULUS"])
    k = len(word)
    q_mult = r.randint(40, 120)
    rem = r.randint(1, k - 1)
    pos = q_mult * k + rem
    letter = word[rem - 1]
    ans = f"\\text{{Remainder }} = {rem} \\implies \\text{{Letter }} \\mathbf{{{letter}}}"
    prompt = (
        f"Consider the infinitely repeating letter sequence formed by repeating the word $\\text{{{word}}}$:\n\n"
        f"$$\\text{{{word}{word}{word}}}...$$\n\n"
        f"Determine the ${pos}^{{\\text{{th}}}}$ letter in the sequence."
    )
    steps = [
        step(from_latex=f"\\text{{Cycle length }} = {k}", to_latex_str=f"{pos} \\div {k} = {q_mult} \\text{{ remainder }} {rem}", op=f"Divide position {pos} by cycle length {k}", rule="Modular cycle remainder"),
        step(from_latex=f"\\text{{Remainder }} = {rem}", to_latex_str=ans, op=f"Select the {rem}-th letter of {word}", rule="Cyclic indexing"),
    ]
    return _q("13_cyclic_repeating_word_and_letter_pattern", 13, prompt, ans, steps,
              f"Count the number of letters in {word} ({k}) and find the remainder when {pos} is divided by {k}.",
              "A repeating pattern of period k repeats every k positions; the remainder identifies the position within the cycle.",
              f"{pos} = {k}({q_mult}) + {rem}, so it matches the {rem}-th letter, which is {letter}.",
              ["used_quotient_instead_of_remainder"], "easy", 3)


# 14. Cyclic units digit of a large power
def build_14_cyclic_units_digit_of_large_power(r: random.Random) -> Dict[str, Any]:
    base = r.choice([2, 3, 7, 8])
    cycles = {
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
    }
    cyc = cycles[base]
    q_mult = r.randint(120, 520)
    rem = r.choice([1, 2, 3])
    exp_n = 4 * q_mult + rem
    u_digit = cyc[rem - 1]
    ans = f"\\text{{Units digit}} = {u_digit}"
    prompt = (
        f"By examining the repeating pattern in the units digits of powers of ${base}$ "
        f"(${base}^1, {base}^2, {base}^3, {base}^4, ...$), determine the units digit of ${base}^{{{exp_n}}}$."
    )
    steps = [
        step(from_latex=f"{base}^1, {base}^2, {base}^3, {base}^4", to_latex_str=f"\\text{{Units digit cycle (length 4): }} \\{{{cyc[0]}; {cyc[1]}; {cyc[2]}; {cyc[3]}\\}}", op="List the 4-cycle of units digits", rule="Periodic units digits of powers"),
        step(from_latex=f"{exp_n} \\div 4 = {q_mult} \\text{{ remainder }} {rem}", to_latex_str=ans, op=f"Use remainder {rem} to pick element {rem} of the cycle", rule="Modular exponent cycle"),
    ]
    return _q("14_cyclic_units_digit_of_large_power", 14, prompt, ans, steps,
              f"Write down the units digits of {base}^1, {base}^2, {base}^3, {base}^4 to see the 4-term repeating cycle.",
              "The units digits of powers of 2, 3, 7, and 8 repeat in cycles of 4. Divide the exponent by 4 and use the remainder.",
              f"{exp_n} divided by 4 leaves remainder {rem}, so the units digit is the {rem}-th digit in {cyc}, which is {u_digit}.",
              ["off_by_one_cycle_index_on_remainder"], "medium", 3)


# 15. Quadratic sequence: identify constant second difference
def build_15_quadratic_identify_constant_second_difference(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3, 4, 5])
    b = r.randint(-7, 7)
    c = r.randint(-12, 12)
    terms = [a * n * n + b * n + c for n in range(1, 6)]
    d1 = [terms[i + 1] - terms[i] for i in range(4)]
    d2 = 2 * a
    ans = f"\\text{{First differences: }} {d1[0]}; {d1[1]}; {d1[2]}; {d1[3]}; \\quad \\text{{Second difference}} = {d2}"
    prompt = (
        f"Consider the quadratic number pattern: ${terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]};\\; {terms[4]};\\; ...$\n\n"
        f"Calculate the first differences and determine the constant second difference."
    )
    steps = [
        step(from_latex=f"{terms[0]}; {terms[1]}; {terms[2]}; {terms[3]}; {terms[4]}", to_latex_str=f"\\text{{First differences: }} {d1[0]}; {d1[1]}; {d1[2]}; {d1[3]}", op="Subtract consecutive terms to get first differences", rule="D_n = T_{n+1} - T_n"),
        step(from_latex=f"{d1[1]} - ({d1[0]}) = {d1[2]} - ({d1[1]})", to_latex_str=f"\\text{{Constant second difference}} = {d2}", op="Subtract consecutive first differences", rule="Second difference of quadratic sequence"),
    ]
    return _q("15_quadratic_identify_constant_second_difference", 15, prompt, ans, steps,
              "First subtract consecutive terms (T2 - T1, T3 - T2, ...), then subtract consecutive first differences.",
              "A sequence is quadratic if its second differences are constant.",
              f"First differences: {d1[0]}; {d1[1]}; {d1[2]}; {d1[3]}. Constant second difference = {d2}.",
              ["confused_first_difference_with_second_difference"], "easy", 3)


# 16. Quadratic sequence: extend sequence using differences
def build_16_quadratic_extend_sequence_using_differences(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, -1, 1, 2, 3, 4])
    b = r.randint(-8, 8)
    c = r.randint(-15, 15)
    terms = [a * n * n + b * n + c for n in range(1, 7)]
    d1 = [terms[i + 1] - terms[i] for i in range(5)]
    d2 = 2 * a
    ans = f"T_5 = {terms[4]}; \\quad T_6 = {terms[5]}"
    prompt = (
        f"Given the quadratic number pattern: ${terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]};\\; ...$\n\n"
        f"Write down the next two terms ($T_5$ and $T_6$) of the sequence."
    )
    steps = [
        step(from_latex=f"\\text{{First diffs: }} {d1[0]}; {d1[1]}; {d1[2]}", to_latex_str=f"\\text{{Second diff}} = {d2} \\implies \\text{{next first diffs: }} {d1[3]}; {d1[4]}", op="Extend first differences using constant second difference", rule="Constant second difference"),
        step(from_latex=f"T_4 = {terms[3]}", to_latex_str=f"T_5 = {terms[3]} + ({d1[3]}) = {terms[4]},\\quad T_6 = {terms[4]} + ({d1[4]}) = {terms[5]}", op="Add next first differences to get T5 and T6", rule="Recursive quadratic extension"),
    ]
    return _q("16_quadratic_extend_sequence_using_differences", 16, prompt, ans, steps,
              "Find the constant second difference, use it to find the next first differences, then add them to T4.",
              "T5 = T4 + D4 and T6 = T5 + D5.",
              f"Second difference = {d2}, so D4 = {d1[3]} and D5 = {d1[4]}. Thus T5 = {terms[4]} and T6 = {terms[5]}.",
              ["added_second_difference_directly_to_t4"], "easy", 3)


# 17. Quadratic sequence: find leading coefficient a from second difference
def build_17_quadratic_find_leading_coefficient_a_from_second_diff(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-5, -4, -3, -2, 2, 3, 4, 5, 6])
    b = r.randint(-9, 9)
    c = r.randint(-15, 15)
    terms = [a * n * n + b * n + c for n in range(1, 5)]
    d1 = [terms[i + 1] - terms[i] for i in range(3)]
    d2 = 2 * a
    ans = f"2a = {d2} \\implies a = {a}"
    prompt = (
        f"A quadratic sequence with general term $T_n = an^2 + bn + c$ starts with the terms:\n\n"
        f"$${terms[0]}; \\quad {terms[1]}; \\quad {terms[2]}; \\quad {terms[3]}; \\quad ...$$\n\n"
        f"Determine the constant second difference and hence calculate the value of $a$."
    )
    steps = [
        step(from_latex=f"\\text{{First diffs: }} {d1[0]}; {d1[1]}; {d1[2]}", to_latex_str=f"\\text{{Second difference}} = {d1[1]} - ({d1[0]}) = {d2}", op="Compute second difference", rule="Second difference calculation"),
        step(from_latex=f"2a = {d2}", to_latex_str=f"a = \\frac{{{d2}}}{{2}} = {a}", op="Equate 2a to constant second difference and divide by 2", rule="2a = second difference"),
    ]
    return _q("17_quadratic_find_leading_coefficient_a_from_second_diff", 17, prompt, ans, steps,
              "Remember that the constant second difference of T_n = an^2 + bn + c is equal to 2a, not a.",
              "2a = second difference.",
              f"Second difference = {d2}, so 2a = {d2} and a = {a}.",
              ["equated_a_directly_to_second_difference"], "easy", 3)


# 18. Quadratic sequence: find b and c using 3a + b and a + b + c
def build_18_quadratic_find_b_and_c_using_3a_plus_b_method(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, 1, 2, 3, 4])
    b = r.choice([-9, -7, -5, -3, -1, 1, 3, 5, 7, 9])
    c = r.randint(-14, 14)
    t1 = a + b + c
    t2 = 4 * a + 2 * b + c
    t3 = 9 * a + 3 * b + c
    d1_1 = t2 - t1
    ans = f"b = {b}, \\quad c = {c}"
    prompt = (
        f"A quadratic number pattern $T_n = an^2 + bn + c$ has $a = {a}$ and its first three terms are:\n\n"
        f"$${t1}; \\quad {t2}; \\quad {t3}$$\n\n"
        f"Use the relationships $3a + b = T_2 - T_1$ and $a + b + c = T_1$ to calculate the values of $b$ and $c$."
    )
    steps = [
        step(from_latex=f"3a + b = T_2 - T_1 = {d1_1}", to_latex_str=f"3({a}) + b = {d1_1} \\implies b = {b}", op="Substitute a into 3a + b = T2 - T1 to find b", rule="First difference formula 3a + b = T2 - T1"),
        step(from_latex=f"a + b + c = T_1 = {t1}", to_latex_str=f"({a}) + ({b}) + c = {t1} \\implies c = {c}", op="Substitute a and b into a + b + c = T1 to find c", rule="First term formula T1 = a + b + c"),
    ]
    return _q("18_quadratic_find_b_and_c_using_3a_plus_b_method", 18, prompt, ans, steps,
              f"First calculate T2 - T1 = {d1_1} and set 3({a}) + b = {d1_1}.",
              "For T_n = an^2 + bn + c: T1 = a + b + c and T2 - T1 = 3a + b.",
              f"3({a}) + b = {d1_1} gives b = {b}. Then {a} + ({b}) + c = {t1} gives c = {c}.",
              ["used_2a_plus_b_instead_of_3a_plus_b"], "medium", 3)


# 19. Quadratic general term with positive leading coefficient a > 0
def build_19_quadratic_general_term_positive_leading_a(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3, 4])
    b = r.randint(-8, 8)
    c = r.randint(-12, 12)
    terms = [a * n * n + b * n + c for n in range(1, 5)]
    d1 = [terms[i + 1] - terms[i] for i in range(3)]
    d2 = 2 * a
    tn_str = _fmt_quad(a, b, c)
    ans = f"T_n = {tn_str}"
    prompt = (
        f"Determine the general term $T_n = an^2 + bn + c$ of the quadratic sequence:\n\n"
        f"$${terms[0]}; \\quad {terms[1]}; \\quad {terms[2]}; \\quad {terms[3]}; \\quad ...$$"
    )
    steps = [
        step(from_latex=f"2a = {d2}", to_latex_str=f"a = {a}", op="Use constant second difference to find a", rule="2a = second difference"),
        step(from_latex=f"3({a}) + b = {d1[0]}", to_latex_str=f"b = {b}", op="Use 3a + b = T2 - T1 to find b", rule="First difference relation"),
        step(from_latex=f"{a} + ({b}) + c = {terms[0]}", to_latex_str=ans, op="Use a + b + c = T1 to find c and state T_n", rule="General quadratic term"),
    ]
    return _q("19_quadratic_general_term_positive_leading_a", 19, prompt, ans, steps,
              "Solve in order: 2a = second difference, 3a + b = T2 - T1, and a + b + c = T1.",
              "Every quadratic sequence has T_n = an^2 + bn + c with constant second difference 2a.",
              f"2a = {d2} => a = {a}; 3({a}) + b = {d1[0]} => b = {b}; {a} + ({b}) + c = {terms[0]} => c = {c}. So {ans}.",
              ["algebraic_slip_solving_3a_plus_b_or_a_plus_b_plus_c"], "medium", 4)


# 20. Quadratic general term with negative leading coefficient a < 0
def build_20_quadratic_general_term_negative_leading_a(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-4, -3, -2, -1])
    b = r.randint(-6, 10)
    c = r.randint(-10, 20)
    terms = [a * n * n + b * n + c for n in range(1, 5)]
    d1 = [terms[i + 1] - terms[i] for i in range(3)]
    d2 = 2 * a
    tn_str = _fmt_quad(a, b, c)
    ans = f"T_n = {tn_str}"
    prompt = (
        f"Consider the quadratic sequence: ${terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]};\\; ...$\n\n"
        f"Determine the general term $T_n$ in the form $T_n = an^2 + bn + c$."
    )
    steps = [
        step(from_latex=f"\\text{{First diffs: }} {d1[0]}; {d1[1]}; {d1[2]}", to_latex_str=f"2a = {d2} \\implies a = {a}", op="Find negative second difference and solve for a", rule="2a = second difference"),
        step(from_latex=f"3({a}) + b = {d1[0]}", to_latex_str=f"b = {b}", op="Solve 3a + b = T2 - T1 for b", rule="3a + b = D1"),
        step(from_latex=f"({a}) + ({b}) + c = {terms[0]}", to_latex_str=ans, op="Solve a + b + c = T1 for c", rule="a + b + c = T1"),
    ]
    return _q("20_quadratic_general_term_negative_leading_a", 20, prompt, ans, steps,
              "Watch the negative signs when subtracting decreasing first differences!",
              "When second differences are negative, a < 0.",
              f"Second difference = {d2}, so a = {a}, b = {b}, c = {c}, giving {ans}.",
              ["lost_negative_sign_on_second_difference"], "medium", 4)


# 21. Quadratic general term with fractional leading coefficient (odd second difference)
def build_21_quadratic_general_term_fractional_leading_a(r: random.Random) -> Dict[str, Any]:
    d2 = r.choice([1, 3, 5, -1, -3])
    # Let 2*T_n = d2 * n^2 + b2 * n + c2 with d2 + b2 even so T_n is integer for all n!
    # Wait: n^2 and n have the same parity, so d2*n^2 + b2*n is always even if d2 and b2 have the same parity!
    b2 = r.choice([-7, -5, -3, -1, 1, 3, 5, 7])
    c = r.randint(-10, 12)
    terms = [(d2 * n * n + b2 * n) // 2 + c for n in range(1, 5)]
    d1 = [terms[i + 1] - terms[i] for i in range(3)]
    b_sign = "+" if b2 >= 0 else "-"
    c_part = f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else "")
    ans = f"T_n = \\frac{{{d2}}}{{2}}n^2 {b_sign} \\frac{{{abs(b2)}}}{{2}}n{c_part}"
    prompt = (
        f"Determine the general term $T_n = an^2 + bn + c$ for the quadratic sequence:\n\n"
        f"$${terms[0]}; \\quad {terms[1]}; \\quad {terms[2]}; \\quad {terms[3]}; \\quad ...$$"
    )
    steps = [
        step(from_latex=f"\\text{{First diffs: }} {d1[0]}; {d1[1]}; {d1[2]}", to_latex_str=f"2a = {d2} \\implies a = \\frac{{{d2}}}{{2}}", op="Find odd second difference and fractional a", rule="2a = second difference"),
        step(from_latex=f"3\\left(\\frac{{{d2}}}{{2}}\\right) + b = {d1[0]}", to_latex_str=f"b = \\frac{{{b2}}}{{2}}", op="Solve 3a + b = T2 - T1 for b", rule="Fractional coefficient b"),
        step(from_latex=f"\\frac{{{d2}}}{{2}} + \\frac{{{b2}}}{{2}} + c = {terms[0]}", to_latex_str=ans, op="Solve a + b + c = T1 for c", rule="Fractional quadratic general term"),
    ]
    return _q("21_quadratic_general_term_fractional_leading_a", 21, prompt, ans, steps,
              f"Here the constant second difference is {d2} (odd), so a = {d2}/2.",
              "When the second difference is odd, a and b are halves, while T_n still produces integers.",
              f"a = {d2}/2, b = {b2}/2, c = {c}, giving {ans}.",
              ["rounded_fractional_a_to_integer"], "hard", 4)


# 22. Quadratic sequence: calculate specific term T_k from T_n
def build_22_quadratic_calculate_specific_term_from_tn(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-2, 1, 2, 3])
    b = r.randint(-7, 7)
    c = r.randint(-12, 12)
    k = r.randint(10, 22)
    tk = a * k * k + b * k + c
    tn_str = _fmt_quad(a, b, c)
    ans = f"T_{{{k}}} = {tk}"
    prompt = (
        f"A quadratic number pattern has the general term:\n\n"
        f"$$T_n = {tn_str}$$\n\n"
        f"Calculate the value of the ${k}^{{\\text{{th}}}}$ term ($T_{{{k}}}$)."
    )
    steps = [
        step(from_latex=f"T_n = {tn_str}", to_latex_str=f"T_{{{k}}} = {a}({k})^2 + ({b})({k}) + ({c})", op=f"Substitute n = {k} into T_n", rule="Function evaluation"),
        step(from_latex=f"{a * k * k} + ({b * k}) + ({c})", to_latex_str=ans, op="Simplify numerical expression", rule="Order of operations"),
    ]
    return _q("22_quadratic_calculate_specific_term_from_tn", 22, prompt, ans, steps,
              f"Substitute n = {k} and square {k} before multiplying by {a}.",
              "Evaluate an^2 + bn + c at n = k.",
              f"T_{k} = {a}({k*k}) + ({b})({k}) + ({c}) = {tk}.",
              ["squared_a_times_n_instead_of_n_only"], "easy", 3)


# 23. Quadratic sequence: solve for n given term value V
def build_23_quadratic_solve_for_n_given_term_value(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    b = r.randint(-5, 5)
    c = r.randint(-15, 15)
    n_sol = r.randint(7, 16)
    val = a * n_sol * n_sol + b * n_sol + c
    tn_str = _fmt_quad(a, b, c)
    const_eq = c - val
    ans = f"n = {n_sol}"
    prompt = (
        f"The general term of a quadratic number pattern is given by:\n\n"
        f"$$T_n = {tn_str}$$\n\n"
        f"Determine which term in the sequence has a value of ${val}$."
    )
    steps = [
        step(from_latex=f"{tn_str} = {val}", to_latex_str=f"{_fmt_quad(a, b, const_eq)} = 0", op="Equate T_n to given value and write in standard form", rule="Standard quadratic equation"),
        step(from_latex=f"(n - {n_sol})({a}n + {a * n_sol + b}) = 0", to_latex_str=f"n = {n_sol} \\quad (\\text{{since }} n \\in \\mathbb{{N}})", op="Factorise and select positive integer n", rule="Position n must be a natural number"),
    ]
    return _q("23_quadratic_solve_for_n_given_term_value", 23, prompt, ans, steps,
              f"Set {tn_str} = {val}, bring {val} to the left-hand side, and solve the quadratic equation.",
              "Since n represents a term position, n must be a positive integer (n in N).",
              f"Solving {_fmt_quad(a, b, const_eq)} = 0 gives n = {n_sol} as the valid natural number solution.",
              ["accepted_negative_or_fractional_root_for_n"], "medium", 4)


# 24. Quadratic sequence: test membership of a candidate value
def build_24_quadratic_test_membership_of_candidate_value(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2])
    b = r.randint(-4, 4)
    c = r.randint(-10, 10)
    n_near = r.randint(6, 12)
    is_member = r.choice([True, False])
    if is_member:
        cand = a * n_near * n_near + b * n_near + c
        verdict = f"\\text{{Yes, }} {cand} \\text{{ is the }} {n_near}^{{\\text{{th}}}} \\text{{ term }} (n = {n_near} \\in \\mathbb{{N}})"
    else:
        cand = a * n_near * n_near + b * n_near + c + 1
        verdict = f"\\text{{No, }} {cand} \\text{{ is not a term because }} n \\notin \\mathbb{{N}}"
    tn_str = _fmt_quad(a, b, c)
    prompt = (
        f"A quadratic sequence has the general term $T_n = {tn_str}$.\n\n"
        f"Determine by calculation whether ${cand}$ is a term in this sequence."
    )
    steps = [
        step(from_latex=f"{tn_str} = {cand}", to_latex_str=f"{_fmt_quad(a, b, c - cand)} = 0", op="Set T_n equal to candidate value and rearrange", rule="Membership test equation"),
        step(from_latex="n \\in \\mathbb{N}\\text{ check}", to_latex_str=verdict, op="Test whether a positive integer solution n exists", rule="Term index must be a natural number"),
    ]
    return _q("24_quadratic_test_membership_of_candidate_value", 24, prompt, verdict, steps,
              f"Set {tn_str} = {cand} and check if the equation has a positive whole number solution n.",
              "A number V is a term in the sequence if and only if T_n = V has a solution n in {1, 2, 3, ...}.",
              verdict,
              ["failed_to_check_if_n_is_positive_integer"], "medium", 4)


# 25. Quadratic difference tree diagram analysis with seeded SVG
def build_25_quadratic_difference_tree_diagram_analysis(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3, 4])
    b = r.randint(-5, 6)
    c = r.randint(-8, 10)
    t = [a * n * n + b * n + c for n in range(1, 5)]
    d1 = [t[i + 1] - t[i] for i in range(3)]
    d2 = 2 * a
    tn_str = _fmt_quad(a, b, c)
    x_off = 55 + (abs(c) % 15)
    svg = (
        f'<svg viewBox="0 0 440 175" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="0" width="440" height="175" fill="#f8fafc" rx="8"/>'
        f'<text x="20" y="42" font-size="12" font-family="sans-serif" font-weight="bold" fill="#334155">Terms:</text>'
        f'<text x="{x_off+40}" y="42" font-size="14" font-family="sans-serif" font-weight="bold" fill="#0f172a" text-anchor="middle">{t[0]}</text>'
        f'<text x="{x_off+130}" y="42" font-size="14" font-family="sans-serif" font-weight="bold" fill="#0f172a" text-anchor="middle">{t[1]}</text>'
        f'<text x="{x_off+220}" y="42" font-size="14" font-family="sans-serif" font-weight="bold" fill="#0f172a" text-anchor="middle">{t[2]}</text>'
        f'<text x="{x_off+310}" y="42" font-size="14" font-family="sans-serif" font-weight="bold" fill="#1d4ed8" text-anchor="middle">p</text>'
        f'<line x1="{x_off+50}" y1="50" x2="{x_off+80}" y2="80" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="{x_off+120}" y1="50" x2="{x_off+90}" y2="80" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="{x_off+140}" y1="50" x2="{x_off+170}" y2="80" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="{x_off+210}" y1="50" x2="{x_off+180}" y2="80" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="{x_off+230}" y1="50" x2="{x_off+260}" y2="80" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="{x_off+300}" y1="50" x2="{x_off+270}" y2="80" stroke="#64748b" stroke-width="1.5"/>'
        f'<text x="20" y="98" font-size="12" font-family="sans-serif" font-weight="bold" fill="#334155">1st diff:</text>'
        f'<text x="{x_off+85}" y="98" font-size="13" font-family="sans-serif" fill="#0369a1" text-anchor="middle">{d1[0]}</text>'
        f'<text x="{x_off+175}" y="98" font-size="13" font-family="sans-serif" fill="#0369a1" text-anchor="middle">{d1[1]}</text>'
        f'<text x="{x_off+265}" y="98" font-size="13" font-family="sans-serif" font-weight="bold" fill="#1d4ed8" text-anchor="middle">q</text>'
        f'<text x="20" y="150" font-size="12" font-family="sans-serif" font-weight="bold" fill="#334155">2nd diff:</text>'
        f'<text x="{x_off+130}" y="150" font-size="13" font-family="sans-serif" fill="#15803d" text-anchor="middle">{d2}</text>'
        f'<text x="{x_off+220}" y="150" font-size="13" font-family="sans-serif" fill="#15803d" text-anchor="middle">{d2}</text>'
        f'</svg>'
    )
    ans = f"q = {d1[2]}, \\quad p = {t[3]}, \\quad T_n = {tn_str}"
    prompt = (
        f"Refer to the difference tree diagram for the quadratic sequence starting ${t[0]};\\; {t[1]};\\; {t[2]};\\; p$ "
        f"with constant second difference ${d2}$.\n\n"
        f"Determine the values of $q$ and $p$, and find the general term $T_n$."
    )
    steps = [
        step(from_latex=f"q - ({d1[1]}) = {d2}", to_latex_str=f"q = {d1[2]}", op="Add constant second difference to find first difference q", rule="q = D2 + d2"),
        step(from_latex=f"p - ({t[2]}) = {d1[2]}", to_latex_str=f"p = {t[3]}", op="Add q to T3 to find T4 = p", rule="T4 = T3 + q"),
        step(from_latex=f"2a = {d2},\\; 3a + b = {d1[0]},\\; a + b + c = {t[0]}", to_latex_str=ans, op="Solve for a, b, c to obtain T_n", rule="Quadratic general formula"),
    ]
    return _q("25_quadratic_difference_tree_diagram_analysis", 25, prompt, ans, steps,
              f"First find q = {d1[1]} + {d2}, then p = {t[2]} + q.",
              "Each row in a quadratic difference tree adds the difference below it.",
              f"q = {d1[2]}, p = {t[3]}, and T_n = {tn_str}.",
              ["added_second_difference_directly_to_t3_for_p"], "medium", 4, _svg_spec(svg))


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_linear_sequence_common_difference_and_next_terms": build_01_linear_sequence_common_difference_and_next_terms,
    "02_linear_sequence_general_term_formula": build_02_linear_sequence_general_term_formula,
    "03_linear_sequence_calculate_specific_term": build_03_linear_sequence_calculate_specific_term,
    "04_linear_sequence_solve_for_term_position_n": build_04_linear_sequence_solve_for_term_position_n,
    "05_linear_sequence_number_of_terms_in_finite_list": build_05_linear_sequence_number_of_terms_in_finite_list,
    "06_linear_sequence_unknown_variable_consecutive_terms": build_06_linear_sequence_unknown_variable_consecutive_terms,
    "07_linear_sequence_fractional_algebraic_unknown": build_07_linear_sequence_fractional_algebraic_unknown,
    "08_linear_sequence_decimal_common_difference": build_08_linear_sequence_decimal_common_difference,
    "09_linear_sequence_from_two_non_consecutive_terms": build_09_linear_sequence_from_two_non_consecutive_terms,
    "10_linear_modelling_study_tables_and_chairs": build_10_linear_modelling_study_tables_and_chairs,
    "11_linear_modelling_data_plan_cost_threshold": build_11_linear_modelling_data_plan_cost_threshold,
    "12_linear_modelling_matchstick_row_squares": build_12_linear_modelling_matchstick_row_squares,
    "13_cyclic_repeating_word_and_letter_pattern": build_13_cyclic_repeating_word_and_letter_pattern,
    "14_cyclic_units_digit_of_large_power": build_14_cyclic_units_digit_of_large_power,
    "15_quadratic_identify_constant_second_difference": build_15_quadratic_identify_constant_second_difference,
    "16_quadratic_extend_sequence_using_differences": build_16_quadratic_extend_sequence_using_differences,
    "17_quadratic_find_leading_coefficient_a_from_second_diff": build_17_quadratic_find_leading_coefficient_a_from_second_diff,
    "18_quadratic_find_b_and_c_using_3a_plus_b_method": build_18_quadratic_find_b_and_c_using_3a_plus_b_method,
    "19_quadratic_general_term_positive_leading_a": build_19_quadratic_general_term_positive_leading_a,
    "20_quadratic_general_term_negative_leading_a": build_20_quadratic_general_term_negative_leading_a,
    "21_quadratic_general_term_fractional_leading_a": build_21_quadratic_general_term_fractional_leading_a,
    "22_quadratic_calculate_specific_term_from_tn": build_22_quadratic_calculate_specific_term_from_tn,
    "23_quadratic_solve_for_n_given_term_value": build_23_quadratic_solve_for_n_given_term_value,
    "24_quadratic_test_membership_of_candidate_value": build_24_quadratic_test_membership_of_candidate_value,
    "25_quadratic_difference_tree_diagram_analysis": build_25_quadratic_difference_tree_diagram_analysis,
}
