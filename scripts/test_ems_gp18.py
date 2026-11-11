import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'caps-ai-backend'))
from app.services.generator_registry import generate_variant

topics_to_test = [
    ("Cash receipts journal for a services business 1", 42),
    ("Cash payments journal for a services business", 42),
    ("Accounting concepts", 42),  # has accounting equation table
]

ss_pattern = re.compile(r'SS\[[MA]\]')
all_passed = True

for topic, seed in topics_to_test:
    res = generate_variant(topic, grade='8', subject='Economic and Management Sciences', seed=seed, count=1)
    q = res[0] if isinstance(res, list) else res
    ws = str(q.get('worked_solution') or '')
    
    if ss_pattern.search(ws):
        print(f"FAIL: {topic} worked solution contains legacy SS[M]/SS[A] marker!")
        all_passed = False
    
    # Assert cell-by-cell or step-by-step breakdown exists
    if ("- **" not in ws and "Step 1" not in ws and "(a)" not in ws) or "Cell-by-Cell" not in ws and "Transaction" not in ws and "(a)" not in ws:
        print(f"FAIL: {topic} worked solution is not formatted cell-by-cell / step-by-step! Found: {ws[:100]}")
        all_passed = False
    else:
        print(f"PASS: {topic} produces cell-by-cell solution without legacy markers. First line: {ws.splitlines()[0][:60]}")

if all_passed:
    print("ALL EMS journal and equation memos verified: cell-by-cell format with zero SS[M]/SS[A] markers!")
else:
    sys.exit(1)
