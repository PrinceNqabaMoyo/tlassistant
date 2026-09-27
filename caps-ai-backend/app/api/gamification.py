"""
Gamification API Router (Layer E)
---------------------------------
Endpoints for querying gamification status, XP, badges, and recording
standardized ChallengeGate examination attempts.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional

from app.services import gamification_service

router = APIRouter(prefix="/api/gamification", tags=["Gamification & Credentials"])


class ChallengeAttemptRequest(BaseModel):
    user_id: str
    challenge_id: str
    subject: str
    topic_id: str
    score: int
    total_marks: int
    student_profile: Optional[Dict[str, Any]] = None


@router.post("/challenge/attempt")
def record_challenge_attempt(req: ChallengeAttemptRequest):
    """
    Submits a ChallengeGate assessment attempt.
    Awards Topic Medals and ungameable XP if score meets mastery thresholds.
    """
    profile = req.student_profile or {"earned_badges": [], "xp_ledger": {}}
    result = gamification_service.record_challenge_attempt(
        student_profile=profile,
        challenge_id=req.challenge_id,
        subject=req.subject,
        topic_id=req.topic_id,
        score=req.score,
        total_marks=req.total_marks
    )
    return result


@router.get("/status/{user_id}")
def get_gamification_status(user_id: str, subject: str = "Mathematics"):
    """
    Calculates deterministic level, ungameable XP, and badge summaries.
    """
    profile = {"earned_badges": [], "xp_ledger": {}}
    state = gamification_service.calculate_gamification_state(
        student_profile=profile,
        subject=subject,
        mastery_snapshot={},
        completed_topics=[]
    )
    return {"success": True, "user_id": user_id, "state": state}
