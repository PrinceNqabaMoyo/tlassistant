"""Authoring-quality gate for Business Studies generators.

Catches the mistakes that a plain py_compile check hides (stale __pycache__) and
that only show up at request time:
  * real syntax errors
  * pools that raise when a question is built (NameError, KeyError, ...)
  * word_bank payloads whose text_parts count does not match the blanks
  * unresolved format placeholders left in visible text
  * mojibake / stray characters in visible text
  * duplicated prompts inside one pool (padding masquerading as content)

Usage:  python scripts/bs_quality_gate.py grade10 [topic_key ...]
"""
import sys
import os
import re
import ast
import collections

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'caps-ai-backend'))

from app.api import grade10_business_studies as g10
from app.api import grade11_business_studies as g11
from app.api import grade12_business_studies as g12

MODULES = {'grade10': g10, 'grade11': g11, 'grade12': g12}
SUBSKILLS = ['concepts', 'application', 'discussion', 'word_bank', 'matching',
             'crossword', 'essay']
# requested subskill -> question_type the generator MUST return (guards against
# a pool silently falling back to MCQ, which fakes coverage in the counts)
EXPECTED_TYPE = {
    'concepts': 'mcq',
    'word_bank': 'word_bank',
    'matching': 'matching_columns',
    'crossword': 'crossword',
    'essay': 'essay',
}

TEXT_FIELDS = ['prompt', 'explanation', 'sample_answer', 'expected_answer', 'hint_trigger']
LIST_FIELDS = ['options', 'marking_points', 'word_bank', 'column_a', 'column_b', 'guidelines']

# characters that should never appear in authored South-African English text
MOJIBAKE = re.compile(r'[\u0400-\u04FF\u4e00-\u9fff\u3040-\u30ff\u0600-\u06ff]')
PLACEHOLDER = re.compile(r'\{[a-zA-Z_][a-zA-Z0-9_]*\}|\[\s*TBD\s*\]|TODO|XXX|FIXME')


def scan_text(value, where, problems):
    if not isinstance(value, str):
        return
    if MOJIBAKE.search(value):
        bad = sorted({c for c in value if MOJIBAKE.match(c)})
        problems.append(f'{where}: mojibake {bad} in {value[:60]!r}')
    if PLACEHOLDER.search(value):
        problems.append(f'{where}: unresolved placeholder in {value[:70]!r}')
    if '  ' in value and '   ' in value:
        problems.append(f'{where}: triple space (likely missing join) in {value[:60]!r}')


def _qsig(q):
    """Content signature so entropy variants (same prompt, different options /
    pairs / words / marking-point subsets) count as distinct authored questions."""
    t = q.get('question_type')
    p = q.get('prompt', '')
    if t == 'mcq':
        return ('mcq', p, tuple(q.get('options') or []), q.get('correct_index'))
    if t == 'word_bank':
        return ('wb', p, tuple(sorted((q.get('correct_map') or {}).items())))
    if t == 'matching_columns':
        return ('match', p, tuple(sorted((q.get('correct_pairs') or {}).items())))
    if t == 'crossword':
        return ('cw', p, tuple(q.get('words') or []))
    if t == 'typed':
        return ('typed', p, tuple(q.get('marking_points') or []), q.get('marks'))
    if t == 'essay':
        return ('essay', p, tuple((c.get('description'), c.get('marks')) for c in (q.get('rubric') or [])))
    return (t, p)


def check_topic(topic, fn, problems):
    gen = fn if (callable(fn) and not hasattr(fn, 'generate')) else fn.generate
    counts = {}
    for sk in SUBSKILLS:
        try:
            qs = gen(subskill=sk, difficulty='medium', count=200, seed=42, topic=topic)
        except Exception as exc:
            problems.append(f'{topic}/{sk}: RAISES {type(exc).__name__}: {exc}')
            continue
        counts[sk] = len({_qsig(q) for q in qs})
        exp = EXPECTED_TYPE.get(sk)
        if exp and qs:
            wrong = [q.get('question_type') for q in qs if q.get('question_type') != exp]
            if wrong:
                problems.append(
                    f'{topic}/{sk}: FALLBACK - requested {sk} but got '
                    f'{dict(collections.Counter(wrong))} (expected {exp})')
        for n, q in enumerate(qs):
            where = f'{topic}/{sk}#{n}({q.get("question_type")})'
            for f in TEXT_FIELDS:
                scan_text(q.get(f), where + '.' + f, problems)
            for f in LIST_FIELDS:
                for i, v in enumerate(q.get(f) or []):
                    scan_text(v, f'{where}.{f}[{i}]', problems)
            if q.get('question_type') == 'word_bank':
                nb, np_ = len(q.get('blanks') or []), len(q.get('text_parts') or [])
                if np_ != nb + 1:
                    problems.append(f'{where}: text_parts={np_} but blanks={nb} (need {nb + 1})')
                answers = (q.get('correct_map') or {}).values()
                bank = q.get('word_bank') or []
                for a in answers:
                    if a not in bank:
                        problems.append(f'{where}: answer {a!r} not in word bank')
            if q.get('question_type') == 'mcq':
                opts = q.get('options') or []
                try:
                    ci = int(q.get('correct_index'))
                except (TypeError, ValueError):
                    problems.append(f'{where}: correct_index not an int')
                    continue
                if not (0 <= ci < len(opts)):
                    problems.append(f'{where}: correct_index {ci} out of range ({len(opts)} options)')
                if len(opts) != len(set(opts)):
                    problems.append(f'{where}: duplicate options')
            if q.get('question_type') == 'matching_columns':
                a, b = q.get('column_a') or [], q.get('column_b') or []
                pairs = q.get('correct_pairs') or {}
                if len(a) != len(set(a)) or len(b) != len(set(b)):
                    problems.append(f'{where}: duplicate column entries create ambiguous pairs')
                for k, v in pairs.items():
                    if k not in a:
                        problems.append(f'{where}: pair key {k!r} not in column_a')
                    if v not in b:
                        problems.append(f'{where}: pair value {v!r} not in column_b')
            if q.get('question_type') == 'crossword':
                words = q.get('words') or []
                clues = q.get('clues') or {}
                for w in words:
                    if w not in clues:
                        problems.append(f'{where}: word {w!r} has no clue')
                size = q.get('grid_size') or 0
                longest = max((len(w) for w in words), default=0)
                if longest > size:
                    problems.append(f'{where}: word of {longest} letters exceeds grid_size {size}')
            if q.get('question_type') == 'essay':
                total = sum(int(c.get('marks', 0)) for c in q.get('rubric') or [])
                if total != int(q.get('marks', 0)):
                    problems.append(f'{where}: rubric marks sum {total} != question marks {q.get("marks")}')
    return counts


def main():
    grade = sys.argv[1]
    gens = MODULES[grade].GENERATORS
    wanted = sys.argv[2:] or list(gens)
    failing = []
    for topic in wanted:
        if topic not in gens:
            print(f'{topic}: NOT REGISTERED')
            failing.append(topic)
            continue
        problems = []
        counts = check_topic(topic, gens[topic], problems)
        total = sum(counts.values())
        status = 'OK  ' if not problems and not counts.get('_') else 'FAIL'
        print(f'{status} {topic}  total_authored={total}  {counts}')
        for p in problems:
            print('      !', p)
        if problems:
            failing.append(topic)
    print(f'\n{len(failing)} topic(s) with problems: {failing or "none"}')
    return 1 if failing else 0


sys.exit(main())
