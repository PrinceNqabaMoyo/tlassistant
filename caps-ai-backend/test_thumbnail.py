#!/usr/bin/env python3
"""
Test script for the thumbnail generator
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.utils.thumbnail_generator import ThumbnailGenerator

def test_thumbnail_generator():
    """Test the thumbnail generator with different component types"""
    try:
        # Initialize the generator
        generator = ThumbnailGenerator()
        print("✓ ThumbnailGenerator initialized successfully")
        
        # Test supported types
        print(f"✓ Supported types: {list(generator.supported_types.keys())}")
        
        # Test a simple thumbnail generation
        test_params = {'m': 1, 'c': 0}
        thumbnail_bytes = generator.generate('linear_function', test_params)
        print(f"✓ Linear function thumbnail generated: {len(thumbnail_bytes)} bytes")
        
        # Test another type
        test_params = {'sets': ['A', 'B'], 'sizes': [10, 15]}
        thumbnail_bytes = generator.generate('venn_diagram', test_params)
        print(f"✓ Venn diagram thumbnail generated: {len(thumbnail_bytes)} bytes")
        
        # Test tree diagram (this was one of the problematic ones)
        test_params = {'labels': ['Root', 'Child 1', 'Child 2']}
        thumbnail_bytes = generator.generate('tree_diagram', test_params)
        print(f"✓ Tree diagram thumbnail generated: {len(thumbnail_bytes)} bytes")
        
        print("\n🎉 All tests passed! The thumbnail generator is working correctly.")
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_thumbnail_generator()
    sys.exit(0 if success else 1)
