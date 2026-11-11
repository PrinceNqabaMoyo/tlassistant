from pathlib import Path

p = Path("caps-ai-backend/app/utils/natural_sciences/term3_energy_change_forces_generator.py")
txt = p.read_text(encoding="utf-8")

old_text = '''        marks=7,
        modality="free_body_diagram",
        fbd_spec={
            "mass_kg": mass_kg,
            "angle_deg": 0,
            "forces": [
                {"name": "F_N", "label": "Normal Force (FN)", "magnitude": round(mass_kg * 9.8), "dir": "up"},
                {"name": "F_g", "label": "Weight (Fg)", "magnitude": round(mass_kg * 9.8), "dir": "down"}
            ]
        },
    )'''

new_text = '''        marks=7,
        modality="semantic",
    )'''

if old_text in txt:
    txt = txt.replace(old_text, new_text, 1)
    p.write_text(txt, encoding="utf-8")
    print("Replaced heat transfer fbd_spec with modality='semantic'")
else:
    print("old_text not found")
