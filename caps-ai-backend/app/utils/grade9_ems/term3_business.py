import random

def _rng(seed=None):
    if seed is not None:
        return random.Random(seed)
    return random.Random()

def _with_metadata(item, subskill, learning_objective_id, question_family_id, concept_id, concept_group, diagnostic_tags):
    item['subskill'] = subskill
    item['learning_objective_id'] = learning_objective_id
    item['question_family_id'] = question_family_id
    item['concept_id'] = concept_id
    item['concept_group'] = concept_group
    item['diagnostic_tags'] = diagnostic_tags
    return item

def _generate_business_functions(rng, mode, seed=None):
    questions = [
        {
            "prompt": "Which business function is responsible for finding, hiring, training, and managing employees?",
            "sample_answer": "Human Resources (HR)",
            "ideal_answer": "The Human Resources function.",
            "hint_sections": {
                "1_nudge": "Think about the department that deals with the 'people' in the business.",
                "2_concept": "This function handles recruitment, training, and employee well-being.",
                "3_breakdown": "It is called Human Resources or HR."
            }
        },
        {
            "prompt": "Which business function is responsible for acquiring capital, managing cash flow, and preparing financial statements?",
            "sample_answer": "Financial Function",
            "ideal_answer": "The Financial function.",
            "hint_sections": {
                "1_nudge": "Think about the department responsible for tracking money and budgets.",
                "2_concept": "This function ensures the business has enough funds to operate and stay solvent.",
                "3_breakdown": "It is called the Financial function."
            }
        },
        {
            "prompt": "Which business function is responsible for transforming raw materials into finished goods and maintaining quality control?",
            "sample_answer": "Production Function",
            "ideal_answer": "The Production or Operations function.",
            "hint_sections": {
                "1_nudge": "Think about the factory floor where goods are physically manufactured.",
                "2_concept": "This function combines labour, machinery, and raw inputs to create goods.",
                "3_breakdown": "It is called the Production function."
            }
        },
        {
            "prompt": "Which business function is responsible for market research, advertising, product pricing, and distribution (the 4 Ps)?",
            "sample_answer": "Marketing Function",
            "ideal_answer": "The Marketing function.",
            "hint_sections": {
                "1_nudge": "Think about how customers learn about products and decide to buy them.",
                "2_concept": "This function manages Product, Price, Place, and Promotion.",
                "3_breakdown": "It is called the Marketing function."
            }
        },
        {
            "prompt": "Which business function handles data processing, filing, record-keeping, and office communications?",
            "sample_answer": "Administration Function",
            "ideal_answer": "The Administration function.",
            "hint_sections": {
                "1_nudge": "Think about secretarial, clerical, and general office information management.",
                "2_concept": "This function collects, files, and retrieves critical documents and reports.",
                "3_breakdown": "It is called the Administration function."
            }
        },
        {
            "prompt": "Which business function sets organizational goals, formulates strategy, leads staff, and coordinates all other business activities?",
            "sample_answer": "General Management",
            "ideal_answer": "The General Management function.",
            "hint_sections": {
                "1_nudge": "Think about top executives and managers who guide the overall company direction.",
                "2_concept": "This function performs planning, organizing, leading, and controlling (POLC).",
                "3_breakdown": "It is called General Management."
            }
        },
        {
            "prompt": "Which business function is responsible for buying raw materials, machinery, and office supplies at the best quality and price?",
            "sample_answer": "Purchasing / Procurement Function",
            "ideal_answer": "The Purchasing or Procurement function.",
            "hint_sections": {
                "1_nudge": "Think about the department that orders goods from external suppliers.",
                "2_concept": "This function negotiates terms, delivery dates, and prices with vendors.",
                "3_breakdown": "It is called Purchasing or Procurement."
            }
        },
        {
            "prompt": "Which business function is responsible for creating a positive public image, handling media relations, and corporate social responsibility (CSR)?",
            "sample_answer": "Public Relations (PR) Function",
            "ideal_answer": "The Public Relations function.",
            "hint_sections": {
                "1_nudge": "Think about how a company communicates with the public, journalists, and local community.",
                "2_concept": "This function protects the business reputation and builds goodwill.",
                "3_breakdown": "It is called Public Relations (PR)."
            }
        }
    ]
    
    if seed is not None:
        q = questions[int(seed) % len(questions)]
    else:
        q = rng.choice(questions)
    
    item = {
        "id": f"ems9_bus_{rng.randint(1000, 9999)}",
        "topic": "Functions of a Business & Trade Unions",
        "question_type": "standard",
        "prompt": q["prompt"],
        "marks": 2,
        "sample_answer": q["sample_answer"],
        "ideal_answer": q["ideal_answer"],
        "marking_points": ["Correct identification of the function or role of trade unions."],
        "hint_sections": q["hint_sections"],
        "guidelines": ["Award full marks for clear understanding of the core concepts."],
        "teaching_note": "Learners should be able to name all 8 business functions."
    }
    return [_with_metadata(item, subskill='business_functions', learning_objective_id='lo_bus_func', question_family_id='bus_func_q', concept_id='bus_func', concept_group='business', diagnostic_tags=['semantic', 'ems'])]

def generate(subskill="business_functions", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_business_functions(rng, mode, seed=seed)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
