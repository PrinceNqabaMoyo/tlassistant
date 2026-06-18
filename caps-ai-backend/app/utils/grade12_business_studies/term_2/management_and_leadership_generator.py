"""Grade 12 Business Studies - Term 2 - Management and leadership.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='management_and_leadership',
    curriculum_reference='Term 2 > Management and leadership',
    id_prefix='g12_bs_leadership',
)

LO_CONCEPTS = 'lo_management_leadership'
LO_STYLES = 'lo_leadership_styles'
LO_THEORIES = 'lo_leadership_theories'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Democratic leadership',
            'prompt': 'A leader who invites employees to take part in decision-making uses the … style.',
            'options': ['autocratic', 'democratic', 'laissez-faire', 'transactional'],
            'correct_index': 1,
            'explanation': 'In the democratic leadership style employees are invited to be part of the decision-making process.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on involving employees in decisions.',
                'Employees share in decisions = democratic.',
                'Autocratic excludes employees from decisions.',
            ),
            'guidelines': ['Employees share decisions = democratic.'],
        }, subskill='concepts', learning_objective_id=LO_STYLES, question_family_id='democratic_identify', concept_id='democratic_style', concept_group='styles', misconception_tags=['confuses_democratic_with_laissez_faire'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Autocratic leadership',
            'prompt': 'A leader who makes all decisions without consulting employees uses the … style.',
            'options': ['democratic', 'autocratic', 'charismatic', 'laissez-faire'],
            'correct_index': 1,
            'explanation': 'In the autocratic leadership style employees are not involved in the decision-making process; the leader decides alone.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on the leader deciding alone.',
                'No employee input = autocratic.',
                'Democratic invites employee input.',
            ),
            'guidelines': ['Leader decides alone = autocratic.'],
        }, subskill='concepts', learning_objective_id=LO_STYLES, question_family_id='autocratic_identify', concept_id='autocratic_style', concept_group='styles', misconception_tags=['confuses_autocratic_with_democratic'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Laissez-faire leadership',
            'prompt': 'A leader who lets experienced, trusted employees make their own decisions uses the … style.',
            'options': ['autocratic', 'laissez-faire/free-reign', 'transactional', 'democratic'],
            'correct_index': 1,
            'explanation': 'The laissez-faire/free-reign style allows experienced, reliable and trustworthy employees to make decisions themselves.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on hands-off leadership.',
                'Letting trusted staff decide = laissez-faire.',
                'Transactional uses rewards and punishments.',
            ),
            'guidelines': ['Hands-off, staff decide = laissez-faire.'],
        }, subskill='concepts', learning_objective_id=LO_STYLES, question_family_id='laissez_faire_identify', concept_id='laissez_faire_style', concept_group='styles', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Transactional leadership',
            'prompt': 'A leader who uses rewards and punishments as incentives to influence behaviour uses the … style.',
            'options': ['charismatic', 'transactional', 'democratic', 'laissez-faire'],
            'correct_index': 1,
            'explanation': 'The transactional style uses rewards and punishments as incentives to influence the behaviour of employees.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on rewards and punishments.',
                'Incentives/punishments = transactional.',
                'Charismatic relies on charm and influence.',
            ),
            'guidelines': ['Rewards/punishments = transactional.'],
        }, subskill='concepts', learning_objective_id=LO_STYLES, question_family_id='transactional_identify', concept_id='transactional_style', concept_group='styles', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Management vs leadership',
            'prompt': 'Which statement best distinguishes management from leadership?',
            'options': [
                'Management inspires people while leadership controls resources',
                'Management focuses on planning/organising/controlling while leadership focuses on inspiring and influencing people',
                'They are exactly the same',
                'Leadership only happens at the top of the business',
            ],
            'correct_index': 1,
            'explanation': 'Management focuses on planning, organising and controlling resources, while leadership focuses on inspiring, motivating and influencing people.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Compare the focus of each.',
                'Management = systems/resources; leadership = people/vision.',
                'They overlap but are not identical.',
            ),
            'guidelines': ['Management = resources; leadership = people.'],
        }, subskill='concepts', learning_objective_id=LO_CONCEPTS, question_family_id='management_vs_leadership', concept_id='management_leadership', concept_group='concepts', misconception_tags=['confuses_management_with_leadership'], diagnostic_tags=['comparison']),
        with_metadata({
            'title': 'Situational leadership theory',
            'prompt': 'A leader who changes their style depending on the situation is applying the … theory.',
            'options': ['leaders and followers', 'situational leadership', 'transformational leadership', 'transactional leadership'],
            'correct_index': 1,
            'explanation': 'In situational leadership the leader applies different leadership styles depending on the situation.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on adapting style to the situation.',
                'Adapting to the situation = situational leadership.',
                'Transformational leadership suits drastic change.',
            ),
            'guidelines': ['Adapt style to situation = situational leadership.'],
        }, subskill='concepts', learning_objective_id=LO_THEORIES, question_family_id='situational_identify', concept_id='situational_theory', concept_group='theories', misconception_tags=['confuses_situational_with_transformational'], diagnostic_tags=['identification', 'theories']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Identify and motivate a style',
            'prompt': 'A manager makes all decisions alone and simply tells staff what to do during a crisis. Identify the leadership style and motivate why it may be suitable here. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The style is autocratic leadership.',
                'The leader makes decisions without consulting employees.',
                'It is suitable in a crisis because quick, decisive action is needed.',
                'It provides clear direction when there is no time for consultation.',
            ],
            'sample_answer': 'The style is autocratic leadership because the manager makes all decisions alone and tells staff what to do. It may be suitable in a crisis because quick, decisive action and clear direction are needed, and there is no time for lengthy consultation.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the behaviour to a style.',
                'Decides alone + tells staff = autocratic.',
                'Motivate why autocratic suits a crisis.',
            ),
            'answer_part_hints': ['Name the style.', 'Motivate the choice.'],
            'guidelines': ['Identify autocratic and motivate.'],
            'teaching_note': 'Reward autocratic identification with a crisis motivation.',
            'keywords': ['autocratic', 'decides alone', 'crisis', 'quick', 'direction'],
        }, subskill='application', learning_objective_id=LO_STYLES, question_family_id='identify_style_scenario', concept_id='autocratic_style', concept_group='styles', scenario_family_id='crisis_manager', diagnostic_tags=['scenario_analysis', 'styles'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Recommend a leadership style',
            'prompt': 'A team of experienced, highly skilled software developers works best with freedom. Recommend a suitable leadership style and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend the laissez-faire/free-reign style.',
                'The team is experienced, reliable and trustworthy.',
                'Freedom allows creativity and self-direction.',
                'It increases motivation and ownership of the work.',
            ],
            'sample_answer': 'The laissez-faire/free-reign style is suitable because the developers are experienced, reliable and trustworthy. Giving them the freedom to make their own decisions allows creativity and self-direction, and increases their motivation and ownership of the work.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match a skilled, independent team to a style.',
                'Experienced team that wants freedom = laissez-faire.',
                'Motivate with creativity and motivation.',
            ),
            'answer_part_hints': ['Name the style.', 'Motivate the choice.'],
            'guidelines': ['Recommend laissez-faire and motivate.'],
            'teaching_note': 'Reward laissez-faire with a motivation.',
            'keywords': ['laissez-faire', 'experienced', 'freedom', 'creativity', 'motivation'],
        }, subskill='application', learning_objective_id=LO_STYLES, question_family_id='recommend_style_scenario', concept_id='laissez_faire_style', concept_group='styles', scenario_family_id='developer_team', diagnostic_tags=['scenario_analysis', 'styles'], answer_structure_tags=['recommend', 'motivate'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Impact of the democratic style',
            'prompt': 'Discuss the positive and negative impact of the democratic leadership style in the workplace. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Positive: employees feel valued and motivated through participation.',
                'Positive: better decisions from a range of ideas and inputs.',
                'Positive: improves teamwork and employee commitment.',
                'Negative: decision-making can be slow because of consultation.',
                'Negative: may be unsuitable in a crisis needing quick decisions.',
            ],
            'sample_answer': 'The democratic style positively makes employees feel valued and motivated through participation, leads to better decisions from a range of inputs, and improves teamwork and commitment. However, it can slow down decision-making because of the consultation involved and may be unsuitable in a crisis that needs quick, decisive action.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Give both positives and negatives.',
                'Participation/motivation (positive) vs slow decisions (negative).',
                'Balance both sides.',
            ),
            'answer_part_hints': ['Give positives.', 'Give negatives.'],
            'guidelines': ['Provide positives and negatives.'],
            'teaching_note': 'Reward a balanced impact discussion.',
            'keywords': ['participation', 'motivated', 'better decisions', 'slow', 'crisis'],
        }, subskill='discussion', learning_objective_id=LO_STYLES, question_family_id='democratic_impact_discussion', concept_id='democratic_style', concept_group='styles', diagnostic_tags=['discussion', 'evaluation'], answer_structure_tags=['positives', 'negatives'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Leadership theories',
            'prompt': 'Explain the situational and transformational leadership theories and how each can improve leadership. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Situational leadership: the leader adapts their style to the situation and the team\u2019s readiness.',
                'It improves leadership by matching the approach to each circumstance.',
                'Transformational leadership: the leader inspires and drives major change.',
                'It is best used during drastic change to motivate and unite employees.',
                'Both increase effectiveness when applied appropriately.',
            ],
            'sample_answer': 'Situational leadership means the leader adapts their style to suit the situation and the readiness of the team, which improves leadership by matching the approach to each circumstance. Transformational leadership means the leader inspires and drives major change, and is best used during drastic change to motivate and unite employees. Both theories increase effectiveness when applied appropriately.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain each theory and its benefit.',
                'Situational = adapt; transformational = inspire change.',
                'Link each to better leadership.',
            ),
            'answer_part_hints': ['Explain each theory.', 'State how it improves leadership.'],
            'guidelines': ['Cover both theories with benefits.'],
            'teaching_note': 'Reward both theories explained with benefits.',
            'keywords': ['situational', 'adapt', 'transformational', 'change', 'inspire'],
        }, subskill='discussion', learning_objective_id=LO_THEORIES, question_family_id='theories_discussion', concept_id='situational_theory', concept_group='theories', diagnostic_tags=['discussion', 'theories'], answer_structure_tags=['explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
