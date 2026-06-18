import json
import sys
import os

# Add the backend to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'caps-ai-backend')))

from generators.bs_generator import generate_macro_environment_question
from generators.ems_generator import generate_needs_and_wants_question

def main():
    print("--- Testing EMS Needs vs Wants Generator ---")
    ems_q = generate_needs_and_wants_question()
    print(json.dumps(ems_q, indent=2))
    
    print("\n--- Testing BS Macro Environment Generator ---")
    bs_q = generate_macro_environment_question(assessment_type="activity")
    print(json.dumps(bs_q, indent=2))

if __name__ == "__main__":
    main()
