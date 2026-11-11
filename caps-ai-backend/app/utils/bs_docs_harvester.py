"""Business Studies curriculum-doc harvester (Gr 10-12, shared).

Extracts authentic exam/textbook questions WITH their memoranda from the
markdown curriculum docs (curriculum_docs_auto/ preferred, curriculum_docs/
as supplement). Per project policy the .md files are the primary source;
PDFs in curriculum_source_files/ are only used offline when a .md is corrupt.

Everything is deterministic (pure file parsing, zero LLM, no network) and
cached per (grade, topic_key). Corrupt or off-subject docs (e.g. a geometry
mis-scrape) are rejected by a business-vs-geometry sanity gate.

Returned items are plain typed-question dicts:
    {title, prompt, marking_points, sample_answer, marks,
     learning_objective_id, question_family_id, retry_variant, difficulties}
which both G10 (build_generate pools) and G11/G12 (make_generate) layers can
consume, feeding the typed / discussion / essay archetypes.
"""
from __future__ import annotations

import json
import os
import random
import re
from functools import lru_cache
from typing import Any, Dict, List, Optional

# Same scraped corpus as sci_docs_harvester, so the same cleaning: auditing every
# string of every harvested BS item found 145 of 4,822 units still carrying
# markup - '1\. Moral characteristics', '\[6]' mark allocations, '<sup>+</sup>'.
from .scrape_text_clean import prepare_text

# Workspace root: this file lives at
# <root>/caps-ai-backend/app/utils/bs_docs_harvester.py
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_AUTO_DIR = os.path.join(_ROOT, "curriculum_docs_auto")
_DOCS_DIR = os.path.join(_ROOT, "curriculum_docs")
_REGISTRY = os.path.join(_ROOT, "caps-ai-backend", "app", "services", "caps_term_registry_data.json")

_DOC_DIR = {10: "BusinessStudies_Gr10", 11: "BusinessStudies_Gr11", 12: "BusinessStudies_Gr12"}

# Sanctioned fallbacks for topics whose curriculum .md is corrupt or absent:
# sidecar JSON / text extracts placed next to this module, e.g.
#   harvest_overrides/grade10_bs_self_management.json
_SIDECAR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "harvest_overrides")

# tokens that must never decide doc<->topic similarity on their own
_STOPWORDS = frozenset(
    "the a an of and or for to in on with business businesses grade term "
    "recent contemporary".split()
)
_BIZ_WORDS = (
    "business consumer market environment profit entrepreneur employees "
    "management marketing production goods services company economy "
    "legislation customer ownership"
)
_GEO_WORDS = ("triangle", "angle", "circle", "theorem", "bisect", "parallel lines", "quadrilateral", "euclidean")

_QHDR_RE = re.compile(r"^\s*(?:#{0,6}\s*)?\|?\s*(?:\*\*)?\s*(\d{1,2}\.\d(?:\.\d)?)(?:\s*\*\*)?(?:\s+(.*))?$")
_MARKS_RE = re.compile(r"\((\d{1,3})(?:\s*marks?)?\)\s*[:.]?\s*$", re.I)
_BULLET_RE = re.compile(r"^(?:&nbsp;|\s|\u00a0)*(?:[*\u2022\u2013\u2014-])\s*(?=\S)(.+)$")
_ANSWER_RE = re.compile(r"^(?:#{1,6}\s*)?\**\s*answer\s*:?\s*\**\s*(.*)$", re.I)
_BREAK_RE = re.compile(r"^(?:#{1,6}\s*)?\**\s*(?:activity|question \d|consolidation|homework|note\b)", re.I)
_NUM_ONLY_RE = re.compile(r"^[\d.,;\s\-&nbsp;]*$")


def _clean(text: str) -> str:
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    text = re.sub(r"[✅ü✔×✓]", " ", text)
    text = text.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip(" .*-–—:;")


def _tokens(name: str) -> frozenset:
    return frozenset(
        w for w in re.sub(r"[^a-z0-9 ]", " ", name.lower()).split() if w and w not in _STOPWORDS
    )


