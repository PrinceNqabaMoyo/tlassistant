#!/usr/bin/env python3
"""
Test quiz system through Flask app
This tests the actual API endpoints
"""

import requests
import json
import time

def test_quiz_api():
    """Test the quiz system through the Flask API"""
    print("🧪 Testing Quiz System via Flask API...")
    print("=" * 50)
    
    base_url = "http://localhost:5001"
    
    # Test 1: Check if server is running
    print("🌐 Testing server connection...")
    try:
        response = requests.get(f"{base_url}/api/math/geometry/curriculum-topics", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running")
        else:
            print(f"❌ Server returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start it with: python run.py")
        return False
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False
    
    # Test 2: Generate quiz question
    print("\n📝 Testing quiz generation...")
    try:
        quiz_data = {
            "topic": "Calculations involving 2D Shapes",
            "difficulty": "easy",
            "question_type": "area_calculation",
            "shape_type": "triangle_equilateral",
            "count": 1,
            "south_african_context": True
        }
        
        response = requests.post(
            f"{base_url}/api/math/geometry/generate-quiz-question",
            json=quiz_data,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Quiz generation working")
                print(f"   Generated: {len(data['questions'])} questions")
                print(f"   Method: {data.get('generation_method', 'unknown')}")
                question = data['questions'][0]
                print(f"   Question: {question['question'][:50]}...")
                print(f"   Answer: {question['correct_answer']}")
            else:
                print(f"❌ Quiz generation failed: {data.get('error', 'Unknown error')}")
                return False
        else:
            print(f"❌ HTTP error: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Quiz generation error: {e}")
        return False
    
    # Test 3: Get curriculum topics
    print("\n📚 Testing curriculum topics...")
    try:
        response = requests.get(f"{base_url}/api/math/geometry/curriculum-topics", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                topics = data.get('topics', [])
                print(f"✅ Found {len(topics)} curriculum topics")
                print(f"   Topics: {', '.join(topics[:3])}...")
            else:
                print(f"❌ Curriculum topics failed: {data.get('error')}")
                return False
        else:
            print(f"❌ HTTP error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Curriculum topics error: {e}")
        return False
    
    # Test 4: Validate parameters
    print("\n🔍 Testing parameter validation...")
    try:
        validation_data = {
            "shape_type": "triangle_equilateral",
            "parameters": {"sides": [3, 4, 5]}
        }
        
        response = requests.post(
            f"{base_url}/api/math/geometry/validate-parameters",
            json=validation_data,
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"✅ Parameter validation working")
                print(f"   Valid: {data.get('is_valid')}")
            else:
                print(f"❌ Parameter validation failed: {data.get('error')}")
                return False
        else:
            print(f"❌ HTTP error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Parameter validation error: {e}")
        return False
    
    print("\n🎉 All API tests passed!")
    print("=" * 50)
    return True

if __name__ == "__main__":
    print("Make sure the Flask server is running:")
    print("  cd caps-ai-backend")
    print("  python run.py")
    print()
    
    success = test_quiz_api()
    if success:
        print("✅ Quiz system is working correctly!")
    else:
        print("❌ Quiz system has issues that need to be fixed")
    
    sys.exit(0 if success else 1)
