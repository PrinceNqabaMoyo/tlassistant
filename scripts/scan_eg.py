import glob, re

for f in sorted(glob.glob('caps-ai-backend/app/utils/grade7_*/*.py') + glob.glob('caps-ai-backend/app/utils/natural_sciences/ns7_*.py')):
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    matches = re.findall(r"e\.g\.\s*['\"][^'\"]+['\"]", text)
    if matches:
        print(f"{f}: {matches}")
