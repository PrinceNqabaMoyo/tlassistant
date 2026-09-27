import json
from app.services.generator_registry import get_generator_for_topic

topics = [
    "waves sound and light",
    "matter and materials",
    "vectors and newtons laws",
    "vertical projectile motion",
    "doppler effect",
    "meiosis"
]

results = []
for topic in topics:
    try:
        gen = get_generator_for_topic(topic, grade=None, subject="Physical Sciences")
        if not gen:
            results.append(f"{topic}: GENERATOR NOT FOUND")
            continue
        
        q = gen(difficulty="medium")
        results.append(f"{topic}: SUCCESS ({len(q)} questions)")
    except Exception as e:
        results.append(f"{topic}: FAILED - {str(e)}")

for r in results:
    print(r)
