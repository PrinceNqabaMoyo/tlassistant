import os
import json
import re
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone, timedelta

from app.services.llm_provider import get_llm_provider, BaseLLMProvider
from app.services.student_model import StudentModel

# --- Singleton state ---
_llm_provider: Optional[BaseLLMProvider] = None
_student_model: Optional[StudentModel] = None


# --- Orchestrator Prompt ---

ORCHESTRATOR_SYSTEM_PROMPT = """You are a warm, encouraging learning coach for South African students following the CAPS curriculum.
You have a cross-subject view of the student's progress. Your job is to:

1. Generate a concise, actionable weekly study plan.
2. Write a short, personalized encouragement message.
3. Identify when a student should seek help from their class teacher.

Rules:
- Be encouraging, never discouraging.
- Prioritize topics the student is struggling with.
- Suggest spaced repetition for problems older than 24 hours.
- Flag topics where the student has 3+ consecutive incorrect answers as "needs teacher help".
- Keep the study plan to 3-5 items max — students get overwhelmed.
- Suggest time blocks (15-30 min per item).

Respond in this exact JSON format:
{
  "encouragement": "Short personalized message (1-2 sentences)",
  "plan": [
    {
      "subject": "...",
      "grade": "...",
      "topic": "...",
      "subskill": "...",
      "action": "retry" | "review" | "new",
      "reason": "struggling" | "streak_broken" | "mastery_low" | "spaced_repetition",
      "duration_minutes": 15-30,
      "seek_teacher_help": true | false
    }
  ],
  "teacher_escalation": [
    {
      "subject": "...",
      "topic": "...",
      "reason": "..."
    }
  ]
}
"""


def initialize_orchestrator(firestore_db=None):
    global _student_model, _llm_provider
    _student_model = StudentModel(firestore_db) if firestore_db else None
    _llm_provider = get_llm_provider()
    print("Orchestrator initialized.")


def _get_provider() -> BaseLLMProvider:
    global _llm_provider
    if _llm_provider is None:
        _llm_provider = get_llm_provider()
    return _llm_provider


# --- Deterministic analysis ---

def _analyze_student(user_id: str) -> Dict[str, Any]:
    """Deterministic analysis of student data. Returns raw findings."""
    if not _student_model or not user_id:
        return {"mastery": [], "struggling": [], "broken_streaks": []}

    mastery = _student_model.get_all_mastery_summary(user_id)
    struggling = _student_model.get_struggling_problems_for_spaced_repetition(
        user_id, min_age_hours=24, max_records=10
    )
    broken_streaks = _student_model.get_streaks_needing_attention(user_id, max_incorrect=3)

    # Filter to actionable items
    low_mastery = [m for m in mastery if m.get("mastery_score", 1.0) < 0.6 and m.get("submissions", 0) >= 2]
    low_mastery.sort(key=lambda x: x["mastery_score"])

    return {
        "mastery": low_mastery,
        "struggling": struggling,
        "broken_streaks": broken_streaks,
    }


def _build_orchestrator_context(analysis: Dict[str, Any]) -> str:
    """Builds a compact text summary for the LLM prompt."""
    lines = ["## Student Progress Summary", ""]

    if analysis["broken_streaks"]:
        lines.append("### Broken streaks (3+ wrong in a row)")
        for s in analysis["broken_streaks"][:5]:
            lines.append(
                f"- {s['subject']} {s['grade']} — {s['topic']} ({s['subskill']}): "
                f"{s['consecutive_incorrect']} consecutive incorrect"
            )
        lines.append("")

    if analysis["struggling"]:
        lines.append("### Struggling problems (not retried in 24h+)")
        for p in analysis["struggling"][:5]:
            lines.append(
                f"- {p.get('subject', '?')} {p.get('grade', '?')} — {p.get('topic', '?')} "
                f"({p.get('subskill', '?')}): {p.get('reason', '')}"
            )
        lines.append("")

    if analysis["mastery"]:
        lines.append("### Low mastery areas (< 60%)")
        for m in analysis["mastery"][:10]:
            lines.append(
                f"- {m['subject']} {m['grade']} — {m['topic']} ({m['subskill']}): "
                f"{m['mastery_score']:.0%} over {m['submissions']} attempts"
            )
        lines.append("")

    if not any(analysis.values()):
        lines.append("Student is doing well across all subjects. Suggest reviewing recent topics.")

    return "\n".join(lines)


