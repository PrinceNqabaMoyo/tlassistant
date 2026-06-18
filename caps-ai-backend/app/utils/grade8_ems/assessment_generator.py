import random
from app.utils.grade8_ems import (
    term1_gov_and_society,
    term1_accounting_basics,
    term2_markets_and_production,
    term2_crj,
    term3_cpj_and_crj,
    term3_ownership
)

def _rng(seed=None):
    return random.Random(seed)

def generate_assessment(term="term1", target_marks=50, mode="assessment", seed=None):
    """
    Generates a full exam-style assessment paper for a given term for Grade 8 EMS.
    Aggregates questions across topics to hit the target_marks threshold.
    """
    rng = _rng(seed)
    
    generators_by_term = {
        'term1': [
            (term1_gov_and_society.generate, ['concepts', 'discussion']),
            (term1_accounting_basics.generate, ['concepts', 'accounting_equation'])
        ],
        'term2': [
            (term2_markets_and_production.generate, ['concepts', 'discussion']),
            (term2_crj.generate, ['crj'])
        ],
        'term3': [
            (term3_cpj_and_crj.generate, ['cpj']),
            (term3_ownership.generate, ['concepts', 'discussion'])
        ],
        'full_year': [
            (term1_gov_and_society.generate, ['concepts', 'discussion']),
            (term1_accounting_basics.generate, ['concepts', 'accounting_equation']),
            (term2_markets_and_production.generate, ['concepts', 'discussion']),
            (term2_crj.generate, ['crj']),
            (term3_cpj_and_crj.generate, ['cpj']),
            (term3_ownership.generate, ['concepts', 'discussion'])
        ]
    }
    
    gens = generators_by_term.get(term)
    if not gens:
        raise ValueError(f"Unknown term: {term}")
    
    questions = []
    current_marks = 0
    attempts = 0
    
    difficulties = ['easy', 'easy', 'medium', 'medium', 'medium', 'hard']
    
    while current_marks < target_marks and attempts < 100:
        attempts += 1
        gen_func, subskills = rng.choice(gens)
        subskill = rng.choice(subskills)
        difficulty = rng.choice(difficulties)
        
        # Generate 1 question
        q_list = gen_func(subskill=subskill, difficulty=difficulty, count=1, mode=mode, seed=rng.randint(0, 999999))
        if q_list:
            q = q_list[0]
            # Avoid exact duplicates by ID
            if not any(existing['id'] == q['id'] for existing in questions):
                # Also avoid exact prompt duplicates
                if not any(existing['prompt'] == q['prompt'] for existing in questions):
                    questions.append(q)
                    current_marks += int(q.get('marks', 1))
    
    # Sort questions: 
    # 1. MCQ first
    # 2. Typed next
    # 3. Tabular last
    def sort_key(q):
        if q['question_type'] == 'mcq':
            type_weight = 0
        elif q['question_type'] == 'typed':
            type_weight = 1
        else:
            type_weight = 2
            
        marks = int(q.get('marks', 1))
        return (type_weight, marks)

    questions.sort(key=sort_key)
    
    for i, q in enumerate(questions):
        q['question_number'] = i + 1
        
    return questions
