"""
Unit Tests for Ebbinghaus Memory-Decayed BKT in StudentModel
Verifies:
1. P(L_{k, t}) = P(L_{k, t-1}) * e^(-lambda * delta_t) calculation.
2. Immediate retrieval (delta_t = 0) exhibits 0 decay.
3. 21 days with lambda = 0.015 drops 0.85 mastery to ~0.62 (<0.70 threshold -> 'refresh_recommended').
4. Future/negative delta does not inflate mastery.
"""

from datetime import datetime, timezone, timedelta

from app.services.student_model import calculate_decayed_mastery, StudentModel


def test_calculate_decayed_mastery_immediate():
    now = datetime(2026, 9, 20, 12, 0, 0, tzinfo=timezone.utc)
    raw = 0.85
    # Zero elapsed days -> byte-identical score
    decayed = calculate_decayed_mastery(raw, now, lambda_decay=0.015, current_time=now)
    assert decayed == 0.85


def test_calculate_decayed_mastery_21_days():
    t0 = datetime(2026, 9, 1, 12, 0, 0, tzinfo=timezone.utc)
    t1 = datetime(2026, 9, 22, 12, 0, 0, tzinfo=timezone.utc)  # 21 days later
    raw = 0.85
    # e^(-0.015 * 21) = e^(-0.315) ~= 0.72978
    # 0.85 * 0.72978 ~= 0.620
    decayed = calculate_decayed_mastery(raw, t0, lambda_decay=0.015, current_time=t1)
    assert 0.615 <= decayed <= 0.625
    assert decayed < 0.70  # Triggers 'refresh_recommended'


def test_calculate_decayed_mastery_zero_or_negative():
    now = datetime.now(timezone.utc)
    assert calculate_decayed_mastery(0.0, now) == 0.0
    # Future timestamp should not inflate score
    future = now + timedelta(days=5)
    assert calculate_decayed_mastery(0.80, future, current_time=now) == 0.80


def test_get_mastery_details_refresh_status():
    class MockDoc:
        def __init__(self, data):
            self._data = data
            self.exists = bool(data)

        def to_dict(self):
            return self._data

    class MockDocRef:
        def __init__(self, data):
            self._data = data

        def get(self):
            return MockDoc(self._data)

    class MockDB:
        def __init__(self, mock_data):
            self.mock_data = mock_data

    # Simulate subskill mastered 25 days ago
    past_date = datetime.now(timezone.utc) - timedelta(days=25)
    model = StudentModel(firestore_db=None)
    # Patch _get_mastery directly
    model._get_mastery = lambda uid, sub, grd, top, subsk: {
        "mastery_score": 0.88,
        "submissions": 12,
        "lastUpdated": past_date,
    }

    details = model.get_mastery_details(
        user_id="learner_123",
        subject="Mathematics",
        grade="10",
        topic="Trigonometry",
        subskill="Special Angles"
    )

    assert details["raw_mastery"] == 0.88
    assert details["decayed_mastery"] < 0.70
    assert details["status"] == "refresh_recommended"
    assert details["needs_refresh"] is True
