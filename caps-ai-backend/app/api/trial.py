"""
Trial & Subscription Management Endpoints (Phase D2)
Exposes endpoints for computing user subscription/trial status,
enforcing 403 TRIAL_EXPIRED gates, and dev/testing tier toggles.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Dict, Any, Optional

from app.services.trial_manager import compute_trial_status, check_feature_access
from app.utils.firebase_admin_client import get_firestore_client

router = APIRouter(tags=["Trial & Subscription"])


class CheckAccessPayload(BaseModel):
    userId: Optional[str] = "student_guest"
    requested_action: str = "practice"
    profile: Optional[Dict[str, Any]] = None


class MockTierPayload(BaseModel):
    userId: Optional[str] = "student_guest"
    tier: str = "trial"  # "trial", "trial_expired", "standard", "pro", "school"
    days_left: Optional[int] = None


@router.get("/status")
async def get_trial_status(
    userId: Optional[str] = Query(default="student_guest"),
    tier: Optional[str] = Query(default=None),
    days_remaining: Optional[int] = Query(default=None)
):
    """
    Returns current trial and subscription entitlement status.
    Supports query-based override for instant UI testing.
    """
    profile: Dict[str, Any] = {}
    
    # Try fetching from Firestore if client available
    if userId and userId != "student_guest":
        try:
            db = get_firestore_client()
            doc = db.collection("students").document(userId).collection("profile").document("current").get()
            if doc.exists:
                profile = doc.to_dict() or {}
        except Exception:
            pass

    # Apply overrides if passed (e.g. from developer testing console)
    if tier:
        profile["subscription_tier"] = tier
    if days_remaining is not None and tier == "trial":
        from datetime import datetime, timezone, timedelta
        now = datetime.now(timezone.utc)
        profile["trial_ends_at"] = (now + timedelta(days=days_remaining)).isoformat()

    status = compute_trial_status(profile)
    return status


@router.post("/check-access")
async def verify_feature_access(payload: CheckAccessPayload):
    """
    Validates whether the user's tier permits a requested action (e.g. 'assessment').
    Returns 200 with permitted status, or 403 TRIAL_EXPIRED / TIER_RESTRICTED.
    """
    profile = payload.profile or {}
    
    # If no profile was provided, check firestore
    if not profile and payload.userId and payload.userId != "student_guest":
        try:
            db = get_firestore_client()
            doc = db.collection("students").document(payload.userId).collection("profile").document("current").get()
            if doc.exists:
                profile = doc.to_dict() or {}
        except Exception:
            pass

    allowed, error_payload = check_feature_access(profile, payload.requested_action)
    if not allowed and error_payload:
        raise HTTPException(status_code=error_payload.get("code", 403), detail=error_payload)
    
    return {
        "status": "permitted",
        "action": payload.requested_action,
        "allowed": True,
    }


@router.post("/mock-upgrade")
async def mock_tier_upgrade(payload: MockTierPayload):
    """
    Developer/Testing endpoint: instantly sets or toggles subscription tier
    in Firestore or returns mock profile for demo testing.
    """
    from datetime import datetime, timezone, timedelta
    now = datetime.now(timezone.utc)
    
    days = payload.days_left if payload.days_left is not None else (14 if payload.tier == "trial" else 30)
    ends_at = (now + timedelta(days=days)).isoformat() if payload.tier != "trial_expired" else (now - timedelta(days=1)).isoformat()

    profile_update = {
        "subscription_tier": payload.tier,
        "subscription_ends_at": ends_at if payload.tier in ["standard", "pro", "school"] else None,
        "trial_started_at": (now - timedelta(days=2)).isoformat() if payload.tier != "trial_expired" else (now - timedelta(days=16)).isoformat(),
        "trial_ends_at": ends_at if payload.tier in ["trial", "trial_expired"] else None,
    }

    if payload.userId and payload.userId != "student_guest":
        try:
            db = get_firestore_client()
            db.collection("students").document(payload.userId).collection("profile").document("current").set(profile_update, merge=True)
        except Exception:
            pass

    computed = compute_trial_status(profile_update)
    return {
        "message": f"Tier updated to {payload.tier}",
        "profile": profile_update,
        "status": computed,
    }


class SchoolActivationPayload(BaseModel):
    userId: Optional[str] = "teacher_guest"
    license_key: str
    school_name: Optional[str] = "South African High School"


@router.post("/school/activate")
async def activate_school_plan(payload: SchoolActivationPayload):
    """
    Activates institutional school license code issued via school invoice/procurement.
    """
    from app.services.trial_manager import activate_school_license

    profile = {}
    if payload.userId and payload.userId != "teacher_guest":
        try:
            db = get_firestore_client()
            doc = db.collection("teachers").document(payload.userId).collection("profile").document("current").get()
            if doc.exists:
                profile = doc.to_dict() or {}
        except Exception:
            pass

    success, result = activate_school_license(profile, payload.license_key, payload.school_name or "")
    if not success:
        raise HTTPException(status_code=400, detail=result)

    if payload.userId and payload.userId != "teacher_guest":
        try:
            db = get_firestore_client()
            db.collection("teachers").document(payload.userId).collection("profile").document("current").set(profile, merge=True)
        except Exception:
            pass

    return result

