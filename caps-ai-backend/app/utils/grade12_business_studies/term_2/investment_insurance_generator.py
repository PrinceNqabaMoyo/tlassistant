"""Grade 12 Business Studies - Term 2 - Investment: Insurance.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='investment_insurance',
    curriculum_reference='Term 2 > Investment: Insurance',
    id_prefix='g12_bs_insurance',
)

LO_CONCEPTS = 'lo_insurance_concepts'
LO_PRINCIPLES = 'lo_insurance_principles'
LO_COMPULSORY = 'lo_compulsory_insurance'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Insurance vs assurance',
            'prompt': 'Cover taken out against an event that will definitely happen, such as death, is …',
            'options': ['insurance', 'assurance', 'indemnity', 'an excess'],
            'correct_index': 1,
            'explanation': 'Assurance covers an event that will definitely happen (e.g. death), while insurance covers an event that may or may not happen.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on a certain vs uncertain event.',
                'Certain event (death) = assurance.',
                'Uncertain event (fire/theft) = insurance.',
            ),
            'guidelines': ['Certain event = assurance.'],
        }, subskill='concepts', learning_objective_id=LO_CONCEPTS, question_family_id='insurance_assurance_identify', concept_id='assurance', concept_group='concepts', misconception_tags=['confuses_insurance_with_assurance'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Under-insurance',
            'prompt': 'When goods are insured for less than their actual value, this is …',
            'options': ['over-insurance', 'under-insurance', 'reinstatement', 'an excess'],
            'correct_index': 1,
            'explanation': 'Under-insurance occurs when an asset is insured for less than its actual value, so the average clause reduces the payout.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on insuring for too little.',
                'Insured for less than value = under-insurance.',
                'Insured for more than value = over-insurance.',
            ),
            'guidelines': ['Insured for less than value = under-insurance.'],
        }, subskill='concepts', learning_objective_id=LO_CONCEPTS, question_family_id='under_insurance_identify', concept_id='under_insurance', concept_group='concepts', misconception_tags=['confuses_under_with_over_insurance'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Principle of indemnity',
            'prompt': 'The principle that an insured person should be restored to the same financial position as before the loss (not profit from it) is …',
            'options': ['utmost good faith', 'indemnification/indemnity', 'insurable interest', 'security'],
            'correct_index': 1,
            'explanation': 'Indemnity restores the insured to the financial position they were in before the loss, so they do not profit from a claim.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on restoring, not profiting.',
                'Restore to pre-loss position = indemnity.',
                'Utmost good faith is about honest disclosure.',
            ),
            'guidelines': ['Restore to pre-loss position = indemnity.'],
        }, subskill='concepts', learning_objective_id=LO_PRINCIPLES, question_family_id='indemnity_identify', concept_id='indemnity', concept_group='principles', misconception_tags=['confuses_indemnity_with_insurable_interest'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Utmost good faith',
            'prompt': 'The principle that both parties must disclose all relevant information honestly when taking out insurance is …',
            'options': ['indemnity', 'utmost good faith', 'insurable interest', 'security'],
            'correct_index': 1,
            'explanation': 'Utmost good faith requires both the insurer and the insured to honestly disclose all relevant information.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on honest disclosure.',
                'Honest disclosure of all facts = utmost good faith.',
                'Indemnity is about restoring the loss.',
            ),
            'guidelines': ['Honest disclosure = utmost good faith.'],
        }, subskill='concepts', learning_objective_id=LO_PRINCIPLES, question_family_id='good_faith_identify', concept_id='utmost_good_faith', concept_group='principles', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Compulsory insurance',
            'prompt': 'Which of the following is an example of compulsory insurance?',
            'options': ['Fire insurance', 'Unemployment Insurance Fund (UIF)', 'Theft insurance', 'Life assurance'],
            'correct_index': 1,
            'explanation': 'The UIF is compulsory insurance required by law, along with examples such as the Road Accident Fund and COIDA.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on insurance required by law.',
                'UIF is required by law = compulsory insurance.',
                'Fire/theft insurance is non-compulsory.',
            ),
            'guidelines': ['UIF = compulsory insurance.'],
        }, subskill='concepts', learning_objective_id=LO_COMPULSORY, question_family_id='compulsory_identify', concept_id='uif', concept_group='compulsory', misconception_tags=['confuses_compulsory_with_non_compulsory'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Insurable interest',
            'prompt': 'The requirement that the insured must suffer a financial loss if the insured item is damaged is the principle of …',
            'options': ['insurable interest', 'indemnity', 'reinstatement', 'excess'],
            'correct_index': 0,
            'explanation': 'Insurable interest means the insured must stand to suffer a financial loss if the insured item is damaged or lost.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on standing to lose financially.',
                'Must suffer a financial loss = insurable interest.',
                'Indemnity restores you after the loss.',
            ),
            'guidelines': ['Must stand to lose financially = insurable interest.'],
        }, subskill='concepts', learning_objective_id=LO_PRINCIPLES, question_family_id='insurable_interest_identify', concept_id='insurable_interest', concept_group='principles', diagnostic_tags=['identification']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Apply the average clause',
            'prompt': 'A business insures stock for R80 000 but the actual value is R100 000. A fire causes R40 000 damage. Using the average clause, calculate the compensation. Show your working. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Average clause: (insured value / actual value) x loss.',
                '(80 000 / 100 000) x 40 000.',
                '= 0.8 x 40 000.',
                'Compensation = R32 000.',
            ],
            'sample_answer': 'Compensation = (insured value / actual value) x loss = (80 000 / 100 000) x 40 000 = 0.8 x 40 000 = R32 000.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Use the average clause formula.',
                'Compensation = (insured/actual) x loss.',
                'Multiply the ratio by the loss.',
            ),
            'answer_part_hints': ['Set up the formula.', 'Calculate the compensation.'],
            'guidelines': ['Show working and final compensation.'],
            'teaching_note': 'Reward correct formula and R32 000.',
            'keywords': ['average clause', 'insured value', 'actual value', '0.8', '32000'],
        }, subskill='application', learning_objective_id=LO_CONCEPTS, question_family_id='average_clause_calc', concept_id='average_clause', concept_group='concepts', scenario_family_id='stock_fire', diagnostic_tags=['calculation'], answer_structure_tags=['calculate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Identify a principle',
            'prompt': 'An insured business failed to disclose that its premises had flooded before. The insurer rejects the claim. Identify the principle breached and explain. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The principle breached is utmost good faith.',
                'Both parties must disclose all relevant information honestly.',
                'The business hid material information (the previous flooding).',
                'This entitles the insurer to reject the claim.',
            ],
            'sample_answer': 'The principle breached is utmost good faith, which requires both parties to disclose all relevant information honestly. Because the business hid material information about the previous flooding, the insurer is entitled to reject the claim.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match non-disclosure to a principle.',
                'Hiding material facts breaches utmost good faith.',
                'Explain the consequence for the claim.',
            ),
            'answer_part_hints': ['Name the principle.', 'Explain the breach.'],
            'guidelines': ['Identify utmost good faith and explain.'],
            'teaching_note': 'Reward utmost good faith with an explanation.',
            'keywords': ['utmost good faith', 'disclose', 'material information', 'reject', 'claim'],
        }, subskill='application', learning_objective_id=LO_PRINCIPLES, question_family_id='identify_principle_scenario', concept_id='utmost_good_faith', concept_group='principles', scenario_family_id='non_disclosure', diagnostic_tags=['scenario_analysis', 'principles'], answer_structure_tags=['identify', 'explain'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Importance of insurance',
            'prompt': 'Discuss the advantages/importance of insurance for businesses. (8 marks)',
            'marks': 8,
            'marking_points': [
                'It protects the business against financial losses from insured risks.',
                'It provides peace of mind and business continuity after a loss.',
                'It allows the business to recover and continue operating.',
                'It protects assets such as stock, vehicles and premises.',
                'Some insurance (e.g. UIF, COIDA) is required by law.',
            ],
            'sample_answer': 'Insurance protects a business against financial losses from insured risks, providing peace of mind and helping it continue operating after a loss. It protects assets such as stock, vehicles and premises, allows recovery after an event, and some forms (such as UIF and COIDA) are required by law.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List the benefits of insurance.',
                'Protection, continuity, asset cover, legal requirement.',
                'Explain each briefly.',
            ),
            'answer_part_hints': ['List advantages.', 'Explain each.'],
            'guidelines': ['Provide several advantages.'],
            'teaching_note': 'Reward a range of insurance advantages.',
            'keywords': ['protect', 'losses', 'continuity', 'assets', 'legal'],
        }, subskill='discussion', learning_objective_id=LO_COMPULSORY, question_family_id='insurance_importance_discussion', concept_id='insurance', concept_group='concepts', diagnostic_tags=['discussion'], answer_structure_tags=['list', 'advantages'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Compulsory vs non-compulsory insurance',
            'prompt': 'Distinguish between compulsory and non-compulsory insurance and give an example of each. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Compulsory insurance is required by law.',
                'Example of compulsory: UIF, RAF or COIDA.',
                'Non-compulsory insurance is taken out voluntarily.',
                'Example of non-compulsory: fire, theft or vehicle insurance.',
                'Non-compulsory cover is based on the business\u2019s own risk assessment.',
            ],
            'sample_answer': 'Compulsory insurance is required by law, such as the UIF, RAF or COIDA. Non-compulsory insurance is taken out voluntarily based on the business\u2019s own risk assessment, such as fire, theft or vehicle insurance. The key difference is that one is a legal requirement while the other is a personal/business choice.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Contrast required vs voluntary insurance.',
                'Compulsory = by law; non-compulsory = voluntary.',
                'Give an example of each.',
            ),
            'answer_part_hints': ['Define each.', 'Give an example of each.'],
            'guidelines': ['Distinguish both with examples.'],
            'teaching_note': 'Reward the distinction with correct examples.',
            'keywords': ['compulsory', 'law', 'UIF', 'non-compulsory', 'voluntary', 'fire'],
        }, subskill='discussion', learning_objective_id=LO_COMPULSORY, question_family_id='compulsory_compare_discussion', concept_id='uif', concept_group='compulsory', diagnostic_tags=['discussion', 'comparison'], answer_structure_tags=['distinguish', 'example'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
