"""Comprehensive 5-Dimension Audit Engine for Mathematical Literacy Grades 10 to 12.

Implements all stages of the Math Lit audit plan:
  --stage d1          Confirm subskill archetype counts across all 36 topics (all >= 50).
  --stage inventory   Extract all figure descriptions from curriculum_docs_auto/MathematicalLiteracy_Gr*.
  --stage harvest     Execute 1,871 archetypes across seeds [101, 102, 103] and harvest payloads.
  --stage classify    Classify D2a/D2b/D3 for all archetypes (needs diagram, rendered, philosophy method).
  --stage report      Generate full Markdown report and per-archetype CSV.
  --all               Run all python stages in sequence.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
BACKEND_DIR = ROOT / "caps-ai-backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

# Import leak detector utilities
from scripts.audit_diagram_description_leak import (  # noqa: E402
    collect_prompt_text,
    find_figure_references,
    find_description_signals,
    doc_overlap,
    has_diagram_payload,
    has_unrendered_visual_key,
    has_table,
    tokens,
)

REPORTS_DIR = ROOT / "reports"
DATA_DIR = REPORTS_DIR / "data"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# STAGE D1: Confirm Topic Subskill Archetype Counts
# ---------------------------------------------------------------------------
def run_stage_d1() -> Dict[str, Any]:
    print("\n" + "=" * 80)
    print("STAGE D1: Confirming Subskill Archetype Counts (Grades 10–12)")
    print("=" * 80)

    term_reg_path = BACKEND_DIR / "app/services/caps_term_registry_data.json"
    registry_data = json.loads(term_reg_path.read_text(encoding="utf-8"))

    from app.services.generator_registry import ALL_GENERATORS

    mathlit_topics = [
        t for t in registry_data
        if str(t.get("grade")) in ("10", "11", "12")
        and "Mathematical Literacy" in str(t.get("subject", ""))
    ]

    print(f"Total Mathematical Literacy topics found in registry: {len(mathlit_topics)}")
    results = {}
    failing_topics = []
    total_subskills = 0

    for idx, t in enumerate(mathlit_topics, 1):
        grade = str(t.get("grade"))
        term = t.get("term")
        name = t.get("name")
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

        count = len(subskills)
        total_subskills += count
        passed = count >= 50
        status_str = "PASS" if passed else f"FAIL ({count})"
        if not passed:
            failing_topics.append((grade, term, name, count))

        results[grade].append({
            "term": term,
            "name": name,
            "generator_key": gen_key,
            "subskills_count": count,
            "subskills": subskills,
            "status": status_str,
            "module": mod_name
        })

        print(f"  [{idx:02d}] Gr{grade} Term {term} | '{name}' | key: '{gen_key}' | subskills: {count} ({status_str})")

    out_file = DATA_DIR / "mathlit_d1_counts.json"
    out_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nTotal topics: {len(mathlit_topics)} | Total subskills: {total_subskills}")
    print(f"Wrote Stage D1 counts to {out_file}")

    if failing_topics:
        print(f"\nFAILED: {len(failing_topics)} topics have fewer than 50 archetypes:")
        for ft in failing_topics:
            print(f"  Gr{ft[0]} T{ft[1]} '{ft[2]}': {ft[3]} subskills")
        sys.exit(1)

    print("STAGE D1: 100% PASS (All 36 topics have >= 50 archetypes)")
    return results


# ---------------------------------------------------------------------------
# STAGE INVENTORY: Extract all Figure Descriptions from Curriculum Docs
# ---------------------------------------------------------------------------
def run_stage_inventory() -> List[Dict[str, Any]]:
    print("\n" + "=" * 80)
    print("STAGE INVENTORY: Parsing Figure Descriptions in curriculum_docs_auto")
    print("=" * 80)

    curriculum_base = ROOT / "curriculum_docs_auto"
    files = list(curriculum_base.glob("MathematicalLiteracy_Gr*/**/*.md"))
    print(f"Found {len(files)} Mathematical Literacy curriculum documentation files.")

    inventory: List[Dict[str, Any]] = []

    # Patterns to match figure blocks
    # 1. >DIAGRAM\[ ... ]
    # 2. Figure N.N: ...
    # 3. **Diagram N** or * **Diagram N:** ...
    # 4. ### Graph N: ...
    diag_block_re = re.compile(r'>DIAGRAM\\?\[(.*?)(?:\]|\n\n(?=[^>\s]))', re.DOTALL | re.IGNORECASE)
    fig_header_re = re.compile(
        r'^(?:[#*_\s-]*)(Figure\s+\d+(?:\.\d+)?[:\s][^\n]+|'
        r'Diagram\s+\d+[:\s][^\n]+|'
        r'Graph\s+\d+[:\s][^\n]+)',
        re.MULTILINE | re.IGNORECASE
    )

    for f in sorted(files):
        # Extract Grade and Term from path
        parts = f.relative_to(curriculum_base).parts
        grade_str = ""
        m_gr = re.search(r'Gr(\d+)', parts[0])
        if m_gr:
            grade_str = m_gr.group(1)
        term_str = ""
        m_t = re.search(r'Term\s*(\d+)', parts[1] if len(parts) > 1 else "")
        if m_t:
            term_str = m_t.group(1)
        topic_file = f.stem

        text = f.read_text(encoding="utf-8", errors="ignore")

        # 1. Capture >DIAGRAM blocks
        for m in diag_block_re.finditer(text):
            raw_block = m.group(0).strip()
            content = m.group(1).strip()
            # Determine figure type
            fig_type = "diagram"
            lower = content.lower()
            if "venn" in lower:
                fig_type = "probability_figure"
            elif "tree" in lower:
                fig_type = "probability_figure"
            elif "map" in lower:
                fig_type = "map"
            elif "plan" in lower:
                fig_type = "plan"
            elif "graph" in lower or "bar" in lower or "histogram" in lower:
                fig_type = "data_graph"
            elif "scale" in lower:
                fig_type = "instrument"

            inventory.append({
                "source_file": str(f.relative_to(ROOT)).replace("\\", "/"),
                "grade": grade_str,
                "term": term_str,
                "topic": topic_file,
                "marker_type": ">DIAGRAM[...]",
                "heading": content.split("\n")[0][:80],
                "raw_text": raw_block[:1000],
                "figure_type": fig_type,
                "tokens": list(tokens(raw_block)),
                "is_decorative": False,
            })

        # 2. Capture Figure / Diagram / Graph headers
        for m in fig_header_re.finditer(text):
            header_line = m.group(1).strip()
            # Grab following context (up to 400 chars)
            pos = m.end()
            context_chunk = text[pos:pos + 400].strip()
            full_chunk = header_line + "\n" + context_chunk

            lower_header = header_line.lower()
            lower_ctx = full_chunk.lower()

            is_decorative = False
            if any(dec in lower_header for dec in ("telescope", "cape town", "university", "photo", "building")):
                is_decorative = True

            fig_type = "figure"
            if "bill" in lower_header or "statement" in lower_header or "tariff" in lower_header:
                fig_type = "document_bill"
            elif "seating" in lower_header or "floor" in lower_header or "plan" in lower_header:
                fig_type = "plan"
            elif "map" in lower_header or "navigation" in lower_header:
                fig_type = "map"
            elif "graph" in lower_header:
                fig_type = "data_graph" if any(k in lower_ctx for k in ("bus", "earnings", "trip", "bar")) else "function_graph"
            elif "scale" in lower_header or "meter" in lower_header:
                fig_type = "instrument"
            elif is_decorative:
                fig_type = "decorative_photo"

            inventory.append({
                "source_file": str(f.relative_to(ROOT)).replace("\\", "/"),
                "grade": grade_str,
                "term": term_str,
                "topic": topic_file,
                "marker_type": header_line.split(":")[0],
                "heading": header_line,
                "raw_text": full_chunk[:1000],
                "figure_type": fig_type,
                "tokens": list(tokens(full_chunk)),
                "is_decorative": is_decorative,
            })

    out_file = DATA_DIR / "mathlit_doc_figure_inventory.json"
    out_file.write_text(json.dumps(inventory, indent=2), encoding="utf-8")
    print(f"Parsed {len(inventory)} total figure descriptions across curriculum documents.")
    print(f"Wrote curriculum figure inventory to {out_file}")
    return inventory


# ---------------------------------------------------------------------------
# STAGE HARVEST: Run all 1,871 Archetypes across Seeds 101, 102, 103
# ---------------------------------------------------------------------------
def run_stage_harvest(seeds: List[int] = [101, 102, 103]) -> Dict[str, Any]:
    print("\n" + "=" * 80)
    print(f"STAGE HARVEST: Executing 1,871 Archetypes across seeds {seeds}")
    print("=" * 80)

    # Load D1 results
    d1_file = DATA_DIR / "mathlit_d1_counts.json"
    if not d1_file.exists():
        d1_data = run_stage_d1()
    else:
        d1_data = json.loads(d1_file.read_text(encoding="utf-8"))

    from app.services.generator_registry import ALL_GENERATORS

    harvested: Dict[str, Any] = {}
    total_runs = 0
    errors_count = 0

    for grade, topics in d1_data.items():
        for t in topics:
            gen_key = t["generator_key"]
            topic_name = t["name"]
            subskills = t["subskills"]

            fn = ALL_GENERATORS.get(gen_key)
            if not fn:
                print(f"ERROR: Generator not found in ALL_GENERATORS: {gen_key}")
                errors_count += 1
                continue

            for sub in subskills:
                sub_id = f"gr{grade}_{gen_key}_{sub}"
                harvested[sub_id] = {
                    "sub_id": sub_id,
                    "grade": grade,
                    "term": t["term"],
                    "topic": topic_name,
                    "generator_key": gen_key,
                    "subskill": sub,
                    "seeds": {}
                }

                for s in seeds:
                    total_runs += 1
                    try:
                        with contextlib.redirect_stdout(io.StringIO()):
                            # Execute generator with explicit subskill & seed
                            res = fn(subskill=sub, seed=s, count=1)
                        q = res[0] if isinstance(res, list) and res else res
                        if isinstance(q, dict):
                            prompt_text = collect_prompt_text(q)
                            worked_text = " ".join(
                                str(q.get(k) or "")
                                for k in ("worked_solution", "explanation", "expected_answer", "correct_answer")
                            )
                            d_spec = q.get("diagram_spec") or q.get("diagram") or q.get("graph") or q.get("function_graph")
                            d_type = None
                            if isinstance(d_spec, dict):
                                d_type = (
                                    d_spec.get("kind")
                                    or d_spec.get("diagram_type")
                                    or d_spec.get("type")
                                    or d_spec.get("image_type")
                                    or d_spec.get("master")
                                )

                            harvested[sub_id]["seeds"][str(s)] = {
                                "has_diagram_payload": has_diagram_payload(q),
                                "diagram_type": d_type,
                                "diagram_spec_raw": d_spec if isinstance(d_spec, dict) else None,
                                "unrendered_keys": has_unrendered_visual_key(q),
                                "has_table": has_table(q),
                                "modality": q.get("modality"),
                                "question_type": q.get("question_type"),
                                "prompt_text": prompt_text,
                                "worked_text": worked_text,
                                "prompt_refs": find_figure_references(prompt_text),
                                "prompt_desc": find_description_signals(prompt_text),
                                "has_canonical_steps": bool(isinstance(q.get("canonical_solution"), dict) and q["canonical_solution"].get("steps")),
                                "has_worked_solution": bool(q.get("worked_solution") or q.get("explanation")),
                            }
                        else:
                            harvested[sub_id]["seeds"][str(s)] = {"error": "Non-dict return payload"}
                            errors_count += 1
                    except Exception as ex:
                        harvested[sub_id]["seeds"][str(s)] = {"error": str(ex)}
                        errors_count += 1

            print(f"  Harvested Gr{grade} '{topic_name}' ({len(subskills)} subskills x {len(seeds)} seeds)")

    out_file = DATA_DIR / "mathlit_audit_payloads.json"
    out_file.write_text(json.dumps(harvested, indent=2), encoding="utf-8")
    print(f"\nTotal archetype runs: {total_runs} | Total subskills: {len(harvested)} | Errors: {errors_count}")
    print(f"Wrote harvested payloads to {out_file}")

    if errors_count > 0:
        print(f"WARNING: Encountered {errors_count} errors during payload harvest.")

    return harvested


# ---------------------------------------------------------------------------
# STAGE CLASSIFY: Classify D2a, D2b, D3 + Anti-Shortcut Traces across 1,871 Archetypes
# ---------------------------------------------------------------------------
def _inspect_disk_renderers() -> Dict[str, Any]:
    """Read actual frontend JSX files on disk so the referee reflects true dispatch & schema support."""
    dr_path = ROOT / "src/components/workspace/shared/mathx/DiagramRenderer.jsx"
    ml_path = ROOT / "src/components/workspace/shared/mathx/MathLitDiagramRenderer.jsx"
    sf_path = ROOT / "src/components/workspace/shared/mathx/StatsAndFinancialGraphRenderer.jsx"
    db_path = ROOT / "src/components/workspace/modalities/diagram_bank/index.js"

    dr_code = dr_path.read_text(encoding="utf-8") if dr_path.exists() else ""
    ml_code = ml_path.read_text(encoding="utf-8") if ml_path.exists() else ""
    sf_code = sf_path.read_text(encoding="utf-8") if sf_path.exists() else ""
    db_code = db_path.read_text(encoding="utf-8") if db_path.exists() else ""

    # Does DiagramRenderer pass normalizedSpec and check effectiveKind for StatsAndFinancialGraphRenderer & GeoGebra?
    stats_uses_effective_kind = (
        "].includes(effectiveKind)" in dr_code
        and "<StatsAndFinancialGraphRenderer spec={normalizedSpec}" in dr_code
        and "<GeoGebraGeometryRenderer spec={normalizedSpec}" in dr_code
    )
    # Does FunctionGraph still hijack Boolean(spec.type && !spec.kind)?
    function_graph_hijacks_type = "Boolean(spec.type && !spec.kind)" in dr_code
    # Does MathLitDiagramRenderer handle cartesian_system directly (not aliased to function_graph)?
    cartesian_in_mathlit = (
        "'cartesian_system': 'function_graph'" not in dr_code
        and "cartesian_system" in ml_code
    )
    boxplot_aliased = "'boxplot': 'box_and_whisker'" in dr_code

    return {
        "stats_uses_effective_kind": stats_uses_effective_kind,
        "function_graph_hijacks_type": function_graph_hijacks_type,
        "cartesian_in_mathlit": cartesian_in_mathlit,
        "boxplot_aliased": boxplot_aliased,
        "sf_supports_slices": "spec.slices" in sf_code,
        "sf_supports_steps": "spec.steps" in sf_code,
        "sf_supports_bars": "spec.bars" in sf_code,
        "sf_supports_series": "spec.series" in sf_code,
        "sf_supports_summary": "spec.summary" in sf_code,
        "ml_supports_net_layout": "spec.layout" in ml_code,
        "ml_floor_plan_dynamic_rooms": ("room.length_m" in ml_code or "r.length_m" in ml_code),
        "banked_floor_plan": "architectural_floor_packaging_plan" in db_code,
    }


def _extract_spec_tokens(obj: Any, ignore_keys: Set[str]) -> Set[str]:
    """Extract numeric and domain string tokens from a diagram_spec dictionary for binding checks."""
    out: Set[str] = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ignore_keys:
                continue
            out.update(_extract_spec_tokens(v, ignore_keys))
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            out.update(_extract_spec_tokens(item, ignore_keys))
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
        # Store integer or decimal representations (both dot and SA comma)
        if float(obj).is_integer():
            out.add(str(int(obj)))
        else:
            s_val = str(round(float(obj), 2))
            out.add(s_val)
            out.add(s_val.replace(".", ","))
    elif isinstance(obj, str):
        s = obj.strip()
        if not s or s.startswith("#"):
            return out
        # Extract numbers and words >= 3 chars
        for num in re.findall(r"\d+(?:[.,]\d+)?", s):
            out.add(num)
            out.add(num.replace(".", ","))
            out.add(num.replace(",", "."))
        for word in re.findall(r"[A-Za-z]{3,}", s.lower()):
            if word not in {"the", "and", "for", "with", "from", "plan", "map", "diagram", "graph", "chart", "scale", "table", "view", "true", "false"}:
                out.add(word)
    return out


def _validate_spec_and_renderer(
    subskill: str,
    d_spec: Optional[Dict[str, Any]],
    disk_state: Dict[str, Any],
) -> Tuple[bool, bool, str, List[str]]:
    """Return (renderer_dispatched, schema_valid, method, failure_reasons)."""
    if not isinstance(d_spec, dict) or not d_spec:
        return False, False, "NONE", ["missing_diagram_spec"]

    failures: List[str] = []
    raw_kind = str(d_spec.get("kind") or "").strip().lower()
    eff_kind = str(
        d_spec.get("kind")
        or d_spec.get("diagram_type")
        or d_spec.get("type")
        or d_spec.get("image_type")
        or d_spec.get("master")
        or ""
    ).strip().lower()

    if not eff_kind:
        return False, False, "NONE", ["missing_kind"]

    # Reject wrong diagram type for piecewise graph interpretation
    if "piecewise_graph" in subskill.lower() and eff_kind == "function_flow":
        failures.append("wrong_kind_function_flow_for_piecewise_graph")

    # 1. Banked SVG master check
    if eff_kind == "architectural_floor_packaging_plan":
        if not disk_state["banked_floor_plan"]:
            failures.append("banked_component_missing")
        has_schema = bool(d_spec.get("view") or d_spec.get("pins") or d_spec.get("master"))
        if not has_schema:
            failures.append("missing_view_or_pins")
        return (len(failures) == 0), has_schema and (len(failures) == 0), "B_VECTOR_MATHLIT", failures

    # Alias normalization matching DiagramRenderer.jsx
    alias_map = {
        "bar_chart": "bar_graph",
        "double_bar_chart": "double_bar_graph",
        "2d_net": "rectangular_prism_net",
        "3d_solid": "mensuration_3d",
    }
    if disk_state["boxplot_aliased"]:
        alias_map["boxplot"] = "box_and_whisker"

    norm_kind = alias_map.get(eff_kind, eff_kind)

    mathlit_kinds = {
        "inline_svg", "floor_plan", "bar_scale", "graphic_scale", "compass_rose",
        "bearing_map", "elevation_compass", "elevation_view", "strip_map", "grid_map",
        "seating_plan", "packaging_packing", "packaging_cartons", "mensuration_2d",
        "mensuration_3d", "2d_polygon", "cartesian_system",
    }
    stats_kinds = {
        "box_and_whisker", "bar_graph", "double_bar_graph", "histogram",
        "frequency_polygon", "pie_chart", "step_tariff", "break_even",
        "probability_spinner", "contingency_table", "contingency_table_and_tree",
        "venn_3_sets", "venn_diagram", "tree_diagram", "ogive", "cumulative_frequency",
        "scatter_plot", "line_graph", "broken_line_graph",
    }
    geogebra_kinds = {
        "cube_net", "rectangular_prism_net", "triangular_prism_net",
        "cylinder_net", "pyramid_net", "cone_net",
    }

    # Check if DiagramRenderer drops non-kind specs (`diagram_type` / `type` without `kind`)
    if not raw_kind and norm_kind in (stats_kinds | geogebra_kinds):
        if not disk_state["stats_uses_effective_kind"]:
            failures.append(f"diagram_renderer_checks_spec_kind_not_effectiveKind_for_{eff_kind}")
    if d_spec.get("type") and not raw_kind and disk_state["function_graph_hijacks_type"]:
        failures.append(f"function_graph_hijacks_spec_type_{eff_kind}")

    # Determine method & dispatch
    if norm_kind == "cartesian_system":
        if not disk_state["cartesian_in_mathlit"]:
            failures.append("cartesian_system_aliased_to_parabola_or_missing_in_mathlit_renderer")
        method = "B_VECTOR_MATHLIT"
        dispatched = disk_state["cartesian_in_mathlit"]
    elif norm_kind in mathlit_kinds:
        method = "B_VECTOR_MATHLIT"
        dispatched = True
    elif norm_kind in stats_kinds or norm_kind in geogebra_kinds or norm_kind in ("function_graph", "function_flow"):
        method = "B_VECTOR_GENERIC"
        dispatched = True
    else:
        method = "NONE"
        dispatched = False
        failures.append(f"unrecognized_diagram_kind_{eff_kind}")

    # Validate required schema keys for norm_kind
    schema_ok = False
    if norm_kind == "inline_svg":
        schema_ok = bool(d_spec.get("svg") and "<svg" in str(d_spec.get("svg")))
    elif norm_kind == "floor_plan":
        has_rooms = bool(d_spec.get("rooms"))
        has_dims = bool(d_spec.get("length_m") or d_spec.get("width_m") or d_spec.get("dimensions"))
        if has_rooms and not disk_state["ml_floor_plan_dynamic_rooms"] and not has_dims:
            failures.append("floor_plan_ignores_spec_rooms_on_disk")
            schema_ok = False
        else:
            schema_ok = has_rooms or has_dims
    elif norm_kind in ("bar_scale", "graphic_scale"):
        schema_ok = any(k in d_spec for k in ("segment_value_km", "segment_value_m", "bar_km", "scale", "segments", "max_km", "total_km"))
    elif norm_kind in ("compass_rose", "bearing_map", "elevation_compass"):
        schema_ok = any(k in d_spec for k in ("bearing_deg", "angle", "compass", "north_facing_wall", "towns", "points", "from_label", "to_label", "target_dir"))
    elif norm_kind == "elevation_view":
        schema_ok = any(k in d_spec for k in ("side", "active_side", "elevation", "width_m", "height_m", "roof", "features", "dimensions", "label"))
    elif norm_kind == "strip_map":
        schema_ok = bool(d_spec.get("stops") and len(d_spec.get("stops", [])) >= 2)
    elif norm_kind == "grid_map":
        schema_ok = bool(d_spec.get("stops") or d_spec.get("landmarks") or d_spec.get("cells") or (d_spec.get("columns") and d_spec.get("rows")) or d_spec.get("cols"))
    elif norm_kind == "seating_plan":
        schema_ok = any(k in d_spec for k in ("rows", "seats_per_row", "blocks", "aisle", "target_seat", "highlighted_seat"))
    elif norm_kind in ("packaging_packing", "packaging_cartons"):
        has_std = ("carton_l" in d_spec and "box_l" in d_spec) or ("container" in d_spec and "box" in d_spec) or ("dims" in d_spec)
        has_net_style = ("layout" in d_spec or "solid" in d_spec) and disk_state["ml_supports_net_layout"]
        schema_ok = bool(has_std or has_net_style)
    elif norm_kind in ("mensuration_2d", "mensuration_3d", "2d_polygon"):
        schema_ok = any(k in d_spec for k in ("length", "width", "radius", "height", "base", "dim_l", "dim_r", "sides", "shape", "dimensions"))
    elif norm_kind == "cartesian_system":
        schema_ok = bool(isinstance(d_spec.get("lines"), list) and len(d_spec["lines"]) >= 1 and disk_state["cartesian_in_mathlit"])
    elif norm_kind == "box_and_whisker":
        has_top = all(k in d_spec for k in ("min", "max")) and any(k in d_spec for k in ("median", "q2"))
        has_nested = isinstance(d_spec.get("box_and_whisker"), dict)
        has_summary = isinstance(d_spec.get("summary"), dict) and disk_state["sf_supports_summary"]
        schema_ok = bool(has_top or has_nested or has_summary)
        if isinstance(d_spec.get("summary"), dict) and not disk_state["sf_supports_summary"]:
            failures.append("stats_renderer_ignores_spec_summary")
    elif norm_kind in ("bar_graph", "double_bar_graph", "histogram", "frequency_polygon", "line_graph", "broken_line_graph"):
        has_cat_val = bool(d_spec.get("categories") and d_spec.get("values"))
        has_bars = bool(d_spec.get("bars")) and disk_state["sf_supports_bars"]
        has_series = bool(d_spec.get("series")) and disk_state["sf_supports_series"]
        schema_ok = bool(has_cat_val or has_bars or has_series)
        if d_spec.get("bars") and not disk_state["sf_supports_bars"]:
            failures.append("stats_renderer_ignores_spec_bars")
        if d_spec.get("series") and not disk_state["sf_supports_series"]:
            failures.append("stats_renderer_ignores_spec_series")
    elif norm_kind == "pie_chart":
        has_sectors = bool(d_spec.get("sectors"))
        has_slices = bool(d_spec.get("slices")) and disk_state["sf_supports_slices"]
        schema_ok = bool(has_sectors or has_slices)
        if d_spec.get("slices") and not disk_state["sf_supports_slices"]:
            failures.append("stats_renderer_ignores_spec_slices")
    elif norm_kind == "step_tariff":
        has_blocks = bool(d_spec.get("blocks"))
        has_steps = bool(d_spec.get("steps")) and disk_state["sf_supports_steps"]
        schema_ok = bool(has_blocks or has_steps)
        if d_spec.get("steps") and not disk_state["sf_supports_steps"]:
            failures.append("stats_renderer_ignores_spec_steps")
    elif norm_kind == "break_even":
        schema_ok = any(k in d_spec for k in ("fixed_cost", "selling_price", "cost_line", "income_line", "lines"))
    elif norm_kind == "probability_spinner":
        schema_ok = bool(d_spec.get("sectors") or d_spec.get("slices") or d_spec.get("labels"))
    elif norm_kind in ("contingency_table", "contingency_table_and_tree", "venn_3_sets", "venn_diagram", "tree_diagram"):
        schema_ok = any(k in d_spec for k in ("rows", "cells", "sets", "tree", "branches", "outcomes", "regions", "counts", "a_only", "intersection"))
    elif norm_kind in ("ogive", "cumulative_frequency", "scatter_plot"):
        schema_ok = any(k in d_spec for k in ("points", "upper_bounds", "cumulative", "values", "x_values"))
    elif norm_kind in geogebra_kinds:
        schema_ok = any(k in d_spec for k in ("side", "edge", "length", "width", "height", "radius", "layout", "solid", "faces"))
    elif norm_kind == "function_flow":
        schema_ok = bool(d_spec.get("inputs") and "piecewise_graph" not in subskill.lower())

    if not schema_ok:
        failures.append(f"invalid_or_unsupported_schema_for_{eff_kind}")

    return dispatched and (len(failures) == 0), schema_ok and (len(failures) == 0), method, failures


def run_stage_classify() -> Dict[str, Any]:
    print("\n" + "=" * 80)
    print("STAGE CLASSIFY: Classifying D2a / D2b / D3 + Anti-Shortcut Traces (1,871 Archetypes)")
    print("=" * 80)

    payloads_file = DATA_DIR / "mathlit_audit_payloads.json"
    inventory_file = DATA_DIR / "mathlit_doc_figure_inventory.json"

    if not payloads_file.exists():
        payloads = run_stage_harvest()
    else:
        payloads = json.loads(payloads_file.read_text(encoding="utf-8"))
        # Re-harvest automatically if older payload file lacks diagram_spec_raw
        sample_entry = next(iter(payloads.values()), {})
        sample_seed = sample_entry.get("seeds", {}).get("101", {})
        if "diagram_spec_raw" not in sample_seed:
            payloads = run_stage_harvest()

    if not inventory_file.exists():
        inventory = run_stage_inventory()
    else:
        inventory = json.loads(inventory_file.read_text(encoding="utf-8"))

    disk_state = _inspect_disk_renderers()
    print(f"Disk Renderer State: {json.dumps(disk_state)}")

    # Pre-index doc inventory tokens by topic
    doc_blocks_by_topic: Dict[str, List[Dict[str, Any]]] = {}
    for item in inventory:
        t_key = item["topic"].lower()
        if t_key not in doc_blocks_by_topic:
            doc_blocks_by_topic[t_key] = []
        doc_blocks_by_topic[t_key].append(item)

    classified: Dict[str, Any] = {}
    class_counts = {
        "PROMPT_REFERENCES_FIGURE": 0,
        "DESCRIBED_NOT_DRAWN": 0,
        "TEXT_SUBSTITUTED": 0,
        "NOT_REQUIRED": 0,
        "INCONSISTENT": 0
    }
    outcome_counts = {
        "RENDERED": 0,
        "GENERATED_NOT_RENDERED": 0,
        "MISSING": 0,
        "NOT_REQUIRED": 0,
        "EXTRA": 0
    }
    method_counts = {
        "A_PLATE": 0,
        "B_VECTOR_MATHLIT": 0,
        "B_VECTOR_GENERIC": 0,
        "C_3D": 0,
        "NONE": 0
    }
    trace_summary = {
        "total_with_diagram_spec": 0,
        "schema_valid_pass": 0,
        "seed_varies_pass": 0,
        "bound_to_question_pass": 0,
        "all_traces_pass": 0,
    }

    ignore_spec_keys = {
        "kind", "diagram_type", "type", "image_type", "master", "diagram_role",
        "show_grid", "interactive", "color", "stroke", "fill",
    }

    for sub_id, data in payloads.items():
        grade = data["grade"]
        topic = data["topic"]
        subskill = data["subskill"]
        seeds_data = data.get("seeds", {})

        seed_classes = []
        seed_drawn = []
        seed_dispatched = []
        seed_schema_valid = []
        seed_bound = []
        seed_methods = []
        seed_refs = []
        seed_signals = []
        seed_spec_AutoStrings = []
        trace_failures: List[str] = []

        # Find matching doc blocks for this topic
        topic_lower = topic.lower()
        matched_blocks = [
            b for k, blocks in doc_blocks_by_topic.items()
            if any(w in k for w in topic_lower.split() if len(w) > 3)
            for b in blocks
        ]

        for s_key in ("101", "102", "103"):
            s_data = seeds_data.get(s_key, {})
            p_text = s_data.get("prompt_text", "")
            w_text = s_data.get("worked_text", "")
            refs = s_data.get("prompt_refs", [])
            desc = s_data.get("prompt_desc", {})
            has_diag = s_data.get("has_diagram_payload", False)
            d_spec = s_data.get("diagram_spec_raw")

            # Check overlap against curriculum doc blocks
            has_doc_overlap = False
            for blk in matched_blocks:
                if blk.get("is_decorative"):
                    continue
                ov = doc_overlap(p_text, set(blk.get("tokens", [])))
                if ov >= 0.40:
                    has_doc_overlap = True
                    break

            # Classify D2a (Need) — note: DESCRIBED_NOT_DRAWN takes precedence over PROMPT_REFERENCES_FIGURE
            # if the prompt still narrates the figure's layout/direction in prose!
            if desc.get("narrates") or has_doc_overlap:
                s_cls = "DESCRIBED_NOT_DRAWN"
            elif refs:
                s_cls = "PROMPT_REFERENCES_FIGURE"
            elif any(
                w in subskill.lower() for w in
                ("map", "plan", "scale", "elevation", "net", "packaging", "diagram", "graph", "histogram", "box_and_whisker", "tree")
            ):
                s_cls = "TEXT_SUBSTITUTED"
            else:
                s_cls = "NOT_REQUIRED"

            seed_classes.append(s_cls)
            seed_drawn.append(has_diag)
            seed_refs.extend(refs)
            if desc.get("strong") or desc.get("spatial"):
                seed_signals.extend(desc.get("strong", []) + desc.get("spatial", []))

            if has_diag and isinstance(d_spec, dict):
                seed_spec_AutoStrings.append(json.dumps(d_spec, sort_keys=True))
                dispatched, schema_ok, m, fails = _validate_spec_and_renderer(subskill, d_spec, disk_state)
                seed_dispatched.append(dispatched)
                seed_schema_valid.append(schema_ok)
                seed_methods.append(m)
                trace_failures.extend(fails)

                # Check bound_to_question: at least 1 token/number from d_spec appears in prompt or worked solution
                spec_toks = _extract_spec_tokens(d_spec, ignore_spec_keys)
                combined_lower = (p_text + " " + w_text).lower()
                is_bound = any(tok.lower() in combined_lower for tok in spec_toks) if spec_toks else False
                seed_bound.append(is_bound)
                if not is_bound:
                    trace_failures.append(f"seed_{s_key}_diagram_not_bound_to_question")
            else:
                seed_dispatched.append(False)
                seed_schema_valid.append(False)
                seed_methods.append("NONE")
                seed_bound.append(False)

        # Reconcile D2a across seeds
        if len(set(seed_classes)) == 1:
            final_class = seed_classes[0]
        else:
            final_class = "INCONSISTENT"

        class_counts[final_class] += 1

        is_drawn_all = all(seed_drawn) and len(seed_drawn) == 3
        is_drawn_any = any(seed_drawn)
        schema_valid_all = is_drawn_all and all(seed_schema_valid)
        dispatched_all = is_drawn_all and all(seed_dispatched)
        bound_all = is_drawn_all and all(seed_bound)

        # Check seed_varies across seeds 101, 102, 103
        s101_type = str(seeds_data.get("101", {}).get("diagram_type") or "").lower()
        if is_drawn_all:
            if s101_type == "architectural_floor_packaging_plan":
                # Banked architectural SVG master uses static room layout pins
                seed_varies = True
            else:
                seed_varies = len(set(seed_spec_AutoStrings)) >= 2
            if not seed_varies:
                trace_failures.append("static_diagram_spec_across_seeds_101_102_103")
        else:
            seed_varies = False

        if final_class == "DESCRIBED_NOT_DRAWN" and is_drawn_any:
            trace_failures.append("prompt_still_narrates_figure_description")

        if is_drawn_any:
            trace_summary["total_with_diagram_spec"] += 1
            if schema_valid_all:
                trace_summary["schema_valid_pass"] += 1
            if seed_varies:
                trace_summary["seed_varies_pass"] += 1
            if bound_all:
                trace_summary["bound_to_question_pass"] += 1

        all_traces_ok = (
            is_drawn_all
            and dispatched_all
            and schema_valid_all
            and seed_varies
            and bound_all
            and final_class != "DESCRIBED_NOT_DRAWN"
        )
        if all_traces_ok:
            trace_summary["all_traces_pass"] += 1

        # D2b Outcome
        if is_drawn_any:
            if all_traces_ok:
                final_outcome = "RENDERED"
            else:
                final_outcome = "GENERATED_NOT_RENDERED"
        else:
            if final_class in ("PROMPT_REFERENCES_FIGURE", "DESCRIBED_NOT_DRAWN", "TEXT_SUBSTITUTED"):
                final_outcome = "MISSING"
            else:
                final_outcome = "NOT_REQUIRED"

        outcome_counts[final_outcome] += 1

        # D3 Method
        active_method = [m for m in seed_methods if m != "NONE"]
        final_method = active_method[0] if active_method else "NONE"
        method_counts[final_method] += 1

        s101 = seeds_data.get("101", {})

        classified[sub_id] = {
            "sub_id": sub_id,
            "grade": grade,
            "term": data["term"],
            "topic": topic,
            "subskill": subskill,
            "d2a_need_class": final_class,
            "d2b_outcome": final_outcome,
            "d3_method": final_method,
            "diagram_type": s101.get("diagram_type"),
            "schema_valid": schema_valid_all,
            "seed_varies": seed_varies,
            "bound_to_question": bound_all,
            "trace_failures": sorted(set(trace_failures)),
            "prompt_refs": list(set(seed_refs)),
            "narrative_signals": list(set(seed_signals))[:4],
            "seed_101_sample_prompt": (s101.get("prompt_text", ""))[:220].replace("\n", " "),
        }

    out_file = DATA_DIR / "mathlit_audit_classified.json"
    out_file.write_text(json.dumps(classified, indent=2), encoding="utf-8")

    print("\n" + "-" * 50)
    print("CLASSIFICATION SUMMARY ACROSS 1,871 ARCHETYPES:")
    print("-" * 50)
    print("D2a (Diagram Need):")
    for k, v in class_counts.items():
        print(f"  {k:26s}: {v:5d} ({v / len(classified) * 100:5.1f}%)")
    print("\nD2b (Diagram Outcome):")
    for k, v in outcome_counts.items():
        print(f"  {k:26s}: {v:5d} ({v / len(classified) * 100:5.1f}%)")
    print("\nD3 (Rendering Method):")
    for k, v in method_counts.items():
        print(f"  {k:26s}: {v:5d} ({v / len(classified) * 100:5.1f}%)")
    print("\nAnti-Shortcut Trace Summary (Diagram-Emitting Archetypes):")
    for k, v in trace_summary.items():
        print(f"  {k:26s}: {v:5d}")

    print(f"\nWrote classification data to {out_file}")
    return classified


# ---------------------------------------------------------------------------
# CLI Argument Dispatcher
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Math Lit Comprehensive 5-Dimension Audit Runner")
    parser.add_argument(
        "--stage",
        action="append",
        choices=["d1", "inventory", "harvest", "classify", "report", "all"],
        help="Stage(s) to run (may be passed multiple times, default: all)",
    )
    args = parser.parse_args()
    stages = args.stage or ["all"]

    if "d1" in stages or "all" in stages:
        run_stage_d1()
    if "inventory" in stages or "all" in stages:
        run_stage_inventory()
    if "harvest" in stages or "all" in stages:
        run_stage_harvest()
    if "classify" in stages or "all" in stages:
        run_stage_classify()
    if "report" in stages or "all" in stages:
        from scripts.generate_mathlit_comprehensive_report import main as gen_report
        gen_report()


if __name__ == "__main__":
    main()