@lru_cache(maxsize=1)
def _registry_names() -> List[Dict[str, Any]]:
    try:
        with open(_REGISTRY, encoding="utf-8") as fh:
            data = json.load(fh)
        return [e for e in data if "_bs_" in str(e.get("generator_key", ""))]
    except Exception:
        return []


def _topic_name(topic_key: str) -> Optional[str]:
    for entry in _registry_names():
        if entry.get("generator_key") == topic_key:
            return entry.get("name")
    return None


def _read_doc(grade: int, topic_key: str):
    """Doc content: .md first; sidecar extract only when the .md is unusable.

    Returns a str (text to parse) or a list/dict (pre-structured sidecar).
    Sidecars are trusted (hand-overridden from PDFs), so they skip the
    business-vs-geometry sanity gate.
    """
    path = _find_doc(grade, topic_key)
    if path:
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
            if _looks_business(text):
                return text
        except OSError:
            pass
    base = os.path.join(_SIDECAR_DIR, topic_key)
    for ext in (".json", ".txt", ".md"):
        side = base + ext
        if os.path.isfile(side):
            try:
                raw = open(side, encoding="utf-8", errors="replace").read()
                if ext == ".json":
                    return json.loads(raw)
                return raw
            except Exception:
                continue
    return None


def _find_doc(grade: int, topic_key: str) -> Optional[str]:
    """Best fuzzy match of topic name against doc filenames (auto tree first)."""
    name = _topic_name(topic_key)
    if not name:
        return None
    target = _tokens(name)
    if not target:
        return None
    best, best_score = None, 0.0
    for directory in (_AUTO_DIR, _DOCS_DIR):
        root = os.path.join(directory, _DOC_DIR[grade])
        if not os.path.isdir(root):
            continue
        for dirpath, _dirnames, filenames in os.walk(root):
            if os.path.basename(dirpath) == "images":
                continue
            for fn in filenames:
                if not fn.endswith(".md"):
                    continue
                cand = _tokens(os.path.splitext(fn)[0])
                if not cand:
                    continue
                inter = len(target & cand)
                score = inter / max(1, min(len(target), len(cand)))
                if score > best_score:
                    best, best_score = os.path.join(dirpath, fn), score
    return best if best_score >= 0.45 else None


def _looks_business(text: str) -> bool:
    # Reject off-subject mis-scrapes (e.g. a Euclidean-Geometry .md saved under a
    # Business Studies topic). Geometry files have ~0 business words and a huge
    # geometry-word count, so the ratio test is the real discriminator; the small
    # absolute floor only screens out empty/irrelevant stubs. Legitimate topics
    # such as 'Presentations & data responses' repeat few business keywords, so a
    # high floor wrongly rejected them.
    low = text.lower()
    biz = sum(low.count(w) for w in _BIZ_WORDS.split())
    geo = sum(low.count(w) for w in _GEO_WORDS)
    return biz >= 3 and biz > geo * 3


# ---------------------------------------------------------------------------
# Term-aware, format-tailored source selection.
#   Terms 1-3  -> curriculum_docs (curated topic files + controlled tests,
#                 exemplar papers and Mixed revision files, which carry real
#                 numbered memoranda).
#   Term 4     -> curriculum_docs_auto (only tree with Term 4 .md).
# A topic is sourced from its matched topic file(s) AND the term's exam papers
# (attributed by distinctive-topic-token overlap so sibling topics do not leak).
# ---------------------------------------------------------------------------

_GENERIC_TOKENS = frozenset(
    "business businesses environment environments term grade product products "
    "service services company companies aspect factor factors issue issues "
    "example following question answer learners learnerscan".split()
)
_DIRTERM_RE = re.compile(r"(?i)term[\s_\-]*(\d)")
_EXAM_HINT_RE = re.compile(
    r"(?i)(controlled[\s_\-]*test|exemplar|preliminary|mixed|\bexam\b)"
)
_MEMO_HEAD_RE = re.compile(r"(?i)^\s*(?:#{1,6}\s*)?\**\s*memorandum\b|^\s*MEMORANDUM\b")
_QNUM_RE = re.compile(r"^\s*(?:#{1,6}\s*)?(?:\*\*)?\s*(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)\b[.)]?\s*(.*)$")


