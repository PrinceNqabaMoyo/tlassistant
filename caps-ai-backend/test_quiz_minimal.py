#!/usr/bin/env python3
"""
Minimal test to isolate the quiz API issue
"""

import urllib.request
import urllib.parse
import json

def test_minimal():
    """Test with minimal data"""
    print("🧪 Testing Minimal Quiz API...")
    
    base_url = "http://127.0.0.1:5001"
    
    # Test with absolute minimal data
    quiz_data = {
        "topic": "Calculations involving 2D Shapes",
        "difficulty": "easy"
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
            print(f"✅ Response received: {response_data}")
            return True
            
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}: {e.reason}")
        # Try to read the error response
        try:
            error_data = json.loads(e.read().decode())
            print(f"   Error details: {error_data}")
        except:
            print(f"   Raw error: {e.read().decode()}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_minimal()
