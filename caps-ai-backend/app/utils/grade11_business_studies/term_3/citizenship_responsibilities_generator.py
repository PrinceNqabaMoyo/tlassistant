"""Grade 11 Business Studies - Term 3 - Topic 14: Citizenship and
responsibilities.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='citizenship_responsibilities',
    curriculum_reference='Term 3 > Citizenship and responsibilities',
    id_prefix='g11_bs_citizen',
)

LO_CITIZENSHIP = 'lo_citizenship_rights_responsibilities'
LO_INVOLVEMENT = 'lo_business_social_involvement'
LO_ROLES = 'lo_roles_in_development'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Citizenship',
            'prompt': 'The status of a person being part of a country with all its rights, privileges and duties is …',
            'options': ['citizenship', 'civil society', 'governance', 'responsibility'],
            'correct_index': 0,
            'explanation': 'Citizenship is the status of a person being part of a country with all its rights, privileges and duties.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify belonging to a country.',
                'Citizenship = being part of a country with rights and duties.',
                'Civil society refers to non-government organisations.',
            ),
            'guidelines': ['Link "part of a country with rights/duties" to citizenship.'],
        }, subskill='concepts', learning_objective_id=LO_CITIZENSHIP, question_family_id='citizenship_definition', concept_id='citizenship', concept_group='citizenship', misconception_tags=['confuses_citizenship_with_civil_society'], diagnostic_tags=['definition', 'citizenship']),
        with_metadata({
            'title': 'Civil society',
            'prompt': 'The collective name for organisations and associations that are NOT part of the government is …',
            'options': ['civil society', 'citizenship', 'the state', 'a CBO'],
            'correct_index': 0,
            'explanation': 'Civil society is the collective name given to organisations and associations that are not part of the government.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify non-government groupings.',
                'Civil society = organisations outside government.',
                'A CBO is one specific type of community group.',
            ),
            'guidelines': ['Non-government organisations collectively = civil society.'],
        }, subskill='concepts', learning_objective_id=LO_ROLES, question_family_id='civil_society_definition', concept_id='civil_society', concept_group='roles', misconception_tags=['confuses_civil_society_with_government'], diagnostic_tags=['definition', 'roles']),
        with_metadata({
            'title': 'NGO',
            'prompt': 'People grouping themselves into an organisation to fulfil duties in society that the government is not meeting form a(n) …',
            'options': ['CBO', 'NGO', 'SOE', 'JSE'],
            'correct_index': 1,
            'explanation': 'A non-governmental organisation (NGO) is people grouping themselves to fulfil duties in society that the government is not meeting.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the non-government body.',
                'NGOs fill gaps the government does not meet.',
                'CBOs are volunteer-based and operate locally.',
            ),
            'guidelines': ['Fills gaps government misses = NGO.'],
        }, subskill='concepts', learning_objective_id=LO_ROLES, question_family_id='ngo_definition', concept_id='ngo', concept_group='roles', misconception_tags=['confuses_ngo_with_cbo'], diagnostic_tags=['definition', 'roles']),
        with_metadata({
            'title': 'CBO',
            'prompt': 'People forming volunteer-based groups to provide services at a local level form a(n) …',
            'options': ['NGO', 'CBO', 'SOC', 'MOI'],
            'correct_index': 1,
            'explanation': 'A community-based organisation (CBO) is people forming volunteer-based groups to provide services at a local level.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the local volunteer group.',
                'CBOs are volunteer-based and local.',
                'NGOs are usually larger and broader than CBOs.',
            ),
            'guidelines': ['Local volunteer-based group = CBO.'],
        }, subskill='concepts', learning_objective_id=LO_ROLES, question_family_id='cbo_definition', concept_id='cbo', concept_group='roles', misconception_tags=['confuses_cbo_with_ngo'], diagnostic_tags=['definition', 'roles']),
        with_metadata({
            'title': 'Rights vs responsibilities',
            'prompt': 'The duty one has to behave correctly or answer to certain obligations is called a …',
            'options': ['right', 'responsibility', 'privilege', 'freedom'],
            'correct_index': 1,
            'explanation': 'Responsibilities are the duties one has to answer to obligations or to behave correctly in certain situations (rights are entitlements).',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Distinguish duties from entitlements.',
                'A duty/obligation = responsibility.',
                'A right is an entitlement to have or do something.',
            ),
            'guidelines': ['Duty/obligation = responsibility.'],
        }, subskill='concepts', learning_objective_id=LO_CITIZENSHIP, question_family_id='responsibility_definition', concept_id='responsibilities', concept_group='citizenship', misconception_tags=['confuses_rights_with_responsibilities'], diagnostic_tags=['definition', 'citizenship']),
        with_metadata({
            'title': 'Reason for social involvement',
            'prompt': 'Which of the following is a reason a business becomes involved in social programmes?',
            'options': [
                'To avoid paying any taxes',
                'To comply with BBBEE and address skills shortages',
                'To reduce product quality',
                'To ignore the community',
            ],
            'correct_index': 1,
            'explanation': 'Businesses become involved in social programmes to comply with BBBEE, address the lack of qualified workers, and respond to issues such as HIV/AIDS.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify a genuine reason for involvement.',
                'Compliance (BBBEE) and skills shortages are real reasons.',
                'Avoiding tax or lowering quality are not reasons.',
            ),
            'guidelines': ['Look for compliance/skills/community reasons.'],
        }, subskill='concepts', learning_objective_id=LO_INVOLVEMENT, question_family_id='reason_involvement_identification', concept_id='social_involvement', concept_group='involvement', misconception_tags=['confuses_social_involvement_with_tax_avoidance'], diagnostic_tags=['identification', 'involvement']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Identify a development initiative',
            'prompt': 'A construction company funds a local skills-training centre and offers bursaries to learners. Identify how the business contributes to community development and recommend ONE further role it could play. (4 marks)',
            'marks': 4,
            'marking_points': [
                'It contributes to social and economic development through education/skills.',
                'Bursaries and a training centre build skills and employability.',
                'Further role: create jobs / support local suppliers.',
                'Further role: fund healthcare, infrastructure or other social programmes.',
            ],
            'sample_answer': 'The company contributes to social and economic development by funding a skills-training centre and bursaries, which builds skills and employability in the community. A further role it could play is to create jobs and support local suppliers, or fund healthcare and infrastructure programmes.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the contribution, then add a role.',
                'Skills and bursaries support social/economic development.',
                'Further roles include jobs, suppliers, healthcare.',
            ),
            'answer_part_hints': ['Identify the contribution.', 'Recommend a further role.'],
            'guidelines': ['Use scenario evidence plus a recommendation.'],
            'teaching_note': 'Reward identifying the contribution and adding a valid role.',
            'keywords': ['development', 'skills', 'bursaries', 'jobs', 'community', 'training'],
        }, subskill='application', learning_objective_id=LO_INVOLVEMENT, question_family_id='identify_initiative_scenario', concept_id='social_involvement', concept_group='involvement', scenario_family_id='construction_skills_centre', diagnostic_tags=['scenario_analysis', 'involvement'], answer_structure_tags=['identify', 'recommend'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Role of an institution',
            'prompt': 'A flood damages homes in a township. Suggest how a non-governmental organisation (NGO) and a community-based organisation (CBO) could each contribute to the community\'s recovery. (4 marks)',
            'marks': 4,
            'marking_points': [
                'NGO: mobilise larger-scale relief, funding and coordination.',
                'NGO: provide expertise/resources the government is not meeting.',
                'CBO: organise local volunteers to deliver immediate help.',
                'CBO: provide services at a local level (food, shelter, clean-up).',
            ],
            'sample_answer': 'An NGO could mobilise larger-scale relief, funding and coordination, providing resources and expertise that the government is not meeting. A CBO could organise local volunteers to deliver immediate help at a local level, such as food, shelter and clean-up for affected households.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match each institution to its role.',
                'NGOs work broadly; CBOs work locally with volunteers.',
                'Tie each role to the recovery need.',
            ),
            'answer_part_hints': ['Give the NGO role.', 'Give the CBO role.'],
            'guidelines': ['Distinguish the NGO from the CBO role.'],
            'teaching_note': 'Reward distinct, appropriate roles for NGO and CBO.',
            'keywords': ['NGO', 'CBO', 'relief', 'volunteers', 'local', 'community'],
        }, subskill='application', learning_objective_id=LO_ROLES, question_family_id='institution_role_scenario', concept_id='ngo', concept_group='roles', scenario_family_id='township_flood', diagnostic_tags=['scenario_analysis', 'roles'], answer_structure_tags=['apply', 'distinguish'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Why businesses become involved in social programmes',
            'prompt': 'Explain the reasons why businesses have to become involved in social programmes. (6 marks)',
            'marks': 6,
            'marking_points': [
                'To comply with legislation such as BBBEE.',
                'To address the lack of qualified workers (skills development).',
                'To respond to social issues such as the effect of HIV/AIDS.',
                'To build reputation, goodwill and a sustainable operating environment.',
            ],
            'sample_answer': 'Businesses become involved in social programmes to comply with legislation such as BBBEE, to address the shortage of qualified workers through skills development, and to respond to social issues such as the effect of HIV/AIDS. Involvement also builds reputation and goodwill and creates a more stable, sustainable environment for the business.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List reasons for involvement.',
                'Think compliance, skills and social issues.',
                'Involvement also builds reputation and sustainability.',
            ),
            'answer_part_hints': ['Give several reasons.', 'Explain each.'],
            'guidelines': ['Provide at least three reasons.'],
            'teaching_note': 'Reward distinct reasons from the curriculum.',
            'keywords': ['BBBEE', 'skills', 'qualified workers', 'HIV/AIDS', 'reputation', 'sustainable'],
        }, subskill='discussion', learning_objective_id=LO_INVOLVEMENT, question_family_id='reasons_involvement_discussion', concept_id='social_involvement', concept_group='involvement', diagnostic_tags=['discussion', 'involvement'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Rights and responsibilities of citizens',
            'prompt': 'Outline the rights and responsibilities of citizens. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Rights: e.g. the right to education, safety and owning property.',
                'Rights are legal/moral entitlements citizens may claim.',
                'Responsibilities: obeying the law and respecting others\' rights.',
                'Responsibilities: contributing to society and acting correctly.',
            ],
            'sample_answer': 'Citizens have rights such as the right to education, safety and owning property - legal and moral entitlements they may claim. They also have responsibilities, such as obeying the law, respecting the rights of others, paying taxes and contributing positively to society by behaving correctly.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Cover both rights and responsibilities.',
                'Rights are entitlements; responsibilities are duties.',
                'Give examples of each.',
            ),
            'answer_part_hints': ['Give rights.', 'Give responsibilities.'],
            'guidelines': ['Address both rights and responsibilities.'],
            'teaching_note': 'Reward balanced coverage of rights and responsibilities.',
            'keywords': ['rights', 'education', 'safety', 'property', 'responsibilities', 'obey the law'],
        }, subskill='discussion', learning_objective_id=LO_CITIZENSHIP, question_family_id='rights_responsibilities_discussion', concept_id='citizenship', concept_group='citizenship', diagnostic_tags=['discussion', 'citizenship'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
