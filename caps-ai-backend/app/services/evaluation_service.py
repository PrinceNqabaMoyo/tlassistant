"""
evaluation_service.py  –  Part-Marking Engine v1.0
===================================================
Replaces the legacy mock grader with a robust, CAPS-aligned marking engine
that supports:

  • Part marks for tabular cells (journals, ledgers, statements)
  • Mathematical expression parsing (AST-based)
  • Consequential / method marking across dependent cells
  • String matching for details columns
  • Standalone calculation grading with foundational-value matching

Marking Rules Reference (from marking rules.txt):
  Rule 1b: New value → 1 mark
  Rule 1c: Operation on 2 new values → 1 mark per value + 0.5 for result
  Rule 1d: Totals of already-marked values → 0.5 mark
  Rule 1e: Method marks (consequential marking)
  Rule 1f: Don't penalise pre-evaluated sub-expressions
  Rule 2:  Ledger cells each worth 1 mark for strings, derivation explained
  Rule 3a: Multi-step calc: 1 mark per 2 steps, 0.5 for odd extra step,
           0.5 for correct final answer
  Rule 3b: If user determines formula → 1 mark; correct answer → 0.5 mark
           If user extracts values from data → 1 mark; correct answer → 0.5
"""
import asyncio
import ast
import math
import re
from typing import Any, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
#                       MATH EXPRESSION PARSER
# ---------------------------------------------------------------------------

def _clean_number_str(s: str) -> str:
    """Remove spaces inside numbers like '26 000' → '26000', handle R prefix."""
    s = s.strip()
    s = re.sub(r'^[Rr]\s*', '', s)           # strip currency prefix
    s = re.sub(r'[,\s]+(?=\d)', '', s)        # '26 000' → '26000'
    s = s.replace('(', '-').replace(')', '')   # accounting brackets → negative
    return s


def _safe_eval_expr(expr_str: str) -> Optional[float]:
    """
    Safely evaluate a mathematical expression string.
    Uses Python's ast module to parse and evaluate only arithmetic nodes.
    Returns None if the expression is not a valid arithmetic expression.
    """
    cleaned = _clean_number_str(expr_str)
    if not cleaned:
        return None

    # Quick check: if it's just a plain number
    try:
        return float(cleaned)
    except ValueError:
        pass

    # Replace × ÷ with Python ops
    cleaned = cleaned.replace('×', '*').replace('÷', '/').replace('x', '*')
    # Handle percentage: '10%' → '0.10'
    cleaned = re.sub(r'(\d+(?:\.\d+)?)\s*%', lambda m: str(float(m.group(1)) / 100), cleaned)

    try:
        tree = ast.parse(cleaned, mode='eval')
    except SyntaxError:
        return None

    # Walk the AST and ensure only safe nodes
    for node in ast.walk(tree):
        if isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp,
                             ast.Constant, ast.Num,
                             ast.Add, ast.Sub, ast.Mult, ast.Div,
                             ast.Pow, ast.Mod, ast.USub, ast.UAdd)):
            continue
        # Reject anything else (function calls, names, etc.)
        return None

    try:
        result = eval(compile(tree, '<expr>', 'eval'))
        return float(result)
    except Exception:
        return None


def _extract_numbers_from_expr(expr_str: str) -> List[float]:
    """Extract all numeric literals from a math expression string."""
    cleaned = _clean_number_str(expr_str)
    cleaned = cleaned.replace('×', '*').replace('÷', '/').replace('x', '*')
    cleaned = re.sub(r'(\d+(?:\.\d+)?)\s*%', lambda m: str(float(m.group(1)) / 100), cleaned)
    matches = re.findall(r'-?\d+(?:\.\d+)?', cleaned)
    return [float(m) for m in matches]


def _count_operations(expr_str: str) -> int:
    """Count arithmetic operations in an expression string."""
    cleaned = _clean_number_str(expr_str)
    cleaned = cleaned.replace('×', '*').replace('÷', '/').replace('x', '*')
    return len(re.findall(r'[+\-*/]', cleaned))


