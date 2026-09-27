"""
caps-ai-backend/app/services/jev_service.py
System One Decision Layer powered by TypeSafe AI (Jev).

Provides sub-100ms, machine-typed, probabilistic decisions (Choice, Score, Noul)
over program state without generating freeform prose or incurring token latency.

CRITICAL INVARIANT (Zero-Failure Fallback Guarantee):
If Jev is not paid up, not configured (missing TYPESAFE_API_KEY), or returns
401/402/403/429/500/timeout, this service automatically and silently falls back
to intelligent, deterministic Python heuristics. The application NEVER crashes.
"""

import os
import time
import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict

try:
    import requests
except ImportError:
    requests = None  # type: ignore

logger = logging.getLogger(__name__)


# =============================================================================
# JEV TYPED PRIMITIVES
# =============================================================================

@dataclass
class JevChoice:
    """Selects one option from a predefined developer-specified list with probabilities."""
    question: str
    choices: List[str]
    type: str = "choice"


@dataclass
class JevScore:
    """Evaluates state against an ordered rubric or severity scale."""
    question: str
    rubric: List[str]
    type: str = "score"


@dataclass
class JevNoul:
    """Boolean condition returning calibrated probability (0.0 to 1.0) and confidence."""
    question: str
    type: str = "noul"


# =============================================================================
# JEV SERVICE CLASS
# =============================================================================

