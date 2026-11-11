import json

d = json.load(open("caps-ai-backend/app/services/caps_term_registry_data.json", encoding="utf-8"))
print("Type of data:", type(d))
if isinstance(d, list):
    print("Length of list:", len(d))
    print("Sample item keys:", list(d[0].keys()))
    # Find Grade 11 MathLit items
    g11_mathlit = [item for item in d if item.get("grade") in (11, "11", "Grade 11") and "Literacy" in item.get("subject", "")]
    print(f"Found {len(g11_mathlit)} items for Grade 11 Mathematical Literacy:")
    for item in g11_mathlit:
        print(f"Term: {item.get('term')}, Topic: {item.get('topic')}, Key: {item.get('generator_key')}")
