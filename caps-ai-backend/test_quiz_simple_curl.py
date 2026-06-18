#!/usr/bin/env python3
"""
Simple test using urllib instead of requests
"""

import urllib.request
import urllib.parse
import json

def test_quiz_api():
    """Test the quiz API using urllib"""
    print("🧪 Testing Quiz API...")
    
    base_url = "http://127.0.0.1:5001"
    
    # Test 1: Get curriculum topics
    print("📚 Testing curriculum topics...")
    try:
        with urllib.request.urlopen(f"{base_url}/api/math/geometry/curriculum-topics") as response:
            data = json.loads(response.read().decode())
            if data.get('success'):
                print(f"✅ Found {len(data.get('topics', []))} curriculum topics")
            else:
                print(f"❌ Error: {data.get('error')}")
                return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    # Test 2: Generate quiz question
    print("\n📝 Testing quiz generation...")
    try:
        quiz_data = {
            "topic": "Calculations involving 2D Shapes",
            "difficulty": "easy",
            "question_type": "area_calculation",
            "shape_type": "triangle_equilateral",
            "count": 1
        }
        
        data = json.dumps(quiz_data).encode('utf-8')
        req = urllib.request.Request(
            f"{base_url}/api/math/geometry/generate-quiz-question",
            data=data,
            headers={'Content-Type': 'application/json'}
        )
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if data.get('success'):
                print("✅ Quiz generation working!")
                question = data['questions'][0]
                print(f"   Question: {question['question'][:50]}...")
                print(f"   Answer: {question['correct_answer']}")
            else:
                print(f"❌ Quiz generation failed: {data.get('error')}")
                return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    print("\n🎉 Quiz system is working!")
    return True

if __name__ == "__main__":
    test_quiz_api()
