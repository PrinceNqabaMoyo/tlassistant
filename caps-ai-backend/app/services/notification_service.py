"""
Notification Service (Phase D5)
------------------------------
Manages student notification queues, in-app alerts, streak reminders,
assignment dispatch, and WhatsApp formatted broadcast templates.
"""
from __future__ import annotations

import time
import uuid
from typing import Any, Dict, List, Optional

# In-memory notification store for testing and fast local operation
_NOTIFICATIONS_STORE: Dict[str, List[Dict[str, Any]]] = {}


def _make_id(prefix: str = "notif") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


def dispatch_notification(
    user_id: str,
    title: str,
    message: str,
    notif_type: str = "general",
    action_url: Optional[str] = None,
    priority: str = "normal",
) -> Dict[str, Any]:
    """Dispatches an in-app notification to a student's queue."""
    if not user_id:
        raise ValueError("user_id is required")

    notif = {
        "id": _make_id(),
        "user_id": user_id,
        "title": title,
        "message": message,
        "type": notif_type,
        "action_url": action_url or "",
        "priority": priority,
        "read": False,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    if user_id not in _NOTIFICATIONS_STORE:
        _NOTIFICATIONS_STORE[user_id] = []

    _NOTIFICATIONS_STORE[user_id].insert(0, notif)
    return notif


def get_user_notifications(user_id: str, unread_only: bool = False) -> List[Dict[str, Any]]:
    """Retrieves notifications for a user."""
    user_notifs = _NOTIFICATIONS_STORE.get(user_id, [])
    if not user_notifs:
        # Seed welcome/default notifications for interactive demonstration
        _seed_demo_notifications(user_id)
        user_notifs = _NOTIFICATIONS_STORE.get(user_id, [])

    if unread_only:
        return [n for n in user_notifs if not n.get("read", False)]
    return list(user_notifs)


def mark_notification_read(user_id: str, notif_id: str) -> bool:
    """Marks a single notification as read."""
    user_notifs = _NOTIFICATIONS_STORE.get(user_id, [])
    for n in user_notifs:
        if n["id"] == notif_id:
            n["read"] = True
            return True
    return False


def mark_all_read(user_id: str) -> int:
    """Marks all notifications for a user as read."""
    user_notifs = _NOTIFICATIONS_STORE.get(user_id, [])
    count = 0
    for n in user_notifs:
        if not n.get("read", False):
            n["read"] = True
            count += 1
    return count


def format_whatsapp_parent_digest(
    student_name: str,
    subject: str,
    grade: str,
    score: float,
    focus_area: str,
    streak_days: int = 5,
    report_url: str = "https://app.fundile.co.za/reports",
) -> str:
    """Produces a formatted WhatsApp text message for parents."""
    status_emoji = "🌟" if score >= 75 else "📈"
    return (
        f"📊 *Fundile Academic Progress Update*\n\n"
        f"Learner: *{student_name}*\n"
        f"Subject: *Grade {grade} {subject}*\n"
        f"Current Assessment Score: *{score:.1f}%* {status_emoji}\n"
        f"Study Consistency: *{streak_days} Days Active This Week* 🔥\n\n"
        f"🎯 *Key Focus Area*: {focus_area}\n"
        f"Action: Complete the recommended 5-minute targeted micro-drill.\n\n"
        f"🔗 Full Diagnostic PDF Report: {report_url}"
    )


def format_whatsapp_class_broadcast(
    teacher_name: str,
    class_name: str,
    announcement: str,
    join_code: str,
    due_date: Optional[str] = None,
) -> str:
    """Produces a formatted WhatsApp broadcast message for class groups."""
    due_str = f"\n📅 Due Date: *{due_date}*" if due_date else ""
    return (
        f"📚 *Classroom Announcement — {class_name}*\n"
        f"Teacher: *{teacher_name}*\n\n"
        f"{announcement}{due_str}\n\n"
        f"🔑 Class Join Code: *{join_code}*\n"
        f"👉 Open Fundile and enter your code: https://app.fundile.co.za/join"
    )


def _seed_demo_notifications(user_id: str) -> None:
    """Seeds contextual demo notifications for a learner."""
    _NOTIFICATIONS_STORE[user_id] = [
        {
            "id": f"notif_seed_{user_id}_1",
            "user_id": user_id,
            "title": "Streak Reminder 🔥",
            "message": "You have a 5-day streak! Practice 1 problem today to keep your streak bonus.",
            "type": "streak_reminder",
            "action_url": "/workspace",
            "priority": "high",
            "read": False,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
        {
            "id": f"notif_seed_{user_id}_2",
            "user_id": user_id,
            "title": "New Credential Unlocked! 📌",
            "message": "You earned the Subskill Pin for VAT Calculation Prodigy.",
            "type": "badge_unlocked",
            "action_url": "/trophies",
            "priority": "normal",
            "read": False,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
        {
            "id": f"notif_seed_{user_id}_3",
            "user_id": user_id,
            "title": "Class Assignment: Accounting CRJ",
            "message": "Mrs. Ndlovu assigned Grade 10 Cash Receipts Journal Exercise 4.",
            "type": "assignment_due",
            "action_url": "/workspace",
            "priority": "normal",
            "read": False,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
    ]
