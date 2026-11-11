import re
from pathlib import Path

ROOT = Path("caps-ai-backend/app/utils")
py_files = list(ROOT.rglob("*.py"))

fixed = []

for p in py_files:
    if "backups" in str(p) or "templates" in str(p):
        continue
    content = p.read_text(encoding="utf-8")
    original = content

    # Replace CAPS in prompt strings
    # e.g. "Use the CAPS calculation principle" -> "Use the standard curriculum calculation principle"
    # e.g. "CAPS markup formula" -> "standard markup formula"
    # e.g. "according to CAPS" -> "according to the curriculum standards"
    # e.g. "CAPS requirements" -> "curriculum requirements"
    content = re.sub(r'\bCAPS calculation principle\b', 'standard calculation principle', content)
    content = re.sub(r'\bCAPS "What I WANT / What I HAVE"\b', '"What I WANT / What I HAVE"', content)
    content = re.sub(r'\bCAPS formula\b', 'standard formula', content)
    content = re.sub(r'\bCAPS markup\b', 'standard markup', content)
    content = re.sub(r'\bCAPS geometric reasons?\b', 'standard geometric reasons', content)
    content = re.sub(r'\bCAPS weight\b', 'curriculum weight', content)
    content = re.sub(r'\bCAPS format\b', 'standard format', content)
    content = re.sub(r'\bunder CAPS\b', 'under national curriculum standards', content)
    content = re.sub(r'\bCAPS curriculum\b', 'national curriculum', content)

    if content != original:
        p.write_text(content, encoding="utf-8")
        fixed.append(str(p.relative_to(ROOT)))

print(f"Fixed CAPS leaks in {len(fixed)} files:")
for f in fixed:
    print(f"  {f}")
