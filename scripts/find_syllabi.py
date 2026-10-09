import os
from pathlib import Path

REPO_ROOT = Path(r"c:\Users\princ\fundile-tlassistant-vite")
AUTO_ROOT = REPO_ROOT / "caps-ai-backend" / "curriculum_docs_auto"
MANUAL_ROOT = REPO_ROOT / "caps-ai-backend" / "curriculum_docs"

print("Scanning for Syllabus files in curriculum_docs_auto...")
auto_syllabi = sorted(list(AUTO_ROOT.glob("*/Syllabus.md")))
for s in auto_syllabi:
    print(f"  {s.parent.name}: {s.name} ({s.stat().st_size} bytes)")

print(f"Total Syllabus files found in curriculum_docs_auto: {len(auto_syllabi)}")
