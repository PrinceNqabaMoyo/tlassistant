import sys
sys.path.insert(0, 'caps-ai-backend')

from app.utils.natural_sciences.ns8_particle_model_matter_generator import generate_particle_model_matter_questions
from app.utils.natural_sciences.ns8_energy_transfer_electrical_generator import generate_energy_transfer_questions
from app.utils.natural_sciences.ns8_telescopes_space_exploration_generator import generate_telescopes_questions

print("=== PARTICLE MODEL ===")
for s in range(15):
    q = generate_particle_model_matter_questions(count=1, seed=s)[0]
    ds = q.get('diagram_spec')
    dtype = ds.get('type') if ds else None
    sub = q.get('subskill')
    if dtype:
        print(f"seed {s}: subskill={sub}, type={dtype}")

print("\n=== ENERGY TRANSFER ===")
for s in range(15):
    q = generate_energy_transfer_questions(count=1, seed=s)[0]
    ds = q.get('diagram_spec')
    dtype = ds.get('type') if ds else None
    sub = q.get('subskill')
    if dtype:
        print(f"seed {s}: subskill={sub}, type={dtype}")

print("\n=== TELESCOPES ===")
for s in range(15):
    q = generate_telescopes_questions(count=1, seed=s)[0]
    ds = q.get('diagram_spec')
    dtype = ds.get('type') if ds else None
    sub = q.get('subskill')
    if dtype:
        print(f"seed {s}: subskill={sub}, type={dtype}")
