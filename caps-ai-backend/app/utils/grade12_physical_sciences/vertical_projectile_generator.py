import random
import time
from typing import Any, Dict, List

TOPIC = 'grade12_vertical_projectile'

def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"

def generate(difficulty: str = "medium") -> List[Dict[str, Any]]:
    questions = []
    
    g = 9.8
    vi = random.randint(10, 40)
    t_max = round(vi / g, 2)
    questions.append({
        'id': _make_id("proj_maxheight"),
        'question_type': 'typed',
        'question': f"A ball is thrown vertically upwards at {vi} m/s. Calculate the time taken to reach maximum height in s. (Use g = 9.8 m/s^2, ignore air resistance)",
        'correct_answer': f"{t_max}".replace('.', ','),
        'explanation': f"vf = vi + g*t => 0 = {vi} - 9.8*t => t = {vi} / 9.8 = {t_max} s",
    })

    h = round((vi**2) / (2 * g), 2)
    questions.append({
        'id': _make_id("proj_hmax"),
        'question_type': 'typed',
        'question': f"A ball is thrown vertically upwards at {vi} m/s. Calculate the maximum height reached in m. (Use g = 9.8 m/s^2)",
        'correct_answer': f"{h}".replace('.', ','),
        'explanation': f"vf^2 = vi^2 + 2g Delta y => 0 = {vi}^2 - 2(9.8) Delta y => Delta y = {vi}^2 / 19.6 = {h} m",
    })
    
    return questions
