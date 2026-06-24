from typing import Dict, Any, List, Optional
from datetime import datetime, timezone, timedelta


class StudentModel:
    """Shared source of truth for per-subskill mastery and cross-topic engagement.

    The model is used by both the adaptive progression engine and the agentic tutor.
    It intentionally keeps the same Firestore path shape already used by the app:
    artifacts/{app_id}/users/{user_id}/... so existing data remains readable.
    """

    def __init__(self, firestore_db, app_id: str = "tlassistant"):
        self.db = firestore_db
        self.app_id = app_id

    def _user_ref(self, user_id: str):
        if not self.db:
            return None
        return self.db.collection("artifacts").document(self.app_id).collection("users").document(user_id)

    def record_submission(
        self,
        user_id: str,
        subject: str,
        grade: str,
        topic: str,
        subskill: str,
        score: float,
        max_score: float,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Records a single submission and updates the mastery score for a subskill."""
        if not self.db or not user_id:
            return {"status": "noop", "reason": "no_db_or_user"}

        mastery = self._get_mastery(user_id, subject, grade, topic, subskill)
        submitted = mastery.get("submissions", 0)
        weighted_score = mastery.get("weighted_score", 0.0)
        max_weighted = mastery.get("max_weighted", 0.0)

        # Simple rolling weighted average (max score weighted 1)
        new_weighted_score = weighted_score + score
        new_max_weighted = max_weighted + max_score
        new_mastery = (new_weighted_score / new_max_weighted) if new_max_weighted > 0 else 0.0

        record = {
            "lastUpdated": datetime.now(timezone.utc),
            "submissions": submitted + 1,
            "weighted_score": new_weighted_score,
            "max_weighted": new_max_weighted,
            "mastery_score": round(new_mastery, 3),
            "is_struggling": new_mastery < 0.6,
            "subject": subject,
            "grade": grade,
            "topic": topic,
            "subskill": subskill,
        }
        if metadata:
            record["metadata"] = metadata

        doc_ref = self._mastery_doc(user_id, subject, grade, topic, subskill)
        doc_ref.set(record, merge=True)

        self._record_engagement(user_id, subject, grade, topic)
        return record

    def get_mastery(
        self,
        user_id: str,
        subject: str,
        grade: str,
        topic: str,
        subskill: str,
    ) -> float:
        mastery = self._get_mastery(user_id, subject, grade, topic, subskill)
        return mastery.get("mastery_score", 0.0)

    def get_weak_subskills(
        self,
        user_id: str,
        subject: str,
        grade: str,
        topic: str,
        threshold: float = 0.6,
    ) -> List[Dict[str, Any]]:
        """Returns subskills for this topic with mastery below the threshold."""
        if not self.db or not user_id:
            return []

        base_path = self._user_ref(user_id).collection("mastery").document(subject).collection(grade).document(topic).collection("subskills")
        docs = base_path.stream()
        weak = []
        for doc in docs:
            data = doc.to_dict()
            score = data.get("mastery_score", 0.0)
            if score < threshold:
                weak.append({
                    "subskill": doc.id,
                    "mastery_score": score,
                    "submissions": data.get("submissions", 0),
                })
        weak.sort(key=lambda x: x["mastery_score"])
        return weak

    def get_engaged_topics(self, user_id: str, grade: str) -> List[Dict[str, str]]:
        """Returns topics the student has engaged with in a given grade, across subjects."""
        if not self.db or not user_id:
            return []

        doc = self._user_ref(user_id).collection("engagement").document(grade).get()
        if not doc.exists:
            return []
        data = doc.to_dict()
        topics = data.get("topics", [])
        return [{"subject": t.get("subject"), "topic": t.get("topic")} for t in topics]

    # --- Streak tracking ---

    def record_attempt(
        self,
        user_id: str,
        subject: str,
        grade: str,
        topic: str,
        subskill: str,
        is_correct: bool,
    ) -> Dict[str, Any]:
        """Records a single attempt and updates the consecutive correct streak."""
        if not self.db or not user_id:
            return {"status": "noop", "reason": "no_db_or_user"}

        doc_ref = self._streak_doc(user_id, subject, grade, topic, subskill)
        doc = doc_ref.get()
        data = doc.to_dict() or {}

        consecutive_correct = data.get("consecutive_correct", 0)
        consecutive_incorrect = data.get("consecutive_incorrect", 0)

        if is_correct:
            consecutive_correct += 1
            consecutive_incorrect = 0
        else:
            consecutive_incorrect += 1
            consecutive_correct = 0

        streak_record = {
            "consecutive_correct": consecutive_correct,
            "consecutive_incorrect": consecutive_incorrect,
            "lastUpdated": datetime.now(timezone.utc),
        }
        doc_ref.set(streak_record, merge=True)
        return streak_record

    def get_streak(
        self,
        user_id: str,
        subject: str,
        grade: str,
        topic: str,
        subskill: str,
    ) -> Dict[str, int]:
        """Returns the current consecutive correct/incorrect streak for a subskill."""
        if not self.db or not user_id:
            return {"consecutive_correct": 0, "consecutive_incorrect": 0}
        doc = self._streak_doc(user_id, subject, grade, topic, subskill).get()
        if not doc.exists:
            return {"consecutive_correct": 0, "consecutive_incorrect": 0}
        data = doc.to_dict()
        return {
            "consecutive_correct": data.get("consecutive_correct", 0),
            "consecutive_incorrect": data.get("consecutive_incorrect", 0),
        }

    # --- Legacy collections ---

    def record_success(
        self,
        user_id: str,
        subject: str,
        grade: str,
        topic: str,
        subskill: str,
        score: float = None,
    ) -> None:
        """Writes to the solved_freeform_problems collection on high mastery."""
        if not self.db or not user_id:
            return
        doc_ref = self._user_ref(user_id).collection("solved_freeform_problems").document()
        doc_ref.set({
            "subject": subject,
            "grade": grade,
            "topic": topic,
            "subskill": subskill,
            "score": score,
            "timestamp": datetime.now(timezone.utc),
        })

    def record_struggle(
        self,
        user_id: str,
        subject: str,
        grade: str,
        topic: str,
        subskill: str,
        reason: str = "",
    ) -> str:
        """Writes to the struggling_problems collection. Returns the doc ID."""
        if not self.db or not user_id:
            return ""
        doc_ref = self._user_ref(user_id).collection("struggling_problems").document()
        doc_ref.set({
            "subject": subject,
            "grade": grade,
            "topic": topic,
            "subskill": subskill,
            "reason": reason,
            "lastUpdated": datetime.now(timezone.utc),
        })
        return doc_ref.id

    def get_recent_struggles(self, user_id: str, max_records: int = 10) -> List[Dict[str, Any]]:
        """Reads the legacy struggling_problems collection."""
        if not self.db or not user_id:
            return []

        ref = self._user_ref(user_id).collection("struggling_problems")
        docs = ref.order_by("lastUpdated", direction="DESCENDING").limit(max_records).stream()
        return [doc.to_dict() for doc in docs]

    def get_recent_successes(self, user_id: str, max_records: int = 10) -> List[Dict[str, Any]]:
        """Reads the legacy solved_freeform_problems collection."""
        if not self.db or not user_id:
            return []

        ref = self._user_ref(user_id).collection("solved_freeform_problems")
        docs = ref.order_by("timestamp", direction="DESCENDING").limit(max_records).stream()
        return [doc.to_dict() for doc in docs]

    def mark_problem_solved(self, user_id: str, thread_id: str) -> None:
        """Removes a struggling problem record when the student finally succeeds."""
        if not self.db or not user_id:
            return
        doc_ref = self._user_ref(user_id).collection("struggling_problems").document(thread_id)
        doc_ref.delete()

    # --- Cross-subject orchestrator queries ---

    def get_all_mastery_summary(self, user_id: str) -> List[Dict[str, Any]]:
        """Returns a flat list of every subskill the student has attempted,
        across all subjects and grades, with mastery scores."""
        if not self.db or not user_id:
            return []

        summary = []
        mastery_root = self._user_ref(user_id).collection("mastery")
        for subject_doc in mastery_root.stream():
            subject = subject_doc.id
            for grade_col in subject_doc.reference.collections():
                grade = grade_col.id
                for topic_doc in grade_col.stream():
                    topic = topic_doc.id
                    for subskill_doc in topic_doc.reference.collection("subskills").stream():
                        data = subskill_doc.to_dict() or {}
                        summary.append({
                            "subject": subject,
                            "grade": grade,
                            "topic": topic,
                            "subskill": subskill_doc.id,
                            "mastery_score": data.get("mastery_score", 0.0),
                            "submissions": data.get("submissions", 0),
                            "is_struggling": data.get("is_struggling", False),
                            "last_updated": data.get("lastUpdated"),
                        })
        return summary

    def get_struggling_problems_for_spaced_repetition(
        self, user_id: str, min_age_hours: int = 24, max_records: int = 20
    ) -> List[Dict[str, Any]]:
        """Returns struggling problems older than min_age_hours that have
        not yet been retried successfully."""
        if not self.db or not user_id:
            return []

        cutoff = datetime.now(timezone.utc) - timedelta(hours=min_age_hours)
        ref = (
            self._user_ref(user_id)
            .collection("struggling_problems")
            .where("lastUpdated", "<", cutoff)
            .order_by("lastUpdated", direction="DESCENDING")
            .limit(max_records)
        )
        return [doc.to_dict() for doc in ref.stream()]

    def get_streaks_needing_attention(
        self, user_id: str, max_incorrect: int = 3
    ) -> List[Dict[str, Any]]:
        """Returns streaks where consecutive_incorrect >= max_incorrect."""
        if not self.db or not user_id:
            return []

        streaks = []
        streaks_root = self._user_ref(user_id).collection("streaks")
        for subject_doc in streaks_root.stream():
            subject = subject_doc.id
            for grade_col in subject_doc.reference.collections():
                grade = grade_col.id
                for topic_doc in grade_col.stream():
                    topic = topic_doc.id
                    for subskill_doc in topic_doc.reference.collection("subskills").stream():
                        data = subskill_doc.to_dict() or {}
                        if data.get("consecutive_incorrect", 0) >= max_incorrect:
                            streaks.append({
                                "subject": subject,
                                "grade": grade,
                                "topic": topic,
                                "subskill": subskill_doc.id,
                                "consecutive_incorrect": data.get("consecutive_incorrect", 0),
                                "consecutive_correct": data.get("consecutive_correct", 0),
                                "last_updated": data.get("lastUpdated"),
                            })
        return streaks

    def record_study_plan(self, user_id: str, plan_items: List[Dict[str, Any]], ai_message: str = "") -> str:
        """Saves a generated study plan. Returns the doc ID."""
        if not self.db or not user_id:
            return ""
        doc_ref = self._user_ref(user_id).collection("study_plans").document()
        doc_ref.set({
            "created_at": datetime.now(timezone.utc),
            "week_of": datetime.now(timezone.utc).strftime("%Y-%W"),
            "items": plan_items,
            "ai_message": ai_message,
        })
        return doc_ref.id

    def get_latest_study_plan(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Returns the most recent study plan for the user."""
        if not self.db or not user_id:
            return None
        ref = (
            self._user_ref(user_id)
            .collection("study_plans")
            .order_by("created_at", direction="DESCENDING")
            .limit(1)
        )
        docs = list(ref.stream())
        if not docs:
            return None
        return docs[0].to_dict()

    def _get_mastery(self, user_id, subject, grade, topic, subskill):
        if not self.db or not user_id:
            return {}
        doc_ref = self._mastery_doc(user_id, subject, grade, topic, subskill)
        doc = doc_ref.get()
        return doc.to_dict() if doc.exists else {}

    def _mastery_doc(self, user_id, subject, grade, topic, subskill):
        return (
            self._user_ref(user_id)
            .collection("mastery")
            .document(subject)
            .collection(grade)
            .document(topic)
            .collection("subskills")
            .document(subskill)
        )

    def _streak_doc(self, user_id, subject, grade, topic, subskill):
        return (
            self._user_ref(user_id)
            .collection("streaks")
            .document(subject)
            .collection(grade)
            .document(topic)
            .collection("subskills")
            .document(subskill)
        )

    def _record_engagement(self, user_id, subject, grade, topic):
        doc_ref = self._user_ref(user_id).collection("engagement").document(grade)
        doc = doc_ref.get()
        existing = doc.to_dict() if doc.exists else {}
        topics = existing.get("topics", [])
        # Deduplicate by (subject, topic)
        new_entry = {"subject": subject, "topic": topic}
        filtered = [t for t in topics if not (t.get("subject") == subject and t.get("topic") == topic)]
        filtered.append(new_entry)
        doc_ref.set({"topics": filtered, "lastUpdated": datetime.now(timezone.utc)}, merge=True)
