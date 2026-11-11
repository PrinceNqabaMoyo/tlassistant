with open('caps-ai-backend/app/utils/grade9_mathematics/geometry_straight_lines_triangles_generator.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for l in lines[-35:]:
    print(l.rstrip().encode('ascii', 'replace').decode('ascii'))
