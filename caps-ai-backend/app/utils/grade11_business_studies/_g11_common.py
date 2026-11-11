"""Shared deterministic helpers for Grade 11 Business Studies generators.

Mirrors the structure of the hand-built reference generators
(`term_1/influences_on_business_environments_generator.py` and
`term_1/the_challenges_of_the_business_environments_generator.py`) so every new
topic generator emits the same rich, adaptive-ready question shape:

- seeded RNG (deterministic; same seed => identical questions)
- per-question metadata (learning_objective_id, concept_id, concept_group,
  question_family_id, retry_variant, misconception_tags, diagnostic_tags,
  minimum_mastery_score) used by the Standard/Pro adaptive progression layer
- 3-section scaffold hints (`hint_sections`) per the hint system
- keyword-based mastery support for typed answers (`keywords`)

A topic generator only declares its content pools and a small `TopicMeta`, then
exports `generate = make_generate(meta, concept_pool, application_pool,
discussion_pool)`.
"""
from __future__ import annotations

import random
import re
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Sequence


@dataclass(frozen=True)
class TopicMeta:
    topic_id: str
    subtopic_id: str
    curriculum_reference: str
    id_prefix: str  # e.g. "g11_bs_mkt" -> ids like g11_bs_mkt_mcq_123


FILTERABLE_METADATA_KEYS = (
    'learning_objective_id',
    'concept_id',
    'concept_group',
    'question_family_id',
    'scenario_family_id',
)


def rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed)


def select_items(r: random.Random, pool: Sequence[Any], count: int, difficulty: str, seed: Optional[int] = None) -> List[Any]:
    """Deterministically select `count` items, filtered by difficulty band."""
    filtered = [item for item in pool if difficulty in _difficulties(item)]
    working = filtered or list(pool)
    if not working:
        return []
    if count == 1 and len(working) > 1:
        if seed is not None:
            offset = int(seed) % len(working)
        else:
            offset = r.randint(0, len(working) - 1)
        return [working[offset]]
    if count <= len(working):
        shuffled = list(working)
        r.shuffle(shuffled)
        return shuffled[:count]
    result = working[:]
    r.shuffle(result)
    while len(result) < count:
        result.append(r.choice(working))
    return result[:count]


def _difficulties(item: Any) -> Sequence[str]:
    if isinstance(item, tuple):
        item = item[1]
    return item.get('difficulties', ['easy', 'medium', 'hard'])


def with_metadata(
    item: Dict[str, Any],
    *,
    subskill: str,
    learning_objective_id: str,
    question_family_id: str,
    concept_id: Optional[str] = None,
    concept_group: Optional[str] = None,
    scenario_family_id: Optional[str] = None,
    retry_variant: str = 'core',
    misconception_tags: Optional[List[str]] = None,
    diagnostic_tags: Optional[List[str]] = None,
    answer_structure_tags: Optional[List[str]] = None,
    minimum_mastery_score: Optional[float] = None,
) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        'subskill': subskill,
        'learning_objective_id': learning_objective_id,
        'concept_id': concept_id,
        'concept_group': concept_group,
        'question_family_id': question_family_id,
        'scenario_family_id': scenario_family_id,
        'retry_variant': retry_variant,
        'difficulty_band': item.get('difficulty_band', item.get('difficulties', ['easy', 'medium', 'hard'])),
        'misconception_tags': misconception_tags or [],
        'diagnostic_tags': diagnostic_tags or [],
        'answer_structure_tags': answer_structure_tags or [],
    })
    if minimum_mastery_score is not None:
        enriched['minimum_mastery_score'] = minimum_mastery_score
    return enriched


def _matches_metadata(item: Dict[str, Any], filters: Dict[str, Any]) -> bool:
    for key, value in filters.items():
        if value is None:
            continue
        if item.get(key) != value:
            return False
    return True


