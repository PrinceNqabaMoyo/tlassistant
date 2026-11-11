with open('caps-ai-backend/app/utils/grade10_mathematics/_math_common.py', 'r', encoding='utf-8') as f:
    c = f.read()
print("has diagram_spec in gr10 _math_common:", "diagram_spec" in c)
print("has modality in gr10 _math_common:", "modality" in c)
