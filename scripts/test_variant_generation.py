import sys
from pathlib import Path

BACKEND_DIR = Path("caps-ai-backend")
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.services.generator_registry import generate_variant, resolve_generator_key, ALL_GENERATORS

test_topics = [
    ("Numbers and calculations with numbers", "10", "Mathematical Literacy"),
    ("Patterns relationships and representations", "10", "Mathematical Literacy"),
    ("Probability", "10", "Mathematical Literacy"),
    ("Scale maps and plans", "10", "Mathematical Literacy"),
    ("Assembly diagrams floor plans and packaging", "10", "Mathematical Literacy"),
    ("Financial documents and tariff systems", "10", "Mathematical Literacy"),
    ("Personal income expenditure and budgets", "10", "Mathematical Literacy"),
    ("Banking interest and taxation", "10", "Mathematical Literacy"),
    ("Data handling", "10", "Mathematical Literacy"),
    ("Measurement of perimeter and area", "10", "Mathematical Literacy"),
]

for t, g, s in test_topics:
    key = resolve_generator_key(t, grade=g, subject=s)
    print(f"\n==================================================")
    print(f"Topic: '{t}' (Gr {g} {s}) -> Key: '{key}'")
    gen = ALL_GENERATORS.get(key)
    print(f"Generator module: {getattr(gen, '__module__', 'unknown')}")
    try:
        res = generate_variant(topic=t, grade=g, subject=s, count=1, seed=101)
        q = res[0] if isinstance(res, list) else res
        print(f"Result ID: {q.get('question_id') or q.get('id')}")
        print(f"Result subskill: {q.get('subskill')}")
        print(f"Result prompt: {q.get('prompt')[:120]}...")
        print(f"Result correct_answer: {q.get('correct_answer') or q.get('answer_latex')}")
    except Exception as e:
        print(f"ERROR: {e}")