def _topic_term(topic_key: str):
    for entry in _registry_names():
        if entry.get("generator_key") == topic_key:
            try:
                return int(str(entry.get("term")))
            except (TypeError, ValueError):
                return None
    return None


def _dir_term(dirname: str):
    m = _DIRTERM_RE.search(dirname or "")
    return int(m.group(1)) if m else None


def _distinctive_tokens(topic_key: str):
    toks = _tokens(_topic_name(topic_key) or "")
    distinctive = toks - _GENERIC_TOKENS
    return distinctive or toks


def _relevant(text: str, rel) -> bool:
    return bool(_tokens(text) & rel)


def _read_text(path):
    try:
        return open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return None


def _read_sidecar(topic_key: str):
    base = os.path.join(_SIDECAR_DIR, topic_key)
    for ext in (".json", ".txt", ".md"):
        side = base + ext
        if os.path.isfile(side):
            try:
                raw = open(side, encoding="utf-8", errors="replace").read()
                return json.loads(raw) if ext == ".json" else prepare_text(raw)
            except Exception:
                continue
    return None


def _candidate_files(grade: int, topic_key: str, term):
    name = _topic_name(topic_key) or ""
    target = _tokens(name)
    trees = [_AUTO_DIR, _DOCS_DIR] if term == 4 else [_DOCS_DIR, _AUTO_DIR]
    topic_files, exam_files = [], []
    for tree in trees:
        root = os.path.join(tree, _DOC_DIR[grade])
        if not os.path.isdir(root):
            continue
        tf, ef = [], []
        for dirpath, _dirs, filenames in os.walk(root):
            if os.path.basename(dirpath) == "images":
                continue
            dterm = _dir_term(os.path.basename(dirpath))
            for fn in filenames:
                if not fn.endswith(".md") or fn == "Syllabus.md":
                    continue
                stem = os.path.splitext(fn)[0]
                cand = _tokens(stem)
                score = len(target & cand) / max(1, min(len(target), len(cand))) if cand else 0.0
                if _EXAM_HINT_RE.search(stem):
                    if dterm is None or dterm == term:
                        ef.append(os.path.join(dirpath, fn))
                elif score >= 0.45:
                    tf.append(os.path.join(dirpath, fn))
        if tf and not topic_files:
            topic_files = tf
        if ef and not exam_files:
            exam_files = ef
    return topic_files, exam_files


@lru_cache(maxsize=128)
def _load_sources(grade: int, topic_key: str):
    term = _topic_term(topic_key)
    topic_files, exam_files = _candidate_files(grade, topic_key, term)
    topic_texts = []
    for p in topic_files:
        s = _read_text(p)
        if s and _looks_business(s):
            topic_texts.append(prepare_text(s))
    exam_texts = []
    for p in exam_files:
        s = _read_text(p)
        if s and _looks_business(s):
            exam_texts.append(prepare_text(s))
    sidecar = None
    if not topic_texts:
        # The topic's own .md is corrupt or missing: fall back to the sanctioned
        # sidecar. Exam-paper texts are term-wide and rarely cover every topic,
        # so they must not suppress this fallback; any genuinely relevant exam
        # items are merged on top of the sidecar by harvest_items.
        sidecar = _read_sidecar(topic_key)
    return tuple(topic_texts), tuple(exam_texts), sidecar


def _mk_mcq(prompt, options, correct, ci, topic_key, name, marks=2):
    return {
        "kind": "mcq", "title": "Exam MCQ", "prompt": prompt,
        "options": list(options), "correct": correct, "correct_index": str(ci),
        "marking_points": [correct], "sample_answer": correct,
        "explanation": f"Memo: the correct option is {correct}.",
        "marks": int(marks or 2), "learning_objective_id": topic_key,
        "question_family_id": f"{topic_key}_exammcq", "retry_variant": "doc_mcq",
        "difficulties": ["easy", "medium", "hard"],
        "misconception_tags": [], "diagnostic_tags": [],
        "guidelines": [f"Authentic CAPS exam question from the {name} paper."],
    }


