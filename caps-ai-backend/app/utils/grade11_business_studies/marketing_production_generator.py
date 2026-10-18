import random
from typing import Dict, Any

def generate(**kwargs) -> Dict[str, Any]:
    seed_val = kwargs.get("seed", random.randint(1, 1000000))
    mode = kwargs.get("mode", "compound")
    r = random.Random(seed_val)
    
    context = ""
    instruction = ""
    parts = []
    
    if mode == "elementary_marketing":
        p = r.choice(["Product", "Price", "Place", "Promotion"])
        context = "The marketing mix is composed of the 4Ps."
        instruction = "Explain one element of the marketing mix."
        parts = [{
            "id": "mkt_1",
            "type": "essay_sub",
            "question": f"Discuss the role of '{p}' as an element of the marketing mix.",
            "marks": 6,
            "solution": f"Expected points regarding the {p} element...",
            "rubric": "Max 6 marks. 2 marks per valid point."
        }]
    elif mode == "elementary_production":
        concept = r.choice(["Quality Control", "Quality Assurance"])
        context = "The production function manages the physical creation of goods."
        instruction = "Explain quality management concepts."
        parts = [{
            "id": "prod_1",
            "type": "essay_sub",
            "question": f"Explain the concept of {concept} in the context of the production function.",
            "marks": 4,
            "solution": f"Explanation of {concept}...",
            "rubric": "Max 4 marks. 2 marks per valid point."
        }]
    else:
        # Compound
        context = "Moyo Manufacturing produces high-quality consumer goods and needs to align its production and marketing strategies."
        instruction = "Answer the questions below based on the scenario."
        
        parts.append({
            "id": "comp_1",
            "type": "essay_sub",
            "question": "Differentiate between quality control and quality assurance.",
            "marks": 4,
            "solution": "Quality Control: Inspecting final products (reactive). Quality Assurance: Process-oriented, ensuring quality at every step (proactive).",
            "rubric": "Max 4 marks. 2 marks for Quality Control, 2 marks for Quality Assurance."
        })
        
        ps = r.sample(["Product", "Price", "Place", "Promotion"], 2)
        parts.append({
            "id": "comp_2",
            "type": "essay_sub",
            "question": f"Evaluate the impact of {ps[0]} and {ps[1]} on the success of Moyo Manufacturing.",
            "marks": 8,
            "solution": f"Impact points for {ps[0]}... Impact points for {ps[1]}...",
            "rubric": "Max 8 marks. 4 marks for each element."
        })
        
        parts.append({
            "id": "comp_3",
            "type": "essay_sub",
            "question": "Outline the safety regulations (Occupational Health and Safety Act) that the production manager must implement in the factory.",
            "marks": 6,
            "solution": "Provide protective clothing, ensure safe working environment, report accidents, first aid availability.",
            "rubric": "2 marks per valid point (Max 6)."
        })
        
    full_prompt = f"{context}\n\n{instruction}\n\n" + "\n\n".join(
        f"{p['id']}. {p['question']} ({p['marks']} marks)" for p in parts
    )
    total_marks = sum(p["marks"] for p in parts)
    
    return {
        "id": f"g11_bs_mkt_prod_{r.randint(100000, 999999)}",
        "topic": "Marketing and Production",
        "subskill": "marketing_production_integration",
        "mode": mode,
        "marks": total_marks,
        "prompt": full_prompt,
        "question": full_prompt,
        "sample_answer": "\n\n".join(f"{p['id']}: {p['solution']}" for p in parts),
        "marking_schema": {
            "total_marks": total_marks,
            "marking_points": [
                {"id": p["id"], "desc": p["question"][:60], "marks": p["marks"], "editable": True}
                for p in parts
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": "Review the 4Ps of marketing (Product, Price, Place, Promotion) and production quality systems.",
            "tier_2": "Quality control is reactive end-of-line testing; quality assurance is proactive process prevention.",
            "tier_3": "Connect OHSA regulations (protective gear, machine guards) directly to workplace compliance."
        },
        "metadata": {
            "subject": "Business Studies",
            "grade": 11,
            "topic": "Marketing and Production",
            "mode": mode,
            "total_marks": total_marks
        },
        "context": context,
        "instruction": instruction,
        "parts": parts,
    }
