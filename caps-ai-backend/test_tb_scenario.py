import sys, random
sys.path.insert(0, r'caps-ai-backend')
from app.utils.sole_trader.trial_balance_structured import make_trial_balance_partial_completion_question

q = make_trial_balance_partial_completion_question(r=random.Random(10), difficulty='hard')
print(q.get('prompt', 'No prompt found'))
