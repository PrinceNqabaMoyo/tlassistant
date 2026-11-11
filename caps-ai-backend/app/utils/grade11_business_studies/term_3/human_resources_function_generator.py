"""Grade 11 Business Studies - Term 3 - Topic 18: Introduction to the human resources function.

Grounded in curriculum_docs_auto/BusinessStudies_Gr11/Term 3/04. Introduction to the human resources function.md.
Covers:
- Recruitment: internal vs. external recruitment, job description vs. job specification.
- Selection: screening, shortlisting, interviewing, reference checks, job offer.
- Induction and placement: purpose, benefits, matching competencies to job requirements.
- Salary determination methods: piecemeal vs. time-related, gross vs. net salary, deductions, fringe benefits.
- Implications of legislation on HR: BCEA, LRA, EEA, SDA.

Deterministic generator (seeded RNG + curated South African CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='human_resources_function',
    curriculum_reference='Term 3 > Introduction to the human resources function',
    id_prefix='g11_bs_hr',
)

LO_RECRUITMENT = 'lo_recruitment_selection'
LO_INDUCTION = 'lo_induction_placement'
LO_SALARY = 'lo_salary_fringe_benefits'
LO_LEGISLATION = 'lo_hr_legislation'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Job description vs Job specification',
            'prompt': 'A written summary of the key responsibilities, duties, and working conditions of a job is known as a …',
            'options': ['job specification', 'job description', 'employment contract', 'performance appraisal'],
            'correct_index': 1,
            'explanation': 'A job description outlines the duties, responsibilities, and tasks of the post, whereas a job specification specifies the qualifications, skills, and personal attributes required.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on what describes the job duties.',
                'Job description = tasks, duties, and responsibilities.',
                'Job specification = qualifications and personal traits.',
            ),
            'guidelines': ['Duties of the post = job description.'],
        }, subskill='concepts', learning_objective_id=LO_RECRUITMENT, question_family_id='job_desc_vs_spec', concept_id='job_description', concept_group='recruitment', misconception_tags=['confuses_description_with_specification'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Internal vs External Recruitment',
            'prompt': 'Which of the following is an advantage of internal recruitment?',
            'options': [
                'Brings new skills and innovative ideas into the business',
                'Candidate is already familiar with company culture and procedures',
                'Minimises resentment among colleagues who were not promoted',
                'Creates a larger pool of diverse applicants'
            ],
            'correct_index': 1,
            'explanation': 'Internal recruitment uses existing employees who already know the business culture, policies, and operating systems, reducing induction time and training costs.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Consider existing staff knowledge.',
                'Current employees already understand business processes.',
                'External recruitment brings new ideas but is more expensive.',
            ),
            'guidelines': ['Familiarity with business systems = internal recruitment benefit.'],
        }, subskill='concepts', learning_objective_id=LO_RECRUITMENT, question_family_id='internal_recruitment_benefit', concept_id='recruitment_methods', concept_group='recruitment', misconception_tags=['confuses_internal_and_external_recruitment'], diagnostic_tags=['benefits']),
        with_metadata({
            'title': 'Selection procedure steps',
            'prompt': 'What is the correct sequence of the initial steps in a professional selection procedure?',
            'options': [
                'Interviewing -> Shortlisting -> Screening applications -> Employment offer',
                'Screening applications -> Shortlisting candidates -> Conducting interviews -> Reference checks',
                'Conducting interviews -> Job offer -> Screening -> Medical examination',
                'Reference checks -> Advertising -> Induction -> Shortlisting'
            ],
            'correct_index': 1,
            'explanation': 'The selection procedure begins with screening all CVs against minimum criteria, shortlisting suitable candidates, interviewing them, and conducting reference checks.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Think about filtering applicants from many to few.',
                'Screen all applications first to eliminate unqualified CVs.',
                'Shortlist the top contenders before calling them for interviews.',
            ),
            'guidelines': ['Screening -> Shortlisting -> Interviews -> Reference checks.'],
        }, subskill='concepts', learning_objective_id=LO_RECRUITMENT, question_family_id='selection_sequence', concept_id='selection_procedure', concept_group='selection', misconception_tags=['inverts_selection_sequence'], diagnostic_tags=['procedure']),
        with_metadata({
            'title': 'Salary determination: Piecemeal vs Time-related',
            'prompt': 'A salary system where employees are paid according to the number of units produced or items completed is called …',
            'options': ['time-related pay', 'piecemeal system', 'commission on sales', 'fringe benefit system'],
            'correct_index': 1,
            'explanation': 'Under the piecemeal (piece rate) system, remuneration is directly linked to the volume of output produced, unlike time-related pay which pays for hours worked.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on payment per unit of output.',
                'Piecemeal = paid per piece/unit made.',
                'Time-related = paid per hour, day, or month.',
            ),
            'guidelines': ['Pay per unit produced = piecemeal system.'],
        }, subskill='concepts', learning_objective_id=LO_SALARY, question_family_id='piecemeal_vs_time', concept_id='remuneration_systems', concept_group='salary', misconception_tags=['confuses_piecemeal_with_timerelated'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'BCEA Leave Provisions',
            'prompt': 'According to the Basic Conditions of Employment Act (BCEA), how many days of paid annual leave is a full-time worker entitled to per year?',
            'options': ['14 consecutive days', '21 consecutive days (or 1 day per 17 days worked)', '30 working days', '10 days at employer discretion'],
            'correct_index': 1,
            'explanation': 'The BCEA entitles full-time employees to a minimum of 21 consecutive days of paid annual leave per annual cycle (or 1 day for every 17 days worked).',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recall standard South African labour standards.',
                'The BCEA sets statutory annual leave at 21 consecutive days.',
                'Sick leave is 30 days over a 3-year cycle.',
            ),
            'guidelines': ['Statutory annual leave = 21 consecutive days.'],
        }, subskill='concepts', learning_objective_id=LO_LEGISLATION, question_family_id='bcea_leave_provisions', concept_id='bcea_compliance', concept_group='legislation', misconception_tags=['misremembers_statutory_leave_days'], diagnostic_tags=['legislation']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Gross vs Net Salary Calculation',
            'prompt': 'Sipho earns a gross monthly salary of R24,000. His compulsory deductions are: PAYE tax R3,600, Pension fund (7.5%) R1,800, Medical Aid R1,500, and UIF (1%) R177.12. Calculate Sipho’s net take-home salary. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Identify total deductions: R3,600 + R1,800 + R1,500 + R177.12 = R7,077.12.',
                'Formula: Net Salary = Gross Salary - Total Deductions.',
                'Calculate net salary: R24,000 - R7,077.12.',
                'Final answer: R16,922.88.',
            ],
            'sample_answer': 'Total Deductions = R3,600 + R1,800 + R1,500 + R177.12 = R7,077.12. Net Salary = R24,000 - R7,077.12 = R16,922.88.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Remember: Net = Gross minus all deductions.',
                'Sum all deductions first (PAYE + Pension + Medical Aid + UIF).',
                'Subtract total deductions from the gross salary.',
            ),
            'answer_part_hints': ['Find total deductions.', 'Subtract from gross.'],
            'guidelines': ['Total deductions = R7,077.12; Net = R16,922.88.'],
            'teaching_note': 'Ensure learners understand that UIF is capped at 1% of statutory earnings and deducts from gross.',
            'keywords': ['gross', 'net salary', 'PAYE', 'UIF', 'deductions', 'take-home pay'],
        }, subskill='application', learning_objective_id=LO_SALARY, question_family_id='net_salary_calc', concept_id='salary_deductions', concept_group='salary', diagnostic_tags=['calculation', 'salary'], answer_structure_tags=['calculate', 'stepwise'], minimum_mastery_score=0.7),
        with_metadata({
            'title': 'Job Specification Formulation',
            'prompt': 'Khaya Logistics is expanding its freight operations in Durban and needs a Senior Warehouse Controller. Outline THREE requirements that should be listed in the job specification rather than the job description. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Minimum educational qualification (e.g. Diploma in Supply Chain or Logistics Management).',
                'Required work experience (e.g. 5+ years experience managing warehouse dispatch).',
                'Specialised skills/certifications (e.g. Forklift operator licence, ERP inventory software proficiency).',
                'Key personal traits/attributes (e.g. strong leadership, ability to work night shifts).',
            ],
            'sample_answer': 'Three requirements for the job specification: 1. Relevant qualification such as a Diploma in Logistics or Supply Chain Management. 2. Minimum of 5 years warehouse supervisory experience. 3. Specialised skills and licences, such as valid forklift certification and proficiency in warehouse inventory software.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Job specification focuses on the person, not the task.',
                'Include qualifications, years of experience, and technical skills.',
                'Do not list duties like packing boxes (that is the job description).',
            ),
            'answer_part_hints': ['Give three personal/professional requirements.', 'Focus on candidate qualifications.'],
            'guidelines': ['State 3 candidate requirements with brief context.'],
            'teaching_note': 'Do not accept job tasks (e.g. managing stock). Only candidate attributes (qualifications, experience, licences).',
            'keywords': ['job specification', 'qualifications', 'experience', 'licence', 'attributes'],
        }, subskill='application', learning_objective_id=LO_RECRUITMENT, question_family_id='job_spec_formulation', concept_id='job_specification', concept_group='recruitment', diagnostic_tags=['scenario', 'recruitment'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Benefits of a formal induction program',
            'prompt': 'Explain the importance and benefits of a well-structured induction program for newly appointed employees. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Helps new employees feel welcomed, valued, and settled in their new workplace.',
                'Familiarises new staff with company policies, health and safety rules, and operational routines.',
                'Reduces initial anxiety and increases employee confidence and productivity quickly.',
                'Reduces staff turnover and early resignations by establishing clear expectations from day one.',
            ],
            'sample_answer': 'A well-structured induction program helps new employees feel welcomed and valued, reducing anxiety and settling them into the business culture. It familiarises them with organizational policies, safety procedures, and job expectations, which improves early productivity and reduces costly staff turnover.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain how induction helps both employee and employer.',
                'Induction orientation lowers anxiety and clarifies workplace rules.',
                'It leads to higher job satisfaction and lower staff turnover.',
            ),
            'answer_part_hints': ['State benefits for employee.', 'State benefits for the business.'],
            'guidelines': ['Provide three distinct benefits with explanation.'],
            'teaching_note': 'Reward clear explanations linking orientation to workplace performance and retention.',
            'keywords': ['induction', 'orientation', 'turnover', 'culture', 'policies', 'productivity'],
        }, subskill='discussion', learning_objective_id=LO_INDUCTION, question_family_id='induction_benefits_discussion', concept_id='induction_program', concept_group='induction', diagnostic_tags=['discussion', 'induction'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Employment Equity Act compliance in HR',
            'prompt': 'Discuss how human resources managers must apply the Employment Equity Act (EEA) during recruitment and selection. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Ensure job advertisements do not discriminate unfairly based on race, gender, disability, or age.',
                'Implement affirmative action measures to ensure designated groups have equal employment opportunities.',
                'Use objective, non-biased criteria and psychometric tests that are scientifically validated and culturally fair.',
                'Formulate and submit an Employment Equity plan with measurable numerical goals for workplace transformation.',
            ],
            'sample_answer': 'HR managers must ensure that recruitment advertisements and selection criteria do not unfairly discriminate on the grounds of race, gender, disability, or religion. They must implement affirmative action measures to provide designated groups with equitable representation, use culturally fair selection tests, and align hiring with the company’s Employment Equity transformation plan.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on fair labour practices and affirmative action.',
                'The EEA prohibits unfair discrimination in adverts and interviews.',
                'Affirmative action promotes designated groups (black people, women, people with disabilities).',
            ),
            'answer_part_hints': ['Discuss non-discrimination.', 'Discuss affirmative action measures.'],
            'guidelines': ['Provide three distinct points discussing non-discrimination and transformation.'],
            'teaching_note': 'Reward references to designated groups, non-discriminatory advertising, and affirmative action.',
            'keywords': ['Employment Equity Act', 'affirmative action', 'designated groups', 'discrimination', 'transformation'],
        }, subskill='discussion', learning_objective_id=LO_LEGISLATION, question_family_id='eea_hr_compliance_discussion', concept_id='eea_legislation', concept_group='legislation', diagnostic_tags=['discussion', 'legislation'], answer_structure_tags=['list', 'discuss'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
