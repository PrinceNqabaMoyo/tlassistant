"""Grade 11 Business Studies - Term 3 - Topic 13: Assessment of entrepreneurial
qualities.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='entrepreneurial_assessment',
    curriculum_reference='Term 3 > Assessment of entrepreneurial qualities',
    id_prefix='g11_bs_entre',
)

LO_QUALITIES = 'lo_entrepreneurial_qualities'
LO_SUCCESS = 'lo_key_success_factors'
LO_STRATEGIES = 'lo_sustainability_strategies'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Entrepreneur',
            'prompt': 'Someone who converts a business idea into a business venture is a(n) …',
            'options': ['employee', 'entrepreneur', 'shareholder', 'manager'],
            'correct_index': 1,
            'explanation': 'An entrepreneur is someone who converts a business idea into a business venture.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify who turns ideas into ventures.',
                'An entrepreneur converts an idea into a business.',
                'A manager runs an existing business; an entrepreneur starts it.',
            ),
            'guidelines': ['Link "converts an idea into a venture" to entrepreneur.'],
        }, subskill='concepts', learning_objective_id=LO_QUALITIES, question_family_id='entrepreneur_definition', concept_id='entrepreneur', concept_group='qualities', misconception_tags=['confuses_entrepreneur_with_manager'], diagnostic_tags=['definition', 'entrepreneurship']),
        with_metadata({
            'title': 'Perseverance',
            'prompt': 'An entrepreneur who does not give up despite challenges and problems shows the quality of …',
            'options': ['perseverance', 'confidence', 'creativity', 'risk-taking'],
            'correct_index': 0,
            'explanation': 'Perseverance is when an entrepreneur does not give up despite challenges and problems.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the behaviour to a quality.',
                'Not giving up = perseverance.',
                'Confidence is believing in oneself; creativity is new ideas.',
            ),
            'guidelines': ['Not giving up = perseverance.'],
        }, subskill='concepts', learning_objective_id=LO_QUALITIES, question_family_id='perseverance_definition', concept_id='perseverance', concept_group='qualities', misconception_tags=['confuses_perseverance_with_confidence'], diagnostic_tags=['definition', 'qualities']),
        with_metadata({
            'title': 'Sustainability',
            'prompt': 'A business that can continue operating without damaging the environment and community shows …',
            'options': ['profitability', 'sustainability', 'productivity', 'liquidity'],
            'correct_index': 1,
            'explanation': 'Sustainability means the business can continue without doing damage to the environment and the community in which it works.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the long-term, responsible factor.',
                'Sustainability = continuing without harming environment/community.',
                'Profitability is only about monetary gain.',
            ),
            'guidelines': ['Continuing responsibly = sustainability.'],
        }, subskill='concepts', learning_objective_id=LO_SUCCESS, question_family_id='sustainability_definition', concept_id='sustainability', concept_group='success_factors', misconception_tags=['confuses_sustainability_with_profitability'], diagnostic_tags=['definition', 'success_factors']),
        with_metadata({
            'title': 'Customer base',
            'prompt': 'A loyal group of customers who always buy a business\'s goods or services is its …',
            'options': ['target market', 'customer base', 'shareholders', 'workforce'],
            'correct_index': 1,
            'explanation': 'A customer base is the loyal group of customers who always buy a business\'s goods or services - a key success factor.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the loyal buyers.',
                'A loyal, repeat group of buyers = customer base.',
                'The target market is who you aim at, not necessarily loyal buyers.',
            ),
            'guidelines': ['Loyal repeat buyers = customer base.'],
        }, subskill='concepts', learning_objective_id=LO_SUCCESS, question_family_id='customer_base_definition', concept_id='customer_base', concept_group='success_factors', misconception_tags=['confuses_customer_base_with_target_market'], diagnostic_tags=['definition', 'success_factors']),
        with_metadata({
            'title': 'Key success factor',
            'prompt': 'Which of the following is a key success factor for a business?',
            'options': ['High staff turnover', 'A solid, loyal customer base', 'Ignoring ethics', 'Wasting resources'],
            'correct_index': 1,
            'explanation': 'Key success factors include sustainability, profitability and a solid/loyal customer base.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Pick what makes a business succeed.',
                'A loyal customer base supports success.',
                'High turnover and waste undermine success.',
            ),
            'guidelines': ['Look for factors that support success.'],
        }, subskill='concepts', learning_objective_id=LO_SUCCESS, question_family_id='success_factor_identification', concept_id='key_success_factors', concept_group='success_factors', misconception_tags=['confuses_success_with_failure_factors'], diagnostic_tags=['identification', 'success_factors']),
        with_metadata({
            'title': 'Good governance',
            'prompt': 'Processes and institutions that produce results meeting society\'s needs while best using available resources describe …',
            'options': ['good governance', 'risk-taking', 'creativity', 'productivity'],
            'correct_index': 0,
            'explanation': 'Good governance refers to processes and institutions that produce results to meet society\'s needs while making the best use of available resources.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify responsible, effective management.',
                'Good governance meets society\'s needs using resources well.',
                'It supports a business\'s sustainability and reputation.',
            ),
            'guidelines': ['Responsible, effective use of resources = good governance.'],
        }, subskill='concepts', learning_objective_id=LO_STRATEGIES, question_family_id='good_governance_definition', concept_id='good_governance', concept_group='strategies', misconception_tags=['confuses_governance_with_productivity'], diagnostic_tags=['definition', 'strategies']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Assess entrepreneurial qualities',
            'prompt': 'Thabo started a small delivery business. When his first van broke down he borrowed another and kept all deliveries on time, and he constantly looks for new routes to win customers. Identify TWO entrepreneurial qualities he shows and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Perseverance - he did not give up when the van broke down.',
                'Creativity/opportunity-seeking - he looks for new routes to win customers.',
                'Customer focus - he kept deliveries on time for customers.',
                'Each quality is motivated with scenario evidence.',
            ],
            'sample_answer': 'Thabo shows perseverance because he did not give up when his van broke down but borrowed another to keep deliveries on time. He also shows creativity and opportunity-seeking because he constantly looks for new routes to win customers.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match behaviours to named qualities.',
                'Not giving up = perseverance; new routes = creativity.',
                'Use the scenario as evidence for each quality.',
            ),
            'answer_part_hints': ['Name two qualities.', 'Motivate each with evidence.'],
            'guidelines': ['Use scenario evidence for each quality.'],
            'teaching_note': 'Reward two correctly-named qualities with motivation.',
            'keywords': ['perseverance', 'creativity', 'customer focus', 'opportunity', 'did not give up'],
        }, subskill='application', learning_objective_id=LO_QUALITIES, question_family_id='assess_qualities_scenario', concept_id='entrepreneur', concept_group='qualities', scenario_family_id='thabo_delivery', diagnostic_tags=['scenario_analysis', 'qualities'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Recommend improvements',
            'prompt': 'A business is losing customers, wastes materials and has no financial records. Recommend TWO strategies to help it remain profitable and sustainable. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Sound financial management / keep proper financial records.',
                'Effective management of scarce resources to reduce waste.',
                'Maintain a solid customer base through better service/marketing.',
                'Thorough planning and ethical, socially responsible behaviour.',
            ],
            'sample_answer': 'The business should introduce sound financial management by keeping proper records, and manage its scarce resources effectively to reduce material waste. It should also work to rebuild a solid customer base through better service and marketing, supported by thorough planning.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Target the weaknesses in the scenario.',
                'No records -> financial management; waste -> resource management.',
                'Losing customers -> rebuild the customer base.',
            ),
            'answer_part_hints': ['Give two strategies.', 'Link them to the problems.'],
            'guidelines': ['Recommendations must address the scenario weaknesses.'],
            'teaching_note': 'Reward strategies tied to the specific weaknesses.',
            'keywords': ['financial management', 'resources', 'waste', 'customer base', 'planning'],
        }, subskill='application', learning_objective_id=LO_STRATEGIES, question_family_id='recommend_improvements_scenario', concept_id='sustainability', concept_group='strategies', scenario_family_id='struggling_business', diagnostic_tags=['recommendation', 'strategies'], answer_structure_tags=['recommend', 'apply'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Qualities of an entrepreneur',
            'prompt': 'Outline the qualities of a successful entrepreneur. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Confidence - believes in themselves and their goals.',
                'Passion and perseverance - enthusiasm and not giving up.',
                'Creativity - new ideas/doing things in new ways.',
                'Opportunity-seeking - spotting gaps in the market.',
                'Customer focus and willingness to take calculated risks.',
            ],
            'sample_answer': 'A successful entrepreneur shows confidence (belief in themselves and their goals), passion and perseverance (enthusiasm and not giving up despite challenges), creativity (new ideas and new ways of doing things), opportunity-seeking (spotting gaps in the market), strong customer focus, and a willingness to take calculated risks.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List and explain several qualities.',
                'Think confidence, passion, perseverance, creativity.',
                'Add opportunity-seeking, customer focus and risk-taking.',
            ),
            'answer_part_hints': ['Name each quality.', 'Explain each briefly.'],
            'guidelines': ['Provide at least four qualities with explanation.'],
            'teaching_note': 'Reward breadth of qualities plus explanation.',
            'keywords': ['confidence', 'passion', 'perseverance', 'creativity', 'opportunity', 'customer focus', 'risk'],
        }, subskill='discussion', learning_objective_id=LO_QUALITIES, question_family_id='qualities_discussion', concept_id='entrepreneur', concept_group='qualities', diagnostic_tags=['discussion', 'qualities'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Strategies for profitability and sustainability',
            'prompt': 'Suggest strategies that businesses can use to ensure they remain profitable and sustainable. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Thorough planning of operations and finances.',
                'Sound financial management.',
                'Effective management of scarce resources and employees.',
                'Maintaining a solid customer base; behaving ethically and being socially responsible.',
            ],
            'sample_answer': 'Businesses can remain profitable and sustainable through thorough planning, sound financial management, and effective management of scarce resources and employees. They should maintain a solid customer base through good service, and behave ethically and be socially responsible to protect their reputation and long-term survival.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List strategies for long-term success.',
                'Think planning, finance, resources and customers.',
                'Ethics and social responsibility support sustainability.',
            ),
            'answer_part_hints': ['Give several strategies.', 'Explain each.'],
            'guidelines': ['Provide at least three strategies.'],
            'teaching_note': 'Reward distinct strategies from the curriculum list.',
            'keywords': ['planning', 'financial management', 'resources', 'customer base', 'ethics', 'social responsibility'],
        }, subskill='discussion', learning_objective_id=LO_STRATEGIES, question_family_id='strategies_discussion', concept_id='sustainability', concept_group='strategies', diagnostic_tags=['discussion', 'strategies'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
