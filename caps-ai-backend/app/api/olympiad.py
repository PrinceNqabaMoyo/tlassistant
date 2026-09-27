"""
Olympiad API Router (Layer F)
-----------------------------
Endpoints for checking CAPS gate status, generating problems, grading submissions,
and querying the Technique Library.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

from app.services import olympiad_service, leaderboard_service

router = APIRouter(prefix="/api/olympiad", tags=["Olympiad Track"])


class SubmitOlympiadRequest(BaseModel):
    user_id: str
    problem_id: str
    selected_index: int
    correct_index: int
    division: str = "junior"


@router.get("/gate-status/{user_id}")
def get_gate_status(user_id: str):
    """Checks whether learner meets the CAPS Mathematics prerequisite."""
    return olympiad_service.check_caps_mastery_gate(user_id)


@router.get("/problem")
def get_olympiad_problem(
    category: str = "random",
    division: str = "junior",
    seed: Optional[int] = None,
):
    """Generates a seeded SAMO Round 1 problem."""
    problem = olympiad_service.get_problem(category=category, division=division, seed=seed)
    return {"success": True, "problem": problem}


@router.post("/submit")
def submit_olympiad_answer(req: SubmitOlympiadRequest):
    """Submits answer to an Olympiad problem."""
    result = olympiad_service.submit_answer(
        user_id=req.user_id,
        problem_id=req.problem_id,
        selected_index=req.selected_index,
        correct_index=req.correct_index,
        division=req.division,
    )
    return result


@router.get("/techniques")
def get_techniques():
    """Returns all cards in the Olympiad Technique Library."""
    techniques = olympiad_service.get_technique_library()
    return {"success": True, "techniques": techniques}


class LeaderboardOptInRequest(BaseModel):
    user_id: str
    is_opted_in: bool


@router.get("/leaderboard")
def get_olympiad_leaderboard(
    division: str = "all",
    province: str = "all",
    limit: int = 50,
    user_id: Optional[str] = None
):
    """Retrieves national opt-in rankings filtered by division and province."""
    return leaderboard_service.get_leaderboard(
        division=division,
        province=province,
        limit=limit,
        current_user_id=user_id
    )


@router.post("/leaderboard/opt-in")
def set_leaderboard_opt_in(req: LeaderboardOptInRequest):
    """Toggles learner public visibility on the Olympiad leaderboard."""
    success = leaderboard_service.set_user_opt_in_status(req.user_id, req.is_opted_in)
    return {"success": success, "user_id": req.user_id, "is_opted_in": req.is_opted_in}
