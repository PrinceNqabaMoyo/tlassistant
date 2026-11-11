with open('caps-ai-backend/app/utils/grade10_mathematics/term_2/analytical_geometry_generator.py', 'rb') as f:
    data = f.read()
print(b"subskill\": \"distance_formula\"" in data)
idx = data.find(b"distance_formula")
print(repr(data[idx-50:idx+100]))