def apply_metadata_filters(pool: List[Dict[str, Any]], **kwargs) -> List[Dict[str, Any]]:
    base_filters = {
        key: kwargs.get(key)
        for key in FILTERABLE_METADATA_KEYS
        if kwargs.get(key) is not None
    }
    retry_variant = kwargs.get('retry_variant')

    if not base_filters and retry_variant is None:
        return pool

    exact_filters = dict(base_filters)
    if retry_variant is not None:
        exact_filters['retry_variant'] = retry_variant

    exact_matches = [item for item in pool if _matches_metadata(item, exact_filters)]
    if exact_matches:
        return exact_matches

    family_line_matches = [item for item in pool if _matches_metadata(item, base_filters)]
    if family_line_matches:
        return family_line_matches

    broadened_filters = {
        key: value
        for key, value in base_filters.items()
        if key in ('learning_objective_id', 'concept_id', 'concept_group')
    }
    if retry_variant is not None and broadened_filters:
        broadened_variant_matches = [
            item for item in pool
            if _matches_metadata(item, {**broadened_filters, 'retry_variant': retry_variant})
        ]
        if broadened_variant_matches:
            return broadened_variant_matches

    if broadened_filters:
        broadened_matches = [item for item in pool if _matches_metadata(item, broadened_filters)]
        if broadened_matches:
            return broadened_matches

    return pool


def make_mcq_question(meta: TopicMeta, r: random.Random, item: Dict[str, Any]) -> Dict[str, Any]:
    correct_option = item['options'][int(item['correct_index'])]
    return {
        'id': f"{meta.id_prefix}_mcq_{r.randint(1000, 999999)}",
        'title': item.get('title', 'Concept check'),
        'question_type': 'mcq',
        'prompt': item['prompt'],
        'options': item['options'],
        'correct_index': str(item['correct_index']),
        'explanation': item['explanation'],
        'marks': 1,
        'hint_sections': item.get('hint_sections', []),
        'guidelines': item.get('guidelines', []),
        'sample_answer': correct_option,
        'ideal_answer': correct_option,
        'marking_points': [correct_option],
        'teaching_note': item.get('teaching_note', item['explanation']),
        'topic_id': meta.topic_id,
        'subtopic_id': meta.subtopic_id,
        'subskill': item.get('subskill'),
        'learning_objective_id': item.get('learning_objective_id'),
        'concept_id': item.get('concept_id'),
        'concept_group': item.get('concept_group'),
        'question_family_id': item.get('question_family_id'),
        'scenario_family_id': item.get('scenario_family_id'),
        'retry_variant': item.get('retry_variant', 'core'),
        'difficulty_band': item.get('difficulty_band', item.get('difficulties', ['easy', 'medium', 'hard'])),
        'curriculum_reference': item.get('curriculum_reference', meta.curriculum_reference),
        'misconception_tags': item.get('misconception_tags', []),
        'diagnostic_tags': item.get('diagnostic_tags', []),
        'answer_structure_tags': item.get('answer_structure_tags', []),
        'minimum_mastery_score': item.get('minimum_mastery_score', 1.0),
    }


def make_typed_question(meta: TopicMeta, r: random.Random, item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'id': f"{meta.id_prefix}_typed_{r.randint(1000, 999999)}",
        'title': item.get('title', 'Written response'),
        'question_type': 'typed',
        'prompt': item['prompt'],
        'marks': item['marks'],
        'marking_points': item['marking_points'],
        'sample_answer': item['sample_answer'],
        'ideal_answer': item.get('ideal_answer', item['sample_answer']),
        'hint_sections': item.get('hint_sections', []),
        'answer_part_hints': item.get('answer_part_hints', []),
        'guidelines': item.get('guidelines', []),
        'teaching_note': item.get('teaching_note', ''),
        'keywords': item.get('keywords', []),
        'topic_id': meta.topic_id,
        'subtopic_id': meta.subtopic_id,
        'subskill': item.get('subskill'),
        'learning_objective_id': item.get('learning_objective_id'),
        'concept_id': item.get('concept_id'),
        'concept_group': item.get('concept_group'),
        'question_family_id': item.get('question_family_id'),
        'scenario_family_id': item.get('scenario_family_id'),
        'retry_variant': item.get('retry_variant', 'core'),
        'difficulty_band': item.get('difficulty_band', item.get('difficulties', ['easy', 'medium', 'hard'])),
        'curriculum_reference': item.get('curriculum_reference', meta.curriculum_reference),
        'misconception_tags': item.get('misconception_tags', []),
        'diagnostic_tags': item.get('diagnostic_tags', []),
        'answer_structure_tags': item.get('answer_structure_tags', []),
        'minimum_mastery_score': item.get('minimum_mastery_score', 0.6),
    }


def hint_sections(testing: str, reasoning: str, transfer: str) -> List[Dict[str, str]]:
    """Build the standard 3-section scaffold hint block."""
    return [
        {'title': 'What is being tested?', 'text': testing},
        {'title': 'Reasoning path', 'text': reasoning},
        {'title': 'Transfer idea', 'text': transfer},
    ]


