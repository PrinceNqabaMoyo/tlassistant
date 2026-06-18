"""Grade 12 Business Studies - Term 1 - Macro environment: Business strategies.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='macro_environment_strategies',
    curriculum_reference='Term 1 > Macro environment: Business strategies',
    id_prefix='g12_bs_strategy',
)

LO_TOOLS = 'lo_analysis_tools'
LO_STRATEGIES = 'lo_business_strategies'
LO_EVALUATION = 'lo_strategy_evaluation'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': "Porter's Five Forces",
            'prompt': "Porter's Five Forces model is mainly used to analyse the …",
            'options': ['internal/micro environment', "business's competitive position in the market", 'financial statements', 'organisational culture'],
            'correct_index': 1,
            'explanation': "Porter's Five Forces analyses the competitive strength/position of a business within its market/industry.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on competition in the market.',
                'Five forces of competition = competitive position.',
                'PESTLE looks at the macro environment instead.',
            ),
            'guidelines': ["Porter's Five Forces = competitive position."],
        }, subskill='concepts', learning_objective_id=LO_TOOLS, question_family_id='porter_definition', concept_id='porters_five_forces', concept_group='tools', misconception_tags=['confuses_porter_with_pestle'], diagnostic_tags=['definition', 'tools']),
        with_metadata({
            'title': 'PESTLE analysis',
            'prompt': 'An industrial analysis tool used to identify and evaluate factors in the macro environment is …',
            'options': ['SWOT analysis', 'PESTLE analysis', "Porter's Five Forces", 'Force Field Analysis'],
            'correct_index': 1,
            'explanation': 'PESTLE analysis identifies and evaluates the Political, Economic, Social, Technological, Legal and Environmental factors in the macro environment.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on macro-environment factors.',
                'Political/Economic/Social/etc. external factors = PESTLE.',
                'SWOT covers internal strengths/weaknesses too.',
            ),
            'guidelines': ['Macro external factors = PESTLE.'],
        }, subskill='concepts', learning_objective_id=LO_TOOLS, question_family_id='pestle_definition', concept_id='pestle_analysis', concept_group='tools', misconception_tags=['confuses_pestle_with_swot'], diagnostic_tags=['definition', 'tools']),
        with_metadata({
            'title': 'SWOT analysis',
            'prompt': 'In a SWOT analysis, opportunities and threats refer to factors that are …',
            'options': ['internal to the business', 'external to the business', 'always negative', 'only financial'],
            'correct_index': 1,
            'explanation': 'In SWOT, strengths and weaknesses are internal, while opportunities and threats are external factors.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recall the four parts of SWOT.',
                'Opportunities/threats sit outside the business = external.',
                'Strengths/weaknesses are internal.',
            ),
            'guidelines': ['Opportunities/threats = external.'],
        }, subskill='concepts', learning_objective_id=LO_TOOLS, question_family_id='swot_definition', concept_id='swot_analysis', concept_group='tools', diagnostic_tags=['definition', 'tools']),
        with_metadata({
            'title': 'Integration strategy',
            'prompt': 'A business that takes over its supplier up the supply chain is using …',
            'options': ['forward vertical integration', 'backward vertical integration', 'market penetration', 'divestiture'],
            'correct_index': 1,
            'explanation': 'Backward vertical integration is when a business merges with/takes over its suppliers up the supply chain.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Think about direction along the supply chain.',
                'Taking over suppliers (upstream) = backward vertical integration.',
                'Taking over distributors (downstream) = forward integration.',
            ),
            'guidelines': ['Taking over suppliers = backward vertical integration.'],
        }, subskill='concepts', learning_objective_id=LO_STRATEGIES, question_family_id='integration_identify', concept_id='backward_vertical_integration', concept_group='strategies', misconception_tags=['confuses_backward_with_forward_integration'], diagnostic_tags=['identification', 'strategies']),
        with_metadata({
            'title': 'Intensive strategy',
            'prompt': 'Selling existing products into the existing market to increase market share is called …',
            'options': ['market development', 'market penetration', 'product development', 'diversification'],
            'correct_index': 1,
            'explanation': 'Market penetration focuses on selling existing products into the existing market to increase market share.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Same product, same market.',
                'Existing product + existing market = market penetration.',
                'New markets = market development.',
            ),
            'guidelines': ['Existing product, existing market = market penetration.'],
        }, subskill='concepts', learning_objective_id=LO_STRATEGIES, question_family_id='intensive_identify', concept_id='market_penetration', concept_group='strategies', misconception_tags=['confuses_penetration_with_development'], diagnostic_tags=['identification', 'strategies']),
        with_metadata({
            'title': 'Defensive strategy',
            'prompt': 'A struggling business sells off a division that is no longer profitable. This defensive strategy is …',
            'options': ['divestiture', 'market penetration', 'concentric diversification', 'horizontal integration'],
            'correct_index': 0,
            'explanation': 'Divestiture/divestment is the disposal/selling of assets or divisions that are no longer profitable or relevant.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on selling off a division.',
                'Selling unprofitable divisions = divestiture.',
                'Liquidation is selling all assets to pay creditors.',
            ),
            'guidelines': ['Selling unprofitable divisions = divestiture.'],
        }, subskill='concepts', learning_objective_id=LO_STRATEGIES, question_family_id='defensive_identify', concept_id='divestiture', concept_group='strategies', misconception_tags=['confuses_divestiture_with_liquidation'], diagnostic_tags=['identification', 'strategies']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': "Apply Porter's Five Forces",
            'prompt': "A new coffee chain wants to assess its competitive position. Advise it on how it could apply Porter's Five Forces model. (4 marks)",
            'marks': 4,
            'marking_points': [
                'Assess the power of buyers (ability of customers to push prices down).',
                'Assess the power of suppliers (ability of suppliers to raise input prices).',
                'Assess the threat of new entrants and barriers to entry.',
                'Assess the threat of substitutes and rivalry among existing competitors.',
            ],
            'sample_answer': "The coffee chain should assess the power of buyers and suppliers, the threat of new entrants (and the barriers to entry), the threat of substitute products, and the rivalry among existing competitors. Analysing these five forces shows how strong its competitive position is and where it should focus.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List and apply the five forces.',
                'Buyers, suppliers, new entrants, substitutes, rivalry.',
                'Tie each force to the coffee market.',
            ),
            'answer_part_hints': ['Name the forces.', 'Apply them to the scenario.'],
            'guidelines': ['Cover the five forces applied to the scenario.'],
            'teaching_note': 'Reward the five forces applied to the coffee chain.',
            'keywords': ['buyers', 'suppliers', 'new entrants', 'substitutes', 'rivalry'],
        }, subskill='application', learning_objective_id=LO_TOOLS, question_family_id='apply_porter_scenario', concept_id='porters_five_forces', concept_group='tools', scenario_family_id='coffee_chain', diagnostic_tags=['scenario_analysis', 'tools'], answer_structure_tags=['apply', 'list'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Recommend a strategy',
            'prompt': 'A clothing business wants to grow by selling its current product range in new provinces. Identify the most suitable business strategy and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The strategy is market development (an intensive strategy).',
                'It sells existing products in new markets/geographical areas.',
                'It lets the business grow without developing new products.',
                'It increases sales and market share in new regions.',
            ],
            'sample_answer': 'The business should use market development, an intensive strategy, because it sells its existing products in new geographical areas (provinces). This lets it grow and increase sales and market share without the cost and risk of developing new products.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match existing product + new market to a strategy.',
                'Existing products in new areas = market development.',
                'Motivate why it fits the growth goal.',
            ),
            'answer_part_hints': ['Name the strategy.', 'Motivate the choice.'],
            'guidelines': ['Identify market development and motivate.'],
            'teaching_note': 'Reward market development with a motivation.',
            'keywords': ['market development', 'existing products', 'new markets', 'growth'],
        }, subskill='application', learning_objective_id=LO_STRATEGIES, question_family_id='recommend_strategy_scenario', concept_id='market_development', concept_group='strategies', scenario_family_id='clothing_growth', diagnostic_tags=['scenario_analysis', 'strategies'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Diversification strategies',
            'prompt': 'Explain the different types of diversification strategies a business could use to grow. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Concentric diversification: add new products related to existing ones to appeal to new customers.',
                'Horizontal diversification: add new, unrelated products that appeal to existing customers.',
                'Conglomerate diversification: add new, unrelated products that appeal to new customers.',
                'Diversification spreads risk across products/markets.',
                'It can open new revenue streams and reduce dependence on one product.',
            ],
            'sample_answer': 'Concentric diversification adds new products related to existing ones to appeal to new customers, horizontal diversification adds unrelated products aimed at existing customers, and conglomerate diversification adds unrelated products aimed at new customers. Diversification spreads risk, opens new revenue streams and reduces dependence on a single product or market.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Distinguish the three diversification types.',
                'Think related vs unrelated products and existing vs new customers.',
                'Explain why a business diversifies.',
            ),
            'answer_part_hints': ['Name each type.', 'Explain each.'],
            'guidelines': ['Cover concentric, horizontal and conglomerate.'],
            'teaching_note': 'Reward correct distinction of the three types.',
            'keywords': ['concentric', 'horizontal', 'conglomerate', 'unrelated', 'risk'],
        }, subskill='discussion', learning_objective_id=LO_STRATEGIES, question_family_id='diversification_discussion', concept_id='diversification_strategies', concept_group='strategies', diagnostic_tags=['discussion', 'strategies'], answer_structure_tags=['explain', 'list'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Steps in strategy evaluation',
            'prompt': 'Advise a business on the steps it should follow in strategy evaluation. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Examine the underlying bases/assumptions of the strategy.',
                'Look forward and backward at the implementation process.',
                'Compare expected with actual performance (measure performance).',
                'Take corrective action where necessary.',
                'Set specific dates for control and follow-up.',
            ],
            'sample_answer': 'The business should examine the underlying bases of its strategy, look forward and backward at the implementation process, and compare expected with actual performance. It must then take corrective action where necessary, set specific dates for control and follow-up, and decide on the desired outcome.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List the evaluation steps in order.',
                'Examine bases, review implementation, measure, correct, follow up.',
                'End by deciding on the desired outcome.',
            ),
            'answer_part_hints': ['Name each step.', 'Keep them in order.'],
            'guidelines': ['Provide the strategy-evaluation steps.'],
            'teaching_note': 'Reward correct evaluation steps.',
            'keywords': ['bases', 'implementation', 'compare performance', 'corrective action', 'follow-up'],
        }, subskill='discussion', learning_objective_id=LO_EVALUATION, question_family_id='strategy_evaluation_discussion', concept_id='strategy_evaluation', concept_group='evaluation', diagnostic_tags=['discussion', 'process'], answer_structure_tags=['list', 'sequence'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
