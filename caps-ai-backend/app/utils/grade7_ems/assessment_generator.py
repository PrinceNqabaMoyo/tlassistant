import random
from app.utils.grade7_ems import (
    term1_money_and_needs,
    term1_businesses,
    term2_accounting_concepts,
    term2_income_and_expenses,
    term2_budgets,
    term3_entrepreneurship
)

def _rng(seed=None):
    return random.Random(seed)

def generate_assessment(term="term1", target_marks=50, mode="assessment", seed=None):
    """
    Generates a full exam-style assessment paper for a given term.
    Aggregates questions across topics to hit the target_marks threshold.
    By default uses mode='assessment' (which behaves like 'practice' with no scaffolding).
    """
    rng = _rng(seed)
    
    generators_by_term = {
        'term1': [
            (term1_money_and_needs.generate, ['concepts', 'discussion']),
            (term1_businesses.generate, ['concepts', 'discussion'])
        ],
        'term2': [
            (term2_accounting_concepts.generate, ['concepts', 'discussion']),
            (term2_income_and_expenses.generate, ['concepts', 'calculation', 'journal']),
            (term2_budgets.generate, ['concepts', 'calculation', 'journal'])
        ],
        'term3': [
            (term3_entrepreneurship.generate, ['concepts', 'discussion'])
        ],
        'full_year': [
            (term1_money_and_needs.generate, ['concepts', 'discussion']),
            (term1_businesses.generate, ['concepts', 'discussion']),
            (term2_accounting_concepts.generate, ['concepts', 'discussion']),
            (term2_income_and_expenses.generate, ['concepts', 'calculation', 'journal']),
            (term2_budgets.generate, ['concepts', 'calculation', 'journal']),
            (term3_entrepreneurship.generate, ['concepts', 'discussion'])
        ]
    }
    
    gens = generators_by_term.get(term)
    if not gens:
        raise ValueError(f"Unknown term: {term}")
    
    questions = []
    current_marks = 0
    attempts = 0
    
    # We want a mix of difficulties: easy, medium, hard
    # Assessment papers usually have a normal distribution, but we will pick uniformly for variety
    difficulties = ['easy', 'easy', 'medium', 'medium', 'medium', 'hard']
    
    while current_marks < target_marks and attempts < 100:
        attempts += 1
        gen_func, subskills = rng.choice(gens)
        subskill = rng.choice(subskills)
        difficulty = rng.choice(difficulties)
        
        # generate 1 question
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
    # 2. Typed/Calculation/Journal next
    # 3. Inside categories, sort by difficulty and marks
    def sort_key(q):
        type_weight = 0 if q['question_type'] == 'mcq' else 1
        marks = int(q.get('marks', 1))
        return (type_weight, marks)

    questions.sort(key=sort_key)
    
    # Add question numbers
    for i, q in enumerate(questions):
        q['question_number'] = i + 1
        
    return questions