class JevService:
    """System One Decision Model client with circuit breaker and deterministic fallback."""

    def __init__(self, api_key: Optional[str] = None, endpoint: Optional[str] = None):
        self.api_key = api_key or os.getenv("TYPESAFE_API_KEY") or os.getenv("JEV_API_KEY")
        self.endpoint = endpoint or os.getenv("TYPESAFE_ENDPOINT", "https://api.typesafe.ai/v1/classify")
        self.timeout = float(os.getenv("JEV_TIMEOUT_SECS", "2.0"))  # Hard 2.0s socket timeout
        
        # Circuit Breaker state: prevents spamming failed/unpaid API endpoints
        self.circuit_open = False
        self.last_circuit_trip = 0.0
        self.circuit_cooldown_secs = 300.0  # 5-minute cooldown on 402/401/repeated errors

    def is_available(self) -> bool:
        """Returns True only if an API key exists and circuit is closed."""
        if not self.api_key or requests is None:
            return False
        if self.circuit_open:
            # Check if cooldown has elapsed
            if time.time() - self.last_circuit_trip > self.circuit_cooldown_secs:
                self.circuit_open = False
                logger.info("[JevService] Circuit cooldown elapsed. Re-testing Jev endpoint.")
                return True
            return False
        return True

    def classify(self, state: str, questions: Dict[str, Any], context_tag: str = "generic") -> Dict[str, Any]:
        """
        Executes parallel typed classification over state using Jev API.
        Guaranteed to return valid typed dictionaries even if Jev is unpaid/offline.
        """
        if not self.is_available():
            return self._deterministic_fallback(state, questions, context_tag)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "state": state,
            "questions": {k: asdict(v) if hasattr(v, "__dataclass_fields__") else v for k, v in questions.items()}
        }

        try:
            resp = requests.post(self.endpoint, json=payload, headers=headers, timeout=self.timeout)
            
            # Handle payment/auth failure: Trip circuit to protect application latency
            if resp.status_code in (401, 402, 403):
                logger.warning(f"[JevService] Account payment or auth issue (HTTP {resp.status_code}). Tripping circuit breaker for 5 mins.")
                self._trip_circuit()
                return self._deterministic_fallback(state, questions, context_tag, error=f"HTTP {resp.status_code}")

            resp.raise_for_status()
            data = resp.json()
            return data.get("results", {})

        except Exception as e:
            logger.warning(f"[JevService] Classification failed or timed out ({e}). Falling back to deterministic heuristics.")
            return self._deterministic_fallback(state, questions, context_tag, error=str(e))

    def _trip_circuit(self):
        self.circuit_open = True
        self.last_circuit_trip = time.time()

    # =========================================================================
    # SCHEMA 1: ADAPTIVE FOUNDATIONAL ROUTER (Tang & Stokke Regression)
    # =========================================================================
    def evaluate_foundational_need(
        self,
        question_text: str,
        student_failed_step: str,
        error_type: str,
        grade: int,
        topic: str
    ) -> Dict[str, Any]:
        """
        Sub-100ms classification to determine which foundational Tang/Stokke sub-drill
        to deploy when a student struggles with a compound problem.
        """
        state = f"""
        Grade: {grade}
        Topic: {topic}
        Problem: {question_text}
        Student Attempt / Failed Step: {student_failed_step}
        Detected Error Trace: {error_type}
        """

        questions = {
            "prerequisite_gap": JevChoice(
                question="What is the root prerequisite failure in this student's step?",
                choices=[
                    "none_accidental_slip",
                    "additive_number_bonds",             # Make-10, bridging, integer signs
                    "multiplicative_factor_bonds",       # Factor pairs, times tables, decomposition
                    "fraction_unit_partitioning",        # Conceptual failure of what a fraction represents
                    "fraction_common_denominator_lcd",   # Finding or equalizing denominators
                    "distributive_law_expansion",        # Multiplying across parentheses
                ]
            ),
            "recommended_pedagogy": JevChoice(
                question="Which instructional modality will best repair this student's gap?",
                choices=[
                    "tang_visual_strip_model",           # Interactive visual fraction/area diagram
                    "tang_number_bond_matrix",           # Kakooma-style decomposition puzzle
                    "stokke_direct_worked_example",      # Explicit step-by-step procedure modeling
                    "stokke_fluency_speed_sprint",       # 60-second automaticity sprint
                    "continue_at_grade_level"            # Retry isomorphic question at same grade level
                ]
            ),
            "cognitive_overload": JevNoul(
                question="Does this student attempt exhibit signs of cognitive overload or wild guessing?"
            )
        }

        return self.classify(state, questions, context_tag="foundational_router")

    # =========================================================================
    # SCHEMA 2: SOCRATIC INTENT & SHIELD SAFETY ROUTER
    # =========================================================================
    def evaluate_socratic_interaction(
        self,
        student_message: str,
        current_question_context: str,
        current_topic: str
    ) -> Dict[str, Any]:
        """
        Evaluates student chat in the Socratic drawer before calling Gemma.
        Prevents solution leaks, verifies topic boundaries, and determines intent.
        """
        state = f"""
        Topic: {current_topic}
        Question Context: {current_question_context}
        Student Message: "{student_message}"
        """

        questions = {
            "is_on_topic": JevNoul(
                question=f"Is this student message asking about {current_topic} or valid prerequisite concepts?"
            ),
            "learner_intent": JevChoice(
                question="What is the student's primary conversational intent?",
                choices=[
                    "asking_for_solution_shortcut",      # "just tell me the answer", "what is x?"
                    "seeking_step_validation",           # "is step 2 right?", "did I get 14?"
                    "conceptual_confusion",              # "where did the 4 come from?", "why divide?"
                    "frustrated_or_giving_up",           # "this is too hard", "i hate this"
                    "ready_to_proceed"                   # "okay got it", "i see it now"
                ]
            ),
            "leak_vulnerability": JevScore(
                question="How vulnerable is this prompt to coercing a generative model into leaking numerical answers?",
                rubric=["safe", "moderate_coercion", "direct_leak_attempt"]
            )
        }

        return self.classify(state, questions, context_tag="socratic_router")

    # =========================================================================
    # SCHEMA 3: COGNITIVE TEACH-BACK EVALUATOR
    # =========================================================================
    def evaluate_teach_back_explanation(
        self,
        student_explanation: str,
        target_concept_key: str,
        expected_concept_rules: str
    ) -> Dict[str, Any]:
        """
        Evaluates student self-explanations against CAPS conceptual rubrics.
        """
        state = f"""
        Concept Target: {target_concept_key}
        Expected Rule: {expected_concept_rules}
        Student Explanation: "{student_explanation}"
        """

        questions = {
            "conceptual_mastery": JevScore(
                question="Evaluate the depth and correctness of the student's conceptual explanation:",
                rubric=[
                    "incorrect_misconception",
                    "surface_rote_recitation",
                    "sound_conceptual_grasp",
                    "rigorous_mastery"
                ]
            ),
            "specific_misconception": JevChoice(
                question="If flawed, which specific misconception does the student hold?",
                choices=[
                    "none_correct",
                    "sign_inversion_confusion",
                    "unit_denominator_confusion",
                    "incomplete_distribution",
                    "swapped_inverse_operations"
                ]
            )
        }

        return self.classify(state, questions, context_tag="teach_back")

    # =========================================================================
    # DETERMINISTIC FAIL-SAFE ENGINE (100% Zero-API, Offline-Safe)
    # =========================================================================
    def _deterministic_fallback(
        self,
        state: str,
        questions: Dict[str, Any],
        context_tag: str,
        error: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        High-fidelity Python rule-based classifier executing when Jev is unpaid,
        offline, or unreachable.
        """
        state_lower = (state or "").lower()
        results = {}

        for q_id, q_obj in questions.items():
            # 1. Noul Boolean judgments
            if isinstance(q_obj, JevNoul) or (isinstance(q_obj, dict) and q_obj.get("type") == "noul"):
                prob = 0.95  # Default permissive
                if q_id == "is_on_topic":
                    # Check off-topic indicators
                    off_words = ["play", "game", "minecraft", "fortnite", "roblox", "girlfriend", "boyfriend", "joke", "hack"]
                    if any(w in state_lower for w in off_words):
                        prob = 0.05
                    else:
                        prob = 0.95
                elif q_id == "cognitive_overload":
                    frust_words = ["hate", "stupid", "impossible", "give up", "dont know", "don't know", "can't", "cant"]
                    prob = 0.85 if any(w in state_lower for w in frust_words) else 0.15

                results[q_id] = {
                    "probability": prob,
                    "confidence": 0.90,
                    "is_fallback": True,
                    "fallback_note": error or "deterministic_rule"
                }

            # 2. Choice Discrete Selections
            elif isinstance(q_obj, JevChoice) or (isinstance(q_obj, dict) and q_obj.get("type") == "choice"):
                choices = q_obj.choices if isinstance(q_obj, JevChoice) else q_obj.get("choices", [])
                selected_choice = choices[0] if choices else "unknown"

                if q_id == "prerequisite_gap":
                    if any(w in state_lower for w in ["denom", "lcd", "fraction", "half", "quarter", "numerator"]):
                        selected_choice = "fraction_common_denominator_lcd"
                    elif any(w in state_lower for w in ["factor", "pair", "times", "trinomial", "quadratic", "product"]):
                        selected_choice = "multiplicative_factor_bonds"
                    elif any(w in state_lower for w in ["bracket", "parenthes", "distribut", "expand"]):
                        selected_choice = "distributive_law_expansion"
                    elif any(w in state_lower for w in ["plus", "minus", "negative", "sign", "bridge", "make-10", "make 10"]):
                        selected_choice = "additive_number_bonds"
                    else:
                        selected_choice = "none_accidental_slip"

                elif q_id == "recommended_pedagogy":
                    if "fraction" in state_lower:
                        selected_choice = "tang_visual_strip_model"
                    elif any(w in state_lower for w in ["factor", "times", "table"]):
                        selected_choice = "stokke_fluency_speed_sprint"
                    elif any(w in state_lower for w in ["plus", "minus", "bond"]):
                        selected_choice = "tang_number_bond_matrix"
                    elif "distribut" in state_lower:
                        selected_choice = "stokke_direct_worked_example"
                    else:
                        selected_choice = "continue_at_grade_level"

                elif q_id == "learner_intent":
                    if any(w in state_lower for w in ["just tell me", "what is the answer", "what is x", "give me answer"]):
                        selected_choice = "asking_for_solution_shortcut"
                    elif any(w in state_lower for w in ["is this right", "is step", "did i get", "check my"]):
                        selected_choice = "seeking_step_validation"
                    elif any(w in state_lower for w in ["why", "where did", "how come", "explain"]):
                        selected_choice = "conceptual_confusion"
                    elif any(w in state_lower for w in ["hate", "give up", "too hard", "cant do"]):
                        selected_choice = "frustrated_or_giving_up"
                    elif any(w in state_lower for w in ["got it", "i see", "makes sense", "okay"]):
                        selected_choice = "ready_to_proceed"
                    else:
                        selected_choice = "conceptual_confusion"

                elif q_id == "specific_misconception":
                    if "sign" in state_lower or "negative" in state_lower:
                        selected_choice = "sign_inversion_confusion"
                    elif "denom" in state_lower or "fraction" in state_lower:
                        selected_choice = "unit_denominator_confusion"
                    elif "distribut" in state_lower:
                        selected_choice = "incomplete_distribution"
                    else:
                        selected_choice = "none_correct"

                results[q_id] = {
                    "choice": selected_choice,
                    "probabilities": {c: 1.0 if c == selected_choice else 0.0 for c in choices},
                    "is_fallback": True,
                    "fallback_note": error or "deterministic_rule"
                }

            # 3. Score Ordered Rubrics
            elif isinstance(q_obj, JevScore) or (isinstance(q_obj, dict) and q_obj.get("type") == "score"):
                rubric = q_obj.rubric if isinstance(q_obj, JevScore) else q_obj.get("rubric", [])
                selected_score = rubric[0] if rubric else "unknown"

                if q_id == "leak_vulnerability":
                    if any(w in state_lower for w in ["just tell me the answer", "give me the final value"]):
                        selected_score = "direct_leak_attempt"
                    elif any(w in state_lower for w in ["solve it for me", "what is x"]):
                        selected_score = "moderate_coercion"
                    else:
                        selected_score = "safe"

                elif q_id == "conceptual_mastery":
                    # Evaluates length and keyword depth
                    if len(state_lower) > 50 and any(w in state_lower for w in ["because", "therefore", "represents", "multiplies", "equal"]):
                        selected_score = "sound_conceptual_grasp"
                    elif len(state_lower) > 20:
                        selected_score = "surface_rote_recitation"
                    else:
                        selected_score = "incorrect_misconception"

                results[q_id] = {
                    "score": selected_score,
                    "probabilities": {r: 1.0 if r == selected_score else 0.0 for r in rubric},
                    "is_fallback": True,
                    "fallback_note": error or "deterministic_rule"
                }

        return results


# Global singleton instance for easy import
jev_service = JevService()
