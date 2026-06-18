from . import (
    term1_gov_and_society,
    term1_accounting_basics,
    term2_markets_and_production,
    term2_crj,
    term3_cpj_and_crj,
    term3_ownership
)
from .assessment_generator import generate_assessment

def generate_topic_questions(subtopic, subskill="concepts", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    generators = {
        'term1_gov_and_society': term1_gov_and_society.generate,
        'term1_accounting_basics': term1_accounting_basics.generate,
        'term2_markets_and_production': term2_markets_and_production.generate,
        'term2_crj': term2_crj.generate,
        'term3_cpj_and_crj': term3_cpj_and_crj.generate,
        'term3_ownership': term3_ownership.generate
    }
    
    if subtopic not in generators:
        raise ValueError(f"Unknown Grade 8 EMS subtopic: {subtopic}")
        
    return generators[subtopic](subskill=subskill, difficulty=difficulty, count=count, mode=mode, seed=seed, **kwargs)

def generate_assessment_paper(term="term1", target_marks=50, mode="assessment", seed=None):
    return generate_assessment(term=term, target_marks=target_marks, mode=mode, seed=seed)
