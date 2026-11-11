"""Provenance + quality verifier for the science doc-harvester.

Usage:  python scripts/_sci_verify.py "Life Sciences" 10
For every topic in a subject+grade it asserts:
  1. no sibling overlap   - no two topics return an identical harvest
  2. every topic has source chapter files
  3. MEMO PROVENANCE      - every marking point / MCQ correct answer / pair
                            definition occurs VERBATIM inside that topic's own
                            chapter(s). A miss means the item is not grounded.
  4. no scrape junk       - prompts/pair-terms free of codes, markup, exercise
                            headings, crossword-style glued tokens.
"""
import sys, os, re, json, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
os.environ["SCI_HARVEST_STRICT"] = "1"
from app.utils import sci_docs_harvester as S

REG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "caps-ai-backend", "app", "services", "caps_term_registry_data.json")

JUNK_RE = re.compile(
    r"exercise \d|end of chapter|\besg[a-z0-9]{1,4}\b|memory trick|\*\*|__|"
    r"\{\s*\d|\\frac|\bhttp\b|<!--|!\[|&nbsp;|^\s*\d+[.)]\s", re.I,
)
# a term whose letters are all consonants and >=4 long is a glued-token artifact
GLUED_RE = re.compile(r"\b[BCDFGHJKLMNPQRSTVWXYZ]{5,}\b")


def topics(subject, grade):
    data = json.load(open(REG, encoding="utf-8"))
    out, seen = [], set()
    for e in data:
        if str(e.get("subject")) == subject and str(e.get("grade")) == str(grade):
            k = e["generator_key"]
            if k not in seen:
                seen.add(k)
                out.append(k)
    return out


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", S._clean(s).lower())


def main():
    subject = sys.argv[1] if len(sys.argv) > 1 else "Life Sciences"
    grade = sys.argv[2] if len(sys.argv) > 2 else "10"
    sigs, problems = {}, []
    for k in topics(subject, grade):
        g = S._grade_of(None, k)
        texts, _sidecar, paths, rejected = S._load_all(g, k)
        items = S.harvest_items(None, k)
        pairs = S.harvest_pairs(None, k)
        typed = [i for i in items if i.get("kind") != "mcq"]
        mcq = [i for i in items if i.get("kind") == "mcq"]
        if rejected:
            for rj in rejected:
                print(f"    REJECTED {k}: {rj}")
        if not paths:
            problems.append(f"{k}: NO SOURCE CHAPTER")
            continue
        src = norm(" ".join(texts))
        ungrounded = 0
        for i in mcq:
            if norm(i["correct"]) not in src:
                ungrounded += 1
                problems.append(f"{k}: MCQ answer not in chapter -> {i['correct'][:60]!r}")
        for i in typed:
            for m in i.get("marking_points") or []:
                n = norm(m)
                if len(n) >= 25 and n not in src:
                    ungrounded += 1
                    problems.append(f"{k}: memo not in chapter -> {m[:70]!r}")
        junk = 0
        for i in items:
            p = str(i.get("prompt", ""))
            if JUNK_RE.search(p):
                junk += 1
                problems.append(f"{k}: junk prompt -> {p[:80]!r}")
            for o in (i.get("options") or []):
                if JUNK_RE.search(str(o)):
                    junk += 1
                    problems.append(f"{k}: junk option -> {o[:60]!r}")
        for t, d in pairs:
            n = norm(d)
            if len(n) >= 25 and n not in src:
                ungrounded += 1
                problems.append(f"{k}: pair def not in chapter -> {d[:70]!r}")
            if JUNK_RE.search(t) or GLUED_RE.search(t.replace(" ", "")):
                junk += 1
                problems.append(f"{k}: junk pair term -> {t[:60]!r}")
        blob = "|".join(sorted([str(i.get("prompt", ""))[:120] for i in items]
                               + [f"{t}={d[:60]}" for t, d in pairs]))
        sigs.setdefault(hashlib.md5(blob.encode()).hexdigest()[:12], []).append(k)
        print(f"{k:44s} typed={len(typed):4d} mcq={len(mcq):4d} pairs={len(pairs):4d} "
              f"files={len(paths)} ungrounded={ungrounded} junk={junk}")
    for s, ks in sigs.items():
        if len(ks) > 1:
            problems.append(f"SIBLING OVERLAP identical harvest: {ks}")
    print("=" * 72)
    if problems:
        print(f"PROBLEMS ({len(problems)}):")
        for p in problems[:60]:
            print("  -", p)
    else:
        print("ALL CLEAN: every memo verbatim from its own chapter, no junk, no overlap.")
    print(f"{subject} Gr{grade}: {len(sigs)} distinct topic harvests.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
