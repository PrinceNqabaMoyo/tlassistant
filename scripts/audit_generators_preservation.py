"""
scripts/audit_generators_preservation.py
Rule 2 & Generator Preservation Law:
Ensures zero-deletion of generator seeds, archetypes, and modules.
Fails loudly if any generator file is deleted or if total inventory drops below baseline.
"""
import os
import sys
import json
from collections import defaultdict

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UTILS_DIR = os.path.join(BASE_DIR, 'caps-ai-backend', 'app', 'utils')
BASELINE_INVENTORY_FILE = os.path.join(BASE_DIR, 'reports', 'cognitive_audit', 'generator_preservation_baseline.json')

MINIMUM_BASELINE_GENERATOR_COUNT = 200

EXPECTED_DIRECTORIES = [
    'grade10_accounting',
    'grade11_accounting',
    'grade12_accounting',
    'grade10_business_studies',
    'grade11_business_studies',
    'grade12_business_studies',
    'grade10_mathematics',
    'grade11_mathematics',
    'grade12_mathematics',
    'grade7_mathematics',
    'grade8_mathematics',
    'grade9_mathematics',
    'grade10_physical_sciences',
    'grade11_physical_sciences',
    'grade12_physical_sciences',
    'grade7_ems',
    'grade8_ems',
    'grade9_ems',
    'life_sciences',
    'natural_sciences',
    'technical_mathematics',
    'mathematical_literacy',
]

def audit_generators():
    print("=" * 70)
    print("FUNDILE GENERATOR PRESERVATION & INVENTORY AUDIT")
    print("Enforcing Generator Preservation Law (Zero-Deletion Invariant)")
    print("=" * 70)

    if not os.path.exists(UTILS_DIR):
        print(f"[ERROR] FATAL: Utils directory not found at {UTILS_DIR}")
        sys.exit(1)

    discovered = {}
    folder_counts = defaultdict(int)

    for dirpath, _, filenames in os.walk(UTILS_DIR):
        for f in filenames:
            if 'generator' in f and f.endswith('.py'):
                rel_path = os.path.relpath(os.path.join(dirpath, f), UTILS_DIR).replace('\\', '/')
                discovered[rel_path] = os.path.getsize(os.path.join(dirpath, f))
                top = rel_path.split('/')[0]
                folder_counts[top] += 1

    total_count = len(discovered)
    print(f"Discovered {total_count} generator files across {len(folder_counts)} folders.")

    for folder in sorted(EXPECTED_DIRECTORIES):
        count = folder_counts.get(folder, 0)
        if count == 0:
            print(f"[VIOLATION] Expected subject directory '{folder}' has 0 generators!")
            sys.exit(1)
        else:
            print(f"  [OK] {folder:30}: {count:2} generators")

    if total_count < MINIMUM_BASELINE_GENERATOR_COUNT:
        print(f"[FATAL] Total generator count {total_count} is less than minimum baseline {MINIMUM_BASELINE_GENERATOR_COUNT}!")
        sys.exit(1)

    os.makedirs(os.path.dirname(BASELINE_INVENTORY_FILE), exist_ok=True)

    if os.path.exists(BASELINE_INVENTORY_FILE):
        with open(BASELINE_INVENTORY_FILE, 'r', encoding='utf-8') as bf:
            baseline_data = json.load(bf)
            baseline_files = set(baseline_data.get('generators', {}).keys())

        current_files = set(discovered.keys())
        deleted_files = baseline_files - current_files

        if deleted_files:
            print("\n[CRITICAL PRESERVATION VIOLATION] The following generators were deleted without approval:")
            for df in sorted(deleted_files):
                print(f"   - {df}")
            print("\nABORTING: Generator Preservation Law forbids deletion of existing generator seeds or archetypes.")
            sys.exit(1)
        else:
            print(f"\n[PASS] PRESERVATION CHECK PASSED: 0 of {len(baseline_files)} baseline generators deleted.")
    else:
        print(f"\nCreating initial preservation baseline at {BASELINE_INVENTORY_FILE}...")
        with open(BASELINE_INVENTORY_FILE, 'w', encoding='utf-8') as bf:
            json.dump({
                "baseline_timestamp": "2026-10-14",
                "total_count": total_count,
                "generators": discovered
            }, bf, indent=2)
        print("[PASS] Baseline generated successfully.")

    print("\n" + "=" * 70)
    print(f"[PASS] ALL {total_count} GENERATORS VERIFIED INTACT. 0 DELETIONS DETECTED.")
    print("=" * 70)

if __name__ == '__main__':
    audit_generators()
