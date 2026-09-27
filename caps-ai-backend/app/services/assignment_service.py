"""
Assignment Service (Layer D — Phase D9)
Deterministic assignment and homework lifecycle service.
Allows teachers to assign topic drills and mock papers to classes via 6-character class codes,
and tracks student completion and scores into the teacher's mark book.
"""

import uuid
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional

# In-memory storage for development / testing with persistent Firestore schema readiness
_ASSIGNMENTS_DB: Dict[str, Dict[str, Any]] = {
    "asg_101": {
        "assignment_id": "asg_101",
        "class_id": "cls_gr10_acc",
        "teacher_id": "tch_demo_101",
        "title": "Cash Receipts Journal — 15% VAT & Debtors Drill",
        "subject": "Accounting",
        "grade": "10",
        "topic": "Cash Receipts Journal",
        "question_count": 5,
        "due_date": "2026-09-25",
        "show_marks_immediately": True,
        "created_at": "2026-09-20T08:00:00Z",
        "submissions": {
            "s1": {"student_id": "s1", "student_name": "Thabo Ndlovu", "score": 85, "submitted_at": "2026-09-20T08:15:00Z", "status": "completed"},
            "s2": {"student_id": "s2", "student_name": "Lerato Dlamini", "score": 62, "submitted_at": "2026-09-20T08:18:00Z", "status": "completed"}
        }
    },
    "asg_102": {
        "assignment_id": "asg_102",
        "class_id": "cls_gr10_math",
        "teacher_id": "tch_demo_101",
        "title": "Quadratic Equations & Factoring Sprint",
        "subject": "Mathematics",
        "grade": "10",
        "topic": "Algebraic Expressions",
        "question_count": 8,
        "due_date": "2026-09-26",
        "show_marks_immediately": True,
        "created_at": "2026-09-20T08:10:00Z",
        "submissions": {
            "s5": {"student_id": "s5", "student_name": "Kagiso Molefe", "score": 68, "submitted_at": "2026-09-20T08:20:00Z", "status": "completed"}
        }
    }
}


def create_assignment(
    class_id: str,
    teacher_id: str,
    title: str,
    subject: str,
    grade: str,
    topic: str,
    question_count: int = 5,
    due_date: str = "2026-09-25",
    show_marks_immediately: bool = True
) -> Dict[str, Any]:
    """Creates a new teacher assignment for a class."""
    asg_id = f"asg_{uuid.uuid4().hex[:8]}"
    assignment = {
        "assignment_id": asg_id,
        "class_id": class_id,
        "teacher_id": teacher_id,
        "title": title,
        "subject": subject,
        "grade": str(grade),
        "topic": topic,
        "question_count": int(question_count),
        "due_date": due_date,
        "show_marks_immediately": bool(show_marks_immediately),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "submissions": {}
    }
    _ASSIGNMENTS_DB[asg_id] = assignment
    return assignment


def get_class_assignments(class_id: str) -> List[Dict[str, Any]]:
    """Fetches all assignments created for a specific class roster."""
    results = [
        asg for asg in _ASSIGNMENTS_DB.values()
        if asg.get("class_id") == class_id
    ]
    results.sort(key=lambda x: x.get("created_at", ""), reverse=True)
    return results


def get_student_assignments(student_id: str, class_ids: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """Fetches assignments visible to a student with their specific submission status."""
    results = []
    for asg in _ASSIGNMENTS_DB.values():
        if class_ids and asg.get("class_id") not in class_ids:
            continue

        submission = asg.get("submissions", {}).get(student_id)
        item = {
            "assignment_id": asg["assignment_id"],
            "class_id": asg["class_id"],
            "title": asg["title"],
            "subject": asg["subject"],
            "grade": asg["grade"],
            "topic": asg["topic"],
            "question_count": asg["question_count"],
            "due_date": asg["due_date"],
            "is_submitted": submission is not None,
            "score": submission.get("score") if submission else None,
            "status": "completed" if submission else "pending"
        }
        results.append(item)

    results.sort(key=lambda x: (x["is_submitted"], x["due_date"]))
    return results


def submit_assignment(
    assignment_id: str,
    student_id: str,
    student_name: str,
    score: int
) -> Dict[str, Any]:
    """Records a student's score upon completing an assigned homework practice."""
    if assignment_id not in _ASSIGNMENTS_DB:
        raise ValueError(f"Assignment {assignment_id} not found")

    asg = _ASSIGNMENTS_DB[assignment_id]
    submission = {
        "student_id": student_id,
        "student_name": student_name,
        "score": int(score),
        "submitted_at": datetime.now(timezone.utc).isoformat(),
        "status": "completed"
    }
    asg["submissions"][student_id] = submission
    return {
        "assignment_id": assignment_id,
        "submission": submission,
        "recorded": True
    }


def get_assignment_submissions(assignment_id: str) -> List[Dict[str, Any]]:
    """Returns all student submissions for an assignment to populate teacher mark books."""
    if assignment_id not in _ASSIGNMENTS_DB:
        return []
    return list(_ASSIGNMENTS_DB[assignment_id].get("submissions", {}).values())
