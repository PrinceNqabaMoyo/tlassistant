"""
audit_logger.py
Cognitive Audit Logger for Fundile Backend.
Records question generation and marking evaluation events to a human-readable JSONL audit file.
"""
import os
import json
from datetime import datetime

AUDIT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../reports/cognitive_audit"))
AUDIT_FILE = os.path.join(AUDIT_DIR, "live_traffic_audit.jsonl")

def _ensure_dir():
    if not os.path.exists(AUDIT_DIR):
        try:
            os.makedirs(AUDIT_DIR, exist_ok=True)
        except Exception:
            pass

def log_question_generation(subject, grade, topic, questions, seed=None, role="learner"):
    """Appends question generation event to live audit log."""
    try:
        _ensure_dir()
        sample_q = questions[0] if isinstance(questions, list) and questions else questions
        record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event_type": "QUESTION_GENERATION",
            "role": role,
            "subject": subject,
            "grade": str(grade),
            "topic": topic,
            "seed": seed,
            "question_count": len(questions) if isinstance(questions, list) else 1,
            "sample_prompt": sample_q.get("prompt") or sample_q.get("title") or sample_q.get("prompt_latex") if isinstance(sample_q, dict) else str(sample_q),
            "total_marks": sample_q.get("marks", 1) if isinstance(sample_q, dict) else 1,
            "has_hints": bool(sample_q.get("hints")) if isinstance(sample_q, dict) else False,
        }
        with open(AUDIT_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
    except Exception as e:
        # Non-blocking logging failure
        print(f"[AuditLogger] Question generation log warning: {e}")

def log_answer_evaluation(question_id, user_answer, result, role="learner"):
    """Appends answer evaluation event to live audit log."""
    try:
        _ensure_dir()
        record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event_type": "ANSWER_EVALUATION",
            "role": role,
            "question_id": question_id,
            "user_answer": user_answer,
            "score": result.get("score", 0),
            "total": result.get("total", 1),
            "is_correct": result.get("is_correct", False),
            "feedback": result.get("feedback", ""),
            "misconception_tag": result.get("misconception_tag"),
        }
        with open(AUDIT_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
    except Exception as e:
        # Non-blocking logging failure
        print(f"[AuditLogger] Answer evaluation log warning: {e}")
