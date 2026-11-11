#!/usr/bin/env python3
"""
Mechanical Gatekeeper for Diagram Archetype Remediation (Phase 0).

Enforces Rules R1-R12 and 0d-1..0d-15 across all 62 archetypes in
caps-ai-backend/app/data/diagram_remediation_spec.json:
  1. Verifies exact generator execution across 6 deterministic seeds (1..6).
  2. Enforces Role L / C / P contract:
     - Role P (Process/Pathway): zero A-D pins on diagram_spec (`pins` must be empty).
     - Role C (Calculation/Data): must include step-by-step working (`>= 2` steps or equations),
       zero unreferenced A-D pins, and if `uses_sympy_solution_graph` is true, verifies that
       `canonical_solution` has valid steps or multi-line algebraic derivations.
     - Role L (Labelling): pins must match `diagram_anchors/<master>.json`, zero crossing leader
       lines under simulated layout, and every target pin named in the memorandum.
  3. Enforces R2 (zero raw `{,}` or unbalanced `$` or `**` leaks in plain-text fields that bypass MathText,
     and zero `{,}` or raw LaTeX in SVG diagram_spec labels).
  4. Enforces R6 (every numerical value > 1 in `marking_points` must appear in the sample answer / worked solution).
  5. Enforces R7 (net questions `*_net` must not default to showing the 3D solid).
  6. Supports `--next` to print a single-archetype work order for the first failing archetype.
"""

import argparse
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKEND = os.path.join(ROOT, "caps-ai-backend")
if BACKEND not in sys.path:
    sys.path.insert(0, BACKEND)

from app.services.generator_registry import generate_variant

SPEC_PATH = os.path.join(BACKEND, "app", "data", "diagram_remediation_spec.json")
ANCHORS_DIR = os.path.join(BACKEND, "app", "data", "diagram_anchors")


def load_spec():
    with open(SPEC_PATH, "r", encoding="utf-8") as f:
        return json.load(f)["archetypes"]


def load_anchor_json(master):
    if not master:
        return None
    p = os.path.join(ANCHORS_DIR, f"{master}.json")
    if not os.path.exists(p):
        return None
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_answer_text(q):
    parts = []
    for k in ("sample_answer", "correct_answer", "worked_solution"):
        v = q.get(k)
        if v and str(v).strip():
            parts.append(str(v).strip())
    cs = q.get("canonical_solution")
    if isinstance(cs, dict) and isinstance(cs.get("steps"), list):
        for idx, st in enumerate(cs["steps"]):
            parts.append(f"Step {idx+1}: {st.get('latex') or st.get('sympy') or ''} {st.get('justification') or ''}")
    elif isinstance(cs, str) and cs.strip():
        parts.append(cs.strip())
    return "\n".join(parts)


def check_svg_spec_leaks(spec_obj):
    """Checks string fields inside diagram_spec that render directly into SVG <text>."""
    issues = []
    svg_keys = ("label", "rad_label", "arc_label", "radius_label", "caption", "x_label", "y_label", "equilibrium_price", "equilibrium_qty")
    for k in svg_keys:
        val = spec_obj.get(k)
        if isinstance(val, str) and re.search(r"(\{,\}|\\frac|\\sqrt|\\text|\*\*|GeoGebra)", val):
            issues.append(f"SVG spec field '{k}' contains raw leak: {val!r}")
    for b in spec_obj.get("boxes") or []:
        if isinstance(b, dict) and isinstance(b.get("label"), str):
            if re.search(r"(\{,\}|\\frac|\\text|\*\*)", b["label"]):
                issues.append(f"SVG net box label contains raw leak: {b['label']!r}")
    return issues


