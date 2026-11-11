"""Shared deterministic helpers for Grade 10 Business Studies generators.

Mirrors the deterministic gold-standard pattern used by grade10_accounting
(seeded RNG + curated content banks + builder functions) but emits the question
shapes understood by the Business Studies /generate and /mark endpoints:

    mcq    -> {question_type, prompt, options, correct_index(str), explanation, marks, ...}
    typed  -> {question_type, prompt, marking_points, sample_answer, explanation, marks, ...}

No LLM is used. Generation is fully deterministic given a seed.
"""
from __future__ import annotations

import random
import re
import uuid
from typing import Any, Dict, List, Optional


def rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    r.seed(int(seed)) if seed is not None else r.seed()
    return r


def make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


try:
    from ..sa_naming_engine import pick_sa_scenario
except ImportError:
    from app.utils.sa_naming_engine import pick_sa_scenario

# A dynamic bank of South-African flavoured business scenarios.
# Context is drawn deterministically from sa_naming_engine with proportional
# representation across all 9 provinces and SA demographic groups.
def pick_scenario(r: random.Random) -> Dict[str, str]:
    return pick_sa_scenario(r)


# Kept for backward compatibility with static imports
BUSINESS_SCENARIOS: List[Dict[str, str]] = [
    {"business": "Khumalo Fresh Produce CC", "owner": "Lindiwe Khumalo", "industry": "retail groceries"},
    {"business": "Mokoena Renewable Solutions (Pty) Ltd", "owner": "Kagiso Mokoena", "industry": "clean energy"},
    {"business": "Van der Merwe Logistics", "owner": "Pieter van der Merwe", "industry": "transport"},
    {"business": "Naidoo & Chetty Distributors", "owner": "Priya Naidoo", "industry": "wholesale"},
    {"business": "Baloyi Cold-Chain Freight (Pty) Ltd", "owner": "Tinyiko Baloyi", "industry": "cold-chain logistics"},
    {"business": "Hendricks Marine Fabrication CC", "owner": "Denver Hendricks", "industry": "light engineering"},
]


