#!/usr/bin/env python3
"""
Non-Bypassable Coordinator & Swarm Pre-Commit Policy Gate
=========================================================
Executed automatically by .git/hooks/pre-commit (costing 0 LLM tokens).
Blocks any commit by Gemini 3.8 Flash (or any worker) if:
  1. Any locked referee script (validate_topic_50_archetypes.py, topic_diagram_policy_manifest.json,
     audit_diagram_description_leak.py, audit_heart_standard_plates.py) has been tampered with.
  2. Stray temporary scripts (e.g. check_*.py, temp_*.py) exist in caps-ai-backend/.
  3. Any staged generator in caps-ai-backend/app/utils/ fails validate_topic_50_archetypes.py
     (including the BLENDER_3D_FOUNDRY and CAMPBELL_CURATED_PLATE rules).
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
HASH_FILE = ROOT / "scripts" / ".referee_hashes.json"
REGISTRY_PATH = ROOT / "caps-ai-backend" / "app" / "services" / "caps_term_registry_data.json"

PROTECTED_REFEREE_FILES = [
    "scripts/validate_topic_50_archetypes.py",
    "scripts/topic_diagram_policy_manifest.json",
    "scripts/audit_diagram_description_leak.py",
    "scripts/audit_heart_standard_plates.py",
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_referee_integrity() -> bool:
    if not HASH_FILE.exists():
        print("[POLICY GATE FAIL] Missing scripts/.referee_hashes.json")
        return False
    expected = json.loads(HASH_FILE.read_text(encoding="utf-8"))
    for rel in PROTECTED_REFEREE_FILES:
        fpath = ROOT / rel
        if not fpath.exists():
            print(f"[POLICY GATE FAIL] Protected referee file deleted: {rel}")
            return False
        actual_hash = sha256_file(fpath)
        if expected.get(rel) and actual_hash != expected[rel]:
            print(
                f"[POLICY GATE FAIL] Anti-Tampering Violation: '{rel}' was modified!\n"
                f"  Expected SHA-256: {expected[rel]}\n"
                f"  Actual SHA-256:   {actual_hash}\n"
                f"  Gemini 3.8 Flash is strictly forbidden from editing referee scripts."
            )
            return False
    return True


def check_stray_temp_files() -> bool:
    res = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "caps-ai-backend/"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    untracked = [line.strip() for line in res.stdout.splitlines() if line.strip()]
    stray = [
        f for f in untracked
        if Path(f).name.startswith(("check_", "tmp_", "test_tmp_")) and f.endswith(".py")
    ]
    if stray:
        print(f"[POLICY GATE FAIL] Untracked temporary scripts in caps-ai-backend/: {stray}")
        return False
    return True


def validate_staged_generators() -> bool:
    res = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    staged_files = [line.strip() for line in res.stdout.splitlines() if line.strip()]
    util_files = [f for f in staged_files if f.startswith("caps-ai-backend/app/utils/") and f.endswith(".py")]
    if not util_files:
        return True

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    from scripts.validate_topic_50_archetypes import validate_topics

    # Identify unique (grade, subject, topic_name) matching modified generator stems
    topics_to_check: list[tuple[int, str, str]] = []
    seen: set[tuple[int, str, str]] = set()

    for uf in util_files:
        stem = Path(uf).stem
        # Extract grade from file path if present (e.g. grade9_mathematics -> 9)
        grade_match = re.search(r"grade(\d+)", uf.lower())
        target_grade = int(grade_match.group(1)) if grade_match else None

        # Strip _archetypes_01_25, _archetypes_26_50, _svg, _generator, _part1, _part2
        for suffix in (
            "_archetypes_01_25",
            "_archetypes_26_50",
            "_svg",
            "_generator",
            "_part1",
            "_part2",
        ):
            if stem.endswith(suffix):
                stem = stem[: -len(suffix)]
                break

        for entry in registry:
            entry_grade = int(entry.get("grade", 0))
            if target_grade is not None and entry_grade != target_grade:
                continue
            gen_key = str(entry.get("generator_key") or entry.get("generator_file") or "")
            matched = False
            if stem and (stem in gen_key or gen_key in stem):
                matched = True
            elif stem == "measurement_3d" and ("surface_area" in gen_key or "measurement" in gen_key):
                matched = True

            if matched:
                key = (int(entry["grade"]), str(entry["subject"]), str(entry["name"]))
                if key not in seen:
                    seen.add(key)
                    topics_to_check.append(key)

    for grade, subject, topic_name in topics_to_check:
        rc = validate_topics(grade=grade, subject=subject, topic_filter=topic_name)
        if rc != 0:
            print(f"[POLICY GATE FAIL] Staged topic failed validation: Gr{grade} {subject} - '{topic_name}'")
            return False

    return True


def main() -> int:
    if "--write-hashes" in sys.argv:
        hashes = {rel: sha256_file(ROOT / rel) for rel in PROTECTED_REFEREE_FILES}
        HASH_FILE.write_text(json.dumps(hashes, indent=2) + "\n", encoding="utf-8")
        print(f"[POLICY GATE] Locked SHA-256 referee hashes written to {HASH_FILE}")
        return 0

    if not verify_referee_integrity():
        return 1
    if not check_stray_temp_files():
        return 1
    if not validate_staged_generators():
        return 1

    print("[POLICY GATE PASS] Referee integrity, stray-file check, and 50-archetype + Blender/Campbell diagram gates passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
