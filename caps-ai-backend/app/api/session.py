"""
Session Audit Endpoints (Phase D1)
Accepts session completion payloads from client telemetry, writes to session_index,
and persists the YAML+Markdown audit file.
"""

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime

from app.services.session_file_writer import write_session_audit
from app.utils.firebase_admin_client import get_firestore_client

router = APIRouter(tags=["Session Audit"])


class SessionEndPayload(BaseModel):
    sessionId: Optional[str] = None
    userId: Optional[str] = "student_guest"
    subject: str = "Mathematics"
    grade: str = "10"
    topic: str = "General Practice"
    subskill: Optional[str] = "Core Concepts"
    score: float = Field(default=1.0, ge=0.0, le=1.0)
    durationSeconds: int = Field(default=60, ge=0)
    misconceptionTags: List[str] = []
    procedureSteps: List[Dict[str, Any]] = []
    cellErrors: List[Dict[str, Any]] = []
    timestamp: Optional[str] = None


@router.post("/end")
async def end_session(payload: SessionEndPayload):
    """
    Finalizes a student practice session, indexing telemetry in Firestore
    and writing the audit .md trail.
    """
    try:
        firestore_db = None
        try:
            firestore_db = get_firestore_client()
        except Exception:
            pass

        session_dict = payload.model_dump()
        if not session_dict.get("sessionId"):
            session_dict["sessionId"] = f"session_{int(datetime.utcnow().timestamp())}"
        if not session_dict.get("timestamp"):
            session_dict["timestamp"] = datetime.utcnow().isoformat()

        result = write_session_audit(
            session_data=session_dict,
            firestore_client=firestore_db,
            storage_bucket=None  # Falls back to local/cloud storage bucket
        )

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to record session audit: {str(e)}")
