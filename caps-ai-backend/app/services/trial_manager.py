"""
Fundile Trial & Subscription Manager (Layer D — Phase D2)

Governs user lifecycle, 14-day free trial tracking, hard paywall gates,
and feature entitlements across Trial, Standard, Pro, and School tiers.
"""

from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Optional, Tuple

TRIAL_DURATION_DAYS = 14

TIER_PERMISSIONS = {
    "trial": {
        "modes": ["scaffold", "practice"],
        "max_hints_tier": 2,
        "allow_assessments": False,
        "allow_socratic_agent": False,
        "allow_progress_map": True,
        "allow_pdf_reports": True,
        "allow_simulearn": True,
        "allow_class_roster": True,
    },
    "trial_expired": {
        "modes": ["scaffold"], # read/preview only
        "max_hints_tier": 1,
        "allow_assessments": False,
        "allow_socratic_agent": False,
        "allow_progress_map": False,
        "allow_pdf_reports": False,
        "allow_simulearn": False,
        "allow_class_roster": False,
    },
    "standard": {
        "modes": ["scaffold", "practice", "assessment"],
        "max_hints_tier": 2,
        "allow_assessments": True,
        "allow_socratic_agent": False,
        "allow_progress_map": True,
        "allow_pdf_reports": True,
        "allow_simulearn": True,
        "allow_class_roster": True,
    },
    "pro": {
        "modes": ["scaffold", "practice", "assessment"],
        "max_hints_tier": 4,
        "allow_assessments": True,
        "allow_socratic_agent": True,
        "allow_progress_map": True,
        "allow_pdf_reports": True,
        "allow_simulearn": True,
        "allow_class_roster": True,
    },
    "school": {
        "modes": ["scaffold", "practice", "assessment"],
        "max_hints_tier": 4,
        "allow_assessments": True,
        "allow_socratic_agent": True,
        "allow_progress_map": True,
        "allow_pdf_reports": True,
        "allow_simulearn": True,
        "allow_class_roster": True,
        "allow_teacher_dashboard": True,
        "allow_assignment_builder": True,
    },
}


def parse_datetime(dt_str: Optional[str]) -> datetime:
    """Parse ISO datetime string safely, defaulting to UTC now."""
    if not dt_str:
        return datetime.now(timezone.utc)
    try:
        # Handle 'Z' suffix
        if dt_str.endswith("Z"):
            dt_str = dt_str[:-1] + "+00:00"
        return datetime.fromisoformat(dt_str)
    except Exception:
        return datetime.now(timezone.utc)


