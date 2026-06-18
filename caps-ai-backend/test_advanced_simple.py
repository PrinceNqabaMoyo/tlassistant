#!/usr/bin/env python3
"""
Simple test for advanced question types using urllib
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

import urllib.request
import urllib.parse
import json

def test_advanced_questions():
    """Test advanced question generation"""
    print("🧪 Testing Advanced Question Types...")
    print("=" * 50)
    
    # Test medium difficulty to trigger advanced questions
    test_cases = [
        {'difficulty': 'medium', 'shape_type': 'triangle_equilateral', 'count': 3},
        {'difficulty': 'hard', 'shape_type': 'rectangle', 'count': 3},
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test_case['difficulty']} {test_case['shape_type']}")
        
        try:
            # Prepare request data
            data = {
                'topic': 'Calculations involving 2D Shapes',
                'difficulty': test_case['difficulty'],
                'question_type': 'area_calculation',
                'shape_type': test_case['shape_type'],
                'count': test_case['count'],
                'include_diagram': True,
                'south_african_context': True,
                'conversion_required': False,
                'reasoning_required': test_case['difficulty'] == 'hard'
            }
            
            # Create request
            req = urllib.request.Request(
                'http://localhost:5001/api/math/geometry/generate-quiz-question',
                data=json.dumps(data).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            
            # Send request
            with urllib.request.urlopen(req) as response:
                response_data = json.loads(response.read().decode('utf-8'))
                
                questions = response_data.get('questions', [])
                print(f"   Generated {len(questions)} questions")
                print(f"   Method: {response_data.get('generation_method', 'unknown')}")
                
                # Check for advanced questions
                advanced_count = 0
                for j, question in enumerate(questions, 1):
                    template_id = question.get('template_id', '') or ''
                    if 'advanced_' in template_id:
                        advanced_count += 1
                        print(f"   Question {j}: {question['question'][:60]}...")
                        print(f"   Answer: {question['correct_answer']}")
                        print(f"   Type: {template_id}")
                    else:
                        print(f"   Question {j}: {question['question'][:60]}...")
                        print(f"   Answer: {question['correct_answer']}")
                        print(f"   Type: {template_id or 'basic'}")
                
                print(f"   Advanced questions: {advanced_count}/{len(questions)}")
                
        except Exception as e:
            print(f"   ❌ Exception: {str(e)}")
    
    print("\n✅ Advanced question testing completed!")

if __name__ == "__main__":
    test_advanced_questions()
