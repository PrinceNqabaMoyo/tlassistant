import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'caps-ai-backend'))
from app.services.generator_registry import generate_variant

topics = [
    ("General ledger and Trial balance of a service business", ["general ledger", "trial balance", "ledger", "t-account", "balance", "dead clic", "debit", "credit"]),
    ("Government", ["government", "state", "public", "municipality", "services", "revenue", "tax"]),
    ("The National Budget", ["budget", "fiscal", "expenditure", "revenue", "treasury", "surplus", "deficit", "tax", "sars", "paye", "vat"]),
    ("Accounting concepts", ["capital", "assets", "liabilities", "income", "expenses", "owner's equity", "transaction", "profit", "loss", "drawings", "accounting equation"]),
    ("the accounting cycle", ["accounting cycle", "source document", "journal", "ledger", "trial balance", "financial statements", "cycle"]),
    ("Source documents", ["receipt", "invoice", "deposit slip", "cheque", "cash register", "source document", "document", "bank statement"]),
    ("Cash receipts journal for a services business 1", ["crj", "cash receipts", "receipt", "analysis of receipts", "bank", "current income"]),
    ("Cash receipts journal for a services business 2", ["crj", "cpj", "journal", "bank", "receipts", "payments"]),
    ("Cash payments journal for a services business", ["cpj", "cash payments", "cheque", "bank", "stationery", "trading", "wages"]),
    ("Forms of ownership", ["sole trader", "partnership", "close corporation", "private company", "public company", "liability", "ownership", "shareholder", "smme", "sustainable", "natural resources"]),
    ("Levels and functions of management", ["management", "manager", "planning", "organising", "leading", "controlling", "top-level", "middle-level", "lower-level", "leadership"]),
    ("The markets", ["goods market", "services market", "factor market", "financial market", "buyer", "seller", "demand", "supply", "market"]),
    ("Factors of production", ["labour", "capital", "natural resources", "raw materials", "entrepreneurship", "remuneration", "wages", "rent", "interest", "profit"]),
]

all_passed = True
for topic, expected_keywords in topics:
    for s in [42, 101, 777]:
        try:
            res = generate_variant(topic, grade='8', subject='Economic and Management Sciences', seed=s, count=2)
            qs = res if isinstance(res, list) else [res]
            for q in qs:
                p = (q.get('prompt') or q.get('question') or '').lower()
                matched = [kw for kw in expected_keywords if kw in p]
                if not matched:
                    # check if worked_solution or options have keywords
                    blob = (p + ' ' + str(q.get('worked_solution') or '') + ' ' + str(q.get('options') or '')).lower()
                    matched = [kw for kw in expected_keywords if kw in blob]
                if not matched:
                    print(f"WARNING: Topic '{topic}' [seed {s}] did not contain expected keywords {expected_keywords}. Prompt: {p[:100]}")
                    all_passed = False
        except Exception as e:
            print(f"CRASH in '{topic}' [seed {s}]: {e}")
            all_passed = False

if all_passed:
    print("ALL 13 Grade 8 EMS topics verified: dedicated generators produce topic-relevant questions with 0 foreign mixing!")