def compute_trial_status(profile: Optional[Dict[str, Any]] = None, now: Optional[datetime] = None) -> Dict[str, Any]:
    """
    Computes active tier, days remaining, expiration status, and feature flags
    for a given user profile.
    """
    if now is None:
        now = datetime.now(timezone.utc)

    if not profile:
        profile = {}

    current_tier = profile.get("subscription_tier", "trial").lower()
    
    # Check paid subscriptions
    if current_tier in ["standard", "pro", "school"]:
        ends_at_str = profile.get("subscription_ends_at")
        if ends_at_str:
            ends_at = parse_datetime(ends_at_str)
            if now > ends_at:
                current_tier = "trial_expired"
            else:
                days_left = max(0, int((ends_at - now).total_seconds() // 86400))
                perms = TIER_PERMISSIONS.get(current_tier, TIER_PERMISSIONS["standard"])
                return {
                    "tier": current_tier,
                    "is_active": True,
                    "is_trial": False,
                    "trial_expired": False,
                    "days_remaining": days_left,
                    "permissions": perms,
                    "profile_persists": True,
                }
        else:
            # Active lifetime / ongoing subscription
            perms = TIER_PERMISSIONS.get(current_tier, TIER_PERMISSIONS["standard"])
            return {
                "tier": current_tier,
                "is_active": True,
                "is_trial": False,
                "trial_expired": False,
                "days_remaining": 999,
                "permissions": perms,
                "profile_persists": True,
            }

    # If already explicitly flagged expired
    if current_tier == "trial_expired":
        return {
            "tier": "trial_expired",
            "is_active": False,
            "is_trial": False,
            "trial_expired": True,
            "days_remaining": 0,
            "permissions": TIER_PERMISSIONS["trial_expired"],
            "profile_persists": True,
        }

    # Default / Trial evaluation
    started_at_str = profile.get("trial_started_at") or profile.get("created_at")
    started_at = parse_datetime(started_at_str) if started_at_str else now
    
    ends_at_str = profile.get("trial_ends_at")
    if ends_at_str:
        ends_at = parse_datetime(ends_at_str)
    else:
        ends_at = started_at + timedelta(days=TRIAL_DURATION_DAYS)

    remaining_seconds = (ends_at - now).total_seconds()
    
    if remaining_seconds <= 0:
        return {
            "tier": "trial_expired",
            "is_active": False,
            "is_trial": False,
            "trial_expired": True,
            "days_remaining": 0,
            "trial_started_at": started_at.isoformat(),
            "trial_ends_at": ends_at.isoformat(),
            "permissions": TIER_PERMISSIONS["trial_expired"],
            "profile_persists": True,
        }
    
    days_left = max(1, int((remaining_seconds + 86399) // 86400))
    return {
        "tier": "trial",
        "is_active": True,
        "is_trial": True,
        "trial_expired": False,
        "days_remaining": days_left,
        "trial_started_at": started_at.isoformat(),
        "trial_ends_at": ends_at.isoformat(),
        "permissions": TIER_PERMISSIONS["trial"],
        "profile_persists": True,
    }


def check_feature_access(profile: Optional[Dict[str, Any]], requested_action: str) -> Tuple[bool, Optional[Dict[str, Any]]]:
    """
    Validates whether the user's tier permits a given action (e.g. 'assessment', 'socratic_agent').
    Returns (True, None) if permitted, or (False, error_payload) if blocked.
    """
    status = compute_trial_status(profile)
    tier = status["tier"]
    perms = status["permissions"]

    if status["trial_expired"]:
        if requested_action in ["assessment", "practice", "socratic_agent", "challenge"]:
            return False, {
                "error": "TRIAL_EXPIRED",
                "code": 403,
                "message": "Your 14-day free trial has expired. Subscribe to Fundile Standard or Pro to unlock assessments and complete curriculum progress.",
                "tier": tier,
                "days_remaining": 0,
                "upgrade_url": "/subscribe",
            }

    if requested_action == "assessment" and not perms.get("allow_assessments", False):
        return False, {
            "error": "TIER_RESTRICTED",
            "code": 403,
            "message": "Assessment Mode requires a Fundile Standard or Pro subscription. Complete practice in Scaffold/Practice mode or upgrade your account.",
            "tier": tier,
            "upgrade_url": "/subscribe",
        }

    if requested_action == "socratic_agent" and not perms.get("allow_socratic_agent", False):
        return False, {
            "error": "PRO_TIER_REQUIRED",
            "code": 403,
            "message": "The live Socratic AI Tutor is exclusive to Fundile Pro. Standard deterministic hints (Tiers 1-2) are active for your account.",
            "tier": tier,
            "upgrade_url": "/subscribe",
        }

    return True, None


def validate_school_license(license_key: str) -> Tuple[bool, Optional[str], Optional[Dict[str, Any]]]:
    """
    Validates institutional school license keys issued via manual invoice / school procurement.
    Supports format:
      - 'SCH-YYYY-XXXX-XXXX' (e.g. 'SCH-2026-CAPS-9081')
      - 'FUNDILE-SCH-XXXX' (e.g. 'FUNDILE-SCH-8821')
    """
    key = str(license_key or "").strip().upper()
    if not key:
        return False, "License key is required", None

    parts = key.split("-")
    if (len(parts) == 4 and parts[0] == "SCH") or (len(parts) == 3 and parts[0] == "FUNDILE" and parts[1] == "SCH"):
        return True, None, {
            "license_key": key,
            "tier": "school",
            "duration_days": 365,
            "status": "valid",
            "type": "institutional_annual_license",
        }
    return False, "Invalid school license format. Expected SCH-YYYY-XXXX-XXXX or FUNDILE-SCH-XXXX", None


def activate_school_license(profile: Dict[str, Any], license_key: str, school_name: str = "") -> Tuple[bool, Dict[str, Any]]:
    """
    Activates institutional school license on a user/school profile for 365 days.
    """
    valid, err, details = validate_school_license(license_key)
    if not valid:
        return False, {"error": err, "code": 400}

    now = datetime.now(timezone.utc)
    ends_at = now + timedelta(days=details["duration_days"])

    profile["subscription_tier"] = "school"
    profile["subscription_ends_at"] = ends_at.isoformat()
    profile["school_license_key"] = license_key
    if school_name:
        profile["school_name"] = school_name

    status = compute_trial_status(profile, now=now)
    return True, {
        "success": True,
        "message": "School license activated successfully for 365 days.",
        "status": status,
        "school_license": details,
    }
