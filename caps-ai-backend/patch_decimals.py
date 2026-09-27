import glob
import os

files = [
    "app/utils/grade10_physical_sciences/waves_sound_light_generator.py",
    "app/utils/grade10_physical_sciences/matter_materials_generator.py",
    "app/utils/grade11_physical_sciences/vectors_newton_generator.py",
    "app/utils/grade12_physical_sciences/vertical_projectile_generator.py",
    "app/utils/grade12_physical_sciences/doppler_effect_generator.py",
    "app/utils/life_sciences/meiosis_human_reproduction_generator.py"
]

for f in files:
    if os.path.exists(f):
        with open(f, 'r') as file:
            content = file.read()
        
        # simple hack to stringify and replace '.' with ','
        # but we shouldn't replace in python syntax, only in strings
        content = content.replace("f\"{velocity}\"", "f\"{velocity}\".replace('.', ',')")
        content = content.replace("f\"{t}\"", "f\"{t}\".replace('.', ',')")
        content = content.replace("f\"{dist * 2 / 340:.2f} s.\"", "f\"{dist * 2 / 340:.2f} s.\".replace('.', ',')")
        content = content.replace("f\"{E:.2e} J\"", "f\"{E:.2e} J\".replace('.', ',')")
        content = content.replace("f\"{E*2:.2e} J\"", "f\"{E*2:.2e} J\".replace('.', ',')")
        content = content.replace("f\"{E/2:.2e} J\"", "f\"{E/2:.2e} J\".replace('.', ',')")
        content = content.replace("f\"{(E/h):.2e} J\"", "f\"{(E/h):.2e} J\".replace('.', ',')")
        
        content = content.replace("f\"{n}\"", "f\"{n}\".replace('.', ',')")
        content = content.replace("f\"{conc}\"", "f\"{conc}\".replace('.', ',')")
        content = content.replace("f\"{fx}\"", "f\"{fx}\".replace('.', ',')")
        content = content.replace("f\"{fnet}\"", "f\"{fnet}\".replace('.', ',')")
        content = content.replace("f\"{t_max}\"", "f\"{t_max}\".replace('.', ',')")
        content = content.replace("f\"{h}\"", "f\"{h}\".replace('.', ',')")
        content = content.replace("f\"{fl}\"", "f\"{fl}\".replace('.', ',')")
        
        with open(f, 'w') as file:
            file.write(content)
