import sys
sys.path.append('.')
from app.utils.grade11_accounting.term2.clubs_nonprofit_generator import generate_questions

for i in range(20):
    try:
        generate_questions(count=1, seed=i)
        print(f"Seed {i} OK")
    except Exception as e:
        print(f"Seed {i} Failed:", e)
