"""Deterministic procedure / working tracker for Mathematics.

Given a question's canonical solution graph and the learner's step-by-step
working, this engine:

  * parses each student line into a SymPy object (equation or expression),
  * checks symbolic equivalence between consecutive lines,
  * localises the FIRST line where the working breaks,
  * awards NSC-style method + accuracy (carry-over) marks.

No LLM is used. The Pro-tier agent consumes this structured diagnosis to narrate
*why* a step is wrong, but the diagnosis itself is fully reproducible.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

import sympy as sp
from sympy.parsing.sympy_parser import (
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)

_TRANSFORMS = standard_transformations + (implicit_multiplication_application,)


def parse_line(text: str) -> Optional[Any]:
    """Parse a single working line into a SymPy ``Eq`` or expression.

    Tolerant of common learner notation: implicit multiplication (``2x``),
    ``^`` for powers, comma decimals (``0,5``). Returns ``None`` if unparseable.
    """
    if text is None:
        return None
    s = str(text).strip()
    if not s:
        return None
    # Normalise learner / SA notation before parsing.
    s = s.replace("^", "**")
    # Comma decimal -> dot, but only between digits (avoid touching tuples).
    s = _decomma(s)
    s = s.replace("\u00d7", "*").replace("\u00f7", "/")
    try:
        if "=" in s:
            lhs, rhs = s.split("=", 1)
            return sp.Eq(
                parse_expr(lhs, transformations=_TRANSFORMS),
                parse_expr(rhs, transformations=_TRANSFORMS),
            )
        return parse_expr(s, transformations=_TRANSFORMS)
    except (sp.SympifyError, SyntaxError, TypeError, ValueError):
        return None


def _decomma(s: str) -> str:
    import re

    return re.sub(r"(?<=\d),(?=\d)", ".", s)


def _restore_sympy(srepr_str: str) -> Optional[Any]:
    """Rebuild a SymPy object from its ``srepr`` string.

    ``srepr`` emits SymPy constructor calls (e.g. ``Add(Symbol('x'), Integer(2))``)
    so it is restored by evaluating against the SymPy namespace.
    """
    if not srepr_str:
        return None
    try:
        return eval(srepr_str, {"__builtins__": {}}, sp.__dict__)
    except Exception:
        try:
            return sp.sympify(srepr_str)
        except (sp.SympifyError, TypeError, ValueError):
            return None


def _one_side(obj: Any) -> Any:
    if isinstance(obj, sp.Equality):
        return sp.expand(obj.lhs - obj.rhs)
    return sp.expand(obj)


def equivalent(a: Any, b: Any, chain_type: str) -> bool:
    """Are two working lines equivalent under the chain semantics?"""
    if a is None or b is None:
        return False
    try:
        if chain_type == "equation":
            pa, pb = _one_side(a), _one_side(b)
            if pa == 0 and pb == 0:
                return True
            if pa == 0 or pb == 0:
                return False
            ratio = sp.simplify(pa / pb)
            return ratio.is_number and ratio != 0
        # expression chain: value-preserving
        return sp.simplify(sp.sympify(a) - sp.sympify(b)) == 0
    except (sp.SympifyError, TypeError, ValueError, ZeroDivisionError):
        return False


def diagnose(
    canonical_solution: Dict[str, Any],
    student_steps: List[str],
    max_marks: int,
) -> Dict[str, Any]:
    """Diagnose a learner's working against the canonical solution.

    Returns per-step statuses, the first error index (or ``None``), the matched
    misconception tags for that step, and an NSC-style mark breakdown.
    """
    chain_type = canonical_solution.get("chain_type", "equation")
    canonical_steps = canonical_solution.get("steps", [])

    # The reference starting point is the first canonical step's "from".
    start = _restore_sympy(canonical_steps[0]["from_sympy"]) if canonical_steps else None
    final_ref = _restore_sympy(canonical_solution.get("final_sympy", ""))

    parsed = [parse_line(line) for line in student_steps if str(line).strip()]
    statuses: List[Dict[str, Any]] = []
    first_error: Optional[int] = None
    valid_transitions = 0

    prev = start
    for idx, cur in enumerate(parsed):
        if cur is None:
            statuses.append({"index": idx, "status": "unparseable"})
            if first_error is None:
                first_error = idx
            prev = cur
            continue
        ok = equivalent(prev, cur, chain_type) if prev is not None else True
        if ok:
            statuses.append({"index": idx, "status": "correct"})
            valid_transitions += 1
        else:
            statuses.append({"index": idx, "status": "error"})
            if first_error is None:
                first_error = idx
        prev = cur

    # Final-answer accuracy: last parsed line equivalent to canonical final.
    final_correct = False
    if parsed and final_ref is not None and parsed[-1] is not None:
        last = parsed[-1]
        if chain_type == "equation":
            final_correct = _final_equation_match(last, final_ref, canonical_solution.get("var", "x"))
        else:
            final_correct = equivalent(last, final_ref, "expression")

    error_step_meta = _error_meta(canonical_steps, first_error)

    # NSC-style marks: method marks for valid transitions (capped), 1 accuracy mark.
    method_max = max(1, max_marks - 1)
    method_marks = min(valid_transitions, method_max)
    accuracy_marks = 1 if final_correct else 0
    total = min(max_marks, method_marks + accuracy_marks)

    return {
        "step_statuses": statuses,
        "first_error_step": first_error,
        "error_type": error_step_meta.get("error_type"),
        "misconception_tags": error_step_meta.get("misconception_tags", []),
        "final_answer_correct": final_correct,
        "marks": {
            "method": method_marks,
            "accuracy": accuracy_marks,
            "awarded": total,
            "max": max_marks,
        },
        "score": total,
        "max_score": max_marks,
        "is_correct": total == max_marks,
    }


def _final_equation_match(last: Any, final_ref: Any, var: str) -> bool:
    """Does the learner's last line state the same solution as canonical?"""
    try:
        x = sp.Symbol(var)
        target = final_ref
        # final_ref may be the bare value or an Eq(x, value).
        if isinstance(final_ref, sp.Equality):
            target = final_ref.rhs
        if isinstance(last, sp.Equality):
            # Accept "x = value" in either orientation.
            for cand in (last.rhs, last.lhs):
                if sp.simplify(cand - target) == 0:
                    return True
            # Or the equation is satisfied by the value.
            return sp.simplify(last.lhs.subs(x, target) - last.rhs.subs(x, target)) == 0
        return sp.simplify(sp.sympify(last) - target) == 0
    except (sp.SympifyError, TypeError, ValueError):
        return False


