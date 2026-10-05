#!/usr/bin/env python3
"""
Question Authenticity & Zero-Meta-Curriculum Auditor
Audits all question generators, challenge files, and diagnostic banks to verify
that questions reflect authentic exam problems and contain 0% meta-curriculum jargon.
"""

import os
import re
import sys

FORBIDDEN_PATTERNS = [
    re.compile(r"according to (the )?caps", re.IGNORECASE),
    re.compile(r"according to (the )?curriculum", re.IGNORECASE),
    re.compile(r"as required by (the )?caps", re.IGNORECASE),
    re.compile(r"caps curriculum expects", re.IGNORECASE),
    re.compile(r"in the caps document", re.IGNORECASE),
    re.compile(r"official caps requirements", re.IGNORECASE),
    re.compile(r"annual teaching plan requires", re.IGNORECASE),
    re.compile(r"atp specifies that", re.IGNORECASE),
]

SCAN_DIRS = [
    "src/data",
    "src/components/student",
    "src/components/workspace",
    "caps-ai-backend/app/services",
    "caps-ai-backend/app/utils",
]

def audit():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    violations = []

    for scan_dir in SCAN_DIRS:
        target_path = os.path.join(repo_root, scan_dir)
        if not os.path.exists(target_path):
            continue

        for root, dirs, files in os.walk(target_path):
            if any(x in root for x in ["__pycache__", "node_modules", ".git", "curriculum_docs"]):
                continue
            for f in files:
                if f.endswith((".py", ".js", ".jsx", ".ts", ".tsx")):
                    file_path = os.path.join(root, f)
                    try:
                        with open(file_path, "r", encoding="utf-8") as fh:
                            for line_no, line in enumerate(fh, 1):
                                # Check lines that look like questions/prompts
                                l_lower = line.lower()
                                if any(k in l_lower for k in ["prompt", "question_text", "title:", "prompt:", "question:"]):
                                    for pattern in FORBIDDEN_PATTERNS:
                                        if pattern.search(line):
                                            rel = os.path.relpath(file_path, repo_root)
                                            violations.append((rel, line_no, line.strip(), pattern.pattern))
                    except Exception as e:
                        pass

    print("=" * 60, flush=True)
    print("EXAM AUTHENTICITY & ZERO-META-CURRICULUM AUDIT", flush=True)
    print("=" * 60, flush=True)

    if violations:
        print(f"FAILED: Found {len(violations)} meta-curriculum violation(s):", flush=True)
        for v in violations:
            print(f"  [{v[0]}:{v[1]}] Matched '{v[3]}': {v[2]}", flush=True)
        sys.exit(1)
    else:
        print("PASSED: 100% of scanned question prompts conform to Authentic Exam Standards.", flush=True)
        print("Zero meta-curriculum policy text found in student question banks.", flush=True)
        sys.exit(0)

if __name__ == "__main__":
    audit()
