import random
from typing import Dict, Any

def generate(**kwargs) -> Dict[str, Any]:
    seed_val = kwargs.get("seed", random.randint(1, 1000000))
    mode = kwargs.get("mode", "compound")
    r = random.Random(seed_val)
    
    context = ""
    instruction = ""
    parts = []
    
    if mode == "elementary_savings":
        amount = r.randint(1, 5) * 1000
        rate = r.randint(5, 10)
        interest = amount * (rate/100)
        context = "Savings play an important role in economic growth."
        instruction = "Calculate the interest earned on savings."
        parts = [{
            "id": "sav_1",
            "type": "calculation",
            "question": f"A student saves R{amount} in a bank account that offers {rate}% interest per year. Calculate the interest earned after one year.",
            "marks": 3,
            "solution": f"Interest = R{amount} x {rate}% = R{interest:.2f}",
            "rubric": "1 mark for correct principal and rate, 1 mark for calculation, 1 mark for answer."
        }]
    elif mode == "elementary_production":
        sector = r.choice(["Primary", "Secondary", "Tertiary"])
        context = "The production process turns raw materials into finished goods and services."
        instruction = "Identify the economic sector."
        parts = [{
            "id": "prod_1",
            "type": "essay_sub",
            "question": f"Describe the role of the {sector} sector in the production process and give one example of a business in this sector.",
            "marks": 4,
            "solution": f"Role of {sector} sector... Example...",
            "rubric": "2 marks for role description, 2 marks for a valid example."
        }]
    else:
        # Compound
        context = "A local furniture manufacturer is expanding their operations and wants to ensure their management and production processes are efficient."
        instruction = "Answer the following questions."
        
        parts.append({
            "id": "comp_1",
            "type": "essay_sub",
            "question": "Name and briefly explain the three levels of management in a business.",
            "marks": 6,
            "solution": "Top management (strategic), Middle management (tactical), Lower/First-line management (operational).",
            "rubric": "1 mark for naming, 1 mark for explanation per level (Max 6)."
        })
        
        parts.append({
            "id": "comp_2",
            "type": "essay_sub",
            "question": "Explain the four factors of production required by the furniture manufacturer.",
            "marks": 8,
            "solution": "Capital (machinery), Land/Natural Resources (wood), Labour (carpenters), Entrepreneurship (owner).",
            "rubric": "1 mark for naming, 1 mark for explanation per factor (Max 8)."
        })
        
        amount = r.randint(10, 50) * 1000
        rate = r.randint(6, 12)
        interest = amount * (rate/100)
        parts.append({
            "id": "comp_3",
            "type": "calculation",
            "question": f"The business saves R{amount} of its profits in a fixed deposit account earning {rate}% simple interest p.a. Calculate the interest earned in one year.",
            "marks": 3,
            "solution": f"Interest = R{amount} x {rate}% = R{interest:.2f}",
            "rubric": "1 mark formula/substitution, 2 marks answer."
        })
        
    return {
        "metadata": {
            "subject": "EMS",
            "grade": 8,
            "topic": "Management, Production and Savings",
            "mode": mode,
            "total_marks": sum(p["marks"] for p in parts)
        },
        "context": context,
        "instruction": instruction,
        "parts": parts,
        "hints": ["Management is divided into top, middle, and lower levels.", "The four factors of production are land, labour, capital, and entrepreneurship."]
    }