def _exam_items(text, topic_key, name, rel):
    """Parse a question paper that has a numbered Memorandum section.

    Joins answers keyed by question number back to their stems: MCQ letters
    (1.1.1 D), short/word-list answers (1.2.1 legal) and en-dash bullet marking
    points for direct questions (2.1 ... - point). Only questions whose text
    shares a distinctive token with this topic are kept, so sibling topics in
    the same term paper do not leak in.
    """
    if not _MEMO_HEAD_RE.search(text):
        return []
    in_memo = False
    stems, options, wordset = {}, {}, set()
    cur_q = None
    memo_letter, memo_ans, memo_points, memo_title = {}, {}, {}, {}
    cur_memo = None
    for raw in text.splitlines():
        line = raw.replace("\xa0", " ").strip()
        if not line:
            continue
        if not in_memo and _MEMO_HEAD_RE.match(line):
            in_memo = True
            cur_q = cur_memo = None
            continue
        if line.startswith("#"):
            cur_q = cur_memo = None
            continue
        if not in_memo:
            m = _QNUM_RE.match(line)
            if m and not _OPTION_RE.match(line):
                rest = _clean(m.group(2) or "")
                if len(rest) >= 12 and rest[:1].lower() not in ("a", "b", "c", "d") and not rest[:2].isdigit():
                    stems[m.group(1)] = rest
                    cur_q = m.group(1)
                    options.setdefault(cur_q, {})
                    continue
            o = _OPTION_RE.match(line)
            if o and cur_q:
                options[cur_q][o.group(1)] = _clean(o.group(2))
                continue
            parts = line.replace("\t", " ").split()
            if len(parts) >= 4 and all(re.fullmatch(r"[A-Za-z&/']+", p) for p in parts) and line.lower() == line:
                wordset.update(p.strip(".,").lower() for p in parts)
            continue
        nums = re.findall(r"\d{1,2}\.\d{1,2}(?:\.\d{1,2})?", line)
        if nums:
            num = nums[-1]
            after = line[line.rfind(num) + len(num):].strip()
            cur_memo = num
            lm = re.match(r"^([A-D])\b", after)
            if lm:
                memo_letter[num] = lm.group(1)
            elif after:
                low = after.lower().strip(" .")
                if low in wordset or len(after.split()) <= 3:
                    memo_ans[num] = _clean(after)
                else:
                    memo_points.setdefault(num, [])
                    memo_title[num] = _clean(after)
            else:
                memo_points.setdefault(num, [])
            continue
        b = _BULLET_RE.match(line)
        if b and cur_memo is not None:
            t = _clean(b.group(1))
            if len(t) >= 8 and "any other relevant" not in t.lower():
                memo_points.setdefault(cur_memo, []).append(t)
    items = []
    for num, letter in memo_letter.items():
        opts = options.get(num) or {}
        stem = stems.get(num, "")
        if len(opts) < 3 or letter not in opts or len(stem) < 12:
            continue
        ordered = sorted(opts.items())
        opt_texts = [v for _, v in ordered]
        ci = [k for k, _ in ordered].index(letter)
        if not _relevant(stem, rel):
            continue
        items.append(_mk_mcq(stem, opt_texts, opts[letter], ci, topic_key, name))
    for num, ans in memo_ans.items():
        stem = stems.get(num, "")
        if len(stem) < 12 or len(ans) < 2 or not _relevant(stem, rel):
            continue
        it = _mk_typed(stem, [ans], 2, topic_key, name, "examshort")
        if it:
            items.append(it)
    for num, pts in memo_points.items():
        if len(pts) < 2:
            continue
        prompt = stems.get(num) or memo_title.get(num) or ""
        if len(prompt) < 12 or not _relevant(prompt, rel):
            continue
        it = _mk_typed(prompt, pts, min(len(pts), 8), topic_key, name, "exambullet")
        if it:
            items.append(it)
    return items


_SCENARIO_RE = re.compile(r"(?i)\b(the scenario below|use the table below|answer the questions? that follow|refer to the (?:cartoon|table|diagram|source))")


_OPTION_RE = re.compile(r"^([A-D])[ .)\t]+(?!\1)([A-Za-z][^\n]{2,200})$")


