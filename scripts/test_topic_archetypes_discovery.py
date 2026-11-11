import sys
from pathlib import Path

BACKEND_DIR = Path("caps-ai-backend")
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.services.generator_registry import get_topic_archetypes, resolve_generator_key

topics = [
    "Conversions and time",
    "Measuring length weight volume and temperature",
    "Personal income expenditure and budgets",
    "Banking interest and taxation",
    "Financial documents and tariff ystems",
    "Financial documents and tariff systems",
    "Numbers and calculations with numbers",
    "Data handling",
    "Scale maps and plans",
    "Assembly diagrams floor plans and packaging",
    "Measurement of perimeter and area",
    "Patterns relationships and representations",
    "Probability"
]

for t in topics:
    res_key = resolve_generator_key(t, grade="10", subject="Mathematical Literacy")
    arch_info = get_topic_archetypes(t, grade="10", subject="Mathematical Literacy")
    archs = arch_info.get("archetypes", [])
    print(f"Topic: '{t}' -> resolved_key: '{res_key}' -> count: {len(archs)}")
    print(f"   First 3 archs: {archs[:3]}")
