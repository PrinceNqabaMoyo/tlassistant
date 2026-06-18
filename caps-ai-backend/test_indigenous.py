import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from app import create_app

app = create_app()
with app.test_client() as client:
    response = client.post('/api/accounting/grade10/indigenous-bookkeeping/generate', 
                           json={"subskill": "informal_vs_formal", "difficulty": "easy", "question_type": "mixed", "count": 1})
    print("STATUS CODE:", response.status_code)
    print("RESPONSE:", response.get_data(as_text=True))
