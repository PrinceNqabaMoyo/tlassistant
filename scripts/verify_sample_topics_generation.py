import urllib.request
import urllib.parse
import json

test_topics = [
    # Grade 7
    (7, "Mathematics", "Working with whole numbers"),
    (7, "Natural Sciences", "The Biosphere"),
    (7, "Economic and Management Sciences", "Needs and Wants"),
    # Grade 8
    (8, "Mathematics", "Integers"),
    (8, "Natural Sciences", "Glossary1"),
    (8, "Economic and Management Sciences", "Accounting concepts"),
    # Grade 9
    (9, "Mathematics", "Integers"),
    (9, "Natural Sciences", "Cells as the basic units of life"),
    (9, "Economic and Management Sciences", "The circular flow"),
    # Grade 10
    (10, "Mathematics", "Algebraic expressions"),
    (10, "Mathematical Literacy", "Personal income expenditure and budgets"),
    (10, "Technical Mathematics", "Number Systems"),
    (10, "Physical Sciences", "Classification of matter"),
    (10, "Life Sciences", "The chemistry of life"),
    (10, "Accounting", "Financial accounting of a sole trader"),
    (10, "Business Studies", "The macro environment"),
    # Grade 11
    (11, "Mathematics", "Exponents and surds"),
    (11, "Mathematical Literacy", "Interest banking and inflation"),
    (11, "Technical Mathematics", "Exponents and surds"),
    (11, "Physical Sciences", "Vectors in two dimensions"),
    (11, "Life Sciences", "Photosynthesis"),
    (11, "Accounting", "Bank reconciliation"),
    (11, "Business Studies", "The challenges of the business environments"),
    # Grade 12
    (12, "Mathematics", "Differential calculus"),
    (12, "Mathematical Literacy", "Income tax"),
    (12, "Technical Mathematics", "Complex numbers"),
    (12, "Physical Sciences", "Momentum and Impulse"),
    (12, "Life Sciences", "Genetics and inheritance"),
    (12, "Accounting", "Companies"),
    (12, "Business Studies", "Impact of recent legislation on businesses"),
]

print(f"Testing {len(test_topics)} curriculum topics against http://localhost:5173/api/generate ...")
passed = 0
failed = []

for grade, subject, topic in test_topics:
    params = urllib.parse.urlencode({
        "subject": subject,
        "grade": grade,
        "topic": topic,
        "seed": 42
    })
    url = f"http://localhost:5173/api/generate?{params}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data.get("success") or "questions" in data:
                passed += 1
                q = data.get("questions", [data])[0] if isinstance(data.get("questions"), list) else data
                prompt = (q.get("prompt") or q.get("question") or q.get("title") or "")[:40].replace('\n', ' ')
                print(f"  [OK] Gr {grade:2d} {subject:32s} -> \"{prompt}...\"")
            else:
                failed.append((grade, subject, topic, "Payload missing success or questions"))
                print(f"  [FAIL] Gr {grade:2d} {subject}: Response format error")
    except Exception as e:
        failed.append((grade, subject, topic, str(e)))
        print(f"  [FAIL] Gr {grade:2d} {subject}: {e}")

print(f"\nSummary: {passed}/{len(test_topics)} passed.")
if failed:
    print(f"Failed count: {len(failed)}")
    for f in failed:
        print(f"  - Gr {f[0]} {f[1]} ({f[2]}): {f[3]}")
