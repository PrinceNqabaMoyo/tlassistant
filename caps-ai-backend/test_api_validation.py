#!/usr/bin/env python3
"""
Test script for API curriculum validation
"""

import requests
import json

def test_api_validation():
    """Test the API curriculum validation endpoint"""
    
    # Test data
    test_data = {
        "questions": [{
            "question": "A triangle has base 5.4 cm and height 15.7 cm. What is its area?",
            "options": ["42.3 cm²", "43.3 cm²", "41.3 cm²", "84.6 cm²"],
            "correct_answer": "42.3 cm²",
            "explanation": "Area = ½ × base × height = ½ × 5.4 × 15.7 = 42.3 cm²",
            "topic": "Area Calculations",
            "difficulty": "medium",
            "question_type": "area_calculation",
            "shape_type": "triangle_equilateral",
            "parameters": {"base": 5.4, "height": 15.7, "area": 42.3},
            "curriculum_alignments": ["Calculations involving 2D Shapes"],
            "metric_units": {"length": "cm", "area": "cm²"},
            "south_african_context": True,
            "conversion_required": False,
            "reasoning_required": False,
            "question_id": "test_1"
        }]
    }
    
    try:
        response = requests.post(
            "http://localhost:5001/api/math/geometry/validate-curriculum",
            headers={"Content-Type": "application/json"},
            json=test_data
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                validation = result.get('validation_result', {})
                print(f"\nValidation Results:")
                print(f"Total Questions: {validation.get('total_questions', 0)}")
                print(f"Valid Questions: {validation.get('valid_questions', 0)}")
                print(f"Curriculum Coverage: {validation.get('curriculum_coverage_percentage', 0)}%")
                print(f"Covered Areas: {validation.get('covered_curriculum_areas', [])}")
            else:
                print(f"API Error: {result.get('error', 'Unknown error')}")
        else:
            print(f"HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_api_validation()

