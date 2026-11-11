#!/usr/bin/env python3
"""Auditor for Central Curriculum Diagram Registry.

Enforces:
1. Valid schema and non-empty metadata for every registered archetype.
2. Verified presence of generator file on disk.
3. Verified presence of renderer component file on disk.
4. Consumption verification: checks that renderer source code (and imported sub-renderers) references all required_fields.
5. Evidence grounding: checks that all evidence documents exist in curriculum_docs_auto/.
6. Enforces zero phantom test IDs and valid need tier definitions.

Exit code 0 on pass, exit code 1 on failure.
"""

import json
import os
import re
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
REGISTRY_PATH = os.path.join(PROJECT_ROOT, "curriculum_diagram_registry.json")


def get_full_renderer_source(rend_path):
    """Reads renderer source and resolves local imported component sources."""
    sources = []
    if not os.path.exists(rend_path):
        return ""
    
    with open(rend_path, mode="r", encoding="utf-8") as rf:
        primary_source = rf.read()
    sources.append(primary_source)

    # Look for local imports e.g. import Foo from './Foo' or import { bar } from './diagram_bank'
    import_matches = re.findall(r"import\s+(?:\{[^}]+\}|\w+)\s+from\s+['\"](\.[^'\"]+)['\"]", primary_source)
    rend_dir = os.path.dirname(rend_path)

    for rel_path in import_matches:
        for ext in ["", ".jsx", ".js", ".tsx", ".ts", "/index.js", "/index.jsx"]:
            cand = os.path.normpath(os.path.join(rend_dir, rel_path + ext))
            if os.path.exists(cand) and not os.path.isdir(cand):
                try:
                    with open(cand, mode="r", encoding="utf-8") as sub_f:
                        sub_content = sub_f.read()
                        sources.append(sub_content)
                        # Check one level deeper for re-exports in index files
                        sub_matches = re.findall(r"import\s+(?:\{[^}]+\}|\w+)\s+from\s+['\"](\.[^'\"]+)['\"]", sub_content)
                        sub_dir = os.path.dirname(cand)
                        for sub_rel in sub_matches:
                            for sub_ext in ["", ".jsx", ".js", ".tsx", ".ts"]:
                                deep_cand = os.path.normpath(os.path.join(sub_dir, sub_rel + sub_ext))
                                if os.path.exists(deep_cand) and not os.path.isdir(deep_cand):
                                    with open(deep_cand, mode="r", encoding="utf-8") as deep_f:
                                        sources.append(deep_f.read())
                                    break
                except Exception:
                    pass
                break

    return "\n".join(sources)


