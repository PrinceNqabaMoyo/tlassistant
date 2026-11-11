"""Deterministic semantic-entropy expanders for Business Studies generators.

For a semantic subject, entropy cannot come from re-rolling numbers. It comes
from combinatorics over an already-grounded content base:

    mcq        - rotate distractor subsets and correct-answer position
    matching   - sub-sample term/definition pairs and shuffle column B
    crossword  - sub-sample a single-token vocabulary pool
    word_bank  - sub-sample term-blank sentences and shuffle the pool
    typed      - rotate marking-point emphasis and vary the command verb
    essay      - vary the command verb and the framing sentence

Each variant is deterministic (seeded from a stable hash of the fact content +
variant index), so the SAME fact base yields the SAME set of variant questions
across processes and runs. `sample_pool` in `_bs_common` then draws without
replacement from the enlarged pool, so different top-level seeds show different
variants.

The public entry point is `expand_fact_base(...)`. A generator builds a compact
fact base (list of dicts) and hands it to `expand_fact_base` to obtain the six
pool lists expected by `build_generate`.
"""
from __future__ import annotations

import hashlib
import re
from typing import Any, Callable, Dict, Iterable, List, Optional

from ._bs_common import (
    make_crossword,
    make_essay,
    make_matching,
    make_mcq,
    make_typed,
    make_wordbank,
)


# ---------------------------------------------------------------------------
# Stable per-fact random helpers.
# ---------------------------------------------------------------------------

def _stable_rng(*parts: Any) -> Any:
    """Deterministic `random.Random` seeded from a stable hash of the inputs.

    Uses SHA-256 over the joined string so results are identical across runs
    and Python versions (unlike `hash()` which is salted).
    """
    import random
    key = "|".join(str(p) for p in parts)
    h = int.from_bytes(hashlib.sha256(key.encode("utf-8")).digest(), "big")
    return random.Random(h)


def _shuffled(seq: List[Any], *parts: Any) -> List[Any]:
    r = _stable_rng(*parts)
    out = list(seq)
    r.shuffle(out)
    return out


def _subset(seq: List[Any], k: int, *parts: Any) -> List[Any]:
    """Deterministic size-k subset sampled without replacement."""
    if k >= len(seq):
        return list(seq)
    r = _stable_rng(*parts)
    return r.sample(list(seq), k)


# ---------------------------------------------------------------------------
# MCQ expansion.
#
# fact = {
#   "stem": "A group of two or more people ... is called a …",
#   "correct": "team",
#   "distractors": ["competitor", "supplier", "auditor", "manager", "customer"],
#   "explanation": "A team consists of two or more people ...",
# }
# ---------------------------------------------------------------------------

def expand_mcq_variants(prefix: str, vaid: str, facts: List[Dict[str, Any]],
                        variants_per_fact: int = 6, option_count: int = 4) -> List[Callable[[], Dict[str, Any]]]:
    out: List[Callable[[], Dict[str, Any]]] = []
    for fi, fact in enumerate(facts):
        stem = fact["stem"]
        correct = fact["correct"]
        distractors = list(fact.get("distractors") or [])
        expl = fact.get("explanation", "")
        if not distractors:
            # Fallback: single-item "MCQ" is degenerate; skip entropy here.
            kw = dict(prefix=prefix, prompt=stem, options=[correct],
                      correct_index=0, explanation=expl, visual_aid_key=vaid)
            out.append(lambda kw=kw: make_mcq(**kw))
            continue
        n_distract = max(1, option_count - 1)
        for vi in range(variants_per_fact):
            picked = _subset(distractors, n_distract, prefix, fi, vi, "d")
            opts = _shuffled([correct] + picked, prefix, fi, vi, "o")
            ci = opts.index(correct)
            kw = dict(prefix=prefix, prompt=stem, options=opts,
                      correct_index=ci, explanation=expl, visual_aid_key=vaid)
            out.append(lambda kw=kw: make_mcq(**kw))
    return out


