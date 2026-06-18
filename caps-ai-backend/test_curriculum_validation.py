#!/usr/bin/env python3
"""
Test script for curriculum validation system
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.utils.curriculum_validator import CurriculumValidator
from app.utils.quiz_models import QuizQuestion, DifficultyLevel, QuestionType, ShapeType

def test_curriculum_validation():
    """Test the curriculum validation system"""
    
    # Create a test question
    test_question = QuizQuestion(
        question="A triangle has base 5.4 cm and height 15.7 cm. What is its area?",
        options=["42.3 cm²", "43.3 cm²", "41.3 cm²", "84.6 cm²"],
        correct_answer="42.3 cm²",
        explanation="Area = ½ × base × height = ½ × 5.4 × 15.7 = 42.3 cm²",
        topic="Area Calculations",
        difficulty=DifficultyLevel.MEDIUM,
        question_type=QuestionType.AREA_CALCULATION,
        shape_type=ShapeType.TRIANGLE_EQUILATERAL,
        parameters={"base": 5.4, "height": 15.7, "area": 42.3},
        geometric_constraints=["positive_dimensions"],
        curriculum_alignments=["Calculations involving 2D Shapes"],
        metric_units={"length": "cm", "area": "cm²"},
        south_african_context=True,
        conversion_required=False,
        reasoning_required=False,
        question_id="test_1"
    )
    
    print("Test question created successfully!")
    print(f"Question: {test_question.question}")
    print(f"Difficulty: {test_question.difficulty}")
    print(f"Question Type: {test_question.question_type}")
    print(f"Shape Type: {test_question.shape_type}")
    
    # Test curriculum validator
    try:
        validator = CurriculumValidator()
        print("\nCurriculum validator created successfully!")
        
        # Validate single question
        validation_result = validator.validate_question(test_question)
        print(f"\nValidation Result:")
        print(f"Valid: {validation_result.is_valid}")
        print(f"Result: {validation_result.result}")
        print(f"Curriculum Areas: {[area.value for area in validation_result.curriculum_areas]}")
        print(f"Warnings: {validation_result.warnings}")
        print(f"Errors: {validation_result.errors}")
        print(f"Suggestions: {validation_result.suggestions}")
        
        # Test batch validation
        batch_result = validator.validate_question_batch([test_question])
        print(f"\nBatch Validation Result:")
        print(f"Total Questions: {batch_result['total_questions']}")
        print(f"Valid Questions: {batch_result['valid_questions']}")
        print(f"Curriculum Coverage: {batch_result['curriculum_coverage']:.2f}%")
        print(f"Covered Areas: {[area.value for area in batch_result['covered_areas']]}")
        
    except Exception as e:
        print(f"Error testing curriculum validator: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_curriculum_validation()

