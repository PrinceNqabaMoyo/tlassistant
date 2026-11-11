"""Check that a named RULE-ANCHOR is present in every required rule/skill file.

Usage: python scripts/check_rule_presence.py --rule diagram_description_design_law
Exit 0 only if the anchor appears in all files listed for that rule.
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RULE_FILES = {
    "diagram_description_design_law": [
        "diagram_doctrine.md",
        ".agents/AGENTS.md",
        ".agents/skills/caps-generator-contract/SKILL.md",
        ".agents/skills/curriculum-topic-curator/SKILL.md",
        ".agents/skills/flash-remediation-protocol/SKILL.md",
    ],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rule", required=True, choices=sorted(RULE_FILES))
    args = ap.parse_args()
    anchor = f"RULE-ANCHOR: {args.rule}"
    missing = []
    for rel in RULE_FILES[args.rule]:
        p = ROOT / rel
        ok = p.exists() and anchor in p.read_text(encoding="utf-8", errors="ignore")
        print(f"  {'PASS' if ok else 'FAIL'}  {rel}")
        if not ok:
            missing.append(rel)
    total = len(RULE_FILES[args.rule])
    print(f"{total - len(missing)}/{total} files contain '{anchor}'")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
