import os
import sys
import json
import random
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path("caps-ai-backend").resolve()))
from app.services.generator_registry import CURRICULUM_MANIFEST, generate_variant

diagram_matches = []
table_matches = []
drag_drop_matches = []

test_seeds = [42, 101, 202]

print("Scanning all 476 topics in CURRICULUM_MANIFEST for interactive modalities...")

sample_manifest = list(CURRICULUM_MANIFEST.items())

for (subject, grade, topic), gen_key in sample_manifest:
    
    # Generate question with seed 101
    try:
        qs = generate_variant(
            topic=topic,
            subskill="default",
            difficulty="medium",
            count=1,
            seed=101,
            grade=str(grade),
            subject=subject,
            extra_config={"mode": "auto", "stage": "practice"}
        )
        if not qs:
            continue
        q = qs[0]
        
        qtype = str(q.get("question_type", "")).lower()
        modality = str(q.get("modality", "")).lower()
        
        # 1. Diagram / Visual
        if (
            q.get("diagram_spec") or
            q.get("correct_edge") or
            qtype == "diagram_select" or
            modality == "diagram" or
            modality in ["geometric_nets", "electrodynamics", "organic_chemistry"]
        ):
            diagram_matches.append({
                "subject": subject,
                "grade": grade,
                "topic": topic,
                "type": qtype,
                "modality": modality or "diagram",
                "diagram_kind": q.get("diagram_spec", {}).get("kind") if isinstance(q.get("diagram_spec"), dict) else "special_3d"
            })
            
        # 2. Table Filling / Ledger
        if (
            modality == "ledger" or
            modality == "arithmetic_grid" or
            q.get("journal") or
            q.get("table_schema") or
            q.get("correct_map") or
            qtype in ["table_completion", "tabular_fill", "journal", "ledger"]
        ):
            table_matches.append({
                "subject": subject,
                "grade": grade,
                "topic": topic,
                "type": qtype,
                "modality": modality or "ledger",
                "rows_count": len(q.get("journal", {}).get("rows", [])) or len(q.get("table_schema", {}).get("rows", [])) or len(q.get("table", {}).get("rows", []))
            })
            
        # 3. Drag and Drop / Word Bank / Matching
        if (
            qtype in ["table_wordbank", "word_bank", "drag_and_drop", "matching_columns", "match"] or
            bool(q.get("word_bank"))
        ):
            drag_drop_matches.append({
                "subject": subject,
                "grade": grade,
                "topic": topic,
                "type": qtype,
                "word_bank_count": len(q.get("word_bank", []))
            })
            
    except Exception as e:
        continue

print(f"\n=======================================================")
print(f"INTERACTIVE QUESTION AVAILABILITY SURVEY")
print(f"=======================================================")
print(f"1. Topics with Interactive Diagram Specs / Selection: {len(diagram_matches)}")
for d in diagram_matches[:8]:
    print(f"   • Gr {d['grade']} {d['subject']}: '{d['topic']}' (kind: {d['diagram_kind']}, type: {d['type']})")
if len(diagram_matches) > 8:
    print(f"   ...and {len(diagram_matches) - 8} more topics")

print(f"\n2. Topics with Interactive Table Filling / Ledgers: {len(table_matches)}")
for t in table_matches[:10]:
    print(f"   • Gr {t['grade']} {t['subject']}: '{t['topic']}' (modality: {t['modality']}, type: {t['type']})")
if len(table_matches) > 10:
    print(f"   ...and {len(table_matches) - 10} more topics")

print(f"\n3. Topics with Word Bank / Tap-to-Place / Matching: {len(drag_drop_matches)}")
for w in drag_drop_matches[:8]:
    print(f"   • Gr {w['grade']} {w['subject']}: '{w['topic']}' (type: {w['type']}, tokens: {w['word_bank_count']})")
if len(drag_drop_matches) > 8:
    print(f"   ...and {len(drag_drop_matches) - 8} more topics")
