import sys
sys.path.insert(0, "caps-ai-backend")

from app.utils.mathematical_literacy import gr11_conversions_and_time_generator as conv

print("conv.SUBSKILLS count:", len(conv.SUBSKILLS) if hasattr(conv, "SUBSKILLS") else "No SUBSKILLS")
print("conv attributes with list:", [a for a in dir(conv) if isinstance(getattr(conv, a), (list, tuple)) and not a.startswith("__")])

# Test 10 generations and check what subskill IDs are emitted
emitted = set()
for i in range(52):
    q = conv.generate(seed=100 + i, archetype_index=i, count=1)[0]
    emitted.add(q.get("subskill"))

print("Emitted subskills count:", len(emitted))
print("Sample emitted:", list(emitted)[:5])
if hasattr(conv, "SUBSKILLS"):
    diff = emitted - set(conv.SUBSKILLS)
    print("Emitted not in conv.SUBSKILLS:", diff)
    diff2 = set(conv.SUBSKILLS) - emitted
    print("In conv.SUBSKILLS not emitted:", diff2)
