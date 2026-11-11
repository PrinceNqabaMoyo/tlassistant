"""
diagnose_grade8.py: Systematically inspect Grade 8 Maths, EMS, and NS generators
for prompt leaks, phrasing giveaways, bold quote issues, and diagram requirements.
"""
import glob
import os
import re

MATH_FILES = glob.glob('caps-ai-backend/app/utils/grade8_mathematics/*.py')
EMS_FILES = glob.glob('caps-ai-backend/app/utils/grade8_ems/*.py')
NS_FILES = glob.glob('caps-ai-backend/app/utils/**/*natural_sciences*.py', recursive=True) + glob.glob('caps-ai-backend/app/utils/grade8_natural_sciences/*.py')

def scan_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    issues = []
    # 1. Bold quote leaks
    if re.search(r'\*\*\s*["\u201c]', content):
        issues.append('bold_quote_wrap')
    # 2. Method giveaways in prompts
    matches = re.findall(r'(?i)\b(difference of (two )?squares|bodmas|pemdas|additive inverse|multiplicative inverse|distributive (law|property))\b', content)
    if matches:
        issues.append(f'method_names: {[m[0] for m in matches]}')
    # 3. Formula giveaways
    if re.search(r'(?i)\bmaximum\s*[-\u2212]\s*minimum\b', content):
        issues.append('formula_leak: maximum - minimum')
    if re.search(r'(?i)\(median\)', content):
        issues.append('answer_leak: (median)')
    if re.search(r'(?i)classify whether.*prism or pyramid', content):
        issues.append('giveaway: classify whether prism or pyramid')
    if 'Mitchells Plain' in content:
        issues.append('hardcoded: Mitchells Plain')
    if 'Imran' in content:
        issues.append('hardcoded: Imran')
    return issues

print("=== Grade 8 Mathematics ===")
for mf in sorted(MATH_FILES):
    res = scan_file(mf)
    if res:
        print(f"{os.path.basename(mf)}: {res}")

print("\n=== Grade 8 EMS ===")
for ef in sorted(EMS_FILES):
    res = scan_file(ef)
    if res:
        print(f"{os.path.basename(ef)}: {res}")

print("\n=== Grade 8 Natural Sciences ===")
for nf in sorted(NS_FILES):
    res = scan_file(nf)
    if res:
        print(f"{os.path.basename(nf)}: {res}")
