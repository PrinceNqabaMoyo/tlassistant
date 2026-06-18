#!/usr/bin/env python3
"""
Standalone test script for quiz system
Run this directly: python test_quiz_standalone.py
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_quiz_system():
    """Test the quiz system"""
    try:
        print("🧪 Testing Enhanced Quiz System...")
        print("=" * 50)
        
        # Test imports
        print("📦 Testing imports...")
        from app.utils.quiz_models import QuizGenerationRequest, DifficultyLevel, QuestionType, ShapeType
        from app.utils.quiz_generators import QuizGenerationService
        from app.utils.curriculum_mapping import get_curriculum_mapper
        from app.utils.geometric_validators import GeometricConstraintValidator
        print("✅ All imports successful")
        
        # Test quiz generation
        print("\n📝 Testing quiz generation...")
        quiz_service = QuizGenerationService()
        
        request = QuizGenerationRequest(
            topic="Calculations involving 2D Shapes",
            difficulty=DifficultyLevel.EASY,
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            count=1
        )
        
        response = quiz_service.generate_questions(request)
        
        if response.success:
            print("✅ Quiz generation working")
            print(f"   Generated: {len(response.questions)} questions")
            print(f"   Method: {response.generation_method}")
            question = response.questions[0]
            print(f"   Question: {question.question[:50]}...")
            print(f"   Answer: {question.correct_answer}")
        else:
            print("❌ Quiz generation failed")
            return False
        
        # Test curriculum mapping
        print("\n📚 Testing curriculum mapping...")
        mapper = get_curriculum_mapper()
        categories = list(mapper.question_categories.keys())
        print(f"✅ Found {len(categories)} question categories")
        print(f"   Categories: {', '.join(categories[:3])}...")
        
        # Test geometric validation
        print("\n🔍 Testing geometric validation...")
        validator = GeometricConstraintValidator()
        
        # Test valid triangle
        triangle_params = {'sides': [3, 4, 5]}
        result = validator.validate_triangle(triangle_params)
        print(f"✅ Triangle [3,4,5]: {'Valid' if result.is_valid else 'Invalid'}")
        
        # Test invalid triangle
        invalid_triangle = {'sides': [1, 2, 10]}
        result = validator.validate_triangle(invalid_triangle)
        print(f"✅ Triangle [1,2,10]: {'Valid' if result.is_valid else 'Invalid'}")
        
        # Test circle validation
        circle_params = {'radius': 5}
        result = validator.validate_circle(circle_params)
        print(f"✅ Circle radius 5: {'Valid' if result.is_valid else 'Invalid'}")
        
        print("\n🎉 All tests passed!")
        print("=" * 50)
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you're running this from the caps-ai-backend directory")
        return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_quiz_system()
    sys.exit(0 if success else 1)