# --- Main orchestrator entry points ---

def generate_study_plan(user_id: str) -> Dict[str, Any]:
    """Generates a weekly study plan for the student.
    Returns the plan document and saves it to Firestore."""
    if not _student_model or not user_id:
        return {"status": "noop", "reason": "no_db_or_user"}

    analysis = _analyze_student(user_id)

    # If nothing is wrong, return a lightweight "keep going" plan
    if not any(analysis.values()):
        plan = {
            "encouragement": "You're on fire! Keep up the great work across all your subjects.",
            "plan": [
                {
                    "subject": "general",
                    "grade": "",
                    "topic": "general review",
                    "subskill": "",
                    "action": "review",
                    "reason": "maintenance",
                    "duration_minutes": 20,
                    "seek_teacher_help": False,
                }
            ],
            "teacher_escalation": [],
        }
        _student_model.record_study_plan(user_id, plan["plan"], plan["encouragement"])
        return {"status": "ok", "plan": plan, "source": "deterministic"}

    # Build LLM prompt
    context = _build_orchestrator_context(analysis)
    prompt = ORCHESTRATOR_SYSTEM_PROMPT + "\n\n" + context + "\n\nNow generate the JSON response."

    provider = _get_provider()
    try:
        raw = provider.invoke(messages=[{"role": "user", "content": prompt}])
        # Extract JSON from the response
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            plan = json.loads(match.group(0))
        else:
            plan = json.loads(raw)
    except Exception as e:
        # Fallback deterministic plan if LLM fails
        plan = _fallback_plan(analysis)
        plan["_llm_error"] = str(e)

    # Save to Firestore
    _student_model.record_study_plan(user_id, plan.get("plan", []), plan.get("encouragement", ""))

    # Create notifications for spaced repetition items
    _create_reminder_notifications(user_id, analysis)

    return {"status": "ok", "plan": plan, "source": "llm"}


def check_and_notify(user_id: str) -> Dict[str, Any]:
    """Daily check. Returns notifications that should be shown to the student.
    Intended to be called by a scheduler or when the student opens the app."""
    if not _student_model or not user_id:
        return {"status": "noop", "reason": "no_db_or_user", "notifications": []}

    notifications = []

    # 1. Spaced repetition reminders
    struggling = _student_model.get_struggling_problems_for_spaced_repetition(
        user_id, min_age_hours=24, max_records=5
    )
    for p in struggling:
        notifications.append({
            "type": "spaced_repetition",
            "subject": p.get("subject", ""),
            "grade": p.get("grade", ""),
            "topic": p.get("topic", ""),
            "subskill": p.get("subskill", ""),
            "message": (
                f"You struggled with {p.get('topic', 'this topic')} "
                f"({p.get('subskill', '')}) in {p.get('subject', '')}. "
                f"Repetition builds mastery — give it another try!"
            ),
            "created_at": datetime.now(timezone.utc).isoformat(),
        })

    # 2. Broken streak alerts
    broken = _student_model.get_streaks_needing_attention(user_id, max_incorrect=3)
    for s in broken:
        notifications.append({
            "type": "streak_alert",
            "subject": s["subject"],
            "grade": s["grade"],
            "topic": s["topic"],
            "subskill": s["subskill"],
            "message": (
                f"You've had {s['consecutive_incorrect']} wrong answers in a row on "
                f"{s['topic']} ({s['subskill']}). Take a breath, review the concept, and try again."
            ),
            "created_at": datetime.now(timezone.utc).isoformat(),
        })

    # 3. Teacher escalation
    broken_for_escalation = [s for s in broken if s["consecutive_incorrect"] >= 5]
    for s in broken_for_escalation:
        notifications.append({
            "type": "teacher_escalation",
            "subject": s["subject"],
            "grade": s["grade"],
            "topic": s["topic"],
            "subskill": s["subskill"],
            "message": (
                f"You've attempted {s['topic']} ({s['subskill']}) many times without success. "
                f"Consider asking your class teacher for extra help with this topic."
            ),
            "created_at": datetime.now(timezone.utc).isoformat(),
        })

    # Write notifications to Firestore
    for n in notifications:
        _student_model._user_ref(user_id).collection("notifications").add(n)

    return {"status": "ok", "notifications": notifications}