# Pool builders are callables so per-call randomness (e.g. scenario names) stays
# deterministic under the same seed.
PoolBuilder = Callable[[random.Random], List[Dict[str, Any]]]


def _normalise_text_parts(text_parts: Optional[List[str]], blanks: List[str], prompt: str) -> List[str]:
    """Coerce authored segments into the WordBankQuestionUI shape.

    The UI renders ``parts[i]`` then blank ``blanks[i]`` for every non-final
    element, so ``text_parts`` MUST be exactly ``len(blanks) + 1`` long. Fold
    any extra authored separator segments forward to avoid phantom blanks.
    """
    parts = list(text_parts) if text_parts else [prompt] + [""] * len(blanks)
    want = len(blanks) + 1
    if len(parts) == want:
        return parts
    n = len(blanks)
    if n and len(parts) in (2 * n, 2 * n + 1):
        merged: List[str] = [parts[0]]
        for i in range(1, 2 * n - 1, 2):
            merged.append(parts[i] + parts[i + 1])
        merged.append("".join(parts[2 * n - 1:]))
        if len(merged) == want:
            return merged
    if len(parts) > want:
        return parts[: want - 1] + ["".join(parts[want - 1:])]
    return parts + [""] * (want - len(parts))


def _with_meta(meta: TopicMeta, item: Dict[str, Any], subskill: str) -> Dict[str, Any]:
    """Attach the standard adaptive metadata every G11/G12 question carries."""
    return {
        'topic_id': meta.topic_id,
        'subtopic_id': meta.subtopic_id,
        'subskill': item.get('subskill', subskill),
        'learning_objective_id': item.get('learning_objective_id'),
        'concept_id': item.get('concept_id'),
        'concept_group': item.get('concept_group'),
        'question_family_id': item.get('question_family_id'),
        'scenario_family_id': item.get('scenario_family_id'),
        'retry_variant': item.get('retry_variant', 'core'),
        'difficulty_band': item.get('difficulty_band', item.get('difficulties', ['easy', 'medium', 'hard'])),
        'curriculum_reference': item.get('curriculum_reference', meta.curriculum_reference),
        'misconception_tags': item.get('misconception_tags', []),
        'diagnostic_tags': item.get('diagnostic_tags', []),
        'answer_structure_tags': item.get('answer_structure_tags', []),
        'hint_sections': item.get('hint_sections', []),
        'guidelines': item.get('guidelines', []),
    }


def make_wordbank_question(meta: TopicMeta, r: random.Random, item: Dict[str, Any]) -> Dict[str, Any]:
    blanks = [str(b) for b in item.get('blanks', [])]
    structured_blanks = [{'id': b, 'label': b} for b in blanks]
    correct_map = {str(k): v for k, v in item.get('correct_map', {}).items()}
    text_parts = _normalise_text_parts(item.get('text_parts'), blanks, item['prompt'])
    out = {
        'id': f"{meta.id_prefix}_wb_{r.randint(1000, 999999)}",
        'title': item.get('title', 'Word bank'),
        'question_type': 'word_bank',
        'modality': 'math',
        'solution_type': 'word_bank',
        'prompt': item['prompt'],
        'word_bank': list(item.get('word_bank', [])),
        'blanks': structured_blanks,
        'correct_map': correct_map,
        'text_parts': text_parts,
        'expected_answer': str(correct_map),
        'explanation': item.get('explanation', ''),
        'marks': int(item.get('marks', len(blanks) or 1)),
        'minimum_mastery_score': item.get('minimum_mastery_score', 1.0),
    }
    out.update(_with_meta(meta, item, 'word_bank'))
    return out


def make_matching_question(meta: TopicMeta, r: random.Random, item: Dict[str, Any]) -> Dict[str, Any]:
    column_a = list(item.get('column_a', []))
    column_b = list(item.get('column_b', []))
    correct_pairs = dict(item.get('correct_pairs', {}))
    out = {
        'id': f"{meta.id_prefix}_match_{r.randint(1000, 999999)}",
        'title': item.get('title', 'Match the columns'),
        'question_type': 'matching_columns',
        'modality': 'math',
        'solution_type': 'matching',
        'prompt': item['prompt'],
        'column_a': column_a,
        'column_b': column_b,
        'correct_pairs': correct_pairs,
        'expected_answer': str(correct_pairs),
        'explanation': item.get('explanation', ''),
        'marks': int(item.get('marks', len(correct_pairs) or 1)),
        'minimum_mastery_score': item.get('minimum_mastery_score', 1.0),
    }
    out.update(_with_meta(meta, item, 'matching'))
    return out


