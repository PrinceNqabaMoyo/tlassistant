"""
Unit Tests for Enhanced Quiz System
Standard unittest structure
"""

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils.quiz_generators import QuizGenerationService, ConstraintBasedGenerator, TemplateBasedGenerator
from app.utils.quiz_models import (
    QuizGenerationRequest, DifficultyLevel, QuestionType, ShapeType
)
from app.utils.curriculum_mapping import get_curriculum_mapper
from app.utils.geometric_validators import GeometricConstraintValidator


class TestQuizGeneration(unittest.TestCase):
    """Test quiz generation functionality"""

    def setUp(self):
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

        self.assertTrue(response.success)
        self.assertEqual(len(response.questions), 1)
        self.assertIsNotNone(response.questions[0].question)
        self.assertIsNotNone(response.questions[0].correct_answer)

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
            self.assertTrue(response.success)
            self.assertEqual(len(response.questions), 1)

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
            self.assertTrue(response.success)
            self.assertEqual(response.questions[0].difficulty, difficulty)


class TestGeometricValidation(unittest.TestCase):
    """Test geometric constraint validation"""

    def setUp(self):
        """Set up test fixtures"""
        self.validator = GeometricConstraintValidator()

    def test_triangle_validation_valid(self):
        """Test valid triangle parameters"""
        params = {'sides': [3, 4, 5]}
        result = self.validator.validate_triangle(params)
        self.assertTrue(result.is_valid)

    def test_triangle_validation_invalid(self):
        """Test invalid triangle parameters"""
        params = {'sides': [1, 2, 10]}  # Violates triangle inequality
        result = self.validator.validate_triangle(params)
        self.assertFalse(result.is_valid)
        self.assertIn("triangle inequality", result.error_message.lower())

    def test_circle_validation_valid(self):
        """Test valid circle parameters"""
        params = {'radius': 5}
        result = self.validator.validate_circle(params)
        self.assertTrue(result.is_valid)

    def test_circle_validation_invalid(self):
        """Test invalid circle parameters"""
        params = {'radius': -2}  # Negative radius
        result = self.validator.validate_circle(params)
        self.assertFalse(result.is_valid)
        self.assertIn("positive", result.error_message.lower())


class TestCurriculumMapping(unittest.TestCase):
    """Test curriculum mapping functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.mapper = get_curriculum_mapper()

    def test_question_categories_exist(self):
        """Test that all question categories exist"""
        categories = self.mapper.question_categories.keys()
        self.assertEqual(len(categories), 11)
        self.assertIn("Shape Classification", categories)
        self.assertIn("Area & Perimeter Calculations", categories)

    def test_difficulty_characteristics(self):
        """Test difficulty level characteristics"""
        easy_chars = self.mapper.get_difficulty_characteristics(DifficultyLevel.EASY)
        self.assertIn("whole numbers", easy_chars['description'].lower())

        hard_chars = self.mapper.get_difficulty_characteristics(DifficultyLevel.HARD)
        self.assertIn("complex", hard_chars['description'].lower())

    def test_shape_coverage(self):
        """Test shape coverage for different categories"""
        triangle_shapes = self.mapper.get_shapes_for_category("Triangle Height Concepts")
        self.assertIn(ShapeType.TRIANGLE_EQUILATERAL, triangle_shapes)

        quadrilateral_shapes = self.mapper.get_shapes_for_category("Quadrilateral Sorting & Grouping")
        self.assertIn(ShapeType.SQUARE, quadrilateral_shapes)


if __name__ == "__main__":
    unittest.main()
