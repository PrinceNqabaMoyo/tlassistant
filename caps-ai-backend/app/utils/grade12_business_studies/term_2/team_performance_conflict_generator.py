"""Grade 12 Business Studies - Term 2 - Team performance assessment and conflict.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='team_performance_conflict',
    curriculum_reference='Term 2 > Team performance assessment and conflict management',
    id_prefix='g12_bs_team',
)

LO_CRITERIA = 'lo_team_criteria'
LO_STAGES = 'lo_team_stages'
LO_CONFLICT = 'lo_conflict_management'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Forming stage',
            'prompt': 'In which stage of team development do members first meet, are polite and unsure of their roles?',
            'options': ['Storming', 'Forming', 'Norming', 'Performing'],
            'correct_index': 1,
            'explanation': 'In the forming stage members first come together, are polite and still unsure of their roles and the task.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on the first meeting of the team.',
                'First, polite, unsure stage = forming.',
                'Conflict arises later, in storming.',
            ),
            'guidelines': ['First, polite stage = forming.'],
        }, subskill='concepts', learning_objective_id=LO_STAGES, question_family_id='forming_identify', concept_id='forming', concept_group='stages', misconception_tags=['confuses_forming_with_storming'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Storming stage',
            'prompt': 'During which stage do team members experience conflict and compete for position?',
            'options': ['Forming', 'Storming', 'Norming', 'Adjourning'],
            'correct_index': 1,
            'explanation': 'In the storming stage conflict arises as members compete for position and challenge ideas.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on conflict and competition.',
                'Conflict/competition stage = storming.',
                'Norming is when the team settles and agrees on norms.',
            ),
            'guidelines': ['Conflict stage = storming.'],
        }, subskill='concepts', learning_objective_id=LO_STAGES, question_family_id='storming_identify', concept_id='storming', concept_group='stages', misconception_tags=['confuses_storming_with_norming'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Performing stage',
            'prompt': 'In which stage does the team work effectively and productively towards its goals?',
            'options': ['Norming', 'Performing', 'Forming', 'Storming'],
            'correct_index': 1,
            'explanation': 'In the performing stage the team works effectively and productively towards achieving its goals.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on effective, productive work.',
                'Effective, productive stage = performing.',
                'Adjourning is when the team disbands.',
            ),
            'guidelines': ['Effective, productive stage = performing.'],
        }, subskill='concepts', learning_objective_id=LO_STAGES, question_family_id='performing_identify', concept_id='performing', concept_group='stages', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Criterion for team performance',
            'prompt': 'Which of the following is a criterion for successful team performance?',
            'options': ['Affirmative action', 'Shared values', 'Vertical integration', 'Market penetration'],
            'correct_index': 1,
            'explanation': 'Criteria for successful team performance include shared values, communication, collaboration and positive interpersonal attitudes and behaviour.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recall the team performance criteria.',
                'Shared values is a team criterion.',
                'Integration/penetration are growth strategies.',
            ),
            'guidelines': ['Shared values = a team criterion.'],
        }, subskill='concepts', learning_objective_id=LO_CRITERIA, question_family_id='criteria_identify', concept_id='shared_values', concept_group='criteria', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Grievance vs conflict',
            'prompt': 'A formal complaint by an employee about a work-related issue is best described as a …',
            'options': ['conflict', 'grievance', 'strike', 'lockout'],
            'correct_index': 1,
            'explanation': 'A grievance is a formal complaint raised by an employee about a work-related issue, whereas conflict is a broader clash between people or groups.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on a formal complaint.',
                'Formal employee complaint = grievance.',
                'Conflict is a broader disagreement/clash.',
            ),
            'guidelines': ['Formal complaint = grievance.'],
        }, subskill='concepts', learning_objective_id=LO_CONFLICT, question_family_id='grievance_identify', concept_id='grievance', concept_group='conflict', misconception_tags=['confuses_grievance_with_conflict'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Difficult personality',
            'prompt': 'A team member who constantly finds fault and is never satisfied is best described as the …',
            'options': ['complainer', 'expert', 'indecisive', 'over-agree'],
            'correct_index': 0,
            'explanation': 'The complainer constantly finds fault and is never satisfied, which can lower team morale.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on constant fault-finding.',
                'Always finds fault = complainer.',
                'The expert thinks they know everything.',
            ),
            'guidelines': ['Constant fault-finding = complainer.'],
        }, subskill='concepts', learning_objective_id=LO_CONFLICT, question_family_id='difficult_person_identify', concept_id='complainer', concept_group='conflict', diagnostic_tags=['identification']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Identify the team stage',
            'prompt': 'A newly formed project team is arguing about who should lead and whose ideas are best. Identify the stage of team development and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The stage is storming.',
                'Members are experiencing conflict and competing for position.',
                'There are disagreements about leadership and ideas.',
                'This typically follows the forming stage.',
            ],
            'sample_answer': 'The team is in the storming stage because members are experiencing conflict, competing for the leadership position and disagreeing about whose ideas are best. This stage typically follows forming as roles are still being established.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the conflict to a stage.',
                'Arguing/competing for position = storming.',
                'Motivate using the conflict clues.',
            ),
            'answer_part_hints': ['Name the stage.', 'Motivate the choice.'],
            'guidelines': ['Identify storming and motivate.'],
            'teaching_note': 'Reward storming with a motivation.',
            'keywords': ['storming', 'conflict', 'compete', 'position', 'disagree'],
        }, subskill='application', learning_objective_id=LO_STAGES, question_family_id='identify_stage_scenario', concept_id='storming', concept_group='stages', scenario_family_id='project_team', diagnostic_tags=['scenario_analysis', 'stages'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Handle conflict in the workplace',
            'prompt': 'Two departments are in ongoing conflict over shared resources. Advise the manager on the steps to resolve the conflict. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Acknowledge the conflict and identify its real cause.',
                'Bring the parties together to discuss the issue openly.',
                'Allow each side to state its position and listen actively.',
                'Find a mutually acceptable solution and follow up to ensure it works.',
            ],
            'sample_answer': 'The manager should acknowledge the conflict and identify its real cause, then bring the two departments together to discuss the issue openly. Each side should state its position while the manager listens actively, after which they agree on a mutually acceptable solution and follow up to ensure it is working.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List conflict-resolution steps.',
                'Acknowledge, discuss, listen, agree, follow up.',
                'Apply the steps to the resource dispute.',
            ),
            'answer_part_hints': ['List the steps.', 'Apply to the scenario.'],
            'guidelines': ['Provide conflict-resolution steps.'],
            'teaching_note': 'Reward ordered conflict-resolution steps.',
            'keywords': ['acknowledge', 'cause', 'discuss', 'listen', 'solution', 'follow up'],
        }, subskill='application', learning_objective_id=LO_CONFLICT, question_family_id='resolve_conflict_scenario', concept_id='conflict_resolution', concept_group='conflict', scenario_family_id='department_conflict', diagnostic_tags=['scenario_analysis', 'conflict'], answer_structure_tags=['apply', 'sequence'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Criteria for successful team performance',
            'prompt': 'Discuss the criteria for successful team performance. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Positive interpersonal attitudes and behaviour among members.',
                'Shared values and a common goal that unite the team.',
                'Open and effective communication between members.',
                'Collaboration, where members work together and support one another.',
                'These criteria improve trust, productivity and team success.',
            ],
            'sample_answer': 'Successful team performance depends on positive interpersonal attitudes and behaviour, shared values and a common goal, open and effective communication, and collaboration where members work together and support one another. Meeting these criteria builds trust, raises productivity and improves the chances of the team succeeding.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List and explain the criteria.',
                'Attitudes, shared values, communication, collaboration.',
                'Link the criteria to team success.',
            ),
            'answer_part_hints': ['List the criteria.', 'Explain each.'],
            'guidelines': ['Cover the team performance criteria.'],
            'teaching_note': 'Reward each criterion explained.',
            'keywords': ['interpersonal', 'shared values', 'communication', 'collaboration', 'trust'],
        }, subskill='discussion', learning_objective_id=LO_CRITERIA, question_family_id='criteria_discussion', concept_id='shared_values', concept_group='criteria', diagnostic_tags=['discussion'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Stages of team development',
            'prompt': 'Explain the stages of team development a team goes through. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Forming: members meet, are polite and unsure of roles.',
                'Storming: conflict arises as members compete for position.',
                'Norming: the team settles, agrees on norms and roles.',
                'Performing: the team works effectively towards its goals.',
                'Adjourning/mourning: the team disbands after completing the task.',
            ],
            'sample_answer': 'In forming, members meet and are polite but unsure of their roles. In storming, conflict arises as members compete for position. In norming, the team settles and agrees on norms and roles. In performing, the team works effectively towards its goals. Finally, in adjourning/mourning, the team disbands after completing the task.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List the stages in order.',
                'Forming, storming, norming, performing, adjourning.',
                'Explain each briefly.',
            ),
            'answer_part_hints': ['Name each stage.', 'Explain each.'],
            'guidelines': ['Cover all stages in order.'],
            'teaching_note': 'Reward all stages explained in order.',
            'keywords': ['forming', 'storming', 'norming', 'performing', 'adjourning'],
        }, subskill='discussion', learning_objective_id=LO_STAGES, question_family_id='stages_discussion', concept_id='forming', concept_group='stages', diagnostic_tags=['discussion'], answer_structure_tags=['list', 'sequence'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
