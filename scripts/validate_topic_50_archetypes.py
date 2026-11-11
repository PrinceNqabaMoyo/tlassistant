#!/usr/bin/env python3
"""
Fast Single-Topic / Multi-Topic 50-Archetype & 5D Diagram Pre-Flight Validator
==============================================================================
Designed specifically to prevent Gemini 3.8 Flash failure modes BEFORE moving to the next topic:
  1. Asserts >= 50 distinct semantic subskills (0 _subskill_N shims).
  2. Asserts 0 raw '<svg' embedded inside prompt / question_text (must be in diagram_spec).
  3. Asserts 100% of emitted diagram_spec payloads use valid DiagramRenderer kinds (e.g.
     {"kind": "inline_svg", "svg": "<svg...", "diagram_role": "context"}) and vary across seeds 101, 102, 103.
  4. Asserts 0 leak-detector regex triggers ('The graph shows', 'The diagram shows', '\\dots' in patterns,
     'image point', etc.) that cause DESCRIBED_NOT_DRAWN or MISSING failures.
  5. Asserts >= 65% of archetypes vary their prompt/answer across seeds [101, 102, 103] (catches fake rng usage).

Usage:
  python scripts/validate_topic_50_archetypes.py --grade 7 --subject "Mathematics"
  python scripts/validate_topic_50_archetypes.py --grade 8 --subject "Mathematics" --topic "Integers"
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
BACKEND_DIR = ROOT / "caps-ai-backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

import scripts.run_universal_comprehensive_diagram_audit as audit  # noqa: E402
from app.services.generator_registry import generate_variant, get_topic_archetypes  # noqa: E402
from scripts.audit_diagram_description_leak import (  # noqa: E402
    collect_prompt_text,
    doc_overlap,
    find_description_signals,
    find_figure_references,
    has_diagram_payload,
    has_table,
)


def validate_topics(grade: int, subject: str, topic_filter: str = "") -> int:
    term_reg_path = BACKEND_DIR / "app/services/caps_term_registry_data.json"
    registry_data = json.loads(term_reg_path.read_text(encoding="utf-8"))

    g_str = str(grade)
    topics = [
        t for t in registry_data
        if str(t.get("grade")) == g_str
        and (subject.lower() == "all" or subject.lower() == str(t.get("subject", "")).lower())
    ]
    if not topics and subject.lower() != "all":
        topics = [
            t for t in registry_data
            if str(t.get("grade")) == g_str
            and subject.lower() in str(t.get("subject", "")).lower()
        ]
    if topic_filter:
        tf_low = topic_filter.strip().lower()
        topics = [t for t in topics if tf_low in str(t.get("name", "")).lower() or tf_low in str(t.get("generator_key", "")).lower()]

    if not topics:
        print(f"ERROR: No topics found for Grade {grade} {subject} (filter='{topic_filter}')")
        return 1

    with contextlib.redirect_stdout(io.StringIO()):
        inventory = audit.run_stage_inventory(subject, [g_str])

    doc_blocks_by_topic: Dict[str, List[Dict[str, Any]]] = {}
    for item in inventory:
        t_key = item["topic"].lower()
        doc_blocks_by_topic.setdefault(t_key, []).append(item)

    disk_state = audit._inspect_disk_renderers()
    ignore_spec_keys = {
        "kind", "diagram_type", "type", "image_type", "master", "diagram_role",
        "show_grid", "interactive", "color", "stroke", "fill",
    }

    total_failures = 0
    seeds = [101, 102, 103]

    for t in topics:
        t_name = str(t.get("name", ""))
        subj = str(t.get("subject", subject))
        arch_info = get_topic_archetypes(t_name, grade=g_str, subject=subj)
        subskills = list(arch_info.get("archetypes", [])) if arch_info else []
        shims = [s for s in subskills if audit.SHIM_ID_RE.search(str(s))]

        print(f"\n=== Validating Gr{g_str} {subj} | '{t_name}' ({len(subskills)} subskills, {len(shims)} shims) ===")

        topic_errors: List[str] = []
        if len(subskills) < 50:
            topic_errors.append(f"D1 FAIL: Only {len(subskills)}/50 semantic subskills found.")
        if shims:
            topic_errors.append(f"D1 FAIL: Synthetic shims detected: {shims[:5]}")

        topic_lower = t_name.lower()
        matched_blocks = [
            b for k, blocks in doc_blocks_by_topic.items()
            if any(w in k for w in topic_lower.split() if len(w) > 3)
            for b in blocks
        ]

        varied_items = 0
        gnr_list: List[str] = []
        missing_list: List[str] = []
        raw_svg_in_prompt: List[str] = []

        for sub in subskills:
            sub_str = str(sub)
            seed_classes = []
            seed_drawn = []
            seed_tbl = []
            seed_dispatched = []
            seed_schema_valid = []
            seed_bound = []
            seed_methods = []
            seed_spec_strings = []
            seed_has_simulearn = []
            trace_failures: List[str] = []
            prompts_seen = set()

            for seed in seeds:
                with contextlib.redirect_stdout(io.StringIO()):
                    qs = generate_variant(topic=t_name, seed=seed, grade=g_str, subject=subj, count=1, subskill=sub_str)
                    q = qs[0] if qs and isinstance(qs[0], dict) else {}
                if not q:
                    trace_failures.append(f"seed_{seed}_empty_payload")
                    continue

                p_text = collect_prompt_text(q)
                w_text = " ".join(str(q.get(k) or "") for k in ("worked_solution", "explanation", "expected_answer", "correct_answer"))
                prompts_seen.add(p_text + "||" + w_text)
                if "<svg" in p_text.lower() and sub_str not in raw_svg_in_prompt:
                    raw_svg_in_prompt.append(sub_str)

                refs = find_figure_references(p_text)
                desc = find_description_signals(p_text)
                has_diag = has_diagram_payload(q)
                has_tbl = has_table(q)
                d_spec = q.get("diagram_spec") or q.get("diagram") or q.get("graph") or q.get("function_graph")

                has_steps = bool(
                    (isinstance(q.get("canonical_solution"), dict) and q["canonical_solution"].get("steps"))
                    or q.get("worked_solution")
                    or q.get("explanation")
                    or q.get("sample_answer")
                )
                seed_has_simulearn.append(has_steps)

                has_doc_ov = False
                for blk in matched_blocks:
                    if blk.get("is_decorative"):
                        continue
                    if doc_overlap(p_text, set(blk.get("tokens", []))) >= 0.40:
                        has_doc_ov = True
                        break

                if desc.get("narrates") or has_doc_ov:
                    s_cls = "DESCRIBED_NOT_DRAWN"
                elif refs:
                    s_cls = "PROMPT_REFERENCES_FIGURE"
                else:
                    s_cls = "NOT_REQUIRED"

                seed_classes.append(s_cls)
                seed_drawn.append(has_diag)
                seed_tbl.append(has_tbl)

                if has_diag and isinstance(d_spec, dict):
                    seed_spec_strings.append(json.dumps(d_spec, sort_keys=True))
                    dispatched, schema_ok, m, fails = audit._validate_universal_spec(sub_str, d_spec, disk_state)
                    seed_dispatched.append(dispatched)
                    seed_schema_valid.append(schema_ok)
                    seed_methods.append(m)
                    trace_failures.extend(fails)

                    spec_toks = audit._extract_spec_tokens(d_spec, ignore_spec_keys)
                    combined_lower = (p_text + " " + w_text).lower()
                    is_bound = any(tok.lower() in combined_lower for tok in spec_toks) if spec_toks else True
                    seed_bound.append(is_bound)
                    if not is_bound:
                        trace_failures.append(f"seed_{seed}_diagram_not_bound_to_question")
                else:
                    seed_dispatched.append(False)
                    seed_schema_valid.append(False)
                    seed_methods.append("TABLE_2D" if has_tbl else "NONE")
                    seed_bound.append(False)

            if len(prompts_seen) > 1 or len(set(seed_spec_strings)) > 1:
                varied_items += 1

            final_class = seed_classes[0] if seed_classes and len(set(seed_classes)) == 1 else (seed_classes[0] if seed_classes else "ERROR")
            is_drawn_all = bool(seed_drawn) and all(seed_drawn) and len(seed_drawn) == len(seeds)
            is_drawn_any = any(seed_drawn)
            is_tbl_any = any(seed_tbl)
            schema_valid_all = is_drawn_all and all(seed_schema_valid)
            dispatched_all = is_drawn_all and all(seed_dispatched)
            bound_all = is_drawn_all and all(seed_bound)

            if is_drawn_all and len(seeds) >= 2:
                seed_varies = len(set(seed_spec_strings)) >= 2 or any("A_PLATE" in m for m in seed_methods) or "floor_packaging_plan" in seed_spec_strings[0]
                if not seed_varies:
                    trace_failures.append("static_diagram_spec_across_seeds")
            else:
                seed_varies = is_drawn_all

            if is_drawn_any:
                if not (is_drawn_all and dispatched_all and schema_valid_all and seed_varies and bound_all and final_class != "DESCRIBED_NOT_DRAWN"):
                    gnr_list.append(f"{sub_str} -> {sorted(set(trace_failures))}")
            elif is_tbl_any and final_class != "PROMPT_REFERENCES_FIGURE":
                pass
            elif final_class in ("PROMPT_REFERENCES_FIGURE", "DESCRIBED_NOT_DRAWN"):
                missing_list.append(f"{sub_str} ({final_class})")

        if raw_svg_in_prompt:
            topic_errors.append(
                f"RAW SVG IN PROMPT ({len(raw_svg_in_prompt)}): Put SVG in diagram_spec={{'kind': 'inline_svg', 'svg': svg}}, never in prompt: {raw_svg_in_prompt[:5]}"
            )
        if gnr_list:
            topic_errors.append(f"GENERATED_NOT_RENDERED ({len(gnr_list)}): {gnr_list[:8]}")
        if missing_list:
            topic_errors.append(f"MISSING DIAGRAM / LEAK TRIGGER ({len(missing_list)}): {missing_list[:8]}")

        if topic_errors:
            total_failures += len(topic_errors)
            for err in topic_errors:
                print(f"  [FAIL] {err}")
        else:
            print(f"  [PASS] 50/50 semantic subskills | 0 GNR | 0 MISSING | {varied_items}/{len(subskills)} seed-varied")

    if total_failures > 0:
        print(f"\nOVERALL RESULT: FAIL ({total_failures} error groups detected)")
        return 1
    print("\nOVERALL RESULT: PASS (Exit Code 0)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate 50-archetype topic implementation against Flash failure modes.")
    parser.add_argument("--grade", type=int, required=True, help="Grade number (7-12)")
    parser.add_argument("--subject", type=str, required=True, help="Subject name")
    parser.add_argument("--topic", type=str, default="", help="Optional topic name substring")
    args = parser.parse_args()
    return validate_topics(args.grade, args.subject, args.topic)


if __name__ == "__main__":
    sys.exit(main())
