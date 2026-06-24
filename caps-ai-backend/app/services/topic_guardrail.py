import os
from typing import Optional, List, Dict, Any


# Static list of allowed generic prompt patterns. These are tightly scoped to
# the current question and do not require a wiki lookup.
_ALLOWED_GENERIC_PROMPTS = [
    "explain the hint",
    "show me another example",
    "give me another example",
    "another example",
    "why is this wrong",
    "why is this incorrect",
    "explain my mistake",
    "explain this",
    "try again",
    "next question",
    "previous question",
]


def _clean(text: Optional[str]) -> str:
    return (text or "").strip().lower().rstrip("?!.")


class TopicGuardrail:
    """Deterministic topic guardrail for the agentic tutor.

    Allowed topics are, in order:
      1. The current topic.
      2. Any topic within the same grade that the student has already engaged with
         AND that has a documented cross-subject link.
    """

    def __init__(self, student_model=None):
        self.student_model = student_model

    def check(
        self,
        user_input: str,
        current_subject: str,
        current_grade: str,
        current_topic: str,
        user_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns {"allowed": bool, "linked_topic": Optional[str], "reason": str}."""
        if not user_input or not current_subject or not current_grade or not current_topic:
            return {"allowed": False, "linked_topic": None, "reason": "missing_context"}

        clean_input = _clean(user_input)

        # Always allow topic-scoped helper prompts
        if any(clean_input.startswith(p) for p in _ALLOWED_GENERIC_PROMPTS):
            return {"allowed": True, "linked_topic": None, "reason": "generic_helper"}

        # Check direct topic mention
        if current_topic.lower().replace("-", " ") in clean_input:
            return {"allowed": True, "linked_topic": None, "reason": "current_topic"}

        # Check cross-subject same-grade links
        if user_id and self.student_model:
            engaged = self.student_model.get_engaged_topics(user_id, current_grade)
            allowed_links = _load_allowed_links(current_subject, current_grade)
            for entry in engaged:
                engaged_topic = entry.get("topic")
                engaged_subject = entry.get("subject")
                if not engaged_topic or not engaged_subject:
                    continue
                if engaged_topic.lower().replace("-", " ") in clean_input:
                    key = (engaged_subject, current_subject)
                    if _has_link(key, current_topic, engaged_topic, allowed_links):
                        return {
                            "allowed": True,
                            "linked_topic": f"{engaged_subject}/{engaged_topic}",
                            "reason": "cross_subject_link",
                        }

        return {"allowed": False, "linked_topic": None, "reason": "off_topic"}


def _load_allowed_links(subject: str, grade: str) -> Dict[str, List[str]]:
    """Returns a mapping of (subject_a, subject_b) -> list of linked topic pairs.

    For now this is a hardcoded seed. It should be moved to a YAML/JSON file in
    caps-wiki once the cross-subject link matrix is formalized.
    """
    # Example: chemistry/electrons -> biology/electrons
    return {
        ("physical-sciences", "biology"): [
            ("electrons", "electrons"),
            ("atoms", "cells"),
        ],
        ("biology", "physical-sciences"): [
            ("electrons", "electrons"),
        ],
        ("mathematics", "technical-mathematics"): [
            ("algebra", "algebra"),
        ],
        ("technical-mathematics", "mathematics"): [
            ("algebra", "algebra"),
        ],
    }


def _has_link(
    key: tuple,
    current_topic: str,
    engaged_topic: str,
    allowed_links: Dict[str, List[str]],
) -> bool:
    links = allowed_links.get(key, [])
    current_topic_norm = current_topic.lower().replace("-", " ")
    engaged_topic_norm = engaged_topic.lower().replace("-", " ")
    for a, b in links:
        if (a in current_topic_norm and b in engaged_topic_norm) or (
            b in current_topic_norm and a in engaged_topic_norm
        ):
            return True
    return False
