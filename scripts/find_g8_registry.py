with open('caps-ai-backend/app/services/generator_registry.py', encoding='utf-8') as f:
    text = f.read()
import re
for m in re.finditer(r'\(["\'](mathematics|economic_management_sciences|natural_sciences)["\'],\s*["\'](8|grade-8)["\'],\s*["\']([^"\']+)["\']\)', text):
    print(m.group(0))