def _parse(text: str) -> List[Dict[str, Any]]:
    """State machine over doc lines.

    Handles inline style ('1.1 State three components. (4 marks)' as a bare or
    hashed heading), split style ('#### 1.1' + question on next line), MCQ
    blocks (A-D options + 'Answer' memo) and memo bullets with or without an
    'Answer' header. Bullets accumulate until the next question or a
    non-bullet paragraph closes the memo block.
    """
    items: List[Dict[str, Any]] = []
    number: Optional[str] = None
    question: Optional[str] = None
    marks: Optional[int] = None
    notes: List[str] = []
    notes_started = False
    options: List[str] = []
    in_answer_block = False

    def emit() -> None:
        nonlocal number, question, marks, notes, notes_started, options, in_answer_block
        if number and not _SCENARIO_RE.search(question or ""):
            if len(options) >= 3 and in_answer_block:
                # MCQ with a lettered memo answer
                correct = next((o for o in options if o.lower().startswith(notes[0].lower()[:40]) or notes[0].lower().startswith(o.lower()[:40])), None) if notes else None
                if correct is None and notes:
                    m = re.match(r"^([A-D])\b", notes[0])
                    letter = m.group(1) if m else None
                    idx = {"A": 0, "B": 1, "C": 2, "D": 3}.get(letter or "", -1)
                    correct = options[idx] if 0 <= idx < len(options) else None
                if question and correct and len(question) >= 20:
                    others = [o for o in options if o != correct][:3]
                    items.append({
                        "number": number,
                        "question": question,
                        "marks": marks or 1,
                        "notes": [correct] + others,
                        "mcq": {"correct": correct, "options": options[:4]},
                    })
            elif question and len(question) >= 25:
                picked = [n for n in notes if len(n) >= 15 and not _NUM_ONLY_RE.match(n)][:8]
                if len(picked) >= 2:
                    m = marks if marks is not None else len(picked)
                    if 2 <= m <= 25:
                        items.append({"number": number, "question": question, "marks": m, "notes": picked})
        number, question, marks, notes, notes_started, options, in_answer_block = None, None, None, [], False, [], False

    for raw in text.splitlines():
        line = raw.replace("\xa0", " ").strip()
        if not line or line.startswith("|"):
            continue
        b = _BULLET_RE.match(line)
        if b:
            inner = b.group(1).strip()
            qb = _QHDR_RE.match(inner)
            if qb and (qb.group(2) or "").strip():
                # bullet that is really a numbered question separator
                emit()
                number = qb.group(1)
                tail = _clean(qb.group(2) or "")
                m = _MARKS_RE.search(tail)
                if m:
                    marks = int(m.group(1))
                    tail = tail[: m.start()].strip()
                if len(tail) >= 25:
                    question = tail
                continue
            if number is not None:
                notes.append(_clean(inner))
                notes_started = True
            continue
        q = _QHDR_RE.match(line)
        if q:
            emit()
            number = q.group(1)
            tail = _clean(q.group(2) or "")
            m = _MARKS_RE.search(tail)
            if m:
                marks = int(m.group(1))
                tail = tail[: m.start()].strip()
            if len(tail) >= 25:
                question = tail
            continue
        a = _ANSWER_RE.match(line)
        if a is not None and "answer" in line.lower()[:20]:
            in_answer_block = True
            tail = _clean(a.group(1) or "")
            if tail:
                notes.append(tail)
                notes_started = True
            continue
        opt = _OPTION_RE.match(line)
        if opt and number is not None and not in_answer_block:
            options.append(_clean(opt.group(1) + " " + opt.group(2)))
            continue
        if in_answer_block and options and line[:1] in "ABCD" and not line.startswith("#"):
            notes.append(_clean(line))
            continue
        if _BREAK_RE.match(line) or (line.startswith("#") and not _ANSWER_RE.match(line)):
            # Structural boundary (a new content heading / activity / question
            # block). Always flush: a question is only emitted if its memo came
            # BEFORE this boundary. This prevents an unanswered activity
            # question from borrowing a later, unrelated section's bullets as
            # its answer; the notes-driven path supplies grounded questions
            # instead. The '#### Answer' header is excluded above.
            emit()
            continue
        # plain paragraph
        if number is not None and not question and not options:
            m = _MARKS_RE.search(line)
            cand = _clean(line[: m.start()] if m else line)
            if len(cand) >= 25:
                question = cand
                if m:
                    marks = int(m.group(1))
        elif notes_started:
            emit()
    emit()
    return items


