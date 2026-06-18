"""
Unit Tests for Enhanced Quiz System
Proper test structure using pytest
"""

import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils.quiz_generators import QuizGenerationService, ConstraintBasedGenerator, TemplateBasedGenerator
from app.utils.quiz_models import (
    QuizGenerationRequest, DifficultyLevel, QuestionType, ShapeType
)
from app.utils.curriculum_mapping import get_curriculum_mapper
from app.utils.geometric_validators import GeometricConstraintValidator


class TestQuizGeneration:
    """Test quiz generation functionality"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.quiz_service = QuizGenerationService()
        self.curriculum_mapper = get_curriculum_mapper()
        self.validator = GeometricConstraintValidator()
    
    def test_basic_quiz_generation(self):
        """Test basic quiz question generation"""
        request = QuizGenerationRequest(
            topic="Calculations involving 2D Shapes",
            difficulty=DifficultyLevel.EASY,
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            count=1
        )
        
        response = self.quiz_service.generate_questions(request)
        
        assert response.success is True
        assert len(response.questions) == 1
        assert response.questions[0].question is not None
        assert response.questions[0].correct_answer is not None
    
    def test_different_question_types(self):
        """Test different question types"""
        question_types = [
            QuestionType.AREA_CALCULATION,
            QuestionType.PERIMETER_CALCULATION,
            QuestionType.SHAPE_CLASSIFICATION,
            QuestionType.UNIT_CONVERSION
        ]
        
        for qtype in question_types:
            request = QuizGenerationRequest(
                topic="Calculations involving 2D Shapes",
                difficulty=DifficultyLevel.MEDIUM,
                question_type=qtype,
                count=1
            )
            
            response = self.quiz_service.generate_questions(request)
            assert response.success is True
            assert len(response.questions) == 1
    
    def test_difficulty_levels(self):
        """Test different difficulty levels"""
        difficulties = [DifficultyLevel.EASY, DifficultyLevel.MEDIUM, DifficultyLevel.HARD]
        
        for difficulty in difficulties:
            request = QuizGenerationRequest(
                topic="Calculations involving 2D Shapes",
                difficulty=difficulty,
                question_type=QuestionType.AREA_CALCULATION,
                count=1
            )
            
            response = self.quiz_service.generate_questions(request)
            assert response.success is True
            assert response.questions[0].difficulty == difficulty


class TestGeometricValidation:
    """Test geometric constraint validation"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.validator = GeometricConstraintValidator()
    
    def test_triangle_validation_valid(self):
        """Test valid triangle parameters"""
        params = {'sides': [3, 4, 5]}
        result = self.validator.validate_triangle(params)
        assert result.is_valid is True
    
    def test_triangle_validation_invalid(self):
        """Test invalid triangle parameters"""
        params = {'sides': [1, 2, 10]}  # Violates triangle inequality
        result = self.validator.validate_triangle(params)
        assert result.is_valid is False
        assert "triangle inequality" in result.error_message.lower()
    
    def test_circle_validation_valid(self):
        """Test valid circle parameters"""
        params = {'radius': 5}
        result = self.validator.validate_circle(params)
        assert result.is_valid is True
    
    def test_circle_validation_invalid(self):
        """Test invalid circle parameters"""
        params = {'radius': -2}  # Negative radius
        result = self.validator.validate_circle(params)
        assert result.is_valid is False
        assert "positive" in result.error_message.lower()


class TestCurriculumMapping:
    """Test curriculum mapping functionality"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.mapper = get_curriculum_mapper()
    
    def test_question_categories_exist(self):
        """Test that all question categories exist"""
        categories = self.mapper.question_categories.keys()
        assert len(categories) == 11
        assert "Shape Classification" in categories
        assert "Area & Perimeter Calculations" in categories
    
    def test_difficulty_characteristics(self):
        """Test difficulty level characteristics"""
        easy_chars = self.mapper.get_difficulty_characteristics(DifficultyLevel.EASY)
        assert "whole numbers" in easy_chars['description'].lower()
        
        hard_chars = self.mapper.get_difficulty_characteristics(DifficultyLevel.HARD)
        assert "complex" in hard_chars['description'].lower()
    
    def test_shape_coverage(self):
        """Test shape coverage for different categories"""
        triangle_shapes = self.mapper.get_shapes_for_category("Triangle Height Concepts")
        assert ShapeType.TRIANGLE_EQUILATERAL in triangle_shapes
        
        quadrilateral_shapes = self.mapper.get_shapes_for_category("Quadrilateral Sorting & Grouping")
        assert ShapeType.SQUARE in quadrilateral_shapes


if __name__ == "__main__":
    pytest.main([__file__])
