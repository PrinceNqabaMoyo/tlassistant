"""Deterministic curriculum-doc harvester for Natural/Physical/Life Sciences.

Rationale (2026-11 audit)
-------------------------
For sciences there is NO manually typed curriculum_docs tree (only a partial
Physical-Science Gr10/11), so the auto-scraped markdown in
``curriculum_docs_auto/<Subject>_Gr<NN>/Term <T>/*.md`` is the only per-topic
source. Those files were produced by the mypdf pipeline from the textbook PDFs;
they carry rich STRUCTURE (``# CHAPTER``, ``## Key Terminology`` markdown tables
``| **term** | definition | illustration |``, ``####`` notes headings with
bulleted memo-points) but are bloated with image noise (``![alt](x.png)`` and
``<!-- DIAGRAM_PLACEHOLDER -->`` comments).

We therefore mine the .md (token-free) rather than re-extract the textbook PDFs:
the .md already re-imposes the table/heading structure that raw PDF text
extraction loses. A textbook PDF is only opened as a narrow per-topic fallback
(see ``_pdf_fallback`` hook) when a topic's .md is genuinely absent/thin.
Exam papers are a separate Phase-2 concern (they live ONLY as PDFs).

Everything is deterministic (pure file parsing, zero LLM, no network) and cached
per (grade, topic_key). Returned items mirror the Business Studies harvester
shapes so the existing archetype integrity checks and quality gates apply:

    typed: {kind,title,prompt,marking_points,sample_answer,explanation,marks,...}
    mcq:   {...,options,correct,correct_index,...}
    pairs: [(term, definition), ...]   # grounds word_bank/matching/crossword
"""
from __future__ import annotations

import json
import os
import random
import re
from functools import lru_cache
from typing import Any, Dict, List, Optional

# Scraped-markdown hygiene is shared with bs_docs_harvester: the same corpus, the
# same LaTeX / HTML / escaped-punctuation artefacts, one implementation.
from .scrape_text_clean import (delatex as _delatex,
                               html_to_text as _html_to_text, prepare_text)

# Workspace layout: <root>/caps-ai-backend/app/utils/sci_docs_harvester.py
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_AUTO_DIR = os.path.join(_ROOT, "curriculum_docs_auto")
# original textbook PDFs; scraped when a .md chapter is corrupt/absent
_PDF_DIR = os.path.join(_ROOT, "curriculum_source_files")
_REG = os.path.join(_ROOT, "caps-ai-backend", "app", "services", "caps_term_registry_data.json")
# Optional hand-curated sidecars for a topic whose auto .md is corrupt/thin.
_SIDECAR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sci_harvest_overrides")

# subject -> auto folder stem (grade interpolated)
_SUBJECT_DIR = {
    "Life Sciences": "LifeSciences_Gr",
    "Natural Sciences": "NaturalSciences_Gr",
    "Physical Sciences": "PhysicalSciences_Gr",
}

_STOPWORDS = frozenset(
    "the a an of and or for to in on with grade term chapter unit topic "
    "introduction overview summary".split()
)

# --- noise + structure patterns ------------------------------------------------
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
_IMG_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")          # ![desc](img.png)
_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\([^)]*\)")     # [text](url) -> keep? drop
_HEAD_RE = re.compile(r"^(#{2,6})\s+(.*?)\s*$")
_BULLET_RE = re.compile(r"^(?:&nbsp;|\s|\u00a0)*(?:[*\u2022\u2013\u2014-])\s+(?=\S)(.+)$")
# | **term** | definition | ... |   (Key Terminology tables)
_TROW_RE = re.compile(r"^\s*\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|")
# inline  **Term**: definition   or   Term — definition (>=24 chars)
_TERMDEF_INLINE_RE = re.compile(
    r"^\s*(?:[*\u2022-]\s*)?\**([A-Z][A-Za-z ,'\-/]{2,44}?)\**\s*[:\u2013-]\s+([A-Za-z].{24,300})$"
)
_NUM_ONLY_RE = re.compile(r"^[\d.,;\s\-&nbsp;%]*$")
_DEF_LEAD_RE = re.compile(
    r"\b(?:is|are|was|were|means|mean|refers to|consist(?:s)? of|comprise(?:s)?|"
    r"describ(?:e|es)|defin(?:e|es|ed)|involv(?:e|es)?)\b", re.I,
)
_STRUCT_HEADS = (
    "activity", "question", "revision", "consolidation", "homework", "summary",
    "introduction", "key term", "key concept", "learning objective", "topic overview",
    "new words", "mind map", "diagram", "figure", "table", "assessment", "do you know",
    "brainstorm", "remember", "tip", "important", "teaching", "instructions",
    "investigation", "practical", "experiment", "safety",
)


