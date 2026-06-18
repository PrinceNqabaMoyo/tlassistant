"""
LLM Question Rate Limiter

Tracks per-user usage of LLM-requiring question types (typed, table)
and filters them out of generated question sets when limits are exceeded.

Limits:
- typed (LLM-evaluated): 1 per user per month
- table (open-ended, LLM-evaluated): 1 per user per 3 months

Usage is tracked in Firestore under: users/{user_id}/llm_question_usage/{record_id}
"""

from __future__ import annotations

import datetime
from typing import Any, Dict, List, Optional

# Will be set by the caller (MainApp or route) to avoid circular imports
_firestore_db = None


def init_firestore(db):
    """Call once at app startup to inject the Firestore client."""
    global _firestore_db
    _firestore_db = db


def _get_usage_collection(user_id: str):
    """Get the Firestore collection reference for a user's LLM question usage."""
    if not _firestore_db:
        return None
    return _firestore_db.collection('users').document(user_id).collection('llm_question_usage')


def _count_recent_usage(user_id: str, question_type: str, months: int) -> int:
    """Count how many LLM questions of a given type the user has received in the last N months."""
    coll = _get_usage_collection(user_id)
    if not coll:
        return 0

    cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=months * 30)

    try:
        docs = (
            coll
            .where('question_type', '==', question_type)
            .where('served_at', '>=', cutoff)
            .stream()
        )
        return sum(1 for _ in docs)
    except Exception as e:
        print(f"[llm_rate_limiter] Error counting usage for {user_id}/{question_type}: {e}")
        return 0


def _record_usage(user_id: str, question_type: str, question_id: str):
    """Record that an LLM question was served to the user."""
    coll = _get_usage_collection(user_id)
    if not coll:
        return

    try:
        coll.add({
            'question_type': question_type,
            'question_id': question_id,
            'served_at': datetime.datetime.utcnow(),
        })
    except Exception as e:
        print(f"[llm_rate_limiter] Error recording usage for {user_id}/{question_type}: {e}")


# --- Rate limits ---
_LIMITS = {
    'typed': {'max': 1, 'months': 1},      # 1 typed question per month
    'table': {'max': 1, 'months': 3},       # 1 table (open-ended) question per 3 months
}


def filter_questions_by_llm_limit(
    questions: List[Dict[str, Any]],
    user_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Filter a list of generated questions, removing LLM-requiring types
    that exceed the user's rate limit.

    - If user_id is None or Firestore is unavailable, all LLM questions are removed
      (safe default: no cost).
    - Deterministic question types (mcq, calc, table_wordbank) are never filtered.
    """
    if not questions:
        return questions

    # Types that require LLM evaluation
    llm_types = set(_LIMITS.keys())

    # If no user_id or no Firestore, strip all LLM questions (safe default)
    if not user_id or not _firestore_db:
        return [q for q in questions if q.get('question_type') not in llm_types]

    # Check current usage for each LLM type
    allowed_counts: Dict[str, int] = {}
    for qtype, limit in _LIMITS.items():
        used = _count_recent_usage(user_id, qtype, limit['months'])
        remaining = max(0, limit['max'] - used)
        allowed_counts[qtype] = remaining

    # Filter: keep all deterministic questions, and only keep LLM questions up to the limit
    filtered: List[Dict[str, Any]] = []
    for q in questions:
        qtype = q.get('question_type', '')
        if qtype not in llm_types:
            # Deterministic — always keep
            filtered.append(q)
        elif allowed_counts.get(qtype, 0) > 0:
            # LLM type but still within limit — keep and record
            filtered.append(q)
            allowed_counts[qtype] -= 1
            _record_usage(user_id, qtype, q.get('id', ''))
        # else: over limit — skip this question

    return filtered
