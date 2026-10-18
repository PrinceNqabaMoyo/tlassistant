#!/usr/bin/env python3
"""
E2E Specification Anti-Hollywood Auditor
Fundile Automated Verification Engine

Enforces Rules 0d-1 through 0d-7 and e2e/E2E_CONTRACT.md:
  - AUD-01: Zero Silent Skips (no `if (isVisible())`, `if (count() > 0)`, or catch suppressions)
  - AUD-02: Zero Privilege Spoofing (no `?persona=admin` or `?persona=super_admin` in URLs)
  - AUD-03: Zero Backdoor Database Mutations (no `approveTestPayment()` mid-test)
  - AUD-04: Source-Code Grounding (zero phantom `data-testid` selectors)

Usage:
  python scripts/audit_e2e_specs.py
  python scripts/audit_e2e_specs.py --file e2e/set1_interactive_side_by_side.spec.js
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Ensure stdout and stderr handle utf-8 on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Terminal color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

# Audit check codes & metadata
RULE_METADATA = {
    "AUD-01": {
        "title": "Silent Skip Detection",
        "description": "Locators wrapped in conditional statements (isVisible, count) or empty catch blocks.",
        "severity": "FATAL",
    },
    "AUD-02": {
        "title": "Privilege Spoofing Detection",
        "description": "Super Admin privileges spoofed via URL query parameters (?persona=admin).",
        "severity": "FATAL",
    },
    "AUD-03": {
        "title": "Mid-Test Backdoor Mutation",
        "description": "Database helper scripts (e.g. approveTestPayment) called during test execution.",
        "severity": "FATAL",
    },
    "AUD-04": {
        "title": "Phantom Selector Detection",
        "description": "Locator references a data-testid not present in src/ source components.",
        "severity": "FATAL",
    },
}

class Violation:
    def __init__(self, rule_code: str, file_path: str, line_no: int, line_content: str, message: str):
        self.rule_code = rule_code
        self.file_path = file_path
        self.line_no = line_no
        self.line_content = line_content.strip()
        self.message = message

    def __str__(self):
        meta = RULE_METADATA.get(self.rule_code, {})
        color = RED if meta.get("severity") == "FATAL" else YELLOW
        return (
            f"  {color}[{self.rule_code}] {meta.get('title')}{RESET}\n"
            f"    {BOLD}File:{RESET} {self.file_path}:{self.line_no}\n"
            f"    {BOLD}Issue:{RESET} {self.message}\n"
            f"    {DIM}Line {self.line_no}: {self.line_content}{RESET}\n"
        )


def collect_source_test_ids(src_dir: Path) -> Tuple[Set[str], Set[str], Set[str]]:
    """
    Scans src/ in a single fast pass for all declared data-testid values,
    dynamic template prefixes, and source string literals.
    Returns:
      (exact_test_ids, dynamic_prefixes, all_source_tokens)
    """
    exact_ids: Set[str] = set()
    dynamic_prefixes: Set[str] = set()
    all_tokens: Set[str] = set()

    testid_pattern = re.compile(
        r"""data-testid\s*=\s*(?:["']([^"']+)["']|\{\s*["']([^"']+)["']\s*\}|\{\s*`([^`$]+)\$\{|`([^`$]+)\$\{)"""
    )
    ternary_pattern = re.compile(
        r"""data-testid\s*=\s*\{[^}]*?\?\s*['"]([a-zA-Z0-9_-]+)['"]\s*:\s*['"]([a-zA-Z0-9_-]+)['"]"""
    )
    token_pattern = re.compile(r"""[a-zA-Z0-9_-]{3,}""")

    extensions = {".jsx", ".js", ".tsx", ".ts", ".html"}

    for root, _, files in os.walk(src_dir):
        for f in files:
            if any(f.endswith(ext) for ext in extensions):
                file_path = Path(root) / f
                try:
                    content = file_path.read_text(encoding="utf-8", errors="ignore")
                    for match in testid_pattern.finditer(content):
                        if match.group(1):
                            exact_ids.add(match.group(1))
                        elif match.group(2):
                            exact_ids.add(match.group(2))
                        elif match.group(3):
                            dynamic_prefixes.add(match.group(3))
                        elif match.group(4):
                            dynamic_prefixes.add(match.group(4))

                    for match in ternary_pattern.finditer(content):
                        exact_ids.add(match.group(1))
                        exact_ids.add(match.group(2))

                    # Index all alphanumeric words/identifiers
                    for tok in token_pattern.findall(content):
                        all_tokens.add(tok)
                except Exception as e:
                    print(f"Warning: unable to parse {file_path}: {e}", file=sys.stderr, flush=True)

    return exact_ids, dynamic_prefixes, all_tokens


