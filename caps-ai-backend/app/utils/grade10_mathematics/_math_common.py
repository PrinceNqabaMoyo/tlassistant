"""Shared deterministic helpers for Grade 10 Mathematics generators.

Unlike Business Studies / EMS (which select from hand-authored content banks),
Mathematics answers must be *computed*. These helpers use SymPy to:

  * draw seeded, deterministic parameters,
  * compute the canonical answer,
  * build a canonical, step-by-step solution graph (consumed by both the marker
    and the procedure tracker),
  * emit KaTeX-ready LaTeX using the South-African decimal **comma** convention.

No LLM is used anywhere here. Given a seed, generation is fully reproducible.

Question shapes emitted (all carry adaptive metadata):

    mcq          -> {question_type, prompt, options, correct_index(str), explanation, marks}
    math_short   -> {question_type, prompt_latex, answer_mode, answer_latex,
                     answer_sympy, canonical_solution, marks}
    math_steps   -> {question_type, prompt_latex, answer_mode='steps',
                     canonical_solution, marks}

`canonical_solution` shape:

    {
      "goal": "solve for x",
      "chain_type": "equation" | "expression",
      "var": "x",
      "steps": [
        {"from_latex": "...", "to_latex": "...", "from_sympy": "...",
         "to_sympy": "...", "op": "subtract 2", "rule": "additive inverse",
         "common_errors": ["sign_error"]},
        ...
      ],
      "final_latex": "x = 4",
      "final_sympy": "4"
    }
"""
from __future__ import annotations

import random
import re
import uuid
from typing import Any, Dict, List, Optional

import sympy as sp


# --------------------------------------------------------------------------- #
# Seeded RNG + ids
# --------------------------------------------------------------------------- #
def rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    r.seed(int(seed)) if seed is not None else r.seed()
    return r


def make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def nonzero(r: random.Random, lo: int, hi: int, exclude: Optional[List[int]] = None) -> int:
    """Random integer in [lo, hi] excluding 0 and any extra excluded values."""
    excl = set(exclude or [])
    excl.add(0)
    choices = [n for n in range(lo, hi + 1) if n not in excl]
    return r.choice(choices)


# --------------------------------------------------------------------------- #
# LaTeX rendering with SA decimal comma
# --------------------------------------------------------------------------- #
def _commaize(latex: str) -> str:
    """Render decimal points as commas (SA/CAPS convention).

    Uses ``{,}`` so KaTeX keeps the comma tight against the digits instead of
    adding the list-separator spacing a bare ``,`` would produce.
    """
    return re.sub(r"(?<=\d)\.(?=\d)", "{,}", latex)


def to_latex(expr: Any) -> str:
    """SymPy object -> KaTeX string with comma decimals."""
    return _commaize(sp.latex(expr))


def num(value: Any, places: Optional[int] = None) -> str:
    """Format a plain number as a LaTeX string with a comma decimal separator.

    ``places`` rounds (e.g. trig answers to 2 dp). When omitted, integers render
    without a decimal part and floats use their natural repr.
    """
    if places is not None:
        s = f"{float(value):.{places}f}"
    elif isinstance(value, int) or (isinstance(value, float) and value.is_integer()):
        s = str(int(value))
    else:
        s = str(value)
    return s.replace(".", "{,}")


# --------------------------------------------------------------------------- #
# Canonical solution builders
# --------------------------------------------------------------------------- #
def step(
    *,
    from_expr: Any,
    to_expr: Any,
    op: str,
    rule: str = "",
    common_errors: Optional[List[str]] = None,
    from_latex: Optional[str] = None,
    to_latex: Optional[str] = None,
) -> Dict[str, Any]:
    """One canonical working step.

    ``from_expr`` / ``to_expr`` should be SymPy objects (``Eq`` for equation
    chains, expressions for simplification chains). They are stored both as
    rendered LaTeX and as ``srepr`` strings so the procedure tracker can rebuild
    them for equivalence checks.
    """
    return {
        "from_latex": from_latex if from_latex is not None else to_latex_safe(from_expr),
        "to_latex": to_latex if to_latex is not None else to_latex_safe(to_expr),
        "from_sympy": sp.srepr(from_expr) if from_expr is not None else "",
        "to_sympy": sp.srepr(to_expr) if to_expr is not None else "",
        "op": op,
        "rule": rule,
        "common_errors": list(common_errors or []),
    }


def to_latex_safe(expr: Any) -> str:
    if expr is None:
        return ""
    if isinstance(expr, str):
        return expr
    return to_latex(expr)


def solution(
    *,
    goal: str,
    steps: List[Dict[str, Any]],
    final_expr: Any,
    chain_type: str = "equation",
    var: str = "x",
    final_latex: Optional[str] = None,
) -> Dict[str, Any]:
    return {
        "goal": goal,
        "chain_type": chain_type,
        "var": var,
        "steps": list(steps),
        "final_latex": final_latex if final_latex is not None else to_latex_safe(final_expr),
        "final_sympy": sp.srepr(final_expr) if final_expr is not None else "",
    }


