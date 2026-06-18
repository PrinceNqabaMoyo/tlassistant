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

def _generate_business_functions(rng, mode):
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
            "prompt": "What is the primary role of a Trade Union in the workplace?",
            "sample_answer": "To protect and advance the rights of workers.",
            "ideal_answer": "To protect the rights and interests of workers and negotiate with employers.",
            "hint_sections": {
                "1_nudge": "Think about an organization that employees join to have a stronger voice.",
                "2_concept": "They negotiate for better pay, safer working conditions, and job security.",
                "3_breakdown": "They protect workers' rights."
            }
        }
    ]
    
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
    pool = _generate_business_functions(rng, mode)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
