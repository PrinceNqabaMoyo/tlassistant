"""Grade 10 Mathematics — Term 1 — Patterns & Sequences (deterministic, SymPy-backed)."""
from __future__ import annotations
from typing import Any, Dict
import sympy as sp
from app.utils.grade10_mathematics._math_common import (
    build_generate, make_short, make_steps, nonzero, solution, step, to_latex, to_latex_safe, with_metadata,
)

TOPIC = "grade10_math_patterns_sequences"
LO = "math10_patterns_sequences"
n = sp.Symbol("n")


def _term(a: int, d: int, pos: int) -> int:
    """T_n = a + (n-1)d, evaluated at position pos (1-indexed)."""
    return a + (pos - 1) * d


def _seq(a: int, d: int, count: int) -> str:
    """Render a semicolon-separated sequence."""
    return "; ".join(str(_term(a, d, i)) for i in range(1, count + 1))


def _build_next_terms(r, difficulty: str) -> Dict[str, Any]:
    a = r.randint(1, 20)
    d = nonzero(r, 1, 10)
    terms_shown = r.randint(3, 5)
    terms_needed = r.randint(2, 3)
    seq_str = _seq(a, d, terms_shown)
    next_vals = "; ".join(str(_term(a, d, terms_shown + i)) for i in range(1, terms_needed + 1))
    expr = sp.Eq(sp.Symbol("T_n"), a + (n - 1) * d)
    steps = [
        step(from_expr=sp.Symbol("d"), to_expr=sp.Integer(d), op="find common difference", rule="d = T_2 - T_1", common_errors=["forgot_common_difference_sign"]),
        step(from_expr=sp.Symbol("T_n"), to_expr=expr, op="write general term", rule="T_n = a + (n-1)d", common_errors=["off_by_one_in_n"]),
    ]
    sol = solution(goal="find next terms", chain_type="expression", var="n", steps=steps, final_expr=next_vals)
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Write down the next {terms_needed} terms: }} {seq_str}; \\ldots",
                   answer_expr=next_vals, answer_mode="expression", marks=2, canonical_solution=sol,
                   explanation=f"The common difference is {d}. Each term increases by {d}.",
                   hint=f"Find d by subtracting consecutive terms, then add {d} repeatedly.")
    return with_metadata(q, topic=TOPIC, subskill="next_terms",
                         learning_objective_id=f"{LO}.next_terms",
                         misconception_tags=["forgot_common_difference_sign", "off_by_one_in_n"],
                         diagnostic_tags=["sequences", "linear"])


def _build_common_difference(r, difficulty: str) -> Dict[str, Any]:
    if r.random() < 0.8:
        a = r.randint(1, 20)
        d = nonzero(r, -15, 15)
        count = r.randint(4, 6)
        seq_str = _seq(a, d, count)
        ans = sp.Integer(d)
        explanation = f"d = T_2 - T_1 = {a+d} - {a} = {d}" if d != 0 else "All terms are equal, so d = 0."
        misconception = ["forgot_common_difference_sign"]
    else:
        # Non-linear distractor
        a = r.randint(1, 5)
        seq = [a * i * i for i in range(1, 6)]
        seq_str = "; ".join(str(v) for v in seq)
        ans = "none"
        explanation = "The differences between consecutive terms are not constant, so there is no common difference."
        misconception = ["assumed_linear_when_quadratic"]
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Find the common difference: }} {seq_str}; \\ldots",
                   answer_expr=ans, answer_mode="expression", marks=1,
                   explanation=explanation, hint="Subtract consecutive terms. If the result is always the same, that is d.")
    return with_metadata(q, topic=TOPIC, subskill="common_difference",
                         learning_objective_id=f"{LO}.common_difference",
                         misconception_tags=misconception,
                         diagnostic_tags=["sequences", "common_difference"])


