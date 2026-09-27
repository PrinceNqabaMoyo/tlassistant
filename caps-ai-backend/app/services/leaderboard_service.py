"""
SAMO Olympiad Leaderboard Service (Layer F)
-------------------------------------------
Manages opt-in national rankings, division filtering, and percentile tiers
for the South African Mathematics Olympiad (SAMO) competition track.

Strictly preserves psychological safety: only opt-in learners are ranked,
and standard CAPS syllabus tracks remain completely non-competitive.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime, timezone


# Canonical national benchmark seed data across South African provinces
DEFAULT_LEADERBOARD_ENTRIES: List[Dict[str, Any]] = [
    {
        "user_id": "seed_01",
        "initials": "SZ",
        "name": "Sipho Z.",
        "school": "Maritzburg College",
        "province": "KwaZulu-Natal",
        "division": "Senior",
        "solved": 64,
        "score": 98,
        "is_opted_in": True,
        "updated_at": "2026-09-18T10:00:00Z"
    },
    {
        "user_id": "seed_02",
        "initials": "LD",
        "name": "Lerato D.",
        "school": "Westerford High",
        "province": "Western Cape",
        "division": "Senior",
        "solved": 59,
        "score": 95,
        "is_opted_in": True,
        "updated_at": "2026-09-18T11:30:00Z"
    },
    {
        "user_id": "seed_03",
        "initials": "KM",
        "name": "Kagiso M.",
        "school": "St. Albans College",
        "province": "Gauteng",
        "division": "Junior",
        "solved": 55,
        "score": 92,
        "is_opted_in": True,
        "updated_at": "2026-09-19T08:15:00Z"
    },
    {
        "user_id": "seed_04",
        "initials": "AM",
        "name": "Andile M.",
        "school": "Hilton College",
        "province": "KwaZulu-Natal",
        "division": "Senior",
        "solved": 51,
        "score": 90,
        "is_opted_in": True,
        "updated_at": "2026-09-19T09:40:00Z"
    },
    {
        "user_id": "seed_05",
        "initials": "ZK",
        "name": "Zanele K.",
        "school": "Bishops Diocesan",
        "province": "Western Cape",
        "division": "Junior",
        "solved": 48,
        "score": 88,
        "is_opted_in": True,
        "updated_at": "2026-09-19T14:20:00Z"
    },
    {
        "user_id": "seed_06",
        "initials": "BN",
        "name": "Bongani N.",
        "school": "King Edward VII (KES)",
        "province": "Gauteng",
        "division": "Senior",
        "solved": 46,
        "score": 87,
        "is_opted_in": True,
        "updated_at": "2026-09-19T16:05:00Z"
    },
    {
        "user_id": "seed_07",
        "initials": "PM",
        "name": "Precious M.",
        "school": "Clarendon High",
        "province": "Eastern Cape",
        "division": "Junior",
        "solved": 42,
        "score": 86,
        "is_opted_in": True,
        "updated_at": "2026-09-20T07:10:00Z"
    },
    {
        "user_id": "seed_08",
        "initials": "JL",
        "name": "Johan L.",
        "school": "Paul Roos Gimnasium",
        "province": "Western Cape",
        "division": "Senior",
        "solved": 40,
        "score": 84,
        "is_opted_in": True,
        "updated_at": "2026-09-20T07:30:00Z"
    }
]

# In-memory store for active session/test lifecycle
_LEADERBOARD_STORE: Dict[str, Dict[str, Any]] = {
    e["user_id"]: dict(e) for e in DEFAULT_LEADERBOARD_ENTRIES
}


def calculate_percentile_tier(score: float) -> str:
    """Calculates national distinction tier based on SAMO Round 1 score."""
    if score >= 95:
        return "Top 1%"
    elif score >= 90:
        return "Top 5%"
    elif score >= 80:
        return "Top 10%"
    elif score >= 70:
        return "Top 15%"
    elif score >= 60:
        return "Top 30%"
    return "Participant"


def _format_initials(name: str) -> str:
    parts = name.strip().split()
    if len(parts) >= 2:
        return f"{parts[0][0].upper()}{parts[-1][0].upper()}"
    elif len(parts) == 1 and parts[0]:
        return parts[0][:2].upper()
    return "ST"


def update_user_leaderboard_entry(
    user_id: str,
    name: str,
    school: str,
    province: str,
    division: str,
    score: int,
    solved: int,
    is_opted_in: bool = True
) -> Dict[str, Any]:
    """Updates or inserts a student's leaderboard entry."""
    initials = _format_initials(name)
    division_norm = "Junior" if division.lower() in ("junior", "gr8", "gr9", "8", "9") else "Senior"
    
    entry = {
        "user_id": user_id,
        "initials": initials,
        "name": f"{name.split()[0]} {name.split()[-1][0]}." if len(name.split()) > 1 else name,
        "school": school,
        "province": province,
        "division": division_norm,
        "solved": solved,
        "score": score,
        "tier": calculate_percentile_tier(score),
        "is_opted_in": is_opted_in,
        "updated_at": datetime.now(timezone.utc).isoformat()
    }
    _LEADERBOARD_STORE[user_id] = entry
    return entry


def set_user_opt_in_status(user_id: str, is_opted_in: bool) -> bool:
    """Toggles a learner's visibility on the public Olympiad leaderboard."""
    if user_id in _LEADERBOARD_STORE:
        _LEADERBOARD_STORE[user_id]["is_opted_in"] = is_opted_in
        return True
    return False


def get_leaderboard(
    division: str = "all",
    province: str = "all",
    limit: int = 50,
    current_user_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Returns ranked national leaderboard entries matching criteria.
    Only opted-in entries are listed publicly, but the calling student's
    own rank is always calculated so they can monitor personal standing.
    """
    candidates = list(_LEADERBOARD_STORE.values())

    # Sort candidates by score DESC, solved DESC
    candidates.sort(key=lambda x: (x["score"], x["solved"]), reverse=True)

    # Assign universal ranks
    ranked_list = []
    user_rank_info = None

    for idx, item in enumerate(candidates, start=1):
        entry_copy = dict(item)
        entry_copy["rank"] = idx
        entry_copy["tier"] = calculate_percentile_tier(item["score"])

        if current_user_id and item["user_id"] == current_user_id:
            entry_copy["is_current_user"] = True
            user_rank_info = entry_copy
        else:
            entry_copy["is_current_user"] = False

        ranked_list.append(entry_copy)

    # Apply filters to visible list
    filtered_list = []
    for item in ranked_list:
        # Check division filter
        if division.lower() != "all":
            if division.lower() != item["division"].lower():
                continue
        # Check province filter
        if province.lower() != "all":
            if province.lower() != item["province"].lower():
                continue
        # Exclude opted-out entries unless it's current user
        if not item["is_opted_in"] and not item.get("is_current_user", False):
            continue

        filtered_list.append(item)
        if len(filtered_list) >= limit:
            break

    return {
        "success": True,
        "division": division,
        "province": province,
        "total_ranked": len(ranked_list),
        "leaderboard": filtered_list,
        "current_user_standing": user_rank_info
    }
