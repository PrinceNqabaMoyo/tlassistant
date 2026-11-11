import glob
import os

targets = [
    "grade7_mathematics",
    "grade8_mathematics",
    "grade9_mathematics",
    "grade10_mathematics",
    "grade11_mathematics",
    "grade12_mathematics",
    "grade10_physical_sciences",
    "grade11_physical_sciences",
    "grade12_physical_sciences",
    "grade10_life_sciences",
    "life_sciences",
    "technical_mathematics",
    "natural_sciences"
]

for t in targets:
    p = os.path.join("caps-ai-backend/app/utils", t)
    files = glob.glob(f"{p}/**/*.py", recursive=True)
    print(f"\n=== {t} ({len(files)} files) ===")
    for f in sorted(files):
        print(f"  {os.path.relpath(f, p)}")
