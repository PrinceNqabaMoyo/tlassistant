import sys
sys.path.insert(0, "caps-ai-backend")

from app.services.generator_registry import get_topic_archetypes, resolve_generator_key, ALL_GENERATORS

topic = "Conversions and time"
grade = "10"
subject = "Mathematical Literacy"

gen_key = resolve_generator_key(topic, grade=grade, subject=subject)
print("Resolved gen_key:", gen_key)
print("In ALL_GENERATORS?", gen_key in ALL_GENERATORS)

res = get_topic_archetypes(topic, grade=grade, subject=subject)
print("Result of get_topic_archetypes:", res)
