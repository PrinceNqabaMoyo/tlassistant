import requests

base = 'http://localhost:5001'
for step in range(3):
    r = requests.get(f'{base}/api/generate?subject=Mathematical+Literacy&grade=11&topic=Interest+banking+and+inflation&stage=diagnostic&diagnostic_step={step}&seed=101')
    q = r.json()['questions'][0]
    print(f"Step {step}: type={q.get('question_type')} modality={q.get('modality')} expected_ans={q.get('expected_answer')}")
    mr = requests.post(f'{base}/api/mark', json={
        'question_id': q.get('id'),
        'user_answer': q.get('expected_answer'),
        'subject': 'Mathematical Literacy',
        'grade': 11,
        'question': q
    })
    res = mr.json()
    print(f"Mark: is_correct={res.get('is_correct')} score={res.get('score')} max={res.get('max_score')}")
