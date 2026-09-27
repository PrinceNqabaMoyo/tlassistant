"""
Teacher LMS Cockpit & Class Management Endpoints (Phase D4)
Enables teachers to create classes and generate 6-character join codes,
and students to enter codes and link their progress to the teacher roster.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Dict, Any, List, Optional

from app.services.class_service import (
    create_class,
    join_class_by_code,
    list_classes_for_teacher,
    get_class_roster,
)

router = APIRouter(tags=["Teacher LMS Cockpit"])


class CreateClassPayload(BaseModel):
    teacherId: str
    teacherName: str = "Teacher"
    className: str
    subject: str = "Mathematics"
    grade: str = "10"
    schoolId: Optional[str] = None


class JoinClassPayload(BaseModel):
    studentId: str
    studentName: str = "Learner"
    joinCode: str


@router.post("/create")
async def api_create_class(payload: CreateClassPayload):
    """Creates a new class and returns its unique 6-character join code."""
    try:
        class_doc = create_class(
            teacher_id=payload.teacherId,
            teacher_name=payload.teacherName,
            class_name=payload.className,
            subject=payload.subject,
            grade=payload.grade,
            school_id=payload.schoolId,
        )
        return {
            "status": "success",
            "message": f"Class created! Share join code {class_doc['joinCode']} with your students.",
            "class": class_doc,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create class: {str(e)}")


@router.post("/join")
async def api_join_class(payload: JoinClassPayload):
    """Enrolls a student into a class via 6-character join code."""
    success, result = join_class_by_code(
        student_id=payload.studentId,
        student_name=payload.studentName,
        join_code=payload.joinCode,
    )
    if not success:
        raise HTTPException(status_code=404, detail=result)
    return result


@router.get("/teacher/{teacher_id}")
async def api_get_teacher_classes(teacher_id: str):
    """Retrieves all active classes for a specific teacher or solo tutor."""
    classes = list_classes_for_teacher(teacher_id)
    return {"classes": classes, "count": len(classes)}


@router.get("/{class_id}")
async def api_get_class_details(class_id: str):
    """Retrieves details and student roster for a class."""
    class_doc = get_class_roster(class_id)
    if not class_doc:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_doc
