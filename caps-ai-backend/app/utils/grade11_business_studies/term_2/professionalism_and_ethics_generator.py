"""Grade 11 Business Studies - Term 2 - Topic 12: Professionalism and ethics.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='professionalism_and_ethics',
    curriculum_reference='Term 2 > Professionalism and ethics',
    id_prefix='g11_bs_ethics',
)

LO_CONCEPTS = 'lo_professionalism_ethics_concepts'
LO_THEORIES = 'lo_theories_of_ethics'
LO_PRACTICE = 'lo_ethical_business_practice'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Ethics',
            'prompt': 'The moral principles that govern a person\'s behaviour when conducting an activity are called …',
            'options': ['professionalism', 'ethics', 'legislation', 'culture'],
            'correct_index': 1,
            'explanation': 'Ethics refers to the moral principles that govern a person\'s behaviour, or the moral principles applied when conducting an activity.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the moral principles.',
                'Ethics = moral principles of right and wrong.',
                'Professionalism is about applying skills/knowledge in a job.',
            ),
            'guidelines': ['Link "moral principles" to ethics.'],
        }, subskill='concepts', learning_objective_id=LO_CONCEPTS, question_family_id='ethics_definition', concept_id='ethics', concept_group='concepts', misconception_tags=['confuses_ethics_with_professionalism'], diagnostic_tags=['definition', 'ethics']),
        with_metadata({
            'title': 'Professionalism',
            'prompt': 'When people with specific skills and abilities use their knowledge in a specific job or profession, this is called …',
            'options': ['ethics', 'professionalism', 'morality', 'corruption'],
            'correct_index': 1,
            'explanation': 'Professionalism is when people with specific skills and abilities use their knowledge in a specific job or profession.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify applying skills in a job.',
                'Professionalism = using skills/knowledge in a profession.',
                'Ethics is about moral right and wrong.',
            ),
            'guidelines': ['Link "skills/knowledge in a job" to professionalism.'],
        }, subskill='concepts', learning_objective_id=LO_CONCEPTS, question_family_id='professionalism_definition', concept_id='professionalism', concept_group='concepts', misconception_tags=['confuses_professionalism_with_ethics'], diagnostic_tags=['definition', 'professionalism']),
        with_metadata({
            'title': 'Consequential theory',
            'prompt': 'An ethical theory that judges whether an action is right based on its outcomes/consequences is the …',
            'options': ['rights approach', 'consequential theory', 'common good approach', 'virtue theory'],
            'correct_index': 1,
            'explanation': 'The consequential theory judges whether an action is right or wrong based on its outcomes/consequences.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on what the theory looks at.',
                'Consequential theory judges by outcomes/consequences.',
                'The rights approach focuses on protecting rights instead.',
            ),
            'guidelines': ['Judging by outcomes = consequential theory.'],
        }, subskill='concepts', learning_objective_id=LO_THEORIES, question_family_id='consequential_theory_definition', concept_id='consequential_theory', concept_group='theories', misconception_tags=['confuses_consequential_with_rights'], diagnostic_tags=['definition', 'theories']),
        with_metadata({
            'title': 'Common good approach',
            'prompt': 'An ethical approach that judges actions by how well they serve the welfare of the whole community is the …',
            'options': ['rights approach', 'consequential theory', 'common good approach', 'self-interest theory'],
            'correct_index': 2,
            'explanation': 'The common good approach judges actions by how well they serve the welfare/interests of the whole community.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on whose interests matter.',
                'Common good = welfare of the whole community.',
                'The rights approach focuses on individual rights.',
            ),
            'guidelines': ['Welfare of the community = common good approach.'],
        }, subskill='concepts', learning_objective_id=LO_THEORIES, question_family_id='common_good_definition', concept_id='common_good_approach', concept_group='theories', misconception_tags=['confuses_common_good_with_rights'], diagnostic_tags=['definition', 'theories']),
        with_metadata({
            'title': 'Rights approach',
            'prompt': 'An ethical approach that judges actions by whether they respect and protect the rights of those affected is the …',
            'options': ['rights approach', 'consequential theory', 'common good approach', 'profit approach'],
            'correct_index': 0,
            'explanation': 'The rights approach judges actions by whether they respect and protect the moral rights of those affected.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on what is protected.',
                'Rights approach = protecting people\'s rights.',
                'Consequential theory focuses on outcomes.',
            ),
            'guidelines': ['Protecting rights = rights approach.'],
        }, subskill='concepts', learning_objective_id=LO_THEORIES, question_family_id='rights_approach_definition', concept_id='rights_approach', concept_group='theories', misconception_tags=['confuses_rights_with_consequential'], diagnostic_tags=['definition', 'theories']),
        with_metadata({
            'title': 'Ethical business practice',
            'prompt': 'Which of the following is an example of ethical business practice?',
            'options': [
                'Paying workers below the minimum wage',
                'Paying fair wages and providing quality goods',
                'Selling counterfeit goods',
                'Misleading customers in adverts',
            ],
            'correct_index': 1,
            'explanation': 'Ethical business practices include paying fair wages, providing quality goods and services, and not building a business at someone else\'s expense.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the morally right practice.',
                'Fair wages and quality goods are ethical.',
                'Counterfeits and misleading adverts are unethical.',
            ),
            'guidelines': ['Look for fair, honest treatment of stakeholders.'],
        }, subskill='concepts', learning_objective_id=LO_PRACTICE, question_family_id='ethical_practice_identification', concept_id='ethical_practice', concept_group='practice', misconception_tags=['confuses_ethical_with_unethical'], diagnostic_tags=['identification', 'practice']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Apply an ethical theory',
            'prompt': 'A factory considers dumping waste in a river to save money. Using the common good approach, explain whether this decision is ethical. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The common good approach considers the welfare of the whole community.',
                'Dumping waste harms the community (health, water, environment).',
                'It serves the business\'s interest at the community\'s expense.',
                'Therefore the decision is unethical under the common good approach.',
            ],
            'sample_answer': 'Under the common good approach, an action is ethical if it serves the welfare of the whole community. Dumping waste in the river harms the community\'s health, water and environment for the business\'s own gain, so the decision is unethical.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Apply the named theory to the case.',
                'Common good = community welfare comes first.',
                'Weigh community harm against business gain.',
            ),
            'answer_part_hints': ['State what the theory looks at.', 'Apply it to the decision.'],
            'guidelines': ['Apply the theory, do not just define it.'],
            'teaching_note': 'Reward applying the common good approach to reach a judgement.',
            'keywords': ['common good', 'community', 'welfare', 'harm', 'unethical', 'environment'],
        }, subskill='application', learning_objective_id=LO_THEORIES, question_family_id='apply_theory_scenario', concept_id='common_good_approach', concept_group='theories', scenario_family_id='factory_waste', diagnostic_tags=['scenario_analysis', 'theories'], answer_structure_tags=['apply', 'judge'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Good vs bad decision',
            'prompt': 'A manager discovers a product defect but ships the goods anyway to meet a deadline. Identify whether this is a good or bad ethical decision and recommend the ethical action. (4 marks)',
            'marks': 4,
            'marking_points': [
                'This is a bad (unethical) decision.',
                'It puts profit/deadlines above customer safety and honesty.',
                'Ethical action: hold the goods and fix the defect / inform customers.',
                'Provide quality goods and act honestly with stakeholders.',
            ],
            'sample_answer': 'This is a bad, unethical decision because it puts the deadline and profit above customer safety and honesty. The ethical action is to hold the defective goods, fix the defect and provide quality products, being honest with customers rather than shipping faulty goods.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Judge the decision, then recommend.',
                'Shipping known defects harms customers = unethical.',
                'Ethical action provides quality goods honestly.',
            ),
            'answer_part_hints': ['Classify the decision.', 'Recommend the ethical action.'],
            'guidelines': ['Justify and recommend.'],
            'teaching_note': 'Reward correct judgement plus an ethical recommendation.',
            'keywords': ['unethical', 'defect', 'honesty', 'quality', 'customers', 'safety'],
        }, subskill='application', learning_objective_id=LO_PRACTICE, question_family_id='good_bad_decision_scenario', concept_id='ethical_practice', concept_group='practice', scenario_family_id='defect_shipment', diagnostic_tags=['scenario_analysis', 'practice'], answer_structure_tags=['identify', 'recommend'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Theories of ethics',
            'prompt': 'Briefly explain the consequential theory, the common good approach and the rights approach as theories of ethics that apply to the workplace. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Consequential theory: judges actions by their outcomes/consequences.',
                'Common good approach: judges actions by the welfare of the whole community.',
                'Rights approach: judges actions by whether they respect/protect rights.',
                'Each theory is explained distinctly.',
            ],
            'sample_answer': 'The consequential theory judges whether an action is right based on its outcomes or consequences. The common good approach judges actions by how well they serve the welfare of the whole community. The rights approach judges actions by whether they respect and protect the rights of those affected.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain each theory distinctly.',
                'Consequences, community welfare, rights - one each.',
                'Keep the three theories clearly separate.',
            ),
            'answer_part_hints': ['Explain each theory.', 'Keep them distinct.'],
            'guidelines': ['Cover all three theories.'],
            'teaching_note': 'Reward distinct, accurate explanations of all three theories.',
            'keywords': ['consequential', 'outcomes', 'common good', 'community', 'rights', 'protect'],
        }, subskill='discussion', learning_objective_id=LO_THEORIES, question_family_id='theories_of_ethics_discussion', concept_id='theories', concept_group='theories', diagnostic_tags=['discussion', 'theories'], answer_structure_tags=['explain', 'distinguish'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Benefits of ethical business ventures',
            'prompt': 'Discuss the advantages/benefits of ethical business ventures. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Builds a good reputation and customer trust/loyalty.',
                'Attracts and retains good employees and investors.',
                'Reduces legal risk and the cost of misconduct.',
                'Supports long-term sustainability and community goodwill.',
            ],
            'sample_answer': 'Ethical business ventures build a good reputation and earn customer trust and loyalty, which increases sales. They attract and retain good employees and investors, reduce the legal risk and cost of misconduct, and support long-term sustainability and community goodwill.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List benefits of acting ethically.',
                'Think reputation, trust, talent and risk.',
                'Ethics also supports long-term sustainability.',
            ),
            'answer_part_hints': ['Give several benefits.', 'Explain each.'],
            'guidelines': ['Provide at least three benefits.'],
            'teaching_note': 'Reward distinct, business-linked benefits of ethics.',
            'keywords': ['ethical', 'reputation', 'trust', 'loyalty', 'employees', 'sustainability'],
        }, subskill='discussion', learning_objective_id=LO_PRACTICE, question_family_id='benefits_of_ethics_discussion', concept_id='ethical_practice', concept_group='practice', diagnostic_tags=['discussion', 'practice'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
