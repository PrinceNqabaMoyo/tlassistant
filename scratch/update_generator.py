# scratch/update_generator.py
import re
from pathlib import Path

ROOT = Path(r"c:\Users\princ\fundile-tlassistant-vite")
TARGET = ROOT / "generate_architecture_html.py"

content = TARGET.read_text(encoding="utf-8")
print(f"Target current length: {len(content)} bytes, lines: {len(content.splitlines())}")
