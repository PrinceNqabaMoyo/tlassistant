"""Deterministic BKT Adaptive Progression & Curriculum Dossier Pipeline Service.

Simulates High-Performing, Medium-Performing, and Low-Performing learner trajectories
across Diagnostic -> Scaffold / Elementary Micro-Drill -> Practice (>= 50 questions) -> Exam (3 Exams).
100% deterministic (Zero LLM tokens). Uses the live generator registry and evaluation_service.
"""
from __future__ import annotations

import asyncio
import json
import math
from typing import Any, Dict, List, Optional

from .evaluation_service import grade_submission
from .generator_registry import (
    generate_variant,
    get_topic_archetypes,
    resolve_generator_key,
)

BANNED_PHRASES = (
    "according to caps",
    "curriculum document",
    "dbe requirements",
    "annual teaching plan",
)


def build_canonical_answer(question: Dict[str, Any]) -> Any:
    """Synthesizes the 100% canonical answer payload matching modalityAnswerDriver.js."""
    if not question:
        return ""

    q_type = str(question.get("question_type") or "").lower()
    modality = str(question.get("modality") or "")

    # 1. Arithmetic Grid (Long Division)
    if modality == "arithmetic_grid" or bool(question.get("arithmetic_grid")):
        grid = question.get("arithmetic_grid") or {}
        return {
            "quotient": str(
                grid.get("quotient")
                if grid.get("quotient") is not None
                else question.get("correct_quotient")
                if question.get("correct_quotient") is not None
                else question.get("expected_answer", 169)
            ),
            "remainder": str(
                grid.get("remainder")
                if grid.get("remainder") is not None
                else question.get("correct_remainder", 0)
            ),
        }

    # 2. MCQ
    options = question.get("options")
    if q_type == "mcq" or (isinstance(options, list) and len(options) > 0):
        if isinstance(question.get("correct_index"), int):
            return question["correct_index"]
        target = str(
            question.get("expected_answer")
            or question.get("correct_answer")
            or question.get("sample_answer")
            or ""
        ).strip()
        if isinstance(options, list):
            for idx, opt in enumerate(options):
                if str(opt).strip() == target:
                    return idx
        return target or 0

    # 3. Diagram Select
    if q_type == "diagram_select" or modality == "diagram" or bool(question.get("correct_edge")):
        return str(
            question.get("correct_edge")
            or question.get("expected_answer")
            or question.get("correct_answer")
            or "AB"
        )

    # 4. Ledger / Table
    if (
        modality == "ledger"
        or question.get("table_schema")
        or question.get("journal")
        or q_type in ("table", "ledger", "tabular_fill", "table_completion")
    ):
        src_map = None
        if isinstance(question.get("correct_map"), dict) and question["correct_map"]:
            src_map = question["correct_map"]
        elif isinstance(question.get("expected_answer"), dict) and question["expected_answer"]:
            src_map = question["expected_answer"]
        if src_map:
            cleaned = {}
            for k, v in src_map.items():
                cleaned[k] = str(v[0] if v else "") if isinstance(v, list) else v
            return cleaned

    # 5. Multi-part sub_parts
    sub_parts = question.get("sub_parts")
    if isinstance(sub_parts, list) and len(sub_parts) > 1:
        return {
            "parts": [
                str(sp.get("expected_answer") or sp.get("answer_latex") or "")
                for sp in sub_parts
            ],
            "value": " ; ".join(
                str(sp.get("expected_answer") or sp.get("answer_latex") or "")
                for sp in sub_parts
            ),
        }

    # 6. Semantic / Rubric
    if modality in ("semantic", "rubric") or q_type in ("rubric", "essay", "short_answer", "conceptual"):
        explanation = str(
            question.get("model_answer")
            or question.get("ideal_answer")
            or question.get("sample_answer")
            or question.get("expected_answer")
            or question.get("worked_solution")
            or question.get("explanation")
            or ""
        )
        keywords = (
            question.get("keywords")
            if isinstance(question.get("keywords"), list)
            else question.get("key_concepts")
            if isinstance(question.get("key_concepts"), list)
            else []
        )
        return {"keywords": keywords, "explanation": explanation}

    # 7. Math Steps
    if q_type == "math_steps":
        sol = question.get("canonical_solution") or {}
        steps = sol.get("steps") if isinstance(sol, dict) else []
        if isinstance(steps, list) and len(steps) > 0:
            lines = [
                str(st.get("to_latex") or st.get("step") or question.get("expected_answer") or "")
                for st in steps
                if isinstance(st, dict)
            ]
            lines = [ln for ln in lines if ln]
            if lines:
                return lines

    # 8. Standard Math / Typed / Calculation
    sol_obj = question.get("canonical_solution") if isinstance(question.get("canonical_solution"), dict) else {}
    raw_ans = (
        question.get("expected_answer")
        if question.get("expected_answer") is not None
        else question.get("correct_answer")
        if question.get("correct_answer") is not None
        else sol_obj.get("final_latex")
        or question.get("sample_answer")
        or question.get("final_answer")
        or question.get("answer_latex")
        or question.get("model_answer")
        or ""
    )
    if isinstance(raw_ans, (dict, list)):
        return json.dumps(raw_ans)
    return str(raw_ans)


