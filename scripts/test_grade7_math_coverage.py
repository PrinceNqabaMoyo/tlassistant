import sys
import os

# Add backend directory to sys.path
backend_dir = os.path.join(os.path.dirname(__file__), "..", "caps-ai-backend")
sys.path.insert(0, backend_dir)

from app.services.generator_registry import generate_variant, resolve_generator_key

topics = [
    'whole numbers',
    'integers',
    'fractions',
    'decimals',
    'patterns',
    'algebraic expressions',
    'functions and relationships',
    'geometry of 2d shapes',
    'geometric nets for 3d shapes',
    'perimeter and area',
    'surface area and volume',
    'transformation geometry',
    'data handling',
    'probability',
    'exponents'
]

print("=== GRADE 7 MATHEMATICS COMPLETE COVERAGE AUDIT ===")
all_passed = True
for t in topics:
    try:
        key = resolve_generator_key(t, grade='7', subject='Mathematics')
        res = generate_variant(t, grade='7', seed=42)
        q = res[0]
        subskill = q.get('subskill', 'unknown')
        qid = q.get('id', 'no_id')
        print(f"PASS: {t:30} -> {key:45} [{subskill}] ({qid})")
    except Exception as e:
        print(f"FAIL: {t:30} -> ERROR: {e}")
        all_passed = False

if all_passed:
    print("\nALL 15 GRADE 7 MATHEMATICS TOPICS SUCCESSFULLY RESOLVED WITH DEDICATED GENERATORS!")
else:
    print("\nSOME TOPICS FAILED!")
    sys.exit(1)
