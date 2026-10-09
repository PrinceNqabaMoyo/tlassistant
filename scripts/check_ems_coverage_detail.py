import sys
import re
from pathlib import Path

REPO_ROOT = Path(r"c:\Users\princ\fundile-tlassistant-vite")
BACKEND_DIR = REPO_ROOT / "caps-ai-backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key

auto_dir = BACKEND_DIR / "curriculum_docs_auto"

for grade in ["7", "8", "9"]:
    folder = auto_dir / f"EMS_Gr{grade}"
    print(f"\n=================== EMS GRADE {grade} ===================")
    for term_dir in sorted(folder.glob("Term*")):
        for md_file in sorted(term_dir.glob("*.md")):
            raw_title = md_file.stem
            clean_title = re.sub(r"^\d+[\.\s_]+", "", raw_title).strip()
            if not clean_title or clean_title.lower() == "revision":
                continue
            key = resolve_generator_key(topic=clean_title, grade=grade, subject="EMS")
            func = ALL_GENERATORS.get(key) if key else None
            func_name = getattr(func, "__name__", str(func))
            module_name = getattr(func, "__module__", "unknown")
            print(f"[{term_dir.name}] {clean_title}")
            print(f"   -> key: {key}")
            print(f"   -> func: {module_name}.{func_name}")