def _numbers_close(a: float, b: float, tol: float = 0.5) -> bool:
    """Check if two numbers are approximately equal, allowing for rounding."""
    if a == 0 and b == 0:
        return True
    return abs(a - b) <= tol


# ---------------------------------------------------------------------------
#                   CELL-LEVEL SCORING (TABULAR QUESTIONS)
# ---------------------------------------------------------------------------

def _score_string_cell(student: str, expected: str) -> Dict[str, Any]:
    """
    Score a text/string cell (details column, dates, folio references).
    Rule 2 & Rule 1c: 1 mark for each correct string cell.
    """
    s = student.strip().lower()
    e = expected.strip().lower()

    if not e:
        # Empty expected → nothing to mark
        return {"score": 0, "max_score": 0, "feedback": ""}

    if s == e:
        return {"score": 1, "max_score": 1, "feedback": "Correct."}

    # Partial match: check if the key words are present
    e_words = set(e.split())
    s_words = set(s.split())
    overlap = e_words & s_words
    if len(overlap) >= len(e_words) * 0.7 and len(e_words) > 1:
        return {"score": 0.5, "max_score": 1, "feedback": f"Partially correct. Expected: {expected}"}

    return {"score": 0, "max_score": 1, "feedback": f"Incorrect. Expected: {expected}"}


def _classify_cell_type(cell_id: str, expected_val: str, headers: List[str],
                        row_idx: int, col_idx: int) -> str:
    """
    Classify a cell as 'numeric', 'string', or 'empty' based on its
    expected value and its column header.
    """
    if not expected_val or expected_val.strip() == '':
        return 'empty'

    # Try to parse as number
    cleaned = _clean_number_str(expected_val)
    try:
        float(cleaned)
        return 'numeric'
    except ValueError:
        return 'string'


