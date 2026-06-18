"""Grade 12 Business Studies - Term 1 - Ethics and professionalism.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='ethics_and_professionalism',
    curriculum_reference='Term 1 > Ethics and professionalism',
    id_prefix='g12_bs_ethics',
)

LO_CONCEPTS = 'lo_ethics_concepts'
LO_KING = 'lo_king_code'
LO_UNETHICAL = 'lo_unethical_unprofessional'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Ethical behaviour',
            'prompt': 'Acting according to a set of values that is morally acceptable in society is …',
            'options': ['professional behaviour', 'ethical behaviour', 'corporate governance', 'a code of conduct'],
            'correct_index': 1,
            'explanation': 'Ethical behaviour means acting according to a set of values that is morally acceptable in society.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on morally acceptable values.',
                'Acting on what is morally right = ethical behaviour.',
                'Professionalism is broader and covers conduct/competence.',
            ),
            'guidelines': ['Morally acceptable values = ethical behaviour.'],
        }, subskill='concepts', learning_objective_id=LO_CONCEPTS, question_family_id='ethical_behaviour_definition', concept_id='ethical_behaviour', concept_group='concepts', misconception_tags=['confuses_ethics_with_professionalism'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Professionalism',
            'prompt': 'The accepted standards and expectations of people\u2019s conduct and competence in the workplace (including appearance and attitude) describes …',
            'options': ['ethics', 'professionalism', 'business ethics', 'a code of conduct'],
            'correct_index': 1,
            'explanation': 'Professionalism describes the accepted standards and expectations of people\u2019s conduct and competence in the workplace; it is broader than ethics and includes appearance, attitude and loyalty.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on workplace conduct and competence.',
                'Standards of conduct/competence at work = professionalism.',
                'Ethics is specifically about what is morally right.',
            ),
            'guidelines': ['Workplace conduct/competence standards = professionalism.'],
        }, subskill='concepts', learning_objective_id=LO_CONCEPTS, question_family_id='professionalism_definition', concept_id='professionalism', concept_group='concepts', misconception_tags=['confuses_professionalism_with_ethics'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Corporate governance',
            'prompt': 'The exercise of ethical and effective leadership by those responsible for managing a business is …',
            'options': ['corporate governance', 'business ethics', 'professionalism', 'an AGM'],
            'correct_index': 0,
            'explanation': 'Corporate governance is the exercise of ethical and effective leadership by the individuals responsible for managing the business.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on ethical and effective leadership of a business.',
                'Ethical, effective leadership/direction = corporate governance.',
                'A code of conduct is a document of acceptable behaviour.',
            ),
            'guidelines': ['Ethical/effective leadership of a business = corporate governance.'],
        }, subskill='concepts', learning_objective_id=LO_KING, question_family_id='corporate_governance_definition', concept_id='corporate_governance', concept_group='king', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'King Code principle',
            'prompt': 'A business that openly shares accurate financial and operational information with stakeholders is applying which King Code principle?',
            'options': ['Accountability', 'Transparency', 'Responsibility', 'Profitability'],
            'correct_index': 1,
            'explanation': 'Transparency means the business openly and accurately discloses information to stakeholders.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on openly sharing information.',
                'Open, accurate disclosure to stakeholders = transparency.',
                'Accountability is taking responsibility for decisions/actions.',
            ),
            'guidelines': ['Open disclosure = transparency.'],
        }, subskill='concepts', learning_objective_id=LO_KING, question_family_id='king_principle_identify', concept_id='transparency', concept_group='king', misconception_tags=['confuses_transparency_with_accountability'], diagnostic_tags=['identification', 'king']),
        with_metadata({
            'title': 'Unethical practice',
            'prompt': 'A business that deliberately understates its income to pay less tax is engaging in …',
            'options': ['tax evasion', 'unfair advertising', 'sexual harassment', 'over-insurance'],
            'correct_index': 0,
            'explanation': 'Deliberately understating income to pay less tax is tax evasion, an unethical (and illegal) business practice.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on dishonest handling of tax.',
                'Understating income to avoid tax = tax evasion.',
                'Unfair advertising misleads customers, not the tax authority.',
            ),
            'guidelines': ['Understating income to dodge tax = tax evasion.'],
        }, subskill='concepts', learning_objective_id=LO_UNETHICAL, question_family_id='unethical_identify', concept_id='tax_evasion', concept_group='unethical', misconception_tags=['confuses_tax_evasion_with_unfair_advertising'], diagnostic_tags=['identification', 'unethical']),
        with_metadata({
            'title': 'Unprofessional practice',
            'prompt': 'An employee who uses company funds for personal expenses is committing which unprofessional practice?',
            'options': ['Abuse of work time', 'Unauthorised use of workplace funds and resources', 'Unfair advertising', 'Sexual harassment'],
            'correct_index': 1,
            'explanation': 'Using company funds for personal expenses is the unauthorised use of workplace funds and resources.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on misuse of the business\u2019s money/resources.',
                'Personal use of company funds = unauthorised use of funds/resources.',
                'Abuse of work time is wasting paid working hours.',
            ),
            'guidelines': ['Personal use of company funds = unauthorised use of funds/resources.'],
        }, subskill='concepts', learning_objective_id=LO_UNETHICAL, question_family_id='unprofessional_identify', concept_id='unauthorised_use_of_funds', concept_group='unethical', diagnostic_tags=['identification', 'unprofessional']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Apply King Code principles',
            'prompt': 'A company has been accused of hiding losses from its shareholders. Recommend how it can apply the King Code principles of transparency, accountability and responsibility to restore good corporate governance. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Transparency: openly and accurately disclose financial information to shareholders.',
                'Accountability: hold directors answerable for their decisions and report at the AGM.',
                'Responsibility: act responsibly towards stakeholders and correct the wrongdoing.',
                'Implement a code of conduct and independent auditing to rebuild trust.',
            ],
            'sample_answer': 'The company should apply transparency by openly and accurately disclosing its financial position to shareholders, accountability by holding directors answerable for their decisions and reporting fully at the AGM, and responsibility by acting in stakeholders\u2019 interests and correcting the wrongdoing. Implementing a code of conduct and independent audits would help rebuild trust.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Link each King principle to an action.',
                'Transparency = disclose; accountability = answerable; responsibility = act in stakeholders\u2019 interests.',
                'Tie the actions to restoring trust.',
            ),
            'answer_part_hints': ['Address each principle.', 'Give a concrete action for each.'],
            'guidelines': ['Cover transparency, accountability and responsibility.'],
            'teaching_note': 'Reward each principle linked to a concrete governance action.',
            'keywords': ['transparency', 'accountability', 'responsibility', 'disclose', 'AGM'],
        }, subskill='application', learning_objective_id=LO_KING, question_family_id='apply_king_scenario', concept_id='corporate_governance', concept_group='king', scenario_family_id='hidden_losses', diagnostic_tags=['scenario_analysis', 'king'], answer_structure_tags=['recommend', 'apply'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Deal with an unethical practice',
            'prompt': 'A retailer charges much higher prices for the same goods in remote rural areas. Identify the unethical practice and recommend how the business could deal with it. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The unethical practice is unfair pricing of goods in rural areas.',
                'Set fair, consistent prices regardless of location.',
                'Adopt and enforce a code of conduct on pricing.',
                'Be transparent with customers about pricing.',
            ],
            'sample_answer': 'The practice is the unfair pricing of goods in rural areas. The business should deal with it by setting fair and consistent prices regardless of location, adopting and enforcing a code of conduct on pricing, and being transparent with customers about how prices are set.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Name the practice, then give remedies.',
                'Overcharging rural customers = unfair pricing in rural areas.',
                'Remedies centre on fair, transparent pricing.',
            ),
            'answer_part_hints': ['Identify the practice.', 'Recommend how to deal with it.'],
            'guidelines': ['Identify the practice and give remedies.'],
            'teaching_note': 'Reward identifying rural pricing plus fair-pricing remedies.',
            'keywords': ['unfair pricing', 'rural', 'fair', 'code of conduct', 'transparent'],
        }, subskill='application', learning_objective_id=LO_UNETHICAL, question_family_id='deal_unethical_scenario', concept_id='pricing_in_rural_areas', concept_group='unethical', scenario_family_id='rural_pricing', diagnostic_tags=['scenario_analysis', 'unethical'], answer_structure_tags=['identify', 'recommend'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Ethical vs professional behaviour',
            'prompt': 'Distinguish between ethical behaviour and professional behaviour, giving an example of each. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Ethical behaviour is acting on values that are morally acceptable in society.',
                'Example of ethical behaviour: refusing to pay or accept bribes.',
                'Professional behaviour is meeting accepted standards of conduct and competence at work.',
                'Example of professional behaviour: dressing appropriately and meeting deadlines.',
                'Professionalism is broader and includes appearance, attitude and loyalty.',
            ],
            'sample_answer': 'Ethical behaviour is acting according to values that are morally acceptable in society, for example refusing to pay or accept bribes. Professional behaviour is meeting the accepted standards of conduct and competence in the workplace, for example dressing appropriately and meeting deadlines. Professionalism is the broader concept and also covers appearance, attitude and loyalty.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Contrast the two concepts.',
                'Ethics = morally right; professionalism = workplace standards.',
                'Add an example for each.',
            ),
            'answer_part_hints': ['Define each.', 'Give an example of each.'],
            'guidelines': ['Distinguish both and give examples.'],
            'teaching_note': 'Reward a clear distinction with examples.',
            'keywords': ['ethical', 'morally acceptable', 'professional', 'standards', 'example'],
        }, subskill='discussion', learning_objective_id=LO_CONCEPTS, question_family_id='ethics_vs_professionalism_discussion', concept_id='ethical_behaviour', concept_group='concepts', diagnostic_tags=['discussion', 'comparison'], answer_structure_tags=['distinguish', 'example'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Challenges of unethical practices',
            'prompt': 'Explain how unethical business practices such as unfair advertising and tax evasion pose challenges to businesses. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Unfair advertising can mislead customers and damage the business\u2019s reputation.',
                'It may lead to legal action, fines and loss of customer trust.',
                'Tax evasion is illegal and can result in penalties, fines or prosecution.',
                'It damages the business\u2019s relationship with SARS and its public image.',
                'Unethical practices reduce investor confidence and long-term sustainability.',
            ],
            'sample_answer': 'Unfair advertising misleads customers and damages the business\u2019s reputation, which can lead to legal action, fines and loss of trust. Tax evasion is illegal and can result in heavy penalties, fines or prosecution, damaging the business\u2019s relationship with SARS and its public image. Overall, unethical practices reduce investor confidence and threaten the long-term sustainability of the business.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain the consequences of each practice.',
                'Think reputation, legal penalties and lost trust.',
                'Link the practices to long-term sustainability.',
            ),
            'answer_part_hints': ['Address each practice.', 'Explain the challenges.'],
            'guidelines': ['Explain challenges for both practices.'],
            'teaching_note': 'Reward consequences linked to reputation, legality and trust.',
            'keywords': ['mislead', 'reputation', 'legal', 'penalties', 'trust', 'SARS'],
        }, subskill='discussion', learning_objective_id=LO_UNETHICAL, question_family_id='unethical_challenges_discussion', concept_id='tax_evasion', concept_group='unethical', diagnostic_tags=['discussion', 'evaluation'], answer_structure_tags=['explain', 'consequences'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