def _build_general_term(r, difficulty: str) -> Dict[str, Any]:
    a = r.randint(1, 20)
    d = nonzero(r, -10, 10)
    count = r.randint(4, 6)
    seq_str = _seq(a, d, count)
    # T_n = a + (n-1)d = dn + (a-d)
    ans = sp.expand(a + (n - 1) * d)
    steps = [
        step(from_expr=sp.Symbol("d"), to_expr=sp.Integer(d), op="find common difference", rule="d = T_2 - T_1", common_errors=["forgot_common_difference_sign"]),
        step(from_expr=sp.Symbol("T_n"), to_expr=sp.Eq(sp.Symbol("T_n"), a + (n - 1) * d), op="substitute into formula", rule="T_n = a + (n-1)d", common_errors=["off_by_one_in_n"]),
        step(from_expr=sp.Eq(sp.Symbol("T_n"), a + (n - 1) * d), to_expr=sp.Eq(sp.Symbol("T_n"), ans), op="simplify", rule="expand brackets", common_errors=["sign_error"]),
    ]
    sol = solution(goal="find general term", chain_type="expression", var="n", steps=steps, final_expr=ans)
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Find the general formula $T_n$ for: }} {seq_str}; \\ldots",
                   answer_expr=ans, answer_mode="expression", marks=2, canonical_solution=sol,
                   explanation=f"a = {a}, d = {d}, so T_n = {a} + (n-1)({d}) = {to_latex(ans)}",
                   hint="Use T_n = a + (n-1)d, then simplify.")
    return with_metadata(q, topic=TOPIC, subskill="general_term",
                         learning_objective_id=f"{LO}.general_term",
                         misconception_tags=["off_by_one_in_n", "forgot_common_difference_sign", "sign_error"],
                         diagnostic_tags=["sequences", "general_term"])


def _build_term_from_n(r, difficulty: str) -> Dict[str, Any]:
    a = r.randint(1, 15)
    d = nonzero(r, 1, 8)
    pos = r.randint(10, 50)
    # T_n = a + (n-1)d, simplified
    formula = sp.expand(a + (n - 1) * d)
    ans = _term(a, d, pos)
    steps = [
        step(from_expr=formula, to_expr=None, op="substitute n", rule=f"replace n with {pos}", common_errors=["used_term_value_as_position"]),
        step(from_expr=None, to_expr=sp.Integer(ans), op="evaluate", rule="arithmetic", common_errors=["sign_error"]),
    ]
    sol = solution(goal="evaluate term", chain_type="expression", var="n", steps=steps, final_expr=sp.Integer(ans))
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Given $T_n = {to_latex(formula)}$, find $T_{{{pos}}}$.}}",
                   answer_expr=sp.Integer(ans), answer_mode="value", marks=1, canonical_solution=sol,
                   explanation=f"T_{{{pos}}} = {a} + ({pos}-1)({d}) = {ans}",
                   hint="Substitute the position number into the formula.")
    return with_metadata(q, topic=TOPIC, subskill="term_from_n",
                         learning_objective_id=f"{LO}.term_from_n",
                         misconception_tags=["used_term_value_as_position", "sign_error"],
                         diagnostic_tags=["sequences", "evaluation"])


def _build_n_from_term(r, difficulty: str) -> Dict[str, Any]:
    a = r.randint(1, 15)
    d = nonzero(r, 2, 8)
    formula = sp.expand(a + (n - 1) * d)
    # Pick a valid term value
    target_n = r.randint(5, 20)
    target_val = _term(a, d, target_n)
    # Solve a + (n-1)d = target_val  =>  n = (target_val - a)/d + 1
    ans = sp.Integer(target_n)
    eq = sp.Eq(a + (n - 1) * d, target_val)
    steps = [
        step(from_expr=sp.Eq(sp.Symbol("T_n"), target_val), to_expr=eq, op="substitute formula", rule=f"{a} + (n-1)({d}) = {target_val}", common_errors=["used_term_value_as_position"]),
        step(from_expr=eq, to_expr=sp.Eq(n, ans), op="solve for n", rule="linear equation", common_errors=["off_by_one_in_n"]),
    ]
    sol = solution(goal="find position", chain_type="equation", var="n", steps=steps, final_expr=ans)
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Given $T_n = {to_latex(formula)}$, find $n$ if $T_n = {target_val}$.}}",
                   answer_expr=ans, answer_mode="value", marks=2, canonical_solution=sol,
                   explanation=f"{a} + (n-1)({d}) = {target_val}  =>  n = {target_n}",
                   hint="Set the formula equal to the given term value and solve for n.")
    return with_metadata(q, topic=TOPIC, subskill="n_from_term",
                         learning_objective_id=f"{LO}.n_from_term",
                         misconception_tags=["used_term_value_as_position", "off_by_one_in_n"],
                         diagnostic_tags=["sequences", "solve_for_n"])


