"""Grade 12 Business Studies - Term 3 - Social responsibility and corporate citizenship.

Covers social responsibility, the triple bottom line, socio-economic issues, CSR and CSI.
Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='social_responsibility_csr_csi',
    curriculum_reference='Term 3 > Social responsibility and corporate citizenship: CSR & CSI',
    id_prefix='g12_bs_csr',
)

LO_SR = 'lo_social_responsibility'
LO_ISSUES = 'lo_socio_economic_issues'
LO_CSR_CSI = 'lo_csr_csi'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Social responsibility',
            'prompt': 'A business\u2019s obligation to act in ways that benefit society and the environment, not just profit, is …',
            'options': ['social responsibility', 'corporate governance', 'market penetration', 'liquidation'],
            'correct_index': 0,
            'explanation': 'Social responsibility is a business\u2019s obligation to act in ways that benefit society and the environment, beyond just making a profit.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on benefiting society and the environment.',
                'Acting for society/environment = social responsibility.',
                'Corporate governance is about ethical leadership.',
            ),
            'guidelines': ['Acting for society/environment = social responsibility.'],
        }, subskill='concepts', learning_objective_id=LO_SR, question_family_id='sr_definition', concept_id='social_responsibility', concept_group='sr', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Triple bottom line',
            'prompt': 'The triple bottom line measures a business\u2019s performance in terms of …',
            'options': [
                'profit only',
                'people, planet and profit',
                'price, place and promotion',
                'plan, do and check',
            ],
            'correct_index': 1,
            'explanation': 'The triple bottom line measures performance in terms of people (social), planet (environmental) and profit (economic).',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recall the three Ps.',
                'People, planet, profit = triple bottom line.',
                'Price/place/promotion are marketing Ps.',
            ),
            'guidelines': ['People, planet, profit = triple bottom line.'],
        }, subskill='concepts', learning_objective_id=LO_SR, question_family_id='triple_bottom_line_identify', concept_id='triple_bottom_line', concept_group='sr', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'CSR vs CSI',
            'prompt': 'Programmes that are part of the business\u2019s core strategy and may benefit the business (e.g. ethical sourcing) describe …',
            'options': ['CSI', 'CSR', 'TQM', 'BBBEE'],
            'correct_index': 1,
            'explanation': 'CSR (Corporate Social Responsibility) is part of the business\u2019s core strategy and may benefit the business, while CSI focuses on uplifting communities with no direct business benefit.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on core strategy that may benefit the business.',
                'Core, strategic, may benefit business = CSR.',
                'CSI uplifts communities with no direct benefit.',
            ),
            'guidelines': ['Strategic, may benefit business = CSR.'],
        }, subskill='concepts', learning_objective_id=LO_CSR_CSI, question_family_id='csr_identify', concept_id='csr', concept_group='csr_csi', misconception_tags=['confuses_csr_with_csi'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'CSI',
            'prompt': 'A business funding a school in a poor community, with no direct benefit to itself, is an example of …',
            'options': ['CSR', 'CSI', 'market development', 'a dividend'],
            'correct_index': 1,
            'explanation': 'CSI (Corporate Social Investment) focuses on uplifting communities, typically with no direct benefit to the business, e.g. funding a school.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on uplifting the community with no direct benefit.',
                'Community upliftment, no direct benefit = CSI.',
                'CSR is part of core strategy and may benefit the business.',
            ),
            'guidelines': ['Community upliftment, no direct benefit = CSI.'],
        }, subskill='concepts', learning_objective_id=LO_CSR_CSI, question_family_id='csi_identify', concept_id='csi', concept_group='csr_csi', misconception_tags=['confuses_csi_with_csr'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Socio-economic issue',
            'prompt': 'Which of the following is a socio-economic issue a business can help address?',
            'options': ['Unemployment', 'Vertical integration', 'Compound interest', 'Market share'],
            'correct_index': 0,
            'explanation': 'Socio-economic issues include HIV/AIDS, unemployment and poverty, which businesses can help address.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recall the socio-economic issues.',
                'Unemployment is a socio-economic issue.',
                'Integration/interest are business finance terms.',
            ),
            'guidelines': ['Unemployment = a socio-economic issue.'],
        }, subskill='concepts', learning_objective_id=LO_ISSUES, question_family_id='socio_issue_identify', concept_id='unemployment', concept_group='issues', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Component of CSR',
            'prompt': 'Treating employees fairly and providing safe working conditions is part of which CSR focus?',
            'options': ['Ethical responsibility towards employees', 'Tax evasion', 'Market penetration', 'Liquidation'],
            'correct_index': 0,
            'explanation': 'CSR includes ethical responsibility towards employees, such as fair treatment and safe working conditions.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on responsibility towards employees.',
                'Fair treatment/safe conditions = ethical responsibility to employees.',
                'Tax evasion is unethical, not CSR.',
            ),
            'guidelines': ['Fair treatment of employees = a CSR component.'],
        }, subskill='concepts', learning_objective_id=LO_CSR_CSI, question_family_id='csr_component_identify', concept_id='csr', concept_group='csr_csi', diagnostic_tags=['identification']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Address a socio-economic issue',
            'prompt': 'High unemployment affects the community where a business operates. Recommend ways the business could help address unemployment. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Create jobs by expanding operations and hiring locally.',
                'Offer learnerships, internships and skills training.',
                'Support small/local businesses and suppliers (enterprise development).',
                'Partner with government/NGOs on job-creation projects.',
            ],
            'sample_answer': 'The business could help address unemployment by creating jobs through expansion and hiring locally, offering learnerships, internships and skills training, and supporting small local businesses and suppliers. It could also partner with government or NGOs on job-creation projects.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on creating jobs and skills.',
                'Hire locally, train, support small business, partner.',
                'Tie each to reducing unemployment.',
            ),
            'answer_part_hints': ['Give recommendations.', 'Explain each.'],
            'guidelines': ['Provide ways to address unemployment.'],
            'teaching_note': 'Reward practical ways to address unemployment.',
            'keywords': ['create jobs', 'learnerships', 'training', 'small business', 'partner'],
        }, subskill='application', learning_objective_id=LO_ISSUES, question_family_id='address_issue_scenario', concept_id='unemployment', concept_group='issues', scenario_family_id='community_unemployment', diagnostic_tags=['scenario_analysis', 'issues'], answer_structure_tags=['recommend'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Identify CSR vs CSI',
            'prompt': 'A company (a) ensures fair wages and safe conditions for staff, and (b) builds a clinic in a rural village. Classify each as CSR or CSI and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                '(a) Fair wages and safe conditions = CSR (part of core operations/strategy).',
                'CSR can benefit the business through motivated, productive staff.',
                '(b) Building a clinic = CSI (community upliftment).',
                'CSI has no direct benefit to the business.',
            ],
            'sample_answer': 'Ensuring fair wages and safe conditions for staff is CSR because it is part of the company\u2019s core operations and can benefit the business through motivated, productive staff. Building a clinic in a rural village is CSI because it uplifts the community with no direct benefit to the business.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Classify each action.',
                'Core/strategic = CSR; community upliftment = CSI.',
                'Motivate each classification.',
            ),
            'answer_part_hints': ['Classify each.', 'Motivate each.'],
            'guidelines': ['Classify both and motivate.'],
            'teaching_note': 'Reward correct CSR/CSI classification with motivation.',
            'keywords': ['CSR', 'core', 'CSI', 'community', 'no direct benefit'],
        }, subskill='application', learning_objective_id=LO_CSR_CSI, question_family_id='classify_csr_csi_scenario', concept_id='csr', concept_group='csr_csi', scenario_family_id='wages_clinic', diagnostic_tags=['scenario_analysis', 'csr_csi'], answer_structure_tags=['classify', 'motivate'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Impact of CSR',
            'prompt': 'Discuss the impact of CSR programmes on businesses and communities. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Improves the business\u2019s reputation and brand image.',
                'Builds customer loyalty and can increase sales.',
                'Improves relationships with the community and stakeholders.',
                'Communities benefit from upliftment, jobs and development.',
                'CSR programmes can be costly and reduce short-term profits.',
            ],
            'sample_answer': 'CSR improves the business\u2019s reputation and brand image, builds customer loyalty and can increase sales, and improves relationships with the community and stakeholders. Communities benefit from upliftment, jobs and development. However, CSR programmes can be costly and may reduce short-term profits.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Cover impact on business and community.',
                'Reputation/loyalty (business) and upliftment (community).',
                'Mention the cost as a drawback.',
            ),
            'answer_part_hints': ['Impact on business.', 'Impact on community.'],
            'guidelines': ['Cover both business and community impact.'],
            'teaching_note': 'Reward impact on both business and community.',
            'keywords': ['reputation', 'loyalty', 'community', 'upliftment', 'cost'],
        }, subskill='discussion', learning_objective_id=LO_CSR_CSI, question_family_id='csr_impact_discussion', concept_id='csr', concept_group='csr_csi', diagnostic_tags=['discussion', 'evaluation'], answer_structure_tags=['positives', 'negatives'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Social responsibility and the triple bottom line',
            'prompt': 'Explain the link between social responsibility and the triple bottom line. (6 marks)',
            'marks': 6,
            'marking_points': [
                'The triple bottom line measures people, planet and profit.',
                'Social responsibility addresses the people (social) element.',
                'It also addresses the planet (environmental) element.',
                'Acting responsibly supports long-term profit (economic) sustainability.',
                'Together they balance social, environmental and economic goals.',
            ],
            'sample_answer': 'The triple bottom line measures a business on people, planet and profit. Social responsibility addresses the people element through fair treatment and community upliftment and the planet element through environmental care, which in turn supports long-term profit sustainability. Together, social responsibility and the triple bottom line help the business balance social, environmental and economic goals.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Connect social responsibility to people/planet/profit.',
                'Social responsibility covers people and planet.',
                'Link to long-term profit and balance.',
            ),
            'answer_part_hints': ['Explain the triple bottom line.', 'Link social responsibility.'],
            'guidelines': ['Explain the link clearly.'],
            'teaching_note': 'Reward linking social responsibility to all three elements.',
            'keywords': ['people', 'planet', 'profit', 'social', 'sustainability'],
        }, subskill='discussion', learning_objective_id=LO_SR, question_family_id='sr_tbl_discussion', concept_id='triple_bottom_line', concept_group='sr', diagnostic_tags=['discussion'], answer_structure_tags=['explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
