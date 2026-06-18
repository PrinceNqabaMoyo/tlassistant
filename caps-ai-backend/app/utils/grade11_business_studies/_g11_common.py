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


def select_items(r: random.Random, pool: Sequence[Any], count: int, difficulty: str) -> List[Any]:
    """Deterministically select `count` items, filtered by difficulty band."""
    filtered = [item for item in pool if difficulty in _difficulties(item)]
    working = filtered or list(pool)
    if not working:
        return []
    if count <= len(working):
        return r.sample(working, count)
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
    correct_option = item['options'][item['correct_index']]
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


def make_generate(
    meta: TopicMeta,
    concept_pool: PoolBuilder,
    application_pool: PoolBuilder,
    discussion_pool: PoolBuilder,
) -> Callable[..., List[Dict[str, Any]]]:
    def generate(subskill: str = 'concepts', difficulty: str = 'medium', count: int = 1, seed=None, **kwargs):
        r = rng(seed)
        concepts = apply_metadata_filters(concept_pool(r), **kwargs)
        application = apply_metadata_filters(application_pool(r), **kwargs)
        discussion = apply_metadata_filters(discussion_pool(r), **kwargs)

        if subskill == 'application':
            return [make_typed_question(meta, r, item) for item in select_items(r, application, count, difficulty)]
        if subskill == 'discussion':
            return [make_typed_question(meta, r, item) for item in select_items(r, discussion, count, difficulty)]
        if subskill == 'mixed':
            mixed_pool = (
                [('mcq', item) for item in concepts]
                + [('typed', item) for item in application]
                + [('typed', item) for item in discussion]
            )
            selected = select_items(r, mixed_pool, count, difficulty)
            questions = []
            for kind, item in selected:
                questions.append(
                    make_mcq_question(meta, r, item) if kind == 'mcq' else make_typed_question(meta, r, item)
                )
            return questions
        return [make_mcq_question(meta, r, item) for item in select_items(r, concepts, count, difficulty)]

    return generate