# --------------------------------------------------------------------------- #
# Question builders
# --------------------------------------------------------------------------- #
def make_mcq(
    *,
    prefix: str,
    prompt: str,
    options: List[str],
    correct_index: int,
    explanation: str,
    marks: int = 1,
    prompt_latex: Optional[str] = None,
    options_latex: Optional[List[str]] = None,
    hint: Optional[str] = None,
) -> Dict[str, Any]:
    hint_text = hint or explanation
    return {
        "id": make_id(f"{prefix}_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "prompt_latex": prompt_latex or "",
        "options": list(options),
        "options_latex": list(options_latex) if options_latex else [],
        "correct_index": str(int(correct_index)),
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint_text,
        "guidelines": [hint_text] if hint_text else [],
    }


def make_short(
    *,
    prefix: str,
    prompt_latex: str,
    answer_expr: Any,
    answer_mode: str = "expression",
    marks: int = 1,
    canonical_solution: Optional[Dict[str, Any]] = None,
    answer_latex: Optional[str] = None,
    answer_places: Optional[int] = None,
    explanation: str = "",
    hint: Optional[str] = None,
) -> Dict[str, Any]:
    """A single-answer question marked symbolically.

    ``answer_mode``: ``"value"`` (a number), ``"expression"`` (an algebraic
    expression), or ``"set"`` (e.g. inequality solution / multiple roots).
    """
    if answer_latex is None:
        if answer_places is not None:
            answer_latex = num(answer_expr, answer_places)
        else:
            answer_latex = to_latex_safe(answer_expr)
    return {
        "id": make_id(f"{prefix}_short"),
        "question_type": "math_short",
        "prompt_latex": prompt_latex,
        "answer_mode": answer_mode,
        "answer_latex": answer_latex,
        "answer_sympy": sp.srepr(answer_expr) if not isinstance(answer_expr, str) else answer_expr,
        "canonical_solution": canonical_solution or {},
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint or "",
        "guidelines": [hint] if hint else [],
    }


def make_steps(
    *,
    prefix: str,
    prompt_latex: str,
    canonical_solution: Dict[str, Any],
    marks: Optional[int] = None,
    explanation: str = "",
    hint: Optional[str] = None,
) -> Dict[str, Any]:
    """A multi-step working question, marked by the procedure tracker.

    Default marks = 1 method mark per intermediate step + 1 accuracy mark for the
    final line (NSC-style), unless overridden.
    """
    resolved_marks = int(marks) if marks is not None else max(2, len(canonical_solution.get("steps", [])) + 1)
    return {
        "id": make_id(f"{prefix}_steps"),
        "question_type": "math_steps",
        "prompt_latex": prompt_latex,
        "answer_mode": "steps",
        "answer_latex": canonical_solution.get("final_latex", ""),
        "answer_sympy": canonical_solution.get("final_sympy", ""),
        "canonical_solution": canonical_solution,
        "explanation": explanation,
        "marks": resolved_marks,
        "hint_trigger": hint or "",
        "guidelines": [hint] if hint else [],
    }


def make_diagram_select(
    *,
    prefix: str,
    prompt: str,
    target: str,
    correct_edge: str,
    marks: int = 1,
    explanation: str = "",
    hint: Optional[str] = None,
) -> Dict[str, Any]:
    """A question answered by clicking a side of an interactive diagram.

    The diagram (carried via ``with_metadata(..., diagram_spec=...)``) renders
    clickable edges; the learner selects one and it is compared to
    ``correct_edge`` (an edge key such as ``"AC"``). This proves the Diagram
    Spec is bidirectional: the same vocabulary renders *and* marks the figure.
    """
    return {
        "id": make_id(f"{prefix}_dsel"),
        "question_type": "diagram_select",
        "prompt": prompt,
        "prompt_latex": "",
        "target": target,
        "correct_edge": correct_edge,
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint or "",
        "guidelines": [hint] if hint else [],
    }


def with_metadata(
    question: Dict[str, Any],
    *,
    topic: str,
    subskill: str,
    learning_objective_id: str,
    misconception_tags: Optional[List[str]] = None,
    diagnostic_tags: Optional[List[str]] = None,
    minimum_mastery_score: float = 0.6,
    keywords: Optional[List[str]] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    question.update(
        {
            "topic": topic,
            "subject": "mathematics",
            "grade": "grade-10",
            "subskill": subskill,
            "learning_objective_id": learning_objective_id,
            "misconception_tags": list(misconception_tags or []),
            "diagnostic_tags": list(diagnostic_tags or []),
            "minimum_mastery_score": float(minimum_mastery_score),
            "keywords": list(keywords or []),
        }
    )
    if diagram_spec is not None:
        question["diagram_spec"] = diagram_spec
    return question


# --------------------------------------------------------------------------- #
# Generic generate() dispatcher used by each topic module
# --------------------------------------------------------------------------- #
def build_generate(subskill_builders: Dict[str, Any], default_subskill: str):
    """Return a ``generate(subskill, difficulty, count, seed)`` function.

    ``subskill_builders`` maps a subskill key to ``builder(r, difficulty)`` that
    returns a single question dict. Determinism: each question uses a derived
    seed ``seed*1000 + index`` so a fixed seed reproduces the exact set.
    """

    # Real subskills for "mixed" practice — exclude aliases that point at an
    # existing builder (e.g. "concepts").
    real_keys = [k for k in subskill_builders if k != "concepts"]

    def generate(subskill: Optional[str] = None, difficulty: str = "medium", count: int = 1, seed: Optional[int] = None, **_: Any):
        mixed = subskill == "mixed"
        questions: List[Dict[str, Any]] = []
        base = 0 if seed is None else int(seed)
        for i in range(max(1, int(count))):
            key = real_keys[i % len(real_keys)] if mixed else (subskill if subskill in subskill_builders else default_subskill)
            r = rng(base * 1000 + i if seed is not None else None)
            q = subskill_builders[key](r, difficulty)
            if seed is not None:
                # Deterministic id so a fixed seed reproduces output byte-for-byte
                # (lets the agent regenerate the exact same variant).
                q["id"] = f"{q.get('topic', 'math')}_{key}_{base}_{i}"
            questions.append(q)
        return {"questions": questions}

    return generate
