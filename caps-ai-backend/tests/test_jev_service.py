"""
Unit tests for JevService (System One Decision Layer)
Validates zero-failure fallback guarantees, circuit breaker on HTTP 402, and typed outputs.
"""

import pytest
from unittest.mock import patch, MagicMock
from app.services.jev_service import JevService, JevChoice, JevScore, JevNoul


def test_jev_service_fallback_when_unconfigured():
    """Ensures JevService NEVER fails when no API key is configured."""
    service = JevService(api_key=None)
    assert not service.is_available()

    # Foundational Need evaluation
    result = service.evaluate_foundational_need(
        question_text="Solve for x: x^2 - 5x - 24 = 0",
        student_failed_step="(x - 6)(x + 4) = 0",
        error_type="incorrect_factors",
        grade=10,
        topic="algebraic_expressions"
    )
    assert "prerequisite_gap" in result
    assert "recommended_pedagogy" in result
    assert result["prerequisite_gap"]["is_fallback"] is True
    # Verify fallback correctly detected multiplicative factor gap
    assert result["prerequisite_gap"]["choice"] == "multiplicative_factor_bonds"


def test_jev_service_socratic_interaction_fallback():
    """Ensures Socratic interaction routing returns safe fallback classifications."""
    service = JevService(api_key=None)

    # 1. Asking for shortcut
    res1 = service.evaluate_socratic_interaction(
        student_message="Just tell me the answer please!",
        current_question_context="Quadratic factoring",
        current_topic="Mathematics Grade 10"
    )
    assert res1["learner_intent"]["choice"] == "asking_for_solution_shortcut"
    assert res1["leak_vulnerability"]["score"] == "direct_leak_attempt"
    assert res1["is_on_topic"]["probability"] > 0.8

    # 2. Off-topic query
    res2 = service.evaluate_socratic_interaction(
        student_message="How do I play Minecraft with my friends?",
        current_question_context="Trigonometry",
        current_topic="Mathematics Grade 10"
    )
    assert res2["is_on_topic"]["probability"] < 0.2


def test_jev_service_circuit_breaker_on_http_402_payment_required():
    """Validates that a 402 Payment Required trips the circuit breaker and falls back gracefully."""
    service = JevService(api_key="mock_test_key_unpaid")
    assert service.is_available()

    # Mock HTTP 402 Payment Required response from TypeSafe
    mock_resp = MagicMock()
    mock_resp.status_code = 402

    with patch("requests.post", return_value=mock_resp):
        res = service.evaluate_socratic_interaction(
            student_message="Why did the sign flip?",
            current_question_context="Inequalities",
            current_topic="Mathematics"
        )
        # Should gracefully return fallback without raising an exception
        assert res["learner_intent"]["choice"] == "conceptual_confusion"
        assert res["learner_intent"]["is_fallback"] is True
        # Circuit breaker should now be open
        assert service.circuit_open is True
        assert not service.is_available()


def test_jev_service_teach_back_fallback():
    """Validates teach-back evaluation scoring."""
    service = JevService(api_key=None)

    res = service.evaluate_teach_back_explanation(
        student_explanation="Because dividing an inequality by a negative number reverses the direction of the values on the number line, therefore the sign flips.",
        target_concept_key="inequality_division_negative",
        expected_concept_rules="reverses inequality sign"
    )
    assert "conceptual_mastery" in res
    assert res["conceptual_mastery"]["score"] in ["sound_conceptual_grasp", "rigorous_mastery"]
