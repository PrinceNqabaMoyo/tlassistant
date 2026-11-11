with open('public/diagrams/human_ear_wikimedia.svg', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'rect7140' in l or 'rect7136' in l:
        print(f"Line {i+1}: {l.strip()[:100]}")
