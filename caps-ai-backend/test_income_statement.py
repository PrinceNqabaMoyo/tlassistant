import sys
sys.path.append('.')
from app.utils.grade11_accounting.income_statement_generator import generate_questions

for i in range(100):
    generate_questions(count=1, seed=i)
print("Done income statement items.")
