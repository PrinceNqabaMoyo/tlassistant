"""Grade 12 Business Studies - Term 1 - The human resources function.

Covers recruitment, selection, induction, placement, salary determination,
fringe benefits and the implications of legislation on the HR function.
Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='human_resources_function',
    curriculum_reference='Term 1 > The human resources function',
    id_prefix='g12_bs_hr',
)

LO_RECRUIT = 'lo_recruitment'
LO_SELECT = 'lo_selection'
LO_CONTRACT = 'lo_employment_contract'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Recruitment',
            'prompt': 'The process of attracting suitable candidates to apply for a vacant position is …',
            'options': ['selection', 'recruitment', 'induction', 'placement'],
            'correct_index': 1,
            'explanation': 'Recruitment is the process of attracting suitable candidates to apply for a vacant position.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on attracting applicants.',
                'Attracting candidates to apply = recruitment.',
                'Selection is choosing among the applicants.',
            ),
            'guidelines': ['Attracting applicants = recruitment.'],
        }, subskill='concepts', learning_objective_id=LO_RECRUIT, question_family_id='recruitment_definition', concept_id='recruitment', concept_group='recruitment', misconception_tags=['confuses_recruitment_with_selection'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Job description vs specification',
            'prompt': 'A document that lists the duties and responsibilities of a job is a …',
            'options': ['job specification', 'job description', 'employment contract', 'code of conduct'],
            'correct_index': 1,
            'explanation': 'A job description lists the duties and responsibilities of the job, while a job specification lists the qualifications and skills the candidate needs.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Distinguish duties from candidate requirements.',
                'Duties/responsibilities of the job = job description.',
                'Required skills/qualifications = job specification.',
            ),
            'guidelines': ['Duties of the job = job description.'],
        }, subskill='concepts', learning_objective_id=LO_RECRUIT, question_family_id='job_description_definition', concept_id='job_description', concept_group='recruitment', misconception_tags=['confuses_description_with_specification'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Internal recruitment',
            'prompt': 'Filling a vacancy by promoting an existing employee is an example of …',
            'options': ['external recruitment', 'internal recruitment', 'induction', 'selection'],
            'correct_index': 1,
            'explanation': 'Internal recruitment fills a vacancy from within the business, for example by promoting or transferring an existing employee.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on filling from within.',
                'Promoting an existing employee = internal recruitment.',
                'Hiring from outside = external recruitment.',
            ),
            'guidelines': ['Filling from within = internal recruitment.'],
        }, subskill='concepts', learning_objective_id=LO_RECRUIT, question_family_id='internal_recruitment_identify', concept_id='internal_recruitment', concept_group='recruitment', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Induction',
            'prompt': 'The process of introducing a new employee to the business, its people and procedures is …',
            'options': ['recruitment', 'induction', 'selection', 'screening'],
            'correct_index': 1,
            'explanation': 'Induction introduces a new employee to the business, its culture, people and procedures so they can settle in.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on introducing a new hire.',
                'Settling a new employee in = induction.',
                'Selection chooses the candidate before induction.',
            ),
            'guidelines': ['Introducing a new employee = induction.'],
        }, subskill='concepts', learning_objective_id=LO_SELECT, question_family_id='induction_definition', concept_id='induction', concept_group='selection', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Employment contract',
            'prompt': 'A legally binding agreement between an employer and an employee is a/an …',
            'options': ['code of conduct', 'employment contract', 'job specification', 'partnership agreement'],
            'correct_index': 1,
            'explanation': 'An employment contract is a legally binding agreement between the employer and the employee.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on a legal agreement to work.',
                'Legally binding employer-employee agreement = employment contract.',
                'A code of conduct sets acceptable behaviour.',
            ),
            'guidelines': ['Legal employer-employee agreement = employment contract.'],
        }, subskill='concepts', learning_objective_id=LO_CONTRACT, question_family_id='contract_definition', concept_id='employment_contract', concept_group='contract', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Fringe benefits',
            'prompt': 'Medical aid and a pension fund offered in addition to a salary are examples of …',
            'options': ['fringe benefits', 'commission', 'piece work', 'overtime'],
            'correct_index': 0,
            'explanation': 'Fringe benefits are extra benefits, such as medical aid and pension, offered in addition to an employee\u2019s salary.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on extras added to a salary.',
                'Medical aid/pension on top of salary = fringe benefits.',
                'Commission is pay linked to sales.',
            ),
            'guidelines': ['Extras added to salary = fringe benefits.'],
        }, subskill='concepts', learning_objective_id=LO_CONTRACT, question_family_id='fringe_benefits_identify', concept_id='fringe_benefits', concept_group='contract', diagnostic_tags=['identification']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Recommend a recruitment method',
            'prompt': 'A business needs to fill a senior management post quickly and wants to reward loyal staff. Recommend a recruitment method and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend internal recruitment.',
                'It is faster and cheaper than external recruitment.',
                'It rewards and motivates loyal, existing staff through promotion.',
                'The candidate already knows the business and its culture.',
            ],
            'sample_answer': 'The business should use internal recruitment by promoting a suitable existing employee. This is faster and cheaper than external recruitment, rewards and motivates loyal staff, and the candidate already understands the business and its culture.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the goals to a recruitment method.',
                'Quick + reward loyal staff = internal recruitment.',
                'Motivate with cost, speed and familiarity.',
            ),
            'answer_part_hints': ['Name the method.', 'Motivate the choice.'],
            'guidelines': ['Recommend internal recruitment with motivation.'],
            'teaching_note': 'Reward internal recruitment plus a motivation.',
            'keywords': ['internal recruitment', 'promote', 'faster', 'cheaper', 'motivate'],
        }, subskill='application', learning_objective_id=LO_RECRUIT, question_family_id='recommend_recruitment_scenario', concept_id='internal_recruitment', concept_group='recruitment', scenario_family_id='senior_post', diagnostic_tags=['scenario_analysis'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Analyse an employment contract',
            'prompt': 'A contract does not state the working hours, salary or leave of the employee. Identify the problem and recommend improvements so the contract is legally compliant. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The contract omits essential terms required by law.',
                'Add the agreed working hours and overtime arrangements.',
                'State the salary/wage and payment intervals.',
                'Include leave entitlements and notice/termination terms.',
            ],
            'sample_answer': 'The contract is incomplete because it omits essential terms required by the BCEA. It should be improved by adding the agreed working hours and overtime, the salary or wage and how often it is paid, and the leave entitlements and notice/termination terms, so that it is legally compliant.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Spot the missing legal terms.',
                'Hours, pay, leave and notice are essential terms.',
                'Recommend adding each missing term.',
            ),
            'answer_part_hints': ['Identify the problem.', 'Recommend the missing terms.'],
            'guidelines': ['Identify missing terms and recommend fixes.'],
            'teaching_note': 'Reward identifying missing terms plus the additions.',
            'keywords': ['working hours', 'salary', 'leave', 'notice', 'legally compliant'],
        }, subskill='application', learning_objective_id=LO_CONTRACT, question_family_id='analyse_contract_scenario', concept_id='employment_contract', concept_group='contract', scenario_family_id='incomplete_contract', diagnostic_tags=['scenario_analysis'], answer_structure_tags=['identify', 'recommend'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Role of the interviewer',
            'prompt': 'Discuss the role of the interviewer before and during a selection interview. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Before: study the job description and each candidate\u2019s CV/application.',
                'Before: prepare relevant questions and book a suitable venue.',
                'During: make the candidate feel at ease and ask the prepared questions.',
                'During: listen actively and record/assess the responses fairly.',
                'During: give the candidate a chance to ask questions and explain next steps.',
            ],
            'sample_answer': 'Before the interview the interviewer should study the job description and each candidate\u2019s CV, prepare relevant questions and arrange a suitable venue. During the interview they should put the candidate at ease, ask the prepared questions, listen actively and assess the answers fairly, then allow the candidate to ask questions and explain the next steps.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Split the answer into before and during.',
                'Before = preparation; during = conduct and assessment.',
                'Cover fairness and active listening.',
            ),
            'answer_part_hints': ['Cover before the interview.', 'Cover during the interview.'],
            'guidelines': ['Address both before and during.'],
            'teaching_note': 'Reward both before and during roles.',
            'keywords': ['prepare questions', 'job description', 'at ease', 'listen', 'assess'],
        }, subskill='discussion', learning_objective_id=LO_SELECT, question_family_id='interviewer_role_discussion', concept_id='selection', concept_group='selection', diagnostic_tags=['discussion'], answer_structure_tags=['before', 'during'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Impact of recruitment methods',
            'prompt': 'Discuss the advantages and disadvantages of external recruitment. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Advantage: brings new skills, ideas and experience into the business.',
                'Advantage: a larger pool of candidates to choose from.',
                'Disadvantage: more expensive and time-consuming than internal recruitment.',
                'Disadvantage: the new employee needs time to learn the business and may demotivate existing staff.',
            ],
            'sample_answer': 'External recruitment brings new skills, ideas and experience into the business and offers a larger pool of candidates to choose from. However, it is more expensive and time-consuming than internal recruitment, the new employee needs time to learn the business, and it can demotivate existing staff who were overlooked.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Give both advantages and disadvantages.',
                'New skills/larger pool (advantages) vs cost/time (disadvantages).',
                'Balance both sides.',
            ),
            'answer_part_hints': ['Give advantages.', 'Give disadvantages.'],
            'guidelines': ['Provide advantages and disadvantages.'],
            'teaching_note': 'Reward a balanced discussion.',
            'keywords': ['new skills', 'larger pool', 'expensive', 'time-consuming', 'demotivate'],
        }, subskill='discussion', learning_objective_id=LO_RECRUIT, question_family_id='external_recruitment_discussion', concept_id='external_recruitment', concept_group='recruitment', diagnostic_tags=['discussion', 'evaluation'], answer_structure_tags=['advantages', 'disadvantages'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