def _error_meta(canonical_steps: List[Dict[str, Any]], first_error: Optional[int]) -> Dict[str, Any]:
    if first_error is None:
        return {}
    # Map the error onto the canonical step the learner was attempting.
    idx = min(first_error, len(canonical_steps) - 1) if canonical_steps else None
    if idx is None or idx < 0:
        return {"error_type": "unknown", "misconception_tags": []}
    common = canonical_steps[idx].get("common_errors", [])
    return {
        "error_type": common[0] if common else "equivalence_break",
        "misconception_tags": common,
    }


def mark_short_answer(question: Dict[str, Any], student_answer: str) -> Dict[str, Any]:
    """Mark a single-answer (math_short) question.

    Beyond plain symbolic equivalence, the ``answer_mode`` enforces the *form*
    the question asks for, so a learner can't answer "factorise" with the
    already-expanded expression (or vice versa):

      value / expression : value-preserving equivalence only
      expanded           : equivalent AND fully expanded
      factored           : equivalent AND written as a product (not a sum)
      equation / set     : same solution set
    """
    max_marks = int(question.get("marks", 1))
    mode = question.get("answer_mode", "expression")
    ref = _restore_sympy(question.get("answer_sympy", ""))
    cur = parse_line(student_answer)
    correct = False
    if ref is not None and cur is not None:
        if mode in ("equation", "set") or isinstance(ref, sp.Equality) or isinstance(cur, sp.Equality):
            correct = equivalent(cur, ref, "equation")
        elif mode == "factored":
            correct = _is_factored(cur) and equivalent(cur, ref, "expression")
        elif mode == "expanded":
            try:
                correct = (sp.expand(cur) == cur) and equivalent(cur, ref, "expression")
            except (sp.SympifyError, TypeError, ValueError):
                correct = False
        else:
            correct = equivalent(cur, ref, "expression")
    score = max_marks if correct else 0
    return {
        "is_correct": correct,
        "score": score,
        "max_score": max_marks,
        "feedback": "Correct." if correct else f"Not yet. Expected: {question.get('answer_latex', '')}",
    }


def _is_factored(expr: Any) -> bool:
    """True if the top level is a product/power (factored), not a bare sum."""
    try:
        e = sp.sympify(expr)
    except (sp.SympifyError, TypeError, ValueError):
        return False
    if e.is_Atom:
        return False
    return e.is_Mul or e.is_Pow
