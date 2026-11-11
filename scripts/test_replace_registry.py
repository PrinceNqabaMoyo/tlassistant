import json

with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find all entries for Grade 9 Math
non_gr9_math_before = []
gr9_math_entries = []
non_gr9_math_after = []

found_gr9 = False
passed_gr9 = False

for item in data:
    is_gr9_math = str(item.get('grade')) == '9' and 'math' in item.get('subject', '').lower()
    if is_gr9_math:
        found_gr9 = True
        gr9_math_entries.append(item)
    else:
        if not found_gr9:
            non_gr9_math_before.append(item)
        else:
            non_gr9_math_after.append(item)

print(f"Before: {len(non_gr9_math_before)}, Gr9 Math: {len(gr9_math_entries)}, After: {len(non_gr9_math_after)}")
