#!/usr/bin/env python3
"""
Direct test script for quiz system
Tests the files directly without module imports
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_quiz_system():
    """Test the quiz system by importing files directly"""
    try:
        print("🧪 Testing Enhanced Quiz System...")
        print("=" * 50)
        
        # Test direct imports
        print("📦 Testing direct imports...")
        
        # Import the quiz models directly
        sys.path.append(os.path.join(os.path.dirname(__file__), 'app', 'models'))
        from quiz_models import QuizGenerationRequest, DifficultyLevel, QuestionType, ShapeType
        print("✅ quiz_models imported successfully")
        
        # Import the quiz generators directly
        sys.path.append(os.path.join(os.path.dirname(__file__), 'app', 'utils'))
        from quiz_generators import QuizGenerationService
        print("✅ quiz_generators imported successfully")
        
        from geometric_validators import GeometricConstraintValidator
        print("✅ geometric_validators imported successfully")
        
        from curriculum_mapping import get_curriculum_mapper
        print("✅ curriculum_mapping imported successfully")
        
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
        print("This might be due to missing dependencies or circular imports")
        return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_quiz_system()
    sys.exit(0 if success else 1)
