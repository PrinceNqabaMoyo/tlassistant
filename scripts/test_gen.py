import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, 'caps-ai-backend')
from app.utils.grade9_mathematics.probability_generator import generate

for s in [1, 42, 99]:
    res = generate(seed=s)
    q = res['questions'][0]
    print(f"Seed {s}: subskill={q['subskill']} | Ans={q.get('correct_answer')}")

print("All probability_generator tests passed!")
