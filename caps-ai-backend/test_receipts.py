import sys
sys.path.append('.')
from app.utils.grade11_accounting.term2.clubs_nonprofit_generator import _gen_receipts_payments_items
import random

r = random.Random(42)
for i in range(100):
    _gen_receipts_payments_items(r)
print("Done receipts items.")
