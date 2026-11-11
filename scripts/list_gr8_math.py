import json

with open("caps-ai-backend/app/services/caps_term_registry_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Data is {type(data)} with {len(data)} items")
if len(data) > 0:
    print("Item 0 keys:", list(data[0].keys()) if isinstance(data[0], dict) else type(data[0]))
    # Filter for grade 8 mathematics
    gr8 = [item for item in data if str(item.get("grade")) == "8" and item.get("subject") == "Mathematics"]
import sys
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant, get_topic_archetypes

print("=== Checking Grade 8 Mathematics Generator Status ===")
for idx, item in enumerate(gr8, 1):
    name = item.get('name')
    key = item.get('generator_key')
    try:
        res = get_topic_archetypes(topic=name, grade="8", subject="Mathematics")
        sub_list = res.get("archetypes", [])
        count = len(sub_list)
        status = f"{count} archetypes"
    except Exception as e:
        status = f"ERROR: {e}"
    print(f"{idx:2d}. [T{item.get('term')}] {name:<42} | key: {key:<45} | {status}")



