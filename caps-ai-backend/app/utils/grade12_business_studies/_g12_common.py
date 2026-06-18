"""Shared deterministic helpers for Grade 12 Business Studies generators.

Grade 12 reuses the same adaptive-ready question shape and builders as Grade 11
(seeded RNG, per-question metadata, 3-section scaffold hints, keyword-based
mastery). To avoid duplicating that infrastructure this module simply re-exports
the Grade 11 helpers; each Grade 12 topic generator declares its content pools
and a small ``TopicMeta`` then exports
``generate = make_generate(meta, concept_pool, application_pool, discussion_pool)``.
"""
from __future__ import annotations

from app.utils.grade11_business_studies._g11_common import (  # noqa: F401
    TopicMeta,
    apply_metadata_filters,
    hint_sections,
    make_generate,
    make_mcq_question,
    make_typed_question,
    rng,
    select_items,
    with_metadata,
)

__all__ = [
    'TopicMeta',
    'apply_metadata_filters',
    'hint_sections',
    'make_generate',
    'make_mcq_question',
    'make_typed_question',
    'rng',
    'select_items',
    'with_metadata',
]