# ---------------------------------------------------------------------------
# Matching-columns expansion.
#
# pairs = [ {"term": "Prejudice", "defn": "A preconceived opinion ..."}, ... ]
# ---------------------------------------------------------------------------

_MATCH_LEADS = [
    "Match each term in Column A with its correct definition in Column B",
    "Match the following CAPS terms to their definitions",
    "Pair each concept with its meaning",
    "Match the terms to the correct definitions",
]


def expand_matching_variants(prefix: str, vaid: str, pairs: List[Dict[str, str]],
                             variants: int = 6,
                             size_options: Optional[List[int]] = None) -> List[Callable[[], Dict[str, Any]]]:
    out: List[Callable[[], Dict[str, Any]]] = []
    sizes = [s for s in (size_options or [5, 6, 4]) if 2 <= s <= len(pairs)]
    if not sizes:
        return out
    for vi in range(variants):
        n = sizes[vi % len(sizes)]
        chosen = _subset(pairs, n, prefix, vi, "mpick", n)
        col_a = [p["term"] for p in chosen]
        col_b_full = [p["defn"] for p in chosen]
        col_b = _shuffled(col_b_full, prefix, vi, "b", n)
        correct_pairs = {p["term"]: p["defn"] for p in chosen}
        lead = _MATCH_LEADS[vi % len(_MATCH_LEADS)]
        prompt = f"{lead}. ({n} items)  Terms: " + ", ".join(col_a)
        kw = dict(
            prefix=prefix,
            prompt=prompt,
            column_a=col_a,
            column_b=col_b,
            correct_pairs=correct_pairs,
            explanation="Each definition is the CAPS meaning of the matching term.",
            marks=n,
            visual_aid_key=vaid,
        )
        out.append(lambda kw=kw: make_matching(**kw))
    return out


# ---------------------------------------------------------------------------
# Crossword expansion from a term/definition vocabulary pool.
# ---------------------------------------------------------------------------

def _is_crossword_token(term: str) -> bool:
    token = re.sub(r"[^A-Za-z]", "", term)
    return token.isalpha() and len(token) >= 4 and len(token) <= 14 and " " not in term.strip()


_CW_LEADS = [
    "Crossword of key CAPS terms",
    "Fill in the business-studies vocabulary",
    "Crossword puzzle for this topic",
    "Complete the grid with the correct business terms",
]


def expand_crossword_variants(prefix: str, vaid: str, pairs: List[Dict[str, str]],
                              variants: int = 5,
                              size_options: Optional[List[int]] = None) -> List[Callable[[], Dict[str, Any]]]:
    vocab = [p for p in pairs if _is_crossword_token(p["term"])]
    if len(vocab) < 4:
        return []
    out: List[Callable[[], Dict[str, Any]]] = []
    sizes = [s for s in (size_options or [6, 7, 5]) if 4 <= s <= len(vocab)]
    if not sizes:
        return []
    for vi in range(variants):
        n = sizes[vi % len(sizes)]
        chosen = _subset(vocab, n, prefix, vi, "cw", n)
        words = [re.sub(r"[^A-Za-z]", "", p["term"]).upper() for p in chosen]
        clues = {w: p["defn"] for w, p in zip(words, chosen)}
        grid = max(12, max(len(w) for w in words) + 2)
        lead = _CW_LEADS[vi % len(_CW_LEADS)]
        prompt = f"{lead} ({n} words)."
        kw = dict(
            prefix=prefix,
            prompt=prompt,
            words=words,
            clues=clues,
            grid_size=grid,
            explanation="Each answer is a key CAPS term; the clue is its definition.",
            marks=n,
            visual_aid_key=vaid,
        )
        out.append(lambda kw=kw: make_crossword(**kw))
    return out