_SECTION_PAIR_RE = re.compile(
    r"\*\*([A-Z][A-Za-z ,&'\-/]{3,60}?)\*\*[:\s]*\n?\s*([A-Z][^*\n]{40,400})"
)


def _section_pairs(text: str) -> List[tuple]:
    """(heading term, description) pairs from bold-section study texts."""
    out: List[tuple] = []
    seen = set()
    for term, desc in _SECTION_PAIR_RE.findall(text):
        term, desc = _clean(term), _clean(desc)
        low = term.lower()
        if len(term) > 45 or low in seen or not term[0].isupper():
            continue
        if any(w in low for w in ("answer", "activity", "note", "revision", "instructions")):
            continue
        seen.add(low)
        out.append((term, desc))
    return out


# ---------------------------------------------------------------------------
# Notes-driven mining: most topic .md files carry their ANSWERS in the teaching
# notes (a heading followed by its definition paragraph and/or bullet list),
# while the activity/consolidation questions have no inline memo. So we build
# grounded questions straight from the notes: heading -> prompt, the document's
# own paragraph/bullets -> memo. Purely deterministic and verifiable.
# ---------------------------------------------------------------------------

_HEAD_RE = re.compile(r"^(#{3,6})\s+(.*?)\s*$")
_DEF_LEAD_RE = re.compile(
    r"\b(?:is|are|was|were|means|mean|refer(?:s)? to|consist(?:s)? of|comprise(?:s)?|"
    r"describ(?:e|es)|defin(?:e|es|ed)|involv(?:e|es)?)\b", re.I,
)
_TERMDEF_RE = re.compile(
    r"^\s*(?:[*\u2022-]|\d+[.)])?\s*\**([A-Z][A-Za-z ,'\-/]{2,44}?)\**\s*[:\u2013-]\s+([A-Za-z].{24,300})$"
)
_STRUCT_HEADS = (
    "activity", "question", "revision", "consolidation", "homework", "example",
    "summary", "introduction", "key concepts", "learning objectives", "topic overview",
    "new words", "mind map", "diagram", "qr code", "assessment", "do you know",
    "brainstorm", "remember", "tip", "important tips", "teaching", "instructions",
)


def _clean_head(head: str) -> str:
    head = re.sub(r"^\d+(?:[.,]\d+)*[.)]?\s*", "", head)
    head = re.sub(r"^[^A-Za-z]+", "", head)
    return _clean(head)


def _structural(head: str) -> bool:
    low = head.lower().strip()
    if re.match(r"^(activity|question|figure|table)\b", low):
        return True
    return any(low.startswith(s) for s in _STRUCT_HEADS)


def _blocks(text: str):
    """Split notes into (heading, body-lines) blocks at level 3-6 headings."""
    out, head, body = [], None, []
    for raw in text.splitlines():
        line = raw.replace("\xa0", " ").strip()
        m = _HEAD_RE.match(line)
        if m:
            if head is not None:
                out.append((head, body))
            head, body = _clean_head(m.group(2)), []
            continue
        if head is not None:
            body.append(line)
    if head is not None:
        out.append((head, body))
    return out


def _block_parts(body):
    """Return (lead_paragraph, [bullet_points]) for one notes block."""
    lead, bullets = None, []
    for line in body:
        if not line or line.startswith("|"):
            continue
        b = _BULLET_RE.match(line)
        if b:
            t = _clean(b.group(1))
            if len(t) >= 8 and not _NUM_ONLY_RE.match(t):
                bullets.append(t)
            continue
        if lead is None and not _QHDR_RE.match(line) and not _BREAK_RE.match(line) and "http" not in line.lower():
            cand = _clean(line)
            if len(cand) >= 45:
                lead = cand
    return lead, bullets


def _cap1(s: str) -> str:
    return s[:1].upper() + s[1:]


