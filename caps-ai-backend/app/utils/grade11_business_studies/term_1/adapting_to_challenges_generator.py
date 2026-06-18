"""Grade 11 Business Studies - Term 1 - Topic 3: Adapting to the challenges in
the business environments.

Deterministic generator (seeded RNG + curated CAPS content banks). Subskills:
concepts (mcq), application (typed), discussion (typed), mixed.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import (
    TopicMeta,
    hint_sections,
    make_generate,
    with_metadata,
)

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='adapting_to_challenges',
    curriculum_reference='Term 1 > Adapting to the challenges in the business environments',
    id_prefix='g11_bs_adapt',
)

LO_ADAPT = 'lo_ways_to_adapt_to_challenges'
LO_INFLUENCE = 'lo_direct_influence_and_social_responsibility'
LO_LNP = 'lo_lobbying_networking_power_relations'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Merger',
            'prompt': 'When two or more businesses join their resources together to form one new business, this is a …',
            'options': ['takeover', 'merger', 'acquisition', 'alliance'],
            'correct_index': 1,
            'explanation': 'A merger occurs when two or more businesses join (usually by agreement) to form one new business.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Distinguish how businesses combine.',
                'A merger creates ONE new business from the joined resources.',
                'Mergers are by agreement; takeovers can be against the other business\'s will.',
            ),
            'guidelines': ['Look for the option where a new combined business is formed.'],
        }, subskill='concepts', learning_objective_id=LO_ADAPT, question_family_id='merger_definition', concept_id='merger', concept_group='mergers_takeovers_acquisitions_alliances', misconception_tags=['confuses_merger_with_takeover'], diagnostic_tags=['definition', 'restructuring']),
        with_metadata({
            'title': 'Takeover',
            'prompt': 'Buying the majority of another company\'s shares to gain control of it is a …',
            'options': ['merger', 'alliance', 'takeover', 'network'],
            'correct_index': 2,
            'explanation': 'A takeover happens when a company takes control/ownership of another by buying the majority of its shares.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify gaining control through shares.',
                'Control comes from owning the majority of shares.',
                'A takeover can happen against the other business\'s will.',
            ),
            'guidelines': ['Link controlling interest to majority shareholding.'],
        }, subskill='concepts', learning_objective_id=LO_ADAPT, question_family_id='takeover_definition', concept_id='takeover', concept_group='mergers_takeovers_acquisitions_alliances', misconception_tags=['confuses_takeover_with_acquisition'], diagnostic_tags=['definition', 'restructuring']),
        with_metadata({
            'title': 'Acquisition',
            'prompt': 'A business buys another business at an agreed price, and the bought business continues as a subsidiary. This is a(n) …',
            'options': ['acquisition', 'merger', 'strike', 'lobby'],
            'correct_index': 0,
            'explanation': 'In an acquisition a business buys another at an agreed price; the acquired business often continues to operate as a subsidiary.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Spot the agreed purchase of a whole business.',
                'The acquired business keeps operating, usually as a subsidiary.',
                'Acquisitions usually involve companies not listed on the JSE.',
            ),
            'guidelines': ['Look for "agreed price" and "subsidiary".'],
        }, subskill='concepts', learning_objective_id=LO_ADAPT, question_family_id='acquisition_definition', concept_id='acquisition', concept_group='mergers_takeovers_acquisitions_alliances', misconception_tags=['confuses_acquisition_with_merger'], diagnostic_tags=['definition', 'restructuring']),
        with_metadata({
            'title': 'Alliance',
            'prompt': 'Two businesses with common goals agree to co-operate while remaining separate. This is a(n) …',
            'options': ['merger', 'takeover', 'alliance', 'acquisition'],
            'correct_index': 2,
            'explanation': 'In an alliance, businesses with common visions work together for mutual benefit but remain separate.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Note that the businesses stay separate.',
                'They merely co-operate; no new combined business is formed.',
                'Alliances make businesses more competitive and better able to respond to challenges.',
            ),
            'guidelines': ['Look for co-operation while remaining separate entities.'],
        }, subskill='concepts', learning_objective_id=LO_ADAPT, question_family_id='alliance_definition', concept_id='alliance', concept_group='mergers_takeovers_acquisitions_alliances', misconception_tags=['confuses_alliance_with_merger'], diagnostic_tags=['definition', 'restructuring']),
        with_metadata({
            'title': 'Information management',
            'prompt': 'The collection, storage and distribution of information so it is easily retrieved and used is called …',
            'options': ['strategic management', 'information management', 'networking', 'lobbying'],
            'correct_index': 1,
            'explanation': 'Information management is the collection, storage and distribution of information so staff can retrieve and use it effectively.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the definition to the correct adaptation strategy.',
                'It is about how information is recorded, stored, retrieved and used.',
                'Investing in IT systems supports good information management.',
            ),
            'guidelines': ['Focus on handling of information, not goals or contacts.'],
        }, subskill='concepts', learning_objective_id=LO_ADAPT, question_family_id='information_management_definition', concept_id='information_management', concept_group='ways_to_adapt', misconception_tags=['confuses_information_with_strategic_management'], diagnostic_tags=['definition', 'adaptation']),
        with_metadata({
            'title': 'Hedging against inflation',
            'prompt': 'Investing surplus funds in assets such as gold or property so their value grows faster than inflation is called …',
            'options': ['lobbying', 'hedging', 'networking', 'bargaining'],
            'correct_index': 1,
            'explanation': 'Hedging means investing money so its value overcomes inflation, e.g. in gold, property or precious metals.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify protecting money from inflation.',
                'Hedging spreads risk by investing in assets with intrinsic value.',
                'Examples: gold, oil, property, bonds and shares.',
            ),
            'guidelines': ['Link the term to beating inflation through investment.'],
        }, subskill='concepts', learning_objective_id=LO_LNP, question_family_id='hedging_definition', concept_id='hedging', concept_group='types_of_lobbying', misconception_tags=['confuses_hedging_with_saving'], diagnostic_tags=['definition', 'lobbying']),
        with_metadata({
            'title': 'Lobbying',
            'prompt': 'An organised process where businesses use their influence to change government policy is called …',
            'options': ['networking', 'lobbying', 'hedging', 'merging'],
            'correct_index': 1,
            'explanation': 'Lobbying is an organised process where individuals/businesses use their influence to change government policy.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify influencing government policy.',
                'Lobbying is done by people with similar motives or commercial positions.',
                'It advances a cause and builds public trust.',
            ),
            'guidelines': ['Focus on influencing government/policy.'],
        }, subskill='concepts', learning_objective_id=LO_LNP, question_family_id='lobbying_definition', concept_id='lobbying', concept_group='lobbying', misconception_tags=['confuses_lobbying_with_networking'], diagnostic_tags=['definition', 'lobbying']),
        with_metadata({
            'title': 'Networking',
            'prompt': 'Businesses sharing information and developing professional contacts to benefit all members is called …',
            'options': ['lobbying', 'hedging', 'networking', 'a takeover'],
            'correct_index': 2,
            'explanation': 'Networking is where businesses share information and develop professional contacts to benefit all the members in the network.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify building professional contacts.',
                'The goal is to reach as many people as possible and make each connection count.',
                'Examples: chambers of commerce (formal) and golf/sport events (informal).',
            ),
            'guidelines': ['Focus on contacts and shared information for mutual benefit.'],
        }, subskill='concepts', learning_objective_id=LO_LNP, question_family_id='networking_definition', concept_id='networking', concept_group='networking', misconception_tags=['confuses_networking_with_lobbying'], diagnostic_tags=['definition', 'networking']),
        with_metadata({
            'title': 'Power relations',
            'prompt': 'A measure of a business\'s ability to control its environment and the behaviour of other businesses is called …',
            'options': ['power relations', 'information management', 'hedging', 'social responsibility'],
            'correct_index': 0,
            'explanation': 'Power relations describe a business\'s ability to control its environment and the behaviour of other businesses.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify ability to control/influence others.',
                'When businesses negotiate, one may be in a stronger position.',
                'Formed via strategic alliances, persuading large investors and company representatives.',
            ),
            'guidelines': ['Focus on control and influence over others.'],
        }, subskill='concepts', learning_objective_id=LO_LNP, question_family_id='power_relations_definition', concept_id='power_relations', concept_group='power_relations', misconception_tags=['confuses_power_relations_with_networking'], diagnostic_tags=['definition', 'power_relations']),
        with_metadata({
            'title': 'Social responsibility',
            'prompt': 'The obligation a business has to protect its environment and improve the quality of life in its communities is called …',
            'options': ['social responsibility', 'lobbying', 'hedging', 'bargaining'],
            'correct_index': 0,
            'explanation': 'Social responsibility is the obligation a business has to protect the environment and improve community quality of life.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify obligation to environment and community.',
                'It is a way a business can have a direct, positive influence on the environment.',
                'Projects benefit communities and improve the business image.',
            ),
            'guidelines': ['Focus on responsibility to environment and society.'],
        }, subskill='concepts', learning_objective_id=LO_INFLUENCE, question_family_id='social_responsibility_definition', concept_id='social_responsibility', concept_group='direct_influence', misconception_tags=['confuses_social_responsibility_with_profit'], diagnostic_tags=['definition', 'social_responsibility']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Identify the restructuring type',
            'prompt': 'Two competing bakeries agree to join all their resources and trade as one new company, ABC Bakeries. Identify the type of business combination and motivate your answer. (4 marks)',
            'marks': 4,
            'marking_points': [
                'This is a merger.',
                'Two businesses joined their resources to form one new business.',
                'It was done by agreement between the two bakeries.',
                'They now trade as one new company (ABC Bakeries).',
            ],
            'sample_answer': 'This is a merger because the two bakeries joined their resources by agreement to form one new business that trades as ABC Bakeries.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the scenario to merger/takeover/acquisition/alliance.',
                '"Join all resources" + "one new company" signals a merger.',
                'A new combined business = merger; control via shares = takeover.',
            ),
            'answer_part_hints': ['Name the combination type.', 'Quote evidence from the scenario.'],
            'guidelines': ['Use scenario wording as evidence.'],
            'teaching_note': 'Strong answers name the type AND justify with scenario evidence.',
            'keywords': ['merger', 'join', 'resources', 'new business', 'agreement'],
        }, subskill='application', learning_objective_id=LO_ADAPT, question_family_id='identify_restructuring_scenario', concept_id='merger', concept_group='mergers_takeovers_acquisitions_alliances', scenario_family_id='bakery_merger', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Recommend a social responsibility project',
            'prompt': 'A manufacturing business wants to have a positive direct influence on its community. Recommend ONE social responsibility project it could undertake and explain TWO benefits for the business. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend a relevant project (e.g. clean-up campaign, bursaries, feeding scheme).',
                'Benefit: improves the business image/reputation in the community.',
                'Benefit: builds customer loyalty and can increase market share.',
                'Benefit: attracts/retains staff and builds goodwill.',
            ],
            'sample_answer': 'The business could fund a community feeding scheme. This improves its reputation and goodwill in the community, and builds customer loyalty which can increase market share.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Pair a project with business benefits.',
                'Social responsibility improves image, loyalty and goodwill.',
                'Benefits should link back to the business, not only the community.',
            ),
            'answer_part_hints': ['Name a project.', 'Give two benefits to the business.'],
            'guidelines': ['Link each benefit to the business.'],
            'teaching_note': 'Answers must connect the project to clear business benefits.',
            'keywords': ['social responsibility', 'image', 'reputation', 'loyalty', 'goodwill', 'community'],
        }, subskill='application', learning_objective_id=LO_INFLUENCE, question_family_id='recommend_social_responsibility', concept_id='social_responsibility', concept_group='direct_influence', scenario_family_id='manufacturer_social_responsibility', diagnostic_tags=['recommendation', 'social_responsibility'], answer_structure_tags=['recommend', 'explain_benefit'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Identify lobbying, networking or power relations',
            'prompt': 'A business joins the local chamber of commerce, regularly attends its events and exchanges ideas with other members. Identify which strategy this illustrates and give ONE advantage of it. (4 marks)',
            'marks': 4,
            'marking_points': [
                'This illustrates networking.',
                'Members meet and exchange information/ideas.',
                'Advantage: attracts new customers / generates business leads.',
                'Advantage: new perspectives, business ideas and relationships.',
            ],
            'sample_answer': 'This illustrates networking, because the business meets and exchanges ideas with others through the chamber of commerce. An advantage is that it generates new business leads and relationships that can increase market share.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Distinguish networking from lobbying and power relations.',
                'Meeting and exchanging ideas through a chamber = networking.',
                'Lobbying targets government policy; power relations are about control.',
            ),
            'answer_part_hints': ['Name the strategy.', 'Give one advantage.'],
            'guidelines': ['Use scenario evidence to justify.'],
            'teaching_note': 'Networking is about contacts and shared information for mutual benefit.',
            'keywords': ['networking', 'chamber of commerce', 'contacts', 'leads', 'ideas'],
        }, subskill='application', learning_objective_id=LO_LNP, question_family_id='identify_lnp_scenario', concept_id='networking', concept_group='networking', scenario_family_id='chamber_networking', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['identify', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Strategic response to a challenge',
            'prompt': 'A new competitor opens nearby and starts taking a business\'s customers. Explain how a strategic response could help the business adapt to this challenge. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Management analyses information and the new competitor\'s effect.',
                'They design proper plans/strategies to respond.',
                'They consider stakeholders\' viewpoints and requirements.',
                'A strategic response helps identify, minimise and eliminate the challenge to stay sustainable.',
            ],
            'sample_answer': 'A strategic response means management analyses the threat from the new competitor and puts proper plans in place, considering stakeholders, so it can minimise the challenge and remain sustainable in a competitive market.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Apply the strategic-response adaptation method.',
                'Strategic responses use analysis and planning to address challenges.',
                'Good answers link the plan to staying competitive/sustainable.',
            ),
            'answer_part_hints': ['Explain analysing the challenge.', 'Explain putting plans in place.'],
            'guidelines': ['Connect the response to sustainability/competitiveness.'],
            'teaching_note': 'Strong answers describe analysis + planning, not just "work harder".',
            'keywords': ['strategic response', 'plans', 'analyse', 'competitor', 'sustainable', 'stakeholders'],
        }, subskill='application', learning_objective_id=LO_ADAPT, question_family_id='strategic_response_scenario', concept_id='strategic_response', concept_group='ways_to_adapt', scenario_family_id='new_competitor_response', diagnostic_tags=['scenario_analysis', 'adaptation'], answer_structure_tags=['explain', 'apply'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Ways to adapt to challenges',
            'prompt': 'Discuss ways in which businesses can adapt to the challenges of the business environments. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Information management: collect, store and use information effectively (invest in IT).',
                'Strategic responses: analyse challenges and put proper plans in place.',
                'Mergers, takeovers, acquisitions and alliances to respond and survive.',
                'Organisation design and flexibility to adapt structures.',
                'Direct influence on the environment and social responsibility.',
            ],
            'sample_answer': 'Businesses can adapt through effective information management (investing in IT to store and use information), strategic responses (analysing challenges and planning), mergers/takeovers/acquisitions/alliances to survive, flexible organisation design, and by having a direct influence on the environment through social responsibility.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List and explain several adaptation methods.',
                'Cover information management, strategic responses and restructuring.',
                'Add organisation design/flexibility and social responsibility.',
            ),
            'answer_part_hints': ['Name each method.', 'Explain how each helps the business adapt.'],
            'guidelines': ['Give at least four distinct methods with explanation.'],
            'teaching_note': 'Reward breadth across the curriculum list plus explanation.',
            'keywords': ['information management', 'strategic responses', 'mergers', 'alliances', 'flexibility', 'social responsibility'],
        }, subskill='discussion', learning_objective_id=LO_ADAPT, question_family_id='ways_to_adapt_discussion', concept_id='ways_to_adapt', concept_group='ways_to_adapt', diagnostic_tags=['discussion', 'adaptation'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Reasons why businesses lobby',
            'prompt': 'Explain the reasons why businesses lobby. (6 marks)',
            'marks': 6,
            'marking_points': [
                'To influence/change government policy in their favour.',
                'To advance what the business must deliver on and build public trust.',
                'To find solutions to emerging generic challenges.',
                'To advance a cause and protect the business\'s sustainability.',
            ],
            'sample_answer': 'Businesses lobby to influence and change government policy in their favour, to advance what they must deliver and build public trust, to find solutions to emerging challenges, and to advance a cause that protects their sustainability.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Give reasons, not just a definition.',
                'Lobbying aims to change policy and build trust.',
                'It helps businesses address challenges and protect sustainability.',
            ),
            'answer_part_hints': ['Give several reasons.', 'Keep each reason distinct.'],
            'guidelines': ['Provide at least three reasons.'],
            'teaching_note': 'Do not confuse reasons for lobbying with types of lobbying.',
            'keywords': ['lobby', 'government policy', 'public trust', 'cause', 'challenges'],
        }, subskill='discussion', learning_objective_id=LO_LNP, question_family_id='reasons_to_lobby_discussion', concept_id='lobbying', concept_group='lobbying', diagnostic_tags=['discussion', 'lobbying'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Advantages of networking',
            'prompt': 'Discuss the advantages of networking for a business. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Attracts new customers, increasing market share and profitability.',
                'A source of new perspectives and business ideas.',
                'Builds new business relationships and generates opportunities.',
                'Assists with marketing/expansion and future business decisions.',
            ],
            'sample_answer': 'Networking can attract new customers and increase market share and profitability, provide new perspectives and ideas, build relationships and generate new opportunities, and assist with marketing, expansion and future business decisions.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'List benefits of building professional contacts.',
                'Think customers, ideas, relationships and opportunities.',
                'Networking also supports marketing and expansion.',
            ),
            'answer_part_hints': ['Give several advantages.', 'Link each to the business.'],
            'guidelines': ['Provide at least three advantages.'],
            'teaching_note': 'Reward distinct, business-linked advantages.',
            'keywords': ['networking', 'customers', 'market share', 'ideas', 'relationships', 'opportunities'],
        }, subskill='discussion', learning_objective_id=LO_LNP, question_family_id='advantages_of_networking_discussion', concept_id='networking', concept_group='networking', diagnostic_tags=['discussion', 'networking'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Ways to form power relations',
            'prompt': 'Describe ways in which businesses can form power relationships. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Strategic alliance/partnership agreements to benefit from each other.',
                'Persuasion of large/powerful investors to gain credit and better deals.',
                'Using influential company representatives on boards.',
                'Using influence to control the environment and other businesses.',
            ],
            'sample_answer': 'Businesses can form power relationships through strategic alliance/partnership agreements, by persuading large powerful investors (gaining easier credit and better supplier deals), by appointing influential company representatives, and by using their influence to control their environment and other businesses.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List ways to build control/influence.',
                'Think alliances, powerful investors and representatives.',
                'Power relations are about controlling the environment and others.',
            ),
            'answer_part_hints': ['Name each way.', 'Explain how it builds power.'],
            'guidelines': ['Provide at least three ways.'],
            'teaching_note': 'Distinguish power relations from ordinary networking.',
            'keywords': ['power relations', 'strategic alliance', 'investors', 'representatives', 'influence'],
        }, subskill='discussion', learning_objective_id=LO_LNP, question_family_id='form_power_relations_discussion', concept_id='power_relations', concept_group='power_relations', diagnostic_tags=['discussion', 'power_relations'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