# ---------------------------------------------------------------------------
# Word-bank expansion.
# Each pair becomes a fill-in "The <defn> is called a <term>." sentence; a
# variant blanks out `size` of them and offers `size + noise` terms as pool.
# ---------------------------------------------------------------------------

def expand_wordbank_variants(prefix: str, vaid: str, pairs: List[Dict[str, str]],
                             variants: int = 5,
                             size_options: Optional[List[int]] = None,
                             size: int = 4,
                             noise: int = 1) -> List[Callable[[], Dict[str, Any]]]:
    usable = [p for p in pairs if p.get("term") and p.get("defn")]
    if not usable:
        return []
    sizes = [s for s in (size_options or [size, size + 1, max(2, size - 1)]) if 2 <= s <= len(usable)]
    if not sizes:
        return []
    out: List[Callable[[], Dict[str, Any]]] = []
    for vi in range(variants):
        sz = sizes[vi % len(sizes)]
        chosen = _subset(usable, sz, prefix, vi, "wbk", sz)
        # Extra distractor terms not among the blanks (must exist in vocabulary).
        rest = [p for p in usable if p not in chosen]
        extra = _subset(rest, noise, prefix, vi, "wbx", noise) if len(rest) >= noise else []
        pool_terms = [p["term"] for p in chosen] + [p["term"] for p in extra]
        pool = _shuffled(pool_terms, prefix, vi, "wbp")
        blanks = [f"b{i + 1}" for i in range(len(chosen))]
        correct_map = {blanks[i]: p["term"] for i, p in enumerate(chosen)}
        text_parts: List[str] = []
        for i, p in enumerate(chosen):
            text_parts.append(f"{p['defn'].rstrip('.')} is called a")
        text_parts.append(".")
        prompt = "Fill each blank with the correct term:\n" + "\n".join(
            f"{i + 1}. {p['defn']}  ->  ______" for i, p in enumerate(chosen)
        )
        kw = dict(
            prefix=prefix,
            prompt=prompt,
            pool=pool,
            blanks=blanks,
            correct_map=correct_map,
            text_parts=text_parts,
            explanation="Match each definition to its CAPS term from the word bank.",
            marks=len(chosen),
            visual_aid_key=vaid,
        )
        out.append(lambda kw=kw: make_wordbank(**kw))
    return out


# ---------------------------------------------------------------------------
# Typed / discussion expansion.
#
# spec = {
#   "base": "the importance of setting goals",       # topic phrase
#   "marking_points": [...],                        # all points (memo answers)
#   "marks": int,                                   # total marks when asking full set
#   "min_ask": int,                                 # smallest subset to request
# }
# Variants rotate (a) the command verb, (b) which N-of-M subset the learner is
# asked to produce (memo keeps the FULL marking_points so any accepted subset
# scores correctly).
# ---------------------------------------------------------------------------

_VERBS = ["Explain", "Describe", "Discuss", "Outline", "Suggest", "Recommend"]


def expand_typed_variants(prefix: str, vaid: str, specs: List[Dict[str, Any]],
                          variants: int = 3) -> List[Callable[[], Dict[str, Any]]]:
    out: List[Callable[[], Dict[str, Any]]] = []
    for si, spec in enumerate(specs):
        base = spec.get("base", "").strip()
        all_mps = list(spec.get("marking_points") or [])
        full_marks = int(spec.get("marks") or len(all_mps))
        sample = spec.get("sample_answer") or " ".join(all_mps)
        if not all_mps or not base:
            continue
        m = len(all_mps)
        min_ask = int(spec.get("min_ask") or max(2, min(3, m)))
        max_ask = int(spec.get("max_ask") or m)
        for vi in range(variants):
            r = _stable_rng(prefix, si, vi, "tv")
            verb = _VERBS[r.randrange(len(_VERBS))]
            n = max_ask if max_ask >= m else r.randint(min_ask, min(max_ask, m))
            rotated = _shuffled(all_mps, prefix, si, vi, "rot")
            asked = rotated[:n]
            # Marks scale linearly with the number of points asked.
            marks = max(1, int(round(full_marks * (n / m))))
            kw = dict(
                prefix=prefix,
                prompt=f"{verb} {n} {base}. ({marks})",
                marking_points=asked,
                sample_answer=sample,
                marks=marks,
                visual_aid_key=vaid,
            )
            out.append(lambda kw=kw: make_typed(**kw))
    return out