def audit_spec_file(
    file_path: Path,
    exact_test_ids: Set[str],
    dynamic_prefixes: Set[str],
    all_tokens: Set[str]
) -> List[Violation]:
    """Audits a single Playwright spec file against Rules AUD-01 through AUD-04."""
    violations: List[Violation] = []

    try:
        lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr, flush=True)
        return violations

    in_test_body = False
    preflight_zone = True

    # Regex patterns for AUD checks
    silent_skip_patterns = [
        (re.compile(r"""if\s*\([^)]*\.isVisible\(\)"""), "Conditional 'if' check wrapping isVisible() causes silent skipping on failure"),
        (re.compile(r"""if\s*\([^)]*\.count\(\)\s*>"""), "Conditional 'if' check wrapping count() causes silent skipping on failure"),
        (re.compile(r"""\.isVisible\(\)\.catch\("""), "Catching isVisible() failure suppresses assertion failures"),
        (re.compile(r"""\?\s*(?:await\s+)?[a-zA-Z0-9_$.]+\.isVisible\("""), "Ternary expression branching on isVisible() introduces conditional skipping"),
    ]

    privilege_spoof_pattern = re.compile(r"""(?:\?|&)persona=(?:admin|super_admin)""")
    backdoor_payment_pattern = re.compile(r"""\bapproveTestPayment\s*\(""")

    # Match locators with data-testid
    testid_usage_pattern = re.compile(r"""data-testid=["']([^"']+)["']""")

    for idx, line in enumerate(lines, start=1):
        # Track boundary of test body vs pre-flight setup
        if "test(" in line or "test.only(" in line:
            in_test_body = True
        if "browser" in line and ("launch(" in line or "newPage(" in line):
            preflight_zone = False

        # Strip single-line comments before running checks
        code_part = line.split("//")[0]

        # AUD-01: Silent Skip Checks
        for pattern, msg in silent_skip_patterns:
            if pattern.search(code_part):
                violations.append(Violation("AUD-01", str(file_path), idx, line, msg))

        # AUD-02: Privilege Spoofing
        if privilege_spoof_pattern.search(code_part):
            violations.append(
                Violation(
                    "AUD-02",
                    str(file_path),
                    idx,
                    line,
                    "Forbidden URL query parameter (?persona=admin). Super Admin must use authentic credentials.",
                )
            )

        # AUD-03: Backdoor Mid-Test Database Mutations
        if backdoor_payment_pattern.search(code_part):
            if not preflight_zone:
                violations.append(
                    Violation(
                        "AUD-03",
                        str(file_path),
                        idx,
                        line,
                        "Mid-test backdoor database write (approveTestPayment). Payment approval must be executed through the Super Admin UI.",
                    )
                )

        # AUD-04: Phantom Selectors (Source Code Grounding)
        for match in testid_usage_pattern.finditer(line):
            testid = match.group(1)
            # Handle template expressions in test files, e.g. payment-row-${testEmail}
            if "${" in testid:
                prefix = testid.split("${")[0]
                matched_prefix = any(prefix.startswith(dp) or dp.startswith(prefix) for dp in dynamic_prefixes)
                matched_raw = prefix in all_tokens
                if not matched_prefix and not matched_raw:
                    violations.append(
                        Violation(
                            "AUD-04",
                            str(file_path),
                            idx,
                            line,
                            f"Phantom selector prefix: '{prefix}' not found in any source file in src/",
                        )
                    )
            else:
                matched_dynamic = any(testid.startswith(dp) for dp in dynamic_prefixes)
                if testid not in exact_test_ids and testid not in all_tokens and not matched_dynamic:
                    violations.append(
                        Violation(
                            "AUD-04",
                            str(file_path),
                            idx,
                            line,
                            f"Phantom selector: '[data-testid=\"{testid}\"]' is not defined in any component in src/",
                        )
                    )

    return violations


