"""Grade 11 Business Studies - Term 2 - Topic 10: The marketing function.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='marketing_function',
    curriculum_reference='Term 2 > The marketing function',
    id_prefix='g11_bs_marketing',
)

LO_MARKETING = 'lo_marketing_meaning_activities'
LO_PRODUCT = 'lo_product_policy'
LO_PRICE = 'lo_pricing_policy'
LO_DISTRIBUTION = 'lo_distribution'
LO_COMMUNICATION = 'lo_marketing_communication'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Marketing',
            'prompt': 'The activities a company undertakes to promote the buying or selling of a product or service is called …',
            'options': ['production', 'marketing', 'distribution', 'financing'],
            'correct_index': 1,
            'explanation': 'Marketing is the activities a company undertakes to promote the buying or selling of a product or service.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify promoting buying/selling.',
                'Marketing promotes the buying and selling of products.',
                'Distribution is only how products reach customers.',
            ),
            'guidelines': ['Link "promote buying/selling" to marketing.'],
        }, subskill='concepts', learning_objective_id=LO_MARKETING, question_family_id='marketing_definition', concept_id='marketing', concept_group='marketing', misconception_tags=['confuses_marketing_with_distribution'], diagnostic_tags=['definition', 'marketing']),
        with_metadata({
            'title': 'Marketing activity (risk bearing)',
            'prompt': 'A wholesaler carries the risk that stock may be damaged or unsold. Which marketing activity is this?',
            'options': ['storage', 'risk bearing', 'standardisation', 'transport'],
            'correct_index': 1,
            'explanation': 'Risk bearing is the marketing activity where the business carries the risk of goods being damaged, stolen or unsold.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the action to a marketing activity.',
                'Carrying the risk of loss/unsold goods = risk bearing.',
                'Storage is keeping goods until needed; transport is moving them.',
            ),
            'guidelines': ['Carrying risk = risk bearing.'],
        }, subskill='concepts', learning_objective_id=LO_MARKETING, question_family_id='marketing_activity_risk', concept_id='risk_bearing', concept_group='marketing_activities', misconception_tags=['confuses_risk_with_storage'], diagnostic_tags=['classification', 'marketing']),
        with_metadata({
            'title': 'Product policy',
            'prompt': 'The component of the marketing mix that explains how a business develops a new product\'s design and packaging is the …',
            'options': ['pricing policy', 'product policy', 'distribution policy', 'communication policy'],
            'correct_index': 1,
            'explanation': 'The product policy is the first component of the marketing mix; it explains how a business develops a product\'s design and packaging.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the design/packaging component.',
                'Product policy covers product, design and packaging.',
                'Pricing policy is about setting prices.',
            ),
            'guidelines': ['Design/packaging = product policy.'],
        }, subskill='concepts', learning_objective_id=LO_PRODUCT, question_family_id='product_policy_definition', concept_id='product_policy', concept_group='product', misconception_tags=['confuses_product_with_price'], diagnostic_tags=['definition', 'product']),
        with_metadata({
            'title': 'Pricing technique (skimming)',
            'prompt': 'A firm charges the highest initial price customers will pay for a new gadget, then lowers it over time. This pricing technique is …',
            'options': ['penetration pricing', 'skimming', 'bait pricing', 'cost-based pricing'],
            'correct_index': 1,
            'explanation': 'Skimming is when a firm charges the highest initial price customers will pay and then lowers it over time.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the tactic to the technique.',
                'High initial price, lowered over time = skimming.',
                'Penetration pricing starts low to win market share.',
            ),
            'guidelines': ['High-then-lower price = skimming.'],
        }, subskill='concepts', learning_objective_id=LO_PRICE, question_family_id='pricing_technique_skimming', concept_id='skimming', concept_group='pricing', misconception_tags=['confuses_skimming_with_penetration'], diagnostic_tags=['classification', 'pricing']),
        with_metadata({
            'title': 'Pricing technique (penetration)',
            'prompt': 'A new brand sets a very low price to quickly attract customers and gain market share. This technique is …',
            'options': ['skimming', 'penetration pricing', 'psychological pricing', 'mark-up pricing'],
            'correct_index': 1,
            'explanation': 'Penetration pricing sets a low initial price to penetrate the market and gain market share quickly.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the tactic to the technique.',
                'Low price to win market share fast = penetration pricing.',
                'Skimming starts high and lowers over time.',
            ),
            'guidelines': ['Low price to gain share = penetration.'],
        }, subskill='concepts', learning_objective_id=LO_PRICE, question_family_id='pricing_technique_penetration', concept_id='penetration_pricing', concept_group='pricing', misconception_tags=['confuses_penetration_with_skimming'], diagnostic_tags=['classification', 'pricing']),
        with_metadata({
            'title': 'Direct vs indirect distribution',
            'prompt': 'When a manufacturer sells directly to consumers with no intermediaries, this is a … channel of distribution.',
            'options': ['indirect', 'direct', 'reverse', 'horizontal'],
            'correct_index': 1,
            'explanation': 'A direct channel of distribution is when the manufacturer sells directly to consumers without intermediaries.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Count the intermediaries.',
                'No intermediaries = direct channel.',
                'Indirect channels use wholesalers/retailers.',
            ),
            'guidelines': ['No middlemen = direct.'],
        }, subskill='concepts', learning_objective_id=LO_DISTRIBUTION, question_family_id='direct_channel_definition', concept_id='direct_distribution', concept_group='distribution', misconception_tags=['confuses_direct_with_indirect'], diagnostic_tags=['definition', 'distribution']),
        with_metadata({
            'title': 'Intermediaries',
            'prompt': 'Wholesalers and retailers that help move goods from producers to consumers are called …',
            'options': ['intermediaries', 'manufacturers', 'consumers', 'regulators'],
            'correct_index': 0,
            'explanation': 'Intermediaries (e.g. wholesalers and retailers) are the businesses that help move goods from producers to consumers in indirect distribution.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the middlemen.',
                'Wholesalers/retailers between producer and consumer = intermediaries.',
                'They are used in indirect channels of distribution.',
            ),
            'guidelines': ['Middlemen = intermediaries.'],
        }, subskill='concepts', learning_objective_id=LO_DISTRIBUTION, question_family_id='intermediaries_definition', concept_id='intermediaries', concept_group='distribution', misconception_tags=['confuses_intermediary_with_producer'], diagnostic_tags=['definition', 'distribution']),
        with_metadata({
            'title': 'Marketing communication component (publicity)',
            'prompt': 'A favourable press release about a business that the business does not pay for is an example of …',
            'options': ['advertising', 'publicity', 'personal selling', 'sales promotion'],
            'correct_index': 1,
            'explanation': 'Publicity is unpaid promotion (e.g. a press release covered by the media), unlike advertising which is paid for.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Note whether it is paid for.',
                'Unpaid media coverage = publicity.',
                'Advertising is paid; personal selling is face-to-face.',
            ),
            'guidelines': ['Unpaid media coverage = publicity.'],
        }, subskill='concepts', learning_objective_id=LO_COMMUNICATION, question_family_id='publicity_definition', concept_id='publicity', concept_group='communication', misconception_tags=['confuses_publicity_with_advertising'], diagnostic_tags=['classification', 'communication']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Identify the pricing technique',
            'prompt': 'A clothing store prices a jacket at R299,99 instead of R300 to make it feel cheaper. Identify the pricing technique and explain why it works. (4 marks)',
            'marks': 4,
            'marking_points': [
                'This is psychological pricing.',
                'R299,99 feels meaningfully cheaper than R300 to customers.',
                'It influences customer perception of value.',
                'It can increase sales by making the price seem lower.',
            ],
            'sample_answer': 'This is psychological pricing. Pricing the jacket at R299,99 instead of R300 makes it feel cheaper to customers, influencing their perception of value and encouraging more sales.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the tactic to a technique.',
                'Prices ending in ,99 target perception = psychological pricing.',
                'It works on how customers perceive the price.',
            ),
            'answer_part_hints': ['Name the technique.', 'Explain why it works.'],
            'guidelines': ['Identify and justify.'],
            'teaching_note': 'Reward correct technique plus an explanation of perception.',
            'keywords': ['psychological pricing', 'perception', 'cheaper', 'value', 'sales'],
        }, subskill='application', learning_objective_id=LO_PRICE, question_family_id='identify_pricing_scenario', concept_id='psychological_pricing', concept_group='pricing', scenario_family_id='jacket_pricing', diagnostic_tags=['scenario_analysis', 'pricing'], answer_structure_tags=['identify', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Choose a distribution channel',
            'prompt': 'A small farmer sells fresh vegetables to local households at a weekly market stall. Identify the distribution channel used and give ONE reason it suits the business. (4 marks)',
            'marks': 4,
            'marking_points': [
                'This is a direct channel of distribution.',
                'The farmer sells directly to consumers with no intermediaries.',
                'Reason: keeps prices lower / higher profit (no middlemen).',
                'Reason: direct contact with customers/fresh produce.',
            ],
            'sample_answer': 'This is a direct channel of distribution because the farmer sells vegetables directly to households with no intermediaries. It suits the business because removing middlemen keeps prices lower and profit higher, and allows direct contact with customers for fresh produce.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Decide if intermediaries are used.',
                'Selling straight to consumers = direct channel.',
                'Direct channels avoid middlemen costs.',
            ),
            'answer_part_hints': ['Name the channel.', 'Give one reason it suits the business.'],
            'guidelines': ['Use scenario evidence.'],
            'teaching_note': 'Reward correct channel plus a relevant reason.',
            'keywords': ['direct', 'channel', 'no intermediaries', 'profit', 'consumers', 'fresh'],
        }, subskill='application', learning_objective_id=LO_DISTRIBUTION, question_family_id='choose_channel_scenario', concept_id='direct_distribution', concept_group='distribution', scenario_family_id='farmer_market_stall', diagnostic_tags=['scenario_analysis', 'distribution'], answer_structure_tags=['identify', 'justify'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Marketing activities',
            'prompt': 'Discuss the marketing activities a business performs (e.g. standardisation and grading, storage, transport, financing, risk bearing, buying and selling). (8 marks)',
            'marks': 8,
            'marking_points': [
                'Standardisation and grading: sorting products into uniform quality classes.',
                'Storage: keeping goods safely until they are needed/sold.',
                'Transport: moving goods from producers to consumers.',
                'Financing: providing/obtaining funds to carry out marketing.',
                'Risk bearing: carrying the risk of goods being damaged or unsold.',
                'Buying and selling: acquiring goods and selling them to customers.',
            ],
            'sample_answer': 'Marketing activities include standardisation and grading (sorting products into uniform quality classes), storage (keeping goods until needed), transport (moving goods to consumers), financing (providing funds for marketing), risk bearing (carrying the risk of damage or unsold stock), and buying and selling (acquiring and selling goods to customers).',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List and explain the marketing activities.',
                'Use the curriculum list of six activities.',
                'Give a short explanation of each activity.',
            ),
            'answer_part_hints': ['Name each activity.', 'Explain each briefly.'],
            'guidelines': ['Provide at least four activities with explanation.'],
            'teaching_note': 'Reward breadth across the activity list plus explanation.',
            'keywords': ['standardisation', 'grading', 'storage', 'transport', 'financing', 'risk bearing', 'buying', 'selling'],
        }, subskill='discussion', learning_objective_id=LO_MARKETING, question_family_id='marketing_activities_discussion', concept_id='marketing_activities', concept_group='marketing_activities', diagnostic_tags=['discussion', 'marketing'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Components of marketing communication',
            'prompt': 'Discuss the components of the marketing communication policy (sales promotion, advertising, publicity and personal selling). (8 marks)',
            'marks': 8,
            'marking_points': [
                'Advertising: paid, non-personal promotion through media.',
                'Sales promotion: short-term incentives (discounts, samples) to boost sales.',
                'Publicity: unpaid promotion through media coverage/press releases (PR).',
                'Personal selling: face-to-face selling that builds relationships and closes sales.',
            ],
            'sample_answer': 'The marketing communication policy has four components. Advertising is paid, non-personal promotion through media. Sales promotion uses short-term incentives such as discounts and samples to boost sales. Publicity is unpaid promotion through media coverage and press releases (public relations). Personal selling is face-to-face selling that builds relationships and closes sales.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain each communication component.',
                'Distinguish paid (advertising) from unpaid (publicity).',
                'Personal selling is face-to-face; sales promotion is short-term incentives.',
            ),
            'answer_part_hints': ['Name each component.', 'Explain each.'],
            'guidelines': ['Cover all four components.'],
            'teaching_note': 'Reward distinct, accurate explanations of each component.',
            'keywords': ['advertising', 'sales promotion', 'publicity', 'personal selling', 'media', 'public relations'],
        }, subskill='discussion', learning_objective_id=LO_COMMUNICATION, question_family_id='communication_components_discussion', concept_id='communication', concept_group='communication', diagnostic_tags=['discussion', 'communication'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Importance of trademarks',
            'prompt': 'Explain the importance of trademarks to businesses and consumers. (6 marks)',
            'marks': 6,
            'marking_points': [
                'For business: identifies and distinguishes the brand from competitors.',
                'For business: builds brand loyalty and protects against imitation.',
                'For consumers: assures consistent quality and origin.',
                'For consumers: makes products easy to recognise and trust.',
            ],
            'sample_answer': 'Trademarks help businesses identify and distinguish their brand from competitors, build brand loyalty and protect against imitation. For consumers, a trademark assures consistent quality and origin and makes products easy to recognise and trust.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Cover both business and consumer benefits.',
                'For business: identity, loyalty, protection.',
                'For consumers: recognition, quality assurance, trust.',
            ),
            'answer_part_hints': ['Give business benefits.', 'Give consumer benefits.'],
            'guidelines': ['Address both businesses and consumers.'],
            'teaching_note': 'Reward coverage of both perspectives.',
            'keywords': ['trademark', 'brand', 'loyalty', 'recognise', 'quality', 'trust'],
        }, subskill='discussion', learning_objective_id=LO_PRODUCT, question_family_id='importance_of_trademarks_discussion', concept_id='trademarks', concept_group='product', diagnostic_tags=['discussion', 'product'], answer_structure_tags=['explain', 'two_perspectives'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
