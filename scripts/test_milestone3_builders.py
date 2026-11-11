import sys, os, json
sys.path.insert(0, os.path.abspath('caps-ai-backend'))
from app.utils.life_sciences.sensory_reproductive_builders import build_eye_question

q = build_eye_question(42, 12)
print("diagram_meta:", json.dumps(q.get("diagram_meta"), indent=2))
