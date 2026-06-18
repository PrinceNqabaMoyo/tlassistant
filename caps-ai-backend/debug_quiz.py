#!/usr/bin/env python3
"""
Debug script to test quiz generation directly
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def debug_quiz_generation():
    """Debug quiz generation step by step"""
    print("🔍 Debugging Quiz Generation...")
    print("=" * 50)
    
    try:
        # Test 1: Import quiz models
        print("📦 Testing quiz models import...")
        from app.utils.quiz_models import QuizGenerationRequest, DifficultyLevel, QuestionType, ShapeType
        print("✅ quiz_models imported successfully")
        
        # Test 2: Import quiz generators
        print("\n📦 Testing quiz generators import...")
        from app.utils.quiz_generators import QuizGenerationService
        print("✅ quiz_generators imported successfully")
        
        # Test 3: Create quiz service
        print("\n🔧 Creating quiz service...")
        quiz_service = QuizGenerationService()
        print("✅ Quiz service created successfully")
        
        # Test 4: Create request
        print("\n📝 Creating quiz request...")
        request = QuizGenerationRequest(
            topic="Calculations involving 2D Shapes",
            difficulty=DifficultyLevel.EASY,
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            count=1
        )
        print("✅ Quiz request created successfully")
        
        # Test 5: Generate questions
        print("\n🎯 Generating quiz questions...")
        response = quiz_service.generate_questions(request)
        print(f"✅ Quiz generation completed")
        print(f"   Success: {response.success}")
        print(f"   Method: {response.generation_method}")
        print(f"   Questions: {len(response.questions)}")
        
        if response.success and response.questions:
            question = response.questions[0]
            print(f"   Question: {question.question}")
            print(f"   Answer: {question.correct_answer}")
        else:
            print(f"   Error: {response.error_message}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    debug_quiz_generation()
