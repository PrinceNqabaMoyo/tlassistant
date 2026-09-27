import random
import time
import math
from typing import Any, Dict, List

TOPIC = 'grade11_vectors_newton'

def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"

def generate(difficulty: str = "medium") -> List[Dict[str, Any]]:
    questions = []
    
    f1 = random.randint(10, 50)
    theta = random.randint(10, 80)
    fx = round(f1 * math.cos(math.radians(theta)), 2)
    questions.append({
        'id': _make_id("vec_components"),
        'question_type': 'typed',
        'question': f"A force of {f1} N acts at {theta} degrees above the horizontal. Calculate its horizontal component in N.",
        'correct_answer': f"{fx}".replace('.', ','),
        'explanation': f"Fx = F cos(theta) = {f1} * cos({theta}) = {fx} N",
    })

    mass = random.randint(2, 20)
    accel = random.randint(1, 5)
    fnet = mass * accel
    questions.append({
        'id': _make_id("vec_newton"),
        'question_type': 'typed',
        'question': f"An object of mass {mass} kg accelerates at {accel} m/s^2. Calculate the net force acting on it in N.",
        'correct_answer': f"{fnet}".replace('.', ','),
        'explanation': f"Fnet = ma = {mass} * {accel} = {fnet} N",
    })
    
    return questions
