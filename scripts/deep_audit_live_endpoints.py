import urllib.request
import json
import re
import sys

TOPICS_GR10 = [
    "Patterns, relationships and representations",
    "Measuring: length, weight, volume and temperature",
    "Measurement: perimeter and area",
    "Numbers and calculations with numbers",
    "Financial documents and tariff systems",
    "Personal income, expenditure and budgets",
    "Banking, interest and taxation",
    "Scale, maps and plans",
    "Assembly diagrams, floor plans and packaging",
    "Data handling",
    "Probability",
    "Conversions and time",
]

TOPICS_GR11 = [
    "Conversions and time",
    "Exchange rates",
    "Interest, banking and inflation",
    "Patterns, relationships and representations",
    "Plans and other representations",
    "Finance (taxation and UIF)",
    "Area and volume",
    "Data handling",
    "Maps",
    "Financial documents and tariff systems",
    "Weight and temperature",
    "Probability",
]

def audit():
    total_audited = 0
    total_passed = 0
    failures = []
    
    for grade, topics in [(10, TOPICS_GR10), (11, TOPICS_GR11)]:
        print(f"\n--- AUDITING GRADE {grade} LIVE ENDPOINTS ---")
        for topic in topics:
            url = (
                f"http://127.0.0.1:5001/api/generate?subject=Mathematical+Literacy"
                f"&grade={grade}&topic={urllib.parse.quote(topic)}&count=5&seed=42"
            )
            req = urllib.request.Request(url)
            try:
                resp = urllib.request.urlopen(req, timeout=10)
                data = json.loads(resp.read().decode())
                assert data.get("success"), f"API returned success=False: {data}"
                questions = data.get("questions", [])
                assert len(questions) == 5, f"Expected 5 questions, got {len(questions)}"
                
                # Check each question
                for q in questions:
                    prompt = q.get("prompt", "")
                    ans = q.get("expected_answer", "")
                    options = q.get("options", [])
                    
                    # Rule checks
                    assert "{ }" not in prompt and "7{ }50" not in prompt, f"Corrupted brace in prompt: {prompt}"
                    assert "{ }" not in ans, f"Corrupted brace in expected answer: {ans}"
                    
                    # Distractor check
                    for opt in options:
                        assert not re.search(r"\(Alt(?:ernative)?\s*\d*\)", opt, re.IGNORECASE), f"Synthetic distractor: {opt}"
                        assert not re.search(r"\(Option\s*\d*\)", opt, re.IGNORECASE), f"Synthetic option: {opt}"
                        assert "{ }" not in opt, f"Corrupted brace in option: {opt}"
                
                print(f"  [PASS] Gr{grade} {topic} (5 variants, 0 leaks, 0 synthetic distractors)")
                total_passed += 1
            except Exception as e:
                print(f"  [FAIL] Gr{grade} {topic}: {e}")
                failures.append((grade, topic, str(e)))
            total_audited += 1

    print(f"\nSummary: {total_passed}/{total_audited} topics passed live end-to-end API generation.")
    if failures:
        print("FAILURES:", failures)
        sys.exit(1)
    else:
        print("ALL 24 TOPICS PASSED LIVE GENERATION AUDIT!")
        sys.exit(0)

if __name__ == "__main__":
    audit()
