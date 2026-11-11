import os
from pathlib import Path

targets = ["income_tax_sars_compound", "taxable_income_elementary", "7{ }50", "tax_bracket_elementary"]

for root, dirs, files in os.walk("."):
    if "node_modules" in root or ".git" in root or "venv" in root or ".system_generated" in root or "dist" in root:
        continue
    for file in files:
        if file.endswith((".py", ".js", ".jsx", ".json", ".md")):
            fpath = os.path.join(root, file)
            try:
                content = Path(fpath).read_text(encoding="utf-8", errors="ignore")
                for t in targets:
                    if t in content:
                        print(f"FOUND '{t}' in: {fpath}")
            except Exception:
                pass
