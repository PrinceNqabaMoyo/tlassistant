import sys
sys.path.insert(0, "caps-ai-backend")
from app.utils.grade10_life_sciences import cytology_mitosis_generator
import random

try:
    r = random.Random(42)
    q = cytology_mitosis_generator._build_organelle_drill(r)
    print("Success:", q.get("id"))
except Exception as e:
    print("Error in _build_organelle_drill:", e)
