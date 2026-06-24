from typing import Dict, Any, List, Optional

from app.services.student_model import StudentModel
from app.services.generator_registry import generate_variant


# Standard package thresholds
STANDARD_THRESHOLDS = {
    "scaffold_to_practice": 0.6,
    "practice_to_assessment": 0.8,
}


def evaluate_standard_progression(
    mode: str,
    score: float,
    max_score: float,
) -> Dict[str, Any]:
    """Rule-based linear progression for Standard package.

    Returns:
        {
            "action": "advance" | "stay" | "repeat",
            "next_mode": "scaffold" | "practice" | "assessment" | "complete",
            "mastery": float,
            "reason": str,
        }
    """
    mastery = score / max_score if max_score > 0 else 0.0

    if mode == "scaffold":
        if mastery >= STANDARD_THRESHOLDS["scaffold_to_practice"]:
            return {"action": "advance", "next_mode": "practice", "mastery": mastery, "reason": "Scaffold passed"}
        return {"action": "repeat", "next_mode": "scaffold", "mastery": mastery, "reason": "Need more scaffold practice"}

    if mode == "practice":
        if mastery >= STANDARD_THRESHOLDS["practice_to_assessment"]:
            return {"action": "advance", "next_mode": "assessment", "mastery": mastery, "reason": "Practice mastered"}
        return {"action": "repeat", "next_mode": "practice", "mastery": mastery, "reason": "Practice not yet mastered"}

    if mode == "assessment":
        if mastery >= STANDARD_THRESHOLDS["practice_to_assessment"]:
            return {"action": "advance", "next_mode": "complete", "mastery": mastery, "reason": "Assessment passed"}
        return {"action": "repeat", "next_mode": "practice", "mastery": mastery, "reason": "Assessment failed; return to practice"}

    return {"action": "stay", "next_mode": mode, "mastery": mastery, "reason": "Unknown mode"}


def evaluate_pro_progression(
    student_model: StudentModel,
    user_id: str,
    subject: str,
    grade: str,
    topic: str,
    subskill: str,
    score: float,
    max_score: float,
    mode: str,
    metadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
    """Non-linear adaptive progression for Pro package.

    Records the submission, updates streaks, and checks if the student is weak
    on this or any subskill. If weak, injects targeted micro-practice.
    On 3 consecutive correct answers, triggers level-up for the subskill.
    """
    if not student_model or not user_id:
        return evaluate_standard_progression(mode, score, max_score)

    mastery_record = student_model.record_submission(
        user_id=user_id,
        subject=subject,
        grade=grade,
        topic=topic,
        subskill=subskill,
        score=score,
        max_score=max_score,
        metadata=metadata,
    )
    mastery = mastery_record.get("mastery_score", 0.0)
    is_struggling = mastery_record.get("is_struggling", False)

    # Record attempt for streak tracking
    is_correct = mastery >= 0.6  # consider >= 60% as a "correct" attempt for streak purposes
    streak_record = student_model.record_attempt(
        user_id=user_id,
        subject=subject,
        grade=grade,
        topic=topic,
        subskill=subskill,
        is_correct=is_correct,
    )
    consecutive_correct = streak_record.get("consecutive_correct", 0)
    consecutive_incorrect = streak_record.get("consecutive_incorrect", 0)

    # Record success / struggle into legacy collections
    if mastery >= 0.8:
        student_model.record_success(
            user_id=user_id,
            subject=subject,
            grade=grade,
            topic=topic,
            subskill=subskill,
            score=score,
        )
    if mastery < 0.5 or consecutive_incorrect >= 3:
        student_model.record_struggle(
            user_id=user_id,
            subject=subject,
            grade=grade,
            topic=topic,
            subskill=subskill,
            reason=f"mastery={mastery:.2f}, consecutive_incorrect={consecutive_incorrect}",
        )

    # Level-up: 3 consecutive correct answers at current subskill
    if consecutive_correct >= 3:
        return {
            "action": "level_up",
            "next_mode": mode,
            "target_subskill": subskill,
            "mastery": mastery,
            "streak": consecutive_correct,
            "reason": f"{consecutive_correct} consecutive correct answers on {subskill}. Ready for next section.",
            "intervention": None,
        }

    weak_subskills = student_model.get_weak_subskills(
        user_id=user_id,
        subject=subject,
        grade=grade,
        topic=topic,
        threshold=0.6,
    )

    if mode in ("practice", "assessment") and (is_struggling or weak_subskills or consecutive_incorrect >= 3):
        target = weak_subskills[0] if weak_subskills else {"subskill": subskill, "mastery_score": mastery}
        try:
            variants = generate_variant(
                topic=topic,
                subskill=target["subskill"],
                difficulty="medium",
                count=1,
            )
        except Exception:
            variants = []
        return {
            "action": "intervene",
            "next_mode": "practice",
            "target_subskill": target["subskill"],
            "mastery": mastery,
            "streak": consecutive_incorrect,
            "reason": f"Weak subskill detected: {target['subskill']} (mastery={mastery:.2f})",
            "intervention": {
                "type": "micro_practice",
                "questions": variants,
            },
        }

    return evaluate_standard_progression(mode, score, max_score)


def get_progression_recommendation(
    student_model: StudentModel,
    user_id: str,
    subject: str,
    grade: str,
    topic: str,
) -> List[Dict[str, Any]]:
    """Returns a list of focus areas for the student based on their mastery data."""
    if not student_model or not user_id:
        return []

    weak = student_model.get_weak_subskills(user_id, subject, grade, topic, threshold=0.6)
    return [
        {
            "subskill": w["subskill"],
            "mastery_score": w["mastery_score"],
            "recommendation": "practice",
        }
        for w in weak
    ]
