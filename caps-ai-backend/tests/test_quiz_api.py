"""
Integration Tests for Quiz API Endpoints
Tests the actual HTTP endpoints
"""

import pytest
import json
from app import create_app


@pytest.fixture
def app():
    """Create test app"""
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()


class TestQuizAPI:
    """Test quiz API endpoints"""
    
    def test_generate_quiz_question(self, client):
        """Test quiz question generation endpoint"""
        response = client.post('/api/math/geometry/generate-quiz-question', 
                             json={
                                 'topic': 'Calculations involving 2D Shapes',
                                 'difficulty': 'easy',
                                 'question_type': 'area_calculation',
                                 'shape_type': 'triangle_equilateral',
                                 'count': 1
                             })
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert len(data['questions']) == 1
        assert 'question' in data['questions'][0]
    
    def test_get_curriculum_topics(self, client):
        """Test curriculum topics endpoint"""
        response = client.get('/api/math/geometry/curriculum-topics')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert 'topics' in data
        assert len(data['topics']) > 0
    
    def test_validate_parameters(self, client):
        """Test parameter validation endpoint"""
        response = client.post('/api/math/geometry/validate-parameters',
                             json={
                                 'shape_type': 'triangle_equilateral',
                                 'parameters': {'sides': [3, 4, 5]}
                             })
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['is_valid'] is True
    
    def test_quiz_stats(self, client):
        """Test quiz stats endpoint"""
        response = client.get('/api/math/geometry/quiz-stats')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert 'constraint_generator' in data
        assert 'template_generator' in data


if __name__ == "__main__":
    pytest.main([__file__])
