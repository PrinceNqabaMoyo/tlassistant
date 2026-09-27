"""
Integration Tests for Quiz API Endpoints
Tests the actual HTTP endpoints using standard unittest
"""

import unittest
import json

try:
    import flask
    from app import create_app
    HAS_FLASK = True
except ImportError:
    HAS_FLASK = False


@unittest.skipUnless(HAS_FLASK, "Flask is required to run HTTP API tests")
class TestQuizAPI(unittest.TestCase):
    """Test quiz API endpoints"""

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.client = cls.app.test_client()

    def test_generate_quiz_question(self):
        """Test quiz question generation endpoint"""
        response = self.client.post('/api/math/geometry/generate-quiz-question',
                                   json={
                                       'topic': 'Calculations involving 2D Shapes',
                                       'difficulty': 'easy',
                                       'question_type': 'area_calculation',
                                       'shape_type': 'triangle_equilateral',
                                       'count': 1
                                   })

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['questions']), 1)
        self.assertIn('question', data['questions'][0])

    def test_get_curriculum_topics(self):
        """Test curriculum topics endpoint"""
        response = self.client.get('/api/math/geometry/curriculum-topics')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('topics', data)
        self.assertGreater(len(data['topics']), 0)

    def test_validate_parameters(self):
        """Test parameter validation endpoint"""
        response = self.client.post('/api/math/geometry/validate-parameters',
                                   json={
                                       'shape_type': 'triangle_equilateral',
                                       'parameters': {'sides': [3, 4, 5]}
                                   })

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertTrue(data['is_valid'])

    def test_quiz_stats(self):
        """Test quiz stats endpoint"""
        response = self.client.get('/api/math/geometry/quiz-stats')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('constraint_generator', data)
        self.assertIn('template_generator', data)


if __name__ == "__main__":
    unittest.main()