def make_crossword_question(meta: TopicMeta, r: random.Random, item: Dict[str, Any]) -> Dict[str, Any]:
    words = [w.upper() for w in item.get('words', [])]
    clues = {k.upper(): v for k, v in item.get('clues', {}).items()}
    longest = max((len(w) for w in words), default=0)
    grid_size = max(int(item.get('grid_size', 0) or 0), longest + 2, 10)
    out = {
        'id': f"{meta.id_prefix}_cross_{r.randint(1000, 999999)}",
        'title': item.get('title', 'Crossword'),
        'question_type': 'crossword',
        'modality': 'math',
        'solution_type': 'crossword',
        'prompt': item['prompt'],
        'words': words,
        'clues': clues,
        'grid_size': grid_size,
        'expected_answer': ', '.join(words),
        'explanation': item.get('explanation', ''),
        'marks': int(item.get('marks', len(words) or 1)),
        'minimum_mastery_score': item.get('minimum_mastery_score', 1.0),
    }
    out.update(_with_meta(meta, item, 'crossword'))
    return out


def make_essay_question(meta: TopicMeta, r: random.Random, item: Dict[str, Any]) -> Dict[str, Any]:
    rubric = list(item.get('rubric', []))
    marks = int(item.get('marks', 20))
    schema = {
        'total_marks': marks,
        'marking_points': [
            {
                'id': f'mp_{i + 1}',
                'desc': f"{c.get('criterion', 'Criterion')}: {c.get('description', '')}".strip(': '),
                'marks': int(c.get('marks', 0)),
                'editable': True,
            }
            for i, c in enumerate(rubric)
        ],
        'deductions': [],
        'carry_forward_rule': 'consequential_accuracy',
    }
    sample = item.get('sample_answer', '')
    out = {
        'id': f"{meta.id_prefix}_essay_{r.randint(1000, 999999)}",
        'title': item.get('title', 'Essay'),
        'question_type': 'essay',
        'modality': 'semantic',
        'solution_type': 'rubric',
        'prompt': item['prompt'],
        'rubric': rubric,
        'marking_schema': schema,
        'sample_answer': sample,
        'expected_answer': sample,
        'explanation': sample,
        'marks': marks,
        'min_words': int(item.get('min_words', 120)),
        'max_words': int(item.get('max_words', 350)),
        'keywords': item.get('keywords', []),
        'minimum_mastery_score': item.get('minimum_mastery_score', 0.6),
    }
    out.update(_with_meta(meta, item, 'essay'))
    return out


