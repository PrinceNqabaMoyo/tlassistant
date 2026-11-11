with open('caps-ai-backend/app/utils/grade7_mathematics/geometric_nets_3d_generator.py', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if '"subskill":' in line:
            print(f"{i+1}: {line.strip()}")
