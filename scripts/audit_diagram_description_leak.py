"""Diagram-description leak detector (Diagram Description -> Design Law, diagram_doctrine.md §9).

Finds questions whose text points at a figure, or narrates a figure, and checks whether the
payload actually carries a diagram. Reusable for any subject/grade.

Library use (imported by scripts/run_mathlit_comprehensive_diagram_audit.py):
    collect_prompt_text(q) -> str
    find_figure_references(text) -> list[str]
    find_description_signals(text) -> dict
    doc_overlap(text, block_tokens) -> float
    has_diagram_payload(q) -> bool

CLI (report-only unless --strict):
    python scripts/audit_diagram_description_leak.py
    python scripts/audit_diagram_description_leak.py --subject "Mathematical Literacy" --grades 10 11 12 --seeds 101
    python scripts/audit_diagram_description_leak.py --subject Mathematics --grades 10 --strict
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Text collection
# ---------------------------------------------------------------------------
TEXT_KEYS = (
    "question_text", "prompt", "question", "stem", "context", "scenario",
    "instructions", "instruction", "stimulus", "preamble", "case_study",
)
PART_KEYS = ("parts", "sub_questions", "subquestions", "questions", "items")
OPTION_KEYS = ("options", "choices")


def _strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for k in TEXT_KEYS + ("text", "label"):
            if isinstance(v.get(k), str):
                yield v[k]
    elif isinstance(v, (list, tuple)):
        for x in v:
            yield from _strings(x)


def collect_prompt_text(q: dict) -> str:
    """All learner-visible question text (stem, parts, options). Excludes memo/hints."""
    if not isinstance(q, dict):
        return ""
    out = []
    for k in TEXT_KEYS:
        if isinstance(q.get(k), str):
            out.append(q[k])
    for k in PART_KEYS:
        if k in q:
            out.extend(_strings(q[k]))
    for k in OPTION_KEYS:
        if k in q:
            out.extend(_strings(q[k]))
    # de-duplicate while preserving order (prompt and question_text are often identical)
    seen, uniq = set(), []
    for s in out:
        s2 = s.strip()
        if s2 and s2 not in seen:
            seen.add(s2)
            uniq.append(s2)
    return "\n".join(uniq)


# ---------------------------------------------------------------------------
# Signals
# ---------------------------------------------------------------------------
FIG_NOUN = (
    r"(?:diagram|figure|map|floor\s*plan|plan|graph|chart|sketch|picture|image|drawing|"
    r"photograph|net|venn\s*diagram|tree\s*diagram|strip\s*map|seating\s*plan|elevation|"
    r"bar\s*graph|pie\s*chart|histogram|box[- ]and[- ]whisker\s*(?:plot|diagram)?|"
    r"scale\s*drawing|layout|annexure)"
)
_REF_PATTERNS = [
    rf"\b(?:the|this|following|given|attached|accompanying|above|below)\s+(?:\w+\s+){{0,3}}?{FIG_NOUN}\b",
    rf"\b{FIG_NOUN}\s+(?:below|above|shown|provided|given|attached)\b",
    rf"\brefer\s+to\s+(?:the\s+)?(?:\w+\s+){{0,3}}?{FIG_NOUN}\b",
    rf"\b(?:on|from|in|using|use)\s+the\s+(?:\w+\s+){{0,2}}?{FIG_NOUN}\b",
    r"\bmeasure(?:d|ment)?\s+(?:on|from)\s+the\b",
    r"\b(?:as\s+)?(?:shown|illustrated|depicted)\s+(?:below|above|in\s+the)\b",
]
REF_RE = [re.compile(p, re.I) for p in _REF_PATTERNS]
# learner-constructs-the-figure (figure is an OUTPUT, not a stimulus)
CONSTRUCT_RE = re.compile(
    rf"\b(?:draw|sketch|plot|construct|complete|design|create)\s+(?:\w+\s+){{0,3}}?{FIG_NOUN}\b", re.I
)
NON_FIG_PLAN_RE = re.compile(
    r"\b(?:contract|prepaid|tariff|subscription|medical(?:\s+aid)?|payment|installment|pension|savings|data|pricing|phone|cellphone)\s+plans?\b",
    re.I,
)
NON_FIG_FIGURE_RE = re.compile(
    r"\b(?:population|census|sales|revenue|turnover|expenditure|budget|income|profit|loss|cost|investment|"
    r"interest|inflation|percentage|total|overall|interim|annual|monthly|quarterly|audited|deductions?|"
    r"salary|wage|tax(?:ation)?|net|gross|significant|unrounded|rounded)\s+figures?\b",
    re.I,
)
NON_FIG_NET_RE = re.compile(
    r"\bnet\s+(?:salar(?:y|ies)|wages?|pay|income|profits?|loss(?:es)?|proceeds|amounts?|values?|worth|costs?|prices?|tax(?:es)?|vat|forces?|accelerations?|work|flux|changes?|investments?|earnings|revenues?|cash|payouts?)\b|\b(?:gross|total|monthly|annual|average|resultant)\s+net\b",
    re.I,
)

SPATIAL_PHRASES = [
    r"\b(?:north|south|east|west)(?:ern)?\s+(?:wall|side|end|corner|boundary|of)\b",
    r"\bto\s+the\s+(?:left|right|north|south|east|west)\s+of\b",
    r"\b(?:opposite|adjacent\s+to|next\s+to|in\s+the\s+corner|along\s+the|parallel\s+to|perpendicular\s+to)\b",
    r"\b(?:is|are)\s+(?:located|positioned|situated|placed)\b",
    r"\bthe\s+(?:road|route|river|path|railway|street|n\d+)\s+(?:runs|passes|goes|crosses|continues)\b",
    r"\b(?:row|rows)\s+[A-Z]\b",
    r"\b(?:circle|circles)\s+(?:labelled|marked|containing|contains)\b",
    r"\b(?:intersect(?:ion|ing)?\s+of\s+the\s+circles|inside\s+the\s+box)\b",
    r"\b(?:x-axis|y-axis|horizontal\s+axis|vertical\s+axis)\b",
    r"\bthe\s+(?:graph|line|curve|bar)\s+(?:shows|passes|starts|rises|falls|reaches)\b",
    r"\b(?:shaded|labelled|marked)\s+(?:region|area|section|part|[A-Z]\b)",
    r"\bbranch(?:es)?\s+of\s+the\s+tree\b",
]
STRONG_PHRASES = [
    r"\bdrawn\s+to\s+(?:a\s+)?scale\b",
    r"\bmeasured\s+(?:width|length|height|distance)\b",
    r"\bon\s+the\s+(?:map|plan|diagram|drawing)\s+(?:measures|is|was)\b",
    r"\b(?:venn|tree)\s+diagram\s+(?:with|showing|has|containing)\b",
    r"\bthe\s+(?:map|plan|diagram|figure|graph)\s+shows\b",
]
SPATIAL_RE = [re.compile(p, re.I) for p in SPATIAL_PHRASES]
STRONG_RE = [re.compile(p, re.I) for p in STRONG_PHRASES]
DIM_RE = re.compile(
    r"\b\d+(?:[.,]\d+)?\s*(?:mm|cm|m|km)\b(?!\w)|\b\d+(?:[.,]\d+)?\s*(?:mm|cm|m)?\s*(?:by|x|×)\s*\d+(?:[.,]\d+)?\s*(?:mm|cm|m)\b",
    re.I,
)

STOP = set("""the and for with that this from have are was were will your into than then them they their
which what when where while also each such been being does done many more most much only other some
there these those very would could should about after again against below above between both during
under over shall must learner learners question answer calculate determine show work marks mark rand
""".split())


def tokens(text: str) -> set:
    return {w for w in re.findall(r"[a-z]{4,}", text.lower()) if w not in STOP}


def find_figure_references(text: str) -> list:
    construct_spans = [m.span() for m in CONSTRUCT_RE.finditer(text)]
    non_fig_plan_spans = [m.span() for m in NON_FIG_PLAN_RE.finditer(text)]
    non_fig_figure_spans = [m.span() for m in NON_FIG_FIGURE_RE.finditer(text)]
    non_fig_net_spans = [m.span() for m in NON_FIG_NET_RE.finditer(text)]
    hits = []
    for rx in REF_RE:
        for m in rx.finditer(text):
            s, e = m.span()
            if any(cs <= s < ce or cs < e <= ce for cs, ce in construct_spans):
                continue
            if any(ns <= s < ne or ns < e <= ne for ns, ne in non_fig_plan_spans):
                continue
            if any(fs <= s < fe or fs < e <= fe for fs, fe in non_fig_figure_spans):
                continue
            if any(ns <= s < ne or ns < e <= ne for ns, ne in non_fig_net_spans):
                continue
            hits.append(m.group(0).strip())
    return sorted(set(hits))


def find_constructs(text: str) -> list:
    return sorted({m.group(0).strip() for m in CONSTRUCT_RE.finditer(text)})


def find_description_signals(text: str) -> dict:
    spatial = sorted({m.group(0).strip() for rx in SPATIAL_RE for m in rx.finditer(text)})
    strong = sorted({m.group(0).strip() for rx in STRONG_RE for m in rx.finditer(text)})
    dims = DIM_RE.findall(text)
    return {
        "spatial": spatial,
        "strong": strong,
        "dimension_count": len(dims),
        "narrates": bool(strong) or (len(spatial) >= 2 and len(dims) >= 2),
    }


def doc_overlap(text: str, block_tokens: set) -> float:
    """Share of a doc figure block's content words that reappear in the prompt."""
    if len(block_tokens) < 8:
        return 0.0
    return len(tokens(text) & block_tokens) / len(block_tokens)


