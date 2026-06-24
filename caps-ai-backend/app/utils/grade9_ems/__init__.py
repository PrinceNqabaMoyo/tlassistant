from . import (
    term1_crj_cpj,
    term1_general_ledger,
    term1_economy,
    term1_circular_flow,
    term2_debtors_journal,
    term2_economy,
    term2_sectors_of_economy,
    term3_creditors_journal,
    term3_debtors_ledger,
    term3_business,
    term3_trade_unions,
    assessment_generator,
)
from . import assessment_generator

def generate_topic_questions(subtopic, subskill="concepts", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    generators = {
        'term1_crj_cpj': term1_crj_cpj.generate,
        'term1_general_ledger': term1_general_ledger.generate,
        'term1_economy': term1_economy.generate,
        'term1_circular_flow': term1_circular_flow.generate,
        'term2_debtors_journal': term2_debtors_journal.generate,
        'term2_economy': term2_economy.generate,
        'term2_sectors_of_economy': term2_sectors_of_economy.generate,
        'term3_creditors_journal': term3_creditors_journal.generate,
        'term3_debtors_ledger': term3_debtors_ledger.generate,
        'term3_business': term3_business.generate,
        'term3_trade_unions': term3_trade_unions.generate,
    }

    if subtopic not in generators:
        raise ValueError(f"Unknown Grade 9 EMS subtopic: {subtopic}")

    return generators[subtopic](subskill=subskill, difficulty=difficulty, count=count, mode=mode, seed=seed, **kwargs)

def generate_assessment_paper(term="term1", target_marks=50, mode="assessment", seed=None):
    return assessment_generator.generate(mode=mode, count=5)