# --- Helpers ---

def _fallback_plan(analysis: Dict[str, Any]) -> Dict[str, Any]:
    """Deterministic fallback if the LLM fails to produce valid JSON."""
    plan_items = []
    teacher_escalation = []

    for s in analysis.get("broken_streaks", [])[:3]:
        plan_items.append({
            "subject": s["subject"],
            "grade": s["grade"],
            "topic": s["topic"],
            "subskill": s["subskill"],
            "action": "retry",
            "reason": "streak_broken",
            "duration_minutes": 20,
            "seek_teacher_help": s["consecutive_incorrect"] >= 5,
        })
        if s["consecutive_incorrect"] >= 5:
            teacher_escalation.append({
                "subject": s["subject"],
                "topic": s["topic"],
                "reason": f"{s['consecutive_incorrect']} consecutive incorrect answers",
            })

    for p in analysis.get("struggling", [])[:3]:
        if len(plan_items) >= 5:
            break
        plan_items.append({
            "subject": p.get("subject", ""),
            "grade": p.get("grade", ""),
            "topic": p.get("topic", ""),
            "subskill": p.get("subskill", ""),
            "action": "retry",
            "reason": "spaced_repetition",
            "duration_minutes": 15,
            "seek_teacher_help": False,
        })

    for m in analysis.get("mastery", [])[:3]:
        if len(plan_items) >= 5:
            break
        plan_items.append({
            "subject": m["subject"],
            "grade": m["grade"],
            "topic": m["topic"],
            "subskill": m["subskill"],
            "action": "review",
            "reason": "mastery_low",
            "duration_minutes": 20,
            "seek_teacher_help": False,
        })

    return {
        "encouragement": "Keep pushing — every attempt makes you stronger!",
        "plan": plan_items,
        "teacher_escalation": teacher_escalation,
    }


def _create_reminder_notifications(user_id: str, analysis: Dict[str, Any]) -> None:
    """Creates Firestore notification docs for the most critical items."""
    if not _student_model or not user_id:
        return

    # Only create notifications for the top 3 most critical items
    critical = []
    critical.extend(analysis.get("broken_streaks", [])[:2])
    critical.extend(analysis.get("struggling", [])[:2])

    for item in critical:
        if "consecutive_incorrect" in item:
            msg = (
                f"Reminder: {item['topic']} ({item['subskill']}) in {item['subject']} "
                f"needs attention. You've had {item['consecutive_incorrect']} wrong in a row."
            )
        else:
            msg = (
                f"Reminder: Retry {item.get('topic', 'this topic')} in {item.get('subject', '')}. "
                f"Repetition builds mastery!"
            )

        _student_model._user_ref(user_id).collection("notifications").add({
            "type": "study_reminder",
            "message": msg,
            "subject": item.get("subject", ""),
            "grade": item.get("grade", ""),
            "topic": item.get("topic", ""),
            "subskill": item.get("subskill", ""),
            "created_at": datetime.now(timezone.utc),
            "read": False,
        })
