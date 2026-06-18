"""Grade 11 Business Studies - Term 2 - Topic 9: Stress, crisis and change
management.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='stress_crisis_change',
    curriculum_reference='Term 2 > Stress, crisis and change management',
    id_prefix='g11_bs_stress',
)

LO_STRESS = 'lo_stress_management'
LO_CRISIS = 'lo_crisis_management'
LO_CHANGE = 'lo_change_management'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Stress',
            'prompt': 'A state of mental or emotional strain or tension resulting from adverse or demanding circumstances is …',
            'options': ['crisis', 'stress', 'change', 'morale'],
            'correct_index': 1,
            'explanation': 'Stress is a state of mental or emotional strain or tension resulting from adverse or demanding circumstances.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the mental/emotional strain.',
                'Stress is tension from demanding circumstances.',
                'A crisis is a sudden emergency event, not the strain itself.',
            ),
            'guidelines': ['Link "mental/emotional strain" to stress.'],
        }, subskill='concepts', learning_objective_id=LO_STRESS, question_family_id='stress_definition', concept_id='stress', concept_group='stress', misconception_tags=['confuses_stress_with_crisis'], diagnostic_tags=['definition', 'stress']),
        with_metadata({
            'title': 'Crisis management',
            'prompt': 'The process that a business uses to deal with an emergency is called …',
            'options': ['change management', 'crisis management', 'stress management', 'risk bearing'],
            'correct_index': 1,
            'explanation': 'Crisis management is the process that a business uses to deal with an emergency event or situation.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the process to an emergency.',
                'Crisis management deals with emergencies.',
                'Change management deals with planned/ongoing change.',
            ),
            'guidelines': ['Link "emergency" to crisis management.'],
        }, subskill='concepts', learning_objective_id=LO_CRISIS, question_family_id='crisis_management_definition', concept_id='crisis_management', concept_group='crisis', misconception_tags=['confuses_crisis_with_change'], diagnostic_tags=['definition', 'crisis']),
        with_metadata({
            'title': 'Change management',
            'prompt': 'The process that a business uses to deal with change and development within the business is called …',
            'options': ['crisis management', 'change management', 'stress management', 'production control'],
            'correct_index': 1,
            'explanation': 'Change management is the process that a business uses to deal with change and development within the business.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the process to change.',
                'Change management facilitates and implements change.',
                'Crisis management responds to emergencies.',
            ),
            'guidelines': ['Link "change and development" to change management.'],
        }, subskill='concepts', learning_objective_id=LO_CHANGE, question_family_id='change_management_definition', concept_id='change_management', concept_group='change', misconception_tags=['confuses_change_with_crisis'], diagnostic_tags=['definition', 'change']),
        with_metadata({
            'title': 'Causes of stress',
            'prompt': 'Which of the following is a cause of stress in the business environment?',
            'options': ['Reasonable workload', 'Work overload and unrealistic deadlines', 'Supportive managers', 'Flexible working hours'],
            'correct_index': 1,
            'explanation': 'Causes of stress include work overload, long working hours, time pressures and deadlines, and incompetent managers.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify a demanding circumstance.',
                'Overload and tight deadlines cause stress.',
                'Supportive managers and flexible hours reduce stress.',
            ),
            'guidelines': ['Look for demanding/pressured conditions.'],
        }, subskill='concepts', learning_objective_id=LO_STRESS, question_family_id='causes_of_stress_identification', concept_id='causes_of_stress', concept_group='stress', misconception_tags=['confuses_stressor_with_relief'], diagnostic_tags=['identification', 'stress']),
        with_metadata({
            'title': 'Kotter step 1',
            'prompt': 'According to John P Kotter\'s 8 steps of leading change, the FIRST step is to …',
            'options': [
                'anchor the changes in corporate culture',
                'establish a sense of urgency',
                'form a powerful coalition',
                'celebrate short-term wins',
            ],
            'correct_index': 1,
            'explanation': 'Kotter\'s first step is to establish a sense of urgency by motivating employees about the need for change.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recall the order of Kotter\'s steps.',
                'Change starts by creating urgency.',
                'Anchoring in culture is the LAST step.',
            ),
            'guidelines': ['First step = sense of urgency.'],
        }, subskill='concepts', learning_objective_id=LO_CHANGE, question_family_id='kotter_step1', concept_id='kotter_model', concept_group='change', misconception_tags=['confuses_first_step_with_last'], diagnostic_tags=['recall', 'change']),
        with_metadata({
            'title': 'Major changes',
            'prompt': 'Which of the following is an example of a major change that businesses and people must deal with?',
            'options': ['Buying stationery', 'Globalisation and affirmative action', 'Cleaning the office', 'Daily team meetings'],
            'correct_index': 1,
            'explanation': 'Major changes include unemployment, retrenchment, globalisation and affirmative action.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify a large-scale change.',
                'Globalisation and affirmative action are major changes.',
                'Routine tasks are not "major changes".',
            ),
            'guidelines': ['Look for large-scale, structural change.'],
        }, subskill='concepts', learning_objective_id=LO_CHANGE, question_family_id='major_changes_identification', concept_id='major_changes', concept_group='change', misconception_tags=['confuses_routine_with_major_change'], diagnostic_tags=['identification', 'change']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Manage workplace stress',
            'prompt': 'Employees at a call centre report high stress from work overload and tight deadlines. Recommend TWO ways the business can help employees manage this stress. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Balance workloads / set realistic deadlines.',
                'Provide employee wellness/counselling support.',
                'Encourage breaks, exercise and work-life balance.',
                'Provide training/time-management support.',
            ],
            'sample_answer': 'The business can balance workloads and set realistic deadlines, and provide wellness support such as counselling. It can also encourage regular breaks and a healthy work-life balance, and offer time-management training to help employees cope.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Target the causes of the stress.',
                'Overload/deadlines call for workload and time fixes.',
                'Wellness support also helps employees cope.',
            ),
            'answer_part_hints': ['Give two ways.', 'Link them to the causes.'],
            'guidelines': ['Recommendations must address the scenario causes.'],
            'teaching_note': 'Reward two practical, relevant stress-management measures.',
            'keywords': ['stress', 'workload', 'deadlines', 'wellness', 'breaks', 'balance'],
        }, subskill='application', learning_objective_id=LO_STRESS, question_family_id='manage_stress_scenario', concept_id='management_of_stress', concept_group='stress', scenario_family_id='call_centre_stress', diagnostic_tags=['scenario_analysis', 'stress'], answer_structure_tags=['recommend', 'apply'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Identify the cause of change',
            'prompt': 'A retailer must adopt new online systems because competitors now sell internationally and customers shop online. Identify whether this is an internal or external cause of change and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'This is an external cause of change.',
                'Driven by competitors and customer behaviour (outside the business).',
                'Globalisation/technology are external forces.',
                'Motivation references factors beyond the business\'s control.',
            ],
            'sample_answer': 'This is an external cause of change because it is driven by competitors selling internationally and customers shopping online - forces outside the business such as globalisation and technology, which the business cannot control.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Decide where the cause originates.',
                'Competitors and customers are external forces.',
                'Internal causes come from inside the business.',
            ),
            'answer_part_hints': ['Classify the cause.', 'Motivate your choice.'],
            'guidelines': ['Use scenario evidence.'],
            'teaching_note': 'Reward correct internal/external classification plus motivation.',
            'keywords': ['external', 'competitors', 'customers', 'globalisation', 'technology'],
        }, subskill='application', learning_objective_id=LO_CHANGE, question_family_id='cause_of_change_scenario', concept_id='causes_of_change', concept_group='change', scenario_family_id='retailer_online_change', diagnostic_tags=['scenario_analysis', 'change'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': "Kotter's 8 steps of leading change",
            'prompt': 'Elaborate on John P Kotter\'s eight steps of leading change. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Establish a sense of urgency.',
                'Form a powerful coalition of influential people.',
                'Create a vision for change and develop strategies.',
                'Communicate the vision to everyone.',
                'Empower/remove obstacles and act on the vision.',
                'Create and celebrate short-term wins.',
                'Build on the change (consolidate gains).',
                'Anchor the changes in the corporate culture.',
            ],
            'sample_answer': 'Kotter\'s steps are: establish a sense of urgency; form a powerful coalition of influential people; create a vision for change; communicate that vision; empower employees and remove obstacles; create and celebrate short-term wins; build on the change to consolidate gains; and finally anchor the changes in the corporate culture so they become part of how the business works.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List the steps in order.',
                'Start with urgency, end with anchoring in culture.',
                'Short-term wins come before consolidating gains.',
            ),
            'answer_part_hints': ['Name each step.', 'Keep them in order.'],
            'guidelines': ['Provide the steps clearly and in a logical order.'],
            'teaching_note': 'Reward correct steps; order strengthens the answer.',
            'keywords': ['urgency', 'coalition', 'vision', 'communicate', 'short-term wins', 'culture'],
        }, subskill='discussion', learning_objective_id=LO_CHANGE, question_family_id='kotter_steps_discussion', concept_id='kotter_model', concept_group='change', diagnostic_tags=['discussion', 'change'], answer_structure_tags=['list', 'sequence'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Dealing with a crisis',
            'prompt': 'Recommend ways in which businesses can deal with a crisis in the workplace. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Have a crisis management plan and team ready.',
                'Communicate quickly, honestly and clearly with stakeholders.',
                'Act decisively to contain the crisis and protect people.',
                'Review and learn from the crisis to prevent recurrence.',
            ],
            'sample_answer': 'Businesses should have a crisis management plan and team in place, communicate quickly and honestly with stakeholders, act decisively to contain the crisis and protect people, and afterwards review what happened to learn from it and prevent a recurrence.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recommend steps for handling emergencies.',
                'Think plan, communicate, act, review.',
                'Crisis management protects people and reputation.',
            ),
            'answer_part_hints': ['Give several ways.', 'Explain each.'],
            'guidelines': ['Provide at least three ways.'],
            'teaching_note': 'Reward distinct, practical crisis responses.',
            'keywords': ['crisis', 'plan', 'communicate', 'act', 'contain', 'review'],
        }, subskill='discussion', learning_objective_id=LO_CRISIS, question_family_id='deal_with_crisis_discussion', concept_id='crisis_management', concept_group='crisis', diagnostic_tags=['discussion', 'crisis'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
