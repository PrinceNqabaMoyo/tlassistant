"""Grade 12 Business Studies - Term 3 - Human rights, inclusivity and environment.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='human_rights_inclusivity',
    curriculum_reference='Term 3 > Human rights, inclusivity and environmental issues',
    id_prefix='g12_bs_rights',
)

LO_RIGHTS = 'lo_human_rights'
LO_DIVERSITY = 'lo_diversity'
LO_HEALTH = 'lo_health_safety'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Human rights in the workplace',
            'prompt': 'An employer reading employees\u2019 private messages without consent violates the right to …',
            'options': ['privacy', 'freedom of speech', 'safety', 'information'],
            'correct_index': 0,
            'explanation': 'Reading private messages without consent violates the employee\u2019s right to privacy.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on personal information being accessed.',
                'Accessing private messages = privacy violation.',
                'Freedom of speech is about expression.',
            ),
            'guidelines': ['Private messages accessed = privacy.'],
        }, subskill='concepts', learning_objective_id=LO_RIGHTS, question_family_id='privacy_identify', concept_id='privacy', concept_group='rights', misconception_tags=['confuses_privacy_with_freedom_of_speech'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Equality',
            'prompt': 'Fair employment practices without any discrimination, giving everyone equal rights and status, describes …',
            'options': ['dignity', 'equality', 'diversity', 'respect'],
            'correct_index': 1,
            'explanation': 'Equality means fair employment practices without discrimination, where everyone is entitled to equal rights and status.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on equal treatment and no discrimination.',
                'Equal rights, no discrimination = equality.',
                'Dignity is treating people with respect.',
            ),
            'guidelines': ['Equal rights, no discrimination = equality.'],
        }, subskill='concepts', learning_objective_id=LO_RIGHTS, question_family_id='equality_definition', concept_id='equality', concept_group='rights', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Diversity in the workplace',
            'prompt': 'Employing people of different races, genders, ages and cultures reflects workplace …',
            'options': ['diversity', 'equity', 'segregation', 'uniformity'],
            'correct_index': 0,
            'explanation': 'Diversity means having a workforce made up of people who differ in race, gender, age, culture and other characteristics.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on differences among employees.',
                'A mix of different people = diversity.',
                'Uniformity is everyone being the same.',
            ),
            'guidelines': ['A mix of different people = diversity.'],
        }, subskill='concepts', learning_objective_id=LO_DIVERSITY, question_family_id='diversity_definition', concept_id='diversity', concept_group='diversity', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Diversity issue',
            'prompt': 'Which of the following is a diversity issue a business must manage?',
            'options': ['Inflation', 'Gender', 'Interest rates', 'Market share'],
            'correct_index': 1,
            'explanation': 'Diversity issues include poverty, race, gender, language, age, culture/religion and disability.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recall the diversity issues.',
                'Gender is a diversity issue.',
                'Inflation/interest rates are macro factors.',
            ),
            'guidelines': ['Gender = a diversity issue.'],
        }, subskill='concepts', learning_objective_id=LO_DIVERSITY, question_family_id='diversity_issue_identify', concept_id='diversity_issues', concept_group='diversity', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Health and safety representative',
            'prompt': 'A worker appointed to monitor and report on workplace safety issues is a …',
            'options': ['shop steward', 'health and safety representative', 'trade union', 'debt counsellor'],
            'correct_index': 1,
            'explanation': 'A health and safety representative monitors and reports on workplace safety issues to protect the workplace environment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on monitoring workplace safety.',
                'Monitors/reports on safety = health and safety representative.',
                'A shop steward represents union members.',
            ),
            'guidelines': ['Monitors workplace safety = health and safety representative.'],
        }, subskill='concepts', learning_objective_id=LO_HEALTH, question_family_id='health_rep_identify', concept_id='health_safety_rep', concept_group='health', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Dignity',
            'prompt': 'Treating an employee with respect and consideration upholds their right to …',
            'options': ['dignity', 'information', 'freedom of movement', 'privacy'],
            'correct_index': 0,
            'explanation': 'Dignity is upheld when a person is treated with respect and consideration.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on respect and consideration.',
                'Treating someone with respect = dignity.',
                'Privacy is about personal information.',
            ),
            'guidelines': ['Respect/consideration = dignity.'],
        }, subskill='concepts', learning_objective_id=LO_RIGHTS, question_family_id='dignity_definition', concept_id='dignity', concept_group='rights', diagnostic_tags=['definition']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Deal with a diversity issue',
            'prompt': 'A business has employees who speak many different languages, causing miscommunication. Recommend ways the business could deal with this diversity issue. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Use a common business language and translate key documents.',
                'Provide language or communication training.',
                'Use clear, simple communication and visual aids.',
                'Promote respect for different languages and cultures.',
            ],
            'sample_answer': 'The business could agree on a common business language and translate key documents, provide language or communication training, and use clear, simple communication supported by visual aids. It should also promote respect for the different languages and cultures so that all employees feel included.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on managing language diversity.',
                'Common language, translation, training, respect.',
                'Tie each to reducing miscommunication.',
            ),
            'answer_part_hints': ['Give recommendations.', 'Explain each.'],
            'guidelines': ['Provide ways to manage language diversity.'],
            'teaching_note': 'Reward practical ways to manage language diversity.',
            'keywords': ['common language', 'translate', 'training', 'visual aids', 'respect'],
        }, subskill='application', learning_objective_id=LO_DIVERSITY, question_family_id='deal_diversity_scenario', concept_id='diversity_issues', concept_group='diversity', scenario_family_id='language_diversity', diagnostic_tags=['scenario_analysis', 'diversity'], answer_structure_tags=['recommend'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Promote health and safety',
            'prompt': 'After several workplace accidents, a factory wants to improve safety. Explain the responsibilities of the employer in promoting health and safety. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Provide a safe working environment and safe equipment.',
                'Provide protective clothing and safety training.',
                'Identify and reduce hazards and risks.',
                'Appoint health and safety representatives and report incidents.',
            ],
            'sample_answer': 'The employer must provide a safe working environment with safe equipment, supply protective clothing and safety training, and identify and reduce hazards. They should also appoint health and safety representatives and ensure that incidents are reported and investigated.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on the employer\u2019s safety duties.',
                'Safe environment, equipment, training, hazard control.',
                'Mention representatives and reporting.',
            ),
            'answer_part_hints': ['List responsibilities.', 'Explain each.'],
            'guidelines': ['Explain employer health and safety responsibilities.'],
            'teaching_note': 'Reward employer safety responsibilities.',
            'keywords': ['safe environment', 'protective clothing', 'training', 'hazards', 'representatives'],
        }, subskill='application', learning_objective_id=LO_HEALTH, question_family_id='promote_safety_scenario', concept_id='health_safety_rep', concept_group='health', scenario_family_id='factory_safety', diagnostic_tags=['scenario_analysis', 'health'], answer_structure_tags=['explain'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Benefits of diversity',
            'prompt': 'Discuss the benefits of diversity in the workplace. (8 marks)',
            'marks': 8,
            'marking_points': [
                'A wider range of skills, ideas and perspectives improves problem-solving.',
                'Diversity boosts creativity and innovation.',
                'It helps the business understand and serve a diverse customer base.',
                'It improves the business\u2019s reputation and compliance with equity laws.',
                'It creates an inclusive culture that attracts and retains talent.',
            ],
            'sample_answer': 'Diversity brings a wider range of skills, ideas and perspectives, which improves problem-solving and boosts creativity and innovation. It helps the business understand and serve a diverse customer base, improves its reputation and compliance with equity laws, and creates an inclusive culture that attracts and retains talent.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List the benefits of diversity.',
                'Think skills, creativity, customers, reputation, talent.',
                'Explain each briefly.',
            ),
            'answer_part_hints': ['List benefits.', 'Explain each.'],
            'guidelines': ['Provide several benefits.'],
            'teaching_note': 'Reward a range of diversity benefits.',
            'keywords': ['perspectives', 'creativity', 'customers', 'reputation', 'inclusive'],
        }, subskill='discussion', learning_objective_id=LO_DIVERSITY, question_family_id='diversity_benefits_discussion', concept_id='diversity', concept_group='diversity', diagnostic_tags=['discussion'], answer_structure_tags=['list', 'advantages'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Protect the environment and human health',
            'prompt': 'Recommend strategies a business could use to protect the environment and human health. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Reduce, reuse and recycle waste to limit pollution.',
                'Use cleaner technology and renewable energy.',
                'Comply with environmental laws and standards.',
                'Provide a safe, healthy working environment for employees.',
                'Educate employees and the community on environmental responsibility.',
            ],
            'sample_answer': 'A business could reduce, reuse and recycle waste to limit pollution, use cleaner technology and renewable energy, and comply with environmental laws and standards. It should also provide a safe and healthy working environment and educate employees and the community on environmental responsibility.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on environmental and health protection.',
                'Recycle, clean technology, compliance, safe workplace.',
                'Explain each strategy briefly.',
            ),
            'answer_part_hints': ['Give strategies.', 'Explain each.'],
            'guidelines': ['Provide environmental and health strategies.'],
            'teaching_note': 'Reward practical protection strategies.',
            'keywords': ['recycle', 'clean technology', 'comply', 'safe workplace', 'educate'],
        }, subskill='discussion', learning_objective_id=LO_HEALTH, question_family_id='protect_environment_discussion', concept_id='environment', concept_group='health', diagnostic_tags=['discussion', 'recommendation'], answer_structure_tags=['recommend', 'list'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
