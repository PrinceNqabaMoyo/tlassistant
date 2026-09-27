import random
import time
from typing import Any, Dict, List

TOPIC = 'grade10_waves_sound_light'

def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"

def generate(difficulty: str = "medium") -> List[Dict[str, Any]]:
    questions = []
    
    # Pillar 1: Transverse Waves
    freq = random.randint(2, 50)
    wavelength = round(random.uniform(0.1, 5.0), 1)
    velocity = round(freq * wavelength, 1)
    questions.append({
        'id': _make_id("waves_transverse"),
        'question_type': 'typed',
        'question': f"A transverse wave has a frequency of {freq} Hz and a wavelength of {wavelength} m. Calculate its speed in m/s.",
        'correct_answer': f"{velocity}".replace('.', ','),
        'explanation': f"v = f * lambda = {freq} * {wavelength} = {velocity} m/s",
    })

    # Pillar 2: Sound Echo
    dist = random.randint(50, 500)
    speed = 340
    t = round(2 * dist / speed, 2)
    questions.append({
        'id': _make_id("waves_echo"),
        'question_type': 'typed',
        'question': f"A person claps and hears the echo from a wall {dist} m away. If the speed of sound is {speed} m/s, how long did it take to hear the echo? Answer in s.",
        'correct_answer': f"{t}".replace('.', ','),
        'explanation': f"Delta x = v * Delta t / 2 => {dist} = 340 * t / 2 => t = {dist * 2 / 340:.2f} s.",
    })

    # Pillar 3: EM Radiation
    freq_em = random.randint(2, 9) * 10**14
    h = 6.63e-34
    E = h * freq_em
    questions.append({
        'id': _make_id("waves_em"),
        'question_type': 'mcq',
        'question': f"What is the energy of a photon with frequency {freq_em:.1e} Hz? (h = 6.63 x 10^-34 J.s)",
        'options': [f"{E:.2e} J", f"{E*2:.2e} J".replace('.', ','), f"{E/2:.2e} J".replace('.', ','), f"{(E/h):.2e} J".replace('.', ',')],
        'correct_answer': f"{E:.2e} J",
        'explanation': f"E = hf = (6.63 x 10^-34) * ({freq_em:.1e}) = {E:.2e} J",
    })
    
    # Just returning 3 as smoke test for authentic CAPS
    return questions
