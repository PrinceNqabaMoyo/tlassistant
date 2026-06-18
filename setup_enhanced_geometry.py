#!/usr/bin/env python3
"""
Setup script for Enhanced Geometry Studio
This script helps set up the enhanced geometry features for testing
"""

import os
import sys
import subprocess
import json

def check_python_dependencies():
    """Check if required Python packages are installed"""
    required_packages = [
        'flask',
        'flask-cors',
        'matplotlib',
        'numpy',
        'plotly',
        'python-dotenv'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✓ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package} is missing")
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install " + " ".join(missing_packages))
        return False
    
    return True

def update_main_app():
    """Update MainApp.py to include geometry endpoints"""
    main_app_path = "caps-ai-backend/MainApp.py"
    
    if not os.path.exists(main_app_path):
        print(f"✗ {main_app_path} not found")
        return False
    
    # Read the current file
    with open(main_app_path, 'r') as f:
        content = f.read()
    
    # Check if geometry endpoints are already added
    if "from geometry_api_endpoints import geometry_bp" in content:
        print("✓ Geometry endpoints already added to MainApp.py")
        return True
    
    # Add the import
    import_line = "from geometry_api_endpoints import geometry_bp"
    
    # Find where to add the import (after other imports)
    lines = content.split('\n')
    import_end_line = 0
    
    for i, line in enumerate(lines):
        if line.startswith('from ') or line.startswith('import '):
            import_end_line = i
    
    # Insert the import
    lines.insert(import_end_line + 1, import_line)
    
    # Add blueprint registration
    if "app.register_blueprint(geometry_bp)" not in content:
        # Find where to add the registration (after app creation)
        app_line = -1
        for i, line in enumerate(lines):
            if "app = Flask(__name__)" in line:
                app_line = i
                break
        
        if app_line != -1:
            lines.insert(app_line + 2, "app.register_blueprint(geometry_bp)")
    
    # Write the updated file
    with open(main_app_path, 'w') as f:
        f.write('\n'.join(lines))
    
    print("✓ Updated MainApp.py with geometry endpoints")
    return True

def create_test_endpoints():
    """Create test endpoints for quick verification"""
    test_endpoints = {
        "health": "GET /api/math/geometry/health",
        "test_triangle": "POST /api/math/geometry/test-calculations",
        "test_circle": "POST /api/math/geometry/test-calculations", 
        "test_quad": "POST /api/math/geometry/test-calculations",
        "generate_diagram": "POST /api/math/geometry/generate-diagram",
        "calculate_props": "POST /api/math/geometry/calculate-properties",
        "generate_quiz": "POST /api/math/geometry/generate-quiz"
    }
    
    print("\n📋 Available Test Endpoints:")
    for name, endpoint in test_endpoints.items():
        print(f"  {name}: {endpoint}")
    
    return test_endpoints

def create_curl_test_script():
    """Create a curl test script for quick API testing"""
    curl_script = """#!/bin/bash
# Enhanced Geometry Studio - API Test Script

echo "🧪 Testing Enhanced Geometry Studio API"
echo "========================================"

BASE_URL="http://localhost:5001/api/math/geometry"

# Test 1: Health Check
echo "\\n1. Testing Health Check..."
curl -s "$BASE_URL/health" | python -m json.tool

# Test 2: Triangle Calculations
echo "\\n2. Testing Triangle Calculations..."
curl -s -X POST "$BASE_URL/test-calculations" \\
  -H "Content-Type: application/json" \\
  -d '{"test_type": "triangle"}' | python -m json.tool

# Test 3: Circle Calculations
echo "\\n3. Testing Circle Calculations..."
curl -s -X POST "$BASE_URL/test-calculations" \\
  -H "Content-Type: application/json" \\
  -d '{"test_type": "circle"}' | python -m json.tool

# Test 4: Quadrilateral Calculations
echo "\\n4. Testing Quadrilateral Calculations..."
curl -s -X POST "$BASE_URL/test-calculations" \\
  -H "Content-Type: application/json" \\
  -d '{"test_type": "quadrilateral"}' | python -m json.tool

# Test 5: Generate Triangle Diagram
echo "\\n5. Testing Diagram Generation..."
curl -s -X POST "$BASE_URL/generate-diagram" \\
  -H "Content-Type: application/json" \\
  -d '{
    "diagram_type": "triangle",
    "dimension": "2d",
    "parameters": {
      "vertices": [[0,0], [3,0], [1.5,2.5]],
      "color": "blue"
    }
  }' | python -c "import sys, json; data=json.load(sys.stdin); print('Success:', data.get('success', False)); print('Image length:', len(data.get('image_base64', '')))"

# Test 6: Calculate Triangle Properties
echo "\\n6. Testing Property Calculations..."
curl -s -X POST "$BASE_URL/calculate-properties" \\
  -H "Content-Type: application/json" \\
  -d '{
    "shape": "triangle",
    "parameters": {
      "sides": [3, 4, 5],
      "angles": [90, 53.13, 36.87]
    }
  }' | python -m json.tool

# Test 7: Generate Quiz
echo "\\n7. Testing Quiz Generation..."
curl -s -X POST "$BASE_URL/generate-quiz" \\
  -H "Content-Type: application/json" \\
  -d '{
    "topic": "triangles",
    "difficulty": "medium"
  }' | python -m json.tool

echo "\\n✅ API Testing Complete!"
"""
    
    with open("test_geometry_api.sh", "w") as f:
        f.write(curl_script)
    
    # Make it executable on Unix systems
    try:
        os.chmod("test_geometry_api.sh", 0o755)
    except:
        pass
    
    print("✓ Created test_geometry_api.sh script")
    return True

def main():
    """Main setup function"""
    print("🚀 Enhanced Geometry Studio Setup")
    print("=================================")
    
    # Check if we're in the right directory
    if not os.path.exists("caps-ai-backend"):
        print("✗ Please run this script from the project root directory")
        return False
    
    # Check Python dependencies
    print("\n📦 Checking Python Dependencies...")
    if not check_python_dependencies():
        print("\n❌ Please install missing dependencies first")
        return False
    
    # Update MainApp.py
    print("\n🔧 Updating MainApp.py...")
    if not update_main_app():
        print("❌ Failed to update MainApp.py")
        return False
    
    # Create test script
    print("\n📝 Creating Test Script...")
    create_curl_test_script()
    
    # Show test endpoints
    create_test_endpoints()
    
    print("\n✅ Setup Complete!")
    print("\n📋 Next Steps:")
    print("1. Start the backend: cd caps-ai-backend && python MainApp.py")
    print("2. Test the API: ./test_geometry_api.sh")
    print("3. Start the frontend: npm start")
    print("4. Navigate to Geometry Studio and select 'Enhanced Features Test'")
    
    print("\n🔗 Quick Test Commands:")
    print("curl http://localhost:5001/api/math/geometry/health")
    print("curl -X POST http://localhost:5001/api/math/geometry/test-calculations -H 'Content-Type: application/json' -d '{\"test_type\": \"triangle\"}'")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