def _build_missing_terms(r, difficulty: str) -> Dict[str, Any]:
    a = r.randint(1, 15)
    d = nonzero(r, 1, 8)
    formula = sp.expand(a + (n - 1) * d)
    # Show terms 1-5 with one missing
    missing_pos = r.randint(2, 4)
    terms = [_term(a, d, i) for i in range(1, 6)]
    shown = [str(v) if i != missing_pos - 1 else "\\ldots" for i, v in enumerate(terms)]
    seq_str = "; ".join(shown)
    ans = sp.Integer(terms[missing_pos - 1])
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{Find the missing term: }} {seq_str}",
                   answer_expr=ans, answer_mode="value", marks=1,
                   explanation=f"The missing term is T_{{{missing_pos}}} = {a} + ({missing_pos}-1)({d}) = {ans}",
                   hint="Use the general formula or find the common difference.")
    return with_metadata(q, topic=TOPIC, subskill="missing_terms",
                         learning_objective_id=f"{LO}.missing_terms",
                         misconception_tags=["off_by_one_in_n", "forgot_common_difference_sign"],
                         diagnostic_tags=["sequences", "missing_terms"])


def _build_diagram_pattern(r, difficulty: str) -> Dict[str, Any]:
    """Text-based pattern problem (diagram description + general formula)."""
    family = r.choice(["tables", "matchsticks", "stadium"])
    if family == "tables":
        a, d = 4, 2
        desc = "\\text{Each table seats 4 people. When joined, each extra table adds 2 seats.}"
    elif family == "matchsticks":
        a, d = 3, 2
        desc = "\\text{A row of 1 square uses 3 matchsticks on the bottom/top. Each extra square adds 2 matchsticks.}"
    else:
        a, d = 500, 250
        desc = "\\text{A stadium has 500 seats in row 1. Each subsequent row has 250 more seats.}"
    formula = sp.expand(a + (n - 1) * d)
    ans = formula
    steps = [
        step(from_expr=sp.Symbol("a"), to_expr=sp.Integer(a), op="identify first term", rule="a = T_1", common_errors=["used_term_value_as_position"]),
        step(from_expr=sp.Symbol("d"), to_expr=sp.Integer(d), op="find common difference", rule=f"d = T_2 - T_1 = {a+d} - {a}", common_errors=["forgot_common_difference_sign"]),
        step(from_expr=sp.Symbol("T_n"), to_expr=sp.Eq(sp.Symbol("T_n"), formula), op="write formula", rule="T_n = a + (n-1)d", common_errors=["off_by_one_in_n"]),
    ]
    sol = solution(goal="find general formula from pattern", chain_type="expression", var="n", steps=steps, final_expr=ans)
    q = make_short(prefix=TOPIC, prompt_latex=f"{desc} \\quad \\text{{Find $T_n$ for figure $n$.}}",
                   answer_expr=ans, answer_mode="expression", marks=2, canonical_solution=sol,
                   explanation=f"a = {a}, d = {d}, so T_n = {to_latex(formula)}",
                   hint="Find the number of items for figure 1, 2, 3. The difference gives d.")
    return with_metadata(q, topic=TOPIC, subskill="diagram_pattern",
                         learning_objective_id=f"{LO}.diagram",
                         misconception_tags=["off_by_one_in_n", "forgot_common_difference_sign", "used_term_value_as_position"],
                         diagnostic_tags=["sequences", "diagram_pattern"])


def _build_letter_sequence(r, difficulty: str) -> Dict[str, Any]:
    pattern_len = r.randint(3, 5)
    letters = [chr(ord('A') + i) for i in range(pattern_len)]
    pattern_str = "".join(letters)
    pos = r.randint(20, 100)
    idx = (pos - 1) % pattern_len
    ans = letters[idx]
    q = make_short(prefix=TOPIC, prompt_latex=f"\\text{{The pattern {pattern_str}{pattern_str}{pattern_str}\\ldots continues. What is the {pos}th letter?}}",
                   answer_expr=ans, answer_mode="expression", marks=1,
                   explanation=f"The pattern repeats every {pattern_len} letters. {pos} mod {pattern_len} = {(pos % pattern_len) or pattern_len}, so the letter is '{ans}'.",
                   hint="Divide the position by the pattern length and look at the remainder.")
    return with_metadata(q, topic=TOPIC, subskill="letter_sequence",
                         learning_objective_id=f"{LO}.letter_sequence",
                         misconception_tags=["off_by_one_in_n"],
                         diagnostic_tags=["sequences", "modular"])


