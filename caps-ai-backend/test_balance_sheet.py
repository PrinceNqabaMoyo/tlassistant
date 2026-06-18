import sys
sys.path.append('.')
from app.utils.grade11_accounting.partnership_balance_sheet_generator import generate_questions

for i in range(100):
    generate_questions(count=1, seed=i)
print("Done balance sheet items.")