def main():
    parser = argparse.ArgumentParser(description="Audit Playwright E2E specs for anti-Hollywood compliance.")
    parser.add_argument("--file", type=str, help="Audit a specific spec file instead of the whole e2e directory.")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    src_dir = project_root / "src"
    e2e_dir = project_root / "e2e"

    print(f"\n{BOLD}{CYAN}======================================================================{RESET}", flush=True)
    print(f"{BOLD}{CYAN}   FUNDILE E2E SPECIFICATION MECHANICAL AUDITOR (ANTI-HOLLYWOOD)    {RESET}", flush=True)
    print(f"{BOLD}{CYAN}======================================================================{RESET}\n", flush=True)

    print(f"[*] Indexing source components in {src_dir}...", flush=True)
    exact_test_ids, dynamic_prefixes, all_tokens = collect_source_test_ids(src_dir)
    print(f"   [V] Discovered {len(exact_test_ids)} exact data-testid attributes.", flush=True)
    print(f"   [V] Discovered {len(dynamic_prefixes)} dynamic testid prefixes.", flush=True)
    print(f"   [V] Indexed {len(all_tokens)} source identifier tokens.\n", flush=True)

    # Determine files to audit
    files_to_audit: List[Path] = []
    if args.file:
        target_path = Path(args.file)
        if not target_path.is_absolute():
            target_path = project_root / target_path
        if not target_path.exists():
            print(f"{RED}Error: File not found: {target_path}{RESET}", file=sys.stderr)
            sys.exit(1)
        files_to_audit.append(target_path)
    else:
        for root, _, files in os.walk(e2e_dir):
            for f in files:
                if f.endswith(".spec.js") or f == "runParticipantSet.js":
                    files_to_audit.append(Path(root) / f)

    files_to_audit.sort()
    print(f"[*] Auditing {len(files_to_audit)} Playwright specification(s)...\n", flush=True)

    all_violations: List[Violation] = []
    file_violation_counts: Dict[str, int] = {}

    for spec_file in files_to_audit:
        rel_path = spec_file.relative_to(project_root)
        violations = audit_spec_file(spec_file, exact_test_ids, dynamic_prefixes, all_tokens)
        if violations:
            file_violation_counts[str(rel_path)] = len(violations)
            all_violations.extend(violations)
            print(f"{RED}[FAIL] {rel_path} ({len(violations)} violation(s)){RESET}", flush=True)
            for v in violations:
                print(v, flush=True)
        else:
            print(f"{GREEN}[PASS] {rel_path} (0 violations -- Clean){RESET}", flush=True)

    # Summary
    print(f"\n{BOLD}{CYAN}----------------------------------------------------------------------{RESET}", flush=True)
    print(f"{BOLD}AUDIT SUMMARY{RESET}", flush=True)
    print(f"{BOLD}{CYAN}----------------------------------------------------------------------{RESET}", flush=True)
    print(f"Total Specs Audited: {len(files_to_audit)}", flush=True)
    print(f"Total Violations:    {len(all_violations)}", flush=True)

    rule_counts: Dict[str, int] = {}
    for v in all_violations:
        rule_counts[v.rule_code] = rule_counts.get(v.rule_code, 0) + 1

    for rule_code, meta in RULE_METADATA.items():
        count = rule_counts.get(rule_code, 0)
        status_color = GREEN if count == 0 else RED
        print(f"  {status_color}{rule_code}: {meta['title']:<30} {count} violation(s){RESET}", flush=True)

    if all_violations:
        print(f"\n{BOLD}{RED}[FAIL] AUDIT FAILED: Mechanical violations found.{RESET}", flush=True)
        print(f"Refer to {BOLD}e2e/E2E_CONTRACT.md{RESET} for remediation guidelines.\n", flush=True)
        sys.exit(1)
    else:
        print(f"\n{BOLD}{GREEN}[PASS] AUDIT PASSED: All specifications meet the Zero-Theater contract.{RESET}\n", flush=True)
        sys.exit(0)


if __name__ == "__main__":
    main()
