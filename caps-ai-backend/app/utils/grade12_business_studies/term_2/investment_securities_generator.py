"""Grade 12 Business Studies - Term 2 - Investment: Securities.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='investment_securities',
    curriculum_reference='Term 2 > Investment: Securities',
    id_prefix='g12_bs_securities',
)

LO_JSE = 'lo_jse_factors'
LO_FORMS = 'lo_forms_of_investment'
LO_SHARES = 'lo_types_of_shares'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Function of the JSE',
            'prompt': 'Which is a main function of the Johannesburg Securities Exchange (JSE)?',
            'options': [
                'To set income tax rates',
                'To provide a market where shares and securities are bought and sold',
                'To pay salaries of employees',
                'To insure businesses against risk',
            ],
            'correct_index': 1,
            'explanation': 'The JSE provides a regulated market where shares and other securities are bought and sold, giving businesses access to capital and investors a place to trade.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on buying and selling shares.',
                'A market to trade shares/securities = the JSE.',
                'Tax is set by government, not the JSE.',
            ),
            'guidelines': ['Market to trade shares = JSE function.'],
        }, subskill='concepts', learning_objective_id=LO_JSE, question_family_id='jse_function_identify', concept_id='jse', concept_group='jse', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Ordinary shares',
            'prompt': 'Shares that carry voting rights and a variable dividend depending on profit are …',
            'options': ['preference shares', 'ordinary shares', 'debentures', 'bonus shares'],
            'correct_index': 1,
            'explanation': 'Ordinary shares carry voting rights and earn a variable dividend that depends on the company\u2019s profit.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on voting rights and variable dividends.',
                'Voting + variable dividend = ordinary shares.',
                'Preference shares get a fixed dividend and usually no vote.',
            ),
            'guidelines': ['Voting + variable dividend = ordinary shares.'],
        }, subskill='concepts', learning_objective_id=LO_SHARES, question_family_id='ordinary_shares_identify', concept_id='ordinary_shares', concept_group='shares', misconception_tags=['confuses_ordinary_with_preference'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Preference shares',
            'prompt': 'Shares that receive a fixed dividend and are paid before ordinary shareholders are …',
            'options': ['ordinary shares', 'preference shares', 'founders shares', 'bonus shares'],
            'correct_index': 1,
            'explanation': 'Preference shares earn a fixed dividend and are paid before ordinary shareholders, but usually carry no voting rights.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on a fixed dividend and payment priority.',
                'Fixed dividend, paid first = preference shares.',
                'Ordinary shares get a variable dividend.',
            ),
            'guidelines': ['Fixed dividend, paid first = preference shares.'],
        }, subskill='concepts', learning_objective_id=LO_SHARES, question_family_id='preference_shares_identify', concept_id='preference_shares', concept_group='shares', misconception_tags=['confuses_preference_with_ordinary'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Unit trusts',
            'prompt': 'An investment where money from many investors is pooled and invested in a range of assets by a manager is a …',
            'options': ['fixed deposit', 'unit trust', 'debenture', 'RSA Retail Savings Bond'],
            'correct_index': 1,
            'explanation': 'A unit trust pools money from many investors, which a fund manager invests across a range of assets, spreading risk.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on pooled money managed for investors.',
                'Pooled, professionally managed funds = unit trust.',
                'A fixed deposit is a single lump sum at a bank.',
            ),
            'guidelines': ['Pooled, managed funds = unit trust.'],
        }, subskill='concepts', learning_objective_id=LO_FORMS, question_family_id='unit_trust_identify', concept_id='unit_trust', concept_group='forms', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Simple vs compound interest',
            'prompt': 'Interest calculated only on the original principal amount each period is …',
            'options': ['compound interest', 'simple interest', 'a dividend', 'a capital gain'],
            'correct_index': 1,
            'explanation': 'Simple interest is calculated only on the original principal, while compound interest is calculated on the principal plus accumulated interest.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on interest on the original amount only.',
                'Interest on the principal only = simple interest.',
                'Interest on interest = compound interest.',
            ),
            'guidelines': ['Interest on principal only = simple interest.'],
        }, subskill='concepts', learning_objective_id=LO_FORMS, question_family_id='interest_identify', concept_id='simple_interest', concept_group='forms', misconception_tags=['confuses_simple_with_compound'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Dividends',
            'prompt': 'A portion of a company\u2019s profit paid out to shareholders is a …',
            'options': ['dividend', 'debenture', 'capital gain', 'levy'],
            'correct_index': 0,
            'explanation': 'A dividend is a portion of a company\u2019s profit that is paid out to its shareholders.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on profit paid to shareholders.',
                'Profit share to shareholders = dividend.',
                'A debenture is a loan to the company.',
            ),
            'guidelines': ['Profit share to shareholders = dividend.'],
        }, subskill='concepts', learning_objective_id=LO_SHARES, question_family_id='dividend_definition', concept_id='dividend', concept_group='shares', diagnostic_tags=['definition']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Calculate simple interest',
            'prompt': 'Thabo invests R10 000 at 8% simple interest per year for 3 years. Calculate the total interest earned and the final amount. Show your working. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Simple interest = P x r x n = 10 000 x 0.08 x 3.',
                'Interest = R2 400.',
                'Final amount = principal + interest = 10 000 + 2 400.',
                'Final amount = R12 400.',
            ],
            'sample_answer': 'Simple interest = P x r x n = 10 000 x 0.08 x 3 = R2 400. The final amount = 10 000 + 2 400 = R12 400.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Use the simple interest formula.',
                'Interest = principal x rate x number of years.',
                'Add the interest to the principal for the final amount.',
            ),
            'answer_part_hints': ['Calculate the interest.', 'Calculate the final amount.'],
            'guidelines': ['Show working and final amount.'],
            'teaching_note': 'Reward correct formula, interest and final amount.',
            'keywords': ['simple interest', 'principal', 'rate', '2400', '12400'],
        }, subskill='application', learning_objective_id=LO_FORMS, question_family_id='simple_interest_calc', concept_id='simple_interest', concept_group='forms', scenario_family_id='thabo_investment', diagnostic_tags=['calculation'], answer_structure_tags=['calculate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Recommend an investment',
            'prompt': 'An investor wants a low-risk, government-backed investment for 5 years. Recommend a suitable form of investment and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend RSA Retail Savings Bonds / a government bond.',
                'It is government-backed, so it is low risk.',
                'It offers a guaranteed/fixed return over the period.',
                'It suits an investor who prioritises safety over high returns.',
            ],
            'sample_answer': 'The investor should choose RSA Retail Savings Bonds because they are government-backed and therefore low risk, and they offer a guaranteed return over the chosen period. This suits an investor who prioritises safety over high returns.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match low-risk and government-backed to a product.',
                'Government-backed, low risk = RSA Retail Savings Bonds.',
                'Motivate with safety and guaranteed return.',
            ),
            'answer_part_hints': ['Name the investment.', 'Motivate the choice.'],
            'guidelines': ['Recommend a low-risk investment and motivate.'],
            'teaching_note': 'Reward RSA bonds with a safety motivation.',
            'keywords': ['RSA Retail Savings Bonds', 'government', 'low risk', 'guaranteed', 'safety'],
        }, subskill='application', learning_objective_id=LO_FORMS, question_family_id='recommend_investment_scenario', concept_id='government_bonds', concept_group='forms', scenario_family_id='low_risk_investor', diagnostic_tags=['scenario_analysis'], answer_structure_tags=['recommend', 'motivate'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Ordinary vs preference shares',
            'prompt': 'Distinguish between ordinary and preference shares. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Ordinary shares carry voting rights; preference shares usually do not.',
                'Ordinary shares earn a variable dividend; preference shares earn a fixed dividend.',
                'Preference shareholders are paid dividends before ordinary shareholders.',
                'Ordinary shareholders carry more risk but more potential reward.',
            ],
            'sample_answer': 'Ordinary shares carry voting rights and earn a variable dividend that depends on profit, while preference shares usually carry no voting rights and earn a fixed dividend. Preference shareholders are paid before ordinary shareholders, so ordinary shareholders carry more risk but have greater potential reward.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Contrast the two types of shares.',
                'Compare voting rights, dividends and payment order.',
                'Note the risk/reward difference.',
            ),
            'answer_part_hints': ['Compare voting and dividends.', 'Compare payment order/risk.'],
            'guidelines': ['Distinguish the two share types.'],
            'teaching_note': 'Reward clear distinctions across the key features.',
            'keywords': ['voting', 'variable dividend', 'fixed dividend', 'paid first', 'risk'],
        }, subskill='discussion', learning_objective_id=LO_SHARES, question_family_id='shares_compare_discussion', concept_id='ordinary_shares', concept_group='shares', diagnostic_tags=['discussion', 'comparison'], answer_structure_tags=['distinguish'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Factors for investment decisions',
            'prompt': 'Discuss the factors an investor should consider when making an investment decision. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Risk: the chance of losing the invested money.',
                'Return: the income/profit expected from the investment.',
                'Liquidity: how easily the investment can be converted to cash.',
                'Investment period/term: how long the money will be tied up.',
                'Inflation and tax implications on the real return.',
            ],
            'sample_answer': 'An investor should consider the risk (chance of losing money), the expected return, and the liquidity (how easily it can be turned into cash). They should also consider the investment period or term, and the effect of inflation and tax on the real return, balancing these factors against their own goals.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List the decision factors.',
                'Risk, return, liquidity, term, inflation/tax.',
                'Explain why each matters.',
            ),
            'answer_part_hints': ['List factors.', 'Explain each.'],
            'guidelines': ['Provide several investment factors.'],
            'teaching_note': 'Reward a range of investment factors.',
            'keywords': ['risk', 'return', 'liquidity', 'period', 'inflation', 'tax'],
        }, subskill='discussion', learning_objective_id=LO_JSE, question_family_id='investment_factors_discussion', concept_id='investment_factors', concept_group='jse', diagnostic_tags=['discussion'], answer_structure_tags=['list'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
