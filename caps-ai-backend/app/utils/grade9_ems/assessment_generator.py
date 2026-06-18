import random
from . import term1_crj_cpj, term1_general_ledger, term1_economy, term2_debtors_journal, term2_economy, term3_creditors_journal, term3_debtors_ledger, term3_business

def _rng(seed=None):
    if seed is not None:
        return random.Random(seed)
    return random.Random()

def generate(subskill="assessment", difficulty="medium", count=1, mode="assessment", seed=None, **kwargs):
    rng = _rng(seed)
    questions = []
    
    # 1. Economic Systems (Term 1)
    try:
        q1 = term1_economy.generate(count=1, seed=rng.randint(1, 10000), mode=mode)[0]
        questions.append(q1)
    except:
        pass
        
    # 2. General Ledger (Term 1)
    try:
        q2 = term1_general_ledger.generate(count=1, seed=rng.randint(1, 10000), mode=mode)[0]
        questions.append(q2)
    except:
        pass
        
    # 3. CRJ/CPJ (Term 1)
    try:
        q3 = term1_crj_cpj.generate(subskill="crj", count=1, seed=rng.randint(1, 10000), mode=mode)[0]
        questions.append(q3)
    except:
        pass
        
    # 4. Debtors Journal (Term 2)
    try:
        q4 = term2_debtors_journal.generate(count=1, seed=rng.randint(1, 10000), mode=mode)[0]
        questions.append(q4)
    except:
        pass
        
    # 5. Price Theory (Term 2)
    try:
        q5 = term2_economy.generate(count=1, seed=rng.randint(1, 10000), mode=mode)[0]
        questions.append(q5)
    except:
        pass

    # 6. Creditors Journal (Term 3)
    try:
        q6 = term3_creditors_journal.generate(count=1, seed=rng.randint(1, 10000), mode=mode)[0]
        questions.append(q6)
    except:
        pass
        
    # 7. Business Functions (Term 3)
    try:
        q7 = term3_business.generate(count=1, seed=rng.randint(1, 10000), mode=mode)[0]
        questions.append(q7)
    except:
        pass
    
    if count < len(questions):
        questions = rng.sample(questions, count)
        
    return questions