def _clean(text: str) -> str:
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    # citation / activity codes like [ESG5K] ( ), < >
    text = re.sub(r"\[[A-Z]{1,3}\d{1,3}[A-Za-z]?\]", " ", text)
    # NO general 'all-caps + digit' sweep. One used to sit here (a bare-code
    # cleanup for tokens like ESG82 / 2CXD) and it was silently deleting real
    # curriculum content: census over the 163 science .md files gave 553 matches
    # of which only 152 were evidence tags, the rest being CO2 (80x), NH3 (52x),
    # SO2 (31x), CH4 (18x), HNO3, CH3COO, KNO3, NO2, SO4, WFPC2, PH7 and ax2 -
    # and it deleted them only when preceded by a space, so the same formula
    # survived at the start of a memo and broke verbatim grounding. The real
    # tags all belong to the ES family, which the narrow rule below already
    # covers, so nothing is lost by dropping the sweep.
    text = re.sub(r"\bES[GB][BCDFGHJKLMNPQRSTVWXYZ0-9]{1,3}\b", " ", text)
    # LaTeX: drop $...$ delimiters and backslash-escaped punctuation; keep inner words
    text = re.sub(r"\\\((.+?)\\\)", r"\1", text)
    text = text.replace("$", "")
    text = re.sub(r"\\([_*(){}\[\]#&%$])", r"\1", text)   # \_ -> _  \( -> (
    text = re.sub(r"\\[a-zA-Z]+", " ", text)              # \frac \text -> drop
    # markdown emphasis / stray leading dashes from broken bullets
    text = text.replace("**", " ").replace("__", " ")
    text = re.sub(r"_(\S[^_]*?)_", r"\1", text)            # _italic_ -> italic
    text = re.sub(r"(?<![A-Za-z])[*_](?![A-Za-z])", " ", text)
    text = re.sub(r"^\s*[-\u2013\u2014]\s*", "", text)      # leading '- ' artifact
    text = text.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2018", "'")          # left single quote -> ASCII
    # Wingdings / checkbox artifacts only. U+00D7 x and U+00FC u are NOT listed:
    # multiplication signs and accented names are real content.
    text = re.sub(r"[\u2705\u2714\u2716\u2718\u2713\u2611\u2610\uf0fc\uf0a8]", " ", text)
    # cp1252-read-as-utf8 mojibake (a 3-char run starting with U+00E2). Only the
    # multi-char SEQUENCE is the signature: single chars in U+0080-U+00BF are
    # REAL punctuation this corpus needs - degree (1998 occurrences, temperatures),
    # plus-minus (92, tolerances), one-half (60). Deleting the whole range
    # silently turned "25 degrees C" into "25 C".
    text = re.sub(r"\u00e2[\u0080-\u00bf]{1,2}", " ", text)
    text = re.sub(r"\u00c2[\u0080-\u00bf]", " ", text)
    text = text.replace("\u00bd", "1/2").replace("\u00bc", "1/4").replace("\u00be", "3/4")
    text = re.sub(r"[\u00a9\u00ae]", " ", text)   # copyright / registered marks
    # subscript/superscript braces: H_{2}O -> H2O ; bare subscripts: G_1 -> G1
    text = re.sub(r"[_^]\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"([A-Za-z])_(?=\d)", r"\1", text)
    # brackets emptied by the code strips above
    text = re.sub(r"[\(\[]\s*[\)\]]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" .*-\u2013\u2014:;")


_AFRIKAANS = frozenset(
    "die van met deur en is word nie vir op hom haar ons julle "
    "beweging uniforme snelheid verandering liggaam skeikunde "
    "deur 'n "
    .split()
)
_INSTR_HEADS = (
    "explain", "state", "describe", "compare", "contrast", "construct", "add",
    "divide", "multiply", "calculate", "determine", "use", "refer", "name",
    "give", "write", "draw", "list", "complete", "fill", "answer", "remember",
    "rewrite", "substitute", "find", "show", "sketch", "label", "match",
    "watch", "see", "click", "visit", "read", "study", "observe", "hence",
    "avoid", "clench", "colour", "color", "underline", "tick", "circle",
    "identify", "indicate", "repeat", "try", "place", "keep", "take", "get",
)
_ARTICLE_HEADS = ("the ", "a ", "an ", "this ", "these ", "their ", "its ")
# multi-word boilerplate rows from the scrape's study aids. NOTE: this must stay
# a set of PHRASES - splitting this string on whitespace would turn "memory trick"
# into the separate words "memory"/"trick" and never match the 2-word term.
_BAD_TERMS = frozenset((
    "clue", "hint", "hints", "example", "examples", "note", "notes",
    "remember", "tip", "answer", "question", "activity", "definition",
    "term", "illustration", "figure", "table", "instructions", "do you know",
    "key words", "key word", "new words", "memory trick", "memory tricks",
    "mnemonic", "end of chapter exercises", "exercise", "activities",
    "multiple choice", "short questions", "matching", "true or false",
    "words to know", "hard words", "key terms",
))
# Second-person prose is an instruction, not a curriculum term. Deliberately
# narrow: no "it"/"is"/"of" style stopwords, because a token-substring test
# would reject almost every real definition. Only pronoun forms that signal
# learner-directed prose are listed.
_PERSONAL = frozenset("you your yours we us our ours they them".split())
# leads that only point at a list/figure are not definitions
_POINTER_RE = re.compile(
    r"\b(following|as follows|below|above|illustrated|shown|given here|listed)\b", re.I,
)
# headings/boilerplate that can never be a curriculum TERM. Curated as first-
# word matches so a real entry like "Tissue" or "Cell wall" is never dropped.
_BAD_TERM_HEADS = frozenset(
    "activity activities question questions revision consolidation homework "
    "summary introduction overview diagram figure table tables assessment "
    "investigation practical experiments experiment safety instructions teaching "
    "brainstorm remember remind tip tips important note notes example examples "
    "clue hints hint answer answers definition definitions defined term terms "
    "illustration exercise exercises video memory mnemonics mnemonic matching "
    "multiple true false words word keywords clue "
    "authentic archetype worked exam-style memo memorandum".split()
)


def _looks_afrikaans(s: str) -> bool:
    toks = set(re.sub(r"[^a-z ]", " ", s.lower()).split())
    return len(toks & (_AFRIKAANS - {"is", "en", "op", "die"})) >= 2 or (
        "beweging" in toks or "snelheid" in toks or "uniforme" in toks
    )


def _bad_term(t: str) -> bool:
    if not t or len(t) > 45:
        return True
    low = t.lower().strip()
    words = low.split()
    if low in _BAD_TERMS or len(words) > 8:
        return True
    if words and words[0] in _BAD_TERM_HEADS:
        return True
    # section-number / contents-table rows: '3.2', '11.2', '2.6', '6.5'
    if re.fullmatch(r"[\d.,()\s]+", t):
        return True
    if words and words[0] in _INSTR_HEADS:
        return True
    if any(w in _PERSONAL for w in words):
        return True
    if low.startswith(_ARTICLE_HEADS):
        return True
    if t.endswith("?") or "http" in low or ". " in t:
        return True
    if ":" in t or "exercise" in low or "video" in low:
        return True
    # contents-table / sequence labels are not vocabulary ("First phase",
    # "Step 2", "Row 3") - they make meaningless vocab-MCQ answers.
    if re.match(r"^(first|second|third|fourth|fifth|sixth|next|last|previous)\s+"
                r"(phase|step|stage|part|day|week|term|year|row|line|column|question|item)\b", low):
        return True
    if re.match(r"^(step|stage|phase|part|figure|row|column|line|item|no\.?)\s*\d", low):
        return True
    return _looks_afrikaans(t)


def _bad_def(d: str) -> bool:
    if not d or len(d) < 24:
        return True
    low = d.lower().strip()
    words = low.split()
    if words and words[0] in _INSTR_HEADS:
        return True
    if words and words[0] in _PERSONAL:
        return True
    if d.rstrip().endswith("?"):
        return True
    if len(words) > 90:  # exercise solutions / long instructions
        return True
    if re.match(r"^\d+[.)]\s", d) or "http" in low or "video" in low or "click" in low:
        return True
    # "X are responsible for the following functions" is a pointer, not a memo
    if _POINTER_RE.search(d) and not re.search(r"[.;:]\s*[A-Za-z]", d):
        return True
    return _looks_afrikaans(d)


def _tokens(name: str) -> frozenset:
    return frozenset(
        w for w in re.sub(r"[^a-z0-9 ]", " ", (name or "").lower()).split()
        if w and w not in _STOPWORDS
    )


@lru_cache(maxsize=1)
def _registry_rows() -> List[Dict[str, Any]]:
    try:
        with open(_REG, encoding="utf-8") as fh:
            data = json.load(fh)
        return [e for e in data if str(e.get("subject")) in _SUBJECT_DIR]
    except Exception:
        return []


@lru_cache(maxsize=256)
def _topic_meta(topic_key: str):
    """(subject, grade, terms set, names set) from the registry for a generator_key.

    A single PS generator_key can back several topic names; we union them so doc
    matching is not artificially narrowed to one row.
    """
    subject, grade, terms, names = None, None, set(), set()
    for e in _registry_rows():
        if e.get("generator_key") == topic_key:
            subject = subject or e.get("subject")
            if grade is None:
                try:
                    grade = int(str(e.get("grade")))
                except (TypeError, ValueError):
                    grade = None
            try:
                terms.add(int(str(e.get("term"))))
            except (TypeError, ValueError):
                pass
            if e.get("name"):
                names.add(str(e.get("name")))
    return subject, grade, frozenset(terms), tuple(sorted(names))


def _grade_of(grade: Optional[int], topic_key: str) -> Optional[int]:
    if grade is not None:
        return int(grade)
    return _topic_meta(topic_key)[1]


# ---------------------------------------------------------------------------
# Topic -> candidate doc files.
#
# The registry ``name`` IS the chapter title and the auto-scrape names its file
# ``NN. <chapter title>.md``, so the reliable signal is a NORMALIZED STRING
# match, not fuzzy token overlap. Pure token scoring made sibling chapters bleed
# into each other ("Introduction to life sciences" and "The chemistry of life"
# both scored on the generic token 'life' and pulled the same 4 files).
#
# Tiered, so placement is provable per topic:
#   1.0  normalized chapter title == registry name
#   0.8  one contains the other (scrape renamed/duplicated a word)
#   fuzzy token-overlap ONLY when nothing matched directly (odd filenames)
# ---------------------------------------------------------------------------
_DIRTERM_RE = re.compile(r"(?i)term[\s_\-]*(\d)")
_NUM_PREFIX_RE = re.compile(r"^\s*\d+[.)]?\s*")


def _dir_term(dirname: str):
    m = _DIRTERM_RE.search(dirname or "")
    return int(m.group(1)) if m else None


def _norm_name(s: str) -> str:
    s = _NUM_PREFIX_RE.sub("", (s or "").lower())
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(w for w in s.split() if w not in _STOPWORDS)


def _candidate_files(grade: int, topic_key: str) -> List[tuple]:
    """[(score, path)] chapters whose FILENAME matches the topic name.

    Score keeps the tier visible to the caller: 1.0 exact, 0.8 containment,
    <0.8 fuzzy. A sub-topic (e.g. 'Food security' inside the human-impact
    chapter) must not be answered by a fuzzy 0.55 chapter match, so _load_all
    only accepts >=0.8 here and otherwise falls through to section scoping.
    """
    subject, _g, terms, names = _topic_meta(topic_key)
    stem = _SUBJECT_DIR.get(subject or "")
    if not stem:
        return []
    root = os.path.join(_AUTO_DIR, f"{stem}{grade}")
    if not os.path.isdir(root):
        return []
    targets = sorted({t for t in (_norm_name(n) for n in names) if len(t) >= 4})
    if not targets:
        targets = [t for t in [_norm_name(topic_key.replace("_", " "))] if t]
    if not targets:
        return []
    target_sets = [frozenset(t.split()) for t in targets]

    direct: List[tuple] = []
    fuzzy: List[tuple] = []
    for dirpath, _dirs, filenames in os.walk(root):
        if os.path.basename(dirpath) == "images":
            continue
        dterm = _dir_term(os.path.basename(dirpath))
        for fn in filenames:
            if not fn.endswith(".md") or fn == "Syllabus.md":
                continue
            fnorm = _norm_name(os.path.splitext(fn)[0])
            if not fnorm:
                continue
            ftoks = frozenset(fnorm.split())
            bias = 0.05 if (terms and dterm in terms) else 0.0
            path = os.path.join(dirpath, fn)
            if fnorm in targets:
                direct.append((1.0 + bias, path))
                continue
            # containment: needs a real title, not one stray word
            if any(
                (len(tset) >= 2 and (tset <= ftoks or ftoks <= tset))
                or (len(t) >= 8 and (t in fnorm or fnorm in t))
                for t, tset in zip(targets, target_sets)
            ):
                direct.append((0.8 + bias, path))
                continue
            score = max(len(tset & ftoks) / max(1, min(len(tset), len(ftoks)))
                        for tset in target_sets)
            if score + bias >= 0.55:
                fuzzy.append((score + bias, path))
    pool = direct if direct else fuzzy
    pool.sort(reverse=True)
    return pool


def _strip_images(text: str) -> str:
    text = _HTML_COMMENT_RE.sub(" ", text)
    text = _IMG_RE.sub(" ", text)
    return text


# --- wrong-subject gate ---------------------------------------------------
# The mypdf pipeline mis-filed whole chapters into the wrong subject tree, e.g.
#   LifeSciences_Gr11/Term 4/04. Human impact on the environment.md  -> Business
#   NaturalSciences_Gr9/Term 2/04. Reactions of Acids and bases.md   -> Business
#   PhysicalSciences_Gr12/... electrochemistry                       -> Accounting
# Measured on those files: home-word hits 12 vs business 173, and 3 vs 97,
# while genuine chapters score home 596-613 with business 4-8. So "foreign
# dominates home" separates them by two orders of magnitude. Business Studies
# harvesting already had this guard (_looks_business); sciences had none.
_HOME_WORDS = {
    "Life Sciences": (
        "cell", "organ", "enzyme", "mitosis", "meiosis", "dna", "species",
        "ecosystem", "photosynthesis", "respiration", "nutrient", "tissue",
        "skeleton", "biodiversity", "microorganism", "virus", "bacteria",
        "fungi", "plant", "animal", "physiology", "homeostasis", "genetic",
        "evolution", "nervous", "hormone", "reproduction", "digestion",
    ),
    "Natural Sciences": (
        "atom", "element", "energy", "force", "circuit", "ecosystem", "weather",
        "matter", "compound", "mixture", "motion", "magnet", "light", "sound",
        "food", "vertebrate", "classification", "cycle", "soil", "climate",
        "dissolve", "gravity", "friction", "temperature", "species",
    ),
    "Physical Sciences": (
        "atom", "molecule", "mole", "stoichiomet", "circuit", "electromagnet",
        "newton", "momentum", "velocity", "acceleration", "organic", "titration",
        "ion", "bond", "electric", "voltage", "current", "ray", "wave",
        "kinetic", "equilibrium", "anode", "cathode", "electrode", "oxidation",
    ),
}
# business / accounting / social-studies markers that must NOT dominate science
_FOREIGN_WORDS = (
    "business", "micro environment", "market environment", "macro environment",
    "entrepreneur", "stanp", "cash book", "ledger", "debit", "credit", "vat",
    "income statement", "balance sheet", "stakeholder", "marketing mix", "swot",
    "pestle", "paye", "sars", "coida", "gaap", "bank reconciliation", "debtors",
    "creditors", "human rights", "democracy", "parliament", "colonis",
)


# keyword stems matched as substrings (their word forms vary: stoichiometry /
# stoichiometric, electromagnetism / electromagnetic induction)
_STEMS = ("stoichiomet", "electromagnet")


def _kw_count(low: str, words) -> int:
    """Word-boundary keyword count.

    Plain substring counting is not safe here: "ion" occurs inside
    "reconciliation" and "current" inside "currently", which inflated the home
    score of a pure Accounting file to 420 and nearly let it pass the gate.
    """
    n = 0
    for w in words:
        w = w.strip()
        if " " in w or w in _STEMS:
            n += low.count(w)                       # phrase / stem: substring ok
        else:
            n += len(re.findall(r"\b" + re.escape(w) + r"(?:s|es|ing|ed)?\b", low))
    return n


def _wrong_subject(text: str, subject) -> bool:
    words = _HOME_WORDS.get(subject or "")
    if not words:
        return False
    low = text.lower()
    home = _kw_count(low, words)
    foreign = _kw_count(low, _FOREIGN_WORDS)
    return foreign >= 10 and foreign > home


# ---------------------------------------------------------------------------
# LaTeX de-escaping and inline-HTML conversion live in scrape_text_clean, imported
# above, because the Business Studies harvester reads the same scraped markdown
# and leaked the same artefacts ('1\. Moral characteristics', '\[6]' as a mark
# allocation, '<sup>+</sup>' as an ion charge). The history of why each pass
# exists is recorded there.
# ---------------------------------------------------------------------------


def _read_text(path: str) -> Optional[str]:
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return None


# ---------------------------------------------------------------------------
# Textbook PDF scraping.
#
# Why this exists: the auto-scrape mis-filed whole chapters with another
# subject's text (5 confirmed), so those topics would otherwise be empty. The
# source PDFs for the SAME chapters are clean, so scraping them recovers them.
#
# The output must be markdown: _blocks() splits a document ONLY on '##'/'###'
# headings, and _TROW_RE reads key terms only from '| **term** | def |' table
# rows. A plain text dump has neither and harvests nothing, so this uses
# pymupdf4llm - the same engine caps-ai-backend/curriculum_docs/extract_pdf.py
# used for the original scrape - which emits both.
# ---------------------------------------------------------------------------
# PDF file prefix per subject. Natural Sciences is SINGULAR here but its auto
# folder is PLURAL - the two are not interchangeable.
_PDF_STEM = {
    "Life Sciences": "LifeSciences",
    "Natural Sciences": "NaturalScience",
    "Physical Sciences": "PhysicalSciences",
}
_PDF_NAME_RE = re.compile(r"^Textbook_(?P<stem>.+?)_Gr(?P<grade>\d+)_(?P<chap>.+)\.pdf$", re.I)


def pdf_roots():
    """Where the original textbook/syllabus PDFs live: one flat directory."""
    return [_PDF_DIR] if os.path.isdir(_PDF_DIR) else []


@lru_cache(maxsize=1)
def _pdf_index():
    """{(subject, grade): {norm_chapter_title: path}} from the textbook PDFs."""
    idx: Dict[tuple, Dict[str, str]] = {}
    stem2sub = {v: k for k, v in _PDF_STEM.items()}
    for root in pdf_roots():
        for dirpath, _dirs, filenames in os.walk(root):
            for fn in filenames:
                m = _PDF_NAME_RE.match(fn)
                if not m:
                    continue
                subject = stem2sub.get(m.group("stem"))
                if not subject:
                    continue
                key = (subject, int(m.group("grade")))
                norm = _norm_name(m.group("chap"))
                if len(norm) >= 4:
                    idx.setdefault(key, {}).setdefault(norm, os.path.join(dirpath, fn))
    return idx


# Wingdings / checkbox bullets. Replaced by '-' rather than deleted, so they
# become real bullets that _BULLET_RE can already parse.
_DINGBAT = re.compile(r"[\u2705\u2714\u2716\u2718\u2713\u2611\u2610\uf0fc\uf0a8]")


def _pdf_doc_clean(text: str) -> str:
    """Whole-document cleanup for text coming out of a PDF.

    Deliberately NOT _clean(): _clean collapses every newline into a single
    space because it is written for terms and definitions, and applying it to a
    chapter flattened 88k characters into one line, destroying the '##' heading
    structure that _blocks() splits on. Only document-level artefacts are fixed
    here; per-item cleaning still happens downstream.
    """
    text = _DINGBAT.sub("-", text)
    text = re.sub(r"\u00e2[\u0080-\u00bf]{1,2}", " ", text)   # mojibake runs
    text = re.sub(r"\u00c2[\u0080-\u00bf]", " ", text)
    return text.replace("\xa0", " ")


def _md_table_row(row: str) -> str:
    """Merge several bold runs inside ONE table cell into a single bold term.

    pymupdf4llm renders a key-terminology table as
        |**greenhouse gases**<br>**(GHGS)**|gases which trap heat...|
    and _TROW_RE only matches one '| **term** |' run, so the cell's bold parts
    are joined into one term after <br> has become a space.
    """
    cells = []
    for cell in row.split("|"):
        parts = re.findall(r"\*\*(.+?)\*\*", cell)
        if len(parts) >= 2:
            plain = re.sub(r"\*\*.+?\*\*", " ", cell).strip()
            cell = " **" + " ".join(p.strip() for p in parts) + "**" + (" " + plain if plain else "")
        cells.append(cell)
    return "|".join(cells)


# Inline-HTML handling ('## **<mark>Water purification</mark>**',
# 'NH<sub>4</sub><sup>+</sup>') lives in scrape_text_clean.html_to_text: the same
# tags broke syllabus heading matching and leaked into prompts here, and into
# Business Studies rubrics the same way.


def _md_line(ln: str) -> str:
    """Normalise one scraped line: unwrap heading bold, join multi-bold cells."""
    s = ln.lstrip()
    if s.startswith("#"):
        return ln.replace("**", "")
    if s.startswith("|"):
        return _md_table_row(ln)
    return ln


def _prepare(text: str) -> str:
    """Document-level hygiene applied to every source before harvesting."""
    return prepare_text(_strip_images(text))


@lru_cache(maxsize=512)
def _pdf_to_md(path: str) -> str:
    """Textbook PDF -> markdown, scraped with the repo's own engine.

    caps-ai-backend/curriculum_docs/extract_pdf.py already uses pymupdf4llm for
    exactly this job, and measuring it against a hand-rolled font-size heading
    reconstruction on the same files settled the choice (LS Gr11 ch.10 then PS
    Gr12 ch.13):
        markdown headings   70 -> 123  /  32 -> 203
        table rows           0 -> 242  /   0 -> 143
        term/def pairs       7 ->  56  /   8 ->  10
    write_images=False is deliberate: the committed auto tree is littered with
    images/*.md links because the original scrape ran with write_images=True,
    and that noise is what the harvester then has to strip.
    """
    try:
        import pymupdf4llm
    except ImportError:  # pragma: no cover - optional dependency
        return ""
    try:
        text = pymupdf4llm.to_markdown(path, write_images=False, show_progress=False)
    except Exception:  # pragma: no cover - unreadable pdf
        return ""
    text = re.sub(r"<br\s*/?>", " ", text)
    text = _html_to_text(text)
    text = "\n".join(_md_line(ln) for ln in text.splitlines())
    return _delatex(_pdf_doc_clean(text))


def _pdf_for_topic(grade: int, topic_key: str):
    """(path, score) best textbook PDF for a topic, or (None, 0).

    Exact / containment matching only - NO fuzzy fallback. Fuzzy at 0.55 mapped
    'Electrochemical reactions' onto Electric-circuits.pdf, which would have
    silently generated electrochemistry questions from an electric-circuits
    chapter. A wrong chapter is worse than no chapter.
    """
    subject, _g, _terms, names = _topic_meta(topic_key)
    stem = _PDF_STEM.get(subject or "")
    if not stem:
        return None, 0.0
    table = _pdf_index().get((subject, int(grade))) or {}
    targets = sorted({t for t in (_norm_name(n) for n in names) if len(t) >= 4})
    if not targets:
        targets = [t for t in [_norm_name(topic_key.replace("_", " "))] if t]
    best, best_score = None, 0.0
    for t in targets:
        tset = frozenset(t.split())
        for norm, path in table.items():
            score = 0.0
            if norm == t:
                score = 1.0
            else:
                fset = frozenset(norm.split())
                if (len(tset) >= 2 and (tset <= fset or fset <= tset)) or \
                   (len(t) >= 8 and (t in norm or norm in t)):
                    score = 0.8
            if score > best_score:
                best, best_score = path, score
    return best, best_score


def _pdf_fallback(grade: int, topic_key: str) -> Optional[tuple]:
    """(cleaned_markdown_text, path) from the topic's textbook PDF, or None.

    Used when every .md candidate was rejected (wrong subject / too thin), which
    is exactly the corrupt-chapter case. Same cleanliness + subject gate as .md.
    """
    path, _score = _pdf_for_topic(grade, topic_key)
    if not path:
        return None
    cleaned = _pdf_to_md(path)          # already normalised by _pdf_to_md
    if not cleaned:
        return None
    if _wrong_subject(cleaned, _topic_meta(topic_key)[0]):
        return None
    if len(cleaned) < 1200 or not re.search(r"^#{2,6}\s", cleaned, re.M):
        return None
    return cleaned, path


# ---------------------------------------------------------------------------
# Section-level topics.
#
# The syllabus splits one chapter into several separately-assessed topics: LS
# Gr11 Term 4 is a single chapter ("Human impact on the environment") but FOUR
# syllabus topics (water purification & recycling, food security, loss of
# biodiversity, solid waste). FILENAME matching can never reach those, and a
# fuzzy filename match would quietly serve one topic another topic's questions.
# So we cut the chapter at its own headings and harvest only that region.
# ---------------------------------------------------------------------------
_MIN_SECTION_CHARS = 700


def _targets_for(topic_key: str):
    """[(norm_name, token_set)] the topic names the registry knows for a key.

    A name joined with '&' is TWO syllabus topics sharing one line ('Water
    purification & recycling'), so both halves are added: the textbook keeps
    them as separate sections and the joined form matches neither on its own.
    'and' is NOT split, because CAPS writes real single topics with it ('Life
    processes in plants and animals') and splitting those would widen matching.
    """
    names = list(_topic_meta(topic_key)[3])
    extra = [part for n in names if "&" in n for part in n.split("&")]
    names += extra
    targets = sorted({t for t in (_norm_name(n) for n in names) if len(t) >= 4})
    if not targets:
        targets = [t for t in [_norm_name(topic_key.replace("_", " "))] if t]
    return [(t, frozenset(t.split())) for t in targets]


def _head_hit(hn: str, targets) -> bool:
    """Does a section heading name the topic? Exact or token-containment only.

    Partial overlap was tried and rejected: 'Human respiration' matched the
    'Cellular respiration' heading on the single shared token 'respiration',
    which would have served respiratory-chemistry questions under a human-
    physiology topic. CAPS topic names appear verbatim as textbook headings, so
    a strict rule loses nothing real.
    """
    if not hn:
        return False
    toks = frozenset(hn.split())
    for t, tset in targets:
        if hn == t:
            return True
        if len(tset) >= 2 and (tset <= toks or toks <= tset):
            return True
        if len(tset) == 1 and len(toks) >= 2 and tset <= toks:
            return True
    return False


def _scope_to_headings(text: str, targets) -> str:
    """Text under headings that match the topic, up to the next equal/higher
    heading. Returns '' when nothing matches or the region is too small."""
    out, open_lvl = [], None
    for raw in text.splitlines():
        m = _HEAD_RE.match(raw.strip())
        if m:
            lvl = len(m.group(1))
            if open_lvl is not None and lvl <= open_lvl:
                open_lvl = None
            if open_lvl is None and _head_hit(_norm_name(_clean_head(m.group(2))), targets):
                open_lvl = lvl
                out.append(raw)
                continue
        if open_lvl is not None:
            out.append(raw)
    sec = "\n".join(out)
    return sec if len(sec) >= _MIN_SECTION_CHARS else ""


def _section_sources(grade: int, topic_key: str):
    """[(region_text, rel_path)] from the scraped .md tree.

    Only .md is searched: opening every textbook PDF of a grade at request time
    is far too slow, so mined chapters are materialised into this same tree by
    scripts/mine_pdf_chapters.py. The subject gate is re-applied here, which is
    what keeps a corrupt chapter from being 'rescued' by section scoping.
    """
    subject = _topic_meta(topic_key)[0]
    targets = _targets_for(topic_key)
    stem = _SUBJECT_DIR.get(subject or "")
    if not targets or not stem:
        return []
    root = os.path.join(_AUTO_DIR, f"{stem}{grade}")
    if not os.path.isdir(root):
        return []
    out = []
    for dirpath, _dirs, filenames in os.walk(root):
        if os.path.basename(dirpath) == "images":
            continue
        for fn in filenames:
            if not fn.endswith(".md") or fn == "Syllabus.md":
                continue
            path = os.path.join(dirpath, fn)
            raw = _read_text(path)
            if not raw:
                continue
            cleaned = _prepare(raw)
            if len(cleaned) < 1200 or _wrong_subject(cleaned, subject):
                continue
            sec = _scope_to_headings(cleaned, targets)
            if sec:
                out.append((sec, os.path.relpath(path, _AUTO_DIR).replace("\\", "/")))
    return out


@lru_cache(maxsize=256)
def _load_all(grade: int, topic_key: str):
    """(texts, sidecar, source_paths, rejected_paths) for provenance reporting."""
    subject = _topic_meta(topic_key)[0]
    texts: List[str] = []
    used: List[str] = []
    rejected: List[str] = []
    for score, p in _candidate_files(grade, topic_key):
        raw = _read_text(p)
        if not raw:
            continue
        cleaned = _prepare(raw)
        rel = os.path.relpath(p, _AUTO_DIR).replace("\\", "/")
        if _wrong_subject(cleaned, subject):
            # mis-scraped chapter holding another subject's text
            rejected.append(rel + " [wrong subject]")
            continue
        if len(cleaned) > 1200 and (re.search(r"^#{2,6}\s", cleaned, re.M) or "| **" in cleaned):
            texts.append(cleaned)
            used.append(rel if score >= 0.8 else f"{rel} [weak filename match {score:.2f}]")
        else:
            rejected.append(rel + " [too thin]")
    sidecar = _read_sidecar(topic_key)
    if not texts and sidecar is None:
        # sub-topic of a chapter (no filename match): cut the chapter at its own
        # heading so questions stay inside the right syllabus topic
        for text, rel in _section_sources(grade, topic_key):
            texts.append(text)
            used.append(rel + " [chapter section]")
    if not texts and sidecar is None:
        # still nothing: the scrape is corrupt/absent, so mine the textbook PDF
        fb = _pdf_fallback(grade, topic_key)
        if fb:
            texts.append(fb[0])
            used.append(os.path.relpath(fb[1], _ROOT).replace("\\", "/") + " [mined from PDF]")
    return tuple(texts), sidecar, tuple(used), tuple(rejected)


def _load_sources(grade: int, topic_key: str):
    texts, sidecar, _paths, _rejected = _load_all(grade, topic_key)
    return texts, sidecar


def _read_sidecar(topic_key: str):
    base = os.path.join(_SIDECAR_DIR, topic_key)
    for ext in (".json", ".md", ".txt"):
        side = base + ext
        if os.path.isfile(side):
            try:
                raw = open(side, encoding="utf-8", errors="replace").read()
                return json.loads(raw) if ext == ".json" else _strip_images(raw)
            except Exception:
                continue
    return None


# ---------------------------------------------------------------------------
# Miners: term/definition pairs (tables + inline), notes blocks -> typed,
# pairs -> vocab MCQ. Mirrors the proven BS extractors.
# ---------------------------------------------------------------------------
def _termdef_pairs(text: str) -> List[tuple]:
    out, seen = [], set()
    for line in text.splitlines():
        line = line.replace("\xa0", " ").strip()
        term = d = None
        m = _TROW_RE.match(line)
        if m:
            term, d = m.group(1), m.group(2)
        else:
            mi = _TERMDEF_INLINE_RE.match(line)
            if mi and "|" not in line:
                term, d = mi.group(1), mi.group(2)
        if not term:
            continue
        term, d = _clean(term), _clean(re.sub(r"^\|", "", d or ""))
        term = re.sub(r"(?i)^(definition|definitions|meaning|what is)\s+of\s+", "", term).strip()
        low = term.lower()
        if _bad_term(term) or _bad_def(d):
            continue
        if low in seen:
            continue
        seen.add(low)
        out.append((term, d))
    return out


def _blocks(text: str):
    out, head, body = [], None, []
    for raw in text.splitlines():
        line = raw.replace("\xa0", " ").strip()
        m = _HEAD_RE.match(line)
        if m:
            if head is not None:
                out.append((head, body))
            head, body = _clean_head(m.group(2)), []
            continue
        if head is not None and line:
            body.append(line)
    if head is not None:
        out.append((head, body))
    return out


def _clean_head(head: str) -> str:
    head = re.sub(r"^\d+(?:[.,]\d+)*[.)]?\s*", "", head)
    head = re.sub(r"^(?:chapter|unit|topic)\b[^A-Za-z]*", "", head, flags=re.I)
    head = re.sub(r"(?i)^(definition|definitions|meaning)\s+of\s+", "", head)
    head = re.sub(r"^[^A-Za-z]+", "", head)
    return _clean(head)


def _structural(head: str) -> bool:
    low = head.lower().strip()
    return any(low.startswith(s) for s in _STRUCT_HEADS)


def _block_parts(body):
    lead, bullets = None, []
    for line in body:
        if line.startswith("|"):
            continue
        b = _BULLET_RE.match(line)
        if b:
            t = _clean(b.group(1))
            if len(t) >= 8 and not _NUM_ONLY_RE.match(t):
                bullets.append(t)
            continue
        if lead is None and len(line) > 2 and not _structural(line):
            cand = _clean(line)
            if len(cand) >= 45 and "http" not in cand.lower() and not _bad_def(cand):
                lead = cand
    return lead, bullets


def _cap1(s: str) -> str:
    return s[:1].upper() + s[1:]


def _list_prompt(head: str) -> str:
    low = head.lower()
    if re.match(r"^(stages?|steps?|phases?|process|procedure|method|way|how|types?|kinds?|categor)", low):
        return _cap1("State the " + low) + "."
    if re.match(r"^(importance|role|function|significance|advantage|disadvantage|benefit|"
                r"effect|impact|consequence|reason|purpose|need|factor)", low):
        return _cap1("Explain the " + low) + "."
    if re.match(r"^(difference|similarity|compare)", low):
        return _cap1("Differentiate/compare the following: " + low) + "."
    if re.match(r"^(component|part|element|characteristic|feature|source|cause|structure|organ)", low):
        return _cap1("Describe the " + low) + "."
    return f"With reference to the notes, describe the following: {head}."


def _mk_typed(prompt, memo, marks, topic_key, name, family):
    memo = [m for m in memo if m][:8]
    if not memo or len(prompt) < 20:
        return None
    return {
        "kind": "typed", "title": f"Doc note {family}", "prompt": prompt,
        "marking_points": memo, "sample_answer": " ".join(memo),
        "explanation": " ".join(memo), "marks": marks,
        "learning_objective_id": topic_key,
        "question_family_id": f"{topic_key}_{family}", "retry_variant": family,
        "difficulties": ["easy", "medium", "hard"] if len(memo) >= 4 else ["medium", "hard"],
        "misconception_tags": [], "diagnostic_tags": [],
        "guidelines": [f"Answer from the {name} notes in the curriculum document."],
    }


def _notes_to_items(text, topic_key, name):
    out = []
    for head, body in _blocks(text):
        if len(head) < 6 or _structural(head) or _bad_term(head):
            continue
        lead, bullets = _block_parts(body)
        bullets = [b for b in bullets if not _bad_def(b) and not _looks_afrikaans(b)]
        if len(bullets) >= 3:
            marks = max(3, min(len(bullets), 8))
            it = _mk_typed(_list_prompt(head), bullets, marks, topic_key, name, "noteslist")
            if it:
                out.append(it)
        if lead and _DEF_LEAD_RE.search(lead) and len(lead) >= 50 and not _bad_def(lead) \
                and not _looks_afrikaans(lead) and not _bad_term(head):
            it = _mk_typed(f"Explain what is meant by the following: {head}.", [lead], 2,
                           topic_key, name, "defnote")
            if it:
                out.append(it)
    return out


def _mk_mcq(prompt, options, correct, ci, topic_key, name, marks=1):
    return {
        "kind": "mcq", "title": "Doc Vocab MCQ", "prompt": prompt,
        "options": list(options), "correct": correct, "correct_index": str(ci),
        "marking_points": [correct], "sample_answer": correct,
        "explanation": f'"{correct}" is defined in the document as the matching term.',
        "marks": int(marks or 1), "learning_objective_id": topic_key,
        "question_family_id": f"{topic_key}_tdmcq", "retry_variant": "doc_mcq",
        "difficulties": ["easy", "medium", "hard"],
        "misconception_tags": [], "diagnostic_tags": [],
        "guidelines": [f"Key vocabulary from the {name} curriculum document."],
    }


def _termdef_mcq(pairs, topic_key, name):
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
        items.append(_mk_mcq(
            f'Which ONE of the following terms best matches this definition: "{defn}"?',
            opts, term, ci, topic_key, name))
    return items


# ---------------------------------------------------------------------------
# Public API (mirrors bs_docs_harvester)
# ---------------------------------------------------------------------------
# A scraper/regex bug used to be invisible because harvest_* swallowed every
# exception and returned []. Set SCI_HARVEST_STRICT=1 to raise during review.
_STRICT = os.environ.get("SCI_HARVEST_STRICT") == "1"


def harvest_items(grade: Optional[int], topic_key: str, limit: int = 220) -> List[Dict[str, Any]]:
    try:
        g = _grade_of(grade, topic_key)
        if g is None:
            return []
        texts, sidecar = _load_sources(g, topic_key)
        names = _topic_meta(topic_key)[3]
        name = names[0] if names else topic_key
        raw: List[Dict[str, Any]] = []
        if isinstance(sidecar, list):
            raw += [dict(it) for it in sidecar if it.get("prompt") and it.get("marking_points")]
        else:
            src = [sidecar] if isinstance(sidecar, str) else texts
            for t in src:
                raw += _notes_to_items(t, topic_key, name)
                raw += _termdef_mcq(_termdef_pairs(t), topic_key, name)
        out, seen = [], set()
        for it in raw:
            key = str(it.get("prompt", "")).lower()[:90]
            if not key or key in seen:
                continue
            seen.add(key)
            out.append(it)
            if len(out) >= limit:
                break
        return out
    except Exception:
        if _STRICT:
            raise
        return []


def harvest_pairs(grade: Optional[int], topic_key: str, limit: int = 120) -> List[tuple]:
    try:
        g = _grade_of(grade, topic_key)
        if g is None:
            return []
        texts, sidecar = _load_sources(g, topic_key)
        src = [sidecar] if isinstance(sidecar, str) else texts
        pairs: List[tuple] = []
        for t in src:
            pairs += _termdef_pairs(t)
            for head, body in _blocks(t):
                if len(head) < 6 or _structural(head) or _bad_term(head):
                    continue
                lead, _ = _block_parts(body)
                if lead and _DEF_LEAD_RE.search(lead) and 40 <= len(lead) <= 300 \
                        and not _bad_def(lead) and not _looks_afrikaans(lead):
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
        if _STRICT:
            raise
        return []
