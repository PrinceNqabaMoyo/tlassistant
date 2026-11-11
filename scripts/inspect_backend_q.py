import urllib.request, json

url = 'http://127.0.0.1:5001/api/generate?subject=life_sciences&grade=12&topic=Human+responses+to+the+environment&subskill=human_eye_structure&seed=42'
with urllib.request.urlopen(url) as r:
    data = json.loads(r.read())
    q = data['questions'][0]
    for k, v in q.items():
        if k not in ['solution_steps']:
            print(f"{k}: {v}")
