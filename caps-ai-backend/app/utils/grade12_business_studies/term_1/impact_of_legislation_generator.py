"""Grade 12 Business Studies - Term 1 - Impact of recent legislation on business.

Covers SDA, LRA, EEA, BCEA, COIDA, BBBEE, NCA and CPA.
Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='impact_of_legislation',
    curriculum_reference='Term 1 > The impact of recent legislation on businesses',
    id_prefix='g12_bs_legislation',
)

LO_ACTS = 'lo_acts_purpose'
LO_BBBEE = 'lo_bbbee_pillars'
LO_COMPLIANCE = 'lo_compliance'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Employment Equity Act',
            'prompt': 'Which Act aims to eliminate unfair discrimination and promote affirmative action in the workplace?',
            'options': ['BCEA', 'Employment Equity Act (EEA)', 'COIDA', 'National Credit Act'],
            'correct_index': 1,
            'explanation': 'The Employment Equity Act (EEA) promotes equity by eliminating unfair discrimination and implementing affirmative action measures.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on discrimination and affirmative action.',
                'Equity + affirmative action = Employment Equity Act.',
                'The BCEA sets basic conditions like working hours.',
            ),
            'guidelines': ['Equity/affirmative action = EEA.'],
        }, subskill='concepts', learning_objective_id=LO_ACTS, question_family_id='eea_identify', concept_id='eea', concept_group='acts', misconception_tags=['confuses_eea_with_bcea'], diagnostic_tags=['identification', 'acts']),
        with_metadata({
            'title': 'Basic Conditions of Employment Act',
            'prompt': 'Which Act sets out minimum working hours, leave and notice periods for employees?',
            'options': ['BBBEE Act', 'Basic Conditions of Employment Act (BCEA)', 'Skills Development Act', 'Consumer Protection Act'],
            'correct_index': 1,
            'explanation': 'The BCEA sets the basic conditions of employment such as working hours, leave and notice periods.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on basic conditions like hours and leave.',
                'Working hours/leave/notice = BCEA.',
                'The SDA is about skills and learnerships.',
            ),
            'guidelines': ['Basic conditions (hours/leave) = BCEA.'],
        }, subskill='concepts', learning_objective_id=LO_ACTS, question_family_id='bcea_identify', concept_id='bcea', concept_group='acts', diagnostic_tags=['identification', 'acts']),
        with_metadata({
            'title': 'Skills Development Act',
            'prompt': 'SETAs and learnerships are established mainly under which Act?',
            'options': ['Skills Development Act (SDA)', 'Labour Relations Act', 'COIDA', 'Consumer Protection Act'],
            'correct_index': 0,
            'explanation': 'The Skills Development Act (SDA) provides for SETAs and learnerships to improve the skills of the workforce.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on skills, SETAs and learnerships.',
                'Skills/learnerships/SETAs = Skills Development Act.',
                'The LRA governs unions and disputes.',
            ),
            'guidelines': ['Skills/SETAs/learnerships = SDA.'],
        }, subskill='concepts', learning_objective_id=LO_ACTS, question_family_id='sda_identify', concept_id='sda', concept_group='acts', diagnostic_tags=['identification', 'acts']),
        with_metadata({
            'title': 'Consumer Protection Act',
            'prompt': 'Which Act protects consumers from unfair business practices and gives them the right to safe, good-quality goods?',
            'options': ['National Credit Act', 'Consumer Protection Act (CPA)', 'Employment Equity Act', 'COIDA'],
            'correct_index': 1,
            'explanation': 'The Consumer Protection Act (CPA) protects consumers and gives them rights such as the right to safe, good-quality goods.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on protecting consumers.',
                'Consumer rights to safe, quality goods = CPA.',
                'The NCA focuses on credit and over-indebtedness.',
            ),
            'guidelines': ['Consumer rights/quality goods = CPA.'],
        }, subskill='concepts', learning_objective_id=LO_ACTS, question_family_id='cpa_identify', concept_id='cpa', concept_group='acts', misconception_tags=['confuses_cpa_with_nca'], diagnostic_tags=['identification', 'acts']),
        with_metadata({
            'title': 'COIDA',
            'prompt': 'An employee injured on duty is compensated under which Act?',
            'options': ['COIDA', 'BBBEE Act', 'Skills Development Act', 'National Credit Act'],
            'correct_index': 0,
            'explanation': 'COIDA compensates employees who are injured or contract diseases in the course of their employment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on injury at work and compensation.',
                'Compensation for workplace injury/disease = COIDA.',
                'The EEA deals with discrimination, not injury.',
            ),
            'guidelines': ['Workplace injury compensation = COIDA.'],
        }, subskill='concepts', learning_objective_id=LO_ACTS, question_family_id='coida_identify', concept_id='coida', concept_group='acts', diagnostic_tags=['identification', 'acts']),
        with_metadata({
            'title': 'A pillar of BBBEE',
            'prompt': 'Which of the following is one of the revised FIVE pillars of BBBEE?',
            'options': ['Market penetration', 'Skills development', 'Quality assurance', 'Indemnification'],
            'correct_index': 1,
            'explanation': 'The revised five pillars of BBBEE are ownership, management control, skills development, enterprise and supplier development, and socio-economic development.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recall the five BBBEE pillars.',
                'Skills development is one of the five pillars.',
                'Market penetration is a growth strategy, not a pillar.',
            ),
            'guidelines': ['Skills development is a BBBEE pillar.'],
        }, subskill='concepts', learning_objective_id=LO_BBBEE, question_family_id='bbbee_pillar_identify', concept_id='bbbee_pillars', concept_group='bbbee', diagnostic_tags=['identification', 'bbbee']),
        with_metadata({
            'title': 'Labour Relations Act',
            'prompt': 'Trade unions, collective bargaining and the right to strike are mainly regulated by the …',
            'options': ['Labour Relations Act (LRA)', 'Consumer Protection Act', 'Skills Development Act', 'BCEA'],
            'correct_index': 0,
            'explanation': 'The Labour Relations Act (LRA) regulates trade unions, collective bargaining and the right to strike.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on unions, bargaining and strikes.',
                'Unions/bargaining/strikes = LRA.',
                'The BCEA sets basic employment conditions.',
            ),
            'guidelines': ['Unions/strikes/bargaining = LRA.'],
        }, subskill='concepts', learning_objective_id=LO_ACTS, question_family_id='lra_identify', concept_id='lra', concept_group='acts', diagnostic_tags=['identification', 'acts']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Apply the BBBEE pillars',
            'prompt': 'A medium-sized business wants to improve its BBBEE score. Recommend ways it could apply the revised five pillars of BBBEE in the workplace. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Ownership: sell shares/equity to black shareholders.',
                'Management control: appoint black people into management/board positions.',
                'Skills development: train and develop employees through learnerships.',
                'Enterprise and supplier development / socio-economic development: support black-owned suppliers and community projects.',
            ],
            'sample_answer': 'The business can improve ownership by selling equity to black shareholders, improve management control by appointing black people to management and board positions, and invest in skills development through learnerships. It can also support enterprise and supplier development by procuring from black-owned suppliers and contribute to socio-economic development through community projects.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Apply each of the five pillars.',
                'Ownership, management control, skills, ESD, socio-economic development.',
                'Give a workplace action for each.',
            ),
            'answer_part_hints': ['Name the pillars.', 'Give an action for each.'],
            'guidelines': ['Apply the five pillars with actions.'],
            'teaching_note': 'Reward pillars linked to concrete actions.',
            'keywords': ['ownership', 'management control', 'skills development', 'supplier development', 'socio-economic'],
        }, subskill='application', learning_objective_id=LO_BBBEE, question_family_id='apply_bbbee_scenario', concept_id='bbbee_pillars', concept_group='bbbee', scenario_family_id='improve_bbbee', diagnostic_tags=['scenario_analysis', 'bbbee'], answer_structure_tags=['recommend', 'apply'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Comply with an Act',
            'prompt': 'A factory has been found not to keep records of employees\u2019 working hours and leave. Identify the Act being breached and recommend how the business can comply. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The Act is the Basic Conditions of Employment Act (BCEA).',
                'Keep accurate records of working hours, overtime and leave.',
                'Ensure working hours and leave meet the minimum standards.',
                'Provide written particulars of employment to staff.',
            ],
            'sample_answer': 'The Act being breached is the Basic Conditions of Employment Act (BCEA). To comply, the business should keep accurate records of working hours, overtime and leave, ensure these meet the minimum standards, and give employees written particulars of employment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match working hours/leave to the right Act.',
                'Hours and leave records point to the BCEA.',
                'Compliance means meeting the minimum standards and record-keeping.',
            ),
            'answer_part_hints': ['Name the Act.', 'Recommend compliance steps.'],
            'guidelines': ['Identify the BCEA and give compliance steps.'],
            'teaching_note': 'Reward BCEA plus record-keeping/compliance steps.',
            'keywords': ['BCEA', 'working hours', 'leave', 'records', 'minimum standards'],
        }, subskill='application', learning_objective_id=LO_COMPLIANCE, question_family_id='comply_act_scenario', concept_id='bcea', concept_group='acts', scenario_family_id='hours_records', diagnostic_tags=['scenario_analysis', 'compliance'], answer_structure_tags=['identify', 'recommend'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Impact of the LRA',
            'prompt': 'Discuss the positive and negative impact of the Labour Relations Act (LRA) on businesses. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Positive: provides clear procedures for resolving disputes, reducing conflict.',
                'Positive: promotes fair labour practices and better employer-employee relations.',
                'Positive: gives a structured framework for collective bargaining.',
                'Negative: strikes and lockouts can disrupt production and reduce productivity.',
                'Negative: compliance and dispute processes can be time-consuming and costly.',
            ],
            'sample_answer': 'The LRA positively gives businesses clear procedures for resolving disputes, promotes fair labour practices and provides a structured framework for collective bargaining, which improves employer-employee relations. However, it can negatively affect businesses because strikes and lockouts disrupt production, and compliance with dispute-resolution processes can be time-consuming and costly.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Give both positives and negatives.',
                'Think dispute resolution/fairness (positive) vs strikes/cost (negative).',
                'Balance both sides.',
            ),
            'answer_part_hints': ['Give positives.', 'Give negatives.'],
            'guidelines': ['Provide positives and negatives.'],
            'teaching_note': 'Reward a balanced impact discussion.',
            'keywords': ['dispute', 'fair labour', 'collective bargaining', 'strikes', 'cost'],
        }, subskill='discussion', learning_objective_id=LO_ACTS, question_family_id='lra_impact_discussion', concept_id='lra', concept_group='acts', diagnostic_tags=['discussion', 'evaluation'], answer_structure_tags=['positives', 'negatives'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Role and funding of SETAs',
            'prompt': 'Explain the role of SETAs and how they are funded. (6 marks)',
            'marks': 6,
            'marking_points': [
                'SETAs identify, create and manage learnerships, internships and apprenticeships.',
                'They develop sector skills plans and improve workforce skills.',
                'They administer training in their sector/jurisdiction.',
                'They are funded mainly through the skills development levy paid by employers.',
                'A portion of the levy is paid back to businesses as grants for approved training.',
            ],
            'sample_answer': 'SETAs identify, create and manage learnerships, internships and apprenticeships within their sector, develop sector skills plans and improve workforce skills. They are funded mainly through the skills development levy paid by employers, and a portion of the levy is paid back to businesses as grants for approved training.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain what SETAs do and where their money comes from.',
                'Role = manage learnerships/skills; funding = skills levy.',
                'Mention the levy and grants back to employers.',
            ),
            'answer_part_hints': ['Explain the role.', 'Explain the funding.'],
            'guidelines': ['Cover both role and funding.'],
            'teaching_note': 'Reward role plus the skills levy funding mechanism.',
            'keywords': ['learnerships', 'skills', 'sector', 'skills development levy', 'grants'],
        }, subskill='discussion', learning_objective_id=LO_ACTS, question_family_id='setas_discussion', concept_id='sda', concept_group='acts', diagnostic_tags=['discussion'], answer_structure_tags=['explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