def _score_numeric_cell(
    student_input: str,
    expected_val: str,
    rubric: Optional[Dict[str, Any]] = None,
    is_total: bool = False,
    student_context: Optional[Dict[str, float]] = None,
    dependencies: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Score a numeric cell with part marks.

    Parameters
    ----------
    student_input : str
        Raw student input (could be a number or expression like '26000 + 12000')
    expected_val : str
        The expected correct value as a string
    rubric : dict, optional
        Structured rubric with 'foundational_values', 'operations', 'formula_structure'
    is_total : bool
        If True, this cell is a total/subtotal (Rule 1d: 0.5 mark)
    student_context : dict, optional
        Map of cell_id → student's numeric value for consequential marking
    dependencies : list, optional
        List of cell_ids this cell depends on for consequential marking
    """
    expected_num = _safe_eval_expr(expected_val)
    if expected_num is None:
        # Not a numeric cell after all
        return _score_string_cell(student_input or '', expected_val)

    if not student_input or student_input.strip() == '':
        max_s = 0.5 if is_total else 1
        if rubric:
            max_s = rubric.get('max_score', max_s)
        return {"score": 0, "max_score": max_s, "feedback": "No answer provided."}

    student_num = _safe_eval_expr(student_input)

    # ── CASE 1: Simple cell with no rubric (foundational value) ──
    if not rubric:
        max_s = 0.5 if is_total else 1
        if student_num is not None and _numbers_close(student_num, expected_num):
            return {"score": max_s, "max_score": max_s, "feedback": "Correct."}

        # ── CONSEQUENTIAL MARKING (Rule 1e) ──
        if dependencies and student_context and student_num is not None:
            # Try to see if the student's answer is consistent with their
            # own prior answers using the expected operation
            # This is a simplified version; full impl needs operation info
            pass

        return {"score": 0, "max_score": max_s,
                "feedback": f"Incorrect. Expected {expected_val}"}

    # ── CASE 2: Cell with structured rubric ──
    fv = rubric.get('foundational_values', [])
    ops = rubric.get('operations', [])
    max_score = rubric.get('max_score', 1)
    formula = rubric.get('formula_structure', '')

    score = 0
    feedback_parts = []

    # Extract the numbers the student used
    student_numbers = _extract_numbers_from_expr(student_input) if student_num != expected_num else fv.copy()

    # Award marks for foundational values (Rule 1b: 1 mark per new value)
    matched_fv = 0
    for v in fv:
        if any(_numbers_close(v, sn) for sn in student_numbers):
            matched_fv += 1

    value_marks = matched_fv  # 1 mark per matched foundational value

    # Award marks for operations (Rule 1c: 0.5 per operation)
    student_ops = _count_operations(student_input)
    expected_ops = len(ops)
    op_marks = min(student_ops, expected_ops) * 0.5

    # Award marks for correct final answer (Rule 3a/3b: 0.5 for correct answer)
    answer_mark = 0
    if student_num is not None and _numbers_close(student_num, expected_num):
        answer_mark = 0.5

    score = min(value_marks + op_marks + answer_mark, max_score)

    if answer_mark > 0 and matched_fv == len(fv):
        feedback_parts.append("Correct.")
    elif answer_mark > 0:
        feedback_parts.append(f"Correct answer, but check your working. {formula}")
    elif matched_fv > 0:
        feedback_parts.append(f"Some correct values identified. {formula}")
    else:
        feedback_parts.append(f"Incorrect. {formula}")

    # ── CONSEQUENTIAL MARKING (Rule 1e) ──
    if score < max_score and dependencies and student_context and student_num is not None:
        # Re-derive expected using student's own prior values
        try:
            dep_vals = [student_context.get(d, 0) for d in dependencies]
            if len(dep_vals) >= 2:
                # Try basic operations
                for op_fn, op_name in [(lambda a, b: a + b, '+'),
                                        (lambda a, b: a - b, '-'),
                                        (lambda a, b: a * b, '×'),
                                        (lambda a, b: a / b if b != 0 else None, '÷')]:
                    result = dep_vals[0]
                    valid = True
                    for dv in dep_vals[1:]:
                        result = op_fn(result, dv)
                        if result is None:
                            valid = False
                            break
                    if valid and _numbers_close(student_num, result):
                        method_marks = min(max_score * 0.5, max_score - score)
                        score += method_marks
                        feedback_parts.append(
                            f"Method mark awarded ({method_marks}): "
                            f"correct method applied to your values."
                        )
                        break
        except Exception:
            pass

    return {
        "score": round(score, 1),
        "max_score": max_score,
        "feedback": " ".join(feedback_parts)
    }


# ---------------------------------------------------------------------------
#              QUESTION-LEVEL GRADING (DISPATCHERS)
# ---------------------------------------------------------------------------

async def _grade_mcq(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    """Grade an MCQ question. Full marks or zero."""
    max_score = question.get('marks', 1)
    correct_idx = question.get('correct_idx')
    is_correct = str(answer) == str(correct_idx)
    return {
        "score": max_score if is_correct else 0,
        "max_score": max_score,
        "is_correct": is_correct,
        "feedback": "Correct!" if is_correct else f"Incorrect. The correct answer was option {correct_idx + 1}."
    }


async def _grade_calc(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    """
    Grade a standalone calculation question with part marks.
    Rule 3a: Multi-step: 1 mark per 2 steps, 0.5 for extra, 0.5 for answer.
    Rule 3b: Formula identification + correct answer.
    """
    correct_value = question.get('correct_value')
    rubric = question.get('rubric')
    max_score = question.get('marks', 1)

    if not answer or str(answer).strip() == '':
        return {"score": 0, "max_score": max_score, "is_correct": False,
                "feedback": "No answer provided."}

    if rubric:
        result = _score_numeric_cell(str(answer), str(correct_value), rubric=rubric)
        return {**result, "is_correct": result['score'] >= result['max_score'] * 0.8}

    # Fallback: no rubric, just check the value
    student_num = _safe_eval_expr(str(answer))
    expected_num = float(correct_value) if correct_value is not None else None

    if student_num is not None and expected_num is not None and _numbers_close(student_num, expected_num):
        return {"score": max_score, "max_score": max_score, "is_correct": True,
                "feedback": "Correct."}

    return {"score": 0, "max_score": max_score, "is_correct": False,
            "feedback": f"Incorrect. Expected {correct_value}."}


async def _grade_table(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    """
    Grade a tabular question (journal, ledger, note, statement).
    Iterates through each editable cell, classifies it, and applies
    the appropriate scoring rule. Maintains a student_context dict
    for consequential marking across cells.
    """
    correct_map = question.get('correct_map', {})
    rubric_map = question.get('rubric_map', {})   # per-cell rubrics
    dep_map = question.get('dependency_map', {})   # per-cell dependencies
    headers = question.get('headers', []) or question.get('journal', {}).get('headers', [])
    rows = question.get('rows', []) or question.get('journal', {}).get('rows', [])

    # If answer is dict of cell_id → value submitted by student
    student_answers = answer if isinstance(answer, dict) else {}

    total_score = 0
    total_max = 0
    cell_results = {}
    student_context = {}  # cell_id → student's numeric value

    # Determine which cells are totals (last row typically)
    total_row_ids = set()
    if rows:
        last_row = rows[-1]
        if isinstance(last_row, list):
            for cell in last_row:
                if isinstance(cell, dict):
                    cid = cell.get('cell_id', '')
                    val = cell.get('value', '')
                    if 'total' in val.lower() or 'totals' in val.lower():
                        # Mark numeric cells in the totals row
                        for c2 in last_row:
                            if isinstance(c2, dict) and c2.get('editable'):
                                total_row_ids.add(c2.get('cell_id', ''))
                        break

    # Process cells in order (row by row) for consequential marking
    for cell_id in sorted(correct_map.keys()):
        expected = correct_map[cell_id]

        # Parse cell coordinates
        parts = cell_id.split('_')
        if len(parts) >= 3:
            row_idx = int(parts[1].replace('r', ''))
            col_idx = int(parts[2].replace('c', ''))
        else:
            row_idx, col_idx = 0, 0

        cell_type = _classify_cell_type(cell_id, expected, headers, row_idx, col_idx)

        if cell_type == 'empty':
            continue

        student_val = student_answers.get(cell_id, '')
        is_total = cell_id in total_row_ids
        rubric = rubric_map.get(cell_id)
        deps = dep_map.get(cell_id)

        if cell_type == 'string':
            res = _score_string_cell(student_val, expected)
        else:
            res = _score_numeric_cell(
                student_val, expected,
                rubric=rubric,
                is_total=is_total,
                student_context=student_context,
                dependencies=deps,
            )

        # Track student's numeric value for consequential marking
        sn = _safe_eval_expr(student_val)
        if sn is not None:
            student_context[cell_id] = sn

        cell_results[cell_id] = res
        total_score += res['score']
        total_max += res['max_score']

    return {
        "score": round(total_score, 1),
        "max_score": round(total_max, 1),
        "is_correct": total_score >= total_max * 0.8 if total_max > 0 else False,
        "cell_results": cell_results,
        "feedback": f"Scored {round(total_score, 1)} out of {round(total_max, 1)}."
    }


async def _grade_wordbank(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    """Grade a table_wordbank question — each cell is a string match."""
    correct_map = question.get('correct_map', {})
    student_answers = answer if isinstance(answer, dict) else {}
    total_score = 0
    total_max = 0
    cell_results = {}

    for cell_id, expected in correct_map.items():
        if not expected or expected.strip() == '':
            continue
        student_val = student_answers.get(cell_id, '')
        res = _score_string_cell(student_val, expected)
        cell_results[cell_id] = res
        total_score += res['score']
        total_max += res['max_score']

    return {
        "score": round(total_score, 1),
        "max_score": round(total_max, 1),
        "is_correct": total_score >= total_max * 0.8 if total_max > 0 else False,
        "cell_results": cell_results,
        "feedback": f"Scored {round(total_score, 1)} out of {round(total_max, 1)}."
    }


async def _grade_typed(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    """Grade a typed/free-text question. Basic string or numeric check."""
    max_score = question.get('marks', 1)
    correct = question.get('correct_value') or question.get('correct_answer', '')

    if not answer or str(answer).strip() == '':
        return {"score": 0, "max_score": max_score, "is_correct": False,
                "feedback": "No answer provided."}

    # Try numeric comparison first
    student_num = _safe_eval_expr(str(answer))
    expected_num = _safe_eval_expr(str(correct))
    if student_num is not None and expected_num is not None:
        if _numbers_close(student_num, expected_num):
            return {"score": max_score, "max_score": max_score, "is_correct": True,
                    "feedback": "Correct."}
        return {"score": 0, "max_score": max_score, "is_correct": False,
                "feedback": f"Incorrect. Expected {correct}."}

    # String comparison
    res = _score_string_cell(str(answer), str(correct))
    return {**res, "is_correct": res['score'] >= res['max_score'] * 0.8 if res['max_score'] > 0 else False}


# ---------------------------------------------------------------------------
#                         SINGLE QUESTION DISPATCHER
# ---------------------------------------------------------------------------

async def _grade_single_question(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    """Route a question to the appropriate grading function."""
    q_type = question.get('question_type', 'unknown')

    if q_type == 'mcq':
        return await _grade_mcq(question, answer)
    elif q_type == 'calc':
        return await _grade_calc(question, answer)
    elif q_type in ('journal', 'ledger', 'accounting_equation'):
        return await _grade_table(question, answer)
    elif q_type == 'table_wordbank':
        return await _grade_wordbank(question, answer)
    elif q_type == 'typed':
        return await _grade_typed(question, answer)

    max_score = question.get('marks', 1)
    return {
        "score": 0,
        "max_score": max_score,
        "is_correct": False,
        "feedback": "Unsupported question type for automated grading."
    }


# ---------------------------------------------------------------------------
#                       PUBLIC API: grade_submission
# ---------------------------------------------------------------------------

async def grade_submission(
    questions: List[Dict[str, Any]],
    answers: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Takes a list of questions and a dictionary of submitted answers
    keyed by question ID, and returns a grading report with part marks.
    """
    results = {}
    total_score = 0
    total_max_score = 0

    for q in questions:
        q_id = q.get('id')
        if not q_id:
            continue

        ans = answers.get(str(q_id))

        # Handle bundle questions
        if q.get('question_type') == 'bundle':
            bundle_score = 0
            bundle_max = 0
            bundle_parts_results = []
            parts = q.get('parts', [])

            for i, part in enumerate(parts):
                part_ans = ans[i] if (isinstance(ans, list) and i < len(ans)) else None
                part_res = await _grade_single_question(part, part_ans)
                bundle_score += part_res['score']
                bundle_max += part_res['max_score']
                bundle_parts_results.append(part_res)

            results[str(q_id)] = {
                "score": round(bundle_score, 1),
                "max_score": round(bundle_max, 1),
                "is_correct": bundle_score >= bundle_max * 0.8 if bundle_max > 0 else False,
                "feedback": f"Bundle: {round(bundle_score, 1)} / {round(bundle_max, 1)}",
                "parts": bundle_parts_results,
            }
            total_score += bundle_score
            total_max_score += bundle_max
        else:
            q_res = await _grade_single_question(q, ans)
            results[str(q_id)] = q_res
            total_score += q_res['score']
            total_max_score += q_res['max_score']

    return {
        "results": results,
        "total_score": round(total_score, 1),
        "max_score": round(total_max_score, 1),
        "overall_feedback": f"You scored {round(total_score, 1)} out of {round(total_max_score, 1)}."
    }
