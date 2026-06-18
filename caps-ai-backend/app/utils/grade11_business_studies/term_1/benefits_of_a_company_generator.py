"""Grade 11 Business Studies - Term 1 - Topic 6: Benefits of a company over
other forms of ownership.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='benefits_of_a_company',
    curriculum_reference='Term 1 > Benefits of a company over other forms of ownership',
    id_prefix='g11_bs_company',
)

LO_FORMS = 'lo_forms_of_ownership'
LO_BENEFITS = 'lo_benefits_of_a_company'
LO_FORMATION = 'lo_company_formation_documents'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Limited liability',
            'prompt': 'A legal structure where the owner\'s loss will not exceed the amount they invested is called …',
            'options': ['unlimited liability', 'limited liability', 'continuity', 'securities'],
            'correct_index': 1,
            'explanation': 'Limited liability means the loss of the business will not exceed the amount invested by the owner.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on how far losses can go.',
                'Limited liability caps the owner\'s loss at their investment.',
                'Companies offer limited liability; sole traders have unlimited liability.',
            ),
            'guidelines': ['Link "loss capped at investment" to limited liability.'],
        }, subskill='concepts', learning_objective_id=LO_BENEFITS, question_family_id='limited_liability_definition', concept_id='limited_liability', concept_group='benefits', misconception_tags=['confuses_limited_with_unlimited'], diagnostic_tags=['definition', 'liability']),
        with_metadata({
            'title': 'Continuity',
            'prompt': 'A company continues to exist even if a shareholder retires or dies. This benefit is called …',
            'options': ['continuity', 'liability', 'taxation', 'securities'],
            'correct_index': 0,
            'explanation': 'Continuity means the company continues to exist even if a change of ownership takes place (e.g. a shareholder retires).',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on the lifespan of the business.',
                'A company has continuity independent of its owners.',
                'A sole trader usually ends when the owner dies/leaves.',
            ),
            'guidelines': ['Link "continues to exist" to continuity.'],
        }, subskill='concepts', learning_objective_id=LO_BENEFITS, question_family_id='continuity_definition', concept_id='continuity', concept_group='benefits', misconception_tags=['confuses_continuity_with_liability'], diagnostic_tags=['definition', 'continuity']),
        with_metadata({
            'title': 'Memorandum of Incorporation',
            'prompt': 'The document that sets out the rights, responsibilities and duties of shareholders and directors (the company\'s constitution) is the …',
            'options': ['prospectus', 'notice of incorporation', 'Memorandum of Incorporation (MOI)', 'audit report'],
            'correct_index': 2,
            'explanation': 'The MOI sets out the rights, responsibilities and duties of shareholders and directors and serves as the company\'s constitution.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the company\'s constitution.',
                'The MOI governs shareholders\' and directors\' rights and duties.',
                'A prospectus invites the public to buy shares; the MOI is internal rules.',
            ),
            'guidelines': ['Link "constitution of the company" to MOI.'],
        }, subskill='concepts', learning_objective_id=LO_FORMATION, question_family_id='moi_definition', concept_id='moi', concept_group='formation_documents', misconception_tags=['confuses_moi_with_prospectus'], diagnostic_tags=['definition', 'formation']),
        with_metadata({
            'title': 'Prospectus',
            'prompt': 'A document inviting the public to buy securities or shares is a …',
            'options': ['Memorandum of Incorporation', 'prospectus', 'notice of incorporation', 'lease'],
            'correct_index': 1,
            'explanation': 'A prospectus is a document inviting the public to buy securities or shares.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the document aimed at the public.',
                'A prospectus invites the public to buy shares.',
                'Only public companies may issue a prospectus.',
            ),
            'guidelines': ['Link "invite the public to buy shares" to prospectus.'],
        }, subskill='concepts', learning_objective_id=LO_FORMATION, question_family_id='prospectus_definition', concept_id='prospectus', concept_group='formation_documents', misconception_tags=['confuses_prospectus_with_moi'], diagnostic_tags=['definition', 'formation']),
        with_metadata({
            'title': 'Company as a legal person',
            'prompt': 'A key benefit of a company is that it has legal status, meaning it …',
            'options': [
                'is the same legal person as its owners',
                'is a separate legal person that can act on its own',
                'cannot own assets or sign contracts',
                'must be owned by only one person',
            ],
            'correct_index': 1,
            'explanation': 'A company is a separate legal person with the capacity and powers to act on its own (own assets, sign contracts, sue and be sued).',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on the legal status of a company.',
                'A company is separate from its owners in law.',
                'This separation gives owners limited liability.',
            ),
            'guidelines': ['Link "separate legal person" to a company\'s legal status.'],
        }, subskill='concepts', learning_objective_id=LO_BENEFITS, question_family_id='legal_status_definition', concept_id='legal_status', concept_group='benefits', misconception_tags=['confuses_company_with_owner'], diagnostic_tags=['definition', 'legal_status']),
        with_metadata({
            'title': 'Sole trader liability',
            'prompt': 'Compared with a company, a sole trader carries … for the debts of the business.',
            'options': ['limited liability', 'unlimited liability', 'no liability', 'shared liability with the state'],
            'correct_index': 1,
            'explanation': 'A sole trader has unlimited liability - full legal responsibility for all business debts, unlike a company\'s limited liability.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Compare liability across forms of ownership.',
                'Sole traders have unlimited liability; companies limited.',
                'Unlimited liability puts personal assets at risk.',
            ),
            'guidelines': ['Contrast sole trader vs company liability.'],
        }, subskill='concepts', learning_objective_id=LO_FORMS, question_family_id='sole_trader_liability', concept_id='unlimited_liability', concept_group='forms_of_ownership', misconception_tags=['confuses_sole_trader_with_company'], diagnostic_tags=['comparison', 'liability']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Recommend a form of ownership',
            'prompt': 'Two partners want to grow their business, raise large capital and protect their personal assets from business debts. Recommend a suitable form of ownership and give TWO reasons. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend forming a (private) company.',
                'Reason: limited liability protects personal assets.',
                'Reason: a company can raise more capital (shares/securities).',
                'Reason: continuity - the business survives ownership changes.',
            ],
            'sample_answer': 'They should form a private company. A company offers limited liability, so their personal assets are protected from business debts, and it can raise more capital by issuing shares while also enjoying continuity if ownership changes.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match their needs to a form of ownership.',
                'Protecting personal assets points to limited liability (a company).',
                'Companies raise more capital and have continuity.',
            ),
            'answer_part_hints': ['Name the form.', 'Give two reasons.'],
            'guidelines': ['Link each reason to the partners\' needs.'],
            'teaching_note': 'Reward a company recommendation with benefit-based reasons.',
            'keywords': ['company', 'limited liability', 'capital', 'shares', 'continuity', 'personal assets'],
        }, subskill='application', learning_objective_id=LO_BENEFITS, question_family_id='recommend_form_scenario', concept_id='limited_liability', concept_group='benefits', scenario_family_id='partners_grow_business', diagnostic_tags=['recommendation', 'forms_of_ownership'], answer_structure_tags=['recommend', 'justify'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Benefit vs challenge',
            'prompt': 'A sole trader is considering registering a company. Explain ONE benefit and ONE challenge of doing so. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Benefit: limited liability / continuity / easier to raise capital.',
                'Challenge: more legal requirements and paperwork (MOI, registration).',
                'Challenge: higher costs and stricter regulation (audits, tax).',
                'Answer balances one clear benefit and one clear challenge.',
            ],
            'sample_answer': 'A benefit of registering a company is limited liability, which protects the owner\'s personal assets. A challenge is the increased legal requirements and costs, such as preparing an MOI, registering the company and complying with audits and stricter regulation.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Give one upside and one downside.',
                'Benefits: liability, capital, continuity.',
                'Challenges: legal requirements, costs, regulation.',
            ),
            'answer_part_hints': ['Give one benefit.', 'Give one challenge.'],
            'guidelines': ['Balance benefit and challenge.'],
            'teaching_note': 'Reward a clear benefit AND a clear challenge.',
            'keywords': ['company', 'limited liability', 'legal requirements', 'costs', 'regulation', 'MOI'],
        }, subskill='application', learning_objective_id=LO_FORMS, question_family_id='benefit_vs_challenge_scenario', concept_id='legal_status', concept_group='benefits', scenario_family_id='sole_trader_to_company', diagnostic_tags=['scenario_analysis', 'forms_of_ownership'], answer_structure_tags=['explain', 'evaluate'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Benefits of a company',
            'prompt': 'Discuss the benefits of establishing a company versus other forms of ownership. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Legal status and liability: separate legal person with limited liability.',
                'Capital and cash flow: can raise large capital through shares.',
                'Life span and continuity: continues despite ownership changes.',
                'Ownership and management: separation of ownership (shareholders) and management (directors).',
                'Profit-sharing and taxation considerations.',
            ],
            'sample_answer': 'A company has separate legal status and limited liability, protecting owners\' personal assets. It can raise large amounts of capital by issuing shares, has continuity (it survives ownership changes), and separates ownership (shareholders) from management (directors). These benefits make it stronger than a sole trader or partnership for growth, despite differences in profit-sharing and taxation.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Cover several benefit categories.',
                'Use the curriculum list: liability, capital, continuity, ownership/management, taxation.',
                'Contrast with sole trader/partnership where relevant.',
            ),
            'answer_part_hints': ['Name each benefit.', 'Explain why it is an advantage.'],
            'guidelines': ['Provide at least four distinct benefits with explanation.'],
            'teaching_note': 'Reward breadth across the curriculum benefit list.',
            'keywords': ['legal status', 'limited liability', 'capital', 'continuity', 'ownership', 'management'],
        }, subskill='discussion', learning_objective_id=LO_BENEFITS, question_family_id='benefits_of_company_discussion', concept_id='benefits', concept_group='benefits', diagnostic_tags=['discussion', 'forms_of_ownership'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Company formation documents',
            'prompt': 'Explain the purpose of the Memorandum of Incorporation, the notice of incorporation and the prospectus. (6 marks)',
            'marks': 6,
            'marking_points': [
                'MOI: sets out rights/responsibilities/duties of shareholders and directors (the constitution).',
                'Notice of incorporation: notifies the CIPC that a company is being registered/incorporated.',
                'Prospectus: invites the public to buy securities/shares (initial and secondary offer).',
                'Each document is explained distinctly.',
            ],
            'sample_answer': 'The Memorandum of Incorporation (MOI) is the company\'s constitution, setting out the rights, responsibilities and duties of shareholders and directors. The notice of incorporation notifies the authorities (CIPC) that a company is being incorporated. The prospectus is a document that invites the public to buy securities or shares, covering the initial and secondary offer.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain each document\'s purpose.',
                'MOI = constitution; notice = registration; prospectus = invite public.',
                'Keep the three documents distinct.',
            ),
            'answer_part_hints': ['Explain the MOI.', 'Explain the notice and prospectus.'],
            'guidelines': ['Distinct purpose for each document.'],
            'teaching_note': 'Reward distinct, accurate purposes for all three documents.',
            'keywords': ['MOI', 'constitution', 'notice of incorporation', 'prospectus', 'shares', 'public'],
        }, subskill='discussion', learning_objective_id=LO_FORMATION, question_family_id='formation_documents_discussion', concept_id='formation_documents', concept_group='formation_documents', diagnostic_tags=['discussion', 'formation'], answer_structure_tags=['explain', 'distinguish'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
