import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'caps-ai-backend'))

from app.utils.grade8_ems import term3_ownership
from app.utils.grade8_ems import term3_management
from app.utils.grade8_ems import term1_general_ledger
from app.utils.grade8_ems import term2_accounting_cycle

targets = [
    ("Forms of Ownership", term3_ownership, 5, "01. Forms of ownership.md"),
    ("Levels and Functions of Management", term3_management, 4, "02. Levels and functions of management.md"),
    ("General Ledger & Trial Balance", term1_general_ledger, 3, "01. General ledger and Trial balance of a service business.md"),
    ("The Accounting Cycle", term2_accounting_cycle, 4, "01. the accounting cycle.md"),
]

all_passed = True
for name, mod, min_subskills, doc_ref in targets:
    subskills = getattr(mod, 'SUBSKILLS', None)
    if not subskills:
        funcs = [f for f in dir(mod) if f.startswith('_gen_') or f.startswith('_build_')]
        count = len(funcs)
    else:
        count = len(subskills)
    
    doc = getattr(mod, '__doc__', '') or ''
    if count < min_subskills:
        print(f"FAIL: {name} has {count} subskills < {min_subskills}")
        all_passed = False
    elif doc_ref not in doc:
        print(f"FAIL: {name} docstring missing '{doc_ref}' citation")
        all_passed = False
    else:
        print(f"PASS: {name} — {count} subskills, cited '{doc_ref}'")

if all_passed:
    print("ALL 4 Grade 8 EMS expanded topics verified with authoritative curriculum doc citations!")
else:
    sys.exit(1)
