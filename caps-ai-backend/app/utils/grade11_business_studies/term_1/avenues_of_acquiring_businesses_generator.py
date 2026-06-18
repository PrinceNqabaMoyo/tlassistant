"""Grade 11 Business Studies - Term 1 - Topic 7: Avenues of acquiring
businesses.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='avenues_of_acquiring_businesses',
    curriculum_reference='Term 1 > Avenues of acquiring businesses',
    id_prefix='g11_bs_avenues',
)

LO_BUY = 'lo_reasons_to_buy_existing_business'
LO_FRANCHISE = 'lo_franchising'
LO_OUTSOURCE = 'lo_outsourcing'
LO_LEASE = 'lo_leasing'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Franchising',
            'prompt': 'A concept where the owner licenses its business model, brand and know-how to another party who pays fees is called …',
            'options': ['outsourcing', 'leasing', 'franchising', 'hedging'],
            'correct_index': 2,
            'explanation': 'Franchising is where the franchisor licenses its business model, brand, know-how and rights to a franchisee in return for fees.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify licensing a whole business model.',
                'Franchising licenses brand and know-how for fees.',
                'The franchisee runs a proven model under the franchisor\'s brand.',
            ),
            'guidelines': ['Link licensing brand/model to franchising.'],
        }, subskill='concepts', learning_objective_id=LO_FRANCHISE, question_family_id='franchising_definition', concept_id='franchising', concept_group='avenues', misconception_tags=['confuses_franchising_with_outsourcing'], diagnostic_tags=['definition', 'avenues']),
        with_metadata({
            'title': 'Franchisee',
            'prompt': 'The party who pays a fee for the right to use the trademark and proprietary knowledge of a business is the …',
            'options': ['franchisor', 'franchisee', 'lessor', 'lessee'],
            'correct_index': 1,
            'explanation': 'The franchisee pays a fee to the franchisor for the right to use the trademark and proprietary knowledge.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify who pays and who owns.',
                'The franchisee pays; the franchisor owns the model.',
                'Compare with lessee (pays) vs lessor (owns) in leasing.',
            ),
            'guidelines': ['The party paying fees = franchisee.'],
        }, subskill='concepts', learning_objective_id=LO_FRANCHISE, question_family_id='franchisee_definition', concept_id='franchisee', concept_group='avenues', misconception_tags=['confuses_franchisee_with_franchisor'], diagnostic_tags=['definition', 'avenues']),
        with_metadata({
            'title': 'Outsourcing',
            'prompt': 'An agreement where one company hires another to supply services that could be done internally is called …',
            'options': ['franchising', 'outsourcing', 'leasing', 'a merger'],
            'correct_index': 1,
            'explanation': 'Outsourcing is an agreement where one company hires another company or person to supply services or goods that could be done internally.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify hiring out internal work.',
                'Outsourcing contracts work that could be done in-house to others.',
                'Examples: security, cleaning, payroll, IT services.',
            ),
            'guidelines': ['Link hiring out internal functions to outsourcing.'],
        }, subskill='concepts', learning_objective_id=LO_OUTSOURCE, question_family_id='outsourcing_definition', concept_id='outsourcing', concept_group='avenues', misconception_tags=['confuses_outsourcing_with_franchising'], diagnostic_tags=['definition', 'avenues']),
        with_metadata({
            'title': 'Leasing',
            'prompt': 'A contract outlining terms under which one party rents goods or services owned by another party is called …',
            'options': ['leasing', 'franchising', 'outsourcing', 'a takeover'],
            'correct_index': 0,
            'explanation': 'Leasing is a contract outlining the terms under which one party agrees to rent goods or services owned by another party.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify renting an asset.',
                'Leasing = renting goods owned by another party.',
                'Lessor owns the asset; lessee rents and uses it.',
            ),
            'guidelines': ['Link renting an asset to leasing.'],
        }, subskill='concepts', learning_objective_id=LO_LEASE, question_family_id='leasing_definition', concept_id='leasing', concept_group='avenues', misconception_tags=['confuses_leasing_with_buying'], diagnostic_tags=['definition', 'avenues']),
        with_metadata({
            'title': 'Lessor vs lessee',
            'prompt': 'In a lease agreement, the owner of the asset who grants the lease is the …',
            'options': ['lessee', 'lessor', 'franchisee', 'tenant'],
            'correct_index': 1,
            'explanation': 'The lessor is the owner of the asset who grants a lease to the lessee (the tenant who rents it).',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the owner of the leased asset.',
                'Lessor = owner who grants the lease.',
                'Lessee = tenant who rents and uses the asset.',
            ),
            'guidelines': ['Owner who grants the lease = lessor.'],
        }, subskill='concepts', learning_objective_id=LO_LEASE, question_family_id='lessor_lessee_definition', concept_id='lessor', concept_group='avenues', misconception_tags=['confuses_lessor_with_lessee'], diagnostic_tags=['definition', 'avenues']),
        with_metadata({
            'title': 'Reason to buy an existing business',
            'prompt': 'Which of the following is a reason an entrepreneur may decide to buy an existing business?',
            'options': [
                'It has no existing customers',
                'It already has an established customer base and income',
                'It guarantees there will be no competitors',
                'It removes the need for any contracts',
            ],
            'correct_index': 1,
            'explanation': 'An existing business already has an established customer base, staff, suppliers and income, reducing start-up risk.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Think about what is already in place.',
                'An existing business comes with customers, staff and income.',
                'This reduces the risk of starting from scratch.',
            ),
            'guidelines': ['Look for an established base that lowers risk.'],
        }, subskill='concepts', learning_objective_id=LO_BUY, question_family_id='reason_to_buy_existing', concept_id='buy_existing_business', concept_group='avenues', misconception_tags=['confuses_buying_with_starting'], diagnostic_tags=['reasoning', 'avenues']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Identify the avenue',
            'prompt': 'Mazella Properties owns properties; businesses pay them monthly to use a property for a specified period. Identify the business avenue and motivate by quoting from the scenario. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The avenue is leasing/renting.',
                'Motivation: businesses "pay them every month for the use of a property".',
                'It is for "a specified period of time".',
                'Mazella (lessor) owns the asset; the businesses (lessees) rent it.',
            ],
            'sample_answer': 'The avenue is leasing, because businesses "pay them every month for the use of a property" "for a specified period of time". Mazella Properties is the lessor that owns the property, and the businesses are the lessees that rent it.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the scenario to an avenue.',
                'Paying monthly to use an owned asset = leasing.',
                'Quote the scenario for the motivation.',
            ),
            'answer_part_hints': ['Name the avenue.', 'Quote scenario evidence.'],
            'guidelines': ['Must quote from the scenario.'],
            'teaching_note': 'Reward correct avenue plus a direct quote.',
            'keywords': ['leasing', 'rent', 'monthly', 'property', 'specified period', 'lessor'],
        }, subskill='application', learning_objective_id=LO_LEASE, question_family_id='identify_avenue_scenario', concept_id='leasing', concept_group='avenues', scenario_family_id='mazella_properties', diagnostic_tags=['scenario_analysis', 'avenues'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Recommend an avenue',
            'prompt': 'An entrepreneur wants to run a fast-food outlet using a well-known brand and proven systems, with support and training. Recommend the BEST avenue and give TWO reasons. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend franchising.',
                'Reason: uses an established brand/trademark that attracts customers.',
                'Reason: proven business model, systems and training/support.',
                'Reason: lower risk than starting a new brand from scratch.',
            ],
            'sample_answer': 'They should buy a franchise. Franchising lets them trade under a well-known brand that already attracts customers, and they receive a proven business model with training and support, which lowers the risk compared with starting a new brand from scratch.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the needs to the avenue.',
                'Wanting a known brand + proven systems = franchising.',
                'Give reasons tied to brand, support and lower risk.',
            ),
            'answer_part_hints': ['Name the avenue.', 'Give two reasons.'],
            'guidelines': ['Link reasons to the entrepreneur\'s needs.'],
            'teaching_note': 'Reward franchising with brand/support/risk reasons.',
            'keywords': ['franchising', 'brand', 'trademark', 'proven model', 'training', 'support'],
        }, subskill='application', learning_objective_id=LO_FRANCHISE, question_family_id='recommend_avenue_scenario', concept_id='franchising', concept_group='avenues', scenario_family_id='fast_food_franchise', diagnostic_tags=['recommendation', 'avenues'], answer_structure_tags=['recommend', 'justify'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Advantages and disadvantages of franchising',
            'prompt': 'Discuss the advantages and disadvantages of franchising as an avenue of acquiring a business. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Advantage: established brand/trademark attracts customers.',
                'Advantage: proven business model with training and ongoing support.',
                'Advantage: easier access to finance due to lower risk.',
                'Disadvantage: ongoing franchise fees/royalties reduce profit.',
                'Disadvantage: limited independence - must follow franchisor rules.',
            ],
            'sample_answer': 'Franchising offers an established brand and trademark that attracts customers, a proven business model with training and support, and easier access to finance because of the lower risk. However, the franchisee must pay ongoing fees and royalties that reduce profit, and has limited independence because they must comply with the franchisor\'s rules and procedures.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Balance pros and cons of franchising.',
                'Advantages: brand, proven model, support, finance.',
                'Disadvantages: fees/royalties and limited independence.',
            ),
            'answer_part_hints': ['Give advantages.', 'Give disadvantages.'],
            'guidelines': ['Provide both advantages and disadvantages.'],
            'teaching_note': 'Reward balanced coverage of advantages and disadvantages.',
            'keywords': ['franchising', 'brand', 'proven model', 'support', 'fees', 'royalties', 'independence'],
        }, subskill='discussion', learning_objective_id=LO_FRANCHISE, question_family_id='franchising_pros_cons_discussion', concept_id='franchising', concept_group='avenues', diagnostic_tags=['discussion', 'avenues'], answer_structure_tags=['list', 'evaluate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Disadvantages of outsourcing',
            'prompt': 'Discuss the disadvantages of outsourcing as a business avenue. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Loss of control over the quality of outsourced work.',
                'Confidential information may be exposed to outsiders.',
                'Dependence on the service provider; risk if they underperform.',
                'Possible job losses internally and hidden/ongoing costs.',
            ],
            'sample_answer': 'Outsourcing can mean a loss of control over the quality of the work, exposure of confidential information to outside parties, and dependence on the service provider, which is risky if they underperform. It may also cause internal job losses and bring hidden or ongoing costs.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List the downsides of contracting work out.',
                'Think control, confidentiality and dependence.',
                'Consider job losses and hidden costs too.',
            ),
            'answer_part_hints': ['Give several disadvantages.', 'Explain each.'],
            'guidelines': ['Provide at least three disadvantages.'],
            'teaching_note': 'Reward distinct disadvantages of outsourcing.',
            'keywords': ['outsourcing', 'control', 'quality', 'confidential', 'dependence', 'jobs'],
        }, subskill='discussion', learning_objective_id=LO_OUTSOURCE, question_family_id='outsourcing_disadvantages_discussion', concept_id='outsourcing', concept_group='avenues', diagnostic_tags=['discussion', 'avenues'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Reasons to purchase an existing business',
            'prompt': 'Explain reasons why entrepreneurs may decide to purchase an existing business. (6 marks)',
            'marks': 6,
            'marking_points': [
                'It already has an established customer base and income.',
                'Existing staff, suppliers and systems are in place.',
                'Lower risk than starting from scratch; track record is visible.',
                'Easier to obtain finance because the business has a trading history.',
            ],
            'sample_answer': 'Entrepreneurs may buy an existing business because it already has an established customer base and income, existing staff, suppliers and systems, and a visible track record that lowers risk. Its trading history also makes it easier to obtain finance than for a brand-new start-up.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List reasons for buying rather than starting.',
                'Existing customers, staff and income reduce risk.',
                'A track record helps with finance.',
            ),
            'answer_part_hints': ['Give several reasons.', 'Explain each.'],
            'guidelines': ['Provide at least three reasons.'],
            'teaching_note': 'Reward distinct reasons linked to lower risk.',
            'keywords': ['existing business', 'customer base', 'income', 'staff', 'lower risk', 'finance'],
        }, subskill='discussion', learning_objective_id=LO_BUY, question_family_id='reasons_to_buy_discussion', concept_id='buy_existing_business', concept_group='avenues', diagnostic_tags=['discussion', 'avenues'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
