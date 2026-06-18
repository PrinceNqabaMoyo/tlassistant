import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.api.grade7_ems import GENERATORS

def run_tests():
    success = True
    print("Testing Grade 7 EMS Generators...")
    
    for topic, generator in GENERATORS.items():
        print(f"\nTesting: {topic}")
        try:
            # Test different subskills if applicable, else default
            # We don't know the exact subskills supported by all without checking, 
            # so we'll test 'concepts' primarily, and others if we know them
            subskills = ['concepts']
            if 'accounting' in topic or 'income' in topic or 'budgets' in topic:
                subskills.extend(['calculations', 'journals', 'discussion'])
            if 'money' in topic or 'businesses' in topic or 'entrepreneurship' in topic:
                subskills.extend(['discussion'])
                
            for subskill in set(subskills):
                try:
                    q = generator(subskill=subskill, count=1)
                    if q:
                        print(f"  [OK] {subskill} - Generated 1 {q[0].get('question_type')} question")
                    else:
                        print(f"  [WARN] {subskill} - Generated empty list")
                except Exception as e:
                    print(f"  [ERROR] {subskill} - {str(e)}")
                    success = False
        except Exception as e:
            print(f"  [FATAL ERROR] {str(e)}")
            success = False
            
    if success:
        print("\nALL TESTS PASSED!")
    else:
        print("\nSOME TESTS FAILED!")

if __name__ == '__main__':
    run_tests()
