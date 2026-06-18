from app.api.grade11_business_studies import generate_questions

samples = {
    'concepts': generate_questions(
        'grade11_bs_challenges_of_the_business_environments',
        'concepts',
        'medium',
        count=2,
        config={},
    ),
    'application': generate_questions(
        'grade11_bs_challenges_of_the_business_environments',
        'application',
        'medium',
        count=1,
        config={
            'question_family_id': 'challenge_classification_from_scenario',
            'retry_variant': 'guided',
        },
    ),
    'discussion': generate_questions(
        'grade11_bs_challenges_of_the_business_environments',
        'discussion',
        'medium',
        count=1,
        config={
            'question_family_id': 'macro_environment_challenges_discussion',
            'retry_variant': 'core',
        },
    ),
}

for label, questions in samples.items():
    print(label, len(questions))
    for question in questions:
        print({
            'subskill': question.get('subskill'),
            'question_family_id': question.get('question_family_id'),
            'scenario_family_id': question.get('scenario_family_id'),
            'retry_variant': question.get('retry_variant'),
            'question_type': question.get('question_type'),
        })
