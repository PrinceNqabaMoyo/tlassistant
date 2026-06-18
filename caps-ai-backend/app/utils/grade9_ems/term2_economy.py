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

def _generate_price_theory(rng, mode):
    questions = [
        {
            "prompt": "According to the law of demand, what happens to the quantity demanded of a product when its price increases?",
            "sample_answer": "It decreases.",
            "ideal_answer": "The quantity demanded decreases.",
            "hint_sections": {
                "1_nudge": "Think about your own behavior as a consumer. Do you buy more or less when things get expensive?",
                "2_concept": "There is an inverse relationship between price and quantity demanded.",
                "3_breakdown": "When price goes up, people buy less. It decreases."
            }
        },
        {
            "prompt": "Which sector of the economy is concerned with the extraction of raw materials from nature?",
            "sample_answer": "Primary sector",
            "ideal_answer": "The primary sector.",
            "hint_sections": {
                "1_nudge": "Think about the 'first' step in production, like farming or mining.",
                "2_concept": "Sectors are primary, secondary, and tertiary. This is the foundation.",
                "3_breakdown": "The primary sector handles raw materials."
            }
        }
    ]
    
    q = rng.choice(questions)
    
    item = {
        "id": f"ems9_econ_{rng.randint(1000, 9999)}",
        "topic": "Price Theory & Sectors",
        "question_type": "standard",
        "prompt": q["prompt"],
        "marks": 2,
        "sample_answer": q["sample_answer"],
        "ideal_answer": q["ideal_answer"],
        "marking_points": ["Correct identification of the relationship or sector."],
        "hint_sections": q["hint_sections"],
        "guidelines": ["Award full marks for variations indicating decrease or primary."],
        "teaching_note": "Ensure learners understand the law of demand and supply separately."
    }
    return [_with_metadata(item, subskill='price_theory', learning_objective_id='lo_price_theory', question_family_id='econ_q', concept_id='price_theory', concept_group='economy', diagnostic_tags=['semantic', 'ems'])]

def generate(subskill="price_theory", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_price_theory(rng, mode)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