def _build_linear_param(r, difficulty: str) -> Dict[str, Any]:
    k = sp.Symbol("k")
    a_coeff = nonzero(r, 1, 5)
    b_coeff = nonzero(r, -5, 5)
    c_const = nonzero(r, -20, 20)
    d = nonzero(r, 2, 8)
    # Three terms: (ak+b)/c, (ak+b)/c + d, (ak+b)/c + 2d  => linear when expressed as T_n
    # Actually let's make it: T1 = k/3 - 1, T2 = -5k/3 + 2, T3 = -2k/3 + 10
    # For linear: d must be constant => T2-T1 = T3-T2
    c1 = nonzero(r, 1, 5)
    c2 = nonzero(r, 1, 5)
    c3 = nonzero(r, 1, 5)
    const1 = nonzero(r, -10, 10)
    const2 = nonzero(r, -10, 10)
    const3 = nonzero(r, -10, 10)
    # T1 = c1*k + const1, T2 = c2*k + const2, T3 = c3*k + const3
    # For common difference: T2-T1 = T3-T2 => (c2-c1)k + (const2-const1) = (c3-c2)k + (const3-const2)
    # => [(c2-c1)-(c3-c2)]k = (const3-const2)-(const2-const1)
    # => [2c2-c1-c3]k = const3-2*const2+const1
    lhs_coeff = 2 * c2 - c1 - c3
    rhs_val = const3 - 2 * const2 + const1
    if lhs_coeff == 0:
        # degenerate, regenerate
        return _build_linear_param(r, difficulty)
    ans = sp.Rational(rhs_val, lhs_coeff)
    t1 = c1 * k + const1
    t2 = c2 * k + const2
    t3 = c3 * k + const3
    steps = [
        step(from_expr=sp.Eq(t2 - t1, t3 - t2), to_expr=None, op="equate differences", rule="T_2 - T_1 = T_3 - T_2", common_errors=["sign_error"]),
        step(from_expr=None, to_expr=sp.Eq(k, ans), op="solve for k", rule="linear equation in k", common_errors=["sign_error"]),
    ]
    sol = solution(goal="find k for linear sequence", chain_type="equation", var="k", steps=steps, final_expr=ans)
    q = make_steps(prefix=TOPIC, prompt_latex=f"\\text{{The sequence with terms $T_1 = {to_latex(t1)}$, $T_2 = {to_latex(t2)}$, $T_3 = {to_latex(t3)}$ is linear. Find $k$.}}",
                   canonical_solution=sol, marks=3,
                   explanation="For a linear sequence, the difference between consecutive terms must be constant.",
                   hint="Set T_2 - T_1 = T_3 - T_2 and solve for k.")
    return with_metadata(q, topic=TOPIC, subskill="linear_param",
                         learning_objective_id=f"{LO}.linear_param",
                         misconception_tags=["sign_error", "assumed_linear_when_quadratic"],
                         diagnostic_tags=["sequences", "parameter"])


