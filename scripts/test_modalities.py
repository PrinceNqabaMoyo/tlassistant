import sys, os
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant

specs = [
    ("Physical Sciences", "11", "Electric circuits", "circuit"),
    ("Life Sciences", "12", "Genetics and inheritance", "punnett_square"),
    ("Natural Sciences", "9", "Cells as the basic units of life", "bio_diagram"),
    ("Physical Sciences", "11", "Vectors in two dimensions", "free_body_diagram"),
    ("Mathematics", "8", "Geometry of 3D objects", "geometric_nets"),
    ("Physical Sciences", "12", "Organic molecules", "organic_chemistry"),
    ("Physical Sciences", "12", "Electrodynamics", "electrodynamics"),
    ("Mathematics", "11", "Euclidean geometry", "diagram")
]

for subj, gr, top, expected_mod in specs:
    res = generate_variant(subject=subj, grade=gr, topic=top, seed=42)
    q = res[0] if isinstance(res, list) else res
    mod = q.get("modality")
    qid = q.get("id")
    has_target = (mod == expected_mod)
    print(f"[{subj} Gr{gr} - {top}] -> mod: '{mod}' (expected '{expected_mod}'), Match: {has_target}, id: {qid}")
