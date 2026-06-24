"""Grade 10 Mathematics API (deterministic, SymPy-backed).

Self-contained blueprint mirroring the Business Studies convention
(``/api/business-studies/grade10``). Serves the rebuilt maths stack:

    POST /generate   – deterministic question generation (computed answers)
    GET  /topics     – topic + subskill catalogue for the frontend registry
    GET  /sections   – scaffold step ordering for a topic
    POST /mark       – mark a batch (mcq / math_short / math_steps)
    POST /diagnose   – live procedure-tracker diagnosis of one working attempt

The legacy ``/api/math`` routes are left untouched.
"""
from __future__ import annotations

import traceback
from typing import Any, Dict, List

from flask import Blueprint, jsonify, request

from app.services import procedure_tracker as pt
from app.utils.grade10_mathematics._math_curriculum import (
    get_section_for_topic,
    get_topic_sections,
    list_topics,
)
from app.utils.grade10_mathematics.term_1 import algebraic_expressions_generator

grade10_mathematics_bp = Blueprint("grade10_mathematics", __name__)

GENERATORS = {
    "grade10_math_algebraic_expressions": algebraic_expressions_generator.generate,
}


def _generate_questions(topic: str, subskill: str, difficulty: str, count: int, seed: Any) -> List[Dict[str, Any]]:
    if topic not in GENERATORS:
        raise ValueError(f"No generator found for topic: {topic}")

    # A scaffold section may map to a pool of subskills; pick one deterministically.
    section = get_section_for_topic(topic, subskill)
    if section and section.get("formats"):
        import random

        picker = random.Random(int(seed) if seed is not None else None)
        subskill = picker.choice(section["formats"])

    result = GENERATORS[topic](subskill=subskill, difficulty=difficulty, count=count, seed=seed)
    return result.get("questions", [])


@grade10_mathematics_bp.route("/generate", methods=["POST"])
def generate_endpoint():
    data = request.get_json() or {}
    topic = data.get("topic")
    subskill = data.get("subskill", "concepts")
    difficulty = data.get("difficulty", "medium")
    count = int(data.get("count", 1))
    seed = data.get("seed")

    if not topic:
        return jsonify({"error": "Missing 'topic'"}), 400
    if count < 1 or count > 20:
        return jsonify({"error": "count must be between 1 and 20"}), 400

    try:
        questions = _generate_questions(topic, subskill, difficulty, count, seed)
        return jsonify({"questions": questions})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:  # noqa: BLE001 - surface generation errors to client
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@grade10_mathematics_bp.route("/topics", methods=["GET"])
def topics_endpoint():
    return jsonify({"topics": list_topics()})


@grade10_mathematics_bp.route("/sections", methods=["GET"])
def sections_endpoint():
    topic = request.args.get("topic")
    if not topic:
        return jsonify({"error": "Missing topic query param"}), 400
    steps = [
        {"key": s["key"], "title": s["title"], "formats": s["formats"]}
        for s in get_topic_sections(topic)
    ]
    return jsonify({"topic": topic, "steps": steps})


def _mark_one(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    q_type = question.get("question_type")
    if q_type == "mcq":
        correct_idx = str(question.get("correct_index", ""))
        is_correct = str(answer) == correct_idx
        return {
            "is_correct": is_correct,
            "score": 1 if is_correct else 0,
            "max_score": 1,
            "feedback": "Correct." if is_correct else "Not quite — review the explanation.",
        }
    if q_type == "math_short":
        return pt.mark_short_answer(question, str(answer or ""))
    if q_type == "math_steps":
        steps = answer if isinstance(answer, list) else str(answer or "").splitlines()
        diag = pt.diagnose(question.get("canonical_solution", {}), steps, int(question.get("marks", 1)))
        return diag
    return {"is_correct": False, "score": 0, "max_score": int(question.get("marks", 1)), "feedback": "Unsupported question type."}


@grade10_mathematics_bp.route("/mark", methods=["POST"])
def mark_endpoint():
    data = request.get_json() or {}
    questions = data.get("questions", [])
    answers = data.get("answers", {})

    results: Dict[str, Any] = {}
    total_score = 0
    max_score = 0
    for q in questions:
        q_id = str(q.get("id", ""))
        res = _mark_one(q, answers.get(q_id))
        results[q_id] = res
        total_score += res.get("score", 0)
        max_score += res.get("max_score", 0)

    return jsonify(
        {
            "results": results,
            "total_score": total_score,
            "max_score": max_score,
            "percentage": round(100 * total_score / max_score, 1) if max_score else 0,
        }
    )


@grade10_mathematics_bp.route("/diagnose", methods=["POST"])
def diagnose_endpoint():
    """Diagnose a single working attempt (live Working Pad feedback)."""
    data = request.get_json() or {}
    question = data.get("question", {})
    steps = data.get("steps", [])
    if not isinstance(steps, list):
        steps = str(steps or "").splitlines()
    try:
        diag = pt.diagnose(
            question.get("canonical_solution", {}),
            steps,
            int(question.get("marks", 1)),
        )
        return jsonify(diag)
    except Exception as e:  # noqa: BLE001
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
