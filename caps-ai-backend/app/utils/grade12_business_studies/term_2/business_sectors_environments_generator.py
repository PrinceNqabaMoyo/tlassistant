"""Grade 12 Business Studies - Term 2 - Business sectors and their environments.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='business_sectors_environments',
    curriculum_reference='Term 2 > Business sectors and their environments',
    id_prefix='g12_bs_sectors',
)

LO_SECTORS = 'lo_business_sectors'
LO_ENVIRONMENTS = 'lo_business_environments'
LO_CONTROL = 'lo_extent_of_control'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Primary sector',
            'prompt': 'A business that mines coal operates mainly in the …',
            'options': ['primary sector', 'secondary sector', 'tertiary sector', 'public sector'],
            'correct_index': 0,
            'explanation': 'The primary sector extracts/collects/harvests natural resources and raw materials from the earth, e.g. mining.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Think about extracting raw materials.',
                'Mining/harvesting raw materials = primary sector.',
                'Manufacturing them = secondary sector.',
            ),
            'guidelines': ['Extracting raw materials = primary sector.'],
        }, subskill='concepts', learning_objective_id=LO_SECTORS, question_family_id='primary_identify', concept_id='primary_sector', concept_group='sectors', misconception_tags=['confuses_primary_with_secondary'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Secondary sector',
            'prompt': 'A bakery that turns flour into bread operates in the …',
            'options': ['primary sector', 'secondary sector', 'tertiary sector', 'informal sector'],
            'correct_index': 1,
            'explanation': 'The secondary sector manufactures/processes raw materials into semi-finished or finished products, e.g. baking bread.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Think about processing raw materials.',
                'Manufacturing/processing = secondary sector.',
                'Selling the bread to customers = tertiary sector.',
            ),
            'guidelines': ['Manufacturing/processing = secondary sector.'],
        }, subskill='concepts', learning_objective_id=LO_SECTORS, question_family_id='secondary_identify', concept_id='secondary_sector', concept_group='sectors', misconception_tags=['confuses_secondary_with_tertiary'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Tertiary sector',
            'prompt': 'A supermarket that sells groceries to consumers operates in the …',
            'options': ['primary sector', 'secondary sector', 'tertiary sector', 'quaternary sector'],
            'correct_index': 2,
            'explanation': 'The tertiary sector provides/distributes final products and services to customers, e.g. retail.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Think about distributing/selling final goods and services.',
                'Selling/services to customers = tertiary sector.',
                'Making the goods = secondary sector.',
            ),
            'guidelines': ['Selling/services to customers = tertiary sector.'],
        }, subskill='concepts', learning_objective_id=LO_SECTORS, question_family_id='tertiary_identify', concept_id='tertiary_sector', concept_group='sectors', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Micro environment',
            'prompt': 'The business itself, including its functions and resources, is the …',
            'options': ['macro environment', 'market environment', 'micro environment', 'foreign environment'],
            'correct_index': 2,
            'explanation': 'The micro environment is the business itself, characterised by all the processes/functions/factors within the business.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on inside the business.',
                'The business and its functions = micro environment.',
                'Suppliers/competitors are the market environment.',
            ),
            'guidelines': ['Inside the business = micro environment.'],
        }, subskill='concepts', learning_objective_id=LO_ENVIRONMENTS, question_family_id='micro_identify', concept_id='micro_environment', concept_group='environments', misconception_tags=['confuses_micro_with_market'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Market environment',
            'prompt': 'Suppliers, customers and competitors immediately outside the business form the …',
            'options': ['micro environment', 'market environment', 'macro environment', 'internal environment'],
            'correct_index': 1,
            'explanation': 'The market environment is made up of the components immediately outside the business, such as suppliers, customers and competitors.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on factors just outside the business.',
                'Suppliers/customers/competitors = market environment.',
                'Broad uncontrollable factors = macro environment.',
            ),
            'guidelines': ['Suppliers/customers/competitors = market environment.'],
        }, subskill='concepts', learning_objective_id=LO_ENVIRONMENTS, question_family_id='market_identify', concept_id='market_environment', concept_group='environments', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Macro environment',
            'prompt': 'Which environment consists of external, uncontrollable forces such as inflation and legislation?',
            'options': ['micro environment', 'market environment', 'macro environment', 'task environment'],
            'correct_index': 2,
            'explanation': 'The macro environment consists of external uncontrollable factors/forces outside the business, e.g. economic and legal factors.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on uncontrollable external forces.',
                'Inflation/legislation = macro environment.',
                'These cannot be controlled by the business.',
            ),
            'guidelines': ['Uncontrollable external forces = macro environment.'],
        }, subskill='concepts', learning_objective_id=LO_ENVIRONMENTS, question_family_id='macro_identify', concept_id='macro_environment', concept_group='environments', diagnostic_tags=['identification']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Classify challenges by environment',
            'prompt': 'A bakery faces: (a) outdated ovens, (b) a powerful flour supplier raising prices, and (c) rising fuel prices nationally. Classify each challenge into the correct business environment. (3 marks)',
            'marks': 3,
            'marking_points': [
                'Outdated ovens = micro environment (inside the business).',
                'Powerful flour supplier = market environment (immediately outside).',
                'Rising fuel prices nationally = macro environment (uncontrollable external).',
            ],
            'sample_answer': 'The outdated ovens fall in the micro environment because they are inside the business. The powerful flour supplier is in the market environment because suppliers are immediately outside the business. Rising national fuel prices fall in the macro environment because they are uncontrollable external forces.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match each challenge to an environment.',
                'Inside = micro; immediately outside = market; uncontrollable = macro.',
                'Justify each classification.',
            ),
            'answer_part_hints': ['Classify each item.', 'Justify briefly.'],
            'guidelines': ['Classify all three correctly.'],
            'teaching_note': 'Reward correct classification with justification.',
            'keywords': ['micro', 'market', 'macro', 'supplier', 'uncontrollable'],
        }, subskill='application', learning_objective_id=LO_ENVIRONMENTS, question_family_id='classify_challenges_scenario', concept_id='business_environments', concept_group='environments', scenario_family_id='bakery_challenges', diagnostic_tags=['scenario_analysis'], answer_structure_tags=['classify'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Extent of control',
            'prompt': 'A retailer is affected by a new national tax law and by poor staff morale. Explain the extent to which the business can control each challenge. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The national tax law is in the macro environment.',
                'The business has no/little control over the macro environment; it can only adapt.',
                'Poor staff morale is in the micro environment.',
                'The business has full control over the micro environment and can resolve morale directly.',
            ],
            'sample_answer': 'The national tax law is in the macro environment, over which the business has little or no control, so it can only adapt to comply. Poor staff morale is in the micro environment, over which the business has full control, so it can address it directly through better management and motivation.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Link control to the environment.',
                'Macro = little/no control; micro = full control.',
                'Explain how the business responds to each.',
            ),
            'answer_part_hints': ['Address the tax law.', 'Address staff morale.'],
            'guidelines': ['Explain control for each challenge.'],
            'teaching_note': 'Reward correct extent of control for each.',
            'keywords': ['macro', 'no control', 'micro', 'full control', 'adapt'],
        }, subskill='application', learning_objective_id=LO_CONTROL, question_family_id='extent_control_scenario', concept_id='extent_of_control', concept_group='control', scenario_family_id='retailer_control', diagnostic_tags=['scenario_analysis'], answer_structure_tags=['explain'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Three business sectors',
            'prompt': 'Explain the three business sectors and give an example of a business in each. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Primary sector extracts/harvests natural resources, e.g. a mine or farm.',
                'Secondary sector manufactures/processes raw materials, e.g. a factory or bakery.',
                'Tertiary sector provides/distributes products and services, e.g. a retailer or bank.',
                'The sectors are interdependent and rely on one another.',
            ],
            'sample_answer': 'The primary sector extracts or harvests natural resources, such as a mine or farm. The secondary sector manufactures or processes those raw materials, such as a factory or bakery. The tertiary sector distributes the final products and provides services, such as a retailer or bank. The three sectors are interdependent and rely on one another.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain each sector with an example.',
                'Extract -> manufacture -> distribute/service.',
                'Mention interdependence.',
            ),
            'answer_part_hints': ['Explain each sector.', 'Give an example for each.'],
            'guidelines': ['Cover all three sectors with examples.'],
            'teaching_note': 'Reward each sector explained with an example.',
            'keywords': ['primary', 'secondary', 'tertiary', 'raw materials', 'services'],
        }, subskill='discussion', learning_objective_id=LO_SECTORS, question_family_id='sectors_discussion', concept_id='business_sectors', concept_group='sectors', diagnostic_tags=['discussion'], answer_structure_tags=['explain', 'example'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Environments and control',
            'prompt': 'Discuss the three business environments and the extent of control a business has over each. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Micro environment: the business itself; the business has full control.',
                'Market environment: suppliers/customers/competitors; the business has some/partial control (can influence).',
                'Macro environment: external uncontrollable forces; the business has little/no control and must adapt.',
                'Understanding control helps the business respond appropriately to each challenge.',
            ],
            'sample_answer': 'The micro environment is the business itself, over which it has full control. The market environment includes suppliers, customers and competitors, over which the business has only partial control but can influence through relationships and marketing. The macro environment consists of external uncontrollable forces, over which the business has little or no control and can only adapt. Understanding the extent of control helps the business respond appropriately.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Cover all three environments and their control.',
                'Full control (micro), partial (market), none (macro).',
                'Explain how control affects the response.',
            ),
            'answer_part_hints': ['Explain each environment.', 'State the extent of control.'],
            'guidelines': ['Cover all three with extent of control.'],
            'teaching_note': 'Reward each environment with its level of control.',
            'keywords': ['micro', 'market', 'macro', 'full control', 'no control'],
        }, subskill='discussion', learning_objective_id=LO_CONTROL, question_family_id='environments_control_discussion', concept_id='extent_of_control', concept_group='control', diagnostic_tags=['discussion', 'evaluation'], answer_structure_tags=['explain', 'list'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