def _build_word_problem(r, difficulty: str) -> Dict[str, Any]:
    scenario = r.choice(["savings", "stadium", "data_plan"])
    if scenario == "savings":
        a = r.randint(50, 200)
        d = r.randint(20, 100)
        target_week = r.randint(10, 30)
        total_saved = _term(a, d, target_week)
        prompt = f"\\text{{You save R{a} in week 1 and increase your savings by R{d} each week. How much have you saved after {target_week} weeks?}}"
        formula = sp.expand(a + (n - 1) * d)
        # Sum = target_week/2 * (2a + (target_week-1)d)
        ans = sp.Rational(target_week, 1) * (2 * a + (target_week - 1) * d) // 2
        steps = [
            step(from_expr=sp.Symbol("a"), to_expr=sp.Integer(a), op="identify a", rule="T_1 = a", common_errors=["used_term_value_as_position"]),
            step(from_expr=sp.Symbol("d"), to_expr=sp.Integer(d), op="identify d", rule="common difference", common_errors=["forgot_common_difference_sign"]),
            step(from_expr=sp.Symbol("T_n"), to_expr=sp.Eq(sp.Symbol("T_n"), formula), op="write formula", rule="T_n = a + (n-1)d", common_errors=["off_by_one_in_n"]),
            step(from_expr=sp.Eq(sp.Symbol("T_n"), formula), to_expr=None, op="substitute n", rule=f"n = {target_week}", common_errors=["used_term_value_as_position"]),
            step(from_expr=None, to_expr=sp.Integer(ans), op="calculate", rule="arithmetic series sum", common_errors=["sign_error"]),
        ]
    elif scenario == "stadium":
        a = r.randint(400, 600)
        d = r.randint(150, 300)
        target_row = r.randint(10, 20)
        ans = _term(a, d, target_row)
        prompt = f"\\text{{A stadium has {a} seats in row 1. Each row has {d} more seats than the previous. How many seats in row {target_row}?}}"
        formula = sp.expand(a + (n - 1) * d)
        steps = [
            step(from_expr=sp.Symbol("a"), to_expr=sp.Integer(a), op="identify a", rule="T_1 = a", common_errors=["used_term_value_as_position"]),
            step(from_expr=sp.Symbol("d"), to_expr=sp.Integer(d), op="identify d", rule="common difference", common_errors=["forgot_common_difference_sign"]),
            step(from_expr=sp.Symbol("T_n"), to_expr=sp.Eq(sp.Symbol("T_n"), formula), op="write formula", rule="T_n = a + (n-1)d", common_errors=["off_by_one_in_n"]),
            step(from_expr=sp.Eq(sp.Symbol("T_n"), formula), to_expr=sp.Integer(ans), op="substitute n", rule=f"n = {target_row}", common_errors=["used_term_value_as_position"]),
        ]
    else:  # data_plan
        a = r.randint(100, 150)
        d = r.randint(10, 30)
        target_gb = r.randint(15, 30)
        ans = _term(a, d, target_gb)
        prompt = f"\\text{{A data plan costs R{a} for 1 GB. Each extra GB costs R{d} more. Find the cost for {target_gb} GB.}}"
        formula = sp.expand(a + (n - 1) * d)
        steps = [
            step(from_expr=sp.Symbol("a"), to_expr=sp.Integer(a), op="identify a", rule="cost for 1 GB", common_errors=["used_term_value_as_position"]),
            step(from_expr=sp.Symbol("d"), to_expr=sp.Integer(d), op="identify d", rule="extra cost per GB", common_errors=["forgot_common_difference_sign"]),
            step(from_expr=sp.Symbol("T_n"), to_expr=sp.Eq(sp.Symbol("T_n"), formula), op="write formula", rule="T_n = a + (n-1)d", common_errors=["off_by_one_in_n"]),
            step(from_expr=sp.Eq(sp.Symbol("T_n"), formula), to_expr=sp.Integer(ans), op="substitute", rule=f"n = {target_gb}", common_errors=["used_term_value_as_position"]),
        ]
    sol = solution(goal="solve word problem", chain_type="expression", var="n", steps=steps, final_expr=sp.Integer(ans))
    q = make_steps(prefix=TOPIC, prompt_latex=prompt, canonical_solution=sol, marks=3,
                   explanation="Identify a and d from the problem, write the formula, then substitute.",
                   hint="Look for the starting value and what is added each time.")
    return with_metadata(q, topic=TOPIC, subskill="word_problem",
                         learning_objective_id=f"{LO}.word_problem",
                         misconception_tags=["used_term_value_as_position", "off_by_one_in_n", "forgot_common_difference_sign"],
                         diagnostic_tags=["sequences", "word_problems"])


# --------------------------------------------------------------------------- #
# Dispatcher
# --------------------------------------------------------------------------- #
generate = build_generate(
    {
        "next_terms": _build_next_terms,
        "common_difference": _build_common_difference,
        "general_term": _build_general_term,
        "term_from_n": _build_term_from_n,
        "n_from_term": _build_n_from_term,
        "missing_terms": _build_missing_terms,
        "diagram_pattern": _build_diagram_pattern,
        "letter_sequence": _build_letter_sequence,
        "linear_param": _build_linear_param,
        "word_problem": _build_word_problem,
    },
    default_subskill="next_terms",
)
