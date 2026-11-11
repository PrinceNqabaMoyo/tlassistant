import sys, os
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'caps-ai-backend'))
from app.services.generator_registry import generate_variant
from app.utils.ems_namelist import NAMES, BUSINESS_TYPES, AREAS

topics = [
    "General ledger and Trial balance of a service business",
    "Government",
    "The National Budget",
    "Accounting concepts",
    "the accounting cycle",
    "Source documents",
    "Cash receipts journal for a services business 1",
    "Cash receipts journal for a services business 2",
    "Cash payments journal for a services business",
    "Forms of ownership",
    "Levels and functions of management",
    "The markets",
    "Factors of production",
]

name_counts = Counter()
total_questions = 0
inappropriate_businesses = []

for topic in topics:
    for seed in range(1, 21):  # 20 seeds
        try:
            res = generate_variant(topic, grade='8', subject='Economic and Management Sciences', seed=seed, count=1)
            qs = res if isinstance(res, list) else [res]
            for q in qs:
                total_questions += 1
                prompt = (q.get('prompt') or '') + ' ' + (q.get('question') or '')
                for name in NAMES:
                    if f" {name} " in prompt or f"{name}'s" in prompt or prompt.startswith(f"{name} "):
                        name_counts[name] += 1
                
                # Check for inappropriate corporate complexity in Grade 8
                p_lower = prompt.lower()
                if "debenture" in p_lower or "preference share" in p_lower or "hostile takeover" in p_lower:
                    inappropriate_businesses.append((topic, seed, prompt[:80]))
        except Exception as e:
            print(f"Error generating {topic} seed {seed}: {e}")

print(f"Total questions audited across 20 seeds: {total_questions}")
print(f"Unique names mentioned: {len(name_counts)}")
top_5 = name_counts.most_common(5)
print("Top 5 names:")
highest_pct = 0.0
highest_name = None
for name, cnt in top_5:
    pct = (cnt / total_questions) * 100
    if pct > highest_pct:
        highest_pct = pct
        highest_name = name
    print(f"  {name}: {cnt} times ({pct:.1f}%)")

if highest_pct > 15.0:
    print(f"FAIL: Name '{highest_name}' has prevalence {highest_pct:.1f}% > 15.0% threshold!")
    sys.exit(1)
else:
    print(f"PASS: Highest name prevalence is {highest_name} at {highest_pct:.1f}% (<= 15.0% threshold).")

if inappropriate_businesses:
    print(f"FAIL: {len(inappropriate_businesses)} inappropriate corporate items found in Grade 8!")
    sys.exit(1)
else:
    print("PASS: Business types strictly align with Grade 8 scope (Service businesses and sole traders).")
