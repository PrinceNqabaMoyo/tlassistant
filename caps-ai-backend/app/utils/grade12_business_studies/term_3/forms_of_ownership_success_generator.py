"""Grade 12 Business Studies - Term 3 - Forms of ownership: success and/or failure.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='forms_of_ownership_success',
    curriculum_reference='Term 3 > Forms of ownership: Criteria for success and/or failure',
    id_prefix='g12_bs_ownership',
)

LO_FORMS = 'lo_forms_of_ownership'
LO_LIABILITY = 'lo_liability'
LO_CRITERIA = 'lo_success_criteria'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Limited liability',
            'prompt': 'When shareholders can only lose the amount they invested, the business has …',
            'options': ['unlimited liability', 'limited liability', 'no liability', 'joint liability'],
            'correct_index': 1,
            'explanation': 'Limited liability means owners/shareholders can only lose the amount they invested; their personal assets are protected.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on losing only the investment.',
                'Lose only what you invested = limited liability.',
                'Unlimited liability puts personal assets at risk.',
            ),
            'guidelines': ['Lose only the investment = limited liability.'],
        }, subskill='concepts', learning_objective_id=LO_LIABILITY, question_family_id='limited_liability_definition', concept_id='limited_liability', concept_group='liability', misconception_tags=['confuses_limited_with_unlimited'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Unlimited liability',
            'prompt': 'A sole trader whose personal assets can be used to pay business debts has …',
            'options': ['limited liability', 'unlimited liability', 'shared liability', 'no liability'],
            'correct_index': 1,
            'explanation': 'Unlimited liability means the owner is personally responsible for all business debts, so personal assets can be used to settle them.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on personal assets being at risk.',
                'Personal assets pay debts = unlimited liability.',
                'Limited liability protects personal assets.',
            ),
            'guidelines': ['Personal assets at risk = unlimited liability.'],
        }, subskill='concepts', learning_objective_id=LO_LIABILITY, question_family_id='unlimited_liability_definition', concept_id='unlimited_liability', concept_group='liability', misconception_tags=['confuses_unlimited_with_limited'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Private company',
            'prompt': 'A form of ownership whose name ends in (Pty) Ltd, with limited liability and a separate legal personality, is a …',
            'options': ['sole trader', 'partnership', 'private company', 'close corporation'],
            'correct_index': 2,
            'explanation': 'A private company (Pty) Ltd has limited liability, a separate legal personality and continuity, and is owned by shareholders.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on (Pty) Ltd.',
                '(Pty) Ltd with limited liability = private company.',
                'A sole trader is owned by one person.',
            ),
            'guidelines': ['(Pty) Ltd = private company.'],
        }, subskill='concepts', learning_objective_id=LO_FORMS, question_family_id='private_company_identify', concept_id='private_company', concept_group='forms', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Continuity',
            'prompt': 'The ability of a business to continue to exist even if ownership changes is called …',
            'options': ['liability', 'continuity', 'liquidity', 'capital'],
            'correct_index': 1,
            'explanation': 'Continuity is the ability of a business to continue to exist even if there is a change of ownership.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on the business continuing despite ownership change.',
                'Continues despite ownership change = continuity.',
                'Liability is about responsibility for debts.',
            ),
            'guidelines': ['Continues despite ownership change = continuity.'],
        }, subskill='concepts', learning_objective_id=LO_FORMS, question_family_id='continuity_definition', concept_id='continuity', concept_group='forms', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Criterion: capital',
            'prompt': 'A company can raise large amounts of capital by issuing shares. This relates to which success criterion?',
            'options': ['Capital', 'Division of profits', 'Tax implications', 'Management'],
            'correct_index': 0,
            'explanation': 'The ability to raise funds (e.g. by issuing shares) relates to the capital criterion for success.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on raising funds.',
                'Raising funds/shares = capital criterion.',
                'Division of profits is about sharing profit.',
            ),
            'guidelines': ['Raising funds = capital criterion.'],
        }, subskill='concepts', learning_objective_id=LO_CRITERIA, question_family_id='capital_criterion_identify', concept_id='capital', concept_group='criteria', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Sole trader',
            'prompt': 'A business owned and controlled by one person with unlimited liability is a …',
            'options': ['private company', 'partnership', 'sole trader', 'public company'],
            'correct_index': 2,
            'explanation': 'A sole trader is owned and controlled by one person who has unlimited liability for the business\u2019s debts.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on one owner with unlimited liability.',
                'One owner, unlimited liability = sole trader.',
                'A partnership has 2+ owners.',
            ),
            'guidelines': ['One owner, unlimited liability = sole trader.'],
        }, subskill='concepts', learning_objective_id=LO_FORMS, question_family_id='sole_trader_identify', concept_id='sole_trader', concept_group='forms', diagnostic_tags=['identification']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Recommend a form of ownership',
            'prompt': 'Two friends want to start a business together, share profits and limit their personal risk. Recommend a suitable form of ownership and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend a private company (Pty) Ltd.',
                'It offers limited liability, protecting their personal assets.',
                'It has a separate legal personality and continuity.',
                'It can raise more capital and they can share profits as shareholders.',
            ],
            'sample_answer': 'They should form a private company (Pty) Ltd because it offers limited liability that protects their personal assets, has a separate legal personality and continuity, and can raise more capital. As shareholders they can also share the profits according to their shareholding.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match limited risk + shared ownership to a form.',
                'Limited liability + shared ownership = private company.',
                'Motivate with liability, continuity and capital.',
            ),
            'answer_part_hints': ['Name the form.', 'Motivate the choice.'],
            'guidelines': ['Recommend a form and motivate.'],
            'teaching_note': 'Reward a suitable form with a motivation.',
            'keywords': ['private company', 'limited liability', 'legal personality', 'continuity', 'capital'],
        }, subskill='application', learning_objective_id=LO_FORMS, question_family_id='recommend_form_scenario', concept_id='private_company', concept_group='forms', scenario_family_id='two_friends', diagnostic_tags=['scenario_analysis'], answer_structure_tags=['recommend', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Criteria and success',
            'prompt': 'Explain how the criteria of capital and management could contribute to the success of a private company. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Capital: a company can raise large amounts by issuing shares, funding growth.',
                'Access to capital improves its chances of survival and expansion.',
                'Management: directors and professional managers bring expertise.',
                'Good management leads to better decisions and performance.',
            ],
            'sample_answer': 'A private company can raise large amounts of capital by issuing shares, which funds growth and improves its chances of survival and expansion. It is also run by directors and professional managers whose expertise leads to better decisions and performance, both of which contribute to the success of the business.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Link each criterion to success.',
                'Capital funds growth; management brings expertise.',
                'Explain the effect of each.',
            ),
            'answer_part_hints': ['Address capital.', 'Address management.'],
            'guidelines': ['Link both criteria to success.'],
            'teaching_note': 'Reward both criteria linked to success.',
            'keywords': ['capital', 'shares', 'management', 'expertise', 'success'],
        }, subskill='application', learning_objective_id=LO_CRITERIA, question_family_id='criteria_success_scenario', concept_id='capital', concept_group='criteria', scenario_family_id='company_success', diagnostic_tags=['scenario_analysis', 'criteria'], answer_structure_tags=['explain'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Impact of a form of ownership',
            'prompt': 'Discuss the advantages and disadvantages of a private company as a form of ownership. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Advantage: limited liability protects shareholders\u2019 personal assets.',
                'Advantage: separate legal personality and continuity.',
                'Advantage: can raise more capital than a sole trader or partnership.',
                'Disadvantage: more legal requirements and higher formation/admin costs.',
                'Disadvantage: financial statements may need to be audited and shares cannot be sold to the public.',
            ],
            'sample_answer': 'A private company offers limited liability that protects shareholders\u2019 personal assets, a separate legal personality with continuity, and the ability to raise more capital than a sole trader or partnership. However, it faces more legal requirements and higher formation and administration costs, its financial statements may need to be audited, and it cannot sell shares to the public.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Give advantages and disadvantages.',
                'Liability/capital/continuity (advantages) vs cost/regulation (disadvantages).',
                'Balance both sides.',
            ),
            'answer_part_hints': ['Give advantages.', 'Give disadvantages.'],
            'guidelines': ['Provide advantages and disadvantages.'],
            'teaching_note': 'Reward a balanced discussion.',
            'keywords': ['limited liability', 'legal personality', 'capital', 'legal requirements', 'audited'],
        }, subskill='discussion', learning_objective_id=LO_FORMS, question_family_id='company_impact_discussion', concept_id='private_company', concept_group='forms', diagnostic_tags=['discussion', 'evaluation'], answer_structure_tags=['advantages', 'disadvantages'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Criteria for success or failure',
            'prompt': 'Discuss how the criteria of taxation, division of profits and legislation could contribute to the success or failure of a form of ownership. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Taxation: companies pay company tax, while sole traders are taxed in their personal capacity, affecting profitability.',
                'Favourable tax treatment can contribute to success; a heavy tax burden can lead to failure.',
                'Division of profits: clear, fair sharing keeps owners satisfied and committed.',
                'Disputes over profit sharing can cause failure, especially in partnerships.',
                'Legislation: meeting legal requirements builds credibility; non-compliance can lead to penalties or closure.',
            ],
            'sample_answer': 'Taxation affects success because companies pay company tax while sole traders are taxed personally; favourable tax treatment helps profitability while a heavy tax burden can cause failure. Clear and fair division of profits keeps owners satisfied and committed, whereas disputes over profit sharing can lead to failure, especially in partnerships. Meeting legislation builds credibility, while non-compliance can lead to penalties or closure.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Link each criterion to success or failure.',
                'Tax, profit sharing and legislation each cut both ways.',
                'Explain how each can help or harm.',
            ),
            'answer_part_hints': ['Address each criterion.', 'Explain success/failure.'],
            'guidelines': ['Cover taxation, profit division and legislation.'],
            'teaching_note': 'Reward each criterion linked to success or failure.',
            'keywords': ['taxation', 'company tax', 'division of profits', 'legislation', 'compliance'],
        }, subskill='discussion', learning_objective_id=LO_CRITERIA, question_family_id='criteria_discussion', concept_id='success_criteria', concept_group='criteria', diagnostic_tags=['discussion', 'evaluation'], answer_structure_tags=['explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
