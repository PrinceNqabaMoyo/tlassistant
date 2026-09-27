"""
Notifications API Endpoints (Phase D5)
--------------------------------------
Routes for fetching notifications, marking them read, and generating WhatsApp templates.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

from app.services import notification_service

router = APIRouter(prefix="/api/notifications", tags=["Notifications"])


class DispatchNotificationRequest(BaseModel):
    user_id: str = Field(..., description="Recipient student user ID")
    title: str = Field(..., description="Notification title")
    message: str = Field(..., description="Notification body")
    type: str = Field("general", description="streak_reminder, assignment_due, badge_unlocked, trial_warning")
    action_url: Optional[str] = Field(None, description="In-app deep link")
    priority: str = Field("normal", description="normal, high, urgent")


class MarkReadRequest(BaseModel):
    user_id: str
    notif_id: Optional[str] = None
    mark_all: bool = False


class WhatsAppParentDigestRequest(BaseModel):
    student_name: str
    subject: str
    grade: str
    score: float
    focus_area: str
    streak_days: int = 5
    report_url: Optional[str] = "https://app.fundile.co.za/reports"


class WhatsAppBroadcastRequest(BaseModel):
    teacher_name: str
    class_name: str
    announcement: str
    join_code: str
    due_date: Optional[str] = None


@router.get("/{user_id}")
def get_notifications(user_id: str, unread_only: bool = False):
    """Retrieve in-app notifications for a student."""
    notifs = notification_service.get_user_notifications(user_id=user_id, unread_only=unread_only)
    unread_count = len([n for n in notifs if not n.get("read", False)])
    return {
        "success": True,
        "user_id": user_id,
        "unread_count": unread_count,
        "notifications": notifs,
    }


@router.post("/dispatch")
def dispatch_notification(req: DispatchNotificationRequest):
    """Teacher or system dispatches an alert into the student's queue."""
    notif = notification_service.dispatch_notification(
        user_id=req.user_id,
        title=req.title,
        message=req.message,
        notif_type=req.type,
        action_url=req.action_url,
        priority=req.priority,
    )
    return {"success": True, "notification": notif}


@router.post("/mark-read")
def mark_notification_read(req: MarkReadRequest):
    """Marks one or all notifications as read."""
    if req.mark_all:
        count = notification_service.mark_all_read(req.user_id)
        return {"success": True, "marked_count": count}
    elif req.notif_id:
        success = notification_service.mark_notification_read(req.user_id, req.notif_id)
        if not success:
            raise HTTPException(status_code=404, detail="Notification not found")
        return {"success": True, "notif_id": req.notif_id}
    else:
        raise HTTPException(status_code=400, detail="Must provide notif_id or set mark_all=true")


@router.post("/whatsapp-parent-digest")
def generate_parent_digest(req: WhatsAppParentDigestRequest):
    """Generates a formatted WhatsApp digest string for parents."""
    text = notification_service.format_whatsapp_parent_digest(
        student_name=req.student_name,
        subject=req.subject,
        grade=req.grade,
        score=req.score,
        focus_area=req.focus_area,
        streak_days=req.streak_days,
        report_url=req.report_url or "https://app.fundile.co.za/reports",
    )
    return {"success": True, "whatsapp_text": text}


@router.post("/whatsapp-broadcast")
def generate_class_broadcast(req: WhatsAppBroadcastRequest):
    """Generates a formatted WhatsApp announcement string for class groups."""
    text = notification_service.format_whatsapp_class_broadcast(
        teacher_name=req.teacher_name,
        class_name=req.class_name,
        announcement=req.announcement,
        join_code=req.join_code,
        due_date=req.due_date,
    )
    return {"success": True, "whatsapp_text": text}
