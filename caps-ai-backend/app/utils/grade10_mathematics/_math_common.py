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
    options: Optional[List[str]] = None,
    choices: Optional[List[str]] = None,
    correct_index: Optional[int] = None,
    answer: Optional[str] = None,
    explanation: str,
    marks: int = 1,
    prompt_latex: Optional[str] = None,
    options_latex: Optional[List[str]] = None,
    hint: Optional[str] = None,
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    opts = list(options if options is not None else (choices or []))
    if correct_index is None and answer is not None:
        try:
            resolved_index = opts.index(answer)
        except (ValueError, TypeError):
            resolved_index = 0
    else:
        resolved_index = int(correct_index) if correct_index is not None else 0

    hint_text = hint or explanation
    exp_ans = opts[resolved_index] if 0 <= resolved_index < len(opts) else ""
    return {
        "id": make_id(f"{prefix}_mcq"),
        "question_type": "mcq",
        "modality": "math",
        "solution_type": "mcq",
        "prompt": prompt,
        "prompt_latex": prompt_latex or "",
        "options": opts,
        "options_latex": list(options_latex) if options_latex else [],
        "correct_index": str(resolved_index),
        "expected_answer": exp_ans,
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint_text,
        "hints": {
            "tier_1": hint or "Carefully examine all given options and definitions.",
            "tier_2": explanation or "Apply the governing CAPS property or rule to eliminate invalid choices.",
            "tier_3": f"Notice that {explanation}" if explanation else "Work backwards from each option to find the unique match.",
        },
        "guidelines": list(guidelines or []),
    }