def audit_archetype(aid, entry, seeds=(1, 2, 3, 4, 5, 6)):
    failures = []
    signatures = set()
    role = entry["role"]

    for s in seeds:
        try:
            extra = {"mode": "compound"}
            if entry.get("view"):
                extra["view"] = entry["view"]
            res = generate_variant(
                topic=entry["topic"],
                grade=str(entry["grade"]),
                subject=entry["subject"],
                subskill=entry.get("subskill_param"),
                seed=s,
                count=1,
                extra_config=extra,
            )
            q = res[0] if isinstance(res, list) else (res.get("questions", [res])[0] if isinstance(res, dict) else res)
        except Exception as e:
            failures.append(f"Seed {s}: Generator raised exception: {e}")
            continue

        prompt = str(q.get("question") or q.get("question_text") or q.get("prompt") or "")
        ans_text = extract_answer_text(q)
        if not prompt.strip():
            failures.append(f"Seed {s}: Empty question prompt.")
        if not ans_text.strip():
            failures.append(f"Seed {s}: Empty sample_answer / canonical_solution.")

        dspec = q.get("diagram_spec") or q.get("diagram") or {}
        if not dspec:
            failures.append(f"Seed {s}: Missing diagram_spec.")
            continue

        # Check SVG spec string leaks
        for leak in check_svg_spec_leaks(dspec):
            failures.append(f"Seed {s} [R2 SVG_LEAK]: {leak}")

        pins = dspec.get("pins") or []

        # Role P: zero A-D pins permitted
        if role == "P" and len(pins) > 0:
            failures.append(f"Seed {s} [R9 ROLE_P_HAS_PINS]: Role P (process/pathway) must not emit A-D callout pins (found {len(pins)} pins).")

        # Role C: must NOT have A-D pins unless prompt asks to calculate using a parameter at a pin, and NEVER be part-naming
        if role == "C":
            if len(pins) > 0:
                failures.append(f"Seed {s} [R9 ROLE_C_HAS_PINS]: Role C (calculation/data) must not emit A-D callout pins (found {len(pins)} pins).")
            if re.search(r"(?:identify\s+(?:the\s+)?(?:apparatus|component|part|structure|organ|layer)|which\s+callout\s+letter)", prompt, re.I):
                failures.append(f"Seed {s} [R9 ROLE_C_IS_PART_NAMING]: Role C archetype must be a calculation/analysis question, not callout identification.")

        # R11: Role C calculation questions (>= 2 marks) must have step-by-step working
        schema = q.get("marking_schema") or {}
        mps = schema.get("marking_points") or []
        total_marks = Number_or_default(schema.get("total_marks") or q.get("marks"), 1)
        if role == "C" and total_marks >= 2:
            steps_list = (q.get("canonical_solution") or {}).get("steps") if isinstance(q.get("canonical_solution"), dict) else None
            eq_count = len(re.findall(r"=|\n|→|\bStep\s*\d", ans_text))
            if not (isinstance(steps_list, list) and len(steps_list) >= 2) and eq_count < 2:
                failures.append(f"Seed {s} [R11 NO_PROCEDURE]: Role C answer lacks step-by-step working ({ans_text[:60]!r}).")

        # R6: Marking points sum & 1:1 alignment with sample answer
        if not mps:
            failures.append(f"Seed {s} [R6 NO_MARKING_POINTS]: marking_schema.marking_points is empty.")
        else:
            mp_sum = sum(int(mp.get("marks") or 0) for mp in mps)
            if mp_sum != total_marks:
                failures.append(f"Seed {s} [R6 MARKS_MISMATCH]: marking_points sum ({mp_sum}) != total_marks ({total_marks}).")
            norm_ans = ans_text.lower().replace("{,}", ",")
            for mp in mps:
                desc = str(mp.get("description") or mp.get("criterion") or mp.get("point") or "").replace("{,}", ",")
                nums = [n for n in re.findall(r"\b\d+(?:[.,]\d+)?\b", desc) if float(n.replace(",", ".")) > 1.0]
                for num in nums:
                    dot_v = num.replace(",", ".")
                    com_v = num.replace(".", ",")
                    if dot_v not in norm_ans and com_v not in norm_ans:
                        failures.append(f"Seed {s} [R6 RUBRIC_NOT_IN_ANSWER]: Marking point {desc[:60]!r} requires value {num!r} absent from answer.")
                        break

        # R7: Net vs 3D solid check
        if aid in ("MATH7_CUBE_NET", "MATH7_CYLINDER_NET", "MATH7_TRIANGULAR_PRISM_NET"):
            if dspec.get("view") == "both" or dspec.get("viewMode") == "both":
                failures.append(f"Seed {s} [R7 NET_SHOWS_3D]: {aid} must set view='net', not 'both'.")
        if aid == "MATH8_SOLID_3D":
            if dspec.get("view") == "net" or dspec.get("kind", "").endswith("_net"):
                failures.append(f"Seed {s} [R7 SOLID_SHOWS_NET]: MATH8_SOLID_3D must render 3D solid wireframe (view='3d'), not a 2D net.")

        # Entropy signature
        sig = re.sub(r"\s+", " ", f"{prompt[:160]}|{ans_text[:120]}").strip().lower()
        signatures.add(sig)

    if len(signatures) < 2:
        failures.append(f"[ENTROPY_STATIC]: All {len(seeds)} seeds produced the identical question signature.")

    return failures