# ---------------------------------------------------------------------------
# Essay expansion. Same rubric; rotate the framing command.
#
# spec = {
#   "topic": "'Teamwork is essential for achieving business objectives.'",
#   "ask":   "Discuss this statement, referring to X, Y and Z.",
#   "rubric": [...], "sample_answer": str, "marks": int,
#   "min_words": int, "max_words": int,
# }
# ---------------------------------------------------------------------------

_ESSAY_LEADS = [
    "Discuss this statement",
    "Argue for or against this view",
    "Critically evaluate this statement",
    "To what extent do you agree with this statement? Justify your answer",
    "Explain why this statement is true in the modern workplace",
]


def expand_essay_variants(prefix: str, vaid: str, specs: List[Dict[str, Any]],
                          variants: int = 3) -> List[Callable[[], Dict[str, Any]]]:
    out: List[Callable[[], Dict[str, Any]]] = []
    for si, spec in enumerate(specs):
        for vi in range(variants):
            lead = _ESSAY_LEADS[(si + vi) % len(_ESSAY_LEADS)]
            prompt = f"{spec['topic']} {lead}, {spec['ask']}."
            kw = dict(
                prefix=prefix,
                prompt=prompt,
                rubric=list(spec["rubric"]),
                sample_answer=spec["sample_answer"],
                marks=int(spec.get("marks", 20)),
                min_words=int(spec.get("min_words", 180)),
                max_words=int(spec.get("max_words", 450)),
                visual_aid_key=vaid,
            )
            out.append(lambda kw=kw: make_essay(**kw))
    return out


# ---------------------------------------------------------------------------
# One-stop wrapper.
# ---------------------------------------------------------------------------

def expand_fact_base(prefix: str, vaid: str,
                     mcq_facts: Optional[Iterable[Dict[str, Any]]] = None,
                     pairs: Optional[Iterable[Dict[str, str]]] = None,
                     typed_specs: Optional[Iterable[Dict[str, Any]]] = None,
                     essay_specs: Optional[Iterable[Dict[str, Any]]] = None,
                     mcq_variants: int = 6,
                     matching_variants: int = 6,
                     matching_sizes: Optional[List[int]] = None,
                     crossword_variants: int = 5,
                     crossword_sizes: Optional[List[int]] = None,
                     wordbank_variants: int = 5,
                     wordbank_sizes: Optional[List[int]] = None,
                     typed_variants: int = 3,
                     essay_variants: int = 3) -> Dict[str, List[Callable[[], Dict[str, Any]]]]:
    mcq_facts = list(mcq_facts or [])
    pairs = list(pairs or [])
    typed_specs = list(typed_specs or [])
    essay_specs = list(essay_specs or [])
    return {
        "concepts": expand_mcq_variants(prefix, vaid, mcq_facts, variants_per_fact=mcq_variants),
        "application": [],
        "discussion": expand_typed_variants(prefix, vaid, typed_specs, variants=typed_variants),
        "word_bank": expand_wordbank_variants(prefix, vaid, pairs, variants=wordbank_variants, size_options=wordbank_sizes),
        "matching": expand_matching_variants(prefix, vaid, pairs, variants=matching_variants, size_options=matching_sizes),
        "crossword": expand_crossword_variants(prefix, vaid, pairs, variants=crossword_variants, size_options=crossword_sizes),
        "essay": expand_essay_variants(prefix, vaid, essay_specs, variants=essay_variants),
    }