def audit_registry():
    print("\n======================================================================")
    print("   CURRICULUM DIAGRAM REGISTRY AUDITOR (PHASE 3 ENFORCEMENT)          ")
    print("======================================================================\n")

    if not os.path.exists(REGISTRY_PATH):
        print(f"[FAIL] Registry file missing: {REGISTRY_PATH}")
        sys.exit(1)

    try:
        with open(REGISTRY_PATH, mode="r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[FAIL] Invalid JSON in registry: {e}")
        sys.exit(1)

    archetypes = data.get("archetypes", [])
    print(f"[*] Auditing {len(archetypes)} registered diagram archetype(s)...")

    violations = []

    for arch in archetypes:
        arch_id = arch.get("id")
        name = arch.get("name", arch_id)
        print(f"\n--- Archetype: {arch_id} ({name}) ---")

        # Required schema keys
        required_keys = [
            "id", "name", "subject", "grade", "term", "topic",
            "source", "spec_key", "renderer", "renderer_path",
            "generator_file", "required_fields", "evidence",
            "need_tier", "test_id", "status"
        ]
        for k in required_keys:
            if k not in arch or arch[k] is None or arch[k] == "":
                violations.append(f"[{arch_id}] Missing or empty required attribute '{k}'")

        source = arch.get("source")
        if source not in ("generated", "banked"):
            violations.append(f"[{arch_id}] Invalid source '{source}' (must be 'generated' or 'banked')")

        need_tier = arch.get("need_tier")
        if need_tier not in ("Essential", "Supporting"):
            violations.append(f"[{arch_id}] Invalid need_tier '{need_tier}'")

        # Generator existence
        gen_path = os.path.join(PROJECT_ROOT, arch.get("generator_file", ""))
        if not os.path.exists(gen_path):
            violations.append(f"[{arch_id}] Generator file does not exist: {gen_path}")
        else:
            print(f"  [OK] Generator file verified: {arch.get('generator_file')}")

        # Renderer existence & field consumption
        rend_path = os.path.join(PROJECT_ROOT, arch.get("renderer_path", ""))
        if not os.path.exists(rend_path):
            violations.append(f"[{arch_id}] Renderer file does not exist: {rend_path}")
        else:
            print(f"  [OK] Renderer component verified: {arch.get('renderer_path')}")
            rend_full_source = get_full_renderer_source(rend_path)
            for req_field in arch.get("required_fields", []):
                base_field = req_field.split("[")[0].split(".")[0]
                if base_field not in rend_full_source:
                    violations.append(f"[{arch_id}] Field '{req_field}' is listed as required but not referenced in renderer '{rend_path}' or its imported sub-renderers")
                else:
                    print(f"    [+] Consumes required field: '{req_field}'")

        # Evidence existence
        for ev in arch.get("evidence", []):
            ev_clean = ev.split("#")[0]
            ev_path = os.path.join(PROJECT_ROOT, ev_clean)
            if not os.path.exists(ev_path):
                violations.append(f"[{arch_id}] Evidence source document does not exist: {ev_path}")
            else:
                print(f"  [OK] Evidence grounded in curriculum: {ev_clean}")

        # Test ID presence in renderer
        test_id = arch.get("test_id")
        if rend_path and os.path.exists(rend_path):
            rend_full_source = get_full_renderer_source(rend_path)
            if test_id not in rend_full_source:
                violations.append(f"[{arch_id}] Declared test_id '{test_id}' not found in renderer JSX '{rend_path}'")
            else:
                print(f"  [OK] Test selector grounded in live JSX: data-testid=\"{test_id}\"")

    # Audit Visual Aids
    visual_aids = data.get("visual_aids", [])
    print(f"\n[*] Auditing {len(visual_aids)} registered exploratory visual aid(s)...")
    for aid in visual_aids:
        aid_id = aid.get("id")
        name = aid.get("name", aid_id)
        print(f"\n--- Visual Aid: {aid_id} ({name}) ---")

        req_aid_keys = ["id", "name", "component_path", "test_id", "category", "curriculum_reach", "status"]
        for k in req_aid_keys:
            if not aid.get(k):
                violations.append(f"[{aid_id}] Missing or empty visual aid attribute '{k}'")

        comp_path = os.path.join(PROJECT_ROOT, aid.get("component_path", ""))
        if not os.path.exists(comp_path):
            violations.append(f"[{aid_id}] Visual aid component missing on disk: {comp_path}")
        else:
            print(f"  [OK] Component exists: {aid.get('component_path')}")
            with open(comp_path, mode="r", encoding="utf-8") as cf:
                comp_source = cf.read()
            test_id = aid.get("test_id")
            if test_id not in comp_source:
                violations.append(f"[{aid_id}] test_id '{test_id}' not found in component JSX '{comp_path}'")
            else:
                print(f"  [OK] Test selector grounded in live JSX: data-testid=\"{test_id}\"")

    print("\n----------------------------------------------------------------------")
    print("AUDIT SUMMARY")
    print("----------------------------------------------------------------------")
    print(f"Total Archetypes Audited: {len(archetypes)}")
    print(f"Total Visual Aids Audited: {len(visual_aids)}")
    print(f"Total Contract Violations: {len(violations)}")

    if violations:
        print("\n[FAIL] CONTRACT VIOLATIONS DETECTED:")
        for v in violations:
            print(f"  [X] {v}")
        print("\nFix all violations before proceeding.")
        sys.exit(1)

    print("\n[PASS] DIAGRAM REGISTRY AUDIT PASSED: 100% Contract Compliance Verified.\n")
    sys.exit(0)


if __name__ == "__main__":
    audit_registry()
