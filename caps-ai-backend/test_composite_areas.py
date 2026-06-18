#!/usr/bin/env python3
"""
Test Composite Areas Implementation
Tests the enhanced composite area functionality with South African contexts
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.utils.advanced_question_types import AdvancedQuestionGenerator, AdvancedQuestionType
from app.utils.quiz_models import DifficultyLevel

def test_composite_areas():
    """Test composite area question generation"""
    print("🧪 Testing Composite Areas Implementation")
    print("=" * 50)
    
    generator = AdvancedQuestionGenerator()
    
    # Test easy composite area
    print("\n📝 Testing EASY Composite Area:")
    easy_question = generator.generate_composite_area_question(DifficultyLevel.EASY)
    print(f"Question: {easy_question['question']}")
    print(f"Answer: {easy_question['answer']}")
    print(f"Explanation: {easy_question['explanation']}")
    print(f"South African Context: {easy_question.get('south_african_context', False)}")
    print(f"Real World Context: {easy_question.get('real_world_context', 'N/A')}")
    
    # Test medium composite area
    print("\n📝 Testing MEDIUM Composite Area:")
    medium_question = generator.generate_composite_area_question(DifficultyLevel.MEDIUM)
    print(f"Question: {medium_question['question']}")
    print(f"Answer: {medium_question['answer']}")
    print(f"Explanation: {medium_question['explanation']}")
    print(f"South African Context: {medium_question.get('south_african_context', False)}")
    print(f"Real World Context: {medium_question.get('real_world_context', 'N/A')}")
    
    # Test hard composite area
    print("\n📝 Testing HARD Composite Area:")
    hard_question = generator.generate_composite_area_question(DifficultyLevel.HARD)
    print(f"Question: {hard_question['question']}")
    print(f"Answer: {hard_question['answer']}")
    print(f"Explanation: {hard_question['explanation']}")
    print(f"South African Context: {hard_question.get('south_african_context', False)}")
    print(f"Real World Context: {hard_question.get('real_world_context', 'N/A')}")
    
    # Test shaded region questions
    print("\n📝 Testing Shaded Region Questions:")
    shaded_question = generator.generate_shaded_region_question(DifficultyLevel.MEDIUM)
    print(f"Question: {shaded_question['question']}")
    print(f"Answer: {shaded_question['answer']}")
    print(f"Explanation: {shaded_question['explanation']}")
    print(f"South African Context: {shaded_question.get('south_african_context', False)}")
    print(f"Real World Context: {shaded_question.get('real_world_context', 'N/A')}")
    
    # Test multiple questions to verify variety
    print("\n🔄 Testing Question Variety:")
    contexts = set()
    for i in range(5):
        question = generator.generate_composite_area_question(DifficultyLevel.EASY)
        context = question.get('real_world_context', 'Unknown')
        contexts.add(context)
        print(f"  Question {i+1}: {context}")
    
    print(f"\n✅ Generated questions with {len(contexts)} different South African contexts: {', '.join(contexts)}")
    
    print("\n🎉 Composite Areas Implementation Test Complete!")

if __name__ == "__main__":
    test_composite_areas()