def make_mcq(
    *,
    prefix: str,
    prompt: str,
    options: List[str],
    correct_index: int,
    explanation: str,
    marks: int = 2,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    hint_text = hint or explanation
    c_idx = int(correct_index)
    exp_ans = options[c_idx] if 0 <= c_idx < len(options) else ""
    return {
        "id": make_id(f"{prefix}_mcq"),
        "question_type": "mcq",
        "modality": "math",
        "solution_type": "mcq",
        "prompt": prompt,
        "options": list(options),
        "correct_index": str(c_idx),
        "expected_answer": exp_ans,
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint_text,
        "hints": {
            "tier_1": hint or "Read the question carefully and review all multiple-choice options.",
            "tier_2": explanation or "Apply the governing CAPS business principle to identify the single correct choice.",
            "tier_3": f"Core rationale: {explanation}" if explanation else "Eliminate the distractors to select the correct answer.",
        },
        "guidelines": list(guidelines or []),
        "visual_aid_key": visual_aid_key,
    }


def make_typed(
    *,
    prefix: str,
    prompt: str,
    marking_points: List[str],
    sample_answer: str,
    marks: Optional[int] = None,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    resolved_marks = int(marks) if marks is not None else max(1, len(marking_points))
    hint_text = hint or (f"Make sure your answer covers: {', '.join(marking_points[:3])}." if marking_points else "")
    schema = {
        "total_marks": resolved_marks,
        "marking_points": [
            {
                "id": f"mp_{idx + 1}",
                "desc": pt,
                "marks": max(1, resolved_marks // max(1, len(marking_points))),
                "target_concepts": [w for w in re.split(r"[,/;\s]+", pt) if len(w) > 3],
                "editable": True,
            }
            for idx, pt in enumerate(marking_points)
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    return {
        "id": make_id(f"{prefix}_typed"),
        "question_type": "typed",
        "modality": "semantic",
        "solution_type": "marking_points",
        "prompt": prompt,
        "marking_points": list(marking_points),
        "marking_schema": schema,
        "sample_answer": sample_answer,
        "expected_answer": sample_answer,
        "explanation": sample_answer,
        "marks": resolved_marks,
        "hint_trigger": hint_text,
        "hints": {
            "tier_1": hint or "Focus on the key business concept or definition requested.",
            "tier_2": "Ensure your explanation addresses each required marking point.",
            "tier_3": f"Sample response direction: {sample_answer}" if sample_answer else "State the concept clearly with relevant business context.",
        },
        "guidelines": list(guidelines or []),
        "visual_aid_key": visual_aid_key,
    }


def _normalise_text_parts(
    text_parts: Optional[List[str]], blanks: List[str], prompt: str
) -> List[str]:
    """Coerce authored segments into the shape WordBankQuestionUI expects.

    The UI renders ``parts[i]`` followed by the blank slot ``blanks[i]`` for every
    non-final element, so ``text_parts`` MUST be exactly ``len(blanks) + 1`` long.

    Authoring files commonly write one segment *before* and one segment *after*
    every blank, which produces ``2 * len(blanks)`` (or ``2 * len(blanks) + 1`` when
    a lone trailing "." is also given) segments. Rendered literally, those extra
    segments become *phantom blanks*. Fold each trailing separator into the
    following prefix so the visible sentence is preserved:

        ["The ", " does X.", "The ", " does Y.", "The ", " does Z."]
        -> ["The ", " does X.The ", " does Y.The ", " does Z."]
    """
    parts = list(text_parts) if text_parts else [prompt] + [""] * len(blanks)
    want = len(blanks) + 1
    if len(parts) == want:
        return parts
    n = len(blanks)
    if n and len(parts) in (2 * n, 2 * n + 1):
        # parts layout: prefix0, sep0, prefix1, sep1, ... prefixN-1, sepN-1 [, tail]
        merged: List[str] = [parts[0]]
        for i in range(1, 2 * n - 1, 2):
            merged.append(parts[i] + parts[i + 1])
        # The final segment (and any lone trailing separator) belongs to the last part.
        merged.append("".join(parts[2 * n - 1:]))
        if len(merged) == want:
            return merged
    if len(parts) > want:
        return parts[: want - 1] + ["".join(parts[want - 1:])]
    return parts + [""] * (want - len(parts))


def make_wordbank(
    *,
    prefix: str,
    prompt: str,
    pool: List[str],
    blanks: List[str],
    correct_map: Dict[str, str],
    explanation: str,
    marks: int = 2,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
    text_parts: Optional[List[str]] = None,
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Build a word-bank question.

    `blanks`   – list of blank labels, e.g. ["1", "2", "3"]
    `correct_map` – dict mapping blank label -> correct word from pool,
                   e.g. {"1": "Marketing", "2": "Production"}
    `text_parts` – optional list of text segments surrounding blanks.
                   Length should be len(blanks) + 1. Used by WordBankQuestionUI.
    """
    hint_text = hint or explanation
    # Structured blanks for frontend WordBankQuestionUI compatibility
    structured_blanks = [{"id": str(b), "label": str(b)} for b in blanks]
    resolved_text_parts = _normalise_text_parts(text_parts, blanks, prompt)
    return {
        "id": make_id(f"{prefix}_wb"),
        "question_type": "word_bank",
        "modality": "math",
        "solution_type": "word_bank",
        "prompt": prompt,
        "word_bank": list(pool),
        "blanks": structured_blanks,
        "correct_map": dict(correct_map),
        "expected_answer": str(correct_map),
        "text_parts": resolved_text_parts,
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint_text,
        "hints": {
            "tier_1": hint or "Read the entire sentence and identify the missing business term.",
            "tier_2": "Eliminate terms from the word bank that don't match the grammatical context.",
            "tier_3": f"Correct concept: {explanation}" if explanation else "Place the exact terminology from the bank.",
        },
        "guidelines": list(guidelines or []),
        "visual_aid_key": visual_aid_key,
    }


def make_matching(
    *,
    prefix: str,
    prompt: str,
    column_a: List[str],
    column_b: List[str],
    correct_pairs: Dict[str, str],
    explanation: str,
    marks: int = 2,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Build a matching-columns question.

    `column_a`    – left-side items, e.g. ["A", "B", "C"]
    `column_b`    – right-side items, e.g. ["1", "2", "3"]
    `correct_pairs` – mapping from column_a label -> column_b label,
                     e.g. {"A": "2", "B": "1", "C": "3"}
    """
    hint_text = hint or explanation
    return {
        "id": make_id(f"{prefix}_match"),
        "question_type": "matching_columns",
        "modality": "math",
        "solution_type": "matching",
        "prompt": prompt,
        "column_a": list(column_a),
        "column_b": list(column_b),
        "correct_pairs": dict(correct_pairs),
        "expected_answer": str(correct_pairs),
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint_text,
        "hints": {
            "tier_1": hint or "Match the most obvious business concept first.",
            "tier_2": "Look for defining keywords connecting Column A to Column B.",
            "tier_3": f"Matching rationale: {explanation}" if explanation else "Align each descriptor with its exact term.",
        },
        "guidelines": list(guidelines or []),
        "visual_aid_key": visual_aid_key,
    }


def make_crossword(
    *,
    prefix: str,
    prompt: str,
    words: List[str],
    clues: Dict[str, str],
    grid_size: int = 10,
    explanation: str,
    marks: int = 2,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Build a crossword question.

    `words`    – list of words to place in the grid (uppercase)
    `clues`    – dict mapping word -> clue text
    `grid_size`– size of the square grid
    """
    hint_text = hint or explanation
    return {
        "id": make_id(f"{prefix}_cross"),
        "question_type": "crossword",
        "modality": "math",
        "solution_type": "crossword",
        "prompt": prompt,
        "words": [w.upper() for w in words],
        "clues": dict(clues),
        "grid_size": int(grid_size),
        "expected_answer": ", ".join(words),
        "explanation": explanation,
        "marks": int(marks),
        "hint_trigger": hint_text,
        "hints": {
            "tier_1": hint or "Check the letter count of the blank grid slots.",
            "tier_2": "Read the clue carefully for CAPS business vocabulary terms.",
            "tier_3": f"Clue answer: {explanation}" if explanation else "Fill the intersecting letters to verify.",
        },
        "guidelines": list(guidelines or []),
        "visual_aid_key": visual_aid_key,
    }


def make_essay(
    *,
    prefix: str,
    prompt: str,
    rubric: List[Dict[str, Any]],
    sample_answer: str,
    marks: int = 20,
    min_words: int = 150,
    max_words: int = 400,
    hint: Optional[str] = None,
    visual_aid_key: Optional[str] = None,
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Build an essay / long-form question.

    `rubric` – list of criteria dicts, e.g.
        [{"criterion": "Introduction", "marks": 4, "description": "..."}, ...]
    """
    hint_text = hint or (
        "Plan your answer: write an introduction, develop your points in the body, "
        "and finish with a conclusion."
    )
    schema = {
        "total_marks": int(marks),
        "marking_points": [
            {
                "id": f"mp_{idx + 1}",
                "desc": f"{crit.get('criterion', 'Criterion')}: {crit.get('description', '')}".strip(": "),
                "marks": int(crit.get("marks", max(1, int(marks) // max(1, len(rubric))))),
                "target_concepts": [w for w in re.split(r"[,/;\s]+", f"{crit.get('criterion', '')} {crit.get('description', '')}") if len(w) > 3],
                "editable": True,
            }
            for idx, crit in enumerate(rubric)
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    return {
        "id": make_id(f"{prefix}_essay"),
        "question_type": "essay",
        "modality": "semantic",
        "solution_type": "rubric",
        "prompt": prompt,
        "rubric": list(rubric),
        "marking_schema": schema,
        "sample_answer": sample_answer,
        "expected_answer": sample_answer,
        "explanation": sample_answer,
        "marks": int(marks),
        "min_words": int(min_words),
        "max_words": int(max_words),
        "hint_trigger": hint_text,
        "hints": {
            "tier_1": hint or "Structure your essay with an Introduction, Body paragraphs, and a Conclusion.",
            "tier_2": "Use clear subheadings for each rubric criterion to maximize marks.",
            "tier_3": f"Key arguments: {sample_answer[:120]}..." if sample_answer else "Develop full explanatory sentences with practical business examples.",
        },
        "guidelines": list(guidelines or [f"Word range: {min_words}–{max_words} words.", "Structure: Introduction, Body, Conclusion."]),
        "visual_aid_key": visual_aid_key,
    }


def sample_pool(r: random.Random, pool: List[Dict[str, Any]], count: int) -> List[Dict[str, Any]]:
    """Pick `count` items from a pool of *factory callables or dicts*.

    Each pool entry is a zero-arg callable returning a fresh question dict
    (so ids/scenario shuffles differ per call). Sampling is without
    replacement when the pool is large enough, otherwise with replacement.
    """
    n = max(1, min(int(count or 1), 50))
    if not pool:
        return []
    if len(pool) >= n:
        chosen = r.sample(pool, n)
    else:
        chosen = [r.choice(pool) for _ in range(n)]
    return [item() if callable(item) else dict(item) for item in chosen]


# --- archetype derivation from already-authored content ---------------------

_BLANK_MARKERS = ("\u2026", "...", "_____")


def _eval_pool(pool: Optional[List[Any]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for f in (pool or []):
        try:
            out.append(f() if callable(f) else dict(f))
        except Exception:
            continue
    return out


def _derive_prefix(q: Dict[str, Any]) -> str:
    _id = str(q.get("id") or "g10")
    for tok in ("_mcq_", "_typed_", "_wb_", "_match_", "_cross_", "_essay_"):
        if tok in _id:
            return _id.split(tok)[0]
    return _id.rsplit("_", 1)[0] or "g10"


def _correct_option(q: Dict[str, Any]) -> Optional[str]:
    try:
        return q["options"][int(q["correct_index"])]
    except (KeyError, IndexError, ValueError, TypeError):
        return None


def _wb_kwargs(q: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    prompt = q.get("prompt", "")
    marker = next((m for m in _BLANK_MARKERS if m in prompt), None)
    if not marker:
        return None
    parts = prompt.split(marker)
    if len(parts) != 2:
        return None
    ans = _correct_option(q)
    if not ans or len(ans) > 30:
        return None
    return dict(
        prefix=_derive_prefix(q),
        prompt=prompt.replace(marker, " ______ "),
        pool=list(q["options"]),
        blanks=["1"],
        correct_map={"1": ans},
        text_parts=[parts[0].rstrip() + " ", " " + parts[1].strip()],
        explanation=q.get("explanation", ""),
        visual_aid_key=q.get("visual_aid_key"),
        guidelines=q.get("guidelines"),
    )


def _collect_pairs(concepts: List[Dict[str, Any]]) -> List[tuple]:
    """Extract (prompt, correct_answer, explanation) tuples from concept MCQs."""
    pairs: List[tuple] = []
    seen = set()
    for q in concepts:
        ans = _correct_option(q)
        p = q.get("prompt", "")
        if not ans or not p or ans in seen:
            continue
        seen.add(ans)
        pairs.append((p, ans, q.get("explanation", "")))
    return pairs


def _match_kwargs_list(concepts: List[Dict[str, Any]], prefix: str) -> List[Dict[str, Any]]:
    """Build several matching variants by sub-sampling the (prompt, answer) pairs.

    Entropy: each variant picks a different subset of pairs and shuffles the B
    column, so different seeds yield genuinely different matching questions.
    """
    pairs = _collect_pairs(concepts)
    pairs_ok = [(p, a) for p, a, _ in pairs if len(a) <= 28]
    if len(pairs_ok) < 3:
        return []
    import random
    sizes = [s for s in (4, 5, 6, 3) if s <= len(pairs_ok)]
    if not sizes:
        return []
    leads = [
        "Match each description in Column A with the correct term in Column B",
        "Pair each CAPS description with its defining term",
        "Match the following definitions to their terms",
        "Match each concept to the description that best fits",
    ]
    out: List[Dict[str, Any]] = []
    variants = max(6, min(10, len(pairs_ok)))
    for vi in range(variants):
        n = sizes[vi % len(sizes)]
        rr = random.Random(f"{prefix}|match|{vi}|{n}")
        chosen = rr.sample(pairs_ok, n)
        col_a = [p for p, _ in chosen]
        col_b_full = [a for _, a in chosen]
        col_b = list(col_b_full)
        rr.shuffle(col_b)
        correct_pairs = {p: a for p, a in chosen}
        lead = leads[vi % len(leads)]
        out.append(dict(
            prefix=prefix,
            prompt=f"{lead}. ({n} items)  Descriptions: " + ", ".join(p[:40] for p, _ in chosen),
            column_a=col_a,
            column_b=col_b,
            correct_pairs=correct_pairs,
            explanation="Match each CAPS description to its defining term.",
            marks=n,
        ))
    return out


def _cw_kwargs_list(concepts: List[Dict[str, Any]], prefix: str) -> List[Dict[str, Any]]:
    """Build several crossword variants by sub-sampling a single-token vocab.

    Preferred tokens are one-word answers (>=4 letters). If a topic's answers
    are mostly multi-word, fall back to the longest alphabetic word inside each
    answer so every topic still yields a real crossword instead of silently
    falling back to the mixed pool.
    """
    pairs = _collect_pairs(concepts)
    seen: set = set()
    vocab: List[tuple] = []

    def _add(token: str, clue: str) -> None:
        u = token.upper()
        if len(token) < 4 or not token.isalpha() or u in seen:
            return
        seen.add(u)
        vocab.append((u, clue))

    # Pass 1: pure single-word answers. Punctuation-only differences (HIV/AIDS,
    # Risk-taker) may be stripped, but a real space disqualifies the token --
    # stripping 'Counterfeiting/imitations' used to glue both words together
    # into an un-grid-able 23-letter monster.
    for p, ans, expl in pairs:
        a = ans.strip()
        if " " not in a and "/" not in a and "-" not in a:
            tok = re.sub(r"[^A-Za-z]", "", a)
            if tok.isalpha():
                _add(tok, expl or a)
        elif " " not in a:
            _add(max(re.split(r"[/\-]", a), key=len).strip(), expl or a)
    # Pass 2 (fallback): longest word inside multi-word answers.
    if len(vocab) < 6:
        for p, ans, expl in pairs:
            words = [w for w in re.findall(r"[A-Za-z]{4,}", ans)]
            if not words:
                continue
            _add(max(words, key=len), expl or ans)
    if len(vocab) < 4:
        return []
    import random
    sizes = [s for s in (6, 7, 5, 8) if s <= len(vocab)]
    if not sizes:
        return []
    leads = [
        "Crossword of key CAPS terms",
        "Fill in the business-studies vocabulary",
        "Crossword puzzle for this topic",
        "Complete the grid with the correct business terms",
    ]
    out: List[Dict[str, Any]] = []
    variants = max(4, min(8, len(vocab)))
    for vi in range(variants):
        n = sizes[vi % len(sizes)]
        rr = random.Random(f"{prefix}|cw|{vi}|{n}")
        chosen = rr.sample(vocab, n)
        words = [w for w, _ in chosen]
        clues = {w: c for w, c in chosen}
        grid = max(12, max(len(w) for w in words) + 2)
        lead = leads[vi % len(leads)]
        out.append(dict(
            prefix=prefix,
            prompt=f"{lead} ({n} words).",
            words=words,
            clues=clues,
            grid_size=grid,
            explanation="Each answer is a key term; the clue is its definition.",
            marks=n,
        ))
    return out


def _cw_kwargs(concepts: List[Dict[str, Any]], prefix: str) -> Optional[Dict[str, Any]]:
    lst = _cw_kwargs_list(concepts, prefix)
    return lst[0] if lst else None


def _essay_kwargs(q: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    mps = [m for m in (q.get("marking_points") or []) if m]
    if not mps:
        return None
    marks = int(q.get("marks") or len(mps))
    per = max(1, marks // len(mps))
    rubric = [{"criterion": f"Point {i + 1}", "description": mp, "marks": per} for i, mp in enumerate(mps)]
    rubric[-1]["marks"] += marks - sum(c["marks"] for c in rubric)
    sample = q.get("sample_answer") or q.get("explanation") or " ".join(mps)
    return dict(
        prefix=_derive_prefix(q),
        prompt=q["prompt"],
        rubric=rubric,
        sample_answer=sample,
        marks=marks,
        min_words=max(80, marks * 15),
        max_words=max(200, marks * 30),
        visual_aid_key=q.get("visual_aid_key"),
        guidelines=q.get("guidelines"),
    )


def _ensure_derived_pools(pools: Dict[str, List[Any]]) -> None:
    """Fill any missing rich-format pool by deriving it from core content."""
    if not any(k in pools and pools.get(k) for k in ("concepts", "discussion", "application")):
        return
    concepts = _eval_pool(pools.get("concepts"))
    prefix = _derive_prefix(concepts[0]) if concepts else "g10"
    typed = [q for q in _eval_pool(pools.get("discussion")) + _eval_pool(pools.get("application"))
             if q.get("question_type") == "typed" and q.get("marking_points")]

    if not pools.get("word_bank"):
        facs = [lambda kw=kw: make_wordbank(**kw) for q in concepts for kw in [_wb_kwargs(q)] if kw]
        if facs:
            pools["word_bank"] = facs
    if not pools.get("matching"):
        facs = [lambda kw=kw: make_matching(**kw) for kw in _match_kwargs_list(concepts, prefix)]
        if facs:
            pools["matching"] = facs
    if not pools.get("crossword"):
        kws = _cw_kwargs_list(concepts, prefix)
        if kws:
            pools["crossword"] = [lambda kw=kw: make_crossword(**kw) for kw in kws]
    if not pools.get("essay"):
        facs = [lambda kw=kw: make_essay(**kw) for q in typed for kw in [_essay_kwargs(q)] if kw]
        if facs:
            pools["essay"] = facs


def _harvest_pools(pools: Dict[str, List[Any]], topic_key: str) -> None:
    """Append authentic exam questions harvested from the curriculum .md docs.

    Typed drills join the discussion pool; MCQ blocks are converted to the
    raw G10 concept-dict shape and joined to concepts. Fully deterministic
    (pure file parsing, cached) and silently no-ops when no doc matches.
    """
    try:
        from ..bs_docs_harvester import harvest_items
        grade = int(str(topic_key)[5:7])
        items = harvest_items(grade, topic_key)
    except Exception:
        return
    prefix = str(topic_key)
    for it in items:
        if it.get("kind") == "mcq":
            opts = list(it["options"])
            try:
                ci = int(it["correct_index"])
                assert 0 <= ci < len(opts)
            except (KeyError, ValueError, TypeError, AssertionError):
                continue
            raw = {
                "id": make_id(f"{prefix}_mcq"),
                "question_type": "mcq",
                "prompt": it["prompt"],
                "options": opts,
                "correct_index": str(ci),
                "explanation": it.get("explanation", ""),
                "marks": int(it.get("marks", 1) or 1),
            }
            pools.setdefault("concepts", []).append(lambda q=raw: dict(q))
        else:
            mps = list(it.get("marking_points") or [])
            if not mps:
                continue
            raw = make_typed(
                prefix=prefix,
                prompt=it["prompt"],
                marking_points=mps,
                sample_answer=it.get("sample_answer", ""),
                marks=it.get("marks"),
                guidelines=it.get("guidelines"),
            )
            pools.setdefault("discussion", []).append(lambda q=raw: dict(q))


def build_generate(pools_builder):
    """Return a `generate(subskill, difficulty, count, seed=None, **kw)` function.

    `pools_builder(r)` must return a dict mapping subskill-key -> list of
    factory callables. A 'mixed' key is auto-derived from the union if absent.

    If a topic declares only the core pools (concepts / application /
    discussion) the richer formats (word_bank / matching / crossword / essay)
    are DERIVED from that already-grounded CAPS content so the topic still
    serves every archetype instead of silently falling back to MCQ. Topics that
    hand-author these pools (see market/macro/business-sectors) are left as-is.
    """

    def generate(subskill: str = "concepts", difficulty: str = "medium", count: int = 1, seed: Optional[int] = None, **_kw) -> List[Dict[str, Any]]:
        r = rng(seed)
        pools = pools_builder(r)
        topic_key = str(_kw.get("topic") or _kw.get("topic_key") or "")
        if topic_key.startswith("grade1") and "_bs_" in topic_key:
            _harvest_pools(pools, topic_key)
        _ensure_derived_pools(pools)
        if "mixed" not in pools:
            union: List[Any] = []
            for key, items in pools.items():
                union.extend(items)
            pools["mixed"] = union
        key = str(subskill or "concepts").strip().lower()
        pool = pools.get(key) or pools.get("mixed") or []
        return sample_pool(r, pool, count)

    return generate
