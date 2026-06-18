#!/usr/bin/env python3
"""
Test infinite question variations
"""

import urllib.request
import urllib.parse
import json
import time

def test_infinite_variations():
    """Test that we get different questions each time"""
    print("🧪 Testing Infinite Question Variations...")
    print("=" * 50)
    
    base_url = "http://127.0.0.1:5001"
    
    # Test with different shapes and difficulties
    test_cases = [
        {'shape_type': 'triangle_equilateral', 'difficulty': 'easy'},
        {'shape_type': 'triangle_equilateral', 'difficulty': 'medium'},
        {'shape_type': 'triangle_equilateral', 'difficulty': 'hard'},
        {'shape_type': 'rectangle', 'difficulty': 'easy'},
        {'shape_type': 'circle', 'difficulty': 'medium'},
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test_case['shape_type']} - {test_case['difficulty']}")
        
        quiz_data = {
            "topic": "Calculations involving 2D Shapes",
            "difficulty": test_case['difficulty'],
            "question_type": "area_calculation",
            "shape_type": test_case['shape_type'],
            "count": 1,
            "include_diagram": True,
            "south_african_context": True,
            "conversion_required": False,
            "reasoning_required": test_case['difficulty'] == 'hard'
        }
        
        try:
            data = json.dumps(quiz_data).encode('utf-8')
            req = urllib.request.Request(
                f"{base_url}/api/math/geometry/generate-quiz-question",
                data=data,
                headers={'Content-Type': 'application/json'}
            )
            
            with urllib.request.urlopen(req) as response:
                response_data = json.loads(response.read().decode())
                
                if response_data['success'] and response_data['questions']:
                    question = response_data['questions'][0]
                    print(f"   Question: {question['question']}")
                    print(f"   Answer: {question['correct_answer']}")
                    print(f"   Parameters: {question['parameters']}")
                else:
                    print(f"   ❌ Failed: {response_data.get('error', 'Unknown error')}")
                    
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        # Small delay to avoid overwhelming the server
        time.sleep(0.1)
    
    print(f"\n🎯 Testing multiple questions with same parameters...")
    print("=" * 50)
    
    # Test multiple questions with same parameters to see variation
    quiz_data = {
        "topic": "Calculations involving 2D Shapes",
        "difficulty": "easy",
        "question_type": "area_calculation",
        "shape_type": "triangle_equilateral",
        "count": 1,
        "include_diagram": True,
        "south_african_context": True,
        "conversion_required": False,
        "reasoning_required": False
    }
    
    questions = []
    for i in range(5):
        try:
            data = json.dumps(quiz_data).encode('utf-8')
            req = urllib.request.Request(
                f"{base_url}/api/math/geometry/generate-quiz-question",
                data=data,
                headers={'Content-Type': 'application/json'}
            )
            
            with urllib.request.urlopen(req) as response:
                response_data = json.loads(response.read().decode())
                
                if response_data['success'] and response_data['questions']:
                    question = response_data['questions'][0]
                    questions.append(question)
                    print(f"   Question {i+1}: {question['question']}")
                    print(f"   Parameters: {question['parameters']}")
                else:
                    print(f"   ❌ Failed: {response_data.get('error', 'Unknown error')}")
                    
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        time.sleep(0.1)
    
    # Check for variation
    if len(questions) > 1:
        unique_questions = len(set(q['question'] for q in questions))
        print(f"\n📊 Variation Analysis:")
        print(f"   Total questions generated: {len(questions)}")
        print(f"   Unique questions: {unique_questions}")
        print(f"   Variation rate: {unique_questions/len(questions)*100:.1f}%")
        
        if unique_questions == len(questions):
            print("   ✅ Perfect variation - infinite questions working!")
        elif unique_questions > 1:
            print("   ⚠️  Partial variation - some questions repeated")
        else:
            print("   ❌ No variation - questions are identical")

if __name__ == "__main__":
    test_infinite_variations()
