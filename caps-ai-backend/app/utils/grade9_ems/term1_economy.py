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

def _generate_economic_systems(rng, mode):
    questions = [
        {
            "prompt": "Which economic system is characterized by private ownership of factors of production and profit motive?",
            "sample_answer": "Market Economy",
            "ideal_answer": "Market Economy",
            "hint_sections": {
                "1_nudge": "Think about systems where individuals and businesses make decisions, not the government.",
                "2_concept": "In this system, prices are determined by supply and demand.",
                "3_breakdown": "The correct term is Market Economy or Capitalism."
            }
        },
        {
            "prompt": "In a command economy, who makes the major economic decisions regarding what to produce and how to produce it?",
            "sample_answer": "The government / State",
            "ideal_answer": "The government or the state.",
            "hint_sections": {
                "1_nudge": "Think about a system where control is centralized.",
                "2_concept": "There is little to no private ownership; authorities plan everything.",
                "3_breakdown": "The government makes all economic decisions."
            }
        }
    ]
    
    q = rng.choice(questions)
    
    item = {
        "id": f"ems9_econ_{rng.randint(1000, 9999)}",
        "topic": "Economic Systems",
        "question_type": "standard",
        "prompt": q["prompt"],
        "marks": 2,
        "sample_answer": q["sample_answer"],
        "ideal_answer": q["ideal_answer"],
        "marking_points": ["Correct identification of the system or role."],
        "hint_sections": q["hint_sections"],
        "guidelines": ["Award full marks for variations like capitalism/market economy or state/government."],
        "teaching_note": "Ensure learners can distinguish between Market, Command, and Mixed economies."
    }
    return [_with_metadata(item, subskill='economic_systems', learning_objective_id='lo_econ_sys', question_family_id='econ_sys_q', concept_id='econ_sys', concept_group='economy', diagnostic_tags=['semantic', 'ems'])]

def generate(subskill="economic_systems", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_economic_systems(rng, mode)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
