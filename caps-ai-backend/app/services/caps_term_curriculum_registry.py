"""Canonical CAPS Term Curriculum Registry.

Defines authentic South African CAPS Annual Teaching Plan (ATP) Term distribution
(Terms 1, 2, 3, 4) for all 476 topics across all 30 curriculum suites (Grades 7–12 across all 10 subjects).
Enforces Rule 20 (Term & Calendar Metadata) and Rule 26b (Zero-Meta Invariant).
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_REGISTRY_JSON_PATH = Path(__file__).parent / "caps_term_registry_data.json"

_ALL_TOPIC_RECORDS: List[Dict[str, Any]] = []
_BY_SUBJECT_GRADE: Dict[Tuple[str, str], List[Dict[str, Any]]] = {}
_BY_SUBJECT_GRADE_TERM: Dict[Tuple[str, str, int], List[Dict[str, Any]]] = {}
_BY_TOPIC_LOOKUP: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
_BY_KEY_LOOKUP: Dict[str, Dict[str, Any]] = {}


def _normalize_subject(subject: str) -> str:
    s = str(subject or "").lower().replace("_", " ").replace("-", " ").strip()
    if "acc" in s:
        return "Accounting"
    if "bus" in s:
        return "Business Studies"
    if "ems" in s or "economic" in s:
        return "Economic and Management Sciences"
    if "lit" in s or "mathslit" in s:
        return "Mathematical Literacy"
    if "tech" in s:
        return "Technical Mathematics"
    if "phys" in s:
        return "Physical Sciences"
    if "life" in s or "bio" in s:
        return "Life Sciences"
    if "nat" in s:
        return "Natural Sciences"
    if "math" in s:
        return "Mathematics"
    return "Mathematics"


def _normalize_grade(grade: str | int) -> str:
    cleaned = "".join(ch for ch in str(grade) if ch.isdigit())
    return cleaned if cleaned else "10"


def _normalize_topic_name(topic: str) -> str:
    return str(topic or "").lower().replace("_", " ").replace("-", " ").strip()


def _init_registry():
    global _ALL_TOPIC_RECORDS
    if _ALL_TOPIC_RECORDS:
        return

    if not _REGISTRY_JSON_PATH.exists():
        # Fallback minimal init
        return

    try:
        with open(_REGISTRY_JSON_PATH, "r", encoding="utf-8") as f:
            records = json.load(f)
    except Exception as e:
        print(f"Warning: Failed to load caps_term_registry_data.json: {e}")
        return

    _ALL_TOPIC_RECORDS = records
    for rec in records:
        subj = _normalize_subject(rec.get("subject", ""))
        gr = _normalize_grade(rec.get("grade", ""))
        term = int(rec.get("term", 1))
        name = rec.get("name", "")
        gen_key = rec.get("generator_key", "")

        # Default weights & durations based on phase and cognitive level
        phase = "FET" if int(gr) >= 10 else "Senior"
        suggested_duration = 60 if phase == "FET" else 45
        caps_weight = 25  # standard term weight ~25%

        enriched = {
            "subject": subj,
            "grade": gr,
            "term": term,
            "name": name,
            "generator_key": gen_key,
            "suggested_duration_mins": rec.get("suggested_duration_mins", suggested_duration),
            "caps_weight_percent": rec.get("caps_weight_percent", caps_weight),
            "learning_objective_id": f"{subj.lower()}_{gr}_{name.lower().replace(' ', '_')}",
        }

        sg_key = (subj, gr)
        if sg_key not in _BY_SUBJECT_GRADE:
            _BY_SUBJECT_GRADE[sg_key] = []
        _BY_SUBJECT_GRADE[sg_key].append(enriched)

        sgt_key = (subj, gr, term)
        if sgt_key not in _BY_SUBJECT_GRADE_TERM:
            _BY_SUBJECT_GRADE_TERM[sgt_key] = []
        _BY_SUBJECT_GRADE_TERM[sgt_key].append(enriched)

        topic_norm = _normalize_topic_name(name)
        _BY_TOPIC_LOOKUP[(subj, gr, topic_norm)] = enriched

        if gen_key:
            _BY_KEY_LOOKUP[gen_key] = enriched


_init_registry()


def get_topic_meta(topic: str, grade: str | int = "10", subject: str = "Mathematics") -> Optional[Dict[str, Any]]:
    """Retrieves authoritative CAPS metadata for a given topic."""
    _init_registry()
    subj = _normalize_subject(subject)
    gr = _normalize_grade(grade)
    topic_norm = _normalize_topic_name(topic)

    # 1. Exact match
    direct = _BY_TOPIC_LOOKUP.get((subj, gr, topic_norm))
    if direct:
        return direct

    # 2. Fuzzy substring match within subject and grade
    candidates = _BY_SUBJECT_GRADE.get((subj, gr), [])
    for c in candidates:
        c_name = _normalize_topic_name(c["name"])
        if topic_norm in c_name or c_name in topic_norm:
            return c

    # 3. Check generator key mapping
    from .generator_registry import resolve_generator_key
    resolved_key = resolve_generator_key(topic, grade=gr, subject=subj)
    if resolved_key and resolved_key in _BY_KEY_LOOKUP:
        return _BY_KEY_LOOKUP[resolved_key]

    return None


def get_term_for_topic(topic: str, grade: str | int = "10", subject: str = "Mathematics") -> int:
    """Returns the authentic CAPS ATP term (1, 2, 3, or 4) for a given topic."""
    meta = get_topic_meta(topic, grade=grade, subject=subject)
    if meta:
        return meta.get("term", 1)
    return 1


def get_topics_by_term(term: int, grade: str | int = "10", subject: str = "Mathematics") -> List[Dict[str, Any]]:
    """Returns all authentic CAPS topics for a specific term, grade, and subject."""
    _init_registry()
    subj = _normalize_subject(subject)
    gr = _normalize_grade(grade)
    return _BY_SUBJECT_GRADE_TERM.get((subj, gr, int(term)), [])


def get_all_topics_for_subject_grade(grade: str | int = "10", subject: str = "Mathematics") -> List[Dict[str, Any]]:
    """Returns all topics for a given subject and grade, grouped with their authentic terms."""
    _init_registry()
    subj = _normalize_subject(subject)
    gr = _normalize_grade(grade)
    return _BY_SUBJECT_GRADE.get((subj, gr), [])


def stamp_question_term_metadata(question: Dict[str, Any], topic: str, grade: str | int, subject: str) -> Dict[str, Any]:
    """Stamps authoritative term, weight, and duration onto a generated question payload.
    Ensures Rule 20 compliance across all 476 topics.
    """
    meta = get_topic_meta(topic, grade=grade, subject=subject)
    if meta:
        question["term"] = meta["term"]
        if "caps_weight_percent" not in question or question.get("caps_weight_percent") is None:
            question["caps_weight_percent"] = meta.get("caps_weight_percent", 25)
        if "suggested_duration_mins" not in question or question.get("suggested_duration_mins") is None:
            question["suggested_duration_mins"] = meta.get("suggested_duration_mins", 45)
    else:
        # Default fallback
        if "term" not in question:
            question["term"] = 1
        if "caps_weight_percent" not in question:
            question["caps_weight_percent"] = 25
        if "suggested_duration_mins" not in question:
            question["suggested_duration_mins"] = 45
    return question


def get_frontend_curriculum_data() -> Dict[str, Any]:
    """Generates the structured curriculum tree consumed by frontend components
    (TopicScopeModal, TodaysDeskView, UniversalWorkspace).
    Grouped strictly by Subject -> Grade -> Topics with authentic Term declarations.
    """
    _init_registry()
    result: Dict[str, Dict[str, Any]] = {}
    for (subj, gr), topics in _BY_SUBJECT_GRADE.items():
        if subj not in result:
            result[subj] = {}
        result[subj][gr] = {
            "topics": [t["name"] for t in topics],
            "topics_with_terms": [
                {
                    "name": t["name"],
                    "term": t["term"],
                    "duration": t["suggested_duration_mins"],
                    "weight": t["caps_weight_percent"],
                    "generator_key": t["generator_key"],
                }
                for t in topics
            ],
            "syllabus_info": True,
        }
    return result