DIAGRAM_KEYS = ("diagram_spec", "diagram", "graph", "function_graph")
OTHER_VISUAL_KEYS = ("diagram_meta", "visual_context", "svg", "svg_data", "image", "image_url", "chart")


def has_diagram_payload(q: dict) -> bool:
    """True only for keys UniversalWorkspace actually renders in the question card (L1298)."""
    return any(isinstance(q.get(k), dict) and q.get(k) for k in DIAGRAM_KEYS)


def has_unrendered_visual_key(q: dict) -> list:
    return [k for k in OTHER_VISUAL_KEYS if q.get(k)]


def has_table(q: dict) -> bool:
    if q.get("headers") and q.get("rows"):
        return True
    for k in ("table", "table_schema", "data_table", "markdown_table"):
        if q.get(k):
            return True
    return bool(re.search(r"^\s*\|.*\|\s*$\n^\s*\|\s*:?-{3,}", collect_prompt_text(q), re.M))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _harvest(subject: str, grades: list, seeds: list, all_archetypes: bool = True):
    sys.path.insert(0, str(ROOT / "caps-ai-backend"))
    from app.services.generator_registry import generate_variant, get_topic_archetypes  # noqa: E402

    reg = json.loads((ROOT / "caps-ai-backend/app/services/caps_term_registry_data.json").read_text(encoding="utf-8"))
    topics = [r for r in reg if str(r.get("grade")) in grades and subject.lower() in str(r.get("subject", "")).lower()]
    for t in topics:
        subskills = [None]
        if all_archetypes:
            try:
                arch_info = get_topic_archetypes(t["name"], grade=str(t["grade"]), subject=t["subject"])
                if arch_info and arch_info.get("archetypes"):
                    subskills = arch_info["archetypes"]
            except Exception:
                subskills = [None]
        for subskill in subskills:
            for seed in seeds:
                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        kwargs = {"topic": t["name"], "seed": seed, "grade": str(t["grade"]), "subject": t["subject"], "count": 1}
                        if subskill:
                            kwargs["subskill"] = subskill
                        qs = generate_variant(**kwargs)
                    yield t, seed, (qs[0] if qs else None), None
                except Exception as e:  # report, never hide
                    yield t, seed, None, repr(e)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject", default="Mathematical Literacy")
    ap.add_argument("--grades", nargs="+", default=["10", "11", "12"])
    ap.add_argument("--seeds", nargs="+", type=int, default=[101])
    ap.add_argument("--all-archetypes", action="store_true", default=True, help="scan all registered archetypes for each topic (default: True)")
    ap.add_argument("--sample-only", action="store_true", help="only scan default single sample per topic")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any critical/high finding")
    args = ap.parse_args()

    n = crit = high = errs = 0
    for t, seed, q, err in _harvest(args.subject, args.grades, args.seeds, all_archetypes=not args.sample_only):
        n += 1
        if err or not q:
            errs += 1
            print(f"  ERROR  Gr{t['grade']} {t['name']} seed={seed}: {err}")
            continue
        text = collect_prompt_text(q)
        refs = find_figure_references(text)
        desc = find_description_signals(text)
        drawn = has_diagram_payload(q)
        if refs and not drawn:
            crit += 1
            print(f"  CRITICAL PROMPT_REFERENCES_FIGURE/no diagram  Gr{t['grade']} {t['name']} [{q.get('subskill')}] refs={refs[:3]}")
        elif desc["narrates"] and not drawn:
            high += 1
            print(f"  HIGH     DESCRIBED_NOT_DRAWN  Gr{t['grade']} {t['name']} [{q.get('subskill')}] signals={(desc['strong'] or desc['spatial'])[:3]}")
    print(f"\nScanned {n} questions | critical={crit} high={high} errors={errs}")
    sys.exit(1 if args.strict and (crit or high or errs) else 0)


if __name__ == "__main__":
    main()
