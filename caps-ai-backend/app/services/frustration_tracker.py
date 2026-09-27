"""
Frustration Tracker & 3-Strike Circuit Breaker
Prevents student fatigue by escalating chronic failure to canonical SimuLearn animations
and isomorphic variant practice rather than infinite incorrect attempts.
"""

from typing import Dict, Any


class FrustrationTracker:
    def __init__(self):
        # Maps (user_id, question_id) -> strike_count: int
        self._strike_store: Dict[str, int] = {}

    def _key(self, user_id: str, question_id: str) -> str:
        return f"{user_id}:{question_id}"

    def record_attempt(self, user_id: str, question_id: str, is_correct: bool) -> Dict[str, Any]:
        """
        Records an attempt. If incorrect, increments strike count and returns pedagogical action.
        """
        k = self._key(user_id, question_id)

        if is_correct:
            self._strike_store.pop(k, None)
            return {
                "status": "success",
                "strikes": 0,
                "action": "advance_progression"
            }

        strikes = self._strike_store.get(k, 0) + 1
        self._strike_store[k] = strikes

        if strikes == 1:
            return {
                "status": "struggling",
                "strikes": 1,
                "hint_tier": 1,
                "action": "deliver_tier1_nudge"
            }
        elif strikes == 2:
            return {
                "status": "struggling",
                "strikes": 2,
                "hint_tier": 2,
                "action": "deliver_tier2_scaffold"
            }
        else:
            # 3 or more strikes: Circuit breaker triggers
            self._strike_store.pop(k, None) # reset after escalation
            return {
                "status": "circuit_breaker_tripped",
                "strikes": strikes,
                "hint_tier": 3,
                "action": "trigger_simulearn",
                "require_isomorphic_variant": True,
                "message": "Let's watch a quick worked example step-by-step before trying a fresh variant."
            }

    def reset(self, user_id: str, question_id: str):
        self._strike_store.pop(self._key(user_id, question_id), None)


frustration_tracker = FrustrationTracker()
