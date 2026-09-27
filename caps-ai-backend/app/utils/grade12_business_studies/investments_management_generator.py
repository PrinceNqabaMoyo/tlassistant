import random
from typing import Dict, Any

def generate(**kwargs) -> Dict[str, Any]:
    seed_val = kwargs.get("seed", random.randint(1, 1000000))
    mode = kwargs.get("mode", "compound")
    r = random.Random(seed_val)
    
    context = ""
    instruction = ""
    parts = []
    
    if mode == "elementary_insurance":
        insured = r.randint(300, 600) * 1000
        value = r.randint(700, 1000) * 1000
        loss = r.randint(100, 200) * 1000
        claim = (insured / value) * loss
        context = "Businesses use insurance to protect against pure risks."
        instruction = "Calculate the insurance claim using the average clause."
        parts = [{
            "id": "ins_1",
            "type": "calculation",
            "question": f"A warehouse is valued at R{value}. It is insured for R{insured}. A fire causes damage amounting to R{loss}. Calculate the amount the insurer will pay. Show the formula.",
            "marks": 4,
            "solution": f"Formula: Claim = (Insured Amount / Market Value) x Loss\nClaim = (R{insured} / R{value}) x R{loss}\nClaim = R{claim:.2f}",
            "rubric": "1 mark for formula, 1 mark for substitution, 1 mark for correct calculation, 1 mark for final answer."
        }]
    elif mode == "elementary_investments":
        principal = r.randint(10, 50) * 1000
        rate = r.choice([0.08, 0.10, 0.12])
        years = r.randint(2, 5)
        simple = principal * rate * years
        compound = principal * ((1 + rate) ** years) - principal
        context = "Investment securities offer different returns based on interest calculation methods."
        instruction = "Compare simple and compound interest yields."
        parts = [{
            "id": "inv_1",
            "type": "calculation",
            "question": f"An amount of R{principal} is invested for {years} years at {int(rate*100)}% p.a. Calculate the total interest earned using simple interest and compound interest.",
            "marks": 6,
            "solution": f"Simple Interest: R{principal} x {rate} x {years} = R{simple:.2f}\nCompound Interest: R{principal} x (1 + {rate})^{years} - R{principal} = R{compound:.2f}",
            "rubric": "3 marks for Simple Interest, 3 marks for Compound Interest."
        }]
    elif mode == "elementary_management":
        style = r.choice(["Autocratic", "Democratic", "Laissez-faire", "Transactional", "Transformational"])
        context = "Leadership styles affect employee morale and productivity."
        instruction = "Evaluate the given leadership style."
        parts = [{
            "id": "man_1",
            "type": "essay_sub",
            "question": f"Discuss the impact (positives and negatives) of the {style} leadership style on a business.",
            "marks": 8,
            "solution": f"Impact of {style} leadership...",
            "rubric": "Max 8 marks. 2 marks per point. Include both positives and negatives."
        }]
    else:
        # Compound
        context = "ABC Traders is evaluating its investment portfolio, insurance coverage, and leadership structures."
        instruction = "Answer the following questions."
        
        insured = r.randint(500, 800) * 1000
        value = r.randint(900, 1200) * 1000
        loss = r.randint(150, 300) * 1000
        claim = (insured / value) * loss
        parts.append({
            "id": "comp_1",
            "type": "calculation",
            "question": f"ABC Traders' building is valued at R{value} but insured for R{insured}. Fire damages the building to the value of R{loss}. Calculate the claim amount.",
            "marks": 4,
            "solution": f"Claim = (R{insured} / R{value}) x R{loss} = R{claim:.2f}",
            "rubric": "1 mark formula, 2 marks substitution, 1 mark answer."
        })
        
        parts.append({
            "id": "comp_2",
            "type": "essay_sub",
            "question": "Distinguish between shares and debentures as forms of investment.",
            "marks": 4,
            "solution": "Shares: Ownership in company, returns are dividends (variable). Debentures: Loan to company, returns are interest (fixed).",
            "rubric": "Max 4 marks. 2 marks for shares, 2 marks for debentures."
        })
        
        parts.append({
            "id": "comp_3",
            "type": "essay_sub",
            "question": "Recommend when it is appropriate for a manager to use the democratic leadership style.",
            "marks": 4,
            "solution": "Appropriate when: Employees are skilled/experienced, complex decisions require different perspectives, time is available for consultation.",
            "rubric": "2 marks per valid recommendation (Max 4)."
        })
        
    return {
        "metadata": {
            "subject": "Business Studies",
            "grade": 12,
            "topic": "Investments, Insurance & Management",
            "mode": mode,
            "total_marks": sum(p["marks"] for p in parts)
        },
        "context": context,
        "instruction": instruction,
        "parts": parts,
        "hints": ["Remember the average clause formula for under-insurance.", "Interest is the cost of borrowing or return on investment."]
    }
