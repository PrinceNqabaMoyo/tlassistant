import sys
sys.path.insert(0, 'caps-ai-backend')

from app.utils.mathematical_literacy.conversions_time_generator import generate, SUBSKILLS
import random

issues = []

for subskill in SUBSKILLS:
    for seed in [1, 2, 42, 101, 2024]:
        res = generate(subskill=subskill, seed=seed)
        q = res[0] if isinstance(res, list) else res
        options = q.get('options', [])
        ans = q.get('correct_answer', '')
        prompt = q.get('prompt', '')
        sol = q.get('worked_solution', '')

        # Check duplicate options
        if len(options) != 4:
            issues.append(f"[{subskill} seed={seed}] Option count is {len(options)}, expected 4")
        elif len(set(options)) != len(options):
            issues.append(f"[{subskill} seed={seed}] Duplicate options: {options}")

        # Check for \circ without base or \circF / \circC
        for text_field in [prompt, sol, ans]:
            if r'\circF' in text_field or r'\circC' in text_field or r'^\circ' in text_field:
                issues.append(f"[{subskill} seed={seed}] Invalid \\circ token in {text_field[:60]}")

        # Check for (Variant in options
        for opt in options:
            if '(Variant' in str(opt):
                issues.append(f"[{subskill} seed={seed}] Fallback '(Variant' in option: {opt}")

print(f"Total issues found: {len(issues)}")
for iss in issues[:40]:
    print(" -", iss)
