import os

phrases = [
    ("inclined_plane_newton", "Gr10 Vectors"),
    ("perpendicular to the principal axis at a distance", "Gr11 Optics"),
    ("In the circuit diagram represented below", "Gr11 Circuits"),
    ("consisting of a nickel (Ni) half-cell", "Gr11/12 Electrochemistry"),
    ("A constant net horizontal force of 400 N acts forward", "Gr12 Momentum"),
    ("moves horizontally along a rough surface. A constant pulling force of", "Gr12 Work Energy"),
]

for root, dirs, files in os.walk("caps-ai-backend/app/utils"):
    for f in files:
        if f.endswith(".py"):
            p = os.path.join(root, f)
            t = open(p, "r", encoding="utf-8", errors="ignore").read()
            for phrase, label in phrases:
                if phrase in t:
                    print(f"[{label}] Found in {p}")