def build_partial_answer(question: Dict[str, Any]) -> Any:
    """Synthesizes a partial-credit answer payload awarding method marks (0 < score < max_score)."""
    if not question:
        return "__PARTIAL_METHOD_STEP__"

    modality = str(question.get("modality") or "")
    q_type = str(question.get("question_type") or "").lower()

    # 1. Multi-part sub_parts: answer first part(s) right, last part wrong
    sub_parts = question.get("sub_parts")
    if isinstance(sub_parts, list) and len(sub_parts) > 1:
        parts = []
        for idx, sp in enumerate(sub_parts):
            if idx < len(sub_parts) - 1:
                parts.append(str(sp.get("expected_answer") or sp.get("answer_latex") or ""))
            else:
                parts.append("incorrect_part_attempt")
        return {"parts": parts, "value": " ; ".join(parts)}

    # 2. Ledger: fill half the cells accurately
    if modality == "ledger" and isinstance(question.get("correct_map"), dict):
        entries = list(question["correct_map"].items())
        if len(entries) >= 2:
            half = max(1, len(entries) // 2)
            partial_dict = {
                k: (str(v[0]) if isinstance(v, list) and v else v)
                for k, v in entries[:half]
            }
            partial_dict["__partial_method__"] = True
            return partial_dict

    # 3. Arithmetic Grid
    if modality == "arithmetic_grid" or question.get("arithmetic_grid"):
        grid = question.get("arithmetic_grid") or {}
        return {
            "quotient": str(grid.get("quotient") or question.get("correct_quotient") or 169),
            "remainder": "999",
            "__partial_method__": True,
        }

    # 4. Semantic / Rubric
    if modality in ("semantic", "rubric") or q_type in ("rubric", "essay", "short_answer", "conceptual"):
        kws = question.get("keywords") if isinstance(question.get("keywords"), list) else []
        if len(kws) >= 2:
            half_kws = kws[: max(1, len(kws) // 2)]
            return {
                "keywords": half_kws,
                "explanation": " ".join(str(k) for k in half_kws),
                "__partial_method__": True,
            }
        model_text = str(
            question.get("sample_answer")
            or question.get("model_answer")
            or question.get("expected_answer")
            or ""
        )
        words = model_text.split()
        return {
            "keywords": [],
            "explanation": " ".join(words[: max(2, len(words) // 3)]),
            "__partial_method__": True,
        }

    return "__PARTIAL_METHOD_STEP__"


def build_wrong_answer(question: Dict[str, Any]) -> Any:
    """Synthesizes a known distractor / wrong answer payload (0 marks + misconception_tag)."""
    if not question:
        return "incorrect_response_xyz"

    modality = str(question.get("modality") or "")
    q_type = str(question.get("question_type") or "").lower()

    if modality == "arithmetic_grid" or question.get("arithmetic_grid"):
        return {"quotient": "999999", "remainder": "888"}

    options = question.get("options")
    if q_type == "mcq" or (isinstance(options, list) and len(options) > 0):
        correct_idx = question.get("correct_index") if isinstance(question.get("correct_index"), int) else 0
        opt_len = max(2, len(options) if isinstance(options, list) else 4)
        return (correct_idx + 1) % opt_len

    if q_type == "diagram_select" or modality == "diagram" or bool(question.get("correct_edge")):
        right_edge = str(question.get("correct_edge") or "AB")
        return "BC" if right_edge == "AB" else "AB"

    if modality == "ledger" and isinstance(question.get("correct_map"), dict):
        wrong_map = {}
        for k in question["correct_map"].keys():
            wrong_map[k] = "999999"
        return wrong_map

    sub_parts = question.get("sub_parts")
    if isinstance(sub_parts, list) and len(sub_parts) > 1:
        return {
            "parts": ["__INCORRECT_DISTRACTOR_TOKEN__" for _ in sub_parts],
            "value": " ; ".join("__INCORRECT_DISTRACTOR_TOKEN__" for _ in sub_parts),
        }

    if modality in ("semantic", "rubric") or q_type in ("rubric", "essay", "short_answer", "conceptual"):
        return {"keywords": [], "explanation": "Unrelated misconception response."}

    return "incorrect_value_9999"


def format_answer_for_markdown(ans: Any) -> str:
    """Formats an answer payload cleanly for Markdown table/block display."""
    if ans is None:
        return "`(empty)`"
    if isinstance(ans, dict):
        if "parts" in ans and isinstance(ans["parts"], list):
            return " | ".join(f"**[{i+1}]** `{v}`" for i, v in enumerate(ans["parts"]))
        if "explanation" in ans:
            kws = ans.get("keywords") or []
            kw_str = f" *(Keywords: {', '.join(str(k) for k in kws[:5])})*" if kws else ""
            exp = str(ans.get("explanation") or "")
            if len(exp) > 120:
                exp = exp[:117] + "..."
            return f"`{exp}`{kw_str}"
        if "quotient" in ans:
            return f"`Quotient: {ans.get('quotient')}, Remainder: {ans.get('remainder')}`"
        filtered = {k: v for k, v in ans.items() if k != "__partial_method__"}
        s = json.dumps(filtered, ensure_ascii=False)
        return f"`{s[:140]}...`" if len(s) > 140 else f"`{s}`"
    if isinstance(ans, list):
        s = " -> ".join(str(x) for x in ans)
        return f"`{s[:140]}...`" if len(s) > 140 else f"`{s}`"
    s = str(ans).strip()
    if s == "__PARTIAL_METHOD_STEP__":
        return "`[Partial Working Step — Method Marks Earned]`"
    return f"`{s[:140]}...`" if len(s) > 140 else f"`{s}`"


def _normalize_question_for_grading(question: Dict[str, Any], user_answer: Any) -> tuple[Dict[str, Any], str, Any]:
    q_id = str(question.get("id") or "q_active")
    clean_answer = user_answer
    if isinstance(user_answer, dict) and "cells" in user_answer and isinstance(user_answer["cells"], dict):
        clean_answer = {
            **user_answer.get("cells", {}),
            **{k: v for k, v in user_answer.items() if k != "cells"},
        }

    q_copy = dict(question)
    q_copy["id"] = q_id
    if ("journal" in q_copy or "table_schema" in q_copy) and not q_copy.get("question_type"):
        q_copy["question_type"] = "journal"
    elif ("options" in q_copy or "options_latex" in q_copy) and not q_copy.get("question_type"):
        q_copy["question_type"] = "mcq"
    elif (
        ("arithmetic_grid" in q_copy and q_copy.get("arithmetic_grid"))
        or (isinstance(clean_answer, dict) and "quotient" in clean_answer)
    ) and not q_copy.get("modality"):
        q_copy["modality"] = "arithmetic_grid"

    if "correct_index" in q_copy and "correct_idx" not in q_copy:
        q_copy["correct_idx"] = q_copy["correct_index"]

    return q_copy, q_id, clean_answer


def _extract_worked_solution(q: Dict[str, Any]) -> str:
    """Extracts the rich step-by-step worked solution across diverse generator naming conventions."""
    # 1. If explicit multi-line worked_solution or explanation is present:
    ws = str(q.get("worked_solution") or q.get("explanation") or "").strip()
    if ws and len(ws) > 10:
        return ws

    # 2. Check solution_steps (list of strings or list of step dicts):
    sol_steps = q.get("solution_steps")
    if isinstance(sol_steps, list) and len(sol_steps) > 0:
        lines = []
        for idx, st in enumerate(sol_steps):
            if isinstance(st, str):
                lines.append(st)
            elif isinstance(st, dict):
                rule = st.get("rule") or st.get("description") or st.get("op") or f"Step {idx+1}"
                to_val = st.get("to") or st.get("to_latex") or st.get("step") or ""
                lines.append(f"{rule}: ${to_val}$" if to_val else rule)
        if lines:
            return "\n".join(lines)

    # 3. If canonical_solution has step transitions (SymPy math graphs):
    if isinstance(q.get("canonical_solution"), dict):
        steps = q["canonical_solution"].get("steps") or []
        if steps:
            lines = []
            for st in steps:
                desc = st.get("description") or st.get("rule") or ""
                latex = st.get("to_latex") or st.get("step") or ""
                lines.append(f"{desc}: ${latex}$" if desc else f"${latex}$")
            if lines:
                return "\n".join(lines)

    # 4. If multi-part sub_parts exist:
    if isinstance(q.get("sub_parts"), list) and len(q["sub_parts"]) > 0:
        parts_sol = []
        for idx, sp in enumerate(q["sub_parts"]):
            lbl = sp.get("label") or sp.get("part") or f"Part {idx+1}"
            sp_ans = sp.get("worked_solution") or sp.get("explanation") or sp.get("expected_answer") or sp.get("answer_latex") or ""
            if sp_ans:
                parts_sol.append(f"[{lbl}] {sp_ans}")
        if parts_sol:
            return " ; ".join(parts_sol)

    # 5. Check candidate keys:
    for k in ("worked_solution", "ideal_answer", "model_answer", "sample_answer", "final_answer", "solution", "explanation"):
        val = str(q.get(k) or "").strip()
        if val:
            return val

    # 6. Fallback to expected/correct answers:
    return str(q.get("correct_answer") or q.get("expected_answer") or q.get("answer_latex") or q.get("correct_edge") or "").strip()



def _audit_question_invariants(question: Dict[str, Any], grade: str, subject: str, topic: str) -> List[str]:
    """Checks 6-pillar invariants and returns any issue flags."""
    issues: List[str] = []
    prompt_text = str(
        question.get("prompt")
        or question.get("question")
        or question.get("question_text")
        or question.get("instruction")
        or question.get("prompt_latex")
        or ""
    ).strip()

    if len(prompt_text) <= 10:
        issues.append(f"Prompt too short ({len(prompt_text)} chars)")
    if "undefined" in prompt_text or "NaN" in prompt_text:
        issues.append("Prompt contains 'undefined' or 'NaN'")
    p_low = prompt_text.lower()
    for banned in BANNED_PHRASES:
        if banned in p_low:
            issues.append(f"Meta-curriculum jargon detected: '{banned}'")

    try:
        g_num = int("".join(ch for ch in str(grade) if ch.isdigit()) or "10")
    except ValueError:
        g_num = 10

    if g_num < 12:
        t_low = str(question.get("topic") or "").lower()
        s_low = str(question.get("subskill") or "").lower()
        for term in ("complex_numbers", "argand", "polar form", "de moivre"):
            if term in t_low or term in s_low:
                issues.append(f"Grade {grade} cross-grade bleed: '{term}'")
        if "life" in str(subject).lower():
            for term in ("dihybrid", "punnett", "guinea pig", "pea plant", "monohybrid cross"):
                if term in p_low:
                    issues.append(f"Grade {grade} Life Sciences cross-grade bleed: '{term}'")

    total_marks = int(question.get("marks") or (question.get("marking_schema") or {}).get("total_marks") or 1)
    mp_list = (question.get("marking_schema") or {}).get("marking_points") or []
    if not mp_list:
        issues.append("Empty marking_points in marking_schema")
    else:
        mp_sum = sum(int(mp.get("marks") or 0) for mp in mp_list)
        if mp_sum != total_marks:
            issues.append(f"Marking points sum ({mp_sum}) != total_marks ({total_marks})")

    hints = question.get("hints") or {}
    if not (hints.get("tier_1") and hints.get("tier_2") and hints.get("tier_3")):
        issues.append("Missing 3-tier hints")

    # Worked solution presence check
    sol = _extract_worked_solution(question)
    if not sol or len(sol.strip()) == 0:
        issues.append("Missing worked solution / sample answer")

    # MCQ options check
    if question.get("question_type") == "mcq" or bool(question.get("options")) or bool(question.get("options_latex")):
        opts = question.get("options") or question.get("options_latex") or []
        if not isinstance(opts, list) or len(opts) < 2:
            issues.append(f"MCQ has invalid options: {opts}")

    return issues


def _update_bkt_state(
    state: Dict[str, Any],
    score: float,
    max_score: float,
    is_correct: bool,
    mode: str,
    misconception_tag: Optional[str],
) -> Dict[str, Any]:
    """Mirrors studentStore.js recordAttempt BKT / EMA state transition 1-for-1."""
    pct = round((score / max_score) * 100) if max_score > 0 else (100 if is_correct else 0)
    passed = is_correct if isinstance(is_correct, bool) else (pct >= 50)

    new_formative = int(state.get("formativeMastery", 0))
    consecutive_errors = int(state.get("consecutiveErrors", 0))
    prerequisite_gap = bool(state.get("prerequisiteGapDetected", False))

    if passed:
        consecutive_errors = 0
        prerequisite_gap = False
        gain_scale = max(0.5, pct / 100.0)
        if new_formative < 60:
            new_formative = min(100, round(new_formative + 11 * gain_scale))
        elif new_formative < 80:
            new_formative = min(100, round(new_formative + 6 * gain_scale))
        else:
            new_formative = min(100, round(new_formative + 3 * gain_scale))
    else:
        consecutive_errors += 1
        drop = max(12, round(new_formative * 0.22)) if consecutive_errors >= 2 else 4
        new_formative = max(0, new_formative - drop)
        if consecutive_errors >= 2:
            prerequisite_gap = True
            new_formative = min(new_formative, 45)

    current_eval = int(state.get("evaluativeScore", 0))
    if mode in ("exam", "assessment") or str(mode).startswith("exam_"):
        new_evaluative = round(current_eval * 0.7 + pct * 0.3)
    else:
        new_evaluative = current_eval

    new_status = (
        "scaffold"
        if prerequisite_gap
        else "exam_ready"
        if new_formative >= 80
        else "practice"
        if new_formative >= 60
        else "scaffold"
    )

    return {
        "formativeMastery": new_formative,
        "evaluativeScore": new_evaluative,
        "status": new_status,
        "questionsAttempted": int(state.get("questionsAttempted", 0)) + 1,
        "questionsPassed": int(state.get("questionsPassed", 0)) + (1 if passed else 0),
        "consecutiveErrors": consecutive_errors,
        "prerequisiteGapDetected": prerequisite_gap,
        "lastMisconceptionTag": None if passed else (misconception_tag or state.get("lastMisconceptionTag")),
    }


def _complete_diagnostic(state: Dict[str, Any], diag_pct: float) -> Dict[str, Any]:
    """Mirrors studentStore.js completeDiagnostic calibration 1-for-1."""
    raw_pct = max(0, min(100, round(diag_pct)))
    if raw_pct >= 80:
        calibrated = max(85, raw_pct)
    elif raw_pct >= 60:
        calibrated = max(64, min(74, raw_pct))
    else:
        calibrated = 42

    status = (
        "exam_ready"
        if calibrated >= 80
        else "practice"
        if calibrated >= 60
        else "scaffold"
    )
    return {
        **state,
        "formativeMastery": calibrated,
        "evaluativeScore": round(calibrated * 0.8),
        "status": status,
        "consecutiveErrors": 0,
        "prerequisiteGapDetected": False,
    }


def _build_stage_plan(
    persona: str,
    practice_count: int = 50,
    exams_count: int = 3,
    questions_per_exam: int = 5,
) -> List[Dict[str, Any]]:
    """Constructs the chronological question plan for the given student persona."""
    plan: List[Dict[str, Any]] = []

    if persona == "high-performing":
        # 1. Diagnostic (3/3 correct -> 100% -> exam_ready)
        for d_idx in range(3):
            plan.append({
                "phase_label": f"Diagnostic Q{d_idx+1}/3",
                "stage": "diagnostic",
                "diagnostic_step": d_idx,
                "seed": 100 + d_idx,
                "intent": "canonical",
            })
        # 2. Practice (50 questions: 46 canonical, 3 partial, 1 slip)
        for p_idx in range(practice_count):
            q_num = p_idx + 1
            intent = "canonical"
            if q_num in (15, 30, 42):
                intent = "partial"
            elif q_num == 25:
                intent = "wrong"
            plan.append({
                "phase_label": f"Practice Q{q_num}/{practice_count}",
                "stage": "practice",
                "seed": 1000 + q_num,
                "intent": intent,
            })
        # 3. 3 Exams (5 questions per exam)
        for ex_num in range(1, exams_count + 1):
            for eq_idx in range(1, questions_per_exam + 1):
                intent = "partial" if (ex_num == 2 and eq_idx == 4) else "canonical"
                plan.append({
                    "phase_label": f"Exam {ex_num} - Q{eq_idx}/{questions_per_exam}",
                    "stage": "assessment",
                    "exam_number": ex_num,
                    "seed": 2000 + ex_num * 100 + eq_idx,
                    "intent": intent,
                })

    elif persona == "medium-performing":
        # 1. Diagnostic (2/3 correct -> 67% -> practice)
        for d_idx in range(3):
            plan.append({
                "phase_label": f"Diagnostic Q{d_idx+1}/3",
                "stage": "diagnostic",
                "diagnostic_step": d_idx,
                "seed": 200 + d_idx,
                "intent": "wrong" if d_idx == 2 else "canonical",
            })
        # 2. Practice (50 questions: ~76% pass rate, mix of canonical, partial, single slips)
        wrong_slots = {4, 11, 19, 27, 35, 43}
        partial_slots = {2, 7, 14, 22, 29, 38, 46}
        for p_idx in range(practice_count):
            q_num = p_idx + 1
            intent = "canonical"
            if q_num in wrong_slots:
                intent = "wrong"
            elif q_num in partial_slots:
                intent = "partial"
            plan.append({
                "phase_label": f"Practice Q{q_num}/{practice_count}",
                "stage": "practice",
                "seed": 3000 + q_num,
                "intent": intent,
            })
        # 3. 3 Exams (progressive improvement across Exam 1 -> Exam 2 -> Exam 3)
        for ex_num in range(1, exams_count + 1):
            for eq_idx in range(1, questions_per_exam + 1):
                intent = "canonical"
                if ex_num == 1 and eq_idx == 3:
                    intent = "wrong"
                elif ex_num == 1 and eq_idx == 5:
                    intent = "partial"
                elif ex_num == 2 and eq_idx == 4:
                    intent = "partial"
                plan.append({
                    "phase_label": f"Exam {ex_num} - Q{eq_idx}/{questions_per_exam}",
                    "stage": "assessment",
                    "exam_number": ex_num,
                    "seed": 4000 + ex_num * 100 + eq_idx,
                    "intent": intent,
                })

    else:  # low-performing
        # 1. Diagnostic (1/3 correct -> 33% -> calibrated 42% scaffold)
        for d_idx in range(3):
            plan.append({
                "phase_label": f"Diagnostic Q{d_idx+1}/3",
                "stage": "diagnostic",
                "diagnostic_step": d_idx,
                "seed": 300 + d_idx,
                "intent": "canonical" if d_idx == 0 else "wrong",
            })
        # 2. Scaffold & Prerequisite Gap Regression (2 consecutive errors -> 2 Micro-Drills -> 2 Scaffold recovery)
        plan.append({"phase_label": "Scaffold Q1 (Slip 1)", "stage": "scaffold", "seed": 401, "intent": "wrong"})
        plan.append({"phase_label": "Scaffold Q2 (Slip 2 -> Gap Detected)", "stage": "scaffold", "seed": 402, "intent": "wrong"})
        plan.append({"phase_label": "Elementary Micro-Drill Q1 (Regression)", "stage": "micro_drill", "seed": 403, "intent": "canonical"})
        plan.append({"phase_label": "Elementary Micro-Drill Q2 (Consolidation)", "stage": "micro_drill", "seed": 404, "intent": "canonical"})
        plan.append({"phase_label": "Scaffold Q3 (Recovery)", "stage": "scaffold", "seed": 405, "intent": "canonical"})
        plan.append({"phase_label": "Scaffold Q4 (Unlock Practice >=60%)", "stage": "scaffold", "seed": 406, "intent": "canonical"})

        # 3. Practice (50 questions: struggles early with another regression at Q8-Q9, then climbs to >=80% exam_ready)
        wrong_slots = {3, 8, 9, 16, 24, 33}
        partial_slots = {1, 5, 12, 18, 21, 28, 36, 42}
        for p_idx in range(practice_count):
            q_num = p_idx + 1
            stage_override = "micro_drill" if q_num == 10 else "practice"
            intent = "canonical"
            if q_num in wrong_slots:
                intent = "wrong"
            elif q_num in partial_slots:
                intent = "partial"
            label = (
                f"Practice Q{q_num}/{practice_count} (Micro-Drill Recovery)"
                if q_num == 10
                else f"Practice Q{q_num}/{practice_count}"
            )
            plan.append({
                "phase_label": label,
                "stage": stage_override,
                "seed": 5000 + q_num,
                "intent": intent,
            })

        # 4. 3 Exams (Exam 1 struggles -> Exam 2 improves -> Exam 3 passes)
        for ex_num in range(1, exams_count + 1):
            for eq_idx in range(1, questions_per_exam + 1):
                intent = "canonical"
                if ex_num == 1 and eq_idx in (2, 4):
                    intent = "wrong"
                elif ex_num == 1 and eq_idx == 5:
                    intent = "partial"
                elif ex_num == 2 and eq_idx == 3:
                    intent = "wrong"
                elif ex_num == 2 and eq_idx == 5:
                    intent = "partial"
                elif ex_num == 3 and eq_idx == 4:
                    intent = "partial"
                plan.append({
                    "phase_label": f"Exam {ex_num} - Q{eq_idx}/{questions_per_exam}",
                    "stage": "assessment",
                    "exam_number": ex_num,
                    "seed": 6000 + ex_num * 100 + eq_idx,
                    "intent": intent,
                })

    return plan


async def simulate_persona_topic_dossier(
    grade: str,
    subject: str,
    topic: str,
    persona: str = "high-performing",
    practice_count: int = 50,
    exams_count: int = 3,
    questions_per_exam: int = 5,
) -> Dict[str, Any]:
    """Executes the full BKT trajectory for a single (grade, subject, topic, persona)."""
    resolved_key = resolve_generator_key(topic, grade=str(grade), subject=subject)
    arch_info = get_topic_archetypes(topic=topic, grade=str(grade), subject=subject)
    subskills = arch_info.get("archetypes") or ["default"]

    plan = _build_stage_plan(
        persona=persona,
        practice_count=practice_count,
        exams_count=exams_count,
        questions_per_exam=questions_per_exam,
    )

    state: Dict[str, Any] = {
        "formativeMastery": 0,
        "evaluativeScore": 0,
        "status": "diagnostic_required",
        "questionsAttempted": 0,
        "questionsPassed": 0,
        "consecutiveErrors": 0,
        "prerequisiteGapDetected": False,
        "lastMisconceptionTag": None,
    }

    steps_log: List[Dict[str, Any]] = []
    all_issues: List[str] = []
    diag_scores: List[float] = []
    exam_summaries: Dict[int, Dict[str, Any]] = {
        ex: {"score": 0.0, "max_score": 0.0, "questions": 0}
        for ex in range(1, exams_count + 1)
    }

    for idx, item in enumerate(plan):
        step_num = idx + 1
        stage = item["stage"]
        seed = item["seed"]
        subskill = subskills[idx % len(subskills)] if subskills else "default"

        extra_config: Dict[str, Any] = {"stage": stage}
        if "diagnostic_step" in item:
            extra_config["diagnostic_step"] = item["diagnostic_step"]

        questions = generate_variant(
            topic=topic,
            subskill=subskill,
            difficulty="auto",
            count=1,
            seed=seed,
            grade=str(grade),
            subject=subject,
            extra_config=extra_config,
        )
        q = questions[0]
        q_issues = _audit_question_invariants(q, grade=str(grade), subject=subject, topic=topic)
        for iss in q_issues:
            flagged = f"Step {step_num} (seed={seed}, id={q.get('id')}): {iss}"
            if flagged not in all_issues:
                all_issues.append(flagged)

        total_marks = int(q.get("marks") or (q.get("marking_schema") or {}).get("total_marks") or 1)
        intent = item["intent"]
        if intent == "partial" and total_marks < 2:
            intent = "canonical"

        if intent == "canonical":
            user_ans = build_canonical_answer(q)
        elif intent == "partial":
            user_ans = build_partial_answer(q)
        else:
            user_ans = build_wrong_answer(q)

        q_copy, q_id, clean_ans = _normalize_question_for_grading(q, user_ans)
        report = await grade_submission([q_copy], {q_id: clean_ans})
        res = (report.get("results") or {}).get(q_id) or {}

        score = float(res.get("score", 0))
        max_score = float(res.get("max_score", total_marks) or total_marks)
        is_correct = bool(res.get("is_correct", score >= max_score))
        feedback = str(res.get("feedback") or "")
        misconception_tag = res.get("misconception_tag")
        if not is_correct and not misconception_tag:
            tags = q.get("misconception_tags") or ["general_procedural_error"]
            misconception_tag = tags[0] if tags else "general_procedural_error"

        # Verify grading contract against intent
        if intent == "canonical" and (not is_correct or score < max_score):
            all_issues.append(
                f"Step {step_num} (seed={seed}, id={q_id}): Canonical answer scored {score}/{max_score} instead of 100%"
            )
        elif intent == "wrong" and score > 0:
            all_issues.append(
                f"Step {step_num} (seed={seed}, id={q_id}): Wrong answer scored {score}/{max_score} instead of 0"
            )

        bkt_before = int(state["formativeMastery"])
        status_before = str(state["status"])

        if stage == "diagnostic":
            pct = (score / max_score) * 100.0 if max_score > 0 else 0.0
            diag_scores.append(pct)
            if len(diag_scores) == 3:
                avg_diag = sum(diag_scores) / 3.0
                state = _complete_diagnostic(state, avg_diag)
                state["questionsAttempted"] = 3
                state["questionsPassed"] = sum(1 for s in diag_scores if s >= 50)
            else:
                state = _update_bkt_state(state, score, max_score, is_correct, stage, misconception_tag)
        else:
            state = _update_bkt_state(state, score, max_score, is_correct, stage, misconception_tag)

        if "exam_number" in item:
            ex_n = item["exam_number"]
            exam_summaries[ex_n]["score"] += score
            exam_summaries[ex_n]["max_score"] += max_score
            exam_summaries[ex_n]["questions"] += 1

        prompt_str = str(
            q.get("prompt")
            or q.get("question")
            or q.get("question_text")
            or q.get("instruction")
            or q.get("prompt_latex")
            or ""
        ).strip()
        memo_ans = (
            q.get("expected_answer")
            if q.get("expected_answer") is not None
            else q.get("correct_answer")
            if q.get("correct_answer") is not None
            else q.get("sample_answer")
            or q.get("worked_solution")
            or ""
        )
        worked_sol = _extract_worked_solution(q)
        options_list = q.get("options") or q.get("options_latex")
        options_clean = [str(o) for o in options_list] if isinstance(options_list, list) else None

        steps_log.append({
            "step": step_num,
            "phase_label": item["phase_label"],
            "stage": stage,
            "exam_number": item.get("exam_number"),
            "seed": seed,
            "question_id": q_id,
            "subskill": q.get("subskill") or subskill,
            "difficulty": q.get("difficulty") or "medium",
            "mode": q.get("mode") or "compound",
            "modality": q.get("modality") or "standard",
            "intent": intent,
            "prompt": prompt_str,
            "options": options_clean,
            "sub_parts": q.get("sub_parts") if isinstance(q.get("sub_parts"), list) else None,
            "user_input_formatted": format_answer_for_markdown(user_ans),
            "expected_memo_formatted": format_answer_for_markdown(memo_ans),
            "worked_solution": worked_sol,
            "score": score,
            "max_score": max_score,
            "is_correct": is_correct,
            "feedback": feedback,
            "misconception_tag": misconception_tag,
            "bkt_before": bkt_before,
            "bkt_after": int(state["formativeMastery"]),
            "evaluative_score": int(state["evaluativeScore"]),
            "status_before": status_before,
            "status_after": str(state["status"]),
            "consecutive_errors": int(state["consecutiveErrors"]),
            "prerequisite_gap_detected": bool(state["prerequisiteGapDetected"]),
        })

    practice_steps = [s for s in steps_log if s["stage"] == "practice" or "Practice Q" in s["phase_label"]]
    exam_steps = [s for s in steps_log if s["stage"] == "assessment"]
    practice_prompts = [s["prompt"] for s in practice_steps]
    unique_prompts = set(practice_prompts)
    practice_entropy = round(len(unique_prompts) / len(practice_prompts), 2) if practice_prompts else 1.0

    return {
        "grade": str(grade),
        "subject": subject,
        "topic": topic,
        "persona": persona,
        "resolved_generator_key": resolved_key,
        "archetypes_discovered": subskills,
        "total_questions": len(steps_log),
        "practice_questions_count": len(practice_steps),
        "practice_entropy": practice_entropy,
        "unique_practice_questions": len(unique_prompts),
        "exams_completed": exams_count,
        "exam_questions_count": len(exam_steps),
        "exam_summaries": exam_summaries,
        "final_bkt_mastery": int(state["formativeMastery"]),
        "final_evaluative_score": int(state["evaluativeScore"]),
        "final_status": str(state["status"]),
        "issues": all_issues,
        "passed_pipeline": len(all_issues) == 0 and len(practice_steps) >= practice_count,
        "steps": steps_log,
    }
