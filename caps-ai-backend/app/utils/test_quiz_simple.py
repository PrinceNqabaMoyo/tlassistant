"""
Simple test function for quiz system
Can be imported and run from anywhere
"""

def test_quiz_system():
    """Simple test function for the quiz system"""
    try:
        from app.utils.quiz_generators import QuizGenerationService
        from app.utils.quiz_models import QuizGenerationRequest, DifficultyLevel, QuestionType, ShapeType
        
        print("🧪 Testing Quiz System...")
        
        # Initialize service
        quiz_service = QuizGenerationService()
        
        # Test basic generation
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
            return True
        else:
            print("❌ Quiz generation failed")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


if __name__ == "__main__":
    test_quiz_system()
