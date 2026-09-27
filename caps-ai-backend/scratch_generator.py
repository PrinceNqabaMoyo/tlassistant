import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

waves = r'''
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
        'correct_answer': f"{velocity}",
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
        'correct_answer': f"{t}",
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
        'options': [f"{E:.2e} J", f"{E*2:.2e} J", f"{E/2:.2e} J", f"{(E/h):.2e} J"],
        'correct_answer': f"{E:.2e} J",
        'explanation': f"E = hf = (6.63 x 10^-34) * ({freq_em:.1e}) = {E:.2e} J",
    })
    
    # Just returning 3 as smoke test for authentic CAPS
    return questions
'''

matter = r'''
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
        'correct_answer': f"{n}",
        'explanation': f"n = m/M = {mass} / {molar_mass} = {n} mol",
    })

    vol = random.randint(1, 10)
    n2 = random.randint(1, 5)
    conc = round(n2 / vol, 2)
    questions.append({
        'id': _make_id("matter_conc"),
        'question_type': 'typed',
        'question': f"A solution contains {n2} moles in {vol} dm^3. Calculate its concentration in mol/dm^3.",
        'correct_answer': f"{conc}",
        'explanation': f"c = n/V = {n2} / {vol} = {conc} mol/dm^3",
    })
    
    return questions
'''

vectors = r'''
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
        'correct_answer': f"{fx}",
        'explanation': f"Fx = F cos(theta) = {f1} * cos({theta}) = {fx} N",
    })

    mass = random.randint(2, 20)
    accel = random.randint(1, 5)
    fnet = mass * accel
    questions.append({
        'id': _make_id("vec_newton"),
        'question_type': 'typed',
        'question': f"An object of mass {mass} kg accelerates at {accel} m/s^2. Calculate the net force acting on it in N.",
        'correct_answer': f"{fnet}",
        'explanation': f"Fnet = ma = {mass} * {accel} = {fnet} N",
    })
    
    return questions
'''

proj = r'''
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
        'correct_answer': f"{t_max}",
        'explanation': f"vf = vi + g*t => 0 = {vi} - 9.8*t => t = {vi} / 9.8 = {t_max} s",
    })

    h = round((vi**2) / (2 * g), 2)
    questions.append({
        'id': _make_id("proj_hmax"),
        'question_type': 'typed',
        'question': f"A ball is thrown vertically upwards at {vi} m/s. Calculate the maximum height reached in m. (Use g = 9.8 m/s^2)",
        'correct_answer': f"{h}",
        'explanation': f"vf^2 = vi^2 + 2g Delta y => 0 = {vi}^2 - 2(9.8) Delta y => Delta y = {vi}^2 / 19.6 = {h} m",
    })
    
    return questions
'''

doppler = r'''
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
        'correct_answer': f"{fl}",
        'explanation': f"fL = [v / (v - vs)] * fS = [{v} / ({v} - {vs})] * {fs} = {fl} Hz",
    })
    
    return questions
'''

meiosis = r'''
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
'''

base_path = "c:/Users/princ/fundile-tlassistant-vite/caps-ai-backend/app/utils"

write_file(f"{base_path}/grade10_physical_sciences/waves_sound_light_generator.py", waves)
write_file(f"{base_path}/grade10_physical_sciences/matter_materials_generator.py", matter)
write_file(f"{base_path}/grade11_physical_sciences/vectors_newton_generator.py", vectors)
write_file(f"{base_path}/grade12_physical_sciences/vertical_projectile_generator.py", proj)
write_file(f"{base_path}/grade12_physical_sciences/doppler_effect_generator.py", doppler)
write_file(f"{base_path}/life_sciences/meiosis_human_reproduction_generator.py", meiosis)

print("Files generated successfully!")
