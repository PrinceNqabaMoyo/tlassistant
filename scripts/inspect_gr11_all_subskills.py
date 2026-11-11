import sys
import importlib
sys.path.insert(0, "caps-ai-backend")

modules = [
    ("conversions", "gr11_conversions_and_time_generator"),
    ("patterns", "gr11_patterns_relationships_generator"),
    ("plans", "gr11_plans_representations_generator"),
    ("data_handling", "gr11_data_handling_generator"),
    ("maps", "gr11_maps_generator"),
]

for name, mod_name in modules:
    mod = importlib.import_module("app.utils.mathematical_literacy." + mod_name)
    subs = getattr(mod, "SUBSKILLS", [])
    print(f"\n--- {mod_name} ---")
    print(f"SUBSKILLS count: {len(subs)}")
    emitted = []
    for i in range(min(5, len(subs))):
        q = mod.generate(seed=100 + i, archetype_index=i, count=1)[0]
        emitted.append((subs[i], q.get("subskill")))
    print("Mapping (chosen vs emitted):", emitted)