def _list_prompt(head: str) -> str:
    low = head.lower()
    if low.startswith(("ways", "way", "how", "measure", "strateg", "advise", "step", "procedure", "guideline")):
        return _cap1("Suggest " + low) + "."
    if low.startswith(("importance", "benefit", "advantage", "disadvantage", "reason", "role",
                       "function", "impact", "effect", "challenge", "factor", "requirement",
                       "principle", "meaning", "consequence")):
        return _cap1("Explain the " + low) + "."
    if low.startswith(("component", "element", "characteristic", "type", "kind", "source", "cause")):
        return _cap1("State the " + low) + "."
    return f"Refer to the notes and explain the following: {head}."


def _mk_typed(prompt, memo, marks, topic_key, name, family):
    memo = [m for m in memo if m][:8]
    if not memo or len(prompt) < 20:
        return None
    return {
        "kind": "typed", "title": f"Doc note {family}",
        "prompt": prompt, "marking_points": memo,
        "sample_answer": " ".join(memo), "explanation": " ".join(memo),
        "marks": marks, "learning_objective_id": topic_key,
        "question_family_id": f"{topic_key}_{family}", "retry_variant": family,
        "difficulties": ["easy", "medium", "hard"] if len(memo) >= 4 else ["medium", "hard"],
        "misconception_tags": ["omitted_legislation_impact"] if "legislat" in prompt.lower() else [],
        "diagnostic_tags": [],
        "guidelines": [f"Answer from the {name} notes in the curriculum document."],
    }


def _notes_to_items(text, topic_key, name):
    """One 'state/explain' list question + one 'define' question per notes block."""
    out = []
    for head, body in _blocks(text):
        if len(head) < 6 or _structural(head):
            continue
        lead, bullets = _block_parts(body)
        if len(bullets) >= 3:
            marks = max(3, min(len(bullets), 8))
            it = _mk_typed(_list_prompt(head), bullets, marks, topic_key, name, "noteslist")
            if it:
                out.append(it)
        if lead and _DEF_LEAD_RE.search(lead) and len(lead) >= 50:
            it = _mk_typed(f"Explain what is meant by the following: {head}.", [lead], 2, topic_key, name, "defnote")
            if it:
                out.append(it)
    return out


def _termdef_pairs(text):
    """(term, definition) pairs from Key-concepts / 'Term: definition' lines."""
    out, seen = [], set()
    for raw in text.splitlines():
        m = _TERMDEF_RE.match(raw.replace("\xa0", " ").strip())
        if not m:
            continue
        term, defn = _clean(m.group(1)), _clean(m.group(2))
        low = term.lower()
        if len(term) > 45 or not term[:1].isupper() or low in seen:
            continue
        if any(w in low for w in ("answer", "activity", "note", "revision", "question", "page")):
            continue
        if defn[:1].isdigit() or "http" in defn.lower():
            continue
        seen.add(low)
        out.append((term, defn))
    return out


def _termdef_mcq(pairs, topic_key, name):
    """Grounded MCQs: match a definition to its term; distractors are sibling terms."""
    items = []
    if len(pairs) < 4:
        return items
    for i, (term, defn) in enumerate(pairs):
        opts = [term]
        k = 1
        while len(opts) < 4 and k <= len(pairs):
            cand = pairs[(i + k) % len(pairs)][0]
            if cand not in opts:
                opts.append(cand)
            k += 1
        if len(opts) < 4:
            break
        rng = random.Random(f"tdmcq|{topic_key}|{i}|{term}")
        rng.shuffle(opts)
        ci = opts.index(term)
        items.append({
            "kind": "mcq", "title": f"Doc Vocab MCQ {i}",
            "prompt": f'Which ONE of the following terms best matches this definition: "{defn}"?',
            "options": opts, "correct": term, "correct_index": str(ci),
            "marking_points": [term], "sample_answer": term,
            "explanation": f'"{term}" is defined in the document as "{defn}".',
            "marks": 2, "learning_objective_id": topic_key,
            "question_family_id": f"{topic_key}_tdmcq", "retry_variant": "doc_mcq",
            "difficulties": ["easy", "medium", "hard"],
            "misconception_tags": [], "diagnostic_tags": [],
            "guidelines": [f"Key vocabulary from the {name} curriculum document."],
        })
    return items


