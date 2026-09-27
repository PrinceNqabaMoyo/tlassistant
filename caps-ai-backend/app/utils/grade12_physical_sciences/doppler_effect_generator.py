import random
import time
from typing import Any, Dict, List

TOPIC = 'grade12_doppler_effect'

def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"

def generate(difficulty: str = "medium") -> List[Dict[str, Any]]:
    questions = []
    
    v = 340
    fs = random.randint(500, 1500)
    vs = random.randint(10, 50)
    fl = round(v * fs / (v - vs), 1)
    
    questions.append({
        'id': _make_id("doppler_approach"),
        'question_type': 'typed',
        'question': f"An ambulance moves towards a stationary observer at {vs} m/s. The siren emits a frequency of {fs} Hz. Calculate the frequency heard by the observer. (v = {v} m/s)",
        'correct_answer': f"{fl}".replace('.', ','),
        'explanation': f"fL = [v / (v - vs)] * fS = [{v} / ({v} - {vs})] * {fs} = {fl} Hz",
    })
    
    return questions
