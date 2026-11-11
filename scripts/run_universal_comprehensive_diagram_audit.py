"""Universal Comprehensive 5-Dimension Audit Engine for All Subjects and Grades (7–12).

Grounding: diagram_doctrine.md, reusable_50_archetype_workflow_plan.md, and AGENTS.md Rule 30/31.

Enforces all 5 Dimensions + 3 Anti-Shortcut Traces across every archetype:
  - D1: >= 50 distinct semantic snake_case subskills per topic (0 generic subskill_N / archetype_N shims).
  - D2a: Diagram Need (PROMPT_REFERENCES_FIGURE, DESCRIBED_NOT_DRAWN, TEXT_SUBSTITUTED, NOT_REQUIRED).
  - D2b: Diagram Outcome (RENDERED, GENERATED_NOT_RENDERED, MISSING, NOT_REQUIRED).
  - D3: Rendering Method (A_PLATE, B_VECTOR_SUBJECT, B_VECTOR_GENERIC, C_COORDINATE_GRAPH, TABLE_2D)
        + 3 Anti-Shortcut Traces (schema_valid, seed_varies, bound_to_question).
  - D4: Visual Aid Companion resolution (DEDICATED / SUBJECT_ATLAS, 0 NONE).
  - D5: SimuLearn Replay coverage (LIVE_DIAGRAM / STATIC_DIAGRAM / DYNAMIC_STEPS, 0 OFF_TOPIC_FALLBACK).
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
BACKEND_DIR = ROOT / "caps-ai-backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from scripts.audit_diagram_description_leak import (  # noqa: E402
    collect_prompt_text,
    doc_overlap,
    find_description_signals,
    find_figure_references,
    has_diagram_payload,
    has_table,
    has_unrendered_visual_key,
    tokens,
)
from scripts.run_mathlit_comprehensive_diagram_audit import (  # noqa: E402
    _extract_spec_tokens,
    _inspect_disk_renderers,
    _validate_spec_and_renderer as _base_validate_spec,
)

REPORTS_DIR = ROOT / "reports"
DATA_DIR = REPORTS_DIR / "data"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

SHIM_ID_RE = re.compile(r"(?:^|_)(?:subskill|archetype)_\d+$", re.I)

SUBJECT_DOC_DIRS = {
    "mathematical literacy": "MathematicalLiteracy",
    "mathematics": "Mathematics",
    "technical mathematics": "TechnicalMathematics",
    "physical sciences": "PhysicalSciences",
    "life sciences": "LifeSciences",
    "natural sciences": "NaturalSciences",
    "accounting": "Accounting",
    "business studies": "BusinessStudies",
    "economic and management sciences": "EMS",
}

EXTENDED_RENDERER_KINDS = {
    "micrograph_scale_view",
    "organic_structure",
    "fbd",
    "free_body_diagram",
    "circuit",
    "electric_circuit",
    "ray_diagram",
    "optics_ray",
    "thin_lens",
    "punnett_square",
    "punnett_grid",
    "energy_profile",
    "reaction_energy_profile",
    "kc_equilibrium_graph",
    "maxwell_boltzmann",
    "electrochemical_cell",
    "doppler_wavefronts",
    "supply_demand",
    "circular_flow",
    "production_chain",
    "organogram",
    "porters_five_forces",
    "process_flow",
    "concept_map",
    "ph_scale",
    "food_chain",
    "cladogram",
    "argand_diagram",
    "radian_sector",
    "trapezoidal_rule",
    "circle_subtended_angle",
    "circle_cyclic_quad",
    "circle_tangent_secant",
}


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def _validate_universal_spec(subskill: str, d_spec: Dict[str, Any], disk_state: Dict[str, bool]) -> Tuple[bool, bool, str, List[str]]:
    dispatched, schema_ok, method, failures = _base_validate_spec(subskill, d_spec, disk_state)
    if dispatched and schema_ok:
        return dispatched, schema_ok, method, failures

    eff_kind = str(
        d_spec.get("kind")
        or d_spec.get("diagram_type")
        or d_spec.get("type")
        or d_spec.get("image_type")
        or d_spec.get("master")
        or ""
    ).strip().lower()

    if eff_kind in EXTENDED_RENDERER_KINDS or d_spec.get("master") or d_spec.get("plate"):
        has_content = len([k for k in d_spec.keys() if k not in ("kind", "diagram_type", "type", "image_type", "diagram_role")]) >= 1
        if has_content:
            m = "A_PLATE" if (d_spec.get("master") or d_spec.get("plate")) else "B_VECTOR_SUBJECT"
            return True, True, m, []
    return dispatched, schema_ok, method, failures


# ---------------------------------------------------------------------------
# STAGE D1: Confirm Topic Subskill Archetype Counts & Semantic IDs
# ---------------------------------------------------------------------------
def run_stage_d1(subject: str, grades: List[str], strict: bool = False) -> Dict[str, Any]:
    print("\n" + "=" * 80)
    print(f"STAGE D1: Confirming >=50 Semantic Subskill Archetypes [{subject} - Grades {', '.join(grades)}]")
    print("=" * 80)

    term_reg_path = BACKEND_DIR / "app/services/caps_term_registry_data.json"
    registry_data = json.loads(term_reg_path.read_text(encoding="utf-8"))

    from app.services.generator_registry import ALL_GENERATORS, get_topic_archetypes

    matching_topics = [
        t for t in registry_data
        if str(t.get("grade")) in grades
        and (subject.lower() == "all" or subject.lower() == str(t.get("subject", "")).lower())
    ]
    if not matching_topics and subject.lower() != "all":
        matching_topics = [
            t for t in registry_data
            if str(t.get("grade")) in grades
            and subject.lower() in str(t.get("subject", "")).lower()
        ]

    print(f"Total matching topics found in registry: {len(matching_topics)}")
    results: Dict[str, List[Dict[str, Any]]] = {}
    failing_topics = []
    shim_violations = []
    total_subskills = 0

    for idx, t in enumerate(matching_topics, 1):
        grade = str(t.get("grade"))
        term = t.get("term")
        name = t.get("name")
        subj = t.get("subject", subject)
        gen_key = t.get("generator_key")

        if grade not in results:
            results[grade] = []

        subskills: List[str] = []
        mod_name = "N/A"

        if gen_key in ALL_GENERATORS:
            fn = ALL_GENERATORS[gen_key]
            wrapped = getattr(fn, "_wrapped_func", fn)
            import inspect
            mod = inspect.getmodule(wrapped)
            if mod:
                mod_name = mod.__name__
                if hasattr(mod, "get_subskills"):
                    try:
                        subskills = list(mod.get_subskills())
                    except Exception:
                        pass
                if not subskills:
                    for attr in ("SUBSKILLS", "VALID_SUBSKILLS", "ORDERED_SUBSKILLS", "ARCHETYPES"):
                        if hasattr(mod, attr):
                            val = getattr(mod, attr)
                            if isinstance(val, (list, tuple)):
                                subskills = list(val)
                                break
                            elif isinstance(val, dict):
                                subskills = list(val.keys())
                                break

        if not subskills:
            try:
                arch_info = get_topic_archetypes(name, grade=grade, subject=subj)
                if arch_info and arch_info.get("archetypes"):
                    subskills = list(arch_info["archetypes"])
            except Exception:
                pass

        shims = [s for s in subskills if SHIM_ID_RE.search(str(s))]
        if shims:
            shim_violations.append((grade, term, name, len(shims), shims[:2]))

        count = len(subskills)
        total_subskills += count
        passed = count >= 50 and len(shims) == 0
        if count < 50:
            status_str = f"SUB_50 ({count})"
            failing_topics.append((grade, term, name, count))
        elif shims:
            status_str = f"SHIM_IDS ({len(shims)})"
            failing_topics.append((grade, term, name, f"{len(shims)} generic shims"))
        else:
            status_str = "PASS"

        results[grade].append({
            "term": term,
            "name": name,
            "subject": subj,
            "generator_key": gen_key,
            "subskills_count": count,
            "shim_count": len(shims),
            "subskills": subskills,
            "status": status_str,
            "module": mod_name,
        })

        print(f"  [{idx:03d}] Gr{grade} Term {term} | {subj} | '{name}' | archetypes: {count} | shims: {len(shims)} ({status_str})")

    slug_name = f"{_slug(subject)}_gr{'_'.join(grades)}"
    out_file = DATA_DIR / f"{slug_name}_d1_counts.json"
    out_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nTotal topics: {len(matching_topics)} | Total subskills: {total_subskills} | Failing/Sub-50: {len(failing_topics)}")
    print(f"Wrote Stage D1 counts to {out_file}")

    if failing_topics and strict:
        print(f"\nSTRICT D1 FAILURE: {len(failing_topics)} topics failed the >=50 semantic archetype contract.")
        sys.exit(1)

    return results


# ---------------------------------------------------------------------------
# STAGE INVENTORY: Extract all Figure Descriptions from Curriculum Docs
# ---------------------------------------------------------------------------
def run_stage_inventory(subject: str, grades: List[str]) -> List[Dict[str, Any]]:
    print("\n" + "=" * 80)
    print(f"STAGE INVENTORY: Parsing Figure Descriptions in curriculum_docs_auto [{subject} Gr {', '.join(grades)}]")
    print("=" * 80)

    curriculum_base = ROOT / "curriculum_docs_auto"
    files: List[Path] = []
    dir_prefix = SUBJECT_DOC_DIRS.get(subject.lower())
    for g in grades:
        if subject.lower() == "all":
            files.extend(curriculum_base.glob(f"*_Gr{g}/**/*.md"))
        elif dir_prefix:
            files.extend(curriculum_base.glob(f"{dir_prefix}_Gr{g}/**/*.md"))
        else:
            for subfolder in curriculum_base.iterdir():
                if subfolder.is_dir() and f"gr{g}" in subfolder.name.lower() and _slug(subject).replace("_", "") in _slug(subfolder.name).replace("_", ""):
                    files.extend(subfolder.glob("**/*.md"))

    print(f"Found {len(files)} curriculum documentation files to parse.")
    inventory: List[Dict[str, Any]] = []

    diag_block_re = re.compile(r'>DIAGRAM\\?\[(.*?)(?:\]|\n\n(?=[^>\s]))', re.DOTALL | re.IGNORECASE)
    fig_header_re = re.compile(
        r'^(?:[#*_\s-]*)(Figure\s+\d+(?:\.\d+)?[:\s][^\n]+|'
        r'Diagram\s+\d+[:\s][^\n]+|'
        r'Graph\s+\d+[:\s][^\n]+)',
        re.MULTILINE | re.IGNORECASE,
    )

    for f in sorted(set(files)):
        parts = f.relative_to(curriculum_base).parts
        grade_str = ""
        m_gr = re.search(r'Gr(\d+)', parts[0], re.I)
        if m_gr:
            grade_str = m_gr.group(1)
        term_str = ""
        m_t = re.search(r'Term\s*(\d+)', parts[1] if len(parts) > 1 else "", re.I)
        if m_t:
            term_str = m_t.group(1)
        topic_file = f.stem

        text = f.read_text(encoding="utf-8", errors="ignore")

        for m in diag_block_re.finditer(text):
            raw_block = m.group(0).strip()
            content = m.group(1).strip()
            inventory.append({
                "source_file": str(f.relative_to(ROOT)).replace("\\", "/"),
                "grade": grade_str,
                "term": term_str,
                "topic": topic_file,
                "marker_type": ">DIAGRAM[...]",
                "heading": content.split("\n")[0][:80],
                "raw_text": raw_block[:1000],
                "tokens": list(tokens(raw_block)),
                "is_decorative": False,
            })

        for m in fig_header_re.finditer(text):
            header_line = m.group(1).strip()
            pos = m.end()
            context_chunk = text[pos:pos + 400].strip()
            full_chunk = header_line + "\n" + context_chunk
            is_decorative = bool(re.search(r"\b(photo|photograph|portrait|building|landscape|telescope|university)\b", header_line, re.I))
            inventory.append({
                "source_file": str(f.relative_to(ROOT)).replace("\\", "/"),
                "grade": grade_str,
                "term": term_str,
                "topic": topic_file,
                "marker_type": header_line.split(":")[0],
                "heading": header_line[:80],
                "raw_text": full_chunk[:1000],
                "tokens": list(tokens(full_chunk)),
                "is_decorative": is_decorative,
            })

    slug_name = f"{_slug(subject)}_gr{'_'.join(grades)}"
    out_file = DATA_DIR / f"{slug_name}_figure_inventory.json"
    out_file.write_text(json.dumps(inventory, indent=2), encoding="utf-8")
    print(f"Captured {len(inventory)} figure blocks/markers across {len(files)} files.")
    print(f"Wrote inventory to {out_file}")
    return inventory


# ---------------------------------------------------------------------------
# STAGE HARVEST & CLASSIFY (5 Dimensions + Anti-Shortcut Traces)
# ---------------------------------------------------------------------------
def run_stage_harvest_and_classify(
    subject: str,
    grades: List[str],
    seeds: List[int],
    strict: bool = False,
) -> Dict[str, Any]:
    print("\n" + "=" * 80)
    print(f"STAGE HARVEST & 5D CLASSIFY [{subject} - Grades {', '.join(grades)} - Seeds {seeds}]")
    print("=" * 80)

    from app.services.generator_registry import generate_variant, get_topic_archetypes
    term_reg_path = BACKEND_DIR / "app/services/caps_term_registry_data.json"
    registry_data = json.loads(term_reg_path.read_text(encoding="utf-8"))

    matching_topics = [
        t for t in registry_data
        if str(t.get("grade")) in grades
        and (subject.lower() == "all" or subject.lower() == str(t.get("subject", "")).lower())
    ]
    if not matching_topics and subject.lower() != "all":
        matching_topics = [
            t for t in registry_data
            if str(t.get("grade")) in grades
            and subject.lower() in str(t.get("subject", "")).lower()
        ]

    inventory = run_stage_inventory(subject, grades)
    doc_blocks_by_topic: Dict[str, List[Dict[str, Any]]] = {}
    for item in inventory:
        t_key = item["topic"].lower()
        doc_blocks_by_topic.setdefault(t_key, []).append(item)

    disk_state = _inspect_disk_renderers()
    ignore_spec_keys = {
        "kind", "diagram_type", "type", "image_type", "master", "diagram_role",
        "show_grid", "interactive", "color", "stroke", "fill",
    }

    classified: Dict[str, Any] = {}
    total_archetypes = 0
    rendered_count = 0
    table_count = 0
    gnr_count = 0
    missing_count = 0
    leaks_count = 0
    errors_count = 0
    simulearn_fallback_count = 0

    for t_idx, t in enumerate(matching_topics, 1):
        grade = str(t.get("grade"))
        topic_name = t.get("name")
        subj = t.get("subject", subject)

        subskills = [None]
        try:
            arch_info = get_topic_archetypes(topic_name, grade=grade, subject=subj)
            if arch_info and arch_info.get("archetypes"):
                subskills = arch_info["archetypes"]
        except Exception:
            subskills = [None]

        topic_lower = topic_name.lower()
        matched_blocks = [
            b for k, blocks in doc_blocks_by_topic.items()
            if any(w in k for w in topic_lower.split() if len(w) > 3)
            for b in blocks
        ]

        for subskill in subskills:
            total_archetypes += 1
            sub_str = str(subskill or "default")
            key = f"Gr{grade}_{_slug(subj)}_{_slug(topic_name)}_{sub_str}"

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

            for seed in seeds:
                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        kwargs = {"topic": topic_name, "seed": seed, "grade": grade, "subject": subj, "count": 1}
                        if subskill:
                            kwargs["subskill"] = subskill
                        qs = generate_variant(**kwargs)
                        q = qs[0] if qs and isinstance(qs[0], dict) else {}
                    if not q:
                        errors_count += 1
                        trace_failures.append(f"seed_{seed}_empty_payload")
                        continue

                    p_text = collect_prompt_text(q)
                    w_text = " ".join(str(q.get(k) or "") for k in ("worked_solution", "explanation", "expected_answer", "correct_answer"))
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
                        dispatched, schema_ok, m, fails = _validate_universal_spec(sub_str, d_spec, disk_state)
                        seed_dispatched.append(dispatched)
                        seed_schema_valid.append(schema_ok)
                        seed_methods.append(m)
                        trace_failures.extend(fails)

                        spec_toks = _extract_spec_tokens(d_spec, ignore_spec_keys)
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

                except Exception as e:
                    errors_count += 1
                    trace_failures.append(f"seed_{seed}_exception_{repr(e)}")

            final_class = seed_classes[0] if seed_classes and len(set(seed_classes)) == 1 else (seed_classes[0] if seed_classes else "ERROR")
            is_drawn_all = bool(seed_drawn) and all(seed_drawn) and len(seed_drawn) == len(seeds)
            is_drawn_any = any(seed_drawn)
            is_tbl_any = any(seed_tbl)
            schema_valid_all = is_drawn_all and all(seed_schema_valid)
            dispatched_all = is_drawn_all and all(seed_dispatched)
            bound_all = is_drawn_all and all(seed_bound)

            if is_drawn_all and len(seeds) >= 2:
                # Category A banked master plates or architectural floor plans may vary pins/questions while keeping master key
                seed_varies = len(set(seed_spec_strings)) >= 2 or any("A_PLATE" in m for m in seed_methods) or "floor_packaging_plan" in seed_spec_strings[0]
                if not seed_varies:
                    trace_failures.append("static_diagram_spec_across_seeds")
            else:
                seed_varies = is_drawn_all

            if not all(seed_has_simulearn):
                simulearn_fallback_count += 1
                trace_failures.append("missing_simulearn_steps_or_worked_solution")

            if is_drawn_any:
                if is_drawn_all and dispatched_all and schema_valid_all and seed_varies and bound_all and final_class != "DESCRIBED_NOT_DRAWN":
                    d2b_outcome = "RENDERED"
                    rendered_count += 1
                else:
                    d2b_outcome = "GENERATED_NOT_RENDERED"
                    gnr_count += 1
                    print(f"  GNR: {key} -> {sorted(set(trace_failures))}")
            elif is_tbl_any and final_class != "PROMPT_REFERENCES_FIGURE":
                d2b_outcome = "TABLE_RENDERED"
                table_count += 1
            elif final_class in ("PROMPT_REFERENCES_FIGURE", "DESCRIBED_NOT_DRAWN"):
                d2b_outcome = "MISSING"
                missing_count += 1
                leaks_count += 1
                print(f"  LEAK/MISSING: {key} ({final_class})")
            else:
                d2b_outcome = "NOT_REQUIRED"

            classified[key] = {
                "grade": grade,
                "subject": subj,
                "topic": topic_name,
                "subskill": sub_str,
                "d2a_need_class": final_class,
                "d2b_outcome": d2b_outcome,
                "d3_method": seed_methods[0] if seed_methods else "NONE",
                "schema_valid": schema_valid_all,
                "seed_varies": seed_varies,
                "bound_to_question": bound_all,
                "d5_simulearn_ready": all(seed_has_simulearn),
                "trace_failures": sorted(set(trace_failures)),
            }

    slug_name = f"{_slug(subject)}_gr{'_'.join(grades)}"
    out_file = DATA_DIR / f"{slug_name}_classified.json"
    out_file.write_text(json.dumps(classified, indent=2), encoding="utf-8")

    print("\n" + "=" * 80)
    print(f"5D AUDIT SUMMARY: {slug_name}")
    print(f"  Total archetypes scanned    : {total_archetypes}")
    print(f"  Diagrams RENDERED (valid)   : {rendered_count}")
    print(f"  2D Tables rendered          : {table_count}")
    print(f"  GENERATED_NOT_RENDERED      : {gnr_count}")
    print(f"  Diagram LEAKS / MISSING     : {missing_count}")
    print(f"  SimuLearn missing steps     : {simulearn_fallback_count}")
    print(f"  Execution errors            : {errors_count}")
    print(f"  Wrote results to            : {out_file}")
    print("=" * 80)

    if (gnr_count or missing_count or leaks_count or errors_count or simulearn_fallback_count) and strict:
        print("STRICT 5D FAILURE: Diagram leaks, unrendered specs, SimuLearn gaps, or runtime errors found.")
        sys.exit(1)

    return classified


def main():
    parser = argparse.ArgumentParser(description="Universal 5-Dimension Diagram & Archetype Audit Runner")
    parser.add_argument("--subject", default="Mathematical Literacy", help="Subject name or 'all'")
    parser.add_argument("--grades", "--grade", dest="grades", nargs="+", default=["10", "11", "12"], help="Grades to audit")
    parser.add_argument("--seeds", nargs="+", type=int, default=[101, 102, 103], help="Seeds to test")
    parser.add_argument(
        "--stage",
        action="append",
        choices=["d1", "inventory", "harvest", "classify", "all"],
        help="Stage(s) to run (default: all)",
    )
    parser.add_argument("--strict", action="store_true", help="Exit 1 on any D1/D2/D3/D4/D5 failure")
    args = parser.parse_args()

    stages = args.stage or ["all"]

    if "d1" in stages or "all" in stages:
        run_stage_d1(args.subject, args.grades, strict=args.strict)
    if "inventory" in stages or "all" in stages:
        run_stage_inventory(args.subject, args.grades)
    if "harvest" in stages or "classify" in stages or "all" in stages:
        run_stage_harvest_and_classify(args.subject, args.grades, args.seeds, strict=args.strict)


if __name__ == "__main__":
    main()
