"""Grade 11 Business Studies - Term 3 - Topic 16: Start a business venture based
on an action plan.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='start_business_venture',
    curriculum_reference='Term 3 > Start a business venture based on an action plan',
    id_prefix='g11_bs_startup',
)

LO_STARTUP = 'lo_startup_factors'
LO_INITIATE = 'lo_initiation_aspects'
LO_FUNDING = 'lo_funding'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Strategy',
            'prompt': 'A long-term plan of action to achieve a goal is called a …',
            'options': ['strategy', 'operation', 'productivity', 'budget'],
            'correct_index': 0,
            'explanation': 'A strategy is a long-term plan of action to achieve a goal.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the long-term plan.',
                'Strategy = long-term plan to reach a goal.',
                'Operations are the day-to-day activities.',
            ),
            'guidelines': ['Long-term plan = strategy.'],
        }, subskill='concepts', learning_objective_id=LO_INITIATE, question_family_id='strategy_definition', concept_id='strategy', concept_group='initiation', misconception_tags=['confuses_strategy_with_operations'], diagnostic_tags=['definition', 'initiation']),
        with_metadata({
            'title': 'Productivity',
            'prompt': 'The effectiveness of production in terms of the rate of output per unit of input is called …',
            'options': ['cost-saving', 'productivity', 'business growth', 'risk'],
            'correct_index': 1,
            'explanation': 'Productivity is the effectiveness of production in terms of the rate of output per unit of input.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify output per input.',
                'Productivity = output per unit of input.',
                'Cost-saving is about cutting expenses.',
            ),
            'guidelines': ['Output per input = productivity.'],
        }, subskill='concepts', learning_objective_id=LO_INITIATE, question_family_id='productivity_definition', concept_id='productivity', concept_group='initiation', misconception_tags=['confuses_productivity_with_growth'], diagnostic_tags=['definition', 'initiation']),
        with_metadata({
            'title': 'Cost-saving',
            'prompt': 'The plans a business makes to cut its costs and expenses are known as …',
            'options': ['business growth', 'cost-saving', 'productivity', 'strategy'],
            'correct_index': 1,
            'explanation': 'Cost-saving refers to the plans made by the business to cut its costs/expenses.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify cutting expenses.',
                'Cost-saving = plans to cut costs/expenses.',
                'Business growth is expansion in size.',
            ),
            'guidelines': ['Cutting expenses = cost-saving.'],
        }, subskill='concepts', learning_objective_id=LO_STARTUP, question_family_id='cost_saving_definition', concept_id='cost_saving', concept_group='startup', misconception_tags=['confuses_cost_saving_with_growth'], diagnostic_tags=['definition', 'startup']),
        with_metadata({
            'title': 'Startup factor',
            'prompt': 'Which of the following is a factor a business must consider BEFORE start-up?',
            'options': [
                'The colour of the office walls only',
                'Environmental changes and customer service',
                'The CEO\'s favourite sport',
                'Ignoring competitors',
            ],
            'correct_index': 1,
            'explanation': 'Factors to consider before start-up include the culture of the organisation, environmental changes, customer service, business growth and cost-saving.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Pick a genuine start-up factor.',
                'Environmental changes and customer service matter.',
                'Trivial or irrelevant preferences are not factors.',
            ),
            'guidelines': ['Look for business-relevant start-up factors.'],
        }, subskill='concepts', learning_objective_id=LO_STARTUP, question_family_id='startup_factor_identification', concept_id='startup_factors', concept_group='startup', misconception_tags=['confuses_relevant_with_irrelevant_factors'], diagnostic_tags=['identification', 'startup']),
        with_metadata({
            'title': 'Source of funding',
            'prompt': 'Which of the following is a source of funding for a business?',
            'options': ['Loading', 'A bank loan', 'Dispatching', 'Routing'],
            'correct_index': 1,
            'explanation': 'Sources of funding include own capital, bank loans, overdrafts, credit and investors.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify where money comes from.',
                'A bank loan is a source of funding.',
                'Loading/dispatching/routing are production terms.',
            ),
            'guidelines': ['Source of money = funding source.'],
        }, subskill='concepts', learning_objective_id=LO_FUNDING, question_family_id='funding_source_identification', concept_id='sources_of_funding', concept_group='funding', misconception_tags=['confuses_funding_with_production_terms'], diagnostic_tags=['identification', 'funding']),
        with_metadata({
            'title': 'Factor influencing choice of funding',
            'prompt': 'Which of the following influences a business\'s choice of funding?',
            'options': [
                'The weather forecast',
                'The amount of capital needed and the cost of finance',
                'The colour of the logo',
                'The CEO\'s star sign',
            ],
            'correct_index': 1,
            'explanation': 'Factors influencing the choice of funding include the nature of finance, the amount of capital needed, the risk and the cost of finance.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Pick a real funding consideration.',
                'Amount needed and cost of finance matter.',
                'Irrelevant factors do not influence funding choice.',
            ),
            'guidelines': ['Look for finance-related considerations.'],
        }, subskill='concepts', learning_objective_id=LO_FUNDING, question_family_id='funding_factor_identification', concept_id='choice_of_funding', concept_group='funding', misconception_tags=['confuses_relevant_funding_factors'], diagnostic_tags=['identification', 'funding']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Analyse start-up factors',
            'prompt': 'An entrepreneur plans to open a coffee shop but has not researched nearby competitors or who the customers will be. Identify TWO factors she has overlooked and recommend how to address them. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Overlooked the competitive environment (environmental changes).',
                'Overlooked customer service / knowing the target customers.',
                'Recommend market research on competitors and customers.',
                'Recommend adjusting the offering/strategy to the findings.',
            ],
            'sample_answer': 'She has overlooked the competitive environment and an understanding of her customers and customer service. She should carry out market research on nearby competitors and the target customers, and then adjust her offering and strategy based on what she finds.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Spot the missing start-up factors.',
                'No competitor/customer research = overlooked factors.',
                'Recommend research and adjustment.',
            ),
            'answer_part_hints': ['Identify two factors.', 'Recommend how to address them.'],
            'guidelines': ['Use scenario evidence plus recommendations.'],
            'teaching_note': 'Reward identifying overlooked factors and addressing them.',
            'keywords': ['competitors', 'customers', 'market research', 'environment', 'customer service'],
        }, subskill='application', learning_objective_id=LO_STARTUP, question_family_id='analyse_startup_scenario', concept_id='startup_factors', concept_group='startup', scenario_family_id='coffee_shop_startup', diagnostic_tags=['scenario_analysis', 'startup'], answer_structure_tags=['identify', 'recommend'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Choose a source of funding',
            'prompt': 'A new business needs a large amount of capital for equipment but wants to keep monthly repayments and risk low. Recommend a suitable source of funding and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend a source matched to a large amount and low risk (e.g. own capital/investor/long-term loan).',
                'Consider the amount of capital needed.',
                'Consider the cost of finance and risk.',
                'Motivate why the chosen source keeps repayments/risk low.',
            ],
            'sample_answer': 'Because a large amount of capital is needed but the business wants low repayments and risk, it could use own capital or bring in an investor rather than expensive short-term debt; if borrowing, a long-term loan spreads repayments. This matches the amount needed while keeping the cost of finance and risk lower.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the funding source to the needs.',
                'Large amount + low risk favours equity or long-term finance.',
                'Weigh cost of finance and repayment burden.',
            ),
            'answer_part_hints': ['Name a source.', 'Motivate against the needs.'],
            'guidelines': ['Tie the choice to amount, cost and risk.'],
            'teaching_note': 'Reward a sensible source with a motivation on cost/risk.',
            'keywords': ['capital', 'investor', 'own capital', 'long-term loan', 'cost of finance', 'risk'],
        }, subskill='application', learning_objective_id=LO_FUNDING, question_family_id='choose_funding_scenario', concept_id='choice_of_funding', concept_group='funding', scenario_family_id='equipment_funding', diagnostic_tags=['recommendation', 'funding'], answer_structure_tags=['recommend', 'motivate'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Aspects when initiating a business',
            'prompt': 'Discuss the aspects that must be considered when initiating a business (e.g. strategy, operations, productivity, size). (8 marks)',
            'marks': 8,
            'marking_points': [
                'Strategy: a long-term plan of action to achieve goals.',
                'Operations: the activities used to achieve the business\'s goals.',
                'Productivity: getting the best output per unit of input.',
                'Size of the business: scale of operations suited to demand/resources.',
                'Cost-saving and business growth must also be planned.',
            ],
            'sample_answer': 'When initiating a business, the entrepreneur must consider its strategy (a long-term plan to achieve goals), its operations (the activities used to reach those goals), its productivity (the best output per unit of input), and the size of the business (the scale of operations suited to demand and resources). Cost-saving and planned business growth should also be considered.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List and explain initiation aspects.',
                'Think strategy, operations, productivity, size.',
                'Add cost-saving and growth.',
            ),
            'answer_part_hints': ['Name each aspect.', 'Explain each.'],
            'guidelines': ['Provide at least four aspects with explanation.'],
            'teaching_note': 'Reward breadth across the initiation aspects.',
            'keywords': ['strategy', 'operations', 'productivity', 'size', 'cost-saving', 'growth'],
        }, subskill='discussion', learning_objective_id=LO_INITIATE, question_family_id='initiation_aspects_discussion', concept_id='strategy', concept_group='initiation', diagnostic_tags=['discussion', 'initiation'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Reasons businesses need funding',
            'prompt': 'Explain the reasons why businesses need funding. (6 marks)',
            'marks': 6,
            'marking_points': [
                'To buy assets/equipment and premises (start-up and capital costs).',
                'To finance day-to-day operations and working capital.',
                'To fund expansion and business growth.',
                'To cover unexpected costs and manage cash-flow gaps.',
            ],
            'sample_answer': 'Businesses need funding to buy assets, equipment and premises when starting up, to finance day-to-day operations and working capital, to fund expansion and growth, and to cover unexpected costs and bridge cash-flow gaps.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List reasons money is needed.',
                'Think assets, operations, growth and cash flow.',
                'Funding supports both start-up and ongoing needs.',
            ),
            'answer_part_hints': ['Give several reasons.', 'Explain each.'],
            'guidelines': ['Provide at least three reasons.'],
            'teaching_note': 'Reward distinct reasons across start-up and operations.',
            'keywords': ['funding', 'assets', 'equipment', 'operations', 'growth', 'cash flow'],
        }, subskill='discussion', learning_objective_id=LO_FUNDING, question_family_id='reasons_funding_discussion', concept_id='sources_of_funding', concept_group='funding', diagnostic_tags=['discussion', 'funding'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
