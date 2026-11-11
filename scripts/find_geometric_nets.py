import re
content = open("src/components/workspace/UniversalWorkspace.jsx", encoding="utf-8").read()

matches = [m.start() for m in re.finditer(r"geometric_nets", content)]
for idx, p in enumerate(matches):
    print(f"Match {idx} at {p}:")
    print(content[max(0, p - 80):min(len(content), p + 120)])
    print("-" * 50)