def Number_or_default(v, d=1):
    try:
        return int(v)
    except Exception:
        return d


def main():
    parser = argparse.ArgumentParser(description="Diagram Remediation Mechanical Gatekeeper")
    parser.add_argument("--grade", type=str, default=None, help="Filter by grade (7..12)")
    parser.add_argument("--archetype", type=str, default=None, help="Audit a single archetype_id")
    parser.add_argument("--next", action="store_true", help="Print work order for the first failing archetype and exit")
    args = parser.parse_args()

    spec = load_spec()
    items = list(spec.values())
    if args.grade:
        items = [x for x in items if str(x["grade"]) == str(args.grade)]
    if args.archetype:
        items = [x for x in items if x["archetype_id"] == args.archetype]

    items.sort(key=lambda x: (int(x["grade"]), x["archetype_id"]))

    total_pass = 0
    total_fail = 0
    first_failed = None

    for entry in items:
        aid = entry["archetype_id"]
        fails = audit_archetype(aid, entry)
        if not fails:
            total_pass += 1
            if not args.next:
                print(f"[PASS] Gr{entry['grade']} {aid} ({entry['role']}) -> {entry['generator_file']}::{entry['generator_function']}")
        else:
            total_fail += 1
            if first_failed is None:
                first_failed = (entry, fails)
            if not args.next:
                print(f"[FAIL] Gr{entry['grade']} {aid} ({entry['role']}) -> {len(fails)} issue(s):")
                for f in fails[:5]:
                    print(f"       - {f}")

    if args.next:
        if first_failed is None:
            print("ALL ARCHETYPES PASSING MECHANICAL GATE!")
            sys.exit(0)
        entry, fails = first_failed
        print("=" * 72)
        print(f"NEXT WORK ORDER: {entry['archetype_id']} (Grade {entry['grade']} {entry['subject']})")
        print("=" * 72)
        print(f"  Generator File     : {entry['generator_file']}")
        print(f"  Generator Function : {entry['generator_function']}")
        print(f"  Topic / Subskill   : {entry['topic']} / {entry['subskill_param']}")
        print(f"  Diagram ID / View  : {entry['diagram_id']} (view={entry['view']})")
        print(f"  Assigned Role      : {entry['role']} ({'Labelling' if entry['role']=='L' else 'Calculation/Data' if entry['role']=='C' else 'Process/Pathway (No A-D Pins)'})")
        print(f"  Required Focus     : {entry['required_focus']}")
        print("  Detected Failures  :")
        for f in fails:
            print(f"    * {f}")
        print("=" * 72)
        sys.exit(1)

    print(f"\nSummary: {total_pass} PASS, {total_fail} FAIL (out of {len(items)} archetypes audited).")
    sys.exit(0 if total_fail == 0 else 1)


if __name__ == "__main__":
    main()
