import random
import time
from typing import Any, Dict, List

TOPIC = 'life_sciences_meiosis_human_reproduction'

def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"

def generate(difficulty: str = "medium") -> List[Dict[str, Any]]:
    questions = []
    
    questions.append({
        'id': _make_id("meiosis_cross"),
        'question_type': 'mcq',
        'question': "During which phase of meiosis does crossing over occur?",
        'options': ["Prophase I", "Metaphase I", "Prophase II", "Anaphase I"],
        'correct_answer': "Prophase I",
        'explanation': "Crossing over occurs during Prophase I, leading to genetic variation.",
    })
    
    questions.append({
        'id': _make_id("meiosis_hormone"),
        'question_type': 'mcq',
        'question': "Which hormone is responsible for ovulation in the human menstrual cycle?",
        'options': ["Luteinizing Hormone (LH)", "Follicle Stimulating Hormone (FSH)", "Oestrogen", "Progesterone"],
        'correct_answer': "Luteinizing Hormone (LH)",
        'explanation': "A surge in LH triggers ovulation, usually around day 14 of the menstrual cycle.",
    })
    
    return questions
