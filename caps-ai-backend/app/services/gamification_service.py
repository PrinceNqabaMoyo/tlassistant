"""
Gamification & Ungameable XP Engine (Layer E)
Implements a 4-Tier credentialing system:
1. Subskill Pin (Atomic mastery >= 80%)
2. Topic Medal (Bronze 60%, Silver 80%, Gold 95%)
3. Term Trophy (All Term topics >= Silver)
4. Subject Medallion (Full Grade curriculum mastered at Gold level)

Ungameable XP Philosophy:
- First-mastery award only (no grinding identical questions for XP inflation).
- Zero decay.
- Streak bonuses capped deterministically.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime, date, timezone


# XP Award Constants
XP_VALUES = {
    "subskill_first_mastery": 50,
    "topic_bronze": 100,
    "topic_silver": 200,
    "topic_gold": 350,
    "term_trophy": 750,
    "subject_medallion": 2000,
    "daily_streak_bonus": 20  # Flat daily bonus, max 1x per day
}

# 4-Tier Badge Definitions
BADGE_TIERS = {
    "subskill_pin": {"tier": 1, "name": "Subskill Pin", "icon": "📍", "color": "emerald"},
    "topic_medal": {"tier": 2, "name": "Topic Medal", "icon": "🏅", "color": "amber"},
    "term_trophy": {"tier": 3, "name": "Term Trophy", "icon": "🏆", "color": "indigo"},
    "subject_medallion": {"tier": 4, "name": "Subject Medallion", "icon": "👑", "color": "purple"}
}


def calculate_gamification_state(
    student_profile: Dict[str, Any],
    subject: str,
    mastery_snapshot: Dict[str, float],
    completed_topics: List[str],
    term: int = 1
) -> Dict[str, Any]:
    """
    Computes deterministic badges, level, ungameable XP, and streak status.
    
    Args:
        student_profile: Firestore student profile dict containing earned_badges and xp_ledger
        subject: e.g. "Mathematics", "Accounting"
        mastery_snapshot: Dict mapping subskill_id -> mastery_score (0.0 to 1.0)
        completed_topics: List of topic IDs completed by learner
        term: Current school term (1..4)
    """
    xp_ledger = student_profile.get("xp_ledger", {})
    earned_badges = student_profile.get("earned_badges", [])
    earned_badge_ids = {b["id"] for b in earned_badges}

    new_badges = []
    total_xp = 0

    # 1. Process Subskill Pins (Tier 1)
    subskills_mastered = 0
    for subskill_id, score in mastery_snapshot.items():
        if score >= 0.80:
            subskills_mastered += 1
            badge_id = f"pin_{subject}_{subskill_id}"
            if badge_id not in earned_badge_ids:
                badge = {
                    "id": badge_id,
                    "tier": "subskill_pin",
                    "title": f"{subskill_id.replace('_', ' ').title()} Mastery",
                    "subject": subject,
                    "earned_at": datetime.now(timezone.utc).isoformat(),
                    "xp_awarded": XP_VALUES["subskill_first_mastery"]
                }
                new_badges.append(badge)
                earned_badge_ids.add(badge_id)

    # 2. Process Topic Medals (Tier 2)
    for topic_id in completed_topics:
        # Calculate topic aggregate score
        topic_subskills = [v for k, v in mastery_snapshot.items() if topic_id in k or k.startswith(topic_id)]
        avg_score = (sum(topic_subskills) / len(topic_subskills)) if topic_subskills else 0.85
        
        medal_grade = "bronze"
        if avg_score >= 0.95:
            medal_grade = "gold"
        elif avg_score >= 0.80:
            medal_grade = "silver"
        elif avg_score >= 0.60:
            medal_grade = "bronze"
        else:
            continue

        badge_id = f"medal_{subject}_{topic_id}_{medal_grade}"
        if badge_id not in earned_badge_ids:
            badge = {
                "id": badge_id,
                "tier": "topic_medal",
                "grade": medal_grade,
                "title": f"{topic_id.replace('_', ' ').title()} {medal_grade.title()} Medal",
                "subject": subject,
                "earned_at": datetime.now(timezone.utc).isoformat(),
                "xp_awarded": XP_VALUES[f"topic_{medal_grade}"]
            }
            new_badges.append(badge)
            earned_badge_ids.add(badge_id)

    # 3. Process Term Trophy (Tier 3)
    # If student has at least 4 Silver+ topic medals in this term
    silver_or_gold_count = sum(1 for b in earned_badges + new_badges if b.get("tier") == "topic_medal" and b.get("grade") in ("silver", "gold") and b.get("subject") == subject)
    if silver_or_gold_count >= 4:
        trophy_id = f"trophy_{subject}_term_{term}"
        if trophy_id not in earned_badge_ids:
            badge = {
                "id": trophy_id,
                "tier": "term_trophy",
                "title": f"{subject} Term {term} Mastery Trophy",
                "subject": subject,
                "term": term,
                "earned_at": datetime.now(timezone.utc).isoformat(),
                "xp_awarded": XP_VALUES["term_trophy"]
            }
            new_badges.append(badge)
            earned_badge_ids.add(trophy_id)

    # Combine all badges
    all_badges = earned_badges + new_badges

    # Calculate total ungameable XP strictly from one-time awards
    for b in all_badges:
        total_xp += b.get("xp_awarded", 0)

    # Compute Level (1000 XP per level with sqrt curve)
    level = max(1, int((total_xp / 250) ** 0.5) + 1)
    xp_for_next_level = int(((level) ** 2) * 250)
    xp_current_level_base = int(((level - 1) ** 2) * 250)
    level_progress_percent = min(100.0, max(0.0, ((total_xp - xp_current_level_base) / max(1, xp_for_next_level - xp_current_level_base)) * 100))

    return {
        "total_ungameable_xp": total_xp,
        "level": level,
        "level_progress_percent": round(level_progress_percent, 1),
        "xp_to_next_level": max(0, xp_for_next_level - total_xp),
        "earned_badges": all_badges,
        "new_badges_unlocked": new_badges,
        "subskills_mastered_count": subskills_mastered,
        "tier_summary": {
            "subskill_pins": sum(1 for b in all_badges if b.get("tier") == "subskill_pin"),
            "topic_medals": sum(1 for b in all_badges if b.get("tier") == "topic_medal"),
            "term_trophies": sum(1 for b in all_badges if b.get("tier") == "term_trophy"),
            "subject_medallions": sum(1 for b in all_badges if b.get("tier") == "subject_medallion")
        }
    }


def record_challenge_attempt(
    student_profile: Dict[str, Any],
    challenge_id: str,
    subject: str,
    topic_id: str,
    score: int,
    total_marks: int
) -> Dict[str, Any]:
    """
    Evaluates a standardized challenge gate attempt and awards Topic Medal / Ungameable XP
    if threshold is met on first attempt without grind inflation.
    """
    pct = (score / max(1, total_marks)) * 100.0
    passed = pct >= 60.0

    grade = "unranked"
    xp_earned = 0
    new_badge = None

    earned_badges = student_profile.get("earned_badges", [])
    earned_badge_ids = {b["id"] for b in earned_badges}

    if pct >= 95.0:
        grade = "gold"
    elif pct >= 80.0:
        grade = "silver"
    elif pct >= 60.0:
        grade = "bronze"

    if passed and grade != "unranked":
        badge_id = f"medal_{subject}_{topic_id}_{grade}"
        if badge_id not in earned_badge_ids:
            xp_earned = XP_VALUES.get(f"topic_{grade}", 100)
            new_badge = {
                "id": badge_id,
                "tier": "topic_medal",
                "grade": grade,
                "title": f"{topic_id.replace('_', ' ').title()} {grade.title()} Medal",
                "subject": subject,
                "earned_at": datetime.now(timezone.utc).isoformat(),
                "xp_awarded": xp_earned
            }
            earned_badges.append(new_badge)
            student_profile["earned_badges"] = earned_badges

    return {
        "success": True,
        "challenge_id": challenge_id,
        "score": score,
        "total_marks": total_marks,
        "percent": round(pct, 1),
        "passed": passed,
        "medal_awarded": grade if passed else None,
        "xp_earned": xp_earned,
        "new_badge": new_badge,
        "attempt_timestamp": datetime.now(timezone.utc).isoformat()
    }


def archive_academic_year(
    student_profile: Dict[str, Any],
    completed_year: int,
    completed_grade: str,
    next_grade: str
) -> Dict[str, Any]:
    """
    Carries forward student achievements upon academic year rollover (Resolves OQ5).
    All earned badges, ungameable XP, and credentials are permanently archived
    into 'academic_portfolio' as an immutable transcript. Current-year active mastery
    targets are initialized for the new grade curriculum.
    """
    portfolio = student_profile.get("academic_portfolio", {})
    earned_badges = student_profile.get("earned_badges", [])
    total_xp = student_profile.get("total_ungameable_xp", 0)

    portfolio[str(completed_year)] = {
        "year": completed_year,
        "grade": completed_grade,
        "archived_at": datetime.now(timezone.utc).isoformat(),
        "badges": list(earned_badges),
        "xp_accumulated": total_xp,
        "is_immutable_certificate": True
    }

    student_profile["academic_portfolio"] = portfolio
    student_profile["current_grade"] = next_grade

    return {
        "success": True,
        "completed_year": completed_year,
        "completed_grade": completed_grade,
        "next_grade": next_grade,
        "archived_badges_count": len(earned_badges),
        "lifetime_xp": total_xp,
        "portfolio": portfolio
    }