def harvest_items(grade: int, topic_key: str, limit: int = 220) -> List[Dict[str, Any]]:
    """Deterministically harvest grounded questions (with memo) for one topic.

    Sources are chosen per CAPS term (curriculum_docs for Terms 1-3,
    curriculum_docs_auto for Term 4) and read with format-tailored parsers:
      * teaching notes -> 'explain/state' questions whose memo is the doc's own
        paragraph/bullets;
      * term:definition vocabulary -> grounded MCQs (sibling-term distractors);
      * inline activity memoranda -> exam questions answered in place;
      * the term's controlled-test / exemplar numbered memoranda, joined to
        their stems by question number and relevance-filtered to this topic.
    Deduped by prompt and capped at `limit`.
    """
    try:
        topic_texts, exam_texts, sidecar = _load_sources(grade, topic_key)
        name = _topic_name(topic_key) or topic_key
        raw: List[Dict[str, Any]] = []
        if sidecar is not None:
            # sanctioned fallback for a corrupt/missing topic .md
            raw += _sidecar_items(sidecar, topic_key, limit)
        else:
            for t in topic_texts:
                raw += _inline_items(t, topic_key, name)
                raw += _notes_to_items(t, topic_key, name)
                raw += _termdef_mcq(_termdef_pairs(t), topic_key, name)
        rel = _distinctive_tokens(topic_key)
        for t in exam_texts:
            raw += _exam_items(t, topic_key, name, rel)
        out, seen = [], set()
        for it in raw:
            key = str(it.get("prompt", "")).lower()[:80]
            if not key or key in seen:
                continue
            seen.add(key)
            out.append(it)
            if len(out) >= limit:
                break
        return out
    except Exception:
        return []


def _sidecar_items(sc, topic_key, limit):
    name = _topic_name(topic_key) or topic_key
    if isinstance(sc, list):
        return [dict(it) for it in sc[:limit] if it.get("prompt") and it.get("marking_points")]
    raw = _inline_items(sc, topic_key, name) + _notes_to_items(sc, topic_key, name)
    raw += _termdef_mcq(_termdef_pairs(sc), topic_key, name)
    out, seen = [], set()
    for it in raw:
        k = str(it.get("prompt", "")).lower()[:80]
        if not k or k in seen:
            continue
        seen.add(k)
        out.append(it)
        if len(out) >= limit:
            break
    return out


def _inline_items(content, topic_key, name):
    """Questions that already carry an inline memorandum (activity answers)."""
    out: List[Dict[str, Any]] = []
    seen = set()
    for it in _parse(content):
        key = it["question"].lower()[:80]
        if key in seen:
            continue
        seen.add(key)
        if it.get("mcq"):
            opts = list(it["mcq"]["options"])
            try:
                ci = opts.index(it["mcq"]["correct"])
            except ValueError:
                continue
            out.append(_mk_mcq(it["question"], opts, it["mcq"]["correct"], ci,
                               topic_key, name, it.get("marks") or 2))
            continue
        it2 = _mk_typed(it["question"], it["notes"], it.get("marks") or len(it["notes"]),
                        topic_key, name, "docdrill")
        if it2:
            out.append(it2)
    return out


def harvest_pairs(grade: int, topic_key: str, limit: int = 120) -> List[tuple]:
    """(term, definition) pairs to ground matching / word-bank / crossword.

    Merges, per relevant topic file: bold study-text sections, Key-concepts
    term:definition lines, and notes headings whose lead paragraph defines
    them. Deterministic and deduped by term.
    """
    try:
        topic_texts, _exam, sidecar = _load_sources(grade, topic_key)
        texts = list(topic_texts)
        if isinstance(sidecar, str):
            texts = [sidecar]
        pairs: List[tuple] = []
        for content in texts:
            pairs += _section_pairs(content) + _termdef_pairs(content)
            for head, body in _blocks(content):
                if len(head) < 6 or _structural(head):
                    continue
                lead, _ = _block_parts(body)
                if lead and _DEF_LEAD_RE.search(lead) and 40 <= len(lead) <= 300:
                    pairs.append((head, lead))
        out, seen = [], set()
        for term, defn in pairs:
            low = term.lower()
            if not term or low in seen or len(term) > 60:
                continue
            seen.add(low)
            out.append((term, defn))
        return out[:limit]
    except Exception:
        return []
