import random
import time
from typing import Any, Dict, List

TOPIC = 'grade10_matter_materials'

def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"

def generate(difficulty: str = "medium") -> List[Dict[str, Any]]:
    questions = []
    
    mass = random.randint(10, 100)
    molar_mass = random.choice([12, 16, 44, 58.5, 98])
    n = round(mass / molar_mass, 2)
    questions.append({
        'id': _make_id("matter_mole"),
        'question_type': 'typed',
        'question': f"Calculate the number of moles in {mass} g of a substance with molar mass {molar_mass} g/mol.",
        'correct_answer': f"{n}".replace('.', ','),
        'explanation': f"n = m/M = {mass} / {molar_mass} = {n} mol",
    })

    vol = random.randint(1, 10)
    n2 = random.randint(1, 5)
    conc = round(n2 / vol, 2)
    questions.append({
        'id': _make_id("matter_conc"),
        'question_type': 'typed',
        'question': f"A solution contains {n2} moles in {vol} dm^3. Calculate its concentration in mol/dm^3.",
        'correct_answer': f"{conc}".replace('.', ','),
        'explanation': f"c = n/V = {n2} / {vol} = {conc} mol/dm^3",
    })
    
    return questions
