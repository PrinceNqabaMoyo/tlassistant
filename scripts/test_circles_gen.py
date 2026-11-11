import sys
sys.path.insert(0, "caps-ai-backend")

from app.utils.technical_mathematics import circles_angular_movement_generator

q = circles_angular_movement_generator.generate(seed=42)
print("Keys:", q.keys())
print("Modality:", q.get("modality"))
print("Diagram spec:", q.get("diagram_spec"))
