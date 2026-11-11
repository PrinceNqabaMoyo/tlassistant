import os
from pathlib import Path

base = Path("caps-ai-backend/app/utils/mathematical_literacy")
gr10_dirs = [
    "budgets",
    "banking_tax",
    "tariffs",
    "numbers_calculations",
    "data_handling",
    "scale_maps",
    "assembly_packaging",
    "perimeter_area",
    "patterns_relationships",
    "probability",
    "measuring"
]

for d in gr10_dirs:
    dp = base / d
    if dp.exists():
        py_files = list(dp.glob("*.py"))
        print(f"Directory: {d} ({len(py_files)} files)")
        for pf in py_files:
            lines = pf.read_text(encoding="utf-8", errors="ignore").splitlines()
            print(f"   {pf.name}: {len(lines)} lines")
