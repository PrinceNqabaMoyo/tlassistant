import random
from typing import Dict, Any, List

def generate(**kwargs) -> Dict[str, Any]:
    seed_val = kwargs.get("seed", random.randint(1, 1000000))
    mode = kwargs.get("mode", "compound")
    r = random.Random(seed_val)
    
    # 6-pillar contract fields
    context = ""
    instruction = ""
    parts = []
    
    if mode == "elementary_legislation":
        acts = ["B-BBEE", "BCEA", "LRA", "COIDA", "CPA"]
        act = r.choice(acts)
        context = "Recent legislation has a profound impact on business operations in South Africa."
        instruction = f"Discuss the impact of the {act} on businesses."
        parts = [{
            "id": "leg_1",
            "type": "essay_sub",
            "question": f"Outline the main pillars or purpose of the {act} and evaluate its impact (positives and negatives) on businesses.",
            "marks": 8,
            "solution": f"Expected points on the impact of {act}, discussing both pros and cons.",
            "rubric": "Max 8 marks. 2 marks per valid point. Must include both positive and negative impacts."
        }]
    elif mode == "elementary_hr_recruitment":
        recruitment_type = r.choice(["Internal", "External"])
        context = "The Human Resources function is responsible for finding the best candidates to fill vacancies."
        instruction = "Evaluate the recruitment procedure."
        parts = [{
            "id": "hr_1",
            "type": "essay_sub",
            "question": f"Explain the meaning of {recruitment_type} recruitment and discuss its advantages for a business.",
            "marks": 6,
            "solution": f"Definition of {recruitment_type} recruitment (2). Advantages include...",
            "rubric": "Max 6 marks. 2 marks for definition, 4 marks for advantages."
        }]
    elif mode == "elementary_salary_calc":
        gross = r.randint(15000, 45000)
        paye_rate = r.choice([0.18, 0.25, 0.30])
        uif_pct = 1
        uif = gross * (uif_pct / 100.0)
        paye = gross * paye_rate
        net = gross - paye - uif
        context = "Salary administration is a key component of the HR function."
        instruction = "Calculate the net salary."
        parts = [{
            "id": "sal_1",
            "type": "calculation",
            "question": f"An employee earns a gross salary of R{gross}. Deductions include PAYE at {int(paye_rate*100)}% and UIF at {uif_pct}%. Calculate the net salary.",
            "marks": 4,
            "solution": f"Gross = R{gross}\nPAYE = {int(paye_rate*100)}% of R{gross} = R{paye:.2f}\nUIF = {uif_pct}% of R{gross} = R{uif:.2f}\nNet Salary = R{gross} - R{paye:.2f} - R{uif:.2f} = R{net:.2f}",
            "rubric": "1 mark for PAYE, 1 mark for UIF, 1 mark for correct subtraction, 1 mark for final net salary."
        }]
    else:
        # Compound
        context = "Thabo's Manufacturing is expanding its operations and needs to comply with legislation while hiring new staff."
        instruction = "Answer the following questions based on the scenario."
        
        acts = ["B-BBEE", "BCEA", "LRA"]
        act = r.choice(acts)
        parts.append({
            "id": "comp_1",
            "type": "essay_sub",
            "question": f"Discuss the impact of the {act} on Thabo's Manufacturing.",
            "marks": 6,
            "solution": f"Points discussing how {act} affects a manufacturing business...",
            "rubric": "2 marks per valid point (Max 6)."
        })
        
        parts.append({
            "id": "comp_2",
            "type": "essay_sub",
            "question": "Outline the selection procedure Thabo should follow after receiving applications.",
            "marks": 6,
            "solution": "1. Screen applications. 2. Shortlist. 3. Interviews. 4. Reference checks. 5. Medical exams (if applicable). 6. Offer of employment.",
            "rubric": "2 marks per valid step (Max 6)."
        })
        
        gross = r.randint(20000, 30000)
        uif = gross * 0.01
        paye = gross * 0.18
        net = gross - paye - uif
        parts.append({
            "id": "comp_3",
            "type": "calculation",
            "question": f"A newly hired manager is offered a gross salary of R{gross}. Calculate their net salary if PAYE is 18% and UIF is 1%.",
            "marks": 3,
            "solution": f"PAYE = R{paye:.2f}\nUIF = R{uif:.2f}\nNet = R{net:.2f}",
            "rubric": "1 mark PAYE, 1 mark UIF, 1 mark Net."
        })
        
    return {
        "metadata": {
            "subject": "Business Studies",
            "grade": 12,
            "topic": "Legislation and Human Resources",
            "mode": mode,
            "total_marks": sum(p["marks"] for p in parts)
        },
        "context": context,
        "instruction": instruction,
        "parts": parts,
        "hints": ["Remember that net salary = gross - deductions.", "Consider both positives and negatives for legislative impacts."]
    }
