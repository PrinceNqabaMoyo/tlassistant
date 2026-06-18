"""Grade 11 Business Studies - Term 1 - Topic 4: Contemporary socio-economic
issues and businesses.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='socio_economic_issues',
    curriculum_reference='Term 1 > Contemporary socio-economic issues and businesses',
    id_prefix='g11_bs_socio',
)

LO_ISSUES = 'lo_socio_economic_issues_impact'
LO_PIRACY = 'lo_piracy_and_solutions'
LO_IR = 'lo_industrial_relations'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Piracy',
            'prompt': 'Goods that are illegally replicated and sold without permission from the registered owner are examples of …',
            'options': ['dumping', 'piracy', 'inflation', 'corruption'],
            'correct_index': 1,
            'explanation': 'Piracy refers to goods that are illegally replicated and sold without permission from the registered owner.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the illegal copying of goods.',
                'Piracy = illegal replication without the owner\'s permission.',
                'Solutions to piracy are copyright, patent and trademark.',
            ),
            'guidelines': ['Focus on illegal copying/replication.'],
        }, subskill='concepts', learning_objective_id=LO_PIRACY, question_family_id='piracy_definition', concept_id='piracy', concept_group='piracy', misconception_tags=['confuses_piracy_with_dumping'], diagnostic_tags=['definition', 'piracy']),
        with_metadata({
            'title': 'Dumping',
            'prompt': 'When excess international goods are imported and flood the local markets, this is called …',
            'options': ['dumping', 'piracy', 'hedging', 'inflation'],
            'correct_index': 0,
            'explanation': 'Dumping is when excess international goods are imported and flood the local markets.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify foreign goods flooding the market.',
                'Dumping floods local markets with cheap imported goods.',
                'It harms local producers who cannot compete on price.',
            ),
            'guidelines': ['Focus on imported goods flooding local markets.'],
        }, subskill='concepts', learning_objective_id=LO_ISSUES, question_family_id='dumping_definition', concept_id='dumping', concept_group='socio_economic_issues', misconception_tags=['confuses_dumping_with_piracy'], diagnostic_tags=['definition', 'socio_economic']),
        with_metadata({
            'title': 'Patent',
            'prompt': 'The exclusive right given by government to the owner of an invention for a limited period (20 years) is a …',
            'options': ['trademark', 'copyright', 'patent', 'licence'],
            'correct_index': 2,
            'explanation': 'A patent is the exclusive right given by government to the owner of an invention for a limited period of twenty years.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the protection to an invention.',
                'A patent protects an invention for a limited period (20 years).',
                'Copyright protects IP works; a trademark protects a brand symbol.',
            ),
            'guidelines': ['Link patents to inventions.'],
        }, subskill='concepts', learning_objective_id=LO_PIRACY, question_family_id='patent_definition', concept_id='patent', concept_group='solutions_to_piracy', misconception_tags=['confuses_patent_with_copyright'], diagnostic_tags=['definition', 'piracy']),
        with_metadata({
            'title': 'Copyright',
            'prompt': 'The right that protects an owner\'s intellectual property to prevent unlawful use is …',
            'options': ['copyright', 'patent', 'trademark', 'a strike'],
            'correct_index': 0,
            'explanation': 'Copyright protects an owner\'s intellectual property (IP) to prevent unlawful use thereof.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the protection to creative/IP works.',
                'Copyright protects intellectual property from unlawful use.',
                'Patents protect inventions; trademarks protect brand symbols.',
            ),
            'guidelines': ['Link copyright to intellectual property.'],
        }, subskill='concepts', learning_objective_id=LO_PIRACY, question_family_id='copyright_definition', concept_id='copyright', concept_group='solutions_to_piracy', misconception_tags=['confuses_copyright_with_trademark'], diagnostic_tags=['definition', 'piracy']),
        with_metadata({
            'title': 'Trademark',
            'prompt': 'A unique symbol that represents a specific brand or business is a …',
            'options': ['patent', 'trademark', 'copyright', 'prospectus'],
            'correct_index': 1,
            'explanation': 'A trademark is a unique symbol that represents a specific brand/business.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the protection to a brand symbol.',
                'A trademark protects a unique brand symbol.',
                'Patents protect inventions; copyright protects IP works.',
            ),
            'guidelines': ['Link trademarks to brand symbols.'],
        }, subskill='concepts', learning_objective_id=LO_PIRACY, question_family_id='trademark_definition', concept_id='trademark', concept_group='solutions_to_piracy', misconception_tags=['confuses_trademark_with_patent'], diagnostic_tags=['definition', 'piracy']),
        with_metadata({
            'title': 'Trade union',
            'prompt': 'An employee organisation intent on improving working conditions is a …',
            'options': ['workplace forum', 'trade union', 'board of directors', 'lockout'],
            'correct_index': 1,
            'explanation': 'A trade union is an employee organisation intent on improving working conditions.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the organisation representing employees.',
                'Trade unions act for employees to improve working conditions.',
                'They negotiate with employers and can call strikes.',
            ),
            'guidelines': ['Focus on representing employees.'],
        }, subskill='concepts', learning_objective_id=LO_IR, question_family_id='trade_union_definition', concept_id='trade_union', concept_group='industrial_relations', misconception_tags=['confuses_union_with_forum'], diagnostic_tags=['definition', 'industrial_relations']),
        with_metadata({
            'title': 'Strike vs lockout',
            'prompt': 'A form of industrial action used by employers to prevent workers from entering the premises is a …',
            'options': ['strike', 'go-slow', 'lockout', 'boycott'],
            'correct_index': 2,
            'explanation': 'A lockout is a form of industrial action used by employers to prevent workers from entering the premises.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Note who initiates the action.',
                'A lockout is started by the employer; a strike by workers.',
                'A go-slow is when workers deliberately work slowly.',
            ),
            'guidelines': ['Distinguish employer vs employee action.'],
        }, subskill='concepts', learning_objective_id=LO_IR, question_family_id='lockout_definition', concept_id='lockout', concept_group='industrial_relations', misconception_tags=['confuses_lockout_with_strike'], diagnostic_tags=['definition', 'industrial_relations']),
        with_metadata({
            'title': 'Labour Relations Act',
            'prompt': 'Which Act regulates industrial relations between employers and employees in South Africa?',
            'options': ['Companies Act (No. 71 of 2008)', 'Labour Relations Act (No. 66 of 1995)', 'Consumer Protection Act', 'Income Tax Act'],
            'correct_index': 1,
            'explanation': 'The Labour Relations Act (No. 66 of 1995) regulates industrial relations and protects the rights of employers and employees.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match labour matters to the correct Act.',
                'The LRA (No. 66 of 1995) governs industrial relations.',
                'It covers strikes, lockouts and union rights.',
            ),
            'guidelines': ['Link industrial relations to the LRA.'],
        }, subskill='concepts', learning_objective_id=LO_IR, question_family_id='lra_identification', concept_id='labour_relations_act', concept_group='industrial_relations', misconception_tags=['confuses_lra_with_companies_act'], diagnostic_tags=['legislation', 'industrial_relations']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Identify the solution to piracy',
            'prompt': 'A music producer discovers their songs are being copied and sold illegally. Recommend the BEST legal solution to protect their work and explain your choice. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend copyright protection.',
                'Copyright protects intellectual property (the songs).',
                'It prevents unlawful use/copying of the work.',
                'The owner can take legal action against those who copy it.',
            ],
            'sample_answer': 'The producer should register copyright, which protects their intellectual property (the songs) and prevents unlawful copying, allowing legal action against anyone who reproduces the work without permission.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the work to the right protection.',
                'Creative works (songs) are protected by copyright.',
                'Patents protect inventions; trademarks protect brand symbols.',
            ),
            'answer_part_hints': ['Name the solution.', 'Explain why it fits.'],
            'guidelines': ['Justify with the type of work being protected.'],
            'teaching_note': 'Copyright fits creative/IP works specifically.',
            'keywords': ['copyright', 'intellectual property', 'songs', 'unlawful', 'protect'],
        }, subskill='application', learning_objective_id=LO_PIRACY, question_family_id='identify_piracy_solution', concept_id='copyright', concept_group='solutions_to_piracy', scenario_family_id='music_piracy', diagnostic_tags=['scenario_analysis', 'piracy'], answer_structure_tags=['recommend', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Impact of a socio-economic issue',
            'prompt': 'Cheap imported clothing is flooding the local market where a small clothing manufacturer operates. Explain how this socio-economic issue impacts the business. (4 marks)',
            'marks': 4,
            'marking_points': [
                'This is dumping of cheap imported goods.',
                'The business loses sales/market share to cheaper imports.',
                'Lower revenue may force retrenchments or closure.',
                'It becomes hard to compete on price/quality.',
            ],
            'sample_answer': 'This is dumping. The cheap imports take sales and market share from the local manufacturer, reducing its revenue and making it hard to compete on price, which may lead to retrenchments or even closure.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Name the issue, then explain its effect.',
                'Flooding with cheap imports = dumping.',
                'Link the issue to sales, jobs and competitiveness.',
            ),
            'answer_part_hints': ['Name the issue.', 'Explain its impact on the business.'],
            'guidelines': ['Connect the issue to concrete business effects.'],
            'teaching_note': 'Reward naming the issue plus a clear business impact.',
            'keywords': ['dumping', 'imports', 'market share', 'compete', 'revenue', 'jobs'],
        }, subskill='application', learning_objective_id=LO_ISSUES, question_family_id='impact_of_issue_scenario', concept_id='dumping', concept_group='socio_economic_issues', scenario_family_id='dumping_clothing', diagnostic_tags=['scenario_analysis', 'socio_economic'], answer_structure_tags=['identify', 'explain_effect'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Evaluate industrial action',
            'prompt': 'Workers at a factory refuse to work until management increases their wages. Identify the type of industrial action and explain ONE way management could resolve the dispute. (4 marks)',
            'marks': 4,
            'marking_points': [
                'This is a strike (workers refuse to work).',
                'Management can hold bargaining/negotiation sessions with the union.',
                'Aim for a win-win wage agreement.',
                'Maintain fair, transparent communication to rebuild trust.',
            ],
            'sample_answer': 'This is a strike because the workers refuse to work. Management could resolve it through bargaining sessions with the trade union, negotiating a fair wage agreement and communicating transparently to reach a win-win outcome.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Name the action, then give a resolution.',
                'Refusing to work = strike.',
                'Bargaining/negotiation with unions resolves disputes.',
            ),
            'answer_part_hints': ['Name the action.', 'Give one resolution.'],
            'guidelines': ['Link resolution to negotiation/bargaining.'],
            'teaching_note': 'Distinguish strike (workers) from lockout (employer).',
            'keywords': ['strike', 'refuse to work', 'bargaining', 'union', 'negotiate', 'wages'],
        }, subskill='application', learning_objective_id=LO_IR, question_family_id='evaluate_industrial_action', concept_id='strike', concept_group='industrial_relations', scenario_family_id='factory_strike', diagnostic_tags=['scenario_analysis', 'industrial_relations'], answer_structure_tags=['identify', 'recommend'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Impact of piracy',
            'prompt': 'Discuss the impact of piracy on businesses. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Loss of sales and income as customers buy illegal copies.',
                'Damage to brand reputation if pirated goods are poor quality.',
                'Reduced incentive to innovate/invest in new products.',
                'Job losses and reduced profitability; legal costs to fight piracy.',
            ],
            'sample_answer': 'Piracy reduces a business\'s sales and income because customers buy cheaper illegal copies. It can damage brand reputation when pirated goods are poor quality, reduces the incentive to innovate, lowers profitability and can cause job losses, while the business also incurs legal costs to fight piracy.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain several effects of piracy.',
                'Think sales, reputation, innovation and jobs.',
                'Piracy also creates legal costs for the business.',
            ),
            'answer_part_hints': ['Give several impacts.', 'Explain each briefly.'],
            'guidelines': ['Provide at least three distinct impacts.'],
            'teaching_note': 'Reward distinct, business-linked impacts.',
            'keywords': ['piracy', 'sales', 'reputation', 'innovation', 'jobs', 'profit'],
        }, subskill='discussion', learning_objective_id=LO_PIRACY, question_family_id='impact_of_piracy_discussion', concept_id='piracy', concept_group='piracy', diagnostic_tags=['discussion', 'piracy'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Roles of trade unions',
            'prompt': 'Discuss the roles of trade unions in the workplace. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Represent and protect the rights/interests of workers.',
                'Negotiate wages and working conditions with employers.',
                'Address poverty reduction and job-creation challenges.',
                'Support members during disputes and improve working conditions.',
            ],
            'sample_answer': 'Trade unions represent and protect workers\' rights, negotiate wages and working conditions with employers, address poverty reduction and job-creation challenges, and support members during disputes while working to improve overall working conditions.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List what unions do for workers.',
                'Think representation, negotiation and protection.',
                'Unions also address broader social challenges.',
            ),
            'answer_part_hints': ['Give several roles.', 'Explain each role.'],
            'guidelines': ['Provide at least three roles.'],
            'teaching_note': 'Reward distinct roles tied to worker interests.',
            'keywords': ['trade union', 'represent', 'negotiate', 'working conditions', 'rights', 'poverty'],
        }, subskill='discussion', learning_objective_id=LO_IR, question_family_id='roles_of_unions_discussion', concept_id='trade_union', concept_group='industrial_relations', diagnostic_tags=['discussion', 'industrial_relations'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Ethical misconduct',
            'prompt': 'Explain ethical misconduct in businesses, using examples. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Ethical misconduct is unacceptable behaviour within a business.',
                'Example: corruption through dishonest dealings such as bribery.',
                'Example: sexual harassment of colleagues.',
                'Example: mismanagement of funds for personal gain.',
            ],
            'sample_answer': 'Ethical misconduct is unacceptable behaviour within a business. Examples include corruption through bribery and dishonest dealings, sexual harassment of colleagues, and the mismanagement of funds for personal gain. Such conduct damages trust and the business\'s reputation.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Define the term and give examples.',
                'Ethical misconduct = unacceptable business behaviour.',
                'Examples: corruption, sexual harassment, mismanagement of funds.',
            ),
            'answer_part_hints': ['Define ethical misconduct.', 'Give examples.'],
            'guidelines': ['Include a definition and at least two examples.'],
            'teaching_note': 'Reward definition plus concrete examples.',
            'keywords': ['ethical misconduct', 'corruption', 'bribery', 'sexual harassment', 'mismanagement'],
        }, subskill='discussion', learning_objective_id=LO_ISSUES, question_family_id='ethical_misconduct_discussion', concept_id='ethical_misconduct', concept_group='socio_economic_issues', diagnostic_tags=['discussion', 'ethics'], answer_structure_tags=['define', 'exemplify'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
