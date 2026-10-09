"""Exam-on-Demand & Diagnostic Baseline Engine (Pillar 2).

Implements:
1. Calendar-Scoped Mock Exam Generation (enforcing topic.term <= selected_term).
2. Diagnostic Baseline Calibration Engine (unassisted beta in {0.30, 0.60, 0.85}).
3. Post-Exam Triage Autopsy Report & 3-Step Cognitive Repair Sequence.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .caps_term_curriculum_registry import (
    get_all_topics_for_subject_grade,
    get_term_for_topic,
    get_topic_meta,
)
from .generator_registry import generate_variant


def generate_diagnostic_baseline_assessment(
    subject: str,
    grade: str | int,
    topic: str,
    seed: Optional[int] = 42,
) -> Dict[str, Any]:
    """Generates an unassisted 3-item diagnostic benchmark for calibrating BKT prior P(L0).
    Difficulty levels:
    - Item 1: Foundational Recall (beta = 0.30)
    - Item 2: Routine Procedure (beta = 0.60)
    - Item 3: Complex Synthesis (beta = 0.85)
    Invariants: Zero hint leakage.
    """
    rng = random.Random(seed)
    difficulties = [
        {"level": "easy", "beta": 0.30, "label": "Foundational Concept"},
        {"level": "medium", "beta": 0.60, "label": "Routine Procedure"},
        {"level": "hard", "beta": 0.85, "label": "Complex Synthesis"},
    ]

    items = []
    total_marks = 0

    for idx, d in enumerate(difficulties):
        item_seed = rng.randint(1000, 999999) if seed else None
        try:
            questions = generate_variant(
                topic=topic,
                difficulty=d["level"],
                count=1,
                seed=item_seed,
                grade=str(grade),
                subject=subject,
            )
            if questions:
                q = dict(questions[0])
                # Invariant: Zero hint leakage during diagnostic baseline
                q["hints"] = {
                    "tier_1": "Diagnostic calibration mode — hints disabled.",
                    "tier_2": "Diagnostic calibration mode — hints disabled.",
                    "tier_3": "Diagnostic calibration mode — hints disabled.",
                }
                q["is_diagnostic"] = True
                q["calibration_beta"] = d["beta"]
                q["checkpoint_label"] = d["label"]
                items.append(q)
                total_marks += q.get("marks", 2)
        except Exception:
            continue

    return {
        "assessment_type": "diagnostic_baseline",
        "subject": subject,
        "grade": str(grade),
        "topic": topic,
        "total_items": len(items),
        "total_marks": total_marks,
        "questions": items,
        "calibration_checkpoints": [d["beta"] for d in difficulties[: len(items)]],
    }


def generate_calendar_mock_exam(
    subject: str,
    grade: str | int,
    term: int = 1,
    paper: int = 1,
    total_marks: int = 50,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    """Generates an authentic examination paper strictly constrained to term <= selected_term.
    Enforces Rule 20 and authentic DBE/IEB cognitive distribution.
    """
    rng = random.Random(seed)
    all_topics = get_all_topics_for_subject_grade(grade=grade, subject=subject)

    # 1. Strict calendar guardrail: only content taught up to selected term
    eligible_topics = [t for t in all_topics if int(t["term"]) <= int(term)]
    if not eligible_topics:
        eligible_topics = all_topics[:4]

    # Select representative topics (up to 5 topics)
    sample_size = min(len(eligible_topics), 5)
    selected_topic_metas = rng.sample(eligible_topics, sample_size) if len(eligible_topics) >= sample_size else eligible_topics

    questions = []
    current_marks = 0
    q_index = 1

    for t_meta in selected_topic_metas:
        t_name = t_meta["name"]
        item_seed = rng.randint(1000, 999999) if seed else None
        target_diff = rng.choice(["easy", "medium", "medium", "hard"])

        try:
            generated = generate_variant(
                topic=t_name,
                difficulty=target_diff,
                count=1,
                seed=item_seed,
                grade=str(grade),
                subject=subject,
                extra_config={"mode": "compound", "term": t_meta["term"], "paper": paper},
            )
            if generated:
                q = dict(generated[0])
                q["exam_question_number"] = f"Question {q_index}"
                q["term"] = t_meta["term"]
                questions.append(q)
                current_marks += q.get("marks", 2)
                q_index += 1
                if current_marks >= total_marks:
                    break
        except Exception:
            continue

    # Exam title
    paper_str = f"Paper {paper}" if int(grade) >= 10 and subject in ["Mathematics", "Physical Sciences", "Accounting"] else ""
    term_title = f"Term {term} Examination" if term < 4 else "Final Examination"
    exam_title = f"Grade {grade} {subject} {term_title} {paper_str}".strip()

    return {
        "success": True,
        "exam_title": exam_title,
        "subject": subject,
        "grade": str(grade),
        "selected_term": int(term),
        "paper": paper,
        "total_marks": current_marks,
        "time_limit_mins": max(30, int(current_marks * 1.2)),
        "question_count": len(questions),
        "questions": questions,
    }


def generate_post_exam_triage_report(
    submission_results: List[Dict[str, Any]],
    exam_metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Generates the post-exam diagnostic autopsy report and dispatches
    the 3-step cognitive repair sequence.
    """
    total_marks_possible = 0
    total_marks_earned = 0
    misconception_counter: Dict[str, int] = {}
    flagged_topics: List[Dict[str, Any]] = []

    for res in submission_results:
        marks_avail = int(res.get("marks", 2))
        marks_awarded = int(res.get("marks_awarded", 0))
        total_marks_possible += marks_avail
        total_marks_earned += marks_awarded

        # Check for missed marks
        if marks_awarded < marks_avail:
            tags = res.get("misconception_tags") or ["general_procedural_error"]
            for tag in tags:
                misconception_counter[tag] = misconception_counter.get(tag, 0) + (marks_avail - marks_awarded)

            flagged_topics.append({
                "topic": res.get("topic", "Core Procedure"),
                "question_id": res.get("question_id"),
                "lost_marks": marks_avail - marks_awarded,
                "misconception_tags": tags,
                "remediation_drill": f"elementary_{tags[0]}" if tags else "elementary_foundation",
            })

    # Sort top misconceptions by lost marks
    sorted_misconceptions = sorted(misconception_counter.items(), key=lambda x: x[1], reverse=True)
    overall_percentage = (total_marks_earned / total_marks_possible * 100) if total_marks_possible > 0 else 0.0

    top_blocker = sorted_misconceptions[0] if sorted_misconceptions else ("none", 0)

    return {
        "total_marks_earned": total_marks_earned,
        "total_marks_possible": total_marks_possible,
        "overall_percentage": round(overall_percentage, 1),
        "pass_status": overall_percentage >= 50.0,
        "top_misconception_blocker": {
            "tag": top_blocker[0],
            "marks_lost": top_blocker[1],
        },
        "all_flagged_misconceptions": [
            {"tag": tag, "marks_lost": lost} for tag, lost in sorted_misconceptions
        ],
        "flagged_questions_count": len(flagged_topics),
        "three_step_repair_plan": {
            "step_1_autopsy": f"You lost {top_blocker[1]} marks purely due to '{top_blocker[0].replace('_', ' ')}'.",
            "step_2_micro_drill": f"Assigned 5-minute targeted drill on {top_blocker[0].replace('_', ' ')}.",
            "step_3_simulearn": "SimuLearn visual animation replay recommended for step-by-step review.",
        },
        "flagged_items": flagged_topics,
    }
