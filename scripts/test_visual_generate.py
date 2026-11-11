import urllib.request
import urllib.parse
import json

test_configs = [
    ('Physical Sciences', '10', 'Electric circuits'),
    ('Life Sciences', '12', 'Genetics and inheritance'),
    ('Life Sciences', '10', 'The basic units of life'),
    ('Physical Sciences', '11', "Newton's laws and application of Newton's laws"),
    ('Mathematics', '9', 'Geometry of 3D objects'),
    ('Physical Sciences', '12', 'Organic molecules'),
    ('Physical Sciences', '12', 'Electrodynamics'),
    ('Mathematics', '11', 'Euclidean geometry')
]

for subj, gr, top in test_configs:
    url = f"http://127.0.0.1:5001/api/generate?subject={urllib.parse.quote(subj)}&grade={gr}&topic={urllib.parse.quote(top)}&count=1&seed=42"
    try:
        req = urllib.request.urlopen(url)
        data = json.loads(req.read().decode())
        q = data.get('questions', [{}])[0]
        mod = q.get('modality')
        qid = q.get('id')
        specs = [k for k in q.keys() if 'spec' in k]
        print(f"[{subj} Gr{gr} - {top}] -> modality: {mod}, id: {qid}, specs: {specs}")
    except Exception as e:
        print(f"[{subj} Gr{gr} - {top}] -> ERROR: {e}")