def expand_matching_pool(pool: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Entropy for curated matching pools: sub-sampled variants of each item.

    A single authored 5-pair matching becomes several deterministic variants
    (different pair subsets, sizes, leads and shuffled Column B orders).
    """
    out: List[Dict[str, Any]] = []
    leads = [
        'Match each item in Column A with its correct partner in Column B',
        'Pair up each entry in Column A with the right entry in Column B',
        'Match the Column A items to their Column B partners',
    ]
    for idx, item in enumerate(pool):
        pairs = item.get('correct_pairs') or {}
        out.append(item)
        if len(pairs) < 4:
            continue
        items = list(pairs.items())
        base_seed = str(item.get('prompt', ''))[:40]
        for vi in range(1, 5):
            n = max(3, len(items) - vi)
            rr = random.Random(f"mp|{idx}|{vi}|{n}|{base_seed}")
            chosen = rr.sample(items, min(n, len(items)))
            column_b = [d for _t, d in chosen]
            rr.shuffle(column_b)
            variant = dict(item)
            variant['prompt'] = f"{leads[vi % len(leads)]}. ({len(chosen)} items)"
            variant['column_a'] = [t for t, _d in chosen]
            variant['column_b'] = column_b
            variant['correct_pairs'] = dict(chosen)
            variant['marks'] = len(chosen)
            out.append(variant)
    return out


def expand_crossword_pool(pool: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Entropy for curated crossword pools: sub-sampled word-set variants."""
    out: List[Dict[str, Any]] = []
    leads = [
        'Crossword of key terms for this topic',
        'Fill in the business-studies vocabulary',
        'Topic crossword puzzle',
    ]
    for idx, item in enumerate(pool):
        words = list(item.get('words') or [])
        clues = item.get('clues') or {}
        out.append(item)
        if len(words) < 5:
            continue
        base_seed = str(item.get('prompt', ''))[:40]
        for vi in range(1, 4):
            n = max(4, len(words) - vi)
            rr = random.Random(f"cwp|{idx}|{vi}|{n}|{base_seed}")
            chosen = rr.sample(words, min(n, len(words)))
            variant = dict(item)
            variant['prompt'] = f"{leads[vi % len(leads)]} ({len(chosen)} words)."
            variant['words'] = chosen
            variant['clues'] = {w: clues.get(w, '') for w in chosen}
            variant['marks'] = len(chosen)
            out.append(variant)
    return out


def derive_wordbank(concepts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Turn '....' style concept MCQs into grounded single-blank word banks."""
    out: List[Dict[str, Any]] = []
    for c in concepts:
        prompt = c.get('prompt', '')
        marker = next((m for m in ('\u2026', '...', '____') if m in prompt), None)
        if not marker:
            continue
        parts = prompt.split(marker)
        if len(parts) != 2:
            continue
        try:
            answer = c['options'][int(c['correct_index'])]
        except (KeyError, IndexError, ValueError, TypeError):
            continue
        if not answer or len(answer) > 30:
            continue
        out.append({
            'title': c.get('title', 'Complete the sentence'),
            'prompt': prompt.replace(marker, ' ______ '),
            'word_bank': list(c['options']),
            'blanks': ['1'],
            'correct_map': {'1': answer},
            'text_parts': [parts[0].rstrip() + ' ', ' ' + parts[1].strip()],
            'explanation': c.get('explanation', ''),
            'marks': 1,
            'hint_sections': c.get('hint_sections', []),
            'learning_objective_id': c.get('learning_objective_id'),
            'concept_id': c.get('concept_id'),
            'concept_group': c.get('concept_group'),
            'question_family_id': c.get('question_family_id'),
            'misconception_tags': c.get('misconception_tags', []),
            'diagnostic_tags': c.get('diagnostic_tags', []),
        })
    return out


def derive_matching(concepts: List[Dict[str, Any]], max_items: int = 5, extra_pairs: Optional[List[tuple]] = None) -> List[Dict[str, Any]]:
    """Pair concept terms (title) with their CAPS definitions (explanation).

    extra_pairs optionally extends the term/definition pool with pairs
    harvested from the curriculum docs. Entropy: returns several sub-sampled
    variants (different term subsets, sizes, leads, and shuffled Column B
    orders) so different seeds render genuinely different matching questions
    while staying fully deterministic.
    """
    usable = [c for c in concepts if c.get('title') and c.get('explanation')]
    usable = [{'title': t, 'explanation': d} for t, d in (extra_pairs or [])] + usable
    # de-duplicate by title so column A entries stay unambiguous
    seen = set()
    picked = []
    for c in usable:
        if c['title'] in seen:
            continue
        seen.add(c['title'])
        picked.append(c)
    if len(picked) < 3:
        return []
    sizes = [s for s in (max_items, max_items + 1, max_items + 2, 3) if s <= len(picked)]
    if not sizes:
        return []
    leads = [
        'Match each term in Column A with its correct definition in Column B',
        'Pair each CAPS term with its defining description',
        'Match the following business terms to their definitions',
        'Match each concept to the definition that best fits',
    ]
    out: List[Dict[str, Any]] = []
    variants = max(6, min(10, len(picked)))
    for vi in range(variants):
        n = sizes[vi % len(sizes)]
        rr = random.Random(f"match|{vi}|{n}|" + picked[0]['title'])
        chosen = rr.sample(picked, n)
        column_a = [c['title'] for c in chosen]
        column_b = [c['explanation'] for c in chosen]
        rr.shuffle(column_b)
        correct_pairs = {c['title']: c['explanation'] for c in chosen}
        out.append({
            'title': 'Match terms to definitions',
            'prompt': f"{leads[vi % len(leads)]}. ({n} items)",
            'column_a': column_a,
            'column_b': column_b,
            'correct_pairs': correct_pairs,
            'explanation': 'These are the CAPS definitions of the key terms of this topic.',
            'marks': n,
        })
    return out


def derive_crossword(concepts: List[Dict[str, Any]], max_items: int = 8, extra_pairs: Optional[List[tuple]] = None) -> List[Dict[str, Any]]:
    """Build crossword variants from concept terms and their definitions.

    extra_pairs (harvested term/definition pairs) seed the vocab first.
    Vocab sources, in preference order (all passes always run so thin topics
    still collect enough tokens):
      1. one-word titles (>=4 letters, the classic key-term case)
      2. longest word inside short multi-word term titles (<=6 words)
      3. longest word inside the correct option of each MCQ
    Entropy: several sub-sampled variants with different word sets, sizes,
    and leads.
    """
    vocab: List[tuple] = []  # (WORD, clue)
    seen = set()

    def _add(token: str, clue: str) -> None:
        token = re.sub(r'[^A-Za-z]', '', token or '')
        key = token.upper()
        if len(token) < 4 or not token.isalpha() or key in seen or not clue:
            return
        seen.add(key)
        vocab.append((key, clue))

    def _longest_word(text: str) -> str:
        words = re.findall(r'[A-Za-z]{4,}', text or '')
        return max(words, key=len) if words else ''

    # Pass 0: harvested term/definition pairs from the curriculum doc.
    for term, desc in (extra_pairs or []):
        _add(_longest_word(term) or term, desc)
    # Pass 1: single-word titles.
    for c in concepts:
        raw = (c.get('title') or '').strip()
        if not raw or ' ' in raw:
            continue
        _add(raw, c.get('explanation', ''))
    # Pass 2: longest word inside short multi-word term titles.
    for c in concepts:
        raw = (c.get('title') or '').strip()
        if ' ' not in raw or len(raw.split()) > 6:
            continue
        _add(_longest_word(raw), c.get('explanation', ''))
    # Pass 3: longest word inside the correct option (topics whose titles are
    # full exam sentences; the explanation carries the definition clue).
    for c in concepts:
        opts = c.get('options') or []
        try:
            ans = str(opts[int(c.get('correct_index', -1))])
        except (IndexError, ValueError, TypeError):
            continue
        _add(_longest_word(ans), c.get('explanation', '') or c.get('title', ''))
    if len(vocab) < 4:
        return []
    sizes = sorted({min(len(vocab), s) for s in (max_items, 6, 7, 5, 4)})
    leads = [
        'Crossword of key CAPS terms for this topic',
        'Fill in the business-studies vocabulary',
        'Topic crossword puzzle',
        'Complete the grid with the correct business terms',
    ]
    out: List[Dict[str, Any]] = []
    variants = max(4, min(8, len(vocab)))
    for vi in range(variants):
        n = sizes[vi % len(sizes)]
        rr = random.Random(f"cw|{vi}|{n}|" + vocab[0][0])
        chosen = rr.sample(vocab, n)
        words = [w for w, _ in chosen]
        clues = {w: c for w, c in chosen}
        out.append({
            'title': 'Topic crossword',
            'prompt': f"{leads[vi % len(leads)]} ({n} words).",
            'words': words,
            'clues': clues,
            'grid_size': max(10, max(len(w) for w in words) + 2),
            'explanation': 'Each answer is a key term of the topic; the clue is its definition.',
            'marks': n,
        })
    return out


def derive_essay(discussion: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Render each discussion prompt as a rubric-scored essay with a memo."""
    out: List[Dict[str, Any]] = []
    for d in discussion:
        points = d.get('marking_points') or []
        if not points:
            continue
        marks = int(d.get('marks', 6) or 6)
        per = max(1, marks // len(points))
        rubric = [{'criterion': f'Point {i + 1}', 'description': p, 'marks': per} for i, p in enumerate(points)]
        rubric[-1]['marks'] += marks - sum(c['marks'] for c in rubric)
        out.append({
            'title': d.get('title', 'Extended response'),
            'prompt': d['prompt'],
            'rubric': rubric,
            'sample_answer': d.get('sample_answer', ''),
            'marks': marks,
            'min_words': max(80, marks * 15),
            'max_words': max(200, marks * 30),
            'keywords': d.get('keywords', []),
            'hint_sections': d.get('hint_sections', []),
            'learning_objective_id': d.get('learning_objective_id'),
            'concept_id': d.get('concept_id'),
            'concept_group': d.get('concept_group'),
            'question_family_id': d.get('question_family_id'),
        })
    return out


def _harvested(grade: int, topic_key: str) -> List[Dict[str, Any]]:
    """Authentic exam Q&A harvested from the curriculum .md docs (cached).

    Returns raw item dicts; failures degrade silently to an empty list so
    generators never depend on the docs tree being present.
    """
    try:
        from ..bs_docs_harvester import harvest_items
        return harvest_items(grade, topic_key)
    except Exception:
        return []


def make_generate(
    meta: TopicMeta,
    concept_pool: PoolBuilder,
    application_pool: PoolBuilder,
    discussion_pool: PoolBuilder,
    *,
    wordbank_pool: Optional[PoolBuilder] = None,
    matching_pool: Optional[PoolBuilder] = None,
    crossword_pool: Optional[PoolBuilder] = None,
    essay_pool: Optional[PoolBuilder] = None,
) -> Callable[..., List[Dict[str, Any]]]:
    def generate(subskill: str = 'concepts', difficulty: str = 'medium', count: int = 1, seed=None, **kwargs):
        effective_seed = seed
        if 'subskill_' in str(subskill):
            try:
                slot_idx = int(str(subskill).split('subskill_')[-1])
                effective_seed = (seed or 100) + slot_idx * 1337
            except Exception:
                pass
        r = rng(effective_seed)
        concepts = apply_metadata_filters(concept_pool(r), **kwargs)
        application = apply_metadata_filters(application_pool(r), **kwargs)
        discussion = apply_metadata_filters(discussion_pool(r), **kwargs)

        # enrich with authentic questions harvested from the curriculum docs
        topic_key = str(kwargs.get('topic') or kwargs.get('topic_key') or '')
        harvest_pairs: List[tuple] = []
        if topic_key.startswith('grade1') and '_bs_' in topic_key:
            try:
                grade = int(topic_key[5:7])
            except ValueError:
                grade = 0
            if grade:
                harvested = _harvested(grade, topic_key)
                if harvested:
                    if grade >= 11:
                        # G11/G12 concept pools are raw dicts: MCQs slot straight in
                        concepts = concepts + [h for h in harvested if h.get('kind') == 'mcq']
                    discussion = discussion + [h for h in harvested if h.get('kind') != 'mcq']
                try:
                    from ..bs_docs_harvester import harvest_pairs as _hp
                    harvest_pairs = _hp(grade, topic_key)
                except Exception:
                    harvest_pairs = []

        if subskill == 'word_bank':
            pool = wordbank_pool(r) if wordbank_pool else derive_wordbank(concepts)
            return [make_wordbank_question(meta, r, item) for item in select_items(r, pool, count, difficulty, seed=effective_seed)]
        if subskill == 'matching':
            pool = expand_matching_pool(matching_pool(r)) if matching_pool else derive_matching(concepts, extra_pairs=harvest_pairs)
            return [make_matching_question(meta, r, item) for item in select_items(r, pool, count, difficulty, seed=effective_seed)]
        if subskill == 'crossword':
            pool = expand_crossword_pool(crossword_pool(r)) if crossword_pool else derive_crossword(concepts, extra_pairs=harvest_pairs)
            return [make_crossword_question(meta, r, item) for item in select_items(r, pool, count, difficulty, seed=effective_seed)]
        if subskill == 'essay':
            pool = essay_pool(r) if essay_pool else derive_essay(discussion)
            return [make_essay_question(meta, r, item) for item in select_items(r, pool, count, difficulty, seed=effective_seed)]

        if subskill == 'application':
            return [make_typed_question(meta, r, item) for item in select_items(r, application, count, difficulty, seed=effective_seed)]
        if subskill == 'discussion':
            return [make_typed_question(meta, r, item) for item in select_items(r, discussion, count, difficulty, seed=effective_seed)]
        if subskill == 'mixed':
            mixed_pool = (
                [('mcq', item) for item in concepts]
                + [('typed', item) for item in application]
                + [('typed', item) for item in discussion]
            )
            selected = select_items(r, mixed_pool, count, difficulty, seed=effective_seed)
            questions = []
            for kind, item in selected:
                questions.append(
                    make_mcq_question(meta, r, item) if kind == 'mcq' else make_typed_question(meta, r, item)
                )
            return questions
        return [make_mcq_question(meta, r, item) for item in select_items(r, concepts, count, difficulty, seed=effective_seed)]

    return generate
