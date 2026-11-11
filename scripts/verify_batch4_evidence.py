import os

evs = [
    'curriculum_docs_auto/Mathematics_Gr9/Term 2/04. Geometry of 2D shapes.md',
    'curriculum_docs_auto/Mathematics_Gr10/Term 3/04. Euclidean geometry 1.md',
    'curriculum_docs_auto/Mathematics_Gr10/Term 3/04. Euclidean geometry 2.md',
    'curriculum_docs_auto/Mathematics_Gr12/Term 2/02. Analytical geometry.md',
]

for e in evs:
    print(f"{e}: {os.path.exists(e)}")
