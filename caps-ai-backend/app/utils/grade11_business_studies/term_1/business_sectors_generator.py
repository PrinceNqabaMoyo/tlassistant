"""Grade 11 Business Studies - Term 1 - Topic 5: Business Sectors.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='business_sectors',
    curriculum_reference='Term 1 > Business Sectors',
    id_prefix='g11_bs_sectors',
)

LO_SECTORS = 'lo_meaning_of_sectors'
LO_LINK = 'lo_link_between_sectors'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Primary sector',
            'prompt': 'The sector that deals with the extraction of raw materials and natural resources is the … sector.',
            'options': ['primary', 'secondary', 'tertiary', 'public'],
            'correct_index': 0,
            'explanation': 'The primary sector deals with the extraction/collecting/cultivating of raw materials and natural resources.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the activity to a sector.',
                'Extraction of raw materials = primary sector.',
                'Examples: agriculture, fishing, forestry, mining.',
            ),
            'guidelines': ['Link extraction of raw materials to the primary sector.'],
        }, subskill='concepts', learning_objective_id=LO_SECTORS, question_family_id='primary_sector_definition', concept_id='primary_sector', concept_group='sectors', misconception_tags=['confuses_primary_with_secondary'], diagnostic_tags=['definition', 'sectors']),
        with_metadata({
            'title': 'Secondary sector',
            'prompt': 'The sector that transforms raw materials into finished or unfinished products is the … sector.',
            'options': ['primary', 'secondary', 'tertiary', 'informal'],
            'correct_index': 1,
            'explanation': 'The secondary sector transforms the raw materials from the primary sector into finished or unfinished products.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the activity to a sector.',
                'Transforming raw materials into products = secondary sector.',
                'Examples: manufacturing, construction, factories.',
            ),
            'guidelines': ['Link processing/manufacturing to the secondary sector.'],
        }, subskill='concepts', learning_objective_id=LO_SECTORS, question_family_id='secondary_sector_definition', concept_id='secondary_sector', concept_group='sectors', misconception_tags=['confuses_secondary_with_tertiary'], diagnostic_tags=['definition', 'sectors']),
        with_metadata({
            'title': 'Tertiary sector',
            'prompt': 'The sector that offers services to other businesses and consumers is the … sector.',
            'options': ['primary', 'secondary', 'tertiary', 'natural'],
            'correct_index': 2,
            'explanation': 'The tertiary sector refers to industries that offer services to other businesses and consumers (the services industry).',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the activity to a sector.',
                'Offering services = tertiary sector.',
                'Examples: retailers, wholesalers, tourism, transport, banking.',
            ),
            'guidelines': ['Link services to the tertiary sector.'],
        }, subskill='concepts', learning_objective_id=LO_SECTORS, question_family_id='tertiary_sector_definition', concept_id='tertiary_sector', concept_group='sectors', misconception_tags=['confuses_tertiary_with_secondary'], diagnostic_tags=['definition', 'sectors']),
        with_metadata({
            'title': 'Mining classification',
            'prompt': 'A gold-mining company belongs to which sector?',
            'options': ['primary', 'secondary', 'tertiary', 'quaternary'],
            'correct_index': 0,
            'explanation': 'Mining extracts natural resources (gold), so it belongs to the primary sector.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Classify a real industry.',
                'Mining extracts minerals/metals = primary sector.',
                'Extraction always points to the primary sector.',
            ),
            'guidelines': ['Classify by the nature of the activity.'],
        }, subskill='concepts', learning_objective_id=LO_SECTORS, question_family_id='classify_industry', concept_id='primary_sector', concept_group='sectors', retry_variant='reworded', misconception_tags=['confuses_mining_with_manufacturing'], diagnostic_tags=['classification', 'sectors']),
        with_metadata({
            'title': 'Forward link',
            'prompt': 'When a business sells its goods to a business in another sector, this is an example of a …',
            'options': ['backward link', 'forward link', 'merger', 'lockout'],
            'correct_index': 1,
            'explanation': 'A forward link is when businesses sell goods and services to businesses in the same or another sector.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Note the direction of the transaction.',
                'Selling forward to another business = forward link.',
                'Buying from another business = backward link.',
            ),
            'guidelines': ['Selling = forward link.'],
        }, subskill='concepts', learning_objective_id=LO_LINK, question_family_id='forward_link_definition', concept_id='forward_link', concept_group='links', misconception_tags=['confuses_forward_with_backward'], diagnostic_tags=['definition', 'links']),
        with_metadata({
            'title': 'Backward link',
            'prompt': 'When a manufacturer buys raw materials from a farming business, this is an example of a …',
            'options': ['forward link', 'backward link', 'alliance', 'strike'],
            'correct_index': 1,
            'explanation': 'A backward link is when businesses buy goods and services from businesses in the same or another sector.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Note the direction of the transaction.',
                'Buying inputs from another business = backward link.',
                'Selling output forward = forward link.',
            ),
            'guidelines': ['Buying = backward link.'],
        }, subskill='concepts', learning_objective_id=LO_LINK, question_family_id='backward_link_definition', concept_id='backward_link', concept_group='links', misconception_tags=['confuses_backward_with_forward'], diagnostic_tags=['definition', 'links']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Classify and link',
            'prompt': 'A furniture factory buys timber from a forestry company and sells finished tables to a retailer. Identify the sector the factory belongs to and explain ONE link it has with another sector. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The factory belongs to the secondary sector (it transforms timber into tables).',
                'Backward link: it buys timber from the forestry company (primary sector).',
                'Forward link: it sells tables to a retailer (tertiary sector).',
                'Explanation must connect the factory to another sector.',
            ],
            'sample_answer': 'The furniture factory is in the secondary sector because it transforms timber into tables. It has a backward link with the primary sector (buying timber from the forestry company) and a forward link with the tertiary sector (selling tables to a retailer).',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Classify the business, then identify a link.',
                'Transforming raw materials = secondary sector.',
                'Buying inputs = backward link; selling output = forward link.',
            ),
            'answer_part_hints': ['Name the sector.', 'Explain a link to another sector.'],
            'guidelines': ['Use scenario evidence for the link.'],
            'teaching_note': 'Reward correct sector plus a correctly-named link.',
            'keywords': ['secondary', 'transform', 'backward link', 'forward link', 'timber', 'retailer'],
        }, subskill='application', learning_objective_id=LO_LINK, question_family_id='classify_and_link_scenario', concept_id='secondary_sector', concept_group='links', scenario_family_id='furniture_factory_links', diagnostic_tags=['scenario_analysis', 'sectors'], answer_structure_tags=['identify', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Identify the sector',
            'prompt': 'A tour operator arranges holiday packages and transport for tourists. Identify the sector and motivate your answer. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The tour operator is in the tertiary sector.',
                'It offers services (holidays, transport) to consumers.',
                'No extraction of raw materials or manufacturing takes place.',
                'Motivation must reference the provision of services.',
            ],
            'sample_answer': 'The tour operator is in the tertiary sector because it offers services such as holiday packages and transport to consumers, rather than extracting raw materials or manufacturing products.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Classify by what the business does.',
                'Providing services = tertiary sector.',
                'Look for "services" rather than extraction/manufacturing.',
            ),
            'answer_part_hints': ['Name the sector.', 'Motivate with evidence.'],
            'guidelines': ['Justify with provision of services.'],
            'teaching_note': 'Reward correct sector plus justification.',
            'keywords': ['tertiary', 'services', 'transport', 'tourists', 'consumers'],
        }, subskill='application', learning_objective_id=LO_SECTORS, question_family_id='identify_sector_scenario', concept_id='tertiary_sector', concept_group='sectors', scenario_family_id='tour_operator', diagnostic_tags=['scenario_analysis', 'sectors'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Link between the sectors',
            'prompt': 'Discuss the link/relationship between the primary, secondary and tertiary sectors. (6 marks)',
            'marks': 6,
            'marking_points': [
                'The primary sector extracts raw materials and supplies them to the secondary sector.',
                'The secondary sector transforms raw materials into products.',
                'The tertiary sector distributes/sells the products and provides services.',
                'The sectors are interdependent: each relies on the others (forward and backward links).',
            ],
            'sample_answer': 'The primary sector extracts raw materials and supplies them to the secondary sector, which transforms them into products. The tertiary sector then distributes, sells and provides services for these products. The three sectors are interdependent through forward and backward links, each relying on the others.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain how the sectors depend on each other.',
                'Trace raw materials from extraction to services.',
                'Use the idea of forward and backward links.',
            ),
            'answer_part_hints': ['Explain each sector\'s role.', 'Explain how they connect.'],
            'guidelines': ['Show interdependence between all three sectors.'],
            'teaching_note': 'Reward the flow from primary to secondary to tertiary plus interdependence.',
            'keywords': ['primary', 'secondary', 'tertiary', 'raw materials', 'interdependent', 'links'],
        }, subskill='discussion', learning_objective_id=LO_LINK, question_family_id='link_between_sectors_discussion', concept_id='sector_links', concept_group='links', diagnostic_tags=['discussion', 'sectors'], answer_structure_tags=['explain', 'connect'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Meaning of the three sectors',
            'prompt': 'Explain the meaning of the primary, secondary and tertiary sectors, giving an example of each. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Primary: extraction of raw materials (e.g. mining/farming).',
                'Secondary: transforms raw materials into products (e.g. manufacturing).',
                'Tertiary: offers services to businesses and consumers (e.g. retail/banking).',
                'Each explanation should be paired with a relevant example.',
            ],
            'sample_answer': 'The primary sector extracts raw materials and natural resources, for example mining or farming. The secondary sector transforms these raw materials into products, for example manufacturing. The tertiary sector offers services to businesses and consumers, for example retail or banking.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Define each sector and give an example.',
                'Extraction, transformation, services - in that order.',
                'Pair each definition with a clear example.',
            ),
            'answer_part_hints': ['Define each sector.', 'Give an example of each.'],
            'guidelines': ['Definitions plus examples for all three sectors.'],
            'teaching_note': 'Reward accurate definitions paired with examples.',
            'keywords': ['primary', 'secondary', 'tertiary', 'extraction', 'manufacturing', 'services'],
        }, subskill='discussion', learning_objective_id=LO_SECTORS, question_family_id='meaning_of_sectors_discussion', concept_id='sectors', concept_group='sectors', diagnostic_tags=['discussion', 'sectors'], answer_structure_tags=['define', 'exemplify'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