def make_short(
    *,
    prefix: str,
    prompt_latex: Optional[str] = None,
    prompt: Optional[str] = None,
    answer_expr: Any = None,
    answer: Any = None,
    answer_mode: str = "expression",
    marks: int = 1,
    canonical_solution: Optional[Dict[str, Any]] = None,
    answer_latex: Optional[str] = None,
    answer_places: Optional[int] = None,
    explanation: str = "",
    hint: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """A single-answer question marked symbolically.

    ``answer_mode``: ``"value"`` (a number), ``"expression"`` (an algebraic
    expression), or ``"set"`` (e.g. inequality solution / multiple roots).
    """
    resolved_prompt_latex = prompt_latex if prompt_latex is not None else (prompt or "")
    resolved_answer_expr = answer_expr if answer_expr is not None else (answer if answer is not None else 0)

    if answer_latex is None:
        if answer_places is not None:
            answer_latex = num(resolved_answer_expr, answer_places)
        else:
            answer_latex = to_latex_safe(resolved_answer_expr)
    return {
        "id": make_id(f"{prefix}_short"),
        "question_type": "math_short",
        "modality": "math",
        "solution_type": "symbolic_steps",
        "prompt": prompt or resolved_prompt_latex,
        "prompt_latex": resolved_prompt_latex,
        "answer": str(answer) if answer is not None else str(resolved_answer_expr),
        "expected_answer": str(answer_latex or resolved_answer_expr),
        "answer_mode": answer_mode,
        "answer_latex": answer_latex,
        "answer_sympy": sp.srepr(resolved_answer_expr) if not isinstance(resolved_answer_expr, str) else resolved_answer_expr,
        "canonical_solution": canonical_solution or {},
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint or explanation,
        "hints": {
            "tier_1": hint or "Focus on the given values and identify the core operation.",
            "tier_2": explanation or "Apply the governing algebraic identity or formula step by step.",
            "tier_3": f"Notice that: {explanation}" if explanation else "Work systematically to obtain the simplified expression or value.",
        },
        "guidelines": list(kwargs.get("guidelines") or []),
    }


def make_steps(
    *,
    prefix: str,
    prompt_latex: str,
    canonical_solution: Dict[str, Any],
    marks: Optional[int] = None,
    explanation: str = "",
    hint: Optional[str] = None,
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """A multi-step working question, marked by the procedure tracker.

    Default marks = 1 method mark per intermediate step + 1 accuracy mark for the
    final line (NSC-style), unless overridden.
    """
    resolved_marks = int(marks) if marks is not None else max(2, len(canonical_solution.get("steps", [])) + 1)
    return {
        "id": make_id(f"{prefix}_steps"),
        "question_type": "math_steps",
        "modality": "math",
        "solution_type": "symbolic_steps",
        "prompt_latex": prompt_latex,
        "answer_mode": "steps",
        "answer_latex": canonical_solution.get("final_latex", ""),
        "expected_answer": str(canonical_solution.get("final_latex", "")),
        "answer_sympy": canonical_solution.get("final_sympy", ""),
        "canonical_solution": canonical_solution,
        "explanation": explanation,
        "marks": resolved_marks,
        "hint_trigger": hint or "",
        "hints": {
            "tier_1": hint or "Identify the first logical step and required factorisation or expansion.",
            "tier_2": explanation or "Apply NSC procedure rules: each line must be mathematically equivalent to the previous line.",
            "tier_3": f"Key transition: {explanation}" if explanation else "Complete each intermediate step systematically before writing the final simplified line.",
        },
        "guidelines": list(guidelines or []),
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
    guidelines: Optional[List[str]] = None,
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
        "modality": "diagram",
        "solution_type": "diagram_element",
        "prompt": prompt,
        "prompt_latex": "",
        "target": target,
        "correct_edge": correct_edge,
        "expected_answer": correct_edge,
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint or "",
        "hints": {
            "tier_1": hint or "Look closely at the labeled vertices and angle of reference on the diagram.",
            "tier_2": explanation or "Apply the trigonometric definition relative to the reference angle (opposite, adjacent, hypotenuse).",
            "tier_3": f"Identification rule: {explanation}" if explanation else "Select the required side or angle corresponding to the target ratio.",
        },
        "guidelines": list(guidelines or []),
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


def make_function_transform(
    *,
    prefix: str,
    prompt: str,
    target_params: Dict[str, float],
    sliders: List[str],
    marks: int = 2,
    tolerance: float = 0.0,
    explanation: str = "",
    hint: Optional[str] = None,
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """A question answered by dragging parameter sliders on the function grapher.
    The learner manipulates ``a`` / ``q`` (and possibly ``b``) until the curve
    matches a dashed target. The submitted ``{a, q, b}`` is compared to
    ``target_params`` structurally (within ``tolerance``) — never pixels — so it
    is the function-graph analogue of ``diagram_select`` / ``number_line_build``.
    The interactive diagram itself is attached via ``with_metadata(diagram_spec=)``.
    """
    return {
        "id": make_id(f"{prefix}_ftrans"),
        "question_type": "function_transform",
        "prompt": prompt,
        "prompt_latex": "",
        "target_params": {k: float(v) for k, v in target_params.items()},
        "sliders": list(sliders),
        "tolerance": float(tolerance),
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint or "",
        "hints": {
            "tier_1": hint or "Observe how parameter 'a' affects curve curvature and 'q' shifts vertical position.",
            "tier_2": explanation or "Align the turning point or asymptote first, then adjust curvature to match.",
            "tier_3": f"Alignment goal: {explanation}" if explanation else "Drag the sliders until the active plot matches the dashed target.",
        },
        "guidelines": list(guidelines or []),
    }


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
            r = rng(base * 1000 + i if seed is not None else None)
            if mixed:
                key = real_keys[i % len(real_keys)]
            elif subskill and subskill in subskill_builders:
                key = subskill
            else:
                key = r.choice(real_keys) if real_keys else default_subskill
            q = subskill_builders[key](r, difficulty)
            if seed is not None:
                # Deterministic id so a fixed seed reproduces output byte-for-byte
                # (lets the agent regenerate the exact same variant).
                q["id"] = f"{q.get('topic', 'math')}_{key}_{base}_{i}"
            questions.append(q)
        return {"questions": questions}

    return generate
