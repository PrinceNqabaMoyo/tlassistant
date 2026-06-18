import sys
sys.path.append('.')
from app.utils.grade11_accounting.term2.analysis_interpretation_generator import generate_questions

for i in range(100):
    generate_questions(count=1, seed=i)
print("Done analysis items.")
